## Summary

The paper proposes LoLoRA, a method that updates LoRA's A matrix using local, forward-pass learning rules (HPCA or autoencoder loss) instead of backpropagation. This avoids storing A's input activations for the backward pass, yielding memory savings similar to LoRA-FA while allowing online adaptation. The paper also provides a theoretical analysis (Theorem 4.4) showing that the optimal static A spans the top-r eigenvectors of the input covariance matrix, which connects to and generalizes the EVA initialization.

## Strengths

- **Clean theoretical result characterizing optimal A under random regression (Theorem 4.4).** The theorem proves that when the target is unknown, the optimal frozen A must span the top-r eigenspace of the input covariance matrix, with any nonsingular transformation being equivalent. This provides formal justification for PCA-based initialization (EVA) and for local rules like HPCA that converge to this subspace.

- **Multi-domain evaluation across three model families and task types.** The paper tests on RoBERTa-large (GLUE), LLaMA-3.1-8B (math reasoning), LLaVA-7B (multimodal instruction tuning), and TinyLlama (ablations), demonstrating breadth.

- **Ablation comparing multiple local update rules (Table 6).** Five local rules are compared (HPCA variants, AE, SoftHebb), and only those that converge to the principal subspace perform well, confirming the theoretical connection.

- **Quantified memory savings reported per experiment.** The paper reports peak extra GPU memory for each method (e.g., Tables 3 and 4), allowing direct comparison.

## Weaknesses

### Major

- **Online update provides no measurable benefit over static EVA initialization.** The paper's key differentiator from LoRA-FA (EVA) is the online HPCA update, yet across all experiments LoLoRA HPCA and LoRA-FA (EVA) achieve nearly identical results: Table 3 shows both at 0.829 accuracy; Table 4 shows 2.93 vs 2.92 perplexity; Table 6 shows 2.535 vs 2.536 perplexity at r=8. The method's core mechanism—adapting to input distribution shifts during training—is never tested in a scenario where such shifts occur (e.g., multi-task or continual fine-tuning). Without evidence that the online update provides value over a good static initialization, the practical contribution over LoRA-FA (EVA) is unclear.

- **Memory savings are marginal and, on one experiment, reversed relative to the closest baseline.** On LLaVA (Table 4), LoLoRA HPCA uses **more** extra memory (24.1 GB) than LoRA-FA (uniform) (23.9 GB), contradicting the claimed memory benefit over LoRA-FA. The paper acknowledges this but does not reconcile it with the general "up to 20% less" claim. The 13% reduction vs standard LoRA on MathQA (26 vs 30 GB) is real but comes entirely from freezing A's activations—the same mechanism used by LoRA-FA. LoLoRA does not improve over LoRA-FA on memory.

- **The theoretical analysis does not motivate the online update.** Theorem 4.4 characterizes the optimal *initialization* of A under a stationary target assumption. HPCA converges to this same subspace during training, but the paper never shows (theoretically or empirically) that the online trajectory matters. The stationary-target assumption is acknowledged as a limitation but no experiment tests robustness to non-stationarity (the very setting where online adaptation would be expected to help). The practical advantage claimed in the abstract ("adapt to input distribution shifts") therefore remains unvalidated.

### Minor

- **Run time overhead is not discussed.** Table 4 shows LoLoRA HPCA taking 2h 52m vs 2h 45m for standard LoRA and 2h 46m for LoRA-FA (uniform). With EVA initialization, LoLoRA takes 3h 30m vs 3h 24m for LoRA-FA (EVA). The paper claims a "compromise" but does not analyze whether the marginal memory savings justify the slowdown, especially when the memory advantage over LoRA-FA is unclear on this task.

- **LoLoRA introduces additional hyperparameters and optimizer state** (local learning rate, HPCA smoothing factor) that LoRA-FA does not require. This complexity is acknowledged in the conclusion but not quantified (e.g., size of the local optimizer state relative to total adapter memory). When r is small this is negligible, but the overhead should be explicitly accounted for in the memory analysis.

### Trivial

- The paper claims "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" — the phrasing "consistently outperforms... in two out of three" is slightly contradictory (consistency usually implies more than 2/3). This is a presentational quibble.

## Nice-to-Haves

