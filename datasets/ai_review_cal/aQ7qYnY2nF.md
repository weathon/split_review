- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3
Now I have a thorough understanding of the paper and all reviewer claims. Let me construct the final consolidated review.

---

## Summary

This paper proposes RL-RC-DoT, a reinforcement-learning-based method for controlling macro-block QP deltas in the x264 encoder to optimize compression for a downstream task (car detection or ROI encoding). The key innovation is that the policy requires no access to the downstream task model or ground-truth labels during inference—it operates purely on encoder-side statistics (MB-tree features). The method uses a hierarchical action space for scalability, a self-supervised reward that treats raw-frame task outputs as pseudo-ground truth, and an auxiliary macro-block reward prediction loss. Experiments on BDD100K show a 24.7% BD-rate reduction for car detection and 25.6% for ROI encoding over vanilla x264, with real-time inference speed (~30 FPS). A robustness experiment (training on YOLOv5-nano, testing on SSD and DeepLab segmentation) suggests the method does not severely overfit to the training detector.

## Strengths

1. **Operates under practically important constraints not jointly satisfied by prior work.**  
   The policy uses only encoder statistics (MB-tree features, Section 3) — no downstream task model, no segmentation map, no saliency map, and no ground truth — during inference. This is a genuine differentiator from Xie et al. (2022) (requires segmentation maps at encoding time) and Li et al. (2021) (per-frame optimization without cross-frame planning). The constraint set is well-motivated for streaming / edge deployment (Section 1).

2. **Hierarchical action space for scalable per-macro-block QP control.**  
   The RL agent operates on a lower-resolution action space that is upsampled to the original macro-block resolution (Section 3). This directly addresses the computational challenge of controlling a 30×20 QP delta matrix per frame and is a concrete architectural contribution over prior sequential per-block policies.

3. **Macro-block reward information auxiliary loss improves performance.**  
   The auxiliary head predicts per-block reward components, providing a more granular learning signal. The ablation study (Table 4) confirms that removing it degrades BD-rate for both car detection (–24.7% → –21.3%) and ROI encoding (–25.64% → –22.10%). This is clean, controlled evidence that the component earns its place.

4. **Robustness across task models and a related task.**  
   A policy trained on YOLOv5-nano detection achieves a BD-rate of –24.3% when tested with SSD detection and –14.2% on DeepLab car segmentation (Table 3). This shows the method preserves task-relevant information beyond the specific training detector, which is important for data-collection scenarios where the downstream model may change over time.

5. **Real-time inference speed.**  
   Evaluation runs at ~30 FPS on a Tesla V100 + Intel Xeon CPU (Section 4.3), meeting the real-time requirement for live streaming. This backs up the paper's practical deployment claim.

## Weaknesses

### Fatal
None.

### Major

1. **No comparison to any prior task-aware compression method.**  
   The paper compares only to vanilla x264, a task-agnostic encoder (Tables 1–3). The authors argue that prior task-aware methods have "fundamentally different" setups (Xie et al. requires segmentation maps at inference; Li et al. optimizes per frame; most did not release code), making direct comparison potentially misleading (Section 4.3). This justification is not unreasonable *as a reason to avoid an unfair comparison*, but it does not excuse the complete absence of any informed baseline. The paper could have (a) implemented a simplified adaptation of a prior method under compatible settings (e.g., a per-frame RL baseline without segmentation maps), or (b) constructed a non-RL oracle using the downstream task at inference to bound the improvement achievable with task-side information. Without *any* task-aware baseline, the headline claim — that RL-RC-DoT improves task-aware compression — is supported only against a task-agnostic encoder. Being better than x264 does not establish being better than or competitive with existing task-aware methods. This substantially limits the paper's ability to demonstrate its contribution relative to the state of the art.

2. **Data filtering procedure is opaque and may introduce selection bias.**  
   The paper states it "filtered out streams that exhibited trivial rate-task performance (RD) curves" and "excluded streams that showed zero precision across most target bit-rates" (Section 4.1). The number of excluded streams is not reported. Filtering on the quantity being evaluated (detection precision) is circular unless justified — videos with zero detection precision at low bitrates are genuinely challenging, and their removal could inflate the reported BD-rate improvements. The authors should (a) report how many streams were excluded, (b) characterize the excluded streams, and (c) show results with and without filtering to demonstrate that the improvement is not an artifact of selection. This is necessary for the reader to assess generalizability.

### Minor

3. **Reward formulation may encode biases against detecting objects that the raw detector misses.**  
   The detection reward is precision between detections on the raw frame (pseudo-ground truth) and detections on the reconstructed frame (Section 3, line 92). If the raw-frame detector misses objects (which is common for low-confidence instances), the agent is not rewarded for recovering them — and in fact could be penalized if such detections do not match the raw frame's output. The paper acknowledges the self-supervised nature of this approach but does not analyze this asymmetry or its potential impact on detection completeness. A sensitivity analysis comparing to ground-truth labels (where available during evaluation) or using a different reward formulation would clarify whether this bias is significant.

