Now I have all the information I need. Let me synthesize the final review.

## Summary

SeMv-3D proposes a general text-to-3D generation framework with two components: a Triplane Prior Learner (TPL) that uses orthogonal attention to generate three consistent orthogonal views (front, top, side) from text, and a Semantic-aligned View Synthesizer (SVS) that encodes these into features and renders arbitrary views in a single feed-forward pass via a batch rendering strategy. The paper targets the trade-off between multi-view consistency (strong in prior-based methods) and semantic consistency (strong in fine-tuning-based methods), claiming to achieve both simultaneously.

## Strengths

1. **Novel orthogonal attention (OA) mechanism for enforcing spatial correspondence among three orthogonal views.** The OA design (Eqs. 3–5) explicitly correlates pixels across xy, xz, and yz planes based on shared axes — e.g., pixel (a,b) in the xy-plane attends to all pixels with x=a in the xz-plane and y=b in the yz-plane. The qualitative ablation (Fig. 6) shows OA substantially improves geometry and texture over temporal attention, which only captures coarse spatial relationships. This is a genuinely novel architectural contribution for the task.

2. **Batch rendering strategy enabling arbitrary views in a single feed-forward pass.** The SVS batch sampling approach (Sec. 3.3.2) allows the method to render *any* number of views in one step. Table 1 shows that the best baseline (MVDream) produces at most 4 views per step, while SeMv-3D is unrestricted. This capability is not demonstrated by prior general text-to-3D methods and is a clear differentiator.

