## Summary

This paper provides a theoretical analysis of how residual connections and normalization layers counteract oversmoothing in linearized GNNs. It establishes four main results: (1) residual connections prevent complete collapse and confine the reachable subspace to a Krylov subspace determined by the initial features; (2) BatchNorm prevents complete collapse through its column-wise scaling operation and drives convergence to the top-k eigenspace of the centered message-passing operator; (3) the centering step in normalization layers generically distorts the structural eigenvectors of the graph (extending beyond the regular-graph case identified by prior work); (4) based on this diagnosis, it proposes Graphnorm, a normalization layer that replaces fixed centering with a learned projection onto the top-k eigenspace.

## Strengths

- **Proposition 3 (Krylov reachability with residual connections, lines 188–191) is a genuinely informative characterization.** It proves that the reachable subspace of a GNN with initial residual connections is exactly the Krylov subspace Kr(A, X^{(0)}), meaning the system preserves dependence on initial features. This goes cleanly beyond prior oversmoothing analyses (Oono & Suzuki 2019; Wu et al. 2023; Keriven 2022) which showed only convergence to a subspace governed solely by the message-passing operator, and it explains mechanistically *why* residual connections prevent memoryless collapse.

- **Propositions 5–6 (BN drives convergence to the top-k eigenspace, with a tightness guarantee, lines 233–246) provide a precise asymptotic characterization where prior work only offered coarse collapse/no-collapse distinctions.** Prior theoretical work on normalization in GNNs did not characterize *which* subspace the features converge to. The result also ties in naturally with positional encoding literature (line 247), showing that deep GNNs with BN can be seen as emulating explicit eigenvector augmentation.

- **Proposition 7 (centering distorts structural eigenvectors for any non-regular graph, lines 274–283) is a principled diagnosis that generalizes a known issue.** Cai et al. (2021) identified the centering problem only for regular graphs; this result extends it to all non-regular graphs and quantifies the spectral dampening. This connects two previously separate lines of work (oversmoothing theory and WL expressivity via structural eigenvectors).

- **Graphnorm is derived directly from the theoretical diagnosis (lines 299–313).** The method replaces the fixed all-ones centering with a learned projection onto the top-k eigenspace (plus a residual vector to recover the all-ones direction). This is not an ad-hoc heuristic — the design follows logically from Proposition 7 — and it is backward-compatible with BatchNorm and GraphNorm.

- **The ablation study (Figure 1, lines 321–323) cleanly validates the theory.** It shows that the commonly used μ(X) measure fails to detect rank collapse (PairNorm and unnormalized baselines maintain μ but collapse to rank 1), exactly matching the paper's claim that single-measure analyses are incomplete. The experimental confirmation that BN without centering behaves differently from BN with centering supports the centering analysis.

## Weaknesses

### Major

- **The empirical validation of Graphnorm contains a stark unexplained asymmetry that weakens the causal story.** The theory predicts that centering distortion harms performance and Graphnorm fixes it. If this mechanism were the dominant factor, Graphnorm should benefit GCN and GAT comparably to GIN. The results show the opposite: for GCN and GAT, Graphnorm is essentially tied with BatchNorm (differences ≤1.2 points on all node classification tasks, mostly within one standard deviation). For GIN, Graphnorm produces transformative gains (Cora: 68.4→86.5, CiteSeer: 49.7→94.9, ogbn-arxiv: 21.1→68.9). The GIN+BatchNorm baselines on these datasets are also far below GCN+BatchNorm (e.g., GIN+BatchNorm on Cora: 68.4 vs GCN+BatchNorm: 85.2), suggesting GIN may have fundamental training instability on these benchmarks that Graphnorm incidentally resolves through an unrelated mechanism (e.g., better-conditioned optimization landscape). The paper's discussion (line 415) acknowledges GAT's asymmetry as out-of-scope but offers no explanation for the GIN pattern. This discrepancy does not invalidate the theory, but it means the experiments do not cleanly support the claimed causal link between "fixing centering distortion" and "improving performance," which is a key part of the paper's narrative.

### Minor

- **Proposition 4 (BN prevents collapse, lines 220–223) is largely a direct consequence of the BN definition.** After BN, each column has unit norm in the centered space (eq. 102–103), so μ(BN(Y)) = √k ≥ √2 for any Y with non-zero column variance. The GNN-specific content is the rank condition on V_{≠0}^T X^{(0)} that prevents degeneracy at the first layer. The result is mathematically correct, and the paper is honest about the mechanism (it attributes the effect to scaling, not to anything GNN-specific in lines 237–238), but its novelty as a "result about BN+GNN interaction" is limited — it is primarily a property of the BN operation itself with a mild initialization condition.

