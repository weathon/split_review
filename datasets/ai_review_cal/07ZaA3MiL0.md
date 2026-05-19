- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 6, 5, 3
Now I have all the information needed. Let me construct the final consolidated review.

## Summary

This paper proposes CIDM (Consistent Iterative Denoising Model) for robot manipulation, addressing two specific weaknesses of diffusion models in action prediction: (1) inconsistent denoising directions when multiple successful actions exist, and (2) time-varying noise supervision across timesteps. CIDM introduces a time-invariant denoising field with a truncated noise prediction (bounded norm beyond distance c from the target) and a radial loss that weights training samples by inverse square-root distance from successful actions. The method is evaluated on RLBench, reporting state-of-the-art average success rates of 82.3% (multi-view, 18 tasks) and 83.9% (single-view, 10 tasks).

## Strengths

- **Mathematical identification of diffusion model limitations for multimodal action spaces (Section 3.1, Equations 5–8).** The paper formalizes two concrete issues: that the score function of a mixed Gaussian points to a weighted combination of actions rather than any single successful action, and that noise predictions for the same noisy input change across timesteps. This provides clear motivation for the proposed solutions and isolates issues that prior robot manipulation works had not explicitly articulated.

- **Design of a time-invariant consistent denoising field (Section 3.3, Equation 14).** The truncated denoising field, which outputs \(y-\hat{y}\) within distance \(c\) and \(c(y-\hat{y})/\|y-\hat{y}\|\) beyond it, is a principled way to avoid confusion between multiple successful actions. The ablation (Table 3, row 1 vs. row 3) shows a 2.8% improvement over the standard diffusion field, and the temporal consistency ablation (Table 4) confirms that time-invariant training (\(\bar{\alpha}_N=1\)) significantly outperforms time-varying variants (68.4% vs. 62.0% for \(\bar{\alpha}_N=0.6\)).

- **Radial loss function (Section 3.4, Equation 15–17).** The loss weights samples by \(1/\sqrt{r}\) (capped at 10), emphasizing accuracy near successful actions where single-step denoising is expected. Ablation (Table 3, row 1 vs. row 4) shows a 3.0% improvement over standard L2 loss. This is a simple but effective design choice that directly targets the paper's identified problem.

- **State-of-the-art results on RLBench (Tables 1 and 2).** The method reports the highest average success rates among all baselines in both multi-view (82.3%) and single-view (83.9%) settings, with strong performance on challenging tasks such as "stack blocks" (a 33 percentage point improvement over the prior diffusion-based method).

## Weaknesses

### Major

- **Insufficient statistical rigor for the reported results.** The paper evaluates each task with only **4 trials** (Section 4.1: "we evaluate each task four times and take the average success probability as the performance metric") and provides no error bars, confidence intervals, or significance tests. On a benchmark where both environment randomness and the method's own sampling introduce variability, 4 trials is far too few to distinguish genuine improvement from noise. Standard RLBench evaluations (e.g., PerAct, 3D Diffuser Actor) typically use 25–100+ trials per task. The margins by which CIDM leads baselines on many tasks could easily flip with additional runs. This is a structural flaw: the central claim of state-of-the-art performance is not supported by the evidence as presented. The issue affects both the main results (Tables 1, 2) and the ablations (Tables 3, 4).

- **Critical underspecification of inference and design details.** Several details needed for reproducibility and soundness assessment are missing: (1) The initial action \(y_N\) is said to be "randomly sampled from the action space" (Section 3.2) but the distribution (uniform? Gaussian?) is never specified. (2) The hyperparameter \(c\) in the denoising field (Eq. 14) is described as "smaller than the distance between two successful actions" but how it was chosen in practice, whether it is task-specific or global, and how it interacts with action-space scale are not discussed. (3) The action space representation (ranges for translation, rotation) is not given, making it impossible to interpret the scale of \(c\) or the sampling procedure. (4) The number of denoising steps \(N\) is mentioned (\(N=100\)) only in the temporal consistency ablation; the main evaluation does not clearly state \(N\).

### Minor

- **Training-inference distribution mismatch unexamined.** During training, CIDM uses central sampling concentrated near successful actions and the radial loss further emphasizes small-noise samples. During inference, the initial action is drawn from a random distribution over the (unspecified) action space. The paper does not analyze whether the learned denoising field generalizes to inputs far from the training distribution, nor does it compare against a version trained with wider-distribution sampling to assess robustness. While the truncated field design (Eq. 14) mitigates this concern somewhat by providing uniform outputs at large distances, the absence of any analysis is a gap.

