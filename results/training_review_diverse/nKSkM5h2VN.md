Now I have all the information I need. Let me compile the final consolidated review.

## Summary

This paper proposes a test-time adversarial defense framework centered on three elements: (1) an "opposite adversarial path" (OAP) training strategy that maps adversarial inputs to reference points pushed in the anti-adversarial direction, (2) integration of an OAP-trained purifier with reverse diffusion as a directional prior, and (3) a dual-path diffusion cleaning design that increases the computational cost of adaptive attacks. The paper also identifies a granularity pitfall in AutoAttack (Rand) evaluation for diffusion-based defenses. Empirical results on CIFAR-10/100 and ImageNet show the OAP prior improves both clean and robust accuracy when plugged into DISCO, and the dual-path method increases attack computation time 10–40× over DiffPure.

## Strengths

- **The OAP training strategy demonstrably improves existing defenses.** Table 2 shows that training DISCO with the OAP reference point (K=1) lifts robust accuracy from 73.13% to 86.10% under non-adaptive PGD-ℓ∞ (ResNet-18) and from 85.00% to 88.79% under non-adaptive AutoAttack (WRN-28-10), while also improving clean accuracy. This is a clear, quantifiable benefit over a competitive baseline.

- **The granularity pitfall in AutoAttack (Rand) evaluation is a useful methodological finding.** Table 3 shows that using per-step adjoint method calls (rather than one encapsulated call) drops DiffPure's robust accuracy from 76.56% to 64.06% on CIFAR-10, with similar trends on CIFAR-100 and ImageNet. This is an actionable implementation-level observation for the community.

- **The dual-path design substantially increases adaptive attack computation time.** Table 4 reports attack times increasing from 593s (DiffPure) to 6,881s (Ours) under BPDA+EOT, and from 3,633s to 22,722s under PGD+EOT. This makes adaptive attacks practically more expensive, which the paper correctly identifies as a trade-off rather than a principled guarantee.

- **The paper provides reasonable non-adaptive evaluation on full CIFAR-10 test set** with error bars for the OAP+diffusion method (Table 4 rows: 90.77±2.25% clean, 88.48±2.04% robust under PGD-ℓ∞; 90.46±2.36% clean, 89.06±2.62% robust under AutoAttack Standard), showing competitive performance under non-adaptive attacks.

## Weaknesses

### Major

- **The diffusion integration relies on an unvalidated gradient approximation.** Equation (8) replaces the conditional gradient  ∇_{x_{t-1}} log p_θ(x^K | x_{t-1}) with η(ŝ{x^K} − x_{t-1}), where ŝ{x^K} is the purifier's output at the same input. This substitution is not derived, and the paper provides no empirical validation (e.g., cosine similarity between the approximated direction and a reference gradient, or an ablation showing the term's contribution). Since the entire Sec. 3.2 contribution depends on this approximation, its lack of justification is a structural gap. The noise-augmented training (Eq. 9) partially addresses domain mismatch but does not validate the gradient proxy itself.

- **The DiffAttack evaluation (Table 4) is overestimated and presented without sufficient caveat.** The paper acknowledges (line 488) that "DiffAttack focuses on attacking the only one path by computing the gradient on it without meeting our dual path strategy," meaning the reported 93.75% robust accuracy (vs. 46.88% for DiffPure) comes from an attack that does not handle the defense's dual-path structure. This result is presented in the main table without qualification in the caption or footnote. A properly adaptive attack would need to compute gradients through both paths. The paper's own conclusion (line 502) vaguely notes possible overestimation. This significantly undermines the strongest quantitative claim.

- **The paper lacks an ablation study attributing gains to specific components.** The method has three main components: (a) OAP training of the purifier, (b) integration with reverse diffusion, and (c) dual-path cleaning with color transfer. Without ablations, it is impossible to determine whether the accuracy improvements in Table 4 come from the OAP prior, the diffusion integration, the dual-path design, or the color transfer. For example, does the diffusion+OAP combination in Sec. 3.2 outperform the OAP-only purifier (Sec. 3.1) on adaptive attacks? This is not tested.

- **The "excessive denoising" framing is at odds with the actual method.** The paper motivates the approach with Table 1, where K=5,10,20 opposite steps give near-100% robust accuracy on a non-defense classifier. However, for the trained purifier, K>1 degrades performance (Table 2), and the paper empirically sets K=1 throughout all main experiments (line 183, line 413). The paper explains this discrepancy, but the narrative and the practice remain in tension. The core idea that survives is a single-step opposite-direction push, which is closer to existing anti-adversarial approaches than the "excessive" framing suggests.

### Minor

- **Key experiments use small subsets.** The AutoAttack pitfall finding (Table 3) uses only 64 images. The adaptive attack results in Table 4 do not clearly state the test set size, and the paper mentions "different random seeds" without clarifying whether full 10,000-image CIFAR-10 test sets were used consistently. This raises concerns about estimate stability.

- **Equation (2) suggests joint optimization of classifier and purifier** (min_{p,θ} 𝔼 [max_{x'} ℒ((f_p ∘ g_θ)(x'), y)]), but the paper only trains the purifier θ while keeping the classifier f_p fixed. This formulation is never corrected, creating a misleading impression of the optimization scope.

