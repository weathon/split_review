Now I have enough context to write the consolidated review. Let me finalize my analysis of the paper's strengths and weaknesses, verify each against the paper, and produce the review.

Key verification points:

1. **Harsh critic claim: baseline test-time inference unspecified** — Verified from paper. Section §2 says "task-id t is seen during agent training but is agnostic during the testing phase." Section §3.4 describes TuKA's CLIP-based retrieval for test-time expert selection. But the paper does not describe how most baselines (HydraLoRA, BranchLoRA, O-LoRA, etc.) select their task-specific modules without task IDs at test time. This is a real, verifiable gap. However, many baselines (Dense/Sparse MoLE, MoLA use input-dependent routing; SD-LoRA composes adaptively; Seq-FT/LwF/EWC use single models) likely handle this naturally. The concern applies mainly to HydraLoRA, BranchLoRA, and O-LoRA. This is **Major**, not Fatal — it's a presentation/clarity issue, not a methodological invalidation.

2. **Harsh critic: DKIL component ablation missing** — Verified. Table 3 only ablates shared components (core tensor, encoder, decoder). The EWC, consistency, and orthogonal loss terms (λ₁, λ₂, λ₃) are not individually ablated. This is **Major** — it weakens the evidence for DKIL's specific design.

3. **Harsh critic: "high-order tensor" language** — The paper uses "fourth-order tensor" which is standard terminology. **REMOVE**.

4. **Harsh critic: retrieval risk discussion** — Valid suggestion but minor. Table 5 already shows generalization works. **Minor**.

5. **Harsh critic: simulator fidelity** — The paper acknowledges the simulator is built for benchmarking, not claiming photorealistic fidelity. **REMOVE** (scope creep — the paper is about continual learning, not simulator validation).

6. **Harsh critic: parameter counts in appendix** — Paper says they're in Appendix C. **Minor**.

7. **Strength Finder: sharing ablation rigorously justifies architecture** — Table 3 is informative but limited. Keep but qualify.

8. **Strength Finder: DKIL drastically reduces forgetting** — Valid from Table 2 data, but DKIL components not individually validated. Keep but note the missing ablation.

Now let me also verify the strength finder's stronger claims:

- **"High-order tensor representation effectively decouples"**: Valid. Table 1, Figure 8 support this.
- **"Generalizes well to unseen scenes"**: Valid. Table 5 supports this.
- **"Realistic and challenging benchmark"**: The benchmark is described in §4 and §5, with 24 tasks spanning 5 sim scenes + 2 real scenes × 4 environments. Valid.

Let me now produce the final review.## Summary

This paper formalizes the All-day Multi-scenes Lifelong Vision-and-Language Navigation (AML-VLN) problem and proposes Tucker Adaptation (TuKA), a parameter-efficient method that lifts LoRA-style adaptation into a fourth-order tensor. Tucker decomposition decouples the tensor into shared core skills, scene-specific experts, and environment-specific experts. A Decoupled Knowledge Incremental Learning (DKIL) strategy combines EWC, consistency, and orthogonal constraints to mitigate forgetting across a 24-task benchmark spanning five simulated scenes and two real-world scenes under four lighting conditions. The resulting AllDayWalker agent achieves 65% average success rate (vs. 44% for the best LoRA-based baseline) and 11% average forgetting rate (vs. 18%).

## Strengths

- **Novel high-order tensor formulation for multi-hierarchical knowledge.** Modeling adaptation weights as a fourth-order tensor and decomposing it via Tucker decomposition (Equation 2) into scene experts, environment experts, and a shared core tensor is a genuinely new architecture in the continual-LoRA space. The fourth-order vs. third-order ablation (Figure 8) provides direct evidence that decoupling scene and environment dimensions matters, with consistent gains across all 20 tasks.

- **Strong benchmark construction for lifelong VLN.** The AllDay-Habitat platform extends Habitat with three physics-based degradation models (scattering, low-light, overexposure; Equations 10–12) to produce 24 hierarchically structured navigation scenarios (Figure 6). This is a well-motivated multi-dimensional benchmark that combines scene and environment variation.

