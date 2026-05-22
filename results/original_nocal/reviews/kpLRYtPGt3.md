Now I have all the verification I need. Let me produce the final consolidated review.

## Summary

Neon introduces a strikingly simple post-hoc parameter merge that improves generative models by (1) briefly fine-tuning on self-generated synthetic data (which degrades performance), then (2) reversing that degradation via negative extrapolation: θ_Neon = θ_r − w(θ_s − θ_r). The paper proves that mode-seeking samplers (low temperature, CFG, top-k) create anti-alignment between synthetic and real-data gradients, so reversing the synthetic gradient reduces the true-data risk. Empirically, Neon improves diffusion, flow matching, autoregressive, and few-step models across ImageNet, CIFAR-10, and FFHQ — achieving a state-of-the-art 1.02 FID on ImageNet-256 with xAR-L using only 0.36% extra compute and as few as 1k synthetic samples.

## Strengths

- **State-of-the-art result with negligible overhead.** Neon elevates xAR-L on ImageNet-256 from 1.28 to 1.02 FID, surpassing UCGM's 1.06 (Sun et al., 2025), using only 0.36% additional training compute (Section 4.2, Figure 5). This directly demonstrates the core claim that reversing self-training degradation yields substantial quality gains at minimal cost.

- **Rigorous theoretical foundation.** Theorem 1 proves that anti-alignment (s = ⟨r_d, P r_s⟩ < 0) is sufficient for Neon to reduce the true-data risk. Theorem 2 proves that mode-seeking samplers (monotone reweighting of log p_θ) induce cos φ < 0, which guarantees anti-alignment near good models (Section 3.1). This formal justification — absent in prior self-training work — connects sampler properties directly to the success of gradient reversal.

- **Universality across four architecture families.** Neon is validated on diffusion (EDM), flow matching, autoregressive (xAR, VAR), and few-step (IMM) models (Sections 4.1–4.3). No prior self-improvement method achieves this breadth: DDO requires likelihoods (inapplicable to flow matching/IMM), Discriminator Guidance is diffusion-specific, and SIMS requires inference-time modifications.

- **Identifiable precision-recall mechanism.** Figure 4 shows that Neon monotonically decreases precision while raising recall along an inverted-U, with net FID improvement. The paper explains this as redistributing probability mass from over-represented to under-represented modes — a mechanism grounded in the theory and empirically verified, going beyond FID-only reporting.

- **Minimal data requirement and robustness.** As few as 1k synthetic samples suffice for near-optimal gains on xAR-L (FID 1.05 vs. 1.02 with 750k; Section 4.2). The method is robust to synthetic data quality (Figure 10: FID 1.30–1.31 for γ ∈ [1,3]), base model quality (Figure 9: compensates for 40% data reduction), and transfers across architectures (Figure 8: flow/IMM data improve EDM-VP).

## Weaknesses

### Major

- **Missing direct quantitative comparison with prior self-improvement methods on shared benchmarks.** The paper positions Neon against DDO, SIMS, Discriminator Guidance, and Self-Play FT, highlighting Neon's simplicity and generality. However, it provides no head-to-head FID table on a common setting (e.g., CIFAR-10 EDM-VP, where DDO reports FIDs ~1.4–1.5; or ImageNet-256 where SIMS/DDO have published results). A comparison table would let readers assess whether Neon is competitive, superior, or merely different — essential for substantiating the claim that Neon is "simpler and more general" without sacrificing performance. The SOTA claim for xAR-L on ImageNet-256 (Section 4.2) is well-supported against UCGM, but the broader positioning against self-improvement methods lacks quantitative backing.

### Minor

- **Anti-alignment (s < 0 and cos φ < 0) is never directly measured for real neural networks.** The paper proves this condition theoretically (Theorems 1–2) and provides substantial indirect evidence: the precision-recall trade-off (Figure 4), U-shaped FID curves, transferability across architectures (Figure 8), and the null result with CIFAR-10C (Section 4.4). However, a direct measurement — e.g., computing the cosine similarity between the synthetic fine-tuning gradient and a validation-set population gradient at the base checkpoint for one real model — would transform the anti-alignment claim from a plausible explanation into a verified mechanism. Without it, alternative explanations (e.g., implicit regularization from the merge) cannot be ruled out.

