Now I have all the information I need. Let me compose the final consolidated review.

## Summary

This paper introduces BAdd, a bias mitigation method that injects bias-capturing features (from a separately trained model or label-based regressor) into the penultimate layer of a classifier during training. The rationale is that by providing bias information directly, the model's main features do not need to encode it, forcing the learned representations to be invariant to the protected attribute. After training, the bias features are discarded and the classification head is fine-tuned. The method is evaluated on seven benchmarks (four single-attribute, three multi-attribute) and achieves competitive to state-of-the-art results, with notable gains on multi-attribute settings (+27.5% on FB-Biased-MNIST, +5.5% on CelebA).

## Strengths

- **Substantial gains on multi-attribute bias benchmarks**: BAdd achieves a +27.5% absolute accuracy improvement over the second-best method (FairKL) on FB-Biased-MNIST at q=0.99 (Table 5: 69.5% vs. 42.0%) and +5.5% on CelebA bias-conflicting samples for the HeavyMakeup attribute (Table 8: 92.7% vs. 87.2%). These are large margins on the exact settings where single-attribute methods collapse, directly validating the paper's central claim.

- **Consistent empirical superiority across diverse settings**: On single-attribute benchmarks, BAdd outperforms or ties state-of-the-art on Biased-MNIST (all four q levels, Table 1), Biased-UTKFace (both race and age bias, Table 2), and Corrupted-CIFAR10 (all four q levels, Table 5), with the Corrupted-CIFAR10 results remarkable given that a simple linear regressor substitutes the bias-capturing classifier.

- **Evidence of feature-level invariance**: The mean pairwise cosine similarity across background variations on Biased-MNIST (Table 4) is near 1 for all q levels (0.973–0.985), while vanilla drops to 0.416 at q=0.999. This is direct evidence that BAdd's representations are actually invariant to the protected attribute, not just improving accuracy through some other mechanism.

- **Ablation studies validating design choices**: The paper systematically compares addition vs. concatenation of bias features (Table 9: addition outperforms by 6.6–55.2 points) and layer depth (Table 10: penultimate layer is best), confirming that the specific design matters.

- **Intuitive and plausible mechanism**: The loss-spike explanation (Figure 2) and gradient analysis (Eqs. 3–4) provide a coherent narrative for why vanilla models get trapped in a bias-reinforcing cycle and how adding bias features breaks it. While not a formal proof, the narrative is grounded in observable phenomena (the spikes) and supported by the empirical results.

## Weaknesses

### Fatal

None.

### Major

- **Ambiguity in how $\mathbf{b}$ is constructed for multiple bias attributes.** The paper's central claim is effectiveness on multi-attribute bias, but the methodology section (Sec. 3) defines $\mathbf{b}$ as the representation from a model that predicts "protected attribute(s) $t$" without specifying how $b(\cdot)$ is designed or trained when $q>1$ attributes are involved. For FB-Biased-MNIST (foreground + background color), the paper does not state whether $b(\cdot)$ is a single multi-label classifier predicting both jointly, two separate classifiers with concatenated outputs, or some other design. For CelebA (Table 8), the table reports WearingLipstick and HeavyMakeup in separate columns — it is unclear whether this means one model was trained with both attributes embedded in $\mathbf{b}$ (and results are then disaggregated per attribute) or whether separate models were trained for each attribute. This ambiguity undermines reproducibility and the evaluation of the claimed multi-attribute capability. The paper should specify the exact architecture and training procedure of $b(\cdot)$ for each multi-attribute dataset.

- **Absence of ablation on the fine-tuning step.** The fine-tuning stage (discarding $\mathbf{b}$ and retraining only the classification head for 20 epochs) is critical: it converts training-time behavior into inference-time fairness. Yet the paper provides no ablation on (a) the number of fine-tuning epochs, (b) whether fine-tuning could reintroduce bias, or (c) what happens if it is omitted entirely. Since the method's final performance depends on this step, the lack of analysis is a notable gap.

### Minor

- **The theoretical justification is intuitive but undersupported.** The gradient analysis (Eqs. 3–4) and the loss-spike argument rely on the assumption that $\mathcal{L}_\mathcal{A} \approx 0$ while $\mathcal{L}_\mathcal{C} \gg 0$, and that adding $\mathbf{b}$ keeps $\sigma_\kappa^{(i)}$ large and $A_0^{(i)}$ small. The claim that "the addition of $\mathbf{b}$ entails invariably large $\sigma_\kappa^{(i)}$" is asserted rather than derived, and the gradient analysis abstracts away the shared dependence of $A_0^{(i)}$ on the classifier weights $\mathbf{W}$. Loss-spike evidence is shown only for Biased-MNIST (Figure 2), not for any other dataset. The paper would benefit from showing that the same dynamics hold on a second dataset (e.g., Biased-UTKFace or CelebA) and from directly measuring the gradient contributions of bias-aligned vs. bias-conflicting samples. That said, the empirical results (cosine similarity, accuracy gains) are the stronger evidence, and the theory is primarily motivational.

