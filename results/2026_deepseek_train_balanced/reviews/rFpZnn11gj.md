## Summary

The paper introduces PathGen-1.6M, a dataset of 1.6 million pathology image-text pairs generated from TCGA whole-slide images via a multi-agent collaboration pipeline. The pipeline combines prompt-based CLIP retrieval and clustering for patch selection, then uses trained LMM agents for description generation, revision, and summarization. Models trained on this data (PathGen-CLIP, PathGen-CLIP-L, PathGen-LLaVA) achieve substantial improvements across zero-shot classification, WSI classification, and multimodal understanding benchmarks, including surpassing GPT-4V on PathMMU.

---

## Strengths

- **Large and well-sourced dataset with strong empirical payoff.** PathGen-1.6M is currently the largest pathology image-text dataset, built from 7,300 TCGA WSIs across 27 tissue types. PathGen-CLIP-L achieves 79.7% average zero-shot accuracy across 9 datasets, a 13.5-point improvement over the prior best (PathCLIP at 66.2%), and PathGen-CLIP (ViT-B) already exceeds PathCLIP by 8.1 points (Table 1). These gains are large, consistent, and unlikely to arise from noise.

- **Clean WSI evaluation design.** The WSI classification experiments (Table 2) explicitly exclude TCGA-derived test sets (CAMELYON16, CAMELYON17, BRACS), avoiding direct training-test leakage. The improvements are substantial: e.g., PathGen-CLIP-L achieves 92.6 average AUC with ACMIL vs. the next best 87.2 (PLIP). This is the cleanest evidence that the dataset provides genuinely transferable features.

- **PathGen-LLaVA achieves strong results on PathMMU.** The LMM trained on PathGen data achieves 58.4% overall accuracy vs. GPT-4V's 49.8% and Quilt-LLaVA's 41.5% (Table 3), demonstrating that the generated dataset and vision backbone support effective multimodal reasoning.

- **Two-stage training strategy is principled.** Training first on PathGen-1.6M (morphological descriptions) then fine-tuning on PathGen$_{init}$ (diagnostic information from curated sources) is a sensible design acknowledged in the paper (Section 4.1), with ablation in supplementary materials.

- **Scalable methodology.** The pipeline of extracting representative patches from existing WSI archives and generating captions via trained LMMs offers a repeatable template for expanding pathology VL datasets, addressing a real scalability bottleneck in the field.

---

## Weaknesses

### Fatal
None.

### Major
- **Missing comparison with CONCH — the most directly relevant prior pathology CLIP model.** CONCH (Lu et al., 2024) is cited in the related work (line 35) as a pathology-specific CLIP model, yet appears in none of the evaluation tables: not in zero-shot classification (Table 1), WSI classification (Table 2), or few-shot experiments. CONCH is trained on ~1.2M pathology image-text pairs generated from reports — the same paradigm this paper pursues. Without this comparison, the claimed "SOTA" status is unsubstantiated against the closest competitor, and the reader cannot assess whether gains come from the multi-agent pipeline or simply from using more data from TCGA. This is the single most consequential omission.

- **No direct evaluation of caption quality.** The paper's central methodological contribution is a multi-agent pipeline designed to generate *high-quality* captions. Yet the captions themselves are never evaluated — no human rating, no automated metric (CIDEr, BLEU, CLIPScore, or pathology-specific measures), no error analysis of the revision agent's corrections, and no analysis of information loss in the 77-token summarization bottleneck. Downstream CLIP performance is an indirect signal that conflates caption quality with data scale (1.6M vs. ~700K in existing sets), image diversity (7,300 WSIs), and training recipe. The causal claim "better captions → better CLIP" is asserted but not demonstrated. For a paper titled around data generation, this is a fundamental evidential gap.

- **No ablations of the data generation pipeline components.** The pipeline has four distinct design choices: (1) prompt-based retrieval + clustering for patch selection, (2) a Description LMM, (3) a Revise LMM, and (4) a Summarizer. None are ablated. The sole ablation mentioned (line 101) addresses CLIP training-stage order, not the generation pipeline. Without ablations, the reader cannot determine whether the revision agent improves quality, the summarizer discards useful information, prompt-based retrieval adds value over clustering alone, or a simpler approach (e.g., directly prompting GPT-4V to caption each patch) would perform as well. This makes the pipeline feel ornamental rather than empirically necessary.

### Minor
- **Bootstrapping from the same limited sources.** The Description LMM agent (PathGen-LLaVA$_{desp}$) is trained on 30K GPT-4V-enhanced captions drawn from PathCap, OpenPath, and Quilt-1M — the same three sources used to train PathGen-CLIP$_{init}$ (lines 57, 61). While not circular, this bootstrapping means the description generator inherits the limitations (e.g., simplistic captions, misalignment) the paper criticizes in these sources. The degree to which GPT-4V enhancement overcomes these limitations is not analyzed.

- **Organ-level distribution overlap may inflate zero-shot results.** LC-Lung and LC-Colon (Table 1) are from the same organ sites (lung, colon) heavily represented in TCGA, which accounts for most of the 13.5-point average gain. The paper does not discuss whether this organ-level overlap inflates results on these specific datasets.

