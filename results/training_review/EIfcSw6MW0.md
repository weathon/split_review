Now I have all the information I need. Let me write the consolidated review.

## Summary

This paper proposes "Duet," a certified robust training method that uses a pre-trained vanilla model as a guide to preserve clean accuracy. The key idea is to perform SVD on weight matrices and transfer the rotation matrices (U, V^T) from the vanilla model to the certification model via a similarity loss, under the premise that rotation matrices encode clean-accuracy capability while singular values affect certified robustness. Experiments on CIFAR-10 with a 6 Conv + 2 FC architecture show a 3.76% clean accuracy improvement over global Lipschitz regularization, with a 0.93% certified accuracy drop, and rotation matrix similarity increasing from 77.8% to 95.6%.

## Strengths

- **Conceptually motivated decomposition of clean accuracy vs. robustness factors.** The paper identifies that certified robust training primarily scales spectral norms (singular values), and argues that this neglects rotation matrix information critical for clean accuracy. The SVD-based separation provides a clean conceptual framework and distinguishes the method from prior approaches that treat the entire weight update uniformly.

- **Quantitative improvement on the targeted metric.** The method achieves a 3.76% clean accuracy improvement over global Lipschitz regularization (BCP-style training) while incurring only a 0.93% certified accuracy drop. These numbers, though from limited settings, directly measure progress on the stated goal.

- **Empirical confirmation of rotation matrix alignment.** The average rotation matrix similarity between the certification model and the vanilla model improves from 77.8% to 95.6% under Duet, confirming that the proposed similarity loss effectively drives the desired alignment.

## Weaknesses

### Fatal

None. The core idea is not fundamentally flawed; the issues are about insufficient validation and presentation clarity.

### Major

- **Insufficient experimental evaluation to support the claimed generalizability.** The experiments are conducted on a single dataset (CIFAR-10), a single perturbation radius (36/255 in ℓ₂), and a single small architecture (6 Conv + 2 FC). Standard practice in certified robustness requires evaluation across multiple datasets (e.g., CIFAR-100, Tiny ImageNet), multiple radii, and ideally multiple architectures. Without this, the claim that Duet "offers practical solutions for a wide range of scenarios" is unsupported.

- **No comparison against state-of-the-art certified robust training methods.** The experimental comparison is limited to two baselines: global Lipschitz regularization (BCP-style, Lee et al., 2020) and local Lipschitz regularization (Huang et al., 2021). Several well-established methods discussed in the paper's own Related Work section — LMT (Tsuzuku et al., 2018), GloRo (Leino et al., 2021), and other modern approaches — are not compared experimentally. The reported improvements are relative to one specific baseline, making it unclear whether Duet offers any advantage over alternative approaches.

- **No ablation studies.** The method has at least three components: the guide model, the rotation matrix similarity loss, and the low-rank approximation. None are ablated. It is impossible to determine which component contributes what, or whether the clean accuracy improvement is due to the proposed mechanism or to auxiliary benefits of the two-model setup (e.g., implicit regularization from knowledge distillation).

- **The core causal claim is asserted but not validated.** The paper argues that rotation matrices determine clean accuracy while singular values determine certified robustness, and that aligning rotation matrices causally preserves clean accuracy. However, no experiment isolates this causal relationship. The similarity increase (77.8% → 95.6%) could be a side effect of better overall training rather than the cause of clean accuracy preservation. No analysis of singular value distributions, no controlled experiment with deliberately disrupted rotation alignment, and no measurement of whether similarity correlates with clean accuracy during training is provided.

### Minor

- **Ambiguity in the loss function formulation.** The notation $\|\sigma_{cer}^l\|$ and $\|\sigma_{van}^l\|$ in the similarity loss (Section 4.4) is ambiguous: it is unclear whether this denotes the spectral norm (the largest singular value) or the norm of the full vector of singular values. While the context suggests the spectral norm (since the paper earlier defines spectral norm as the maximum singular value), the use of norm-on-vector-of-singular-values notation is non-standard and should be clarified.

- **Standard experimental details are missing.** The paper does not report learning rate, batch size, number of training epochs, warm-up schedule, weight decay, or whether results are averaged over multiple random seeds with standard deviations. These are necessary for reproducibility assessment.

- **The claim of computational efficiency is unsupported by data.** The paper states that low-rank approximation "reduces the computational and storage costs" but provides no runtime measurements, memory profiling, or speed comparisons with baselines. In fact, the paper notes that local Lipschitz regularization is "impractical due to computational and memory costs" but provides no quantitative comparison of these costs against Duet.

