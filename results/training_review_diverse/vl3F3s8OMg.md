Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

This paper studies the role of Euclidean symmetry in model-based RL and planning. It defines "Geometric MDPs" and shows that their linearized dynamics satisfy G-steerable kernel constraints (Theorems 3–4), which theoretically reduce the number of free parameters in the dynamics and policy. Motivated by this theory, the authors propose an equivariant version of TD-MPC that enforces G-equivariance in the dynamics, reward, value, policy, and MPPI sampling procedure. Experiments on PointMass, Reacher, and MetaWorld Reach show 2×–3× sample efficiency gains over the non-equivariant baseline.

## Strengths

1. **Novel connection between steerable kernel theory and model-based RL.** The paper formally proves that linearized dynamics of Geometric MDPs satisfy G-steerable kernel constraints (Section 3.2). This connection — from continuous symmetry in MDPs through linearization to steerable kernels — is original and provides a principled basis for parameter reduction estimates (e.g., a 6×6 matrix reduced to 12 free parameters for 3D PointMass).

2. **Concrete equivariant model-based RL algorithm.** The paper extends equivariance from prior discrete-grid/value-based settings (Zhao et al., 2022b) and model-free settings (van der Pol et al., 2020b; Wang et al., 2021) to continuous state/action spaces with sampling-based planning (MPPI). The algorithm enforces explicit equivariance/invariance constraints on all components: encoder, dynamics, reward, value, policy, and the planning procedure.

3. **Clear empirical sample-efficiency gains.** Results on PointMass (2D and 3D variants), Reacher (easy/hard), and MetaWorld Reach consistently show that the equivariant version learns 2×–3× faster than the non-equivariant baseline (Figures 5, 6). On Reacher Hard, the D₈-equivariant variant shows a particularly clear margin. The 3D experiments with Icosahedral (order 60) and Octahedral (order 24) groups further validate the approach in higher dimensions.

4. **Explicit acknowledgment of scope limitations.** The paper candidly notes that locomotion tasks do not greatly benefit from Euclidean symmetry and that tasks with local coordinates/kinematic constraints are less suitable (Sections 3.2 and 6). This prevents overclaiming and provides useful guidance for practitioners.

## Weaknesses

### Fatal
None.

### Major

1. **Unquantified gap between continuous theory and discrete-subgroup implementation.** The theoretical results (Theorems 3–4, parameter reduction estimates) are derived for continuous group actions and assume infinitesimal symmetry transformations. The implementation, by contrast, uses finite discrete subgroups (D₄, D₈, C₈, Icosahedral, Octahedral) because they are "more stable and easier to implement" (line 214). The paper does not analyze how the theoretical guarantees (steerable kernel constraints, parameter reduction factors) transfer to these discrete approximations. For example, the 12-parameter count for 3D PointMass assumes continuous SO(3); the Icosahedral (order 60) group imposes strictly weaker constraints. The paper frames the experimental results as corroborating the continuous theory ("The results justify the theoretical estimation on improvement of sample efficiency," line 216), but the mapping is loose. This weakens the claimed connection between Theorem 3 and the empirical results. *Why it matters:* The paper's central narrative — that continuous symmetry yields the advertised reduction, validated by experiments — is partially undermined without quantifying the approximation.

2. **Equivariance of the sampling-based planner is only proven for a simplified special case (K=1), not for the practical multi-trajectory MPPI.** Proposition 5 proves equivariance of the G-augmented sampling procedure only "when K=1" — i.e., when selecting a single best trajectory at a single time step. The full MPPI procedure used in practice samples multiple H-horizon trajectories and selects actions via softmax-weighted combination over top-k trajectories. The paper does not analyze whether equivariance holds in this realistic setting, nor does it characterize the approximation error. Additionally, the G-augmented sampling strategy multiplies the action budget by |G| (e.g., 60× for Icosahedral), but the paper never reports wall-clock time or computational overhead. The assertion "computational costs increase" (line 227) is left unquantified. *Why it matters:* Without this analysis, it is unclear whether the empirical gains stem from the equivariant neural networks alone, or whether the equivariant planning loop contributes meaningfully. The practical overhead of G-augmented sampling may be prohibitive for larger groups.

### Minor

3. **Theoretical exposition in the main text is overly compressed.** The derivation from equivariant dynamics to G-steerable kernel constraints (Section 3.2) is presented in a few paragraphs. Key assumptions (e.g., that the linearization point p transforms consistently, that A(p) and B(p) depend on p smoothly enough to satisfy kernel constraints pointwise) are stated but not elaborated. Theorem 2 ("value iteration resembles equivariant message passing") is asserted in a single sentence without specifying the graph structure, message update, or sense of "resembles." While the appendix may contain details, the main text — which is what most readers evaluate — does not provide a self-contained argument. *Why it matters:* The theoretical motivation is a core contribution; the main-text exposition needs to be clear enough for a skeptical reader to follow the reasoning.

