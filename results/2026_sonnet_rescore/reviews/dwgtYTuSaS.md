## Summary

This paper introduces Continuous Online Action Detection (COAD), a task formulation in which an OAD model not only detects actions in real time from streaming video but also adapts on-the-fly from the stream in a single causal pass without data storage. To support the task, the authors curate Ego-OAD, a large-scale egocentric benchmark derived from Ego4D MQ annotations (87 classes, 22,991 instances, 263 hours). Three training strategies are proposed: state continuity (keeping the RNN hidden state across windows), orthogonal gradient projection (borrowed from Han et al., 2025), and non-uniform loss (from An et al., 2023). Experiments on Ego-OAD and EPIC-KITCHENS show improvements in out-of-stream generalization, with more mixed in-stream results.

---

## Strengths

- **Well-defined novel task formulation.** COAD clearly extends standard OAD with causal, single-pass, no-storage constraints tailored to wearable-device deployment. The formulation is grounded in formal constraints (Section 4.5) and distinguishes itself from both offline OAD and generic continual learning.

- **Large-scale, realistic benchmark.** Ego-OAD fills a real gap: egocentric OAD datasets with fine-grained temporal annotations are scarce. The dataset covers 87 classes, 263h of video, multi-label annotations with 36% overlapping instances, and diverse everyday activities beyond the kitchen-centric EPIC-KITCHENS.

- **Meaningful out-of-stream generalization gains.** Table 1 shows COAD achieves +5.9 mAP / +6.9 Top-5 Recall over the pretrained-only baseline in the out-of-stream egocentric setting, and +4.4 Top-5 Recall over naive in-stream training (w/o COAD). These are real improvements on held-out data.

- **Thorough hyperparameter trade-off analysis.** Figure 3 provides concrete evidence of the adaptation–generalization trade-off under varying learning rates and strides, including the notable result that even at stride 128 (one gradient step every ~68 seconds), the model continues to improve out-of-stream generalization.

- **Cross-dataset validation.** EPIC-KITCHENS experiments (Table 2) show COAD consistently achieves the best out-of-stream generalization across verb, noun, and action categories (notably Noun Top-5 Recall: 50.2 vs. 37.5 for pretrained-only), demonstrating generality beyond Ego-OAD.

- **Egocentric pretraining importance.** Table 4 shows consistent large gaps favoring egocentric pretraining over exocentric (e.g., +10.1 Top-5 Recall for TimeSformer), which grounds the benchmark's design choices empirically.

---

## Weaknesses

### Fatal

None.

### Major

- **Missing continual learning baselines.** The paper situates COAD within the continual/online learning paradigm but compares only against "Pretrained Only" and a naive "w/o COAD" baseline. Standard continual learning methods such as EWC, experience replay with a small buffer, or online gradient-based meta-learning are not compared. Without such comparisons, the results only establish that *some* adaptation beats *no* adaptation—not that the specific COAD protocol is the right approach. This is the most significant evidential gap in the experimental argument.

- **Personalization claim not supported by evaluation design.** The abstract and introduction repeatedly invoke "personalized adaptation to individual users." However, the in-stream set contains 1,177 videos from diverse users; the paper provides no per-user evaluation, no analysis of whether the model improves on a single user's own held-out data, and no decomposition of gains by user identity. The out-of-stream set is also multi-user. As designed, the experiment measures dataset-level domain shift, not user-specific personalization. The paper cannot claim to demonstrate personalization without this analysis.

- **COAD underperforms naive training on in-stream mAP (ego condition).** Table 1 shows COAD (36.8 mAP) < w/o COAD (39.0 mAP) in the in-stream ego pretraining setting. For a method whose stated goal includes "adaptation to the user's environment," underperforming naive training on the user's own data in mAP is a notable result. The paper describes this briefly as "balancing adaptation and generalization" but provides no analysis of whether the gap is robust across hyperparameters or whether it reflects a genuine method limitation. The EPIC-KITCHENS in-stream results also show both COAD and w/o COAD underperforming the pretrained-only model on several metrics (e.g., Action mAP: COAD 7.9 vs. Pretrained 9.6), attributed vaguely to "fine-grained actions limiting detection of recurring patterns" with no supporting analysis.

### Minor

- **State continuity contribution is negligible in ablation.** Table 3 shows: with state continuity off but orthogonal gradient + non-uniform loss on, performance is 25.9/36.7 mAP and 75.8/89.2 Recall, vs. full COAD at 26.0/36.8 and 76.0/89.3. The gap is 0.1/0.1 mAP and 0.2/0.1 Recall—essentially within noise. The paper's description that "state continuity provides a smaller but consistent gain" is accurate but understates how marginal this is, given it is listed as a distinct methodological contribution.

- **Abstract headline numbers cherry-pick the most favorable condition.** The "up to 20% in top-5 accuracy" comes specifically from the exo pretraining in-stream setting (COAD 80.0 vs. Pretrained Only 57.5 = +22.5), where the baseline is weakest. In the ego pretraining in-stream condition—the condition most aligned with the paper's motivation of egocentric adaptation—the corresponding gain is +16.0. The abstract is not false, but "up to" framing across conditions with substantially different baseline strengths is potentially misleading about typical performance.

- **Deliberate small pretraining set may artificially inflate COAD gains.** The pretraining set has only 186 videos vs. 1,177 for in-stream—a 6× asymmetry. The paper justifies this as "to better assess the impact of continuous learning," but it means that part of COAD's measured gain could stem simply from training on more data rather than from the specific continuous learning strategies. A sensitivity analysis over pretraining/in-stream ratios, or an IID baseline trained on equivalent in-stream data volume, would disambiguate data-quantity effects from algorithmic effects.

