Here is my final consolidated review.

---

## Summary

This paper proposes MTSAM, a framework that adapts the Segment Anything Model (SAM) for multi-task learning. It makes two contributions: (1) architectural modifications to SAM (removing the prompt encoder, adding task-specific no-mask embeddings and mask decoders) to enable outputs with varying channel dimensions per task, and (2) Tensorized low-Rank Adaptation (ToRA), a parameter-efficient fine-tuning method that stacks per-task update matrices into a 3-mode tensor and applies Tucker decomposition to capture both task-shared and task-specific information. Experiments on NYUv2, CityScapes, and PASCAL-Context show consistent improvements over LoRA-based and other multi-task baselines in terms of average relative improvement (\(\Delta_b\)), while using fewer trainable parameters.

## Strengths

- **Effective architectural adaptation of SAM to multi-task learning.** The paper identifies a genuine mismatch between SAM's prompt-based, fixed-channel-output design and the requirements of multi-task dense prediction (varying output channels per task). The proposed solution—removing the prompt encoder and introducing trainable task embeddings with per-task mask decoders (Section 3.2, Figures 2–3)—is clean and well-motivated.

- **Consistent empirical improvement across three benchmarks.** On NYUv2 (3 tasks), CityScapes (2 tasks), and PASCAL-Context (4 tasks), MTSAM + ToRA achieves the highest \(\Delta_b\) among all baselines (Tables 1–3). The improvement is consistent across datasets with different task compositions, and the method outperforms not only LoRA variants but also CNN-based (Cross-Stitch, MTAN, NDDR-CNN) and Transformer-based (VTAGML, SwinMTL) multi-task methods.

- **Parameter efficiency with a clear theoretical rationale.** ToRA's parameter complexity is \(O(dp + kq)\), which—crucially—does not scale with the number of tasks \(T\) in its dominant terms, while independent LoRAs scale as \(O(T r d + T r k)\). Theorem 1 formalizes this: under a joint low-rank condition (bounded ranks of the mode-1 and mode-2 unfoldings of the stacked update tensor), ToRA can represent the same set of update matrices as \(T\) independent LoRAs with fewer parameters. This is a genuine parameter-efficiency guarantee.

- **Thorough ablation studies.** The paper systematically ablates rank choices (Table 4), orthogonal regularization components (Table 5), and the regularization hyperparameter \(\lambda\) (Table 6), demonstrating that ToRA consistently outperforms LoRA-STL and LoRA-HPS across rank settings and that the orthogonal regularization on the core tensor provides additional gains.

## Weaknesses

### Fatal

None.

### Major

None.

### Minor

- **Theoretical claims are overframed relative to what Theorem 1 actually establishes.** The abstract, introduction, and Section 3.5 state that ToRA's "expressive power surpasses that of LoRA" and claim "superior expressive power." In reality, Theorem 1 establishes a *parameter-count inequality* under the assumption that the stacked update matrices are jointly low-rank in their mode-1 and mode-2 unfoldings. This is a parameter-efficiency result, not a representation-capacity result: it shows ToRA can represent the same set of matrices with fewer parameters, not that it can represent functions LoRA cannot. The theorem is mathematically sound but its interpretation is overstated. The paper's own framing in Section 3.5 ("for any multi-task learning problem solvable by multiple LoRAs, ToRA can also solve the problem by using fewer parameters") is more accurate than the abstract's "expressive power surpasses." The authors should reframe consistently to avoid misleading readers.

- **No uncertainty quantification.** All experimental results (Tables 1–6) report point estimates from a single run without standard deviations, confidence intervals, or significance tests. Several improvements over LoRA-STL are small in absolute terms (e.g., mIoU 52.1 vs. 51.8 on NYUv2; Abs Err 0.282 vs. 0.283). Without error bars, the reader cannot assess whether these gains are reliable or within the noise floor. This is the most significant empirical weakness in an otherwise well-designed experimental section.

