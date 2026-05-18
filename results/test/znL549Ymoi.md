Now I have all the information I need. Let me construct the consolidated review.

## Summary

This paper introduces a simple four-component protocol to induce instructed lying in 20–24 chat models across four families (Llama, Gemma, Yi, Qwen). By applying PCA to residual stream activations, it identifies three iterative refinement stages in the latent space: (1) separation of honest/lying instruction clusters, (2) emergence of truth directions (true-vs-false representations), and (3) rotation of truth directions under lying prompts from parallel to anti-parallel relative to the honest condition. The paper shows that completion of Stage 3 correlates with lying capability and uses activation patching (on two models) and contrastive steering (across model families) to causally link Stage 3 layers to deceptive behavior.

## Strengths

- **Simple, generalizable protocol for inducing instructed lying across diverse model families and sizes.** The paper demonstrates a single prompting procedure that works reliably across 24 models from four families (Llama, Gemma, Yi, Qwen) ranging from 1.5B to 70B parameters (Figure 2, Table 1). This is a meaningful extension over prior work (Campbell et al., 2023) that focused on a single model (Llama-2-70B-chat).

- **Identification of a consistent three-stage representational motif.** By performing PCA on residual stream activations layer-by-layer and tracking cosine similarity between "truth directions" under honest vs. lying prompts, the paper reveals a qualitatively consistent pattern: instruction clusters separate (Stage 1), truth directions emerge (Stage 2), then rotate from parallel to anti-parallel (Stage 3). This three-stage structure is visually demonstrated across all lying-capable models (Figure 3, Figure 4, Appendix I).

- **Predictive relationship between Stage 3 progression and lying capability.** The paper shows that the degree of truth-direction rotation (cosine similarity between honest and lying truth directions in late layers) distinguishes models that can lie from those that cannot (Figure 4). Models incapable of lying never complete Stage 3 (cosine similarity remains ~1), while successful liars reach anti-parallel (cosine similarity ~ −1). This is an interpretable predictor grounded in the model's internal representations rather than just output behavior.

- **Integration of multiple interpretability methods (probing, patching, steering) converging on Stage 3 layers.** The causal identification is triangulated: activation patching localizes lying-critical layers and attention heads (Figure 5), and contrastive steering is effective *only* when applied to Stage 3 layers (Figure 6). This convergence across methods strengthens the case that the rotation motif is functionally relevant, not merely correlational.

## Weaknesses

### Major

- **The central predictive claim ("Stage 3 progression predicts lying") lacks statistical rigor and uses undefined variables.** The paper states "stage 3 progression strongly correlates with the lying score across all models tested" (line 190) but reports no correlation coefficient, p-value, or confidence interval. Moreover, "Stage 3 progression" is not given an operational definition (is it the final-layer cosine similarity? the maximum slope? the point where cosine crosses zero?) and "lying score" is never formally defined in the main text (the paper points to appendix §E for "quantification of model performance"). For a claim highlighted in the abstract, title, and conclusion, the absence of any statistical measure is a significant gap that weakens the paper's strongest result.

- **Causal (patching) evidence for the universality claim is shown for only 2 of the lying-capable models.** The detailed layer-by-layer and head-by-head activation patching results (Figure 5) are presented for Llama-3-8b-Instruct and Gemma-2-9b-it. While the steering results span more models (Figure 6A), the patching analysis that identifies the *sparse set of layers and attention heads* causally responsible for lying—and ties them to Stage 3—is demonstrated on only two models. The abstract claims this is "consistent across all models tested," but the main text does not provide sufficient causal evidence to support universality. (Note: appendix results may partially address this, but the main text should either reference them explicitly or scale back the claim.)

- **Stage identification procedure is informal and not reproducible from the description.** The three stages are described verbally, and the boundaries between them are stated without any algorithmic criterion (e.g., "layer 7" marks a transition in Figure 3A, but how this boundary was determined is not explained). Stage 2 is not even given a labeled subsection header in the results section (the text jumps directly from "Stage 1" to "Stage 3" at lines 179–181). Without a principled, reproducible method for assigning layers to stages (change-point detection on cosine similarity slope, clustering purity thresholds, etc.), the central structural claim—that the same three stages appear in every lying-capable model—rests on visual inspection rather than a quantifiable procedure. This creates a risk of circularity if stages are defined post hoc by the presence of the rotation the paper aims to explain.

