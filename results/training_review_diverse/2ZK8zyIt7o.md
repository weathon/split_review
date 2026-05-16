Now let me produce the final consolidated review.

---

## Summary

This paper proposes two main contributions for improving long-text alignment in text-to-image diffusion models: (1) a segment-level encoding method that divides long texts into segments, encodes each separately, and merges the embeddings with special-token adjustments, enabling CLIP to process arbitrarily long inputs; (2) a decomposed preference optimization approach that identifies a text-irrelevant component in CLIP-based preference scores (the "cone effect") and reweights it during reward fine-tuning to mitigate overfitting. After fine-tuning SD v1.5 (512×512) for ~20 hours, the resulting model (longSD) shows improved alignment on the authors' evaluation metrics compared to stronger foundation models including PixArt-α and Kandinsky v2.2.

## Strengths

1. **Preference decomposition analysis is insightful and well-motivated.** The paper identifies that CLIP-based preference scores can be decomposed into a text-relevant component (measuring T2I alignment) and a text-irrelevant component (capturing aesthetics, photorealism, etc.), and that the latter dominates the optimization direction during reward fine-tuning. This analysis is supported by the "cone effect" visualization (Figure 2), retrieval accuracy comparisons (Table 1), and the score decomposition in Figure 2(c). The insight that this text-irrelevant component drives overfitting is plausible and practically useful.

2. **Gradient reweighting strategy is simple, principled, and effective.** Building on the decomposition, the paper proposes reweighting the text-irrelevant gradient component (ω < 1), showing in Figure 5 that ω=0.3 maintains stable FID while improving both Denscore and Denscore-O, whereas unweighted training leads to overfitting (FID degradation). The visual comparisons in Figure 6 further demonstrate the qualitative benefit. This is a clean, computationally lightweight intervention with clear motivation.

3. **Segment-level encoding provides a practical solution to CLIP's token limit.** The ablation on special-token handling (removing `<eot>` embeddings, replacing `<pad>` with a unique `<pad*>`) for concatenating segment embeddings is a technically sound engineering contribution. This enables CLIP—which has pretrained image-text alignment capabilities—to be used alongside T5 in the final CLIP+T5 configuration, combining the strengths of both encoders.

4. **Reasonable compute-to-performance ratio.** The paper demonstrates that fine-tuning a relatively small model (SD v1.5) for ~20 hours on 6 A100s can yield competitive long-text alignment, which is a practically relevant finding. The comparison against P2I diffusion (Table 3) within the same framework shows consistent improvements.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation relies heavily on the authors' own metric (Denscore) and evaluation set, with no standard benchmark results presented in the main paper.** The paper mentions evaluating on DPG-Bench (Section 5.1, last sentence) but never reports the results in any results section or figure. DPG-Bench is a widely used benchmark for long-text alignment, and its absence means the headline claim of "outperforming stronger foundation models" rests primarily on metrics computed on a 5k-image subset of the authors' own training distribution. GPT-4o evaluation (Figure 7) partially mitigates concerns about metric overfitting, but GPT-4o is itself an imperfect proxy. The paper would be substantially stronger with DPG-Bench or other standard benchmark results.

2. **The ablation establishing ω=0.3 (Figure 5) uses CLIP-cat encoding with LCMLoRA+DRTune, but the final longSD model uses CLIP+T5 with full fine-tuning.** The paper acknowledges that "the optimal value of ω can vary depending on the model and training strategy used" but provides no sensitivity analysis or verification that ω=0.3 transfers to the final CLIP+T5 configuration. This leaves a gap between the ablation study and the actual method used for the main results in Table 2.

3. **The causal mechanism linking the text-irrelevant component to overfitting is plausible but not rigorously established.** The evidence is: (a) V exists, (b) reweighting V (ω < 1) improves results. However, the paper does not directly measure whether overfitting artifacts correlate with the magnitude of V's gradient contribution, nor does it ablate the reweighting independently of other components (e.g., DRTune, the particular ω selection). The improvement from reweighting could also be explained by V acting as a noisy gradient direction or a regularizer, without the specific causal chain claimed. The mechanism is a reasonable hypothesis, but the paper presents it as a finding rather than a conjecture supported by correlational evidence.

### Minor

1. **Resolution difference between SD v1.5 (512×512) and baselines like PixArt-α/Kandinsky (1024×1024) is not addressed in the evaluation setup.** While FID computation typically resizes all images to 299×299 for Inception feature extraction (making this less of an issue than it first appears), the paper does not explicitly state whether baseline images were handled consistently. This is a clarity issue that invites scrutiny of the headline comparison.

2. **The role of segment-level encoding in the final system is somewhat underspecified.** The paper presents segment-level encoding as a contribution for diffusion models (Section 3.1), but Figure 4 shows that CLIP-cat (segment-level CLIP alone) performs similarly to T5-mlp, while CLIP+T5 drives the real gains. The segment-level encoding is a necessary enabler for CLIP to participate in the CLIP+T5 combination, but the paper's framing as a standalone contribution to diffusion model encoding is not fully supported by the results. The contribution is clearer for the preference model (Denscore) than for the diffusion model itself.

