Now I have enough information to write the consolidated review. Let me synthesize everything.

## Summary

This paper formalizes the All-Day Multi-Scenes Lifelong Vision-and-Language Navigation (AML-VLN) problem and proposes Tucker Adaptation (TuKA), a method that represents multi-hierarchical navigation knowledge (spanning scenes and environments) as a fourth-order tensor. TuKA uses Tucker decomposition to decouple knowledge into shared subspaces (core tensor, encoder, decoder) and scenario-specific experts (scene and environment factor matrices). The paper further presents a Decoupled Knowledge Incremental Learning (DKIL) strategy with inheritance, elastic weight consolidation, consistency, and orthogonal constraints to mitigate forgetting. Building on TuKA, the AllDayWalker agent is developed and evaluated on a 24-task benchmark (20 simulated + 4 real-world), including an extended Habitat simulator with physically grounded degradation models (low-light, scattering, overexposure). Results show AllDayWalker achieves 65% average SR (vs. 50% for the best baseline SD-LoRA) with 11% average forgetting.

## Strengths

1. **Novel use of high-order tensor representation for multi-hierarchical knowledge**: TuKA explicitly decouples scene knowledge (U³ factor matrix) and environment knowledge (U⁴ factor matrix) via a fourth-order tensor with Tucker decomposition, while matrix-based methods (LoRA, MoE-LoRA) are limited to two-hierarchical representations. The ablation in Figure 8 shows fourth-order tensors consistently outperform third-order tensors across all 20 tasks, empirically supporting the benefit of decoupling.

2. **Strong empirical performance on a comprehensive benchmark**: AllDayWalker achieves 65% average SR across 24 tasks, substantially outperforming the best baseline SD-LoRA (50%) and BranchLoRA (44%) — a 15-21 percentage point improvement (Table 1). The agent also achieves 55% SR on unseen scene-environment combinations vs. 39-40% for baselines (Table 5), demonstrating generalization.

3. **DKIL strategy with technically sound design**: The decoupled learning strategy combines knowledge inheritance, elastic weight consolidation on shared subspaces, consistency constraints on expert rows, and orthogonal constraints for new expert exploration. Table 3 validates the importance of sharing the core tensor and encoder, confirming the design rationale.

4. **New benchmark contribution**: The paper extends Habitat with three physically grounded imaging models (atmospheric scattering, low-light noise, overexposure saturation) to create the AllDay-Habitat simulation platform, providing a concrete testbed for lifelong VLN under diverse conditions across 24 tasks spanning 5 simulated and 2 real-world scenes.

## Weaknesses

### Fatal

None.

### Major

1. **Forgetting metric (F-SR) computation is underspecified and produces anomalous negative values**: The forgetting rate is defined as (M-SR_t − SR_t) / M-SR_t, where M-SR_t is "the performance obtained when training solely on navigation tasks 1 through t." Table 2 reports *negative* forgetting for AllDayWalker on T14 (−3%) and T20 (−4%), meaning the sequential lifelong agent outperforms the multi-task joint-training baseline. The paper does not explain how M-SR_t was computed (training budget, optimizer settings, number of steps). If the multi-task baseline is trained with a fraction of the total gradient steps that the lifelong agent receives across all tasks, then M-SR_t is not a proper upper bound and all forgetting rates in the paper may be underestimated. This does **not** invalidate the SR results (Table 1), which are the primary evidence, but it undermines the specific claim of "only 11% forgetting." The authors must clarify the M-SR_t training protocol and explain or remedy the negative values.

2. **No variance reported across task orders or random seeds**: The Figure 6 caption states "the order of tasks is randomized," yet all results are reported for a single order with no standard deviations or confidence intervals. Lifelong learning results are highly sensitive to task order, and the large per-task SR fluctuations (e.g., T2 at 23% vs. T7 at 87%) suggest order effects could be substantial. Without variance across multiple runs (at least 3 seeds/orders), it is impossible to assess whether the reported improvements are statistically robust.

3. **TTA baselines (FSTTA, FeedTTA) are not lifelong methods**: These methods perform temporary test-time adaptation within a single episode and do not retain knowledge across tasks. While the paper does state they "perform small, temporary adaptation during test time," including them in the main comparison table alongside lifelong methods (without a clear asterisk or separation) inflates the apparent superiority of AllDayWalker on the forgetting dimension. They should be either removed from the lifelong comparison or clearly repositioned as non-lifelong lower-bound references with explicit caveats.

