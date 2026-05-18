Now I have a thorough understanding of the paper and all the review claims. Let me compile my final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
### Minor
### Trivial

## Nice-to-Haves
## Removed Points
## Novel Insights
## Suggestions

## Score and Decision

Let me write the final review now.

The key things I've verified:

1. The paper references quantitative experiments in appendix (`sec:numerical_celeba`) — so "no quantitative metrics" is partially wrong since the parser strips the appendix. But the main paper is indeed quite qualitative.

2. The paper discusses the invertibility approximation and cites Reizinger et al. 2022, and has a "Model Misspecification" paragraph in the Discussion — so the paper does acknowledge this issue.

3. The paper discusses Mahajan et al. 2019 and Karimi et al. 2020 in the related work section but does not compare experimentally — valid weakness.

4. The paper's default distance choice and lack of discussion about the relationship to the prior is a genuine gap in the discussion.

5. The paper's main experiments are on Morpho-MNIST and CelebA with figures showing example counterfactuals — this is reasonable for a method paper but could be stronger with quantitative metrics.

Let me finalize.I now have a complete understanding of the paper and all reviews. Here is my consolidated review.

---

## Summary

This paper introduces DeepBC, a tractable method for computing backtracking counterfactuals in deep structural causal models (SCMs) where causal mechanisms are (approximately) invertible and differentiable. Two variants are proposed: a stochastic version sampling counterfactuals via Langevin Monte Carlo, and a mode version finding a single "most likely" counterfactual via iterative linearization-based constrained optimization. The paper connects backtracking counterfactuals to the counterfactual explanation literature and claims three properties: causal compliance, versatility, and modularity. Experiments on Morpho-MNIST and CelebA illustrate these properties.

## Strengths

1. **Causal compliance via latent-space distance**: DeepBC measures distance in the structured latent space of an SCM rather than in observable space, ensuring that counterfactuals preserve all causal mechanisms. This is convincingly demonstrated in the Morpho-MNIST experiment (Figs. 3a, 4), where backtracking changes thickness alongside intensity (preserving their causal relation), while interventional counterfactuals break the link and produce out-of-distribution images. The paper also shows that only upstream latent variables change when the antecedent is a non-root variable, with downstream latents left untouched — a clean empirical validation of the conceptual framework.

2. **Versatility beyond the instance-label setup**: DeepBC supports complex causal graphs with multiple high-dimensional and scalar variables, allowing any subset of variables as antecedent. This is evidenced by the CelebA experiments (Fig. 5), where counterfactuals manipulate four attributes (Age, Gender, Beard, Bald) with a non-trivial causal graph, and by support for different distance functions including sparsity and stochastic sampling. This contrasts with typical counterfactual explanation methods that are limited to a single label variable.

3. **Theoretical unification and algorithmic framework**: The paper formally shows that mode DeepBC reduces to the Wachter counterfactual explanation formulation as a special case (Sec. 3.2), placing non-causal explanation methods within a causal framework. The mode DeepBC algorithm uses a Levenberg-Marquardt-style method with a closed-form solution per iteration (Algorithm 1), and the paper provides an invertible parameterization for categorical variables using a Gumbel-softmax-like formulation — practical contributions that make the framework operational.

4. **Modularity demonstration**: The paper shows that structural equations can be swapped (e.g., manually replacing the beard mechanism to produce an OOD counterfactual where being female is associated with a beard, Fig. 6), illustrating a capability not offered by non-modular methods.

5. **Sensitivity to graph misspecification**: The paper demonstrates that using an incorrect causal graph (I→T instead of T→I) causes DeepBC counterfactuals to depend on the backtracking conditional, violating causal compliance (Fig. 3b), which validates the method's reliance on a correct graph and provides a useful diagnostic signal.

## Weaknesses

### Major

1. **Main paper lacks quantitative validation of the method's reliability**: The experiments are overwhelmingly qualitative — individual image examples and scatter plots with no quantitative metrics in the main text. While the paper references quantitative experiments in the appendix (`\cref{sec:numerical_celeba}`), the main manuscript contains no numerical evaluation of constraint satisfaction (e.g., $\|\mathbf{F}_S(\mathbf{u}') - \mathbf{x}^*_S\|_2$), no assessment of counterfactual plausibility or distributional fidelity, no runtime comparisons, and no sensitivity analysis for the penalty parameter $\lambda$ or distance weights $w_i$. For a method paper proposing two algorithms, the absence of even a single table or summary statistic in the main paper makes it difficult to assess whether the method works robustly across examples or whether the shown results are cherry-picked. This is the most significant weakness and limits the paper's evidentiary support for its claims.

2. **No systematic experimental comparison to related causally-aware counterfactual methods**: The paper discusses Mahajan et al. (2019) and Karimi et al. (2020/2021) in the related work section, describing how the methods differ in philosophy and assumptions. However, no experimental comparison — not even a qualitative one — is provided. Given that these are the most closely related approaches, the lack of positioning relative to them in the experiments is a significant gap. Even a side-by-side qualitative comparison of counterfactual outputs would help the reader understand what DeepBC offers beyond existing causally-aware approaches.

### Minor

3. **Invertibility approximation for VAE modules is not empirically validated**: The method relies on accurate inversion of the reduced form $\mathbf{F}^{-1}$. For normalizing flows this holds exactly, but for the conditional VAEs used for the image variable in both experiments, the inversion is only approximate (via the encoder). The paper cites theoretical support (Reizinger et al., 2022) and mentions non-invertibility in the Discussion as a limitation, but provides no empirical check of inversion quality (e.g., reconstruction error, latent consistency between $\mathbf{x}$ and $\mathbf{F}(\mathbf{F}^{-1}(\mathbf{x}))$). If the approximation is poor for certain inputs, the entire backtracking procedure — which minimizes distances in this latent space — could produce counterfactuals inconsistent with the factual observation. Even a single number reporting average reconstruction error on the training set would substantially increase confidence.

