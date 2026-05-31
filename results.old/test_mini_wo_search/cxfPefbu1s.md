Now I have a thorough understanding of the paper. Let me construct the consolidated review.

## Summary

This paper identifies *disguised procedural unfairness* — the problem that imposing causal fairness constraints can inadvertently alter neutral components of the data generating process — and proposes a framework to decouple objectionable components from neutral ones using reference points and a value instantiation rule. The framework is motivated by Rawlsian procedural justice, requiring (I) no arbitrary interference with neutral components and (II) configuration of reference points to benefit the least advantaged. Experiments on a simulated linear model and UCI Adult demonstrate the problem and show improved approval rates for disadvantaged groups compared to Path-Specific Counterfactual Fairness.

---

## Strengths

1. **Novel identification of disguised procedural unfairness.** The paper provides a concrete, well-illustrated diagnosis (Section 3, Figure 1) showing that existing causal fairness constraints (Kilbertus et al., Nabi et al., Chiappa) produce arbitrary deviations on neutral components — a subtle problem that prior work missed. The linear example (Section 3) cleanly demonstrates that different constraint formulations yield different arbitrary shifts on the same neutral coefficients, violating the requirement that procedure not be influenced by arbitrary contingencies.

2. **Principled decoupling via value instantiation rule.** Algorithm 1 specifies a clear, edge-specific procedure: inputs along objectionable edges receive reference points (fixed values), while inputs along neutral edges retain their original values (or propagate downstream from reference points). This directly prevents spillover onto neutral components, addressing Requirement I. The modular design (Algorithm 2) leverages causal modularity to apply the rule sequentially via topological sorting, avoiding the global parameter coupling that causes disguised unfairness in prior methods.

3. **Operationalization of the Difference Principle.** Equation (4) formulates reference point configuration as an optimization maximizing expected outcome for the least advantaged individuals. The UCI Adult experiment (Figure 2c) demonstrates a concrete improvement: compared to Path-Specific Counterfactual Fairness (which *reduces* approval rates for low-income females), the proposed method boosts approval rates for the least advantaged group.

4. **Empirical insight that objectionable components extend beyond protected features.** On UCI Adult, the optimal reference point for edge *M → Y* is "married" (not flipping sex), revealing that procedural fairness may require addressing components not centered on protected attributes — a nuance prior feature-flipping approaches miss.

---

## Weaknesses

### Fatal
None.

### Major

1. **Reference point optimization is underspecified and its practical instantiation is unclear (Section 4.2.2, Equation 4).** The paper states the optimization problem abstractly — maximize expected outcome for the least advantaged over the Cartesian product of tail-node domains — but provides no concrete algorithm, search strategy, discretization scheme, or convergence discussion. The UCI Adult experiment reports optimal reference points as "female" for *A → Y* and "married" for *M → Y*, yet the paper never explains *how* these values were obtained (e.g., grid search, exhaustive enumeration, gradient-based method). For edges with continuous parents, the search over a continuous domain is nontrivial and unaddressed. This gap matters because the paper's central claim of *configuring* reference points to benefit the least advantaged is only as strong as the optimization procedure that produces them.

2. **Limited experimental evaluation.** The real-world evaluation is restricted to one dataset (UCI Adult) and one causal fairness baseline (Path-Specific Counterfactual Fairness, Chiappa 2019) plus the unconstrained model. The experiments do not include comparisons to other causal fairness methods (e.g., Kilbertus et al., Nabi et al.) or report any predictive accuracy or cost metrics (e.g., false positive/negative rates, overall utility). While the paper's focus is procedural fairness, the complete absence of utility metrics makes it impossible to assess whether the boost in approval rates for the least advantaged comes at the cost of overall decision quality. In a loan-approval scenario, increasing approvals without regard to repayment ability is itself problematic. The evaluation demonstrates a proof of concept but falls short of establishing practical viability.

3. **No discussion of sensitivity to the choice of objectionable edge set.** The paper requires the set of objectionable edges as input but offers no principled criterion or guidance for practitioners to determine this set. The UCI Adult experiment follows prior work (Nabi et al., Chiappa) for problematic paths, but the paper does not explore how different choices of objectionable edges affect outcomes, nor does it discuss robustness to misspecification. Since the framework's output depends entirely on this set, leaving its selection unguided is a significant methodological gap.

### Minor

