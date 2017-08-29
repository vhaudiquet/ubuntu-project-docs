This page is intended to list all of the miscellaneous pieces of DMB
knowledge that have accumulated over the years.

This page is authoritative. If you think you've found a mistake, please
`email the DMB <mailto:developer-membership-board@lists.ubuntu.com>`__.

.. _conducting_meetings:

Conducting meetings
===================

Chair
-----

We share the responsibility of chairing the meetings. There should be a
list on the `agenda page <DeveloperMembershipBoard/Agenda>`__. If you
have just chaired, rotate the list and update the entry at the top of
the page so we know who is chairing next.

Quorum
------

The quorum is 50% + 1. For example, if the DMB has 7 members (as it does
at the time of writing), quorum is 4. This number is the minimum number
of **+1** votes that we need for any resolution to pass. Members are
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

| ``2. Adjust ACLs. PPU changes or the creation of a new packageset must be done by the TB. Addition to an existing DMB-managed Launchpad group is the common case, however, and DMB members can do this directly. For requests to the TB, file a bug against the ubuntu-community project and email technical-board@lists.ubuntu.com. Ideally provide the TB with the exact "edit-acl" command to run.``
| ``3. Announce successful applicants (this can be done in a single email or multiple emails as appropriate), as ``\ ```the community council would like to see these announced`` <https://irclogs.ubuntu.com/2016/07/21/%23ubuntu-meeting.html#t17:17>`__\ `` and ``\ ```we agreed in a subsequent meeting`` <https://irclogs.ubuntu.com/2016/08/01/%23ubuntu-meeting.html#t16:02>`__\ ``. Send emails to:``

#. 

   #. A reply to the original devel-permissions@ thread (useful for
      future reference).

| `` 2. An email to ubuntu-devel@.``
| `` 3. An email to ubuntu-news-team@lists.ubuntu.com.``
| ``4. Remove the applicant's agenda item if it is still present.``

.. _actions_after_an_unsuccessful_application:

Actions after an unsuccessful application
-----------------------------------------

#. Assign a meeting action to close the application. Closing an
   application involves:

| ``2. Reply with regrets to the devel-permissions@ thread only (useful for future reference when the applicant reapplies, and to make it clear that voting is complete).``
| ``3. Remove the applicant's agenda item if it is still present.``

Packagesets
===========

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
\`lp:~developer-membership-board/+junk/packageset\`. We should look at
automating runs of this script, but currently we need to remember to
manually run it from time to time.

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

.. _dmb_staffing_elections:

DMB Staffing Elections
======================

A `Condorcet Internet Voting Service <http://civs.cs.cornell.edu/>`__
poll will be created by a member of the DMB whose membership is not
expiring. The poll is initially setup, then the organizer receives an
email to a control form for the poll where they can add email addresses
of voters.

This
`script <https://bazaar.launchpad.net/~stefanor/+junk/election-tools/view/head:/voter-addresses.py>`__
is useful to get the email addresses of members of ubuntu-dev, use the
'-e' switch to only obtain their email addresses and use those in the
poll control form.

Then send an email to ubuntu-devel-announce regarding the fact that a
poll is underway, this provides a way for developers who do not receive
a ballot to contact the poll organizer and reminds people there is an
election underway. Here's an `example
email <https://lists.ubuntu.com/archives/ubuntu-devel-announce/2017-August/001222.html>`__.
