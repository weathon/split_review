Now I have enough information to write the consolidated review. Let me compose my final assessment.

## Summary

The paper formalizes the all-day multi-scenes lifelong vision-and-language navigation (AML-VLN) problem and proposes Tucker Adaptation (TuKA), a parameter-efficient method that represents multi-hierarchical navigation knowledge as a high-order tensor using Tucker decomposition. It further introduces a decoupled knowledge incremental learning (DKIL) strategy for lifelong learning, and builds the AllDayWalker agent. The paper also extends Habitat with physically motivated degraded imaging (scattering, low-light, overexposure) to create a new benchmark. Experiments across 24 tasks show AllDayWalker achieves 65% average SR vs. 52% for the best baseline (SD-LoRA) with only 11% forgetting rate.

## Strengths

1. **Novel formulation of multi-hierarchical knowledge via Tucker decomposition (TuKA).** The paper identifies a genuine limitation of LoRA-family adapters for lifelong VLN — they represent task knowledge with two-dimensional matrices that cannot naturally separate scene-level, environment-level, and shared knowledge. TuKA addresses this by lifting adaptation into a 4th-order tensor (Scene × Environment × input_dim × output_dim) and using Tucker decomposition to decouple shared core knowledge from scene/environment-specific expert factors (Eq. 2–3, Fig. 3c). This architectural insight is the paper's primary intellectual contribution and is well-motivated.

2. **Strong empirical performance on the AML-VLN benchmark.** AllDayWalker achieves an average success rate of **65%** across 24 tasks, outperforming the best baseline SD‑LoRA (52%) by 13%, while maintaining an average forgetting rate of only **11%** vs. 18% for SD‑LoRA (Tables 1–2). The gap is consistent across individual tasks, not just averages. The method also shows stability when scaling to 30 tasks (Table 4), suggesting robustness.

3. **Generalization to unseen scenarios with learned expert structure.** On six completely unseen navigation tasks (Table 5), AllDayWalker achieves 55% average SR, substantially outperforming BranchLoRA (40%) and SD‑LoRA (39%). This demonstrates that the decoupled expert representation supports transfer to novel scene–environment combinations — a practically important capability.

4. **Comprehensive evaluation scope.** The paper includes: (a) a new problem formalization (AML‑VLN), (b) a custom benchmark with physically grounded degradation models (Eq. 10–12), (c) ablations on tensor order (Fig. 8), shared components (Table 3), and scalability (Table 4), and (d) real-world deployment. This breadth anchors the contribution in a realistic setting.

## Weaknesses

### Major

1. **Key ablations are confounded by parameter capacity, not just architectural design.** The central claim that the 4th-order tensor outperforms the 3rd-order because of its "decoupled representation of multi-hierarchical knowledge" (Fig. 8) is undermined by a large parameter-count disparity. A 4th-order TuKA layer with r1=r2=8, r3=r4=64, M=7, N=4 requires ~328K params per layer, while the 3rd-order variant (U³∈ℝ^{20×128}) requires only ~76K — a **4.3× difference**. The observed gains could partly reflect increased capacity rather than the decoupled structure. A capacity-controlled ablation (e.g., matching total parameters by increasing r3 in the 3rd-order variant or reducing ranks in the 4th-order) is needed to substantiate the architectural claim.

2. **Parameter fairness in the main comparison is not established.** The paper states parameters were kept "comparable" across methods, but the actual counts differ substantially. For a Qwen2-7B layer (hidden=4096): LoRA (r=6) uses ~49K params, TuKA uses ~328K (6.7× more), while MoE‑LoRA (r=16, K=8) uses ~590K. TuKA thus sits between these, but the gap to simple LoRA is large enough that the reported 13‑point SR advantage (65% vs. 52%) cannot be confidently attributed to the method's architecture rather than its larger per-task parameter budget. A controlled comparison where LoRA's rank is increased to match TuKA's parameter count (or TuKA's ranks are reduced to match LoRA's) would cleanly resolve this.

