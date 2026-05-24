Now I have a complete understanding of the paper and can confidently evaluate each claim. Here is my consolidated review.

---

## Summary

This paper proposes the first formal mathematical framework for quantifying the generalizability of ML experimental studies. It defines experiments, experimental conditions (with a three-way factor classification: design, held-constant, allowed-to-vary), ideal vs. empirical studies, and results as distributions over rankings with ties. Generalizability is defined as the probability that two independent empirical studies of the same size yield similar result distributions (measured via MMD with goal-specific kernels — Borda, Jaccard, Mallows). An algorithm estimates the minimum number of experiments needed to achieve a desired generalizability level. The framework is demonstrated on two real published studies (categorical encoder benchmark and BIG-bench LLM evaluation), showing how required sample size varies with design factors and research goals.

## Strengths

1. **Novel formalization of experimental studies (Section 3)** — The paper provides the first mathematical framework for ML experimental studies, distinguishing ideal from empirical studies, classifying factors (design/held-constant/allowed-to-vary), and formalizing results as distributions over rankings with ties (Definitions 3.1–3.4). This goes beyond prior causal-inference frameworks that assume a treatment/response structure absent in ML benchmarking.

2. **Quantifiable definition of generalizability (Definition 4.1)** — Introduces a formal, measurable definition as the probability that two independent empirical studies of the same research question yield result distributions within an MMD-based threshold. Prior work (National Academies of Science, 2019; Pineau et al., 2021) gave only intuitive verbal definitions; this is the first operationalization in ML.

3. **Algorithm to estimate required number of experiments (Section 4.3)** — Proposes a practical method to compute the minimum sample size \(n^*\) achieving desired generalizability \((\alpha^*, \varepsilon^*)\), leveraging an empirically observed linear relationship between \(\log n\) and the \(\alpha^*\)-quantile of the MMD (Proposition 4.2). This gives experimenters a concrete tool for study design.

4. **Kernel-based similarity tied to study goals (Section 4.1)** — Defines three kernels (Borda for a specific alternative, Jaccard for the top tier, Mallows for the full ranking) that let the similarity measure reflect different research goals. This flexibility is absent from existing replicability definitions that only consider parameter equality.

5. **Application to real published studies (Section 5)** — Applies the framework to Matteucci et al. (2023) and Srivastava et al. (2023), demonstrating that some design-factor combinations are already generalizable while others are not, and showing how \(n^*\) varies with design factors and goals. Figures 2 and 3 provide concrete diagnostic evidence.

6. **Analysis of sensitivity to the number of preliminary experiments (Section 5.3)** — Evaluates how the estimate of \(n^*\) stabilizes as the number of preliminary experiments \(N\) increases, showing that Mallows kernel needs fewer preliminary experiments than Borda. This gives practitioners actionable guidance on when estimates can be trusted.

## Weaknesses

### Fatal
None.

### Major
None. The paper's core claims are well-supported by the formalization and case studies.

### Minor

1. **Main-text validation uses a self-referential benchmark** — Section 5.3 evaluates the stability of the \(n^*\) estimate by comparing \(n^*_N\) to \(n^*_{50}\) (the estimate from 50 preliminary experiments), treating \(n^*_{50}\) as ground truth. This is internally consistent but does not validate against the true required sample size. The paper mentions synthetic-data validation in the appendix (line 265, "1 complements this section analyzing the behavior of \(n_N^*\) on synthetic data, for which the true \(n^*\) is known"), but the main text's central evidence rests on a circular reference point. While the transparency is commendable, the claim that the algorithm "works" would have been strengthened by including a summary of the synthetic validation in the body.

2. **No sensitivity analysis for the i.i.d. assumption and choice of \(\mu\)** — The framework assumes experimental conditions are sampled i.i.d. from a probability space \((C, \mathcal{F}, \mu)\), where \(\mu\) is chosen by the experimenter. In practice, conditions are not drawn from a random process, and two experimenters choosing different \(\mu\) could reach different conclusions. The paper acknowledges this limitation in passing (the experimenter chooses \(\mu\)) but provides no guidelines for specifying \(\mu\) in practice and no sensitivity analysis showing how robust the results are to different choices. This limits the framework's immediate applicability for practitioners who need to know how to set up the probability space.

3. **No sensitivity analysis for kernel bandwidth choices** — The paper recommends bandwidths (\(\nu = 1/n_a\) for Borda, \(\nu = 1/\binom{n_a}{2}\) for Mallows) with heuristic justifications based on the range of the argument. While these are plausible, the case studies do not explore sensitivity to these choices. An experimenter applying the framework would not know how much their \(n^*\) estimate depends on bandwidth selection.

