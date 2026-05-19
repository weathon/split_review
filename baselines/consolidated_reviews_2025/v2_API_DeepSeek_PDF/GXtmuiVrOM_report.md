## Summary
This paper introduces DORAEMON (DOmain RAndomization via Entropy MaximizatiON), a constrained optimization framework for automatically shaping the dynamics-parameter sampling distribution in Domain Randomization (DR) for sim-to-real Reinforcement Learning. The core idea is to maximize the entropy of the training distribution (i.e., increase the diversity of sampled dynamics parameters) subject to a constraint that the policy's in-distribution success rate remains above a threshold α. This formulation removes the need for manual distribution tuning or real-world data.

The method is implemented through a decoupled optimization loop: a policy is trained with SAC + history conditioning + asymmetric actor-critic, while the dynamics distribution (parameterized as independent Beta distributions) is updated by solving a constrained entropy-maximization problem. An importance-sampling estimator reuses training data to evaluate the success-rate constraint, and a backup optimization (Eq. 6) provides recovery when constraint violations occur.

Experiments on six MuJoCo benchmarks (CartPole, SwingUpCartpole, Hopper, Walker2D, HalfCheetah, Swimmer) show that DORAEMON achieves higher global success rates than four baselines (No-DR, Fixed-DR, LSDR, AutoDR). A real-world validation on a 7-DoF PandaPush task (17 randomized dynamics parameters) demonstrates 60% zero-shot sim-to-real success rate versus 46.7% for the best baseline (LSDR), though with limited statistical power (30 real-world rollouts).

**Research Value**: The paper addresses a practical problem (automatic DR distribution shaping) with a clean, principled formulation (entropy maximization + success-rate constraint). The main conceptual contributions are: (C1) a constrained entropy-maximization framing for automatic DR, (C2) a sample-efficient algorithmic implementation with IS-based estimation and backup recovery, and (C3) empirical validation across diverse tasks including a real robot. The paper is well-structured, the method is clearly explained, and the experimental design is thorough for the simulated benchmarks. Key limitations include the statistical power of the real-world evaluation, reliance on a hand-defined success indicator, and potential performance collapse under overly aggressive entropy growth.

## Strengths
**S1. Clean, principled formulation.** The constrained entropy-maximization formulation (Eq. 3) is elegant and directly addresses the core challenge of automatic DR: how to widen the distribution without collapsing policy performance. The use of a success-probability constraint (rather than average return) is well-motivated, as it is robust to catastrophic failures on infeasible dynamics. The KL trust-region constraint (Eq. 4) provides a principled mechanism for gradual distribution growth.

**S2. Sample-efficient distribution updates.** By using importance sampling to estimate the success rate under candidate distributions from existing training data (Eq. 5), DORAEMON avoids costly Monte-Carlo rollouts that prior methods (LSDR, SPDL) require. This is a genuine practical advantage.

**S3. Thorough ablation and sensitivity analysis.** Appendix B provides a careful dissection of DORAEMON's components from the perspective of self-paced curriculum learning (Fig. 13), showing that each design choice (history conditioning, asymmetric actor-critic, backup optimization) contributes measurably to performance. The sensitivity analysis of the trust-region size ϵ (Fig. 8) and the success-rate threshold α (Fig. 10) is thorough and informative.

**S4. Comprehensive simulated benchmarks.** Six MuJoCo environments with varying dimensionality (2D to 13D) provide a robust evaluation of the method's scalability. The comparison against four baselines (No-DR, Fixed-DR, LSDR, AutoDR) is fair and well-documented, with per-environment hyperparameter tuning.

**S5. Real-world validation.** The PandaPush task is a well-designed real-world benchmark for studying adaptive behavior under unknown dynamics. The 17-dimensional randomization space and the center-of-mass variation create a genuinely challenging sim-to-real problem. The project website with video demonstrations is a valuable supplement.

**S6. Honest limitations section.** The Limitations paragraph (Section 6) acknowledges the potential for catastrophic forgetting during backtracking and suggests a concrete mitigation (KL constraint on policy parameters). This transparency is commendable.

## Weaknesses
**W1. [Major] Underpowered real-world evaluation.** The Sim2Real comparison (Table 1) is based on only 30 real-world rollouts (3 per seed × 10 seeds). For a binary outcome, the 95% confidence interval for DORAEMON's 60% success rate spans approximately 41-77%, which overlaps substantially with LSDR's 46.7% (~29-65%). The headline claim of "superior performance" on the real robot is therefore not statistically supported.

