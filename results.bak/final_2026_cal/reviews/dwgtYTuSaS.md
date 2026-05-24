Now I have solid calibration data. Let me set my round-1 bracket and finalize.

**Round 1 bracket**: (4.0, 6.0) — The paper is clearly stronger than the 2-3 range papers (which are withdrawn/rejected with fatal flaws) and weaker than the 6.5+ papers (which have more comprehensive evaluation). I'm comparing it most closely to RIVER (5.0, Accept) and TV-Online (4.5, Reject), both of which are benchmark+method papers for online/streaming video tasks.

Let me narrow the bracket to (4.5, 5.5) and finalize the review.

---

## Summary

This paper introduces Continuous Online Action Detection (COAD), a novel task formulation where OAD models continuously learn and adapt from streaming video in a single pass without storing data or requiring multiple training passes. The authors curate Ego-OAD, a large-scale egocentric OAD benchmark (263h, 87 classes, 22,991 instances) from Ego4D Moment Queries, and propose training strategies including state continuity, orthogonal gradient projection, and non-uniform loss weighting. Results on Ego-OAD show that training on streaming video yields large improvements (up to +22.5 Top-5 Recall) over a weakly-supervised pretrained baseline, and the COAD-specific components add further gains on out-of-stream generalization.

## Strengths

1. **New task formulation with practical relevance.** The COAD problem (Section 4.5) formalizes a gap between offline OAD training and real-world deployment: models that must adapt from a single-pass stream without data storage. This is well-motivated for egocentric wearable devices and is distinguished clearly from standard offline OAD (Section 4.3).

2. **Large-scale egocentric OAD benchmark.** Ego-OAD (Section 3) provides 263 hours of video, 87 classes, 22,991 instances across diverse environments (not just kitchens). Multi-label annotations with 36% instance overlap reflect real-world annotation ambiguity, and the scale substantially exceeds existing egocentric OAD resources.

3. **Clean ablation study isolating component contributions.** Table 3 systematically ablate state continuity, orthogonal gradient, and non-uniform loss. The paper shows that non-uniform loss contributes +4.2 mAP / +8.3 Top-5 Recall, orthogonal gradients add +4.5 Top-5 Recall, and state continuity provides smaller consistent gains. This allows readers to attribute specific benefits to each design choice.

4. **Informative analysis of the adaptation-generalization trade-off.** Figure 3 varies learning rate and window stride to show how hyperparameters shift the balance between in-stream (adaptation) and out-of-stream (generalization) performance, providing practical guidance for deployment.

5. **Performance trajectory approaching IID upper bound.** Figure 4 demonstrates that COAD steadily narrows the gap to an offline IID-trained model as more streaming data is processed, while ablated variants plateau lower. This is the strongest evidence that the COAD components matter beyond simple continuous training.

## Weaknesses

### Major

1. **No benchmarking of existing OAD methods on Ego-OAD in any setting.** The paper compares COAD only against its own baselines (Pretrained Only, w/o COAD). While the COAD task is new and existing OAD methods cannot be directly applied in the streaming single-pass setting, there is no evaluation of even the most basic offline OAD methods (e.g., LSTR, TeSTra, MiniROD, GateHub) trained on the combined pretrain+in-stream data as a reference point. An IID upper bound appears only in Figure 4 but is never reported as a concrete number in Tables 1-2. Without this, it is difficult to assess whether COAD's single-pass streaming performance is meaningfully close to what an offline model can achieve, or whether the dataset itself presents genuinely new challenges for OAD methods. For a paper that contributes both a dataset and a method, this is a significant gap.

