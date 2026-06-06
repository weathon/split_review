Now I have all the information I need to write the meta-review. Let me verify a few specific claims from the rebuttal.

Key verified facts:
- **Section 4.5 replay prohibition**: Confirmed at line 120: "no replay or storage of past data is permitted"
- **Table 1 in-stream ego**: COAD 36.8 mAP / 89.3 Recall vs w/o COAD 39.0 mAP / 86.7 Recall — rebuttal claim that COAD wins on Recall is verified
- **Table 1 in-stream exo**: Both COAD and w/o COAD at 31.0 mAP — rebuttal claim verified
- **Table 3 without non-uniform loss**: 21.8/42.4 mAP (out/in) — the higher in-stream mAP without non-uniform loss confirms the structural explanation
- **Table 3 state continuity row**: 25.9/36.7 vs 26.0/36.8 — 0.1/0.1 difference confirmed
- **EPIC-KITCHENS split** 293/202/137 — confirmed in Section 5.1
- **Table 2 w/o COAD overfitting**: Noun Top-5 Recall 36.6 out vs Pretrained Only 37.5, Action out 17.7 vs 21.9 — confirmed
- **"CODA" typo**: Confirmed at line 66: "Continuous OAD (CODA)"
- **EPIC-KITCHENS pretraining fraction**: 293/(293+202) = 59.3% — rebuttal claim verified

---

## Summary

This paper proposes **Continuous Online Action Detection (COAD)**, a task formulation enabling OAD models to adapt on-the-fly from streaming egocentric video via single-pass, causal training without data replay. The authors curate **Ego-OAD**, a large-scale benchmark derived from Ego4D Moment Queries (263h, 87 classes, 22,991 instances), adapt three training strategies (state continuity, orthogonal gradient projection, non-uniform loss) from prior work to the RNN-based OAD setting, and evaluate on Ego-OAD and EPIC-KITCHENS.

---

## Rebuttal Assessment

### Weakness: Absence of continual learning baselines
- **Author's response:** Partially address
- **Assessment:** Partially convincing. The rebuttal's strongest point — that replay-based methods are explicitly prohibited by the task formulation — is **confirmed by the paper** (Section 4.5: "no replay or storage of past data is permitted"). This genuinely rules out the majority of CL baselines. The EPIC-KITCHENS cross-validation also adds genuine independent evidence of COAD's utility: Table 2 confirms that w/o COAD overfits (Action out 17.7 vs Pretrained Only 21.9; Noun Top-5 Recall 36.6 vs 37.5), strengthening the claim that COAD is doing meaningful regularization. However, the argument that EWC is inapplicable to COAD is more contestable: the paper's task is within-task distributional adaptation, and Fisher regularization applied to pretrained weights requires no replay. The commitment to add EWC in revision does not count — it is not in the paper. The reviewer underweighted the replay-constraint argument and the EPIC-KITCHENS evidence, but the EWC gap is genuine.
- **Score impact:** Weakness downgraded (Major → Minor)

### Weakness: COAD underperforms naive training on in-stream mAP without adequate analysis
- **Author's response:** Partially address
- **Assessment:** Partially convincing. The rebuttal's three points are verifiable in the paper. (1) In the ego in-stream condition, COAD wins on Top-5 Recall (89.3 vs 86.7) — **confirmed**. The pattern is mAP vs. Recall trade-off, not uniform underperformance. (2) Figure 3 does map the in-stream/out-of-stream trade-off across learning rates and strides — confirmed. (3) Table 3 confirms the non-uniform loss structural explanation: without it, in-stream mAP rises to 42.4 but out-of-stream mAP collapses to 21.8. This is the clearest mechanical explanation for the gap, and it is already in the paper. However, Section 5.3's one-sentence treatment ("effectively balancing adaptation") remains thin, and no class-level or segment-level breakdown exists — the author commits to adding one only in revision.
- **Score impact:** Weakness downgraded (Major → Minor)

