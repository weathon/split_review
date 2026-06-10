Now let me write the final review with calibration.

## Summary

This paper provides the first distributional equivalence characterization for linear non-Gaussian latent-variable causal models without any structural assumptions — no acyclicity, no indicator pattern restrictions, no hierarchical constraints. The central contributions are: (1) a graphical criterion (Theorem 2) that reduces equivalence checking from exponentially many subset pairs to per-vertex singleton checks via a novel "children bases" concept; (2) a transformational characterization (Theorem 3) showing that cycle reversals and edge additions/deletions are necessary and sufficient to traverse equivalence classes, analogous to Meek's rules for CPDAGs; and (3) the introduction of "edge ranks" (Definition 4) as a new tool with an elegant duality to path ranks (Theorem 1), filling a missing piece in the rank-based toolbox. A proof-of-concept algorithm (glvLiNG) is developed and evaluated.

## Strengths

- **First equivalence characterization without structural assumptions (Theorem 2, Eq. 19).** Prior work (e.g., Adams et al., 2021) only gave conditions for unique identification of acyclic linear non-Gaussian models, not the full equivalence class. This result fills that gap completely and is analogous to how CPDAGs characterize Markov equivalence for the causally sufficient acyclic case. The local decomposition to per-vertex singletons makes the criterion practically checkable.

- **Introduction of edge ranks with elegant duality to path ranks (Theorem 1, Eq. 16).** This is a genuinely new algebraic-graph-theoretic tool connecting max-flow-min-cut with bipartite matching. While rooted in König's theorem (1931), the edge rank side had not been introduced to causal discovery. The paper demonstrates its concrete utility: Example 1 (§3.2) shows that path ranks alone lead to intractable complexity for equivalence checking, while edge ranks enable the local decomposition in Theorem 2.

- **Complete transformational characterization (Theorem 3).** Cycle reversals (Lemma 6) and edge additions/deletions (Lemma 7) are both necessary and sufficient to traverse equivalence classes. The "coloop" criterion for admissible edge addition (Eq. 20) is elegant and computationally checkable, enabling practical BFS/DFS-based equivalence class traversal.

- **Well-organized step-by-step derivation.** Each section motivates the next by identifying specific limitations of the prior tool: algebraic equivalence (Lemma 1) → path ranks (Lemmas 2-3) → motivation for more local tool via complexity argument (§3.2, Example 1) → edge ranks → final criterion → transformational characterization. The paper draws clear structural analogies to classical frameworks throughout (Table 2, Appendix C.5).

- **Efficient algorithm and concrete quantitative grounding.** glvLiNG solves n=10 problems in under 5 seconds vs hours for the LP baseline (Table 4). Exhaustive enumeration of equivalence class sizes (Table 3) — e.g., 783 equivalence classes from 480,640 irreducible 5-vertex digraphs with 2 latent variables — provides concrete quantitative validation.

## Weaknesses

### Fatal

None

### Major

- **Empirical evaluation is thin in the main text.** Section 5 summarizes five experimental aspects in ~200 words without showing any figures or tables — all quantitative results are deferred to the appendix. The finite-sample evaluation (point 4) is described in a single sentence ("glvLiNG performs particularly better than baselines on denser graphs...while baselines perform better on sparser graphs") with no visible crossover point or magnitude. Since the title includes "Learning" alongside "Characterization," and the paper claims glvLiNG is "the first structural-assumption-free method for latent-variable causal discovery," the algorithmic contribution needs more visible experimental support. The 7.5-scored anchor "A Versatile Causal Discovery Framework to Allow Causally-Related Hidden Variables" (FhQSGhBlqv) achieved comparable scope with full experimental evaluation in the main text, and this paper's stronger theory deserves comparably visible empirical backing.

### Minor

- **Lemma 5 (line 234) notation typo:** The statement writes "$\mathcal{G} \stackrel{\mathcal{H}}{\sim} \mathcal{H}$" which should be "$\mathcal{G} \stackrel{X}{\sim} \mathcal{H}$" to match Definition 1's notation for distributional equivalence on observed variables $X$. This is a genuine typo in the paper (not a parser artifact), as the condition $\stackrel{X}{\sim}$ is used consistently elsewhere.

- **OICA dependency limits practical applicability.** The authors acknowledge this transparently and frame glvLiNG as a proof of concept, but the known inefficiency of over-complete ICA may restrict the method to settings with very few latent variables. The authors identify clear future directions for replacing OICA with partial rank estimation methods.

### Trivial

- Example 2 (line 291) writes "$L \setminus \{X_2\} = \{L_1, L_2\}$" which is technically correct since $X_2$ is observed and not in $L$, but writing simply "$L = \{L_1, L_2\}$" would be clearer and avoid the appearance of an error.

## Nice-to-Haves

