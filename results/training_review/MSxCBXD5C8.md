Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

The paper proposes SKPS-Net for anomalous action recognition in a few-shot setting, introducing three components: (1) a spatial adaptive key patch selection module that uses feature map spatial correspondences to locate small discriminative regions without extra parameters, (2) a lightweight long-short spatio-temporal relation module using 2D convolutions and frame differencing, and (3) a spatio-temporal refined loss combining multi-head attention cross-transformer and Hausdorff-distance-based temporal matching. The method is evaluated on HMDB51, Kinetics, and UCF-Crime v2 under 1/5/10-shot settings using TRX as the baseline.

## Strengths

- **Spatial adaptive key patch selection is a well-motivated architectural contribution**: The idea of using the feature map's spatial correspondences (exploiting CNN translation equivariance) to select informative local patches without external object detectors or position annotations is reasonable and addresses a genuine challenge in anomaly recognition where discriminative objects are small. The ablation (Table 4) shows this module outperforms center/random cropping, with particularly larger gains on the anomaly dataset — the Strength Finder notes a +6.1% gain on UCF-Crime v2 10-shot vs center patch, directly validating the motivation that naive cropping fails for small anomalous objects.

- **Lightweight spatio-temporal relation module is practical and clearly described**: Combining 2D temporal convolution (for long-range temporal relation) with feature-level frame differencing (for short-range motion) avoids the overhead of 3D ConvNets or optical flow networks. The design is well-specified in Section 2.2 with clear equations (1)-(3) and Figure 2. The feature map visualizations in Figure 6 qualitatively demonstrate that after this module, activations focus on changing action regions rather than static background.

- **Structured ablation studies provide reasonable attribution**: Tables 3 and 4 progressively add modules and show incremental gains (e.g., the ablation adds key patch selection, then spatio-temporal relation, then refined loss, with each contributing improvements). The comparison against center/random patch cropping in Table 4 is a useful sanity check that distinguishes adaptive selection from trivial alternatives.

- **Cross-dataset evaluation on UCF-Crime v2**: Training on Kinetics and evaluating on UCF-Crime v2 tests generalization to unseen anomalous actions, which is more realistic and challenging than same-dataset evaluation.

## Weaknesses

### Fatal
None.

### Major

- **The headline improvement of "1.2%" is ambiguous and potentially misleading**. The abstract claims *"outperforming the most competitive methods by 1.2% on the anomalous action dataset UCF-Crime v2."* The body text (Section 3.1) states *"our method achieved an absolute improvement of... 1.2% under the 10-shot setting on the UCF-Crime v2"* without specifying the comparison partner. The paper acknowledges (line 191) that the baseline TRX *"has an obvious performance gap"* vs ATA and OTAM. If the 1.2% improvement is measured against TRX (the baseline), the abstract's phrasing *"most competitive methods"* is overstated. Since Tables 1 and 2 are embedded as images and the exact numerical comparison to the strongest prior method is not explicitly stated in the text, the reader cannot verify the central advertised claim. The paper should clearly state: "improvement of X% over TRX and Y% over OTAM/ATA."

- **The key patch selection weight $u_i$ is underspecified to the point of irreproducibility.** In Section 2.3, the paper states (line 94) that shift vectors $\mathbf{l}_i$ are constant and $u_i$ is "defined as the weight of the shift vector," with points fused "according to the information distributed in the feature map" via Eq. (4): $\dot{A} = \sum u_i \dot{l}_i$. The paper never explains how $u_i$ is obtained — is it the feature map activation value at the corresponding spatial location? Is it a softmax over activations? A learned parameter? The text claims (lines 89, 112) the module requires *"no extra weight,"* but if $u_i$ is a learnable parameter, that contradicts the claim; if $u_i$ is derived deterministically from the feature map, the exact formula is absent. Without this specification, the module cannot be replicated and its "plug-and-play" claim is unverifiable.

- **The spatio-temporal refined loss is incompletely defined.** Section 2.4 states the loss is "the sum of two parts: multi-head attention cross-transformer and temporal refined match loss," but no combined loss equation is written (no weighting coefficients $\alpha, \beta$, no explicit scalar formula). More critically, $D_{MH}$ in Eq. (8) is a vector difference $cat(S_g, S_l) - F_{qe}$, not a scalar loss; the paper never explains how this vector distance is converted into a training loss (e.g., via cross-entropy on distances, as is standard in few-shot matching). The paper states $D_{TR}$ in Eq. (9) using Hausdorff distance, which is a scalar, but how the two components are combined and used for gradient computation remains unclear. This prevents reproduction of the method.

- **Experimental evidence is insufficient to support "state-of-the-art" claims given the small margins.** The reported gains over strong baselines are small (e.g., 0.1–0.5% in many settings), and no confidence intervals, standard deviations, or statistical significance tests are reported over multiple runs. Given the variance inherent in episodic few-shot evaluation, these margins could be within noise. At 1-shot, SKPS-Net underperforms both ATA and OTAM on all three datasets, which is not adequately explained. The paper should report results over multiple random seeds and discuss when/why the method fails.

