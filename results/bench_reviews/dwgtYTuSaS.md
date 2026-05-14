Now I have all the information I need. Let me construct the final review.

## Summary

This paper introduces Continuous Online Action Detection (COAD), a task formulation where OAD models learn from streaming video in a single pass without data storage, targeting egocentric wearable device deployment. The authors curate Ego-OAD, a large-scale benchmark (87 classes, 22,991 instances, 263h) derived from Ego4D Moment Queries, and propose training strategies combining single-pass streaming, state continuity, orthogonal gradient projection, and non-uniform loss. On Ego-OAD, COAD shows improvements over a pretrained-only baseline, but technical novelty is limited as the core components are adapted from prior streaming-video learning work without identifying challenges unique to OAD or proposing new algorithms to address them.

## Strengths

1. **Ego-OAD benchmark fills a gap in egocentric OAD evaluation.** The paper curates a large-scale benchmark (263h, 87 classes, 22,991 instances) from Ego4D MQ, offering diverse everyday scenarios beyond kitchen-only datasets like EPIC-KITCHENS. The label aggregation (Appendix A) and multi-label annotations with 36% overlap provide a more realistic testbed for OAD than existing options. This dataset is a genuine asset to the community.

2. **Clear experimental setup for studying adaptation vs. generalization.** The three-way split (pretraining / in-stream / out-of-stream) borrowed from Carreira et al. (2024a) provides a clean framework to evaluate whether online adaptation improves deployment performance, and the ablation study (Table 3) isolates the contribution of each component (orthogonal gradient adds +4.5% out-of-stream Top-5 recall; non-uniform loss adds +4.2 mAP).

3. **Quantitative gains on Ego-OAD are non-trivial.** On the out-of-stream split, COAD achieves a 6.9% improvement in Top-5 Recall over the Pretrained Only baseline (ego pretraining), versus 2.5% from w/o COAD — a meaningful gap that demonstrates the method's components help generalization beyond merely seeing more data.

4. **Temporal coherence improvements are visually convincing.** Qualitative results (Figures 5, 6) show COAD produces more temporally stable predictions than the baseline, with fewer spurious class switches — a practically important quality for real-time egocentric AI.

## Weaknesses

### Fatal
None.

### Major

1. **Technical novelty is limited — the paper adapts existing streaming-learning techniques to OAD without introducing new algorithmic insights for the OAD setting.** The paper explicitly builds on Carreira et al. (2024a) (single-pass streaming training, state continuity) and Han et al. (2025) (orthogonal gradient projection), and the non-uniform loss comes from An et al. (2023). The paper acknowledges these as the sources, but the result is a straightforward application of existing ideas to OAD. No analysis is provided of what challenges are *unique* to OAD (vs. general video streaming) or what new technical machinery was needed. The paper claims "OAD-specific training strategies" (abstract), but the strategies themselves are not OAD-specific — they are the same techniques used for general streaming video. A paper can be novel by identifying new challenges in a domain and developing solutions, but here the challenges are not identified and the method is directly ported.

2. **The evaluation confounds "more labeled data" with "online adaptation" in the central comparison.** The Pretrained Only baseline is trained on 186 videos, while COAD additionally processes 1,177 in-stream videos with labels. The comparison between COAD and w/o COAD (both see the same data) does control for data quantity, but the paper's headline improvements (e.g., "up to 20% top-5 accuracy") compare COAD to Pretrained Only — where the gain confounds more training data with the streaming method. The IID training baseline (trained offline on combined data) appears only in Figure 4 and not in Tables 1-2, making it harder to assess how much of COAD's gain over Pretrained Only is due to adaptation vs. simply having access to more in-distribution labeled data. This matters because the w/o COAD baseline *also* sees the same 1,177 videos but often achieves comparable or better in-stream mAP on Ego-OAD (e.g., 39.0 vs. 36.8), raising questions about what exactly the orthogonal gradient and non-uniform loss components contribute when the model has access to the same data offline.

3. **No runtime, memory, or throughput analysis despite motivating with resource-constrained wearable devices.** The paper argues for RNNs over Transformers due to "high computational and memory costs" and frames COAD as suitable for "real-time deployment on resource-constrained devices" (Section 2), yet provides zero measurements of FLOPs, latency, GPU memory, or on-device throughput. This makes the deployment claims untestable and weakens the paper's framing.

### Minor

1. **EPIC-KITCHENS results show COAD underperforms the pretrained-only baseline on several out-of-stream metrics.** While the harsh critic's claim that "COAD loses on 8/12 in-stream metrics" is factually incorrect (COAD wins on all 12 metric/domain combinations against w/o COAD), examining Table 2 more carefully reveals that on out-of-stream evaluation, Pretrained Only ties COAD on Action Top-5 (21.9 both) and has competitive Verb mAP (11.4 vs 11.8). The paper's explanation — "fine-grained nature of the actions" — is superficial and not backed by analysis. Since EPIC-KITCHENS is exactly the kind of personalized, user-specific setting where continuous adaptation should shine, the modest results and lack of deeper investigation weaken the generality claim.

2. **Ego-OAD benchmark validity concerns are not fully addressed.** Background frames derived from unannotated intervals in Ego4D MQ may contain actions that were simply not queried, inflating false positive rates. The paper acknowledges the union-merging strategy but does not report inter-annotator agreement on the aggregated labels, nor analyze whether the 36% multi-label overlap reflects genuine concurrent actions or annotation disagreement. These are standard dataset quality checks that would strengthen the contribution.

