Now I have all the information I need. Let me produce the final consolidated review.

## Summary

This paper addresses fairness-accuracy tradeoffs when demographic information is only partially available (the "demographic scarce regime"). The authors propose FairDSR, a two-stage framework that: (1) trains an uncertainty-aware attribute classifier using self-ensembling and Monte Carlo dropout, and (2) enforces fairness constraints only on samples whose proxy sensitive attributes are predicted with low uncertainty. The paper demonstrates across five datasets that this uncertainty-aware selection can yield better fairness-accuracy tradeoffs than standard proxy-attribute approaches, and shows through ablations with conformal prediction that the finding is not tied to a single uncertainty measure.

## Strengths

- **Novel and well-motivated idea of using uncertainty in the attribute classifier to guide fairness enforcement.** The paper's core hypothesis — that samples with uncertain proxy attributes are inherently harder to discriminate against, while samples with reliable attributes drive unfairness — is intuitive and supported by the analysis in Table 1 and Figure 3. This reframes the problem from "how to impute the sensitive attribute accurately" to "when to trust the imputation for fairness purposes."

- **Solid empirical evidence across multiple datasets, classifiers, and uncertainty measures.** The paper validates on five real-world benchmarks (Adult, Compas, LSAC, CelebA, New Adult), with multiple base classifiers (Random Forest, Logistic Regression) and two distinct uncertainty estimation methods (MC dropout, conformal prediction). The conformal prediction ablation (Figure 7, Table 4) is particularly convincing, showing that the same pattern holds under a fundamentally different uncertainty framework with formal coverage guarantees. This breadth of validation strengthens the paper's central finding substantially.

- **Ablations cleanly isolate the contribution of each design choice.** The consistency loss ablation (Figure 6) shows that removing it degrades the Pareto front below even the Proxy-DNN baseline, confirming the importance of the self-ensembling training. The uncertainty-threshold analysis (Figure 5) reveals the monotonic relationship between uncertainty and fairness, and the confidence-interval ablation (Figure 4) demonstrates why naive confidence-based uncertainty is insufficient. These controlled experiments make the paper's mechanistic claims more credible.

- **Competitive performance against relevant baselines.** On the Adult dataset, FairDSR (certain) achieves ΔDP=0.007, ΔEOP=0.015, ΔEOD=0.018 with accuracy 0.830 — clearly better than CGL (0.009, 0.027, 0.026 with acc 0.834) and FairDA (0.087, 0.071, 0.078 with acc 0.809), which are the most directly comparable methods. On Compas, FairDSR (weighted) achieves the lowest demographic parity (0.027) among all methods while maintaining competitive accuracy (0.672).

## Weaknesses

### Fatal

None.

### Major

- **The central claim of "outperforming models trained with fairness constraints on the true sensitive attributes in most benchmarks" is overstated relative to the evidence.** On Adult (Table 2), FairDSR (certain) achieves ΔDP=0.007 vs VanilaFairness's 0.005, ΔEOD=0.018 vs 0.017 — these differences are within 1 standard deviation on every metric. On Compas (Table 3), FairDSR (certain) has worse fairness on all three metrics (ΔDP=0.085 vs 0.032, ΔEOP=0.067 vs 0.039, ΔEOD=0.074 vs 0.041) while being more accurate (0.676 vs 0.634). These are different tradeoff points, not an unambiguous improvement. The conformal prediction ablation on Adult (Figure 7) does show clear Pareto-dominance over the true-attribute baseline, which supports the claim on *Adult specifically*, but "most benchmarks" requires evidence from more datasets — LSAC, CelebA, and New Adult results are in supplementary. The authors should either (a) scale back this claim to "comparable or better on some benchmarks" or (b) bring the supplementary results to the main paper to substantiate it.

- **Single-point comparisons for most baselines, without full tradeoff curves, make it impossible to verify whether FairDSR Pareto-dominates them across the tradeoff spectrum.** The paper reports one operating point per method in Tables 2–3, each tuned to "achieve minimal fairness violation." But different methods have different tradeoff shapes: on Compas, CGL achieves lower ΔEOD (0.065) but lower accuracy (0.612) than FairDSR (certain) (ΔEOD=0.074, acc=0.676). Which is better depends on the application's relative weight on fairness vs. accuracy. The Pareto fronts in Figure 3 cover only FairDSR variants vs. Proxy-DNN and Clean, omitting CGL, FairDA, FairRF, and others. Without tradeoff curves for all relevant baselines, the reader cannot assess whether the claimed superiority holds across the entire tradeoff space or only at the specific operating point chosen.

### Minor

