## Summary
# Final Review Report

## Summary

This paper proposes EvA, an evolutionary (genetic algorithm) attack for graph neural networks that directly optimizes edge perturbations in discrete space without gradients. The method addresses several limitations of gradient-based attacks: it avoids discrete-to-continuous relaxation, removes the need for differentiable proxy losses, works in a black-box setting, and uses a sparse encoding with memory linear in the attack budget. The authors demonstrate EvA on semi-supervised node classification under evasion attacks, evaluating it on CoraML, Citeseer, and PubMed with GCN, GPRGNN, APPNP, and GAT models. EvA achieves consistently lower perturbed accuracy than state-of-the-art gradient-based methods like PRBCD and LRBCD, with gains of 5–20 percentage points at moderate budgets. The method also enables two novel attack objectives: reducing randomized-smoothing-based certified ratios and breaking conformal prediction coverage on graphs. However, the paper overstates several claims (e.g., "fixes all five issues"), contains an internal evidence contradiction in the transductive setting results, understates the query-complexity cost (512K forward passes vs ~500 for PRBCD), and the "first attack" claims for certificates and conformal prediction cannot be verified without external literature. The limitations section omits critical caveats about targeted-attack degeneracy and wall-clock time trade-offs.

## Strengths
**S1. Methodological novelty — solving discrete optimization without gradients.** The core idea of using a genetic algorithm to directly optimize edge perturbations in the discrete {0,1} space is a clean departure from the dominant gradient-based paradigm. This eliminates the relaxation gap that plagues methods like PRBCD and avoids the need for differentiable proxy losses. The approach is principled and well-motivated by the discrete nature of graph perturbations.

**S2. Sparse encoding with linear memory complexity.** The proposed sparse encoding (storing only edge indices of perturbations rather than dense gradient blocks) is a practical engineering contribution. It reduces memory from O(N²) to O(|S|·δ), where δ is the attack budget and |S| the population size, enabling larger populations and faster batched evaluation on small-to-medium graphs.

**S3. Broad and consistent empirical evaluation.** The paper evaluates EvA across three datasets (CoraML, Citeseer, PubMed), four model architectures (GCN, GPRGNN, APPNP, GAT), six perturbation budgets, and both inductive and transductive settings. The consistent pattern of improved attack effectiveness over PRBCD and LRBCD supports the core thesis that search-based attacks have been underexplored.

**S4. Demonstration of novel attack objectives.** The ability to directly optimize non-differentiable objectives (certified ratio, conformal coverage/set size) is a genuine advantage of the black-box GA approach. The paper provides proof-of-concept experiments showing that EvA can reduce certified ratios below MLP baselines and break conformal coverage, opening new research directions for graph adversarial attacks.

**S5. Honest about key limitation (query cost).** While the limitations section could be expanded, the acknowledgement that EvA "uses many forward passes" is an important disclosure. The batch-stacking technique partially mitigates this for small graphs, and the authors identify query efficiency as a future direction.

## Weaknesses
**W1. Overclaimed general superiority contradicted by own data.** The paper repeatedly claims EvA "outperforms SOTA" across all settings, but Table 1 (Page 13, Appendix A) shows that in the transductive setting at higher budgets (ε≥0.15), EvA does **not** outperform PRBCD or LRBCD — results are within one standard deviation or slightly worse (e.g., GCN ε=0.15: EvA 59±3 vs PRBCD 60±2). This is a direct factual contradiction between a stated claim and the reported data, which undermines the paper's credibility.

**W2. Unverifiable "first attack" claims.** The paper claims "the first graph certificate attack" and "the first conformal attack on graphs" (Page 2, Introduction). Without external literature verification (unavailable in this run), these priority claims cannot be confirmed. The claims should be qualified with scope boundaries and "to the best of our knowledge" phrasing.

**W3. Query cost discrepancy significantly understated.** EvA requires |S|·T forward passes (default: 1024×500 = 512K) versus ~500–600 for PRBCD. The Limitations section (Page 10) mentions "many forward passes" but does not quantify this 1000× cost difference. Any practical deployment must weigh this cost against the marginal improvement in attack effectiveness.

