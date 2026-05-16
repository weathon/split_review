Now I have a thorough understanding of the paper. Let me carefully synthesize the final review.

## Summary

This paper presents the first comprehensive empirical study of Bayesian neural network (BNN) surrogate models for Bayesian optimization (BO). It evaluates seven surrogate types—finite-width BNNs with HMC, SGHMC, deep ensembles, linearized Laplace, deep kernel learning, infinite-width BNNs (NNGP), and standard GPs—across diverse synthetic and real-world benchmarks varying in dimensionality, stationarity, output count, and input type. The study yields several findings: rankings are highly problem-dependent; HMC is the best fully-stochastic BNN; deep ensembles underperform; full stochasticity may be unnecessary (DKL is competitive); and infinite-width BNNs excel in high-dimensional settings.

## Strengths

1. **Comprehensive, problem-diverse empirical evaluation.** The paper compares 7 surrogate model types across synthetic and real-world benchmarks varying in dimensionality (2–60), objectives (1–3), stationarity, and input type (continuous, discrete, mixed). This breadth (Figures 3, 5, 6) directly supports the core finding that *model ranking is highly problem dependent* and prevents over-generalization from a narrow task set.

2. **Identification of infinite-width BNNs as a strong high-dimensional surrogate.** Figure 8 shows that I-BNNs consistently outperform GPs and other BNNs as dimensionality increases (20–60), with particularly large gaps on polynomial functions, neural-network function draws, and a realistic knowledge-distillation task. This is a novel finding that challenges the default GP choice in high-dimensional BO and is supported by controlled experiments.

3. **Demonstration that deep ensembles underperform in BO.** Across multiple benchmarks (Figures 3, 5), deep ensembles plateau at noticeably lower objective values (e.g., BraninCurrin, DTLZ1). The paper provides an ablation study (§4.5) linking this weakness to limited data sizes in BO, which distinguishes this setting from the typical regime where ensembles succeed.

4. **Evidence that full stochasticity may be unnecessary.** Deep kernel learning (DKL), which is only partially stochastic (last-layer GP), is competitive with fully stochastic BNNs (HMC) on several problems (e.g., Branin, BraninCurrin, Figure 3), while being simpler. This supports the claim that representation learning can matter more than full Bayesian treatment in the small-data BO regime.

5. **Systematic architecture sensitivity analysis.** Section 3.2 quantifies how network depth, width, prior variance, and likelihood variance affect posterior predictions and BO performance (Figures 1, 2). This provides concrete guidance for practitioners and reinforces the paper's main message that optimal architecture choices are problem-dependent.

6. **Ablation studies on mean vs. uncertainty quality (§4.5) and runtime comparisons (§4.5).** Hybrid models swapping mean and uncertainty estimates across surrogates reveal mechanistic insight (HMC/I-BNNs have better means, GPs have better uncertainty). Wall-clock times are reported, showing I-BNNs are competitive in both performance and runtime.

## Weaknesses

### Fatal
None.

### Major
None.

### Minor

1. **GP hyperparameter selection method is ambiguous in the main text.** The paper states it uses "standard Gaussian processes with the Matérn-5/2 kernel" (line 78) but does not specify in the main text whether GP hyperparameters (e.g., length-scale) were selected via marginalization or Type-II MLE optimization. While the experiment details are referenced to the appendix (which was stripped by the parser and exists in the original submission), the main text should state this explicitly. The paper's own §4.6 ("Revisiting Standard Assumptions") shows that the choice of marginalization vs. optimization does *not* significantly change GP performance overall ("we do not find that using the Matérn kernel and hyperparameter marginalization significantly improves the performance of GPs in general"), so this is a clarity issue rather than an evidential threat. But given that §4.6 is positioned as a separate sensitivity analysis, the main experiments' configuration should be stated up front.

