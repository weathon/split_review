I have thoroughly analyzed the paper and all calibration anchors. Here is my final consolidated review:

---

## Summary

LoLoRA proposes a hybrid fine-tuning method that applies local unsupervised updates (HPCA) to the LoRA A matrix during the forward pass while training matrix B via standard backpropagation, thereby eliminating the need to store input activations for A. The paper provides a theoretical result (Theorem 4.4) showing that optimal A should span the top eigenvectors of the input covariance matrix, consistent with the EVA initialization. Empirically, LoLoRA achieves memory savings comparable to LoRA-FA, but the claimed advantage of local updates over a good static initialization (LoRA-FA with EVA) is not supported by the evidence.

## Strengths

1. **Theoretical characterization of optimal A (Theorem 4.4):** The paper formally proves that, under a random regression model, the optimal frozen A is an arbitrary nonsingular transformation of the top r eigenvectors of the input covariance. This provides a stronger theoretical foundation than prior empirical work on data-driven initialization (EVA). The result is clean, well-structured, and connects directly to the method design.

2. **Systematic ablation of initialization and local update rules:** Tables 5 and 6 carefully compare four A initializations (Uniform, Orthogonal, PiSSA, EVA) and five local update rules (HPCA variants, AE, SoftHebb) on TinyLlama/Alpaca, offering practical guidance on which configurations work best.

3. **Multi-domain evaluation:** The method is tested on RoBERTa-large (NLU, GLUE), LLaMA-3.1-8B (math reasoning, GSM8K), and LLaVA-v1.5-7B (vision-language), showing the memory-efficiency benefits hold across diverse settings.

4. **Memory reduction demonstrated:** Table 3 shows LoLoRA achieves 26 GB peak extra memory vs. 30 GB for standard LoRA (a 13% saving) while maintaining comparable accuracy.

## Weaknesses

### Fatal
None.

### Major

1. **The core claim — that local updates provide a meaningful advantage over a good static initialization — is not supported by the evidence.** The key differentiator of LoLoRA from LoRA-FA is the online local update of A during training. The natural baseline to isolate this component is LoRA-FA with the theoretically optimal static initialization, which the paper itself identifies as PCA-based (EVA, matching Theorem 4.4). Across all experiments, LoLoRA HPCA is essentially tied with or slightly worse than LoRA-FA (EVA):

   - **GLUE (Tables 1–2):** LoLoRA HPCA vs. LoRA-FA (EVA): CoLA 66.3 vs. 64.7 (LoLoRA better by 1.6), RTE 84.6 vs. 83.6 (better by 1.0), MRPC 89.9 vs. 90.0 (tied), STS-B 92.0 vs. 91.9 (tied), MNLI 90.3 vs. 90.4 (LoRA-FA better), QNLI 94.7 vs. 94.5 (LoLoRA better by 0.2), QQP 90.6 vs. 90.6 (tied), SST-2 96.4 vs. 96.3 (tied). All differences are well within reported standard deviations.
   
   - **Math reasoning (Table 3):** LoLoRA HPCA and LoRA-FA (EVA) are *exactly tied* at 82.9% accuracy.
   
   - **LLaVA (Table 4):** LoLoRA HPCA (loss 1.075) is *worse* than LoRA-FA (EVA) (loss 1.070); LoLoRA HPCA (EVA) (loss 1.074) is also worse.
   
   - **Ablation (Tables 5–6):** LoRA-FA (EVA) at r=8 achieves perplexity 2.536; LoLoRA HPCA (uniform) achieves 2.535 — within error.
   
   The online HPCA matches the EVA initialization but does not surpass it, meaning the additional complexity of local updates (extra optimizer state, local rule hyperparameters, computational overhead) lacks empirical justification.

2. **Overstated conclusions.** The conclusion states: "our experiments showed that HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups." This phrasing is misleading. Against standard (uniform-initialized) LoRA-FA, LoLoRA HPCA is worse on most GLUE tasks (e.g., CoLA 66.3 vs. 67.9, RTE 84.6 vs. 86.4, MNLI 90.3 vs. 90.6, QQP 90.6 vs. 90.8, SST-2 96.4 vs. 96.7), while the two cases where it is better (math: 82.9% vs. 82.6%; LLaVA: loss 1.075 vs. 1.087) show marginal gaps. The word "consistently" does not match the data, most of which are within statistical noise. Similarly, the abstract frames the contribution as "further reducing the memory required for fine-tuning" relative to standard LoRA — a benefit already achieved by the simpler LoRA-FA.

### Minor

3. **Theoretical assumptions limit practical relevance of the main result.** Theorem 4.4 assumes that ΔW entries are i.i.d. Gaussian and independent of input (Assumption 4.1), and the analysis considers each submodule in isolation with stationary targets. The paper acknowledges the stationarity limitation but does not discuss the Gaussian randomness assumption. Under realistic conditions where the fine-tuning target has task-specific structure and submodules interact via backpropagation, the theory does not predict whether local unsupervised updates (which ignore task alignment) will help or hurt. The experimental results suggest the latter — they do not help consistently.

4. **LoLoRA introduces extra overhead for no clear benefit.** While memory savings are identical to LoRA-FA, LoLoRA requires an additional optimizer state for A and computation for the local rule (HPCA or AE). The LLaVA experiment (Table 4) shows LoLoRA HPCA takes 2h 52m vs. 2h 46m for LoRA-FA (uniform). The memory difference between LoLoRA (24.1 GB) and LoRA-FA (23.9 GB) is negligible. The paper acknowledges the extra optimizer state as a limitation but does not provide a full accounting of the computational overhead (wall-clock time across all experiments, extra FLOPs).

