I have thoroughly verified all claims against the paper. Here is my consolidated review.

---

## Summary

This paper investigates why autoregressive language models underperform on structured numerical data, using quantum chemistry property prediction (QM9) as a motivating case study. It formulates and tests five hypotheses (conditional vs. unconditional modeling, causal masking, lack of symmetries, poor tokenization, insufficient pretraining) by training hundreds of models on building-block tasks from linear algebra and 3D structure computation. The central positive finding is a strong log-linear correlation between invariance error and predictive error (Figure 3), suggesting that capturing symmetries is a key bottleneck. The paper also compares small from-scratch LMs against fine-tuned LLaMA3.1-8B and evaluates continuous tokenization (xVal) on the building-block tasks.

## Strengths

1. **Systematically tests and rules out multiple plausible hypotheses.** The paper formulates five specific hypotheses (Sections 6–10) and provides targeted experiments for each. It convincingly shows that causal masking (encoder-decoder vs. decoder-only, digit reversal) and conditional vs. unconditional modeling are not the primary bottlenecks — clean null results that narrow the space of explanations.

2. **Identifies invariance as a strong correlate of predictive performance.** Figure 3 shows a clear log-linear relationship between invariance error and task error across hundreds of trained models varying in size, architecture, and tokenization. This goes beyond prior speculation (Charton 2021, Zhou et al. 2023) by providing quantitative evidence that symmetry handling is more predictive of performance than causal masking or tokenization choice. The paper consistently frames this as a *correlation*, not causation.

3. **Clean ablation of continuous vs. discrete tokenization via xVal.** The paper not only compares digit, 3-digit chunk, and xVal tokenization (Figure 4), but also ablates continuous input and continuous output components separately (Figure 6, left). This shows that both components contribute to xVal's advantage and that discrete methods require larger models to learn invariance — a specific and actionable finding.

4. **The building-block decomposition methodology is well-designed.** Breaking down DFT computations into matrix operations, distance calculations, and potential energy estimation (Section 4) provides a controlled testbed that connects toy problems to a practical domain. This enables targeted attribution of performance gaps to specific computational subroutines.

## Weaknesses

### Fatal
None.

### Major

1. **The pretraining comparison is confounded and does not support the strong conclusion drawn from it.** Section 10 compares small LMs trained from scratch for ~100 epochs against LLaMA3.1-8B fine-tuned for 1 epoch with LoRA — differing in model size (two orders of magnitude), training budget (1–2 orders of magnitude difference in gradient steps), and optimization procedure. The paper acknowledges this discrepancy (line 189: "1-2 orders of magnitude fewer gradient steps") but nonetheless concludes that "text pretraining is surprisingly unhelpful" (abstract) and "text-pretrained models perform worse on every task except matrix products" (Figure 6 caption). Because training compute, gradient steps, and optimization are not controlled, the experiment does not isolate the effect of pretraining. It shows that a large model fine-tuned briefly with LoRA underperforms a small model trained extensively from scratch — which is informative about the *combination* of budget and approach, but not about the value of pretraining itself. This undermines one of the paper's four advertised key findings.

2. **xVal, the paper's best-performing tokenization method, is never evaluated on the real QM9 tasks.** The paper frames quantum chemistry as its central case study (abstract: "using quantum chemistry simulations as a case study") and presents Table 1 showing that LMs underperform on QM9 HOMO prediction. xVal outperforms discrete tokenization on the building-block tasks (Figure 4), yet it is absent from Table 4 (which compares only discrete-tokenized LMs and EGNNs on energy/HOMO prediction). Testing xVal on QM9 would be the most direct way to validate whether the building-block insights about continuous tokenization and invariance transfer to the practical target. Without this experiment, the bridge between the building-block analysis and the QM9 case study remains incompletely demonstrated.

### Minor

