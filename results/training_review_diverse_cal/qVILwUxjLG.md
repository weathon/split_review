Now I have all the information needed. Let me produce the consolidated review.

## Summary

**Score based on assessment:** This paper proposes NeuralPES, a deep neural network-based non-stationary contextual bandit algorithm that uses ensemble sampling with sequence models and predictive models to prioritize collecting information with enduring value. The algorithm achieves strong empirical results on two real-world recommendation datasets (MIND, KuaiRec), outperforming window-based variants of Neural Ensemble, Neural LinUCB, and Neural Linear. The paper also provides theoretical analysis of a linearized version (LinPS) that connects the algorithm's regret to the durability of information. The core idea is interesting and the empirical results are promising, but the paper has several weaknesses in presentation and experimental completeness.

## Strengths

- **Strong empirical performance on real-world non-stationary datasets**: NeuralPES achieves the highest average CTR on MIND (0.1552 vs. 0.1513 for best baseline Window Neural Ensemble) and highest average rating on KuaiRec (1.3421 vs. 1.3172) as shown in Table 1, with improvements holding across 20 random seeds.

- **Theoretical evidence linking regret to information durability**: The regret analysis for LinPS (Theorem 1) shows the bound depends on mutual information terms that capture how long information persists, and the corollaries demonstrate that regret approaches zero when information is not durable (e.g., AR(1) with γ_i→0, abrupt changes with q_i→1). This formally substantiates the claim about lasting-information prioritization.

- **Ablation studies verify key design components**: Removing the predictive model (Neural Sequence Ensemble) causes a performance crash on KuaiRec (Figure 5), confirming the predictive component is essential, not just architectural overhead. The regularization for loss of plasticity also shows consistent improvement.

- **Scalable architecture validated on high-dimensional features**: The algorithm is deployed on features of dimension 100 (MIND) and up to 1588/283 (KuaiRec) using a single A100 GPU, demonstrating that NeuralPES addresses the scalability limitation it identifies in prior predictive sampling approaches.

## Weaknesses

### Fatal
None.

### Major

- **Missing comparison to predictive sampling (Liu 2023)**: The paper's narrative centers on recovering the benefits of predictive sampling while scaling to deep neural networks, yet no variant of predictive sampling is included as a baseline. The justification that it "does not efficiently scale" does not excuse omitting it from the synthetic AR(1) logistic bandit experiment (only 10 actions, 10-dimensional features), where a linear implementation would be computationally trivial. Without this comparison, the empirical results show only that NeuralPES beats window-based neural algorithms; they do not directly validate that NeuralPES retains the lasting-information benefits of predictive sampling or closes the performance gap over established non-stationary methods. This is the paper's central premise and it is left unverified.

### Minor

