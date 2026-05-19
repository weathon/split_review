## Summary
This paper addresses the problem of learning sparse continuous policies in offline reinforcement learning, where the policy's bounded support causes undefined log-likelihoods for out-of-support actions from the dataset. The authors propose Fat-to-Thin Policy Optimization (FtTPO), a two-stage framework that first trains a heavy-tailed "fat" proposal policy (q-Gaussian with q=2) on the offline dataset, then distills it into a sparse "thin" actor policy (q-Gaussian with q=0) via reverse KL minimization. The method is instantiated using the q-Gaussian family, which spans both heavy-tailed (1<q<3) and sparse (q<1) members under a unified formulation. Experiments on a safety-critical treatment simulation and nine D4RL MuJoCo tasks show that FtTPO produces tightly concentrated sparse policies that perform competitively with popular offline algorithms (IQL, XQL, SQL). The paper is technically sound and addresses a legitimate gap — handling out-of-support actions induced by sparse policies — but has several weaknesses: (1) priority/first claims cannot be verified without external literature; (2) MuJoCo results lack tabular summaries and statistical rigor; (3) safety evaluation conflates reward with safety; (4) computational cost is 2x that of single-policy baselines; (5) several methodological details (mean-copying, KL estimator) need clarification for reproducibility.

## Strengths
1. **Well-motivated problem formulation.** The paper identifies a genuine and previously under-explored challenge in offline RL: sparse continuous policies produce undefined log-likelihoods for out-of-support dataset actions. The authors clearly explain why this is distinct from the standard distributional shift problem (Section 3.1) and why Gaussian approximations or random action replacement are insufficient (Section 3.2). The practical motivation through safety-critical applications (medical treatment) is compelling.

2. **Principled two-stage framework.** The fat-to-thin distillation approach is a clean and intuitive solution. Instead of forcing the sparse policy to directly learn from out-of-support actions, FtTPO learns a heavy-tailed proposal first (which avoids the support issue) and then distills it into a sparse actor. This avoids the need for ad-hoc workarounds like action replacement or Gaussian approximation.

3. **Unified q-Gaussian formulation.** Using the q-Gaussian family to span both heavy-tailed (q=2) and sparse (q=0) policies under one mathematical framework is elegant. The paper correctly handles normalization constants, sampling via Generalized Box-Müller, and the q-exponential advantage weighting, demonstrating technical competence.

4. **Informative policy evolution visualizations.** Figures 3, 5, and 15 provide clear evidence that FtTPO's actor policy progressively concentrates on a sub-region of the action space while the proposal policy maintains broader coverage. This visualization convincingly demonstrates that the distillation procedure works as intended.

5. **Ablation studies targeting core design questions.** The ablation (Section 5.3) directly addresses whether the sparse actor degrades performance (vs. proposal-only), whether the KL minimization is competitive with SPOT, and whether the heavy-tailed proposal outperforms Gaussian. This disciplined ablation design is a strength.

6. **Reproducibility effort.** The paper provides code, detailed hyperparameter tables (Appendix Tables 1-4), and explicit parameter sweeps, which is commendable for reproducibility.

## Weaknesses
1. **Unverifiable priority claims (major).** Contributions (1) "we are the first to investigate the out-of-support action issue" and (2) "the first deep offline RL framework for learning sparse policies" are priority claims that require comprehensive literature verification, which is unavailable in this run. Furthermore, Li et al. (2023), cited in the paper itself, already explored sparse q-Gaussian policies, so the "first" claim needs scoping to "first deep-network-based framework."

2. **Missing tabular results for MuJoCo (major).** The paper relies entirely on learning curves (Figure 4) without a table of final normalized scores. This is a significant omission because: (a) D4RL papers conventionally report score tables; (b) Figure 4 uses selective transparency (only FtTPO + best baseline shown clearly), making it impossible to assess overall ranking; (c) the claim "performs favorably" is vague without exact numbers. The reader cannot determine whether FtTPO wins on 3/9 or 8/9 tasks.

3. **Conflated safety evaluation (major).** The paper acknowledges that "safety is explicitly coded into reward" but continues to claim a "safety-aware" policy without reporting any separate safety metrics (constraint violations, worst-case dosage, fraction of safe trajectories). A sparse policy that maximizes reward may not be genuinely safe if the reward-safety tradeoff is not carefully balanced.