3. **Forgetting rate computation is ambiguous for tasks 21–24.** The definition of F‑SRₜ (Eq. 13) states M‑SRₜ is the performance when training "solely on navigation tasks 1 through t, t ≤ 20." Yet Table 2 reports F‑SR for all 24 tasks, including T21–T24. The paper does not explain how M‑SRₜ was obtained for t > 20, whether it was fixed at M‑SR₂₀, or computed separately. This makes the reported forgetting rates for the last four tasks uninterpretable. Additionally, the construction of separate multitask models for every t (up to 20) is computationally intensive and not described — the paper should clarify the training protocol, scenes, and order used for these models.

### Minor

4. **Generalization evaluation has an asymmetric design.** In the unseen-scenario experiments (Table 5), AllDayWalker uses its stored scene/environment features to retrieve the best-matching expert via cosine similarity (Sec. 3.4). The baselines (BranchLoRA, SD‑LoRA, StreamVLN) lack any such retrieval mechanism and output a single action from the continually learned model. This asymmetry inflates AllDayWalker's apparent generalization advantage. While the retrieval mechanism is an integral part of the method, the paper should include an ablation that evaluates AllDayWalker *without* retrieval (e.g., using a randomly selected or uniformly averaged expert) to isolate the benefit of the learned expert representation from the retrieval process.

5. **Task order is not disclosed.** The paper states "the order of tasks is randomized" (Fig. 6 caption) but does not report the specific sequence used in the main experiments. Since continual learning is highly sensitive to task order, this is a reproducibility concern. The exact sequence (e.g., "{sim‑world‑v1, Normal}, {sim‑world‑v2, Low‑light}, …") should be provided in the appendix.

6. **No sensitivity analysis for regularization hyperparameters.** The total training objective weights the main navigation loss at λ = 0.5 (since λ₁=0.2, λ₂=0.2, λ₃=0.1), meaning half of the training signal comes from regularization. This is unusually high, yet the paper provides no ablation or sensitivity study for λ₁, λ₂, λ₃, or the Fisher EMA coefficient ω=0.95. The reader cannot assess whether the results are robust to these choices.

### Trivial

7. Some entries in Tables 1–2 have formatting artifacts (missing values in later columns for SD‑LoRA, EWC‑LoRA, etc.), likely from PDF extraction. The values should be verified and presented completely in the camera-ready version.

## Nice-to-Haves

- A parameter-controlled comparison (higher-rank LoRA) and capacity-controlled tensor-order ablation, as described above, would substantially strengthen the core claims.
- Reporting F‑SR for the 30‑task setting (Table 4 only shows SR) would make the scalability claim more complete.
- Training time and memory consumption comparisons would help contextualize the "parameter-efficient" claim.
- A qualitative analysis of which tasks have high F‑SR and why would add useful insight.

## Removed Points

- **Criticism about lack of benchmark standardization (not based on R2R/RxR):** The benchmark is purpose-built for the AML‑VLN problem which requires degraded imaging environments not available in standard VLN datasets. This is a reasonable design choice for a new problem setting, not a weakness.
- **Criticism about the benchmark being "self-created":** A new problem formalization necessarily requires a new benchmark. The paper provides physically grounded degradation models (Eq. 10–12) and describes the construction. The complaint is generic and applies to any paper that introduces a new task.
- **Claim that the method's advantage over matrix-based approaches is overstated:** The harsh critic argues that "matrix-based approaches can still capture multi-hierarchical knowledge through structured compositions." This is a philosophical debate about representation capacity — the paper's empirical results show that the explicit decoupling in TuKA is beneficial in practice, which is sufficient support for the claim.
- **Critique about using modal products with vectors:** The paper design choice of selecting single rows from U³/U⁴ is justified as a way to align the high-order tensor with the LLM's 2D weight matrices (a stated challenge). Whether this "reduces the tensor to an almost degenerate structure" is a modeling choice, not a mistake.
- **Criticism about the orthogonal constraint being "too restrictive":** This is speculative — the paper's results show it works well. Without evidence of failure cases, this is not a substantive weakness.
- **Criticism about FSTTA/FeedTTA descriptions being terse:** These are secondary baselines; the paper properly cites the original works. The description is adequate for context.

