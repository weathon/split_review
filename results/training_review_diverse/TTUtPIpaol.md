Now I have all the information I need. Let me compose the final review.

## Summary

This paper introduces EEP (Efficient Expert Pruning), a gradient-free evolutionary method for pruning experts in Sparse Mixture-of-Experts (SMoE) language models. EEP operates in two phases: (1) discrete expert pruning via evolutionary search over a router mapping matrix (one-hot) to select which experts to retain, and (2) continuous expert merging where the same matrices become real-valued to combine knowledge from pruned experts into survivors. The key empirical results are striking: on Mixtral 8×7B, pruning from 8 to 4 experts raises average accuracy across 10 benchmarks from 62.4% (full model) to 70.3% (prune-only) and 74.2% (prune+merge), with SQuAD improving from 53.4% to 80.6%. The method generalizes to Mixtral 8×22B, Qwen-MoE models, and MMLU (including out-of-distribution tasks), and yields measurable memory savings (47-71%) and inference speedups (up to 1.41×).

## Strengths

- **EEP achieves high sparsity with substantial performance improvements, even without fine-tuning.** Reducing experts by 50-75% consistently improves over the full model on most benchmarks. At 4 experts on Mixtral 8×7B, Prune Only averages 70.3% vs. the full model's 62.4% (Table 1). The improvement is sustained across 10 diverse tasks, not cherry-picked.

- **The two-phase gradient-free paradigm (pruning + merging via evolutionary search) is novel and effective.** The paper cleanly separates discrete selection (pruning phase) from continuous weight combination (merging phase), and shows that merging consistently adds 3-6 points over pruning alone (Table 1). This contrasts with prior work that either requires gradient-based fine-tuning or uses predefined importance criteria.

- **The method generalizes across models, model scales, and task distributions.** Results on Mixtral 8×22B (Table 2) and Qwen models show consistent improvements. The MMLU experiment (50 in-distribution + 7 OOD tasks, Table 3) demonstrates that EEP outperforms all baselines on both held-in and unseen tasks.

- **Profiling data shows practical deployment benefits.** Reducing total experts from 8 to 4 cuts GPU memory from 88.6 GB to 46.6 GB (47% savings) while maintaining or improving accuracy, and combining with 1 active expert achieves 1.41× speedup (Table 4).

- **The observation that pruning improves routing is supported by activation pattern analysis.** Section 5.6 provides suggestive evidence (Figure 5) that the router's behavior shifts meaningfully after pruning, offering a plausible mechanism for the counterintuitive performance improvement.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **Search cost is not quantified.** The paper claims efficiency ("Efficient Expert Pruning") and that the method "can be conducted on devices capable of inference," but provides no concrete numbers on the computational cost of the evolutionary search — GPU hours, number of forward passes, or wall-clock time. The limitations section merely acknowledges it "requires a potentially costly search process" without bounding it. This makes it difficult for a practitioner to assess the trade-off between search cost and downstream gains. Reporting search cost (e.g., total forward passes or GPU hours for the main Mixtral 8×7B experiments) is essential.

- **Search hyperparameters are absent from the main text.** Population size, number of generations, mutation rate/noise scale, the exact size of the sampled search subsets per dataset, and whether crossover is layerwise or matrixwise are not reported in the main paper. While the appendix (stripped by the parser) may contain these, key numbers (e.g., search set size, number of generations) should be in the main text for reproducibility and to let readers assess the search's affordability.

- **No confidence intervals or variance estimates for EEP results.** The paper reports random-baseline variance (30 runs) but presents all EEP results as point estimates. Given the stochastic nature of evolutionary search, reporting standard deviations across multiple search runs (or at least across different search subsets) would strengthen confidence that reported gains are robust rather than tied to a specific search trajectory.

- **The "without any fine-tuning" phrasing is imprecise when applied to the full pipeline.** The abstract states EEP achieves better performance "without any fine-tuning" and supports this with the prune-only SQuAD result (53.4%→75.4%). This is accurate for the prune-only phase. However, the full EEP pipeline includes the merging phase, which updates all surviving expert weights via linear combination — an operation many readers would consider a form of adaptation. The paper should clearly distinguish "no gradient-based fine-tuning" from "no weight updates at all."

