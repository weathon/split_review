## Summary
# Final Review Report

## Summary

This paper proposes Scattered Forest Search (SFS), an inference-time search method for LLM-based code generation. The core idea is to reframe code generation as a black-box optimization problem over code space, where validation tests serve as the objective function and the LLM acts as the optimizer. SFS integrates three techniques: Scattering (generating diverse textual improvement directions before producing child solutions), Foresting (multi-start seed initialization with varied coding-style prompts), and Scouting (cross-branch sharing of insights via global memory). The method is evaluated on HumanEval, MBPP, APPS, CodeContests, and Leetcode benchmarks using GPT-3.5, showing improved pass@1 and pass@any rates, faster discovery of correct solutions, and higher solution diversity compared to best-of-N, line search, and tree search baselines.

**Key Strengths:** The paper introduces a well-motivated framework with a clear optimization perspective. The empirical evidence for improved solution diversity is solid, with multiple similarity metrics (BERT, TF-IDF, Levenshtein) consistently showing that SFS generates more diverse candidates. The ablation study cleanly isolates the contribution of each technique. The experiments span five benchmarks of varying difficulty, and the scaling curves convincingly show that SFS continues improving with additional budget while baselines plateau.

**Key Weaknesses:** (1) The theoretical analysis (Section 3.4) is a qualitative Markov chain analogy, not a rigorous proof — it invokes Cheeger's inequality without establishing reversibility or stationary distribution existence. (2) Self-generated validation tests have a 27.5% false negative rate, which substantially impacts pass@1 selection accuracy; the robustness claim is only partially supported. (3) Several claims are overstated ("parameter-free," "novel technique," theoretical demonstration). (4) The comparison with LATS in Appendix E shows that the relative advantage depends heavily on evaluation protocol, a nuance absent from the main text. (5) The conclusion makes unsupported claims about cost reduction and real-time applicability.

**Novelty verdict:** Deferred to manual verification (external literature search unavailable in this run). The core technical contribution — using LLM-generated textual improvement directions to diversify tree search branches — appears practically useful but may overlap with existing prompt engineering and evolutionary search methods for code generation.

## Strengths
**1. Clean optimization framing.** Reframing code generation as black-box optimization over code space is a conceptually useful perspective. It naturally motivates the need for diverse exploration (to avoid local optima) and provides a vocabulary (search directions, multi-start, feedback sharing) that makes the method design principled rather than ad hoc.

**2. Solid diversity evidence.** The paper provides multiple quantitative metrics (BERT cosine similarity, TF-IDF similarity, Levenshtein similarity, token sequence similarity) showing that SFS generates meaningfully more diverse solutions than baselines. The BERT similarity scores (0.9945 for SFS vs. 0.9998 for tree search on HumanEval in Table 6), while numerically close, are consistently lower across all benchmarks. The seed scattering experiment (Table 1, Section 3.5) is particularly compelling — even unrelated prompts like nonsense poetry improve solution diversity and pass@any rates.

**3. Clean ablation study.** The three-way ablation (Table 7) cleanly shows that each component contributes positively, with Scattering providing the largest individual gain (pass@1 drops from 82.5% to 75.6% when removed). This makes the method's internal logic transparent.

**4. Favorable scaling behavior.** The scaling curves (Figures 2, 12, 18) show that SFS continues improving up to ~20 solutions, while baselines plateau much earlier. This is practically important for users who can afford higher search budgets.

**5. Strong pass@any results.** The pass@any rates (Table 3) show that SFS discovers correct solutions substantially more often than comparable methods (89.0% vs. 83.1% for Line, 76.9% for Tree on HumanEval). Since pass@any reflects the search component (not the selection component), this directly validates the exploration improvement claim.

**6. Implementability.** The method is described with sufficient pseudocode (Appendix C) and does not require model fine-tuning or external tools beyond the LLM API. The approach is practical and reproducible for researchers with API access.

## Weaknesses
**W1. Overclaimed theoretical contribution.** Section 3.4 frames a qualitative Markov chain conductance analogy as a "theoretical analysis" and "theoretical explanation." In reality, no formal theorem, proof, or quantitative bound is provided. The conductance argument assumes a stationary distribution and reversibility without justification, and Cheeger's inequality is invoked without verifying the necessary conditions. The argument is at best an intuitive motivation, not a theoretical analysis. This overclaim should be corrected in revision.

