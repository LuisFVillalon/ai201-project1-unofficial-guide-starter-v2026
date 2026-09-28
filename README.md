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

All my documents contain headelines and paragraphs that are about the topic in that headline. Each document regards a specific topic or county.

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
| 1. Retrieved chunk contains the answer | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 2. Every answer names a source | 5 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks are complete and say which town they're about | ≥95% end in punct; no chunk <100 chars; 100% name town | 95.9% / 4 short / 15.3% | 95.9% / 4 short / 15.3% | 95.9% / 4 short / 15.3% | MISSED |
| 5. Nonexistent towns get refused, not invented | 3 of 3 | 3/3 | 3/3 | 3/3 | MET |

### Real output

All output below is from `results/run_2026-09-27_2238_before.md`.

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `city_guides` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.5
- Runs per question: 3, caching off
- When: 2026-09-27 22:38

**Criteria 1 and 2** — the five answers from run 1. Each one contains the
expected answer and names at least one source file.

#### Is there a pub in Elder Ness I can go for a drink on a Monday? — run 1

- Best distance: 0.3979 (passed the gate)
- Sources retrieved: guide_corry_vale.md, guide_eating.md, guide_elder_ness.md, guide_kestrelford.md

```
No, you cannot. Elder Ness has one pub, but it is closed on Mondays (guide_elder_ness.md and guide_eating.md).
```

#### Is business booming around the coast in November? — run 1

- Best distance: 0.4954 (passed the gate)
- Sources retrieved: guide_halden_bay.md, guide_kestrelford.md, guide_pellew_sands.md, guide_seasons.md

```
No, business is not booming around the coast in November. According to `guide_seasons.md`, coastal businesses begin closing by November, and days are short. Additionally, `guide_halden_bay.md` states that much of the food and drink businesses close entirely from November to February.
```

#### I am stranded in Marchwood, what district should I stay at? — run 1

- Best distance: 0.4529 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_marchwood.md

```
You should stay in the Northgate district (`guide_marchwood.md`).
```

#### I am 55 years old and would love to go on a walk in Thornby Wells, do you recommend it? — run 1

- Best distance: 0.4773 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_regional_transport.md, guide_thornby_wells.md, guide_walking.md

```
Yes, I recommend it. Thornby Wells has flat, formal gardens and level streets, making it the region's most accessible town on foot (guide_walking.md). It is also described as flat, compact, and with level pump rooms and gardens (guide_accessibility.md).
```

#### I just bought a bus ticket from operator Kestrelford, can I use it to ride the bus from operator Halden Bay? — run 1

- Best distance: 0.4474 (passed the gate)
- Sources retrieved: guide_accessibility.md, guide_eating.md, guide_regional_transport.md, guide_seasons.md

```
No, you cannot. Three operators run in the region and they do not accept each other's tickets (*guide_regional_transport.md*).
```

**Criterion 3** — produced by `run_eval.py::check_out_of_scope`, cutoff 0.5.
Refused 5 of 5. Retrieval is deterministic and the gate is a comparison
against a fixed number, so this is one pass, not three.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.754 | refused |
| How do I change the oil in a diesel engine? | 0.892 | refused |
| Who won the 1994 World Cup? | 0.899 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.846 | refused |
| How do I write a for loop in Rust? | 0.813 | refused |

**Criterion 4** — produced by `check_chunks.py::report`, measuring the chunks
that `chunker.py::split_documents` produces. No model calls and no retrieval,
so the number is the same every run.

```
$ python check_chunks.py
98 chunks, produced by chunker.py::split_documents

1. Chunks ending on . ! or ?
   94/98 = 95.9%   target >= 95%
   MET

2. Chunks under 100 characters
   4   target 0
   MISSED
     guide_eating.md#0  (26 chars)  '# Eating across the region'
     guide_regional_transport.md#0  (27 chars)  '# Getting around the region'
     guide_seasons.md#0  (26 chars)  '# When to visit the region'
     guide_walking.md#0  (23 chars)  '# Walking in the region'

3. Town-guide chunks naming their town
   11/72 = 15.3%   target 100%
   MISSED
   61 chunks do not name their town, for example:
     guide_brightwater.md#1  '## Getting there'
     guide_brightwater.md#2  '## Getting around'
     guide_brightwater.md#3  '## Eat and drink'
     guide_brightwater.md#4  '## What to see'
     guide_brightwater.md#5  '## Where to stay'
```

Two of the three parts missed, so the criterion as a whole is MISSED. The four
short chunks are all the same thing: a document's `# Title` line with no body
under it, because `_split_by_heading` cuts at every heading level and the title
of a region-wide guide is followed immediately by a `##` section. The town-name
result is the bigger miss — 15.3% against a target of 100% — and the cause is
visible in the examples: the nine town guides use identical section headings,
so a chunk reading "## Eat and drink" is indistinguishable from the same
section of the other eight guides once it leaves its file.

**Criterion 5** — produced by `app.py::cmd_ask`, run by hand against three
plausible town names that are not in the corpus. Refused 3 of 3, no invented
details.

| Fake-town question | Best distance | Result |
|---|---|---|
| Where should I stay in Ashcombe Ferry? | 0.519 | "I don't have enough information about that." |
| Is there a pub in Netherby Cross? | 0.566 | "I don't have enough information about that." |
| How do I get to Wrenmoor by bus? | 0.549 | "I don't have enough information about that." |

