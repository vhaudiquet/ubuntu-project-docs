(path-to-upload-rights)=
# Path to upload rights

```{note}
The links shown on this page are subject to sudden changes over the next
few months as more of the documentation it refers to is migrated here. Please
expect inconsistencies -- and feel welcome to correct any links you find that
are incorrect.
```

These interactive charts show the skills needed to obtain permissions for
uploading changes to the Ubuntu Package Archive. They can be used as a guide
to help build your applications for upload rights on:

* {ref}`Package Sets <membership-in-packageset>`
* {ref}`MOTU <membership-in-motu>`, 
* {ref}`Core Developer <membership-in-core-dev>`


## The overall journey

Since Ubuntu is based on Debian, they share a similar technical skillset. This
means that as a contributor, you may want to contribute to Debian as well as
Ubuntu, or just focus on one (as you prefer).

This diagram shows the overall expected progression paths you can take as a
contributor. Click any of the nodes to learn more.


:::{mermaid}
block-beta
  columns 8

%% Column 1
  block:col1
  columns 1
    space:3
    Start(("Start"))
    space
  end

%% Column 2
  block:col2
  columns 1
    space
    space
    Ubuntu{{"<b>Ubuntu<br>path</br>"}}
    space
    Debian{{"<b>Debian<br>path</b>"}}
  end

  Start --> Ubuntu
  Start --> Debian

