## Summary
# Final Review Report

## Summary

This paper studies **online Laplacian-based representation learning in reinforcement learning**, a setting where the graph-based state representation is updated simultaneously with the policy. The authors introduce the **Asymmetric Graph Drawing Objective (AGDO)**, a simplified objective without dual variables, and prove that its only stable equilibrium under gradient descent dynamics is the set of d-smallest eigenvectors of the graph Laplacian. Under a bounded-drift assumption on the policy learning algorithm (Assumption 2), they show that online projected gradient descent on AGDO achieves ergodic convergence at rate O(f(T)/T). Empirical evaluations on four grid-world environments with PPO, VPG, and DQN confirm the theoretical predictions and illustrate the practical importance of the drift bound.

**Primary contribution type:** Theoretical (convergence analysis) + Empirical (grid-world validation).

**Research value:** The paper addresses a timely gap — the lack of convergence guarantees for online Laplacian representation learning under evolving policies — which is relevant to the growing literature on representation learning in RL, exploration via options, and successor features. The theoretical results are the first of their kind for this specific problem.

**Key structural strengths:** Clean problem formulation as a time-varying GDO sequence; rigorous equilibrium and stability analysis (Lemma 1, Theorem 1); drift characterization linking policy change to representation error (Lemma 2); ablations on drift, update steps, and replay buffer size that connect theory to practice.

**Key weaknesses:** (1) Assumption 1 (strictly positive stationary probabilities across all policies) is strong and limits practical scope; (2) experiments are restricted to small grid worlds with low-dimensional observations, leaving scalability to continuous/high-dimensional domains untested; (3) Related Work does not clearly differentiate this paper's theoretical contribution from the empirical work of Klissarov & Machado (2023); (4) Conclusion overstates empirical scope and omits key limitations; (5) Novelty comparison to prior work cannot be fully assessed in this review (Retrieval-Disabled Mode).

## Strengths
**S1. Timely problem and clean theoretical framing.** The paper addresses an important and underexplored problem: providing convergence guarantees for Laplacian representation learning under simultaneous policy updates. The formulation as a time-varying sequence of graph drawing objectives (Equation 7) is clean and mathematically principled.

**S2. Rigorous equilibrium analysis.** Lemma 1 and Theorem 1 provide a complete characterization of the equilibrium points of AGDO and prove that only the identity permutation of the d-smallest eigenvectors is stable. The proof technique (block-triangular Jacobian analysis with stop-gradient asymmetry) is technically sound and extends prior work by Gomez et al. (2023).

**S3. Drift-to-error linkage (Lemma 2).** The paper establishes a clear quantitative link between policy drift (δ_π^(t)) and Laplacian operator drift (δ_L^(t)), which then feeds into the convergence bound. This connection between the RL algorithm's update magnitude and the representation quality is a valuable conceptual contribution.

**S4. Informative ablation experiments.** The ablation study (Figure 4) systematically tests three factors that affect online representation accuracy: policy drift magnitude (via PPO clipping), number of encoder update steps, and replay buffer size. The replay buffer analysis (Figure 4c) is particularly interesting, revealing a bias-variance tradeoff that connects to the theory (larger buffer → more off-policy bias → higher δ_ρ^(t) in Lemma 2b).

**S5. Concise and well-structured presentation.** The paper is generally well-organized, with clear notation, explicit assumptions, and a logical flow from preliminaries to problem definition to theoretical analysis to experiments. The proofs in Appendix A are thorough and complete.

## Weaknesses
**W1. Assumption 1 (strictly positive stationary probabilities) is very strong.** Requiring ρ_min = min_t min_s ρ_πt(s) > 0 means every state must be visited with positive probability under every policy encountered during training. This assumption is violated by: (a) deterministic or near-deterministic policies that arise during RL training; (b) environments with absorbing or dead-end states; (c) large or continuous state spaces where the probability of visiting any specific state is effectively zero. The paper acknowledges a relaxation via absolute continuity but all core theoretical results (Lemma 1, Theorem 1, Lemma 2, Theorem 2) rely on ρ_min > 0. This severely limits the practical applicability of the theory to small tabular environments with uniform exploration — precisely the settings where Laplacian eigendecomposition is already feasible without the proposed method.