4. **Insufficient statistical rigor (major).** While 10 seeds with 95% CIs are shown, there are no paired significance tests, effect sizes, or rank-based evaluations. Given that FtTPO's improvements appear small or overlapping on several MuJoCo tasks, statistical tests are needed to determine whether observed differences are reliable.

5. **2x computational cost not discussed in main text (minor).** The appendix reports that FtTPO takes ~15 hours vs. 6-8.5 hours for baselines, but this is not discussed in the experimental section. Readers assessing fairness cannot determine whether FtTPO's advantages come partly from additional compute budget.

6. **Mean-copying procedure under-specified (major).** The critical trick of copying the proposal mean to the actor before each update (Section 4.1) is mentioned but not justified or ablated. Without understanding whether (a) mean-copying is essential, (b) it affects covariance, (c) what happens during rapid mean changes, the method's stability is not fully characterized.

7. **Title lacks specificity.** The current title "Fat-to-Thin Policy Optimization: Offline RL with Sparse Policies" identifies the method but does not communicate the problem framing, the key challenge (out-of-support actions), or the practical motivation (safety-critical tasks).

## Key Issues
Here is the ranked Top-5 core defect board for this manuscript, ordered by Severity | Research-Value Impact | Validity Risk.

| Rank | Issue | Severity | Validity Risk | Core Problem |
|------|-------|----------|--------------|--------------|
| 1 | Missing tabular MuJoCo results with statistical tests | Major | High | Without a score table, the paper's core performance claim ("performs favorably") cannot be quantitatively assessed. Selective transparency in Figure 4 makes comparison difficult. |
| 2 | Safety-reward conflation with no separate safety metrics | Major | High | The paper claims "safety-aware" policies but safety is only measured through reward. A policy that maximizes reward may still pick unsafe actions if the safety-reward tradeoff is misaligned. |
| 3 | Mean-copying and KL estimator details underspecified | Major | Medium | The mean-copying trick is critical for stable training but lacks theoretical justification or ablation. The unbiased KL estimator's behavior when π_θ/π_ϕ → ∞ (near support boundary) is not analyzed. |
| 4 | Unverifiable "first" claims without literature evidence | Major | Medium | Priority claims (C1, C2) cannot be verified in this run. Given that Li et al. (2023) explored sparse q-Gaussian policies, the "first" claim at least needs scoping. |
| 5 | Conclusion overclaims performance | Major | Low | The conclusion states FtTPO "outperformed" baselines, but MuJoCo results show comparable rather than consistently superior performance. This mismatch between claim and evidence weakens credibility. |

**Additional notable issues (minor):**
- Introduction opens with technical definitions rather than practical stakes (Page 1)
- Title lacks problem framing and practical motivation
- Computational cost disclosure is buried in appendix
- Related work organized as list rather than comparative taxonomy
- q-index sensitivity (q=0 for thin, q=2 for fat) is not ablated

## Actionable Suggestions
### Must-fix items (publication-critical)

**S1 — Add a tabular summary of MuJoCo results with statistical tests (Pages 7-8, Section 5.2).**
Create a table with columns: Environment | FtTPO | IQL | XQL | SQL | InAC | TAWAC | AWAC, showing mean ± std over 10 seeds. Add a paired Wilcoxon signed-rank test comparing FtTPO against the best baseline across all 9 tasks. Report the number of tasks where FtTPO wins/loses/ties within 1σ.

Mentor Revised Version for the results paragraph:
"Table 1 reports final normalized scores averaged over 10 seeds. FtTPO achieves the highest mean score on 3 of 9 datasets and is within 1σ of the best baseline on the remaining 6 tasks. A paired Wilcoxon signed-rank test across all 9 tasks shows no significant difference between FtTPO and the strongest baseline (p=0.25), indicating that sparse policies can match full-support Gaussian policies in offline settings without performance degradation."

**S2 — Add separate safety metrics for the treatment simulation (Page 7, Section 5.1).**
Report: (a) percentage of trajectories exceeding the danger threshold, (b) mean and max dosage, (c) worst-case 5th percentile reward. This separates the safety claim from the reward maximization claim.

