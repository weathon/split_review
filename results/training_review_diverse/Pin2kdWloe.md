Now I have a thorough understanding of the paper and can verify the reviewer's claims against the actual content. Let me compose the final consolidated review.

## Summary

This paper challenges the assumption that multitask (MT) learning is always the optimal objective in continual learning (CL). It formalizes a theoretical framework for linear-convex problems, proving (Theorem 4) that when task sequences exhibit positive instability, there exists a finite critical task duration beyond which a single-task (ST) agent that fully forgets each task accumulates lower average lifelong error than an MT agent. The paper then provides empirical evidence across three diverse benchmarks (CLEAR, MD5, ML10) and a controlled Permuted-CIFAR setting showing that the qualitative predictions of the theory — that MT can be suboptimal under high instability or long task durations — hold for neural networks. It also proposes heuristic instability estimation methods and a proof-of-concept Selective Replay agent.

## Strengths

- **Rigorous theoretical formalization for the linear-convex case.** The paper proves (Corollary 3 and Theorem 4, Section 4.2) that for strictly convex linear models with positive sequence instability, there exists a finite critical task duration $\bar{h}$ beyond which the ST agent's average lifelong error falls below the MT agent's. This moves a previously heuristic observation about MT suboptimality into a formal condition with clear assumptions (noiseless linear regression, squared loss, gradient descent), filling a gap relative to prior conceptual discussions.

- **Principled evaluation metric tied to online learning.** The paper adopts the average lifelong error (Equation 1), which is directly linked to dynamic regret from online learning. This metric naturally captures forward transfer — not just forgetting — and is used consistently across theory and experiments (Tables 1–3, Figure 3), giving a more complete picture of lifelong performance than traditional final-task metrics.

- **Broad empirical validation across diverse CL settings.** The study tests predictions on three structurally different benchmarks: CLEAR (smooth distribution shift), MD5 (sharp semantic task changes across 5 datasets), and Meta-World ML10 (adversarial RL tasks). The results confirm that the superior agent is data-dependent — MT wins on CLEAR; ST wins on MD5 and ML10 (Table 1) — and that varying task duration $h$ generally moves $\Delta_T$ in the direction predicted by the theory (Table 2, Figure 3).

- **Heuristic instability measures that rank benchmarks correctly.** The paper proposes two practical proxies for $\Delta_T^I$ in non-convex settings (Section 5.2, Table 4): (1) approximating task-specific and multitask minimizers and (2) a transfer-matrix diagonal-vs-off-diagonal comparison. Both correctly rank CLEAR as low-instability and MD5/ML10 as high-instability, aligning with the observed $\Delta_T$ values.

## Weaknesses

### Fatal

None.

### Major

- **No statistical significance or variance reported for any experiment.** Tables 1–3 and Figures 3–4 show no error bars, confidence intervals, standard deviations, or seed information. Given the known variability of neural network training (especially in RL, where ML10 uses PPO-based methods), it is impossible to assess whether the observed $\Delta_T$ differences are reliable or within noise. This is a methodological gap that weakens all empirical claims.

- **The theory-empirics gap is acknowledged but not bridged.** The theoretical analysis (Section 4.1–4.2) assumes noiseless linear regression, strictly convex quadratic losses, and full-batch gradient descent. The paper is transparent that "the non-linear case can not be approached theoretically" (line 70), but the empirical sections position the neural-network results as validating the theory's predictions without establishing a formal or even quantitative link. The neural instability measures (Options 1 & 2, Section 5.2) are heuristic: Option 1 is explicitly agent-dependent (contradicting the theory's definition of $\Delta_T^I$ as agent-independent), and Option 2 is a transfer-matrix heuristic. Neither is shown to quantitatively predict the critical task duration $\bar{h}$ — the Permuted-CIFAR experiments (Figure 3) show the correct qualitative trend (higher instability → lower $\bar{h}$) but do not compare the estimated $\bar{h}$ to any theoretical bound or the proposed instability measures. The paper's central mechanistic claim — that the competition between $\Delta_T^{ST}$ and $\Delta_T^I$ as a function of $h$ governs neural-network outcomes — is supported only by correlational evidence.

### Minor

- **The ML10 $\Delta_T$ does not decay with $h$ as predicted by the theory.** Table 2 shows the reward difference $\Delta_T$ in ML10 failing to decrease with task duration. The paper's explanation ("inherent noisiness of the reward signal," line 138) is a plausible but untested hypothesis. This unexplained result weakens the claim that the theory is predictive in RL settings.

- **The Selective Replay demo assumes oracle knowledge of instability.** The SR agent (Section 5.3) is given explicit knowledge of when to switch objectives (lines 177–178: "We take advantage of the knowledge of the sequence"). The paper acknowledges this (line 184), but the subsection still claims to "showcase the practical applicability of our framework" (line 124), which overreaches. The demo validates the concept but does not demonstrate a deployable method.

- **RL implementation details are underspecified.** The paper does not state what RL algorithm is used to implement the ST and MT agents on ML10 (PPO is cited in references but not mentioned in the method), how the multi-task objective is defined in the RL setting (joint value function or separate critics), or whether the same base optimizer is used. This is a reproducibility concern.

- **The MD5 (MULTIDATASET) benchmark lacks sufficient detail for reproduction.** The paper states that tasks are standardized to 30 classes (line 128) but does not specify: (a) how classes were selected from original datasets (which have varying class counts — e.g., Aircraft has 100, Cars has 196), (b) image preprocessing/resizing, or (c) whether class balance was maintained across the 30 selected classes.