4. **Ad-hoc preprocessing choices in BIG-bench case study** — The 80% coverage filter (conditions where ≥80% of LLMs have results, and LLMs covering ≥80% of conditions) is a pragmatic choice but could significantly affect the results. The paper notes this filter but provides no ablation or sensitivity analysis. Given that this filtering removes much of the data, its impact on the estimated \(n^*\) values is unknown.

### Trivial

- **Mapping from \(\varepsilon^*\) to \(\delta^*\) in the interpretability example is imprecise** — Line 218 states that achieving \((\alpha^*=0.99, \delta^*=0.05)\)-generalizability for the Jaccard kernel "means that, with probability 0.99, the average Jaccard coefficient between two rankings drawn from the results is 0.95." This simplifies the MMD interpretation: the threshold is on the MMD between two distributions (which involves intra- and inter-distribution comparisons), not directly on the average pairwise Jaccard coefficient. The simplification is understandable as intuition-building but could mislead readers about what exactly is being bounded.

## Nice-to-Haves

- Report confidence intervals for the estimated \(n^*\). The algorithm fits a linear model to log-transformed quantiles; uncertainty in the slope and intercept could propagate to \(n^*\).
- Include a brief summary of synthetic-validation results (currently in the appendix) in the main text to directly address the circular-benchmark concern.
- Provide concrete guidelines for practitioners on how to define the probability space \((C, \mathcal{F}, \mu)\) and suggest default choices for \(\mu\) (e.g., uniform over available datasets).

## Removed Points

These points were raised by reviewers but are excluded from the main weaknesses after verification against the paper:

1. **"Definition measures replicability, not generalizability"** — The paper's definition (Def. 4.1) directly operationalizes the definition from the cited literature (National Academies of Science, 2019; Pineau et al., 2021): "the property of two independent studies with the same research question to yield similar results." The samples \(X, Y\) in Def. 4.1 are drawn from \(\mathbb{P}\) (the ideal study distribution), which represents the full space of experimental conditions. The framework thus captures whether results hold under unseen conditions drawn from the same distribution — which is the standard notion of generalizability. The critic's distinction between "replicability" and "generalizability" is not supported by the paper's own citations.

2. **"Proposition 4.2 proof is only in the appendix"** and **"Synthetic validation is only in the appendix"** — These sections were stripped by the PDF parser; they exist in the original submission. Per policy, missing appendix content cannot be held against the paper.

3. **"Algorithm validation is circular"** — The paper's Section 5.3 transparently states "we consider the estimate \(n^*_{50}\) made at \(N=50\) as the ground truth." This is a stability analysis (testing convergence of the estimate as \(N\) increases), not a circular validation claim. The true ground-truth validation is in the (stripped) synthetic-data appendix. The concern is addressed in Minor Weakness #1 above with appropriate framing.

4. **"Missing confidence intervals"** — Moved to Nice-to-Haves; this is not standard practice for all methodological papers and does not threaten the core contribution.

5. **Various formatting/style nitpicks and generic "could be stronger" critiques** — Removed per policy. These do not affect the paper's technical validity.

## Novel Insights

None beyond the paper's own contributions. The paper's framework is itself the novel contribution. The reviews do not surface any perspective that meaningfully extends what the paper already provides.

## Suggestions

1. Add a short main-text summary of the synthetic-data validation results (1–2 sentences with key numbers) so the reader can verify the algorithm against known ground truth without consulting the appendix.
2. Include a sensitivity analysis for the choice of the probability measure \(\mu\) in at least one case study — for example, compare uniform weighting of datasets against size-weighted or stratified sampling — and discuss how practitioners should specify \(\mu\).
3. Add a brief ablation showing how \(n^*\) estimates change under different bandwidth choices for the Borda and Mallows kernels (e.g., \(\nu/2\) and \(2\nu\) relative to the recommended value).
4. Clarify the interpretability example in Section 4.3: the threshold \(\varepsilon^*\) is on the MMD between distributions, and the connection to the "average Jaccard coefficient between two rankings" is an approximation justified by the kernel's properties. A short technical note would prevent misinterpretation.

## Score and Decision

The paper makes a clear, well-structured, and genuinely novel contribution: the first formal framework for quantifying generalizability of ML experimental studies. The formalization is rigorous, the kernel-based approach for capturing different research goals is flexible and well-motivated, and the case studies demonstrate real utility. The weaknesses are minor — the validation could be more complete in the main text, and sensitivity analysis for modeling choices would strengthen the practical contribution — but none undermine the core claims. The paper is a solid contribution that will be of value to the research community.

**Score: 7.5**

**Decision: Accept**

MY FINAL SCORE: <score>7.5</score>
MY FINAL DECISION: <decision>Accept</decision>