## Summary

This paper proposes Power Sampling, an inference-time MCMC procedure that targets the power distribution \(p^\alpha\) of a base language model, as a training-free alternative to RL posttraining (specifically GRPO). The method progressively builds sequences via blockwise Metropolis-Hastings, using the base model's own likelihoods as the only scoring mechanism. Experiments across three model families (Qwen2.5-Math-7B, Qwen2.5-7B, Phi-3.5-mini-instruct) and four benchmarks show that Power Sampling approaches GRPO on in-domain MATH500, sometimes exceeds it on out-of-domain tasks (HumanEval, AlpacaEval 2.0), and preserves generation diversity that GRPO loses.

## Strengths

- **Training-free, verifier-free, and dataset-free approach.** The method requires none of the resources that make RL posttraining expensive—no training runs, no curated datasets, no external reward model or verifier. This is clearly stated and genuinely distinguishes the work from most competing approaches (lines 57, 75).

- **Theoretical differentiation from low-temperature sampling is well-established.** Proposition 1 and Observation 1 (Section 4.1, Example 1) provide a clean mathematical argument for why sampling from \(p^\alpha\) is not equivalent to low-temperature sampling, and the accompanying toy example concretely illustrates the difference. This theoretical grounding is stronger than what many inference-time methods offer. The distinction between "sum of exponents" vs. "exponent of sums" (Equations 7-8) is a genuinely useful insight.

- **Diversity preservation is convincingly demonstrated.** The pass@k curves (Figure 5) show that Power Sampling rises to ~0.98 at k=16 (matching the base model), while GRPO plateaus at ~0.90. The likelihood/confidence histograms (Figure 4) confirm that Power Sampling maintains distributional breadth while GRPO collapses to a sharp peak. This is the paper's most robust empirical finding and addresses a known weakness of RL posttraining.

- **Consistent results across model families.** The method improves over the base model and low-temperature sampling across all three model families (Qwen2.5-Math-7B, Qwen2.5-7B, Phi-3.5-mini-instruct) and all four benchmarks, suggesting the approach is not brittle or model-specific.

## Weaknesses

### Major

1. **The Phi-3.5-mini-instruct GRPO baseline appears to be a failed training run, which inflates comparative claims that rely on it.** On MATH500, GRPO achieves only 0.406 vs. the base model's 0.400 (essentially no improvement) and is *worse* than low-temperature sampling at 0.478. On HumanEval, GRPO drops to 0.134 from the base model's 0.213—a 37% relative *degradation* (Table 1, rows for Phi-3.5). The paper states that "a set of hyperparameters selected from Abdin et al. (2024) that avoids training instabilities and converges to improvement over the base model" was used, but the numbers contradict this claim. Since several headline comparisons (e.g., "outperforms GRPO by up to +59.8% on HumanEval" on line 282) draw on Phi-3.5 results, this undermines confidence in those specific claims. The Qwen2.5 models, where GRPO is strong (MATH500: 0.785 vs. base 0.496), are not affected by this issue.

2. **No compute-matched comparison against standard sampling baselines.** Power Sampling uses many forward passes per output. Equation (12) estimates \(\frac{N_{\text{MCMC}} T^2}{4B}\) tokens per output; with \(T=3072, B=192\), this is ~12.3k tokens per MCMC step, and for even modest \(N_{\text{MCMC}}=10\) this exceeds 100k tokens. The paper compares against low-temperature sampling (single forward pass) and GRPO (a training method with cheap inference). Without comparing against best-of-N or majority voting using the same total token budget from the base model, it is impossible to tell whether Power Sampling's gains come from the \(p^\alpha\) target and MCMC procedure or simply from spending more inference compute. This is the single most important missing experiment.

3. **No error bars or variance estimates.** Table 1 reports only point estimates for all methods and benchmarks. Several differences are small (e.g., GPQA: 0.389 vs. 0.399 for Power Sampling vs. GRPO on Qwen2.5-Math-7B). Without confidence intervals, multiple seeds, or significance tests, the reader cannot assess whether these differences are meaningful or noise.

