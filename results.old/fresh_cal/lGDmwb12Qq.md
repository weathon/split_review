Now I have a thorough understanding of the paper and the reviews. Let me construct the final consolidated review.

## Summary

This paper proposes **Sampling-Gaussian (SG)**, a distribution-based supervision method for stereo matching. The approach replaces the standard smooth L1 loss on the soft-argmax output with a combined L1 + cosine similarity loss applied to the full probability distribution, extends the disparity range beyond [0, 192) to mitigate endpoint bias, and replaces trilinear interpolation with bilinear spatial-only upsampling. The method is evaluated on five baselines (PSMNet, GwcNet-g, MSN3D, MSN2D, IGEV-Stereo) across Sceneflow and KITTI datasets, reporting consistent D1-error reductions.

## Strengths

- **Identification of two concrete problems in prior distribution-based stereo matching.** The paper pinpoints (a) endpoint truncation — setting the disparity range to [0, 192) causes biased predictions near 0 and 192 for distribution-based losses (Sec. 3.2, Eq. 5), and (b) incompatibility between trilinear interpolation and convex target distributions (Sec. 3.2, Fig. 2 right). Both are clearly motivated and directly motivate the paper's design choices.

- **Proposes a non-trivial combined loss (L1 + cosine similarity) on probability vectors.** Interpreting the distributions as vectors and using cosine similarity alongside L1 is a genuine departure from the standard cross-entropy approach. Fig. 3 provides a concrete illustration of why L1 alone can be insufficient (different vectors with the same L1 loss yield very different EPE), and the ablation (Sec. 5.2.3) shows the combined loss outperforms CE alone.

- **Demonstrates consistent D1-error improvement across five diverse baselines.** On the KITTI datasets, the method improves all five baselines, with the largest gain on the lightweight MSN2D (0.54% D1 reduction) and smaller but nonzero gains on stronger baselines like IGEV-Stereo (0.01%). The consistent sign of improvement across architectures (conv3D, 2D-conv, iterative refinement) supports the generality claim.

- **Cross-domain generalization improvement.** Models trained on Sceneflow and evaluated directly on KITTI2015 show improved performance with SG (Sec. 5.5), suggesting the method also benefits out-of-domain robustness.

## Weaknesses

### Fatal
None.

### Major

- **The claim that SG "can be applied directly without altering the network" (line 120) contradicts the paper's own method description.** Line 120 explicitly says "without altering the network" and the abstract says "directly applied," yet Sec. 4.2 describes necessary structural changes: replacing trilinear interpolation with bilinear interpolation, changing the disparity range from [0, 192) to [-dₑₓₜ, 192+dₑₓₜ), and adjusting the cost volume construction. These are architectural modifications, not a zero-code-change plug-in. While the inference formula (§4.4, Eq. 7) indeed has the same form as soft-argmax (just with a ×4 scale factor), saying the method requires "no network alteration" is inaccurate and overstates the contribution's ease of adoption. This overclaim does not invalidate the core contribution but needs correction.

- **The theoretical justification for rejecting trilinear interpolation as "impossible" is insufficiently supported.** The paper states (line 184) that after trilinear interpolation the probability distribution "is impossible to fit the target distribution" and "impossible for the network to converge." However, trilinear interpolation operates on pre-softmax logits (real-valued), not on probabilities. The softmax of linearly interpolated logits can approximate a convex shape — it is a softmax of linearly interpolated values, which is not itself linear. The paper provides no mathematical proof or controlled experiment demonstrating true impossibility. The ablation (Sec. 5.2.2) shows bilinear outperforms trilinear, but this conflates two changes (interpolation method + disparity resolution), so it does not establish impossibility, only practical inferiority. The claim should be softened to "empirically suboptimal" or rigorously proven.

### Minor

- **No uncertainty estimates for any reported results.** The paper reports single-run numbers without confidence intervals, standard deviations, or multiple seeds. This is especially concerning for the 0.01% improvement on IGEV-Stereo (Sec. 5.4, Table on KITTI), which is within the range of noise for a single run on a strong baseline. While multiple-run reporting is not universally standard in this field, the very small gain on the strongest baseline needs statistical grounding to be convincing.

- **Missing ablation that isolates the supervision signal from the architectural changes.** The core question — does the Gaussian + combined loss supervision help *independently* of the upsampling change and range extension? — is not directly answered. A cleaner test would be: train a baseline with its original architecture (trilinear + [0,192) range) using (a) standard L1, (b) Gaussian+CE, (c) Gaussian+L1, (d) Gaussian+L1+cos. The current ablations change multiple variables simultaneously, making it impossible to attribute improvement to the supervision mechanism alone.

