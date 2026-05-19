- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8
Now I have a thorough understanding of the paper. Let me construct the final consolidated review.

## Summary

The paper introduces a signal sampling theory for graphons — graph limits that model large dense graphs. It proves a Poincaré inequality for graphon signals (without requiring smoothness assumptions on the graphon), connects uniqueness sets on graphons to bandwidth, and shows that Gaussian elimination on eigenvectors of finite sampled graphs yields uniqueness sets that are consistent as the graph converges to the graphon. An algorithm based on a coarse graphon approximation and a greedy heuristic is proposed, with experiments on citation networks and MalNet-Tiny.

---

## Strengths

1. **Poincaré inequality for graphons without smoothness assumptions (Theorem 3.1 / thm:poincare).** The paper generalizes Pesenson's finite-graph Poincaré inequality to graphons and, critically, does *not* require continuity or smoothness assumptions on the graphon. This is explicitly noted as a differentiator from prior graphon signal processing work (line 51–52) and is a genuine theoretical contribution.

2. **Consistency result linking finite-graph uniqueness sets to graphon uniqueness sets via spectral clustering (Theorem 3.6 / thm:consistency_general and Proposition 3.7 / prop:sampled_points_are_uniqueness_sets).** The paper provides a non-asymptotic high-probability bound showing that Gaussian elimination on the Laplacian eigenvectors of a sufficiently large graph sampled from a mixture-model graphon recovers one node from each mixture component, which forms a uniqueness set. This rigorously connects discrete graph sampling to the continuous graphon setting.

3. **Runtime advantage over prior discrete methods (Section 5, runtime analysis).** The algorithm's complexity scales as O(pq²) for the graphon-level step versus O(p|E|) for the comparable greedy method applied to the full graph. Moreover, the graphon sampling intervals can be pre-computed once and reused across graphs generated from the same graphon, avoiding repeated spectral computations.

4. **Two-task empirical validation.** The paper evaluates on two distinct tasks — GNN transferability (node classification on citation networks) and accelerated positional encoding computation (graph classification on MalNet-Tiny) — showing that graphon-subsampled graphs are not completely useless, and in the PE task the gap over random sampling is more meaningful (0.33 vs. 0.27 with isolated nodes removed).

---

## Weaknesses

### Fatal
None.

### Major

1. **Algorithm–theory gap: the consistency guarantees do not directly apply to the proposed algorithm.** The theoretical consistency results (Theorem 3.6, Proposition 3.7) concern Gaussian elimination (GE) on the Laplacian eigenvectors of the finite graph. The proposed algorithm, however, uses a *greedy heuristic* from Anis et al. applied to a coarse graphon approximation. The paper states these are "closely connected" (line 335) but provides no proof that the greedy heuristic inherits the theoretical guarantees. The rebuttal-added claim that "when the regularity assumptions of our theorems are satisfied, this algorithm will generate a consistent sampling set" (line 322) is therefore an overstatement. The conditions in Proposition 3.7 involve the difficulty function φ_n(δ), the minimum component weight w_min, and other quantities from Schiebinger et al. that are neither checked nor verifiably satisfied by the heuristic interval-selection procedure. This gap weakens the paper's central narrative that theory directly drives practice.

