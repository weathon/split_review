Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper addresses fairness-aware learning when sensitive attributes are only partially annotated. The authors propose a soft-labeling regularization approach that replaces "hard" pseudo-labels (imputed by an attribute classifier) with probability-weighted importance-sampling estimates of fairness criteria (demographic parity and equalized odds). Two uncertainty-aware variants are introduced — a marginal model that averages attribute probabilities before computing fairness, and a Bayesian variant that averages the fairness objective over ensemble members — inspired by the Bayesian fairness framework of Dimitrakakis et al. (2019). The method is evaluated on Adult (tabular) and CelebA (image) datasets with varying proportions of labeled sensitive attributes.

## Strengths

1. **Principled derivation using importance sampling**: The reformulation of the fairness criteria for unlabeled data (Equations 6–9) via the identity $\mathbb{E}_{x\sim P_a}[f(x)] = \mathbb{E}_{x\sim P}[f(x) \frac{p(z=a|x)}{p(z=a)}]$ provides a formal justification for using probability-weighted estimates rather than heuristic hard assignments. This connects the "soft" labeling idea directly to the definition of the fairness metric.

2. **Uncertainty-aware variants improve fairness in high-dimensional settings**: The Bayesian variant (soft reg b) achieves the lowest equalized odds disparity on the CelebA dataset across both tasks (attractiveness and smiling), and exhibits substantially lower variance across runs (Table 1). This is a concrete, demonstrated benefit of incorporating parameter uncertainty in the attribute classifier when labeled data is scarce (5%).

3. **Evaluation across two modalities with varying labeled proportions**: The method is tested on both tabular data (Adult, with 10%–100% labeled proportions over 50 runs) and high-dimensional image data (CelebA, 5% labeled over 10 runs), providing evidence of generalizability beyond a single setting.

4. **Intuitive handling of low-confidence examples**: As discussed in Section 4.1 (paragraph following Eq. 7), the soft formulation naturally down-weights examples where the attribute classifier is uncertain (near-uniform probability), unlike hard pseudo-labeling which forces a binary assignment regardless of confidence. This is a clear conceptual advantage.

## Weaknesses

### Fatal
None.

### Major

1. **The improvement over baselines on Adult is not convincingly established**: The Adult results (Figure 1) show that the proposed soft regularization methods achieve slightly lower Equalized Odds disparity than the pseudo-label and confidence-based baselines. However, the standard deviations (from 50 runs) overlap substantially across methods at most labeling proportions, and no statistical significance tests (paired bootstrap, confidence intervals, or effect sizes) are reported. The differences (~0.01–0.02 EO) are small relative to the error bar magnitudes, making it difficult to determine whether the observed advantage is robust. This weakens the central empirical claim for the tabular modality.

2. **The "softness" effect is not isolated from the reformulated loss function**: The pseudo-label baseline uses hard labels + the standard DP/EO loss (Eq. 4: $|\mathbb{E}_{x\sim P_0}f(x) - \mathbb{E}_{x\sim P_1}f(x)|$), while the soft method uses probability-weighted importance-sampling loss (Eqs. 6–7). These differ in *two* respects: (a) binary label vs. continuous probability, and (b) the functional form of the loss itself. Without an ablation that controls for one factor at a time (e.g., hard labels used with the reformulated loss, or soft probabilities used with the standard loss), it is unclear which component drives any observed improvement. The paper's claim that soft labels are beneficial conflates these two design choices.

### Minor

1. **Extraneous sum over $y$ in the Demographic Parity formulation (Equation 6)**: The DP loss for unlabeled data is written as $\mathcal{L}_U^{DP} = \sum_{y\in\mathcal{Y}} | \mathbb{E}_{x\sim P}[f(x)\frac{p(z=0|x)}{p(z=0)}] - \mathbb{E}_{x\sim P}[f(x)\frac{p(z=1|x)}{p(z=1)}] |$. Demographic Parity does not condition on the label $y$; the sum over $y$ is mathematically extraneous (it multiplies the DP gap by $|\mathcal{Y}|$). This does not affect the reported experimental results (which focus on Equalized Odds), but it is a notational error in a core equation that should be corrected.

2. **Strong vanilla baseline on the CelebA smiling task undercuts the narrative**: On the smiling task with 5% labeled data, the vanilla model (no fairness regularization) achieves an EO of 0.028, which is better than all baselines except soft reg b (0.019). The paper acknowledges this (Section 5.2.1: "it's worth mentioning that the vanilla method for the smiling task... surpasses most of the other methods in terms of fairness"), but does not discuss why fairness interventions should be expected to help here or what this reveals about the difficulty of the test bed. The attractive task provides a cleaner comparison, but the smiling result raises questions about whether the dataset uniformly requires fairness regularization.

3. **No sensitivity analysis for the trade-off hyperparameters**: The fairness regularization weight $\lambda_f = 1.0$ and the unlabeled data weight $\lambda_U = 0.5$ are fixed across all experiments on both datasets. Since the accuracy–fairness trade-off depends critically on these values, the absence of any sensitivity analysis is a gap in the experimental methodology.