- **Inconsistency between text description and pseudocode in the selection step**: The text (lines 240–242) states the agent uses the *m*-th predictive model (singular) to predict the reward, but Algorithm NeuralPES (line 266) sums over *all* i=1..M predictive models: $A_t \in \argmax_{a} \sum_{i=1}^M f^{\mathrm{pred}}(w^{\mathrm{pred}}_{i,t}; (\hat{w}_{m,t+2} \odot b(\psi_m; C_t, a))$. The base network $\psi_m$ and future weight $\hat{w}_{m,t+2}$ come from the sampled particle m, but the predictive model weights are averaged across all particles. This averaging operation is not described in the main text. While the pseudocode itself is unambiguous enough to implement from, the discrepancy between the text (which implies a single-model decision) and the pseudocode (which averages) needs to be resolved, and the motivation for averaging should be discussed.

- **Regret bound rate is not contextualized**: Theorem 1 gives $\mathrm{Regret}(T) \leq \sqrt{\frac{d}{2}T[I(\theta_2;\theta_1) + (T-1)I(\theta_3;\theta_2|\theta_1)]}$. For a general reversible Markov chain, $I(\theta_3;\theta_2|\theta_1)$ is a positive constant, making the bound $O(T)$ (linear) in the non-stationary case. The paper discusses the stationary special case (recovers $\sqrt{T}$) and the i.i.d. extreme (zero regret), but does not explicitly state that the general bound is linear or discuss why this is the expected behavior in non-stationary bandits. A brief discussion relating the bound to known minimax rates for non-stationary bandits (e.g., total-variation bounds) would help readers properly interpret the result. (Note: the average regret bound $\overline{\mathrm{Regret}} \leq \sqrt{\frac{d}{2} I(\theta_3;\theta_2|\theta_1)}$ is a constant, so per-step regret does not grow unboundedly — this is a meaningful property that should be highlighted alongside the caveat about cumulative regret.)

- **Hyperparameter values not reported**: The number of gradient steps $\tau, \tau_{\mathrm{seq}}, \tau_{\mathrm{pred}}$, the replay buffer size $K$, the sequence length $L$, and learning rates are listed as inputs to the algorithms but their specific values in the experiments are not reported. Reporting these and noting sensitivity would improve reproducibility.

### Trivial
- The "select" line in Algorithm NeuralPES has a mismatched closing parenthesis (minor LaTeX issue from parsing).

## Nice-to-Haves
- Disentangling the two-step-ahead targeting from the predictive model by comparing against a one-step-ahead version ($\hat{w}_{m,t+1}$ instead of $\hat{w}_{m,t+2}$) would isolate whether the *two-step* horizon drives the improvement.
- A formal link between the LinPS theory and the actual NeuralPES algorithm (e.g., showing under what conditions NeuralPES approximates LinPS) would make the theoretical section more directly relevant.
- Per-day or per-week regret breakdowns on the real-world datasets would visualize how NeuralPES adapts to specific non-stationarity patterns (e.g., day-of-week seasonality in MIND).
- Diagnostics of the predictive model (e.g., how often $\hat{w}_{m,t+2}$ differs from $\hat{w}_{m,t+1}$, or how predictions correlate with actual reward changes) would strengthen the interpretation of the ablation.

## Removed Points
These points from the reviews were removed for the following reasons:
- *"Statistical testing: confidence intervals or pairwise t-test results"* — The paper reports standard errors over 20 seeds, which is the standard practice for this setting. Confidence intervals do not change the believability of the contribution.
- *"NeuralPES is the first non-stationary contextual bandit learning algorithm that is scalable... and effectively explores"* — Generic phrasing removed from strengths; the concrete empirical results speak for themselves.
- *"The selection step also contains a minor notation issue... If the intention is truly to use a single sampled particle throughout, the sum is either a typo or unnecessary"* — This is the same issue captured under the pseudocode-text inconsistency above.
- *"The explanation given ('environment changes are mostly unpredictable and the predictive model determines whether information lasts') is not backed by any analysis"* — While true, this is a minor interpretive point; the main ablation result (predictive model is crucial) is clear and valid regardless of the specific explanation given.
- *"The paper does not consider context and state evolution as a result of actions"* — The paper explicitly scopes this out in the conclusion as future work.
- *"Attention mechanisms can be potentially leveraged"* — A suggestion for future work, not a weakness.
- *Various claims about "missing appendix" or "missing proofs"* — These sections were stripped by the parser; they exist in the original submission.

## Novel Insights

The reviews reveal a useful perspective that the paper itself does not fully articulate: the pseudocode's averaging of predictive model weights (i=1..M) while anchoring the base network and future-weight rollout to a single sampled particle m represents a subtle but potentially important design choice. It combines the exploration structure of ensemble sampling (the sampled particle determines *what* to target) with the variance reduction of ensemble averaging (all predictive models contribute to the final decision). This hybrid is architecturally different from standard Thompson-sampling-style ensemble approaches, and the paper would benefit from explicitly motivating it. Whether this design is intentional or an artifact of the pseudocode is not clear from the current text.

## Suggestions

1. **Resolve the pseudocode-text inconsistency**: Either update the text to describe the averaging over predictive models (and explain its motivation), or change the pseudocode sum over i to use only the sampled m-th predictive model, whichever matches the intended algorithm.
2. **Add a predictive sampling baseline to the synthetic experiment**: Even a linear implementation on the AR(1) logistic bandit (10 actions, 10-dim features) would directly validate whether NeuralPES recovers the benefits of predictive sampling at minimal computational cost.
3. **Contextualize the regret bound rate**: Add a sentence or two acknowledging that the cumulative bound is O(T) in general non-stationary settings (a standard expectation), and highlight that the average regret bound is a finite constant, which has meaningful implications for long-run performance.
4. **Report experimental hyperparameters**: Provide the actual values used for $\tau, \tau_{\mathrm{seq}}, \tau_{\mathrm{pred}}, K, L$, and learning rates in the main text or appendix.

## Score and Decision

**Originality**: The combination of neural ensembles with two-step-ahead predictive modeling for lasting-information prioritization is novel, though it builds directly on Liu 2023's predictive sampling concept.  
**Importance**: Addressing non-stationarity in large-scale contextual bandits is practically important, and the real-world dataset results support the relevance.  
**Claims**: The empirical claims of superior performance are well-supported. The claim about "prioritizing lasting information" has theoretical support for the linearized version and indirect empirical support from ablations, but the missing predictive sampling baseline weakens the central narrative.  
**Soundness**: The experimental methodology (20 seeds, standard errors, real-world datasets, ablation studies) is sound. The theoretical analysis is standard information-theoretic regret bounding.  
**Clarity**: The algorithm is clearly described in pseudocode, but the text-pseudocode discrepancy and the lack of regret-rate contextualization reduce clarity.  
**Value**: With revisions addressing the missing baseline and presentation issues, this paper would be a solid contribution. In its current form, the core empirical result is strong but the claim about scaling predictive sampling is unverified.

MY FINAL SCORE: <pineapple>6.0</pineapple>
MY FINAL DECISION: <orange>Accept</orange>