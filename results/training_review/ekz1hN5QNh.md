Now I have a thorough understanding of the paper. Let me compose the final consolidated review.

---

## Summary

This paper introduces HCNN, a fully hyperbolic convolutional neural network framework in the Lorentz model, with novel formulations of the 2D convolutional layer, batch normalization using the Lorentzian centroid, and multinomial logistic regression via explicit hyperplane distance. The authors demonstrate that their components can be used to build hybrid (HECNN) and fully hyperbolic (HCNN) ResNet and VAE architectures, showing improved performance over Euclidean and Poincaré baselines on image classification and generation tasks, particularly under adversarial attacks and low-dimensional settings.

## Strengths

- **First fully hyperbolic CNN encoder in computer vision.** The paper provides a complete Lorentz-model framework (convolution, batch norm, MLR, residual connections, activations) that replaces every Euclidean CNN component, addressing a genuine gap — prior vision HNNs all used Euclidean encoders. Evidence: Sections 4.1–4.4; the paper explicitly contrasts with concurrent Poincaré CNN (van Spengler et al., 2023) that also goes fully hyperbolic but in a different model.

- **Novel Lorentz MLR with explicit closed-form hyperplane distance.** Theorems 1 and 2 derive the distance from a Lorentz point to a geodesic hyperplane and use it to formulate an MLR classifier. This is mathematically rigorous, directly comparable to the Poincaré MLR in prior work, and reusable by other researchers. Evidence: Section 4.3, Equations 8–13.

- **Efficient, geometrically grounded Lorentz batch normalization.** The proposed LBN uses the closed-form Lorentzian centroid (avoiding slow iterative Fréchet mean) and parallel-transport-based re-scaling along straight geodesics at the origin. The description is clear enough to implement, and the efficiency advantage over prior Riemannian BN (Lou et al., 2020) is well-motivated. Evidence: Section 4.2, Equations 2–3.

- **Consistent and sometimes sizable gains in adversarial robustness.** Under FGSM and PGD attacks on CIFAR-100, HCNN achieves up to ~5% accuracy improvement over the Euclidean baseline (e.g., 31.77% vs. 26.30% under PGD with ε=3.2/255) — the strongest empirical signal in the paper. Evidence: Table 2, lines 228–248.

- **Strong low-dimensional performance.** At 8D embeddings on CIFAR-100, HECNN and HCNN maintain substantially higher accuracy than Euclidean and Poincaré models, validating the core motivation that hyperbolic space excels at compact representations. Evidence: Figure 3, lines 312–314.

## Weaknesses

### Fatal
None.

### Major

1. **HECNN consistently outperforms HCNN, undermining the "fully hyperbolic" framing.** On every classification dataset (Table 1), the hybrid encoder HECNN beats the fully hyperbolic HCNN (78.76 vs. 78.07 on CIFAR-100; 65.96 vs. 65.71 on Tiny-ImageNet). In the low-embedding experiment (Figure 3), HECNN also matches or exceeds HCNN at most dimensionalities. The paper acknowledges this ("contrary to our hypothesis," "unexpected") but offers no deeper analysis of *why* — e.g., whether the residual connection heuristic accumulates errors in deeper hyperbolic layers, whether early vision features are ill-suited to hyperbolic geometry, or whether numerical instability compounds. Without resolving or at least analyzing this tension, the paper's headline narrative ("fully hyperbolic" as the ideal) is unsupported by its own evidence, and the actual contribution (the hybrid encoder) is downplayed.

2. **Generation results are incomplete and the paper overclaims.** Table 3 compares HCNN-VAE against hybrid (Euclidean encoder + hyperbolic latent) VAEs, but omits an HECNN-VAE baseline. Since classification shows HECNN often outperforms HCNN, the absence of this comparison means one cannot attribute the generation improvements to the fully hyperbolic encoder specifically. Moreover, the paper claims HCNN-VAE "outperforms all baselines" (line 322), yet on CIFAR-100 Gen FID, HCNN-VAE scores **100.27**, which is *worse* than both hybrid Poincaré (98.19) and hybrid Lorentz (98.34). This overstatement weakens credibility.

3. **The residual connection and activation functions are geometric heuristics, not principled hyperbolic operations.** The residual connection (Section 4.4) simply adds space components and recomputes the time component from the norm — the paper admits this is chosen for best empirical performance. The activation applies ReLU to the space component and reconstructs the time component from the norm. Neither operation respects the Lorentzian geodesic structure or isometry. While pragmatic, this undermines the claim of operating "fully" in hyperbolic space and would benefit from analysis comparing against more principled alternatives (e.g., tangent-space residual connections).

### Minor

1. **The LFC (Lorentz Fully Connected) layer in Equation 3 is not defined in the paper.** The paper states it is "similar to Chen et al. 2021" and "does not use normalization." However, since this is a core component of the proposed convolutional layer, the paper would benefit from a brief self-contained description (e.g., how the kernel lives in tangent space vs. on the manifold, how matrix multiplication respects the Lorentz constraint). As written, a reader needs Chen et al. 2021 on hand to fully understand the method.

2. **No ablation study isolating individual components.** The paper does not show what happens when each proposed module (Lorentz conv, LBN, Lorentz MLR, hyperbolic residual) is replaced with its Euclidean counterpart while keeping others fixed. Without this, it is unclear which component drives the modest improvements (~1% classification, a few FID points).

