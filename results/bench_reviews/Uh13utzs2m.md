Now I have a thorough understanding of the paper and calibration anchors. Let me write the final review.

## Summary

This position paper argues that continual learning (CL) research has over-focused on incremental classification, limiting both theoretical development and practical applicability. Through four concrete examples—multi-target classification (iCaRL's combinatorial explosion), robotics with manifold constraints (EWC's parameter proximity ≠ functional proximity), continuous task spaces (KD's failure to spatially vary regularization), and abstract concept memorization (coresets cannot compress strategic counterfactuals)—the paper demonstrates how specific CL methods fail when assumptions of discrete classes, Euclidean metrics, symmetric similarities, and task boundaries are violated. It identifies three conceptual challenges (C1: continuity, C2: spaces/metrics, C3: objectives) and provides recommendations for each.

## Strengths

- **Technically grounded, method-specific demonstrations of failure**: The paper targets specific, canonical CL methods (iCaRL, EWC, KD, coresets) rather than making vague complaints. The iCaRL combinatorial explosion argument (2^N clusters for N Action Units, yielding 4.3×10^9 clusters for N=32) is concrete, quantitative, and follows directly from Equation (1). The EWC manifold-constraint argument (Eq. 2: parameters close in Fisher-weighted distance may violate safety constraints on the output manifold) identifies a genuine principle-level failure, not just an implementation gap. These analyses make the critique substantive and falsifiable.

- **The asymmetric divergence analysis in Section 3.2 is excellent**: The two-Gaussian example (KL divergences of 2.8 vs. 20.5 bits in opposite directions) is a concrete, counterintuitive illustration that directly supports the non-obvious claim that "how informative is task A about task B" differs from the reverse. This has immediate practical implications for task identification and buffer comparison, and the recommendation to "compare both directions on toy examples with large distances" is actionable and non-trivial.

- **Clear position of genuine contemporary interest**: The central claim is easily summarized in one sentence and is highly relevant to the CL community, where incremental classification remains the dominant evaluation paradigm. The position invites productive disagreement—particularly the question of whether the research program has structural limitations or merely needs wider evaluation.

- **Effective use of the "spaces" taxonomy**: The three-space framework (parameter/data/function) with the analysis of metric choices provides a useful conceptual scaffold. The recommendation to "patch broken methods by switching spaces" (Section 3.2 Rec #3) is practical and concrete—e.g., re-expressing joint-angle outputs as end-effector poses via a kinematics model.

- **Thoughtful, if brief, engagement with counterarguments**: Section 4 addresses the most natural objection—that fundamental problems like stability gap should be solved in classification first—and offers a reasonable response: that overreliance on classification risks producing task-specific solutions even when more general ones exist.

## Weaknesses

### Fatal
None.

### Major

- **Conflation of implementation failures with principle-level failures weakens the argument's force**: The paper never systematically distinguishes between failures that are tautological (iCaRL's class-based buffer doesn't work without classes—of course it doesn't) and failures that reveal deeper structural limitations (EWC's implicit assumption that parameter proximity implies functional proximity breaks under manifold constraints). If only implementations fail, the position reduces to "also develop methods for other settings"—already happening and trivially correct. If principles fail, the much stronger claim that the research program has structural limitations is supported. The paper contains examples of both (Section 2.2 approaches principle-level failure; Section 2.1 mixes principle-level combinatorial explosion with implementation-level "iCaRL needs classes"), but never draws this distinction explicitly. This ambiguity leaves the reader uncertain of the paper's true claim and its burden of proof.

- **Insufficient engagement with existing beyond-classification CL work**: The paper cites but does not analyze why existing work on continual RL, continual generation, continual dense prediction, and continual robotics learning (e.g., Daab et al. 2024) has not already addressed the identified gaps. If there is already a thriving sub-community doing continual RL and continual robotics, the paper's position implicitly claims this isn't happening enough or isn't working—but it never explains *why* the field converged on classification. Understanding the convergence (standardization? reproducibility? benchmark availability? difficulty?) matters for the prescription. Without this analysis, the recommendation to "move beyond" risks ignoring the real methodological reasons for the field's focus.

### Minor

- **Recommendations in Section 3.3 (Objectives) are underspecified**: The three recommendations—"consider generation for avoiding forgetting" (generative replay dates to Robins 1995), "consider densities for task identification" (standard OOD detection literature), and "consider the energy-based model connection" (Grathwohl et al. 2020)—are either well-known ideas or too high-level to guide research direction. Unlike Section 3.2, which offers concrete advice like "compare both KL divergence directions," Section 3.3 provides considerations without articulating what acting on them would change about CL method design.

- **The key insight about spatially-varying regularization is dropped too quickly**: Section 2.3 observes that "it is necessary that the function be regularized to different degrees in different regions"—that regularization strength should vary spatially, not just temporally. This is a genuine and non-obvious conceptual contribution that emerges naturally from the continuous-task-space analysis but receives only two sentences of development. It deserves substantial expansion as it points toward a genuinely new research direction.

- **The title/abstract framing ambiguity**: The title says "Move Beyond" (suggesting replacement/de-emphasis) while the abstract says "broaden the scope" (suggesting addition). Section 4 partially addresses this by acknowledging the utility of incremental classification, but the paper never fully commits to which position it holds. These are different claims with different burdens of proof: the stronger reading requires showing classification-focused work is actively harmful; the weaker reading is harder to argue is controversial.

### Trivial
- The cross-entropy/EWC curvature interaction (end of Section 2.1) is asserted in a single sentence without development—this potentially interesting point about loss geometry and regularization deserves either expansion or removal to avoid dangling claims.

## Nice-to-Haves

- A deeper analysis of the relationship between the multi-target classification explosion (Section 2.1) and the metric-choice discussion (Section 3.2): moving from discrete clusters to continuous spaces is directly connected, but the paper doesn't draw this connection explicitly.
- Expansion of the spatially-varying regularization insight from Section 2.3, which could be one of the paper's most generative contributions.
- A brief analysis of why classification benchmarks became dominant (reproducibility? standardization? simplicity?) and how these advantages can be replicated in broader settings—this would address the "classification benchmarks provide standardized comparison" counterargument that the paper currently omits.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Overclaiming/strong framing" criticism**: The harsh critic noted the gap between strong framing ("move beyond") and moderate delivery. While the framing ambiguity is real, this is not overclaiming—position papers are allowed and expected to make strong claims. The issue is that the paper doesn't clearly commit to one reading, not that its claims are too strong. Kept as a minor framing issue rather than a major overclaim.

- **Demand for empirical validation of the position**: The harsh critic implies the paper would be stronger with empirical demonstrations. This is a position paper using reasoning and mathematical analysis of method formulations—empirical results are optional and not needed to support arguments that follow from the methods' own equations.

- **"Zergling rush example is thin"**: While Section 2.4 is the weakest example section, the coreset formulation (Eq. 4) combined with the observation that rare strategic counterfactuals contribute little to total gradients does constitute a principled argument. The references to NELL and biological memory systems are supporting citations, not the core argument. Kept as a minor gap (abstract-to-concrete bridge) rather than a major weakness.

- **Criticisms of "choose the correct metric" as tautological**: While literally true that one always intends to choose the correct metric, the recommendation in context includes concrete sub-recommendations (check for asymmetry, consider switching spaces, be explicit about what Euclidean metric assumes). The heading is vague but the content is not entirely vacuous. Subsumed into the Section 3.3 weakness about underspecification.

## Novel Insights

The paper's most novel insight is the identification that spatially-varying regularization—where regularization strength should differ across input regions, not just across time—is necessary in continuous task spaces. This emerges naturally from the box-pushing example (well-explored regions of weight-distribution space should be regularized more strongly than sparsely sampled regions, where some "forgetting" is desirable to allow improvement) but receives almost no development. If expanded, this could constitute a genuinely new theoretical direction for CL, as current methods uniformly regularize across all past data.

## Suggestions

- Explicitly categorize the four example failures into "implementation-level" vs. "principle-level" failures, and use this categorization to sharpen the position claim. At minimum, state clearly: "of these four failures, X are principle-level and Y are implementation-level; the existence of X principle-level failures supports the strong reading of our position."

- Expand the spatially-varying regularization observation (Section 2.3, lines around the box-pushing example) from two sentences to a dedicated paragraph or subsection. This is the paper's most generative direction and treating it as a passing observation undersells it.

- Add a paragraph in Section 4 or the Introduction analyzing why the field converged on incremental classification (reproducibility, standardization, benchmark availability) and how these advantages might be replicated in broader settings, or why they cannot be.

## Calibration Anchors

| Paper | Avg Score | Comparison |
|-------|-----------|------------|
| `yqKfMr0yvY.md` (LLM-as-judge critique) | 7.67 | Stronger theoretical framework (measurement theory), more comprehensive and novel conceptual lens. Our paper's critique is comparable in targeting specific methods but less novel in its theoretical framing. |
| `5X4GDSUumr.md` (No champions in TSF) | 7.0 | Much more thorough empirical evidence (3500+ networks). Our paper has no empirical component but compensates with mathematical analysis of method formulations. |
| `BXLRMWLDQw.md` (Adversarial ML not progressing) | 6.33 | Similar pattern: six detailed case studies of method failures, clear framework, but ultimately still rejected despite strong analysis. Our paper has similar depth but fewer case studies. |
| `vFae5rRman.md` (Benchmarking is broken) | 6.0 | Had a concrete prototype (PeerBench) making recommendations actionable. Our paper's recommendations are less concrete, placing it below this anchor. |
| `NHDOjeVMb5.md` (Embeddings should capture implicit semantics) | 5.67 | Similar profile: good critique with pilot study, recommendations not novel enough. Our paper is comparable but has stronger technical analysis. |
| `cIbQaSXqYm.md` (MOS insufficient) | 5.0 | Similar pattern of strong critique with underspecified recommendations. Our paper has more technically grounded demonstrations. |
| `R6TXwNF1SB.md` (Six pillars of AGI) | 3.0 | Truly vague and incoherent argument. Our paper is clearly above this—its arguments are specific and falsifiable. |
| `FJF1sa6elQ.md` (Model multifacetedness) | 3.33 | Framework is conceptual with limited actionable steps. Our paper has more concrete technical content. |

Our paper sits above the medium-scoring paradigm-critique papers (5.0-5.67 range) because its technical demonstrations of method failure are concrete, mathematical, and directly derived from the methods' own formulations. It sits below the high-scoring papers (6.33-7.67) because its recommendations are less developed and it lacks a novel theoretical framework comparable to measurement theory or a concrete implementation like PeerBench. The two major weaknesses (implementation/principle conflation, insufficient engagement with existing beyond-classification work) prevent it from reaching the 6+ range.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>