**W2. High verifier noise undermines pass@1 reliability.** Self-generated validation tests have a 27.5% false negative rate and 33.75% total inaccuracy (Appendix Table 11). This means the search algorithm's selection mechanism frequently discards correct solutions. The paper claims robustness to validation noise based on pass@any, but pass@1 (the primary metric) improves by 6.5 percentage points when ground-truth tests are provided (Table 8), showing substantial sensitivity. The practical utility of SFS depends strongly on verifier quality, which is not fully acknowledged.

**W3. Comparison framing selective.** Table 4 reports LATS at 75.6% (HumanEval) under the "no ground-truth tests" setting, but Appendix Table 9 shows LATS achieves 83.8% under its original protocol with ground-truth checking — exceeding SFS's 82.5% in that same table. The main text does not reconcile this discrepancy. Similarly, Self-repair achieves 90.5% on HumanEval (Table 9), which is strong. The relative positioning of SFS depends heavily on evaluation setup, and the main text should be more transparent about this.

**W4. "Parameter-free" is inaccurate.** The method uses UCT with an exploration parameter $c$ (Eq. 1), a branching factor $k$, and a forest size $n$. Calling it "parameter-free" is misleading; the authors likely mean "no additional training hyperparameters," but even that is not strictly true since $c$ requires tuning.

**W5. Missing statistical rigor.** No variance, confidence intervals, or significance tests are reported. Many improvements in Tables 2-5 are within a few percentage points, which may overlap with random variation. For example, on MBPP+ (Table 2), SFS (65.7%) vs. Tree (65.4%) is a 0.3% gap — well within noise.

**W6. APPS evaluation uses a small, potentially unrepresentative sample.** Only 200 of 10,000 problems are sampled, without stratification by difficulty level. The APPS results (20.5% pass@1) may not reflect true performance, and the CodeContests results (4.24% pass@1) are so low that comparison across methods is statistically fragile.

**W7. Conclusion makes unsupported claims.** The conclusion claims SFS "could significantly reduce computational costs" and is "attractive for large-scale deployments, especially in real-time applications" — but no cost, latency, or throughput measurements are reported. SFS requires 2 LLM API calls per solution (Appendix C.6), making it more expensive per solution than BoN (1 call). These claims are speculative and should be removed or properly qualified.

## Key Issues
**Issue 1: Theoretical overclaim without formal substance (severity=high, fixable).**
- Anchor: Page 5-6, Section 3.4 "A Theoretical Perspective"; Page 2 claims "theoretical explanation demonstrating how our methods enhance exploration."
- Verification: The section defines Markov transition kernels (Eq. 3, 4) and invokes conductance and Cheeger's inequality (Eq. 5), but contains no theorem, no proof, no bound. The argument that diverse directions increase conductance is an intuitive statement, not a theoretical derivation. Reversibility and stationary distribution existence are assumed without justification.
- Impact: Undermines scientific credibility if reviewers expect formal guarantees. The paper's main empirical contribution is strong enough to stand without an overclaimed theoretical section.
- Fix: Either (a) remove the "theoretical" framing and replace with "intuitive motivation from Markov chain theory," or (b) provide a concrete bound under simplified assumptions (e.g., finite set of direction types, uniform sampling).

**Issue 2: Verifier noise confounds main results (severity=high, fixable).**
- Anchor: Page 9, Section 4.6; Figure 13 confusion matrix; 27.5% false negative rate.
- Verification: Self-generated validation tests incorrectly reject correct solutions 27.5% of the time. Pass@1 improves by 6.5 points when ground-truth tests are used (Table 8, 82.5% → 89.0%), showing the method is sensitive to verifier quality.
- Impact: The paper's primary metric (pass@1) conflates search quality with verifier accuracy. Readers cannot tell how much of the pass@1 gap comes from better search vs. better test generation.
- Fix: (a) Report pass@any as the primary search-effectiveness metric alongside pass@1. (b) Add an experiment using a fixed, high-quality verifier (e.g., GPT-4 generated tests) to isolate search performance from test quality. (c) Explicitly bound the pass@1 improvement attributable to search vs. verifier.