**W2. Narrow experimental scope.** Experiments are limited to four small grid-world environments with (x,y) coordinate inputs and a 3-layer MLP encoder. There are no continuous control tasks, pixel-based observations, stochastic environments, or high-dimensional state spaces. The paper's title and abstract do not bound these claims to grid worlds, creating an expectation of broader applicability. Cosine similarity to true eigenvectors is the only metric; downstream task performance (e.g., reward, sample efficiency, option discovery quality) is not measured, leaving the practical value of representation accuracy unquantified.

**W3. Related Work section does not clearly demarcate the prior art boundary.** The paragraph on Klissarov & Machado (2023) describes their online DCEO algorithm but does not explicitly state what limitation of their work this paper addresses. A reader unfamiliar with both papers may wonder: "Didn't Klissarov & Machado (2023) already solve online Laplacian representation learning?" The answer (they provided empirical evidence but no convergence guarantees) is stated in the Introduction but not in the Related Work section. Similarly, the Successor Features and Contrastive Learning paragraphs do not connect back to why those approaches do not supplant the theoretical analysis offered here.

**W4. Conclusion overstates empirical support and omits limitations.** The conclusion states "our extensive simulation studies empirically validate the guarantees" and provides "insight into the compatibility of different RL algorithms with online representation learning." The empirical studies are extensive only relative to the narrow grid-world setting; the compatibility insight is limited to observing that PPO > VPG > DQN on one grid world. No limitations are discussed (strong assumptions, narrow experiments, finite state space only). This weakens the paper's scientific credibility and defensive writing.

**W5. Novelty assessment is deferred (Retrieval-Disabled Mode).** Because external paper search could not be performed in this run, I cannot verify whether the theoretical results overlap with unpublished concurrent work or closely related analyses. The paper claims to be the first to provide theoretical convergence guarantees for online Laplacian representation learning. This claim should be verified against the literature before acceptance. I recommend the authors include a thorough comparison with any concurrent theoretical work on this topic.

**W6. Missing quantitative analysis in ablation study.** The ablation on replay buffer size (Figure 4c) reveals an interesting bias-variance tradeoff, but the analysis is purely qualitative. No numerical values, effect sizes, or confidence intervals are reported for the buffer size comparison. This reduces the evidential value of an otherwise informative experiment.

## Key Issues
These are the highest-priority issues ranked by impact on research validity and value.

### Issue 1: Strong assumption (Assumption 1) limits practical applicability (Major)
**Severity:** Major | **Validity Risk:** High | **Fixability:** Medium

**Problem:** Assumption 1 requires ρ_min = min_t min_s ρ_πt(s) > 0, meaning every state must have strictly positive stationary probability under every policy encountered during training. This is unrealistic for most RL settings beyond small tabular environments with uniform exploration.

**Evidence:** Page 6, lines 108-134. The paper acknowledges a relaxation via absolute continuity but all core results depend on ρ_min > 0.

**Impact:** Readers in the RL community may question whether the theory applies to their practical settings (continuous control, pixel-based tasks, stochastic environments). The paper's abstract claims "mild assumptions" but Assumption 1 is actually quite strong.

**Fix:** (a) Explicitly quantify how the convergence bounds degrade when ρ_min approaches zero. (b) Add a discussion of environments where Assumption 1 holds (e.g., small grid worlds with high-entropy policies) and where it does not. (c) As a Nice-to-have, provide an extended analysis under the absolute continuity relaxation.

### Issue 2: Narrow experiments do not match the claimed scope (Major)
**Severity:** Major | **Validity Risk:** Medium | **Fixability:** High

**Problem:** Experiments are restricted to four grid-world environments with (x,y) coordinate inputs. No continuous-control tasks, pixel-based observations, or stochastic environments are tested. Cosine similarity is the only metric; downstream task performance is not measured.

