Now I have a good picture of the calibration landscape. Let me write the consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

This paper proposes **Continuous Online Action Detection (COAD)**, a new task formulation that combines online action detection with single-pass adaptation from streaming video, enabling models to learn on-the-fly from continuous egocentric video streams. The authors introduce **Ego-OAD**, a large-scale benchmark curated from Ego4D MQ with 87 classes, ~23K instances, and 263 hours of video, and develop three training strategies—state continuity, orthogonal gradient projection, and non-uniform loss weighting—for adapting an RNN-based detection head. Results on Ego-OAD and EPIC-KITCHENS show improvements in top-5 recall over baselines, with a focus on balancing adaptation to the in-stream data and generalization to unseen out-of-stream data.

## Strengths

1. **Well-motivated and timely new task formulation**: COAD bridges offline OAD training and real-world deployment, enabling models to learn continuously from streaming video without storing data or replay. The motivation is clearly articulated and the paradigm aligns well with emerging interests in on-device training and personalized egocentric AI.

2. **Large-scale, realistic benchmark contribution**: Ego-OAD, curated from Ego4D MQ with 87 classes, 22,991 instances, 263 hours of video, and 36% multi-label overlap, fills a real gap in egocentric OAD evaluation. Table 4 demonstrates that egocentric pretraining provides meaningful gains on this benchmark (30.0 mAP with EgoVLP vs. 26.4 with Kinetics), confirming the dataset captures domain-specific patterns that matter.

3. **Systematic ablation isolating each component's contribution**: Table 3 cleanly separates the effect of each proposed strategy. Removing orthogonal gradient drops out-of-stream Top-5 Recall by 4.5pp (76.0→71.5), and removing non-uniform loss drops out-of-stream mAP by 4.2 (26.0→21.8). This provides clear causal evidence that the full configuration is necessary for best generalization.

4. **Demonstration that COAD narrows the gap to IID training**: Figure 4 shows that as COAD processes more in-stream data, out-of-stream mAP and Top-5 Recall steadily rise toward the offline IID upper bound, despite the strict single-pass constraint. This offers concrete visual evidence of effective continuous learning.

## Weaknesses

### Fatal
None.

### Major

1. **No confidence intervals or multi-run statistics reported**: All experiments appear to be single runs. The key mAP comparison between COAD and w/o COAD on out-of-stream egocentric pretraining is only 26.0 vs. 25.5 (+0.5 mAP). Given the small margins and the high variance typical of online/incremental experiments, it is plausible that the main mAP results are not reproducible or could flip with a different seed. The ablation ordering in Table 3 is similarly fragile without variance estimates. This is the single most significant evidential gap in the paper.

2. **Method evaluation relies primarily on Top-5 Recall while mAP gains are marginal**: The headline claims ("up to 20% improvement" and "up to 7% improvement") are drawn from Top-5 Recall. On the more standard OAD metric—mAP—the improvement over the w/o COAD baseline is modest at best: +0.5 mAP (out-of-stream, ego) and +1.5 mAP (out-of-stream, exo), while in-stream COAD is flat or worse (36.8 vs. 39.0 for ego pretraining). The paper does not adequately acknowledge or discuss this gap between the two metrics. Since both metrics are reported, the authors should address why Top-5 Recall is the appropriate target for the community's interest.

3. **Baseline comparison is limited to an ablated version of the same model**: The only adaptation baseline ("w/o COAD") is the same architecture without the three proposed strategies—essentially an ablation control. There is no comparison to other adaptation methods that could be applied in this setting, such as Elastic Weight Consolidation, experience replay, standard SGD-finetuning with a small learning rate, or simpler gradient decorrelation methods. This makes it difficult to assess whether the proposed combination of techniques offers a meaningful advance beyond straightforward online fine-tuning.

### Minor

1. **The evaluation protocol's weak pretraining may exaggerate adaptation gains**: The pretraining set contains only 186 videos vs. 1,177 in-stream videos. While the paper acknowledges this is a "weak initialization," the large data skew means the headline gains partly reflect moving from a data-starved initial model to a model that sees much more data—a scenario that may not hold when reasonable pretraining on the full Ego4D corpus is available. The paper would benefit from demonstrating that COAD gains persist with stronger pretraining.

2. **In-stream performance trade-off is underexplained**: Table 3 shows the full COAD achieves lower in-stream mAP (36.8) than several ablated variants (e.g., state cont. + orth. grad. without non-uniform loss reaches 42.4). While the paper frames this as "balancing adaptation and generalization," the asymmetry is striking: the generalization gain is only +0.5 mAP while the in-stream cost is -2.2 mAP relative to w/o COAD. This deserves deeper analysis.

3. **No computational cost or runtime analysis**: The paper argues RNNs are suitable for resource-constrained devices and on-device training but provides no measurements of latency, throughput, parameter update counts, or memory usage for the orthogonal gradient projection. Such measurements would substantially strengthen the practical relevance claims.

4. **No analysis of forgetting**: In continuous single-pass training, the model may forget earlier patterns as the stream evolves. The paper does not measure whether COAD experiences less forgetting than the baseline (e.g., performance trends over time or on early vs. late data), despite the orthogonal gradient method being designed to mitigate interference.

### Trivial

None.

## Nice-to-Haves

- A brief comparison showing how simple online SGD-finetuning (with small LR, no special strategies) performs would isolate whether the proposed techniques add value beyond straightforward adaptation.
- An analysis of label efficiency: the non-uniform loss is claimed to improve label efficiency, but no experiment measures actual label usage (e.g., how many labels are consumed vs. frame-wise supervision).
- A discussion of why one-step gradient decorrelation (only orthogonal to g_{t-1}) is sufficient, rather than maintaining a buffer of recent gradients for longer-range decorrelation.

