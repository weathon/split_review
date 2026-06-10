## Summary

The paper proposes State Chrono Representation (SCR), a representation learning framework for image-based RL that augments behavioral metrics (bisimulation/MICo distances) with long-term temporal information. Two main components are introduced: (1) a **chronological embedding** $\psi$ that captures behavioral distance between state-pairs across trajectories, and (2) a **temporal measurement** $\hat{m}$ constrained by lower and upper bounds to encode cumulative reward information between current and future states. Experiments on DeepMind Control Suite (default and distraction settings) and Meta-World show strong gains over metric-based baselines (DBC, MICo, SimSR), particularly in the distraction setting.

---

## Strengths

- **Consistent and large margins on every generalization task (Table 2, lines 328–330):** SCR outperforms all five baselines on all eight Distracting DM_Control tasks. The gains are substantial (e.g., Cartpole-SwingUp: 565.1 vs. 230.0 next-best, Cheetah-Run: 331.7 vs. 177.4, Hopper-Stand: 400.8 vs. 19.6, Walker-Walk: 555.1 vs. 167.2). This directly supports the paper's core claim about generalization.

- **Ablation study validates both novel components are necessary (Figure 7, lines 405–413):** Removing either the chronological embedding ($\psi$) or the temporal measurement ($\hat{m}$) degrades performance, and removing both ($\phi$ only) performs worst. This ties the two proposed architectural innovations to empirical gains.

- **Novel distance metric with theoretical grounding and empirical superiority (Definition 2, Theorem 3, Lemma 1, lines 410–413):** The proposed $\hat{d}(\mathbf{a}, \mathbf{b}) = \sqrt{\|\mathbf{a}\|^2_2 + \|\mathbf{b}\|^2_2 - \mathbf{a}^{\top}\mathbf{b}}$ is proven to be a diffuse metric with non-zero self-distance. The ablation confirms it outperforms cosine, MICo angular, and L1 alternatives.