- **The combined loss motivation is largely heuristic, and the only CE comparison is an unclear number.** The paper says CE "achieved only 0.94" (line 339) without specifying what metric (EPE? D1? On which dataset/setting?). The cosine similarity on probability vectors is unusual — since both vectors are nonnegative and sum to 1, cosine similarity reduces to a function of the dot product, which is closely related to cross-entropy. The paper does not discuss when the combined loss would behave differently from CE or how the gradient interacts with the softmax output's normalization. The ablation also notes (line 339) that "if λ is too large, the network would eventually collapse," suggesting the loss is numerically fragile.

- **Computational cost is not reported.** The paper claims "no reduction in efficiency" (Abstract) but does not provide inference-time latency or memory comparisons. The extended disparity range (D = dₘₐₓ + 2×dₑₓₜ) increases the cost volume size, which has clear computational implications even if the Top-k post-processing is removed. Runtime numbers (ms per frame) for each baseline vs. SG variant should be reported.

### Trivial

- **Terminological imprecision in the gradient analysis.** The paper uses the term "biased gradient" (Sec. 3.1, line 165) to describe the fact that ∂L/∂e^{zᵢ} ∝ (i−d). The math is correct — indices farther from d receive proportionally larger gradient weights — but describing this as "bias" conflates weight-magnitude effects with statistical bias. The gradient is unbiased w.r.t. its target; it is merely non-uniformly scaled. This does not affect the method's validity.

- **The inference formula (Eq. 7) works with a coarser disparity resolution.** Since the disparity dimension remains at D/4 resolution (not upsampled to D), the output is quantized in steps of 4 pixels at the cost-volume level before soft-argmax. While the ×4 multiplier recovers the scale, this means sub-pixel precision relies entirely on the softmax weighting rather than on native resolution. This is a design trade-off worth acknowledging.

## Nice-to-Haves

- An ablation that isolates the supervision signal from the architectural changes: train a standard baseline (e.g., PSMNet with its original trilinear upsampling and [0,192) range) using (a) L1 only, (b) Gaussian + CE, (c) Gaussian + L1, (d) Gaussian + L1 + cosine. This would directly test whether the supervision mechanism itself drives improvement.
- A controlled experiment comparing trilinear vs. bilinear upsampling *with the same number of disparity levels* to disentangle the upsampling method from the resolution change.
- Reporting inference runtime (ms/frame) and GPU memory for each baseline vs. SG variant.

## Removed Points

These points raised by one or both reviewers have been removed with justification:

1. **"Experimental results are presented via in-text references to tables that are missing from parsed text"** — Parser artifact. Tables are embedded via \input{} statements that the PDF extraction lost. The original submission contains them.
2. **"Missing related works"** — As per instructions, I cannot assess whether related works are missing without external knowledge.
3. **"Typos, formatting issues, broken equation references"** — These are PDF parsing artifacts, not author errors.
4. **"No discussion of the effect of extended range on cost volume computation"** (as a fatal issue) — The paper does mention the range extension (Sec. 4.1) and shows an ablation (Sec. 5.2.4) demonstrating its positive effect. The computational implications could be discussed but this is not fatal.
5. **"The strength that improvement is 'substantial'"** — The 0.01% improvement on IGEV-Stereo is not substantial; the strength finder exaggerated. The appropriate characterization is "consistent" not "substantial."
6. **"Missing limitations section"** — Nice to have but not a weakness in the method itself.
7. **"The gradient bias argument conflates variance with bias"** — Retained as a Trivial weakness but reframed as terminological imprecision rather than a substantive error. The math is correct.

## Novel Insights

The two reviews interact in an informative way: the harsh critic correctly identifies that the "impossible" claim about trilinear interpolation is unproven and that the plug-and-play claim is overstated, while the strength finder correctly identifies that the paper makes a genuine contribution in diagnosing the endpoint-truncation problem and proposing a novel loss. However, neither reviewer noticed that the most compelling evidence for the method — consistent improvement across 5 baselines — is undercut by the lack of statistical uncertainty reporting and the conflation of multiple architectural changes. The real value of the paper lies in the vector-space interpretation of distribution supervision and the combined L1+cosine loss, not in the architectural modifications (extended range, bilinear upsampling), which are reasonable but auxiliary. The paper would be significantly stronger if it separated these contributions cleanly.

## Suggestions

1. **Correct the overclaim about "direct application without altering the network."** Acknowledge that the method requires changing the upsampling operation and extending the disparity range. If you want to maintain the claim, provide a version that works with the original architecture (trilinear + standard range) with only the loss changed, and report whether it still improves.
2. **Provide a clean ablation isolating the supervision signal.** Show that Gaussian + combined loss improves accuracy even when the architecture (trilinear upsampling, [0,192) range) is kept fixed.
3. **Report multiple-seed runs or confidence intervals** for the main results, especially the 0.01% gain on IGEV-Stereo.
4. **Soften the "impossible" claim about trilinear interpolation** to "empirically suboptimal" or provide a rigorous proof.
5. **Report inference-time speed and memory usage** to substantiate the "no efficiency decrease" claim.
6. **Clarify the CE comparison number** ("achieved only 0.94") — specify the metric, setting, and baseline value for context.

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>