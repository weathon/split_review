## Summary

This paper proposes Spherical Watermark, a lossless watermarking scheme for diffusion models. The method embeds binary watermarks into the Gaussian noise input through three reversible modules: binary embedding (mixing repeated watermark bits with random padding via an invertible matrix T over F₂), spherical mapping (projecting onto the unit sphere, applying an orthogonal rotation C, and scaling by a χ²-distributed radius), and diffusion integration. The key theoretical result is that the watermarked noise matches the target Gaussian prior up to third-order moments via a spherical 3-design argument. Empirically, the scheme achieves strong undetectability (classifier accuracy near chance), FID matching the original distribution, 99.99% extraction accuracy on clean data, robustness under post-processing and adversarial attacks, and ~4 orders-of-magnitude faster extraction than the PRC baseline.

## Strengths

1. **Novel and theoretically grounded spherical 3-design approach.** The paper proves (Theorems 3.1–3.2, Lemmas 3.3–3.4) that the watermarked noise matches the target prior up to third-order moments. This is a stronger formal distribution-matching guarantee than prior lossless methods (Gaussian Shading, PRC) provide—those rely on cryptographic or coding-theoretic indistinguishability rather than explicit moment matching. The chain of reasoning from 3-wise independent Bernoulli bits → spherical 3-design → orthogonal rotation invariance is mathematically coherent.

2. **Elimination of per-image key management while preserving losslessness.** Unlike Gaussian Shading, which requires a unique key and nonce per image, Spherical Watermark uses a fixed signature K = {T, C} (Section 3.2). The empirical evidence (Figure 2) confirms that this fixed-key design maintains near-chance detection, whereas Gaussian Shading with fixed keys becomes detectable at 97% accuracy—demonstrating a practical trade-off that prior methods could not achieve.

3. **Four-orders-of-magnitude faster extraction than PRC.** Figure 4 reports extraction times of ~10^−3.5 s for Spherical Watermark vs ~10^1.0 s for PRC. This is a direct consequence of replacing belief-propagation decoding with simple matrix inversion and rounding (Eq. 13), quantified over 100 trials with logarithmic-scale visualization.

4. **Sustained detection at high watermark capacities where PRC fails.** Figure 6(a) shows that PRC's decoding collapses entirely beyond l_m = 2000 under JPEG-70 compression, while Spherical Watermark maintains high detection rates across the full tested capacity range. This robustness advantage stems from the majority-vote + spherical mapping design rather than error-correcting codes.

5. **Empirical undetectability via classifier attacks and FID.** Figure 2 and Table 1 show that a ResNet-18 classifier cannot distinguish Spherical Watermark outputs from unwatermarked ones (near 50% accuracy), while Tree-Ring and fixed-key Gaussian Shading are detected at 100% and 97% accuracy. FID values in Table 1 match the original within error bars (e.g., 48.12 vs 48.13 on COCO SD v1.5).

## Weaknesses

### Fatal
None.

### Major

1. **Overstatement of the theoretical guarantee in the introduction and conclusion.** The introduction states "we prove that the final noise is statistically indistinguishable from standard Gaussian noise" (line 26), and the conclusion claims the noise is "provably ... indistinguishable from a standard Gaussian prior." However, the actual theoretical analysis only reaches 3rd-order moment matching (spherical 3-design). Lemma 3.4 requires *uniform* distribution on the sphere to recover exact N(0, I), but the paper only has a spherical 3-design (matching up to degree 3). The opening of Section 3.3 similarly claims "the final latent code z_w is distributed as N(0, I_{l_x})" without qualification. While Section 5 acknowledges that "higher-order moments may deviate," the stronger claim appears in multiple prominent places and is inconsistent with what is actually proven. This needs correction before publication—the paper should distinguish between what is proven (matching up to 3rd-order moments) and what is empirically supported (practical indistinguishability).

2. **The security parameter ρ is never instantiated.** Eqs. (2–4) use the language of computational indistinguishability (negl(ρ), PPT adversary) with a security parameter ρ, but ρ is left undefined throughout. Without connecting ρ to any concrete parameter (latent dimensionality? watermark length? key size?), the negl(·) formalism carries no substantive meaning. The paper should either instantiate ρ and derive concrete bounds, or drop the cryptographic formalism in favor of more direct empirical characterization.

### Minor

3. **Framing of the Gaussian Shading comparison conflates two separate issues.** The paper evaluates Gaussian Shading with fixed keys and reports 97% detection accuracy (Figure 2). The paper explicitly notes (line 193) "with fixed keys, Gaussian Shading no longer achieves true losslessness," so the setup is transparent. However, the presentation could mislead readers into thinking Gaussian Shading is inherently detectable, when in fact its detectability stems from using a configuration that breaks its own security guarantee. The paper's valid point—that Gaussian Shading's per-image key requirement is impractical—should be presented separately from the undetectability comparison. Showing Gaussian Shading in its intended (per-image key) configuration as a control would be fairer.

4. **The rotation matrix C's actual dimensions are ambiguous.** The paper sets l_c = l_x in descriptions (line 113) but notes in a footnote that "l_c is chosen as a factor of l_x (e.g. l_c = ⌊√l_x⌋)." If l_c ≠ l_x, the multiplication C z^(2) in Eq. (10) does not directly apply as a simple matrix-vector product. The paper does not specify the actual l_c used in experiments or explain how C maps to an l_x-dimensional vector when l_c < l_x (e.g., block-diagonal application, tiling, or some other mechanism). This ambiguity affects reproducibility.