### Weakness: State continuity contributes negligibly
- **Author's response:** Partially address
- **Assessment:** Partially convincing. The architectural consistency argument (closing train–test discrepancy in hidden state handling) is genuine and confirmed by Sections 4.3–4.5. The ablation numbers (0.1 mAP, 0.2 Recall) are still marginal. The rebuttal's concession that the OAD-specific framing is weakened by state continuity's small effect is honest. The argument is conceptually sound but does not change the empirical verdict.
- **Score impact:** Weakness unchanged

### Weakness: Pretraining set size is artificially small
- **Author's response:** Partially address
- **Assessment:** Partially convincing. The rebuttal correctly distinguishes two claims: (a) the absolute gains over Pretrained Only are partly inflated by the small pretraining set — this concern remains valid; (b) the COAD-vs-w/o-COAD differential is unaffected by pretraining set size since both start from the same checkpoint — this is correct and reduces the severity. The EPIC-KITCHENS split (59% pretraining, verified as 293/495) providing an independent check is a meaningful point. The sensitivity analysis is promised only for revision.
- **Score impact:** Weakness downgraded (Minor → Trivial)

### Weakness: Abstract headline numbers cherry-pick favorable condition
- **Author's response:** Partially address
- **Assessment:** Partially convincing. The rebuttal's interpretation that the 20% gain is correctly attributed to "continuous learning" (not exclusively to COAD) is verified by the abstract text ("continuous learning from streaming videos improves..."). However, the abstract still does not report the COAD-vs-w/o-COAD gain, and the omission of the more informative reference point leaves readers with an inflated impression of COAD-specific improvements. The commitment to revise is future work.
- **Score impact:** Weakness unchanged

### Weakness: "CODA" typo in Section 4
- **Author's response:** Acknowledge
- **Assessment:** Confirmed at line 66. Minor issue.
- **Score impact:** Weakness unchanged (trivial)

---

## Strengths

- **Large-scale egocentric OAD dataset (Ego-OAD):** 263h, 87 classes, 22,991 instances with 36% overlap rate fills a genuine benchmarking gap; egocentric pretraining advantage (+10.1 Top-5 Recall) independently validates its domain specificity.
- **Empirically validated out-of-stream generalization:** COAD achieves +5.9 mAP / +6.9 Recall over Pretrained Only in ego pretraining (Table 1); cross-dataset validation on EPIC-KITCHENS (Noun Top-5 Recall 50.2 vs. 37.5 Pretrained Only) provides independent evidence, as does the w/o COAD overfitting pattern confirmed in Table 2.
- **Explicit task formulation with principled constraints:** The no-replay, single-pass, causal training protocol is internally consistent and motivationally coherent for wearable device deployment; Section 4.5 clearly states the constraints.
- **Characterization of adaptation–generalization trade-off:** Figure 3 and Table 3 together show that non-uniform loss (not orthogonal gradient or state continuity) is the dominant driver of out-of-stream generalization, a practically important finding for streaming temporal detection.

---

## Weaknesses

### Fatal
None.

### Major
- **No EWC-class CL baseline:** Replay-based baselines are legitimately excluded by the task protocol. However, EWC-style regularization (Fisher penalty on pretrained weights, no replay) remains applicable and is absent. The rebuttal commits to adding it only in revision. Without it, the paper cannot fully situate COAD against the broader no-replay CL literature.

### Minor
- **State continuity is near-zero empirically:** The 0.1 mAP / 0.2 Recall contribution (Table 3) is marginal. The architectural consistency argument is reasonable but weakens the OAD-specific framing, as the dominant gains come from two methods adapted directly from prior work.
- **In-stream mAP gap inadequately analyzed:** The 2.2 mAP gap (COAD 36.8 < w/o COAD 39.0 in ego in-stream) is mechanically explained by the non-uniform loss design (confirmed via Table 3), but Section 5.3's treatment remains a single sentence; no class- or segment-level breakdown is provided.
- **Abstract framing still incomplete:** The 20% figure is not COAD-specific; the COAD-over-w/o-COAD delta (+4.4 Top-5 Recall in ego out-of-stream) is absent from the abstract, leaving readers with an inflated impression of method-specific gains.

