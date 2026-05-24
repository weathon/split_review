Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper studies aggregation of multiple LLM outputs into a single answer. It proposes two algorithms: **Optimal Weight (OW)** , a linear weighted voting scheme using accuracy information that is proven Bayes-optimal under conditional independence; and **Inverse Surprising Popularity (ISP)** , a second-order method based on answer correlations that is shown (in expectation of an "advantage" proxy) to dominate both majority voting and the classical surprisingly popular rule. The paper provides theoretical analysis (Bayesian optimality, closed-form advantage gaps, finite-sample bounds), simulations, and experiments on three datasets (UltraFeedback, MMLU, ARMMAN) where the proposed methods consistently outperform majority voting.

## Strengths

1. **Bayesian optimality of OW (Theorem 1).** The paper proves that the linear weighted scheme with weights \(\sigma_K^{-1}(x_i)\) achieves the maximum possible expected accuracy among *all* aggregation algorithms (not just linear ones) under the conditional-independence model. This is the strongest possible theoretical guarantee for a first-order method.

2. **Closed-form advantage ordering for ISP (Theorem 2).** The paper derives an explicit, interpretable expression for \(\mathbb{E}[\mathrm{Adv}_{\mathrm{ISP}}(s^*) - \mathrm{Adv}_{\mathrm{MV}}(s^*)]\) that is strictly positive whenever any agent beats random guessing (\(x_i > 1/K\)). The analysis also explains *why* the surprisingly popular rule underperforms majority voting in the LLM setting (Section 4.1), a non-obvious finding.

3. **Consistent empirical validation across three datasets.** On UltraFeedback (73.66% vs. 72.21%), MMLU (90.37% vs. 89.32%), and ARMMAN (85.78% vs. 85.24%), the proposed methods outperform majority voting. Per-question comparisons (Table 4) show favorable ratios (e.g., 2545/1727 on UltraFeedback), and statistical significance is established. Across 16 model ensembles, OW-L and OW-I outperform MV in 97.92% and 85.83% of cases, respectively.

4. **Finite-sample guarantee (Theorem 3).** The paper provides a high-probability bound showing that the ISP-over-MV advantage persists when second-order information is estimated from a finite dataset, addressing the central practical concern about estimation error.

5. **Practical synthesis of first- and second-order information (OW-L, OW-I).** The paper introduces unsupervised pipelines that estimate accuracies from pairwise correlations, enabling use of the theoretically optimal OW aggregator without ground-truth labels. These heuristics consistently yield the best empirical results.

## Weaknesses

### Fatal
None.

### Major

None. The paper's claims are generally well-supported within their stated scope. The issues below are substantive but do not invalidate the core contributions.

### Minor

1. **Theorem 2 proves advantage ordering, not accuracy ordering.** The paper proves \(\mathbb{E}[\mathrm{Adv}_{\mathrm{ISP}}(s^*)] \ge \mathbb{E}[\mathrm{Adv}_{\mathrm{MV}}(s^*)]\) but the aggregation algorithms select the label maximizing advantage. A higher expected advantage for the true label does not *formally* guarantee higher selection probability—variance and correlations with false labels could in principle reverse the ordering. The paper argues intuitively that this gap is benign (Section 4, lines 209) and the simulations (Table 2) confirm the accuracy ordering matches, but the headline claim "provably outperforms majority voting" rests on a theoretical proxy rather than a direct accuracy guarantee. Bridging this gap formally or stating the limitation more prominently would strengthen the paper.

2. **The practical algorithms (OW-L, OW-I) that carry the paper's empirical weight are heuristics without theoretical support.** The Bayesian optimality guarantee (Theorem 1) assumes access to true accuracies \(x_i\). The OW-L and OW-I methods estimate these from second-order information with no guarantee that the plug-in weights are near-optimal. The paper is transparent about this (Section 5.2), but it means the strongest empirical results are produced by methods whose theoretical connection to the paper's rigorous analysis is unquantified. A consistency result for the ERM estimator or a bound on the accuracy loss from plug-in estimation would significantly strengthen the paper.

3. **Limited baselines.** The experiments compare only against MV and SP. In the multi-agent LLM literature, other natural aggregation strategies exist that the paper does not consider: (a) confidence-weighted voting when models provide confidence scores, (b) Bayesian model averaging with uniform priors, (c) learned aggregation via a small adjudicator model. Including even one such baseline would sharpen the claim that higher-order information is genuinely more effective than other natural strategies.

