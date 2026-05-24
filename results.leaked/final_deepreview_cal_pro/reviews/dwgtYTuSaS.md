Now I have all the calibration data I need. Let me synthesize the final review.

---

## Summary

This paper introduces Continuous Online Action Detection (COAD), a new task formulation that extends standard Online Action Detection (OAD) by requiring models to simultaneously detect actions and continuously learn from streaming egocentric video in a single causal pass, without storing data. To support this task, the authors curate Ego-OAD, a 263-hour benchmark derived from Ego4D Moment Queries with 87 fine-grained action classes and 22,991 temporally grounded action instances. They propose three training strategies — hidden-state continuity, orthogonal gradient projection, and non-uniform loss — that align training dynamics with streaming inference constraints. Experiments demonstrate up to 22.5% Top-5 Recall improvement on in-stream adaptation and up to 6.9% Top-5 Recall improvement on out-of-stream generalization, with cross-dataset validation on EPIC-KITCHENS.

## Strengths

- **Novel task formulation**: COAD fills a genuine gap between offline OAD training and real-world deployment on wearable devices. The constraints (single-pass, causal, no data storage) are well-motivated and clearly defined, creating a distinct and practically relevant problem setting.

- **Substantial benchmark contribution**: Ego-OAD provides a large-scale (263h, 87 classes, 22,991 instances, multi-label with 36% overlapping actions) egocentric testbed for OAD research. The curation process — merging annotator passes and grouping free-form descriptions into unified classes — produces a realistic benchmark that captures the ambiguity of real-world egocentric video.

- **Well-ablated training strategies**: Table 3 provides clear evidence that each proposed component matters. Non-uniform loss contributes +4.2 mAP and +8.3 Top-5 Recall on out-of-stream generalization; orthogonal gradient projection adds +4.5 Top-5 Recall. The ablation directly supports the paper's design choices.

- **Thorough experimental analysis**: Beyond the main results, the paper provides a trade-off analysis (Figure 3) showing performance under varying stride and learning rate, a performance-over-time plot (Figure 4) demonstrating convergence toward an IID upper bound, qualitative results (Figure 5), and cross-dataset validation on EPIC-KITCHENS (Table 2). The experiments substantiate the headline claims.

- **Practical label efficiency demonstration**: Figure 3 shows that even with a stride of 128 (loss computed roughly every 68 seconds), out-of-stream mAP drops only marginally while still improving adaptation — a practically meaningful result for deployment.

## Weaknesses

### Fatal

None.

### Major

None that rise to the level of threatening the core contribution. The issues below are addressable through revisions and do not undermine the paper's central claims.

### Minor

- **Ambiguous dataset split description**: The paper states that the three Ego-OAD splits "correspond to the original Ego4D MQ validation split," but it is unclear whether this statement refers only to the out-of-stream test set (519 videos, matching the MQ validation size) or to all three splits collectively. The provenance of the pretraining (186) and in-stream (1,177) videos — presumably drawn from the MQ training split — should be stated explicitly. This does not invalidate the results but creates ambiguity for reproducibility and for assessing potential pretraining data overlap with feature extractors like EgoVLP.

- **Overstated label-efficiency claim**: Section 4.5 states that the non-uniform loss "allows training with sparse instead of dense frame-level annotations," implying this is a COAD-specific benefit. However, as the paper itself acknowledges, this strategy follows MiniROD (An et al., 2023) and is already an established practice in offline OAD training. The claim should be reframed to emphasize that this technique is *particularly compatible* with the COAD setting rather than being enabled by it.

- **Weak in-stream adaptation on EPIC-KITCHENS**: Table 2 shows that both COAD and the w/o COAD baseline struggle to adapt effectively on EPIC-KITCHENS, with COAD's in-stream action mAP (7.9) falling below the Pretrained Only baseline (9.6). The paper attributes this to fine-grained annotations, but the negative result is noted only briefly and limits the generality claims.

- **Presentation of Table 2**: The dual out-/in-stream numbers per cell are difficult to parse without clear column headers indicating which number corresponds to which setting. The text reports nearly flat out-of-stream gains, and the table undercuts the otherwise consistent story from Table 1.

### Trivial

- The "Baseline" reference in Figure 3 is not labeled in the caption, and the IID upper bound in Figure 4 is discussed only qualitatively — reporting concrete numbers would sharpen the comparison.
- The w/o COAD baseline could be specified more precisely: whether it resets the RNN hidden state between training windows and whether it uses uniform per-frame loss is stated indirectly through the description of what it omits rather than what it does.
- The choice to limit orthogonal gradient projection to a single preceding gradient (rather than a running buffer of past gradients) is not discussed.

## Nice-to-Haves

