Now I have all the information I need. Let me synthesize the final review.

---

## Summary

This paper proposes GenZSL, a generative zero-shot learning method that "induces" unseen-class visual features from similar seen-class samples (using CLIP text embeddings as weak semantic vectors) rather than generating from scratch/Gaussian noise as in prior generative ZSL. The method introduces two technical components: (i) class diversity promotion (CDP), which removes the first principal component of CLIP text embeddings to make class vectors nearly orthogonal, and (ii) an inductive variational autoencoder (IVAE) with target class reconstruction and boosting losses. Experiments on CUB, SUN, and AWA2 report large performance gains and substantially faster training compared to prior generative ZSL baselines.

## Strengths

- **Novel induction-based paradigm for generative ZSL.** GenZSL is the first generative ZSL method to generate unseen class features from similar seen class samples rather than from noise. This is a genuine conceptual departure from prior "imagination-based" generative ZSL and is plausibly motivated by human concept learning. The paper states this clearly as a core contribution (Section 1).

- **Practical advantage of eliminating expert-annotated attributes.** GenZSL uses only weak class semantic vectors (CLIP text embeddings of class names) and yet achieves strong results. Table 4 shows that when all methods use the same CLIP text embeddings, GenZSL's harmonic mean is at least 22.1% higher than f-VAEGAN. This is practically significant because expert attribute annotation is expensive and limits scene generalization.

- **Ablation validates the necessity of each component.** Table 3 shows that removing CDP, the target class reconstruction loss (L_TR), or the boosting loss causes large performance drops (e.g., removing L_TR reduces harmonic mean by 30.8% on CUB and 33.5% on AWA2). This confirms that the two design principles (class diversity promotion and target class-guided information boosting) are individually necessary.

- **Large efficiency gains.** Training speed is more than 60× faster than f-VAEGAN on AWA2 (Figure 5), and the method converges early. This is a meaningful practical advantage.

## Weaknesses

### Fatal
None.

### Major

- **Uncontrolled visual feature extractor invalidates the primary comparisons.** The paper states that visual features are "extracted from the CLIP vision encoder [37]" (implementation details). The baselines in Tables 1 and 2 (f-VAEGAN, TF-VAEGAN, etc.) were originally published using ResNet101 features. The paper does not state whether these baselines were re-run with CLIP features or whether published numbers are used as-is. If the latter (which is the default reading given no mention of re-running), the comparisons are confounded: the reported performance gap could be substantially driven by the CLIP feature backbone rather than by the proposed induction mechanism. The same concern applies to Table 2's GZSL comparisons and weakens the paper's central claim of "24.7% performance gains."

- **No direct ablation isolating "induction vs. imagination" within the same architecture.** The paper's core thesis is that induction (generating from seen-class samples) is superior to imagination (generating from noise). Yet no experiment compares GenZSL to an otherwise identical variant that uses Gaussian noise as the encoder input while keeping all other components (CDP, losses, CLIP features) the same. The ablation in Table 3 does not include this control. The only comparisons to imagination-based methods (f-VAEGAN, TF-VAEGAN) use different architectures and potentially different features, conflating multiple factors. Without this controlled experiment, the paper cannot attribute its gains specifically to the induction mechanism as opposed to CDP, the boosting losses, or the CLIP backbone.

### Minor

- **Unclear whether baseline methods in Table 4 were properly adapted for CLIP text embeddings.** f-VAEGAN and TF-VAEGAN were designed for expert-annotated attribute vectors. The paper reports a sharp performance drop for f-VAEGAN (harmonic mean from 52.9% to 35.3%) when switching from strong to weak semantic vectors. It does not specify whether these methods were re-trained or had their hyperparameters tuned for CLIP text embeddings. The observed degradation may partly reflect suboptimal configuration rather than an inherent limitation of imagination-based architectures.

- **No standard deviations or confidence intervals reported.** Given the stochasticity of VAE training and sampling, reporting single-run numbers weakens confidence in the results. This is especially relevant for the large claimed margins.

