- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 5, 6
Now I have a thorough understanding of the paper. Let me construct the final review.

## Summary

This paper introduces INNAprop, an optimizer that combines the Dynamical Inertial Newton (DIN) method with RMSprop adaptive gradient scaling. The key idea is to leverage second-order information via a gradient-difference trick that avoids explicit Hessian computation while keeping the memory footprint equivalent to AdamW (3 full-dimension slots). The paper evaluates INNAprop on CIFAR-10, ImageNet, Food101 (image classification), and GPT-2 pre-training/fine-tuning, reporting consistent improvements over AdamW in both training speed and final accuracy.

## Strengths

- **Memory footprint equivalent to AdamW**: Section 2 explicitly derives the reduction from 6 to 3 memory slots ($v_k$, $\psi_k$, $\theta_k$), matching AdamW's memory while retaining second-order-like dynamics. This is a concrete engineering contribution that matters for large-scale training.

- **Conservative tuning protocol favoring AdamW**: Table 1 systematically documents that learning rates, schedulers, and weight decay are reused from AdamW settings — INNAprop only tunes its own hyperparameters ($\alpha,\beta$). On CIFAR-10, CIFAR-10 (ResNet18/VGG11/DenseNet121), and Food101, all experiments use matched $\lambda$ and $\sigma$ between optimizers, and INNAprop still achieves modest gains (e.g., 91.58 vs 91.14 on ResNet18 CIFAR-10, 70.12 vs 69.34 on ResNet18 ImageNet), strengthening the robustness claim.

- **Consistent positive signal across diverse settings**: Despite small margins, INNAprop outperforms AdamW in final accuracy on every single benchmark reported — CIFAR-10 (3 architectures), ImageNet (3 architectures), Food101, GPT-2 pre-training (3 sizes), and GPT-2 LoRA fine-tuning (3 sizes). The direction of improvement is uniform, which is unlikely to arise from chance alone.

- **Theoretical grounding and unification**: The derivation from the continuous DIN ODE (Section 2) provides geometric insight, and Remark 2 notes that $\alpha=\beta=1$ empirically recovers AdamW behavior, offering practitioners a clear connection between the methods.

## Weaknesses

### Fatal
None.

### Major
- **"Steps to match AdamW" metric is undefined**: Table 4 reports values like "51,000 (1.96× faster)" without any explanation of how this quantity is computed. The reader cannot determine whether this measures the iteration at which INNAprop surpasses AdamW's *final* loss, the earliest crossing point, or something else entirely. The 1.96× speedup claim for GPT-2 mini is striking and would normally warrant careful justification, but it is presented without definition or validation. This undermines the paper's training speed claims.

- **ResNet-50 ImageNet comparison uses different weight decay**: For the ResNet-50 experiment, AdamW uses $\lambda=0.1$ (from the literature) while INNAprop uses $\lambda=0.01$ (selected because "it resulted in a faster decrease in training loss"). The paper does not report INNAprop's accuracy with $\lambda=0.1$ or AdamW's accuracy with $\lambda=0.01$. Since weight decay directly affects generalization, the 76.43 vs 76.33 advantage cannot be cleanly attributed to the optimizer. This is acknowledged in passing but the claim "Table 3... illustrates the advantage of INNAprop" overstates what the evidence supports.

- **GPT-2 pre-training uses different RMSprop decay**: For GPT-2 from scratch, INNAprop uses $\sigma=0.99$ while AdamW uses $\beta_2=0.95$. The paper states $\sigma=0.99$ was selected as the best among $\{0.9, 0.95, 0.99\}$ on GPT-2 mini, but no results for $\sigma=0.95$ (matching AdamW) are reported for the larger models. This confounds the comparison — the lower validation loss could partially reflect the different momentum decay rather than the DIN dynamics. The GPT-2 LoRA experiment is cleaner (matched $\sigma=0.999$), which partially mitigates this.

### Minor
- **ViT-B/32 ImageNet result from a single seed**: Table 3 reports Top-1 accuracy of 75.23 vs 75.02 (a 0.21pp advantage) from one run. The caption states "one run for ViT-B/32." With typical seed variation for ViT training, this margin is within noise range. A result this close needs at least 3 seeds to be convincing.

