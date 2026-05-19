- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5
Now I have all the information I need. Let me synthesize the final review.

## Summary

This paper proposes MARS, a framework that learns a latent representation of multi-step action sequences via a conditional VAE augmented with an action transition scale and environmental dynamics prediction, to handle "fragmentary interaction" (missing/delayed states) in real-time control. The method converts multi-step action selection into single-step latent policy learning. It is applied to TD3 and evaluated on MuJoCo and navigation tasks with constant and random interaction intervals, plus one real-world snake robot task.

## Strengths

- **Formalization of fragmentary interaction as FIMDP**: Section 2.2 introduces an explicit MDP variant that models the sparse observation pattern and multi-step action sequences required when states are lost, providing a principled target for RL methods beyond ad-hoc action-repeat heuristics.

- **Scale-conditioned VAE with dynamics prediction**: The sc-VAE (Section 3.1) jointly models multi-step actions and their transition scale η, augmented with an unsupervised environmental dynamics prediction loss (Section 3.2). The ablation study (Figure 8a, described qualitatively) indicates both components contribute to performance, supporting the claim that MARS produces semantically meaningful latent representations.

- **Empirical advantage over baselines in simulation**: In constant and random fragmentary interaction settings, MARS-TD3 consistently outperforms frameskip and advance-decision baselines across six simulated environments (Figures 5, 6). The paper reports that MARS "is comparable to the ideal TD3 even in long-interval interaction settings, and even better on Hopper and Walker" (Section 4.2), suggesting the latent representation is effective.

- **t-SNE visualization of latent space**: Figure 8b provides qualitative evidence that latent actions with similar environmental impact cluster together, supporting the claim of semantic smoothness in the learned representation space.

## Weaknesses

### Fatal
None.

### Major

**1. Real-world experiment (RQ2) provides no quantitative evidence.** Section 4.3 describes a snake robot control task and states: "The result is shown in figure 7. We will release the robot control system in the near future." There are zero numeric metrics — no success rate, no baseline comparison in the real-world setting, no ablation of the interaction interval or packet loss rate. Yet the paper's Contribution (4) claims that MARS "significantly improves the performance of real-world high-frequency robot control tasks." This claim is entirely unsupported by the evidence presented. Either quantitative results must be provided, or the real-world claim should be removed from the contributions.

**2. The generalization claim (RQ3) is stated without supporting evidence.** Section 4.4 says "We test MARS with popular RL methods on 2dmaze and Mujoco. In summary, MARS can effectively combine with different RL methods." This is a single sentence with no table, no figure, and no quantitative comparison. Since the paper explicitly lists RQ3 as a research question, the answer must be more than an unsupported assertion.

**3. Baseline protocol for random fragmentary interaction is underspecified.** The paper describes baselines as frameskip (repeat last action) and advance decision (output c actions at once). For constant intervals this is clear. For random intervals (Section 4.2, line 188: "longest interval to 10 time steps"), the paper does not specify how the advance decision baseline produces variable-length sequences when the next observation arrival time is unknown. Does the baseline know the interval length in advance? Does it pad with dummy actions? This ambiguity makes it impossible to assess whether the comparison is fair or whether MARS benefits from an implicit advantage in task formulation.

### Minor

**4. Action transition scale conditioning lacks explicit consistency enforcement.** The actor network outputs both $a_\eta$ and $a_z$, which are fed to the decoder. The VAE reconstruction loss includes a $\zeta$ (cumulative action change) term that trains the decoder to produce sequences whose transition scale matches the input $\eta$. However, there is no mechanism ensuring that when the actor outputs a novel $(a_\eta, a_z)$ combination not well-covered by the VAE's training distribution, the decoded sequence's actual transition scale will match $a_\eta$. This is a general concern with VAE-based latent variable models in RL (the policy may explore off-manifold combinations), but the paper does not discuss or mitigate it. Adding an explicit penalty or consistency check would strengthen the method.

**5. State residual prediction assumes additive state spaces.** The dynamics prediction loss (Eq. 6–7) predicts $\delta_{s_t} = s_{t+c} - s_t$. This assumes Euclidean state variables. In MuJoCo environments, state vectors include joint angles which are periodic (modulo $2\pi$), where a simple linear difference is not an appropriate target. The paper does not discuss whether states are pre-processed (e.g., converting angles to sin/cos) to handle this.