%% Column 3
  block:col3
  columns 1
    UploadRights{{"<b>Upload<br>rights</b>"}}
    space
    Basics("<a href='#upload-path-basics'>Basics</a>")
    space
    Contributor("<a href="https://www.debian.org/doc/manuals/maint-guide/">Contributor</a>")
  end

%% Column 4
  block:col4
  columns 1
    PPU["<a href='https://canonical-ubuntu-project.readthedocs-hosted.com/who-makes-ubuntu/joining/membership-in-packageset/'>PPU<br>PackageSet</a>"]
    space
    Intermediate("<a href='#upload-path-intermediate'>Intermediate</a>")
    space
    Maintainer("<a href='https://wiki.debian.org/DebianMaintainer'>Maintainer</a>")
  end

%% Column 5
  block:col5
  columns 1
    MOTU["<a href='https://canonical-ubuntu-project.readthedocs-hosted.com/who-makes-ubuntu/joining/membership-in-MOTU/'>MOTU</a>"]
    space
    Advanced("<a href='#upload-path-advanced'>Advanced</a>")
    space
    Developer("<a href='https://wiki.debian.org/DebianDeveloper'>Developer</a>")
  end

%% Column 6
  block:col6
  columns 1
    CoreDev["<a href='https://canonical-ubuntu-project.readthedocs-hosted.com/who-makes-ubuntu/joining/membership-in-core-dev/'>Core Dev</a>"]
    space
    Expert("<a href='#upload-path-expert'>Expert</a>")
    space:2
  end

%% Connections
Basics --> Intermediate
Intermediate --> Advanced
Intermediate --> PPU
Advanced --> Expert
Advanced --> MOTU
Expert --> CoreDev

Contributor --> Maintainer
Maintainer --> Developer

%% Styling
classDef debianStyle fill: #F8A3C0, stroke: #DD1155
  class Debian debianStyle
  class Contributor debianStyle
  class Maintainer debianStyle
  class Developer debianStyle

classDef ubuntuStyle fill: #FFDAB9, stroke: #E95420,stroke-width:1px;
  class Ubuntu ubuntuStyle
  class Basics ubuntuStyle
  class Intermediate ubuntuStyle
  class Advanced ubuntuStyle
  class Expert ubuntuStyle

classDef uploaderStyle fill: #FFDF7E, stroke: #FBAB13
  class UploadRights uploaderStyle
  class PPU uploaderStyle
  class MOTU uploaderStyle
  class CoreDev uploaderStyle

classDef invisible fill: transparent, stroke: transparent
  class col1,col2,col3,col4,col5,col6 invisible
:::


(upload-path-basics)=
## Basics

These topics will get you started with a good foundation for your future
contributions to Ubuntu.

:::{mermaid}
block-beta
columns 2
  block
    InitialStudies("Initial studies")
    columns 1
    Concepts{{"<a href=https://github.com/canonical/ubuntu-maintainers-handbook>Concepts</a>"}}
    GitUbuntu{{"git-ubuntu"}}
    DebianPolicy{{"<a href=https://www.debian.org/doc/debian-policy/>Debian Policy</a>"}}
  end

  block
    InitialTasks("Initial tasks")
    columns 1
    BugTriage["<a href='https://canonical-ubuntu-project.readthedocs-hosted.com/contributors/bug-triage/'>Bug triage</a>"]
    BiteSizedBugs["Bite-sized bugs"]
    TrivialPackgeMerges["Trivial package merges"]
  end

  InitialStudies --> InitialTasks

  style InitialStudies fill: #FFDAB9, stroke:#F4A460
  style InitialTasks fill:#FFDAB9, stroke:#F4A460
:::

Once your team and/or mentor says you are ready for more, you can move onto the
intermediate tasks.


(upload-path-intermediate)=
## Intermediate

This set of topics and tasks will prepare you to apply for single-package (PPU)
or Package Set upload rights.

```{mermaid}
block-beta
    columns 2

    block
        IntermediateStudies("Intermediate studies")
        columns 1
        UnderstandDep8{{"<a href=https://salsa.debian.org/ci-team/autopkgtest/blob/master/doc/README.package-tests.rst>Understand DEP8</a>"}}
        ComplexPackageMerges{{"Complex package merges"}}
        SRU{{"<a href=https://canonical-sru-docs.readthedocs-hosted.com/>Study SRU</a>"}}
        BlockA{{" "}}
    end
   
    block
        IntermediateTasks("Intermediate tasks")
        columns 1
        AddAUTOPKGTESTS["<a href=https://canonical-ubuntu-project.readthedocs-hosted.com/contributors/bug-fix/package-tests/>Add Autopkgtest</a>"]
        ProposeMigration["<a href=https://canonical-ubuntu-project.readthedocs-hosted.com/how-ubuntu-is-made/processes/proposed-migration/>Proposed Migration</a>"]
        DoSRUS["Do SRUS"]
        WorkOnBugs["Work on packaging bugs/features"]
    end
    
    %% Transitions
    UnderstandDep8 --> AddAUTOPKGTESTS
    ComplexPackageMerges --> ProposeMigration
    SRU --> DoSRUS

    style IntermediateStudies fill: #FFDAB9, stroke:#F4A460;
    style IntermediateTasks fill:#FFDAB9, stroke:#F4A460;
    style BlockA fill:transparent,stroke:transparent;
```

Once you have done enough of these tasks that your team/mentor says you are
ready to continue your journey, you can move onto the Advanced topics.

At this time, you can also consider yourself ready to apply for PPU or
Package Set upload rights if there are particular packages or sets of packages
you are particularly focused on. 


(upload-path-advanced)=
## Advanced

```{mermaid}
block-beta
    columns 2

    block
        AdvancedStudies("Advanced studies")
        columns 1

        BlockA(" ")
        BlockB(" ")
        BlockC(" ")

        StudyFFE{{"<a href=https://canonical-ubuntu-project.readthedocs-hosted.com/staging/release-team/freeze-exceptions/>Study FFE</a>"}}
        PlusOne{{"<a href=https://canonical-ubuntu-project.readthedocs-hosted.com/contributors/advanced/plus-one-maintenance/>Study +1</a>"}}
    end

    block
        AdvancedTasks("Advanced tasks")
        columns 1
        UpstreamSubmissionFixes["Upstream submission fixes/features"]
        UpstreamSubmissionDelta["Upstream submission of delta"]
        MilestonesAndExceptions["Milestones and exceptions"]
        DoAnFFE["Do An FFE"]
        PlusOneShadowing["+1 Shadowing"]
    end

    StudyFFE-->DoAnFFE
    PlusOne-->PlusOneShadowing

    style AdvancedStudies fill: #FFDAB9, stroke:#F4A460;
    style AdvancedTasks fill:#FFDAB9, stroke:#F4A460;
    style BlockA fill:transparent,stroke:transparent;
    style BlockB fill:transparent,stroke:transparent;
    style BlockC fill:transparent,stroke:transparent;

```

With enough of these tasks under your belt to demonstrate your skills and
experience, you can move onto the Expert topics.

At this point, you can consider yourself ready to apply for MOTU.


(upload-path-expert)=
## Expert 

As a member of MOTU, the following tasks and topics will guide you towards
becoming a Core Developer. Keep doing enough of these tasks until you have the
experience you need to apply for Core Dev.

```{mermaid}
block-beta
    columns 2
    
    block 
        columns 1
        ExpertStudies("Expert studies")

        StudyLibaryTransitions{{"<a href=https://wiki.debian.org/Teams/ReleaseTeam/Transitions>Study Libary Transitions</a>"}}
        StudyPackageTransitions{{"<a href=https://wiki.debian.org/PackageTransition>Study Package Transitions</a>"}}
        BlockA(" ")
        StudyMIR{{"<a href=https://canonical-ubuntu-project.readthedocs-hosted.com/MIR/main-inclusion-review/>Study MIR</a>"}}
    end

    block
        columns 1
        ExpertTasks("Expert tasks")

        DoLibaryTransitions["Do Libary Transitions"]
        DoPackageTransitions["Do Package Transitions"]
        DoMIR["Do a MIR"]
        SeedChange["Seed Change"]
    end

        StudyLibaryTransitions-->DoLibaryTransitions
        StudyPackageTransitions-->DoPackageTransitions
        StudyMIR-->DoMIR
        StudyMIR-->SeedChange

    style ExpertStudies fill: #FFDAB9, stroke:#F4A460;
    style ExpertTasks fill:#FFDAB9, stroke:#F4A460;
    style BlockA fill:transparent,stroke:transparent;
```