**Issue 3: LATS comparison discrepancy (severity=high, fixable).**
- Anchor: Page 8, Tables 4 and 5; Appendix E, Table 9.
- Verification: Table 4 reports LATS at 75.6% (HumanEval) under no ground-truth tests, but Table 9 shows LATS at 83.8% under its original protocol. The discrepancy exceeds 8 percentage points. The paper notes this briefly ("ran under our setup") but does not explain which comparison is fairer or why the gap exists.
- Impact: Selective comparison framing may mislead readers about SFS's relative performance. The strongest baseline (LATS with ground-truth checking) outperforms SFS without ground-truth checking.
- Fix: Add a dedicated paragraph discussing the two evaluation protocols, their trade-offs, and where SFS stands in each. Consider reporting results under identical conditions (same ground-truth access or same no-ground-truth access) in the same table.

**Issue 4: Missing statistical significance (severity=medium, fixable).**
- Anchor: Tables 2-6, no variance or significance metrics reported.
- Verification: Many improvements are small (e.g., MBPP+ pass@1: 65.7% SFS vs. 65.4% Tree = 0.3% gap). Without multi-seed runs or bootstrapped confidence intervals, the stability of these rankings is unknown.
- Impact: Weakens confidence in the claim that SFS "consistently outperforms" baselines.
- Fix: Report mean ± std over at least 3 seeds, or provide bootstrap confidence intervals for pass@k metrics. Mark statistically significant improvements.

## Actionable Suggestions
### S1. Reframe the theoretical section (Must)
Replace "A Theoretical Perspective" with "Intuitive Motivation from Markov Chain Theory" or remove the conductance formalism entirely. The qualitative argument that diverse directions improve exploration is valid as intuition, but claiming it as a theory is not defensible. Keep only the transition kernel definitions (Eq. 3-4) which are useful for describing the method, and move the conductance discussion to a brief intuitive paragraph without invoking Cheeger's inequality.

### S2. Add a verifier-accuracy isolation experiment (Must)
Run SFS and baselines on a subset (e.g., 50 HumanEval problems) using ideal verifiers: (a) ground-truth tests, (b) GPT-4 generated tests, (c) self-generated GPT-3.5 tests. Report pass@1 and pass@any under each verifier in a new table. This separates search quality from test quality and quantifies the gap attributable to each. Add a paragraph discussing the interaction.

### S3. Reconcile LATS comparison (Must)
Add a paragraph in Section 4.2 or a new subsection comparing the two evaluation protocols:
- Protocol A (no ground-truth tests): SFS 82.5 vs. LATS 75.6 (HumanEval)
- Protocol B (ground-truth checking at each iteration): LATS 83.8 vs. SFS 82.5 (HumanEval, Appendix Table 9)
Explain why the ranking changes and discuss practical implications. If possible, run LATS under Protocol A on your setup (already done) and SFS under Protocol B, then present both comparisons side-by-side.

### S4. Add statistical significance measures (Must)
Re-run main experiments (HumanEval and MBPP at minimum) with 3-5 random seeds and report pass@1 as mean ± std. Add a footnote or supplementary table marking whether the best result is significantly different from the second-best using a paired bootstrap test (p < 0.05). This addresses concerns about the 0.3% gap on MBPP+.

### S5. Remove or qualify "parameter-free" claim (Nice-to-have)
Change "Our parameter-free method" to "Our method introduces only two search parameters (the UCT exploration constant c and the branching factor k) and requires no additional training or labeled data."

### S6. Remove cost and real-time claims from Conclusion (Must)
Replace the second paragraph of the conclusion with a limitations paragraph (see Mentor Revised Version in annotation on Page 10 — Conclusion). The current cost-reduction and real-time claims are unsupported and likely to be challenged by reviewers.

### S7. Report APPS difficulty distribution (Nice-to-have)
Add a table showing how many of the 200 sampled APPS problems fall into introductory/interview/competition categories, and report per-category performance. This helps readers assess the generalizability of the APPS results.

### S8. Add missing parenthesis in Eq. (2) (Must)
Fix the LaTeX/formatting error in Equation (2). The correct form should be:
$bQ(s_i, d_{i+1})^{(t+1)} \leftarrow (1 - \alpha_n) bQ(s_i, d_{i+1})^{(t)} + \alpha_n \max\{bQ(s_i, d_{i+1})^{(t)}, bQ(s_{i+1}, d_{i+2})^{(t+1)}\}$
Ensure the parentheses are properly closed and the superscript is clearly attached to the Q-value symbol.

