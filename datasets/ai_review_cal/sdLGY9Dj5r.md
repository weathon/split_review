- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 5, 8, 5
Now let me write the final consolidated review.

## Summary

This paper proposes ZO-PoG, a black-box prompt learning framework that alternates between optimizing discrete prompts (via policy gradient with Gumbel-Softmax reparameterization) and continuous prompts (via zeroth-order gradient in a low-dimensional subspace). The method is motivated by the observation that continuous prompt methods like BBT start from randomly initialized discrete prompts, which may be suboptimal. By learning the discrete prompt distribution and the continuous embedding jointly, ZO-PoG aims to improve downstream task performance without model parameter access. The paper provides a convergence analysis showing sub-linear convergence, and reports experiments across 5 GLUE datasets with RoBERTa-large, GPT2-XL, and Llama3.

## Strengths

1. **First collaborative framework for discrete and continuous prompt optimization**: ZO-PoG is the first framework to jointly optimize both discrete text prompts (via policy gradient) and continuous prompt embeddings (via zeroth-order gradient) in a black-box setting. The alternating optimization strategy (Algorithm 1) cleanly combines two previously separate lines of work (continuous tuning via BBT and discrete tuning via BDPL) into a single coherent method.

2. **Convergence analysis with explicit query complexity**: Section 4 provides a rigorous convergence analysis (Theorem 1) showing ZO-PoG achieves an ε-stationary point with total query complexity O(√(nκ)/ε³). Proposition 1 establishes bounded variance for the policy gradient estimator, offering theoretical justification for stability. This level of formal analysis is absent from most black-box prompt learning papers.

3. **Consistent empirical improvements across multiple architectures**: The paper evaluates on 5 GLUE datasets with 3 backbone models (encoder-only RoBERTa-large, decoder-only GPT2-XL, and Llama3). Results reported in Tables 1–3 show ZO-PoG outperforming all baselines (Manual Prompt, BBT, BDPL, SSPT) in the majority of settings. For example, on WNLI with RoBERTa-large (prompt length 50), ZO-PoG achieves a 5.17% absolute improvement over the best baseline.

4. **Ablations verify necessity of both components**: Figure 3 shows that removing either the discrete optimization component (w/o Policy Gradient) or the continuous component (w/o Zeroth-Order) degrades performance across all three backbone models and both prompt lengths, supporting the claim that the collaboration is responsible for the gains.

## Weaknesses

### Fatal

None.

### Major

1. **Critical hyperparameters and implementation details are omitted**: The paper does not report the values of I₁ (discrete sampling times), I₂ (continuous sampling times), learning rates η_α and η_z, Gumbel-Softmax temperature τ, smoothing parameter μ, mini-batch size B, or subspace dimension d anywhere in the experimental setup (Section 5.1). Algorithm 1 lists these as inputs, but the "Implementation Details" paragraph only mentions hardware and backbone models. Without these values, the experiments are unreproducible and it is unclear whether baselines were tuned fairly. The code is promised at an anonymous URL, but the paper itself must document these settings.

2. **σ_g in the convergence analysis is not defined**: Proposition 1 bounds the variance of the policy gradient estimator as 2σ_g²/I² + 2σ_α²/B, where σ_g appears without formal definition or introduction in Assumptions 1–4. This makes the variance bound and the subsequent condition I = O(√(nκ)σ_g/ε) in Theorem 1 incomplete — the result cannot be properly evaluated or applied without knowing what σ_g represents and how it relates to problem parameters.

### Minor

1. **Ablation specification is ambiguous**: The paper states it removes the "discrete prompt optimization component (w/o Policy Gradient)" but does not specify how this is implemented. It could mean (a) α is fixed at its random initialization while the rest of the algorithm (including I₂ prompt sampling in the ZO step) remains unchanged, or (b) the entire discrete mechanism is replaced with a single fixed random prompt. These are different ablations with different interpretations, and the distinction matters for attributing gains to the learned distribution vs. multi-sample averaging. A one-sentence clarification would resolve this.

2. **Weak statistical evidence**: Results are reported as mean over only 3 random seeds. Many improvements over the strongest baseline are modest (~1% on MNLI, CoLA, SNLI). No confidence intervals or statistical significance tests are provided. While 3 seeds is common in this literature due to computational cost, the small effect sizes make it hard to rule out noise. At minimum, the paper should report per-seed results or effect sizes with confidence intervals.

