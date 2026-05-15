I'm unable to list the human reviews directory with the available tools, so I will proceed with the review based on my direct analysis of the paper and the provided reviewer inputs.

Let me now output the final consolidated review.

---

## Summary

This paper proposes Fuzzed Randomized Smoothing (FRS), a defense against pre-training-phase textual backdoor attacks on PLMs. FRS has two main components: (1) **biphased model parameter smoothing** — adding Gaussian noise to top-*H* layers during fine-tuning and inference to reduce computational cost, and (2) **fuzzed text randomization** — using MCTS to identify vulnerable input regions and focusing randomization probability there rather than uniformly. The paper provides a theoretical analysis (Corollary 1) claiming a broader certified robustness radius when using non-uniform over uniform randomization, and validates empirically across three datasets, three attack methods, and several model architectures (BERT-base to LLaMA3-8B).

## Strengths

- **Consistent and broad empirical superiority.** Table 1 shows that FRS outperforms both empirical defenses (RIPPLe_d, ONION, RAP, Bite, PSIM, BKI, R-Adaptor) and the only certified baseline (TextGuard) on CA, PA, and ASR across three datasets and three attack methods (RIPPLe_a, LWP, BadPre). The improvements over TextGuard on ASR are often substantial (e.g., SST-2 RIPPLe_a: 6.2% vs. 13.5%) *and* FRS simultaneously achieves higher clean accuracy (92.1% vs. 80.3%), meaning it is less destructive to benign performance. Statistical significance (*p*<0.01, *t*-test) is reported.

- **Ablation confirms both modules contribute.** Table 3 demonstrates that removing either the biphased model parameter smoothing (‑BMPS) or the fuzzed text randomization (‑FTR) degrades PA and increases ASR across all settings, e.g., on AG'News under RIPPLe_a, ASR rises from 7.1% (full FRS) to 12.0% (‑FTR) and 15.3% (‑BMPS). This provides clear evidence that each component serves a distinct, positive purpose.

- **Scalability across model sizes and architectures.** Table 4 shows FRS consistently outperforms TextGuard on BERT-base, BERT-large, RoBERTa-base, RoBERTa-large, and LLaMA3-8B, spanning 110M to 8B parameters and both encoder/decoder architectures. The advantage holds even for the largest model, though the margin narrows — a finding the paper honestly acknowledges.

- **Novel application of MCTS-based fuzzing to NLP backdoor defense.** Adapting software fuzzing ideas (MCTS with UCB selection, KL-divergence-based scoring, mutation operators in Damerau-Levenshtein space) to proactively localize vulnerable input regions is a genuinely novel methodological contribution that goes beyond uniform randomization.

- **Biphased parameter smoothing reduces computational overhead.** Training once with injected noise and then generating *K* noisy parameter copies at inference avoids the cost of fine-tuning *K* separate models — a practical engineering contribution that makes the method more realistic for large PLMs.

## Weaknesses

### Fatal
None.

### Major
1. **The "certified robustness radius" in Table 2 is empirically measured, not a theoretical certification bound.** The paper states (lines 267–268) that it finds "the maximum percentage of tokens that can be perturbed while the model still maintains correct prediction with high probability." This is an empirical search, not a certified bound derived from the smoothing distribution (as in standard randomized smoothing, which uses Neyman-Pearson-based provable radii). The theoretical radius formula in Corollary 1 is *never directly computed and compared* to these empirical values. The section title "Certified Robustness Radius" is therefore misleading. This gap between the claimed theoretical certification and the actual experimental measurement weakens the paper's central quantitative claim.

2. **The theoretical derivation (Section 4.4) relies on strong assumptions that are not validated for the actual attacks studied.** Theorem 1 and Corollary 1 assume: (a) the trigger is a contiguous segment of exactly *R*_r*L* tokens, (b) the trigger lies entirely within the MCTS-identified vulnerable region, (c) randomizing each token independently with probability ω fully neutralizes the backdoor, and (d) the smoothed model on benign input perfectly matches the clean fine-tuned model (Assumption 1). No experiments verify whether these hold for the actual attacks tested (RIPPLe, LWP, BadPre), many of which use non-contiguous or syntactic triggers. The derivation does not account for the data-adaptive nature of the MCTS distribution — the analysis assumes the trigger is correctly found without bounding the search's failure probability. Without validating these assumptions or providing a bound that accounts for search uncertainty, the theoretical contribution is only a first sketch, not a complete certification.

3. **Only one certified defense baseline (TextGuard) is compared.** While the paper compares against seven empirical defenses, it benchmarks against a single certified method. The paper's central framing is about "certifying language model robustness" — yet there is no comparison to other randomized-smoothing-based certified approaches adapted to text (e.g., different smoothing distributions or certification procedures). The absence of a second certified baseline makes it difficult to attribute FRS's advantages specifically to the fuzzing innovation rather than to orthogonal factors like model capacity or fine-tuning details.

### Minor
1. **The definition of "certified robustness against backdoor attacks" (Section 3, Eq. 1) is input-perturbation robustness, not training-phase backdoor certification.** The paper requires that for any x' within distance *R*_r*L* of benign x, the defended model's prediction on x' equals the clean model's prediction on x. This is a valid guarantee that triggers within the radius are neutralized. However, it differs from what parts of the literature call "backdoor certification" (e.g., Weber et al., 2023), where the guarantee is that *the training process* creates no effective backdoor. The paper should acknowledge this distinction explicitly to avoid confusion.

2. **The assumption that MCTS-identified high-KL regions contain triggers is unvalidated.** Section 4.3 identifies "vulnerable areas" via KL divergence between model predictions on mutated vs. original inputs. This measures *any* sensitive region, not specifically trigger-containing ones. No case study or synthetic experiment verifies whether the identified regions actually overlap with ground-truth triggers. The entire fuzzing mechanism depends on this correspondence.

