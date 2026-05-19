## Summary
# Final Review Report

## Summary

This paper proposes CDiffuser, a method that integrates contrastive learning into diffusion-based trajectory planning for offline reinforcement learning. The core idea is to bias the diffusion trajectory generation process so that generated states are pulled toward high-return states and pushed away from low-return states, using a soft probabilistic partition based on modified influence functions. The method builds on Diffuser (Janner et al., 2022) and adds a contrastive module trained jointly with the trajectory reconstruction and return prediction objectives.

**Contribution Claims (C1-C3):**
- C1: A novel method (CDiffuser) that improves diffusion-based RL algorithms via return-contrastive trajectory generation.
- C2: First application of contrastive learning over state returns (rather than representations) to bias diffusion model training in RL.
- C3: Empirical demonstration of outstanding performance on 12 D4RL benchmarks.

**Strengths:**
- The motivation is clear and addresses a real limitation of prior diffusion planning methods that treat all samples uniformly.
- The soft-partitioning design via influence functions is principled and provides a continuous spectrum between high/low return states.
- Results on 12 D4RL benchmarks show consistent improvements over the backbone Diffuser across all tasks, with particularly strong gains on Hopper-Medium (+18.0) and Med-Replay Walker2d (+13.6).
- The ablation study systematically isolates the effect of the contrastive module, positive-only training, and guidance removal.

**Key Weaknesses:**
- The contrastive loss (Eq. 9) deviates from standard InfoNCE by omitting positive similarities from the denominator, which changes the optimization behavior and may not perform true contrastive learning as claimed.
- The gradient derivation in Appendix A.5 contains mathematical errors in the ∇_θ and ∇_ϕ expressions.
- The experimental analysis overclaims in several places (e.g., causal attribution of "long-term dynamic consistency" without proper controls, claiming "outstanding performance" while underperforming on HalfCheetah tasks).
- The hyperparameter σ = 1×10^8 used in several settings effectively performs hard thresholding, contradicting the soft-partitioning motivation.
- The related work section lacks critical positioning against the strongest competitor (Decision Diffuser).
- Novelty verification is deferred due to external retrieval unavailability in this run.

**Recommendation:** Major revision required. The core idea is sound and the experimental results are promising, but the paper needs correction of mathematical errors, tightening of claims, and more careful experimental analysis before acceptance.

## Strengths
1. **Well-motivated problem framing**: The paper identifies a genuine limitation in diffusion-based planning methods—they generate trajectories whose state distribution mirrors the offline dataset, making high-return states under-represented when low-return samples dominate. This is a clear and practical issue in offline RL where datasets often contain heterogeneous quality.

2. **Principled soft-partitioning design**: The use of modified influence functions (Eq. 7-8) for probabilistic grouping of states into high/low return categories is more nuanced than hard thresholding. The sigmoidal gating allows boundary samples to contribute to both positive and negative sets, which is a reasonable design for handling ambiguous states near the decision boundary.

3. **Strong empirical results on multiple settings**: CDiffuser outperforms the backbone Diffuser on all 12 D4RL tasks, with substantial gains on Medium Hopper (+18.0 normalized score) and Med-Replay Walker2d (+13.6). The ablation study (Figure 4) convincingly shows that the contrastive module provides additive benefits beyond guidance, that both positive and negative samples are needed, and that the method is particularly effective on medium/replay datasets where high-return samples are scarce.

4. **Comprehensive hyperparameter analysis**: Section 4.5 and Appendix A.3 provide detailed hyperparameter specifications and sensitivity analysis across ξ, ζ, σ, and λ_c, which aids reproducibility and practical deployment.

5. **Reproducibility efforts**: The paper provides pseudocode (Appendix A.1), detailed hyperparameter tables (Table 2), and an anonymous code repository. Hardware specifications are also reported.

6. **Honest limitation disclosure**: The paper acknowledges a key limitation (state-return ambiguity when the same state appears in both high- and low-return trajectories), which is an important boundary condition for the method's applicability.

## Weaknesses
### Major Weaknesses (Fixable)

