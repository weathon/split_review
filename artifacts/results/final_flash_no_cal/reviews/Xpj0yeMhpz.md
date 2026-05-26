Now I have all the information needed. Let me write the consolidated review.

## Summary

This paper introduces a novel formalism for machine unlearning that decouples the class label from the target concept, identifying three practically important mismatch scenarios (target mismatch, model mismatch, data mismatch) beyond the conventional all-matched setting. The authors propose TARF (TARget-aware Forgetting), which combines annealed gradient ascent on forgetting data with dynamic, contrast-guided gradient descent on hard-to-affect remaining data. The method is theoretically motivated by a "representation gravity" analysis and empirically validated across multiple datasets (CIFAR-10/100, ImageNet-1k), architectures, and real-world applications (concept removal in diffusion models, personal information removal in LLMs). TARF consistently outperforms prior methods in mismatch settings while remaining competitive in the conventional setting.

## Strengths

- **Novel and well-motivated problem formulation.** The paper systematically identifies that previous unlearning work assumed class labels and target concepts coincide, and defines a clear four-scenario taxonomy (all matched, target mismatch, model mismatch, data mismatch) formalized through label-domain relations (Section 3.1, Figure 1). This opens a practically important direction that existing methods cannot handle.

- **Theoretical characterization of forgetting dynamics.** Theorem 3.2 formally bounds the loss-gap between data subsets in terms of their representation distance, and Definition 3.3 ("representation gravity") operationalizes this to identify unobserved target-concept data. The analysis is further connected to the specific failure modes (insufficient representation, decomposition lacking) via Remarks 3.2 and 3.3, which directly motivate the algorithm design.

- **Effective and unified algorithmic framework.** The TARF framework (Section 3.3) elegantly unifies target identification and separation through a single loss function (Eq. 3) with time-dependent coefficients. The three-phase interpretation (identification → separation → retraining approximation) is conceptually clear. Empirically, TARF achieves the lowest Gap in all four mismatch settings on CIFAR-10/100 (Table 3) and ImageNet-1k (Table 4), often by a wide margin (e.g., Gap 0.21% vs. next-best 8.86% on CIFAR-100 target mismatch), while maintaining competitive performance in the all-matched setting.

- **Comprehensive empirical validation.** Experiments span CIFAR-10/100 with multiple architectures (ResNet-18, VGG-16bn, WideResNet-50), ImageNet-1k, concept removal in Stable Diffusion (Figure 6), and personal information unlearning on TOFU with LLaMA3.2 (Table 5). This breadth convincingly demonstrates the method's generality.

- **Thorough ablation analysis.** Figure 7 systematically investigates the annealed schedule for gradient ascent, initial strength \(k\), model architecture effects, and the choice of gradient operation on selected data, providing practical guidance for hyperparameter selection.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Numerical discrepancy in Table 3.** For the GA baseline on CIFAR-100 target-mismatch, the reported UA=21.38, RA=96.64, TA=70.22, MIA=99.67 and the Retrained reference (0.00, 97.85, 73.72, 100.00) yield a computed Gap of ~6.6 using the paper's stated formula \(( \frac{1}{4}\sum |\mathcal{R}_{\text{Retain}} - \mathcal{R}_{\text{Opt}}| )\), but the table reports 8.86. Other entries in the same table are consistent with the formula (verified for FT, RL, BS, L1-sparse, SCRUB, and TARF on both CIFAR-10 and CIFAR-100). This error does not affect the paper's conclusions—TARF's Gap (0.21) is far lower regardless—but it should be corrected for accuracy. The authors should clarify whether the displayed metric values or the Gap were computed from unrounded numbers.

2. **Ambiguity in the handling of identified false-retaining data.** In target-mismatch, false-retaining data (which belong to the target concept but are not part of the given forgetting set) are identified via Phase I and assigned \(\tau=0\), excluding them from the gradient descent objective in Phases II and III. Yet the model retains high accuracy on them (RA remains near the Retrained reference). The paper states Phase II "deconstructs the target concept" and Phase III "approximates the retraining objective," but the precise mechanism by which these excluded data recover accuracy—whether through shared-feature propagation from \(\tau=1\) data, representation-level effects, or another mechanism—is not clearly explained. A more explicit account of what each gradient operation accomplishes across the data subsets would improve reproducibility and clarity. (The ablation in Figure 7, right, confirms that gradient cleaning works better than gradient ascent on these data, which is informative but does not fully resolve the mechanistic question.)

