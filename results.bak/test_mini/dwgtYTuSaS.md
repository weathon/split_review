Now I have all the information I need. Let me construct the final review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
- strength 1 with evidence
- strength 2 with evidence

## Weaknesses
### Fatal
### Major
- weakness 1 — why it matters
### Minor
- weakness 1 — why it matters
### Trivial
- weakness 1

## Nice-to-Haves
- suggestion that would improve but is not a core flaw

## Removed Points
Include something like this "These points are flagged to be removed, treat them with caution"
Weaknesses that are removed keep the details of the S/W just in case they are useful 

## Novel Insights

## Suggestions

## Score and Decision

Let me write the review now.

---

Now let me think about the round-1 bracket and round-2 calibration:

Round 1 bracket: Based on the three queries, the weak anchors averaged ~3.0, middle anchors averaged 4.0-6.0, and strong anchors averaged 8.0. The paper clearly sits in the middle band — it has real contributions but significant evaluation weaknesses. I'd bracket it between 3.5 and 5.5.

Round 2 narrowing: The second batch of queries for scores (3.5, 6.0) returned anchors at 4.0-5.5. Reading these anchors:

1. EgoNight (5.0, Poster) - benchmark paper with dataset contribution, but limited method novelty and some evaluation concerns. Comparable dataset contribution level. But EgoNight has cleaner evaluation (just testing existing models) while COAD has more evaluation issues.

2. TV-Online (4.5, Reject) - benchmark+method paper that was rejected. Method novelty concerns similar to COAD's. TV-Online had more rigorous evaluation though. COAD is comparable or slightly weaker due to the in-stream mAP issue and EPIC-KITCHENS weakness.

3. IIKC (5.5, Poster) - stronger theoretical contribution, cleaner experiments. COAD is clearly weaker.

Comparing COAD to these anchors: COAD's dataset contribution (Ego-OAD) is solid, but the evaluation issues are more substantial than EgoNight's. The method is more incremental than IIKC. I'd place it near TV-Online's score but slightly below — around 4.0.

Final score: **4.0**. This is a borderline reject — the dataset and task formulation have merit, but the evaluation shortcomings and incremental method prevent acceptance in current form.## Summary

This paper introduces **Continuous Online Action Detection (COAD)**, a task formulation that requires models to perform online action detection while continuously adapting from a single-pass, causal video stream without data storage or replay. It also contributes **Ego-OAD**, a large-scale egocentric OAD benchmark (87 classes, ~23k instances, 263h) derived from Ego4D Moment Queries. The proposed method combines a GRU-based OAD head with orthogonal gradient projection (from Han et al. 2025), non-uniform loss weighting (from An et al. 2023), and state continuity. Results on Ego-OAD show gains in out-of-stream Top-5 Recall (up to 6.9% absolute) over a pretrained-only baseline.

---

## Strengths

1. **Ego-OAD benchmark addresses a clear gap.** The paper curates a substantial egocentric OAD dataset (87 classes, 22,991 instances, 263h, 36% overlapping actions) from Ego4D MQ, filling the need for realistic, multi-label, temporally-grounded egocentric OAD data that prior datasets (EPIC-KITCHENS is single-domain, THUMOS14 is exocentric) do not cover. This is likely the most valuable contribution and could benefit future research.

2. **Clear ablation study isolating each component.** Table 3 systematically ablates state continuity, orthogonal gradient, and non-uniform loss on Ego-OAD. The results show that removing orthogonal gradient drops out-of-stream Top-5 Recall by 4.5%, removing non-uniform loss drops it by 8.3%, and removing state continuity drops it by 0.2% — providing concrete evidence that each element contributes.

3. **COAD improves out-of-stream generalization over the pretrained-only baseline.** On Ego-OAD (Table 1, ego pretrain, out-of-stream), COAD achieves 76.0% Top-5 Recall vs. 69.1% for pretrained only, with w/o COAD at 71.6%. This demonstrates that the full method produces meaningful generalization gains on the proposed benchmark.

4. **The formal definition of the COAD task is clearly specified.** Section 4.5 provides explicit constraints (single-pass, causal ordering, batch size one, no data storage, state continuity), cleanly distinguishing COAD from standard offline OAD and establishing a well-scoped problem formulation for on-device adaptation.

