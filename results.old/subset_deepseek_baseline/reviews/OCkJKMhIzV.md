## Summary
This paper evaluates how large language models (LLMs) behave in three canonical game-theoretic tasks—Rock-Paper-Scissors (RPS), Centipede Game (CG), and Traveler’s Dilemma (TD)—where human behavior systematically deviates from classical game-theoretic predictions. By mirroring established human-subject protocols, the authors compare LLM decisions to both equilibrium predictions and historical human data. They find that LLMs generally align more with game-theoretic rationality than with human play, exhibit limited sensitivity to payoff-related hyperparameters, and show high variance across prompt verbalizations.

## Strengths

- **Direct comparison with human behavioral data.** The work shifts the evaluation focus from “how rational is the LLM?” to “how human-like is the LLM?” – a valuable perspective for understanding LLM decision-making in interactive settings.
- **Thorough experimental design.** Three diverse game types (evolutionary, sequential, one-shot) are studied. The use of multiple verbalizations of strategy labels (10 per condition) and aggregation across them provides a principled measure of prompt-induced variance, a known source of LLM brittleness.
- **Rigorous execution at scale.** The experiments involve 100 agents, repeated rounds, different payoff magnitudes, and multiple model families (3B–671B parameters), lending robustness to the reported trends.
- **Clear reporting of high standard deviations across verbalizations.** Rather than hiding this variance, the authors flag it explicitly, which is honest and informative for future work on prompt sensitivity.

## Weaknesses

### Fatal
None.

### Major
1. **Comparison to human experiments may not be fully controlled.** The paper states that it “imitates the experimental setup” of the original human studies but reduces the number of rounds in RPS to 30 and participants to 100 (for computational reasons). It does not report the exact parameters of the historical human experiments (e.g., Wang et al. 2014 used 30 rounds?; McKelvey and Palfrey 1992 played a different number of matches per subject?). Without confirming that the comparison is apples-to-apples, the quantitative claims about how LLMs compare to humans (e.g., “most models underperform with respect to the NE scores” vs humans who outperformed NE) may be misleading.

2. **Insufficient statistical analysis of hyperparameter insensitivity.** The paper claims that LLMs are “largely insensitive” to payoff parameters ($\omega$ in RPS, $r$ in TD, horizon and stakes in CG). In RPS a single Spearman coefficient is mentioned across all $\omega$; in CG and TD the claim is supported only by visual inspection of tables/figures. Formal tests of equivalence or effect sizes are missing, making this conclusion less convincing than it could be.

3. **High variance across verbalizations undermines some conclusions.** While the reporting of standard deviations is commendable, the magnitude (e.g., standard deviations of 10–30% in CG probabilities, large differences across models) suggests that the observed behavior is heavily contingent on how strategies are labeled. This casts doubt on whether any single aggregate pattern (e.g., “LLMs tend to take earlier”) is robust across plausible prompt variations.

### Minor
- The paper omits a discussion of whether the historical human data were collected under one-shot or repeated-play conditions for TD (Capra et al. 1999 used repeated rounds, which is acknowledged). However, the compared results appear to match the experimental protocols used for LLMs, so this is not a fatal omission.
- The models tested are from 2024; given the rapid pace of LLM development, the findings may date quickly. This is unavoidable but worth noting.

### Trivial
- Table 1 and Table 2 have some formatting issues in the text (e.g., duplicated model names in Table 1). These are parser artifacts and not actual errors.

## Nice-to-Haves
- A qualitative analysis of why specific verbalizations cause such large behavioral shifts would be very informative.
- A Bayesian or meta-analytic approach to combine results across verbalizations (rather than just mean±std) could provide more interpretable effect-size estimates.
- Testing whether providing explicit reference to game-theoretic concepts (e.g., “Nash equilibrium”, “backward induction”) changes behavior would help disentangle pre-training knowledge from in-context reasoning.

## Novel Insights
Beyond its own empirical contributions, the paper offers the insight that LLMs exhibit a kind of “cautious rationality”: they tend to avoid risky strategies (e.g., passing in CG, claiming high in TD) when the theoretical equilibrium is safe but low-paying. Yet in RPS they fail to achieve equilibrium payoffs because they cannot maintain the required randomness. This suggests that LLMs’ strategic behavior is not simply “more rational” than humans, but is shaped by a mix of over-regularization (avoiding risk) and pattern-matching that is sensitive to the label space.

## Suggestions
- Provide a table that explicitly lists the original human experiment parameters (number of rounds, participants, payoff scales) alongside those used for the LLMs, to clarify comparability.
- For the hyperparameter sensitivity claim, include a statistical test (e.g., ANOVA or equivalence testing) that directly tests for an effect (or lack thereof) of $\omega$, $r$, and stakes on the key behavioral metrics.
- Report the number of independent trials (seeds) used for each LLM model beyond the verbalizations, and whether temperature was fixed at 0 or a low value to reduce stochasticity.

## Score and Decision
Score: 7.0

Decision: Accept

**MY FINAL SCORE:** <score>7.0</score>  
**MY FINAL DECISION:** <decision>Accept</decision>