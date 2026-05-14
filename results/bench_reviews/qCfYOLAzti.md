Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper identifies a failure mode in LLM unlearning called *spurious unlearning*, where gradient-ascent-based methods (GA, NPO) suppress target responses but redistribute probability mass into semantically similar paraphrases — the "squeezing effect." To counter this, the authors propose a bootstrapping framework (BS-T at the token level, BS-S at the sequence level) that suppresses not just target responses but also the model's own high-confidence generations ("model beliefs"). Experiments on TOFU, WMDP, and MUSE show consistent improvements over baselines, and the paper provides theoretical analysis via the AKG learning dynamics framework.

## Strengths

- **Identification and empirical characterization of the squeezing effect**: The paper convincingly demonstrates (§3.2, Fig. 2) that NPO-based unlearning persistently retains probability mass in high-likelihood neighborhoods that are semantically similar to target responses (LaaJ similarity ≈1.0 for high-likelihood vs. 4.2 for low-likelihood regions). The tracking of log-probability dynamics (Fig. 2b-c) directly shows probability mass being squeezed into these regions under NPO, providing a mechanistic explanation for spurious unlearning.

- **Bootstrapping framework that directly targets the identified failure**: BS-T and BS-S explicitly suppress both target responses and model beliefs. Fig. 4a-b demonstrates that under BS methods, log-probabilities of both targets AND high-likelihood neighbors decrease monotonically — in stark contrast to the squeezing pattern of GA/NPO. This translates to practical gains across TOFU Table 1, where BS-S achieves best aggregate scores across all model scales and forget ratios, and WMDP Table 2, where BS methods achieve near-random forgetting accuracy with competitive MMLU retention.

- **Flexible, compatible design**: The bootstrapping objectives are formulated as plug-in components that work with any base unlearning loss (GA, NPO, WGA) and with retain regularization (GradDiff). This compatibility is empirically verified and enables broad applicability.

- **LaaJ evaluation provides independent validation beyond surface metrics**: The LLM-as-judge evaluation (§3.1, Fig. 4c) reveals cases where classical metrics report success but the model still leaks knowledge, and shows BS methods achieve meaningfully higher similarity discrimination (BS-S: 4.3 vs. NPO: 2.8) while maintaining fluency.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Tension between metric critique and primary evaluation**: Section 3.1 argues that TOFU metrics (Probability, ROUGE, Truth Ratio) can be misleading when used in isolation — for example, Truth Ratio can be 0.34 while the model still leaks knowledge. Yet Table 1's Memorization metric is a harmonic mean that includes Truth Ratio as one of four components. While a composite is not equivalent to the individual metrics criticized, and the paper provides complementary LaaJ results (Fig. 4c) and WMDP results (QA accuracy), the reliance on Truth Ratio within the primary evaluation metric creates an unresolved tension that weakens confidence in the headline Table 1 results.

- **Single-setting LaaJ evaluation**: The LLM-based evaluation in Fig. 4c covers only one setting (TOFU 10%, Llama 3.1 8B, Gemini 2.5 Flash). Given that the paper's core claim is about mitigating spurious unlearning — a phenomenon the paper itself argues table metrics miss — a more systematic LaaJ evaluation across settings would substantially strengthen the case.

- **Marginal improvements in some settings**: Several Table 1 comparisons show small gaps (e.g., BS-S 0.61 vs. NPO 0.58 for 10%-1B, BS-S 0.63 vs. NPO 0.62 for 10%-3B). No standard deviations or confidence intervals are reported. While larger-scale LLM benchmarks rarely provide multi-seed statistics due to computational cost, the consistency of BS-S ranking first across 9/9 settings in Table 1 and the complementary evidence from probability dynamics (Fig. 4a-b) partially mitigate this concern.

- **Theory is descriptive rather than prescriptive**: Theorem 5.2 shows that the BS-T residual augments the GA residual with an extra term from the belief distribution, and Theorem 5.3 extends this to off-policy BS-S. These are direct algebraic consequences of the loss construction and provide interpretable insight into why BS reshapes gradient dynamics, but they do not provide convergence guarantees, bounds, or quantitative predictions. The theory serves an explanatory role — it clarifies the mechanism — which is valuable but limited.

### Trivial

- The on-policy BS-S variant used in practice is explicitly excluded from the theoretical analysis (which requires teacher-forcing); the paper acknowledges this and defers discussion to the appendix, but a sentence in the main text summarizing the practical implications would improve clarity.

## Nice-to-Haves