3. **The orthogonal gradient projection only decorrelates from the immediately preceding gradient.** This provides limited protection against longer-term gradient drift. The paper does not analyze whether representations change systematically over in-stream processing, nor measure forward/backward transfer (standard continual learning evaluation). The claim of "catastrophic forgetting" mitigation is asserted but not tested.

4. **The ablation study (Table 3) shows COAD has lower in-stream mAP than w/o COAD (36.8 vs. 39.0), but this trade-off is not investigated.** The paper notes this is a "trade-off" but does not analyze why the orthogonal gradient and non-uniform loss specifically hurt in-stream performance, leaving a significant open question about the method's behavior.

### Trivial
None.

## Nice-to-Haves
- Including the IID training baseline in Tables 1-2 rather than only in Figure 4 would provide a proper upper bound for the main comparisons.
- Per-class performance breakdown would help assess whether gains come from improving frequent or rare classes.
- A simple fine-tuning baseline (same architecture, shuffled mini-batches, multiple epochs on in-stream data) would help separate the benefit of "more data" from the benefit of "single-pass streaming constraints."

## Removed Points
The following points from the harsh critic are removed because they are factually incorrect:

- **"On 8 out of 12 in-stream metrics, the w/o COAD baseline outperforms COAD on EPIC-KITCHENS."** — Factually wrong. Comparing Table 2 numbers: COAD *outperforms* w/o COAD on all 12 metric/domain combinations on EPIC-KITCHENS. COAD's generalization performance claim is supported by the data.
- **"COAD ties or slightly edges the baseline on some metrics while losing on others"** on EPIC-KITCHENS out-of-stream. — Wrong. COAD wins on 5 out of 6 out-of-stream metrics and ties on the 6th.
- **"The authors claim COAD 'consistently achieves the best generalization performance' but this is demonstrably false."** — Checked against Table 2, COAD is the best or tied for best on all metrics.
- **"The paper claims COAD provides inconsistent or marginal improvements"** on EPIC-KITCHENS. — The numbers consistently favor COAD over w/o COAD on every metric.
- Criticisms about formatting, missing appendix content, and missing references — removed per instructions.

## Novel Insights

Beyond the paper's own contributions, the most interesting observation is the asymmetry between Ego-OAD and EPIC-KITCHENS: COAD provides clear gains on the diverse Ego-OAD benchmark but marginal improvements on EPIC-KITCHENS. This suggests that the value of online streaming adaptation depends heavily on the diversity and predictability of the action space — fine-grained, domain-specific actions (cooking) may not benefit as much from single-pass adaptation as broader, more varied activities (Ego-OAD). This finding, if properly investigated, could inform when streaming adaptation is worth the computational overhead in egocentric settings.

## Suggestions

1. Include the IID offline-trained baseline in Tables 1-2 to allow direct comparison of the full chain — this would clarify whether COAD's gains over Pretrained Only come from seeing more data or from the streaming method itself.
2. Provide runtime and memory measurements (latency, FLOPs, GPU memory) to substantiate the real-time/wearable deployment framing, which is currently asserted without evidence.
3. Add per-class performance analysis and investigate why EPIC-KITCHENS shows limited gains — this would strengthen the paper's understanding of when COAD is beneficial.
4. Report inter-annotator agreement and quantify the "true negative" validity of background frames in Ego-OAD to establish dataset quality.

## Score and Decision

**Anchors used for calibration:**

| Path | Avg Score | Comparison |
|------|-----------|------------|
| `738HjJEbml.md` (QueryStream) | 5.00 | Similar level — both adapt existing ideas to a new streaming context. QueryStream is a training-free plug-in; COAD has a new dataset but less technical novelty in its method. |
| `gVbPWbA97s.md` (StreamingVLM) | 6.00 | Stronger paper — has a genuine technical contribution (KV cache design + training-inference alignment) plus a benchmark. COAD's method novelty is weaker by comparison. |
| `gmpnSSiJt7.md` (TV-Online) | 4.50 | Similar — both contribute a new benchmark and adapt existing techniques. TV-Online has a more involved method (progressive training, RL); COAD's method is simpler but cleaner. |
| `1RrwTXSU4c.md` (Online Error Detection) | 3.50 | Weaker — narrower task, less rigorous evaluation. COAD is stronger in scope and experimental design. |
| `DTQIjngDta.md` (High-scoring anchor) | 8.00 | Significantly stronger — fundamental algorithmic contribution (permutation-equivariant architecture). COAD does not approach this level of novelty. |
| `pPKqLyWiNr.md` (Mid-range anchor) | 5.00 | Similar — both repurpose existing ideas for a new task setting. |
| `d7YpJuV64J.md` (Low-scoring anchor) | 2.67 | Weaker paper — unclear contribution. COAD is clearly better motivated and executed. |

Positioned relative to these anchors, this paper's contribution is most comparable to the 4.5–5.0 band. The dataset contribution is real and valuable, and the evaluation framework is sound. However, the method's limited novelty — applying existing streaming-learning techniques to OAD without new algorithmic insight for the OAD setting — prevents it from reaching the bar of a top conference paper. The over-claimed novelty in title and abstract further detracts.

MY FINAL SCORE: <pineapple>4.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>