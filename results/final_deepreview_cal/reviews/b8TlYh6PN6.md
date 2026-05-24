Now I have all the information needed. Let me produce the final consolidated review.

---

## Summary

This paper establishes the first distributional equivalence characterization for linear non-Gaussian latent-variable models with arbitrary latent structure and cycles. The key technical innovations are (1) the introduction of **edge rank constraints**, a new graphical tool dual to the familiar path ranks, and (2) a **local graphical criterion** (Theorem 2) that reduces equivalence checking to per-variable basis-match conditions, yielding an efficiently checkable decision procedure. The paper further provides a **transformational characterization** (Theorem 3) — an analog of Meek's conjecture for this setting — that enables traversal of the full equivalence class via cycle reversals and edge additions/deletions, and develops a proof-of-concept algorithm (glvLiNG). The theoretical contribution is genuinely foundational: closing a long-standing gap in the causal discovery literature.

## Strengths

- **Novel edge-rank framework and duality (Theorem 1).** The introduction of edge ranks as a local, edge-level analog of path ranks is a genuine conceptual innovation. The duality theorem (Equation 16) elegantly connects two perspectives on graph bottlenecks and fills a missing piece in the rank-based causal discovery toolbox. The duality is not merely a restatement — it enables the decomposition in Lemma 5 that the entire subsequent characterization rests on.

- **Exact, checkable graphical criterion (Theorem 2).** The reduction from checking all subsets \(x \subseteq X\) to checking singletons \(X_i\) individually is the paper's central technical insight. The criterion (Equation 19) is clean, local, and reduces to the classical causally-sufficient result when latents are absent. This is the first constructive decision procedure for equivalence in this setting.

- **Transformational characterization (Theorem 3) and traversal.** Lemma 6 (cycle reversals) and Lemma 7 (edge additions/deletions) provide a complete set of local graph operations that preserve equivalence, giving a direct analog of Meek's conjecture. The claim that at most one cycle reversal suffices is elegant, and the BFS/DFS traversal this enables has practical value — demonstrated in the paper's interactive online demo.

- **Clean theoretical foundation via irreducibility.** Propositions 1 and 2 define and operationalize a canonical reduction to irreducible models, eliminating trivial latent variables. This is a necessary and well-executed preliminary that strengthens the overall framework.