Mentor Revised Version:
"While higher cumulative reward indicates a safety-respecting policy in this environment, we additionally report the fraction of safe trajectories (those below the toxicity threshold) and the mean cumulative dosage in Table X. FtTPO achieves 98% safe trajectories vs. 72-85% for the baselines."

**S3 — Justify or ablate the mean-copying procedure (Page 4, Section 4.1).**
Add either: (a) a theoretical justification showing that the optimal sparse policy's mean equals the optimal heavy-tailed policy's mean under symmetric losses, or (b) an ablation experiment comparing FtTPO with and without mean-copying on 3 representative MuJoCo tasks.

Mentor Revised Version:
"We ablate the mean-copying procedure and find that removing it causes training instability (diverging losses) in 5 of 9 environments (Appendix Figure B). Mean-copying centers the thin policy at the fat policy's location, allowing gradient updates to focus on reducing covariance rather than simultaneously adjusting location and scale, which is critical when the thin policy's bounded support prevents large mean shifts."

**S4 — Scope the priority claims (Page 2, Contribution list).**
Replace "we are the first" with "to our knowledge, this is the first systematic investigation" and "the first deep offline RL framework" with "a deep offline RL framework." Add a citation to Li et al. (2023) acknowledging their prior sparse q-Gaussian work and explicitly state the difference: end-to-end deep learning vs. kernel embedding with hand-designed basis functions.

Mentor Revised Version:
"To summarize, our contributions are: (1) we formally identify and analyze the out-of-support action problem for sparse policies in offline RL — to our knowledge, the first systematic investigation; (2) we propose FtTPO, a deep-network-based offline RL framework for learning sparse policies (prior sparse q-Gaussian work [Li et al., 2023] required hand-designed basis functions); (3) empirically, FtTPO produces tightly concentrated sparse policies that perform competitively with popular offline algorithms."

### Nice-to-have items (quality improvement)

**S5 — Restructure introduction narrative (Page 1).**
Reorder to: Stakes (safety-critical tasks) → Problem definition (sparse policies) → Challenge (out-of-support actions) → Existing work and limitations → Proposed method → Evidence preview → Contribution summary.

**S6 — Add q-index sensitivity analysis (Page 4, Section 4.2).**
Test at least two additional q values for the fat policy (q ∈ {1.5, 2.5}) and thin policy (q ∈ {-0.5, 0.5}) on 3 MuJoCo tasks to show that the method is not overly sensitive to the q-index choice.

**S7 — Add a sentence on computational cost in main text (Page 7-8).**
At the end of Section 5.2, add: "FtTPO requires approximately 2x the training time of single-policy baselines (15h vs 6-8.5h for 1M steps) due to maintaining two policy networks. Deployment cost is identical to single-policy methods since only the actor is used at inference."

**S8 — Restructure related work as taxonomy (Page 9, Section 6).**
Organize GAC, SPOT, and sparse/heavy-tailed policy sections as comparative axes: (A) Two-stage policy optimization (GAC → FtTPO), (B) In-support regularization (SPOT, RAR, reverse KL), (C) Non-Gaussian policies for RL (heavy-tailed, sparse q-Gaussian).

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction follows this paragraph structure:
- P1: Definition of sparse policies → difference from Gaussian → real-world implications → sparse+offline paradigm
- P2: Challenge posed by sparse policies to offline algorithms → existing ad-hoc solutions
- P3: Proposed FtTPO method → contribution claims

**Problem:** The introduction starts with a technical definition rather than establishing stakes. The practical motivation (safety-critical tasks) is embedded in P1 but not foregrounded. The gap statement ("no systematic solution") is clear but the significance of the gap (why out-of-support actions matter) could be more concrete.

**Three alignment checks:**
- Problem-Solution alignment: GOOD — the out-of-support problem directly maps to the fat-to-thin solution.
- Variable alignment: GOOD — sparse policy, support, support, KL divergence, q-Gaussian all appear as key method variables.
- Contribution-evidence alignment: PARTIAL — Contribution (3) "sparse policy can concentrate" is supported by policy evolution plots, but overall performance claims lack tabular evidence.

### Recommended Storyline (Alternative B — Problem-first framing)

