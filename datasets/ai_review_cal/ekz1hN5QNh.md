- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper introduces HCNN, a fully hyperbolic CNN operating in the Lorentz model, with novel formulations of 2D convolution, batch normalization (using a closed-form centroid rather than iterative Fréchet mean), and multinomial logistic regression — components previously missing for Lorentz-based vision architectures. The authors evaluate both a hybrid encoder variant (HECNN) and a fully hyperbolic variant (HCNN) on image classification (ResNet-18) and VAE-based image generation, comparing against Euclidean, hybrid Poincaré, and Lorentz baselines. The paper makes a genuine mathematical contribution by completing the Lorentz CNN toolkit, and the hybrid encoder variant delivers consistent improvements on several tasks.

---

## Strengths

1. **Novel Lorentz formulations for three missing CNN components**: Sections 4.1–4.3 derive Lorentz-model equivalents of 2D convolution, batch normalization, and multinomial logistic regression. The batch normalization uses a closed-form Lorentzian centroid (Eq. 8) instead of the slow iterative Fréchet mean of prior Riemannian BN, and the MLR (Theorem 2, Eq. 12) provides a mathematically grounded classifier. These are concrete, verifiable technical contributions that extend the toolkit for hyperbolic neural networks in vision.

2. **Adversarial robustness improvements**: On CIFAR-100, HCNN achieves 31.77% accuracy under PGD attack (ε=3.2/255) versus 26.30% for Euclidean and 23.78% for Hybrid Poincaré (Table 2) — a relative improvement of over 5 percentage points. This is the most clear-cut quantitative advantage and is robust across perturbation levels.

3. **Strong low-dimensional performance**: Figure 3 shows that at 8-dimensional embeddings, HECNN/HCNN substantially outperform Euclidean and hybrid baselines on CIFAR-100. This validates the central motivation that hyperbolic geometry excels in low-dimensional regimes and provides a practical path toward smaller models.

4. **First fully hyperbolic encoder architecture in computer vision**: The paper is explicit (Section 2) that prior vision HNNs use hyperbolic heads on Euclidean backbones, while HCNN is the first work to learn features in hyperbolic space throughout the encoder. This fills a gap acknowledged in the literature.

5. **Efficient batch normalization design**: Section 4.2's Lorentz BN avoids iterative Fréchet mean computation used in prior Riemannian BN by leveraging the closed-form Lorentzian centroid and parallel-transport-based re-scaling through the origin's tangent space (Eq. 10). This is a concrete algorithmic improvement.

6. **Latent embedding analysis with qualitative evidence**: Figure 4 shows that HCNN-VAE produces curved clusters with consistent distances from the origin in latent space, visually distinct from the radial clusters of hybrid/Euclidean VAEs — providing evidence that the fully hyperbolic architecture qualitatively changes feature representations.

---

## Weaknesses

### Fatal
None.

### Major

1. **The fully hyperbolic model (HCNN) does not outperform the hybrid encoder (HECNN) in classification, creating a framing mismatch.**  
   Table 1 shows HECNN consistently beats HCNN across all three datasets (e.g., CIFAR-100: 78.76% vs 78.07%; Tiny-ImageNet: 65.96% vs 65.71%). The paper acknowledges this ("we also notice that the hybrid encoder model outperforms the fully hyperbolic model" at line 202) and even calls it "unexpected" (line 314). However, the paper's title, abstract, and overall narrative center the *fully* hyperbolic model as the primary contribution while HECNN — a partial application of the same Lorentz components — empirically works better. This disconnect between framing and evidence is a coherence problem. The paper would be stronger if it either recentered its claims around the hybrid encoder or provided a more compelling case for why the fully hyperbolic variant is valuable despite being empirically weaker on classification.

2. **Overstatement in generation results.**  
   The paper claims (line 322) that "our HCNN-VAE outperforms all baselines." However, Table 2 shows that on CIFAR-100 *Generation* FID, Hybrid Poincaré (98.19) is better than HCNN (100.27). While HCNN leads on 5 of 6 metrics, the "outperforms all" claim is technically false. This overstatement weakens the paper's credibility and should be corrected.

### Minor

3. **Hyperparameters optimized for Euclidean models, disadvantaging the Poincaré baseline.**  
   The paper states (line 200) that all models use hyperparameters "optimized for Euclidean CNNs." This is transparent but creates an unlevel comparison, particularly for the Poincaré ResNet baseline (van Spengler 2023), which performs dramatically worse (62.01% vs 65.19% on Tiny-ImageNet). While the Lorentz model may genuinely be more stable, the current comparison is not diagnostic of geometry — it is confounded by hyperparameter choice. A sensitivity study or per-model tuning search on a small dataset would substantially strengthen this comparison.