4. **Hierarchical action space is underspecified.**  
   The paper states the agent "operate[s] on a lower-resolution action space, which is subsequently upsampled to the original dimensions through interpolation" (Section 3). The resolution of the lower space and the interpolation method (bilinear? nearest-neighbor?) are not described. This detail is necessary for reproducibility and could affect the granularity and smoothness of QP control. 

5. **The "first" claim could be qualified more carefully.**  
   The paper states it is "the first task-aware video compression method that builds on top of existing encoders and does not require solving the task during inference" (Section 1, contribution 1). While this claim is largely defensible given the specific constraint set (no segmentation maps at inference, cross-frame temporal planning, standard encoder), Xie et al. (2022) and Li et al. (2021) share sufficient similarity that the claim would benefit from a more precise qualifier such as "to our knowledge" or a clear statement of which specific axes distinguish this work from its closest predecessors.

6. **No statistical significance reported for BD-rate improvements.**  
   Standard errors are given (e.g., ±1.38% for the main detection result), but no significance test (e.g., paired t-test or sign test across the 100 test videos) is reported to confirm that the improvement over x264 is not due to chance or driven by a few outlier videos. Adding this would strengthen the evidential basis.

### Trivial
- The qualitative figures (Figures 4, 6, 7) are visually compelling but show only a few frames; supplementary video material or aggregate per-frame results would strengthen the presentation.
- The feature set used for the state (MB-tree statistics) is listed generically ("block energy cost, inverse quantization scaling factor, etc.") without a complete enumeration (Section 3). A full list would aid reproducibility.

## Nice-to-Haves
- **Intermediate γ values in ablation.** The myopic-policy ablation uses γ=0 (Table 4). Testing one or two intermediate values (e.g., γ=0.5, 0.9) would give a more informative picture of how the temporal horizon affects performance.
- **Ablation of the hierarchical action space.** Ablating the upsampling (e.g., learning directly on the full 30×20 space, even if slower) would quantify the cost of the hierarchical approximation.
- **Testing on a more distantly related task.** The robustness experiment already covers SSD (different detector) and DeepLab (different task, segmentation). Testing on a qualitatively different task (e.g., scene classification, depth estimation) would further probe generalization.
- **Histogram of video-wise BD-rate.** Reporting the distribution across the 100 test videos (rather than just the mean and s.e.m.) would reveal whether the method is consistently better or relies on a few large wins.

## Removed Points

These points from the reviewers are excluded or demoted from the main weaknesses section for the reasons stated below. Treat them with caution if referenced.

1. *Critic's note about Related Work characterization (Section 1.1).* The critic argues the paper's taxonomy of prior work conflates certain methods. This is a framing observation, not a concrete weakness of the paper's contribution or results. **Removed** (formatting/framing nitpick).

2. *Critic's suggestion that the paper's method is "not the first" because Li et al. (2021) / Xie et al. (2022) "also do not require the task at inference time in some configurations."* This is speculative — the paper provides specific reasons why those methods do require task-specific information (segmentation maps, single-frame optimization). **Removed** as insufficiently grounded (speculative claim about prior work's capabilities not substantiated in the paper under review).

3. *Critic's statement that "the paper does not discuss what happens when the raw frame's task output is noisy or incorrect."* This observation is subsumed by Weakness #3 (reward formulation bias), which is the concrete manifestation of this issue. **Merged** into Weakness #3.

4. *Strength Finder's generic/superficial strengths.* The Strengths Finder listed "the paper addressed an important problem" and "targeted an interesting question" — these are generic and not specific to the paper's evidence. **Removed**.

5. *Critic's demand for scene classification as a robustness test.* This asks the paper to address a problem outside its stated scope (driving-focused tasks: detection, segmentation, saliency). **Removed** (scope creep).

## Novel Insights

None beyond the paper's own contributions. The reviews did not surface an unexpected reinterpretation of the paper's results or a connection to a broader phenomenon that the paper itself does not discuss.

## Suggestions

1. **Add at least one informed baseline.** Even a simplified adaptation of a prior method under compatible settings, or a non-RL oracle that uses the downstream task at inference (e.g., a lightweight saliency proxy to set QP deltas), would significantly strengthen the evaluation. This would anchor the reader's understanding of how RL-RC-DoT compares to alternatives that relax one constraint at a time.

2. **Report the number of excluded streams and characterize them.** Show results on both the filtered and unfiltered datasets, or at minimum provide statistics on the excluded videos (length, content type, detection performance under x264). This addresses the selection bias concern.

3. **Analyze the reward formulation's effect on detection completeness.** Compare precision-recall curves (using ground-truth labels from BDD100K, which are available) between x264 and RL-RC-DoT. This would reveal whether the agent is improving true detection or just preserving a biased set of raw-frame detections.

4. **Specify the hierarchical action space details.** Document the lower-resolution dimensions, the interpolation method, and how upsampled QP deltas are mapped to the 16×16 MB grid.

5. **Add a statistical significance test** (paired t-test or sign test across test videos) for the BD-rate improvements.
