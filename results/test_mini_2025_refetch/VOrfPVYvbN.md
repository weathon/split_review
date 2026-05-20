Now I have all the information needed. Let me write the final consolidated review.

## Summary

This paper proposes Domain Bridge, a method for discovering the input data domain of black-box classifiers by iteratively searching over textual descriptions. The search loop works as follows: starting from a broad description, Stable Diffusion generates images, which are classified by the target model; correctly classified images are re-encoded into textual descriptions via CLIP/BLIP, and LLM components (Summarizer, Grouper, Enricher) refine these descriptions for the next iteration. On Places365, the method identifies 360/365 classes versus 159/365 for the prior corpus-based baseline. The approach is novel — using generative models as an expandable search space for forensic domain discovery — and the main result is compelling.

## Strengths

- **Massive coverage improvement over corpus-based baselines.** On the Places365 target model, the proposed method identifies 360 out of 365 classes (98.6%), compared to only 159 (43.6%) for the prior corpus-based approach (Zhang et al., 2023) using ImageNet (Table 2, Section 6.2). This more-than-doubling of coverage is direct evidence that the generative search space overcomes the fixed-category limitation of static datasets.

- **Demonstrates fine-grained attribute discovery on CelebA.** On a 40-attribute face classifier, the method recovers interpretable textual descriptions for most attributes (e.g., "Balding" → "man, receding hairline", "Smiling" → "person, smiling") and even reveals target model biases — the "No_Beard" attribute triggers on "man, tie and shirt" rather than on facial features alone (Table 4, Section 6.4). No prior black-box domain-forensic method has shown this level of attribute-level resolution.

- **Generated data enables effective model cloning.** When 5,000 images from the method's descriptions are used for cloning (GoogLeNet), the clone achieves 84.8% accuracy versus 35.5% for the corpus-based approach and 81.3% for a subset of original CIFAR-10 images (Table 3, Section 6.3). This validates that the recovered descriptions capture class-relevant visual features.

- **Real-world validation on Hugging Face models.** The method correctly identifies the domain of a pneumonia chest X-ray classifier, a brand-specific shoe classifier (Nike/Adidas/Converse), and 97/100 food classes including fine-grained ones like "deviled eggs" (Section 6.5), demonstrating practical applicability.

## Weaknesses

### Fatal

None.

### Major

- **CelebA experiment has no quantitative evaluation.** Table 4 is purely qualitative — there is no success rate, no ground-truth mapping from attribute name to acceptable textual description, no inter-annotator agreement, and no countable hit rate. The paper claims the method "successfully identifies" attributes, but this cannot be assessed without a measurable criterion. Some results are ambiguous (e.g., "Big_Nose" → "sims 4" is presented as an interesting finding about generative model biases, but does it count as a correct identification?). Without a quantitative metric, this experiment — which is the primary support for the paper's claim of fine-grained attribute discovery — provides only anecdotal evidence.

- **Critical hyperparameters and implementation details are missing, compromising reproducibility.** The search algorithm involves several parameters that are named but never given concrete values: number of images per node (*m*), maximum tree depth, verbosity threshold for summarization, number of summarization variants (*l*), the regularization weight *λ* in the objective function (Equation 1), and the exact LLM prompts for the Description Summarizer, Grouper, and Enricher (all three of which use GPT-4 via API). Without these details, the method cannot be independently reproduced, and the sensitivity of results to these choices cannot be assessed.

- **No ablation studies of the core components.** The pipeline contains five components (Description Decoder, Image Encoder, Summarizer, Grouper, Enricher), three of which are LLM-mediated modules with unverified contributions. There is no ablation removing the Summarizer, Grouper, or Enricher to measure their individual impact. Consequently, it is impossible to determine which components drive the observed performance or whether the pipeline could be simplified.

- **The objective function's generality term (Equation 1) is neither ablated nor parameterized.** The paper formulates *V*(*e*) = relevance − *λ*·generality as a principled objective, but *λ* is never reported and there is no comparison of results with versus without the generality penalty. The function is applied only at termination (Step 11) to select among candidates, while the search itself uses only relevance (*k/m*) for pruning and tree expansion. The claimed methodological contribution of a "joint relevance-generality objective" is therefore unsupported by any empirical evidence.

### Minor

- **The baseline comparison conflates search-space scale with the iterative mechanism.** The paper compares against a corpus-based method (Zhang et al., 2023) that searches over ImageNet's 1,000 categories, while the proposed method uses Stable Diffusion (trained on LAION-5B) which provides a far larger search space. The resulting improvement (360/365 vs. 159/365) could be largely due to the scale of the generative model's latent space rather than the iterative refinement loop. An additional baseline using the same generative model but with static (non-iterative) search over a large fixed set of descriptions would isolate the contribution of iterative feedback.

