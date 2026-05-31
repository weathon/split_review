Good. Now let me run the calibration search.Now let me read the two most relevant middle-band anchors in full.Now let me narrow within the 5.5–7.0 range.Now I have sufficient information to write the final review.

---

## Summary

Spherical Watermark proposes an encryption-free, lossless watermarking framework for diffusion models. It converts binary watermark bits into standard Gaussian noise via three reversible steps: (1) a binary embedding module that uses 3-wise independent mixing to produce a high-entropy code, (2) a spherical mapping module that normalizes to the unit sphere, applies an orthogonal rotation, and scales by a chi-square-distributed radius, and (3) standard diffusion integration. The key contributions are theoretical guarantees that the watermarked noise matches the Gaussian prior up to third-order moments (spherical 3-design), elimination of per-image key storage, and a ~10,000× extraction speedup over the nearest lossless competitor (PRC Watermark), with improved robustness under adversarial attacks and superior watermark capacity scaling.

---

## Strengths

- **Complete modular theoretical chain**: Theorem 3.1 establishes 3-wise independence of z^(1), Theorem 3.2 proves z^(2) is a spherical 3-design, Lemma 3.3 shows orthogonal rotation preserves the 3-design property, and Lemma 3.4 is invoked to complete the Gaussian approximation. This provides a rigorous (if degree-bounded) characterization of the watermarked noise distribution.

- **Empirically confirmed undetectability**: Figure 2 shows that classifiers trained on both latent-level (MLP) and image-level (ResNet-18) features achieve ~50% accuracy on the proposed method—indistinguishable from random guessing. Table 1 shows FID values (e.g., 48.1224 vs. 48.1256 baseline on COCO with SD v1.5) are statistically indistinguishable from the unwatermarked baseline. This directly supports the distributional preservation claim.

- **Substantial computational advantage**: Figure 4 (log-scale) shows extraction time of ~10^{-3.5}s vs. ~10^1s for PRC Watermark—roughly four orders of magnitude—attributable directly to the elimination of belief-propagation decoding.

- **Superior adversarial robustness and capacity scaling**: Table 2 shows 99.83% TPR under adversarial attack (WEvade) vs. 95.38% for PRC Watermark. Figure 6(a) shows PRC Watermark fails entirely above l_m = 2000 bits while Spherical Watermark sustains high accuracy at all tested capacities.

- **Well-designed ablation studies**: Figures 6(b–c) confirm that binary embedding (3-wise independence) and spherical mapping are both necessary — removing either causes either detectability or robustness collapse. Table 3 shows predictable and interpretable tradeoffs from varying sparsity s and repetition N. Tables 4–5 confirm insensitivity to ODE solver choice and timestep count.

---

## Weaknesses

### Fatal
None.

### Major

- **Gap between the stated formal security guarantee and the delivered theoretical result**: Equation 2 uses cryptographic computational indistinguishability notation — "for any probabilistic polynomial-time adversary A, |Pr[A(z_w)=1] − Pr[A(z)=1]| ≤ negl(ρ)" — which implies a hard-complexity-theoretic guarantee. The actual theoretical results deliver only a spherical 3-design, i.e., moment matching up to degree 3. Lemma 3.4 establishes that *exact* Gaussian recovery requires *truly* uniform angular distribution, but z^(2) is not truly uniform — it is a discrete distribution on the 2^{l_x} vertices of the rescaled Hamming hypercube (each coordinate is ±1/√l_x). The paper's Discussion section honestly acknowledges that "higher-order moments may deviate from the true prior," but this contradicts the formal claim in Eq. 2. The bridge from "3-design" to "negl(ρ) computational indistinguishability" is never established. This is a presentation and framing mismatch rather than a flaw in the underlying method (empirical evidence at l_x=16384 is compelling), but stating Eq. 2 as a delivered theorem-backed guarantee is not accurate as written. The paper should reframe its formal claim to honestly reflect what is proven: indistinguishability by any degree-≤3 polynomial test, with the large-dimensional regime making higher-order deviations empirically negligible.

### Minor

