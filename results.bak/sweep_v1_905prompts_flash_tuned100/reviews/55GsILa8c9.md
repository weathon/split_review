My round-1 bracket: **5.5–6.5**. The narrowing pass (round 2) confirms this: the paper is comparable to MADGEN (6.00, accept) and ReNovo (6.50, accept), and clearly stronger than RankNovo (5.50, reject) and the causal instruction tuning paper (5.67, reject). I'll finalize at **6.0**.

Now let me write the consolidated review.

## Summary

This paper introduces CausalNovo, a model-agnostic framework that applies causal representation learning principles to *de novo* peptide sequencing from tandem mass spectra. CausalNovo uses a Structural Causal Model to motivate two principles — independence and sufficiency — and implements a Causality Extraction Module (CEM) that learns a soft importance mask over spectral peaks using information-theoretic objectives (contrastive independence loss, sufficiency/purification cross-entropy losses) alongside a replace-based causal intervention. Experiments across three benchmark datasets show consistent improvements (up to ~10%) over three strong baselines at amino acid, peptide, and PTM levels, with supporting analysis on noise robustness, cross-species generalization, and attention patterns.

## Strengths

**1. Well-motivated vulnerability analysis.** Figure 1 systematically shows that three state-of-the-art sequencing models (CasaNovo, AdaNovo, π-HelixNovo) degrade when noise peaks are perturbed, with precision dropping as the m/z tolerance tightens. This cleanly establishes the problem that CausalNovo addresses — that existing models rely on spurious correlations with non-causal peaks.

**2. Principled causal intervention grounded in domain knowledge.** The replace-based do-operation (Section 3.4.1) uses the theoretical spectrum — a well-established database-search concept — to identify non-causal ions, then replaces a fraction with noise from other spectra. This connects causal theory to a practical, interpretable operation that leverages established proteomics knowledge.

**3. Consistent gains across baselines, datasets, and metrics.** Tables 1 and 2 show that CausalNovo improves all three baselines on all three datasets across amino acid, peptide, and PTM metrics. On Seven-species, amino acid precision improves by +12.0% for CasaNovo and +9.1% for π-HelixNovo. These gains are not cherry-picked — they hold across the board.

**4. Mechanistic validation via attention analysis.** Table 7 shows that CausalNovo's top-three attended peaks include all three causal peaks in 32.87% of predictions versus 19.26% for the baseline, and that the baseline completely misses causal peaks in 12.73% of predictions versus 10.76% for CausalNovo. This directly links the framework's objectives to actual model behavior.

**5. Robustness analysis under varying noise regimes.** Figure 4 shows that CausalNovo maintains higher amino acid precision across the full Noise-Signal Ratio spectrum (+10.2%, +12.2%, +12.0% average improvement over the three baselines). Table 6 demonstrates up to 28.5% relative improvement in peptide precision under the most challenging perturbation conditions.

**6. Cross-species validation.** Table 3 shows leave-one-out cross-species validation where CausalNovo improves CasaNovo's peptide precision across all nine species (average +2.6%), demonstrating that learned causal representations transfer well to unseen biological distributions.

## Weaknesses

### Major

**1. The CEM capacity confound is not fully resolved.** The ablation study (Table 4) compares the baseline (no CEM) against the baseline + CEM + independence objective in a single step. This conflates two effects: (i) adding the CEM's 3-layer Transformer + MLP parameters (~2.5M extra parameters), and (ii) the independence objective itself. The paper does not include a control where the CEM is added to the baseline but trained with only the standard cross-entropy loss (without causal objectives). Such a control would isolate whether improvements come from the causal objectives or simply from increased model capacity.

**Why this matters:** The paper's central claim is that *causal disentanglement* drives the gains, but the 1.2% improvement from baseline (0.741) to baseline+Independence (0.753) could partially reflect the extra parameters. That said, this concern is **partially mitigated** by the stepwise ablation within CausalNovo: adding purification (+0.8%) and symmetric training (+0.4%) on top of the CEM-equipped model shows that the causal-specific objectives themselves drive additional gains beyond any capacity effect. A CEM-only control would strengthen the paper substantially.

### Minor

**2. The purification objective is poorly justified.** The paper states that maximizing I(z_s; Y) "can indirectly lead to the purification of z_c" but provides only a vague, one-sentence explanation. In typical causal disentanglement, one would minimize I(z_s; Y) to prevent non-causal factors from carrying predictive signal. The paper's reasoning — that overlapping information between z_c and z_s makes it harmless — is not standard and is insufficiently explained. While the ablation shows the objective empirically helps, the theoretical grounding needs clarification. This is a secondary concern because the empirical evidence stands on its own.

