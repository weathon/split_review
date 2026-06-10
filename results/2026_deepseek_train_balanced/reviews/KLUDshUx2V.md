## Summary

This paper proposes an automated pipeline for generating concept banks for Concept Bottleneck Models using LLMs (LLaMa3-70B, Qwen2-72B) and a multimodal CLIP-based evaluation metric to assess concept quality without running a full CBM training pipeline. It investigates three research questions: (RQ1) whether LLMs can generate concept banks comparable to ConceptNet, (RQ2) whether unimodal text-based semantic similarity (BERTScore) suffices for concept-label evaluation, and (RQ3) whether multimodal information (CLIP) provides better concept quality assessment. The main findings are that LLM-generated concepts outperform ConceptNet-sourced concepts on CIFAR-10 and CIFAR-100, that BERTScore fails to distinguish meaningful from random concepts, and that the proposed CLIP-based metric separates them effectively.

## Strengths

- **Training-free concept quality evaluation.** The proposed CLIP-based metric (Section 3.3.3) evaluates concept banks directly via image-concept similarity, without requiring end-to-end CBM training. This is a genuine efficiency advantage over methods that infer concept quality only from final CBM classification accuracy (Oikarinen et al., 2023; Yuksekgonul et al., 2022). The paper explicitly positions this as enabling fast iteration on concept banks before committing to a full CBM pipeline (lines 49–50).

- **Demonstration that LLMs can generate competitive concept banks on standard datasets.** Table 3 and Section 4 report that LLM-generated concepts (LLaMa3-70B, Qwen2-72B) outperform ConceptNet-sourced concepts on CIFAR-10 and CIFAR-100 when evaluated with the proposed metric. This provides evidence that LLMs alone can produce useful concept banks, reducing reliance on curated knowledge bases like ConceptNet.

- **Empirical gap between multimodal and unimodal evaluation.** Table 2 shows that BERTScore (unimodal) produces near-indistinguishable scores across random, ConceptNet, and LLM-generated concepts on CUB-200 and poor results on CIFAR-100, while the CLIP-based metric (Table 3) shows clear separation. This directly supports RQ2 and provides a meaningful comparative finding.

- **Prefix prompting analysis.** The paper systematically experiments with different prefix templates for CLIP-based concept embedding and finds that prefix tuning improves scores (lines 100–110). This is a practical, reproducible finding that future work can build on.

## Weaknesses

### Fatal

None.

### Major

- **The proposed evaluation metric is not validated against any independent ground truth of concept quality.** The paper's central claim—that LLM-generated concepts "surpass" ConceptNet concepts and that the CLIP-based metric reliably quantifies concept quality—depends entirely on the metric's validity. However, the metric is never validated against: (a) downstream CBM classification performance, (b) human judgments of concept relevance, or (c) alignment with human-annotated concept banks. The only sanity check offered (Section 3.3.1, line 82) contains a confused hypothesis—stating that a reliable metric should show "no significant difference between the scores of randomly generated concepts when compared with ones generated via LLMs and ConceptNet"—which actually contradicts the results section (line 118) where a "huge disparity" is presented as evidence of reliability. Without external validation, the comparison between LLM and ConceptNet concepts (RQ1) and the claim that the multimodal metric is superior (RQ3) rest on circular reasoning: the metric whose validity is unproven is used as the yardstick.

- **The BERTScore evaluation (RQ2) is critically underdefined.** The paper states (line 86): "we find the top-k concepts against each class and match those top concepts with the ground truth." The "ground truth" for concept-class associations is never specified. For CIFAR-10/100 and CUB-200, no standard concept-class ground truth exists, and the paper introduces no such resource. Without knowing what the accuracy numerator and denominator represent, Table 2's numbers are uninterpretable. The subsequent claim that poor results reflect "a fundamental lack of understanding between concepts and class labels" (line 116) could equally reflect a broken evaluation setup.

- **Internal contradiction about the central experimental outcome.** Section 4 (line 118) states that "our LLM-generated concepts also outperform ConceptNet-based concepts in all three datasets." However, the Conclusion (lines 179–180) states that "our generated concepts for the CUB-200 dataset did not surpass those from ConceptNet." These are directly contradictory statements about the same experimental comparison. The abstract (line 4) only claims superiority on CIFAR-10 and CIFAR-100, which is consistent with the Conclusion. This inconsistency between the results section and the conclusion is a serious evidential gap that undermines the paper's primary claim about RQ1.

