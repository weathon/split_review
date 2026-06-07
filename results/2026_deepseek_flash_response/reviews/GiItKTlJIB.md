## Summary

This paper introduces a deletion-based probing framework to evaluate how much LLMs genuinely depend on CoT traces for physics problem solving. By intercepting CoT mid-generation, deleting tokens under three strategies (end, random, physics-aware), and measuring downstream accuracy, answer length, and information overlap, the paper finds that models maintain accuracy under moderate deletions (40–60%) through "cramming" — reconstructing missing reasoning steps in final answers. The study covers three open-source models (Magistral, Phi-4, Qwen-A3B) across three physics benchmarks.

## Strengths

- **Novel deletion-based probing methodology.** The framework of systematically deleting CoT tokens mid-generation and measuring downstream effects is a genuinely different approach from prior faithfulness work that relied on post-hoc analysis or input-level perturbations (Lanham et al., Turpin et al., Lyu et al.). The three deletion strategies (end, random, physics-aware) give complementary views of how models respond to missing reasoning content. The method is clearly specified and the experimental pipeline is illustrated in Figure 1.

- **Systematic identification of "cramming" as a compensatory behavior.** The paper documents that answer length increases as CoT tokens are deleted, producing a consistent X-shaped pattern (Figures 5 and 6) across all three models and datasets. This is a non-obvious finding — models do not simply produce shorter, worse answers under deletion; they actively produce longer answers that attempt to reconstruct missing reasoning. The convergence of evidence across three deletion strategies and three models strengthens this finding.

- **Controlled comparison across three deletion strategies reveals informative differences.** The finding that physics-aware deletion degrades accuracy more slowly (70–80% threshold) than end deletion (~40%) or random deletion (~60%) is a genuine empirical contribution. It suggests that domain-relevant information is somewhat redundant or recoverable, while sequential truncation disrupts reasoning more quickly. This kind of controlled ablation goes beyond prior work using single ablation types.

- **Calibration study establishing sample sufficiency.** The convergence analysis (Section 3.1) showing that ~5 prompt repetitions per condition reduce relative error bars below 10%, with bootstrapped confidence intervals over 50 UG-Physics questions, is methodologically careful and uncommon in this literature.

## Weaknesses

### Major

1. **Bag-of-words overlap metrics are a poor fit for the faithfulness analysis.** The paper claims that physics's "clear structure—equations, units, and terminology—enables precise quantification" (line 35–36), but then uses Jaccard similarity and Manhattan distance on bag-of-words vectors, which discard precisely that structure. Physics reasoning involves equations with specific relationships between variables — bag-of-words cannot distinguish between a model that faithfully reconstructs F = ma using momentum notation (Δp/Δt) and one that merely outputs generic physics vocabulary with incorrect relationships. The paper's own Section 4.2 acknowledges that overlap reflects "surface-level similarity rather than genuine fidelity," but the core claim of a "rigorous faithfulness analysis" (contribution 3, line 35) is overstated given these metrics. Given that the cramming and faithfulness analysis is one of the paper's three stated contributions, this mismatch between the stated motivation and the actual metrics substantially weakens the evidence.

2. **LLM-as-judge metric lacks validation against a ground-truth correctness signal.** The primary accuracy metric (Score) is Claude-4 Sonnet scoring answers 0–1 based on a holistic rubric combining correctness, derivation accuracy, logic, formatting, and clarity. There is no human baseline, inter-annotator agreement study, or complementary objective metric (e.g., "is the final numerical answer correct?") to validate the judge. The same model is also used for physics-aware token identification — while this is not a true circularity (different pipeline stages), it compounds the concern about independent verification. An objective correctness check alongside the judge score would substantially strengthen the central accuracy-robustness claim.

### Minor

1. **Claims of "stability" thresholds lack statistical rigor.** The paper states accuracy remains "stable" until ~40% (end deletion) or ~60% (random deletion), but this is a qualitative visual assessment. The figures (e.g., Figure 4) show accuracy declining monotonically from 0% deletion — "stable" and "collapsing" are not tested with significance tests or confidence intervals on the difference from baseline. Given the temperature range (0.6–0.7) introduces sampling variance, statistical testing would meaningfully strengthen the claim.

2. **Underspecified deletion implementation.** The paper describes "intercepting CoT mid-generation" and "removing tokens before decoding" (lines 17, 29, 33) but does not clarify whether this uses offline modification (generate full CoT, parse at delimiter, delete, restart from modified prefix) or online KV-cache manipulation. These approaches differ in how they affect the distribution the model sees — offline modification introduces a discontinuous prefix. This is a standard implementation detail that can be clarified, but its absence is a gap for reproducibility and interpretation.

3. **Dataset sizes partially reported.** PhysReason is stated as 1,200 problems, but UG Physics and PhyBench sizes are not given in the main text. This makes it difficult to assess statistical power per condition, especially since the calibration study used only 50 UG-Physics questions.

4. **The "cramming" interpretation could benefit from a control condition.** The observation that answer lengths increase when CoT is deleted could partly reflect a simpler statistical tendency: a shorter prefix leads the model to generate more output tokens to reach a complete answer. The information-overlap analysis partially addresses this, but a control condition (e.g., deleting tokens from an unrelated physics passage of similar length) would more cleanly distinguish "genuine reasoning reconstruction" from "generic output-length distribution."

### Trivial

- The paper writes "Magistral" and "Magistrall" (line 59) — if this refers to Mistral's models, the name should be corrected for consistency.
- Figure reference ordering is unconventional (Figure 4 described textually before Figure 3 in places).