- Include at least one summary figure or table from the appendix experiments (e.g., Table 4 on runtime, or a summary of finite-sample performance showing the crossover between glvLiNG and baselines) in the main text to strengthen the algorithmic claim within the page budget.
- Brief discussion of robustness to model misspecification (near-linearity, weakly non-Gaussian noise) would strengthen practitioner relevance.

## Removed Points

These points are flagged to be removed, treat them with caution.
- Harsh Critic's concern about Example 2 notation — verified it is technically correct since $X_2$ is observed, not latent. Retained as trivial presentation nitpick above.

## Novel Insights

The most novel conceptual contribution is the introduction of edge ranks as a dual to path ranks, revealing that local (edge-level bipartite matching) and global (max-flow-min-cut) perspectives are two sides of the same bottleneck concept. This duality (Theorem 1, rooted in König's theorem from 1931 but not previously leveraged in causal discovery) is what makes the equivalence characterization tractable: Example 1 demonstrates that path ranks alone lead to intractable complexity for equivalence checking (up to 1,024 graphs in a single equivalence class for a well-structured graph), while edge ranks enable the local decomposition in Theorem 2 that reduces verification to per-vertex checks. The analogy drawn between this work's results and classical CPDAG/Meek rules/MAG frameworks (Table 2) positions the contribution as completing a foundational piece missing from the causal discovery literature.

## Suggestions

- Bring at least one experimental figure/table into the main text (e.g., the runtime comparison from Table 4, or a compact summary of finite-sample performance) to support the algorithmic claims.
- Fix the Lemma 5 notation typo ($\mathcal{G} \stackrel{\mathcal{H}}{\sim} \mathcal{H}$ → $\mathcal{G} \stackrel{X}{\sim} \mathcal{H}$).
- Consider adding a brief paragraph on robustness to model misspecification in Section 6.

## Calibration Report

**All anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| `TRHyAnInUC.md` | 3.25 | R1 | Diffusion-based CD — much weaker, applied/empirical paper |
| `MVpvyeVeyI.md` | 3.40 | R1 | Causal Bayesian Optimization — weaker applied paper |
| `AvXrppAS2o.md` | 3.00 | R1 | Outcome prediction + causal — much weaker |
| `fSxiromxAq.md` | 3.00 | R1 | Sparse causal model — much weaker |
| `fGhr39bqZa.md` | 6.00 | R1 | Homologous surrogates for latent CD — weaker theory, partial equivalence only |
| `BZYIEw4mcY.md` | 6.00 | R1 | Efficient latent CD with complex relations — assumes acyclicity, still needs structural conditions |
| `7oT1X8xjIk.md` | 5.80 | R1 | Nonlinear repr. identifiability — different setting, weaker theory |
| `Bp0HBaMNRl.md` | 6.75 | R1 | Differentiable causal discovery for hierarchical latent models — narrower setting, limited experiments |
| `xByvdb3DCm.md` | 8.00 | R1 | Selection meets intervention — comparable novelty, stronger experiments |
| `3cuJwmPxXj.md` | 8.00 | R1 | Intervention extrapolation — different setting, strong theory+empirics |
| `bjxuqI4KwU.md` | 7.50 | R2 | Linear SCM ID with Gaussian noise — strong theory but no algorithm/experiments; narrower setting |
| `FhQSGhBlqv.md` | 7.50 | R2 | Versatile framework for causally-related hidden vars — similar scope, strong experiments, but assumes acyclicity, achieves only Markov equivalence |
| `k03mB41vyM.md` | 6.50 | R2 | Identifiable exchangeable mechanisms — unifying framework, weaker empirical |

**Round 1 bracket: 7.0–8.0.** The paper is clearly above the 6.0–6.75 anchors (homologous surrogates, hierarchical models) which have comparable scope but weaker theory and/or narrower settings. The 7.5 anchors (RLCD, linear SCM ID) have comparable or weaker theoretical contributions — RLCD assumes acyclicity and achieves only Markov equivalence; linear SCM ID has no algorithm/experiments. The 8.0 anchor (selection+intervention) has comparable theoretical novelty but stronger empirical presentation.

**Round 2 narrowing:** This paper's theory is strictly stronger than both 7.5 anchors: it handles cycles (unlike RLCD) and achieves distributional equivalence (stronger than Markov equivalence), introduces a novel tool (edge ranks), and provides a complete transformational characterization. However, the thin main-text experiments are a genuine weakness that the 7.5 anchors (especially RLCD at FhQSGhBlqv) do not share. The 8.0 anchor (selection+intervention at xByvdb3DCm) matches in novelty but has full experimental support.

**Final score: 7.5.** The paper's theoretical contribution is foundational — the first equivalence characterization for latent-variable models in any parametric setting without structural assumptions — and clearly stronger than the 7.5 anchors in theory. However, the main-text empirical presentation is a concrete weakness (all experiments deferred to appendix, no figures/tables visible) that holds it just below the 8.0 level where comparable novelty is matched by full experimental support.

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>