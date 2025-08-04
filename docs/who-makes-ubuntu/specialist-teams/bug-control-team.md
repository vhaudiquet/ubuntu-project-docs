(bug-control-team)=
# Ubuntu Bug Control

The Bug Control team is a subset of the {ref}`Ubuntu Bug Squad <bug-squad>` with
additional permissions.

The Ubuntu Bug Control team ([`ubuntu-bugcontrol`](https://launchpad.net/~ubuntu-bugcontrol)
in Launchpad) can change the importance of Ubuntu bug tasks, set the status of
an Ubuntu bug task to "Triaged" or "Won't Fix" and target a bug for a release
of Ubuntu.

Both individuals and teams can join the Ubuntu Bug Control team. This page
outlines how to join.


## Generic requirements

These requirements are applicable to everyone (whether joining as a team or
individual). You must:

* Understand [Bugs/Importance](https://wiki.ubuntu.com/Bugs/Importance)

* Understand [Bugs/Status](https://wiki.ubuntu.com/Bugs/Status)

* Understand [Bugs/Assignment](https://wiki.ubuntu.com/Bugs/Assignment)

* Read [Debugging Procedures](https://wiki.ubuntu.com/DebuggingProcedures)

* Read the [Debugging sections](https://wiki.ubuntu.com/Debugging) relative to your interest


## Specific requirements


::::{tab-set}
:::{tab-item} **For individuals**
:sync: individuals

To join Ubuntu Bug Control as an individual, you must:

* Be (and promise to be) polite to bug reporters, even if they are not polite,
  by signing the Ubuntu {ref}`Code of Conduct <code-of-conduct>`.

* Understand:

  * [Bugs/Triage](https://wiki.ubuntu.com/Bugs/Triage)

  * [Assigning bugs](https://wiki.ubuntu.com/Bugs/Assignment)

  * Choosing a [bug task status](https://wiki.ubuntu.com/Bugs/Status) and
    setting a bug task's importance. There is a particular procedure for
    triaging and each possible importance has a specific meaning, so make sure
    you understand the conventions.

* Complete the generic requirements.

* Know the requirements for making an Apport crash report publicly visible --
  by default these are private. Documentation regarding this can be found at
  [Triaging Apport crash reports](https://wiki.ubuntu.com/Bugs/Triage#Apport_crash_reports).

* Have a list of bug reports you have worked on that demonstrate your
  understanding of the triage process. Improve some bug reports and keep a
  short list (at least 5) of your best ones.

```{warning}

Requirement 4 can be waived if you are an upstream developer or bug triager, or
if an Ubuntu developer vouches for your triaging ability.
```
:::

:::{tab-item} **For teams**
:sync: teams

To join Ubuntu Bug Control as a team:

* The team must be a closed or moderated team.

* The team must require all its members to sign the Ubuntu {ref}`Code of Conduct <code-of-conduct>`.

* The team must have *at least one* representative tasked with educating new
  members on Ubuntu Bug Control policies.

* The representative above must be a current member, directly or indirectly, of
  Ubuntu Bug Control.

* The team must limit their use of Ubuntu Bug Control permissions to a specific
  set of packages -- i.e. they should not be setting the importance of bugs
  about every package in Ubuntu.
:::
::::


## Application

::::{tab-set}
:::{tab-item} **For individuals**
:sync: individuals

Membership through a team
: Membership in some teams automatically grants membership to Ubuntu Bug Control,
for example: [ubuntu-core-dev](https://launchpad.net/~ubuntu-core-dev),
[ubuntu-core-doc](https://launchpad.net/~ubuntu-core-doc), and
[ubuntu-dev](https://launchpad.net/~ubuntu-dev). Check if your team is a member
by visiting the team's homepage and looking at the {guilabel}`Subteam of`
section.


Apply for membership directly
: e-mail your application to `ubuntu-bugcontrol AT lists.launchpad.net`. In your
email, please copy and answer the following questions:

  1. Do you promise to be polite to bug reporters even if they are rude to you or
   Ubuntu? Have you signed the Ubuntu Code of Conduct?

  1. Have you read Bugs/Triage, Bugs/Assignment, Bugs/Status and Bugs/Importance?
   Do you have any questions about that documentation?

  1. What sensitive data should you look for in a private Apport crash report bug
   before making it public? (See Bugs/Triage for more information)

  1. Is there a particular package or group of packages that you are interested
   in helping with?

  1. Please list five or more bug reports you have triaged, and include an
   explanation of your decisions. These bugs should be representative of your
   very best work and they should demonstrate your understanding of the triage
   process and how to properly handle bugs. For each bug in the list, please
   indicate what importance you would give it and explain the reasoning. Provide
   URLs in your list of bugs. 

```{note}

If you are an upstream developer, or a bug triager for an upstream project,
contact [Brian Murray](https://launchpad.net/~brian-murray).
```
:::

:::{tab-item} **For teams**
:sync: teams

One of your team's administrators should e-mail the team application to
`ubuntu-bugcontrol AT lists.launchpad.net` -- please give us:

* A brief statement with the reasons why it is important for the team to be a
  member

* A list of the Ubuntu source packages the team plans to work on

* Identify who is/are the representative(s) -- give us the link to the
  Launchpad page of each representative 
:::
::::



## Evaluation criteria and process

::::{tab-set}
:::{tab-item} **For individuals**
:sync: individuals

The application review is a subjective process; however, this is a list of what
we usually look for:

1. Has the applicant provided the importance they would give a bug report?
1. Does the reasoning for the bug importance make sense?
1. Has the applicant provided an explanation for every bug provided? Is it logical?
1. Is the applicant respectful and tactful in their communications?
1. Are the applicant's comments detailed and do they explain their actions?
1. Is the applicant following the
   [Debugging Procedures](https://wiki.ubuntu.com/DebuggingProcedures) for the
   package the bug report is about?
1. Has the applicant made bug titles or descriptions more descriptive?
1. Has the applicant added any bug watches to bug reports? (Linked bugs upstream)
1. Has the applicant forwarded any bugs upstream? (Registered in upstream bug
   tracking system and reported a bug) 

The review process will take at least 7 days, to ensure that every Ubuntu Bug
Control member has had an opportunity to review and comment on the application.

Example Application
: The following are examples of high-quality Bug Control applications,
  containing lots of different types of triaging work.

  * [Application from Yofel](https://lists.launchpad.net/ubuntu-bugcontrol/msg00715.html)

  * [Application from Kamal Mostafa](https://lists.launchpad.net/ubuntu-bugcontrol/msg01024.html)

  * [Application from kermiac](https://lists.launchpad.net/ubuntu-bugcontrol/msg01083.html)
:::

:::{tab-item} **For teams**
:sync: teams

One of the team's administrators will review the application and act on it.
This may require e-mail/IRC exchange.

Evaluation is subjective.

:::
::::

## Length of membership

Initial membership will be set for three months from the date of approval.
After this initial period, membership will be valid for one year.
Approximately one week before the expiry date, an email will be sent warning of
the upcoming expiration, and to request action.

You are expected to renew when needed, following the email's directions.


## Links

* {ref}`bug-squad`

* Ubuntu Wiki: [Helping with bugs](https://wiki.ubuntu.com/HelpingWithBugs)

* Ubuntu Wiki: [Bugs/Triage](https://wiki.ubuntu.com/Bugs/Triage)

* Ubuntu Wiki: [Bugs/Importance](https://wiki.ubuntu.com/Bugs/Importance)

* Ubuntu Wiki: [Bugs/Status](https://wiki.ubuntu.com/Bugs/Status)

* Ubuntu Wiki: [Bugs/Assignment](https://wiki.ubuntu.com/Bugs/Assignment)

* Ubuntu Wiki: [Ubuntu Bug Control in Launchpad](http://launchpad.net/people/ubuntu-bugcontrol)