## Nice-to-Haves

- Equation-level or symbolic matching (e.g., using sympy for normalized equation comparisons) would transform the overlap analysis from a vocabulary check into a genuine faithfulness test.
- Lower-temperature (e.g., T=0.1) sensitivity analysis to isolate reasoning effects from sampling variance.
- Human evaluation on a subset to validate the LLM judge scores.

## Removed Points

These points were raised in the reviews but are removed for the reasons stated:

- **Harsh critic Issue 1 (LLM-as-judge circularity is fatal):** Downgraded from fatal to minor. The paper provides the judge with the expected answer for direct comparison (line 108), which significantly mitigates the circularity concern. The underlying concern about the holistic rubric mixing correctness with presentation factors is valid but not fatal.
- **Harsh critic Issue 3 (implementation speculation about KV-cache):** Removed as speculative. The critic's detailed technical objection about KV-cache consistency assumes a specific implementation that the paper does not claim. With open-source models, one can regenerate from the modified prefix straightforwardly.
- **Strength Finder claim 3 ("rigorous physics-structured overlap quantification"):** Merged into weakness 1. The strength was overstated — the overlap metrics are not as rigorous as claimed.
- **Generic strengths about "addressing an important problem":** Removed as they lack specific evidence from the paper.
- **Observations about missing appendix content:** Removed per instructions (parser strips these).
- **Formatting/style nitpicks and typo criticisms:** Removed per instructions (parser artifacts or not substantive).

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an observation about the paper that the paper itself does not already make. The harsh critic's point about the bag-of-words metrics being a poor fit is a critique, not a novel insight about the subject matter.

## Suggestions

1. **Replace or supplement bag-of-words overlap with domain-aware matching.** Normalize equation strings (e.g., using sympy) to check mathematical equivalence regardless of variable names; check numerical values and unit conversions. This would leverage the very property (physics's structured content) that the paper claims enables precise quantification.
2. **Add a complementary objective correctness metric.** A simple binary check (is the final numerical answer correct?) alongside the judge score would disentangle answer correctness from derivation quality and make the accuracy-robustness claim much more convincing.
3. **Report confidence intervals or statistical tests for deletion thresholds.** Assess whether accuracy at 30% deletion is significantly different from baseline.
4. **Clarify the deletion implementation** (offline prefix modification vs. online inference manipulation).
5. **Add a control condition** deleting tokens from an unrelated passage (not the model's own CoT) to verify that cramming is specific to reasoning reconstruction.

---

## Calibration Anchors

| Path | Avg Score | Round | Comparison to Paper |
|------|-----------|-------|-------------------|
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/1OyE9IK0kx.md` (On the Hardness of Faithful CoT Reasoning) | 5.00 | 1 | Similar topic (CoT faithfulness). The current paper has more novel methodology and more concrete findings, making it somewhat stronger. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/lUyYX9VFgA.md` (Code-of-thought prompting) | 3.00 | 1 | Much weaker paper — poorly executed. Current paper is clearly stronger. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/pXIbcRPxWR.md` (Supervised Chain of Thought) | 2.50 | 1 | Much weaker — theoretical paper with limited experimental support. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/asGQQc7gNo.md` (Is Factuality Enhancement a Free Lunch) | 6.67 | 1 | Better executed — more comprehensive experiments, cleaner evaluation. Current paper is weaker. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/awtd0XhzKQ.md` (FLARE) | 5.75 | 1 | Different genre (method paper). Comparable quality but the current paper has clearer writing and more novel empirical findings. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/rpbzBXdo4x.md` (Mind Your Step) | 5.00 | 2 | Similar genre (empirical CoT study). Comparable quality — both have interesting findings but evaluation limitations. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ZyLkNVHBZF.md` (How Far Is Video Generation from World Model) | 5.50 | 2 | Similar in having a well-motivated research question but evaluation metrics that don't fully deliver. Comparable quality. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/CIN2VRxPKU.md` (Evaluating Deep Unlearning) | 5.33 | 2 | Different topic but similar evaluation-oriented contribution. Comparable quality. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/3GTtZFiajM.md` (Justice or Prejudice) | 6.75 | 2 | Better executed — systematic bias quantification framework. Current paper is weaker. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/87YOFayjcG.md` (JudgeLM) | 5.25 | 2 | Different topic (training LLM judges). Comparable quality of execution. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/9OevMUdods.md` (Towards Understanding Factual Knowledge) | 6.75 | 2 | Better executed — comprehensive benchmark. Current paper is weaker. |
| `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/t15cWqydys.md` (Inferring from Logits) | 3.00 | 1 | Much weaker — narrow focus, limited contribution. |

**Round 1 Bracket:** [4.5, 6.5] — The paper is clearly above poorly-executed papers (scores 2.5–3.0) and clearly below top-tier papers (scores 7.5+).  

**Round 2 Narrowing:** Comparing against anchors at 5.00 (Faithful CoT, Mind Your Step), 5.33 (Deep Unlearning), 5.50 (Video Generation/Physics), and 5.75 (FLARE), the current paper sits in the 5.0–5.75 range. It is somewhat stronger than the 5.00 anchors (more novel methodology, more concrete findings) but not as strong as the 5.75–6.67 anchors (less rigorous evaluation, weaker metrics). The bag-of-words overlap metrics and unvalidated LLM judge prevent it from reaching the 6+ tier.

**Final Score:** 5.5 — This reflects a solid empirical paper with a genuinely novel methodology and interesting findings, held back by evaluation metrics that don't fully deliver on the paper's stated promises.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>