Now I have enough information. Let me compose the consolidated review.

## Summary

The paper formalizes the all-day multi-scenes lifelong VLN (AML-VLN) problem and proposes Tucker Adaptation (TuKA), which represents multi-hierarchical navigation knowledge as a 4th-order tensor using Tucker decomposition to decouple shared core skills from scene- and environment-specific experts. A decoupled knowledge incremental learning (DKIL) strategy is introduced to consolidate shared subspaces while constraining specific experts. The resulting agent, AllDayWalker, is evaluated on a 24-task benchmark spanning 7 scenes and 4 environments, achieving 65% average SR vs. 44% for the best baseline (BranchLoRA), with an 11% average forgetting rate.

## Strengths

1. **Problem formalization.** The paper defines AML-VLN, a realistic setting where VLN agents must continually learn across diverse scenes and visual conditions while mitigating catastrophic forgetting. This goes beyond single-task or single-environment adaptation studied in prior LoRA/MoE-LoRA work (Section 2).

2. **Tucker Adaptation (TuKA) for high-order tensor representation.** TuKA uses a 4th-order tensor with Tucker decomposition (Equation 2) to explicitly decouple shared navigation skills (core tensor G) from scene experts (U³) and environment experts (U⁴) (Section 3.2). This is a principled structural advance over matrix-based LoRA and two-hierarchical MoE-LoRA variants, and the tensor-matrix alignment (Equation 3) that reduces the high-order representation to a 2D weight matrix for LLM integration is technically clever.

3. **Strong empirical results.** AllDayWalker achieves 65% average SR across 24 tasks, outperforming the best baseline (BranchLoRA, 44%) by 21 percentage points while maintaining the lowest average forgetting rate (11% vs. 36%) (Tables 1, 2). The results are consistent across SR, SPL, and OSR metrics (Figure 7).

4. **Controlled ablation validating the decoupled tensor design.** Figure 8 shows that the 4th-order tensor (scene and environment as separate modes) consistently outperforms a 3rd-order tensor (coupled scene-environment expert set) across all 20 tasks, providing direct evidence for the benefit of the decoupled multi-hierarchical representation (Section 5.3).

5. **AllDay-Habitat simulation platform.** The paper extends Habitat with three physically-based imaging models (scattering via Equation 10, low-light via Equation 11, overexposure via Equation 12) to support the new benchmark (Section 4), a useful infrastructure contribution.

## Weaknesses

### Fatal
None.

### Major

1. **The tensor structure requires a fixed, pre-specified set of scenes and environments.** The tensor dimensions are ℝ^{a_l × b_l × M × N} where M=7 scenes and N=4 environments are fixed before training. Factor matrices U³ ∈ ℝ^{M×r₃} and U⁴ ∈ ℝ^{N×r₄} cannot accommodate a new scene or environment type without redefining the entire tensor and retraining. The paper presents no mechanism for dynamic expansion. While many continual learning methods operate with a fixed set of classes, the paper's "lifelong" framing and claim of suitability for open-world deployment conflict with this structural constraint. This limits the method's applicability to settings where the scenario space is fully known in advance.

2. **The forgetting metric (F-SR) has ambiguities that undermine parts of the analysis.** The paper defines M-SR_t as performance from joint training on tasks 1 through t, with the footnote "t ≤ 20" (Eq. 13 caption). Yet F-SR values are reported for T1–T24 (Table 2), including T21–T24 where M-SR_t is never defined for t > 20. All methods show 0% F-SR on T24 — if this is computed from M-SR₂₀, the metric is applied inconsistently. AllDayWalker also shows negative forgetting on T14 (-3%) and T20 (-4%), which is possible but unexplained. The paper should clarify how F-SR is computed for t > 20 and explain anomalous values.

3. **The generalization evaluation protocol for baselines is underspecified.** Table 5 evaluates AllDayWalker on six unseen scenarios where it uses CLIP similarity to retrieve the most similar scene/environment expert. The paper does not describe how the baselines (BranchLoRA, SD-LoRA) select or compose experts for these unseen scenarios. If baselines lack a comparable retrieval mechanism, the comparison is biased in favor of the proposed method. This needs clarification, or the baselines should be equipped with the same CLIP-based retrieval capability for a fair comparison.

### Minor

4. **Missing controlled ablation isolating the tensor contribution.** The paper claims tensor representation is inherently superior for multi-hierarchical knowledge, but no comparison is made against a method that also decouples scene and environment knowledge without using tensors — e.g., two separate LoRA adapters (one per hierarchy) combined additively or gated. Without this control, the improvement could partly stem from having more adaptation parameters or from the DKIL regularization, rather than from the tensor structure itself.

