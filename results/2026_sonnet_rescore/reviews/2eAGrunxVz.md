## Summary

Spherical Watermark is an encryption-free, lossless watermarking framework for diffusion models that (1) mixes repeated watermark bits with random padding to form a 3-wise independent binary code, (2) projects this code onto the unit sphere via normalization and orthogonal rotation, and (3) scales by a chi-square-distributed radius to recover approximate Gaussian noise for use as the diffusion starting point. The method requires no per-image key storage, provides a moment-matching theoretical guarantee for undetectability, and demonstrates strong empirical performance in computational efficiency, adversarial robustness, and scalability with watermark capacity — outperforming the leading lossless competitor (PRC Watermark) on all three axes.

---

## Strengths

1. **Rigorous, layered theoretical analysis up to third-order moments**: Theorem 3.1 establishes 3-wise independence of z^(1), Theorem 3.2 proves z^(2) forms a spherical 3-design on S^{l_x−1}, Lemma 3.3 shows rotation preserves the 3-design property, and Lemma 3.4 provides the polar decomposition grounding. The abstract is honest: it claims preservation "up to third-order moments," and the Discussion (Section 5) acknowledges "higher-order moments may deviate from the true prior." The chain is coherent and self-consistent as stated.

2. **Strong empirical undetectability with concrete numbers**: Figure 2 shows classifiers trained on latent and image features achieve ~50% accuracy on the proposed method (indistinguishable from random chance), while Tree-Ring and fixed-key Gaussian Shading achieve 100% and 97%, respectively. Table 1 confirms FID of 48.1224 vs. original 48.1256 on COCO with SD v1.5 — essentially identical. PRC Watermark also passes these tests, so the comparison is well-calibrated.

3. **Compelling adversarial robustness with specific advantage**: Table 2 shows the proposed method achieves 99.83% TPR and 98.12% ACC under adversarial attack (WEvade), versus PRC Watermark's 95.38% TPR and 97.69% ACC. The 4+ percentage point advantage is explained theoretically (lossless methods provide no classifier foothold for adversarial gradients) and is independently motivated.

4. **~4-orders-of-magnitude extraction speedup over PRC**: Figure 4 on a log scale places extraction time at ~10^{−3.5} s vs. PRC's ~10^{1.0} s. The paper correctly attributes this to the elimination of belief-propagation decoding. Embedding time is also substantially lower than Gaussian Shading (~10^{−2.0} vs. ~10^{0.5} s).

5. **Validated modular design via ablation**: Figure 6(b) shows that omitting the binary embedding module makes the latent trivially distinguishable; Figure 6(c) shows that removing spherical mapping causes a dramatic robustness drop under brightness adjustment. Each module is verified to be necessary.

6. **Scalability advantage in watermark capacity**: Figure 6(a) demonstrates that PRC Watermark's accuracy collapses beyond l_m = 2000 bits under JPEG-70 compression, while Spherical Watermark sustains high detection rates through the full tested range (up to l_m = 512 with default N = 31, yielding l_{Nm} = 15872 effective dimensions).

7. **Robustness across ODE solvers and timestep schedules**: Tables 4–5 show that extraction accuracy under DDIM, PNDM, and DPM-Solver++ is essentially identical (e.g., 99.98% vs. 99.98% vs. 99.98% under PNG), and the method tolerates generation timesteps ranging from 10–50 steps without meaningful degradation.

---

## Weaknesses

### Fatal
None.

### Major