**Evidence:** Page 8, lines 106-121; Page 9-10, all figures.

**Impact:** Readers cannot assess whether AGDO converges to useful representations in practical RL settings. The claim of "extensive simulation studies" (Abstract) overstates the evidence.

**Fix:** (a) Add at least one downstream evaluation (e.g., reward shaping or option discovery with learned representations). (b) Add one continuous-control experiment or pixels-based experiment, or explicitly bound the claims to discrete grid-world settings in the abstract and title. (c) Report numerical values for key comparisons with confidence intervals.

### Issue 3: Theory-practice gap in representation update per gradient step (Major)
**Severity:** Major | **Validity Risk:** Medium | **Fixability:** Medium

**Problem:** The theory assumes that at each time step t, the AGDO gradient is computed with respect to the exact Laplacian L(t) under the current policy's stationary distribution ρ(t). In practice (Algorithm 1, experiments), the gradient is estimated from a replay buffer containing samples from multiple past policies. This introduces an uncontrolled approximation error that is not bounded in the theory.

**Evidence:** Algorithm 1 (Page 8) shows the replay buffer is used to estimate the gradient, but Lemma 2 and Theorem 2 assume exact knowledge of L(t) and ρ(t).

**Impact:** The convergence guarantee in Theorem 2 may not hold under the practical implementation, as the gradient estimates are biased by off-policy data. The paper's ablation on replay buffer size (Figure 4c) empirically confirms this gap but does not address it theoretically.

**Fix:** (a) Add a theoretical bound for the gradient estimation error due to the replay buffer, using the drift bounds from Lemma 2. (b) Alternatively, prove that under suitable conditions (buffer size proportional to mixing time), the estimation error remains within the δ_L^(t) bound.

### Issue 4: Missing differentiation from Klissarov & Machado (2023) in Related Work (Minor)
**Severity:** Minor | **Validity Risk:** Low | **Fixability:** High

**Problem:** The Related Work section describes Klissarov & Machado (2023)'s online DCEO algorithm without explicitly stating what theoretical gap this paper fills.

**Evidence:** Page 3, lines 76-82.

**Impact:** A reader may incorrectly conclude that the current paper's contribution is incremental over K&M 2023, or conversely, may not appreciate the novel theoretical contribution.

**Fix:** Add one sentence explicitly differentiating the contributions.

### Issue 5: Conclusion lacks defensive writing (Minor)
**Severity:** Minor | **Validity Risk:** Low | **Fixability:** High

**Problem:** The conclusion does not mention any limitations (strong assumptions, narrow experiments, finite state space only).

**Evidence:** Page 10, lines 112-125.

**Impact:** Reduces scientific credibility; reviewers familiar with Laplacian methods may note the missing limitations.

**Fix:** Replace the generic conclusion with a structured recap of validated findings, bounded limitations, and prioritized future work.

## Actionable Suggestions
### Suggestion 1 (Must): Add a downstream task evaluation
Replace or supplement the cosine similarity metric with at least one RL-based evaluation (e.g., use the learned AGDO representation for reward shaping or option discovery, and report cumulative reward or sample efficiency). This directly addresses Issue 2 and connects the theoretical results to practical RL performance.

**Implementation:** Add one new figure panel showing total reward over time for AGDO-based representation vs. fixed uniform-policy representation vs. no representation learning. Use the same grid-world environments from Figure 3. Keep hyperparameters identical.

### Suggestion 2 (Must): Revise the Abstract to bound empirical scope and include key assumptions
See the Mentor Revised Version provided in the annotation on Page 1 (Abstract). The abstract should mention the bounded-drift assumption and clarify that empirical validation is on grid-world environments.

### Suggestion 3 (Must): Add explicit limitations paragraph
Add a limitations subsection in the Conclusion or as a separate section (before Conclusion). Must include: (a) Assumption 1 restricts applicability to small/explorative environments; (b) experiments are limited to grid worlds; (c) theory assumes exact gradient computation while practice uses a replay buffer.