**W2. [Major] IS estimator variance not analyzed.** The importance-sampling estimator (Eq. 5) is central to DORAEMON's sample efficiency, but the paper provides no analysis of its variance or effective sample size. As the distribution ν_φ widens, the IS weights can degenerate, especially in high-dimensional parameter spaces (e.g., 17D PandaPush). The paper acknowledges potential overestimation and adds a backup optimization, but does not quantify when the estimator becomes unreliable.

**W3. [Medium] Limited novelty relative to self-paced curriculum learning.** The constrained optimization formulation (Eq. 3) is closely related to self-paced curriculum learning methods [Klink et al. 2020a,b], differing primarily in (a) using entropy maximization rather than I-projection, (b) operating on latent (unobserved) dynamics parameters rather than observable contexts, and (c) the backup optimization (Eq. 6). While these differences are non-trivial, the conceptual overlap is significant. The paper's novelty lies more in the application to DR than in a fundamentally new optimization framework.

**W4. [Medium] Success indicator shifts rather than eliminates tuning.** DORAEMON replaces manual distribution tuning with manual success-indicator tuning. Defining σ(τ) requires choosing return thresholds or distance thresholds, which may require as much domain expertise as tuning distribution parameters. The paper acknowledges this briefly but does not discuss how sensitive results are to the choice of success threshold.

**W5. [Minor] Promotional language in abstract and conclusion.** Terms like "remarkable Sim2Real transferability," "significant step," and "highly adaptive and generalizable policies" overstate the evidence, which is based on one real-world task with limited statistical power and six simulated benchmarks.

**W6. [Minor] Missing quantitative success-cell analysis for HalfCheetah.** Fig. 3 visually shows DORAEMON covering more success cells, but no numerical count is provided. This is a missed opportunity for quantitative evidence.

**W7. [Minor] Eq. (4) formatting issue.** The two constraints in Eq. (4) are not separated by punctuation, which could cause misreading.

**W8. [Deferred] Novelty verification.** Due to Retrieval-Disabled Mode (external paper search unavailable), novelty claims (C1-C3) cannot be verified against the external literature. The assessment above is based on manuscript-grounding only. See Section 9 for the deferred-verification board.

## Key Issues
**Issue 1: Underpowered real-world evaluation (Critical/Major)**
- **Severity**: Major | **Validity Risk**: High | **Fixability**: High
- **Evidence**: Table 1 (Page 9) reports 30 real-world rollouts total. At 60% success rate, the 95% CI spans ~41-77% (Wilson interval). LSDR at 46.7% has CI ~29-65%.
- **Root cause**: Real-world evaluation is expensive, but 30 trials with a binary metric cannot statistically differentiate methods.
- **Impact**: The paper's most impactful claim (successful sim-to-real transfer) rests on statistically weak evidence.
- **Recommended fix**: (Must) Add confidence intervals to Table 1. Increase real-world trials to ≥100 across configurations. Report per-configuration results.
- **Acceptance criteria**: Once CIs are reported and do not overlap with baselines (or if overlap is acknowledged), the claim becomes defensible.

**Issue 2: Uncharacterized IS estimator variance (Major)**
- **Severity**: Major | **Validity Risk**: High | **Fixability**: High
- **Evidence**: Eq. (5) with discussion on Page 5. The paper trusts "recycling training data works sufficiently well" without diagnostic evidence.
- **Root cause**: IS weights ν_{φ_{i+1}}(ξ_k)/ν_{φ_i}(ξ_k) can have high variance when φ_{i+1} diverges from φ_i, especially in high-D.
- **Impact**: If IS estimates are unreliable, the constraint G ≥ α may be silently violated, causing premature distribution widening.
- **Recommended fix**: (Must) Report effective sample size (ESS) or IS weight coefficient of variation over training. (Nice-to-have) Add a clipping or reweighting scheme to control IS variance.