- **The contribution of ToRA vs. the architectural modifications is not fully disentangled.** The paper compares MTSAM+ToRA against MTSAM+LoRA-STL and MTSAM+LoRA-HPS, which isolates the effect of ToRA *within the modified architecture*. However, there is no comparison against a baseline that keeps SAM's original architecture (prompt encoder) with per-task heads, or against fully fine-tuned SAM with the same architectural modifications. This makes it difficult to assess how much of the overall gain is attributable to the architectural changes vs. the ToRA parameterization.

### Trivial

None.

## Nice-to-Haves

- Include a full fine-tuning baseline (all encoder parameters unfrozen) on the same architecture as an upper-bound reference for the PEFT methods.
- Report wall-clock training time or FLOPs for ToRA vs. LoRA variants to quantify the training-time computational overhead of tensor reconstruction.
- Add an analysis of the learned factor matrices (e.g., visualizing \(U_3\) to see whether related tasks cluster, or measuring how well the joint low-rank assumption holds empirically).
- Study training dynamics: does ToRA's advantage over LoRA-STL appear early or only after extensive training (200 epochs on NYUv2)?
- Compare against a controlled subset of tasks on NYUv2 to test whether ToRA's advantage grows with the number of tasks.

## Removed Points

Points from the reviews that were filtered out per meta-reviewer guidelines. These should be treated with caution:

- **"Sublinear is imprecise"** (Harsh Critic): The paper's parameter complexity is \(O(dp + kq)\), whose dominant terms are independent of \(T\). The \(Tv\) term is lower-order. "Sublinear" is technically correct in the big-O sense. **Removed** — the reviewer's objection is inaccurate.
- **"Task embedding copying is unclear"** (Harsh Critic): The paper states \(E_t \in \mathbb{R}^{N_t \times D}\) is expanded to \(E'_t \in \mathbb{R}^{N_t \times D \times H/16 \times W/16}\) by spatial copying. The dimensions are explicitly given. **Removed** — the paper is clear.
- **"Inadequate baselines — missing Polyhistor/HiPro comparison"** (Harsh Critic): Polyhistor targets hierarchical vision transformers and HiPro targets vision-language models. Neither is directly applicable to SAM's architecture. The paper already compares against 9 baselines spanning CNN-based, Transformer-based, and LoRA-based methods. **Removed** — demanding these specific baselines is scope creep and disagreement on taste, not a genuine gap.
- **"Unclear novelty relative to existing tensor-based multi-task methods"** (Harsh Critic): The application of Tucker decomposition to multi-task SAM fine-tuning, combined with the specific ToRA formulation (orthogonal regularization, per-task slicing, initialization scheme) and the architectural adaptation of SAM, constitutes a legitimate contribution for a methods+application paper. **Removed** — the paper is being evaluated against the wrong class of expectations.
- **"Missing related works"** (implicit in the critic's framing): Per meta-reviewer policy, missing related works cannot be raised without external sources to confirm their existence. **Removed** on policy grounds.
- **"Missing appendix/proofs"**: The parser strips these sections from all papers; they exist in the original submission. **Removed** on policy grounds.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a useful tension: Theorem 1 cleanly establishes a parameter-count advantage under a joint low-rank condition, but the paper's claim that this implies "superior expressive power" conflates parameter efficiency with representation capacity. The genuinely novel empirical finding is that Tucker-decomposed update tensors with orthogonal regularization consistently outperform independent LoRAs across three multi-task dense prediction benchmarks when applied to SAM — a non-trivial demonstration given SAM's architectural idiosyncrasies. The lack of error bars, however, means the margin of this advantage remains unclear.

## Suggestions

1. Reframe the theoretical claims throughout the paper to match what Theorem 1 actually shows: ToRA achieves the same representation as \(T\) independent LoRAs with provably fewer parameters under a joint low-rank condition. Remove the "expressive power surpasses" language.
2. Run experiments with at least 3 random seeds and report means with standard deviations (or at minimum, report standard deviations for the main tables). This is essential to establish whether the observed improvements over LoRA-STL are statistically meaningful.
3. Add an ablation that controls for the architectural modifications alone — e.g., compare MTSAM+LoRA-STL against SAM with its original prompt encoder + per-task prediction heads — to isolate ToRA's contribution.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>