4. **No analysis of attribute classifier quality**: The method's performance depends on the accuracy and calibration of the auxiliary models $f_z$ and $f_d$, yet no diagnostic metrics (accuracy, calibration error, or confidence distributions) are reported for the attribute classifier across different labeled-set sizes. This makes it difficult to interpret results — e.g., whether soft labeling helps more when the classifier is poorly calibrated.

### Trivial

None.

## Nice-to-Haves

- An ablation that isolates the "softness" effect from the importance-sampling weighting scheme, as suggested in the "Strengthening the Paper" section of the harsh review. For example, compare: (a) hard pseudo-labels with the same importance-sampling loss, and (b) soft probabilities with the standard (non-reweighted) DP/EO loss.
- An experiment on a synthetic or semi-synthetic dataset where the attribute classifier's quality can be controlled, to directly test the claim that soft labels are more robust to classifier errors.
- Varying the labeled proportion on CelebA (beyond 5%) to match the richer analysis on Adult.
- A brief discussion of limitations: e.g., the method assumes the attribute classifier is trained only on $D_L$, which may be highly biased when $D_L$ is small.

## Removed Points

These points were flagged by the reviewers but are removed from the main weaknesses for the following reasons:

- **"Mathematical error is fatal / undermines theoretical grounding"** (harsh critic point 1, inflated severity): The DP sum-over-$y$ is a notational error but does not affect experimental results (which use EO). The importance-sampling derivation itself is sound. The critic's framing as a fatal error is an overstatement; it is retained as a Minor weakness above.

- **"Garbled pseudo-code harms reproducibility"** (section-by-section note): The pseudo-code rendering issues in the extracted PDF are parser artifacts, not author errors. The textual description in the paper is sufficient to understand the algorithm.

- **"Paper does not discuss the strong vanilla baseline on CelebA smiling"** (harsh critic point 3): The paper *does* discuss this explicitly (line 202: "it's worth mentioning that the vanilla method for the smiling task... surpasses most of the other methods"). The critic's claim that this is not discussed is factually incorrect. The observation itself (that vanilla is competitive) is retained as a Minor weakness above, as it weakens the experimental narrative.

- **"Alternative baselines not given in main results as separate lines"** (section-by-section note): Details about which variants appear in which figure/table cannot be fully verified from the text alone, and the paper describes all baselines in Section 5. The existing comparisons are sufficient.

- **"Loss of theoretical justification for soft vs hard"** (harsh critic's framing of point 4 as a missing proof): The paper provides an intuitive argument (Section 4.1 final paragraph) about low-confidence examples contributing less. Demanding a formal proof is a reasonable suggestion but not a fatal gap; the retained Major weakness covers the more concrete ablation concern.

- **"Comparison against Chen et al. (2019) is missing"** (missing parts): The paper's scope (learning fair models) differs from Chen et al.'s (assessing bias), as the critic acknowledges. This is not a meaningful gap.

- **"Typo: 'feather exploration'"** (section-by-section note): This is a parser/rendering artifact.

## Novel Insights

The harsh review's observation that the pseudo vs. soft comparison conflates the labeling strategy with the loss function reweighting is a genuinely useful insight that goes beyond what the paper discusses. This type of ablation — teasing apart the "softness" of the label from the importance-sampling form of the loss — would significantly strengthen the paper's contribution and is not an obvious decomposition. The main review's discussion of the CelebA smiling task also usefully highlights that fairness methods can sometimes underperform a simple vanilla baseline, and that papers should explicitly address when fairness regularization is expected to be beneficial versus unnecessary.

## Suggestions

1. **Fix the DP formulation in Equation (6)** by removing the extraneous sum over $\mathcal{Y}$, or clarify that it represents a per-label decomposition of the expectation (and correct the implied scaling).
2. **Add statistical significance tests** (e.g., paired bootstrap or confidence intervals) for the Adult results to substantiate the claimed improvements.
3. **Conduct an ablation** that isolates the "softness" effect from the importance-sampling weighting: compare hard pseudo-labels with the reformulated loss vs. soft probabilities with the standard loss.
4. **Report diagnostics for the attribute classifier** (accuracy, Brier score, or expected calibration error) across different labeled-set sizes so readers can assess when the soft approach is most beneficial.
5. **Add a sensitivity analysis** for $\lambda_f$ and $\lambda_U$ on at least one dataset/task to demonstrate robustness of the conclusions to these hyperparameter choices.

## Score and Decision

The paper addresses a relevant and practically important problem. The core idea (soft probability weighting derived from importance sampling) is sound, and the uncertainty-aware variants are a principled extension. The experimental evidence is supportive but not definitive: the improvements on Adult are small relative to error bars and lack statistical testing, the CelebA smiling task shows a competitive vanilla baseline, and the lack of an ablation isolating the softness contribution makes it unclear which design choice drives the gains. These are addressable issues that do not invalidate the contribution. The paper would benefit from a major revision strengthening the experimental methodology.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>