4. **The role and choice of backtracking conditional $p^B$ is under-discussed**: The paper treats $p^B$ as a user-specified factorized exponential family with default squared Euclidean distance and equal weights, but does not discuss the tension between this choice and the prior over $U$. The default squared Euclidean distance on latents corresponds to an implicit conditional density centered at the factual value, which is not the same as the data-driven prior over $U_i$ (e.g., a standard Gaussian). This mismatch means that the "most likely" counterfactual produced by mode DeepBC is most likely with respect to a user-defined similarity on the latent space, not with respect to the model's actual noise distribution. The paper would benefit from acknowledging this explicitly and discussing when the default choice is appropriate versus when alternative distances derived from the noise prior might be preferable.

5. **Stochastic DeepBC algorithm lacks discussion of sampling quality**: Algorithm 2 (stochastic DeepBC) is described briefly. The Langevin Monte Carlo proposal requires specifying step size $\eta$ and number of steps $T$, and the initialization at the mode makes the sampler biased toward the mode unless $T$ is very large. The paper does not discuss burn-in, mixing diagnostics, or how to obtain multiple effectively independent samples. The single figure showing five samples is insufficient to assess the quality of the sampling procedure.

### Trivial

6. **Sparsity extension's two-step greedy procedure is not analyzed**: The sparsity extension (Sec. 3.4) runs mode DeepBC twice — once to identify the $M$ latents with largest change, then again restricted to those latents. This heuristic is plausible but its behavior (e.g., does it converge to a local optimum? does the ordering of selection matter?) is not examined.

7. **Modularity demonstration is a straightforward property of SCMs**: Replacing a learned mechanism with a manually constructed one (Fig. 6) is a basic property of any modular SCM. While it illustrates the concept, it does not distinguish DeepBC from other SCM-based approaches or constitute a substantive experiment on its own.

## Nice-to-Haves

- Include a sensitivity analysis for the penalty parameter $\lambda$ in the main paper, showing how constraint satisfaction and solution quality vary, with a practical recommendation for setting it.
- Show reconstruction error or latent consistency metrics for the VAE components used in the experiments.
- Add a side-by-side qualitative comparison with Mahajan et al. (2019) or Karimi et al. (2021) to help position DeepBC relative to existing causally-aware methods.
- Discuss the relationship between the backtracking conditional $p^B$ and the prior over $U$, and consider showing an ablation where the distance is derived from the noise distribution.

## Removed Points

- **"No quantitative metrics at all"**: The paper explicitly states "We also demonstrate quantitative experiments and their results in~\cref{sec:numerical_celeba}" (line 341). The parser strips supplementary sections, so quantitative results likely exist in the original submission. The main paper remains light on quantitative results (kept as a Major weakness above), but the claim of zero quantitative evaluation is removed.

- **"The method relies on existence of exact inverses" as a fatal flaw**: The paper discusses the approximation and its limitations (lines 73-77, Model Misspecification paragraph) and cites relevant theory. It is an acknowledged limitation, not an unexamined assumption. The concern about empirical validation is kept (minor weakness #3) but reframed from a fatal structural flaw to an empirical gap.

- **"Comparisons against closed-source/API-only models"**: Not applicable; no such demand is made by the reviewer.

- **"Missing related works"**: Per instructions, this cannot be confirmed without external sources.

- **Formatting/style nitpicks**: Removed per instructions.

- **"Suggestion to add more baselines/tasks that would broaden the paper"**: These are scope-creep suggestions that would turn the paper into a benchmark rather than a stronger version of the proposed method.

## Novel Insights

The reviewer's observation about the tension between the user-specified backtracking conditional $p^B$ and the data-driven prior over $U$ is a genuinely novel and thoughtful point that goes beyond the paper's own discussion. The paper treats $p^B$ as a free design choice without noting that the default squared Euclidean distance may produce counterfactuals that are causally compliant but improbable under the model's actual noise distribution. This is a subtle and important point that future work on backtracking counterfactuals should address. The reviewer's suggestion to potentially derive the distance from the noise prior (e.g., $d_i(u'_i, u_i) = \|u'_i\|^2_2 - \|u_i\|^2_2$) is a concrete, actionable alternative worth exploring.

## Suggestions

1. Add at least one quantitative table to the main paper: measure constraint satisfaction ($\|\mathbf{F}_S(\mathbf{u}^*) - \mathbf{x}^*_S\|_2$) and latent perturbation size across multiple factual examples for both Morpho-MNIST and CelebA. A simple comparison of these metrics across the two DeepBC variants and interventional counterfactuals would substantially strengthen the evidentiary base.

2. Include a brief empirical validation of the VAE inversion quality (reconstruction error on the training set) to build trust that the latent representation is faithful.

3. Acknowledge and discuss the relationship between the backtracking conditional $p^B$ and the prior over $U$, and clarify when the default squared Euclidean distance is appropriate versus when other choices may be more principled.

4. Add a discussion of burn-in and mixing for the stochastic DeepBC algorithm, and show more samples or a diagnostic (e.g., trace plots of the energy function) to assess sampling quality.

5. Provide a sensitivity analysis for the penalty parameter $\lambda$ with a practical guideline for setting it.

## Score and Decision

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>