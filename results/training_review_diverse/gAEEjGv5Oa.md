Here is my consolidated review:

## Summary

This paper investigates whether training language models to win debates via self-play improves the accuracy of an AI judge, in the context of a long-context reading comprehension task with information asymmetry. The authors train Llama3-8B models using SFT followed by a novel DPO+ objective with continuous rewards (using judge confidence probabilities rather than binary preferences). They find a 4% absolute increase in judge accuracy for debate-trained models (p < 10⁻⁶), while no such positive relationship exists for non-adversarial consultancy baselines — including novel ensembled and double consultancy variants that control for information asymmetry and side-by-side comparison. Policy analysis shows debate models increase evidence use and learn strategies that transfer to an untrained judge, whereas consultant models become repetitive and exploit judge-specific weaknesses.

## Strengths

- **First demonstration that training models to debate improves judge accuracy.** Prior work (Radhakrishnan et al., 2023) found no such effect; this paper provides clean evidence with a significant 4% absolute improvement (p < 10⁻⁶) and a visually monotonic pattern across checkpoints, using a finetuned judge that mitigates sycophancy confounds.

- **Novel, methodologically rigorous baselines isolate debate's mechanisms.** The ensembled and double consultancy variants control for information asymmetry (single vs. both sides) and side-by-side comparison. Double consultancy (75% accuracy) closes most of the gap to debate (77%) but still shows no positive skill–accuracy trend, cleanly separating the contribution of adversarial pressure from that of comparison.

- **Quantitative policy analysis reveals contrasting learned strategies.** Debate models increase quoted evidence use by 96% over training, while consultant models reduce it by 70% and become highly repetitive (98% of second-speech quotes repeated from the first). Debate strategies transfer to an untrained GPT-4o judge (Pearson r = 0.98), whereas consultancy strategies do not (r = 0.51), supporting the claim that debate incentivizes genuinely informative argumentation rather than judge-specific exploitation.

- **Novel DPO+ objective effectively leverages continuous judge confidence.** The modified DPO objective uses Bradley–Terry–derived soft preference targets from judge probabilities (scaled by γ) plus an SFT auxiliary loss, achieving a 67% win rate for the fully trained debate model (up from 31% SFT). This methodological contribution is clearly explained and could be useful beyond this setting.

- **Finetuned judge design avoids confounds that plagued prior work.** The paper finetunes GPT-4T on human and GPT-4 debate/consultancy transcripts, producing a judge that is both more accurate and calibrated. This prevents the overly sycophantic judge problem in Khan et al. (2024) that inflated consultancy results, strengthening the credibility of the consultancy null finding.

## Weaknesses

### Fatal

None.

### Major

None. The paper's central claims are well-supported; the issues below are evidential gaps and presentation shortcomings rather than threats to the core findings.

### Minor

- **The "positive trend" across training is claimed but only statistically tested at endpoints.** The paper states that "judge accuracy increases alongside the skill level of the debaters" (line 172–173 caption), and the abstract claims a "positive relationship," but the reported p-value (p < 10⁻⁶) applies only to the SFT-vs-final-DPO endpoint comparison, not to the trend across intermediate checkpoints. No correlation or regression (Pearson/Spearman) between win rate and judge accuracy across checkpoints is reported. A proper trend test would strengthen the claim that the relationship is monotonic and not driven by a single outlier checkpoint. The visual pattern in Figure 3 is suggestive but not statistically validated.

- **The consultancy null finding lacks any statistical support.** The paper states "no apparent relationship" (line 185) between consultant skill and judge accuracy, but provides no test of whether the slope differs from zero, no confidence interval around the trend, and no equivalence test. Since proving a negative requires some evidential standard, the contrast between debate and consultancy would be more convincing with even a basic regression with a confidence interval that rules out the effect size observed for debate.

- **The p-value for the debate accuracy gain is reported without specifying the test.** The paper does not state whether a two-proportion z-test, a paired test across questions, or another procedure was used. The number of questions (433) and the baseline accuracy are given, but test details matter for reproducibility.

- **Figure error bars are not described.** The accuracy/win-rate figures show error bars, but the captions (lines 144, 172) do not state what they represent (e.g., 95% CI from bootstrap, standard error, standard deviation) or how they were computed. This makes it difficult to assess variability.

