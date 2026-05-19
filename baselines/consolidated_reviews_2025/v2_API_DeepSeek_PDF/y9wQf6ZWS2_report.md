## Summary
# Final Review Report

## Summary

This paper proposes RegQ, a regularized Q-learning algorithm designed to achieve provable convergence under linear function approximation — a setting where standard Q-learning is known to diverge due to the deadly triad. The core idea is remarkably simple: adding an L2 regularization term (ηθ_k) to the Q-learning update. The authors establish convergence via the Borkar-Meyn O.D.E. framework combined with a switching system analysis, constructing upper and lower comparison systems whose global asymptotic stability implies convergence of the original stochastic algorithm. An error bound characterizing the bias introduced by regularization is also derived. Experiments on two small-scale divergence-prone environments (θ→2θ and Baird's counterexample) demonstrate that RegQ converges faster than two time-scale baselines (CQL and Greedy-GQ).

**Strengths**: The algorithmic idea is clean and theoretically motivated. The convergence proof strategy (regularization → negative definiteness → common Lyapunov function → Borkar-Meyn theorem) is logically coherent and technically sound. The single time-scale nature is a genuine practical advantage over two time-scale alternatives.

**Weaknesses**: The theoretical analysis relies on strong assumptions (Assumption 2.2: orthogonal, non-negative feature columns) that limit practical applicability. The experimental validation is restricted to two toy problems and lacks statistical rigor (no variance reporting in main learning curves, narrow baseline comparison). The bias-inducing regularization creates an inherent accuracy-stability trade-off that is not adequately discussed. Novelty claims cannot be independently verified in this run (external paper search unavailable), but the core idea of adding regularization for convergence in off-policy TD has precedent in prior work on TD-learning [Diddigi et al., 2019].

## Strengths
1. **Simple and elegant algorithmic idea**: The core contribution — adding an L2 regularization term to the Q-learning update to ensure convergence — is conceptually straightforward. This simplicity is a genuine strength because it makes the method easy to understand, implement, and potentially extend. The update rule (Eq. 11) adds only one line of code to standard Q-learning with linear function approximation.

2. **Sound theoretical framework**: The convergence proof strategy is well-motivated and technically rigorous. By showing that the regularized update renders the switching system matrices negative definite, the authors establish a common quadratic Lyapunov function, which then enables the Borkar-Meyn theorem to guarantee almost-sure convergence. The construction of upper and lower comparison systems via the vector comparison principle is a clever way to handle the affine term in the shifted O.D.E.

3. **Single time-scale advantage**: Unlike several prior convergent Q-learning methods (CQL [Carvalho et al., 2020], Greedy-GQ [Maei et al., 2010], target-network-based methods [Zhang et al., 2021]) that require two learning rates, RegQ operates at a single time scale. This simplifies hyperparameter tuning and, as the experiments suggest, can lead to faster convergence in practice.

4. **Error bound characterization**: Lemma 3.2 explicitly quantifies the bias introduced by regularization, decomposing it into a regularization-induced term and a projection-induced term. This provides theoretical transparency about the accuracy-stability trade-off, which is important for practitioners deciding whether the convergence guarantee is worth the bias.

5. **Transparent limitations**: The paper clearly states the assumptions (Assumptions 2.1-2.3) and the condition on η (Eq. 13) needed for convergence. While these assumptions are restrictive (see Weaknesses), their explicit statement allows readers to assess applicability.

## Weaknesses
The weaknesses are organized from most impactful to least impactful.

1. **Restrictive feature assumptions limit practical applicability (Major)**: Assumption 2.2 requires the feature matrix X to have full column rank, be non-negative, and have orthogonal columns. Column orthogonality is particularly restrictive — most practical feature constructions (tile coding, radial basis functions, Fourier basis, learned representations) do not satisfy this condition. Since the convergence proof critically relies on this assumption (used to establish diagonal properties of X^T DX in the switching system analysis), the theoretical guarantees do not extend to commonly used feature representations. The paper claims these assumptions are "commonly adopted in the literature," but this does not reduce their restrictiveness. A practical algorithm that demands orthogonal features is not substantially more useful than prior methods with strong assumptions.

2. **Experimental validation is inadequate for the claimed contributions (Major)**: The empirical evaluation has four significant shortcomings:
   - **Toy-scale only**: The two main experiments (θ→2θ with 2 states, Baird's with 7 states) are minimal testbeds designed specifically to cause divergence. While demonstrating convergence on these is necessary, it is far from sufficient.
   - **Narrow baselines**: Only two two time-scale methods (CQL, Greedy-GQ) plus a target-network variant are compared. Missing comparisons include Zap Q-learning, target network + truncation [Chen et al., 2022], and other recent convergent approaches.
   - **No variance/confidence intervals on main learning curves**: Figures 1a and 1b show only mean trajectories without error bands, despite claiming averages over 50 runs.
   - **Claim (3) "faster convergence" is not statistically substantiated**: Without error bars or significance tests, the visual impression of faster convergence cannot be assessed rigorously.

3. **Inherent bias-stability trade-off is under-analyzed (Major)**: The regularization term ηθ_k ensures convergence but introduces bias. Lemma 3.2 provides an error bound that grows with η in the first term and decreases with η in the second term, creating a complex trade-off. However, the paper provides no practical guidance on selecting η, no ablation study comparing different η values in the main text, and no discussion of whether η can be annealed during training to reduce bias while maintaining stability. The claim "If η = 0 satisfies (13), we can guarantee convergence to an optimal policy without errors" is theoretically true but practically vacuous — condition (13) with η=0 is unlikely to hold in most MDPs because it requires λ_max(C) * max_{π,s,a} [γd^T P^π(e_a ⊗ e_s)/(2d(s,a)) - (2-γ)/2] < 0.

4. **Unclear novelty relative to prior regularized TD-learning (Moderate)**: The paper's key inspiration is Diddigi et al. [2019], which adds L2 regularization to TD-learning for convergent off-policy evaluation. The extension to Q-learning is non-trivial due to the bootstrapping and policy dependence, but the paper does not clearly delineate which technical challenges are new to the control setting versus inherited from the evaluation setting. The switching system analysis heavily borrows from Lee and He [2019]'s framework.

5. **Writing and presentation issues (Minor)**: Several sections suffer from unclear narrative flow (see Storyline Options), the related work is organized as a paper list rather than by methodological themes, some technical claims are stated imprecisely (e.g., the Lyapunov argument in Section 2.5), and the conclusion adds unsupported future claims about deep RL extension.

## Key Issues
### Issue 1: Assumption 2.2 (orthogonal, non-negative features) — the gap between theory and practice
**Severity: Major | Fixability: Moderate**

The convergence proof depends on features being non-negative, full column rank, and orthogonal. The orthogonality condition is used in the quasi-monotonicity proof (Appendix A.6, where X^T DX being diagonal is critical). This means RegQ's theoretical guarantees do not apply to most practical feature representations. The paper should either relax this assumption (e.g., to bounded condition number plus diagonal dominance of X^T DX) or explicitly position the work as theoretical with acknowledgment that practical features require additional verification.

**Required action**: Add a section discussing which parts of the proof break when features are not orthogonal, and whether empirical convergence can still be observed for non-orthogonal features (e.g., add a synthetic experiment with non-orthogonal features that still converges).

### Issue 2: Experimental validation insufficient to support "faster convergence" claim
**Severity: Major | Fixability: High**

Contribution (3) claims "faster convergence than other two time-scale Q-learning algorithms," but the evidence is limited to two toy problems, with no variance reporting and only two baselines. A reviewer could reasonably challenge that the claim is overstated relative to the evidence.

**Required action**: (a) Add at least one moderate-scale control problem with linear FA (e.g., an extended version of Mountain Car or a simple linear MDP). (b) Report error bars (std or 95% CI) on all learning curves. (c) Add at least one more recent baseline. (d) Temper the claim to "competitive convergence on divergence-prone examples" unless stronger evidence is provided.

### Issue 3: Lack of practical guidance on η selection
**Severity: Major | Fixability: High**

The regularization coefficient η determines both stability (larger η ensures condition (13)) and accuracy (larger η increases bias). The paper provides no practical guidance on selecting η, no cross-validation procedure, no theoretical optimal η, and no discussion of annealing. The only mention is "Overall, we can see that the convergence rate gets faster as η increases" in the appendix — which actually conflicts with the bias issue.

**Required action**: (a) Add a dedicated subsection on η selection with practical recommendations. (b) Provide an ablation study showing the effect of η on both convergence speed and final solution quality. (c) Discuss whether η can be annealed toward zero during training.

### Issue 4: Circular presentation of existence assumptions in convergence proof
**Severity: Minor | Fixability: High**

The convergence analysis (Section 5) assumes existence of the equilibrium point (Theorem 5.1(c)), which is later guaranteed by Lemma 3.1 under a different η condition. The relationship between the two η conditions (Lemma 3.1's η > X^2_max sqrt(|S||A|) - λ_min(C) vs. Eq. (13)'s condition) is not discussed. Are they equivalent? Does one imply the other?

**Required action**: Clarify the logical dependency: Lemma 3.1 provides existence under one condition; the negative definiteness condition (13) is then used for stability. If both conditions must simultaneously hold, state this explicitly and discuss whether this overconstrains η.

### Issue 5: Unmotivated deep RL future work statement
**Severity: Minor | Fixability: High**

The conclusion speculates about extending to deep RL "without using the target network." Since the theory relies on linear FA assumptions (orthogonal features, etc.), there is no evidence that the regularization approach would work with neural networks. This statement creates a misleading impression of the paper's scope.

**Required action**: Replace with a more measured statement: "An open challenge is whether similar regularization mechanisms can be effective in nonlinear function approximation settings, though this would require new theoretical tools beyond the linear switching system framework."

## Actionable Suggestions
### Suggestion 1 (Must): Address restrictive feature assumptions

**Problem**: Assumption 2.2 (orthogonal, non-negative columns) is too restrictive for practical adoption.

**Action**: 
- Add a new experiment where RegQ is tested with non-orthogonal features (e.g., randomly generated features or features with controlled condition number) to demonstrate empirical convergence even when Assumption 2.2 is violated.
- Discuss which parts of the convergence proof critically rely on orthogonality versus which can be relaxed. 
- If orthogonality can be relaxed to "X^T DX is diagonally dominant," state this explicitly.
- Add a paragraph in the conclusion acknowledging this limitation.

**Expected benefit**: Significantly increases the practical relevance of the paper and provides guidance for practitioners.

### Suggestion 2 (Must): Strengthen experimental validation

**Problem**: Current experiments are on toy problems only, and key learning curves lack variance information.

**Action**:
- Add a moderate-scale control experiment (e.g., a larger random MDP with linear FA or the full version of Mountain Car with meaningful tiling).
- Report standard deviation or 95% confidence intervals as shaded regions on all learning curves (Figures 1 and 4).
- Add at least one additional convergent Q-learning baseline (e.g., target network + truncation [Chen et al., 2022] or Zap Q-learning [Devraj and Meyn, 2017]).
- Run a statistical significance test (e.g., paired t-test at final iteration) between RegQ and each baseline.

**Expected benefit**: Makes contribution (3) ("faster convergence") defensible and addresses reproducibility concerns.

### Suggestion 3 (Must): Provide η selection guidelines

**Problem**: No practical guidance on choosing the regularization coefficient η.

**Action**:
- Add a subsection "Practical Selection of η" with: (a) a cross-validation procedure using a validation set, (b) a discussion of the η that satisfies both Lemma 3.1 and Eq. (13), (c) an ablation study showing convergence behavior and final error for η ∈ {0.01, 0.1, 1, 2, 5, 10} on at least one benchmark.
- Consider adding an η-annealing schedule: start with large η for stability, decay to zero for reduced bias.
- Provide a heuristic default η (e.g., η = λ_max(C)/2 or η = 1) based on empirical observations.

**Expected benefit**: Makes the algorithm practically usable and demonstrates the bias-stability trade-off empirically.

### Suggestion 4 (Nice-to-have): Restructure related work

**Problem**: Related work reads as a paper-by-paper list rather than a thematic comparison.

**Action**: Reorganize into methodological categories:
1. Strong-assumption convergence proofs (Melo et al., Lee and He, Yang and Wang)
2. Target-network-based methods (Zhang et al., Carvalho et al., Agarwal et al., Chen et al.)
3. Gradient-based and optimization methods (Maei et al., Ghiassian et al.)
4. Sampling and re-weighting methods (Sutton et al., 2016)
5. Other approaches (linear programming, Zap Q-learning, optimistic design)

For each category, state the common approach, key limitations, and how RegQ differs.

**Expected benefit**: Readers can quickly understand where RegQ fits in the literature.

### Suggestion 5 (Nice-to-have): Improve convergence proof presentation

**Problem**: The logical flow between Lemma 3.1 (existence), condition (13) (negative definiteness), and Theorem 5.1 (GAS) is hard to follow.

**Action**: Add a proof roadmap before Eq. (14):
"Step 1: Lemma 3.1 guarantees a unique solution θ_e to (9) when η is sufficiently large. Step 2: Condition (13) ensures -A_{πXθ} - ηI is negative definite for all policies, enabling a common Lyapunov function. Step 3: The upper and lower comparison systems (constructed using the vector comparison principle from Lemma A.8) bound the original system trajectory. Step 4: Theorem 5.1 establishes global asymptotic stability of the shifted O.D.E. Step 5: Theorem 5.2 invokes the Borkar-Meyn theorem for almost-sure convergence."

**Expected benefit**: Makes the proof strategy accessible to readers less familiar with switching system theory.

### Suggestion 6 (Nice-to-have): Bound and clarify the conclusion

**Problem**: The conclusion speculates about deep RL without justification.

**Action**: Replace the final two sentences with a concise summary of validated findings and bounded limitations. See the annotation on Page 9 - Conclusion for a concrete rewrite.

**Expected benefit**: Improves scientific credibility by matching claims to evidence.

## Storyline Options + Writing Outlines
### Current Storyline Analysis

The current introduction follows this structure:
1. P1: Deep RL success → deadly triad problem
2. P2: TD-learning solutions to deadly triad (survey)
3. P3: Q-learning's convergence difficulty under strong assumptions
4. P4: Main goal + contribution list
5. P5-6: Related work (paper-by-paper survey)

**Problem**: The first paragraph is unfocused (too much space on Atari benchmarks tangentially related to linear FA). The gap (Q-learning divergence under linear FA) appears late, after a long TD-learning survey. The reader must wait until paragraph 4 to understand why regularization helps.

### Chosen Storyline Revision

**Storyline**: Deadly Triad Problem → Prior attempts are too restrictive or complex → A simple fix: regularization → Theoretical guarantee → Empirical validation

This follows a **Problem → Gap → Solution → Evidence** arc with tighter alignment:
- Problem alignment (✓): The deadly triad directly motivates the need for convergence guarantees
- Variable alignment (✓): The key variable η (regularization weight) appears early and is central to all subsequent analysis
- Evidence alignment (✓): Abstract and intro claims are directly testable in experiments

### Abstract Outline (Complete)

**S1 (Problem + Domain)**: "Q-learning with linear function approximation is known to diverge due to the deadly triad — the combination of off-policy learning, function approximation, and bootstrapping."

**S2 (Prior Limitation)**: "Existing convergent variants either rely on strong assumptions about the feature representation or MDP structure, or require two time-scale updates that complicate practical deployment."

**S3 (Proposed Method)**: "This paper introduces RegQ, a single time-scale Q-learning algorithm that achieves provable convergence under linear function approximation by adding an L2 regularization term to the parameter update."

**S4 (Theory)**: "Using an ordinary differential equation analysis combined with a switching system framework, we prove global asymptotic stability when the regularization coefficient η satisfies a verifiable condition, and derive an error bound quantifying the bias-regularization trade-off."

**S5 (Empirical Result)**: "Experiments on two established divergence-prone benchmarks confirm that RegQ converges reliably and competitively with state-of-the-art convergent Q-learning methods."

### Introduction Outline (Complete)

**P1 (The Deadly Triad Challenge)**: State the problem directly: Q-learning diverges when off-policy sampling, function approximation, and bootstrapping are combined. Cite Baird [1995] and Tsitsiklis and Van Roy [1997]. Motivate why linear FA is a natural starting point for theoretical analysis.

*Transition*: "Despite significant progress in stabilizing TD-learning for policy evaluation, the control setting — Q-learning — has proven more resistant to analysis."

**P2 (Prior Work on Convergent Q-learning)**: Survey existing approaches organized by strategy: (a) strong-assumption methods (Melo et al., Lee and He, Yang and Wang), (b) target-network methods (Zhang et al., Carvalho et al., Agarwal et al., Chen et al.), (c) gradient-based methods (Maei et al., Greedy-GQ), (d) other approaches. For each, state the key limitation that motivates RegQ.

*Transition*: "A common thread is that prior methods either require strong assumptions or introduce additional complexity (two time-scale learning, target networks, projection steps). This raises the question: can a simpler modification — pure regularization — achieve convergence without these complications?"

**P3 (Regularization Intuition)**: Explain conceptually why adding L2 regularization to the Q-learning update can prevent divergence: the regularization term (ηθ_k) pulls parameters toward zero, preventing the unbounded growth that causes divergence in the standard algorithm. This is analogous to how L2 regularization stabilizes TD-learning [Diddigi et al., 2019].

*Transition*: "Building on this intuition, we formally prove that the regularized algorithm converges and characterize its solution."

**P4 (Contributions)**: List the three contributions:
1. A new single time-scale regularized Q-learning algorithm (RegQ)
2. Convergence proof via O.D.E. + switching system with upper/lower comparison systems, plus error bound
3. Experimental validation on divergence-prone benchmarks with competitive performance

**P5 (Paper Organization)**: Optional brief roadmap sentence.

### Comparison Checklist

| Alignment Check | Current | Revised |
|---|---|---|
| Problem alignment | Weak (buried after RL success stories) | Strong (deadly triad stated prominently) |
| Variable alignment | Moderate (η appears in Section 4) | Strong (regularization introduced early) |
| Evidence alignment | Moderate (claims match experiments but limited) | Strong (bounded claims with explicit evidence mapping) |

## Priority Revision Plan
The following revision items are ordered by priority (P0 = publication-critical, P1 = important, P2 = quality improvement).

### P0 Items (Must Fix Before Resubmission)

**P0.1: Address restrictive feature assumptions**
- **What**: Relax Assumption 2.2 or add empirical demonstration with non-orthogonal features
- **Where**: Section 2.3 (assumptions) + Experiments (new experiment) + Conclusion (limitation)
- **Effort**: Medium (new experiment + text revisions)
- **Impact**: High — directly determines practical relevance of theoretical guarantees

**P0.2: Strengthen experimental validation**
- **What**: (a) Add standard deviation/CI to all learning curves, (b) add at least one moderate-scale experiment, (c) add at least one more baseline, (d) temper "fastest convergence" claim
- **Where**: Section 6 + Appendix A.8
- **Effort**: Medium-High (requires new experimental runs)
- **Impact**: High — claim (3) cannot be defended without stronger evidence

**P0.3: Provide η selection guidance**
- **What**: Add a practical recommendation for choosing η, with ablation study showing effect on convergence and accuracy
- **Where**: New subsection in Section 4 or 6
- **Effort**: Low-Medium (analysis of existing data + a few additional runs)
- **Impact**: High — makes the algorithm practically usable

### P1 Items (Important Improvements)

**P1.1: Clarify convergence proof flow**
- **What**: Add a proof roadmap showing the logical dependency between Lemma 3.1, condition (13), and Theorem 5.1/5.2
- **Where**: Section 5 (Convergence Analysis)
- **Effort**: Low (text revision only)
- **Impact**: Medium — significantly improves readability for reviewers

**P1.2: Restructure related work**
- **What**: Organize by methodological categories rather than paper-by-paper listing
- **Where**: Section 1 (Related Works paragraph)
- **Effort**: Low (reorganization + new sentences)
- **Impact**: Medium — helps readers understand RegQ's positioning

**P1.3: Rewrite conclusion**
- **What**: Remove unsupported deep RL speculation; add explicit limitations (feature assumptions, bias, experiment scope)
- **Where**: Section 7
- **Effort**: Low (text revision)
- **Impact**: Medium — improves scientific credibility

### P2 Items (Quality-of-Execution Improvements)

**P2.1: Improve abstract narrative flow**
- **What**: Restructure into problem-gap-solution-result format
- **Where**: Abstract
- **Effort**: Low
- **Impact**: Low-Medium — improves first impression

**P2.2: Add notation clarity**
- **What**: Clarify P, Ππ, and P^π relationship; explain D matrix structure
- **Where**: Section 2.2
- **Effort**: Low
- **Impact**: Low — aids reproducibility

**P2.3: Expand O.D.E. experiment**
- **What**: Verify stochastic algorithm convergence matches deterministic fixed point; add comparison with unregularized Q-learning
- **Where**: Section 6.3
- **Effort**: Low-Medium
- **Impact**: Low — illustrative value only

## Experiment Inventory & Research Experiment Plan
### Completed Experiment Inventory

| Exp ID | Objective/Hypothesis | Setup | Metrics | Main Outcome | Claim Supported | Current Limitation |
|---|---|---|---|---|---|---|
| E1: θ→2θ (Sec 6.1) | RegQ converges in 2-state problem where Q-learning diverges | 2 states, 1 feature, zero reward, deterministic transition | θ value over iterations | RegQ converges faster than CQL, Greedy-GQ, Q-target | C3 (faster convergence) | Toy problem; only 1 feature; no variance shown in Figure 1a |
| E2: Baird 7-star (Sec 6.2) | RegQ converges in overparameterized 7-state problem | 7 states, 2 actions, 15 features, off-policy sampling | θ value over iterations | RegQ converges faster than CQL, Greedy-GQ, Q-target | C3 (faster convergence) | Toy problem; no variance shown in Figure 1b |
| E3: O.D.E. experiment (Sec 6.3) | Illustrate upper/lower system bounding property | |S|=2, |A|=2, uniform sampling, uniform reward | θ1-θe1, θ2-θe2 over time | Trajectory bounded by comparison systems | C2 (switching system theory) | Only visual illustration; no quantitative metrics |
| E4: Hyperparameter sensitivity (Fig 4, Appendix A.8.2) | Effect of learning rate and η on convergence | Same as E1/E2 with varying α and η | Convergence speed | Faster convergence with larger η | C3 | Only 2 learning rates tested; no effect on final solution accuracy |
| E5: Mountain Car (Table 1, Appendix A.8.3) | RegQ performs comparably to Q-learning when Q-learning converges | Tile-coded continuous state, 1000 train episodes, 100 test runs | Episode reward (mean±std) | RegQ comparable to Q-learning at optimal η | C1 (algorithm works) | Q-learning already converges here; RegQ offers no advantage |

### Research-Theme Gap Diagnosis

| Research Value Claim | Supported Evidence | Weakness |
|---|---|---|
| New knowledge: provable convergence for linear FA Q-learning | Theoretical proof provided | Relies on strict Assumption 2.2; η conditions may be hard to verify |
| Practical usefulness: algorithm is simple and implementable | Single-line update rule | No practical η selection guidance; convergence not tested on practical-scale problems |
| Reproducibility: algorithm can be reproduced from text | Update rule clearly stated; pseudocode in appendix | Missing hyperparameter sensitivity analysis; no code or data provided |
| Potential to change practice: could replace target networks | Theory avoids target networks | No deep RL experiments; feature assumptions incompatible with neural nets |

### Proposed Research Experiments

**P0.1: Non-orthogonal feature validation**
- **Target Claim**: C2 (convergence proof)
- **Hypothesis**: RegQ converges even with non-orthogonal features that violate Assumption 2.2
- **Minimal Design**: Generate random feature matrices with controlled condition numbers (1, 5, 10, 50) on the Baird 7-star problem; run RegQ and report convergence
- **Controls/Baselines**: Same experiment with orthogonal features (baseline condition)
- **Metrics**: Convergence proportion (fraction of runs that converge) and convergence speed
- **Success Criterion**: RegQ converges with condition number up to 10 with >90% probability
- **Estimated Cost**: Low (simulation, ~2 hours)
- **Expected Quality Gain**: High — addresses the most critical theoretical limitation

**P0.2: Moderate-scale benchmark validation**
- **Target Claim**: C3 (practical convergence)
- **Hypothesis**: RegQ converges on a larger linear MDP problem
- **Minimal Design**: Use a randomly generated MDP with |S|=50, |A|=5, h=20 features; compare RegQ vs standard Q-learning (expected to diverge) vs CQL
- **Controls/Baselines**: Standard Q-learning, CQL, Greedy-GQ
- **Metrics**: RMS Bellman error over training, variance over 10 seeds
- **Success Criterion**: RegQ converges while standard Q-learning diverges; RegQ matches or exceeds CQL convergence speed
- **Estimated Cost**: Low-Medium (~1 day including analysis)
- **Expected Quality Gain**: High — directly addresses the "toy problem only" criticism

**P0.3: η ablation study**
- **Target Claim**: C1, C3
- **Hypothesis**: There exists a range of η that balances convergence stability and solution accuracy
- **Minimal Design**: On Baird 7-star and Mountain Car, sweep η ∈ {0.01, 0.1, 0.5, 1, 2, 5, 10}; report both convergence speed and final θ error relative to optimal Q*
- **Controls/Baselines**: η=0 (standard Q-learning)
- **Metrics**: Convergence time, final ||Xθ - Q*|| error, number of divergent runs
- **Success Criterion**: Identify η range where RegQ converges and bias is within acceptable range (e.g., <10% of optimal value range)
- **Estimated Cost**: Low (~4 hours simulation)
- **Expected Quality Gain**: High — provides practical η selection guidance

**P1.1: Variance reporting on existing experiments**
- **Target Claim**: C3
- **Hypothesis**: RegQ has lower variance than two time-scale methods
- **Minimal Design**: Re-run existing experiments with 50 seeds; compute mean ± std at each timestep
- **Controls/Baselines**: Same as E1/E2
- **Metrics**: Mean ± std learning curves, area under curve, final convergence distribution
- **Success Criterion**: Statistically significant advantage over at least one baseline
- **Estimated Cost**: Low (re-analysis of existing runs)
- **Expected Quality Gain**: Medium — makes C3 defensible

### ASCII Diagram — Experiment Upgrade Plan

```text
P0.1: Non-orthogonal features
  [Current: Assumption 2.2 required]
  → Test RegQ with random features (cond# 1-50)
  → If converges → relax assumption; If not → characterize boundary
  → Expected: convergence up to moderate condition number

P0.2: Moderate-scale benchmark
  [Current: only |S|=2,7 toy problems]
  → |S|=50, |A|=5, h=20 random linear MDP
  → Compare: RegQ vs Q-learning vs CQL vs Greedy-GQ
  → Expected: RegQ converges where Q-learning diverges

P0.3: η ablation study
  [Current: no practical selection guidance]
  → Sweep η ∈ {0.01, 0.1, 0.5, 1, 2, 5, 10}
  → Report: convergence speed + final error
  → Expected: Pareto frontier for η selection

P1.1: Variance reporting
  [Current: Figure 1 missing error bands]
  → Re-run 50 seeds; compute mean±std curves
  → Add shaded confidence intervals to Figures 1a, 1b
```

## Novelty Verification & Related-Work Matrix
External literature search was not started in this run; novelty/comparison conclusions are deferred to manual verification.

## References
External literature search was not started in this run; no external references are listed.

## Scores
**Final Score**: 4.5 / 10

**Rationale**: The paper presents a clean algorithmic idea (RegQ) with a rigorous convergence proof rooted in switching system theory. The single time-scale property is a genuine practical advantage. However, the score is constrained by three major limitations:

1. **Restrictive assumptions (assumption cost)**: The convergence proof relies on features being orthogonal, non-negative, and full rank (Assumption 2.2). This substantially limits practical applicability and raises the question of whether the method is more useful than prior strong-assumption methods it claims to improve upon.

2. **Insufficient empirical validation**: The experiments are limited to two toy problems, lack variance reporting, and compare against only two baselines. The claim of "fastest convergence" is not statistically substantiated.

3. **Unresolved bias-stability trade-off**: The paper does not provide practical guidance on selecting the regularization coefficient η, nor does it characterize how the bias from regularization affects solution quality in realistic settings.

The research value is moderate: the theoretical framework (regularization → negative definiteness → common Lyapunov function → Borkar-Meyn convergence) is technically sound and could inspire further work, but the current empirical package does not convincingly demonstrate practical utility.

**Post-Revision Target**: [5.5, 6.5] / 10

**Conditions**: Achieving this post-revision score requires:
- P0.1: Empirical demonstration of convergence with non-orthogonal features (or theoretical relaxation of Assumption 2.2)
- P0.2: At least one moderate-scale experiment with proper variance reporting and additional baselines
- P0.3: Practical η selection guidance with supporting ablation study
- P1.3: Rewritten conclusion with explicit limitations

If all P0 and P1 items are addressed, the paper would present a theoretically grounded algorithm with credible empirical support, warranting a score in the 5.5-6.5 range. If the P0 items are only partially addressed, the target range would lower to [4.5, 5.5].