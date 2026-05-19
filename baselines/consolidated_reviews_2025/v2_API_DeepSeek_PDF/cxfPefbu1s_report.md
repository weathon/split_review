## Summary
# Final Review Report

## Summary

This paper (published at ICLR 2024) addresses the problem of "disguised procedural unfairness" in algorithmic fairness — the inadvertent alteration of neutral data generating components when enforcing fairness constraints on objectionable ones. The authors draw on Rawls' theory of pure procedural justice to motivate two requirements: (I) no arbitrary alterations on neutral components, and (II) inequalities arranged to benefit the least advantaged. They propose a decoupling framework consisting of (a) a value instantiation rule that assigns reference points (fixed input values) to objectionable causal edges while keeping neutral edges' inputs unchanged, and (b) a configuration procedure that optimizes these reference points to maximize favorable outcomes for the least advantaged.

The paper makes a conceptually valuable contribution by diagnosing an overlooked problem — that existing causal fairness methods (path-specific effects, counterfactual fairness) can introduce unjustified changes to neutral causal mechanisms. The proposed reference-point framework offers a principled alternative. However, the paper has significant limitations: (1) the framework assumes a known, correctly specified causal graph with causal sufficiency and modularity — strong assumptions; (2) the reference point optimization via simulated annealing has no optimality guarantees; (3) experiments compare against only one baseline without statistical significance reporting; (4) the framework lacks guidance on how to identify objectionable components in practice; and (5) novelty verification requires external literature comparison that was not available in this review run.

**Retrieval-Disabled Mode Note:** External paper search was unavailable in this run. Therefore, novelty and comparison conclusions (including SOTA positioning and prior-work overlap assessment) are explicitly deferred for manual verification. The review below is grounded solely in manuscript-internal evidence.

## Strengths
1. **Important problem diagnosis.** The paper identifies a genuinely overlooked issue — disguised procedural unfairness — where enforcing causal fairness constraints can inadvertently alter neutral components of the data generating process in arbitrary, unjustifiable ways. This diagnosis is clearly illustrated with a linear example showing parameter deviations in neutral edges.

2. **Principled philosophical grounding.** The connection to Rawls' pure procedural justice and the formalization of two requirements (Fair Equality of Opportunity and the Difference Principle) provides a coherent normative framework for evaluating procedural fairness in data generating processes. This bridges an important gap between philosophical concepts of fairness and technical ML implementation.

3. **Clean decoupling mechanism.** The value instantiation rule (Algorithm 1) is a technically sound approach for addressing objectionable components at the input level while preserving the learned causal mechanisms. The recognition that reference points should be assigned to edges (not variables) is a subtle and important insight, especially when the same variable is the tail of multiple edges with different objectionability statuses.

4. **Edge-specific intervention framing.** By connecting the value instantiation rule to the edge intervention literature (Shpitser & Tchetgen 2016), the paper correctly situates its contribution within the causal inference framework and makes clear how procedural fairness can be achieved without re-estimating causal effects.

5. **Broad definition of objectionable components.** Moving beyond protected features to include any edge in the causal graph (e.g., height → income, accent → evaluation) increases the practical applicability of the framework to a wider range of discrimination scenarios.

## Weaknesses
### W1. Strong causal assumptions without validation (Major)
The framework assumes a correctly specified causal graph, causal sufficiency (no hidden confounders), and causal modularity. These assumptions are stated but not tested or relaxed. In real-world fairness applications (e.g., hiring, lending), the true causal graph is rarely known with certainty, and hidden confounding is the norm rather than the exception. The paper does not analyze how misspecification of the graph or violation of causal sufficiency affects the decoupling quality. This limits the practical applicability of the framework.

### W2. Insufficient empirical validation (Major)
The experiment on UCI Adult compares against only one baseline (Chiappa 2019). No comparison with Kilbertus et al. (2017), Nabi & Shpitser (2018), or the simple parameter-dropping approach (Section 4.1). No standard errors, confidence intervals, or significance tests are reported. The approval rate differences — the main empirical evidence — could be within the noise range. The Folktables experiment (mentioned but deferred to appendix) is not discussed in the main text.

### W3. Reference point optimization lacks guarantees (Major)
Equation (4) defines an optimization over the Cartesian product of tail-node domains. For continuous variables, this is infinite-dimensional. The paper uses simulated annealing (Appendix D.1.1), a heuristic with no convergence guarantees to global optimality. No analysis of solution quality (e.g., how close the found reference points are to the true optimum, sensitivity to initialization) is provided.

