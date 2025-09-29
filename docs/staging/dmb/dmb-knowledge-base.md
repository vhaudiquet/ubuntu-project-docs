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





## Conducting meetings


### Scheduling

Meetings currently run every other week, alternating between 16:00 UTC and
19:00 UTC. In the case of vacation such as over New Year, cancel or move
individual meetings as appropriate, but please try not to push all future
meetings around, as this can cause some confusion.

The meeting schedule can be changed by the DMB by majority vote, and it is
expected for the schedule to be confirmed or changed as necessary at the first
meeting after new DMB members are elected. Please also consider the needs of
pending and future applicants if changing the schedule, as doing so may affect
their plans.


### Agenda

We maintain [an agenda page](https://discourse.ubuntu.com/t/ubuntu-developer-membership-board-agenda/66634)
with the dates of upcoming meetings, the agendas for them and outstanding
meeting actions.


### Chair

We share the responsibility of chairing the meetings. There should be a list on
the [agenda page](https://discourse.ubuntu.com/t/ubuntu-developer-membership-board-agenda/66634).
If you have just chaired, rotate the list and update the entry at the top of
the page so we know who is chairing next.


### Quorum

[Quorum was originally publicly discussed](https://discourse.ubuntu.com/t/open-discussion-meetings-quorum/5966)
on the community forum. The specific meaning of **quorum** for voting
[was later clarified](https://lists.ubuntu.com/archives/devel-permissions/2021-October/001763.html)
and is explained in the {ref}`dmb-voting-and-quorum` section.


### General progress during meetings

In January 2023 the DMB agreed to the following. See [the original thread](https://lists.ubuntu.com/archives/devel-permissions/2022-November/002099.html) (November 2022 and January 2023) for more details.

* We accept that it's OK for DMB members to be absent or distracted for whatever
  reason, but not to hold up meetings because of this. Corollary: if as a DMB
  member you are so distracted that you're holding up the meeting, then maybe
  you should consider yourself to be actually absent, and conscious to not hold
  the others up waiting on you.

* We think that three minutes is about the **maximum** that should normally be
  acceptable for a response from a DMB member, with the majority of responses
  expected to be much quicker than that.

* If a DMB member holds up meeting progress for more than three minutes because
  we're waiting for a response from them, then the chair should consider that
  person to be absent and move on. This includes voting: if that means the vote
  wasn't quorate, then we will end the vote and continue as if that person was
  absent anyway.

* DMB members should prepare questions and comments in advance as much as
  possible to avoid holding up meetings while they research, think and type.

* However, we don't want to prevent people from taking their time to research,
  think or or type long answers when this is actually required -- for example in
  response to something that happened during the meeting itself. So a DMB member
  can indicate that they are genuinely active in the meeting but not ready to
  speak yet by sending "...", or a longer explanation if they wish, at least
  once every three minutes. This can include thinking time, doing research on an
  application, working on a long answer, etc. We will take "..." to mean "I'm
  still here, working on my next message to the channel, extending my timeout by
  another three minutes". The meeting will normally then wait for their message
  before moving on, subject to the chair's discretion.

* For the avoidance of doubt, the above applies to DMB members only, not to
  anyone else, and certainly not to applicants. We've not seen an issue with
  applicants being unreasonably slow to respond, and want them to give us
  thoughtful responses and not feel under any additional pressure. They should
  respond as feel appropriate and as they always have done.


### Handling applications

* Try to handle applicants in the order they applied; earliest first.

* Applicants will usually attend an IRC meeting to be questioned by the DMB on
  matters that members wish to clarify before they can vote. If the applicants
  or the DMB are having trouble meeting each other then the application may be
  handled over email, but **it is important this happens in a timely fashion**.

* Many of our applicants do not have English as their first language.

  * Be understanding if the answers you get are not 100% clear

  * Ask questions one at a time. Let the meeting know when you are done
    questioning so that others can take over.

* Make sure that the applicant has signed the
  [Ubuntu Code of Conduct](https://launchpad.net/codeofconduct/2.0). It is
  required to be signed by every Ubuntu developer.


### Voting

Applications have to reach +1 in order to pass. If the meeting is quorate and
all members present vote in the same way (+1 or -1), then the application will
have passed or failed -- the remaining members cannot overturn the vote. If the
vote is in doubt then it is *hung* and the remaining members will be asked to
vote by email or at the next meeting. In this case those members are entitled to
ask the applicant further questions if they still have any on reviewing the
meeting log.


### Actions after a successful application

1. Assign two meeting actions: one to make ACL changes, and one to announce
   the successful applicant. This is to make sure that the announcement does not
   get forgotten.

2. Adjust ACLs:

   * Modification of the membership list for an existing packageset team can
     be done directly by the DMB. A DMB member should go to the packageset's
     uploader team page, and add the applicant to the team.

   * Modification of the package list for an existing packageset can also be done
     directly by the DMB. This requires using
     `the `edit-acl` tool: https://bazaar.launchpad.net/~ubuntu-archive/ubuntu-archive-tools/trunk/view/head:/edit-acl`

     **Note from Sally: this Launchpad link is broken**

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

     2. Open a bug against the [ubuntu-community project](https://launchpad.net/ubuntu-community),
        and the bug description should include the exact
        `edit-acl: https://bazaar.launchpad.net/~ubuntu-archive/ubuntu-archive-tools/trunk/view/head:/edit-acl`
        command to run.

        **Note from Sally: this LP link is broken**

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

   * If applying for {ref}`ubuntu-developers-contributing` membership, the
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
See {ref}`ubuntu-developers-sru` for details.

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
as for {ref}`ubuntu-developers-contributing`, which do not grant any upload
rights to the Ubuntu Archive, do not require adding the new members to any of
the above teams. Those should only be added to
[`~ubuntu-developer-members`](https://launchpad.net/~ubuntu-developer-members).


## Applications from DDs

DDs who are PPU through the normal process can apply by email to have their
access extended to further packages they (or a team they are a member of)
maintain. This only requires one DMB member to agree in order to pass.


## DMB restaffing

### How DMB members are appointed

See [Governance docs: DMB selection process](https://canonical-ubuntu-governance-docs.readthedocs-hosted.com/en/latest/policy/dmb-selection-process/).


### Checklist after new DMB appointments

* Update:

  * (TB) `~developer-membership-board` Launchpad team

  * (TB) [`developer-membership-board@lists.ubuntu.com`](https://lists.ubuntu.com/mailman/listinfo/developer-membership-board)
    membership and then send welcome email

  * (self-subscribe) [`devel-permissions@lists.ubuntu.com membership`](https://lists.ubuntu.com/mailman/listinfo/devel-permissions)

  * Private Matrix room access

  * List of DMB member IRC nicknames in `ubottu`'s `!dmb-ping`

    * Can be requested by typing: `!no dmb-ping is <comma separated list of IRC usernames>: DMB ping.`

  * Calendar meeting event invitation list

* Send welcome email to new DMB members (see the previous one)


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


## Rules and regulations

This section contains rules for the DMB to use when conducting its business.
Changes to these rules should be proposed by a board member and voted on by the
board.


### Board Member attendance

This rule [was proposed](https://lists.ubuntu.com/archives/devel-permissions/2021-August/001726.html)
on the mailing list, and [approved on 2021-11-05](https://lists.ubuntu.com/archives/devel-permissions/2021-November/001780.html).
The final formal wording is from [this post](https://lists.ubuntu.com/archives/devel-permissions/2021-October/001750.html)
and is reproduced here:

Any DMB member who fails to attend 6 consecutive scheduled DMB meetings (during
a period no shorter than 12 weeks) shall be considered inactive and removed from
membership in the DMB. Since the number of members required for quorum is 1/2
the number of active DMB members, rounded up, the change in the number of active
members will affect quorum. At such time as any DMB member is found to be
inactive due to this rule, the current DMB chair will add an action item to
schedule a public vote for a new DMB member. Previous DMB members, including
those changed to inactive due to this rule, are eligible to run in the new
election and any later elections. This proposal is not retroactive, and the
attendance requirement shall start the first meeting after this proposal is
adopted.


(dmb-voting-and-quorum)=
### Voting and quorum

The details for this rule, and **quorum** voting in particular, are not always
clear, so the TL:DR for this rule is, any proposal or application that is voted
on at a regular meeting must use the process shown in the Python function below;
if the function does not result in pass or fail, then at the next scheduled
meeting, the vote will pass with only a majority of present members (meaning the
sum of votes from present members must be greater than 0).

This rule was proposed and approved in a
[mailing list thread](https://lists.ubuntu.com/archives/devel-permissions/2021-August/001728.html),
that was discussed and then [extended to a poll](https://lists.ubuntu.com/archives/devel-permissions/2021-October/001756.html)
for which [the results](https://lists.ubuntu.com/archives/devel-permissions/2021-November/001782.html)
are explained below.

"Quorum votes are required, however if quorum is not reached at first meeting,
at the next meeting majority present votes are required"

As *quorum* can be difficult to parse under all circumstances, an explanation
from a [mailing list post](https://lists.ubuntu.com/archives/devel-permissions/2021-October/001763.html)
(and [follow up post](https://lists.ubuntu.com/archives/devel-permissions/2021-October/001764.html)
for a tie vote) is summarized in this Python function, where `total_members` is
the total number of **active** board members (which is typically 7):

```none
def do_vote(*votes, total_members=7):

  absent = total_members - len(votes)

  net_vote = sum(votes)

  min = net_vote - absent

  max = net_vote + absent

  if min > 0:

    print(f'Vote minimum {min} > 0, vote passes')

  elif max < 0:

    print(f'Vote maximum {max} < 0, vote fails')

  elif min == max == net_vote == 0:

    print(f'Vote is tied, vote fails')

  else:

    print(f'Vote is between {min} and {max}, outcome unknown as quorum was not reached')
```

This function represents the meaning of **quorum** votes. Note that if
**`total_members`** is 7, if the number of voters is less than 4, it is
impossible to pass or fail.


