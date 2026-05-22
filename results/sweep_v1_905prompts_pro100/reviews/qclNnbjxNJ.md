Now I have all the data I need. Let me synthesize and produce the final review.

---

## Summary

This paper addresses an underexplored problem in interventional causal discovery: post-treatment selection, where samples are selectively included after interventions (e.g., quality-control filtering in gene perturbation studies). The authors show that existing interventional frameworks cannot distinguish genuine causal relations from spurious dependencies induced by post-treatment selection, because both produce the same invariance patterns (variant marginal, invariant conditional). They introduce a novel causal formulation that explicitly models post-treatment selection via an augmented DAG with intervention indicators, characterize the Markov properties, and define a new FI-Markov equivalence class with a corresponding F-PAG graphical representation. An algorithm, F-FCI, is proven sound and complete under oracle CI tests. Experiments on synthetic and real-world single-cell perturbation data demonstrate improved precision and lower SHD compared to six baselines.

## Strengths

- **Novel problem formulation with clear diagnostic.** The paper identifies that post-treatment selection and genuine causation are indistinguishable under existing interventional frameworks because both exhibit variant marginal distributions and invariant conditionals. Figure 1 and Section 2.2 provide crisp, concrete examples (e.g., Figures 1(a) vs 1(b)) that make the non-identifiability tangible and justify the need for a new formulation.

- **Theoretically grounded equivalence class and graphical representation.** The FI-Markov equivalence (Definition 2) and F-PAG (Definition 5) go beyond standard PAG-based representations by exploiting interventional CI patterns. Lemmas 2–4 linking inducing paths to marginal/conditional distribution changes provide concrete graphical criteria, and Theorem 2 characterizes when two augmented DAGs are FI-Markov equivalent. This is a genuine theoretical advance over prior MAG/PAG frameworks.

- **Sound and complete algorithm with explicit orientation rules.** F-FCI (Algorithm 1) systematically integrates observational skeleton discovery, interventional orientation via CI patterns (Step 2.2), and refinement via Type I inducing nodes (Step 2.3). Theorems 3 and 4 establish soundness and completeness under oracle CI tests. The algorithm operationalizes the theory in a concrete, implementable procedure.

- **Comprehensive empirical validation.** The method is evaluated against six strong baselines (GIES, JCI-GSP, IGSP, UT-IGSP, FCI-interven, CDIS) across varying sample sizes, graph sizes, and both hard and soft interventions. Results (Figure 6) show consistent improvements in DAG Precision (~5%) and lower SHD. The application to the Norman single-cell perturbation dataset demonstrates practical utility beyond synthetic benchmarks.

## Weaknesses

### Fatal

None.

### Major

- **The Step 2.3 refinement requires interventions on Type I inducing nodes, but this is not transparently analyzed.** The algorithm's key advance — distinguishing direct causal edges from selection-induced inducing paths (Figure 4(b) vs (a)) — uses CI tests involving ψ_n, the intervention indicator for a Type I inducing node X_n on the inducing path (Step 2.3). By definition, ψ_n exists only when X_n is among the intervention targets I. The paper acknowledges this dependency in the conclusion ("The identification of direct causal links and selection structures depends critically on the presence of Type I inducing nodes") and implicitly in the algorithm pseudocode, but does not state it as an explicit input requirement, does not characterize which intervention patterns suffice for the completeness guarantee, and does not include an ablation varying the availability of such interventions. This matters because a practitioner cannot determine from the paper whether their intervention budget enables the claimed refinement, nor what fraction of edges can be resolved without it.

- **The role of hard vs. soft interventions in Step 2.3 is unclear.** The refinement step relies on "blocking selection on latent confounders via marginalized changes from two hard interventions" (p.8). The paper states the framework covers both hard and soft interventions, but the key disambiguation step is justified only for hard interventions (which break structural edges from S). Whether — and how much — of the refinement survives under purely soft interventions is neither analyzed nor experimentally isolated. Figure 6 shows results under both "Hard" and "Soft" conditions with the method outperforming baselines in both, which is encouraging, but the soft-intervention advantage may come from other components of the algorithm rather than Step 2.3.

### Minor

- **The F-PAG definitions are dense and under-motivated.** Definition 5 introduces four mark types and eight edge types. While Figure 5 helps, the operational meaning of the new square (□) and filled-triangle (▲) marks, and how they are derived from CI patterns, is not explained with the systematicity needed for self-contained reproducibility. A concise decision table mapping CI pattern → edge mark would substantially improve clarity.

- **The experimental gain is real but modest.** The average precision improvement of ~5% over baselines (Figure 6) is consistent but not large. For a method whose main innovation is distinguishing specific ambiguous edge types, it would be informative to report metrics specifically on those ambiguous edges (e.g., precision on edges that existing methods confuse with selection-induced ones), rather than only global DAG Precision and SHD.

- **No analysis of statistical power for the ψ-based CI tests.** The algorithm makes heavy use of CI tests between intervention indicators ψ and observed variables. These tests may have limited power at finite samples, especially when interventions are sparse. A brief discussion or diagnostic would strengthen the experimental validation.

### Trivial

- The algorithm pseudocode (Algorithm 1, Step 2.2) has a presentation issue: the CI condition patterns appear repeated across multiple orientation rules (same tuple of (⊥,⊥,⊥,⊥) shown for multiple cases), likely due to formatting. The actual CI patterns should be differentiated.

## Nice-to-Haves

