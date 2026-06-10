## Summary

X-Gen addresses cross-view ego-centric video prediction: given an exo-centric video, the first ego-centric frame, and a text instruction, it generates future ego-centric frames. The method has two stages — (1) a cross-view HOI mask prediction model with an ego-exo memory attention module that anticipates future ego-centric hand-object masks from exo-centric observations, and (2) a video diffusion model conditioned on those predicted masks. An automated pipeline combining EgoHOS, 100DOH, Sapiens, and SAM-2 generates pseudo HOI masks without manual annotation. On Ego-Exo4D and H2O, X-Gen outperforms single-view video prediction baselines across SSIM, PSNR, LPIPS, and FVD.

## Strengths

- **Two-stage design validated by informative ablations.** Tables 2–4 systematically isolate each design choice: HOI masks outperform hand-only or object-only masks; the combined ego+exo memory attention beats either variant alone; HOI masks provide more effective conditioning than text instructions alone. These ablations are clean and directly support the paper's architectural claims.

- **Automated HOI annotation pipeline with evidence for temporal consistency.** The pipeline (EgoHOS + SAM-2 tracking for ego, 100DOH + Sapiens + SAM-2 for exo) is clearly described in Sec. 2.4. Table 6 shows that SAM-2 tracking (which enforces temporal consistency) significantly improves downstream generation quality compared to per-frame EgoHOS alone — concrete evidence that the pipeline design matters.

- **Zero-shot transfer to H2O without re-training.** Table 1 (right) shows X-Gen achieves 290.6 FVD on H2O vs. 428.7 for the next-best baseline (ConsistI2V), despite domain shift across action categories, environments, and objects. This is the strongest evidence that HOI-centric modeling aids generalization.

- **Intellectual honesty in limitations.** The paper explicitly shows a failure case (complex hand movements, Fig. 5 last row) and provides an oracle comparison (X-Gen w/ future masks) that locates the bottleneck in mask prediction rather than generation — a useful diagnostic that strengthens rather than weakens the paper.

## Weaknesses

### Fatal
None.

### Major

- **Headline comparison conflates the benefit of having exo information with the benefit of HOI-mask modeling (Table 1).** X-Gen receives the full exo-centric video, exo HOI masks, and predicted ego HOI masks; the baselines (SVD, Seer, DynamiCrafter, SparseCtrl, SEINE, ConsistI2V) receive only the first ego frame and text. Superiority is expected from access to strictly more information, but this does not validate the paper's central claim — that *explicitly predicting and conditioning on HOI masks* is the driver. Table 5 partially addresses this by showing the two-stage HOI approach outperforms single-model alternatives that directly use exo-RGB or exo-masks. However, this ablation is relegated to a secondary table and does not appear in the main comparison. The paper needs a direct apples-to-apples comparison where a method also receives exo information but does *not* use HOI-mask prediction, evaluated under identical conditions in the main results table.

- **No quantitative comparison against the most directly related cross-view methods (Luo et al., 2024a,b).** The paper identifies Luo et al. (2024b) as performing exo-to-ego image generation using hand pose guidance, and Luo et al. (2024a) as performing cross-view video generation (ego→exo). These are the closest prior approaches to X-Gen's task. While the task definitions differ (image vs. video, direction), the absence of any quantitative comparison means the paper's positioning as an advance in *cross-view generation specifically* (rather than simply outperforming single-view methods that lack exo data) is unsubstantiated.

- **No variance reporting or statistical significance.** Diffusion models are stochastic and video prediction metrics (especially FVD) exhibit high variance. Every table reports single point estimates without error bars, confidence intervals, or even mention of multiple runs. This is particularly problematic for the ablation studies (Tables 2–6), where some margins are modest and could be within noise range. For a paper making empirical claims at a top venue, this is a meaningful gap.

### Minor

- **Ambiguity in mask-prediction evaluation.** The paper states: "We sample 1,000 video clips from the validation set, from which we select 500 video clips and annotate them with HOI masks to evaluate the performance of the mask prediction model" (Sec. 3). It is never specified whether these 500 clips were manually annotated or annotated via the automated pipeline. If the latter, the evaluation measures agreement between two automated processes rather than actual segmentation accuracy, and the claim that the pipeline can "replace manual annotation" is not independently validated.

