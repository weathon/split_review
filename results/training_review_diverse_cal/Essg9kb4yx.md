Now I have a thorough understanding of the paper and all reviewer claims. Let me produce the consolidated review.

## Summary

This paper tackles the realistic and underexplored problem of **continual unlearning in LLMs without access to retained data**. It proposes the O³ framework with two main innovations: (1) an orthogonal-regularized LoRA module that disentangles parameter updates across sequential unlearning requests, and (2) an unsupervised OOD detector (trained with a contrastive entropy loss + MLM loss) that adaptively controls how much of the unlearning LoRA to apply during inference. Experiments across three tasks (QA, fictitious knowledge generation, intent classification) and seven datasets show O³ consistently achieves the best Unlearning-Utility Ratio (U²R) compared to seven baselines that all require retained data, while reducing trainable parameters by over 99%.

## Strengths

- **First framework for continual LLM unlearning without retained data**: The paper addresses a genuine practical gap — unlearning requests arriving sequentially with no access to original training data. The O³ framework is evaluated against seven baselines (all of which use retained data) and achieves the highest U²R across all three task settings (Figure 2, Tables 2–3), often by a wide margin.

- **Orthogonal LoRA regularization demonstrably prevents interference**: The orthogonal loss (Eq. 6) forces the parameter space of each new unlearning LoRA to be orthogonal to the previous one. The ablation (Table 5, λ=0 vs. λ>0) shows this design is critical: without it both unlearning effectiveness and utility preservation degrade substantially.

