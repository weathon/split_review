## Summary

This paper introduces FF-Erase, the first machine unlearning framework designed specifically for Forward-Forward (FF) models — a biologically plausible alternative to backpropagation. The method uses a "guidance model" to provide target goodness distributions, shifting the original model's per-layer goodness scores via KL-divergence to forget target data, with periodic recovery steps to maintain utility. Two guidance model strategies (mini-retrained and fast-distilled) are proposed. The paper also introduces G-MIA, a goodness-based membership inference attack leveraging per-layer goodness vectors for black-box verification of unlearning. Experiments on CIFAR-10/100, MNIST, and Fashion-MNIST with TinyCNN, AlexNet, and VGG13 show that FF-Erase can unlearn 20% of training data 1.9–3.1× faster than retraining.

## Strengths

- **First unlearning method for Forward-Forward models.** The paper correctly identifies that existing unlearning methods designed for BP-based models cause collapse in FF models due to their sensitivity to parameter tuning and layer-wise independent training. FF-Erase demonstrably avoids this collapse, while gradient ascent (GA) fails across a wide range of hyperparameters (Figure 5: all λ values either collapse or fail to unlearn). This fills a genuine gap.

- **Goodness-guided unlearning via guidance model is well-motivated and empirically validated.** The use of KL-divergence toward a guidance model's goodness distribution (Equation 5) is a principled way to achieve stable parameter updates in the absence of a joint loss signal. The ablation (Table 1) convincingly shows that the guidance model is critical: a randomly initialized guidance model (R.G.M) causes utility to collapse (Acc_t = 55.53%), while properly trained guidance models (e.g., D-(0.5,0.5)) maintain both utility and effectiveness.

- **G-MIA is a practical black-box verification tool that outperforms existing black-box MIAs on FF models.** Figure 3 shows G-MIA consistently outperforms the standard black-box final-layer MIA (FL) across all datasets and architectures, and matches or exceeds some white-box MIAs on deeper models (VGG13, CIFAR-100). This is a useful contribution for the FF ecosystem where standard black-box MIAs are insufficient.

- **Efficiency analysis is concrete.** Table 1 provides a clear breakdown of unlearning time (guidance model acquisition + goodness decrease) and shows speedups of 1.9–3.1× over retraining with specific, reproducible configurations. The analysis of how α₁ and α₂ affect the efficiency-effectiveness trade-off (Section 6.4) is informative.

- **Evaluation spans multiple architectures and datasets.** Experiments use 4 benchmarks and 3 architectures with 2 FF training algorithms (CwComp, Deeperforward), demonstrating generality beyond a single setting.

## Weaknesses

### Major

- **G-MIA's reliability as a verification metric is undermined by the R.G.M result — a collapsed model achieves nearly identical G-MIA scores to the properly retrained gold standard.** In Table 1, the randomly initialized guidance model (R.G.M) yields a collapsed model (Acc_t = 55.53%, Acc_f = 51.18%) yet its G-MIA ACC (0.553) is essentially identical to the retrained model RE (0.551). If G-MIA cannot distinguish catastrophic model degradation from proper unlearning, its effectiveness as a standalone verification metric is in question. While the paper uses multiple metrics in combination (Acc_f, Acc_t), the claim that G-MIA is a "reliable tool for unlearning verification" (Section 1) is weakened by this result. The paper does not discuss this limitation.

### Minor

- **Numerical inconsistency between Figure 4c and Table 1 for the RE baseline.** The retrained model's G-MIA ACC is reported as 0.532 in Figure 4c but 0.551 in Table 1 — a difference of ~0.02. Since all results are reported without error bars or multiple seeds, it is impossible to determine whether this reflects natural variance or an uncontrolled experimental discrepancy. This reduces confidence in the precision of all reported metrics.

- **No error bars, confidence intervals, or multi-seed results.** Every number in the paper is a single point estimate. For a comparison where the key effects (G-MIA differences between methods) are as small as 0.005–0.02, the absence of any variance estimate makes it impossible to assess statistical reliability. This is a significant omission for a paper whose core claims depend on fine-grained metric comparisons.

- **The speedup claim in the abstract (1.9–3.1×) does not account for the effectiveness trade-off.** The 3.1× figure corresponds to D-(0.5,0.1), which has G-MIA ACC of 0.587 — substantially worse than RE (0.551). Configurations that achieve effectiveness close to RE (e.g., D-(0.5,0.5), R-(0.5,0.5)) have speedups of only 1.9–2.1×. The abstract should transparently reflect this trade-off rather than presenting the range as uniformly achievable with acceptable effectiveness.

- **Only one approximate unlearning baseline (GA) is compared, and its adaptation to FF models is underspecified.** The paper demonstrates that GA fails (either collapsing or failing to unlearn), which is sufficient to motivate a new method. However, the description of how GA is applied to FF models — per-layer or via a global objective — is not provided. Since FF models update per-layer without backprop, the exact mechanics of "gradient ascent" matter for reproducibility. Additional baselines (e.g., fine-tuning on remaining data, bad-teacher-style unlearning adapted to goodness scores) would strengthen the evaluation, though their absence is not fatal for a first paper on the topic.

- **Hyperparameters ε₁, ε₂ (termination thresholds in Algorithm 1) are never specified for the experiments.** These thresholds control early stopping and directly affect the effectiveness-utility trade-off, but no values or selection procedure are reported.

- **Synthetic data generation for G-MIA is not described.** Section 5 states the attacker "can synthesize data that has a similar distribution to the training data" and refers to model inversion techniques, but the experimental setup does not specify how synthetic data was actually generated for each dataset. This affects reproducibility of the attack.

### Trivial

- The paper sometimes uses "goodness" as both the vector of class scores and the scalar score, causing minor clarity issues (e.g., Equation 1 defines g^l as a vector but the text refers to "goodness score" in the singular).

