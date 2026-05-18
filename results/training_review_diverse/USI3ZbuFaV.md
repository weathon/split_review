Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary

This paper proposes Fuzzed Randomized Smoothing (FRS), a certified defense against pre-training backdoor attacks on PLMs. It combines (1) biphased model parameter smoothing (adding Gaussian noise to top-H layers during fine-tuning and inference), and (2) MCTS-guided fuzzed text randomization (identifying trigger-prone segments and concentrating randomization probability there). The paper claims a broader certified robustness radius via Corollary 1 and validates empirically across three datasets, three attack methods, and five victim models.

## Strengths

- **Novel problem framing and practical motivation**: FRS is explicitly designed for the post-attack scenario where defenders have no access to the original poisoned pre-training data (Section 4.2). This directly targets a gap in prior work that requires in-attack access.

- **Strong and consistent empirical defense across multiple dimensions**: FRS outperforms all baselines (six empirical + TextGuard) on CA, PA, and ASR across SST-2, OffensEval, and AG's News under RIPPLe_a, LWP, and BadPre attacks (Table 1). Example: on SST-2 under RIPPLe_a, FRS achieves 91.3% PA and 6.2% ASR vs. TextGuard's 85.1% PA and 15.8% ASR, while maintaining higher CA (92.4% vs. 85.2%). These results use K=20 for both methods.

- **Ablation confirms additive contribution of both modules**: Table 3 shows that removing either BMPS or FTR degrades PA and increases ASR across all three datasets. E.g., on SST-2 with BadPre, PA drops from 88.7% (full FRS) to 83.2% (-FTR) and 80.5% (-BMPS).

- **Consistent advantage across diverse architectures and scales**: FRS maintains its edge over TextGuard across BERT-base/large, RoBERTa-base/large, and LLaMA3-8B (Table 4), covering 110M to 8B parameters and both encoder and decoder architectures. On OffensEval under RIPPLe_a with RoBERTa-large: FRS 85.3% PA vs. TextGuard 78.7% PA.

- **Novel MCTS-based fuzzing for non-uniform text randomization**: The idea of using MCTS to proactively search for trigger-prone segments before applying randomized smoothing is genuinely novel and borrows productively from software fuzzing (Section 4.3).

## Weaknesses

### Fatal

None.

### Major

1. **The theoretical certificate rests on an unverified premise about MCTS success.** Theorem 1 and Corollary 1 assume that the identified vulnerable area contains the trigger and that randomization probability ω_H applies to the trigger segment. But the MCTS identification procedure (Section 4.3.1) is heuristic — there is no guarantee it locates the trigger, no analysis of its failure probability, and no quantification of how MCTS failure degrades the certificate. The paper acknowledges that "with more MCTS iteration budget, the confidence that the trigger is successfully captured can be higher" but provides no analysis linking iteration budget to capture probability. Without this, the certified robustness guarantee is not grounded.

2. **No standard certified accuracy curves (accuracy vs. radius).** In the randomized smoothing literature (Cohen et al., 2019 and follow-ups), the standard evaluation is to report certified test-set accuracy as a function of radius. The paper instead reports average and maximum robustness radii (Table 2). While these numbers show FRS outperforms TextGuard, they do not convey how many test points are certified at various radii, nor do they allow comparison with other certified defenses in the standard way. The description in §5.2.2 ("find the maximum percentage of tokens that can be perturbed while the model still maintains correct prediction with high probability") describes an empirical search rather than a formal certification procedure, and the paper does not clarify how the binary search over radii is connected to the beta-binomial confidence bound of Theorem 1. Without accuracy-vs-radius curves, the claim of "broader certified robustness" — the paper's headline theoretical contribution — is only partially supported.

3. **The theoretical derivation is not a rigorous robustness certificate in the standard RS sense.** The derivation of Theorem 1 and Corollary 1 uses a simple bound Δ = 1 − ω^{R_rL} that assumes independent token randomization — it does not account for the adversarial selection of trigger tokens within the radius, nor does it derive a tight bound via the Neyman-Pearson lemma as in standard RS. The resulting "radius" R_r^{new} = log(ω_M)/log(ω_H) × R_r^{old} follows from simple algebraic manipulation of this bound; it is not a certificate that any perturbation within this radius is safe, but rather a calculation of how the Δ bound changes with ω. The paper conflates a bound comparison with a certified robustness guarantee. The gap between the claimed "provably broader certified robustness radius" and what is actually derived is significant.

### Minor

1. **The radius computation procedure is underspecified.** Section 5.2.2 describes finding "the maximum percentage of tokens that can be perturbed while the model still maintains correct prediction with high probability (e.g., 95% confidence)" but does not detail the search algorithm, confidence correction for multiple testing, or how this connects to the beta-binomial bound in Theorem 1. The use of K=20 base models is modest for RS — standard practice uses thousands of Monte Carlo samples. The paper should clarify how certification is performed in practice.

