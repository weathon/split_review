## Summary
# Final Review Report

## Summary

This paper proposes GOODRL (Graph-assisted Offline-Online Deep Reinforcement Learning) for Dynamic Workflow Scheduling (DWS) in cloud computing. The paper makes three main technical contributions: (1) a task-specific graph representation with a Graph Attention Actor Network that evaluates each task-machine pair separately to improve action differentiation; (2) a system-oriented graph representation with a Graph Attention Critic Network that uses bi-directional edges and self-attention for comprehensive state evaluation under dynamic workflow arrivals; and (3) an offline-online training framework that uses imitation learning from HEFT for pre-training, followed by PPO with gradient control and decoupled high-frequency critic updates for stable online adaptation.

The paper is well-structured, the problem is practically important, and the method is technically sound overall. Experiments across 12 offline and 6 online scenarios show that GOODRL consistently achieves lower mean flowtime than expert-designed heuristics (EST, PEFT, HEFT), GPHH, and a transformer-based DRL baseline (ERL-DWS). The ablation studies validate the architectural choices, and appendices provide additional evidence on scalability, transferability to FJSS, and multi-objective extensibility.

**Key strengths:** Clear problem motivation, innovative dual-graph representation design, comprehensive experiments across varying scales, open-sourced code and data.

**Key weaknesses:** GPHH baseline comparison uses best-of-30-runs reporting which inflates apparent GPHH performance and is not a standard comparison practice; online learning gains over offline are modest (≤1.24%) with their practical significance claim not fully evidenced; the gradient control mechanism uses a hard gradient-zeroing strategy rather than soft clipping; reward sparsity and off-policy buffer issues are not discussed. Novelty verification is deferred due to unavailability of external literature search in this run.

## Strengths
**S1. Practical and well-motivated problem.** Dynamic Workflow Scheduling with heterogeneous machines and unpredictable arrivals is a realistic and under-explored problem in cloud computing. The paper clearly articulates why existing methods (static heuristics, GPHH, vector/matrix-based RL representations) are insufficient, establishing a strong motivation for the proposed approach.

**S2. Innovative dual-graph representation design.** Separating the graph representation for the actor (task-specific, per-action-pair) and critic (system-oriented, full-state) is a novel architectural choice with a clear rationale: the actor needs discriminative power to differentiate actions, while the critic needs holistic context for value estimation. The ablation studies (Appendix F, G) convincingly demonstrate the benefit of each design element (pairwise processing, focused embedding, bi-directional edges, self-attention).

**S3. Comprehensive experimental evaluation.** The paper evaluates across 12 offline and 6 online scenarios with varying workflow counts (1k-20k), machine configurations (5×5, 6×4), arrival rates (λ=5.4, 9), and workflow patterns (Montage, CyberShake, SIPHT, Inspiral). The appendices further demonstrate scalability to pattern/rate/machine changes, transferability to FJSS, and extensibility to multi-objective cost optimization — going well beyond a single-task evaluation.

**S4. Good reproducibility practices.** The code and data are publicly available on GitHub, hyperparameters are documented in detail (Appendix J), and the paper reports hardware/software configurations. This significantly increases the potential impact of the work by allowing direct comparison and extension.

**S5. Open-sourced offline-online training framework.** The two-stage PPO training with imitation learning pre-training and online fine-tuning is practically valuable. The gradient control mechanism and decoupled high-frequency critic training are simple but effective techniques that address the real challenge of adapting scheduling policies under distribution shift, as evidenced by the noise-injection robustness experiments.

## Weaknesses
**W1. GPHH baseline comparison uses non-standard best-of-30-runs reporting.** (Severity: Major) The paper compares GOODRL against GPHH by taking the minimum mean flowtime from the top-3 heuristics evolved across 30 independent runs. This introduces positive selection bias and does not reflect expected GPHH performance. Appendix K shows extreme variance (e.g., GPHH-top1=5314.9 vs GPHH-min=300.2 in scenario ⟨6×4, 9, 1k⟩), confirming that the minimum is not representative. The two scenarios where GPHH marginally beats GOODRL (gaps 1.24%, 0.15%) may not hold if expected (mean) GPHH performance were used.

**W2. Online learning gains over offline are modest and the claimed practical significance is not directly evidenced.** (Severity: Major) The online PPO fine-tuning improves mean flowtime by at most 1.24% over the offline-only agent, and in one scenario the offline agent outperforms the online one. The paper argues these small gains translate to substantial cost savings by referencing Appendix R (Table 20), but Table 20 compares two distinct scheduling plans with different reward functions, not Ours-Offline vs Ours-Online. The connection between online learning and cost savings is not established by the presented data.

