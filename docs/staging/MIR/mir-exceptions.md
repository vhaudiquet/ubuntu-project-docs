(mir-exceptions)=

# Exceptions


## Font Packages

Fonts packages given that fonts are just data, there\'s no way for them
to trip any of the problems that would cause us to not want to support
it. Therefore not all of the process has to be followed for these.
Unfortunately there were cases where src:font-\* packages contained way
more than just a font - due to that either the MIR Team (if a MIR bug
was filed) or the Ubuntu-Archive team (on promoting it) has to do a spot
check that neither the source nor the created binary packages violate
these assumptions.

The only limitation is that the package needs a valid team subscriber
before being promoted by an archive admin - just in case anything might
come up later. The MIR Team should try to clarify that with the Team
that owns the depending package to own the font as well (read: without
the overhead of a full MIR process).

## OEM Packages

Starting in 20.04, Ubuntu Desktop ISOs will support installing hardware specific metapackages if the machine being installed on has a corresponding enablement package available. These packages enable an additional APT archive. This is the subject of a [discussion with the Technical Board](https://lists.ubuntu.com/archives/technical-board/2020-January/002478.html). See [OEMArchive](https://wiki.ubuntu.com/OEMArchive) for further details.

See {ref}`mir-oem-exception`.

## Re-Reviews

Historically if something was in main once there was no re-evaluation done
later unless if teams asked for it based on huge changes. Doing regular
re-evaluations on all packages would be a nice, but also rather huge effort.

We want to be pragmatic, therefore:
- All we identify shall be recommended tasks (not required to continue) unless we find something really intolerable.
- We'd appreciate if the owning team could file a MIR-reporter bug for it, but would not insist on it if they can't. In that case we create a stub for it.

The benefit of this is, that the stricter rules that we have today (added for
good reasons usually triggered by painful lessons learned no one wants to
repeat), will be considered and thereby might create useful suggestions for
components that are central to Ubuntu, its quality and maintainability.

We'd create a MIR bug if there was none. But if there was a bug already
we'd want to keep the context together and avoid flooding launchpad with
multiple MIR bugs for a single package. Therefore in this case, just
as we do when we retroactively promote in an SRU we'd add per-series bug tasks
to show the state of each review independently.
If source renames are involved those can be tracked the same way all associated
to one bug.

#### Renamed or Reorganized sources

We can use some regular events to start with re-reviews at a small scale,
and that is when things pop up on our radar anyway.

In the past, if a source was already in main, but then appeared in a different
form - common cases that come to mind are renames or code split out - have
gotten a fast-path approval based on being in main already.

But from now on, for packages old enough to not have any audit-trail via a MIR
bug, we want to do a re-evaluation when they show up as component mismatch.

### opt-in re-review

For special cases (read: do not dump hundreds of requests to the MIR team at
once) teams can also request a re-review. That might even be worthwhile if
there already is a former MIR bug - for example if the project was rewritten in
another language all former assumptions might be invalid anyway.

For that a team should contact the MIR team directly in the MIR team meeting.
