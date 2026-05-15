Now I have a thorough understanding of the paper and the reviews. Let me construct the final consolidated review.

---

## Summary

This paper proposes a test-time adversarial defense method based on "excessive denoising along the opposite adversarial path" (OAP). The key ideas are: (1) training a purifier to map adversarial inputs toward points shifted in the *opposite* direction of a PGD attack (away from, rather than toward, the decision boundary); (2) integrating this OAP prior with diffusion-based purification; and (3) a dual-path cleaning purifier (DPC) that increases the computational cost of adaptive attacks. The paper also identifies a pitfall in AutoAttack (Rand) evaluation for diffusion-based defenses, showing that using granular (per-step) adjoint calls yields stronger attacks than the single-call approach in DiffPure.

## Strengths

- **Novel conceptual idea (OAP) with clean motivating evidence.** The controlled experiment in Table 1 demonstrates that moving data along the opposite gradient direction (using ground-truth labels) can dramatically increase accuracy on a normally trained classifier, providing a clear conceptual foundation for why "excessive denoising" along OAP could be beneficial. This insight — that moving *away* from the decision boundary rather than toward perceptual similarity is a viable defense principle — is genuinely novel.

- **OAP is demonstrated to improve existing defenses as a plug-and-play module.** When OAP (K=1) is integrated with DISCO, clean accuracy improves from 89.26% to 92.5% and robust accuracy from 82.99% to 88.29% under PGD-ℓ∞ (Table 3). This shows that the OAP training target generalizes beyond the paper's specific pipeline and can upgrade existing test-time defenses.

- **Important evaluation finding about AutoAttack (Rand) and diffusion-based defenses.** Section 4.4 shows that DiffPure's robustness is overestimated when using a single adjoint call: robust accuracy drops from 76.56% to 64.06% on CIFAR-10 (Table 3 in Sec. 4.4) when per-step adjoint calls are used. This is a concrete, reproducible finding that exposes a methodological flaw in the prior evaluation of diffusion-based defenses, and the paper applies this improved evaluation to its own adaptive attacks.

- **Practical consideration of attack computation cost.** The DPC design increases attack time by roughly 10× over DiffPure (e.g., 6880.97s vs 592.92s per image under BPDA+EOT), creating a genuine trade-off between attack effectiveness and computational cost. This is a legitimate practical consideration, even if it is not a robustness guarantee.

## Weaknesses

### Fatal
None.

### Major

- **The most impressive robustness result (93.75% under DiffAttack) is achieved against an attack that does not properly adapt to the dual-path structure.** The paper explicitly acknowledges (line 488) that "DiffAttack focuses on attacking the only one path by computing the gradient on it without meeting our dual path strategy." This means the 93.75% figure is not a meaningful robustness evaluation — it is an artifact of the attack not being designed for the defense. A proper adaptive attack that jointly computes gradients through the full dual-path pipeline (color transfer + dual diffusion + baseline purifier) is absent from the evaluation. Without this, the paper's robustness claims for DPC are unsubstantiated.

- **Gains over DiffPure under properly adapted attacks are marginal.** Under BPDA+EOT, DPC achieves 81.25% vs. DiffPure's 80.92% — essentially within variance. Under PGD+EOT, the gap is 53.12% vs. 46.88% (~6%), which is modest. Combined with the unadapted-DiffAttack issue above, the claimed empirical advantage of DPC over the state of the art is not compelling. The core OAP+diffusion method (Section 3.2) performs comparably to DiffPure (88.48% vs. 87.21% under PGD-ℓ∞, 89.06% vs. 87.71% under AA-Standard), but these are small margins.

### Minor

- **The motivation experiment (Table 1) uses "Robust Accuracy" in a non-standard way.** The column labeled "Robust Accuracy" in Table 1 measures accuracy on data shifted along the opposite gradient direction (not accuracy under adversarial perturbation). While the experiment is clearly described and the procedure is transparent, the terminology is potentially misleading — especially since the paper's own Section 4 notes that "robust accuracy is measured for adversarial samples." The "robust accuracy" values (e.g., 100% at K=-20) are not comparable to standard robust accuracy metrics used elsewhere in the paper, and the framing could give readers an inflated impression of what OAP can do.

- **The min-max formulation in the introduction is not actually optimized.** The paper presents (line 25) a min-max objective $\min_{p,\theta} \mathbb{E}[\max_{x'\in B(x)} \mathcal{L}((f_p \circ g_\theta)(x'), y)]$ as the "formulation of processing the input data," but the actual training objective (Eq. 3) is a simple L1 minimization $\|g_\theta(x_{adv}) - x^K\|_1$ that does not involve any inner maximization or joint optimization over the classifier. This creates a disconnect between the stated formulation and the implemented method.