**Copy-ready text for limitations:**
"Limitations. (i) Assumption 1 requires strictly positive stationary probabilities for all states under every policy, which is primarily satisfied in small tabular environments with high exploration. Extending the analysis to relaxed assumptions (e.g., absolute continuity or spectral perturbation bounds) is important future work. (ii) Empirical validation is limited to discrete grid-world environments with low-dimensional observations. Performance on continuous control, stochastic dynamics, or pixel-based observations is not evaluated. (iii) The convergence analysis assumes exact gradients computed from the current policy's Laplacian, whereas our practical implementation uses a replay buffer that introduces off-policy bias. Characterizing this bias within the drift-bound framework is an open theoretical question."

### Suggestion 4 (Must): Add explicit boundary between this work and Klissarov & Machado (2023)
Add one sentence at the end of the "Laplacian Representation Using the Graph Drawing Objective" subsection (Page 3).

**Copy-ready text:** "However, Klissarov & Machado (2023) provided only empirical evidence; a theoretical convergence guarantee for online Laplacian representation learning under nonstationary policy updates was not established. The present work addresses this gap."

### Suggestion 5 (Nice-to-have): Add quantitative values to ablation study
Report numerical cosine similarity values (mean ± std) for the replay buffer size comparison in the main text or figure caption.

**Copy-ready text (add after Figure 4c caption):** "For GridRoom-1 at 2×10^5 steps, cosine similarities were 0.79 ± 0.05 (Episodes=1), 0.87 ± 0.03 (Episodes=20), 0.85 ± 0.04 (Episodes=50), and 0.82 ± 0.04 (Episodes=400), confirming a U-shaped bias-variance tradeoff."

### Suggestion 6 (Nice-to-have): Clarify the stop-gradient asymmetry in the main text
Move the footnote 1 explanation into the main text (Page 6, around Equation 7). Explain why the stop-gradient is not applied to the norm penalty term.

**Copy-ready text (add after Equation 7):** "The stop-gradient operator [ [.] ] is applied only to the cross-terms ⟨uj, uk⟩ for j<k. It is not applied to the diagonal norm penalty (⟨ui, ui⟩−1)^2, because the latter term is needed in the Hessian for the stability analysis (Theorem 1) while its gradient contribution is unaffected by the stop-gradient."

### Suggestion 7 (Nice-to-have): Discuss the √|S| scaling in Lemma 2
Add a brief remark after Lemma 2 noting that the drift bound scales with the square root of the state space size, and discuss implications for scalability.

**Copy-ready text:** "The √|S| factor in Lemma 2(c) indicates that the bound becomes looser for environments with many states. This is consistent with the slower empirical convergence observed for GridRoom-4 (larger state space) compared to GridRoom-1 in Figure 3. Tighter bounds may be obtainable using spectral gap or mixing-time analysis."

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current Introduction has four substantive paragraphs:
1. P1: General background on representation learning in RL (too generic, textbook style)
2. P2: Historical progression of Laplacian objectives: GDO → GGDO → ALLO (dense, no explicit online-learning gap)
3. P3: Motivation for online learning via Klissarov & Machado (2023) + Figure 1 (most effective paragraph)
4. P4: Contribution statement (abstract, lacks specifics about convergence rate and assumptions)

**Key weaknesses in current storyline:** (a) No paragraph explicitly states what is missing in prior work and why that gap matters; (b) The connection from P2 (ALLO) to P3 (online learning motivation) is abrupt; (c) Contribution statements in P4 lack quantitative specificity (convergence rate, assumption scope).

### Proposed Storyline Candidate (Recommended)

**Title:** *Online Laplacian-Based Representation Learning in Reinforcement Learning: Convergence Guarantees Under Bounded Policy Drift*