2. **The "de facto standard" claim about I-BNNs is slightly overstated.** The Discussion (line 348) says I-BNNs "are well-positioned to become a de facto standard surrogate for Bayesian optimization." The evidence strongly supports that I-BNNs are *promising* and *excel in high dimensions*, but on standard low-dimensional benchmarks (Figures 3, 6) they are competitive but not dominant—sometimes underperforming GPs. Moreover, the paper's own final paragraph recommends "simple models with strong but generic assumptions—such as standard GP models." The forward-looking claim is defensible but the phrasing could mislead readers about the current evidence base. It should be tempered to reflect the observed problem-dependence.

3. **Number of MC samples for acquisition function not reported.** The paper uses Monte-Carlo Expected Improvement (line 226) but does not state the number of posterior samples used for acquisition evaluation across methods. If this number varies systematically between methods (e.g., fewer samples for expensive BNN inference), it could affect the comparisons. This is standard reporting information that should be provided in the main text or appendix.

4. **Discrete input encoding not discussed.** The paper includes problems with discrete/categorical inputs (Pest Control, Cell Coverage, Oil Spill Sorbent) and notes their presence (line 257) but does not describe how GPs or BNNs encode these inputs. Since encoding choices can significantly affect surrogate performance on discrete inputs, this is a gap in the experimental reporting.

### Trivial

1. **Architecture sensitivity study restricted to HMC.** The paper notes (line 136) that it focuses on HMC for the sensitivity analysis "as it is the gold standard." This is a reasonable scope choice, but the paper could briefly note whether similar architectural sensitivities are expected for other inference methods.

2. **Model ranking metric could be more robust.** The relative scoring in Figure 9 normalizes per trial as (r_i - r_l) / (r_h - r_l). The critic's concern about outlier sensitivity is noted; one bad trial compresses all scores. This doesn't invalidate the qualitative rankings but warrants a brief discussion.

## Nice-to-Haves

- A failure-mode analysis for I-BNNs would strengthen the high-dimensional result: on which problems do I-BNNs underperform most, and why? (E.g., are they worse on smooth low-dimensional functions?)
- For deep ensembles, systematically varying ensemble size and retraining frequency could confirm whether poor performance is a fundamental limitation or a misconfiguration artifact.

## Removed Points

- **Critic's framing of Critical Issue 1 as an "evidential issue" that undermines core comparisons.** Removed because: (a) the experiment details exist in the appendix (stripped by parser), (b) §4.6 actually shows the GP configuration choice does *not* significantly change performance, which *strengthens* rather than undermines robustness. The valid sub-point (clarity in main text) is kept as Minor #1 above.

- **Critic's claim that §4.6 is "disconnected from the main experiments."** Removed because §4.6 explicitly tests whether standard GP configurations (Matérn kernel, marginalization) are universally beneficial, which is directly relevant to the main experiments' choice of GP configuration.

## Novel Insights

None beyond the paper's own contributions. The collection of findings—particularly the I-BNN high-dimensional result, the deep ensemble underperformance linked to small data, and the competitiveness of DKL despite limited stochasticity—are the paper's genuine contributions. The reviews do not surface additional novel interpretations beyond what the paper already provides.

## Suggestions

1. In §3 or §4.1, explicitly state: "For all main experiments, GP hyperparameters were selected via [marginalization / Type-II MLE]." This resolves the ambiguity without requiring readers to consult the appendix.

2. Temper the Discussion claim about I-BNNs to: "well-positioned to become a strong candidate surrogate" or "well-positioned to become a default choice for high-dimensional BO" to better match the evidence.

3. Report the number of MC samples used for acquisition evaluation across all surrogates in §4.1.

4. Add a brief note (one paragraph) on how discrete inputs were encoded for both GPs and BNNs.

## Score and Decision

This is a timely, well-executed, and comprehensive empirical study that fills a clear gap in the Bayesian optimization literature. The experimental design is sound, the range of surrogate models is impressive, and the findings are well-supported by the evidence. None of the weaknesses undermine the core contributions. The paper requires minor clarifications but no structural revision.

MY FINAL SCORE: <pineapple>7.5</pineapple>
MY FINAL DECISION: <orange>Accept</orange>