- **The OAP prior is only demonstrated with DISCO as the base architecture.** The paper claims the purifier "can be plugged into pre-trained models" (Abstract) but Table 2 only tests DISCO+OAP. No results with alternative base architectures (e.g., UNet denoisers, other purifiers) are provided, limiting the generality claim.

- **The AutoAttack pitfall finding, while useful, is narrow in scope.** It is tested on only 64 images per dataset and compared only against DiffPure's implementation. The paper does not explore whether this granularity issue affects other diffusion-based defenses (e.g., DDA mentioned in related work) or whether the effect is complementary to other recently identified overestimation issues (e.g., the surrogate process of Lee et al. 2023).

### Trivial

- None beyond ordinary presentation issues typical of extracted PDFs.

## Nice-to-Haves

- Ablation study isolating the contributions of (a) OAP training alone, (b) OAP+diffusion integration, (c) dual-path design without color transfer, and (d) color transfer alone.
- Full test-set (10,000 images) evaluation for all entries in Table 4.
- Empirical validation of the gradient approximation in Eq. (8) (e.g., cosine similarity comparison or an ablation removing the term entirely).
- A genuinely adaptive attack for the dual-path method that handles both paths, with appropriately caveated results.

## Removed Points

- **Critical Issue 2 (training objective mismatch):** The reviewer claimed the mapping (x_adv → x^K) lacks meaningful correspondence because x^K is defined relative to the clean image. This is incorrect. Both x_adv and x^K are derived from the same underlying clean image x: x_adv = x + δ (adversarial perturbation) and x^K = x with K opposite steps applied. The training pairs share the same clean origin, making the supervised mapping standard — no different conceptually from training a denoiser on (noisy_in, clean_target) pairs. This criticism is removed.

- **Critical Issue 5 (time cost as non-contribution):** The reviewer claimed the time-cost increase is "trivially achievable by adding more computation." This overstates the case. The dual-path method both increases attack time AND yields modest accuracy improvements (81.25% vs. 80.92% under BPDA+EOT; 53.12% vs. 46.88% under PGD+EOT). The contribution is not purely about making things slower. Downgraded to Minor (the time-cost framing is a weak defense principle but not invalid).

- **Criticism about DDA not being compared experimentally:** The paper mentions DDA in related work but is under no obligation to include every possible baseline, especially when DiffPure (the most directly comparable diffusion-based defense) is the primary comparison partner.

## Novel Insights

The paper's most genuinely novel observation is the granularity pitfall: that the number of adjoint method calls in AutoAttack (Rand) evaluation of diffusion-based defenses matters significantly, and prior work (DiffPure) systematically overestimates robustness by using a single encapsulated adjoint call. This is a clean, implementation-level insight. The OAP training idea — pushing toward a deliberately "over-purified" reference rather than the clean image — is also a useful conceptual contribution, even if in practice only K=1 works and the "excessive" framing over-promises.

## Suggestions

1. Commit to whether the method uses K=1 or multiple steps in the narrative. If K=1 is what works, drop the "excessive denoising" framing in favor of "anti-adversarial directional push" — the results are still interesting without the overclaim.
2. Provide an ablation study: compare (a) vanilla DISCO, (b) DISCO+OAP(K=1), (c) DISCO+OAP+diffusion, (d) DISCO+OAP+diffusion+dual-path. This would let readers attribute gains and would likely strengthen the paper by showing each component's contribution.
3. Run a proper adaptive attack on the dual-path method that computes gradients through both paths, including the color transfer. Report the honestly degraded numbers alongside honest caveats.
4. Validate Eq. (8)'s approximation by measuring the cosine similarity between η(ŝ{x^K} - x_{t-1}) and the true  ∇ log p_θ(x^K|x_{t-1}) (which can be estimated via score-based methods) — or at minimum, ablate the OAP directional term entirely in the diffusion process to see its marginal effect.
5. Consistently report test-set sizes across all tables and report confidence intervals for all main results (Table 4 currently has ± values for some rows but not for the PGD+EOT and DiffAttack rows).

## Score and Decision

**Originality:** 6/10 — The OAP training direction and the AutoAttack granularity pitfall are novel; the dual-path time-cost idea is incremental.  
**Importance of research question:** 7/10 — Adversarial robustness remains important, and improving test-time defenses is a relevant direction.  
**Claims supported:** 4/10 — The core claims (OAP improves robustness) are partially supported, but the diffusion integration lacks validation, the DiffAttack result is overestimated, and the lack of ablations makes attribution impossible.  
**Soundness of experiments:** 4/10 — Small subsets, inadequate adaptive attack for a key result, missing ablations, and unclear test-set sizes collectively weaken the empirical foundation.  
**Clarity of writing:** 6/10 — Generally readable but the misleading Eq. (2) and the tension between "excessive" narrative and K=1 practice create confusion.  
**Value to community:** 5/10 — The AutoAttack pitfall finding is genuinely useful; the OAP training idea may inspire follow-up work, but in its current form the experimental validation is insufficiently rigorous.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>