- **Orthogonal gradient applied only to the immediately preceding step.** Equation 3 projects the current gradient orthogonal to only g_{t-1}. For a temporally correlated stream, this may be insufficient to decorrelate over longer-range dependencies. The paper provides no theoretical or empirical justification for one-step orthogonalization being sufficient—not even an ablation over k-step history.

### Trivial

- **In-stream degradation over stream tail not analyzed.** Figure 4 shows out-of-stream performance improving monotonically over training—but whether in-stream performance degrades as the model specializes toward later-stream content is not shown. This matters for the stated use case of long-term deployment.

---

## Nice-to-Haves

- A per-user breakdown of in-stream and out-of-stream performance would directly demonstrate user personalization and is the most important experiment missing to support the paper's narrative.
- An ablation separating data-volume effects from algorithmic effects (e.g., IID model trained on in-stream volume, no COAD strategies) would clarify whether gains are algorithmic or data-driven.
- Extending the orthogonal gradient comparison to include k>1 step history, gradient clipping, or gradient normalization would add methodological depth given that this component drives the largest generalization gains.
- A brief annotator agreement analysis for Ego-OAD's union merging strategy would strengthen the dataset contribution's credibility.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **"Missing related works"**: The harsh critic implied missing related works in continual learning. Per review rules, related-work gaps cannot be verified without external sources and are excluded.

- **IID upper bound conflation**: The harsh critic argued the Figure 4 IID upper bound "conflates improvement with achievability." This is speculative framing—the figure is labeled as an oracle/upper bound and presented as such, which is standard practice.

- **Annotation consistency concern (as a fatal issue)**: The harsh critic raised concerns about the union annotation strategy producing inconsistent labels. This is a valid minor concern, but was presented more severely than warranted—the paper explicitly addresses this by grouping semantically similar descriptions into unified classes (Section 3), making it a partially addressed issue. Retained as a nice-to-have.

- **Strength Finder's "important problem" and "interesting question" framing**: Generic claims about the problem's importance have been dropped. Only concrete, evidence-backed strengths retained.

---

## Novel Insights

The paper's most analytically interesting (and underemphasized) finding is that COAD's benefit is asymmetric: the method helps *out-of-stream generalization* more than *in-stream adaptation*—and on in-stream mAP, COAD actually underperforms naive training in the strongest baseline condition (36.8 vs. 39.0 with ego pretraining). This suggests that the orthogonal gradient projection and non-uniform loss act more as regularizers preserving generalization than as accelerators of domain adaptation, and that the "adaptation" framing in the paper is somewhat inverted: COAD's main contribution is *preventing forgetting* during stream training, not *personalizing to the stream*. This reframing, if developed explicitly, would make the paper's contribution clearer and more defensible.

---

## Suggestions

1. **Add at least one continual learning baseline** (e.g., EWC, or experience replay with a buffer of ~100 samples). Even a simple replay baseline would reveal whether COAD's streaming-specific design is better than the most natural CL alternative.
2. **Add per-user evaluation** on a subset of Ego4D where the same user appears in multiple sessions. This is the most direct way to demonstrate personalization.
3. **Add an IID-on-equivalent-data control**: train a standard IID model on the same amount of data as the in-stream set (no COAD strategies) to separate data-volume effects from algorithmic gains.
4. **Reframe the abstract** around out-of-stream generalization (which COAD clearly and consistently improves) rather than in-stream adaptation (where results are mixed), to match what the experiments actually demonstrate.
5. **Expand the discussion of in-stream mAP trade-off**, including a hyperparameter sensitivity check, to give readers a clearer picture of when COAD's regularization hurts in-domain accuracy.

---

## Score and Decision

**Originality**: The task formulation is novel as applied to OAD, but all technical components are borrowed from prior work. The Ego-OAD dataset is an original contribution. Moderate originality. (3/5)

**Importance**: Egocentric on-device OAD is a well-motivated and practically relevant research direction. The benchmark fills a real gap. (4/5)

**Claims supported**: Out-of-stream generalization claims are well-supported. In-stream adaptation and personalization claims are weaker or unsupported by the evaluation design. (3/5)

**Soundness**: Core experimental setup is sound. Missing CL baselines and the data-volume confound reduce confidence in method-specific conclusions. (3/5)

**Clarity**: Writing is generally clear. The abstract framing is somewhat misleading relative to the actual result pattern. (3/5)

**Community value**: Ego-OAD is a real and useful benchmark. COAD as a task formulation is a clean contribution. Method contribution is more marginal. (3/5)

The paper makes genuine contributions—the Ego-OAD benchmark and the COAD task formulation are real additions to the field. However, the method novelty is limited (all components from prior work), the personalization narrative is not demonstrated by the evaluation, and the missing continual learning baselines mean the community cannot assess whether COAD's specific streaming design is better than simpler alternatives. The EPIC-KITCHENS results show COAD primarily preventing catastrophic forgetting rather than improving on the pretrained baseline. Taken together, the paper is a borderline case that leans toward rejection in its current form, primarily due to the gap between its strongest claims (personalization, adaptation) and what the experiments actually demonstrate.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>

<subscores>
<originality>3</originality>
<importance>4</importance>
<claims_supported>3</claims_supported>
<soundness>3</soundness>
<clarity>3</clarity>
<community_value>3</community_value>
</subscores>