3. **The assumption that V encodes only text-irrelevant information is strong and only partially validated.** The paper shows that V correlates with image aesthetics (Figure 3), but does not demonstrate that manipulating V leaves text-relevant alignment unchanged while manipulating the orthogonal component affects it. The retrieval accuracy results in Table 1 provide indirect support by showing that removing V improves alignment-focused retrieval, but a more direct validation (e.g., showing that modifying V does not change text-alignment metrics) would strengthen the claim.

4. **The FID of 86.40 for the original SD-1.5 is unusually high** and not contextualized against standard FID references. This makes the subsequent improvements less interpretable. Reporting FID on a standard dataset (e.g., COCO validation) would provide helpful context.

5. **The P2I diffusion comparison (Table 3) mentions GPT-4o evaluation but the numbers are not clearly presented** (the table appears only as an image with unreadable values in the text extraction). The paper should ensure these results are legible.

### Trivial

- None.

## Nice-to-Haves

- **Human evaluation** on a small set of long-text prompts would strengthen the claim about "improving alignment," since GPT-4o is itself an imperfect proxy for human judgment of factual correctness.
- **Gradient norm analysis** tracking the contribution of V vs. the orthogonal component during training would more directly support the causal claim about overfitting.
- **Failure case analysis** would help clarify remaining gaps (the Discussion acknowledges limitations with complex dependencies—showing concrete examples would be useful).
- **Inference cost** of the segment-level encoding is not discussed.

## Removed Points

These points were flagged by reviewers but are excluded from the main assessment for the reasons stated:

1. **"Reproducibility issue because details are in the appendix/supplementary material and code is in supplementary material"** — Removed per hard rule: the parser strips appendix and supplementary sections from all papers; they exist in the original submission. The paper states code and checkpoints will be released.

2. **"No comparison with other fine-tuning methods like T5-only models"** — Removed: this is scope creep. The paper compares with P2I diffusion (the most relevant training-strategy competitor) and demonstrates their method can be applied orthogonally.

3. **"No human evaluation"** — Downgraded to Nice-to-Haves. GPT-4o evaluation is a reasonable proxy used in many recent papers; its absence is not a fatal gap.

4. **"The paper should report FID on COCO2017 validation"** — Removed: the paper's evaluation is on long-text prompts where standard FID references like COCO are not directly comparable. The 5k evaluation set is appropriate for the paper's focus.

5. **"Segment-level encoding is not used in the final system"** — This is factually incorrect. The final system uses CLIP+T5, and CLIP requires segment-level encoding to handle long texts; segment-level encoding is what enables the CLIP component of CLIP+T5. The criticism was partially valid about clarity but overstated in substance.

6. **"Criticism that the cone effect analysis makes a strong assumption"** — Kept in Minor (point #3) but weakened from the reviewer's framing. The paper provides several forms of validation (retrieval accuracy, score tables, visualizations) that support its interpretation even if not definitively proving it.

## Novel Insights

The reviewer contributions do not surface any genuinely novel insight beyond the paper's own contributions. The observation that the text-irrelevant component of CLIP-based preference scores causes overfitting during reward fine-tuning is the paper's own finding, and the reviewers' analyses largely corroborate or refine this rather than adding new perspectives.

## Suggestions

1. **Add DPG-Bench results** (and at least one other standard long-text benchmark) to the main paper. This is the single most impactful change: it would demonstrate that the alignment gains generalize beyond the authors' own dataset and metric.

2. **Verify the ω=0.3 setting for the final CLIP+T5 configuration.** Even a single ablation showing that ω=0.3 (vs. ω=1.0) also transfers to the full system would close the gap between the ablation study and the main results.

3. **Clarify the role of segment-level encoding.** Explicitly state that segment-level encoding is the method that enables CLIP to handle long texts in the CLIP+T5 combination, and that the main performance gains come from combining both encoders. If this is the case, the contribution framing should match.

4. **Address the resolution comparison explicitly.** State whether baseline images (from PixArt-α, Kandinsky) were resized before FID computation, and whether any downsampling artifacts could affect the comparison.

5. **Add a gradient norm analysis** during training to show that the text-irrelevant component's gradient magnitude correlates with overfitting patterns. This would significantly strengthen the causal narrative.

## Score and Decision

This paper presents genuinely useful contributions—the preference decomposition analysis and gradient reweighting are practically valuable insights, and the empirical results on the authors' evaluation set are consistent. However, the evaluation relies too heavily on the authors' own metric (Denscore) and evaluation set, and the absence of standard benchmark results (DPG-Bench is mentioned but not shown) means the headline claim of "outperforming stronger foundation models" is not fully supported by the evidence provided. The gap between the ablation setup (CLIP-cat, LCMLoRA) and the final system (CLIP+T5, full LoRA) further weakens the empirical story. These issues are addressable but in the current form the paper's strongest claims outrun its evidence.

**Originality**: Good — preference decomposition and gradient reweighting are novel.  
**Importance of question**: High — long-text alignment is a recognized challenge.  
**Claims supported**: Partially — claims about outperforming foundation models need stronger independent evaluation.  
**Soundness of experiments**: Adequate but with gaps noted above.  
**Clarity**: Generally clear, though the role of segment-level encoding could be better scoped.  
**Value to community**: Moderate — the insights about text-irrelevant gradient components are practically useful.

Score: 5.5

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>