- **The MMLU OOD result is modest relative to in-distribution gains.** On the 7 unseen MMLU datasets (Table 3), EEP (Prune+Merge) achieves 71.3% at 6 experts vs. the full model's 72.6% — a slight degradation. The claim of "strong generalization ability" should be tempered; the method generalizes well across in-distribution tasks but does not meaningfully improve over the full model on OOD tasks.

- **Router analysis is illustrative but not conclusive.** Section 5.6 provides activation statistics (Figure 5) for one layer on one dataset. While suggestive, this does not constitute a direct causal test of the "fewer experts improve routing" hypothesis. Controlled experiments (e.g., comparing EEP-selected patterns against random pruning with equivalent sparsity, or measuring router agreement with a reference assignment) would strengthen the mechanistic claim.

### Trivial

- **Numerical inconsistency:** The abstract and contributions section report SQuAD prune-only accuracy as 75.4%, while Table 1 shows 75.2% for the same condition. Likely a rounding or run-to-run variation, but should be reconciled.

## Nice-to-Haves

- A controlled ablation comparing EEP-selected pruning patterns against random pruning at the same sparsity level (with the same merging applied) would help isolate the benefit of the search from the benefit of the merging mechanism.
- Profiling across multiple tasks and batch sizes (not just SQuAD at batch size 256) would strengthen the efficiency claims.
- A simple baseline that uses NAEE/Frequency to select the pruning pattern and then applies a lightweight merging (uniform averaging or frequency-weighted) would help disentangle the value of the evolutionary search from the value of the merging itself.

## Removed Points

- **"Baselines are one-shot methods that do not use any training data" (from Critical Issue 4).** This is incorrect. NAEE "exhaustively evaluates the loss between the full model and all pruning choices" — this requires data. Frequency and soft-activation baselines also require forward passes on data to compute activation statistics. The comparison is not as inequitable as claimed. This point is removed as factually wrong.

- **Criticisms about missing appendix content** (e.g., reproducibility details from Critical Issue 5). The review parser strips appendix sections from all papers; these details exist in the original submission. However, the main-text omission of key numbers (population size, search set sizes, GPU hours) remains a valid minor weakness as noted above.

- **The claim that the SQuAD improvement is "extraordinary" and the most plausible explanation is overfitting (Critical Issue 2).** The improvement is large but consistent across 10+ benchmarks. It is unlikely that overfitting to a single search subset would simultaneously improve performance on 10 diverse tasks (COPA, MultiRC, WIC, WSC, RTE, BoolQ, CB, ReCoRD, DROP, SQuAD). The overfitting concern is valid but the reviewer overstated its severity.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Quantify search cost** in the main text: report GPU hours or total forward passes for the main experiments (Mixtral 8×7B, 4 experts, on a representative task). This directly addresses the most significant omission and lets readers judge the efficiency claim.
2. **Report EEP results with variance** across at least 3 search runs or search-subset samples for one or two representative tasks to demonstrate robustness against overfitting.
3. **State search set sizes explicitly** for each experiment (e.g., "1024 examples per task").
4. **Clarify the "no fine-tuning" language** throughout to distinguish "gradient-free" from "no weight updates" — the pruning phase genuinely requires no updates, while the merging phase performs weight averaging.
5. **Include a controlled router experiment** (e.g., random pruning vs. EEP-selected pruning at the same sparsity, with both followed by the same merging) to strengthen the mechanistic claim.

## Score and Decision

This paper makes a genuine contribution: a novel, effective, gradient-free approach to expert pruning that achieves strong empirical results across multiple models and tasks. The core claims are well-supported by the experimental data. The weaknesses are real but minor — they concern missing details and presentation clarity rather than structural flaws. The paper would benefit from addressing these in a revision, particularly the search-cost quantification.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>