## Summary

This paper introduces Spherical Watermark, a framework that embeds watermark bits into the initial Gaussian noise of diffusion models without per-image key storage. The method uses three modules: (1) a binary embedding module that mixes repeated watermark bits with random padding via an involutory matrix over $\mathbb{F}_2$ to produce 3-wise independent bits; (2) a spherical mapping module that normalizes to the unit sphere, applies a fixed orthogonal rotation, and scales by a chi-square-distributed radius; and (3) standard diffusion integration. The paper claims the resulting watermarked noise is statistically indistinguishable from standard Gaussian noise, eliminates the key-management overhead of Gaussian Shading, and achieves extraction times four orders of magnitude faster than PRC Watermark.

## Strengths

- **Practical elimination of per-image key storage.** The method uses a single fixed secret signature $K = \{\mathbf{T}, \mathbf{C}\}$ for all images, directly addressing the key-management overhead of Gaussian Shading and the cryptographic complexity of PRC. This is a genuine practical improvement.

- **Computational efficiency.** Embedding and extraction are roughly four orders of magnitude faster than PRC Watermark (Figure 4), with extraction requiring only matrix-vector multiplications and majority-vote decoding rather than belief propagation. This makes the scheme viable for large-scale deployment.

- **Strong empirical robustness.** Under adversarial attacks (WEvade), the method achieves TPR@1%FPR of 99.83% (Table 2), significantly outperforming lossy baselines and matching/exceeding PRC. It also maintains high accuracy far beyond PRC's capacity limit under JPEG-70 compression (Figure 6a). The ablation on modules (Figure 6b,c) convincingly demonstrates the necessity of both binary embedding and spherical mapping.

- **Generalizability across architectures.** The method is validated on SD v1.5, v2.1, v3, FLUX.1-DEV, pixel-space diffusion (G-Diffusion), and flow-based models (Glow), all with extraction accuracy above 98% (Appendix F.1, Tables 6, 7).

- **Rigorous analysis of rotation optimality.** Appendix D provides a formal argument that under an AWGN channel, the orthogonal rotation design achieves provably higher per-bit extraction accuracy than Gaussian Shading's truncated-sampling scheme, with Jensen's inequality establishing strict superiority.

## Weaknesses

### Major

- **Theoretical gap in the losslessness proof: a spherical 3‑design does not satisfy the requirement of Lemma 3.4.**  
  The paper's central argument is: $\mathbf{z}^{(2)}$ is a spherical 3‑design (Theorem 3.2) → rotation preserves this (Lemma 3.3) → scaling by $r \sim \chi(l_x)$ yields $\mathbf{z}_w$ distributed as $\mathcal{N}(\mathbf{0}, \mathbf{I}_{l_x})$ (Lemma 3.4).  
  **The gap:** Lemma 3.4's converse (product → Gaussian) requires $\mathbf{u}$ to be **exactly uniformly distributed** on the unit sphere. A spherical 3‑design matches moments only up to degree 3; it is *not* uniformly distributed. Lemma 3.4's condition is therefore unmet.  
  The paper states (line 349) that $\mathbf{z}_w$ "is distributed as $\mathcal{N}(\mathbf{0}, \mathbf{I}_{l_x})$," yet the proof only establishes (a) moment matching to degree 3, and (b) asymptotic convergence of marginal distributions as $l_x \to \infty$ via Stein's method (Lemma 3.3). The paper acknowledges higher-order moments "may deviate" in Section 5, which is in tension with the stronger claim made in Section 3.3. The central "losslessness" claim is thus **theoretically overstated**: what is actually proven is asymptotic Gaussianity of marginals plus third-order moment matching, not exact multivariate Gaussianity. This does not invalidate the method — the empirical evidence for practical indistinguishability is strong — but it means the theoretical guarantee is meaningfully weaker than advertised.

- **The "provable" claim is tied to an asymptotic ($l_x \to \infty$) CLT result, not a finite-sample guarantee.**  
  Lemma 3.3 uses Stein's method to show that $\sqrt{l_x} z_i^{(3)}$ converges in Wasserstein distance to $\mathcal{N}(0,1)$ at rate $O(l_x^{-1/2})$, treating the maximum dependency degree $D \le N + l_m - 1$ as constant. While the asymptotic bound is valid for the scaling regime where $l_x \to \infty$, the paper's experiments set $l_x = 16384$, $N=31$, $l_m=512$. The asymptotic argument is reasonable but does not provide a concrete finite-sample bound on the statistical distance between the constructed distribution and the true Gaussian. A bound expressed in terms of $l_x$, $N$, and $s$ would substantiate the "provable" claim.