2. **No runtime or memory analysis.** The method requires: (a) fine-tuning with clipped SGD + noise (Eq. 4), (b) generating K=20 pre-duplicated models with noise on top-H layers at inference start (Eq. 5), (c) per-sample MCTS search, and (d) K=20 forward passes per sample. The paper provides no runtime comparison against TextGuard or any baseline. The claim of "efficient" defense is unsubstantiated. Note: the reviewer's claim of "160B parameters" is incorrect — noise is applied only to top H=10 layers, so the memory overhead is approximately one base copy plus 20 noise vectors for H layers, which is more tractable. Still, the computational cost deserves quantification.

3. **No hyperparameter sensitivity analysis.** The paper uses fixed values for ω_H, Λ, H, σ, and MCTS budget without justification, ablation, or sensitivity study. These parameters likely interact in complex ways (e.g., H controls how much of the model is perturbed; σ controls the noise variance; the MCTS budget affects trigger identification quality).

4. **Assumption 1 requires stronger justification.** The paper assumes "the output of the smoothed model on benign input is consistent with that of the clean fine-tuned model" and claims this "can be approximately guaranteed with the biphased parameter smoothing as long as η is set small enough." No evidence or analysis is given to support this claim. Given that pre-training backdoors are known to persist through standard fine-tuning, this assumption is nontrivial and warrants explicit validation (e.g., comparing FRS's outputs on benign inputs to a truly clean model's outputs).

5. **Standard deviations not reported.** Table 1 reports numbers with four decimal places but no standard deviations, despite 5 random seeds being run. The t-test significance is mentioned but unverifiable without variance information.

### Trivial

None worth enumerating separately beyond what is already listed above.

## Nice-to-Haves

- Certified accuracy vs. radius plots (this is the single most impactful addition — would address Weakness 2 above).
- Ablation of the MCTS component: compare FRS against (a) uniform randomization, (b) random segment selection, (c) an oracle that knows the trigger location. This would directly quantify the benefit of MCTS-guided fuzzing.
- Runtime and memory comparison with TextGuard and empirical baselines.
- Sensitivity analysis for key hyperparameters (ω_H, MCTS budget, H, σ).

## Removed Points

These points from the reviewer were removed per the filtering rules:
- **"Notation in Eq. 2 is garbled"** — The garbled LaTeX (`\big\langle\big|\frac{\d H^{\prime}}{\d F}`) appears in the prose of Section 3, not Eq. 2. Per the instruction, formatting artifacts from PDF extraction are parser issues, not author errors.
- **"The paper never clarifies how biphased parameter smoothing relates to the ensemble definition"** — The paper explicitly states in Section 4.1 that θ̃_F = [θ̃_F,1, ..., θ̃_F,K] is the ensemble, and Section 4.2 describes generating the K copies via Eq. 5. The connection is clearly drawn.
- **"20 × 8B = 160B parameters, not feasible"** — The noise in Eq. 5 is applied only to top-H layers (H=10), not the full model. The memory overhead is one base copy plus noise vectors for H layers, not 20 full copies. The computational cost concern is valid (kept in Minor) but the memory claim is factually incorrect.
- **"TextGuard may require a different K"** — The paper states "we adopt the same number of base models here in TextGuard and FRS for fair comparison" (Section 5.2.1), directly addressing this concern.
- **"No comparison to other certified defenses (Zhang et al. 2023, Weber et al. 2023)"** — Missing-baseline complaints about papers I cannot independently verify are removed per instructions. The paper cites relevant vision-only RS works (Weber et al., Wang et al., Xie et al.) in the related work and notes the gap in text-domain certified backdoor defenses.

## Novel Insights

The reviews surface an interesting tension: the paper's strongest contribution — the MCTS-guided fuzzing that proactively searches for triggers — is also what undermines its theoretical rigor as a *certified* defense. Certification requires covering the worst-case perturbation; a heuristic search that might miss the trigger cannot provide a worst-case guarantee. This suggests the paper might be more honestly positioned as a **practical defense with empirical robustness guarantees** (where the MCTS search demonstrably improves robustness in practice) rather than a **certified defense with provable guarantees** in the strict RS sense. Re-framing the contribution around the empirical improvement — supported by the strong results in Tables 1-4 — would resolve much of the tension between the claimed theory and what is actually demonstrated.

## Suggestions

1. **Re-frame the theoretical contribution honestly.** Either (a) tighten the certificate to account for MCTS failure probability (e.g., via a union bound over identification failure), or (b) drop the "certified" framing and present the method as an empirically validated defense that uses RS-style voting as a component. The empirical results are strong enough to stand on their own without overclaiming the theory.

2. **Add standard certified accuracy vs. radius curves** for all three datasets, with comparisons to TextGuard. This is the minimal addition needed to support the "broader certified robustness radius" claim.

3. **Ablate the MCTS component** against uniform randomization, random segment selection, and an oracle that knows the trigger. This would directly quantify how much of the benefit is due to intelligent trigger search.

4. **Report standard deviations** for all main results (Tables 1, 2, 4) and clarify the certification procedure (how the beta-binomial bound connects to the binary search for radius in §5.2.2).

5. **Include a runtime comparison** (inference time per sample) and **memory analysis** for FRS vs. baselines.

## Score and Decision

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>