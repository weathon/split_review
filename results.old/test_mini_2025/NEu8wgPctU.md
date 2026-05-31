Now I have sufficient calibration data. Let me synthesize the final review.

## Round-1 bracket: between the anchor at ~5.0 (rejected world model / autonomous driving papers) and ~7.0 (accepted world model / autonomous driving paper). I place the paper initially in the 5–7 range.

## Round-2 narrowing: Comparing against p01BR4njlY (5.75, accepted poster — similar-level contribution with some experimental concerns), HN0CYZbAPw (6.5, accepted poster — RL finetuning with clean experiments), and dgb4rfPzaw (5.0, rejected — insufficient baselines), AdaWM sits between 5.0 and 6.0. It has a stronger theoretical contribution than typical 5.0 papers but weaker experimental rigor than typical 6.5+ papers. I narrow to **5.5**.

Here is the final consolidated review:

---

## Summary

This paper proposes AdaWM, an adaptive world-model-based planning method for autonomous driving that addresses performance degradation during online finetuning. The key idea is to identify whether a dynamics model mismatch or a policy mismatch is the dominant cause of performance drop, then selectively finetune only the problematic component using efficient low-rank updates (LoRA-based for the model, sub-unit convex combination for the policy). The paper provides a theoretical bound on the performance gap (Theorem 1) and validates the approach on CARLA driving tasks, reporting consistent improvements in time-to-collision and success rate over several baselines.

## Strengths

- **Novel adaptive finetuning framework for world model RL.** The paper identifies a practical problem (performance degradation during finetuning due to distribution shift) and proposes a principled approach: identify which mismatch dominates and update accordingly. This is a genuinely useful formulation that goes beyond fixed finetuning schedules (model-only, policy-only, alternating). The motivating example in Figure 1 makes the problem intuitive.

- **Theoretical analysis of the performance gap.** Theorem 1 derives an upper bound decomposing performance degradation into dynamics model mismatch terms (ℰₚ, ℰₘₐₓ) and policy mismatch (ℰ_π). This decomposition provides a conceptual foundation for the adaptation strategy. While the mapping to practice is simplified, the theoretical framing is a strength the paper's competitors lack.

- **Consistent and substantive empirical gains.** On all four CARLA evaluation tasks, AdaWM achieves the highest or second-highest success rate and time-to-collision (Table 2 vs. DreamerV3, VAD, UniAD). More importantly, Table 3 shows AdaWM outperforming alternative finetuning strategies (model-only, policy-only, alternating) on the same base architecture. For example, on ROM03: AdaWM TTC 2.05 / SR 0.82 vs. Model-only TTC 0.95 / SR 0.60.

- **Diagnostic evidence supports the mechanism.** Figure 4 tracks TV distances during finetuning and shows that fixed strategies cause the *other* mismatch to grow (e.g., model-only finetuning increases policy mismatch), while AdaWM keeps both mismatches low. This provides direct evidence that the adaptation decisions are sensible.

- **Robustness across a range of hyperparameter C.** Table 4 shows strong performance for C between 2 and 50, with degradation only at extreme values (0.5 or 100). This suggests the method does not require precise tuning despite the threshold being a simplification of the theoretical constants.

## Weaknesses

### Major

- **No statistical reporting.** No standard deviations, confidence intervals, or number of random seeds are reported in any table or figure. Given the well-known variance of CARLA evaluations, the reader cannot assess whether the reported advantages (especially the modest ones, e.g., LTM03 TTC: Model-only 1.39 vs. AdaWM 1.32) are consistent or within noise. This is the single most significant weakness and substantially undermines confidence in the results. The paper should report results over ≥3 seeds with appropriate variance metrics.

### Minor

- **Theory-to-practice gap in the adaptation rule.** Theorem 1 yields a criterion involving constants C₁ and C₂ derived from problem parameters (γ, rₘₐₓ, Γ, etc.). In the algorithm, this is replaced by a single scalar threshold C comparing TV distances, and the paper states C is "a function of C₁ and C₂" but never specifies the mapping. This makes the adaptation rule effectively a heuristic whose connection to the theory is asserted but not operationalized. The ablation (Table 4) confirms C requires task-specific tuning (optimal C differs across tasks: ROM03 best at C=10, RTD12 best at C=5), weakening the claim of theory-grounded adaptation.

- **Table 2 comparison is framed as headline results but conflates finetuning vs. no finetuning.** The paper compares AdaWM (with online finetuning) against VAD, UniAD, and DreamerV3 (without finetuning, as the paper acknowledges on lines 205-206). While the paper includes the fair comparison in Table 3, the abstract and introduction do not clearly separate the two comparisons, and a reader could be misled into attributing the gains in Table 2 to the *adaptive* strategy specifically, rather than to finetuning in general.