4. **Modest absolute gains.** On the subsets where models disagree (the only questions where aggregation can help), the absolute accuracy improvements are 0.5–3%. While consistent and statistically significant, the practical impact is limited. The paper is honest about these numbers but could more prominently contextualize the effect sizes (e.g., Cohen's d) rather than reporting only t-statistics, which with N in the thousands achieve significance for even tiny differences.

5. **Conditional independence assumption (Assumption 1) is strong for LLMs.** The paper acknowledges this and references an extended analysis in Appendix C, but the main text provides no intuition about how severely violations affect the guarantees. The reader cannot assess robustness from the main paper alone. Two paragraphs characterizing the dependency structures under which results still hold, or a simulation with correlated agents, would substantially increase confidence.

6. **Theorem 3's finite-sample bound uses imprecise notation.** The \(\gtrsim\) and \(\tilde{O}\) notation obscures the exact dependence on \(\delta\) and \(M\), limiting the theorem's practical usability for determining required sample sizes.

7. **No confidence intervals reported alongside point estimates.** The t-statistics are reported for the aggregate comparison, but per-dataset confidence intervals for the accuracy differences would be more informative, given the large N that inflates t-values.

### Trivial

- **Notation inconsistency for \(\sigma_K\).** The abstract defines \(\sigma_K(x) = \frac{x^2}{K-1+x^2}\) while the main text (line 77) defines \(\sigma_K(x) = \frac{e^x}{K-1+e^x}\). The main text's version is the one used in the proofs and should be used consistently throughout.

## Nice-to-Haves

- A simulation that explicitly violates conditional independence (e.g., shared training data between agents) would test the robustness of the theoretical claims in a controlled setting.
- Discussion of the computational cost of ISP (summing over all \(K-1\) alternatives in Equation 5 for each of \(N\) agents) and its scaling with \(K\) and \(N\).
- Ablation showing sensitivity to the number of questions \(M\) used to estimate second-order information in real data.

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Criticism about missing appendix content** (appendix extension for conditional independence, expanded expressions for OW-L): The reviewer complained these were not visible in the extracted text. Per review guidelines, the parser strips the appendix from all submissions; these exist in the original paper. Removed.
- **Criticism that the paper lacks discussion of computational cost/runtime:** The paper explicitly states "Additional details (e.g., computational resources and runtime) and prompts are provided in Appendix F.3." This information exists in the full submission. Removed per rule about missing appendix content.
- **Criticism about reproducibility of OW-L (Equation 7 being underspecified):** The paper states "The expanded expressions are presented in Appendix F.2." The initialization and optimization details would be there. Removed per rule about missing appendix content.
- **Criticism about the practical relevance of finding that SP underperforms MV:** The strength finder correctly identifies this as a supporting strength (it is a non-obvious analysis clarifying when second-order methods work). The harsh critic did not actually criticize this, but the framing is worth noting: this is a strength, not a weakness.
- **Strength Finder point about OW being "the strongest possible formal guarantee":** While true within the model, this strength is tempered by Weakness #2 (heuristic practical methods). The strength is genuine but should not be overstated. Kept as-is with appropriate context.

## Novel Insights

Beyond the paper's own contributions, the reviews surface a notable pattern: the paper's strongest theoretical result (Bayesian optimality of OW) and its strongest empirical results (OW-L, OW-I) are decoupled. OW-L and OW-I are heuristic methods that estimate the inputs to OW but come with no convergence or near-optimality guarantees. This creates a gap between what the theory promises and what the experiments deliver—a common but under-discussed pattern in ML papers where clean theoretical models motivate heuristics adapted for real-world constraints. The other key insight from the reviews is that the advantage/accuracy gap in Theorem 2 is a genuinely subtle point: the paper's central "provable" claim is actually about a proxy objective, and the leap to accuracy is empirically validated but not theoretically proven. This distinction is important for readers evaluating the strength of the theoretical contribution.

## Suggestions

1. Add a paragraph discussing the advantage-to-accuracy gap explicitly in the main paper, stating what is and is not proven, and providing the empirical evidence (simulations, Table 2) that the ordering transfers.
2. Add at least one additional baseline—confidence-weighted voting is the most natural and easiest to implement if the LLMs provide token log-probabilities.
3. Report 95% confidence intervals or Cohen's d alongside the t-statistics for the main comparisons.
4. Add a sentence or two in the main text summarizing the nature of the relaxation in Appendix C (e.g., "the results extend to settings where the correlation structure satisfies [condition]").
5. Fix the notation inconsistency for \(\sigma_K\) between the abstract and main text.

## Score and Decision

**Calibration rounds:**

*Round 1 (bracketing):* Weak anchors (scores 2.0–3.2): `SbDf6E4kA2` (3.2, "Mixture of Complementary Agents"), `yBSoEHMN6p` (3.0, "Collective Test-Time Scaling"), `viySlQiXEA` (2.0, "LLM Deployment in Edge"), `pkHaUX69ZN` (2.0, "Generative Self-Aggregation"). Middle anchors (scores 4.5–6.0): `73J3hsato3` (6.0, "Social Agents"), `f6mDQ7zl4t` (4.8, "RL for Solution Aggregation"), `Ug1R40CH8Y` (4.5, "RL for Label Aggregation"). Strong anchors (scores 8.0): `9gw03JpKK4` (8.0, "Gaia2"), `VKGTGGcwl6` (8.0, "LLMs Get Lost"). The paper clearly sits above the weak band (2–3) and well below the strong band (8), placing it in the middle 3.5–7.5 bracket.

*Round 2 (narrowing):* Within the bracket, `VtN1z92lvu` (6.67, "Decision Aggregation under Quantal Response," Accept Poster) is the closest topical match—similar information-aggregation theory with LLM experiments. The current paper has comparable theoretical depth (more theorems) but the quantal response paper has more surprising results and tighter experiments. `XNbVoi9mfr` (6.50, "AtC," Accept Poster) and `WtbPaWO8lH` (6.00, "Causal Discovery in the Wild," Accept Poster) are other accepted-poster anchors with theory-plus-experiments structure similar to this paper. The current paper is slightly weaker than "Decision Aggregation" (6.67) due to the advantage/accuracy gap and heuristic gap, but comparable to "Causal Discovery in the Wild" (6.00) and "Social Agents" (6.00).

The paper makes genuine theoretical contributions (Bayesian optimality, closed-form advantage gaps, finite-sample bounds) and provides consistent empirical support across three datasets. The limitations (advantage/accuracy gap, heuristic practical methods, limited baselines, modest effect sizes) are real but do not undermine the core claims—they call for clearer exposition and additional experiments rather than structural revision. The paper is a solid poster-level contribution.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>