- **Table 3 (effect of $K$ on ML10) is acknowledged as inconclusive.** The authors note (line 145) that task difficulty is not controlled across the sequence, making the results hard to interpret. This experiment adds little evidentiary value to the paper.

- **The instability estimates (Table 4) are not validated against the theoretical $\Delta_T^I$.** While they rank benchmarks correctly, the paper does not check whether they quantitatively predict the critical task duration $\bar{h}$ observed in Figure 3, leaving the link between the instability proxy and the theoretically-grounded $\Delta_T^I$ untested.

### Trivial

- The paper references "Lemma 9" and other numbered results (line 68, 74) that are not present in the main text, suggesting missing appendix content (though this is a parser artifact).

## Nice-to-Haves

- **Validating the instability estimator.** A natural extension would be to check whether the proposed $\tilde\Delta_T^I$ measures (Options 1 & 2) quantitatively predict the critical $h$ where $\Delta_T$ crosses zero in the Permuted-CIFAR experiments. This would make the framework actionable rather than descriptive.

- **Testing existing CL methods (EWC, ER, etc.) on the MD5/ML10 benchmarks** where ST beats MT. If the paper's message is that methods implicitly assume MT optimality, showing that standard methods underperform a simple forgetting baseline on these benchmarks would sharpen the practical relevance of the critique.

- **Extending theory via a function-space analysis (e.g., NTK)** would provide a principled bridge from the linear-convex setting to overparameterized neural networks, though this is beyond the current paper's scope and should not be required for acceptance.

## Removed Points

These points are flagged to be removed; treat them with caution.

- "ST agent is an extremely weak baseline" — The ST and MT agents are explicitly defined as analytical abstractions to study the fundamental trade-off, not as practical CL methods. The paper is clear about this framing (Section 3). Removed (misunderstands the paper's analytical purpose).
- "MT agent is an unrealistic oracle" — Same rationale: the MT agent is an analytical construct for studying the MT objective, not a proposed algorithm. Removed.
- "The claim about CL methods being biased estimates of the MT objective is too sweeping" — The paper cites Yin et al. (2020) and Lanzillotta et al. (2024) to support this claim (line 32). Removed (paper substantiates the claim with citations).
- "Proof of Theorem 4 not in main text" — Standard practice for conference papers to present informal theorem statements in the main text with proofs deferred. Removed (per rules about missing appendix/proofs).
- "Figure 2 uses only two alternating tasks, which is trivial" — The paper is explicit that this is a toy illustration to build intuition (Section 4.3). Removed (strawman).
- "The paper does not compute a numeric $\bar{h}$" — The paper does estimate it: "the critical task duration for PC-32 is estimated to be between 3000 and 6000 steps" (line 168). Removed (factually incorrect).
- "Extend theory via NTK" — A constructive suggestion for future work, not a weakness of the current paper. Moved to Nice-to-Haves.
- "Test existing CL methods on benchmarks where ST beats MT" — Scope creep; the paper's contribution is about the MT objective, not benchmarking CL algorithms. Moved to Nice-to-Haves.

## Novel Insights

The most interesting observation emerging from the reviews (beyond the paper's own contributions) is the tension between the paper's theoretical precision and its empirical scope: the theory cleanly identifies agent-independent instability as the quantity governing the ST-vs-MT trade-off, but the neural-network proxies for instability are inherently agent-dependent, creating a gap that the paper papers over with "the concept remains empirically useful." This raises a deeper question the field should confront — whether sequence-level properties like "instability" can ever be defined independently of the model class used to measure them, or whether the data-dependence the paper advocates for is inescapably also model-dependence.

## Suggestions

1. **Report error bars / confidence intervals** for all empirical results (Tables 1–3, Figures 3–4). This is the most impactful improvement — without it, readers cannot assess whether the reported $\Delta_T$ values are reliable. Use at least 3–5 random seeds.
2. **Validate the instability estimators quantitatively.** On the Permuted-CIFAR benchmarks, compute $\tilde\Delta_T^I$ from Options 1 & 2 and compare the predicted critical $h$ to the empirically observed crossover point. This would tighten the theory-empirics link.
3. **Specify the RL implementation details** — which algorithm (PPO? SAC?), whether the MT agent uses a shared critic or separate critics, and how the multi-task reward objective is defined.
4. **Add reproduction details for MD5** — how classes were selected, image sizes, data augmentation, balance preservation.
5. **Reframe the SR demo** as a proof-of-concept that validates the concept under idealized conditions, rather than claiming "practical applicability," to avoid overclaiming.

## Score and Decision

This paper makes a genuine conceptual contribution by formalizing conditions under which the multitask objective is suboptimal in continual learning, backed by clean theory for linear-convex problems and broad (if not yet rigorous) empirical support. The main limitations — absence of statistical rigor, heuristic nature of the neural-network instability measures, and oracle-dependent demo — are real but addressable. The paper does not need NTK-level theory or a full CL method benchmark to be a useful contribution.

**Originality**: The formalization of critical task duration and the decomposition of $\Delta_T$ into stability/instability components is novel, even if the high-level conceptual point (MT is not always optimal) has precursors.

**Quality**: Theoretical analysis is sound within its assumptions. Empirical work is suggestive but lacks statistical rigor.

**Clarity**: Well-written and honest about limitations.

**Significance**: Useful framing that could influence how CL method designers think about objectives.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>