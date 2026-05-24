Now I have a thorough understanding of the paper and can verify all the key claims. Let me write the consolidated review.

## Summary

This paper proposes MoE-F, a method for dynamically combining pre-trained LLMs in online time-series prediction tasks using stochastic filtering (the Wonham-Shiryaev filter). The key idea is to frame expert selection as a finite-state, continuous-time HMM, derive closed-form filtering equations for the posterior expert weights, and update the transition dynamics via a heuristic perturbation-and-matrix-logarithm procedure. Empirical results on a financial market movement task (NIFTY dataset) show a 17% absolute F1 improvement over the best individual LLM expert.

## Strengths

1. **Closed-form filtering equations avoid Monte Carlo simulation**: Theorem 1 provides a stochastic differential equation for the optimal posterior estimate π_t^(n) that is available in closed-form, which the paper correctly notes "is rarely the case in stochastic filtering" and avoids particle filtering's computational burden. This is a concrete theoretical contribution.

2. **Clear plug-and-play framing**: The algorithm explicitly operates without learned routing, requiring no retraining when adding or removing experts. This is a meaningful distinction from standard MoE approaches and is well-articulated in the related work section ("Learned Routing vs. Ours").

3. **Regularization guarantees for the Q-matrix update**: Propositions 1 and 2 provide theoretical guarantees that the perturbation P_t^α = (1-α)P_t + αI_N is invertible and row-stochastic (Prop. 1), and that the KL divergence between perturbed and original rows is bounded (Prop. 2), ensuring the update is well-behaved.

4. **Per-class label breakdown (Table 3)**: The decomposition of performance by class label provides useful insight into how MoE-F combines expert strengths, revealing that different experts specialize in different market regimes (e.g., Llama-2 better at predicting "Fall," Llama-3 better at "Rise").

## Weaknesses

### Fatal
None.

### Major

1. **No comparison against any ensemble or gating baseline.** The paper compares MoE-F only against individual LLM experts. This means the observed 17% F1 gain cannot be attributed to the filtering mechanism — it may simply reflect the benefit of ensembling multiple models. Simple baselines such as uniform averaging of expert predictions, softmax weighting by cumulative loss, or the Hedge algorithm would isolate the contribution of the filtering recursion. Without them, the paper's central claim — that stochastic filtering provides a principled and effective gating mechanism — is unsupported by the experiments. (Section 5.2, Table 1)

2. **Single task, single dataset for the main evaluation, supporting broad overclaims.** The entire empirical case rests on one dataset (NIFTY, 317 time steps) and one task (financial market movement). The paper claims MoE-F is "readily adaptable to various other challenging tasks" and a "viable online mixture of expert framework," yet provides no evidence on any other task, domain, or dataset. The ablations (Section 4.3) re-use the same NIFTY test set for experts fine-tuned on other datasets (ACL18, CIKM, BigData22); this does not constitute multi-task evaluation. (Section 5)

3. **Per-class analysis reveals gains are concentrated on the Neutral class, not uniform across all labels.** Table 3 shows MoE-F achieves Fall F1=0.30 (vs. best expert 0.35), Neutral F1=0.60 (vs. best expert 0.62), and Rise F1=0.30 (vs. best expert 0.32). The overall F1 improvement is driven primarily by better handling of the imbalanced majority class (Neutral, 143/317 samples). MoE-F does not improve over the best individual expert on Fall or Rise. This nuance is not discussed in the paper, which instead presents the aggregate F1 as a headline result. (Table 3, Section "Decomposing Expert Performance by Class Labels")

### Minor

1. **The Q-update in Step 3 is heuristic and theoretically disconnected from the filtering optimality guarantees.** Theorem 1 provides optimal filtering equations *given* the true infinitesimal generator Q. However, Q is estimated via a follow-the-leader heuristic: rows of P are set to the current softmin weights, regularized, log-transformed, and projected onto the set of valid generators. Propositions 1–2 address invertibility and KL stability of the perturbation, but not whether the resulting Q leads to good filtering. The paper provides no justification that this estimate converges to the true Q or that the filter remains near-optimal under a mismatched Q. (Section 4, Steps 3, lines 448–486; Theorem 1)

2. **Row-constant transition matrix imposes a strong, unacknowledged assumption.** The transition matrix P_t is constructed with all rows equal to the same softmin weight vector π̄_t (Eq. ~\eqref{eq:Markov_transition}). This implies that, under the estimated dynamics, the Markov chain's transition probabilities are identical regardless of the current state — i.e., the chain has no state-dependent switching behavior. This strong assumption is neither explicitly stated nor justified. (Section 4, Eq. ~\eqref{eq:Markov_transition})