## Novel Insights

The reviews surface a recurring tension: the paper's strongest evidence (4th-order vs. 3rd-order tensor comparison) is also its most confounded by capacity differences. This points to a broader methodological challenge in continual learning — when comparing methods with fundamentally different architectural inductive biases, disentangling "better representation" from "more capacity" requires careful experimental design that the paper does not fully deliver. A second insight is that the expert retrieval mechanism in the generalization experiments blurs the line between the quality of learned representations and the quality of the inference-time matching procedure; separating these would give a cleaner picture of what TuKA actually learns.

Another notable point from cross-referencing the reviews: the paper claims "parameter-efficient" but the measure of efficiency matters. TuKA has fewer *cumulative* parameters across tasks than LoRA (which adds a full adapter per task), but more *per-task-instance* parameters. Which notion of efficiency is relevant depends on the deployment scenario, and the paper would benefit from being explicit about this.

## Suggestions

1. Add a capacity-controlled ablation comparing 3rd-order and 4th-order tensors at matched parameter budgets (e.g., increase r3 in the 3rd-order variant or reduce ranks in the 4th-order).
2. Add a LoRA baseline with matched parameter count (e.g., r=40 for hidden=4096) to the main comparison table, or explicitly justify why the current rank choices are standard in the LoRA literature.
3. Clarify the M‑SRₜ computation for t > 20 and explain how the multitask models were constructed (training protocol, task order, computational cost).
4. Report the exact task order used in the main experiments (in appendix).
5. Add an ablation of AllDayWalker without expert retrieval (random expert, averaged expert) for the generalization setting.
6. Add sensitivity analysis for λ₁, λ₂, λ₃ and ω (at minimum a 1D sweep around the chosen values).

## Score and Decision

I conducted calibration in two rounds. Round 1 bracketed the paper between the weak‑score band (avg < 3.5, papers scoring 2‑3) and the high‑score band (avg > 7.5). Round 2 narrowed the comparison:

| Anchor | Avg Score | Round | Comparison |
|--------|-----------|-------|------------|
| EKfcngSxwD — "Incrementally Adapting Generative VLMs with Task Codebook" | 4.67 | R2 | Weaker — our paper has a more novel method (Tucker decomposition vs. codebook of MLPs), more extensive experiments, and real-world validation, though both have evaluation concerns |
| 2oKkQTyfz7 — "General Scene Adaptation for VLN" | 6.40 | R2 | Stronger — this paper had cleaner evaluation despite limited novelty; our paper has stronger method contribution but more evaluation confounds |
| OALIb8oNfl — "Maintaining Structural Integrity in Parameter Spaces for PEFT (FLoRA)" | 5.75 | R2 | Comparable — both use Tucker decomposition for PEFT but in different domains; FLoRA has cleaner ablations while our paper has more extensive task-level validation |
| bqv7M0wc4x — "ICL-TSVD" | 5.50 | R2 | Comparable — both are CL with pretrained models; ICL-TSVD has theoretical grounding while our paper has stronger empirical breadth |
| 29sul3tAEa — "HyperAdapter" | 4.80 | R2 | Weaker — comparable CL+adapter approach but our paper has more comprehensive evaluation and a new benchmark |

The paper's strongest anchors are the GSA-VLN paper (6.40) and FLoRA (5.75). Relative to GSA-VLN, our paper has a stronger method contribution but weaker evaluation controls. Relative to FLoRA, our paper has more extensive task-level validation but less methodological rigor in ablations. Given the three major concerns (uncontrolled ablation, parameter fairness, forgetting metric ambiguity), the paper sits below the 6.4 anchor and closer to the 5.5‑5.75 range — specifically **5.5**, reflecting a solid contribution that requires significant revisions before the core claims are fully supported.

**MY FINAL SCORE: 5.5**
**MY FINAL DECISION: Reject**