5. **No hyperparameter sensitivity analysis for λ₁, λ₂, λ₃.** The DKIL loss has three balancing coefficients (λ₁=0.2, λ₂=0.2, λ₃=0.1) controlling EWC, consistency, and orthogonality respectively. No ablation shows how performance varies with these values, making it unclear how robust the method is to this choice.

6. **The orthogonality constraint (Eq. 8) is a strong assumption without analysis.** The loss forces each new expert row to be orthogonal to all previously learned experts. This could be harmful when two scenes share visual features (e.g., two kitchens under different environments). The paper does not analyze whether this constraint ever forces apart expert representations that should be similar.

### Trivial
- The benchmark uses 4 visual conditions (normal, low-light, overexposure, scattering). While these are common degradation types, the "all-day" framing is aspirational and the connection to actual 24-hour lighting is not established. Minor naming overclaim.

## Nice-to-Haves
- Evaluate performance when the tensor is incrementally expanded (adding new rows to U³/U⁴) to simulate truly open-ended lifelong learning.
- Visualize expert embeddings (e.g., UMAP of scene/environment expert rows) to verify that the decoupled representation learns meaningful clusters.
- Report standard continual learning summary metrics (average accuracy, forward/backward transfer) in addition to per-task SR and F-SR.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The paper does not include code or video links accessible in review."** — The paper explicitly states "Code and video demos are available at: https://ganvin-li.github.io/AllDayWalker/." Removed per hard rule.
- **"The tables are garbled in the parsed text."** — Parser artifact, not an author error. Removed per hard rule.
- **"Appendix: Referenced but not available."** — The parser strips appendices from all papers; they exist in the original submission. Removed per hard rule.
- **Criticism that "all-day" is an overclaim because only four environments are tested.** — The paper explicitly scopes to these four common visual conditions (normal, low-light, overexposure, scattering). "All-day" is an aspirational term consistent with standard ML naming conventions; downgraded to trivial.
- **Speculation that the orthogonality constraint "may conflict with shared subspace learning."** — This is a hypothetical concern without evidence from the paper that such conflict actually occurs. Retained as minor weakness (#6) in a grounded form, but the speculative language is removed.
- **"HydraLoRA and BranchLoRA already have structure for shared-specific decoupling; the paper does not explain why more than two levels are necessary."** — The paper does explain this: "knowledge spans multiple hierarchical levels: core navigation skills, scene-specific knowledge, and environment-specific knowledge. These methods represent all knowledge within two hierarchical matrices" (Section 3.1, pg 4). The critic's point misreads the paper.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the tension between the paper's "lifelong" framing and the fixed-tensor implementation, but this is a gap between aspiration and execution rather than a novel observation.

## Suggestions

1. **Clarify the F-SR computation for tasks t > 20** where M-SR_t is not defined. Specify whether F-SR for T21–T24 is computed using M-SR₂₀ or some alternative, and explain the negative F-SR values (T14, T20).
2. **Address the fixed-tensor limitation** either by proposing an incremental expansion mechanism (appending rows to U³/U⁴ and expanding the core tensor) or by transparently acknowledging this as a scope limitation requiring future work.
3. **Add a controlled ablation** comparing TuKA against a dual-LoRA baseline that decouples scene and environment knowledge without tensors, to isolate the benefit of the tensor structure itself.
4. **Document the baseline inference protocol** for the generalization experiments (Table 5). If baselines were not given expert retrieval, either provide it or acknowledge the asymmetry.
5. **Include sensitivity analysis** for λ₁, λ₂, λ₃, and analyze the effect of the orthogonality constraint on expert similarity.
6. **Report parameter counts** for all methods to verify that TuKA's advantage is not primarily from having more trainable parameters.

## Score and Decision

The paper presents a novel tensor-based adaptation method, a well-motivated problem formulation, and strong empirical results across a substantial benchmark. The core contribution (TuKA) is technically interesting and the ablation comparing 3rd vs. 4th order tensors directly validates the decoupled design. However, three issues are significant — the fixed-tensor limitation conflicting with the "lifelong" framing, ambiguities in the forgetting metric computation for tasks beyond t=20, and the underspecified baseline protocol for generalization experiments. These require substantial clarification and potential methodological adjustment, but they do not invalidate the paper's central contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>