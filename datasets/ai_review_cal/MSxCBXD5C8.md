- Decision: Reject
- Avg Score: 3.00
- Scores: 3, 3, 3, 3
Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes SKPS-Net, a few-shot anomalous action recognition framework built on the TRX baseline, with three plug-in modules: (1) a spatial adaptive key patch selection module that uses feature map spatial information to crop informative local patches without extra parameters, (2) a long-short feature map spatio-temporal relation module that enriches the feature map with temporal and motion cues via lightweight 2D convolutions, and (3) a spatio-temporal refined loss combining multi-head cross-transformer attention with a Hausdorff metric. Experiments on HMDB51, Kinetics, and UCF-Crime v2 show consistent improvements, including a 1.2% gain on the anomalous action dataset under the 10-shot setting.

## Strengths

- **Lightweight, annotation-free key patch selection**: The spatial adaptive key patch selection module (Section 2.3) operates on the feature map directly, uses fractional coordinates with bilinear interpolation for differentiability, and requires no extra weights or position annotations. This is a principled approach to an important problem (small anomalous objects). Table 4 demonstrates that the adaptively selected patch outperforms naive center/random cropping, confirming the module adds signal beyond a simple baseline.

- **Efficient spatio-temporal modeling**: The long-short feature map spatio-temporal relation module (Section 2.2) replaces heavy 3D CNNs or optical flow networks with two lightweight 2D convolution submodules for temporal aggregation and motion differencing. Figure 6 provides visual evidence that the post-relation feature maps focus on changing action regions while suppressing static background, and Table 3 shows consistent accuracy gains from adding this module.

- **State-of-the-art results on anomalous action recognition**: On UCF-Crime v2, SKPS-Net achieves an absolute improvement of 1.2% over the best competitor under the 10-shot setting (Table 2). This directly supports the paper's central claim that local key patch selection, informed by spatio-temporal cues, is particularly beneficial for anomaly recognition where discriminative information resides in small regions.

- **Comprehensive ablation and visualization**: The paper provides sequential ablations for each module (Table 3), comparisons against center/random cropping alternatives (Table 4), and visualizations of both selected patches (Figure 5) and feature maps before/after spatio-temporal relation (Figure 6). These experiments collectively trace the contribution of each design decision.

## Weaknesses

### Fatal

None.

### Major

- **The core mechanism of the key patch selection module is underspecified (Section 2.3)**. The module computes a fused center point as $\dot{A} = \sum_i u_i \dot{l}_i$, where $\dot{l}_i$ are constant shift vectors and $u_i$ are weights. The paper states that $u_i$ "is defined as the weight of the shift vector" and that the points are "fused according to the information distributed in the feature map" — but **it never specifies the actual computation that maps the feature map to $u_i$**. Is $u_i$ the feature map value at the corresponding spatial location? An average or max across channels? A spatial softmax? A learned projection? The paper claims "no extra weight," which rules out learned parameters, but does not say what the weight *is*. Since the adaptive patch selection is the first and most central contribution, this gap prevents an independent reader from implementing or verifying the method. The high-level idea is communicated, but the missing mathematical detail is a significant reproducibility concern for a methods paper. The authors should explicitly state the tensor operations (e.g., "the feature map at the $N \times M$ positions is $f_i$, and $u_i = \text{softmax}(f_i)$" or equivalent).

### Minor

- **UCF-Crime v2 evaluation protocol is incompletely documented (Section 3)**. The paper states the model is trained on Kinetics and evaluated on UCF-Crime v2, and uses 5-way settings (from the implementation details). However, it does not describe: how the UCF-Crime v2 classes are split for the 5-way episodes (how many anomaly classes are available, how they are sampled), how many test episodes are used for the cross-domain evaluation, or whether the evaluation uses the original 13 video-level anomaly classes. This information is needed to interpret the results in Table 2.

- **No variance estimates reported**. All accuracy numbers in Tables 1–4 are reported as point estimates without standard deviations. Given that the ablation gains for individual modules are small (e.g., 0.4–0.5% on HMDB/Kinetics, 0.7–1.4% on UCF-Crime v2), it is unclear whether these improvements are statistically significant. Reporting variances over multiple random seeds or episode draws is standard practice in few-shot learning.

