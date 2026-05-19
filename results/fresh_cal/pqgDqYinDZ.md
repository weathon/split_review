Now I have a thorough understanding of the paper. Let me write the consolidated final review.

---

## Summary

This paper proposes a multi-objective inverse reinforcement learning (MOIRL) framework for learning from multi-expert demonstrations with different preferences. It assumes a common vectorized reward across experts, enforced via consensus ADMM in discrete environments and a penalty-based extension of IQ-Learn (MOIQ) in continuous environments. The method claims to enable transfer to preferences unseen in the demonstrations using a single model conditioned on preference input. Experiments on Deep Sea Treasure (DST) and multi-objective MuJoCo environments show competitive performance against GAIL baselines in most settings.

---

## Strengths

1. **Novel integration of IQ-Learn with multi-objective reward consensus** — The paper derives a constrained optimization (Equation 10) and converts the consensus constraint into a penalty term on the critic objective (Equations 13–14), enabling end-to-end training without separate IRL-RL loops. This is a methodological advance over prior MOIRL approaches that require running single-objective IRL independently per expert (Section 2).

2. **Competitive performance across most preferences with a single model** — Table 1 shows the model achieves expert-level or better average return in 13 out of 15 tested preference–environment combinations, with the same architecture handling preferences via conditioning input $Q(s,a,\omega_i)$ and $\pi(s,a,\omega_i)$ (Section 5.3, Table 1 caption).

3. **Sample efficiency advantage clearly demonstrated in low-data regime** — In DST, where each expert provides only ~20 state-action pairs (2-step episodes × 10 demos), GAIL fails while MOIQ reaches expert-level performance within 100K environment steps (Section 5.3). The paper attributes this to shared reward knowledge, providing concrete evidence for the advantage.

4. **Empirical support for the common-reward hypothesis** — On discrete DST (Figure 1), all agents converge to near-optimal return within 10 ADMM rounds on both mini-map and default map, validating that the consensus ADMM procedure effectively enforces a common reward.

5. **Honest reporting of limitations** — The paper transparently acknowledges transferability failures in Mo-Walker and Mo-HalfCheetah (Section 5.4), and discusses limitations including demonstration quality and preference labeling requirements (Section 6).

---

## Weaknesses

### Fatal
None.

### Major

1. **Only one baseline (GAIL), and it is not a multi-expert method** — The paper compares only against GAIL (trained separately per expert), which does not capture the multi-expert setting. The paper itself cites several multi-expert IRL methods in related work (Kishikawa & Arai 2021, 2022; Chen et al. 2020, 2022; MSRD), but none are used as baselines. The justification ("Since there are few IRL algorithms with multi-expert setting," line 221) is insufficient given these cited methods exist. Without comparison to at least one method that also addresses the multi-expert/multi-objective problem, it is unclear whether MOIQ's specific approach (common reward + penalty) is responsible for the results or simply having access to pooled demonstrations. This weakens the experimental contribution substantially.

2. **No ablation of the penalty coefficient β** — The consensus penalty weight β is introduced as the central hyperparameter of the continuous method (Equations 13–14, line 165: "β is the constraint coefficient controlling the importance of the common reward constraint"), yet it is fixed at β=5 with no ablation study. The paper does not examine: (a) whether the penalty actually enforces reward similarity across experts, (b) how sensitive results are to β, or (c) what happens when β=0 (no consensus constraint). This is a critical gap because the penalty is the core mechanism distinguishing MOIQ from independent IQ-Learn.

3. **Transferability claim is only partially supported** — The paper claims transferability to unseen preferences (Abstract, line 14, contribution 3), but the evidence is mixed. The paper itself states that in Mo-Walker and Mo-HalfCheetah "the preference doesn't match the vectorized return quite well" (Section 5.4), and attributes this to insufficiently distinct experts. However, no quantitative transferability metric (e.g., correlation between input preference and achieved return) is provided for any environment. For the environments where transfer works (DST, Mo-Ant), the evidence is visual only (Figure 3). A stronger claim requires quantifiable evaluation across all environments.

4. **Incomplete comparison on computational cost** — The paper motivates the method by arguing that prior approaches "completely ignore the computational cost because it still needs to run IRL n times" (Section 2), but provides no wall-clock time, parameter count, or training-step comparison to either GAIL or the cited multi-expert methods. The discrete ADMM method also runs IRL/RL per expert per round, so its relative efficiency is asserted rather than demonstrated.

### Minor

1. **Vector reward recovery from Q is underspecified** — The paper writes $r_i = \mathcal{T}^\pi Q_i$ (line 179) as the estimated vector reward, but $\mathcal{T}^\pi$ is defined in Section 3 only for scalar Q (line 79: $(\mathcal{T}^\pi Q)(s,a)=Q(s,a)-\gamma\mathbb{E}_{s'}[V^\pi(s')]$). It is a natural extension to apply the operator per dimension of a vector-valued Q, but the paper does not state this explicitly. The critic network uses $Q(s,a,\omega_i)$ (line 176) which is implicitly vector-valued (since $\omega_i^T$ is applied to scalarize it), but how the per-dimension reward is recovered is left to the reader to infer. This creates an unnecessary clarity barrier.

2. **No confidence intervals or statistical testing** — Results are averaged across 5 seeds but no confidence intervals, standard deviations, or significance tests are reported for any experiment (Table 1, Figure 1). Given the known variance of RL/IRL training, this limits the reader's ability to assess result reliability.

