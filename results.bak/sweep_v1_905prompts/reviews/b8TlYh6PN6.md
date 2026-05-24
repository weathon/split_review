## Summary

This paper provides, for the first time in any parametric setting, a graphical characterization of distributional equivalence for linear non-Gaussian causal models with arbitrary latent variables and cycles. It introduces *edge rank constraints* as a new local graphical tool (dual to the well-known path ranks) and uses them to derive a clean graphical criterion for when two models induce the same observed distribution set (Theorem 2), a transformational characterization that enables equivalence class traversal (Theorem 3), and an algorithm (glvLiNG) that recovers models up to equivalence without structural assumptions like acyclicity, measurement models, or pure children requirements.

---

## Strengths

- **First general equivalence characterization for latent-variable models with cycles.** The paper delivers on its central claim: Theorem 2 reduces equivalence checking to a small set of local conditions (children bases of L and each L∪{X_i}), which is dramatically simpler than the global path-rank condition of Lemma 3. As the paper notes, this is the first such result in any parametric setting for models with arbitrary latent structures and cycles — a genuinely open gap in the literature.

- **Edge rank constraints as a new graphical tool.** The paper defines edge ranks (max bipartite matching via edges) and proves a duality theorem (Theorem 1) connecting them to path ranks — a connection known in matroid theory but absent from the causal discovery toolbox. This duality is not a cosmetic reformulation: as the paper demonstrates, edge ranks admit the local decomposition that enables Theorem 2, whereas path ranks do not. The tool itself has potential applicability beyond this specific paper.

- **Clean transformational characterization of the equivalence class.** Theorem 3 shows that two models are equivalent iff one can be reached from the other via admissible cycle reversals (Lemma 6) and edge additions/deletions (Lemma 7). This is the analog of Meek's conjecture for this setting and provides a practical way to traverse the full equivalence class via BFS/DFS. Example 2 and Figure 3 illustrate the mechanics clearly.

- **Rigorous reduction to irreducible form.** Proposition 1 gives a sharp graphical condition for irreducibility, and Proposition 2 provides an explicit reduction procedure (illustrated in Figure 1) that eliminates trivial unidentifiability without increasing edges or cycles. This canonicalization is essential and correctly handled.

---

## Weaknesses

### Major
- **The main text presents no headline numerical results from the experiments.** The evaluation section (Section 5) summarizes five experimental aspects through qualitative statements and references to appendix tables. For a submission where the algorithm is claimed as a contribution ("the first structural-assumption-free method"), a reader cannot assess the actual empirical performance from the main paper alone — no recovery rates, no precision/recall numbers, no error bars appear in the body text. Even a single compact table in the main paper showing, e.g., oracle recovery rates or finite-sample F1 scores would give readers the necessary signal to judge the method's practical behavior.

