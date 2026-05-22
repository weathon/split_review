Now I have a thorough understanding of the paper and all the claims. Let me write the consolidated review.

## Summary

This paper introduces Spherical Watermark, an encryption-free lossless watermarking framework for diffusion models. The method converts binary watermark bits into Gaussian noise through three invertible modules: binary embedding (mixing watermark bits with random padding via an invertible matrix T), spherical mapping (projecting onto the unit sphere, applying orthogonal rotation C, and scaling by chi-square radius), and diffusion integration. The key insight is using spherical 3-design theory to show the resulting noise approximately matches a standard Gaussian, eliminating the per-image key storage overhead of prior lossless methods like Gaussian Shading while avoiding the heavy cryptographic decoding of PRC. Experiments on Stable Diffusion v1.5 and v2.1 show strong undetectability (near 50% classifier accuracy, matching FID), robustness under attacks (98.12% ACC under adversarial conditions), and four orders-of-magnitude faster extraction than PRC.

## Strengths

1. **Novel application of spherical t-design theory to watermarking.** The paper provides a formal connection between spherical 3-designs and lossless watermarking (Theorems 3.1–3.2, Lemmas 3.3–3.4). This is a genuinely new theoretical angle that goes beyond the cryptographic or repetition-code approaches of prior lossless methods. The proof that the binary code $\mathbf{z}^{(1)}$ is 3-wise independent (Theorem 3.1) and that $\mathbf{z}^{(2)}$ forms a spherical 3-design (Theorem 3.2) is a clean, theoretically grounded construction.

2. **Encryption-free design yields dramatic computational advantages.** Unlike Gaussian Shading (which requires unique key+nonce per image) and PRC (which requires heavy belief-propagation decoding), Spherical Watermark uses a single fixed signature $(\mathbf{T}, \mathbf{C})$. Figure 4 shows extraction time is roughly $10^{-3.5}$ seconds versus $10^1$ seconds for PRC — four orders of magnitude faster. This is a concrete, practically significant improvement.

3. **Empirically strong undetectability and robustness across multiple settings.** Table 2 shows that under adversarial attacks (WEvade), the method achieves 98.12% ACC and 99.83% TPR, outperforming PRC (97.69%/95.38%) while lossy methods collapse to near-chance. Table 1 shows FID matching the unwatermarked baseline. The classifier-based undetectability tests (Figure 2) show near-50% accuracy for both latent-level and image-level discrimination.

4. **Thorough ablation studies isolate module contributions.** Figure 6(b)–(c) demonstrates that omitting $\mathcal{B}$ makes the noise trivially distinguishable, while omitting $\mathcal{S}$ collapses robustness under brightness adjustment. Tables 3–5 systematically explore sensitivity to $s$, $N$, ODE solvers, and timesteps, showing the method is robust across a range of practical configurations.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **Theoretical guarantee is overstated in the abstract and conclusion.** The paper claims watermarked noise is "provably and empirically indistinguishable" from standard Gaussian (abstract, conclusion). However, the actual theoretical analysis shows only that $\mathbf{z}^{(2)}$ is a spherical 3-design (matching moments up to degree 3) and that marginal distributions converge as $l_x \to \infty$ (Lemma 3.3). Lemma 3.4's exact Gaussian result requires the direction vector to be *exactly* uniform on the sphere — which a 3-design is not. The paper acknowledges this gap in Section 5 ("higher-order moments may deviate"), but the abstract, introduction, and conclusion use much stronger language. The theoretical contribution would be better framed as "provably matching up to third-order moments with empirical evidence of full indistinguishability" rather than claiming the full distributional guarantee is proven.

2. **Statistical evaluation of undetectability could be more rigorous.** The undetectability evaluation relies on binary classifier accuracy (two-layer MLP and ResNet-18) and FID. While these are reasonable, standard distributional tests (e.g., marginal Kolmogorov-Smirnov tests, higher-moment comparisons like kurtosis, or a statistical distance estimate) would directly validate the "statistically indistinguishable" claim. The classifier test is also limited to a *fixed signature* setting; an adversary with access to multiple watermarked samples or who can vary the conditioning prompt might exploit higher-order structure not captured by the current tests.

3. **Comparison with Gaussian Shading's lossless variant is missing.** The paper compares against Gaussian Shading with *fixed keys* and transparently notes that "with fixed keys, Gaussian Shading no longer achieves true losslessness." However, the paper's core claim about undetectability would be strengthened by also comparing against the true lossless variant of Gaussian Shading (with per-image keys/nonces) to demonstrate that Spherical Watermark matches its undetectability while eliminating key storage. The current comparison makes the undetectability gap look larger than it would be against the proper lossless baseline.

4. **Inversion-free extraction not validated independently.** The extraction pipeline relies on DDIM inversion, which introduces noise. The paper's 99.99% clean accuracy shows robustness to this noise, but a clean sanity check (directly feeding $\hat{\mathbf{z}}_T = \mathbf{z}_w$ without inversion to verify the analytical extraction equations work as expected) would strengthen confidence in the extraction procedure, especially since the theoretical extraction equations involve an interesting interplay of chi-square scaling and rounding that is not entirely obvious from the exposition alone.