- **The causal mechanism behind the paper's hypothesis is asserted but not rigorously tested.** The paper shows a clear *correlation* between attribute prediction uncertainty and downstream fairness (Table 1, Figure 3), and the conformal prediction ablation adds credibility. However, alternative explanations are not ruled out: datasets with more separable sensitive attributes may also have stronger feature-attribute confounding, making discrimination easier regardless of uncertainty-based selection. FairDSR (uncertain) prunes low-uncertainty samples, which changes the training distribution in ways that could independently improve fairness (e.g., balancing group proportions, removing majority-class samples). The paper does not analyze the demographic composition or feature distributions of the selected subsets to verify the hypothesized mechanism. A controlled experiment — partitioning data by uncertainty matched on group proportions — would substantially strengthen the causal claim.

- **The evaluation protocol for single-point comparisons is underspecified.** The paper states that baselines are trained "to achieve minimal fairness violation" (line 149) but does not describe how the fairness-accuracy tradeoff hyperparameter λ was selected for each method. Were all λ explored and the fairest model picked? Or was λ tuned for each method independently on a validation set? If the latter, different methods may be at different points on their tradeoff curves, making cross-method comparisons unreliable. This concern is partially addressed by the Pareto fronts for the proposed variants, but not for the other baselines.

- **The paper mentions adversarial debiasing as a fairness mechanism under consideration (line 49) but never reports results for it.** If adversarial debiasing was tested, the results should be included; if not, the mention should be removed to avoid misleading readers about the scope of the evaluation.

### Trivial

- The threshold R (for the consistency loss) is mentioned but its selection procedure is not described, unlike threshold H which is clearly explained.
- The number of λ values swept for the Pareto fronts is not specified.

## Nice-to-Haves

- Providing tradeoff curves (Pareto fronts) for all methods on all datasets — not just FairDSR variants vs. Proxy-DNN and Clean — would allow rigorous assessment of dominance claims.
- Reporting the demographic composition and feature statistics of the selected subsets (low- vs. high-uncertainty samples) would help validate the hypothesized mechanism and rule out selection-bias confounds.
- Bringing LSAC, CelebA, and New Adult results into the main paper (or adding statistical tests across all datasets) would make the "most benchmarks" claim verifiable without consulting supplementary.

## Removed Points

The following points from the reviews were removed with justification:

1. **"Notation issues (\Dtwo, \Done appearing without explanation)"** — These are LaTeX macros that render as $D_1$, $D_2$ in the actual paper and are defined in Section 3 (line 11). The extracted plaintext shows raw LaTeX, which is a parser artifact.

2. **"The paper includes ARL, DRO, CVaR DRO which are not directly comparable"** — The paper itself acknowledges (line 268) that these methods optimize worst-case accuracy, not group fairness. Including them provides contextual baselines and does not harm the paper's claims about its own method. The comparison is clearly labeled.

3. **"Only two datasets (Adult and Compas) given full treatment"** — This is a presentation choice common in ML papers with length constraints. The supplementary material contains results on LSAC, CelebA, and New Adult. The authors do not hide these results.

4. **"Pure formatting/style nitpicks"** — Minor phrasing concerns were removed as they do not affect the scientific contribution.

## Novel Insights

The most interesting observation spanning the reviews is that the paper's central finding — uncertainty in proxy attributes correlates with downstream fairness — is simultaneously the paper's most original contribution and its weakest link. The Strength Finder correctly identifies this as a novel empirical finding supported across two different uncertainty estimation frameworks (MC dropout and conformal prediction), while the Harsh Critic correctly points out that this remains a correlational finding without causal verification. This tension is productive: the paper has identified a real and practically useful phenomenon, but the exact mechanism is underspecified. Future work strengthening the causal case would significantly elevate the contribution.

## Suggestions

1. Scale back the claim about outperforming true-attribute models to match the evidence — e.g., "achieves comparable or better fairness-accuracy tradeoffs on several benchmarks" rather than "can outperform... in most benchmarks." This simple change would eliminate the largest mismatch between claims and evidence.

2. Provide a demographic composition analysis of the selected subsets (low- vs. high-uncertainty samples). Show whether the selection disproportionately removes certain groups and whether the observed fairness improvement persists after controlling for group balance.

3. Include Pareto front tradeoff curves for CGL and FairDA — the two most directly comparable proxy-attribute methods — to substantiate the claim that FairDSR Pareto-dominates them, rather than only being better at a single operating point.

## Score and Decision

The paper tackles a real and important problem with a clever, well-motivated idea. The empirical work is substantial: five datasets, multiple classifiers, two uncertainty frameworks, and targeted ablations. The core finding — that selective fairness enforcement based on attribute uncertainty improves tradeoffs — is validated convincingly across multiple experimental settings.

The main weakness is a mismatch between the strength of the claims and the strength of the evidence, particularly the overstated "outperform true sensitive attributes" claim. The evaluation, while solid, would benefit from comprehensive tradeoff curves for all baselines. However, these are issues of presentation and experimental thoroughness, not fundamental flaws in the approach.

The paper makes a genuine contribution to an important sub-area of fairness research and the core findings are reproducible from the provided information.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>