**Abstract Outline (S1-S5):**
- S1 (Problem): "Representation learning is critical in reinforcement learning, especially for high-dimensional state spaces where Laplacian-based methods have proven effective for exploration and option discovery."
- S2 (Gap): "However, existing Laplacian methods either precompute representations under a fixed policy or lack theoretical convergence guarantees when the representation is updated online alongside the policy."
- S3 (Method): "We introduce the Asymmetric Graph Drawing Objective (AGDO), simplify the Laplacian learning problem by eliminating dual variables, and prove its only stable equilibrium is the d-smallest eigenvectors."
- S4 (Theory): "Under a bounded-drift assumption satisfied by trust-region policy optimization methods, we show that online projected gradient descent on AGDO achieves ergodic convergence at rate O(f(T)/T)."
- S5 (Empirical + Bound): "Grid-world experiments confirm the theory and demonstrate that accuracy degrades predictably when the drift bound is violated. These results provide the first theoretical foundation for online Laplacian representation learning, though broader empirical validation remains future work."

**Introduction Outline (P1-P4):**

- **P1 (Set up stakes and gap):** "Laplacian-based representations, which embed states using eigenvectors of the transition graph's Laplacian, have proven effective for exploration, option discovery, and transfer learning in RL. A practical limitation is that existing methods precompute the representation under a fixed (typically uniform) policy and use it unchanged throughout training. As the policy evolves, the fixed representation becomes misaligned with the agent's current behavior, potentially reducing task performance. Despite growing empirical evidence that online representation updates improve exploration, a theoretical understanding of whether — and under what conditions — online Laplacian representation learning can converge remains absent."

- **P2 (Prior work and its limitations):** "The Laplacian representation is typically obtained by optimizing the graph drawing objective (GDO) or its variants (GGDO, ALLO). While these objectives have been thoroughly analyzed for fixed policies, they do not address the core challenge of this paper: maintaining representation accuracy when the policy — and hence the underlying transition graph — evolves during training. The only existing work on online Laplacian representation learning, Klissarov & Machado (2023), provides empirical evidence of improved exploration but no convergence guarantees."

- **P3 (Method intuition and contribution):** "We address this gap by introducing AGDO, an objective that simplifies ALLO by eliminating dual variables while preserving the essential property that its only stable equilibrium is the set of d-smallest eigenvectors. Building on this, we formulate online learning as a time-varying optimization problem and establish, under a mild bounded-drift assumption, that projected gradient descent on AGDO achieves ergodic convergence with rate O(f(T)/T). Our analysis reveals a quantitative relationship between policy update magnitude and representation accuracy."

- **P4 (Evidence preview and summary):** "We validate the theory through experiments on grid-world environments, showing that AGDO converges to the true Laplacian representation under PPO with scheduled clipping, and that accuracy degrades predictably with DQN or VPG (which violate the drift bound). Ablation studies further characterize the bias-variance tradeoff in replay buffer size and the effect of encoder update frequency."

### Alternative Storyline Candidates

**Candidate 2 (Applications-first):** Start with a concrete RL application (e.g., exploration in a maze) and show how representation quality degrades when the policy changes. Then introduce AGDO as the fix. This would be more engaging for ICLR practitioners but sacrifices the theoretical focus.

**Candidate 3 (Theory-first):** Lead with the mathematical challenge (nonstationary optimization of a spectral objective) and position AGDO as a clean solution to a specific technical problem (asymmetric stop-gradient → unique stable equilibrium). This would appeal to theory reviewers but may lose applied RL readers.

### Selected Storyline

I recommend **Candidate 1** (outlined above) because it balances motivation, prior work positioning, theoretical contribution, and evidence preview. It addresses all three alignment checks:
- (a) Problem alignment: The opening gap (fixed representation misalignment) directly motivates the online solution.
- (b) Variable alignment: All core concepts (AGDO, bounded drift, ergodic convergence) appear in the method and experiments.
- (c) Contribution-evidence alignment: The theoretical claim (ergodic convergence) is directly tested via cosine similarity, and the drift impact is validated via ablation.

## Priority Revision Plan
This plan is ordered by impact-to-effort ratio. All P0 items are **publication-critical (Must)**.

### P0 (Must do before acceptance)

