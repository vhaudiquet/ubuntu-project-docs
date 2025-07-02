(freeze-exception-process)=
# Freeze exception process

As with most rules, there are occasional exceptions to the restrictions imposed
by the various stages of the Ubuntu release process. These exceptions are
granted by the release team based on information provided by the developer who
proposes the change.

## General instructions

Requests for freeze exceptions should be filed as bugs in Launchpad against the
relevant package (or just "Ubuntu" if the package is not available yet).

The bug should be set to status *New* when requesting a freeze exception, to
ensure the release team sees the request. Once the bug is filed and the
necessary information is available, subscribe
[`ubuntu-release`](https://launchpad.net/~ubuntu-release).
All freeze exceptions must include the following information, to provide the
release team with enough information to weigh the risk of regressions against
the benefit of the changes:

* A description of the proposed changes, with sufficient detail to estimate
  their potential impact on the distribution

* A rationale for the exception, explaining the benefit of the change

* Any additional information which would be helpful in considering the decision


## Feature Freeze exceptions

A request for an exception to {ref}`feature-freeze` should demonstrate that the
benefit of new functionality, or the total benefit of a new upstream release
that includes it, outweighs the risk of regressions and other potential
disruption of the release process.

Exception requests **must** include the following additional details:

* An explanation of what testing has been performed on the new version in Ubuntu,
  including verification that the new package:

  * Builds

  * Installs

  * Upgrades

  * Does not break packages depending on it, or that corresponding updates have
    been prepared

* If the upload is a new upstream micro-release, the relevant part of the
  upstream changelog and/or release notes also needs to be included


### Feature Freeze for new upstream versions

If you want to introduce a new upstream version with new features and/or
ABI/API changes, you should first create a new bug under your package (or, if
there is already a bug related to the exception, you can reuse the bug), e.g.
`https://bugs.launchpad.net/ubuntu/+source/<PACKAGE>/+filebug`

Your bug contents need to include the following:

* Add `[FFE]` to the bug summary (large title)

* Add an FFE stanza to the description starting with `## FFE ##`

* **State the reason why you feel it is necessary** (e.g. other bugs it fixes)

* Attach (as files):

  * A diff of the **Upstream** changelog (not `debian/changelog`):

    ```none
    diff -u <package>-{old-version,new-version}/ChangeLog > changelog.diff
    ```

    Note that the changelog is sometimes called `CHANGES`, is missing or the
    tarball merely has a `NEWS` file

  * The `NEWS` file, if you think that this information will help reviewing your
    request (true for most GNOME packages)

  * Build log (as a file)

    * `pbuilder` has the `--logfile` option

    * `pbuilder-dist` and `cowbuilder-dist` automatically save it as `last_operation.log`

  * Install log

   * For instance, a copy and paste of the install messages from console when
     installing

  * Mention what testing you've done to see that it works 

    * A screenshot showing the main features would also be nice

* Subscribe (do not assign!) the '`ubuntu-release`' team


```{important}
We expect requesters to have an updated package already prepared and tested!
You will need this anyway to provide proper build logs.
```

Once the Feature Freeze Exception has been ACK'd by a member of the
[Release Team](https://launchpad.net/~ubuntu-release), the status will be
changed to *TRIAGED*. You can then either upload the package (if you're in
[`motu`](http://launchpad.net/~motu) or
[`ubuntu-core-dev`](http://launchpad.net/~ubuntu-core-dev)), or follow the
{ref}`sponsorship-process`. Please close the bug from the upload, where possible.


```{seealso}
* [Open requests](https://bugs.launchpad.net/~ubuntu-release/+subscribedbugs)

* [Original announcement](https://lists.ubuntu.com/archives/ubuntu-motu/2006-February/000545.html) of the change to the UVF exceptions process
```


### Feature Freeze for bugfix-only updates

Up through RC, if a developer believes an upload of a new upstream release that
just has bug fixes in it is warranted, they may upload it. The developer should
explicitly document that this is a bugfix-only upload in the changelog or sync
request.

If you are not sure whether something qualifies, check with a member of
`ubuntu-release` (or subscribe `ubuntu-release` to the bug) and if one person
from `ubuntu-release` agrees it's a bug fix update, you're good for upload.

### Feature Freeze for new packages

New source packages in the Archive do not require Feature Freeze exceptions, as
they must be explicitly opted into by users. For NEW uploads which are not
syncs from Debian, make sure you have the agreement of a member of
{ref}`the Archive Admins` to perform the necessary queue reviews before you
upload.

However, at the point where you integrate the new package into an existing one
(e.g. adding a dependency or turning on a feature) or add it to a seed, Feature
Freeze begins to apply and you must seek an exception. This is the point at
which risk is added to people who didn't explicitly choose it.

## User Interface Freeze exceptions

The exception request bug report needs to have a justification for why the User
Interface (UI) needs to be changed at that point, and give a rationale of why the
benefits of it are worth breaking existing documentation and translations.

Every change of the UI (either a string or the layout) requires you to notify
the [documentation](https://lists.ubuntu.com/mailman/listinfo/ubuntu-doc) and
[translation](https://lists.ubuntu.com/mailman/listinfo/ubuntu-translators)
teams.

Please add links to your posts in the
[`ubuntu-doc@`](https://lists.ubuntu.com/archives/ubuntu-doc/) and
[`ubuntu-translators@`](https://lists.ubuntu.com/archives/ubuntu-translators/)
mailing list archives to the bug.

After that, subscribe the release team as usual.

== Milestone freeze Exceptions (like BetaFreeze) ==

During milestone/final release freeze periods, extreme caution is exercised when considering exceptions, as a regression could cause a deadline to be missed, or a build to receive less testing than desired.  A request for an exception must demonstrate strong rationale and minimal risk for the update to be considered.

Exception requests must include the following additional details:

 * It must fix a bug milestoned for that particular milestone.
 * A complete `debdiff` of the proposed upload must be provided (preferably as bug attachment).

== Packageset FFe Delegations ==

From time to time the `ubuntu-release` team will delegate the responsibility of reviewing Feature Freeze exceptions for a packageset to one or more designated individuals that are not members of the Release Team.  Delegates are expected to be Ubuntu Developers with upload rights to the packageset in question who have a good working relationship with the Release Team and have demonstrated a clear understanding of the freeze guidelines.

For the `kubuntu-desktop` packageset in Ubuntu 20.04, the Release Team delegates FFe-granting authority to 
[[https://launchpad.net/~rikmills|Rik Mills (~rikmills)]] and [[https://launchpad.net/~tsimonq2|Simon Quigley (~tsimonq2)]].

== Exceptions for Universe/Multiverse ==
The FreezeExceptionProcess is the same for Universe/Multiverse as for Main/Restricted, except where explained below.

=== Milestone Freeze ===

During the last week of development before the release, all uploads need to get approved by the release team. 

Process:
 * Either file a bug with the debdiff and assign it to `ubuntu-release` and get approval for it.
 * Or ask a member of the `ubuntu-release` [[http://launchpad.net/~ubuntu-release|team]] on IRC of approval for the debdiff.

Decision: [[MOTU/Council/Meetings/2007-02-23]].

----
[[CategoryProcess]]

