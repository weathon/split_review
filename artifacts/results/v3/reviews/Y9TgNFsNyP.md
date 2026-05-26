## Summary

This paper introduces FF-Erase, the first machine unlearning method specifically designed for Forward-Forward (FF) models. The key contribution is a goodness-guided unlearning framework that uses a guidance model to stabilize parameter updates, avoiding the model collapse that occurs when applying standard gradient-ascent unlearning to FF models. Additionally, it proposes G-MIA, a membership inference attack that leverages per-layer goodness vectors to verify unlearning effectiveness. Experiments on multiple architectures (TinyCNN, AlexNet, VGG13) and datasets (CIFAR-10/100, MNIST, Fashion-MNIST) show FF-Erase achieves 1.9–3.1× speedup over retraining from scratch with modest accuracy degradation.

## Strengths

1. **First formalization of the FF unlearning problem.** The paper clearly identifies why conventional gradient-ascent unlearning fails on FF models (parameter sensitivity due to layer-wise greedy training, risk of layer divergence) and backs this with a concrete illustration (Figure 1) and discussion. This establishes a genuinely novel problem space.

2. **FF-Erase framework with clear efficiency gains.** The goodness-guided approach (Algorithm 1, Eqs. 5–6) is well-motivated by the identified failure modes of GA. The empirical results show consistent 1.9–3.1× speedup over retraining while maintaining comparable G-MIA scores (Figures 4, 5, Table 1), directly supporting the core efficiency claim.

3. **Thorough ablation on guidance models.** Table 1 systematically varies α₁ (data proportion) and α₂ (epoch proportion) for both mini-retrained and fast-distilled guidance models, demonstrating the efficiency-effectiveness trade-off. The control experiment with a randomly initialized guidance model (R.G.M row) convincingly validates the design choice.

4. **Broad evaluation coverage.** Experiments span 4 datasets and 3 architectures using two different FF algorithms (CwComp, Deeperforward), supporting generalizability beyond a single setting.

## Weaknesses

### Major

1. **No statistical significance or multiple runs reported.** All experimental results (Figure 4, Figure 5, Table 1) appear to come from a single random data split. The paper states "we randomly sample 20% of the training data as forgetting" without any indication of repeated trials or error bars. Given inherent variance in FF training and unlearning, the reported differences (e.g., G-MIA scores of 0.5245 vs 0.5320 for FF-Erase(D) vs RE) cannot be assessed for significance. This weakens all comparative claims about effectiveness, efficiency, and model utility. *Verification: No mention of multiple seeds, standard deviations, or confidence intervals anywhere in Section 6.*

2. **G-MIA's "black-box" framing is misleading relative to its actual access requirements.** The paper repeatedly describes G-MIA as a "black-box" attack (abstract, contributions, Section 5), yet the attacker must obtain "the output of the target model of attack, i.e., the goodness vectors from all layers" (Section 5). Meanwhile, Section 2 defines black-box MIAs as those that "only use the model's final prediction output." The paper's own default setting uses a predictor on top of the goodness vectors for inference (Section 3.1: "We employ this predictor as our default setting"). In a realistic API deployment, only the predictor's output (class logits/probabilities) would be exposed, not the per-layer goodness vectors. The comparison with the final-layer (FL) MIA, which uses strictly less information, is therefore asymmetric. This does not invalidate G-MIA as a method, but the access model needs to be honestly characterized (e.g., as a grey-box or intermediate-output attack) and its practicality justified.

### Minor

3. **Gradient ascent (GA) baseline is underspecified.** The paper claims GA "fails for FF models" but never specifies the exact update rule used: is the gradient computed with respect to the per-layer FF loss (Eq. 2) or some other objective? Is it applied jointly across layers or independently per layer? While the exploration of λ values in Section 6.3 partially addresses the robustness of the failure claim, the missing implementation details hinder reproducibility and make it difficult to assess whether the failure is fundamental or stems from a particular implementation choice. *Verification: Section 6.3 says "using gradient ascent as a representative" applied to "Equation (4)" but Eq. 4 is the general unlearning objective, not an update rule. Algorithm 1 is the FF-Erase algorithm, not the GA baseline.*

4. **Termination thresholds ε₁ and ε₂ are introduced without guidance.** Algorithm 1 uses thresholds ε₁ and ε₂ for early stopping, but no values, sensitivity analysis, or guidance on setting them is provided. This is a practical reproducibility gap.

### Trivial

5. Section 5 mentions synthetic data generation for shadow model training but defers details to the appendix; a one-sentence description in the main text would improve self-containedness.

## Nice-to-Haves

- A "fine-tune on remaining data only" baseline would be a natural lightweight comparison point for the unlearning experiments, directly controlling for the effect of simply re-training on D_remain without a dedicated forgetting mechanism.
- A sensitivity study on the recovery interval K (only a single value is reported) would help practitioners understand the utility-efficiency trade-off.
- Brief discussion of how synthetic data for shadow models is generated would improve completeness of Section 5.

## Removed Points

