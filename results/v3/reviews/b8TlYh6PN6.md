## Summary

This paper studies distributional equivalence in linear non-Gaussian (LiNG) causal models with arbitrary latent variables and cycles. It introduces *edge rank* constraints as a new rank-based tool, proves a duality with path ranks, and uses this to derive a graphical criterion for when two latent-variable models are distributionally equivalent (Theorem 2). It further provides a transformational characterization via cycle reversals and edge additions/deletions (Theorem 3), and proposes an algorithm (glvLiNG) that recovers the equivalence class from data. The paper claims this is the first equivalence characterization with latent variables in any parametric setting without structural assumptions, and the first structural-assumption-free discovery method.

## Strengths

1. **First equivalence characterization for latent-variable LiNG models with arbitrary structure and cycles.** The problem of characterizing distributional equivalence with both latents and cycles is stated as open, and the paper delivers a concrete criterion (Theorem 2) and a transformational characterization (Theorem 3) that together describe the equivalence class. This is a genuine theoretical advance over prior work that required acyclicity or specific measurement patterns.

2. **Novel edge-rank constraints and their duality with path ranks.** Section 3.3 introduces edge ranks as a local, edge-level tool that complements the global path-rank perspective, and proves a clean duality (Theorem 1, illustrated in Figure 2). This fills a missing piece in the rank-based toolbox for causal discovery and is the conceptual foundation that enables the paper's later results.

3. **Rigorous reduction to irreducible form.** Proposition 2 (with examples in Figure 1) gives an explicit procedure that removes trivial unidentifiable components, allowing the analysis to focus on genuinely distinguishable structure. This canonicalization is clearly presented and well-motivated.

4. **Transformational characterization with an intuitive graphical interpretation.** Theorem 3 shows that two equivalent models can be connected by admissible cycle reversals and edge additions/deletions, mirroring the classical Meek conjecture for DAGs. Example 2 and Figure 3 illustrate the operations concretely.

5. **Released code and interactive demo.** The paper provides an interactive demo at equiv.cc and releases the implementation, supporting transparency and enabling further research.

## Weaknesses

### Major

1. **The paper's central theoretical step — the local decomposition from Lemma 5 to Theorem 2 — is asserted without justification in the main text.**  
   The paper states that "edge ranks allow Lemma 5 to admit a nice local decomposition: instead of checking all subsets x ⊆ X, it suffices to check each singleton X_i ∈ X independently" and then presents Theorem 2. No proof sketch, intuition, or example is given to explain *why* this decomposition works or why checking only singleton {X_i} suffices. The derivation is entirely relegated to the appendix (which is stripped). Since Theorem 2 is the foundation for both the equivalence criterion and the algorithm's subproblem decomposition, a reader cannot assess whether this step is correct from the main text alone. This is a significant presentation gap for a theory paper where the main contribution is a graphical criterion.

2. **The experimental evaluation is essentially absent from the main text.**  
   Section 5 describes results qualitatively (e.g., "glvLiNG solves cases with n = 10 vertices in under 5s") but presents no tables, figures, or numerical results. All detailed evaluations — Table 3 (equivalence class quantification), Table 4 (runtime), Table 5 (oracle comparisons), and the finite-sample results — are deferred to the appendix. For a paper that simultaneously claims a "discovery method" and lists algorithm development as a contribution, the absence of any experimental data in the main text makes the evaluation section unverifiable. The real-data application (stock returns) is described in a single paragraph without quantitative metrics or baselines.

### Minor

3. **The algorithm description is too high-level to assess correctness or implementability.**  
   The glvLiNG pipeline has three steps, but the core second step (constructing a digraph that realizes observed rank patterns) is described only in vague terms. Phase 1 "reduces to a bipartite realization problem known in matroid theory," and Phase 2 "give[s] an explicit construction (Lemma 10 in Appendix A)." Neither the bipartite reduction nor Lemma 10's construction is explained in the main text. Without these details, the algorithm remains a black box — a reader cannot evaluate whether the construction is correct, complete, or tractable.

