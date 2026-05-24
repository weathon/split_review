Now I have all the verification I need. Let me produce the consolidated review.

## Summary

RegMix formulates data mixture selection for LLM pre-training as a regression task: train hundreds of small proxy models (1M parameters, 1B tokens each) on diverse random mixtures, fit a LightGBM regressor to predict validation loss from mixture weights, simulate millions of mixtures to identify the optimal one, then train the large model (1B parameters, 25B tokens) with that mixture. The method relies on a *rank invariance hypothesis* — that the relative ordering of mixtures by loss is preserved across model scales. On the Pile dataset (17 domains), LightGBM achieves a 97.12% Spearman rank correlation between predictions on 1M-proxy models and actual ranks of 1B models, supporting the hypothesis. The paper also contributes empirical findings about the outsized importance of web corpora (Pile-CC) and non-obvious domain interactions.

## Strengths

- **Rank invariance validated with strong quantitative evidence.** LightGBM trained on 512 × 1M-parameter proxy models (1B tokens each) achieves a 97.12% Spearman rank correlation when predicting the validation-loss ranks of 1B-parameter models trained on 25B tokens (Table 2, line 170). This is direct empirical support for the method's central hypothesis and demonstrates that small models can reliably rank mixtures for much larger models.

- **10× compute reduction vs. DoReMi with matched average performance.** RegMix uses an estimated 3.5×10¹⁸ FLOPs for mixture selection versus DoReMi's 3.7×10¹⁹ FLOPs (Table 4, line 282), while achieving the same average downstream performance (48.6% vs. 48.6%). The parallel-training design is a structural, scalable advantage over methods that require long sequential proxy runs.

- **Counterintuitive finding about web corpora.** The paper shows that Pile-CC (CommonCrawl) validation loss has a near-perfect correlation (close to 1.0) with HellaSwag performance, while Wikipedia loss correlates much more weakly (Figure 3, line 241). This directly challenges the common practice of using Wikipedia as a primary quality benchmark and empirically justifies optimizing web-domain loss.

- **Non-obvious domain interactions revealed.** Linear regression coefficients (Figure 6) show that the PhilPapers domain has positive coefficients for all other domains — a finding that contradicts typical human intuition and demonstrates the need for automated methods over manual heuristics.

- **Actionable guidance for proxy model allocation.** The paper shows that increasing the number of proxy models from 128 to 512 (each on 0.2B tokens) outperforms training 128 models on 0.8B tokens each, under the same FLOPs budget (Figure 3, line 190). This provides concrete guidance for practitioners using the method.

## Weaknesses

### Fatal
None.

### Major

- **RegMix is statistically indistinguishable from the trivial Pile-CC Only baseline.** The average downstream performance is 48.6±0.3 for RegMix vs. 48.5±0.3 for training exclusively on Pile-CC (Table 4, line 280) — a difference of 0.1, well within one standard deviation. On several individual tasks, Pile-CC Only *outperforms* RegMix (e.g., Lambada: 34.2 vs. 32.9; SciQ: 82.4 vs. 82.8 is close; LogiQA: 26.6 vs. 25.4). The paper's own finding that Pile-CC validation loss correlates most strongly with downstream tasks makes this baseline the most natural competitor. The fact that the full regression pipeline does not clearly beat "just train on the most correlated domain" seriously weakens the claim that the regression modeling adds practical value beyond identifying which single domain matters most.

- **DoReMi comparison compromised by re-normalization.** The paper takes DoReMi's published best weights (originally over 22 Pile subsets) and re-normalizes them across the 17 available domains (line 295). The paper acknowledges this "may result in sub-optimal performance for DoReMi." This is a significant caveat: the central claim of "matching or surpassing DoReMi" relies on a comparison where the baseline likely operates at a disadvantage. A fairer comparison would either re-run DoReMi on the same 17-domain subset or clearly label the baseline as "DoReMi weights (adapted)" and qualify claims accordingly.

### Minor

- **Rank invariance tested on only 64 mixtures at the large scale.** With 17 domains, the simplex is high-dimensional, yet the critical 1B/25B validation uses only 64 unseen mixtures (line 177). The 97.12% Spearman ρ is impressive, but the paper does not report confidence intervals or bootstrap estimates, so the precision of this number is unclear. Moreover, the test mixtures are drawn from a Dirichlet-based distribution similar to the training mixtures, so this measures in-distribution generalization rather than rank invariance across the full simplex (including extreme single-domain boundaries).