**W4. Crossover design creates budget waste.** The crossover operator concatenates halves of parent perturbation vectors, which can produce duplicate edge indices in the child vector. Since duplicates are no-ops during XOR evaluation, a fraction of the budget is effectively wasted. The paper does not analyze or mitigate this inefficiency.

**W5. Certificate attack evaluation methodology unclear.** The paper uses "adaptive sampling" during search (resampling only the symmetric difference), which the authors acknowledge is "statistically flawed" (Page 19, § D). However, it does not clearly specify whether the final reported certified ratios (Fig. 4, right) use this same method or a statistically rigorous full-resampling protocol. This ambiguity affects trust in the certificate attack results.

**W6. Targeted attack limitation is critical but buried.** The paper correctly notes that with binary (0-1) accuracy as fitness, the GA degenerates to random search for targeted attacks (discussed in §5, not in Limitations). This is a serious limitation that should be prominently disclosed and is currently underemphasized.

**W7. Cross-reference error in Fig. 4.** The text on Page 9 states conformal coverage is shown "as shown in Fig. 4 (right)" but the coverage plot is on the left panel. The right panel shows certificate results. This factual error should be corrected.

## Key Issues
**Issue 1 (Critical) — Factual contradiction: transductive results do not support "EvA outperforms SOTA" claim.**
- **Anchor:** Page 13, Appendix A, Table 1 + surrounding text "Consistent with other experiments, here also EvA outperforms SOTA."
- **Evidence:** Table 1 shows at GCN ε=0.15: EvA 59±3 vs PRBCD 60±2 (PRBCD better); at GCN ε=0.20: EvA 57±3 vs PRBCD 56±2 (tied); at GPRGNN ε=0.20: EvA 50±16 vs PRBCD 50±13 (tied). In the transductive setting, EvA does NOT consistently outperform SOTA at higher budgets.
- **Impact:** This is a direct claim-data contradiction. If uncorrected, it damages the paper's factual credibility and can lead reviewers to question whether similar selective reporting occurs elsewhere.
- **Fix:** Replace the claim with an accurate description of transductive results. Acknowledge that while EvA excels in the inductive setting (which is the paper's main focus), transductive results are mixed at higher budgets with overlapping standard deviations.

**Issue 2 (Major) — Memory complexity claim is inconsistent across paper.**
- **Anchor:** Page 1 claims O(ε·E); Page 4 correctly derives O(|S|·ε·|E[Vatt:V]|).
- **Impact:** The Page 1 version omits the population size factor |S|, making the memory appear independent of the algorithm's key parameter. Since gradient-based methods like PRBCD with block size B have O(B) memory, the comparison becomes misleading without stating that |S| and B may differ by orders of magnitude.
- **Fix:** Standardize to O(|S|·δ) with δ=ε·|E[Vatt:V]| across all occurrences.

**Issue 3 (Major) — Unquantified query cost disparity.**
- **Anchor:** Page 10, Limitations — "EvA uses many forward passes." No quantification.
- **Impact:** The default EvA configuration (|S|=1024, T=500) requires ~512K forward passes. PRBCD requires ~500-600 forward passes (500 epochs + 100 fine-tune). This 1000× cost factor is not disclosed in the main text, and the Limitations section understates it as "many forward passes." A practitioner choosing between methods cannot make an informed trade-off.
- **Fix:** Add a dedicated paragraph quantifying the cost and showing a cost-effectiveness Pareto plot.

**Issue 4 (Major) — Certificate attack evaluation protocol is ambiguous.**
- **Anchor:** Page 19, § D states adaptive sampling is "statistically flawed" and not used for final evaluation. But Page 7 and Fig. 4 description do not state what evaluation protocol generated the reported certified ratios.
- **Impact:** If reported ratios in Fig. 4 used the flawed adaptive sampling, the results may underestimate the true certified ratio, overstating attack effectiveness. If full resampling was used, the paper must specify m (number of MC samples) and the statistical bound used.
- **Fix:** Explicitly state evaluation protocol in Section 5.1 or experimental setup.

**Issue 5 (Major) — "First attack" claims unverifiable.**
- **Anchor:** Page 2, Introduction — "first graph certificate attack" and "first conformal attack on graphs."
- **Impact:** Without external literature verification, these claims of priority are unsubstantiated and may be contested during review. Different interpretations of "certificate attack" or "conformal attack" could invalidate the claim.
- **Fix:** Add qualifiers: "To the best of our knowledge, under the inductive evasion setting with L0-budgeted edge perturbations..." and then discuss potential overlap with known related work.

## Actionable Suggestions
### Must-Fix Items (Publication-Critical)

**S1. Correct the transductive claim (Issue 1).**
- Revise Page 13, Appendix A text from "EvA outperforms SOTA" to a nuanced statement. Example:
  "In the transductive setting, EvA shows larger improvements at low budgets (ε≤0.05) but produces comparable or overlapping results at higher budgets (ε≥0.15), consistent with the known flaw of transductive robustness evaluation discussed in §2."
- This single fix addresses the most damaging credibility issue in the paper.

**S2. Standardize memory complexity claim (Issue 2).**
- Revise Page 1 from "O(ε·E)" to "O(|S|·ε·|E[Vatt:V]|) where |S| is the population size and δ = ε·|E[Vatt:V]| is the perturbation budget." Ensure Page 4 uses the same expression.

**S3. Add query-cost disclosure and cost-effectiveness analysis (Issue 3).**
- In the Experiments section (Page 8), add one sentence: "With default settings (|S|=1024, T=500), EvA performs ~512K forward passes per attack run, compared to ~500 for PRBCD. A cost-effectiveness comparison is provided in Appendix §D.3."
- In Limitations (Page 10), replace "many forward passes" with: "EvA requires 2-3 orders of magnitude more forward passes than gradient-based attacks (~512K vs ~500 for PRBCD with default parameters), which may be prohibitive in query-limited scenarios."

**S4. Clarify certificate attack evaluation protocol (Issue 4).**
- In Section 5.1 (Page 7) or the certificate experiment description (Page 9), add: "All reported certified ratios in Fig. 4 were obtained using full m=10,000 independent MC samples with a 95% Clopper-Pearson lower bound, following the standard certificate evaluation protocol [Bojchevski et al., 2020]. The adaptive sampling strategy described in §D was used only during the attack search phase to reduce computation, not for the final reported results."

**S5. Qualify priority claims (Issue 5).**
- Change "first graph certificate attack" to "first attack on randomized-smoothing-based graph certificates under the L0-budgeted evasion setting, to the best of our knowledge."
- Change "first conformal attack on graphs" to "first attack on conformal prediction sets for inductive GNNs via edge perturbations, to the best of our knowledge."

### Nice-to-Have Items (Quality Improvements)

**S6. Add deduplication after crossover (Page 3).**
- After crossover, deduplicate the child vector and pad with random non-duplicate indices to fully utilize the budget.

**S7. Add statistical significance tests (Page 8).**
- Report wins/ties/losses or paired p-values across the 5 data splits for EvA vs PRBCD.

**S8. Add a "Cost-Effectiveness Pareto" figure.**
- Replace/diversify Fig. 8 to show a Pareto frontier: x-axis = relative query cost, y-axis = accuracy reduction. This helps readers understand the cost-benefit trade-off.

**S9. Expand Limitations section (Page 10).**
- Restructure into bullet points with concrete numbers, as described in the annotation on Page 10.

**S10. Fix Fig. 4 cross-reference (Page 9).**
- Change "Fig. 4 (right)" to "Fig. 4 (left)" when referring to conformal coverage.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction (Page 1-2) uses a "list of problems → EvA fixes all" structure. The first paragraph enumerates five gradient-based limitations in a dense list, then claims to "fix all five." The second paragraph gives a GA overview. The third paragraph (Page 2) discusses imperceptibility, local budget, and then introduces the novel certificate/conformal attacks. This structure has three issues: (a) the list-of-problems format reads more like a related-work critique than a motivating narrative; (b) the transition from "fix all five" to "novel objectives" is abrupt; (c) the core message — that discrete optimization can be solved directly — is buried in the middle of the first paragraph.

### Best Storyline Candidate (Recommended)

**Arc:** Big Picture → Core Insight (discrete vs continuous gap) → GA Solution → Sparse encoding enabler → Novel objectives as consequence → Empirical preview → Contribution summary.

**Abstract Outline (5 sentences):**
- **S1 (Problem):** "Graph neural networks are vulnerable to small structural perturbations, but existing gradient-based attacks suffer from a fundamental limitation: they relax the inherently discrete edge-perturbation problem into a continuous optimization, creating a gap between the relaxed and true objectives."
- **S2 (Gap):** "This relaxation gap is compounded by the need for differentiable proxy losses, white-box access, and O(N²) memory, which restrict both the effectiveness and applicability of gradient attacks."
- **S3 (Method):** "We propose EvA, an evolutionary attack that directly optimizes discrete edge perturbations using a genetic algorithm, eliminating relaxation, proxy losses, and white-box requirements."
- **S4 (Key result):** "Across three datasets and four architectures, EvA reduces GNN accuracy by 5–20 percentage points more than the strongest gradient-based attack (PRBCD) at equivalent budgets, while using O(δ) memory linear in the perturbation budget."
- **S5 (Novelty enabler):** "By operating on any black-box objective, EvA naturally extends to non-differentiable goals, enabling the first attack on randomized-smoothing certificates and on conformal prediction sets for graphs."

### Introduction Outline (4 Paragraphs)

**P1 — The discrete optimization gap (Problem + Key Insight)**
- Role: Establish the importance of GNN robustness, then frame the core limitation of gradient attacks as a *discrete-to-continuous relaxation gap*, not merely as a list of engineering inconveniences.
- Claim: Gradient-based attacks optimize a relaxed continuous problem, so their solutions are structurally suboptimal even before considering proxy losses or white-box access.
- Transition: "We argue that this relaxation is unnecessary — the discrete perturbation space can be searched directly."

**P2 — Evolutionary search as a natural fit (Solution Idea)**
- Role: Introduce EvA's GA approach at the conceptual level (population-based discrete search without gradients).
- Claim: A genetic algorithm operating directly on edge indices can explore the discrete space more effectively because it avoids relaxation and can directly optimize any objective.
- Key detail: Sparse encoding (O(δ) per individual) makes this feasible.
- Transition: "This black-box access not only improves attack effectiveness but also enables fundamentally new attack objectives."

**P3 — Novel objectives enabled (Certificate + Conformal Attacks)**
- Role: Explain that by removing the differentiability requirement, EvA can directly optimize complex, non-differentiable goals like certified ratio and conformal coverage.
- Claim: These are the first demonstrations (to the best of our knowledge) of attacks on graph certificates and conformal GNNs.
- Transition: "We evaluate EvA across standard benchmarks to quantify its advantage."

**P4 — Empirical preview + Contribution Summary**
- Role: Summarize experimental scope (3 datasets, 4 architectures, inductive/transductive) and the key finding (consistently lower accuracy than PRBCD/LRBCD). State contributions concisely.
- Transition: "We detail the method in §3 and results in §6."

### Comparison with Current Storyline

| Aspect | Current | Recommended |
|---|---|---|
| Problem framing | "5 issues" list format | Single core concept (discrete vs continuous gap) |
| Core insight delivery | Middle of P1 | Opening of P2, clearly separated |
| Novel objectives | Appear as afterthought in P2-P3 | Given their own dedicated paragraph (P3) |
| Empirical promise | Vague ("outstanding effectiveness") | Specific (5-20 pp improvement range) |
| Memory complexity | O(ε·E) imprecise | O(δ) with δ defined |
| Readability | Dense, problem-list heavy | Clear arc: insight → solution → enabler → evidence |

## Priority Revision Plan
### Ranked Defect Board (Highest Risk First)

```text
Rank | Defect | Type | Validity Risk | Fix Difficulty | Effort | Confidence
-----|--------|------|-------------|---------------|--------|----------
#1   | Transductive claim contradicts data (Table 1) | Critical | High | Low (text fix) | 30 min | High
#2   | Inconsistent memory complexity (O(ε·E) vs O(|S|·δ)) | Major | Medium | Low (standardize) | 30 min | High
#3   | Unquantified query cost (512K vs 500 passes) | Major | Low (disclosure) | Low (add paragraph) | 1 hr | High
#4   | Certificate attack eval protocol unclear | Major | Medium | Medium (add text) | 2 hr | Medium
#5   | "First attack" claims unverifiable | Major | Medium | Low (add qualifiers) | 30 min | High
#6   | Crossover creates duplicate budget waste | Minor | Low | Low (add dedup) | 2 hr | Medium
#7   | No statistical significance tests | Minor | Low | Medium (add tests) | 4 hr | Medium
#8   | Fig. 4 cross-reference error (left vs right) | Minor | Low | Low (fix text) | 5 min | High
```

### Revision Order and Expected Impact

**Phase 1 (High Impact, Low Effort, ~1 day total):**
1. Fix transductive claim (Page 13) — eliminates critical credibility risk.
2. Standardize memory complexity (Page 1 and Page 4) — removes internal inconsistency.
3. Add query-cost disclosure (Page 10 Limitations) — prevents reviewer pushback on practicality.
4. Qualify "first attack" claims (Page 2) — avoids priority disputes.
5. Fix Fig. 4 reference (Page 9) — simple typo correction.

**Phase 2 (High Impact, Medium Effort, ~2-3 days):**
6. Clarify certificate attack evaluation protocol (Section 5.1 and Page 9) — resolves ambiguity about result validity.
7. Add deduplication after crossover (Section 3) — improves budget utilization and reproducibility.

**Phase 3 (Moderate Impact, Higher Effort, ~1 week):**
8. Add statistical significance testing (wins/ties/losses or paired p-values across 5 splits).
9. Add cost-effectiveness Pareto figure (Appendix) to show query-cost vs accuracy-reduction trade-off.
10. Expand and restructure Limitations section with concrete numbers.

### Expected Impact After Fixes
- **Credibility risk:** Eliminated (Issue #1 resolved).
- **Reproducibility risk:** Reduced (Issue #4, #6 resolved).
- **Practical adoption clarity:** Improved (Issue #3, #9 — readers can make informed cost-benefit decisions).
- **Novelty positioning:** Strengthened but still requires external literature verification.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | EvA vs PRBCD/LRBCD on vanilla GCN | CoraML, Citeseer, PubMed; inductive; 6 budgets (0.01-0.20); 5 splits | Perturbed accuracy | EvA achieves 5-20 pp lower accuracy | C1 (GA attack is more effective) | No significance tests; query cost not shown |
| E2 | EvA vs PRBCD on adversarially trained models | Same as E1, with robust training using LRBCD/PRBCD/EvA | Perturbed accuracy | EvA still outperforms across training methods | C1 (robustness to adversarial training) | Cross-training evaluation only; no adaptive attack analysis |
| E3 | Local constrained variant (EvA Local vs LRBCD) | CoraML, Citeseer, PubMed; ε_loc=0.5 | Perturbed accuracy + degree violation count | EvA Local better than LRBCD on most | C1 (local constraints feasible) | Degraded on PubMed; no termination analysis |
| E4 | Targeted attack (EvA vs PRBCD, budget 1-10) | CoraML GCN; per-node targeted; tanh-margin fitness | Failure count (NA nodes) | EvA fails on 2 vs PRBCD fails on 16 (budget=10) | C1 (targeted advantage at budget≥2) | PRBCD better at budget=1; fitness function is proxy |
| E5 | Certificate attack (certified ratio) | CoraML GPRGNN; robust training; B0,3; smoothing p=0.4 | Certified ratio, certified accuracy, smooth accuracy | Cert ratio below MLP at 5% budget | C3 (first certificate attack) | Evaluation protocol not fully specified |
| E6 | Conformal coverage attack | CoraML GCN; inductive; 1-α level | Coverage, set size | Coverage drops with budget; set size increases | C3 (first conformal attack) | Only one dataset; α not specified |
| E7 | Ablation: fitness functions (Acc vs CE vs MG) | CoraML GCN; global attack | Perturbed accuracy | CE is poor; MG ≈ Acc | C1 (GA works with any objective) | Only one dataset/model combination |
| E8 | Ablation: mutation type (UM vs TM vs ATM) | CoraML GCN; global attack | Perturbed accuracy | ATM best; TM better than UM | C1 (mutation strategy matters) | Only one dataset |
| E9 | Scaling analysis (population size, steps) | PubMed GCN; global attack | Accuracy vs steps | Larger population/steps improves EvA; PRBCD saturates | C1 (GA benefits from scaling) | Only one dataset |
| E10 | Memory/time analysis | PubMed; various configs | Wall clock, max memory, accuracy drop | EvA matches PRBCD at same wall time; improves with more time/memory | C2 (sparse encoding efficiency) | Only PubMed; GPU details not specified |

### Research-Theme Gap Diagnosis

- **New knowledge (core):** The main research-value claim — that discrete search-based attacks can outperform gradient-based methods — is partially supported by the inductive results but compromised by the transductive contradiction (Issue 1). This must be resolved.
- **Reproducibility:** The certificate attack evaluation protocol is ambiguous (Issue 4). The sparse encoding is clearly described, but the GA hyperparameter sensitivity is not fully explored (population size effect studied only on PubMed).
- **Impact on practice:** The query-cost barrier (512K forward passes) is not adequately disclosed, which limits practical adoption insights.

### Proposed Research Experiments

**P0 Experiment: Cost-controlled comparison (Must-fix, ~2 days)**
- **Target Claim:** C1 (EvA is more effective than gradient-based attacks)
- **Hypothesis:** EvA's advantage persists under matched query budgets (same number of forward passes)
- **Design:** Run EvA with T_EvA = 500 steps (512K passes) and PRBCD with T_PRBCD = 512K/|S_block| adjusted to match. Also run a low-budget EvA variant (|S|=64, T=100 → 6.4K passes) to find the crossover point where EvA ceases to be better.
- **Controls:** Same model, dataset, split, seed
- **Metrics:** Perturbed accuracy, wall-clock time, peak GPU memory
- **Success Criterion:** EvA still outperforms PRBCD under matched budgets OR the paper honestly reports the budget at which PRBCD catches up.
- **Expected Gain:** Eliminates the query-cost critique and demonstrates the method's true cost-effectiveness.

**P1 Experiment: Certificate attack evaluation protocol clarification (Must-fix, ~1 day)**
- **Target Claim:** C3 (certificate attack results in Fig. 4 are valid)
- **Design:** Rerun certificate attack evaluation with full m=10,000 MC samples and report the certified ratio with 95% Clopper-Pearson bounds. Compare with the adaptive-sampling estimate.
- **Controls:** Same perturbation, same model, same random seed
- **Success Criterion:** The difference between adaptive-sampling and full-evaluation certified ratios is < 2 pp.
- **Expected Gain:** Validates or corrects the certificate attack results and removes evaluation ambiguity.

**P2 Experiment: Statistical significance across splits (Nice-to-have, ~3 days)**
- **Target Claim:** C1 (consistent improvement)
- **Design:** For each dataset/budget/model combination, compute a paired t-test (EvA vs PRBCD) across the 5 splits. Report p-values or wins/ties/losses.
- **Success Criterion:** Majority of comparisons show p<0.05 significance.
- **Expected Gain:** Strengthens the empirical claims with statistical rigor.

### ASCII Diagram — Revision Strategy Roadmap

```text
[Issue #1: Transductive claim contradicts Table 1]
    -> Fix: Rewrite claim to match data (Low effort, High impact)
    -> Expected: Eliminates critical credibility risk

[Issue #2: Inconsistent memory complexity]
    -> Fix: Standardize to O(|S|·δ) everywhere (Low effort, Medium impact)
    -> Expected: Removes internal inconsistency

[Issue #3: Query cost understated]
    -> Fix: Quantify 512K vs 500 forward passes (Low effort, Medium impact)
    -> Expected: Honest disclosure prevents reviewer pushback

[Issue #4: Certificate attack protocol ambiguous]
    -> Fix: Specify evaluation MC protocol (Medium effort, High impact)
    -> Expected: Results become verifiable

[Issue #5: "First attack" unverifiable]
    -> Fix: Add scope qualifiers (Low effort, Medium impact)
    -> Expected: Avoids priority disputes
```

### ASCII Diagram — Experiment Upgrade Plan

```text
P0 (Must, ~2 days): Cost-controlled comparison
    EvA (|S|=1024, T=500) vs PRBCD (matched passes)
    Also: Low-budget EvA (|S|=64, T=100)
    -> Validates C1 under fair comparison

P1 (Must, ~1 day): Certificate eval protocol
    Full MC resampling (m=10K) vs adaptive sampling
    -> Validates C3, removes ambiguity

P2 (Nice, ~3 days): Statistical significance
    Paired t-test over 5 splits per setting
    -> Supports C1 with statistical rigor
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Scoring rationale (research value + novelty prioritized):**

- **Research value (7/10):** The paper demonstrates a genuine and important insight — that discrete search-based attacks can outperform gradient-based methods on the standard inductive benchmark. The novel attack objectives (certificates, conformal) open underexplored areas. However, the value is partially offset by: (a) the transductive claim-data contradiction that weakens trust, (b) the 1000× query cost that limits practical deployment, and (c) the absence of statistical significance testing.

- **Novelty (6/10):** The GA-for-graph-attacks idea is conceptually novel in the graph adversarial community but technically an application of a well-known metaheuristic (genetic algorithm). The sparse encoding is a practical contribution. The certificate/conformal attacks are genuinely novel objectives, though their "first" claims cannot be verified in this run. Overall, the novelty is moderate — the core insight is solid but incremental in terms of algorithmic contribution.

- **Validity/Soundness (6/10):** The inductive results are consistent and well-executed. However, the transductive contradiction (Issue 1), ambiguous certificate evaluation protocol (Issue 4), and inconsistent memory complexity claims (Issue 2) reduce the overall soundness score. The paper would benefit from a more thorough, self-critical presentation of limitations.

- **Reproducibility (7/10):** The method is described in sufficient detail (GA components, encoding, hyperparameters in Appendix C). The code is promised on OpenReview. The sparse encoding mapping function (Eq. 2) and crossover/mutation operations are clearly specified. Minor issues: the certificate evaluation protocol needs clarification, and the deduplication after crossover is not specified.

- **Presentation (6/10):** The writing is generally clear but has room for improvement. The introduction's "list of five problems" structure is less engaging than a unified narrative. There is a factual cross-reference error (Fig. 4 left vs right). The hype language ("outstanding effectiveness", "fixes all five issues") should be toned down. The Limitations section needs expansion.

**Post-Revision Target: [7.0, 7.5] / 10**

- If the transductive contradiction is corrected (Issue 1), the query cost is honestly disclosed (Issue 3), and the certificate protocol is clarified (Issue 4), the score would rise to ~7.0.
- If statistical significance tests and a cost-effectiveness Pareto analysis are also added, the score could reach ~7.5.
- The upper bound is constrained by the moderate algorithmic novelty (GA is a well-known metaheuristic) and the unverifiable "first attack" claims, which cannot be fully resolved without external literature.