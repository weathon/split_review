Now let me finalize the review with proper calibration.

## Summary
This paper introduces **Spherical Watermark**, an encryption-free, lossless watermarking framework for diffusion models. The method embeds binary watermark bits by mixing them with random padding through a binary invertible matrix, then mapping the result onto the unit sphere via a 3-design construction, orthogonal rotation, and chi-square scaling to recover Gaussian noise. The framework eliminates per-image key storage and belief-propagation decoding, achieving extraction times four orders of magnitude faster than PRC Watermark while maintaining ~98-99% extraction accuracy under diverse attacks and matching unwatermarked FID scores.

## Strengths
- **Encryption-free architecture with extreme computational efficiency:** By replacing per-image stream ciphers and belief-propagation decoding with fixed binary matrix multiplication and orthogonal rotation (Eqs. 9–10), the method eliminates key storage overhead and reduces extraction latency by four orders of magnitude compared to PRC Watermark (Figure 4). This is a concrete, practically meaningful improvement.
- **Strong empirical undetectability and distribution preservation:** FID scores match the unwatermarked baseline (Table 1, differences within 0.1–0.5 variance range), and latent-level classifiers achieve near-chance accuracy (~50%) for distinguishing watermarked from unwatermarked samples (Figure 2). Image-level classifiers similarly fail to detect the watermark, consistent with theoretical moment-matching results.
- **Scalable capacity where baselines fail:** Figure 6(a) shows PRC Watermark completely degrades beyond l_m = 2000 bits under JPEG-70 compression, while Spherical Watermark sustains ~98%+ accuracy across the full capacity range. This is a substantively stronger result than the competing lossless method.
- **Robustness under diverse attacks:** Table 2 and Figure 5 show ~98% ACC under adversarial attacks, outperforming both lossy methods (which collapse to ~49-52%) and PRC Watermark (~95-97%). Ablations in Table 3 systematically characterize the sparsity/robustness tradeoff.

## Weaknesses

### Fatal
None.

### Major
- **Theoretical claims overstate what the mathematics delivers:** The abstract states "We theoretically prove that the watermarked noise distribution preserves the target prior up to third-order moments, and empirically demonstrate that it is statistically indistinguishable from a standard multivariate normal distribution." Lemma 3.3 only establishes asymptotic convergence as l_x → ∞, not finite-dimensional guarantees. The spherical 3-design matches moments only up to degree 3; higher-order moments (degree 4+) are uncontrolled. The authors themselves acknowledge this in Section 5: "higher-order moments may deviate from the true prior." This contradicts the "statistically indistinguishable" claim used to frame the core contribution. The cryptographically-styled undetectability definition (Eq. 2) is never actually proven — no reduction to hardness assumptions or distributional distance bounds with quantified ε are provided.

- **DDIM inversion error during extraction is not theoretically analyzed:** Extraction uses an empty prompt (∅) in the ODE solver (Eq. 12), while the original embedding uses the actual text prompt. DDIM inversion is inherently approximate, and inversion error constitutes an unmodeled perturbation of the watermarked latent. While majority-vote decoding empirically absorbs this error (Tables 2–5), Section 3.3's theoretical analysis covers only the forward embedding pass and never quantifies how inversion error degrades extraction accuracy. Bridging this gap would strengthen the claim of reliable extraction.

### Minor
- **Gaussian Shading baseline comparison uses a degraded operating point:** The paper acknowledges that Gaussian Shading "with fixed keys, no longer achieves true losslessness" (Section 4.1). Comparing Spherical Watermark (designed for fixed-key operation) against a lossy variant of Gaussian Shading (which is intended for per-image keys) is comparing different operating points. The paper should more clearly frame this comparison — e.g., "achieves comparable robustness to Gaussian Shading without per-image key storage."
- **The undetectability definition (Eq. 2) uses cryptographic terminology (computationally indistinguishable) without a computational hardness foundation:** No PPT adversary analysis is attempted. This is a notational overreach rather than a mathematical error, but it creates confusion about what is proven versus what is merely desirable.

## Nice-to-Haves
- Quantify the finite-dimensional approximation error ε between the watermarked noise distribution and the true Gaussian, as a function of l_x and design parameters (N, s). Even an empirical bound would make the theoretical contribution more precise and usable.
- Add controlled experiments measuring how inversion error scales with prompt mismatch, number of DDIM steps, and ODE solver, and how extraction accuracy degrades as a function of this error. This would empirically bridge the gap between the clean theoretical analysis and practical extraction.
- Discuss the threat model more explicitly: what happens if an adversary knows the signature K = (T, C)? Can targeted perturbations degrade extraction?

