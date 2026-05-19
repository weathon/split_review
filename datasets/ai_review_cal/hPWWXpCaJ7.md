- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6
Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes GEVRM, a closed-loop vision-language-action (VLA) model that incorporates principles from classical internal model control (IMC) to improve robustness to visual perturbations. The method combines a text-guided video diffusion model for generating expressive future goal states with prototypical contrastive learning that aligns current and goal state representations, thereby implicitly estimating and compensating for external perturbations. Experiments on the CALVIN benchmark and the Bridge dataset show strong improvements in goal generation quality (FID: 94.47 vs. 236.75 for GR-1) and action execution on both standard and perturbed settings.

## Strengths

- **Novel integration of IMC principles into VLA for perturbation robustness.** The paper is the first to instantiate the classical IMC framework within a modern VLA model, mapping the IMC components (reference input, internal model, feedback) to video goal generation, prototypical contrastive state alignment, and goal-conditioned diffusion policy. This conceptual framing is well-motivated and clearly described (Figure 1, Section 4).

- **Goal generation quality far exceeds prior work.** On the goal generation task (Table 1), GEVRM achieves FID 94.47 and FVD 3.8, compared to GR-1's 236.75 FID and 12.83 FVD — more than halving FID and reducing FVD by over 70%. This is a large, concrete improvement in video prediction quality for robotics.

- **State alignment is empirically essential.** The ablation (Figure 5a) shows that removing state alignment reduces average task completion length on CALVIN Env. D from ~2.7 to ~2.1, and removing VAE fine-tuning causes a similar drop. The t-SNE visualization (Figure 6) further confirms that state alignment produces tighter intra-class clustering and better temporal consistency.

- **Strong action execution on standard CALVIN.** In the ABC→D zero-shot setting (Table 2), GEVRM achieves higher chain completion than UniPi, GR-1, and HiP, demonstrating that the framework's benefits are not confined to perturbed environments.

## Weaknesses

### Fatal

None.

### Major

- **Overclaim about real-robot execution performance.** The abstract states that GEVRM "shows significant improvements in realistic robot tasks" and the conclusion claims "state-of-the-art performance in simulated and realistic visual manipulation tasks." However, no closed-loop action execution was performed on real robots; the only use of real data (Bridge dataset) is for evaluating goal generation quality via FID/FVD. While the Bridge evaluation is valuable, the phrasing "realistic robot tasks" and "realistic visual manipulation tasks" misleadingly implies real-robot execution. This overclaim should be corrected by qualifying the scope of the "realistic" evaluation.

- **No variance or confidence intervals reported.** Every quantitative result (Tables 1, 2, 3, Figure 5) is reported as a point estimate without standard deviation, confidence intervals, or number of seeds. Given that CALVIN evaluations use long-horizon chain tasks, single-run results could be noisy. This is a significant evidential gap — the reader cannot assess whether the reported improvements (e.g., the 45.9% improvement in average completion length under perturbations) are reliable or within noise range.

- **Narrow baseline comparison for the core robustness claim.** The perturbed-environment evaluation (Table 3) compares GEVRM only to SuSIE. Claiming "state-of-the-art" for perturbation robustness on this basis is premature. Other methods that address distribution shift or robustness in VLA (e.g., through data augmentation, domain randomization, or robust policy training) should be included, or the claim should be scoped to "outperforms the data-augmentation baseline SuSIE."

- **Ablation of the core robustness mechanism is on the wrong setting.** Figure 5 ablates VAE fine-tuning and state alignment on the *standard* CALVIN D environment, not on the perturbed setting. Since the paper's central thesis is that state alignment improves robustness specifically under perturbations, the most relevant ablation — full model vs. no state alignment on perturbed D — is missing. The current ablation shows these components matter for generalization, but does not directly test the IMC-robustness claim.

### Minor

- **Citation error in baseline description.** In Section 5.2 (Action Execution), GR-1 is cited as "(Black et al., 2023)" but the correct reference is Wu et al. (2023). (The same paper correctly cites GR-1 as Wu et al., 2023 in both the Related Work and the Goal Generation baselines.) This does not make the experimental comparison uninterpretable — the method is correctly named and described — but it is a factual error that should be fixed.