2. **Weak experimental validation against a single, weak baseline.** The experiments compare the proposed method *only* against random sampling (Tables 1 and 2). The related work discusses multiple graph sampling methods (Anis et al., leverage score sampling, Chamon et al.'s greedy method — lines 71–73), but none are implemented as baselines. The improvements over random sampling are small and typically within one standard deviation (e.g., Cora base: 0.49±0.09 vs. 0.46±0.09; CiteSeer base: 0.56±0.06 vs. 0.51±0.08; PubMed base: 0.71±0.07 vs. 0.69±0.07). Several configurations show random sampling performing as well or better (e.g., Cora x2 eig., PubMed x2 comm.). Without comparison to at least one competitive baseline, the claim of "good empirical performance" (abstract) is unsupported.

3. **Datasets are not "large" by contemporary standards.** The paper motivates itself with large-graph challenges, yet the main experiments use Cora (~2.7K nodes), CiteSeer (~3.3K nodes), and PubMed (~20K nodes). These are small to medium graphs. The MalNet-Tiny experiment is more relevant (graphs ≥4.5K nodes) but still modest. While this does not invalidate the approach, the "large graph" framing is incongruous with the experimental scale and the paper should either use larger graphs or adjust the scope claim.

### Minor

4. **Key theorems are opaque without cross-referencing external work.** Theorem 3.6 presents a probability bound involving multiple constants (c₀, c₁, c₂, w_min, δ, φ_n, ψ, b, S_max, C, α) that are referred to Schiebinger et al. with no intuitive explanation in the main text. While deferring definitions to an appendix is acceptable, a short paragraph giving intuition for the key parameters (e.g., "φ_n measures component separability," "w_min is the smallest mixture weight") would make the result interpretable. As written, a reader cannot assess the strength or non-vacuity of the bound from the main text alone.

5. **The assumption that node labels / latent positions are known is acknowledged but its implications are not discussed.** The paper states in Section 5 (line 345) that the method requires node labels ω_i (or at least their order) to be known. This is a strong requirement — for most real-world graphs (social networks, molecular graphs, citation networks), such latent positions are unavailable. The paper does not discuss how to handle settings where this information is absent, nor does it provide a heuristic for estimating node order (e.g., via graph embedding). This limits practical applicability and deserves more prominent treatment.

6. **Algorithmic details for the coarse graph construction are under-specified.** Step (2) requires computing integrals of the induced graphon over intervals to produce the coarse graph C̃_q (̃Ã_q entries defined as double integrals over partition cells — line 333). The paper does not explain how these integrals are computed efficiently for large sparse graphs. Naive computation would be O(n²). The runtime analysis claims O(|E| + pq² + m) but omits the cost of step (1) (constructing the induced graphon) and the integration step. Furthermore, step (3)'s local clustering (heat kernel PageRank) parameters are not specified.

### Trivial
None.

---

## Nice-to-Haves

- **Sensitivity analysis for hyperparameters (q, p, number of communities, r).** The paper fixes these ad hoc and varies them only by doubling at a single operating point. A systematic study would clarify robustness.
- **Statistical significance testing.** With only 5–10 runs and overlapping error bars, reporting p-values or confidence intervals for the accuracy differences would strengthen the empirical claims.
- **Intuitive explanation of the Γ(S) construction** in the Poincaré inequality section. The current description is dense and would benefit from a diagram or concrete example (e.g., for a stochastic block model graphon).

---

## Removed Points

These points were identified by the reviewers but are removed or downgraded for the following reasons:

- **"Node labels assumption is hidden in a comment and not discussed in the main text"** — This is factually incorrect. While the assumption also appears in a `\begin{comment}` block (lines 11–17, which would be hidden in rendering), it is stated *in the main text* at line 345: "provided that their node labels ω_1,…,ω_n (or at least their order) are known." The criticism that it is "not discussed" is removed; however, the valid concern that its implications are underexplored is retained as a Minor weakness (#5 above).

- **"The paper should compare against additional baselines from related work"** — Retained as Major weakness #2 (the lack of any competitive baseline is already covered). The specific demand for Anis et al., leverage scores, or Chamon et al. is subsumed under the general weakness about insufficient baselines.

- **"Missing appendix content / missing proofs"** — The parser strips appendix sections. Per the instructions, criticisms about missing appendix content are removed.

- **"The concurrent paper covers very similar ground"** — The paper acknowledges this (lines 75–78) and clearly differentiates: their work focuses on comparing the Poincaré constant across graph sequences, while this paper analyzes consistency via spectral clustering. Not a weakness.

- **Strength: "Use of local clustering (heat-kernel PageRank)"** — This is a minor implementation detail, not a core scientific contribution. Removed as superficial.

- **Strength: "Connection to mixture models via CDF-based equivalence"** — This is a technical lemma supporting the main results, not an independent strength. Subsumed under the consistency result strength.

---

## Novel Insights

None beyond the paper's own contributions. The harsh critic's main insight — that the algorithm does not implement the theory it claims — is a genuine observation about a gap between the theoretical framework and the practical procedure, but this is a critique, not a novel contribution. The Strength Finder's observations correctly identify the theoretical results but do not add new perspective beyond what the paper itself claims.

---

## Suggestions

1. **Directly implement the theoretical sampling procedure.** Replace (or augment) the greedy heuristic in step (2) with column-pivoted QR (i.e., the GE-based approach from the theory) applied to approximate eigenvectors (e.g., via randomized SVD). This would directly validate the consistency theorem and eliminate the theory-algorithm gap. If the heuristic must be retained, prove (or at least formally conjecture) its relationship to GE and state the limitation honestly.

2. **Add at least one competitive baseline.** Compare against the greedy method of Anis et al. (applied to the full graph) or leverage-score sampling. Even if the graphon method does not outperform them in accuracy, a clear cost-accuracy trade-off (e.g., comparable accuracy at much lower runtime) would substantiate the practical value.

3. **Provide intuition for the bound in Theorem 3.6.** Add a 2–3 sentence paragraph in Section 4 explaining what the key constants (φ_n, w_min, δ) mean and give a concrete example (e.g., a 2-block SBM) where the bound can be interpreted.

4. **Acknowledge the node-label limitation prominently** in the introduction or algorithm section. Discuss when this assumption is reasonable (e.g., graphs with known generative process) and when it is not. Optionally, include a heuristic for settings where node order is unknown.

5. **Specify the algorithmic complexity of the integration step** and clarify how the coarse graph C̃_q is computed in O(|E|) rather than O(n²). Provide a brief procedure or reference.

---
