## Summary
This paper proposes GOODRL, an offline-online deep reinforcement learning approach for dynamic workflow scheduling (DWS) in cloud computing. The method features three innovations: (1) a task-specific graph representation with a Graph Attention Actor Network that processes each (task, machine) pair separately to better differentiate actions; (2) a system-oriented graph representation with a Graph Attention Critic Network that models cross-workflow and machine interactions for accurate value estimation; and (3) an offline-online training scheme using imitation learning for pre-training followed by PPO with gradient control and decoupled high-frequency critic updates for online adaptation. Experiments across offline and online DWS scenarios with up to 20,000 workflows report GOODRL achieving an average rank of 1.17 with substantial mean flowtime reductions compared to expert-designed PDRs, GPHH, and a transformer-based DRL baseline.

## Strengths
- **Novel dual-graph representation is well-motivated and clearly designed.** The separation of a task-specific graph (for the actor) and a system-oriented graph (for the critic) is a principled architectural choice. The task-specific graph's pairwise processing and focused embedding are explicitly designed to address the action-differentiation challenge, while the system-oriented graph's bi-directional edges and self-attention target holistic state evaluation. This is a concrete architectural contribution beyond prior work that uses a single shared graph for both networks.

- **Tackles large-scale, highly dynamic DWS problems that are under-explored.** The paper evaluates on scenarios with up to 20,000 dynamically arriving workflows (Poisson arrivals with λ=5.4, 9 per hour), which is substantially larger and more dynamic than the small-scale static settings common in prior GNN-based scheduling work. The problem scale is explicitly noted as a gap in the literature.

- **Consistent top ranking across multiple scenarios with quantified improvements.** The paper provides concrete summary statistics: GOODRL achieves an average rank of 1.17 across 12 offline scenarios and maintains this rank in online settings. Mean flowtime Gap reductions are reported in the text (up to 289.98% over expert-designed PDRs, 1128.92% over ERL-DWS). The paper also honestly reports the two scenarios where GPHH slightly outperforms Ours-Offline (Gaps of 1.24% and 0.15%), which adds credibility.

- **Offline-online training scheme with imitation learning pre-training is a sensible approach.** The use of HEFT as a teacher for imitation learning to avoid the cold-start problem (accumulation of uncompleted tasks from random initialization) is well-justified, and the subsequent online fine-tuning with gradient control is a practical contribution.

## Weaknesses
### Fatal
None.

### Major

- **Ablation studies lack quantitative results (Section 5.4).** The ablations validating the three core technical innovations are described entirely in qualitative terms. The paper states that "Our-TSEM achieved the lowest cross-entropy loss" and "Ours-SOEM significantly outperforms... in value loss" and "Ours-Online achieved superior online performance improvement," but provides **zero numerical values** for cross-entropy loss, value loss, or mean flowtime in the text. Without these numbers, the claimed benefits of pairwise processing, focused embeddings, bi-directional edges, self-attention, gradient control, and decoupled critic updates cannot be independently assessed. This is a significant omission because these ablations are the primary evidence for the paper's specific design innovations.

- **FJSS transferability experiment is insufficiently described.** The transfer to flexible job-shop scheduling is reported in a single sentence claiming "cost savings of up to 41%" with no description of the problem instances, modified reward function, baselines compared, or experimental setup. This experiment is too thin to constitute evidence of generalization and should either be properly documented or removed.

### Minor

- **ERL-DWS baseline comparison is weakened by admitted under-optimization.** The paper states (line 148) that "Despite our best efforts, including adding imitation learning, ERL-DWS showed no significant improvement in test performance. We hence report its best available results." While this transparency is appreciated, it raises the concern that the baseline may not have been properly tuned for this setting. The reported 1128.92% Gap gap may partially reflect suboptimal configuration rather than architectural superiority of GOODRL.

- **Gradient control design choices are asserted without analysis.** The mechanism sets the gradient to zero if its L2 norm exceeds μ_prev+σ_prev or τ_0. This is a non-standard form of clipping that could stall learning. The paper provides no sensitivity analysis of τ_0, no histogram of gradient norms, no comparison to standard gradient clipping, and no discussion of when gradient zeroing might harm rather than help. The ablation claims "superior performance" but without numbers this cannot be evaluated.

- **No variance measures reported in the textual summary.** While the paper mentions using five random seeds (line 141) and the tables (which are parser-inaccessible images) may contain standard deviations, the textual discussion of results reports only means and Gap percentages without any measure of variance. This makes it impossible to judge the statistical significance of the reported improvements.

### Trivial
- The paper references pseudo-code and supplementary details via footnoted references (superscript 1, 2) that appear to point to a stripped appendix; these implementation details are not available in the extracted text.

## Suggestions
1. **Quantify all ablation results.** Provide a table (or detailed textual reporting) with the cross-entropy loss values, value loss numbers, and mean flowtime for each ablated variant (TSEM w/o pair, TSEM w. mean, SOEM w/o. edge, SOEM w/o. self, Online w/o. grad., Online w/o. freq.) alongside the full GOODRL configuration. Without this, the core architectural claims are unverifiable.

2. **Report standard deviations or confidence intervals** for all main results in the text. The use of five random seeds provides the data to compute these.

3. **Either substantially expand the FJSS transfer experiment** (describe problem instances, reward modification, baselines, full results) or remove it entirely.

4. **Add sensitivity analysis for the gradient control mechanism** (e.g., how results vary with τ_0, a comparison to standard gradient clipping/norm scaling) to justify the design.

5. **Provide absolute mean flowtime values** in the text, not just Gap percentages. This would allow readers to understand the scale of the reported improvements.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

## Questions


## Decision
Reject
