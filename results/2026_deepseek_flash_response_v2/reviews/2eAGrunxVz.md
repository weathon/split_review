## Summary

This paper proposes Spherical Watermark, a lossless watermarking framework for diffusion models. The method converts binary watermarks into Gaussian noise via a spherical 3-design construction: binary embedding (mixing watermark bits with random padding using an invertible matrix T) followed by spherical mapping (normalization to the unit sphere, orthogonal rotation, and chi-square scaling). It requires only a single fixed secret key rather than per-image keys, eliminating key-management overhead. Experiments with Stable Diffusion show fidelity preservation, undetectability matching PRC, computational efficiency (~4 orders of magnitude faster transform), and strong robustness under adversarial attacks.

## Strengths

1. **Elegant theoretical connection to spherical 3-designs**: The paper proves that the watermarked noise matches the uniform spherical distribution up to third-order moments (Theorem 3.2, Lemma 3.3, Lemma 3.4), providing formal grounding for distributional fidelity. This is a genuinely novel theoretical contribution compared to prior lossless watermarking methods that rely on cryptographic constructs.

2. **Elimination of per-image key storage**: A single fixed signature K = {T, C} suffices for all images, unlike Gaussian Shading which requires a unique key+nonce per image. This is a practical advantage for large-scale deployment, directly supporting the paper's claim of reduced key-management overhead.

3. **Strong empirical undetectability**: Table 1 shows FID matching the original unwatermarked baseline (48.12 vs 48.13 on COCO SD v1.5), and Figure 2 shows near-chance classifier accuracy — matching PRC while Tree-Ring and Gaussian Shading (with fixed keys) are trivially detectable.

4. **Adversarial robustness and high-capacity advantage**: Under WEvade attacks (Table 2), the method achieves 99.83% TPR vs PRC's 95.38% (+4.5% absolute). Figure 6(a) shows sustained detection across the full capacity range (l_m up to 3000+) while PRC fails entirely beyond l_m=2000 under JPEG-70 — a clear scalability advantage.

5. **Comprehensive ablation studies**: Module ablations (Figure 6b-c) confirm both binary embedding and spherical mapping are necessary; ODE solver and timestep ablations (Tables 4-5) show robustness across different sampling configurations (all ≥96% ACC across DDIM, PNDM, DPM-Solver++).

6. **Computational efficiency**: The transform (embedding+extraction) is ~4 orders of magnitude faster than PRC's belief-propagation decoding (Figure 4), a genuine practical advantage for deployment scenarios.

## Weaknesses

### Major

- **Mismatch between theoretical guarantee and claimed indistinguishability**: The problem formulation (Eq. 2) defines undetectability as computational indistinguishability with a negl(ρ) bound, but the theory only guarantees moment-matching up to degree 3 (Theorem 3.2). A spherical 3-design can deviate from uniformity in fourth and higher moments, and the paper does not bound the statistical distance or show that higher-order deviations are negligible. The abstract correctly states "up to third-order moments" in its first sentence, but the introduction (line 26: "prove that the final noise is statistically indistinguishable from standard Gaussian noise"), conclusion (line 336: "provably and empirically indistinguishable"), and contribution list (line 28) assert full indistinguishability without this qualification. The limitations section acknowledges "higher-order moments may deviate," but the forward-facing claims outrun what is proven. This gap between claim and proof erodes credibility and should be addressed in revision.

### Minor

- **Gaussian Shading undetectability comparison uses a weakened baseline**: The paper evaluates Gaussian Shading with fixed keys (line 193: "Note that with fixed keys, Gaussian Shading no longer achieves true losslessness") and then shows it is detectable while the proposed method is not. Gaussian Shading with per-image keys (its intended configuration) would also be undetectable. The comparison is informative for illustrating the cost of single-key simplification, but the presentation could misleadingly imply a fundamental undetectability advantage over Gaussian Shading rather than a key-management trade-off.

- **"Encryption-free" terminology is imprecise**: The method still requires secret, fixed parameters K = {T, C} to prevent unauthorized removal. "Single-key" or "fixed-key" would be more accurate descriptors. The true advantage — eliminating per-image key management — is genuine and significant, but the label overstates the absence of secrets.

- **Computational speedup reported only on a subcomponent**: The paper states extraction is "about four orders of magnitude faster" than PRC, but explicitly notes this excludes "any diffusion sampling or inversion procedures" (line 256). The ODE inversion step (Eq. 12) is common to all latent-based methods and is likely the dominant cost. Without knowing what fraction of total runtime the transform represents, the end-to-end speedup is unclear.

### Trivial

- Notational issue: In Eq. 6, l̅_m = N × l_m is used without explicit prior definition, which may confuse readers on first encounter.

## Nice-to-Haves

- Report end-to-end extraction timing (including DDIM inversion) to contextualize the transform-level speedup.
- Discuss whether knowledge of the spherical 3-design architecture (but not the specific T, C matrices) enables targeted attacks exploiting the known higher-order moment structure.

