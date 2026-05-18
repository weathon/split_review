Now I have a thorough understanding of the paper and the reviews. Let me construct the final consolidated review.

---

## Summary

This paper proposes a lightweight, plug-and-play defense against query-based black-box attacks: adding Gaussian noise to intermediate hidden features of a pre-trained model at inference time (rather than adding noise to the input). The authors provide a theoretical analysis (Theorem 1) linking the defense's effectiveness to the ratio of the gradient norms at the feature versus input level and the ratio of defense-to-attack noise variance. They evaluate against five attacks (NES, Square, SignHunt, RayS, SignFlip) on both CNNs and transformers across CIFAR-10 and ImageNet, and also test against adaptive EOT attacks and in combination with adversarial training.

## Strengths

- **Theoretical connection between gradient norms and defense effectiveness**: Theorem 1 provides a closed-form expression connecting the probability of misleading the attacker to the ratio of gradient norms at the feature and input levels and the noise variance ratio. The analysis further shows (Section 3.2, Figure 1) that this gradient ratio increases as the attacker perturbs the input toward adversarial samples, suggesting the defense becomes more robust during the attack. This goes beyond prior input-noise defenses (RND, SND) which relied solely on empirical evaluation.

- **Consistent empirical superiority over input defenses across most architectures and attacks**: On ImageNet, the feature defense outperforms input defense on 5 out of 6 models under Square attack at 10,000 queries with 2% accuracy drop (e.g., VGG19: 22.2% vs 17.8%; DeiT: 69.0% vs 66.0%; ViT: 62.9% vs 60.9%). On CIFAR-10, the improvement is often substantial (e.g., VGG19 Square: 62.8% vs 39.8%). The benefit holds across score-based (NES, SignHunt, Square) and decision-based (RayS) attacks.

- **Lightweight, plug-and-play design with minimal accuracy degradation**: The defense introduces no training overhead, requires only adding Gaussian noise to hidden features at inference time, and maintains clean accuracy within 1–2% of the base model across all experiments. It applies to any pre-trained model without expensive adversarial training.

- **Robustness against adaptive EOT attacks and synergy with adversarial training**: Even when attackers average multiple queries to cancel randomness (EOT with M=5,10), the feature defense retains higher robustness than input defense (VGG19 vs Square: 53.0% vs 24.2% at M=5, 1000 queries). The defense also synergizes with adversarial training, boosting robustness from 32.5% (AT alone) to 77.8% (Ours+AT) for Square attack.

## Weaknesses

### Fatal

None.

### Major

- **The main experimental tables do not specify which layers were perturbed for the feature defense, making core results difficult to interpret and reproduce.** Algorithm 1 takes a set of perturbed layers \(H\) as input, and the paper includes a layerwise analysis (Table: "Robustness in CIFAR10 at each layer") showing that effectiveness varies substantially by layer (e.g., VGG Square robustness ranges from 50.6% to 63.0% depending on which single layer is perturbed; ViT ranges from 48.3% to 77.3%). Yet the main experimental results (ImageNet Table 1, CIFAR-10 Table 2) report "Feature" defense without disclosing which layer(s) were used or how \(H\) was selected. Without this information, the reader cannot determine whether the reported benefit comes from adding noise at *any* intermediate layer or from a specific, potentially cherry-picked, choice. The layerwise analysis and the main results need to be explicitly connected — if the same layer(s) were used across all experiments, this should be stated; if different layers were used for different models or datasets, the rationale should be given.

### Minor

- **Theorem 1 is a qualitative correlation result, not a quantitative guarantee, and the abstract overclaims by stating the analysis "confirms" enhanced resilience.** The theorem asserts that the probability of misleading the attacker "positively correlates with" an arctan expression. This provides useful insight into the factors influencing robustness (gradient norm ratio, noise variance ratio) but does not constitute a formal robustness guarantee or a testable quantitative bound. The paper's own discussion of the arctan's boundedness acknowledges saturation behavior but not the limit of what the theorem actually establishes. Toning down the abstract's language from "confirms" to "provides insight into" would better match the result.

- **The decision-based attack analysis is incomplete: the feature defense underperforms input defense on SignFlip, and the paper does not explain why.** For SignFlip on CIFAR-10, the input defense achieves 85.5%/86.0% (ResNet50/VGG19) while the feature defense achieves only 82.5%/76.5%. This discrepancy is not discussed, yet it undermines the generality of the claimed benefit for decision-based attacks. The paper's linearization argument (Section 3.3) predicts that higher variance helps mislead the attacker, but it does not explain why this fails for SignFlip specifically.

