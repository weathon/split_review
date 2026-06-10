## Summary

This paper proposes replacing the standard Bradley-Terry (BT) model with the Bradley-Terry model with ties (BTT) for preference modeling in RLHF/DPO. The authors derive a closed-form expression for the bias in preference-strength measurement that arises when BT is fit to data generated under BTT (Theorem 2, Eq. 164), propose a bias-correction algorithm (Algorithm 1) that inverts this bias to recover the true preference strength from conventional datasets lacking ties, and evaluate BTT-based fine-tuning (TDPO) against DPO on synthetic preference datasets where LLMs (Llama-3-70B, Qwen2-72B) label ties in the HH-RLHF dataset.

## Strengths

- **Closed-form derivation of the bias from ignoring ties (Theorem 2, Eq. 164).** The paper proves analytically that fitting a BT model when the true preference distribution follows BTT yields a biased estimate Δr̂ = Δr* + log((2θ + (1+θ²)exp(-Δr*))/(1+θ² + 2θ exp(-Δr*))). This is a precise, monotonic expression whose sign opposes Δr* and whose absolute value is bounded. No prior RLHF work has derived this bias in closed form. The proof sketch is clear and the mathematical reasoning is sound.

- **Principled bias-correction algorithm (Algorithm 1, Section 4.3).** Because the mapping between Δr̂ and Δr* is one-to-one, the paper solves the nonlinear bias equation during training to recover the corrected preference strength. This is a theory-driven offset rather than an ad-hoc margin, and it connects naturally to existing methods (ODPO, adaptive margin) while providing a principled alternative.

- **Cross-validated experimental design with two LLMs.** The paper uses Llama-3-70B and Qwen2-72B in a crossed design (one labels ties, the other evaluates), reducing labeler-specific bias. The win-rate experiments (Figure 3) show TDPO's win rate increases monotonically with tie proportion, and the patterns are directionally consistent across both labeler-evaluator pairings.

## Weaknesses

### Major

- **No comparison against the most directly relevant baseline: ODPO with a constant offset.** The paper repeatedly states that its bias-correction method "can be viewed as a variant of DPO with an offset (ODPO)" (lines 45, 199, 238), yet it never runs the obvious comparison: standard ODPO with a tuned constant offset vs. the theory-derived offset. Without this baseline, the reported win rates (55.82%, 53.70% against DPO) could simply reflect the well-known benefit of adding *any* margin to DPO, not the superiority of the specific theoretically-derived offset. This is the single most critical gap in the experimental evaluation.

- **No statistical uncertainty reported for any experimental result.** Every result — test accuracies (Table 2), win rates (Table 3), ground-truth bias differences (Table 1), and win-rate curves (Figure 3) — is reported as a single point estimate with no confidence intervals, standard errors, or significance tests. With the HH-RLHF dataset containing over 160k samples, bootstrap or other resampling methods would be straightforward. Statements such as "significantly outperform" and "more than a 10% improvement" cannot be assessed without variance information.

- **The central motivating claim — that BTT improves reward learning for *human* preferences — is untested.** Every experiment uses LLMs (Llama-3-70B, Qwen2-72B) to simulate ties, not human annotators. The paper transparently acknowledges this limitation (lines 45, 291), but the gap between motivation and validation remains structural. The experiments show only that BTT better fits the preference patterns of these specific LLMs; whether this transfers to actual human annotators is an open question. The paper's title and framing imply applicability to human preferences, but the evidence does not reach this claim.

### Minor

- **The bias-correction algorithm treats θ as a tunable hyperparameter without sensitivity or transfer analysis.** Algorithm 1 takes θ as input and the bias formula depends on it. The paper selects θ=5 by maximizing test accuracy on Pythia-160M (Table 2) and reuses this value for all subsequent experiments. There is no analysis of: (a) what θ values are plausible for human preferences, (b) how misspecified θ degrades performance, or (c) whether θ=5 transfers to other model sizes or datasets. Since θ controls the assumed probability of ties, it is not a free parameter in the theory.

