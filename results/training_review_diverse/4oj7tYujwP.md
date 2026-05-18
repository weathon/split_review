Now I have all the evidence I need. Let me produce the final consolidated review.

## Summary

This paper introduces ERiC-UP³, a large-scale benchmark dataset for detecting potentially infringing utility patents given a product's multi-modal data (images + text). It formulates this as a new retrieval task, provides 13K expert-annotated product-patent infringement pairs alongside 13M unlabeled patents and 1M product samples, and presents a text-based pipeline combining a CPC classifier (to reduce search space) with a supervised contrastive learning retriever. The dataset is novel in scope and problem framing, but the paper's presentation overclaims the multi-modal contribution relative to a text-only method, and the annotation criteria for infringement labels are underspecified for a benchmark intended to support legally significant downstream tasks.

## Strengths

1. **First expert-annotated dataset for product-patent infringement detection at scale.** The paper explicitly states this is "the first strictly annotated product-patent infringement detection dataset" (Abstract, Section 2.2). The 13K training+test pairs undergo "three rounds of cross-validation" by patent experts (Section 2.2), filling a genuine gap where no prior benchmark existed for this task.

2. **Unprecedented scale of patent and product data.** The benchmark includes "over 13-million patent samples and 1 million product samples" (Abstract), making it the largest multi-modal patent dataset available. This scale is critical for realistic evaluation — a retrieval pool of 13M patents mirrors the real-world search space.

3. **Novel and practically important task formulation.** The paper formulates patent infringement detection as a retrieval problem: given a product (text + images), retrieve infringing patents from a large gallery (Section 2.1). This goes beyond existing patent classification/summarization tasks and addresses an authentic industrial need for proactive IP risk detection.

4. **Effective patent-based classifier training strategy (non-obvious finding).** Section 4.2 (Table 6) shows that a classifier trained on patent texts mapped to CPC codes transfers surprisingly well to product-to-patent classification, outperforming both direct infringement-pair training and GPT-4-generated labels. This is a practical insight the community can build on.

5. **Useful ablation of textual section combinations.** Table 4 systematically evaluates which patent/product text sections work best for retrieval ("Abstract+Claims" for patents, "Title+Description" for products), providing actionable guidance for future work on this task.

## Weaknesses

### Fatal
None.

### Major

1. **Ground-truth labeling criteria are underspecified for a benchmark with legal stakes.** The paper says infringement pairs are "meticulously labeled by patent experts through three rounds of cross-validation" (Section 2.2) and describes three data sources — Virtual Patent Marking data, pre-listing IP audits, and historical cases (Section 2.3). However, it never states: (a) what specific legal criteria the experts used to determine infringement (literal infringement? doctrine of equivalents? claim interpretation?), (b) whether VPM over-marking (listing non-infringed patents) was filtered and how, (c) any inter-annotator agreement statistic (e.g., Cohen's κ or Krippendorff's α). For a dataset framed as supporting "IP infringement detection" — a determination with legal consequences — these omissions undermine users' ability to assess label quality and benchmark validity. The paper should document the annotation protocol explicitly and report agreement rates.

2. **Multi-modal framing is overclaimed relative to the delivered contribution.** The title, abstract, and introduction repeatedly emphasize multi-modal data and "deep functional understanding across images and text." Yet the main pipeline (Section 3) is entirely text-based. The multi-modal analyses in Section 4.4 are presented as scattered probes (image retrieval with stretch detection at 33.92% mAR@500, cross-modal CLIP at 57.14%, visual-enhanced fusion) that do not feed into a unified method, and none outperforms the text-only pipeline (60.49% mAR@500). The paper never demonstrates a strong multi-modal baseline. This creates a mismatch: the task is scoped as multi-modal, but the central contribution is a text-only system on a multi-modal dataset. The paper would be stronger if it either delivered a competitive multi-modal baseline or honestly scoped the contribution as primarily text-based with the multi-modal data offered as a resource for future work.

### Minor

3. **The mRoM evaluation metric is underspecified.** Section 2.6 defines mRoM as "mean Rank of Matches" without clarifying: (a) whether ranks are computed relative to the full 13M patent pool or the reduced (classifier-filtered) subset — critical for interpreting Table 7 where "w/o classifier" and "with classifier" rows are compared; (b) what rank is assigned to queries where no infringing patent is found in the top-K (excluded from the mean? assigned a default rank of K+1?); (c) distributional statistics (median, quartiles) that would validate the reported mean of 110.00 alongside the 58.47% mAR@500. Additional reporting of these details would prevent potential misinterpretation.

