Now I have enough information to write the consolidated review. Let me compile it.

## Summary

This paper empirically investigates whether training language models to win debates (via self-play DPO) leads to more accurate evaluator judgments on a hidden-information reading comprehension task (QUALITY). The authors find a 4% absolute increase in judge accuracy for debate-trained models (p < 10⁻⁶), while equivalently trained non-adversarial consultancy models show no such improvement. The paper introduces novel consultancy baselines (ensembled and double consultancy), develops a continuous-reward DPO variant (DPO⁺), and analyzes learned argumentation strategies showing that debate models use more evidence and less repetition than consultants.

## Strengths

1. **First positive training-time result for debate in scalable oversight.** Prior work (Radhakrishnan, 2023) failed to find improvements from training models to debate; this paper provides the first evidence that training language models to win debates can improve judge accuracy (4% absolute, p < 10⁻⁶, Section 4.2, Figure 5). This directly addresses an important open question in the scalable oversight literature.

2. **Positive skill–accuracy relationship for debate but not for consultancy.** Judge accuracy rises with debater win rate, while for single, ensembled, and double consultancy the relationship is indistinguishable from noise (Figure 5, Section 4.2). Since neither debaters nor consultants are trained to maximize judge accuracy, this contrast isolates adversarial training structure as the likely driver of truth-seeking improvement.

3. **Novel consultancy baselines that decompose debate's advantage.** The introduction of ensembled and double consultancy (Section 2.3) provides a controlled decomposition of why debate outperforms simpler alternatives. Double consultancy (75% accuracy) nearly matches debate (77%) while still showing no positive skill–accuracy trend (Section 4.3), revealing that presenting both sides side-by-side accounts for much of the accuracy gain, but the *trend* with optimization is unique to adversarial training.

4. **Evidence that debate models learn more informative policies.** The fully-trained debate model uses 96% more quoted words than its SFT starting point, while the consultant uses 70% fewer quotes and becomes repetitive (98% of second-speech quotes are repeats, Section 4.4, Figure 6). The debate model's win rates transfer strongly to an untrained GPT-4o judge (Pearson r = 0.98) vs. only 0.51 for consultants, indicating debate encourages generally useful argumentation rather than judge-specific exploitation.

5. **Careful judge calibration and honest limitation discussion.** The paper trains a calibrated judge to address sycophancy confounds (Section 3.1) and is unusually transparent about its limitations: refutation plays no detectable role, results are confined to one domain, and the strongest baseline (double consultancy) closes most of the accuracy gap.

## Weaknesses

### Fatal

None.

### Major

1. **Double consultancy nearly matches debate in endpoint accuracy, complicating the narrative of what drives gains.** Double consultancy achieves 75% judge accuracy vs. 77% for debate (Section 4.3) using consultant models that are *worse* arguers by the paper's own metrics (repetitive, less evidence). The paper does not report whether this 2% gap is statistically significant. The paper's main argument that debate's advantage comes from adversarial training rests more on the *trend* (positive skill-accuracy for debate, flat for double consultancy) than on endpoint superiority, but the trend analysis itself lacks formal statistical testing (no regression with confidence intervals, no significance test for trend differences). Given that the paper identifies the three factors behind debate's success as (1) side-by-side comparison, (2) asymmetric evidence, and (3) discouraging exploitation (Section 5.1), and factors (1) and (2) are shared with double consultancy, the unique contribution of adversarial training (factor 3) rests on indirect evidence from policy analysis.

