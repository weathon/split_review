Now let me do calibration search to assess the paper's quality relative to anchor papers.Round 1 bracket: **4.0–6.5**. Let me now do round 2 narrowing within this bracket.I have enough information to write the final review. Let me compose it now.

---

## Summary

This paper proposes **Continuous Online Action Detection (COAD)**, a task formulation extending standard Online Action Detection (OAD) to allow models to adapt on-the-fly from streaming egocentric video using single-pass, causal training without data replay. The authors curate **Ego-OAD**, a large-scale benchmark derived from Ego4D Moment Queries featuring 263h of video, 87 fine-grained action classes, and 22,991 temporal instances, split into pretraining/in-stream/out-of-stream partitions. They adapt three training strategies—state continuity, orthogonal gradient projection, and non-uniform loss weighting—to the RNN-based OAD setting, and evaluate on both Ego-OAD and EPIC-KITCHENS, showing measurable gains in out-of-stream generalization.

---

## Strengths

- **Large-scale egocentric OAD dataset (Ego-OAD):** The dataset fills a genuine gap — public egocentric OAD benchmarks with fine-grained temporal annotations are scarce. With 263h of video, 87 classes, and multi-label overlap annotations (36% of instances overlap, average overlap 9.90s), it provides a realistic and diverse testbed. The value of this benchmark is independently confirmed by the backbone comparison in Table 4, which demonstrates that egocentric pretraining (EgoVLP on TimeSformer) yields a +10.1 Top-5 Recall gain over exocentric pretraining on the pretrained-only baseline.

- **Empirically validated out-of-stream generalization:** COAD consistently outperforms both the Pretrained Only and w/o COAD baselines on out-of-stream evaluation. In the ego pretraining setting (Table 1), COAD achieves +5.9 mAP and +6.9 Top-5 Recall over the pretrained-only baseline, compared to +5.4 mAP / +2.5 recall for naive in-stream training. Cross-dataset validation on EPIC-KITCHENS (Table 2) reinforces the finding: COAD achieves out-of-stream Noun Top-5 Recall of 50.2 vs. 37.5 for pretrained-only.

- **Principled ablation with hyperparameter trade-off analysis:** Figure 3 maps the in-stream vs. out-of-stream performance trade-off across learning rate and stride configurations. Figure 4 shows COAD's out-of-stream performance monotonically improving and approaching the IID upper bound as more in-stream data is processed. These are informative characterizations of the method's behavior in the streaming setting.

- **Demonstration that egocentric pretraining matters for egocentric OAD:** The consistent, large gap between ego and exo pretrained backbones across all tables (Table 1, Table 4) is a concrete contribution to the OAD literature's understanding, where prior work has focused on exocentric benchmarks with TSN-style frame-based features.

---

## Weaknesses

### Fatal
None.

### Major

- **Absence of continual learning baselines.** For a paper that positions itself squarely within the continual/streaming learning paradigm (citing on-device training, catastrophic forgetting, streaming video learning), the evaluation only compares against "Pretrained Only" and "w/o COAD" (unconstrained in-stream training). There are no comparisons to established CL baselines such as EWC, rehearsal/experience-replay with a small buffer, or other online adaptation techniques. The current tables show only that (a) some in-stream adaptation beats no adaptation (unsurprising), and (b) the proposed COAD strategies help over naive in-stream training. Without competitive CL baselines, the paper cannot establish that COAD is the right approach to streaming OAD — only that it improves over not adapting.

- **COAD underperforms naive training on in-stream mAP (ego setting) without adequate analysis.** Table 3 shows that the full COAD method achieves 36.8 in-stream mAP vs. 39.0 for the w/o COAD baseline under ego pretraining — a model with no proposed training strategies outperforms COAD on the user's own data by 2.2 mAP. Section 5.3 dismisses this as a "trade-off" and "balance" in a single sentence. For a method whose stated primary purpose includes "adaptation to the user's environment," performing below naive training on that same environment's data in a key metric warrants more investigation. It is not clear whether this gap is consistent, hyperparameter-sensitive, or specific to certain action classes.

### Minor

- **State continuity contributes negligibly per ablation (Table 3).** The row with State Continuity off but Orthogonal Gradient and Non-uniform Loss on (row 4: ✗ ✓ ✓) achieves 25.9/36.7 mAP and 75.8/89.2 Top-5 Recall, vs. the full COAD's 26.0/36.8 and 76.0/89.3. The differences are 0.1 mAP and 0.2 Recall (out-of-stream). Section 5.4 characterizes this as "a smaller but consistent gain," which understates how marginal the contribution is. Since state continuity is the only OAD-specific adaptation among the three components, its near-zero impact weakens the OAD-specific framing.

