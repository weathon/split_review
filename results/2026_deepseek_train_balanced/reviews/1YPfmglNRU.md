## Summary

This paper introduces a formal, entropy-based distinction between two types of "expertise" a decision-maker's policy can have in treatment effect estimation: *predictive expertise* (actions informed by treatment effects) and *prognostic expertise* (actions informed by potential outcomes generally). It proves a boundedness result linking expertise to overlap, characterizes existing CATE methods through this lens, and proposes an "Expertise-informed" pipeline that estimates the dominant expertise type from data to guide method selection. The empirical evaluation on synthetic data shows that the pipeline achieves best-of-both-worlds performance.

## Strengths

1. **Formal entropy-based definitions of predictive and prognostic expertise (Eqns. 4–5).** The paper provides principled mutual-information-based measures that cleanly capture the intuitive distinction between actions informed by treatment effects vs. actions informed by outcomes more generally. Prior work on treatment effect estimation only assumed overlap (non-perfect expertise) and treated the policy as a nuisance; this is the first formalization of what it means for a policy to have varying degrees of specific types of expertise. The definitions are mathematically sound and interpretable.

2. **Proposition 1: boundedness of expertise and in-context action variability (Eqns. 6–7).** The result that $E^\pi_{\text{prog}} + C^\pi \leq 1$ and $E^\pi_{\text{pred}} + C^\pi \leq 1$ establishes a fundamental trade-off: high expertise necessarily implies poor overlap, making the estimation problem harder. This directly supports the paper's central argument that leveraging expertise as an inductive bias is critical precisely when it is most needed. The traffic-light diagram (Figure 2) visualizes this clearly.

3. **Empirical demonstration that expertise type determines relative method performance (Figures 4a–4d, Table 1).** The experiments show that Action-predictive methods outperform under predictive expertise, while Balancing representations outperform under prognostic expertise. The "Expertise-informed" pipeline achieves a PEHE of **1.096** averaged across all datasets, compared to 1.123 (Action-predictive alone), 1.134 (Baseline), 1.149 (Propensity), and 1.188 (Balancing alone) — the best overall performance. This directly validates the claim that identifying the type of expertise can inform quantitative model selection.

4. **Clear conceptual distinction between expertise and optimality (§3.1, π_mis vs. π_risk example).** The paper provides a concrete numerical example where a misinformed policy achieves higher expected outcomes yet has lower predictive expertise than a risk-averse policy. This disentangles expertise from any arbitrary success measure, clarifying that expertise captures the *information content* of actions about outcomes, not their performance.

5. **Demonstration that oracle expertise can be estimated from observable data (Figures 5a–5d).** Despite expertise being defined over unobserved counterfactuals, the paper shows that plugging predicted potential outcomes from learned models into Eqns. 4–5 yields reliable estimates. Action-predictive gives the most consistent estimation across all configurations, transforming an oracle concept into a practical tool.

## Weaknesses

### Fatal

None.

### Major

1. **Synthetic-only evaluation with no bridge to semi-synthetic or real data.** The entire experimental evaluation is conducted on a fully synthetic setup where the prognostic/predictive/irrelevant partition of features is hard-coded into the data-generating process (line 205: the treatment effect "depends only on predictive variables and not on prognostic variables"). The outcome that Action-predictive works better when policies depend on predictive features, and Balancing works better when policies depend on prognostic or irrelevant features, follows largely from this construction. The paper makes practical claims about model selection in healthcare and education (line 19, lines 739–740) but never tests these claims on any semi-synthetic benchmark (IHDP, ACIC, News) or real dataset. Given that the practical value of the framework depends on whether real decision-makers' expertise patterns resemble the clean decomposition in the simulator, this gap is significant. The conclusion appropriately frames the work as "an initial demonstration" (line 797), but the abstract and introduction make stronger applied claims that the evidence does not fully support.

### Minor

