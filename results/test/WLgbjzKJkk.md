Now I have a thorough understanding of all claims. Let me produce the final review.

## Summary

This paper identifies a genuine weakness in end-to-end Transformer-based multi-object tracking (e2e-MOT): the standard Tracking-Aware Label Assignment (TALA) starves detection queries of positive training samples because tracked objects are exclusively assigned to tracking queries. The authors propose two complementary remedies: (1) **COLA** (COopetition Label Assignment), which allows detection queries in intermediate decoders to also be matched to tracked objects, boosting tracking query representations via self-attention; and (2) **Shadow Sets**, a one-to-set matching strategy where each query is expanded into multiple shadow queries that jointly predict the same target, with hard-mining training and representative selection at inference. On DanceTrack and BDD100K, CO-MOT achieves state-of-the-art results among end-to-end methods (69.4% HOTA, 52.8% TETA) while maintaining efficiency comparable to MOTR.

## Strengths

1. **Empirically grounded motivation with clear diagnostic evidence.** The paper pinpoints the root cause of e2e-MOT underperformance through a careful diagnostic study (Section 3.1). Table 1 quantifies that removing tracking queries at inference improves MOTR's mAP from 42.5% to 60.6%, and retraining as pure detection yields 66.1% — directly showing that tracking queries suppress detection. Figure 1 provides corresponding visual evidence of tracking termination caused by poor detection. This diagnostic is clean and reproducible.

2. **COLA improves tracking through detection-query cooperation, validated by attention analysis.** The coopetition assignment allows detection queries matched to tracked objects in intermediate decoders to enhance tracking query representations via self-attention. Figure 3 shows detection queries contribute >15% attention to corresponding tracking queries in decoders L>2, often exceeding self-attention contributions. Table 3a confirms this yields a +3.8% HOTA and +5.1% AssA gain over the baseline at no extra computational cost — an elegantly efficient improvement.

3. **Shadow sets provide a principled one-to-set matching strategy with careful design validation.** The concept of expanding each query into multiple noise-initialized shadows with max-cost training (hard mining) and min-score inference (conservative selection) is well-motivated. Tables 3b–3c systematically validate each design choice (initialization method, N_S=3, λ=max for training, φ=min for inference), providing clear practical guidance.

4. **State-of-the-art efficiency among e2e methods.** CO-MOT achieves 69.4% HOTA on DanceTrack and 52.8% TETA on BDD100K, outperforming prior e2e methods by meaningful margins. Section 4.5 and Figure 4 show it requires only 38% of MOTRv2's FLOPs (173G vs. ~455G) while matching its HOTA performance and running 1.4× faster, all without an external detector.

5. **Comprehensive ablation and honest limitations.** Tables 3a–3c systematically evaluate each component. Section 4.6 frankly acknowledges weaker performance on MOT17 (attributed to data scarcity) and difficulty with small/difficult targets — refreshing candor that strengthens credibility.

## Weaknesses

### Fatal
None.

### Major

1. **Query count and FLOPs configuration is ambiguous.** The paper contains an unresolved inconsistency in the query configuration. Section 3.3 defines total queries as $(N_T+N_D) \times N_S$, and Section 4.2 states "We use 300 initial queries." With $N_S=3$, this yields either:
   - **300 sets** → 900 total shadow queries (if "initial queries" = $N_T+N_D$), which raises questions about how FLOPs remain identical to MOTR's 173G despite a 3× increase in decoder queries.
   - **100 sets** → 300 total shadow queries (if "initial queries" = $(N_T+N_D) \times N_S$), which would reduce effective tracking capacity from 300 to 100 objects — a non-trivial constraint for crowded scenes like MOT17 that could explain the weaker results there.
   
   The paper never clarifies which interpretation is correct or discusses the capacity trade-off. Since the efficiency comparison (Figure 4) and the performance interpretation on MOT17 both hinge on this parameter, the ambiguity undermines the reader's ability to interpret the core empirical claims. **This is addressable in a revision** but as written it is a significant gap.

2. **Central motivation is not fully validated by the evidence presented.** The paper's narrative (Sections 1 and 3.1) argues that COLA fixes the problem that "detection queries have scarce positive samples" and "the detection will deteriorate." However, the ablation in Table 3a shows DetA changes minimally (71.8% → 73.5%), and the paper itself notes (line 165) that COLA "actually helps tracking" rather than detection. The actual mechanism — attention-based representation augmentation (Figure 3) — is different from the stated causal story of fixing detection deterioration. This does not diminish the empirical results, but the paper would benefit from aligning its motivation narrative with the mechanism the evidence actually supports. The requested Table-1-style mAP analysis with CO-MOT would directly clarify this.

### Minor