**6. "First DRL framework" claim is somewhat overstated.** The paper frames fragmentary interaction as largely unstudied, but prior work on delayed MDPs, action-repetition strategies, and multi-step action prediction (including Ramstedt & Pal 2019, which is cited) addresses closely related settings. The paper's genuine contribution is the *latent representation learning* approach to multi-step actions, not the problem setup. The novelty claims should be calibrated accordingly.

**7. FIMDP formalism includes the policy in the transition function.** Equation (2) defines $\mathbf{K}(s_{t+c}|s_t,u_t) = p(s_{t+c}|s_t,u_t)\pi(u_t|s_t)$, which conflates the environment dynamics with the agent's decision rule. In standard MDP notation, the environment transition is independent of the policy. This non-standard formalism should be clarified or revised.

**8. Ablation study lacks quantitative metrics.** The paper states that "Figure 8 (a) shows that both modules effectively optimize the latent space" but provides no numbers (e.g., reconstruction error, policy return with confidence intervals). The t-SNE visualization (Figure 8b) is qualitative and should be supplemented with a quantitative clustering metric.

### Trivial
None.

## Nice-to-Haves

- Adding a simple RNN-based policy that takes the last received observation and outputs actions in real time would be a meaningful additional baseline for the POMDP-like aspect of the problem.
- Reporting results with confidence intervals over more seeds (e.g., 10 runs instead of 3) would improve statistical rigor.
- Clarifying how the warmup stage duration was chosen and whether it is critical to performance (or whether the representation model could be learned online) would strengthen the method analysis.

## Removed Points

These points were flagged for removal but are retained here with brief justification in case they are useful:

- **Encoder's use of future states as "privileged information"**: The critic raised this as a concern, but the paper explicitly addresses it (line 96): the encoder uses full state sequences only during training (acceptable for representation learning), while the decoder uses only $s_t$ at both train and test time. No train-test mismatch exists in the decoder. **Reason for removal: the paper already addresses this.**

- **"Could MARS be measuring a proxy? / confounders not controlled"**: This was a generic area-of-concern sweep without a concrete anchor in the paper. **Reason for removal: speculative, not grounded in a specific issue.**

- **Missing appendix content / proofs / implementation details**: The reviewer noted missing pseudocode and training details. Per instructions, the appendix is stripped by the parser and exists in the original submission. **Reason for removal: parser artifact.**

- **Typo/formatting nitpicks**: Grammar, punctuation, formatting issues are parser artifacts per instructions. **Reason for removal: parser errors, not author errors.**

- **Strength: "Generality to different RL algorithms"**: The strength finder claimed this as a core strength, but the paper provides no quantitative evidence for it — only one unsupported sentence. **Reason for removal: unsupported claim, not a verified strength.**

- **Criticism about the interesting claim that MARS outperforms ideal TD3 on Hopper/Walker needing an explanation**: The paper offers a plausible explanation (compressing episode length). This is a curiosity, not a weakness. **Reason for removal: the paper does provide an explanation.**

## Novel Insights

None beyond the paper's own contributions. The reviews surface a recurring tension: the paper proposes a well-motivated representation learning approach for a practical problem, but the empirical evaluation is inconsistent — strong in simulation settings (with the caveat of underspecified baselines) but essentially absent for the real-world claim that features prominently in the contribution list. The transition scale consistency concern, while real, is a standard VAE-off-manifold issue rather than a novel structural flaw.

## Suggestions

1. **Provide quantitative real-world results or remove the claim.** A single figure with "the result is shown" and "we will release" is insufficient. Report success rates, comparison to baselines on the same physical task, and relevant metrics.

2. **Specify the evaluation protocol for random intervals.** State clearly whether the random interval length is known to the agent at decision time, and how the advance decision baseline handles variable-length sequences. Without this, the experimental results for random FIMDP are difficult to interpret.

3. **Support or remove the generalization claim (RQ3).** A dedicated research question deserves at minimum a table showing comparative performance across different RL algorithms.

4. **Add a discussion of off-manifold generalization** for the VAE decoder, and consider a simple auxiliary loss or constraint that encourages the actor's $a_\eta$ output to be consistent with the decoded sequence's actual transition scale.

5. **Address the state residual prediction assumption** — clarify whether state variables are pre-processed (e.g., sin/cos encoding for angles) to make the additive residual formulation appropriate.
