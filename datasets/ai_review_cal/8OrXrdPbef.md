- Decision: Reject
- Avg Score: 4.25
- Scores: 5, 1, 6, 5
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

FLAG proposes a clustered federated learning algorithm that combines both data similarity (via principal angles of class-wise SVD vectors) and gradient similarity (via cosine angles between client updates) into a single proximity matrix for agglomerative hierarchical clustering. The paper introduces a weighted class-wise similarity metric to handle quantity shift, an automatic cluster-number search via a threshold sweep on a validation set, and one-shot clustering before training begins. Experiments on four benchmarks (CIFAR-10, FMNIST, SVHN, CIFAR-100) under label skew combined with quantity shift show improvements over several baselines.

## Strengths

- **Ablation study validates the core claim**: Table 4 (Section 5.3) directly compares the combined G+D variant against data-only (D) and gradient-only (G) similarity, and the paper reports that combining both outperforms either alone across all four datasets. This is the paper's central algorithmic hypothesis, and the evidence for it is direct.

- **Consistent improvements across multiple datasets and heterogeneity levels**: FLAG achieves the highest reported accuracy across 16 configurations (4 datasets × 2 skew levels × 2 quantity-shift levels) in Tables 2 and 3, with some margins being substantial (e.g., the paper reports SVHN 30% skew, low quantity shift: FLAG 83.8% vs. next best PACFL 77.7%). This breadth of evaluation within the label-skew+quantity-shift setting is a genuine strength.

- **One-shot clustering reduces communication overhead**: Algorithm 1 performs clustering only at round \(t=0\). Figure 2 shows FLAG converging within 20–30 rounds across all datasets, faster than all baselines. This directly addresses a practical limitation of iterative clustering approaches (e.g., IFCA).

