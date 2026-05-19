Now I have all the verification data. Let me compose the final consolidated review.

---

## Summary

This paper proposes RGANet, the first method designed for concealed object detection (COD) in lensless imaging. The method incorporates an optical-aware feature extraction (OFE) module using learnable Wiener filtering, two region gaze modules (RGMs) that collaboratively exploit spatial and frequency cues, a region amplifier (RA) that warps features to magnify object regions, and a hierarchical feature decoding (HFD) module. The authors also contribute two new datasets (SLCOD simulated, DLCOD real) as benchmarks. Experiments show consistent improvements over adapted baselines across four metrics on both easy and hard test sets.

## Strengths

- **Novel problem formulation.** The paper is, to the best knowledge of the authors and as verified by the related work, the first to investigate COD for lensless imaging. Prior lensless work addresses general segmentation (Yin et al. 2022) or recognition (Pan et al. 2021a), not the specific COD setting. This reframing is grounded: lensless measurements lack visual semantics, making standard COD methods inapplicable without adaptation.

- **Consistent quantitative improvements.** On Test-Easy, RGANet reduces mean absolute error (ℳ) by 23.3% and improves weighted F-measure (Fβ^w) by 7.0% relative to the best prior method (LOINet); on Test-Hard, gains are 19.7% and 13.0% respectively (Table 1). The improvement holds across all four metrics and across two test sets with different difficulty levels.

- **Comprehensive ablation with individual component verification.** Each of the four key components (OFE, RA, HFD, RGM with FCE) is ablated in Tables 2–3, and each removal degrades performance. The ablations cover different configurations (single vs. dual RGM, with/without FCE, with/without RA, with/without HFD, with/without OFE), supporting the claim that each module contributes.

- **Learnable Wiener-filter design with a clear rationale.** The OFE module (Section 3.2) uses a learnable PSF A_θ and regularization K_θ trained jointly with the downstream network, explicitly *not* for human-viewable reconstruction but for task-relevant feature extraction. This is a principled departure from prior lensless feature extraction methods (Khan et al. 2022; Boominathan et al. 2020).

- **Adaptive frequency separation via a learnable threshold.** The FCE component (Section 3.3) introduces a learnable radius r to separate high- and low-frequency DCT components, unlike prior COD methods that use fixed cutoffs. Table 3 shows that the learned balance (r=5) outperforms the extremes (r=1, r=7) and removal, validating the design choice.

## Weaknesses

### Fatal

None.

### Major

- **No experimental variance reported.** All quantitative results (Tables 1–3) report single-run numbers with no error bars, standard deviations, or mention of multiple seeds. Several ablation comparisons involve small differences (e.g., Table 2, Test-Hard ℳ: 0.057 with HFD vs. 0.053 without — a 0.004 gap). Without variance estimates, it is impossible to judge whether the reported improvements are statistically significant, which weakens the empirical support for the core claims. This is a standard rigor expectation for deep learning papers.

- **Potential test-set contamination from dataset overlap unaddressed.** The paper acknowledges 326 overlapping data pairs between their DLCOD dataset and the dataset from Yin et al. (2022), both drawn from the same ImageNet subset (Section 4.1). However, the paper does *not* state whether these overlapping pairs are excluded from the test splits (Test-Easy, Test-Hard). If overlapping images appear in the test sets while LOINet (from Yin et al. 2022) was trained on overlapping data, RGANet's advantage over LOINet could be artificially inflated. This must be explicitly clarified.

### Minor

- **RA module's inverse mapping is underspecified.** Equations (5)–(6) define a sampling function using inverse mappings M_x^{-1} and M_y^{-1}, described only as "indicate the inverse operation of Eq. (5)." The paper does not explain how these inverses are computed (for arbitrary cumulative marginal distributions, they are not analytically invertible in closed form), how the warping is made differentiable for backpropagation, or whether bilinear interpolation (standard for such operations) is used. This gap prevents independent reimplementation and weakens the methodological description.

- **HFD module's attention mechanism is not specified.** Section 3.5 states the module "enhances the object regions with an attention mechanism" without saying whether this is channel attention, spatial attention, self-attention, or something else. For a core component whose removal degrades performance (Table 2 #8), the description is overly vague.