- **Pretraining set size is artificially small.** The dataset is split 186/1,177/519 for pretraining/in-stream/out-of-stream. Section 5.1 acknowledges this is intentional ("to better assess the impact of continuous learning"), but making the pretrained baseline weak by design also inflates the gains attributed to in-stream adaptation. A sensitivity analysis showing that COAD's gains persist across different pretraining set sizes would substantially strengthen the claim.

- **Abstract headline numbers cherry-pick the most favorable condition.** The "up to 20% in top-5 accuracy" comes from the exo pretraining in-stream setting (+22.5 Top-5 Recall; Table 1), where the baseline is weakest. The gain of COAD *over naive in-stream training* in the same condition is only +3.8 Top-5 Recall. The same abstract framing could honestly read "improves over naive in-stream training by up to ~4% in Top-5 Recall." This is not a fabricated number, but presenting the maximum vs. the weakest baseline without context in the abstract is misleading framing.

### Trivial

- Section 4 title uses "CODA" where the paper intends "COAD" (parser issue; the abbreviation is consistently COAD throughout).

---

## Nice-to-Haves

- **Per-user evaluation.** The primary motivation for COAD is personalizing AI systems to individual users on wearable devices. The current in-stream training pool consists of 1,177 diverse videos from many users; the out-of-stream set is similarly multi-user. Evaluating whether per-user streams improve that same user's held-out performance would directly demonstrate personalization. A subset of Ego4D likely has the same user across sessions.

- **Competing CL baselines.** Even simple replay with a 1-step or small buffer, or EWC applied to the RNN, would situate COAD's approach in the CL literature and make the method contribution evaluable.

- **Analysis of longer-horizon forgetting.** The learning curve in Figure 4 shows monotonic out-of-stream improvement, but whether in-stream performance degrades over the tail of the stream (model specializes and forgets earlier windows) is not examined. This matters for the stated use case of long-term on-device deployment.

- **Orthogonal gradient history.** The projection in Eq. 3 is applied against only the immediately preceding gradient window. A brief empirical comparison with k-step history or no projection would clarify why single-step decorrelation is sufficient for this streaming setting.

- **Annotator agreement statistics.** With 87 fine-grained classes from merged free-form descriptions, reporting inter-annotator agreement (before merging) would help users of the Ego-OAD dataset understand the label reliability.

---

## Removed Points

*These points are flagged to be removed; treat them with caution.*

- **Harsh Critic: "EPIC-KITCHENS out-of-stream shows COAD 'largely recovers to' pretrained baseline (Verb mAP 29.0 vs. 29.0)"** — Removed because the critic confused the table format. Table 2 reports "out/in" (out-of-stream / in-stream). The 29.0 figures are **in-stream** values. The out-of-stream Verb mAP is COAD = 11.8 > Pretrained Only = 11.4. COAD does improve out-of-stream on EPIC-KITCHENS on most metrics.

- **Harsh Critic: "Personalization narrative is structurally unable to demonstrate personalization"** — Demoted to Nice-to-Have. The paper's motivation does invoke personalization, but never explicitly claims per-user evaluation metrics. The evaluation design is consistent with domain generalization (which the paper's framing increasingly aligns with in the experiments). The mismatch between motivation and evaluation is real but not a fundamental invalidating gap — it is a direction for future work.

- **Harsh Critic: "The annotation merging strategy is aggressive without annotator agreement statistics"** — Demoted to Nice-to-Have. The paper's annotation design (union of annotators + manual semantic grouping) is described in Section 3. Absence of agreement statistics is a dataset characterization gap, not a validity-threatening flaw.

- **Harsh Critic: "One-step orthogonal gradient projection may be insufficient without theoretical justification"** — Demoted to Nice-to-Have. This is a methodological nicety, not a flaw. The technique is taken from Han et al. (2025) where it is validated; adapting it to the OAD streaming context without re-deriving theory is standard practice.

- **Harsh Critic: "Figure 4 IID upper bound is misleading"** — Removed. The paper explicitly presents IID training as an "upper bound" oracle, and the figure shows COAD steadily approaching it. There is no claim that COAD achieves the upper bound; the visual is used correctly as an aspirational reference. 

- **Strength Finder: "Well-defined novel task formulation… validated by results in Table 1"** — Partially retained. The task formulation is well-defined, but the "novel" framing is diluted by the explicit acknowledgment that all three techniques are borrowed from prior work and the three-way split protocol is directly from Carreira et al. (2024a). The contribution is adapting these to OAD — real but narrower than "novel task formulation with novel training strategies."

- **Strength Finder: "Demonstration of the importance of egocentric pretraining"** — Kept in slightly weaker form. The egocentric vs. exocentric pretraining comparison is a valuable empirical finding, but as a secondary result rather than a headline contribution.

---

## Novel Insights

