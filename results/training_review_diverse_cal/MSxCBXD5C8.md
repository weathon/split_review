Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper proposes SKPS-Net for few-shot anomalous action recognition. The key ideas are: (1) a spatial adaptive key patch selection module that locates informative small patches from feature maps without extra parameters, (2) a long-short feature map spatio-temporal relation module using lightweight 2D convolutions, and (3) a spatio-temporal refined loss combining multi-head cross-transformer attention with a temporal Hausdorff matching loss. Experiments on HMDB51, Kinetics, and UCF-Crime v2 show consistent improvements over the TRX baseline, with absolute gains of 0.6% (5-shot) and 1.2% (10-shot) on the anomalous action dataset.

## Strengths

- **Novel parameter-free key patch selection from feature maps**: The spatial adaptive key patch selection module (Section 2.3) uses no learned parameters — it computes patch coordinates from the feature map's spatial distribution and uses bilinear interpolation for differentiable cropping. This is a clean improvement over prior work (Wang et al., 2021a) that required separate object detectors or extra learned weights.

- **Lightweight spatio-temporal modeling at the feature-map level**: The long-short relation module (Section 2.2) uses only lightweight 2D convolutions (channel-averaging + 1×1 conv for temporal relation; frame differencing + 3×3 conv for motion relation), avoiding heavy 3D CNNs or optical flow networks. The ablation study (Table 3) shows consistent accuracy gains when this module is added, and the visualization (Figure 6) confirms it focuses on moving objects rather than static background.

- **Comprehensive ablation isolating each component**: Table 3 incrementally adds the key patch selection, spatio-temporal relation, and refined loss across three datasets and three shot settings, providing clean causal evidence that each proposed module contributes positively.

- **Controlled comparison against naive patch strategies**: Table 4 compares adaptive selection against cropping from the center or a random position (same patch size). The adaptive patch consistently outperforms these baselines, validating that the selection mechanism finds genuinely informative regions.

- **Consistent improvements across multiple datasets and shot settings**: The method achieves top results on both normal action datasets (HMDB51, Kinetics) and the anomalous dataset (UCF-Crime v2) at 5-shot and 10-shot, demonstrating the key-patch enhancement is broadly useful.

## Weaknesses

### Major

- **The core selection mechanism is underspecified**. Section 2.3 defines the patch center as $\dot{A} = \sum_i u_i \dot{l}_i$ and states that "the element $u_i$ is defined as the weight of the shift vector" and points are "fused according to the information distributed in the feature map." However, the paper never specifies *how* $u_i$ is computed from the feature map activations. Are the $u_i$ derived via softmax over spatial positions? Via a linear projection? Direct feature-map values? This is the central operation of the paper's most distinctive module, and the missing detail makes the method incompletely reproducible. The selection module's "no extra weight" property implies $u_i$ must be a function of the feature map itself, but the exact computation is left to the reader's inference. *(Supported by lines 94–98: the description ends before specifying the computation of $u_i$.)*

- **Efficiency claims are not supported and partially contradicted by the architecture.** The paper repeatedly describes the modules as "lightweight," "plug-and-play," "few extra training costs," and "no extra weight" (lines 14, 19, 22, 112). However, the overall system adds a second full ResNet-50 branch for key patch feature extraction ("The global and key patch feature extraction networks both use ResNet-50," line 172). A full ResNet-50 — even processing smaller 128×128 patches — is not negligible. The paper reports no FLOPs, no parameter counts, no training time comparisons, and no inference speed comparisons. The "lightweight" claim is defensible for the selection module itself (which indeed has no learned parameters) and for the relation module (2D convs vs. 3D/optical flow), but the overall system's cost is unsubstantiated. The authors should report actual computational costs and clarify which components the efficiency claims apply to.

### Minor

- **No statistical variability reported.** Few-shot learning results are known to be noisy. The paper reports only point estimates over 10,000 test episodes (line 172) without standard deviations, confidence intervals, or significance tests. While the large number of episodes likely makes standard errors small, the absence of any variance measure means the small gains (e.g., 0.6% on UCF-Crime v2 5-shot) cannot be assessed for statistical significance.

