Now I have a thorough understanding of the paper and can verify all the claims against the text. Let me compose the final review.

## Summary

MeanSparse proposes a post-training robustness method: compute per-channel activation statistics (μ, σ) from the training set, then hard-threshold activations within μ ± ασ by replacing them with μ. Applied to top RobustBench models, it reports new SOTA AutoAttack accuracy on CIFAR-10 (ℓ∞: 73.71%→75.28%; ℓ2: 84.97%→87.28%), CIFAR-100 (42.67%→44.78%), and ImageNet (59.56%→62.12%), with ≤0.05% clean accuracy loss and minimal computational overhead.

## Strengths

- **Concrete SOTA improvements across four benchmarks.** The gains (1.5–2.3 percentage points AutoAttack accuracy) are clearly reported on specific RobustBench models with specific numbers (Section 4.2, Figure 3). These are not generic claims.

- **Near-perfect clean accuracy preservation while gaining robustness.** Across all settings, clean accuracy drops by ≤0.05% (e.g., CIFAR-10 WideResNet-94-16: 93.68%→93.63%). This property is non-trivial for a post-hoc modification and is well-documented.

- **Low computational overhead for a post-training method.** Statistics computation requires only a single forward pass (102 seconds for RaWideResNet on CIFAR-10, ~90 minutes for ConvNeXt-L on ImageNet) with 2–3% inference-time cost (Section 4.2, Table 1 description). This is quantified and meaningful.

- **Demonstrated generality across architectures.** Improvements are shown on CNNs (WideResNet, RaWideResNet, ConvNeXt-L) and a vision transformer (Swin-L), across three datasets (Section 4.2, Figure 3). This breadth is genuinely stronger than testing on a single architecture.

- **Transparent limitations section.** The paper explicitly acknowledges that MeanSparse does not improve robustness on standard (non-adversarially) trained models, and that adaptive attacks using identity backpropagation can reduce effectiveness (Section 4.4). This honesty is a real virtue.

## Weaknesses

### Major

- **Gradient masking acknowledged but the main narrative relies on non-adaptive AutoAttack.** The MeanSparse operation is a hard threshold: activations within μ ± ασ produce zero (or undefined) gradients. The paper states: "Although MEANSPARSE masks the gradient" (Section 4.3) and "white-box attacks that ignore the MeanSparse transformation during backpropagation and use the identity function can impact MEANSPARSE's effectiveness" (Section 4.4). However, the headline SOTA claims are built entirely on standard (non-adaptive) AutoAttack. The paper references adaptive evaluation in Appendix A.4 but does not quantify the robustness drop under that attack in the main paper. At ICLR, where gradient obfuscation (Athalye et al., 2018) is a well-known failure mode, the narrative should center the adaptive evaluation, not defer it to a supplementary section. The paper would be substantially stronger if the main text reported: (a) the numerical drop under BPDA/identity-backprop adaptation, and (b) a comparison showing whether the SOTA improvement persists. The paper does provide mitigating evidence (black-box attack improvements are referenced in A.3, and AutoAttack includes SquareAttack which is query-based), so this is not a fatal flaw — but the framing mismatch between the headline claims and the acknowledged vulnerability is a major weakness at a top venue.

- **The ℓ₀-regularization derivation is presented as theoretical grounding but explicitly discarded.** Section 3.1 develops a proximal-operator formulation for an ℓ₀-penalized optimization, then states it "is not used in the final MEANSPARSE technique" (line 83). The connection between the derived hard-thresholding operator and the actual method (which centers around the mean, not zero) is asserted rather than derived (line 128). The formal apparatus does no analytical work: it does not guide α selection, predict performance, or provide guarantees. Presenting the method as a simple statistical thresholding operation (block low-information features near the channel mean) would be more honest and concise. This is a presentation weakness that inflates the paper without adding substance.

### Minor

- **No principled procedure for selecting α.** The paper shows results for varying α in Table 1 and notes that α < 0.25 preserves clean accuracy on CIFAR-10, but the selection criterion is described only as "careful selection" (Section 4.2). For different architectures, datasets, or attack norms, the operating range may differ, and the paper provides no training-set-only heuristic for setting α without peeking at test-set robustness. A data-driven selection rule (e.g., based on feature-distribution statistics) would strengthen the method's practical usability and reduce the risk of implicit test-set fitting.

### Trivial

- None.

## Nice-to-Haves

- **Quantify the adaptive-attack robustness drop in the main paper.** If the adaptive (identity-backprop) AutoAttack numbers from Appendix A.4 show that most of the improvement survives, this would directly address the most serious concern. If the improvement collapses, the paper should be reframed accordingly (e.g., as a cautionary finding about post-hoc thresholding).
- **A per-layer or per-channel analysis** showing which layers or channels contribute most to the robustness improvement would convert the current black-box operation into actionable insight.

## Removed Points

The following points from the harsh critique were considered but are removed for the reasons stated:

- **"Missing comparison to Feature Squeezing and other post-hoc defenses"** — REMOVED. Feature Squeezing is an input-level preprocessing defense; MeanSparse operates on internal activations. The paper's scope is activation-function modification, not input preprocessing. The critic's demand is scope creep.
- **"Adaptive attack results not quantified in main paper (as a standalone weakness)"** — REMOVED as a separate point and merged into the gradient masking concern above. The paper references Appendix A.4 for these results; per the review guidelines, the parser strips appendix content and the paper should not be penalized for content that exists but was not preserved in the extraction.
- **"Statistical significance dismissal is incorrect reasoning"** — REMOVED. The paper's claim that statistical significance tests are negligible is about the deterministic nature of the evaluation (post-training, no randomness; RobustBench results are highly consistent). This reasoning is reasonable for a deterministic evaluation setup with near-zero variance.
- **"Overfitting argument is a non sequitur"** — REMOVED. Showing similar trends on both training and test sets is standard evidence against overfitting (overfitting is characterized by improvement on training data but degradation on test data). The critic's interpretation is incorrect.
- **Strength: "Principled derivation from ℓ₀-regularized optimization"** — REMOVED. The paper itself states this optimization formulation "is not used in the final MEANSPARSE technique." The connection is decorative rather than functional and does not serve as a genuine strength.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the known tension between post-hoc hard-thresholding defenses and gradient obfuscation, but raise no novel conceptual insight not already in the adversarial robustness literature (Athalye et al., 2018; Tramer et al., 2020). The core observation — that the paper's theoretical framing is disconnected from its actual method — is an important presentational critique but not a new scientific insight.

## Suggestions

1. **Restructure the paper so adaptive evaluation is the centerpiece.** Move the results from Appendix A.4 into the main body, alongside the non-adaptive results. If the robustness holds under BPDA/identity-backprop, the contribution is genuine and well-supported. If it largely collapses, reframe the paper explicitly as a study of gradient obfuscation in post-hoc defenses.
2. **Remove or substantially compress the ℓ₀ proximal-operator derivation** and present MeanSparse directly as the statistical thresholding operation it is. The formal framing adds length without explanatory power.
3. **Provide a data-driven heuristic for α selection** that does not require test-set feedback (e.g., based on the fraction of training-set activations that fall within the threshold per channel).
4. **Add a per-layer ablation** showing which layers' activations contribute most to the robustness gain — this would distinguish the method from a single global knob.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>