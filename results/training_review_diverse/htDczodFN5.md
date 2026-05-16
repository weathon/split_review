Now I have a thorough understanding of the paper. Let me write the consolidated review.

---

## Summary

This paper investigates the pre-training dynamics of in-context learning (ICL) through the lens of two sub-abilities: task recognition (TR) and task learning (TL). It proposes metrics to quantify competition between TR and TL, finds that this competition exists across 8 LLMs and is negatively correlated (Pearson r = −0.591) with ICL performance, analyzes how model size, dataset size, and data curriculum affect competition, and proposes an adaptive ensemble method that fuses TR-proficient and TL-proficient checkpoints at inference.

## Strengths

1. **First quantitative operationalization of competition between TR and TL during pre-training.** The paper defines and measures competition (occurrence rate C_i^h, intensity C_i^s, cumulative evolution R_i) and demonstrates that it is a widespread phenomenon across all 8 examined LLMs (Figure 2), with some models showing competition in over half of training steps. This provides a concrete measurement framework for studying ICL emergence.

2. **Negative correlation between competition intensity and ICL performance across multiple model families.** Using Pearson correlation across 8 models, the paper reports r = −0.591 between average competition intensity and final ICL accuracy (Figure 4). While not "strong" in the strictest sense, this is the first quantitative evidence linking competition to ICL outcomes and provides a plausible target for optimization.

3. **Well-controlled model-size analysis within the Pythia suite.** The analysis of model size (Section 3.3.1) uses the Pythia family, which shares architecture, data, and training hyperparameters. The finding that larger models exhibit competition earlier but with lower average intensity following a power-law trend (Figure 6) is a genuine insight backed by a controlled experimental design. The exception of Pythia-1B is honestly reported.

4. **Adaptive ensemble method with ablation support.** The proposed ensemble (Section 4) selects TR-best and TL-best checkpoints and weights them by accuracy-above-random. Ablation studies confirm that both checkpoint selection and adaptive weighting contribute to performance gains (Tables 1–2, referenced in text). The result that two smaller models (e.g., Pythia-1B + Pythia-2.8B) can outperform a single larger model (Pythia-6.9B) on several datasets is noteworthy.

## Weaknesses

### Fatal

None.

### Major

1. **Factor analyses for dataset size and data curriculum are confounded across model families.** The model-size analysis within Pythia is well-controlled, but the dataset-size (Section 3.3.2) and curriculum (Section 3.3.3) comparisons draw conclusions from cross-family comparisons. For dataset size: Pythia-2.8B vs. MiniCPM-2B, and Pythia-6.9B vs. Amber-7B vs. OLMo-7B differ in architecture, data composition, tokenizer, and hyperparameters — not just dataset size. For curriculum: MiniCPM-2B vs. Pythia-2.8B and CrystalCoder-7B vs. Amber-7B have similar confounds. The paper's claims that "scaling dataset size postpones competition" (line 395) and that specific curricula adjust competition (Sections 3.3.3) are therefore not adequately supported. The paper should either restrict these conclusions to correlational observations with explicit caveats, or run controlled ablations (e.g., training Pythia-410M variants on systematically varied data sizes). This is the most significant weakness because it weakens the paper's prescriptive claims about regulating competition through pre-training choices.

2. **Ensemble checkpoint selection is data-dependent.** The paper selects checkpoints with the best TR/TL performance "for the required ability" (line 501) using the same datasets on which the ensemble is evaluated. There is no mention of a held-out validation set for checkpoint selection — the only mention of a "development set" (line 511) is inside an `\ignore` block and not part of the active paper. This means the checkpoints are optimized for the evaluation tasks themselves, potentially inflating results through selection bias. The ablation (replacing best with random checkpoints) partially mitigates this concern, but the paper should clarify whether the tasks used for checkpoint selection are disjoint from those reported for final evaluation, or clearly state the limitation if they are not.

3. **Non-monotonic trend in dataset-size analysis is not discussed.** The paper claims "the evolving curve keeps moving to the right with the increasing of dataset size" (line 394) for both model sets. However, in the 7B set, Amber-7B (1T tokens) appears right-shifted relative to Pythia-6.9B (300B tokens), but OLMo-7B (3T tokens) appears left-shifted relative to Amber-7B (as noted by the reviewer — this is a specific factual claim about what Figure 5 shows). If this is correct, the trend is non-monotonic, contradicting the stated conclusion. The paper must either correct the claim or explain the non-monotonicity.

### Minor

1. **The "stable–rise" pattern is described qualitatively without statistical characterization.** The claim that competition exhibits a "stable–rise" pattern (line 304) is illustrated for only two models (MiniCPM-2B and Amber-7B) with no statistical test (e.g., phase-wise distribution comparison, autocorrelation). Generalizability across the full model set is unclear.

2. **Threshold ε = 0.01 has no sensitivity analysis.** The noise filter in Eq. (5) uses ε = 0.01. It is plausible but arbitrary. No analysis shows whether key findings (correlation with ICL, factor trends) are robust to different ε values (e.g., 0.005, 0.02, 0.05).