### Trivial
- "CODA" typo in line 66 of Section 4 where "COAD" is intended throughout the paper.
- Pretraining set is intentionally small (186 of 1,882 videos); no sensitivity analysis across pretraining fractions is in the paper.

---

## Nice-to-Haves
- Per-user evaluation on Ego4D sessions with repeated user appearances to directly test personalization motivation.
- Sensitivity experiment varying pretraining set size to disentangle baseline weakness from adaptation gains.
- EWC (or similar no-replay regularization) CL baseline comparison.
- Longer-horizon forgetting analysis (whether in-stream performance degrades as the stream specializes).
- Annotator agreement statistics for the 87-class semantic grouping.

---

## Novel Insights

The rebuttal reinforces an underappreciated insight from Table 3 that the original review identified: within COAD, the non-uniform (final-step) loss is overwhelmingly the dominant mechanism preventing streaming overfitting (+4.2 mAP, +8.3 Top-5 Recall out-of-stream; without it, in-stream mAP actually rises to 42.4 while out-of-stream collapses to 21.8). The rebuttal's observation that this is structural — dense supervision inflates per-step gradient magnitude — extends the finding: the choice of *where* in a temporal window supervision is applied, not how gradients are decorrelated or how hidden states are managed, governs adaptation–generalization balance in RNN-based streaming detection. Combined with Figure 3's finding that sparse supervision (one label per ~68s at stride 128) suffices for meaningful generalization, COAD's most actionable contribution is demonstrating that final-step loss locality is the critical ingredient for streaming OAD, not the more architecturally elaborate gradient projection.

---

## Suggestions

1. Add an EWC-style baseline (Fisher regularization applied within the single-pass, no-replay constraint) to situate COAD in no-replay CL literature — this was correctly identified as the remaining gap even after the rebuttal.
2. Provide a class-level or segment-level breakdown of the in-stream mAP gap between COAD and w/o COAD to characterize which actions drive the trade-off.
3. Revise the abstract to report the COAD-vs-w/o-COAD gain alongside the vs-Pretrained-Only gain so readers can distinguish method-specific from adaptation-in-general improvements.
4. Add a sensitivity experiment with varying pretraining set sizes to disentangle weak-baseline inflation from genuine COAD gains.
5. Correct the "CODA" typo in Section 4, line 66.

---

## Score and Decision

The rebuttal provides substantive and verifiable responses to two of the original major weaknesses:

1. The replay constraint is explicitly stated in Section 4.5 and genuinely rules out replay-based CL baselines. The original review was too quick to group all CL baselines together.
2. The in-stream mAP gap has a mechanical explanation verified in Table 3 (non-uniform loss structurally reduces per-step gradient magnitude), and the pattern is mAP-vs-Recall trade-off rather than uniform underperformance.
3. The EPIC-KITCHENS cross-validation evidence (w/o COAD overfitting) is more compelling than the original review credited.

However, the rebuttal does not change the paper's actual content — all additions are committed for revision only. The EWC baseline gap remains unaddressed in the current submission. Method novelty (all three components borrowed from prior work) is unchanged. The abstract framing issue persists.

The rebuttal moves the major weaknesses to minor status through legitimate arguments grounded in the paper, which warrants a small score adjustment. The paper now reads as a borderline case with a genuine dataset contribution, cross-dataset validation, and reasonable (if thinly novel) method adaptation, but still lacking a no-replay CL comparison that would firmly establish COAD's place in the CL landscape.

**Score: 5.5 — Borderline Reject/Borderline Accept**

The rebuttal partially rehabilitates the paper by clarifying the task constraints and the mechanical source of the in-stream/out-of-stream trade-off, but with all substantive additions deferred to revision, the current submission remains below the acceptance bar.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>