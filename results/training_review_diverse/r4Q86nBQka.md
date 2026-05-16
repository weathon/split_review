Now I have all the information I need. Let me produce the final consolidated review.

## Summary

INNAprop combines the Dynamical Inertial Newton (DIN) continuous-time system with RMSprop adaptive gradient scaling to create a new optimizer whose memory footprint matches AdamW. The algorithm replaces Hessian-vector products with a finite difference of gradients (g_k − g_{k−1}), avoiding costly second-order computations. Empirical evaluation on CIFAR-10, ImageNet, Food101, and GPT-2 (pre-training and LoRA fine-tuning) shows that INNAprop consistently matches or slightly outperforms AdamW.

## Strengths

1. **Principled derivation from a continuous-time ODE.** The paper derives INNAprop from the DIN dynamical system (a second-order ODE with Newtonian effects) combined with RMSprop scaling (Section 2.2). This gives the algorithm a clear theoretical grounding and distinguishes it from purely heuristic adaptive methods. The connection between Hessian-vector products and gradient differences (d/dt ∇J(θ(t))) is correctly identified and exploited.

2. **Memory footprint equivalent to AdamW.** Through a change of coordinates (introducing the ψ auxiliary variable), the algorithm uses only three full-size memory slots (v_k, ψ_k, θ_k), matching Adam's memory requirements (Section 2.2). This is a genuine practical advantage over Hessian-based optimizers like Sophia or Shampoo and is well-articulated in the paper.

3. **Consistent (if modest) empirical outperformance across diverse benchmarks.** INNAprop matches or beats AdamW on CIFAR-10 (e.g., ResNet18: 91.58 vs. 91.14), ImageNet (ResNet18: 70.12 vs. 69.34, ViT-B/32: 75.23 vs. 75.02), GPT-2 pre-training (validation loss lower across all model sizes), and GPT-2 LoRA fine-tuning (perplexity lower across all sizes). The direction of the improvement is consistent, which is non-trivial for a new optimizer.

4. **Systematic bias toward AdamW in hyperparameter tuning.** The tuning protocol (Table 1) reuses AdamW's learning rate, scheduler, and weight decay for INNAprop, only tuning the new (α, β) parameters on CIFAR-10. This is a principled and honestly-stated approach that strengthens the claim that INNAprop is easy to use.

5. **Actionable hyperparameter recommendations.** The grid search on CIFAR-10 (Figure 2) identifies two useful regimes: (α, β) = (0.1, 0.9) for fast early training and (α, β) = (2.0, 2.0) for better final accuracy on long runs. The conclusion gives concrete recommendations for LLMs vs. image classification, making the method immediately usable.

## Weaknesses

### Fatal

None.

### Major

1. **Only AdamW as a baseline, and potential omission of Sophia comparison data.** The paper compares INNAprop to AdamW exclusively across all experiments, even though the introduction discusses several other relevant optimizers (Sophia, Lion, AdEMAMix). This is particularly concerning because:
   - Sophia was explicitly designed as a Hessian-aware optimizer for LLMs — the exact claimed niche of INNAprop — yet is never compared.
   - The GPT-2 figure file is named `gpt2_all_models_with_sophia.pdf` (line 328), strongly suggesting that Sophia results exist in the figure, but the paper's text, tables, and conclusions never mention or discuss Sophia's performance. If Sophia data appears in the figure without discussion, this is a significant omission that could reflect selective reporting. If the filename is misleading, it should be corrected.
   
   Without comparisons to at least one other recent optimizer, the paper cannot support its claim that INNAprop is a "promising competitor" beyond simply matching AdamW.

2. **No uncertainty quantification, despite small effect sizes.** The reported improvements over AdamW are modest in many cases:
   - ResNet-50 on ImageNet: +0.10 pp Top-1 accuracy
   - ViT-B/32 on ImageNet: +0.21 pp Top-1 accuracy
   - GPT-2 small LoRA perplexity: 3.48 vs. 3.44 (0.04 difference)
   - GPT-2 medium LoRA perplexity: 3.20 vs. 3.17 (0.03 difference)
   
   No standard deviations, confidence intervals, or statistical significance tests are reported anywhere in the paper. CIFAR-10 uses 8 seeds (reasonable), ImageNet ResNets use 3 seeds, and ViT uses only 1 seed. Given the small effect sizes, it is impossible for the reader to assess whether these differences are reproducible or within the noise of the training setup. This is the single most important weakness for a paper whose primary contribution is empirical.

3. **Inconsistent hyperparameter protocol across experiments.** The paper states that AdamW is systematically favored (Table 1), but several choices deviate from this stated protocol in ways that could advantage INNAprop:
   - For ResNet-50 on ImageNet, INNAprop uses (α, β) = (1.0, 1.0), which was **not** one of the pairs selected from CIFAR-10 tuning (where (0.1, 0.9) and (2.0, 2.0) were chosen). The paper's Remark 2.3 states that (1, 1) empirically recovers AdamW behavior — making it an odd choice for demonstrating improvement.
   - For GPT-2 pre-training, INNAprop uses σ = 0.99 while AdamW uses β₂ = 0.95 — a material difference in the gradient averaging window that could independently affect performance.
   - For ResNet-50, weight decay differs between AdamW (λ = 0.1) and INNAprop (λ = 0.01, selected after trying both values).
   
   This inconsistent tuning makes it difficult to attribute improvements to the INNA dynamics versus hyperparameter choices.

