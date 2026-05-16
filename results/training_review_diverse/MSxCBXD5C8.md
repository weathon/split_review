Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes SKPS-Net for few-shot anomalous action recognition. The method introduces three components: (1) a spatial adaptive key patch selection module that uses feature-map-level spatial information (rather than pooled feature vectors) to select discriminative local patches without extra trainable parameters, (2) a lightweight long-short spatio-temporal relation module that fuses long-range temporal information and short-range motion via 2D convolutions and frame differencing, and (3) a spatio-temporal refined loss combining multi-head cross-attention on global/local subspaces with bidirectional Hausdorff temporal alignment. Evaluations on HMDB51, Kinetics, and UCF-Crime v2 show consistent but modest improvements over TRX and other few-shot baselines.

## Strengths

- **Feature-map-based adaptive key patch selection without extra parameters**: Unlike prior work that pools spatial information into a feature vector before selecting patches (Wang et al., 2021a; 2022b), this module directly operates on the 2D feature map to retain spatial structure. It requires no additional trainable weights and supports end-to-end gradient back-propagation. (Section 2.3, lines 86–112)

- **Lightweight spatio-temporal relation module using efficient 2D convolutions**: The module decomposes spatio-temporal modeling into a temporal submodule (reshaping time-as-channels + 1×1 2D conv to fuse all frames, followed by 3D conv) and a motion submodule (frame differencing at the feature map level). This avoids the cost of 3D CNNs or optical flow networks while enriching feature maps with both long-range and short-range temporal context. (Section 2.2, lines 46–83; qualitative evidence in Figure 6)

- **Comprehensive ablation studies isolating each component**: Tables 3 and 4 (described in text) systematically validate each module's contribution and show that adaptive selection outperforms center-patch or random-patch alternatives (e.g., on Kinetics 5-shot: 82.5% adaptive vs. 81.3% center patch). This provides reasonable evidence that the design choices are meaningful.

- **Consistent improvements across multiple datasets and settings**: The method improves over TRX on all three datasets (HMDB51, Kinetics, UCF-Crime v2) across 1-shot, 5-shot, and 10-shot settings, with margins from 0.4% to 2.3%. While modest, the pattern is consistent.

## Weaknesses

### Fatal
None.

### Major

- **The UCF-Crime v2 evaluation protocol is underspecified, undermining the paper's core claim about anomalous action recognition.** The paper states the model is "trained on Kinetics and evaluated on UCF-Crime v2" (line 166), and that 5-way tasks are used. However, it does not specify: (a) how many classes UCF-Crime v2 contains, (b) which specific classes are used for the 5-way evaluation, (c) how tasks are sampled from these classes, or (d) how many videos per class are available. The paper claims "state-of-the-art" on anomalous action recognition and reports improvements of 0.6% (5-shot) and 1.2% (10-shot) on this dataset, but the reader cannot verify or reproduce these results. While the paper states baselines are "reimplemented... under the same condition" (line 179), the condition itself is not defined. This is not a minor presentation issue — it affects the believability of the paper's central contribution. (Section 3, lines 166–193; Table 2)

### Minor

- **The computation of weights $u_i$ in the key patch selection module is not specified.** The module samples $N\times M$ points from the feature map and defines shift vectors $\dot{l}_i$ with associated weights $u_i$, then computes $\dot{A} = \sum u_i \dot{l}_i$. The paper states "$u_i$ is defined as the weight of the shift vector" (line 94) and that points are "fused according to the information distributed in the feature map" — but it never explains how $u_i$ is numerically obtained from the feature map activations. Is it the feature value at that spatial location? A softmax over spatial locations? Something else? Since the module claims "no extra weight" (no trainable parameters), the reader needs to know the exact function. This does not invalidate the method but hurts reproducibility. (Section 2.3, lines 94–98)

- **Modest improvements without reported variance.** Absolute gains over TRX range from 0.4% to 2.3% across all settings. No standard deviations or confidence intervals are reported (the paper averages over 10,000 test episodes, which provides some stability, but multiple random seeds are the norm in few-shot learning). Without variance estimates, it is unclear whether the margins are statistically significant, especially the smaller ones (e.g., ~0.4% on some settings). (Section 3, line 172; Table 1, Table 2)

- **"State-of-the-art" claim is overstated.** Given the modest margins, the absence of variance estimates, and the underspecified UCF-Crime v2 protocol, claiming "state-of-the-art performance in few-shot action recognition" (abstract, line 4) is too strong. The paper shows improvements over a specific set of baselines on a subset of benchmarks, which is valuable but not conclusively SOTA.

