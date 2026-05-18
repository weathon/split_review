Now I have a thorough understanding of the paper. Let me write the consolidated review.

## Summary

The paper proposes MoE-F, an algorithm that uses Wonham-Shiryaev stochastic filtering to dynamically combine LLM expert predictions for time-series tasks. The key idea is to frame the online expert selection problem as a continuous-time HMM and derive filtering equations (Theorem 1) that optimally update mixture weights based on each expert's running loss. The algorithm operates in three steps: (1) parallel filtering to obtain expert-specific weight estimates, (2) softmin aggregation of filter outputs, and (3) a heuristic update of the HMM transition rate matrix Q. Empirical results on a Financial Market Movement (FMM) task show a 48.5% relative F1 improvement over the best individual expert (0.52 vs. 0.35).

## Strengths

- **Novel application of stochastic filtering to online LLM gating**: The paper's core idea — using the Wonham-Shiryaev filter to adaptively combine LLM predictions in an online time-series setting — is genuinely novel and departs from static learned-routing MoE approaches. The three-step architecture (parallel filters → softmin aggregation → Q-matrix update) is thoughtfully structured.

- **Large empirical gains on a real-world task**: On the NIFTY FMM dataset with 317 test days, MoE-F achieves F1=0.52 against the best individual expert's 0.35 (Table 1). The ablation experiments (Tables 2, 3) confirm consistent improvements and demonstrate that the filter dynamically re-weights experts, with per-class decomposition showing the method mitigates degenerate experts (e.g., the "+nifty" adapter that always predicts Neutral).

- **Plug-and-play design**: The algorithm requires no expert retraining and can be applied as a "harness" over any set of pre-trained LLMs, with the ability to add/remove experts online (Section 7). This is a genuine practical advantage over learned routing approaches.

- **Auxiliary theoretical guarantees for Q-matrix update**: Propositions 1 and 2 provide formal guarantees about the perturbation used in Step 3 (invertibility, row-stochasticity, KL-bound stability). While narrow in scope, these are non-trivial and correctly proved.

## Weaknesses

### Fatal
None.

### Major

- **Binary cross-entropy loss used for a 3-class classification problem.** The theoretical development (Theorem 1 and Equation 4) is built on the binary cross-entropy loss: ℓ(y,ŷ) = y log ŷ + (1-y) log(1-ŷ). However, the FMM task has three classes (Fall, Neutral, Rise), as shown in the test statistics (Table 1) and the per-class breakdown (Table 3). The paper never explains how a binary loss is applied to a 3-class problem, nor how the filtering equations (derived specifically for the binary CE case) remain optimal when applied to a non-binary setup. If a one-vs-rest binarization was used, it should be stated; if a categorical cross-entropy was used instead, the core theoretical guarantee no longer applies to the implementation. This gap makes the connection between theory and experiment unverifiable.

- **Theorem 1 is asserted without derivation or verification of the observation model structure.** The theorem claims closed-form optimal filtering equations for the hidden Markov process w_t given observations ℓ_t^(n). The Wonham-Shiryaev filter requires the observation process to satisfy a specific diffusion structure (dZ_t = h(w_t) dt + dV_t with independent Wiener noise). The paper provides no derivation showing that ℓ_t^(n) (which depends on Y_t, which itself shares the same Brownian motion W_t driving the signal) satisfies this required structure. The theorem is simply stated, and the filtering equations are presented as given. For a paper whose central theoretical contribution is this optimality guarantee, the lack of justification undermines trust in the core claim. The algorithm's filtering step may still perform well empirically, but the "optimality" label is unsubstantiated.

### Minor

- **Temporal indexing ambiguity between theory and experiments.** The continuous-time model (Eq. 1) indexes predictions and targets concurrently: the drift at time t uses F(x_{[0:t]}) and contributes to Y_t. The experiment description (line 569) states that experts predict "the market movement the following day (i.e., t+1)" from data up to day t. The paper does not clearly reconcile these two temporal conventions. The reviewer's concern about "look-ahead bias" is overstated for the cross-entropy case (the B function in Algorithm 1 line 6 does not actually depend on Y_t in the cross-entropy case used in experiments — see Eq. 7 definition), and the filter does not appear to use future information improperly. However, the lack of a clean mapping from the continuous-time formalism to the discrete daily data makes it unnecessarily difficult to verify the correctness of the implementation, and some of the notational choices (e.g., writing ℓ(Y_t, f^(n)(x_{[0:t]})) where the experimental prediction is for t+1) are confusing.

- **Missing comparison to simple online ensemble baselines.** The experiments compare against individual experts but not against obvious lightweight alternatives such as uniform averaging of expert predictions, exponentially-weighted (Hedge) aggregation with a fixed learning rate, or follow-the-leader. Since the softmin aggregation in Step 2 already provides a simple ensemble mechanism, ablating the contribution of the filtering step (Step 1) is necessary to isolate whether the improvement comes from the stochastic filter or from the aggregation. The large reported gains (17% absolute F1) are less convincing without this control.

- **No uncertainty quantification on reported results.** All numbers are given as point estimates (means over 3 seeds for open-weight models, single run for GPT-4o). No standard deviations, confidence intervals, or significance tests are reported. Given the small test set (317 days) and the inherent variance in LLM outputs, it is impossible to assess whether the 0.52 F1 is statistically distinguishable from, say, 0.40.

