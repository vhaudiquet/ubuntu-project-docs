This page is intended to list all of the miscellaneous pieces of DMB
knowledge that have accumulated over the years.

This page is authoritative. If you think you've found a mistake, please
`email the DMB <mailto:developer-membership-board@lists.ubuntu.com>`__.

<<TableOfContents()>>

.. _conducting_meetings:

Conducting meetings
===================

Scheduling
----------

Meetings currently run every other week, alternating between 1500 UTC
and 1900 UTC. In the case of vacation such as over New Year, cancel or
move individual meetings as appropriate, but please try not to push all
future meetings around, as this can cause some confusion.

The meeting schedule can be changed by the DMB by majority vote, and it
is expected for the schedule to be confirmed or changed as necessary at
the first meeting after new DMB members are elected. Please also
consider the needs of pending and future applicants if changing the
schedule, as doing so may affect their plans.

Agenda
------

We maintain `an agenda
page <https://wiki.ubuntu.com/DeveloperMembershipBoard/Agenda>`__ with
the dates of upcoming meetings, the agendas for them and outstanding
meeting actions.

Chair
-----

We share the responsibility of chairing the meetings. There should be a
list on the `agenda page <DeveloperMembershipBoard/Agenda>`__. If you
have just chaired, rotate the list and update the entry at the top of
the page so we know who is chairing next.

Quorum
------

`Quorum was originally publicly discussed on the community
forum <https://discourse.ubuntu.com/t/open-discussion-meetings-quorum/5966>`__.
The specific meaning of **quorum** for voting was later
`clarified <https://lists.ubuntu.com/archives/devel-permissions/2021-October/001763.html>`__
and is explained in the `section below <#Voting_and_Quorum>`__.

.. _handling_applications:

Handling applications
---------------------

-  Try to handle applicants in the order they applied, earliest first.
-  Applicants will usually attend an IRC meeting to be questioned by the
   DMB on matters that members wish to clarify before they can vote. If
   the applicants or the DMB are having trouble meeting each other then
   the application may be handled over email, but **it is important this
   happens in a timely fashion**.
-  Many of our applicants do not have English as their first language.

   -  

      -  Be understanding if the answers you get are not 100% clear
      -  Ask questions one at a time. Let the meeting know when you are
         done questioning so that others can take over.

Voting
------

Applications have to reach +1 in order to pass. If the meeting is
quorate and all members present vote in the same way (+1 or -1), then
the application will have passed or failed - the remaining members
cannot overturn the vote. If the vote is in doubt then it is *hung* and
the remaining members will be asked to vote by email or at the next
meeting. In this case those members are entitled to ask the applicant
further questions if they still have any on reviewing the meeting log.

.. _actions_after_a_successful_application:

Actions after a successful application
--------------------------------------

#. Assign two meeting actions: one to make ACL changes, and one to
   announce the successful applicant. This is to make sure that the
   announcement does not get forgotten.
#. Adjust ACLs.

-  

   -  Modification of the membership list for an existing packageset
      team can be done directly by the DMB. A DMB member should go to
      the packageset's uploader team page, and add the applicant to the
      team.
   -  Modification of the package list for an existing packageset can
      also be done directly by the DMB. This requires using the
      "`edit-acl <https://bazaar.launchpad.net/~ubuntu-archive/ubuntu-archive-tools/trunk/view/head:/edit-acl>`__"
      tool

      -  example (replace *add* with *delete* to remove a package
         instead of adding):

``   * ``

::

    edit-acl -S $RELEASE -P $PACKAGESET -s $PACKAGE add 

-  

   -  usually the command should be repeated for all supported releases:

``   * ``

::

    for RELEASE in $(distro-info --supported); do edit-acl ...; done 

-  

   -  If the action requires creation of a new packageset or PPU, or
      (rarely) changes to the uploader for a packageset or PPU, it must
      be done by the TB, so the DMB member must:

| ``  1. For a new packageset, create a new uploader team (see ``\ ```Packageset`` <#Packageset>`__\ `` section below)``
| ``   * For a new PPU, the uploader is the applicant``
| ``  1. Open a bug against the ``\ ```ubuntu-community project`` <https://launchpad.net/ubuntu-community>`__\ ``, and the bug description should include the exact "``\ ```edit-acl`` <https://bazaar.launchpad.net/~ubuntu-archive/ubuntu-archive-tools/trunk/view/head:/edit-acl>`__\ ``" command to run.``
| ``   * For PPU creation, [``\ ```a bug with this subject`` <https://bugs.launchpad.net/ubuntu-community/+filebug?field.title=%5BTB/DMB%5D%20PPU%20for%20%7Cfile>`__\ ``] and include the PPU member name``
| ``   * For packageset creation (or uploader team change), [``\ ```a bug with this subject`` <https://bugs.launchpad.net/ubuntu-community/+filebug?field.title=%5BTB/DMB%5D%20Packageset%20%20for%20%7Cfile>`__\ ``] and include the packageset name``
| ``   * In the bug, if creating a new packageset, request the TB create the packageset, setting the DMB as owner:``
| ``    * ``

