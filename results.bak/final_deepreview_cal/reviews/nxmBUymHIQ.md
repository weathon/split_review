Now I have all the information needed. Let me synthesize the final consolidated review.

## My Bracket and Calibration Summary

**Round 1 bracketing** placed this paper between 3.5 and 5.5, based on comparison to the LoRA-FA anchor (5.33, rejected), EVA paper (4.75, rejected), and other PEFT variants.

**Round 2 narrowing** anchors within the bracket: EVA (4.75, rejected), EigenLoRA (5.00, rejected), DeLoRA (5.25, accepted), SubZero (4.25, rejected). The paper is closest in nature to the EVA paper (same topic, similar criticisms) and the LoRA-FA paper (same problem setting, similar core issue of incremental contribution).

**Final position**: Below LoRA-FA (5.33) and DeLoRA (5.25), comparable to EVA (4.75) and EigenLoRA (5.00). The paper has a genuine theoretical contribution (Theorem 4.4) that the EVA paper lacked, but its core practical claim — that local updates to A improve over freezing with good initialization — is unsupported. The method contribution is weaker than LoRA-FA's simpler, more impactful idea. Score: **4.5**.

---

## Final Review: LoLoRA

## Summary

This paper proposes LoLoRA, a hybrid fine-tuning method that replaces gradient-based training of LoRA's down-projection matrix A with forward-pass Hebbian PCA (HPCA) updates, while training the up-projection matrix B via standard backpropagation. The method is motivated by reducing activation memory for the A adapter. The paper provides a theoretical analysis (Theorem 4.4) showing that the optimal initialization for a frozen A spans the dominant eigensubspace of the input covariance matrix, consistent with data-driven initialization methods like EVA. Experiments on GLUE, mathematical reasoning, and multimodal fine-tuning evaluate the approach against LoRA and LoRA-FA baselines.

## Strengths

- **Clean theoretical characterization of optimal A initialization (Theorem 4.4).** The paper proves that under a random regression assumption, the optimal frozen A is any nonsingular linear transformation of the first r principal components of the input covariance matrix. This formally justifies data-driven initialization of A, going beyond prior empirical observations (e.g., EVA). Theorem 4.5's result that any full-rank B initialization is equally optimal is a nice complementary result.

- **Systematic ablation across initializations and local update rules (Tables 5, 6).** On TinyLlama/Alpaca, the paper compares four LoRA-FA initializations (Uniform, Orthogonal, PiSSA, EVA) and five local update rules for LoLoRA (HPCA variants, AE, SoftHebb). The finding that different local rules converge to similar perplexity — matching LoRA-FA (EVA) — supports the claim that they converge to the same optimal subspace.

- **Memory savings relative to standard LoRA are demonstrated.** On math reasoning (Table 3), LoLoRA achieves 26 GB extra memory vs. LoRA's 30 GB (a 13% reduction), and on GLUE the paper reports up to 20% savings. The memory measurement methodology (peak allocated excluding model parameters) is clearly defined in Section 5.3.

- **Empirical validation across three domains.** The method is tested on NLU (GLUE, RoBERTa-large), mathematical reasoning (GSM8K, LLaMA-3.1-8B), and multimodal fine-tuning (LLaVA-v1.5-7B), demonstrating generality.

## Weaknesses

### Major

- **The core method does not improve over LoRA-FA with good initialization — the central claim is unsupported.** The paper's thesis is that local updates to A mitigate the performance trade-off of freezing A. However, the experiments consistently show that the simpler baseline — LoRA-FA with EVA initialization — matches or exceeds LoLoRA on nearly every metric:
  - **Math reasoning (Table 3):** LoLoRA HPCA and LoRA-FA (EVA) both achieve exactly 82.9% — a tie.
  - **Multimodal (Table 4):** LoLoRA (2.93 perplexity) sits between LoRA-FA uniform (2.97) and LoRA-FA EVA (2.92). The EVA-initialized frozen baseline is strictly better.
  - **Ablations (Tables 5 vs. 6):** LoLoRA HPCA yields perplexity 2.557 (r=2), 2.546 (r=4), 2.535 (r=8). LoRA-FA (EVA) yields 2.558, 2.546, 2.536 — **functionally identical**. The online HPCA updates are neither better nor meaningfully different from simply using a PCA initialization and freezing.
  - On GLUE, LoLoRA slightly edges LoRA-FA (EVA) on some tasks, but the gap is well within error bars and LoRA-FA (uniform) itself beats LoLoRA on most tasks.

  When the proposed method's results are indistinguishable from a simpler, cheaper baseline (LoRA-FA with EVA initialization) that also saves memory, the practical contribution of the online update mechanism is not demonstrated. The paper's claim that "HPCA consistently outperforms standard LoRA-FA" (conclusion) relies on defining "standard" as uniform initialization — a weak and misleading comparison.

- **The theoretical contribution justifies EVA initialization, not online updates.** Theorem 4.4 derives the optimal frozen A — which elegantly explains why EVA initialization works. But the paper then proposes iterative local updates to A (HPCA) that converge to the same subspace during training. Since the experiments show that freezing at the optimal initialization achieves identical results, the theory does not motivate the method. The paper never demonstrates a scenario where distribution shift or non-stationarity makes online adaptation beneficial. The theory is sound but orthogonal to the claimed contribution.

- **Missing direct comparison of LoLoRA vs. LoRA-FA (EVA) with the same initialization across all experiments.** The most informative comparison — LoLoRA versus LoRA-FA (EVA) with the same initial A — is only shown in Table 4 (multimodal). On GLUE (Tables 1-2) and math reasoning (Table 3), LoLoRA is initialized uniformly, while the EVA baseline is a separate LoRA-FA run. The paper should have included LoLoRA initialized with EVA (as in Table 4) across all experiments, or at least directly compared the two consistently.