- **The ground-truth reward experiment (Section 5.1) reports only the *difference* in absolute bias between BT and BTT (0.0206–0.0353), not the absolute bias of either method.** If both methods have small absolute bias, the practical value of the difference is unclear. Reporting absolute values would clarify the practical significance.

- **The synthetic ties experiment (Section 5.3) does not control for total sample size or the number of non-tied samples as the tie ratio varies.** The paper varies the percentage of tied samples while "untied samples randomly selected," but does not state whether the total number of training samples is held constant. This confound could drive performance differences independently of the preference model used.

### Trivial

- The claim to be "the first to propose the use of BTT to model human preference" (line 49) is slightly overstated — BTT is a known model since Rao (1967). The novelty is in applying BTT to RLHF, which the paper adequately conveys elsewhere.
- The paper uses the term "ODPO methods" (line 238) to refer to its own bias-corrected DPO, which conflates the proposed method with the existing ODPO baseline that is never compared against.

## Nice-to-Haves

- A small-scale human annotation study (e.g., 500–1000 pairs labeled by humans for ties) would substantially strengthen the paper's claim that BTT improves reward learning for human preferences. Even a correlation analysis between LLM tie labels and human tie labels would be valuable.
- Sensitivity analysis showing how bias-correction performance varies as a function of misspecified θ (e.g., true θ=3 but algorithm uses θ=5).

## Removed Points

- *Criticism about "the empirical evaluation cannot support claims about human preferences" being fatal* — Demoted to Major. The paper explicitly acknowledges this limitation (lines 45, 291) and scopes its experiments to LLM-simulated data. The theoretical contribution (bias derivation) is independent of human data.
- *Criticism that "training on noise" at tie ratio 1.0 is a confound* — Removed. This is the expected behavior being demonstrated: BTT handles ties correctly while DPO treats random labels as signal. This supports rather than undermines the paper's thesis.
- *Criticism about missing related works* — Removed per instruction. The reviewer has no basis to assert missing works.
- *Criticism about Algorithm 1 adding computational overhead* — Removed. Trivial implementation detail not central to the paper's contribution.
- *Criticism about missing appendix/references* — Removed. Parser strips these from all papers.
- *Criticism about Pythia-160M being too small to generate text* — The paper already acknowledges this (line 239). Accuracy on reward prediction is a valid metric.
- *Pure formatting/style nitpicks and speculation about "not yet released" models* — Removed.
- *Strength Finder's generic/superficial strengths* — Removed. Only the concrete, evidenced strengths are retained above.

## Novel Insights

None beyond the paper's own contributions. The review inputs did not surface a genuinely novel synthesis that the paper itself does not provide.

## Suggestions

1. **Add ODPO as a baseline.** Tune a constant offset on the same validation data used to select θ. This is the single most informative comparison — it separates the effect of having *any* margin from the effect of having the *specific theoretically-derived* margin.
2. **Report uncertainty estimates** (confidence intervals via bootstrap or standard errors across seeds) for all experimental results.
3. **Report absolute bias values** for both BT and BTT in the ground-truth reward experiment, not just the difference.
4. **Add θ sensitivity analysis** showing performance as a function of misspecified θ (e.g., sweep θ from 1 to 10 and report test accuracy at each value).
5. **Include a human annotation pilot study** or at minimum correlate LLM tie labels with any available human judgment signal in the HH-RLHF dataset.

## Score and Decision

**Score:** The paper has a clear, mathematically sound theoretical contribution (the bias derivation) and a principled algorithm. However, the experimental validation has three significant gaps: (1) no comparison against the most relevant baseline (ODPO), (2) no statistical uncertainty reported anywhere, and (3) the central empirical claim about human preferences is supported only by LLM-simulated data. These gaps prevent strong acceptance at ICLR. The paper's strengths are real but do not compensate for the weaknesses in empirical validation.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>