### S9. Add compute cost comparison (Nice-to-have)
Report total LLM API calls, estimated cost (in USD), and wall-clock time for each method under the same budget. This makes the practical efficiency discussion evidence-based rather than speculative.

## Storyline Options + Writing Outlines
### Current Storyline Assessment
The current introduction has a reasonable structure but could be more effective. The current flow:
1. P1: Inference scaling is effective (literature review style) → P2: Gap (homogeneous solutions) + proposed solution → Transition paragraph + contribution list.
The key problem is that the gap statement ("existing methods produce similar solutions") appears only in P2, after a full paragraph of literature summary. The reader must wait too long to understand the paper's specific contribution.

### Abstract Outline (Complete, 5 sentences)
**S1 (Problem):** "Repeated sampling and tree-based search methods for LLM code generation often produce highly similar candidate solutions, limiting their ability to explore diverse code regions and find correct programs efficiently."
**S2 (Gap):** "These methods lack a mechanism to generate diverse improvement directions, causing their search to plateau within local solution clusters."
**S3 (Method):** "We propose Scattered Forest Search (SFS), which reframes code generation as black-box optimization and introduces three techniques — Scattering (diverse textual directions), Foresting (multi-start seeds), and Scouting (cross-branch insight sharing) — to systematically diversify the search trajectory."
**S4 (Key Results):** "On HumanEval+ and HumanEval with GPT-3.5, SFS achieves pass@1 rates of 67.1% and 87.2%, improving 8.6 and 4.3 percentage points over prior search methods, while halving the iterations to find correct solutions."
**S5 (Scope):** "SFS scales more efficiently than existing methods across five code generation benchmarks, though its selection accuracy depends on verifier quality."

### Best Storyline Candidate for Introduction (Recommended Revision)
**P1 (Stakes + Inference scaling context):** "Large language models can solve complex code generation tasks more reliably when multiple candidate solutions are sampled and verified. Recent work has shown that scaling inference-time compute can match or exceed training-only improvements (Snell et al., 2024; Brown et al., 2024). The dominant approach, best-of-N sampling, generates independent solutions from the same prompt and selects the best via a verifier (Cobbe et al., 2021; Lightman et al., 2023)."

**P2 (Specific gap):** "However, sampling from the same prompt produces highly similar solutions, as our analysis shows (mean BERT cosine similarity > 0.998 across candidates from identical prompts). This homogeneity limits exploration: the search space of possible code solutions is vast, but existing methods only probe a narrow region around each sampled starting point. A search strategy that deliberately generates diverse candidate solutions while exploiting feedback could substantially improve inference scaling for code generation."

**P3 (Proposed approach + intuition):** "To address this, we reframe code generation as a black-box optimization problem over code space, where validation tests define the objective function and the LLM acts as the optimizer. From this perspective, we develop Scattered Forest Search (SFS). The key insight is that before generating a refinement from a parent solution, we first ask the LLM to propose multiple textual improvement directions — analogous to gradient probes in numerical optimization — and then implement each direction independently. This produces child solutions that explore different, often orthogonal, regions of code space."

**P4 (Method summary + contributions):** "SFS combines three mechanisms: Scattering (diverse direction generation), Foresting (multi-start seed initialization with varied coding-style prompts), and Scouting (cross-branch sharing of successful strategies). The method requires no additional training or labeled data. We evaluate SFS on HumanEval, MBPP, Leetcode, APPS, and CodeContests, showing higher accuracy, faster discovery, and better scaling than best-of-N, line search, and tree search baselines. We also provide an intuitive Markov-chain motivation for why direction diversity improves exploration."

**P5 (Contribution list — same as current but merged to two items):**
- We introduce Scattered Forest Search (SFS), which applies optimization-inspired search techniques — Scattering, Foresting, and Scouting — to improve exploration and avoid local optima in LLM-based code generation.
- We empirically validate SFS across five benchmarks, demonstrating significant improvements in accuracy, scalability, and solution diversity over existing search methods, and analyze the impact of verifier noise on selection reliability.

## Priority Revision Plan
Ranked by impact on paper acceptance likelihood:

