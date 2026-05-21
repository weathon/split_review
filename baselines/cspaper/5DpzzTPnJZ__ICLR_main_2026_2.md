---
job_id: fa8433d6-afdd-49e0-8d3e-8ba3b47ab1d9
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 5DpzzTPnJZ.pdf
paper: The Rank and Gradient Lost in Non-Stationarity: Sample Weight Decay for Mitigating Plasticity Loss in Reinforcement Learning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is directly about reinforcement learning, optimization dynamics, and learning theory for plasticity loss, all of which are squarely within ICLR scope.

## Minimum Quality
Pass ✅. The submission contains the expected scientific components, including abstract, introduction, related work, theory/method, experiments, quantitative results, and conclusion. While I found several important issues in the theory and empirical positioning, they are weaknesses for review rather than grounds for desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, reviewer-targeting instructions, or other manipulative content in the provided paper text.

# Expected Review Outcome:
## Summary
This paper studies plasticity loss in deep RL through a theoretical lens, focusing on non-stationarity from replay distribution shift and bootstrapped targets. The authors argue that plasticity loss is associated with two mechanisms, NTK rank degeneration and a $\Theta(1/k)$ decay in gradient magnitude, and propose a replay-sampling strategy, Sample Weight Decay (SWD), that increases the sampling probability of recent transitions to counteract this decay. Empirically, the method is evaluated on TD3, Double DQN, and SAC with SimBa across MuJoCo, ALE, and DMC tasks.

## Strengths
The paper tackles an important and timely problem. Plasticity loss in deep RL has become a real concern, especially for long-horizon training and large replay buffers, and a replay-level intervention is a sensible angle because it is potentially cheap and compatible with many existing methods.

The proposed method is simple and easy to implement. Algorithm 1 is straightforward, has very few hyperparameters, and can plausibly be integrated into standard replay-based pipelines without architectural changes. That practical simplicity is a real plus.

The empirical scope is reasonably broad. The paper tests SWD with three algorithmic families, TD3, Double DQN, and SAC, over continuous control, Atari, and DMC benchmarks. Even though I have concerns about some of the comparisons, the breadth is better than many papers in this space.

Some of the visual empirical evidence is compelling. In **Figure 1**, the aggregate reliable metrics show a consistent upward shift for the SWD variants over the corresponding baselines across the three benchmark groups. This is a useful summary figure because it communicates that the effect is not confined to one algorithm or one environment. Likewise, **Figure 2** shows fairly consistent gains for TD3 on several MuJoCo tasks, especially Ant and Humanoid, where the gap appears sustained over much of training rather than being a transient early-training effect. **Figure 3** similarly suggests gains for Double DQN on the ALE tasks tested.

I also appreciated the attempt to include mechanistic diagnostics beyond reward curves. **Figure 5(b)** and **Figure 5(c)** try to connect the proposed replay weighting to gradient norm and GraMa, which is directionally the right thing to do if the paper wants to argue it is addressing plasticity rather than merely changing exploration or sample efficiency. The approximate implementation is also a nice practical touch; **Table 2** indicates that the bucket-based approximation can recover nearly the same return as exact SWD while keeping runtime close to uniform sampling.

## Weaknesses
I have several substantial concerns, most of them centered on the gap between the stated theoretical claims and what is actually established in the paper.

1. **The theoretical story is much weaker and less clean than the paper claims.**  
   The abstract and introduction frame the work as a theory-driven explanation of plasticity loss, attributing it to NTK rank collapse and $\Theta(1/k)$ gradient decay. However, in the main paper, the NTK part in **Section 4.1** is mostly high-level discussion rather than a formal result. I do not see a theorem, proposition, or quantitative statement in the main paper that actually proves NTK rank collapse occurs under RL non-stationarity, or that links rank collapse to plasticity loss in the concrete training setting used later. The section cites general NTK convergence literature and then asserts that random initialization guarantees no longer hold once RL reuses previous iterates as initialization. That intuition is not the same as a formal characterization of degeneration. So one of the two headline mechanisms is, at least in the main paper, not really derived.

2. **The central gradient theorem, Theorem 3 and Equation (4), has indexing and derivational inconsistencies that make it hard to trust as stated.**  
   In **Page 6, Equation (4)**, the gradient decomposition is written as
   \[
   \nabla \mathbb{E}_{\mu_h^k}\left[(f-\mathcal{T}_h\hat f_{h+1}^k)^2\right]\big|_{\hat f_h^{k-1}}
   = \frac{1}{k}\nabla \mathbb{E}_{\hat d_h^k}\left[(f-\mathcal{T}_h\hat f_{h+1}^{k-1})^2\right]\big|_{\hat f_h^{k-1}}
   + \mathbb{E}_{\mu_h^k}\left[\nabla f^2|_{\hat f_h^{k-1}}\cdot(\mathcal{T}_h\hat f_{h+1}^{k-1}-\mathcal{T}_h\hat f_{h+1}^{k})\right].
   \]
   But in the proof in **Appendix B.3 (Pages 16-17)**, the intermediate steps switch indices in a suspicious way, including terms such as $\mathcal{T}_h \hat f_h^{k-1}$ where one would expect $\mathcal{T}_h \hat f_{h+1}^{k-1}$. There is also a mismatch between the derivative of $(f-\cdot)^2$, which should involve $2(f-\cdot)\nabla f$, and the final presentation involving $\nabla f^2$ in Equation (4). This is not a cosmetic issue. Since the whole method is justified as compensating a specific $\Theta(1/k)$ gradient decay, ambiguity in the exact decomposition matters.

