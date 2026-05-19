- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 5, 5, 5
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

MMEval proposes a benchmark for evaluating image-to-video (I2V) generation models on motion quality, moving beyond holistic metrics (FVD, CLIP-Temp) to category-specific evaluation. The paper categorizes motion into linear (fluid and rigid-body), rotational, and oscillatory types, and designs physically motivated metrics for each (FC-Score, CS-Score, q-Score, LF-Score, P-Score, Dir-Score, Speed-Score). Evaluating five recent I2V models, the authors find that no model excels across all motion types—some handle fluid motion well but fail on rigid-body linear motion or large oscillations. The curated dataset of ~1,000 image-video pairs and ~5,200 prompt-image pairs will be publicly released.

## Strengths

1. **First category-specific motion quality evaluation for I2V generation.** The paper moves beyond single-number "motion quality" scores by defining five distinct, physically motivated metrics tied to specific motion types (FC-Score for fluid constancy, CS-Score for rigid-body consistency, q-Score for rotation, LF-Score for low-frequency oscillations, P-Score for periodicity). This granularity is absent from existing benchmarks like EvalCrafter and VBench (Section 4.2.1).

2. **Clear experimental evidence that no model handles all motion types.** Tables 3–7 show consistent cross-model variation: FluidAnimation (GAN) dominates fluid motion but fails on rigid bodies; DynamiCrafter leads on rotation but scores poorly on linear rigid motion; all models fail on large oscillations (P-Score ≈ 0 except PikaLabs). This directly supports the paper's central finding that "different models perform better for different motion types, but none of them successfully model all motion-types" (Section 5.1, Section 6).

3. **Well-controlled dataset design that isolates object motion.** The data collection constraints (static camera, single object of focus, object-driven motion, Section 3.1) ensure that the metrics measure the object's motion rather than camera movement or background changes, enabling cleaner attribution of failures to the model's motion modeling ability.

4. **Quantitative evidence of direction and speed failures.** Table 8 reports Dir-Score ≈ 0.5 across models, showing they produce the same direction regardless of prompt. Table 9 gives low Speed-Score values (e.g., 0.2 for OpenSora on Linear-Fluids), concretely supporting the claim that "all models struggle to understand and model motion direction and speed" (Section 5.2–5.3).

5. **Use of a task-specific GAN baseline as a validation tool.** Including FluidAnimation (Mahapatra & Kulkarni, 2022)—a model trained explicitly for constant fluid flow—provides a sanity check: its FC-Score exceeds ground truth, correctly signaling "overly smooth" generation and confirming that the metric captures smoothness (Table 3, Section 5.1).

6. **Visual evidence supporting the periodicity metric.** Figures 1 and 2 show clear repetitive patterns in ground-truth distance matrices for large oscillations and their absence in generated videos, providing intuitive justification for the P-Score approach (Section 4.2.1).

## Weaknesses

### Fatal
None. The paper's core claims—that category-specific metrics reveal granular model weaknesses and that no current model masters all motion types—are supported by convergent evidence across multiple independent metrics and models.

### Major

1. **FC-Score and LF-Score conflate smooth motion with no motion, and this is not remedied.** The FC-Score measures the fraction of FFT energy in the zeroth frequency component, which is maximized both by perfectly constant optical flow (smooth motion) and by zero flow (a static video). The paper acknowledges this for FC-Score ("it is crucial to also check motion magnitude, as a still video may exhibit a high FC-Score despite no actual motion") but implements no such check. For LF-Score (low-frequency energy up to 25%), the same problem exists and is not even mentioned. While the ground-truth comparisons mitigate this somewhat, the scores remain ambiguous without a separate motion-magnitude filter, and the paper's interpretations of "low FC-Score suggests flickering" could be confounded by models that generate near-static outputs.

2. **No human validation of any motion-specific metric.** None of the five proposed metrics (FC-Score, CS-Score, q-Score, LF-Score, P-Score) is validated against human perceptual judgments. For a benchmark intended to guide model development, it is essential to establish that the metrics correlate with what humans perceive as good motion quality. Prior benchmarks like VBench and EvalCrafter include at least some human agreement studies. Without any correlation analysis—not even a small-scale study—the reader has no evidence that a higher FC-Score corresponds to more natural fluid motion, or that q-Score captures anything humans notice in rotational motion. This is the most consequential gap in the paper.

### Minor

3. **q-Score's complementary-bin assumption for rotation is not analyzed for robustness.** The metric assumes that for any pixel moving in direction θ, there is a complementary pixel moving in direction −180°+θ, leading to equal histogram counts in complementary bins. This holds strictly only for symmetric objects with a centered axis of rotation and rigid-body motion. Real objects tested (ferris wheels whose cabins stay upright, ceiling fans with asymmetric blades) can violate this assumption. The paper does not analyze how sensitive the metric is to these violations. However, the empirical observation that ground-truth videos achieve low q-Scores suggests it works reasonably well in practice.