### Trivial
- The computational efficiency comparison (Figure 4) shows only the watermark-to-noise transform time, explicitly excluding diffusion inversion/sampling. This is reasonable but the caption and text could more prominently state what is and isn't included to avoid misinterpretation.
- The logarithmic y-axis labels in Figure 4 use notation like "$10^{-3.5}$" — this is a minor presentation issue.

## Nice-to-Haves
- A direct statistical distance estimate (e.g., total variation bound or maximum mean discrepancy) between the watermarked and true Gaussian distributions for the finite $l_x = 16384$ setting would calibrate the strength of the undetectability guarantee.
- An open-source release of the code would aid reproducibility and allow the community to verify the extraction procedure independently.

## Removed Points

- **Issue 1 from harsh critic ("extraction is mathematically invalid"):** REMOVED. The critic claims $\hat{\mathbf{z}}^{(2)} = r \mathbf{z}^{(2)}$ has entries "on the order of $\pm 128$" making the rounding operation fail. This is factually incorrect. The paper clearly states $\mathbf{z}^{(2)} = \mathbf{v} / \|\mathbf{v}\|_2$ (Eq. 10) where $\|\mathbf{v}\|_2 = \sqrt{l_x}$, so entries of $\mathbf{z}^{(2)}$ are $\pm 1/\sqrt{l_x}$. Then $r\mathbf{z}^{(2)}$ has entries $\pm r/\sqrt{l_x} \approx \pm 1$ (since $\mathbb{E}[r] \approx \sqrt{l_x}$ for $l_x = 16384$). Rounding $(\pm 1 + 1)/2$ yields exactly $\{0, 1\}$. The extraction pipeline as described in Eq. 13 is mathematically sound. This point must be removed because it misreads the normalization step in the paper. *(Note: the paper could still benefit from a brief clarifying sentence that $r/\sqrt{l_x} \approx 1$ makes the rounding work, but the described procedure is correct as written.)*

- **Criticism about missing code/reproducibility (harsh critic's "without code, this is unverifiable"):** REMOVED per rules — code release is not required for review and this constitutes a reproducibility nitpick.

- **Criticism about missing comparison with RingID, SEAL:** REMOVED per rules — the paper explicitly scopes to lossless methods and these are lossy/detection-only methods; the critic acknowledges this is "acceptable" but still lists it as a weakness.

- **Strength Finder's claim that the paper provides "stronger formal guarantee than prior lossless methods":** REMOVED — Gaussian Shading provides an *exact* Gaussian guarantee (exact losslessness) while this paper provides an approximate guarantee (3-design). Claiming it's "stronger" is inaccurate; the contribution is different (encryption-free, not stronger per se).

- **Criticism about missing the cost of diffusion inversion in time comparison:** REMOVED — the paper explicitly states it evaluates "exclusively the transformation between the watermark and its latent noise representation, excluding any diffusion sampling or inversion procedures." The comparison is transparent.

- **Nitpicks about proofs being in appendix, missing appendix content:** REMOVED per rules — the parser strips these sections.

## Novel Insights

The two reviews, taken together, expose an interesting tension: the harsh critic's central "fatal" claim about extraction invalidity turns out to be a straightforward mathematical error (failing to account for the $\|\mathbf{v}\|_2$ normalization in $\mathbf{z}^{(2)}$), while the genuinely substantive concern — that the theoretical guarantee is limited to third-order moments and the paper's strong language overstates it — is acknowledged by both the paper's own limitations section and the reviewer. This suggests that the paper's weakest point is not about correctness but about calibration between its theoretical results and their presentation. The extraction procedure is structurally valid; the remaining concerns are about precision of claims and completeness of statistical validation, both addressable in a revision.

## Suggestions

1. **Rephrase theoretical claims for precision.** Replace "provably and empirically indistinguishable" with "provably matching up to third-order moments with strong empirical evidence of full indistinguishability" throughout the abstract, introduction, and conclusion. This would accurately reflect what is proven and what is empirically observed.

2. **Add simple statistical tests** (e.g., marginal KS tests, fourth-moment comparisons) to directly quantify how close the watermarked noise is to $\mathcal{N}(0, I)$ in distribution, rather than relying solely on classifier-based tests.

3. **Include the lossless Gaussian Shading variant** (with per-image keys) as a baseline for undetectability to demonstrate that Spherical Watermark matches it while eliminating key storage. Alternatively, clearly state that GS with per-image keys achieves similar undetectability but incurs storage overhead (the current comparison with fixed-key GS is fair but incomplete).

4. **Add a clarifying sentence** in Section 3.2 noting that because $\mathbb{E}[r] \approx \sqrt{l_x}$, the quantity $r\mathbf{z}^{(2)}$ has entries approximately $\pm 1$, making the rounding operation $\text{round}((\cdot + 1)/2)$ in Eq. 13 well-defined. This would preempt the confusion exhibited in the review.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>