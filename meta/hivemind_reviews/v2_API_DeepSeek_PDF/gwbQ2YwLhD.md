## Summary
# Final Review Report

## Summary

This paper (published at ICLR 2024) investigates how the scale/measurement units of variables affects score-based DAG structure learning algorithms. The authors prove that under the Gaussian additive noise model, the Model Mean Squared Error (MMSE) — and consequently log-likelihood based losses such as BIC and ELBO — can be minimized by structurally incorrect DAGs when variables are measured on different scales. The theoretical analysis covers d-dimensional chains, forks, and colliders, providing exact variance-ordering conditions under which the MMSE favors the wrong graph. Empirical experiments on synthetic and real-world (Sachs protein-signaling) data confirm that four prominent structure learners (NOTEARS, GES, DAG-GNN, GraN-DAG) predict systematically wrong substructures under scaled data, even in non-linear settings and when only a single variable is scaled. The paper also proposes a Scale Robust Loss (SRL) that removes free variance terms for root nodes, showing improved robustness for discrete learners like GES.

The paper makes a valuable contribution by generalizing prior results (Loh & Buhlmann 2014; Reisach et al. 2021) from linear 2-node settings to d-dimensional and non-linear cases, and by demonstrating that log-likelihood based losses inherit the same vulnerability under the Gaussian assumption. The work is well-motivated, technically rigorous within its assumptions, and supported by extensive experiments. However, key limitations include: (i) theoretical results restricted to three structural primitives (chains, forks, colliders), (ii) strong dependence on the Gaussian noise assumption for log-likelihood claims, (iii) the proposed SRL solution only applies to discrete learners, not the continuous learners most affected, and (iv) limited real-world validation without known ground truth. Novelty/comparison claims require external literature verification that was unavailable in this review run.

## Strengths
1. **Clear, well-motivated research question.** The paper identifies a genuine and practically important vulnerability in score-based structure learning — that variable scaling can systematically mislead DAG learners. The medical example (Page 2, Figure 1) effectively illustrates the real-world stakes of this problem.

2. **Rigorous theoretical extension of prior results.** Propositions 2-6 provide the first exact variance-ordering conditions for d-dimensional chains, forks, and colliders under MMSE optimization, going significantly beyond prior work which focused on linear 2-node systems. The proof sketches are conceptually clear and the full proofs are provided in the appendix.

3. **Extension to log-likelihood based losses.** Propositions 7-10 formally connect the MMSE sensitivity to widely used losses (BIC, ELBO) under the Gaussian noise assumption. This is an important contribution because most practitioners use BIC/ELBO without being aware of this vulnerability.

4. **Comprehensive experimental validation.** The paper systematically answers four empirical questions (Q1-Q4) with extensive synthetic and real-world experiments. The 100% failure rates for NT/DG/GND under scaling are striking and convincingly demonstrate that the effect is not a rare edge case. The GES/SRL results (Tab. 1) provide a constructive proof-of-concept that the vulnerability can be mitigated.

5. **Transparent limitation discussion.** The paper honestly acknowledges the scope limitations of its theoretical results (chains/forks/colliders only) and the practical limitations of SRL (discrete learners only). This transparency is commendable.

6. **Well-structured presentation.** The paper flows logically from problem motivation → assumptions → theoretical analysis → practical mitigation → experiments → conclusion. Figures and tables are clear and directly support the narrative.

## Weaknesses
**1. Theoretical results restricted to three structural primitives (Major).** Propositions 2-6 are proven only for chains, forks, and colliders (Assumption A1). Remark 1 claims decomposition allows reasoning about "far more complex graphs," but this decomposition argument is not formally proven. In real DAGs, overlapping substructures interact through shared nodes, and the global MMSE is not a simple additive combination of substructure losses. The empirical Q3 results partially address this gap but do not replace theoretical proof.

**2. Log-likelihood claims depend critically on Gaussian noise assumption (Major).** Propositions 7-10 show that BIC, ELBO, and general log-likelihood losses are susceptible to scaling *only under the Gaussian noise assumption*. For non-Gaussian noise models (e.g., Poisson, categorical, heavy-tailed), the log-likelihood does not reduce to MMSE, and the scale-sensitivity argument does not carry over. The paper does not discuss this boundary, and the wording (e.g., "all log-likelihood based losses are susceptible") overstates the scope.

