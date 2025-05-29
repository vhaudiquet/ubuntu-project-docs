# The Main Inclusion Review (MIR) process

Packages in Ubuntu main (and restricted) are officially maintained,
supported and recommended by the Ubuntu project. Security updates are
provided for them as necessary by Canonical, and Canonical's standard
support services apply to these packages.

Therefore, special consideration is necessary before adding new packages
to these components. The [Ubuntu MIR Team](https://launchpad.net/~ubuntu-mir)
reviews packages for promotion from universe to main.

That is the **Main Inclusion Review (MIR)**.

* MIR state machine {ref}`mir-process-states`

```{admonition} To do
:class: note

Add the simplified overview of the MIR state machine diagram here
```

* MIR exceptions {ref}`mir-exceptions`
* How to file an MIR bug {ref}`file-mir-bug`
  * {ref}`mir-template`
* {ref}`review-mir-bug`
* {ref}`mir-slo`
* {ref}`mir-helpers`

## MIR Team weekly status meeting


The MIR Team holds weekly meetings every Tuesday at
<time datetime="T16:30+01:00">16:30 CET</time> on the IRC Server
`irc.libera.chat` in the `#ubuntu-meeting` channel. You can follow these
[instructions](https://libera.chat/guides/connect) on how to connect to
`irc.libera.chat`.

The meeting is meant to help to facilitate

* a fair share of work for each of us
* a timely response to reporters of MIR requests
* detection and discussion of any current or complex cases

Due to the nature of this process there are times when this is very busy
and the meeting is strongly needed. But there are other times (e.g. at
the beginning of a new release) where not a lot is happening. In such
*idle* phases the leader of the meeting can pre-check the links we
usually check together and skip steps of the agenda quoting that a
pre-check has not shown anything worth to discuss.

From there we can then go rather directly to *Any other business?*
which serves as a catch all for all attendees. By that we can make the
meeting more efficient in those times, instead of filing a monologue-log
every week.

If you're chairing the meeting, you can the following meetingology
template:

```
#startmeeting Weekly Main Inclusion Requests status

Ping for MIR meeting - didrocks joalif slyon sarnold cpaelzer mylesjp pushkarnk ( dviererbe )

# Awareness of external agenda items
Mission: To be aware and potentially allocate the required time, poll if anyone attending has discussions that should be added to the agenda today.

#topic current component mismatches
Mission: Identify required actions and spread the load among the teams

#link https://people.canonical.com/~ubuntu-archive/component-mismatches-proposed.svg
#link https://people.canonical.com/~ubuntu-archive/component-mismatches.svg

#topic New MIRs
Mission: ensure to assign all incoming reviews for fast processing

#link https://bugs.launchpad.net/ubuntu/?field.searchtext=&orderby=-date_last_updated&field.status%3Alist=NEW&field.status%3Alist=CONFIRMED&assignee_option=none&field.assignee=&field.subscriber=ubuntu-mir

#topic Incomplete bugs / questions
Mission: Identify required actions and spread the load among the teams

#link https://bugs.launchpad.net/ubuntu/?field.searchtext=&orderby=-date_last_updated&field.status%3Alist=INCOMPLETE_WITH_RESPONSE&field.status%3Alist=INCOMPLETE_WITHOUT_RESPONSE&field.subscriber=ubuntu-mir

#topic Process/Documentation improvements
Mission: Review pending process/documentation pull-requests or issues

#link https://github.com/canonical/ubuntu-mir/pulls
#link https://github.com/canonical/ubuntu-mir/issues

#topic MIR related Security Review Queue
Mission: Check on progress, do deadlines seem doable?

Some clients can only work with one, some with the other escaping - the URLs point to the same place.
#link https://bugs.launchpad.net/~ubuntu-security/+bugs?field.searchtext=%5BMIR%5D&assignee_option=choose&field.assignee=ubuntu-security&field.bug_reporter=&field.bug_commenter=&field.subscriber=ubuntu-mir&orderby=-date_last_updated&start=0
#link https://bugs.launchpad.net/~ubuntu-security/+bugs?field.searchtext=[MIR]&assignee_option=choose&field.assignee=ubuntu-security&field.bug_reporter=&field.bug_commenter=&field.subscriber=ubuntu-mir&orderby=-date_last_updated&start=0

Internal link
- ensure your teams items are prioritized among each other as you'd expect
- ensure community requests do not get stomped by teams calling for favors too much
#link https://warthogs.atlassian.net/jira/software/c/projects/SEC/boards/594

#topic Any other business?
Mission: catch-all chance for anything missed or not covered by the usual agenda items.

#endmeeting
```



### Contributing

We welcome everyone who wants to improve the Ubuntu MIR documentation! Whether you've found a typo, have a suggestion for improving existing content, or want to add new content, we'd love to hear from you.

To contribute, simply submit a pull request with your changes or create an issue. Please also attend the weekly MIR Team meeting (every Tuesday at <time datetime="T16:30+01:00">16:30 CET</time> on the IRC `irc.libera.chat` in the `#ubuntu-meeting` channel) to discuss your issue with the MIR Team. You can follow these [instructions](https://libera.chat/guides/connect) on how to connect to `irc.libera.chat`.


