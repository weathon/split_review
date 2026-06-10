## Summary

The paper proposes CHG Shapley, a data valuation method that replaces the standard accuracy-based utility function (which requires expensive model retraining) with a gradient-alignment-based score (CHG score). By deriving a closed-form Shapley expression under this alternative utility, the method reduces computational complexity to the equivalent of a single model retraining. The method is evaluated on data selection (pruning) and noisy-label detection tasks using ResNet-18 on CIFAR-10/100 and Tiny ImageNet.

## Strengths

1. **Closed-form Shapley under a gradient-alignment utility (Theorem 1)** — This is the paper's main theoretical contribution. The derivation of an analytical Shapley expression when the utility takes the form $U(S) = \|\alpha\|^2 - \|\frac{1}{|S|}\sum_{i\in S} x_i - \alpha\|^2$ reduces the complexity from $\mathcal{O}(n^2 \log n)$ model retrainings (Data Shapley) to the equivalent of a single pass. This is a genuine algorithmic advance if the utility function proves to be a faithful proxy.

2. **Substantial empirical gains on noisy-label detection across all selection fractions** — In Table `tab:noise`, CHG Shapley outperforms all three compared baselines (AdaptiveRandom, Glister, GradMatch) by a wide margin on every fraction from 0.05 to 0.7 on both CIFAR-10 and CIFAR-100. For example, at 30% noise on CIFAR-10, CHG Shapley achieves 85.33% vs. 73.73% for the next best (Glister) — an 11.6 pp improvement. This pattern is consistent across 10 experimental conditions.

3. **Best accuracy at the most challenging low-selection ratios** — On CIFAR-10 at the 5% selection fraction, CHG Shapley achieves 87.15% vs. 85.44% (Glister) and 85.17% (GradMatch). On CIFAR-100 at 5%, it achieves 53.97% vs. 50.42% (GradMatch). These are demanding tests of data valuation quality since the selection budget is severely constrained.

## Weaknesses

### Fatal
None.

### Major

1. **The CHG score is asserted to measure "influence on model accuracy" without any validation of this link.** The CHG score is derived from Lemma 1 (Nesterov's bound), which upper-bounds the *loss after a single gradient step* by $\|\nabla f(\theta)\|^2 - \|\nabla f(\theta) - x\|^2$. The paper repeatedly claims this score "measures the influence of data subsets on model accuracy" (lines 93, 125, 283) or "approximates" it. But there is no argument, theoretical or empirical, connecting one-step gradient alignment at an arbitrary epoch's parameters to the *converged accuracy* of a model trained on subset $S$. This is the central premise of the method — the entire Shapley computation rests on this utility function being a meaningful proxy for subset performance — and it is asserted rather than justified. A simple correlation study (Spearman rank correlation between CHG scores and actual converged accuracy across randomly sampled subsets) would directly test this premise and is absent.

2. **Key baselines missing from the main experimental tables.** The noisy-label detection results (Table `tab:noise`) compare CHG Shapley only against AdaptiveRandom, Glister, and GradMatch — all data *selection* methods not designed for label-noise detection. The most relevant comparisons are with Data Shapley, Beta Shapley, and Data Banzhaf, which the paper's own taxonomy (Table `\ref{tab:summary_of_data_valuation_algorithms}`) lists as the prior data valuation methods. Without these baselines, the claim of "superior performance" (line 202) on noisy-label detection is not supported by the tables presented to the reader. The paper references additional comparisons in figures (Picture \ref{pic:noisy data}, \ref{pic:point removal}) but these are not visible in the text, and the main accuracy tables exclude the most natural competitors.

### Minor

3. **Per-class approximation in Algorithm 2 departs from the theoretical setting without discussion.** Algorithm 2 computes Shapley values within each class separately (player set = $N_c$, not $N$), using $\alpha = \frac{1}{N_c}\sum_{i\in N_c} l_i \nabla f(i;\theta)$. Theorem 1 derives the closed form for the full dataset utility function. While the formula itself can be applied with $n=|N_c|$, the resulting Shapley values measure contribution *within a class*, not globally, and the paper does not discuss whether this changes the interpretation or validity of the valuations. The main experimental results (Tables `tab:main`, `tab:noise`) are presumably produced using Algorithm 2, creating a gap between the theory and the actual evaluation protocol.

4. **Hardness weighting modifies the objective that Lemma 1 applies to, without re-derivation.** The paper changes the optimization objective from $\frac{1}{N}\sum f(i;\theta)$ (ERM) to $\frac{1}{N}\sum h_i f(i;\theta)$ with $h_i = f(i;\theta)$ (line 91-93), and then defines the CHG score using weighted gradients $l_i \nabla f(i;\theta)$. Lemma 1's bound was derived for the standard (unweighted) objective. The paper does not re-derive or justify how the bound transfers to the modified objective, creating a logical gap between the theoretical motivation and the actual method.

### Trivial

None.

## Nice-to-Haves

- A correlation analysis between CHG scores and actual converged subset accuracy — the single highest-leverage experiment for validating the core premise.
- Comparison against Data Shapley, Beta Shapley, and Data Banzhaf in the noisy-label detection tables.
- An ablation to isolate the effect of the hardness weighting ($h_i$) — the "Gradient Shapley" baseline partially covers this but the comparison is not discussed.
- Standard deviations or confidence intervals for the main results to account for training stochasticity.

## Removed Points

The following points from the inputs were removed per the filtering rules:

- **"Unverified theoretical centerpiece / missing proof of Theorem 1"** — Removed per hard rule: proofs and appendices are stripped by the PDF parser and exist in the original submission.
- **"No comparison with data valuation baselines at all"** — Partially removed because the paper explicitly references comparisons with other data evaluation methods in Picture \ref{pic:noisy data} and \ref{pic:point removal}. The absence from the main tables remains as Weakness #2.
- **"Framing gap about trustworthy ML"** — Removed: a presentation concern, not a substantive methodological weakness.
- **Strength: "Computational time competitive with single-pass gradient methods"** — Removed: the timing data shows CHG Shapley is comparable to Glister/GradMatch (often slower, sometimes faster), which does not clearly support an efficiency advantage over these gradient-based selection methods.
- **Strength: Generic claims about the problem being important** — Removed per instructions to drop generic/superficial strengths.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the central tension clearly: the paper achieves genuine computational efficiency through a clever closed-form Shapley, but the enabling premise — that the CHG score is a faithful proxy for subset accuracy — remains unvalidated. This tradeoff is characteristic of methods that replace expensive ground-truth utilities with tractable surrogates, but the paper would benefit from explicitly testing this link rather than asserting it.

## Suggestions

1. Add a direct empirical validation of the CHG score's Spearman rank correlation with converged model accuracy across randomly sampled subsets at various sizes. This is the single most important experiment for establishing the method's credibility.
2. Include Data Shapley, Beta Shapley, and/or Data Banzhaf in the noisy-label detection comparison table. These are the methods the paper explicitly positions itself as improving upon, and their absence from the main tables weakens the evaluation.
3. Discuss the per-class approximation's relationship to the theory: does Theorem 1 still apply directly, and what does a per-class Shapley value mean conceptually?
4. Add standard deviations or confidence intervals to the accuracy tables, since training with SGD is stochastic and the strong claims would benefit from variance estimates.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>