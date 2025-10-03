# DMB knowledge base

```{note}
[Page source](https://wiki.ubuntu.com/DeveloperMembershipBoard/KnowledgeBase)
```

```{admonition} Sally's note
This page should not go into the docs in its current format. Any knowledge that
should be kept should find appropriate pages to live on (can be new pages).

I have only changed the formatting, corrected some minor spelling errors and
updated links to point to internal references where the original wiki link points
to a wiki page that has been moved already. The wording of the content is the
same as the wiki page.
```

This page is intended to list all of the miscellaneous pieces of DMB knowledge
that have accumulated over the years.

This page is authoritative. If you think you've found a mistake, please
[email the DMB](mailto:developer-membership-board@lists.ubuntu.com).






## Actions after a successful application

1. Assign two meeting actions: one to make ACL changes, and one to announce
   the successful applicant. This is to make sure that the announcement does not
   get forgotten.

2. Adjust ACLs:

   * Modification of the membership list for an existing packageset team can
     be done directly by the DMB. A DMB member should go to the packageset's
     uploader team page, and add the applicant to the team.

   * Modification of the package list for an existing packageset can also be done
     directly by the DMB. This requires using the [`edit-acl` tool](https://git.launchpad.net/ubuntu-archive-tools/tree/edit-acl)

     * Example: (replace `add` with `delete` to remove a package instead of adding):

       ```none
       edit-acl -S $RELEASE -P $PACKAGESET -s $PACKAGE add
       ```

     * Usually the command should be repeated for all supported releases:

       ```none
       for RELEASE in $(distro-info --supported); do edit-acl ...; done
       ```

   * If the action requires creation of a new packageset or PPU, or (rarely)
     changes to the uploader for a packageset or PPU, it must be done by the TB,
     so the DMB member must:

     1. For a new packageset, create a new uploader team (see {ref}`dmb-packagesets` section)

        * For a new PPU, the uploader is the applicant

     2. Open a bug against the [ubuntu-community project](https://launchpad.net/ubuntu-community), and the bug description should include the exact [`edit-acl`](https://git.launchpad.net/ubuntu-archive-tools/tree/edit-acl) command to run.

        * For PPU creation, [file a bug with this subject](https://bugs.launchpad.net/ubuntu-community/+filebug?field.title=[TB/DMB]%20PPU%20for%20)
          and include the PPU member name

        * For packageset creation (or uploader team change),
          [file a bug with this subject](https://bugs.launchpad.net/ubuntu-community/+filebug?field.title=[TB/DMB]%20Packageset%20%20for%20)
          and include the packageset name

        * In the bug, if creating a new packageset, request the TB create the
          packageset, setting the DMB as owner:

          ```none
          edit-acl -S $RELEASE -p developer-membership-board -P $PACKAGESET -t admin create
          ```

        * Also request the TB set or change the uploader:

          ```none
          edit-acl -S $RELEASE -p $UPLOADER -P $PACKAGESET -t upload modify
          ```

        * Usually the commands should be repeated for all supported releases:

          ```none
          for RELEASE in $(distro-info --supported); do edit-acl ...; done
          ```

     3. Email `technical-board@lists.ubuntu.com` to inform them of the opened
        bug (include a link to the bug).

     4. Add the new TB bug to the [DMB agenda](https://discourse.ubuntu.com/t/ubuntu-developer-membership-board-agenda/66634)
        in the "Open TB bugs" section.

     5. After the new packageset is created by the TB, a DMB member will need to
        add the appropriate packages.

3. If not already a member, add the applicant to either
   [`~ubuntu-dev`](https://launchpad.net/~ubuntu-dev/+members) or
   [`~ubuntu-uploaders`](https://launchpad.net/~ubuntu-uploaders/+members).

   See {ref}`dmb-teams-to-add-uploaders-to`.

   * If applying for {ref}`dmb-joining-contributing` membership, the
     applicant should only be added to the
     [`~ubuntu-developer-members`](https://launchpad.net/~ubuntu-developer-members)
     team and nothing more.

4. Announce successful applicants (this can be done in a single email or multiple
   emails as appropriate), as the Community Council
   [would like to see these announced](https://irclogs.ubuntu.com/2016/07/21/%23ubuntu-meeting.html#t17:17)
   and [we agreed in a subsequent meeting](https://irclogs.ubuntu.com/2016/08/01/%23ubuntu-meeting.html#t16:02).

   Send emails to:

   * A reply to the original `devel-permissions@lists.ubuntu.com` thread (useful
      for future reference)

   * An email to `ubuntu-devel@lists.ubuntu.com`

   * An email to `ubuntu-news-team@lists.ubuntu.com`

5. Remove the applicant's agenda item if it is still present.


### Actions after an unsuccessful application

Assign a meeting action to close the application. Closing an application involves:

* Reply with regrets to the `devel-permissions@lists.ubuntu.com` thread only
  (useful for future reference when the applicant reapplies, and to make it
  clear that voting is complete).

* Remove the applicant's agenda item if it is still present.


(dmb-packagesets)=
## Packagesets

Packagesets exist per-release and are defined in the Launchpad database
accessible by API (using the `edit-acl` command). For easy viewing, see
[~ubuntu-archive/packagesets](https://ubuntu-archive-team.ubuntu.com/packagesets/).

Consider creating a packageset once we have:

* Two or more PPU uploaders.

* Two or more related packages.

* The grouping of those packages needs to make logical sense.

The application process is more-or-less the same as for developer upload rights.
The differences are:

* Each packageset needs a *description*. This is so that developers can mail
  `devel-permissions` after the set is created in order to have packages added.
  One DMB member then needs to judge the description against the requested change
  and may make it if they decide it is warranted.

* We create packagesets with just one uploader, which is a team that we then add
  developers to. The team should be configured like so:

  * Owned by the DMB (but without having the DMB as a member).

  * Self renewal.

  * 720 day expiry period.

    ```{note}
    For 'Ubuntu Flavor' packageset teams, [the TB requested](http://ubottu.com/meetingology/logs/ubuntu-meeting-2/2019/ubuntu-meeting-2.2019-06-04-19.04.moin.txt) a 180 day expiry period.
    ```

  * `~ubuntu-core-dev` as a member.

  * Member of `~ubuntu-uploaders` (in rare cases the DMB may require membership
    of packageset uploaders: in this case make the team a member of `~ubuntu-dev`
    instead.)

If necessary, we can modify the description later on following a full vote,
either by email or in a meeting.

Quick set of steps for creating packageset team:

1. Start at [new team registration page](https://launchpad.net/people/+newteam).

2. Make sure {guilabel}`Membership Policy` is *Restricted Team*.

3. Set both the {guilabel}`Subscription Period` and {guilabel}`Self Renewal Period`
   to 720 (or 180 for 'flavor' teams).

4. Change renewal option to *invite them to renew their own membership*.

5. Create the team.

6. On the new team page:

   1. Click {guilabel}`Change Details` and then {guilabel}`Change Owner`.

   2. Change the team owner to `developer-membership-board`.

7. On the new team member page:

   1. Add `ubuntu-core-dev`.

   2. Edit `ubuntu-core-dev` membership expiration to *Subscription Expires: Never*.

   3. Remove (deactivate) yourself.

   4. Remove (deactivate) `developer-membership-board`.

8. Go to [`~ubuntu-uploaders` member page](https://launchpad.net/~ubuntu-uploaders/+members)
   (or, if appropriate, [`~ubuntu-dev` member page](https://launchpad.net/~ubuntu-dev/+members))
   and add the new team as a member.


### Special packagesets


#### Automatically managed packagesets

Flavour packagesets are automatically managed from seeds. There is a script to
control this, which contains a list of overrides too. See
[the Launchpad script](https://code.launchpad.net/~developer-membership-board/+git/packageset).
We should look at automating runs of this script, but currently we need to
remember to manually run it from time to time.

The script encodes the logic about which packagesets packages should go to,
based on how sources are shared between flavours. Broadly, `kubuntu`, `ubuntu`
and`ubuntu-server` are considered top-tier flavours and if they contain a
package that is shared with others then they win and it goes into their set.
`core` and `desktop-core` win out over all flavour sets too. See the `seed-sets`
mapping at the top of the `packageset-push` script in the above branch.


#### Personal packagesets and glob expansions

Where an individual has a special reason for upload rights to a large number of
packages that the DMB expects to need to manage frequently, we can create a
"personal packageset" for this person, named "`personal-<lpid>`". There was once
one: `personal-gunnarhj`, that existed until Gunnar was granted Core Dev and was
therefore no longer needed. This was defined as the set that the DMB has agreed
that Gunnar may upload, which included individual packages to which he has PPU,
as well as glob expansions. The globs were defined in the packageset description.
This way, any DMB member could update the glob expansions for Gunnar (by relying
on their existing definition) without needing to refer to the full DMB for
agreement or the TB to make the change.

This was managed manually, but it may be advisable to script updates if needed
in the future.

See the thread starting at [May 2016](https://lists.ubuntu.com/archives/devel-permissions/2016-May/000924.html),
but extending over June, July, August and September for details.


#### Canonical OEM metapackage packageset

The `canonical-oem-metapackages` packageset is glob based. The exact glob is
defined in the packageset description and is expanded according to the list of
source packages in the Ubuntu Archive for a given series. Any DMB member may
update the packageset according to the glob expansion at any time without
needing further consultation. However, this is now done automatically with
[this script](https://git.launchpad.net/~developer-membership-board/+git/oem-meta-packageset-sync/tree/oem-meta-packageset-sync).

The script is "owned" by the DMB, who is the gatekeeper for changes to the
script, but run and managed on behalf of the DMB by the
[Archive Admin team](https://launchpad.net/~ubuntu-archive/+members). To make
this work, the packageset is owned by the Archive Admin team.

The expected nature of the packageset, to which the DMB grants upload access,
relies on the MIR team's requirements for these packages, defined at
{ref}`mir-exceptions-oem`.

* [Background thread](https://lists.ubuntu.com/archives/devel-permissions/2020-July/001542.html)
* Decided at the [DMB meeting of 2020-08-11](https://irclogs.ubuntu.com/2020/08/10/%23ubuntu-meeting.html#t19:01)
* Documented at [OEM Archive](https://wiki.ubuntu.com/OEMArchive)


### Delegating packageset uploader permissions

The DMB can decide to delegate the granting of upload rights to a packageset to
a different group of developers. An example is that the Ubuntu Desktop team is
self-managed. This means that applicants to that packageset do not come to the
DMB, but they come to the team itself instead. The procedure is the same as for
most other applications: somebody approaches the DMB with the proposal and it is
voted on at the meeting. If approved, the body delegated should be added as an
administrator of the team. It is very important that the teams come with a
policy that says how applications will be managed. That is the document which
you approve. You can see some examples on {ref}`dmb`, and it is important that
this list is kept current.


## SRU Developers

Based on [this thread](https://lists.ubuntu.com/archives/ubuntu-devel/2017-February/039652.html),
[the DMB agreed](https://irclogs.ubuntu.com/2017/02/27/%23ubuntu-meeting.html#t19:32)
to create [a new team for SRU developers](https://launchpad.net/~ubuntu-sru-developers).
This was [announced to ubuntu-devel on 28 February 2017](https://lists.ubuntu.com/archives/ubuntu-devel/2017-February/039702.html).
See {ref}`dmb-joining-sru-dev` for details.

This team is for contributors who work mostly on SRUs but don't necessarily yet
have experience in wider Ubuntu development. Team membership allows the sponsors
to get out of the way for SRUs only.

This team grants Ubuntu Membership. In other words, the DMB must determine that
an applicant meets the requirements for Ubuntu Membership before granting an
applicant membership of this team.

Add successful applicants to the [`~ubuntu-sru-developers`](https://launchpad.net/~ubuntu-sru-developers)
team.


### Removals

There was some concern about potential bad uploads bothering the SRU team, so to
mitigate this the DMB also agreed that individual `~ubuntu-sru-developers`
membership will be removed if any of:

* `~ubuntu-sru` resolves to remove the member (how they do so is up to them); or
* The DMB resolves to remove the member by a quorate vote, and a vote will be
  held if any member of `~ubuntu-sru` requests it.


(dmb-teams-to-add-uploaders-to)=
## Teams to add uploaders to

By default, uploaders to packagesets and per-package uploaders should be granted
membership. This does **not** happen automatically -- they must be added to the
`~ubuntu-dev` team. The reason for this is that occasionally the DMB may want to
grant people upload rights if they do not meet the usual "significant and
sustained" (interpreted as 6 months of contributions). That is: **when adding a
new packageset or PPU uploader, add the individual to `~ubuntu-dev` if they are
being granted membership or (for PPU only) to `~ubuntu-uploaders` if they are
not**.

An exception to the above is that some packagesets *require* membership. You can
identify these because the uploading teams are a member of `~ubuntu-dev` instead
of `~ubuntu-uploaders`. In these cases applicants must satisfy the membership
critera: granting upload rights without membership is not possible.

This is, of course, only the case when adding **uploaders**. Memberships such
as for {ref}`dmb-joining-contributing`, which do not grant any upload
rights to the Ubuntu Archive, do not require adding the new members to any of
the above teams. Those should only be added to
[`~ubuntu-developer-members`](https://launchpad.net/~ubuntu-developer-members).



## Accidental expiry

Since we usually require uploaders to self-renew after some period, sometimes
this is missed by an uploader, and they request that we reinstate them shortly
after expiry.

The DMB have long established that if it's relatively soon after expiry in the
judgement of an individual DMB member, then the uploader can have their
membership reinstated without any further consideration.

If it has been some considerable time since the uploader's team membership
expired, then a full DMB vote is required as usual, but the DMB has in the past
opted not to require a full application (just an agenda item and a quick
discussion at the next meeting).

For the "relatively soon" case, the DMB member should use the following process:

1. Make sure the request is available in the archives of `devel-permissions@`

2. Go to the "Members" page on Launchpad for the team in question (e.g.
   [`~ubuntu-core-dev` members](https://launchpad.net/~ubuntu-core-dev/+members))

3. Page to the end to locate the "Former members" section and locate the uploader.

4. Check the "Expired on" date in the "Status" column is relatively recent. If
   it is not, then stop this process here and ask that the applicant attends a
   DMB meeting to request reinstatement as discussed above.

5. Using the {guilabel}`Edit` button on the right of the former team member
   entry, change "Expiration" to "On" using the default date provided, write a
   suitable comment, and click the {guilabel}`Renew` button.

6. Reply to the `devel-permissions@` thread confirming renewal so there is a
   record in the Archive.





