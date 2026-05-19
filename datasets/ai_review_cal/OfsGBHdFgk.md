- Decision: Reject
- Avg Score: 3.80
- Scores: 3, 3, 3, 5, 5
Now I have all the evidence I need. Let me produce the consolidated review.

## Summary

This paper proposes ISCA, an improved variant of SCAFFOLD for distributed/federated learning, and its compressed counterpart ISCAM. The two key algorithmic modifications are: (1) updating the local control variable at every inner step rather than keeping it fixed, and (2) computing the uploaded control variable using the most recent local model rather than the initial one. The paper provides convergence analyses for both algorithms under standard assumptions (L-smoothness, bounded gradient noise). ISCAM's theoretical rate improves the dependence on the client participation ratio from $(N/S)^{1/2}$ to $(N/S)^{1/3}$ in the $\sigma\to0$ regime, a genuine theoretical advance over prior compressed FL methods.

## Strengths

- **Clear, well-motivated algorithmic fix.** The paper identifies two specific, concrete deficiencies in SCAFFOLD (fixed local control variable during inner loops; control variable computed from a stale model) and proposes targeted modifications (Lines 9 and 12–13 of Algorithm 1). The design rationale is transparent and reproducible.

- **Theoretical convergence guarantee without bounded-heterogeneity assumptions.** Theorem 1 provides the rate $\sqrt{\frac{LR\sigma^2}{SKT}} + \frac{LR}{T}\big(\frac{N}{S}\big)^{2/3}$ requiring only L-smoothness and bounded gradient noise (Assumptions 1–2). No additional bounded-heterogeneity assumption is needed, matching the best-known rate for SCAFFOLD.

- **ISCAM achieves a genuine theoretical improvement in communication complexity.** Theorem 2 gives a rate with $(N/S)^{1/3}$ dependence in the $\sigma\to0$ regime, strictly better than SCALLION's $(N/S)^{1/2}$ (Table 2). This is a verifiable theoretical improvement over prior compressed FL methods for non-IID settings, and the compression-error argument (compressing the increment $\Delta_i^t$ rather than $v_i^{t,K+1}$ directly) is well-reasoned.

- **Experimental evidence is suggestive of the claimed consistency.** The test-accuracy curves (Figures 1–3) qualitatively show ISCA/ISCAM achieving more similar performance between IID and non-IID settings than SCAFFOLD, and often converging faster than baselines. This provides initial evidence for the paper's core practical claim.

## Weaknesses

### Major

- **Experimental evaluation is too weak to convincingly support the paper's central practical claim.** The paper's core narrative — that ISCA bridges the theory-practice gap of SCAFFOLD by achieving consistent performance across homogeneous and heterogeneous settings — rests on an empirical demonstration that lacks quantitative rigor. Specifically:
  - No numeric final accuracy values are reported; results are shown only as learning curves without error bars, standard deviations, or any measure of variance across runs.
  - No ablation study is conducted to isolate the contribution of each of the two proposed modifications. Given that the differences from SCAFFOLD are precisely two identifiable changes, an ablation is a natural and necessary experiment.
  - Only two simple datasets (MNIST, Fashion MNIST) and one small fully-connected network are used. The heterogeneity split is mild (2 shards per client), and no experiment on more complex tasks (CIFAR, language modeling) or architectures (CNNs, ResNets) is provided.
  - The claim "converges faster" is not substantiated with quantitative measures such as communication rounds to a target accuracy or wall-clock time.

  Because the theoretical rates do not differentiate ISCA from SCAFFOLD (both are $\mathcal{O}$-equivalent), the entire weight of the paper's main contribution falls on the empirical validation. In its current form, that validation is insufficient to support the claim.

- **The theoretical analysis does not explain why ISCA should outperform SCAFFOLD in practice.** The convergence rates of ISCA and SCAFFOLD are identical in order (Table 1). The paper offers only intuitive reasoning (Section 3.2) for why the modifications matter but provides no refined theoretical comparison — e.g., analyzing the constants, showing a smaller variance term in the finite-time regime, or proving that convergence of the control variables is more accurate. This creates a coherence problem: a practitioner reading the paper cannot tell whether the observed empirical improvement is a robust phenomenon predicted by the theory or a happenstance of the specific experimental configuration.

### Minor

- **The initialization $u_i^0 = \nabla f_i(x^0)$ requires a full-gradient computation on each client's local dataset.** Algorithm 1 (Line 1) specifies this initialization, but the paper does not discuss its practical cost. For clients with large local datasets, a full pass over all local data could be expensive. It is not discussed whether alternative initializations (e.g., zero) would affect convergence.

- **The specific tuned hyperparameter values per baseline are not reported.** The paper states that learning rates were tuned over a grid $\{0.01, 0.05, 0.1, 0.5, 1, 3, 5, 10\}^2$ and gives $\beta_1=\beta_2=0.1$ for ISCAM, but does not report the actual selected $(\alpha_{\mathrm{in}}, \alpha_{\mathrm{out}})$ values for each method. This harms reproducibility.

### Trivial

- No explicit limitations or future work discussion is included in the paper. Adding a brief limitations paragraph would improve completeness.

- Algorithm 1's Line 1 notation says "v^0 ← ∇f(x^0)" — computing the full global gradient at initialization requires server-side aggregation of per-client full gradients, an implementation detail not discussed.

## Nice-to-Haves

- Comparing against a broader set of heterogeneity-mitigation baselines (e.g., FedProx, FedNova) would strengthen the empirical positioning, though the paper's focus on SCAFFOLD is defensible.
- Additional datasets (CIFAR-10, a simple NLP task) and architectures (CNNs) would improve the generalizability of the empirical claims.
- Reporting training loss or gradient norm convergence would connect the experiments more directly to the theoretical analysis.

## Removed Points

These points from the source reviews are flagged to be removed; treat them with caution:

1. **"Paper does not cite previous work that tried similar ideas"** — Removed per instructions: cannot verify missing related works without external sources.
2. **"Table 1 formatting appears garbled"** — Removed: parser artifact, not an author error.
3. **"Claim about 'ancient local model' is not quantified"** — Removed: the paper does quantify this in Section 3.2 (lines 133–137), explaining it refers to the initial model $x^t$ rather than the most recent $y_i^{t,K}$.
4. **"Paper does not discuss whether the compression trick could be applied to SCAFFOLD or SCALLION"** — Removed: speculative and outside the paper's scope.
5. **"The paper does not report the number of communication rounds"** — Removed: the x-axes of Figures 1–3 are labeled "Communication Rounds" and show the range, so this information is present.
6. Several generic strengths from the Strength Finder (e.g., "this paper addressed an important problem") — Removed as generic/superficial or because they conflict with verified weaknesses.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add quantitative rigor to the experiments**: report final test accuracy (mean ± std over at least 3–5 seeds) in a table, and show the accuracy gap between IID and non-IID settings for each method.
2. **Include an ablation study** that toggles the two modifications independently on top of SCAFFOLD to verify each contributes to the improved consistency.
3. **Provide the specific tuned hyperparameter values** selected for each baseline in the reported grid search.
4. **Acknowledge the full-gradient initialization cost** and discuss whether practical alternatives (e.g., zero initialization) work.
5. **Add a limitations paragraph** explicitly discussing the scope and potential costs of the proposed methods.
6. Consider connecting the theory and experiments more directly by plotting gradient norm convergence or by providing a refined theoretical result (e.g., bounding constants or control-variable accuracy) that predicts the observed improvement.
