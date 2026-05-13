Now I have enough information to write the comprehensive review. Let me synthesize everything.

Key findings from my verification:

1. **Missing CRC baseline**: Valid concern. The paper compares only against vanilla conformal. CRC is the most natural loss-aware baseline and the paper itself identifies it as the most closely related work. However, the paper argues CRC is different (monotonically decreasing losses only, controls rather than optimizes). For the separable loss case, CRC should be applicable, making the absence of comparison a meaningful gap.

2. **Greedy algorithm Equation**: The constraint p̂(y|x) ≤ α - p(S^i) is indeed problematic as written. At α=0.1, this limits candidates to those with probability ≤ 0.1 initially, and becomes even more restrictive. This appears to be the wrong direction for a coverage-seeking algorithm.

3. **Proposition 3 quantile**: The proposition claims coverage 1-α but defines τ̂_α as the (1-α) quantile with a ≥ threshold on a conformity score. As analyzed, using the (1-α) quantile with ≥ would give approximately α coverage, not 1-α coverage. This appears to be a notation error; the method likely uses the α-quantile in implementation. This is a significant notation/formulation issue that makes the theoretical claim incorrect as stated.

4. **Abstract framing**: The claim "current methods for uncertainty quantification do not incorporate any information at all about downstream decisions" is an overstatement given CRC exists. The paper later acknowledges this but the abstract claim is too strong.

5. **Error bars**: Only median-of-means over 10 runs, no error bars presented.

6. **Random separable costs**: The separable loss experiments use random uniform costs rather than domain-relevant costs.

7. **Robustness claim**: "Robust to scarce and noisy data" based on a single dataset.

8. **Three-way split**: Penalized conformal requires 3-way split but claimed convergence rate doesn't account for reduced effective sample size.

Let me now write the review.</think>Now I have thoroughly verified all claims against the paper. Let me synthesize the final review.

## Summary

This paper introduces decision-focused conformal prediction, a framework that produces prediction sets minimizing a user-specified decision loss while retaining standard marginal coverage guarantees. The key contributions are: (1) a penalized conformal method that adds a λ-weighted decision loss term to standard nonconformity scores, (2) a hyperparameter-free "Separable Penalized Ratio" method grounded in the Neyman-Pearson lemma for separable losses, and (3) a greedy algorithm for non-separable losses that optimizes over the combinatorial structure of the loss function. All methods are proven to provide 1-α marginal coverage and empirically demonstrate 60-75% reductions in decision loss compared to vanilla conformal prediction across four datasets.

## Strengths

- **Sound high-level framework**: The idea of incorporating downstream decision loss into conformal prediction while preserving coverage guarantees is well-motivated and technically coherent. The two-desiderata formulation (coverage + low decision loss) cleanly captures the core problem. The Neyman-Pearson characterization (Proposition 2) for the oracle optimal set under separable losses provides an elegant theoretical foundation for the hyperparameter-free method.

- **Extension to non-separable losses**: The greedy optimization approach for non-separable losses (e.g., hierarchy-aware coverage losses) addresses a practically important and theoretically challenging setting where losses have combinatorial structure. The Fitzpatrick dermatology case study compellingly illustrates why standard conformal sets can be decision-irrelevant and how the method can incorporate clinical hierarchies.

- **Empirical reductions in decision loss are substantial and consistent**: Across all datasets (CIFAR-100, ImageNet, iNaturalist, Fitzpatrick) and loss functions, the proposed methods consistently outperform vanilla conformal prediction on decision loss metrics (Tables 1-3, Figure 3), with the Fitzpatrick dataset demonstrating clinically coherent prediction sets (Figure 1).

- **Robustness to classifier quality**: The accuracy-vs-loss ablation (Figure 4) on Fitzpatrick shows decision-focused conformalization improves over vanilla conformal at every level of base model accuracy, including very noisy classifiers.