- **No computational cost analysis to substantiate "lightweight" claims.** The paper repeatedly describes the proposed modules as "lightweight" and "plug-and-play" (lines 14, 19, 49, 74, 112) but never reports FLOPs, parameter counts, or inference time for the added components relative to the baseline. This makes the efficiency claims unverifiable.

- **No ablation on key hyperparameters.** The patch size is fixed to 128×128 and the number of sampling points $N\times M$ is not specified, let alone ablated. These hyperparameters likely affect the trade-off between localization precision and computational cost. (Section 3, line 172)

### Trivial

- **The "whole-range temporal relation" claim for the $1\times1$ 2D convolution (Section 2.2.1)** is technically correct — after reshaping time-as-channels, a 1×1 conv does produce each output as a weighted combination of all input time steps. However, the framing could mislead readers into expecting more complex non-linear dependencies. A brief clarification would help.

- The paper does not discuss limitations or failure cases (e.g., when the anomalous object is not small, or motion is too fast for frame differencing), which would strengthen the paper's honesty.

## Nice-to-Haves

- **A comparison with attention-based spatial selection methods** (e.g., spatial transformer networks, non-local blocks) as additional baselines, though the paper's focus on few-shot methods is defensible.
- **Quantitative analysis of patch quality** (e.g., overlap with ground-truth object regions) to go beyond anecdotal visualizations.
- **Ablation on patch size ($128\times128$ vs. alternatives)** and sampling grid density ($N\times M$).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Overstates limitation of existing methods by claiming they only consider global features without acknowledging attention/multi-scale works"** — Removed as a strawman. The paper makes a specific claim within few-shot action recognition, supported by citations (Wang et al., 2021b; Perrett et al., 2021; Nguyen et al., 2022). The reviewer's generic counter-claim about "many recent works" is not specific enough to engage with the paper's actual subfield.
- **"Motion relation module does not handle occlusion or large motion well"** — Removed as a generic, non-actionable criticism that could apply to any frame-differencing approach. Not specific to this paper's contribution.
- **"Does K1 with kernel 1×1 really establish whole-range temporal relation?"** — The technical claim is correct: after reshaping time-as-channels, a 1×1 2D convolution fuses all time steps (each output is a linear combination of all input channels/timesteps). The criticism is factually incorrect about what the operation does. The presentation nuance about linear vs. non-linear is addressed as a Trivial point above.

## Novel Insights

None beyond the paper's own contributions. The reviews raise standard concerns about evaluation rigor and specification clarity but do not surface a fundamentally new perspective on the method or problem.

## Suggestions

1. **Specify the UCF-Crime v2 evaluation protocol in full**: number of classes, which classes are used, how 5-way tasks are sampled, number of videos per class, and the exact training/evaluation pipeline for all baselines. This is the single most important fix.

2. **Clarify how $u_i$ is computed** in the key patch selection module. Even a one-sentence description (e.g., "$u_i$ is the feature map activation at the corresponding spatial location, normalized across all $N\times M$ points") would resolve the ambiguity.

3. **Report standard deviations** over multiple random seeds (e.g., 5 runs) for the main results, or at minimum acknowledge that margins are modest and discuss their significance.

4. **Add computational cost analysis** (FLOPs and/or parameter counts) for each module to substantiate the "lightweight" and "plug-and-play" claims.

5. **Tone down the "state-of-the-art" claim** or qualify it with the specific comparison setting and margin.

6. **Add an ablation on the key patch size and the number of sampling points** to show robustness to these hyperparameters.

## Score and Decision

This paper addresses a worthwhile problem (few-shot anomalous action recognition) and proposes a coherent three-component pipeline with a plausible motivation. The strengths — particularly the feature-map-based patch selection and the lightweight spatio-temporal relation module — are genuine contributions. The ablation studies provide reasonable evidence that each component contributes.

However, the paper has a significant evaluative gap: the UCF-Crime v2 protocol — on which the central claim about anomalous action recognition rests — is underspecified to the point where the results cannot be verified or reproduced. Combined with modest margins, no variance estimates, an overclaimed "state-of-the-art" label, and an underspecified algorithmic detail (the $u_i$ weights), the paper in its current form does not meet the bar for acceptance. These issues are fixable in revision.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>