2. **Pipeline threshold (1/2) is stated without justification or sensitivity analysis.** The Expertise-informed pipeline in Figure 6 uses a threshold of $1/2$ for the ratio $\hat{E}_{\text{pred}}/\hat{E}_{\text{prog}}$ to decide between Action-predictive and Balancing. This threshold is presented as-is with no motivation, ablation, or robustness check. Since the pipeline's performance depends on this choice, a sensitivity analysis would significantly strengthen confidence in the approach.

3. **Source of "real-world datasets" for covariates is unspecified.** Line 203 states that covariates come "from real-world datasets" but does not specify which ones. This matters because the distribution of feature correlations in real data could affect how cleanly the prognostic/predictive/irrelevant decomposition applies, and a reader evaluating reproducibility needs to know the source.

4. **Imprecise characterization of $C^\pi$ as a "measure of overlap."** The paper states that $C^\pi = \mathbb{H}[A^\pi|X]/\mathbb{H}[A^\pi]$ is "related directly to the overlap assumption" and is "a measure of the amount of overlap" (lines 117–118). Overlap requires $\pi(x)[a] > 0$ for all $x$ and $a$, which is a pointwise condition. While $C^\pi=0$ implies overlap violation, $C^\pi > 0$ does not guarantee overlap (e.g., a policy could be deterministic for some $x$ and stochastic for others). The paper partially acknowledges this in a footnote (line 120) but the framing in the main text is looser than warranted.

5. **Limited baseline comparison.** Only four methods are compared (TARNet, IPW, CFRNet, DragonNet). Standard causal methods like Causal Forest, BART-based estimators, and the broader metalearner suite (S/T/X-learners) are absent. This limits the generality of the claim that "different methods perform best under different expertise types" — we only see this pattern for the four methods tested.

### Trivial

None.

## Nice-to-Haves

- Evaluating the framework on at least one semi-synthetic benchmark (IHDP, ACIC, or News) would substantively strengthen the practical claims without requiring a fully new study.
- A sensitivity analysis for the pipeline threshold (e.g., testing values in $\{0.25, 0.5, 0.75, 1.0\}$) would make the proposed pipeline more robust and credible.
- Specifying which real-world datasets provided the covariates in the simulator would aid reproducibility.

## Removed Points

These points were raised but removed after cross-checking against the paper:

- *"Proof of Proposition 1 absent from main text"* — Removed per hard rule: the parser strips appendix content; the proof existed in the original submission.
- *"Circularity in the Expertise-informed pipeline"* — Removed: Action-predictive is empirically shown (Figures 5a–5d) to be the best estimator of expertise across all configurations, so using it for estimation is a natural and justified design choice. The pipeline selects *away* from Action-predictive when prognostic expertise dominates (Table 1, 1.439 vs. 1.495), confirming genuine identification rather than bias.
- *"Relative improvement plots can be misleading when Baseline degrades"* — Removed: the paper explicitly acknowledges this caveat (line 341).
- *"No confidence intervals for Table 1"* — Removed: standard deviations are provided, which is the standard practice for this type of evaluation.
- *"Novelty overclaimed — literature already has methods leveraging the policy"* — Removed: the paper does not claim to invent methods but to formalize the *type* of expertise, which is genuinely under-formalized; it explicitly cites DragonNet and inverse decision modeling as prior work that exploits the policy.

## Novel Insights

None beyond the paper's own contributions. The key insight — that the entropy-based distinction between predictive and prognostic expertise can explain when balancing representations help vs. hurt — is well-articulated by the paper itself.

## Suggestions

1. Tone down the applied claims in the abstract and introduction to match the synthetic-only evidence, reframing the pipeline as a proof-of-concept rather than a "quantitative basis" for real-world model selection until tested on semi-synthetic benchmarks.
2. Add a sensitivity analysis for the pipeline threshold, or motivate it theoretically.
3. Specify the source of real-world covariates and ideally test on IHDP or an ACIC task to bridge the gap between simulation and practice.

## Score and Decision

MY FINAL SCORE: <score>7</score>
MY FINAL DECISION: <decision>Accept</decision>