- **Formal security claim in Eq. 2 is overstated relative to the delivered proofs.** The definition of "Undetectability" in Eq. 2 uses full cryptographic computational indistinguishability language — "for any probabilistic polynomial-time adversary A, |Pr[A(z_w)=1] − Pr[A(z)=1]| ≤ negl(ρ)" — which requires hardness assumptions and an equivalence between the watermarked distribution and the Gaussian. What is actually proven is that z^(2) is a spherical 3-design (Theorem 3.2), and Lemma 3.4's converse ("if r² ~ χ²(n) and u is uniform on S^{n-1} and r ⊥ u, then ru ~ N(0, I)") requires a *truly* uniform u — but z^(3) = Cz^(2) is only a rotated 3-design, not truly uniform. The paper acknowledges this gap directly in Section 5 ("higher-order moments may deviate from the true prior") and the abstract is honest ("up to third-order moments"), but the gap between these hedged statements and the formal guarantee in Eq. 2 is substantial and should be resolved. The correct formal statement is: z_w is indistinguishable from N(0, I) by any polynomial test of degree ≤ 3. The cryptographic notation in Eq. 2 implies a hardness-based guarantee that is never formally derived. This is a presentation and framing mismatch that should be corrected in a revision.

### Minor

- **Gaussian Shading comparison framing could be clearer about the nature of its limitation.** The paper notes in Section 4.1 that "with fixed keys, Gaussian Shading no longer achieves true losslessness," which is accurate. But Figure 2 and Table 1 then present Gaussian Shading's 97–100% classifier accuracy and elevated FID as failures of undetectability, when the root cause is the key management limitation, not a fundamental flaw in the underlying mechanism. A clearer framing would state: Gaussian Shading achieves losslessness through per-image nonces, making it impractical in the fixed-key deployment scenario; the proposed paper solves the same problem without per-image keys. This is a contribution worth stating plainly rather than via an unflattering comparison.

- **No formal quantification of inversion error tolerance for majority voting.** Extraction in Eq. 13 applies C^{−1} to the noisy DDIM-inverted estimate ẑ_T and rounds coordinates. Robustness depends on inversion error being small enough that sign preservation under majority voting holds. Tables 4–5 provide strong empirical evidence (>99.8% accuracy across all solver/timestep configurations), but the paper never formally characterizes how much coordinate-level inversion error N=31 repetitions can absorb. A brief formal bound would close this gap and sharpen the contribution.

### Trivial

- **Notation inconsistency in Eq. 6**: the block dimension is written "l_m = N × l_m" in the equation label (line 84), which conflates the repeated message length with the original message length l_m. A clearer notation such as l_{Nm} = N × l_m (as used implicitly elsewhere in the paper) would prevent confusion.

- **Timing values in Figure 4 are log-scale approximations**: the table below the figure uses "~10^{-2.0}", "~10^{1.0}" etc. Exact timing values (e.g., in milliseconds) would make the efficiency claim more reproducible and precise, particularly since the ~4 orders of magnitude claim is a headline result.

---

## Nice-to-Haves

- A brief analysis of the API-level security scenario: because C is an orthogonal matrix and T is a fixed binary matrix, a sufficiently persistent adversary with many API queries might attempt to probe the signature K={T, C}. Even a qualitative argument that such an attack requires latent access (not provided by a black-box API) would strengthen the security framing.

- Quantifying the KL divergence or maximum moment deviation between z_w and N(0, I) as a function of l_x would replace the empirical 50% classifier accuracy argument with a tighter and more elegant theoretical closing of the undetectability guarantee.

- Expanding Figure 6(a) to a richer parameter sweep (jointly varying N, s, and l_m) would make the scalability advantage over PRC more compelling and give the paper a cleaner empirical identity around this finding, which is currently underemphasized.

---

## Removed Points

*These points are flagged to be removed, treat them with caution.*