- **Evaluation limited to a single dataset (Pile) and a single optimization target (Pile-CC loss).** Whether the method generalizes to other corpora, languages, or optimization targets (e.g., minimizing average loss across domains, optimizing for a specific downstream task) is untested. The OOD experiment (excluding Pile-CC entirely) is a good start but does not substitute for a second dataset.

- **Training hyperparameters for the 1B models are not reported.** The paper states only that models are trained on 25B tokens following the Chinchilla compute-optimal ratio (line 230). Learning rate, batch size, optimizer, warmup schedule, and regularization details are absent, which hinders reproducibility and makes it difficult to assess whether results are sensitive to these choices.

- **Domain interaction analysis uses only linear regression coefficients.** Section 5.4 (line 310) presents linear regression weights as evidence that "domain interactions are difficult for humans to understand." A linear model with L2 penalty captures only first-order relationships, not higher-order interactions or synergies between domains. The paper frames these coefficients as revealing "complex interactions," but the model's expressivity is inherently limited.

### Trivial

- The claim that "data mixture effects transcend scaling laws" (Section 5.5, line 311) is an observational statement supported by scatter-plot visualizations, not a rigorously tested hypothesis against scaling-law baselines. This is a minor overstatement of a qualitative observation.

## Nice-to-Haves

- Report wall-clock time or practical infrastructure requirements for the parallel training of 512 × 1M models, beyond FLOPs estimates. The 10× FLOPs advantage over DoReMi is real, but the two methods' proxy stages differ so much in design (many parallel small models vs. one long sequential run) that a simple FLOPs ratio is only a partial picture of practical cost.

- Explore sensitivity to different target domains (e.g., optimizing for Wikipedia loss or HellaSwag loss) to test whether the method's effectiveness depends on the specific correlation structure of Pile-CC.

- Provide confidence intervals (e.g., bootstrapped) for the Spearman correlation in Table 2 to quantify the precision of the rank-invariance evidence on the 64-test-mixture sample.

## Removed Points

*These points were flagged by reviewers but are removed from the main evaluation with justifications.*

- "Missing comparison to other recent data mixture methods (DoGE, Skill-It, Data Selection via Convexity)": The paper already cites these and other methods in related work. Criticism about experimental comparison breadth is scope-creep; the paper adequately compares to DoReMi (the leading method in its class) and two strong baselines (Human, Pile-CC Only). **Removed per rule: DO NOT mention missing related works.**

- "The mixture generation process is underspecified": The paper describes multiplying the token distribution by a value from 0.1 to 5.0 and using these as Dirichlet α parameters (line 66). This is adequately specified for reproducibility. **Removed: unclear what additional detail is missing.**

- "The paper does not discuss failure cases": Generic criticism that could apply to almost any paper. **Removed.**

- "The paper should compare to methods in a different category (sample-level, token-level)": The paper explicitly scopes itself as a group-level selection method (Section 2, line 39). **Removed: scope-creep.**

- Parser-artifact complaints about missing figures or garbled text. **Removed per instructions: these are parser errors, not author errors.**

## Novel Insights

The most penetrating insight that emerges from cross-referencing the reviews is that the paper's main contribution — the regression-based mixture selection pipeline — is better supported as a tool for *understanding* domain interactions and validating the rank invariance hypothesis than as a tool for *improving* downstream performance beyond simple heuristics. The 97.12% rank correlation is strong evidence that the method works for its intended purpose, but the near-identical performance to Pile-CC Only suggests that the additional complexity of the regression step may not always be necessary when a single dominant domain can be identified. The PhilPapers interaction finding is genuinely non-obvious and demonstrates the method's value for revealing structure that intuition misses — this may be its most durable contribution.

## Suggestions

1. Address the Pile-CC Only issue head-on: either (a) show settings where RegMix clearly outperforms the single-domain heuristic (e.g., when no single domain dominates, or in multi-objective optimization), or (b) reframe the contribution as a general framework for mixture analysis that subsumes the heuristic as a special case, rather than claiming superiority over it.

2. Either re-run DoReMi on the same 17-domain subset or relabel the baseline and qualify the comparison more strongly. The current presentation overclaims relative to the evidence.

3. Add confidence intervals (bootstrapped) to the key Spearman correlation numbers in Table 2 and consider testing rank invariance on a more diverse set of mixtures (e.g., extreme single-domain mixtures) to strengthen the core claim.

4. Report training hyperparameters for the 1B models in the main text or appendix to improve reproducibility.

5. Test generalizability on at least one additional dataset or optimization target to demonstrate the method is not specific to the Pile/Pile-CC correlation structure.

## Score and Decision

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Accept</decision>