1. **Contrastive loss formulation is incorrect (Page 5 - Section 3.2.2)**. Equation (9) defines the contrastive loss as L = -log[ Σ pos / Σ neg ], which omits positive similarities from the denominator. Standard InfoNCE uses L = -log[ pos / (pos + Σ neg) ]. The current form may not perform true contrastive learning as claimed, since the denominator lacks the critical positive-negative competition mechanism. (Annotation ID: 8f42d55e)

2. **Gradient derivation errors in Appendix A.5 (Page 15)**. The derivation for ∇_θ incorrectly drops λ_d ∂L_d/∂θ, and the derivation for ∇_ϕ incorrectly retains λ_d ∂L_d/∂ϕ (which is zero). While the textual conclusion happens to be correct, the supporting mathematics is flawed. (Annotation ID: 24ed240c)

3. **Selective experimental reporting (Page 6 - Section 4.2)**. The narrative claims "outstanding performance" and "best or second-best on 6 of 9 locomotion tasks" but omits cases where CDiffuser underperforms, most notably on HalfCheetah-Medium (43.9 vs DD 49.1, IQL 47.4) and HalfCheetah-Med-Replay (40.0 vs MOPO 53.1, CQL 45.5). (Annotation ID: ff95c850)

4. **Overclaimed causal attribution in dynamic consistency analysis (Page 8 - Section 4.4)**. The paper claims "the contrastive module benefits the long-term dynamic consistency" based on 24 trajectories with purely qualitative visual comparison (color grids), no quantitative metrics, and no causal control. (Annotation ID: d7d1a0b2)

5. **Unsupported mechanistic claim (Page 7 - Section 4.3)**. "CDiffuser is better at making use of low-return samples" is a causal mechanism claim not supported by the evidence, which only shows correlational patterns across dataset types. (Annotation ID: e936e3d9)

6. **Contradiction in soft-partitioning claim (Page 4, Appendix Table 2)**. Several datasets use σ = 1×10^8, which makes the sigmoid effectively a step function, contradicting the stated motivation for "probabilistic partitioning" to handle boundary samples softly. (Annotation ID: 42fbb508)

### Minor Weaknesses

7. **Abstract lacks quantified results (Page 1)**. No concrete performance numbers are reported in the abstract.

8. **First-claim scope (Page 2 - Contributions)**. The claim of being "first" to apply contrastive learning for return contrasting in diffusion RL would benefit from explicit scope qualifiers.

9. **Related work lacks critical positioning (Page 9 - Section 5)**. The section does not explain why return conditioning in Decision Diffuser is insufficient compared to CDiffuser's approach.

10. **Conclusion vague on future directions (Page 9 - Section 6)**. "Contrast on actions also deserves to be explored" is too generic; specific research directions would be more useful.

11. **Missing Maze2d baselines (Page 6 - Table 1)**. Several natural baselines (DD, DT, TT) are not reported for Maze2d, weakening the "best on all navigation tasks" claim.

12. **Novelty verification incomplete**: Due to external retrieval being unavailable in this run, the novelty of C2 ("first to apply contrastive learning to contrast return for diffusion") cannot be fully verified against the literature. Manual verification is required.

## Key Issues
### Ranked Error Board (Top 5 by Severity × Validity Risk)

| Rank | Issue | Section/Page | Severity | Validity Risk | Fixability | Annotation ID |
|------|-------|-------------|----------|---------------|------------|---------------|
| 1 | Contrastive loss Eq. (9) deviates from InfoNCE; denominator lacks positive sample competition | Page 5 - Section 3.2.2 | Major | High - May not learn true contrastive representations | Fixable - Replace with standard InfoNCE form | 8f42d55e |
| 2 | Gradient derivation errors in Appendix A.5 (∇_θ and ∇_ϕ) | Page 15 - Appendix A.5 | Major | Medium - Correct conclusion but wrong math undermines trust | Fixable - Correct as specified in annotation | 24ed240c |
| 3 | Selective experimental reporting; HalfCheetah underperformance unmentioned | Page 6 - Section 4.2 | Major | Medium - Overclaims weaken objectivity | Fixable - Add balanced discussion | ff95c850 |
| 4 | Unsupported causal claim about dynamic consistency (no quantitative metrics, no control) | Page 8 - Section 4.4 | Major | High - Causal attribution unsupported | Fixable - Add quant metrics, soften language | d7d1a0b2 |
| 5 | Soft-partitioning vs extreme σ=1e8 contradiction | Page 4/8 - Sections 3.2.1/4.5 | Major | Medium - Reduces credibility of design narrative | Fixable - Justify σ choice or rename to "adaptive thresholding" | 42fbb508 |

