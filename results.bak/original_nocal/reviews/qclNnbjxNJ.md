Now I have a thorough understanding of the paper. Let me synthesize the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions

## Score and Decision

Let me write the review now.

---

Here is my consolidated review.

## Summary

This paper identifies and addresses post-treatment selection — a previously underexplored problem where samples are selectively included after interventions — in interventional causal discovery with latent confounders. The authors show that post-treatment selection creates distributional invariance patterns indistinguishable from true causation under existing frameworks. They propose: (i) an augmented DAG model that explicitly represents post-treatment selection, (ii) a refined equivalence class (ℱℐ-Markov equivalence) with a corresponding graphical representation (ℱ-PAG) that can distinguish causation from selection, and (iii) a sound and complete algorithm (ℱ-FCI) that recovers the ℱ-PAG from observational and interventional data. Experiments on synthetic data and real single-cell perturbation data show gains over strong baselines.

## Strengths

1. **Identifies and formally models a genuinely overlooked source of ambiguity.** Section 2.2 and Figure 1 demonstrate that under existing frameworks, a non-causal inducing path through post-treatment selection produces the same interventional invariance pattern as an actual causal edge (variant marginal p(effect), invariant conditional p(effect|cause)). This explicit challenge to prior work is clearly motivated and well-supported.

2. **Theoretical characterization of a finer equivalence class with formal guarantees.** Theorem 2 provides graphical criteria (same skeleton, v-structure, and marks among intervened nodes) for ℱℐ-Markov equivalence. Theorem 3 (soundness) and Theorem 4 (completeness) formally guarantee that ℱ-FCI recovers the correct ℱ-PAG. These are substantive theoretical contributions that go beyond prior interventional equivalence classes.

3. **Empirical validation across both synthetic and real-world settings.** Figure 6 shows consistent improvements over six baselines (GIES, IGSP, UT-IGSP, JCI-GSP, FCI-interven, CDIS) across multiple graph sizes and sample sizes, with higher DAG Precision and lower SHD. The real-world application to Norman et al. (2019) single-cell perturbation data (Section 5.2) demonstrates practical utility in a biologically relevant setting where post-treatment selection is known to occur.

4. **The core insight — using hard interventions on Type I inducing nodes to disambiguate causation from selection — is conceptually novel and principled.** The idea that CI patterns from multiple hard interventions can break the symmetry between direct causal edges and selection-induced paths is clearly explained (Section 3.2, Figure 4) and is the paper's key methodological contribution.

## Weaknesses

### Fatal
None.

### Major
1. **Algorithm 1 pseudocode in Step 2.2 is incompletely specified.** The six conditional blocks all read `if CIs == (⟂, ⟂, ⟂, ⟂)` with identical conditions but different orientations. The actual distinct CI patterns are presented in the table in Figure 4(i) (6 columns with ✓/✗ patterns), and the text references using these rules. However, the mapping from the six CI patterns in Figure 4(i) to specific edge orientations (→, ↔, ○→, etc.) is not made explicit — Figure 4(i) maps patterns to DAG structures (a)–(h), not directly to F-PAG edge marks. This creates an avoidable gap between the theoretical characterization and a reproducible algorithm description. While the approach is recoverable from the figure and text together, the pseudocode as written is ambiguous and does not constitute a complete specification.

2. **Per-edge-type evaluation is mentioned but not shown in the main paper.** The paper's central claim is distinguishing causal edges from selection-induced edges. Yet the main experimental results (Figure 6) report only aggregate DAG Precision and SHD. The paper states that "ability to distinguish post-treatment selection is assessed in Table 1" (line 282), but this table is not in the main paper body (appendix was stripped). To properly validate the core contribution, the main paper should include per-edge-type precision/recall (causal vs. selection vs. confounded), or at minimum summarize those results in the main text. Without this, the claim that the method distinguishes causation from selection rests on indirect evidence.

### Minor
3. **Definition 5 (ℱ-PAG) semantics are imprecise.** The square mark □ is described as "a node with at least one tail and at least one arrowhead," but it is used as an endpoint mark on edges (e.g., □—□, □—○). The semantics of what each ℱ-PAG edge type (e.g., □—□ vs. □—○ vs. ○—□) encodes about underlying inducing paths is not formally defined. While Figure 5 provides illustrative examples, the paper would benefit from a precise graphical semantics table mapping each edge type to its CI interpretation.