4. **Retriever baselines are weak.** Table 5 compares fine-tuned models only against their frozen counterparts. Any retrieval method trained on task-specific data should outperform a frozen language model, so the reported 29–52% relative improvements are unsurprising. The paper does not compare against standard retrieval paradigms such as DPR or ColBERT, which are well-established for text-based retrieval. This weakens the claim that the SCL approach is a useful reference baseline for future work. Adding even one such baseline would substantially strengthen the evaluation.

5. **Classifier's oracle failure rate is not discussed.** Table 6 shows the patent-based classifier achieves 83.5% Top-5 accuracy on the Large test set, meaning ~16.5% of test products will have the correct patent excluded from the search space before retrieval even begins (Section 3.1). The paper does not discuss this trade-off, report the per-query failure rate, or propose a fallback strategy. The modest overall mAR@500 improvement (58.47% → 60.49%) could mask a pattern where gains on easy cases compensate for guaranteed failures on hard ones.

6. **Hard-sample mining is mentioned but not evaluated.** Section 3.2 states that negative samples are "periodically update[d] with patents that the model currently finds challenging," citing Karpukhin et al. (2020). No ablation quantifies the effect of this design choice, leaving readers to wonder whether it helps, hurts, or is neutral.

7. **Training setup details are absent.** The paper does not report batch size, learning rate, training hardware, or wall-clock time for any of the experiments, including fine-tuning a 7B-parameter LLaMa2 model. These are standard reproducibility details.

### Trivial

- The five CPC categories used in the Base dataset (A45, A47, A63, B65, H01) are listed in Section 2.2 without any description of what product/patent domains they cover. A brief domain description would help researchers understand the scope.
- The paper states an optimal text combination (Section 4.1, Table 4) but does not explicitly confirm this combination is used uniformly across subsequent experiments.

## Nice-to-Haves

- A formal datasheet (Gebru et al., 2020) documenting dataset composition, collection methodology, intended uses, and known biases would greatly aid responsible use.
- A clean multi-modal baseline (e.g., late fusion of text and image similarity scores) that is at least compared against text-only performance — even if it does not beat text, stating this as a finding would be valuable.
- Per-query breakdown of classifier failures and their impact on final retrieval accuracy, to assess whether the modest net improvement from the classifier is worthwhile.

## Removed Points

- *Criticism about dataset not being released / no URL provided.* Removed per hard rules: the rule states that criticisms questioning the release status or availability of any dataset cited in the paper should be removed. (The dataset is the paper's own contribution, making this ambiguous — but following the literal rule.)
- *Criticism about missing appendix / proofs in appendix.* Removed per hard rules: the parser strips appendices; they exist in the original submission.
- *Criticism about "figures not described in sufficient textual detail."* Removed per hard rules: figure rendering issues are parser artifacts.
- *Formatting/style nitpicks.* Removed per hard rules.

## Novel Insights

The most interesting observation that emerges from the reviews is the tension between the paper's two core claims. On one hand, the dataset is genuinely novel and practically valuable — there is simply no other large-scale, expert-annotated benchmark for this task. On the other hand, the paper's decision to present a text-only pipeline as its main method while giving the multi-modal data only exploratory treatment creates a credibility gap. The classifier-transfer finding (patent-based CPC training generalizing to product inputs) is the most original technical insight in the paper, not the SCL retriever. Future work would benefit most from deeper characterization of the infringement labels themselves (what kinds of infringement, what claim elements are at issue) and from multi-modal methods that actually exploit the image data the benchmark provides.

## Suggestions

1. **Document the annotation protocol in detail.** State the legal criteria experts used, report inter-annotator agreement, and discuss how VPM over-marking was filtered. This single change would most improve the paper's credibility as a benchmark resource.
2. **Rebalance the multi-modal framing.** Either deliver a competitive multi-modal baseline that at least matches text-only performance, or reframe the contribution as primarily text-based with multi-modal data offered for future use. The current framing promises more than it delivers.
3. **Define mRoM precisely and report distributional statistics.** Clarify the rank computation denominator and what happens to failed queries. Report median and quartiles alongside the mean.
4. **Add at least one standard retrieval baseline** (DPR or ColBERT) to Table 5 to calibrate reader expectations about difficulty.
5. **Ablate the hard-sample mining mechanism** and report the classifier's oracle failure rate with its impact on per-query outcomes.

## Score and Decision

This is a valuable benchmark paper with a genuinely novel dataset and a well-motivated task. The weaknesses are real but fixable — the underspecified annotation criteria is the most significant concern, but the dataset itself is clearly the result of substantial expert effort. The multi-modal overclaiming is a presentation issue that can be corrected by honest re-scoping. The paper should not be rejected for these issues; they are addressable in a revision.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>