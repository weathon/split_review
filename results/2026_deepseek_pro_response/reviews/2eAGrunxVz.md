Now I have a clear calibration picture. Let me compare the paper against the round-2 anchors:

- **jlhBFm7T2J (6.50, PRC Watermark, Accept)**: Our paper's direct baseline. PRC was accepted despite reviewers flagging loose theoretical bounds, robustness inferior to alternatives, and noticeable image changes. Our paper improves on PRC across robustness (Table 2), speed (~30,000× faster, Figure 4), capacity scaling (Figure 6a), and matches it on undetectability (Table 1, Figure 2). Our paper has its own theoretical gap (3-design ≠ exact Gaussian) but this is comparable to the theoretical looseness flagged in PRC.

- **1IwoEFyErz (6.00, Shallow Diffuse, Reject)**: Limited technical contribution, limited attacks, poor presentation. Our paper is clearly stronger.

- **ll2nz6qwRG (5.83, WIND, Accept)**: Only one model evaluated, theoretical proof flagged as unconvincing. Our paper is stronger with more thorough evaluation.

Our paper is stronger than the 6.50 PRC anchor due to practical improvements demonstrated head-to-head, and has comparable theoretical depth. Score: **7.0**.

---

## Summary
This paper introduces Spherical Watermark, a lossless watermarking method for diffusion models that maps binary watermarks to Gaussian noise through binary mixing (using a sparse embedding matrix T), spherical projection and normalization, orthogonal rotation (C), and chi-square scaling. The method eliminates per-image key management and cryptographic primitives, requiring only a single fixed secret signature. Experiments using Stable Diffusion v1.5/v2.1 show the method preserves FID, achieves chance-level classifier detectability at both latent and image levels, and extracts watermarks approximately four orders of magnitude faster than PRC Watermark while offering superior robustness.

## Strengths
- **Strong empirical undetectability:** Table 1 shows FID for the proposed method (48.12 on COCO SD v1.5) is indistinguishable from the original (48.13), while all other methods except PRC Watermark show measurable degradation. Figure 2 shows latent-level (MLP) and image-level (ResNet-18) classifiers at ~50% accuracy for the proposed method, while Tree-Ring and Gaussian Shading are trivially detected at 97–100%.
- **Massive computational efficiency gain:** Figure 4 reports extraction time of ~10^(-3.5) s for the proposed method vs. ~10^1 s for PRC Watermark — approximately four orders of magnitude faster — due to replacing belief-propagation decoding with simple matrix multiplication and majority voting. Embedding is also faster.
- **Thorough and informative ablation studies:** Figure 6(b) shows omitting binary embedding destroys undetectability; Figure 6(c) shows omitting spherical mapping causes robustness collapse under brightness adjustment. Table 3 systematically explores sparsity s and repetition N, confirming predictable degradation behavior. Tables 4–5 show solver and timestep choices have minimal impact.
- **Non-trivial theoretical framework:** The chain from 3-wise independence of XOR-mixed bits (Theorem 3.1) to spherical 3-design (Theorem 3.2) to the chi-square polar decomposition connection (Lemma 3.4) is genuinely novel in the watermarking literature and provides a principled alternative to cryptographic approaches.

## Weaknesses

### Fatal
None.

### Major
- **Theoretical gap between proof and claims.** The paper's central theoretical claim (abstract: "recover exact multivariate Gaussian noise"; introduction: "statistically indistinguishable from standard Gaussian noise"; Section 3.3 opening: "the final latent code z_w is distributed as N(0, I_{l_x})") does not follow from the presented analysis. Theorems 3.1–3.2 and Lemma 3.3 establish only that z^(3) is a spherical 3-design — matching the uniform spherical distribution in moments up to degree 3. Lemma 3.4 (polar decomposition) requires the direction vector to be *uniformly* distributed on S^{n-1} to recover N(0, I); a spherical 3-design does not satisfy this. The paper acknowledges the limitation in Section 5 ("higher-order moments may deviate from the true prior"), but the abstract, introduction, and conclusion overclaim what is actually proved. The empirical evidence (FID, classifier results) strongly supports practical indistinguishability, so this is a framing/correctness issue in the theoretical claims rather than a methodological flaw, but the claims throughout the paper need recalibration.