4. **Untested assumption of additive/decouplable mechanisms.** The value instantiation rule cleanly separates objectionable from neutral influence only when the causal mechanism is additive in its inputs. The paper acknowledges this limitation (Section 4.1: "If the model does not have additive structures…the decomposition…cannot be easily carried out") but does not test any non-additive settings (e.g., interactions between objectionable and neutral parents, nonlinearities in real-world data). The generality of the approach in realistic, non-additive DGPs remains unexamined.

5. **The linear example violation of the Difference Principle (Figure 3a) is illustrative but not evaluative.** It convincingly demonstrates that a problem exists but does not itself constitute a quantitative evaluation of the proposed method — it only motivates why decoupling is needed. This is a framing issue rather than a flaw, but the paper's empirical support for the difference principle claim rests heavily on this single simulation.

### Trivial
None.

---

## Nice-to-Haves

- **Computational cost / scalability.** The method requires fitting separate models for each local causal module (Algorithm 2), then solving a potentially high-dimensional optimization over reference points. A brief discussion of runtime or scaling behavior (even for the small UCI Adult model) would help practitioners assess practicality.
- **Ablation on objectionable edge selection.** An ablation showing how the set of objectionable edges affects both reference points and fairness/accuracy outcomes would strengthen confidence in the method.
- **Guidance on handling continuous-valued tail nodes** in the reference point optimization (e.g., discretization strategies, gradient-based optimization).

---

## Removed Points

These points are flagged to be removed; treat them with caution.

- **"The direct correction step contradicts the paper's stated goal"** (Harsh Critic's Section 4 criticism of Algorithm 1). The paper clearly states this option is only applicable "if there is additional assumption on the functional form and/or parameters" (Algorithm 1, lines 245–249) and notes in the main text that such information "may not be readily available" (lines 219–220). This does not contradict the goal; it is a conditional alternative. **Removed: strawman that misreads the paper.**

- **"Missing related work"** (implied by requests for more baselines like demographic parity, equalized odds). These are outcome-level, non-causal fairness notions that are outside the paper's scope. The paper's contribution is specifically about procedural fairness in the data generating process. **Removed: scope creep.**

- **"Reproducibility details missing (splits, seeds, hyperparameters)"** (Harsh Critic's Missing Parts). Per the review guidelines, the parser strips appendix and reproducibility statement sections from all papers; these exist in the original submission. **Removed: parser artifact.**

- **"Missing proofs in appendix" / "absent references"** — same as above; parser artifact. **Removed.**

- **"Overall the paper feels like a position paper with proof-of-concept"** — subjective opinion without a specific, verifiable anchor. **Removed.**

- **Strength: "Use of causal modularity to enable local intervention"** — this leverages a well-known property of SCMs (independence of causal mechanisms). The paper uses it correctly, but it is not a novel contribution specific to this paper. **Removed from Strengths** (but the modular design remains part of the paper's technical contribution).

---

## Novel Insights

The core idea of "disguised procedural unfairness" — that enforcing fairness on objectionable causal paths can introduce arbitrary and undocumented changes on *neutral* components — is a genuinely novel diagnostic lens. The reference point approach (intervening at the input level of local causal modules rather than constraining parameters) is a creative technical response that cleanly avoids parameter-level contamination. An interesting subtlety that emerges from the review is that the framework may be most impactful not as a drop-in replacement for existing causal fairness methods, but as a diagnostic tool to audit whether a given fairness intervention actually produces the intended procedural guarantees without side effects on neutral parts of the DGP.

---

## Suggestions

1. Provide a concrete algorithm for solving the reference point optimization (Equation 4) — even a simple enumeration for discrete domains with complexity analysis — and report how the UCI Adult reference points were actually computed.
2. Expand the experimental evaluation to at least one additional real-world dataset, include one more causal fairness baseline (e.g., Nabi et al.'s constraint-based approach), and report predictive accuracy alongside fairness metrics to characterize the utility trade-off.
3. Add a brief ablation varying the set of objectionable edges on the same dataset, showing how results change.
4. Discuss the robustness of the value instantiation rule when the causal graph is misspecified or when mechanisms contain interactions.

---

## Score and Decision

**Overall assessment:** The paper identifies a genuine and previously overlooked problem in causal fairness and proposes a well-motivated, principled framework to address it. The conceptual contribution — disguised procedural unfairness — is novel and important. However, the technical contribution is weakened by an underspecified optimization procedure and narrow experimental validation (one dataset, one baseline, no utility metrics). The paper reads more as a compelling research proposal with a proof-of-concept than a fully validated method. For ICLR's standards, the empirical support is insufficient to recommend acceptance.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>