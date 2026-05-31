## Summary

This paper provides a theoretical and empirical analysis of how predictive deviations between two continuations of the same prompt evolve inside pre-LayerNorm residual transformers. The authors prove that the residual architecture exhibits "neutral dynamics"—differences neither systematically shrink nor grow in expectation—and derive a predictable drift corridor that bounds systematic separation. They validate these predictions through controlled experiments on GPT2 variants and Qwen2.5 models, showing that neutrality is an architectural invariant that persists across scales and model families.

## Strengths

- **Novel theoretical framework**: The paper provides the first structural account of how deviations propagate through residual transformers, moving beyond empirical descriptions to formal analysis. The drift identity (Lemma 13) and predictable drift corridor (Proposition 1) are genuine theoretical contributions that give precise, testable predictions about model behavior.

- **Clean separation of architectural and stochastic effects**: The closed vs. open decoding regime distinction is elegant and methodologically sound. It isolates the architectural contribution from sampling variability, allowing the authors to prove that neutrality is a property of the residual backbone itself, not an artifact of training or sampling.

- **Rigorous empirical validation**: The experiments are well-designed, using controlled randomization networks (CRN), sibling rollouts, multiple statistical tests (t-tests, Azuma-Hoeffding bounds, anytime e-tests), and ablation studies across temperature and sibling counts. The validation across two model families (GPT2 and Qwen2.5) spanning 15M to 3B parameters demonstrates robustness.

- **Mean-field formulation**: The agent-based perspective and mean-field lift (Theorem 2) provide a principled bridge from individual trajectory behavior to population-level dynamics, explaining why neutrality holds at scale without requiring access to individual weights.

## Weaknesses

### Fatal
None.

### Major

- **The connection to hallucinations is overstated relative to what is actually proven**: The paper repeatedly claims to explain "hallucination persistence" and frames this as the central motivation, but the analysis only addresses predictive distribution differences (measured by JS divergence), not semantic correctness. The authors acknowledge this distinction (Section 2.2.1) but then revert to language suggesting the results explain hallucination mechanisms. The paper would be stronger if it more carefully delineated what neutrality does and does not explain about actual hallucinations.

- **The practical significance of the results is unclear**: The paper proves that deviations neither systematically grow nor shrink, but this is a negative result—it shows what the architecture does *not* do. The claim that this has implications for mitigation (e.g., "approaches that control onset cannot by themselves eliminate persistence") is not supported by any experiments showing that existing methods fail due to this architectural property. The paper would benefit from a concrete demonstration of how neutrality constrains or interacts with actual mitigation strategies.

- **The bound in Proposition 1 is not empirically evaluated**: The predictable drift corridor $c_t$ is derived theoretically, but the experiments only report that observed drift is "well inside" or "several orders of magnitude below" the corridor. The actual corridor values are never reported, making it impossible to assess how tight the bound is or whether it provides meaningful constraints in practice.

### Minor

- **Limited horizon (N=32)**: While the authors argue this is sufficient for the theoretical claims, longer generations would strengthen the empirical case, especially for claims about "persistence" over many steps.

- **The mean-field lift, while mathematically sound, adds limited practical insight**: The exchangeability assumption for trajectory agents is reasonable, but the result that neutrality aggregates to the population level follows almost directly from linearity of expectation. The layerwise agent analysis is acknowledged to be rough due to non-exchangeability.

### Trivial

- The Tolkien quote in the title and conclusion, while charming, does not add scientific substance.

## Nice-to-Haves

- Report the actual corridor bounds $c_t$ alongside the observed drift values so readers can assess tightness.
- Include a small-scale experiment showing how a known mitigation method (e.g., retrieval augmentation) interacts with neutrality—does it change the drift behavior or only affect onset?
- Discuss whether other architectures (e.g., post-LayerNorm, non-residual) would produce different dynamics, to clarify the specificity of the claim.

## Novel Insights

The paper's core insight is that the residual architecture of pre-LayerNorm transformers imposes a specific structural constraint on how predictive differences evolve: they are martingale differences in the closed regime and have bounded predictable drift in the open regime. This reframes "persistence" from a bug or training artifact to an architectural invariant. The drift identity (Lemma 13) is particularly elegant, showing that the expected change in divergence equals the difference between same-token and different-token updates. This provides a precise mathematical language for describing why deviations can persist without requiring any specific training outcome.

## Suggestions

1. **Reframe the narrative around predictive dynamics rather than hallucinations**: The paper's strongest contributions are the theoretical analysis of residual transformer dynamics and the statistical framework for testing neutrality. These stand on their own merit. The hallucination framing creates expectations the paper cannot fully meet and may lead readers to over-interpret the results.

2. **Report the corridor bounds explicitly**: Add a column to Table 1 showing the maximum $c_t$ value for each model, or plot the corridor alongside the observed drift in Figure 2. This would allow readers to assess how tight the theoretical bound is and whether it provides meaningful practical constraints.

3. **Add a concrete example of what neutrality looks like in practice**: Show a specific prompt where two continuations diverge, track their JS divergence over steps, and overlay the theoretical predictions. This would help readers connect the abstract analysis to observable behavior.

## Score and Decision

The paper makes a genuine theoretical contribution by providing the first structural analysis of how predictive deviations propagate through pre-LayerNorm residual transformers. The theoretical framework is rigorous, the experimental design is sound, and the results are consistent across model scales and families. However, the paper overstates the connection to hallucinations and does not fully deliver on the practical implications it claims. The core results are valuable but more limited in scope than the framing suggests.

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>