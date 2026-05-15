Now I have a thorough understanding of the paper and can verify the reviewer claims. Let me compose the consolidated review.

## Summary

This paper presents a systematic empirical study comparing Bayesian neural network (BNN) surrogates against standard Gaussian process (GP) surrogates for Bayesian optimization. It evaluates seven surrogate types (HMC, SGHMC, deep ensembles, LLA, deep kernel learning, infinite-width BNNs, and standard GPs) across synthetic benchmarks, six real-world datasets, high-dimensional problems, and non-stationary tasks. Key findings include: (i) no single surrogate dominates across all problems; (ii) HMC is the most effective inference method for finite-width BNNs; (iii) deep kernel learning is surprisingly competitive with fully stochastic BNNs; (iv) deep ensembles perform poorly in the small-data BO regime; (v) infinite-width BNNs show strong performance on high-dimensional problems. The paper fills a clear gap in the literature by providing a comprehensive, methodologically neutral comparison.

## Strengths

- **Comprehensive and methodologically neutral comparison**: The paper evaluates seven distinct surrogate types across synthetic benchmarks, six real-world datasets, high-dimensional problems, and non-stationary tasks (Figs. 2–5, Section 4). This breadth supports the paper's headline finding that no single surrogate dominates and that rankings are highly problem-dependent. The paper explicitly avoids championing a particular approach ("we believe it is particularly valuable not to have a 'horse in the race'"), which lends credibility to the findings.

- **Novel study of infinite-width BNNs for Bayesian optimization**: As the paper correctly claims, this is the first study to apply infinite-width BNNs (I-BNNs) as BO surrogates (lines 65–66). The finding that I-BNNs perform well on high-dimensional problems is genuinely novel and practically relevant, supported by three tasks including a real knowledge-distillation problem (Fig. 4).

- **Counterintuitive findings that challenge conventional wisdom**: The paper provides empirical evidence that (a) deep ensembles — widely used in uncertainty estimation — perform surprisingly poorly in small-data BO (Fig. 2), (b) deep kernel learning is competitive with fully stochastic BNNs despite lacking parameter stochasticity, and (c) standard GP design choices (Matérn kernel, hyperparameter marginalization) do not consistently improve performance (Section 4.6, Fig. 6). These results are interesting and well-supported.

- **Useful architectural sensitivity study**: The systematic investigation of prior variance, likelihood variance, network depth, width, and activation function (Figs. 1–2, Section 3.1) provides concrete guidance for practitioners and demonstrates that optimal BNN configurations are problem-dependent.

- **Ablation studies separating mean from uncertainty quality**: The hybrid-model analysis (Section 4.5) revealing that HMC and I-BNNs have better mean estimates while GPs have better uncertainty estimates is insightful and goes beyond surface-level accuracy comparisons.

## Weaknesses

### Fatal
None.

### Major

1. **The high-dimensional I-BNN claim is partially supported by tasks with favorable structure.** Two of the three high-dimensional experiments are synthetic: a polynomial function and a fixed draw from a neural network. The neural-network function draw is generated from an architecture whose prior aligns naturally with the I-BNN's NNGP kernel (derived from the same architecture family). While the reviewer overstates this as "exact prior matching" — a finite-width NN draw is not from the infinite-width NNGP prior — the evaluation nonetheless stacks the deck somewhat in favor of I-BNNs. The polynomial function is not clearly confounded, and the knowledge-distillation task (real-world, unconfounded) is genuine. The core claim that "I-BNNs are particularly promising, especially in high dimensions" (abstract, line 4) is therefore partly supported but over-generalized. The paper would be stronger with an explicit counterfactual: a high-dimensional stationary objective drawn from a GP prior, to test whether I-BNNs excel broadly or specifically on NN-aligned structure. This does not invalidate the paper — the knowledge distillation task still shows real-world value — but it weakens what would otherwise be the strongest finding.

### Minor

2. **The architecture used in the main experiments is not explicitly stated in the main text.** Section 3.1 presents a sensitivity study with a base configuration (depth=3, width=128, tanh; line 114), but it is not confirmed whether this same configuration carries over to the main benchmarks (Figs. 3–5). The paper states that "hyperparameters generally have minimal effects on the performance" (line 235) and defers details to the appendix, but the ambiguity weakens in-text reproducibility. This is addressable.

3. **No formal statistical significance assessment of rankings.** Rankings (Figs. 3, 4, 6) are reported with means and standard errors over 10 trials but without significance tests or confidence intervals on pairwise comparisons. The claim that "HMC generally works the best" (finding ii) rests on visual impression rather than statistical testing. Given that the variability could alter ordering, this is a gap — though a common one in empirical benchmark papers. The paper could partially address this via a simple paired permutation test.