### Top-10 Extended Board (continued)

| 6 | Mechanistic overclaim about "making use of low-return samples" | Page 7 - Section 4.3 | Major | Medium - Correlation/causation confusion | e936e3d9 |
| 7 | Abstract lacks quantified headline result | Page 1 - Abstract | Minor | Low - Reduces first-impression impact | 9554877a |
| 8 | First-claim needs tighter scoping | Page 2 - Contributions | Minor | Low - Vulnerable to reviewer challenge | 5e63095d |
| 9 | Related Work lacks position vs Decision Diffuser | Page 9 - Section 5.1 | Minor | Low - Weakens narrative | 65479719 |
| 10 | Conclusion's future direction too vague | Page 9 - Section 6 | Minor | Low - Missed opportunity | d4ed125d |

## Actionable Suggestions
Below are concrete, executable revision actions mapped to the key issues identified. Each item is labeled **Must** (publication-critical) or **Nice-to-have** (quality improvement).

### P0 — Critical Fixes

**1. Fix contrastive loss Eq. (9) — Must**
Replace Eq. (9) with the standard InfoNCE form that includes positives in the denominator:
$$L^i_h = -\log \frac{\sum_{k=0}^{\kappa} \exp(\text{sim}(f(\hat{s}^{i,0}_h), f(s^+_h))/T)}{\sum_{k=0}^{\kappa} \exp(\text{sim}(f(\hat{s}^{i,0}_h), f(s^+_h))/T) + \sum_{k=0}^{\kappa} \exp(\text{sim}(f(\hat{s}^{i,0}_h), f(s^-_h))/T)}$$
If the authors deliberately chose the ratio-form for a specific reason, this design choice must be explicitly justified with analysis of gradient behavior. Update all downstream references (Eq. 13, Algorithm 1) accordingly.

**2. Correct gradient derivation in Appendix A.5 — Must**
Replace ∇_θ and ∇_ϕ derivations with:
- ∇_θ = λ_d ∂L_d/∂θ + λ_c ∂L_c/∂θ
- ∇_ϕ = λ_v ∂L_v/∂ϕ
This correctly reflects that ψ_θ is updated by trajectory reconstruction and contrastive loss, while J_ϕ is updated only by return prediction.

**3. Add balanced experimental discussion — Must**
In Section 4.2, add a paragraph acknowledging cases where CDiffuser underperforms. Specifically discuss:
- HalfCheetah-Medium (43.9) vs IQL (47.4), DD (49.1)
- HalfCheetah-Med-Replay (40.0) vs MOPO (53.1)
- Why the contrastive mechanism might be less effective when state-return correlation is weak (e.g., HalfCheetah).

### P1 — Important Improvements

**4. Add quantitative metrics for dynamic consistency analysis — Must**
Replace the qualitative visual comparison in Figure 6 with a quantitative analysis: report mean ± std of state similarity across all trajectories for each method, and include a paired statistical test (e.g., Wilcoxon) comparing CDiffuser vs Diffuser.

**5. Soften causal claims — Must**
- Replace "the contrastive module benefits the long-term dynamic consistency" with "CDiffuser's generated trajectories show higher state similarity to ground-truth trajectories, which is consistent with improved dynamics modeling."
- Replace "CDiffuser is better at making use of low-return samples" with "CDiffuser shows larger gains on datasets with more low-return samples, which is consistent with the hypothesis that..."
- Replace "actions...are always toward the high-return states" with "the learned policy tends to select actions that lead to higher-return states."

**6. Justify extreme σ values — Must**
In Section 3.2.1 or Appendix A.3, add a discussion explaining why σ = 1×10^8 is used for several datasets. If this approximates hard thresholding, acknowledge the trade-off and clarify when soft vs hard partitioning is appropriate.