### Minor

1. **"Second-order" framing is overstated.** The paper's title and abstract describe INNAprop as using "second-order information," but the algorithm replaces Hessian-vector products with a finite difference of gradients (g_k − g_{k−1}). This is a first-order approximation that provides no curvature information beyond what is captured by the change in gradient over one step. The paper is transparent about the mechanics (Section 2.2 correctly identifies d/dt ∇J(θ) = ∇²J(θ)θ̇), but the "second-order" branding throughout (title, abstract, introduction claims) is stronger than what the algorithm actually delivers and invites unrealistic expectations.

2. **The "Steps to match AdamW" metric conflates early and late convergence.** This unconventional metric (Table 4) reports the step at which INNAprop reaches AdamW's *final* validation loss. This depends entirely on where AdamW was stopped and says nothing about what would happen with longer training. Standard convergence curves with shaded error regions and final means would be more informative.

3. **No ablation studies.** The paper never isolates the contribution of each component: there is no comparison to INNA without RMSprop scaling, nor to RMSprop with INNA-like momentum (beyond a brief remark about numerical instability). Ablations would clarify whether the improvement comes from the INNA dynamics, the RMSprop scaling, or their specific combination.

4. **No wall-clock time or memory measurements.** The paper claims the memory footprint is "equivalent to AdamW" and that per-step cost is similar, but provides no measurements of either. A simple table comparing parameter memory, gradient memory, optimizer states, and per-iteration time would be straightforward and convincing.

5. **No discussion of limitations or failure cases.** The paper does not discuss when INNAprop might underperform (e.g., very large batch sizes, non-smooth losses, the practical implications of the γ_k < β constraint, or what happens if the scheduler violates it during warmup).

### Trivial

- The ψ₀ = (1 − αβ)θ₀ initialization (Algorithm 1) and its effect are not analyzed or justified.

## Nice-to-Haves

- A comparison to at least one additional recent optimizer (Sophia or Lion) would substantially strengthen the practical relevance claim.
- Standard deviations or 95% confidence intervals on all main numerical results (Tables 2–4).
- An ablation comparing INNAprop to INNA without RMSprop and to RMSprop with standard momentum.

## Removed Points

- **"RMSprop with momentum is numerically unstable — unsupported claim":** The paper does reference Figure \ref{fig:innaprop_momentum} for this (Remark 2.2), so the criticism that "no experiment or reference is given" is inaccurate. Removed.
- **"Missing code release":** Code release is standard practice but not a requirement for validity. Removed per instructions on reproducibility nitpicks.
- **"Missing limitations section":** While a limitations section would be welcome, the absence is not a structural flaw; the paper has a conclusion that summarizes findings and mentions future work. Downgraded to a minor point and merged.
- **Generic formatting or phrasing nitpicks:** Removed per instructions.

## Novel Insights

None beyond the paper's own contributions. The key novel observation — that a specific change of coordinates in the discretized DIN + RMSprop ODE reduces memory from 6 to 3 slots while preserving the dynamics — is already presented in Section 2.2. The reviewer materials do not surface any additional insight not already in the paper.

## Suggestions

1. **Expand baselines.** At minimum, compare INNAprop to Sophia on GPT-2 (since the figure filename already suggests these results exist). Adding Lion and AdEMAMix on ImageNet would further strengthen the paper. Clarify what the "with_sophia" figure contains and discuss it in the text.
2. **Add uncertainty quantification.** Report means ± std or 95% confidence intervals for all key metrics. For small differences (e.g., 0.10 pp on ResNet-50), a paired bootstrap or t-test would help establish reliability.
3. **Fix the hyperparameter protocol.** Either (a) commit to the CIFAR-10 tuned (α, β) values without modification for all larger experiments, or (b) tune all hyperparameters per-task and report both configurations. Avoid settings like (1.0, 1.0) that are described as recovering AdamW behavior.
4. **Tone down the "second-order" language.** Use precise wording: "curvature-aware" or "Newton-inspired" rather than "second-order information," to accurately reflect that only gradient differences are used.
5. **Add a wall-clock time comparison** and a brief memory usage table to substantiate the claimed practical advantages.

## Score and Decision

The paper presents a clean, principled combination of two well-known ideas (INNA + RMSprop) with a nice memory-saving coordinate transformation. The algorithm is plausible and the consistent (if modest) improvements over AdamW across multiple benchmarks are suggestive. However, the empirical evaluation has significant gaps: only one baseline (AdamW), no uncertainty quantification, suggestive but unacknowledged Sophia data in a figure, and an inconsistently applied hyperparameter protocol. The improvements are small enough that until uncertainty is quantified and at least one additional baseline is compared, the paper's core claim ("promising competitor") is not fully supported.

The contribution is real but incremental, and the paper would benefit from addressing the major weaknesses before acceptance at a competitive venue.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>