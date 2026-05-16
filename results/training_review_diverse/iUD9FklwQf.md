Here is my final consolidated review:

---

## Summary

This paper presents G4SATBench, the first unified benchmark for GNN-based SAT solving. It curates 7 synthetic SAT datasets across 3 difficulty levels, re-implements multiple GNN baselines (NeuroSAT, GCN, GGNN, GIN) under a common interface, and systematically evaluates them on three tasks (satisfiability prediction, satisfying assignment prediction, unsat-core variable prediction) with multiple training objectives and inference algorithms. Beyond benchmarking, the paper conducts comparative analyses suggesting that GNNs develop a solving strategy resembling greedy local search but struggle to learn CDCL heuristics in latent space.

## Strengths

- **First unified benchmark for GNN-based SAT solving.** G4SATBench fills a real gap by providing standardized datasets (7 problem families × 3 difficulty levels), re-implemented baselines with identical interfaces, and a common evaluation protocol. This addresses the reproducibility problems noted across prior work (Section 4.1, Table 1) and will be a useful resource for the community.

- **Large-scale systematic evaluation.** The paper conducts extensive hyperparameter tuning (grid search) and runs experiments across 3 seeds, totaling ~8,000 GPU hours. The evaluation spans 4 GNN architectures, 2 graph constructions, 3 prediction tasks, 3 training objectives, and multiple inference algorithms—making it the most comprehensive empirical baseline to date (Section 5, Tables 1–4).

- **Valuable empirical finding: unsupervised losses consistently outperform supervised learning for satisfying-assignment prediction.** Table 2 (labeled Tab. 2 in paper) shows that unsupervised objectives (UNS₂) achieve substantially higher solving accuracy than supervised training across most datasets, with gains of 30–70 percentage points on medium CA/PS datasets. The paper correctly attributes this to the multiplicity of satisfying assignments and the bias of supervised learning toward a single solution (Section 5.2).

- **Systematic generalization analysis across distributions and difficulty levels.** Figures 2 and 3 evaluate cross-dataset and cross-difficulty transfer, showing that SR-trained models generalize best and that transfer across substantially different distributions remains challenging. The observation that models generalize better from hard to easy than vice versa is worth highlighting (Section 5.1).

- **Analysis of iterative decoding behavior linking GNNs to local search patterns.** Figure 6 quantifies distinct assignments, variable flips, and unsatisfied clauses per iteration, showing a pattern of many early flips and convergence. This analysis provides a useful lens for understanding GNN behavior during SAT solving (Section 6.2).

## Weaknesses

### Fatal
None.

### Major

- **The contrastive pretraining experiment (Table 6) is underspecified and its conclusion is premature.** The paper concludes that GNNs "still encounter difficulties in effectively learning the CDCL heuristic in the latent space" based on minimal (≤1%) performance changes after contrastive pretraining. However, it provides no evidence that the pretraining actually succeeded: no final contrastive loss values, no cosine similarity between original and augmented representations, no t-SNE or other visualization, and no downstream analysis verifying that representations of original/augmented pairs became closer. Without such verification, the null result could simply reflect ineffective pretraining (e.g., insufficient training, poor hyperparameters, or a hard contrastive task) rather than a fundamental inability of GNNs to learn CDCL heuristics. This gap undermines one of the paper's central analysis claims. The authors should either demonstrate that the pretraining was effective or substantially temper the conclusion.

### Minor

- **No variance or statistical significance reported for any result.** All tables present only mean accuracy across 3 seeds, without standard deviations or confidence intervals. For a benchmark paper intended as a community reference, this is a notable omission. Readers cannot assess which differences between methods/losses are reliable (e.g., in Table 1, NeuroSAT on LCG\* and GGNN on VCG\* often differ by <1 percentage point). Reporting standard deviations would significantly increase the paper's value.

- **The claim that GNNs learn a greedy local search strategy is suggestive but not conclusively supported.** The evidence in Figure 6 (decreasing flipped variables and unsatisfied clauses over iterations) is consistent with a greedy local search pattern, but also consistent with iterative refinement converging to a fixed point—a general property of many GNN architectures. The paper does not directly compare the GNN's trajectory to that of an actual LS solver (e.g., GSAT or WalkSAT) on the same instances, which would substantially strengthen the claim. The paper uses cautious language ("reminiscent of," "akin to"), which partially mitigates this, but the abstract and introduction make a stronger positive claim ("effectively learn a solving strategy akin to greedy local search") that would benefit from more direct evidence.

- **Analysis of predicted assignments (Figure 6) relies on visual trends without quantitative summary measures.** The paper would benefit from reporting concrete numbers such as mean convergence iteration, fraction of instances where the final assignment is satisfying, or quantitative overlap between GNN and GSAT flips on the same instances.

- **The augmented-instance experiment (Table 5) lacks a control: testing the model trained on augmented instances on *original* instances.** If the augmented-trained model fails on original instances, this would suggest overfitting to augmented structure rather than learning a generalizable CDCL-like strategy. Adding this control would clarify the interpretation.

### Trivial

- The paper mentions computing dataset statistics ("compute several statistics of the SAT instances across difficulty levels") but does not show them in the main text. A summary table of mean/median variables, clauses, and clause-to-variable ratio per dataset and difficulty level would improve interpretability.

## Nice-to-Haves

- **Hyperparameter ranges:** The paper mentions grid search but does not report the ranges searched for each model. Providing these would aid reproducibility.
- **Direct GSAT comparison:** A head-to-head comparison of GNN and GSAT trajectories (e.g., Hamming distance between flips) would turn a plausible observation into a convincing result, but the paper's cautious language makes this an enhancement rather than a fix.
- **Additional pretraining verification:** Beyond the contrastive experiment, alternative approaches (e.g., distilling CDCL solver decisions) could provide additional evidence about whether GNNs can learn CDCL heuristics.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Figure 3 (referenced as Figure 2 in text)"** — The paper correctly references Figure~\ref{fig:sat-diff} for cross-difficulty transfer. The figure numbering is consistent in the paper; this appears to be a reviewer misreading.
2. **Criticism that dataset statistics are missing as a primary weakness** — The paper mentions computing statistics; omitting them from the main text is a minor presentation gap, not a structural weakness. Moved to Trivial.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface any insight about the paper that the authors themselves have not already identified or discussed.

## Suggestions

1. Add standard deviations to all tables (the single highest-impact improvement for a benchmark paper).
2. Verify that the contrastive pretraining actually made representations of original and augmented instances similar (report contrastive loss, cosine similarity) before drawing conclusions about GNNs' inability to learn CDCL.
3. Either strengthen the LS claim with direct comparison to a GSAT solver on the same instances, or soften the language in the abstract/introduction to match what the evidence supports.
4. Add a control to Table 5: test the augmented-trained model on original instances.
5. Include a brief dataset statistics table in the main text.

## Score and Decision

This is a solid benchmark paper that makes a genuine contribution (unified datasets, re-implemented baselines, comprehensive evaluation) and provides interesting analytical insights. The core benchmark contribution is not undermined by the weaknesses—the curated datasets and reproducible baselines will be valuable regardless. However, two of the paper's central analysis claims (that GNNs learn a greedy local search strategy and that they cannot learn CDCL heuristics) are currently supported by evidence that is either suggestive rather than conclusive (LS claim) or underspecified (contrastive pretraining). These are fixable in revision but do reduce the strength of the paper as it stands.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>