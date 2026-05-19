## Summary

This paper proposes State Chrono Representation (SCR), a representation learning framework for image-based RL that augments existing behavioral metric methods (bisimulation, MICo) with explicit long-term temporal information. SCR introduces two components: (1) a **chronological embedding** ψ that captures behavioral distances between temporal state pairs, and (2) a **temporal measurement** m that quantifies cumulative rewards over extended horizons. The framework additionally proposes a novel diffuse metric \( \hat{d} \) that avoids numerical issues of angular distances while preserving non-zero self-distance. Experiments on Distracting DM Control and Meta-World show substantial improvements over existing metric-based methods (DBC, MICo, SimSR) and data-augmentation methods (DrQ), particularly under visual distractions and sparse rewards.

---

## Strengths

1. **Explicit temporal information integration addresses a genuine limitation of one-step metrics.** The paper correctly identifies that DBC and MICo rely on one-step transitions and struggle with sparse rewards and distractors. SCR's chronological embedding (Theorem 3) and temporal measurement (Section 3.3) directly target this gap. The results in Table 2 — where SCR achieves 3–10× improvements on several Distracting DM Control tasks (e.g., Cartpole-SwingUpSparse: 185.7 vs. 11.2 for DrQ) — validate the practical importance of this direction.

2. **Novel diffuse metric with both theoretical and practical advantages.** The proposed \( \hat{d}(\mathbf{a},\mathbf{b}) = \sqrt{\|\mathbf{a}\|^2_2 + \|\mathbf{b}\|^2_2 - \mathbf{a}^\top\mathbf{b}} \) (Definition 2) satisfies the triangle inequality as a diffuse metric, has non-zero self-distance (Lemma 1), and avoids the numerical instabilities of angular distances involving arccos operations. The ablation study (Figure 5) confirms that \( \hat{d} \) outperforms L1, cosine, and MICo angular distances in the same framework.

3. **Strong and consistent empirical results under distraction.** On Distracting DM Control (Table 2), SCR achieves the highest mean score on all 8 tasks with large margins. The aggregate IQM (Figure 3) confirms systematic advantage over all baselines. On Meta-World (Table 4), SCR achieves 0.969 average success rate with low variance (0.032), outperforming both metric-based methods (DBC: 0.479, SimSR: 0.258) and DrQ (0.886).

4. **Comprehensive ablations isolating each component.** Figure 5 systematically ablates ψ, \( \hat{m} \), and the distance metric \( \hat{d} \), showing that each contributes to the final performance. Figure 6 investigates the sampling step range [1,100] and demonstrates robustness around the optimum.

---

## Weaknesses

### Fatal
None.

### Major

1. **The upper-bound constraint (Eq. 6 / label{eq:triangle}) for the temporal measurement lacks theoretical justification.** The paper defines \( m(\mathbf{x}_i,\mathbf{x}_j) \) as expected optimal cumulative reward from \( \mathbf{x}_i \) to \( \mathbf{x}_j \), and imposes the inequality
   \[
   |\hat{m}(\mathbf{x}_i,\mathbf{x}_j)| \leq d(\mathbf{x}_i,\mathbf{y}_{i'}) + |\hat{m}(\mathbf{y}_{i'},\mathbf{y}_{j'})| + d(\mathbf{x}_j,\mathbf{y}_{j'}).
   \]
   No derivation or proof is provided that the true \( m \) satisfies this inequality. The right-hand side involves the behavioral metric \( d \) (which captures reward differences and dynamics divergence) and \( \hat{m} \) on arbitrary reference states \( \mathbf{y}_{i'},\mathbf{y}_{j'} \). The paper says the constraint is "proposed based on Fig. 2" (line 215) but does not formally connect the quantities. In practice, \( \mathcal{L}_{up} \) functions as a heuristic regularizer that pushes \( |\hat{m}| \) downward via a ReLU penalty with stop-gradient. While this design is not necessarily wrong, presenting it as a "constraint" without justification overstates its theoretical grounding. The authors should either derive the bound under mild assumptions, or acknowledge it as an auxiliary learning objective and demonstrate its effect via ablation (e.g., removing \( \mathcal{L}_{up} \) while keeping \( \mathcal{L}_{low} \)).

2. **The asymmetric metric function for \( \hat{m} \) is critically underspecified.** Line 193 states that \( \hat{m} \) is a "non-parametric asymmetric metric function (details are presented at the end of this section)," but the end of the section (lines 237–240) merely cites existing work on quasimetrics without specifying the actual implementation. How is asymmetry achieved? Is it a bilinear form, separate feedforward networks for \( \mathbf{x}_i \) and \( \mathbf{x}_j \), or another mechanism? What is the precise functional form, initialization, and any normalization? This is not a minor detail — the entire temporal measurement pipeline depends on it, and the paper cannot be reproduced without this information. This is the most significant omission in the method section.