3. **No runtime or query complexity comparison**: The paper does not report total forward passes, wall-clock time, or convergence curves (accuracy vs. queries) for any method. ZO-PoG uses I₁ + I₂ forward passes per iteration plus additional passes for the ZO symmetric difference (2 per sample in the continuous step). Without cost analysis, it is unclear whether the gains come at a higher computational budget.

4. **BBTv2 is cited but not compared**: BBTv2 (Sun et al., 2022a) is discussed in Related Work as an improved version of BBT that optimizes prompts across all layers, but it is not included as a baseline. While including every possible baseline is not required, BBTv2 is a natural extension of BBT and its omission weakens the empirical evidence that ZO-PoG is competitive with state-of-the-art continuous-only methods.

5. **Convergence analysis not validated empirically**: Theorem 1 guarantees sub-linear convergence under asymptotic conditions on I, B, and μ. However, the paper does not include any convergence plots (loss vs. iterations or forward passes) to demonstrate whether this theoretical behavior is realized in practice. The disconnect between the asymptotic theory (which prescribes large I/B) and the practical setting (where I₁, I₂ are presumably small integers) limits the analysis's usefulness.

### Trivial

None.

## Nice-to-Haves

- A systematic study of how prompt length (20 vs. 50) interacts with performance — the paper notes no strict correlation but does not analyze this further.
- Ablation controlling for the number of discrete prompt samples in the ZO step by comparing against I₂ = 1 (a single sample from the learned distribution). This would directly isolate the benefit of learning the distribution from the variance reduction of multi-sampling.
- Application to at least one non-GLUE or non-English dataset to demonstrate broader applicability.

## Removed Points

- **"Unfair ablation: multi-sample advantage" (Harsh Critic issue 1, parts)**: The critic claimed the "w/o Policy Gradient" ablation uses a single discrete prompt and thus doesn't control for multi-sampling. This is speculative — the paper does not specify the ablation implementation, but the natural reading of an ablation that "removes the discrete optimization component" is that it keeps the algorithm structure (including I₂ sampling) but fixes α at initialization. If so, multi-sampling is controlled for. The ambiguity is a genuine issue (captured above as Minor weakness 1), but the specific accusation of unfairness is not verifiable from the paper. *Removed because the claim depends on an unsupported assumption about the ablation implementation.*

- **"First to jointly optimize" claim is overstated**: The critic called this a slight overstatement, claiming "a sequential combination is a natural extension." Whether the combination is "natural" is subjective. The paper clearly motivates why the collaboration is novel (prior work optimized each separately). *Removed because it is a subjective opinion about degree of novelty, not a verifiable weakness.*

- **Assumption 1 (block-wise smoothness) concerns**: The critic questioned whether L_α is well-behaved for the reparameterized loss. These are standard assumptions in non-convex optimization with Gumbel-Softmax; similar assumptions appear throughout the policy gradient literature. *Removed as a generic theoretical concern that applies to nearly all convergence analyses in this area.*

- **Missing related works**: *Removed per instructions not to mention missing related works.*

- **Formatting/OCR artifacts** (e.g., "y distribution" on Algorithm line 10): *Removed per instructions (these are parser errors, not author errors).*

- **Strength from Strength Finder about "variance-reduced policy gradient"**: This technique (VR-PGE with baseline subtraction) is adopted directly from prior work (Diao et al., 2022; Williams, 1992). It is not a contribution specific to this paper, so it is removed as a listed strength.

## Novel Insights

None beyond the paper's own contributions. The two reviewer inputs largely converge on the same set of structural concerns (missing hyperparameters, weak statistics, ambiguous ablation) without adding new analytical perspectives beyond what is evident from reading the paper directly.

## Suggestions

1. **Document all hyperparameters** (I₁, I₂, η_α, η_z, τ, μ, B, d) in the main paper or appendix. A single table of hyperparameter values would address the most serious weakness.

2. **Clarify the ablation** by adding one sentence describing exactly what "w/o Policy Gradient" and "w/o Zeroth-Order" mean (e.g., "We keep the algorithm structure identical but skip the α update, leaving α at its random initialization").

3. **Add convergence curves** showing loss or accuracy vs. number of forward passes for ZO-PoG and all baselines. This would simultaneously address the theory-practice gap, the query complexity concern, and provide stronger evidence of practical convergence.

4. **Define σ_g formally** in Assumptions 1–4 or in a remark before Proposition 1.

5. **Include per-seed results** or bootstrapped confidence intervals for the main results, given the small number of seeds and modest effect sizes.

6. **Report total forward passes** used by each method in a single table to enable fair comparison of computational cost.