```
$ python app.py ask "Where should I stay in Ashcombe Ferry?"
  (best distance 0.519, cutoff 0.5)

I don't have enough information about that.

0 model calls this session
```

All three were stopped by the relevance gate, not by the model declining — the
run reports `0 model calls`, so no fake-town question ever reached it. My
stated reason for this criterion assumed the model would have to refuse on its
own, and that isn't what happened. The margin is also thin: 0.519, 0.549 and
0.566 against a cutoff of 0.5. A fake town whose name sits closer to the real
guides would pass the gate and reach the model untested, so 3/3 here says the
gate is holding, not that the model refuses to invent towns.

**Per-question pass/fail**, produced by `run_eval.py::main` scoring each
answer with `scorer.py::judge`. This is the summary the criterion table
above was aggregated from.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| Is there a pub in Elder Ness I can go for a drink on a Monday? | pass | pass | pass |
| Is business booming around the coast in November? | pass | pass | pass |
| I am stranded in Marchwood, what district should I stay at? | pass | pass | pass |
| I am 55 years old and would love to go on a walk in Thornby Wells, do you recommend it? | pass | pass | pass |
| I just bought a bus ticket from operator Kestrelford, can I use it to ride the bus from operator Halden Bay? | pass | pass | pass |

> **Note on `expects`:** my original `expects` values in `questions.py` were
> full sentences, which `scorer.py`'s substring match can never satisfy, so the
> first run scored 0/5. I shortened each to the key phrase — "Northgate",
> "closed", "do not accept" — without changing what I considered a correct
> answer.

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | Retrieved chunk contains the answer (4 of 5) | MET | 5/5 in all three run. In each run the file that holds the answer was among the retrieved sources, and the expected phrase in the answer were found. |
| 2 | Every answer names a source (5 of 5) | MET | I checked all 15 logged answers (5 questions × 3 runs), not just run 1. Each one names at least one corpus file. |
| 3 | Gate stops out-of-corpus questions (4 of 5) | MET | 5/5 refused. The nearest out-of-scope question is 0.25 above the 0.5 cutoff, and the in-scope questions all sit below it (0.398–0.495). The gate is a fixed comparison on deterministic distances, so one pass shows the same result all three runs would. |
| 4 | Chunks are complete and name their town (≥95% punct; 0 under 100 chars; 100% name town) | MISSED | All three parts must hold, and two failed. Punctuation passed narrowly (95.9% against 95%). There were 4 chunks under 100 characters against a target of 0. Only 15.3% of town-guide chunks name their town, against a target of 100%. The numbers are nowhere near the target. |
| 5 | Nonexistent towns get refused (3 of 3) | MET | By the wording of the target it's met: all three questions got "I don't have enough information about that" and no invented details. But the relevance gate did the refusing, not the model. I'm calling it MET on what the target says, and flagging that it held for a different reason than the one I expected. |

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

     Criterion 4 — MISSED. Stage: chunking. Both failed parts come from one cause: chunker.py::_split_by_heading cuts at every heading level, including the document's # Title.
     
          - 4 chunks under 100 characters. In the four region-wide guides (eating, regional_transport, seasons, walking), the # Title line is followed immediately by a ## section, so the title becomes a chunk on its own with no body, 23–27 characters long.
     
          - Only 15.3% of town-guide chunks name their town. The town's name appears only in the # Title, which stays in chunk #0. Every later section starts with a generic heading like ## Eat and drink or ## Getting there, and all nine town guides share those headings. Once one of those chunks leaves its file, nothing in its text says which town it describes. 
     

## The Improvement

**What I changed:**

In chunker.py::_split_by_heading, the # Title is no longer a split point, and it is added to the start of every section chunk from that file. 

**Why I picked it:**

My criterion 4 diagnosis traced both failures (title-only chunks under 100 characters, and chunks that don't name their town) to one cause: _split_by_heading splits at every heading level, including the # Title. This change goes after that cause directly.

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | 4/5 | 4/5 | 4/5 | MET |
| 2. Every answer names a source | 5 of 5 | 4/5 | 4/5 | 4/5 | MISSED |
| 3. Gate stops out-of-corpus questions | 4 of 5 | 5/5 | 5/5 | 5/5 | MET |
| 4. Chunks are complete and say which town they're about | ≥95% end in punct; no chunk <100 chars; 100% name town | 100% / 0 short / 100% | 100% / 0 short / 100% | 100% / 0 short / 100% | MET |
| 5. Nonexistent towns get refused, not invented | 3 of 3 |	3/3 | 3/3 | 3/3 | MET |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

Partly. The modification in my chunking strategy fixed criterion 4 but broke criterion 2.

- **Fixed:** Criterion 4 went from MISSED to MET. Before, 4 chunks were under 100 characters and only 15.3% of town-guide chunks named their town. Now 0 chunks are under 100 characters (shortest is 174) and 100% of town-guide chunks (72/72) name their town.
- **Broke:** Criterion 2 went from MET to MISSED. The Thornby Wells walking question's best distance went from 0.4773 to 0.5046, just over the 0.5 relevance cutoff, so the gate refused it in all 3 runs and it got no answer or source.
- **Side effect:** One of the three fake-town questions, "How do I get to Wrenmoor by bus?", now passes the gate (0.549 → 0.478). In all 3 runs the model declined on its own, saying the documents don't mention Wrenmoor, and invented nothing. The other two fake towns were still refused by the gate.

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