3. **Even taking Theorem 3 at face value, the jump from the theorem to SWD is not rigorously established.**  
   The paper says SWD "neutralizes the $\frac{1}{k}$ attenuation" in **Section 5**, but this is more asserted than shown. The theorem concerns the initial gradient at iteration $k$ for a simplified finite-horizon FQI objective, evaluated specifically at the previous minimizer. SWD instead changes replay sampling probabilities over the entire buffer during practical deep RL training with TD3, SAC, and DDQN. There is no theorem showing that the proposed weight schedule yields a non-decaying gradient lower bound, no analysis of the bias introduced by changing the replay distribution, and no derivation connecting the linear age-based weights in Algorithm 1 to the exact $\frac{1}{k}$ factor in Equation (4). In short, the method is inspired by the theorem, but not tightly derived from it.

4. **The theory-to-experiment gap is large.**  
   The main theory is formulated for a simplified episodic finite-horizon FQI setting in **Section 4**, whereas the experiments are on TD3, SAC, and Double DQN, mostly in standard infinite-horizon discounted settings with target networks, delayed updates, policy learning, entropy regularization, and large nonlinear function approximation. The paper explicitly says the framework can be extended, but those extensions are not established in the main paper in a way that supports the empirical claims. This matters because a theory paper can simplify, but if the method is sold as "theoretically grounded" for the practical algorithms tested, the bridge needs to be much tighter.

5. **There are several presentation and notation problems in the mathematical parts, including some that affect correctness.**  
   A few examples:
   - In **Theorem 2 / Equation (3) on Page 5**, the greedy policy is defined as $\pi_{\hat f,h}$, but the bound later uses $V_1^{\pi_f}(x)$ and then an expectation under $\pi_j$, which appears to be a typo for something else.  
   - The first square-root term in **Equation (3)** has a dangling plus sign inside the radical, suggesting a typesetting or algebra issue.  
   - In the definition of $\hat d_h^{\pi^{k+1}}$ on **Page 4**, there is a double comma in $\mathbb{I}\{s=s_h^{k+1},,a=a_h^{k+1}\}$ and the notation fluctuates between $\hat d_h^{\pi^{k+1}}$ and $\hat d_h^k$.  
   - Theorem 1 states convergence as $|\mathcal D_h^k| \to \infty$, but in this setup the replay buffer size is tied to the number of episodes, and the probabilistic assumptions needed for this convergence under nonstationary data collection are not stated clearly.  
   On their own, typos happen. But here they occur in the core mathematical claims, and that reduces confidence in the technical argument.

6. **The paper’s use of GraMa is internally inconsistent.**  
   In **Section 6.3 on Page 9**, the text states: “a larger GraMa value indicates a weaker learning capability of the neural network.” However, in **Appendix C.1 on Page 19**, GraMa is described as a metric where “higher scores correspond to greater neural plasticity.” Those are opposite interpretations. Since GraMa is a central diagnostic used to claim that SWD alleviates plasticity loss, this contradiction is not minor. The authors need to resolve which direction of the metric corresponds to more plasticity and ensure all figures and claims are interpreted consistently.

7. **The empirical comparison set is not strong enough for the paper’s claims, especially the stronger claims of generality and state of the art.**  
   The most immediate missing baselines are recency-oriented replay baselines that are simpler and more directly related to SWD than PER. For instance, a smaller replay buffer, a sliding-window buffer, recent-only sampling, or a mixture of recent and uniform replay would be natural controls. Without them, it is hard to tell whether the gains come specifically from the proposed linear age weighting, or simply from emphasizing recent data in any form. This is especially important because the method is conceptually close to a family of replay heuristics, not just to PER.

8. **Claims about comparison to other plasticity methods are too broad relative to the evidence shown.**  
   The paper repeatedly emphasizes orthogonality to existing plasticity-preserving methods and uses phrases like “SOTA performance” in the abstract and introduction. But the direct comparison in **Figure 8** is only on **Humanoid Run**, not across the broader suite. That is not enough to support general superiority over the existing plasticity literature. At most, the paper shows a promising result on one hard environment.