4. **Selection strength is not quantified.** The data generation procedure (line 280) selects samples with "∑ f_s(X_i) that fall within a predefined interval," but the fraction of retained samples (i.e., how severe the selection is) is not reported. This makes it difficult to assess whether the selection scenario is realistic or trivially detectable.

5. **The assumption that interventions are available on all Type I inducing nodes is acknowledged but not analyzed.** The paper notes in the conclusion (line 296) that identification depends on Type I inducing nodes, but does not characterize failure modes or partial recovery when this assumption is violated. A discussion of which structures remain identifiable when some Type I inducing nodes are not intervened on would strengthen the paper.

### Trivial
6. Step 2.3 of Algorithm 1 contains garbled update lines (e.g., `X_{I^{(i)}} \xrightarrow{\Delta} X_{I^{(i)}}`) that appear to be formatting artifacts.

## Nice-to-Haves
- A concrete step-by-step toy example (with CI test outcomes and orientation decisions) showing how ℱ-FCI resolves an ambiguous case that baselines misclassify.
- Ablation study of ℱ-FCI without Step 2.3 to isolate the contribution of Type I inducing node detection.
- Experiments without post-treatment selection to confirm the method does not falsely detect selection when none is present.
- Formal comparison (coarseness proof) showing that ℱℐ-Markov equivalence is strictly finer than the Hauser & Bühlmann or Jaber et al. interventional equivalence classes.

## Removed Points
- **Criticism that Algorithm 1 is incompletely specified to the point of invalidating the method (Harsh Critic's Critical Issue 1 as "fatal").** The orientation rules ARE provided in Figure 4(i) (the 6-column CI pattern table), and the text explicitly references them. The pseudocode has a presentation issue (identical conditions) but the method is recoverable. This is demoted to Major weakness 1 above.
- **Claim that "the F-PAG semantics are insufficiently defined" to the point of being a "methodological gap bordering on structural."** The rough semantics are clear from Figure 5 and the explanatory text. The definition is imprecise but not fatal. Demoted to Minor weakness 3.
- **Claim that baseline comparison is "unfair" because "baselines are designed to fail under selection."** This is not unfair — the entire point is to show that modeling selection yields better results when selection is present. The critic is arguing against the premise of the evaluation.
- **Section-by-section nitpicks** (notation clarity, vague definitions, missing formal proofs in the body) that are typical of any paper with a stripped appendix and do not identify specific errors.
- **Strength Finder's generic/superficial strengths** (e.g., "problem importance," "clear motivation") — these are merged into the concrete strengths above.
- **Missing related works concern** — excluded per instructions (no external sources to verify).
- **Reproducibility nitpicks about undisclosed hyperparameters** — excluded per instructions as standard.

## Novel Insights
None beyond the paper's own contributions. The key insight — that hard interventions on intermediate (Type I inducing) nodes can resolve the ambiguity between direct causation and post-treatment selection — is the paper's own contribution, not something that emerges from the reviews.

## Suggestions
1. **Fix Algorithm 1, Step 2.2 immediately.** Replace the six identical `CIs == (⟂, ⟂, ⟂, ⟂)` conditions with the six distinct CI pattern tuples from Figure 4(i)'s table, each mapped to its corresponding edge orientation. This is a presentation fix but critical for reproducibility.
2. **Add a per-edge-type evaluation table to the main paper** (or at minimum a summary paragraph) showing precision/recall separately for causal edges, selection-induced edges, and latent confounder edges. This would directly validate the paper's central claim.
3. **Clarify Definition 5** by providing a table that formally states: for each ℱ-PAG edge type (→, ↔, □—□, □—○, etc.), what CI pattern it corresponds to and what inducing path structure it represents.
4. **Report selection retention rates** in the synthetic data experiments to characterize the difficulty of the selection problem.
5. **Add a limitations paragraph** analyzing which structures become unidentifiable when Type I inducing nodes are not intervened upon.
6. **Clean up Step 2.3 update notation** — the current `\xrightarrow{\Delta}` arrows are not explained and appear corrupted.

---

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>