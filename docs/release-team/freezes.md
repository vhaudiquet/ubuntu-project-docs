(freezes)=
# Freezes

This article provides an overview of the stabilization freezes that lead to
the release of a new version of Ubuntu. The series of freezes means
the gradual introduction of restrictions on modifications in certain areas, so
that the distribution can stabilize as it nears the final release.

See {ref}`release-cycle` for an overview of the entire release process.


(debian-import-freeze)=
## Debian Import Freeze

**Prior** to the Debian Import Freeze date, new versions of packages are
automatically imported from Debian's `unstable` branch (where they have not been
customized for Ubuntu). Entirely new packages (those not in Ubuntu at all) are
also automatically imported.

The import is done by copying the source package verbatim from Debian and
building fresh binary packages on the Ubuntu autobuilders.

**After** the Debian Import Freeze date, the Release Team disables the
automatic import of new packages and versions from Debian. The import of a new
package (or package version) from Debian after the Debian Import Freeze must be
explicitly requested by a developer.

If the package needs to be modified for Ubuntu, or is not in Debian, then a
developer can still upload it directly.

```{admonition} Historical note
:class: tip
For some LTS release (12.04 and lower) imports were done from `testing`, but
since the introduction of {ref}`proposed-migration`, syncs happen from
`unstable` all the time. 
```


(feature-freeze)=
## Feature Freeze

During Feature Freeze (FF), Ubuntu developers stop introducing new features,
packages, and {term}`API`/{term}`ABI` changes, and instead concentrate on fixing
bugs in the current release in development (`devel`).

It is possible to apply for {ref}`exceptions <freeze-exceptions>` under some
circumstances -- such exceptions must be approved by the Ubuntu Release Team.

```{note}
The general development activity is still unrestricted until the Feature Freeze;
however, the Feature Freeze is often scheduled for the same day.
```


(user-interface-freeze)=
## User Interface Freeze

The user interface (UI) should be finalized to allow documentation writers and
translators to work on a consistent target that doesn't render screenshots or
documentation obsolete.

After the User Interface Freeze (UIF), the following things are not allowed to
change without a {ref}`freeze exception <freeze-exceptions>`:

* User Interface of individual applications installed by default
* Appearance of the Desktop
* Distribution-specific artwork
* All user-visible strings in the Desktop and applications installed by default


(documentation-string-freeze)=
## Documentation String Freeze

At this point, documentation strings should no longer be created or changed.
This freeze ensures the documentation can be accurately translated.

Exceptions to this rule may be considered before the release for significant and
glaring errors or exceptional circumstances.

A string change must be discussed (and approved) on the
[`ubuntu-doc` mailing list](mailto:ubuntu-doc@lists.ubuntu.com). If a string is
changed after the freeze, it must be communicated to the translators (by writing
to the `ubuntu-translators` mailing list) *with enough time to update the
translations before the
{ref}`translation freeze <non-language-pack-translation-deadline>`*.

After release, any fixes must comply with the {ref}`stable-release-updates`
process, and where necessary must be accompanied by translations before
uploading. 


(kernel-feature-freeze)=
## Kernel Feature Freeze

The {term}`kernel` feature development should end at this point, and the kernels
can be considered feature-complete for the release. From now on, only bug-fix
changes are expected.

```{note}
The Kernel Feature Freeze occurs after the {ref}`feature-freeze` because the
Linux Kernel is typically released upstream after the Feature Freeze.
Additionally, the Kernel Feature Freeze is deliberately scheduled so that the
Beta images have a fully featured kernel suitable for testing.
```


(hardware-enablement-freeze)=
## Hardware Enablement Freeze

All new hardware enablement tasks for devices targeting the given release should
be finished, and all the respective packages should be in the Ubuntu Package
Archive. The Release Team no longer accepts changes in the Ubuntu Package
Archive related to supporting new image types or platforms. This freeze ensures
that any new platforms are already available for testing of the beta images and
in the weeks leading to the {ref}`final-freeze`.