- **Re-implementation faithfulness is only partially validated.** The paper re-implements several prior methods (STRM, SloshNet, BiMACL) for comparison on the new UCF-Crime v2 dataset where original published numbers do not exist. To the paper's credit, the re-implementations of TRX and TRX++ *are* validated against original published values (they match in Table 1 — TRX*: 80.58 vs. TRX (re-impl): 80.58 on HMDB 5-shot). This shows the re-implementation pipeline is sound. However, the STRM, SloshNet, and BiMACL re-implementations are not similarly validated against any published benchmark, so the UCF-Crime v2 comparisons rest on untested re-implementations of those methods. The paper's SOTA claims would be stronger with validation that these re-implementations reproduce original results on a standard split.

- **Frame-level feature extraction for the temporal refined loss is not specified.** Section 2.4.2 defines a bidirectional mean Hausdorff metric operating on "frame-level feature sets" $F_s = \{f_s^0, f_s^1, ..., f_s^i\}$ and $F_q = \{f_q^0, f_q^1, ..., f_q^j\}$. However, the network description earlier produces *video-level* feature vectors (after spatial pooling). The paper never explains how frame-level features are obtained — whether from pre-pooling activations of the backbone, from the key patch branch, or through a separate temporal decomposition step. This makes the temporal refinement component incompletely defined.

- **Method is general few-shot action recognition, not specific to anomalies.** The introduction motivates the work with anomaly-specific challenges (intensity, irregularity, small objects in surveillance), but the proposed modules (key patch selection, spatio-temporal relation, refined loss) are general-purpose and do not leverage any property unique to anomalous actions. This framing mismatch does not invalidate the results, but it overstates the domain specificity of the contribution.

### Trivial

- The text notes "we reimplement these methods" — minor spelling inconsistency (should be "re-implement" for consistency with the table caption). This is a parser artifact, not an author error.

## Nice-to-Haves

- Provide the exact computation of $u_i$ explicitly (e.g., softmax over feature map positions conditioned on spatial activations). This is the single highest-leverage fix for reproducibility.
- Report mean and standard deviation over multiple runs or test episodes for all main results.
- Report FLOPs and parameter counts for the baseline vs. SKPS-Net to substantiate efficiency claims.
- Validate STRM, SloshNet, and BiMACL re-implementations against published numbers on HMDB or Kinetics standard splits.

## Removed Points

These points from the reviewers are flagged to be removed; treat them with caution:

- **"No evidence re-implementations are faithful" (Harsh Critic #2, strong form):** The reviewer claims there is "no evidence" of faithfulness. On the contrary, the paper shows TRX and TRX++ re-implementations match original published values exactly (same numbers in the top and bottom halves of Table 1). The concern is valid for STRM/SloshNet/BiMACL, but the blanket statement is too strong. I have moved this to a Minor weakness rather than the Fatal/Major framing the reviewer gave it.

- **"Multi-head attention cross-transformer subspaces are ambiguous" (Harsh Critic, Other Observations):** The paper explicitly defines: "global (the whole frame) and local (the key patch) subspaces" (line 126). This is clear and not ambiguous. Removed.

- **"State-of-the-art" claim as a strength (Strength Finder #3):** The SOTA claim is contingent on the re-implementation comparisons. Since the STRM/SloshNet/BiMACL re-implementations on UCF-Crime v2 are not independently verified, "state-of-the-art" is a reported result rather than an established fact. I retain this as a claimed result but do not present it as an unqualified strength.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface an interpretation of the results that the authors themselves missed.

## Suggestions

1. **Specify $u_i$ computation.** This is the single most important fix. State whether $u_i$ is the feature-map activation at the corresponding spatial position, normalized via softmax across all $N\times M$ positions, or something else. Provide the exact formula and the gradient flow.

2. **Report FLOPs, parameter counts, and training/inference time** for TRX baseline vs. the full SKPS-Net, and break down which component contributes what cost. Clarify which efficiency claims apply to which module.

3. **Report standard deviations** for all main results, especially on UCF-Crime v2 where the gains are small.

4. **Specify frame-level feature extraction.** State clearly whether the temporal refined loss uses backbone activations before the final pooling layer or features from a separate temporal decomposition, and how the dimensionality aligns.

5. **Tone down the anomaly-specific framing** if the method is general-purpose, or add experiments/discussion showing why the method is particularly suited to anomalies vs. general actions.

## Score and Decision

The paper proposes a novel approach to patch-level feature enhancement for few-shot action recognition with clean ablations and compelling visualizations. However, the core selection mechanism (computation of $u_i$) is insufficiently specified for reproducibility, and the efficiency claims are unsupported by measurements. These issues are addressable in revision but materially weaken the submission as presented. The small performance gains and partially unvalidated re-implementations add further caution.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>