| Priority | Item | Action | Effort | Expected Impact |
|----------|------|--------|--------|-----------------|
| P0 | Theoretical overclaim (Section 3.4, Abstract, Introduction) | Replace "theoretical analysis" framing with "intuitive motivation"; remove Cheeger's inequality invocation if no formal proof is added | Low (editorial) | High — removes a likely reviewer objection |
| P0 | LATS comparison discrepancy (Section 4.2, Appendix E) | Add a reconciliation paragraph; present both protocols side-by-side | Low (editorial) | High — restores transparency |
| P0 | Remove unsupported claims in Conclusion | Rewrite Conclusion paragraph 2 to state limitations instead of speculative benefits | Low (editorial) | High — prevents reviewer criticism |
| P0 | Fix Eq. (2) missing parenthesis | Correct the LaTeX formatting error | Low (technical) | Medium — removes technical ambiguity |
| P1 | Verifier accuracy isolation experiment | Add a controlled experiment with different verifier qualities | Medium (experimental) | High — quantifies search vs. selection contribution |
| P1 | Add statistical significance | Re-run with 3 seeds, report mean±std, bootstrap CIs | Medium (experimental) | High — strengthens all empirical claims |
| P1 | "Parameter-free" wording change | Qualify to "no additional training or labeled data required" | Low (editorial) | Medium — corrects misstatement |
| P2 | APPS difficulty distribution | Report sampled difficulty breakdown | Low (analysis) | Medium — improves representativeness |
| P2 | Compute cost comparison | Report API calls and cost per method | Low (analysis) | Medium — supports practical claims |

### ASCII Diagram — Revision Strategy Roadmap
```text
[Current manuscript issues]
    |
    ├── Theoretical overclaim (P0)
    |   └── Reword Section 3.4 as "intuitive motivation"
    |   └── Remove Cheeger's inequality invocation
    |
    ├── LATS comparison discrepancy (P0)
    |   └── Add reconciliation paragraph with both protocols
    |
    ├── Verifier noise confounds pass@1 (P1)
    |   └── Add controlled verifier experiment
    |   └── Report pass@any as primary search metric
    |
    ├── Missing statistical rigor (P1)
    |   └── Multi-seed runs + bootstrap CIs
    |
    └── Conclusion overclaims (P0)
        └── Rewrite with empirically grounded limitations
```

### Page Coverage Audit