**3. SRL only applies to discrete learners — the most affected methods are excluded (Major).** The proposed Scale Robust Loss requires knowing which nodes have no parents, which is only feasible for discrete structure learners (like GES). The continuous learners most affected by scaling (NOTEARS, DAG-GNN, GraN-DAG) cannot use SRL because during early optimization all variables have at least one parent. The paper defers this to future work without concrete suggestions.

**4. Table 1 interpretation is ambiguous (Major).** The table shows 100% entries across all three prediction columns for NT on chain ground truth, implying the same algorithm predicts chain, fork, *and* collider simultaneously — which is structurally impossible unless the predicted graph contains multiple disconnected components. The table needs clarification on whether columns represent substructure detection within larger graphs or entire predicted graphs.

**5. Missing variance/confidence reporting across experiment repetitions (Major).** Table 1 reports percentages without confidence intervals or standard deviations. With 30 repetitions, "50%" could mean 15/30 correct — but without variance the reader cannot assess whether this figure is stable or fluctuates substantially across data realizations.

**6. Real-world evaluation uses circular protocol (Minor).** The Sachs dataset has no known ground truth. The evaluation protocol (run SL algorithm → get G → scale data → check if G' appears) depends on the algorithm's own initial prediction. This makes the SHD comparisons suggestive but not conclusive about correctness of structure learning.

**7. Novelty and positioning claims cannot be externally verified in this run.** Due to Retrieval-Disabled Mode, the paper's novelty relative to the full literature on varsortability, variance-based identifiability, and score-based DAG learning cannot be independently verified. The claims appear plausible but require manual literature check.

## Key Issues
### Ranked Error Board (highest risk first)

| Rank | Issue | Severity | Validity Risk | Fixability | Annotation ID |
|------|-------|----------|---------------|------------|---------------|
| 1 | Theoretical scope limited to chains/forks/colliders (A1) | Major | High — decomposition claim unproven | Partial — add formal decomposition proof or explicit scope disclaimer | P3-A1 |
| 2 | Log-likelihood claims depend on Gaussian noise without qualifier | Major | High — overstatement to "all log-likelihood losses" | Easy — add explicit Gaussian qualifier in claims | P6-Prop7-10 |
| 3 | SRL inapplicable to continuous learners most affected | Major | Medium — solution does not address core affected methods | Hard — requires new research | P7-SRL |
| 4 | Table 1 interpretation ambiguous | Major | Medium — misreading could inflate confidence | Easy — clarify column semantics and add CI | P8-Tab1 |
| 5 | Experiment repetition variance not reported | Major | Medium — cannot assess statistical reliability | Easy — add std/CI to percentages | P8-Q1 |
| 6 | Real-world evaluation uses circular protocol | Minor | Low — results still informative as sensitivity analysis | Medium — add synthetic ground-truth validation alongside | P9-Q4 |
| 7 | Introduction lacks clear gap statement | Minor | Low — harms readability but not validity | Easy — restructure first paragraph | P1-Intro |
| 8 | Abstract merges multiple claims without separation | Minor | Low — clarity issue | Easy — restructure abstract into 4 explicit sentences | P1-Abstract |
| 9 | Medical example depends on specific threshold | Minor | Low — illustrative purpose clear | Easy — add caveat about threshold dependence | P2-Medical |
| 10 | MMSE definition uses non-standard 1/(2n) factor | Minor | Low — does not affect results | Easy — clarify or standardize to 1/n | P4-Def1 |

## Actionable Suggestions
### Revision: Abstract (Page 1)
**Problem:** The abstract merges three contributions into a dense flow without clear separation and does not qualify the Gaussian noise assumption for log-likelihood claims.

**Recommended action:** Restructure into four explicit sentences: (S1) Problem + stakes, (S2) Prior gap, (S3) This paper's d-dimensional conditions and non-linear/log-likelihood extension (with Gaussian qualifier), (S4) Key finding + bounded implication.

**Mentor Revised Version:**
"Structure learning aims to recover the Directed Acyclic Graph (DAG) underlying observed data, but prevalent score-based learners rely on least-square or log-likelihood losses that are sensitive to variable scaling. Prior work established this sensitivity only for linear, low-dimensional settings. We generalize these results to d-dimensional chains, forks, and colliders, providing exact variance-ordering conditions under which the model mean squared error (MMSE) is minimized by a wrong DAG. We further show that, under the Gaussian noise assumption, log-likelihood based losses (BIC, ELBO) inherit this scale sensitivity, and that the effect persists for non-linear dependencies. Our experiments on synthetic and real-world protein-signaling data confirm that measurement scale can systematically mislead continuous structure learners, while discrete learners can be made scale-robust through normalization and free-variance exclusion."

### Revision: Introduction Paragraph 1 (Page 1)
**Problem:** The opening paragraph is too broad — 5 background sentences before reaching the paper's focus.

**Recommended action:** Compress background into 2 sentences and state the concrete gap: MMSE contains free variance terms for root nodes, making scale a confound.

**Mentor Revised Version:**
"Given a finite data sample, structure learning aims to recover the Directed Acyclic Graph (DAG) underlying the data-generating distribution — a task critical in medicine, biology, and causal inference. Score-based methods, popularized recently by NOTEARS, optimize a loss such as the log-likelihood, which under Gaussian noise reduces to the mean squared error across all variables (the model MSE, or MMSE). A key but often overlooked property is that the MMSE contains free variance terms for variables modeled as root nodes. This creates an unsuspected vulnerability: variable scaling can shift which graph minimizes the MMSE, potentially favoring structurally incorrect DAGs. Understanding when and why this occurs, especially beyond low-dimensional linear settings, is the focus of the present work."

### Revision: Related Work (Page 2-3)
**Problem:** List-like structure without comparison axes; misses explicit positioning relative to varsortability (Reisach et al.).

**Recommended action:** Restructure into two subsections: (2.1) Identifiability and Variance, (2.2) Empirical Scale Sensitivity. Explicitly state how this paper differs.

### Revision: Proposition 2-6 scope caveat (Page 5)
**Problem:** The paper states that decomposition allows reasoning about complex graphs but does not prove this. Proposition 2 only establishes pairwise dominance, not global optimality.

**Recommended action:** Add a remark after Proposition 2:
"We emphasize that Proposition 2 establishes pairwise dominance of the reversed chain over the true chain; it does not claim that the reversed chain is the global MMSE minimizer among all DAGs. Characterizing the global minimizer under arbitrary variance orderings remains an open problem."

### Revision: Proposition 7-8 — add Gaussian qualifier (Page 6)
**Problem:** The statement "optimizing the MMSE is equivalent to optimizing the log-likelihood" only holds under Gaussian noise.

**Recommended action:** Restate Proposition 8 as:
"Proposition 8. Under the same Gaussian-noise assumptions of Proposition 7, any log-likelihood based loss L(x,θ) = Σ log p(x_i|θ) + h(·) reduces to the MMSE plus a term h(·). Consequently, L(x,θ) inherits the MMSE's susceptibility to variable scaling when the noise is Gaussian. For non-Gaussian noise models, the equivalence does not hold and scale sensitivity requires separate analysis."

### Revision: Table 1 (Page 7)
**Problem:** The table showing 100% entries across all three columns for NT is ambiguous.

**Recommended action:** Add a clarifying footnote: "Each cell shows the proportion of runs where the *predicted graph contained a substructure* of the type indicated by the column header. Since multiple substructure types can appear in the same predicted graph, row percentages may sum to more than 100%." Also add ± bootstrapped confidence intervals.

### Revision: SRL section (Page 7)
**Problem:** SRL only applies to discrete learners; no path forward for continuous learners.

**Recommended action:** Add a sentence sketching a potential direction: "For continuous learners, a scale-robust objective could be achieved by reweighting each variable's MSE contribution by an estimate of its noise variance, or by constraining W columns during optimization to penalize free variance terms. Developing and validating such objectives is an important direction for future work."

### Revision: Conclusion (Page 9)
**Problem:** Generic limitations, overbroad future work.

**Recommended action:** Replace with three specific open problems: (i) extending theoretical conditions to general DAGs, (ii) scale-robust losses for continuous learners, (iii) non-Gaussian noise analysis.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current paper follows the structure: Background → Related Work → Assumptions → Theoretical Analysis → Mitigation → Experiments → Conclusion. This is a logical, standard structure for a theoretical-empirical paper. The main weakness is in the Introduction, which opens with generic DAG/BN background and takes too long to reach the paper's specific gap.

### Abstract Outline (Complete)

- **S1 (Problem/Domain):** Structure learning is crucial but prevalent DAG learners use MSE/log-likelihood losses.
- **S2 (Prior Gap):** Prior work only showed scale sensitivity for linear 2-node systems.
- **S3 (This Paper):** We provide d-dimensional conditions for MMSE failure and show log-likelihood losses (BIC, ELBO) are also susceptible under Gaussian noise.
- **S4 (Method/Evidence):** Empirical confirmation on synthetic and real-world data.
- **S5 (Bounded Implication):** Discrete learners can be made robust via normalization + variance exclusion.

### Introduction Outline (Complete)

- **P1 (Motivation + Gap):** Define structure learning task. State the overlooked property — MMSE contains free variance terms for root nodes, making scale a confound. Clearly state: "We investigate when and why this occurs beyond low-dimensional linear settings."
- **P2 (Prior Work + Gap Elaboration):** Loh & Buhlmann (2014) and Reisach et al. (2021) establish linear, low-dim sensitivity. The gap: d-dimensional, non-linear, log-likelihood losses.
- **P3 (Contribution Statement):** (C1) Exact variance-ordering conditions for d-dimensional chains/forks/colliders. (C2) Log-likelihood vulnerability under Gaussian noise. (C3) Empirical confirmation with SRL mitigation.
- **P4 (Medical Example + Roadmap):** Brief example showing practical stakes. Then: "We proceed by stating assumptions, establishing theoretical results, and validating empirically."

### Recommended Storyline Improvement

The current storyline requires the reader to wait until Paragraph 2 of the Introduction to understand the specific gap. A stronger narrative would front-load the gap description. I recommend the following restructured Introduction:

**Candidate A (Recommended):**
1. **Hook + problem definition (2 sentences):** DAG structure learning is vital yet flawed — the MMSE loss is known to be scale-sensitive.
2. **Concrete gap (2-3 sentences):** Prior work only studied this in linear 2-node settings. Real problems have dozens of variables and use log-likelihood losses.
3. **Our insight (2 sentences):** The root cause is that MMSE contains free variance terms for root nodes. Scale determines which nodes become root nodes.
4. **Contributions (3 items):** (C1) d-dimensional conditions, (C2) log-likelihood extension, (C3) experiments + SRL.
5. **Roadmap (1 sentence):** "We proceed with assumptions, theory, experiments, and conclusion."

**Candidate B (Alternative):**
Start with the medical example (Figure 1) as an opening vignette to immediately establish stakes, then define the gap, then contributions.

### Three Alignment Checks for Current Storyline vs Candidate A

| Check | Current | Candidate A |
|-------|---------|-------------|
| Problem alignment | Gap stated in P2, after background | Gap stated in P1 |
| Variable alignment | "MMSE" introduced in P1 | Same, with better motivation |
| Contribution-evidence alignment | Good across experiment section | Same |
| Narrative readability | Background-heavy start | Faster engagement |

## Priority Revision Plan
### P0 — Must Address (Publication-Critical)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P0 | Log-likelihood claims overstate scope (Gaussian assumption not explicit) | Add explicit Gaussian qualifier to Propositions 7-10 and contribution statements | Prevents reviewer rejection based on overclaim |
| P0 | Table 1 ambiguous interpretation (100% across all columns) | Clarify column semantics, add footnote explaining multiple substructures, add confidence intervals | Prevents reader confusion and potential misinterpretation |
| P0 | Proposition 2 only shows pairwise dominance, not global optimality | Add explicit caveat after Proposition 2 (see suggested text in Actionable Suggestions) | Honest scope disclosure prevents overclaim |
| P0 | Missing variance reporting across experiment repetitions | Add std dev or bootstrapped CI to Table 1 percentages | Allows statistical reliability assessment |

### P1 — Should Address (Major Quality Improvement)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P1 | SRL only works for discrete learners; no path for continuous learners | Add concrete future direction (e.g., variance-reweighted MSE) | Shows authors are aware of the practical gap and have a plan |
| P1 | Decomposition claim (Remark 1) is unproven | Tone down Remark 1: state that extension to arbitrary DAGs is an open problem | Prevents overclaim and improves scientific honesty |
| P1 | Abstract lacks structure and Gaussian qualifier | Restructure into 4 explicit sentences (see Actionable Suggestions) | Clearer communication of scope |
| P1 | Related work is list-like | Reorganize by comparison axes; discuss varsortability explicitly | Strengthens novelty positioning |

### P2 — Nice to Have (Quality Polish)

| Priority | Issue | Action | Expected Impact |
|----------|-------|--------|-----------------|
| P2 | Medial example threshold dependence | Add caveat that 0.49 vs 0.51 difference is example-specific | Minor clarity improvement |
| P2 | MMSE definition with 1/(2n) factor | Use standard 1/n or explain 1/2 choice | Notation clarity |
| P2 | Conclusion generic future work | Replace with 3 specific open problems | More actionable |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective / Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|----------------------|-------|---------|--------------|-----------------|-------------------|
| Q1 | Confirm theoretical findings: scale determines predicted structure | Synthetic {3,10}-node chains/forks/colliders, linear/non-linear, 3 scales × 10 trials | Graph substructure prediction match rate | NT/DG/GND 100% fail; GES partial; GESR improves | C1 (d-dim conditions) | Only chains/forks/colliders; no CI |
| Q2 | Severity when subset of variables scaled | Same setup, scale only subset A | Proportion of runs with wrong fork/collider | Single-node scaling with ≥2 neighbors causes 100% failure (NT/DG/GND) | C1 (practical severity) | GES results hard to interpret |
| Q3 | Ablation of (A1) — complex DAGs | 20 random 10-node DAGs, 3-node substructures identified | Substructure prediction accuracy | 100% affected for NT/DG/GND; GES ~20% | C1 (generalization beyond A1) | Only 20 base DAGs |
| Q4 | Real-world impact | Sachs protein-signaling (Sachs et al. 2005) | SHD, substructure presence | 100% severe effects (except GES); higher SHD under scaling | C3 (real-world confirmation) | No ground truth; circular protocol |

### Research-Theme Gap Diagnosis

**New knowledge:** The paper contributes novel theoretical conditions (variance ordering) for MMSE failure in d-dimensional chains/forks/colliders. This is a genuine advance over prior 2-node results. However, the new knowledge is bounded by the strong assumptions (A1, A2, Gaussian noise).

**Reproducibility:** The paper provides code and deterministic seeds. Reproducibility is strong.

**Impact on practice/understanding:** The paper shows practitioners that scaling matters for continuous DAG learners even with log-likelihood losses. But without a practical solution for continuous learners, the actionable impact is limited to suggesting data normalization — which practitioners may already do.

### Proposed Research Experiments (P0/P1/P2)

| Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Est. Cost | Expected Gain |
|-------------|------------|---------------|----------|---------|------------------|-----------|---------------|
| P0: Table 1 reliability | 50% for GESR is stable | Bootstrap 10k resamples from existing 30 runs | N/A (uses existing data) | 95% CI width | CI width < 10% | 1 day | Statistical rigor |
| P1: Non-Gaussian scale sensitivity | Scale affects log-likelihood losses for non-Gaussian noise | Synthetic Poisson and t-distributed noise data, test GES+BIC vs GES+SRL | Gaussian baseline | Wrong substructure rate | Effect size similar to Gaussian case | 1 week | Broader scope |
| P1: Continuous-learner SRL proxy | Column-wise variance weighting reduces scale bias | Modify NT loss: ||X-XW||²_F + λΣ||W[:,j]||₁·Var(X_j)^{-1} | Standard NT on scaled data | SHD, correct edge rate | Improvement ≥20% in SHD | 2 weeks | Practical mitigation |
| P2: More complex DAGs | A1-based conditions extend to random DAGs | 100 random DAGs, 50 nodes each, repeat Q1-Q3 protocol | 20-DAG baseline | Substructure error rate | Effect persists for ≥80% of DAGs | 2 weeks | Generalization evidence |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

*Rationale:* The paper provides a meaningful theoretical extension of prior results (Loh & Buhlmann 2014; Reisach et al. 2021) from linear 2-node systems to d-dimensional chains/forks/colliders and from square losses to log-likelihood based losses under Gaussian noise. The experimental demonstration is thorough and the 100% failure rates for continuous learners are striking. However, the theoretical scope is restricted to three structural primitives (decomposition claim unproven), the log-likelihood claims are not qualified sufficiently for non-Gaussian settings, the proposed mitigation (SRL) does not apply to the most affected methods, and experimental reporting lacks variance statistics. The core contribution is a rigorous characterization of an important vulnerability, but the practical impact is limited by these scope constraints.

**Post-Revision Target: [7.0, 8.0] / 10**

*Rationale:* If the P0 items are addressed — (1) explicit Gaussian qualifier in all log-likelihood claims, (2) Table 1 clarification with confidence intervals, (3) scope caveat for global optimality of reversed chain, (4) variance reporting for experiment repetitions — the manuscript becomes significantly more defensible. Addition of even one concrete suggestion for continuous-learner robustness (P1) could raise confidence further. The upper bound reflects the inherent limitation that the theoretical results are proven only for chains/forks/colliders; fully general DAG analysis would require substantially more work beyond the scope of this revision cycle.