Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper formalizes the all-day multi-scenes lifelong VLN (AML-VLN) problem—continual VLN across multiple scenes and diverse illumination conditions—and proposes Tucker Adaptation (TuKA), which represents multi-hierarchical navigation knowledge as a fourth-order tensor and uses Tucker decomposition to decouple shared subspaces from scene-specific and environment-specific experts. The AllDayWalker agent combines TuKA with a Decoupled Knowledge Incremental Learning (DKIL) strategy that consolidates shared knowledge via EWC while constraining expert drift. The paper also extends Habitat with three physically-motivated degradation models (low-light, scattering, overexposure). Experiments on a 24-task benchmark show AllDayWalker achieving 65% SR vs. 44% for the next-best BranchLoRA, with the lowest forgetting rate (11% F-SR).

## Strengths

- **Novel and principled technical contribution.** Tucker decomposition to represent multi-hierarchical knowledge (scene × environment × shared skills) in a high-order tensor is genuinely new within the VLN and PEFT literature (Eq. 2–3, Figure 3c). By aligning the fourth-order tensor dimensions to a 2D matrix for LLM adaptation, TuKA provides a principled alternative to the two-matrix LoRA family that explicitly decouples scene and environment experts rather than collapsing them into a single task dimension. This is the paper's strongest contribution.

- **Consistent and substantial empirical results.** In Table 1, AllDayWalker achieves the highest average SR (65%) across all 24 tasks, outperforming the next-best method (O-LoRA, 52%) by 13 points, and extends this advantage across SPL, OSR, and forgetting metrics. In Table 2, AllDayWalker achieves the lowest average forgetting rate (11% F-SR) versus 18% for the next-best SD-LoRA. These margins are large and hold across the full task sequence.

- **Well-designed ablations validate the architectural choices.** Figure 8 rigorously shows that a fourth-order tensor (decoupled scene/environment experts) consistently outperforms a third-order tensor (coupled expert set) across all 20 tasks. Table 3 ablates the shared components, showing that sharing both the core tensor 𝒢 and encoder U² yields the best SR (65%), while sharing U¹ does not hurt performance and saves storage. Table 4 demonstrates stability when scaling from 24 to 30 tasks.

- **Generalization to unseen scenarios is demonstrated.** Table 5 reports AllDayWalker achieving 55% average SR on six completely unseen scene–environment pairs (4 simulation + 2 real), substantially surpassing BranchLoRA (40%) and SD-LoRA (39%), and improving over the vanilla StreamVLN backbone (35%). This provides evidence that the decoupled knowledge representation transfers.

- **Reproducibility-oriented contributions.** The paper releases code, video demos, and extends Habitat with three physically-motivated degradation models (Eq. 10–12), creating a reusable benchmark for all-day VLN research.

## Weaknesses

### Major

