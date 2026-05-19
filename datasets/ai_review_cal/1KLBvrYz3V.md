- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 6, 8, 8
Now I have all the information needed. Let me compile the final consolidated review.

## Summary

The paper introduces Century, a dataset of 1,500 historically sensitive images and a framework for evaluating how multimodal foundation models perform "historical contextualisation" — describing images with awareness of their socio-cultural and historical dimensions. The dataset is constructed via a scalable two-pronged methodology (knowledge graph queries + LLM-generated search terms mining 37.8M Wikipedia records), validated through automated and human evaluation along quality/diversity dimensions. An evaluation protocol measuring accuracy, thoroughness, and objectivity is proposed and demonstrated on four foundation models.

## Strengths

1. **Scalable, reproducible methodology for curating sensitive historical images.** The two-pronged approach (7,385 knowledge-graph-derived terms + 1,297 LLM-derived terms with only 15.1% overlap) is novel, principled, and avoids purely manual curation. The method is described clearly and can be adapted to other image datasets.

2. **Dataset diversity and sensitivity are validated through convergent evidence.** Human evaluation with 151 participants finds 90.9% of images are rated "somewhat sensitive" or higher, and every UN sub-region is represented. The convergence between automated labels (61.5% mean sensitivity) and human labels (55.8%) provides reasonable evidence of construct validity for the dataset itself, and both label sets are released.

3. **Reference-free evaluation protocol with explicit dimensions.** Defining evaluation along accuracy, thoroughness, and objectivity — and implementing this as a reproducible protocol with six automated labeller models — provides a structured foundation that the community can build upon, critique, and refine.

4. **Thoughtful treatment of limitations and ethical considerations.** Sections 5.2 and 7 are unusually thorough, addressing geographic representation bias, the risk that institutional norms may not reflect community perspectives, the pitfalls of generative labelling for normative judgments, and protections for human annotators. This self-awareness strengthens the paper's credibility.

## Weaknesses

### Fatal

None. The dataset contribution is solid and the core claims about the dataset are supported by evidence.

### Major

1. **The evaluation protocol for historical contextualisation lacks validation.** The paper uses LLM-as-judge to score model responses on accuracy, thoroughness, and objectivity — an extremely challenging judgment task requiring both factual historical knowledge and normative sensitivity. No correlation or agreement metrics are reported between automated and human evaluations on this task. The human evaluation (63 images, n=378 responses) is acknowledged as small-scale but is too limited to serve as validation of the automated protocol. Without evidence that the automated evaluators produce ratings aligned with informed human judgment on this specific task, the reported scores in Table 3 are not interpretable as reliable measurements of "historical contextualisation capability." This is an evidential gap, not a fatal flaw — the dataset remains useful — but it means the third claimed contribution (the evaluation protocol and its results) is less well-supported than the first two.

2. **Context-free evaluation creates a construct validity gap.** The paper evaluates models on images with no accompanying textual information. As the paper itself notes (Section 4.2), some images are ambiguous without context (e.g., a modern-day monastery representing a historical battle). The paper acknowledges this and recommends experimenting with context-driven protocols in future work, but still presents the current results as measurements of "historical contextualisation capabilities." The gap between what is measured (recognition of visually identifiable historical content) and what is claimed (contextualisation) is large enough that the comparative ranking of models in Table 3 should be treated as exploratory, not diagnostic.

3. **The framing of three equal contributions overstates the evaluation component.** The paper lists three contributions of equal weight, but the evaluation protocol is presented with substantial caveats (small human evaluation, unvalidated automated judges, context-free setup, vague finding that Century is "effective at discovering opportunities for all foundation models to improve"). This framing forces the evaluation to carry more weight than the evidence currently supports. The dataset and construction methodology are the clear primary contributions; the evaluation is best viewed as a demonstration of potential use.

### Minor

4. **Variance across automated labeler models is acknowledged but not deeply analyzed.** The paper reports differences as large as 30 percentage points between labeler models (e.g., GPT-4 Turbo vs. Gemini 1.5 Pro for sensitivity). The ensembling approach (averaging across "four best-performing" labelers) is reasonable but the criteria for "best-performing" are not stated, and the selection could introduce bias. Releasing all individual label ratings mitigates this, but the analysis would benefit from explicit justification of the selection criteria.

5. **The human evaluation for quality/diversity uses crowdworkers with self-reported relevant experience** (e.g., "undergraduate degree in history"), which is a weak proxy for the kind of expert historical judgment that would best validate sensitivity annotations. While practical, this limits the strength of the claim that the dataset's sensitivity labels are authoritative.

### Trivial

None that are not parser artifacts.

## Nice-to-Haves

- A small validation study comparing automated evaluations with expert historian judgments on a held-out set of responses (even 30–50 responses rated by 2–3 professional historians) would substantially strengthen the evaluation protocol.
- Disaggregated analysis of model performance by image type (events vs. people vs. locations), geographic region, and iconicity would demonstrate the value of the released metadata and reveal whether observed patterns are systematic.
- A static snapshot of the images (rather than Wikipedia links) would protect against link rot.

## Removed Points

These points were raised by reviewers but are removed for the reasons stated:

- **"128 images provenance unexplained":** The sentence cuts off at "(8." — this is a parser artifact. The original paper would specify the source. Removed per rule on parser artifacts.
- **"No concrete examples of model outputs":** Figure 1 in the original paper provides qualitative examples showing failures. Removed as factually incorrect.
- **"Starter set not clearly defined":** The paper defines it precisely at line 109: "all images with a mean rating of 'sensitive' > 3.0 across human and automated evaluation, with each geographical sub-region downsampled to no more than six images." Removed as factually incorrect.
- **"No analysis of inter-rater reliability for human evaluations":** The paper states "we review disagreement in human judgements of sensitivity using CrowdTruth metrics" — this content was likely in the full paper/appendix that the parser stripped. Removed per rule on missing appendix content.
- **"Link rot / dataset stability":** The paper provides Wikipedia links plus search terms and metadata. Concern about the availability of cited entities should not be flagged. Removed per hard rule.
- **"No discussion of dataset stability":** Same as above.
- **"Low overlap (15.1%) could indicate noise":** This is speculation. The paper notes the complementary coverage as a positive feature. Removed as speculation without evidence.
- **"Automated labeling not a reliable proxy":** While variance exists, the paper reports convergent evidence at the aggregate level. The criticism is framed too absolutely; the weakness is retained in weakened form (Minor #4 above).

## Novel Insights

None beyond the paper's own contributions. The review process surfaces the fundamental tension between the paper's contributions cleanly: the dataset construction methodology is genuinely novel and well-validated, but the evaluation protocol — while thoughtful in design — lacks the validation evidence needed to treat its results as diagnostic of model capability. This asymmetry between the strength of the dataset contribution and the weakness of the evaluation contribution is the central structural issue the paper should address.

## Suggestions

1. **Reframe the evaluation contribution.** Present the evaluation protocol and results as a "demonstration of how Century can be used" rather than a fully validated benchmark. The abstract and introduction should reflect this asymmetry. The dataset/methodology are the primary contributions.

2. **Add a validation study** comparing automated evaluations with expert human judgments (even modest in size) for the historical contextualisation task, or explicitly label the current evaluation results as exploratory.

3. **Clarify the "best-performing" labeler selection criteria** used for ensembling in Section 4.2, and discuss whether the results are robust to which labelers are included in the ensemble.

4. **Provide qualitative examples of model responses** in an appendix or figure, so readers can ground the evaluation dimensions in concrete model behavior.
