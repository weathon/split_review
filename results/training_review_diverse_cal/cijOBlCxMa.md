Now I have a complete understanding of the paper and the reviews. Here is my consolidated meta-review:

---

## Summary

CustomNet integrates explicit 3D viewpoint control ([R,T] camera parameters) into diffusion-based object customization, enabling simultaneous zero-shot control over viewpoint, location, and background while preserving object identity. The method extends Zero-1-to-3 with location concatenation, a dual cross-attention mechanism for disentangled object/background control, and a data construction pipeline that uses natural images from OpenImages as training targets. The core thesis — that explicit viewpoint conditioning is the missing ingredient preventing copy-pasting in encoder-based customization — is well-supported by ablation studies.

## Strengths

- **Novel integration of 3D viewpoint control into customization, with clear ablation support.** The paper identifies that existing encoder-based methods lack 3D awareness, leading to copy-pasting. The ablation in Fig. 4 (right panel) directly shows that removing the [R,T] viewpoint parameters causes the model to collapse into copy-pasting despite training on multi-view data. This cleanly isolates the contribution of viewpoint conditioning.

- **Strong qualitative results demonstrating viewpoint variation, identity preservation, and background harmony.** Fig. 2 and the qualitative comparison figures show outputs where object viewpoint changes substantially while identity (color, texture, structure) is maintained, backgrounds are coherent, and the result is not a simple copy-paste. This distinguishes CustomNet from prior zero-shot methods like BLIP-Diffusion, ELITE, and GLIGEN, which the qualitative results show struggling with identity.

- **Well-designed architectural components with supporting ablations.** The dual cross-attention (disentangling object and text conditioning) and the data construction pipeline (using natural images as targets rather than synthetic blends) are each ablated in Fig. 5, showing measurable degradation when removed. The 5th column of Fig. 5 demonstrates that without dual attention, viewpoint control degrades significantly.

- **Practical contribution: a data pipeline that reduces "floating" artifacts.** The pipeline reversing the typical synthetic-data approach — starting from natural images, segmenting foreground, and using Zero-1-to-3 to generate novel views as training targets — demonstrably improves output harmony compared to the naive Objaverse+background blending (Fig. 5, 4th column).

## Weaknesses

### Fatal
None.

### Major

1. **User study is critically under-documented.** The paper reports collecting 2700 answers with CustomNet preferred 78.78% (ID), 59.12% (View), and 66.33% (Text) of the time, but provides no details about: the number of participants, how they were recruited (AMT? internal? expert?), whether images were shown paired or side-by-side, whether order was randomized, what instructions were given, or whether participants could zoom/inspect details. Without this information, the user study results — which are a primary quantitative evidence pillar — are nearly uninterpretable. The field's best practices for human evaluation in generative models require at minimum participant count, recruitment method, and task description.

2. **Internal inconsistency between paper text and table for user study values.** The paper text reads: "(78.78%, 64.67%, 67.84%)," but the table reports View = 0.5912 (not 0.6467) and Text = 0.6633 (not 0.6784). While small, this discrepancy undermines trust in the numbers. Authors must clarify which values are correct.

### Minor

1. **Automatic identity metrics (DINO-I, CLIP-I) are partially confounded by the concatenation design.** The model receives the reference object as a concatenated input channel to the UNet (for location control), giving it direct pixel-level access to the reference that methods like DreamBooth, BLIP-Diffusion, and ELITE do not have. This inflates pixel-level and feature-level similarity scores compared to methods that work only through compressed embeddings. While the viewpoint control demonstrably prevents trivial copy-pasting (Fig. 4), the metrics still reflect the advantage of pixel-level reference access. The paper should acknowledge this architectural asymmetry as a caveat in the quantitative comparison, and ideally report identity preservation conditioned on the magnitude of viewpoint change (e.g., DINO-I stratified by small-angle vs. large-angle viewpoint changes).

