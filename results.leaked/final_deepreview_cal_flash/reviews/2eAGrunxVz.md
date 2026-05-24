Now I have a complete understanding. Let me write the final consolidated review.

## Summary

This paper proposes Spherical Watermark, an encryption-free watermarking framework for diffusion models that transforms binary watermarks into Gaussian noise via spherical mapping (projection onto the unit sphere, orthogonal rotation, and chi-square scaling). The method eliminates per-image key management required by Gaussian Shading and avoids the heavy cryptographic decoding of PRC Watermark, while achieving strong empirical undetectability and robustness. The authors provide theoretical analysis showing the watermarked noise matches the Gaussian prior up to third-order moments, and extensive experiments on Stable Diffusion demonstrate competitive or superior performance across undetectability, traceability, and computational efficiency (extraction ~4 orders of magnitude faster than PRC).

## Strengths

1. **Clean and well-motivated methodological design.** The spherical mapping approach (binary embedding → 3-wise independent bits → spherical 3-design → orthogonal rotation → chi-square scaling) is elegant and principled. The theoretical grounding in spherical t-designs (Section 3.3, Theorems 3.1–3.2, Lemmas 3.3–3.4) provides a clear justification for why the constructed noise matches the Gaussian up to third-order moments.

2. **Strong empirical evidence for practical undetectability.** The paper convincingly demonstrates that watermarked noise is practically indistinguishable from standard Gaussian via multiple complementary tests: latent-level MLP classifiers (Figure 2, near-50% accuracy), image-level ResNet-18 classifiers (Figure 2), and FID scores matching the unwatermarked baseline (Table 1). This goes beyond what most competing methods provide.

3. **Dramatic computational advantage over PRC Watermark.** Extraction time is ~10⁻³·⁵ s — roughly four orders of magnitude faster than PRC's ~10¹ s (Figure 4). This is a genuine practical contribution, as PRC's belief-propagation decoding is a known bottleneck. The encryption-free design also eliminates per-image key storage, addressing a real deployment concern.

4. **Thorough and well-structured experimental evaluation.** The paper evaluates undetectability, robustness under multiple post-processing and adversarial attacks (Table 2, Figure 5), scalability to large payloads (Figure 6a), module ablations (Figures 6b–c), parameter sensitivity (Table 3, Figure 6d), and robustness across ODE solvers and timestep configurations (Tables 4–5). The ablation on modules convincingly shows that both the binary embedding and spherical mapping are necessary.

## Weaknesses

### Fatal
None.

### Major

1. **Gap between formal undetectability definition and actual theoretical guarantees.** Eq. (2) defines undetectability as computational indistinguishability (bounded by `negl(ρ)` for any PPT adversary), but the theoretical analysis only proves moment-matching up to degree three. Section 3.3 states that the final latent code *"is distributed as `N(0, I)`"* in `ℝ^{l_x}` — a stronger claim than what the spherical 3-design argument supports. Lemma 3.4 requires *exact* uniform distribution on the sphere to yield a true Gaussian via the polar decomposition, but the construction only provides a spherical 3-design (exact up to degree three). The paper acknowledges in the Limitations (Section 5) that *"higher-order moments may deviate"*, but this caveat is absent from the main theoretical section and the conclusion, which reasserts *"provably and empirically indistinguishable"*. The paper should either weaken the claims to match what is proven or provide a rigorous bound quantifying how the 3-design approximation translates to statistical distance.

2. **Underspecified rotation matrix creates a gap between theory and practice.** The theoretical analysis (Section 3.3, Lemma 3.3) assumes a global orthogonal rotation `C ∈ ℝ^{l_x × l_x}` acting on the full vector. However, the paper states that `l_c` is chosen as *"a factor of `l_x` (e.g. `l_c = ⌊√l_x⌋`)"* for efficiency — which for the default `l_x = 16384` implies `l_c ≈ 128`. The paper never explains how an `l_c × l_c` rotation is applied to an `l_x`-dimensional vector (block-diagonal? reshaping? kronecker product?). If a block-diagonal structure is used, the spherical 3-design property proven for individual blocks does not automatically extend to the concatenated full vector, and the proof in Appendix C would require a different argument. This ambiguity undermines both reproducibility and the connection between the theoretical analysis and the actual computation.

