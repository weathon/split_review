Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper introduces PianoMotion10M, a large-scale dataset of 116 hours of piano performance videos with 10 million annotated 3D hand poses (MANO model), paired with audio and MIDI—the first resource of this scale for music-driven hand motion generation. It also presents a baseline model that disentangles hand position prediction from gesture generation (via a diffusion model), a set of evaluation metrics (FGD, WGD, PD, Smoothness, FID), and benchmark results against re-implemented prior methods.

## Strengths

- **First large-scale dataset integrating piano music with continuous 3D hand motion.** PianoMotion10M provides 116 hours/10M frames, which is over 20× larger than the prior largest music-motion dataset (AIST++ at 5.19 hours), as shown in Table tab:dataset-compare. The paper also includes MIDI annotations, which no prior music-motion dataset provides. This scale directly supports the paper's core claim that existing data is insufficient for this task.

- **Baseline model outperforms adapted prior methods, particularly on overall motion fidelity.** The best configuration (Our-Large, HuBERT+Transformer) achieves FID 3.281 vs. EmoTalk's 4.645 and LivelySpeaker's 4.157 (Table tab:benchmark)—a meaningful improvement of 29% over the strongest baseline on the holistic double-hand metric.

- **Principled two-stage architecture with clear ablation studies.** Disentangling hand position prediction (regressor) from gesture generation (diffusion) avoids the "static average pose" failure mode visible in EmoTalk's outputs (Figure 5). The paper systematically ablates audio features (Wav2vec vs. HuBERT), decoders (SSM vs. Transformer), model scales (Base vs. Large), and denoising steps (5–1000, Table tab:abl), providing clear evidence for design choices.

- **Task-specific evaluation metrics covering multiple dimensions.** The benchmark introduces FGD/WGD for single-hand gesture fidelity, PD for positional accuracy, and a relative-acceleration Smoothness metric that corrects for the static-motion confound (lines 240–241), going beyond generic motion metrics.

## Weaknesses

### Major

- **Baseline trained on only 2 of 14 subjects, but the paper does not clarify whether the quantitative results reflect this.** Section 4.3 (line 212) states: "Specifically, our model is trained by subject \texttt{1467634} and subject \texttt{66685747}, which have the similar piano keyboard layout." The dataset contains 14 subjects with highly diverse playing styles and keyboard layouts. The train/val/test split (7,519/821/8,399 clips) is defined over the full dataset, but the baseline reportedly uses only two subjects. If the benchmark results in Table tab:benchmark come from this two-subject training, they are not representative of what the full dataset supports, and the benchmark is not properly instantiated as a standardized evaluation. If they come from full training despite what Section 4.3 says, the paper is critically unclear. Either way, this ambiguity and the two-subject limitation are the most significant issues in the paper. The authors must clarify: (a) which training set produced the results in Table tab:benchmark, and (b) if only two subjects were used, provide results from the full training split or justify why this is a valid benchmark setup.

- **No quantitative validation of annotation accuracy.** The annotation pipeline is entirely automatic (MediaPipe → HaMeR → Hampel filter → interpolation → Savitzky-Golay). The paper mentions that annotations are "manually checked to ensure their quality" (line 139) and that MIDI files with "high discrepancies are adjusted" (line 133), but provides no numbers: what fraction of frames was checked, what was the estimated keypoint error, what was the MIDI note-level accuracy? For a dataset contribution of 10M frames, the degree of noise and systematic error in the pose annotations directly determines whether downstream models learn actual piano hand motion or annotation-pipeline artifacts. Some form of quantitative quality assessment is essential for the dataset to be credible.

### Minor

- **No error bars, confidence intervals, or significance tests on any metric.** Differences between methods are sometimes very small (e.g., right-hand WGD of 0.244 for multiple configurations in Table tab:benchmark). Without uncertainty quantification, it is impossible to tell whether reported improvements reflect real differences or random variation. For a benchmark paper, this is a standard expectation.

- **Missing simple baselines to calibrate metric scales.** The only baselines are re-implementations of EmoTalk (talking head) and LivelySpeaker (co-speech gesture), both from different tasks. Simple baselines such as predicting the mean pose, linear interpolation from audio features, or nearest-neighbor retrieval from the training set would establish floor/ceiling values and make the metric magnitudes interpretable (e.g., "Is FGD=0.35 good or mediocre?").

- **Subject imbalance is documented but not analyzed.** Subject 66685747 contributes 535 videos (3.5M frames), while several subjects contribute fewer than 20 videos (e.g., subject 494725787 has 1 video/7,488 frames). The paper acknowledges this distribution (Table tab:stat) but does not discuss its impact on the benchmark, the risk of models overfitting to dominant subjects, or whether the train/val/test split ensures subject-independent evaluation (the paper reports total clips per split but does not clarify whether subjects are split across splits).