4. **P-Score's SVM classifier may be confounded by generation artifacts rather than measuring periodicity.** The metric trains an SVM on LBP features of distance-matrix visualizations from ground-truth videos and applies it to generated videos. Differences in resolution, blur, flickering, or color shifts between ground-truth and generated videos will alter the LBP features of the distance-matrix image, so the classifier could partially learn to distinguish "clean ground-truth appearance" from "artifact-ridden generation appearance" rather than periodicity. The paper's validation using PikaLabs (which scores 1) is suggestive but does not fully resolve this confound.

5. **Speed-Score is coarse and conflates prompt-following with speed modeling.** The metric assigns a binary 0/1 per set of three speed-conditioned videos, checking only the ordinal relation (slow < moderate < fast). It cannot distinguish models that produce small, barely perceptible speed differences from those that produce large, meaningful ones. Moreover, a model that ignores the speed prompt entirely will score 0, but this failure is about text-conditioning rather than motion modeling per se.

6. **No variability or significance information reported.** With 50 samples per object type, the paper reports only mean scores without standard deviations, confidence intervals, or statistical tests. This makes it impossible to assess whether observed differences between models (e.g., "DynamiCrafter leads on rotation") are reliable or within the noise.

7. **No analysis of segmentation failure rates or selection bias.** The paper notes that videos failing object detection (GroundingDINO+SAM) are excluded, but does not report how many are excluded per model or per object type. If certain models systematically fail to preserve recognizable objects (and are thus excluded), this introduces a selection bias that favors models producing clearer object appearances rather than better motion.

### Trivial

8. **Using "cinemagraph" in every prompt may bias model behavior.** The prompt template begins "a cinemagraph of object moving…" Cinemagraphs conventionally depict a mostly static scene with a small, looping moving region, which may not align well with evaluating full-object motions like a swinging pendulum or a rotating ferris wheel.

## Nice-to-Haves

- Add a motion-magnitude filter (e.g., mean optical flow magnitude threshold) to both FC-Score and LF-Score, so that still videos are penalized rather than rewarded.
- Conduct a small-scale human validation study (e.g., 50 clips per motion type, 5 raters) correlating metric rankings with human preference for at least FC-Score, CS-Score, and q-Score.
- Replace the SVM-based P-Score with a direct, interpretable periodicity measure such as autocorrelation of the distance matrix along its diagonals.
- Report standard deviations or confidence intervals for all metric scores.
- Analyze q-Score's sensitivity to object asymmetry and axis location using synthetic rotational videos.

## Removed Points

*These points were flagged by reviewers but are removed per the consolidation rules. They should be treated with caution.*

- **"Code and dataset not yet released"** — Hard rule: remove any criticism questioning the release status or availability of cited entities. The paper states these will be released.
- **"1,000 vs 900 videos discrepancy"** — The critic counted 18 object types from text mentions, but Section 5.1 (line 176) states "20*50" generated videos for motion smoothness, confirming 20 object types × 50 = 1,000. The critic's count was incomplete (missing 2 object types likely shown in Table 1, which is an image). Factually incorrect; removed.
- **"Approximately 5,000 image-prompt pairs is imprecise"** — The paper says "approximately 5,000" in the abstract and "5,200" in the detailed description. This is a completely reasonable approximation; not a real inconsistency.
- **"First-of-its-kind is overstated"** — A minor wording nitpick. In context, the claim refers to classifying generated videos by motion type for category-specific evaluation, which is original relative to existing benchmarks.
- **"Only five models evaluated"** — The critic themselves notes this is "not a requirement for acceptance."
- **"Missing discussion of failure cases for segmentation"** — While this could be nice to have, it's elevated as a formal weakness when the paper already acknowledges the exclusion criterion. Kept in Minor #7 instead as a reduced concern.

## Novel Insights

The harsh critic and strength finder together surface a tension that the paper itself does not fully resolve: the metrics are physically motivated and produce internally consistent results (e.g., the GAN baseline expectedly overshoots ground truth on FC-Score, PikaLabs expectedly scores 1 on P-Score), yet none of them have been validated against human perception. This means the paper provides a *diagnostic tool* whose internal logic is sound but whose external validity is untested. The most productive path forward is not to discard the metrics but to add the missing human-calibration step. The critic's concern that FC-Score con flates smooth motion with no motion is real but partially self-limiting: in practice, models that produce static videos would also score poorly on CLIP-Temp and would produce FC-Scores higher than ground truth (like the GAN), which the paper already interprets as unrealistic. None of the weaknesses fundamentally invalidates the observation that different models fail at different motion types—a finding that holds across multiple independent metrics and is the paper's primary contribution.

## Suggestions

1. **Highest priority:** Add a motion-magnitude filter to FC-Score and LF-Score, and conduct a small human validation study (even 50–100 comparisons) to calibrate at least 2–3 of the proposed metrics against perceptual judgments.
2. Report standard deviations for all tabulated results so readers can assess the reliability of model rankings.
3. Report how many videos per model were excluded at the segmentation stage to surface potential selection bias.
4. Replace the SVM-based P-Score with a more interpretable periodicity measure (e.g., diagonal autocorrelation of the distance matrix), or at minimum add a feature-level analysis to rule out the artifact confound.
5. Clarify the object type count: verify whether there are 20 object types (as implied by line 176) and enumerate them explicitly in the text rather than only in Table 1.
