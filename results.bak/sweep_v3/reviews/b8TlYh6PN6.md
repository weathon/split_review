Now I have all the information needed to produce a calibrated, consolidated review. Let me synthesize.

## Summary

This paper provides the first graphical characterization of distributional equivalence for linear non-Gaussian causal models that simultaneously allow **both** arbitrary latent structure and cycles — a setting where no such characterization existed before. The authors introduce *edge rank* constraints as a new tool, prove a duality between path ranks and edge ranks, and derive a local graphical criterion (Theorem 2) that reduces equivalence checking to comparing children bases of the latent set and each observed variable. They further give a transformational characterization (Theorem 3) analogous to the Meek conjecture, enabling traversal of the full equivalence class. An algorithm (glvLiNG) is developed as a proof-of-concept that this characterization can be operationalized.

## Strengths

1. **First distributional equivalence characterization for the general latent-variable + cycles setting.** Theorem 2 gives a local graphical criterion requiring only children-base checks for the latent set and each observed variable. Prior equivalence results required either no latent variables (Lacerda et al., 2008; Ghassami et al., 2020) or strong structural restrictions such as acyclicity (Adams et al., 2021). This is a genuine advance.

2. **Edge rank constraints (Definition 4) and the duality theorem (Theorem 1) are a novel and well-motivated tool.** The paper shows that path ranks (global, path-based) and edge ranks (local, edge-based) are duals via the equality $$\min(|Z|,|Y|) - \rho_{\mathcal{G}}(Z,Y) = |V| - \max(|Z|,|Y|) - r_{\mathcal{G}}(V\setminus Y, V\setminus Z).$$ This duality is what enables the local decomposition that makes Theorem 2 tractable. The paper makes a convincing case that this tool has value beyond this specific setting.

3. **Transformational characterization (Theorem 3) is clean and operationally useful.** The result that any two equivalent irreducible models are connected by a sequence of admissible cycle reversals and edge additions/deletions, with at most one cycle reversal needed, provides a concrete way to traverse the equivalence class. The running example (Figure 3, six equivalent digraphs) and the interactive demo make this concrete.

4. **Well-structured exposition with good examples.** Despite the technical density, the paper uses Examples 1 and 2 effectively, and the running analogy with Markov equivalence / CPDAGs / Meek conjecture helps orient the reader. Figures 2 and 3 are well-designed to illustrate the core concepts.

## Weaknesses

### Fatal
None.

### Major

1. **The experimental evaluation of glvLiNG is far too thin in the main text to assess it as a "structural-assumption-free discovery method."** The finite-sample experiments (the core test of whether the algorithm actually works on data) are described in a single qualitative sentence in Section 5: "glvLiNG performs particularly better than baselines on denser graphs and stays more robust to latent dimensionality... while baselines perform better on sparser graphs." No numbers, no error bars, no F1 scores or SHD values appear in the main paper. The runtime comparison (Table 4) only compares glvLiNG's rank-realization step against a linear programming baseline, not an end-to-end comparison. The oracle-input comparison (Table 5) shows that existing methods fail under misspecification, but does not demonstrate that glvLiNG succeeds. The real-data example is a brief qualitative paragraph. While all details are deferred to Appendix D.4 — and the paper itself acknowledges that "glvLiNG serves more as a proof of concept" (line 336) — the contribution list (point 4) still claims "an efficient algorithm," and the title of Section 5 is "Algorithm and Evaluation." The mismatch between the framing and the evidence is significant.

2. **The paper frames glvLiNG as "the first structural-assumption-free method for latent-variable causal discovery" (contributions, abstract, Section 5) but then backpedals in the final remarks to "the algorithm serves more as a proof of concept."** These are contradictory framings. The paper should either reposition the algorithm contribution as a proof-of-concept from the start (dropping "efficient algorithm" from the contributions) or substantially expand the experimental evidence to support the stronger claim. As written, a reader could reasonably feel overpromised.

### Minor

1. **Proof sketches for the main theorems are absent from the main text.** While proofs are deferred to the appendix (standard practice), the main text provides no intuition for several nontrivial transitions. In particular, the move from Lemma 5 (all subsets of $X$) to Theorem 2 (only singletons) is stated as "Fortunately, this time, the answer is yes" without explaining *why* edge ranks admit this decomposition while path ranks do not. Similarly, the claim that "at most one cycle reversal is needed" (Theorem 3) is asserted without justification. Adding one-paragraph proof sketches would significantly improve accessibility for expert readers.

2. **Theorem 4 (maximal equivalent digraph, the CPDAG counterpart) is only mentioned in passing and stated in the appendix.** Since the CPDAG analogy is a major narrative device throughout the paper, stating the counterpart's content (even as a brief claim) in the main text would round out the story. Currently, the reader is told "Due to space limit, this result is presented in Theorem 4 (Appendix C.3)" — but one sentence stating what it says would have been feasible.

3. **The derivation from Lemma 3 (path rank characterization) to Lemma 5 (edge rank characterization) is asserted rather than derived.** The paper states "let us rephrase Lemma 3 using edge ranks below" and presents Lemma 5, but the actual algebraic steps through Theorem 1 (duality) are not shown. While the duality theorem is stated separately, the reader must reconstruct the mapping. A brief "by applying Theorem 1 to both sides of Equation (11) we obtain..." would clarify.