### Minor
- **Theorem 2's critical local decomposition is stated without any proof sketch or rationale in the main text.** The paper says "edge ranks allow Lemma 5 to admit a nice local decomposition: instead of checking all subsets x ⊆ X, it suffices to check each singleton X_i ∈ X independently," but offers no explanation for why this decomposition holds. Given that this is the central result enabling both the graphical criterion and the algorithm's efficiency, a brief illustration (e.g., showing that sets Y containing multiple X's do not yield new constraints beyond the singletons) would help readers assess the claim without diving into the appendix.

- **The algorithm section is described at a very high level.** Phase 1 and Phase 2 of glvLiNG are described in a single paragraph each, with key constructions (the matroid realization problem, Lemma 10) deferred entirely to the appendix. This is acceptable for a primarily theoretical paper but makes it difficult to understand how the algorithm actually works from the main text alone. Slightly more detail — e.g., the core idea of how each X_i's outgoing edges are recovered from rank queries — would improve readability.

- **The glvLiNG algorithm's graph construction step (Phase 2) is not validated under oracle conditions.** The paper validates runtime against a linear programming baseline (point 2) and compares existing methods given oracle tests (point 3), but does not include an experiment where rank constraints from a known ground-truth graph are used as *perfect oracle input* to the construction algorithm to verify it outputs a graph in the correct equivalence class. Such an experiment would separate structural recovery error from OICA estimation error and directly confirm that the algorithmic machinery (Phase 2 and traversal) works as proven. This is a gap in the evaluation design, though the theoretical proof provides assurance.

- **Reliance on OICA as an upstream estimator.** The paper acknowledges this as a limitation and frames glvLiNG as a proof of concept, which is appropriate. However, the main text's experimental summaries describe finite-sample performance without quantifying the degree to which OICA estimation error degrades the structural recovery.

### Trivial
- The paper contains a small typographical error in Lemma 5: the notation `$\mathcal{G} \stackrel{\mathcal{H}}{\sim} \mathcal{H}$` appears to be a formatting issue (should likely read `$\mathcal{G} \stackrel{X}{\sim} \mathcal{H}$`).

---

## Nice-to-Haves

- An oracle experiment for graph construction correctness (separate from OICA estimation) would substantially strengthen the algorithm validation.
- Discussion of how the equivalence class size scales with the number of observed variables (beyond the enumeration up to 6 vertices) would help assess practical applicability.
- The paper mentions possible integration of OICA-free estimators as a future direction; a brief discussion of specific candidates (e.g., cumulant-based methods) would be useful.

---

## Removed Points

The following points from the inputs were removed after verification against the paper:

- **Criticism about the "first structural-assumption-free method" claim being insufficiently scoped** — The paper clearly defines "structural assumptions" as graph restrictions (acyclicity, pure children, measurement models, etc.) and explicitly states its remaining assumptions (faithfulness, access to oracle OICA) on line 316. The reviewer's concern about faithfulness and OICA is addressed by the paper's own framing.
- **Criticism about missing comparison with other low-assumption methods** — The reviewer suggests comparison with "rank-based methods that do not require OICA," but the paper's claim is that no prior structural-assumption-free method exists for this setting. The comparison with LaHiCaSi and PO-LiNGAM under oracle (Table 5, in appendix) is the appropriate head-to-head.
- **Criticism about Theorem 4 being mentioned only in passing** — The paper explicitly states "Due to space limit, this result is presented in Theorem 4 (Appendix C.3)." This is standard practice for conference papers.
- **Criticism about the transition from Lemma 3 to Lemma 5 relying on correctness of Theorem 1** — This is speculation about a potential error, not an identified error. No concrete mistake is pointed out.
- **Criticism about the paper lacking scalability discussion for the equivalence class** — The paper enumerates classes up to 6 vertices and provides an interactive demo. A more thorough analysis would be nice but is not a core weakness.
- **Strength Finder's claim about "first structural-assumption-free discovery method" is kept as a restatement of the paper's own claim** but is noted alongside its caveats.

---

## Novel Insights

None beyond the paper's own contributions.

---

## Suggestions

1. **Add a proof sketch or intuition paragraph for Theorem 2's local decomposition** in the main text. Even 3–4 sentences explaining why sets Y containing multiple X's do not produce new constraints beyond the singletons would dramatically improve reader confidence in the paper's central result.
2. **Include at least one compact table in the main paper** showing key numerical results — e.g., oracle recovery rate (does the constructed graph belong to the correct equivalence class?) and finite-sample F1 scores for at least one experimental condition (e.g., varying sample size at fixed graph density).
3. **Add an oracle experiment for graph construction correctness:** generate mixing matrices that exactly satisfy a ground-truth graph's rank constraints, run Phase 2 and traversal, and report whether the output graph is in the correct equivalence class. This would cleanly separate structural recovery from OICA estimation error and directly validate the algorithmic claims.

---

## Score and Decision

To calibrate the score, I retrieved three bands of anchors. The **weak anchor band** (avg 3.0–3.25) contains papers with unsupported claims or inadequate methods — clearly below this paper. The **mid anchor band** (avg 5.8–6.75) contains papers on causal discovery with latent variables that make structural assumptions (pure children, acyclicity, etc.) but have more complete evaluation; these include "Efficient and Trustworthy Causal Discovery with Latent Variables" (6.0), "Structural Estimation of Partially Observed Linear Non-Gaussian Acyclic Model" (6.5), and "Differentiable Causal Discovery for Latent Hierarchical Causal Models" (6.75). The **strong anchor band** (avg 8.0) contains papers with both strong theory and thorough empirical validation.

**Round-1 bracket:** 5.5–7.5 (this paper is clearly above the 3.0-level rejects but below the 8.0-level papers with full empirical validation).

**Narrowing (Round 2):** Within the bracket, I compared against the 6.0, 6.5, and 6.75 anchors. This paper's theoretical contribution (equivalence characterization with no structural assumptions) is *more fundamental* than any of these anchors — those papers still rely on pure-children-like assumptions. However, this paper's evaluation is *thinner* than all of those anchors (the main text contains only qualitative summaries, while the 6.0–6.75 anchors include result tables in the body). On balance, the paper is comparable to the 6.5 anchor in overall quality: stronger theory, weaker evaluation.

**Final score: 6.5.** The theoretical contribution is genuinely novel and fills a recognized gap in the literature. The evaluation, however, is too thin for a higher score — the main text provides no quantitative results that a reader can independently assess.

**Decision: Accept.** The equivalence characterization, edge rank tool, and transformational characterization are substantial theoretical contributions that advance the state of the art in latent-variable causal discovery. The algorithmic component, while dependent on OICA, demonstrates that the characterization is learnable. The weaknesses are addressable and do not undermine the paper's core theoretical claims.

**Anchors consulted (all rounds):**
- TRHyAnInUC (3.25) — weak CD paper, clearly below • AvXrppAS2o (3.00) — weak CD paper, clearly below • fSxiromxAq (3.00) — weak CD paper, clearly below • 1dDxMPJy4i (3.00) — weak CD paper, clearly below • BZYIEw4mcY (6.00) — comparable scope, makes structural assumptions, stronger eval • nHkMm0ywWm (6.50) — comparable scope, makes structural assumptions, comparable overall quality • 7oT1X8xjIk (5.80) — representation learning, less relevant • fGhr39bqZa (6.00) — homologous surrogates, still makes assumptions • Bp0HBaMNRl (6.75) — differentiable latent CD, stronger eval, different setting • jE6VXUhxq9 (6.25) — deterministic relations, less relevant • k03mB41vyM (6.50) — exchangeable mechanisms, less relevant • Nx4PMtJ1ER (8.00) — strong theory+eval, above • xByvdb3DCm (8.00) — strong theory+eval, above • 3cuJwmPxXj (8.00) — strong theory+eval, above • hrqNOxpItr (8.00) — strong theory+eval, above

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>