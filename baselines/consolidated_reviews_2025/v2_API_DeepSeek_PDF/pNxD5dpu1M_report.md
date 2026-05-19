## Summary
# Final Review Report

## Summary

This paper introduces Chung-Lu cooperative mean field games (CLCMFGs), a new modeling framework for cooperative multi-agent reinforcement learning (MARL) on very sparse graphs. The key technical insight is to leverage Chung-Lu (CL) random graphs—which can generate sparse networks with finite expected degree and possibly infinite variance—as the underlying interaction topology, extending prior graphon/graphex-based MFG models that require the expected average degree to diverge to infinity.

The paper makes four main contributions: (1) formulation of CLCMFGs with theoretical mean-field convergence guarantees (Theorem 1, Proposition 1, Corollary 1); (2) a two-systems approximation that separates agents into low-degree (k ≤ k*) and high-degree (k > k*) groups via Heuristic 1; (3) two scalable learning algorithms (CLMFC and CLMFMARL) that reduce the graphical MARL problem to a single-agent MFC MDP; and (4) empirical evaluation on four benchmark problems (SIS, SIR, Color, Rumor) across eight real-world networks, showing 3–20× reduction in mean-field approximation error compared to Lp graphon and graphex baselines.

The paper addresses an important open problem in the MFG-MARL literature—handling very sparse, power-law-type agent networks—and provides a theoretically grounded practical solution. However, several issues limit the current version: the core algorithmic approximation (Heuristic 1) lacks theoretical error bounds; the comparison with IPPO does not control for statistical significance or compute budget; the conclusion omits explicit limitations; and the narrative structure of the introduction can be improved for clarity. These issues are fixable with targeted revisions, and the overall research direction is promising.

## Strengths
1. **Important problem framing.** The paper identifies a genuine gap in the MFG-MARL literature: existing graphon and graphex-based MFG models require the expected average degree to diverge to infinity, excluding the sparse power-law topologies commonly observed in real-world networks. Targeting the finite-first-moment/infinite-second-moment regime is a well-motivated and non-trivial research direction.

2. **Solid theoretical backbone.** The paper provides formal convergence results (Theorem 1, Proposition 1, Corollary 1) connecting the finite-N system to the limiting CLCMFG, building on local weak convergence of CL graphs. The proof in Appendix A shows careful reformulation to fit the Lacker et al. (2023) framework, and Corollary 1's optimal policy transfer guarantee is a practically meaningful result.

3. **Pragmatic algorithmic design.** The two-systems approximation (low-degree agents with exact degree classes + high-degree agents aggregated into µ∞) is a clever engineering compromise that balances computational tractability with accuracy. The paper provides both a model-based solver (CLMFC, Algorithm 1) and a model-free variant (CLMFMARL, Algorithm 2), offering flexibility for different application settings.

4. **Comprehensive empirical evaluation.** The evaluation spans 4 diverse benchmark problems (SIS, SIR, Color, Rumor) across 8 real-world networks from the KONECT database (CAIDA, Cities, Digg, Enron, Flixster, Slashdot, Yahoo, YouTube) with up to 3.2M nodes. Table 1 convincingly demonstrates that CLCMFG reduces mean-field approximation error by 3–20× compared to LPGMFG and GXMFG baselines.

5. **Reproducibility consideration.** The simulation details in Appendix C report hyperparameters (learning rate, KL coefficient, network architecture, batch sizes) and computing resource usage (80,000 core hours on Intel Xeon CPUs), which is helpful for reproducibility.

## Weaknesses
1. **Unquantified approximation error (Heuristic 1).** The two-systems approximation—the core algorithmic contribution—is built on Heuristic 1 (size-biased neighbor degree distribution). While the paper cites Jackson et al. (2008) for justification, no theoretical error bound is provided. The finite-to-limit theoretical convergence (Theorem 1) is rigorous, but the central algorithmic approximation has no accompanying characterization. This asymmetry between theoretical rigor and algorithmic approximation is a significant gap. *Severity: Major.*

