Now I have a thorough understanding of the paper. Let me prepare the draft review and then run calibration searches.Now let me run the 5 calibration searches:Now let me write the final consolidated review:

---

## Summary
Spherical Watermark proposes an encryption-free, lossless watermarking framework for diffusion models. Binary watermarks are first mixed with random padding to form a 3-wise independent code, then projected onto the unit sphere as a spherical 3-design, orthogonally rotated, and scaled by a chi-square-distributed radius to produce approximately Gaussian-distributed noise. The method eliminates per-image key management overhead, and experiments on Stable Diffusion demonstrate that extraction is roughly four orders of magnitude faster than PRC Watermark, robustness is maintained at high watermark capacities (up to l_m=512 bits where PRC fails entirely), and adversarial attack resistance is marginally better than PRC.

---

## Strengths

- **Strong empirical undetectability**: Figure 2 shows classifiers achieve ~50% accuracy (indistinguishable from chance) at both latent-level (MLP) and image-level (ResNet-18) for the proposed method, while Tree-Ring and fixed-key Gaussian Shading achieve 100% and 97% respectively. Table 1 confirms FID scores (e.g., 48.1224 vs. 48.1256 on COCO with SD v1.5) match the unwatermarked baseline.

- **Superior adversarial robustness**: Table 2 shows 98.12% ACC and 99.83% TPR under WEvade adversarial attack, outperforming PRC Watermark (97.69% ACC, 95.38% TPR) and all lossy methods (DwtDct: 16.15% TPR). The paper provides a sound theoretical explanation (Appendix E) for why lossless methods resist adversarial attacks that exploit detectable embeddings.

- **Massive computational efficiency gain**: Figure 4 shows extraction is approximately four orders of magnitude faster than PRC Watermark (~10^{-3.5}s vs. ~10^{1.0}s), directly attributable to eliminating belief-propagation decoding. This is a significant practical contribution.

- **Scalable watermark capacity**: Figure 6(a) shows PRC Watermark fails entirely past l_m=2000 bits under JPEG-70 compression, while Spherical Watermark sustains high detection rates across the full capacity range, including the default l_m=512 bits.

- **Thorough ablations**: Figures 6(b–c) validate that both binary embedding and spherical mapping are necessary (omitting binary embedding makes the latent trivially distinguishable; omitting spherical mapping collapses robustness under brightness adjustment). Tables 4–5 confirm robustness across ODE solvers and timestep schedules.

---

## Weaknesses

### Fatal
None.

### Major
- **Mismatch between formal security claim and what is actually proved** (Eq. 2 vs. Theorems 3.1–3.2 and Lemma 3.4): Eq. 2 invokes cryptographic negl(ρ) notation — "for any probabilistic polynomial-time adversary A, |Pr[A(z_w)=1] − Pr[A(z)=1]| ≤ negl(ρ)" — which implies full computational indistinguishability. What the paper actually proves is that z^{(2)} is a spherical 3-design (Theorem 3.2) and that orthogonal rotation preserves this (Lemma 3.3). Lemma 3.4's converse direction formally requires u to be *truly* uniform on S^{n-1}, but z^{(3)} = Cz^{(2)} is only a 3-design (an approximation of uniform). Consequently, z_w ≈ N(0, I) only up to 3rd-order moments, not exactly. The paper handles this honestly in Section 5 ("higher-order moments may deviate from the true prior") and in the abstract ("up to third-order moments"), but these admissions conflict with the negl(ρ) notation in Eq. 2 and with the abstract's claim of recovering "exact multivariate Gaussian noise." The large dimensionality (l_x=16384) likely makes the approximation error negligible in practice, and the 50% classifier accuracy strongly supports the claim empirically — but the formal scaffolding overstates what is proved.

### Minor
- **Gaussian Shading comparison framing**: The paper compares against Gaussian Shading in a fixed-key setting (Section 4.1: "with fixed keys, Gaussian Shading no longer achieves true losslessness"), which is the operationally correct comparison for the paper's goal. However, the framing conflates "Gaussian Shading fails in the fixed-key setting" with a general undetectability failure. Gaussian Shading's original per-image nonce design achieves losslessness by construction; it fails only at per-image key management. The PRC Watermark comparison (genuinely targeting the fixed-key setting) is the more directly meaningful primary comparison, and the paper's advantages there are compelling on their own.

### Trivial
- Eq. 6 writes "l_m = N × l_m" where the row dimension label should read l_{Nm} = N × l_m to avoid self-referential notation. The meaning is unambiguous from context, but the notation is imprecise.

