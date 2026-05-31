## Human Reviewer 1

### Summary
The paper proposes ScaPre, a training‑free, closed‑form framework to erase many target concepts from text‑to‑image diffusion models while preserving quality on non‑targets. It stabilizes multi‑concept edits via a spectral trace regularizer (second‑order target statistics plus an SVD‑based overlap regulator), improves precision with a mutual‑information–guided "Informax Decoupler", and preserves global structure through Bures‑geometry alignment; the quadratic part reduces to a Sylvester system solved in one shot. On Stable Diffusion v1.4/1.5, ScaPre achieves state‑of‑the‑art large‑scale forgetting, e.g., Imagenette residual accuracy 0.8 (Table 1), Diversi50 3.9 (Table 3), Confuse5 overall 84.3 (Table 4), and unlearns 50 concepts in $\sim$120 s on an A6000 (Fig. 3), while claiming up to x5 more concepts than baselines.

### Strengths
- Conflict‑aware spectral trace regularizer + SVD overlap control; MI‑guided channel reweighting; Bures‑alignment for geometry‑aware stability.

- Convex quadratic core with unique Sylvester solution; clear derivations and proximal mapping.

- Best residual accuracy/UQ on Imagenette, Diversi50, and Confuse5 with robust visuals.

- 50‑concept unlearning in $\sim$120s; low memory/time vs. baselines (Fig. 3).

### Weaknesses
- Construction of "target/neutral" inputs, threshold choice, and variance of MI estimates need clarification.

- Heavy use of classifier‑based "unlearn accuracy" and CLIP; limited human/adversarial prompt evaluation.

- Results limited to SD v1.4/1.5; unclear portability to SDXL/DiT architectures.

- Deeper, main‑text ablations of S vs. R vs. Informax vs. geometry step and sensitivity of UQ's normalization would strengthen claims.

### Questions
- How are "target" and especially "neutral" inputs instantiated for MI estimation without extra data? What sample size/thresholding is used, and how stable are channel scores across layers?

- Which cross‑attention layers/branches (K vs. V) are edited, and how does performance vary layerwise?

- Can you show results on SDXL/DiT to illustrate architectural generality or required modifications to S and R?

- Do you test robustness to synonyms/negation/compositional prompts or other circumventions (e.g., multilingual)? A breakdown would substantiate "precise" forgetting.

### Soundness
4

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper proposes ScaPre, a closed-form framework for scalable and precise concept unlearning in text-to-image diffusion models.
It addresses three challenges in large-scale unlearning: conflicting weight updates, imprecise forgetting causing collateral damage, and inefficiency from auxiliary modules.

### Strengths
1. The empirical validation is good, for example, ScaPre achieves the lowest unlearning accuracy on Imagenette while maintaining high CLIPcoco, outperforming other baselines.

2. The algorithm is innovative and lightweight. The closed-form solution avoids iterative fine-tuning, and geometry alignment via Bures distance preserves global covariance structure better than L2 regularization. Also, the Informax Decoupler is reasonable.

3. The benchmark construction. ImageNet-Confuse5 explicitly tests disentanglement of visually similar concepts (e.g., dog breeds), a realistic and challenging setting absent in prior work.

### Weaknesses
1.  Some notation is ambiguous. For example, The symbol W is used for both the updated matrix and intermediate solution W⋆ without distinction in Sec. 4.3 (see Eq. (8)–(10)). In Appendix B.1, Eq. (11) redefines the objective with A = λI + S+R and B = diag(α), but these symbols are not introduced in the main text, breaking continuity.

2. Random seeds, data splits for ImageNet-Diversi50/ImageNet-Confuse5, and prompt selection criteria are omitted (see Sec. 5.1), hindering replication.

3. Fig. 3 reports GPU-hours and memory but omits per-concept scaling trends (e.g., time vs. number of concepts), critical for “scalable” claims (see Sec. 5.5).

### Questions
Please introduce A and B in the main text when first used in Eq. (8), aligning with Appendix B.1 notation.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
To address the challenges of conflicting weight updates, collateral damage to non-target concepts, and reliance on extra data in large-scale concept unlearning for text-to-image diffusion models, this paper proposes ScaPre (Scalable-Precise Concept Unlearning), a unified lightweight framework aiming for scalable and precise unlearning.
ScaPre integrates a conflict-aware stable design (spectral trace regularizer + geometry alignment) and an Informax Decoupler, achieving an efficient closed-form solution without extra data/sub-models; experiments show it can unlearn up to 5× more concepts than the best baseline while maintaining high generation quality.

### Strengths
The paper innovatively combines a conflict-aware stable design and an Informax Decoupler, which effectively solves the core problems of instability in large-scale unlearning and imprecise separation of target/non-target concepts, making up for the shortcomings of existing methods in large-scale scenarios.

ScaPre adopts a closed-form solution, ensuring high efficiency (unlearning 50 concepts in 120 seconds) and reproducibility without extra data or auxiliary modules; meanwhile, its experiments cover objects, styles, and explicit content benchmarks, with comprehensive and convincing results.

### Weaknesses
1. Experimental benchmarks are mostly ImageNet-derived datasets (e.g., Imagenette, ImageNet-Diversi50), lacking evaluations on more complex and diverse real-world scenarios (e.g., dynamic concepts, cross-modal associated concepts), making it hard to verify the method’s practical generalization.

2. It is suggested to explore ScaPre’s adaptability and performance changes on larger diffusion models (e.g., Stable Diffusion XL). 

3. It is suggested that the authors enhance and enrich the elaboration of the overview figure in this paper, as the current description of this figure is too simplistic, omits many details, and makes it difficult for readers to understand.

4. In the proposed Imagenette benchmark, it is not explicitly specified what prompts are used for evaluation and whether these prompts are merely category names; thus, it is suggested that the authors use more complex prompts to evaluate the impact of prompts on the experimental results.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
The paper addresses a challenge of large-scale concept unlearning in text-to-image diffusion models. While existing approaches can remove individual concepts, they struggle when scaling to multiple concepts simultaneously, facing issues with conflicting weight updates, imprecise unlearning boundaries, and computational scalability bottlenecks.

### Strengths
1. The paper is well-structured and easy to follow
2. While the majority of other algorithms fine-tune the the entire model weights
3. Addresses fundamental challenges through theoretically grounded components
4. Comparison with other methods on a large-scale multi-concept unlearning (up to 50 concepts)
5. Extensive appendix with math proofs and detailed results

### Weaknesses
1. No comparison with parameter efficient Unlearning methods (e.g., SEMU https://arxiv.org/abs/2502.07587)
2. It would be beneficial to have the data from figure 3 in a from of a table in the appendix
3. Based on the theoretical foundation the method should also work on other SOTA models (e.g., SDXL, Stable Diffusion 3.5, FLUX.1-dev, Qwen-Image); however, no experimental confirmation is presented in the paper

### Questions
see Weaknesses section

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
2