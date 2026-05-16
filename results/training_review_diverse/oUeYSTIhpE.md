Now I have a thorough understanding of the paper. Let me synthesize the review.

## Summary

The paper proposes DisCo-DSO, a generative-model-based approach that jointly optimizes discrete and continuous variables in hybrid spaces using deep reinforcement learning with parameterized action spaces. The key idea is to have an RNN output both discrete-token logits and continuous-parameter distribution parameters at each step, enabling joint sampling and optimization rather than the standard decoupled approach where continuous parameters are optimized separately after discrete skeletons are formed. Experiments on a parameterized bitstring task, symbolic regression, and decision tree policy optimization show that DisCo-DSO consistently achieves better solutions with dramatically fewer function evaluations compared to decoupled baselines.

## Strengths

- **Joint sampling drastically reduces function evaluations**: DisCo-DSO samples a complete solution in one forward pass, whereas decoupled methods require many evaluations per discrete skeleton for continuous optimization. This is empirically demonstrated across all three tasks (Figures 2, 3, 5), with the advantage growing in more complex problems.

- **Robustness to non-differentiable and discontinuous objectives**: The parameterized bitstring task (Section 4.1) shows that DisCo-DSO overcomes highly nonlinear landscapes (f₁ and f₂) where decoupled approaches either require many more samples or fail outright, without assuming differentiability of the objective.

- **Superior generalization in symbolic regression**: DisCo-DSO achieves the best average reward on the test set with the fewest function evaluations (Figure 3), avoiding the overfitting/bloat problem that plagues GP-based decoupled methods.

- **Outperforms state-of-the-art on DT policy optimization**: Across four RL benchmarks (MountainCar, CartPole, Acrobot, LunarLander), DisCo-DSO finds univariate decision trees that surpass all literature baselines (evolutionary DTs, cascading DTs, differentiable DTs) at comparable or lower complexity (Figure 6), while being significantly more sample-efficient (Figure 5).

- **Novel methodological extension**: The paper is the first to apply deep RL with parameterized discrete-continuous action spaces to discrete optimization problems, extending existing deep RL-for-combinatorial-optimization frameworks to handle hybrid spaces without decoupling, relaxation, or tokenization of continuous variables.

## Weaknesses

### Fatal
None.

### Major

- **Incomplete/ambiguous policy gradient equation (Equation 5)**: The gradient formula as presented shows only `∇_θ log p(l_i | ...) if l_i ∈ \bar{\mathcal{L}}` (purely discrete tokens). For parameterized tokens (l_i ∈ \hat{\mathcal{L}}), the joint probability includes both the discrete token selection and the continuous parameter sampling: `log p((l_i,β_i)|...) = log p(l_i|...) + log p(β_i|l_i,φ^(i))`. The equation does not make this decomposition explicit, and the continuous-parameter log-probability term is missing from the rendered equation. While the method description (Section 3.2) clearly intends joint learning — the model emits both ψ^(i) and φ^(i), and the entropy bonus (Equation 6) explicitly handles continuous parameters — the gradient equation as printed does not communicate the actual learning rule. This makes it impossible for a reader to verify the theoretical correctness of the optimization from the paper alone. **The authors must provide a correct, complete gradient that makes the role of continuous parameters explicit.**

### Minor

- **Symbolic regression evaluation underspecified**: Section 4.2 does not name the specific benchmark datasets used (e.g., Nguyen, Koza, or a custom set), report per-dataset results, or specify the number/distribution of constants in the target equations. The only result is an aggregate over "all datasets" (Figure 3). While the aggregate advantage is clear, the lack of per-dataset detail prevents readers from assessing whether the benefit is consistent or concentrated on particular problem types. This is a reproducibility gap.

