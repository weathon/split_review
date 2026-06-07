Now I have a solid calibration. Let me compile the final review.

**Round 1 bracket:** 5.0–7.0

**Round 2 anchors:**
- Continual LLaVA (4.75) — our paper is clearly stronger (more novel architecture, better-specified method, more comprehensive evaluation)
- HILOW (5.75) — our paper is stronger (more novel architecture, larger evaluation, stronger results)
- Spurious Forgetting (6.33) — roughly comparable quality; our paper has stronger architectural novelty and evaluation, but shares having a significant methodological gap
- SLM (6.50) — comparable
- LOIRE (7.00) — clearly stronger than our paper in methodological rigor and component isolation

**Final score: 6.0.** The paper is a solid accept-level contribution with a genuinely novel Tucker decomposition architecture, comprehensive evaluation (24 tasks, sim+real, benchmark contribution), and strong results. The major disentanglement weakness (tensor structure vs. DKIL training strategy not separated) prevents a higher score but does not invalidate the core contributions.

---

## Summary

This paper formalizes the All-Day Multi-Scenes Lifelong VLN (AML-VLN) problem, where a navigation agent must continually learn across diverse scenes and illumination conditions without catastrophic forgetting. The core proposal is Tucker Adaptation (TuKA), which lifts LoRA-style parameter-efficient adaptation from 2D matrices to a 4th-order tensor decomposed via Tucker decomposition, explicitly decoupling scene-specific knowledge, environment-specific knowledge, and shared navigation skills. The resulting agent, AllDayWalker, is evaluated on a new benchmark (AllDay-Habitat) with 24 tasks across simulation and real-world scenes, achieving 65% average SR vs. 44–52% for the strongest baselines and an 11% average forgetting rate vs. 18% for the next-best method.

## Strengths

- **Novel architecture for multi-hierarchical continual learning:** The use of Tucker decomposition to represent adaptation weights as a 4th-order tensor with decoupled scene and environment expert factor matrices (§3.2, Eq. 2–3) is genuinely novel in both the continual learning and VLN literatures. The alignment mechanism (Eq. 3) that collapses the tensor to a 2D ΔW via row selection from U³ and U⁴ is a clean solution to the LLM-alignment challenge.

- **Substantial and consistent empirical gains:** AllDayWalker achieves 65% average SR across all 24 tasks (Table 1), outperforming BranchLoRA (44%), SD-LoRA (~56%), and O-LoRA (52%) by 9–21 points. The average forgetting rate of 11% (Table 2) is nearly half that of SD-LoRA (18%), directly supporting the claim that the method mitigates catastrophic forgetting.

- **Strong generalization to completely unseen scene–environment combinations:** On six held-out unseen scenarios spanning simulation and real-world settings (Table 5), AllDayWalker achieves 55% average SR vs. 39–40% for the strongest baselines — a 15-point margin that supports the claim that decoupled scene/environment representations enable transfer.

- **The 4th-order vs. 3rd-order tensor ablation validates the decoupled design:** Figure 8 shows that the 4th-order (decoupled scene × environment) representation consistently outperforms the 3rd-order (coupled scene×environment expert) across all 20 tasks. This directly corroborates the architectural motivation.

- **Physically-grounded benchmark construction:** The AllDay-Habitat platform (§4) synthesizes degraded environments using well-established imaging models — atmospheric scattering (Eq. 10), low-light noise with shot/read noise (Eq. 11), and sensor saturation for overexposure (Eq. 12) — producing a 24-task benchmark with realistic visual diversity that is a reusable contribution to the community.

## Weaknesses

### Fatal

None.

### Major

- **The gains from the tensor structure versus the DKIL training strategy are not disentangled.** TuKA bundles a novel tensor architecture with a Decoupled Knowledge Incremental Learning (DKIL) strategy that includes EWC on shared subspaces (Eq. 4), expert consistency constraints (Eq. 7), orthogonal subspace constraints (Eq. 8), expert inheritance initialization, and selective freezing of inactive experts. These DKIL components are orthogonal to the tensor representation — EWC, consistency regularization, and orthogonality constraints could be applied to any MoE-LoRA baseline. Yet the paper never ablates applying the DKIL recipe to, e.g., HydraLoRA or BranchLoRA. The 3rd-order vs. 4th-order ablation (Figure 8) keeps DKIL constant and only varies the tensor structure, and the shared-component ablation (Table 3) varies what is shared but still within TuKA. Without a baseline that combines DKIL training with a non-tensor architecture, the reader cannot determine how much of the 21-point SR gap over BranchLoRA comes from the Tucker structure versus from the bundled continual-learning techniques. An experiment applying DKIL to the best MoE-LoRA baseline would directly answer this and substantially strengthen the paper.