- **Generalization beyond risk control**: The paper correctly identifies that conformal risk control requires monotonically decreasing losses with set size (line 42), while the proposed framework handles arbitrary set-valued losses—a genuine and important extension.

## Weaknesses

### Fatal
None.

### Major

- **Greedy algorithm formulation (Eq. 7) appears incorrect as written**: The constraint $\hat{p}(y|x) \leq \alpha - p(S^i)$ is incoherent for a coverage-seeking algorithm. At α=0.1 (the paper's setting), this initially restricts candidates to labels with p̂(y|x) ≤ 0.1, and after each addition the constraint tightens (since p(S^i) grows, α-p(S^i) shrinks). This produces very small prediction sets that fail to achieve the target 1-α coverage—the opposite of the intended behavior. The correct constraint for the per-instance optimization problem (min L(S) s.t. Σp̂(y|x) ≥ 1-α) should allow selecting any label not yet in the set until the coverage constraint is satisfied. If the implementation differs from the equation, reproducibility is compromised; if it matches, the non-separable results are unreliable. Since this greedy method is the paper's primary algorithmic contribution for the non-separable case (Section 3.2.1), this formulation issue directly undermines a core contribution.

- **Missing comparison with conformal risk control (CRC)**: The paper identifies CRC (Angelopoulos et al., 2022) as the most closely related work (line 42) and its primary differentiator from CRC is handling non-monotonic losses. However, the experiments only compare against vanilla conformal prediction. For the separable loss experiments, CRC is directly applicable (separable losses decrease with set growth), making it the most natural baseline. Without this comparison, the empirical contribution is limited to showing that loss-aware methods outperform loss-agnostic conformal prediction—which is expected by construction. The paper's claim of "significantly lower decision loss" (Abstract) is thus established only against the weakest possible baseline.

- **Proposition 3 (Separable Penalized Ratio) quantile notation is inconsistent**: The proposition defines τ̂_α as the "empirical 1-α quantile" of scores s(x,y) = p̂(y|x)/ℓ(y) and the set as S = {y: s(x,y) ≥ τ̂_α}. Since s is a conformity score (higher = more likely the true label), using the (1-α)-quantile with ≥ threshold yields approximately α coverage (only ~10% of scores exceed the 0.9 quantile), not the claimed 1-α. The standard conformal argument would require the α-quantile for a ≥ threshold on conformity scores. The oracle solution (Proposition 2) correctly uses the α-quantile of p(y|x)/ℓ(y). The proposition as written is therefore incorrect—either the notation should describe the α-quantile, or the mathematical claim cannot hold as stated. This undermines the theoretical guarantee for the separable hyperparameter-free method.

### Minor

- **Abstract overstates the novelty gap**: The abstract claims "current methods for uncertainty quantification do not incorporate any information at all about downstream decisions," which is overstated given conformal risk control explicitly incorporates loss information. The paper acknowledges CRC in Section 1.1 but does not reconcile this with the abstract claim.

- **Only one dataset demonstrates non-separable, domain-meaningful losses**: The Fitzpatrick dataset with clinical hierarchies is the paper's most compelling application, but the other three datasets (CIFAR-100, ImageNet, iNaturalist) use synthetically generated hierarchies. This limits the evaluation of non-separable losses to a single real-world use case.

- **No error bars or confidence intervals**: Results are reported as median-of-means across 10 runs without error bars or significance tests, making it difficult to assess the statistical reliability of claimed improvements.

- **Separable loss experiments use random costs**: The separable experiments assign random uniform costs {1/4, 2/4, 3/4, 1} to labels, which lack decision-theoretic meaning. Any method that reduces set size will reduce such costs, so these experiments provide a weak test of the method's ability to handle structured, domain-relevant costs.

### Trivial
- None.

## Nice-to-Haves

- Comparison with conformal risk control on separable losses would substantially strengthen the empirical narrative.
- Analysis of sensitivity to the bound M in the greedy algorithm for non-separable losses.
- Error bars or confidence intervals across the 10 experimental runs.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh critic: "three-way data split substantially reduces sample efficiency"** — The paper explicitly acknowledges the three-way split and states the convergence rate remains O(1/√n) relative to total sample size (line 97). The sample split is standard practice in conformal prediction and the paper is transparent about it.

- **Harsh critic: "Proposition 1 is standard and adds little"** — Uniform convergence bounds for ERM are indeed standard machinery, but they serve a necessary role in justifying why the λ-tuning procedure converges. This is a building block, not a claimed novelty.

- **Harsh critic: "robust to scarce and noisy data claim unsupported"** — The paper does show systematic analysis via Figure 4 (accuracy vs. loss curves across multiple model checkpoints on Fitzpatrick), which is more than a single anecdotal result. The claim is qualified appropriately per dataset.

- **Strength finder: "Unlike conformal risk control, handles losses that don't decrease monotonically with set size"** — While factually correct based on the paper's claims, this strength is offset by the lack of CRC comparison in experiments; it's an unverified theoretical advantage rather than a demonstrated empirical one.

- **Harsh critic: "approximation quality of plug-in estimates not analyzed"** — This is a valid concern for future work but asking a paper to analyze miscalibration effects is beyond its stated scope; the paper's contribution is the algorithmic framework with coverage guarantees, not a full robustness analysis of the plug-in assumption.

- **Harsh critic: "absolute loss values not shown"** — The tables referenced (Tables 1-3) would contain these values; this appears to be a limitation of the parsed paper format, not necessarily a missing reporting issue.

## Novel Insights

The paper's most insightful contribution is recognizing that the Neyman-Pearson lemma provides the optimal oracle solution for the coverage-constrained decision loss minimization problem under separable losses, yielding a natural, hyperparameter-free conformal score (the probability-to-cost ratio). This transforms what could have been a purely heuristic penalty-tuning approach into a principled, theoretically grounded method. The extension to non-separable losses via greedy optimization of the plug-in oracle problem is also conceptually clean—though undermined by the formulation issue in Eq. (7).

## Suggestions

- **Fix_eq7**: Correct the greedy algorithm constraint in Eq. (7). The constraint should allow adding labels that contribute to achieving coverage (e.g., $\hat{p}(y|x) \leq 1 - \alpha - p(S^i)$ or simply removing the probability constraint from the greedy selection and using it only as a stopping condition).

- **Add_crc_baseline**: Include conformal risk control as a baseline in the separable loss experiments, since CRC is applicable there and is the most natural comparison point.

- **Fix_proposition3**: Clarify the quantile definition in Proposition 3—one reading suggests τ̂_α should be described as the α-quantile (or equivalently, the ⌊α(n+1)/n⌋-th order statistic), consistent with the oracle solution's use of the α-quantile in Proposition 2.

## Evaluation

**Originality**: The idea of decision-focused conformal prediction is novel and timely. The Neyman-Pearson grounding for separable losses is particularly clean. The extension to non-separable losses fills a genuine gap left by CRC.

**Importance of research question**: Highly important—conformal prediction sets that ignore downstream decision utility are often practically useless, and improving their actionability is a significant goal.

**Claim support**: Substantially weakened by Eq. (7) formulation issue, Proposition 3 notation error, and the missing CRC baseline. The core claim—that the methods achieve lower decision loss while maintaining coverage—is only established against vanilla conformal (a weak baseline) and the theory contains errors.

**Experimental soundness**: Adequate datasets and loss functions, but missing the most important baseline (CRC) and lacking error bars. The Fitzpatrick case study is compelling.

**Clarity**: Generally well-written, but mathematical notation issues (Proposition 3, Eq. 7) create confusion rather than illumination.

**Value to community**: The framework is valuable and the problem is important, but the current execution has theoretical and experimental gaps that need correction.

MY FINAL SCORE: <pineapple>5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>