**3. No variance or confidence intervals reported.** Tables 1, 2, and 3 report single-run results without standard deviations or statistical significance. While single-run evaluation is the norm in the NovoBench benchmark, adding error bars (e.g., across 3 runs with different seeds) for at least the main comparisons would increase confidence in the reported improvements.

**4. Hyperparameter sensitivity unclear.** The tolerance threshold γ for identifying non-causal peaks (Equation 4) is a critical hyperparameter, but its value is not stated in the main text. The paper should report the chosen value and discuss sensitivity.

### Trivial

- The CEM architecture is described as "3 Transformer layers followed by an MLP head" (Section 4.2), but exactly how the per-peak d-dimensional representation is reduced to a scalar importance score is not explicitly stated (presumably the MLP maps d → 1).
- The paper uses only 3 ion types (b, y, a) for the main experiments. The additional analysis with 18 types (Table 6) is reassuring but should be referenced more prominently.

## Nice-to-Haves

- Run the suggested ablation: add a CEM to the baseline but train it with standard cross-entropy loss (no independence, purification, or symmetric objectives), to isolate the effect of extra parameters from the causal objectives.
- Provide a clearer theoretical justification for the purification objective, or replace it with a more standard formulation (e.g., minimizing I(z_s; Y) while maintaining I(z_c; Y)).
- Report means and standard deviations over multiple runs for key results.
- State the tolerance threshold γ used for non-causal peak identification and provide a sensitivity analysis.

## Removed Points

**These points are flagged as removed; treat them with caution.**
- *"CEM architecture under-specified (δ(z) outputs n×1 but how is d-dim reduced to scalar)"* — The paper states "3 Transformer layers followed by an MLP head" in Section 4.2, which is sufficient detail for a paper of this type. The MLP maps d → 1. This is a standard architecture choice.
- *"Unclear whether same hyperparameters used for all models"* — The paper states "retrained with the same configurations" (Section 4.1). While this could be more specific, it is a standard and acceptable reporting practice.
- *"Weakness about missing related works"* — Removed per instructions (no external sources to verify).
- *"Approximation of conditional MI via contrastive learning should be acknowledged"* — The paper already acknowledges this implicitly by describing the implementation as a practical approximation; the link to conditional MI is standard in the literature.

## Novel Insights

The harsh critic's CEM confound point is the most useful observation — it applies the right pressure on a real experimental design gap. However, the critic understates the partial mitigation from the stepwise ablation (which shows that purification and symmetric objectives add value even after the CEM is in place). The strength finder's attention analysis (Table 7) is genuinely valuable and provides a mechanistic link that many similar papers lack. Beyond the paper's own contributions, the main takeaway is that combining causal principles with domain knowledge (theoretical spectrum for intervention) is a promising template for robust biological sequence modeling — but future work should rigorously control for architecture capacity when making causal attribution claims.

## Suggestions

1. **Most impactful single fix:** Add an ablation where the baseline has a CEM of the same architecture but is trained without the causal-specific objectives (i.e., only the standard cross-entropy loss on the full representation, ignoring the mask). If the gain over the bare baseline is substantially smaller than with the causal objectives, the central claim is much stronger.
2. Clarify the purification objective's theoretical basis — either provide a principled derivation or reframe it as an empirically motivated auxiliary loss.
3. Add error bars (standard deviation over multiple seeds) for the main comparisons in Tables 1, 2, and 3.

## Score and Decision

The paper makes a genuine contribution: it identifies a real problem (models relying on noise peaks), proposes a principled framework grounded in causal theory, and validates it thoroughly. The CEM confound is a notable gap but does not undermine the core contribution — the combined evidence (stepwise ablation, attention analysis, robustness analysis) strongly suggests the causal objectives are driving the improvements, not just extra parameters. The purification justification needs work but the ablation shows it empirically helps. Overall, a solid paper with room for strengthening.

**Round-1 bracket:** 5.5–6.5  
**Round-2 anchors:** ReNovo (6.50, accept) — comparable contribution but CausalNovo has more novel methodology; MADGEN (6.00, accept) — similar quality and evaluation depth; Causal Instruction Tuning (5.67, reject) — weaker empirical grounding; PepHAR (6.20, accept) — comparable evaluation quality. **Final score:** 6.0.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>