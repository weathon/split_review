## Summary

This paper proposes that time-series forecasting (TSF) models should be designed to learn underlying dynamics, and introduces a PRO-DYN nomenclature to analyze TSF architectures through this lens. The authors identify that successful models have a learnable dynamics (DYN) function at the end of the model with pre-processing (PRO) functions before it, while underperforming models lack this structure. They validate their hypothesis by adding linear dynamics layers to four underperforming models (Informer, FiLM, MICN, FEDformer) and by converting three successful models (iTransformer, PatchTST, Crossformer) into post-processing configurations, with results supporting their claims.

## Strengths

- **Novel and well-motivated perspective**: The paper provides a fresh, principled lens for understanding why certain TSF architectures succeed or fail, moving beyond the typical focus on attention mechanisms. The connection to dynamical systems theory is conceptually sound and provides a clear framework for model analysis.

- **Systematic and rigorous experimental design**: The authors conduct extensive experiments across 25 datasets with 4 forecasting horizons (200 scores per model), use statistical significance testing (Wilcoxon test), and carefully control for confounders (parameter addition, data length variation) through the PRO-added baseline and setup conditioning analysis.

- **Clear, falsifiable hypothesis with strong empirical support**: The core claim—that learnable dynamics at the model end drives performance—is clearly stated and tested. The RQ1 results showing 51-85% of cases improved across diverse backbones (Transformer, CNN, SSM) provide compelling evidence.

## Weaknesses

### Major

- **The linear dynamics layer is a minimal and potentially insufficient instantiation of "dynamics"**: The paper equates "learnable dynamics" with a single linear layer mapping L timesteps to H timesteps. While this is a valid starting point, it is a very weak form of dynamics. The paper's title and framing suggest a more fundamental principle, but the experiments only test the simplest possible implementation. The authors acknowledge this limitation but do not explore richer dynamics (e.g., Neural ODEs, autoregressive mechanisms, or nonlinear state-space models), which would substantially strengthen the claim.

- **The PRO-DYN nomenclature, while useful, is somewhat post-hoc and descriptive rather than prescriptive**: The analysis in Table 1 identifies correlations between architecture features and performance, but the nomenclature itself does not explain *why* the DYN-at-end configuration is superior. The RQ2 experiments show that moving the DYN layer to the beginning hurts performance, but the paper does not provide a mechanistic explanation for this phenomenon. The claim that "pre-processing-like architectures take better advantage of longer look-back windows" is observational rather than explanatory.

- **The RQ2 experiment design has a confound**: In the post-processing configuration, the original DYN layer is retained as a PRO layer (since it cannot be removed without changing hyperparameters). This means the post-processing models have *two* linear layers (one at the beginning, one at the end) while vanilla models have one. The performance drop could partially be attributed to this architectural redundancy or optimization difficulty rather than purely the configuration change.

### Minor

- **The paper does not discuss computational cost or parameter count implications**: Adding a linear DYN layer adds parameters (L×H matrix plus bias). The paper controls for this with the PRO-added baseline, but a discussion of the efficiency trade-offs would strengthen the practical recommendations.

- **The Triformer case is mentioned as an exception but not fully explained**: Triformer has both green features (complete learnable dynamics, PRE-DYN configuration) but is in the underperforming group. The paper mentions this briefly in the conclusion but does not analyze why this model fails despite having the "correct" architecture.

### Trivial

- The paper uses "systemic" where "systematic" is likely intended (e.g., "systemic study" in the abstract and introduction).

## Nice-to-Haves

- Testing with nonlinear dynamics (e.g., a 2-layer MLP with residual connections) would substantially strengthen the claim that "dynamics" broadly, not just "linear dynamics," is what matters.
- An ablation study varying the position of the DYN layer within the same model (e.g., beginning, middle, end) would provide stronger evidence for the location hypothesis.
- Analysis of what the learned linear dynamics matrices look like (e.g., visualization, spectral analysis) could provide insight into what the models are actually learning.

## Novel Insights

The paper's key insight is that the success of simple linear models in TSF is not an indictment of deep learning but rather a consequence of their implicit dynamics-learning capability, which many complex architectures lack. The PRO-DYN framework provides a vocabulary for discussing this property, and the empirical demonstration that adding a single linear layer to underperforming models can recover substantial performance is practically valuable. The finding that the *location* of the dynamics block matters (at the end, not the beginning) is a non-obvious architectural guideline that could influence future TSF model design.

## Suggestions

- Strengthen the core claim by testing at least one nonlinear dynamics instantiation (e.g., a small MLP or a single-layer GRU) in the RQ1 experiments to show that the principle generalizes beyond linear mappings.
- Provide a more mechanistic explanation for why the DYN-at-end configuration is superior, perhaps through analysis of gradient flow or representation learning dynamics.
- Address the Triformer counterexample explicitly—if a model has both green features but underperforms, what additional factors (e.g., training instability, overfitting, dataset-specific issues) might explain this?

## Score and Decision

The paper makes a genuinely novel contribution by reframing TSF model analysis through the lens of dynamical systems, and the experimental validation is thorough and well-controlled. The main weakness is that the "dynamics" tested are limited to a single linear layer, which is a minimal instantiation of the concept. However, the paper is transparent about this limitation and the core hypothesis is well-supported within these bounds. The work is likely to influence how the community thinks about TSF architecture design.

**Score**: 7.0

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>