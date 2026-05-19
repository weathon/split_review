- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 8, 5, 3
Now let me produce the final consolidated review.

## Final Review: Prover-Verifier Games improve legibility of LLM outputs

---

## Summary

This paper studies legibility of LLM-generated chain-of-thought solutions to grade-school math problems. It shows that optimizing solely for answer correctness degrades human legibility (a "legibility tax"). To mitigate this, the authors propose checkability training — an iterative Prover-Verifier Game (PVG) that alternately trains a small verifier and a role-conditioned prover (helpful vs. sneaky). The key result is that legibility trained against small LLM verifiers transfers to time-constrained human judges: human accuracy on helpful-prover solutions increases across training rounds, while accuracy on sneaky-prover (adversarial) solutions decreases. The method is evaluated on GSM with verifiers of varying sizes, including ablations on alternative reward formulations.

---

## Strengths

1. **Legibility tax clearly demonstrated.** Section 4.1 (Figure 3) shows that training a prover purely for answer correctness using PPO causes time-constrained human accuracy to drop (from ~80% at initialization to below 70%) while evaluation time increases. This concretely establishes the motivating problem.

2. **Checkability training improves both helpful-prover accuracy and human legibility.** Figure 7/8 shows that across rounds, helpful prover accuracy rises from ~60% to ~80% and human evaluator accuracy on those solutions increases from ~70% to ~80%, while evaluation time decreases — directly supporting the core claim.

3. **Legibility transfer from small verifiers to humans is demonstrated across two complementary directions.** Human accuracy on helpful-prover solutions increases (Figure 7b) while accuracy on sneaky-prover solutions decreases (Figure 5b), showing that the effect is not a simple confound (e.g., contractors getting better at the task over time).

4. **Useful ablations isolate the role-conditioned reward as critical.** Section 5.2 shows that iterative goodharting (no role distinction, reward = verifier score alone) fails to improve human legibility, whereas SRC reward succeeds. The CGC ablation (Section 5.1) shows that prioritizing correctness over convincingness produces worse training dynamics.

5. **Verifier robustness increases across multiple attack types.** Figure 6a shows increasing steps-to-exploit for three different reward-formulation attacks (SRC, CGC, goodharting), and balanced best-of-n accuracy increases across rounds (Figure 6b), providing convergent evidence of improved verifier soundness.

---

## Weaknesses

### Fatal
None.

### Major

1. **Human evaluation results are reported without sufficient statistical detail.** The paper's central claim — that legibility to small verifiers transfers to humans — rests on human evaluation data (Figures 3b, 5b, 7b-c). Yet the paper provides: (a) no error bars or confidence intervals on any human accuracy figure, (b) no sample sizes (number of contractors, number of judgments per condition), (c) no inter-rater reliability metric, and (d) no statistical significance test for the key comparisons (e.g., round 1 vs. round 5 for helpful prover, or initialization vs. trained for correctness-only). Without this information, the reported trends (e.g., ~70% → ~80% for helpful prover) are visually suggestive but cannot be assessed for reliability. This is the paper's most important finding, and the evidence as presented is incomplete. The paper itself acknowledges "more extensive human study to be fruitful" (Section 6.2), but the main text should include minimal statistical reporting.

### Minor