- **No evidence that the network learns a \(\hat{y}\)-independent field.** The paper asserts (Section 3.3) that training on \(\hat{y}\)-conditioned denoising fields yields a field \(\epsilon_x(y)\) that is independent of the specific successful action, but provides neither a formal argument nor empirical verification (e.g., a 2D visualization or analysis of field behavior in regions between successful actions). This is an important assumption of the method that goes unsupported.

- **Computational cost not compared.** Model size, parameter count, training time, and inference latency are not reported, making it difficult to assess practical deployment trade-offs relative to baselines.

- **Multimodality not quantified.** The paper's motivation centers on tasks with multiple successful actions, but it does not characterize which tasks are multimodal, by how much, or whether CIDM's gains correlate with multimodality.

## Nice-to-Haves

- A 2D toy-example visualization of the learned denoising field \(\epsilon_x(y)\) would concretely demonstrate that the network learns a sensible Voronoi-like segmentation of the action space.
- Analysis of the distribution of noise magnitudes encountered during inference vs. training, showing that the network's predictions remain reasonable for inputs far from the training distribution.
- Justification or ablation of the square-root form of the radial weight \(1/\sqrt{r}\) (as opposed to other functional forms).

## Removed Points

These points from the reviewers were removed with justification:

1. **"Ablation on temporal consistency is uninformative / too ambiguous" (Removed).** The paper clearly describes the experiment: a time-variable denoising field \(\epsilon_x(y;\bar{\alpha}_t\hat{y})\) where the target is scaled by \(\bar{\alpha}_t\), with \(\bar{\alpha}_t\) decreasing from 1 to \(\bar{\alpha}_N\). The network is time-invariant (no timestep conditioning). The results (Table 4) show time-invariant (\(\bar{\alpha}_N=1\)) outperforms time-varying variants. This is interpretable and informative.

2. **"Abstract implies the method chooses which action to denoise toward" (Removed).** The abstract states "designs new noise supervision to avoid interference" — this accurately describes the conditioned-field training approach. No misleading implication.

3. **"Score-function analysis is standard / claim it's specific to robot manipulation is overstated" (Removed).** The paper frames the analysis in the context of robot manipulation action spaces where data is scarce; it does not claim the mathematical properties are unique to this domain. The framing is appropriate.

4. **"Radial loss justification is not formally derived / \(\delta(r)\) form is ad-hoc" (Removed).** The paper provides clear motivation: high weight near successful actions, upper bound to avoid instability. Formal derivation is not required for an empirical systems paper; the ablation validates the design.

5. **"Baseline results source is unclear" (Removed).** The paper states it follows the settings of PerAct and GNFactor. Citing published baseline numbers under matched protocols is standard practice in RLBench evaluations.

6. **"The method's contribution may be largely due to training distribution rather than field design or loss" (Removed).** The ablations transparently separate each component's contribution: central sampling (7.3%), denoising field (2.8%), radial loss (3.0%). The paper is clear about what each component contributes.

7. **"Temporal consistency ablation needs more details (timestep conditioning, loss function)" (Removed).** The experiment replaces \(\hat{y}\) with \(\bar{\alpha}_t\hat{y}\) in the denoising field; the loss function is the radial loss (consistent across experiments). The network is time-invariant by design. The description is adequate for understanding the comparison.

## Novel Insights

None beyond the paper's own contributions. The synthesis of the two reviewers' perspectives confirms that the paper's core methodological contribution is well-motivated and clearly presented, but that the experimental validation has a significant structural weakness (inadequate trial count, missing specification of key design choices) that prevents the results from being taken as conclusive. No novel insight emerges that the paper itself does not provide.

## Suggestions

- **Re-run the main evaluation with at least 25–50 trials per task and report error bars (standard deviation or 95% confidence intervals)**. This is the single most impactful improvement. The current 4-trial protocol cannot support the claimed state-of-the-art results.
- **Explicitly specify the action space representation, bounds, and the sampling distribution for initial inference actions.**
- **Clearly state how the hyperparameter \(c\) is chosen** (is it task-specific? a fixed value? how does it relate to action space scale?).
- **Report the number of denoising steps \(N\)** used in the main evaluation (the ablation mentions \(N=100\); clarify if this is consistent).
- **Include an analysis or visualization of the learned denoising field** (even in 2D) to support the claim that the network learns a \(\hat{y}\)-independent field.
- **Compare computational cost** (model size, inference time) against baselines.
