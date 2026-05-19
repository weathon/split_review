- Decision: Reject
- Avg Score: 1.67
- Scores: 1, 1, 3
Now I have all the information needed. Let me produce the final consolidated review.

## Summary

This paper proposes a framework combining Uncertainty-Receptive Fusion (URF) for multi-modal learning, an image acquisition model with Monte Carlo inference, and entropy-based uncertainty assessment (EUA/GUE) for medical image analysis. The stated goal is fracture classification on the MURA dataset, but the methodology is developed for segmentation and regression tasks, resulting in a fundamental task incoherence that runs throughout the paper.

## Strengths

- **Principled treatment of aleatoric uncertainty via an image acquisition model.** The paper formalizes spatial transformations and noise (Equation 3) and derives a Monte Carlo inference procedure using latent variables (Section 2.2, Equations 4–10). This provides a more rigorous Bayesian foundation than ad-hoc test-time augmentation, with explicit prior distributions specified for rotation and noise parameters (Section 2.2).

- **Combined consideration of aleatoric and epistemic uncertainty.** The framework jointly addresses input-driven (aleatoric) uncertainty through the acquisition model and model-driven (epistemic) uncertainty through MC dropout (Sections 2.2.2–2.2.3), which is more comprehensive than works focusing on a single uncertainty type.

- **Explicit prior specification for transformation parameters.** The paper concretely defines a uniform prior for rotation angle and a Gaussian prior for image noise (Section 2.2), enabling principled sampling rather than ad-hoc augmentation choices.

## Weaknesses

### Fatal

- **Fundamental task incoherence between motivation and methodology.** The introduction and abstract frame the paper as addressing **fracture classification** on the MURA dataset: "We provide an end-to-end system specifically created for the classification of fractures musculoskeletal radiographs images" (line 20). However, the methodology is developed for **segmentation** tasks throughout: pixel-level uncertainty analysis (line 150: "It is advantageous to assess uncertainty at the pixel level when doing segmentation tasks"), structure-wise uncertainty via Volume Variation Coefficient (Section 2.2.3), Dice scores as the evaluation metric (line 197), and the conclusion stating the work examined "CNN-driven medical image segmentation" (line 208). The URF method in Section 2.1 is described for **regression** with multi-modal inputs. These three framings (classification, segmentation, regression) are never reconciled. The paper literally does not know what task it is solving, and the connection between URF (multi-modal regression ensemble), the image acquisition model (segmentation-oriented), and the MURA dataset (image-level classification) is never established. This is not a minor scope ambiguity — it invalidates the paper's core claim of a coherent end-to-end system.

### Major

- **Methodology components are disconnected fragments rather than a unified framework.** The paper presents URF (Section 2.1), an image acquisition model (Section 2.2), EUA (Section 2.2.2), and GUE (Section 2.2.3) as separate blocks with no explanation of how they integrate. URF is a multi-modal boosting scheme for regression; the acquisition model is a Bayesian framing of test-time augmentation for segmentation; EUA/GUE are uncertainty estimation methods. How URF uses the acquisition model's uncertainty estimates, or how the sequential boosting relates to the entropy-based EUA, is never specified. The paper reads as a compilation of loosely connected ideas rather than a single, coherent proposal.

- **Experimental evidence is not present in the extracted text.** Section 2.4 (Summary) and Section 3 (Conclusion) make quantitative claims about performance (Dice scores, comparisons between EUA and EUA+TTD, W-Net combination) and repeatedly reference "Figures 6," "Figure 5," "Table 4," and "Table 5" as supporting evidence. None of these figures or tables appear in the extracted text. While it is possible the parser failed to extract embedded images/tables (as it did with the image reference for Figure 1), this means no quantitative validation can be assessed from the submitted text. Combined with the task incoherence, the paper's central performance claims are unverifiable.

### Minor

- **Equation 8 is mathematically ill-formed.** The three-line array attempts to express the expectation E(Y|I) but is garbled: the first line is an incomplete integral (missing the measure dy), the second defines Q with differentials dangling outside an integral expression, and the third treats "dy" as an assignable quantity — which is nonsensical. This makes a key derivation unreadable (line 110).

- **Key terminology is undefined.** The section heading "PRIOR DISTRIBUTIONS OF FLUKY MODEL" (Section 2.2.1) introduces the term "Fluky Model" that never appears or is defined in the body text. The variable $X$ is introduced in line 82 ("labels corresponding to $X$ and $X_0$") without definition, and seems to be used interchangeably with $I$ (the image), creating confusion throughout the derivation.

- **Novelty of URF relative to prior work is unclear.** The paper claims URF "follow[s] a novel pattern of sequential boosting among diverse base learners" (line 61), but does not compare against standard boosting methods (AdaBoost, XGBoost) or explain how uncertainty-weighted boosting differs from existing confidence-weighted ensemble methods. Without positioning against the large body of work on boosting and uncertainty-weighted ensembles, the claimed novelty cannot be evaluated.

### Trivial

None.

## Nice-to-Haves

- Provide dataset splits, training hyperparameters, and implementation details for the MURA dataset.
- Clarify whether the system targets classification, segmentation, or regression — then consistently develop the methodology for that single task.
- Show how URF (multi-modal boosting) connects to the image acquisition model; e.g., does URF use the acquisition model's uncertainty estimates as its weighting mechanism?
- Include a pseudocode block for the sequential boosting procedure in URF.

## Removed Points

These points from the reviewers were excluded:

- **"Complete absence of experimental validation" as a pure structural flaw.** The paper does describe experimental discussion in prose (Dice scores, comparisons, Monte Carlo sample sizes). The missing figures/tables may be a parser extraction artifact (as with Figure 1's embedded image). The point is retained in the Major section as "experimental evidence is not present in the extracted text" but not treated as "no experiments were done."

- **Formatting and grammar nitpicks** (e.g., "supplement" vs "augment," "cognitive state calculation...cerebration"). These are excluded per formatting-artifact rules.

- **Criticisms about the URF uncertainty measure being "ad-hoc" without specific justification.** The derivation of Equation 2 from Gaussian log-likelihood components is a reasonable if simple heuristic; calling it ad-hoc without demonstrating a concrete flaw is opinion.

- **"Missing related works"** — excluded per instructions.

- **Strength Finder claim of "demonstrated accuracy gain from EUA"** — removed because the evidence (Figures 6, Table 5) is not present in the extracted text, so the gain is claimed but not demonstrated. This conflicts with a verified weakness.

- **Generic strengths** ("important problem," "addressed interesting question") — removed as they lack specific content.

## Novel Insights

None beyond the paper's own contributions. The reviews surface the task-incoherence problem clearly but do not generate novel insights about the methodology itself.

## Suggestions

1. **Resolve the task identity crisis.** Decide whether the paper addresses classification (MURA), segmentation, or regression — then rewrite the motivation, methodology, and experiments consistently for that single task. The current text presents three different tasks in different sections.

2. **Provide a clear diagram or pseudocode showing how URF, the acquisition model, EUA, and GUE fit into a single pipeline.** Explain which component produces which output and how they are combined.

3. **Fix Equation 8** — it should properly express E(Y|I) as an integral over the joint distribution of the latent image, transformation, and noise parameters, not as the current garbled array.

4. **Include the experimental figures and tables** that are currently referenced but absent, with proper baselines and error bars.

5. **Define all notation before or upon first use.** The variable $X$ appears undefined in line 82 and seems to substitute for $I$.