2. **Framing conflates data-scale gains with method-specific gains.** The abstract claims "continuous learning from streaming videos improves adaptation … by up to 20% in top-5 accuracy." In Table 1 (Ego pretrained, in-stream), w/o COAD already achieves 86.7 Top-5 Recall (a 13.4-point gain over Pretrained Only's 73.3), while COAD adds 2.6 points over that to 89.3. The 20% figure reflects the combined effect of training on 10x more data *plus* the COAD components. The narrative in the abstract and introduction does not distinguish these effects, creating the impression that the gains are attributable to the method rather than to the natural consequence of training on far more data. The text in Section 5.3 acknowledges w/o COAD's competitive in-stream performance but does not clearly separate the two effects in the headline claims.

3. **EPIC-KITCHENS results are inconsistent and inadequately analyzed.** On EPIC-KITCHENS (Table 2), COAD often fails to outperform even Pretrained Only on in-stream metrics (Verb mAP: 29.0 vs. 29.0; Action mAP: 9.6 vs. 7.9). The w/o COAD baseline actually *degrades* performance compared to Pretrained Only on almost all in-stream metrics (e.g., Verb mAP drops from 29.0 to 16.6). The paper attributes this to fine-grained actions "limit[ing] the model's ability to detect and exploit recurring patterns," but offers no analysis — e.g., a breakdown by action frequency, video length distributions, or a comparison of backbone features (EgoVLP vs. TSN fine-tuned on EPIC) to support this claim. This weakens the generality claims made in the conclusion.

### Minor

4. **Split construction is underspecified.** The paper states that the three splits (186 pretraining, 1,177 in-stream, 519 out-of-stream) "correspond to the original Ego4D MQ validation split" but does not clarify whether splits are by video, by user, by environment, or random. This matters substantially for interpreting generalization: if the out-of-stream set involves novel users, the 6.9% Top-5 Recall gain is more meaningful than if it samples from similar environments. No domain-shift statistics (action distribution, visual similarity) between splits are provided.

5. **No annotation quality metrics.** The dataset curation merges multiple annotator passes and groups similar descriptions into 87 unified classes, but the paper reports no inter-annotator agreement or label confusion analysis. Given that 36% of instances overlap and descriptions can differ subtly (e.g., `pour_milk` vs. `pour_milk_into_the_bowl`), the paper does not quantify how well the grouping resolves residual ambiguity.

6. **No analysis of computational cost.** COAD involves forward + backward + gradient projection per window. For a paper targeting resource-constrained wearable devices, the absence of wall-clock time, FLOPs, or throughput measurements is a noticeable omission (though the method itself is lightweight by design).

### Trivial

7. Minor typo: "Countinuous" → "Continuous" in the first bullet of contributions (Section 1).

## Nice-to-Haves

- Benchmarking 2-3 existing OAD methods (e.g., MiniROD, LSTR) trained offline on the combined pretrain+in-stream data would substantially strengthen the dataset contribution and provide a concrete reference for COAD's value.
- Clarifying the split construction (by user? by environment?) and reporting domain-shift statistics (action distribution, visual feature similarity) between splits would make the generalization claims more interpretable.
- An analysis of why EPIC-KITCHENS fails — e.g., ablating backbone features, video length distributions, or action granularity — would help readers understand the method's limitations.
- A brief comparison of orthogonal gradient (using only the immediate past gradient) to a larger buffer or to Elastic Weight Consolidation would justify the design choice.

## Removed Points
- *Criticism that the paper provides "zero comparisons to any existing OAD model" as a fatal structural flaw* — REMOVED because the COAD task is a new formulation where existing OAD methods (designed for offline training with multiple epochs and shuffled data) cannot be directly applied without substantial modification. The paper's baselines (Pretrained Only, w/o COAD, IID upper bound) are the natural comparisons for this new task. However, the absence of offline benchmarking to establish the dataset as a useful OAD benchmark remains a major weakness. 
- *Criticism that orthogonal gradient uses only previous gradient without comparing to larger buffers* — WEAKENED to Nice-to-Have, as the paper cites Han et al. (2025) for the technique and provides ablation evidence showing its benefit.
- *"Missing related works"* — REMOVED per instructions.
- *Several generic strengths from the Strength Finder* — REMOVED (e.g., "systematic ablation" is retained as a real strength; generic phrasings about the problem being important are removed).

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. **Benchmark 2-3 existing OAD methods** on Ego-OAD in the standard offline setting (trained on combined pretrain+in-stream data, evaluated on out-of-stream). Report these as reference points alongside the COAD results, even though they are not directly comparable in the streaming setting. This would establish the dataset's utility and show the gap COAD aims to close.

2. **Clarify split construction.** State explicitly whether the pretrain/in-stream/out-of-stream splits partition by video, by user, or by environment. If by video (random), note that the "generalization" measured is to held-out videos rather than to novel users or scenarios.

3. **Recalibrate headline claims.** In the abstract and introduction, separate the effect of training on streaming data ("up to 20% over a weakly-supervised pretrained model") from the effect of the COAD-specific components ("an additional +2.6% top-5 recall on in-stream and +4.4% mAP on out-of-stream over simple continuous training"). The full ablation in Table 3 supports honest attribution.

4. **Analyze the EPIC-KITCHENS failure case.** Report a breakdown by action frequency, compare backbone features (EgoVLP vs. TSN-finetuned), and discuss whether the issue stems from action granularity, video length, or backbone differences. Acknowledge that the method's gains concentrate on datasets with coarser or more repetitive actions.

## Score and Decision

**Round 1 bracket**: (4.0, 6.0) — The paper is clearly stronger than withdrawn/rejected papers in the 2-3 range and weaker than benchmark+method papers with comprehensive evaluations at 6.5+.

**Round 2 anchors used**:
- RIVER Bench (xmtvHH62Ic, avg 5.0, Accept): Similar structure (new benchmark + method for streaming video). Our paper has a more novel task formulation and cleaner ablation, but RIVER has broader evaluation coverage. Comparable quality.
- TV-Online (gmpnSSiJt7, avg 4.5, Reject): Also benchmark + progressive training framework. Our paper has clearer task definition and better-motivated method components. Slightly stronger.
- EgoNight (DKD4QbOKBN, avg 5.0, Accept): Egocentric benchmark (VQA). Clean, focused contribution. Our paper adds a new task dimension beyond just the dataset, making it more ambitious but also less polished.
- StreamingVLM (gVbPWbA97s, avg 6.0, Accept): Strong execution with comprehensive evaluation on multiple benchmarks. Our paper has less comprehensive evaluation coverage.

**Final calibration**: The paper sits between the RIVER/TV-Online level and the StreamingVLM level. The main contributions (COAD task formulation + Ego-OAD dataset + method with clear ablations) are solid, but the evaluation gaps (no offline OAD benchmarking, underspecified splits, EPIC-KITCHENS issues) prevent it from reaching the 6.0 level. Compared to RIVER (5.0, Accept), the paper has a more novel task but weaker evaluation coverage. I score it 5.0.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Accept</decision>