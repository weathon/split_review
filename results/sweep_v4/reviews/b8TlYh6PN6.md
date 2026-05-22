Now I have all the evidence needed. Let me write the consolidated review.

## Summary

This paper provides the first general characterization of distributional equivalence for linear non-Gaussian causal models that simultaneously accommodate both latent variables and cycles. The authors introduce a new theoretical tool—edge rank constraints—and establish a duality with the classical path rank constraints (Theorem 1), a local graphical criterion for equivalence (Theorem 2), and a transformational characterization of the equivalence class (Theorem 3). Based on these results, they develop glvLiNG, a constraint-based algorithm for recovering the equivalence class from data, and provide quantitative evaluation (though detailed tables are in the appendix). The paper's core theoretical contribution—closing a known gap in equivalence characterization for latent-variable cyclic models—is genuinely novel and significant.

## Strengths

1. **First general equivalence characterization for latent-variable models with cycles.** Theorems 2 and 3 provide graphical and transformational criteria for when two linear non-Gaussian models with arbitrary latent structure and cycles induce the same observed distribution set. As the paper notes, this is the first such result in any parametric setting without structural assumptions on latents. The reduction to known special cases (e.g., causally sufficient acyclic case in §4) strengthens this claim.

2. **Edge rank constraints as a new tool with duality results.** The introduction of edge ranks (Definition 4) and the duality with path ranks (Theorem 1, Equation 16, illustrated in Figure 2) is an elegant theoretical contribution with potential utility beyond this paper. The paper demonstrates this by showing how edge ranks enable the local decomposition in Theorem 2—something path ranks could not straightforwardly provide (illustrated in Example 1). The connection to matroid theory is noted but not overstated.

3. **Clean and well-structured exposition of dense material.** The paper progresses logically from problem setup (irreducibility, §2) through path ranks (§3.1), the complexity motivation for edge ranks (§3.2-3.3), to the final characterization (§4) and algorithm (§5). The writing is clear, definitions are precise, and the analogy with Markov equivalence / CPDAG is used effectively throughout to orient the reader.

4. **Irreducibility reduction cleanly eliminates trivial cases.** Propositions 1 and 2 (§2.2, illustrated in Figure 1) derive a graphical condition and explicit reduction procedure that canonically eliminates non-identifiable latent structures, grounding the subsequent analysis on non-degenerate models.

5. **Transformational characterization for equivalence class traversal.** Theorem 3, together with Lemmas 6 and 7, provides a "Meek-like" generative characterization of the equivalence class via admissible cycle reversals and edge additions/deletions, with the surprising result that at most one cycle reversal is needed (§4, line 306). The interactive demo at equiv.cc and Figure 3 provide concrete illustration.

## Weaknesses

### Fatal
None.

### Major

1. **The glvLiNG algorithm depends on OICA, which is acknowledged as impractical but the downstream sensitivity is unexamined.** The paper explicitly states (§5) that the algorithm assumes "access to an oracle OICA" and acknowledges (§5, Conclusion) that OICA is "known to be inefficient in practice" and that glvLiNG is "more a proof of concept." However, the paper provides no sensitivity analysis quantifying how OICA estimation errors propagate through the rank-realization and equivalence-class-traversal phases. Without this, a reader cannot assess at what sample sizes, dimensionalities, or latent counts the method would produce reliable results. This limits the paper's claimed contribution of a "structural-assumption-free discovery method." The theoretical contribution of the equivalence characterization is not diminished, but the practical claim of having a working discovery method is weakened.

### Minor

1. **Experimental detail in the main text is brief relative to the evaluation claims.** The paper presents five evaluation aspects (§5, lines 324-334) but the main body only provides summary-level claims (runtime "under 5s" for n=10 vertices; baselines "misidentify over half of the edges"; "glvLiNG performs particularly better on denser graphs"). The detailed Tables 3-5 and sample-size results are deferred to the appendix. While this is common for page-limited venues, the presented summary is thin enough that a reader cannot independently assess effect sizes, variances, or how many replicates were used. The real-data application (Hong Kong stock data) is mentioned in two sentences without showing the learned graph or quantitative validation.

2. **The efficiency comparison (Table 4) is against a linear programming baseline that is not named or described.** The paper (§5, line 328) states glvLiNG "solves cases with n=10 vertices in under 5s, while the baseline takes hours beyond n=5" but the baseline is described only as "a linear programming baseline for constructing digraphs to satisfy ranks of oracle OICA mixing matrices." Without knowing whether this baseline is a reasonable reference point (e.g., an integer programming formulation that is known to be NP-hard in worst case), or whether the comparison is apples-to-apples on the same compute infrastructure, the runtime advantage is hard to interpret.

