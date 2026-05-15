I now have all the information needed. Let me produce the final consolidated review.

## Summary

The paper proposes ExVideo, a parameter-efficient post-tuning approach for extending video diffusion models. Applied to Stable Video Diffusion, the method extends generation from 25 to 128 frames (5×) using only 1,500 GPU hours by fine-tuning only temporal modules (temporal attention, positional embeddings) and adding a small identity-initialized 3D convolution layer. The approach keeps most parameters frozen and leverages standard memory-saving techniques.

## Strengths

- **Practical 5× frame extension with modest training cost**: The method extends SVD from 25 to 128 frames using only 1.5k GPU hours on 8 A100 GPUs with a 40k-video dataset. This is a genuine efficiency contribution — full fine-tuning at this scale would be prohibitively expensive, and prior approaches (streaming, interpolation) fail to extend narrative time or maintain coherence (Section 3.3).

- **Principled initialization preserves pre-trained behavior**: The identity 3D convolution kernel is initialized with an identity center and zeros elsewhere, ensuring no change to video representations before training (Section 3.2). The cyclic initialization of extended positional embeddings leverages the existing embedding structure. These design choices are well-motivated and avoid disrupting the base model's capabilities.

- **Qualitative evidence of generalization**: The generated examples show the model handling diverse styles (flat anime, pixel art — unseen during training) and resolutions not encountered during post-tuning (Figures 2, 4, 5). While qualitative, this visual evidence supports the claim that the base model's generalization abilities are retained.

- **Detailed memory-efficient training recipe**: The paper specifies a concrete set of engineering optimizations — parameter freezing, mixed precision, gradient checkpointing, Flash Attention, DeepSpeed sharding — making the approach reproducible (Section 3.3).

## Weaknesses

### Fatal

None. The core claim — that the method can extend video generation duration with limited compute — is supported by the fact that the model was successfully trained to produce 128-frame videos, and qualitative results show plausible, coherent outputs. The weaknesses below are serious but do not invalidate the existence of the contribution.

### Major

- **No quantitative evaluation whatsoever**: The paper presents zero numerical metrics (FVD, IS, CLIP score, frame consistency, user study, or any other standard benchmark). Every claim about quality, coherence, and motion realism rests entirely on a handful of cherry-picked keyframes and optical-flow visualizations. In a field where FVD on UCF-101 or similar benchmarks is the established evaluation standard, this omission makes it impossible to assess the method's quality relative to alternatives or to verify that quality does not degrade over the 128-frame horizon. The authors acknowledge that the base model struggles with human portraits (Section 5) but provide no systematic analysis of failure modes or quality degradation across the extended frame count. This is the single most consequential weakness in the paper.

- **Vague and uncontrolled comparison with baselines**: Section 4.4 claims comparisons against "several existing video synthesis models" but never names which models, versions, seeds, prompts, or first frames were used. The only reported observation is that other models produce "minimal motion" while ExVideo generates "significant movements." Motion magnitude is not a proxy for video quality, and without controlling for conditions or using any quantitative motion metric, this comparison carries no evidentiary weight. The paper does not claim broad superiority, but this section still attempts to position the method favorably without rigorous support.

- **No ablation studies for design choices**: The method introduces three modifications: (1) fine-tuning temporal attention, (2) extended cyclic-initialized positional embeddings, (3) an additional identity 3D convolution layer. No ablation is provided to justify these choices. The reader cannot determine whether all three components are necessary, whether simpler alternatives (e.g., linear interpolation of positional embeddings, LoRA on temporal modules, or direct full fine-tuning) would perform similarly, or whether the identity 3D convolution contributes meaningfully. This limits the paper's scientific contribution as a methodology paper.

### Minor

- **"Cyclic initialization" is not precisely defined**: The paper states that extended positional embeddings are "initialized in a cyclic pattern, drawing upon the configurations of the pre-existing embeddings" (Section 3.2). It does not specify whether this means repeating the existing 25 embeddings cyclically, interpolating between them, or some other scheme. This is an implementation detail that would need to be clarified for reproducibility.

