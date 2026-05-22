Now I have a thorough understanding of the paper and all the reviewers' claims. Let me write the consolidated review.

## Summary

The paper introduces LoLoRA, a LoRA variant that updates the low-rank adapter matrix *A* using local Hebbian PCA (HPCA) rules on the forward pass, avoiding the need to store input activations for *A*'s backward pass and thereby achieving the same memory savings as LoRA-FA (where A is frozen). The authors provide theoretical analysis (Theorems 4.4–4.6) showing that under a random regression target assumption, the optimal *A* spans the top-*r* eigenvectors of the input covariance matrix—motivating PCA-based local updates. Experiments on GLUE, MetaMathQA→GSM8K, LLaVA, and ablations on TinyLlama compare LoLoRA against LoRA and LoRA-FA (with uniform and EVA initializations).

## Strengths

- **Clean theoretical derivation of optimal A (Theorem 4.4).** The paper proves that under a random-ΔW₀ assumption, the optimal fixed *A* consists of an arbitrary nonsingular transformation of the top eigenvectors of Σ_zz. This provides a principled foundation for why PCA-based initialization (EVA) or PCA-convergent local updates (HPCA) are sensible for *A*. The asymmetry between *A* and *B* (Theorem 4.5 shows any full-rank *B* initialization is equivalent) is a genuinely useful conceptual insight.

- **Thorough ablation of local update rules (Table 6).** The paper systematically compares HPCA, HPCA with SVD-first initialization, AE (autoencoder), and SoftHebb across ranks 2, 4, 8 on TinyLlama-1.1B. The results confirm that HPCA-based rules converge to the PCA subspace and perform best among the local alternatives, validating the design choice.

- **Empirical demonstration of memory savings over standard LoRA.** Tables 3 and 4 show that LoLoRA reduces peak extra memory by ~13% compared to standard LoRA (26 GB vs. 30 GB on MathQA, 24.1 GB vs. 24.6 GB on LLaVA) while maintaining competitive accuracy/perplexity. This confirms the core practical benefit of not storing activations for *A*.

- **Online adaptation avoids a separate precomputation pass.** Unlike LoRA-FA (EVA), which requires a pre-processing PCA pass over the dataset to initialize *A*, LoLoRA's HPCA updates converge to the same subspace during training itself. This is a practical logistical advantage for memory-constrained settings where a separate precomputation pass is inconvenient.

## Weaknesses

### Fatal
None.

### Major

- **The empirical evidence does not show a meaningful advantage over LoRA-FA (EVA), the strongest frozen-A baseline.** The paper's central claim is that online HPCA updates improve over a one-time PCA initialization, but the numbers do not support this:
  - **GLUE (Tables 1–2):** LoLoRA is comparable to LoRA-FA (EVA) but is *worse than LoRA-FA (uniform)* on 5 of 8 tasks (often by non-trivial margins, e.g., RTE 84.6 vs. 86.4, CoLA 66.3 vs. 67.9).
  - **MathQA (Table 3):** LoLoRA ties LoRA-FA (EVA) at 0.829 ± 0.004 vs. 0.829 ± 0.005—identical within error bars.
  - **LLaVA (Table 4):** LoLoRA achieves *worse* perplexity (2.93) than LoRA-FA (EVA) (2.92) and than standard LoRA (2.90).
  
  The claim "HPCA consistently outperforms standard LoRA-FA in two out of three experimental setups" refers to LoRA-FA with *uniform* initialization, not the stronger EVA variant. When compared against LoRA-FA (EVA)—which also requires no backprop through *A*—LoLoRA does not show a clear quality gain in any experiment. This undermines the paper's core value proposition.

