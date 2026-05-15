Now I have a thorough understanding of the paper and all review inputs. Let me synthesize the final review.

## Summary

VBGS formulates 3D Gaussian splatting as variational inference with conjugate priors, deriving closed-form updates for the posterior parameters of a Gaussian mixture model over spatial coordinates and colors. The authors claim this enables continual learning from streaming 2D/3D data without replay buffers, and they compare against a gradient-based optimization baseline on Tiny ImageNet, Blender 3D objects, and Habitat rooms.

---

## Strengths

- **Closed-form variational update rule from conjugacy**: The paper derives exact, iterative update equations for the natural parameters of the posterior (Section 3.3, Equations for $\eta_{t,k}$ and $\nu_{t,k}$) using Normal-Inverse-Wishart and Dirichlet priors. This enables a single update step per observation without gradient backpropagation, which is a genuinely different approach from standard 3DGS optimization.

- **Demonstrated continual learning without catastrophic forgetting**: In the 2D image patch experiment (Figure 3a), VBGS maintains consistent PSNR across sequential patches and converges to the batch-training accuracy, while the gradient baseline's performance degrades. The 3D continual experiment (Figure 3b) shows similar behavior: VBGS improves steadily while the gradient method deteriorates after ~50 frames. This empirically validates that the accumulation of sufficient statistics avoids forgetting.

- **Faster per-observation update**: Wall-clock time for VBGS is $0.03 \pm 0.03$ seconds versus $0.05 \pm 0.02$ for gradient-based optimization (Section 4.1, t-test $p = 0$).

- **Component reassignment mechanism**: Section 3.4 introduces a heuristic that reinitializes unused components (where $\alpha_k$ equals its prior) to under-explained data points. This yields substantial improvement on Habitat rooms (Figure 5b: VBGS+reassign achieves roughly double the PSNR of VBGS alone on the Van Gogh room), addressing a practical limitation of fixed cluster assignments.

---

## Weaknesses

### Fatal
None. All identified issues are weaknesses that limit the paper's scope and strength of claims, but none invalidate the core contribution (a variational Bayes formulation for Gaussian mixture scene representation with closed-form continual updates).

### Major

1. **"Matches state-of-the-art" claim is unsupported by the evidence.** The abstract claims VBGS "matches state-of-the-art performance on static datasets," but the only comparison is against a stripped-down gradient baseline that uses no adaptive density control, no opacity modeling, and zero-order spherical harmonics. The reported PSNR values (15–25 dB on Blender) are far below the 33–37 dB reported by actual 3DGS (Kerbl et al., 2023). The paper does not compare against published 3DGS numbers or replay-based continual learning methods such as SplaTAM, which is explicitly cited in the motivation. Without these comparisons, the paper's performance claims relative to the broader literature cannot be evaluated.

2. **Frozen assignments limit the model's ability to adapt its clustering structure.** The paper explicitly states (Section 4.4) that assignments $q(z)$ are "always computed with respect to the initial posterior over parameters." This means the component structure (which data points belong to which cluster) is determined solely by the initial parameter values and never updated when new data arrives. The model accumulates sufficient statistics for existing components, but it cannot reassign data points to different components based on new information. While the reassignment heuristic (Section 3.4) partially addresses this by moving unused components, it is an ad-hoc fix rather than a principled extension of the variational framework.

3. **Training objective (ELBO on point clouds) does not match the evaluation metric (rendered image PSNR).** The variational inference objective is the ELBO computed on (spatial, color) pairs in point-cloud space. However, the primary evaluation metric is PSNR on rendered novel views. The gradient baseline directly optimizes rendered image quality via differentiable rendering. This means the comparison is between a method that optimizes the evaluation metric and one that optimizes a different (though related) objective. The mismatch is acknowledged implicitly but its implications for the validity of the comparison are not discussed.

4. **No comparison against replay-based continual learning methods.** The paper motivates VBGS as an alternative to replay buffers (citing SplaTAM, NICE-SLAM), yet never compares against a replay-based method on the same streaming data. A direct comparison on the Habitat rooms setting would be essential to substantiate the claim that VBGS is better than existing continual learning approaches for 3D scene representation.

### Minor

1. **The generative model does not incorporate opacity or view-dependent effects.** VBGS models (spatial, color) pairs with a GMM, but actual 3DGS includes opacity, alpha compositing with depth sorting, and view-dependent color via spherical harmonics. The paper uses the 3DGS renderer as a post-hoc step for novel view synthesis, but the learning objective does not capture these phenomena. The fixed color covariance prevents intra-component color blending, but this also precludes any color variation within a component.

2. **The gradient baseline is simplified relative to standard 3DGS.** The comparison baseline uses no adaptive density control, zero-order spherical harmonics, fixed opacity, and (for images) a fixed camera at identity with zero depth variation. The paper is transparent about these choices, but the results cannot be interpreted as comparing VBGS against "3D Gaussian Splatting" as the community understands it. The paper should clarify this distinction more prominently.

