## Summary
This paper proposes Fed-MADS, a federated active learning framework that uses the Information Bottleneck principle to select informative unlabeled data points for labeling. The method computes a selection score based on KL-divergence between local and global model latent representations and cross-entropy between their predictions, selecting samples with the largest divergence. Experiments on four benchmark datasets show improvements over existing FAL methods in model accuracy, rule accuracy, and rule fidelity.

## Strengths
- **Novel application of IB principle to FAL**: The paper is the first to connect Information Bottleneck theory with federated active learning, providing a principled theoretical foundation for data selection that goes beyond simple uncertainty-based approaches.
- **Clean integration with XFL framework**: The design choice of implementing variational distributions using local and global parametric models is elegant and naturally fits the federated learning setting, making the approach practically deployable.
- **Comprehensive evaluation with explainability metrics**: Beyond standard accuracy, the paper evaluates rule accuracy and rule fidelity, which are directly relevant to the XFL setting and demonstrate the method's impact on model interpretability.

## Weaknesses
### Fatal
None.

### Major
- **Theoretical derivation contains a critical error**: The derivation from Eq.(7) to Eq.(8) is mathematically incorrect. The authors claim that because KL-divergence and cross-entropy are nonnegative, Eq.(7) ≤ the RHS of Eq.(8). However, Eq.(7) contains negative terms (-𝔼[H_{P,Q}(z|x)] and +β𝔼[H_{P,Q}(y|z)]) that are not bounded by the RHS expression. The inequality direction is not justified, and the surrogate objective in Eq.(8) is not a valid upper bound of the original objective. This undermines the theoretical foundation of the method.
- **The minimax formulation is not actually implemented**: The paper claims a minimax objective in Eq.(13), but Algorithm 1 simply selects top-b samples by score without any adversarial optimization or iterative minimax procedure. The "max" over Q is trivially solved by ranking, and there is no "min" component in the data selection step. The minimax framing is misleading.
- **Limited experimental scope**: All experiments use only 10 clients with i.i.d. data splits. The paper does not evaluate non-i.i.d. settings, which are the primary challenge in federated learning. Additionally, only one base model (LR-XFL) is tested, making it unclear whether the method generalizes to other XFL architectures.

### Minor
- **The ablation study is limited**: Only the β parameter is ablated. There is no ablation of the two score components (latent KL vs. prediction cross-entropy) to understand their individual contributions, nor an ablation of the global model's role versus using only local model information.
- **Missing statistical significance tests**: The paper reports mean and standard deviation but does not perform statistical tests (e.g., paired t-tests) to verify whether improvements over baselines are statistically significant.
- **The analysis section is superficial**: The communication and computation cost analysis (Section 3.4) is too brief and lacks quantitative comparisons with baseline methods.

### Trivial
- The figure caption in Figure 2 is repeated verbatim three times, which is redundant.

## Nice-to-Haves
- Evaluate on non-i.i.d. data partitions, which is the more realistic and challenging FL scenario
- Test with multiple XFL architectures beyond LR-XFL to demonstrate generalizability
- Include an ablation study that isolates the contribution of the latent representation divergence term vs. the prediction divergence term
- Provide theoretical or empirical analysis of why the proposed selection criterion works better than uncertainty-based methods

## Novel Insights
The paper's core insight—that divergence between local and global models in both latent space and prediction space is a useful signal for active learning in federated settings—is genuinely interesting and practically motivated. The idea that samples where local and global models disagree most are the most informative for labeling is intuitive and aligns with the goal of improving global model generalization. However, the theoretical justification via IB is not rigorous, and the practical contribution stands independently of the flawed derivation.

## Suggestions
1. Fix the theoretical derivation: either provide a correct upper bound derivation or reframe the method as a heuristic motivated by IB principles rather than a rigorous IB-based objective.
2. Rename or reframe the "minimax" aspect: the current algorithm is simply top-b selection, not a minimax procedure. Either implement a true minimax optimization or remove the minimax terminology.
3. Add experiments with non-i.i.d. data distributions and at least one additional XFL architecture to demonstrate robustness and generalizability.

## Score and Decision
The paper presents a novel and well-motivated approach to federated active learning with clear practical benefits. However, the flawed theoretical derivation and misleading minimax framing are significant issues that undermine the paper's claims. The empirical results are promising but limited in scope. The core idea has merit, but the paper needs substantial revision to address the theoretical and experimental gaps.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>