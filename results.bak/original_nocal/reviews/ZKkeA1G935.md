Now I have all the information needed. Let me compose the consolidated review.

## Summary

This paper studies whether large language models (LLMs) can mitigate catastrophic forgetting in Graph Continual Learning (GCL). It makes three contributions: (1) identifying task ID leakage in the common "local testing" evaluation paradigm and advocating for the more realistic "global testing" setup; (2) introducing LLM4GCL, a comprehensive benchmark evaluating 9 LLM-/GLM-based methods across 7 textual-attributed graphs; and (3) proposing SimGCL, a simple two-stage method (first-session graph-prompted instruction tuning + training-free prototype classification) that achieves state-of-the-art results on most datasets.

## Strengths

1. **Clear diagnosis of a flawed evaluation paradigm.** Section 3.1 and Table 1 convincingly demonstrate that under local testing, even a trivial mean-pooling prototype achieves 100% task ID prediction accuracy and 0% forgetting ratio — exposing widespread inflation in prior reported GCL performance. This is a well-motivated and empirically grounded contribution.

2. **First comprehensive benchmark for LLMs in GCL.** LLM4GCL integrates 9 methods across 7 TAG datasets spanning multiple domains and scales, with standardized NCIL and FSNCIL settings (Tables 2–4). Prior GCL benchmarks included only GNN-based methods; this fills a genuine gap and should facilitate future research. The code is released as an easy-to-use platform.

3. **SimGCL achieves strong results on the majority of datasets.** On 5 out of 7 datasets in both NCIL and FSNCIL, SimGCL substantially outperforms all prior GNN-, LLM-, and GLM-based baselines (e.g., +21.7% over SimpleCIL on Cora NCIL; +18.0% on Citeseer FSNCIL). The gains are often large and consistent, supporting the claim that combining graph-prompted instruction tuning with training-free prototypes is a promising direction.

4. **Systematic empirical analysis.** The eight key observations (Obs. ❶–❽) extract actionable insights grounded in the data — e.g., the persistent weakness of GNN-based methods, the effectiveness of prototype-based approaches, and the impact of model scaling — that guide future work beyond the proposed method itself.

## Weaknesses

### Fatal
None.

### Major

1. **Overclaim of "consistently overperforms" contradicted by the paper's own data.** Obs. ⑧ states that SimGCL "consistently overperform[s] other baselines (23 out of 28)," but SimpleCIL (a simpler, graph-agnostic LLM baseline) beats SimGCL by large margins on Arxiv-23 in both NCIL (+13.7% Ā, +25.2% A_N) and FSNCIL (+18.0% Ā, +29.7% A_N), and on Arxiv (FSNCIL, both metrics). Since SimpleCIL is explicitly listed among the LLM-based baselines, including it in the "overperform" claim is inaccurate. The paper acknowledges the Arxiv-23 limitation but does not resolve the tension: if the core methodological novelty of SimGCL is its graph-aware prompting, the fact that a graph-agnostic method (SimpleCIL) often matches or exceeds it on several datasets weakens the central argument. The authors should substantially qualify these claims (e.g., "SimGCL outperforms baselines on most datasets, with notable exceptions on sparse-graph and long-session settings").

### Minor

2. **No ablation isolating the effect of the graph-aware prompt.** The paper does not compare SimGCL against a variant that uses only node text (without ego-graph descriptions) in the prompt. This makes it impossible to attribute the method's gains to structural understanding vs. the LLM's intrinsic text ability. Similarly, no ablation compares LoRA-tuned vs. fully frozen LLM backbones to assess whether instruction tuning helps or overfits. These ablations are standard for a method whose novelty rests on graph-prompted tuning.

3. **No statistical validation.** All results are reported as single values without standard deviations, confidence intervals, or multi-seed runs. Some claimed improvements are modest (e.g., SimGCL vs. SimpleCIL on WikiCS NCIL: 73.5 vs. 71.4, a 2.1% gain), and several counterexamples (SimpleCIL beating SimGCL) could fall within noise. Without error bars, the empirical case for the method's superiority is weaker than it should be.

4. **SimGCL's final accuracy collapses under long sessions.** Table 4 shows that on the 2W20S configuration (Arxiv), SimGCL's A_N drops to 17.5 while SimpleCIL achieves 39.1. Although the average accuracy Ā remains strong (57.4 vs. 52.6), the low final accuracy indicates severe forgetting in the last sessions. The paper attributes this to overfitting but does not provide per-session trajectory analysis to validate this explanation or compare with SimpleCIL's forgetting pattern.

5. **Missing analysis of why SimGCL fails on Arxiv-23 while SimpleCIL succeeds.** The paper speculates that Arxiv-23's sparse graph structure is the cause, but this does not explain why SimpleCIL (which ignores graph structure) succeeds. A concrete analysis of prototype quality (e.g., intra-/inter-class prototype similarity) on this dataset would clarify whether the graph prompt actually degrades the representations rather than enhancing them.

### Trivial
None.

## Nice-to-Haves
- An analysis of per-session accuracy trajectories for Table 4 to diagnose when and why SimGCL's final accuracy collapses relative to SimpleCIL.
- t-SNE/PCA visualization of prototypes on a dataset where SimGCL wins (e.g., Cora) and one where it loses (Arxiv-23) to show whether the graph prompt improves class separation.
- Including a small-buffer replay baseline (while the paper focuses on rehearsal-free settings, a comparison would contextualize the prototype approach).

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Global testing may also have task-ID leakage"** (Harsh Critic #3): The paper provides empirical evidence that global testing eliminates the specific leakage mechanism — TPP collapses from near-100% accuracy (Table 1, local testing) to 12–45% (Table 2, global testing). The concern is speculative and not supported by any evidence in the paper.
- **"CoRa typo"** and **"Prototype formula K notation reuse"**: These are trivial formatting/notation issues that do not affect the paper's substance.
- **"No citation of prior critique of local testing"**: This is a missing related-work reference that cannot be authoritatively assessed and does not affect the paper's own valid contribution.
- **"Even minor modifications can lead to outstanding results is vague"**: A subjective phrasing nitpick about the abstract's tone.
- **From Strength Finder — overbroad strength claim** ("large and consistent improvements over ALL existing baselines"): The concrete evidence (23/28 entries strongest) is retained in Strengths above, but the "all" framing is removed since SimpleCIL outperforms SimGCL on specific datasets.

## Novel Insights
None beyond the paper's own contributions. The synthesis of the two reviews does not surface any novel observation about the paper that is not already stated in its text.

## Suggestions
1. Tone down the "consistently overperforms" claim and explicitly discuss the failure cases (Arxiv-23, long-session A_N) alongside the successes.
2. Add ablation studies: (a) SimGCL with text-only prompts (no graph structure), (b) SimGCL without LoRA tuning (frozen LLM). These are essential to validate the contribution of the graph-prompting component.
3. Report standard deviations over at least 3 random seeds for the main comparisons (SimGCL vs. SimpleCIL across all datasets).
4. Add per-session accuracy tracking for the long-session experiments (Table 4) to reveal when forgetting accelerates and why SimpleCIL maintains higher final accuracy.
5. Include a direct analysis of prototype quality (e.g., intra- vs. inter-class similarity) on Arxiv-23 to explain why the graph prompt underperforms the text-only baseline.

## Score and Decision

This paper makes a meaningful contribution by exposing the task-ID leakage problem and establishing a new benchmark for LLMs in GCL. The proposed SimGCL method is effective on most datasets but suffers from overclaimed generality, missing ablations, and no statistical validation. These weaknesses are addressable with revisions and do not invalidate the paper's core contributions.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>