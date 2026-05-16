Now I have all the information I need to produce a thorough, verified review. Let me synthesize everything.

## Summary

This paper identifies a confound in prior evaluations of unseen-class unlabeled data in semi-supervised learning (SSL): earlier work fixed total unlabeled dataset size while varying the proportion of unseen classes, which simultaneously changed the amount of seen-class data, violating the controlled variable principle. The paper proposes the RE-SSL framework, which fixes the seen-class ratio and varies only the unseen-class ratio, and evaluates 15 SSL algorithms across five factors (sample-number, category-number, category-index, nearness, label distribution) using five robustness metrics. The central finding is that unseen classes do not necessarily impair SSL performance—several methods (e.g., ICT, PseudoLabel) are robust or even benefit from unseen-class data under properly controlled conditions.

## Strengths

- **Identifies a genuine confound in prior SSL evaluation protocols.** The paper uses a structural causal model (Figure 1) to formalize why fixing total |D_U| while varying unseen-class proportion creates a spurious correlation between seen- and unseen-class data. This is a novel and well-motivated critique that prior safe SSL evaluations overlooked.

- **Proposes a principled corrected evaluation framework (RE-SSL).** The core idea—holding seen-class unlabeled data constant (fixing \(r_s\)) while varying unseen-class data (\(r_u\))—is conceptually sound and directly removes the confound identified in prior work. The dataset construction is clearly illustrated in Figure 2.

- **Demonstrates a non-obvious finding that challenges a prevailing assumption.** The main results (Tables 1, 2) show that under the corrected protocol, multiple SSL methods have near-zero or even positive \(R_{\text{slope}}\) (e.g., ICT: +0.039 on CIFAR10, PseudoLabel: -0.010, UASD: -0.019). Extended experiments (Table 3) show that accuracy can increase as the number of unseen-class categories grows (e.g., MixMatch from 0.496 at base to 0.606 at \(C_n=5\)), directly contradicting the assumption that unseen classes always harm SSL models.

- **Explores five orthogonal factors of unseen-class impact.** Beyond sample-number (\(r\)), the paper examines category-number (\(C_n\)), category-index (\(C_i\)), nearness (CIFAR vs. MNIST), and label distribution (\(C_{ib}\)). This multi-dimensional exploration goes well beyond prior work's narrow focus on sample-number alone.

- **Provides actionable algorithm-level insights.** The analysis identifies which algorithms are robust (ICT, PseudoLabel, PiModel, UASD, CAFA) and offers reasoned explanations—e.g., ICT's Mixup mitigates unseen-class interference; FixMatch's fixed threshold makes it overly sensitive. These insights provide practical guidance for model selection in deployment scenarios with potential unseen-class contamination.

## Weaknesses

### Fatal
None.

### Major
None. (The weaknesses identified below are real but do not threaten the core contribution.)

### Minor

1. **Metrics for extended factors are not formally redefined.** The five evaluation metrics (\(R_{\text{slope}}\), GM, WAD, BAD, \(P_{AD\ge0}\)) are formally introduced in §3.2 for the factor \(r\) (a ratio from 0 to 1), with integral forms over continuous \(r\). When these metrics are applied to the category-number factor \(C_n\) (Table 3), category-index factor \(C_i\) (Table 4), and label-distribution factor \(C_{ib}\) (Table 5), the paper does not explicitly restate how each metric is computed for the new independent variable. For instance:
   - In Table 3, \(R_{\text{slope}}\) is reported for accuracy vs. \(C_n\) (integer values 1–5), but the paper never says "we fit a linear regression of accuracy on \(C_n\) and report the slope."
   - For \(C_i\) (Table 4), the paper notes that only GM is used because the values lack a progressive relationship, but the original GM is an integral over continuous \(r\); the discrete adaptation for category-index values is not specified.
   - For \(C_{ib}\) (Table 5), both \(R_{\text{slope}}\) and GM are reported without restating the formula.

   This does not invalidate the results (the adaptation is conceptually straightforward and the comparisons within each table are internally consistent), but it makes exact reproducibility harder and should be clarified.

2. **No direct empirical comparison with the prior (confounded) evaluation protocol.** The paper critiques prior methods (DS3L, Safe-Student) for using a flawed protocol, but never replicates that protocol on the same algorithms to show that conclusions would differ. A side-by-side comparison—e.g., plotting accuracy curves under the old protocol (fixing total |D_U|, varying unseen proportion) vs. RE-SSL—would empirically validate the central motivation. As it stands, the critique remains a logical argument rather than an empirically demonstrated confound. This weakens the persuasiveness of the motivation but does not undermine the paper's independent contribution: the RE-SSL framework and findings stand on their own as a corrected methodology.

3. **No uncertainty quantification.** All experiments are run with three seeds (0, 1, 2) and averaged, but no standard deviations, confidence intervals, or per-seed ranges are reported. Given the fine-grained distinctions drawn between algorithms (e.g., "PseudoLabel and ICT are relatively robust" vs. "FixMatch is very sensitive"), the reader cannot assess whether observed differences are statistically reliable. Reporting variance is standard practice and should be straightforward to add.