- **Clear, well-structured exposition.** The paper is written with notable clarity. The extended analogy with Markov equivalence throughout (CPDAGs, Meek's conjecture) helps readers map new results onto familiar concepts. Definitions are precise, examples are well-chosen, and Figure 2's illustration of path-rank/edge-rank duality is pedagogically effective.

## Weaknesses

### Fatal

None.

### Major

None. The theoretical core — the equivalence characterization, the criterion, and the transformational traversal — is coherently presented and its significance is clear.

### Minor

- **Finite-sample evaluation results are absent from the main text.** The evaluation in §5 summarizes five experimental angles, but for the finite-sample simulations (angle 4) and the real-world application (angle 5), only qualitative remarks appear ("glvLiNG performs particularly better than baselines on denser graphs," "recovers meaningful patterns"). Actual metrics (e.g., SHD, F1, precision/recall, variance across trials) and the experimental setup are deferred to Appendix D.4–D.5. While the paper explicitly frames glvLiNG as a "proof of concept" and the main contribution as the equivalence characterization, the main text's evaluation section would be substantially stronger with even a single summary table of quantitative results. This is addressable in revision without new experiments.

- **"At most one cycle reversal" claim is stated without justification in the main text.** Theorem 3 asserts "at most one cycle reversal is needed," which is intriguing and simplifies the class description, but the main text provides no sketch of why this bound holds. A brief intuitive explanation (or a pointer to where in the appendix the justification lives) would improve confidence.

- **Equivalence class traversal and its complexity are not discussed in the main text.** The transformational characterization (Theorem 3) enables traversal, but the paper does not address worst-case equivalence class sizes, traversal cost, or scaling behavior in the main body — information that would help readers assess the algorithm's practical scope beyond the small exhaustive enumeration (Table 3).

### Trivial

- The real-world stock-return analysis (§5, angle 5) is anecdotal in the main text. Even simple consistency checks or cross-validation against known stylized facts are not mentioned (results deferred to Appendix D.5).

## Nice-to-Haves

- A self-contained sketch of the key proof idea behind the local decomposition in Theorem 2 — specifically how Lemma 5's condition on all subsets reduces to singletons — would make the reader's confidence less dependent on the appendix.
- Discussion of computational complexity of equivalence class traversal, and statistics on class sizes beyond the small exhaustive enumeration, would ground the transformational approach in practical terms.
- The CPDAG-like result (Theorem 4, Appendix C.3) is briefly mentioned; a sketch in the main text would strengthen the narrative of comprehensive characterization.

## Removed Points

These points were flagged by reviewers but are removed from the final review:

- **"Proofs are deferred to an appendix not included in the review material."** REMOVED — per evaluation protocol, stripped appendices are a parser artifact, not an author error. The original submission includes full proofs.

- **"The core algorithm step is only sketched; Lemma 10 and full algorithmic details are in the appendix."** REMOVED — same reason as above. The paper explicitly states that detailed formulations are in Appendix A.

- **"The paper should clarify that parametric assumptions (linearity, non-Gaussianity, faithfulness) remain."** REMOVED — the paper is explicitly scoped to "linear non-Gaussian models" from the title through every section. The abstract, introduction (§1), problem setup (§2.1), and conclusion (§6) all reiterate this scope. Faithfulness is stated as an assumption in §5. The OICA limitation is discussed in §5 and §6. No reasonable reader would mistake this for an assumption-free claim beyond structural assumptions.

- **"The claim to be the first structural-assumption-free method should be clarified — OICA identifiability conditions remain."** REMOVED — the paper carefully distinguishes structural assumptions (about graph patterns) from parametric assumptions (linearity, non-Gaussianity). The "structural-assumption-free" claim refers to not requiring pure children, measurement models, triangle-freeness, bow-freeness, acyclicity, or other graph-structural restrictions that all prior latent-variable methods impose. The OICA requirements are discussed as limitations in §5 and §6.

## Novel Insights

The introduction of edge ranks and their duality with path ranks (Theorem 1) represents a genuinely novel insight with implications beyond this paper. The duality reveals that the familiar rank constraints used in causal discovery — path ranks, d-separation, t-separation — have an underexplored dual formulation in terms of bipartite matchings on edges. This is not merely a technical convenience for the current paper's proofs; it opens a new perspective on rank-based causal discovery that could simplify results in related settings (linear Gaussian, discrete models, selection bias). The paper's observation that this duality has been known in matroid theory since König (1931) but overlooked in causal discovery is itself a valuable scholarly contribution.

## Suggestions

- Move a summary table of finite-sample metrics (SHD, edge F1, runtime vs. sample size and graph density) from Appendix D.4 into the main evaluation section. Even one compact table would substantially strengthen the empirical presentation without requiring new experiments.
- Add a brief sketch of why at most one cycle reversal suffices in Theorem 3 (one or two sentences of intuition in the main text, with formal proof citation to the appendix).
- Consider adding a short paragraph on the computational complexity of BFS traversal over the equivalence class, even if only to bound the worst-case number of admissible operations per graph.

## Score and Decision

**Round-1 bracketing:** Searched for causal discovery / latent variable / equivalence characterization papers. Retrieved weak anchors (scores 3.0–3.25), middle anchors (5.25–6.50), and strong anchors (8.0). The paper clearly sits above the weak band and below the 8.0 anchors. Initial bracket: **6.0–8.0**.

**Round-2 narrowing:** Retrieved and read anchors inside the bracket:

| Anchor | Score | Comparison |
|--------|-------|------------|
| BZYIEw4mcY | 6.00 | Paper under review has a more fundamental theoretical contribution (first equivalence characterization vs. algorithm development), clearer presentation. **Clearly stronger.** |
| fGhr39bqZa | 6.00 | Similar domain; homologous surrogates vs. first equivalence characterization. Paper under review is theoretically deeper. **Clearly stronger.** |
| nHkMm0ywWm | 6.50 | PO-LiNGAM — comparable setting but still requires structural assumptions (pure children). The paper under review's equivalence characterization is more foundational. **Moderately stronger theoretically, weaker empirically in main text.** |
| FhQSGhBlqv | 7.50 | Rank-based latent CD with strong theoretical results and well-presented empirical section. Comparable theoretical novelty, but the paper under review's equivalence characterization is more fundamental. The empirical gap keeps it below this anchor. **Slightly weaker.** |
| bjxuqI4KwU | 7.50 | Purely theoretical identifiability paper. The paper under review is more comprehensive (theory + algorithm + demo + broader scope including cycles). **Comparable in theoretical quality.** |

The paper lands between nHkMm0ywWm (6.50) and FhQSGhBlqv (7.50). The theoretical contribution — the first equivalence characterization in this setting — is more significant than nHkMm0ywWm's contribution, but the empirical presentation in the main text is weaker than FhQSGhBlqv's. Given that the paper explicitly frames glvLiNG as a proof of concept and the core contribution as the characterization, the empirical weakness carries less weight than it would for a primarily algorithmic paper. The paper is closer to the 7.5 anchors in theoretical quality but held back by the sparse empirical section.

**Final score: 7.0.** Decision: **Accept.**

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>