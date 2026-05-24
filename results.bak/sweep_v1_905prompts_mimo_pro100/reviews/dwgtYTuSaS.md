Now I have all the information I need. Let me write the final review.

## Summary

This paper introduces Continuous Online Action Detection (COAD), a task formulation enabling models to detect actions in real-time while continuously learning from streaming egocentric video without data storage or replay. The authors curate Ego-OAD, a large-scale egocentric OAD benchmark from Ego4D, and adapt three continuous learning strategies (state continuity, orthogonal gradient projection, non-uniform loss) to the OAD setting. Experiments on Ego-OAD and EPIC-KITCHENS demonstrate that COAD improves out-of-stream generalization over both a pretrained-only baseline and a naive continuous training baseline.

## Strengths

- **Well-defined novel task formulation**: Section 4 clearly formalizes COAD with precise mathematical grounding (Eqs. 1–6), articulating the distinction from standard offline OAD training (shuffled windows, reset hidden states, multiple epochs). The multi-stage framework (backbone pretraining → offline OAD → COAD → inference) is well-motivated and reproducible.

- **Useful benchmark dataset**: Ego-OAD comprises 87 action classes, 22,991 labeled instances across 263h of egocentric video from Ego4D. This fills a genuine gap, as existing egocentric OAD datasets (e.g., EPIC-KITCHENS) are limited to kitchen environments. The benchmark uses multi-label temporal annotations with 36% overlap, providing a realistic testbed.

- **Consistent out-of-stream generalization gains**: In Table 1, COAD achieves +4.4 Top-5 Recall improvement over the fair w/o COAD baseline on out-of-stream data (ego pretraining), and +6.9 over Pretrained Only. Table 3's ablation shows non-uniform loss contributes +8.3 Top-5 Recall and orthogonal gradient contributes +4.5, demonstrating that the specific COAD strategies meaningfully improve generalization beyond naive continuous training.

- **Thorough ablation analysis**: Table 3 systematically removes each COAD component, clearly isolating individual contributions. Figure 3's stride/learning-rate trade-off analysis is informative, and the finding that the model still improves at stride=128 (supervision only ~every 68 seconds) is genuinely interesting. Figure 4's training curves demonstrate steady improvement approaching the IID upper bound.

## Weaknesses

### Fatal
None.

### Major

- **Inflated headline claims from conflating baselines**: The abstract claims "improves adaptation to the user's environment by up to 20% in top-5 accuracy, and improves generalization to new scenarios by up to 7%." These numbers come from comparing COAD to Pretrained Only (a model that has never seen any in-stream data). The actual improvement from the proposed COAD *strategies* is obtained by comparing COAD to w/o COAD, yielding far more modest gains: out-of-stream Top-5 Recall +4.4 (ego), in-stream Top-5 Recall +2.6 (ego), and in-stream mAP actually *drops* by 2.2 points (Table 1, ego setting). The ~20% figure is largely attributable to doing continuous training at all, not to the specific strategies the paper proposes. This conflation significantly overrepresents the paper's methodological contribution.

- **COAD strategies trade in-stream mAP for out-of-stream generalization — contradicting the "adaptation" narrative**: Table 1 shows COAD achieves 36.8 in-stream mAP versus 39.0 for w/o COAD (ego pretraining), a 2.2-point drop. While in-stream Top-5 Recall does improve (+2.6), the net effect is that COAD's primary benefit is *regularization against overfitting* during continuous training, not enhanced adaptation as the abstract and introduction repeatedly frame it. The paper should be forthright about this trade-off rather than characterizing COAD as improving "adaptation to the user's environment."

- **Inconsistent results on EPIC-KITCHENS**: Table 2 shows COAD achieves 7.9 in-stream Action mAP versus 9.6 for Pretrained Only — a clear regression. COAD ties Pretrained Only on in-stream Verb mAP (29.0) and barely improves Noun mAP (3.9 vs 3.8). The paper acknowledges the struggle ("both COAD and the w/o COAD baseline struggle to adapt effectively") but attributes it to "the fine-grained nature of the actions and annotations" without explaining *why* fine-grained annotations specifically undermine COAD. This inconsistency weakens the claim that COAD's principles generalize beyond Ego-OAD.

### Minor

- **No variance or confidence intervals reported**: Given that margins between COAD and w/o COAD are sometimes 1–2 points in mAP and 2–4 points in Top-5 Recall, readers cannot assess whether the differences are statistically reliable. This is standard practice concern for results at these margins.

- **State continuity component has negligible contribution**: Table 3 shows that removing state continuity (row 4 vs row 1) changes out-stream mAP by only +0.1 and out-stream Top-5 Recall by only −0.2. In some comparisons, state continuity even slightly hurts performance (e.g., row 3 vs row 5: −0.2 mAP out-stream). The paper claims "state continuity provides a smaller but consistent gain" (Section 5.4), but the data shows it is essentially a no-op. This raises questions about whether this component is pulling its weight.

- **Method novelty is incremental**: The three COAD components (state continuity, orthogonal gradient projection, non-uniform loss) are explicitly adapted from Carreira et al. (2024) and Han et al. (2025). The paper acknowledges this but the contribution is applying existing continuous learning techniques to OAD, not inventing the techniques themselves. The orthogonal gradient projection uses only the immediately preceding gradient (one-step decorrelation), which limits its theoretical motivation for longer-range correlations.

- **Table 4 (Feature Extractors) feels tangential**: The comparison of TSN vs. TimeSformer is informative but separate from the COAD analysis — all COAD experiments use TimeSformer, so this table reads as an additional contribution bolted on rather than integrated.