- **No statistical variance is reported.** All experiments appear to be single runs with no confidence intervals or error bars. The cloning result in Scenario 4 (95.2% accuracy, exceeding the target model's 94.9%) is particularly striking and would benefit from multiple seeds to establish whether this is a reliable finding or statistical noise.

- **Computational cost is not quantified.** The paper mentions efficiency as a concern (Section 6.6) but provides no concrete numbers: how many Stable Diffusion generations were required per class? How many GPT-4 API calls? This information is essential for practitioners evaluating the method's feasibility.

### Trivial

- Table 4 lists "5_o_Clock_Shadow" as an attribute; this formatting artifact persists from the CelebA dataset naming convention.

## Nice-to-Haves

- An ablation comparing search with and without the Description Enricher, to test whether LLM-based enrichment adds value over simply generating more images from existing descriptions.
- Analysis of why the cloning result (Scenario 4) exceeds target model accuracy — e.g., whether generated images are "canonical" views that are easier to classify, or whether the specific GoogLeNet architecture benefits from particular generated image characteristics.
- Computational cost analysis (total generations, API calls) for the main experiments.

## Removed Points

These points from the inputs were flagged for removal, with brief justifications:

- *"The baseline comparison is constructed to guarantee victory"* — Overstated framing. The paper's contribution is the whole pipeline (generative model + iterative search), and comparing against the prior corpus-based approach is legitimate as a system-level comparison. The missing control (same generator without iteration) is retained as a Minor weakness above, but the characterization of deliberate unfairness is removed as unsupported.

- *"The cloning experiment produces suspiciously strong results... data contamination"* — The speculation that generated images "accidentally resemble CIFAR-10 test set images" is unsubstantiated and reflects reviewer speculation, not a verified problem. The striking nature of the result is acknowledged in the Minor weakness about missing variance, but the framing as "extraordinary claim" requiring "error analysis" for a relatively small gap (95.2% vs. 94.9%) on a simple dataset like CIFAR-10 is inflated. Stable Diffusion generating cleaner canonical views is a plausible explanation.

- *"Section 6.5 (Hugging Face evaluation) is too brief"* / *"The pneumonia detector results are not quantified"* — This section is described as a real-world demonstration, not a rigorous benchmark. The paper transparently reports what it found (method could not distinguish positive from negative pneumonia classes). Criticizing it for not being a full-scale evaluation exceeds the section's stated scope.

- *"No discussion of failure modes"* / *"The self-correcting effect is not empirically demonstrated"* — These are reasonable suggestions but function as "nice-to-have" scope extensions rather than specific weaknesses. The paper does discuss convergence to local optima and generative model biases (Sections 6.4, 6.6). The self-correcting mechanism is described as a property of the algorithm's design (correct descriptions cascade, wrong ones die out), not as a separate empirical finding.

- *Various formatting criticisms, missing appendix, missing related works* — Removed per hard rules (parser artifact, parsers strip appendices, cannot confirm missing related works without external sources).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add a control baseline** that uses the same Stable Diffusion backbone but generates images from a large fixed set of descriptions (e.g., 10,000 LAION captions) without iterative refinement. This would isolate whether the improvement comes from the generative model's scale or the iterative feedback loop.

2. **Turn the CelebA experiment into a quantitative evaluation** by defining an acceptable output for each attribute (e.g., via manual labeling or synonym sets) and reporting accuracy and top-5 accuracy.

3. **Report all hyperparameters and make LLM prompts available** in an appendix: *m*, maximum tree depth, verbosity threshold, *l*, *λ*, and the exact prompts for the three LLM components.

4. **Ablate the three LLM components** (Summarizer, Grouper, Enricher) by running the search without each one in turn and reporting how domain coverage changes.

5. **Report variance** by running the main experiments (CIFAR-10 domain identification, Places365, cloning) with multiple random seeds.

6. **Report computational cost** — total Stable Diffusion generations, total GPT-4 calls, and approximate wall-clock time for the CIFAR-10 and Places365 experiments.

---

## Score and Decision

**Calibration anchors summary:**

| Path | Avg Score | Round | Comparison |
|------|-----------|-------|------------|
| 0rS9o1uKqu (TLDR reconstruction) | 2.50 | R1-low | Much weaker — methodologically flawed, less novel |
| XQFSIdKMhJ (Vehicle generative AI) | 2.50 | R1-low | Much weaker — poorly motivated, weak experiments |
| GYHF2OfyWP (Black-box attacks FL) | 3.00 | R1-low | Much weaker — narrower contribution, weak evaluation |
| 1i6lkavJ94 (Conformal generative) | 6.25 | R1-mid | Stronger — has theoretical grounding and clear experimental validation |
| CF8H8MS5P8 (Generative AI paradox) | 7.00 | R1-mid | Stronger — thorough experiments, well-executed study |
| 1ZAqAmK6BM (Tabular generative) | 5.25 | R1-mid | Similar — creative idea but evaluation gaps |
| yBmMgvaEtO (Stochastic black-box opt) | 5.00 | R2 | Similar — novel formulation but weak empirical validation, rejected |
| hIKsem01M5 (PRISM prompt engineering) | 5.00 | R2 | Similar — iterative T2I+LLM paradigm, similar missing ablations, rejected |
| x31F1VmiV7 (BSPA prompt attacks) | 5.25 | R2 | Slightly weaker — creative attack but limited evaluation |
| 12Acp6ZcRa (T2I robustness eval) | 5.50 | R2 | Similar — solid evaluation framing but missing key controls |
| 1SbkubNdbW (Label smoothing & inversion) | 6.20 | R2 | Stronger — thorough experiments despite some gaps, accepted |
| s8cMuxI5gu (Gradient inversion) | 7.00 | R2 | Stronger — clean method, solid experiments, accepted |

**Round 1 bracket:** Between approximately 3.5 and 7.0.

**Round 2 narrowing:** Compared against topically similar papers at 5.0–6.2. The paper's novel application domain (domain discovery/forensics) distinguishes it from PRISM (5.0) and BSPA (5.25), but its evaluation gaps (missing ablations, no quantitative CelebA metrics, unreported hyperparameters) are more severe than the label smoothing paper (6.2) or gradient inversion paper (7.0). The paper sits between the PRISM/BSPA cluster and the label smoothing paper.

**Final score:** 5.5 — the idea and main result are genuinely novel and the Places365 result is strong, but the evaluation has multiple clear gaps (no CelebA quantification, no ablations, missing hyperparameters) that prevent the paper from meeting the acceptance bar for a top venue in its current form. The paper would benefit substantially from addressing the Major weaknesses above.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>