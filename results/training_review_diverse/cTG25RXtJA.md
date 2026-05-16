Now I have all the information needed. Let me compose the final consolidated review.

## Summary

The paper proposes KEEP (Knowledge-Enhanced Explainable Prompting), a framework that injects fine-grained, image-wise domain knowledge into VLM prompt learning via RAG and domain-specific foundation models. The framework consists of two stages: knowledge-enhanced prompt creation (using domain-specific FMs and RAG to generate image-specific knowledge) and knowledge-enhanced prompt learning (aligning images and knowledge-enhanced prompts via an attention mechanism). The method is evaluated on eight datasets spanning medical and natural domains, showing consistent improvements over prior prompt learning methods alongside explainability analyses.

## Strengths

1. **Consistent state-of-the-art performance across diverse domains**: KEEP achieves average relative improvements of ~3.2% on medical datasets and ~2.6% on natural image datasets over the second-best method (Tables 1 and 2), directly supporting the claim that fine-grained domain-specific knowledge enhances VLM adaptation more effectively than coarse-grained prompt methods.

2. **Demonstrated faithfulness of knowledge through intervention**: Figure 4 shows that replacing domain-specific knowledge with random, coarse-grained, or intervened knowledge causes clear performance degradation across all eight datasets. This provides causal evidence that the elicited knowledge truthfully reflects the model's decision process—a key requirement for XAI trustworthiness that prior prompt-learning works have not addressed quantitatively.

3. **Data efficiency via domain knowledge**: On CCBTM, when training data drops from 50% to 10%, KEEP's accuracy only declines from 94.9% to 92.0%, while LASP drops from 91.5% to 82.7% (Table 3). This demonstrates a practical advantage of image-wise knowledge in low-data regimes.

4. **Ablation validates designed components**: Removing the image-prompt attention logit, image-prompt matching loss, or classification loss each degrades performance (e.g., on medical datasets from 92.19% to 87.51%, 88.40%, and 90.86% respectively—Table 4), confirming that the proposed attention mechanism and losses are necessary for the gains.

5. **Flexible integration across domains**: The framework works across 8 datasets (dermoscopic, chest X-ray, brain MRI, natural objects, aircraft, flowers, textures) using different knowledge sources (MiniGPT-4/GPT-4 for natural; MedCPT + PMC-LLaMA + KAD/BiomedCLIP for medical), demonstrating generalizability without domain-specific re-engineering.

6. **Qualitative visual and textual explanations**: Figure 5 shows attention maps highlighting discriminative image regions with corresponding word-level importance in the prompts (e.g., "melanoma", "dots", "globules" for a dermoscopic image), offering interpretability beyond the class-level textual prompts of prior works.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the experimental evidence.

### Minor
1. **Unclear baseline tuning fairness.** The implementation section states that grid search was used to select KEEP's hyperparameter β, but does not explicitly state whether the baseline methods (CoOp, CoCoOp, KgCoOp, LASP, TCP, etc.) were tuned with a comparable search. The paper reports that "All prompt learning methods implemented in this paper adopted random crop and random flip for data augmentation" and specifies a common optimizer and learning rate, which suggests a fair implementation baseline. However, without an explicit statement that baselines underwent equivalent hyperparameter search, the reported margins may partially reflect tuning effort rather than architectural advantage. The authors should clarify the search procedure applied to each baseline.

2. **Explainability evaluation is primarily qualitative for understandability and plausibility.** The paper evaluates faithfulness quantitatively via knowledge intervention (Figure 4), which is a nice contribution. However, understandability and plausibility are assessed solely through qualitative attention maps and t-SNE plots (Figures 5 and 6). While this is common practice in the VLM literature, the paper's strong XAI framing would be strengthened by quantitative faithfulness metrics beyond the intervention experiment (e.g., insertion/deletion scores) or at least a small user study demonstrating that the explanations improve human decision-making. This does not invalidate the contribution but limits the strength of the XAI claims.

3. **Novelty claim may be overreaching.** The paper states it is "to the best of our knowledge the first work to incorporate RAG and domain-specific FMs for prompt learning in various fields." While the combination is novel, the claim is broad and the related work section does not provide a systematic comparison to rule out concurrent or prior work that may have used similar techniques (e.g., RAG in non-prompt-learning settings, or domain-specific knowledge in prompt learning without RAG). The paper would benefit from a more carefully scoped novelty statement.

### Trivial
- "Alabtion Study" should read "Ablation Study" (line 133).
- "EXPERIENTS" in Section 4 heading should read "EXPERIMENTS" (line 92).
- "EXPLAINBILITY" in Section 4.3 heading should read "EXPLAINABILITY" (line 201).

## Nice-to-Haves
- A brief discussion of failure cases or limitations: e.g., how robust is the method when the domain-specific FMs make inaccurate concept predictions (Equation 2)? What happens when the RAG pipeline retrieves noisy documents?
- Reporting the computational cost of the knowledge-creation stage (LLM calls, retrieval overhead) would help practitioners assess practical feasibility.
- An explicit statement of the hyperparameter search ranges and validation protocol for all baselines would strengthen reproducibility.

## Removed Points

These points are flagged to be removed, treat them with caution:

1. **"Missing core method description (Section 3.3)."** — The extracted paper shows garbled text ("324 325 326...") between the end of Section 3.2 and the start of Section 4, which is a PDF parser artifact. The original submission clearly references Section 3.3 at line 57 ("The second stage is Knowledge-Enhanced Prompt Learning (3.3)") and mentions Algorithm 1; these were lost during PDF extraction. Per the rules, formatting artifacts introduced by the parser are not author errors.

2. **"No quantitative metrics for explainability."** — This is factually incorrect. The faithfulness evaluation (Section 4.3, Figure 4) is quantitative: it measures accuracy under five prompt settings (no knowledge, random, general, fine-grained, intervened) across all eight datasets. The lack of quantitative metrics applies only to the understandability and plausibility subsections, which is already captured in Minor weakness #2.

## Novel Insights

None beyond the paper's own contributions. The reviews largely converge on the paper's strengths and surface two well-known concerns (baseline tuning, qualitative-only XAI evaluation) without introducing genuinely novel observations that the authors would not have considered.

## Suggestions

1. **Clarify baseline tuning**: Add a sentence explicitly stating whether each baseline underwent the same grid search procedure, and if so, report the search ranges. This single addition would resolve the most significant uncertainty about the experimental results.

2. **Strengthen the explainability evaluation**: Add one or two quantitative metrics for understandability/plausibility (e.g., deletion/insertion scores for the attention maps, or a concept-accuracy measure showing that highlighted concepts are diagnostically relevant). Even a small-scale human evaluation (e.g., "does the highlighted knowledge match expert judgment?") would significantly bolster the XAI claims.

3. **Softened novelty framing**: Replace "the first work to incorporate RAG and domain-specific FMs for prompt learning" with a more precise claim (e.g., "to our knowledge, the first to combine image-wise RAG-based knowledge with prompt learning for both medical and natural domains"), which is both verifiable and sufficient for the contribution.

## Score and Decision

The paper presents a well-executed framework with consistent gains across diverse domains, a principled faithfulness evaluation, and evidence of data efficiency. The weaknesses are minor (unclear baseline tuning, qualitative-only XAI for two of three dimensions, and an overbroad novelty claim) and addressable. The core contribution—using image-wise domain knowledge from FMs and RAG to improve both performance and interpretability of VLM adaptation—is solid and well-supported.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>