**Issue 3: Success-indicator tuning burden (Medium)**
- **Severity**: Minor | **Validity Risk**: Medium | **Fixability**: High
- **Evidence**: Page 2, Introduction P4. The paper claims "the complexity of the problem shifts from tuning distributions to simply defining a binary rule."
- **Root cause**: Defining σ(τ) requires choosing return thresholds or distance thresholds, which may require comparable domain expertise.
- **Impact**: Practical adoption barrier; a practitioner must still tune the success definition.
- **Recommended fix**: (Nice-to-have) Add a sensitivity study over different success definitions for at least one environment. Provide concrete guidance for choosing J_{LB} thresholds.

**Issue 4: Catastrophic forgetting during backtracking (Medium)**
- **Severity**: Medium | **Validity Risk**: Medium | **Fixability**: Medium
- **Evidence**: Section 6 Limitations (Page 9) and Appendix Fig. 13 show performance degradation.
- **Root cause**: When the backup optimization (Eq. 6) shifts the distribution toward easier dynamics, the policy loses competence on previously solvable harder dynamics.
- **Impact**: The best-performing policy during training must be tracked, limiting the method's practicality.
- **Recommended fix**: (Must) Implement the suggested KL constraint on policy parameters to prevent forgetting. (Nice-to-have) Experiment with replay buffers that retain trajectories from diverse dynamics.

**Issue 5: Performance degradation near maximum entropy (Medium)**
- **Severity**: Medium | **Validity Risk**: Medium | **Fixability**: Medium
- **Evidence**: Appendix Fig. 17 (PandaPush) shows degradation at timesteps ~3.5M; Appendix Fig. 9 shows entropy actually decreasing after growing.
- **Root cause**: The Beta distribution's entropy gradient near (a,b)→(1,1) is small, making fine-grained control difficult near the maximum entropy uniform.
- **Impact**: The method may not stably converge to ν_max; best intermediate distributions must be saved.
- **Recommended fix**: (Nice-to-have) Investigate alternative distribution parameterizations with better-behaved entropy gradients near uniformity.

## Actionable Suggestions
### Suggestion 1 (Must): Add confidence intervals to Table 1 and increase Sim2Real sample size
- **Target**: Page 9, Table 1
- **Problem**: 30 real-world rollouts cannot statistically distinguish methods.
- **Action**: 
  1. Add 95% Wilson confidence intervals to the Sim2Real success rates.
  2. Increase real-world trials to at least 100 (10 per seed × 10 seeds, or more configurations).
  3. Report per-configuration results (Fig. 14 has 3 configurations; report success rate for each).
  4. If larger sample collection is infeasible, explicitly state the limited statistical power and frame results as a feasibility demonstration rather than a definitive comparison.

### Suggestion 2 (Must): Diagnose IS estimator reliability
- **Target**: Page 5, around Eq. (5)
- **Problem**: IS variance is uncharacterized; may silently fail in high dimensions.
- **Action**:
  1. Compute and report effective sample size (ESS = (Σ w_k)² / Σ w_k²) over training timesteps.
  2. Add a plot showing ESS/K ratio for at least Hopper, Walker2D, and PandaPush.
  3. If ESS drops below K/2 at any point, implement IS weight clipping or a lower-bound on the IS ratio.

### Suggestion 3 (Must): Bound promotional language
- **Target**: Page 1 (Abstract), Page 9 (Conclusion), throughout
- **Problem**: "Remarkable", "significant step", "highly adaptive" overstate the evidence.
- **Action**: Replace promotional adjectives with quantitative bounds. A full revision is provided in the annotation on Page 1 Abstract.

### Suggestion 4 (Must): Fix Eq. (4) formatting
- **Target**: Page 4, Eq. (4)
- **Problem**: Missing punctuation between two constraints causes potential misreading.
- **Action**: Insert a comma or semicolon: `G(θ_i, φ_{i+1}) ≥ α, D_KL(ν_{φ_{i+1}} ∥ ν_{φ_i}) ≤ ϵ`

### Suggestion 5 (Nice-to-have): Add quantitative cell counts for HalfCheetah
- **Target**: Page 8, "Effect of entropy maximization" paragraph
- **Problem**: Fig. 3 is presented as visual evidence without quantification.
- **Action**: Add one sentence with success-cell counts, e.g., "DORAEMON achieves success in 24/35 parameter cells, compared to 18/35 for LSDR."

