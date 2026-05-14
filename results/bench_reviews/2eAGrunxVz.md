Now I have thoroughly read the paper. Let me synthesize the final review.

---

## Summary

This paper introduces Spherical Watermark, an encryption-free watermarking framework for diffusion models that converts binary watermark bits into Gaussian-like noise via a binary embedding matrix and a spherical mapping (projection onto the unit sphere, orthogonal rotation, and chi-square radius scaling). The method requires no per-image key storage, achieves extraction speeds roughly four orders of magnitude faster than PRC Watermark, and empirically matches unwatermarked image quality (FID) while maintaining robust watermark extraction under diverse post-processing and adversarial attacks.

## Strengths

- **Novel algorithmic contribution.** The use of a spherical 3-design — constructed from a 3-wise independent binary code projected onto the unit sphere — as the core mechanism for lossless-to-the-eye watermarking is genuinely clever and well-motivated. The three-stage pipeline (binary embedding → spherical mapping → diffusion integration) is clean and principled (Section 3.2).

- **Dramatic computational efficiency gain.** Extraction is approximately four orders of magnitude faster than PRC Watermark (Figure 4), enabled by the encryption-free design that replaces belief-propagation decoding with simple matrix inversion, rounding, and majority voting. This is a concrete, well-measured practical advantage.

- **Strong and broad empirical evaluation.** The paper evaluates on two Stable Diffusion versions, two prompt datasets (COCO, SDP), and multiple distortion types (JPEG, Gaussian blur, brightness, Gaussian noise, drop, resize, adversarial WEvade attacks). FID scores are essentially identical to the unwatermarked baseline (Table 1: e.g., 48.12 vs. 48.13), classifiers achieve near-chance accuracy (Figure 2), and tracing accuracy exceeds 95% under post-processing (Table 2). Generalization is shown across SD v3, FLUX.1-DEV, pixel-space G-Diffusion, and Glow (Appendix F.1).

- **Honest limitations section.** Section 5 explicitly acknowledges that "higher-order moments may deviate from the true prior" and that the Gaussian guarantee depends on the spherical 3-design definition. This honest self-assessment strengthens the paper's credibility.

- **Well-executed ablation studies.** Removing the binary embedding module makes the latent trivially distinguishable; removing spherical mapping degrades robustness under brightness adjustment (Figures 6b, 6c). Parameter sweeps over sparsity _s_ and repetition _N_ (Tables 15–17) clearly show the robustness–undetectability trade-off.

## Weaknesses

### Major

- **Theoretical overstatement of "provable indistinguishability."** The conclusion states that watermarked latents are "provably and empirically indistinguishable from a standard Gaussian prior." The theory proves: (i) z^(1) is 2-wise and 3-wise independent (Theorem 3.1); (ii) z^(2) is a spherical 3-design (Theorem 3.2); (iii) marginals of z^(3) converge to N(0, 1/lx) as lx→∞ (Lemma 3.3); (iv) if u is uniformly distributed on the sphere, then r·u ∼ N(0,I) (Lemma 3.4). However, the crucial logical link is missing: z^(3) is a spherical 3-design, **not** uniformly distributed on the sphere, so the converse of Lemma 3.4 does not apply to the actual construction. A 3-design matches the uniform distribution only up to polynomial degree 3 — this does not imply full distributional equivalence or computational indistinguishability. The paper acknowledges this honestly in Section 5 ("higher-order moments may deviate from the true prior"), but the abstract and conclusion overstate what was proved. The paper should either (a) provide a bound on the KL divergence or total variation distance between the actual distribution and N(0,I) as a function of lx, or (b) reframe the claim as "provably matches the Gaussian prior up to third-order moments" rather than full indistinguishability. In its current form, this is a genuine gap between the headline claim and the supporting mathematics.

### Minor

- **PRC Watermark comparison uses default parameters only.** The paper attributes PRC Watermark's lower accuracy and higher latency to inherent limitations (code-rate tuning, error floor), and all experiments use default PRC settings. While using defaults is standard practice and the efficiency comparison is clearly unfair in the opposite direction (favoring PRC, not the authors), it would strengthen the paper to discuss whether PRC's performance could be improved with tuned parameters or to justify why the default configuration is representative. As it stands, the robustness comparison overstates the authors' advantage slightly.

### Trivial

- The term "encryption-free" is slightly imprecise since the scheme does rely on a fixed secret key (T, C) whose confidentiality is essential. The intended contrast (no stream cipher, no PRC, no cryptographic primitives) is clear from context, but a more precise term like "cryptography-free" or "non-cryptographic" would avoid confusion.

## Nice-to-Haves

- A bound on the total variation or KL divergence between the actual watermarked distribution and N(0,I) as a function of lx would significantly strengthen the theoretical contribution and close the gap between the 3-design guarantee and the losslessness claim.

