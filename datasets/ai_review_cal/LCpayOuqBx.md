- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 8, 3
Now I have a thorough understanding of the paper and can verify the reviewer claims against the source material. Let me compose the final consolidated review.

## Summary

This paper proposes DOS (Dreaming Outlier Semantics), a zero-shot OOD detection method that leverages LLMs to generate candidate outlier class labels based on visual similarity to ID classes, then uses a proportional scoring function to distinguish ID from OOD samples. The core idea is that adding these "dreamed" outlier labels to CLIP's text classifier improves separation without accessing any actual OOD data. The method is evaluated across far, near, and fine-grained OOD detection tasks and achieves strong results on multiple benchmarks.

## Strengths

1. **Novel and well-motivated paradigm**: The idea of using LLM knowledge to hallucinate plausible outlier categories for OOD detection (Section 3.1) is original and cleanly motivated by the finding that adding actual OOD labels dramatically improves CLIP-based OOD detection (Figure 1). This bridges LLM world knowledge and VLM-based OOD detection in a practical, training-free way.

2. **Strong empirical results across diverse settings**: DOS achieves average FPR95 of 0.21% and AUROC of 99.93% on far OOD (Table 1), 1.80% average FPR95 improvement over MCM on near OOD (Table 3), and 7.12% average FPR95 improvement on fine-grained OOD (Table 4). These results are consistently strong across four ID datasets and three OOD task types.

3. **Well-designed ablations supporting core components**: The paper ablates the score function (Figure 6a), showing S_DOS outperforms MaxSoftmax, MSP, Energy, and MaxLogit alternatives. It ablates prompt design (Figure 6b), confirming the "visually resemble" constraint is critical. It tests across LLMs (GPT-3.5, LLaMA2-7B, Claude2) showing generalizability (Figure 6c). And it tests sensitivity to the number of outlier labels L (Figure 7).

4. **Zero-shot without auxiliary training or data**: Unlike CLIPN (which requires an extra dataset and text encoder) and ZOC (which requires a text-based image description generator), DOS requires no additional training or auxiliary data — only ID labels and an off-the-shelf LLM. This is a genuine practical advantage.

## Weaknesses

### Major

- **No analysis of overlap between LLM-generated classes and OOD test classes.** The paper checks that generated labels don't overlap with ID classes (Section 3.1, near OOD: "Overlapping classes in V_dood with V_id are removed by string matching"), but does not check overlap with the *actual OOD test classes*. This is concretely concerning:
  - **Fine-grained OOD** (CUB-200, Stanford-Cars, etc.): Half of classes are held out as OOD. The LLM is prompted to "provide different subclasses within the same major category." Since the LLM knows the domain (e.g., bird species from CUB-200), it could easily generate OOD half-classes. If so, those "dreamed" labels are not true proxies — they are the actual test classes.
  - **Near OOD** (ImageNet-10 → ImageNet-20): The LLM is asked for classes "visually resembling" each ID class. ImageNet-20 was constructed with semantically similar classes (dog vs. wolf). The generated "wolf" for ID "dog" directly matches the OOD test label.
  
  While this doesn't constitute "data leakage" in the traditional sense (the LLM isn't trained on these test sets), it conflates two factors: the method's general mechanism vs. coincidental overlap with the held-out OOD labels. Without overlap analysis, the reader cannot determine how much of the reported gain would persist under a different OOD split where overlap is absent. This is the single most important gap in the evaluation.

### Minor

- **Task-specific prompts vs. claimed generality.** The paper provides three distinct prompts for far, near, and fine-grained OOD (Section 3.1), and claims DOS is "OOD-Agnostic" (Section 3.2, point 1). However, choosing which prompt to use requires knowing the *type* of OOD you expect. In a truly open-world scenario where far, near, or fine-grained OOD could appear unpredictably, a single prompt is needed. The ablation (Figure 6b) showing performance degradation with "visually irrelevant/dissimilar" prompts reinforces that prompt choice matters. The paper should either disclaim this limitation or propose a unified prompt.