- **Slightly misleading framing of the Gaussian Shading comparison**: Section 4.1 notes that "with fixed keys, Gaussian Shading no longer achieves true losslessness," and Figure 2 then shows Gaussian Shading achieving 97–100% classifier accuracy. This framing conflates a key-management limitation (the fixed-key variant is impaired by design) with a fundamental undetectability failure. The correct framing is: Gaussian Shading's original design is lossless by construction but requires per-image keys; the fixed-key setting is simply outside its design envelope. This should be stated more clearly so that the proposed method's advantage (achieving losslessness *without* per-image keys) is correctly attributed. The comparison with PRC Watermark — which genuinely targets the fixed-key setting — is the fair peer comparison, and those results are strong enough to stand on their own.

- **Fixed-key security analysis is absent**: Since the signature K = {T, C} is fixed across all generated images, an adversary who can obtain multiple (watermark input, image) pairs via API queries could in principle attempt to recover K. The paper does not analyze whether recovery of C from observable data is feasible or infeasible. Even a brief argument (e.g., latent access is required but not available via black-box API, making the attack infeasible) would close this gap.

### Trivial

- Equation 6 uses l_m = N × l_m as the label for the row dimension of T, which is inconsistent notation (l_m should be l_{Nm} or l_{N·m} to distinguish the repeated message length from the original message length l_m). This notation ambiguity appears without consequence to reproducibility since the method is well-described elsewhere, but it should be corrected for clarity.

---

## Nice-to-Haves

- A quantitative bound on KL divergence or maximum moment deviation between the watermarked noise and the true Gaussian as a function of l_x would substantially strengthen the theoretical contribution and replace the current informal appeal to "large dimensionality makes deviations negligible."
- The capacity–robustness tradeoff in Figure 6(a) is among the most compelling empirical results in the paper and is relatively underemphasized in the discussion. A richer sweep varying N and s jointly with l_m would make the scalability claim stronger and provide clearer design guidance.
- Analysis of the inversion error tolerance: since extraction relies on sign preservation through noisy DDIM inversion, a brief characterization of how many coordinate sign flips the N=31 majority vote can absorb would clarify the robustness margin.

---

## Removed Points

*These points are flagged as removed — treat with caution.*

- **"Algorithm 1 has R indexed as 3D but reshaped on return" (Harsh Critic)**: Verified against the paper. Algorithm 1 line 1 initializes R as N × l_m × l_r, with line 12 returning Reshape(R, (l_m, l_r)). This is a valid observation about the reshape but is a trivial implementation detail that does not affect correctness or reproducibility. Removed per trivial/formatting rule.

- **"Computational efficiency uses log-scale approximations rather than exact numbers" (Harsh Critic)**: The paper states Figure 4 uses "a logarithmic scale on the y-axis for visualization" and provides a table of approximate values. Requesting exact timing numbers is a minor reproducibility concern, not a methodological flaw. This is a trivial presentation preference, not a weakness that threatens any claim. Removed per trivial rule.

- **"Strength: Lemma 3.4 recovers exact multivariate Gaussian noise" (Strength Finder)**: The abstract says "scales by a chi-square-distributed radius to recover exact multivariate Gaussian noise" — but as established, the recovery is only exact when the angular component is truly uniform, which z^(2) is not. This specific phrasing of the strength (exactness) is contradicted by the verified Major weakness. Removed per the rule that weaknesses win over conflicting strengths.

- **"Fixed-key adversarial recovery from linear algebra is fatal" (Harsh Critic)**: Demoted to Minor. The harsh critic frames this as a fatal gap, but feasibility depends entirely on latent access (unavailable via black-box API), making the threat speculative rather than demonstrated. The concern is real but not fatal.

---

## Novel Insights

The paper's most insightful observation — implicit in the construction but underemphasized — is that the key architectural obstacle separating "lossless" from "encryption-free lossless" watermarking is the need for injected randomness to vary per-image. By introducing fresh random padding r at each invocation while keeping the signature K fixed, Spherical Watermark threads this needle: the per-image randomness comes from r (which is discarded after embedding, since it occupies the padding region of x and is not needed for extraction), while K provides the deterministic structure needed for key-free extraction. This decomposition of "randomness for losslessness" from "secret key for security" is the conceptual core of the design and deserves more explicit emphasis. It also clarifies why the capacity–robustness tradeoff behaves as it does: increasing l_m directly competes with l_r for the fixed budget l_x, reducing the entropy available to mask watermark structure.