## Removed Points

*Points flagged for removal; treat with caution.*

- **"Headline claims are overstated relative to the evidence"**: The abstract claims "up to 20% improvement in top-5 accuracy" and "up to 7% improvement in generalization." Table 1 shows max Δ Top-5 Recall of 22.5pp (In-stream, Exo) and 6.9pp (Out-of-stream, Ego). The numbers are accurately stated and the "up to" qualifier is appropriate. The critic conflates metric preference (mAP vs. Top-5) with accuracy of reporting. The real concern (small mAP gains) is already captured in Major weakness 2.

- **"Orthogonal gradient projection borrowed without justification"**: The paper properly cites Han et al. (2025) and the ablation in Table 3 shows it provides a clear benefit (out-of-stream Top-5 Recall drops 4.5pp without it). Asking for comparisons to other gradient decorrelation methods is scope creep for this paper.

- **"Does not consider lightweight Transformer variants"**: The paper explicitly scopes itself to RNNs for efficiency reasons. This is a design choice, not a flaw.

- **"Missing related works"**: Cannot be verified without external sources; the paper covers the relevant OAD literature adequately.

- **"Formatting/style nitpicks"**: Parser artifacts, not author errors.

- **"Missing appendix details"**: The appendix content is stripped by the parser; these details exist in the original submission.

## Novel Insights

The harsh critic correctly identifies that the paper's empirical foundation is weaker than its ambitions—the headline numbers come from Top-5 Recall while mAP gains are thin, and the lack of statistical grounding makes the 0.5 mAP gap between COAD and w/o COAD uninterpretable. However, neither reviewer fully explores the implications of the in-stream/out-of-stream framing. The paper's most interesting finding is that forced trade-off: COAD sacrifices in-stream mAP (36.8 vs. 39.0 for w/o COAD) while modestly improving out-of-stream mAP (26.0 vs. 25.5). If this asymmetry is real—rather than noise—it suggests the orthogonal gradient + non-uniform loss combination acts primarily as a regularizer that prevents overfitting to the stream, not as a mechanism for adaptation per se. The value of the task formulation and benchmark may ultimately outlast the specific method proposed here.

## Suggestions

1. **Add multi-run experiments with confidence intervals** — this is the highest-leverage improvement. Even 3 seeds with mean ± std would significantly strengthen the paper and make the small mAP differences interpretable.
2. **Compare against a simple online fine-tuning baseline** (standard SGD with small LR, no gradient projection, no non-uniform loss, but with state continuity) to isolate whether the proposed strategies add value over straightforward adaptation.
3. **Acknowledge and discuss the mAP vs. Top-5 Recall gap explicitly** — either justify why Top-5 Recall is the right primary metric for this setting, or calibrate the claims in the abstract to reflect the mAP results.
4. **Consider testing with a larger pretraining set** to show that COAD gains persist when the initial model is reasonably strong, not just when it is intentionally weak.

## Score and Decision

My initial bracketing placed the paper between the weak anchors (avg <3.5: clear rejects) and the strong anchors (avg >7.5: strong accepts). Round 1 identified the paper as plausibly in the 3.5–7.5 range. 

Round 2 narrowed this by retrieving anchors in the (4.0, 5.5) and (5.0, 6.5) bands for similar topics. Comparing the paper to these anchors:

- **PARSE-Ego4D** (avg 5.5, **Rejected**): A pure dataset/benchmark paper from Ego4D, criticized as "too thin for a main conference paper." Our paper has more substance (task formulation + method + dataset) but the method evaluation is notably weaker. The paper under review is comparable or slightly below.

- **Solving New Tasks by Adapting** (avg 5.75, **Accepted Poster**): Has thorough experiments, clear baselines, and quantitative comparisons. Our paper falls below this anchor due to weaker evaluation (no error bars, limited baselines).

- **MetaAdapter** (avg 5.4, **Rejected**): Method paper with clear experimental issues (unclear descriptions, missing comparisons). Our paper has a similar profile—a reasonable method with evaluation gaps—but the task formulation provides additional novelty.

- **ZeroI2V** (avg 6.0, **Rejected**): Had significant gains and clear method but was rejected over terminology concerns. Our paper's evaluation issues are more fundamental (no error bars, small mAP gains).

- **C-CLIP** (avg 6.5, **Accepted Poster**): Multimodal continual learning with strong experiments and comparisons. Our paper is clearly below this level.

The paper sits between the weaker rejects (4.0–5.0) and the borderline papers (5.5–6.0) that sometimes get accepted. The COAD task formulation and Ego-OAD benchmark are legitimate contributions, but the method evaluation is insufficient to support the claimed advantages. Given the lack of error bars, the small mAP margins, and the limited baselines, the paper falls below the ICLR acceptance bar.

**Round 1 bracket**: 3.5–7.5 → narrowed to approximately 4.5–5.5 in Round 2.

The paper is closest to anchors around 5.0 (marginally below acceptance threshold). It is stronger than the <4.0 papers which had fatal flaws, but weaker than the 6.0+ papers which had solid experiments and evaluation. The task formulation and benchmark are valuable, but the evaluation is not yet at the level required for acceptance. Score of **5.0** reflects a paper with a genuinely interesting idea and a useful benchmark, held back by evaluation that does not convincingly support the method claims.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>