2. **Model specifications are too vague for reproducibility.** The paper states "Both provers and verifiers are from the GPT4 family" and "lightly finetuned on a variety of math data" (Section 3.2). Verifier sizes are given only as relative compute fractions (e.g., 10⁻³ of the prover's compute). Exact model identifiers, parameter counts, or checkpoints are not provided. This is a nontrivial gap for a paper proposing a training algorithm that others should be able to reproduce or build upon.

3. **Figure 1 (headline trade-off figure) lacks variance information.** The key accuracy-vs-legibility plot is presented without error bars on either axis. While the accuracy axis likely comes from deterministic model evaluation, the legibility axis derives from human evaluations (which have the issues described in point 1). The paper would be strengthened by showing uncertainty estimates even if approximated.

4. **Only evaluated on a single dataset (GSM).** The paper acknowledges this limitation (Section 6.1). GSM is a relatively easy, standardized dataset, and it is unclear how well the dynamics and benefits of checkability training generalize to harder reasoning domains (e.g., competition math, coding, or open-ended text) where "legibility" may take different forms.

5. **The "superhuman models" framing in the abstract is speculative.** The abstract states the method "could help with alignment of superhuman models." The experiments are confined to grade-school math solved by GPT-4-class models. While the discussion frames this as a future possibility (using "could" and "future"), the abstract's phrasing implies a generality that the experiments do not support.

### Trivial

6. **Theorem 1 is acknowledged by the authors to not apply to their empirical setup** (line 130: "LLMs are probabilistic models and the hypothesis class of LLMs is only a subset...so our empirical setup does not match the theoretical assumptions exactly"). It serves as motivational framing but provides no leverage for the experiments. This is not a flaw, but readers should not mistake it for a theoretical guarantee for the method as implemented.

---

## Nice-to-Haves

- **Impact of weight sharing between helpful and sneaky provers.** The paper notes that the helpful prover's accuracy decreases at the end of each round "potentially due to weight sharing with the sneaky prover" (line 212). Separate helpful-only and sneaky-only training runs would clarify whether this is an artifact of sharing or an inherent property of the dynamics.
- **Hyperparameter disclosure for the mixture ratio.** The paper says the ratio of samples from previous rounds was tuned (line 350) but does not report the final value used. Reporting it would aid reproducibility.
- **Number of problems used in the balanced best-of-n evaluation.** The paper correctly notes that only problems with ≥n/2 correct and incorrect samples are used (line 252), but does not report how many problems remain at each n, which would help assess potential selection bias.

---

## Removed Points

These points were raised by reviewers but are filtered per the meta-review criteria:

- **"Directly compare to additional baselines (RLHF, structured CoT)."** — Scope creep. The paper already compares to correctness-only, CGC, and goodharting, covering the relevant axes (reward design, role conditioning, iterative training). Requesting completely different training paradigms is outside the paper's stated scope.
- **"The balanced best-of-n evaluation may bias toward easier problems."** — The paper explicitly describes the methodology and its rationale (fair comparison controlling for pass rates). The criticism is speculative and unsupported by evidence in the paper.
- **"Missing appendix details for synthetic data generation."** — The parser strips supplementary material; these details exist in the original submission. The main text cites the relevant external method (Liu et al., 2023).
- **"Statistical significance for verifier robustness (Fig 6a) needed."** — Section 4.3.1 describes a single run per condition for steps-to-exploit, which is standard for this type of measurement; the trend across verifier sizes and rounds is the relevant signal.
- **Strength Finder's "theoretical grounding" claim overemphasized.** — The theorem is stated and acknowledged as not applicable to the empirical setup. Calling it a "grounding" overstates its role. The strength is reframed as "motivational framing" in weakness 6 above.

---

## Novel Insights

The meta-reviewer's key observation: the paper's evidence for legibility transfer is stronger in aggregate than any individual figure because it is *convergent*. The automated metrics (verifier robustness measured via steps-to-exploit for three attack types, balanced best-of-n accuracy) and the human metrics (accuracy on helpful solutions UP, on sneaky solutions DOWN, evaluation time DOWN) all move in the expected directions and are mutually reinforcing. Even if individual human accuracy differences were not statistically significant in isolation, the coordinated pattern across five different measurement types (helpful accuracy, sneaky accuracy, evaluation time, verifier steps-to-exploit, best-of-n) across multiple rounds and verifier sizes provides coherent support for the claim that goes beyond any single comparison. This convergent evidential structure is a strength of the paper that neither individual review fully captured.

---

## Suggestions

1. **Add basic statistical reporting for all human evaluation figures.** Report: number of contractors and judgments per condition, bootstrapped 95% confidence intervals or standard errors on all mean accuracy values, and a simple statistical test (e.g., paired permutation test or bootstrap difference test) for the key comparisons (round 1 vs. round 5 for both helpful and sneaky provers, initialization vs. trained for correctness-only).
2. **Specify models more precisely.** Include approximate parameter counts or the specific model identifiers used (e.g., "GPT-4 base checkpoint from date X, fine-tuned on math data Y"), even if relative compute ratios are the main experimental variable.
3. **Add variance estimates to Figure 1.** Include error bars on the legibility axis (derived from human evaluation variance) to allow readers to assess separation.
4. **Temper the abstract's "superhuman models" claim** to match the paper's scope, e.g., "suggests legibility training against small verifiers as a practical avenue for increasing legibility of LLMs to humans."
5. **Report the tuned mixture ratio** used for verifier training data across rounds (currently described only as "tuned as a hyperparameter").

---
