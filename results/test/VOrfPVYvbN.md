Now I have all the evidence I need. Let me write the consolidated review.

---

## Summary

This paper introduces Domain Bridge, a method for inferring the input data domain of black-box image classifiers by iteratively generating images with Stable Diffusion, checking target-model classifications, and using the results (via CLIP/BLIP encoding and GPT-4 summarization/grouping/enrichment) to refine textual descriptions of the target domain. The method is evaluated on CIFAR-10 (10/10 classes correct), Places365 (360/365 vs. 159 for a corpus-based baseline), a CelebA face-attribute classifier, and models from Hugging Face, with a model-cloning follow-up showing 84.8% accuracy using 5,000 generated images vs. 35.5% for the corpus baseline.

## Strengths

- **Strong quantitative results on domain identification**: On CIFAR-10 the method identifies all 10 classes correctly versus the corpus baseline misclassifying "truck" as "entertainment center." On Places365 it identifies 360/365 classes versus 159/365 for the baseline (Table 2). These are large gaps that suggest the generative search space genuinely provides finer granularity than static corpora.

- **Compelling model cloning demonstration**: Using only 5,000 images generated from the recovered descriptions for model cloning achieves 84.8% accuracy, substantially outperforming the corpus-based approach (35.5%) and even surpassing the 81.3% obtained from held-out CIFAR-10 training data (Table 3). This quantifies the practical utility of the recovered descriptions.

- **Demonstrate operational generality**: The method is applied to diverse real-world models from Hugging Face (pneumonia X-ray detector, brand-specific shoe classifier, 100-class food classifier with 97/100 correct), validating the method beyond curated academic benchmarks.

- **Reveals model biases as a side benefit**: The face-attribute experiment surfaces that the target model relies on attire cues (e.g., "No_Beard" → "man, tie and shirt"), demonstrating an unadvertised capability of the approach for detecting spurious correlations in the target model.

## Weaknesses

### Major

- **Objective function defined but not used to guide the search (overclaim)**: Equation (1) formalizes V(e) with both relevance and generality terms, and the paper claims to "search for an embedding that optimizes the objective function" (line 79). However, the search algorithm (Section 4.1) uses only the relevance score (fraction k/m of correct classifications) to drive all decisions — enrichment, summarization, grouping, pruning. The full objective including the generality term (cosine similarity) is only computed at termination to rank candidate nodes (line 157). The paper does not demonstrate that the generality term provides any benefit during search, nor does it compare a version that uses the full objective against the current relevance-only search. This is a significant gap between what the formalism promises and what the algorithm delivers.

- **Baseline comparison lacks sufficient specification**: The "corpus-based approach" is referenced to prior work but the paper does not describe how it was implemented for the comparison — what dataset it used (ImageNet only?), what selection algorithm it ran, or what its output format was. Without this, the reported advantage (360/365 vs. 159/365 for Places365) cannot be adequately scrutinized. The claim that it misclassifies "truck" as "entertainment center" or "airplane cabin" as "cinema" is stated without explanation of whether this reflects a limitation of the specific prior method or of the comparison setup. This is critical since the paper's central claim of superiority rests on these comparisons.

### Minor

- **No ablation study**: The framework has five distinct components (Description Decoder, Image Encoder, Summarizer, Grouper, Enricher) plus LLM operations. No experiment tests a variant that omits any component (e.g., no summarizer, no grouper, no enricher) or compares against a simpler version that just picks the highest-relevance description without iterative refinement. The reader cannot tell which components are essential and whether results are driven by the search procedure or by brute-force coverage of the 1,000 ImageNet initial descriptions.

- **Fine-grained face attribute results show systematic confounding that is under-analyzed**: Table 5 (tab:face) shows that outcomes frequently converge on gender terms ("woman," "man") even for attributes where gender is not the causal feature (e.g., "Arched_Eyebrows" → "woman, thick eyebrows"; "Bushy_Eyebrows" → "man, mustache"). While the paper acknowledges some of these as biases in the generative model or target model, it does not quantify how often this occurs, analyze whether the search is latching onto the strongest available signal (gender) rather than the actual attribute, or propose a mechanism to mitigate it. The "self-correcting effect" claimed in the Discussion refers to robustness against incorrect descriptions, not protection against spurious correlations — but the distinction is not clearly made.

