Now I have a complete understanding of the paper. Let me synthesize the final review.

## Summary

The paper proposes WePe (Weight Perturbation), a training-free method for detecting AI-generated images by measuring predictive uncertainty via weight perturbation in DINOv2. The key idea is that models trained only on natural images treat generated images as OOD, exhibiting higher sensitivity to weight perturbations. For a test image, features are extracted from the original model and from models with perturbed weights; the average cosine similarity between them serves as the detection score—high similarity indicates natural, low similarity indicates generated. Experiments across ImageNet, LSUN-BEDROOM, and GenImage benchmarks show state-of-the-art performance, particularly notable in generalization to unseen generators on GenImage where WePe achieves 90.60% accuracy on VQDM while training-based methods collapse to near-random.

## Strengths

- **Strong generalization to unseen generators without training**: On the GenImage benchmark (Table 3), WePe achieves 81.27% average accuracy, outperforming all training-based methods including LaRE (77.91%) that were trained on SD V1.4. Most strikingly, on the unseen VQDM generator, training-based methods collapse to near-random performance (~50%), while WePe achieves 90.60%. This directly demonstrates the practical value of the training-free OOD framing.

- **Multiple perturbation types all work effectively**: Table 5 shows that Gaussian (87.99 AUROC), Uniform (89.06), and Laplace (87.13) noise all yield strong performance, consistently outperforming MC Dropout (81.63). This indicates the detection signal is not brittle with respect to the specific noise distribution, a useful robustness property.

- **Robustness to common image degradations**: Figure 6 shows WePe maintains superior performance under JPEG compression, Gaussian blur, and Gaussian noise compared to both training-based and training-free baselines, which is critical for real-world deployment.

- **Clear empirical validation of the core hypothesis**: Figure 2 directly demonstrates that a moderate weight perturbation preserves features for natural images but disrupts features for generated images, providing visual and quantitative evidence for the differential sensitivity property underlying the method.

## Weaknesses

### Fatal

None.

### Major

- **The mathematical derivation in Section 3.3 does not rigorously support the "upper bound" claim**: The derivation from Eq. 2 to Eq. 3 relies on a critical "unbiased assumption" that $\mathbb{E}_{\theta_j}[f(\mathbf{x};\theta_j)] \approx f(\mathbf{x};\theta)$, which is neither proven nor empirically validated for nonlinear models with additive weight noise. Furthermore, the application of the Cauchy-Schwarz inequality to arrive at the bound is presented without explicitly stating it. The paper frames this as a "principled uncertainty-based framework" but the derivation does not hold up to scrutiny — the actual operational method is simply the average cosine similarity between features from the original and perturbed models (the final line of Eq. 3). The paper does acknowledge in the Limitations section (line 430) and in Section 3.4 (line 122) that it "does not directly prove this theoretically," which partially mitigates this concern, but the paper still presents Eq. 3 as an upper bound in its derivation, which is a claim the derivation does not establish. The contribution narrows from "principled uncertainty framework" to "empirical heuristic of weight perturbation feature stability" — a weaker but still valid claim.

- **Insufficient differentiation from RIGID**: RIGID adds noise to input images and measures feature change in DINOv2; WePe adds noise to model weights and measures feature change in DINOv2. Both exploit differential robustness of real vs. generated images to perturbations in a foundation model's representation space, both are training-free. The experimental improvements over RIGID are moderate (e.g., 87.99 vs 83.58 average AUROC on ImageNet; 88.01 vs 85.20 on LSUN; 81.27 vs 78.19 on GenImage). Crucially, there is no per-image analysis showing which images RIGID gets wrong that WePe gets right (or whether the signals are highly correlated), which would be essential for establishing that weight perturbation captures something genuinely different from input perturbation. Without this, the novelty of the mechanism remains questionable.

### Minor

- **ViT-g/14 underperformance is unexplained and contradicts the stated hypothesis**: Table 4 shows DINOv2 ViT-g/14 (84.92 AUROC) performs *worse* than ViT-L/14 (87.99), yet the paper explains poorer small-model performance by saying "larger models can better capture the differences between real and fake images" (line 376). The ViT-g/14 anomaly directly contradicts this explanation and is not discussed. Possible reasons (e.g., different perturbation scale needed, overfitting of larger model) would be valuable to explore.

