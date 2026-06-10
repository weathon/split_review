## Summary

CGNN proposes incorporating commute time (from Markov chain theory) into message passing on directed graphs. The paper's core contributions are: (1) DiLap, a new digraph Laplacian defined as the divergence of the gradient on digraphs; (2) a theoretical connection (Lemma 1, Theorem 2) linking DiLap to the fundamental matrix, enabling commute time computation via a sparse pseudoinverse rather than dense matrix inversion; (3) a similarity-based graph rewiring to ensure irreducibility/aperiodicity while preserving sparsity; and (4) the CGNN architecture that weights neighbor contributions by commute-time proximity.

## Strengths

1. **Principled theoretical connection between a digraph Laplacian and commute times.** Lemma 1 (Eq. 155-157) and Theorem 2 (Eq. 164-171) formally prove that the fundamental matrix Z — and hence hitting/commute times — can be expressed through the Weighted DiLap $\widetilde{\mathcal{T}} = \widetilde{\mathbf{\Pi}}(\widetilde{\mathbf{D}}^{-1}-\widetilde{\mathbf{P}})$. This is a genuine theoretical contribution: it establishes a provable relationship that grounds random-walk distances in a Laplacian operator, rather than relying on heuristics.

2. **Efficient commute time computation avoiding dense matrix inversion.** The paper reduces commute time computation from O(N³) (inverting a dense matrix via Theorem 1) to O(q|E|) using randomized truncated SVD on the sparse matrix R (Section 5.3). With q=5 in practice, this makes commute-time-aware message passing feasible on large sparse digraphs.

3. **Sparsity-preserving graph rewiring with empirical fidelity check.** Unlike the PageRank-based approach (which creates a dense complete graph), the proposed rewiring adds at most two undirected edges per node. The paper quantifies the effect on commute times (δ ≤ 0.063 across three datasets, Table 5) and shows the PPR variant is both less accurate and slower (Table 4), providing clear evidence that the sparsity-preserving approach is superior.

4. **Honest scope analysis acknowledging limitations.** Section 6.3 explicitly analyzes datasets where CGNN underperforms (CoraML, Snap-Patents) and explains why: citation networks lack mutual path dependencies, making commute time weighting inappropriate. This nuanced assessment strengthens credibility.

5. **Ablation isolating the role of directionality.** The CGNN vs. CGNN$_{\mathrm{sym}}$ comparison (Table 6) shows symmetrizing edges causes substantial accuracy drops (e.g., 77.61→71.31 on Squirrel), demonstrating the directed commute time signal — not just the weighting mechanism — drives the performance gains.

## Weaknesses

### Fatal
None.

### Major

1. **Ambiguous computational pipeline for large graphs undermines the central complexity claim.** The paper claims O(q|E|) complexity (line 218) and reports results on Snap-Patents (2.9M nodes, 14M edges). However, Algorithm 1 (line 208) says "Compute the commute time matrix $\mathcal{C}$ with Eq. (17)" — and Eq. (175-180) defines $\mathcal{C}$ via outer products $(\pi^{-1/2} \otimes \pi^{-1/2})$ and Hadamard products with $\mathcal{R}^\dagger$, operations that produce a dense $N \times N$ matrix. For Snap-Patents, a dense $N \times N$ float matrix would require ~6.7 PB. The paper never explains how the full dense matrix is avoided. A plausible implementation computes only the $O(|E|)$ entries needed for $\widetilde{\mathcal{C}}^{\text{out}}/\widetilde{\mathcal{C}}^{\text{in}}$ directly from the low-rank factors of $\mathcal{R}^\dagger$, but this is not stated. The pseudocode and equations suggest forming $\mathcal{C}$ explicitly, which is incompatible with the reported large-scale results. **The paper must clarify whether the dense matrix is actually formed and, if not, describe the actual pipeline precisely.** This ambiguity affects the credibility of both the complexity analysis and the Snap-Patents experiments.

### Minor

1. **Missing hyperparameters and model configurations.** The experimental section (Section 6) reports no hyperparameters for any model: no learning rate, hidden dimension, number of layers, dropout rate, weight decay, training epochs, or optimizer. This makes independent reproduction of the reported results difficult. Additionally, the paper describes CGNN as "an enhanced version of DirGNN" (line 281) but does not specify the DirGNN variant used (the exact $\mathrm{Agg}_{\text{in}}/\mathrm{Agg}_{\text{out}}$ functions, architecture depth, hidden dimensions for the baseline). Since CGNN uses mean aggregation (line 195), confirming DirGNN used the same architecture choices is important for a fair comparison.

