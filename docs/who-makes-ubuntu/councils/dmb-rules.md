(dmb-rules)=
# DMB rules

This section contains rules and regulations for the {ref}`dmb` to use when conducting its business.
Changes to these rules should be proposed by a board member and voted on by the board.


## Board Member attendance

The final formal wording is from [this post](https://lists.ubuntu.com/archives/devel-permissions/2021-October/001750.html) and is reproduced here:

> Any DMB member who fails to attend 6 consecutive scheduled DMB meetings (during a period no shorter than 12 weeks) shall be considered inactive and removed from membership in the DMB.
> Since the number of members required for quorum is 1/2 the number of active DMB members, rounded up, the change in the number of active members will affect quorum.
> At such time as any DMB member is found to be inactive due to this rule, the current DMB chair will add an action item to schedule a public vote for a new DMB member.
> Previous DMB members, including those changed to inactive due to this rule, are eligible to run in the new election and any later elections.
> This proposal is not retroactive, and the attendance requirement shall start the first meeting after this proposal is adopted.

```{note}
This rule [was proposed](https://lists.ubuntu.com/archives/devel-permissions/2021-August/001726.html) on the mailing list, and [approved on 2021-11-05](https://lists.ubuntu.com/archives/devel-permissions/2021-November/001780.html).
```

(dmb-voting-and-quorum)=
## Voting and quorum

> Quorum votes are required, however if quorum is not reached at first meeting, at the next meeting majority present votes are required.

The details for this rule, and **quorum** voting in particular, are not always clear, so the TL:DR for this rule is, any proposal or application that is voted on at a regular meeting must use the process shown in the Python function below;
if the function does not result in pass or fail, then at the next scheduled meeting, the vote will pass with only a majority of present members (meaning the sum of votes from present members must be greater than 0).

```{note}
This rule was proposed and approved in a [mailing list thread](https://lists.ubuntu.com/archives/devel-permissions/2021-August/001728.html), that was discussed and then [extended to a poll](https://lists.ubuntu.com/archives/devel-permissions/2021-October/001756.html) for which [the results](https://lists.ubuntu.com/archives/devel-permissions/2021-November/001782.html) are explained below.
```

As *quorum* can be difficult to parse under all circumstances, an explanation from a [mailing list post](https://lists.ubuntu.com/archives/devel-permissions/2021-October/001763.html) (and [follow up post](https://lists.ubuntu.com/archives/devel-permissions/2021-October/001764.html) for a tie vote) is summarized in this Python function, where `total_members` is the total number of **active** board members (which is typically 7):

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

This function represents the meaning of **quorum** votes.
Note that if **`total_members`** is 7, if the number of voters is less than 4, it is impossible to pass or fail.