- **FCE adaptive threshold ablation is limited.** The learnable parameter r is only tested at three discrete values (1, 5, 7) plus removal (Table 3). While r is described as learnable during training, the ablated configurations test fixed values rather than demonstrating that the learned r at convergence outperforms a fixed optimal value. The ablation is thin for what is presented as a key innovation.

- **High parameter count (59M) without deployment discussion.** RGANet has 59M parameters (Table 1), substantially more than LOINet (3.4M). The paper notes this is "intermediate" among compared methods but does not discuss whether this complexity is compatible with the low-cost, miniature form factor that motivates lensless cameras in the first place.

### Trivial

None.

## Nice-to-Haves

- The RA module could benefit from an ablation against a simpler crop-and-resize baseline to isolate the benefit of the specific warping mechanism, beyond the current "remove RA" baseline.
- A limitations section discussing failure cases (e.g., when RA amplifies wrong regions, or when frequency cues mislead for texture-matched objects) would strengthen the paper.
- The baselines are evaluated with the authors' OFE module replacing their native feature extraction (e.g., LOINet's SFL). While this ensures a controlled comparison, it could be complemented by evaluating baselines with their own feature extraction to test whether the OFE module is broadly beneficial or specialized to RGANet.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **Dataset availability (Harsh Critic #1).** The critic states the paper does not state public release plans. Per evaluation guidelines: criticisms questioning the release status or availability of datasets cited in the paper are removed. The dataset is cited as existing, and its availability status is not an admissible weakness in this review.

- **OFE module physical consistency (Harsh Critic, §3.2 note).** The critic questions whether the learned PSF A_θ remains "physically consistent" with the actual PHlatCam PSF. The paper explicitly states (Section 3.2) that the OFE module "does not act as visual reconstruction to satisfy the requirements of the human eye but rather collaborates with the back-end design to reason about the semantics." The module is intentionally unconstrained; this is by design, not a flaw.

- **"Statistically clear" strength phrasing (Strength Finder strength #2).** The Strength Finder claims the improvement margins are "statistically clear." Since no variance estimates are reported (verified weakness), this claim is unsupported. The raw numerical improvements remain as reported; the strength is retained but rephrased without the statistical claim.

- **Strawman: RA using I_OFE vs. deeper features (Harsh Critic, §3.4).** The critic questions why the RA takes I_OFE (Wiener-filtered measurement) rather than deeper features. The RA sits between two RGMs and operates on the output of the OFE module. This is a deliberate architectural choice; criticizing it without evidence that deeper features would improve performance is speculative and not grounded in the paper.

## Novel Insights

The most interesting cross-cutting theme from the reviews is the tension between the paper's thorough component-level ablation (Tables 2–3 verify every module) and the absence of experimental replication (single runs, no error bars). The paper's claims rest heavily on modest metric differences in the ablations — differences that could plausibly fall within run-to-run noise. This tension is compounded by the unresolved test-set overlap ambiguity, which specifically threatens the comparison against LOINet (the strongest baseline). If the authors clarify both issues (confirm test-set decontamination and report multi-run statistics), the paper's experimental foundation would be substantially stronger. Conversely, if the overlap does include test-set images and the small ablation gaps are within noise, the core claims would be undermined rather than supported.

## Suggestions

1. **Report multi-run statistics.** Run the full method and key ablations (at minimum: full model, no RA, no RGM) with 3–5 random seeds and report mean ± std for all metrics in Tables 1–3. This is the single most impactful improvement to the paper's credibility.
2. **Clarify test-set decontamination.** State explicitly whether any of the 326 overlapping data pairs between DLCOD and Yin et al. (2022) appear in Test-Easy or Test-Hard. If they do, report results with those pairs excluded.
3. **Specify RA implementation details.** Describe how M_x^{-1} and M_y^{-1} are computed in practice, how differentiability is achieved, and whether bilinear interpolation is used. A reference to the prior work (Zheng et al. 2019) is insufficient without specifying what adaptation is made.
4. **Specify HFD attention type.** Provide the type of attention used in the HFD module (channel, spatial, self-attention, etc.) and a brief architectural description.
5. **Add a limitations paragraph.** Briefly discuss scenarios where the method might fail (e.g., objects that match background texture, RA amplifying false positives).

## Score and Decision

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>