---

## Nice-to-Haves
- Replace Eq. 2's negl(ρ) notation with an explicit moment-matching guarantee ("indistinguishable by any test of degree ≤ 3") or provide an upper bound on the deviation from true Gaussian as a function of l_x, to match what is formally proved.
- A quantitative characterization of the KL divergence (or maximum moment deviation) as a function of l_x would substantially strengthen the theoretical contribution beyond the 3-design argument.
- A brief formal analysis of how much inversion error (in terms of coordinate sign flips) the N=31 majority voting can tolerate, calibrated against realistic DDIM inversion errors, would complement the empirical ablation in Tables 4–5.
- A brief discussion of whether the fixed signature K={T, C} could be recovered by an adversary who issues many API queries and observes outputs — the authors could briefly argue this requires latent-level access unavailable via a black-box API.
- Expanding Figure 6(a) with a joint sweep over N and s alongside l_m would give the scalability claim a cleaner empirical foundation.

---

## Removed Points
*These points are flagged to be removed; treat them with caution.*

- **Algorithm 1 3D-to-2D reshape ambiguity** (harsh critic): The algorithm explicitly writes "Return Reshape(R, (l_m, l_r))" on the final line, making the reshape unambiguous. Not a real reproducibility concern.

- **Extraction sign-preservation not formally analyzed** (harsh critic): The paper provides implicit analysis through Tables 3–5 (ablation on N, s, and timestep settings), which characterize the robustness margin empirically. The absence of a formal derivation does not undermine the contribution.

- **Figure 4 uses log-scale approximations** (harsh critic): Using a logarithmic y-axis is standard practice for quantities spanning 4+ orders of magnitude. The accompanying table provides the approximate values. Not a methodological error.

- **Adversary could recover K={T,C} by probing the API** (harsh critic — speculative): The harsh critic explicitly acknowledges "probably not via a black-box API." This is speculative and cannot be anchored to a specific passage in the paper. Moved to nice-to-have.

- **Strength: "exact multivariate Gaussian noise"** (strength finder): Conflicts with the verified Major weakness about the theory-proof gap. The "exact" characterization overstates the formal result; removed per conflict rule.

---

## Novel Insights
The paper's core insight — that binary codes with k-wise independence, when normalized to the unit sphere, form spherical designs whose moment-matching properties survive orthogonal rotation, and that chi-square scaling then approximates a full multivariate Gaussian — connects coding-theoretic notions (k-wise independence, repetition codes with majority voting) to geometric statistics on the sphere in a clean and practically useful way. The dimension-dependence of the approximation quality (l_x=16384 making higher-order deviations negligible) implicitly provides a principled criterion for when this approach is safe to deploy, suggesting a useful design principle: for fixed-key latent watermarking, the watermark-to-noise mapping can be made provably innocuous by exploiting the high dimensionality of modern diffusion latent spaces.

---

## Score and Decision

**Axis evaluation:**
- *Originality*: High — spherical mapping for fixed-key lossless watermarking is novel and structurally elegant.
- *Importance*: High — content provenance for diffusion-generated media is a pressing societal problem; fixed-key, encryption-free design is a meaningful practical advance.
- *Claims support*: Moderate-to-high — empirical support is strong across all major claims; formal proof notation overclaims in Eq. 2, but paper honestly acknowledges the 3-design approximation in Section 5.
- *Soundness of experiments*: High — thorough ablations, multiple datasets, two backbone models, adversarial evaluation, and timestep/solver robustness studies.
- *Clarity*: Good — well-organized; limitations honestly acknowledged; minor notation inconsistency in Eq. 6.
- *Value to research community*: High — 4-orders-of-magnitude extraction speedup and maintained capacity at l_m=512 bits where PRC fails are concrete, reproducible contributions.

The paper is a solid, well-executed contribution. Its core technique works, its efficiency and scalability advantages over PRC Watermark are real and significant, and its ablations are thorough. The primary weakness (overstatement in Eq. 2's formal notation versus the moment-matching result actually proved) is a presentation issue that revision can address; it does not invalidate the method or its empirical results.

---

# Selected Anchors

<related>["jlhBFm7T2J", "T0ebbDO60R", "OQccFglTb5", "HexshmBu0P", "ETFfXGM3e4", "PCm1oT8pZI", "71pur4y8gs", "mDKxlfraAn", "16O8GCm8Wn"]</related>

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>