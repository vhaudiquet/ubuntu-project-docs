"""
The ``.. railroad`` directive is a custom directive to generate rail-road
diagrams with the excellent `railroad-diagrams`_ library. The content of the
directive will be executed as Railroad Diagrams script using the Python version
of the library.

The directive has one required argument which will be the stem of the filename
for all generated images. The options that may be specified under the directive
are as follows:

TODO

For example::

    .. railroad::

        Sequence(
            NonTerminal('Comparison'),
            ZeroOrMore(
                Sequence(Choice('and', 'or'), NonTerminal('Comparison'))
            )
        )

.. _railroad-diagrams: https://github.com/tabatkins/railroad-diagrams
"""

from __future__ import annotations

import ast
import logging
from pathlib import Path
from hashlib import sha1
from itertools import chain
from importlib import util, resources

from typing import TYPE_CHECKING, Any

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.application import Sphinx
from sphinx.util.nodes import set_source_info
from sphinx.util.docutils import SphinxDirective
from sphinx.util.i18n import search_image_for_language

if TYPE_CHECKING:
    from typing import ClassVar, Any
    from sphinx.util.typing import ExtensionMetadata, OptionSpec
    from sphinx.writers.html5 import HTML5Translator
    from sphinx.writers.latex import LaTeXTranslator
    from sphinx.writers.manpage import ManualPageTranslator
    from sphinx.writers.texinfo import TexinfoTranslator
    from sphinx.writers.text import TextTranslator

logger = logging.getLogger(__name__)


class railroad(nodes.General, nodes.Inline, nodes.Element):
    pass


def figure_wrapper(
    directive: SphinxDirective, node: railroad, caption: str
) -> nodes.figure:
    figure_node = nodes.figure('', node)
    if 'align' in node:
        figure_node['align'] = node.attributes.pop('align')

    inodes, messages = directive.parse_inline(caption)
    caption_node = nodes.caption(caption, '', *inodes)
    caption_node.extend(messages)
    set_source_info(directive, caption_node)
    figure_node += caption_node
    return figure_node


def align(argument):
    return directives.choice(argument, ('left', 'center', 'right'))


class RailroadDirective(SphinxDirective):
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    option_spec: ClassVar[OptionSpec] = {
        # Directive options for the enclosing figure
        'alt': directives.unchanged,
        'align': align,
        'caption': directives.unchanged,
        'name': directives.unchanged,
        'class': directives.class_option,
    }

    def run(self) -> list[nodes.Node]:
        document = self.state.document
        if self.arguments:
            if self.content:
                return [
                    document.reporter.error(
                        'railroad directive cannot have both content and a '
                        'filename argument', line=self.lineno)
                ]
            argument = search_image_for_language(self.arguments[0], self.env)
            rel_filename, filename = self.env.relfn2path(argument)
            self.env.note_dependency(rel_filename)
            try:
                with open(filename, encoding='utf-8') as fp:
                    rr_code = fp.read()
            except OSError:
                return [
                    document.reporter.error(
                        'External railroad file %r not found or '
                        'reading it failed', line=self.lineno)
                ]
        else:
            rr_code = '\n'.join(self.content)
            rel_filename = None
            if not rr_code.strip():
                return [
                    document.reporter.warning(
                        'Ignoring "railroad" directive without content',
                        line=self.lineno)
                ]

        node = railroad()
        node['code'] = rr_code
        node['options'] = {
            # Why is docname here? Do we need the output filename different for
            # each document the diagram is included within?
            'docname': self.env.docname,
        }

        if 'alt' in self.options:
            node['alt'] = self.options['alt']
        if 'align' in self.options:
            node['align'] = self.options['align']
        if 'class' in self.options:
            node['classes'] = self.options['class']

        if 'caption' in self.options:
            figure = figure_wrapper(self, node, self.options['caption'])
            self.add_name(figure)
            return [figure]
        else:
            self.add_name(node)
            return [node]


# Copy doc-string for the class from the module
RailroadDirective.__doc__ = __doc__


def check_railroad(code: str) -> ast.AST:
    """
    A crude attempt at checking the code in the body of a railroad directive
    is vaguely sane.
    """
    try:
        node = ast.parse(code, '<string>', 'eval')
    except SyntaxError as exc:
        raise ValueError(str(exc)) from None
    else:
        if not (
            isinstance(node, ast.Expression) and
            isinstance(node.body, ast.Call) and
            isinstance(node.body.func, ast.Name) and
            node.body.func.id == 'Diagram'
        ):
            raise ValueError(f'expected Diagram() at the top of {code!r}')
    return node


