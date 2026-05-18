I now have a thorough understanding of the paper and the reviews. Let me write the final consolidated review.

## Summary

This paper introduces a framework for incorporating downstream decision losses into conformal prediction. The authors propose several methods: a penalized non-conformity score with hyperparameter tuning, a closed-form ratio-based method for separable losses (via Neyman-Pearson), and a greedy algorithm for non-separable losses. All methods come with standard conformal coverage guarantees. Experiments on CIFAR-100, ImageNet, iNaturalist, and the Fitzpatrick dermatology dataset demonstrate substantial reductions in decision loss (60-75%) over standard conformal prediction, along with a compelling case study producing clinically coherent prediction sets.

---

## Strengths

1. **Provable coverage guarantees for all proposed methods**: The paper rigorously proves that the Separable Penalized Ratio (Proposition labeled Neyman-Pearson, lines 115-121) and the greedy-based non-separable method (Proposition 3, lines 153-159) maintain standard conformal coverage bounds: \(1-\alpha \le P(Y \in S_{f(X)}) \le 1-\alpha + \frac{1}{n+1}\). These guarantees are correct and directly support the paper's central claim that coverage is preserved.

2. **Large and consistent empirical reductions in decision loss**: Across four datasets (CIFAR-100, iNaturalist, ImageNet, Fitzpatrick) and both separable and non-separable loss functions, the proposed algorithms achieve "reductions of 60-75% in loss" over standard conformal prediction (line 26). All three algorithmic variants (penalized conformal, separable penalized ratio, greedy optimizer) produce significantly lower decision loss, as shown in Figure 3 and the accompanying tables.

3. **Clinically coherent prediction sets in a real-world healthcare case study**: On the Fitzpatrick dermatology dataset, the method produces prediction sets that "contain diagnoses within a common family of malignant epidermal diseases" while satisfying coverage guarantees (Figure 1 and Section 4.2). This demonstrates that the framework can incorporate domain-specific hierarchical knowledge to produce sets that are genuinely more actionable for high-stakes decision-making.

4. **Learning-theoretic guarantee for hyperparameter selection**: Proposition 1 shows that the optimal penalty weight \(\lambda\) can be learned via empirical risk minimization with a finite-sample bound of order \(O(1/\sqrt{n})\), providing formal justification for the two-stage tuning strategy.

5. **Closed-form optimal solution for separable losses via Neyman-Pearson lemma**: The paper generalizes prior work (which only handled set size, e.g., Sadinle 2019) to arbitrary separable losses, deriving an optimal thresholding rule grounded in classical statistical theory.

6. **Demonstrated robustness to noisy base classifiers**: Ablation on the Fitzpatrick dataset (Figure 4) shows that the decision-focused methods "benefit from decision-focused conformalization even when the underlying classifier is very noisy," outperforming base conformal at every accuracy level tested.

---

## Weaknesses

### Fatal
None. The paper's core claims—that the methods maintain coverage guarantees while reducing decision loss—are supported.

### Major

1. **Insufficiently justified greedy algorithm for non-separable losses (Section 3.2.2, Eq. 8/150).** The greedy algorithm is presented as the hyperparameter-free solution for non-separable losses, but its design is not adequately explained. The paper states it is "for solving the plug-in optimization problem" (line 146) and cites Leskovec et al. (2007), but does not explain:
   - Why the selection ratio \((M - \mathcal{L}(S^i \cup \{y\}))/(1 - \hat{p}(y|x))\) takes this specific form, or what role the denominator \(1 - \hat{p}(y|x)\) plays.
   - How the greedy's constraint \(\hat{p}(y|x) \leq \alpha - p(S^i)\) relates to the plug-in problem's constraint \(\sum_{y \in S} p(y|x) \geq 1-\alpha\) (Eq. 140-141). The two constraints appear at odds—the greedy limits total probability to ≤ α (miscoverage) while the plug-in problem requires ≥ 1-α (coverage)—and the paper offers no reconciliation.
   - Whether any approximation guarantees (e.g., for submodular optimization) carry over from the Leskovec et al. framework.

   The coverage guarantee is unaffected (Proposition 3 holds for any ordering), and the empirical results show the greedy works. But the paper claims the greedy "solves" the plug-in problem, and this claim is not supported by the text. Since the greedy is a centerpiece of the non-separable hyperparameter-free approach, this gap weakens the paper's presentation of one of its stated contributions.

### Minor

1. **Absence of experimental comparison with conformal risk control (Angelopoulos et al. 2022).** The paper identifies risk control as "most closely related to our work" (line 42) and claims it "does not directly optimize the expected value" and "may sacrifice coverage." These are comparative claims without empirical backing. While the two frameworks solve different problems (coverage guarantee vs. risk control), a direct comparison on at least one dataset and loss would help readers understand when the proposed methods offer practical advantages. This is the most impactful missing experiment.

2. **Ambiguity in non-separable results interpretation.** The paper states that "penalized conformal methods, when appropriately tuned, tend to outperform the other methods we tested on CIFAR100, ImageNet, and iNaturalist" (line 191). It is unclear whether "other methods" includes the greedy optimizer in the non-separable setting. Since the greedy is presented as the hyperparameter-free alternative, readers need to know whether it underperforms penalized conformal on larger datasets, and if so, under what conditions each method is preferable.

3. **Sensitivity to the coverage level \(\alpha\) is not explored.** All experiments fix \(\alpha = 0.1\) (line 170). The trade-off between decision loss and coverage at different \(\alpha\) values is not discussed or shown. This is important for practitioners who may need to balance coverage stringency against set quality.