- **The "excessive denoising" claim is tempered by the K=1 choice.** The paper's name and framing emphasize *excessive* denoising (multiple steps), but the actual defense defaults to K=1. The paper acknowledges the inconsistency (lines 180–184) and explains it as resulting from the absence of ground-truth labels during actual training. However, this means the practical contribution reduces to a single-step gradient-direction mapping, which is conceptually closer to prior anti-adversarial methods (e.g., Anti-Adv) than the "excessive" framing suggests.

- **Several important hyperparameters lack sensitivity analysis and the evaluation is over multiple attacks but only on a subset of data.** Parameters such as η (step size in Eq. 9), t* (diffusion time step), ε (Sinkhorn divergence), the number of target images C, and the K value itself are not analyzed for sensitivity. Moreover, the adaptive attack evaluation uses different data sizes and random seeds than the non-adaptive evaluation, making the two sets of results not directly comparable (as the paper itself notes on line 491).

- **The reported attack time costs lack variance information.** While hardware is specified (Intel Xeon Platinum 8280 + NVIDIA V100, line 406), the time costs in Table 4 are reported as single values without standard deviations or information about how many runs were averaged. Given the stochastic nature of diffusion processes and EOT, time costs likely vary across runs, and this information would be needed for reproducibility.

### Trivial
None.

## Nice-to-Haves

- An ablation experiment comparing the full OAP+diffusion method against the same diffusion process with standard guided-diffusion conditioning (without the OAP prior) would help isolate the benefit of the OAP term.
- Cross-classifier evaluation (testing with a different classifier than the one used to generate OAP training targets) would strengthen the "plug-and-play" generality claim.
- Visual examples of the "excessively denoised" outputs (x^K) would help assess whether the method trades perceptual quality for robustness.

## Removed Points

- **"Time cost reported without hardware details":** REMOVED — the paper specifies hardware (line 406: "Intel Xeon(R) Platinum 8280 CPU and NVIDIA V100") and mentions using 8 V100 GPUs (line 486). This criticism is factually wrong.
- **"DPC test in Figure 2 attack not clearly specified":** REMOVED — the paper clearly states (lines 314–315) that "The adaptive adversarial image x_adv is generated via BPDA+EOT." The critic missed this.
- **"Missing appendix/proofs" claims:** REMOVED per instructions — the parser strips appendix sections; they exist in the original submission.
- **Several formatting/style nitpicks from the harsh critic:** REMOVED per instructions.
- **"The granularity observation should be applied uniformly to all baselines"** (from Missing Parts): This is a reasonable suggestion but the paper states (line 360, 417) that this adjoint strategy IS used in implementing the adaptive attacks throughout the experiments. The granularity finding is specifically about AutoAttack (Rand), and the paper's adaptive evaluation uses BPDA+EOT, PGD+EOT, and DiffAttack, which are different attack families. This is more of a scope clarification than a missing experiment. Weaken to nice-to-have.
- **Strength Finder - generic strengths like "addresses important problem":** REMOVED — generic statements not backed by specific evidence from the paper.

## Novel Insights

The harsh critic correctly identifies that the DiffAttack result (93.75%) is not a meaningful robustness figure because the attack does not adapt to the dual-path structure. This is the single most important unresolved tension in the paper: the paper's most eye-catching number is produced by an evaluation protocol the paper itself admits is incomplete. Conversely, the Strength Finder correctly identifies that the OAP concept is genuinely novel and the granularity-of-adjoint finding is a real methodological contribution with implications beyond this paper. The two reviews together reveal a paper with a solid conceptual core (OAP) and a useful evaluation finding (adjoint granularity), but whose main defense pipeline (DPC) is not adequately stress-tested against properly adapted adversaries.

## Suggestions

1. **Implement and evaluate against a properly adapted attack for DPC.** The most critical missing experiment is an adaptive attack that jointly backpropagates through the full dual-path pipeline (color transfer, dual diffusion, baseline purifier). Without this, the robustness claims for DPC are not credible and the paper's main selling point (the 93.75% against DiffAttack) is misleading.

2. **Address the terminology issue in Table 1.** Re-label the "Robust Accuracy" column to clarify that it measures accuracy on data shifted along the opposite gradient direction, not accuracy under adversarial perturbation. Alternatively, frame it purely as a proof-of-concept without using the term "robust accuracy."

3. **Align the stated formulation with the actual method.** Either remove the min-max objective from the introduction or clarify that it is an ideal formulation that the method approximates via the OAP training target, not an objective that is directly optimized.

4. **Add sensitivity analysis and variance for key hyperparameters and time costs.** Report time costs with means and standard deviations across multiple runs, and include ablation studies on η, t*, C, and K.

## Score and Decision

The paper has a genuinely novel conceptual insight (OAP) and a useful evaluation contribution (adjoint granularity for AutoAttack). However, the main claimed defense pipeline (DPC) is not adequately evaluated: the most impressive robustness result comes from an attack that does not adapt to the defense structure, a problem the paper itself acknowledges. Gains over the strongest baseline (DiffPure) under properly adapted attacks are marginal. These evaluation gaps prevent the paper from substantiating its central robustness claims.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>