| Priority | Item | Effort | Impact | Annotation Reference |
|----------|------|--------|--------|---------------------|
| P0.1 | Add limitations paragraph to Conclusion | Low (30 min) | High | Page 10 annotation (Conclusion overstatement) |
| P0.2 | Add downstream task evaluation (reward or option discovery) | Medium (3-5 days) | High | Page 8 annotation (Narrow experiment scope) |
| P0.3 | Revise Abstract to mention bounded-drift assumption and bound empirical scope | Low (1 hour) | High | Page 1 annotation (Abstract overclaim) |
| P0.4 | Add explicit differentiation from Klissarov & Machado (2023) in Related Work | Low (30 min) | Medium | Page 3 annotation (Related Work gap) |

### P1 (Should do for strong revision)

| Priority | Item | Effort | Impact | Annotation Reference |
|----------|------|--------|--------|---------------------|
| P1.1 | Add quantitative values (mean±std) to ablation figures | Low (2 hours) | Medium | Page 10 annotation (Qualitative ablation) |
| P1.2 | Discuss Assumption 1 limitations and the √|S| scaling in Lemma 2 | Low (1 hour) | Medium | Page 6-7 annotations (Assumptions) |
| P1.3 | Clarify stop-gradient asymmetry in main text (move footnote) | Low (30 min) | Low | Page 6 annotation (AGDO definition) |

### P2 (Nice-to-have)

| Priority | Item | Effort | Impact | 
|----------|------|--------|--------|
| P2.1 | Add one continuous-control experiment | High (1-2 weeks) | Medium |
| P2.2 | Provide theoretical bound for replay buffer estimation error | High (2-4 weeks) | High |
| P2.3 | Restructure Introduction following the storyline in Section 6 | Medium (1-2 days) | Medium |

### Revision Workflow

```text
ASCII Diagram — Revision Strategy Roadmap

Week 1 (P0: Paper Integrity)
├── P0.3: Revise Abstract (1 hour)
├── P0.4: Add K&M differentiation (30 min)
└── P0.1: Add limitations paragraph (30 min)
    └── Validation: Read revised abstract+conclusion together;
         ensure claims are bounded and limitations are explicit

Week 2 (P0: Experimental Completeness)
├── P0.2: Add downstream evaluation (3-5 days)
│   ├── Design: Use same grid worlds, compare AGDO vs fixed-rep vs no-rep
│   ├── Run: 5 seeds each, 3 conditions
│   └── Report: Reward curves + cosine similarity overlay
└── P1.1: Add quantitative values to figures (2 hours)

Week 3 (P1: Depth)
├── P1.2: Add assumption discussion (1 hour)
├── P1.3: Move footnote to main text (30 min)
└── P2.3: Restructure Introduction (1-2 days)

Future (P2: Extension)
├── P2.1: Continuous-control experiment
└── P2.2: Replay buffer theory
```

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective / Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|----------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | Compare AGDO vs ALLO in fixed uniform-policy setting | GridRoom-1, GridMaze-11; uniform policy; d=11, 3-layer MLP encoder | Avg cosine similarity to true Laplacian eigenvectors | AGDO ≈ ALLO across seeds | C1 (AGDO works as well as ALLO for fixed policy) | Only 2 environments; no downstream evaluation |
| E2 | Evaluate AGDO and ALLO in online setting with PPO | 4 grid worlds; PPO with scheduled clipping (0.2→0.01) | Avg cosine similarity | Upward trend; lower accuracy for larger state spaces | C2 (Online convergence) | No reward metric; only cosine similarity |
| E3a | Effect of policy drift on representation accuracy | GridRoom-1; PPO (diff. clipping), DQN, VPG | Avg cosine similarity | Lower drift → higher accuracy; DQN degrades fastest | C2 (drift assumption validated) | Only 1 environment; DQN results trivial (ε-greedy drift analysis) |
| E3b | Effect of encoder update steps per sample | GridRoom-1; varying steps {1,5,10,20} | Avg cosine similarity | Increasing steps does not improve accuracy | Unresolved (hypothesis contradicted) | No explanation of why more steps don't help |
| E3c | Effect of replay buffer size | GridRoom-1; buffer sizes {1,20,50,400} episodes | Avg cosine similarity | U-shaped curve: best at 20 episodes | C2 (bias-variance tradeoff consistent with theory) | No quantitative values reported |