- **Writing quality issues.** Section 4.2 contains a near-verbatim repetition of a sentence ("This allows the network structure of the certification model to minimize..."), and several passages are grammatically awkward, which impedes readability.

### Trivial

- Figures and the SVD diagram are presented as image placeholders in the extracted text — these should render properly in the original submission.

## Nice-to-Haves

- Testing at multiple ℓ₂ radii (e.g., 36/255, 72/255, 108/255) and ℓ∞ perturbations would strengthen generalizability claims.
- Visualizing singular value distributions for vanilla, baseline-certified, and Duet models would support the claimed mechanism.
- A plot of rotation matrix similarity vs. clean accuracy over the course of training would help establish the causal relationship.
- Adding randomized smoothing as a complementary baseline (noting that it is a probabilistic rather than deterministic method) would be natural since the paper discusses both categories.

## Removed Points

These points are flagged to be removed; treat them with caution:

1. **"The paper does not name the specific prior methods it compares against"** — REMOVED: factually incorrect. The paper explicitly states "global Lipschitz constant (Lee et al., 2020) and local Lipschitz constant (Huang et al., 2021)" in the experiment section (line 165).

2. **"Algorithm 1 is not actually provided" and "figures missing"** — REMOVED: the algorithm is presented as a figure in the original submission; the parser strips all images. It exists in the original paper.

3. **"The Lipschitz constant formula holds only for linear layers with 1-Lipschitz activations, which is not mentioned"** — REMOVED: the paper explicitly states that ReLU (which is 1-Lipschitz) is used as the activation function (line 38), and later mentions MaxMin. The formula is correct as stated.

4. **"The SVD decomposition diagram is garbled"** — REMOVED: this is a parser artifact from PDF extraction; the textual description of SVD is clear and standard.

5. **Strength Finder claim: "Computational efficiency via low-rank approximation"** — REMOVED: this conflicts with the verified weakness that no computational cost data is provided. An unsupported claim cannot serve as a strength.

6. **Missing related works** — REMOVED per policy (cannot verify existence of missing references without external sources).

## Novel Insights

None beyond the paper's own contributions. The reviews surface the same central tension: the paper proposes an interesting conceptual decomposition (rotation matrices for clean accuracy, singular values for robustness) but does not provide the experimental breadth needed to substantiate it. The insight that the method lacks causal validation of its core mechanism is the most important observation across the reviews.

## Suggestions

The paper needs substantial expansion before it could be considered for publication:

1. **Expand the experimental evaluation** to at least two datasets (CIFAR-10 and CIFAR-100), multiple ℓ₂ radii, and at least one additional architecture (e.g., ResNet-based). Report results with standard deviations over multiple seeds.

2. **Add ablation studies** isolating each component: (i) without the guide model, (ii) without the similarity loss (standard certified training), (iii) without low-rank approximation (full-rank transfer), and (iv) Duet full.

3. **Compare against additional SOTA baselines** beyond global/local Lipschitz regularization, such as LMT (Tsuzuku et al., 2018), GloRo (Leino et al., 2021), and SABR, on equal footing.

4. **Validate the causal mechanism** by showing that rotation matrix similarity correlates with clean accuracy during training, and/or by showing that disrupting the similarity loss degrades clean accuracy while leaving certified accuracy unaffected.

5. **Clarify the loss function notation**: specify whether $\|\sigma\|$ denotes the spectral norm or the norm of the singular value vector, and state how the similarity loss is weighted relative to the certification loss.

## Score and Decision

**Originality:** The core idea (vanilla-model-guided rotation matrix transfer via SVD) is moderately novel, though knowledge distillation for robustness has been explored.

**Importance of research question:** The clean accuracy vs. certified robustness trade-off is practically important. The question is well-motivated.

**Claims supported:** Only weakly. The experimental evidence is too thin and the core causal mechanism is not validated.

**Soundness of experiments:** Weak — single dataset, single radius, single architecture, no ablations, no error bars, missing hyperparameters.

**Clarity of writing:** Below average — method description has ambiguities, repeated sentences, and lacks algorithmic detail (though the algorithm figure was stripped).

**Value to the research community:** The conceptual framing (rotation matrices vs. singular values) could be valuable if properly validated, but in its current form the paper does not provide the evidence needed to build upon.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>