**7. Add quantified headline result to Abstract — Nice-to-have**
Insert a concrete number, e.g., "outperforms Diffuser on all 12 D4RL tasks with average gains of up to +18.0 points."

**8. Scope the first-claim — Nice-to-have**
Tighten contribution (ii) to: "To our knowledge, this is the first work to apply contrastive learning directly to the diffusion trajectory generation process for return-based state biasing in offline RL."

### P2 — Quality Improvements

**9. Strengthen related-work positioning — Nice-to-have**
Add explicit comparison with Decision Diffuser explaining why its trajectory-level return conditioning is insufficient and how CDiffuser's per-state contrast provides finer-grained control.

**10. Add Maze2d baselines — Nice-to-have**
Report results for DT, TT, and DD on Maze2d environments, or explicitly state they are omitted with justification.

**11. Improve conclusion — Nice-to-have**
Add a compact summary of validated findings (2-3 key results with numbers), then the limitation, then a more specific future direction (e.g., "action-level contrastive objectives or inverse dynamics modeling").

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current manuscript uses a competent but conventional structure: Background → Method → Experiments → Related Work → Conclusion. The introduction follows: offline RL context → extrapolation error → diffusion models → gap identification → proposed solution → contributions. This is serviceable but can be improved for clarity and impact.

**Three alignment checks on current storyline:**
- Problem alignment: The stated problem (diffusion planning neglects sample return diversity) directly matches the proposed solution (return contrast mechanism). ✓
- Variable alignment: Core concepts (state return, contrastive learning, trajectory generation) appear consistently throughout. ✓
- Contribution-evidence alignment: Abstract/introduction claims are generally supported by experiments, though the "outstanding performance" framing needs moderation. Partial ✓

### Recommended Storyline Candidate (Selected)

**Title revision:**
"CDiffuser: Return-Contrastive Diffusion for Trajectory Planning in Offline Reinforcement Learning"

**Rationale:** The current title mentions "Planning Towards High Return States Via Contrastive Learning" which is informative but slightly verbose. The revised title clarifies the problem domain, method name, and core mechanism.

### Abstract Outline (S1-S5)

**S1 - Problem & Domain (target 1 sentence):**
"Offline reinforcement learning agents can benefit from diffusion-based trajectory planning, but existing methods generate trajectories whose state distribution mirrors the dataset, making high-return states unlikely when low-return data dominates."

**S2 - Prior Gap (target 1 sentence):**
"Even with classifier-guided sampling, performance degrades when high-return states are scarce because the guidance cannot fully overcome the prior data distribution."

**S3 - Proposed Method (target 1-2 sentences):**
"We propose CDiffuser, which augments diffusion-based planning with a return contrastive mechanism: during training, a contrastive loss pulls generated trajectory states toward high-return regions and pushes them away from low-return regions using a soft probabilistic partitioning of states based on their returns."

**S4 - Key Result (target 1 sentence):**
"On 12 D4RL benchmarks, CDiffuser outperforms the backbone Diffuser on all tasks, achieving average gains of up to +18.0 normalized score, with best or second-best results on 9 of 12 settings."

**S5 - Bounded Implication (target 1 sentence):**
"A limitation is that the method relies on return-to-go as the contrast criterion, which is ambiguous when the same state appears in both high- and low-return trajectories."

**Note:** The current abstract uses S1-S4 but lacks a concrete S5 result, has no quantified result in S4, and omits a limitation. The revised version above addresses these gaps.

### Introduction Outline (Paragraph-by-Paragraph)

**P1 (current: offline RL context):**
Role: Establish importance of offline RL and its real-world applications.
Current defect: Generic paragraph that could be shortened.
**Revision**: Merge with P2. Start directly with the core challenge: "Offline reinforcement learning enables learning from static datasets without costly interaction, but static data introduces the extrapolation error problem—out-of-distribution actions receive erroneously optimistic value estimates."

**P2 (current: extrapolation error and conservative methods):**
Role: Identify limitation of prior conservative approaches.
Keep this paragraph mostly as-is but strengthen the transition: end with "Diffusion models offer a fundamentally different approach: they learn the full data distribution as a generative process, naturally staying close to the observed data without explicit conservatism."