9. **The figures support some performance gains, but they also reveal variance and non-uniformity that the text downplays.**  
   For example, in **Figure 2(e) Hopper**, the gain is not consistently strong and the curves remain noisy. In **Figure 3**, the performance improvement seems clearer on Phoenix and DemonAttack than on Breakout, where the practical gap looks smaller. This does not invalidate the method, but it does undercut the stronger “consistently delivers SOTA performance” framing. The paper would be stronger with more task-level quantitative summaries, not just selected curve narratives.

10. **Some of the tabular evidence raises questions about robustness rather than fully resolving them.**  
   **Table 12** shows a broad hyperparameter sweep, which is useful, but the standard deviations are large across many settings, and the mean returns vary meaningfully. I would not call this “low sensitivity” without additional analysis. Similarly, **Table 13** is used to argue linear decay is preferable to exponential or polynomial decay, but this is demonstrated on one task only, Humanoid Run, so the conclusion is narrower than the text suggests. Finally, **Table 2** supports the efficiency claim for the approximate sampler, but again only on one environment.

11. **The discussion of why PER performs poorly relative to SWD is not fully convincing.**  
   In **Section 6.1**, the paper contrasts SWD with PER and states that PER “demands nearly several times more training time” while bringing limited gains. But PER and SWD optimize very different notions of sample utility. If the core claim is about plasticity, then stronger mechanistic evidence is needed to show that SWD’s benefit is indeed due to preserving learnability rather than changing the target distribution in a favorable way for the tested tasks.

12. **Some claims are overstated relative to the actual support.**  
   Examples include “unified theory,” “formally characterizing the two culprit factors,” and “general remedy to plasticity loss.” The paper has interesting ideas and useful experiments, but the current main-paper theory does not fully justify that level of generality.

## Questions
1. Please carefully restate and correct **Theorem 3 / Equation (4)**. In particular, can you provide a notation-clean derivation showing exactly how the gradient at $\hat f_h^{k-1}$ decomposes, with all indices consistent, and explain whether the second term should involve $2(f-\cdot)\nabla f$ or $\nabla f^2$? This would substantially affect my confidence.

2. Can you clarify the status of the NTK claim in **Section 4.1**? Is there a formal theorem in the main paper that proves rank degeneration under RL non-stationarity, or is this section intended as motivation only? Right now the paper presents NTK degeneration as a derived mechanism, but the main text reads more like intuition plus prior results.

3. The theory is developed for simplified FQI, but the experiments are on TD3, SAC, and DDQN. Can you explain more concretely which parts of the theory are expected to transfer to actor-critic and target-network settings, and which parts are only heuristic inspiration? A short, precise statement of scope would help.

4. Please resolve the contradiction in the interpretation of **GraMa** between **Page 9** and **Appendix C.1**. Which direction indicates higher plasticity, and do the interpretations of **Figures 5 and 6** remain correct after that clarification?

5. A crucial missing empirical question is whether SWD beats simpler recency baselines. Could you provide comparisons against at least one or two of the following: recent-only replay, fixed-size sliding-window replay, smaller replay buffer, or a mixed recent-plus-uniform sampler? Positive results there would greatly strengthen the claim that the proposed weighting schedule matters beyond generic recency bias.

6. Since SWD changes the replay distribution, is there any importance correction or argument showing that the induced bias does not harm value estimation? If no correction is used, please explain why the bias-variance tradeoff is favorable and under what conditions.

7. For the comparison against other plasticity methods in **Figure 8**, can you provide evidence beyond a single environment? Right now that result is suggestive, but not enough to support broad superiority or “orthogonality” claims.

8. Could you provide more task-level quantitative summaries, not only aggregate metrics and learning curves? This is particularly relevant for assessing whether the improvements are robust or driven by a subset of environments.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
I do not see a specific ethics issue that requires escalation based on the content presented in the main paper.

## Soundness Rating
2: fair. The paper contains a plausible method and a reasonably broad empirical evaluation, but the central theoretical claims are not supported as cleanly as advertised, and there are inconsistencies in the mathematical presentation that weaken confidence.

## Presentation Rating
2: fair. The high-level motivation is understandable, but the exposition in the theory sections has multiple notation, indexing, and interpretation issues, and some claims are overstated relative to the evidence.

## Contribution Rating
2: fair. The replay-weighting idea is practical and the experiments are promising, but the novelty and scientific value are held back by the loose theory-to-method connection and by missing key baselines that would better establish what is actually new.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper addresses an important problem and has a simple, potentially useful method with encouraging empirical results. However, the current version overclaims on the theory side, has several nontrivial technical inconsistencies in its core derivations, and does not include the most important empirical controls for an age-based replay method. With a cleaned-up theoretical presentation and stronger baseline comparisons, my assessment could improve.

## Reviewer Confidence
4: confident. I am confident in the assessment and checked the mathematical and empirical parts carefully, although the paper’s notation issues mean there is still some possibility that a few intended claims are clearer than the current writing makes them appear.