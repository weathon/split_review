- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6
Now I have all the evidence I need. Let me write the final consolidated review.

## Summary

DebugAgent proposes an automated framework for discovering and repairing error slices (systematic failure subsets) in vision models. Its technical core is three-fold: (1) structured attribute/tag generation covering object, background, and global factors, (2) an efficient breadth-first tree-structured slice enumeration algorithm with pruning and intersection to overcome combinatorial explosion, and (3) a method to predict error slices beyond the validation set using tag substitution and instruction-based generation. Experiments span image classification, pose estimation, and object detection.

## Strengths

- **Efficient slice enumeration is convincingly validated.** The breadth-first tree-structured algorithm with pruning and intersection (Section 4.1.4) achieves a 510× speedup over naive enumeration and 7–12× over a tree-structured baseline, with linear runtime scaling in data volume. This is the paper's strongest technical contribution and is well-supported by Figures 4–5.

- **Model repair outperforms the closest prior method across three tasks.** Table 2 shows that DebugAgent's data selection based on identified error slices yields consistent improvements over HiBug and random selection: e.g., ResNet18 accuracy from 68.0% to 72.0% (HiBug: 70.6%), pose estimation AP from 48.7% to 50.7% (HiBug: 49.7%), and detection mAP from 38.6% to 40.0% (HiBug: 39.3%). These results are averaged over five runs and demonstrate practical utility.

- **Cross-model failure pattern analysis provides novel insights.** Section 5.3 reports quantitative overlap of top-10% error slices across models: 86% for object detection models, 73% for pose estimation, and only 31% for classification. This finding is methodologically interesting and demonstrates the framework's diagnostic value beyond repair.

- **Unseen slice prediction methods are conceptually novel.** The combination of CLIP-based tag substitution and GPT-based instruction generation (Section 4.2) for predicting error patterns not present in the validation set addresses a genuine limitation of prior work that few methods tackle.

## Weaknesses

### Fatal

None.

### Major

- **Data source for unseen slice evaluation (Section 5.4, Table 1) is not specified.** The paper reports large performance drops on "predicted error slices" (e.g., classification accuracy falling from 0.837 to 0.297) but never states what dataset these performance numbers are computed on. The slices are attribute–tag combinations; to evaluate them, one must find data matching those combinations. Is this the validation set itself (meaning the slices are unseen only in the sense of not being previously enumerated, not that the data is unseen)? A held-out pool? The query set from Section 5.5? The paper is silent on this, and the claim is a core contribution ("addressing a key limitation of prior approaches"). This must be clarified and the experimental design made transparent.

- **Attribute/tag quality is evaluated only via a single qualitative example.** Section 5.1 (Figure 3) shows one image with attributes from DebugAgent, Domino, and HiBug. No quantitative metrics — coverage, human-rated coherence, error-relevance scoring, or inter-annotator agreement — are provided for a claimed contribution that the paper frames as primary. The downstream repair results (Table 2) provide indirect support, but without isolating the attribute quality component (e.g., via controlled substitution or ablation), the claim that DebugAgent produces "attributes of significantly higher quality" (abstract) remains under-evidenced.

### Minor

- **Model repair comparison is limited to a single prior automated method.** Only HiBug and random selection are compared in Table 2. The paper acknowledges (Section 6) that diverse workflows complicate fair comparison, which is reasonable. Nevertheless, the claim of "state-of-the-art" repair is weaker than it would be with at least one additional baseline on a shared task (e.g., AdaVision on the ImageNet bear subset). This does not invalidate the results but tempers the strength of the claim.

- **No error bars or significance tests in Tables 1 and 2.** Reporting averages over 5 runs without variance makes it impossible to assess whether the observed gaps over HiBug (e.g., 72.0 vs. 70.6, 50.7 vs. 49.7) are statistically reliable. This is standard to expect for a methods paper claiming superiority.

- **No ablation isolates the contribution of individual components.** While Figure 5 ablate the enumeration algorithm (varying data volume and attribute count), there is no ablation for: (a) the comparative attribute generation strategy vs. direct GPT querying, (b) the tag substitution vs. instruction-based prediction methods individually, or (c) the contribution of unseen slice prediction to downstream repair gains. This makes it difficult to attribute which design choices drive the reported improvements.

### Trivial

- The phrase "generates an initial list of potential and unbiased tags" (Section 3.2.2) describes the goal of the multi-stage refinement process but uses "unbiased" in a loose, non-technical sense. Rephrasing would avoid potential confusion with statistical bias.

## Nice-to-Haves

- A human evaluation of tag/attribute quality (e.g., rating coherence, error-relevance, consistency) would substantially strengthen the paper's primary contribution claim about attribute generation.
- Including confidence intervals (e.g., bootstrap 95% CI) for Table 2 would allow readers to assess the reliability of the repair improvements.
- An explicit description of the data pool used to compute "performance on predicted slices" (Table 1) is needed — whether it is the validation set, a held-out pool, or the query set.

## Removed Points

- **"510× speedup not properly caveated":** The paper clearly states this is for 4-attribute slice enumeration over naive enumeration (Section 5.2). It is adequately caveated.
- **"How is unbiasedness ensured?" (tag refinement):** The paper describes the multi-stage refinement process; "unbiased" here is used in a colloquial sense describing the refinement goal. This is an excessive nitpick.
- **"Instruction-based prediction adds nothing new":** The paper distinguishes tag substitution (feature-space exploration) from instruction-based (GPT knowledge base without model error priors). The two serve different purposes, and the distinction is stated. The critic's speculation about redundancy is not grounded in an error in the paper.
- **"How many image pairs are sampled?":** While reproducibility could be improved, this level of operational detail is rarely specified in vision papers for LLM-based generation steps and is a relatively minor point not harming the core claims.

## Novel Insights

None beyond the paper's own contributions. The cross-model overlap analysis (86%/73%/31%) is the most distinctive empirical finding in the paper. The harsh critic and strength finder largely recapitulate the paper's own framing and results rather than offering new perspectives.

## Suggestions

1. **Clarify the data source for Table 1 explicitly.** Describe whether the predicted slices are evaluated on the validation set (and if so, clarify what "beyond the validation set" means — slices that were not previously enumerated vs. slices evaluated on unseen data), or on a separate hold-out pool. This is the single most important clarification needed.
2. **Add a quantitative evaluation of attribute/tag quality**, even a small-scale human rating study (e.g., 50 attributes × 3 raters on coherence and error-relevance) or a coverage metric (fraction of failure cases explained by at least one generated attribute).
3. **Add error bars (e.g., 95% CI or std) to Tables 1 and 2**, and ideally report per-run values or include a significance test comparing DebugAgent to HiBug.
4. **Include an ablation study** showing the contribution of the comparative attribute generation strategy (vs. direct GPT querying), and the impact of tag substitution vs. instruction-based prediction separately.
5. **Consider adding one additional baseline comparison** on a shared task where comparison is feasible (e.g., AdaVision on the ImageNet bear classification task), or at minimum discuss the practical obstacles more concretely.