The paper's most actionable finding — underappreciated in the current framing — is the empirical demonstration that the adaptation–generalization trade-off in streaming video learning is primarily governed by the non-uniform (final-step) loss, not by gradient decorrelation or state continuity. Table 3 shows that removing state continuity has near-zero effect when the other two components are present, while removing non-uniform loss causes out-of-stream Top-5 Recall to drop by 8.3 points. This suggests that loss locality (where in a window the supervision signal is computed) is the dominant factor for preventing streaming overfitting in RNN-based temporal models — a practical insight for any streaming temporal detection system, not just COAD. Combined with Figure 3's finding that even very sparse supervision (one labeled frame per ~68 seconds at stride 128) suffices for meaningful adaptation, this opens a practically important direction: streaming OAD under extremely sparse annotation budgets.

---

## Suggestions

1. **Add at least one standard CL baseline** (e.g., replay with a small buffer, or EWC). This is the single change most likely to strengthen the paper's claim that COAD is the right method for streaming OAD.
2. **Analyze and explain the in-stream mAP gap** (COAD 36.8 < w/o COAD 39.0 in ego pretraining). Identify which classes or stream segments drive this gap.
3. **Revise the abstract** to present gains relative to the directly comparable baseline (w/o COAD) in addition to the maximum vs. pretrained-only condition.
4. **Report per-user evaluation** on a Ego4D subset where individual users appear in multiple sessions, directly testing the personalization motivation.
5. **Add a sensitivity experiment** varying the size of the pretraining set (e.g., 186 vs. 500 vs. 1,000 pretraining videos) to show that COAD's gains are not purely a function of the artificially small pretraining baseline.

---

## Score and Decision

**Calibration anchors retrieved:**

| Path | Avg Score | Round | Comparison |
|---|---|---|---|
| Y7jJN0VQ4y | 5.71 | R1/R2 | CL for streaming video anomaly detection — similar structure (new task + CL method + benchmark), also lacks CL baselines; paper under review has stronger cross-dataset validation and larger dataset |
| Kh5OS3oNlg | 5.50 | R1/R2 | Ego4D annotation dataset paper — thinner technical contribution, no method novelty; paper under review is clearly stronger |
| RnxwxGXxex | 5.67 | R2 | CLDyB: Dynamic CL benchmarking — more rigorous benchmark methodology but narrower method scope; comparable level |
| TLADT8Wrhn | 6.25 | R2 | TiC-CLIP continual training — larger scale, more impactful benchmark, higher method novelty; paper under review is weaker |
| P6G1Z6jkf3 | 6.00 | R1/R2 | Egocentric representation learning with HOD — stronger method novelty, fully novel architecture; paper under review is weaker methodologically |
| MMEgo | 6.00 | R2 | Egocentric multimodal LLM with large QA dataset — larger dataset, more novel method; clearly stronger |
| jawV7vhGHw | 4.25 | R1 | Probabilistic adaptation for real-time video — weaker method formalization, no dataset; paper under review is stronger |
| Uj2Wjv0pMY | 4.33 | R1 | Procedural egocentric video error detection dataset — limited method novelty; comparable dataset contribution |
| M8gXSFGkn2 | 7.00 | R1 | EgoHOI benchmark — clearly stronger: novel benchmark + new method + thorough evaluation |
| Z5nqeTH24j | 4.40 | R2 | VidEgoThink egocentric benchmark — primarily benchmark contribution with limited method; comparable dataset contribution |
| j3BWS9kDYm | 5.00 | R2 | EgoLM egocentric motion — new architecture + new tasks but methodological gaps; roughly comparable |
| qnAZqlMGTB | 5.75 | R2 | StreamingBench for MLLMs — benchmark paper with strong characterization; comparable scope |

**Round 1 bracket:** 4.0–6.5

**Round 2 narrowing:** The paper sits clearly above the 4.0–4.5 range (has real cross-dataset validation, a large dataset, and systematic ablations — clearly better than Uj2Wjv0pMY and jawV7vhGHw). It is below the 6.0–6.5 range (P6G1Z6jkf3, MMEgo) because its method novelty is thin — all three training components are explicitly borrowed, and the main methodological gap (missing CL baselines) remains. It is closest to the 5.5–5.75 cluster (Y7jJN0VQ4y, RnxwxGXxex, qnAZqlMGTB): papers with a real contribution but significant gaps. The missing CL baselines — a standard requirement for a continual learning paper — and the unexplained in-stream mAP regression prevent a score of 6.0. The genuine dataset contribution and cross-dataset validation prevent a score below 5.0.

**Final score: 5.0 — Borderline Reject**

The paper has a legitimate dataset contribution (Ego-OAD) and useful empirical findings, but in its current form the method contribution is not well-enough supported: all training strategies are borrowed from prior work, the primary competing paradigm (standard CL methods) is not evaluated, and the key adaptation claim is undercut by COAD underperforming naive training on in-stream mAP in the most relevant (ego pretraining) condition without adequate analysis. With CL baselines added and honest framing of the mixed results, this paper could reach acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>