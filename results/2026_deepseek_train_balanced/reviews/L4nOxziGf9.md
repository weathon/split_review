## Summary

The paper proposes RAR (Rephrase, Augment, Reason), a gradient-free framework that addresses question underspecification in zero-shot VQA. RAR uses the same LVLM to extract visually-grounded information (keywords, captions, rationales) about the image, fuses these into multiple rephrased question candidates, and selects the best candidate via the model's own answer-confidence score. The method is evaluated on 3 LVLMs (BLIP-2, MiniGPT-4, LLaVA-1.5) across 3 VQA benchmarks (VQAv2, A-OKVQA, VizWiz), showing consistent improvements in every setting (up to +7.94% absolute on weaker models).

## Strengths

- **Consistent gains across all 21 tested model–dataset–metric combinations (Table 1).** The main claim is backed by positive absolute improvements in every setting, including models from three different architectures. This breadth of evaluation provides solid evidence that RAR's effect is not a fluke of a single favorable configuration.

- **Informative ablations isolate the contribution of each pipeline component (Table 2).** Removing rationales (largest drop, ~2.7pp on VQAv2), captions (~1.2pp), or question entities (~1.4pp) all degrade performance, confirming that each information source in Stage I(a) is individually useful.

- **Empirical disambiguation from mere paraphrasing (Table 3).** RAR outperforms the Pegasus paraphrasing baseline under both oracle selection (72.42 vs. 70.99 on VQAv2) and unsupervised confidence-based selection (66.43 vs. 62.91). Notably, paraphrasing sometimes *hurts* performance under unsupervised selection (62.91 vs. 62.58 baseline), while RAR consistently improves it, showing the visual grounding adds substantive information beyond cosmetic rewrites.

- **Oracle upper bound reveals meaningful headroom (Table 1).** The oracle setting yields up to +14.41% (A-OKVQA direct, MiniGPT-4 7B) and +20.09% (VizWiz, MiniGPT-4 7B), confirming the question candidates themselves are beneficial and that improving the selection function could unlock further gains.

- **Linguistic analysis confirms increased complexity (Table 4).** Both ADD (syntactic complexity) and ID (semantic complexity) increase after RAR on VQAv2 (ADD: 17.87→29.52, ID: 0.258→0.296) and A-OKVQA (ADD: 25.40→32.81, ID: 0.282→0.299), providing direct evidence that the rephrased questions are less underspecified.

## Weaknesses

### Fatal
None.

### Major

- **The confidence-based selection function is used but never directly evaluated as a selection mechanism.** The gap between RAR's actual performance and the oracle is substantial (e.g., 66.43 vs. 72.42 on VQAv2 with BLIP-2, a ~6pp gap; on VizWiz with MiniGPT-4 7B, 37.81 vs. 50.47, a ~12.7pp gap). Yet the paper provides no analysis of the selection function's behavior: what fraction of the time does it pick the best candidate? Is it better than random selection? Does confidence correlate with correctness in this setting? The paper asserts that "relative confidence" suffices because overconfidence is systematic, but this is not self-evidently true — systematic overconfidence in certain rephrasing patterns could systematically select bad candidates. A simple experiment reporting the selection hit rate would directly validate or bound the method's core claim. As it stands, the paper demonstrates that the *combination* of candidate generation and confidence-based selection yields improvements, but cannot attribute how much of the headroom loss comes from the selection step versus the generation step.

### Minor

- **Gains on the strongest model (LLaVA-1.5) are small and the pattern is underexplored.** On LLaVA-1.5, improvements are +0.42% on VQAv2, +1.53% on A-OKVQA direct, and +0.92% on VizWiz. While consistently positive, these gains are modest relative to the substantial computational overhead of the RAR pipeline (keyword extraction, rationale generation, caption generation, object queries, generating n=5 candidates, NLI filtering, scoring all 5 candidates). The paper leads with headlines like "up to 7.94%" but this comes from the weakest model combination (MiniGPT-4 on VizWiz). A more prominent discussion of diminishing returns on stronger models and whether the cost-benefit justifies the pipeline for such settings would improve the paper's honesty.