- **The core OOD assumption lacks quantitative validation**: The paper treats generated images as OOD for DINOv2 based only on the t-SNE visualization in Figure 1, which is a qualitative tool on a narrow slice of data (birds, cats, boats). No standard OOD metrics (MSP, Energy, Mahalanobis distance) are reported to quantitatively verify this assumption. While Figure 2 provides empirical evidence for differential sensitivity, establishing whether the OOD framing is actually the correct explanation vs. an alternative (e.g., generated images have different low-level artifacts) would strengthen the paper.

### Trivial

None.

## Nice-to-Haves

- Per-image scatter plot comparing WePe scores vs. RIGID scores to assess whether the methods capture the same or different signals.
- Quantitative OOD analysis correlating standard OOD scores with WePe detection performance.
- Error analysis showing which generators or image types WePe performs worst on, to understand when the OOD assumption may break down.
- Empirical verification of the "unbiased assumption" — checking whether the mean of perturbed features actually converges to the unperturbed feature.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"Generated images may not be OOD for DINOv2 since diffusion models may be trained on overlapping data"** — This is speculative and the paper's empirical results already demonstrate the method works across multiple generators and benchmarks. If the overlap were large enough to invalidate the approach, this would show up in the results. The paper also acknowledges the OOD assumption in its Limitations section.

- **"Human analogy is misleading"** — The critic misreads the analogy. The paper's point is precisely that humans, like models trained on natural data, can distinguish generated images without explicit training on the distinction — which is the exact setup WePe uses. This is consistent, not contradictory.

- **"GenImage baseline results from other papers are unreliable"** — Cross-paper comparison without re-implementation is standard practice in the field, especially for large datasets. The paper explicitly states this limitation. This is not a substantive weakness.

- **"No error bars in main tables"** — The paper states variance is reported in Figure multi_forward (which appears to be in the appendix). Reporting variance across seeds in a supplementary figure is standard practice. This is a nitpick.

- **"Performance drops at extreme noise levels, so 'robust' is misleading"** — No reasonable reader would interpret "robust to noise level" as meaning performance is constant across all noise levels, including degenerate extremes where features are identical or completely destroyed. The paper's characterization is reasonable.

- **"Perturbing high layers corrupting real images conflicts with the OOD hypothesis"** — This is speculative. High-layer features in ViT models may encode natural-image-specific statistics that are preferentially disrupted for ID samples. Without evidence either way, this is not a confirmed contradiction.

- **Strength Finder's claim about "principled derivation enabling efficient computation"** — Conflicts with the verified weakness about the invalid derivation. Removed from strengths.

- **Strength Finder's generic claim "this paper addressed an important problem"** — Superficial, removed.

## Novel Insights

The most interesting tension in this work is that weight perturbation and input perturbation (RIGID) appear to exploit the same fundamental property — differential feature robustness in a foundation model — but through different entry points (model weights vs. input pixels). The key unresolved question is whether these two entry points capture genuinely different information or merely two paths to the same signal. If the signals are highly correlated, the contribution becomes incremental; if they capture complementary failure modes, an ensemble could substantially outperform either alone. The paper misses the opportunity to resolve this, which would be far more informative than aggregate AUROC comparisons.

## Suggestions

- Either prove the upper bound in Eq. 3 rigorously (addressing the unbiased assumption) or reframe Section 3.3 as motivated by (rather than derived from) uncertainty estimation. The current presentation claims rigor it does not deliver, and straightforwardly acknowledging the method as an empirically motivated heuristic would be more honest and still publishable.
- Add a per-image comparison between WePe and RIGID scores (scatter plot, correlation analysis) to establish whether weight perturbation captures information beyond input perturbation. This single analysis would clarify the degree of novelty.

## Score and Decision

The paper makes a genuine and valuable contribution: a training-free detector that generalizes well to unseen generators, with clear empirical validation. However, the mathematical framework claimed as "principled" doesn't hold up to scrutiny, and the relationship to RIGID remains insufficiently analyzed, which weakens the novelty claim since both methods exploit essentially the same phenomenon through different perturbation entry points. The core empirical contribution is real but incremental relative to RIGID, and the theoretical packaging overclaims.

Originality: Moderate — weight perturbation for detection is a twist on RIGID's input perturbation, but the similarity is high. Importance: High — the generalization to unseen generators is a real practical need. Claims support: Partially — empirical results are strong but the theoretical claim is not justified. Experiment soundness: Good — comprehensive benchmarks, multiple ablation studies. Clarity: Adequate — the mathematical derivation section misleads. Value: Moderate — useful training-free detector, but novelty gap with RIGID needs more evidence.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>