### Minor

- **Scope is narrower than the title and framing suggest.** The paper studies only *instructed lying* (models explicitly told to lie). The title "Interpretability of LLM Deception: Universal Motif" and abstract's broader use of "deception" could imply coverage of spontaneous deception, imitative falsehoods, or strategic deception. The limitations section (line 226) acknowledges this, but the title and abstract do not reflect the bounded scope. The findings are about instructed lying—a specific and important setting—but the broader terminology oversells the generality.

- **Interpretive ambiguity of the "rotation" phenomenon.** The paper describes the rotation of truth directions as the key motif, but does not analyze whether this rotation reflects a deception-specific computation or a simpler mechanism (e.g., a learned "flip" operation that inverts an existing truthful representation). The observation that cosine similarity goes from +1 to −1 is consistent with a linear negation of the truth direction under lying prompts. The paper does not distinguish between these interpretations.

### Trivial

- **Inconsistent model count.** The abstract and §4.1 (line 170) state "20" models, while the contributions list (line 16) and Figure 4 caption say "24." This inconsistency erodes confidence in the reporting and should be corrected.

## Nice-to-Haves

- Formalize "lying score" (e.g., honest accuracy − lying accuracy) and report it for all models.
- Provide a correlation coefficient and p-value for the Stage 3 progression vs. lying score relationship, or a logistic regression predicting lying capability from cosine similarity.
- Report at least one model from Yi and Qwen families in the main-text patching analysis, or explicitly state where these results appear in the appendix.
- Discuss whether the rotation is a "flip" of an existing representation or a genuine deception-specific computation.

## Removed Points

- **Criticism that supplementary figures in the appendix are unavailable for verification.** The appendix was stripped by the parser; these figures exist in the original submission. Removed per hard rule.
- **Criticism about "knowingly lie" assumption conflating instruction-following with deception.** The paper clearly defines its setup (instructed lying) and acknowledges this scope in the limitations. The paper never claims to study spontaneous deception. This is a framing preference, not a flaw.
- **Generalizations from the strength finder that are too generic or conflict with verified weaknesses.** Some phrasing about "comprehensive evaluation across 20+ models" and "universality" was softened: the behavioral evaluation is indeed comprehensive, but the causal evidence is not.

## Novel Insights

The most interesting observation from the review process is the disconnect between the paper's observational and causal evidence. The paper convincingly shows that the rotation motif is universal *as an observational phenomenon* (across all 24 models), but the causal evidence that these specific layers *drive* lying is demonstrated on far fewer models. This raises an important question the paper does not fully address: is the rotation a causal mechanism for deception, or a necessary-but-not-sufficient representational signature that emerges whenever a model processes conflicting (honest vs. lying) instructions? The steering results (Figure 6A, effective across families) suggest the latter is unlikely, but the gap between observational breadth and causal depth is worth examining in future work.

## Suggestions

1. **Operationalize everything.** Define "Stage 3 progression" by a reproducible criterion (e.g., final-layer cosine similarity between truth directions, or the area under the cosine curve below zero). Define "lying score" explicitly (e.g., honest accuracy − lying accuracy). Report the correlation with a coefficient and p-value. These changes would turn suggestive figures into testable, replicable claims.

2. **Add a stage-boundary algorithm.** Use a quantitative criterion (e.g., when the derivative of cosine similarity crosses a threshold, or when PCA cluster purity exceeds a threshold) to assign layers to stages automatically. Report the consistency of boundaries across all 24 models. This would convert the visual observation into a rigorous finding.

3. **Extend causal evidence to more families in the main text.** Even one additional model from Yi and Qwen families for the patching analysis would substantially strengthen the universality claim. If these results already exist in the appendix, add explicit cross-references in the main text (e.g., "see Appendix Figure X for analogous results on Yi-9B and Qwen-7B").

4. **Calibrate the title and abstract.** Use "instructed lying" or "knowingly lying" instead of the broader "deception" to match the experimental scope. This is a simple fix that would increase precision.

## Score and Decision

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>