- **Criticism about fairness of G-MIA vs FL comparison "if the asymmetry favors the baseline":** This criticism was framed as "G-MIA uses all layer goodnesses while FL uses only final logits" — this is a valid concern about asymmetric information, not about favoring the baseline. The asymmetry favors G-MIA (more information), making the comparison unfair to FL. This is a legitimate weakness, kept as Major weakness #2.
- **"Missing related works":** Removed per the hard rule not to mention missing related works.
- **Reproducibility concerns citing undisclosed hyperparameters:** The hyperparameter issue with ε₁, ε₂ is retained (Minor). Other hyperparameter concerns that are standard for the field were removed.
- **Formatting/style nitpicks:** Removed per hard rules.
- **"The paper cites references that may not exist":** Removed per hard rule — all cited references are assumed to exist.

## Novel Insights

None beyond the paper's own contributions. The merger analysis surfaces that the core tension in this paper is between its genuine novelty (first FF unlearning method, well-motivated approach) and its insufficient experimental rigor (single runs, no error bars) — a tension common to many first-of-its-kind papers. The G-MIA access-model issue is a distinct framing concern that, while not fatal, reflects a pattern of slightly over-claiming relative to what is actually demonstrated.

## Suggestions

1. **Add multiple runs (at least 5 seeds) with mean ± std** for all key metrics (G-MIA scores, Acc_f, Acc_t, time) to establish statistical reliability of the comparative claims.
2. **Re-classify G-MIA** as a grey-box or "intermediate-output" attack (or explicitly justify a threat model where goodness vectors are naturally exposed in FF model APIs), and adjust all language accordingly.
3. **Specify the GA baseline implementation clearly** — per-layer vs. joint update, which loss function, learning rate schedule — so that the "GA fails" claim can be independently verified.
4. **Provide recommended values or a sensitivity analysis for ε₁, ε₂, and K** to improve reproducibility.

## Score and Decision

**Round-1 bracket:** [4.0, 5.5]

**Round-2 narrowed anchors:** lgnAEBE1Xq (Contrastive Unlearning, 5.00), drrXhD2r8V (SPE-Unlearn, 5.00), TLBPjECC5D (Unlearning via Sparse Representations, 5.25), pUOesbrlw4 (Deep Unlearning, 5.25)

**Calibration anchors used:**

| Anchor | Score | Source | Comparison |
|--------|-------|--------|------------|
| Xagys9QD3T (Pseudo-Probability Unlearning) | 3.00 | round1-topic-low | Weaker — had fundamentally flawed evaluation objective |
| hwXUmwJAq5 (UGradSL) | 3.00 | round1-topic-low | Weaker — incorrect evaluation metrics for unlearning |
| dYTjB86pcT (System Aware Unlearning) | 5.50 | round1-topic-mid | Stronger theoretical contribution but limited empirical eval |
| pUOesbrlw4 (Deep Unlearning) | 5.25 | round1-topic-mid | Comparable — novel method, similar level of empirical rigor |
| wAemQcyWqq (Oblivious Unlearning) | 5.67 | round1-weakness | Stronger — theoretical guarantees, more thorough evaluation |
| KEeTRb8GLf (Blind Unlearning) | 3.60 | round1-weakness | Weaker — significant theoretical and practical issues |
| LRSspInlN5 (Black-Box MIA Diffusion) | 5.50 | round1-weakness | Comparable on MIA aspect, but different problem domain |
| lgnAEBE1Xq (Contrastive Unlearning) | 5.00 | round2 | Comparable — similar strengths and weakness profile |
| drrXhD2r8V (SPE-Unlearn) | 5.00 | round2 | Comparable — novel approach, similar experimental gaps |
| TLBPjECC5D (Unlearning via Sparse Representations) | 5.25 | round2 | Comparable — good results, similar missing rigor |
| CGfWyU28Pd (Why Fine-Tuning Struggles) | 4.50 | round1-weakness | Comparable — interesting analysis but narrow scope |

**What the low-band anchors failed at:** The 3.0–3.6 anchors (Pseudo-Probability Unlearning, UGradSL, Blind Unlearning) had fundamental methodological flaws — incorrect evaluation objectives (maximizing forget error instead of matching retrained model), wrong metrics (claiming higher MIA = better privacy), or theoretical issues that invalidated core claims. **The paper under review does NOT share these failures.** Its evaluation methodology is sound, metrics are appropriate (G-MIA scores compared against retrained model as gold standard), and the approach is well-motivated. However, the lack of error bars is a gap that comparable 5.0–5.25 papers in the calibration set also exhibit to varying degrees, placing this paper firmly in that middle tier.

**Final score: 5.0 / Decision: Reject**

The paper addresses a genuinely novel problem with a well-motivated method, and the ablation study on guidance models is thorough. However, the absence of statistical rigor (single-run results throughout) undermines confidence in the quantitative claims, and the G-MIA black-box framing needs honest re-characterization. These issues are fixable, but in their current form they prevent the paper from meeting the acceptance bar.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>