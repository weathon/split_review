## Summary

This paper proposes DIME (Discriminative Mutual Information Estimation), a method for dynamic feature selection that estimates conditional mutual information (CMI) via a simple regression objective. The key idea is to train a value network to predict the incremental loss improvement from adding a feature, which at optimality (with the Bayes classifier and cross-entropy loss) equals the CMI. This discriminative approach avoids expensive generative models while still providing CMI estimates that enable variable per-sample budgets, non-uniform feature costs, and incorporation of prior information. Experiments on tabular (medical, MNIST) and image (ImageNet subsets, histopathology) datasets show consistent improvements over baselines including Argmax Direct, EDDI, and RL-based methods.

## Strengths

- **Clean theoretical connection (Lemma 1, §4.1)**: The paper proves that under the Bayes classifier with cross-entropy loss, the expected incremental loss improvement equals the CMI. This elegantly bridges generative and discriminative approaches — CMI can be estimated via a regression objective rather than through expensive generative models or direct argmax prediction.

- **Consistent empirical gains across all tested domains (§5)**: DIME outperforms all baselines (Argmax Direct, EDDI, Hard Attention, CAE, CwCF, OL) on both tabular and image datasets across varying feature budgets. The gains are nontrivial (e.g., ~97% accuracy on Imagenette with ~7.7% of patches, >90% accuracy on MNIST with ~1.27% of pixels) and hold across both medical and general vision tasks.

- **A single model supports multiple stopping criteria and cost-weighting (§4.3)**: Because DIME estimates the CMI itself (not just the argmax), a single trained model can be evaluated with budget-constrained, confidence-constrained, or penalty-based stopping criteria, and can handle non-uniform feature costs via the ratio I/c_i. Prior discriminative methods that only output the argmax cannot decouple selection from stopping or cost adjustment without retraining.

- **Principled extension to prior information with theoretical guarantee (Theorem 2, §4.2)**: The paper formally extends CMI estimation to incorporate prior variables Z, proving that the modified objectives recover p(y|x_S, z) and I(y; x_i | x_S, z) at optimality. The MHIST experiment with Canny edge priors (§5.2) validates this improves performance.

- **Systematic ViT vs. ResNet comparison for DFS on images (§5.2)**: The paper demonstrates that Vision Transformers significantly outperform ResNets for DFS on image data, attributing this to the self-attention mechanism's suitability for partial-input problems — a practically useful finding.

## Weaknesses

### Fatal
None.

### Major

- **Theory–practice gap in CMI estimation claims.** The central theoretical claim (Lemma 1, Theorem 1) that the MSE objective recovers exact CMI assumes the predictor is the Bayes classifier and networks are infinitely expressive. In practice, the predictor is a finite-capacity neural network trained with SGD on policy-generated data. The paper acknowledges this (lines 200–203) and defers both a suboptimality analysis and a CMI estimation accuracy experiment to the appendix. However, the main text does not bound the bias, show calibration, or demonstrate that the learned value network actually approximates CMI on real problems. Since "estimating the CMI" is the paper's core framing (title, abstract, contributions), the gap between the theoretical claim (exact CMI under ideal conditions) and the practical evidence (task accuracy, not CMI accuracy) is a significant omission. This does not invalidate the paper — the method works empirically — but it weakens the central narrative that improved performance stems from accurate CMI estimation rather than from other properties of the training objective.

### Minor

- **The advantage over Argmax Direct at fixed budgets is not mechanistically explained.** At fixed budgets, both DIME and Argmax Direct select features greedily (argmax of their respective scores), so the stopping-rule advantage is irrelevant. The empirical advantage at fixed budgets must come from more accurate feature rankings, but the paper's explanation (line 202: "the policy replicates selections that improve the loss during training") is vague and does not articulate why an MSE-on-Δ objective would produce better rankings than a direct argmax objective. This is not a fatal issue — the paper's main value over Argmax Direct lies in the additional capabilities (variable budgets, non-uniform costs, prior information) — but the fixed-budget improvement is left as an unexplained empirical observation.

- **Proposition 1's connection to the λ-based stopping rule is overstated in the framing.** Proposition 1 states that average-budget policies dominate per-prediction-budget policies. The paper then proposes a λ-based stopping rule (stop when max_i CMI/c_i < λ), which is itself a per-prediction threshold. The paper acknowledges this (line 299: "our penalized criterion is not the optimal one alluded to in Proposition 1"), but the abstract and introduction frame "allowing variable per-sample feature budgets" as a key contribution following from CMI estimation. The λ rule is a reasonable heuristic and works empirically, but the logical thread from Proposition 1 to λ is broken — Proposition 1 motivates average constraints, while λ is a per-prediction threshold. A clearer framing would present λ as a separate heuristic rather than as flowing from the theoretical analysis.

- **Training time, inference cost, and model size are not reported.** The paper motivates DIME in part as more efficient than generative methods, but it provides no runtime, FLOP, or parameter count comparisons. This makes it difficult to assess the practical efficiency claims.

### Trivial
None.

## Nice-to-Haves
- The CMI estimation accuracy experiment and suboptimality analysis should be promoted from the appendix to the main text, or at least summarized with key quantitative findings. This would directly address the theory–practice gap.
- An ablation comparing DIME's argmax (ignoring CMI magnitudes) against Argmax Direct at fixed budgets would clarify whether the advantage comes from better rankings or from something else.
- Reporting training time per epoch or inference latency would strengthen the efficiency motivation.

## Removed Points
These points are flagged for removal; treat them with caution:
- **"Tables/figures not verifiable due to stripped inserts"**: Parser limitation, not a paper error. The paper submitted with full figures.
- **"The 'Intubation' dataset is private"**: Stated transparently (line 427). Two of three tabular datasets (ROSMAP, MNIST) are public, and code is provided.
- **"ϵ-greedy schedule and replay buffer not specified in main text"**: Standard implementation details deferred to appendix; common practice in this venue.
- **"RL methods claim relies on self-supporting citations"**: A characterization of the literature, not a weakness of the paper's own contribution.
- **"Joint optimization may have other optima"** (from the critic's section-by-section note): Speculative; the theorem explicitly assumes infinitely expressive networks.
- Several strengths from Strength Finder that were generic or redundant were merged into the core strengths above.

## Novel Insights
The harsh critic's observation that DIME's advantage over Argmax Direct at fixed budgets is unexplained reveals an interesting tension: the paper's framing (CMI estimation → better stopping rules → better performance) is partially decoupled from the actual mechanism producing the fixed-budget gains. This suggests the regression-on-Δ objective may have benefits (richer training signal, better regularization) that go beyond CMI estimation per se. The paper would be stronger if it acknowledged this possibility explicitly.

## Suggestions
1. Add a main-figure calibration plot or correlation analysis showing that v_i(x_S) tracks true CMI as features are progressively selected. This would directly substantiate the core claim.
2. Add an ablation isolating the ranking quality: compare DIME's argmax (ignoring magnitude) against Argmax Direct at fixed budgets. If DIME still wins, the advantage comes from the objective function itself, not from CMI-estimation-enabled stopping rules.
3. Clarify the framing around Proposition 1 and the λ rule: present Proposition 1 as motivation for *why* variable budgets are desirable, not as justification for the specific λ heuristic.
4. Report approximate training time or inference FLOPs to support efficiency claims.

## Score and Decision

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>