**W3. Gradient control uses hard gradient zeroing instead of soft clipping.** (Severity: Medium) When the gradient L2-norm exceeds the threshold, the gradient is set to zero (no update) rather than being clipped to the threshold. This binary strategy may freeze the actor during sustained distribution shifts. While experiments show recovery within 150 iterations, the mechanism's behavior under persistent non-stationarity is not analyzed.

**W4. Reward sparsity and its impact on learning are not discussed.** (Severity: Medium) The reward is only non-zero when one or more workflows complete between consecutive decision steps. With long workflows (e.g., Inspiral: 29.41h total workload), many consecutive steps may yield $r_t = 0$. The paper does not discuss how PPO handles this sparsity, whether advantage estimation (GAE) mitigates it, or whether auxiliary per-task rewards were considered.

**W5. Novelty verification is incomplete (deferred due to retrieval unavailability).** (Severity: Informational) External literature search was not available in this review run. The paper's claims of novelty — particularly the dual-graph representation for DWS, the pairwise (s,a) processing in the actor, and the offline-online training framework — require external verification against related work in GNN-based scheduling, offline-online RL for combinatorial optimization, and dynamic scheduling with heterogeneous resources.

## Key Issues
**Issue 1 (Critical): GPHH baseline reporting inflates apparent performance.** [Evidence: Page 8-9, Table 1, Appendix K] The paper selects the minimum from the top-3 heuristics across 30 GPHH runs. This is not standard practice and introduces positive selection bias. Appendix K reveals extreme variance: in scenario ⟨6×4, 9, 1k⟩, GPHH-top1 = 5314.90 while the selected minimum = 300.20. Without standard deviation or mean reporting, readers cannot assess whether GOODRL's marginal losses (1.24%, 0.15%) to GPHH in two scenarios are statistically meaningful.

**Fix requirement (Must):** Re-report all GPHH results as mean ± std across 30 runs. Add statistical significance tests against each baseline. If the best-of-30 approach is maintained (as a supplement), clearly disclose this and also report the full distribution.

**Issue 2 (Major): Online learning's practical significance is overstated.** [Evidence: Page 9-10, Table 2, Appendix R] The paper claims small flowtime improvements translate to substantial cost savings, citing Appendix R. However, Table 20 compares two different scheduling plans (not Ours-Offline vs Ours-Online) under a multi-objective reward that includes cost. The 0.84% flowtime → 36.11% cost reduction claim conflates two separate experiments.

**Fix requirement (Must):** Separate the claims: (a) online learning provides consistent but modest flowtime improvements over offline-only (Table 2 supports this); (b) multi-objective reward modification can achieve cost-flowtime trade-offs (Appendix O supports this). Do not imply online learning directly causes large cost savings.

**Issue 3 (Major): Gradient control mechanism uses hard gradient-zeroing.** [Evidence: Page 7, Section 4.3.2] The gradient is set to zero vector when threshold is exceeded, rather than scaled down. This may freeze learning under sustained distribution shifts.

**Fix requirement (Must):** Compare):** Replace hard zeroing with standard gradient clipping: $\nabla_\theta J = \frac{\tau_0}{\|\nabla_\theta J\|_2} \nabla_\theta J$ when the norm exceeds $\tau_0$. Add an ablation comparing hard-zero vs soft-clip in Appendix L.

**Issue 4 (Medium): Reward sparsity not discussed.** [Evidence: Page 5, Rewards paragraph] The reward is only non-zero when workflows complete between steps. With workflows taking up to 29.41 hours and many task assignments per workflow, the reward signal may be extremely sparse. The paper does not address how PPO handles this.

**Fix requirement (Nice-to-have):** Add a brief paragraph discussing reward sparsity, noting whether GAE or other techniques compensate, and reporting the average proportion of non-zero reward steps during training.

**Issue 5 (Medium): Critic mean pooling vs actor focused embedding inconsistency not justified.** [Evidence: Page 6, Section 4.2.2] The critic uses mean pooling over all node embeddings, which the actor section criticizes as dilutes information. The paper does not explain why mean pooling is acceptable for the critic but not the actor.

**Fix requirement (Nice-to-have):** Add a justification explaining that value estimation requires a stable, low-variance aggregate of system state, while action selection requires discriminative signals concentrated on the focused task.