2. **Missing statistical significance in learning comparisons.** Table 2 reports only single best-objective values after 24 hours of training. Without confidence intervals, standard deviations, or significance tests, the reader cannot assess whether the reported improvements (e.g., CLMFMARL -9.11 vs IPPO -19.70 on SIS N=860) are reproducible or reflect single-run variation. This is a critical omission for a competitive algorithm comparison. *Severity: Major.*

3. **Uncontrolled compute budget in algorithm comparison.** The comparison between CLMFC/CLMFMARL and IPPO is performed under a fixed wall-clock time (24 hours) rather than matched environment interactions or gradient updates. Since CLMFC operates on a compact MF representation while IPPO requires per-agent rollouts, the comparison conflates algorithmic quality with representation efficiency. *Severity: Major.*

4. **Informal treatment of core theoretical assumptions.** The "tacit assumption" that Var(deg(v_N)) → ∞ is stated informally rather than as a formal numbered assumption. Since the infinite-variance regime is central to the paper's claimed contribution (finite first moment, infinite second moment), this should be formalized like Assumption 1. The claim that "our approach applies to the finite variance case as well" is stated without theoretical or empirical support. *Severity: Major.*

5. **Action-dependent reward handling is underspecified.** The paper mentions that action-dependent rewards can be handled via an extended state space and split time steps, but this construction is described in one sentence. The theoretical guarantees (Theorem 1, Proposition 1, Corollary 1) are presented for the simple reward r(μ^N_t), while the experimental problems (Color, Rumor) use action-dependent rewards. The gap between theoretical setting and experimental practice is not bridged. *Severity: Major.*

6. **Conclusion lacks explicit limitations.** The conclusion summarizes contributions and suggests generic future work directions (partial observability, bounded rationality) but does not state any limitations of the current approach. This omission reduces scientific credibility. *Severity: Minor.*

7. **Introduction narrative structure is literature-list style.** The first introduction paragraph reads as a chronological survey of graph-based MFG models (graphon → Lp graphon → graphex) rather than a problem-driven motivation. The core gap is stated at the end rather than upfront, reducing narrative engagement. *Severity: Minor.*

## Key Issues
These are the most impactful defects, ranked by severity and impact on the paper's validity and research value.

| Rank | Issue | Severity | Validity Risk | Fixability | Confidence | Priority |
|------|-------|----------|---------------|------------|------------|----------|
| 1 | Heuristic 1 lacks quantified error bounds | Major | High—core algorithmic approximation uncharacterized | Medium—can add empirical convergence analysis | High | P0 (Must fix for publication) |
| 2 | Statistical significance missing in Table 2 | Major | High—reported gains may be noise | High—add multi-seed variance and significance tests | High | P0 (Must fix for publication) |
| 3 | Compute budget not matched in algorithm comparison | Major | Medium—conflates algorithmic quality with representation efficiency | Medium—add interaction-matched comparison | High | P0 (Must fix for publication) |
| 4 | "Tacit assumption" about infinite variance is informal | Major | Medium—core modeling choice lacks formal treatment | High—add Assumption 1b | High | P1 (Should fix) |
| 5 | Action-dependent reward handling underspecified | Major | Medium—theory-experiment gap | Medium—clarify extended state space mapping | High | P1 (Should fix) |

**Additional items:** CLMFMARL's claimed advantage over two-systems approximation (Page 7) is overstated (Issue annotation #12). The Conclusion lacks explicit limitations. The extensive approximation formula (Page 6) uses undefined symbols.