### Minor

4. **The out-of-domain outperformance claim requires more careful framing.** The paper states that Power Sampling "can even *outperform* [GRPO] on *out-of-domain* reasoning tasks" (line 55). However, the GRPO baseline was trained only on MATH. The comparison therefore pits an inference-time method using the full base model against a single-domain fine-tune. This is a valid comparison of two *approaches* (training-free vs. train-on-one-domain), but the headline "outperforms RL" conflates the method with the domain specificity of the training data. The paper should acknowledge this asymmetry explicitly in the abstract and introduction. (The in-domain MATH500 comparison, where the playing field is level, is the cleanest test and shows Power Sampling within 3-4 points of GRPO—an interesting result that does not need the out-of-domain framing.)

5. **No wall-clock time or FLOPs comparison.** While the token count estimate (Equation 12) is useful, the paper never reports actual running time or FLOP-equivalent costs for any method. This makes it difficult for practitioners to assess whether the method's benefits justify its cost.

6. **Hyperparameter selection procedure is not documented.** The paper reports \(B=192, \alpha=4.0, \tau=1/\alpha\) but does not describe how these were chosen, whether they were tuned on the test sets, or whether they are stable across tasks. For AlpacaEval 2.0, a different temperature (\(\tau=0.5\)) is used for the proposal distribution (line 278), suggesting sensitivity. This is a potential source of overfitting.

### Trivial

7. The claim that the algorithm is "single-shot" (line 211) is defined explicitly ("even though multiple inference calls are made…simulate sampling a *single sequence*") but departs from conventional usage where single-shot means one autoregressive forward pass. The paper would avoid confusion by simply calling it a multi-pass single-output method.

## Nice-to-Haves

- A compute-matched ablation: compare Power Sampling against best-of-N sampling from the base model at the same total token budget per output. This would isolate whether the \(p^\alpha\) target and MCMC procedure provide leverage beyond brute-force sampling.
- Pass@k curves for the out-of-domain benchmarks (not just MATH500), to show whether diversity preservation generalizes.
- Ablation of \(N_{\text{MCMC}}\), \(B\), and \(\alpha\) to show how sensitive performance is to these choices.

## Removed Points

These points from the reviews were evaluated and determined to not be valid weaknesses of the paper as written:

- **"Out-of-domain comparison is structurally deceptive"** (Harsh Critic point 1): The paper clearly states that GRPO was trained on MATH (Section 5.1: "posttrains these models on the MATH training split"). The out-of-domain results, while needing more careful framing (kept as Minor weakness #4 above), are presented transparently. The comparison shows that a training-free method can generalize to domains where a single-domain fine-tune struggles—which is itself informative. This is not "structurally deceptive"; the framing just needs qualification.
- **"Single-shot is redefined misleadingly"** (Harsh Critic point 3): The paper explicitly defines what it means by single-shot on line 211. Readers may disagree with the terminology choice, but there is no deception.
- **"No evidence that p^α mechanism drives improvements"** (Harsh Critic point 5): The paper does compare against low-temperature sampling (the most direct baseline for the hypothesis), showing Power Sampling consistently outperforms it (Table 1). This provides evidence that the combination of the \(p^\alpha\) target plus the MCMC procedure is beneficial. A compute-matched comparison against best-of-N (kept as Major weakness #2) would strengthen this further but is distinct from "no evidence."
- **"The evaluation lacks rigor"** (generic area-of-concern sweep): Replaced by specific, anchored weaknesses above.
- Several strength-finder strengths that are generic or overlap with weaknesses (sycophantic praise of the paper's importance): Removed.

## Novel Insights

The harsh critic raises one genuinely insightful observation that goes beyond the paper's own framing: the pass@k diversity preservation result (Figure 5) is the paper's strongest finding because it is not confounded by compute asymmetry—it compares methods at the same k (same number of outputs) and does not depend on per-output token budgets. This finding suggests that inference-time MCMC sampling from the base model's power distribution can achieve "the best of both worlds" (single-shot accuracy approaching RL + multi-shot diversity of the base model), which is a more compelling and less contestable claim than "outperforms RL on out-of-domain tasks." The paper would benefit from leading with this narrative rather than the out-of-domain outperformance angle.

## Suggestions

1. Replace or remove the Phi-3.5 GRPO results, or report the training hyperparameters in full so reviewers can assess whether the baseline was properly tuned.
2. Add a compute-matched comparison against best-of-N sampling from the base model at the same token budget.
3. Report results with error bars (multiple seeds or bootstrap confidence intervals).
4. Reframe the out-of-domain outperformance claim as: "Power Sampling achieves comparable performance to domain-specific GRPO on in-domain MATH500 and generalizes to out-of-domain tasks without additional training."
5. Report wall-clock inference times and FLOP-equivalent costs.
6. Document the hyperparameter search procedure for \(\alpha, B, N_{\text{MCMC}}\).

## Score and Decision

**Round 1 bracketing:** The paper was compared against anchors in three bands on the topic of MCMC/inference-time sampling for LLM reasoning. Weak anchors (avg score 2.5–3.25) were rejected papers with thin contributions. Middle anchors ranged from 4.75 to 6.60, with relevant papers like Reprompting (5.40, Gibbs sampling for CoT prompts), Hint Marginalization (5.75, iterative Monte Carlo reasoning), and Twisted SMC (6.60, SMC for math reasoning). Strong anchors (7.0–8.5) included thoroughly executed papers like Smaller/Weaker/Better (7.00) and Syntactic/Semantic Control via SMC (8.00). The initial bracket was set to (5.0, 7.0).

**Round 2 narrowing:** Additional anchors were retrieved inside the bracket. "Large Language Monkeys" (5.00, rejected) has less novelty but better evaluation breadth. "Hint Marginalization" (5.75, rejected) has weaker theoretical foundations. "Twisted SMC" (6.60, accepted) is the closest comparison methodologically but has a more polished evaluation, though it only covers math benchmarks while this paper covers more domains. The Phi-3.5 baseline issue and missing compute-matched comparison place this paper slightly below the Twisted SMC paper. Compared to "Smaller, Weaker, Yet Better" (7.00, accepted), this paper has less evaluation rigor but a more novel core idea (inference-time vs. training-data generation).

**Final score:** This paper presents a genuinely novel and well-motivated approach with promising results, but the evaluation has meaningful gaps (broken Phi-3.5 baseline, missing compute-matched comparison, no error bars) that prevent accepting the strongest claims at face value. The core idea and diversity preservation result are valuable contributions that, with revisions, could be suitable for acceptance.

**Anchors used:**

| Paper | Path | Avg Score | Round | Comparison |
|-------|------|-----------|-------|------------|
| Twisted SMC for Math | Ze4aPP0tIn.md | 6.60 | R1, R2 | Most similar methodologically; this paper has more novel scope (training-free, no verifier) but weaker evaluation rigor. Slightly below. |
| Reprompting (Gibbs sampling) | tQqLV2N0uz.md | 5.40 | R1 | Similar inference-time iterative sampling framing; this paper has stronger theoretical foundations and more diverse benchmarks. Above. |
| Small/Weak/Better | 3OyaXFQuDl.md | 7.00 | R2 | Better-executed evaluation with thorough ablations. This paper has a more novel core idea but less evaluation rigor. Below. |
| LL Monkeys (repeated sampling) | 0xUEBQV54B.md | 5.00 | R2 | Broader scaling analysis but less algorithmic novelty. This paper's core contribution is more significant. Above. |
| Hint Marginalization | DzKdjWe59v.md | 5.75 | R2 | Similar iterative Monte Carlo framing for reasoning. This paper has stronger theoretical grounding and more diverse benchmarks. Above. |
| Syntactic Control via SMC | xoXn62FzD0.md | 8.00 | R1 | Significantly more polished evaluation and multiple constrained domains. This paper is clearly below. |

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Reject</decision>