- **No details on the FID auto-encoder.** The paper states "We pre-train an auto-encoder to project motion sequence onto a latent space for double hands" (line 228) but gives no information about its architecture, training data, reconstruction quality, or latent dimensionality. This makes the FID numbers difficult to interpret or reproduce.

- **Annotation pipeline effects not quantified.** The paper describes Hampel filtering, linear interpolation for gaps <30 frames, and discarding of short-duration detections, but does not report what fraction of frames was flagged as outliers, interpolated, or discarded. This makes it hard to assess the pipeline's impact on motion realism.

### Trivial

- **PD values (e.g., 0.03–0.04) are presented without reference to the units or scale of hand positions**, making them difficult to interpret.
- **The paper does not discuss where the baseline fails** (e.g., fast passages, hand overlaps, unfamiliar fingerings), which would improve transparency.

## Nice-to-Haves

- **Human evaluation of motion quality.** A small perceptual study (e.g., preference judgments between generated and GT motions) would strengthen the case that the automatic metrics align with human perception. Not standard for all motion-generation papers but would elevate this benchmark.
- **Per-subject generalization analysis.** Reporting per-subject metrics would reveal whether performance varies widely across the imbalanced subject distribution and clarify model robustness.
- **Ethical/privacy statement.** Since videos of identifiable performers from Bilibili are used, a statement about consent, platform terms, or privacy protections would be appropriate.
- **Ablation removing the position predictor** (e.g., training the diffusion model to predict both position and gesture jointly) to more directly isolate the position predictor's contribution.
- **Discussion of whether Hampel filter parameters** (window size 20) and Savitzky-Golay smoothing might attenuate genuine rapid articulations (e.g., trills, staccato runs).

## Removed Points

These points were flagged by the critic but are removed or downgraded per the review guidelines:

1. **"Smoothness metric favors slow, static motions"** — The paper already addresses this by using *relative acceleration* (difference from ground-truth acceleration, lines 240–241), not absolute acceleration. Static motions with nonzero GT acceleration would incur a large penalty. This is a misreading of the paper's formulation and is removed.

2. **"No evidence metrics correlate with human judgment"** — Human validation of new metrics is a high bar not standard in motion-generation benchmark papers. Moved to Nice-to-Have.

3. **"The large model has 557M parameters, risk of overfitting"** — Speculative without evidence of actual overfitting, especially given the 10M-frame dataset. Overfitting risk is already implicitly covered by the two-subject training concern. Removed as redundant.

4. **"The Hampel filter and Savitzky-Golay smoothing may remove genuine rapid movements"** — A reasonable technical question but presented without analysis or evidence. Moved to Nice-to-Have.

## Novel Insights

The harsh critic's most valuable observation is the tension between the paper's two-subject training setup and its benchmark aspirations: a benchmark is only as good as its standardized instantiation, and training a baseline on 2/14 subjects while defining a full 14-subject train/val/test split creates a mismatch that undermines comparability. Beyond the paper's own contributions, the key meta-point across the reviews is that dataset-scale contributions require dataset-quality validation—scale alone is not sufficient evidence of utility without quantitative error analysis on a held-out validation subset.

## Suggestions

1. **Clarify and correct the training setup.** State explicitly whether Table tab:benchmark results come from the two-subject training or the full training split. If the former, train the baseline on the full training set (7,519 clips) and report those results. If computational constraints are a concern, acknowledge them and provide results on a balanced subset.
2. **Report annotation accuracy.** Annotate at least a few hundred frames manually (or compare against an alternative method) and report per-keypoint 3D error in meters or pixel reprojection error. Similarly, report note-level accuracy of MIDI transcription against manual verification.
3. **Provide error bars** (e.g., 95% CI via bootstrapping over clips) for all metrics in Table tab:benchmark.
4. **Add simple baselines** (mean pose, nearest-neighbor retrieval) to calibrate metric scales.
5. **Report the fraction of frames removed/interpolated** by the annotation pipeline's filtering steps.
6. **Clarify the train/val/test split policy** regarding subject identity—are clips from the same subject allowed across splits?
7. **Add a limitations section** discussing failure cases, subject imbalance effects, and generalization to unseen keyboard layouts.

## Score and Decision

The PianoMotion10M dataset itself is a large-scale, well-motivated contribution that addresses a genuine gap. However, the paper is significantly weakened by two issues: (1) the baseline is trained on only 2 of 14 subjects with no clarification of whether the benchmark results come from this limited setup, and (2) the annotation pipeline lacks any quantitative accuracy validation. These are structural issues for a paper that positions itself as both a dataset release and a benchmark. The dataset's potential value is real, but in its current form the benchmark contribution is not yet credible. A major revision addressing the training setup ambiguity, adding annotation validation, and providing error bars would substantially strengthen the paper.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>