### Minor

- **The paper's comparison framing is unclear in one place.** Line 181-182 says *"Our method also gets a noticeable improvement on other methods using the same baseline, namely STRM, SloshNet, and BiMACL."* STRM and SloshNet build on TRX, so they share the baseline; BiMACL does not, making this statement confusing. Clarification is needed.

- **The ablation baseline is not explicitly named.** Table 3 labels the first row "Baseline" but the text (line 172) says TRX is used — this should be stated in the table caption or footnotes for clarity.

- **Eq. (3) indexing ambiguity**: $M''_t = K_3 * M'_{t+1} - M'_t$ uses $t+1$ but $t$ as an index, and the concatenation process "at different times" to form the motion mask is stated without specifying the temporal boundary conditions (what happens at the last frame?).

### Trivial
- The notation for the shift vector switches between $\mathbf{l}_i$ and $\dot{l}_i$ / $\dot{A}$ in different parts of Section 2.3, which is mildly confusing.

## Nice-to-Haves

- Report results with standard deviations over multiple seeds for all main tables to establish significance.
- Apply the proposed modules to a non-TRX baseline (e.g., OTAM or ATA) to demonstrate true plug-and-play generality.
- Quantify patch localization accuracy (e.g., IoU with ground-truth anomaly regions) on a subset of UCF-Crime v2 to directly validate that selected patches capture anomalous objects.
- Include an ablation varying key patch size (64×64, 96×96, 128×128, 160×160) to demonstrate robustness.
- Provide a failure case analysis for the 1-shot underperformance — does the key patch module fail with limited data, or does the spatio-temporal relation overfit?

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism about no evaluation on standard anomaly detection benchmarks (frame-level AUC on UCF-Crime v1, ShanghaiTech):** The paper explicitly scopes itself to few-shot action recognition on anomalous action classes (Section 1, line 38: "the anomalous action recognition can be seen as the few-shot action recognition task"). Demanding a different evaluation protocol outside this scope is not fair.

- **Criticism about missing related work:** Removed per instructions — you do not have external sources to confirm existence of missing works.

- **Criticism about missing appendix/proofs:** The parser strips appendix sections from all papers; they exist in the original submission.

- **Criticism that the paper may mislead readers with "anomalous action recognition" framing:** The paper is upfront about its few-shot classification protocol (line 38). This is a characterization, not a deception.

- **Criticism that the reimplementation of baselines may use different conditions:** The paper states results marked * are from original papers and others are "re-implemented... to ensure fair comparison" (line 179). This is standard practice; the critic's concern is speculative.

- **Generic formatting/style nitpicks** about typos, punctuation, etc.: These are parser artifacts, not author errors.

- **Criticism that the ablation baseline is "not explicitly defined":** Line 172 explicitly states "We use the TRX as the baseline." The critic missed this.

## Novel Insights

The most interesting tension that emerges across reviews is between the paper's genuine architectural insight — that feature maps retain spatial correspondences useful for selecting small discriminative patches without extra detectors — and the incomplete specification of how that selection actually works. The $u_i$ weight computation is the linchpin of the entire key patch selection module, yet it is the least described component. This is not a trivial omission: if $u_i$ is computed as the feature map activation at the corresponding spatial position (which would be consistent with the "no extra weight" claim), the module is a learned spatial attention mechanism at the patch level, which is a meaningful contribution. If $u_i$ is a learned parameter, the "no extra weight" claim is false and the method reduces to learning a fixed spatial offset, which is less interesting. Resolving this ambiguity would clarify the paper's true contribution.

## Suggestions

1. **Explicitly state the comparison partner for every improvement claim.** Replace "absolute improvement of 1.2%" with "improvement of X% over TRX and Y% over the best prior method." Ensure the abstract's claim is precisely supported by a specific table cell the reader can verify.

2. **Fully specify the $u_i$ weight computation** in Section 2.3 with an explicit formula. If $u_i$ is derived from the feature map activation at the corresponding spatial position (e.g., $u_i = \text{softmax}(A_i)$ where $A_i$ is the activation value or some function of it), write the equation. If it is learned, state that and adjust the "no extra weight" claim.

3. **Write the complete loss function** as a single equation: e.g., $\mathcal{L} = \alpha \cdot \text{CE}(D_{MH}) + \beta \cdot D_{TR}$ or whatever the actual form is, with values of any hyperparameters. Clarify how $D_{MH}$ (currently a vector) is converted to a scalar loss.

4. **Report standard deviations** over multiple runs (at least 3-5 random seeds) for all main results to assess whether the reported gains are significant.

5. **Discuss the 1-shot failure case**: Why does SKPS-Net underperform ATA/OTAM at 1-shot on all datasets? Is the key patch module unstable with very limited data?

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>