### Suggestion 6 (Nice-to-have): Clarify success indicator sensitivity
- **Target**: Page 8-9, Success rate vs. Entropy trade-off
- **Problem**: The paper uses α=0.5 for all experiments but does not provide a practical guideline for choosing α for a new task.
- **Action**: Add a recommendation paragraph: "For new tasks, we recommend starting with α=0.5 and adjusting based on the observed entropy-success rate trade-off. Lower α yields wider distributions but risks training instability."

### Suggestion 7 (Nice-to-have): Add PandaPush reward rescaling clarification
- **Target**: Page 21 (Appendix C), Reward function paragraph
- **Problem**: The reward rescaling ("such that it starts at a value of zero") is ambiguous.
- **Action**: Clarify that the constant shift is subtracted from all rewards in the episode, making the total return invariant to initial distance.

### Suggestion 8 (Please consider): Add a practical hyperparameter guideline
- **Target**: Appendix A.2 or a new paragraph in the main text
- **Problem**: The trust-region size ϵ and update frequency K are crucial hyperparameters without practical guidance.
- **Action**: Add a brief paragraph: "We recommend ϵ ∈ [0.005, 0.05] and K roughly matching the number of episodes per SAC iteration. Larger ϵ enables faster convergence but may require the backup optimization (Eq. 6) more frequently."

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this structure:
- P1: RL sample inefficiency + safety → simulation training → reality gap → three categories of sim-to-real methods
- P2: DR trade-off (optimality vs robustness) + non-stationarity + manual tuning problem
- P3: Prior automatic DR methods (Yu et al., Mozian et al., Akkaya et al.) and their limitations
- P4: DORAEMON proposal + key results preview

**Alignment checks**:
- Problem alignment: ✓ The stated challenge (manual tuning of DR distributions) matches the proposed solution (automatic entropy maximization).
- Variable alignment: ✓ Core concepts (entropy, success rate, dynamics distribution, history-conditioned policy) appear consistently throughout.
- Contribution-evidence alignment: ✓ The introduction's claims are supported by experiments, though the wording ("remarkable", "consistently more sample efficient") is stronger than the evidence warrants.

### Recommended Storyline Improvement

The current narrative is functional but can be sharpened. The main issue is that P2 and P3 overlap in discussing DR challenges and prior solutions. A tighter structure would be:

**Candidate Storyline A (Recommended): "Gap-First"**
- P1: Sim-to-real problem → DR as a promising solution → key challenge: distribution tuning.
- P2: Prior automated DR methods (LSDR, AutoDR, Active DR) and their specific limitations (reference distribution required, uniform-only, boundary bias, poor scalability).
- P3: Our idea — maximize entropy of sampling distribution subject to success-rate constraint → DORAEMON.
- P4: Key results (succinct, with numbers).

This structure puts the gap front and center, then shows how DORAEMON fills it.

### Abstract Outline (Revised)

S1 (Problem): "Domain Randomization is effective for sim-to-real transfer but requires manual tuning of the dynamics-parameter sampling distribution."
S2 (Challenge): "Excessive randomization produces overly conservative policies; narrow distributions limit generalization."
S3 (Gap): "Existing automatic DR methods require reference distributions, extra Monte-Carlo evaluations, or confine themselves to uniform distributions."
S4 (Method): "We propose DORAEMON, which maximizes the entropy of the training distribution subject to a success-rate constraint, automatically widening the distribution as the policy improves."
S5 (Result): "On six simulated benchmarks, DORAEMON achieves higher global success rates than No-DR, Fixed-DR, LSDR, and AutoDR. On a 7-DoF real robotic pushing task with unknown dynamics, DORAEMON-trained policies achieve 60% zero-shot success rate (baseline: 46.7%)."

### Introduction Outline (Revised, Paragraph-by-Paragraph)

**P1: Motivation and Challenge** (Big Picture)
- Role: Establish the sim-to-real problem and why DR is important but has a key limitation.
- Key claim: DR requires manual tuning of the sampling distribution.
- Evidence: References [Vuong et al. 2019], [Muratore et al. 2022b].
- Transition: "Several methods have been proposed to automate this tuning..."

**P2: Prior Automated DR Methods** (Gap)
- Role: Survey LSDR, AutoDR, Active DR, and their specific limitations.
- Key claim: These methods either (a) require a reference distribution, (b) require extra rollouts, (c) are confined to uniform distributions, or (d) scale poorly with dimensionality.
- Evidence: [Mozian et al. 2020], [Akkaya et al. 2019], [Mehta et al. 2020].
- Transition: "In this paper, we address these limitations with a different approach..."

