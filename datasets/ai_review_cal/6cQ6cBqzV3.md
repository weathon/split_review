- Decision: Accept
- Avg Score: 5.75
- Scores: 8, 6, 6, 3
Now I have all the information needed. Let me synthesize the final review.

## Summary
This paper introduces LoRA-X, a low-rank adapter constrained to the singular subspace of its base model, enabling training-free transfer between different base models without requiring original or synthetic training data. The core idea is to parameterize the adapter as $\tilde{U}\Delta\Sigma\tilde{V}^\top$ using the truncated SVD of the base model weights, then project it onto a target model's subspace via the closed-form formula $U_t U_t^\top \Delta W_s V_t V_t^\top$. The paper evaluates the method on text-to-image style transfer across diffusion models in the SD 1.5 and SDXL families.

## Strengths

- **Novel subspace-constrained adapter design that enables training-free transfer**: The paper formalizes a key insight — constraining the adapter update to the base model's singular subspace (Eq. 1) ensures it satisfies $UU^\top\Delta W VV^\top = \Delta W$ (Eq. 2), making it inherently projectable onto a target model's subspace. This design is clearly distinguished from SVDiff, whose goal is parameter efficiency rather than transferability (Section 4.1).

- **Elegant closed-form projection transfer method**: The transfer formula (Eq. 3) $\Delta W_{t\leftarrow s} = U_t U_t^\top \Delta W_s V_t V_t^\top$ is simple, principled, and requires no data or training. The ablation in Table 5 convincingly demonstrates that this projection step is critical: naively copying $\Delta\Sigma_s$ directly to the target (without subspace projection) causes a significant performance drop (DINO 0.851 vs. 0.896).

- **Strong ablation studies validating the subspace constraint**: Table 2 shows that standard LoRA (without the subspace constraint) degrades substantially when projected to a different base model (DINO 0.830 for LoRA vs. 0.896 for LoRA-X transferred). Table 6 reveals that transferred LoRA-X remains robust to rank reduction while trained LoRA-X degrades — an interesting and non-obvious finding. Table 7 validates transfer from a smaller source (SD Eff-v1.0) to a larger target (SD-v1.5).

- **Convincing results within the demonstrated scope**: Table 1 shows that for same-family transfers (SD-v1.5 $\to$ SD Eff-v1.0, SDXL $\to$ SSD-1B), the transferred LoRA-X achieves HPSv2 and LPIPS scores very close to those of a LoRA-X trained directly on the target model (e.g., BlueFire: 0.286 vs. 0.303 HPSv2; 0.652 vs. 0.656 LPIPS), supporting the paper's core claim.

## Weaknesses

### Fatal
None.

### Major

- **No variance or statistical significance reporting despite 30 seeds**: The paper reports that results are "averaged over 30 seeds" (Table 1 caption) but provides no standard deviations, confidence intervals, or any measure of uncertainty. The central claim is that "Transferred LoRA-X performs comparably to the one Trained with the datasets" (line 193). For example, BlueFire's HPSv2 shows 0.274 (Trained) vs. 0.272 (Transferred) on SD Eff-v1.0 and 0.303 vs. 0.286 on SD-v1.5 → SD Eff-v1.0. Without error bars, the reader cannot assess whether these differences are within noise or represent real degradation. This is the single most impactful weakness, as it undermines confidence in the paper's headline result.

- **Different-dimension transfer method (Section 4.2.2) is proposed but never experimentally validated**: The paper presents a least-squares linear transformation approach for cases where source and target dimensions differ, but all experiments involve same-architecture transfers (SD 1.5-family models share architecture dimensions; SDXL-family models share architecture dimensions). The paper claims "cross-model transfer" broadly, but the empirical evidence is limited to same-dimension, same-family transfers. The scope should be explicitly bounded, and Section 4.2.2 should either be accompanied by experiments or clearly marked as speculative/future work.

### Minor

