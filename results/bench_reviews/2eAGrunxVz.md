Now I have a thorough understanding of the paper and the calibration anchors. Let me synthesize the final review.

## Summary

Spherical Watermark introduces an encryption-free, lossless watermarking framework for diffusion models. The core idea is a three-stage pipeline — binary embedding (mixing watermark bits with random padding for 3-wise independence), spherical mapping (projecting onto the unit sphere via a spherical 3-design, applying orthogonal rotation, and scaling by chi-square radius), and diffusion integration — that maps binary watermarks into Gaussian-like noise without modifying the pretrained model. The method eliminates the per-image key storage burden of Gaussian Shading and the heavy cryptographic decoding of PRC Watermark, achieving orders-of-magnitude faster extraction while preserving visual fidelity and robustness under diverse attacks.

## Strengths

- **Clean, well-motivated design with theoretical grounding**: The binary embedding → spherical mapping → orthogonal rotation pipeline is elegant. Theorem 3.1 (3-wise independence), Theorem 3.2 (spherical 3-design), and the supporting lemmas form a coherent theoretical chain that explains why the watermarked noise approximates a standard Gaussian — up to third-order moments, as the paper honestly states in the abstract. The connection to spherical designs is a genuinely novel bridge between coding theory and lossless watermarking.

- **Convincing empirical undetectability**: FID scores match unwatermarked generations across SD v1.5/v2.1 and two prompt datasets (Table 1), while both MLP (latent-level) and ResNet-18 (image-level) classifiers fail to distinguish watermarked samples (Figure 2, ~50% accuracy). This is strong evidence that the watermarked noise passes standard distributional tests.

- **Strong adversarial robustness**: Under WEvade white-box/black-box attacks, the method retains bit accuracy >98% and TPR@1%FPR >99% (Table 2), whereas lossy baselines collapse. The theoretical justification in Appendix E (showing losslessness forces adversarial gradients to zero) is compelling and well-integrated with the empirical results.

- **Dramatic efficiency gains**: Extraction is approximately four orders of magnitude faster than PRC Watermark (Figure 4), confirming that eliminating belief-propagation decoding yields genuine practical benefits. This is not a minor speedup — it changes the deployability of lossless watermarking at scale.

- **Thorough ablation studies**: The modular ablations (Figure 6b,c) cleanly isolate the contributions of binary embedding (for undetectability) and spherical mapping (for robustness). Parameter sensitivity analysis (Figure 6d, Table 3) and ODE solver / timestep ablations (Tables 4-5) demonstrate that the method is not brittle to implementation choices.

- **Generalizability**: The method is validated beyond Stable Diffusion on SD v3, FLUX.1-DEV, pixel-space G-Diffusion, and Glow (Appendix F.1), confirming applicability to any generative model with a Gaussian prior and approximate inverse mapping.

## Weaknesses

### Major

- **Overstated undetectability claims in the introduction and conclusion**: The theoretical analysis proves that the watermarked noise matches the standard Gaussian only up to third-order moments (Theorems 3.1-3.2, Lemmas 3.3-3.4). Lemma 3.4 requires the direction to be *uniformly* distributed on the sphere for exact multivariate normality, but z^(3) is only a spherical 3-design — not uniform. The abstract correctly qualifies this ("up to third-order moments"), but the introduction (line 80: "statistically indistinguishable from standard Gaussian noise") and conclusion (line 1225: "provably and empirically indistinguishable") drop this qualification. The Discussion (§5) appropriately acknowledges that "higher-order moments may deviate from the true prior." The empirical evidence (FID, classifiers) is strong but does not rule out a polynomial-time adversary exploiting higher-order structure. The paper should consistently qualify the theoretical claim throughout and avoid the word "provably" in contexts that suggest full distributional equivalence. This is a real gap between what is proved and what is claimed, and it affects a central selling point of the paper. The practical results remain valuable regardless.

### Minor

- **AWGN optimality analysis is disconnected from the evaluated attacks**: Appendix D proves that the proposed rotation is optimal under an additive white Gaussian noise channel, but the attacks evaluated in §4.2 (JPEG, brightness, blur, resize, median filtering) are structured distortions, not AWGN. The ablation study (Figure 6c) empirically demonstrates the rotation helps, but the AWGN theory does not explain *why* it helps under these specific distortions. The paper would benefit from either (a) closing this gap analytically for a representative non-AWGN attack, or (b) framing the AWGN result as a motivating special case rather than a general optimality claim.

- **Undetectability evaluation uses only basic classifiers**: The latent-level MLP and image-level ResNet-18 are reasonable starting points, but a more sensitive detector — e.g., a likelihood-ratio test exploiting knowledge of the spherical 3-design construction — would provide stronger evidence that no polynomial-time adversary can distinguish the watermarked noise. Without this, the undetectability claim rests more on FID and simple classifiers than on a principled empirical stress test.

### Trivial

- The QR decomposition to obtain **C** yields a Haar-uniform orthogonal matrix when the initial matrix has i.i.d. Gaussian entries (Mezzadri 2006). The paper should cite or briefly note this property since Lemma 3.3 relies on properties of typical entries of such matrices. This is a one-sentence clarification.

- In Lemma 3.3's use of Stein's method, the dependency graph degree *D* should be explicitly computed or bounded for the default parameters to confirm the asymptotic argument applies at practical dimensions.

## Nice-to-Haves