3. **The reassignment heuristic is empirically motivated but not well-analyzed.** The heuristic reassigns 5% of unused components to high-ELBO data points. Its sensitivity to the fraction parameter, the threshold for "unused," and the sampling distribution are not studied. It also departs from the closed-form variational framework, making the method a hybrid approach rather than a pure variational method.

### Trivial

- Figure 2b (continual 3D PSNR) shows that VBGS (Random Init) achieves ~11 dB while Gradient (Random Init) achieves ~21 dB after many steps, but the text reports these as $11.19 \pm 3.53$ dB and $21.26 \pm 1.76$ dB respectively (line 332). The "drastically improving performance" claim in the abstract should be scoped to the comparison against the gradient baseline's continual degradation, not absolute quality.

---

## Nice-to-Haves

- **Ablation of the "assignments w.r.t. initial prior" design choice**: Comparing VBGS against a variant where assignments are recomputed after each data batch (true sequential Bayesian updating) would reveal whether the frozen assignments are a feature or a bug in practice.

- **Comparison to actual 3DGS (author's code)**: Running the official 3DGS repository on the same Blender objects and reporting standard metrics would contextualize the paper's contribution relative to the state of the art.

- **Comparison against replay-based continual learning**: A direct comparison against methods like SplaTAM on the Habitat rooms under streaming conditions would directly support the paper's main motivation.

---

## Removed Points

These points are flagged to be removed, treat them with caution.

- **Harsh Critic Point 1 labeled "structural/fatal"**: The frozen-assignment design is explicitly described and acknowledged by the paper (Section 4.4). The reassignment heuristic (Section 3.4) partially addresses adaptation. The model DOES perform continual learning (accumulates information without forgetting), as demonstrated empirically. The characterization as "invalidates the central claim" is too strong.

- **Harsh Critic claim that model "cannot adapt its grouping of data points as new information arrives"**: This overlooks the component reassignment mechanism (Section 3.4), which moves under-utilized components to poorly explained data. While limited, the model can adapt its structure.

- **Harsh Critic claim that "the comparison does not support the claimed conclusion" about VBGS matching gradient performance**: The paper clearly describes both methods' training setups (point cloud vs. rendered images). The within-paper comparison is valid for comparing VBGS against gradient-based optimization of a similar model; the problem is the overclaiming to "SOTA."

- **Harsh Critic claim about COLMAP depth (line 370–371)**: The paper's statement that SfM "implicitly also provide[s] depth information through triangulation" is factually correct — SfM does produce sparse 3D points via triangulation.

- **Strength Finder Strength 6 (separate spatial/color modalities)**: The modeling choice is standard for GMMs and not particularly novel. The fixed color covariance is a minor innovation. Moved here as it's thin as a strength.

---

## Novel Insights

The reviews surface an interesting tension: the paper's core design choice (frozen assignments with respect to the initial prior) is simultaneously the key to its order-invariance/anti-forgetting property and its most significant limitation. This reveals a fundamental trade-off for Bayesian continual learning in mixture models — you can either have a model that maintains exact order-invariant accumulation of information (by freezing assignments), or one that adaptively reclusters as new data arrives (true sequential Bayesian updating, but potentially prone to forgetting past cluster structure). Neither approach is strictly superior; the choice depends on whether the application requires stable component identification or adaptive clustering. The paper implicitly chooses the former but does not articulate this trade-off.

---

## Suggestions

1. **Tone down the "SOTA" claim** — or back it up with comparisons against actual 3DGS (official code) on the Blender dataset. The current evidence supports "comparable to a gradient-based GMM optimizer," not "state-of-the-art."

2. **Add an experiment comparing against a replay-based method** on the Habitat rooms continual setting to directly support the paper's main motivation.

3. **Add an ablation where assignments are recomputed at each time step** (true sequential VI) to quantify the cost of the frozen-assignment design choice.

4. **Clarify the training/evaluation mismatch** — discuss how optimizing ELBO on point clouds relates to rendered image PSNR, and whether the gap could be closed by adding a rendering-based likelihood term.

---

## Score and Decision

The paper proposes a genuinely different approach to optimizing Gaussian mixture models for 3D scene representation, with a clean variational formulation and closed-form updates. The continual learning experiments convincingly show VBGS avoids catastrophic forgetting. However, the paper significantly overclaims relative to the evidence (claiming SOTA performance with 15-25 dB PSNR), compares only against a simplified baseline, and does not benchmark against actual 3DGS or replay-based continual learning methods. The frozen-assignment design limits adaptation and is not adequately interrogated. The core idea has merit, but the experimental validation is insufficient to support the strongest claims in their current form.

**Score: 5.0 / 10**

**Decision: Reject** — with the suggestion that the authors address the overclaiming, add comparisons against actual 3DGS and replay-based methods, and clarify the scope of their contribution for a resubmission.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>