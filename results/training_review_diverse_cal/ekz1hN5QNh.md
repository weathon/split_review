I've thoroughly verified the paper content against all reviewer claims. Let me now produce the final consolidated review.

## Summary

This paper presents HCNN, a framework for building fully hyperbolic convolutional neural networks using the Lorentz model. The authors provide novel Lorentz-model formulations of 2D convolution, batch normalization (via Lorentzian centroid and parallel transport), and multinomial logistic regression (via hyperbolic hyperplane distance). They demonstrate these components in two architectures — a fully hyperbolic encoder (HCNN) and a hybrid encoder (HECNN) that replaces only high-hyperbolicity ResNet blocks — and evaluate them on classification (CIFAR-10/100, Tiny-ImageNet), adversarial robustness (FGSM/PGD), and VAE-based generation, showing consistent improvements over Euclidean and Poincaré-ball baselines.

## Strengths

- **First fully hyperbolic CNN encoder for vision**: The paper introduces the first vision architecture that learns features in hyperbolic space at every layer, directly addressing the limitation of prior hybrid models that rely on Euclidean backbones and only project to hyperbolic space in task heads (lines 25–27, 42). This is a genuine gap-filling contribution.

- **Novel Lorentz formulations of missing CNN components**: The paper provides Lorentz-model versions of 2D convolutional layers (Section 4.1), batch normalization using the closed-form Lorentzian centroid and parallel transport (Section 4.2), and MLR via hyperbolic hyperplane distance (Theorem 1–2). Prior Lorentz HNN work lacked these components, which were only available in the Poincaré ball. The batch normalization algorithm in particular avoids the slow iterative Fréchet mean required by prior Riemannian BN approaches (lines 106–119).

- **Consistent empirical gains across multiple tasks**: The Lorentz-based models outperform Euclidean and Poincaré baselines in nearly all settings. On CIFAR-100, HECNN achieves 78.76% vs. Euclidean 77.72% (Table 1). Under PGD attacks at ε=3.2/255, HCNN achieves 31.77% vs. Euclidean 26.30% (Table 2). On VAE generation, HCNN achieves best FID on CIFAR-10 (89.20) and CelebA (78.11) (Table 3). The adversarial results are particularly striking: HCNN beats even HECNN on all six attack conditions, showing a clear advantage for full hyperbolicity under distribution shift.

- **Honest treatment of unexpected findings**: The paper openly acknowledges that the hybrid HECNN outperforms the fully hyperbolic HCNN on clean classification accuracy (line 202: "We also notice that the hybrid encoder model outperforms the fully hyperbolic model") and calls the HECNN's strong performance in low-dimensional settings "unexpected" (line 314). This transparency is a strength, not a weakness.

## Weaknesses

### Fatal
None.

### Major

- **Framing over-emphasizes "fully hyperbolic" while results paint a more nuanced picture.** The title ("Fully Hyperbolic Convolutional Neural Networks") and the abstract/figure captions (e.g., line 21: "our HCNN learns features in hyperbolic spaces in every layer, fully leveraging the benefits of hyperbolic geometry") foreground the fully hyperbolic architecture as the central contribution. However, on clean classification (Table 1), the hybrid HECNN consistently outperforms HCNN (95.16 vs 95.14, 78.76 vs 78.07, 65.96 vs 65.71), and the paper's own discussion notes "not all parts of the model benefit from hyperbolic geometry" (line 202). The fully hyperbolic model does find its clear winning scenario — adversarial robustness (Table 2, all 6 conditions) and VAE generation (Table 3, 5/6 metrics) — but this nuance is absent from the title and first-impression framing. The paper would be stronger if it re-centered its contribution on "Lorentz CNN components" (which are the actual novel contribution) and presented the choice of how many hyperbolic layers to use as a design decision informed by downstream desiderata, rather than tying the contribution label to a specific architectural choice that its own results show is not universally optimal. This is fixable with revision — adjust the title to reflect that the core contribution is the Lorentz component set, not the "full" architecture per se.

### Minor

- **The Lorentz convolutional layer description relies heavily on references without enough self-contained detail.** The convolution is defined as `LFC(HCat(...))` (Equation 10), but LFC is only described as "similar to chen2021" and HCat (hyperbolic concatenation of neighboring vectors) is not defined — it is not obvious how concatenation of multiple manifold-valued vectors preserves the manifold constraint before LFC is applied. Similarly, origin padding is mentioned (line 92) but the paper does not discuss whether the padded vectors always satisfy the Lorentz constraint. For a method paper claiming "extend hyperbolic convolutional layers to 2D" and "generalize fundamental components," a reader should be able to understand the layer's mechanics without consulting two separate external papers (chen2021, shimizu-et-al-2020). A short textual description of how LFC operates (tangent-space linear mapping + exponential map, or a closed-form Lorentz operation?) and how HCat works would substantially improve clarity.