- **Missing comparison with multi-attribute methods on FB-Biased-MNIST.** The paper cites OccamNets (shrestha2022occamnets) as a multi-attribute method but does not compare against it on the FB-Biased-MNIST benchmark where BAdd claims its largest gains. On UrbanCars, LLE is compared and BAdd is competitive on BG+CoObj Gap (−3.9 vs. −5.9) and CoObj Gap (−1.6 vs. −2.7) but worse on BG Gap (−4.3 vs. −2.1). A head-to-head comparison against OccamNets on FB-Biased-MNIST would strengthen the multi-attribute claims. This is minor because BAdd already outperforms strong single-attribute methods (FairKL, FLAC, BC-BB) by large margins on that benchmark.

- **Protected attribute labels are required.** As the paper acknowledges (Conclusion), BAdd requires access to protected attribute labels during training. Several competing methods (LM, Rubi, ReBias, LfF, FLAC) do not. This makes the comparison inherently asymmetric (methods that need no labels vs. one that does) and means some of BAdd's gains may come from label availability rather than the core mechanism. This is an honest limitation but worth flagging.

- **The Regressor variant on Corrupted-CIFAR10 is not analyzed.** The paper uses a linear regressor from one-hot texture labels (rather than a trained bias-capturing classifier) for Corrupted-CIFAR10, noting that training a classifier would be complex. This is a pragmatic choice, but the paper does not analyze how the quality or capacity of the regressor bounds the method's performance, nor whether a trained classifier would improve results further.

### Trivial

None.

## Nice-to-Haves

- Show loss-spike plots for at least one additional dataset (e.g., Biased-UTKFace or CelebA) to demonstrate the mechanism generalizes.
- Provide an ablation where the quality of $\mathbf{b}$ is varied (e.g., using a deliberately under-trained or lower-capacity bias classifier) to test robustness.
- Ablate the fine-tuning step: vary epoch count, test omission, verify bias is not re-introduced.

## Removed Points

- **"Figure 1 (teaser) is referenced but not provided in the text"**: This is a parser artifact (figures are typically stripped from text-only PDF extraction). Not an author error.
- **The framing of the theoretical gap as a "critical issue"**: The reviewer called this a critical/structural flaw. Upon verification, the theoretical explanation is intuitive and coherent; it is not a formal proof but is supported by substantial empirical evidence (loss spikes, cosine similarity, accuracy gains across 7 benchmarks). This is a minor weakness, not fatal.
- **"The paper's performance is bounded by how well a simple regressor can encode the bias — an unremarked source of variation"**: The paper explicitly remarks that it uses a linear regressor (Section 4, paragraph on Corrupted-CIFAR10). The concern about lack of analysis of regressor quality is real and retained in Minor, but the framing "unremarked" is inaccurate.

## Novel Insights

The most interesting dynamic the reviews surface is the tension between the paper's simple, elegant mechanism (add bias features → prevent bias encoding in main features → fine-tune) and the under-specification of exactly how that mechanism plays out when biases are heterogeneous (e.g., foreground color + background color = two unrelated visual biases). The reviews collectively expose that the paper's strongest claim — multi-attribute capability — rests on the least documented design decision: how $b(\cdot)$ is constructed for $q>1$. The core insight that the reviews do not contradict but rather refine is that BAdd's simplicity is both its strength (easy to implement, strong results) and its weakest documentation point (the multi-attribute $\mathbf{b}$ construction is underspecified). Beyond the paper's own contributions, the reviews confirm that the field would benefit from a clearer taxonomy of multi-attribute bias mitigation strategies (joint prediction vs. separate per-attribute features vs. ensemble) to make comparisons more systematic.

## Suggestions

1. **Clarify $\mathbf{b}$ construction for multi-attribute cases** in a dedicated paragraph or table: specify architecture, training data, output dimensionality, and whether attributes are predicted jointly or separately for each multi-attribute dataset (FB-Biased-MNIST, UrbanCars, CelebA).
2. **Add an ablation for the fine-tuning step**: show results with 0, 10, 20, 50 fine-tuning epochs, and check whether bias-conflicting accuracy degrades if fine-tuning is too long.
3. **Add loss-spike plots for a second dataset** (e.g., Biased-UTKFace) to demonstrate that the claimed mechanism is not dataset-specific.
4. **Compare against OccamNets** on FB-Biased-MNIST, or explicitly state why it cannot be compared (e.g., architecture incompatibility).
5. **Report the accuracy of the bias-capturing classifier** for each dataset and show how it correlates with BAdd's final performance.

## Score and Decision

The paper introduces a simple, effective method that delivers strong empirical results across seven benchmarks, with particularly impressive gains on multi-attribute settings where prior work struggles. The core idea is novel and the ablations validate the design choices. The main weaknesses are documentation gaps (multi-attribute $\mathbf{b}$ construction, fine-tuning ablation) rather than fundamental flaws. These are addressable in a revision and do not invalidate the paper's contribution. The paper makes a solid contribution to the bias mitigation literature.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>