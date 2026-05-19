- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5
Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

## Summary

This paper proposes the first dataset distillation method for vision-language data, extending trajectory matching (MTT) to multimodal settings. The method jointly distills image-text pairs as synthetic (image, continuous text embedding) pairs by matching bi-trajectories of student models (trained on the distilled set) against expert trajectories (trained on the full dataset) using bidirectional contrastive loss. A LoRA matching variant enables trajectory matching with modern ViT architectures. On Flickr30K and COCO, the method achieves substantial improvements over adapted coreset selection baselines (e.g., 9.9% vs. 1.3% TR R@1 at 100 pairs on Flickr30K).

## Strengths

1. **First method for vision-language dataset distillation, with clear problem formulation.** Section 3.1 formalizes the task as distilling (image, text) pairs in a contrastive, class-free setting — a genuine extension beyond prior class-conditional distillation. Section 3.4 introduces LoRA matching to handle high-resolution images and complex ViTs, solving two of the three stated challenges (no discrete classes, model complexity).

2. **Large and consistent performance gains over adapted coreset baselines.** Table 1 shows that on Flickr30K, with 100 distilled pairs, the method achieves 9.9% TR R@1, while the best coreset method (Random) using 1,000 pairs reaches only 5.6%. The advantage holds across all budgets (100–1,000 pairs) and both datasets, with relative improvements of 138%–661%. The full-data upper bound (Table 2) provides useful calibration context.

3. **LoRA matching is shown to be crucial for ViT-based distillation.** Table 3 (the LoRA table) shows that without LoRA, ViT distillation achieves only 1.5% TR R@1 (100 pairs, Flickr30K); with LoRA (r=4, reducing stored parameters by 78.71%), performance jumps to 10.4%, nearly matching the NFNet-based result. This demonstrates a real architectural insight: trajectory matching over full ViT parameters fails, while matching low-rank adapter trajectories succeeds.

4. **Co-distillation ablation cleanly validates the joint-modality design.** Table 5 (ablation) shows co-distillation (9.9% TR R@1 at 100 pairs) more than doubles the best unimodal alternative (image-only at 3.5%), cleanly isolating the benefit of joint optimization.

5. **Cross-architecture transfer is demonstrated.** Table 4 shows NFNet-distilled data transfers to NF-ResNet50, NF-RegNet, and ViT, and vice versa, replicating a desirable property of prior trajectory matching methods in the multimodal setting.

## Weaknesses

### Fatal
None.

### Major

