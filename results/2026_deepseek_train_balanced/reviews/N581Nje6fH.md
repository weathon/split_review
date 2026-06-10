## Summary

This paper proposes three modifications to TransformerXL for long-horizon robotic decision-making: (1) **Automatic Chunking** — splitting the memory into chunks and attending only to the top-k relevant chunks, (2) **ForgetSpan** — a learned soft-masking mechanism that gradually removes memory elements after a learned span of time, and (3) **SimilarityWeight** — deduplication of observations before storage based on cosine similarity binning. The methods are tested on three custom tasks (Minigrid Memory Task, Audio-Visual Instructions, Visual Corridor with Variable Distractor) using Unity ML-Agents and Minigrid environments.

---

## Strengths

- **Differentiable soft-masking for ForgetSpan (Section 2.2, Eq. 4).** The ramp-based masking function $s_{ti}=max(0,min(1,1+r_{ti}/R))$ provides a non-zero gradient region $[-R,0]$, enabling end-to-end training of the forgetting span $f_i$ through backpropagation rather than requiring hard eviction. This is a principled design choice that avoids non-differentiability issues.

- **Per-episode training time reported across configurations (Section 3.1).** The paper provides wall-clock training times (17s baseline, 46s AC, 20s AC+FS, 42s AC+FS+SW) that allow readers to quantitatively assess the computational trade-off introduced by each component, particularly the 46s→20s reduction when ForgetSpan is added to Automatic Chunking.

- **Ablation testing on the Minigrid task (Section 3.1).** Four configurations (baseline, AC, AC+FS, AC+FS+SW) are compared on the same task with training curves and timing data, providing the most complete evaluation in the paper.

---

## Weaknesses

### Major

- **Methods are critically underspecified (Sections 2.1–2.3), making the contribution difficult to assess or reproduce.** Automatic Chunking is described in a single paragraph: chunk size is never stated, what serves as the query for attending over chunk mean vectors is not specified, and how the top-k chunks are "combined" (concatenation? summation? weighted average?) is not given. ForgetSpan provides equations but never states what maximum span $F$ was used in any experiment, nor gives the ramp length $R$ except implicitly in the results section without motivation. SimilarityWeight's "dynamic threshold" updates "every n timesteps" without specifying $n$ or the update rule. No training hyperparameters (learning rate, optimizer, batch size, number of episodes, number of seeds) are provided anywhere in the paper. The reader cannot determine whether the proposed mechanisms, as implemented, are the cause of the reported results.

- **Only one baseline is used, and it is never defined.** All experiments compare against a single "Gated TransformerXL" baseline. The term "Gated" is never explained or cited — TransformerXL does not have a standard gated variant, and the paper provides no description of what gating mechanism is used or how it differs from the original TransformerXL. This makes it impossible to determine whether the baseline is reasonable or whether the paper is comparing against a strawman.

- **The paper's central claim about "memory efficiency" is never directly measured.** Despite being the headline contribution, no experiment reports memory buffer size over time, compression ratio, attention compute reduction, or any direct metric of memory savings. The only quantitative efficiency evidence is per-episode wall-clock time (Section 3.1), which conflates memory savings with implementation details, hardware, and other factors. For a paper titled around memory efficiency, the absence of any direct memory metric is a fundamental gap.

- **No statistical significance or variance reporting.** All experiments appear to be single runs. No error bars, confidence intervals, or multiple-seed results are reported for any configuration on any task. Given the high variance common in RL training, single-run results cannot be interpreted as reliable evidence.

- **Visual Corridor task omits the baseline entirely (Section 3.3).** The paper states "We only tested Automatic Chunking with ForgetSpan in this task" — the baseline TransformerXL is not compared against. This means the task that is supposed to demonstrate the methods in "a more dynamic scenario" provides no evidence that the proposed modifications outperform the unmodified architecture.

### Minor

- **SimilarityWeight is tested on only one of three tasks (Section 3.1 only).** The mechanism that the paper describes is evaluated exclusively on the Minigrid task and is absent from both the Audio-Visual and Visual Corridor tasks. No rationale is given for its omission. Since the mechanism also introduces significant computational overhead (42s vs 20s for AC+FS), its failure to generalize across tasks weakens the claim of a general-purpose improvement.

- **Generalization tests are thin.** The Audio-Visual generalization test (Section 3.2) reports only qualitative results ("most of the time") with no quantitative success rate. The Visual Corridor test (Section 3.3) varies only one parameter (distractor length) along the same dimension seen during training. No evaluation on unseen environments, different object types, different layouts, or sensor noise is conducted.

- **"Gated TransformerXL" baseline definition gap.** Beyond being the sole baseline, the term itself requires a citation or architectural description. This is a missing detail that a reader needs to interpret the results.

### Trivial

None that survive filtering.

---

## Nice-to-Haves

- Ablating each component on every task (plain TransformerXL, +AC only, +FS only, +AC+FS, +all three) would substantially strengthen the empirical story.
- Adding at least one standard benchmark (e.g., BabyAI, Meta-World) would allow external comparison against prior work.
- A direct plot of memory buffer size or attention compute over training time would directly support the memory efficiency claim.
- The SimilarityWeight mechanism would benefit from a clearer theoretical motivation for the binning-based formulation over a direct cosine-similarity threshold.

---

## Removed Points

These points were flagged during review but are removed as unreliable or inapplicable:

- **"Training times undermine efficiency claim"** — The critic asserted that every variant is slower than the baseline (17s), but the paper's claim is specifically that "computational cost was reduced greatly by ForgetSpan" when comparing AC+FS (20s) vs. AC (46s), not vs. baseline. This is a correct reading of the paper, and the criticism is based on a shifted reference point.
- **Typographical/formatting criticisms** ("chuck" vs "chunk", LaTeX typesetting issues, broken sentence fragments like "Automatic chunking and ForgetSpan are 0") — These are PDF extraction artifacts, not author errors, and are removed per the filtering rules.
- **"Abstract contains broken fragment"** — "Our model for tries to mimic" — likely a parser artifact; removed.
- **Calls for additional baselines (Compressive Transformer, Reformer, Longformer, etc.)** — These are valid references but requesting a full comparative evaluation against every sparse-attention method is scope creep for a paper that is already incomplete in its primary evaluation. Retained in spirit but moved here.
- **"No comparison against prior work" on similar benchmarks** — The tasks are custom environments, precluding direct comparison. This is a limitation but not a flaw per se; the paper's evaluation would be strengthened by standard benchmarks but the lack of them is not an error.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface the paper's central weaknesses — underspecified methodology, single undefined baseline, no direct memory efficiency measurement — rather than offering new technical insights about the approach itself. The soft-masking formulation for ForgetSpan (Eq. 4) is noted as a principled design choice by the Strength Finder, but this is visible in the paper itself.

---

## Suggestions

1. Fully specify all method parameters: chunk size, query mechanism for chunk-level attention, chunk combination method, $F$ and $R$ values per task, threshold update rule for SimilarityWeight, and all training hyperparameters.
2. Define or cite what "Gated TransformerXL" means; alternatively, use the standard TransformerXL as the sole baseline.
3. Add direct memory efficiency metrics: plot memory buffer size and attention compute over training for each configuration.
4. Report results over multiple seeds with error bars.
5. Include the baseline TransformerXL in the Visual Corridor evaluation.
6. Either evaluate SimilarityWeight on all tasks or clearly scope it as a preliminary / separate contribution.

---

## Score and Decision

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>