## Nice-to-Haves

- Class-level forgetting and sequential unlearning scenarios would broaden the evaluation, but the random 20% removal setting is a reasonable starting point for the first FF unlearning paper.
- Sensitivity analysis for K (recovery step frequency), which is described as a dataset-dependent hyperparameter, would help practitioners choose values.
- A discussion of how G-MIA transfers to settings where per-layer goodness vectors are not exposed by the model API would clarify its practical applicability.

## Removed Points

These points were flagged by reviewers but are removed from the main review with justification:

- *"G-MIA scores for FF-Erase and retraining (RE) differ by only 0.02–0.03"* — This is factually inaccurate. In Figure 4c, FF-Erase(D) G-MIA (0.5245) is *better* than RE (0.532), a difference of ~0.007. In Table 1, the best configurations differ from RE by 0.005–0.011. The critic's 0.02–0.03 figure does not match the reported data. The underlying concern about G-MIA reliability (via the R.G.M result) is retained as a Major weakness.

- *"The GA baseline adaptation is not described / not reproducible"* — This is weakened to Minor. The paper describes GA with Equation (4) and a sweep over λ ∈ {10¹, 10⁰, 10⁻¹, 10⁻², 10⁻³, 0}. The core experimental finding (GA fails) does not depend on the exact per-layer implementation detail. The concern about underspecification is valid but not a fatal flaw.

- *"Narrow evaluation scope (only image classification, only 20% random forgetting)"* — Weakened to Nice-to-Have. This is the first paper on FF unlearning; establishing the method on standard benchmarks is appropriate. Demanding graphs, text, or other domains is scope creep.

- *"Questioning whether the guidance model generated via fast-distillation leaks information about the forget set"* — This concern is reasonable but the paper's ablation (R.G.M vs. properly trained guidance models) already shows that the guidance model quality matters and the method works with both retrain-based and distillation-based guidance. The paper would benefit from discussing this, but it is not a demonstrated flaw.

- *"Demanding that the paper address applicability of G-MIA when per-layer goodness vectors are not exposed"* — This is speculative and assumes an API constraint that is not part of the paper's threat model. The paper explicitly assumes the attacker can obtain goodness vectors (Section 5), which is a standard assumption in the FF literature.

## Novel Insights

The most valuable insight from the reviews is that **G-MIA's inability to distinguish between a collapsed model (R.G.M) and the gold-standard retrained model (RE) is a previously overlooked limitation that the paper should directly address**. This was raised by the harsh critic and, upon verification against Table 1, is a real issue: R.G.M achieves G-MIA ACC of 0.553 vs. RE's 0.551, while its utility has completely collapsed. This suggests G-MIA should not be used as the sole verification metric — a point the paper does not discuss. However, the paper's broader claim about FF-Erase's effectiveness is still supported by the combination of Acc_f, Acc_t, and G-MIA metrics, which jointly differentiate R.G.M (collapsed) from FF-Erase (well-behaved). The insight raises a useful caution for future work using MIA-based verification for unlearning.

## Suggestions

1. Report all main results over at least 3–5 random seeds with standard deviations or confidence intervals, especially for G-MIA scores where the effect sizes are small.
2. Explain the numerical discrepancy between Figure 4c (RE G-MIA = 0.532) and Table 1 (RE G-MIA = 0.551). If these come from different experimental conditions, state this explicitly.
3. Discuss the R.G.M finding explicitly: why does a collapsed model achieve the same G-MIA score as a properly retrained model, and what does this imply about the limitations of MIA-based verification?
4. Specify the values or selection procedure for ε₁ and ε₂, and describe how synthetic data was generated for the G-MIA shadow model training.
5. Rephrase the abstract's speedup claim to acknowledge the effectiveness trade-off (e.g., "achieving 1.9× speedup with effectiveness comparable to retraining, and up to 3.1× with a modest effectiveness trade-off").

## Score and Decision

### Calibration Summary

**Round 1 (Bracketing):**
- Weak band (<3.5): Pseudo-Probability Unlearning (3.00), MASIMU (2.50) — these papers have fundamental flaws or very limited contributions. The FF-Erase paper is clearly above this band due to its genuine novelty.
- Middle band (3.5–7.5): Unlearning Mapping Attack (4.80), Auditing Privacy Protection (4.20), Rethinking Adversarial Robustness (5.75), Adversarial Machine Unlearning (5.33), Forget Vectors at Play (4.80) — these papers have real contributions but evaluation gaps. FF-Erase is in this range.
- Strong band (>7.5): Probabilistic Perspective on Unlearning (8.00), Unlearning-based Neural Interpretations (8.00), Unlocking Function Vectors (9.00) — these are fully rigorous works with comprehensive evaluations. FF-Erase is well below this band.

**Initial bracket:** 4.5–6.5

**Round 2 (Narrowing):**
- Do Unlearning Methods Remove Information from LM Weights? (5.50) — novel evaluation methodology but narrow scope. Comparable to FF-Erase in having a clear contribution but evaluation limitations.
- Evaluating Deep Unlearning in LLMs (5.33) — interesting problem formulation but synthetic-only evaluation. Slightly weaker in experimental breadth than FF-Erase.
- Unlearning via Sparse Representations (5.25) — clever application but limited baselines and model-specific. Comparable evaluation rigor to FF-Erase.
- Towards Effective Evaluations for LLM Unlearning (5.50) — evaluation-focused paper, different type of contribution.

Compared to these anchors, FF-Erase has a stronger novelty claim (first in its domain) but similar evaluation limitations (no error bars, limited baselines, single-scenario experiments). The paper is most comparable to the 5.5-level anchors.

**Final score:** 5.5

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>