### Trivial

None.

## Nice-to-Haves

- **Ablate sensitivity to fine-tuning hyperparameters.** The paper uses reduced learning rate and brief fine-tuning but does not study sensitivity to the learning rate, number of steps, or optimizer choice for Neon. A brief ablation on one model would strengthen reproducibility guidance.
- **Show a clear failure case.** The paper mentions that diversity-seeking samplers (rare in practice) would require interpolation rather than extrapolation, but does not empirically demonstrate a scenario where Neon degrades performance. Reporting one such case would increase trust.
- **Direct gradient visualization in reduced-dimensional space.** Extending the 2D Gaussian toy (Figure 2) to a real model via PCA on parameter gradients would visually confirm the anti-alignment claim for actual neural networks.

## Removed Points

These points were flagged by reviewers but are removed from the main review with justification:

1. **"Joint tuning of w and γ introduces a confounding factor."** — The paper transparently discusses the interaction (Section 4.2, Figure 6), shows that independent γ optimization yields 3.01 FID while joint gives 2.01, and explains that w and γ have complementary precision-recall effects. Grid search over two scalars is trivially cheap. This is a feature, not a flaw.

2. **"Claim about no additional real data is slightly overstated."** — The paper claims "no additional real training data" (Section 1, contribution C1), which is literally true: Neon uses only synthetic data for fine-tuning. The compute overhead (<1%) is transparently reported. No overstatement exists.

3. **"Broader SOTA landscape (DiT, SiT, MDTv2) not discussed."** — These are different architectures. The SOTA claim is specifically for the xAR-L architecture pushed to 1.02 FID, benchmarked against UCGM's 1.06 on the same architecture family. This is appropriate scope.

4. **"Hyperparameters deferred to appendix."** — Standard practice for conference submissions; the appendix is stripped by the parser. Not a valid weakness.

5. **"Proofs rely on assumptions (first-order expansions, A-MONO)."** — The paper honestly states these assumptions (Section 3.1 footnotes, Appendix references). The critic does not identify a flaw in the proofs — only notes they exist. Not a substantive weakness.

6. **"Synthetic data generation requires compute."** — The paper never claims zero compute; it reports compute overhead (<1%) throughout and includes it transparently. This is a misreading.

## Novel Insights

None beyond the paper's own contributions. The core insight — that the predictable degradation from self-training on mode-seeking samplers is actually a structured, reversible signal — is the paper's primary novel contribution, and the reviews correctly identify it without adding new synthetic observations.

## Suggestions

- Add a table comparing Neon against DDO, SIMS, and Discriminator Guidance on at least one shared benchmark (e.g., CIFAR-10 EDM-VP and/or ImageNet-256 with a diffusion model). This single addition would address the most significant gap and substantially strengthen the positioning claims.
- Measure and report the cosine similarity between the synthetic fine-tuning gradient and an approximate population gradient (computed on a held-out real validation set) at the base checkpoint for one representative model (e.g., EDM-VP on CIFAR-10). This would elevate the theoretical mechanism from plausible to verified.

## Score and Decision

**Originality:** High. The idea of reversing self-training degradation via a simple parameter merge is novel and counterintuitive.

**Importance of question:** High. Improving generative models without additional real data addresses a fundamental bottleneck in scaling.

**Claims supported:** Mostly well-supported. The main gap is the absence of head-to-head comparisons with prior self-improvement methods.

**Soundness of experiments:** Good. Extensive evaluation across 4 architecture families, 3 datasets, with careful ablations (transfer, base quality, synthetic quality, null result). The theoretical analysis is rigorous.

**Clarity of writing:** Excellent. The paper is well-structured, clearly motivated, and the figures/visualizations are informative.

**Value to community:** High. The method's simplicity (post-hoc merge), universality (works across architectures), and minimal overhead make it immediately adoptable.

The paper presents a simple, elegant, and effective method whose empirical results are strong and consistent. The main weakness — missing direct comparisons with prior self-improvement methods — is a real gap that should be addressed, but it does not invalidate the core contribution. The method demonstrably works across diverse settings and achieves a new SOTA on ImageNet-256 with xAR-L.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>