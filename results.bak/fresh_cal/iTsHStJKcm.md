Now I have a thorough understanding of the paper. Let me produce the consolidated review.

## Summary

This paper proposes a demonstration-free hierarchical planning approach for deformable object (dough) manipulation. It combines large language models (LLMs) for high-level task decomposition and intermediate subgoal point cloud generation (via Python code) with a novel EMD-space gradient-based planning algorithm (DiffPhysics-P2P) that uses differentiable physics with point-to-point correspondence for low-level control. The method operates **without any training or demonstrations** and is evaluated on both single-tool and multi-tool dough manipulation tasks in simulation and on a real robot.

## Strengths

1. **Demonstration-free hierarchical planning combining LLMs with geometric planning is novel.** The paper introduces a clean architecture where LLMs output executable Python code to generate subgoal point clouds, bridging high-level semantic decomposition with low-level geometric planning. This is a genuinely new combination in the deformable object manipulation literature, where prior work (PASTA, DiffSkill, RoboCraft) required substantial training data or predefined stage counts.

2. **DiffPhysics-P2P with point-to-point correspondence is clearly motivated and ablated.** The key technical contribution — using EMD gradient descent to induce one-to-one correspondences between current and candidate particles, then applying per-point L1 loss through differentiable physics — is explained (Section 3.2, Eq. 1–2) and validated via ablation (Figure 5, right). The paper contrasts this with naive EMD loss that lacks correspondence, and the ablation shows removal substantially degrades performance.

3. **Volume-preserving prompt engineering demonstrably improves LLM output quality.** Table 1 quantifies relative volume change with and without the volume-preserving guidance and chain reasoning, showing large improvements (e.g., from −0.48 to −0.01 on the Donut task). This provides concrete evidence that the prompt design choices in Section 3.1 are effective.

4. **Tool-reset mechanism addresses a genuine failure mode of differentiable physics.** The method detects stagnation and resets tool position (Algorithm 1, Figure 3), and the ablation confirms this component is beneficial. This is a practical contribution for making differentiable physics optimization more robust.

5. **Real-robot transfer is demonstrated.** Despite being simulation-to-real and open-loop, the paper shows qualitative results on a UFACTORY xArm 6 with clay for both multi-tool (TwoPancakes) and single-tool tasks, providing initial evidence of practical applicability.

## Weaknesses

### Fatal

None. The paper's core contribution — a demonstration-free hierarchical planning system — is coherent and the evidence for it is partial but not invalidated. The most serious weaknesses (below) are fixable.

### Major

1. **Ground-truth targets for multi-tool tasks are LLM-generated, making the quantitative metric partially circular.** The paper explicitly states (Section 4, Metrics): *"For each multiple-tool task, we utilize the LLM's Python code output from the last stage to generate the point cloud, serving as the ground truth."* The reported score measures normalized EMD decrease from initial to final point cloud relative to this target. Since both the subgoal plan and the target come from the same LLM, the metric primarily measures **self-consistency** — whether execution follows the LLM's own plan — not whether the final shape correctly matches the intended object (donut, baguette, pancake). This weakens the headline quantitative results in Table 2 (left). The qualitative images (Figure 4) look reasonable and partially mitigate this, but the central claim that the method "surpasses multiple benchmarks" on multi-tool tasks rests on a metric that is not independently grounded.

2. **Baseline comparisons are asymmetric and not informative.** 
   - **BC and SAC-N** are given a single demonstration per task (stated in Section 4), far below what these methods require for complex long-horizon tasks. While the paper's motivation is that demos are scarce, comparing against methods starved of data to the point where they are guaranteed to fail does not constitute a meaningful comparison.
   - **PASTA** is evaluated zero-shot on multi-tool tasks using a pretrained model trained on single-tool demonstrations (Section 4). This tests cross-task generalization PASTA was not designed for. A more informative comparison would adapt PASTA to multi-tool settings or compare against a version of PASTA given the same LLM-generated subgoals.
   - The reported scores (e.g., 0.91 vs. −0.02 for Donut) are so lopsided that they raise questions about whether the comparison is rigged rather than informative. At minimum, the paper should include an oracle baseline (hand-designed subgoal point clouds) to isolate the LLM's contribution.

3. **No statistical reporting.** The paper reports only point estimates in Table 2 with no standard deviations, confidence intervals, or variance of any kind. With only 20 trials per multi-tool task and 5 per single-tool task, variance could be substantial. This omission makes it impossible to assess the reliability of the reported improvements.

### Minor

1. **The claim that the EMD-space candidate "serves as our model's prediction of the underlying particle dynamics" (Section 3.2) is overstated.** EMD gradient descent on point positions is a purely geometric operation — it does not encode physical constraints (volume preservation, collision, material stiffness, tool-object interaction). The method does not need this claim to work (the candidate is an intermediate target for differentiable physics, which handles physical plausibility), but the framing incorrectly suggests a physics-grounded prediction where none exists.

2. **Under-specified components affecting reproducibility:**
   - The exact LLM prompt template is not provided (Section 3.1 mentions a "prompt template" and guidelines but no full prompt).
   - The differentiable physics simulator used for the proposed method is not identified (Section 4 says the environment is from PASTA for single-tool tasks, but it's unclear if the same simulator is used for the proposed method's low-level control).
   - How the tool SDF (needed in Eq. 3 for initial position selection) is obtained is not explained.
   - Several hyperparameters are missing: the gradient descent learning rate α in Eq. 1, stopping criteria for the EMD-space planning, and the differentiable physics optimizer details.

