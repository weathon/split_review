Now I have all the verification I need. Let me synthesize the final consolidated review.

---

## Summary

This paper introduces LayoutSciPG, a new task for layout-aware scientific poster generation from papers, and contributes two main resources: (1) SciPG, a large-scale dataset of 11,302 paper-poster pairs collected from conference proceedings, which is an order of magnitude larger than prior datasets (≤300 pairs); and (2) a multimodal extractor-generator framework, where a RoBERTa+BiLSTM extractor selects key text/image elements and a BART-based interactive generator with an adaptive memory mechanism jointly paraphrases content and predicts layout bounding boxes. Experiments using ROUGE, image precision/recall, and layout metrics show improvements over an adapted slide-generation baseline (AdaD2P), with ablation studies confirming the value of the adaptive memory module.

## Strengths

1. **Large-scale dataset (SciPG)**: The paper constructs 11,302 paper-poster pairs from CVPR, ICML, NeurIPS, and ICLR — an order of magnitude larger than prior datasets (≤300 pairs, per Table 1). This directly addresses the data scarcity problem that has limited data-driven poster generation research and is the paper's most valuable contribution.

2. **Adaptive memory mechanism shows clear empirical benefit**: Table 6's ablation study demonstrates that removing the memory module causes the largest decline in layout performance, and the proposed adaptive memory outperforms standard RMT memory. This is supported by parameter sensitivity analysis (Figure 2) showing memory size 50 is optimal, providing concrete evidence that the mechanism addresses long-sequence challenges.

3. **Quantitative gains over the only comparable baseline**: Table 4 reports that the proposed method improves over AdaD2P by +6.29% in ImgP and +6.81% in ImgR for image outputs, and by +22.36% in Overlap and +25.05% in Coverage for layout. Table 3 also shows the extractor outperforms NeuralExt, MSMO, and AdaD2P's extraction module.

4. **Generalization across conferences**: Table 7 shows that training on all topics outperforms per-conference training on text (R-1: 44.43 vs. best single-topic 42.16) and layout metrics, indicating the learned representations transfer across subdomains.

5. **Systematic ablation and parameter tuning**: Table 6 ablates KL-divergence, pretraining, data extension, and three memory variants. Figure 2 sweeps memory size and KL weight. These provide sound empirical justification for the design choices.

## Weaknesses

### Major

1. **Dataset alignment pipeline is not described, making the training signal unverifiable.** The paper states (lines 22, 69) that it "explicitly align[s] elements of each paper with its corresponding poster" and "automatically extract[s] text and image elements from documents and posters and perform[s] matching," but provides zero details on the alignment algorithm, its accuracy, or its failure modes. Every supervised component — the extractor (which sentences/images to select) and the generator (paraphrase targets and layout coordinates) — derives its training signal from this alignment. Without knowing how matching is performed (caption overlap? spatial proximity? learned embeddings?), the entire experimental pipeline is a black box and the work cannot be reproduced. This is the single most critical missing piece.

2. **The evaluation measures poster reconstruction, not paper-to-poster generation.** The paper's stated task is generating a poster *from the paper*, yet both automatic metrics (ROUGE against ground-truth poster text, ImgP/ImgR against ground-truth poster images, layout metrics against ground-truth bounding boxes) and the human evaluation criteria (lines 301-302: "aligns with the content in the ground-truth poster"; "accuracy of matching image elements between the generated and ground-truth posters") compare the output against a single ground-truth poster. A valid alternative poster that faithfully represents the paper but uses different phrasing or layout would be penalized, while a system that simply memorized ground-truth posters would score perfectly. This conflates "poster reconstruction" with "poster generation." The relative improvements over the baseline are still meaningful (both are evaluated under the same protocol), but the absolute quality claims and the framing of the task are overstated.

3. **Extractor loss formulation is inconsistent with the stated objective.** The paper states it uses "standard binary cross-entropy loss" (line 104), but the equations (lines 106-108) define a softmax over *all* elements followed by a sum of negative log-likelihoods over all elements. Softmax normalization pushes probability mass onto exactly one element (multi-class), whereas binary cross-entropy would require per-element sigmoids for multi-label extraction. If the task is multi-label (multiple sentences and images should be extracted), the formulation as written is mathematically wrong. This discrepancy raises doubts about whether the implementation matches the description and makes the reported extraction numbers suspect until clarified.

4. **No qualitative examples are shown.** For a multimodal generation task, the absence of generated poster images is a significant omission. The paper claims "both qualitative and quantitative evaluations" (lines 6, 312) but shows none — no ground-truth vs. generated poster pairs, no layout visualizations, no examples of paraphrasing quality. Tables of numbers cannot substitute for visual inspection of a generation task's output. This is a self-identified gap given the paper's own language.

5. **Layout metrics are imprecisely defined.** "Alignment" is described as "the extent of spatial non-alignment between elements" (line 245) with no formal definition or computation. "Frechet distance" is mentioned without specifying between what distributions it is computed. "Validity" is partially defined (elements > 0.1% of canvas) but the criteria for validity are incomplete. These metrics appear in Tables 4 and 5, but the reader cannot interpret the reported numbers without knowing how they are calculated.