### Trivial
None.

## Nice-to-Haves

- Report computational costs (FLOPs per update, memory footprint) to ground the wearable-device motivation with concrete resource constraints.
- Characterize more precisely when COAD helps most (e.g., for rare classes, long actions, specific environment types) — the stride analysis in Fig. 3 hints at this but deeper analysis would strengthen the paper.
- Provide a clearer explanation of why EPIC-KITCHENS is resistant to COAD's strategies.

## Removed Points

These points are flagged to be removed, treat them with caution.

- **"Dataset is not truly new"**: The harsh critic notes Ego-OAD is a re-curation of Ego4D rather than a newly collected dataset. However, the paper explicitly says it "curates" from Ego4D and does not claim new data collection. This is a common and legitimate contribution pattern.

- **"Wearable device motivation is untested"**: The critic notes that the paper motivates on-device training for wearable devices but doesn't evaluate on wearable devices or report latency. While true, it is common in research papers to motivate with an application domain without fully deploying there. This is scope creep.

- **"Appendix A makes it impossible to evaluate grouping quality"**: The harsh critic notes that manual action class groupings are deferred to Appendix A. Per our rules, we do not penalize for appendix content that was stripped by the parser.

## Novel Insights

The paper's most genuinely novel observation is that continuous OAD training can work with extremely sparse supervision — the stride-128 result (Fig. 3) showing that a model receiving a ground-truth label only every ~68 seconds still improves on continuous streams is a finding that goes beyond the paper's own stated claims and has practical implications for resource-constrained wearable devices. Additionally, the systematic demonstration that continuous learning strategies adapted from video understanding transfer to the OAD setting, with the specific finding that non-uniform loss is the most impactful component while state continuity is nearly inert, provides useful guidance for practitioners in this space.

## Suggestions

1. **Reframe the abstract honestly**: Replace "improves adaptation by up to 20%" with a claim that directly compares COAD to w/o COAD, e.g., "COAD strategies improve out-of-stream generalization by up to 4.4 Top-5 Recall over naive continuous training." This is still a meaningful result and does not conflate continuous training benefits with COAD-specific benefits.
2. **Rename "adaptation" framing**: The paper's core finding is that COAD provides *regularization against overfitting* in continuous training, yielding generalization gains at some cost to in-stream fit. Reframing around this finding would be more honest and still publishable.
3. **Add error bars**: Run at least 3 seeds for the main results in Tables 1–2 to establish whether the 1–2 mAP differences are reliable.
4. **Discuss EPIC-KITCHENS failures more concretely**: Instead of hand-waving about "fine-grained annotations," analyze specific failure cases — e.g., is COAD confused by the much larger label space, the shorter action durations, or the domain gap from kitchen-only videos?

## Reporting: Calibration Anchors

| Anchor | Score | Round | Comparison |
|--------|-------|-------|------------|
| Efficient Object-Centric Learning for Videos | 3.00 | 1 | Weaker — COAD has a clearer problem and better experiments |
| Projected Subnetworks Scale Adaptation | 2.00 | 1 | Much weaker — COAD has far better evaluation and clearer contribution |
| Real-time CV on low-end boards | 3.25 | 1 | Weaker — COAD has better experimental design and clearer task |
| LVLM-CL | 2.50 | 1 | Much weaker — COAD has better experiments and clearer formulation |
| PrAViC (Real-Time Video Classification) | 4.25 | 1 | Weaker — PrAViC had overstated theory and unclear presentation; COAD is cleaner |
| EVGAP (Ego-Exo Alignment) | 4.00 | 1 | Weaker — COAD has better defined task and more thorough evaluation |
| Online Continual Graph Learning | 5.00 | 2 | Similar — both define new task formulations with adapted methods |
| CLDyB (Dynamic CL Benchmarking) | 5.67 | 2 | Similar — both contribute benchmarks; COAD has inflated claims but more experiments |
| Anomalies are Streaming (CL-WSVAD) | 5.71 | 2 | Similar — both adapt existing CL methods to new domains with mixed results |
| StreamChat (Streaming Video Understanding) | 5.80 | 2 | Similar — both contribute benchmarks; COAD is less engineering-heavy but has inflated claims |
| EgoVideo (Hand-Object Dynamics) | 6.00 | 2 | Slightly stronger — EgoVideo has a more novel pipeline and stronger SOTA results |
| Test-Time Adaptation Missing Modalities (MiDl) | 6.00 | 2 | Slightly stronger — MiDl has a cleaner method contribution and consistent results |
| MMEgo (Egocentric Multimodal LLMs) | 6.00 | 2 | Slightly stronger — MMEgo has larger-scale contributions |
| Multi-granularity Correspondence | 8.00 | 1 | Much stronger — this is a top-tier paper |

**Round-1 bracket:** Between 3.0 and 8.0, with the paper plausibly in the 4.5–6.5 range based on topical similarity.

**Round-2 narrowing:** The anchors between 5.0–6.0 (CLDyB, StreamChat, EgoVideo, MiDl) provide the tightest comparison. COAD is comparable to CLDyB and StreamChat (both ~5.7) but weakened by inflated claims and inconsistent EPIC-KITCHENS results. It falls slightly below EgoVideo and MiDl (both 6.0) which have cleaner method contributions and stronger experimental results. The inflated headline claims, while not fatal (tables are transparent), prevent the paper from being scored alongside the 6.0 anchors.

**Final score: 5.0** — A borderline paper with genuine task/dataset contributions, incremental but solid method adaptation, and thorough ablations, but significantly weakened by overclaimed framing and inconsistent cross-dataset results.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>