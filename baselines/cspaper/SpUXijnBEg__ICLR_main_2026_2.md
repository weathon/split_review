---
job_id: ab0b6ce6-5762-4ebd-816a-824179982f10
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: SpUXijnBEg.pdf
paper: Direct Optimal Action Learning
main_score_norm: 0.4
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, centered on offline reinforcement learning, policy extraction from learned Q-functions, and expressive generative policies such as diffusion and flow models.

## Minimum Quality
Pass ✅. The submission contains the expected core components, including abstract, introduction, methodology, experiments, quantitative results, related work, and conclusion. While there are important technical, experimental, and presentation issues, they do not rise to the level of an immediate desk rejection.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden instructions, suspicious formatting, or content attempting to manipulate automated reviewing. The appendix notes LLM use for polishing text, but this is disclosed rather than concealed.

# Expected Review Outcome:
## Summary
This paper proposes Direct Optimal Action Learning (DOAL), a framework for offline RL that replaces end-to-end differentiation through behavior-regularized actor-critic objectives with supervised learning toward an optimized target action derived from the Q-gradient. The method is instantiated for Gaussian, flow, and diffusion-style policies, and the paper argues that the BRAC coefficient can be reinterpreted as a trust-region parameter, leading to a batch-normalized action update controlled by a new hyperparameter $\delta$. Experiments on OGBench and D4RL/Adroit compare DOAL variants against AWR/IQL-style baselines, MaxQ-sampling baselines, and some Q-learning/ReBRAC-based variants.

## Strengths
1. The paper addresses a real practical bottleneck in offline RL with expressive policies. For diffusion and flow policies, backpropagating through iterative sampling chains is indeed cumbersome, and the proposed decoupling of target-action construction from policy fitting is a sensible systems-level idea.

2. The paper is broad in empirical scope. It covers multiple policy classes, Gaussian, flow, and diffusion, and multiple value-learning backbones, IQL, Q-learning, and ReBRAC-style regularized Q-learning. That breadth is useful because the claimed contribution is a framework rather than a single algorithm.

3. The central intuition is easy to understand from **Figure 1**. The side-by-side contrast between BRAC on the left and DOAL on the right communicates the intended conceptual simplification well: instead of differentiating through the policy output inside the Q term, the method constructs an $a^{\text{target}}$ and then applies a policy-native behavior loss. This figure is one of the clearer parts of the paper and helps explain why the authors consider DOAL versatile across policy families.

4. The paper makes a useful practical point about MaxQ sampling. The discussion in Section 4 and the ablation in **Table 4** show that $n_{\text{sample}}$ is not a trivial “bigger is better” knob. The empirical trend in Table 4, where performance often peaks at modest sample counts and degrades at large values, is genuinely informative for practitioners working with resampling-based offline RL.

5. The runtime discussion is a welcome addition. **Figure 2** and the accompanying table give a rough accounting of forward/backward calls and wall-clock time. Even though the analysis is simplistic, it at least tries to quantify the computational tradeoff rather than only claiming efficiency qualitatively.

6. On OGBench, the results are at least somewhat promising. In **Table 1**, the total OGBench score improves from IFQL 329 to DIFQL 359, and from TrigFlow 361 to DTrigFlow 368. In **Table 2**, DMFReBRAC reaches the best OGBench total among listed flow variants at 466. These aggregate improvements are not overwhelming, but they do suggest that the idea can help in some settings.