### Minor

1. **The baseline suite is thin.** For generation, only one adapted baseline (AdaD2P) is compared against. While the task is new and off-the-shelf baselines do not exist, the paper would be strengthened by an ablation that replaces the interactive generator with a simpler non-interactive BART that processes all elements at once, to isolate the benefit of the interactive mechanism. The current ablation (Table 6) focuses on memory variants but does not ablate the interactive vs. non-interactive protocol itself.

2. **GPU memory and computational cost not reported.** The paper claims the interactive generation and adaptive memory address GPU constraints (lines 112, 133), but provides no concrete memory consumption or runtime numbers. Without these, the claimed efficiency benefit is unsubstantiated.

3. **Interactive generation details underspecified.** The paper does not state the average number of elements generated per poster, the generator's maximum context length, or whether the element count ever exceeds it. While the order is specified as document order (line 171), the average sequence length and its relationship to the model's capacity are not discussed.

### Trivial

- The description of ImgP/ImgR (lines 181-184) contains formatting artifacts (split mid-word hyphens, garbled text) likely from PDF extraction, making those sentences unreadable. These should be cleaned in camera-ready.

## Nice-to-Haves

- A zero-shot or prompted comparison to a modern vision-language model (e.g., GPT-4V, Gemini) could contextualize the results, though this is not a requirement given the fine-tuning-based nature of the paper.
- Reporting the alignment accuracy (e.g., human validation of a sample of aligned pairs) would strengthen confidence in the dataset labels.
- Concrete GPU memory consumption numbers (e.g., peak memory with and without adaptive memory) would substantiate the efficiency claims.

## Removed Points

- **"Baselines are too weak; should compare to GPT-4V, Gemini, LLaVA"** — Removed as practically infeasible for an academic submission. These are closed-source API models that cannot be fine-tuned on the same data for a fair comparison. The paper's use of BART-large as its backbone and comparison to an adapted AdaD2P is reasonable for a newly defined task.
- **"The formatting of the paper suggests it is not ready"** — Any formatting issues are parser artifacts, not author errors.
- **"Interactive generation process is underspecified (order not stated)"** — The paper does state the order (document order for testing, line 171). This point is factually incorrect and is removed. However, the related point about missing average element counts is kept in Minor.

## Novel Insights

The reviews collectively surface a tension that goes beyond this paper: evaluating generative tasks that produce multimodal artifacts (posters, slides, infographics) through the lens of reconstruction against a single human-authored reference conflates two distinct quality dimensions — *fidelity to the source document* and *agreement with a specific reference output*. This paper's evaluation framework implicitly assumes the two are equivalent, but a valid alternative poster could differ substantially from the ground-truth while still being faithful to the paper. Future work in document-to-poster generation would benefit from evaluation protocols that decouple these dimensions, e.g., measuring content coverage against the source paper directly (rather than against a ground-truth poster) and treating layout as a separate quality axis judged by functional criteria (legibility, logical grouping, no overlap) rather than by proximity to a single reference layout.

## Suggestions

1. **Describe the alignment algorithm in full.** This is the most critical revision. Provide the exact matching procedure, what features are used (caption overlap, spatial correspondence, lexical similarity?), and ideally include a human validation of a random sample showing alignment accuracy.
2. **Clarify the extractor loss.** Fix the equations to match the stated objective (binary cross-entropy → sigmoid per element, not softmax over all elements) or explain what the actual training labels are.
3. **Include qualitative examples.** Show at least 2-3 generated posters alongside their ground-truth counterparts and the original paper, illustrating both successes and failures.
4. **Reformulate or reframe the evaluation.** Either (a) supplement the current evaluation with paper-fidelity metrics (e.g., ROUGE between generated poster text and the paper, human ratings of informativeness relative to the paper) or (b) explicitly acknowledge and justify the evaluation as a "poster reconstruction" task and adjust claims accordingly.
5. **Provide precise definitions of all layout metrics.** Formalize Alignment, Validity, and Frechet distance so they can be reproduced by other researchers.

## Score and Decision

**Score:** 5.0

**Decision:** Reject

**Rationale:** The paper makes a genuine contribution with the SciPG dataset and proposes a reasonable framework architecture. However, the evaluation has structural issues that prevent acceptance in its current form: (1) the alignment pipeline that generates all training labels is entirely unspecified, making the work unverifiable; (2) the extractor loss equations contradict the stated objective, raising doubts about implementation correctness; (3) the evaluation measures poster reconstruction rather than the claimed paper-to-poster generation task; and (4) no qualitative results are shown for a generation task. The dataset contribution is valuable, and the framework is plausible, but the experimental evidence does not convincingly support the effectiveness claims. Major revisions — particularly full alignment specification, loss correction, qualitative examples, and evaluation reformulation — are needed.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>