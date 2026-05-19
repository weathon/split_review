- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8
Now I have all the information needed to produce the consolidated review. Let me carefully synthesize.

## Summary

This paper proposes Auto-CEI, which combines curriculum learning with Expert Iteration to balance assertiveness and conservativeness in LLM reasoning. The method uses reasoning-step length as a proxy for problem difficulty, adjusting a reward threshold to encourage longer reasoning before the model may output "I don't know." Experiments on BoardgameQA, MATH, and Blocksworld with Llama-3.1-8B show that Auto-CEI achieves the best or tied-best composite objective \(f\) that balances precision and refusal rate.

## Strengths

1. **Superior balance of precision and refusal rate is empirically demonstrated.** Table 1 shows that Auto-CEI achieves the highest composite objective \(f\) on BoardgameQA (0.817 vs. 0.789 for the best baseline) and MATH (0.575 vs. 0.552), and ties for the best on Blocksworld (0.896). It outperforms both over-refusing baselines (SFT+R-Tuning) and over-assertive baselines (RLKF), providing concrete evidence that the curriculum + Expert Iteration framework can shift the precision–refusal trade-off.

2. **The curriculum component is shown to be beneficial via ablation.** The "No Curriculum" ablation in Table 2 yields lower accuracy and higher IDK rates across all three tasks (BoardgameQA: 56.10 vs. 59.70 accuracy, 34.43% vs. 29.37% IDK), confirming that hill-climbing \(c_1\) pushes the model to attempt more reasoning before refusing rather than simply converging to a fixed refusal threshold.

3. **Evaluation spans three diverse reasoning domains.** The paper tests on logical reasoning (BoardgameQA), mathematical reasoning (MATH), and planning (Blocksworld), which is broader coverage than many hallucination-mitigation papers that focus on a single domain. The method achieves competitive \(f\) across all three, suggesting the approach is not narrowly tailored to one problem type.

## Weaknesses

### Fatal

None.

### Major

- **The abstract's quantitative claim (10–24% precision boost) is not supported by the reported results.** The abstract states: "Auto-CEI significantly outperforms the concurrent baseline methods, boosting precision by 10-24%." However, Table 1 shows that compared to the most relevant baselines (EI+R-Tuning, SFT+R-Tuning), the precision improvements are at most ~5% absolute (BoardgameQA: 84.52% vs. 80.77% for EI+R-Tuning = +3.75 pp; vs. 80.36% for SFT+R-Tuning = +4.16 pp). On MATH and Blocksworld, Auto-CEI's precision is actually *lower* than the best baseline (55.63 vs. 60.67 on MATH; 91.53 vs. 93.95 on Blocksworld). The 10–24% range only materializes when comparing against RLKF (a baseline the paper itself acknowledges is unsuitable for these tasks) or against SFT's accuracy (a metric that, without any refusal handling, is not directly comparable to precision). This discrepancy between the headline claim and the data undermines the paper's credibility. The authors should either correct the abstract to match the evidence or provide a clear explanation of what comparison yields the 10–24% figure.

- **No statistical significance is reported.** All results in Tables 1 and 2 are single numbers with no error bars, confidence intervals, or repeated runs. Given that the margins on the key metric \(f\) are small (e.g., +0.023 on MATH, +0.028 on BoardgameQA), it is impossible to assess whether these differences are meaningful or due to random seed variance, sampling noise, or hyperparameter sensitivity. The paper uses random sampling (\(K\) samples per question, temperature-based resampling), so there is inherent stochasticity. At minimum, running each experiment 3–5 times and reporting means and standard deviations is necessary to support the central claims.

### Minor

- **Convergence criterion for Expert Iteration is not defined.** Algorithm 2 (line 164) loops "While \(\pi_\mathrm{ei}\) doesn't converge in \(D_\mathrm{val}\)", but no concrete stopping criterion is given (e.g., no improvement for N iterations, threshold on validation accuracy/f change). Without this, the number of EI rounds per curriculum step is unspecified, making the procedure incompletely specified.