### Trivial
None.

## Nice-to-Haves

- A proof sketch or intuitive explanation of why checking only bases for L and each L∪{X_i} suffices in Theorem 2 would help readers who cannot verify the full proof in the appendix. The paper currently provides a brief interpretation for the causally sufficient special case, but the main text could include 2-3 sentences on the underlying logic.
- The paper could benefit from a complexity analysis (worst-case or typical) for the equivalence-class traversal, beyond the empirical runtime claim for n=10.
- A concrete example where baselines (LaHiCaSi, PO-LiNGAM) fail due to structural assumption violations, shown in the main text rather than just cited, would strengthen the motivation.

## Removed Points

- **"Experimental results are entirely absent from the main paper" (Harsh Critic #1):** Removed because the detailed Tables 3-5 and finite-sample results are in the appendix, which the parser strips from all submissions (they exist in the original submission). Furthermore, the main text does contain quantitative results (enumeration statistics: 1,027,080 digraphs / 26,430 acyclic / 783 equivalence classes; runtime: "n=10 vertices in under 5s"; misidentification: "over half of the edges"). The evaluation is not absent, but its detail level is limited by page constraints. The criticism as a "fatal evidential gap" is not supported given parser-induced truncation.
  
- **"Sufficiency of local decomposition in Theorem 2 is a strong claim without proof visibility" (Harsh Critic #3):** Removed because this is a criticism about missing appendix/ proof content, which the rules explicitly exclude. The proof exists in the original submission (Appendix B). The paper also provides some intuition in the main text (the causally sufficient case and the bipartite matching interpretation).

- **Strength Finder's strength #6 (Real-world demonstration):** Downgraded from strength to implicit mention. The main text devotes only two sentences to the Hong Kong stock data, saying glvLiNG "recovers meaningful patterns" without showing the learned graph or any quantitative validation. This is too thin to stand as a strength in the main text.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Include the key experimental table (at minimum, SHD/F1 for glvLiNG vs. baselines across at least one sample-size setting) in the main text. Even a compact summary would substantially improve the empirical grounding available to the reader.
2. Add a sensitivity analysis paragraph showing how glvLiNG's output degrades with finite samples or imperfect OICA estimates. Even a small simulation with controlled OICA error injection would help.
3. Identify the linear programming baseline used for runtime comparison by name or by citation, to allow readers to assess the fairness of the comparison.
4. Add a brief proof sketch of why the decomposition in Theorem 2 is valid—one paragraph explaining the role of edge-rank properties that enables checking only O(|X|) subsets instead of O(2^{|X|}).

## Score and Decision

**Calibration anchors used:**

| Anchor | Path | Avg Score | Comparison |
|--------|------|-----------|------------|
| When Selection meets Intervention | xByvdb3DCm | 8.00 | Stronger empirical validation and broader impact; our paper has comparable theoretical depth but sparser experiments in main text |
| Linear SCM Identification (Gaussian Noise) | bjxuqI4KwU | 7.50 | Pure theory paper with clean results and no algorithm; our paper provides both theory and algorithm |
| A Versatile Causal Discovery Framework | FhQSGhBlqv | 7.50 | Strong theory + algorithm + experiments; very comparable in quality, though our paper tackles a harder problem (cycles + latents) |
| Structural Estimation of PO-LiNGAM | nHkMm0ywWm | 6.50 | Similar LiNGAM-with-latents topic but relies on pure-children assumptions; our paper is more general |
| Efficient and Trustworthy Causal Discovery | BZYIEw4mcY | 6.00 | Theory + algorithm paper with presentation issues and limited experiments; comparable format to ours but our theoretical result is stronger |
| Latent Variable Identifiability (Nonlinear) | QSuOHV62IQ | 3.50 | Weak theoretical contribution with unsupported claims; our paper is far more rigorous |
| Sparse Causal Model | fSxiromxAq | 3.00 | Very weak paper with neither theory nor rigorous experiments; incomparable |

The paper's theoretical contribution—the first equivalence characterization for linear non-Gaussian models with both latent variables and cycles—is genuinely novel and significant. The edge-rank tool and its duality with path ranks are elegant. The writing is clear and well-structured. The main limitation is the OICA dependency of glvLiNG and the brevity of experimental detail in the main text, which together reduce the practical impact of the algorithmic contribution. Relative to the calibration anchors, the paper sits well above the 6.0-level papers due to its cleaner theoretical contribution and clearer exposition, slightly below the 7.5-level papers which have more thoroughly integrated empirical validation in their main bodies.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>