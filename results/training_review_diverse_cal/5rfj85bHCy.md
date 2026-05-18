Now I have all the information needed to write the consolidated review. Let me compose it.

## Summary

The paper introduces HyResPINNs, a novel PINN architecture that combines standard DNNs with radial basis function (RBF) networks within adaptive residual blocks. A learnable parameter α (passed through sigmoid) controls the convex blend of DNN and RBF outputs per block, while β parameters govern residual skip connections. The motivation is to handle PDE solutions containing both smooth regions (handled by the DNN) and sharp features/discontinuities (handled by the compactly supported RBF component). The method is evaluated on the 1D Allen-Cahn equation and 2D/3D Darcy Flow problems against PINN, ExpertPINNs, ResPINNs, PirateNets, and StackedPINNs.

## Strengths

1. **Architectural novelty with clear motivation.** The hybrid residual block design (Eq. 5) that forms a convex combination of DNN and RBF outputs via a learnable, sigmoid-gated parameter is a clean and well-motivated idea. It directly addresses the known limitation that standard DNN-based PINNs struggle with sharp transitions and discontinuities (lines 47–56). This design is structurally simple enough to be adopted as a drop-in replacement for standard residual blocks.

2. **Compact Wendland kernel for computational efficiency.** The choice of the compactly supported Wendland C⁴ kernel (Eq. 8) ensures sparse kernel matrices (line 211), which is a practical design decision that keeps the RBF overhead in check—an advantage over global RBFs that would scale poorly with data size.

3. **Evaluation across multiple challenging PDEs and against strong baselines.** The method is tested on the Allen-Cahn equation (nonlinear, sharp interfaces) and Darcy Flow with both smooth and rough coefficients, comparing against five baselines including recent state-of-the-art methods (PirateNets, StackedPINNs, ExpertPINNs). This breadth gives reasonable coverage of the claims.

## Weaknesses

### Fatal

None.

### Major

1. **Claimed robustness to training point locations and neural network architectures is unsupported.** The abstract (line 8) states "HyResPINNs are more robust to training point locations and neural network architectures than traditional PINNs," and the conclusion (line 292) reiterates "robustness." However, the visible text contains no experiment that varies training point sampling strategies (random vs. grid vs. adaptive) or DNN architecture (depth, width, activation function). The existing benchmarks test different PDEs, which is robustness to *problem type*, not to the dimensions claimed. This is a significant overclaim—the paper cannot substantiate a headline selling point in its own abstract. The authors should either add dedicated experiments or remove/qualify this claim.

2. **Missing experimental details prevent reproducibility.** Several critical specifications are absent from the paper text:
   - **Loss weights** (λ_ic, λ_bc, λ_r, λ_p) are introduced in Eq. (7) but their numerical values are never given. These control the relative importance of initial conditions, boundary conditions, PDE residual, and the α regularization, and any of them can dominate training behavior.
   - **Number and initialization of RBF centers per block.** The paper states centers are optimized via gradient descent (line 212) but never states how many centers are used, how they are initialized (e.g., randomly placed on a grid?), or whether this count scales with input dimension. The figure captions reference numbers like "centers_12" and "centers_20" but the text does not explain these.
   - **No error bars, multiple seeds, or uncertainty quantification.** Given the strength of the claims ("orders of magnitude greater accuracy," line 9), the absence of any multi-run statistics is a concern. A single run could be an outlier. The PINN community often reports single runs, but exceptionally strong claims demand stronger evidence.

3. **The β-based residual connection is never formally defined.** The paper says "We further incorporate adaptable residual connection parameters between each hybrid block, denoted as β^(l)—similar to the approaches in [22] and [23]" (line 164) and states β^(l) = 1 initialization (line 168), but never writes the forward pass that uses β. The core architectural contribution has "residual" in its name; omitting the equation that defines how the residual connection works (e.g., x^(l+1) = β^(l)·H^(l)(x^(l)) + (1−β^(l))·x^(l) or similar) is a non-trivial specification gap. Readers should not be required to consult two external papers to reconstruct the architecture.

### Minor

4. **The L₂ regularization on α works against the adaptivity mechanism in an unexamined way.** The regularization λ_p Σ α_i² (Eq. 7) penalizes deviations of the raw α from 0, which pushes the sigmoid output toward 0.5 (equal blend). If a problem genuinely requires strong RBF specialization (sigmoid output near 1), the regularization opposes that. The paper's stated motivation—"to encourage smoother solutions" (line 177)—is valid, but the trade-off between regularization and adaptivity is neither discussed nor ablated. A simple experiment with λ_p = 0 vs. λ_p chosen would clarify whether the regularization is even needed and whether it harms adaptivity on problems with sharp features.

5. **Training time comparison is missing.** The paper claims "only modest increases in training costs" (line 9, also line 292) but provides no wall-clock runtime numbers or parameter counts for HyResPINNs vs. baselines. Without these, the reader cannot assess the practical cost-benefit trade-off.