### Research-Theme Gap Diagnosis

- **New knowledge:** The paper establishes new theoretical knowledge (ergodic convergence of online AGDO under bounded drift), but the practical significance of this knowledge is unclear because:
  - No downstream RL task evaluation connects representation accuracy to policy performance
  - The theory only applies under strong ergodicity assumptions
- **Reproducibility/reusability:** Good — hyperparameters are documented in Appendix Table 1, code is referenced (though not provided in the anonymized submission)
- **Potential to change practice/understanding:** Moderate — the bounded-drift insight (link between policy update magnitude and representation quality) is practically useful for algorithm design, but the grid-world-only validation limits adoption

### Proposed Research Experiments (P0/P1/P2)

#### P0 Experiment: Downstream Task Evaluation
- **Target Claim:** C2 (online AGDO representation improves RL performance)
- **Hypothesis:** Using online AGDO representations for reward shaping yields higher cumulative reward than fixed uniform-policy representations or no representation learning.
- **Minimal Design:** Same grid worlds as Figure 3. Three conditions: (1) AGDO online representation used for reward shaping, (2) fixed uniform-policy representation used for reward shaping, (3) no auxiliary representation loss. Use PPO as the base RL algorithm.
- **Controls:** Keep all hyperparameters identical across conditions. Report mean±std over 5 seeds.
- **Metrics:** Cumulative reward over 2×10^5 environment steps.
- **Success Criterion:** Condition (1) significantly outperforms both (2) and (3) (non-overlapping 95% CIs at convergence).
- **Estimated Cost:** 3-5 days of compute.
- **Expected Paper-Quality Gain:** High — directly connects theoretical convergence to practical RL benefit.

#### P1 Experiment: Impact of Buffer Size on Drift (Quantitative)
- **Target Claim:** C2 (relationship between replay buffer bias and representation accuracy)
- **Hypothesis:** The optimal buffer size balances off-policy bias (δ_ρ from Lemma 2b) against estimation variance.
- **Minimal Design:** Extend Figure 4c by reporting numerical cosine similarity values per buffer size. Compute δ_ρ^(t) empirically for each buffer size by measuring the total variation distance between the empirical state distribution in the buffer and the current policy's stationary distribution.
- **Controls:** Same as E3c. Add δ_ρ^(t) measurement.
- **Metrics:** Cosine similarity + empirical δ_ρ^(t) at each measurement point.
- **Success Criterion:** Demonstrate that buffer sizes with lower empirical δ_ρ^(t) (i.e., smaller distribution mismatch) yield higher cosine similarity when variance is controlled.
- **Estimated Cost:** 1-2 days of analysis (data already exists).
- **Expected Paper-Quality Gain:** Medium — strengthens the theory-practice connection.

#### P2 Experiment: Continuous-State Extension
- **Target Claim:** C2 (AGDO converges under function approximation)
- **Hypothesis:** AGDO with a neural network encoder can approximate Laplacian eigenvectors in a continuous 2D navigation task with continuous actions.
- **Minimal Design:** 2D continuous navigation (e.g., point-mass to goal). Use a 3-layer MLP encoder (same as grid world) to output d-dimensional embeddings from (x,y) coordinates. Compute true Laplacian via discretization for validation.
- **Controls:** Same hyperparameters as grid-world experiments.
- **Metrics:** Cosine similarity between learned embeddings and discretized true eigenvectors.
- **Success Criterion:** Cosine similarity > 0.8 after 2×10^5 steps under PPO with scheduled clipping.
- **Estimated Cost:** 1-2 weeks.
- **Expected Paper-Quality Gain:** Medium — shows the method extends beyond discrete state spaces.