### Trivial
- The perturbation equation (Eq. 15) has a self-referential definition: P_t^α ≜ (1-α)P_t^α + α I_N. This appears to be a typo — it should presumably be P_t^α ≜ (1-α)P_t + α I_N.
- The score equation (Eq. 11) uses s_m instead of s_n, an apparent notation slip.

## Nice-to-Haves
- A sketch of the derivation of Theorem 1 in an appendix, verifying that ℓ_t^(n) satisfies the required Wonham-Shiryaev observation structure.
- Comparison against a simple online learning baseline (e.g., Hedge with fixed learning rate) to ablate the filter's contribution.
- Standard deviations or bootstrap confidence intervals for all reported metrics.
- Clarification of how the binary CE loss is applied to the 3-class FMM task, or a binarized version of the task.

## Removed Points

- **Look-ahead bias through B_{t-1}^{(n)}(Y_t) (from Harsh Critic Point 1, partially)**: The critic claims that using Y_t in B_{t-1}^{(n)}(Y_t) introduces future information. However, for the cross-entropy loss case used in the experiments, B_t^{(n)}(y_t) does not actually depend on y_t at all — the definition (Eq. 7, else branch) is simply −log(f/(1−f)), a function of the expert prediction only. The critic did not notice this conditional compilation in the paper's helper function definition. The temporal indexing ambiguity is real and kept above; the specific "look-ahead" accusation is factually incorrect for the cross-entropy setting.

- **"Double use of Y_t" claim (from Harsh Critic Other Observations)**: The critic claims that Y_t is used "both inside the filter update" and in scoring. For the cross-entropy case, the filter update does not actually use Y_t (B does not depend on Y_t, and the ΔL uses losses from t-1 and t-2). The scoring uses Y_t after it has been observed, which is standard sequential prediction. This point is factually incorrect.

- **Criticism that the paper does not include an appendix/proof of Theorem 1 in the appendix**: The parser strips appendices from all papers. A derivation sketch would be valuable, but the absence of an appendix section is an artifact of the review format.

- **Claim that the paper should cover additional domains/tasks**: The paper is evaluated on a specific financial task with ablations. Requesting broader benchmarks is scope creep.

- **Generic strengths from Strength Finder**: "Plug-and-play design with no expert retraining required" is kept above as a genuine strength. However, the Strength Finder's claim that "Propositions 4 and 5 (Section 4.1-4.2)" guarantee stability is referencing proposition numbers that don't exist in the paper (the actual propositions are labeled 1 and 2). The strength about theoretical optimality is weakened by the missing derivation, so it is kept only in qualified form.

- **Criticism about missing related works**: This is removed per instructions as I cannot verify external coverage.

## Novel Insights

Beyond the paper's own contributions, a genuinely novel observation emerging from this work is the demonstration that stochastic filtering theory — normally confined to signal processing and control — can be productively applied to the problem of dynamically routing among LLM experts without retraining. The per-class analysis (Table 3) offers a subtle insight: the filter's advantage comes less from finding a single "best" expert and more from suppressing degenerate experts (those that collapse to predicting only the majority class) while preserving diversity across market regimes. This suggests that the filter acts as a form of online regularization against expert collapse, which is a different benefit than what static routing or standard ensemble methods typically provide.

## Suggestions

1. **Reconcile the loss function with the 3-class task**: Either binarize the FMM task (e.g., Rise vs. Fall, dropping Neutral) so the binary CE theory applies directly, or extend the theoretical development to handle multi-class cross-entropy and explain how the filtering equations change.
2. **Add a derivation sketch for Theorem 1** showing that ℓ_t^(n) satisfies the Wonham-Shiryaev observation structure, or at minimum cite the specific result from the filtering literature that guarantees the SDE form under the paper's assumptions.
3. **Add simple ensemble baselines**: Uniform averaging, exponentially-weighted aggregation (Hedge), and an ablation running Step 2 alone (softmin on raw expert predictions without the filter) to isolate the filter's contribution.
4. **Report error bars** (standard deviations or confidence intervals) for all metrics.
5. **Clarify the temporal indexing**: Provide a clear table showing how continuous-time quantities (t, Y_t, f^(n)(x_{[0:t]}), ℓ_t) map to discrete-time quantities in the experiment, resolving whether the prediction at step t targets Y_t or Y_{t+1}.

## Score and Decision

**Summary**: The paper proposes a genuinely novel approach to online LLM ensembling using stochastic filtering, and the empirical results on a real financial task are striking. However, the paper has two major, unresolved weaknesses: (1) the theoretical optimality claim (Theorem 1) is presented without derivation, and (2) the loss function used in the theory (binary CE) does not match the experimental setup (3-class classification) without explanation. These gaps sever the link between the paper's theoretical apparatus and its empirical evaluation. The missing baselines and lack of error bars are secondary but further weaken the empirical contribution. The paper would need substantial revisions to be acceptably rigorous.

MY FINAL SCORE: <pineapple>5.0</pineapple>
MY FINAL DECISION: <orange>Reject</orange>