### Minor

- **Best-checkpoint selection on the test set (math reasoning experiment).** The paper reports the best GSM8K result evaluated every 0.2 epochs during a single epoch of fine-tuning (Section 5.2). This is a form of test-set cherry-picking — different methods may peak at different checkpoints, and the reported result does not correspond to a fixed training budget. While all methods are evaluated the same way (making comparisons internally consistent), standard practice is to report either the final checkpoint or best validation result on a held-out set. The paper should clarify whether the pattern of which method peaks first is consistent across seeds.

- **Memory comparison frame is ambiguous.** The paper's memory claims (e.g., "13% extra memory reduction") compare LoLoRA to standard LoRA — which is fair, but incomplete. The relevant scientific comparison for a method that claims to improve over LoRA-FA is against LoRA-FA. LoLoRA uses strictly more memory than LoRA-FA (24.1 GB vs. 23.9 GB in Table 4) because it maintains optimizer state for the local A updates (Algorithm 1, step 3). The paper acknowledges this in the conclusion ("our method introduces a small amount of extra optimizer state...") but the abstract and introduction frame the memory reduction as a feature of the method without this caveat.

### Trivial

- The "Extra Memory" definition for Table 3 is stated in the text as "peak allocated memory, excluding model size" but this is only explicitly defined in Section 5.3 for Table 4. Adding a footnote to Table 3 would improve clarity.

## Nice-to-Haves

- An analysis of convergence speed (how many batches HPCA needs to reach the EVA subspace) would strengthen the claim that local updates are a practical alternative to a separate PCA pre-pass.
- Evaluation on tasks with longer training (multiple epochs) could reveal scenarios where online adaptation is beneficial, since all current experiments are one epoch.
- A direct comparison between LoLoRA (uniform init) and LoRA-FA (EVA) showing the trajectory of A's subspace alignment during training.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"Reproducibility details missing (batch size, LR schedule, warmup referenced as Appendix C)"** — The appendix exists in the original submission; the parser strips it. REMOVED (parser artifact).
- **"The EVA baseline is even weaker" (on GLUE)** — This is factually true for GLUE (EVA underperforms uniform there), but the critic uses it to argue the comparison is weak, which conflates two separate points. REMOVED as redundant to the Major weakness above.
- **"The paper should be compared against LoRA-FA (EVA) with the same rank and training budget"** — Already absorbed into Major weakness #3 above. REMOVED as duplicate.
- **Strength Finder's generic strengths** ("this paper addressed an important problem") — REMOVED. Only strengths with specific content were retained.

## Novel Insights

None beyond the paper's own contributions. The observation that the harsh critic's most damaging point — that LoLoRA ties with the simpler LoRA-FA (EVA) baseline — is visible directly from the paper's own Tables 3, 5, and 6. This is not a novel insight from merging reviews, but rather a clear pattern that the paper under-emphasizes.

## Suggestions

1. **Reframe the paper around the theoretical contribution**: Theorem 4.4 is a genuine contribution that provides theoretical justification for data-driven LoRA initialization (EVA). Consider presenting this as the primary contribution, with the online HPCA updates positioned as a practical alternative for settings where a separate PCA pre-pass is infeasible — supported by evidence of convergence speed.

2. **Add a scenario where online adaptation matters**: Train for multiple epochs, or introduce controlled distribution shift during training, to create conditions where the frozen-A baseline degrades and the local updates can demonstrate adaptive benefit. Without this, the method remains a solution in search of a problem.

3. **Include LoLoRA (EVA) as a consistent baseline** across all experiments, and directly compare against LoRA-FA (EVA) with explicit discussion of the (lack of) improvement.

4. **Report final-checkpoint results** alongside best-checkpoint results for the math reasoning experiment.

## Score and Decision

**Bracket**: Round 1 placed the paper between 3.5 and 5.5. Round 2 narrowed by comparison to:
- EVA paper (4.75, rejected) — shares the same core limitation: the method doesn't clearly improve over simpler alternatives. The current paper has stronger theory but weaker method-demonstration.
- LoRA-FA (5.33, rejected) — a simpler method with the same goal; the current paper adds complexity without demonstrated benefit over LoRA-FA with good initialization.
- EigenLoRA (5.00, rejected) — another LoRA variant with PCA-based ideas and similar incremental-contribution concern.
- SubZero (4.25, rejected) — memory-efficient fine-tuning but a different technical approach.
- DeLoRA (5.25, accepted) — accepted despite incremental concerns, but with clearer empirical wins.

The paper is below LoRA-FA (5.33) and DeLoRA (5.25) because its core method claim is unsupported. It is comparable to EVA (4.75) but slightly weaker in execution: EVA at least showed faster convergence as a practical benefit. The theoretical contribution (Theorem 4.4) is real, but the practical method does not deliver.

**Final score**: 4.5

**Decision**: Reject

The paper contains a genuinely interesting theoretical result (Theorem 4.4), but the proposed method — online local updates to A via HPCA — is not shown to provide any practical benefit over the simpler approach of using PCA-based initialization and freezing A (LoRA-FA with EVA). Across three experimental setups, LoLoRA ties or slightly underperforms LoRA-FA (EVA) while using more memory and computation. The evaluation contains a methodological concern (best-checkpoint reporting on the test set). Without evidence that the method improves over the existing state of the art in its narrow lane, the contribution as a practical fine-tuning method is not demonstrated. A revised submission could reframe around the theoretical result.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>