1. **The forward-pass architecture for distilled text during student training is underspecified, creating a verifiability gap.** The paper states that distilled text exists as "continuous sentence embeddings" (line 148) obtained via BERT (line 172), and is visualized via nearest-neighbor decoding (line 250, Figure 3 caption). However, the paper never specifies how these continuous embeddings are actually *consumed* by the student model during training on the distilled set. The described student architecture (line 166) is: text → frozen BERT → trainable projection layer. If BERT expects discrete tokens, how does the student forward pass process the continuous embedding? The most plausible answer (bypass BERT's encoding layers and feed the continuous embedding directly into the projection layer during student training on distilled data) is never stated. This is not a trivial omission — it affects whether a reader can understand, reproduce, or verify the method. The paper should explicitly describe (a) how the continuous embedding is integrated into the student model's forward pass, (b) whether BERT is entirely bypassed during student training on distilled data, and (c) how the model switches between this forward path (during distillation training) and the standard BERT-based path (during evaluation on real text).

### Minor

2. **Text parameter trajectory matching is underspecified given frozen BERT.** The paper states (line 166) that BERT is frozen, yet Eq. 4 includes a text trajectory matching term $\|\hat{\theta}_{txt, s+\hat{R}} - \theta^*_{txt, s+R}\|_2^2$. If BERT is frozen, "text parameters" can only refer to the trainable projection layer (and possibly LoRA adapters). The paper should explicitly state what text-side parameters are being trajectory-matched and quantify their count relative to the image-side parameters, so readers can assess how much of the trajectory matching operates on language-specific information vs. projection-layer alignment.

3. **Framing inconsistency: "train a new model from scratch" vs. using pretrained encoders.** The abstract (line 4) states the method aims to "quickly train a new model from scratch," but the experimental setup (line 166) uses pretrained NFNet and frozen BERT. The method finetunes pretrained models rather than training from scratch. This is a small but notable inconsistency that should be corrected for precision.

4. **Standard deviations not reported for baseline methods.** Table 1 reports standard deviations for the proposed method (over 5 evaluation runs on the same distilled set) but not for the coreset baselines. This makes it harder to assess whether the performance gap is statistically significant. The paper would be strengthened by providing comparable variance estimates for baselines.

5. **The "without LoRA" ViT comparison is discussed but not fully analyzed.** Table 3 shows that ViT without LoRA yields very low performance (1.5% TR R@1 at 100 pairs). The paper attributes this to "attention mechanisms" (line 246), but an equally plausible explanation is that full ViT trajectories (86M parameters) are impractical to store and match effectively. The paper should clarify what is stored in the expert trajectory for the "without LoRA" case and whether the failure is architectural or a consequence of parameter scale.

### Trivial
- None beyond what is addressed above.

## Nice-to-Haves

- A comparison to training on the same budget of real image-text pairs (e.g., 100 random pairs with the same LoRA/projection setup) would calibrate the practical value of synthetic data over simple subsampling.
- An analysis of how the number of saved expert trajectories (currently 20) affects performance.
- A discussion of the computational trade-off: expert training (10 epochs on full data) + distillation (6–15 GPU hours) vs. simply training on the full dataset once.

## Removed Points

The following points from the original reviews are removed with justification:

- **"Baseline comparison is limited / staged"** (Harsh Critic #3) — Removed because: (a) the paper is the *first* on this task, so no prior distillation methods exist to compare against; (b) Table 1 reports all budgets, so the "budget mismatch" claim about comparing 100 distilled to 1,000 coreset is misleading — the paper also shows 100 vs. 100 (9.9% vs. 1.3%). The abstract highlights the 100-vs-1000 comparison for emphasis but does not hide any data.
- **"High learning rates (1000) are extreme"** — Removed because learning rates for distilled image pixels and text embeddings operate in data-space optimization, not model weight space. This is standard practice in dataset distillation (MTT uses similar orders of magnitude).
- **"Image-only ablation not explained"** — Removed because the context (line 343: "keep one of the modalities fixed during distillation") makes the setup clear enough.
- **"Cross-architecture drop not discussed"** — Demoted from the critic's implied severity since the paper's Limitations section (line 358) explicitly acknowledges that distillation effectiveness is "highly influenced by learning algorithms and models used," which covers transferability limitations.
- **All formatting/style nitpicks, missing appendix concerns, and speculative weaknesses about unreleased resources** — Removed per hard rules.

## Novel Insights

The harsh critic's central concern about the continuous text embedding pipeline, while over-claimed as "structural" and "fatal," does surface a genuine clarity gap that neither the strength finder nor the paper itself fully addresses. The paper describes what the distilled text *is* (continuous 768-d embedding) and how it is *visualized* (nearest-neighbor decoding), but critically omits the middle — how the student model's forward pass integrates this embedding during training. This is the kind of omission that may be obvious to the authors but stops a reader from reproducing the work. Separately, the strength finder correctly identifies that the LoRA matching result (1.5% without LoRA → 10.4% with LoRA) is the most technically informative result in the paper, going beyond a pure performance claim to reveal a genuine scaling insight about trajectory matching with high-capacity models.

## Suggestions

1. **Clarify the text embedding forward pass.** Add a paragraph or a figure detail explaining: (a) during student training on distilled data, the continuous text embedding $\hat{y}_j$ is fed directly to the trainable projection layer (bypassing BERT's token → embedding pipeline); (b) during evaluation on real text, the standard BERT encoding path is used. This single clarification resolves the largest ambiguity in the paper.

2. **Specify what constitutes $\theta_{txt}$ for trajectory matching.** State explicitly: when BERT is frozen, the text parameters in Eq. 4 are only the projection layer weights (and LoRA matrices, if used). Report their parameter count alongside the image-side parameter count.

3. **Correct the "from scratch" phrasing.** Replace "train a new model from scratch" with "train a new model" or "finetune a pretrained model" to match the actual procedure.

4. **Report baseline standard deviations.** Even a simple note (e.g., "baseline std computed over 3 random seeds") would improve the interpretability of the reported improvements.
