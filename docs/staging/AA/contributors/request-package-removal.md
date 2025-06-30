(request-package-removal)
# How to request a package removal

```{note}
This page will be moved to:
* Contributors -> Advanced
```

Packages that are removed from Debian are semi-automatically removed from
Ubuntu `universe` on a regular basis by the Archive Admin team. However, packages
are not removed from Ubuntu `main` without an explicit request, and nor are
packages which originated elsewhere.

## The removal request

To request removal of a package, file a bug against the package. The bug must
have the following elements:

* The release to remove it from

* What source and binary packages you expect to be removed

* A rationale for why they should be removed. Examples:

  * E.g: In Noble please remove bin:foo-oldcrap from src:foo as it blocks migration of the new version which is no more building it

  * E.g: In questing please remove src:bar and all of its binaries, they are dysfunctional in that release XX, because …

  * E.g: In plucky please remove src:foobar and all of its binaries, they block the transition of snafu and foobar upstream is orphaned and won’t be updated to work with the new versions of the overall stack

* Confirmation that the binary packages have no `reverse-depends` (no other package
  depends on them). To do so, check the instructions in {ref}`aa-check-dependencies-before-removal`.
  Copy and paste the output from whichever tool you use into the bug.

Once the bug is ready, as per the above list, subscribe the `ubuntu-archive`
team to the bugs.

## Getting help

If you need help deciding whether a package ought to be removed,
please discuss on the `ubuntu-devel` mailing list rather than asking the
Archive Administrators.