- **No cross-model transfer evaluation.** The same LVLM is used to (a) generate captions, (b) generate rationales, (c) answer queries about objects, (d) fuse information into rephrased questions, (e) answer the rephrased questions, and (f) score candidates. If RAR's benefit were truly about reducing underspecification in questions, rephrased questions from model A should help a different model B. If the benefit comes from generating questions that match model A's stylistic preferences, the answer might be no. Running this cross-model experiment would substantially strengthen the claim that RAR addresses underspecification rather than exploiting model-specific confidences. The paper's paraphrasing comparison partially addresses circularity but does not substitute for cross-model transfer.

- **Components used as black boxes are not analyzed.** The keyword extraction system (citing RAKE, line 139) is described as "off-the-shelf" but never named in the main text nor evaluated. The NLI filter (line 155) discards candidates that "contradict the original question," but the paper never reports how often candidates are filtered, what types of questions are disproportionately discarded, or whether the filter introduces biases (e.g., discarding informative rephrasings that superficially contradict the original polarity of yes/no questions). These are non-trivial design decisions that could silently affect results.

- **The complexity analysis (Table 4) uses only 100 instances.** While the ADD/ID metrics are informative, a sample of 100 instances is small, especially for drawing conclusions about dataset-level phenomena. The paper does not report confidence intervals or variability for these metrics.

### Trivial
- Typo: "quantiative" (line 315).

## Nice-to-Haves
- **Hit-rate analysis of the selection function:** Reporting the frequency with which confidence-based selection picks the oracle-best candidate (or the top-k) would strengthen the paper's core claim without additional baselines.
- **Cross-model transfer experiment:** Testing RAR questions from model A on model B would distinguish underspecification reduction from model-specific artifacts.
- **An LLM-prompted rephrasing baseline:** Asking the LVLM itself to "rephrase this question in a different way" (without visual grounding) would provide a cleaner control than Pegasus for isolating the value of image-derived information.

## Removed Points
These points are flagged to be removed; treat them with caution.

- **"No standard deviations or significance tests are presented."** — REMOVED. The paper reports standard deviations via the \interval macro throughout Table 1 (e.g., 54.49\interval{1.44}) for all RAR and oracle results, averaged over 3 random seeds. The critic missed these inline markers.
- **"Asymmetric strength mechanism is not convincingly isolated."** — REMOVED. Table 5 (rows 3 vs. 4) shows LLM-only accuracy improves with RAR questions (32.84%→40.53% on VQAv2), and rows 5–6 further show that simply adding caption/extracted text to the original question (52.88%, 54.31%) differs from full RAR rephrasing (40.53%), while the full LVLM with RAR (row 2: 67.28%) still substantially outperforms all LLM-only settings. This is reasonable evidence that RAR shifts more of the task to the LLM while keeping the image complementary.
- **"No experimental comparison to alternative prompt optimization methods (GRIPS, Tempera, RLPrompt)."** — REMOVED as a distinct weakness. The paper's zero-shot, no-training-set setting (lines 107–112) explicitly distinguishes it from these methods, which require labeled data. The Pegasus paraphrasing comparison already provides a rephrasing baseline. A simpler LLM-prompted rephrasing baseline would be nice-to-have but is not a missing requirement.

## Novel Insights
None beyond the paper's own contributions.

## Suggestions
1. Add a direct evaluation of the selection function: report the hit rate (fraction of instances where confidence-based selection picks the oracle-best candidate) and a "random selection" baseline across the candidate pool.
2. Run a cross-model transfer experiment (e.g., RAR questions from BLIP-2 evaluated on MiniGPT-4) to verify that the benefit comes from reduced underspecification rather than model-specific phrasing affinities.
3. Report details on NLI filtering rates and keyword extraction failure cases to quantify the robustness of these black-box components.
4. Discuss the diminishing returns on strong models more prominently, including a cost-benefit analysis for practitioners.
5. Expand the complexity analysis to a larger sample or report bootstrapped confidence intervals.

## Score and Decision

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>