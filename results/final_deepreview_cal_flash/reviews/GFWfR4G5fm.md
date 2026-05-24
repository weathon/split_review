Now I have all the information I need. Let me compile the final review.

## Summary

This paper identifies three fundamental limitations of static supervised causal learning (SCL)—fragility under distribution shifts, failure in compositional generalization, and synthetic-to-real transfer gap—and proposes the Test-Time Training for SCL (TTT-SCL) framework. The method instantiates this as TACTIC, which searches over causal graphs using a likelihood-based Alignment of Distribution (AD) metric with a sparsity penalty to generate test-aligned training data, then trains an SCL model on that data. Experiments on synthetic, pseudo-real, and real-world (Sachs) benchmarks show strong improvements over both traditional causal discovery methods and prior SCL approaches, with TACTIC (Notears) achieving 78.9 AUROC on Sachs versus 62.3 for AVICI.

## Strengths

1. **Compelling demonstration of static SCL limitations.** Section 3.2 provides clean, systematic experiments (Figure 2, Table 1) showing that state-of-the-art SCL models degrade under mechanism/graph/noise shifts, fail at compositional generalization, and collapse on real-world data despite strong synthetic performance. This clearly motivates the need for a new paradigm.

2. **Principled framework with validated components.** The TTT-SCL framework is clearly articulated, and its two key components—the AD metric and the sparsity constraint—are ablated in Table 3. Removing sparsity drops Sachs AUROC from 78.9 to 63.5, cleanly demonstrating that both terms are essential.

3. **Strong real-world results.** TACTIC (Notears) achieves 78.9 AUROC on Sachs, substantially outperforming the strongest SCL baseline AVICI (62.3) and traditional methods like PC (67.1). This directly demonstrates that test-time alignment can bridge the synthetic-to-real gap identified as a core limitation.

4. **Stage-wise analysis clarifies the mechanism.** Table 4 decomposes performance into search improvement (seed → highest-score graph) and learning improvement (highest-score → final SCL output). The large learning-phase gain (e.g., 66.6→78.9 on Sachs) validates that training an SCL model on aligned generated data provides benefit beyond what any score-based search alone would achieve.

## Weaknesses

### Major

1. **Problematic acceptance probability in stochastic graph refinement (Section 4.2, Figure 3).** The acceptance rule shown in Figure 3 is α = min(1, score(G_{k+1}) / score(G_k)). This ratio-based acceptance is only well-defined when scores are positive. The score function is score(G) = AD(G, D_test) − λ·Sparsity(G), where AD is an average log-likelihood. When scores can be negative—a plausible regime for log-likelihood-based scores—the ratio inverts the intended behavior: a better candidate (less negative) divided by a worse one (more negative) yields a ratio < 1, making good moves unlikely, while worse candidates can be accepted with probability 1. This is not a standard Metropolis–Hastings rule, and the paper provides no discussion of how the score's sign is handled. Because the stochastic refinement is central to TACTIC, this gap needs a clear resolution. The text says "accepted with probability proportional to its score" (different from the figure's formula), adding ambiguity. **The authors must clarify the actual acceptance criterion used and, if the ratio rule was employed, justify that scores are positive in the relevant regime or replace it with a correct rule (e.g., exp-based).**

### Minor

2. **AD likelihood computation is underspecified (Equation 3).** The AD metric is defined as (1/d) Σ log p(X_i | f_i^k), but the paper never states how the conditional density p(X_i | f_i^k) is computed—e.g., whether Gaussian errors with estimated variance are assumed, what regression method is used to obtain f_i^k, or how the likelihood is evaluated. While the paper notes that "many ways to implement AD [are] discussed in Appendix A," the main text should summarize the key choices for reproducibility. The noise distribution for forward-sampling is set to N(0,1) by default, but this does not necessarily match the likelihood model used in AD computation.

3. **Missing variance estimates on real-world benchmarks (Table 2).** Results on Sachs and Syntren are reported as point estimates without standard deviations, while synthetic benchmarks include standard deviations over multiple runs. The striking improvement (66.6→78.9 AUROC on Sachs in the stage-wise analysis) would be strengthened by showing variability across seeds or initializations.

4. **Hyperparameter λ is introduced but not discussed.** The score function uses λ to balance AD and sparsity, but its value and selection method are not reported (only λ=0 is shown for ablation). Sensitivity of results to λ is not explored.

### Trivial

5. **Random DAG sampling procedure not described.** The seed initialization includes "sampling a random DAG," but the paper does not specify how this is done (e.g., uniform over DAGs, edge probability).

## Nice-to-Haves

- A sensitivity analysis for λ would improve reproducibility and demonstrate robustness.
- Reporting typical runtime per test instance would help assess practicality.
- A comparison of TACTIC to classical score-based methods (e.g., GES with BIC) on the same tasks would further clarify when the added complexity of the SCL learning phase pays off beyond the search stage.
- The paper could explicitly discuss assumptions (e.g., causal sufficiency, no hidden confounders) as limitations.