### Minor
- **"Encryption-free" terminology is imprecise.** The method uses a fixed secret Signature K = {T, C} that must be kept confidential to prevent unauthorized removal (Section 3.2, line 82). While the method genuinely avoids cryptographic primitives (stream ciphers, pseudorandom codes) and per-image key management, calling it "encryption-free" obscures that secret-key infrastructure is still required. More precise language (e.g., "cryptographic-primitive-free") would better capture the actual contribution.
- **Classifier experiment could be strengthened.** The image-level classifier experiment (Figure 2) uses 1000 watermarked + 1000 unwatermarked images with ResNet-18. While Figure 2 does report both training loss and test accuracy separately (and ~50% test accuracy is consistent with the indistinguishability conclusion), the relatively small dataset size limits the independent evidential weight of this experiment. The conclusion is triangulated by FID and latent-level MLP results.
- **No inversion baseline on unwatermarked images.** The extraction pipeline uses DDIM inversion with empty prompts (Eq. 12), which is inherently approximate. The residual ~0.01% extraction error under clean conditions (Table 2) could partially stem from inversion inaccuracy rather than watermark degradation. A baseline measuring inversion→re-extraction accuracy on unwatermarked images would disentangle these sources.

### Trivial
- Minor notation collision: the symbol `r` is used for both the chi-square-distributed scalar in Eq. (10) and the random padding vector in Section 3.2, which could confuse readers.

## Nice-to-Haves
- Include the original per-image-key Gaussian Shading configuration as a comparison point (even for a subset of experiments) to help readers understand the trade-off between key-management simplicity and extraction accuracy.
- Add a statistical test for FID differences between methods, since the error bars overlap substantially.
- Clarify the construction of C when l_c ≠ l_x: the footnote mentions choosing l_c as a factor of l_x for efficiency but the tiling/block-wise application mechanism is not described.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Appendix proofs need verification"** — the appendix is stripped from the submission copy; this is not a reviewable concern per the review guidelines.
- **"The security definition in Eqs. (2–4) is decorative / not engaged with"** — the paper borrows cryptographic formalism (PPT adversary, negligible functions) to frame the undetectability and traceability requirements. Using this framework to state design goals without proving security theorems is a stylistic choice, not a substantive flaw.
- **"No comparison with original Gaussian Shading" claimed as a fatal gap** — the paper explicitly notes the fixed-key limitation (line 193) and the comparison is fair in context. Including the original version is a nice-to-have, not a weakness.
- **"Statistical tests missing"** — moved to Nice-to-Haves; reporting mean and std over 5 runs is standard practice in this subfield; formal tests would strengthen but their absence is not a flaw.
- **Strength Finder: "Encryption-free deployment advantage"** — partially qualified by the terminology concern but the core advantage (eliminating per-image key management and cryptographic primitives) is real and retained in the Strengths section.

## Novel Insights
The connection between binary watermark coding and spherical t-designs is genuinely underexplored. The insight that 3-wise independence of XOR-mixed bits (Theorem 3.1) can be leveraged to construct a spherical 3-design (Theorem 3.2) provides a clean algebraic bridge between discrete coding theory and continuous geometric distributions. This opens a direction for distribution-preserving watermarking that is structurally different from both cryptographic pseudorandomness and pattern-injection approaches.

## Suggestions
- Recalibrate the abstract, introduction, and conclusion to accurately reflect the theoretical result: the method produces noise matching N(0, I) up to third-order moments via spherical 3-design, which is empirically indistinguishable under standard metrics. Remove claims of "exact" Gaussian recovery.
- Add an inversion baseline on unwatermarked images to quantify the irreducible error floor from DDIM inversion.
- Replace "encryption-free" throughout with "cryptographic-primitive-free" or "eliminating per-image cryptographic overhead."

## Calibration Notes

**Round 1 (Bracketing):**
- HexshmBu0P (5.33, "A Recipe for Watermarking Diffusion Models", Reject): Recipe-based watermarking with limited novelty, poor image quality. Our paper is clearly stronger.
- ll2nz6qwRG (5.83, "Hidden in the Noise", Accept): Two-stage noise-based watermarking, limited evaluation scope. Our paper is somewhat stronger.
- j7b4mm7Ec9 (7.60, "Lightweight Deep Watermarking", Reject): Well-executed novel contribution. Our paper is weaker due to the theoretical gap.

**Initial bracket: 5.8–7.0.**

**Round 2 (Narrowing):**
- ll2nz6qwRG (5.83, WIND, Accept): Re-read. Limited to single model, incomplete evaluation. Our paper is clearly stronger.
- jlhBFm7T2J (6.50, PRC Watermark, Accept): Direct baseline. Our paper demonstrates substantial improvements over PRC in robustness, speed (~30,000×), and capacity scaling, while matching undetectability. Both papers have nuanced theoretical issues flagged by reviewers. Our paper is somewhat stronger.
- 1IwoEFyErz (6.00, Shallow Diffuse, Reject): Limited contribution, poor presentation. Our paper is clearly stronger.
- f8S3aLm0Vp (6.50, DIAGNOSIS, Accept): Different topic (unauthorized data usage detection), not directly comparable.

**Final score: 7.0** — above the 6.50 PRC Watermark baseline due to demonstrated practical improvements in robustness, computational efficiency, and capacity scaling while maintaining comparable undetectability and theoretical depth.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>