Now I have all the information needed. Let me construct the final review.

---

## Summary

This paper studies backdoor attacks on CNNs from a frequency-domain perspective. It presents empirical evidence that high-frequency components (HFC) are more susceptible to perturbation-based backdoor attacks than low-frequency components (LFC), using experiments with random-noise triggers (0.06 intensity needed for HFC vs. 0.8 for LFC). It then proposes two techniques: (1) a strategy to render visible triggers invisible by masking out their low-frequency components and keeping only mid/high-frequency perturbations, and (2) a new attack that uses low-frequency DCT coefficients from a target-class image as a trigger, injected into a clean image's high frequencies. Experiments report near-100% ASR across CIFAR-10, MNIST, and CelebA on ResNet18, VGG16, and MobileNetV2, with limited defense evaluation against Fine-Pruning, STRIP, and GradCam.

## Strengths

- **Clean experimental demonstration of HFC vs. LFC susceptibility.** Section 3.2 (Figure 4) shows that random noise at intensity 0.06 injected into high frequencies achieves high ASR, while low frequencies require >10× that intensity (0.8) and still perform worse. This is a concrete, reproducible finding that directly supports a core claim of the paper.

- **The invisibility strategy preserves attack performance on tested settings.** Table 1 shows that after hiding visible triggers via mid/high-frequency extraction, BadNet retains ASR of 99.82%–100% across three datasets with minimal degradation (≤0.17%). This demonstrates a practical application of the frequency-domain insight.

- **The proposed attack achieves high ASR across diverse architectures and datasets.** The low-frequency semantic information attack reports 100% ASR on ResNet18, VGG16, and MobileNetV2 over CIFAR-10, MNIST, and CelebA, and the defense experiments (Fine-Pruning, STRIP, GradCam) suggest the attack is not trivially detected by these specific methods.

- **Systematic DCT-based experimental framework.** Section 3.1 provides a clean formalism using DCT/IDCT with frequency masks (Eq. 3) to isolate LFC and HFC contributions, enabling controlled investigation of how different frequency bands respond to backdoor perturbations.

## Weaknesses

### Major

- **No experimental comparison against existing frequency-domain backdoor attacks.** Section 2.2 discusses four prior frequency-domain methods (Wang et al. 2022a / FTROJAN, Feng et al., Zeng et al. 2021, Hammoud & Ghanem 2021) that also place triggers in mid/high frequencies or manipulate DCT spectra. The paper claims its attack is novel but never compares against any of these baselines experimentally. The claim of "100% ASR" is uninformative without knowing whether existing methods achieve comparable or better results on the same settings. This directly undermines the novelty claim for Contribution (4).

- **Missing critical experimental specifications.** The paper does not report: (1) the poisoning rate (what fraction of training data is poisoned?), (2) the value of the frequency threshold ξ used in the masks (Eq. 3), (3) the number of training epochs, (4) the number of independent runs or any variance/confidence metrics. A single unrepeated run with unknown poisoning rate reporting 100% ASR cannot be properly interpreted — a high poisoning rate would make the attack trivial. These gaps prevent reproducibility and assessment of reliability.

