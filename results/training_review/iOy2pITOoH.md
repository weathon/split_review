Now I have enough information to write the consolidated review. Let me carefully cross-check each claim and produce the final review.

## Summary

This paper introduces Spark Transformer, an architectural variant that achieves high activation sparsity in both FFN and attention via a novel **statistical top-k** algorithm. The key ideas are: (1) replacing expensive sorting-based top-k with an O(d) Gaussian-threshold approximation, (2) using a split of the query/key dimensions as a low-cost predictor of which entries to activate, and (3) treating both FFN and attention as key-value lookups under a unified sparsification framework. The authors train Spark Gemma-2 (2B parameters) using the standard Gemma-2 recipe and show it matches the original model's quality on MMLU, HellaSwag, etc., while using only 8% FFN nonzeros and ≤256 attended tokens, corresponding to a 3.1× FLOPs reduction and up to 1.79× wall-clock speedup on CPUs.

## Strengths

- **Novel and theoretically grounded statistical top-k.** The paper introduces an approximate top-k operator that requires only 2d FLOPs (mean + std dev) and provably concentrates around the target sparsity level under a Gaussian assumption (Theorem 1). This is a creative adaptation of ideas from gradient compression to the activation-sparsity setting, and Figure 4 confirms it adds far less training slowdown than JAX's optimized `approx_max_k` even at low recall targets.
- **Unified treatment of FFN and attention sparsity within a single-stage training procedure.** By interpreting both components as key-value lookups, the paper designs Spark FFN and Spark Attention symmetrically, using a fixed projection of the query dimensions as a predictor. This requires no additional parameters, no post-hoc fine-tuning, and no separate training stages — a clean practical advantage over methods that add extra predictor modules or require multi-stage training.
- **Quality is preserved at high sparsity on a modern production-scale model.** Spark Gemma-2 (2B parameters, trained on 2T tokens) matches Gemma-2 quality on the standard suite of benchmarks while operating at 8% FFN nonzeros and ≤256 attended tokens. This is demonstrated via a **controlled comparison** (Spark Gemma-2 vs. the original Gemma-2, same recipe and data), which is the primary evidence for the paper's central quality claim.
- **Real CPU speedups are demonstrated, not just FLOPs counting.** The paper implements custom sparse kernels in gemma.cpp and reports wall-clock speedups of 1.35–1.79× on CPU across varying prompt lengths and core counts. Table 3 additionally reports prefill speedups (1.45–1.70×). These measurements go beyond FLOPs accounting and show genuine practical benefit on accessible hardware.
- **Theoretical analysis of differentiability.** Theorem 2 establishes that a Huber-smoothed variant of statistical top-k is continuously differentiable, providing a principled foundation for gradient-based training.

## Weaknesses

### Fatal
None.

### Major
- **The gap between the headline 3.1× FLOPs reduction and the measured 1.35–1.79× CPU speedup is not analyzed or explained.** The paper computes FLOPs assuming zero overhead from index gathering, masking, tiling, and synchronization, but provides no breakdown of where the remaining overhead comes from. Without this analysis, it is unclear how much of the theoretical FLOPs reduction is practically recoverable. Furthermore, no analytical model or microbenchmarks are provided to estimate potential speedups on GPUs/TPUs, where sparse computation faces different bottlenecks. While the paper acknowledges the "hardware lottery" in the discussion and explicitly scopes its evaluation to CPUs, the absence of any GPU analysis or overhead breakdown weakens the practical-efficiency narrative relative to the strong FLOPs-reduction claims.

### Minor
- **No controlled comparison against an alternative sparsification method on Gemma-2.** The paper compares Spark Gemma-2 against ProSparse and LLaMA ReGLU in Table 2, but these are different base models with different training setups, making it impossible to attribute quality differences to the sparsification method. While the primary claim (Spark Gemma-2 ≈ Gemma-2) is well-controlled, the paper would be stronger with a direct baseline — e.g., applying top-k thresholding or ReLU-switchback to Gemma-2 and comparing quality at similar sparsity levels. The paper notes that training with JAX's approx_max_k is prohibitively slow, but this limitation does not justify the absence of any same-model comparison.
- **Overall training wall-time of Spark Gemma-2 vs. standard Gemma-2 is not reported.** Figure 4 compares only the slowdown of the statistical top-k operator itself against JAX's approx_max_k. A reader cannot determine the total training overhead of the full Spark Transformer architecture, which is relevant for practitioners considering adoption.
- **Ablation study has several gaps:** (a) it covers only 25k steps (~5% of full training), so the final-model behavior at different r/k settings is unknown; (b) no ablation on the choice of r in Spark Attention (only a single fixed r=128 is used); (c) no ablation comparing the fixed projection matrix P against a learned low-rank predictor; (d) no ablation on whether the softplus nonlinearity in Spark Attention is necessary.
- **Predictor quality (recall/precision) is not evaluated.** The paper does not report what fraction of the true top-k entries are captured by the predictor. Without this, it is unclear whether the predictor is effective or whether the statistical top-k on the predictor scores is simply selecting entries that happen to be predictive.
- **Gaussian assumption is only partially validated.** Theorem 1 assumes i.i.d. Gaussian entries, but after training, activations are neither i.i.d. nor necessarily Gaussian. The paper acknowledges this and defers empirical validation to Appendix D.1 (not visible in the main text). Including even a brief quantile-quantile plot or distributional analysis in the main paper would strengthen confidence that the approximation holds throughout training.