- **The inference-time expert retrieval mechanism is presented without any accuracy analysis.** At test time, the agent selects scene expert U³[s,:] and environment expert U⁴[e,:] by matching the query observation's CLIP feature against stored training features (Section 3.4). The paper provides no retrieval accuracy numbers (scene identification or environment identification), no confusion matrices, and no ablation where ground-truth expert IDs are given at test time. Without this analysis, it is impossible to tell whether the method's strong performance relies on near-perfect retrieval or whether it is robust to retrieval errors. The generalization experiment (Table 5) implicitly exercises this mechanism but does not isolate its accuracy. Since the same query feature Fe_q is used to match both scene and environment, a misclassification (e.g., a low-light observation of Scene A matching the stored features of Scene B's low-light observation) could compound errors. This is a genuine evidential gap that should be filled—either by showing that retrieval accuracy is high, or that the method tolerates retrieval errors gracefully. The core technical contribution (TuKA + DKIL) does not depend on any particular retrieval mechanism, but the complete system's validity does.

### Minor

- **The benchmark is small-scale relative to the "all-day multi-scenes" claim.** The benchmark uses 7 scenes (5 simulation + 2 real) and 4 environments, yielding 24 tasks. While this is a reasonable first benchmark and the paper extends to 30 tasks (Table 4) without degradation, the scalability to substantially larger scene sets (e.g., 50+ scenes) is unaddressed. The orthogonal constraint (Eq. 8) enforces pairwise orthogonality among scene expert rows, which becomes a dense O(M²) constraint as M grows and may limit expressivity per expert. The paper should either provide experiments with more scenes or explicitly scope the claim.

- **No variance/confidence reporting.** Results in Tables 1–5 are reported as point estimates without standard deviations or multiple seeds. Given that VLN metrics can have non-trivial variance, this makes it difficult to assess whether the reported margins are statistically significant. Reporting results over 3 random seeds is standard practice in this domain.

- **The loss weighting design (λ = 1 − (λ₁ + λ₂ + λ₃)) is not ablated.** With the chosen hyperparameters (λ₁=0.2, λ₂=0.2, λ₃=0.1), the navigation loss weight is λ = 0.5, meaning the primary training objective is halved relative to the regularization terms. The paper does not study sensitivity to this design choice (e.g., fixing λ=1 and adding regularization as standard multi-objective loss).

- **Notational ambiguity about U³/U⁴ sharing across layers.** In Eq. (2), 𝒳^l carries a layer superscript l, and U¹∈ℝ^{a_l×r₁} and U²∈ℝ^{b_l×r₂} have layer-dependent dimensions, but U³∈ℝ^{M×r₃} and U⁴∈ℝ^{N×r₄} have no layer index. It is not explicitly stated whether U³ and U⁴ are shared across all transformer layers or per-layer. This matters for parameter count and implementation.

### Trivial

- The paper lacks a dedicated limitations/discussion section that could acknowledge the above issues and outline future work.

## Nice-to-Haves

- Visualizing the expert similarity matrix (cosine similarity between rows of U³ and U⁴) before and after training would visually validate whether the orthogonal constraint achieves meaningful expert separation.
- A comparison with a simple multi-head adapter baseline (separate non-decomposed adapters per scene and per environment) would serve as a direct lower-bound ablation of the tensor decomposition's value, though the existing baselines partially serve this role.

## Removed Points

The following points from the harsh critic or strength finder are removed or demoted:

- **No comparison to multi-head adapter baseline**: The paper already compares against Seq-FT, O-LoRA, BranchLoRA, and SD-LoRA, which collectively cover separate per-task adaptation. No additional baseline is needed.
- **Parameter count not reported in main tables**: The paper states "implementation details and methods parameter comparison are provided in Appendix C," which exists in the original submission.
- **SD-LoRA missing values in Table 1**: Likely a PDF extraction artifact; the paper's original submission would have complete data.
- **Claim that LoRA-based methods are "limited to two-hierarchical matrices" is overstated**: Even if stacking multiple LoRA modules could encode more hierarchies, the Tucker formulation is a more principled decomposition; the motivation is acceptable.
- **Generic strength about "addressing an important problem"** : Not specific enough to retain. The concrete strengths above capture the paper's value.

## Novel Insights

The paper's core insight—that multi-hierarchical knowledge in continual VLN (spanning scenes and environments) maps naturally onto a Tucker-decomposed tensor, where shared core skills, scene experts, and environment experts occupy distinct factor matrices—is itself the main novel contribution. The observation that a fourth-order tensor substantially outperforms a third-order one (Figure 8) provides empirical evidence that decoupling the hierarchies rather than collapsing them into a single task dimension yields better representation learning. Beyond the paper's own contributions, the fact that the generalization experiment (Table 5) achieves 55% average SR on completely unseen scene–environment pairs with only a single observation for expert retrieval suggests that CLIP features are surprisingly effective at discriminating both scene identity and environmental degradation type—a property the paper could leverage more explicitly.

## Suggestions

1. **Analyze the retrieval mechanism explicitly.** Provide retrieval accuracy (scene and environment identification) on the validation split. Ablate by giving the model ground-truth expert IDs at test time to isolate retrieval errors from adaptation quality. Report a confusion matrix.
2. **Add variance reporting.** Run the main comparison (Table 1) with 3 random seeds and report mean ± std.
3. **Include a limitations/discussion section.** Acknowledge the current scale, discuss scalability to more scenes, and outline how the retrieval mechanism might degrade in larger expert pools.
4. **Ablate the loss weighting design.** Compare the current λ = 1−(λ₁+λ₂+λ₃) formulation against a standard multi-objective loss where all terms are additive with fixed weights and no compensatory shrinkage of the navigation loss.

## Score and Decision

**Calibration summary.**

*Round 1 bracket:* Between 5 and 7 on the review scale. The paper is clearly stronger than rejected papers in the 2–3.5 range (e.g., LVLM-CL at 2.50, Projected Subnetworks at 2.00) but does not reach the 8+ range of exceptional papers.

*Round 2 narrowing:* Compared to accepted papers in similar areas:

| Anchor | Avg Score | Comparison |
|--------|-----------|------------|
| C-CLIP (sb7qHFYwBc) | 6.50 | Multimodal continual learning for CLIP. Current paper has stronger technical novelty (Tucker vs. LoRA+contrastive) but weaker evaluation breadth and no variance reporting. Comparable quality. |
| GSA-VLN (2oKkQTyfz7) | 6.40 | Scene adaptation for VLN. Current paper has cleaner technical contribution but smaller benchmark. Similar quality. |
| SRDF (OUuhwVsk9Z) | 6.50 | VLN data flywheel. Stronger empirical scope, less technical novelty. Comparable. |
| ICL-TSVD (bqv7M0wc4x) | 5.50 | Continual learning theory-practice bridge. Different domain; current paper is stronger empirically. |
| Continual LLaVA (rwmwFnmjAX) | 4.75 | Rejected; current paper is clearly stronger on both novelty and results. |

The paper sits below the 6.50 anchor papers due to the unfilled evidential gap in the retrieval mechanism analysis and the small-scale benchmark, but clearly above the rejected Continual LLaVA (4.75) and the weaker ICL-TSVD (5.50) due to stronger novelty and results. A score of 6.0 appropriately positions it.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>