### Trivial
None of substance.

## Nice-to-Haves
- The paper could benefit from a brief discussion of the asymptotic complexity of glvLiNG's equivalence-class traversal, since the output size can be exponential.
- A conceptual comparison with OICA-based methods (e.g., Salehkaleybar et al., 2020) would help readers understand how glvLiNG differs beyond the equivalence characterization.
- The "faithfulness" assumption (no coincidental low ranks) is mentioned but its potential real-world violations are not discussed.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism about "structural-assumption-free" being misleading because OICA requires linearity and non-Gaussianity:** The paper is scoped entirely to "linear non-Gaussian models" from the first paragraph of the introduction. "Structural assumptions" is consistently used in context to mean assumptions about graph structure (acyclicity, measurement patterns, purity conditions), not parametric assumptions. The paper is clear on this.
- **Criticism about missing related works:** Removed per review protocol — the reviewer may lack full knowledge of cited works.
- **Criticism about "the reduction procedure might introduce cycles or multiple edges" not being addressed:** The paper explicitly states "Applying the reduction in Proposition 2 does not increase the number of edges or cycles" (line 130). The critic's claim that this "should be argued or proven, not just stated" is overly strict for a side remark in a paper that provides formal proofs in the appendix.
- **Several of the Strength Finder's claimed strengths (about the problem being important, about addressing a fundamental obstacle, etc.):** These are generic and not backed by specific evidence in the paper. Removed.
- **Criticism that examples (Figure 2, Example 1) "do not illustrate the logical steps in the derivation":** This is a subjective preference. The examples serve their purpose of illustrating the concepts rather than proving the theorems.

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a perspective that the paper itself does not already articulate. One observation worth noting: the paper's framing of the duality theorem (Theorem 1) as a known result in matroid theory being newly connected to causal discovery is self-aware and well-placed, and the reviews do not add to this.

## Suggestions

1. **Reposition glvLiNG explicitly as a proof-of-concept in the contribution list.** Change contribution 4 from "develop an efficient algorithm" to "demonstrate that the equivalence characterization can be operationalized" to match the actual evidence provided. This would resolve the main evaluative tension.

2. **Add one-paragraph proof sketches for Theorem 2 and Theorem 3** in the main text, even at the cost of some deferred material. The critical transition from Lemma 5 to Theorem 2 (why checking singletons suffices) needs at least a sentence of intuition.

3. **Move at least one numerical result (F1 score or SHD for finite samples) into the main text**, ideally a table comparing glvLiNG against baselines on a representative experiment, with standard deviations. Even a single table would substantially strengthen the empirical section.

4. **State the content of Theorem 4 explicitly** in Section 4, even as a brief claim ("For each cycle-reversal configuration, there exists a unique maximal equivalent digraph, and we provide efficient criteria to construct it").

## Score and Decision

**Calibration anchors** (all from the deepreview_13k_calibration corpus):

| Anchor | Path | Avg Score | Comparison to Paper Under Review |
|--------|------|-----------|----------------------------------|
| A Versatile Causal Discovery Framework to Allow Causally-Related Hidden Variables | `FhQSGhBlqv.md` | 7.50 | Stronger presentation and experimental evaluation; similar-level theoretical contribution |
| Linear SCM Identification in the Presence of Confounders and Gaussian Noise | `bjxuqI4KwU.md` | 7.50 | Pure theory paper, accepted — comparable theoretical depth but no method/evaluation component |
| Structural Estimation of Partially Observed LiNGAM | `nHkMm0ywWm.md` | 6.50 | Similar theory+algorithm structure with better empirical support; narrower scope (acyclic) |
| Efficient and Trustworthy Causal Discovery with Latent Variables and Complex Relations | `BZYIEw4mcY.md` | 6.00 | Comparable profile: solid theory, algorithm with guarantees, but limited experiments and presentation issues |
| On Causal Discovery in the Presence of Deterministic Relations | `jE6VXUhxq9.md` | 6.25 | Thorough evaluation but narrower contribution; similar overall quality |
| Learning Latent Structural Causal Models | `0sO2euxhUQ.md` | 4.00 | Rejected due to weak theory and limited experiments — much weaker than the paper under review |
| Revealing Hidden Causal Variables and Latent Factors from Multiple Distributions | `vyQmKicyVw.md` | 3.50 | Rejected due to rigour and clarity issues — substantially weaker than the paper under review |

The paper under review makes a genuinely novel theoretical contribution (first equivalence characterization for the general setting) that is well-articulated and properly situated in the literature. The main weakness is the mismatch between the algorithmic claims and the evidence provided in the main text, and the lack of proof sketches for key theoretical transitions. These issues are addressable and do not undermine the core theoretical results. Calibrating against the anchors: the theoretical contribution is on par with the 7.50 papers, but the incomplete evaluation and framing issues bring the overall package down relative to those. It is stronger in theory than the 6.00 anchors but weaker in empirical completeness.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>