| Page | Section | Annotation Count | Coverage Status |
|------|---------|-----------------|-----------------|
| 1 | Abstract + Introduction (P1-P2) | 3 | Covered |
| 2 | Introduction (P3-5, Contributions) | 3 | Covered |
| 3 | Background (Prior Methods) | 1 | Covered |
| 4 | Method (Scattering, Eq. 1-2) | 1 | Covered |
| 5 | Method (Scouting, Theory 3.4) | 1 | Covered |
| 6 | Theory (continued) + Empirical Validation | 0 | Skipped — continuation of theory already annotated on p5; empirical validation is data presentation |
| 7 | Experiments (Benchmarks, Accuracy) | 1 | Covered |
| 8 | Experiments (Scalability, Tables 4-5) | 1 | Covered |
| 9 | Experiments (Ablation, Verifier Accuracy) | 1 | Covered |
| 10 | Additional Related Work + Conclusion | 1 | Covered |
| 15-37 | Appendix | 0 | Skipped — substantive appendix claims (Tables 9-21) are referenced in main-text annotations; no independent issues requiring separate annotation |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup (data/split/protocol/baselines) | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|--------------------------------------|---------|--------------|-----------------|-------------------|
| E1 | Accuracy comparison (Section 4.2, Table 2) | HumanEval+, MBPP+, Leetcode, APPS, CodeContests; GPT-3.5; 10 solutions, 6 self-generated tests; baselines: Base, Line, Tree, BoN | pass@1 | SFS achieves highest pass@1 on all 5 benchmarks | C3 (empirical validation) | No variance reported; small APPS sample (200/10000) |
| E2 | Pass@any comparison (Section 4.2, Table 3) | HumanEval, MBPP, Leetcode, APPS, CodeContests; same setup | pass@any | SFS achieves highest pass@any | C3 | No variance reported |
| E3 | SOTA comparison (Section 4.2, Table 4-5) | HumanEval, MBPP; 2 settings: no ground-truth tests (40 gen max) and subset of GT tests given | pass@1 | SFS outperforms prior SOTA in both settings | C3 | LATS comparison protocol discrepancy (see Issue 3) |
| E4 | Scaling analysis (Section 4.3, Figures 2, 12) | HumanEval, APPS, CodeContests, MBPP, Leetcode; iterations 1-40 | Proportion correct vs. #solutions and #tokens | SFS improves up to 20 sols; baselines plateau | C3 | Only GPT-3.5 shown in main figure |
| E5 | Solution diversity (Section 4.4, Table 6) | HumanEval; 10 iterations | BERT sim., TF-IDF sim., Levenshtein sim., token seq. sim. | SFS has lowest similarity scores | C2 (exploration) | BERT differences numerically small (0.9945 vs 0.9998) |
| E6 | Technique ablation (Section 4.5, Table 7) | HumanEval; 10 iterations | pass@1, pass@any, similarity, val. score, iters | Each component contributes; Scattering most important | C2 | Single benchmark |
| E7 | Verifier accuracy (Section 4.6, Figure 13, Table 8) | HumanEval; comparison: no GT, 3 GT, all GT | pass@1, pass@any, confusion matrix | 27.5% FNR; pass@1 improves 6.5% with GT tests | Robustness to noise | Claim partially supported (pass@any robust, pass@1 sensitive) |
| E8 | Model ablation (Section 4.7, Figure 14, Table 10) | HumanEval; models: GPT-3.5, GPT-4o-mini, GPT-4o, LLaMA-3.1-8B | pass@k curves | Weaker models benefit more from SFS | C3 | No statistical comparison |
| E9 | Seed scattering themes (Section 3.5, Table 1) | HumanEval; themes: None, Jabberwocky, Style, Role | pass@1, pass@any, similarity, val. score | All themes improve over None; Role and Style best | C2 | GPT-3.5 only |
| E10 | MCTS selection policy (Appendix N, Table 21) | HumanEval; UCT vs PUCT | pass@1, pass@any, similarity, iters | UCT slightly outperforms PUCT for SFS | C2 | Limited analysis of why |

### Research-Theme Gap Diagnosis

**Gap 1 — Search vs. Selection Confound.** The paper's central claim is that SFS improves search (exploration and exploitation). However, pass@1 conflates search quality with verifier accuracy. The 27.5% false negative rate means that even when SFS finds the correct solution, it may fail to select it. The magnitude of verifier-induced degradation is not quantified separately from search improvement.

**Gap 2 — Statistical Reliability.** No experiment reports variance or significance. Given the small APPS sample and small deltas on some benchmarks, the stability of the rankings is unknown.

**Gap 3 — Ablation Scope.** The ablation (Table 7) is only on HumanEval with GPT-3.5. It is unclear whether the relative importance of Scattering vs. Foresting vs. Scouting generalizes to stronger models (GPT-4) or harder benchmarks (CodeContests).

### Proposed Research Experiments (P0/P1/P2)

**Exp-R1: Verifier-controlled accuracy decomposition (P0)**
- Target Claim: "SFS improves search effectiveness" (not just pass@1)
- Hypothesis: The search component (pass@any) improves independently of verifier quality, but pass@1 is bottlenecked by verifier accuracy
- Minimal Design: Run SFS + BoN + Tree on 50 HumanEval problems with 3 verifier conditions: (a) self-generated GPT-3.5, (b) GPT-4 generated, (c) ground-truth tests
- Controls: Same 50 problems, same solution budget (10), all methods use same verifier
- Metrics: pass@1, pass@any, gap between pass@1 and pass@any
- Success Criterion: SFS's pass@any remains highest across all verifiers; its pass@1 gap to pass@any shrinks with better verifiers
- Estimated Cost: ~50 problems × 3 verifiers × 4 methods × 10 solutions = ~6000 API calls (~$30 with GPT-3.5)
- Expected Quality Gain: High — separates search from selection, addresses the most critical confound

**Exp-R2: Cross-model and cross-benchmark ablation (P1)**
- Target Claim: "Component contributions are consistent across settings"
- Hypothesis: Scattering remains the most important component regardless of base model or benchmark
- Minimal Design: Run full ablation (Everything / No Scattering / No Foresting / No Scouting) on GPT-4o-mini × CodeContests (or APPS)
- Controls: Same budget and evaluation protocol as current Table 7
- Metrics: pass@1, pass@any, iters (incl), similarity
- Success Criterion: Same ranking of components (Scattering > Foresting > Scouting) holds
- Estimated Cost: ~4 configurations × 200 problems × 10 solutions = ~8000 API calls (~$20 with 4o-mini)
- Expected Quality Gain: Medium — strengthens generalization claim

