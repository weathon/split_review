Now I have a thorough understanding of the paper. Let me produce the final consolidated review.

---

## Summary

This paper proposes aligning the distributions of continuous feature vectors and code vectors in vector quantization (VQ) using the quadratic Wasserstein distance (under a Gaussian hypothesis). The authors introduce a criterion triple (quantization error, codebook utilization, codebook perplexity) to frame VQ as a distribution-matching problem, provide theoretical results on optimal codebook support and density, and validate the approach with synthetic experiments, a controlled comparison against VQ variants, and image-reconstruction results on FFHQ and ImageNet-1K. The paper identifies a genuine problem (codebook collapse and training instability) and offers a clean, principled angle for addressing it.

## Strengths

1. **Novel distributional perspective on VQ problems.** The paper reframes training instability and codebook collapse as manifestations of distribution mismatch between features and code vectors (Section 2). This reframing is conceptually clean, provides interpretability, and is well-motivated by the synthetic examples in Figure 3.

2. **Principled evaluation via the criterion triple.** The three criteria — quantization error \( \mathcal{E} \), codebook utilization \( \mathcal{U} \), and codebook perplexity \( \mathcal{C} \) — are simple, interpretable, and jointly capture the two core VQ pathologies. The paper uses them consistently throughout synthetic and controlled experiments to build its case (Sections 2.2–2.3, Figure 4).

3. **Own theoretical contribution (Theorem 1).** Theorem 1 proves that support matching between feature and codebook distributions is necessary and sufficient for asymptotic full utilization and vanishing quantization error. This is the paper's own result and provides a principled foundation for the distribution-matching approach.

4. **Computationally efficient closed-form objective.** Lemma 3 (Olkin & Pukelsheim, 1982) gives the quadratic Wasserstein distance between two Gaussians in closed form. The paper leverages this to define a tractable loss \( \mathcal{L}_{\mathcal{W}} \) (Equation 4), avoiding expensive distribution-matching alternatives (Section 3.1).

5. **Empirical robustness in controlled comparisons.** In the controlled Gaussian experiment (Section 3.2, Figure 5), Wasserstein VQ maintains optimal criterion values across a wide range of distribution shifts (\( \mu \)), whereas VQ+Linear degrades sharply for \( \mu \ge 4 \). This demonstrates a concrete advantage over an existing approach.

## Weaknesses

### Fatal
None.

### Major

1. **Critically incomplete experimental presentation.** The main empirical evidence (Tables 1 and 2) is presented with essentially no discussion, analysis, or context. The paper states one sentence that Wasserstein VQ "outperforms all alternative methods" and mentions 100% codebook utilization, but provides none of the following: (a) hyperparameter values (\( \alpha_1, \alpha_2, \alpha_3 \), learning rate, optimizer, batch size, number of training steps), (b) codebook sizes used in the main experiments, (c) standard deviations or multiple seeds, (d) training/inference time or computational cost. Without these, the reported results cannot be reproduced, compared on equal footing, or properly evaluated. This is not a minor omission — the experimental section lacks nearly every standard detail needed to assess a new method.

2. **Missing ablation that directly tests the core claim.** The paper states (line 260, garbled fragment) that the method "with Wasserstein term (\( \alpha_3 > 0 \)) consistently outperforms the VQ algorithm without this term (\( \alpha_3 = 0.0 \))." However, this comparison is not presented in any table, figure, or quantitative result. Since the Wasserstein loss is the paper's primary contribution, an ablation that isolates its effect — showing its impact on reconstruction metrics, utilization, and perplexity — is **necessary** to validate the central claim. Its absence is a critical gap.

3. **Generation experiments missing despite the paper's framing.** The abstract and introduction repeatedly tie VQ to autoregressive visual generation ("The success of autoregressive visual generative models hinges on the effectiveness of vector quantization"). The paper's conclusion acknowledges this gap ("due to limited GPU resources, we were unable to conduct image generation experiments"). While the paper can scope its validation to reconstruction, the framing raises expectations that the method improves generative modeling. Reconstruction quality alone does not guarantee that the learned tokens are suitable for autoregressive modeling (e.g., they could be overly correlated or lack coverage). This mismatch between motivation and evaluation weakens the paper's overall contribution.

4. **Gaussian assumption not examined.** The method assumes feature and codebook distributions are Gaussian to obtain a closed-form Wasserstein distance, but the paper provides no analysis of whether this assumption holds for real VQ features, nor does it test sensitivity to violations (e.g., by comparing with non-parametric alternatives or evaluating on features known to be non-Gaussian). The theoretical section (Theorems 1 and 2) motivates distribution matching in general but does not specifically justify the Gaussian assumption or the Wasserstein distance over other distribution-matching objectives.

### Minor

1. **No analysis of computational overhead.** Estimating the sample mean and \( d \times d \) covariance matrix and computing \( \widehat{\Sigma}_1^{1/2} \) and its matrix square root has non-trivial cost, especially with large feature dimensions and per-batch estimation. The paper does not report wall-clock time, memory usage, or scaling behavior.

2. **Synthetic experiments are illustrative but limited.** The Gaussian experiments in Sections 2.3 and 3.2 provide intuition, but they use fixed, known distributions. Real VQ training involves complex, dynamically evolving feature distributions. The paper acknowledges this limitation but then extrapolates from these simplified settings to claim real-world superiority.