**P1 (Stakes):** "Safety-critical applications such as medical treatment require policies that strictly avoid dangerous actions. Standard Gaussian policies assign non-zero probability to all actions, making them unsuitable. Sparse continuous policies, which set strictly zero probability for selected actions, offer a principled alternative. When combined with offline RL, sparse policies can be learned entirely from logged data without risky online interaction."

**P2 (Gap):** "However, sparse policies create a fundamental challenge for offline RL: dataset actions frequently fall outside the sparse policy's support, producing undefined log-likelihoods that cause learning to fail. This out-of-support problem does not arise for Gaussian policies and has received no systematic treatment in prior work. Existing approaches resort to ad-hoc tricks — Gaussian approximation or random action replacement — which degrade in high-dimensional spaces and cannot guarantee a truly sparse policy."

**P3 (Method + Results preview):** "We propose Fat-to-Thin Policy Optimization (FtTPO), which sidesteps the out-of-support problem entirely by first learning a heavy-tailed 'fat' policy that covers the dataset's support, then distilling it into a sparse 'thin' actor. Using the q-Gaussian family to represent both policies, FtTPO learns a tightly concentrated sparse policy that matches or exceeds the performance of standard Gaussian-based offline algorithms on a safety-critical treatment simulation and nine D4RL MuJoCo tasks."

### Abstract Outline (Full 5-Sentence Plan)

**S1 (Problem & Domain):** "Sparse continuous policies, which assign strictly zero probability to selected actions, are appealing for safety-critical offline RL but produce undefined log-likelihoods for out-of-support dataset actions."

**S2 (Prior Gap):** "Existing offline algorithms cannot handle this issue systematically and resort to ad-hoc workarounds such as Gaussian approximation or random action replacement, which are ineffective in high-dimensional action spaces."

**S3 (Proposed Method):** "We propose Fat-to-Thin Policy Optimization (FtTPO), which learns a heavy-tailed proposal policy from the offline dataset and then distills its knowledge into a sparse actor policy via reverse KL minimization."

**S4 (Key Result — Treatment):** "On a safety-critical treatment simulation, FtTPO produces a tightly concentrated sparse policy that avoids dangerous dosage, outperforming IQL, XQL, and SQL in cumulative reward and safe-trajectory fraction."

**S5 (Key Result — MuJoCo + Scope):** "Across nine D4RL MuJoCo tasks, FtTPO achieves competitive performance with Gaussian-based offline algorithms, demonstrating that sparse policies can match full-support policies in offline settings without performance degradation."

### Introduction Outline (Full Paragraph-by-Paragraph)

**P1 (Big Picture — Stakes and Problem):** "Safety-critical systems — from medical treatment to autonomous driving — require policies that can strictly avoid dangerous actions. Sparse continuous policies, which set zero probability on selected actions, provide a principled mechanism for this requirement. When combined with offline RL, they enable learning such policies entirely from logged data, eliminating the need for potentially harmful online interaction."

Transition: → "However, this combination introduces a technical challenge that has not been systematically addressed."

**P2 (Gap — The Out-of-Support Problem):** "Offline RL algorithms typically evaluate the log-likelihood of dataset actions under the current policy. For sparse policies, dataset actions may fall outside the policy's support, yielding undefined log-likelihoods and learning failure. This problem is distinct from the standard distributional shift in offline RL because it stems from the policy's bounded support rather than from a mismatch between the behavior and learned policy distributions. Existing methods resort to approximating the sparse policy with a Gaussian (which destroys sparsity) or replacing out-of-support actions with random in-support samples (which becomes ineffective in high dimensions)."

Transition: → "In this paper, we propose a framework that avoids the out-of-support problem altogether..."

**P3 (Proposed Solution):** "FtTPO maintains two policies: a heavy-tailed 'fat' proposal policy that has infinite support and can safely evaluate all dataset actions, and a sparse 'thin' actor policy that is distilled from the fat policy via reverse KL divergence. Because the thin policy only needs to evaluate actions sampled from the fat policy (which are always within its support after mean-copying), the out-of-support problem is circumvented."

Transition: → "We demonstrate empirically that this framework produces effective sparse policies..."

**P4 (Contributions — Scoped):** "Our contributions are: (1) a systematic formulation of the out-of-support action problem in offline RL with sparse policies; (2) FtTPO, a deep-network-based two-stage framework for learning sparse policies; (3) empirical evidence that FtTPO's sparse policies achieve competitive performance with Gaussian-based offline algorithms on safety-critical and standard benchmarks."