### Minor

3. **Gaussian Shading baseline comparison is not fully informative.** The paper acknowledges that Gaussian Shading is evaluated *"with fixed keys"* and that this *"no longer achieves true losslessness."* However, the undetectability comparison (Figure 2) still presents Gaussian Shading as easily detectable (97% accuracy) to support the claim of superiority over lossless methods. The intended version of Gaussian Shading (with per-image unique keys) is provably lossless with exact standard Gaussian noise. A comparison against the intended version would frame the trade-off more accurately: approximate losslessness + no per-image keys vs. exact losslessness + key overhead. The current presentation inflates the perceived advantage.

4. **Equation (6) notation is confusing.** The equation `l_m = N × l_m` reuses the symbol `l_m` for two different quantities (original watermark length vs. total repeated length), which requires the reader to infer the redefinition from context.

5. **Conclusion overstates theoretical guarantee.** The conclusion states *"Watermarked latent inputs are provably and empirically indistinguishable from a standard Gaussian prior"* without the qualification *"up to third-order moments"* that appears in the abstract.

### Trivial
None.

## Nice-to-Haves

- A small-scale numerical experiment (e.g., `l_x = 100`) computing total variation distance or maximum mean discrepancy between the spherical-3-design-based distribution and the true multivariate normal would help quantify the approximation gap.
- An ablation on the rotation block size `l_c` would clarify whether larger blocks improve undetectability/robustness, and would resolve the ambiguity about the implementation.
- Reporting the storage size of the signature `𝒦 = (T, C)` (in MB) would help practitioners assess deployment feasibility.

## Removed Points

These points from the inputs were flagged and removed.