4. **The ranking formula in the text contains an error.** Line 310 states: "The score of model with maximum reward is (r_i - r_h) / (r_h - r_l)." As written, this yields 0 for the best model and negative values for all others, but Figure 6 shows scores in [0,1]. The intended formula is clearly (r_i - r_l)/(r_h - r_l). This is a typo in the text (the implementation is evidently correct) but it affects clarity.

5. **Deep ensembles are evaluated primarily in the small-data regime (≤100 evaluations), which the paper itself acknowledges is where they struggle.** The paper notes that "the performance of deep ensembles is greatly improved [with more queries], consistent with the explanation that their poor performance on many tasks is due to limited data" (Section 4.5). This is a reasonable admission, but it means the headline finding "(iv) deep ensembles perform relatively poorly" (abstract) is a finding about a specific budget regime, not about the method in general. The paper does address this tension, but the abstract and early discussion present the result without qualification.

### Trivial
6. The non-stationarity experiment result is deferred entirely to the appendix (referenced at line 272). Including a summary figure or key result in the main text would strengthen the narrative.

## Nice-to-Haves

- Adding a high-dimensional GP-draw synthetic task (stationary, Matérn prior) to serve as a counterfactual for the I-BNN evaluation would cleanly disambiguate whether I-BNNs excel specifically on NN-structured objectives or more broadly on high-dimensional problems.
- Including a simple statistical significance analysis (e.g., paired permutation tests for key pairwise comparisons) would strengthen the ranking claims without requiring major changes.
- Summarizing the non-stationarity result with a 1-D figure in the main text rather than deferring entirely to the appendix would improve the paper's flow.

## Removed Points

These points were flagged by reviewers but are removed after cross-checking against the paper — treat with caution if referencing them:

- **"HMC claim is not statistically grounded"** — kept substantively above as Minor point 2, but the critic's framing as a fundamental evidential gap is overstated. The paper reports means with standard errors over 10 trials, which is standard practice for BO benchmarks. Formal significance testing is a nice-to-have, not a requirement.
- **"SGHMC and deep ensembles need tuning per problem"** — the paper explicitly notes (line 235) that hyperparameters have minimal effects on performance and defers additional studies to the appendix. The critic's demand that each method be tuned per problem is disproportionate for a comparative study whose scope already includes 7 methods × many problems.
- **"Missing non-BNN baselines (random forests, HeSBO)"** — this is scope creep. The paper's stated goal is to evaluate BNN surrogates vs. standard GPs for BO, not to benchmark all possible surrogates.
- **"Architecture search results only in appendix"** — this is the standard division of labor between main text and appendix in page-limited papers. The main text summarizes the finding (lines 315–319).
- **"Non-stationarity experiment missing from main text"** — the paper references the appendix for the figure. This is standard practice.
- **"The statement that there is no noticeable preference as dimensionality increases is not well supported"** — the paper qualifies this with empirical comparisons across the real-world benchmarks, which span varied dimensionalities. The reviewer's assertion is a judgment call, not a factual error.

## Novel Insights

The reviewers' most interesting observation not explicitly surfaced by the paper is the tension between the I-BNN high-dimensional result and the prior-alignment confound. The paper attributes I-BNN success to "non-Euclidean similarity metrics" that are "valuable for high-dimensional BO" (line 32). An alternative interpretation is that I-BNNs succeed when the objective's structure matches the prior induced by the neural network architecture — the fixed NN function draw is the clearest case. This does not reduce the contribution (the knowledge distillation task shows real-world relevance), but it suggests the paper's framing could be refined: what makes I-BNNs effective may not be "handling high-dimensions" generically, but rather providing a strong NN-derived prior that is particularly useful when the true objective has NN-like structure. This is a more specific and testable hypothesis than the current framing, and it opens a clear direction for follow-up work.

## Suggestions

1. Explicitly state the architecture (depth, width, activation) used in the main benchmark experiments (Figs. 3–5) in the main text, or clarify that the base configuration from Section 3.1 (depth=3, width=128, tanh) carries over throughout.
2. Add a brief statistical comparison: for the key pairwise contrast (e.g., I-BNN vs. GP on high-dimensional problems), report a paired permutation test p-value or at minimum the fraction of trials where one method outperforms the other.
3. Fix the ranking formula typo on line 310: "(r_i - r_h)" should be "(r_i - r_l)".
4. To strengthen the I-BNN high-dimensional claim, add one counterfactual synthetic experiment where the true objective is drawn from a high-dimensional GP (stationary Matérn). If I-BNNs still excel, the claim is robust; if they do not, the scope of the claim should be qualified accordingly.
5. Include a 1-D illustrative example of the non-stationarity experiment (analogous to Fig. 1) in the main text to make the failure mode of GPs on non-stationary objectives immediately visible to the reader.
6. In the abstract and introduction, qualify finding (iv) slightly — "deep ensembles perform relatively poorly in the small-data regime typical of BO" — to avoid overgeneralizing a budget-dependent result.

## Score and Decision

MY FINAL SCORE: <pineapple>6.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>