## Actionable Suggestions
### S1: Quantify Heuristic 1 approximation error (P0, Must fix)
**Problem:** The two-systems approximation depends on Heuristic 1, which has no quantified error bound.
**Action:** Add an empirical convergence analysis in Section 4: for synthetic CL graphs with known degree distributions, compute the KL divergence or TV distance between the true neighbor degree distribution and the Heuristic 1 approximation as a function of graph size N and degree exponent γ. Report the error magnitude and its decay rate. If a theoretical bound is feasible (e.g., via Stein's method or concentration inequalities for CL graphs), add it as a proposition.
**Expected impact:** Closing the rigor gap between the theoretical convergence results and the algorithmic approximation. Without this, the paper's central algorithmic claim remains unvalidated at a theoretical level.

### S2: Add statistical significance to learning comparison (P0, Must fix)
**Problem:** Table 2 reports single best-objective values only.
**Action:** Repeat all experiments in Table 2 for at least 5 independent seeds with different random initializations. Report mean ± std for each method. Add a paired bootstrap test or Mann-Whitney U test comparing CLMFMARL vs IPPO on the larger graphs (N=860, N=1598). State explicitly whether differences are statistically significant at p < 0.05.
**Expected impact:** Without this, the claimed outperformance of the proposed methods is not statistically grounded and may not survive reviewer scrutiny.

### S3: Compute-matched comparison with IPPO (P0, Must fix)
**Problem:** The 24-hour fixed-time comparison conflates algorithmic quality with representational efficiency.
**Action:** Add a secondary comparison where all methods are evaluated at matched numbers of environment interactions (rather than wall-clock time). Report both sample efficiency curves (reward vs. environment steps) and wall-clock time curves. Add a paragraph discussing the trade-off: CLMFC/CLMFMARL use compact MF representations that enable faster simulation but at the cost of approximation error.
**Expected impact:** Allows reviewers to distinguish between "better algorithm" and "more efficient representation," which is essential for fair assessment.

### S4: Formalize the infinite variance assumption (P1, Should fix)
**Problem:** The "tacit assumption" about diverging variance is informal.
**Action:** Add "Assumption 1b (Degree variance divergence): Var(deg(v_N)) → ∞ as N → ∞." State whether the theoretical results (Theorem 1, Proposition 1, Corollary 1) require this assumption or hold without it. Remove or qualify the claim that "our approach applies to the finite variance case as well" unless supported by evidence.
**Expected impact:** Clarifies the scope of theoretical guarantees and prevents overclaiming.

### S5: Bridge action-dependent reward gap (P1, Should fix)
**Problem:** The main text uses r(μ^N_t) while experiments use action-dependent rewards.
**Action:** Add a remark in Section 3 explicitly stating: "For action-dependent rewards r(x,u), the objective becomes Σ_{t=1}^{2T} r̃(μ̃_t) where μ̃_t is the extended mean field on X_e = X ∪ (X × U). Theorem 1 and Proposition 1 extend to this setting via the construction in Appendix A.1." Alternatively, keep the main text simpler and add an explicit statement that the experiments use this extended formulation.
**Expected impact:** Closes the traceability gap between theory and experiments.

### S6: Add limitations to Conclusion (P2, Nice-to-have)
**Problem:** Conclusion has no limitations.
**Action:** Add 3-4 specific limitations: (a) Heuristic 1 approximation error is uncharacterized, (b) large-N assumption may fail for moderate N, (c) known degree distribution is assumed, (d) cooperative setting only. See the Mentor Revised Version in the Conclusion annotation (Page 9) for a concrete draft.
**Expected impact:** Improves scientific transparency and reviewer perception of rigor.

## Storyline Options + Writing Outlines
### Abstract Outline (Recommended)

**S1 (Problem & Domain):** "Large agent networks with sparse, power-law-type connectivity pose fundamental challenges for multi-agent reinforcement learning due to their size and structural heterogeneity."

**S2 (Prior Gap):** "Existing graphon and graphex-based mean field game models require the expected average degree to diverge to infinity, which excludes the very sparse topologies commonly observed in real-world social and communication networks."

**S3 (Proposed Model):** "We introduce Chung-Lu cooperative mean field games (CLCMFGs), a new MFG framework built on Chung-Lu random graphs that can capture networks with finite expected degree and possibly infinite variance."

**S4 (Key Result & Evidence):** "We provide theoretical mean-field convergence guarantees (Theorem 1) and a practical two-systems approximation that reduces the graphical MARL problem to a single-agent MFC MDP. On eight real-world networks across four benchmark problems, CLCMFG reduces mean-field approximation error by 3–20× compared to Lp graphon and graphex baselines."

**S5 (Bounded Claim):** "Our approach enables tractable MARL on a class of sparse graphs that prior MFG methods cannot handle, with the caveat that the core approximation heuristic has not yet been theoretically bounded."

### Introduction Outline (Paragraph-by-Paragraph Plan)

**P1 — Problem Stakes (new):**
Role: Establish the practical importance of large-scale MARL on sparse networks.
Claim: Real-world agent networks (social, communication, epidemiological) are often very sparse with power-law degree distributions and finite mean degree—a regime that existing graph-based MFG methods cannot handle.
Evidence: Reference real-world network statistics (sparsity, power-law exponents).
Transition: → This gap motivates a new graph-theoretic framework.

**P2 — Prior Work and Its Limitation (revised from current first paragraph):**
Role: Survey graph-based MFG evolution (graphon → Lp graphon → graphex) and identify the common limitation.
Claim: All existing methods require expected average degree → ∞, excluding sparse real-world topologies.
Key citation anchors: Caines & Huang (2019, 2021), Cui & Koeppl (2022), Fabian et al. (2023, 2024).
Transition: → We therefore adopt the Chung-Lu random graph model.

**P3 — CL Model and Motivation (revised from the end of the current second paragraph):**
Role: Introduce CL graphs as the solution, listing the four desirable properties (sparsity generation, theoretical foundation, algorithmic suitability, simplicity).
Claim: The CL model aligns with our aim to model sparse, large agent networks.
Transition: → Leveraging this model, we formulate CLCMFGs.

**P4 — Contribution Overview (revised from the current contribution summary paragraph):**
Role: State contributions concisely (model, theory, approximation, algorithms, empirical validation).
Claim: Four specific contributions as revised in the contribution list annotation.
Transition: → The paper proceeds as follows: Section 2 covers CL graphs, Section 3 the theoretical model, Section 4 the approximation, Section 5 algorithms, Section 6 examples, Section 7 experiments.

### Storyline Alternatives Considered

**Option A (Selected): Problem → Graph Gap → CL Solution → Theory → Approximation → Experiments.**
Advantage: The narrative arc is clear and problem-driven. The gap (sparse networks not covered by existing MFG theory) is established before the solution is introduced.

**Option B (Current paper structure): Literature survey → Learning survey → CL model → Theory → Approximation → Experiments.**
Disadvantage: The opening paragraph reads as a historical survey rather than a motivated problem statement. The CL model is introduced almost as an afterthought at the end of the second paragraph.

**Option C: Application-first.** Open with a concrete application (e.g., epidemic control on a contact network), then abstract to the general problem.
Advantage: High reader engagement. Disadvantage: Would require additional space and may not match the ICLR format's expectation for concise introduction.

## Priority Revision Plan
### P0 (Must fix before acceptance)

| # | Revision Item | Location | Effort | Expected Impact | Acceptance Criterion |
|---|--------------|----------|--------|-----------------|---------------------|
| 1 | Add empirical/theoretical bound for Heuristic 1 error | Section 4 | High (theory) or Medium (empirical) | High—closes core rigor gap | Error bound or empirical convergence analysis provided |
| 2 | Add multi-seed variance + significance tests for Table 2 | Section 7, Table 2 | Medium (re-run 5 seeds) | High—establishes statistical grounding | Mean±std reported; p-value for main comparisons |
| 3 | Add interaction-matched comparison with IPPO | Section 7 | Medium | High—fair algorithm comparison | Sample efficiency curves + discussion paragraph |
| 4 | Fix CLMFMARL advantage claim (does not avoid all approximation error) | Section 5, p.7 | Low (text edit) | High—corrects overclaim | Revised wording per annotation #12 |

### P1 (Should fix before acceptance)

| # | Revision Item | Location | Effort | Expected Impact | Acceptance Criterion |
|---|--------------|----------|--------|-----------------|---------------------|
| 5 | Formalize infinite variance as Assumption 1b | Section 2 | Low (text edit) | Medium—clarifies scope | Assumption 1b added, finite-variance claim qualified |
| 6 | Clarify action-dependent reward mapping | Section 3 | Low (text edit) | Medium—bridges theory-experiment gap | Remark added linking extended state space to main text |
| 7 | Add limitations paragraph to Conclusion | Section 8 | Low (text edit) | Medium—improves transparency | 3-4 specific limitations stated |

### P2 (Nice-to-have improvements)

| # | Revision Item | Location | Effort | Expected Impact | Acceptance Criterion |
|---|--------------|----------|--------|-----------------|---------------------|
| 8 | Restructure Introduction (Option A) | Section 1 | Medium | Medium—improves narrative | Paragraphs reordered per outline |
| 9 | Define symbols in extensive approximation formula | Section 4, p.6 | Low | Low—improves readability | Symbol definitions added in main text |
| 10 | Add quantitative results to Abstract | Abstract | Low | Low—improves first impression | Bounded performance numbers included |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Compare CLCMFG, CLCMFG*, LPGMFG, GXMFG on real networks (Table 1) | 8 real-world networks (KONECT), SIS/SIR/Color/Rumor, 50 trials | Avg. expected total variation Δμ (TV distance) | CLCMFG reduces error 3–20× vs LPGMFG/GXMFG | C3 (two-systems approximation accuracy) | No theoretical error bound for Heuristic 1; CLCMFG* missing on Color/Rumor (cost); Yahoo shows non-monotonic improvement |
| E2 | Compare CLMFC/CLMFMARL vs IPPO on synthetic graphs (Table 2) | CL synthetic graphs, N ∈ {167,406,860,1598}, 24h training on 96 CPUs | Best objective (single value) | CLMFC/MFMARL > IPPO on N≥860; competitive on N=167,406 | C4 (learning algorithm performance) | No variance/std reported; compute budget not interaction-matched |
| E3 | Training curves on synthetic graphs (Figure 3) | N=406 CL graph, 4 problems | Episode return over steps | CLMFC/MFMARL converge faster than IPPO | C4 | Single network size; no confidence bands |
| E4 | Training curves on real networks (Figure 4) | Enron (SIS), Slashdot (SIR), CAIDA (Color), Cities (Rumor) | Episode return over steps | Both algorithms converge on real networks | C4 | No IPPO comparison on real networks |

### Research-Theme Gap Diagnosis

The completed experiments validate the core claims (C3: approximation accuracy, C4: algorithmic performance) but three gaps remain:

1. **Claim C2 (theoretical guarantees) is not empirically validated.** Theorem 1 and Proposition 1 are proven theoretically, but the paper does not include a dedicated experiment showing the convergence of finite-N MFs to the limiting CLCMFG as N increases. A synthetic experiment with controlled N would directly validate the theory.

2. **No systematic study of the threshold k* sensitivity.** The two-systems approximation depends on the choice of k* (the degree threshold separating low-degree and high-degree agents). The paper does not analyze how performance varies with k*.

3. **No OOD or stress-test evaluation.** All experiments are on standard benchmarks with IID initial conditions. The paper does not test robustness to distribution shift, adversarial perturbations, or graph structure misspecification.

### Proposed Research Experiments (P0/P1/P2)

**Exp P0-1: Heuristic 1 error analysis (P0, Must fix)**
- Target Claim: C3 (two-systems approximation)
- Hypothesis: The error of Heuristic 1 decays with graph size N and depends on degree exponent γ.
- Minimal Design: Generate synthetic CL graphs at N ∈ {10^3, 10^4, 10^5, 10^6} with γ ∈ {2.1, 2.5, 3.0, 3.5}. For each configuration, compute the TV distance between the true neighbor degree distribution (sampled empirically) and the Heuristic 1 approximation.
- Controls/Baselines: LPGMFG and GXMFG approximations for comparison.
- Metrics: TV distance, KL divergence.
- Success Criterion: Error decays at rate O(1/N^α) for some α > 0.
- Estimated Cost: Low (single CPU, a few hours per configuration).
- Expected Paper-Quality Gain: High—closes the core rigor gap.

**Exp P0-2: Multi-seed statistical validation (P0, Must fix)**
- Target Claim: C4 (learning algorithm performance)
- Hypothesis: The performance difference between CLMFMARL and IPPO is statistically significant on large graphs.
- Minimal Design: Repeat Table 2 with 5 seeds each; report mean ± std; paired bootstrap test.
- Controls/Baselines: Same as current Table 2.
- Metrics: Mean objective, p-value.
- Success Criterion: p < 0.05 for CLMFMARL vs IPPO on N=860 and N=1598.
- Estimated Cost: Medium (5× more compute, ~4 days per configuration).
- Expected Paper-Quality Gain: High—establishes statistical grounding.

**Exp P0-3: Interaction-matched comparison (P0, Must fix)**
- Target Claim: C4 (learning algorithm performance)
- Hypothesis: The relative advantage of CLMFMARL changes when methods are compared at matched environment interactions.
- Minimal Design: Run all methods at fixed interaction budgets {10^5, 10^6, 10^7, 10^8} rather than fixed wall-clock time.
- Controls/Baselines: Same as current Table 2.
- Metrics: Objective vs interaction count curves.
- Success Criterion: CLMFMARL outperforms IPPO at ≥2 interaction budgets.
- Estimated Cost: Medium.
- Expected Paper-Quality Gain: High—fair comparison.

**Exp P1-1: Finite-N convergence validation (P1, Should fix)**
- Target Claim: C2 (theoretical convergence)
- Hypothesis: The empirical MF converges to the limiting CLCMFG MF at rate O(1/√N).
- Minimal Design: On a simple SIS problem with known CLCMFG solution, compute TV distance between finite-N empirical MF and limiting MF for N ∈ {50, 100, 200, 500, 1000, 2000}.
- Controls/Baselines: None needed.
- Metrics: TV distance.
- Success Criterion: Decreasing trend with N.
- Estimated Cost: Low.
- Expected Paper-Quality Gain: Medium—directly validates Theorem 1.

**Exp P1-2: Threshold k* sensitivity (P1, Should fix)**
- Target Claim: C3 (two-systems approximation)
- Hypothesis: Performance is robust to k* beyond a minimum value (e.g., k* ≥ 5 for power-law γ=2.5).
- Minimal Design: Sweep k* ∈ {1, 3, 5, 10, 20} on 3 network-problem combinations where CLCMFG* is feasible.
- Controls/Baselines: CLCMFG* as reference.
- Metrics: Δμ TV distance vs CLCMFG*.
- Success Criterion: Δμ stabilizes for k* ≥ 5.
- Estimated Cost: Low-Medium.
- Expected Paper-Quality Gain: Medium—guides practitioners on threshold choice.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6 / 10

**Rationale:** The paper addresses an important, well-motivated problem and provides a solid theoretical foundation (convergence theorems) combined with a practical algorithmic framework. The empirical evaluation on eight real-world networks convincingly demonstrates the advantage of CLCMFG over existing methods in the sparse graph regime. However, three critical weaknesses prevent a higher score: (1) the central algorithmic approximation (Heuristic 1) lacks any quantified error bound, creating a significant rigor gap; (2) the learning algorithm comparison (Table 2) lacks statistical significance testing, variance reporting, and compute-matched baselines; and (3) the treatment of core theoretical assumptions is informal in places. These issues are fixable with targeted revisions, and the underlying research direction has substantial potential.

**Post-Revision Target:** [7, 8] / 10

**Justification:** If the authors address the P0 items (Heuristic 1 error analysis, multi-seed statistical validation, interaction-matched comparison, and corrected claims in Section 5), the paper would present a well-rounded contribution with both theoretical and empirical rigor. The upper bound of 8 reflects the inherent limitation that the core approximation may not admit a tight theoretical bound, which is acceptable for an applied theory paper if accompanied by convincing empirical error analysis. A score above 8 would require additional theoretical characterization of the approximation error, which is a substantial research extension beyond the current scope.

### ASCII Diagrams

```text
ASCII Diagram — Paper Structure & Evidence Map

[Problem: Very sparse MARL]
    ↓
[Gap: Graphon/graphex MFG requires E[deg]→∞]
    ↓
[Solution: CLCMFG on Chung-Lu graphs]
    ├── [Theory: Theorem 1 (MF convergence)]
    │   └── [Proposition 1 (Objective convergence)]
    │       └── [Corollary 1 (Optimal policy transfer)]
    ├── [Approximation: Two-systems (Heuristic 1)]
    │   └── [Extensive approx. (CLCMFG*)]
    ├── [Algorithms: CLMFC (model-based) / CLMFMARL (model-free)]
    └── [Evidence: Table 1 (3-20× error reduction) + Table 2 (vs IPPO)]
            │
            └── [GAPS: No Heuristic 1 bound | No std/sig in Table 2]
```

```text
ASCII Diagram — Revision Strategy Roadmap

[Issue 1: Heuristic 1 unquantified]
    → [Fix: Empirical error analysis on synthetic CL graphs]
    → [Gain: Closes rigor gap, strengthens C3]

[Issue 2: No statistical significance in Table 2]
    → [Fix: 5-seed runs, mean±std, bootstrap test]
    → [Gain: Statistical grounding for learning claims]

[Issue 3: Compute budget not matched]
    → [Fix: Interaction-matched comparison curves]
    → [Gain: Fair algorithm assessment, clarifies representation vs. algorithmic advantage]

[Issue 4: Informal infinite-variance assumption]
    → [Fix: Formal Assumption 1b]
    → [Gain: Clearer scope, no overclaiming]

[Issue 5: Underspecified action-dependent rewards]
    → [Fix: Clarify extended state space mapping]
    → [Gain: Theory-experiment traceability]
```

```text
ASCII Diagram — Related-Work Taxonomy Tree (Layered)

Related Work: Graph-Based MFG Models
├── Branch 1: Graphon-based (dense graphs)
│   ├── Leaf 1.1: GMFG (Caines & Huang, 2019; 2021) — dense graphons
│   └── Leaf 1.2: Regularized GMFG (Zhang et al., 2024) — monotone graphons
│   Limitation: Only dense graphs; expected degree must diverge
│
├── Branch 2: Lp Graphon-based (moderately sparse)
│   └── Leaf 2.1: LPGMFG (Fabian et al., 2023; 2024) — Lp graphons
│   Limitation: Still requires E[deg]→∞; excludes power-law γ>2
│
├── Branch 3: Graphex-based (moderately sparse)
│   └── Leaf 3.1: GXMFG (Fabian et al., 2024) — graphex processes
│   Limitation: Heavy-tailed degree distribution; E[deg] still diverges
│
└── Branch 4: Chung-Lu based (very sparse) ← THIS PAPER
    └── Leaf 4.1: CLCMFG — finite E[deg], infinite Var(deg)
    Novelty: First MFG model handling finite-first-moment regime; two-systems approx.
```

The three diagrams above summarize the paper's evidence structure (A), the recommended revision path (B), and the related-work positioning (C). The taxonomy tree (C) shows that CLCMFGs occupy a distinct niche—very sparse graphs with finite expected degree—that prior methods cannot reach.