_rr_spec = None
def custom_railroad(config):
    # This janky implementation is because railroad relies on global module
    # variables for most of its configuration. To permit parallel operation
    # and the (future) ability to customize individual diagrams we import a
    # "fresh" copy of the railroad module for each diagram generated, applying
    # the requested customizations to its "global" variables
    global _rr_spec
    if _rr_spec is None:
        _rr_spec = util.find_spec('railroad')
    rr_module = util.module_from_spec(_rr_spec)
    _rr_spec.loader.exec_module(rr_module)

    css = []
    if config.railroad_style:
        css.append(resources.read_text(__name__, f'{config.railroad_style}.css'))
    if config.railroad_css:
        if css:
            css.append('')
        css.append(config.railroad_css)

    rr_module.DEFAULT_STYLE = '\n'.join(css)
    rr_module.VS = config.railroad_vertical_sep
    rr_module.AR = config.railroad_arc_radius
    rr_module.INTERNAL_ALIGNMENT = config.railroad_internal_alignment
    rr_module.CHAR_WIDTH = config.railroad_char_width
    rr_module.COMMENT_CHAR_WIDTH = config.railroad_comment_char_width
    rr_module.STROKE_ODD_PIXEL_LENGTH = config.railroad_stroke_odd_pixel_length
    return rr_module


def render_railroad(
    self: HTML5Translator | LaTeXTranslator | TexinfoTranslator,
    code: str,
    options: dict[str, Any],
    format: str,
    prefix: str = 'railroad',
) -> tuple[Path | None, Path | None]:
    """
    Render railroad diagram into an SVG output file. Returns a tuple of
    (relative filename, output filename).
    """
    hash_key = ''.join((code, repr(options))).encode()
    hash_value = sha1(hash_key, usedforsecurity=False).hexdigest()
    fn = f'{prefix}-{hash_value}.{format}'
    rel_fn = Path(self.builder.imgpath, fn)
    out_fn = self.builder.outdir / self.builder.imagedir / fn

    if out_fn.is_file():
        return rel_fn, out_fn

    rr = custom_railroad(self.builder.config)
    code_obj = compile(check_railroad(code), '<string>', 'eval')
    diagram = eval(code_obj, {}, vars(rr))
    out_fn.parent.mkdir(parents=True, exist_ok=True)
    with out_fn.open('w') as fp:
        diagram.writeStandalone(fp.write)

    return rel_fn, out_fn


def render_rr_html(
    self: HTML5Translator,
    node: railroad,
    code: str,
    options: dict[str, Any],
    prefix: str = 'railroad',
    imgcls: str | None = None,
    alt: str | None = None,
) -> tuple[str, str]:
    try:
        fn, out_fn = render_railroad(self, code, options, 'svg', prefix)
    except ValueError as exc:
        logger.warning('railroad code %r: %s', code, exc)
        raise nodes.SkipNode from exc

    classes = ' '.join(
        cls for cls in chain([imgcls, 'railroad'], node.get('classes', []))
        if cls
    )

    if fn is None:
        self.body.append(self.encode(code))
    else:
        src = fn.as_posix()
        if alt is None:
            alt = node.get('alt', self.encode(code).strip())
        if 'align' in node:
            align = node['align']
            self.body.append(f'<div align="{align}" class="align-{align}">\n')
        self.body.append('<div class="railroad">')
        if self.builder.config.railroad_output_tag == 'img':
            self.body.append(f'<img src="{src}" alt="{alt}" class="{classes}" />')
        elif self.builder.config.railroad_output_tag == 'object':
            self.body.append(
                f'<object data="{src}" type="image/svg+xml" class="{classes}">')
            self.body.append(
                f'<p class="warning">{alt}</p>')
            self.body.append('</object>')
        else:
            logger.warning('railroad_output_tag must be "img" or "object"')
            raise nodes.SkipNode
        self.body.append('</div>\n')
        if 'align' in node:
            self.body.append('</div>\n')

    raise nodes.SkipNode


def html_visit_railroad(self: HTML5Translator, node: railroad) -> None:
    render_rr_html(self, node, node['code'], node['options'])


def setup(app: Sphinx) -> ExtensionMetadata:
    "Called by Sphinx to install the extension"
    app.add_node(
        railroad,
        html=(html_visit_railroad, None),
    )
    app.add_directive('railroad', RailroadDirective)
    app.add_config_value('railroad_output_format', 'svg', 'html', types=[str])
    app.add_config_value('railroad_output_tag', 'img', 'html', types=[str])
    app.add_config_value('railroad_style', '', 'html', types=[str])
    app.add_config_value('railroad_css', '', 'html', types=[str])
    app.add_config_value('railroad_vertical_sep', 8, 'env')
    app.add_config_value('railroad_arc_radius', 10, 'env')
    app.add_config_value('railroad_internal_alignment', 'center', 'env')
    app.add_config_value('railroad_char_width', 8.5, 'env', types=Any)
    app.add_config_value('railroad_comment_char_width', 7.0, 'env', types=Any)
    app.add_config_value(
        'railroad_stroke_odd_pixel_length', True, 'env', types=[bool])

    return {
        'version': '0.1',
        'parallel_read_safe': True,
    }
