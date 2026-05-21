Now I have enough calibration to write the final review.

## Summary
The paper introduces Continuous Online Action Detection (COAD), a task formulation in which an OAD model performs single-pass, on-the-fly adaptation on a streaming egocentric video without data storage or replay. It contributes (i) Ego-OAD, a 263-hour, 87-class egocentric OAD benchmark curated from the Ego4D Moment Queries split, and (ii) a training procedure that combines hidden-state continuity, orthogonal gradient projection (Han et al., 2025), and last-step non-uniform loss weighting (An et al., 2023). Results are reported on Ego-OAD and EPIC-KITCHENS with an out-of-stream / in-stream split protocol following Carreira et al. (2024a).

## Strengths
- **Concrete new benchmark.** Ego-OAD is large-scale and egocentric (Sec. 3: 87 classes, 22,991 instances, 263h of video, 36% temporally overlapping instances), and it is one of the first egocentric OAD benchmarks beyond kitchen scenes, broadening the field beyond EPIC-KITCHENS.
- **Clean experimental protocol for the proposed task.** Sec. 5.1 partitions data into disjoint pretraining / in-stream / out-of-stream splits, separating "adaptation during the stream" from "generalization on held-out videos" in an interpretable way.
- **Out-of-stream generalization gains are real and consistent.** Table 1 shows COAD improving out-of-stream Top-5 Recall over Pretrained Only by 6.9 pts (Ego) and 6.5 pts (Exo), with mAP also moving up; Fig. 4 shows out-of-stream performance steadily approaching the IID upper bound across stream training.
- **Ablation isolates the dominant component.** Table 3 makes it visible that non-uniform loss is the main driver of out-of-stream gains (removing it drops out-of-stream mAP from 26.0 → 21.8 and Top-5 Recall from 76.0 → 67.7), which is a useful and honest finding.

## Weaknesses

### Fatal
None — the concerns below are real but do not, individually or together, invalidate the contribution.