## Weaknesses
1. **The main theoretical bridge from BRAC to DOAL is much weaker than the paper’s framing suggests, and in places the exposition is mathematically inconsistent.**  
   The key claim appears in Proposition 1 on **Page 4**, which shows gradient equivalence between a deterministic BRAC-style objective and a squared error objective whose target is
   \[
   a^{\text{brac\_target}} = a + \frac{1}{2\alpha}\nabla_{a'} Q_\phi(s,a')\big|_{a'=\pi_\theta(s)}.
   \]
   But DOAL does **not** use this target. It instead replaces the gradient evaluation point $\pi_\theta(s)$ by the dataset action $a$, yielding Equation (17) on **Page 5**:
   \[
   a^{\text{target}} = a + \frac{\delta}{\mathbb{E}_{(s',a')\sim \mathcal B}\|\nabla_{a'}Q_\phi(s',a')\|_2}\nabla_a Q_\phi(s,a).
   \]
   This is not a small implementation detail, it is the core algorithmic change. Proposition 1 therefore does not establish equivalence between BRAC and DOAL, only between BRAC and a different target-matching loss whose target depends on $\pi_\theta(s)$. The paper acknowledges “similar but different,” but the rhetorical arc still leans too heavily on Proposition 1 as if it formally justifies DOAL. At present, the justification is mainly heuristic.

   There is also a notation issue in Equation (13). The displayed expression
   \[
   \nabla_\theta \mathcal L_Q(\theta) = \nabla_\theta \mathcal L_{\text{brac\_target}}(\theta) \triangleq \mathbb E[\nabla_\theta(-\alpha \|\pi_\theta(s)-a^{\text{brac\_target}}\|)\_2^2]
   \]
   appears malformed, with the square outside the norm expression in a confusing way. The corresponding appendix proof on **Page 15** uses a different notation, $J_Q$ and $J_{\text{target}}$, and silently treats $a^*$ as fixed with respect to $\theta$. That is exactly the subtle point that needs care, because $a^*$ depends on $\pi_\theta(s)$ through the evaluation point of $\nabla_a Q$. The proof only works because the target is defined so that the derivative is matched algebraically, not because one is minimizing a standard supervised objective with a stop-gradient target. This should be stated precisely; otherwise readers can easily misinterpret what is actually equivalent to what.

2. **Proposition 2 and the trust-region interpretation are sloppier than they should be, and the paper mixes different norm constraints.**  
   In Section 3.2 on **Page 5**, condition 2 says
   \[
   \mathbb E[\|g(s,a)\|_2] = \delta,
   \]
   but the surrounding text repeatedly calls this an “expected squared magnitude,” which would correspond to $\mathbb E[\|g(s,a)\|_2^2]=\delta$. Those are not the same object. Proposition 2 then solves the constraint using the first moment of the norm, while the practical paragraph immediately afterward says, “In practice, we use the batch statistics as estimator, so we have $\mathbb E_{(s',a')\sim\mathcal B}[\|\nabla_{a'}Q_\phi(s',a')\|_2^2]$,” which switches to the **second** moment. However, Equation (17) on **Page 5** goes back to the first moment, not the second moment. This is a concrete mathematical inconsistency, not a stylistic nitpick.

   This matters because the claimed reinterpretation of $\alpha$ as a trust region is one of the paper’s main conceptual contributions. If the trust region is defined through expected norm, then the update scaling differs from the case defined through expected squared norm; the two have different robustness properties and different dependence on heavy-tailed gradient norms. The current presentation leaves it unclear which algorithm was actually run and what quantity $\delta$ should be understood to control.

3. **The empirical gains are modest, inconsistent, and often concentrated in a few tasks rather than demonstrating a robust advantage.**  
   The authors themselves admit this in Section 5.1 on **Page 7**, stating that on OGBench “those are due to one or two tasks that has significant gains” and otherwise performance is “very similar.” That is not a great sign for a framework paper claiming generality.

   Looking at **Table 1**, the aggregate OGBench gain from TrigFlow to DTrigFlow is only 361 to 368, and ETrigFlow is 359, essentially tied within noise. Several task-level changes are tiny or unfavorable, for example antmaze-large-navigate drops from 72 to 63 for DTrigFlow, and some differences are within large standard deviations. On D4RL totals in Table 1, DOAL variants generally do not improve over baselines. For example IFQL total is 592 while DIFQL is 584, and TrigFlow is 584 while DTrigFlow is 577. That undercuts the claim of broad effectiveness.

   In **Table 2**, DMFQL improves OGBench total from 418 to 443 over MFQL, but on D4RL total it drops from 623 to 614. DMFReBRAC improves OGBench to 466, but D4RL only to 630 versus MFReBRAC 614, while still trailing simple-policy ReBRAC(tanh) at 706 by a very large margin. The picture is therefore mixed: DOAL sometimes helps on OGBench, often does little, and does not close the gap to strong simple-policy baselines on D4RL. The paper’s claims should be toned down substantially.

4. **The experimental protocol raises concerns about selection bias and fairness of comparison.**  
   Appendix F on **Page 20** states that hyperparameter choices and initial ablations were performed using four fixed random seeds, while final results use eight different seeds. That is acceptable in principle, but the paper also says, “With IQL, we first choose $n_{\text{sample}}$ on the Trigflow model, then choose $\delta$ on the DTrigflow model. Then, for all our models with IQL value function $n_{\text{sample}}$ and $\delta$ are shared.” This means model-family-specific choices may be transferred to other methods, which is not obviously fair to either the baselines or DOAL variants.

   More importantly, the paper does not clearly describe a validation protocol separate from the reported test environments/scores. The text repeatedly discusses choosing task-specific hyperparameters, and **Table 5** on **Page 23** lists per-task tuned $\delta$, $n_{\text{sample}}$, and $\alpha_{\text{critic}}$. Without a clearly defined validation split or held-out procedure, it is hard to know whether the reported gains partly reflect test-time tuning on benchmark tasks. This is especially problematic because many of the gains are relatively small.

5. **The computational-efficiency claim is only partially substantiated and the accounting in Figure 2 is too coarse to support the broader message.**  
   The table in Section 5.2 on **Page 8** counts forward/backward calls and correlates them with runtime in **Figure 2**, but this treats all calls as roughly equal. That is a strong simplification. In generative policies, the cost of a “policy call” can depend materially on whether it is a one-step network evaluation, a 10-step flow rollout, or part of a backpropagated chain. The paper also notes that MaxQ runs many samples in parallel “so as long as it fits to memory, it has no impact,” which is too optimistic. Memory pressure and batch parallelism are not free, especially for larger models or wider action-sample sets.

   The figure is still useful as a rough sanity check, but it does not convincingly establish general efficiency across policy classes and hardware settings. This matters because efficiency is one of the paper’s headline claims.

6. **Several parts of the mathematical formulation and algorithm specification are underspecified or inconsistent enough to hurt reproducibility.**  
   A few concrete examples:
   - Equation (10) on **Page 4** defines BRAC using $\text{BCLoss}(\pi_\theta(s),a)$, but for diffusion/flow policies the paper later uses losses defined over noisy interpolants, latent variables, and time $t$. The bridge from the generic Equation (10) to those policy-native losses is conceptually important, but the paper does not formalize it cleanly.
   - Equation (16) on **Page 5** keeps a multiplicative $\alpha$ in front of the DOAL loss, yet Section F.3 on **Page 20** claims this parameter “does not matter” and is effectively just learning-rate scaling. If that is the case, the main text should simplify the objective and remove the implication that $\alpha$ remains semantically important.
   - Equations (22) and (23) on **Pages 18** contain broken parentheses/brackets and unclear indexing. As written, they are difficult to parse and not at publication quality. In a methodology paper, malformed core objectives are a serious presentation and verification problem.
   - In DTrigFlow, Equation (21) on **Page 17** uses $a_t=\cos(t)a^{\text{target}}+\sin(t)z$, but the expectation is written over $a_0\sim p(a_0)$ even though the forward corruption appears to start from $a^{\text{target}}$, not $a_0$. This mismatch needs clarification.

7. **The strongest baseline story in the paper is arguably not DOAL, but tuning MaxQ sampling, which weakens the contribution narrative.**  
   Section 4 and **Table 4** show that tuning $n_{\text{sample}}$ can make a very large difference. In fact, some of the empirical uplift over prior work seems to come from building stronger baselines rather than from DOAL itself. That is a useful contribution, but it also means the paper is trying to sell two stories at once: DOAL as a new extraction framework, and MaxQ tuning as a previously neglected but important factor. The results suggest the second story may be at least as important as the first.

   This matters for contribution assessment. If the main practical win comes from stronger baseline tuning, then the incremental value of DOAL itself is smaller than the paper’s framing implies.

8. **The figure-based evidence for stability and method relationships is not as convincing as the text suggests.**  
   The paper relies on **Figure 3** to argue that the batch-normalized gradient norm is “quite stable during training,” supporting the idea that the normalized scaling is roughly constant. But the figure mainly shows several task-dependent trajectories with noticeably different absolute levels, and at least some drift over training. It supports the weaker statement that norms are not wildly exploding, but not the stronger interpretation that normalization removes most tuning burden in a universal way.

   **Figure 4** presents the relationship between MFQL, DMFQL, MFReBRAC, and DMFReBRAC, with arrows labeled by setting $\delta=0$ or $\alpha_{\text{critic}}=0$. This conceptual diagram is helpful, but it also exposes a limitation: DOAL is nested within a broader family where setting $\delta=0$ recovers the baseline. Since the authors explicitly chose not to include $\delta=0$ in tuning, the reported comparisons do not show whether DOAL robustly beats the best point in that nested family. The figure is useful, but it indirectly highlights that the evaluation is not giving DOAL the strongest possible self-comparison.

9. **The paper’s positioning relative to prior work is not sharp enough.**  
   The related work section mentions many diffusion/flow offline RL papers, but the main text does not clearly explain when DOAL should be preferred over existing Q-guided generation approaches, weighted-resampling methods, or one-step actor-critic distillation methods beyond “it is efficient and versatile.” The distinction from methods like Q-guided diffusion and recent actor-critic formulations for diffusion/flow policies is somewhat blurred. The reader is left with a broad idea, “train on optimized target actions instead of differentiating through the sampler,” but the paper does not clearly delimit where this is materially new versus another instance of Q-guided supervised policy extraction.

10. **Presentation quality is below ICLR expectations for a paper making theoretical and methodological claims.**  
   There are many grammatical issues, repeated phrases, malformed equations, inconsistent task names, and typos throughout the main text. A few examples include duplicated text on **Page 2** (“Empirically, in all, we tested over three different Q-value Empirically...”); inconsistent naming like “antssoccer” vs “antsoccer”; “BARC objective” on **Page 4** where BRAC is intended; and notation slippage between $\mathcal D$ and $\mathcal B$, first and second moments of norms, and $a_0$ versus $a^{\text{target}}$ in diffusion equations. These issues do not make the paper unreadable, but they significantly reduce confidence in the technical details.

## Questions
1. The central issue I would want clarified is the exact relationship between Proposition 1 and DOAL. Can the authors give a more formal derivation, approximation argument, or local analysis showing when replacing
   \[
   \nabla_{a'}Q(s,a')\big|_{a'=\pi_\theta(s)}
   \quad\text{with}\quad
   \nabla_a Q(s,a)
   \]
   is justified? Right now the proposition supports a different target than the one actually used.

2. Please clarify the trust-region definition in Section 3.2. Is $\delta$ intended to control $\mathbb E[\|g\|_2]$, $\mathbb E[\|g\|_2^2]$, or something else? The text, proposition, practical implementation paragraph, and Equation (17) currently point in different directions. A precise correction here would materially increase my confidence.

3. What exact hyperparameter-selection protocol was used for the results in **Tables 1 and 2**? Was there any held-out validation procedure, or were benchmark tasks effectively used for model selection? Please state clearly how $\delta$, $n_{\text{sample}}$, and $\alpha_{\text{critic}}$ were chosen and whether the same protocol was applied fairly across all methods.

4. Since DOAL subsumes the baseline at $\delta=0$, why is $\delta=0$ excluded from the search space in the main comparisons? I understand the authors wanted to highlight active use of Q-gradients, but for a fair empirical claim, the most relevant comparison is whether the best DOAL family member outperforms the best baseline-recovering point.

5. Can the authors provide a cleaner and fully specified algorithm for one representative case, for example DMFQL, including where gradients are stopped, how $a^{\text{target}}$ is clipped or projected if actions are bounded, and whether the Q-gradient is computed through the target network or online network? These implementation details matter.

6. The D4RL results suggest that DOAL is often not beneficial unless Q-learning is regularized. Can the authors sharpen the claim of the paper accordingly? For example, do they believe DOAL is mainly useful when $\nabla_a Q$ is well calibrated, and if so, can they provide diagnostic evidence correlating gradient reliability with gains?

7. In **Figure 2**, can the authors provide memory usage and throughput statistics in addition to function-call counts? The current accounting is directionally useful, but not enough to establish efficiency for more realistic scaling regimes.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
No specific ethical concerns are apparent from the submission. The work studies offline RL methods on standard benchmarks and does not involve sensitive human data, deployment claims, or obviously harmful application details in the paper.

## Soundness Rating
2: fair. The paper has a plausible core idea and nontrivial experiments, but several central mathematical claims are only partially justified, some equations/objectives are inconsistent, and the empirical evidence is mixed rather than fully supportive of the paper’s stronger claims.

## Presentation Rating
2: fair. The main intuition is understandable, and some figures help, but the paper suffers from significant notation issues, malformed equations, grammatical problems, and insufficiently precise methodological exposition.

## Contribution Rating
2: fair. The idea of direct target-action learning for expressive offline RL policies is interesting, and the stronger baseline analysis around MaxQ sampling is useful, but the incremental contribution over existing Q-guided policy extraction methods is not convincingly established, and the gains are inconsistent.

## Overall Rating
4: Marginally below the acceptance threshold. But would not mind if paper is accepted.  
The paper has a reasonable core idea and some practical value, especially in reframing policy extraction and in highlighting the importance of MaxQ tuning. However, the theory-to-method connection is weaker than advertised, the mathematical exposition has important inconsistencies, and the empirical case does not show a robust enough advantage across settings to justify acceptance in its current form.

## Reviewer Confidence
4: confident. I am confident in this assessment and carefully checked the main equations, figures, and result tables, although some ambiguities in the presentation make a few implementation details hard to verify completely.