3. **Limited task scope relative to claims.** The paper claims *"robust generalization capabilities to novel and previously unencountered complex tasks"* but tests only three multi-tool tasks (Donut, Baguette, TwoPancakes) and three single-tool tasks (Spread, Cut, Arrange). All shapes are symmetric and primitive. Testing on more diverse shapes (e.g., a star, a letter shape, a crescent) would be needed to substantiate the generalization claim. The paper itself acknowledges this limitation (Section 5).

4. **No failure analysis or discussion of when the method breaks.** The paper does not analyze cases where the LLM generates infeasible subgoals, the tool reset triggers repeatedly, or the EMD-space candidate is too far from physically realizable. Understanding failure modes would significantly strengthen the paper.

5. **Real-robot evaluation is only qualitative and open-loop.** The trajectory is generated in simulation and executed open-loop (Section 4.4). Deviations between simulation and real dynamics are not measured or corrected. While this is acknowledged as a pilot experiment, it limits what can be claimed about real-world applicability.

### Trivial

- The paper relies on table images that are not text-readable, making it impossible to verify exact numerical values from the plain-text extraction.

## Nice-to-Haves

- **Validation of LLM-generated targets via human evaluation.** Even a small user study (e.g., raters judging whether final point clouds or executed shapes resemble the intended object) would break the circularity concern.
- **Oracle baseline replacing LLM subgoals with hand-designed subgoal point clouds** to isolate the LLM's contribution from the low-level planner's.
- **Compare against a version of PASTA given the same LLM-generated subgoals** (using PASTA as the low-level planner) to isolate the contribution of DiffPhysics-P2P.
- **Sensitivity analysis** for key hyperparameters (number of EMD gradient steps, learning rate α, number of tool resets allowed).
- **Wall-clock time or iteration count** for the method vs. baselines, to contextualize practical applicability.
- **Confidence intervals or standard deviations** for all reported metrics.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"The paper does not justify L1 over L2 norm (Eq. 2)."** — Trivial nitpick. The method uses L1 which is standard for point-wise losses in deformable manipulation; no justification is needed for such a minor design choice.

2. **"The criticism of differentiable physics ('rugged loss landscape') creates tension because the method itself uses differentiable physics."** — This misunderstands the paper. The method uses EMD-space planning to *overcome* the rugged landscape that naive differentiable physics suffers from. The resolution is the paper's core contribution.

3. **"The differentiable physics comparison (Diff. Physics baseline) is unfair because it's comparing whole system vs. a component."** — The Diff. Physics baseline is a legitimate ablation-style comparison intended to show the value of the hierarchical guidance. It is informative, not unfair.

4. **"PASTA reported as 'OOM' is an implementation failure."** — Cannot be verified from the paper text (the tables are images). If a method goes out-of-memory, reporting that is factual; it does not indicate an implementation error.

5. **Missing related works.** — Per instructions, I cannot raise this as a weakness since I lack external sources to verify omissions.

6. **General "evaluation lacks rigor" / "evidence is weak" sweeps without concrete anchors** — The specific, anchored weaknesses are retained above; the generic framing is removed.

## Novel Insights

The reviews surface an interesting synthesis point: the paper's two-level hierarchy creates a **credibility asymmetry**. The low-level planner (DiffPhysics-P2P) is well-validated with clean ablations and a clear mechanism (EMD gradient → point correspondence → per-point L1 loss), while the high-level LLM planning is evaluated with a circular metric (LLM generates both plan and ground-truth target). This means the paper's strongest evidence supports the *execution* component, not the *planning* component. A future version could leverage this by testing the low-level planner with oracle subgoals and the high-level planner with human-judged outcomes, separating the two contributions. This asymmetry is not discussed in either review but emerges from the contrast between the clean ablation methodology for DiffPhysics-P2P and the questionable metric for the LLM stage.

## Suggestions

1. **Fix the multi-tool evaluation metric.** The most critical revision. Options: (a) use human raters to judge whether final shapes match the intended object, (b) generate ground-truth targets from CAD models or human-drawn point clouds, (c) validate a subset of LLM-generated targets via human evaluation and show they are indeed reasonable.
2. **Report standard deviations/confidence intervals** for all quantitative results. With small trial counts (20 per multi-tool task, 5 per single-tool), variance reporting is essential.
3. **Strengthen baselines:** (a) give BC/SAC-N more demonstrations (at least 10–20) to provide a meaningful comparison; (b) adapt PASTA to multi-tool settings rather than testing it zero-shot; (c) add an oracle baseline with hand-designed subgoals.
4. **Provide the LLM prompt template** (full text) in an appendix, along with the differentiable physics simulator details, tool SDF computation, and key hyperparameters.
5. **Add a failure analysis section** discussing when the method breaks and why.
6. **Tone down the generalization claim** — "robust generalization to novel and previously unencountered complex tasks" is not supported by 3 primitive multi-tool shapes. Scope the claim to the actual demonstrated tasks.

## Score and Decision

The paper proposes a genuinely interesting architecture with a well-ablated low-level planner. However, the major weakness — a circular evaluation metric for the headline multi-tool tasks — significantly undermines the quantitative evidence for the LLM planning component. The baseline comparisons are also not informative in their current form. These issues require substantial revision before the paper can be accepted.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>