3. **Tables 1 and 2 are images with no visible numbers in the text.** While this is a parser artifact, the paper's text should include a proper written summary of key numbers (e.g., "Wasserstein VQ achieves rFID X vs Y for baseline Z") rather than relying entirely on figures. The single sentence of analysis is insufficient for a results section.

### Trivial
None.

## Nice-to-Haves
- A comparison with alternative distribution-matching objectives (e.g., KL divergence with variational approximations, Sinkhorn distance) would help justify the Wasserstein choice beyond computational convenience.
- Reporting the effect of the Wasserstein loss during training (e.g., how utilization evolves over iterations with and without \( \mathcal{L}_{\mathcal{W}} \)) would strengthen the narrative.
- A discussion of how the empirical covariance estimates are computed (per-batch, running average, or over the full dataset) would clarify the practical implementation.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The theoretical analysis does not directly support the proposed method"** — While Theorem 2 is cited from Graf & Luschgy (2000), Theorem 1 is the paper's own result showing that support matching is necessary for optimal VQ. This does provide direct theoretical support for distribution matching, though not specifically for the Wasserstein formulation. The critique overstates the weakness. Keeping the reasonable kernel: the gap between Theorems 1–2 and the specific Wasserstein/Gaussian design is real, but it is a minor rather than fatal issue.

- **"Evaluation is limited to reconstruction"** — This is a valid limitation and kept as a Major weakness. However, the harsh critic's framing as "a decisive flaw" overstates it. The paper acknowledges the limitation in the conclusion, and reconstruction is a standard evaluation for VQ methods (many VQ papers report only reconstruction). However, given the paper's strong framing around autoregressive generation, the gap is significant.

- **"The only comparative evaluation that isolates the method is a synthetic experiment of limited relevance"** — The synthetic experiment in Section 3.2 is a controlled comparison that does provide some evidence; it is not the *only* evidence (there are also the main reconstruction tables). The criticism is overly dismissive.

- **Missing related works** — Not mentioned due to my inability to verify.

- **Style/formatting nitpicks** — Removed as parser artifacts.

- **Reproducibility nitpicks about "undisclosed hyperparameters"** — Partially removed per the soft rule. However, the complete absence of training details goes beyond a nitpick and is kept as Major weakness #1.

## Novel Insights

The reviews surface one observation not explicitly in the paper: the Gaussian assumption needed for the closed-form Wasserstein distance sits in tension with the Theorem 2 result that the optimal codebook density is proportional to \( f_A^{d/(d+2)} \) (not equal to \( f_A \) except in the limit \( d \to \infty \)). The paper does not analyze this approximation gap. Additionally, the synthetic experiments (Section 3.2) inadvertently reveal that existing methods like VQ+Linear *can* achieve distribution matching — they just fail under large initialization gaps — which raises the question of whether the Wasserstein regularization could be replaced by better initialization or a simpler alignment term. The reviews do not offer novel insights beyond what a careful reader would derive from the paper's own framing and gaps.

## Suggestions

1. **Provide full experimental details** — Report all hyperparameters (\( \alpha_1, \alpha_2, \alpha_3 \), learning rate, optimizer, batch size, codebook sizes, training steps, resolution). Add standard deviations or results from multiple seeds. Include training-time and inference-time comparisons.

2. **Add the missing ablation** — Show a table quantifying reconstruction metrics and utilization/perplexity for Wasserstein VQ with \( \alpha_3 > 0 \) versus \( \alpha_3 = 0 \) (all else equal). This is the single most important experiment needed.

3. **Address the generation gap** — Either add image generation experiments (even on a small-scale setup) or substantially revise the framing to accurately reflect the scope (reconstruction only). If the latter, explain why reconstruction results are sufficient evidence for the claims made.

4. **Analyze the Gaussian assumption** — Test sensitivity to non-Gaussian features (e.g., by visualizing feature distributions from the trained encoder, or by comparing the proposed loss with a non-parametric Wasserstein estimator on real features).

5. **Report computational cost** — Provide wall-clock time per iteration, memory usage for covariance estimation, and scaling behavior with feature dimension \( d \) and codebook size \( K \).

## Score and Decision

Originality: Good — the distribution-matching perspective on VQ is novel.
Importance of research question: High — codebook collapse and training instability are real problems.
Claims supported: Weak — the central claim is supported by synthetic experiments and briefly stated reconstruction results, but the lack of experimental details, the missing ablation, and the generation gap mean the evidence is insufficient.
Soundness of experiments: Weak — insufficient detail to evaluate, no ablation, no statistical rigor.
Clarity of writing: Good — the paper is generally well-written and clearly structured.
Value to community: Moderate — the idea is interesting, but in its current form the paper does not provide a validated, reproducible method.

The paper identifies a genuine problem and proposes a clean, principled solution. However, the experimental validation falls well below the bar for publication: training details are absent, the crucial ablation isolating the Wasserstein term is missing, and the motivation (autoregressive generation) is untested. The core idea has merit and could become a strong contribution with rigorous experiments, but the present version is not publishable as-is.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>