```{note}
The Hardware Enablement Freeze is usually scheduled for the same day as the Beta
Freeze.
```

(beta-freeze)=
## Beta Freeze

In preparation for the beta release, all uploads are queued and subject to
manual approval by the Release Team.

**Before** Beta Freeze, all uploads enter the Archive without any approval.

**After** the Beta Freeze date, any changes to packages that will affect beta
release images (i.e. seeded packages) require the Release Team's approval
because they've entered the unapproved queue after uploading.

Uploads for packages that do *not* affect beta release images (un-seeded
packages) will still be auto-accepted until {ref}`final-freeze`. So be
careful with what you upload.

```{tip}
Use the {manpage}`seeded-in-ubuntu(1)` tool, provided by the `ubuntu-dev-tools`
package, to list all current daily images containing a specified package or to
determine whether the specified package is seeded or not.
```

This freeze allows the Release Team to fix package inconsistencies or critical
bugs quickly and in an isolated manner. Once the beta release is shipped, we
roll back to {ref}`feature-freeze` and {ref}`user-interface-freeze` status.


(kernel-freeze)=
## Kernel Freeze

The Kernel Freeze is the final date for kernel updates because they require
several lockstep actions that must be folded into the image-building process.

Exceptional circumstances may justify exemptions to the freeze at the discretion
of the Release Team.


(non-language-pack-translation-deadline)=
## Non-language-pack translation deadline

Some translation data cannot currently be updated via the language pack
mechanism. Because these items require more disruptive integration work, they
are subject to an earlier deadline to give developers time to manually export
translations from Launchpad and integrate them into the package.

This deadline marks the date after which translations for such packages are not
guaranteed to be included in the final release. Depending on the package and its
maintainers' workflow, they may be exported later.

```{note}
The [wiki page](https://wiki.ubuntu.com/NonLanguagePackTranslationDeadline)
lists the packages this affects: do we want to include this?
```

Other packages can still be translated until the
{ref}`language-pack-translation-deadline`.


(language-pack-translation-deadline)=
## Language pack translation deadline

Translations done up until this date are included in the final release's
language packs. See the
[language pack creation schedule](https://dev.launchpad.net/Translations/LanguagePackSchedule)
for more.


(final-freeze)=
## Final Freeze

This freeze marks an **extremely** high-caution period until the
{ref}`final-release`. Only bug fixes for release-critical, security-critical or
otherwise "exceptional circumstance" bugs are included in the Final Release,
which the Release Team and (and the relevant team looking after the package)
must confirm.


### Unseeded packages

Packages in {ref}`archive-components-universe` that aren't seeded in any of the
Ubuntu flavours remain in {ref}`feature-freeze` because they do not affect
the release; however, when the Ubuntu Package Archive is frozen, fixes must be
manually reviewed and accepted by the Release Team members.

When the Final Release is close (~2 days out), developers should consider
uploading to the {ref}`-proposed pocket <archive-pockets-proposed>`, from which
the Release Team cherry-picks into the
{ref}`-release pocket <archive-pockets-release>` if circumstances allow. All
packages uploaded to the `-proposed` pocket that do not make it into the
`-release` pocket until the Final Release become candidates for
{ref}`stable-release-updates`. Therefore, uploads to the `-proposed` pocket
during Final Freeze should meet the requirements of Stable Release Updates if
the upload is not accepted into the `-release` pocket. In particular, the upload
must reference at least one bug, which is used to track the stable update.


(release-candidate)=
## Release Candidate

The images produced on the Monday of the release week before
{ref}`final-release` are considered "release candidates".

In an ideal world, the first release candidate would end up being the Final
Release; however, we don't live in a perfect world, and this week is used to
get rid of the last release-critical bugs and do as much testing as possible.

Until the Final Release, changes are only permitted at the Release Team's
discretion and will only be allowed for high-priority bugs that might justify
delaying the release.


## Further reading

- {ref}`freeze-exceptions`
- {ref}`request-a-freeze-exception`