**P3 (current: diffusion for planning):**
Role: Introduce diffusion-based planning and identify the gap.
Key revision needed: Replace the overconfident claim "the results remain unsatisfactory" with a nuanced statement: "While guidance sampling helps, its effectiveness degrades when high-return samples are scarce, as the guidance signal cannot fully overcome the prior distribution."

**P4 (current: proposed method introduction):**
Role: Present CDiffuser's intuition and approach.
Key revision: Strengthen the motivation for why contrastive learning is the right tool. Add: "Contrastive learning naturally implements the desired behavior—pulling representations together for similar items and pushing them apart for dissimilar ones—making it a principled choice for return-based state biasing."

**P5 (current: contributions):**
Role: Summarize contributions.
Key revision: (i) Tighten C1 to "CDiffuser, a diffusion-based trajectory planner augmented with a return-contrastive objective." (ii) Qualify C2 as "the first application of return-contrastive learning (rather than representation learning) to bias diffusion model training in offline RL, to our knowledge." (iii) Replace C3 with a specific claim: "CDiffuser achieves consistent gains over Diffuser on all 12 D4RL tasks, with especially large improvements on datasets with mixed-quality trajectories."

### Alternative Storyline Candidates

**Candidate B (Application-First):** Start with a concrete motivating example (e.g., "Consider two trajectories through the same state—one leads to a 200-step run, the other to a fall after 10 steps. Which action should the agent learn?"). This framing immediately grounds the problem. Risk: May be less conventional for a technical paper.

**Candidate C (Method-Forward):** Start with the insight that contrastive learning principles can be applied to trajectory optimization, then derive the gap from first principles. Better for readers familiar with contrastive learning but less accessible to RL-general audience.

## Priority Revision Plan
### Revision Order (Highest Impact First)

```text
ASCII Diagram — Revision Strategy Roadmap

[Error: Eq.(9) contrastive loss broken]
    -> [Fix: Replace with standard InfoNCE]
    -> [Expected: Loss behaves as intended; claims match mechanism]
    -> [Effort: ~2 hours; changes to Eq.(9),(13), Algorithm 1]

[Error: Appendix A.5 gradient derivation]
    -> [Fix: Correct ∇_θ and ∇_ϕ expressions]
    -> [Expected: Mathematical soundness restored]
    -> [Effort: ~30 minutes]

[Overclaim: selective reporting / causal attribution]
    -> [Fix: Add balanced discussion + soften wording]
    -> [Expected: Improved objectivity; reduced reviewer pushback]
    -> [Effort: ~1 day for rewriting+figure revision]

[Contradiction: σ=1e8 vs soft-partitioning claim]
    -> [Fix: Justify σ choice in text, or rename mechanism]
    -> [Expected: Design narrative becomes self-consistent]
    -> [Effort: ~1 hour]

[Minor: abstract, first-claim, related work, conclusion]
    -> [Fix: Apply suggested rewrites]
    -> [Expected: Improved first impression and positioning]
    -> [Effort: ~2-3 hours total]
```

### Stage Execution Plan

**Stage 1 (Must-Do Before Resubmission):**
1. Fix Eq. (9) contrastive loss → standard InfoNCE
2. Correct Appendix A.5 gradient derivation
3. Add balanced discussion paragraph in Section 4.2 (HalfCheetah underperformance)
4. Replace qualitative dynamic consistency analysis with quantitative metrics
5. Justify or rephrase σ = 1e8 usage

**Stage 2 (Strongly Recommended):**
6. Soften causal/mechanistic claims throughout
7. Scope contribution (ii) first-claim with explicit qualifiers
8. Strengthen related-work positioning against Decision Diffuser
9. Add quantified result to abstract

**Stage 3 (Quality Improvements):**
10. Improve conclusion with validated findings summary and specific future direction
11. Add Maze2d baselines if feasible
12. General writing polish following the storyline outline in Section 6

### Expected Impact After Revision