- **SOTA claim needs clearer qualification.** The abstract and introduction state "achieves new state-of-the-art performance" without qualification. However, on ImageNet-1K with ViT-B/16 (Table 2), CLIPN outperforms DOS. The paper dismisses this as unfair because CLIPN uses extra training data — a valid caveat — but the unqualified SOTA claim in the abstract is misleading. The claim should be explicitly scoped to "zero-shot methods without additional training data" or similar.

- **No ablation or sensitivity analysis on β = K/(K+L).** The score function introduces β as a weighting factor for outlier class contributions (Section 3.2). The paper states β "indicates the proportion between outlier and ID class labels" but provides no sensitivity analysis. Varying β across a grid (e.g., 0.1, 0.3, 0.5, 0.7, 0.9, 1.0) would show whether the specific functional form matters or whether simply adding outlier classes to the softmax denominator (β=1) already accounts for most of the gain. Without this, the contribution of the β design is unclear.

- **No error bars or variance estimates in main results.** The paper reports averaging three independent runs in the setup (Section 4.1), but the main results tables (Tables 1-4) and key figures do not show standard deviations or confidence intervals. This makes it impossible to assess whether differences between methods are statistically significant, particularly in near-OOD where margins are small (e.g., 1.80% FPR95 improvement).

### Trivial

- None that warrant listing beyond what has been described — the paper is well-written and the presentation is clean.

## Nice-to-Haves

- Quantifying the oracle upper bound (CLIP's performance with actual OOD labels) as mentioned in the motivation (Figure 1b) would give readers a clear reference ceiling.
- A mixed-OOD evaluation using a single prompt would strengthen the generality claim.
- An analysis of why different LLMs (Claude2 vs GPT-3.5) produce different quality outlier classes (Figure 6c) could provide actionable insights.

## Removed Points

These points are flagged to be removed; treat them with caution:

- *"No ablation on prompt phrasing (e.g., different wordings of the visual similarity prompt)"* — The paper already ablates prompt types (visually similar vs irrelevant vs dissimilar) in Figure 6b, which is a more meaningful comparison than surface-level wording variations.
- *"The paper does not quantify what FPR95/AUROC CLIP achieves with oracle OOD labels"* — This is a nice-to-have, not a weakness. The motivation is qualitative (Figure 1).
- *"Near OOD on ImageNet-10/20 is small-scale"* — This is the standard benchmark established by MCM (Ming et al., 2022). Following community conventions is not a weakness.
- *"Claude2 outperforms GPT-3.5-turbo but not analyzed"* — The purpose of this ablation is to show generalizability across LLMs, not to compare LLM quality. The result is reported as evidence that the method works with different LLMs, which is sufficient.
- *Parser artifact notes (e.g., "β =KK+L . A.")* — These are formatting artifacts from the PDF extraction, not author errors.

## Novel Insights

The harsh critic raised the overlap concern, but treating it as a "structural/fatal" issue overlooks an important nuance: even if overlap occurs, it doesn't mean the method is "not truly zero-shot" in the way that, say, training on OOD data would be. The LLM is drawing on general world knowledge, not on the specific OOD test set. The real question is whether overlap inflates the reported numbers. Separately, the Strength Finder correctly identifies the paper's main contribution: using LLMs to hallucinate plausible visual alternatives to ID classes is a genuinely new technique that differs meaningfully from "classification by description" methods (Menon & Vondrick, 2023) and from methods that generate "NOT ID" labels (ZOC, CLIPN). The paper's strongest evidence is not any single number but the consistent pattern of improvement across far, near, and fine-grained tasks, which would be hard to explain by overlap alone.

## Suggestions

1. **Address the overlap gap directly.** For each experimental setup: (a) list the generated outlier classes, (b) compute overlap with OOD test classes (exact string match and semantic similarity), and (c) re-run the evaluation with overlapping classes removed. If performance degrades only modestly, the core claim is validated.
2. **Qualify the SOTA claim** in the abstract and introduction to reflect the comparison with CLIPN fairly.
3. **Add a β sensitivity analysis** across a grid (e.g., 0.1, 0.3, 0.5, 0.7, 0.9, 1.0) to show whether the specific functional form matters.
4. **Add error bars** to the main results tables to support significance claims.
5. **Acknowledge the prompt limitation** — the current design requires knowing the OOD type in advance — and discuss potential mitigations (e.g., a single unified prompt or ensemble).
