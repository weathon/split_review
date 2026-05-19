- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 3, 6, 6
Now I have a thorough understanding of the paper and can verify claims against the actual content. Let me compile the final review.

## Summary

This paper proposes a framework for dataset-wide, layer-wise concept analysis in image models (ResNet50). It extracts concept vectors via bisecting k-means clustering of PFVs, decomposes PFVs into concept coefficients via lasso regression, and introduces Generalized Integrated Gradients (GIG) to attribute causal relationships between concepts across layers. The qualitative results showing shared concepts across classes are compelling, and the core methodological pipeline is coherent.

## Strengths

- **Dataset-wide, inter-layer concept analysis is a genuine contribution.** Existing methods like CRP, VCC, and ACE provide class-specific explanations or analyze single layers. This paper extends the scope to the entire dataset across all layers, enabling discovery of shared concepts between classes (e.g., "Bird chest" appearing for both house finch and junco in Figure 1). This is a nontrivial extension.

- **GIG provides a principled approach to inter-layer concept attribution.** The formulation (Eq. 4–5) follows standard Integrated Gradients: scaling the reconstructed embedding from baseline (zero) to the full value via α, and computing ∂/∂u_{pq} of the projected target output along that path. The factor u_{pq} outside the integral plays the same role as (x_i − x'_i) in standard IG. This is mathematically sound — the derivative with respect to u_{pq} is well-defined through the chain rule through F_{ab} — and the method fills a genuine gap in concept attribution by measuring cross-layer causal influence.

- **Bisecting k-means is a reasonable design choice for sparse, variably-dense PFV spaces.** The motivation (background features cluster densely, rare features like "bird beak" are sparse) is clearly articulated, and the C-Insertion/C-Deletion evaluation (Figure 3) shows it generally outperforms SAE and dictionary learning across most layers.

- **Probabilistic PFV sampling addresses foreground-background imbalance.** Selecting PFVs in proportion to their contribution to the logit rather than uniformly is a principled approach to avoid overrepresenting class-irrelevant features like "sky."

## Weaknesses

### Major

- **Inter-layer attribution validation compares only against random ordering.** The Inter-layer Insertion/Deletion experiment (Figure 4, Section 4.2.2) contrasts GIG only with random concept ordering. This is the weakest possible baseline. The paper should compare GIG against standard alternatives: (a) gradient×activation importance, (b) ablation-based (leave-one-concept-out) importance, or (c) standard IG applied separately to each coefficient with a zero baseline. Beating random shows that GIG carries *some* signal, but does not establish that it is *good* relative to reasonable alternatives. Without stronger baselines, the claim that GIG "accurately attributing the relationship between concept vectors" is overstated.

- **No reconstruction fidelity analysis.** The entire GIG pipeline (Eq. 4) operates on the *reconstructed* embedding Ṽ^a = U^a V^{aT}, not the actual embedding X^a. The paper never reports reconstruction error (e.g., MSE between X^a and U^a V^{aT} as a function of concept count k and regularization λ). If reconstruction is poor, the gradient path through F_{ab}(α U^a V^{aT}) may deviate arbitrarily from the true model behavior, undermining the attribution. This is a critical gap.

- **Ablations are missing across all key design choices.** (a) Concept count: The choice of 8× the number of channels per layer (following Bricken et al. 2023 from language model SAEs) is used without any ablation showing how reconstruction quality or interpretability varies with k. (b) PFV sampling strategy: The probabilistic sampling is never compared to random sampling or uniform sampling. (c) Clustering method: Bisecting k-means is compared to SAE and dictionary learning only via downstream C-Insertion/C-Deletion; direct clustering quality metrics (silhouette score, cluster coherence) are absent. (d) Lasso regularization: The parameter λ appears in Eq. 3 but is never reported, let alone ablated.

- **No error bars or statistical significance.** All quantitative results (Figures 3–4) appear to be single runs. The inter-layer experiment uses "20 random images from the ImageNet validation set" — far too few to draw reliable conclusions, and no variance is reported. Without confidence intervals, it is unclear whether the observed advantages over baselines are meaningful.

- **PFV sampling mechanism is underspecified.** The paper states PFVs are selected "probabilistically... in proportion to its contribution to the output (logit)" (Section 3.2.1). But "contribution to the output" is never defined — is it gradient-based (saliency), the absolute logit change under masking, or something else? This is a critical detail for reproducibility and understanding potential biases in the sampling.

### Minor

- **Concept insertion/deletion mechanism is not described.** The paper applies C-Insertion and C-Deletion metrics but never specifies how a concept vector direction is "inserted" or "deleted" from the representation. Is the coefficient for that concept zeroed out? Is the direction projected out of all PFVs? The mechanism matters for interpreting the results.

- **Small evaluation sample.** The inter-layer validation uses only 20 images and 5 target concepts per layer transition. This limits confidence in the conclusions.

- **Novelty claims are somewhat overstated.** The paper states "Our work is the first application of this technique to vision models" (Section 2, line 88) and "mechanistic interpretability... has not been applied to image models" (Section 1, line 24). The specific claim about *dataset-wide, whole-layer* analysis is defensible, but the broader "first in vision" framing is unnecessarily strong and could be misleading without careful qualification.

- **Qualitative assessment of SAE concepts is subjective.** The claim that "the concepts extracted by SAE seem less persuasive" (Figure 3 caption) is presented as evidence without any quantitative backing. This should be removed or accompanied by a human evaluation study.

### Trivial

None.

## Nice-to-Haves

- A derivation showing that GIG satisfies completeness (sum of attributions equals the total change in target projection) would strengthen confidence in the method.
- A computation time / scalability analysis would help readers assess practical applicability.
- Clarifying whether the ERFs are used only for qualitative labeling or also to guide concept extraction (currently the paper suggests the former, but wording in Section 3.1 is ambiguous).

## Removed Points

- **"GIG formulation is mathematically inconsistent"** — This is factually incorrect. The GIG formulation follows standard Integrated Gradients: the path is α scaling all coefficients from 0 to their actual values (analogous to the straight-line path in standard IG), the derivative ∂/∂u_{pq} is taken of the function g(αU^a V^{aT}) which depends on u_{pq} through the chain rule, and the factor u_{pq} outside the integral mirrors (x_i − x'_i) in IG with zero baseline. The critic's claim that the path and derivative variable are mismatched misunderstands how IG applies when the quantity being attributed affects the function's output via a linear transformation (U^a V^{aT}). The formulation is valid.
- **"Circularity in C-Insertion/C-Deletion evaluation"** — GIG is used to compute the importance ordering for *all* extraction methods (bisecting k-means, SAE, dictionary learning) consistently. This is standard practice in CAT evaluation — some attribution method is needed to order concepts, and applying the same method across all competitors is fair.
- **"SAE comparison is unfair"** — The paper transparently describes how SAE is adapted from its usual setting (Section 4, Settings). The comparison methodology is explicit.
- **"Missing related works"** — Per meta-reviewer guidelines, specific missing citations are not verifiable and are not included.
- **"Concepts from SAE seem ambiguous is subjective"** — This is presented as a qualitative observation supplementary to the quantitative AUC comparison. It is fine as a qualitative remark but I note it is not quantitative evidence.
- **Miscellaneous formatting/style nitpicks and reproducibility complaints (missing appendix, hyperparameter table, code, training logs)** — Per guidelines, these are either parser artifacts or not required.

## Novel Insights

The reviews point out a pattern worth noting: the paper's ambition (dataset-wide, whole-layer causal analysis) inherently conflicts with the evaluation strategies available. Existing CAT metrics (C-Insertion/C-Deletion) assume a single importance-ordered list per class, but the paper's contribution covers cross-concept, cross-layer relationships. This means the authors cannot simply reuse existing evaluation tools — they must design new validation protocols. The current workaround (comparing only to random on inter-layer tasks) is unsurprisingly weak. A genuinely novel contribution would be to design and validate a *synthetic* ground-truth task where cross-layer concept relationships are known by construction, enabling rigorous evaluation. This paper does not do this, and this gap is the single largest barrier to accepting its claims.

## Suggestions

1. **Add stronger baselines to the inter-layer validation.** Compare GIG to gradient×activation importance, ablation-based importance, and standard IG applied coefficient-by-coefficient. Show that GIG outperforms these alternatives, not just random.
2. **Report reconstruction error** (MSE between X^a and U^a V^{aT}) across layers and concept counts. Show that the decomposition is faithful. If reconstruction is poor, the GIG path through reconstructed embeddings is not justified.
3. **Add ablations** for: concept count k (vary from 1× to 16× channels), PFV sampling strategy (random vs. proposed), and the lasso regularization parameter λ.
4. **Add error bars** via bootstrapping or multiple runs.
5. **Specify the PFV contribution metric** used for sampling, and the concept insertion/deletion mechanism.
6. **Tone down novelty claims.** Replace "first application to vision models" with precise language about being the first *dataset-wide, inter-layer* concept analysis in vision.
