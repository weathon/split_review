Now I have sufficient information to synthesize the review. Let me construct the final consolidated review.

## Summary
2-3 sentence summary of the paper's contribution.

## Strengths
List concrete strengths with evidence.

## Weaknesses
Rank by severity. Be careful about what to include from the harsh critic.

## Score and Decision

Let me organize my thoughts and write the review.

---

**Key decisions on each weakness:**

1. **IID baseline in Figure 4** - The caption lists 4 curves, none is "IID Training". The text claims it's included and that COAD "narrows the gap." This is a genuine discrepancy. **Keep as Major.**

2. **Personalization claims not tested** - The paper frames COAD as enabling "adaptation to individual users" but experiments use aggregate in-stream/out-of-stream splits without per-user analysis. **Keep as Major** (since it's a gap between claims and evaluation).

3. **Streaming protocol underspecified** - How 1,177 videos are processed as a continuous stream (hidden state management at boundaries) is unclear. **Keep as Minor.**

4. **Dataset from only validation split** - The paper uses only the Ego4D MQ validation split without explanation. **Keep as Minor** - it's an unexplained design choice but doesn't invalidate results.

5. **Multi-label ambiguity** - Paper already acknowledges this and describes mitigation. The critic's suggestion about inter-annotator agreement is nice-to-have. **Remove** (paper addresses it, or move to Nice-to-have).

6. **Orthogonal gradient only consecutive** - Design choice, not a weakness. The critic's suggestion about ablation depth is nice-to-have. **Remove** from weaknesses, move to Nice-to-have.

7. **State continuity in w/o COAD** - w/o COAD deliberately uses a different training protocol (shuffled windows with state resets). This is by design, not a flaw. **Remove** (misunderstanding).

8. **EPIC-KITCHENS unusual pattern** - In-stream Noun mAP (3.8) much lower than out-of-stream (31.4). Paper's explanation is brief. **Keep as Minor** - it's a valid observation.

9. **Qualitative top-1 only** - Minor presentation choice. **Remove** or move to Trivial.

**Strengths from Strength Finder:**
1. New task formulation (COAD) - genuine
2. Large-scale benchmark (Ego-OAD) - genuine
3. Consistent improvements - genuine and supported by Table 1
4. Ablation study - genuine and clean (Table 3)
5. Sparse supervision analysis - genuine (Figure 3)
6. Backbone comparison - genuine but more of a finding than a strength per se

Let me keep 1-5 as strengths.

Now let me finalize the score. Based on calibration:
- Weak anchors: 1.67-3.00 (paper is clearly stronger)
- Middle anchors: 3.75-5.71 (paper is comparable to upper end)
- Strong anchors: 7.5+ (paper is clearly weaker)

The most comparable papers are "Anomalies are Streaming" (5.71, Reject) and "PARSE-Ego4D" (5.50, Reject). The paper under review has similar contribution type (new task + benchmark + baselines) with similar levels of issues.

I'll score 5.0. It's a paper with meaningful contributions but notable gaps between claims and evaluation. The core value (task definition, dataset) is solid but the evidence for some claims is incomplete.

Decision: Reject (with encouragement to revise)Now I have all the information needed to produce the final consolidated review.

## Summary

The paper introduces **Continuous Online Action Detection (COAD)**, a task formulation that extends standard Online Action Detection by requiring models to adapt via single-pass training directly from a continuous video stream without storing data or multiple training epochs. The authors curate **Ego-OAD**, a new large-scale benchmark (87 action classes, 22,991 instances, 263 hours of video) derived from the Ego4D Moment Queries split, and propose training strategies (state continuity, orthogonal gradient projection, non-uniform loss) for an RNN-based detection head. Experiments on Ego-OAD and EPIC-KITCHENS show that COAD improves out-of-stream generalization compared to a pretrained-only baseline and naive online fine-tuning.

## Strengths

1. **Well-motivated new task formulation (COAD).** The paper identifies a genuine gap — standard OAD models train offline and cannot adapt post-deployment. COAD formalizes the problem of single-pass, no-replay learning from a continuous video stream, which is a natural fit for egocentric wearable devices. This bridges online action detection and on-device continual learning in a clean, well-defined setting (Section 4).

2. **Large-scale, realistic egocentric OAD benchmark (Ego-OAD).** The dataset provides 263 hours of untrimmed egocentric video with 87 fine-grained, multi-label action classes and 36% partially-overlapping action instances. This fills a genuine gap — existing egocentric OAD datasets are scarce or domain-limited (e.g., EPIC-KITCHENS is kitchen-only). The multi-label, temporally-dense annotation reflects real-world ambiguity. (Section 3)

3. **Substantial and consistent empirical gains.** On Ego-OAD with egocentric pretraining, COAD improves Top-5 Recall by **16.0%** on the in-stream (adaptation) split and **6.9%** on the out-of-stream (generalization) split relative to the pretrained-only baseline (Table 1). These gains hold across both egocentric and exocentric pretraining. The method consistently outperforms naive online fine-tuning (w/o COAD) on out-of-stream generalization.

4. **Clean ablation isolating each component's contribution.** Table 3 decomposes the method into state continuity, orthogonal gradient projection, and non-uniform loss, showing each contributes to the overall improvement. This gives a clear picture of what drives performance.

5. **Demonstrated effectiveness under sparse supervision.** Figure 3 shows that COAD improves performance even when labels are available only every 128 frames (roughly one label per 68 seconds), which is relevant for real-world deployment where per-frame annotations are unavailable.

## Weaknesses

### Major

1. **The IID training upper-bound comparison in Figure 4 cannot be verified from the paper as presented.** Section 5.4 states that "For comparison, we include an *IID Training* baseline...COAD steadily narrows the gap to this upper bound." However, the figure caption explicitly lists the curves shown as "COAD (blue), COAD w/o Orth. (green), COAD w/o Non-uniform loss (orange), and Pretrained Only (dashed red)" — none of which are the IID baseline. The central claim that COAD approaches offline performance is therefore based on an unverifiable visual comparison. The authors should either confirm that the IID curve is in the figure (and fix the caption) or, if it is absent, add it or remove the claim. This is not fatal to the paper's core contributions (the task, dataset, and Table 1 results stand independently), but it weakens a specific narrative claim.

2. **The paper's framing of personalization outpaces what the experiments actually measure.** The abstract and introduction claim COAD enables adaptation to "individual users' environments" and "personalized egocentric AI." However, the in-stream set aggregates videos from *many* users; there is no per-user analysis, no user-specific split, and no measurement of how quickly or well the model adapts to a *particular* user's recurring actions. The evaluation measures adaptation to a broader data distribution from the same domain, not to individual users. This gap between framing and evidence should be addressed either by adding a per-user experiment or by softening the personalization claims to match what is actually measured.

### Minor

3. **The streaming protocol for handling multiple videos is underspecified.** The in-stream set contains 1,177 separate videos. The paper describes COAD as operating on a "continuous video stream" but does not specify what happens at video boundaries — are the videos concatenated into one long stream (carrying the hidden state across unrelated scenes), or is the state reset between videos? Each choice has implications for the results and for reproducibility. This should be explicitly documented.

4. **Dataset construction choices are not fully justified.** The paper states that all three subsets (pretraining, in-stream, out-of-stream) "correspond to the original Ego4D MQ validation split." The much larger Ego4D MQ *training* split is not used — the pretraining set is only 186 videos. Why the training split was excluded and whether this choice affects task difficulty or representativeness is not discussed. A brief justification would be helpful.

5. **EPIC-KITCHENS results exhibit an unusual pattern that is not adequately explained.** In Table 2, the in-stream Noun mAP for all methods is ≈3.8–3.9, while the out-of-stream Noun mAP is 31–37. Performance on the adaptation stream is an order of magnitude *worse* than on unseen data, which is counterintuitive. The paper attributes this to "the fine-grained nature of the actions and annotations in EPIC-KITCHENS" without further analysis. If the in-stream data is particularly difficult or the annotation differs, this should be clarified; otherwise the effectiveness of adaptation on this dataset is unclear.

### Trivial

6. **Typo in contributions list.** "Countinuous Online Action Detection" (Section 1, bullet 1) and the one-time use of "CODA" instead of "COAD" (Section 4). These are minor but worth correcting.

## Nice-to-Haves

- The orthogonal gradient projection uses only the immediately preceding gradient. An analysis of whether projection against a longer gradient history changes behavior would strengthen the design justification (Section 4.5).
- The paper motivates COAD by resource constraints on wearable devices but reports no training-time or memory-footprint measurements. Even a rough comparison of per-step cost would help assess practical feasibility.
- The qualitative results (Figure 5) show only the top-1 prediction. Since the task is multi-label, probability maps or top-k outputs would be more informative.

## Removed Points

- **Multi-label annotation ambiguity as a weakness:** The paper explicitly acknowledges this issue (Section 3, "To mitigate this ambiguity and ensure more robust recognition, we manually grouped semantically similar free-form action descriptions into unified action classes") and describes its mitigation strategy. The critic's suggestion to report inter-annotator agreement is reasonable but not a required standard for a new dataset. *Removed because the issue is already acknowledged and addressed.*

- **State continuity in w/o COAD baseline:** The critic suggests w/o COAD may be unfairly disadvantaged if it resets the hidden state. However, w/o COAD is explicitly defined as standard fine-tuning using shuffled windows (following the offline training protocol of Section 4.3), which naturally resets state between windows. This is by design, not a flaw. *Removed because it reflects a misunderstanding of the baseline definition.*

- **Orthogonal gradient projection depth as a weakness:** The choice to project against only the consecutive gradient is taken from prior work (Han et al., 2025) and is a standard design decision. The critic's suggestion to analyze depth is reasonable but more of an extension than a weakness. *Demoted to Nice-to-have.*

- **Formatting/style issues (ICLR formatting, "CODA" typo):** The typo "Countinuous" and one "CODA" usage are genuine but trivial. The formatting concern about ICLR template is not evaluable. *Moved to Trivial.*

## Novel Insights

Beyond the paper's own contributions, the reviews surface the observation that the paper's framing of "personalization to individual users" is not well-supported by the aggregate in-stream/out-of-stream evaluation protocol — a common pattern in papers that introduce new continual learning tasks where the motivation is individual adaptation but the evaluation is at the population level. The discrepancy in EPIC-KITCHENS (in-stream mAP << out-of-stream mAP) is another notable phenomenon that could indicate a mismatch between the COAD streaming protocol and datasets with fine-grained class boundaries, which may be worth investigating as a general challenge for online adaptation in egocentric settings.

## Suggestions

1. **Fix Figure 4:** Ensure the IID Training baseline is actually plotted and listed in the caption, or if it cannot be plotted, remove the text claiming COAD "narrows the gap" and instead provide the quantitative comparison in a table.
2. **Clarify the streaming protocol:** Explicitly state what happens at video boundaries in the in-stream set (state reset vs. continuation) and discuss any implications.
3. **Address the personalization framing either by adding per-user experiments or adjusting the language throughout the paper to match the actual evaluation (which measures domain/stream adaptation, not individual-user personalization).
4. **Justify the dataset split choice:** Briefly explain why only the Ego4D MQ validation split was used and whether the training split could contribute additional value.
5. **Add computational cost analysis:** Even a simple comparison of per-step FLOPs or training time between COAD and the baselines would strengthen the practical motivation.

## Score and Decision

Based on calibration against human-reviewed anchors:

**Round 1 (Bracketing):** Weak anchors (high_score<3.5) averaged 1.67–3.00; the paper is clearly stronger than these. Middle anchors (3.5<score<7.5) averaged 3.75–5.71; the paper is comparable to the upper end of this band. Strong anchors (low_score>7.5) averaged 7.6–8.0; the paper is weaker than these. Initial bracket: **4.0–6.0**.

**Round 2 (Narrowing):** Queried for similar "new task + benchmark + baseline" papers in the 4.5–7.5 range. The closest anchors are *PARSE-Ego4D* (5.50, Reject — similar new-annotation+baseline contribution but less technically substantive) and *Anomalies are Streaming* (5.71, Reject — similar new-task+continual-learning+baseline contribution, with comparable gaps between claims and evaluation). The paper under review has a more technically significant task formulation and larger benchmark than PARSE-Ego4D, but shares similar issues of claim-evidence mismatch (personalization framing) with Anomalies are Streaming. The paper is stronger than *Large Scale Video Continual Learning* (4.50) which had more severe evaluation issues, but weaker than *Streaming Video QA* (6.50, Accept) which had a cleaner evaluation and more novel methodology.

**Final calibration:** The paper sits between the 4.50 and 5.71 anchors — its core contributions (task + benchmark) are solid and useful, but the notable gaps (IID baseline visualization, personalization framing, protocol underspecification) prevent it from reaching the 6+ level. I assign **5.0**, reflecting a borderline paper with meaningful contributions whose current evidential and framing issues would need to be resolved for acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>