3. **The "strong negative correlation" claim slightly overstates r = −0.591.** With n = 8 models, a Pearson coefficient of −0.591 represents a moderate correlation, not a strong one. The paper also does not report confidence intervals or bootstrapped uncertainty for this value. Given the small sample, the correlation could be heavily influenced by individual data points.

4. **No task-level analysis of competition patterns.** The paper averages across 16 heterogeneous tasks (sentiment, NLI, toxicity, topic classification). Competition dynamics likely differ across task types, and averaging may obscure important structure. A breakdown by task category would strengthen the analysis.

5. **Inference cost of the ensemble is not discussed.** The ensemble requires two forward passes per example (one for the TR-best checkpoint, one for the TL-best checkpoint). While the paper correctly states parameter counts, it does not discuss the inference FLOPs or latency trade-off. This information would help readers assess the practical value of the method.

6. **Checkpoint sampling resolution (16 + 1) is coarse.** With 16 uniformly spaced checkpoints, competition concentrated between sampled steps could be missed. The paper should discuss how this might affect the cumulative intensity curves (R_i).

### Trivial

- The "first time" claim in the contributions (line 73) is reasonable for the specific TR/TL competition framing, but the broader observation of ability trade-offs during training has precedent in the multi-task learning literature. A slightly more measured characterization would be appropriate.

## Nice-to-Haves

- A small-scale causal intervention experiment (e.g., continuing training from a high-competition checkpoint with a penalty on opposite-direction TR/TL changes) would significantly strengthen the claim that competition affects ICL outcomes, but such an experiment is beyond the scope of a primarily observational/descriptive paper.
- Reporting the correlation with confidence intervals bootstrapped over the 8 models would clarify uncertainty.
- A task-category breakdown of competition patterns.
- Sensitivity analysis for the ε threshold.

## Removed Points

- **Competition metric "conflates magnitude and direction" critique.** The reviewer's example (ΔTR=−0.002, ΔTL=+0.001 giving C_i^s=2) is factually incorrect — these values fall below the ε=0.01 threshold and would yield C_i^s=0. The broader point (the ratio metric does not capture absolute swing magnitude) is a defensible design choice, not a flaw: the metric explicitly measures the trade-off rate ("decrease per unit increase"), which has a clear interpretation. Kept as a minor note at most.
- **"Correlation ≠ causation" as a structural weakness.** The paper uses hedging language throughout ("suggests," "could be crucial") and does not claim a causal relationship. This is a standard caveat that applies to most correlational studies; singling it out as a "critical issue" is overstated. The paper's claims are appropriately qualified.
- **"Model-size analysis is confounded" claim.** The Pythia suite is specifically designed to control for architecture and data while varying size. The paper explicitly states this (lines 365–366). This criticism is factually wrong about the model-size analysis.
- **"Two stages of training" pattern noted as novel.** The reviewer's claim that "similar patterns have been observed in other contexts" is vague and unsupported by specific citations. The paper's specific decomposition into TR/TL competition during pre-training is novel.

## Novel Insights

The reviews surface one genuinely useful observation that goes beyond the paper's own framing: the competition metric C_i^s measures trade-off *rate* (how much of one ability is sacrificed per unit gain of the other), not trade-off *magnitude*. The paper's framing treats "intensity" as interchangeable with either notion, but the two could behave differently — a model with small, frequent, high-ratio competition events might have a different ICL profile from one with rare, large-magnitude, symmetrical competition events. Disentangling these two aspects (rate vs. magnitude) could be a productive direction for future work. Beyond this, the reviews do not contribute additional novel insights beyond what the paper already provides.

## Suggestions

1. **For the main empirical claim:** Acknowledge that the dataset-size and curriculum analyses are cross-family comparisons with confounds, and either (a) reframe them as case studies/suggestive evidence, or (b) run controlled ablations on a small Pythia variant with systematically varied data sizes. This is the single change that would most improve the paper.

2. **For the ensemble method:** Clarify whether checkpoint selection uses a held-out subset of tasks or the same tasks reported for evaluation. If the latter, state this as a limitation and discuss potential over-optimism.

3. **Re-examine the dataset-size trend for the 7B models:** Verify whether OLMo-7B is indeed left of Amber-7B in the competition evolution curves. If so, explain the non-monotonicity or soften the monotonic claim.

4. **Add confidence intervals or bootstrapped estimates** for the Pearson correlation coefficient between competition intensity and ICL performance (Figure 4).

5. **Briefly note inference cost** (two forward passes) when presenting the ensemble results.

## Score and Decision

The paper makes a genuine empirical contribution by operationalizing competition between TR and TL during pre-training and demonstrating its correlation with ICL outcomes. The core observation is well-supported. However, the secondary analyses of pre-training factors (dataset size, curriculum) are weakened by confounded cross-family comparisons, and the ensemble evaluation has a data-dependency concern that is not adequately addressed. The paper would benefit from either controlled experiments or more cautious framing of these weaker claims. With revisions to address the confounds and clarify the evaluation protocol, the paper could be a solid contribution.

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>