::

    edit-acl -S $RELEASE -p developer-membership-board -P $PACKAGESET -t admin create 

| ``   * Also request the TB set or change the uploader:``
| ``    * ``

::

    edit-acl -S $RELEASE -p $UPLOADER -P $PACKAGESET -t upload modify 

| ``   * usually the commands should be repeated for all supported releases:``
| ``    * ``

::

    for RELEASE in $(distro-info --supported); do edit-acl ...; done 

| ``  1. Email technical-board@lists.ubuntu.com to inform them of the opened bug (include a link to the bug).``
| ``  1. Add the new TB bug to the ``\ ```DMB Agenda`` <https://wiki.ubuntu.com/DeveloperMembershipBoard/Agenda>`__\ `` in the ``\ *``Open TB bugs``*\ `` section``
| ``  1. After the new packageset is created by the TB, a DMB member will need to add the appropriate packages``

#. If not already a member, add the applicant to either
   `~ubuntu-dev <https://launchpad.net/~ubuntu-dev/+members>`__ or
   `~ubuntu-uploaders <https://launchpad.net/~ubuntu-uploaders/+members>`__.
   See `#Teams_to_add_uploaders_to <#Teams_to_add_uploaders_to>`__.
#. Announce successful applicants (this can be done in a single email or
   multiple emails as appropriate), as `the community council would like
   to see these
   announced <https://irclogs.ubuntu.com/2016/07/21/%23ubuntu-meeting.html#t17:17>`__
   and `we agreed in a subsequent
   meeting <https://irclogs.ubuntu.com/2016/08/01/%23ubuntu-meeting.html#t16:02>`__.
   Send emails to:

   #. A reply to the original devel-permissions@lists.ubuntu.com thread
      (useful for future reference).
   #. An email to ubuntu-devel@lists.ubuntu.com
   #. An email to ubuntu-news-team@lists.ubuntu.com

#. Remove the applicant's agenda item if it is still present.

.. _actions_after_an_unsuccessful_application:

Actions after an unsuccessful application
-----------------------------------------

#. Assign a meeting action to close the application. Closing an
   application involves:
#. Reply with regrets to the devel-permissions@lists.ubuntu.com thread
   only (useful for future reference when the applicant reapplies, and
   to make it clear that voting is complete).
#. Remove the applicant's agenda item if it is still present.

Packagesets
===========

Packagesets exist per-release and are defined in the Launchpad database
accessible by API (using the edit-acl command). For easy viewing, see
https://people.canonical.com/~ubuntu-archive/packagesets/

Consider making packagesets if someone applies and the grouping makes
logical sense. The application process is more or less the same as for
developer upload rights. The differences are

-  Each packageset needs a *description*. This is so that developers can
   mail \`devel-permissions\` after the set is created in order to have
   packages added. One DMB member then needs to judge the description
   against the reqested change and may make it if they decide it is
   warranted.
-  We create packagesets with just one uploader, which is a team that we
   then add developers to. The team should be configured like so

   -  

      -  Owned by the DMB (but without having the DMB as a member)
      -  Self renewal
      -  720 day expiry period

``   * Note, for 'Ubuntu Flavor' packageset teams, the TB ``\ ```requested`` <http://ubottu.com/meetingology/logs/ubuntu-meeting-2/2019/ubuntu-meeting-2.2019-06-04-19.04.moin.txt>`__\ `` a 180 day expiry period``

-  

   -  \`~ubuntu-core-dev\` as a member
   -  Member of \`~ubuntu-uploaders\` (in rare cases the DMB may require
      membership of packageset uploaders: in this case make the team a
      member of \`~ubuntu-dev\` instead.)

If necessary, we can modify the description later on following a full
vote, either by email or in a meeting.

Quick set of steps for creating packageset team:

#. Start at `new team registration
   page <https://launchpad.net/people/+newteam>`__
#. Make sure *Membership Policy* is **Restricted Team**
#. Set both the *Subscription Period* and *Self Renewal Period* to 720
   (or 180 for 'flavor' teams)
#. Change renewal option to *invite them to renew their own membership*
#. Create the team
#. On the new team page:

   #. Click *Change Details* and then *Change Owner*
   #. Change the team owner to **developer-membership-board**

