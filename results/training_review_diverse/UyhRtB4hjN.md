Now I have all the information I need. Let me produce the final consolidated review.

---

## Summary

This paper proposes LLEGO, an LLM-based genetic programming framework for decision tree induction. The key ideas are (1) a fitness-guided crossover operator that conditions offspring generation on a desired fitness level \(f^{*}\) controlled by hyperparameter \(\alpha\), (2) a diversity-guided mutation operator that uses LLM log-probabilities to preferentially sample low-likelihood (i.e., diverse) offspring controlled by \(\tau\), and (3) higher-arity operations enabled by the LLM's large context window. Empirical results across 12 classification and regression datasets show LLEGO outperforming five baselines (CART, C4.5, GOSDT, DL8.5, GATree), with especially pronounced advantages in larger search spaces (depth-4 trees). An ablation study confirms that all components contribute to the overall performance.

## Strengths

1. **Novel LLM-based variation operators with principled guidance mechanisms.** The fitness-guided crossover (Section 3.2) uses a roulette-wheel parent selection and conditions generation on a target fitness \(f^{*} = f_{\max} + \alpha(f_{\max} - f_{\min})\), providing a clear mechanism for steering search toward high-fitness regions. The diversity-guided mutation (Section 3.3) is genuinely inventive: it generates \(\lambda' > \lambda\) candidate offspring, then resamples using negative log-probability weights with a temperature \(\tau\), directly operationalizing diversity control at the population level. This goes well beyond naive "ask the LLM for a variation."

2. **Strong and consistent empirical performance.** Tables 1 and 2 show LLEGO achieving the best average rank (1.07 for depth-4 classification) across 7 classification and 5 regression datasets against a diverse set of strong baselines including optimal sparse tree methods (GOSDT, DL8.5). The advantage is particularly clear at depth 4 (larger search space), which is consistent with the paper's narrative that semantic guidance helps most in complex spaces. Results include means and standard deviations over 5 seeds.

3. **Well-designed ablation study that honestly characterizes each component's contribution.** Figure 7 systematically ablates four aspects: semantic prior (dataset context \(\mathcal{C}\)), fitness-guided crossover, diversity-guided mutation, and higher arity. Critically, the paper transparently reports that LLEGO_no_prior "performs very competitively" (Section 5.3), and the Limitations section (Section 6) repeats that the method "can operate effectively without semantic priors." This candor strengthens credibility.

4. **Controllable exploration–exploitation trade-off demonstrated empirically.** The hyperparameter studies in Section 5.2 (Figures 5 and 6) show that increasing \(\alpha\) improves offspring fitness at the cost of diversity, while decreasing \(\tau\) in the mutation operator reintroduces diversity. This demonstrates that LLEGO provides principled, interpretable knobs for balancing search behavior — a genuine advance over simply prompting an LLM with a fitness value.

5. **Honest discussion of limitations.** Section 6 acknowledges the computational overhead of LLM inference and explicitly frames the trade-off ("trades off computational requirements for improved search efficiency and generalization performance"). The paper also identifies concrete future directions (inference acceleration, model compression, fine-tuning strategies).

## Weaknesses

### Fatal
None.

### Major

1. **The "semantic priors" framing is overstated relative to the evidence.** The paper repeatedly claims that LLM-encoded *domain knowledge* and *semantic understanding* about the problem space is the key innovation (abstract: "integration of semantic priors and domain-specific knowledge"; line 20: "leveraging the extensive semantic priors of LLMs to reason over solution semantics"; line 180: "leveraging the semantic understanding and domain knowledge of LLMs"). Yet the ablation shows that LLEGO_no_prior — which removes only the dataset description \(\mathcal{C}\) — is highly competitive (Section 5.3). The paper itself attributes this to "the strong few-shot learning capabilities of LLMs," which is a different mechanism than domain semantics. The paper never analyzes *what* the LLM knows about the task domain or *how* that knowledge influences offspring quality vs. simple pattern-matching on fitness-labeled parent trees. The technical contributions (fitness-guided crossover, diversity-guided mutation, higher arity) are genuine and well-demonstrated, but the rhetorical framing around "semantic understanding" exceeds what the evidence supports. The paper would be stronger if it reframed the contribution around *guided few-shot generation* rather than *domain semantics*.

2. **The wall-clock time comparison conflates generator quality with search efficiency in an uncontrolled way.** The evaluation (line 129) gives each method 10 minutes of wall-clock time. Both GP methods use G=25, N=25 (line 127), but GATree's per-generation cost is negligible (random subtree crossover/mutation) while each LLEGO generation requires expensive LLM API calls. Within the 10-minute limit, GATree can likely run substantially more than 25 generations, meaning it performs many *more* total fitness evaluations than LLEGO. The paper does not report how many generations each method completes within the time budget, how many total fitness evaluations each method performs, or provide a controlled comparison that fixes the number of evaluations rather than wall time. Figure 4 compares across 25 generations (which is fair per-generation), but the main results in Tables 1 and 2 may reflect asymmetric search budgets. The paper should at minimum report per-evaluation comparisons or clarify whether G=25 is enforced as a hard cap for both methods.

### Minor

1. **The diversity metric is not defined in the main text.** Figure 4 and the discussion of population diversity reference a "Hellinger distance-based diversity metric" (presumably in the stripped figure caption), but the main text never defines what is being measured — diversity in tree structure space, function space, or some other representation. This makes the diversity results difficult to interpret substantively.

2. **Statistical significance is not assessed.** Results are reported as mean over 5 runs with standard deviations. Several competitive margins appear small relative to the standard errors (e.g., Table 1, depth 3: LLEGO vs. DL8.5 on diabetes and biofeedback). No significance tests or effect-size measures are provided, and the paper does not discuss whether the reported advantages are reliable given the limited number of runs.

3. **No discussion of LLM failure modes or output validation.** The LLM generates trees through free-form language generation, but the paper does not discuss: (a) how often the LLM produces syntactically invalid trees, (b) any retry or error-handling strategy, (c) how many generated offspring are discarded due to malformation or duplication, or (d) how this affects the effective number of useful evaluations. For a method that depends on a stochastic black-box generator, these are relevant reliability considerations.

4. **LLM API inference parameters are unspecified.** The paper specifies the model (gpt-3.5-turbo-0301) but does not report the temperature, top-p, max tokens, or other sampling parameters used when querying the API. The \(\tau\) parameter in the mutation operator controls diversity-guided candidate selection (a different mechanism), not the underlying LLM's decoding temperature. This omission is a practical reproducibility gap for a method whose core is an API call.

### Trivial
None.

## Nice-to-Haves

- A controlled experiment fixing the number of fitness evaluations (rather than wall time) would cleanly separate per-evaluation effectiveness from per-cost efficiency.
- A qualitative example comparing a decision tree evolved by LLEGO vs. one from GATree on the same dataset would help illustrate what structural differences the operators introduce.
- Reporting the number of LLM calls, average token usage per generation, and the time breakdown (LLM inference vs. fitness evaluation vs. other overhead) would help practitioners understand the cost structure.
- A failure analysis reporting the frequency and handling of invalid LLM-generated trees would strengthen reproducibility and reliability claims.

## Removed Points

- **Criticism about fairness-regularized experiment having "no results" (Section 5.4):** The truncated sentence "2).1, we investigated LLEGO's ability to mitigate negative bias by optimizing fairness-regularized objectives" clearly references a stripped appendix section. Per the parser-removal rule, these results exist in the original submission. Removed.
- **Criticism that the paper "does not provide the full prompts" in the main text:** The prompt structure is described in sufficient detail in Sections 3.1–3.3 (task context \(\mathcal{C}\), parent serialization, task-specific instructions). The exact verbatim prompts may reside in the appendix (stripped). The paper's description is adequate for reconstructing the method. Downgraded from the critic's framing.
- **Criticism that GATree can "evaluate orders of magnitude more individuals" making the comparison misleading:** Both GP methods are reported with G=25, so per-generation evaluations are comparable. The wall-clock cap may allow GATree to run more generations, but the paper's findings remain valid per-generation (Figure 4). The core concern about total-evaluation-budget asymmetry is kept in Major Weakness #2 above, but the "orders of magnitude" framing is excessive. Modified.
- **Criticism about model deprecation ("likely deprecated by the time of review"):** This is a practical concern about API availability that applies to virtually all LLM-based papers and does not invalidate the contribution. Integrated into Minor Weakness #4 (LLM inference parameters unspecified) rather than treated as a standalone fatal flaw.

## Novel Insights

The most interesting observation emerging from the reviews is the **tension between the paper's "semantic priors" framing and its own ablation evidence**. The paper would be stronger if leaned into the actual finding: that LLMs are remarkably effective as few-shot *pattern-matching generators* for structured search, even without domain-specific context. This suggests the key advantage of LLMs in GP may not be their memorized domain knowledge but rather their ability to perform in-context learning over fitness-labeled examples — effectively serving as learned, adaptive variation operators. This is a different (and arguably more generalizable) contribution than "domain-specific semantic guidance," and it opens up comparisons against other few-shot generative sequence models that the paper does not currently explore. The fitness-guided crossover with \(\alpha\)-controlled extrapolation and the log-probability-based diversity guidance are the genuinely novel algorithmic contributions regardless of what one calls the mechanism.

## Suggestions

1. Reframe the contribution to honestly center on *guided few-shot generation* via fitness- and diversity-aware prompting, rather than "semantic priors" / "domain knowledge." The technical contributions (fitness-guided crossover with \(\alpha\), diversity-guided mutation with log-probability weighting and \(\tau\), higher arity) stand on their own.
2. Add a per-evaluation comparison (fixing the number of fitness evaluations rather than wall time) to cleanly separate per-evaluation effectiveness from cost.
3. Report the LLM API decoding parameters (temperature, top-p, max tokens) and include verbatim prompt templates.
4. Define the diversity metric explicitly and report a failure analysis (invalid tree rate, retry strategy).
5. Add statistical significance tests or effect-size reporting for the main comparisons.

## Score and Decision

**Originality:** 7/10 — LLMs as variation operators have been explored before (Meyerson et al., Lehman et al.), but the specific design of fitness-guided crossover and log-probability-based diversity-guided mutation with controllable hyperparameters is novel, as is the application to decision tree induction.

**Importance of research question:** 8/10 — Decision tree induction is practically important and the NP-hard combinatorial search problem is well-motivated.

**Claims support:** 6/10 — The empirical results support the claim that LLEGO produces better trees, but the "semantic priors" mechanism is not convincingly isolated from few-shot pattern matching, and the wall-clock comparison has uncontrolled asymmetry.

**Soundness of experiments:** 7/10 — Broad benchmark coverage (12 datasets, 5 baselines) and a thorough ablation study, but weakened by lack of per-evaluation comparison, missing statistical significance, undefined diversity metric, and unreported failure modes.

**Clarity of writing:** 7/10 — The method is clearly described and the ablation results are presented honestly. The main weakness is the mismatch between the "semantic priors" rhetoric and the evidence.

**Value to community:** 7/10 — The operator design patterns (fitness-conditioned prompting, diversity-aware log-probability sampling) are reusable beyond decision tree induction and may inspire follow-up work on guided LLM-based variation operators.

MY FINAL SCORE: <pineapple>7.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>