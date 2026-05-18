Now let me compose the consolidated review.

## Summary

This paper proposes EOR (Explainable Operations Research), a framework that combines bipartite graph-based quantification of constraint/parameter changes (via graph edit distance / GED) with a multi-agent LLM system (Commander, Writer, Safeguard) to generate explanations for what-if analysis in OR. The paper also introduces a new industrial benchmark of 30 problems × 10 expert-crafted queries for evaluating explainable OR. Empirically, EOR consistently outperforms both a vanilla LLM baseline (Standard) and OptiGuide across multiple LLM backbones, achieving up to 95.33% modeling accuracy and explanation quality scores above 8.8/10.

## Strengths

1. **New industrial benchmark for explainable OR** — The paper constructs a benchmark of 30 categorized problems across multiple OR domains (supply chain, finance, logistics, etc.), each with 10 expert-crafted queries involving diverse constraint/parameter modifications (add, delete, update, combine). The queries are developed from scratch and explicitly not part of LLM training data (Section 4.1). This fills a genuine gap, since existing OR datasets (NL4OPT, ComplexOR, IndustryOR) focus on modeling rather than explanation evaluation.

2. **Systematic GED-based quantification methodology** — The three-step pipeline (LP conversion → bipartite graph representation → normalized GED computation, Equations 1–3, Section 3.2.2) provides a principled, unified way to measure the impact of complex constraint and parameter changes. This goes beyond sensitivity analysis on parameters alone and handles constraint additions, deletions, and combinations in a single framework.

3. **Consistent and substantial accuracy improvements** — Table 2 shows EOR outperforming both baselines across all four LLM versions in zero-shot and one-shot settings. With GPT-4-Turbo, EOR achieves 88.33% (zero-shot) and 95.33% (one-shot) vs. 63.00%/75.67% for Standard and 30.33%/58.33% for OptiGuide. The gap is large and consistent.

4. **Clear problem formulation** — Section 3.1 provides a formal mathematical framing of explainable OR with explicitly defined inputs (decision variables, objectives, constraints) and outputs (attribution and justification explanations), establishing a structured foundation for future work.

5. **Multi-agent architecture with built-in safety verification** — The Commander-Writer-Safeguard workflow (Section 3.2.1) includes iterative debugging triggered by safety checks. Table 4 shows this reduces total errors by 60% from zero-shot to one-shot and eliminates syntax errors entirely, which is a practical engineering contribution.

## Weaknesses

### Fatal
None.

### Major

1. **Unvalidated core contribution: the GED-based Decision Information quantification is not shown to causally improve explanation quality.** The paper's most distinctive claim — that quantifying Decision Information via bipartite graph edit distance enhances the LLM's explanations — is not supported by the experimental design. There is no ablation comparing EOR with vs. without the GED signal. The paper states "Since LLMs cannot directly perform this quantification, we utilize them to sense these processes and generate explanatory insights" (Section 3.2.2), but never specifies *how* the GED computation result is communicated to the LLM, what prompt template conveys this information, or how the GED value influences the generated explanation. No example input or output demonstrates the GED value changing the LLM's behavior. Since the multi-agent framework (Commander, Writer, Safeguard) with its iterative debugging loop and well-engineered prompts could entirely account for the observed improvements in both accuracy and explanation quality, the specific contribution of GED-based quantification remains unsubstantiated. This is a structural gap: the paper claims GED + LLMs enhance explanations, but the experimental design cannot separate the effect of GED from the effect of the multi-agent framework.

### Minor

2. **Accuracy metric is underspecified** — Section 4.2 states accuracy is evaluated by "comparing the optimization outcomes" to ground truth, but does not specify whether this means the optimal objective value only, the decision variable assignments, or both. Two solutions can match on objective value while differing on variable values, so the definition matters for reproducibility.

3. **OptiGuide baseline is a weak comparison by design** — The paper itself notes OptiGuide is designed for "easy what-if analysis" and cannot handle constraint deletions or combinations (Section 1), yet includes it as a primary baseline on a benchmark that features such complex modifications. The Standard (vanilla LLM) baseline is more informative, and EOR's strong performance against it is credible. However, the most informative comparison — the multi-agent framework *without* the GED component — is absent, making it impossible to attribute gains to the GED specifically.

4. **No decomposition of accuracy improvements** — The Safeguard agent's iterative debugging loop catches and corrects errors. The paper does not break down whether EOR's accuracy gains come from better initial code generation, more effective debugging, or GED-informed reasoning. A with/without Safeguard ablation would clarify this.

5. **Expert evaluation lacks key reporting details** — The paper mentions "OR experts anonymously score the explanations" (Section 4.2) and reports expert scores in Table 3, but does not specify the number of experts, their qualifications/expertise level, or inter-rater reliability metrics. This makes it difficult to assess the robustness of the expert evaluation.