- **The "second-order" claim is heuristic in the stochastic setting**: The paper uses the identity $\nabla^2\mathcal{J}(\theta)\dot{\theta} = \frac{d}{dt}\nabla\mathcal{J}(\theta)$, which is exact for deterministic gradients. With mini-batch gradients, the discrete approximation $\nabla\mathcal{J}(\theta_{k+1})-\nabla\mathcal{J}(\theta_k)$ does **not** equal $\nabla^2\mathcal{J}(\theta_k)(\theta_{k+1}-\theta_k)$ in expectation due to gradient noise. The paper frames the method as having "second-order intelligence" without discussing this caveat, which would be a valuable addition for scientific clarity.

- **Per-task tuning of $(\alpha,\beta)$**: The CIFAR-10 tuning recommends $(0.1,0.9)$ for fast progress and $(2.0,2.0)$ for best final accuracy, but on ImageNet, the chosen pairs differ per model: $(0.1,0.9)$ for ResNet-18, $(1.0,1.0)$ for ResNet-50, $(0.1,0.9)$ for ViT. The paper acknowledges that $(2.0,2.0)$ "shows no clear advantage" on ResNet-50 and suggests future scheduler design. This is not a fatal flaw but indicates that the CIFAR-10 tuning does not transfer cleanly, and the ImageNet choices appear somewhat *post hoc*.

### Trivial
- In the GPT-2 section (line 324), the text reads "we use the RMSprop parameter $\sigma = 0.99$ (corresponding to $\beta_2$ for AdamW)" — this is slightly confusing since AdamW's $\beta_2$ is 0.95 in that experiment, not 0.99. Clarify.

## Nice-to-Haves
- Include a comparison to at least one more contemporary optimizer (e.g., Lion, Sophia, or AdEMAMix) on at least one benchmark to contextualize the improvement over AdamW relative to the broader optimizer landscape.
- Add seed-level individual results (or standard deviations) for the GPT-2 experiments to allow assessment of variability.
- Consider adding a limitations paragraph discussing when INNAprop might underperform (e.g., sensitivity to the $\beta > \gamma_k$ constraint, possible instability at certain $(\alpha,\beta)$ extremes).

## Removed Points
These points from the input reviews are excluded with brief justification:

1. **"Sophia results appear in the figure but are not discussed"** — The figure filename is `gpt2_all_models_with_sophia.pdf`, but the paper text states it uses AdamW hyperparameters *from the Sophia paper* (citing liu2023sophia for the configuration). The paper does not claim to compare to Sophia, and the figure caption does not mention Sophia. Whether Sophia curves are actually plotted cannot be determined from the text alone. This is speculative and removed.

2. **"Heatmaps labeled with single seed" criticism** — The heatmap caption already states "with one random seed." The criticism that it "should be labeled" is incorrect; it already is. Removed as factually wrong.

3. **"Food101 provides no architectural variety beyond CIFAR-10"** — This is a scope criticism that does not identify an actual flaw. The experiment serves its purpose (transfer learning validation). Removed.

4. **"$\alpha=\beta=1$ recovery not proven"** — The paper says "empirically recover" and "Experiments demonstrate that this consistently aligns with AdamW." This is an empirical claim, not an unsubstantiated one. Removed.

5. **"Table formatting confusing"** — A presentation nitpick with no substantive content. Removed.

6. **"AdamW's $\lambda$ suboptimal for ResNet-18"** — The paper is transparent about changing $\lambda$ from 0.05 to 0.01 to improve AdamW's baseline. Both optimizers use the same $\lambda$. This is a strength of the protocol, not a weakness. Removed.

## Novel Insights
None beyond the paper's own contributions. The reviews primarily surface methodological concerns about comparison fairness and metric definition that the authors should address but do not introduce new analytical perspectives on the method itself.

## Suggestions
1. Define the "Steps to match AdamW" metric explicitly in the main text (e.g., "the earliest iteration at which INNAprop's validation loss falls below AdamW's final validation loss"), and show the reference line on the loss curves.
2. For the confounded experiments (ResNet-50 with different $\lambda$, GPT-2 with different $\sigma$), run the missing controlled conditions: INNAprop with AdamW's $\lambda=0.1$ on ResNet-50, and INNAprop with $\sigma=0.95$ (matching AdamW's $\beta_2$) on GPT-2. Report the results even if they are worse.
3. Run the ViT-B/32 ImageNet experiment with at least 3 seeds to establish statistical significance of the 0.21pp advantage.
4. Add a brief caveat in Section 2 that the gradient-difference approximation of the Hessian is exact only for full-batch gradients and becomes heuristic with mini-batches.