### Minor

1. **No baseline comparing against n-step extensions of DBC/MICo.** The paper motivates SCR by arguing that one-step behavioral metrics fail to capture long-term information. A natural baseline is to augment DBC or MICo with multi-step targets (e.g., replacing the one-step target in the update operator with an n-step target). Without this comparison, it is unclear whether SCR's gains stem from the specific architectural design of ψ and m, or simply from incorporating longer temporal horizons. The ablation in Figure 5 confirms that both ψ and m are individually beneficial, but an n-step DBC baseline would more tightly isolate the paper's contribution.

2. **Limited hyperparameter and architectural detail.** The paper could benefit from a complete table of hyperparameters (learning rates, network sizes, gradient clipping, etc.) beyond the sampling step range. Additionally, the paper claims SCR "does not introduce a significant number of additional parameters" (line 24) but provides no parameter count or wall-clock time comparison against baselines to substantiate this.

### Trivial

1. The description of parameter sharing between φ and ψ (line 177) could be more precise. The paper states "the parameters of the encoders φ and ψ are shared" but then defines ψ as a function of φ's output: \( \psi(\phi(\mathbf{x}_i), \phi(\mathbf{x}_j)) \). This means the convolutional backbone is shared with an additional module composed on top — this is clear enough upon careful reading but could confuse readers.

---

## Nice-to-Haves

- Visualizations (t-SNE/UMAP) of learned representations comparing SCR against DBC/MICo under distraction would strengthen the qualitative analysis.
- An ablation experiment that removes only \( \mathcal{L}_{up} \) (keeping \( \mathcal{L}_{low} \)) would clarify how much the upper-bound constraint contributes beyond the lower bound.
- A breakdown of which distraction types (background video, color, camera pose) drive SCR's improvement would provide additional insight.
- A brief discussion of potential issues in off-policy settings where future states in the replay buffer may not be directly reachable from the current state.

---

## Removed Points

- **Missing proofs in appendix** (fixed points for Theorems 1 and 3): The parser strips appendix content; these proofs exist in the original submission. [Hard Rule]
- **Missing related works**: Not verifiable without external sources. [Hard Rule]
- **No comparison to DrQ-v2 or more recent methods**: The paper uses DrQ as a representative augmentation baseline, which is standard. Demanding this is scope creep. [Soft Rule]
- **Typographical/formatting concerns**: Parser artifacts, not author errors. [Hard Rule]
- **The relation between \( \hat{d} \) and L2 norm could lead to norm-dominance**: The critic raised this as a speculative concern without evidence that it causes issues in practice; the paper's ablation shows \( \hat{d} \) works well. [Speculative, not verified]
- **"No novelty claimed" for the latent dynamics metric**: This is an observation, not a weakness. The paper explicitly builds on existing work.

---

## Novel Insights

The reviews surfaced one genuinely novel observation not explicit in the paper: the upper-bound constraint (Eq. 12) with stop-gradient creates a one-sided penalty that can only push \( |\hat{m}| \) down, never up — effectively an asymmetrical regularizer. This is an interesting engineering insight about how the constraint behaves in practice, distinct from the claimed "bounding" framing. The paper would benefit from acknowledging this and ablating the stop-gradient design choice. Beyond this, the reviews do not contradict or add to the paper's own contributions in a nontrivial way.

---

## Suggestions

1. **Specify the asymmetric metric implementation explicitly** — provide the exact functional form, network architecture, and initialization used for \( \hat{m} \). This is required for reproducibility.

2. **Add an n-step DBC/MICo baseline** — this is the cleanest test of whether the gains come from SCR's specific design or simply from multi-step information.

3. **Reframe the upper-bound constraint** — either provide a theoretical justification, or acknowledge it as a heuristic regularizer and show an ablation removing \( \mathcal{L}_{up} \) to demonstrate its empirical effect.

4. **Provide a full hyperparameter table** and report parameter counts and wall-clock times for SCR vs. baselines.

---

## Score and Decision

The paper addresses a genuine limitation in metric-based representation learning for RL, proposes a well-motivated architecture with two complementary components, and demonstrates strong and consistent empirical gains across multiple domains. The two major weaknesses — the underspecified asymmetric metric and the unjustified upper-bound constraint — are significant but addressable: the first is a reporting gap, and the second, while theoretically underdeveloped, does not invalidate the empirical findings. The core contribution (temporal augmentation of behavioral metrics) is validated by the results.

**Score:** 7.0 — A solid paper with clear contributions and strong empirical evidence, held back from a higher score by two reproducible-construction gaps that can be resolved in revision.

MY FINAL SCORE: <score>7.0</score>
MY FINAL DECISION: <decision>Accept</decision>