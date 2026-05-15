Now I have all the information needed to synthesize the final review.

## Summary

This paper investigates whether training language models (Llama3-8B) to win debates via self-play improves judge accuracy on a long-context reading comprehension task (QuALITY-hard). The authors use a finetuned GPT-4T judge, train debate and consultancy models with SFT followed by a modified DPO that uses continuous judge confidence (rather than binary preferences), and evaluate skill-accuracy trends. They report a 4% absolute increase in judge accuracy after debate training (p<10⁻⁶), find no such positive trend for consultancy baselines, and analyze learned policies to show debate models use more evidence and transfer better to an untrained GPT-4o judge.

## Strengths

- **First positive result for debate training.** Prior work (Radhakrishnan et al., 2023) failed to show that training models to debate improves judge accuracy. This paper demonstrates a statistically significant 4% increase (p<10⁻⁶) from the SFT baseline to the fully DPO-trained debate model, overcoming a key prior null result. The improvement is achieved without ground-truth supervision in the DPO phase.

- **Skill–accuracy relationship is absent for all three consultancy variants while present for debate.** The judge shows no accuracy improvement as consultant models are trained (Figure 3), despite the consultants becoming more persuasive. Even double consultancy (75% accuracy), which closes most of the gap to debate (77%), fails to exhibit a positive trend between consultant skill and judge accuracy. This isolates the adversarial structure of debate as a critical factor.

- **Debate training induces qualitatively different and plausibly better argumentation.** The fully-trained debate model uses 96% more quoted words than SFT, while the consultant uses 70% fewer. Debate-model win rates transfer near-perfectly to an untrained GPT-4o judge (Pearson r=0.98) vs. only 0.51 for consultancy, suggesting debate strategies are more generally convincing rather than judge-specific exploits.

- **Carefully designed consultancy baselines (ensembled and double) decompose debate's advantage.** By comparing single, ensembled, and double consultancy, the paper isolates contributions of asymmetric evidence, side-by-side comparison, and adversarial training pressure — enabling a mechanistic interpretation beyond a simple debate-vs-consultancy comparison.

## Weaknesses

### Fatal
None. The paper's core claim is supported by a statistically significant end-to-end result, and no single weakness invalidates the overall finding.

### Major

1. **Insufficient granularity to support a "trend" claim; no error bars.** The central claim that training models to win debates yields a positive skill–accuracy relationship relies on only three checkpoints (SFT, DPO iteration 1, DPO iteration 2). A trend through three points cannot be meaningfully established. The reported p-value (p<10⁻⁶) tests the end-to-end SFT-to-final-DPO difference, which is valid, but the paper goes beyond this to assert that "further optimization should yield more accurate outcomes" — an extrapolation that requires more intermediate measurements. Additionally, no error bars or confidence intervals are reported for judge accuracy at any checkpoint, making it impossible to assess whether the 4% increase is stable or within evaluation noise.

2. **Training–evaluation circularity only partially addressed.** The same finetuned GPT-4T judge provides both the DPO rewards during training and the accuracy evaluation. Debaters are explicitly trained to maximize confidence from this specific judge, so the observed accuracy increase could partly reflect the judge becoming more confidently aligned with debaters it trained, rather than genuinely better truth-discovery. The GPT-4o transfer experiment (Figure 4, right) partially mitigates this by showing high win-rate correlation (r=0.98), but it measures *win rates*, not *judge accuracy*. The paper does not report whether an untrained GPT-4o judge achieves higher accuracy when evaluating transcripts from stronger debate models — the direct test needed to rule out circularity.

### Minor

3. **Consultancy baselines not trained for the stronger evaluation protocols.** All consultancy models are trained exclusively for single consultancy (one-sided persuasion) but are evaluated on ensembled and double consultancy protocols. The paper then argues that consultancy lacks a positive skill–accuracy trend. This comparison is asymmetrical: we do not know whether training a model specifically for double consultancy (the closest analogue to debate, structurally) would produce a positive trend. The paper's claim about debate's unique advantage would be strengthened by this control.

