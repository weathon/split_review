## Summary

This paper studies distributional equivalence in linear non-Gaussian causal models with arbitrary latent structure and cycles — a gap that has resisted characterization. The authors introduce *edge rank* constraints as a new graphical tool, prove a duality with the more familiar path ranks (Theorem 1), and then derive a local graphical criterion for equivalence that reduces checking all subsets to checking only single observed variables (Theorem 2). They further give a transformational characterization (Theorem 3) analogous to the Meek conjecture, enabling traversal of the entire equivalence class. Finally, they develop glvLiNG, an algorithm that recovers models up to equivalence from data.

## Strengths

- **First equivalence characterization with latent variables and cycles in a parametric setting.** The paper establishes a graphical criterion (Theorem 2) and a transformational characterization (Theorem 3) for when two graphs with arbitrary latent structure and cycles induce the same observed distribution set. This fills a recognized gap: prior work on equivalence with latent variables did not exist. The claim is well-scoped ("linear non-Gaussian models") and the problem is well-motivated: without knowing *what* is identifiable, one cannot design methods for *how* to identify it.

- **Introduction of edge rank constraints as a new tool.** Edge ranks (Definition 4) operate directly on edges rather than paths, making them more local and easier to manipulate. The duality with path ranks (Theorem 1), rooted in König's theorem and matching theory, is elegantly presented (Figure 2) and opens a complementary perspective on rank constraints that may find use beyond this specific setting. The paper shows concretely why this matters: edge ranks enable the local decomposition in Theorem 2 that their path-rank-based counterpart (Lemma 3) does not admit.

- **Clean, practically useful local decomposition (Theorem 2).** The criterion reduces checking all subsets \(Z \subseteq X, Y \subseteq V\) (exponential in the number of observed variables) to checking only the latent set \(L\) and each singleton \(X_i \in X\). This is the same conceptual simplification as going from "same d-separations" to "same adjacencies and v-structures." In the causally sufficient case (\(L = \emptyset\)), it recovers the classical result of Lacerda et al. (2008).

- **Transformational characterization (Theorem 3) with explicit operations.** The two operations — admissible cycle reversals (Lemma 6) and edge additions/deletions (Lemma 7) — are concretely defined graphical checks, not abstract conditions. The example in Figure 3 and the running example in the text make the machinery tangible. The claim that at most one cycle reversal is needed is a useful simplification.

- **Quantification of equivalence-class uncertainty.** The exhaustive enumeration (e.g., 783 equivalence classes among 480,640 irreducible 5-vertex models with 2 latents) gives a concrete sense of the identifiability gap and is a useful reference for the community.

- **Demonstration of model-misspecification pitfalls.** The oracle-input comparison (Table 5) shows existing methods (LaHiCaSi, PO-LiNGAM) misidentify over half the edges when applied to models that violate their structural assumptions, providing clear empirical motivation for a structural-assumption-free approach.

- **Honest scoping of the algorithm's role.** The paper explicitly describes glvLiNG as "more as a proof of concept, showing that such equivalence is indeed recoverable without any structural assumption" (§5, Final remarks), and discusses the limitation of OICA openly.

## Weaknesses

### Fatal
None.

### Major
None that threaten the core claims. The paper's primary contribution is the theoretical characterization, and that is well-supported.

### Minor

1. **Proof sketches for the main theoretical results (Theorem 2, Theorem 3) are too terse in the main text.** The leap from Lemma 5 (equivalence via edge ranks for all \(Y \supseteq L\)) to Theorem 2 (checking only \(L\) and each \(L \cup \{X_i\}\)) is presented as a single sentence ("Fortunately, this time, the answer is yes.") with no intuitive reasoning in the main text. Similarly, the completeness direction of Theorem 3 (the two operations are not just sufficient but *necessary*) is stated but not sketched. While full proofs are in the appendix, a brief intuitive argument (e.g., "by the duality, edge-rank constraints decompose across single vertices because...") would greatly increase reader confidence and is standard for a theory paper.

2. **Finite-sample discovery accuracy results are deferred to the appendix.** The main text describes the finite-sample evaluation only in a single qualitative sentence ("glvLiNG performs particularly better than baselines on denser graphs...") and points to Appendix D.4. For a paper that claims glvLiNG "recovers models from data up to such equivalence" and is "the first structural-assumption-free discovery method," having no accuracy curves, tables, or SHD/F1 numbers in the main text weakens the empirical case. The other evaluation dimensions (class-size statistics, runtime, oracle comparisons) are in the main text, which mitigates this, but the gap is notable.

3. **Algorithm description in the main text is very high-level.** Phase 1 ("reduces to a bipartite realization problem") and Phase 2 ("we give an explicit construction (Lemma 10 in Appendix A)") are described without enough detail in the main text for a reader to understand how they work. While full details are deferred due to page limit, a few sentences on the key ideas of each phase would make the algorithm less opaque.

4. **The real-data application is entirely in the appendix.** The main text mentions a stock-return application with plausible interpretations but gives no results; these are all in Appendix D.5. Adding a brief case description with a key finding (even a sentence or two) would strengthen the main text.

### Trivial

- The paper uses both \(\stackrel{X}{\sim}\) and \(\stackrel{X}{\approx}\) for equivalence; this is slightly confusing on first pass (lines 92 vs 148).
- The notation \(\text{mrl}\) in Proposition 2 (equation 7) is defined but never used again after the proposition — consider renaming for clarity.

## Nice-to-Haves