### Minor

1. **No ablation of individual DKIL loss terms**: The DKIL loss (Eq. 9) has four components: the main navigation loss, EWC on shared subspaces (L_sk), consistency on expert rows (L_co), and orthogonal constraint on new experts (L_es). Table 3 ablates shared components but never ablates the individual loss terms. Which term contributes most to forgetting reduction? Without this, the method appears over-engineered and the contribution of each component is unclear.

2. **CLIP-based expert retrieval accuracy is not evaluated**: Section 3.4 describes storing CLIP features during training and retrieving the closest scene/environment expert via cosine similarity during inference. For unseen scenes (Table 5), the retrieval must pick the nearest *known* scene. The paper does not provide a confusion matrix or accuracy analysis of this retrieval mechanism, which is critical for understanding when the method succeeds or fails.

3. **No discussion of limitations**: The paper does not include a limitations section. Key limitations include: (a) task-id is seen during training, which may not hold in fully autonomous deployment; (b) the environment dimension is unbalanced across real-world scenes (only 2 environments vs. 4 for simulated); (c) the CLIP-based retrieval may fail when visual domain gaps are large.

4. **Missing confidence intervals on main results**: None of the tables report standard deviations or confidence intervals. While single-run evaluation is common in the VLN literature, given the per-task fluctuations, at least a note about the stability of results across runs would be informative.

### Trivial

None beyond what is listed in Removed Points.

## Nice-to-Haves

- A parameter/efficiency comparison table across methods showing actual trainable parameter counts.
- Analysis of how well the CLIP-based expert retrieval works (e.g., confusion matrix of retrieved experts for seen and unseen scenarios).
- Ablation of individual loss terms (EWC vs. consistency vs. orthogonal) in the DKIL strategy.

## Removed Points

- **"Third-order vs fourth-order comparison design is enforced"**: The critic claims that the third-order baseline could be constructed differently and that the conclusion is trivial. However, the comparison in Figure 8 is valid: it tests whether decoupling scene and environment into separate modes (fourth-order) is better than coupling them into one mode (third-order). This is a meaningful empirical question, and the paper's design is the natural one. **Removed** — not a real weakness.

- **"Missing non-LoRA lifelong methods (L2P, DualPrompt, rehearsal)"**: The paper explicitly scopes its comparison to parameter-efficient adapters, which is a valid and well-defined scope. The title and contributions are about adapting LLMs for lifelong VLN, not about comparing all lifelong learning paradigms. **Removed** — scope creep.

- **"Claim about LoRA variants being inherently limited is asserted not demonstrated"**: The paper provides reasoning (two-matrix form cannot capture multi-hierarchical knowledge) and empirical validation (Table 1, Figure 8). **Removed** — not a factual weakness.

- **Formatting/style nitpicks**: Various minor presentation concerns about parameter details being deferred to appendix, etc. These are standard practices and not weaknesses. **Removed**.

- **Negative forgetting is "impossible"** (framed as fatal): The critic says negative forgetting is impossible, but this is overstated. Negative forgetting can arise from multi-task baselines being undertrained (same total gradient budget spread across more tasks) or from positive transfer in lifelong learning. The concern is valid, but calling it "decisive" and "fatal" is not warranted given the SR results stand independently. **Demoted from implied fatal to Major** and reworded.

## Novel Insights

None beyond the paper's own contributions. The core insight — that representing multi-hierarchical navigation knowledge as a high-order tensor with explicit decoupling via Tucker decomposition enables better lifelong learning than two-matrix LoRA variants — is the paper's own contribution, not a novel synthesis from the reviews.

## Suggestions

1. **Clarify M-SR_t computation**: Provide the exact training protocol for computing the multi-task upper bound (training steps per task, optimizer settings, total budget). If the multi-task baseline is undertrained, either re-compute it with adequate resources or report forgetting relative to a properly calibrated upper bound. Address the negative values explicitly.

2. **Report variance**: Run experiments with at least 3 different random task orders (or seeds) and report mean ± std for all metrics. If the task order is intentionally fixed for all methods, state this clearly and justify why results are representative.