- **Missing implementation details for reproducibility.** The number of prototypes N, the temperature δ in the Sinkhorn-Knopp step, the source of the pre-trained 2D VAE and 3D VAE, and exact training hyperparameters (learning rates, batch sizes, number of diffusion steps) are not specified. These details are important for reproducing the work.

- **Goal state usage ambiguity in test-time execution.** Section 4.3 mentions sampling "a set of goals {x_{m,goal}}" but then refers to passing "goal state x_{t,goal}" (singular). It is unclear whether a single frame (e.g., the last frame of the generated video) is used as the goal, or whether multiple frames are used as sub-goals sequentially. This should be clarified.

### Trivial

- The paper lacks a limitations section, which would be valuable given the method's dependence on a pre-trained video generation model and the assumption that text-video pairs are available for planner training.

## Nice-to-Haves

- An analysis of how internal embeddings change under different perturbation types (e.g., correlation between embedding shift and perturbation magnitude) would strengthen the claim that the model "implicitly infers and distinguishes perturbations."
- A discussion of inference time / computational cost would be helpful for practical deployment assessment.

## Removed Points

- **"Problem Formulation claim about text-video pairs is misleading"** (Harsh Critic). The paper says the planner *can be* trained on text-video pairs "which can be derived from large-scale video clips with language labels and robot sequence decision data." This is a statement about the framework's potential data-efficiency advantage, not a false claim about what the experiments actually do. The experiments use robot data, which the paper acknowledges. Removed because the paper's framing is reasonable and the criticism overstates the issue.

- **"Related Work does not connect to learning-based IMC in robotics"** (Harsh Critic). The paper already cites Bu et al. 2024 as a closely related closed-loop visuomotor framework. Demanding more exhaustive coverage of learning-based IMC approaches is scope creep; the paper's contribution is in instantiating IMC within VLA, not in surveying all prior IMC implementations. Removed as scope creep.

- **"Table 1 has no per-task columns"** (Harsh Critic). The table image is garbled by the parser; in the original submission the table likely has proper formatting. Removed as a parser artifact issue.

- **"The random mask 75%/25% split is not ablated"** (Harsh Critic). This is a minor design choice that the paper provides a reasonable justification for (testing uses historical frames, so unmasking first h frames gets highest weight). Requesting an ablation of every hyperparameter is excessive. Demoted to Nice-to-Have at most, but removed from weaknesses.

- **"Qualitative comparison is not quantified"** (Harsh Critic). Figure 3 is a qualitative comparison, which is standard practice; the paper already provides quantitative FID/FVD results (Table 1) that support the same conclusion. Not a weakness.

## Novel Insights

The most interesting observation from cross-referencing the reviewer perspectives is that the paper's strengths and weaknesses are tightly interwoven: the most impressive result (45.9% improvement in perturbed task completion length) is simultaneously the least statistically supported (no variance) and the most narrowly benchmarked (only one baseline). This pattern — large reported gains without reliability metrics — recurs across all three main tables and is the primary barrier to trusting the results. The reviewers agree that the IMC-to-VLA conceptual mapping is genuinely novel and well-executed, but the evidential standards for the empirical claims fall short of what a "state-of-the-art" assertion requires.

## Suggestions

1. **Correct the overclaims.** Replace "realistic robot tasks" / "realistic visual manipulation tasks" with "goal generation on real-robot data (Bridge dataset)" to accurately reflect what was evaluated.
2. **Add variance estimates.** Report results from at least 3 seeds with standard deviations for the main CALVIN experiments (Tables 2 and 3).
3. **Ablate state alignment on perturbed environments.** Run the "w/o SA" variant on the perturbed D setting to directly test whether the core IMC-inspired mechanism helps specifically under perturbations.
4. **Expand the perturbed-environment baseline set.** Include at least one additional robustness-oriented method (e.g., a VLA trained with data augmentation or domain randomization) to support the robustness claim.
5. **Fix the GR-1 citation** in Section 5.2 (should be Wu et al., 2023, not Black et al., 2023).
6. **Specify key hyperparameters** (number of prototypes N, temperature δ, VAE source, learning rates) in a supplementary table.