3. **Hyperparameters inherited from Euclidean training may disadvantage hyperbolic models.** The paper adopts the training procedure and hyperparameters of `resnetHyp` (optimized for Euclidean ResNets) for all models. While this is a reasonable choice for fairness, it leaves open the possibility that hyperbolic models would benefit from different hyperparameters (learning rate, optimizer settings, weight decay). The Poincaré baselines performing substantially worse than Euclidean (e.g., 62.01% vs. 65.19% on Tiny-ImageNet) may partly reflect this mismatch rather than inherent limitations of the Poincaré model.

4. **Mixed generation results on CIFAR-100 Gen FID not discussed.** As noted above, HCNN-VAE is worse than both hybrid baselines on CIFAR-100 Gen FID but better on other datasets. The paper does not discuss this discrepancy, which could point to meaningful limitations of the fully hyperbolic approach on certain data distributions.

### Trivial

None.

## Nice-to-Haves

- Reporting training time and memory usage for hyperbolic models vs. Euclidean, since the paper acknowledges "computational overhead" but provides no measurements.
- Including HECNN-VAE in the generation experiment to allow attribution of encoder vs. decoder effects.
- Visualizing learned convolutional filters or their effect on feature-space geometry.
- A runtime comparison showing that the closed-form Lorentzian centroid is indeed faster than iterative Fréchet mean for batch normalization.

## Removed Points

These points were flagged by the reviewers but are removed or weakened upon verification against the paper:

- **"LFC is completely underspecified — core method irreproducible"** (Harsh Critic #2): The paper cites Chen et al. 2021 for the LFC definition, which is standard practice. The paper's novelty lies in the 2D convolutional framework (HCat, padding with origin vectors, channel-last time-component design), not in re-inventing the Lorentz fully-connected layer from scratch. This is a minor citation-gap, not a structural flaw. Moved to Minor tier above.

- **"Poincaré baselines are weak / unfair comparison"** (Harsh Critic #3): The paper uses the same training procedure for all models. The Poincaré baselines being worse than Euclidean is consistent with the literature the paper cites (Guo et al., 2022). The shared hyperparameter concern is valid but acknowledged by the paper, and is a common tradeoff in fair-comparison setups. Moved to Minor tier above.

- **"Core claim contradicted by own evidence"** as a fatal flaw: The paper *does* acknowledge the hybrid outperforming the fully hyperbolic model (lines 202, 314) and discusses it. However, the lack of analysis of *why* remains a genuine weakness. Moved to Major #1 above, appropriately contextualized.

- **Strength Finder's "consistent empirical gains across tasks and settings"** (as a major strength): The gains are modest (~1% classification, mixed generation results) and the hybrid outperforms the fully hyperbolic model. This strength is retained in a substantially weakened form in the adversarial robustness bullet.

## Novel Insights

The cross-review synthesis reveals that the paper's most compelling empirical signal is adversarial robustness (up to ~5% improvement), not standard classification (~1%). This is interesting because adversarial vulnerability is often linked to linearity in Euclidean representations — hyperbolic curvature might naturally provide a form of "manifold-based" protection. The paper's own results suggest the community should reframe the contribution: the Lorentz components themselves are a genuine technical contribution (MLR, LBN), but the strongest case for *full* hyperbolicity (HCNN) is adversarial defense, while standard classification favors the hybrid (HECNN). This tension — that different tasks benefit from different depths of hyperbolic integration — is more interesting than the paper's current framing allows, and future work could productively investigate *where* in the network hyperbolic geometry helps and where it hurts.

## Suggestions

1. **Reframe the paper's contributions honestly.** The hybrid encoder HECNN is your strongest performer on classification. Lead with that, present HCNN as a proof-of-concept for a fully hyperbolic encoder with complementary strengths (adversarial robustness, low-dimensional embeddings), and analyze why HECNN outperforms HCNN. This would resolve the central tension and make the paper more compelling.

2. **Add an ablation study** replacing each Lorentz component with its Euclidean counterpart one at a time. This is the minimum experiment needed to understand which component drives improvements.

3. **Complete the generation experiment** by adding HECNN-VAE results. Without this, the reader cannot attribute FID improvements to the encoder hyperbolicity vs. some other factor.

4. **Discuss the CIFAR-100 Gen FID result** where HCNN-VAE is worse than hybrid baselines, rather than claiming it "outperforms all baselines."

5. **Provide a brief self-contained description of LFC** — even a sentence specifying whether the kernel lives in tangent space or on the manifold would significantly improve reproducibility.

## Score and Decision

The paper makes genuine technical contributions (Lorentz MLR derivation, centroid-based batch normalization, first fully hyperbolic vision encoder framework) that advance the state of the art in hyperbolic neural networks. However, the paper's central narrative is misaligned with its own evidence: the hybrid encoder consistently outperforms the fully hyperbolic model, the generation results are incomplete, and an overclaim in the VAE results undermines trust. The paper would be significantly stronger with an honest reframing, one additional experiment (HECNN-VAE), and an ablation study. As submitted, these issues prevent the paper from establishing its stated contribution convincingly.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>