- A comparison to gradient checkpointing applied to LoRA would strengthen the memory analysis, since checkpointing is a standard orthogonal technique.
- A subspace drift analysis (angle between HPCA's learned A and the PCA subspace of recent inputs over training) would build intuition for whether the online updates track meaningful shifts or oscillate around the static EVA initialization.
- Testing on a non-stationary scenario (e.g., sequential fine-tuning on two tasks) would directly test the claimed ability to adapt to distribution shifts.

## Removed Points

These points from the harsh critic are removed or downgraded as follows:

- *"LoLoRA does not outperform LoRA-FA" (framed as the paper's central claim being falsified)* — The paper's stated central claim is maintaining LoRA-comparable performance with memory savings, not outperforming LoRA-FA. The claim "HPCA outperforms standard LoRA-FA in 2/3 setups" is accurate when "standard" means uniform initialization. Demoted from Fatal to a Major weakness with a more precise formulation (online update adds no value over LoRA-FA EVA).

- *"The paper cherry-picks favorable comparisons" on GLUE* — The summary says "LoLoRA achieves slightly better results than LoRA-FA (EVA)." Checking the data: LoLoRA HPCA (66.3) vs LoRA-FA EVA (64.7) on CoLA — LoLoRA is better. On other tasks they're close. The claim is accurate. Removed.

- *Criticism about the HPCA (uniform) ablation "undercutting the paper's narrative"* — The paper explicitly says online methods have the advantage of no separate PCA pass. The ablation shows HPCA (uniform) matches LoRA-FA (EVA), which is exactly what the theory predicts. This is consistent, not contradictory. Removed.

- *"Memory savings overstated" — critic claims 20% is not verifiable* — 20% is claimed for GLUE and referenced to Appendix D (stripped by parser). Per the hard rules, missing appendix content should not be penalized. The claim exists in the original submission. Removed with this justification.

- *"The method introduces complexity (learning rate for local updates, HPCA hyperparameters)" — already acknowledged by the paper* — Retained as a Minor weakness but rephrased to add concreteness (quantify the optimizer state overhead).

- *Requests for experiments outside scope* (comparing to gradient checkpointing, testing on broader architectures, additional visualizations) — moved to Nice-to-Haves.

## Novel Insights

The reviews surface an inherent tension in the paper: the theoretical contribution (Theorem 4.4) is genuinely clean and supports EVA-style PCA initialization, but the method's raison d'être is the *online* HPCA update that avoids a separate PCA pre-pass. The data consistently shows that once you have a good initialization (EVA), the online updates add essentially nothing. This suggests the paper's theoretical framework actually points in a simpler direction than its algorithmic contribution: the optimal A is known a priori (the PCA subspace), so one should either (a) pre-compute it (EVA) and freeze, or (b) use the first forward pass to estimate it and then freeze. The HPCA updates that continue throughout training are solving a problem that the theory says is already solved at initialization, and the experiments confirm this.

## Suggestions

1. Add an experiment where the input distribution drifts during fine-tuning (e.g., sequential multi-task adaptation) and show that LoLoRA tracks the changing subspace while LoRA-FA (EVA) does not. This would directly validate the claimed "adapt to input distribution shifts" advantage.
2. Report the peak total GPU memory (model + activations + optimizer) for all methods in all experiments, not just "extra memory," and include a breakdown of where the memory goes (A activations, B activations, local optimizer state, etc.).
3. Discuss the local optimizer state overhead quantitatively: how many extra bytes per layer does Opt_loc introduce compared to LoRA-FA, and how does this scale with rank and model depth?

## Score and Decision

**Calibration anchors:**

| Path | Avg Human Score | Comparison |
|------|:-:|------|
| HiRA (`TwJrTz9cRS`) | 8.00 | Strong PEFT paper with clear empirical improvement over LoRA; LoLoRA's empirical case is much weaker. |
| Forward Learning GNN (`Abr7dU98ME`) | 6.50 | Strong paper on forward-only learning methods; LoLoRA's forward-only innovation is narrower in scope. |
| ReLoRA (`DLJznSp6X3`) | 5.75 | Accepted paper with similar incremental-novelty concerns; LoLoRA has stronger theory but weaker empirical advantage. |
| LoRA-FA (`RbKThNNFxr`) | 5.33 | Closely related baseline; LoLoRA adds theory and local updates but the experimental case over LoRA-FA is marginal. |
| EVA (`DM6Q45HWSk`) | 4.75 | Similar theme of data-driven initialization; LoLoRA has better theoretical grounding but similar empirical issues. |
| ME-LoRA (`0qexTTfnmH`) | 3.75 | Weak incremental Bayesian LoRA variant; LoLoRA has more substance. |
| UnoLoRA (`49ti6LOUw5`) | 3.00 | Multiple serious flaws; LoLoRA is substantially stronger. |

The paper's theoretical contribution (Theorem 4.4) and breadth of evaluation are genuine assets. However, the central empirical weakness—that the online HPCA update provides no measurable benefit over static EVA initialization, yet represents the method's distinguishing feature from the simpler LoRA-FA (EVA)—is a significant limitation. The memory advantage over LoRA-FA is also not consistently demonstrated. The paper sits below the stronger PEFT papers (HiRA, ReLoRA) but above clearly weak submissions (ME-LoRA, UnoLoRA). Relative to the closely related LoRA-FA (5.33) and EVA (4.75) papers, LoLoRA offers stronger theory but weaker empirical support for its specific claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>