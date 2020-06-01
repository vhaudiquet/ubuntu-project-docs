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

`Quorum was last publicly discussed on the community
forum <https://discourse.ubuntu.com/t/open-discussion-meetings-quorum/5966>`__.

We require a absolute majority to pass a motion, so we can pass motions
with >50% of members present if we are unanimously in favour. If we
aren’t unanimously in favour, then we fall back to having to get enough
+1 votes such that the absent members would not be able to swing the
vote below a simple majority even if they were to all vote -1.

In other words, quorum doesn’t really exist as a formal concept for us.
We simply need an absolute majority to pass a motion, and quorum is our
informal way of describing what we need to achieve that in a single
meeting with some members absent.

For the avoidance of doubt: absolute majority means that the requirement
is that >50% of all DMB members are in favour, whether present or not.

As an aside, we have agreed (by absolute majority) that some types of
decision can be made by only one member agreeing. These specific cases
should be documented on this page.

Informally, our "quorum" is 50% rounded up. The DMB has seven members,
so our informal quorum is 4. This number is the minimum number of **+1**
votes that we need for any resolution to pass immediately. Members are
allowed to submit their votes in advance of a meeting, which will count
as if they are present when considering quorum.

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
      team can be done directly by the DMB.
   -  If the action requires creation of a new packageset, or changes to
      the package list for a packageset or PPU, it must be done by the
      TB, so the DMB member must:

| ``  1. Open a bug against the ``\ ```ubuntu-community project`` <https://launchpad.net/ubuntu-community>`__\ ``, and the bug description should include the exact "``\ ```edit-acl`` <https://bazaar.launchpad.net/~ubuntu-archive/ubuntu-archive-tools/trunk/view/head:/edit-acl>`__\ ``" command to run.``
| ``   * For PPU changes, [``\ ```a bug with this subject`` <https://bugs.launchpad.net/ubuntu-community/+filebug?field.title=%5BTB/DMB%5D%20PPU%20addition%20for%20%7Cfile>`__\ ``] and include the PPU member name``
| ``   * For packageset changes, [``\ ```a bug with this subject`` <https://bugs.launchpad.net/ubuntu-community/+filebug?field.title=%5BTB/DMB%5D%20Packageset%20modification%20for%20%7Cfile>`__\ ``] and include the packageset name``
| ``  1. Email technical-board@lists.ubuntu.com to inform them of the opened bug (include a link to the bug).``

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
      -  \`~ubuntu-core-dev\` as a member
      -  Member of \`~ubuntu-uploaders\` (in rare cases the DMB may
         require membership of packageset uploaders: in this case make
         the team a member of \`~ubuntu-dev\` instead.)

If necessary, we can modify the description later on following a full
vote, either by email or in a meeting.

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
Currently there is only one: personal-gunnarhj. This is defined as the
set that the DMB has agreed that Gunnar may upload, which includes
individual packages to which he has PPU, as well as glob expansions. The
globs are defined in the packageset description. This way, any DMB
member may update the glob expansions for Gunnar (by relying on their
existing definition) without needing to refer to the full DMB for
agreement or the TB to make the change.

Currently this is managed manually, but it may be advisable to script
updates if they are frequent.

See the thread starting at
https://lists.ubuntu.com/archives/devel-permissions/2016-May/000924.html,
but extending over June, July, August and September for details.

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
