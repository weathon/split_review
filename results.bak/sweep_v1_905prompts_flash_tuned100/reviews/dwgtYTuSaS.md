Now let me write the final consolidated review.

## Summary

This paper proposes *Continuous Online Action Detection* (COAD), a task formulation that extends standard online action detection by requiring models to also learn and adapt from streaming video in a single causal pass, without data storage or replay. The authors curate Ego-OAD, a large-scale egocentric OAD benchmark from Ego4D (87 classes, 22,991 instances, 263 hours), and introduce three training strategies—state continuity, orthogonal gradient projection, and non-uniform loss weighting—to enable effective single-pass streaming training. Results on Ego-OAD show improvements of up to 16% Top-5 Recall on in-stream data and up to 7% on out-of-stream data over a pretrained-only baseline.

## Strengths

1. **Novel and well-motivated task formulation.** COAD is a clearly defined extension of standard OAD that bridges offline training and real-time deployment. The constraints — single-pass, causal, no data storage or replay — are concretely specified (Section 4.5) and are directly relevant to on-device egocentric AI on wearable devices. No prior OAD work addresses this setting.

2. **Large-scale egocentric OAD benchmark (Ego-OAD).** The dataset fills a clear gap in the literature: existing egocentric OAD datasets are small, kitchen-restricted, or not designed for online detection. Ego-OAD provides 87 action classes, 22,991 labeled instances, and 263 hours of untrimmed video, with multi-label annotations that handle overlapping actions (36% of instances overlap). This is a genuine community contribution.

3. **Clean ablation showing each component contributes.** Table 3 systematically ablates the three training strategies: orthogonal gradient improves out-of-stream Top-5 Recall by +4.5%, non-uniform loss boosts mAP by +4.2%, and state continuity provides smaller consistent gains. The full configuration achieves the best out-of-stream generalization, and the trade-off pattern (in-stream vs. out-of-stream) is physically meaningful and well-documented.

4. **Demonstrated improvements on Ego-OAD are real and non-trivially large on Top-5 Recall.** On the primary benchmark with egocentric pretraining, COAD achieves +16.0 absolute points (21.8% relative) in-stream Top-5 Recall and +6.9 absolute points out-of-stream vs. the pretrained-only baseline (Table 1). While mAP gains are more modest, the recall gains suggest meaningful improvement in covering the set of relevant actions — an important dimension for assistive applications.

## Weaknesses

### Fatal
None.

### Major

1. **Experimental comparison is limited to self-designed baselines.** The paper compares only against *Pretrained Only* and *w/o COAD* (the same model trained on in-stream data without the proposed strategies). There is no comparison against standard offline-trained OAD methods of different architectures (e.g., LSTR, TeSTra, GateHub) that could be applied to the same data. While the IID upper bound in Figure 4 partially addresses this by providing an offline multi-pass baseline, the lack of comparisons to established OAD models makes it difficult to assess whether the architectural choice (GRU) is adequate for this task. The paper's core claim — that "COAD enables models to learn from streaming video" — would be strengthened by showing that the GRU-based COAD method can approach or match the out-of-stream performance of stronger offline architectures trained on the same data.

2. **Modest out-of-stream mAP gains over the w/o COAD baseline.** On the key out-of-stream generalization metric, COAD's mAP advantage over w/o COAD is 0.5 points (ego pretraining) and 1.5 points (exo pretraining). These differences are reported without confidence intervals or statistical significance tests, making it unclear whether they are reliable. The Top-5 Recall gains are more substantial (4.4 and 4.2 points respectively), but mAP is the more standard metric in OAD, and the paper would benefit from acknowledging this discrepancy and providing a significance analysis.

3. **EPIC-KITCHENS results undermine the generality claim.** While the harsh critic's specific complaint about Table 2 was based on a misreading (the critic confused in-stream and out-of-stream columns), the actual numbers still show a concerning pattern: COAD's in-stream Action mAP is 7.9 vs. Pretrained Only's 9.6, and COAD's in-stream Action Top-5 Recall is 20.5 vs. Pretrained Only's 22.9. On out-of-stream, COAD does better (9.9 vs. 8.6 Action mAP), but the overall story is mixed. The paper attributes difficulties to "fine-grained nature of the actions," but this limits the generality claim in the abstract ("establishes a foundation for responsive and adaptive first-person AI systems") — many real-world egocentric scenarios involve fine-grained actions.

### Minor

1. **The w/o COAD baseline could be more precisely described.** The phrase "trained on in-stream data without applying any of the proposed strategies" is open to interpretation. A more precise description would clarify whether this baseline (a) uses the same single-pass streaming protocol as COAD but without the three strategies, or (b) uses offline IID multi-pass training without the strategies. The "Adaptation ✓" column marker and the fact that w/o COAD achieves higher in-stream mAP than COAD (consistent with naive streaming SGD overfitting) suggest the former, but the paper should state this explicitly.

2. **No confidence intervals or statistical tests.** Several key comparisons (Table 1: 26.0 vs 25.5 out-of-stream mAP; Table 3 ablation variants) report small differences without error bars. This is a standard weakness but important to flag given the modest margins.

3. **The IID upper bound in Figure 4 is not fully described in the caption.** The paper mentions it in the text ("offline with multiple passes over the combined pretraining and in-stream data") but the figure caption refers to it only as "IID training." A clearer description in the caption would help readers.

