Now I have enough information to produce the consolidated review.

## Summary

This paper proposes $f$-FERM, a stochastic optimization framework for fair empirical risk minimization using $f$-divergence regularizers. The core technical contribution uses Legendre-Fenchel duality to rewrite the $f$-divergence regularizer as a linearly separable nonconvex-concave min-max problem, enabling unbiased mini-batch gradient estimation and provable convergence guarantees. The framework is also extended to a distributionally robust setting under $\ell_p$ norm uncertainty sets for handling distribution shifts. The mathematical derivations are sound and the unified treatment of multiple $f$-divergences is a genuine contribution. However, the empirical evaluation is too thin to support the paper's claims for a top-tier venue.

## Strengths

1. **Clean variational reformulation enabling unbiased stochastic gradients**: Proposition 1 and Eq. 106 show that by rewriting the $f$-divergence regularizer using Legendre-Fenchel duality, the objective becomes a sum over individual data points. This directly solves the key problem identified in prior work — that most non-linear fairness regularizers "are not amenable to stochastic optimization" (line 25) — and strictly generalizes Lowy et al. (2022) beyond $\chi^2$ divergence.

2. **Provable convergence guarantee across all batch sizes**: Theorem 1 provides an $\mathcal{O}(1/\epsilon^8)$ iteration complexity for Algorithm 1, applicable to all listed $f$-divergences for batch sizes down to 1. This is a formal guarantee that prior methods (e.g., Zhong et al. 2023 requiring offline neural network estimation, or Wang et al. 2023 lacking convergence guarantees) cannot offer.

3. **First DRO framework under $\ell_p$ norm uncertainty sets for nonconvex fair learning**: Section 3.1 derives a distributionally robust formulation with Proposition 2 providing an $\mathcal{O}(\epsilon)$-stationary approximation guarantee under small distribution shifts, extending beyond convex logistic regression (Taskesen et al., 2020) and MMD-based heuristics (Wang et al., 2023).

4. **Closed-form reduction for $\ell_\infty$ uncertainty sets**: Section 3.2 shows that under an $\ell_\infty$ uncertainty set with certain sign conditions on $f^*$, the inner maximization collapses to the explicit form $\mathcal{D}_f(\min\{\mathbb{P}+\delta, 1\} \,\|\, \max\{\mathbb{Q}-\delta, 0\})$, converting a hard nonconvex-nonconcave min-max problem into standard regularized minimization (Eq. 240).

5. **Empirical demonstration of batch-size consistency**: Figure 2 shows that $f$-FERM maintains competitive fairness-accuracy tradeoffs across batch sizes from full-batch down to 2, while competing methods degrade significantly. This provides direct evidence for the paper's central stochasticity claim.

## Weaknesses

### Fatal
None. The core methodological idea is sound and the mathematical derivations are correct.

### Major

1. **Experiments limited to a single dataset family**: Every experiment uses only Adult-derived data (UCI Adult, lines 258, 267; New Adult from Ding et al. 2021, line 280). Standard fairness benchmarks — COMPAS, German Credit, Bank Marketing, Law School — are entirely absent. The paper claims "superiority of fairness-accuracy tradeoffs offered by $f$-FERM for almost all batch sizes" but tests this on one dataset family. No generalization to different domains, data modalities, or even other tabular datasets is demonstrated.

2. **No error bars or multiple runs on main experiments**: Figures 1, 2, and 3 report single curves with no indication of variance. Only the New Adult experiment (Figure 4) reports 25th–75th percentile ranges. Without knowing the variance, the reader cannot assess whether the observed differences between methods are meaningful or within noise. This is especially problematic for the claimed "extraordinary" simultaneous improvement in fairness and accuracy for small-$\lambda$ KL-divergence (line 263), which contradicts standard fairness-accuracy tradeoff expectations and requires statistical support.

3. **Baselines handled opaquely**: Lines 263–264 state that Zafar et al. (2017), Donini et al. (2018), Zemel et al. (2013), Hardt et al. (2016), and Jiang et al. (2020) "demonstrate lower performance" and are "removed from the figure." The reader cannot see what "lower" means, how much lower, or whether the comparison is fair. For the baselines that are shown, no configuration or tuning details are provided.

4. **DRO "semi-stochastic" algorithm undermines core scalability claim**: The $\ell_p$ small-shift algorithm (Section 3.1) requires computing $\hat{p}_j(\theta)$ and $\hat{q}_j(\theta)$ via "one forward pass over all data points" each iteration (lines 229–230). This is an $O(n)$ operation over the full dataset each iteration — the same cost as full-batch gradient descent. The paper's abstract and introduction sell stochastic mini-batch optimization as the core advance, yet the DRO extension itself is not a stochastic method in the mini-batch sense. The paper acknowledges this as "semi-stochastic" (line 229) but never addresses the tension with its headline claims of scalability.

### Minor

1. **Unexplained $O(1/\epsilon^8)$ convergence rate**: Standard SGDA for nonconvex-concave problems typically achieves $O(1/\epsilon^4)$. The paper does not explain why the bound is $O(1/\epsilon^8)$ — whether from the specific $f$-divergence structure, a loose analysis, or a different stationarity metric. Lines 136–137 note that better rates exist with nested-loop algorithms ($O(\epsilon^{-6})$ or even $O(\epsilon^{-2})$ under strong concavity), but the paper does not justify choosing a simpler algorithm whose provable rate is orders of magnitude worse.

