Now I'll write the consolidated review.

## Summary

This paper provides the first complete characterization of distributional equivalence for linear non-Gaussian (LiNG) causal models with arbitrary latent variables and cycles. The authors introduce **edge rank constraints** as a new tool, prove a duality theorem linking edge ranks to the well-known path ranks (Theorem 1), derive a practical graphical criterion for equivalence (Theorem 2), and give a transformational characterization analogous to Meek's conjecture (Theorem 3). They then develop the glvLiNG algorithm that recovers the equivalence class from data without imposing structural assumptions about measurement models, hierarchy, or acyclicity. The theoretical machinery—edge rank duality, reduction to singleton checks (Lemma 9), and matroid-based reconstruction—is technically substantial and genuinely novel.

## Strengths

- **First distributional equivalence characterization for latent-variable LiNG models with cycles.** This fills a clear gap: no prior work characterized distributional equivalence when both latent variables and cycles are present. The result reduces a complex algebraic equivalence condition (mixing-matrix equality up to scaling/permutation) to a purely graphical condition involving children bases for singleton checks (Theorem 2), which is both elegant and practical.

- **Edge rank constraints as a new tool.** The introduction of edge ranks and their duality with path ranks (Theorem 1) is a genuinely novel contribution to the rank-based toolbox for causal discovery. This duality reveals that every path-rank statement, including d-separation and t-separation, has an equivalent edge-rank formulation via matching ranks of support matrices. This perspective enables the local decomposition (Lemma 9) that makes the graphical criterion tractable and could have impact beyond this paper.

- **Transformational characterization and class traversal.** Theorem 3 provides a complete transformational characterization (admissible cycle reversals and edge additions/deletions), analogous to Meek's conjecture for this setting. This yields a practical BFS/DFS traversal of the entire equivalence class, and the authors provide an interactive demo at equiv.cc.

- **Well-structured theoretical development.** The paper progresses logically from the problem setup (irreducibility), through the algebraic-to-graphical reduction, to the edge rank tool, and finally to the graphical criterion and transformational characterization. The proofs in the appendix are detailed and appear sound.

## Weaknesses

### Fatal
None.

### Major

- **Missing oracle experiment for glvLiNG.** The paper evaluates baselines under oracle inputs (Table 5) but does **not** test glvLiNG itself with oracle rank information. This means we cannot assess whether the algorithm's reconstruction Phase 1 and Phase 2 work correctly under ideal conditions. Without this experiment, it is unclear whether errors in finite-sample results (Figure 7) stem from OICA estimation failures or from the algorithm's own reconstruction logic. The paper acknowledges OICA as a limitation and calls glvLiNG a "proof of concept," but the lack of oracle validation leaves the algorithmic contribution unsubstantiated. This is the single most significant gap.

- **Overclaim in framing about being "structural-assumption-free."** The abstract and introduction position the method as "the first structural-assumption-free discovery method." While the paper clarifies that it operates in the linear non-Gaussian parametric family (which is stated), the unqualified phrasing suggests a generality that could mislead readers. FCI and related nonparametric methods are also "structural-assumption-free" regarding graph topology (though they do not recover latent structure). The authors should qualify the claim explicitly: "the first method free from structural assumptions *within the linear non-Gaussian parametric family*." The body of the paper is more careful, but the abstract's phrasing invites misinterpretation.

### Minor

- **Real-world equivalence class size.** The stock-market case study yields 19,008 equivalent graphs on 16 vertices. While the paper identifies invariant edges (20 solid edges among 29-34 total edges), the sheer size of the class raises questions about practical utility. The method correctly outputs an equivalence class, but the paper could do more to discuss how practitioners should interpret such large classes and whether the invariant edges alone provide sufficient actionable information.

- **OICA practical limitations are acknowledged but not stress-tested.** The paper acknowledges OICA's unreliability in §6, and Appendix D.4 describes a robustness check with simulated noisy ranks. However, no systematic sensitivity analysis is provided that would show how glvLiNG degrades as OICA estimation quality varies. The finite-sample experiments use up to 200,000 samples, which is unrealistic for many applications. A controlled noise-injection study on oracle ranks would help separate algorithm robustness from OICA brittleness.

- **Sparse-graph performance.** In the finite-sample experiments (Figure 7, d=1 settings), glvLiNG underperforms the baselines. The paper offers a plausible explanation (baselines exploit sparsity-inducing structural assumptions), but the implication is that glvLiNG's strength is limited to dense settings where model misspecification hurts the baselines. This is a relatively narrow regime of advantage.

### Trivial

- Table 4 formatting has minor alignment issues (some entries span multiple rows in a way that is hard to read).

## Nice-to-Haves