### Minor

- **Undetectability analysis for fixed $\mathbf{m}$ is not explicit.** Theorem 3.1 assumes both $\mathbf{m}$ and padding $\mathbf{r}$ are random Bernoulli(1/2) bits. In deployment, each user has a fixed $\mathbf{m}$ and only $\mathbf{r}$ is freshly sampled. The paper never explicitly states that the 3-wise independence and uniform marginal properties hold conditionally on fixed $\mathbf{m}$. While this likely follows because each $\mathbf{z}_i^{(1)} = \text{(fixed combination of m bits)} \oplus \text{(random combination of r bits)}$ — and the XOR with a constant preserves the uniform Bernoulli distribution — a formal conditional analysis would strengthen the paper and close an important gap for the intended security model.

- **Empirical validation of undetectability could be more rigorous.** The paper trains binary classifiers (MLP on latents, ResNet-18 on images) and reports near-50% accuracy. While this is a reasonable approach for testing computational indistinguishability (consistent with Eq. 2), direct statistical tests on the $\mathbf{z}_w$ vectors (e.g., a two-sample MMD test with a characteristic kernel, or a multivariate normality test) would provide a more direct check. Given the theoretical gap discussed above, stronger empirical corroboration of the distributional claim would be valuable.

- **The dependency graph degree bound in Lemma 3.3 is not fully justified.** The proof states $D \le N + l_m - 1$ but does not derive this bound from the structural constraints of Algorithm 1. Since $N$ and $l_m$ are constants, the asymptotic conclusion is unaffected, but the reasoning is sketchy.

### Trivial

- Figure 4 uses a log-scale y-axis without reporting actual timing numbers in the text; providing the raw numbers would improve reproducibility.
- The paper uses $\approx$ (approximately) in the Lemma 3.4 description on line 406 but "distributed as" (exact) on line 349 — these should be reconciled.

## Nice-to-Haves

- A side-by-side comparison with Gaussian Shading using **per-image keys** (the original lossless configuration) would isolate the cost of avoiding key storage.
- Direct statistical tests on $\mathbf{z}_w$ (e.g., MMD with a Gaussian kernel, or a Henze-Zirkler multivariate normality test) would provide stronger empirical support for the distributional claim.
- A quantified bound on the total variation distance between the constructed distribution and $\mathcal{N}(\mathbf{0},\mathbf{I})$, expressed in terms of $l_x$, $N$, $s$, would substantiate the "provable" framing.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

1. **Criticism that "encryption-free is misleading."** The paper explicitly clarifies (lines 67–84) that it means "no per-image key," which is a truthful description. The critic's objection that secret parameters $\mathbf{T}$ and $\mathbf{C}$ are "functionally equivalent to a secret key" conflates a fixed system-level key with per-image key management — two very different things in practice.

2. **Criticism that the paper's undetectability evaluation "is too weak to substitute for the missing theoretical guarantee."** The paper defines undetectability as computational indistinguishability (Eq. 2), and binary classifiers (MLP, ResNet-18) are a standard approach to test this. Requesting Mardia's test or MMD is a reasonable suggestion but overshoots — the existing tests are not weak; they are appropriate given the paper's own security definition.

3. **Criticism that the fixed-$\mathbf{m}$ scenario invalidates the analysis.** As argued in Minor weakness 1, the construction with random $\mathbf{r}$ and the mixing matrix $\mathbf{T}$ preserves the Bernoulli(1/2) marginal property for each $\mathbf{z}_i^{(1)}$ even for fixed $\mathbf{m}$, because XOR with a constant preserves uniformity. The 3-wise independence also follows from the rank condition on $\mathbf{Q}$'s columns corresponding to $\mathbf{r}$. The critic's claim that the guarantee "does not extend to the realistic scenario" is overstated — the distributional claim in Theorem 3.1 holds for any fixed $\mathbf{m}$ whenever $\mathbf{r}$ is random.