After Stage 1 fixes, the core technical soundness concerns (loss formulation, gradient math) would be resolved, making the paper reviewer-ready. Stage 2 improvements would address novelty positioning and objectivity concerns. The overall quality would move from borderline to solid accept range.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Benchmark comparison on locomotion tasks | 9 D4LM tasks, 3 envs × 3 datasets, compared vs 7 baselines | Normalized average return (10 seeds) | CDiffuser best/2nd-best on 6/9; outperforms Diffuser on all 9 | C1, C3 | Underperforms on HalfCheetah-Medium and HalfCheetah-Med-Replay; not discussed |
| E2 | Benchmark comparison on navigation tasks | 3 Maze2d variants, vs IQL/CQL/Diffuser | Normalized average return | CDiffuser best on all 3 tasks | C1, C3 | Several baselines (DT, TT, DD) not reported |
| E3 | Ablation: remove contrastive loss (CDiffuser-C) | Same as E1, remove L_c from Eq.(14) | Normalized average return | CDiffuser > CDiffuser-C on all tasks | C1, design validation | Does not control for parameter count |
| E4 | Ablation: positive-only training (CDiffuser-N) | Same as E1, train only on high-return states | Normalized average return | CDiffuser-N < CDiffuser on all tasks; CDiffuser-N < CDiffuser-C on 4/9 | Design validation | Confounded by dataset size reduction |
| E5 | Ablation: remove guidance (CDiffuser-G) | Same as E1, remove ρ∇J_ϕ from Eq.(5) | Normalized average return | CDiffuser-G > Diffuser-G on 8/9; CDiffuser-G > CDiffuser-C on medium/med-replay | C1, shows contrast helps beyond guidance | Not tested on Maze2d |
| E6 | State-reward distribution analysis | Walker2d-Med-Replay, compare Diffuser/DD/CDiffuser | Visual scatter plot (Fig. 5) | CDiffuser achieves higher rewards in both in-distribution and OOD regions | C1 (qualitative) | Subjective visual comparison; no quantitative metric |
| E7 | Long-term dynamic consistency | 24 trajectories × 32 steps, compare Diffuser/DD/CDiffuser | State similarity heatmap (Fig. 6) | CDiffuser has more blue grids (higher similarity) | C1 (qualitative) | No quantitative metric; no statistical test; small sample |
| E8 | Hyperparameter sensitivity (ξ, ζ, σ, λ_c) | Hopper-Medium with varying single parameters | Performance vs parameter value (Fig. 7) | Unimodal sensitivity patterns; smooth tuning | Practical guidance | No error bars; no interaction analysis |

### Research-Theme Gap Diagnosis

**New Knowledge:** The core contribution—using contrastive learning directly on trajectory states for return biasing—is conceptually novel. However, the current experimental design does not fully establish *why* the contrastive module helps. The ablation shows it *does* help, but the mechanism (pulling/pushing states in latent space) is not directly verified.

**Reproducibility:** The paper provides adequate detail (pseudocode, hyperparameters, hardware specs). Main reproducibility risks: (1) the contrastive loss uses a non-standard form (Eq. 9) which may affect implementation behavior, (2) the projection network f(·) is described as "a linear layer with Sigmoid" but its input/output dimensions are not specified.

**Potential to Change Practice:** The method is a direct improvement on Diffuser with moderate implementation overhead. If results hold across more diverse environments, it could become a standard extension for diffusion-based planning. However, the lack of analysis on failure cases (where CDiffuser underperforms) limits practical guidance.

### Proposed Research Experiments (P0/P1/P2)

```text
ASCII Diagram — Experiment Upgrade Plan

P0 (Before Resubmission — Critical)
├── E9: State-return correlation analysis for HalfCheetah
│   ├── Hypothesis: CDiffuser underperforms when state-return correlation is weak
│   ├── Design: Compute return variance across states in HalfCheetah datasets
│   └── Expected: Explanation for HalfCheetah underperformance
└── E10: Quantitative dynamic consistency metric
    ├── Hypothesis: CDiffuser improves mean state prediction accuracy
    ├── Design: Report mean±std state similarity, add paired t-test vs Diffuser
    └── Expected: Statistical evidence for claim

P1 (Important — High Yield)
├── E11: Matched-capacity ablation 
│   ├── Hypothesis: CDiffuser gains are not from added parameters
│   ├── Design: Train CDiffuser-C with same total loss magnitude as CDiffuser
│   └── Expected: Rules out capacity confound
├── E12: OOD generalization test
│   ├── Hypothesis: CDiffuser's state biasing improves generalization
│   ├── Design: Evaluate on environment with modified dynamics (e.g., different friction)
│   └── Expected: Robustness evidence
└── E13: Interaction experiment (ξ, ζ, λ_c joint sweep)
    ├── Hypothesis: Optimal ξ depends on λ_c due to loss trade-off
    ├── Design: 2D grid over (ξ, λ_c) with fixed σ
    └── Expected: Practical tuning guidance

P2 (Nice-to-Have)
└── E14: Action-level contrast variant
    ├── Hypothesis: Contrasting actions rather than states captures different info
    ├── Design: Replace Eq.(9) with action-based contrastive objective
    └── Expected: Extension validating action-contrast future direction
```