3. **The robustness radius improvement in Table 2 is not tied to the Corollary 1 formula.** The paper reports 25–35% average radius improvements empirically, but the theoretical formula (R_r_new = log(ω_M)/log(ω_H) × R_r_old) is never instantiated with actual ω values to verify whether the predicted expansion matches the observed one — a straightforward computation given the stated ω_H, ω_L, ω_M.

4. **Parameter noise on top-*H* layers as a backdoor-neutralization mechanism is justified only by a single citation (Kurita et al., 2020), which studies a specific attack (RIPPLe).** Whether adding isotropic Gaussian noise to the last *H* layers generalizes across attack types and model architectures is not theoretically derived or independently ablated beyond the main results.

### Trivial
None.

## Nice-to-Haves
- Direct computation of the theoretical certified radius from Corollary 1 using the stated ω values, and a comparison to the empirical radius.
- A case study on a few examples with known trigger positions to verify MCTS localization accuracy.
- A second certified baseline (e.g., a uniform-smoothing variant of the paper's own framework with a proper Neyman-Pearson certified radius).
- An analysis of how MCTS iteration budget affects trigger localization quality and downstream robustness.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Framing mismatch: the paper does not certify robustness against backdoor attacks."** The paper explicitly defines its certification in Section 3 (Eq. 1): for any input within the distance bound, the defended model's prediction on the perturbed input equals the clean model's prediction on the clean input. This is a valid form of backdoor-defense certification — it guarantees that any trigger inserted within the radius is ineffective. The criticism conflates *training-phase* backdoor certification (does the training process create an effective backdoor?) with *inference-time* defense certification (does the defense neutralize triggers within a bound?). The paper is clear about its setting (post-attack, no access to poisoned data). This criticism is therefore a category error. It has been reduced to a minor terminology-clarity suggestion above.

- **"The certified robustness radius is not properly derived for non-uniform randomization."** The derivation in Corollary 1 is mathematically valid *under its stated assumptions* (contiguous trigger, trigger within identified vulnerable area, independent randomization). The algebra follows directly from the framework. The criticism that the derivation "does not account for adaptivity" is correct but describes the *strength of the assumptions*, not an algebraic error. This is now covered in Major weakness #2 as a limitation of the assumptions rather than an invalid derivation.

- **"Key experimental hyperparameters are unspecified, undermining reproducibility."** The paper provides K=20, σ=0.01, H=10, and GPU setup. Additional parameters (MCTS iterations, C, Λ, ω_H, ω_L, learning rate, ρ, I) would typically appear in the appendix, which the parser strips. Per guidelines, reproducibility nitpicks about parameters likely in the appendix should be removed.

- **Various section-by-section notes** that restate observations already acknowledged in the paper (e.g., "parameter smoothing hurts benign accuracy" — the ablation in Table 3 explicitly discusses this) or criticize methodology choices standard for the field (e.g., not reporting confidence intervals in tables despite reporting *p*<0.01 from *t*-tests).

## Novel Insights

The most novel observation emerging from synthesizing these reviews is the fundamental tension between the paper's two components: the theoretical certification framework (Corollary 1) assumes that the MCTS search correctly identifies the trigger region, but the paper provides no evidence that MCTS finds triggers rather than generic high-sensitivity regions. If MCTS simply identifies regions where the *defended* model has high KL-divergence under mutations, those regions may not correspond to the actual trigger at all — yet the certification guarantee depends on this correspondence. This creates an unaddressed circular dependency: to certify the defense, one must first certify the trigger-localization mechanism. Future work could address this by either (a) providing a separate probabilistic bound that the MCTS search covers the trigger with high confidence, or (b) decoupling the certification from the localization assumption by using a distribution that is provably trigger-covering (e.g., randomizing all segments with sufficient probability) while still achieving efficiency through the biphased parameter smoothing.

## Suggestions
1. **Rename Table 2's metric** from "certified robustness radius" to "empirical robustness radius" and directly compute the theoretical certified radius from Corollary 1 for comparison. If it cannot be computed (e.g., because ω values cannot be calibrated), acknowledge this limitation.
2. **Validate trigger localization** with a synthetic experiment where ground-truth trigger positions are known, measuring the overlap rate between MCTS-identified regions and actual trigger positions.
3. **Add a terminology clarification** in Section 3 or 4 that FRS certifies inference-time robustness (triggers within the radius are neutralized) rather than training-phase certification (no effective backdoor exists in the model), to prevent misinterpretation.
4. **Instantiate Corollary 1** by reporting ω_H, ω_L, ω_M and computing R_r_new from the formula, comparing to the empirical radius from Table 2.
5. **Add at least one additional certified baseline** — even a uniform-randomization version of the paper's own framework with a proper certification bound — to strengthen the claim of certified superiority over alternatives.

## Score and Decision

This paper addresses an important and under-explored problem with a genuinely novel methodological idea (MCTS-guided fuzzing for randomized smoothing). The empirical results are consistently positive across diverse settings, and the ablation convincingly validates both components. The biphased parameter smoothing is a practical contribution that makes the approach computationally feasible.

However, the paper's central claim — broader *certified* robustness radius — is not properly validated. The experimental radius is empirically estimated, not certified; the theoretical derivation rests on strong unverified assumptions; and the comparison set includes only one certified baseline. These are substantive issues that affect the core contribution but are addressable with additional analysis, clearer terminology, and more rigorous experimental design.

The paper represents a useful empirical contribution and a novel methodological direction, but in its current form, the theoretical claims outrun the evidence provided.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>