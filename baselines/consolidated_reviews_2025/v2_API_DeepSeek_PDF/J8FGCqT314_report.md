## Summary
# Final Review Report

## Summary

This paper investigates the performance degradation of Decision Transformers (DT) in stochastic environments. The authors first prove that DT recovers the optimal trajectory almost surely under deterministic transitions and rewards, attributing stochastic degradation to the growing variance of returns-to-go (RTG) over the horizon. They then propose D2T2, which replaces RTG with a steering guidance signal derived from temporal-difference value learning and behavior cloning. The guidance target is the highest-value future state in the same trajectory, predicted from current state context via a causal transformer. D2T2 eliminates the need for manual RTG specification at evaluation time. Experiments on FrozenLake, Tailgate, CARLA, and 18 D4RL tasks show improved performance over DT and competitive results against TD-learning baselines. The paper is well-motivated, the theoretical analysis of DT's deterministic guarantee is instructive, and the experimental scope is broad. However, several gaps in methodological rigor, statistical reporting, and claim substantiation need to be addressed before acceptance.

## Strengths
1. **Well-motivated problem and clear diagnosis.** The paper identifies a concrete, well-recognized limitation of DT — stochastic environment degradation — and traces its cause to the accumulating variance of RTG. The theoretical analysis (Proposition 1) cleanly explains DT's success in deterministic environments, providing a formal anchor for the subsequent method design.

2. **Novel integration of TD learning with transformer-based sequence modeling.** D2T2's core idea — replacing the high-variance RTG with a learned steering signal derived from value-function approximation — is technically sound and addresses two practical issues simultaneously: RTG variance and the requirement of manual RTG specification at inference time. The design of predicting steering targets from past state context via a causal transformer is elegant.

3. **Broad and diverse evaluation.** The experimental suite covers 5 distinct environment types (FrozenLake, Tailgate, two CARLA benchmarks, and three D4RL suites totaling 18 tasks) spanning multiple difficulty levels and stochasticity regimes. This breadth strengthens the generalizability claims.

4. **Useful ablation analysis.** The comparison between D2T2-n (without VAE) and D2T2 (with VAE) in AntMaze and FrankaKitchen (Tables 11-12) provides informative ablation evidence about the role of latent representation in high-dimensional tasks.

## Weaknesses
1. **Oversold SOTA claims without proper statistical evidence.** The paper repeatedly uses "state-of-the-art" and "significantly higher returns" without reporting sufficient statistical detail (exact deltas, confidence intervals, significance tests). The FrozenLake paragraph explicitly says "standard error is small enough...to be ignored," which is methodologically unsound. Several comparisons show D2T2 not being the best (e.g., hopper-Med-Replay, hopper-Medium in Table 3), yet the conclusion claims broad SOTA performance.

2. **Proposition 1 has circular assumptions.** The "well-trained" DT assumption is never formally defined. The proof assumes that if a trajectory achieves R*_0 uniquely, DT must output the optimal action — this is true by construction only if the argmax in Eq. (3) yields probability 1 for one action. The induction step also lacks formal justification for the uniqueness of action identification from the RTG signal. While the proposition is intuitively useful, it does not constitute a rigorous formal proof.

3. **Steering guidance is restricted to same-trajectory states (Eq. 4).** The target state G_t is selected from states in the same trajectory τ_i, which severely limits the method's stitching ability. The paper claims improved stitching (Section 4) but the guidance design inherently blocks cross-trajectory combination. This limitation is not discussed.

4. **VAE error-mitigation mechanism is unclear.** The paper argues that VAE "concentrates the learned knowledge into a compact and expressive latent space" to filter value-function errors, but VAEs are trained to reconstruct inputs, which should propagate errors rather than remove them. The actual denoising mechanism is not explained. The decision of when to use VAE (complex vs. simple tasks) appears ad-hoc.

5. **Missing statistical rigor across experiments.** Several experimental paragraphs lack numerical effect sizes, variance reporting, and significance tests. The omission of DT(m) from Tailgate results (Figure 2a) is a questionable comparison choice that could bias visualization toward the proposed method.

6. **Related Work is a list, not a positioned comparison.** The section catalogs prior methods without explicit comparison axes. The crucial distinction between D2T2 and QDT (both combine DT with Q-learning) is mentioned only briefly and could confuse readers about novelty boundaries.

7. **Introduction lacks narrative clarity.** The first paragraph mixes background, DT description, and limitations without a clear problem→gap→solution arc. The SOTA claim in the final intro paragraph is premature and unsupported.