2. **Empirical gains over the closest baseline (DirGNN) are modest and inconsistent.** CGNN outperforms DirGNN by 0.43–3.70 percentage points on most datasets, but on Snap-Patents CGNN is *worse* (72.33 vs. 73.95). On Chameleon, the difference (79.54 vs. 79.11) is well within one standard deviation. The average improvement is roughly 2–3% on datasets where mutual dependencies exist. The abstract's claim of "superior performance" slightly overstates these incremental gains, though the honest scope analysis partially mitigates this.

3. **Rewiring validation is limited in scope.** The $\delta$ metric (commute time change before/after rewiring) is reported for only 3 of 8 datasets (Table 5). Moreover, the "original graph" commute times are computed on the largest connected component with absorbing nodes removed — itself a modified graph. The claim that rewiring "only minimally alter[s] the overall semantics" would be strengthened by reporting $\delta$ on all datasets and verifying that the *relative ordering* of commute times (which determines the weights) is preserved, not just aggregate L2 distances.

4. **No clean ablation isolating the commute time weighting mechanism.** The comparison with DirGNN is the closest substitute, but without confirming identical architectures across all settings, it conflates architecture choice with the commute time signal. An experiment replacing commute time weights with simpler schemes (e.g., uniform, degree-based, attention-based) within the same DirGNN architecture would better isolate the effect.

5. **Disconnect between hitting-time asymmetry as motivation and symmetric commute time as method.** The paper motivates with hitting time asymmetry (celebrity-follower example: $h(v_i, v_j) \neq h(v_j, v_i)$) but uses commute time $c = h(v_i, v_j) + h(v_j, v_i)$, which is symmetric and loses directional information. The direction-specific masks ($\mathbf{A}$ vs. $\mathbf{A}^\top$) recover directionality downstream, but the paper does not bridge this gap. A brief discussion clarifying how the symmetric quantity still captures asymmetric relationships via edge masking would improve conceptual clarity.

### Trivial
None.

## Nice-to-Haves
- A controlled experiment replacing commute time weights with simpler schemes (e.g., attention, PPR proximity) while keeping the DirGNN architecture fixed.
- Reporting $\delta$ for all datasets to strengthen the rewiring validation.
- Statistical significance tests (e.g., paired t-test) for close results (Chameleon, Snap-Patents).
- Per-epoch or total runtime for Snap-Patents to substantiate the efficiency claim on the largest dataset.
- A clearer explanation of how symmetric commute time combined with direction-specific masks recovers the asymmetry the paper motivates.

## Removed Points
- **"Method only reweights existing edges — does not capture non-local mutual dependencies"**: The paper is clear about its scope: $\widetilde{\mathcal{C}}^{\text{out}} = \mathbf{A} \odot \widetilde{\mathcal{C}}$ (Eq. 18) weights only existing edges. This is a reasonable design choice, not a weakness.
- **"DiLap is not justified as the correct generalization of the Laplacian"**: The paper grounds DiLap in the divergence-of-gradient interpretation (Eq. 8-9) and connects it to the fundamental matrix. This is sufficient theoretical justification.
- **"PPR comparison is unfair"**: Table 4 is presented as evidence that the *rewiring approach* is superior to PageRank for making the graph amenable to commute time computation. This is a fair and informative comparison.
- **"Hyperparameter tuning inflates baseline performance"**: The paper reports "the better of" symmetric/asymmetric adjacency for baselines. This is conservative for CGNN and not clearly a flaw.
- **"No statistical tests"**: Merged into Nice-to-Haves; common practice in GNN node classification benchmarks.

## Novel Insights

The critic's observation about the disconnect between the paper's motivation (hitting time asymmetry) and the chosen quantity (symmetric commute time) is genuinely insightful. The paper motivates with $h(v_i, v_j) \neq h(v_j, v_i)$ but uses $c(v_i, v_j) = h(v_i, v_j) + h(v_j, v_i)$, which is symmetric. While the direction-specific masks ($\mathbf{A}$ vs. $\mathbf{A}^\top$) recover directional information downstream, the paper does not explicitly discuss this conceptual gap. If the asymmetry of hitting times is the core motivation, a more natural quantity might preserve the directional information explicitly in the weighting. This is worth the authors' attention.

## Suggestions
1. **Clarify the computational pipeline.** Explicitly state whether $\mathcal{C}$ is materialized as a dense $N \times N$ matrix. If not (as the large-scale results imply), describe how only the $O(|E|)$ needed entries are computed directly from the low-rank factors of $\mathcal{R}^\dagger$, and update Algorithm 1 accordingly.
2. **Report all hyperparameters** (learning rate, hidden dimension, layers, dropout, weight decay, optimizer, epochs) for all models.
3. **Specify the exact DirGNN baseline architecture** used and confirm it matches CGNN's architecture except for the commute time weights.
4. **Extend the rewiring validation** to all datasets and show that the relative ordering of commute times (not just L2 norm) is preserved.
5. **Conduct a cleaner ablation** replacing commute time weights with uniform or attention-based weights within the same architecture to isolate the mechanism.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>