## Summary

The paper proposes a method to improve robustness of deep neural networks against adversarial attacks by modifying the loss function. For classification, it suggests using a “soft” cross-entropy loss based on posterior probabilities from a Gaussian mixture model (GMM). For regression, a weighted MSE loss is derived using posterior probabilities from GMM clustering. The paper claims this approach avoids the overhead of adversarial training or defensive distillation.

## Strengths

- None can be identified. The idea of using soft labels or probabilistic outputs is not new, and the paper provides no concrete evidence or novel theoretical insight that advances the state of the art.

## Weaknesses

### Fatal

1. **No quantitative experimental results.** The paper only makes vague, unsupported claims: “FGSM is not able to fool the trained network” and “We obtain similar results for Carlini-Wagner attack and on Imagenet dataset.” No accuracy numbers, attack success rates, baseline comparisons, or error bars are reported. Without any numerical evidence, the core claims are untestable.

2. **Method is poorly defined and mathematically suspect.** The loss function in Equation (6) is introduced with an arbitrary normalization condition that is not justified. The regression loss in Equation (7) uses an exponential weighting based on distance from the overall mean, which has no clear connection to adversarial robustness. The EM algorithm in Algorithm 1 appears to operate on the entire dataset at once, but it is never explained how it is integrated with neural network training (e.g., are GMM parameters updated per batch? Are they fixed before training?). The derivation of “probabilistic loss functions” lacks rigor.

3. **Completely insufficient evaluation.** The only “experiment” is a single qualitative example on MNIST with one FGSM perturbation (ε=0.45) showing a misclassification that is then claimed to be fixed by the proposed loss. There is no evaluation on a full test set, no comparison with standard defenses (adversarial training, distillation, label smoothing), no ablation, and no analysis of computational cost. The paper states it also works on ImageNet without providing a single number or even a qualitative result.

4. **Key algorithmic details missing.** The number of clusters for GMM is a hyperparameter that is never discussed. The prior probabilities for classification are set to 0.9 for the correct class, but this choice is arbitrary and not justified. The relationship between the EM “calibration” phase and the actual neural network training is unclear – does the loss function change during training? How are GMM parameters updated in a stochastic gradient setting?

### Major

- The paper provides no discussion of existing related methods such as label smoothing, knowledge distillation, or confidence calibration, all of which are closely related to the idea of using softer targets. The claim of novelty is not supported.
- The writing is extremely vague and contains many unsubstantiated statements (e.g., “regularization does not alleviate the problem entirely because it attempts to reduce network weights … which impacts the ability of the network to learn new patterns” – no evidence or citation).
- The scope is overly ambitious: the paper claims to handle both classification and regression but provides no regression experiment whatsoever.

### Minor

- Equation numbering is broken; Equation (6) is referenced with “?? ”.
- The reference for the AdamW optimizer (L. & F., 2024) is incorrect and appears auto-generated.
- Figures have poor quality and nonstandard annotations (e.g., “bright yellow and green pixels”).

### Trivial

- The abstract uses “adversarial training” where “adversarial examples” is meant.

## Nice-to-Haves

- If the method were clearly specified and rigorously evaluated on standard benchmarks (e.g., CIFAR-10, CIFAR-100, ImageNet) against multiple attacks and compared to baselines, it might have potential. As presented, the paper is not salvageable.

## Novel Insights

None beyond the paper’s own contributions, which are not convincingly demonstrated.

## Suggestions

- Provide full quantitative evaluation on standard datasets with multiple attack types, attack strengths, and clean accuracy.
- Compare with at least adversarial training, label smoothing, and defensive distillation.
- Clearly define how the GMM is integrated with SGD training (e.g., are GMM parameters fixed? Are they updated online?).
- Justify the choice of prior probabilities and number of clusters.
- Include regression experiments if claimed.

## Score and Decision

**MY FINAL SCORE:** <score>1</score>  
**MY FINAL DECISION:** <decision>Reject</decision>