- **Baseline finetuning strategies underspecified.** Table 3 compares AdaWM against model-only, policy-only, and alternating finetuning, but it is unclear whether these baselines use the same low-rank update mechanisms (LoRA, sub-unit decomposition) as AdaWM. If the baselines use full finetuning while AdaWM uses parameter-efficient methods, the comparison conflates the adaptation strategy with the update mechanism. The paper should control for this.

### Trivial

- **Algorithm 1 notation is cryptic at first glance.** Lines 5 and 7 (B' ← B, φ_t = (B'Z)ᵀΦ and Δ' ← Δ, ω_t = (Δ')ᵀΩ) are explained in the text but not in the algorithm itself, making the pseudocode hard to parse without cross-referencing.

- The paper derives the bound under specific RNN assumptions (chosen f_h, f_z with Lipschitz activations) but the practical DreamerV3 architecture uses a more complex dynamics model. Whether the bound's assumptions hold in the experimental setting is not discussed.

## Nice-to-Haves

- An empirical analysis of when mismatch identification works well and when it might fail (e.g., both mismatches large and equally important) would strengthen the paper.
- Demonstrating generalization to a non-driving domain (e.g., a standard DMControl or Atari task) would broaden the contribution's impact.

## Removed Points

- **"Comparisons with VAD/UniAD are unfair because those methods are trained on Bench2Drive while AdaWM is pretrained on only one task."** The paper acknowledges this asymmetry and the baselines are used as provided by their authors. This is a reasonable design choice for comparison, not a flaw.

- **"The algorithm description is completely opaque and hinders reproducibility."** The paper explains the low-rank updates and sub-unit decomposition in Section 2.2's text. The algorithm steps, while terse, are cross-referenced to this explanation. Overstating this as a fatal flaw is unwarranted.

- **"Missing related work discussion on meta-learning and online adaptation."** The related work section cites relevant finetuning strategies (Feng et al., Baker et al., Hansen et al.) organized by the taxonomy in Table 1. While additional coverage is possible, this is a judgment call and not a clear weakness. (Per instructions, do not mention missing related works.)

- **"The bound derivation is relegated to an appendix (not available)."** The appendix was stripped by the parser, not omitted by the authors. This cannot be held against the paper.

## Novel Insights

The harsh critic correctly identifies that the paper's core claim — that the *adaptive* decisions (not just finetuning in general) drive the improvement — is not fully separated from confounds. The most interesting observation from combining the two reviews is that the diagnostic evidence (Figure 4) is actually the paper's strongest piece of support for the adaptive mechanism, yet it receives less emphasis than the headline Table 2 results. The paper would be more convincing if it reframed the narrative around the diagnostic evidence and Table 3, rather than leading with the potentially misleading Table 2 comparisons. The moderate hyperparameter sensitivity (optimal C varying by task) is also a notable practical limitation that is under-discussed.

## Suggestions

1. Report all results over ≥3 random seeds with standard deviations. This is the single most impactful change.
2. Clarify the relationship between Theorem 1's constants (C₁, C₂) and the implemented threshold C, or honestly reframe the adaptation rule as a heuristic inspired by the theory.
3. Specify whether the model-only and policy-only baselines use the same low-rank update mechanisms as AdaWM. If they do not, add a controlled comparison.
4. Restructure the narrative to give Table 3 (finetuning strategies comparison) more prominence and treat Table 2 as a secondary "overall system" comparison.
5. Add a brief discussion of limitations: cases where mismatch identification could fail and the computational cost of estimating TV distances from limited online samples.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>

**Calibration anchors:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| fd2u60ryG0 (LAW — world model for AD) | 7.00 | R1 moderate | Stronger empirical breadth (3 benchmarks), accepted. AdaWM is slightly weaker due to no error bars. |
| HN0CYZbAPw (WSRL — RL finetuning) | 6.50 | R1 moderate | Cleaner experiments and clearer analysis, accepted. AdaWM has comparable contribution but weaker rigor. |
| SXMTK2eltf (GPT-Driver — AD) | 5.00 | R1 moderate | Rejected for low novelty. AdaWM has stronger novelty/theory. |
| RN7RzMxwjC (HarmonyWM — world models) | 5.00 | R1 moderate | Rejected for limited baselines/tasks. AdaWM is stronger on both fronts. |
| p01BR4njlY (Adapting video knowledge) | 5.75 | R2 narrow | Accepted poster with concerns about experimental thoroughness. AdaWM similar level. |
| dgb4rfPzaw (World-simulation perception) | 5.00 | R2 narrow | Rejected for insufficient baselines. AdaWM has stronger evaluation. |

Final bracket: lower bound 5.0 (rejected-level papers), upper bound 7.0 (accepted-level). Narrowed to ~5.5, below the typical acceptance threshold, due to the lack of statistical rigor being the primary barrier to acceptance.