- A brief sketch of how the duality (Theorem 1) relates to König's theorem / matching theory would help readers unfamiliar with matroids connect the dots.
- A sensitivity analysis of how OICA's estimation errors affect the rank-based digraph construction (and the final equivalence class) would be a natural complement to the oracle experiments.
- A summary-graph representation (analogous to CPDAG) for the equivalence class is mentioned (Theorem 4 in Appendix C.3) — bringing this into the main text would complete the analogy with Markov equivalence that the paper carefully develops.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic Point 1 (Insufficient justification of main theoretical result in main text)** is kept but softened to *Minor* weakness 1 above. It is a real concern about exposition, not a fatal flaw — proofs are in the appendix, which is standard.
- **Harsh Critic Point 3 (unclear relationship between theory and algorithm's guarantees)** is removed. The paper explicitly states that under oracle OICA and faithfulness, glvLiNG is guaranteed to recover the full equivalence class, with proofs deferred to Appendix A. Claiming algorithmic guarantees requires deferred proofs due to page limits; this is standard practice, not a gap.
- **Strength Finder's points 3 and 4 from "Supporting strengths"** about the algorithm recovering meaningful patterns from real data and runtime advantage: kept, but the real-data result is weakened since it is deferred to the appendix.
- **Strength Finder's generic praise** (e.g., "well-motivated problem framing" without specific evidence) — absorbed into the summary and first strength, not listed separately.
- **Criticisms about missing tables** — the parser stripped Tables 3-5, they exist in the original submission. Removed.
- **Formatting/style nitpicks** — removed per instructions.
- **"No accuracy results in the main text"** — modified to *Minor* weakness 2 above. The main text *does* report equivalence-class statistics, runtime, and oracle comparisons, and *mentions* finite-sample results qualitatively; only the detailed accuracy numbers are deferred.

## Novel Insights

None beyond the paper's own contributions. The reviewers surface no novel observation that the paper itself does not already make. The primary insight — that edge ranks enable a local decomposition that path ranks do not, leading to the first equivalence characterization with latent variables — is the paper's own central contribution.

## Suggestions

1. **Add a 5-10 line proof sketch** in Section 4 for why the local decomposition (checking only \(L\) and each \(L \cup \{X_i\}\)) follows from Lemma 5. Even a sentence like "because edge-rank constraints for any \(Y \supseteq L\) can be expressed as a union of constraints on the column space of individual vertices, and the bases condition captures which edge subsets are saturated" would help.
2. **Move at least one finite-sample accuracy result into the main text** — e.g., a small table or figure showing SHD or F1-score on simulated data at a representative sample size (say \(n=1000\)) for one or two graph configurations.
3. **Expand the algorithm description in Section 5** by 3-4 sentences explaining what Phase 2's "explicit construction" does at a conceptual level (e.g., "for each observed variable \(X_i\), we query the rank of the submatrix formed by \(X_i\) and \(L\) against its candidate children in the estimated mixing matrix, and include edges where the rank increases").
4. **Add a 2-sentence real-data highlight** in the main text (e.g., "In the stock-return analysis, glvLiNG recovered two latent factors interpretable as broad market indices, with major banks acting as central causal sources").

## Score and Decision

**Calibration anchors** (from batch retrieval):

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `/home/wg25r/review_agent/human_reviews_2026/BNHplerBYE.md` | 5.33 (Poster) | Similar topic (latent-variable causal discovery). That paper has stronger empirical evaluation in the main text but narrower theoretical contribution (GNFM model class). This paper has stronger theory but weaker main-text evaluation. |
| `/home/wg25r/review_agent/human_reviews_2026/ta8BKRa1bl.md` | 6.00 (Poster) | Identifiability theory paper with strong theory and very limited experiments (bivariate only). Similar profile to this paper, which has more experiments but some deferred to appendix. |
| `/home/wg25r/review_agent/human_reviews_2026/TAOpnCPnjg.md` | 4.50 (Poster) | CICA for latent-variable causal discovery. Strong theory, mixed reviews on experiments. This paper's theoretical contribution is more comprehensive (equivalence characterization vs. algorithm-centric theory). |
| `/home/wg25r/review_agent/human_reviews_2026/expkpx9TWg.md` | 4.00 (Reject) | Proxy-based causal effect identification with weak empirical evaluation and concerns about assumptions. This paper's theory is stronger and better-motivated. |
| `/home/wg25r/review_agent/human_reviews_2026/qLbTww6vv2.md` | 4.00 (Reject) | Latent ANM identifiability with proof-gap concerns and weaker empirical validation. This paper has a cleaner theoretical narrative. |
| `/home/wg25r/review_agent/human_reviews_2026/EzHPHhSQMD.md` | 2.00 (Reject) | Game-theoretic causal discovery with weak theory and marginal improvements. This paper is substantially stronger. |
| `/home/wg25r/review_agent/human_reviews_2026/YvMkU4BYOA.md` | 2.00 (Reject) | Heuristic BIC modification with limited evaluation. Not comparable in scope or rigor. |

The paper's primary contribution is theoretical (first equivalence characterization with latent variables), and on that dimension it is solid, novel, and well-executed. The evaluation for the accompanying algorithm is thinner in the main text but the paper scopes the algorithm as a proof of concept. Relative to the anchors, this paper is stronger than the 4.00-4.50 range papers and comparable to the 5.33-6.00 range, though with a different strengths profile (stronger theory, weaker main-text evaluation).

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>