- **Linear algebraic attack on C (from Harsh Critic's security model section)**: The critic argues that an adversary who can "query the API with known watermarks and observe the resulting latents" could recover C. This requires latent access, which is not possible through a black-box API. As the critic acknowledges, the feasibility "depends on whether the adversary can access latents (probably not)." This is speculative and should not be elevated to a confirmed weakness without evidence that latent access is realistic in the stated deployment model.

- **Timing values logged as "approximate" (from Harsh Critic)**: The critic calls this "circular." The paper is transparent that the y-axis is logarithmic and the values are read off the figure. Elevated to Trivial in the main review; removing the "circular" framing as it mischaracterizes the paper's intent.

- **Gaussian Shading "configured to fail" framing (from Harsh Critic)**: The critic states this "inflates the undetectability claim." This is retained as a Minor weakness on its own merits (the framing could be clearer), but the stronger "circular" and "inflate" language is removed. The paper explicitly discloses the fixed-key limitation, and the comparison is practically motivated.

- **Generic strengths from Strength Finder**: "This paper addressed an important problem" is generic and removed. Replaced by concrete grounded strengths above.

- **Appendix E proof reference (from Harsh Critic's theoretical discussion)**: The critic references "Appendix E" for a formal justification of losslessness under adversarial attack. Per review rules, appendix content is stripped from the parsed text and assumed to exist in the original; no criticism based on appendix absence is included.

---

## Novel Insights

The most structurally novel insight in the paper is the identification of spherical 3-designs as the right mathematical object for lossless watermarking: the Hamming hypercube, when normalized, already sits on the unit sphere in a configuration that matches the uniform spherical distribution up to third-order polynomials, and this approximation quality is the direct cause of why the method achieves near-perfect empirical undetectability at high dimension (l_x = 16384). The compactness of this correspondence — 3-wise independence of binary codes → 3rd-order moment matching on the sphere → approximate Gaussianity under chi-square scaling — is elegant and likely generalizable beyond the diffusion watermarking setting. The connection between the 3-design property and the adversarial robustness of lossless methods (established in Appendix E, referenced in the discussion) is also a meaningful theoretical observation that future work on watermarking could build on.

---

## Suggestions

1. **Replace Eq. 2's cryptographic notation with a statement matched to what is proven**: State the formal guarantee as "z_w is indistinguishable from N(0, I) by any statistical test of degree ≤ 3" and explicitly quantify as a function of l_x how much higher-order moments deviate. This makes the claim honest, precise, and more convincing than the current gap between negl(ρ) language and moment arguments.

2. **Reframe the Gaussian Shading comparison**: Lead with the framing that GS achieves losslessness through per-image nonces (its core mechanism), and use the fixed-key variant only to illustrate what happens in the specific deployment scenario (fixed key). This makes the proposed contribution clearer and avoids the appearance of testing a competitor in a configuration designed to highlight weaknesses.

3. **Add a formal bound on inversion error tolerance**: A brief argument quantifying how many coordinate sign-flip errors N=31 majority voting can absorb (in terms of maximum allowable fraction of corrupted coordinates) would strengthen the theoretical completeness of the extraction guarantee.

4. **Expand Figure 6(a)**: Report a joint sweep over N and l_m under JPEG-70 to fully characterize the capacity-robustness trade-off surface. This would make the scalability claim more quantitative and compelling.

---

## Evaluation

**Originality**: High. The spherical mapping approach — using the Hamming hypercube's normalization as a 3-design and combining it with chi-square scaling — is a clean, novel idea. The connection to spherical design theory as a tool for watermarking is original.

**Importance of research question**: High. Lossless, scalable, encryption-free watermarking for diffusion models addresses a pressing practical need for content provenance.

**Claims supported**: Mostly well-supported empirically. The theoretical framework is solid up to the Eq. 2 mismatch, which the paper partially acknowledges. Empirical evidence (Figures 2, 5, 6; Tables 1–5) is thorough and convincing.

**Soundness of experiments**: Strong. Two backbone models, two datasets, 100 users, five keys per run, ablations on all hyperparameters, three ODE solvers, 50 timestep configurations, and both post-processing and adversarial attacks are covered.

**Clarity of writing**: Good. The pipeline is clearly described, theoretical steps are well-motivated, and the limitations are honestly stated. The Eq. 2 framing issue and notation inconsistency are localized.

**Value to the research community**: High. The method is simple to implement, requires no retraining, eliminates per-image key management, and significantly outperforms the leading lossless method on efficiency and scalability. The open-source code (referenced but stripped from the parsed version) would make this directly usable.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>

<subscores>
<originality>4</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>4</soundness>
<clarity>4</clarity>
<community_value>4</community_value>
</subscores>