#. On the new team member page:

   #. Add **ubuntu-core-dev**
   #. Edit **ubuntu-core-dev** membership expiration to *Subscription
      Expires: Never*
   #. Remove (deactivate) yourself
   #. Remove (deactivate) **developer-membership-board**

#. Go to `~ubuntu-uploaders member
   page <https://launchpad.net/~ubuntu-uploaders/+members>`__ (or, if
   appropriate, `~ubuntu-dev member
   page <https://launchpad.net/~ubuntu-dev/+members>`__) and add the new
   team as a member

.. _special_packagesets:

Special packagesets
-------------------

.. _automatically_managed_packagesets:

Automatically managed packagesets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Flavour packagesets are automatically managed from seeds. There is a
script to control this, which contains a list of overrides too. See
`lp:~developer-membership-board/+git/packageset <https://code.launchpad.net/~developer-membership-board/+git/packageset>`__.
We should look at automating runs of this script, but currently we need
to remember to manually run it from time to time.

The script encodes the logic about which packagesets packages should go
to, based on how sources are shared between flavours. Broadly,
kubuntu/ubuntu/ubuntu-server are considered top-tier flavours and if
they contain a package that is shared with others then they win and it
goes into their set. core and desktop-core win out over all flavour sets
too. See the \`seed-sets\` mapping at the top of the \`packageset-push\`
script in the above branch.

.. _personal_packagesets_and_glob_expansions:

Personal packagesets and glob expansions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Where an individual has a special reason for upload rights to a large
number of packages that the DMB expects to need to manage frequently, we
can create a "personal packageset" for this person, named "personal-".
There was once one: personal-gunnarhj, that existed until Gunnar was
granted core dev and was therefore no longer needed. This was defined as
the set that the DMB has agreed that Gunnar may upload, which included
individual packages to which he has PPU, as well as glob expansions. The
globs were defined in the packageset description. This way, any DMB
member could update the glob expansions for Gunnar (by relying on their
existing definition) without needing to refer to the full DMB for
agreement or the TB to make the change.

This was managed manually, but it may be advisable to script updates if
needed in the future.

See the thread starting at
https://lists.ubuntu.com/archives/devel-permissions/2016-May/000924.html,
but extending over June, July, August and September for details.

.. _canonical_oem_metapackage_packageset:

Canonical OEM metapackage packageset
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The \`canonical-oem-metapackages\` packageset is glob based. The exact
glob is defined in the packageset description and is expanded according
to the list of source packages in the Ubuntu archive for a given series.
Any DMB member may update the packageset according to the glob expansion
at any time without needing further consultation.

The expected nature of the packageset, to which the DMB will grant
upload access, relies on the MIR team's requirements for these packages,
defined at https://wiki.ubuntu.com/MIRTeam/Exceptions/OEM.

-  Background thread:
   https://lists.ubuntu.com/archives/devel-permissions/2020-July/001542.html
-  Decided at the `DMB meeting of
   2020-08-11 <https://irclogs.ubuntu.com/2020/08/10/%23ubuntu-meeting.html#t19:01>`__
-  Documented at `OEMArchive <OEMArchive>`__

.. _delegating_packageset_uploader_permissions:

Delegating packageset uploader permissions
------------------------------------------

The DMB can decide to delegate the granting of upload rights to a
packageset to a different group of developers. An example is that the
Ubuntu desktop team is self managed. This means that applicants to that
packageset do not come to the DMB, but they come to the team itself
instead. The procedure is the same as for most other applications:
somebody approaches the DMB with the proposal and it is voted on at the
meeting. If approved, the body delegated should be added as an
administrator of the team. It is very important that the teams come with
a policy that says how applications will be managed. That is the
document which you approve. You can see some examples on
`DeveloperMembershipBoard <DeveloperMembershipBoard>`__, and it is
important that this list is kept current.

.. _sru_developers:

SRU Developers
==============

Based on `this
thread <https://lists.ubuntu.com/archives/ubuntu-devel/2017-February/039652.html>`__,
the DMB
`agreed <https://irclogs.ubuntu.com/2017/02/27/%23ubuntu-meeting.html#t19:32>`__
to create `a new team for SRU
developers <https://launchpad.net/~ubuntu-sru-developers>`__. This was
`announced to ubuntu-devel on 28 February
2017 <https://lists.ubuntu.com/archives/ubuntu-devel/2017-February/039702.html>`__.
See UbuntuDevelopers#SRU_developers for details.

This team is for contributors who work mostly on SRUs but don't
necessarily yet have experience in wider Ubuntu development. Team
membership allows the sponsors to get out of the way for SRUs only.