**P3: DORAEMON Proposal** (Idea)
- Role: Present the core intuition and mathematical formulation.
- Key claim: Entropy maximization with success-rate constraint yields automatic distribution widening.
- Evidence: Eq. (3), toy example preview.
- Transition: "We evaluate DORAEMON on..."

**P4: Results Preview** (Evidence)
- Role: Summarize key empirical findings without hype.
- Key claim: DORAEMON outperforms baselines on 6 sim benchmarks and a real robot.
- Evidence: Numeric preview of key results (sim success rates, real success rate with qualifier).
- Transition to Section 2 (Related Work).

### Mentor Revised Version (Full Introduction)

**P1**: "Reinforcement Learning (RL) holds promise for robotic control but suffers from low sample efficiency and safety concerns during real-world data collection. Training in simulation addresses these issues but introduces the reality gap — the discrepancy between simulated and real dynamics. Domain Randomization (DR) mitigates this gap by varying simulator parameters during training, yet the performance of DR policies depends critically on manually tuning the sampling distribution's range and shape [Vuong et al., 2019]."

**P2**: "Recent work has attempted to automate DR distribution selection. Mozian et al. (2020) optimize a training distribution to match a reference distribution via M-projection, requiring expensive Monte-Carlo evaluations. Akkaya et al. (2019) gradually widen a uniform distribution based on boundary performance, but are confined to uniform families and update one dimension at a time. Mehta et al. (2020) learn a sampling policy, but rely on a predefined reference distribution. A common limitation is the need for a reference distribution or extra interaction budget."

**P3**: "We propose DORAEMON, which directly maximizes the entropy of the training distribution subject to a success-rate constraint. The key intuition is that wider distributions improve generalization, but the distribution should only widen as long as the policy maintains acceptable performance. This constrained optimization eliminates the need for a reference distribution and naturally handles high-dimensional parameter spaces. The success-rate constraint is evaluated via importance sampling from collected trajectories, avoiding additional interaction."

**P4**: "We evaluate DORAEMON on six continuous-control benchmarks with 2-13 randomized parameters. DORAEMON consistently achieves higher global success rates than four baselines. On a 7-DoF real robotic pushing task with 17 unknown dynamics parameters, DORAEMON achieves 60% zero-shot success rate, compared to 46.7% for the best baseline (LSDR). We also provide ablations showing the contribution of each component."

## Priority Revision Plan
This plan lists revisions in order of importance (P0 = critical for publication, P1 = important, P2 = quality improvement).

### P0 — Must fix before publication

| Priority | Action | Target | Effort | Impact |
|----------|--------|--------|--------|--------|
| P0 | Add confidence intervals to Table 1 Sim2Real results | Page 9, Table 1 | Low | Validates core claim |
| P0 | Add IS estimator diagnostics (ESS plot) | Page 5 / Appendix | Medium | Ensures constraint reliability |
| P0 | Tone down promotional language in Abstract/Conclusion | Pages 1, 9 | Low | Scientific objectivity |
| P0 | Fix Eq. (4) punctuation | Page 4 | Low | Readability |

### P1 — Important improvements

| Priority | Action | Target | Effort | Impact |
|----------|--------|--------|--------|--------|
| P1 | Increase Sim2Real sample size to ≥100 trials | Page 9 | High | Statistical power |
| P1 | Add success-cell counts for HalfCheetah heatmap | Page 8 | Low | Quantitative evidence |
| P1 | Address catastrophic forgetting (KL policy constraint) | Page 9 / Appendix B | Medium | Method robustness |

### P2 — Quality enhancements

| Priority | Action | Target | Effort | Impact |
|----------|--------|--------|--------|--------|
| P2 | Add hyperparameter guideline for ϵ and K | Appendix A.2 | Low | Practical adoption |
| P2 | Clarify reward rescaling in PandaPush | Appendix C | Low | Reproducibility |
| P2 | Acknowledge success-indicator tuning burden explicitly | Page 2, Introduction P4 | Low | Intellectual honesty |

### Expected Impact After Full Revision

If all P0 and P1 items are addressed:
- The real-world claim becomes statistically defensible (or honestly qualified).
- The IS estimator's reliability is verifiable by readers.
- The narrative becomes more objective and evidence-grounded.
- The method's practical limitations (forgetting, tuning burden) are transparent.

