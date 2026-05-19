- Decision: Reject
- Avg Score: 6.50
- Scores: 6, 5, 5, 10
I now have verified all claims against the paper. Here is the consolidated final review.

---

## Summary

SpaceSet is a large-scale simulated space-based image dataset for space situational awareness (SSA), containing 20,000 images at 4418×4418 resolution from four overlapping cameras. Images are generated using orbital dynamics (SGP4/TLE propagation) with a physical camera model incorporating Poisson-Gaussian noise, lens distortion, and star fields. The dataset spans observation distances from 19 km to 63,000 km across LEO/MEO/GEO regimes and includes automated bounding-box annotations derived from bearing angles. The paper also benchmarks detection (YOLO variants, DETR, Faster R-CNN) and tracking methods, showing that current SOTA algorithms struggle on this data.

## Strengths

- **Four-camera multi-view setup is a genuine novelty.** The paper simulates cameras at azimuth angles 0°, 75°, 90°, and 105°, extending the observation window. Table 1 confirms that every prior space-based dataset (SPARK, BUAA-SID, etc.) uses only a single camera. This is a concrete, verifiable contribution with clear practical value for multi-view SSA tasks.

- **Observation distance range is two orders of magnitude larger than prior datasets.** The paper reports distances from 19 km to ~63,000 km, while the closest competitor (SPARK) covers only 0.5–2 km. Figure 4 provides a histogram of the range distribution across four cameras, confirming coverage from LEO through GEO altitudes.

- **Benchmarking reveals that standard detectors perform poorly on SpaceSet, confirming the dataset poses non-trivial challenges.** YOLOv8m achieves only 0.598 mAP@50 (Table 2), tracking methods produce MOTA near zero or negative for IoU-based variants (Table 4), and Table 4's "Predict" column shows many models detect far fewer objects than ground truth. These results establish SpaceSet as a meaningful difficult benchmark, not a saturated one.

- **Automated annotation pipeline eliminates manual labeling error.** Bounding boxes are derived analytically from propagated orbital positions via bearing angles, rather than through human annotation. This is a principled design choice that ensures label consistency across the 20,000-image corpus.

## Weaknesses

### Fatal
None.

### Major

- **Annotation formula (Eq. 3, 4) is insufficiently defined.** The formulas use `focal.length` and `H.number` without defining what these terms physically represent, what units they carry, or how they relate to standard pinhole projection (which would be `x_pixel = f_x * tan(θ_x) + c_x`, where `f_x` is focal length in pixels). The expression `focal.length / H.number` cannot be verified as correct or incorrect because neither term is specified — `H.number` could be pixel pitch, a normalization factor, or something else. The y-formula uses a `-width` factor with unexplained sign. Because ground-truth bounding boxes are the core annotation, the community needs a clear, dimensionally consistent derivation to trust the labels. The paper should provide the full forward-projection chain (3D world → normalized camera → distorted → pixel) with all symbols defined. *Note: this is a documentation gap, not necessarily an implementation error — the simulator separately mentions using a pinhole model with Brown-Conrady distortion, so the actual projection is likely correct.*

- **The "realistic" claim is supported only by one qualitative comparison (Figure 1).** The paper asserts realistic photon-level imagery as its primary differentiator from SPARK and other datasets, yet the only evidence is a single figure showing one SpaceSet image, one SPARK image, and one real EGTN2 image with a brief caption noting "similar streaks" and "hot pixels." No quantitative validation is provided: no comparison of noise statistics (SNR distribution, hot pixel density, streak morphology), no cross-dataset transfer experiment (train on SpaceSet, test on real data), and no perceptual study. The dataset acknowledges this limitation in Section 6 ("images are still generated via simulations, which may not capture all the complexities"), but this admission does not exempt the paper from needing to support its central claim of *realism* with evidence. The dataset is still valuable as a challenging synthetic benchmark, but the framing as "bridging the simulation-reality gap" (Section 3.2, line 80) is unsubstantiated.

### Minor

- **Streak generation process is vaguely described.** The paper says "we overlap the images over the exposure time into one image" (line 73) without specifying whether this integrates multiple sub-frames, simulates continuous motion blur, or composites discrete instances. Since streak morphology (length, brightness gradient, trail shape) directly affects detection difficulty, a clearer description is needed.