6. **No discussion of GED computational complexity** — Graph edit distance is NP-hard. The paper cites existing GED algorithms (Gao et al., 2010; Stauffer et al., 2017; AbuAisheh et al., 2015; Xing et al., 2024) but does not state whether an exact or approximate method was used, nor discuss computational cost for larger OR models with hundreds of variables and constraints.

7. **No statistical significance or confidence intervals** — All results are point estimates. With 300 queries per setting, bootstrap confidence intervals or significance tests (e.g., paired permutation tests) would help assess whether differences between methods are reliable.

8. **Failure analysis is coarse** — Section 4.7 categorizes errors into three types (JSON format, correct execution but wrong, runtime errors) but does not analyze *why* modeling logic errors occur (e.g., misinterpretation of constraints, missing constraints, wrong parameters), which would be more informative for improvement.

### Trivial
- None beyond what is already classified as Minor above.

## Nice-to-Haves

- Add an ablation removing the GED component while keeping the three-agent framework and prompts identical, to isolate the effect of Decision Information quantification.
- Show a concrete prompt template or example illustrating how the GED value is supplied to and used by the LLM.
- Validate the GED metric itself: does the normalized GED correlate with human judgments of "how much the decision changed"?
- Report the number and qualifications of OR experts used in the blind evaluation, along with inter-rater reliability (e.g., Fleiss' κ or ICC).
- Add an ablation removing the Safeguard agent (or replacing it with a simple try/except wrapper) to quantify its contribution to accuracy.
- Provide computational cost analysis (LLM API calls per query, total cost) relevant for practical deployment.

## Removed Points

These points were raised by reviewers but are removed for the reasons stated; treat them with caution if encountered:

- **"Definition and role of Decision Information are inconsistent"** — The definition itself (Definition 1, Section 3.2.2: "parameters and constraints specified in a user's query") is clear and consistent. The issue is about *integration* (how GED is used by the LLM), which is already captured as Major weakness #1. Removed as redundant.
- **"No examples or citations showing OptiGuide fails on complex cases"** — The paper provides a concrete warehouse-closure example (Section 1) illustrating why constraint deletion is challenging. Removed as factually incorrect.
- **"300 instances is a small benchmark"** — For an expert-crafted, domain-specific OR benchmark with ground-truth explanations, 300 queries across 30 problems is a reasonable first effort. The paper never claims scale as a strength. Removed.
- **"LLM self-evaluation bias"** — The paper acknowledges this limitation (Section 4.2) and supplements automated evaluation with blind expert review. Removed as already addressed.
- **"Strength: this paper addressed an important problem"** — Generic; removed as per filtering rules.
- **Strength Finder's generic language about "Single most important piece of evidence"** — The Table 2 evidence is already included in Strengths; the framing language is editorial and not needed.

## Novel Insights

The main structural insight that emerges from reviewing this paper is a common pattern in ML/OR systems papers: a complex pipeline with multiple components yields strong end-to-end results, but the paper's evaluation design cannot attribute those results to the component claimed as the methodological novelty (here, GED-based Decision Information quantification). The multi-agent framework with iterative debugging is a well-engineered contribution in its own right, but the paper positions the GED component as "the core of EOR" (abstract). To substantiate this, the authors would need an experimental design that isolates whether the GED signal causally improves explanations — either through an ablation or through a controlled experiment where the same LLM receives vs. does not receive the GED information. Without this, the paper's central claim is a hypothesis rather than a demonstrated finding.

## Suggestions

1. **Most important:** Add an ablation that keeps the three-agent framework and prompts identical but omits the GED computation/communication. Compare explanation quality and modeling accuracy between EOR with and without GED. If the GED adds value, the full EOR should outperform. This single experiment would resolve the main weakness.

2. Clarify the integration mechanism: show a concrete prompt template or provide an example of how the normalized GED value or the graph comparison result is presented to the LLM, and how it influences the output.

3. Define "optimization outcomes" precisely: does accuracy check objective value only, or also decision variable values?

4. Report number of experts, their qualifications, and inter-rater reliability for the blind expert evaluation.

5. Add statistical significance tests (e.g., bootstrap confidence intervals) for the main accuracy and explanation quality comparisons.

6. State whether an exact or approximate GED algorithm is used; briefly discuss complexity or provide runtime for the benchmark.

## Score and Decision

The paper tackles a practically important problem (explainability in OR optimization) and presents a multi-agent framework that achieves strong empirical results against reasonable baselines. The new benchmark is a genuine contribution to the field. However, the paper's central claimed novelty — that Decision Information quantification via graph edit distance enhances LLM-generated explanations — is not validated by the experimental design. The GED integration mechanism is unclear, and no ablation isolates its effect from the multi-agent framework. The remaining weaknesses (underspecified accuracy metric, missing expert evaluation details, no complexity discussion) are individually fixable but collectively reduce confidence.

The paper is a solid systems contribution with a benchmark contribution, but the core methodological claim about Decision Information requires substantiation. The issues are addressable in rebuttal/camera-ready.

MY FINAL SCORE: <score>6.0</score>
MY FINAL DECISION: <decision>Accept</decision>