- **The residual connection's manifold constraint is not discussed.** The proposed residual connection adds space components and reconstructs the time component as $x_t = \sqrt{||\vect{x}_s||^2 - 1/K}$ (line 179). This requires $||\vect{x}_s||^2 \ge 1/|K|$. The paper does not discuss whether this condition can be violated through training, how numerical stability is maintained near the boundary, or whether feature clipping (mentioned in line 46 for general numerical stability) is applied here specifically. While this is unlikely to be a practical problem given the experiments work, it is a missing technical detail in the method description.

- **The VAE latent embedding analysis (Figure 4) makes a strong qualitative claim on subtle visual evidence.** The paper states "these structures cannot be found for the hybrid model" (line 345), comparing the HCNN latent space to hybrid Lorentz. The differences visible in the 2D projection plots (curved clusters vs. origin-pointing clusters) are visually modest, and the claim relies on subjective interpretation. The quantitative results (FID in Table 3) provide stronger support for HCNN's advantage than the qualitative embedding analysis does.

### Trivial
None.

## Nice-to-Haves
- A short derivation or citation for the distance-to-hyperplane formula (Theorem 1). While proofs belong in the appendix (which was stripped by the parser), the main text could briefly indicate how the formula follows from the hyperplane definition in Equation (13).
- An ablation showing performance with varying numbers of hyperbolic encoder blocks, to more precisely characterize when replacing Euclidean blocks helps versus hurts.
- Reporting wall-clock time or parameter counts to quantify the computational overhead of full vs. partial hyperbolization.

## Removed Points

These points were found in the reviews but are removed per verification guidelines:

1. **"The MLR distance formula is presented without proof/derivation"** — REMOVED. The paper presents Theorem 1 and Theorem 2; proofs belong in the appendix, which was stripped by the parser. Per policy, "REMOVE weaknesses about missing proofs in appendix."

2. **"The HECNN configuration sentence is truncated ('i.e.')"** — REMOVED. This is a PDF extraction artifact (missing text after "i.e." at line 200). Per policy, formatting/parser artifacts are not author errors.

3. **"The paper claims HECNN matches or outperforms HCNN on every dataset"** — The harsh critic framed this as if the fully hyperbolic model has no advantage anywhere, but Table 2 shows HCNN outperforms HECNN on all 6 adversarial conditions (often by >1.5%), and Table 3 shows HCNN leading on 5/6 VAE metrics. The framing criticism (Major weakness above) is retained but corrected to reflect the actual pattern of results.

4. **Strength Finder's claim that "HCNN achieves best FID on CIFAR-10 (89.20) and CelebA (78.11)"** — Retained but noted that on CIFAR-100 Gen FID, Hybrid Poincaré (98.19) beats HCNN (100.27). This nuance is captured in the strengths above.

## Novel Insights

The most interesting signal emerging from the reviews — not fully articulated by any single reviewer — is the task-dependent nature of optimal hyperbolicity depth. The fully hyperbolic HCNN clearly wins on adversarial robustness (all 6 conditions in Table 2) and generation (5/6 FID metrics in Table 3), while the hybrid HECNN wins on clean classification accuracy. This suggests a non-trivial trade-off: full hyperbolicity buys robustness and representation quality at the cost of some clean accuracy, likely because the hyperbolic distance metric creates larger margins between classes (good for robustness) while the Euclidean layers in HECNN may preserve finer-grained discriminative details needed for peak clean accuracy. The paper touches on this (line 248: "increased inter-class separation afforded by the distance metric which allows for greater slack") but does not develop it into a design principle. This pattern is worth highlighting as a direction for future work.

## Suggestions

1. Revise the title and abstract to reflect that the core contribution is the *set of Lorentz CNN components* (2D conv, BN, MLR) rather than the "fully hyperbolic" architecture specifically. The components can be deployed in either fully hyperbolic or hybrid configurations, and the choice depends on the task (clean accuracy vs. robustness/generation).
2. Add a paragraph in Section 4.1 explaining what LFC does at an operational level (tangent-space linear mapping + exponential map? closed-form Lorentz operation?) and how HCat is performed, so the layer is understandable without consulting chen2021.
3. Discuss the manifold constraint for the residual connection in Section 4.4 (whether $\|\vect{x}_s\|^2 \ge 1/|K|$ can be violated and how it is handled).
4. Tone down the qualitative claim about the VAE latent space (line 345) or supplement it with a quantitative measure of "tree-likeness" (e.g., hyperbolicity measurement of the learned embeddings).

## Score and Decision

**Originality**: Good — first Lorentz-model CNN encoder for vision, novel BN and MLR formulations.  
**Importance**: Solid — hyperbolic NNs for vision are an active area, and the missing Lorentz components fill a real gap.  
**Claims supported**: Mostly — the empirical results are genuine and well-documented, but the framing overstates the case for the fully hyperbolic architecture.  
**Soundness**: Good — experiments are thorough (5 runs with std, multiple datasets, two architectures, adversarial + generative + low-dim analysis).  
**Clarity**: Adequate — the conv layer details are sparser than ideal for a method paper.  
**Value**: The Lorentz CNN components are reusable and show consistent gains; the paper will be useful to the community.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>