- **Missing reproducibility-critical details**: The LLM prompts for the Summarizer, Grouper, and Enricher (GPT-4) are not provided. The value of λ in the objective function is stated as "a predefined constant" (line 71) but never reported. The number of generated images per iteration (m), total LLM API calls, and total compute time are not disclosed. These omissions hinder reproducibility and assessment of practical viability.

- **Algorithm description has ambiguous terminology**: Step 4 says "If node p is at shallow depths" but "shallow" is never defined relative to a threshold. The condition for proceeding to Step 5 vs. Step 6 when `k=0` at non-shallow depths is not specified. The termination condition (Step 11) references a "preset maximum depth" and a relevance threshold that are not reported.

### Trivial

- The paper does not analyze the 5 failure cases on Places365 (out of 365), which could provide insight into the method's limitations.
- For the Hugging Face food classifier, the three failures (soup classes) are attributed to the image encoder describing ingredients rather than the dish name, but no deeper analysis or attempted workaround is provided.

## Nice-to-Haves

- An experiment using the full objective (relevance + generality) to guide search decisions (e.g., pruning, node selection) rather than only for final ranking would directly test whether the generality term is useful.
- A simpler baseline within the authors' own framework — e.g., pick the description with highest relevance from the initial 1,000 ImageNet classes without any iterative refinement or generative search — would isolate the contribution of the iterative loop.
- A sensitivity analysis for λ and for the maximum depth / relevance threshold would strengthen the paper.
- Reporting precision, recall, or per-attribute accuracy for the face attribute experiment would sharpen the assessment.

## Removed Points

These points are flagged as removed; treat them with caution.

1. **"Initial description pool may not include relevant class name" (from Critic Point 3)**: The critic claims the paper does not test what happens when initial descriptions lack relevant class names. This is factually wrong — the Places365 experiment explicitly uses a second set starting with the generic term "place" (line 241) and reports identical results. Removed.

2. **"Any user can see the model name implies this domain" (from Critic Point 6 on Hugging Face)**: The method operates on black-box models without using model names. The critic's suggestion that the pneumonia X-ray finding is trivial because the model name implies it ignores the black-box setting. Removed.

3. **"Self-correcting effect is contradicted by face results" (from Critic Point 4)**: The paper's "self-correcting effect" discussion (Section 5.5) describes robustness against incorrect descriptions amplifying into cascades of effective ones. It does not claim immunity to local optima — in fact it acknowledges local optima as a limitation (line 368). The critic conflates two different failure modes. Removed.

## Novel Insights

None beyond the paper's own contributions. The reviews surface a tension between the paper's formal framing (optimizing V(e) with a generality term) and its actual algorithm (relevance-guided search with post-hoc objective evaluation), but this is an internal inconsistency in the paper rather than a novel observation about the field.

## Suggestions

1. **Align the formalism with the algorithm**: Either modify the search to use the full objective V(e) to guide decisions (enrichment, pruning), or explicitly state that the search minimizes relevance as a proxy and uses the full objective only for final selection. The current framing overclaims.

2. **Add a controlled ablation**: Compare the full method against a variant that starts from the same initial descriptions but selects the best description by relevance only, without iterative refinement, enrichment, or grouping. This would isolate the contribution of the iterative search loop.

3. **Quantify the confounding in the face attribute experiment**: Report the fraction of attributes for which the method outputs the correct causal attribute versus a spurious correlate (especially gender). Discuss whether this is a fundamental limitation or can be addressed.

4. **Provide reproducibility essentials in an appendix**: Release the GPT-4 prompts, report λ, m (images per iteration), max depth, relevance threshold, and compute costs (API calls, runtime).

## Score and Decision

The paper introduces a novel and practically motivated framework for domain forensics, supported by strong quantitative results on CIFAR-10, Places365, and a model-cloning task. However, the evaluation has notable gaps: the objective function is overclaimed (used only at termination, not during search), the baseline comparison is underspecified, there is no ablation isolating the contribution of key components, and critical implementation details are missing. These issues are real but not fatal — the core empirical results on the main evaluation tasks are strong enough to merit acceptance with major revisions. The paper would benefit from calibrating its claims to match the algorithm, adding ablations, and improving reproducibility documentation.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>