- **Resource efficiency is substantial and well-validated**: O³ uses roughly half the training data of baselines (no retained data needed), trains only 20M parameters (0.3% of full-model baselines' 6,758M), and incurs only 5.1% extra inference overhead (Table 1 and line 181). The inference overhead is contextualized as relative to the base model.

- **Comprehensive ablation study**: Tables 4–6 systematically ablate each design choice (CEL vs. SimCLR/MoCo, scoring distances, layer count, orthogonal loss factor, soft-vs-hard weighting) across multiple datasets, providing clear evidence for each component's contribution.

- **Strong and consistent empirical results**: O³ achieves the best unlearning effectiveness while maintaining near-base-model accuracy on utility datasets (e.g., CommonsenseQA, OpenbookQA in Figure 4). The gains are consistent across discriminative (intent classification), generative (fictitious knowledge), and reasoning (QA) tasks.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the experiments. No identified weakness invalidates the main contributions.

### Minor

- **The contrastive entropy loss (Eq. 7) lacks explicit positive-pair supervision, and the paper's theoretical justification is incomplete.** The loss minimizes the entropy of a softmax distribution over all batch items j for each query i (masked xᵢ* vs. original xⱼ). The paper's claim that this "aligns positive pairs" (line 92) is not directly enforced by the loss — nothing explicitly marks j=i as the positive pair. While in practice the MLM loss (ℒ_MLM) provides token-level grounding that prevents collapse, and the natural data structure (masked xᵢ* will be most similar to its own original xᵢ) provides implicit alignment, the paper would benefit from either (a) a formal argument or empirical analysis (e.g., alignment/uniformity metrics, representation visualization) showing the learned representations avoid degenerate solutions, or (b) an explicit InfoNCE-style positive-pair formulation to ground the loss. This does not invalidate the empirical results (Table 4 shows CEL outperforms standard contrastive methods), but it is a gap in the method's theoretical presentation.

- **The orthogonal loss is only enforced against the immediate predecessor A^{t-1} (Eq. 6), not all previous A matrices.** Over a long sequence of requests (T>2), indirect interference could arise through a chain (A³ non-orthogonal to A¹ even if both are individually orthogonal to A²). The paper's strong results across 3–4 sequential requests suggest this is not a pressing problem for the settings tested, but the practical impact on longer unlearning sequences is unclear, and the design choice merits discussion.

- **The inference-time OOD detector requires T separate detector backbones (one per request), each processing every input.** The paper reports "5.1%" additional overhead, but with many requests this could grow linearly. Clarifying whether this overhead is additive per request would better contextualize scalability.

- **The problem definition (Section 2) frames continual unlearning via mutual information (Eqs. 1–2), but the implemented losses (cross-entropy + orthogonal loss) do not directly optimize this objective.** While this kind of high-level framing followed by practical losses is common in the literature, the disconnect makes the theoretical setup feel vestigial.

### Trivial
- Several figures (Tables 2–3, images) are referenced but not directly readable in the text extraction (parser artifacts). This is a formatting issue, not an author error, but the authors should ensure inline results are also reported in text for accessibility.

## Nice-to-Haves
- **Separate-LoRA baseline**: Comparing against storing one independent LoRA per request (without orthogonal regularization) would further isolate the benefit of the orthogonal design. This is a reasonable suggestion but does not weaken the existing contribution, which already demonstrates strong gains over full-model baselines.

- **Continual learning baselines (EWC, SI, replay)**: Adapting continual learning methods designed to prevent catastrophic forgetting to the unlearning setting would provide additional context, though the paper already compares against seven relevant baselines.

- **Privacy discussion**: The OOD detector stores score vectors of unlearning data for OCSVM fitting. A brief discussion of how this relates to the privacy motivations for not using retained data would strengthen the framing.

## Removed Points

- **The critic's claim that "B's row spaces can still cause modulations to interact even if A's column spaces are orthogonal"** is technically incorrect. If A^t and A^{t-1} have orthogonal column spaces, then for any hidden states h, the outputs A^t(B^t·h) and A^{t-1}(B^{t-1}·h) lie in orthogonal subspaces of ℝ^U — the LoRA output spaces are provably orthogonal regardless of B. The paper's justification ("B can be regarded as the linear weights of matrix A") is hand-wavy but the underlying math is sound.

- **The claim that CEL "can converge to a trivial solution where all queries become similar to the same key"** ignores the MLM loss (ℒ_MLM, Eq. 8) that is jointly optimized and provides strong token-level representation grounding, making representational collapse highly unlikely. The paper's ablation (Table 4, CEL > SimCLR > MoCo) provides empirical evidence that the full design works.

- **The suggestion that CEL should be replaced with InfoNCE**: The paper already ablates against SimCLR and MoCo (which use InfoNCE-style objectives) and shows CEL outperforms both (Table 4). The suggestion contradicts the paper's own evidence.

- **Criticisms about "no retained data" claim being misleading**: The paper is explicit that baselines use retained data while O³ does not (e.g., Section 4.2, line 176: "provide sufficient retained data for all comparison baselines while assuming our O³ framework only uses the data of each unlearning request"). This is acknowledged, not hidden.

- **Formatting/style nitpicks and demands for appendix content**: Removed per instructions (parser artifacts, missing appendix content that exists in original submission).

## Novel Insights

The most interesting observation from the review process is that the CEL loss, despite lacking explicit positive-pair supervision in its mathematical formulation, empirically outperforms properly grounded contrastive objectives (SimCLR, MoCo). This suggests that in the specific setting of OOD detection for unlearning — where the "ID" data consists of diverse unlearning requests from different distributions — the flexibility of an unaligned entropy-minimization loss may be advantageous precisely because it does not hard-wire the assumption that the only positive pair is the (masked, original) of the same instance. The downstream scoring pipeline (Mahalanobis + cosine + OCSVM) likely compensates for any representation-level ambiguity. This interplay between a theoretically under-specified representation loss and a robust scoring mechanism is worth further study.

## Suggestions

- Provide an empirical analysis (e.g., alignment/uniformity metrics, t-SNE/UMAP visualization, or spectral analysis) demonstrating that the CEL-learned representations do not collapse, to address the theoretical concern about the loss.
- Extend the orthogonal regularization to explicitly enforce pairwise orthogonality against all previous A matrices (not just A^{t-1}), or discuss why the one-step constraint suffices for the setting.
- Clarify whether the 5.1% inference overhead is additive per request or fixed regardless of T, and discuss scalability to larger T.

## Score and Decision

**Score**: 7.0

**Decision**: Accept

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>