The paper's core contribution (entropy-maximization DR) is solid and would remain publishable after these revisions.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Evaluate DORAEMON against baselines on sim benchmarks | 6 MuJoCo tasks (2D-13D), 4 baselines, 10 seeds | Global success rate on ν_max, entropy over time | DORAEMON achieves higher/faster convergence on all 6 tasks | C3 (empirical superiority) | Performance degrades near ν_max in some tasks |
| E2 | Visualize 2D dynamics coverage | HalfCheetah, 2D parameter slice, avg return heatmap | Per-cell success (green outline) | DORAEMON covers widest success region | C3 | No quantitative cell counts |
| E3 | α sensitivity analysis | Hopper, Walker2D, HalfCheetah, α={0.5,0.75,0.9} | In-distribution SR, entropy, global SR | α=0.5 best trade-off; α tracking works well | C1 (constraint effectiveness) | Only 3 environments tested |
| E4 | J_LB sensitivity analysis | Hopper, J_LB={1400,1600,1800} | Median return, entropy | Algorithm tracks α regardless of threshold | C1 (success indicator flexibility) | Only Hopper; needs more tasks |
| E5 | ϵ sensitivity analysis | Hopper, Walker2D, HalfCheetah, ϵ={0.005,0.01,0.05} | In-distribution SR, entropy, global SR | DORAEMON maintains α even for large ϵ | C2 (backup optimization) | No theoretical guidance for ϵ choice |
| E6 | Beta vs Gaussian parametrization | Hopper, Walker2D, HalfCheetah | Global SR, entropy | Similar performance; Beta better for bounded support | C1 (flexibility) | Only 3 tasks |
| E7 | Ablation from SPDL perspective | Hopper, Walker2D (3 ϵ values) | In-distribution SR, entropy, global SR | All components (history, asymmetric, backup) contribute | C2 | Backup optimization helps tracking but not always global SR |
| E8 | PandaPush sim evaluation | 17D dynamics, 10 seeds, 10000 rollouts | Success rate, distance to target | DORAEMON: 66.57% SR (best baseline: 37.77%) | C3 (high-D scalability) | Performance drops near max entropy |
| E9 | PandaPush real-world evaluation | 3 configs, 30 rollouts total | Success rate, distance to target | DORAEMON: 60% SR (best baseline: 46.67%) | C3 (sim-to-real transfer) | 30 trials insufficient for statistical significance |

### Research-Theme Gap Diagnosis

1. **New Knowledge (partially supported)**: The core idea — entropy maximization with success-rate constraint for automatic DR — is conceptually novel. However, the optimization framework has significant overlap with self-paced curriculum learning [Klink et al. 2020a,b], which uses similar constrained optimization for task curricula. The paper's contribution is therefore more in the specific application to DR and the algorithmic innovations (IS-based estimation, backup optimization) rather than in a fundamentally new optimization paradigm.

2. **Reproducibility (well supported)**: The paper provides detailed hyperparameter settings (Appendix A.2), search space boundaries (Table 2), and a public code repository. The method uses standard components (SAC, Beta distributions). Reproducibility is strong.

3. **Impact on Practice/Understanding (moderately supported)**: The method's practical value is demonstrated on a real robot, but the limited statistical power weakens the impact claim. The method's requirement for a success indicator (rather than using the raw reward) is both a feature (robust to catastrophic returns) and a barrier (requires extra domain knowledge).

### Proposed Research Experiments

**P0 Experiment: IS Estimator Reliability Diagnostics**
- **Target Claim**: C2 (IS-based estimation is reliable)
- **Hypothesis**: The IS estimator maintains ESS/K > 0.5 throughout training for tasks with up to 13D parameters.
- **Minimal Design**: Compute and plot ESS/K ratio over training timesteps for Hopper (7D), Walker2D (13D), and PandaPush (17D). Report minimum ESS/K across all iterations.
- **Controls**: None needed (diagnostic only).
- **Metrics**: ESS/K ratio, IS weight coefficient of variation.
- **Success Criterion**: ESS/K ≥ 0.5 for ≥95% of training iterations.
- **Estimated Cost**: Low (purely computational, using logged data).
- **Expected Quality Gain**: High — verifies the core assumption of sample-efficient constraint evaluation.

