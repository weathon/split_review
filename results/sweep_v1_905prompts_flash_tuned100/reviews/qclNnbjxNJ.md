## Summary

This paper identifies post-treatment selection as an overlooked challenge in interventional causal discovery and proposes a formal framework to address it. The authors introduce the FI-Markov equivalence class and its graphical representation (F-PAG), along with an algorithm (F-FCI) that is proven sound and complete for recovering causal relations, latent confounders, and post-treatment selection patterns from interventional data with oracle CI tests. Experiments on synthetic data and a real-world gene perturbation dataset show that F-FCI outperforms several baselines.

## Strengths

- **Novel problem formulation addressing a genuine gap.** Post-treatment selection in interventional causal discovery is a real and underexplored problem — existing frameworks produce the same invariance/variability patterns for causal relations and selection-induced dependencies. The paper provides a clean formalization via augmented DAGs and explicitly defines how post-treatment selection is modeled (Section 3.1, Definition 1). The examples in Figure 1 and the CI pattern analysis in Figure 4(i) concretely demonstrate why existing formulations fail.

- **FI-Markov equivalence and F-PAG extend the representational vocabulary in a principled way.** The paper defines a finer-grained equivalence class (Definition 2) that distinguishes structures previously inseparable, and introduces new edge marks (square □, triangle marks) in the F-PAG (Definition 5) that carry genuine structural information not captured by standard PAGs. Theorem 2 provides graphical criteria linking d-separation in the augmented DAG to invariance/variability patterns, which grounds the equivalence class definition.

- **Soundness and completeness guarantees.** The paper provides both a soundness theorem (Theorem 3) and a completeness theorem (Theorem 4) for F-FCI under oracle CI tests. Having both guarantees is stronger than many interventional causal discovery papers that offer only soundness.

- **Consistent empirical advantage over six baselines.** Figure 6 shows F-FCI achieving higher DAG Precision and lower SHD across multiple graph sizes (10–25 variables), sample sizes (500–2000), and both hard and soft interventions. Error bars (95% CI) are reported, and the evaluation uses non-linear SEMs with both latent confounders and post-treatment selection — a non-trivial setup. Code is provided via GitHub.

## Weaknesses

### Major

- **Algorithm pseudocode is incompletely specified in the main text, making the core method difficult to evaluate as presented.** In Step 2.2 (Algorithm 1), all six orientation rules check the identical condition `CIs == (⊥,⊥,⊥,⊥)` while producing different orientation outcomes. The paper defers to Figure 4(i) for the mapping, but that figure maps CI patterns to structure labels (a)–(h), not to edge orientations — the reader must cross-reference Figure 5 and Definition 5 to reconstruct the mapping. The △ and ▲ edge marks introduced in Step 2.3 are used in the pseudocode update rules (e.g., `→△ X_{I(i)}`) but are not formally defined in Definition 5 or explained in the notation system. The `AllPaths()` construction in Step 2.1 enumerates subsets without describing a practical search strategy. These specification gaps mean a reader cannot verify the algorithm's correctness from the description alone, which undermines the paper's headline theoretical claims.

- **Experimental evaluation lacks ablation studies that isolate the contribution of the proposed post-treatment selection modeling.** The comparison against six baselines that do not model post-treatment selection shows F-FCI performs better — this is expected and informative, but it conflates the benefit of modeling selection with the general strength of the constraint-based approach. Without ablations that (a) run F-FCI while ignoring selection (treating it as pre-treatment), (b) remove Step 2.3 (Type I inducing node refinement), or (c) test on data *without* post-treatment selection to verify no degradation, the experiments do not cleanly attribute the gains to the specific innovations claimed. The paper mentions Table 1 in the appendix (ability to distinguish post-treatment selection) and Figures 11–12 (scalability, robustness), but these are inaccessible in the extracted text and not discussed sufficiently in the main body.

- **Real-world evaluation lacks quantitative validation in the main text.** Section 5.2 states that F-FCI identifies regulatory links and spurious selection dependencies on the Norman dataset, with results "evaluated using prior knowledge provided by Enrichr." No precision, recall, F1, or other quantitative metrics are reported in the main text. The analysis is deferred entirely to Appendix D.3, which is stripped. For a paper that makes claims about real-world applicability, this is insufficient evidence.

### Minor

- **Completeness condition is not stated in the theorem statements.** Theorem 4 claims completeness, but the text later acknowledges that identification of direct causal links/selection "depends critically on the presence of Type I inducing nodes" and that Type II inducing nodes remain a limitation. The theorem statements themselves do not qualify this dependence, which could mislead readers about the scope of the guarantee. The condition should be explicitly stated alongside the theorem.