- **Proposition 5's claim "for all weights W^{(t)}" (line 235) is stated without specifying the conditions on W^{(t)} in the main text.** The proof is deferred to the appendix, which is stripped in this review format. The claim may be correct — the BN scaling prevents norm divergence/collapse and the dynamics are governed by the centered message-passing operator — but the main text should at minimum state whether non-degeneracy conditions (e.g., full rank, bounded condition number) are required. Without seeing the proof, a reader cannot assess whether the claim's strength is warranted.

- **Graphnorm's computational cost for eigenvector computation is not discussed anywhere in the paper.** The method requires the top-k eigenvectors of (I − 11^T/n)A. For ogbn-arxiv (~169K nodes), computing these even with iterative methods (Lanczos/Arnoldi) is non-trivial. The paper does not report what k was chosen, how the eigenvectors were computed, or the wall-clock overhead. This is a practical limitation that affects the method's deployability, and it should be acknowledged.

- **The BatchNorm analysis (eq. 102–103) uses a definition without learnable affine parameters γ, β, but practical BN includes them.** The paper's Graphnorm definition (line 311) includes γ_j, β_j as learnable parameters, acknowledging their role, but the BN analysis does not discuss whether these affine parameters can partially compensate for centering distortion. Since γ, β can rescale and shift, the gap between the analyzed and practical BN versions deserves at least a brief discussion.

### Trivial

- None beyond the standard formatting artifacts that are parser-related.

## Nice-to-Haves

- The most informative control experiment would be to compare BatchNorm, BatchNorm-without-centering (already used in the ablation study), and Graphnorm on *all* architectures in the classification table. This would isolate whether the centering removal or the eigenvector-based projection is the active ingredient.
- A hyperparameter sensitivity analysis for k (number of eigenvectors used in Graphnorm) would strengthen the practical evaluation.

## Removed Points

- **Criticism of Proposition 5 as "implausibly strong" (from Harsh Critic):** The critic asserts the claim cannot hold "for all weights" because weights can "project onto lower-dimensional subspaces" etc. This is speculation without proof inspection — the critic has not seen the proof. Furthermore, the claim is about subspace convergence (the features lie in the span of V_k asymptotically), not about exact vector recovery, which makes it more plausible. Demoted from Major to Minor. The remaining Minor weakness is about lack of explicit conditions in the main text.

- **Criticism about "first formal theoretical analysis" being generic (from Strength Finder):** This framing is somewhat generic but the specific strengths (Krylov characterization, eigenspace convergence) are concrete and backed by evidence, so they are kept as stated.

- **Criticism about missing related works:** Removed per instructions (cannot verify existence of related works).

- **Criticism about missing appendix content, proofs, etc.:** Removed per instructions (parser strips appendix sections from all papers).

- **General formatting/style nitpicks:** Removed.

## Novel Insights

The most interesting synthesis from the reviews is the asymmetry between the GIN and GCN/GAT results. The harsh critic correctly identifies this as an evidential gap for the causal story, but a potentially deeper interpretation is that GIN's message-passing operator (raw adjacency matrix A_adj, without degree normalization) makes it far more susceptible to centering distortion than GCN's normalized operator (D^{-1/2} A_adj D^{-1/2}). The raw adjacency matrix of citation networks has highly non-uniform degrees, which amplifies the eigenvalue distortion from centering. This is a testable hypothesis that the paper could explore to strengthen its empirical claims. The fact that the paper does not pursue this explanation — despite having all the technical tools to do so — is perhaps a missed opportunity rather than a fatal flaw.

## Suggestions

1. Address the GIN anomaly explicitly: run diagnostics (training loss curves, gradient norms, eigenvalue spectra of the centered vs. uncentered operators for GIN vs. GCN) to determine whether Graphnorm's GIN gains come from fixing centering distortion or from stabilizing otherwise-unstable GIN training. Report whether GIN+BatchNorm can be improved with better hyperparameter tuning.

2. Add a "BatchNorm-without-centering" baseline to the classification table across all architectures — this is the cleanest ablation for isolating the centering effect.

3. State the computational cost of computing V_k (including what k was used, the method, and wall-clock time for ogbn-arxiv). If approximate methods were used, describe them.

4. In Proposition 5, either (a) state the required conditions on W^{(t)} explicitly in the main text, or (b) weaken "for all weights" to clarify the scope.

5. Discuss whether the affine parameters γ, β in practical BN can compensate for the centering distortion identified in the theory.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>