5. **Design choice of update timing in Algorithm 1 is undiscussed.** The algorithm computes u = Az in line 1, then updates A via the local rule in lines 2–4, then computes h = Wz + Bu in line 5 using the *pre-update* u. This means A is updated every step using the current input, but the forward pass output uses the old A's projection. The possible misalignment between the updated A and B's gradient (which flows through the old u) is not analyzed or compared with the alternative (updating A after the forward pass for the next batch).

### Trivial
None.

## Nice-to-Haves

- The central hypothesis — that local updates adapt to input distribution shifts — would be most naturally tested in a **non-stationary fine-tuning scenario** (e.g., continual learning, temporal distribution shift) where the static EVA initialization would become genuinely suboptimal and online HPCA should demonstrate an advantage. The current experiments are on stationary tasks where the initial PCA is already good.
- A sensitivity analysis of the HPCA smoothing factor (stated as 0.98) and local learning rate would aid reproducibility.
- Reporting wall-clock time and peak memory consistently across all experiments (not just LLaVA) would give a complete cost picture.

## Removed Points

These points were flagged by the reviewers but are removed or demoted for the following reasons:

- *"GLUE experiments do not report full test sets"* — The paper clearly states it uses a "GLUE subset" with standard metrics; this is standard practice and not a weakness.
- *"Memory numbers in Table 3 are ambiguous"* — The LLaVA section (line 341) explicitly defines "peak extra GPU memory as the difference between the peak allocated memory and the memory required to store the frozen base model parameters in bfloat16," clarifying the methodology used across experiments.
- *"Algorithm 1 feedback effect concern"* — The critic worried that updating A before the output creates instability. In fact, u = Az is computed in line 1 *before* the A update in line 4, so the forward pass output uses the old A. The specific concern about feedback effects is not supported by the algorithm as written.
- *"Missing PiSSA initialization baseline"* — PiSSA is included in the ablation (Table 5).
- *"SoftHebb failure not discussed"* — Table 6 reports SoftHebb's substantially worse performance; this is an empirical ablation finding that the paper reports without extensive commentary, which is standard and acceptable.
- *"Could the metric be measuring a proxy?" / general speculative concerns* — These are area-of-concern sweeps that the harsh critic was instructed to generate. They lack specific anchors in the paper's content and are removed.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Reframe the contribution.** The paper's strongest result is Theorem 4.4 (formalizing the optimality of PCA-based A initialization under random regression) and the thorough empirical comparison of initializations and local rules. The current framing overclaims an advantage for online local updates over static initialization that the data do not support. A more honest narrative — "we provide theoretical grounding for data-driven A initialization and systematically compare freezing vs. online local updates, finding they perform similarly" — would better reflect the results.

2. **Add a non-stationary experiment.** If the method genuinely adapts to shifting input distributions (as claimed in the abstract), test it on a setting where the distribution does shift (e.g., curriculum learning, multi-task sequence, or temporal drift). This would be the strongest possible evidence for the method's key differentiator.

3. **Report consistent runtime and memory metrics across all experiments**, not only in the LLaVA section.

## Score and Decision

### Calibration

**Round 1 — Bracketing:** I queried three bands on the topic of LoRA/PEFT memory-efficient fine-tuning:
- **Low band (score < 3.5):** Retrieved anchors included FCLoRA (2.50), OP-LoRA (3.00), DASP (3.00), and an adaptive PEFT paper (3.33). All are clearly weaker than LoLoRA in theoretical depth and experimental scope.
- **Mid band (3.5–7.5):** Retrieved LoFT (6.00), LoRAct (4.00), Taming Momentum (6.00), and ScaLoRA (4.80). These form the relevant comparison range.
- **High band (>7.5):** Retrieved papers on matrix sign methods and RL — topically unrelated. Not useful for comparison.

**Initial bracket:** 3.5 – 5.5.

**Round 2 — Narrowing:** I queried narrower bands within the bracket:
- **LoRA-FA paper (3.50, Reject)** — Proposes freezing A itself. LoLoRA has a cleaner theoretical contribution (Theorem 4.4) and more thorough ablations. LoLoRA is clearly stronger.
- **LoRAct (4.00, Reject)** — Activation compression for PEFT. Similar level: incremental contribution, missing baselines, limited comparison. Comparable to LoLoRA.
- **Stable-LoRA (4.00, Poster Accept)** — Theory-driven stabilization of LoRA training. Clearer empirical improvements (though modest) than LoLoRA, weaker theory. Comparable overall quality.
- **Adversarial price paper (4.50, Reject)** — First theoretical analysis of LoRA robustness. LoLoRA's theory is cleaner and more directly relevant, but both have debatable practical significance.
- **ScaLoRA (4.80, Reject)** — Strong theory but marginal gains. ScaLoRA at least shows consistent (small) improvements; LoLoRA's core claim fails against the right baseline. LoLoRA is somewhat weaker.
- **PSOFT (5.00, Poster Accept)** — Principal subspace orthogonal fine-tuning. Clear and consistent empirical improvements over baselines. LoLoRA is weaker.

The paper sits at **4.0**. The theoretical contribution is genuine and the ablation is thorough, but the central empirical claim is not supported — the method does not outperform the simpler LoRA-FA (EVA) baseline it seeks to improve upon. The overstatement in the conclusion further undermines the presentation. These weaknesses are structural, not fixable with minor revisions.

**Score: 4.0 — Decision: Reject**

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>