- **ATC metric proposed but not validated as a predictor**: The Adapter Transferability Cost is defined in Section 4.2.4 and plotted in Figure 4 for various model pairs. However, no experiment demonstrates that ATC *correlates with actual transfer performance*. The paper already uses per-layer subspace similarity to select which layers to transfer; it remains unclear what the global ATC adds beyond a descriptive statistic. A simple validation (e.g., correlating ATC values with downstream HPSv2 for a set of source-target pairs) would turn this from a suggestion into a contribution.

- **Evaluation metrics lack sufficient specificity**: DINOv2 is described as measuring "similarity based on embedded representations" (line 182), but it is never specified *between what and what* — e.g., cosine similarity between DINO embeddings of images from trained vs. transferred adapters, or between generated and reference images? HPSv2 absolute values (~0.27) are not contextualized with a reference range. Adding a sentence clarifying each metric's computation and providing a baseline (e.g., a non-fine-tuned model's score) would significantly improve interpretability.

- **No experimental comparison with Trans-LoRA**: Trans-LoRA (Wang et al., 2024) is cited in the related work as the most relevant prior method for data-free adapter transfer. While Trans-LoRA uses synthetic data (unlike LoRA-X, which is fully data-free), a direct comparison would clarify the practical advantage of LoRA-X. The paper compares to X-Adapter, but Trans-LoRA is arguably more directly related.

### Trivial

- **SVD notation is non-standard and could confuse readers**: The paper writes $U \in \mathbb{R}^{m \times n}$ for the left singular matrix in Section 4.1, while standard SVD would give $U \in \mathbb{R}^{m \times m}$ (full) or $\tilde{U} \in \mathbb{R}^{m \times r}$ (thin). The convention appears to be consistent within the paper, but the dimensions should be stated more explicitly to avoid confusion.

## Nice-to-Haves

- A clear specification of the threshold used to determine "acceptable level of subspace similarity" (mentioned in the abstract) for deciding which layers to transfer.
- A brief discussion of *why* transferred LoRA-X is robust to rank reduction while trained LoRA-X degrades (Table 6) — this finding is interesting but unexplained.
- Reporting the number of layers where LoRA-X is applied, and whether all attention layers or a selected subset are used.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Garbled equations / formatting artifacts in Section 4.2.2** (e.g., `$(V_s^\top V_s)^{-1}$` with odd subscript-minus): These are parser artifacts from PDF extraction and not author errors. The mathematical content is clear.
- **Missing training hyperparameters (learning rate, batch size, optimizer, steps)**: Per the review guidelines, this is categorized as a reproducibility nitpick about undisclosed hyperparameters, to be removed.
- **Code/checkpoint release not mentioned**: Per guidelines, questions about a cited entity's existence/release status are not valid criticisms.
- **Notation issues beyond the SVD convention**: Minor formatting concerns from the harsh critic (e.g., about Equation 2's consistency with full vs. truncated SVD) are addressed by a careful reading of the paper, where the usage is internally consistent.

## Novel Insights

The reviewers highlight an interesting tension that goes beyond the paper's own discussion: the subspace constraint that enables transferability also creates an asymmetry where transferred adapters are *more* robust to rank reduction than trained ones (Table 6). This is not explained in the paper and suggests that the subspace alignment step (Eq. 3) may implicitly regularize the adapter, compressing it into the most "agreeable" directions between source and target subspaces. This could be a useful design principle for future transferable adapters: the projection step may act as an information bottleneck that filters out source-specific noise.

## Suggestions

1. **Add standard deviations or confidence intervals to all tables** using the 30 seeds already collected. This is the single most impactful change: it turns "numbers are close" into "differences are statistically indistinguishable" (or reveals variance that tempers the claims).

2. **Clearly bound the scope of claims** to same-architecture transfer, and either (a) remove Section 4.2.2, (b) add even a single cross-dimension experiment, or (c) explicitly label the section as a preliminary sketch for future work.

3. **Validate the ATC metric** by showing a correlation (even qualitative) between ATC values and actual transfer quality (e.g., plot HPSv2 of transferred adapters against ATC for several source-target pairs).

4. **Clarify the DINOv2 metric**: state explicitly what two quantities are being compared (e.g., average cosine similarity between DINOv2 embeddings of images generated by the trained vs. transferred adapter across the same prompts).
