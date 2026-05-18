Now I have all the information needed. Let me synthesize the final review.

## Summary

This paper studies the problem of LLM output legibility—whether chain-of-thought solutions can be easily verified by humans or smaller models. The authors show that optimizing solely for answer correctness degrades legibility (a "legibility tax"), and propose an iterative checkability training algorithm, inspired by Prover-Verifier Games, that alternately trains (1) a verifier to judge solution correctness, (2) a helpful prover to produce correct solutions that the verifier accepts, and (3) a sneaky prover to produce incorrect solutions that fool the verifier. The key empirical finding is that training against a small verifier produces solutions that are both reasonably accurate and more legible to time-constrained human evaluators, suggesting that checkability to small models may transfer to human legibility.

## Strengths

1. **Clear demonstration of a legibility tax and its mitigation.** The headline result (Fig. 1) compellingly shows the tradeoff: correctness-only RL produces high-accuracy but illegible solutions, while the initialization is legible but inaccurate. The proposed checkability training achieves a better accuracy–legibility tradeoff, with the helpful prover's accuracy and human judges' accuracy both improving across rounds (Fig. 5). This is the paper's central empirical contribution and is well-supported by converging automated and human metrics.

2. **Systematic evaluation of verifier robustness across multiple attack types and model sizes.** The paper tests verifiers against SRC, CGC, and goodharting attacks (Fig. 6a), evaluates balanced best-of-n accuracy (Fig. 6b), and varies verifier compute across four orders of magnitude. The finding that larger verifiers are harder to exploit and that robustness increases across rounds is well-supported and provides insight into when checkability training works.

3. **Exploration of alternative reward formulations with clear failure analysis.** The comparison of SRC, CGC, and goodharting rewards (Section 5) is informative: CGC leads to worse training dynamics and goodharting does not transfer to human legibility, ablated against the main results. This strengthens the case for the SRC design choice.

4. **Principled theoretical framing.** Theorem 1 connects the verifier-leading Stackelberg equilibrium to completeness and soundness. While the paper is transparent that the empirical setting does not satisfy the theorem's assumptions, the theory provides useful intuition and situates the work within the PAC verification and interactive proofs literature.

5. **Honest and thorough limitations section.** The paper explicitly discusses reliance on ground-truth labels, limited domain (GSM-only), the conflation of CoT with legibility, heterogeneous stopping criteria, and potential hyperparameter suboptimality (Section 6.1). This transparency is commendable and helps readers calibrate the claims.

## Weaknesses

### Fatal

None.

### Major

1. **Inadequate reporting of human evaluation methodology and statistics.** The paper's claim that legibility transfers to humans rests heavily on the human contractor studies in Sections 4.1, 4.3.2, and 4.3.3. The main text provides: (i) the time limit (45 s) and task (determine validity), (ii) mean accuracy values in figures, but **no sample sizes** (number of contractors, number of solutions per condition, whether solutions were judged by one or multiple raters), **no inter-rater agreement**, **no confidence intervals or standard errors**, and **no statistical tests** reported for the human accuracy comparisons across rounds. The figures displaying human accuracy (Fig. 1b–d, Fig. 4b, Fig. 5g–h) show only point estimates without error bars, making it impossible to assess whether the observed differences (e.g., human accuracy increasing from round 0 to round 4 for the helpful prover) are statistically reliable. This is not a trivial omission—it is the linchpin of the human legibility claim. The paper would benefit significantly from transparent reporting of what was already done, even without additional experiments.

### Minor

2. **Ambiguity about checkpoint selection for human evaluation.** The paper defines an early-stopping criterion ("when sneaky incorrect solutions become as convincing as helpful correct solutions," Fig. 2 caption) and states that human evaluations use the "last checkpoints of current-round helpful provers" (Section 4.2.1). However, the paper does not make explicit whether the same early-stopping rule was applied consistently across all human evaluations or whether a fixed number of steps was used. Given that the helpful prover's accuracy can decline at the end of each round (Fig. 2b), this ambiguity matters for interpreting the round-over-round human accuracy trends. The paper acknowledges using different stopping criteria for different experiments and notes "We do not observe qualitative different between early stopping and non early stopping rounds" (Section 6.1), which partially mitigates the concern, but a precise statement about the human evaluation checkpoints is needed.

