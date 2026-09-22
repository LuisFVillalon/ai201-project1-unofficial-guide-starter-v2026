# The Unofficial Guide

Luis Villalon, city_guides

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Milestone 5. -->
     Using city_guides as the corpus, the system can processes questions regarding cities and counties found in the corpus by retrieving the appropriate information. The question can range from geographical to time-senstivity. The top cited sources are provided with the answer. If the answer cannot be answered with the provided documentation in city_guides, the system returns it does not know the answer.

## Chunking Strategy

**Chunk size:**
One chunk per ## section, each section averages around 203 characters accross 98 chunks. 

**Overlap:**
Sections do no share text with their neighbors. Setting a fixed number for the limit would split relevant content once or twice with the cut being in the middle of a sentence. Splitting the chunks by headings kept them whole so retrieval does not have to stitch a fragmented answer back together. 

<!-- Milestone 3. -->

## Sample Chunks

<!-- Milestone 3. -->

======================================================================
Chunk 1  |  source: guide_accessibility.md#0  |  produced by: chunker.py::split_documents
======================================================================
# Getting around the region with limited mobility

An honest assessment rather than a promotional one. Some of these places are
difficult and it is better to know in advance.

======================================================================
Chunk 2  |  source: guide_corry_vale.md#6  |  produced by: chunker.py::split_documents
======================================================================
## When to go

May to September. Outside those months the pub in the third village closes, the farm shop reduces its hours, and several footpaths become genuinely boggy rather than merely wet. The road is not gritted above the second village and is impassable in snow.

======================================================================
Chunk 3  |  source: guide_givens_mill.md#3  |  produced by: chunker.py::split_documents
======================================================================
## Eat and drink

A tearoom attached to the mill, open 10 to 4 daily except Tuesdays, which sells bread made from the flour ground twenty metres away and is the reason most people come. One pub, food served lunchtimes and Thursday to Saturday evenings.

======================================================================
Chunk 4  |  source: guide_kestrelford.md#6  |  produced by: chunker.py::split_documents
======================================================================
## When to go

Late spring and early autumn. The Saturday market runs year-round but is much reduced from November to February. August is busy with walkers. The single-track approach road is genuinely difficult in snow and the town can be cut off for a day or two most winters.

======================================================================
Chunk 5  |  source: guide_regional_transport.md#1  |  produced by: chunker.py::split_documents
======================================================================
## The railway

The line runs along the river valley, connecting Brightwater to the regional
hub in 50 minutes. Eleven services a day on weekdays, six on Sundays. The line
north of Brightwater closed in 1963 and everything beyond it is bus or car.

Tickets are cheaper booked the day before than on the day, and considerably
cheaper than that booked a week ahead. There is no ticket office at
Brightwater station outside weekday mornings; the machine on the platform takes
cards only.


## Sample Answer

<!-- Milestone 4. -->

**Question:**
"I am 55 years old and would love to go on a walk in Thornby Wells, do you recommend it?"
**Answer:**
Yes, Thornby Wells is recommended for walking. It has flat, formal gardens and level streets, making it the region's most accessible town on foot (guide_walking.md).

Sources retrieved: guide_accessibility.md, guide_regional_transport.md, guide_thornby_wells.md, guide_walking.md

**My relevance cutoff:**

<!-- Milestone 4. -->

I chose 5 for my relevance cutoff because I noticed when I asked the questions that were in scope all the related documents never went past 5. 

One group was of relevant questions in scope that could be found in city_guides. The distance for these questions averaged around a 0.45. 
The other group of questions were out of scope and could never be answered with the documents found in city_guides. The distance average for these questions was arounf 0.85.

| Question | In corpus? | Best distance |
|---|---|---|
| Is there a pub in Elder Ness I can go for a drink on a Monday?" | guide_elder_ness.md | 0.3979 |
| "I just bought a bus ticket from operator Kestrelford, can I use it to ride the bus from operator Halden Bay?" | guide_regional_transport.md | 0.4474 |
| "I am stranded in Marchwood, what district should I stay at?" | guide_marchwood.md | 0.4529  |
| "I am 55 years old and would love to go on a walk in Thornby Wells, do you recommend it?" |  guide_accessibility.md | 0.4773 |
| "Is business booming around the coast in November?" | guide_seasons.md | 0.4954 |
| "What is the capital of Mongolia?" | guide_seasons.md | 0.7542 |
| "How do I write a for loop in Rust?" | guide_corry_vale.md | 0.8130 |
| "What is the recommended dosage of ibuprofen for a headache?" | guide_walking.md | 0.8459 |
| How do I change the oil in a diesel engine?" | guide_brightwater.md | 0.8917 |
| "Who won the 1994 World Cup?" | guide_regional_transport.md | 0.8990 |

## How I Used AI

<!-- Milestone 5. -->

**1.**
The chunking function used in milestone 3 implemented initially paired each header with only its immediately following paragraph. This caused for missed retrievals and context loss for multi-paragraph sections in city_guides. I then told my coding agent to update the logic to group each header with all subsequent paragraphs until the next header is reached.

**2.**
I asked for an explanation of the output from running python app.py retrieve "question". It brokedown an explantion of the distance metric between the query and retrieved documents. I adjusted the distance threshold value based on that understanding to optimize retrieval quality.

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |
| 3 |  |  |  |
| 4 |  |  |  |
| 5 |  |  |  |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 |  |  |  |  |
| 2. Every answer names a source | 5 of 5 |  |  |  |  |
| 3. Gate stops out-of-corpus questions | 4 of 5 |  |  |  |  |
| 4. | | | | | |
| 5. | | | | | |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
