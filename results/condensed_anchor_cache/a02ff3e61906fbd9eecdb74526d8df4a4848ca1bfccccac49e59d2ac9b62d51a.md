- Decision: Reject
- Scores: 6, 6, 3, 5

## Merged Review

### Summary

This paper addresses contextual bias in text-guided latent diffusion models (LDMs) by proposing two causally-motivated sampling frameworks: CB+ (strengthens bias) and CB- (weakens bias).  The methods use an LLM (Gemini) to sample confounders (co-occurring objects for CB+) or a VLM (LlaVa) to retrieve non-co-occurring objects (for CB-) from a distribution learned over unconditionally generated images, then condition the LDM on these confounders without retraining or accessing training data.  Evaluation on Visual Genome and COCO reports improvements in FID and LPIPS.  Reviewers are split: two find the work novel, relevant, and well-motivated; one finds the formulation overcomplicated and the method trivially reduces to prompt engineering; one finds the causal framing insightful but the text-level intervention too crude.

### Strengths

- The problem of contextual bias in diffusion models is relevant and well-motivated.  The recognition that contextual bias is “not inherently bad” and the provision of two separate frameworks (CB+ to strengthen, CB- to weaken) is a nuanced and valuable contribution.
- The causally-motivated formulation (causal graphs, confounder sampling, do-operations) provides a novel perspective for thinking about contextual bias and enables automated confounder estimation without explicit training.
- The methods are training-free and require no access to the original training data; they leverage the reasoning capabilities of LLMs/VLMs to automatically adjust the “amount of embedded commonsense” in generated images.
- Many experiments examine specific aspects: impact on realism and diversity (Tab 1, 4), prompt adherence (Tab 3), qualitative results (Fig 5), and complementary use with other conditioning frameworks (Fig 6).
- The CB- framework is a particularly interesting contribution: if a good confounder distribution can be learned, it may help inject diverse contextual biases into generative models.
- (Minority positive from R3) The causal inference formulation provides an interesting perspective, though R3 considers it the only strength.

### Weaknesses

1. **Novelty concern and over-complication (R3 strong, echoed by R2/R4).**  R3 argues the causal formulation is overcomplicated and the method ultimately reduces to a refined form of prompt engineering—retrieving co-occurring objects using LLMs and identifying objects using VLMs is trivial and commonly practiced (R3: “not innovative”).  R2 questions whether the method is simply adding nouns from $c'$ directly to the prompt $y$ (the practical incorporation is unclear).  R4 notes that the core contribution lies in LLM/VLM-based text extraction rather than in diffusion itself, making the intervention “overly rough” and heavily reliant on text prompt conditioning.

2. **Unclear practical implementation of confounder conditioning (R2).**  Despite the math in Eq. 3 and Eq. 7, it is ambiguous how the retrieved confounder $c'$ is actually used during generation for both CB+ and CB-.  From L387 it sounds like nouns from $c'$ are not simply added to the prompt; a step-by-step description is needed.

3. **Weak LDM identity and fairness of comparisons (R2).**  The specific LDM used (Fig 2,4-6) is not clearly stated.  It appears to be an older version of Stable Diffusion (possibly 1.4/2.1, not SDXL, per L509).  If the LDM is weaker than Gemini/LlaVa, the FID improvements may partly reflect the higher capacity and larger pretraining data of the LLM/VLM rather than the proposed method.  This must be clarified.

4. **Robustness gaps and unnatural outputs (R1, R2, R4).**  When the sampled confounder $c'$ is semantically distant from the prompt $y$ (e.g., $c'$ = “a snowy mountain”, $y$ = “a beach”), the model may ignore $c'$ or produce nonsensical images.  Weakening bias (CB-) can lead to physically implausible object combinations (e.g., a cat floating in air, a tree in a bedroom, motorcycles in a kitchen).  R4 notes hallucination issues in VLMs (e.g., mislabeling a horse and a donkey both as “donkey”), causing inaccurate confounder estimation.

5. **Misalignment of commonsense between LLM/VLM and diffusion model (R4).**  The models are trained on different datasets and with different strategies; the “bias” in the LLM/VLM may not match that in the LDM.  Example: LLM/VLM might associate “bird” with “tree,” while the diffusion model associates “bird” with “sky.”  This inconsistency undermines the assumption that $p(c)$ from the VLM is a good proxy for the diffusion model’s confounder distribution.

6. **Over-reliance on text-prompt conditioning (R4).**  The intervention is purely at the text-prompt level, which is limited.  Even with highly detailed prompts, the diffusion model may ignore specified objects (cite: Attend-and-Excite, Chefer et al.).  For a weak diffusion model, simply modifying the prompt may not yield the desired image.  Deeper latent-space interventions (e.g., minority guidance, Um & Ye) may be more effective for generating counter-commonsense images.  R4 recommends comparing against such approaches.

7. **High computational cost and scalability concerns (R1, R4).**  The method requires multiple sampling rounds from LLMs/VLMs (e.g., at least 10 VLM calls per generated image).  The interventional sampling chain (sampling $c'$, then generating $x$) introduces significant overhead compared to standard diffusion.  The need to compute/precompute $p(C')$ is computationally intensive for large datasets.  Preprocessing time, space complexity, and steps to reduce computation are unclear.

8. **Lack of quantitative user-specified bias control (R1).**  The framework does not provide a mechanism for users to specify the desired degree of bias strengthening/weakening, nor does it quantitatively evaluate how well adjustments meet user-defined bias levels.

9. **Need for more challenging test cases (R3).**  Modern diffusion models (SD, DALLE, Flux) can already generate diverse and complex images (e.g., “astronaut riding a horse on Mars”) with simple prompt engineering.  The paper should include examples where the proposed method significantly outperforms naive prompting.

10. **Writing and figure clarity (R2).**  The flow of the paper requires skipping ahead to find explanations, and figure captions are not self-contained.  The use of Eq. 6 requires explicit details: How many unconditional images $x'$ are marginalized over? Are they 10,000 from COCO test+val? Are they diverse enough? These details belong in Sec. 3.3.

11. **Missing details on complementary conditioning (R2).**  The discussion of using CB+ and CB- with other conditionings (ControlNet, DEADiff) is interesting but lacks a concrete description of how they are combined.