**Exp-R3: Statistical significance bootstrap (P1)**
- Target Claim: "All improvements are statistically reliable"
- Hypothesis: Reported improvements are unlikely to occur by chance
- Minimal Design: Bootstrap resample (10,000 iterations) the pass@k estimates from existing single-seed runs to compute 95% CIs; alternatively, run 3 seeds on HumanEval
- Controls: N/A (bootstrapping from existing data)
- Metrics: 95% CI for pass@1, significance flag for SFS vs. best baseline
- Success Criterion: Improvements labeled significant (p < 0.05) for at least 4 out of 5 benchmarks
- Estimated Cost: Near-zero for bootstrap; ~3× API cost for multi-seed runs (~$15)
- Expected Quality Gain: High — addresses the most common reviewer concern

**Exp-R4: Compute efficiency measurement (P2)**
- Target Claim: Basis for realistic deployment discussion
- Hypothesis: SFS's per-iteration cost (2 API calls vs. 1 for BoN) is offset by fewer iterations to find correct solutions
- Minimal Design: Report total API calls, estimated USD cost, and wall-clock time for each method on HumanEval (10 iterations)
- Controls: Same hardware, same API endpoint
- Metrics: Total cost per solved problem, average time to solution
- Success Criterion: Provide empirical data; no ranking necessarily expected
- Estimated Cost: Already collected (log API calls); analysis only
- Expected Quality Gain: Medium — replaces speculative cost claims with evidence

### ASCII Diagram — Experiment Upgrade Plan
```text
P0 (Before resubmission)
├── Exp-R1: Verifier-controlled accuracy (isolate search from selection)
├── Fix Eq. (2) formatting
└── Statistical reporting: add CIs via bootstrap on existing data

P1 (Before resubmission if time permits)
├── Exp-R2: Cross-model ablation (GPT-4o-mini on CodeContests)
└── Exp-R3: Multi-seed runs on HumanEval + MBPP

P2 (Future work)
└── Exp-R4: Compute cost measurement
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

**Rationale:** The paper presents a practically useful search method for LLM code generation with solid empirical support for improved solution diversity and favorable scaling behavior. The ablation study is clean, and the benchmarks are appropriate. However, several factors limit the current score:

- **Research Value (7/10):** The optimization framing is insightful and the Scattering technique is a clear conceptual contribution. The method is likely to be useful for practitioners. However, the theoretical section overclaims without substance, and the best comparison is to LATS (which competes closely), not a clearly established SOTA.
- **Novelty (deferred — see Novelty Verification section):** External literature verification is unavailable in this run. The core technique (using LLM-generated textual directions to diversify tree search) appears novel in the specific SFS integration, but the individual components (prompt variation, multi-start, insight sharing) have clear precedents in evolutionary computation and prompt engineering.
- **Validity/Soundness (6/10):** The empirical methodology has notable gaps — no statistical significance, high verifier noise confounds the primary metric, APPS sampling is limited, and the LATS comparison is inconsistently framed. The theoretical analysis does not deliver on its promises.
- **Reproducibility (7/10):** The method is described with pseudocode and the experimental setup is mostly clear. Two missing details: the APPS/CodeContests adaptation procedure and the seed selection for the 200 APPS sample.
- **Writing Quality (6/10):** The writing is generally clear but contains overclaims ("parameter-free," theoretical demonstration), structurally misplaced content (Sec 3.5 forward reference in Introduction), and a conclusion with unsupported speculation.

**Post-Revision Target: [7.5, 8.0] / 10**

If the authors address the P0 items (theoretical reframing, LATS reconciliation, conclusion rewrite, Eq. 2 fix) and at least one P1 experiment (verifier-controlled accuracy decomposition or statistical significance), the paper would be suitable for a top-tier venue. The core technical contribution is sound, and the empirical evidence for diversity improvement is convincing. The main barriers to a higher score are the overclaims and the unaddressed verifier confound, both of which are fixable.