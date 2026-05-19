## Summary
# Final Review Report

## Summary

This paper presents Uni-O4, a framework that unifies offline and online reinforcement learning using a single on-policy PPO objective, eliminating the need for extra conservatism or regularization that plagues prior offline-to-online methods. The key technical contributions are: (1) an ensemble behavior cloning approach with disagreement regularization to better capture multi-modal behavior policies from offline data; (2) a model-based offline policy evaluation method (AM-Q) combining approximate dynamics models and fitted Q-evaluation to enable safe multi-step policy improvement without online rollouts; and (3) a seamless transition to standard online PPO fine-tuning after offline pretraining.

The method is evaluated on D4RL benchmarks (MuJoCo locomotion, Adroit manipulation, Kitchen, Antmaze), where it achieves competitive or superior normalized returns against a comprehensive set of baselines including CQL, IQL, ATAC, BPPO, and Off2on. Real-world quadruped robot experiments on a latex mattress demonstrate the practical utility of the online-offline-online fine-tuning pipeline, showing adaptation to challenging deformable terrains with limited real-world interaction.

The paper is well-motivated, technically sound in its core design, and the empirical results are generally convincing. However, the manuscript has notable weaknesses: (1) novelty claims about "getting rid of sub-optimality and instability" are overstated given the loose theoretical guarantees and the 22% OPE ranking error rate; (2) several mathematical contributions (Proposition 1, Theorem 1) are relatively trivial and inflated in presentation; (3) the related work section reads as a list rather than a structured comparison; and (4) the conclusion makes unsupported "monotonically" improvement claims. The paper would benefit from more careful claim bounding, a reorganized related-work section, and an explicit limitations discussion.

## Strengths
1. **Clear problem identification and well-motivated approach.** The paper correctly identifies the fundamental tension in offline-to-online RL: conservatism that helps offline learning hurts online fine-tuning. The proposed solution — using a unified on-policy objective for both phases — is a conceptually clean and elegant way to avoid this tension entirely.

2. **Comprehensive empirical evaluation.** The experimental evaluation covers multiple domains (MuJoCo locomotion, Adroit manipulation, Kitchen, Antmaze, real-world quadruped locomotion) and compares against a wide range of baselines (CQL, IQL, TD3+BC, ATAC, BPPO, Off2on, PEX, Cal-QL, SPOT, etc). The 1M step online fine-tuning curves with standard deviations provide strong evidence for the method's effectiveness.

3. **Practical real-world demonstration.** The online-offline-online robot learning experiment on a quadruped navigating a latex mattress is a convincing proof-of-concept. The demonstration that offline fine-tuning can adapt a policy to a challenging deformable terrain with only 180K real-world steps, and further online fine-tuning can improve speed, illustrates the practical value of the unified framework.

4. **Computational efficiency.** The running time analysis showing Uni-O4 completes online fine-tuning in ~30 minutes vs >1000 minutes for Q-ensemble methods (Off2on) is a significant practical advantage for real-world deployment.

5. **Ablation studies supporting design choices.** The ensemble ablation (showing n=4 policies outperforms n=1), alpha ablation (showing α=0.1 works best), and OPE accuracy analysis provide empirical grounding for key design decisions. The policy ensemble analysis in Appendix A.6 (t-SNE visualizations, diversity analysis) is thorough and insightful.