- **The algorithm's reliance on enumerating subsets of `AllPaths()` (Step 2.1) is described without a computational strategy.** While constraint-based methods commonly use greedy search, the paper does not discuss how this procedure is made tractable or report runtime/scaling behavior in the main text (Figure 11 on scalability is deferred to the appendix).

### Trivial

- The notation `Uℐ` appears in Algorithm 1 and should be `∪ℐ` (union of intervention targets).
- The `F-PAG` edge list in Definition 5 contains repeated entries (e.g., `○---○` listed multiple times), suggesting a formatting issue.

## Nice-to-Haves

- An ablation study on data *without* post-treatment selection to confirm F-FCI does not degrade when selection is absent.
- A quantitative real-world evaluation table with precision/recall against known regulatory relationships or pathway enrichment scores.
- A discussion of computational complexity or empirical runtime in the main text.
- Clarifying whether the selection mechanism can depend on latent variables or only on observed ones (the current model assumes at least two observed parents of S).

## Removed Points

- **"Experimental comparison is not informative because baselines are not designed for the problem"** — Removed. Showing that existing methods fail under post-treatment selection while the proposed method succeeds IS the informative comparison. This asymmetry is standard and valid: the baselines are the state of the art, and the paper demonstrates they cannot handle this setting. The ablation concern is retained separately.
- **"Step 2.1 is computationally exponential and practically infeasible"** — Demoted from Major to Minor. Constraint-based methods universally use greedy search strategies for adjacency deletion; the lack of explicit search strategy discussion is a minor oversight, not a fatal flaw, as the standard FCI adjacency search (which the paper cites) can be applied.
- **"The paper does not discuss the selection variable modeling assumption"** — Removed. The paper explicitly states "we assume selection works on at least two observed variables" (Section 2.1), which is a deliberate scope choice, not an omission.
- **"The algorithm's reliance on faithfulness may be more problematic under selection"** — Demoted to Nice-to-Have. Faithfulness is a standard assumption in constraint-based causal discovery. A brief discussion would be nice but is not a weakness.
- **"Missing related works"** — Removed per instructions (cannot verify from external sources).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Fix Step 2.2 of Algorithm 1** — replace each identical `(⊥,⊥,⊥,⊥)` condition with the actual CI pattern that triggers each orientation. A dedicated table mapping the six (or more) CI patterns to edge orientations would make the algorithm implementable and verifiable.
2. **Define all edge marks formally in Definition 5** — the △ and ▲ marks used in Step 2.3 updates must be included in the formal definition of F-PAG.
3. **Add ablation experiments** — specifically, run F-FCI while ignoring post-treatment selection (treating selection as pre-treatment) and without Step 2.3, and test on data without selection to verify no degradation.
4. **Add real-world quantitative results** — report precision/recall or enrichment-based metrics against known ground truth in the main text.
5. **State the completeness condition in Theorem 4** — explicitly note that completeness holds conditional on the availability of hard interventions on Type I inducing nodes.

## Score and Decision

**Round 1 bracket (wide):** between 3.5 and 7.0. The weak anchor (5AJ8R4z5g0, score 3.25, a rejected CATE paper) is clearly weaker — its problem is well-studied and the contribution is incremental. The strong anchor (xByvdb3DCm, score 8.00, "When Selection meets Intervention") addresses pre-treatment selection from the same research group with a perfectly clean execution. This paper is closer to the middle but below the strong anchor due to the algorithm specification gap and missing ablations.

**Round 2 narrow (within bracket):** Compared to two accepted 6.0 anchors (BZYIEw4mcY — efficient causal discovery with latents; fGhr39bqZa — homologous surrogates), both have presentation issues and limited experiments but were accepted based on solid theoretical contributions. The current paper has a similarly novel theoretical contribution but with a more significant specification gap (the broken pseudocode) and weaker real-world validation, placing it slightly below these anchors. Compared to a 5.5 rejected anchor (x2rZGCbRRd — post-treatment covariates), the current paper has a stronger theoretical contribution (soundness+completeness vs. a method paper) but similarly incomplete evaluation.

**Final score: 5.0.** The paper identifies a genuinely novel problem and provides a theoretically grounded framework. However, the algorithm specification is incomplete (broken pseudocode, undefined notation), the experimental evaluation lacks ablations to isolate the claimed contribution, and the real-world validation is not quantitatively supported in the main text. These are significant enough gaps that the paper cannot be accepted in its current form, though the core contribution merits a resubmission after addressing the issues.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>