## Key Issues
### Issue 1 (Major): Statistical evidence insufficient to support claimed superiority
**Severity:** Major | **Fixability:** Fixable  
**Evidence:** Page 7 Tailgate paragraph — "VDT improves DT substantially" without deltas; Page 8 FrozenLake — "standard error is small enough to be ignored" without reporting values; Page 9 Conclusion — "SOTA performance" despite not being best on several D4RL tasks.  
**Impact:** Readers cannot verify claimed improvements. The phrase "SOTA" misrepresents the evidence.  
**Fix:** Report mean±std for all methods across 10 seeds, add paired significance tests, remove unsupported SOTA claims, and include DT(m) in Tailgate figure.

### Issue 2 (Major): Proposition 1 proof has logical gaps
**Severity:** Major | **Fixability:** Partially fixable  
**Evidence:** Page 3 Proposition 1 and Page 13 Appendix proof — "well-trained" is undefined; induction step assumes R*_t uniquely identifies a*_t without justification.  
**Impact:** The theoretical contribution does not meet formal proof standards.  
**Fix:** Define "well-trained" operationally; add explicit uniqueness assumptions for the action-RTG mapping; relegate the informal proof to "theoretical intuition" rather than "Theorem."

### Issue 3 (Major): Steering guidance restricted to same-trajectory states limits stitching
**Severity:** Major | **Fixability:** Partially fixable (fundamental design constraint)  
**Evidence:** Page 5 Eq. (4) — G_t = argmax_{s_j} {γ^{j-t} V(s_j) | j > t, s_j ∈ τ_i}.  
**Impact:** The method cannot consider states from other trajectories for stitching, contradicting the claimed stitching improvement.  
**Fix:** Acknowledge this as a limitation; discuss potential extensions using learned dynamics or cross-trajectory retrieval.

### Issue 4 (Major): VAE error-mitigation mechanism not properly justified
**Severity:** Major | **Fixability:** Fixable  
**Evidence:** Page 6 lines 21-36 — claims VAE "concentrates learned knowledge" without explaining how reconstruction-based training removes value-function errors.  
**Impact:** A core component of D2T2 lacks theoretical grounding.  
**Fix:** Provide a concrete explanation (e.g., stochastic bottleneck suppresses outlier errors from V(·)); add ablation study showing VAE contribution quantitatively.

### Issue 5 (Medium): Introduction narrative structure needs reorganization
**Severity:** Minor | **Fixability:** Fixable  
**Evidence:** Page 1 Introduction — first paragraph tries to cover RL-supervised distinction, RvS, DT mechanism, and limitations all at once.  
**Impact:** Reduces readability and fails to establish a clear research gap.  
**Fix:** Restructure into problem→gap→solution→evidence arc as outlined in the Actionable Suggestions section.

## Actionable Suggestions
### S1. Add rigorous statistical reporting to all experimental results
- Report mean ± standard deviation over at least 5 seeds for every method in every experiment.
- Add a statistical significance test (paired bootstrap or t-test) for all pairwise comparisons where D2T2 is claimed to be "significantly" better.
- Include DT(m) (DT conditioned on max dataset return) in Figure 2(a) for transparency.
- Remove the phrase "standard error is small enough to be ignored" and replace with explicit variance numbers.

### S2. Revise Proposition 1 to clearly state assumptions and scope
- Formally define "well-trained" as: "For every (τ_t, t, R_t) pair in the support of the evaluation distribution, f* attains the maximum of P(Σ r_k = R_t | τ_t, a_t)."
- Add an explicit lemma: "If the optimal trajectory is unique and the environment is deterministic, then for each t, a*_t is the unique action satisfying P(Σ r_k = R*_t | τ_t, a*_t) = 1."
- Reframe the proposition as a "theoretical intuition" or "formal observation" rather than a theorem, since the "well-trained" condition is not directly verifiable.

### S3. Discuss the same-trajectory constraint and its implications
- In Section 3.1 (Step I), acknowledge: "Because G_t is restricted to states in τ_i, this design inherently limits stitching. Extending g to retrieve steering targets from other trajectories via nearest-neighbor search or learned dynamics is an important future direction."
- Remove or soften the stitching claim in Section 4 unless dedicated evidence is added.

### S4. Clarify the VAE error-mitigation mechanism
- Add a technical explanation: "The VAE's stochastic bottleneck encourages the latent code to capture only consistent patterns across steering targets while suppressing instance-level noise from V(·) errors, analogous to a denoising autoencoder."
- Include an explicit ablation table showing performance with and without VAE across all task families (not just AntMaze/Kitchen).