- An oracle experiment testing glvLiNG's SHD under perfect rank information would substantially strengthen the algorithmic contribution. Without it, the algorithm remains an unvalidated proof of concept.
- A sensitivity analysis where controlled noise is injected into oracle ranks before passing them to glvLiNG would help quantify robustness to OICA estimation errors.
- The paper could discuss whether any of the 19,008 graphs in the real-world class share a substantial common core beyond the 20 solid edges, and whether the class size is inflated by edges among latents that are not of primary interest.

## Removed Points

- *Criticism that linearity, non-Gaussianity, and faithfulness are "strong parametric assumptions" that contradict the "assumption-free" claim.* — The paper explicitly operates in the linear non-Gaussian parametric family and uses "structural-assumption-free" to mean free from graph-structure assumptions (measurement models, hierarchy, acyclicity). This distinction is clearly drawn in the introduction. The criticism conflates parametric assumptions with structural assumptions, which the paper carefully separates. The reviewer's point about FCI being "assumption-free regarding graph structure" is addressed by the paper's own discussion of FCI's limitations (lines 42-46). I have retained a *minor* version of this criticism focusing on framing clarity rather than content error.

- *Criticism that the paper overlooks prior equivalence results (Lacerda et al., 2008; Ghassami et al., 2020).* — The paper explicitly cites these works and notes they cover fully observed settings without latent variables (lines 95-97). The claim is about equivalence *with latent variables*. The reviewer misread.

- *Request for "at least one low-scoring anchor comparison."* — All anchors listed below are used. The paper's score is positioned relative to the full set.

## Novel Insights

The most striking observation emerging from this review process is the structural parallel between the paper's theoretical contribution and the classical CPDAG/Meek conjecture framework for Markov equivalence. The paper demonstrates that distributional equivalence in LiNG models with latents and cycles admits the same three-tier structure (graphical criterion, transformational characterization, class presentation) as Markov equivalence in fully observed acyclic graphs. This framing is itself a contribution: it situates latent-variable cyclic models within a well-understood equivalence landscape and shows that they are not inherently more complex in structure, despite the intimidating combinatorics of latent variables and cycles. The key insight enabling this simplification is the edge-rank duality, which translates global path constraints into local bipartite matching constraints that decompose per singleton observed variable.

## Suggestions

1. **Add an oracle experiment for glvLiNG:** Test glvLiNG on perfect rank information derived from ground-truth graphs (i.e., skip OICA and directly feed oracle ranks). Report SHD between the recovered equivalence class and the ground-truth class. This would validate that Phase 1 and Phase 2 of the algorithm are sound.
2. **Add a noise-injection experiment:** Pass oracle mixing matrices with controlled levels of additive noise into glvLiNG to quantify how OICA estimation error propagates to SHD.
3. **Qualify the "structural-assumption-free" claim** in the abstract and introduction to explicitly state "within linear non-Gaussian models."
4. **Discuss practical interpretation of large equivalence classes** beyond listing invariant edges—perhaps showing the distribution of edge frequencies across the class.

## Score and Decision

### Calibration Anchors

| Anchor Paper | Avg Score | Comparison |
|---|---|---|
| `BNHplerBYE.md` — Score-based Greedy Search for Partially Observed Causal Models | 5.33 (Accept Poster) | Similar topic (latent-variable causal discovery). Stronger experiments with consistent empirical validation. This paper has stronger theory but weaker experiments. |
| `ssYeoL4ksl.md` — Identification of Causal Relationships in Linear Cyclic Models with Latent Variables | 5.50 (Reject) | Similar topic (cycles + latents in LiNG). Limited to bivariate analysis; this paper is far more general and complete. Despite similar scores, this paper's theoretical contribution is substantially stronger. |
| `TAOpnCPnjg.md` — Conditional ICA for Estimating Causal Structure with Latent Variables | 4.50 (Accept Poster) | Similar topic. Both have theory + algorithm contributions. This paper's experimental validation was also criticized as weak; this paper compares favorably in theoretical depth. |
| `qLbTww6vv2.md` — Towards Identifiable Latent Additive Noise Models | 4.00 (Reject) | Theory paper with weaker identifiability results. This paper's theory is more complete and the equivalence characterization is stronger. |
| `V7pT2ZRoTB.md` — Theoretical Guarantees for Causal Discovery on Large Random Graphs | 4.50 (Accept Poster) | Pure theory paper. This paper has broader scope (theory + algorithm + experiments), placing it slightly higher. |
| `mA78uXqcnl.md` — Causal Structure Learning in Hawkes Processes | 7.00 (Accept Oral) | Strong across all dimensions (theory, experiments, writing). This paper's experiments are substantially weaker by comparison. |

**Reasoning:** The paper's theoretical contribution (equivalence characterization + edge ranks) is genuinely strong and places it above the average 4-5 range. However, the missing oracle experiment for glvLiNG is a significant gap that prevents the algorithmic contribution from being fully validated. Among the anchors, this paper is stronger than the 4.50 CICA paper and comparable to the 5.33 LGES paper in overall quality, though with a different profile (stronger theory, weaker experiments).

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>