- **Missing details for reproducing decoupled baselines**: The paper never states the budget (number of function evaluations) allocated to the inner continuous optimizers (BFGS, anneal, evo) per discrete skeleton in the decoupled baselines. Since the entire case for DisCo-DSO rests on evaluation efficiency, this is needed to make the efficiency comparisons in Figures 2, 3, and 5 fully interpretable. Similarly, the distribution family 𝒟 for continuous parameters in SR is not specified (it is stated as "truncated normal" for the DT task, but left unspecified for SR).

- **DT literature comparison lacks variance reporting**: Figure 6 compares DisCo-DSO against literature baselines but reports only point estimates (mean reward) without confidence intervals or standard errors. While the paper notes that 1,000 seeds are used for evaluation, the figure does not convey the statistical significance of the reported advantages, particularly for environments where rewards are close to ceiling (MountainCar, CartPole).

- **No ablation of risk-seeking vs. expected reward in the joint setting**: The paper adopts the risk-seeking objective J_ε without empirical justification (e.g., an ablation study) specific to the joint discrete-continuous setting. While citing prior work (Petersen et al., 2021a), a brief comparison would strengthen confidence in the design choice.

### Trivial

- The notation in Section 3.1 (the dummy range [0,1̄] for purely discrete tokens) is slightly convoluted but workable.
- The weighting of the entropy bonus in the overall loss is not explicitly stated.

## Nice-to-Haves

- A per-dataset table for the SR experiment (showing reward and complexity for each benchmark equation) would substantially strengthen the evaluation.
- Error bars (e.g., standard error over multiple runs) on the DT literature comparison in Figure 6, even for a subset of environments.
- An ablation comparing J_ε (risk-seeking) vs. J (expected reward) in the joint setting.

## Removed Points

- **"Convoluted notation" criticism**: This is a style preference, not a substantive weakness. The notation is functional.

- **"Decoupled-GP overfitting claim would be stronger if training reward were shown"**: This is a suggestion for strengthening, not a weakness. The test-set results already support the claim.

- **"The entropy bonus weighting is not stated"**: Minor presentational omission that does not affect the core claims; moved to Trivial.

## Novel Insights

The key insight that emerges from synthesizing the reviews is that DisCo-DSO's primary advantage is structural rather than algorithmic: by making the generative model responsible for the full (discrete, continuous) solution in one shot, the approach eliminates the per-skeleton inner optimization loop that dominates the cost in decoupled methods. This is particularly important in settings where each evaluation is expensive (e.g., RL episodes), and the experiments convincingly show that this structural advantage compounds as problems become more complex. The paper would benefit from presenting the gradient equation as the standard REINFORCE with a factorized action distribution, which is cleaner and avoids the current ambiguity.

## Suggestions

1. **Fix the gradient equation**: Write the full policy gradient for the joint likelihood. For each step i, the log-probability is `log p(l_i|...) + 1_{l_i∈\hat{\mathcal{L}}}·log p(β_i|l_i,φ^(i))`, and the gradient should sum both terms. Show the piecewise definition clearly.

2. **Disclose SR benchmark details**: List the benchmark equations used, report per-dataset results (at least in a table in the main text or appendix), and specify the distribution family 𝒟 used for sampling constants.

3. **Report the budget for inner optimizers**: State how many function evaluations the decoupled baselines (BFGS, anneal, evo) are allowed per discrete skeleton, so that the efficiency comparisons are fully reproducible.

4. **Add confidence intervals**: Include standard errors or confidence intervals for the DT literature comparison (Figure 6), using the 1,000-episode evaluation already performed.

## Score and Decision

The paper presents a timely and well-motivated approach to an important problem. The core idea — using a generative model to jointly sample discrete and continuous solution components — is sound, and the empirical results consistently demonstrate meaningful advantages across diverse tasks. The main weakness is a presentation gap in the policy gradient equation, which must be corrected to clearly show how continuous parameters are learned. This is fixable in revision and does not undermine the paper's core claims (the empirical evidence is consistent with a correct implementation). Based on the paper's originality, the strength and breadth of the experimental validation, and the significance of the problem addressed, the paper merits acceptance pending the clarification of the gradient equation.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>