### Trivial

6. **The notation for α is ambiguous.** Eq. (5) uses α inside a sigmoid ϕ(α), implying α ∈ ℝ is a raw parameter. But lines 168–169 discuss α as if it is the blend weight directly ("When α = 1, only the RBF contributes; when α = 0, only the DNN contributes"). Since sigmoid(1) ≈ 0.73 and sigmoid(0) = 0.5, these statements are inconsistent with Eq. (5). The initialization "α^(l) = 0.5" (line 168) would give sigmoid(0.5) ≈ 0.62, not 0.5. This sloppiness makes the regularization discussion harder to evaluate precisely.

## Nice-to-Haves

- An ablation study with three conditions: (a) fixed α = 0.5 (equal blend, no adaptivity), (b) adaptive α with λ_p = 0, (c) adaptive α with λ_p > 0. This would directly validate the core design choice and clarify the role of regularization.
- A figure showing learned α and β values per block after training on each problem. Since the adaptivity is the distinguishing mechanism, readers need to see whether α actually moves away from 0.5 and in which direction for smooth vs. sharp problems.
- Comparison of different RBF kernel types (Gaussian, multiquadric) to justify the Wendland choice empirically.

## Removed Points

These points from the reviewers are removed or downgraded with justification:

- **"The L₂ regularization is the opposite of what the paper advertises" (Harsh Critic, Issue 1, part)**: Overstated. The regularization is a mild prior (controlled by λ_p) toward balanced blending. It does not prevent adaptivity when the PDE loss gradient is strong. Downgraded to Minor.
- **"Combination of RBF and DNN before nonlinear activation is not a true combination of two representations" (Harsh Critic)**: Design preference, not a weakness. Pre-activation gating is a standard approach (e.g., GLU variants, gated residual networks). Removed.
- **"Choice of Wendland C⁴ kernel without justification" (Harsh Critic)**: The paper does justify it—compactly supported for sparsity and efficiency (line 211). An ablation would be nice but is not required. Removed from weaknesses.
- **"Robustness to problem type and architecture across multiple benchmarks" (Strength Finder)**: Conflicts with verified weakness #1. The paper tests different PDEs (robustness to problem type) but does not test varying architectures or training point locations as claimed. Downgraded in strength framing.
- **"Regularization on α parameters to control excessive nonlinearity" (Strength Finder)**: Conflicts with verified weakness #4 about the regularization-adaptivity tension. The claimed benefit is not ablated. Removed as a strength.

## Novel Insights

The most interesting observation not fully developed in the paper is the synergy between the Wendland kernel's compact support and the adaptive blending mechanism. The Wendland kernel provides local, sparse corrections exactly where sharp features occur, while the global DNN handles the smooth background. If the learned α values per block systematically correlate with regions of high solution curvature, this would provide a powerful interpretability tool—effectively telling the user where the solution is non-smooth. The paper has the data to show this (it has learned centers and α values) but does not present it.

## Suggestions

1. **Tone down the robustness claim** in the abstract and conclusion to match what is actually tested (robustness across problem types, not across training point strategies or architectures). Alternatively, add the experiments needed to support the claim.
2. **Add the missing β residual connection equation** to Section 3.1, e.g., x^(l+1) = β^(l)·H^(l)(x^(l)) + (1−β^(l))·x^(l).
3. **Report the loss weight values** (λ_ic, λ_bc, λ_r, λ_p) and the number/initialization of RBF centers per block. If these differ per problem, provide a table.
4. **Add an ablation** with λ_p = 0 to show the effect of α regularization on both the learned blend weights and the final accuracy.
5. **Clarify the α notation**: distinguish the raw parameter from the sigmoid-squashed blend weight. The current text conflates them.
6. **Include at least 3 random seeds** for the headline results, or at minimum report parameter counts to show that accuracy gains are not purely from increased model capacity.

## Score and Decision

**Originality**: Good—the hybrid DNN+RBF residual block with learnable blending is a novel contribution to the PINN architecture space.

**Importance of research question**: High. Handling mixed smooth/sharp solutions is a recognized limitation of PINNs, and a practical solution would be valuable.

**Claims support**: Weak. The strongest claims (robustness to training point locations and architectures, "orders of magnitude" gains) lack sufficient experimental substantiation in the visible text.

**Soundness**: Adequate but not strong. The architecture is sound, but the experimental methodology has significant gaps (no error bars, missing ablation on the core mechanism, unreported hyperparameters).

**Clarity**: Below average. The β mechanism is not formally defined, the α notation is inconsistent, and several critical experimental details are missing.

**Value to community**: Moderate. If the gaps are addressed, the architecture could be adopted by practitioners; in the current form, the contribution is not well-enough specified to enable reproduction or reliable application.

The paper presents a genuinely novel architectural idea for PINNs that addresses a real limitation. However, the presentation has multiple specification gaps, and the strongest claims outrun the evidence. The core contribution is worth developing, but the paper is not ready for publication in its current form.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>