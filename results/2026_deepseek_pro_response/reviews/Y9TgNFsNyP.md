Now I have sufficient anchors across the full range. Let me finalize the review.

**Bracketing summary:**
- Round 1 bracket: 4.5–6.0
- Round 2 narrowing: The paper sits between Adversarial ML Unlearning (5.33) and Oblivious Unlearning (5.67) / Decoupling Class Label (5.75). FF-Erase has a more compelling ablation than the 5.33 anchor, but the missing baseline and single-setting main-text results prevent it from reaching the 5.67–5.75 tier.

**Final assessment:** FF-Erase is a solid paper with a genuine contribution (first FF unlearning method + G-MIA verification), a well-motivated problem, and a strong ablation study. The two major weaknesses — missing fine-tuning-on-remaining-data baseline and unlearning results restricted to a single setting in the main text — are real but addressable. The paper earns a score of **5.5**.

---

## Summary
This paper introduces FF-Erase, the first machine unlearning framework designed for Forward-Forward (FF) models, along with G-MIA, a goodness-based membership inference attack for verifying unlearning on FF architectures. FF-Erase uses a guidance model (obtained via mini-retraining or fast-distillation) to provide target goodness distributions, steering the original model's layer-wise goodness scores via KL-divergence minimization during unlearning. Experiments on CIFAR-10 with VGG13 show FF-Erase achieves 1.9–3.1× speedup over retraining with modest accuracy degradation, and the G-MIA verification tool consistently outperforms standard black-box MIA baselines.

## Strengths
- **Genuine gap identification with empirical validation**: The paper is the first to address machine unlearning for FF models. §6.3 (Figure 5) systematically tests gradient ascent across a wide λ range and demonstrates it either causes model collapse or fails to unlearn, providing convincing empirical motivation for why a specialized approach is needed.
- **Guidance-model mechanism validated by decisive ablation**: Table 1's R.G.M. row (randomly initialized guidance model) causes test accuracy to collapse to 55.53% (vs. 80.85% for retraining), demonstrating that a properly trained guidance model — not just KL-based regularization — is essential to prevent collapse during unlearning.
- **G-MIA is a practical verification tool for FF models**: Figure 3 shows G-MIA consistently outperforms the final-layer black-box MIA (FL) across all tested architectures and datasets. On deeper models (VGG13, CIFAR-100), G-MIA even matches or exceeds white-box attacks. For FF models, accessing layer-wise goodness vectors is equivalent to accessing model outputs, making the black-box framing defensible within the FF paradigm.
- **Comprehensive efficiency-performance trade-off (Table 1)**: The grid of (α₁, α₂) configurations across both distillation and retraining strategies provides a clear Pareto surface, allowing practitioners to choose operating points. The time decomposition in Eq. 9 gives a predictive cost model grounded in hyperparameters.

## Weaknesses

### Fatal
None.

### Major
- **Missing baseline: continued FF training on D_remain without the forgetting forward step.** FF-Erase's "recovering forward" (Eq. 6, Algorithm 1) is standard FF training on remaining data, interleaved every K epochs with the forgetting forward step. The paper never isolates whether the forgetting forward step (KL-minimization against a guidance model) adds value beyond what recovering forward alone would achieve. Simply continuing FF training on D_remain for a modest number of epochs is the most natural approximate unlearning baseline — it shifts parameters away from the forgetting data's influence without any auxiliary model or KL-based regularization. Without this comparison, the claimed necessity of the guidance-model mechanism is unsubstantiated.
- **Unlearning results in the main text are restricted to a single model–dataset pair.** All unlearning results in the main text (Figures 4 and 5, Table 1) are exclusively for VGG13 trained on CIFAR-10. The paper states other results are in Appendix §C (line 242), but a new-method paper should demonstrate generality through at least some evidence in the body. The G-MIA evaluation (Figure 3) does span multiple architectures and datasets, partially mitigating this for the MIA contribution, but the core unlearning contribution remains undemonstrated beyond one setting in the portion readers can evaluate.

### Minor
- **Guidance model "ignorance" not analyzed.** The paper claims the guidance model is "ignorant of the forgetting data" (lines 121, 176), but since D_forget and D_remain are drawn from the same distribution (a random 20% split), the guidance model trained on D_remain will generalize to D_forget to some degree. The paper never reports the guidance model's accuracy on D_forget or analyzes how this affects the KL-steering unlearning mechanism.
- **Possible numerical discrepancy in §6.3.** The text (line 262) reports G-MIA scores of 0.6, 0.61, and 0.6 for GA at λ=10⁻², 10⁻³, 0 respectively, but the Figure 5 caption lists 0.552, 0.541, and 0.605 for these same λ values. The text values appear to correspond to different λ values in the figure. This needs clarification.
- **Fast-distillation teacher trained on full data.** The fast-distillation strategy (Eq. 8) uses the original model θ_o as teacher, which was trained on D_forget ∪ D_remain. The distilled student may inherit some influence of the forgetting data through the teacher. This potential leakage path is not discussed.