2. **The training data pipeline may propagate Zero-1-to-3's systematic errors.** CustomNet is fine-tuned using Zero-1-to-3's own outputs as training targets (novel views generated from natural images), meaning any systematic errors Zero-1-to-3 has — such as texture stretching on unseen object categories or incorrect geometry for thin structures — could be learned and reinforced by CustomNet. The paper does not analyze this potential failure mode. A simple sanity check (e.g., evaluating on objects with ground-truth multi-view images) would strengthen the claim that the pipeline improves real-world performance.

### Trivial

1. **The dual cross-attention equation (Eq. 2) appears as an empty environment in the extracted text** — the formal mathematical formulation is missing. The prose description is adequate, but a precise equation would aid reproducibility.

2. **The claim "first attempt to concurrently control viewpoint, location, and background"** (line 84) is defensible given the specific integration, but the framing could be tightened to "first to integrate explicit 3D viewpoint parameters into a diffusion-based customization framework with simultaneous location and background control" to avoid potential quibbles about scope.

## Nice-to-Haves

- A viewpoint preservation metric (e.g., estimated pose error between requested and achieved camera pose, computed via off-the-shelf pose estimator or on a subset with known 3D models) would directly support the paper's central claim about viewpoint control.
- An ablation removing concatenation while retaining viewpoint control would isolate whether concatenation is needed only for texture detail or also contributes to identity preservation scores.

## Removed Points

These points from the reviewers were flagged for removal per the filtering guidelines:

- **Missing comparison to Custom Diffusion (Kumari et al., 2023):** Per guidelines, I cannot verify the existence or relevance of this paper independently. Removed as an unverifiable missing-related-work criticism.
- **"Metrics cannot be taken at face value" / "implausibly high user study results":** The reviewer's claim that user study numbers are "implausibly high" is an unsupported judgment. The table values (59.12% for View, 66.33% for Text, 78.78% for ID) are strong but not unprecedented for a method with a genuinely new capability like viewpoint control. The real issue (insufficient documentation) is preserved in Major Weaknesses.
- **The metrics "do not measure what they claim":** Overstated. DINO-I/CLIP-I measure identity similarity between output and reference. Since the model changes viewpoints (not copy-pastes), these metrics do measure identity preservation. The confound from concatenation is real (preserved in Minor) but the claim that they "do not measure what they claim" is a strawman.

## Novel Insights

The integration of 3D viewpoint conditioning into object customization — and specifically the finding that *without* explicit [R,T] parameters, the model degenerates into copy-pasting even when trained on multi-view data — is the paper's most valuable insight. This provides a clear architectural explanation for why prior encoder-based methods produce nearly identical outputs to their inputs: they lack any mechanism to represent or generate a different 3D orientation of the object. The concatenation + viewpoint conditioning combination elegantly resolves this: concatenation provides texture detail, viewpoint conditioning provides geometric diversity.

## Suggestions

1. Document the user study protocol in full: number of participants, recruitment method, task interface (paired/unpaired, randomization), instructions given, and whether participants were screened.
2. Reconcile the text/table discrepancy for View and Text user study percentages.
3. Add a discussion of the concatenation confound in the quantitative evaluation, and consider stratifying DINO-I/CLIP-I by viewpoint change magnitude.
4. Discuss the limitation that Zero-1-to-3 generated views are used as training targets, and ideally provide a small-scale validation against ground-truth multi-view data.
5. Fill in the missing equation for dual cross-attention in the camera-ready version.

## Score and Decision

**Summary evaluation across axes:**
- **Originality:** High. First work to explicitly inject 3D viewpoint control into object customization, with a clean architectural solution.
- **Importance:** High. Copy-pasting is a known weak spot of encoder-based customization; this work directly addresses it.
- **Claims support:** Moderate-strong. Core claim (viewpoint control prevents copy-pasting) is well-supported by ablation. Quantitative comparisons are weakened by the concatenation confound and under-documented user study.
- **Soundness:** Moderate. Methodologically sound, but evaluation has gaps (user study documentation, metric caveats).
- **Clarity:** Good. The paper is well-structured and the ablations clearly communicate the contribution of each design choice.
- **Value:** High. The approach is practical (zero-shot, controllable) and the architectural insights are transferable.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>