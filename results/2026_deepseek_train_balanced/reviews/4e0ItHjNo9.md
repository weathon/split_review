Now I have all the evidence I need. Let me write the consolidated review.

## Summary

This paper proposes **principal counterfactual fairness**, a new fairness notion that uses principal stratification to require counterfactual fairness only for individuals whose protected attribute has no individual causal effect on the outcome. The paper derives statistical bounds (Lemma 1), testable necessary conditions for violation detection (Theorem 1), and a post-processing method to adjust decisions with minimal individual changes, proven consistent at the parametric rate (Theorems 3–4). The core idea — that fairness requirements should depend on whether the protected attribute causally affects the outcome of interest — is well-motivated and addresses a genuine gap in the counterfactual fairness literature.

## Strengths

- **Principled conceptual contribution via principal stratification**: The paper identifies and addresses a real gap — "which attributes and individuals should be protected" — that is rarely discussed in counterfactual fairness literature. Using principal stratification to condition fairness requirements on whether the protected attribute has an individual causal effect on the outcome is a novel and well-motivated approach. The disability-in-college-admissions vs. disability-in-athlete-selection contrast (Section 1, lines 12–14, 20–21) illustrates the problem clearly.

- **Sharp bounds under partial identification (Lemma 1)**: Because principal strata are unobservable (Section 3, line 74), the paper derives sharp upper and lower bounds on the fairness violation measures τ₀(x) and τ₁(x) (Equations 113–114, 119–120). This makes an inherently partially-identified fairness notion operational, which is a technically substantive advance over standard counterfactual fairness that assumes full identifiability.

- **Testable necessary conditions for violation detection (Theorem 1)**: The concrete inequality conditions (Equations 127–128, 133–134) give practitioners a falsification test using only observable data, which is directly useful for auditing deployed systems.

- **Post-processing method with rate-optimal theoretical guarantees (Theorems 3–4)**: The paper proves consistency of the post-processing estimator at the parametric rate \(O_p(1/\sqrt{n})\) using doubly robust estimation (Theorem 2), providing robustness to model misspecification — a stronger guarantee than typical fairness post-processing methods.

## Weaknesses

### Fatal

None.

### Major

- **No baseline comparisons in experiments.** The experimental section (Section 5) evaluates the post-processing approach entirely in isolation. There is no comparison to standard counterfactual fairness post-processing, simpler alternatives (e.g., random flips, ignoring the sensitive attribute), path-specific counterfactual fairness, or any other method. Without baselines, the reported percentage changes in PCF and CF are uninformative — they could reflect trivial behavior that any reasonable method would achieve. For a paper that presents a new-method contribution, this is a critical evidential gap.

- **Thin empirical evaluation relative to claimed scope.** The paper claims "extensive experiments" (Section 1, line 22) but provides only: (a) one synthetic experiment whose data-generating process is unspecified (Section 5.1, ~3 sentences), where the "varying models and estimators" referenced in Table 3 are never enumerated in the text; and (b) one real-world dataset (OULAD) with a single sensitive attribute (disability). No standard errors, confidence intervals, or uncertainty quantification are reported for any metric. This is insufficient to support the paper's methodological claims or to demonstrate generalizability across domains.

- **Framing overclaim relative to partial identification.** The paper repeatedly states that the post-processing approach can **achieve** principal counterfactual fairness (abstract line 4, intro line 22, conclusion line 249). However, as the paper itself acknowledges (Section 6, line 249), principal counterfactual fairness is "partially identified" — the bounds-based approach can *falsify* fairness (detect violations when bounds exclude zero) but can *never confirm* that an algorithm satisfies the true unobservable condition. Theorems 3–4 prove consistency to the optimal solution *of the defined optimization problem*, but this optimization problem itself is solving a partially-identified constraint. The framing of "achieving" fairness overstates what the method can establish, especially for readers who may not closely parse the limitation paragraph.

### Minor

- **No practical guidance on choosing among the four definitions.** The paper proposes four variants of principal counterfactual fairness ordered "from weakest to strongest" (Section 3, line 70): principal counterfactual parity (Definition 4), principal conditional counterfactual fairness (Definition 5), principal counterfactual equalized odds (Definition 6), and principal counterfactual fairness (Definition 7). The bounds (Lemma 1) and necessary conditions (Theorem 1) are derived for Definition 6, while the post-processing targets Definition 7, and the experiments only evaluate Definition 7's metric. The paper never discusses the trade-offs: which definition a practitioner should use when, whether weaker definitions have narrower bounds and better detectability, or whether the choice affects the difficulty of verification.