- **Two-constraint scheme for temporal measurement (Eqs. 13–14, lines 199–235):** Rather than directly regressing the intractable optimal-policy reward sum, the paper enforces a lower bound (any policy's return ≤ optimal) and an upper bound (triangle-inequality-style). The stop-gradient on the upper-bound term (Eq. 18, line 230) shows careful design to prevent representation collapse.

---

## Weaknesses

### Major

- **The latent dynamics model $\hat{P}$ is invoked but never specified (Section 3.1, Eq. 4, Eq. 5):** The metric update operator (Eq. 4) and the loss $\mathcal{L}_\phi$ (Eq. 5) both rely on sampling from $\hat{P}(\cdot|\phi(\mathbf{x}_i), a_{\mathbf{x}_i})$ — described as "the learned latent dynamics model" (line 87). However, the paper provides no description of its architecture, parameterization, training loss, whether it is learned jointly with $\phi$ or separately, or even whether it is deterministic or stochastic. The text says the approach "draws inspiration from SimSR" but does not specify whether the same implementation is used or adapted. Without this, the computation of Eq. (4) and Eq. (5) is not reproducible. This is a significant methodological gap.

- **The asymmetric metric function $\hat{m}$ is named but never defined (Section 3.2, lines 193, 237–240):** The paper calls $\hat{m}$ "a non-parametric asymmetric metric function" and promises "details are presented at the end of this section" (line 193). However, the section titled "Asymmetric Metric Function for $\hat{m}$" (lines 237–240) only states that the function should be asymmetric and cites prior work on quasimetrics — it never actually defines $\hat{m}$. Both the lower-bound loss (Eq. 13) and upper-bound loss (Eq. 14) depend on this unspecified function. This makes a core component of the claimed contribution incomplete.

- **Baseline performance numbers raise credibility concerns (Table 1, lines 304–310):** Several metric-based baselines produce scores that appear anomalously low. MICo achieves 4.9±1.8 on Cheetah-Run and 2.0±0.1 on Finger-Spin in the default setting; DBC scores 104.2±33.3 on Ball-in-Cup-Catch and 43.5±55.6 on Hopper-Stand. These numbers are far below what the published literature for these methods typically reports. Since the paper's main evidence (distraction-setting gains) relies on comparing SCR against these same implementations, the reader cannot rule out that the advantage reflects weak baselines rather than a genuine property of SCR. The paper does not acknowledge this discrepancy or provide any verification that its baseline implementations reproduce published results. (Note: The critic's specific claim that DBC scored 0.0 on cartpole-swingup-sparse is incorrect — that is MICo's score — but the broader concern about depressed baseline performance is valid.)

### Minor

- **The upper constraint (Eq. 15, lines 217–221) is stated without rigorous justification:** The inequality $|\hat{m}(\mathbf{x}_i, \mathbf{x}_j)| \leq d(\mathbf{x}_i, \mathbf{y}_{i'}) + |\hat{m}(\mathbf{y}_{i'}, \mathbf{y}_{j'})| + d(\mathbf{x}_j, \mathbf{y}_{j'})$ imposes a bound on the temporal measurement using arbitrary reference states from a different trajectory. The paper describes this as "the longer path from $\mathbf{x}_i$ to $\mathbf{x}_j$" (line 221), but the RHS routes through unrelated states $(\mathbf{y}_{i'}, \mathbf{y}_{j'})$, not an actual longer path between $\mathbf{x}_i$ and $\mathbf{x}_j$. The constraint is imposed rather than derived, and the paper provides no analysis of whether it is provably satisfied by the true $m$ or what effect it has on convergence of the learning dynamics.

- **Default-setting results are only "comparable" to DrQ, not superior (Table 1, lines 387–388):** In the standard DM_Control setting, SCR and DrQ achieve comparable scores (tied 4-4 on wins). DrQ is a data-augmentation method with no metric learning, yet it matches or exceeds SCR on half the tasks. This undercuts the claim that learning behavioral metrics is beneficial in standard settings, and the paper's characterization of the comparison as merely "comparable" does not fully surface this tension.

- **Meta-World results are reported only as aggregate success rates (Table 3, lines 430–433):** Only the average success rate over six tasks is shown, with very high standard deviations for several baselines (SAC: 0.495±0.475, DBC: 0.479±0.453). Per-task numbers are missing, which could mask whether SCR's advantage is consistent or driven by a subset of tasks. Individual training curves are shown for only 4 of 6 tasks.

### Trivial

- None (the paper is generally well-structured and the presentation is clear).

---

## Nice-to-Haves

- The modularity claim ("can be integrated into any existing RL algorithm") is only demonstrated with SAC. Testing with one additional base algorithm (e.g., DDPG or PPO) would strengthen this.
- The ablation study is limited to 2 tasks; expanding to 3–4 tasks would increase confidence that the findings generalize.
- An analysis of learned representations (e.g., visualizing the temporal measurement values or the structure of the chronological embedding space) would complement the quantitative results.

---

## Removed Points

These points surfaced in the reviews but were removed per filtering rules. They should not influence the score.

- **Critic claim that DBC scores 0.0 on cartpole-swingup-sparse (factual error):** The paper shows DBC at 65.9±80.3 on this task; the 0.0 belongs to MICo.
- **Critic claim that DrQ beats SCR on 6 of 8 tasks in default setting (factual error):** Counting from Table 1, the split is 4-4.
- **Critic claim about parameter sharing impossibility (misunderstanding):** $\psi$ operating on $\phi$'s output with shared weights is possible and not contradictory.
- **Missing implementation details / hyperparameters / network architectures / proofs (likely in stripped appendix):** Per instructions, these are standard omissions caused by PDF parsing stripping appendices.
- **Critic demand for t-SNE visualizations and representation analysis (scope creep):** These are not standard requirements for an empirical RL paper of this type.
- **Critic demand for testing with PPO / DDPG (scope creep):** The paper's claim is modularity of the representation learning framework, not an exhaustive RL algorithm benchmark.
- **Strength Finder's claim about problem importance (generic/superficial):** Dropped per filtering rules — the problem is well-motivated but stating "the problem is important" is not a concrete strength.

---

## Novel Insights

None beyond the paper's own contributions. The key idea — augmenting behavioral metrics with long-term temporal information via a chronological embedding and constrained temporal measurement — is already well-articulated by the authors. The reviewer inputs did not surface any novel perspective not present in the paper.

---

## Suggestions

1. **Specify $\hat{P}$ completely:** Provide the architecture, training loss, optimization details, and whether it is learned jointly with $\phi$ or pre-trained. Clarify whether it follows SimSR's implementation exactly or differs.
2. **Define $\hat{m}$ explicitly:** The "Asymmetric Metric Function" subsection must contain an actual function definition, not just a discussion of asymmetry. If $\hat{m}$ is a simple learned MLP or a particular quasimetric, state it clearly.
3. **Address the baseline discrepancy:** Run DBC, MICo, and SimSR under their original hyperparameters and verify that they achieve their published performance levels on 2–3 representative tasks. Report the comparison transparently, and if the numbers still diverge, explain the differences.
4. **Provide per-task Meta-World results** in a supplementary table so readers can assess consistency.
5. **Strengthen the justification for the upper constraint (Eq. 15):** Either prove that the true $m$ satisfies this inequality, or provide an empirical analysis showing that imposing it improves representation quality and does not introduce bias.
6. **Acknowledge the default-setting limitation upfront:** The paper currently says SCR achieves "comparable" results to DrQ, but should explicitly note that a method with no metric learning (DrQ) matches SCR on 4 of 8 standard tasks.

---

## Score and Decision

The paper proposes a clearly motivated idea with strong empirical results on the challenging distraction setting. The ablation study convincingly ties performance to the proposed components, and the distance metric $\hat{d}$ is both theoretically grounded and practically useful. 

However, two **Major** weaknesses prevent acceptance in the current form: (1) the latent dynamics model $\hat{P}$ is a core component of the metric loss but is never specified, and (2) the temporal measurement function $\hat{m}$ is named but never defined, despite being listed as a core contribution. These are not appendix-level omissions — they are central methodological details without which the method cannot be fully understood or reproduced. Combined with the baseline performance concerns, these issues are too significant for a top-tier venue.

The paper has a clear path to resubmission: specify the missing components, fix baseline verification, and tighten the justification of the upper constraint.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>