Now I have thoroughly analyzed the paper and the reviewer claims. Let me compose the final consolidated review.

---

## Summary

This paper studies the **homomorphism expressivity** of spectral invariant graph neural networks (GNNs). The core result (Theorem 3.3) is an exact characterization: spectral invariant GNNs with `d` iterations can homomorphism-count exactly the family of *parallel trees* whose skeleton depth is at most `d`. The paper uses this characterization to establish a hierarchy of spectral invariant GNNs relative to other architectures (1-WL, 2-FWL, subgraph GNNs, Local 2-GNNs), derive substructure counting bounds (e.g., cycles up to 7 vertices), and address open questions from Arvind et al. (2024) and Zhang et al. (2024b). Experiments on synthetic and real tasks provide supporting evidence.

## Strengths

- **Exact homomorphism characterization (Theorem 3.3).** The paper identifies that spectral invariant GNNs can homomorphism-count precisely the set of parallel trees of bounded skeleton depth — a clean, quantitative description that is both necessary and sufficient. This provides a much more fine-grained measure of expressivity than the WL-based analyses in prior work (Arvind et al., 2024; Zhang et al., 2024b; Rattan & Seppelt, 2023).

- **Maximality via a novel pebble game (Lemmas 3.19–3.21).** The paper extends the Cai-Fürer-Immerman framework to define a pebble game tailored to spectral invariants and proves equivalence to spectral invariant GNNs. This establishes that no graph outside the parallel-tree family can be counted, giving a tight characterization.

- **Comprehensive expressivity hierarchy (Corollaries 3.4–3.8).** The paper establishes quantitative inclusion relations between spectral invariant GNNs and 1-WL, 2-FWL, subgraph GNNs, and Local 2-GNNs (Figure 4), extending and recovering results from Rattan & Seppelt (2023) and Zhang et al. (2024b).

- **New substructure counting bounds (Corollaries 3.14–3.15).** The paper derives precise cycle-counting capabilities — e.g., spectral invariant GNNs with 1 iteration can count cycles up to 6 vertices, with 2 iterations up to 7 vertices — matching the cycle counting power of 2-FWL and significantly extending Cvetkovic et al. (1997) and Fürer (2017).

- **Empirical validation.** Table 1 reports experiments on homomorphism counting, cycle counting, and ZINC that align with the theory (e.g., spectral invariant GNNs count 3–6 cycles but not 7-cycles without 2 iterations).

## Weaknesses

### Fatal
None.

### Major

1. **Counterexample for Corollary 3.11 (strict iteration hierarchy) uses an incorrect path length.** The proof constructs a graph by "replacing each edge in a path `P_{2k+1}` with a parallel edge" and claims it lies in `ℱ^{Spec,(k+1)}` but not `ℱ^{Spec,(k)}`. The skeleton of this graph is `P_{2k+1}` (a path with `2k+1` vertices, `2k` edges). Under any natural interpretation of "depth" for an unrooted skeleton — whether radius (center-rooted depth = k) or diameter (2k) — the parallel tree depth is **not** `k+1`. Using the radius interpretation (the standard convention for tree depth when rooting is not specified), the depth is `k`, placing the graph in `ℱ^{Spec,(k)}` and failing to prove strict separation. This error directly undermines:
   - Corollary 3.11 (the strict hierarchy claim),
   - Corollary 3.13 (the Ω(n) lower bound on iterations), and
   - The claimed resolution of the open question from Arvind et al. (2024, Conjecture: constant iteration convergence).

   **Why this is major and not fatal:** The error is in the construction (wrong path length), not in the underlying claim. It is likely fixable (e.g., `P_{2k+2}` appears to give depth `k+1`). The main theorem (Theorem 3.3) and the hierarchy relative to other architectures are independent of this error. Nevertheless, because the strict iteration hierarchy is prominently advertised as a key contribution, the paper must correct or remove the faulty construction.

2. **Definition of "parallel tree depth" is ambiguous.** The paper defines depth only for *rooted* trees (line 31: `dep(T^r) = max_{u∈V_T} dis_T(r,u)`). Definition 3.2 then defines parallel tree depth as "the minimum depth of any parallel tree skeleton of F" — but the skeleton is an *unrooted* tree. It is unclear whether "depth of a skeleton" means its radius (min over rootings), its diameter, or something else. This ambiguity may have caused the counterexample error, and it makes Theorem 3.3's statement less precise than it should be. The paper needs an explicit formula or convention.

