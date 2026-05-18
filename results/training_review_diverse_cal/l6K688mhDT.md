Now I have a thorough understanding. Let me synthesize the final review.

## Summary

This paper studies how the imbalanced distribution of *pre-training* data (called "parameter imbalance") persists through fine-tuning and affects downstream long-tail tasks. The authors show empirically that (1) this parameter imbalance is more impactful than standard downstream "data imbalance," (2) it cannot be fixed by logit-adjustment methods that target data imbalance, and (3) they propose a causal backdoor adjustment that averages predictions from multiple foundation models (CLIP, OpenCLIP, MetaCLIP) fine-tuned with Logit Adjustment, achieving strong results on ImageNet-LT, Places365-LT, and iNaturalist2018.

## Strengths

- **Formalizes and empirically distinguishes parameter imbalance from data imbalance.** The paper defines parameter imbalance (Def. 1) and provides clear experimental evidence (Figs. 2–3, Tabs. 3–4) that it persists even after data imbalance is corrected via Logit Adjustment. The nine-group analysis (Fig. 2) showing that "Tail-Tail" (D-Few × P-Few) classes suffer most is a genuinely useful diagnostic.

- **Strong empirical results across multiple long-tailed benchmarks.** The method achieves state-of-the-art or competitive results on ImageNet-LT (+3.49% on D-Few over LIFT), Places365-LT (+2.91% overall over VL-LTR), and iNaturalist2018 (+1.91% over RAC), with consistent gains especially on tail classes.

- **Ablation confirms the core mechanism.** Figure 6 shows that the proposed method improves over LA across all nine parameter×data groups, with the largest gains in P-Few groups (+1.32% to +1.50%). Table 8 shows that increasing the number of foundation models M improves performance, directly supporting the claim that diverse semantic factors help.

- **Honest about computational trade-offs.** Table 9 reports inference cost scaling with M, and the paper discusses the performance-efficiency trade-off.

## Weaknesses

### Fatal
None.

### Major

1. **Missing baseline: ensemble of LA-fine-tuned models confounds causal adjustment with ensembling.** The proposed method (Sec. 5.2) fine-tunes multiple foundation models (CLIP, OpenCLIP, MetaCLIP) with LA and averages their predictions with equal weights. Mathematically, this is an ensemble of LA-fine-tuned models. The ablation in Table 8 shows that more models → better performance, which is exactly what any ensemble would do. The paper compares only against single-model methods (LIFT, VL-LTR, RAC, etc.) and never against a simple ensemble of the same three models fine-tuned with LA (or CE). Without this baseline, the reader cannot tell whether the improvement comes from the causal framing or from the well-known benefits of ensembling. This is the single most critical missing experiment: it directly tests whether the backdoor adjustment contributes anything beyond combining diverse models.

### Minor