4. **No runtime or memory analysis.**  
   The paper mentions reducing computational cost by using 32-bit arithmetic (line 46) and acknowledges "computational overhead" (line 379), but provides no FLOPs, parameter counts, or wall-time comparisons. Given that hyperbolic operations (exponential/logarithmic maps, parallel transport) add nontrivial computational cost, this omission makes it difficult to assess the practical viability of the approach.

5. **Lorentz batch normalization uses scalar Fréchet variance rather than per-channel scaling.**  
   Unlike Euclidean BN which applies learnable per-dimension scaling (γ), the proposed LBN (Eq. 10) uses a single scalar Fréchet variance for re-scaling. This is a substantive architectural difference that is not discussed as a potential limitation or ablative dimension. It may partially explain the model's modest gains and merits an experimental comparison against a hypothetical per-channel variant.

### Trivial

6. **Minor imprecision in generation text**: As noted in weakness 2, the "outperforms all baselines" claim (line 322) is contradicted by CIFAR-100 Gen FID results. This should qualify exceptions explicitly.

---

## Nice-to-Haves

- **Zero-curvature limit of Lorentz MLR**: The logit formula (Eq. 12) is derived by analogy with the Euclidean MLR template (Eq. 7). A brief demonstration that the Lorentz MLR reduces to Euclidean MLR as curvature K→0 would improve theoretical grounding.
- **Statistical significance tests**: The standard deviations from five runs are reported and small, but formal significance testing (e.g., bootstrapped confidence intervals or paired comparisons across seeds) would strengthen claims about non-overlapping differences.
- **Residual connection analysis**: The paper's residual connection (averaging space components, recomputing time) is a heuristic. The paper states it provides the best empirical performance among several alternatives (line 179), but a brief theoretical comment on how this affects the manifold structure would be welcome.

---

## Removed Points

*These points were identified by the reviewers but are removed from the main review for the following reasons. Treat them with caution.*

- **"Table 2 rec./gen. FID labels are ambiguous"** — Removed as factually incorrect. The table clearly labels "Rec. FID" and "Gen. FID" and the caption states "Reconstruction and generation FID." The criticism misreads the table.
- **"Figure 3 x-axis confusing"** — Removed. The x-axis label "Embedding dimensions" with ticks 8,16,32,128,512 is consistent and correct (these are the embedding dimensionalities tested).
- **"No comparison against modern architectures (ResNet-50, WRN, ViT)"** — Removed as scope creep. The paper uses ResNet-18, a standard baseline for hyperbolic vision research, and its contribution is foundational (providing components) rather than SOTA-chasing.
- **"Limited task scope (no detection/segmentation)"** — Removed as scope creep. The paper introduces missing Lorentz components and validates them on standard tasks; extending to detection/segmentation is future work.
- **"MLR logit formula given without derivation"** — Removed. The paper provides Theorem 1 (distance to hyperplane) and Theorem 2 (logit formula), with the mapping from distance to logit following the Euclidean template of Eq. 7. The derivation chain is present.
- **"Residual connection breaks Lorentz structure"** — Moved to Nice-to-Have. The paper acknowledges this design choice and provides empirical justification (best among alternatives, line 179). It is not a flaw but a design trade-off.
- **Strength Finder's "statistically significant" claim** — Removed from strengths. The paper does not run formal significance tests; overlapping standard deviations exist on some comparisons (CIFAR-100). The observation of small stds is kept, but the "significant" label is the reviewer's inference, not the paper's.

---

## Novel Insights

None beyond the paper's own contributions. The reviews do not surface a genuinely novel observation about the paper that the paper itself does not already state or imply.

---

## Suggestions

1. **Reframe the contribution to match the evidence.** The hybrid encoder HECNN consistently outperforms HCNN. Either recenter the paper's narrative around HECNN with HCNN as a special case, or provide stronger justification for why the fully hyperbolic variant matters despite weaker classification results.
2. **Correct the generation overstatement.** Qualify the "outperforms all baselines" claim to acknowledge the CIFAR-100 Gen FID exception.
3. **Add a hyperparameter sensitivity study.** On one dataset (e.g., CIFAR-100 or a subset), perform a small grid search for each model variant to show that the Lorentz advantage is not an artifact of untuned baselines.
4. **Report FLOPs, parameter counts, and wall-time** for at least one configuration to contextualize the computational overhead.
5. **Add an ablation of batch normalization design** comparing scalar Fréchet variance against a per-channel variant to understand whether the uniform scaling limits performance.
6. **Consider formal significance tests** (e.g., paired bootstrap across seeds) to quantify confidence in the reported improvements.

---