**From Harsh Critic:**
- *"Gaussian Shading ... the comparison deliberately uses it with fixed keys—a configuration that breaks its losslessness and makes it trivially detectable"* → Downgraded from the critic's "evidential" framing to Minor (#3 above), because the paper explicitly acknowledges the limitation ("Note that with fixed keys, Gaussian Shading no longer achieves true losslessness."), and the main comparison is against PRC Watermark, not Gaussian Shading. The critic's characterization as "intentionally crippled" is too strong; the paper is transparent about the setting.
- *"The classifier experiments ... do not justify the headline claim of superiority over all lossless methods"* → Removed because the paper's comparison against PRC (the SOTA lossless method) does show meaningful advantages in computational efficiency and robustness. The claim is justified for the lossless methods evaluated.
- *"Missing false positive analysis"* → The paper reports TPR@1%FPR which implicitly controls FPR. The critic's request is a nice-to-have, not a weakness.
- Various reproducibility nitpicks about "undisclosed hyperparameters" and "missing appendix proofs" → Parser-stripped content that exists in the original submission.
- *"Rotation matrix details ... the method cannot be reproduced"* → Downgraded from "cannot be reproduced" to Major (#2 above). The paper provides enough to attempt reproduction (l_c = floor(sqrt(l_x)), QR-based generation), but the precise application of the rotation is ambiguous. The critic's assertion of full irreproducibility is too strong.

**From Strength Finder:**
- Generic/scope-creep strengths removed: none of the Strength Finder's points were generic. All are grounded in specific paper evidence and retained, though merged/condensed.

## Novel Insights

The key insight that emerges from synthesizing the reviews is that the paper's core contribution — an encryption-free spherical mapping for watermark embedding — sits in an interesting middle ground between two existing approaches. Gaussian Shading achieves exact losslessness through per-image keys, while PRC achieves cryptographic undetectability through heavy computation. Spherical Watermark shows that one can obtain *practical* (empirically verified) undetectability with dramatically lower overhead by relaxing exact distributional guarantees to moment-matching up to degree three. This trade-off is worth studying, but the paper would benefit from being more explicit that this is a deliberate relaxation rather than claiming to match the stronger guarantees of the prior work.

## Suggestions

1. **Clarify the theoretical claims.** Distinguish between the ideal goal (Eq. 2: computational indistinguishability) and what is actually proven (moment-matching up to third order). Revise Section 3.3's opening sentence to say *"approximately distributed as `N(0, I)` with matching up to third-order moments"* rather than *"is distributed as `N(0, I)`."* Include the caveat about higher-order moments in the main theoretical section, not just in Limitations.

2. **Resolve the rotation matrix ambiguity.** Explicitly state the exact `l_c` value used in the experiments and describe precisely how the `l_c × l_c` rotation matrix is applied to the `l_x`-dimensional vector (e.g., is it block-diagonal? If so, how many blocks? Is the same rotation applied to each block, or independent rotations?). Provide a justification (theoretical or empirical) that the chosen scheme preserves the practical undetectability demonstrated in the experiments.

3. **Add a fair Gaussian Shading comparison.** Include a small-scale or full comparison against Gaussian Shading with per-image keys in its lossless regime, even if only for undetectability on a subset of the data. This would make the trade-off explicit and strengthen the paper's claims about eliminating key overhead.

4. **Fix Eq. (6) notation.** Use a distinct symbol for the total repeated length (e.g., `l_m' = N × l_m` or `l_{Nm}` which is already introduced later).

## Score and Decision

### Calibration Analysis

**Round 1 — Bracketing.** Three queries covering the weak (score < 3.5), middle (3.5–7.5), and strong (> 7.5) bands produced anchors broadly across the scale.

**Round 1 bracket:** The paper clearly sits above the weak-band anchors (3.0–3.4, mostly reject papers with fundamental flaws). It is below the strong-band anchors (7.6–8.0, papers with highly polished execution and few weaknesses). The initial bracket is **4.5–7.5**.

**Round 2 — Narrowing.** Two queries inside (4.5, 6.5) and (5.5, 7.5) returned anchors including:
- **Shallow Diffuse** (6.00, Reject) — Comparable in scope; Spherical Watermark has more thorough experiments but similar-level issues (both have theory-practice gaps). Similar quality.
- **Hidden in the Noise / WIND** (5.83, Accept) — Similar area; Spherical Watermark has cleaner theoretical framing and more comprehensive evaluation. Slightly stronger.
- **PRC Watermark** (6.50, Accept) — The main competitor; PRC has stronger cryptographic guarantees but weaker robustness and efficiency. Spherical Watermark is slightly weaker in theoretical rigor but stronger in practical performance.
- **SAT-LDM** (5.50, Reject) — Less novel methodology; Spherical Watermark is clearly stronger.

**Narrowed bracket:** 5.5–6.5. Within this bracket, the paper is stronger than SAT-LDM (5.50), comparable to Shallow Diffuse (6.00), and slightly weaker than PRC (6.50) due to the theory-practice gaps identified above.

**Final score: 6.0** — A solid paper with real contributions and thorough empirical work, held back by overclaimed theoretical guarantees and underspecified implementation details that prevent it from reaching the level of the strongest papers in this space.

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| fkNsgI1nye | Secure Diffusion Model Unlocked | 3.00 | R1 | Much weaker — fundamental flaws |
| jbfDg4DgAk | Sparse Watermarking in LLMs | 3.00 | R1 | Much weaker — different domain |
| hYEV8QmaOt | From Forgery to Authenticity | 3.40 | R1 | Much weaker — different task |
| T0ebbDO60R | SuperMark | 3.75 | R1 | Weaker — limited contribution |
| HexshmBu0P | Recipe for Watermarking DMs | 5.33 | R1/R2 | Weaker — less novel, narrower eval |
| ETFfXGM3e4 | SAT-LDM | 5.50 | R2 | Weaker — less novel, less clean theory |
| ll2nz6qwRG | Hidden in the Noise (WIND) | 5.83 | R2 | Comparable — similar depth, different trade-offs |
| **1IwoEFyErz** | **Shallow Diffuse** | **6.00** | **R1/R2** | **Comparable — similar quality, Spherical WM has more thorough eval** |
| **jlhBFm7T2J** | **PRC Watermark (undetectable WM)** | **6.50** | **R2** | **Slightly stronger — rigorous crypto guarantees** |
| j7b4mm7Ec9 | Lightweight Deep WM Framework | 7.60 | R1 | Stronger — polished execution, different domain |
| RuP17cJtZo | Generator Matching | 8.00 | R1 | Stronger — different domain, top quality |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>