- **Convincing generalization results.** On six completely held-out scenarios (Table 5), AllDayWalker achieves an average SR of 55% vs. 40% for BranchLoRA and 39% for SD-LoRA, demonstrating that the decoupled expert structure transfers to unseen scene/environment combinations.

- **Thorough baseline coverage.** Twelve comparison methods are evaluated, spanning regularization-based (EWC, LwF), MoE-based (Dense/Sparse MoLE, MoLA, HydraLoRA, BranchLoRA), orthogonal (O-LoRA), compositional (SD-LoRA), and test-time adaptation (FSTTA, FeedTTA) approaches, making this one of the more comprehensive continual-learning-for-VLN comparisons.

## Weaknesses

### Major

- **Baseline test-time inference protocol is unspecified.** The AML-VLN setting (§2) explicitly makes task IDs agnostic at test time. TuKA handles this via CLIP-feature retrieval (§3.4) to select scene and environment experts. However, the paper never describes how baselines that maintain per-task modules (HydraLoRA, BranchLoRA, O-LoRA) perform expert/module selection without task IDs. If these baselines received oracle task IDs while TuKA did not, the comparison is unfair. Conversely, if they also use retrieval or routing and the paper simply omits this detail, the missing description still prevents readers from assessing parity. This gap affects all reported comparisons (Tables 1–2, Table 5, Figure 7) and needs to be addressed in a rebuttal. (Methods like Dense/Sparse MoLE, MoLA, and SD-LoRA may handle this via input-dependent routing or adaptive composition and are less affected, but the paper should state this explicitly.)

- **DKIL loss components are not individually ablated.** The DKIL strategy (§3.3) combines EWC (Equation 4), expert consistency (Equation 7), and orthogonal constraints (Equation 8) with balance hyperparameters λ₁=0.2, λ₂=0.2, λ₃=0.1. The ablation in Table 3 examines only shared vs. unshared core tensor, encoder, and decoder — it does not isolate the contribution of any DKIL loss term. Without deactivating EWC, consistency, or orthogonal constraints one at a time, the reader cannot assess which components of DKIL actually drive the low forgetting rates reported in Table 2 (11% avg. F-SR). This weakens the evidence that the full DKIL design is necessary.

### Minor

- **Ablation on shared decoder is inconclusive.** Table 3 shows that removing the shared decoder (w/o Sd-U¹) barely changes SR (63% vs. 65%). The paper acknowledges this and argues it is retained for "integrity of tensor representation" and storage savings, but the reasoning is thin — a simpler architecture omitting the shared decoder would be equally justified by this data.

- **Negative forgetting rates are unexplained.** Table 2 reports negative F-SR values for AllDayWalker on T14 (−3%) and T20 (−4%). The paper never comments on whether this indicates genuine positive backward transfer or is an artifact of the joint-training upper bound M-SRₜ used in Equation 13.

- **Parameter comparison deferred to appendix.** The paper states that parameter counts and implementation details are in Appendix C (stripped). A summary table in the main text comparing trainable parameters across methods would improve transparency, especially since parameter efficiency is a claimed contribution.

- **Training order and task composition details are appendix-only.** The sequential training order and task composition are described only in the stripped Appendix E. These details matter for assessing benchmark difficulty and reproducibility.

### Trivial

- The text sometimes refers to the tensor 𝒳 as if it were materialized, though it is factorized (Equation 2). This is a minor notational imprecision that does not affect correctness.

## Nice-to-Haves

- A comparison against a simpler expert-composition baseline (e.g., element-wise product of separate scene and environment expert vectors without a Tucker core tensor) would sharpen the contribution by isolating the value of the core tensor's interaction modeling.
- Discussion of failure modes when CLIP-based expert retrieval selects the wrong scene or environment expert, particularly in generalization settings where observations may be ambiguous.
- Reporting confidence intervals or variance across multiple seeds for the main results would strengthen reliability claims.

## Removed Points

These points were flagged by reviewers but are removed from the main review:

- **"High-order tensor language is imprecise"** — A fourth-order tensor is correctly called a high-order tensor in the tensor decomposition literature (Kolda & Bader, 2009, is cited). This is standard terminology.
- **"Simulator lacks perceptual similarity analysis to real degraded conditions"** — The paper's contribution is the continual learning method, not simulator validation. Evaluating perceptual fidelity is outside scope.
- **"LoRA can only represent two-hierarchical knowledge is over-simplified"** — The paper acknowledges MoE-LoRA variants have shared + specific structures (§3.1) and argues this still collapses to two hierarchies, which is a defensible characterization given the scene × environment structure of AML-VLN.
- **"Missing appendix content" / formatting artifacts** — The parser strips appendices and introduces formatting noise. These are not author errors.
- **"Real-world deployment results are overstated"** — The paper includes two real-world scenes in the 24-task benchmark and clearly labels them as such. The claim is proportionate.
- **"Missing related works"** — We do not have external sources to verify proposed missing references; this is excluded per protocol.
- **Strength Finder: "Realistic and challenging benchmark" as standalone strength** — This is descriptive, not evaluative. Merged into the strengths above where supported by concrete evidence.

## Novel Insights

The paper's use of Tucker decomposition to simultaneously decouple scene and environment experts from a shared core is a genuinely novel transfer from multilinear algebra to parameter-efficient continual learning. While Tucker decomposition has been used in other ML contexts (e.g., model compression), its application here — where the third and fourth tensor modes correspond to *semantically distinct* hierarchical knowledge dimensions (scene identity vs. environment condition) rather than arbitrary factorizations — is non-obvious and well-motivated by the AML-VLN problem structure. The empirical finding that a third-order tensor (collapsing scene and environment into one mode) underperforms the fourth-order variant (Figure 8) provides a clean demonstration that explicit decoupling matters.

## Suggestions

- Describe precisely how each baseline performs test-time expert/module selection without task IDs. If some methods received oracle task IDs, either re-run them with a fair retrieval mechanism or explicitly discuss this as a limitation of those baselines rather than a comparison point.
- Add a DKIL component ablation (disable EWC, consistency, orthogonal terms one at a time) to establish which parts of the loss drive the forgetting reduction. This would substantially strengthen the paper.
- Add a brief note in the main text explaining when negative forgetting rates occur and what they mean.
- Include a compact parameter-count comparison table in the main paper rather than deferring entirely to the appendix.

## Score and Decision

**Round-1 bracket:** Compared against anchors, this paper sits above the weak band (LVLM-CL, score 2.50; Projected Subnetworks, score 2.00) and the middle band's lower end (PSPL, score 4.50; Vision-Language Synergy for CL, score 5.00), placing it in the 5.0–7.5 range based on novelty and experimental thoroughness.

**Round-2 narrowing:** Compared against EKfcngSxwD (Task Codebook, 4.67) and YR79EyejsG (Task-Unaware Lifelong Robot Learning, 5.75), the current paper has clearer technical novelty and more extensive evaluation. Compared against GSA-VLN (6.40) — the most directly comparable VLN adaptation paper — the current paper has a more novel architecture (Tucker decomposition vs. memory-based graph) and a more extensive benchmark (24 tasks with scene × environment structure), but shares similar presentation gaps (baseline protocol clarity). It is notably below gc8QAQfXv6 (Function Vectors for CF, 9.00) in theoretical depth and ablation rigor. The two Major weaknesses (unspecified baseline inference protocol, missing DKIL ablation) prevent a score in the 7+ range but the core contribution remains solid.

**Anchor papers referenced:** JIlIYIHMuv (2.50), WM5G2NWSYC (2.00), zEhTnQZB3D (2.33), gNoqEdT2wO (2.33), tpUEqmjZiS (4.50), 9aZ2ixiYGd (5.00), 2oKkQTyfz7 (6.40), eWFkMCBySw (5.00), gc8QAQfXv6 (9.00), 7gUrYE50Rb (8.00), 3i13Gev2hV (8.00), kxnoqaisCT (7.75), EKfcngSxwD (4.67), rwmwFnmjAX (4.75), RnxwxGXxex (5.67), RRayv1ZPN3 (6.20), YR79EyejsG (5.75), J3H8Az3YlB (5.75).

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>