## Summary

This paper proposes G-Init, a weight initialization method for GNNs that extends He et al. (2015)'s Kaiming initialization by incorporating node degrees into the variance analysis. The method derives a standard deviation of $\sqrt{4/n_l}$ (vs. Kaiming's $\sqrt{2/n_l}$) and argues via the circular law and Oono & Suzuki's oversmoothing theory that larger initial singular values slow representation collapse. Experiments on GCN across 8 datasets with depths up to 64 layers show accuracy improvements over Xavier and Kaiming initializations.

---

## Strengths

- **First attempt to derive a GNN-specific initialization from a variance-preserving framework**: The paper identifies a genuine gap — existing initializations (Xavier, Kaiming) are designed for FFNs/CNNs and ignore graph topology. The forward-propagation derivation (Section 3.1) introduces the neighborhood average term $x_l^{(i)'} = \frac{1}{d_i}\sum_{j\in\hat{N}(i)}x_l^{(j)T}$, which is structurally novel compared to prior initialization work. This provides a principled starting point for GNN-specific initialization.

- **Theoretical connection between initialization variance and oversmoothing rate**: Using the circular law (Theorem 2), the paper shows that G-Init's weight matrices have eigenvalues on a disk of radius $\sqrt{2d_i}$ vs. Kaiming's $\sqrt{2}$. Via Theorem 1 (Oono & Suzuki), where the distance to the oversmoothing subspace is $O((s\lambda)^l)$, larger initial singular values from G-Init plausibly slow convergence to the oversmoothing subspace. No prior weight initialization work (Jaiswal et al. 2022; Han et al. 2023; Li et al. 2023) establishes this explicit link between initialization and oversmoothing dynamics.

- **Oversmoothing reduction without architectural modifications**: Unlike methods such as JK-Net, APPNP, GCNII, or DropEdge (Section 5), G-Init reduces oversmoothing purely through weight initialization, without skip connections, residuals, or edge dropping. This makes it complementary to those approaches.

- **Broad evaluation across datasets and depths**: Experiments span 8 datasets (Cora, CiteSeer, Pubmed, Arxiv, Photo, Computers, Physics, CS) with depths from 2 to 64 layers — substantially broader than typical 2–4 layer GCN evaluations. The scale provides evidence that G-Init enables deeper architectures without performance collapse.

---

## Weaknesses

### Major

- **The theoretical derivation relies on an inequality (CBS), not exact variance preservation**: The paper uses the Cauchy–Bunyakovsky–Schwarz inequality to handle the neighborhood averaging term, which produces an **upper bound** on the variance (line 96, line 148), not an exact expression like Kaiming's derivation. This means G-Init's variance choice does not guarantee signal variance stabilization — it only bounds it from above. The paper acknowledges this ("Inequality 7 provides an upper bound," line 148) but still presents G-Init as a "generalization" of Kaiming initialization. The resulting formula $\sqrt{4/n_l}$ is a well-motivated heuristic, not a principled variance-preserving condition in the sense of He et al. (2015). This gap between claimed rigor and actual derivation weakens the paper's central theoretical contribution.

- **Experiments test only GCN**: Despite claiming G-Init is a general GNN initialization method, all experiments use GCN exclusively (line 135: "We experiment with the proposed architecture of GCN"). No other architectures (GAT, GraphSAGE, GIN, GCNII, etc.) are evaluated. Since the oversmoothing dynamics referenced (Oono & Suzuki) and the message-passing schemes vary across architectures, it is entirely unknown whether G-Init's benefits transfer beyond GCN.

- **Only compared against generic initializations (Xavier, Kaiming), not GNN-specific methods**: The related work section (line 171) cites three GNN-specific initialization methods — Jaiswal et al. (2022), Han et al. (2023), and Li et al. (2023). None are included as experimental baselines. If the contribution is a better initialization for GNNs, the relevant comparison is against other GNN-specific methods, not just the generic ones. The paper's experimental results therefore cannot support the claim that G-Init advances the state of the art in GNN initialization.

- **Oversmoothing reduction is claimed but never directly measured**: The paper repeatedly asserts that G-Init "reduces oversmoothing" (abstract, lines 154, 192) but provides only classification accuracy as evidence. Accuracy is a confounded proxy — it reflects optimization quality, training stability, and generalization, not just oversmoothing. The paper directly cites Oono & Suzuki's Theorem 1, which characterizes oversmoothing via the distance $d_M(X^{(l)})$ to a subspace $M$. Direct measurement of this distance, or any representation-collapse metric (e.g., average cosine similarity between node pairs, rank of the representation matrix), would be straightforward to compute and would directly validate the central claim. Its absence is a significant gap.

### Minor

- **The method's "topology awareness" is coarse**: The derivation reduces to using the minimum node degree (after self-loops $d_i=2$, line 146), which is effectively a constant for most graphs. For the Arxiv dataset, the paper tunes $d_i$ to 1.6 (line 146), showing the parameter is dataset-dependent and not purely derived from topology. Calling the method topology-aware is overclaimed — it uses a single scalar per graph (the min degree) rather than genuinely integrating per-node degree structure.

- **The 80/20 mixed initialization strategy undermines the theoretical narrative**: Using G-Init for the first 80% of layers and Xavier for the remaining 20% yields better results than pure G-Init (line 148). The paper attributes this to the "uncontrollable term $k_l^{(i)}$" in Inequality 7 — a hand-wavy explanation. If G-Init is the correct initialization derived from variance analysis, reverting to a different initialization in later layers should not be necessary. This raises doubts about whether the theory actually captures what drives performance.

- **The circular law argument has loose logical connections**: The paper uses the circular law (Theorem 2) — which describes the asymptotic *eigenvalue* distribution of random matrices — to make claims about the largest *singular value* (which Theorem 1 uses). The bridge relies on the inequality $s_1 \geq \max|a_{ij}|$ (line 160), which is correct but gives only a weak bound. Moreover, the weight matrices are $128\times 128$, modest for an asymptotic law. The paper also acknowledges that training changes singular values (lines 156, 162), so the analysis applies only at initialization. The argument is suggestive but not conclusive, and the paper overstates the connection.

- **The analysis uses row-normalized adjacency but experiments use symmetric normalization**: The theoretical derivation (line 76) uses $\hat{A} = \hat{D}^{-1}(A+I)$ for mathematical convenience, claiming it "yields the same analysis." However, the experiments (line 41) use the standard GCN symmetric normalization $\hat{D}^{-1/2}(A+I)\hat{D}^{-1/2}$, which has different spectral properties and different oversmoothing dynamics. The paper provides no justification that the analysis transfers between these normalizations.

- **Non-square weight matrices not addressed**: The derivation assumes $n_l \times n_l$ weight matrices (line 109). GCNs commonly have varying input/output dimensions (e.g., input features → 128 hidden → number of classes). The paper does not discuss how G-Init applies to these cases.

- **$d_i$ introduces a tunable hyperparameter**: The default $d_i=2$ works for most datasets, but Arxiv requires $d_i=1.6$ (line 146). This means the method introduces a dataset-dependent hyperparameter without clear guidance on how to set it without a validation search. The paper acknowledges this as future work (line 192), but it is a practical limitation.

### Trivial

None.

---

## Nice-to-Haves

- **Direct comparison against oversmoothing-mitigation methods** (JK-Net, APPNP, GCNII, DropEdge) is not a core flaw since G-Init is positioned as complementary (line 173: "without changing any of the properties of the network or the graph"), but a head-to-head comparison would strengthen the claim that initialization alone can compete with architectural approaches.
- **Statistical significance** of accuracy improvements is not discussed beyond reporting standard deviations.

---

## Removed Points

These points were flagged in the source reviews but are removed under the filtering rules. Treat with caution:

- **Missing implementation details** (optimizer type, weight decay, dropout, learning rate schedule): Removed per the rule against nitpicks about undisclosed hyperparameters.
- **"No quantitative evidence that standard initializations underperform in GNNs"** (framing criticism): This is a general motivation concern without a specific anchor in the paper's methodology.
- **Strength Finder's "empirically validated hybrid initialization strategy"**: This conflicts with the verified weakness that the 80/20 mix undermines the theory. Per rule, the weakness wins.
- **"Could the metric be measuring a proxy?" (speculative)**: The oversmoothing measurement concern is kept (and strengthened) as a verified weakness since the paper does not directly measure it — the removed framing is the purely speculative "what if" form.
- **Comparison against oversmoothing-mitigation methods as a required baseline**: Moved to nice-to-have since the paper explicitly scopes itself as complementary (line 173).

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Directly measure oversmoothing** using the distance metric $d_M(X^{(l)})$ from Oono & Suzuki (which the paper already cites) or average node representation similarity across layers. This would directly validate the central claim without relying on accuracy as a proxy.
2. **Test on at least one additional GNN architecture** (e.g., GAT or GraphSAGE) to demonstrate generality beyond GCN.
3. **Include at least one GNN-specific initialization baseline** (Jaiswal et al. 2022, Han et al. 2023, or Li et al. 2023) to establish that G-Init advances the state of the art.
4. **Either justify the 80/20 mixed strategy theoretically or drop it** from the main results, as it currently weakens the coherence of the proposal.
5. **Justify the row-normalized analysis → symmetric-normalized experiments gap**, or re-derive the analysis for the symmetric normalization actually used.
6. **Provide guidance for practitioners** on how to set $d_i$ without per-dataset validation, or show that performance is robust across a wide range of values.
7. **Discuss applicability to non-square weight matrices**, which occur in input and output layers of any practical GCN.

---

## Score and Decision

This paper identifies a legitimate gap (no principled, topology-aware weight initialization for GNNs) and makes a reasonable first attempt. The experimental results show consistent accuracy improvements over generic baselines across many datasets and depths, suggesting the method has practical value. However, the theoretical derivation relies on an inequality rather than exact variance preservation (making it a heuristic rather than a principled generalization), the experiments test only GCN and only against generic initializations, and the central claim of oversmoothing reduction is never directly verified. For a top conference, these gaps are too substantial to overlook.

MY FINAL SCORE: <score>4</score>
MY FINAL DECISION: <decision>Reject</decision>