## Weaknesses
1. **Overstated novelty and contribution claims.** The paper claims to "get rid of the sub-optimality and instability issues" and "eclipse all baseline methods" — these are too strong for the evidence provided. The 78% OPE exact ranking accuracy means 22% of policy selection decisions may be incorrect, undermining the "safe multi-step improvement" guarantee. The monotonic improvement claim in the conclusion is not theoretically supported (Theorem 2's bound is loose for practical horizons).

2. **Mathematical contribution inflation.** Proposition 1 is essentially a definition, not a proposition. Theorem 1's bound follows directly from the definition of KL divergence and the bound on Z(s) (1 ≤ Z(s) ≤ n) — it is a straightforward inequality, not a non-trivial theoretical result. The paper would benefit from demoting these to remarks and focusing theoretical claims on more substantive contributions.

3. **OPE theoretical gap.** Theorem 2 bounds |J(π,T) - J(π,ˆT)| but assumes cQ_τ ≈ Q* without bounding the Q-function approximation error. The bound grows as O(H²), making it very loose for H=1000 (MuJoCo). The practical usefulness of this bound for guaranteeing monotonic improvement is questionable.

4. **Ensemble BC objective lacks implementation details.** Equation 6 uses max_j π^j_β(a|s), which is non-differentiable. The paper does not explain how this is handled during optimization. The justification for choosing max over other aggregation functions (mean, geometric mean) is insufficient.

5. **Related work is a list, not a structured analysis.** The section presents 14+ papers in rapid succession without organizing them into comparison axes or clearly stating how each family relates to Uni-O4. This makes it difficult for readers to assess novelty positioning.

6. **Real-world experiment evaluation rigor.** The bar charts in Figure 5 lack clear axis labels and metric definitions. The baseline comparison is not apples-to-apples (WTW uses pure sim-to-real without real-world fine-tuning; IQL uses a different fine-tuning pipeline). The total data budget (7M simulator steps + 280K real-world steps) is not transparently reported.

7. **Missing limitations section.** The conclusion does not discuss limitations, failure modes, or boundary conditions of the method, which is a missed opportunity for scientific honesty and would strengthen the paper's credibility.

## Key Issues
### Issue 1 (Critical): Unsupported monotonic improvement claim (Page 9 - Conclusion)
The conclusion states that online fine-tuning "continuously enhances performance monotonically." However, the theoretical guarantee (Theorem 2) only bounds the error between true and estimated model-based returns with an O(H²) term, which is loose for practical horizon lengths (H=1000 for MuJoCo). The paper does not provide a formal proof of monotonic improvement for either the offline or online phase. The empirical curves show general upward trends but with some variance. This claim should be removed or replaced with "consistently improves performance in practice."

### Issue 2 (Major): OPE reliability and 22% ranking error rate (Page 9 - Section 5.3)
AM-Q's exact ranking accuracy is 78%, meaning 22% of policy selection decisions may choose a suboptimal policy. This is significant because multi-step improvement depends entirely on OPE decisions. The paper does not discuss how these errors affect the overall training process, whether errors compound across iterations, or whether there is graceful degradation. This should be addressed with a dedicated analysis.

### Issue 3 (Major): Overclaimed contribution statements (Page 2 - Introduction)
Phrases like "gets rid of the sub-optimality and instability issues" and "eclipsing all baseline methods" overstate the evidence. Uni-O4 does not universally outperform all baselines on all tasks (e.g., halfcheetah-medium-v2: 52.6 vs ATAC 54.3). These claims should be hedged and scope-bounded.

### Issue 4 (Major): Mathematical inflation of Proposition 1 and Theorem 1 (Page 4 - Method)
Proposition 1 is a definition (KL divergence with normalization). Theorem 1 is a straightforward consequence of the bound 1 ≤ Z(s) ≤ n and the definition of KL divergence. Neither constitutes a substantive theoretical contribution. They should be demoted to remarks or lemmas.

### Issue 5 (Major): Related Work is unstructured (Page 6 - Section 4)
The section lists 14+ papers in paragraph form without clear organizational axes. This makes it hard for readers to understand how Uni-O4 differs from each family of prior work. The section should be reorganized around comparison dimensions (conservatism handling, ensemble use, OPE reliance, etc.).

### Issue 6 (Major): Missing limitations discussion (Page 9 - Conclusion)
The conclusion does not acknowledge any limitations of the method, which reduces scientific credibility. Key limitations to discuss include: (a) AM-Q's 22% ranking error rate, (b) reliance on a learned dynamics model whose accuracy affects OPE, (c) the ensemble policy approach adds computational overhead during offline training, and (d) real-world evaluation is limited to one terrain type.

## Actionable Suggestions
### S1 (Must) — Bound claim scope in Abstract and Introduction
Replace unsupported SOTA and hyperbole with bounded, evidence-grounded claims. For the Abstract, replace "state-of-the-art performance" with "competitive or superior performance on evaluated D4RL benchmarks." For the Introduction, replace "gets rid of the sub-optimality and instability issues" with "substantially reduces fine-tuning instability and achieves higher asymptotic performance across most evaluated tasks."

**Mentor Revised Version (Abstract last sentence):**
"Through comprehensive evaluations on D4RL benchmarks, we demonstrate that Uni-O4 achieves competitive or superior normalized returns against prior methods across locomotion, manipulation, and navigation tasks, while offering substantially faster online fine-tuning."

### S2 (Must) — Remove or qualify monotonically improvement claim in Conclusion
Replace "continuously enhances performance monotonically" with "consistently achieves stable performance improvement during online fine-tuning across evaluated tasks." This is factually accurate without overclaiming theoretical guarantees.

### S3 (Must) — Add limitations section
Add a dedicated limitations paragraph at the end of the Conclusion discussing:
- AM-Q's 78% exact ranking accuracy and potential impact on multi-step improvement
- Dependence on learned dynamics model quality
- Computational overhead of ensemble policies during offline training
- Scope of evaluation (mainly simulated benchmarks, one real-world terrain)

### S4 (Must) — Restructure Related Work around comparison axes
Reorganize Section 4 into 3-4 grouped paragraphs with explicit comparison to Uni-O4:
- **Conservative methods** (CQL, IQL, AWAC): These constrain policy to avoid OOD actions; Uni-O4 avoids this by using on-policy objective
- **Over-conservatism correction** (Cal-QL, PEX): These add mechanisms to reduce conservatism during fine-tuning; Uni-O4 prevents conservatism from being introduced
- **Ensemble/Q-ensemble methods** (Off2on, Zhao et al.): These use multiple value functions; Uni-O4 uses policy ensemble for behavior support
- **Uncertainty-guided / model-based** (Guo et al., Niu et al.): These require additional models; Uni-O4's model is used only for OPE

### S5 (Must) — Demote Proposition 1 and Theorem 1
Proposition 1 should be renamed to "Definition 1" and Theorem 1 should become "Lemma 1" or "Remark 1." Add a note that the proof is straightforward from the normalization bounds in Appendix A.1. This correctly sets reader expectations about the theoretical contributions.

### S6 (Must) — Explain ensemble BC optimization details
Add a paragraph explaining how the max function in Equation 6 is handled during optimization (e.g., stop-gradient on max, or using a soft approximation). Justify the choice of max over mean by adding an ablation study comparing aggregation functions.

### S7 (Nice-to-have) — Extend OPE ablation with error analysis
Add a figure or table showing how AM-Q's 22% ranking error rate affects downstream performance. For example, compare the final fine-tuning performance when using AM-Q vs oracle policy selection (ground-truth online evaluation). This would demonstrate graceful degradation under OPE errors.

### S8 (Nice-to-have) — Improve Figure 5 labeling
Add clear axis labels to Figure 5(b) and 5(c) with units. Define "Average Return" explicitly in the caption. Add error bars or confidence intervals.

## Storyline Options + Writing Outlines
### Current Storyline Assessment

The current introduction follows this structure:
- P1: Robot learning pipeline scenario (motivation)
- P2: Online vs offline RL trade-off (background)
- P3: Pre-training + fine-tuning challenge (gap)
- P4: Conservatism problem analysis (gap elaboration)
- P5: BPPO limitation (prior work gap)
- P6: Method overview and contribution

**Strengths:** Good motivational opening, clear identification of the conservatism tension, effective use of Figure 1(b) to motivate the approach.

**Weaknesses:** The pipeline scenario in P1 is not revisited until the Conclusion and real-world experiments, creating a gap. P3-P4 spend too long on known problems before introducing the solution. The contribution paragraph (P6) makes overclaims.

### Recommended Storyline (Option A) — Problem-First with Stronger Hook

Restructure the introduction as follows:

**P1 (Hook):** Start directly with the tension: "Offline-to-online reinforcement learning faces a fundamental dilemma: the conservatism that enables safe offline learning becomes a liability during online fine-tuning, causing instability and suboptimal convergence." This immediately states the problem and stakes.

**P2 (Prior Attempts):** Summarize existing solutions (conservative initialization, Q-ensemble, regularization) and their shared limitation — they all still carry conservatism into the online phase, leading to either initial performance drops or slower convergence.

**P3 (Our Insight):** "In this work, we observe that the problem stems from misaligned objectives between offline and online phases. If both phases use the same on-policy objective, conservatism is never introduced, and transfer becomes seamless." This clearly states the core insight before technical details.

**P4 (Method):** Briefly describe Uni-O4's three stages: (1) ensemble BC for behavior policy recovery, (2) AM-Q-guided multi-step offline improvement, (3) standard online PPO fine-tuning.

**P5 (Contributions):** Explicitly state 2-3 concrete, bounded contributions with reference to empirical evidence.

### Abstract Outline (Complete)

S1 (Problem & Domain): "Combining offline and online reinforcement learning enables sample-efficient and safe real-world learning, but existing methods suffer from fine-tuning instability due to inherited conservatism from the offline phase."

S2 (Prior Gap): "Prior approaches introduce conservative regularization during offline training, which must then be overcome during online fine-tuning, often causing performance drops or suboptimal asymptotic performance."

S3 (Proposed Method): "We propose Uni-O4, which uses a unified on-policy PPO objective for both offline and online RL. By aligning objectives across phases, conservatism is never introduced, enabling seamless transfer."

S4 (Offline Mechanism): "During offline learning, an ensemble of behavior policies learned with disagreement regularization improves state-action coverage, and a model-based offline policy evaluation method (AM-Q) enables safe multi-step policy improvement without online rollouts."

S5 (Key Result): "On D4RL benchmarks, Uni-O4 achieves competitive or superior normalized returns across locomotion, manipulation, and navigation tasks, while real-world quadruped experiments demonstrate rapid adaptation to challenging terrains with limited interaction."

### Introduction Outline (Complete)

**P1 — Problem Framing (was P4 in current):**
"Offline-to-online RL faces a fundamental dilemma..." [Role: Establish stakes and technical tension. End with a question.]

**P2 — Prior Work and Limitation (condenses current P2-P4):**
"Existing methods address this through conservative Q-functions..." [Role: Show that all existing approaches share the same root limitation — they inherit conservatism. End with the conclusion that a fundamentally different approach is needed.]

**P3 — Our Insight and Method (replaces current P6):**
"Rather than correcting conservatism after the fact, we prevent it entirely by using the same on-policy objective for both offline and online phases." [Role: State the core insight clearly. Briefly describe the three-stage pipeline.]

**P4 — Empirical Preview (new):**
"We evaluate Uni-O4 on D4RL benchmarks and real-world robot tasks. The experimental results show that Uni-O4 achieves competitive offline initialization, stable and rapid online fine-tuning, and practical sim-to-real transfer." [Role: Give readers a roadmap of what evidence follows.]

**P5 — Contributions (explicit and bounded):**
• "A unified on-policy framework that eliminates the need for conservatism in offline-to-online RL."
• "An ensemble behavior cloning method with disagreement regularization that improves multi-modal behavior policy recovery."
• "A computationally efficient OPE method (AM-Q) that enables multi-step offline improvement without online rollouts."
• "Empirical demonstration of superior fine-tuning efficiency and stability across simulated and real-world tasks."

### Storyline Alignment Checks

| Check | Current Storyline | Recommended (Option A) |
|-------|------------------|----------------------|
| (a) Problem-method alignment | Good — conservatism problem → on-policy solution | Same, but stated more sharply |
| (b) Variable alignment | Core concepts (on-policy, ensemble, AM-Q) appear in method | Same, with tighter intro-to-method transition |
| (c) Contribution-evidence alignment | Overstated ("eclipsing," "gets rid of") | Bounded to match available evidence |

## Priority Revision Plan
### Ranked Error Board

| Rank | Issue | Severity | Validity Risk | Fixability | Confidence | Priority |
|------|-------|----------|---------------|------------|------------|----------|
| 1 | Unsupported monotonic improvement claim (Conclusion) | Critical | High — could invalidate key claim | Easy — remove/qualify wording | High | P0 |
| 2 | Overstated contribution claims (Intro/Abstract) | Major | Medium — overclaim undermines credibility | Easy — hedge wording | High | P0 |
| 3 | OPE 22% ranking error not discussed (Section 5.3) | Major | Medium — affects trust in multi-step improvement | Medium — add analysis paragraph | High | P0 |
| 4 | Missing limitations section | Major | Low — does not affect validity but reduces credibility | Easy — add paragraph | High | P0 |
| 5 | Mathematical inflation (Proposition 1, Theorem 1) | Major | Low — does not affect validity but misrepresents contribution | Easy — rename | High | P1 |
| 6 | Related Work unstructured (Section 4) | Major | Low — readability issue | Medium — reorganize | High | P1 |
| 7 | Ensemble BC max function non-differentiability (Section 3.1) | Major | Low — implementation detail | Medium — add explanation | Medium | P1 |
| 8 | Real-world experiment rigor (Figure 5) | Major | Low — presentation issue | Easy — add labels, clarify metrics | Medium | P2 |

### Revision Order

**Phase 1 (P0 — Must fix before resubmission):**
1. Remove "monotonically" and "eclipsing" wording from Conclusion and Introduction
2. Hedge Abstract SOTA claims to "competitive or superior on evaluated benchmarks"
3. Add limitations paragraph at end of Conclusion
4. Add discussion of 22% OPE ranking error rate and its implications

**Phase 2 (P1 — Should fix for stronger paper):**
5. Rename Proposition 1 → Definition, Theorem 1 → Lemma/Remark
6. Reorganize Related Work around comparison axes (see Actionable Suggestions S4)
7. Add implementation details for ensemble BC max function optimization

**Phase 3 (P2 — Nice to have):**
8. Improve Figure 5 axis labels and metric definitions
9. Add oracle OPE comparison to demonstrate graceful degradation under errors
10. Extend cQ_τ vs Q^{π_k} ablation to more dataset types

### Expected Impact

- Fixing P0 items would address the most validity-critical concerns and likely move the paper from "borderline accept" to "clear accept" by removing overclaims that provoke reviewer resistance.
- Fixing P1 items would substantially improve presentation quality and make the novelty positioning clearer.
- Fixing P2 items would strengthen the empirical evaluation but are not required for publication.

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|--------|---------------------|-------|---------|-------------|----------------|-------------------|
| E1 | Offline performance (Table 1) | D4RL Gym/Adroit/Kitchen, 10 eval trajectories, 5 seeds | Normalized return | Uni-O4 achieves best total (1322.0) across 20 tasks | "Competitive offline performance" | Some tasks (halfcheetah-medium: 52.6 vs ATAC 54.3) not best |
| E2 | Antmaze evaluation (Table 2) | D4RL Antmaze 6 tasks | Normalized return (50 trials) | Best total (447.9), 79.4% improvement over BC | "Effective on sparse-reward multi-task" | High variance on diverse tasks (e.g., 83.5±11.1) |
| E3 | Online fine-tuning (Figs 3-4) | 1M environment steps, all methods | Learning curves | Faster convergence, higher asymptotic | "Stable and rapid fine-tuning" | Results are comparative, no statistical significance tests |
| E4 | Real-world robot (Fig 5) | Unitree Go1 on latex mattress | Average return, speed (m/s) | Robot adapts to deformable terrain | "Practical utility for sim-to-real" | Only one terrain; baseline comparison not apples-to-apples |
| E5 | OPE accuracy (Fig 6a) | All MuJoCo tasks, online vs OPE ranking | Accuracy at error thresholds | 78% exact, 95% within 20% error | "Reliable OPE for multi-step improvement" | 22% ranking error rate not discussed |
| E6 | Alpha ablation (Fig 6b) | All MuJoCo tasks | Normalized return during offline opt | α=0.1 > α=0.0 > α=0.5 | "Minor disagreement penalty helps" | Only 3 values tested |
| E7 | Ensemble size (Fig 6c) | All MuJoCo tasks | Final normalized return | n=4 (90.62) ≈ n=8 (90.72) > n=1 (86.85) | "n=4 good trade-off" | Performance gain from 4→8 is marginal |
| E8 | Optimality analysis (Fig 6d) | MuJoCo, Uni-O4 vs PPO from scratch | Normalized scores | Uni-O4 fine-tuning faster and higher than training PPO from scratch | "Better fine-tuning than training from scratch" | Comparison only to scratch PPO, not other fine-tuning methods |
| E9 | cQ_τ vs Q^{π_k} (Fig 20, Appendix) | 3 medium-replay datasets | Normalized return curves | cQ_τ outperforms iterative Q-fitting | "cQ_τ is better choice" | Only 3 datasets; medium-expert not tested |
| E10 | Design choices ablation (Figs 21-24, Appendix) | Walker2d tasks, with/without design choices | Learning curves | State norm, reward scaling, Tanh helpful; value clip minor | "PPO code-level optimizations help" | Only on Walker2d |

### Research-Theme Gap Diagnosis

1. **New knowledge gap:** The paper's primary claim — that on-policy objectives can unify offline and online RL — is conceptually novel. However, the theoretical support is weak (loose bounds, trivial propositions), and the novelty positioning could be clearer with better related-work organization.

2. **Reproducibility gap:** Algorithm steps are described in pseudocode (Algorithm 2, Appendix), and hyperparameters are reported (Table 5). However, the ensemble BC max-function optimization is not fully specified (non-differentiability unaddressed), and some baselines use external implementations, which may introduce uncontrolled variability.

3. **Impact on practice/understanding gap:** The real-world robot demonstration is the strongest evidence for impact, but limited to one terrain type and one robot platform. The computational efficiency advantage (30 min vs 18 hours for Off2on) is practically significant but needs clearer phase-by-phase breakdown.

### Proposed Research Experiments (P0/P1/P2)

**E11 (P0) — OPE error impact analysis:**
- **Target Claim:** "AM-Q enables safe multi-step policy improvement"
- **Hypothesis:** The 22% OPE ranking error rate does not catastrophically affect final performance because errors are not correlated across steps.
- **Minimal Design:** Compare final fine-tuning performance under three conditions: (a) AM-Q-based selection (current), (b) oracle selection using ground-truth online evaluation, (c) random selection (no OPE).
- **Controls/Baselines:** Same offline initialization for all three conditions.
- **Metrics:** Final normalized return, learning curve area under curve.
- **Success Criterion:** AM-Q performance is closer to oracle than to random.
- **Estimated Cost/Time:** Low — reuses existing trained policies; requires only additional evaluation runs (~2 GPU hours).
- **Expected Quality Gain:** High — would validate OPE reliability or reveal degradation.

**E12 (P1) — Broader Q^{π_k} vs cQ_τ ablation:**
- **Target Claim:** "cQ_τ is a favorable choice over iterative Q^{π_k}"
- **Hypothesis:** cQ_τ outperforms Q^{π_k} more significantly on tasks with narrow dataset coverage (medium, medium-replay) than on expert datasets.
- **Minimal Design:** Extend Figure 20 to include medium-expert and expert datasets for all 3 locomotion tasks.
- **Controls/Baselines:** Fixed seed, same number of total gradient steps.
- **Metrics:** Final normalized return after offline optimization.
- **Success Criterion:** cQ_τ is at least as good as the best Q^{π_k} variant on all dataset types.
- **Estimated Cost/Time:** Low — runs existing training pipeline on a few additional datasets (~4 GPU hours).
- **Expected Quality Gain:** Medium — strengthens a key design choice claim.

**E13 (P1) — Max vs Mean aggregation ablation:**
- **Target Claim:** "max is a good choice for f({π^j_β})"
- **Hypothesis:** Max aggregation produces more diverse policies than mean aggregation, leading to better state-action coverage.
- **Minimal Design:** Run ensemble BC with: (a) max aggregation (current), (b) mean aggregation, (c) geometric mean aggregation. Compare diversity metrics (average pairwise KL) and final offline performance.
- **Controls/Baselines:** Same ensemble size (n=4), same α, same offline optimization.
- **Metrics:** Average pairwise KL divergence between ensemble policies, final normalized return.
- **Success Criterion:** Max aggregation achieves higher diversity score and/or final performance than alternatives.
- **Estimated Cost/Time:** Low — modifies only the aggregation function in Equation 6 (~2 GPU hours).
- **Expected Quality Gain:** Medium — justifies a design choice currently lacking theoretical support.

**E14 (P2) — Real-world evaluation on additional terrains:**
- **Target Claim:** "Uni-O4 excels in real-world experiments"
- **Hypothesis:** The online-offline-online pipeline generalizes to other challenging terrains (sand, gravel, slopes).
- **Minimal Design:** Repeat the real-world experiment on 2-3 additional terrain types with the same robot platform.
- **Controls/Baselines:** Same pretrained policy, same fine-tuning protocol.
- **Metrics:** Average return, maximum stable speed, number of falls per episode.
- **Success Criterion:** Consistent improvement over the pretrained baseline across all terrains.
- **Estimated Cost/Time:** High — requires real-robot experimentation (~2-3 weeks).
- **Expected Quality Gain:** High — transforms real-world demonstration from proof-of-concept to generalizable result.

```text
ASCII Diagram — Experiment Upgrade Plan

E11 (P0) ─────────────────────────────────────────────
  OPE Error Impact Analysis
  [Hypothesis: errors don't compound]
  └─ Compare: AM-Q vs Oracle vs Random selection
  └─ Expected: AM-Q closer to Oracle
  └─ Cost: ~2 GPU hours

E12 (P1) ─────────────────────────────────────────────
  Broader cQ_τ vs Q^{π_k} Ablation
  [Extend to medium-expert/expert datasets]
  └─ Strengthen design choice claim
  └─ Cost: ~4 GPU hours

E13 (P1) ─────────────────────────────────────────────
  Max vs Mean Aggregation Ablation
  [Test diversity metrics + final performance]
  └─ Justify f = max design choice
  └─ Cost: ~2 GPU hours

E14 (P2) ─────────────────────────────────────────────
  Real-world Evaluation on Additional Terrains
  [Sand, gravel, slopes — same robot platform]
  └─ Generalize real-world claim
  └─ Cost: ~2-3 weeks (real-robot)
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score: 7/10**

Rationale: The paper presents a conceptually clean and well-motivated approach to a recognized problem in offline-to-online RL. The empirical evaluation is comprehensive and the real-world demonstration is compelling. However, the score is constrained by: (1) overstated novelty and contribution claims that are not fully supported by the evidence; (2) relatively weak theoretical contributions (Proposition 1 and Theorem 1 are simple inequalities presented as substantive results); (3) the OPE evaluation has a 22% ranking error rate whose impact is not discussed; and (4) the absence of a limitations section reduces scientific completeness. The paper's strength lies in its empirical results and practical demonstration rather than theoretical novelty.

**Post-Revision Target: [7.5, 8.5]/10**

If the authors address the P0 items (bound claims, remove monotonicity overstatement, add limitations discussion, discuss OPE error impact) and restructure the Related Work section, the paper could reach 7.5-8.5/10. Further strengthening with additional OPE error analysis and broader real-world evaluation could push it toward the upper end of this range.