## Removed Points

*These points were flagged for removal from the primary review. Treat them with caution.*

- **Harsh critic's claim that the Gaussian Shading comparison is "structurally unfair" and "apples-to-oranges"**: The paper transparently acknowledges the fixed-key configuration (line 193). The comparison serves a legitimate purpose — illustrating the trade-off that motivates the method. Demoted to minor weakness rather than a structural flaw.
- **Criticisms about missing appendix proofs, formatting, reproducibility of hyperparameters**: These are either parser artifacts (missing appendix content), standard practice for the field, or removed per hard rules (typos, formatting).
- **Strength Finder's generic strengths** ("addressed an important problem"): Removed as not substantive or redundant with kept strengths.
- **Harsh critic's concern-sweeps without concrete paper anchors** (e.g., "could the metric be measuring a proxy"): Removed per filtering discipline as speculation rather than identified problems.
- **Harsh critic's point about Algorithm 1 variable naming clarity**: Too fine-grained to retain as an actionable weakness.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any novel synthesis that the paper itself does not already articulate.

## Suggestions

1. Align the indistinguishability claims with what is actually proven: replace "statistically indistinguishable" in the introduction and conclusion with "statistically indistinguishable up to third-order moments" or "empirically indistinguishable as verified by classifiers."
2. Rephrase "encryption-free" to "single-key" or "fixed-key" throughout, to better describe the actual advantage.
3. Add end-to-end timing breakdown or at minimum state the approximate fraction of total extraction time accounted for by the transform versus ODE inversion.
4. When presenting undetectability results, explicitly clarify that Gaussian Shading with per-image keys would also be undetectable, and frame the comparison as illustrating the key-management trade-off rather than a fundamental undetectability advantage.

## Calibration Details

**Round 1 Bracket:** 5–7 (middle band).

**All Retrieved Anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| fkNsgI1nye.md | 3.00 | 1 | Privacy-preserving diffusion inference; not watermarking, much weaker paper |
| vK8C37eHXM.md | 3.20 | 1 | Autoencoder compression; not watermarking, much weaker paper |
| hYEV8QmaOt.md | 3.40 | 1 | Image anti-forensics; not watermarking, much weaker paper |
| jbfDg4DgAk.md | 3.00 | 1 | LLM watermarking; different domain, weaker paper |
| HexshmBu0P.md | 5.33 | 1,2,3 | "A Recipe for Watermarking Diffusion Models" — Rejected. Empirical recipe paper; our paper has stronger novelty and theory. |
| T0ebbDO60R.md | 3.75 | 1 | Super-resolution based watermarking; different approach, weaker evaluation |
| ll2nz6qwRG.md | 5.83 | 1,2,3 | "Hidden in the Noise / WIND" — Accepted. Two-stage watermarking; our paper has more thorough evaluation and stronger theoretical contribution → our paper is better |
| 1IwoEFyErz.md | 6.00 | 1,2 | "Shallow Diffuse" — Rejected for presentation/experimental incompleteness; our paper is better presented with more complete experiments |
| 84n3UwkH7b.md | 8.00 | 1 | Memorization detection in DMs; not watermarking, different topic |
| I5lcjmFmlc.md | 8.00 | 1 | Robust classification via diffusion; not watermarking |
| j7b4mm7Ec9.md | 7.60 | 1 | Lightweight deep watermarking; not diffusion-specific, different subarea |
| fV0t65OBUu.md | 8.00 | 1 | Diffusion covariance matching; not watermarking |
| jlhBFm7T2J.md | 6.50 | 2 | **PRC paper** (direct baseline) — Accepted. Our paper is weaker on theoretical rigor (PRC has cryptographic indistinguishability) but stronger empirically (robustness, capacity, efficiency). Overclaiming issue makes our paper slightly worse overall. |
| uHdf9F1tY4.md | 5.50 | 2,3 | "DiffusionShield" — Rejected. Data copyright protection; comparable quality but our paper has clearer contribution. |
| ETFfXGM3e4.md | 5.50 | 2,3 | "SAT-LDM" — Rejected. Training-based watermarking; our paper has stronger novelty and more complete evaluation. |
| mDKxlfraAn.md | 6.40 | 2 | Watermark removal attack paper; interesting but different direction |
| UchRjcf4z7.md | 6.50 | 2 | Transfer attack to image watermarks; different direction |

**Narrowing to Final Score:** The most informative anchor is the PRC paper (6.50, Accept), which is the direct baseline. Our paper has a weaker theoretical guarantee (moments up to 3rd order vs. cryptographic indistinguishability) and an overclaiming issue, but stronger empirical results (robustness, capacity scaling, efficiency). Comparing against all anchors, the paper sits between WIND (5.83, Accept) and the PRC paper (6.50, Accept), thus **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>