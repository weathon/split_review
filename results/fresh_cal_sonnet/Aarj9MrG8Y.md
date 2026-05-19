Now let me run the calibration search (round 1 — bracketing).Round 1 bracket: **4 – 6**. Now let me narrow with round 2 anchors, reading a few closely-related papers in full.Now I have sufficient context. Let me compose the final review.

---

## Summary

This paper proposes a "universal learning principle" for spectral polynomial graph filters, requiring two conditions: (1) absolute summability of filter coefficients (convergence) and (2) Lipschitz continuity (stability). Under this framework the authors propose Adaptive Power GNN (APGNN), which uses exponentially decaying learnable coefficients θ_k = β_k α^k, analyzes its truncation error, derives a generalization bound via the continuous-graph formalism, and evaluates against 14 baselines on 8 node classification benchmarks including both homophilic and heterophilic datasets.

---

## Strengths

- **Unified convergence + stability design criterion (Section 4.1):** Combining the absolute-summability condition (Theorem 1) with Lipschitz continuity into a single actionable design criterion (Eq. 6) is a useful framing for the polynomial-filter GNN family, even if the individual conditions are classically known. The paper shows explicitly that DAGNN violates convergence as K → ∞, while PPNP and GPR-GNN satisfy the principle, clarifying the design space.

- **Concrete truncation error bound (Eqs. 12–13):** The bound ‖g_β^∞(L) − g_β^K(L)‖₂ ≤ α^{K+1}/(1−α), which is uniform over all graphs and controllable through the joint choice of K and α, is practically useful. The correspondence between this bound and empirical behavior (K > 10 gives diminishing returns; small α → trivial filter) is a genuine empirical–theory link validated in Figure 2.

- **P-hop filter with ablation (Section 4.3, Figure 3b):** The experiment fixing total order T = KP and varying P shows that the P-hop filter maintains or improves accuracy while reducing the number of learnable filter parameters. This is the most concrete and convincingly supported empirical contribution in the paper.

- **Broad experimental coverage:** Evaluation spans 8 datasets (3 homophilic, 3 heterophilic, 2 specialized), with 14 baselines and 10-run averaging. The diversity of graph types lends credibility to the generality of the performance claim.

---

## Weaknesses

### Fatal
None.

### Major

- **Ambiguous and potentially unfair hyperparameter-sharing procedure (Section 6.1):** The paper states: *"we also applied our optimal hyperparameters to them, selecting the maximum value to display."* This sentence is the only description of how baselines were configured. If the baselines were run with APGNN-optimal hyperparameters (learning rate, weight decay, etc.), this is not a fair comparison — different methods have different optimal hyperparameter profiles, and giving baselines parameters tuned for APGNN can inflate APGNN's relative advantage. This ambiguity directly threatens the validity of Table 1, which is the primary empirical evidence.

- **Unspecified constant C in Theorem 2 undermines Section 5's comparative claims:** Theorem 2 states *"there exists a constant C > 0 related to the graph function"* without bounding, specifying, or discussing C further. The paper then compares APGNN's bound to DAGNN's and GPR-GNN's (last paragraph of Section 5), but this comparison is only valid if C is the same across methods, since C presumably depends on how the model interacts with the continuous graph approximation. The paper does not justify this assumption. Without a concrete bound on C, Theorem 2 cannot rigorously support these comparative claims.

- **Missing ablation of learned β_k vs. fixed β_k:** PPNP already satisfies the proposed principle and uses an exponential envelope (Section 4.2). APGNN's distinguishing feature is that β_k is learned per-order rather than fixed. The paper never ablates APGNN with all β_k = 1 fixed (which would reduce it toward a PPNP-like model) versus APGNN with learned β_k. Without this ablation, the reader cannot determine whether APGNN's gains over APPNP come from the exponential decay structure (already present in PPNP) or from the per-order learnable weights (the genuinely new aspect). This is the single most informative missing experiment.

### Minor

