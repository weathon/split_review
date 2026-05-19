- Decision: Reject
- Avg Score: 4.50
- Scores: 5, 5, 5, 3
Now I have all the information needed. Let me compose the consolidated review.

## Summary

This paper conducts a comprehensive empirical study of data valuation methods applied to graph-structured data in the transductive semi-supervised setting. It evaluates game-theoretic (Shapley, Banzhaf, leave-one-out), predictive (datamodels), and graph-specific (PCW/PCWP) valuation approaches across six datasets and three GNN architectures, introducing α-BANZ as a practical semivalue variant. The core finding is that datamodels (DM) and α-BANZ consistently outperform prior graph-specific methods across multiple downstream tasks including influential node identification, brittleness analysis, poisoning detection, and counterfactual prediction.

## Strengths

- **Comprehensive empirical comparison showing DM and α-BANZ outperform prior graph-specific methods across diverse settings**: In the node-removal experiment (Fig. 3), DM and α-BANZ produce the steepest performance drop when removing top-ranked nodes across all six datasets. The same advantage holds for GAT models (Fig. 4, left column) and in both learning-signal and overall-signal variants. These results are also corroborated on poisoning detection (Fig. 7) and LDS evaluation (Fig. 6).

- **First systematic study of data Banzhaf and datamodels on graphs, with rigorous evidence across multiple downstream tasks**: Neither method had been studied for graph data valuation before. The paper demonstrates their effectiveness on five distinct applications (influential node identification, brittleness analysis, poisoning detection, counterfactual prediction, visualization), providing a solid empirical foundation.

- **Construction of valuation scenarios tailored to the transductive graph setting**: Section 3 formalizes the "train" vs. "all" node sets and "learning signal" vs. "overall signal" utility variants. This captures the unique property of graphs where unlabeled nodes affect both training (via message passing) and inference. The empirical results (Fig. 4, first vs. second row) show that DM and α-BANZ remain superior in both settings.

- **Transferability evidence across architectures**: Fig. 8 shows that α-BANZ values computed with SGC (a cheap model) produce nearly identical node-removal curves when transferred to GCN and GAT, suggesting the values capture intrinsic data properties rather than model-specific artifacts.

- **Theoretical grounding and practical connection between game-theoretic and predictive valuations**: Section 2.1 clearly explains the equivalence between semivalues (with appropriate weights) and linear predictive models, and discusses the connection between Banzhaf values and unregularized datamodels at α=0.5. The introduction of α-BANZ with its maximal-sample-reuse estimator is also well-motivated.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

- **α-BANZ hyperparameter sensitivity is insufficiently analyzed**: The paper tunes α on CoraML (finding α=0.1 optimal) and applies it globally to all other datasets without showing whether this choice is robust across graphs with different sparsity, size, or label rates. Since α=0.5 recovers standard Banzhaf (BANZ), the paper does not provide a direct comparison between α-BANZ(0.1) and α-BANZ(0.5) in the main node-removal experiments, making it unclear how much of the reported advantage comes from the tuned α versus the choice of semivalue itself. The LDS counterfactual experiment (Fig. 6b) partially addresses α sensitivity, but only on a single dataset (CoraML). Reporting α sensitivity on at least one additional dataset would substantially strengthen the claim.

- **DM omitted on large graphs without discussion of the empirical implications**: The paper states (line 109) "We omit DM on some of the large datasets due to memory issues." Since DM is one of the two top-performing methods, its absence on CoPhysics, Photo, and Computers weakens the claim of consistent superiority. The paper does not discuss whether this scalability limitation is fundamental or could be addressed (e.g., via subsampling or approximate datamodels), and does not qualify the conclusion that "DM and α-BANZ show consistently strong results" in light of DM's incomplete coverage.

- **Transferability shown only for α-BANZ, not DM**: Fig. 8 demonstrates that α-BANZ values transfer across architectures, but DM — one of the two best methods — is absent from this analysis. Since transferability is claimed to "suggest that the data values capture intrinsic properties of the data, rather than properties of the model," showing this for DM would significantly strengthen that claim.