3. **Remove or reposition TTA baselines**: Either remove FSTTA and FeedTTA from the lifelong comparison tables, or add a clear separator/note explaining they are not lifelong methods and included only as non-lifelong references.

4. **Add DKIL component ablation**: Provide an ablation study showing the contribution of each loss term (EWC, consistency, orthogonal) to forgetting reduction, even if in the appendix.

5. **Add expert retrieval analysis**: Report retrieval accuracy (or a confusion matrix) for the CLIP-based expert matching to help readers understand when the method works and fails.

6. **Add a limitations paragraph**: Discuss the task-id assumption, the unbalanced environment dimension in real-world scenes, and potential failure cases for the retrieval mechanism.

## Score and Decision

**Initial bracket**: Based on calibration search, this paper clearly falls in the middle band (3.5–7.5). It is orders of magnitude stronger than weak-band papers scoring 2.0–2.5 (which have fundamentally flawed methodology or minimal contributions), but does not reach the 8+ band of exceptionally strong papers with clean, fully rigorous evaluation.

**Round 2 narrowing**: Within the 3.5–7.5 band, the most topically similar anchors are GSA-VLN (6.40, VLN + scene adaptation), FLoRA (5.75, Tucker decomposition for PEFT), ICL-TSVD (5.50, continual learning with pre-trained models), and Task-Unaware Lifelong Robot Learning (5.75).

Compared to **GSA-VLN (6.40)**: The current paper has a more novel technical contribution (Tucker decomposition for multi-hierarchical knowledge decoupling vs. memory-based graph navigation) and stronger margin over baselines (15–21 pp vs. more incremental gains). However, GSA-VLN has cleaner evaluation without questionable forgetting metrics. The papers are comparable in overall quality, with the current paper slightly stronger on technical novelty but slightly weaker on evaluation rigor.

Compared to **FLoRA (5.75)**: FLoRA is a general PEFT method using Tucker decomposition with broad applicability, while this paper applies Tucker decomposition to a specific lifelong VLN problem with additional components (DKIL, benchmark, agent). This paper's contribution is more domain-specific but also more complete (problem formalization + method + benchmark + agent). Clearly stronger than FLoRA.

Compared to **ICL-TSVD (5.50)**: That paper has theoretical guarantees but limited practical scope. This paper has more comprehensive practical contributions. Clearly stronger.

**Final score**: 6.0. The paper makes a genuine contribution with a novel problem formalization, a technically interesting method, a useful benchmark, and strong empirical results. However, the underspecified forgetting metric, lack of variance reporting, and mismatched baselines prevent it from being a strong accept. These issues are addressable in revision.

**Decision**: Accept.

**Anchors consulted**:
- JIlIYIHMuv (avg 2.50, round 1): VL + continual learning, weak paper — current paper is far stronger.
- zEhTnQZB3D (avg 2.33, round 1): Continual RL with language — current paper is far stronger.
- eWFkMCBySw (avg 5.00, round 1): Zero-shot VLN-CE — current paper has greater novelty and more comprehensive evaluation.
- tpUEqmjZiS (avg 4.50, round 1): Lifelong robot manipulation — current paper is stronger in both technical contribution and evaluation.
- 2oKkQTyfz7 (avg 6.40, rounds 1 & 2): GSA-VLN scene adaptation — comparable, see detailed comparison above.
- OALIb8oNfl (avg 5.75, round 2): FLoRA Tucker PEFT — current paper is stronger in domain-specific contribution.
- bqv7M0wc4x (avg 5.50, round 2): ICL-TSVD continual learning — current paper is stronger in practical contribution.
- Q5Sawm0nqo (avg 6.17, round 2): Tucker decomposition for time-series adaptation — relevant technique space but different domain.
- YR79EyejsG (avg 5.75, round 2): Task-unaware lifelong robot learning — current paper has more comprehensive evaluation.
- RnxwxGXxex (avg 5.67, round 2): CLDyB continual learning benchmark — different focus (benchmarking vs. method).
- G6DLQ40VVR (avg 6.25, round 2): DivScene object navigation benchmark — different task but similar VLN domain.
- gc8QAQfXv6 (avg 9.00, round 3): Function vectors for CF in LLMs — clearly stronger paper with deeper theoretical contribution and cleaner evaluation. Current paper does not reach this level.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>