### Major
- **The headline "20% adaptation" gain conflates training-on-the-stream with the proposed method.** Abstract and intro claim "up to 20% in top-5 accuracy" of adaptation gain. In Table 1 the cited 22.5-pt jump (Exo in-stream Top-5 Recall, 57.5 → 80.0) is largely captured by the "w/o COAD" baseline that simply trains on the stream without any of the three COAD strategies (76.2; +18.7 of the 22.5 pts). The COAD-specific contribution there is ~3.8 pts; on Ego in-stream mAP, COAD actually loses 2.2 mAP relative to w/o COAD (39.0 → 36.8). The reporting is literally faithful, but the contribution attributable to the paper's method is meaningfully smaller than the abstract implies.
- **"Personalization" is the motivating claim but is never directly evaluated.** The intro/conclusion repeatedly invoke per-user, on-device personalization, but the in-stream set is 1,177 videos pooled across users (Sec. 5.1) and no per-user (train on user *u*, test later on user *u* vs *u'*) analysis is performed. The in-stream metric is computed during single-pass training over that same data (Sec. 5.1: "we evaluate adaptation by measuring performance at each optimization step"), which is closer to an online training-regret quantity than to "adaptation to a user's environment." This is a structural mismatch between motivation and what the experiments measure.
- **EPIC-KITCHENS does not corroborate the main story.** In Table 2, COAD's in-stream Action numbers tie or underperform Pretrained Only (mAP 7.9 vs 9.6; Top-5 Recall 20.5 vs 22.9), and out-of-stream Action gains are slim (mAP 8.6 → 9.9). Sec. 5.3 dismisses this as "fine-grained nature of the actions," but since EPIC-KITCHENS is the standard egocentric OAD benchmark, weak results there cast doubt on the generality claim, which then rests almost entirely on the authors' own Ego-OAD.
- **No contemporary OAD baselines on Ego-OAD.** Although Sec. 2 surveys LSTR, TeSTra, GateHub, MiniRoD, etc., the only comparisons are "Pretrained Only" and "w/o COAD." Without at least one strong OAD baseline on Ego-OAD trained under both offline and COAD protocols, the benchmark is not calibrated against the field, and the claim that an RNN backbone is a reasonable choice in this setting is not externally validated.
- **State continuity contributes ~nothing in the ablation.** In Table 3, removing state continuity moves the numbers from 26.0/36.8 mAP and 76.0/89.3 Recall to 25.9/36.7 and 75.8/89.2 — essentially noise — yet state continuity is one of the three named pillars and is highlighted in Fig. 2. The paper should either down-claim this component or analyze where it actually helps.

### Minor
- **"Wearable" / "on-device" / "resource-constrained" framing is never tested.** Secs. 1 and 6 invoke wearable deployment, but no FLOPs, latency, parameter count, memory footprint, or on-device demonstration is reported. The framing should either be backed up with efficiency evidence or softened.
- **Orthogonal-gradient horizon-1 is unmotivated.** Sec. 4.5 projects $g_t$ only onto $g_{t-1}$, while the same paragraph motivates the projection by "strong temporal correlations between consecutive windows" — which the paper itself implies extends beyond one step. The choice of horizon-1 deserves either an ablation or a justification specific to the OAD setting.
- **No reported variance / single-seed numbers.** Many of the COAD-vs-w/o-COAD deltas are 0.5–2 points (e.g., Ego in-stream mAP 36.8 vs 39.0; out-of-stream mAP 26.0 vs 25.5); a small number of seeds would substantially change confidence in some rankings.
- **Label-merging is consequential but described only at a high level.** Sec. 3 says "we manually grouped semantically similar free-form action descriptions" and defers details to Appendix A. The 87-class taxonomy is the product of subjective decisions; a brief quantitative analysis of how merging affects per-class statistics (and thereby mAP) would help calibrate the headline numbers.
- **IID upper bound is referenced in text but not clearly shown in Fig. 4.** Sec. 5.4 frames Fig. 4 as showing COAD "narrowing the gap to this upper bound," but the figure caption/legend lists only COAD variants and Pretrained Only.

### Trivial
None.

## Nice-to-Haves
- A per-user evaluation (train on a portion of user *u*'s stream, test on later segments of *u* vs *u'*) would directly test the personalization narrative and make the EPIC-KITCHENS counter-result interpretable (does the model fail to fit the stream, or does fitting not transfer to held-out segments from the same user?).
- A mechanistic diagnostic of orthogonal-gradient projection (e.g., gradient cosine similarities over consecutive windows with/without projection, or where in the stream it prevents degradation) would convert the current "we combined three techniques" framing into a real mechanistic story.
- Running at least one strong OAD method (e.g., LSTR or TeSTra) under both offline and COAD protocols on Ego-OAD would calibrate the benchmark.
- Reporting FLOPs / latency / memory per update would make the wearable framing concrete.

## Removed Points
These points are flagged to be removed; treat them with caution.
- *Harsh-critic remark that "w/o COAD" being competitive in some cells "obscures" the contribution* — this is largely a re-statement of the headline-conflation issue and is already captured under Major (avoiding duplication).
- *Generic "evaluation lacks rigor" framing* — kept only where it points at the specific identified problem (per-user, baselines, variance); area-of-concern sweep removed.
- *Strength: "Performance over training approaches the IID upper bound" (Fig. 4)* — partially kept, but downgraded because the figure does not clearly plot the IID bound; we keep the "narrowing gap" claim only as a strength about the trend, not the bound itself.
- *Strength: "Validation on a second dataset (EPIC-KITCHENS)"* — dropped: a verified weakness contradicts it. Out-of-stream Action gains are slim and in-stream COAD ties or underperforms Pretrained Only (Table 2), so this does not function as cross-dataset validation in the way the Strength Finder framed it.
- *Strength: "Ablation isolates contribution of each component"* — kept in spirit, but cited carefully: the ablation actually shows that one of the three named components (state continuity) contributes within noise, which is the basis for a Major weakness.

## Novel Insights
None beyond the paper's own contributions. The submission's most interesting empirical observation — that non-uniform last-step loss is doing most of the generalization work while state continuity contributes essentially nothing — is visible in the paper's own ablation table but not explored as such.

## Suggestions
- Re-state the abstract/intro in terms of the COAD-specific delta over the "w/o COAD" baseline rather than over Pretrained Only, or report both side-by-side so readers can see what is attributable to the method vs. to training on the stream at all.
- Add a per-user split for Ego-OAD (or for a sub-population where Ego4D's user IDs allow it) and report train-on-user-*u* / test-on-user-*u* vs *u'* numbers; this is the natural test for the personalization claim.
- Add at least one Transformer-based OAD baseline (LSTR or TeSTra) trained under both offline and COAD protocols on Ego-OAD, so the benchmark is calibrated against the field and so the RNN choice can be evaluated.
- Either report FLOPs / latency / per-step memory or remove the "on-device / wearable / resource-constrained" framing from intro and conclusion.
- Run a small ablation on the orthogonal-projection horizon (>1 prior gradient) and a sanity check / mechanistic plot for state continuity; if it genuinely contributes nothing, down-claim it from a pillar to a design choice.
- Report results across multiple seeds for the close cells (e.g., Ego in-stream mAP 36.8 vs 39.0; Ego out-of-stream mAP 26.0 vs 25.5).
- Either acknowledge EPIC-KITCHENS as a counter-result that constrains generality, or run an analysis (e.g., per-class breakdown of where COAD helps vs hurts) that supports the fine-grained-actions hypothesis.

## Evaluation on the Stated Axes
- **Originality:** Moderate. The COAD task is a meaningful re-framing of OAD as continuous on-stream learning, but the three constituent training techniques are imported (Han et al., 2025; An et al., 2023; state continuity per Carreira et al., 2024a). The benchmark is the more original contribution.
- **Importance of research question:** Real. Adaptation on streaming egocentric video matters for the wearable-device use case the paper sets up.
- **Whether claims are well supported:** Partially. The "20% adaptation" headline is mostly attributable to training on the stream at all; the "personalized AI" claim is not directly tested; EPIC-KITCHENS does not corroborate the generality claim.
- **Soundness of experiments:** Reasonable protocol, single-seed numbers, no contemporary OAD baselines, ablation reveals one of the three named components contributes within noise.
- **Clarity of writing:** Generally clear, but the gap between motivation (per-user, on-device) and what is measured (pooled in-stream training trajectory) is glossed over.
- **Value to the research community:** Ego-OAD is the most reusable artifact if the curation pipeline (label-merging mapping) is released; the method itself is incremental.

## Calibration Trace
Anchors retrieved:

Round 1 (bracketing):
- `/Jq8HYNZG9s.md` — ShadowPunch (avg 3.00): weak dataset paper, more limited and less rigorous than this submission.
- `/2HdZPEQUig.md` — Efficient Object-Centric Learning for Videos (avg 3.00): less topically relevant.
- `/TadxJc1XAE.md` — TeacherActivityNet (avg 3.00): much weaker / narrower dataset paper.
- `/AfZH9EEuRR.md` — EgoQR (avg 2.20): egocentric wearable task, much weaker.
- `/RnxwxGXxex.md` — CLDyB (avg 5.67, accept): a CL benchmark paper, more methodologically thorough than the submission.
- `/7L2bpe7lfm.md` — Large Scale Video Continual Learning (avg 4.50, reject): closest comparable — video CL with new benchmark angle, similarly mixed reception. Read in full.
- `/BrqFB8Nl7e.md` — Continual Learning After Model Deployment (avg 3.75): conceptually related, weaker support.
- `/G9Ea7mlqGO.md` — CLIP Online CL (avg 3.80): less topically relevant.
- High band (≥7.5): `/SctfBCLmWo.md`, `/7gUrYE50Rb.md`, `/QQ6RgKYiQq.md`, `/9Cu8MRmhq2.md` — all 8.00, but topically different.

Round-1 bracket: 3.5–5.5. The submission is clearly above the bottom anchors (it has a real, large-scale benchmark and a reasonable, if incremental, method) but the verified concerns (headline conflation, no personalization evaluation, EPIC-KITCHENS counter-results, weak state-continuity ablation, no contemporary baselines) keep it below clear-accept anchors.

Round 2 (narrowing within 3.5–6.5):
- `/WnEnU2K3Rb.md` — Beyond the Benchmark (avg 4.25, reject): new dataset + method for VAD, methodologically uneven — close comparable to this submission.
- `/tEei1bolt3.md` — Motion-Grounded Video Reasoning (avg 5.00, reject): new task + dataset; better methodological articulation than this submission.
- `/Uj2Wjv0pMY.md` — Detective Hat (avg 4.33, reject): egocentric 4D procedural dataset; narrower scope.
- `/wMRFTQwp1d.md` — VideoEval (avg 4.00, reject): benchmark-only paper.
- `/qnAZqlMGTB.md` — StreamingBench (avg 5.75, reject): streaming-video benchmark, more thoroughly evaluated; better-supported headline claims than this submission.
- `/TLADT8Wrhn.md` — TiC-CLIP (avg 6.25, accept): web-scale continual training benchmark with strong empirical scaffolding — clearly stronger than this submission.
- `/4sJJixGIZX.md` — Online Continual Graph Learning (avg 5.00, reject): comparable in flavor (new setting + method).

Round-2 narrowing: The submission sits closest to "Large Scale Video CL" (4.50, reject) and "Beyond the Benchmark" (4.25, reject) — both of which propose a benchmark + a method but suffer from limited baseline comparisons and methodological gaps the way this submission does. It is weaker than StreamingBench (5.75) on rigor of evaluation against the stated motivation, and below TiC-CLIP (6.25) by a clear margin. The benchmark contribution lifts it above 3.0-tier dataset-only papers.

Final placement: 4.0 — close to "Large Scale Video CL" (4.5) but discounted slightly for the verified headline-conflation in the abstract, the personalization-claim/evaluation mismatch, and the EPIC-KITCHENS counter-result. Not below 4.0 because Ego-OAD itself is a real contribution and the out-of-stream gains are genuine.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>