- **Theorem 1 is a direct application of classical analysis, overstated as novel:** Lemma 1 (absolute convergence of power series) is classical, and Theorem 1 follows immediately from it via the spectral-radius bound ‖Ã‖₂ ≤ 1. This is essentially the Weierstrass M-test applied to a matrix-valued power series. The paper presents these as core novel theoretical contributions without acknowledging their standard mathematical lineage. The framing "universal learning principle" suggests a deeper discovery than is technically established.

- **Missing JacobiConv baseline:** JacobiConv (Wang and Zhang, 2022b) is explicitly cited in Section 3.1 as a key learnable polynomial filter using the Jacobi basis, directly in the same methodological family as APGNN. It is not included as a baseline in Section 6.1. Given that it is a strong contemporary competitor in the same design space, its omission is a notable gap.

- **Data split protocol unspecified:** Section 6.1 identifies the heterophilic datasets (Cornell, Wisconsin, Texas) from Pei et al. (2020) but does not specify which data split is used (10-fold, random 60/20/20, or fixed public split). For these datasets, absolute accuracy and inter-method comparisons vary substantially across split conventions, limiting reproducibility and the interpretability of Table 1.

- **"Universal" framing overstates scope:** The learning principle applies to spectral polynomial graph filters over undirected graphs. Spatial GNNs (GCN, GraphSAGE, GAT), graph transformers, and heterogeneous graph models are not addressed. The paper's own Section 3 distinguishes spatial and spectral GNNs. "Universal learning principle for GNNs" in the title and abstract implies broader coverage than is delivered.

### Trivial
None that survive the formatting-artifact filter.

---

## Nice-to-Haves

- A numerical illustration of the generalization bound comparison (APGNN vs. DAGNN vs. GPR-GNN) at K = 10 and representative α values, rather than only asymptotic O(·) expressions, would make Section 5's comparative analysis more concrete and actionable.
- A discussion of how the learning principle applies or does not apply to directed graphs and heterogeneous graphs would bound the claimed scope more honestly.
- Providing APGNN-specific complexity analysis (training time and memory vs. K, P, n) alongside the performance table would help practitioners choose hyperparameters.

---

## Removed Points

*These points are flagged for removal; treat them with caution.*

- **Harsh critic: "The principle does not address spatial GNNs, graph transformers, or heterogeneous graphs — scope sweep."** Retained only as a Minor note on the "universal" framing; the paper's own scope is clearly spectral polynomials throughout, so this is a framing issue, not a methodological gap.

- **Harsh critic: "The comparative analysis (Section 5) is not obvious at K = 10 because M and L_M depend on α."** Correct observation, retained in weakened form as part of the Major weakness on constant C; demoted because the asymptotic comparison is technically valid and the issue is the unspecified C, not a mathematical error.

- **Harsh critic: "JacobiConv availability."** The paper cites Wang and Zhang 2022b in related work — the model exists. Criticism retained solely as a missing-baseline concern, not as a model-availability concern.

- **Strength finder: "Necessary and sufficient convergence condition for infinite-depth graph filters as a formal criterion prior methods lacked."** Technically correct that this is N&S, but the mathematical content is the Weierstrass M-test. Retained in weakened form; the framing value is acknowledged while the novelty claim is not.

- **Strength finder: "Superior empirical performance across diverse benchmarks."** Partially invalidated by the hyperparameter-sharing ambiguity, which is a confirmed weakness from the paper's own text. Not independently listed as a strength.

---

## Novel Insights

None beyond the paper's own contributions. The most practically useful insight — that the P-hop filter reduces the required K by a factor of P for a fixed approximation target (Section 4.3), and that this reduction can be verified empirically by fixing T = KP (Figure 3b) — is already centrally discussed by the authors, though it could be foregrounded more strongly as the paper's core contribution.

---

## Suggestions

