## Summary
The paper investigates whether predictive uncertainties in deep learning follow power-law scaling laws with dataset size and model size, analogous to those observed for test loss. Through extensive experiments on vision (CIFAR-10, ImageNet32, CIFAR-10-C) and language (GPT-2 on algorithmic datasets) tasks, using MC Dropout, Deep Ensembles, MCMC, and variational inference methods, the authors report that epistemic, aleatoric, and total uncertainties indeed decay as power laws of the amount of training data. The paper also provides a theoretical connection to Bayesian linear regression and singular learning theory to explain these scaling behaviors.

## Strengths
- **Novel and timely research question**: The paper is among the first to systematically study scaling laws for predictive uncertainty in deep learning, which is of high practical interest for Bayesian deep learning and safe deployment.
- **Comprehensive empirical scope**: The study covers multiple architectures (ResNet, WideResNet, ViT, GPT-2), multiple uncertainty quantification methods (MC Dropout, Deep Ensembles, MCMC, IVON), and both in-distribution and out-of-distribution settings.
- **Practical counterpoint to a common skepticism**: The results demonstrate that epistemic uncertainty does not vanish even with moderate-to-large datasets, providing evidence that Bayesian methods remain relevant in the "big data" regime.

## Weaknesses
### Major
- **Insufficient data to reliably claim power-law scaling**: Each scaling curve is typically fitted to only 3–4 data points (e.g., 25%, 50%, 75%, 100% of the training data). This provides at most a factor of 4 in the dataset-size range, which is far too narrow to distinguish a power law from other functional forms (e.g., exponential, logarithmic). No confidence intervals, goodness-of-fit tests, or comparisons to alternative models are reported. The visual linearity on a log-log plot with so few points is weak evidence.
- **Theoretical contribution is limited**: The only formal derivation is for Bayesian linear regression—a well-known, identifiable model that is far from the over-parameterized neural networks studied experimentally. The connection to singular learning theory (SLT) is speculative and not developed into any testable prediction or bound for the observed exponents. The paper therefore lacks a theoretical framework that explains *why* the observed power-law exponents take the values they do (e.g., -0.44, -0.36, -0.80) or why they vary across methods.
- **Key experiments contradict or weaken the central claim**: The ViT experiments (Fig. 4) show that the uncertainty scaling behavior strongly depends on optimizer choice and training length, undermining the idea of a stable, method-agnostic scaling law. The Phi-2 language experiment shows flat uncertainties across data subsets, which the authors attribute to pretraining but does not fit the claimed power-law pattern. These results are presented as supporting evidence but actually raise serious doubts about the universality of uncertainty scaling laws.
- **No evaluation of practical usefulness**: The paper mentions potential applications in active learning and budget estimation but provides no experiments or quantitative demonstrations. The claim that scaling laws allow extrapolation to larger N is not validated (e.g., by withholding large-data results and testing predictions).

### Minor
- **Uncertainty metrics have known limitations**, which the paper acknowledges but does not address. The additive decomposition of TU into AU and EU is contested in the literature (Wimmer et al. 2023), and the metrics may not be disentangled. This weakens the interpretability of the separate TU, AU, and EU scaling results.
- **The "first study" claim is strong** and may be contestable given prior work on calibration scaling or uncertainty in Gaussian processes. The paper does not provide a dedicated literature search to substantiate this.

### Trivial
- The text has minor inconsistencies (e.g., mismatch between caption and description of Figure 6 regarding MCMC(1) vs MCMC(2)). These do not affect the scientific evaluation.

## Nice-to-Haves
- Fitting the power law on a wider range of dataset sizes (at least an order of magnitude) and reporting goodness-of-fit statistics (R², comparison with alternative models such as exponential or logarithmic).
- Providing a validation experiment where scaling exponents estimated from smaller N are used to predict uncertainty at larger N, demonstrating practical extrapolation.
- Exploring the dependence of the power-law exponent on architecture depth, width, or data dimensionality in a more systematic way.

## Novel Insights
None beyond the paper’s own contributions.

## Suggestions
- At minimum, include error bars or confidence intervals on the power-law exponents (e.g., via bootstrapping) and add the raw data points to a supplemental table.
- Reduce the strength of claims: replace "scaling laws" with "empirical power-law trends" and acknowledge the limited data range and method-dependent variation.
- Add a negative control: test whether random (untrained) ensembles also produce a similar log-log slope, to confirm that the pattern is not an artifact of the loss-function geometry.
- Derive or cite a theoretical prediction for the exponent (e.g., from the intrinsic dimension of the data manifold) and compare to the observed values.

## Score and Decision
This paper addresses a relevant and novel question, and the breadth of experiments is commendable. However, the empirical evidence for scaling laws is weak due to the very limited number of data points per curve and the absence of rigorous fit evaluation. The theoretical contribution is minimal and does not support the central empirical findings. Several experimental results contradict the universal scaling claim. Therefore, the paper does not yet provide sufficient evidence to convince a critical reader of its main thesis.

MY FINAL SCORE: 4.0</score>  
MY FINAL DECISION: Reject</decision>