3. **Incomplete specification of the notation \(\ell_h\) in Assumption 3.1.** The assumption states that "\(\ell_h(\cdot)\) is Lipschitz smooth with constant \(C_\ell\)" but does not explicitly define \(\ell_h\) in the main text. While the intended meaning (the loss function evaluated on the hidden representation \(h(x)\)) is inferable from context, a brief definition would improve readability.

### Trivial

- **Minor imprecision in Theorem 3.2.** The note "when \(t \rightarrow 0\), the RHS mainly relies on ... \((L_{s_1}(\theta^t)-L_{s_2}(\theta^t)) \rightarrow 0\)" could be read as implying the loss difference tends to zero because \(t \rightarrow 0\), when the intended logic is that at initialization (\(t=0\)), a well-trained model has near-equal losses on semantically related subsets. The reasoning is sound but the phrasing is slightly loose.

## Nice-to-Haves

- **Algorithm pseudocode.** The method is described through the loss function (Eq. 3) and Figure 4, but a compact algorithmic listing showing which gradient operation is applied to each data subset in each phase would aid reproducibility and implementation.
- **\(\beta\) sensitivity analysis in the main text.** The threshold \(\beta\), which controls which samples are retained, is a key hyperparameter; the quantile-choice analysis is deferred to Appendix E. A brief summary or plot in the main paper would strengthen the evidence for the method's practical robustness.
- **MIA attack specification.** The membership-inference attack is described only as "confidence-based predictor"; specifying the exact procedure (threshold, training set for the attack model) would improve interpretability of the MIA metric within the Gap.
- **Computation time breakdown.** TARF's total time is comparable to fine-tuning, but a breakdown of time spent in Phase I (identification) versus the later phases would be helpful for practitioners.

## Removed Points

The following points from the inputs were removed after verification against the paper:

- **"\(\mathcal{D}_t\) not formally introduced in the text."** The paper explicitly states "we adopt \(\mathcal{D}_t\) to indicate the dataset of the target concept" (Section 2, paragraph 2) before Table 1. This criticism is factually incorrect.
- **"Theorem 3.2 does not directly justify the specific form of the three-phase loss."** The paper presents the theorem as an intuitive motivation for the design, which is standard and acceptable for an empirical paper. This is not a weakness.
- **"The ablation on gradient operation is not reconciled with the claimed role of Phase II."** The paper does reconcile this: it states that gradient cleaning ("0") on the selected data avoids excessive feature deconstruction, which is consistent with the Phase II design where those data are assigned \(\tau=0\) and excluded from the loss.
- **Nitpicks about missing pseudocode/MIA specification as core weaknesses** (moved to Nice-to-Haves).

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface any perspective that the paper itself does not already address or acknowledge.

## Suggestions

1. **Correct the Gap value** for GA on CIFAR-100 target-mismatch in Table 3 (currently 8.86; should be ~6.6 based on the reported constituent metrics), or clarify if the displayed metrics and the Gap were computed from different precision levels.
2. **Add a paragraph in Section 3.3** explicitly describing how the model's accuracy on false-retaining data (excluded from both gradient terms) is preserved or recovered through the Phase III retraining approximation—e.g., via feature sharing with the \(\tau=1\) retaining data.
3. **Define \(\ell_h\) explicitly** when first used in Assumption 3.1 (e.g., "where \(\ell_h\) denotes the loss function evaluated on the hidden representation \(h\)").
4. **Move the \(\beta\)-quantile sensitivity summary** from Appendix E to the main text (or include a brief note in Section 4.3), given that this threshold is central to the target-identification step.
5. **Provide a pseudocode listing** of the full TARF algorithm in the main paper or appendix, clearly specifying which gradient operation applies to each data subset in each phase.

## Score and Decision

MY FINAL SCORE: <score>8.0</score>
MY FINAL DECISION: <decision>Accept</decision>