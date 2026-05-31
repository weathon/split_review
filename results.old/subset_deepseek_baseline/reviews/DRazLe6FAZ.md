## Summary

This paper proposes that time-series forecasting models should be designed to learn underlying dynamics, and introduces a PRO-DYN nomenclature to analyze TSF architectures through the lens of temporal dynamics. Through systemic analysis of existing models and extensive experiments, the authors demonstrate that (1) adding learnable dynamics (linear layers) to models lacking them improves performance, and (2) the optimal configuration places the dynamics block at the end of the model as a predictor rather than at the beginning.

## Strengths

- **Novel analytical framework**: The PRO-DYN nomenclature provides a principled way to decompose and analyze TSF models based on how they handle temporal relationships, offering a fresh perspective beyond traditional architectural taxonomies.
- **Comprehensive experimental validation**: The paper tests its hypotheses across 25 datasets with 4 forecasting horizons each (200 scores per model), covering diverse model families (Transformers, CNNs, SSMs) and providing statistical significance testing.
- **Clear research questions and systematic investigation**: The two research questions are well-motivated from the systemic analysis, and the experimental design cleanly isolates the effect of dynamics learning from confounding factors like parameter addition and data length variation.
- **Practical implications**: The finding that dynamics should be placed at the model end provides actionable design guidance for practitioners building TSF systems.

## Weaknesses

### Fatal
None.

### Major
- **Limited scope of dynamics**: The paper only considers linear dynamics (a single linear layer) as the DYN function. While this is a reasonable starting point, the claim that "dynamics is what you need" is not fully supported when only the simplest possible dynamics is tested. More complex dynamics (e.g., nonlinear, autoregressive, or state-space formulations) could yield different conclusions.
- **Incomplete isolation of confounders in RQ2**: The post-processing configuration changes multiple aspects simultaneously (adding a DYN layer at the input, converting the original DYN to PRO, changing data flow). The performance degradation could stem from architectural disruption rather than the configuration change per se. A cleaner ablation would keep the original DYN function and only add a PRO function before it.
- **The Triformer anomaly is not adequately addressed**: Triformer has both green features (complete learnable dynamics, PRE-DYN configuration) but is in the under-performing group. This counterexample weakens the paper's central claim and deserves more thorough discussion than a brief mention in the conclusion.

### Minor
- **The PRO-DYN nomenclature, while useful, relies on somewhat arbitrary definitions**: The classification of functions as PRO vs. DYN based on Allen's interval relations is clever but the mapping from mathematical function properties to these temporal relations is not always unambiguous, especially for complex multi-step computations.
- **The performance driver analysis for RQ1 (Figure 5) shows mixed results**: FiLM DYN is not statistically better than its PRO version, and the authors attribute this to "conflict with SSM encoding" without experimental verification. This weakens the generality of the RQ1 conclusion.

### Trivial
None.

## Nice-to-Haves

- Testing with nonlinear dynamics (e.g., a small MLP or Neural ODE block) would strengthen the claim that dynamics learning per se (not just linear mapping) drives performance.
- A controlled experiment where the original DYN function in SOTA models is replaced with a different type of dynamics (e.g., an SSM-based dynamics) would test whether the linear nature of the dynamics matters.
- Analysis of which specific datasets or forecasting horizons benefit most from dynamics addition could provide deeper insights.

## Novel Insights

The paper's key insight is that the success of simple linear models in TSF is not due to their simplicity but because they inherently learn dynamics, while many complex deep models fail because they use non-learnable or partially learnable dynamics (e.g., zero-padding, mean prediction). This reframes the conversation from "why do simple models beat complex ones" to "what architectural properties enable effective dynamics learning." The finding that dynamics should be placed at the model end (PRE-DYN configuration) is a concrete design principle that explains why recent SOTA models like PatchTST and iTransformer succeed while earlier Transformer-based models fail.

## Suggestions

- Conduct an experiment where the DYN function in SOTA models is replaced with a richer dynamics (e.g., a small RNN or Neural ODE) to test whether the benefits scale with dynamics complexity.
- Add a controlled ablation for RQ2 where the original DYN function is kept and only a PRO function is added before it, to isolate the effect of configuration from architectural disruption.
- Provide a more detailed analysis of the Triformer case to understand why it violates the pattern, which could reveal additional important factors beyond dynamics.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>