3. **No statistical significance or variance reporting.** The main results (Table 1) state "All values are mean of 3 (random seed) runs except GPT-4o" but report no confidence intervals, standard deviations, or significance tests. With N=317, random seed variation could produce non-negligible variance in F1 scores. (Table 1 caption)

4. **Tension between continuous-time SDE theory and discrete-time classification task.** The theoretical model assumes Y_t evolves as a continuous-time SDE (Eq. 1) with Brownian noise and uses binary cross-entropy as the observation loss (Eq. 3). The experimental task is a ternary classification (Fall/Neutral/Rise). How the binary cross-entropy loss operates on ternary labels, and how the continuous-time SDE dynamics relate to discrete day-level market movements, is not explained. The paper notes the task "can be defined as a ternary or binary" problem but does not reconcile the mismatch. (Section 2, Eq. 1, Eq. 3; Section 5.1, task description)

### Trivial
None.

## Nice-to-Haves

- A synthetic switching experiment (where the active expert changes abruptly) would directly demonstrate the filtering mechanism's adaptive advantage over static ensemble methods.
- Computational cost analysis comparing MoE-F's O(Nd) per-step cost against simpler O(N) weighting schemes.
- Discretization error analysis: the theory is continuous-time, the algorithm uses Euler-Maruyama; what is the effect of time step on stability and performance?

## Removed Points

The following points from the reviewers are removed with justification:

1. **"No comparison against Hedge / online convex optimization"** — The critic's point about missing related work on prediction with expert advice is a valid observation, but per policy I cannot require specific related works or claim they are missing without external confirmation. The underlying concern (missing ensemble baselines) is already captured in Major Weakness #1.

2. **Formatting/style complaints about \ifthenelse macros and undefined quantities (δ, e^{t ln(δ^8)})** — These are parser artifacts from LaTeX conditionals, not author errors. Removed per policy.

3. **"LLMs perform at chance level"** — The paper does not claim its experts are strong on this specific financial task; the low baselines (F1 0.20–0.35) are presented as a challenging setting where ensembling helps. This is an observation, not a weakness.

4. **"Figure 3 is visually appealing but does not convey quantitative information"** — Figures can serve qualitative purposes; this alone is not a weakness.

5. **"The paper would benefit from stating the SDE model is a modelling assumption"** — The paper already presents it as an assumption ("we assume," "we postulate," "we consider the case where") throughout Section 1 and 2. This criticism misreads the paper.

6. **"The theorem contains undefined notation that is only specified earlier"** — This is standard paper structure; definitions precede theorem statements.

7. **Strength Finder's generic strengths about "addressing an important problem"** — Removed generic/superficial strengths that lack specific evidence from the paper's content.

## Novel Insights

The most striking finding from the cross-review is that the per-class analysis (Table 3) substantially undermines the headline 17% F1 claim. MoE-F's overall F1 of 0.52 comes almost entirely from better handling of the imbalanced Neutral class (F1=0.60 vs. best expert 0.62 — essentially comparable), while it fails to improve over individual experts on the rare Fall class (F1=0.30 vs. best expert Llama-2 at 0.35) and matches them on Rise (0.30 vs. 0.32). This suggests MoE-F may primarily be acting as an adaptive imbalance-correction mechanism rather than a general expert-combination method. This pattern is visible in the paper's own data but not discussed.

## Suggestions

1. **Add at least two ensemble baselines**: uniform averaging of expert predictions, and softmin weighting of cumulative loss over a moving window. These directly isolate whether the filtering recursion adds value over any reasonable ensemble.

2. **Add a second evaluation dataset or task** (even a simple synthetic switching-regime experiment) to support the claim that MoE-F adapts to changing dynamics rather than just averaging.

3. **Report confidence intervals or bootstrap estimates** for the main F1/accuracy metrics.

4. **Acknowledge and discuss the per-class performance pattern**: explain why MoE-F improves Neutral but not Fall/Rise, and whether this is an inherent property of the filtering approach or a consequence of the class imbalance.

5. **Clarify how the binary cross-entropy observation model (Eq. 3) applies to the ternary classification task** used in experiments. If the task was binarized, state that explicitly; if not, explain the adaptation.

## Score and Decision

This paper presents a novel theoretical approach (closed-form filtering for online LLM gating) and a clearly specified algorithm. The mathematical derivation is sound under its stated assumptions. However, the empirical evaluation is insufficient to validate the central claim that the stochastic filtering mechanism drives the reported gains. The complete absence of ensemble baselines, single-dataset evaluation, unreported variance, and the per-class analysis showing gains concentrated on one label class all limit what can be concluded from the experiments. The paper's theoretical contribution is real but disconnected from the experiments in a way that prevents acceptance in its current form. A revised version with proper baselines, broader evaluation, and honest discussion of the per-class results would be substantially stronger.

MY FINAL SCORE: <score>4.5</score>
MY FINAL DECISION: <decision>Reject</decision>