## Removed Points

The following points from the reviewer inputs are removed with justification:

- **Criticisms about missing appendix content (Appendices A–G are referenced but not present in the main text):** Removed per the rule that the parser strips appendices from all papers; they exist in the original submission. The main text should be readable without them, but the absence of appendix content in the parsed version is not a paper flaw.
- **"No discussion of connections to BIC or score-based discovery":** The paper lists GES and NOTEARS as baselines and compares experimentally. The theoretical comparison to BIC is not central to the paper's contribution (which is the TTT-SCL framework, not a new score). This is scope creep.
- **"The paper does not compare to a version of TACTIC that stops at the highest-score graph":** Table 4 directly provides this comparison via the stage-wise analysis.
- **Concerns about computational cost or scalability beyond the paper's scope (d ≤ 20):** The paper acknowledges the small-graph limitation. Demanding large-scale validation beyond the stated scope is not a valid weakness.
- **Generic reproducibility concerns about undisclosed implementation details that are standard for the field.**

## Novel Insights

None beyond the paper's own contributions.

## Suggestions

1. Fix the acceptance probability rule: either adopt a Boltzmann-style acceptance (α = min(1, exp(β·(score(new)−score(current))))) or explicitly ensure scores are positive (e.g., via a learned baseline or exponential transformation). Clarify which rule was actually used in the experiments.
2. Specify the likelihood model used for AD computation (functional form, noise distribution, fitting procedure) and how λ was chosen.
3. Add standard deviations or bootstrap estimates for real-data results (Sachs, Syntren) across multiple runs.
4. Provide a brief discussion of limitations: causal sufficiency, known functional form for likelihood, and the scalability constraint (d ≤ 20).

## Score and Decision

### Calibration

**Round 1 — Bracketing.**
- Weak anchors (avg < 3.5): AvXrppAS2o (3.00, causal structure learning + outcome prediction), JzFLBOFMZ2 (3.20, LLM+CSL), fSxiromxAq (3.00, sparse causal model), TRHyAnInUC (3.25, diffusion+CD), zgM66fu0wv (2.50, iterative real-time CD). All are substantially weaker: less comprehensive experiments, no real-world validation, or less novel methodology.
- Middle anchors (3.5–7.5): ZXs3pkmrRG (5.50, TICL — test-time learning for interventional causal discovery), lQYi2zeDyh (5.00, demystifying amortized CD with transformers), x3F8oPxKV2 (6.25, zero-shot learning of causal models), cbFqqtJGtA (4.25, causal differential networks), 0sO2euxhUQ (4.00, latent SCMs). The most directly comparable paper is TICL (5.50), which also proposes test-time training for SCL. The paper under review has stronger real-world validation and more comprehensive problem identification than TICL, but TICL does not have the acceptance-probability issue.
- Strong anchors (avg > 7.5): xByvdb3DCm (8.00, selection bias in interventional studies), Nx4PMtJ1ER (8.00, signature kernel CI tests), 3cuJwmPxXj (8.00, intervention extrapolation), k38Th3x4d9 (8.00, root cause analysis), hrqNOxpItr (8.00, cross-entropy and data generation). These are top-tier causal papers with strong theory, clean experiments, and no obvious methodological gaps. The paper under review is not at this level.

**Round 1 bracket: 4.5–6.5**

**Round 2 — Narrowing within bracket.**
Queried for 4.5–6.5 on SCL test-time adaptation and 5.5–7.5 on causal discovery with dynamic training data. Key comparisons:
- ZXs3pkmrRG (5.50, TICL): **Comparable.** Both propose test-time training for SCL. TACTIC has more thorough problem diagnosis and real-world validation; TICL avoids the acceptance-probability issue. The paper under review is slightly stronger overall but has the methodological gap. → Anchor at ~5.5.
- x3F8oPxKV2 (6.25, Zero-Shot Learning): **Weaker than this anchor.** The zero-shot paper has stronger theoretical grounding and cleaner methodology but makes stronger assumptions (known graphs, ANM). The paper under review has more realistic assumptions and stronger real-world results but has a technical presentation gap. → Suggests paper is below 6.25.
- lQYi2zeDyh (5.00, Demystifying amortized CD): **Stronger than this anchor.** The paper under review proposes a novel method with strong results, whereas this is a pure analysis paper. → Suggests paper is above 5.00.
- iad1yyyGme (6.75, CausalTime): **Weaker than this anchor.** CausalTime is a well-executed benchmark generation paper accepted at 6.75. The paper under review has a clear methodological concern that CausalTime does not.

**Final score: 5.5** — Placed between the 5.0 analysis paper and the 6.25 zero-shot paper, comparable to TICL (5.5) which has a similar contribution level but a different methodological concern. The core contribution (TTT-SCL framework, problem diagnosis) is solid, but the acceptance-probability issue is a significant presentation gap that must be resolved before the method can be fully trusted.

MY FINAL SCORE: <score>5.5</score>
MY FINAL DECISION: <decision>Reject</decision>