### Proposed Experiment Details

**E9 (P0) — State-Return Correlation Analysis:**
- Target Claim: Explaining CDiffuser's performance variation across environments
- Minimal Design: Compute Spearman correlation between state visitation frequency and return for HalfCheetah, Hopper, Walker2d datasets. Compare CDiffuser's gain vs this correlation.
- Success Criterion: Show that CDiffuser gains positively correlate with state-return separability
- Estimated Cost: ~1 day (analysis only, no training needed)
- Expected Gain: Explains failure cases; strengthens contribution

**E10 (P0) — Quantitative Dynamic Consistency:**
- Target Claim: C1 (long-term dynamic consistency benefit)
- Minimal Design: For each of the 3 methods (Diffuser, DD, CDiffuser), compute mean cosine similarity between generated and ground-truth states over 50 trajectories (not 24). Report with ±std and paired Wilcoxon test p-values.
- Success Criterion: CDiffuser achieves statistically significant improvement (p<0.05) over Diffuser
- Estimated Cost: ~2 days (re-run generation, analysis code)
- Expected Gain: Replaces subjective visual claim with rigorous evidence

**E11 (P1) — Matched-Capacity Ablation:**
- Target Claim: C1 (contrastive module benefit is genuine, not from added capacity)
- Minimal Design: Increase CDiffuser-C's U-Net width/height to match CDiffuser's parameter count. Compare performance.
- Success Criterion: CDiffuser still outperforms matched-capacity CDiffuser-C
- Estimated Cost: ~3 days (training additional models)
- Expected Gain: Eliminates capacity confound; strengthens causal claim

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
### Final Score: 5.5 / 10

**Rationale**: The paper presents a promising idea (return-contrastive diffusion for offline RL planning) with solid empirical results showing consistent improvements over the backbone Diffuser across 12 D4RL tasks. However, the score is constrained by the following factors:

- **Research Value (Primary Dimension)**: Moderate. The idea of using contrastive learning for return biasing in trajectory generation is conceptually sound and practically useful. However, the paper does not fully establish *why* it works mechanistically, and the HalfCheetah underperformance is not discussed, weakening the contribution's generalizability claim.

- **Novelty (Primary Dimension)**: Moderate (+1 increment over Diffuser/DD). The paper's core novelty—applying contrastive learning directly to trajectory states for return biasing—is incremental but meaningful. The first-claim needs scoping. Novelty verification is deferred due to external retrieval unavailability in this run, so this score may need adjustment after literature verification.

- **Validity/Soundness**: Moderate concerns. The contrastive loss Eq. (9) deviates from standard InfoNCE in an unexplained way. The gradient derivation in Appendix A.5 contains mathematical errors. While these are fixable, they currently reduce confidence in the implementation.

- **Reproducibility**: Good. Pseudocode, hyperparameter tables, and code link provided. The non-standard loss formulation is a minor concern.

### Post-Revision Target: [6.5, 7.5] / 10

**Conditional on completing Stage 1 (Must-Do) fixes**:
1. Fix Eq. (9) to standard InfoNCE form
2. Correct Appendix A.5 gradient derivation
3. Add balanced discussion of HalfCheetah underperformance
4. Add quantitative metrics for dynamic consistency analysis
5. Justify σ = 1e8 usage

If all Stage 1 and Stage 2 items are addressed, the paper could reach **7.0-7.5/10**, placing it in the solid accept range for a conference. The upper bound is constrained by the incremental nature of the contribution and the need for external novelty verification.