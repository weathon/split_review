Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

---

## Summary

This paper proposes a coreset-based data selection method that combines $(k,z)$-clustering (k-means/k-median) with sensitivity sampling. Under a $(z,\lambda)$-Hölder continuity assumption on the loss w.r.t. data embeddings, Theorem 5 shows that querying only $k$ points and sampling $O(1/\varepsilon^2)$ additional points yields a weighted sample whose total loss approximates the full dataset loss up to a $(1\pm\varepsilon)$ multiplicative factor plus an additive $\varepsilon\lambda\Phi_k$ term (where $\Phi_k$ is the clustering cost). The paper evaluates the approach on a linear regression task (comparing against uniform and leverage score sampling) and neural network benchmarks (comparing against uniform sampling and the $k$-center coreset of Sener & Savarese 2018).

## Strengths

- **Novel theoretical guarantee with clustering-based error term.** Theorem 5 bounds the additive error by $\varepsilon\lambda\Phi_k(X)$ — the clustering cost — which can be drastically smaller than the $n\cdot\lambda\cdot\text{diameter}$ bound implicit in the $k$-center approach of Sener & Savarese (2018). This is a real theoretical advance: for clusterable data, the error does not scale with the dataset size $n$ or the worst-case spread.

- **Sublinear query complexity.** The algorithm makes only $k$ queries to the loss function (on cluster centers) and then $O(1/\varepsilon^2)$ additional queries on sampled points, for a total of $O(k+1/\varepsilon^2)$ model inferences. This directly addresses the practical bottleneck of expensive model inference — a key motivation stated in the introduction.

- **Generality of the framework.** The assumptions (Hölder continuity w.r.t. embeddings) are significantly more general than the classification-only, strong-distributional-assumption approach of Sener & Savarese. The framework applies to any loss function (regression, classification, etc.) as long as an embedding exists, answering question 4 raised in the introduction.

- **Multi-round adaptive extension.** Theorem 6 extends the result to $r$ rounds, where the error bound involves $\Phi_{k\cdot i}$, showing that the clustering cost can be reduced adaptively with more rounds — providing a clean round-complexity / approximation trade-off.

- **Clean motivation with a lower bound.** Theorem 4 formally justifies the need for adaptive querying by showing that without any queries, uniform sampling incurs error proportional to $n\cdot\sup\ell(e)$.

## Weaknesses

### Fatal
None. The paper has a coherent core contribution — a sensitivity-sampling algorithm with provable guarantees — and the claimed theory-practice gap is not as severe as the harsh critic suggests. The experimental algorithm (cluster $\to$ query centers $\to$ extrapolate via Hölder $\to$ sensitivity sample) is a direct instantiation of the approach Theorem 5 addresses, and the paper describes this procedure in Section 5.2.

### Major
- **$\lambda$ is not specified or justified in the experiments.** The neural network experiments (Section 5.2) use the approximation $\widetilde{\ell}(e) = \ell(A(e)) + \lambda\|e-A(e)\|_2^2$ to extrapolate losses from cluster centers to all points, but the value of $\lambda$ is never stated. It is unclear whether $\lambda$ was set to a constant (e.g., 0 or 1), estimated from data, or treated as a tunable hyperparameter. Since the sampling distribution and thus all experimental results depend on this extrapolation, the omission undermines reproducibility. The paper should either state $\lambda$, estimate it from a holdout set, or show robustness to a range of $\lambda$ values.

- **Missing ablation: sensitivity sampling vs. uniform sampling within clusters.** The paper argues that sensitivity sampling (weighting by distance from centers) provides benefits over uniform sampling, but no experiment isolates this effect. A natural ablation would compare: (a) cluster + sensitivity sample vs. (b) cluster + uniform sample within each cluster. Without this, the claimed benefit of the "sensitivity" component over simple stratified clustering is unsubstantiated.

### Minor
- **Limited baseline comparison for neural network experiments.** The paper compares only against uniform sampling and the $k$-center coreset [SS18]. While [SS18] is the primary prior work being addressed, the abstract's claim of "outperforms state-of-the-art methods" is broader than the evidence supports. Additional comparisons (e.g., margin sampling, entropy sampling, or BADGE) would strengthen this claim. The error bars in Figure 2(b) also overlap in several cases, further qualifying the outperformance claim.

- **No theoretical guarantee for the regression setting.** Section 4 presents a regression algorithm (cluster rows, compute regression on centers, use result to define sampling distribution) but contains no theorem or formal guarantee — only Assumption 8 and a heuristic description. The experimental implementation also sets $\zeta \to \infty$, effectively discarding the label-information part of Assumption 8 and relying solely on distances, which is a disconnect between the theoretical framing and the practice.