4. **Empirical evaluation would benefit from broader baselines and harder test cases.** The tasks are predominantly PointMass variants (where symmetry is almost perfectly preserved) and Reacher. MetaWorld Reach is the only non-toy task. The paper compares only against the non-equivariant version of the same algorithm. Comparisons to simpler symmetry-exploiting baselines (e.g., data augmentation with random rotations/reflections during training) would help isolate the benefit of explicit equivariant architectural constraints. A task with imperfect symmetry (e.g., PointMass with an obstacle) would test whether the method degrades gracefully. *Why it matters:* The paper's claimed practical significance would be strengthened by evidence that the method works beyond near-perfect-symmetry settings and that explicit equivariance outperforms simpler alternatives.

### Trivial

5. Figure 3 (schematic of steerable kernel constraints) lacks a fully explained caption and concrete worked example. The text references a "base space B = X/G" without defining X concretely.
6. Theorem 2 is stated without enough elaboration to be actionable — the connection between value iteration and geometric message passing is asserted but not explained.

## Nice-to-Haves

- A data-augmentation baseline (random rotations/reflections of transitions during training) would help isolate the benefit of explicit equivariant constraints from the benefit of seeing more symmetry-informed data.
- An experiment on a task with imperfect or broken symmetry (e.g., a PointMass with a fixed obstacle or non-uniform friction) would clarify the method's robustness and limits.
- Reporting wall-clock time per episode for the equivariant vs. baseline methods, especially for the Icosahedral (order 60) case, would help practitioners assess the practical cost.
- A brief intuitive explanation in the main text of why linearization yields steerable kernel constraints, with a concrete 2D example walking through the matrix structure.

## Removed Points

- **Reviewer Point 3 about "lack sufficient justification in the main text"**: Partially downgraded from Major to Minor. The derivation *is* present (lines 99–125) and the assumptions are stated. The paper references Lang & Weiler (2020a) for the explicit parameterization. The weakness is about compression/clarity, not missing content. Moved to Minor.
- **Criticism that "Definition 1's requirement of continuous group action conflicts with discrete subgroups"**: The paper explicitly states continuous action is "optional for implementation" (line 54) and that "properties do not require linearization and do not require continuous group actions" (line 87). The paper is transparent about this. Removed as partially addressed.
- **Missing proof sketches/appendix details**: The parser strips appendix content. The paper likely contains proofs in the appendix. Removed per instructions.
- **Request for "more challenging environments with distractors/partial observability"**: Scaled back — this would require a fundamentally different paper. Kept only the reasonable request for one task with broken symmetry.

## Novel Insights

The multi-review synthesis reveals a fundamental tension that the paper does not fully resolve: the theoretical machinery (steerable kernels, continuous Lie group actions) operates in a regime where symmetry is exact and infinitesimal, but the practical implementation relies on discrete subgroups whose approximation quality is uncharacterized. Neither the paper's theory section nor its experiments bridge this gap. This is a common pattern in equivariant deep learning applied to RL — the theory often assumes continuous symmetry while practice uses discrete approximations — but the paper would be strengthened by acknowledging and quantifying this discrepancy rather than presenting the experimental results as direct validation of the continuous theory.

## Suggestions

1. **Quantify the continuous-discrete gap.** Provide bounds or empirical measurements showing how well the discrete subgroups (D₄, D₈, Icosahedral) approximate the continuous steerable kernel constraints. Even ablating with progressively larger subgroups (C₄ → C₈ → C₁₆ → full SO(2) using continuous irreps) would give evidence on convergence.
2. **Analyze multi-trajectory MPPI equivariance.** Either prove that the full softmax-weighted multi-trajectory MPPI remains equivariant, or characterize the violation and explain why it is benign in practice. Report whether the G-augmented sampling is actually responsible for any of the observed gains via an ablation.
3. **Expand the main-text theoretical exposition.** Provide a brief but self-contained derivation in Section 3.2, a concrete matrix example, and at minimum one paragraph of intuition for each theorem (especially Theorem 2, which currently has none).
4. **Add at least one baseline comparison to data augmentation** to demonstrate the value of explicit equivariance over a simpler symmetry-exploiting method.

## Score and Decision

**Originality:** Good. The connection between steerable kernels and linearized dynamics of MDPs is novel.  
**Importance of question:** High. Sample efficiency in model-based RL is practically important.  
**Claims support:** Moderate. The experiments support the practical benefit, but the theory-experiment connection is weaker than claimed due to the continuous-discrete gap.  
**Soundness:** Moderate. The theoretical derivation is valid under stated assumptions; the experiments are cleanly designed but limited in scope.  
**Clarity:** Moderate. The main text is compressed; key theorems lack intuitive explanations.  
**Value to community:** Good. The algorithm is practically useful, and the theoretical framing offers a new perspective on symmetry in RL.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>