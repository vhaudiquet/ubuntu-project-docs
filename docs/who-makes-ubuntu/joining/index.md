(joining-a-role)=
# Developer Membership

```{toctree}
:titlesonly:
:hidden:

path-to-upload-rights
membership-in-packageset
membership-in-MOTU
membership-in-core-dev
dmb-application
```

(ubuntu-developers)=
# Ubuntu developers

```{note}
[Page source](https://wiki.ubuntu.com/UbuntuDevelopers)

TODO: This page probably should be split up

TODO: There is also some overlap with the community pages (which I have not
incorporated) that discuss roles and memberships.
```


Ubuntu developers represent an important part of the creation of Ubuntu. They
have a direct influence on the software included in Ubuntu and whether it meets
the needs of end users. They are responsible for ensuring that Ubuntu works, and
works as well as it can with the resources available.

Everybody is welcome to work on any package they want to improve and we value
these contributions. If you don't have upload rights yet,
{ref}`sponsors <sponsorship>` can review your work and upload it for you.

If you wanted to categorize the different kinds of involvement and upload rights
in Ubuntu, it would look like this:

* {ref}`ubuntu-developers-prospective` who probably just started contributing
  to Ubuntu.

* {ref}`ubuntu-developers-contributing`, who were recognized with
  {ref}`ubuntu-membership`.