### Trivial
None.

## Nice-to-Haves
- Comparison against one established OAD model (e.g., MiniROD or a lightweight Transformer) trained offline on the combined pretraining + in-stream data, to show where COAD sits relative to the offline state of the art.
- Analysis of the orthogonal gradient mechanism's effect on gradient norms or gradient flow, beyond the ablation in Table 3.
- A brief discussion of why the orthogonal gradient uses only the immediately preceding gradient g_{t-1} rather than a longer history, since storing one extra gradient vector does not violate the no-data-storage constraint.

## Removed Points

These points were raised by reviewers but are removed in the final review for the reasons given:
- **"No comparison to any existing OAD method"** — downgraded from Fatal to Major. The paper does include an IID training upper bound (Figure 4) that represents offline multi-pass training on the full data, which partially addresses this. The claim that "standard OAD methods are fully applicable to the streaming setting" conflates inference-only OAD with the COAD paradigm (single-pass training without data storage). The paper's contribution is about the *training paradigm*, not a new architecture; comparing against Transformer-based OAD methods would require adapting them to the streaming single-pass constraint, which is non-trivial.
- **"The w/o COAD baseline is ambiguously defined and potentially unfair"** — removed. The paper describes w/o COAD as "the same model trained on in-stream data without applying any of the proposed strategies," and marks it with "Adaptation ✓." There is no evidence in the paper that w/o COAD is trained offline with multiple passes; the critic's speculation is contradicted by the paper's own description. The higher in-stream mAP of w/o COAD (39.0 vs 36.8) is consistent with naive streaming SGD without regularization, not with unfair offline training.
- **"EPIC-KITCHENS results do not support the claimed generality — Action mAP Pretrained 9.6 vs COAD 7.9"** — corrected. The critic confused out-of-stream and in-stream columns. The actual out-of-stream Action mAP is COAD 9.9 vs Pretrained 8.6 (COAD wins). The point about mixed in-stream results on EPIC-KITCHENS is retained as Major #3.
- **Strength Finder: "Training strategies that significantly improve both adaptation and generalization"** — retained but qualified. The gains are substantial on Top-5 Recall but modest on mAP. The paper's own framing using "up to 20% improvement" references Top-5 Recall, which is accurate.
- **Strength Finder: "Validation on a second dataset (EPIC-KITCHENS)"** — weakened. The results are genuinely mixed and the paper's own discussion acknowledges limitations. Retained as a minor positive but not a strong point.
- **Formatting/style nitpicks** — removed per policy.
- **Missing related work complaints** — removed per policy (cannot verify without external sources).
- **Reproducibility nitpicks about undisclosed hyperparameters** — removed per policy. The paper provides reasonable implementation details.

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Add one strong offline baseline.** Compare COAD against a well-established OAD model (e.g., a lightweight Transformer or even MiniROD with more capacity) trained offline on the combined pretraining + in-stream data with IID multi-epoch sampling. This would directly answer whether continuous learning is beneficial beyond what a strong offline model can achieve.
2. **Report confidence intervals or error bars** on the key comparisons in Tables 1 and 3, especially for the small-margin results (out-of-stream mAP).
3. **Clarify the w/o COAD training protocol explicitly** in a single sentence: "w/o COAD uses the same single-pass streaming protocol as COAD, with no hidden state reset and batch size 1, but without orthogonal gradient projection, non-uniform loss, or state continuity."
4. **Acknowledge the generality limitation** on fine-grained action datasets more prominently in the abstract and conclusion, or add an experiment showing that with longer windows or higher feature rates the EPIC-KITCHENS in-stream gap narrows.

## Score and Decision

**Bracket (Round 1):** After reviewing the paper and comparing against anchors in the low (avg &lt; 3.5), middle (3.5–7.5), and high (&gt;7.5) bands, I initially bracket the paper between **5.0 and 6.5**. The closest topical anchors are PrAViC (4.25, Reject), "Anomalies are Streaming" (5.71, Reject), StreamingBench (5.75, Reject), EgoVideo (6.00, Accept), and MMEgo (6.00, Accept).

**Narrowing (Round 2):** Reading these anchors in full, the COAD paper is:
- Substantially stronger than PrAViC (4.25), which had unclear method description and missing baselines.
- Comparable to "Anomalies are Streaming" (5.71), which proposed a new continual learning task but had concerns about setting realism and missing baselines.
- Comparable to StreamingBench (5.75), which proposed a new task/benchmark but had some tasks that could be handled by offline methods.
- Slightly weaker than EgoVideo (6.00) and MMEgo (6.00), which had stronger experimental validation with clearer margins of improvement and broader evaluation.

**Final Score:** The paper's main contributions — a genuinely new task formulation and a large-scale benchmark — are valuable. The method is reasonable and the ablation is clean. However, the experimental validation has notable limitations: the comparison set is narrow, the mAP gains over the w/o COAD baseline are modest, the EPIC-KITCHENS results are mixed, and no significance testing is provided. These weaknesses prevent the paper from reaching the 6.0+ level of the strongest egocentric papers in the anchor set, but the contributions are real and the paper is clearly above the reject-level anchors (4.25–5.75).

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>