- **Identity 3D convolution kernel size and architecture not specified**: The paper mentions "the central unit of this 3D convolution kernel is initialized as an identity matrix" but does not state the kernel size (e.g., 3×1×1, 3×3×3) or where exactly in the temporal block it is inserted (beyond "subsequent to the positional embedding layer"). These details matter for understanding the method's parameter cost and inductive bias.

- **The training dataset (40k videos, 512×512) differs from SVD's original training distribution**: The paper uses OpenSoraPlan at 512×512, while SVD was trained at different resolutions. No discussion is provided on potential domain shift or its effects, even though the model is later evaluated at higher resolutions (Figure 5).

- **Limitations section is thin**: Section 5 acknowledges that human portrait synthesis fails but provides no quantification (rate, severity, or examples). The main limitation cited ("lack of a robust base model") reads more as a justification for the current results than as a genuine critical self-assessment of ExVideo itself.

### Trivial

None that survive filtering.

## Nice-to-Haves

- **Standard quantitative evaluation (FVD/CLIP)** on a benchmark like UCF-101 or a comparable video dataset, for both 25-frame and 128-frame generation, compared against the original SVD at its native length and against simple baselines (e.g., frame interpolation of SVD outputs, streaming generation).
- **Ablation experiments** comparing the full ExVideo against variants that: (a) only extend positional embeddings, (b) only fine-tune temporal attention, (c) use linear interpolation instead of cyclic initialization, (d) omit the identity 3D convolution.
- **Frame-by-frame quality analysis** showing how metrics evolve from frame 1 to 128, to verify the claim that quality does not degrade over the extended horizon.
- **Application to at least one additional video diffusion model** (e.g., AnimateDiff) to support the claim of generality.
- **Side-by-side video comparisons** (in supplementary material) with named baselines under controlled seeds and prompts.

## Removed Points

These points are flagged to be removed, treat them with caution:

- The harsh critic's framing that the paper claims to "outperform existing models" broadly. The paper's actual comparative claim is narrower: it notes that other models produce "minimal motion" while ExVideo generates "significant movements." The critic overstates this into a general superiority claim. I have retained the substance (vague comparison is a real weakness) but softened the framing.
- The harsh critic's statement that "the paper claims superiority based on such evidence" is somewhat inflated. The paper's claims in the abstract and contributions are about extending duration and preserving generalization, not about benchmark-beating performance. Retained as the comparison section still attempts a qualitative differentiation without rigor.
- General requests for "larger dataset" or "more models to test on" that go beyond the paper's stated scope are moved to Nice-to-Haves.

## Novel Insights

None beyond the paper's own contributions. The insight that post-tuning — a technique from LLM context extension — can be adapted to video diffusion models by treating the temporal modules analogously to LLM positional-embedding and attention layers is the paper's core novel perspective. The reviews do not surface any additional cross-field pattern or unexpected implication.

## Suggestions

1. **Add FVD scores on a standard benchmark** as the highest priority. Even a single-table comparison against SVD-native (25 frames), frame-interpolated SVD (25→128), and a streaming baseline would drastically strengthen the paper. This is the one change that would most improve assessability.
2. **Name the comparison baselines explicitly** in Section 4.4 and, if possible, include a controlled quantitative comparison (e.g., average optical flow magnitude per frame, or a human preference study on motion naturalness).
3. **Add at minimum one ablation** to justify the identity 3D convolution — e.g., compare with vs. without this component. This would differentiate the paper from a straightforward "fine-tune temporal attention + extend positional embeddings" baseline.
4. **Clarify the cyclic initialization scheme** (is it repetition, interpolation, or something else?) and **specify the 3D convolution kernel dimensions**.
5. **Provide failure analysis beyond human portraits** — e.g., what fraction of generated videos show noticeable artifacts, flickering, or motion collapse? Even a few systematic categories would improve the paper's scientific rigor.

## Score and Decision

The paper presents a timely and practically motivated idea with plausible qualitative results. However, the evaluation is fundamentally incomplete by current community standards: zero quantitative metrics, no named baselines, no ablation studies, and only vague comparisons. The core methodological contribution is real, but the evidentiary bar for acceptance is not met. A revision with proper evaluation could make this a strong paper.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>