2. **$\ell_\infty$ large-shift derivation relaxes probability simplex without justification**: Line 237 states: "Notice that we need to relax the probability simplex constraint to obtain this efficient, optimal closed-form solution." The resulting clipping operations ($\min\{\mathbb{P}+\delta, 1\}$, $\max\{\mathbb{Q}-\delta, 0\}$) in Eq. 240 are a heuristic whose validity — whether the relaxed solution respects the original problem's constraints — is never formally established or empirically checked.

3. **No empirical comparison to Zhong et al. (2023)**: The paper itself cites Zhong et al. (2023) as the most directly related work using $f$-divergences for fair learning (line 27) but does not compare against it empirically. Given that the paper frames its contribution as improving on Zhong et al.'s offline estimation approach, this omission weakens the empirical case.

4. **Numerical stability concern with Squared Hellinger**: Table 1 includes $A_{jk}^{-1}$ in the Squared Hellinger row, which could cause numerical instability when $A_{jk}$ is close to zero during optimization. This is not discussed.

5. **Model architecture not specified**: The paper states it uses "neural networks" with a softmax output layer (line 91) but gives no depth, width, activation functions, or other architectural details. This hinders reproducibility.

6. **Missing ablation for the core technical claim**: The paper never directly demonstrates that naively applying SGD to the non-reformulated $f$-divergence objective (without the variational reformulation) fails or converges poorly at small batch sizes, which would be the most direct justification for the entire technical contribution.

### Trivial
None.

## Nice-to-Haves

- Code release would aid reproducibility given the complexity of implementing variational forms for multiple $f$-divergences.
- Adding at least one additional standard fairness dataset (e.g., COMPAS) would substantially strengthen the empirical case.
- A direct comparison showing that naive SGD on the unreformulated $f$-divergence objective fails at small batch sizes would justify the technical contribution. 
- Clarifying the condition $L\delta \lesssim \epsilon$ for the Taylor approximation (Proposition 2) — e.g., how to verify it in practice for a given neural network.
- A formal or empirical check that the relaxed $\ell_\infty$ solutions (Eq. 240) remain valid probability distributions.

## Removed Points

These points were considered but removed after verification against the paper:

- **Unbiasedness of SGD update not verified** — The criticism claimed the unbiasedness of the overall SGD update needs "careful verification." However, Eq. 106 shows the objective is linearly separable as a sum over individual data points, so the mini-batch gradient is trivially unbiased. The concern reflects a misunderstanding.
- **Missing appendix/proof** — The theorem is labeled "Informal Statement" with proofs deferred to the appendix. Per hard rules, weaknesses about missing appendix content are removed (the parser stripped these sections; they exist in the original submission).
- **Missing related works** — Removed per the rule not to add missing related work citations.
- **Missing training details (epochs, schedules)** — Per hard rules, nitpicks about undisclosed hyperparameters are removed.
- **Implicit function theorem differentiability concern** — The paper explicitly acknowledges the differentiability requirement (line 227: "an implicit assumption here is that $f$ is differentiable"), so this criticism is already addressed.
- **No discussion of limitations** — The conclusion (line 293) acknowledges that "a more comprehensive analysis is warranted" regarding optimal $f$-divergence choice, faster convergence, and asymptotic behaviors, partially addressing this concern.
- **Overstatement of novelty** — The critic's concern about incremental contribution over Lowy et al. (2022) is noted but downgraded because extending from $\chi^2$ (a single $f$-divergence) to all $f$-divergences via the same variational technique is more than a trivial increment; it provides a unified framework that was not previously available.

## Novel Insights

None beyond the paper's own contributions. The reviews surface no observation about the method or its properties that the paper itself does not already contain or imply.

## Suggestions

1. **Expand the experimental section substantially**: Add at least 2–3 additional standard fairness datasets (COMPAS, German Credit, Law School). Report all results with multiple random seeds (≥5) and show variance (standard deviations or interquartile ranges) on all figures. Specify the model architecture (number of layers, hidden units, activations) used in all experiments.

2. **Show the failure of naive SGD**: Directly compare the proposed reformulated objective against naively applying SGD to the non-reformulated $f$-divergence objective at small batch sizes. This would be the most direct empirical justification for the entire paper's technical development.

3. **Address the DRO scalability tension**: Acknowledge explicitly that the $\ell_p$ DRO algorithm requires full forward passes and clarify the practical settings where the memory-efficiency vs. computation tradeoff is favorable. Alternatively, explore whether the $\hat{p}_j(\theta), \hat{q}_j(\theta)$ computation can be approximated from mini-batches.

4. **Justify the $O(1/\epsilon^8)$ rate**: Explain where the rate comes from relative to the standard $O(1/\epsilon^4)$ for SGDA, and discuss whether the gap affects practical performance.

5. **Provide visibility into removed baselines**: Show a supplementary figure or table with all baselines including the ones "removed from the figure" so readers can assess the full comparison landscape.

## Score and Decision

MY FINAL SCORE: <score>3.0</score>
MY FINAL DECISION: <decision>Reject</decision>