- **No tissue-type distribution provided.** The dataset spans 27 tissue types (line 85), but no breakdown is reported. The reader cannot assess whether certain tissue types dominate, which would affect conclusions about generalization.

- **Unvalidated revision agent training.** The revise agent is trained on GPT-4-introduced errors (additions, deletions, modifications) that may not match the error distribution of the Description LMM. No analysis is provided of what kinds of errors are actually corrected in practice or whether corrections are beneficial.

- **Heuristic clustering parameter.** The choice k = sqrt(number of patches) for k-means clustering is stated without justification or sensitivity analysis (line 72).

### Trivial
None.

---

## Nice-to-Haves

- A tissue-type or organ-site breakdown of the 1.6M pairs would help assess data bias and its relationship to downstream task performance.
- Sensitivity analysis on the 0.88 similarity filtering threshold and the sqrt(k) heuristic would increase confidence in the patch extraction design.
- Reporting whether the same training/test protocol was used for all compared models (e.g., same prompt templates for zero-shot) would improve fairness assessment.

---

## Removed Points

The following points raised by the reviewers were removed or downgraded:

- **"Circular reliance on same data sources the paper argues are insufficient"** (Harsh Critic): Downgraded to Minor (see above). The paper argues existing sources have quality/scale limitations but still uses them for bootstrapping — a common and reasonable practice, not a circular flaw. The criticism as originally phrased ("circular reliance") overstates the problem.

- **"No discussion of potential ethical concerns or failure modes"**: Removed. Demanding clinical-risk discussion from a dataset/methodology paper exceeds the paper's stated scope. This is not standard practice for this type of contribution.

- **"First large version of CLIP claim is contestable"** (Harsh Critic): Removed. Whether PathGen-CLIP-L is technically the "first large ViT-L" pathology CLIP is a minor nomenclature point that does not affect the paper's contribution.

- **"Evaluation of PathGen-LLaVA surpassing GPT-4V is overstated"** (Harsh Critic): Removed. The paper's framing is slightly enthusiastic but not unreasonable — a pathology-specific model beating GPT-4V by 8.6 points on a pathology benchmark is genuinely noteworthy, even if "expected."

- The Strength Finder's generic claim about the paper "addressing an important problem" was removed as superficial and lacking specific evidence.

- The Strength Finder's "dedicated revision agent for self-correction" is a real design feature but is retained only as indirectly evidenced, as no direct validation of the revision agent's efficacy exists.

---

## Novel Insights

A notable pattern across the reviews is the tension between the paper's framing and its evidence. The paper frames its primary contribution as a *multi-agent pipeline that generates high-quality captions*, but the evidence most strongly supports a different claim: *training on TCGA-derived data at scale improves downstream pathology models*. The downstream gains are large and well-measured, but the mechanism — whether the multi-agent pipeline, the data scale, the image quality of TCGA patches, or the diversity of tissue types drives these gains — is never isolated. This asymmetry between the headline claim and the strongest evidence is the paper's central weakness. The paper would be more convincing if it either (a) directly validated the caption quality, or (b) reframed the contribution around the dataset and its demonstrated utility, treating the pipeline as a reasonable approach rather than a validated innovation.

---

## Suggestions

1. **Add CONCH to all evaluation tables.** This is the most impactful single improvement. Without it, the paper's SOTA claims are incomplete against the closest competitor. If CONCH cannot be run on the exact same setup, a detailed comparison citing published results and clarifying any differences in evaluation protocol would be a reasonable substitute.

2. **Include a direct evaluation of caption quality.** At minimum: (a) sample 200–500 image-caption pairs and have domain experts (or trained annotators) rate accuracy and informativeness, comparing PathGen captions against Quilt-LLaVA and/or GPT-4V captions; (b) report automated CLIPScore or similar between images and captions; (c) analyze the revision agent's corrections qualitatively — what fraction improve vs. degrade the caption? This directly addresses the weakest link in the evidence chain.

3. **Ablate the pipeline components.** Train PathGen-CLIP with: (i) no prompt-based retrieval (clustering only), (ii) no revision step, (iii) no summarization (truncate raw descriptions), (iv) random patch selection. If the full pipeline outperforms all variants, this validates the design. If not, the paper should honestly report which components matter and which are dispensable.

4. **Report tissue-type distribution** of PathGen-1.6M across the 27 types. Ideally, also break down zero-shot results by whether the test organ site appears in the training data.

5. **Tone down causal claims** about caption quality-driving performance unless direct caption evaluation is included. The paper's empirical contributions (dataset, model improvements) stand on their own even without claiming optimality of the generation pipeline.

---

## Score and Decision

This paper has substantial empirical contributions — the PathGen-1.6M dataset, PathGen-CLIP's consistent and large gains across multiple benchmarks, and PathGen-LLaVA's strong PathMMU results are real and valuable. However, for a top-tier venue like ICLR, three major gaps prevent acceptance: (1) the omission of CONCH from all comparisons undermines the SOTA claim against the most relevant prior model; (2) the core methodological claim about caption quality via multi-agent collaboration is never directly validated; (3) the pipeline lacks ablations that would substantiate its design choices. These issues are addressable but require substantial additional work. The paper presents promising results that would likely be competitive after strengthening.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>