4. **The comparison to existing methods is not informative for the paper's intended contribution.**  
   The paper evaluates LaHiCaSi and PO-LiNGAM under oracle inputs on models that violate their assumptions (cyclic, arbitrary latent structure), finding they "tend to produce overly sparse graphs and misidentify over half of the edges." This simply confirms that methods fail when their assumptions are violated — it does not provide a meaningful baseline for the *same task*, because no existing method aims to recover the full equivalence class of linear non-Gaussian models with cycles and latents. A comparison against a natural alternative (e.g., OICA followed by a search over graphs consistent with rank constraints) would be more informative even if naive.

5. **No discussion of statistical variability or finite-sample sensitivity.**  
   The paper acknowledges OICA is used as a black box but provides no analysis of how finite-sample estimation error propagates through the algorithm, nor any confidence/error measures for the recovered equivalence class. Given that OICA is known to be unstable with small samples and the algorithm depends on exact rank information, this is a notable gap.

### Trivial

6. The paper refers frequently to tables and figures in the appendix that are not present in the review version. While this is a formatting artifact, the main text's over-reliance on deferred material (Table 1, Table 2, Figure 5, etc.) makes several passages difficult to follow.

## Nice-to-Haves

- A brief proof sketch or intuition for why the local decomposition in Theorem 2 works (e.g., illustrating the matroid property that enables the singleton check) would greatly improve reader confidence.
- Including a single figure or table of key quantitative results in the main text — even just the finite-sample F1 scores or runtime comparison — would make the evaluation section credible.
- A half-page pseudocode for the graph construction step (Phase 2) would clarify the algorithm significantly.

## Removed Points

These points from the inputs were removed for the reasons stated:

- *Harsh critic's claim that "the paper would benefit from comparing glvLiNG to a natural alternative, such as applying OICA followed by a search over possible graphs consistent with rank constraints."* This is a constructive suggestion, not a grounded weakness — the critic does not show that such an alternative exists, is feasible, or is standard practice. Moved to Nice-to-Haves.

- *Strength Finder's claim about "Empirical demonstration of structural-assumption-free recovery" citing Table 5 and Table 4.* These tables are not in the main text; the paper only gives qualitative descriptions. A strength must cite a specific visible artifact. Removed as unsupported by the main text.

- *Harsh critic's criticism about Table 1 and Table 2 being referenced but not shown.* This is a consequence of the appendix being stripped (a parser artifact, not an author omission). Removed per Hard Rules.

- *Harsh critic's claim that "the paper does not discuss variance or statistical significance of its finite-sample results."* This is a valid point but is already captured by Minor weakness #5 above (statistical variability). The harsh critic framed it as a separate point; merged.

- *Strength Finder's claim that the algorithm "handles denser graphs and larger latent dimensions without model misspecification" and "scales to 10 vertices in under 5 seconds."* These are restatements of the paper's own qualitative claims without independent evidence from visible artifacts. Removed per strength filtering rules.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the paper's main tension — genuinely novel theory presented in an incomplete form — but do not add independent analytical observations.

## Suggestions

1. Add a brief proof sketch or intuition for the local decomposition in Theorem 2 (even 1–2 paragraphs) explaining why checking only singleton {X_i} suffices. A small example showing a case where the condition fails would help.
2. Include at least one quantitative figure or table in the main text — e.g., finite-sample recovery F1 scores or a runtime comparison — so that the evaluation section is self-contained.
3. Provide a half-page pseudocode for the graph construction phase (Phase 2 of glvLiNG) or at minimum describe Lemma 10's construction at the conceptual level.
4. If space permits, include a more informative baseline comparison — e.g., a method that also handles latents in linear non-Gaussian models (such as PO-LiNGAM or RLCD) applied to settings where their assumptions are *plausible* rather than violated.

## Score and Decision

The paper presents a genuinely novel theoretical contribution — the first equivalence characterization for linear non-Gaussian models with both latent variables and cycles, enabled by the new edge-rank tool. The core ideas are creative and the problem is well-motivated. However, the paper in its current form has two major weaknesses: (1) the central theoretical step (the decomposition for Theorem 2) is stated without any justification in the main text, and (2) the experimental evaluation is essentially absent from the main text, with all tables and figures deferred to the inaccessible appendix. These gaps prevent a reader from verifying the paper's two key claims — that the equivalence criterion is correctly derived and that the algorithm actually works. The paper would require a major revision that addresses these deficiencies (at minimum a proof sketch for Theorem 2 and a summary of key experimental results in the main text) before it meets the standard for acceptance.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>