### Trivial
- No error bars or multiple random seeds reported; results could vary across different 20% forget splits.
- The forgetting ratio β is fixed at 0.2; behavior with smaller or larger forget sets is unexplored.
- The abstract and contribution list present speedup (1.9–3.1×) and accuracy degradation (1.6–3.3%) as independent ranges; these endpoints come from different operating points in Table 1 and are not simultaneously achievable.

## Nice-to-Haves
- Reporting the guidance model's accuracy on D_forget and analyzing how this relates to unlearning outcomes would strengthen the paper's conceptual claims.
- Showing unlearning results for at least one additional dataset–architecture pair in the main text would improve confidence in generality.
- Varying the forgetting ratio β beyond 0.2 would demonstrate how the method scales to different unlearning scenarios.

## Removed Points
These points were flagged by reviewers but are removed from the final review:

- **"The appendix was stripped and is unavailable for review"** — REMOVED. Per review guidelines, the appendix exists in the original submission; parser stripping is not an author error. The concern about main-text evidence is retained as a Major weakness on its own terms.
- **"G-MIA is labeled black-box but requires per-layer goodness vectors — a grey-box assumption"** — REMOVED as a standalone weakness. The paper explicitly states FF models output goodness vectors from all layers for inference (line 88). In the FF paradigm, accessing layer-wise goodness vectors is equivalent to accessing model outputs, which is standard black-box access. The paper distinguishes G-MIA from final-layer-only attacks (FL) in Figure 3, making the access-level distinction transparent.
- **"The abstract bundles best-case speedup and best-case accuracy degradation"** — DEMOTED to Trivial. The paper presents these as independent ranges (1.9–3.1×, 1.6–3.3%), not as a single claim of simultaneous achievement.
- **"Figure 4 reports GA at λ=10, which is the collapsed regime — reporting at best λ would be fairer"** — REMOVED. Figure 5 separately explores GA across all λ values, so the paper provides the full picture.
- **"No discussion of why SISA-style sharding cannot be applied to FF models"** — REMOVED. The paper already states exact unlearning methods "are incompatible with general FF models" (line 60). Deeper discussion is unnecessary.
- **"GA at low λ can increase model confidence on forgetting data — this interesting failure mode should be discussed further"** — REMOVED. The paper already notes this (line 262). Requesting more discussion is scope creep.

## Novel Insights
The paper's key insight — that FF models' layer-wise independent training creates a unique unlearning challenge where gradient ascent causes divergent layer-wise behavior (some layers over-forget while others retain influence), and that a guidance model providing target goodness distributions can stabilize this process — is genuinely novel and well-motivated. The observation that deeper FF models amplify the informativeness of per-layer goodness vectors for membership inference (making G-MIA more competitive with white-box attacks on larger architectures) is also interesting and not obvious a priori.

## Suggestions
- The single most impactful experiment would be adding a baseline that runs only the recovering forward (RFwd) on D_remain without the forgetting forward step. If this baseline achieves comparable G-MIA scores, the guidance model mechanism would be unnecessary; if it fails, the paper's motivation is substantially strengthened.
- Clarify the numerical discrepancy between the §6.3 text and Figure 5 regarding G-MIA scores for GA at different λ values.
- Add error bars over multiple random forget splits to the main results in Table 1.
- Discuss whether the fast-distillation strategy's use of θ_o as teacher creates a leakage path for forgetting data influence, and if so, how severe it is.

## Score and Decision

**Anchor comparisons from calibration:**

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| PPU (Xagys9QD3T) | 3.00 | R1 | FF-Erase is clearly stronger — better methodology, stronger ablation, more coherent contribution |
| Blind Unlearning (KEeTRb8GLf) | 3.60 | R1 | FF-Erase has more comprehensive evaluation and stronger ablation |
| Unlearning Mapping Attack (KvFk356RpR) | 4.80 | R2 | FF-Erase has broader scope (unlearning + verification vs. attack only) |
| Deep Unlearning (pUOesbrlw4) | 5.25 | R2 | FF-Erase has stronger ablation (R.G.M.) and addresses a more foundational gap |
| Sparse Representations (TLBPjECC5D) | 5.25 | R2 | FF-Erase is not model-specific and has a more comprehensive evaluation |
| Adversarial Unlearning (iQIQT88prm) | 5.33 | R1/R2 | Comparable novelty; FF-Erase has better ablation, Adversarial has game-theoretic framing |
| Oblivious Unlearning (wAemQcyWqq) | 5.67 | R1/R2 | OUbL has more extensive experiments; FF-Erase has two contributions (unlearning + MIA) |
| Decoupling Class Label (OHOmpkGiYK) | 5.75 | R2 | Comparable quality; Decoupling has more experiments, FF-Erase addresses a more foundational gap |
| Dataset Usage Cardinality (EUSkm2sVJ6) | 7.60 | R1 | DUCI is clearly stronger — more rigorous with confidence intervals and thorough evaluation |

**Round 1 bracket:** 4.5–6.0  
**Round 2 narrowing:** FF-Erase sits between Adversarial Unlearning (5.33) and Oblivious Unlearning (5.67). The missing baseline and single-setting main-text results are meaningful gaps, but the strong ablation (R.G.M.) and dual contribution (unlearning + G-MIA verification) keep it competitive in the middle tier.

**Final score: 5.5**

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>