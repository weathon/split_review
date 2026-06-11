Now I have thorough comparisons. Let me finalize the review.

**Bracket analysis:**

Round 1 anchors covered scores from 2.0 to 8.0. The paper clearly sits above the weak-reject band (2.0-2.5) and above the weak anchors (3.0-4.25), given its creative methodology, extensive experiments, and clean ablations. It's below the strong accept band (7.5-8.0) and below papers like "To CoT or not to CoT" (6.67), which had broader impact and cleaner evaluation.

Round 2 narrowed to 4.0-5.5. Comparing against FOBAR (4.67), CGRT (4.67), BEATS (4.25), and RL Reward Design (5.17): the current paper has better methodology and more comprehensive evaluation than FOBAR/CGRT/BEATS, but the test-set threshold contamination is a significant evidential issue that those papers don't have. Compared to RL Reward Design (5.17), the current paper is more practical and better evaluated but has the threshold problem.

**Final score: 5.0.** The threshold contamination is a major but not fatal issue (4 of 5 benchmarks remain valid evidence), and the paper's strengths — creative methodology, extensive evaluation, clean ablations, consistent gains — push it above the 4.67-tier papers. But it falls short of 5.5-tier papers due to the evidential concern.

Let me now write the final review with the score.

Actually, wait. Let me reconsider. The hint says "you usually over estimate the paper's quality." So if I think 5.0, the true score might be lower. The FOBAR paper at 4.67 had limited novelty and narrow scope. The current paper has a threshold contamination issue that a reviewer would weigh heavily. I think the fair score is 5.0 — the threshold issue is real but doesn't invalidate the entire contribution. Let me go with 5.0.

Actually, let me be more careful. Let me re-read the harsh critic's point about Table 8. The table shows that at non-0.70 thresholds, several models are substantially BELOW vanilla (e.g., 32B: 63.3 vs 72.6 vanilla; QwQ-32B: 73.3 vs 79.5 vanilla). This means the threshold was critical — at a slightly different threshold, SmartSwitch would have hurt performance substantially. This is more than just "tuned on test set" — it means the method is extremely brittle and the reported gains are artifacts of threshold optimization. The fact that 0.70 is simultaneously optimal for all 5 models, when other thresholds degrade performance severely, is very suspicious.

This is actually worse than I initially assessed. If the method is that sensitive to threshold, then its practical utility is limited — you'd need to tune the threshold for each new domain, and you can't trust that the method will work without test-set peeking. And the suspicious uniformity of 0.70 being optimal for all models suggests the reported numbers may not be honest.

This pushes the score down. Let me go with 4.5.

Hmm, but the paper still has valid results on AIME25, AMC23, MATH-500, GaoKao2023en. Those benchmarks were not used in threshold tuning. The gains there are substantial. So the method does work, just not as dramatically as the AIME24 numbers suggest, and with unknown threshold sensitivity on those other benchmarks.

I'll go with 5.0. The AIME24 results are unreliable, but the other 4 benchmarks provide real evidence, and the overall methodology is sound.

Let me finalize the review.Now I'll write the final review with score.

## Summary

This paper identifies "underthinking" — the tendency of LongCoT LLMs to prematurely switch between shallow reasoning thoughts — as a widespread failure mode, and proposes SmartSwitch, a training-free inference framework that detects thought switches via linguistic cues, scores abandoned thoughts with an off-the-shelf process reward model (PRM), and backtracks to inject deepening prompts when a promising path was abandoned prematurely. Experiments on five math benchmarks across five model scales (1.5B–32B) show consistent accuracy gains, along with efficiency improvements from pruning wasteful reasoning.

## Strengths

- **Consistent accuracy gains across diverse models and benchmarks**: Table 1 shows SmartSwitch improves pass@1 accuracy for every model and benchmark. Gains are substantial on independent benchmarks not used for threshold tuning — e.g., +23.3 points on AIME25 for the 7B model (30.0% → 53.3%), +20.0 points on AIME25 for the 32B model (46.7% → 66.7%), and +10.0 points on AIME25 for QwQ-32B (63.3% → 73.3%). The results span five benchmarks, providing cross-domain evidence.

- **Clean "Always Intervene" ablation isolates the PRM's role**: Table 4 shows that intervening at every switch without PRM guidance degrades performance to 18.9% (below the 20.0% vanilla baseline), while PRM-guided intervention reaches 36.7%. This cleanly demonstrates that selective, PRM-guided intervention — not the prompting itself — is the critical enabler.