5. **Traditional baselines embed only 32-bit watermarks vs. 512-bit for others.** DwtDct, DwtDctSvd, and RivaGAN embed 32-bit watermarks while latent-based methods use 512 bits (Section 4.1). This makes comparisons uneven in the traditional methods' favor—they encode far fewer bits, which makes their robustness and FID numbers not directly comparable.

6. **Traceability definition (Eq. 4) uses negl(ρ) but measured ACC is 99.99%.** The formal definition requires error negligible in ρ, but 0.01% error is not formally negligible in the cryptographic sense. This is a minor formal discrepancy since the scheme's practical performance is excellent and all competing methods show similar behavior, but the definition should be relaxed to "overwhelming probability" rather than "1 − negl(ρ)."

### Trivial

7. **Key compromise scenarios not discussed.** If K = {T, C} is compromised, all past and future watermarks can be removed or forged. The paper notes K is kept secret but does not discuss key distribution, rotation, or the implications of compromise. For a deployed system this is important but is outside the paper's stated contribution scope.

## Nice-to-Haves
- Evaluate Gaussian Shading with per-image keys as an additional control for the undetectability comparison, then separately discuss key-management overhead
- Add higher-order statistical tests (kurtosis, 4th-order cross-moments) to directly probe the limitations of the 3-design guarantee
- Specify the actual l_c value and the C application mechanism (block-diagonal? tiled?) used in experiments
- Report the storage cost of C in the implementation to complete the computational efficiency picture

## Removed Points

These points were flagged during review filtering but are not included as substantive weaknesses:

1. **"Gaussian Shading embedding time seems anomalously high"** (Harsh Critic, Section 4.2): The paper reports ~3s for Gaussian Shading embedding. The critic finds this high for a stream cipher. However, the paper states times are averaged over 100 trials "focusing exclusively on the transformation between the watermark and its latent noise representation, excluding any diffusion sampling or inversion procedures." Without knowing the exact implementation, 3s for a 16384-dimensional operation involving the full watermark pipeline (construction, repetition, cipher application, reshaping) is not necessarily anomalous. Removing as speculative.

2. **"Zero standard deviation in adversarial TPR is suspicious"** (Harsh Critic, Table 2): The critic notes 99.83 ± 0.00. However, multiple entries in Table 2 show 0.00 std dev (Gaussian Shading Adv TPR: 99.23 ± 0.00, PRC Adv TPR: 95.38 ± 0.00). The zero likely reflects rounding of very small variance rather than truly zero variance. This is a common artifact in reporting tables and does not indicate a methodological flaw. Removing.

3. **"Robustness at 10 timesteps raises concern about watermark leaking into images"** (Harsh Critic, Section 4.3): This is speculation without evidence, not a concrete problem identified in the paper. Removing.

4. **Strength Finder claim about "stronger theoretical distribution-matching guarantee than prior lossless methods"** — This is retained in modified form. The spherical 3-design is indeed a stronger formal guarantee than what Gaussian Shading (stream cipher) offers in terms of explicit moment matching, though PRC offers cryptographic indistinguishability. The retained strength reflects this nuance.

5. **Strength Finder generic claim about "addressing an important problem"** — Removed as generic/superficial. The retained strengths are concrete and evidenced.

## Novel Insights

None beyond the paper's own contributions. The reviewers did not identify any observation about the paper that the paper itself does not already articulate.

## Suggestions

1. Replace the overstated theoretical claims ("prove that the final noise is statistically indistinguishable") with an honest characterization: "proven to match up to 3rd-order moments via spherical 3-design, with empirical evidence supporting practical indistinguishability."
2. Either instantiate the security parameter ρ or drop the cryptographic negl(·) formalism in favor of direct empirical characterization.
3. Clarify the actual l_c value and the mechanism for applying C to an l_x-dimensional vector in the implementation.
4. Add a control experiment with Gaussian Shading in its intended (per-image key) configuration, and present the key-management discussion separately from the undetectability comparison.
5. Disclose the storage cost of C and the practical parameter choices (l_c, floating-point precision) used in experiments.

## Score and Decision

**Round 1 bracket:** The paper sits above weak anchors (avg ~3.0, tangential watermarking/generative papers) and below strong anchors (avg 8.0, memorization/compression papers). The plausible range is (3.5, 7.5).

**Round 2 narrowing:** Compared against five directly relevant anchors:
- PRC Watermark (6.50, Accept) — slightly above this paper due to cleaner theoretical framing
- Shallow Diffuse (6.00, Reject) — this paper is stronger in both novelty and empirical breadth
- Hidden in Noise (5.83, Accept) — this paper is stronger
- SAT-LDM (5.50, Reject) — this paper is clearly stronger
- A Recipe (5.33, Reject) — this paper is clearly stronger

Comparative judgment: This paper is stronger than Shallow Diffuse (6.00) in novelty and empirical evidence, but slightly below the PRC paper (6.50) due to the theoretical overclaiming and C matrix ambiguity. The core method and most experimental results are solid; the main issues are in framing and clarity, not in the underlying science.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>