4. **Value of the fixed seen-class ratio \(r_s\) is not specified.** The paper states that \(r_s\) is fixed (line 40) but never discloses its numerical value. For a paper whose core contribution is a controlled evaluation framework, this is a notable omission that hampers reproducibility. The experiments cannot be exactly replicated without knowing this parameter.

### Trivial

- **The robustness threshold (\(\sigma_g = -0.020\)) is chosen without justification.** The paper "assumes" \(\sigma_g = -0.020\) to categorize algorithms as robust vs. sensitive (line 128). Since the actual \(R_{\text{slope}}\) values are reported in full, the threshold mainly affects narrative framing (robust vs. sensitive labels) rather than the quantitative contribution. A relative ranking by \(R_{\text{slope}}\) would avoid the arbitrary threshold.
- **The linearity assumption for \(R_{\text{slope}}\) is not acknowledged.** The regression function assumes a linear relationship between accuracy and \(r\) over seven discrete points. The paper does not discuss whether this assumption is reasonable or how nonlinearities might affect interpretation.
- **The label-distribution experiment (§5.4, Table 5) does not specify how many unseen classes are used.** The imbalance factor \(C_{ib}\) is defined, but the number of unseen-class categories in this setting is not stated, adding minor ambiguity.
- **The "far OOD" experiment (MNIST vs. CIFAR-10) confounds nearness with dataset-level differences (grayscale vs. color, digit vs. natural image).** The conclusion that "smaller semantic shift → less damage" is directionally sound but the magnitude of the observed difference may partially reflect low-level feature disparities, not purely semantic nearness. A brief acknowledgment would be appropriate.

## Nice-to-Haves

- A replication-comparison with the old (confounded) protocol using one representative prior method (e.g., DS3L) would substantially strengthen the paper's motivational narrative.
- A sensitivity analysis on the fixed value of \(r_s\) (e.g., trying two different \(r_s\) values) would test whether the conclusions are robust to the choice of this parameter.
- Explicit GPU-hour estimates would help future users assess the cost of adopting the RE-SSL framework.

## Removed Points

These points are flagged to be removed; treat them with caution.

- *"The examples of SSL in NLP and image recognition are generic and add no weight"* — Generic language in the introduction is a presentational nitpick, not a substantive weakness.
- *"The structural causal model slightly over-promises"* — The paper uses the causal model appropriately to motivate the framework; it does not claim to do causal inference beyond identifying the confound. The reviewer's concern is overblown.
- *"The integral forms... but the data only exists at seven discrete points"* — The paper already acknowledges this: "The integrals in Eq. 1 and Eq. 2 are computed as accumulation operations based on empirical values" (line 84). The reviewer's concern is addressed.
- *"Missing related works"* — Per instructions, I cannot confirm the existence of missing references and should not raise this.
- *"Typos, formatting, style nitpicks"* — These are parser artifacts, not author errors.
- *"ResNet-50 is large for CIFAR with 100 labels"* — This is standard practice in the SSL literature; criticizing it is a matter of preference, not a real weakness.
- *"The paper does not discuss computational cost"* — This is a nice-to-have, not a weakness.
- *"The paper uses 'safe SSL' and 'robust SSL' interchangeably"* — This is a minor terminology preference, not a substantive issue.

## Novel Insights

The most interesting insight from synthesizing these reviews is that the paper's two most significant weaknesses—the undefined metrics for extended factors and the lack of direct replication—are actually complementary. If the paper had provided rigorous formal definitions for how the metrics generalize beyond the ratio factor \(r\), it would immediately enable a precise replication of the prior protocol as a special case (where both \(r_s\) and \(r_u\) vary jointly). Making those definitions explicit would both fix the reproducibility gap and naturally enable the direct comparison that would empirically validate the confound critique. This suggests a clean path forward: unified notation for metric computation over arbitrary ordered/continuous factors would solve both problems at once.

## Suggestions

1. **Provide formal, explicit definitions of how each of the five metrics is computed for each of the five factors.** For each factor, specify the independent variable, its range and discretization, and the exact formula used for slope, GM, WAD, BAD, and \(P_{AD\ge0}\). A single table mapping factor → metric applicability → formula would be ideal.
2. **Disclose the numerical value of \(r_s\) used in all experiments** and consider adding a brief sensitivity analysis with an alternative value.
3. **Report standard deviations or per-seed ranges** for key accuracy values and metrics to allow readers to assess the reliability of the observed differences.
4. **Replace the arbitrary threshold \(\sigma_g = -0.020\)** with a relative ranking by \(R_{\text{slope}}\) when discussing algorithm robustness, or provide a principled justification for the chosen threshold.
5. **Add a brief acknowledgment of the linearity assumption** for \(R_{\text{slope}}\) and note that it captures only the overall trend.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>