4. **Computational cost not discussed.** The greedy method requires per-instance optimization; for large label spaces (ImageNet has 1000 classes), this could be expensive. The paper does not report runtimes or discuss computational feasibility, which is relevant for practical deployment.

5. **Sensitivity to synthetic hierarchy construction not discussed.** For CIFAR-100 and ImageNet, hierarchies are generated via clustering on the classifier's final-layer representations (line 172). The quality of these hierarchies likely affects performance, especially for non-separable losses like coverage and max distance. The paper does not discuss sensitivity to this choice or whether results might differ with alternative hierarchy constructions.

6. **Cleaned Fitzpatrick dataset.** The paper is transparent about the cleaning procedure (lines 169-170) and tables separate both versions (Table 1). However, the 60-75% loss reduction claim in the contributions (line 26) and the conclusion are stated in aggregate without clarifying which datasets contribute most heavily. A more precise breakdown would prevent overinterpretation.

### Trivial
None that survive filtering (parser artifacts and formatting issues are not author errors).

---

## Nice-to-Haves

- A comparison to conformal risk control on at least one dataset and one non-separable loss would empirically anchor the paper's claimed advantages.
- A decision-guide table summarizing which method to use under which conditions (separable vs. non-separable loss, large vs. small dataset, high vs. low classifier accuracy) would sharpen the practical contribution.
- Discussion of how the synthetic hierarchy construction for CIFAR-100 and ImageNet affects results, or a sensitivity analysis, would strengthen the non-separable experiments.
- An ablation varying \(\alpha\) (e.g., 0.05, 0.1, 0.2) on at least one dataset would help practitioners understand the coverage-loss trade-off.

---

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"The paper states that the hyperparameter-free separable ratio method 'can also be used when the underlying classifier is noisy' (Figure 4). This is a nice ablation, but the experiment only shows that all methods degrade with worse classifiers, not that the ratio method is specifically robust to noise."** — This criticism misreads the paper. The paper claims (line 193) that "our method benefits from decision-focused conformalization even when the underlying classifier is very noisy, demonstrating that our method outperforms base conformal methods at any level of accuracy." This is a relative claim (benefits over baseline at all noise levels), not an absolute claim that the ratio method is "specifically robust to noise." The experiment supports the stated claim.

- **"The Neyman-Pearson argument for optimality under separable loss (Proposition 3) is sound but could be more clearly connected to the literature on cost-sensitive classification."** — This is a presentational preference, not a weakness.

- **"The paper uses synthetic hierarchies for CIFAR-100 and ImageNet via clustering. This is a pragmatic choice, but the quality of these hierarchies likely affects the results... A short discussion would strengthen the analysis."** — This is a reasonable observation but is already captured under Minor weakness #5 above (synthetic hierarchy sensitivity). The reviewer's version was overly speculative.

- **Several presentation and formatting nitpicks from the reviewer** — These are parser artifacts or style preferences, not substantive weaknesses.

---

## Novel Insights

The primary novel observation emerging from this review is that the paper's core contribution is strongest in the **separable loss setting** (clean Neyman-Pearson derivation, closed-form solution, clear coverage guarantees) and weaker in the **non-separable setting** (where the greedy algorithm functions more as a heuristic validated empirically than as a principled optimizer). This asymmetry is not surprising—non-separable optimization is genuinely harder—but it suggests that the paper's practical value may be highest for problems where decision losses decompose into label-wise costs. The real-world healthcare case study succeeds precisely because the coverage loss (counting intersected hierarchy categories) can be effectively handled by the greedy ordering even without formal optimality guarantees. This suggests a useful practical principle: when domain structure can inform label ordering (as hierarchies do), even a heuristic greedy can produce substantially more coherent sets, and the conformalization step provides a safety net for coverage regardless.

---

## Suggestions

1. **For the greedy algorithm**: Either (a) provide a derivation connecting the greedy selection rule to the plug-in optimization problem, explaining the role of \(1 - \hat{p}(y|x)\) and the constraint \(\hat{p}(y|x) \leq \alpha - p(S^i)\), or (b) characterize it explicitly as a heuristic (not a solution to the plug-in problem) and show on a small controlled experiment that it produces sets close to the optimal plug-in solution. A brief connection to the submodular optimization literature (if applicable) would add rigor.

2. **Add at least one empirical comparison to conformal risk control** on a representative loss (e.g., coverage loss on iNaturalist). This would help readers understand when the proposed methods genuinely outperform the closest existing baseline.

3. **Clarify the non-separable results** by explicitly stating which methods are being compared on each dataset for each loss, and under what conditions the greedy method is preferable to penalized conformal.

4. **Add a brief note on computational cost** (wall-clock time or number of operations) for the greedy method, especially on ImageNet (1000 classes), to help practitioners assess feasibility.

5. **Include an ablation on \(\alpha\)** for at least one dataset, showing how decision loss changes at different coverage levels.

---

## Score and Decision

This paper makes a genuine contribution by bridging decision-focused learning with conformal prediction, providing several concrete algorithms with coverage guarantees, and demonstrating strong empirical results including a compelling healthcare case study. The separable loss methods are clean and well-founded. The main weaknesses—insufficient justification of the greedy algorithm and the absence of a risk control comparison—are real but not fatal; they affect presentation and positioning rather than correctness. The paper's core claims (coverage preserved, loss reduced) are supported.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>