### S5. Strengthen the Related Work positioning
- Create a comparison table (in main text or appendix) contrasting D2T2, QDT, EDT, WT, SPLT, and DoC along dimensions: target problem, guidance signal, RTG-free eval, horizon reduction, same-trajectory constraint, stochasticity focus.
- Add a paragraph explicitly stating: "While QDT also combines DT with Q-learning, it relabels RTG with conservative values and retains RTG at inference. D2T2 fundamentally replaces RTG with a predicted steering target, eliminating the need for manual return specification at test time."

### S6. Bounded claim scope in Conclusion
- Replace "SOTA performance" with: "D2T2 achieves competitive or superior performance relative to strong baselines in stochastic settings, with the largest gains observed on FrozenLake (up to +0.15 over DT) and CARLA benchmarks (+1.6 total score over SPLT)."
- Add explicit limitations paragraph covering: (a) same-trajectory steering constraint, (b) dependence on V(·) quality, (c) VAE usage criterion being ad-hoc, (d) no formal horizon-reduction guarantee.

## Storyline Options + Writing Outlines
### Abstract Outline (5-sentence structure)

**S1 — Problem and Domain:** "Decision Transformer (DT) achieves strong results in deterministic offline RL but degrades substantially in stochastic environments."
**S2 — Prior Gap:** "We show this degradation stems from the accumulating variance of returns-to-go (RTG) over the horizon, and prove that under deterministic dynamics, DT recovers the optimal trajectory almost surely."
**S3 — Proposed Solution:** "To address this, we propose D2T2, which replaces RTG with a steering guidance signal learned from temporal-difference value approximation and behavior cloning, eliminating the need for manual return specification at evaluation."
**S4 — Key Result (Stochastic):** "On stochastic tasks including FrozenLake, Tailgate, and CARLA, D2T2 substantially outperforms DT and prior stochasticity-focused methods."
**S5 — Key Result (Broad):** "Across 18 D4RL tasks, D2T2 achieves competitive performance against strong TD-learning baselines, with the largest gains on challenging replay datasets."

### Introduction Outline (4 Paragraphs)

**P1 — Big Picture + Gap (current paragraph 1 revised):**
- Role: Establish that offline RL with transformers is promising but has a known weakness.
- Claim: DT works well deterministically but fails under stochasticity due to RTG variance.
- Transitions: Open with the RL-supervised distinction briefly, then immediately state the gap.
- Key sentence: "This paper addresses the stochasticity challenge through a temporal-difference steering mechanism."

**P2 — Our Analysis + Theoretical Insight (current paragraph 2):**
- Role: Explain the formal result (Proposition 1) and its implications.
- Claim: DT recovers optimal trajectory under deterministic dynamics; RTG variance grows under stochasticity.
- Key sentence: "Our analysis reveals that the growing variance of RTG over the horizon is the root cause of DT's failure in stochastic environments."
- Transition to next paragraph: "This insight suggests two improvements: replace RTG with a lower-variance signal, and shorten the prediction horizon."

**P3 — Method Overview + Design Choices:**
- Role: Introduce D2T2's two design principles (TD signal, shorter horizon via state targeting).
- Claim: D2T2 maps state to a steering vector via value function + behavior cloning.
- Key sentence: "D2T2 learns to predict a high-value future state from current context alone, converting the original long-horizon prediction into a shorter-horizon one."
- Transition: "This design also eliminates the need for manual RTG input at test time."

**P4 — Contribution Summary + Evaluation Scope:**
- Role: State contributions and list benchmarks.
- Contributions should be bounded claims (not SOTA): (1) Formal proof of DT optimal-trajectory recovery under determinism, (2) D2T2 method with learnable RTG-free guidance, (3) Strong empirical results on 5 benchmarks.
- Remove "bonus strength" framing for RTG elimination — it is a primary contribution.
- End with: "Novelty and comparison conclusions are deferred to the full literature verification."

### Current Storyline vs. Proposed Revision

**Current storyline weakness:** The introduction tries to cover too many topics in the first paragraph (RL vs SL, RvS, DT mechanism, limitations), burying the key insight. The contribution statements appear across three separate paragraphs (end of P1, middle of P2, P3) without a clean summary paragraph.

**Proposed revision benefit:** The 4-paragraph structure creates a clear Big Picture→Gap→Solution→Claim flow. Each paragraph has one role, making the narrative easy to follow. The contribution claims are explicitly bounded.