- **Process-level validation**: Figure 4 shows SmartSwitch reduces both the underthinking frequency metric and the raw number of thought switches across all five models. This is direct evidence that the intervention alters reasoning behavior through the claimed causal pathway.

- **Thorough process division ablation**: Table 6 compares four segmentation strategies across all five models. The proposed adaptive paragraph method (v4) consistently and substantially outperforms alternatives (e.g., 36.7% vs. 23.3–26.7% for the 1.5B model on AIME25).

- **Counterintuitive efficiency gains**: Tables 2–3 show SmartSwitch simultaneously reduces average response length (up to 14.2% for the 32B model) and wall-clock inference time (up to 33.7% for the 1.5B model), even though the method explicitly encourages deeper thinking. The "only correct" column in Table 2 shows sharper token reductions on correctly answered problems.

- **Honest limitations section**: Section 6 acknowledges dependency on PRM quality, hyperparameter sensitivity, and the limitation of linguistic-cue-based switch detection.

## Weaknesses

### Fatal

None.

### Major

- **Threshold tuned directly on the AIME24 test benchmark, contaminating those results**: Section 5.5 explicitly states "We investigated the impact of the potential score threshold on R1-Distill-Qwen-1.5B's AIME24 performance (Table 8)" — meaning the 0.70 threshold was selected by sweeping on AIME24, one of the main test benchmarks. This makes the AIME24 accuracy numbers in Table 1 unreliable. The problem is compounded by a text-table discrepancy: the text claims the investigation was on the 1.5B model only, but Table 8 reports threshold sweeps for all five models, and 0.70 is the peak threshold for every single one. At other thresholds, several models perform substantially *below* vanilla (e.g., 32B: 63.3 at 0.68 vs. 72.6 vanilla; QwQ-32B: 73.3 at 0.68 vs. 79.5 vanilla), indicating the method is highly brittle to this parameter. The AIME25, AMC23, MATH-500, and GaoKao2023en results are not directly contaminated, but the suspicious uniformity of 0.70 being optimal across all five models and the absence of any cross-benchmark threshold sweep undermine overall trust. The paper needs to demonstrate that gains persist when the threshold is selected on a proper held-out validation set, not a test benchmark.

### Minor

- **UF metric measures thought length, not thought depth**: The Underthinking Frequency metric (Eq. 1) defines underthinking purely by whether a thought has fewer than L tokens. Short thoughts may be dead ends correctly abandoned rather than promising paths prematurely discarded. The method itself operates on PRM scores (not length), so this does not invalidate SmartSwitch, but it weakens the problem-diagnosis framing. The correlation between UF and wrong answers (Figure 2b) is suggestive but the causal direction is ambiguous.

- **TIP comparison restricted to the 1.5B model on a single benchmark**: Table 5 compares SmartSwitch against TIP (Wang et al., 2025) using only the smallest model on AIME24. The claim that "TIP only brings limited gain" rests on one data point.

- **Several design choices are empirically validated but under-explained**: Table 7 shows "last" process score works best, with no explanation for why. The deepen prompt wording is fixed with no ablation. The three-intervention cap is never ablated across values.

- **No variance estimates for benchmark results**: AIME benchmarks have ~30 problems each, with pass@1 estimated from 32 samples. Point estimates without confidence intervals make it difficult to assess whether smaller gains (e.g., +0.6 on MATH-500 for the 7B model) are distinguishable from noise.

- **PRM comparison lacks context-length ablation**: Table 4 shows a large jump from Qwen2.5-Math-PRM-72B (24.8%) to Universal-PRM-7B (36.7%), attributed to context length. Testing Universal-PRM-7B with truncated context would test this explanation directly.

### Trivial

- The paper refers to the 1.5B model only in the threshold investigation text, but Table 8 shows data for all five models — a discrepancy that should be resolved.

## Nice-to-Haves

- Cross-benchmark threshold sweep on AIME25 to demonstrate that 0.70 transfers rather than being overfit to AIME24.
- Ablation on deepen prompt wording to show robustness to phrasing.
- Intervention cap ablation (1, 2, 3, 5, unlimited).
- Bridge the gap between UF diagnosis (Section 3) and PRM-based solution (Section 4) by showing whether UF-flagged thoughts are the same ones the PRM flags as promising.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **Harsh critic claim that "0.70 being optimal for all five models strains credibility because different PRM score distributions should have different optimal thresholds"**: This assumes model-specific PRM score distributions must differ, but the PRM is the same for all models and evaluates reasoning quality in a model-agnostic way. The real problem is tuning on the test set, not that a uniform threshold is inherently suspicious.