---

## Weaknesses

### Fatal

None.

### Major

1. **The primary adaptation claim rests on a secondary metric and masks a concerning trend on the primary metric.** Table 1 (Ego-OAD, Ego pretrain, in-stream) shows that **w/o COAD achieves 39.0 mAP while COAD gets only 36.8 mAP** — the baseline *without* the proposed components actually outperforms the full method on the primary OAD metric (mAP) in the in-stream setting. The paper's headline "improves adaptation by up to 20%" is computed from Top-5 Recall (89.3 vs. 73.3), which is a secondary metric. The paper acknowledges this implicitly ("the baseline achieves competitive results, but this often comes at the cost of reduced generalization") but the framing of the abstract and introduction emphasizes the 20% figure without this caveat. For a paper titled "continuous online action detection," the method underperforming simple baselines on in-stream mAP is a significant concern that undermines the central adaptation claim.

2. **The EPIC-KITCHENS results contradict the generality claims.** Table 2 shows that on **Action mAP (out-of-stream)**, COAD achieves 7.9 while the **Pretrained Only** baseline achieves 9.6 — the method is *worse* than doing nothing. Similarly, on Action Top-5 Recall (out-of-stream), COAD gets 20.5 vs. Pretrained Only's 22.9. The paper attributes this to the "fine-grained nature of the actions and annotations in EPIC-KITCHENS" without supporting analysis. This explanation is ad-hoc, and the fact that COAD underperforms a frozen pretrained model on a standard benchmark significantly weakens the claim that COAD is a general-purpose solution for egocentric OAD.

3. **The critical IID upper bound is relegated to a qualitative figure without numerical values.** Figure 4 shows an "IID Training" upper bound approaching ~30 mAP (out-of-stream) — substantially above COAD's ~26 mAP — but no exact numbers are given, and the IID bound does not appear in the main result tables. Without knowing the precise gap between COAD and a model trained offline on the full data, the reader cannot assess whether COAD's gains are meaningful or whether they merely reflect a poor initialization from the small pretraining set (186 videos vs. 1,177 in-stream videos). This is the most important comparison for evaluating the method, and it is not presented quantitatively.

### Minor

4. **The method components are directly adopted from prior work with minimal adaptation.** Orthogonal gradient projection is taken from Han et al. (2025), non-uniform loss from An et al. (2023) (MiniROD), and state continuity is standard RNN practice. The paper's contribution is a specific combination applied to a new setting — a valid but incremental contribution. The framing as a "novel task formulation" is reasonable (adapting Carreira et al. 2024a's continuous learning to the OAD setting with multi-label, overlapping actions), but the method-level novelty is modest.

5. **No comparison against standard continual learning regularization techniques.** The orthogonal gradient method is only compared against a "w/o COAD" baseline. Even though replay is excluded by design (no data storage constraint), regularization-based continual learning methods such as EWC or SI do not require data storage and could provide informative baselines for understanding whether orthogonal gradient offers distinct advantages over simpler regularization.

6. **No variance or statistical significance reported.** Given the single-pass, batch-size-one training protocol, results may vary across runs or data orderings. The paper reports a single number per condition.

### Trivial

- Non-uniform loss is described as enabling "training with sparse instead of dense frame-level annotations" (Section 4.5), but the Ego-OAD annotations are dense per frame; the loss is simply computed only at the final step. This is a computation design choice, not a label-efficiency advantage.

---

## Nice-to-Haves

- Include the IID upper bound from Figure 4 as a row in Table 1 with exact numerical values.
- Analyze why EPIC-KITCHENS results differ from Ego-OAD: e.g., compare action durations, label granularity, repetition patterns.
- Report means and standard deviations over multiple runs or data-order permutations.
- Compare against a regularization-based continual learning method (e.g., EWC applied to the OAD head) as an additional baseline.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Missing appendix / missing proofs in appendix**: The parser strips these; they exist in the original submission.
- **Missing comparisons to Transformer-based OAD methods (TeSTra, GateHub, LSTR)**: The paper scopes these out in Section 2, arguing they are too costly for on-device deployment, which is a reasonable scope choice. Mentioning this as a limitation is scope creep.
- **Critique that state continuity is a "standard design choice"**: This is true but trivially so; it is listed as a component, not claimed as a novel invention.
- **Critique about the data split favoring the method**: The split design is a deliberate choice to emphasize the in-stream adaptation scenario. A reasonable reviewer could disagree, but the paper states the rationale transparently (Section 5.1).
- **Claim that the backbone could be fine-tuned**: The frozen backbone is an explicit design constraint for resource-constrained deployment; criticizing this is imposing a different problem definition.
- **Missing related works**: Cannot be verified without external sources.
- **Formatting/style nitpicks**: Parser artifacts.

