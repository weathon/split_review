Now I have a thorough understanding of the paper and the calibration landscape. Let me compile the final review.

## Summary
The paper proposes LoLoRA, a hybrid fine-tuning method that replaces gradient-based updates of the LoRA down-projection matrix A with local unsupervised updates (Hebbian PCA / autoencoder loss) performed during the forward pass. This avoids storing input activations for A, reducing memory, while adapting A to the input distribution rather than freezing it as in LoRA-FA. The paper also proves that optimal A (when frozen) spans the top principal eigenspace of the input covariance (Theorem 4.4) and that any full-rank B initialization is equally good (Theorem 4.5), providing theoretical grounding for data-driven initialization.

## Strengths

1. **Theoretical characterization of optimal A initialization (Theorem 4.4).** The paper proves that, under a random regression assumption, the optimal frozen-A matrix is any nonsingular linear transformation of the top-r eigenvectors of the input covariance. This provides principled justification for PCA-based initialization (EVA) and for local update rules that converge to this subspace. Theorem 4.5 (asymmetry of A and B) formalizes and extends prior empirical observations.

2. **Systematic ablation of local update rules and initializations (Tables 5 and 6).** On TinyLlama-1.1B, the paper compares five local update rules (HPCA, HPCA no mean, HPCA svd-first, AE, SoftHebb) and four initializations (uniform, orthogonal, PiSSA, EVA) across ranks r=2,4,8. This provides practical guidance for practitioners choosing among local learning approaches.

3. **Demonstrated memory savings across multiple settings.** The paper reports concrete memory reductions: ~13% on LLaMA-3.1-8B (30 GB → 26 GB, Table 3), ~0.5 GB on LLaVA-v1.5-7B (24.6 GB → 24.1 GB, Table 4), and "up to 20%" on GLUE (Appendix D). These savings are measured as peak extra GPU memory, excluding model weights.

## Weaknesses

### Major

1. **Evaluation protocol for the math-reasoning experiment (Section 5.2, Table 3) undermines reliability of the only clear performance advantage.** The paper states: *"The model was tested on GSM8K every 0.2 epoch during fine-tuning, and the best result is reported for each method."* This uses the test set for checkpoint selection (early stopping), which inflates the reported numbers and introduces bias if different methods peak at different checkpoints. While all methods use the same protocol (preserving relative ordering), the absolute values are unreliable as unbiased performance estimates, and the ranking cannot be taken at face value. This is the only experiment (out of three setups) where LoLoRA shows a clear advantage over all baselines—on GLUE it is slightly worse than LoRA-FA (uniform), and on LLaVA it sits between LoRA-FA uniform and LoRA-FA (EVA).

2. **Inconsistent empirical advantage over LoRA-FA.** On GLUE (Tables 1–2), LoLoRA HPCA is comparable to or numerically slightly worse than LoRA-FA (uniform) across all 8 tasks (e.g., CoLA 66.3 vs 67.9, RTE 84.6 vs 86.4). On LLaVA (Table 4), LoLoRA (loss 1.075) sits between LoRA-FA uniform (1.087) and LoRA-FA (EVA) (1.070). The paper's conclusion claims *"HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups,"* but on the GLUE setup—one of the three—it does not outperform. The claim rests primarily on the math experiment, which has the evaluation protocol concern.

### Minor

1. **Rank r not stated in main text for GLUE, LLaMA, and LLaVA experiments.** The paper defers all hyperparameters (including rank) to Appendix C. While appendix details exist in the original submission, the main text should state the rank used for each setup, as it directly affects adapter capacity and memory usage. This is a reproducibility concern that should be fixed.

2. **Conclusion claim slightly overstated.** The paper states *"HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups."* On the GLUE setup, LoLoRA is numerically slightly worse than LoRA-FA (uniform) on most tasks. The claim should be softened to reflect that on GLUE the methods are comparable with a slight edge to LoRA-FA.

### Trivial

None.

## Nice-to-Haves

- Clarify the memory breakdown: what fraction of activation memory does eliminating storage of z save? Is the extra memory for the local optimizer state (running mean, etc.) accounted for in the reported numbers?
- Compare LoLoRA starting from random A vs LoRA-FA starting from random A without EVA, to isolate the benefit of online adaptation over a good initialization.
- Test a scenario with input distribution shift during training (e.g., curriculum learning or domain adaptation) where online adaptation of A would be more valuable than a fixed PCA initialization.

## Removed Points

These points were flagged by the harsh critic but are not retained as weaknesses in the final review:

- *"The memory savings are essentially those of LoRA-FA, not a new benefit."* — This is an observation about the mechanism, not a weakness. LoLoRA's contribution is recovering performance loss while maintaining LoRA-FA's memory savings; both achieve savings by not storing A's input activations. The paper does not claim a new memory-saving mechanism, it claims performance recovery. REMOVED: not a valid weakness.

- *"The paper frames LoRA-FA as degrading performance... on several GLUE tasks LoRA-FA (uniform) is already competitive with or better than standard LoRA."* — While factually true for some tasks (RTE, SST-2), this is noted in the paper's own summary ("Freezing A (LoRA-FA) can sometimes improve stability (RTE, SST-2)"). The paper frames LoRA-FA as having *limitations* not universal degradation. REMOVED: the paper already acknowledges this.

- *"The local update rule hyperparameters (Hebbian PCA, optimizer for A) are not described."* — The paper specifies HPCA with SNL, smoothing factor 0.98 for centering, and references Appendix B for convergence analysis. The main text gives sufficient algorithmic detail; detailed hyperparameters in the appendix is standard practice. REMOVED: adequately addressed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the evaluation protocol concern and the inconsistency of empirical results, but these are critical assessments of known issues rather than novel observations about the method.

## Suggestions

1. **Fix the math-reasoning evaluation.** Use a validation split from the training data for checkpoint selection, or report the final checkpoint performance. If the advantage over LoRA-FA persists under proper evaluation, the paper is substantially strengthened.
2. **State the rank r for every experiment in the main text** (e.g., in a single line below each table or in the experiment setup paragraph).
3. **Soften the conclusion claim** to accurately reflect that on GLUE, LoLoRA achieves comparable but slightly lower performance than LoRA-FA (uniform), while on LLaVA and math it shows modest improvements.

## Score and Decision

### Calibration Anchors

| Anchor | Avg Score | Round/Query | Comparison |
|--------|-----------|-------------|------------|
| LoRA-FA (RbKThNNFxr) | 5.33 | R1-topic-mid | Simpler method, cleaner experiments. Current paper has more novelty (theory + local updates) but an evaluation protocol issue. Roughly comparable but slightly lower. |
| EVA (DM6Q45HWSk) | 4.75 | R1-weakness | Directly related (PCA-based initialization for LoRA). EVA had broader experiments but no theory. Current paper has stronger theory but messier experiments (evaluation concern). Comparable, slightly lower. |
| ReLoRA (DLJznSp6X3) | 5.75 | R1-topic-mid | Accepted. Higher-quality experiments, clearer memory/speedup claims. Current paper has weaker empirical support. Lower. |
| ALLoRA (7X65yoKl3Y) | 3.33 | R1-topic-low | Marginal improvements, weak theory. Current paper is clearly stronger. Higher. |
| DeLoRA (X1U74IwuxG) | 5.25 | R2 | Accepted. Similar-level contribution but cleaner experiments. Current paper is lower. |
| SiVA (VpeAsLmcvg) | 3.75 | R2 | Shaky theoretical assumptions, weak experiments. Current paper is stronger. Higher. |
| GLoRA (NXnNiT0fdp) | 4.75 | R2 | Another rank-adaptive LoRA variant. Similar overall quality. Comparable. |

**Round 1 bracket:** 4.0–5.5  
**Round 2 narrowing:** The paper is comparable to EVA (4.75, rejected) but with a methodological concern that EVA did not have. It sits above clearly weaker papers (ALLoRA 3.33, SiVA 3.75) but below cleaner empirical papers (LoRA-FA 5.33, ReLoRA 5.75, DeLoRA 5.25).  

The low-band anchors (ALLoRA, SiVA) fail on theoretical/empirical rigor and weak contributions. The current paper shares some empirical weakness (inconsistent advantage, evaluation protocol concern) but has stronger theory, placing it above those anchors. The mid-band anchors (LoRA-FA, EVA) represent papers with cleaner experiments but less novelty; the current paper trades cleaner experiments for stronger theory. The evaluation protocol concern is a real flaw that the stronger mid-band papers do not share.

### Final Score

The paper has genuine theoretical contributions and a clearly described method, but the experimental validation has a significant methodological flaw (test-set-based checkpoint selection in the only experiment showing a clear advantage), and the empirical advantage over LoRA-FA is inconsistent across settings. The paper would benefit substantially from fixing the evaluation protocol.

**Score: 4.5**  
**Decision: Reject**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>