## Actionable Suggestions
**Suggestion 1 (Must): Revise GPHH baseline reporting. baseline reporting.** Replace the best-of-30-runs reporting with mean ± std across all 30 runs. Add a paired statistical significance test (e.g., Wilcoxon signed-rank) comparing GOODRL against each baseline across the 30 instances per scenario. If the best-of-30 approach is retained as supplementary, clearly disclose the selection procedure and report the full distribution (min, median, max, std) in the main table.

**Suggestion 2 (Must): Separate online learning claims from multi-objective cost claims.** In Section 5.3 and the Conclusion, clearly distinguish: (a) online learning provides consistent but modest flowtime improvements (0.36%-1.24%) over offline-only, and (b) multi-objective reward modification (Appendix O) can achieve cost savings of up to 41% with slight flowtime increases. Remove the implication that online learning directly causes large cost savings, as this conflates two different experimental setups.

**Suggestion 3 (Must): Replace hard gradient zeroing with soft clipping.** In Section 4.3.2, change the gradient control from:
```
∇θJ = { ∇θJ, if ||∇θJ||2 ≤ μprev+σprev and ||∇θJ||2 ≤ τ0; 0, otherwise }
```
to standard gradient clipping:
```
∇θJ = { ∇θJ, if ||∇θJ||2 ≤ τ0; (τ0/||∇θJ||2)·∇θJ, otherwise }
```
Add an ablation in Appendix L comparing hard-zero vs soft-clip to demonstrate which yields better online adaptation under sustained distribution shift.

**Suggestion 4 (Nice-to-have): Discuss reward sparsity.** Add a paragraph in Section 4.1 or 4.3 discussing: (a) the proportion of non-zero reward steps observed during training, (b) whether Generalized Advantage Estimation (GAE) is used to mitigate sparsity, and (c) whether auxiliary per-task completion rewards were considered and why they were or were not adopted.

**Suggestion 5 (Nice-to-have): Justify critic mean pooling vs actor focused embedding.** Add one sentence in Section 4.2.2 explaining why mean pooling is appropriate for the critic's value estimation but not for the actor's action selection. Suggested wording: "For value estimation, mean pooling provides a stable, low-variance summary of overall system load, which is suitable for predicting long-term returns, whereas action selection requires discriminative signals concentrated on the focused task."

**Suggestion 6 (Nice-to-have): Add computational complexity analysis for pairwise processing.** In Section 4.2.1, add a brief note on the computational cost of per-action-pair processing: "Our pairwise design requires |M| forward passes per decision step. In our experiments with up to 30 machines, this yields 6-7 ms per decision. For larger machine pools, these passes can be trivially parallelized as independent batch computations."

**Suggestion 7 (Nice-to-have): Add explicit mean flowtime equation in Problem Formulation.** In Section 3, add a numbered equation for the objective: $\bar{F} = \frac{1}{|W|} \sum_{i=1}^{|W|} (ft_i - at_i)$ to complement the verbal description.

**Suggestion 8 (Nice-to-have): Strengthen conclusion limitations.** In Section 6, add a concrete limitation statement: "A limitation of the current study is the assumption of FIFO queue execution and flowtime-only optimization. Extending GOODRL to support priority-based queuing, deadline constraints, and multi-objective trade-offs are natural next steps."

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows a traditional academic structure: (P1) cloud computing context → DWS definition → challenges; (P2) limitations of existing heuristics (hand-crafted, GPHH); (P3) limitations of existing RL/GNN methods; (P4) proposed method (three contributions). The narrative is technically complete but could be more engaging and better structured for non-expert readers. The main issues are: (1) P3 mixes L2O background, vector/matrix limitations, and GNN limitations in one dense paragraph, making it hard to track the logical chain; (2) the gap between problem and solution is not crisply stated before the contribution list.

### Proposed Storyline Option (Recommended)

**Big Picture → Concrete Gap → Method Intuition → Key Evidence → Contribution Summary**