1. **Replace the ambiguous hyperparameter-sharing sentence** (Section 6.1) with a clear statement of how baseline hyperparameters were selected — ideally with a dedicated grid search for each method, or an explicit acknowledgment that shared hyperparameters may not be optimal for all baselines.
2. **Add the β_k ablation** (APGNN with all β_k = 1 fixed vs. APGNN with learned β_k, holding α constant) to directly isolate the marginal contribution of per-order learning over a fixed geometric schedule.
3. **Add JacobiConv** as a baseline in Table 1 or at minimum discuss it in Section 4.2's comparative analysis.
4. **Specify data splits** used for all datasets, particularly Cornell, Wisconsin, and Texas, with a statement of which published split convention was followed.
5. **Bound or characterize C** in Theorem 2 for at least one concrete graph model (e.g., stochastic block model) to give the generalization bound operational content beyond its current symbolic form.

---

## Score and Decision

### Calibration

**Round 1 anchors (bracketing):**
| Path | Avg score | Round | Comparison |
|---|---|---|---|
| VyMW4YZfw7 (Simplifying GNN w/ Low Rank Kernels) | 3.0 | R1 low | Weaker: more direct attack on benchmark validity without constructive alternative; rating 1–5 |
| S3zKrEQpRr (GNN as Noisy Channel) | 3.0 | R1 low | Weaker: speculative information-theoretic framing, no experiments |
| bXk9gcKhqp (Polynomial Filter via GIA Theory) | 4.0 | R1 mid | Comparable topic; rejected for unclear novelty and thin experiments |
| 4A5D1nsdtj (Universal Polynomial Basis) | 4.5 | R1 mid | Closely comparable: spectral GNN polynomial filter, also "universal," rejected |
| cTDooc2J9S (Laplace-Transform Filters) | 4.6 | R1 mid | Comparable: spectral GNN transferability theory, similar score band |
| WRLj18zwz6 (Manifold GNN Generalization) | 5.4 | R1 mid | Similar: GNN generalization bound via continuous-space framework |
| SjufxrSOYd (Invariant Graphon Networks) | 8.0 | R1 high | Much stronger: rigorous approximation theory with WL-hierarchy results |
| P7KIGdgW8S (Hölder Stability of GNN) | 8.0 | R1 high | Much stronger: novel separation quality framework with deep theory |

**Round 1 bracket: 4 – 6.**

**Round 2 anchors (narrowing):**
| Path | Avg score | Round | Comparison |
|---|---|---|---|
| bXk9gcKhqp (Polynomial Filter via GIA Theory) | 4.0 | R2 | Very close topically. That paper provides a theoretical argument (GIA theory) plus experiments; rejected for unclear novelty. Paper under review has similar issues. Slightly better experimental breadth, but worse theoretical grounding relative to claims. |
| 4A5D1nsdtj (Universal Polynomial Basis for Spectral GNN) | 4.5 | R2 | Nearest topical match. Also proposes a "universal" polynomial basis with experiments on heterophily+homophily; rejected at 4.5. Paper under review is comparable in scope and contribution depth. |
| WRLj18zwz6 (Manifold GNN Generalization) | 5.4 | R2 | Paper under review has a similar continuous-graph generalization bound but weaker (unspecified C), plus more practical experiments; slightly below this anchor. |
| Gq7RDMeZi4 (Convergent GNN Layers) | 6.25 | R2 | Accepted at 6.25; scales to 1TB graphs and has more concrete convergence proofs. Paper under review is clearly weaker in theoretical depth and experimental scale. |
| g1fE8fSOm5 (GNN Structural Information) | 5.0 | R2 | Comparable borderline paper; feature-learning theory for GCN. Paper under review roughly comparable in contribution level. |

**Positioning:** The paper is slightly better than the 4.0 anchor (broader experiments, cleaner narrative) but clearly weaker than the 5.4 manifold-generalization anchor (the generalization bound here has the unspecified C gap) and much weaker than 6.25. The 4.5 anchor (4A5D1nsdtj) is the tightest match in topic and contribution level, though that paper has its own separate issues. The experimental ambiguity (hyperparameter sharing) and the missing β_k ablation pull the score toward the lower part of the bracket.

**Final score: 4.5**

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>