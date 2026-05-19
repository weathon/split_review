- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 8, 5
Now I have all the information. Let me write the consolidated review.

## Summary

This paper introduces Commute Graph Neural Networks (CGNN), which integrates commute-time-based proximity into message passing on directed graphs. The authors propose a novel digraph Laplacian (DiLap) and establish an analytic connection between DiLap and the fundamental matrix of a Markov chain, enabling efficient computation of commute times via sparse randomized SVD. CGNN achieves state-of-the-art accuracy on 6 of 8 directed graph benchmarks, with particular gains on heterophilic graphs.

## Strengths

**1. Novel digraph Laplacian with analytic connection to commute time.** The paper defines DiLap as \(\mathcal{T} = \mathbf{\Pi}(\mathbf{D}^{-1}-\mathbf{P})\) grounded in the divergence of a signal's gradient on digraphs. Lemma 1 proves that the fundamental matrix—and hence commute time—can be expressed via the pseudoinverse of a sparse matrix \(\mathcal{R}\) derived from DiLap. This provides a principled bridge between digraph spectral theory and random-walk distances that prior digraph Laplacians (Chung 2005, Singh 2016, Li 2012) do not directly offer.

**2. Demonstrated effectiveness on heterophilic and large-scale benchmarks.** CGNN achieves state-of-the-art results on 6/8 datasets, with particularly compelling gains on heterophilic graphs (e.g., +2.42% on Squirrel over DirGNN, +4.3% on Roman-Empire over the next best). Figure 3 provides supporting evidence that commute-time proximity aligns more closely with label similarity than raw adjacency does on heterophilic datasets, giving a mechanistic explanation for the improvement.

**3. Honest scope analysis and thorough ablation on directionality.** The paper explicitly identifies when commute time does not help (citation networks like CoraML and Snap-Patents where mutual paths are inherently absent) and provides a clear rationale. The ablation in Table 5 (CGNN vs. CGNN\(_{\mathrm{sym}}\)) confirms that the directed structure of the commute time, not just an undirected version, drives the gains (e.g., 77.20% vs. 71.31% on Squirrel).

**4. Efficient, sparsity-preserving computation in principle.** The paper connects commute time computation to the randomized truncated SVD of a sparse matrix \(\mathcal{R}\), with claimed complexity \(\mathcal{O}(q|E|)\) for \(q=5\) in practice. The overall CGNN complexity is stated as \(\mathcal{O}((Ld^2+q)|E|)\), which is linear in the number of edges—a key enabler for large-scale digraphs where dense inversion (\(\mathcal{O}(N^3)\)) would be prohibitive.

## Weaknesses

### Fatal
None.

### Major

**1. The commute time computation pipeline is ambiguously described, leaving a gap between the pseudocode and the complexity claim.** Algorithm 1 (line 5) states "Compute the commute time matrix \(\mathcal{C}\) with Eq. (ct_matrix)." Equation (ct_matrix) defines \(\mathcal{C}\) via outer products and Hadamard products that, if materialized literally, produce a dense \(N \times N\) matrix—infeasible for Snap-Patents (2.9M nodes). The complexity analysis (\(\mathcal{O}(q|E|)\)) implies that entries are computed only where needed (i.e., for existing edges), but the paper never states this explicitly. A reader must infer the lazy computation strategy from context. This gap does not invalidate the method—the SVD factorization \(\mathcal{R}^\dagger \approx V\Sigma^{-1}U^T\) allows computing \(\mathcal{R}^\dagger_{ij}\) for arbitrary \((i,j)\) in \(\mathcal{O}(q)\) per entry, so the overall cost for edge entries is \(\mathcal{O}(q|E|)\) with \(\mathcal{O}(Nq)\) memory. However, the presentation is ambiguous enough that a careful reader cannot confirm the method works as described without filling in the missing step themselves.

### Minor

**2. The graph rewiring, while empirically effective, lacks a principled justification for why commute times on \(\widetilde{G}\) approximate those on \(G\) for the original edges.** The proposed rewiring (adding a feature-similarity path) makes the graph irreducible and aperiodic, satisfying the theoretical assumptions. The \(\delta\) metric (Table 3) measures the change in commute times on the largest connected component after removing absorbing nodes, yielding small values (0.0016–0.0624). However, \(\delta\) is computed on a subset (LCC of the original graph) where commute times were already defined. For nodes outside this subset, the rewiring changes commute times from undefined to defined—a fundamentally different quantity. The paper's empirical success (CGNN outperforming CGNN\(_{\mathrm{ppr}}\) in both accuracy and speed) suggests the approach is practically sound, but the theoretical motivation for the rewiring's design (single anchor vector, linear ordering) appears heuristic.

