Now let me write the final consolidated review.

## Summary

This paper proposes FF-Erase, the first machine unlearning method specifically designed for Forward-Forward (FF) models, along with G-MIA, a goodness-based membership inference attack for verification. The core insight is that standard gradient-ascent unlearning fails on FF models because their layer-wise independent training causes divergence and model collapse. FF-Erase addresses this by using a guidance model (ignorant of forgetting data) to stabilize the goodness distribution shift via KL divergence during forgetting, and periodically running recovery forward passes on remaining data to maintain utility. Experiments across four datasets and three architectures show FF-Erase achieves 1.9–3.1× speedup over retraining with only 1.6–3.3% accuracy degradation.

## Strengths

1. **First systematic treatment of FF unlearning, with compelling problem identification.** Section 1 and Figure 1 clearly demonstrate why gradient-based unlearning (e.g., gradient ascent) causes layer-wise divergence and model collapse in FF models — a problem not recognized in the BP-focused unlearning literature. The paper concretely identifies two causes: sensitivity to parameter tuning due to the absence of backpropagation's global consistency, and difficulty in calibrating per-layer forgetting due to independent layer-wise objectives.

2. **FF-Erase achieves near-retraining effectiveness with substantial speedup.** Figure 4 shows FF-Erase(D) attains a G-MIA score of 0.5245 (versus RE's 0.532) and comparable accuracy on forgetting data (81.31% vs 81.61%) using only 38.52% of retraining time. The efficiency is well-characterized in Equation (9), breaking down the contributions of guidance-model acquisition and goodness-decrease phases.

3. **Guidance model prevents collapse while enabling flexible trade-offs, supported by thorough ablation.** Table 1 shows that random guidance (R.G.M) causes severe utility loss (Accₜ = 55.53%), while even weak guidance preserves utility above 77%. The table systematically documents how varying data fraction (α₁) and epoch fraction (α₂) trade off unlearning time against effectiveness, providing practitioners a clear knob for efficiency-performance tuning. The two guidance strategies (mini-retrained, fast-distilled) are practical and cover realistic deployment scenarios.

4. **G-MIA exploits FF-specific goodness signals effectively as a verification tool.** Figure 3 shows G-MIA consistently outperforms the black-box final-layer MIA (FL) across all architectures. On deeper models (VGG13, CIFAR-100), G-MIA matches or exceeds white-box attacks (GR, GAP, ST), demonstrating that layer-wise goodness vectors carry membership information that standard defenses (dropout, batch norm, weight decay) do not suppress.

5. **The hyperparameter sweep in Section 6.3 robustly validates the failure of gradient ascent on FF models.** Figure 5 shows GA either collapses (λ ≥ 0.1) or fails to unlearn (λ ≤ 0.01) across a wide range of regularization strengths, confirming that the problem is structural rather than tunable — a strong empirical argument for why a new FF-specific method is needed.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **G-MIA overclaims "strict black-box" status.** The paper defines black-box MIAs as using "only the model's final prediction output" (Section 2, Related Work), yet G-MIA requires access to per-layer goodness vectors from all layers. Within the MIA literature, this is closer to a gray-box setting — the attacker obtains intermediate representations rather than just the final prediction. The comparison with FL (final-layer MIA), which genuinely uses only final outputs, is therefore not apples-to-apples: G-MIA's superior performance is partially attributable to its richer access. This does not invalidate G-MIA as a verification tool — particularly since FF models' inference output *is* the per-layer goodness vectors (Section 3.1), which might be plausibly exposed in an FF model API — but the framing needs honest recalibration. The authors should explicitly discuss the threat model, justify why obtaining per-layer goodness vectors is realistic for a black-box deployment, and avoid claiming "strict black-box constraint" without qualification.

2. **Missing statistical significance reporting.** The paper reports all accuracy and G-MIA scores as point estimates without error bars, standard deviations, or confidence intervals. Figures 3–5 and Table 1 would be substantially strengthened by showing variance across multiple runs (e.g., different random splits of forgetting/remaining data). Without this, it is difficult to assess whether the reported differences between methods (e.g., G-MIA ACC of 0.5245 vs RE's 0.532) are meaningful or within the noise.

3. **No limitations or failure case discussion.** The paper lacks a dedicated limitations section. Important caveats to acknowledge include: (a) the guidance model adds overhead and requires access to remaining data; (b) the method's behavior when the forgetting set constitutes a large fraction of training data (e.g., >50%) is unexplored; (c) it is unclear how FF-Erase degrades when the guidance model itself is poorly calibrated. Adding a brief limitations paragraph would improve the paper's completeness.

### Trivial

- In Section 6.4, the text states "FF-Erase using a randomly initialized model as guidance model... leads to unacceptable performance degradation: the Acc_f drops to 55.53%." However, Table 1 shows Acc_f = 51.18% and Acc_t = 55.53% for R.G.M. The text appears to conflate the two accuracy values — it should reference Acc_t = 55.53% (or report Acc_f = 51.18%). This does not affect the qualitative point but should be corrected.

## Nice-to-Haves

- **Validate guidance model ignorance.** The paper claims the fast-distilled guidance model is "ignorant of the forgetting data," but using the original model as teacher could leak information about forgetting data through the distillation loss on remaining data. A simple check: report G-MIA scores on forgetting data for the guidance model itself — if truly ignorant, these should be near 0.5.
- **Pareto-front visualization of the efficiency-effectiveness trade-off.** Table 1 presents the trade-off enumeratively; a 2D plot with time on one axis and G-MIA score on the other would let practitioners intuitively compare settings.
- **Ablation of recovery frequency K and stopping thresholds ε₁, ε₂.** These hyperparameters are mentioned in Algorithm 1 but never ablated; their impact on the utility-efficiency trade-off is unexplored.
- **Add a "fully retrained" oracle baseline to Table 1** (guidance model trained on 100% of D_remain for full epochs) to show the upper bound and isolate the impact of the mini-retrained/distilled approximations.

## Removed Points

- **Circularity concern (G-MIA used to evaluate its own method).** The Harsh Critic raised that G-MIA is used as both a proposed method and an evaluation metric for FF-Erase. REMOVED because the paper uses multiple independent metrics (Acc_f, G-MIA score, comparison to RE), and the G-MIA score on forgetting data is a standard MIA-based verification practice. The concern does not hold given the complementary evidence.
- **Generic "need for additional MIAs as independent verification."** REMOVED because the paper already provides multiple metrics and the existing evidence is sufficient — requesting additional attacks is scope creep.
- **"The paper could add more experiments" type criticisms.** REMOVED per instructions: these are generic and do not undermine the core claims.
- **Missing related work.** REMOVED per hard rule — I cannot verify whether works are missing.
- **Reproducibility nitpicks (hyperparameters, implementation details).** REMOVED per hard rule.

## Novel Insights

The reviewers' main contributions beyond the paper itself are: (1) The observation that FF models' inference API naturally exposes per-layer goodness vectors, which makes G-MIA's access assumption less stringent than it might first appear — the paper should explicitly frame this to preempt the gray-box concern. (2) The observation that the fast-distilled guidance model could leak forgetting-data information through the teacher model, which the authors could empirically verify with a simple G-MIA check on the guidance model itself. Neither insight is a fatal flaw, but both point to concrete improvements.

## Suggestions

1. Recalibrate the G-MIA framing: explicitly state that the attacker obtains per-layer goodness vectors (which are part of standard FF model inference output), contrast this with traditional black-box (final output only), and discuss deployment scenarios where this access is realistic. Drop the "strict black-box" phrasing.
2. Add error bars (or report standard deviations over multiple train/forget splits) to all experimental figures and tables.
3. Add a brief limitations paragraph covering the guidance model overhead, scalability to large forgetting sets, and potential failure modes.
4. Correct the minor R.G.M accuracy text error in Section 6.4.

## Calibration Report

I performed three rounds of calibration retrieval. All anchors used for comparison:

**Round 1 (Bracketing):**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| Xagys9QD3T (Pseudo-Probability Unlearning) | 3.00 | R1 | Weaker — less clear motivation, no specific architecture challenge addressed |
| ZyMXxpBfct (Forward Explanation) | 1.50 | R1 | Much weaker — not a unlearning method paper |
| BJfIDS5LsS (MASIMU) | 2.50 | R1 | Much weaker — unclear contribution |
| hwXUmwJAq5 (UGradSL) | 3.00 | R1 | Weaker — incremental, less thorough evaluation |
| OHOmpkGiYK (Decoupling Class Label) | 5.75 | R1 | Comparable in structure but weaker motivation; more significant weaknesses |
| KvFk356RpR (Unlearning Mapping Attack) | 4.80 | R1 | Weaker — threat model issues, unclear practical relevance |
| TLBPjECC5D (Unlearning via Sparse Representations) | 5.25 | R1 | Comparable but criticized as incremental, model-specific |
| E6rpTruK4v (CodeUnlearn) | 3.80 | R1 | Weaker — limited evaluation |
| EUSkm2sVJ6 (DUCI) | 7.60 | R1 | Stronger — broader impact, near-definitive evaluation |
| IGzaH538fz (GNNCert) | 8.00 | R1 | Stronger — theoretical guarantees, broader scope |

**Round 2 (Narrowing):**
| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| pUOesbrlw4 (Deep Unlearning: Fast/Efficient) | 5.25 | R2 | Weaker — training-free but limited scope |
| drrXhD2r8V (SPE-Unlearn) | 5.00 | R2 | Weaker — incremental contribution |
| xmQuUqSynb (Rethinking Adversarial Robustness) | 5.75 | R2 | Weaker — missing key metrics (benign accuracy), incomplete evaluation |
| Jq8NPYVxLW (Less is More MIA) | 5.50 | R2 | Weaker — unclear intuition, incomplete experiments |
| dRel8fuUK4 (Low-Cost High-Power MIA) | 6.00 | R2 | Comparable — well-executed MIA with similar rigor |
| NvRVYVN106 (Privacy Breach Detection) | 5.25 | R2 | Weaker — narrower contribution |
| gNxvs5pUdu (DocMIA) | 6.00 | R2 | Comparable — solid execution on a specific domain |
| kOYnXVQCtA (DeeperForward) | 6.25 | R2 | Comparable — FF algorithm paper, similar execution quality, accepted |
| Abr7dU98ME (ForwardGNN) | 6.50 | R2 | Slightly stronger — broader FF application domain, accepted |
| J9Ofr1PmvX (UnSTAR) | 5.50 | R2 | Weaker — less rigorous evaluation |

**Round 1 bracket:** [5.0, 6.5].
**Round 2 narrowing:** The paper is stronger than the 4.8–5.75 unlearning papers (which had more significant methodological issues) and comparable to the 6.0–6.25 FF algorithm papers (DeeperForward at 6.25, accepted). The primary weakness (G-MIA framing) is a real but manageable overclaim that does not threaten the core unlearning contribution. The final score of 6.0 reflects a well-executed paper in a niche domain with a clear contribution, solid experiments, and one non-trivial framing issue that a rebuttal can address.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>