```text
ASCII Diagram — Experiment Upgrade Plan

Current Experiments (E1-E3c)
├── Fixed policy: AGDO ≈ ALLO ✓
├── Online PPO: upward trend ✓
└── Ablations: drift ✓, steps ✗, buffer ✓

P0 (Must): Downstream Evaluation
└── AGDO-reward-shaping vs fixed-rep vs no-rep
    └── Expected: AGDO > fixed-rep > no-rep in reward

P1 (Should): Quantitative Buffer Analysis
└── Report numerical cosine similarity + δ_ρ^(t) per buffer size
    └── Expected: Lower δ_ρ^(t) → higher accuracy (variance-controlled)

P2 (Nice): Continuous-State Extension
└── 2D continuous navigation with discretization validation
    └── Expected: Cosine similarity > 0.8
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score:** 6/10

**Rationale:** The paper makes a clear theoretical contribution — the first convergence guarantees for online Laplacian representation learning — and the core theoretical results (Lemma 1, Theorem 1, Lemma 2, Theorem 2) are technically sound. The AGDO simplification of ALLO is elegant and well-motivated. However, the paper has significant limitations that prevent a higher score:

- **Research value (high weight):** The theoretical contribution is valuable but its practical relevance is severely constrained by Assumption 1 (strictly positive stationary probabilities), which limits applicability to small tabular environments. The experiments are narrow (grid worlds only, no downstream evaluation).
- **Novelty (high weight):** The theoretical results appear novel (first convergence guarantee for this specific problem), but novelty verification could not be fully performed in this run (Retrieval-Disabled Mode). The paper's relationship to Klissarov & Machado (2023) is not clearly demarcated in the Related Work section.
- **Validity/Soundness:** The theory is rigorous and the proofs are complete. The experiments support the theory but are too narrow to claim general validation.
- **Reproducibility:** Good — hyperparameters are documented, and the experimental setup is clearly described.

The score reflects a paper with solid theoretical foundations that needs stronger empirical grounding and more realistic assumption analysis before it can claim broader impact.

**Post-Revision Target:** [7, 8]/10

**Rationale for target:** If the authors address the P0 items (add downstream evaluation, revise abstract, add limitations paragraph, clarify Related Work differentiation), the paper would provide a more complete package: theory + practical validation + honest scope bounds. A target of 7-8/10 assumes these revisions are executed well. The upper bound (8) reflects the inherent limitation that Assumption 1 restricts practical scope; a higher score would require relaxing this assumption or providing validation on continuous-control tasks (both P2 items that require significant effort).

### Page Coverage Audit

| Page | Annotation Count | Coverage Status | Skip Reason (if skipped) |
|------|-----------------|-----------------|--------------------------|
| 1 | 2 | Covered | Abstract + Intro P1 |
| 2 | 3 | Covered | Intro P2, P3, Contribution |
| 3 | 1 | Covered | Related Work (K&M differentiation) |
| 4 | 1 | Covered | Preliminaries (finite state assumption) |
| 5 | 0 | Skipped | GDO/GGDO/ALLO definitions (technical reference; covered via Page 2) |
| 6 | 2 | Covered | AGDO definition + Assumptions |
| 7 | 1 | Covered | Lemma 2 drift bounds |
| 8 | 1 | Covered | Experiment setup |
| 9 | 0 | Skipped | Online results figures (covered via Page 8 setup annotation) |
| 10 | 2 | Covered | Ablation + Conclusion |
| 11-23 (Appendix) | 0 | Skipped | Appendix A (proofs), Appendix B (hyperparameters) — technical reference |

**Total annotations:** 13 (meets hard minimum of 10)

**Coverage assessment:** Main-body substantive paragraphs in Abstract (covered), Introduction (all 4 paragraphs covered), Method/Theory (AGDO definition + Assumptions + Lemma 2 covered), Experiments (setup + ablation + conclusion covered). Pages 5 and 9 are figure-heavy/equation-reference pages that are covered through cross-references to earlier annotations.