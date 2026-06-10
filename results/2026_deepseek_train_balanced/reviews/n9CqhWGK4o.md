## Summary

This paper proposes a graph construction methodology for COVID-19 severity classification from single-cell RNA-seq data. Nodes represent cell types with transcription-factor/target-gene expression features (reduced to 16 dimensions via scVI), and edges carry 107-dimensional pathway-level cell-cell interaction scores from CellChat. The authors compare five off-the-shelf GNN architectures (PNAConv, GENConv, NNConv, GATConv, TransformerConv) on this graph, with GENConv achieving the best performance (80.35% on Discovery, 73.33% on External 1, 58.24% on External 2). The paper also provides UMAP visualizations of learned representations and a diagnostic analysis of age-related dataset shift.

## Strengths

- **Multi-dimensional edge features as a concrete departure from prior single-edge GNNs in this domain.** The paper explicitly distinguishes its approach from prior work (Section 1, line 14: "many existing models predominantly utilize single-edge features (Wang et al., 2021; Ma et al., 2023; Efremova & Teichmann, 2020)"). The use of 107 pathway-level interaction scores as edge features (Section 2.4) is a genuine architectural difference from single-edge GNNs applied to single-cell data.

- **Representation evolution analysis demonstrates message-passing learns class-relevant structure.** Section 3.3 and Figure 1 show that before message passing, only some cell types (e.g., CD14 Monocytes) exhibit ICU-class separation in embedding space, while after GENConv layers and pooling, all cell types converge into more cohesive class clusters. This directly evidences that the multi-edge message-passing mechanism is extracting discriminative signal that was not present in the raw node features alone.

- **Diagnostic analysis of dataset shift turns a negative result into a meaningful finding.** When performance drops on External 2, the paper systematically investigates age distributions (Section 3.4) using Wilcoxon tests, identifying that the non-ICU group in External 2 is ~10 years older on average (p = 1.2e−06). This turns a performance failure into a testable confound finding, going beyond simple metric reporting.

- **Proper patient-level splitting to prevent data leakage.** Section 2.6 (line 80) explicitly assigns samples from the same patient to the same train/validation/test split, a standard but frequently overlooked precaution that strengthens validity.

- **Domain-knowledge-driven node feature selection as an alternative to statistical filtering.** Rather than selecting differentially expressed or highly variable genes, Section 2.3 constructs node features from transcription factors and their target genes sourced from SpatalkDB (1,217 genes). The Discussion (Section 4, line 147) explicitly contrasts this with statistical selection approaches.

## Weaknesses

### Fatal
None.

### Major

- **No non-GNN baselines, so the core premise is untested.** The paper's central motivation is that modeling cell-cell interactions (via a graph with edges) improves COVID-19 severity prediction compared to methods using only intra-cellular features. Yet every model evaluated is a GNN operating on the same graph. There is no comparison against: an MLP on pooled node features, XGBoost on aggregated gene expression, logistic regression, or even a simple majority-class baseline. Without these, we cannot distinguish whether (a) the graph structure genuinely improves predictions, (b) the node features alone are sufficient and the GNN adds no value, or (c) a simpler model would do as well or better. The paper's central claim — that "inter"-cellular properties captured by the graph matter — is left untested. This is the single most critical gap.

- **No ablation studies to attribute performance to specific design choices.** The paper makes several claims about its design decisions (multi-dimensional edge features, TF/target-gene node features, CellChat-based graph connectivity), but none are ablated. A reader cannot tell whether: using 107 edge features helps over a single aggregate interaction score; TF/target-gene node features help over highly variable genes or all detectable genes; the graph edges themselves are necessary (a "graph" with no edges or uniform edge weights would be a minimal control). Since the claimed novelty is precisely in the graph construction and edge feature design, this gap means the paper cannot support attribution to any specific design choice.

### Minor

- **Only aggregate metrics reported; no per-class breakdown.** The paper reports only overall accuracy, weighted F1, and weighted AUPRC (Table 3). For a three-class medical classification task (Healthy, non-ICU, ICU), no confusion matrices or per-class precision/recall are provided. Weighted metrics can obscure poor performance on minority classes — a critical transparency issue for clinical prediction.

- **No statistical significance testing between models.** The paper states GENConv "outperformed by a significant margin" (Section 3.2) but provides no statistical test (e.g., paired bootstrap, McNemar's test) comparing model performances. With only 5 runs per model and overlapping confidence intervals for several comparisons (e.g., on Discovery, GEN at 80.35±2.61% vs. other models described as "comparable"), the significance of performance differences is unclear.

- **No code or data release for reproducibility.** The paper mentions 5 random seeds but provides no code repository or data access information. For a computational biology paper whose contribution is the modeling pipeline, code release is standard practice.

### Trivial

- **Pooling mechanism is briefly described but underspecified.** Section 2.6 mentions pooling methods of "mean, max, or add" selected via hyperparameter tuning, but does not clarify whether this is global pooling over all nodes (standard for graph classification) or some other mechanism. This is the only underdocumented architectural detail.

## Nice-to-Haves

- The paper could report whether the 58.24% accuracy on External 2 exceeds a majority-class baseline or random chance for the class distribution present.
- Explainable AI techniques (mentioned as future work in Section 4) would substantially strengthen the biological interpretation claims.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"GENConv's edge feature mechanism is trivial, undermining the multi-dimensional edge features claim"** — Removed because this attacks an existing architecture (GENConv, Li et al., 2020) that the paper did not design. The paper's contribution is the graph construction, not the GNN mechanism. The underlying concern (need for simpler baselines) is already addressed in the Major weakness about non-GNN baselines.

- **"External 2 results are close to useless / paper's own explanation undermines its claims"** — Removed because the paper's diagnostic analysis in Section 3.4 (age distribution investigation) is a strength, not a weakness. It honestly identifies a confound and turns a negative result into a meaningful finding. The valid concern about missing majority-class baseline is subsumed under the first Major weakness.

- **"Overclaimed novelty: graph construction from ligand-receptor databases is well-established"** — Removed per hard rules on missing related works (cannot verify external claims about what is or is not established without sources). The paper cites CellChat, SpatalkDB, and prior single-edge GNN work. The claim about "multi-dimensional edge features" is specific enough to be defensible. The paper's inflated rhetoric ("groundbreaking") is noted but is a matter of framing, not a factual error.

## Novel Insights

None beyond the paper's own contributions. The reviews identify the same central gap — absent non-GNN baselines and ablations — without adding a new analytical lens beyond what the paper itself reveals.

## Suggestions

1. Add non-GNN baselines as the top priority: an MLP on pooled node features, XGBoost on aggregated gene expression, and a majority-class classifier. This directly tests whether the graph structure adds value.
2. Add ablation studies: (a) single-dimensional vs. 107-dimensional edge features, (b) TF/target-gene node features vs. highly variable genes, (c) the constructed graph vs. a fully connected or edge-free graph.
3. Report confusion matrices and per-class precision/recall for all datasets.
4. Provide statistical significance tests (e.g., paired bootstrap) for cross-model comparisons.
5. Release code and processed data for reproducibility.

## Score and Decision

The paper addresses an interesting biological question with a thoughtfully constructed graph, and it includes good practices (patient-level splitting, external validation, diagnostic analysis of confounds). However, the experimental validation has two critical gaps: the complete absence of non-GNN baselines and the lack of ablation studies. These gaps mean the paper's core claims — that the graph structure and multi-dimensional edge features add predictive value — remain untested. For a top conference, the evidence bar is higher.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>