### W4. No guidance for identifying objectionable components (Minor)
The framework requires that the set of objectionable edges (EObj) be specified in advance, but no criteria or methodology is provided for determining objectionability. This leaves practitioners without operational guidance and creates a risk of arbitrary or inconsistent application.

### W5. Contribution structure has overlaps (Minor)
The three listed contributions are not mutually exclusive: revealing disguised procedural unfairness is a diagnosis, the value instantiation rule is a technical solution, and the Rawlsian configuration is an application of the same framework. This could be consolidated into two sharper contributions.

### W6. Overclaiming in comparison table (Minor)
Table 1 claims "✓" for all fairness dimensions for the proposed approach, but empirical support is only provided for "Address disguised procedural unfairness" and partially for "Individual-level evaluation." Claims about "Not depend on causal effect identifiability" and "Individualized mitigation" are not substantiated by experiments or formal analysis in the paper.

## Key Issues
### Issue 1: Empirical validation is insufficient to support the claimed practical advantages
**Severity: Major | Location: Page 9 - Experiments 5.2**

The UCI Adult experiment compares against only one baseline (Chiappa 2019's Path-Specific Counterfactual Fairness). The paper claims "offering boosts of approval rates" but does not report standard errors, confidence intervals, or significance tests. Without uncertainty quantification, the reported improvements could be artifacts of a single data split or optimization run. The comparison against Chiappa (2019) is also limited because that method was designed for counterfactual fairness, not for optimizing approval rates for the least advantaged — the comparison may not be apples-to-apples.

**Required Fix:** Report approval rates with at least 3 random seeds with mean±std. Add at least 2 more baselines (parameter-dropping from §4.1, Nabi & Shpitser 2018 constrained optimization). Include statistical significance tests (paired t-test or permutation test) comparing proposed method's least-advantaged-group approval rate against each baseline.

### Issue 2: Reference point optimization has no theoretical guarantees
**Severity: Major | Location: Page 8 - Equation (4), Appendix D.1.1**

The reference point configuration is defined as an optimization problem over the Cartesian product of tail-node value domains. Simulated annealing is used without optimality guarantees. The paper's scalability demonstration (Table 2, 1024 variables) only measures the forward-pass cost, not the annealing search cost, which could be orders of magnitude larger for complex graphs with many objectionable edges.

**Required Fix:** Add analysis of optimization complexity. For discrete domains, discuss exhaustive search feasibility. For continuous domains, discuss gradient-based alternatives when the pipeline is differentiable. Report the number of simulated annealing iterations and convergence diagnostics for the experiments.

### Issue 3: Strong causal assumptions without sensitivity analysis
**Severity: Major | Location: Page 5-7 - Method (Sections 4.1-4.2)**

The framework assumes a correct causal graph, causal sufficiency, and causal modularity. These assumptions are standard in causal inference but are particularly consequential here because an incorrect graph could misidentify which edges are objectionable, leading to procedural unfairness through a different mechanism than the one the framework aims to prevent.

**Required Fix:** Add a sensitivity analysis or discussion section that addresses: (a) What happens when the graph is misspecified? (b) Can the approach be extended to settings with hidden confounding (e.g., using ADMGs or selection bias corrections)? (c) Are there diagnostic checks to detect violations of causal sufficiency or modularity?

### Issue 4: Conclusion lacks specific limitations
**Severity: Minor | Location: Page 9 - Conclusion**

The conclusion references Appendix E for limitations but does not enumerate them in the main text. This is a missed opportunity for scientific transparency, as readers who skip the appendix may overestimate the framework's applicability.

**Required Fix:** Add a concise limitations paragraph in the main conclusion covering: (a) dependence on correct causal graph, (b) heuristic optimization for reference points, (c) need for pre-specified objectionable components, (d) single-baseline experiment.

## Actionable Suggestions
### S1. Strengthen the experimental section
**Priority: Must (P0)**
- **Action:** Add at least 2 more baselines: (a) simple parameter-dropping approach from Section 4.1, (b) Nabi & Shpitser (2018) constrained PSE optimization.
- **Action:** Report mean approval rates ± standard deviation over 5 random seeds for each method.
- **Action:** Add a paired permutation test comparing the least-advantaged-group approval rate of the proposed method against each baseline. Report p-values.
- **Action:** Add the Folktables dataset results to the main text (currently only in appendix).
- **Expected benefit:** Addresses the most critical weakness — insufficient empirical validation. Without this, the claimed practical advantages are not convincingly demonstrated.

### S2. Add reference point optimization analysis
**Priority: Must (P0)**
- **Action:** Report the number of simulated annealing iterations used, convergence criteria, and final objective function values for each experiment.
- **Action:** For the UCI Adult experiment, report the actual reference point values learned (e.g., what specific value was assigned to sex along A→Y and marital status along M→Y).
- **Action:** Add a sensitivity analysis showing how the choice of reference points affects the approval rates (e.g., a grid of reasonable values and corresponding outcomes).
- **Expected benefit:** Makes the optimization transparent and reproducible. Without this, the optimization remains a black box.

### S3. Operationalize objectionable component identification
**Priority: Should (P1)**
- **Action:** Add a brief subsection or paragraph discussing criteria for labeling edges as objectionable: legal mandates, stakeholder input, evidence of disparate impact, or Rawlsian analysis.
- **Expected benefit:** Increases practical applicability and reduces risk of arbitrary usage.

### S4. Address causal assumption sensitivity
**Priority: Should (P1)**
- **Action:** Add a paragraph discussing what happens when the causal graph is misspecified. For example, if a true confounder is missing, the reference point assigned to an objectionable edge may not actually decouple the objectionable influence.
- **Action:** Discuss extension to settings with hidden confounding (directed mixed graphs) or suggest a robustness check using multiple plausible graphs.
- **Expected benefit:** Improves scientific credibility by acknowledging and bounding the assumption space.

### S5. Consolidate contribution claims
**Priority: Nice-to-have (P2)**
- **Action:** Restructure the three bullet contributions into two: (1) diagnosis of disguised procedural unfairness, (2) decoupling framework (value instantiation rule + reference point optimization).
- **Mentor Revised Version:**
  Our contributions are: (1) We identify and formalize disguised procedural unfairness — the inadvertent alteration of neutral data generating components when enforcing causal fairness constraints — showing violations of Rawls' principles. (2) We propose a decoupling framework comprising a value instantiation rule that assigns reference points to objectionable causal edges while preserving neutral components, configured to benefit the least advantaged.

### S6. Add specific limitations to conclusion
**Priority: Should (P1)**
- **Action:** Replace the generic future-work sentence with a 3-4 sentence limitations paragraph covering: (a) dependence on correct causal graph and causal sufficiency, (b) heuristic optimization for reference points, (c) need for pre-specified objectionable components, (d) limited experimental validation against few baselines.
- **Expected benefit:** Improves scientific transparency and prevents over-claiming.

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current introduction has three paragraphs: (1) literature survey on fairness notions, (2) definition of procedural fairness and critique of existing methods, (3) expansion on discrimination examples and contribution list. The main weakness is that the narrative starts with a dense literature list without establishing stakes, and the gap ("under-characterized data generating process properties") is stated abstractly without a concrete motivating example until Section 3.

### Abstract Outline (Recommended Revision)

**S1 - Problem and Domain:** "Automated decision-making systems should be procedurally fair, meaning the processes generating predictions must themselves satisfy fairness requirements, not only the outcomes."

**S2 - Prior Work Gap:** "Existing causal fairness notions, while procedurally motivated, ultimately enforce fairness through outcome-level constraints and can inadvertently alter neutral components of the data generating process in arbitrary, unjustifiable ways — an overlooked issue we term disguised procedural unfairness."

**S3 - Proposed Solution:** "We propose a decoupling framework consisting of a value instantiation rule that assigns reference points to objectionable causal edges while preserving neutral ones, combined with an optimization procedure that configures these reference points to maximize favorable outcomes for the least advantaged individuals."

**S4 - Key Result:** "On a simulated example and the UCI Adult dataset, our approach increases approval rates for disadvantaged groups without altering neutral causal mechanisms, outperforming a path-specific counterfactual fairness baseline."

**S5 - Bounded Implication:** "This work shows that preventing disguised procedural unfairness requires explicitly controlling objectionable components while keeping neutral components intact — a design principle applicable to any causal fairness approach."

### Introduction Outline (Recommended Revision)

**Paragraph 1 - Stakes and Problem:** "Automated decision systems determine access to credit, employment, and social services. For these decisions to be fair, the procedures generating predictions must be justifiable, not only the outcomes. [CITE examples of algorithmic harm]. However, existing fairness notions, including causal approaches, focus on outcome-level metrics."

**Paragraph 2 - Gap:** "This paper identifies a specific, overlooked failure mode: disguised procedural unfairness. When fairness constraints are enforced on objectionable causal pathways, neutral components can be inadvertently altered in arbitrary ways. We show this violates Rawls' requirement that procedures should not be influenced by arbitrary contingencies."

**Paragraph 3 - Proposed Solution Preview:** "Our framework addresses this by decoupling objectionable from neutral components at the input level. The value instantiation rule assigns fixed reference points to objectionable edges, configured to benefit the least advantaged."

**Paragraph 4 - Contributions (consolidated):** "Contributions: (1) Diagnosis of disguised procedural unfairness with formalization through Rawlsian requirements. (2) A decoupling framework with edge-specific reference points and benefit-maximizing configuration."

### Alternative Storyline Options

**Option A: Problem-First (Recommended)** — Open with a concrete failure example (the linear model disguised unfairness), then generalize. This hooks readers immediately.

**Option B: Principle-First** — Open with Rawls' pure procedural justice, then map to algorithmic fairness. Better for philosophy-oriented audiences but risks alienating ML readers.

**Option C: Method-First** — Open with the value instantiation rule, then motivate why it is needed. Less recommended because the "why" precedes the "what" in effective scientific writing.

## Priority Revision Plan
```text
ASCII Diagram — Revision Strategy Roadmap

[W1: Insufficient empirical validation (P0)]
  -> [Fix: Add 2+ baselines, multi-seed stats, significance tests]
  -> [Expected impact: Convincing empirical support]

[W2: Reference point optimization lacks guarantees (P0)]
  -> [Fix: Report convergence, reference values, sensitivity analysis]
  -> [Expected impact: Transparency and reproducibility]

[W3: Strong causal assumptions (P1)]
  -> [Fix: Add sensitivity analysis for graph misspecification]
  -> [Expected impact: Credible assumption boundary]

[W4: No objectionable component guidance (P1)]
  -> [Fix: Add criteria discussion / subsection]
  -> [Expected impact: Practical applicability]

[W5: Overlapping contributions / overclaiming (P2)]
  -> [Fix: Consolidate to 2 contributions, qualify Table 1 checkmarks]
  -> [Expected impact: Clearer novelty positioning]
```

| Priority | Task | Section | Effort | Impact |
|----------|------|---------|--------|--------|
| P0 (Must) | Add statistical validation (multi-seed, CI, significance) | §5 Experiments | Medium | High |
| P0 (Must) | Add 2+ baselines (parameter-drop, Nabi & Shpitser) | §5 Experiments | Medium | High |
| P0 (Must) | Report reference point optimization details (iterations, values) | §4.2.2 + Appendix D | Low | High |
| P1 (Should) | Add causal assumption sensitivity discussion | §4 + New §6 | Low | Medium |
| P1 (Should) | Add limitation paragraph to conclusion | §6 Conclusion | Low | Medium |
| P1 (Should) | Add objectionable component identification guidance | §2 or New §4.3 | Medium | Medium |
| P2 (Nice) | Consolidate contribution claims | §1 Introduction | Low | Low |
| P2 (Nice) | Qualify overclaims in Table 1 | Appendix A Table 1 | Low | Low |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Demonstrate Requirement II violation (simulated linear model) | Linear model with variables (A,C,M,L,Y) from §3, ground truth parameters known | Approval rates by group across thresholds | Disadvantaged group suffers more rejections under all policies | C1 (diagnosis of disguised unfairness) | Only linear; ground truth known (unrealistic) |
| E2 | UCI Adult: compare proposed framework vs Chiappa (2019) | UCI Adult data, causal graph Fig 2(b), objectionable edges A→Y and A→M→Y | Group-wise approval rates for Y=0 and Y=1 subgroups | Proposed method increases approval for female (low-income) group vs baseline | C2 (value instantiation rule), C3 (benefit least advantaged) | Single baseline; no significance tests; no error bars |
| E3 | Scalability demonstration | Random graph with 1024 nodes, avg degree 102 | Parameter count, MAC operations | Computational cost comparable to vanilla regressor | Scalability claim | Only forward-pass cost; annealing optimization cost not included |

### Research-Theme Gap Diagnosis

- **New Knowledge (Weak):** The core conceptual contribution (diagnosis of disguised unfairness) is new and well-supported by the linear example. However, the technical contribution (value instantiation rule) is closely related to edge interventions in causal inference, and the paper does not empirically demonstrate substantial performance advantages over alternative approaches.
- **Reproducibility (Partial):** Code is provided, but the simulated annealing optimization details (iterations, convergence criteria, initialization) are under-specified, making exact reproduction difficult.
- **Impact on Practice/Understanding (Partial):** The paper successfully raises awareness of an overlooked problem, but the practical applicability is limited by strong causal assumptions and lack of guidance for identifying objectionable components.

### Proposed Research Experiments (P0/P1/P2)

```text
ASCII Diagram — Experiment Upgrade Plan

[E2: UCI Adult, one baseline, no stats (Current)]
   |
   v
[E2a: Add 2 baselines: parameter-drop + Nabi&Shpitser (P0)]
   |
   v
[E2b: 5 seeds, mean±std, permutation test (P0)]
   |
   v
[E2c: Report reference point values (P0)]
   |
   v
[E4: Folktables experiment in main text (P1)]
   |
   v
[E5: Graph misspecification sensitivity (P1)]
```

**Experiment E2a — Add baselines (P0)**
- **Target Claim:** C2 (Value instantiation rule advantages)
- **Hypothesis:** Proposed method outperforms both parameter-dropping (simple zeroing of objectionable coefficients) and Nabi & Shpitser (2018) constrained optimization in terms of approval rate for the least advantaged group.
- **Minimal Design:** Implement parameter-dropping: fit unconstrained model, set objectionable coefficients to zero, re-predict. Implement constrained PSE optimization: fit model with PSE bounded by ε=0.01.
- **Controls/Baselines:** Same data split, metric, and subgroup definitions as current paper.
- **Metrics:** Approval rate for female (Y=0) subgroup, approval rate for male (Y=0) subgroup.
- **Success Criterion:** Proposed method yields 5%+ higher approval rate for disadvantaged subgroup compared to both baselines, with p<0.05.
- **Estimated Cost:** 2-3 days for implementation + 1 day for analysis.

**Experiment E2b — Statistical validation (P0)**
- **Target Claim:** C3 (Benefit to least advantaged)
- **Hypothesis:** Observed improvements are statistically significant and stable across random seeds.
- **Minimal Design:** Run all methods (current + 2 new baselines) with 5 different random seeds. Compute mean and standard deviation of approval rates. Perform paired permutation test (1000 permutations) comparing proposed method vs each baseline on least-advantaged-group approval rate.
- **Metrics:** Mean±std approval rates, p-values.
- **Success Criterion:** At least p<0.05 for comparison against each baseline for the Y=0 subgroup.
- **Estimated Cost:** 1-2 days (automated re-runs).

**Experiment E4 — Folktables experiment (P1)**
- **Target Claim:** C2, C3 (Generalizability)
- **Hypothesis:** Results generalize to another dataset (Folktables PUBCOV prediction task as referenced in Appendix D.4).
- **Minimal Design:** Move the Folktables experiment from appendix to main text with same statistical rigor as proposed for E2b.
- **Metrics:** Same as E2b.
- **Success Criterion:** Consistent direction of improvement for least advantaged group.
- **Estimated Cost:** Already collected, only analysis/reporting needed.

**Experiment E5 — Graph misspecification sensitivity (P1)**
- **Target Claim:** Framework robustness
- **Hypothesis:** The decoupling quality degrades gracefully under graph misspecification.
- **Minimal Design:** For the simulated linear model, add/remove edges or misorient edges. Measure the impact on (a) the signed relative deviation of neutral parameters, (b) the approval rate for the least advantaged group.
- **Metrics:** Average deviation of neutral parameters, approval rate changes.
- **Success Criterion:** Graceful degradation (monotonic increase in error with misspecification severity).
- **Estimated Cost:** 3-5 days.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6/10**

**Rationale:** The paper makes a conceptually valuable contribution by identifying and formalizing disguised procedural unfairness — a genuinely overlooked issue in causal fairness. The proposed decoupling framework is technically sound and well-grounded in causal inference principles. However, the empirical validation is insufficient (single baseline, no statistical significance), the reference point optimization relies on heuristic search without guarantees, and the framework's strong causal assumptions are not tested or discussed. The score prioritizes research value (recognizing the novel problem diagnosis) while reflecting the validity concerns from limited experiments and the need for stronger empirical evidence.

**Post-Revision Target: [7.0, 7.8]/10**

If the P0 and P1 items are fully addressed (multi-baseline comparisons with proper statistics, reference point optimization transparency, assumption sensitivity analysis, and limitation discussion), the paper would reach a score of approximately 7.0-7.8/10. The upper bound is constrained by the inherent difficulty of validating causal assumptions in real-world fairness applications. A higher score would require demonstrating the framework on additional real-world datasets with diverse causal structures and providing formal guarantees for the reference point optimization.