- **"Typical values for general images" (30 dB SNR, 80 contrast) are stated without citation (line 134).** These values are presented as baselines to highlight SpaceSet's much lower SNR (1.94 dB) and contrast (4.67), but no reference is given. SNR and contrast vary enormously by imaging domain; the reader cannot verify this claim. The comparison would be more useful with context from astronomy or space-imaging literature specifically.

- **Test set evaluation details could be clearer.** The paper states "100 images from the SpaceSet-5000 dataset are selected for evaluation" (line 152). These are full 4418×4418 images (SpaceSet-5000 uses Camera 2 only), but since all processing uses 260×260 slices, it should be stated explicitly that evaluation is on sliced patches (the paper does say in Section 3.4 that the test set maintains the original 96% negative distribution via no pruning). This information is present but scattered; consolidating it would improve clarity.

- **No cross-dataset comparison with SPARK or other existing benchmarks.** The paper benchmarks models only on SpaceSet data. A cross-dataset generalization experiment (e.g., train on SpaceSet, test on SPARK or vice versa) would directly test whether SpaceSet's added complexity transfers to improved performance on other synthetic data — even a negative result would be informative. Without this, the reader cannot judge whether SpaceSet is "harder" due to meaningful realism or merely different labeling artifacts.

### Trivial

- Abstract says the tracker operates "in LEO, MEO, and GEO orbits" (line 4), which could be read as the observer platform being in all three regimes, while Section 3.1 clarifies the observer is in LEO at 500 km observing RSOs in all regimes. A small rephrasing would prevent confusion.

## Nice-to-Haves

- The paper could include an analysis of false positive sources in detection (stars misclassified as RSOs, hot pixels, etc.) to help users of the dataset diagnose failure modes.
- Training on a larger subset (e.g., SpaceSet-5000) in addition to SpaceSet-100 and showing scaling behavior would strengthen the benchmark section.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Data access statement / download URL missing.** The paper is an anonymized submission; omitting download links is standard for double-blind review. Removed per policy.
- **Simulator not open-sourced.** Describing the simulator without releasing it is acceptable for a dataset paper. Removed.
- **"Figures in appendix referenced but not present"** — the parser strips appendix content from all papers; these figures exist in the original submission. Removed per policy.
- **"Bounding boxes are axis-aligned for oriented streaks"** (raised as a weakness by harsh critic). This is a design choice, not an error. Axis-aligned boxes for streak-shaped objects are standard in SSA detection tasks. Removed as not a genuine weakness.
- **Strength Finder: "Bounding boxes are derived analytically from bearing angles... eliminating manual annotation error."** While the automated pipeline is a strength, the claim that Eqs. (3)–(4) constitute a correct/explicit description is undermined by the verified weakness that these formulas are insufficiently defined. Per the rule that "when a strength and weakness disagree, the weakness wins," this strength is removed.

## Novel Insights

None beyond the paper's own contributions. The harsh critic's dimensional-analysis concern about Eq. (3)/(4) is the most probing observation, but it reveals a documentation gap rather than a fatal implementation error. The strength finder correctly identified the multi-camera setup and extreme range coverage as genuine differentiators, while both reviewers converged on the thin realism validation as the paper's central vulnerability.

## Suggestions

1. **Fix and fully specify Eqs. (3) and (4).** Provide the complete projection chain: 3D world coordinates → camera frame → normalized pinhole projection (with pixel pitch and focal length in consistent units) → distortion → pixel coordinates. Define `focal.length`, `H.number`, and the roles of the `±0.5` and `±width` terms explicitly. If the formula in the paper differs notationally from the simulator's implementation, align them.

2. **Add at least one quantitative realism experiment.** Minimum viable options: (a) compare the distribution of streak lengths, SNRs, or background noise levels in SpaceSet against published values from NEOSSAT, DSCOVR, or (b) train a detector on SpaceSet-100 and test on a few real images (or RSONAR data) to measure transfer, even as a small-scale pilot. The paper acknowledges this need in its limitations section — acting on it would directly strengthen the core contribution.

3. **Provide a citation for the "typical values" claim about SNR (30 dB) and contrast (80),** or reframe the comparison without asserting an unsubstantiated baseline.

4. **Clarify streak generation:** state explicitly whether the 1-second exposure is simulated as continuous motion blur, sub-frame integration, or discrete temporal sampling.