- **The CDP claim about preserving "original class relationships" is imprecise.** After removing the first principal component, class vectors become nearly orthogonal (mean similarity drops from 0.57 to 1.8e-5). Orthogonality fundamentally changes the geometry — relationships in the original space are not "kept" in any meaningful sense. The paper should clarify what is preserved (relative distances in the orthogonal complement) and analyze whether removing this component discards useful class structure (e.g., superclass distinctions like "bird" vs. "mammal").

- **k sensitivity (number of referent classes) is only analyzed on CUB.** The paper's referent selection mechanism may behave differently on SUN (fine-grained scenes) and AWA2 (coarse-grained animals), but only CUB is analyzed in Figure 6(b).

### Trivial

- The wording that the latent variable o is a "perturbation applied to x_refer" (Section 3.3) is slightly informal. The mathematical formulation (x̂ = IVAE(x_refer + o, z̃_target) with o = δ·N(0,1) + μ) is clear, but calling o a "perturbation" could mislead readers into thinking it is small-magnitude additive noise rather than a reparameterized latent variable.

## Nice-to-Haves

- Report results with multiple random seeds and standard deviations.
- Provide a qualitative analysis (e.g., t-SNE or nearest-neighbor visualization of generated features) for failure cases or domains where referent selection may be unreliable.
- Analyze the sensitivity of referent class selection k on SUN and AWA2 datasets.
- Motivate the specific mixup fusion weights (0.8 and 0.2) with a brief justification or sensitivity analysis.

## Removed Points

- **Cognitive psychology motivation is "ornamental":** This is a subjective opinion about the introduction's framing, not a factual weakness. The paper uses cognitive science as inspiration, which is standard practice; it does not claim to implement Bayesian inference over compositional priors.
- **"The paper would benefit from adding more models" / generic suggestions for more experiments:** These are not specific weaknesses of the current paper.
- **Missing discussion of failure cases where referent classes are poor matches:** This is a nice-to-have, not a core weakness.
- **Code repository and dependency version complaints:** Reproducibility concerns about exact dependency versions are nitpicks beyond what is reasonably included in a submission. An anonymous code repository is provided.

## Novel Insights

The harsh critic's most valuable observation is that the paper's central comparison is structurally confounded: the feature backbone (CLIP vs. ResNet) and the generation paradigm (induction vs. imagination) are not disentangled, so the reader cannot tell which factor drives the reported gains. The critic correctly identifies that adding a within-architecture control (GenZSL with noise inputs) would clarify the contribution. The strength finder correctly identifies the paper's genuine novelty (first inductive generative ZSL method) and practical advantage (eliminating expert attribute annotation). Together, the reviews suggest a paper with a genuinely novel idea that has not yet been rigorously validated.

## Suggestions

1. **Re-run all baselines using the same CLIP visual features and weak semantic vectors** (or clearly state which baselines were re-run and which are cited from prior work). If re-running is infeasible, add a dedicated analysis comparing the impact of the feature backbone on the reported numbers.

2. **Add a controlled ablation** comparing GenZSL (with referent sample inputs) to a version of the same architecture that uses Gaussian noise as the encoder input, keeping all losses, CDP, and CLIP features identical. This directly tests whether induction drives the gains.

3. **Report all main results with standard deviations** over at least 3 random seeds, and specify the random seeds used.

4. **Clarify how f-VAEGAN and TF-VAEGAN were configured for weak semantic vectors in Table 4** and whether any hyperparameter tuning was performed for these baselines.

5. **Rephrase the claim about CDP preserving "original class relationships"** to more precisely describe what is preserved in the projected subspace, and discuss whether removing the first principal component could discard useful class structure.

## Score and Decision

This paper introduces a genuinely novel induction-based paradigm for generative ZSL and demonstrates practical advantages (weak semantic vectors, fast training). However, the experimental validation has two significant gaps: (1) the primary comparisons are confounded by the use of different visual feature backbones, and (2) the core "induction vs. imagination" claim is never tested with a within-architecture control. These issues prevent the paper from supporting its central empirical claims in the current form. The ideas are promising and the issues are fixable, but the evidence as presented is insufficient for acceptance.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>