### Minor

1. **Proof sketch for Theorem 3.3 is high-level.** The main text (Section 3.3) states Lemmas 3.17, 3.19, 3.20, 3.21 and sketches how they connect, but the rigorous proofs are deferred to the appendix (Theorems B.14, B.20, Lemma B.17). While this is standard for theory papers with space constraints, the sketch alone is insufficient for a reader to verify correctness without the appendix. Combined with the counterexample error, this is a concern — though it does not affect the paper's acceptability if the appendix proofs are correct.

2. **The connection between experiments and theory is supportive but not a proof.** The critic's claim that experiments are "loosely correlated" is overstated — the cycle-counting experiments (Table 1) directly test the theory's predictions (3–6 cycles with 1 iteration, 7-cycle requiring 2 iterations) and match. However, the homomorphism-counting experiments measure trained GNN predictions, not the formal homomorphism-distinguishing closedness property that defines expressivity. The experiments are useful empirical support but do not substitute for the theoretical proof.

### Trivial
None.

## Nice-to-Haves

- Provide an explicit formula for the depth of an unrooted skeleton tree, e.g., define `depth(T) = min_{r∈V_T} max_{u∈V_T} dis_T(r,u)` (the radius).
- The experiments could be strengthened by testing on additional datasets (e.g., EXP, CSL, BREC as the paper itself suggests).
- A discussion of whether the parallel tree characterization can be extended to other spectral-based architectures (e.g., those using the Laplacian rather than adjacency spectrum).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"Hierarchical claims depend on Theorem 3.3."** (from harsh critic) — This is trivially true of any paper's corollaries and is not a substantive weakness. All results in a paper depend on its main theorem.
- **"Experiments do not validate the theory."** — Partially removed. The experiments directly test the cycle-counting predictions from the theory and confirm them. The critic's characterization was too harsh. The remaining concern about the homomorphism-counting experiments being trained predictors rather than direct expressivity tests is kept as a Minor weakness.
- **"Proof sketch insufficient for correctness verification."** — Downgraded from major to minor. The paper follows standard theory-paper conventions (lemmas in main text, proofs in appendix). The reviewer's concern is understandable but not a structural flaw.
- **"Missing related works."** — Never raised as such by the critic explicitly, but per instructions, I do not mention missing related works.

## Novel Insights

The most distinctive contribution is the discovery that spectral invariants + refinement yields a clean homomorphism-counting characterization in terms of **parallel trees** — graphs obtained by replacing each edge of a tree with a bundle of internally vertex-disjoint paths. This bridges two previously orthogonal branches of graph theory (spectral theory and homomorphism counting) and yields a quantitative expressivity measure that goes well beyond the coarse WL-based comparisons in prior work. The parallel tree family itself is a novel structural class that may be of independent graph-theoretic interest.

## Suggestions

1. **Fix the counterexample for Corollary 3.11.** The simplest fix appears to be replacing `P_{2k+1}` with `P_{2k+2}` (a path of `2k+2` vertices, `2k+1` edges), whose radius is `k+1`. Verify that this graph is indeed not in `ℱ^{Spec,(k)}` under the corrected definition of skeleton depth.
2. **Clarify Definition 3.2.** State explicitly that the depth of an unrooted skeleton tree `T` is its *radius*: `depth(T) = min_{r∈V_T} max_{u∈V_T} dis_T(r,u)`. Provide a concrete example (e.g., `P_5` has depth 2).
3. **If the counterexample cannot be fixed**, weaken the claims accordingly: drop the strict hierarchy claim or state it as a conjecture, and adjust the discussion of the Arvind et al. open question.
4. **In the main text, allocate slightly more space to the proof sketch**, particularly for Lemma 3.17 (equivalence of walk encoding and spectral invariants), which is the key reduction.

## Score and Decision

The paper addresses an important question — what can spectral invariant GNNs express — and provides an elegant answer (parallel trees) with significant implications for understanding GNN hierarchies and substructure counting. The main theoretical result (Theorem 3.3) appears sound in conception, and the supporting lemmas and corollaries are well-structured. However, the counterexample for Corollary 3.11 contains a concrete error (the path length does not yield the claimed depth separation) that undermines a prominently advertised contribution. This error is likely fixable with a corrected construction, but it must be addressed. I find the paper's core contributions valuable enough to warrant acceptance pending this fix.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>