## Priority Revision Plan
### P0 — Must-fix before resubmission (validity-critical)

| Priority | Action | Sections Affected | Expected Impact | Effort |
|----------|--------|-------------------|-----------------|--------|
| P0 | Add statistical significance tests and full variance reporting for all experiments | Section 4, Tables 1-3, Figures 2 | Enables readers to verify claimed improvements; fixes the "ignored standard error" issue | Medium |
| P0 | Remove or qualify all "SOTA" claims, replace with bounded comparative statements | Abstract, Section 1, Section 4, Section 6 | Prevents overclaim; increases scientific credibility | Low |
| P0 | Explicitly define "well-trained" DT in Proposition 1 and add uniqueness lemma | Section 2.2, Appendix A | Makes theoretical contribution rigorous | Low |

### P1 — High priority (substantial quality improvement)

| Priority | Action | Sections Affected | Expected Impact | Effort |
|----------|--------|-------------------|-----------------|--------|
| P1 | Add limitation paragraph discussing same-trajectory steering constraint and V(·) dependence | Section 3.1, Section 6 | Provides honest scope boundaries; reduces reviewer pushback | Low |
| P1 | Clarify VAE error-mitigation mechanism with technical explanation | Section 3.1, Appendix B | Strengthens methodological rigor | Medium |
| P1 | Restructure Related Work with explicit comparison table (D2T2 vs QDT, EDT, WT, SPLT, DoC) | Section 5 | Clarifies novelty boundaries | Medium |
| P1 | Include DT(m) in all experimental figures and tables | Section 4 | Improves fairness of comparison baseline selection | Low |
| P1 | Add an ablation: D2T2 without steering guidance (using only raw value function) | Section 4, Appendix C | Quantifies contribution of behavior-cloning-based SG prediction | Medium |

### P2 — Nice-to-have (improves readability and completeness)

| Priority | Action | Sections Affected | Expected Impact | Effort |
|----------|--------|-------------------|-----------------|--------|
| P2 | Rewrite Introduction following 4-paragraph plan (Problem→Gap→Solution→Claims) | Section 1 | Improves narrative clarity | Medium |
| P2 | Quantify horizon reduction empirically (average steps to reach G_t vs full horizon) | Section 2.3, Appendix C | Validates the shorter-horizon claim | Low |
| P2 | Add VAE vs no-VAE ablation for MuJoCo tasks | Section 4, Appendix C | Completes ablation coverage | Low |
| P2 | Fix typo: "conjure" → "conjecture" in Appendix A | Appendix A | Corrects writing error | Negligible |

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|-----------------|-------------------|
| E1 | VDT: RTG→value function improves DT | Tailgate (3 stop-sign levels, ~100k samples, 300k timesteps) | Return (Fig 2a) | VDT > DT | TD learning reduces RTG variance | No statistical test; DT(m) omitted |
| E2 | D2T2 vs baselines (stochastic) | Tailgate (3 levels) | Return (Fig 2a) | D2T2 highest across all levels | D2T2 effective under stochastic transitions | No significance tests; missing DT(m) |
| E3 | D2T2 vs baselines (stochasticity level) | FrozenLake (p=0.2-0.6) | Return (Fig 2b) | D2T2 competitive vs IQL; beats IQL at p=0.6 | D2T2 robust across stochasticity | "Standard error ignored" — no variance |
| E4 | D2T2 vs baselines (CARLA NoCrash) | Town01→Town02 (25 routes, 10 seeds) | Success%, Speed (Table 1) | D2T2: 98.3% success, 2.81 m/s | SOTA on NoCrash | Only 2 metrics; collision/infraction rates unreported per route |
| E5 | D2T2 vs baselines (CARLA Leaderboard) | Leaderboard devtest (10 seeds) | Total Score, Completion%, Collision/km, Infraction/km (Table 2) | D2T2: 70.2 total score | Competitive on Leaderboard | Overlap in confidence intervals with DT(t) and SPLT |
| E6 | D2T2 vs DT + TD methods (D4RL MuJoCo) | 9 Gym tasks (10 seeds) | Normalized score (Table 3) | D2T2 best average (91.3) | D2T2 competitive on deterministic tasks | Not best on 3/9 tasks; baselines from different papers |
| E7 | D2T2-n vs D2T2 (VAE ablation, AntMaze) | 6 AntMaze tasks (10 seeds) | Success rate (Table 11) | D2T2 > D2T2-n in all tasks | VAE helps in high-dim tasks | Only AntMaze/Kitchen; no MuJoCo VAE ablation |
| E8 | D2T2-n vs D2T2 (VAE ablation, FrankaKitchen) | 3 Kitchen tasks (10 seeds) | Normalized score (Table 12) | D2T2 slightly > D2T2-n | VAE marginally helpful | Small deltas; confidence intervals overlap |