3. **The invariance-evidence is correlational and not tested causally.** The paper's central positive finding is a correlation between invariance error and predictive error (Figure 3, abstract: "a strong correlation"). The paper frames invariance as a bottleneck (Hypothesis 3: "Lack of symmetries") but never performs an intervention that would test whether invariance *causes* better performance — e.g., averaging predictions over random permutations/rotations at inference time to enforce invariance in an LM, or removing symmetries from the task to check whether the LM gap shrinks. The correlation is genuinely interesting and well-documented, but the causal claim remains suggestive. The paper's language is mostly careful ("correlation," "connection"), though the discussion claims that the importance of invariances "hold[s] up to scrutiny" (line 196), which overstates what correlational evidence can support. A single causal intervention would substantially strengthen the paper's main claim.

### Trivial

4. The quantized numerical operation baselines (16-bit, 20-bit) are used in Figures 2–3 but not carried through to Table 4, making cross-figure comparisons less direct. This is a minor presentation inconsistency.

5. The "theoretical limitations" paragraph (Section 4, lines 64–66) discusses serial computation depth and memory bottlenecks as conceptual framing, but is never operationalized into experiments. This is not a weakness of the paper's experiments per se (the paragraph is explicitly presented as background), but the framing raises expectations that are not fulfilled.

## Nice-to-Haves

- **Causal invariance test:** Enforcing invariance at inference time by averaging predictions over 10–100 random permutations/rotations would directly test whether invariance is a causal bottleneck or merely a correlate.
- **xVal on QM9:** Evaluating xVal on the HOMO/energy tasks from Table 4 would validate whether building-block improvements transfer to the target problem.
- **Controlled pretraining comparison:** Either training the small LM for fewer steps or fine-tuning LLaMA for more steps (matching gradient steps or compute budget) would isolate the effect of pretraining.

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The invariance correlation is overinterpreted as explanatory"** — Partially overblown. The paper consistently uses "correlation" language in the abstract and main text (abstract line 4, line 14, Figure 3 caption). Some discussion language is slightly stronger ("hold up to scrutiny") but the overall framing is correlational. The core criticism (no causal test) is kept as Minor weakness #3 above; the claim of "overinterpretation" as a fatal flaw is removed as inaccurate.
- **"The paper claims to train thousands of language models but..."** — A pure nitpick. The claimed scale is reasonable for the number of experimental conditions varied.
- **"The theoretical limitations paragraph is not operationalized"** — The paper clearly distinguishes theoretical limits from practical challenges (line 66: "reasoning about what solutions tend to be learned by a particular architecture is often more important than fundamental constraints"). This is conceptual framing, not a testable hypothesis.
- **Strength 2 from Strength Finder ("Demonstrates that text pretraining often harms performance")** — Conflicts with verified Major weakness #1. The experiment is confounded, so it does not cleanly demonstrate this claim. Moved here.

## Novel Insights

The most insightful observation from this review process is that the paper's greatest strength (systematic hypothesis testing that rules out several common explanations) and its greatest weakness (confounded pretraining comparison combined with missing xVal-on-QM9 results) pull in opposite directions: the paper is very good at telling us what *doesn't* explain LM failures but significantly weaker at establishing what *does*, despite the invariance correlation being genuinely suggestive. The pretraining comparison is particularly frustrating because the paper acknowledges its own confound but then ignores it when drawing conclusions — a rare case where transparency about a limitation does not prevent overclaiming.

## Suggestions

1. Either add a causal invariance test (e.g., inference-time averaging over symmetries) or explicitly reframe the invariance claim as a correlational observation rather than an explanation.
2. Evaluate xVal on at least one QM9 task (HOMO or energy) to validate the building-block-to-real-problem transfer.
3. Either control the pretraining comparison (matching gradient steps or compute) or substantially temper the conclusion — e.g., reframe it as "fine-tuning large pretrained models with limited task-specific training is surprisingly ineffective" rather than "text pretraining is unhelpful."

## Score and Decision

MY FINAL SCORE: <pineapple>5.5</pineapple>
MY FINAL DECISION: <orange>Reject</orange>