---

## Suggestions

1. **Reframe Eq. 2 and surrounding claims**: Replace the cryptographic negl(ρ) formalism with an honest moment-matching statement: "the watermarked noise is indistinguishable from Gaussian by any statistical test of degree ≤ 3, and we provide empirical evidence that higher-order deviations are negligible at l_x = 16384." Then either prove the cryptographic claim rigorously or remove it.

2. **Reframe Gaussian Shading comparison**: Clearly distinguish between Gaussian Shading's key-management limitation (which causes its fixed-key variant to be impaired) and a fundamental undetectability failure. Present the method's contribution as: achieving losslessness *without* per-image key management, rather than as outperforming Gaussian Shading on undetectability per se.

3. **Add a fixed-key attack discussion**: Include at minimum a paragraph in Section 5 arguing why recovery of K from API observations is infeasible (e.g., latent codes are inaccessible, the mapping from binary watermarks to final images goes through stochastic diffusion, etc.).

4. **Fix the notation inconsistency in Eq. 6**: Rename the row dimension of T to l_{Nm} = N × l_m to distinguish it from the scalar l_m.

---

## Score and Decision

**Axes:**
- *Originality*: High. The spherical 3-design framing for lossless watermarking is novel and clean. The insight that random padding per-invocation can serve as the entropy source while signature remains fixed is genuinely new.
- *Importance of research question*: High. Provenance tracking for AI-generated content is a pressing practical problem, and the per-image key management burden of prior lossless methods was a genuine barrier to deployment.
- *Claims well-supported*: Mostly yes. Empirical evidence is strong and multi-faceted. The main gap is between the formal claim in Eq. 2 and what is actually proved — a real but bounded presentation issue.
- *Soundness of experiments*: Strong. Two backbone models, two datasets, five runs per metric, comprehensive ablations on modules, parameters, solvers, and timesteps, plus comparison across six baselines.
- *Clarity of writing*: Good overall, with two localized clarity issues (Gaussian Shading framing, Eq. 2 formalism).
- *Value to research community*: High. The method is simple, fast, and practically deployable.

**Calibration anchors:**
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/jlhBFm7T2J.md` (avg 6.5, Round 1) — PRC Watermark, accepted. Spherical Watermark directly improves upon this paper in practical dimensions (10000× faster, no per-image keys, better robustness under adversarial attack, better capacity scaling). However, PRC has genuine cryptographic guarantees while Spherical has only the 3-design; this is a tradeoff that roughly balances.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ll2nz6qwRG.md` (avg 5.83, Round 1) — WIND watermarking, accepted. Spherical Watermark is clearly stronger: richer theory, more comprehensive evaluation, more significant practical gains.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/1IwoEFyErz.md` (avg 6.0, Round 2) — Shallow Diffuse, rejected. Comparable scope to Spherical Watermark but thinner theory and narrower experimental evaluation. Spherical Watermark is clearly better.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/mDKxlfraAn.md` (avg 6.4, Round 2) — Watermark removal paper, accepted. Different angle (attack vs. defense) but comparable rigor and practical relevance.

**Round 1 bracket**: 5.5–7.0

**Narrowing**: The paper is clearly stronger than the 5.83 WIND anchor (richer theory, better experiments) and comparable to or slightly better than the PRC anchor (6.5) that it improves upon, though the formal theoretical gap (Eq. 2 vs. 3-design) is a real penalty relative to PRC's clean cryptographic guarantee. Positioning at 6.5, matching the PRC paper, is appropriate: the practical improvements justify parity despite the theoretical formalism issue.

**Decision**: Accept. The method is sound, the practical contribution is clear and well-validated, and the weaknesses are bounded presentation issues that do not undermine the core results. The paper would benefit from revision on the Eq. 2 framing and Gaussian Shading comparison, but these are addressable in revision.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>