This team grants Ubuntu membership. In other words, the DMB must
determine that an applicant meets the requirements for Ubuntu membership
before granting an applicant membership of this team.

Add successful applicants to the
`\|~ubuntu-sru-developers <https://launchpad.net/~ubuntu-sru-developers>`__
team.

Removals
--------

There was some concern about potential bad uploads bothering the SRU
team, so to mitigate this the DMB also agreed that individual
~ubuntu-sru-developers membership will be removed if any of:

#. ~ubuntu-sru resolves to remove the member (how they do so is up to
   them); or

``2. the DMB resolves to remove the member by a quorate vote, and a vote will be held if any member of ~ubuntu-sru requests it.``

.. _teams_to_add_uploaders_to:

Teams to add uploaders to
=========================

By default, uploaders to packagesets and per-package uploaders should be
granted membership. This does **not** happen automatically - they must
be added to the \`~ubuntu-dev\` team. The reason for this is that
occasionally the DMB may want to grant people upload rights if they do
not meet the usual *significant and sustained* (interpreted as 6 months
of contributions). That is: **when adding a new packageset or PPU
uploader, add the individual to \`~ubuntu-dev\` if they are being
granted membership or (for PPU only) to \`~ubuntu-uploaders\` if they
are not**.

An exception to the above is that some packagesets *require* membership.
You can identify these because the uploading teams are a member of
\`~ubuntu-dev\` instead of \`~ubuntu-uploaders\`. In these cases
applicants must satisfy the membership critera: granting upload rights
without membership is not possible.

.. _applications_from_dds:

Applications from DDs
=====================

DDs who are PPU through the normal process can apply by email to have
their access extended to further packages they (or a team they are a
member of) maintain. This only requires one DMB member to agree in order
to pass.

.. _dmb_restaffing:

DMB Restaffing
==============

.. _running_a_dmb_election:

Running a DMB election
----------------------

#. Decide which seats are expiring and who will run the election.
   Ideally this is a DMB member whose seat is not expiring. Make sure
   you understand when each seat is expiring as the newly elected
   candidates will be filling those seats as they expire in order.

#. Choose the relevant dates: the deadline for nominations, when the
   vote will start, and when the vote will finish.
   `Consider <https://lists.ubuntu.com/archives/ubuntu-devel/2020-February/040927.html>`__
   adding a period between the nomination deadline and the start of the
   vote to allow the nominees to present a platform and/or for the
   electorate to question nominees. These dates should all appear in the
   initial call for nominations. See the example below for time periods
   used in the past.

#. Send out a call for nominations.
   `Example <https://lists.ubuntu.com/archives/ubuntu-devel-announce/2020-January/001270.html>`__.

#. You may need to chase for enough nominations.
   `Example <https://lists.ubuntu.com/archives/ubuntu-devel/2020-February/040887.html>`__.

#. If you chose to allow a questioning period, announce the nominees and
   invite discussion.

#. When the voting is due to begin, generate a list of email addresses
   of the electorate (the electorate is ~ubuntu-dev). This
   `script <https://git.launchpad.net/~ubuntu-dev/+git/election-tools/tree/voter-addresses.py>`__
   is useful to get the email addresses of members of ubuntu-dev. Keep a
   record of which members have been issued ballots so that you can
   manage any missing ballot requests should they arrive later.

#. Create a `CIVS poll <http://civs.cs.cornell.edu/>`__ with the
   nominees and one additional "No further candidates" ordinary choice.
   The default options are fine. You will then be sent a link to the
   poll control page. Start the poll from there.
   `Example <https://civs.cs.cornell.edu/cgi-bin/results.pl?id=E_e053e79083d092fc>`__.

#. Announce the poll. `Newer
   example <https://lists.ubuntu.com/archives/ubuntu-devel-announce/2020-February/001271.html>`__;
   `older
   example <https://lists.ubuntu.com/archives/ubuntu-devel-announce/2017-August/001222.html>`__.
   This ensures that any members of the electorate who do not receive a
   poll for whatever reason (eg. no email address listed) can still have
   the opportunity to vote.

#. When the poll is due to finish, go to the poll control page and end
   the poll.

#. Announce the election results.
   `Example <https://lists.ubuntu.com/archives/devel-permissions/2020-February/001461.html>`__.

#. Complete the "Checklist after a DMB election" section below.

.. _checklist_after_a_dmb_election:

Checklist after a DMB election
------------------------------