- **Assumption 1 (mean of randomized model equals original model) is stated with brief justification ("when variance is small") but no discussion of when it might break down.** For highly non-linear layers with noise of non-trivial variance, this equality will not hold exactly. The assumption is used to argue that adversarial examples for the original model are also adversarial for the randomized model, so a reader would benefit from explicit acknowledgment of the approximation's limitations.

- **No confidence intervals or error bars are reported.** Given that both the defense and several attacks (NES, Square, SignFlip) involve randomness, and only 1,000 images are used per experiment, reporting variability (e.g., standard errors across multiple runs or bootstrap estimates) would strengthen the conclusions without being standard practice in this sub-area.

### Trivial

- The paper refers to a supplementary material ("Full results are provided in the supplementary material," "as seen in Table 3 in Supplementary") that is not present in the reviewed manuscript. While this was likely stripped by the PDF extraction process, the main paper should be self-contained for the key claims.

## Nice-to-Haves

- A wall-time comparison (forward pass cost) between input noise and feature noise would support the "lightweight" claim beyond clean accuracy metrics.
- An empirical validation of how well the linearization in Section 3.3 holds (e.g., cosine similarity between true and linearized gradients) would strengthen the decision-based attack analysis.
- The SignFlip underperformance could be investigated further — is it because SignFlip operates in \(\ell_\infty\) space and the binary search structure interacts differently with feature-level noise?

## Removed Points

- **"The EOT analysis should discuss more sophisticated variance reduction methods"** — Removed: This asks the authors to speculate about future attack methods that do not exist in the literature. The paper already evaluates EOT with multiple averaging budgets, which is the standard adaptive attack.
- **"The NES anomaly (robustness increases with larger perturbation) contradicts the theoretical intuition"** — Removed: The paper explicitly addresses this, attributing it to approximation errors in the attack. This is a reasonable explanation and not a contradiction.
- **"AAA comparison should be in a different context"** — Removed: The paper explains why AAA is included (it is a related defense method; the comparison against decision-based attacks shows AAA fails, which is informative).
- **"The paper should verify individual sentence-level claims"** — Removed: These are sentence-level nitpicks that do not affect the paper's overall argument.
- **"The paper should add more models/datasets"** — Removed: The paper already evaluates 4 architectures on 2 datasets across 5 attacks, which is a reasonable scope.

## Novel Insights

Beyond the paper's own contributions, the most interesting cross-review observation is that the layerwise analysis (Table: "Robustness in CIFAR10 at each layer") contains a tension with the theoretical story that the review system did not fully resolve. The theory predicts that robustness should increase with the gradient norm ratio. For VGG, layer 12 has the highest GradNorm (2.514) and the highest Square robustness (63.0%), consistent with the theory. However, for SignHunt, layer 15 has the highest robustness (37.4%) despite having a lower GradNorm (1.710) than layer 12 (2.514, with 29.4% robustness). This suggests that the relationship between gradient norm and robustness is attack-dependent in ways the current theory does not capture — an observation that could motivate deeper investigation.

## Suggestions

1. **Specify the layer selection protocol explicitly for every main experiment.** State which layer(s) were used for the Feature defense in Tables 1 and 2 (ImageNet and CIFAR-10), and provide a rationale (e.g., the layer that maximizes the gradient-norm ratio, or a fixed depth for all models). Connect the layerwise analysis directly to the main results.
2. **Tone down the abstract's theoretical claim** from "confirms that this method effectively enhances resilience" to something like "provides analytical insight into" or "theoretically motivates," since Theorem 1 establishes a correlation, not a guarantee.
3. **Discuss the SignFlip discrepancy** — why feature noise underperforms input noise for this specific decision-based attack, and whether this is a structural limitation or an artifact of the binary search mechanism.
4. **Add a brief discussion of the limitations of Assumption 1**, noting that it holds approximately for small noise and locally linear behavior but may break down at deeper layers with higher variance.
5. **Report variability** for at least a subset of key results (e.g., standard deviation across 3 runs for one model/attack pair) to help readers gauge the stability of the reported robust accuracies.

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>