**P0 Experiment: Statistical Power for Sim2Real**
- **Target Claim**: C3 (real-world superiority)
- **Hypothesis**: With adequate sample size, DORAEMON's 60% success rate is statistically distinguishable from LSDR's 46.7%.
- **Minimal Design**: Increase real-world trials to 100 (10 per seed × 10 seeds, or 10 per configuration × 10 configurations). Report per-configuration success rates.
- **Controls**: Same 3 configurations as current study (Fig. 14), plus optionally 2 more CoM settings.
- **Metrics**: Success rate with 95% Wilson CI.
- **Success Criterion**: Non-overlapping CIs between DORAEMON and all baselines, OR clear statement of non-significance.
- **Estimated Cost**: Medium (requires additional robot time; ~70 more trials).
- **Expected Quality Gain**: Critical — validates or honestly bounds the paper's most impactful claim.

**P1 Experiment: Catastrophic Forgetting Mitigation**
- **Target Claim**: C1/C2 (method robustness)
- **Hypothesis**: Adding a KL constraint D_KL(π_{θ_{i+1}} ∥ π_{θ_i}) ≤ δ prevents performance collapse during backtracking.
- **Minimal Design**: Implement KL-constrained policy updates on Hopper and Walker2D. Compare global SR curves with/without constraint.
- **Controls**: Same SAC backbone, same ϵ, same α=0.5.
- **Metrics**: Global SR at convergence, minimum in-distribution SR during training.
- **Success Criterion**: Higher minimum in-distribution SR without reducing peak global SR.
- **Estimated Cost**: Medium (requires new training runs for 2 environments).
- **Expected Quality Gain**: High — addresses the main algorithmic weakness identified by the authors themselves.

**P2 Experiment: Success-Indicator Sensitivity**
- **Target Claim**: C1 (practical usability)
- **Hypothesis**: DORAEMON is robust to the choice of success threshold J_LB within a reasonable range.
- **Minimal Design**: On HalfCheetah and Swimmer, run DORAEMON with 3 different J_LB values (Table 2 value ± 20%). Report final global SR and entropy.
- **Controls**: Same α=0.5, same ϵ.
- **Metrics**: Global SR at convergence, final entropy.
- **Success Criterion**: Global SR varies by ≤5 percentage points across J_LB choices.
- **Estimated Cost**: Low (6 additional training runs).
- **Expected Quality Gain**: Medium — provides practical guidance for new users.

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 6.5/10

**Score breakdown by dimension:**

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| Research Value | 30% | 6/10 | Solid practical contribution (automatic DR) but incremental over self-paced CL framework |
| Novelty | 25% | 5/10 | Constrained entropy-maximization for DR is a novel application, but the optimization framework has close precursors in self-paced CL. Specific algorithmic contributions (IS-based estimation, backup optimization) are genuinely new. Full novelty verification deferred due to retrieval unavailability. |
| Validity/Soundness | 20% | 7/10 | Method is well-formulated and theoretically principled. Main validity concern: IS estimator variance is uncharacterized, and real-world evaluation is underpowered. |
| Reproducibility | 10% | 8/10 | Detailed hyperparameters, public code, clear experimental protocol. Minor ambiguity in reward rescaling. |
| Presentation | 10% | 7/10 | Well-structured and clearly written. Promotional language in abstract/conclusion should be toned down. Eq. (4) has a punctuation issue. |
| Significance | 5% | 6/10 | 60% Sim2Real success rate is promising but statistically underpowered. Sim results are convincing across 6 benchmarks. |

**Final weighting**: Research Value (6) + Novelty (5) dominate the score. The paper makes a genuine contribution to the DR literature but does not introduce a fundamentally new paradigm. The underpowered real-world evaluation prevents a higher score.

### Post-Revision Target: [7.0, 7.5]/10

If all P0 and P1 items are addressed:
- **Confidence intervals added + IS diagnostics** → Validity/Soundness increases from 7→8.
- **Promotional language removed** → Presentation increases from 7→8.
- **Statistical power increased** → Significance increases from 6→7.
- **Catastrophic forgetting mitigation** → Research Value increases from 6→7.

**Upper bound**: 7.5 — the paper's conceptual overlap with self-paced CL limits novelty to 6/10 even with perfect execution. A score above 7.5 would require demonstrating the method on additional real-world tasks or showing a clear advantage over self-paced baselines in a DR setting.