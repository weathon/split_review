## Summary
The paper proposes DTI-DA, a drug-target interaction prediction framework that combines a Graph Attention Network (GAT) for compound encoding, a Knowledge-Aware Network (KAN) for injecting prior relational graphs, and domain adaptation via MMD and adversarial discrimination. The authors introduce a dual-track evaluation protocol (source-only vs. transductive UDA) and report results on BioSNAP and BindingDB, claiming improvements over SVM, RF, GraphDTA, and MolTrans.

## Strengths
- The problem of domain shift in drug-target interaction prediction is practically relevant and timely.
- The explicit separation of evaluation tracks (source-only vs. transductive UDA) with clear leakage safeguards is a sensible methodological choice.
- The ablation study separates the contributions of GAT, KAN, and DA, providing some insight into the components.

## Weaknesses
### Fatal
1. **Contradictory experimental results.** The reported numbers for the same setting are inconsistent across the paper. On BindingDB, the main text states DTI-DA achieves AUC 0.654 (Section 5.1), while the ablation table in Figure 3 lists AUC 0.7452 for the full model on BindingDB – a substantial discrepancy that invalidates the quantitative claims.  
2. **Unreliable comparison due to mismatched baseline numbers.** In Section 5.1, MolTrans AUC is given as 0.7374, yet Figure 2 shows MolTrans AUC at 0.68, making the claimed improvement (+0.895%) internally inconsistent. The paper does not resolve which numbers are correct or under which track they were obtained.

### Major
3. **No statistical support for conclusions.** The paper explicitly states all results are single-run point estimates and no significance tests are provided. Given the tiny improvements (e.g., +0.0066 AUC on BioSNAP), the results could easily be noise. Without variance estimates or multiple runs, the claim of consistent outperformance is unsupported.
4. **Poor clarity of experimental setup.** Figure 2 is ambiguously titled “Results of different models on BioSNAP and BindingDB” but the table underneath shows single values per metric without indicating which dataset or track they correspond to. The relationship between the figure and the text (which gives dataset-specific numbers) is unclear.
5. **KAN construction and dataset-specific results under-specified.** The construction of similarity graphs for KAN and the cluster-based domain splits are described only at a high level, making reproduction difficult. The explanation for why BindingDB results are lower than BioSNAP (higher drift) is post-hoc and not backed by quantitative analysis.

### Minor
6. **Overclaiming relative to modest gains.** The abstract and contributions section frame the approach as outperforming baselines, yet the maximum absolute AUC gain is ~0.06, and on BindingDB the AUC is only 0.654, which is not strong in absolute terms.
7. **Several irrelevant citations (e.g., quantum computing)** appear in the related work section, suggesting padding rather than genuine positioning.

## Nice-to-Haves
- Provide confidence intervals or standard deviations based on multiple random seeds for all reported metrics.
- Clarify the exact dataset split and track for each number in Figure 2 and Figure 3 to resolve the textual inconsistencies.
- Discuss when domain adaptation is most beneficial with quantitative evidence (e.g., measuring domain shift via MMD on held-out sets).

## Novel Insights
None beyond the paper’s own contributions.

## Suggestions
- Fix the contradictory numbers between the main text and figures; ensure all reported values are clearly labeled with the corresponding track (source-only / transductive UDA) and dataset.
- Run each experiment with at least 5 different seeds and report the mean and standard deviation, then check whether the improvement over baselines is statistically significant.
- Provide the code and exact configuration used to generate the cluster-based domain splits so the results can be independently verified.

## Score and Decision
Score: 2.0 (strong reject) – The fatal inconsistencies in the experimental results make the core empirical contribution unreliable. Combined with the lack of statistical rigor and marginal improvements, the paper does not convincingly support its claims.

MY FINAL SCORE: <score>2.0</score>
MY FINAL DECISION: <decision>Reject</decision>