### Minor

- **ConceptNet baseline is a hybrid, not a clean comparison.** The paper states (line 58): "Due to API limitations, we use Sentence Transformer's roberta-based model and find more concepts using algorithm similar to (Oikarinen et al., 2023)." This means the "ConceptNet" baseline is actually a combination of ConceptNet relations and Sentence Transformer retrieval, introducing a second LLM-based component into the baseline. Additionally, LLM-generated concepts benefit from task-specific prompt tuning ("for CUB-200, we slightly modify the prompt to generate data more specific to the attributes of birds," line 62), while ConceptNet is used generically. The comparison is not apples-to-apples.

- **No statistical reporting.** All results are point estimates without variance, confidence intervals, or significance tests. Given that the evaluation uses a random sample of 50 images per class (line 76), results should be reported across different random seeds or image subsets to assess stability.

- **CUB-200 underperformance is noted but not analyzed.** The paper mentions that the proposed approach lags behind Semenov et al. (2024) on CUB-200 (line 118) but provides no analysis of why. CUB-200 is the most widely studied dataset in the CBM literature; a systematic failure on this dataset deserves investigation beyond a brief concession.

- **Random concept generation is underspecified.** The paper states (line 64): "We prompt LLaMA3 to generate irrelevant and unrelated concepts given a class label." The prompt template, sampling strategy, and quality checks for these random concepts are not described. Since the random-vs-meaningful separation is used as a key sanity check, the specifics matter.

### Trivial

- The filtering thresholds (3 and 32 characters, line 70) and diversity filtering ("retain only the diverse set of concepts," line 70) are mentioned but never justified or operationalized.
- Some methodology descriptions (e.g., how the "mode" of similarity scores works in Algorithm 2, line 132) are unclear. The mode of a continuous-valued similarity matrix is not a standard operation.

## Nice-to-Haves

- A human evaluation study of concept interpretability would strengthen the claims, though the paper's focus on automated evaluation makes this an enhancement rather than a requirement.
- Validation of the proposed metric against downstream CBM performance would turn the core contribution from a plausible proposal into a well-supported tool.

## Removed Points

These points from the inputs were removed. Treat them with caution:

- **Missing appendix prompts (Harsh Critic):** The reviewer noted that Appendix A.1 appears empty. Per filtering rules, the parser strips appendix content from all papers; this is not an author error.
- **"Overselling" the evaluation approach (Harsh Critic):** The claim that the paper "oversells" the distinction between its approach and end-to-end CBM evaluation is not supported—the training-free vs. full-pipeline distinction is a meaningful methodological difference.
- **No human evaluation (Harsh Critic):** The paper is about automated evaluation; requiring human evaluation extends beyond the stated scope.
- **TCAV description as imprecise (Harsh Critic):** The description is adequate for a literature survey section; it does not materially affect the paper's contributions.
- **Strength Finder's claim about "most important piece of evidence" being Table 3:** Overstated given the validation gap, but the underlying strength (LLM > ConceptNet on CIFAR-10/100) is genuine.

## Novel Insights

None beyond the paper's own contributions. The two reviewers' analyses did not synthesize into an observation that the paper itself does not already make or imply.

## Suggestions

1. **Validate the proposed metric against downstream CBM performance.** Take the LLM-generated and ConceptNet-based concept banks, plug them into a standard CBM (Koh et al., 2020; Oikarinen et al., 2023), measure CBM accuracy and concept utilization, and show that the proposed metric's rankings correlate with downstream performance.
2. **Resolve the internal contradiction** about whether LLM concepts outperform ConceptNet on CUB-200.
3. **Define the "ground truth"** for the BERTScore accuracy computation explicitly, or reframe the RQ2 analysis without reference to undefined ground truth.
4. **Report variance** across different random image samples to establish stability of the results.
5. **Analyze the CUB-200 failure** — investigate whether the issue is with concept generation (prompts not specialized enough for fine-grained bird attributes), concept filtering (over-aggressive pruning), or the CLIP-based evaluation (insufficient fine-grained discrimination).

## Score and Decision

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>