2. **Causal graph framing is conceptually loose.** The paper identifies the incomplete semantic factor C as a confounder creating the backdoor path X ← C → Y (Sec. 5.1). While the overall intuition (different models attend to different partial features) is reasonable, the justification that C causally affects the input distribution X is somewhat abstract. The graph conflates D (parameter imbalance, a property of pre-training) with C (incomplete semantic factor, a property of the model's feature space), and the figure caption says "We view parameter imbalance as the confounder" while the text correctly identifies C as the confounder. The causal story is not wrong per se, but it is more metaphorical than formally identified, and the paper would benefit from either tightening the graph or being more explicit about its limitations as a conceptual model.

3. **Claims about "parameter imbalance is more important" are scoped to PEFT, but not always stated as such.** Section 4.1 states that "parameter imbalance plays a more vital role than data imbalance" based on experiments using AdaptFormer and VPT. The paper acknowledges (line 162) that PEFT preserves pre-trained information (including its biases), but the broader claim could be misinterpreted as holding under full fine-tuning. The paper should either test full fine-tuning or consistently qualify this claim.

4. **Estimated label prior \(\widehat{\mathbb{P}}_P(Y)\) is treated as ground truth without sensitivity analysis.** The entire analysis of "P-Many/P-Medium/P-Few" groups, the nine-group breakdown, and the GLA-Train failure all depend on this estimate. The paper does not examine how sensitive its conclusions are to errors in this estimate (e.g., via synthetic priors or alternative estimation methods). While the estimation via GLA is a reasonable starting point, the lack of robustness analysis weakens the evidence for claims about parameter imbalance's fundamental nature.

5. **The "incomplete semantic factor" interpretation is not directly validated.** The paper treats CLIP, OpenCLIP, and MetaCLIP as proxies for different incomplete semantic factors and uses Grad-CAM visualizations (Fig. 4) to suggest they attend to different regions. However, no quantitative analysis (e.g., measuring prediction complementarity, correlation of errors across models) is provided to verify that these models actually capture distinct semantic information. If their errors are highly correlated, the ensemble gains would be limited and the "factor" interpretation weak.

### Trivial
None.

## Nice-to-Haves

- Adding class-wise KNN accuracy (rather than just overall) would strengthen the feature representation analysis in Table 4.
- A comparison with full fine-tuning (or at least a discussion of why it is not expected to change the conclusion) would clarify the scope of the parameter imbalance claim.
- A sensitivity analysis varying the \(\widehat{\mathbb{P}}_P(Y)\) estimation method would increase confidence in the group-level analyses.

## Removed Points

- **Criticism that the causal graph is "fundamentally misaligned" and that the backdoor adjustment "is not justified."** After careful reading: the causal graph shows D (parameter imbalance) → C (incomplete semantic factor), C → X (data generation), and C → Y (prediction). The confounder C is the incomplete semantic factor (what features the model extracts), and the backdoor path X ← C → Y is a standard confounder structure. The reviewer appeared to conflate D with C. The graph is abstract but not incorrect for the conceptual story being told. This point is downgraded from Fatal to Minor (item 2 above).

- **Criticism that "GLA-Train failure is insufficiently diagnosed."** The paper provides KNN analysis (Table 4), the nine-group breakdown, and experimental results showing GLA-Train ≈ LA. While more analysis is always possible, the evidence provided is sufficient to support the empirical finding. The strong conclusion that this proves a "fundamental difference" may be overstated, but the empirical observation stands.

- **Criticism about missing appendix (Sec. D.7).** Per policy, parser-stripped appendix content is not a valid criticism.

- **Criticism about zero-shot D-Few > D-Many results being explainable by alternative factors.** The paper uses this as one piece of suggestive evidence for parameter imbalance; it is not the sole basis for the claim and does not need to rule out all alternatives.

- **Criticism about computational cost analysis.** The cost analysis honestly reports the total cost; separating per-model vs. ensembling overhead would be nice but is not a weakness.

## Novel Insights

None beyond the paper's own contributions. The key novel observation — that pre-training imbalance persists through PEFT in a way that logit adjustment cannot fix — is the paper's own finding, and the reviews do not add additional insight beyond what the authors already present.

## Suggestions

1. **Add the critical ensemble baseline.** Ensemble the same three models (CLIP, OpenCLIP, MetaCLIP) fine-tuned with standard LA (or even CE) using equal-weight averaging. If the proposed method outperforms this baseline, the causal framing is supported. If not, the paper should be reframed as "an analysis of parameter imbalance + an effective ensemble method," which is still a useful contribution.

2. **Clarify the causal graph.** Either (a) provide evidence that the incomplete semantic factor indeed causally affects X through data generation, or (b) revise the description to make clear this is a conceptual/analogical model rather than a formal causal identification.

3. **Qualify the scope of claims.** Make explicit throughout that findings about "parameter imbalance" were established under PEFT-based fine-tuning, and note whether full fine-tuning is expected to behave differently.

4. **Add a sensitivity analysis** for \(\widehat{\mathbb{P}}_P(Y)\) to show that the group-level conclusions (P-Few, etc.) are robust to estimation method choices.

## Score and Decision

The paper makes a genuinely useful empirical observation — that pre-training imbalance persists through PEFT and resists logit-adjustment-based correction — and backs this with solid experiments across three benchmarks. The proposed method achieves strong results. However, the major weakness (missing ensemble baseline) means the claimed contribution of the causal backdoor adjustment is not properly separated from trivial ensembling. This is a significant gap that prevents full acceptance of the paper's stated contribution. The paper would be strengthened substantially by addressing this and could become a clear accept with revision.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>