3. **The "transfer" claim is supported by correlational evidence without causal isolation.** The paper observes that helpful solutions that are more convincing to the small verifier are also more accurately judged by humans, and that sneaky solutions harder for the verifier to reject are also harder for humans to spot. The comparison with the correctness-only baseline (which does not transfer) is valuable and shows that checkability training produces qualitatively different, more legible solutions. However, the mechanism of transfer is not isolated—the observed correlation could also arise from solutions shifting toward a more human-natural style as a side effect of training, rather than from the verifier signal specifically. The paper's phrasing is appropriately cautious ("seems to transfer"), but the abstract and introduction make somewhat stronger assertions. A within-round per-solution analysis correlating verifier confidence with human accuracy (controlling for solution correctness) would strengthen the argument.

### Trivial

4. **The goodharting baseline's human evaluation mentions "no significant difference" without specifying the statistical test used** (Section 4.2.3). While this is a secondary negative result, standard reporting practice should include the test type and sample size.

5. **The GPT-4 step-by-step validity metric** (Fig. 4a) is not validated against human judgments of per-step correctness. This is a reasonable automated proxy, but its alignment with human perception is unverified. Minor, since the paper also has direct human data on full-solution accuracy.

## Nice-to-Haves

- Report the human evaluation with full transparency: number of contractors, number of judgments per condition, inter-rater agreement (e.g., Fleiss' κ), and standard errors or confidence intervals for all mean accuracies.
- Provide a precise quantitative rule for the early-stopping criterion, and verify that human evaluation results are robust to small variations in the stopping threshold.
- Compute per-solution correlations between verifier confidence and human accuracy within each round, controlling for solution correctness, to directly test the transfer mechanism.

## Removed Points

- The criticism about human evaluation methodology "not described in the appendix" is removed because the appendix is stripped by the parser and may contain these details in the original submission.
- The criticism that Theorem 1 "plays no role" in experiments is removed as an overstatement—the paper is transparent about the gap between theory and practice, and the theorem serves as principled motivation, which is a standard and acceptable role for theory in empirical papers.
- The generic "could benefit from a simple ablation" suggestions are moved here as they are suggestions, not verified weaknesses.

## Novel Insights

The harsh reviewer's most valuable observation is that the human evaluation reporting gap is the single weakest link in an otherwise well-executed paper. The key human legibility results (Figs. 1b–d, 4b, 5g–h) are presented without error bars or statistical tests, which is a meaningful omission for results at the center of the paper's claimed contribution. The reviewer's suggestion to compute within-round correlations between verifier confidence and human accuracy is a concretely actionable way to strengthen the transfer claim beyond what the current between-condition comparison provides.

## Suggestions

- Add standard errors or confidence intervals to all human accuracy figures. Even bootstrapped 95% CIs would substantially increase confidence in the reported trends.
- Report the number of contractors, number of judgments per condition, and inter-rater agreement in the main text.
- If the early-stopping criterion was applied consistently across all human evaluations, state this explicitly; otherwise, clarify the selection rule.
- Consider adding a per-solution analysis correlating verifier scores with human accuracy within each round to provide direct evidence for the transfer mechanism.

## Score and Decision

The paper makes a genuine contribution: it identifies a concrete legibility tax from correctness-only optimization, proposes a practical training framework to mitigate it, and provides converging evidence from automated and human evaluations. The automated experiments are thorough and well-designed. The main weakness is the thin reporting of the human evaluation methodology, which is fixable (the authors likely have these records) and does not invalidate the core empirical findings—the automated metrics independently support the claim that checkability training improves legibility to verifiers, and the human data trends are consistent and monotonic. With transparent reporting of the human studies, the paper would be a strong contribution.

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>