- **Key implementation details underspecified.** (a) The α annealing schedule for balancing ego-memory and exo-memory attention is described only as "annealing from 1.0 to 0.0 at training stage" — no schedule type (linear, cosine, step) or epoch count is given, precluding reproducibility assessment. (b) The resolution mismatch between the mask prediction model (480×480) and the diffusion model (256×256) is not discussed — how masks are resized and whether downsampling loses the fine-grained HOI detail that the masks are supposed to provide is unaddressed.

- **Limited action/scene scope.** Only cooking scenarios from Ego-Exo4D are used for training. While the H2O zero-shot evaluation partially addresses generalization to tabletop activities, the paper does not discuss whether the approach would extend to non-HOI-heavy settings (e.g., locomotion, social interactions, navigation) where the "hands and objects are the primary signal" assumption may break down.

### Trivial

- The paper samples 16 frames from ~1-second clips but does not explicitly state the frame rate, making it unclear whether this is 16 fps or some other configuration.

## Nice-to-Haves

- **Temporal consistency metrics for generated video.** Given that the HOI masks are specifically designed to provide structural guidance across frames, evaluating temporal coherence (e.g., warping error, flicker metrics) would strengthen the claim that the masks improve consistency, not just per-frame quality.
- **Human evaluation.** The paper relies entirely on automated metrics. A small-scale perceptual study (e.g., "which video has more realistic hand-object motion?") would add weight, especially given the known limitations of FVD on small/domain-specific datasets.
- **Absolute mask prediction accuracy numbers as context for the generation bottleneck.** The oracle experiment in Fig. 5 shows that generation quality is bounded by mask prediction quality. Reporting the absolute IoU/CA/LE of predicted masks (not just relative comparisons across memory attention variants) would help readers assess the headroom for improvement.

## Removed Points

These points from the reviewers were considered but removed or demoted after verification against the paper:

- **Claim that Table 5 ablations use ground-truth masks.** The harsh critic asserted that "these ablated variants appear to use *ground-truth* HOI masks from future frames." The paper text says Table 5 replaces ego HOI masks with *exo-centric RGB frames or exo-centric HOI masks* — these are different conditions, not ground-truth ego masks. This criticism is not supported by the paper and is removed.
- **"Scalability advantage is unclear / just swapping dependencies."** The paper's pipeline is fully automated and demonstrably reduces reliance on manual annotation. Using foundation models as components does not negate the scalability benefit; this is a framing preference rather than a verifiable weakness.
- **Left/right hand distinction not clarified.** The paper explicitly states that "distinguishing between left and right hands does not yield further performance gain" (Table 2 analysis), and the pipeline generates 3-class masks (background/hand/object). This is sufficiently clear.
- **Frame rate / temporal coverage.** A trivial detail that does not affect the paper's evaluation.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the key tension (the headline comparison doesn't isolate what the paper claims to prove) but do not produce unanticipated insights beyond what follows naturally from that analysis.

## Suggestions

1. **Restructure the main results table to include an ablation that uses exo information without HOI-mask prediction.** Either add a row to Table 1 that feeds exo video into a standard video prediction model (e.g., concatenating exo latents or cross-attending exo features in the UNet), or promote the relevant comparison from Table 5 to the main table with the same evaluation protocol (same test set, predicted masks for all conditions). This would cleanly separate the benefit of "having exo information" from "the specific HOI-mask approach."

2. **Add a quantitative comparison against Luo et al. (2024b).** Even if the task differs (image generation vs. video prediction), adapting that method as a frame-by-frame baseline or discussing the gap in evaluation protocols would substantially strengthen the positioning.

3. **Report error bars** (standard deviations from 2–3 runs with different seeds) for at least the main results and key ablations (Tables 1, 2). This is standard practice for diffusion-based methods.

4. **Clarify the annotation protocol for the 500 evaluation clips** — state explicitly whether these were manually annotated or generated by the automated pipeline. If manually annotated, provide annotation protocol details.

5. **Specify the α annealing schedule** (type, duration in epochs) and discuss how mask resolution is handled when bridging 480×480 predictions into a 256×256 diffusion model.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>