### Trivial
- The description of the softplus nonlinearity in Spark Attention ("empirically observed to offer quality benefits") is heuristically motivated. This is not a flaw per se, but the paper could briefly note whether the benefit is substantial or marginal.

## Nice-to-Haves
- An analytical model of potential GPU/TPU speedup from the measured sparsity (e.g., using roofline analysis or sparse-kernel microbenchmarks) would significantly broaden the paper's impact.
- An ablation comparing the fixed projection P against a learned linear projection for the predictor would address a natural architectural question.
- Per-layer sparsity distributions (rather than averages) would reveal whether some layers become much denser than others.

## Removed Points
These points are flagged to be removed, treat them with caution:
- **"Evaluation hardware mismatch undermines the paper's efficiency claims (Structural)"** — The paper explicitly evaluates on CPUs (gemma.cpp) and discusses the hardware lottery. The FLOPs reduction is a valid theoretical metric, and the CPU speedups are real. The criticism that GPU/TPU evaluation is missing is scope creep; however, the *unanalyzed gap* between FLOPs and speedup is retained as a major weakness (see above).
- **"Drop-in replacement claim is overstated"** — The paper changes the FFN and attention architecture but keeps the same parameter count, training recipe, and input/output interface. This is a standard use of "drop-in replacement" in the ML literature.
- **"Softplus suggests over-engineering"** — This is a stylistic judgment, not a substantive weakness.
- **"Table 2 not visible"** — Parser artifact; the table exists in the original submission.
- **"Missing Appendix D.1"** — The parser strips appendix content; the appendix exists in the original paper.
- **"ProSparse/LLaMA ReGLU comparison is uncontrolled"** — The paper's primary comparison (Spark Gemma-2 vs Gemma-2) IS controlled. These are supplementary reference points. The absence of a Gemma-2+top-k baseline is retained as a minor weakness above.

## Novel Insights

Beyond the paper's own contributions, the reviews surface one genuinely novel observation: the statistical top-k algorithm has a fundamentally different failure mode from sorting-based top-k. With sorting, errors are O(1) — you get exactly k entries but may pick the wrong ones. With statistical top-k, errors are distributional — you may get slightly more or fewer than k entries, but the selection is stochastically calibrated. This means the method's practical robustness depends on how well the Gaussian approximation holds across layers and training stages, which is a different kind of reliability question than what the prior sparsity literature has focused on. The paper's empirical validation (Figure 1) suggests the approximation holds well, but understanding when and why it breaks would be a useful direction for follow-up work.

## Suggestions
1. Add an overhead breakdown explaining why 3.1× FLOPs reduction yields only ~1.79× speedup — categorize time spent in: statistical top-k computation, index gathering, sparse/dense matrix multiplication, synchronization overhead.
2. Include a direct quality comparison on Gemma-2 with a simple baseline (e.g., post-hoc top-k thresholding or ReLU fine-tuning at similar sparsity) to isolate the benefit of the proposed approach.
3. Report overall training wall-time for Spark Gemma-2 vs. Gemma-2 to give practitioners a complete picture of the training cost.
4. Add a brief empirical validation of the Gaussian assumption in the main text (e.g., a quantile-quantile plot for a representative layer at early/mid/late training).
5. Include the predictor recall metric: what fraction of the true top-k entries (using full dense computation as ground truth) are captured by the predictor + statistical top-k pipeline?

## Score and Decision

This paper makes a genuine contribution: the statistical top-k algorithm is clever and well-motivated, the unified architecture is elegant, and the empirical validation on a 2B-parameter model trained at scale is substantial. The weaknesses are real but not fatal — they concern the depth of the efficiency analysis and the breadth of the ablation study, not the validity of the core claims. The paper is clearly written, the theory is sound, and the experimental results support the stated conclusions.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>