2. **No cross-evaluation between training regimes and evaluation formats.** The debate-trained models are never evaluated in the double consultancy setup (i.e., generating two separate consultancies without seeing the opponent's arguments), and conversely, consultant-trained models are never evaluated in a debate format. This makes it impossible to determine whether the observed policy differences (more quotes, less repetition) are causally produced by adversarial training or are epiphenomenal. If a debate-trained model evaluated in double consultancy also showed high judge accuracy, this would strengthen the claim; if not, the advantage would be attributable entirely to the evaluation format rather than the training objective.

3. **Results are confined to a single task, model size, and debate format.** The paper uses only QUALITY reading comprehension, Llama3-8B as the debater, a single finetuned GPT-4T judge, and a two-turn simultaneous debate format. The paper acknowledges this limitation, but it fundamentally constrains what can be concluded. Prior work (Kenton et al., 2024) found that debate's benefits vary across tasks, and Khan et al. (2024) found ambiguous results for stronger debaters. Without validation on at least one additional task or model scale, the title and abstract's framing of a general phenomenon is broader than the evidence supports.

### Minor

1. **Missing error bars / confidence intervals on key measurements.** The judge accuracy points in Figure 5 are shown without any uncertainty estimates. Given 433 test questions, the standard error for a ~77% accuracy is about 2%, so the headline 4% improvement is approximately two standard errors — significant but not overwhelming. Similarly, the Pearson correlations for transfer to GPT-4o (0.98 vs. 0.51) are reported without confidence intervals or significance tests. The paper does report a p-value for the endpoint comparison, but including error bars on all data points would substantially strengthen the presentation.

2. **The "positive trend" claim relies heavily on a two-point comparison (SFT → final DPO).** The scatter plot in Figure 5 shows considerable variation across intermediate checkpoints, and no formal trend analysis (e.g., regression of judge accuracy on win rate with standard errors) is provided. The win rate measure itself is derived from round-robin tournaments judged by the same judge, creating some circularity (models that learn to exploit judge idiosyncrasies score high on both metrics). The transfer to GPT-4o partially addresses this, but the robustness of the skill-accuracy trend would benefit from more rigorous statistical treatment.

3. **Limited discussion of the simultaneous debate format's limitations.** Since debaters' second speeches can only respond to the opponent's first speech (not to later arguments), the opportunity for sustained refutation is limited. The paper notes that refutation doesn't seem to matter (Section 4.3, Appendix G), but this may be an artifact of the format — a sequential or multi-turn format might yield different conclusions about the role of refutation.

### Trivial

None.

## Nice-to-Haves

- **Formal trend comparison test:** Report a regression of judge accuracy on win rate across all checkpoints (with standard errors) and a formal test of whether the slope differs between debate and consultancy.
- **Ablation of the SFT loss term** (απ_θ(y_w)) in the DPO⁺ objective to determine whether it is essential or whether continuous-reward cross-entropy alone suffices.
- **One additional task**, even a simple multiple-choice QA dataset without long-context, to help establish that the result is not an artifact of the QUALITY task structure.
- **A more detailed description of the branching rollout procedure** — how many branches per node, how the expected reward is computed, and the variance of the estimates.

## Removed Points

**Harsh Critic Weakness 1 (partial):** The claim that "the evidence for a monotonic positive skill-accuracy relationship is weaker than claimed" uses the word "monotonic" — the paper never claims monotonicity, only a "positive relationship." This is a misreading. However, the underlying point about lack of formal trend analysis is real and is preserved as a Minor weakness.

**Harsh Critic Weakness 1 (continued):** The critic asserts that "the win rate measure itself is derived from round-robin tournaments judged by the same judge, creating circularity." This is partially addressed by the GPT-4o transfer experiment (r=0.98), which shows the win rates are not idiosyncratic to the trained judge. The critic's stronger version of this criticism is therefore weakened.

**Harsh Critic's section notes about "separate learning rates for debate and consultancy without a clear rationale":** The paper provides a rationale: a lower learning rate was found to produce a more performant model in head-to-head debates (Section 3.2.2, Implementation Details). This is a standard hyperparameter tuning practice and not a weakness.

**Strength Finder strengths about "generic/important problem":** Dropped as generic. The paper's importance is self-evident from its topic and does not need to be restated as a strength.

**Strength Finder strength about "DPO⁺ variant leveraging continuous scores":** Preserved in spirit but downgraded — the concurrent work (Nvidia et al., 2024) proposed a very similar loss, and the DPO⁺ variant is not a major novelty claim of the paper.

## Novel Insights

The most interesting observation from the review synthesis is that the paper's own data tells a more nuanced story than the headline: while debate training *does* improve judge accuracy, the mechanism appears to be almost entirely about presenting both sides side-by-side (which double consultancy also does) rather than about adversarial dynamics or refutation. The unique contribution of adversarial training seems to be in *discouraging judge exploitation* during training — preventing the degeneration into repetition and sycophantic strategies that consultancy models exhibit. This suggests that the value of debate may not be in generating better arguments per se, but in providing a training signal that penalizes cheap persuasive strategies that work in the absence of opposition. The paper would be significantly strengthened by directly testing this hypothesis through cross-evaluation experiments.

## Suggestions

1. **Perform cross-evaluation:** Evaluate debate-trained models in the double consultancy setup (generating two separate consultancies without seeing the opponent). This is the single most informative experiment that could be added: if debate-trained models still yield higher judge accuracy in this setup, it would directly demonstrate that adversarial training produces better arguments independent of the evaluation format.

2. **Add error bars / bootstrap confidence intervals** to all data points in Figure 5 and to the reported Pearson correlations for GPT-4o transfer.

3. **Run a formal regression** of judge accuracy on win rate across all checkpoints, with separate slopes for debate and each consultancy variant, and report whether the slopes differ significantly.

## Score and Decision

### Calibration Anchors

**Round 1 (Bracketing):**
- Weak band (<3.5): licAR8FPTW (avg 3.17) — Evaluating Oversight Robustness; weaker experimental design, narrower contribution → current paper is clearly stronger
- Mid band (3.5–7.5): QAwaaLJNCk (avg 6.00) — Multiagent Debate for factuality; overclaimed novelty, straightforward prompting → current paper has more novelty but narrower scope; comparable quality
- Mid band (3.5–7.5): FQepisCUWu (avg 5.60) — ChatEval; similar scope limitations, accepted as poster → current paper is comparable
- Mid band (3.5–7.5): tCfvktlrHI (avg 4.75) — Self-play in non-zero-sum games; narrower framing → current paper is stronger
- Strong band (>7.5): UHPnqSTBPO (avg 8.00) — Provable guarantees for human agreement; fundamentally stronger theoretical contribution → current paper is weaker

**Round 2 (Narrowing, bracket: 5.0–6.5):**
- J4xLuCt2kg (avg 5.75) — Uncertainty in LLM evaluations; accepted poster, limited novelty, well-executed → current paper has stronger novelty, comparable execution
- h71cSd2loX (avg 5.50) — DPO with ties; rejected, limited novelty, no performance improvement → current paper is stronger
- H0qIWXXLUR (avg 6.00) — Learn Your Reference Model; accepted poster, clear improvement but incremental → current paper has broader significance but narrower experiments
- uIGnuyDSB9 (avg 6.00) — SeRA; accepted poster, solid incremental contribution → current paper is comparable

**Bracket:** Round 1 placed the paper between weak (~3) and strong (~8) anchors, narrowing to 5.0–6.5. Round 2 confirms: the paper is clearly stronger than rejected papers in the 4.5–5.5 range and comparable to accepted posters in the 5.5–6.0 range. The paper has genuine novelty (first training-time result) and careful design, but its narrow scope and the double consultancy finding that complicates the core narrative prevent it from being a strong accept. Compared to the anchors, the paper sits at the upper end of the mid-range — better than ChatEval (5.6) and the DPO ties paper (5.5), comparable to SeRA (6.0) and the Uncertainty paper (5.75).

**Final Score:** 6.0

**Decision:** Accept

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>