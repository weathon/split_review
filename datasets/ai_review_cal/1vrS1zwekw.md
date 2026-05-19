- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 5, 6, 6
Now I have verified all claims against the paper. Let me produce the consolidated review.

---

## Summary

This paper proposes **Scale Tasks Per Input (STPI)**, a new paradigm for constructing instruction-following datasets. Unlike prior work that either scales (input, output) pairs per instruction (*ScaleInput*) or scales instruction-only tasks (*ScaleInputFree*), STPI diversifies task instructions *per input* so the model learns to follow different instructions about the same input. The authors instantiate this paradigm with **MUFFIN**, a 68K-instance dataset built via (1) facet-based instruction brainstorming, (2) instruction rematching from existing human-written sets, and (3) classification expansion to balance task types. Experiments on T5-3B, T5-11B, and Llama2 across four zero-shot benchmarks (SuperNI-Test, MMLU, T0-Eval, BBH) show that models tuned on MUFFIN outperform those tuned on datasets from both prior paradigms, with corroborating human evaluation, ablation, scaling, and mixing analyses.

---

## Strengths

1. **Novel and well-motivated paradigm.** The STPI paradigm is clearly defined and grounded in a concrete diagnosis of *ScaleInput* (excessive input sensitivity) and *ScaleInputFree* (poor handling of input-dependent tasks). The paper does not merely swap data sources — it proposes a structurally different way of constructing training data.

2. **Consistent empirical superiority across model scales and benchmarks.** Models tuned on MUFFIN achieve higher scores on 3 of 4 zero-shot benchmarks than models trained on 8 direct-comparison baselines (SelfInst, Unnatural, Dynosaur, Dolly, LongForm, Alpaca, AlpacaGPT, WizardLM). The advantage holds for T5-3B, T5-11B, and Llama2, and the margin grows with model scale (4.42 → 8.03 average improvement over the strongest baseline from 3B to 11B).

3. **Human evaluation with both acceptance ratios and pairwise comparisons.** The two-stage blind evaluation (Section 6.2) provides strong corroboration of the automatic results. MUFFIN wins pairwise against SelfInst, Unnatural, and the human-annotated SuperNI on 3 of 4 benchmarks, with a clear protocol (5 volunteers, random assignment, blind annotation).

4. **Scaling and mixing analyses strengthen the paradigm claim.** Figure 5 shows that MUFFIN at 68K instances outperforms baselines even when they are scaled to several times that size; some baselines even degrade with more data. Figure 6 shows that mixing MUFFIN with SuperNI hurts performance, supporting the claim that the paradigm itself matters more than raw data quantity or quality.

5. **Ablation isolates each module's contribution.** The ablation on the SuperNI validation set (Table 5) cleanly separates the effects of rematching, brainstorming, and classification expansion, with classification expansion specifically improving EM on classification tasks by ~3 points.

---

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **No variance or significance reporting for automatic metrics.** All main results (Table 1, Table 2, etc.) are reported as single numbers without standard deviations, confidence intervals, or significance tests. While common in LLM work, this makes it impossible to gauge whether a 1–2 point gap is reliable. The human evaluation partly mitigates this, but the core automatic claims would be strengthened by multi-seed reporting or significance testing on the main comparisons.

2. **Instruction rematching leakage analysis covers semantics but not strict task-ID identity.** The paper addresses the leakage concern (Q2) with embedding cosine similarity and ChatGPT-based task overlap estimation, and shows MUFFIN has low similarity with SuperNI-Test. However, a stricter check would verify that no rematched instruction corresponds to the *same task definition* as any test task at the task-ID level. Given that SuperNI-Test is the benchmark where MUFFIN shows the largest gains, this tighter verification would definitively rule out one plausible validity threat. The existing evidence is reasonable, not airtight at this granularity.

3. **Mixing result lacks deeper analysis.** The finding that combining MUFFIN with SuperNI hurts performance (Figure 6) is honestly reported and interesting, but the paper only offers a plausible speculation ("different dataset paradigms do obviously have various impacts"). No analysis of optimization dynamics (loss curves, gradient conflict, or data characteristics) is provided to explain *why* the paradigms conflict. This is a missed opportunity to sharpen the paradigm claim.

### Trivial
None.

---

## Nice-to-Haves

- **Controlled paradigm-isolation experiment:** A small-scale experiment where the same input set is used to construct datasets under all three paradigms at the same size would isolate the paradigm effect from data-source differences. The paper's evidence is already strong, but this would preempt the most obvious counterargument.
- **Loss curves or gradient analysis for the mixing result** would deepen understanding of why paradigms conflict rather than complement each other.

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Human evaluation details missing (number of volunteers, inter-annotator agreement)"** — The paper *does* state these: "5 graduate-level volunteers" (line 210), "each volunteer is randomly responsible for 1 or 2 models" (line 210), and "average agreement of 83.3%" (line 140). The criticism is factually incorrect.
- **"Missing appendix / Table Renze not visible"** — The critic notes that the ChatGPT-based task overlap table is "likely in the appendix, which is stripped." Weaknesses about absent appendix content are removed per policy, as these sections exist in the original submission.
- **Generic concern about "could the metric be measuring a proxy?"** — Appears in the harsh critic's general sweep but has no concrete anchor in the paper's evaluation. Removed for lack of specificity.
- **Strength Finder items about the problem being "important"** — Generic framing ("this paper addresses an important problem") removed. Only specific, evidence-grounded strengths are retained.
- **Strength Finder claim that "data quality validated by human annotation" conflicts with no other weakness** — Retained as it is factual and specific to the paper's Section 4.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews generally converge on the paper's strengths and identify the same minor gaps, with no contradictory assessments or surprising observations.

---

## Suggestions

1. Add standard deviations (or min/max range over 2–3 seeds) to Tables 1 and 2 for the main automatic results.
2. Report a strict task-ID level overlap check between rematched instructions (from SuperNI training) and SuperNI-Test task definitions, to complement the existing embedding-similarity analysis.
3. Add a brief analysis of why mixing MUFFIN with SuperNI hurts performance — e.g., per-task loss dynamics or a simple characterization of where the conflict arises.

---