- **The connection between Theorem 5 and the experimental algorithm could be clearer.** The theorem states "there exists an algorithm" without sketching how the sampling probabilities are derived from the $k$ queried points. Section 5.2 describes the experimental procedure in some detail, but the paper does not explicitly walk through how the theorem's guarantee applies to that procedure. A short paragraph connecting the two would significantly improve the paper's readability and credibility.

- **Choices of $k' = 0.2k$ and $k'' = 0.2k$ appear arbitrary** and no sensitivity analysis is provided. The number of clusters ($k''$) especially could affect both the quality of the extrapolation and the total query count.

- **Slight notation inconsistency.** The clustering cost is denoted $\Phi_{k,z}$ in the definition (line 147), $\Phi_k$ in Theorem 5 (line 188), and $\Phi_{k\cdot i}$ in Theorem 6 (line 203). While understandable from context, consistent notation would help.

### Trivial
- The abstract uses "Lipshitz" (typo) — minor parser artifact.

## Nice-to-Haves
- A 2D synthetic visualization showing which points are selected by sensitivity sampling vs. uniform sampling would help build intuition.
- The number of model inference queries used by each baseline (total inferences before and during selection) should be reported, since minimizing inferences is a central motivation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Theorem 5 is disconnected from any concrete algorithm / the paper never specifies this algorithm."** The paper references Algorithm 1 (detailed in the supplementary material, which the parser strips) and describes the high-level procedure in Section 5.2. The harsh critic's claim that "no algorithm is specified" is inaccurate given the experimental description and the assumption that the appendix exists with the pseudocode. The theory-practice gap is overstated.
- **"The entire section [Algorithmic Results] reads as a placeholder."** This is an overstatement. The section states two theorems (Theorems 5 and 6) which are the paper's core theoretical contributions, and the algorithm is referenced (in the appendix).
- **"Theorem 4 is nearly trivial."** While Theorem 4 is simple (a basic lower bound for the non-adaptive case), it properly motivates the need for adaptivity. Removing this would weaken the paper's narrative.
- **Criticisms about "no comparison to margin/entropy/BADGE" framed as a fatal omission.** These are alternative active learning paradigms, not direct competitors in the coreset-based data selection line. While adding them would strengthen the paper, their absence is not a fatal flaw given the paper's stated scope (improving upon the coreset approach of Sener & Savarese).
- **"The paper's central structural flaw—the disconnect between theory and practice—cannot be resolved by adding experiments."** This overstates the issue. The experimental algorithm follows the same paradigm as the theory (cluster + sensitivity sample under Hölder continuity). The main missing piece is specifying $\lambda$, which is addressable.

## Novel Insights

The reviews surface an interesting tension that the paper itself does not fully engage with: the theory (Theorem 5) proves existence of a good sampling distribution based on sensitivity scores, but the practical instantiation requires approximating those sensitivity scores via extrapolation from cluster centers using an unknown Hölder constant $\lambda$. This creates a subtle gap that is common in theory-driven ML papers but rarely explicitly discussed: the theoretical guarantee assumes access to an oracle for the sensitivity upper bound (which requires knowing $\lambda$), while the experiments use a heuristic proxy. A methodological contribution in its own right would be a principled procedure for estimating $\lambda$ from a small labeled validation set, or showing that the algorithm's performance is robust to misspecification of $\lambda$ across several orders of magnitude.

## Suggestions

1. **Specify $\lambda$.** State the value used in experiments, or better, report performance across a sweep of $\lambda$ values (e.g., 0.001, 0.01, 0.1, 1, 10) to demonstrate robustness, or describe a data-driven procedure for estimating it.
2. **Add the sensitivity-vs-uniform-within-clusters ablation.** This is critical for isolating the contribution of the sensitivity component from the clustering component.
3. **Expand baselines modestly.** At minimum, add a comparison to random sampling followed by importance weighting (to separate the effect of the sampling distribution from the weighting scheme).
4. **State the total query count explicitly.** Report the number of model inferences used by each method (including the initial $k'$ random points and the $k''$ cluster centers) so the reader can verify the sublinear query claim.
5. **Add a brief paragraph connecting Theorem 5 to the experimental procedure**, explaining how the theorem's guarantee applies when $\ell$ values are extrapolated from cluster centers.

## Score and Decision

This paper has a genuinely interesting core idea — combining clustering cost with sensitivity sampling for data selection — and provides a nontrivial theoretical guarantee that improves upon prior work. However, the empirical evaluation has significant gaps (unspecified $\lambda$, missing ablation, limited baselines) that prevent the paper from fully substantiating its claims. The contribution is real but the current submission does not present it convincingly enough. I recommend revision and resubmission with the above issues addressed.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>