- **The temperature \(\tau\) for resampling is set to the SFT model's accuracy** (line 179, a probability in [0,1]), which is then capped to [0.4, 0.7]. While the intuition (higher accuracy → more exploration) is clear, using accuracy directly as a temperature parameter is an unusual mapping and is not justified beyond the empirical capping range. The paper would benefit from explaining or ablating this choice.

- **Ablation study is somewhat narrow.** The core contribution — the curriculum — is ablated ("No Curriculum" in Table 2). However, other design decisions are not tested: alternative reward shapes for refusal responses, different initialization strategies (e.g., starting from vanilla SFT rather than R-Tuning with 25% IDK), or simpler resampling schemes. The marginal benefit of the curriculum over "No Curriculum" is also modest on some tasks (e.g., f difference ~0.002 on Blocksworld). A more thorough ablation would strengthen the paper.

- **The hill-climbing step size formula \(d = \min\{0.5, 4\sigma/10\}\) and the domain bounds \([\mu-2\sigma, \mu+2\sigma]\) are presented as empirically selected** without analysis of sensitivity to these choices. Also, the assumption that \(f\) has no local optima in \(c_1\) (line 205) is stated but not justified, which is relevant because \(f\) depends on non-convex LLM fine-tuning dynamics.

### Trivial

- The paper says "Vanila EI" instead of "Vanilla EI" in Tables 1 and the text (lines 252, 290).

## Nice-to-Haves

- Reporting computational cost (number of EI rounds per curriculum step, total GPU hours) would help practitioners assess the overhead.
- Quantitative analysis of Figure 2 (e.g., correlation between error rate and refusal rate across length bins) would strengthen the claim that Auto-CEI aligns refusal with difficulty.
- A sweep of \(\lambda\) across [0, 1] with plots, rather than just two values, would help understand sensitivity to this hyperparameter.

## Removed Points

These points are flagged to be removed, treat them with caution:

- **"RLKF is a weak comparator that makes the comparison set misleading."** The paper transparently explains (line 292) why RLKF is not well-suited to long reasoning tasks and does not rely on the RLKF comparison to support its core claims. The meaningful comparisons are against EI+R-Tuning and SFT+R-Tuning. This criticism is acknowledged and partially addressed by the paper itself.
  
- **"Vanilla EI achieves higher accuracy than Auto-CEI on 2/3 tasks."** This is correctly observed but is not a weakness: Auto-CEI explicitly trades accuracy for precision (the whole point is balancing assertiveness and conservativeness). The paper's objective function \(f\) operationalizes this trade-off, and the paper discusses this through the \(\lambda\) parameter.
  
- **"Missing related work."** Not verifiable without external sources.
  
- **"Missing appendix/proofs."** These may have been stripped by the parser.
  
- **"The initialization uses R-Tuning with 25% refusal — could different initialization achieve similar results?"** This is a reasonable question but is speculative — the paper does ablate the curriculum (which is the novel component), and the initialization is a standard starting point that the paper describes as producing "enough variety." A request for additional ablations is reasonable (included in Minor above), but framing this as a missing critical experiment overstates the concern.
  
- **Several nitpicks about "underspecified" implementation details** (e.g., "the mapping from accuracy to τ is not explained" — it is, as "the same as the overall accuracy... capped in a range [0.4, 0.7]"). These are either explained or are trivial implementation details.

## Novel Insights

None beyond the paper's own contributions. The reviews serve to flag a significant claim-evidence gap in the abstract and the lack of statistical grounding, but do not reveal any novel analytical perspective on the method or results that the paper itself does not provide.

## Suggestions

1. **Correct the abstract** to match the empirical results. For example, state the absolute precision improvements over the most relevant baselines (e.g., "+3–5% precision on BoardgameQA" or "competitive precision with 18–36% refusal rates") rather than the unsupported 10–24% claim.
2. **Add error bars.** Run all experiments 3–5 times with different seeds and report means and standard deviations. This is essential given the small margins.
3. **Define the convergence criterion** for Expert Iteration explicitly in Algorithm 2.
4. **Expand the ablation** to cover at least one alternative reward shape for refusal responses and an alternative initialization (e.g., starting from vanilla SFT with a different IDK reward).
5. **Clarify the temperature mapping** from accuracy to \(\tau\) and consider using a more standard parameterization (e.g., a tunable temperature with a fixed range).