## Removed Points
The following points from the harsh critic were removed or demoted:
- **"The undetectability claim is structurally fatal"** — Demoted to Major. The gap between the 3-design approximation and full Gaussian indistinguishability is real, but the authors acknowledge it in Section 5, and the empirical evidence strongly supports practical indistinguishability. This undermines the framing but does not invalidate the method's empirical contribution.
- **"Extraction introduces systematic bias" as fatal** — Demoted to Major (inversion error is an analytical gap, not a method flaw). The majority-vote decoder's empirical absorption of inversion error is demonstrated, even if not theoretically modeled.
- **"Missing security analysis"** — Removed. The paper does acknowledge that stronger inversion-breaking attacks can compromise recovery (Section 5), and extensive adversarial attack experiments are presented (Table 2, Figure 5, WEvade attacks).
- **"The claim that lossless watermarking is inherently more robust lacks causal explanation"** — Removed as scope creep. The paper shows this empirically (Section 4.2) and references an appendix analysis; requiring causal theory for a property that is demonstrated empirically is beyond the stated scope.
- **"Gaussian Shading comparison is unfair/misleading"** — Softened. The paper does acknowledge the fixed-key limitation of Gaussian Shading and frames the comparison reasonably; calling it "a broken version of the baseline overstates the problem.

## Novel Insights
The harsh critic's observation that the cryptographic indistinguishability definition (Eq. 2) and the 3-design moment-matching analysis (Section 3.3) operate at fundamentally different levels of rigor — one computational, one distributional — highlights a broader tension in the watermarking literature: the gap between "undetectable" as a desirable property and "undetectable" as a mathematically provable guarantee. This paper's approach (3-design → approximate Gaussian) is a legitimate middle ground, but the paper should own it explicitly rather than letting the stronger vocabulary obscure the actual contribution.

## Suggestions
1. Replace "statistically indistinguishable" in the abstract and introduction with a more precise characterization, such as "matches the Gaussian prior up to third-order moments and is empirically indistinguishable at finite dimensions."
2. Add a brief quantitative analysis of DDIM inversion error: measure the ℓ2 distance between ground-truth and inverted latents under the empty-prompt condition, and correlate it with bit-level extraction accuracy.
3. Reframe the Gaussian Shading comparison to emphasize the practical advantage: Spherical Watermark achieves comparable robustness to per-image-key methods without per-image key storage.

## Score and Decision — Calibration

**Round 1 Bracketing:**
- Anchor `fkNsgI1nye.md` (3.00): Privacy-preserving diffusion inference — different topic, weak anchor.
- Anchor `jbfDg4DgAk.md` (3.00): LLM sparse watermarking — different modality, weak anchor.
- Anchor `vK8C37eHXM.md` (3.20): Diffusion + autoencoder compression — different topic.
- Anchor `hYEV8QmaOt.md` (3.40): Image anti-forensics — different topic.
- Anchor `HexshmBu0P.md` (5.33): Watermarking diffusion models recipe — training-based, less methodologically novel.
- Anchor `jlhBFm7T2J.md` (6.50): PRC watermark — most directly comparable; undetectable lossless watermarking for diffusion models.
- Anchor `T0ebbDO60R.md` (3.75): SuperMark — training-free but different approach.
- Anchor `ll2nz6qwRG.md` (5.83): WIND — two-stage watermarking, good but less comprehensive than this paper.
- Anchor `j7b4mm7Ec9.md` (7.60): Lightweight deep watermarking — different domain, not diffusion-specific.
- Anchor `84n3UwkH7b.md` (8.00): Detecting memorization in diffusion — different contribution type.

**Round 1 bracket: 5.5–7.5.** The paper is clearly stronger than the 5.33 anchor (HexshmBu0P) due to its methodological novelty and richer theoretical grounding. The key comparison is with the 6.50 PRC Watermark anchor (jlhBFm7T2J).

**Round 2 Narrowing:**
- `HexshmBu0P.md` (5.33): Training-based recipe paper, less novel and less rigorous than this paper. This paper is stronger.
- `ll2nz6qwRG.md` (5.83): WIND — good but less comprehensive evaluation and less theoretical depth. This paper is stronger.
- `jlhBFm7T2J.md` (6.50): PRC Watermark — the most comparable anchor. Spherical Watermark is **similar in methodology** (both lossless, both embedding into initial noise, both testing undetectability and robustness) but has:
  - *Stronger empirical results*: faster extraction (4 orders), better capacity scaling, better adversarial robustness.
  - *Weaker theoretical guarantees*: 3-design approximation vs. PRC's stronger cryptographic guarantees.
  - Overall: comparable to or slightly stronger than PRC Watermark, but the overclaimed theoretical framing pulls it back.
- `1IwoEFyErz.md` (6.00): Shallow Diffuse — training-free but with presentation issues and limited attack evaluation. This paper is stronger.
- `71pur4y8gs.md` (7.20): TabWak — first tabular diffusion watermark, solid theory and experiments, but different modality, less comparable. This paper's theoretical overclaim prevents it from reaching this tier.

**Comparison to Round 2 anchors:** This paper is stronger than the 5.33 and 5.83 anchors, roughly comparable to the 6.00 anchor (but with better experiments), and marginally comparable to the 6.50 PRC anchor — with better empirics but weaker theory. The gap between theoretical claims and actual proofs prevents reaching the 7+ band. 

The paper sits squarely between 6.0 and 6.5, leaning toward the upper end due to strong empirical results. I assign **6.5**, same as the PRC anchor, because the methodological contribution (encryption-free, faster, no per-image key) is genuinely meaningful, but the theory/experiment claim mismatch prevents going higher.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>