### Research-Theme Gap Diagnosis

1. **New Knowledge — Validated but bounded.** The insight that RTG variance causes DT's stochastic degradation is well-supported theoretically (Proposition 1) and empirically (VDT experiment). However, the claim that D2T2 achieves "shorter horizon" steering is intuition-only — no formal or empirical verification.

2. **Reproducibility — Partially supported.** Algorithm descriptions and hyperparameters are provided. However, the two-phase training (SG learning + policy learning) is not clearly separated in the main text, and the training loss for π_θ is underspecified. The code is submitted as supplementary material but not thoroughly reviewed here.

3. **Potential to Change Practice — Moderate.** The D2T2 approach of replacing RTG with a learned guidance signal is practically useful for eliminating manual RTG tuning at inference time. However, the same-trajectory constraint on steering targets limits applicability in low-coverage settings, and the dependence on a pre-trained V(·) adds complexity.

### Proposed Research Experiments (P0/P1/P2)

| Exp ID | Target Claim | Hypothesis | Minimal Design | Controls/Baselines | Metrics | Success Criterion | Est. Cost | Quality Gain |
|--------|-------------|------------|---------------|-------------------|---------|------------------|-----------|-------------|
| P0-E1 | "Significantly higher" results | D2T2 gains are statistically significant | Compute paired bootstrap p-values for all Table 3 comparisons | DT, IQL, MCQ, SPLT | p-value, effect size Cohen's d | p < 0.05 for tasks where D2T2 claims superiority | 1-2 days | High: validates core empirical claims |
| P0-E2 | VAE error mitigation | VAE latent encoding reduces V(·) noise propagation | Compare D2T2 vs D2T2-n on MuJoCo tasks (Table 3) | D2T2-n, D2T2 | Normalized score, std | D2T2 > D2T2-n on ≥7/9 tasks | 2-3 days | Medium: clarifies VAE role |
| P1-E3 | Steering guidance independent value | BC-based SG prediction adds value beyond raw V(·) | Compare D2T2 vs "D2T2-V" (using raw V(s) as guidance instead of predicted SG) | D2T2, D2T2-V, DT | Return (all tasks) | D2T2 > D2T2-V on ≥3/5 benchmarks | 2-3 days | Medium: validates SG prediction component |
| P1-E4 | Horizon reduction claim | Steering targets reduce effective prediction horizon | Measure average τ(s_t) = steps to reach G_t vs full horizon T for each task | None (descriptive) | Horizon reduction ratio (T-τ)/T | Ratio > 0.3 on average across tasks | 1 day | Medium: supports a key design claim |
| P2-E5 | Stitching improvement | D2T2 combines sub-trajectories better than DT | Compare trajectory composition rates on AntMaze replay datasets | DT, D2T2 | Fraction of actions not from any single demonstration trajectory | D2T2 > DT on diverse datasets | 2-3 days | Low-Medium: supports soft claim |

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 6.5/10**

*Rationale:* The paper addresses a meaningful problem (DT's stochastic degradation) with a well-motivated approach. The theoretical analysis of DT's deterministic behavior is instructive, and the experimental scope is broad. However, the score is constrained by: (1) insufficient statistical rigor across experiments, including suppressed error reporting and unsupported "SOTA" claims; (2) logical gaps in the theoretical proof that weaken its formal contribution; (3) a key methodological constraint (same-trajectory steering targets) that is not discussed as a limitation; and (4) unclear VAE error-mitigation mechanism. The primary scoring dimensions — research value and novelty — are moderate: the idea of replacing RTG with a learned TD-based guidance signal is practically useful but builds directly on existing DT+Q-learning combinations, and the theoretical analysis is intuition-level rather than formally complete.

**Post-Revision Target: [7.5, 8.0]/10**

*Rationale:* If the authors address the P0 and P1 items — particularly adding statistical rigor, bounding claims, clarifying the theoretical assumptions, discussing limitations, and strengthening the VAE justification — the paper could reach a solid score of 7.5-8.0. The core method has genuine practical value (eliminating RTG tuning), and the experimental scope is already strong. The upper bound is limited by the inherent design constraint (same-trajectory steering) which cannot be fully resolved without architectural changes, and by the difficulty of fully proving the horizon-reduction claim.