4. **Reward variance from branching rollouts is unquantified.** The DPO reward function uses Monte Carlo estimates from branching rollouts (the expected judge confidence at leaves of the game tree). The variance of these estimates is not discussed. If variance is high, it could explain why only two DPO iterations are performed and whether training could be improved. This does not invalidate the results but is a methodological gap.

5. **Limited task scope acknowledged but unaddressed.** The paper tests only QuALITY-hard reading comprehension questions. Prior work (Kenton et al., 2024) found debate effectiveness is task-dependent. The authors acknowledge this limitation but do not provide any results on additional tasks to assess generality.

### Trivial
None.

## Nice-to-Haves

- Training a model specifically for double consultancy would strengthen the claim that debate's advantage comes from its adversarial nature rather than train–eval protocol match.
- Measuring GPT-4o judge accuracy (not just win rates) across debate training checkpoints would directly address the circularity concern.
- 5–6 evenly spaced training checkpoints with error bars would provide credible trend evidence.

## Removed Points

These points are flagged to be removed; treat them with caution:

- **"for the first time" overclaiming** — The paper is factually correct that prior training work (Radhakrishnan et al., 2023) failed to show this effect. The claim is not overclaiming.
- **"no requirement of ground truth supervision signal" misleading** — The DPO phase does not use ground truth, and the paper refers to the *gains* (SFT→DPO improvement), which indeed occur without ground truth. This is a reasonable claim in context.
- **"explicit refutation does not play a role" undercuts paper's motivation** — The paper explicitly discusses this finding (lines 223–229) and is upfront that refutation does not yet drive results. This is a honest finding, not an unacknowledged weakness.
- **"barely significant due to high variance" not acknowledged prominently enough** — The paper does acknowledge this (line 206). This is a presentation preference, not a substantive gap.
- **Vanilla DPO ablation relegated to appendix** — The appendix was stripped by the parser; it exists in the original submission. The main text reports win rates for vanilla DPO (67%–71%) vs. the proposed method.
- **Missing related works** — Cannot be verified without external sources.

## Novel Insights

The reviews together surface an interesting tension that the paper itself partially recognizes but does not fully resolve: the mechanisms that make debate effective in this setting are *not* the ones originally theorized (refutation; Irving et al., 2018). Instead, the decomposition into asymmetric evidence, side-by-side comparison, and adversarial training pressure suggests that what makes debate work may be more about forcing the judge to compare competing claims in context — a function that double consultancy can largely replicate — plus the adversarial training dynamic that discourages judge exploitation. This reframing is potentially more valuable than the modest 4% accuracy gain, because it points toward simpler oversight protocols (structured comparison without full debate) that might generalize better. However, the paper does not test this implication by training for double consultancy, which would be a natural follow-up.

## Suggestions

1. **Add more training checkpoints and error bars.** Generate at least 5–6 evenly spaced checkpoints for debate and consultancy and report bootstrap confidence intervals for judge accuracy. This would convert the "trend" from speculation to evidence.
2. **Report GPT-4o's judge accuracy directly.** Measure whether an untrained GPT-4o judge achieves higher accuracy on transcripts from stronger debate models. This is the cleanest test of whether debate training produces genuinely truth-tracking improvements rather than judge-specific adaptation.
3. **Train a consultant optimized for double consultancy.** This control would determine whether the positive skill–accuracy trend is uniquely attributable to debate's adversarial structure or simply to better train–eval protocol alignment.
4. **Quantify the variance in branching-rollout reward estimates** and discuss whether this limits training stability or the number of feasible DPO iterations.

## Score and Decision

The paper makes a genuine contribution: it is the first to show that training models for debate via self-play can improve judge accuracy, and the thoughtfully designed consultancy baselines provide mechanistic insight. However, the core evidential claims are weakened by only three training checkpoints without error bars, and the training–evaluation circularity is only partially addressed. These are real but not fatal limitations — the end-to-end significant result and policy analysis provide meaningful evidence. The paper merits acceptance with major revisions to strengthen the trend evidence and address the circularity concern.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>