### Minor

- **Inference-time expert matching is under-characterized.** Section 3.4 describes CLIP-feature-based two-step matching to select scene and environment experts at inference time. The paper does not report matching accuracy, does not specify how many observations are stored per scene/environment to form the retrieval feature set, and does not analyze navigation performance as a function of matching correctness. For unseen scenarios (Table 5), the nearest-neighbor fallback is used but its behavior is not characterized. While the strong generalization results suggest the mechanism works, a characterization of matching fidelity would strengthen the task-id-agnostic inference claim.

- **Negative forgetting rates are unusual and unexplained.** Table 2 reports F-SR values of −3% (T14) and −4% (T20) for AllDayWalker. By the paper's definition (Eq. 13), a negative value means the lifelong learner outperforms joint multitask training on that task. While this is theoretically possible (joint training trades off between tasks), the paper does not discuss or explain these values, and they warrant clarification.

- **No ablation of individual DKIL loss terms.** The EWC, consistency, and orthogonality losses (§3.3) each carry hyperparameters (λ₁=0.2, λ₂=0.2, λ₃=0.1). Removing them one at a time would help understand which components drive the forgetting reduction.

- **FSTTA and FeedTTA are test-time adaptation methods, not lifelong learning methods.** Including them in Table 1–2 without adapting their protocols to the sequential lifelong setting is a framing mismatch. Their lower performance is unsurprising and provides limited signal for evaluating TuKA against lifelong learning baselines.

- **No limitations section.** The paper would benefit from discussing reliance on CLIP-based expert matching, the assumption that scenes and environments form a clean Cartesian product, and sensitivity to task ordering.

### Trivial

- **Duplicated row in Table 3.** Rows 3 and 6 are identical (all Sd- flags ✓, SR=65, F-SR=11). This appears to be a typesetting error.

## Nice-to-Haves

- Apply the full DKIL training strategy (EWC + consistency + orthogonality + inheritance + freezing) to the strongest MoE-LoRA baseline (BranchLoRA or SD-LoRA) to isolate the contribution of the Tucker tensor architecture.
- Characterize expert matching accuracy and navigation performance under matching failure.
- Report results across multiple random task orders with error bars to establish robustness.
- Discuss the implicit Cartesian-product assumption (scenes × environments) and its limits.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh Critic claim that "Negative forgetting rates suggest a problem with the forgetting metric or its computation (structural)."** Removed as a fatal/structural claim. The negative values are unusual but not impossible — joint training can trade off per-task performance, and a lifelong learner with good regularization could slightly exceed it on some tasks. Retained only as a minor concern asking the paper to explain these values.

- **Harsh Critic claim that the introduction "conflates the dimensionality of the explicit representation with the dimensionality of the knowledge that can be encoded."** This is a philosophical framing critique about representational capacity, not a factual error. The paper's claim that 2D adapters cannot explicitly decouple scene and environment knowledge is reasonable. Removed as non-substantive.

- **Harsh Critic claim about task-id asymmetry giving TuKA an "informational advantage" over baselines.** All methods have access to task-id during training (they train sequentially), and none have it during inference. TuKA's structural prior (scene × environment decomposition) is the paper's contribution, not an unfair advantage. Removed.

- **Strength Finder claim about "well-designed incremental learning strategy with complementary mechanisms."** Generic praise. The DKIL components (EWC, consistency, orthogonality) are standard continual learning techniques. Removed as a standalone strength.

- **Harsh Critic claim that "half the total loss comes from regularization terms, which is unusually high."** The navigation loss weight λ = 0.5 is indeed high for regularization, but the results show the method works. This is a design choice, not a flaw. Removed.

- **Harsh Critic claim about the paper's characterization of MoE-LoRA variants as "two-hierarchical" being inaccurate for BranchLoRA/MoLA.** The paper specifically addresses HydraLoRA in §3.1, and the general observation that all these methods operate on 2D matrix forms is factually correct — more complex routing still operates on 2D matrices. Removed as a strawman critique.

## Novel Insights

None beyond the paper's own contributions. The idea of using Tucker decomposition for multi-hierarchical adaptation weight representation is the paper's novel insight.

## Suggestions

- The single highest-impact improvement is the DKIL-on-baseline ablation. Running EWC + consistency + orthogonality on BranchLoRA with experts organized to mirror the scene × environment structure would directly answer whether the Tucker structure matters or DKIL carries the gains.
- Report matching accuracy for the CLIP-based expert selection and characterize navigation performance under correct vs. incorrect matching.
- Add multiple random task orderings with standard deviations to confirm robustness.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>