- **Memory footprint is identical to LoRA-FA, not an improvement.** Tables 3 and 4 show LoLoRA uses essentially the same peak extra memory as LoRA-FA (26 GB vs. 26 GB in Table 3; 24.1 GB vs. 23.9 GB for LoRA-FA in Table 4). The abstract's phrasing "further reducing the memory required for fine-tuning" is ambiguous: the reduction is relative to standard LoRA (which is true), but the paper gives the impression of improving upon LoRA-FA's memory. Additionally, LoLoRA adds optimizer state for the local updates (acknowledged in the conclusion), which slightly *increases* memory vs. LoRA-FA in the LLaVA experiment (24.1 GB vs. 23.9 GB).

- **Best-in-training reporting for MathQA (Table 3) is a methodological concern.** The paper reports the best accuracy observed during training (evaluated every 0.2 epochs), rather than the final checkpoint. While this is applied uniformly to all methods in the table, it inflates absolute numbers and is inconsistent with the GLUE and LLaVA experiments (which use final metrics). This weakens the reliability of the reported values.

### Minor

- **Theoretical analysis applies to an idealized setting that differs from practice.** The derivation (Theorems 4.4–4.6) assumes an isolated linear submodule with i.i.d. Gaussian ΔW₀ and stationary input distribution. The paper acknowledges this limitation in the conclusion, but the gap between the theory and the actual deep transformer setting (nonlinearities, non-stationary inputs, structured task-dependent ΔW₀) is not bridged. The theory provides intuition but does not constitute a proof of LoLoRA's effectiveness in practice.

- **Missing comparison to other memory-efficient PEFT methods.** The paper compares only LoRA, LoRA-FA, and their initialization variants. Other methods that also avoid storing activations or use local learning (e.g., VeRA, Local LoRA, chunked local learning) are mentioned in related work but never evaluated. Without these comparisons, it is unclear how LoLoRA's memory–performance trade-off positions against the broader landscape.

- **LoLoRA underperforms LoRA-FA (uniform) on most GLUE tasks.** The fact that simply freezing A with uniform random initialization often matches or beats the more complex HPCA-based updates on 5 of 8 GLUE tasks is a surprising result that the paper does not adequately investigate or explain.

- **HPCA (svd first) and HPCA (uniform) perform nearly identically in ablations (Table 6).** This implies the online HPCA updates do not significantly deviate from the initialization, and a good initialization (EVA) may be sufficient. It weakens the argument that online adaptation provides additional value beyond a one-time PCA pass.

### Trivial
None.

## Nice-to-Haves
- Final-checkpoint results for MathQA in addition to best-in-training numbers.
- A controlled experiment tracking the subspace overlap (e.g., principal angle) between the online-learned *A* and the true top-*r* eigenvectors of the input covariance during training.
- A memory breakdown bar chart showing peak memory contributions per component (W, A optimizer, B optimizer, input activations, local optimizer) for LoRA, LoRA-FA, and LoLoRA.

## Removed Points
The following points from the reviewers were evaluated against the paper and removed:

1. **"Misleading framing of memory savings" (Harsh Critic #1):** The abstract says "further reducing the memory" — this is a comparison to standard LoRA, not to LoRA-FA. The paper's memory numbers (26 GB vs. LoRA's 30 GB) confirm this claim is factually accurate. The paper clearly describes the mechanism and shows identical memory to LoRA-FA in the tables. Removed as factually incorrect criticism.

2. **"Theoretical analysis rests on assumptions that are not satisfied" as a structural weakness (Harsh Critic #3):** The paper explicitly acknowledges this limitation in the conclusion ("each submodule isolated with stationary targets, which is not strictly the case"). This is standard practice for providing theoretical intuition in ML papers. Downgraded from a structural weakness to a minor point; the reviewer's framing as a core flaw overstates the issue.

3. **"LoLoRA underperforms LoRA-FA (uniform) on 6 out of 8 GLUE tasks":** The correct count is 5 of 8 (CoLA, RTE, MNLI, QQP, SST-2 — LoLoRA is better on MRPC and QNLI, tied on STS-B). The critic rounded up, and more importantly, the paper's claim is about comparison to LoRA-FA (EVA), not uniform. Removed as imprecise; the underlying concern (weak empirical advantage) is already captured in the Major weakness about LoRA-FA (EVA).

4. **Pure formatting/style nitpicks:** Any criticism about missing appendices or parser-stripped content is removed per the hard rules.

5. **Strength Finder's generic strengths** (e.g., "the paper tackles a genuinely interesting question"): Removed as generic/superficial.

## Novel Insights
None beyond the paper's own contributions. The theoretical derivation (Theorem 4.4) is the paper's most insightful component—it cleanly characterizes the optimal *A* subspace under a random target assumption and provides a principled explanation for the empirical success of PCA-based initialization methods like EVA. However, this insight primarily supports EVA (a prior method) rather than LoLoRA specifically, and the reviewers did not surface additional novel observations beyond what the paper itself provides.

## Suggestions
1. **Re-center the paper's contribution on the theoretical insight and ablation study**, and present LoLoRA as a practical alternative to LoRA-FA that avoids a separate PCA precomputation pass, rather than claiming quality improvements over LoRA-FA (EVA) that the data do not support.
2. **Investigate why LoRA-FA (uniform) outperforms both EVA-initialized variants and LoLoRA on many GLUE tasks** — this counterintuitive result deserves explanation and would strengthen the paper's understanding of when PCA-based subspaces help vs. hurt.
3. **Add a clearer comparison protocol**: run the same evaluation metric (final checkpoint or best-in-training) consistently across all experiments, and report statistical significance tests to clarify whether observed differences are meaningful.
4. **Include at least one additional memory-efficient PEFT baseline** (e.g., VeRA or Local LoRA) to position LoLoRA in the broader landscape.

## Score and Decision

**Calibration anchors** (retrieved from the human-review corpus):

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| `LoRA-FA` (RbKThNNFxr.md) | 5.33 (Reject) | LoRA-FA also freezes A to save memory. That paper had cleaner empirical support (no performance degradation) but less theory. LoLoRA has more theory but weaker empirical support vs. its key baseline. **LoLoRA is slightly weaker overall.** |
| `ReLoRA` (DLJznSp6X3.md) | 5.75 (Accept) | ReLoRA proposed a more complex training scheme with mixed empirical results but was accepted. LoLoRA has comparable theoretical depth but the empirical gap vs. its closest baseline is more pronounced. **LoLoRA is weaker.** |
| `ALLoRA` (7X65yoKl3Y.md) | 3.33 (Reject) | ALLoRA had marginal improvements and missing baselines. LoLoRA has stronger theoretical grounding and cleaner ablations. **LoLoRA is stronger.** |
| `ULoRA` (bYsieh8LE2.md) | 3.67 (Reject) | ULoRA had weak experiments and limited novelty. LoLoRA is more rigorous. **LoLoRA is stronger.** |
| `Activations Aren't Cheap` (3ylNuZXtMg.md) | 4.25 (Reject) | A simple reformulation with limited novelty. LoLoRA has more theoretical contribution but weaker empirical validation. **Comparable.** |
| `RandLoRA` (Hn5eoTunHN.md) | 6.00 (Accept) | Clean story, clear motivation, stronger empirical results across vision and language. **LoLoRA is weaker.** |
| Continual learning paper (2LhCPow6I.md) | 2.33 (Reject) | Unrelated topic with very weak results. **LoLoRA is much stronger.** |

The paper has a genuine theoretical contribution (characterizing optimal *A*) and a thorough ablation of local learning rules, but the central empirical claim—that online HPCA updates improve over a one-time PCA initialization—is not supported by the experiments. On every benchmark, LoLoRA either ties or loses to LoRA-FA (EVA), the directly comparable baseline that also avoids backprop through *A*. Given this gap between the claimed contribution and the evidence, the paper does not meet the bar for acceptance.

**Score:** 4.0

**Decision:** Reject

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>