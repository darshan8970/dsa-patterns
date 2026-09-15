# dsa-patterns

150+ DSA problems organized by **pattern**, not chronology — NeetCode 150 solutions plus
original "concept" problems I write myself, each documented with approach, complexity,
and what I got wrong the first time.

Hi, I'm Darshan — a Computer Science undergrad (AI/ML specialization) documenting my
DSA practice as I prepare for AI/ML engineering internships.

> 📌 Looking for my AI/ML project work instead? See [darshanaiml.dev](https://darshanaiml.dev)
> and my [profile README](https://github.com/darshan8970).

---

## Why this repo exists

Most DSA repos are a flat folder of `sol1.py`, `sol2.py`. This one isn't. It's organized by
**pattern** (not by difficulty or chronology), because the goal isn't "I solved 150 problems" —
it's "I can recognize which of ~16 patterns a new problem maps to." Every solved problem ships
with a short write-up: the pattern, the approach, complexity, and what I got wrong on the first try.

## Progress

<!--PROGRESS_TABLE_START-->
| Pattern | Solved | Total | Progress |
|---|---|---|---|
| Arrays & Hashing | 3 | 9 | ███░░░░░░░ 33% |
| Two Pointers | 0 | 5 | ░░░░░░░░░░ 0% |
| Sliding Window | 0 | 6 | ░░░░░░░░░░ 0% |
| Stack | 0 | 6 | ░░░░░░░░░░ 0% |
| Binary Search | 0 | 7 | ░░░░░░░░░░ 0% |
| Linked List | 0 | 11 | ░░░░░░░░░░ 0% |
| Trees | 0 | 15 | ░░░░░░░░░░ 0% |
| Tries | 0 | 3 | ░░░░░░░░░░ 0% |
| Heap / Priority Queue | 0 | 7 | ░░░░░░░░░░ 0% |
| Backtracking | 0 | 10 | ░░░░░░░░░░ 0% |
| Graphs | 0 | 19 | ░░░░░░░░░░ 0% |
| Dynamic Programming | 0 | 23 | ░░░░░░░░░░ 0% |
| Greedy | 0 | 8 | ░░░░░░░░░░ 0% |
| Intervals | 0 | 6 | ░░░░░░░░░░ 0% |
| Math & Geometry | 0 | 8 | ░░░░░░░░░░ 0% |
| Bit Manipulation | 0 | 7 | ░░░░░░░░░░ 0% |
| **Total** | **3** | **150** | ░░░░░░░░░░ 2% |
<!--PROGRESS_TABLE_END-->

*This table is auto-updated by [`scripts/update_progress.py`](scripts/update_progress.py)
on every push (see the GitHub Action below) — it's never hand-edited, so it's always accurate.*

## Repo structure

```
dsa-patterns/
├── patterns/                  # NeetCode 150, organized by pattern not difficulty
│   ├── arrays-hashing/
│   │   ├── README.md          # pattern primer: when to use it, key tricks
│   │   └── problems/
│   │       └── 0001-two-sum/
│   │           ├── README.md  # approach, complexity, pitfalls
│   │           └── solution.py
│   ├── two-pointers/
│   ├── sliding-window/
│   └── ...                    # 16 patterns total
├── concepts/                  # original problems not found on LeetCode,
│   │                          # written to stress-test my own understanding
│   └── README.md
├── resources/
│   └── cheatsheets/           # one-page pattern cheatsheets
├── scripts/
│   └── update_progress.py     # regenerates the table above from solved problems
└── .github/workflows/
    └── update-readme.yml      # runs update_progress.py on every push to main
```

## How each problem is documented

Every problem folder follows the same template (see
[`patterns/_template/`](patterns/arrays-hashing/problems)) so anyone skimming the repo can
evaluate my thinking, not just my code:

- **Problem** — link + one-line restatement in my own words
- **Pattern** — which of the 16 patterns this falls under, and why
- **Approach** — brute force first, then the optimization, in plain English
- **Complexity** — time/space, with justification (not just "O(n) trust me")
- **What I missed** — the bug or wrong assumption from my first attempt, if any

## Concept problems

The [`concepts/`](concepts) folder is separate from `patterns/` on purpose. These are problems
I write myself — extensions or variations of an idea I just learned — specifically because they
don't exist on LeetCode and force me to actually understand the concept rather than
pattern-match to a solution I've seen before.

## Stack

`Python 3.11` · solutions favor readability and explicit complexity notes over one-liner cleverness.

## Progress log

I'm tracking this alongside a broader AI/ML internship prep timeline — see
[recent build-in-public posts](https://linkedin.com/in/darshan897038) for weekly updates.