- Ablation against a simple data-augmentation baseline (e.g., paraphrasing forget-set responses with an external LLM and adding them to the forget set) would help isolate whether the bootstrapping mechanism specifically is necessary or whether any semantically-similar augmentation yields similar benefits.

- Side-by-side qualitative examples of generations from BS-S, NPO, and retrain for the same prompt would make the reduction in semantic leakage more tangible.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"RMU is mischaracterized as a GA-based approach"* — The paper does not claim RMU is GA-based. It lists RMU among baselines (alongside GradDiff, NPO, SimNPO, WGA) and the squeezing effect analysis in §3.2 focuses specifically on GA and NPO. Including RMU as a comparison point is standard practice and not a mischaracterization.

- *"The theoretical gap for on-policy BS-S is not addressed"* — The paper explicitly states in §5.2: "Note that in on-policy BS-S, the auxiliary sequences are resampled from the model during finetuning and therefore depend on the evolving parameters θ, which violates the teacher-forcing assumption required by the AKG framework. We discuss the implications of this limitation in Appx. D.4." This is directly addressed.

- *"The paper should replace all metric-based evaluation with systematic LLM-based evaluation"* — This demand is unreasonable. The paper uses standard benchmark metrics (which it critiques but does not entirely reject), complements them with LaaJ evaluation, and the WMDP benchmark uses QA accuracy which is not subject to the same criticism. Full replacement with LLM-based evaluation across 27 cells is a scope-creep demand.

- *"Report variance over at least 3 seeds for all main results"* — While ideal, large-scale LLM unlearning benchmarks (TOFU across 3 model scales × 3 forget ratios) are computationally intensive, and single-run evaluation with greedy decoding is the norm in this literature. This is a nice-to-have, not a requirement.

- *Strength Finder claim: "Theoretical grounding via AKG decomposition" as a core strength* — Downgraded. The theory is descriptive rather than providing novel guarantees, though it does offer interpretable insight into the mechanism.

## Novel Insights

Beyond the paper's own contributions, the consolidated reviews highlight an important meta-point: the unlearning field faces a persistent evaluation gap where the metrics best suited to detecting spurious unlearning (LLM-based semantic judgments) are not yet standardized or scalable enough to replace table metrics in large-scale comparisons. The paper navigates this by using both, but the tension remains unresolved — and this tension is emblematic of a broader challenge facing the community.

## Suggestions

- Consider presenting the LaaJ evaluation more prominently, perhaps as a separate table alongside Table 1 for at least the key settings, rather than relegating it to a single bar chart.
- Add a brief discussion of when each metric component in the Memorization composite might fail, to directly address the tension between §3.1's critique and §6.1's metric choice.
- If computationally feasible, report LaaJ results for at least one additional setting (e.g., TOFU 5% or 1%) to strengthen the cross-validation.

## Score and Decision

**Anchor comparison:**

| Path | Paper | Avg Score | Comparison |
|------|-------|-----------|------------|
| BcjZCertEk | Learning-Time Encoding Shapes Unlearning in LLMs | 4.67 (Accept Poster) | Empirical study of data factors; narrower scope, no method proposed. Current paper has broader contribution: phenomenon identification + method + theory + 3 benchmarks. |
| qd9fA4LzVN | Label Smoothing Improves Gradient Ascent in LLM Unlearning | 4.50 (Reject) | Simple smoothing method; limited novelty, weaker results. Current paper identifies a deeper failure mode and proposes a more principled solution. |
| r6Z3BXDrzO | On the Impossibility of Retrain Equivalence | 4.50 (Reject) | Strong theory but claims undermined by prior work. Current paper's empirical foundation is more solid. |
| rzi77zNngG | Leak@$k$: Unlearning Does Not Make LLMs Forget | 4.00 (Reject) | Metric proposal only, no method. Current paper offers both diagnosis and solution. |
| 7cEMkTu7Lf | Unlearning Isn't Deletion | 4.00 (Reject) | Analysis-only, known problems. Current paper goes further with a concrete fix. |
| K6OFqKEidO | Towards Evaluation for Real-World LLM Unlearning | 3.00 (Withdrawn) | Narrow metric contribution. Current paper is substantially broader. |

The current paper makes a genuine contribution: it identifies and mechanistically characterizes the squeezing effect, proposes a well-motivated bootstrapping solution, validates it across three benchmarks and multiple model scales, and provides complementary LaaJ evidence. The metric tension is a real but addressable concern that does not invalidate the core contribution. The paper is stronger than the 4.0–4.5 range papers and comparable to or slightly above the 4.67 anchor.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>