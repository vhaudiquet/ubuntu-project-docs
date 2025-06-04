(main-inclusion-review)=
# Main Inclusion Review (MIR)

Packages in Ubuntu `main` (and `restricted`) are officially
maintained, supported and recommended by the Ubuntu project.
{term}`Canonical` provides security updates, standard support services, and
certain Service Level Agreement (SLA) guarantees for these packages.

Therefore, special consideration is necessary before adding new packages
to `main` or `restricted`. The
[Ubuntu MIR team](https://launchpad.net/~ubuntu-mir)
reviews packages for promotion:

* from {term}`universe` to {term}`main`.
* from {term}`multiverse` to {term}`restricted`.

Reviewing packages before they can be promoted is the **Main Inclusion Review
(MIR)** process.


## MIR process overview

The purpose of the MIR process is to avoid mistakes that have caused issues in
the past. If we reduce the process to its simplest components, it can be
described in only three steps.

First, the process makes the **reporter** think about the package or packages
they want to own. Then, the **reviewer** checks what is submitted and either
approves or raises issues. Finally, any such issues are resolved, and then the
process is complete. 

::::{card-carousel} 3

:::{card}
:img-background: images/mir-step-1-think.png
:link: mir-step-1
:link-type: ref
:::

:::{card}
:img-background: images/mir-step-2-review.png
:link: mir-step-2
:link-type: ref
:::

:::{card}
:img-background: images/mir-step-3-resolve.png
:link: mir-step-3
:link-type: ref
:::
::::

In reality, things are often more complex than that! We use Launchpad (and the
states of bugs in Launchpad) to track the progress of any main inclusion request
as shown in our more detailed {ref}`mir-process-states` breakdown.


## Communication

The MIR team holds a {ref}`mir-team-meeting` where you can raise issues or
discuss your case with the team.

The {ref}`Service Level Objectives <mir-slo>` page details what you can and
should expect from the reviewers.


## MIR documentation

```{note}
This section just collects all the documentation pages together for ease of
reference-- this is not the final format.
```

* {ref}`mir-bug-filing-process`
* {ref}`mir-templates-and-rules`
* {ref}`mir-reporters-template`
* {ref}`mir-reviewers-template`


## MIR special cases

```{toctree}
:maxdepth: 1
:hidden:

../../MIR/mir-exceptions-fonts
../../MIR/mir-exceptions-oem
../../MIR/mir-exceptions-rereview
../../MIR/mir-rust
```

* {ref}`mir-exceptions-fonts`
* {ref}`mir-exceptions-oem`
* {ref}`mir-exceptions-rereview`
* {ref}`mir-rust`