3. **Hyperparameter selection under mismatched training conditions.** The optimal λ, φ, initialization, and $N_S$ are determined in simplified settings: λ and φ are tuned without COLA, with a short 5-epoch schedule, random initialization ($I_{rand}$), and $N_S=5$; initialization is tuned with $N_S=2$ and COLA but not with the final $N_S=3$. The authors then transfer these choices to the full model (COLA, 20 epochs, $I_{noise}$, $N_S=3$). While this is common practice, the optimal values could shift under the combined setting. A joint ablation on the full model would strengthen the work.

4. **MOT17 results lag behind non-e2e methods.** Table 2c shows CO-MOT underperforms many non-end-to-end methods on MOT17. The paper plausibly attributes this to insufficient training data. However, given the query-count ambiguity (Issue 1), it is unclear whether the reduced effective capacity (if total queries are 100 sets) also contributes. An ablation on MOT17 validation separating data effects from capacity effects would be informative.

### Trivial
None.

## Nice-to-Haves

- Provide a pseudocode or algorithmic description of the full inference pipeline (how tracking queries, detection queries, and shadow sets produce the final tracklets).
- Report inference speed (FPS) relative to MOTR, not just relative to MOTRv2.
- Quantify how many positive assignments detection queries receive under TALA vs. COLA (a bar chart of matched detection queries per frame would substantiate the motivation).
- Clarify the distinction from H-DETR/Group-DETR more explicitly — the one-to-set strategy with hard mining within the set is the main differentiator, but the paper could position this more sharply.

## Removed Points

1. **"Undefined inference mechanism for avoiding duplicate predictions" (Harsh Critic Issue 1).** This criticism claims the paper "never describes how duplicate predictions are resolved." In fact, Section 3.4 (line 76) states: *"we remain the competition assignment for the L-th decoder to avoid trajectory redundancy during inference"* — the last decoder uses TALA, so detection queries trained only on newborns in that layer will not produce duplicate boxes for tracked objects at inference. For shadow sets, Section 3.5 (line 89) states: *"we select the box and score predictions of the shadow with the highest score as the tracking outputs"* — only one box per set is output. Both mechanisms are explicitly described. The criticism reflects a misreading of the paper.

2. **"Shadow set is akin to one-to-many" (from Other Observations).** The paper already acknowledges the connection to H-DETR/Group-DETR (lines 16, 83) and explains the difference: one-to-set matching treats the set as a unit with shared matching, unlike one-to-many auxiliary training. This is discussed, not omitted.

3. **Formatting/style nitpicks about Table 2a clarity.** These reflect parser artifacts, not author issues.

## Novel Insights

Beyond the paper's own contributions, the key insight that emerges from the review process is that *cooperative* query interactions (detection queries reinforcing tracking queries in self-attention) can be more impactful than the ostensible goal of improving detection per se. The paper's actual mechanism — query representation augmentation through shared label assignments — suggests that the boundary between "detection" and "tracking" queries in e2e-MOT may be a design artifact worth dissolving further. The finding that detection queries contribute >15% attention to tracking queries (often exceeding self-attention) points toward architectures where query roles are fluid rather than hard-coded by assignment strategy.

## Suggestions

1. **Resolve the query-count ambiguity immediately.** State explicitly: is "300 initial queries" equal to $N_T+N_D$ (number of sets) or $(N_T+N_D)\times N_S$ (total shadow queries)? If the former, explain how 900 shadow queries yield the same 173G FLOPs as MOTR's 300 queries. If the latter, discuss the capacity implications for crowded scenes and justify why the effective reduction to 100 sets does not bottleneck performance on datasets with >100 objects. This is the single most important clarification needed.

2. **Align the motivation with the evidence.** Either provide a Table-1-style mAP analysis for CO-MOT (showing detection improves under COLA) or revise the narrative to accurately reflect that COLA's primary benefit is tracking-query representation augmentation (via attention), not detection improvement. The paper's own analysis in Section 4.4 (lines 165–169) already pivots to this explanation — the introduction and abstract should match.

3. **Provide inference pseudocode.** A concise algorithm showing how the L-decoder outputs (tracking queries + detection queries) and shadow-set selection produce final tracklets would preempt confusion and improve reproducibility.

## Score and Decision

The paper makes a genuine and well-motivated contribution to e2e-MOT. The COLA and shadow set ideas are simple yet effective, and the empirical gains on DanceTrack and BDD100K are clear. The ablation study is thorough. However, the unresolved ambiguity in the query configuration (Issue 1 in Major) is not a minor presentation glitch — it undermines the interpretability of both the FLOPs efficiency claim and the MOT17 capacity discussion. The paper's core contributions are strong enough that this does not invalidate them, but it must be clarified before the paper can be properly evaluated. I recommend acceptance conditioned on this clarification being addressed in the final version.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>