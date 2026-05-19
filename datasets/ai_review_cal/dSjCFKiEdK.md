- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 5, 5, 5
Now I have all the information I need. Let me synthesize the final review after carefully verifying each claim against the paper.

## Summary

InstructBrush proposes a method for visual prompt editing — learning an edit concept from exemplar image pairs and applying it to new images via an InstructPix2Pix backbone. The two main technical contributions are (1) optimizing editing representations in the cross-attention K/V feature space (rather than text embedding space) to capture finer editing details, and (2) a CLIP-sensitivity-based initialization that extracts editing-relevant phrases while filtering out scene content that would hurt generalization. The paper also introduces TOP-Bench, a benchmark of 25 editing effects with 750 images.

## Strengths

- **Attention-based instruction optimization in cross-attention space (Section 4.1).** The paper identifies that prior instruction inversion (Visii) optimizes in text-embedding space, which loses detail because the text encoder is trained on coarse text-image pairs. Shifting optimization to the post-projection K/V features — which are spatially aligned with image features — is a well-motivated and technically sound choice. This directly addresses a known limitation of the prior art.

- **Transformation-oriented instruction initialization via CLIP sensitivity (Section 4.2).** The method extracts unique phrases by measuring CLIP similarity differences between pre- and post-edit image sets (Eqs. 5–6), then plugs these into an instruction template. This cleanly separates editing-relevant information from scene content that prior methods (Visii) would inadvertently bake into the instruction. The truncation condition (η=0.15) handles cases where no discriminative phrase exists, falling back gracefully.

- **TOP-Bench benchmark (Section 5).** The 25-editing-effect benchmark with 10+5 train/test pairs per effect is a concrete contribution. The split into TOP-Global (14 effects) and TOP-Local (11 effects) enables finer-grained evaluation. The field lacks standardized evaluation for visual prompt editing, and this benchmark fills a real gap.

## Weaknesses

### Fatal
None.

### Major

- **Underspecification of what exactly is being optimized in cross-attention.** Section 4.1 states that γ_K, γ_V ∈ ℝ^(m×d) are optimized "in the key and value corresponding to the first m tokens of the text instruction" across all n cross-attention layers. However, the paper never clarifies whether the pretrained K/V linear projection weights are frozen or bypassed, how γ_K, γ_V are initialized from the text encoder's output (do they start as the projection of the initial instruction's token embeddings, or are they randomly initialized?), or how gradient flow works when learned γ_K, γ_V coexist with projection-layer outputs for the remaining l−m tokens. The description "optimizing the features in the key and value" (line 66–75) is ambiguous between (a) directly setting post-projection K/V values (bypassing the projection weights) and (b) optimizing text embeddings that then pass through the frozen projection layers. These are two different methods with different properties, and a reader cannot tell which one is implemented. This ambiguity sits at the center of the paper's claimed contribution.

- **Time-aware instruction is incompletely specified.** Section 4.1 (Optional) divides optimization into j=5 parts based on denoising time steps and defines γ̄ = {γ_K, γ_V}^j_{1...n}, but never explains how these j separate sets of parameters are used at inference time. Are different γ sets activated for different denoising steps? Are they averaged? Concatenated? The paper refers to Figure 15 (presumably in the appendix) for validation of the time-dependent hypothesis, but the actual inference mechanism is absent. This component cannot be reproduced or properly evaluated from the description given.

### Minor

- **GPT-4o baseline is not a scientifically informative comparison.** The paper includes GPT-4o-based IP2P as a baseline (Section 6, "Compared Methods") and notes that it "cannot accurately extract the editing concepts between image pairs." This is expected — GPT-4o is orders of magnitude larger than the diffusion model and not designed for instruction inversion. Including it as a reference point is harmless, but the paper does not calibrate the comparison by acknowledging that this is a fundamentally different paradigm (LLM-based captioning + instruction-based editing) and not a directly comparable approach. The valid comparison against Visii already adequately supports the claims.

- **"pha (2022)" vocabulary reference is ambiguous.** Section 4.2 cites "pha (2022)" as the public vocabulary set for phrase extraction without specifying what this reference is. Since the vocabulary determines whether initialization succeeds or falls back to "None instruction," this should be clearly identified.

- **No sensitivity analysis for key hyperparameters.** Several parameters govern the method (η=0.15 truncation threshold, r=5 phrases, j=5 time partitions, m token count) with no analysis of their impact. A sweep over η alone would demonstrate robustness of the initialization.

- **No training/optimization details.** For a method requiring per-concept optimization, the paper provides no learning rate, number of optimization steps, or compute cost beyond a qualitative mention in Limitations.

### Trivial
None.

## Nice-to-Haves

- A small user study to substantiate the "semantic consistency" claim visually.
- Analysis of failure cases (e.g., when training image pairs are very similar, or when the edit is too subtle for the CLIP-sensitivity initialization).
- Correlation or consistency analysis of the multiple perceptual metrics (LPIPS, DINO, CLIP directional similarity) to help readers understand when they disagree.

## Removed Points
These points are flagged to be removed, treat them with caution:

- **Missing quantitative tables (Table 1, Table 2) in the extracted version.** This is a PDF extraction parser artifact, not an author error. The original submission contains these tables as images. The criticism about "quantitative evidence cannot be assessed" is removed per the rule against penalizing parser artifacts.
- **Data sources for TOP-Bench not described.** The paper states "Please refer to the Supplementary for data acquisition and detailed introduction" (Section 5). Appendix content is stripped in the review pipeline; the original submission contains this information.
- **"Equation 5 backpropagates through the entire U-Net" / "training cost not discussed."** This is standard practice for textual inversion-type methods. The paper acknowledges time cost in Limitations.
- **Formatting/layout nitpicks** (Figure 2 reference order, notation overload in Eq. 3). These are trivial and do not affect the technical content.
- **Missing related works / appendix content.** Per the rules, we do not penalize missing references when we cannot verify them externally, and appendix sections are stripped by the parser.
- **Speculative concerns about the sensitivity formula** ("if the edit is subtle, sensitivity may be small"). No evidence that this causes problems in practice; the threshold mechanism exists precisely to handle this.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the ambiguity in the cross-attention optimization formulation but do not provide a fundamentally new perspective on the problem that the paper itself does not articulate.

## Suggestions

1. **Clarify the attention optimization mechanism explicitly.** State in one clear sentence: (a) whether the pretrained K/V linear projection weights are frozen, (b) whether γ_K, γ_V replace the projection output or are added to it, (c) how they are initialized from the text encoder output of the initialized instruction, and (d) how the remaining l−m tokens' K/V features are handled. A diagram showing the gradient path would help substantially.

2. **Specify how the time-aware instruction's j sets of γ are used at inference.** Provide the exact mechanism — whether different γ sets activate at different denoising steps, or are combined.

3. **Report basic training hyperparameters** (learning rate, optimization steps) and compute cost (GPU hours per editing effect).

4. **Identify the "pha (2022)" vocabulary** by its full name or provide a citation that a reader can look up.

5. **Add a sensitivity analysis** for the truncation threshold η (e.g., sweep over {0.05, 0.10, 0.15, 0.20, 0.25}) to demonstrate that the method is not brittle to this choice.