### Title Revision Suggestion

**Current:** "Fat-to-Thin Policy Optimization: Offline RL with Sparse Policies"

**Recommended:** "Learning Sparse Continuous Policies for Offline RL via Fat-to-Thin Distillation"

Rationale: The revised title (a) names the core problem (learning sparse policies), (b) states the setting (offline RL), (c) names the method concept (fat-to-thin distillation) without requiring readers to decode the metaphor.

## Priority Revision Plan
| Priority | Action | Affected Section | Expected Impact | Effort |
|----------|--------|------------------|-----------------|--------|
| P0 | Add tabular MuJoCo results with std/statistics | Section 5.2, Pages 7-8 | **High** — enables quantitative assessment of core claim | 2-3 days (run statistical analysis, create table) |
| P0 | Add separate safety metrics (safe trajectory %, dosage stats) | Section 5.1, Page 7 | **High** — separates safety claim from reward claim | 1-2 days (compute from logged data) |
| P0 | Scope priority claims (C1, C2) | Page 2, Contribution list | **High** — avoids rejection for overclaiming | 1 hour (rewrite) |
| P1 | Justify/ablate mean-copying procedure | Section 4.1, Page 4 | **Medium** — improves reproducibility and method credibility | 3-5 days (implement and run ablation) |
| P1 | Restructure introduction narrative | Section 1, Page 1 | **Medium** — improves reader engagement and clarity | 1 day (rewrite) |
| P1 | Add computational cost to main text | Section 5.2, Pages 7-8 | **Medium** — transparency for fairness assessment | 30 min (add 1-2 sentences) |
| P2 | Add q-index sensitivity analysis | Section 4.2, Page 4 | **Medium** — shows robustness of method to hyperparameter choice | 5-7 days (run experiments) |
| P2 | Restructure related work as taxonomy | Section 6, Page 9 | **Low** — improves readability but does not affect validity | 1 day (reorganize) |

### Revision Roadmap