- An ablation varying the proportion of Type I inducing nodes that are intervened on, to directly quantify the cost of missing those interventions, would be highly informative.
- A systematic mapping table from CI patterns to F-PAG edge marks would make the algorithm far more accessible.
- Discussion of computational complexity and scalability of the algorithm (promised in Appendix D, Figure 11, but the appendix is not available in this version).

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not provide a formal definition of what constitutes post-treatment selection"** — REMOVED. The paper clearly defines post-treatment selection (line 18-19): "the selective inclusion of samples after interventions," distinguishes it from pre-treatment selection, and models it via S in the augmented DAG (Definition 1, Eq. 1).

- **"It is not explained why the structures in Figure 1 are canonical examples"** — REMOVED. The paper explains this clearly: Figures 1(a) and (b) share identical dependence patterns (variant p(X₂), invariant p(X₂|X₁)) making them indistinguishable under existing frameworks — this is the paper's core motivational diagnostic.

- **"The analysis does not spell out why state-of-the-art methods that model selection as a virtual node would fail"** — REMOVED. Section 2.2 provides a clear argument: post-treatment selection yields the same invariance pattern as causation, so selection-aware frameworks that rely on those invariance patterns cannot distinguish them. The reasoning is self-contained.

- **"The relationship between CI patterns and structural conclusions is not systematically enumerated"** — REMOVED. Figure 4 includes a table mapping CI conditions to structures (a)-(h). While a more detailed mapping would be nice (→ Nice-to-Have), the current version is adequate.

- **"The Norman dataset results are relegated to the appendix and cannot be judged"** — REMOVED. The appendix is stripped by the parser; this is not an author error.

- **"Missing related works / comparison to specific methods for GRNI"** — REMOVED per hard rule: do not mention missing related works.

- **"The paper references pre-treatment selection but F-FCI assumes all selection is post-treatment"** — REMOVED. The paper explicitly scopes itself to post-treatment selection in Section 2.1 and acknowledges CDIS as addressing pre-treatment selection. This is scope definition, not a flaw.

- **"No consideration given to statistical power, test calibration, or finite sample impact"** — MOVED to Minor. This is a generic concern that applies to all constraint-based causal discovery methods; it does not rise to major.

- **"The algorithm's complexity and scalability are not discussed"** — MOVED to Trivial/Nice-to-Have. The paper references scalability results in Appendix D Figure 11; the appendix is unavailable due to stripping.

## Novel Insights

The most genuinely novel observation across the reviews is the structural dependence of the refinement step on the intervention set — specifically, that distinguishing causal edges from selection-induced inducing paths requires not just having interventions in general, but having hard interventions on specific Type I inducing nodes that lie along the ambiguous inducing paths. This is a deeper condition than the standard "we have interventional data" assumption in the literature, and it creates an interesting new axis for intervention design in causal discovery experiments. The paper touches on this in its limitations but does not develop it into a full analysis; doing so would strengthen the contribution and point toward a theory of minimal intervention sets for post-treatment selection disambiguation.

## Suggestions

- **Foreground the intervention-set requirement.** Add an explicit statement in the algorithm input specification: "Step 2.3 requires that at least one Type I inducing node on each ambiguous inducing path is in the intervention set I. Without this, the algorithm falls back to the coarser F-PAG representation (with ◦→ marks)." Recast the completeness theorem to be conditional on the available ψ indicators.
- **Add an ablation study** that varies the fraction of Type I inducing nodes that are intervened on, and plots the fraction of ◦→ edges that get refined to definite causal/selection marks. This would directly quantify the practical scope of the method's advantage.
- **Provide a mapping table** from CI patterns to the F-PAG edge marks (tail, arrowhead, square, triangle, circle) as a concise reference.

## Score and Decision

**Calibration summary:**

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| G5KbDVAlI6 (GISL) | 4.00 | R1 | Similar topic; clearly weaker — imprecise theorems, limited baselines, small-scale experiments |
| ZXs3pkmrRG (TICL) | 5.50 | R1/R2 | Different approach; our paper has stronger theoretical depth |
| Lxst78Rrwj | 5.00 | R2 | Different approach; weaker contribution |
| v1VvCWJAL8 | 5.75 | R2 | Different domain; comparable novelty level |
| fGhr39bqZa | 6.00 | R1 | Solid theory + algorithm for latent variables; comparable quality |
| BZYIEw4mcY | 6.00 | R1 | Efficient causal discovery with latent variables; comparable |
| SKulT2VX9p | 6.67 | R2 | Different domain (fairness); our paper has deeper theory |
| Bp0HBaMNRl | 6.75 | R2 | Differentiable causal discovery; comparable quality, better transparency |
| u63OVngeSp (Intersort) | 7.00 | R2 | Strong theory, good experiments; more transparent about limitations |
| xByvdb3DCm (CDIS) | 8.00 | R1 | Nearly identical topic; stronger presentation, more transparent limitations |

**Round 1 bracket:** 5–7. The paper is clearly stronger than the 4.0 GISL anchor (same domain) and weaker than the 8.0 CDIS anchor (same domain, clearer presentation, more transparent about limitations).

**Round 2 narrowing:** The paper lands at **6.0**. It has genuine theoretical novelty (FI-Markov equivalence, F-PAG, soundness + completeness) and strong experimental validation, comparable to the 6.0–6.75 accepted papers. However, it falls short of the 7.0–8.0 tier because the core refinement step's dependence on having interventions on Type I inducing nodes — the practical bottleneck that determines whether the method actually delivers on its central claim — is not transparently analyzed or experimentally probed. The paper is a solid contribution that would benefit from revisions addressing this transparency gap.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>