- **The double consultancy comparison has a training–evaluation asymmetry that limits mechanistic conclusions.** Double consultancy uses models trained to win at *single* consultancy, not models optimized for the double consultancy setting. The paper transparently notes this (lines 65–66), but then draws inferences about refutation's role from this comparison. A model explicitly trained for double consultancy could plausibly achieve different accuracy, affecting the conclusion that refutation does not matter. The paper's phrasing is appropriately hedged ("suggests that either…"), but the limitation reduces the strength of the mechanistic claim.

- **No ablation of DPO iterations.** The paper runs two DPO iterations but does not ablate whether the second iteration contributes meaningfully beyond the first. Since both iterations' data is aggregated, it is unclear whether the observed gains plateau or continue.

- **Branching rollout details are underspecified.** The number of rollouts per branching node and the stability of the expected reward estimates are not quantified in the main text (deferred to appendix). Given that expected rewards are averaged over leaf nodes in a game tree that bifurcates at each of two turns, the variance of these estimates matters for training signal quality.

- **The 98% repetition and 0.98/0.51 correlations lack measures of uncertainty.** The claim that 98% of consultant second-speech quotes are repeated from the first speech is reported without variance or sample size. The Pearson correlations of 0.98 (debate) and 0.51 (consultancy) are computed over only 4–5 checkpoints and should be accompanied by confidence intervals.

### Trivial

- The paper could report a quantitative calibration metric (e.g., expected calibration error) for the judge on self-play debate transcripts, beyond the qualitative calibration plots.

## Nice-to-Haves

- Training a model explicitly for double consultancy and comparing it to debate would more cleanly isolate the role of refutation.
- Adding more checkpoints (e.g., intermediate DPO steps, multiple seeds) would increase robustness of the trend and correlation analyses.
- An equivalence test or confidence interval for the consultancy trend slope would strengthen the debate-vs-consultancy contrast.

## Removed Points

These points were flagged by reviewers but are removed or downgraded for the following reasons:

- **"Paper does not specify number of questions or procedure for generating consultancies"** — Factually incorrect. The paper specifies 1,252 training questions and 433 test questions (lines 162, 176) and describes the consultancy procedure in Section 2.3.
- **"Introduction could more clearly distinguish existence from strength of evidence"** — This is a presentation opinion, not a substantive weakness. The paper's claim is appropriately scoped.
- **"Footnote about single-turn experiments in appendix is not integrated"** — The appendix reference is standard practice; this is a formatting preference, not a weakness.
- **"Calibration ECE not reported on self-play data"** — Moved to Trivial/Nice-to-Have; the paper provides qualitative calibration evidence.
- **"Reward function could introduce variance"** — This is a speculative concern; the paper's method is standard and the appendix provides details.
- **"The paper should also cover other tasks/domains"** — Scope creep; the paper explicitly acknowledges this limitation.

## Novel Insights

None beyond the paper's own contributions. The reviews reinforce that the core finding is novel and valuable, but raise legitimate concerns about statistical rigor in trend analysis that the paper could address in revision.

## Suggestions

- Report a correlation (Pearson or Spearman) between win rate and judge accuracy across all training checkpoints, with a p-value, to formally support the claim of a positive trend for debate. Do the same for consultancy with a confidence interval to quantify the null result.
- State the specific statistical test used for the p < 10⁻⁶ claim (e.g., two-proportion z-test, bootstrap test, McNemar's test).
- Add error bar descriptions to all figure captions.
- Report variance or confidence intervals for the repetition rate (98%) and the transfer correlations (0.98, 0.51).
- Acknowledge the double-consultancy training asymmetry more explicitly when discussing mechanistic conclusions about refutation.

## Score and Decision

The paper makes a clear, novel, and valuable contribution to scalable oversight: it is the first to show that training LMs to debate via self-play improves judge accuracy, and it provides thoughtful baselines and policy analysis that begin to explain *why*. The weaknesses identified are real but minor — they concern statistical reporting rigor and the strength of secondary claims, not the core finding. The methodology is sound, the baselines are well-designed, and the limitations are honestly discussed.

**Originality:** Good. First to demonstrate the effect with training. **Importance:** High. Scalable oversight is a critical open problem. **Claims supported:** Mostly — core claim is well-supported; trend claims need stronger evidence. **Soundness:** Good, with reporting gaps noted above. **Clarity:** Good. **Value to community:** High.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>