---

## Novel Insights

None beyond the paper's own contributions. The reviews surface two interesting tensions that the paper itself does not fully grapple with: (1) the in-stream mAP reversal (w/o COAD beats COAD) suggests the proposed components may *constrain* adaptation while helping generalization — the paper acknowledges this framing but does not provide analysis of *why* this trade-off occurs or whether it is inherent to the method or an artifact of the hyperparameters; (2) the EPIC-KITCHENS failure mode suggests the method's effectiveness depends on dataset characteristics that are not identified, making it unclear when practitioners should expect COAD to help versus hurt.

---

## Suggestions

1. **Add the IID baseline to Table 1 with exact numbers.** This is the single most impactful change — it would allow readers to calibrate how much of the reported gain is meaningful adaptation vs. recovery from a deliberately weak initialization.
2. **Analyze the in-stream mAP gap.** Explain why w/o COAD outperforms COAD on in-stream mAP (39.0 vs. 36.8 on Ego-OAD). Is this because orthogonal gradient projection slows adaptation? Could a tuned learning rate or different stride resolve this?
3. **Provide a deeper analysis of EPIC-KITCHENS failure.** Either characterize the conditions under which COAD is effective (e.g., action duration thresholds, label coarseness) or explicitly reframe the claims to acknowledge this limitation.
4. **Temper the headline claims.** The "up to 20% adaptation" is on Top-5 Recall in the in-stream setting where w/o COAD also improves by 13.4% — the absolute gain over w/o COAD is 2.6%, and on mAP COAD actually underperforms w/o COAD. The abstract and introduction should reflect this nuance.

---

## Score and Decision

### Calibration Report

**Round 1 (Bracketing):** Three queries on "online action detection continual learning video" returned:
- Weak band (<3.5): anchors at avg 3.0, 3.0, 3.0, 1.0 — clearly below this paper
- Middle band (3.5–7.5): anchors at avg 4.0, 5.0, 4.5, 6.0 — this paper sits in this range
- Strong band (>7.5): anchors at avg 8.0 — clearly above this paper

**Initial bracket:** 3.5 – 5.5

**Round 2 (Narrowing):** Three queries within (3.5, 6.0) on egocentric video, online video understanding, and continual learning returned anchors including:
- EgoNight (5.0, Poster) — comparable dataset contribution but cleaner evaluation
- TV-Online (4.5, Reject) — similar method-novelty concerns, comparable evaluation rigor
- IIKC (5.5, Poster) — stronger theoretical method contribution, cleaner experiments
- StPR (5.0, Poster) — stronger technical novelty, rigorous experiments

**Comparison to anchors:** COAD has a solid dataset contribution comparable to EgoNight (5.0), but its evaluation contains more significant issues (in-stream mAP reversal, EPIC-KITCHENS failure, missing IID bound in tables). The method is more incremental than StPR (5.0) or IIKC (5.5). It is comparable to TV-Online (4.5, Reject) in overall quality: both have a useful benchmark and a reasonable but incremental method, undermined by evaluation gaps that prevent the core claims from being fully supported. COAD is slightly weaker due to the in-stream mAP issue that directly contradicts the adaptation narrative.

**Final score: 4.0** — The dataset and task formulation have genuine value, but the evaluation does not sufficiently support the paper's central claims, and the method contributions are incremental. With major revisions addressing the IID baseline inclusion, EPIC-KITCHENS analysis, and more careful claim framing, the paper could become a solid contribution.

MY FINAL SCORE: <score>4.0</score>
MY FINAL DECISION: <decision>Reject</decision>