- **Brittleness analysis is a self-consistency metric, not independent validation**: The "ensemble guess" is defined as the tightest upper bound among the compared methods (line 116). Showing that DM and α-BANZ are closest to this bound confirms internal consistency, not correctness against ground truth (which the paper acknowledges is intractable). However, the wording risks overinterpretation — an independent check (e.g., manually removing the predicted support for selected nodes and verifying that predictions flip) would elevate this analysis. The paper should explicitly frame this as a consistency check.

- **Poisoning detection improvement over PCWP is modest with overlapping error bars**: In Fig. 7, DM and α-BANZ lead at the top-10% rank but the advantage over PCWP is approximately 10 percentage points, and the reported error bars (shown but not discussed) suggest some differences may not be statistically significant. The absence of any statistical significance commentary weakens the poisoning claim.

- **Hyperparameter disclosure for PCWP is incomplete**: The paper states PCWP truncation ratios were "optimized" but does not specify whether this was done per dataset or globally (line 107 states "We optimize these ratios to obtain PCWP that performs slightly better (see §E.3)" — but §E is in the appendix stripped by parsing). If optimized per dataset, this creates an asymmetric comparison where PCWP gets dataset-specific tuning while α-BANZ uses a fixed α=0.1 across all datasets.

### Trivial
- **Fig. 3 caption omits signal variant**: The paper states the default (learning signal, all setting) on line 103, but the Fig. 3 caption itself does not restate this, making the figure slightly less self-contained.

## Nice-to-Haves
- **Per-method compute cost comparison**: The paper reports 2500+ total compute hours but does not break this down per method. A comparison of the cost-benefit tradeoff (e.g., subsets evaluated per method, retraining costs, per-method wall time) would help practitioners choose between methods.
- **Discussion of the confounding effect of graph structure removal**: When a node is removed, its incident edges are also removed, which affects the utility of remaining nodes in ways not captured by standard marginal contribution logic. The paper briefly mentions this in §4 ("the value of a node as the contribution of these two components") but does not discuss whether any method can or should disentangle feature influence from structural influence.
- **DM approximate evaluation on large graphs**: Even an approximate linear datamodel (e.g., using a subset of nodes as features) on one large dataset would clarify whether DM's effectiveness is limited to small graphs — an important practical question the paper leaves open.

## Removed Points

*These points were identified by reviewers but are removed from the main weaknesses for the reasons stated below.*

- **α-BANZ weighting scheme deferred to appendix §B**: REMOVED per explicit instructions — the parser strips appendix sections from all papers; they exist in the original submission.
- **LDS held-out subsets share same α as training subsets as a confound**: REMOVED — the paper already addresses this via the counterfactual experiment (Fig. 6b) that varies the held-out α. The critic even acknowledges this experiment.
- **"Learning vs. overall signal conflation in figures" framed as a replication concern**: REMOVED — the paper clearly states on line 103 that "Unless specified otherwise, the presented results are in the *all* setting and the *learning signal* variant." This is a clear default and not a confusion.
- **General comments about missing related work**: REMOVED per instructions — I cannot verify the completeness of related work coverage without external sources.
- **Formatting/style nitpicks and generic scope concerns**: REMOVED per instructions.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a novel observation about the paper's content that the paper itself does not already articulate.

## Suggestions

1. **Add α-BANZ sensitivity analysis**: Include a comparison of α-BANZ(0.1) vs. standard BANZ(α=0.5) on at least one additional dataset (e.g., Citeseer or PubMed) in the node-removal experiment to show whether the tuned α or the semivalue choice drives performance.
2. **Frame the brittleness analysis unambiguously as a consistency metric**: Explicitly state that the ensemble guess is the tightest *upper bound among the methods* and that this reflects agreement rather than ground truth. Consider adding a small validation experiment on a few nodes where the predicted support is manually removed.
3. **Complete DM results on at least one large dataset**, or add a sentence explicitly qualifying the limitation: "DM's effectiveness on graphs larger than ~X nodes remains an open question due to memory constraints."
4. **Add DM results to the transferability experiment (Fig. 8)** if feasible, or explicitly note its absence.
5. **State whether PCWP truncation ratios were tuned per dataset or globally**, and if per-dataset, discuss whether this creates an asymmetric comparison with methods using fixed hyperparameters.
6. **Add brief statistical significance commentary** for the key comparisons (e.g., node-removal curves, poisoning detection), noting that overlapping error bars at many points suggest some differences may not be significant.