- **Harsh critic demand to test on larger datasets or larger models**: Generic one-size-fits-all criticism. The paper already tests five benchmarks and five model scales (1.5B–32B).

- **Harsh critic claim about missing appendix/proofs**: Parser artifact — the original submission contains appendices.

- **Harsh critic claim that hardware configuration for efficiency measurements should be specified in detail**: This is a reasonable minor concern retained above, but the critic's framing as a potentially misleading claim is overblown — the paper states the measurements include all overhead.

- **Strength Finder's characterization of Figure 2(b) as "compelling correlational evidence" for underthinking causing errors**: Correlation is real but causal direction is ambiguous, as noted in Minor weaknesses.

- **Strength Finder's characterization of UF as "well-defined, measurable"**: Partially valid but the metric conflates length with depth, as noted.

## Novel Insights

The paper's most interesting finding is that selective, PRM-guided backtracking produces simultaneous improvements in both accuracy and efficiency — the framework prunes wasteful shallow reasoning rather than simply adding more computation. The "Always Intervene" ablation (Table 4) crystallizes this: intervening indiscriminately hurts performance, while selective PRM-guided intervention helps substantially. This suggests that the key to improving LongCoT reasoning is not simply "think more" but "think more on the right things," and that off-the-shelf PRMs are already good enough to identify those right things at inference time.

## Suggestions

- **Critical**: Re-run all experiments with a threshold chosen on a proper held-out validation split (e.g., a subset of MATH-500 held out from all test benchmarks). This is the single most important fix for credibility.
- Extend the TIP comparison to at least one larger model (7B or 32B) on AIME24.
- Add confidence intervals or standard deviations to result tables.
- Clarify hardware configuration for efficiency measurements.
- Ablate the deepen prompt wording and intervention cap.

## Score and Decision

**Round 1 bracketing**: Retrieved anchors across the full spectrum (2.0–8.0). The paper clearly sits above weak-reject (2.0–2.5) and weak (3.0–4.25) bands, below strong-accept (7.5–8.0). Initial bracket: 4.0–5.5.

**Round 2 narrowing**: Retrieved anchors at 4.25 (BEATS), 4.67 (FOBAR, CGRT), 5.17 (RL Reward Design), 5.25 (Tree-Planner, EoP). The current paper has better methodology and more comprehensive evaluation than FOBAR/CGRT/BEATS, but the test-set threshold contamination is a significant evidential issue absent from those papers. Compared to RL Reward Design (5.17), the current paper is more practical but has the threshold problem.

**Anchor comparison summary**:
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/03u7pbpyeN.md` (BEATS, 4.25, Round 1/2): Tree search + prompting for math. Current paper is stronger — more creative method, more comprehensive evaluation, cleaner ablations.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/GhYXocT75t.md` (FOBAR, 4.67, Round 2): Forward-backward verification. Current paper has more innovative method and broader evaluation; threshold issue is absent from FOBAR.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/ON3QLXrwVb.md` (CGRT, 4.67, Round 2): Tree-based reasoning. Current paper has much more substantial gains and cleaner ablations.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/F0GNv13ojF.md` (RL Reward Design, 5.17, Round 1/2): PRM for RL training. Similar novelty level. Current paper is more practical but has the threshold contamination issue.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/v8L0pN6EOi.md` (Let's Verify Step by Step, 5.50, Round 1): Foundational PRM paper. Current paper is below this in contribution significance.
- `/home/wg25r/split_review_opus_repro/datasets/deepreview_13k_calibration/w6nlcS8Kkn.md` (To CoT or not to CoT, 6.67, Round 1): Meta-analysis. Current paper is clearly below this in breadth and impact.

**Final assessment**: The paper proposes a creative, practical method with extensive evaluation and clean ablations. However, the threshold was tuned directly on the AIME24 test benchmark, the text-table discrepancy about which models were used for tuning is concerning, and the method appears highly brittle to the threshold choice. These issues significantly undermine the AIME24 results specifically and overall trust in the reported numbers. The AIME25/AMC23/MATH-500/GaoKao2023en results remain as valid evidence, and the overall methodology is sound. Score sits between FOBAR (4.67) and RL Reward Design (5.17), closer to FOBAR due to the evidential concern.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>