4. **Criticism about unfair comparison with Gaussian Shading (fixed keys).** The paper explicitly notes (line 441, "Note that with fixed keys, Gaussian Shading no longer achieves true losslessness") and runs the standard evaluation used in prior work. The critic's request to "include the original Gaussian Shading with per-image keys" is a nice-to-have, not a flaw.

5. **Strength from Strength Finder claiming "rigorous foundation" of Lemma 3.4 proof.** This conflicts with the verified Major weakness and has been moved here.

## Novel Insights

The most interesting observation emerging from these reviews is the tension between the spherical 3‑design construction and the converse polar decomposition: the paper claims exact Gaussianity (via Lemma 3.4) but only establishes moment matching up to degree 3. The asymptotic CLT in Lemma 3.3 partially bridges this gap but does not yield a finite-sample statistical distance bound. This raises a subtle but important question for the lossless watermarking literature: can a practical construction using a low-degree spherical design actually achieve *computational* indistinguishability (as the empirical evidence suggests) even though it falls short of *statistical* equality? The paper's empirical results hint that it can, but a rigorous reduction — perhaps showing that distinguishing the 3‑design-based distribution from Gaussian requires detecting higher-order moment deviations, which may be computationally hard — would significantly strengthen the contribution.

## Suggestions

1. **Reconcile the strength of the theoretical claim with what is actually proven.** Replace claims of "distributed as $\mathcal{N}(\mathbf{0},\mathbf{I})$" with more precise language such as "matches moments up to degree 3 with asymptotically Gaussian marginals; empirical evidence supports computational indistinguishability." Explicitly bound the statistical distance or Wasserstein error in terms of $l_x, N, s$ for finite dimensions.

2. **Add a formal conditional analysis for fixed $\mathbf{m}$.** Show explicitly that when $\mathbf{m}$ is fixed and only $\mathbf{r}$ is random, each $\mathbf{z}_i^{(1)}$ is still $\text{Bernoulli}(1/2)$ and the 3‑wise independence holds.

3. **Report the raw timing values** (not just a log-scale bar chart) for embedding and extraction times to facilitate comparison.

4. **Add an MMD two-sample test** or a simple multivariate normality diagnostic on $\mathbf{z}_w$ vectors to complement the classifier-based undetectability evaluation.

## Score and Decision

**Score calibration against anchors:**

| Anchor Path | Avg Score | How it compares to this paper |
|---|---|---|
| `oTGJZtrprx.md` (Hiding in the Phase) | 5.00 | Similar domain (diffusion watermarking); comparable empirical breadth but the Spherical Watermark paper has a more serious theoretical gap. |
| `jvse9ZDuMC.md` (Cryptography in Semantic Watermarks) | 4.00 | Related topic (cryptographic flaws in semantic watermarks); the Spherical Watermark paper has greater practical contribution but a similar severity of theoretical overclaim. |
| `cNEshxVcWg.md` (NullGuard) | 3.00 | A watermarked paper with poor presentation; Spherical Watermark is substantially clearer and has stronger experiments. |
| `pAeEzS4LwS.md` (Catch-22) | 2.67 | A paper with fundamental misunderstandings; Spherical Watermark does not have such foundational errors. |
| `5ifzhjMCKq.md` (Guidance Watermarking) | 5.00 | Similar domain; both papers have clear contributions but the Spherical Watermark paper has a more impactful efficiency claim. |
| `DM0Y0oL33T.md` (Generative Universal Verifier) | 8.00 | Top-tier paper in a different area; not directly comparable in topic, but demonstrates the quality bar for high scores. |

**Reasoning:** The paper makes a genuine practical contribution — eliminating per-image key storage while maintaining strong robustness and achieving dramatically faster extraction than PRC. However, the central theoretical claim of "provable losslessness" is overstated: the proof contains a real gap (spherical 3‑design ≠ uniform distribution on the sphere, contravening Lemma 3.4's requirement). The paper's practical claims (efficiency, robustness, generalizability) are well-supported, but the theoretical overclaim is a significant flaw that prevents a higher score. Relative to the anchors, the paper sits between the 4.00 and 5.00 papers — better than NullGuard and Catch-22, comparable to Hiding in the Phase and the Guidance Watermarking paper, but below cryptographically rigorous work.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>