**3. The empirical advantage over DirGNN is inconsistently significant and no statistical tests are reported.** On Chameleon, CGNN (79.54±1.82) vs. DirGNN (79.11±2.28) yields a 0.43 percentage-point gap within one standard deviation. On Snap-Patents, CGNN (72.33) is *worse* than DirGNN (73.95). While CGNN clearly beats DirGNN on most other datasets (citepseer: +3.70, AM-Photo: +2.32, Roman-Empire: +1.66, Arxiv-Year: +2.89), the paper does not report any statistical significance test (paired t-test, McNemar) for any pairwise comparison. This would be straightforward with 10 splits and would strengthen the measured claims.

**4. Key hyperparameters and implementation details are absent.** The paper specifies depth \(L\), hidden size \(d'\), and rank \(q=5\) in the complexity analysis, but does not report learning rate, dropout, weight decay, optimizer, or number of epochs for any dataset. This limits reproducibility, especially since the model has multiple interacting components (rewiring, SVD rank, weighting scheme).

### Trivial

**5.** Algorithm 1 refers to "Eq. (r_piv)" for computing \(\mathcal{R}^\dagger\), but this equation label is not defined in the main text (it likely appears in the appendix, which was stripped by the parser). The referenced equation for \(\mathcal{R}\) (line 158) is present, so this is purely a labeling issue.

## Nice-to-Haves

- **Isolate the effect of rewiring from commute-time weights.** Comparing CGNN against a variant that uses the same rewiring but uniform weights (i.e., DirGNN on \(\widetilde{G}\)) would separate the contribution of added edges from the contribution of commute-time weighting.
- **Ablation on SVD rank \(q\).** Running CGNN with \(q \in \{1, 3, 5, 10, 20\}\) would empirically validate the complexity/accuracy trade-off and clarify whether low-rank approximations are sufficient.
- **Evaluate on a reciprocity-based metric.** The paper's scope analysis (citation vs. social networks) could be strengthened by computing dataset-level reciprocity and showing that CGNN's gain correlates with it across the 8 datasets.
- **Compare with PPR-weighted DirGNN.** Since PPR also captures mutual reachability (via teleport), a DirGNN variant with PPR edge weights would help contextualize the specific advantage of commute-time over alternative asymmetric proximity measures.

## Removed Points

These points from the inputs were excluded after verification:

- *"The introduction frames the problem as a limitation of all existing methods, yet DirGNN already separates incoming/outgoing neighbors"* — This misreads the paper. The paper explicitly states (Sec. 4) that DirGNN captures hitting time but not commute time. The criticism conflates "direction-aware aggregation" (which DirGNN does) with "mutual-path-aware weighting" (which DirGNN does not do, and which is CGNN's contribution).

- *"No code is provided"* — This is a reproducibility concern about the paper's own unreleased code, but conference reviews typically do not penalize for code not being in the submission; many venues allow post-acquisition release.

- *"The claim that a 1-layer DirGNN can capture hitting time is not formally justified"* — The paper provides a plausible intuitive argument in Section 4 (consistent with known GNN behavior as random-walk smoothers), not a formal proof. The claim is intended as motivation, not a theorem, and does not affect the core method.

- *"Missing related works"* — Removed per instructions (no external confirmation of omissions).

- *"Pure formatting/style nitpicks"* — Removed per instructions.

- *"The δ metric on the LCC is cherry-picked"* — This is an unfair characterization. Computing δ necessarily requires a subset where commute times are defined in the original graph; the LCC is the natural choice. The rewiring's purpose is precisely to make commute times defined everywhere, so δ on the LCC measures the cost of that change on the part where comparison is meaningful.

- *Several generic strengths from the Strength Finder* (e.g., "this paper addressed an important problem") removed as generic or superficial.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs largely converge on the paper's content; no review-level insight emerges that the paper does not already articulate.

## Suggestions

1. **Clarify the commute time computation pipeline in Algorithm 1.** Explicitly state that \(\mathcal{R}^\dagger\) is obtained via rank-\(q\) SVD and that entries of \(\mathcal{C}\) are computed on-demand only for pairs \((i,j)\) where \(\mathbf{A}\) or \(\mathbf{A}^\top\) has a nonzero, avoiding materialization of the dense \(N \times N\) matrix. Provide the entrywise formula: \(\mathcal{C}_{ij} = \sum_{k=1}^{q} \sigma_k^{-1} (v_{ik}u_{jk} + v_{jk}u_{ik}) / \sqrt{\pi_i\pi_j} + \dots\) (or equivalent) to make the \(\mathcal{O}(q|E|)\) claim self-evident.

2. **Add statistical significance tests** for the key comparisons (CGNN vs. DirGNN) across all datasets, using the 10 public splits already available.

3. **Report standard hyperparameters** (learning rate, dropout, weight decay, optimizer, epochs) for each dataset in the main paper or appendix.

4. **Add an ablation with uniform weights on the rewired graph** to isolate the contribution of rewiring from that of commute-time weighting.

5. **Replace the ambiguous claim "6 out of 8 state-of-the-art"** with qualified language that acknowledges the close margin on Chameleon and the comparative weakness on Snap-Patents, since these are already discussed in the scope analysis.