- **P1:** Start with the practical importance of cloud workflow scheduling and the specific challenge of DWS (heterogeneous machines, unpredictable arrivals). End with a single, sharp sentence stating the gap: "Existing scheduling methods fail to address all three dynamic aspects simultaneously — heterogeneity, unpredictability, and evolving state — creating a gap between current solutions and real-world needs."
- **P2:** Briefly survey existing approaches (heuristics → GPHH → RL-based) and explain why each falls short for DWS, using a clear contrastive structure rather than a literature list.
- **P3:** State the method intuition in plain language before listing technical contributions: "We address this gap through three interlocking innovations: a task-specific graph that captures machine-task interactions at both topology and feature levels, a system-oriented graph that tracks global workflow dynamics, and an offline-online training framework that combines imitation learning with stable online adaptation."
- **P4:** Preview key experimental outcomes with concrete numbers: "Across 12 offline and 6 online scenarios, GOODRL consistently achieves the lowest mean flowtime, with average rank 1.17 vs 1.92 for the best baseline."

### Abstract Outline (Complete)

**S1 (Problem):** "Dynamic workflow scheduling (DWS) in cloud computing requires assigning tasks from unpredictably arriving workflows to heterogeneous machines while minimizing mean flowtime."
**S2 (Challenge):** "Existing methods either rely on static heuristics that ignore real-time dynamics or use graph representations with fixed structures that cannot accommodate varying workflow counts."
**S3 (Gap):** "A key challenge is simultaneously handling heterogeneous machine configurations, unpredictable workflow arrivals, and constantly evolving system states — aspects not jointly addressed by prior work."
**S4 (Method):** "We propose GOODRL, which introduces a task-specific graph and actor network for per-machine action evaluation, a system-oriented graph and critic network for global state assessment, and an offline-online training scheme that combines imitation learning with gradient-controlled PPO for stable adaptation."
**S5 (Result):** "Experiments across 12 offline and 6 online scenarios show GOODRL achieves the lowest mean flowtime with average rank 1.17, outperforming expert-designed heuristics, genetic programming hyper-heuristics, and transformer-based DRL methods."

### Introduction Outline (Complete)

**P1 Role:** Establish the practical importance and define DWS. End with gap statement.
**P2 Role:** Survey existing solution families (heuristics, GPHH, RL/GNN) and their specific limitations for DWS. Use contrastive structure. End by motivating need for new representations and learning methods.
**P3 Role:** Present method intuition in plain language. This is the transition paragraph. Do not list contributions yet.
**P4 Role:** List three contributions with evidence anchors (reference tables/figures/appendices for each). End with paper organization statement.

## Priority Revision Plan
### P0 (Must, immediate — affects validity of comparisons)

| Priority | Action | Section Affected | Effort | Expected Impact |
|----------|--------|-----------------|--------|-----------------|
| P0 | Re-report GPHH as mean±std (30 runs), add significance tests | Section 5.2, Table 1, Appendix K | Medium (re-computation) | Establishes fair comparison; may change SOTA claims |
| P0 | Replace hard gradient zeroing with soft clipping in gradient control | Section 4.3.2, Appendix L | Low (code change) | Improves adaptation under sustained distribution shift |
| P0 | Separate online learning claims from multi-objective cost claims | Section 5.3, Section 6 | Low (text revision) | Removes rhetorical overreach; improves defensibility |

### P1 (High priority — improves scientific rigor)

| Priority | Action | Section Affected | Effort | Expected Impact |
|----------|--------|-----------------|--------|-----------------|
| P1 | Add online learning ablation: report Ours-Online improvement over Ours-Offline with confidence intervals | Section 5.3, Table 2 | Low (re-analysis) | Quantifies online learning benefit with statistical reliability |
| P1 | Discuss reward sparsity and GAE mitigation | Section 4.1, Section 4.3 | Low (text addition) | Addresses algorithmic transparency concern |
| P1 | Add explicit mean flowtime equation in Problem Formulation | Section 3 | Low (text addition) | Improves clarity of objective |

### P2 (Nice-to-have — improves presentation and completeness)

| Priority | Action | Section Affected | Effort | Expected Impact |
|----------|--------|-----------------|--------|-----------------|
| P2 | Justify critic mean pooling vs actor focused embedding | Section 4.2.2 | Low (text addition) | Resolves apparent design inconsistency |
| P2 | Add computational complexity note for pairwise processing | Section 4.2.1 | Low (text addition) | Addresses scalability concern |
| P2 | Strengthen conclusion limitations (FIFO, single-objective) | Section 6 | Low (text revision) | Improves scientific honesty |
| P2 | Restructure introduction for clearer narrative flow | Section 1 | Medium (rewrite) | Improves reader engagement |

### Revision Timeline