- **Overclaimed "mechanism analysis" that does not go beyond correlational observation.** The paper frames its frequency-domain analysis as "exploring the mechanism of CNN memorizing poisoned samples" (Contributions 1 and 2, Abstract). What is actually provided is: (a) a qualitative observation that different triggers activate different frequency bands (Figure 2), and (b) a correlational experiment showing that HFC random-noise perturbations achieve high ASR at lower intensity than LFC perturbations (Figure 4). There is no causal intervention, no theoretical derivation (despite citing Luo et al.'s F-Principle), and no attempt to distinguish memorization of frequency distribution from memorization of spatial patterns with frequency properties. The paper would be better framed as an *empirical study* of frequency-domain susceptibility rather than a "mechanism" analysis.

- **The "universal" invisibility strategy is evaluated too narrowly to justify the "universal" claim.** Only two visible attacks (BadNet and IAD) are tested in Table 1. The strategy is a straightforward DCT masking operation without claim-specific analysis of why it should generalize to arbitrary visible triggers. More importantly, **invisibility is never quantitatively measured** — no SSIM, LPIPS, human study, or detection metric is reported. The paper only reports ASR and BA, so the "invisibility" claim is entirely unsupported by evidence. The reader cannot tell whether the resulting perturbations are actually imperceptible.

### Minor

- **No rationale for choosing exactly half the dimensions** for the invisibility mask (k₁ > N₁/2, k₂ > N₂/2). Section 3 used ξ as a tunable threshold, but Section 4.1 fixes it to 0.5 without justification or sensitivity analysis.

- **The random-noise trigger experiment uses an unrealistic trigger** (per-sample random noise with no spatial structure). Real triggers are structured (patches, warps, etc.), so the finding that HFC is "more susceptible" may not directly transfer to practical attacks. The paper acknowledges this limitation weakly but does not test with structured triggers.

- **Defense evaluation is limited in scope and depth.** Only three defenses are tested (Fine-Pruning, STRIP, GradCam), and the evaluation is qualitative — no AUC for STRIP detection, no quantitative pruning trade-off curves for Fine-Pruning, no numerical heatmap similarity metric for GradCam. The conclusions (e.g., "entropy distribution closely resembles the clean model") are stated without supporting metrics.

- **No ablation of the attack's key design choices.** The attack has two ingredients: (a) using target-class low-frequency coefficients and (b) injecting them into high frequencies. Neither is ablated — e.g., using random coefficients instead of target-class LFC, injecting into low frequencies instead, or varying the upsampling method. Without these, the contribution of each design choice is unclear.

- **No clean-model baseline BA reported** alongside Table 2. The paper states "average BA improvement of 0.2%" but does not give the absolute BA or the clean model's BA, making this claim uninterpretable.

### Trivial

- The learning rate schedule "decaying by a factor of 10 every 100 training steps" (line 172) is unusual and potentially ambiguous — is it 100 steps or 100 epochs? The total number of training steps is not given. This should be clarified.

- The notation in Eq. 5 (line 101) uses interleaved Z̅_i and Ẑ_i with mask (1−mˡ) — this is clear enough but the prose introducing it (line 98–104) has run-on construction that makes the experimental procedure harder to follow than necessary.

## Nice-to-Haves

- A sensitivity analysis of the threshold ξ in the frequency masks (Section 3.1) would strengthen the empirical analysis.
- Comparing injection of target-class LFC vs. random noise vs. a fixed pattern as the trigger source would directly validate the "semantic information" design choice.
- Measuring invisibility via standard metrics (SSIM, LPIPS) for both the invisible strategy and the new attack would substantially strengthen the claims.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Table 2 is garbled/unreadable"** — The table is an embedded image in the original PDF. Its unreadability in plaintext extraction is a parser artifact, not a paper flaw.
- **"The upsampling module Φ is not specified"** — The paper specifies it as "linear two-dimensional interpolation" (line 157), which the reviewer overlooked.
- **"The Celeba dataset description is garbled"** — The "photos).5)." fragment is a parser artifact.
- **"Missing related works"** — Insufficient external knowledge to confirm; the paper cites relevant frequency-domain work in Section 2.2.
- **"Typos/grammar"** — Formatting artifacts from PDF extraction, not author errors.
- **"No theoretical analysis despite citing Luo et al."** — The paper cites Luo et al. for context; it does not claim to reproduce those derivations.
- **Strength Finder strength about "universal invisibility strategy"** — Dropped because the verification shows the "universal" claim is not adequately supported (only 2 attacks tested, no invisibility metrics), which conflicts with verified weaknesses. The empirical results on the two tested attacks are retained as a weaker strength.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's frame — that the paper's "mechanism" analysis is really a susceptibility observation — is accurate but does not add information beyond what is already apparent from reading the paper. The strength finder adds no novel synthesis.

## Suggestions

1. **Reframe the paper honestly.** Replace "exploring the mechanism" with "an empirical study of frequency-domain susceptibility to backdoor perturbations." This change aligns the framing with what is actually demonstrated and removes the central overclaim.

2. **Add experimental comparisons to existing frequency-domain attacks** (FTROJAN, Hammoud & Ghanem, etc.) on the same datasets and models. This is essential to establish the novelty of the proposed attack.

3. **Report all missing experimental specifications**: poisoning rate, ξ value, training epochs, number of runs, and standard deviations or confidence intervals for all metrics.

4. **Quantify invisibility** using SSIM or LPIPS for both the invisible strategy (Section 4.1) and the new attack (Section 4.2). Without this, the invisibility claims are unsubstantiated.

5. **Ablate the attack design**: compare target-class LFC triggers against random LFC coefficients, random noise, and fixed-pattern triggers to demonstrate that the "low-frequency semantic information" is actually beneficial.

6. **Broaden and deepen the defense evaluation**: include more recent defenses (e.g., Spectral Signatures, Neural Cleanse, Activation Clustering) and report quantitative detection metrics.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>