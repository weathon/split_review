I have all the evidence needed. Here is my consolidated final review.

---

## Summary

SeMv-3D proposes a general text-to-3D framework combining a Triplane Prior Learner (TPL) that generates three orthogonal views (front/top/side) from text, and a Semantic-aligned View Synthesizer (SVS) that encodes these views via DINO, applies cross-attention and the proposed orthogonal attention (OA), and renders arbitrary views through a NeRF-like decoder in a single feed-forward pass. The central claim is achieving *both* semantic consistency and multi-view consistency simultaneously, which prior methods typically trade off. The paper reports competitive Clip Scores (30.26, best among compared methods) and leads in user preference (42.6%) across 48 participants.

## Strengths

- **Simultaneous semantic and multi-view consistency demonstrated empirically.** Table 1 shows SeMv-3D achieves the highest Clip Score (30.26 vs. MVDream's 30.09) and leads in user preference for both semantic consistency (52.1%) and multi-view consistency (55.8%) over all baselines. The qualitative comparisons in Figure 3 show that SeMv-3D preserves object details across views where MVDream fails, and captures textual semantics where prior-based methods (Shap-E, Point-E) lose detail.

- **Arbitrary-view generation in a single feed-forward step.** The batch sampling and rendering strategy (Section 3.3.2) enables any number of views in one inference, while all baselines generate at most 4 views (MVDream) or a single view. This is a clear architectural advantage.

- **Object Retention module is well-motivated and ablated.** The OR module removes background before triplane learning. The qualitative ablation (Figure 4) shows it successfully eliminates extraneous content, and the design of freezing the pretrained T2I model while adding lightweight adapters is sensible for preserving 2D priors.

- **Text-varied synthesis with fixed triplane prior demonstrated.** Figure 5b shows that with the same triplane prior from TPL, SVS can vary local details (textures, materials) according to different text prompts while maintaining multi-view consistency, illustrating a useful decoupling of 3D structure from semantic variation.

- **Code released and results reproducible by design.** The paper includes an anonymous code link and is built on Stable Diffusion 2.1 with publicly available components (DINO, EG3D-style rendering).

## Weaknesses

### Fatal
None. The paper's core claims are supported by experimental evidence, though several significant issues must be addressed.

### Major

1. **The orthogonal attention formulation (Eq. 4) is mathematically problematic as written.** 
   The equation `OA_i(P_1, P_2) = ∏_{M∈P₁} softmax((W_Q(M)W_K(N)^T)/√d) W_V(N)` uses a *product* over all elements M in plane P₁. In standard attention, each query produces its own attended output vector. A product over all queries would perform element-wise multiplication of all per-query attended features, collapsing spatial information and creating gradient degradation (any single near-zero term nullifies the entire output). The textual description in lines 112-113 correctly describes per-pixel orthogonal attention (e.g., pixel (a,b,-) attending to pixels sharing coordinate a in the xz-plane), but the equation *does not implement this description*. Given that the ablation study shows OA outperforms temporal attention qualitatively, the implementation likely deviates from what is written. This is a serious presentation gap: the paper's core technical novelty cannot be reconstructed from the equations, which is unacceptable for a claimed primary contribution. The product (∏) appears to be a typesetting error for either a sum (∑) or indexing by M, but this requires correction.

2. **No objective metric for multi-view consistency — the paper's own primary goal.** 
   The paper frames "multi-view consistency" as one of its two core objectives, yet the quantitative evaluation (Table 1, left) reports only Clip Score and Aesthetic Score on the *front view*. Neither metric evaluates consistency across views. The user study includes a multi-view consistency question, but this is subjective and limited to four specific views (0°, 90°, 180°, 270°). Objective metrics such as LPIPS between adjacent views, structural similarity across viewpoints, or Chamfer distance from reconstructed meshes are standard in the 3D generation literature and are absent here. The paper's central claim of achieving multi-view consistency is therefore supported only by qualitative figures and a single subjective question.

3. **The model is explicitly not converged, weakening comparative claims.** 
   The Limitations section (line 301) states: "due to the limited computational resources in our lab, our method does not converge well." The reported results are from an incompletely trained model, yet comparisons are against fully-trained baselines (MVDream, Shap-E, etc.). The Clip Score margin (30.26 vs. 30.09) is small enough that convergence differences could shift rankings. The paper argues this actually strengthens the result ("even so, our performance exceeds existing methods"), but the reader cannot determine whether the gap would widen or narrow with full training. This issue is disclosed but not discussed in the experimental setup, nor is any convergence analysis (validation curves, learning plateaus) provided to help the reader gauge stability.

### Minor

4. **"Triplane prior" terminology is misleading.** 
   TPL outputs three RGB images (front, top, side views) from a text-to-image diffusion model, not a true triplane feature representation in the EG3D sense (three orthogonal feature planes that define a radiance field). These images are then encoded by DINO into latent tokens that serve as a feature representation. The paper uses "triplane prior" to describe what is functionally a multi-view image generation followed by encoding. This inflates the novelty — TPL is essentially a T2I model fine-tuned to generate three specific views rather than learning a true 3D feature representation. The pipeline itself is reasonable, but the terminology should be clarified to avoid overclaiming.

5. **"Any view" claim is unsupported for out-of-distribution camera poses.** 
   The paper claims "any view" can be generated in one step. The NeRF-like decoder is trained on Objaverse renderings (likely at fixed elevations with varying azimuths). Only standard views (0°, 90°, 180°, 270° and 60° intervals) are shown. No evidence is provided for generalization to extreme elevations, top-down views, or camera poses not seen during training. The claim should be scoped to "arbitrary azimuth at training-distribution elevations" or supported with explicit out-of-distribution evaluations.

6. **Ablation studies are entirely qualitative.**
   Figures 4 and 5a ablate OA, CA, and OR components but report no corresponding quantitative metrics (Clip Score, LPIPS, or any reconstruction error). Without numbers, the marginal benefit of each component cannot be assessed.

### Trivial
- The user study (48 users) does not specify whether participants were experts or laypersons, whether outputs were anonymized, or whether presentation order was randomized. These are standard best practices and should be reported.
- The evaluation uses 25 self-selected prompts. The authors acknowledge this implicitly but should note whether these are from a public benchmark or curated by the authors.

## Nice-to-Haves
- Evaluate on a public benchmark (e.g., GPT-3D prompts, Objaverse-XL) to facilitate standardized comparisons.
- Include failure case analysis — prompts where SeMv-3D struggles (complex topology, thin structures, precise counts/relationships).
- Report validation curves showing convergence behavior to contextualize the "not converged" admission.

## Removed Points
- *Set notation ambiguity (vertical bar used for both set comprehension and logical OR in Eq. 5).* — Parser/formatting issue; mathematical intent remains decipherable.
- *Critique that P₁∩P₂ is not clearly defined for orthogonal planes.* — Orthogonal planes in a discrete 3D grid intersect along a coordinate axis, which is well-defined. The critic's concern reflects a misunderstanding.
- *Claim that softmax is applied "per (M,N) pair independently without normalization across any meaningful axis."* — N is a set, so W_K(N) produces a matrix and softmax normalizes over the key dimension, which is standard.
- *Related work positioning criticism about MVDream being in a "hybrid space."* — MVDream fine-tunes a T2I model on multi-view data, which fits the paper's "fine-tuning-based" category correctly.
- *User study percentage summation check (99.9%).* — This is trivia amounting to rounding error and is not a weakness.

## Novel Insights
None beyond the paper's own contributions. The key insight — that generating triplane-structured orthogonal views via a T2I model and aligning them with text through cross-attention in latent space can improve both semantic and multi-view consistency — is well articulated in the paper itself.

## Suggestions
1. Fix Equation 4: replace the product (∏) with the intended operation (likely an output indexed by M, or a sum over M). Clarify whether OA produces one attended feature per position or a pooled representation.
2. Add objective multi-view consistency metrics: report LPIPS between views at varying azimuth intervals, and/or Chamfer distance from mesh reconstructions across viewpoints.
3. Either train to convergence and re-report results, or provide validation curves showing loss plateauing to demonstrate the current results are stable.
4. Clarify the "triplane prior" terminology: acknowledge that TPL produces three RGB views (not EG3D-style feature planes), and describe how these serve as a prior after DINO encoding.
5. Scope the "any view" claim to the actual evaluation distribution, or provide explicit out-of-distribution camera pose generalization experiments.

## Score and Decision

The paper addresses an important problem with a plausible pipeline and competitive results. However, the core technical contribution (orthogonal attention) is not correctly defined mathematically, the evaluation lacks objective metrics for the paper's own stated primary goal (multi-view consistency), and the model's unconverged state casts uncertainty on comparative claims. These are structural issues requiring correction rather than incremental clarification.

**MY FINAL SCORE:** <pineapple>5.0</pineapple>
**MY FINAL DECISION:** <orange>Reject</orange>