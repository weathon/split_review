## Summary

This paper characterizes distributional equivalence for linear non-Gaussian causal models with both latent variables and cycles — the first such characterization without restrictive graph-structural assumptions (e.g., acyclicity, measurement models, bow-freeness). The key theoretical innovations are (i) edge rank constraints and their duality with path ranks (Theorem 1), (ii) a local graphical criterion for equivalence that reduces checking to children-bases of singletons (Theorem 2), and (iii) a transformational characterization via cycle reversals and edge additions/deletions (Theorem 3). A proof-of-concept algorithm, glvLiNG, demonstrates recoverability from data.

## Strengths

- **First distributional equivalence characterization for models with both latent variables and cycles (§3–§4, Theorem 2, Theorem 3).** The paper fills a clearly identified gap: prior work handled cycles without latents (Lacerda et al., 2008; Ghassami et al., 2020) or latents under restrictive structural assumptions, but none handled both. The authors are explicit about this gap and deliver a genuine theoretical result.

- **Introduction of edge rank constraints and the duality theorem (Definition 4, Theorem 1).** This is a genuinely novel connection between matroid theory (König, 1931; Ingleton & Piff, 1973) and causal discovery. The paper demonstrates that edge ranks provide a local, manipulable alternative to path ranks, and the duality (Equation 16) shows the two perspectives are complementary. This contribution may have broader applicability beyond this paper.

- **Clean handling of trivial unidentifiability via irreducibility (Proposition 1, Proposition 2).** The paper gives a simple graphical condition for when a model is irreducible and an explicit reduction procedure (Figure 1). This cleanly separates genuinely unidentifiable latents from those that are in principle recoverable, and the reduction does not increase edges or cycles (line 122).

- **Transformational characterization (Theorem 3) with explicit operations.** The paper provides two concrete operations (cycle reversals from Lemma 6, edge additions/deletions from Lemma 7) that together fully characterize the equivalence class, analogous to the Meek conjecture for a different setting. Lemma 7's coloop-based criterion for admissible edge changes is a genuinely new result specific to the latent-variable setting.

- **Demonstrated tractability gain from theory (§5).** The glvLiNG algorithm, built directly on Theorem 2's local decomposition, solves n=10 in under 5s while an LP baseline takes hours beyond n=5. This provides concrete evidence that the theoretical characterization translates into computational efficiency.

## Weaknesses

### Major

- **The experimental evaluation of glvLiNG in the main text is too thin to support the abstract's algorithmic claim.** The main text (§5) reports only runtime numbers (5s vs hours) and qualitative summaries (e.g., "misidentify over half of the edges," "performs particularly better on denser graphs") without a single quantitative accuracy metric (precision, recall, SHD, or any graph-structural score) in the main body. Finite-sample evaluation is described in one vague sentence (point 4, line 324). The abstract asserts glvLiNG is "the first structural-assumption-free discovery method" — but the evidence presented in the main text does not establish that it *works* as a discovery method on finite data; it only shows that the theory makes the oracle problem tractable. While the paper partially acknowledges glvLiNG is "more as a proof of concept" (line 328), the abstract's framing implies a stronger empirical contribution.

- **No comparison against OICA-based methods.** Since glvLiNG's first step is OICA (line 308), the most natural baselines are methods that also use OICA for latent-variable recovery (e.g., Salehkaleybar et al., 2020, which the paper cites on line 106). An ablation comparing "OICA alone" vs. "OICA + glvLiNG's graph construction" would isolate what the graph-theoretic contributions add. This comparison is missing entirely, making it impossible to assess whether glvLiNG's equivalence-class traversal provides value beyond the OICA mixing matrix estimate.

### Minor

- **No asymptotic complexity analysis.** Runtime is reported only empirically for n ≤ 10. The paper does not analyze how the equivalence class traversal scales with the number of vertices or latent variables, which is a real concern given that equivalence classes can be enormous (avg ~614 models/class for 5 vertices; line 318). The paper says "it scales well" (line 330) without formal support.

- **Faithfulness assumption mentioned but not discussed in the main text.** The algorithm relies on a faithfulness assumption (Assumption 1, referenced on line 308 but deferred to the stripped appendix). The main text gives only the one-line gloss "no coincidental low ranks in the mixing matrix beyond those structurally entailed." For a paper that emphasizes not making untestable assumptions, the content and plausibility of this faithfulness assumption deserve at least a brief discussion in the main text.

- **Practical utility of large equivalence classes not discussed.** The paper reports enormous equivalence classes (480,640 irreducible models → 783 classes for 5 vertices, 2 latents) but does not discuss what a practitioner can do with such large classes. While Theorem 4 (appendix) on invariant edges and the maximal digraph partially addresses this, the main text would benefit from stating what structural features are identifiable despite class size.

### Trivial

None.

## Nice-to-Haves

- Provide an intuition in the main text for *why* edge ranks enable the local decomposition of Theorem 2 while path ranks do not — the current text (line 248) essentially says "it works" without conveying the mechanism.
- Test baselines both within and beyond their assumptions to separate misspecification effects from method quality.
- Show a concrete example of invariant structural features despite large equivalence classes to help practitioners understand what the theory delivers.

## Removed Points

These points were identified by reviewers but removed after cross-checking against the paper:

- **"Structural-assumption-free" phrasing is misleading (Harsh Critic point 3):** The paper clearly scopes itself to linear non-Gaussian models (abstract, line 33) and defines "structural assumptions" on lines 19–23 as graph-structural constraints (measurement models, acyclicity, hierarchical models, etc.). The phrase is precise given the context. Removed as the paper addresses this concern.

- **Baseline comparisons are "structurally unfair" (Harsh Critic point 2, part about strawman design):** The paper is transparent about applying baselines "beyond their assumptions" (line 322). This is a deliberate stress test, not a hidden attempt to inflate results. The missing within-assumption condition is a separate gap, captured above as a nice-to-have.

- **Algorithm description too brief / reproducibility:** The paper directs readers to the appendix for full details, which is standard for page-limited venues. Removed per hard rules.

- **Faithfulness assumption "not discussed":** The paper does reference Assumption 1 in the appendix (line 308). The point about insufficient main-text discussion is kept as a minor weakness; the claim that it is completely absent would be incorrect.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Downgrade the algorithmic claim in the abstract** to match the empirical evidence. The abstract should say "a proof-of-concept algorithm demonstrating recoverability" or similar, rather than "the first structural-assumption-free discovery method" — unless finite-sample accuracy metrics are added to the main text.
2. **Add finite-sample recovery metrics** (precision, recall, SHD, or equivalent) to the main text. A summary table or even one well-chosen figure would substantially strengthen the evaluation.
3. **Add a comparison against OICA-based methods** (Salehkaleybar et al., 2020 or similar) to isolate what glvLiNG's graph-construction steps add beyond OICA. This could be as simple as comparing the mixing matrix recovered by OICA against the graph recovered by glvLiNG from the same OICA output.
4. **Include a brief complexity discussion** — even a paragraph explaining the asymptotic cost of the rank-realization step and the class traversal would address a clear reader concern.

---

### Calibration Report

**Round 1 — Bracketing:** Three queries across weak (score<3.5), middle (3.5–7.5), and strong (>7.5) bands on topics similar to the paper. Weak anchors (2.50–3.40, Reject) were clearly below the paper's quality. Strong anchors (all 8.00, Accept) were clearly above. Middle anchors included nHkMm0ywWm (6.50, Accept — "Structural Estimation of Partially Observed Linear Non-Gaussian Acyclic Model") and BZYIEw4mcY (6.00, Accept — "Efficient and Trustworthy Causal Discovery with Latent Variables"), which are topically the closest. Bracket: [5, 7].

**Round 2 — Narrowing:** Queries within the bracket returned ia9fKO1Vjq (5.40, Accept with one 3), k03mB41vyM (6.50, Accept), Bp0HBaMNRl (6.75, Accept), and jE6VXUhxq9 (6.25, Reject). Our paper's theoretical novelty is stronger than BZYIEw4mcY (6.00) and ia9fKO1Vjq (5.40), comparable to k03mB41vyM (6.50) and Bp0HBaMNRl (6.75). Its main weakness — thin experimental evaluation relative to the abstract's claims — pulls it slightly below the 6.5 anchors, which had more detailed experiments despite their own limitations. The paper is clearly stronger than the rejected jE6VXUhxq9 (6.25) which suffered from "small contribution."

**Final score:** 6.0 — positioned near BZYIEw4mcY (6.00). Both papers have genuine theoretical contributions in the latent-variable causal discovery space, and both are held back by experimental limitations. Our paper arguably has stronger theory novelty (first to handle both cycles and latents, edge rank duality) but also has weaker in-text empirical validation relative to its own algorithmic claims.

**Anchor papers used (all rounds):**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| AvXrppAS2o.md | 3.00 | R1 | Weaker — different topic, prediction-focused, thin |
| TRHyAnInUC.md | 3.25 | R1 | Weaker — diffusion for CD, unstable method |
| MVpvyeVeyI.md | 3.40 | R1 | Weaker — CBO with unknown graphs, different focus |
| zgM66fu0wv.md | 2.50 | R1 | Weaker — LLM-based CD framework |
| nHkMm0ywWm.md | 6.50 | R1 | Comparable but stronger experiments; our theory is more novel |
| 7oT1X8xjIk.md | 5.80 | R1 | Weaker — representation learning focus, rejected |
| BZYIEw4mcY.md | 6.00 | R1,R2 | **Most comparable** — similar scope, similar experimental limitations, both accepted |
| q07DDpu8Xb.md | 5.25 | R1 | Weaker — distribution shifts for CRL |
| xByvdb3DCm.md | 8.00 | R1 | Stronger — cleaner theory+experiments, all 8s |
| 3cuJwmPxXj.md | 8.00 | R1 | Stronger — intervention extrapolation |
| hrqNOxpItr.md | 8.00 | R1 | Stronger — cross-entropy for identifiability |
| k38Th3x4d9.md | 8.00 | R1 | Stronger — root cause analysis |
| ia9fKO1Vjq.md | 5.40 | R2 | Slightly weaker — extension of existing result, accepted with a 3 |
| jE6VXUhxq9.md | 6.25 | R2 | Weaker — small contribution, rejected despite decent score |
| k03mB41vyM.md | 6.50 | R2 | Slightly stronger — cleaner experiments and unified framework |
| Bp0HBaMNRl.md | 6.75 | R2 | Slightly stronger — differentiable method with stronger experiments |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>