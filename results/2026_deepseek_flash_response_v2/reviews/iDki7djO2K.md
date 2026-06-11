## Summary

This paper proposes a formal definition of forgetting in learning systems, grounded in the concept of predictive self-consistency. The key insight is that if a learner updates its predictions on data that are already consistent with its own expectations, any resulting change cannot reflect new information acquisition and therefore must represent forgetting. The paper introduces a measure $\Gamma_k(t)$ quantifying the "propensity to forget" as the divergence between predictive distributions before and after $k$ self-consistent updates, and presents illustrative experiments across classification, regression, generative modeling, CL, and RL settings.

## Strengths

1. **A principled, task-agnostic formalism grounded in predictive self-consistency.** The paper defines forgetting as violation of a consistency condition (Definition 4.5, Eq. 8) where predictive distributions after updates on self-generated targets should be recoverable by marginalization. This single definition applies across supervised learning, RL, and generative modeling through the abstract $(X_t, Y_t, Z_t)$ interface (§3.3), unifying fragmented definitions from CL and RL literatures that conflate forgetting with parameter drift or task-specific performance decay.

2. **Clean separation of forgetting from backward transfer and from parameter changes.** By sampling $X_t$ from the hybrid distribution $q_e$ (the learner's own predictive beliefs) rather than the true environment (§4.2, Eq. 7–8), the formalism isolates destructive updates from constructive backward transfer. Section 5.1 demonstrates that exact Bayesian learners satisfy the consistency condition even as their parameters change, providing a concrete counterexample proving parameter change $\neq$ forgetting (Takeaway 2). This is a genuine conceptual advance over definitions that conflate parameter drift with forgetting.

3. **Empirical discovery of a non-zero optimal forgetting level for training efficiency.** Section 5.3 and Figure 4 show that varying momentum or model size produces an "elbow" where maximum training efficiency occurs at an intermediate forgetting level. This goes beyond merely measuring forgetting — it suggests a functional trade-off where a moderate amount of forgetting can be beneficial rather than purely destructive, which is a non-trivial finding.

4. **Well-motivated desiderata (4.1–4.4) that transparently guide formalism design.** The four explicit requirements are stated before the formalism is built (§4.1), making design choices and their motivations clear. This is good scientific practice that most papers omit.

5. **Formal justification for replay mechanisms emerges naturally from the theory.** Definition 4.5 shows that when the update $u$ depends on history $H_{0:t-1}$, the consistency condition requires access to past data — providing a mathematical rationale for why replay buffers are needed in CL and RL.

## Weaknesses

### Major

1. **Empirical validation does not meet the paper's own evidentiary standard.** The paper claims the experiments "validate" the formalism (abstract, line 220) but presents no comparison between $\Gamma_k(t)$ and existing forgetting measures (backward transfer, performance drop, parameter change). The paper motivates the need for a new definition by critiquing existing metrics for conflating forgetting with backward transfer (§2, line 40–41) — yet never tests whether $\Gamma_k(t)$ successfully disentangles them in a controlled setting. A simple experiment comparing $\Gamma_k(t)$ to a standard CL forgetting metric on a task where both constructive and destructive transfer occur would demonstrate the claimed advantage. Without this, the core motivation is asserted but not empirically supported.

2. **Unsupported causal claims about forgetting's role in learning dynamics.** Section 5.4 states that in DQN on cartpole, "the forgetting curve follows the TD loss **because** forgetting information is the mechanism by which the agent manages this process" (line 301, emphasis added). This is a causal claim supported only by correlational evidence (both curves rise and fall together). Many confounders could drive both measures, most obviously the non-stationarity of the Q-learning target. Similarly, the trade-off in §5.3 shows that varying hyperparameters changes both $\Gamma_k(t)$ and training efficiency, but this does not establish that forgetting *causes* the efficiency differences — the correlations are consistent with many interpretations. These causal statements should be toned down to correlational observations.

3. **Empirical scope is limited to small models despite claims about "deep learning."** The experiments use "shallow neural network[s]" and "single-layer neural network[s] on a two-moons classification task" (Figure 3 caption) — models far from modern deep learning practice. While the conceptual framework is general, the paper's title "Forgetting is Everywhere" and framing around deep learning (§5.2) imply broader scope than the evidence supports. Computing $\Gamma_k(t)$ requires simulating the learner's predictive distribution over future sequences, and the paper does not explain how this would scale to deeper architectures or more complex tasks. This is a nontrivial gap between the theoretical generality claimed and what is demonstrated.

### Minor

1. **No comparison to any existing forgetting metric.** Beyond the major issue above, the paper could be strengthened by even a single experiment comparing $\Gamma_k(t)$ to a standard measure (e.g., $\text{forgetting}_k = \max_{l<k} a_{l,j} - a_{k,j}$ from CL) to show whether the new measure yields different or better insights. Without this, it is impossible to assess whether $\Gamma_k(t)$ is practically useful or merely a different parametrization of the same information.

2. **Notation inconsistency: $q_e$ vs. $q_c$.** The hybrid distribution is introduced as $q_e$ (§3.2, Eq. 3) and used throughout, but Definition 4.5 (Eq. 8, line 215) uses $q_c$ without explanation. This appears to be a typographical error.

3. **Strong novelty claim not fully supported by the paper's own scope.** The conclusion states this is "the first generalized definition of forgetting" (line 307). While the formalism is well-constructed, the paper does not adequately discuss how it relates to related formalisms — e.g., information-theoretic measures of model change, martingale properties of Bayesian predictive distributions, or the psychology literature on forgetting curves. The novelty claim is plausible but insufficiently supported by the paper's own discussion of prior work.

### Trivial

None.

## Nice-to-Haves

- A controlled experiment where $\Gamma_k(t)$ is compared against a standard CL forgetting metric on a scenario with known ground truth about forgetting vs. backward transfer, to demonstrate the claimed advantage.
- Clarification of how $q_e$ is concretely instantiated for each experimental setting (e.g., for a fixed supervised learning dataset where the environment does not generate inputs conditional on labels).
- Statistical tests (confidence intervals, effect sizes) for the claimed trade-off in §5.3.
- A discussion of how $\Gamma_k(t)$ could be approximated for deeper networks or settings without tractable predictive distributions.

## Removed Points

- **"The formalism defines forgetting into existence, then validates its own definition"** — The harsh critic overstated this: the experiments do show non-trivial patterns (task boundary effects, the forgetting-efficiency trade-off, RL dynamics) that are not "baked into" the definition. However, the kernel of truth (insufficient validation against alternatives) is already covered in Weakness #1 above.
- **"The hybrid distribution $q_e$ is underspecified to the point of being non-operational"** — While the notation inconsistency with $q_c$ is real, the conceptual idea of $q_e$ is clear enough: it is the environment's observational component combined with the learner's predictive component. This is a presentational issue, not a fatal flaw.
- **Various generic "scope creep" criticisms** (e.g., demanding the paper address psychology literature, demanding the paper address non-Bayesian settings where the unforgetful baseline disappears) — these demand the paper solve problems beyond its stated scope.

## Novel Insights

The most useful insight from the review process is that the paper's core strength (a clean, principled definition) is also the source of its main empirical weakness: the definition requires computing divergences between predictive distributions over future sequences, which is tractable only for small models or settings with known distributions. The paper would benefit from explicitly acknowledging this tension and discussing approximations for scaling $\Gamma_k(t)$ to modern architectures, rather than claiming full "validation" from shallow-network experiments.

## Suggestions

1. **Add a comparison experiment** that tests $\Gamma_k(t)$ against a standard CL forgetting metric on a controlled scenario, demonstrating the claimed advantage of disentangling forgetting from backward transfer.
2. **Tone down causal language** in §5.4 — replace "because forgetting is the mechanism" with appropriately correlational phrasing.
3. **Either broaden the experiments** to include deeper architectures or **explicitly scope the claims** to small models and discuss the computational challenges of scaling $\Gamma_k(t)$.
4. **Fix the $q_c$/$q_e$ notation** inconsistency in Definition 4.5.
5. **Add error bars and effect sizes** to the forgetting-efficiency trade-off plots to distinguish signal from noise in the claimed "elbow" pattern.

---

**Calibration Report**

Round 1 (bracketing) — Score range: initially estimated 4–6.

| Anchor | Path | Avg Score | Round | Comparison |
|--------|------|-----------|-------|------------|
| "Replay can provably increase forgetting" | kf9phcBvQ5 | 3.00 | R1 | Weaker: CL theory paper with interesting result but poor writing and limited impact. This paper has a more general conceptual contribution. |
| "Eidetic Learning" | 6E8GCcCgxl | 3.25 | R1 | Weaker: Method paper with strong guarantees but narrow scope. This paper asks a more fundamental question. |
| "Demystifying LM Forgetting" | ohqjYsRBD1 | 4.00 | R1/R2 | Comparable but different: Empirical analysis with similar limitations (no comparison to baselines, limited practical value). This paper has stronger theoretical foundations. |
| "Replay concurrently or sequentially?" | nSYycd5tEC | 4.00 | R2 | Comparable: Theoretical CL paper with rigorous but narrow analysis. This paper is broader in scope but less mathematically tight. |
| "Why Fine-Tuning Struggles..." | CGfWyU28Pd | 4.50 | R2 | Comparable: Theoretical analysis of forgetting in unlearning. Both papers have limited empirical scope but interesting theoretical insights. |
| "Joint Effect of Task Similarity..." | u3dHl287oB | 5.67 | R2 | Stronger on theoretical rigor: Exact analytical expressions for forgetting in a well-defined setting. This paper has broader scope but less precise results. |
| "Spurious Forgetting in CL of LMs" | ScI7IlKGdI | 6.33 | R2 | Stronger overall: Clear novel insight, supported by experiments on real models, practical method derived from theory. More complete paper. |
| "Label-Agnostic Forgetting" | SIZWiya7FE | 6.00 | R1 | Stronger: Method paper with thorough experiments and clear claims. More evidence per claim. |

Round 2 (narrowing, target bracket 4–6): Final calibration based on comparison to anchors — the paper is stronger than the 3.0–4.0 rejected papers but weaker than the 5.67–6.33 accepted ones due to limited empirical validation and unsupported causal claims.

**Final Score: 5.0** — The conceptual contribution is genuinely novel and the formalism is well-constructed, but the empirical evidence is too weak to fully support the paper's claims, and key validation experiments (comparison to existing metrics) are missing.

MY FINAL SCORE: <score>5.0</score>
MY FINAL DECISION: <decision>Reject</decision>