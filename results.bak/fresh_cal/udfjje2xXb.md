Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper proposes GKAN (Graph Kolmogorov–Arnold Network), a GNN architecture that replaces standard linear transformations with learnable B-spline activation functions on edges, inspired by the recently proposed KAN model. The paper claims improved accuracy across node classification, link prediction, and graph classification benchmarks, alongside inherent interpretability through direct visualization of spline weights.

---

## Strengths

- **Consistent accuracy improvements over compared baselines**: Table 2 shows GKAN outperforming GCN, GAT, and GraphSAGE in 8 out of 9 experimental settings, with gains such as +2.3% on Cora node classification and +4.9% on PROTEINS graph classification. The improvements are demonstrated across three task types (node, edge, graph-level), lending breadth to the empirical evaluation.

- **Novel integration of KAN concepts into GNNs**: While the adaptation is conceptually straightforward (replacing linear transforms with splines), the paper is the first to propose and evaluate this specific combination. The application is timely given the interest in KANs.

- **Transparent discussion of limitations**: Section 4.1 candidly acknowledges memory overhead, the absence of edge features, and the nuance that interpretability degrades with depth. This scientific honesty is commendable and allows readers to assess the approach's trade-offs.

---

## Weaknesses

### Fatal

None. The core idea is valid, and the accuracy results, while on a limited set of baselines, are internally consistent.

### Major

- **Interpretability claim is asserted but not validated**: The abstract states GKAN "inherently provides clear insights into the model's decision-making process, eliminating the need for post-hoc explainability techniques." However, the evidence consists of a single qualitative example (node ID 4 on Cora) comparing normalized spline outputs to GNNExplainer edge masks. No quantitative interpretability metrics are provided (fidelity, sparsity, explanation consistency, perturbation analysis). Without aggregated, statistically grounded evaluation over many nodes or graphs, the interpretability contribution remains unsubstantiated. The Limitations section walks back the claim ("we do not claim that GKAN is interpretable, but that it is more interpretable"), which further dilutes the paper's central differentiator.

- **Dataset statistics are swapped for CiteSeer and PubMed in Table 1**: The table reports CiteSeer with 19,717 nodes and PubMed with 3,327 nodes — these values are reversed relative to the standard Planetoid corpus (CiteSeer ≈ 3,327, PubMed ≈ 19,717). While this is a presentation error (the actual datasets loaded via PyTorch Geometric are correct), it erodes trust in the experimental reporting. The authors must correct this and confirm all splits.

- **No standard deviations reported despite averaging over 100 runs**: The paper states results are averaged over 100 runs (line 371–373) but does not report standard deviations or confidence intervals. Several of GKAN's margins are narrow (e.g., +1.2% on CiteSeer node classification: 69.4 vs. 68.2). Without error bars, the reader cannot assess whether these differences are statistically significant.

### Minor

- **Missing relevant baselines**, especially GIN — which the paper itself cites in the introduction (line 62–65) — is absent from the experiments. For graph classification on MUTAG and PROTEINS, GIN is a standard and strong baseline (reported in the 85–90% range on MUTAG). Its omission weakens the claim that GKAN "outperforms state-of-the-art GNN models."

- **Baseline numbers differ substantially from published results**, likely due to using an 80/10/10 train/validation/test split instead of the standard Planetoid fixed splits. While the within-paper comparison is fair (all methods share the same split), the absolute GCN accuracy of 76.3% on Cora (vs. ~81–82% in the original GCN paper with far less training data) raises the question of whether the baseline implementations are optimal. The paper should justify the non-standard split and verify baseline hyperparameters.

- **Message passing does not use edge-specific information**: The message formula `m_{j→i}^{(l)} = spline(x_j^{(l-1)})` applies the spline to the source node's features alone, not to any edge-specific attributes or a joint function of both endpoints. The claim that GKAN employs "spline-based activation functions on edges" (line 7, 104, 195) is over-stated — the activation is per-source-node, applied before sending messages along edges.

- **Extreme computational cost**: GKAN takes 2.05 seconds per epoch vs. GCN's 0.0016s on Cora — over 1,000× slower. The paper acknowledges this but does not analyze time-to-convergence or total training cost. For any practical application, this trade-off would require substantial accuracy gains beyond what is demonstrated.

### Trivial

- **SiLU formula is incorrect**: Line 154 writes `b(x)=silu(x)=x/(1+e)`. The correct SiLU (Sigmoid Linear Unit) is `x * sigmoid(x) = x / (1 + e^{-x})`. The negative sign in the exponent is missing.

---

## Nice-to-Haves

- A perturbation analysis to validate interpretability: mask edges deemed "important" by spline outputs and measure accuracy drop, compared to GNNExplainer's masks.
- Including GIN and at least one modern baseline (e.g., GCNII) for a more complete comparison.
- Reporting standard deviations for all results.
- Ablation study comparing the double-spline design (spline on message + spline on update) to alternatives with standard activations.

---

## Removed Points

These points from the reviewers were considered but removed for the reasons stated:

1. **"No code release"** (Harsh Critic, point 5): The paper states code will be released upon publication, which is standard practice for double-blind submissions. Removed per hard rule that prohibits questioning the release status of cited entities.

2. **"MUTAG statistics are wrong"** (Harsh Critic, point 3): The paper reports ~17.9 nodes and ~39.6 edges per MUTAG graph. Standard TUDataset MUTAG averages ~17.93 nodes per graph; if edges are counted as directed (each undirected edge twice), ~39.6 is correct. The reviewer's alternative figures (30.3 nodes, 60.8 edges) do not match the standard TUDataset statistics and may reflect a different preprocessing.

3. **Interpretability claim is "internally inconsistent"** (Harsh Critic, point 2): The abstract's phrasing ("inherently provides clear insights... eliminating the need for post-hoc explainability techniques") and the Limitations section ("we do not claim GKAN is interpretable, but that it is more interpretable") are different in strength but not strictly contradictory — the limitation clarifies the scope of the claim. The real issue is insufficient evidence, not contradiction. Re-framed as the Major weakness above.

4. **"Overly long introduction" and "incremental adaptation" style criticisms** (Harsh Critic, section notes): These are subjective judgments of presentation style, not substantive weaknesses.

5. **"Reproducibility concern" about undisclosed details**: The paper provides hyperparameter ranges and optimal values for all tasks. This is sufficient for a conference submission.

---

## Novel Insights

None beyond the paper's own contributions. The two reviews largely agree on the paper's empirical claims (consistent accuracy gains over a small set of baselines) and on the central weakness (interpretability claimed but not quantitatively validated). The key tension — whether the accuracy improvements are real or artifacts of weak baselines — cannot be resolved from the paper as written because of the non-standard splits and missing baselines.

---

## Suggestions

1. **Validate interpretability quantitatively**: At minimum, run a perturbation analysis over many nodes: mask edges with high/low spline weights and measure accuracy drop. Compare to GNNExplainer. Report aggregate metrics (e.g., fidelity, sparsity) averaged over the test set. This is the single most important improvement.

2. **Fix the dataset table and report standard deviations** for all results. Clarify why an 80/10/10 split was chosen over the standard Planetoid fixed splits.

3. **Add GIN as a baseline** for graph classification (MUTAG, PROTEINS) and consider adding one modern baseline (GCNII or GATv2) to substantiate the "state-of-the-art" claim.

4. **Ablate the double-spline design**: Compare full GKAN against a variant that uses a standard activation (e.g., ReLU) for either the message step or the update step to justify the architectural choice.

5. **Acknowledge the message-passing framing more precisely**: Clarify that the spline activation is applied per source node rather than being a truly edge-specific function.

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>