* {ref}`Ubuntu Developers (from delegated teams) <ubuntu-developers-delegated>`,
  who can upload to a specific [Package Set](https://wiki.ubuntu.com/ArchiveReorganisation/Permissions).

* {ref}`MOTU <ubuntu-developers-motu>`, who can upload to
  {ref}`universe and multiverse <archive-components>`.

* {ref}`Ubuntu Core Developers (core-dev) <ubuntu-developers-core-dev>`,
  who can upload to all areas of Ubuntu.

* {ref}`Per-Package Uploaders <ubuntu-developers-per-package>`,
  who can upload specific packages.

* {ref}`SRU developers <ubuntu-developers-sru>`, who can upload any package but
  only to stable releases.


(ubuntu-developers-prospective)=
## Ubuntu Prospective Developers

This is where you should start if you are interested in joining the development
team. Prospective Developers:

* Work on bug fixes, merges, syncs and any other aspect of {ref}`ubuntu-development`.

* Gain experience with Debian-format packaging.

* Request sponsor review of suggested changes, where sponsors:

  * Review the packages prepared by the Prospective Developer.

  * Provide constructive feedback.

  * Upload the package when they are satisfied with its quality.

  * For more information, please read {ref}`sponsorship process <sponsorship>`.

* Participate in technical discussions with Ubuntu developers, providing ideas
  and feedback.


### Become a Prospective Developer

There are no requirements to be a Prospective Developer, and anyone with
interest is encouraged to become involved. Please see the links at the top of
this page for pointers in some of the many ways to start contributing to Ubuntu
development.


(ubuntu-developers-contributing)=
## Ubuntu Contributing Developers

* Are members of the [`ubuntu-developer-members`](https://launchpad.net/~ubuntu-developer-members)
  team in Launchpad.

* Have demonstrated *significant and sustained* contributions in the area of
  {ref}`ubuntu-development` -- see {ref}`member-requirements` for
  guidance on what our expectations are for "significant" and "sustained".
  
* Are implicitly considered Ubuntu Members.

* Continue with sponsored uploads as a Prospective Developer.


### Join the ubuntu-developer-members team

* Check the general requirements for {ref}`ubuntu-membership`.

* Apply to the {ref}`dmb` using the {ref}`dmb-application`.


(ubuntu-developers-delegated)=
## Ubuntu Developers (from delegated teams)

* Are members of a [delegated development group](https://wiki.ubuntu.com/UbuntuDevelopers/TeamDelegation)
  in Launchpad.

* Are collectively responsible for maintenance of a subset of packages in Ubuntu.

* Understand packaging concepts, having substantial experience of uploading
  packages through a sponsor.

* Apply this knowledge by uploading new packages, and updating existing packages,
  in an area of expertise.

* May also contribute to other areas in Ubuntu in cooperation with another
  developer.

* Answer questions of other developers to expand their understanding of
  packaging work.

* Provide guidance for prospective Ubuntu developers regarding technical issues.

* Are implicitly considered Ubuntu Members.

* Are granted a vote when the {ref}`Development Membership Board <dmb>` or
  Technical Board are polling Ubuntu Developers.

* Are considered as {ref}`ubuntu-developers-contributing` when working outside
  their delegated subset of packages.

At the current time, the following teams are considered delegated teams
admitting their own members:

* [Ubuntu Desktop Developers](https://wiki.ubuntu.com/DesktopTeam/Developers) (Launchpad: [`~ubuntu-desktop`](https://launchpad.net/~ubuntu-desktop))
* [Mythbuntu Developers](http://www.mythbuntu.org/development/policy) (Launchpad: [`~mythbuntu-dev`](https://launchpad.net/~mythbuntu-dev))
* [Kubuntu Developers](https://wiki.ubuntu.com/Kubuntu/KubuntuDevelopers) (Launchpad: [`~kubuntu-dev`](https://launchpad.net/~kubuntu-dev))
* [Edubuntu Developers](https://wiki.ubuntu.com/Edubuntu/Documentation/Developers) (Launchpad: [`~edubuntu-dev`](https://launchpad.net/~edubuntu-dev))
* [Ubuntu Kernel Uploaders](https://wiki.ubuntu.com/Kernel/Dev/UploadRights) (Launchpad: [`~ubuntu-kernel-uploaders`](https://launchpad.net/~ubuntu-kernel-uploaders))

The following teams are considered delegated teams whose prospective members
apply to the {ref}`Developer Membership Board <dmb>`:

* [Ubuntu Kylin](https://wiki.ubuntu.com/UbuntuKylin) Developers (Launchpad: [`~ubuntukylin-dev`](https://launchpad.net/~ubuntukylin-dev))
* Ubuntu GNOME Developers (Launchpad: [`~ubuntu-gnome-dev`](https://launchpad.net/~ubuntu-gnome-dev))
* Ubuntu Bazaar Uploaders (Launchpad: [`~ubuntu-bzr-dev`](https://launchpad.net/~ubuntu-bzr-dev))
* Ubuntu CLI/Mono Uploaders (Launchpad: [`~ubuntu-cli-mono-dev`](https://launchpad.net/~ubuntu-cli-mono-dev))
* Ubuntu Desktop Extra Uploaders (Launchpad: [`~ubuntu-desktop-extra-dev`](https://launchpad.net/~ubuntu-desktop-extra-dev))
* Ubuntu Input Methods Uploaders (Launchpad: [`~ubuntu-input-methods-dev`](https://launchpad.net/~ubuntu-input-methods-dev))
* Ubuntu Mozilla Uploaders (Launchpad: [`~ubuntu-mozilla-uploaders`](https://launchpad.net/~ubuntu-mozilla-uploaders))
* Ubuntu OIF uploaders (Launchpad: [`~ubuntu-oif-dev`](https://launchpad.net/~ubuntu-oif-dev))
* Ubuntu Qt5 Uploaders (Launchpad: [`~ubuntu-qt5-dev`](https://launchpad.net/~ubuntu-qt5-dev))
* Ubuntu Schooltool Uploaders (Launchpad: [`~ubuntu-schooltool-dev`](https://launchpad.net/~ubuntu-schooltool-dev))
* Ubuntu Sugar Uploaders (Launchpad: [`~ubuntu-sugar-dev`](https://launchpad.net/~ubuntu-sugar-dev))
* Ubuntu Server Developers (Launchpad: [`~ubuntu-server-dev`](https://launchpad.net/~ubuntu-server-dev))
* Ubuntu Studio Uploaders (Launchpad: [`~ubuntu-studio-uploaders`](https://launchpad.net/~ubuntu-studio-uploaders))
* Ubuntu Ubuntu One Uploaders (Launchpad: [`~ubuntu-ubuntuone-dev`](https://launchpad.net/~ubuntu-ubuntuone-dev))
* Ubuntu Xorg uploaders (Launchpad: [`~ubuntu-xorg-dev`](https://launchpad.net/~ubuntu-xorg-dev))
* Ubuntu Zentyal Uploaders (Launchpad: [`~ubuntu-zentyal-dev`](https://launchpad.net/~ubuntu-zentyal-dev))
* Ubuntu Zope Uploaders (Launchpad: [`~ubuntu-zope-dev`](https://launchpad.net/~ubuntu-zope-dev))

The following package sets currently exist without a team owning them:

* `lubuntu`
* `xubuntu`
* `ubuntu-mate`


### Join a delegated team

* Check the general requirements for {ref}`ubuntu-membership`.

* Review the requirements for the specific team of interest, and apply to that
  team for membership, or to the Developer Membership Board following the
  {ref}`usual application process <dmb-application>` if membership is handled
  there.


(form-a-delegated-team)=
### Form a delegated team

* Email `devel-permissions@lists.ubuntu.com` with:

  * A description of your set of packages. The Developer Membership Board will
    use this description to verify which packages should belong to the set. This
    description should contain a name for the package set, and set out criteria
    against which packages can be tested for membership.

  * An initial list of packages.

  * An initial list of members (with their Launchpad IDs).

* The Developer Membership Board, at its next meeting (providing this is more
  than 7 days after the application), will discuss the package set with the
  applicants and then vote on its creation. When applying for a set, please be
  prepared to attend a DMB meeting.

* The Developer Membership Board will take care of creating the package set and
  ensuring that the requested permissions are granted.


### Requesting changes to delegated teams

* Email `devel-permissions@lists.ubuntu.com` with the proposed change(s) and the
  packageset to which the change applies.
  
* A Developer Membership Board member will review the request and either make
  the change or ask for further clarification if it us unclear that the package
  falls under the delegation granted when the team was created.


### Package Sets and Seed Updates

* Ubuntu distribution is {ref}`organized into seeds <seed-management>`. The
  basic seeds, which define what goes into the Archive's `main` component, are:
  `minimal`, `boot`, `standard`, `desktop`, `ship`, `live`, and `supported`.
  There are many other seeds, which can be seen at:

    * [DMB -- packageset](https://git.launchpad.net/~developer-membership-board/+git/packageset/tree/)

    * [Core Dev -- Ubuntu](https://git.launchpad.net/~ubuntu-core-dev/ubuntu-seeds/+git/ubuntu/tree/)

    * [Core Dev -- platform](https://git.launchpad.net/~ubuntu-core-dev/ubuntu-seeds/+git/platform/tree/)

* For some seeds, we currently have an automated way to guarantee that the
  packages included in (or removed from) a seed are automatically included (or
  excluded) from its packageset equivalent (thus guaranteeing, or denying,
  upload permissions to a developer with rights to this package set).

* The process to automatically generate this 1:1 mapping (among seeds <-->
  package sets) is described at:

  * [DMB -- packageset](https://git.launchpad.net/~developer-membership-board/+git/packageset/tree/)
    README file.


(ubuntu-developers-motu)=
## MOTU

* Are [members of the MOTU team](https://launchpad.net/~motu) in Launchpad.

* Are collectively responsible for the maintenance of packages in the `universe`
  and `multiverse` components.

* Understand packaging concepts, having substantial experience of uploading
  packages through a sponsor.

* Apply this knowledge by uploading new packages, and updating existing packages,
  in the `universe` component.

* May also contribute to the `main` component in cooperation with a Ubuntu Core Developer.

* Answer questions of other developers to expand their understanding of
  packaging work.

* Provide guidance for prospective Ubuntu developers regarding technical issues.


### Join MOTU

* Check the general requirements for {ref}`ubuntu-membership`

* Apply to the {ref}`Developer Membership Board <dmb>` using the
  {ref}`application process <dmb-application>`


(ubuntu-developers-core-dev)=
## Ubuntu Core Developers

* Are members of the [`ubuntu-core-dev` team](https://launchpad.net/~ubuntu-core-dev)
  in Launchpad.

* Are collectively responsible for the maintenance of all packages in Ubuntu.

* Have a strong working knowledge of packaging concepts and techniques, refined
  through experience.

* Have a strong working knowledge of Ubuntu project procedures, especially those
  related to the release process and support commitments, and an understanding
  of the reasons why they exist; e.g. having done an
  [SRU](https://documentation.ubuntu.com/sru/en/latest/) or
  [security fix](https://wiki.ubuntu.com/SecurityTeam/UpdatePreparation).

* Can apply this knowledge to a variety of packages and sub-systems.

* Have a history of substantial direct contributions to the distribution.

* Take a leading role in new development projects to improve Ubuntu.

* Specify, develop and deploy new features for the default installation of Ubuntu.

* Exercise great care in their work, with the understanding that their efforts
  have a direct impact on others, including:

  * Every Ubuntu user

  * The Ubuntu release team

  * Corporate partners who provide support for Ubuntu

* Feel a sense of personal responsibility for the quality of Ubuntu releases and
  for the satisfaction of Ubuntu users.

* Are implicitly considered Ubuntu Members.

* Are granted a vote when the Development Membership Board or Technical Board
  are polling Ubuntu Developers.


### Join the Ubuntu Core Developers team

* Check the general requirements for {ref}`ubuntu-membership`

* Apply to the {ref}`Developer Membership Board <dmb>` using the
  {ref}`application process <dmb-application>`


(ubuntu-developers-per-package)=
## Per-Package Uploaders

* Are developers with a specialisation in a specific set of packages in Ubuntu.

* Are granted direct upload to the Ubuntu archive for that set of packages.

* Have enough technical knowledge of the package(s) in question from documented
  work in the package through sponsorship, work in other distributions, or work
  upstream.

* Understand that such an access grant does not permit sole-maintainership, but
  rather the right to participate in the maintenance of the package as part of
  a team.

* Understand the broad strokes of the release schedule, relevant freezes that
  would affect the package in question, and appropriate means by which to handle
  any exceptions.

* Need to show advocacy and support from existing developers, indicating that
  their previous work on the package warrants unsupervised upload.

* Need to have documented previous concern for the packages in question in
  Ubuntu, including previous uploads, effective bug management, etc.

* Need to show a history of effective collaboration with other developers in
  Ubuntu.

* Are specialist maintainers, not generalist maintainers. They are not expected
  to understand packaging best practices as applicable to a wide variety of
  software, or large number of packages in the archive. They *are* expected to
  have exceptional technical expertise with the package(s) for which access is
  requested.

* Are granted a vote when the Development Membership Board or Technical Board
  are polling Ubuntu Developers.

Where a developer has an interest in a wide variety of packages, that developer
is encouraged to strive for membership in one or more existing development teams.
In cases where a given small set of packages attracts the interest of more than
one specialised developer, the Developer Membership Board may recommend the
foundation of a team. See {ref}`form-a-delegated-team`.

There is a slightly special procedure for Debian Developers wishing to have
upload rights to their packages. See {ref}`application process <dmb-application>`.


### Join the Per-Package Uploaders

* Check the general requirements for {ref}`ubuntu-membership`.

* Apply to the {ref}`Developer Membership Board <dmb>` using the
  {ref}`application process <dmb-application>`.


(ubuntu-developers-sru)=
## SRU developers

* Are developers with a specialisation in working on
  [stable release updates](https://documentation.ubuntu.com/sru/en/latest/) in
  Ubuntu.

* Are granted direct upload to the Ubuntu Archive for all packages but only to
  the stable releases.

* Have uploads subject to the standard SRU process, including review from SRU
  team members and all other SRU policies.

* Have a good track record of sponsored SRUs, thus demonstrating an understanding
  of SRU policies, requirements and process.

* Drive SRUs through to the end, not letting things languish in `-proposed`.

* Are granted a vote when the Development Membership Board or Technical Board
  are polling Ubuntu Developers.

Developers who focus on package-specific areas in Ubuntu, such as MOTU and
Package Set uploaders also upload SRUs without necessarily being a member of the
SRU developers team. In contrast, SRU developers work on SRUs across different
sections of the Ubuntu Package Archive.


### Join SRU developers

* Check the general requirements for {ref}`ubuntu-membership`.

* Make sure you meet the description above, and that your sponsors are willing
  to endorse your application.

* Apply to the {ref}`Developer Membership Board <dmb>` using the
  {ref}`application process <dmb-application>`.


### Benefits

* All the {ref}`benefits <member-perks>` of Ubuntu Membership.

* Voting privileges to confirm Ubuntu
  [Technical Board](https://wiki.ubuntu.com/TechnicalBoard) and
  {ref}`Developer Membership Board <dmb>` nominations.

* Opportunity to be nominated for the Developer Membership Board.

* [Access](https://lists.ubuntu.com/archives/ubuntu-devel-announce/2014-February/001079.html)
  to all Valve-produced games for Steam.

* A few Per-Package Uploaders are not members of
  [`ubuntu-dev`](https://launchpad.net/~ubuntu-dev) and are not eligible for
  these benefits. One way to check this is to run `bin/lp-check-membership` from
  the `lptools` package.