- Reporting computational cost (throughput, memory usage, parameter update overhead) during single-pass training would ground the method in its stated motivation of resource-constrained wearable deployment.
- A direct comparison to a fully IID-trained model (on combined pretraining + in-stream data) in the main results table, rather than only in Figure 4, would give readers a concrete ceiling for the single-pass constraint.
- Discussion of whether storing more than one past gradient for the orthogonal projection could improve decorrelation, or justification for why one step suffices.

## Removed Points

These points are flagged to be removed; treat them with caution.

1. **"Dataset splits and potential data leakage (evidential)" from Harsh Critic** — The claim that EgoVLP pretraining may overlap with COAD splits is speculative and cannot be verified from the paper. The paper cites EgoVLP as a feature extractor; questioning whether EgoVLP saw the test videos during pretraining is a general concern applicable to any paper using pretrained features on Ego4D, not a specific flaw of this paper. However, the *ambiguity* in the split description itself is a real clarity issue (retained as Minor).

2. **"Missing appendix / inaccessible details" from Harsh Critic** — The parser strips appendices. The original submission includes Appendix A for class grouping details. This is not a valid criticism.

3. **"Brief discussion of prior work on continual/online learning for video" from Harsh Critic** — The paper already cites Carreira et al. (2024) and Han et al. (2025) in the context of continuous video learning. Adding more references is a nice-to-have, not a weakness.

4. **"Orthogonal gradient uses only one step" demanding discussion** — This is retained as Trivial, not elevated to a major concern. The paper demonstrates the one-step approach works; discussing alternatives is a nice-to-have.

5. **"Redundancy between hidden state and overlapping windows" from Harsh Critic** — This is a vague concern without a specific anchor in the paper's results. The paper shows state continuity provides modest gains (Table 3); speculating about redundancy without evidence is not a valid weakness.

6. **Strength Finder: "Cross-dataset evaluation on EPIC-KITCHENS confirms method is not dataset-specific"** — This strength is partially undermined by the weak in-stream results on EPIC-KITCHENS. The out-of-stream gains are real but modest, and the in-stream adaptation actually fails. The strength is retained but tempered.

## Novel Insights

The paper's integration of orthogonal gradient projection — originally developed for general continuous video learning (Han et al., 2025) — into the OAD-specific training pipeline reveals an interesting interaction: gradient decorrelation primarily benefits *out-of-stream generalization* (+4.5 Top-5 Recall) rather than in-stream adaptation, suggesting that the temporal correlation problem in streaming video is more about preventing overfitting to the stream than about improving within-stream learning. This is a subtle but important distinction for future work in continuous OAD.

## Suggestions

- Explicitly state the Ego4D partition origin (train/val/test) for each of the three Ego-OAD subsets. A single sentence clarifying that pretraining and in-stream sets are drawn from the MQ training split and the out-of-stream set from the MQ validation split would resolve the main reproducibility concern.
- Rephrase the label-efficiency claim in Section 4.5 to acknowledge that non-uniform loss follows MiniROD and emphasize its *compatibility* with COAD rather than presenting sparse supervision as a COAD-specific innovation.
- Add column sub-headers to Table 2 (Out/In) to make the dual-number format immediately interpretable.
- Report the concrete IID upper-bound numbers referenced qualitatively in Figure 4 to give readers a clear ceiling for the single-pass constraint.

## Score and Decision

**Round 1 bracket**: Based on the initial calibration search, the paper sits between approximately 4.5 and 7.5. The weak anchors (<3.5) are clearly below; the strong anchors (>7.5) are topically distant but represent a higher tier of contribution and polish.

**Round 2 narrowing**: The paper is compared against these anchors:
- `7L2bpe7lfm` (4.50, video continual learning): Below our paper — weaker methodology, insufficient novelty, unclear problem setup.
- `Y7jJN0VQ4y` (5.71, continual WSVAD): Below our paper — similar task-formulation spirit but with validity concerns about the task setting and less thorough experiments.
- `qnAZqlMGTB` (5.75, StreamingBench): Below our paper — benchmark-only contribution where tasks could be reformulated as offline; our paper has both benchmark and method.
- `P6G1Z6jkf3` (6.00, hand-object dynamics): Comparable — similar structure (data pipeline + model), solid results, some missing analyses.
- `67sSPPAZiG` (6.00, MMEgo): Comparable — benchmark + model paper with some concerns about incremental contribution.
- `8J2DrrWDKE` (6.67, X-Gen): Slightly above — more novel technical approach, strong results, but some marginal gains concern.
- `M8gXSFGkn2` (7.00, EgoHOIBench): Above our paper — more polished benchmark construction, more extensive experiments across models, clearer framing.

The paper compares most closely to the 6.00 anchors (P6G1Z6jkf3, 67sSPPAZiG) — it shares their pattern of a solid multi-pronged contribution (benchmark + method) with some clarity and framing issues. It falls below the 6.67-7.00 tier due to ambiguous dataset documentation, one overstated claim, and weaker cross-dataset results. The core contributions are genuine and the experimental validation is thorough, placing it at **6.0**.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>