3. **Strong quantitative and user-study results.** SeMv-3D achieves the highest Clip Score (30.26 vs. MVDream's 30.09) and the highest user preferences for both semantic consistency (52.1%) and multi-view consistency (55.8%) across five baselines. This directly supports the paper's central claim of simultaneously achieving both forms of consistency — a claim that neither fine-tuning-based (MVDream) nor prior-based (Shap-E, Point-E, VolumeDiffusion, 3DTopia) methods can make.

4. **Demonstrated ability to decouple shape from appearance via the triplane prior.** The generalization experiment (Fig. 7b) shows that the same TPL-generated triplane prior can be rendered with different textures/materials by varying the SVS text prompt, while preserving geometry and multi-view consistency. This goes beyond what existing methods show and suggests genuine 3D understanding in the learned representation.

## Weaknesses

### Fatal
None.

### Major

1. **No direct quantitative metric for multi-view consistency — the paper's central claim is under-measured.** The paper's core contribution is achieving multi-view consistency *simultaneously* with semantic consistency. Yet the quantitative evaluation (Table 1, left) only measures Clip Score and Aesthetic Score on a *single front view* — neither metric evaluates multi-view consistency. The "Views/One-Step" column counts capacity, not coherence across views. The user study does ask users to rate multi-view consistency (55.8%), but the study is described with limited detail (no confidence intervals, no specification of how "consistency" was defined to users, no significance tests). For a paper whose headline claim is about view consistency, the absence of any direct quantitative measure (e.g., pixel correspondence accuracy across views, 3D reconstruction error, or Chamfer distance) is a significant evidential gap. This is the most consequential weakness.

2. **Ablation studies are qualitative only, with no supporting quantitative results.** The ablations of TPL (Fig. 6) and SVS (Fig. 7a) rely entirely on visual comparisons and descriptive commentary ("decline of red cubes," "unshaped pillows"). Given that quantitative metrics (Clip Score, Aesthetic Score) are available and reported for the full method, the same metrics should be reported for each ablated variant. Without this, it is impossible to assess the marginal contribution of each module (OR, TO, OA, CA) objectively, and the paper's design claims rest entirely on subjective visual inspection.

3. **Non-standard use of "triplane" creates a framing mismatch with the established literature.** The paper uses "triplane" to refer to three orthogonal *RGB images* (front, top, side views) — calling this a "pixel-space triplane" (line 144) — whereas the established triplane literature (EG3D, 3DTopia, etc.) defines a triplane as three *feature planes* used for radiance field parameterization. The paper is not hiding this: it explicitly says "the front, top, and side views—completely orthogonal perspectives—are selected as the ground truth for the triplane" (line 100) and later encodes this "pixel-space triplane" via DINO (line 144). However, the repeated reference to EG3D (line 26) and the framing throughout ("triplane prior," "triplane latents") conflates two different representations. This creates needless confusion about what the method actually learns. The core technical contribution (orthogonal attention + view synthesis from three orthogonal RGB views) does *not* depend on calling the representation a triplane — but the framing misleads readers about how the representation relates to prior work. This requires substantial rewriting to fix.

### Minor

1. **Under-specified user study methodology.** The user study (Sec. 4.4) involves 48 users and 25 prompts but provides no details on: how users were recruited (expertise level), whether users saw all methods side-by-side or sequentially, what specific instructions defined "multi-view consistency" vs. "semantic consistency" for lay users, or how responses were aggregated (majority vote? average preference? pairwise comparison?). The reported percentages lack confidence intervals or statistical significance tests. This limits the credibility of the user study results as evidence.

2. **Qualitative comparison with prior-based methods uses different rendering settings per method.** The paper states (line 223) that for the prior-based comparison, "we pick 6 views... under their respective default settings (e.g., different elevations) with the optimal performance." Using different elevations across methods makes cross-method visual comparison of consistency unreliable — a viewer cannot tell whether differences in appearance are due to the method or the viewing angle. The fine-tuning comparison (Fig. 3a) does use the same views, which is better, but the inconsistency in the prior-based comparison weakens that qualitative evidence.

3. **The OA mathematical description (Eq. 4) uses notation that is likely incorrect or at minimum unclear.** Equation 4 uses `\prod_{M \in \textbf{P}_{1}}` — a product over all positions M in plane P1 — when standard attention computes a *sum* (weighted average). If the product is intentional, the mechanism is very unusual and needs justification. If it is a typo for `\sum`, the paper misleads readers about the implementation. Either way, the notation needs correction.

### Trivial
None.

## Nice-to-Haves

- **Justify the choice of DINO as the encoder** for the pixel-space triplane. The paper uses DINO without explaining why it is preferable over other encoders (CLIP, ViT, etc.) for this specific 3D task.
- **Provide confidence intervals for user study results** and report how responses were aggregated.
- **Add a quantitative multi-view consistency metric** (e.g., percentage of corresponding pixels with similar colors across views for visible surface points, or a 3D reconstruction metric against Objaverse ground truth).

## Removed Points

These points were raised by reviewers but are not included in the main weaknesses above:

- *"Missing references to Instant3D, DreamGaussian, LGM"* — REMOVED per instruction: do not mention missing related works as I cannot verify their relevance or existence.
- *"The baseline selection seems outdated"* — REMOVED per instruction: do not criticize missing related works.
- *"3DTopia performs poorly (Clip 25.87) due to unfair inference configuration; 3DTopia typically requires refinement"* — REMOVED: the paper explicitly states (line 205-206) that all methods are compared "using inference only without any additional optimization or refinement to ensure fairness." The reviewer's concern is addressed by the paper's explicit design choice.
- *"The claim that the method achieves 'any view in a single feed-forward inference' is overstated because SVS requires ray marching and an MLP decoder"* — REMOVED: "feed-forward" in this context means no per-scene optimization, which is standard usage in the general text-to-3D literature. The paper clearly describes the batch rendering process.
- *"Eq. 4 uses \prod where a sum is expected — formatting artifact"* — MOVED to Minor Weakness #3 as a genuine notation concern rather than a formatting nitpick, because it may represent an actual mathematical error.
- *"s.t.i appears to be a formatting artifact"* — REMOVED as a formatting artifact.
- *"Missing appendix, missing proofs in appendix"* — REMOVED per instruction: parser strips appendix content.
- *"The method is not what the paper claims it to be"* — REMOVED as an overstatement. The paper clearly describes what it does (generates three orthogonal RGB views and calls them a pixel-space triplane). The mechanism is transparent even if the terminology is non-standard. The terminology concern is kept in Major #3 with appropriate framing.

## Novel Insights

The most interesting insight from these reviews is that the paper's orthogonal attention mechanism represents a genuinely different approach to 3D correspondence than temporal attention used in video diffusion or the EG3D-style feature triplane regression. Rather than learning a latent feature triplane and regressing it directly (as in 3DTopia), SeMv-3D instead generates three RGB views and then *extracts* features from them via DINO, applying OA to maintain spatial correspondence. This two-stage design (RGB generation → feature extraction → arbitrary view rendering) is architecturally unusual and may explain why the paper achieves strong semantic alignment (since the TPL inherits T2I priors) while also maintaining multi-view consistency (via OA). The insight that OA on pixel-space images could serve as a bridge between 2D generation and 3D consistency is the paper's most interesting contribution, and is somewhat obscured by the "triplane prior" framing.

## Suggestions

1. **Reframe the method accurately.** Rename TPL's output from "triplane prior" to something like "orthogonal multi-view prior" (three generated views) and TPL to "Multi-View Prior Learner." Reserve "triplane" for the feature representation used in SVS after DINO encoding. This would eliminate the terminological confusion and align the paper with the established literature.

2. **Add a quantitative multi-view consistency evaluation.** Possibilities include: (a) computing pixel-wise correspondence accuracy for surface points visible across multiple rendered views of the same object, (b) reconstructing a mesh from the rendered views and measuring Chamfer distance or F-score against Objaverse ground truth, or (c) reporting the standard deviation of rendered pixel colors for the same surface point across views (lower = more consistent). Any direct measure would substantially strengthen the paper's central claim.

3. **Report quantitative results for all ablation variants.** Apply the same Clip Score and Aesthetic Score evaluations (plus the new multi-view consistency metric) to each ablated variant in Figures 6 and 7a. This would objectively validate the contribution of each module (OR, TO, OA, CA) rather than relying on visual inspection.

4. **Provide more detail on the user study protocol** (recruitment method, rater expertise, aggregation procedure) and report confidence intervals or effect sizes.

5. **Fix the OA equations (Eq. 4).** Replace `\prod` with `\sum` if that is what was intended, and clarify the notation for `s.t.i`. Add a diagram illustrating the query-key matching process for a pixel across orthogonal planes.

6. **Use identical viewpoints across all methods in qualitative comparisons**, especially for the prior-based methods in Fig. 3b, to enable direct visual comparison of multi-view consistency.

## Score and Decision

The paper makes a real technical contribution (orthogonal attention enforcing pixel-level correspondence across three orthogonal views, combined with a view synthesis pipeline that achieves both semantic alignment and multi-view consistency), and the results are competitive. However, two major weaknesses prevent acceptance: (1) the central claim of multi-view consistency is not directly measured by any quantitative metric, relying instead on single-view Clip/Aesthetic scores and an under-specified user study, and (2) the ablation studies lack quantitative support, reducing the ability to validate individual component contributions. Additionally, the terminological confusion around "triplane" needs substantial rewriting. These issues are addressable, and the underlying contribution has merit, but the paper in its current form does not provide sufficient evidence for its strongest claims.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>