1. **Week 1 (P0):** Fix GPHH reporting, gradient clipping, and claim separation. These are the highest-impact fixes and require mostly re-analysis or text changes.
2. **Week 2 (P1):** Add confidence intervals, reward sparsity discussion, and equation fixes. These fill the main scientific gaps identified in the review.
3. **Week 3 (P2):** Address presentation improvements, narrative restructuring, and limitation statements.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|--------------|-----------------|-------------------|
| E1 | Offline comparison across 12 scenarios | 30 instances, 1k-5k workflows, 4 patterns, 2 arrival rates, 2 machine configs | Mean flowtime, Gap% | GOODRL avg rank 1.17; beats all baselines | C1 (task-specific graph) + C3 (offline learning) | GPHH reported as best-of-30; no significance tests |
| E2 | Online comparison across 6 scenarios | Pre-trained on ⟨5×5,5.4⟩, tested on 6×4 with 5k-20k workflows | Mean flowtime, Gap% | Ours-Online rank 1.17; gains 0.36-1.24% over Ours-Offline | C2 (system-oriented graph) + C3 (online learning) | Gains modest; one scenario Ours-Offline better |
| E3 | Actor architecture ablation (TSEM) | Imitation learning cross-entropy loss | Cross-entropy over 900 iterations | Ours-TSEM lowest loss vs w/o pair and w. mean | C1 (pairwise processing, focused embedding) | Only tested on imitation task, not final PPO policy |
| E4 | Critic architecture ablation (SOEM) | Value loss (MSE) | Value loss over 900 iterations | Ours-SOEM lowest loss vs w/o edge and w/o self | C2 (bi-directional edges, self-attention) | Only tested on value prediction accuracy |
| E5 | Online learning ablation | Mean flowtime improvement over Ours-Offline | Improvement % at 150-250 iterations | Ours-Online +1.5%; w/o grad -1.2%; w/o freq -184% | C3 (gradient control, decoupled critic) | w/o freq degrades catastrophically; analysis needed |
| E6 | Scalability to changes | Changed workflow patterns, arrival rates, machine configs | Mean flowtime | GOODRL maintains competitive performance | C1+C2 (graph generalization) | Tested on limited configs; no statistical tests |
| E7 | Transferability to FJSS | 4 FJSS instances (10×5, 20×5, 30×10, 40×10) | Makespan | GOODRL competitive with DRL-G, DRL-S on 20×5, 30×10, 40×10 | Method transferability | Worse than DRL-S on 10×5; not tested on DRL-R |
| E8 | Multi-objective extensibility | Added cost to reward function | Flowtime, Cost | Cost savings up to 41%; flowtime increase up to 8% | Extensibility | Small-scale (30 workflows); single weight setting |

### Research-Theme Gap Diagnosis

The paper's core claims about new knowledge center on the dual-graph representation design (C1, C2) and the offline-online training framework (C3). The experimental evidence supports these claims internally (ablation studies confirm design choices; offline/online comparisons confirm performance gains). However, three gaps remain:

1. **GPHH comparison fairness gap:** The primary SOTA comparison uses non-standard reporting, undermining confidence in the comparative advantage.
2. **Online learning value gap:** The claimed practical significance of online learning (through cost savings) is not directly evidenced by the Ours-Offline vs Ours-Online comparison.
3. **Novelty verification gap:** Without external literature search, the paper's position relative to prior GNN-based scheduling methods cannot be fully assessed.

### Proposed Research Experiments (P0/P1/P2)

**P0 Experiment: GPHH statistical re-analysis**
- **Target Claim:** GOODRL outperforms GPHH (Table 1)
- **Hypothesis:** With proper mean±std reporting, GOODRL wins in all scenarios
- **Design:** Re-run GPHH 30 times, compute mean±std per scenario; apply Wilcoxon signed-rank test
- **Controls:** Same 30 instances per scenario; same GPHH config as Appendix K
- **Metrics:** Mean flowtime, std, p-value, effect size
- **Success Criterion:** GOODRL significantly better (p<0.05) in ≥10/12 scenarios
- **Cost:** Re-analysis (no new computation needed)
- **Expected Gain:** Establishes fair comparison; supports SOTA claim

**P1 Experiment: Online learning cost-benefit analysis under distribution shift**
- **Target Claim:** Online learning provides practical benefits (Section 5.3)
- **Hypothesis:** Online learning's benefit is larger under distribution shift than in stationary conditions
- **Design:** Compare Ours-Offline vs Ours-Online under 3 shift types (arrival rate change, machine failure, workflow pattern change) with controlled magnitude
- **Controls:** Fixed pre-trained actor; identical initial conditions
- **Metrics:** Mean flowtime, recovery time (iterations to within 2% of stationary performance)
- **Success Criterion:** Online learning shows ≥3% improvement under at least one shift type
- **Cost:** ~20 CPU hours (reusing existing simulator)
- **Expected Gain:** Quantifies the practical value of online learning