- **Evaluate the original (lossless) Gaussian Shading with per-image keys** on the same undetectability metrics. The current comparison uses fixed-key Gaussian Shading (which the paper correctly notes no longer achieves losslessness). Showing that Spherical Watermark matches or exceeds the original per-image-key variant on FID and classifier accuracy would strengthen the claim that the spherical mapping achieves comparable undetectability without the key-management burden, isolating the contribution of the spherical design from the penalty of fixed keys.

- **Characterize the residual distributional gap** caused by using a spherical 3-design rather than a uniform direction (e.g., bound the KL divergence or total variation distance), allowing a quantitative assessment of what "up to third-order moments" means for practical indistinguishability.

- **Test a stronger detector** (e.g., a likelihood-ratio test based on the known spherical design) to probe whether the watermarked latent truly resists polynomial-time adversaries.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Comparison with Gaussian Shading is unfair to the original scheme"** — The harsh critic argued that comparing against fixed-key Gaussian Shading is unfair because the original scheme uses per-image nonces to preserve distributional indistinguishability. However, the paper explicitly notes this limitation (line 441: "Note that with fixed keys, Gaussian Shading no longer achieves true losslessness") and the comparison is practically motivated: per-image key storage is exactly the impracticality the paper aims to solve. Evaluating the degraded fixed-key variant is a fair comparison against what a practitioner would actually deploy. I have moved the suggestion to also evaluate the original per-image-key variant to "Nice-to-Haves."

- **Strength Finder's generic strengths** — The Strength Finder included some generic claims (e.g., "the paper addressed an important problem") without specific citations. These have been omitted or merged into specific, evidence-backed strengths above.

- **Human finder's similar weaknesses from other papers** — Not applicable; no unrelated weaknesses from other papers were raised in the inputs.

## Novel Insights

The wedding of spherical *t*-designs (a concept from algebraic combinatorics) with lossless watermarking is the paper's most original intellectual move. Prior lossless methods (Gaussian Shading, PRC) relied on cryptographic primitives (stream ciphers, pseudorandom codes) to achieve distributional indistinguishability. This paper shows that a purely combinatorial construction — binary embedding for 3-wise independence, projection to a spherical 3-design, orthogonal rotation — can achieve comparable empirical undetectability without any encryption. The insight that third-order moment matching is sufficient to fool standard distributional tests (FID, trained classifiers) under practical settings is valuable even though it falls short of full computational indistinguishability. The complementary theoretical result (Appendix E) that losslessness itself forces adversarial gradient energy to zero is also a crisp, general insight that transcends this specific construction.

## Suggestions

- Recalibrate the undetectability language in the introduction and conclusion. Replace "statistically indistinguishable" and "provably indistinguishable" with precise statements like "matches the target Gaussian up to third-order moments, and empirically passes standard distributional tests." The Discussion already contains the right language — propagate it forward.

- Add a brief computation showing that the dependency graph degree *D* in Lemma 3.3 is constant (or at least grows sub-linearly) under the default parameter settings, making the Stein's method argument transparent.

- Either connect the AWGN optimality analysis (Appendix D) to a representative non-AWGN attack, or reframe it explicitly as a tractable special case that motivates but does not fully explain the empirical robustness gains.

## Score and Decision

**Anchor comparison:**

- **`/home/wg25r/review_agent/human_reviews_2026/5ifzhjMCKq.md`** (Guidance Watermarking, avg 5.0, Accept Poster): Proposes guiding diffusion with gradients from pretrained watermark decoders. Novel but relies on existing decoders, adds hyperparameters, and is not lossless. Spherical Watermark is more self-contained, theoretically grounded, and lossless. **This paper is stronger.**

- **`/home/wg25r/review_agent/human_reviews_2026/oTGJZtrprx.md`** (PQIM, avg 5.0, Reject): Phase-based watermarking with provable robustness claims that were challenged as overclaimed. Similar pattern of theoretical claims not fully matching empirical breadth. Spherical Watermark has more comprehensive experiments and clearer methodology. **This paper is stronger.**

- **`/home/wg25r/review_agent/human_reviews_2026/3aBWTYGcaT.md`** (Watermarking Diffusion LMs, avg 5.0, Accept Poster): First watermark for diffusion language models; novel domain but more niche. **Comparable novelty, but Spherical Watermark has broader applicability.**

- **`/home/wg25r/review_agent/human_reviews_2026/cNEshxVcWg.md`** (NullGuard, avg 3.0, Withdrawn/Reject): Major writing quality issues, insufficient ablation. **This paper is significantly stronger.**

- **`/home/wg25r/review_agent/human_reviews_2026/8F9aMllvWm.md`** (DGS, avg 2.67, Withdrawn/Reject): Incremental extension of Gaussian Shading with limited novelty. **This paper is much stronger.**

Spherical Watermark is clearly above the 5.0-tier papers. It has a clean, novel methodology, comprehensive experiments, and genuine practical advantages (encryption-free, fast extraction). The one substantive weakness — overclaimed undetectability relative to what is proved — is real but confined to phrasing choices in the intro/conclusion and is fixable without changing the method or results. The paper's theoretical framework (spherical 3-design) and empirical results are solid. This places it in the 6.0-7.0 range. Given the strength of the practical results, the thorough ablations, and the genuine novelty of the spherical-design approach to lossless watermarking, I assign 6.5.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>