- **Principled handling of quantity shift**: The weighted class-wise similarity metric (Eqs. 4–6) uses a logarithmic ratio weight to penalize large differences in class frequency between clients, and the paper validates this under high quantity shift (\(\alpha'=0.25\)) where FLAG maintains its advantage.

- **Communication-efficient data sharing**: Section 4.1 specifies that each client sends principal vectors comprising less than 1% of its class data, keeping the one-shot data-exchange overhead low.

## Weaknesses

### Fatal
None.

### Major

1. **Evaluation scope does not match the claimed breadth of contribution.**  
   The Introduction (Section 1) motivates the method by listing five types of data heterogeneity — class/label skew, feature skew, quantity shift, concept drift, concept shift — and explicitly criticizes prior work (limitation 4) for only testing on one or two types. The Conclusion states that FLAG "addresses a broader range of data heterogeneity issues." Yet the experiments (Section 5) evaluate **only** label skew + quantity shift. Feature skew, concept drift, and concept shift are never tested. This gap between the scope of the claims and the scope of the evidence is significant enough to undermine the "broader range" narrative. The paper's contributions would be better served by either (a) narrowing the claims or (b) including even a small-scale experiment on an additional skew type.

2. **No statistical significance or variance reported.**  
   Every table and figure presents single numbers without error bars, standard deviations, or any mention of multiple runs. Federated learning experiments involve randomness from client sampling, data partitioning, initialization, and the threshold search itself. Some FLAG margins are modest (e.g., Table 2: FLAG 60.26 vs. PACFL 58.25 on CIFAR-10 with 20% skew, \(\alpha'=1\)). Without variance estimates, it is impossible to assess whether these differences are meaningful or noise. This is a fundamental evidential weakness for any experimental ML paper.

### Minor

1. **Missing experimental details affecting reproducibility.**  
   (a) The "lightweight model with simple architecture" used in Algorithm 3's threshold search (Section 4.2, line 131) is never specified — its architecture, depth, and parameter count are absent.  
   (b) The hyperparameter \(\delta\) (Eq. 5) controls how strongly quantity shift penalizes dissimilarity but its value is never stated or justified.  
   (c) The paper does not state what value of \(K\) (number of clusters) was given to the IFCA baseline, which is a critical detail since IFCA requires \(K\) as input and the paper criticizes this very limitation. If IFCA was given the ground-truth cluster count, the comparison is informative; if not, IFCA is disadvantaged.

2. **Limited assessment of the threshold search robustness.**  
   Algorithm 3 selects the clustering threshold \(\alpha\) via an elbow method on validation accuracy curves (Figure 1). The paper shows only one set of curves per dataset without testing robustness across different random seeds, client subsets, or data partitions. The elbow method can be ambiguous, and the paper provides no evidence that the selected \(\alpha\) is consistently optimal.

3. **The clustering overhead is not accounted for in convergence comparisons.**  
   Figure 2 compares communication rounds without factoring in the initial clustering phase (SVD computation on all clients + gradient computation for similarity + the 5-round lightweight evaluation). This phase involves all 100 clients (unlike the \(R=20\%\) sampling in later rounds) and incurs non-negligible cost. A fair comparison would either amortize or quantify this overhead.

### Trivial

- The \(\beta\) combination ratio is set to 0.5 via grid search (Section 5, setup paragraph), but no sensitivity analysis around this value is provided. A brief ablation varying \(\beta\) (e.g., {0.25, 0.5, 0.75}) would strengthen the claims about robustness.

## Nice-to-Haves

- An experiment on feature skew (e.g., rotating images on subsets of clients) or concept shift would substantially bridge the gap between the paper's broad motivation and its current evaluation.
- The paper could explicitly state that the standard benchmark test sets (CIFAR-10, etc.) are completely disjoint from the validation sets used in Algorithm 3, to preempt concerns about test-set overfitting.
- Reporting the total communication cost of the clustering phase (SVD upload + gradient upload + lightweight-model rounds) and adding it to the convergence plots would make the efficiency comparison more precise.

## Removed Points

The following points from the original reviews were removed with justification:

- **"Overfitting to the test set via threshold search" (Harsh Critic, Critical Issue 3, first half)**: Removed. The paper uses 10% of local training data from 30 clients as a validation set for \(\alpha\) selection (Algorithm 3, lines 227–235). Test accuracy is evaluated on standard benchmark test sets (CIFAR-10, FMNIST, SVHN, CIFAR-100), which are completely separate from any training/validation data. This is standard ML practice, not overfitting. The retained minor point about the "lightweight model" being unspecified is a separate, valid reproducibility concern.

- **"Privacy discussion missing"**: Removed as scope creep. The paper does not claim privacy guarantees as a contribution; it focuses on clustering accuracy and communication efficiency.

- **"No comparison with Zhang et al. (2024) or Kim et al. (2024)"**: Removed. The paper already compares against FedAvg, FedProx, PerFedAvg, PACFL, IFCA, CFL, and FedSoft — a substantial set of baselines. Requiring every method cited in the literature review to also appear as a baseline is not a reasonable standard.

- **"FedSoft sometimes competitive, not discussed" (from Section-by-Section Notes)**: Removed. The paper reports the full table and lets the numbers speak. Selective commentary on individual competitor wins is not a structural weakness.

- **Generic "could the metric be measuring a proxy?" / "are confounders controlled?" style speculation**: Removed per the filtering discipline (these had no concrete anchor in the paper).

- **"Strength: FLAG achieves highest accuracy in all 16 configurations"** from Strength Finder: **Refined**. This is factually supported by the paper's text and tables (the paper claims it achieves the highest accuracy across all configurations). Kept as a legitimate strength.

- **Strength Finder's claim about specific numbers from Table 4 (68.3% vs 57.9% etc.)**: I cannot verify exact image-bound numbers, but the paper's text states the combination "significantly improves accuracy." The strength is kept as a general claim supported by the paper's narrative.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no unexpected connections or cross-disciplinary insights that the paper itself does not contain.

## Suggestions

1. **Narrow the scope claims** to match the evaluation: "label skew with quantity shift" rather than "a broader range of data heterogeneity." Alternatively, add experiments on at least one additional skew type (e.g., feature skew via image rotation, or concept drift via different label mappings across clients).

2. **Report means and standard deviations** over at least 5 random seeds for all main tables and figures.

3. **Disclose missing experimental details**: the lightweight model architecture, the value of \(\delta\), and the \(K\) value used for IFCA.

4. **Add a \(\beta\)-sensitivity analysis** (e.g., ablation over \(\beta \in \{0.25, 0.5, 0.75\}\)) to show that the 0.5 default is not critical.

5. **Quantify the clustering overhead** and include it in the communication cost analysis.

---