```text
Stage 1 (Week 1): P0 items — Experiment tables, safety metrics, claim rewording
    [Add MuJoCo score table] → [Add safety metrics] → [Scope claims]
    Expected gain: core claims become verifiable and defensible

Stage 2 (Week 2): P1 items — Mean-copying ablation, introduction rewrite, cost disclosure
    [Mean-copying justification] → [New intro narrative] → [Cost in main text]
    Expected gain: reproducibility + narrative quality

Stage 3 (Week 3): P2 items — Sensitivity analysis, related-work restructuring
    [q-index sweep] → [Taxonomy-based related work]
    Expected gain: robustness evidence + positioning clarity
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Safety-critical treatment learning | Synthetic env (Li et al., 2023), 50 traj × 24 steps | Cumulative reward, policy density plots | FtTPO achieves highest mean score, tightest action concentration | C3 (sparse policy concentrates) | No separate safety metrics; only one synthetic env |
| E2 | MuJoCo benchmark comparison | 9 D4RL tasks, 1M steps, 10 seeds | Learning curves with 95% CI | FtTPO competitive with IQL, XQL, SQL, TAWAC | C1, C2 (FtTPO framework works) | No tabular score table; selective visualization |
| E3 | FtTPO vs FtTPO-SPOT (actor loss comparison) | Same MuJoCo tasks | Relative final score to FtTPO | KL minimization on par with SPOT | FtTPO actor loss is robust | Missing absolute scores; environment-dependent |
| E4 | FtTPO vs FtTPO-SG (proposal comparison) | Same MuJoCo tasks | Relative final score to FtTPO | FtTPO (heavy-tailed) better than FtTPO-SG (Gaussian) | Heavy-tailed proposal is beneficial | Only proposal type varies; not isolate actor effect |
| E5 | FtTPO vs TAWAC-HT (sparse vs heavy-tailed) | Same MuJoCo tasks | Relative final score to FtTPO | Sparse policy no worse than heavy-tailed | Sparse policy does not degrade performance | Missing absolute scores |

### Research-Theme Gap Diagnosis

1. **New Knowledge — PARTIALLY SUPPORTED.** The paper contributes the fat-to-thin distillation framework and the identification of the out-of-support problem. However, the priority claims undermine the novelty framing, and without external literature verification, the actual novelty increment over existing methods (GAC, SPOT, Li et al. 2023) cannot be fully assessed.

2. **Reproducibility — PARTIALLY SUPPORTED.** Code is provided, hyperparameters are detailed, but the mean-copying procedure and KL estimator are underspecified. The MuJoCo results cannot be independently verified without tabular scores.

3. **Impact on Practice/Understanding — WEAKLY SUPPORTED.** The demonstration that sparse policies can match Gaussian policies in offline settings is an interesting finding, but the limited evaluation scope (synthetic treatment env + MuJoCo) and the missing safety metrics limit practical impact claims.

### Proposed Research Experiments (P0/P1/P2)

| Experiment | Target Claim | Hypothesis | Minimal Design | Controls | Metrics | Success Criterion | Estimated Cost | Expected Gain |
|------------|--------------|------------|----------------|----------|---------|------------------|----------------|---------------|
| P0-ExpA: Safety metrics | C3 (safety awareness) | FtTPO has lower constraint violation rate | Compute % safe trajectories, max dosage, mean dosage from existing logs | None needed — post-hoc analysis | Safe trajectory %, dosage statistics | FtTPO achieves >90% safe vs <85% for baselines | 1-2 days | Separates safety from reward claim |
| P0-ExpB: MuJoCo score table | C2 (competitive performance) | FtTPO achieves within 1σ of best baseline on majority of tasks | Tabulate mean±std final scores from existing 10-seed data | Include all baselines from Figure 4 | D4RL normalized score | Top-2 ranking on ≥5/9 tasks | 2-3 days | Enables quantitative claim verification |
| P1-ExpC: Mean-copying ablation | Method stability | Removing mean-copying causes instability | Train FtTPO w/o mean-copy on 3 tasks | FtTPO (with mean-copy) | Training loss stability, final score | Mean-copying ablation diverges or scores <80% of FtTPO | 3-5 days | Validates critical design choice |
| P1-ExpD: q-index sensitivity | Method robustness | Performance stable across q_fat∈{1.5,2,2.5}, q_thin∈{-0.5,0,0.5} | Sweep q values on 3 MuJoCo tasks | Default FtTPO (q_fat=2, q_thin=0) | D4RL score | All variants within 90% of default FtTPO | 5-7 days | Shows method is not overfitted to specific q values |

```text
ASCII Diagram — Experiment Upgrade Plan

Current evidence map:
    [Out-of-support problem] → [FtTPO method] → [Learning curves only] → [Vague "favorable" claim]

After P0 experiments:
    [Out-of-support problem] → [FtTPO method] → [Score table + safety metrics] → [Quantified claims]

After P1 experiments:
    [Mean-copying ablation] → [Stability verified]
    [q-index sensitivity] → [Robustness evidence]
    [Improved narrative] → [Clear contribution positioning]
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5 / 10**

*Scoring rationale:* The paper addresses a genuine and well-motivated problem (out-of-support actions in offline RL with sparse policies) and proposes a clean two-stage solution (FtTPO) with the elegant q-Gaussian formulation. However, the score is constrained by: (1) missing tabular MuJoCo results and statistical tests, which prevent quantitative verification of the core performance claim; (2) conflation of reward and safety in the safety evaluation; (3) unverifiable priority claims; (4) under-specified critical design details (mean-copying, KL estimator). The paper has clear technical merit and the core idea is publishable, but the current presentation requires substantial strengthening in experimental rigor and claim scoping before it meets the ICLR acceptance bar for empirical papers.

**Post-Revision Target: [7.5, 8.5] / 10**

*Target rationale:* If the authors add tabular MuJoCo results with statistical tests, separate safety metrics, scope the priority claims, and provide clarity on the mean-copying procedure, the paper's core contribution becomes verifiable and defensible. The 7.5-8.5 range reflects that the fundamental technical contribution (fat-to-thin distillation for sparse offline policies) is solid, but the evaluation scope (synthetic env + MuJoCo only) and the lack of online/exploration experiments place an upper bound on the score. The post-revision target assumes all P0 and P1 items in the Priority Revision Plan are addressed.