- **Under-described implementation details for the real-world experiment.** The real-world pipeline (Section 5.2, lines 235–242) learns a CPDAG via PC algorithm, then "sampl[es] four DAGs from the learned CPDAG corresponding to the four cases of no subgroup, X₁ as subgroups, X₂ as subgroups, and both" — but the connection between sampling DAGs and defining subgroups is not explained. The steps that produce specific subgroup partitions from the DAGs are unclear, making the experiment difficult to reproduce or assess.

- **No discussion of the ignorability assumption's plausibility in the experiments.** Assumption 1 (line 108) requires \(A \perp\!\!\!\perp (Y(1),Y(0),D(1),D(0)) \mid X\), which is a strong unconfoundedness condition. The paper does not discuss whether this assumption is plausible in either the synthetic or the real-world setting, nor does it address sensitivity to violations.

- **Corollary 1 is technically correct but essentially trivial** — it states that principal counterfactual fairness reduces to standard counterfactual fairness when the protected attribute has no individual causal effect on outcomes for all individuals. This is an immediate consequence of the definitions and is presented with inflated significance.

### Trivial

None.

## Nice-to-Haves

- The synthetic experiment would benefit from a clear specification of the data-generating process (sample sizes, number of replications, parameter values) to enable reproducibility.
- The paper could discuss the computational complexity of solving the optimization-based post-processing for each \(x \in \mathcal{X}\).
- The authors could discuss how to obtain or validate the causal graph needed to determine which variables are covariates X versus outcomes Y, and whether uncertainty in causal discovery propagates to the fairness conclusions.

## Removed Points

These points were raised by the reviewers but removed after cross-checking against the paper:

- *Criticism about Table 1 being described but not visible*: This is a PDF extraction artifact, not a paper flaw.
- *Criticism about garbled objective function in Section 4.3*: This is a parser issue from text extraction.
- *Criticism about missing appendix/related works*: Parser strips these; they exist in the original submission.
- *Strength about "empirical validation on both synthetic and real-world data with a rigorous pipeline"*: The strength finder overstates the rigor of the experiments; the validation is thin rather than rigorous.
- *Criticism about the mapping between population-level and individual-level definitions not being discussed*: This is a nuanced technical point that, while valid, is too fine-grained to warrant inclusion as a distinct weakness.
- *Criticism about the example disconnect (coarse motivating example vs. fine-grained solution)*: The paper's framework correctly handles this; the supposed disconnect is more about presentation than substance.

## Novel Insights

The reviews surface a tension that the paper does not fully resolve: the paper proposes four definitions but develops theory (bounds, necessary conditions) for a middle-strength definition (principal counterfactual equalized odds, Definition 6) while targeting the strongest definition (individual-level, Definition 7) in its post-processing method and experiments. This asymmetry — where the identification results are for one definition but the implementation targets a different one — means the paper never formally connects which of its theoretical results apply to which definition. A practitioner reading the paper would need to reconstruct which bounds, conditions, and guarantees apply to their chosen definition. This structural gap is worth the authors' attention even though it does not invalidate the individual technical results.

## Suggestions

1. **Add at least 2–3 baseline methods** to the experiments: standard counterfactual fairness post-processing, a simple "ignore the sensitive attribute" baseline, and path-specific counterfactual fairness (Chiappa, 2019). Show that the proposed method achieves higher PCF with fewer decision changes relative to these baselines.

2. **Use additional real-world datasets** with different types of sensitive attributes and outcomes (e.g., UCI Adult, COMPAS) to demonstrate generalizability across domains with different causal structures.

3. **Specify the synthetic data-generating process** (sample sizes, parameters, number of replications, the models and estimators used) and report all metrics with standard errors or confidence intervals over multiple random seeds.

4. **Add practical guidance** on which of the four definitions (Definitions 4–7) to use in practice. Explain the trade-off between definition strength and identifiability.

5. **Reconcile the framing** with the partial-identification limitation: use more precise language such as "enforcing no-detectable-violation" or "optimizing for the identified constraints" rather than "achieving" fairness.

## Score and Decision

<score>4.0</score>
<decision>Reject</decision>