**P1 Experiment: Gradient control mechanism comparison**
- **Target Claim:** Gradient control stabilizes online learning (Section 4.3.2)
- **Hypothesis:** Soft gradient clipping yields faster recovery than hard zeroing under sustained shift
- **Design:** Compare hard-zero (current), soft-clip (proposed), and no gradient control in Online w/o grad setup
- **Controls:** Same initial actor, same shift schedule
- **Metrics:** Mean flowtime, gradient norm trajectory, policy entropy change
- **Success Criterion:** Soft-clip achieves ≥5% better final flowtime than hard-zero under distribution shift
- **Cost:** ~10 CPU hours
- **Expected Gain:** Improves algorithmic robustness

**P2 Experiment: Reward structure analysis**
- **Target Claim:** The RL formulation is effective (Section 4.1)
- **Hypothesis:** Dense reward (per-task) improves sample efficiency without degrading final policy quality
- **Design:** Compare sparse reward (current: workflow completion only) vs dense reward (negative sum of per-task completion times) in offline PPO
- **Controls:** Same actor/critic architecture, same training steps
- **Metrics:** Mean flowtime, value loss, training steps to convergence
- **Success Criterion:** Dense reward achieves same final flowtime in ≤80% of training steps
- **Cost:** ~30 CPU hours (re-training)
- **Expected Gain:** Quantifies whether reward sparsity is a practical concern

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Scoring Rationale

This paper tackles a practically important problem (DWS) with a methodologically sound approach. The dual-graph representation and offline-online training framework are technically innovative and well-supported by ablation studies. The experimental evaluation is comprehensive in scale and coverage.

However, three factors constrain the score: (1) the GPHH baseline comparison uses non-standard best-of-30 reporting, which must be corrected before the comparative claims can be fully trusted; (2) the online learning gains are modest (≤1.24%) and their claimed practical significance is not directly evidenced; and (3) novelty verification is deferred due to unavailability of external literature search in this review run. The paper is at an ICLR 2025 accepted level with fixable weaknesses.

**Final Score: 7/10**

*Justification:* The paper has clear technical contributions (dual-graph representation, offline-online training), strong experimental methodology (comprehensive scenarios, open code), and is accepted at a top venue. The GPHH baseline reporting issue and overstated online learning claims are fixable. Without external novelty verification, the score primarily reflects the paper's internal evidence quality and technical soundness.

**Post-Revision Target: [7.5, 8.5]/10**

*Justification:* If the authors fix the GPHH reporting (mean±std + significance tests), correct the online learning claim separation, replace hard gradient zeroing with soft clipping, and the novelty holds up under external verification, the paper could achieve a score of 8-8.0-8.5. The floor of 7.5 assumes at least the P0 fixes are completed. The ceiling of 8.5 assumes all P0 and P1 fixes plus external novelty confirmation.

### Page Coverage Audit

| Page | Annotation Count | Coverage Status | Notes |
|------|-----------------|-----------------|-------|
| 1 (Abstract + Intro P1-P2) | 3 | Covered | Abstract structure, intro gap, heuristics paragraph |
| 2 (Intro P3-P4 + Related Work) | 3 | Covered | L2O paragraph, contribution paragraph, related work |
| 3 (Problem Formulation + Method start) | 1 | Covered | Problem formulation |
| 4 (Method: RL formulation) | 1 | Covered | Reward sparsity noted |
| 5 (Task-specific graph) | 1 | Covered | Pairwise processing efficiency |
| 6 (Critic network) | 1 | Covered | Mean pooling justification |
| 7 (Online learning) | 1 | Covered | Gradient control mechanism |
| 8 (Experiment setup + offline results start) | 1 | Covered | GPHH baseline issue |
| 9 (Offline results cont. + online results) | 1 | Covered | Online learning claim separation |
| 10 (Conclusion) | 1 | Covered | Limitation specificity |
| 11-14 (References) | 0 | Skipped (non-substantive) | Standard references |
| 15-29 (Appendices) | 1 | Covered | Online PPO algorithm buffer concern |
| **Total** | **15** | **Adequate coverage** | |