- **The spatio-temporal refined loss description conflates "loss" with "distance" (Section 2.4)**. The paper describes the multi-head cross-transformer and Hausdorff metric as producing distances $D_{MH}$ and $D_{TR}$, and states the loss is "the sum of two parts." However, it never gives the final loss function (e.g., "the final loss is $\mathcal{L} = \text{CE}(D_{MH} + D_{TR})$" or equivalent). The reader must infer how distances translate to a training objective.

- **Patch selection ablation compares only against weak baselines (Table 4)**. The paper compares the adaptive patch against center cropping and random cropping. While this shows the selection is better than naive alternatives, it does not test against a stronger baseline such as spatial attention from a support-set-trained heatmap or an off-the-shelf saliency detector. This weakens the claim that the specific mechanism — not just the presence of an additional branch — is responsible for the improvement.

### Trivial

- The kernel size and padding of the 3D convolution $K_2$ in the temporal relation module (Section 2.2.1) are not specified, making this submodule's exact behavior ambiguous.

## Nice-to-Haves

- **Disentangle two-branch effect from adaptive selection**: A comparison against a "two-branch TRX" where the second branch crops the center (fixed, not adaptive) would isolate whether the gain comes from adaptive selection or simply from having an additional local feature stream.
- **Plug into a second baseline**: The paper claims the module is "plug-and-play" but only demonstrates it on TRX. Testing on one additional baseline (e.g., OTAM or ATA) would substantially strengthen this claim.
- **Analyze the gradient flow through the clamping function $g$**: The piecewise-constant clamping function has zero gradient almost everywhere, which could impede training. A discussion of how gradients flow through the module (e.g., using a straight-through estimator or ignoring the clamping gradient) would be helpful.
- **Report training/inference time and parameter count**: The paper claims the module is "lightweight" and "low-cost" but provides no runtime or parameter measurements to support this.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *The method's contribution relative to prior work is unclear* — The reviewer critiques novelty but the paper clearly states each module's relationship to prior work (Jiang et al. 2019, Li et al. 2020, Wang et al. 2022a) and the claimed novelty lies in applying these ideas at the feature-map level for key patch selection. This is a matter of interpretation, not a verifiable flaw, and similar hybrid designs are standard in applied ML papers. **Reason for removal**: Not a specific, verifiable weakness — novelty judgments are subjective unless grounded in a concrete error or omission.
- *Section 2.2.2 motion mask concatenation not described in detail* — The paper states: "The motion features calculated by formula (3) at different times are concatenated to get the motion mask." This is sufficiently clear for a reader familiar with basic tensor operations. **Reason for removal**: Reviewer misread; the description is adequate.
- *The text about STRM, SloshNet, and BiMACL is confusing* — The paper says "our method also gets a noticeable improvement on other methods using the same baseline, namely STRM, SloshNet, and BiMACL." These methods are listed in the tables and use TRX as their baseline. **Reason for removal**: The text is clear in context.
- *Criticism that reimplemented baselines underperform reported values* — The paper acknowledges this gap (line 191: "we can tell that our baseline TRX has an obvious performance gap under this setting"). This is common in few-shot reimplementation and the paper's own method is evaluated under the same conditions. **Reason for removal**: The paper already addresses this.
- *Missing related works* — As per guidelines, this cannot be raised without external sources. **Reason for removal**: Per instruction.
- *Various formatting/style nitpicks* — Parser artifacts, not author errors. **Reason for removal**: Per instruction.

## Novel Insights

None beyond the paper's own contributions. The two reviews do surface a useful observation: the few-shot anomaly recognition framing is interesting as a practical use case, and the idea of using the feature map (rather than the feature vector) for spatial adaptation is a plausible alternative to region-proposal or attention-based methods. However, neither review identifies a deeper insight that transcends the paper's own presentation.

## Suggestions

1. **Specify the $u_i$ computation explicitly.** Add one sentence or equation stating how each $u_i$ is derived from the feature map at the corresponding spatial position (e.g., softmax-normalized feature values, or channel-averaged responses, etc.).
2. **Document the UCF-Crime v2 evaluation protocol completely**, including the number of anomaly classes, how 5-way episodes are sampled, and the number of test episodes.
3. **Add standard deviations** to all result tables, especially for ablation studies where gains are small.
4. **Clarify the final loss function** by writing it explicitly as a function of $D_{MH}$ and $D_{TR}$.
5. **Include a stronger patch-selection baseline** (e.g., attention heatmap from a classifier or gradient-based saliency) to better demonstrate the advantage of the proposed mechanism.