- A kernel two-sample test (e.g., MMD) on watermarked vs. clean latent vectors would complement the classifier-based undetectability evaluation. While the classifier tests and FID are standard in this literature, an MMD test would provide a more rigorous statistical complement, particularly given the paper's emphasis on distributional indistinguishability.

- A discussion of the security implications of key compromise (T, C) would strengthen the practical analysis, as the fixed-key design means that key exposure would allow an adversary to both forge and remove watermarks for all past and future images.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"FID error bars are large and all methods overlap, so FID provides no evidence of undetectability"** — This misreads the data. The means show clear separation: the proposed method (48.12) and PRC (48.13) sit at the original (48.13), while Gaussian Shading with fixed keys (50.70) and Tree-Ring (49.33) are 0.5–2.5 points higher. This is strong supporting evidence.

- **"The claim that Spherical Watermark 'delivers superior robustness' is not fully substantiated because PRC was not tuned"** — The comparison asymmetry favors PRC (the baseline), not the authors' method. Using default settings for a published method is standard practice. This is downgraded to a Minor weakness above.

- **"Encryption-free is misleading — it's a symmetric-key scheme"** — The term "encryption-free" refers to the absence of cryptographic primitives (stream cipher, PRC, belief-propagation decoding), not the absence of any secret. The intent is clear. Downgraded to Trivial.

- **Strength Finder claim about "rigorous theoretical guarantee of distributional indistinguishability"** — This is the same overstatement flagged in the Major weakness. The theory proves moment-matching up to degree 3, not full distributional equivalence.

- **Strength Finder claim that "the paper addressed an important problem" or "targeted an interesting question"** — Generic, superficial strength removed.

- **Demand for MMD tests and higher-order cumulant analysis as essential for acceptance** — While useful, these are not standard requirements in the diffusion watermarking literature (Gaussian Shading and PRC Watermark also do not provide them). Moved to Nice-to-Haves.

## Novel Insights

The paper's most interesting insight — not fully developed but substantial — is that a spherical 3-design, constructed from a simple 3-wise independent binary code, is sufficient in practice to produce watermarked latent codes that are undetectable by standard classifiers and preserve FID. This suggests that full distributional equivalence may be unnecessary for practical lossless watermarking, and that moment-matching up to low orders captures what matters for perceptual quality and detection resistance. The proof in Appendix D that the orthogonal rotation is provably optimal among binary mappings under AWGN (maximizing symbol separation) is also a clean, self-contained contribution.

## Suggestions

1. **Soften the theoretical claim in the abstract and conclusion.** Replace "provably and empirically indistinguishable" with "provably matches the Gaussian prior up to third-order moments and is empirically indistinguishable." This is accurate, still strong, and removes the gap between claim and proof.

2. **Add a bound on the distributional distance.** Even a simple analysis of the 4th-order moment mismatch as a function of lx would help readers understand how quickly the approximation improves with dimension and would partially close the theoretical gap.

3. **Clarify the "encryption-free" terminology.** Either define it precisely (e.g., "requiring no cryptographic operations beyond a fixed matrix multiplication") or replace it with a more precise term.

4. **Discuss PRC parameter tuning.** A brief paragraph acknowledging whether PRC's default parameters are representative or whether tuning could close the robustness gap would preempt reader concerns.

---

**Anchor comparison:**

| Anchor Paper | Path | Avg Score | Comparison |
|---|---|---|---|
| Hiding in the Phase (PQIM) | `oTGJZtrprx.md` | 5.00 (Reject) | PQIM had contradictory results, missing formal guarantees, and presentation problems. Spherical Watermark has cleaner methodology, stronger efficiency gains, and better empirical support. |
| Guidance Watermarking | `5ifzhjMCKq.md` | 5.00 (Accept) | Guidance Watermarking requires a pretrained decoder and has significant computational overhead. Spherical Watermark is training-free and far more efficient. |
| SERUM | `AiBUm6iKBf.md` | 5.00 (Accept) | SERUM adds watermark noise and trains a detector. Spherical Watermark's spherical-design approach is more principled and achieves lossless embedding without training. |
| Watermarking Diffusion LMs | `3aBWTYGcaT.md` | 5.00 (Accept) | Different domain (language models), comparable contribution level. Spherical Watermark has stronger efficiency results. |
| Dataset Watermarking Benchmark | `rjhF7b7n6g.md` | 3.00 (Reject) | That paper had factual errors, questionable results, and missing baselines. Spherical Watermark is clearly far stronger. |
| DMark (dLLMs) | `VCYDbyV5WY.md` | 3.00 (Reject) | Different domain, weaker contribution. Spherical Watermark is substantially stronger. |

The paper is clearly above the 5.0-band anchors in methodological novelty, empirical thoroughness, and practical impact. The theoretical overstatement in the conclusion is the main weakness but does not undermine the core contribution, and the paper honestly acknowledges the limitation in Section 5. I assign a score of **6.0**.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>