3. **No quantitative transferability metric** — As noted above, transferability is evaluated only by visual inspection of Figure 3 rather than a quantitative measure such as the correlation between input preference and achieved vectorized return.

### Trivial

1. **Minor notation inconsistencies** — The ADMM update uses $\bar{r}^k$ in the equation (line 118–119) but introduces $\bar{\pmb{r}}^k$ in the text (line 122). The summation index in the per-agent penalty term $\sum_{j=i-1}^{i}$ (Equation 14, line 162) is poorly defined for edge cases (j=-1).

2. **Some garbled/OCR artifacts in the expert generation description** (Section 5.1, line 198) — Though these are parser issues, the text is difficult to parse even accounting for formatting.

---

## Nice-to-Haves

- An ablation study of β values would strengthen the paper considerably.
- Comparison to at least one multi-expert IRL method (e.g., Kishikawa & Arai 2021 on the discrete DST environment) would anchor the contribution.
- A quantitative transferability metric (correlation coefficient between preference $\omega$ and achieved vectorized return) would replace the current visual-only evaluation.
- Wall-clock time comparisons would substantiate computational efficiency claims.

---

## Removed Points

These points are flagged to be removed; treat them with caution:

- **Harsh Critic: "The penalty term itself is defined only for adjacent pairs, which does not enforce all r_i equal; for n>2 this is an odd choice"** — Factually incorrect. Penalizing all adjacent pairs in a chain (0↔1, 1↔2, ...) enforces all $r_i$ equal through transitivity. This is a standard consensus formulation, not an odd choice.

- **Harsh Critic: "The method description is underspecified to the point of non-reproducibility" (framed as structural/fatal)** — The paper states $r_i = \mathcal{T}^\pi Q_i$ (line 179) and the element-wise application of the inverse soft Bellman operator to a vector-valued Q is the natural extension. The notation is sloppy but recoverable. Demoted to Minor weakness (#1 above).

- **Harsh Critic: "The 'single model' claim is unclear and potentially misleading"** — The paper uses $Q(s,a,\omega_i)$ and $\pi(s,a,\omega_i)$ (Section 4.2.2, lines 173, 181), which clearly indicate a single network conditioned on preference $\omega_i$ as input. Separate variable names per expert in the derivation are standard notation, not evidence of separate networks.

- **Harsh Critic: "GAIL is inappropriate for this setting"** — The baseline is weak but the paper at least frames it as a starting point: "Since there are few IRL algorithms with multi-expert setting, we compare our results with GAIL" (line 221). The real issue is the absence of multi-expert baselines, which is already captured in Major weakness #1.

- **Harsh Critic: Section-by-Section notes about garbled text ("Table 1 is heavily garbled", "Figure 2 is not visible")** — These are PDF parser artifacts, not problems in the original submission. Removed per hard rules.

- **Strength Finder: generic praise ("addresses an important problem")** — Removed as generic/superficial; only concrete, evidence-anchored strengths are retained.

- **Harsh Critic: "No statistical testing" and "No analysis of discrete ADMM convergence"** — The first is retained as a minor weakness (standard for empirical ML papers). The second is partially addressed since the paper reports final return and rounds to convergence (Figure 1), which is ADMM convergence analysis at the task level.

---

## Novel Insights

The two reviews together surface a tension at the heart of this paper: the method's strongest advantage (shared reward knowledge enabling sample efficiency) is also its least empirically validated dimension. The harsh critic correctly identifies that without ablation of the consensus penalty β and without comparison to other multi-expert methods, it is impossible to attribute the positive results to the consensus mechanism rather than to pooled data or the IQ-Learn backbone. The strength finder validly highlights that the paper does demonstrate the core claim works in most of the tested settings. The genuinely novel observation is that the discrete ADMM approach (Section 4.1) and the continuous penalty approach (MOIQ, Section 4.2) are methodologically distinct — one iteratively solves for consensus across outer rounds, the other uses a soft penalty within a single end-to-end training loop — yet the paper does not discuss whether they produce empirically equivalent solutions, leaving an interesting open question about the relationship between hard consensus (ADMM) and soft consensus (penalty) in multi-expert IRL.

---

## Suggestions

1. **Add multi-expert baselines.** Compare to at least one of Kishikawa & Arai (2021/2022) or Chen et al. (2020/2022), even if only on the discrete DST environment. If those methods are not easily adaptable, a comparison to independent IQ-Learn runs per expert (the MOIQ method with β=0) would provide a meaningful ablation.

2. **Conduct a β ablation study.** Evaluate β ∈ {0, 1, 5, 10, 50} on at least one continuous environment to show the effect of the consensus penalty on both final return and reward similarity across experts.

3. **Provide a quantitative transferability metric.** Compute the correlation (e.g., Spearman's ρ) between input preference ω and achieved vectorized return across the 19 tested preference values for all 2-dimensional environments, not just visual plots.

4. **Clarify vector reward recovery.** State explicitly that $Q(s,a,\omega)$ outputs a vector in $\mathbb{R}^d$ (one dimension per objective) and that the inverse soft Bellman operator $\mathcal{T}^\pi$ is applied per dimension to produce the vector reward $r = (r^1, \ldots, r^d)$.

5. **Report confidence intervals or standard deviations** for the key experimental results across the 5 seeds.

---

## Score and Decision

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>