-  Point new members to this page
   (https://wiki.ubuntu.com/DeveloperMembershipBoard/KnowledgeBase).
-  Update:

   -  

      -  (TB) ~developer-membership-board Launchpad team
      -  (TB) developer-membership-board@lists.ubuntu.com membership and
         then send welcome email
      -  (self-subscribe) devel-permissions@lists.ubuntu.com membership
      -  Private IRC channel access
      -  List of DMB member IRC nicknames in ubottu's !dmb-ping

``    * Can be requested by typing: !dmb-ping is ``\ \ ``: DMB ping.``

-  

   -  Calendar meeting event invitation list

.. _accidental_expiry:

Accidental Expiry
=================

Since we usually require uploaders to self-renew after some period,
sometimes this is missed by an uploader, and they request that we
reinstate them shortly after expiry.

The DMB have long established that if it's relatively soon after expiry
in the judgement of an individual DMB member, then the uploader can have
their membership reinstated without any further consideration.

If it has been some considerable time since the uploader's team
membership expired, then a full DMB vote is required as usual, but the
DMB has in the past opted not to require a full application (just an
agenda item and a quick discussion at the next meeting).

For the "relatively soon" case, the DMB member should use the following
process:

#. Make sure the request is available in the archives of
   devel-permissions@

| ``2. Go to the "Members" page on Launchpad for the team in question (eg. ``\ ```https://launchpad.net/~ubuntu-core-dev/+members`` <https://launchpad.net/~ubuntu-core-dev/+members>`__\ ``)``
| ``3. Page to the end to locate the "Former members" section and locate the uploader.``
| ``4. Check the "Expired on" date in the "Status" column is relatively recent. If it is not, then stop this process here and ask that the applicant attends a DMB meeting to request reinstatement as discussed above.``
| ``5. Using the edit button on the right of the former team member entry, change "Expiration" to "On" using the default date provided, write a suitable comment, and click the "Renew" button.``
| ``6. Reply to the devel-permissions@ thread confirming renewal so there is a record in the archive.``

.. _rules_and_regulations:

Rules and Regulations
=====================

This section contains rules for the DMB to use when conducting its
business. Changes to these rules should be proposed by a board member
and voted on by the board.

.. _board_member_attendance:

Board Member Attendance
-----------------------

This rule was
`proposed <https://lists.ubuntu.com/archives/devel-permissions/2021-August/001726.html>`__
on the mailing list, and
`approved <https://lists.ubuntu.com/archives/devel-permissions/2021-November/001780.html>`__
on 2021-11-05. The final formal wording is from `this
post <https://lists.ubuntu.com/archives/devel-permissions/2021-October/001750.html>`__
and is reproduced here:

Any DMB member who fails to attend 6 consecutive scheduled DMB meetings
(during a period no shorter than 12 weeks) shall be considered inactive
and removed from membership in the DMB. Since the number of members
required for quorum is 1/2 the number of active DMB members, rounded up,
the change in the number of active members will affect quorum. At such
time as any DMB member is found to be inactive due to this rule, the
current DMB chair will add an action item to schedule a public vote for
a new DMB member. Previous DMB members, including those changed to
inactive due to this rule, are eligible to run in the new election and
any later elections. This proposal is not retroactive, and the
attendance requirement shall start the first meeting after this proposal
is adopted.

.. _voting_and_quorum:

Voting and Quorum
-----------------

The details for this rule, and **quorum** voting in particular, are not
always clear, so the TL;DR for this rule is, any proposal or application
that is voted on at a regular meeting must use the process shown in the
python function below; if the function does not result in pass or fail,
then at the next scheduled meeting, the vote will pass with only a
majority of present members (meaning the sum of votes from present
members must be greater than 0).

This rule was proposed and approved in a `mailing list
thread <https://lists.ubuntu.com/archives/devel-permissions/2021-August/001728.html>`__,
that was discussed and then extended to a
`poll <https://lists.ubuntu.com/archives/devel-permissions/2021-October/001756.html>`__
for which the
`results <https://lists.ubuntu.com/archives/devel-permissions/2021-November/001782.html>`__
are explained below.

"Quorum votes are required, however if quorum is not reached at first
meeting, at the next meeting majority present votes are required"

As *quorum* can be difficult to parse under all circumstances, an
explaination from a `ML
post <https://lists.ubuntu.com/archives/devel-permissions/2021-October/001763.html>`__
(and `follow up
post <https://lists.ubuntu.com/archives/devel-permissions/2021-October/001764.html>`__
for a tie vote) is summarized in this python function, where
*total_members* is the total number of **active** board members (which
is typically 7):

::

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

This function represents the meaning of **quorum** votes. Note that if
**total_members** is 7, if the number of voters is less than 4, it is
impossible to pass or fail.
