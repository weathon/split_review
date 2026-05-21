---
job_id: 9f836601-561f-41f1-ba9e-bb67f4680058
agent_id: ICLR_main_2026_2
status: COMPLETED
filename: 5o0zF03RP9.pdf
paper: IncentRL: Bayesian Adaptation of Preference Gaps in Reinforcement Learning
main_score_norm: 0.2
desk_reject: false
---
# Desk Rejection Assessment:
## Paper Length
Pass ✅.

## Topic Compatibility
Pass ✅. The paper is clearly within ICLR scope, combining reinforcement learning, Bayesian adaptation, KL-regularized objectives, and cognitively inspired modeling.

## Minimum Quality
Pass ✅. The paper contains the expected core components, including Abstract, Introduction, Related Work, Methods, Experiments with quantitative results, Discussion, and Conclusion. While there are serious concerns about technical completeness, novelty, and empirical support, these rise to the level of a strong reject rather than a desk reject.

## Prompt Injection and Hidden Manipulation Detection
Pass ✅. I did not find hidden prompts, manipulative instructions, or suspicious text targeting automated reviewers in the provided paper content.

# Expected Review Outcome:
## Summary
This paper proposes IncentRL, a reinforcement learning framework that augments external rewards with a KL-based preference-prediction alignment term, where the agent is rewarded according to how well predicted outcome distributions \(p(o \mid s,a)\) match preferred outcome distributions \(q(o \mid s)\). The main claimed contribution is an online Bayesian adaptation of the incentive weight \(\beta\), intended to remove manual tuning of the trade-off between external rewards and internal incentives.

The paper presents a high-level theoretical discussion of the effect of \(\beta\), including two simple propositions in a toy finite-MDP setting, and evaluates the method on a 2-state toy problem, MountainCar-v0, and MiniGrid Doorkey 8x8. The empirical results suggest some gains for small fixed \(\beta\), and the paper also provides figures intended to show posterior concentration of the adapted \(\beta\).

## Strengths
1. The paper addresses a real and relevant problem in RL, namely how to balance extrinsic reward with additional intrinsic or shaping signals without having to hand-tune a fixed coefficient for every task. That is a worthwhile question, especially in sparse-reward settings.

2. The core shaping idea is easy to understand: use
\[
r^{\text{total}}(s,a)=r^{\text{ext}}(s,a)-\beta \,\mathrm{KL}(p(o\mid s,a)\|q(o\mid s))
\]
from Section 3.2, and interpret the KL term as a preference-prediction mismatch penalty. Regardless of whether the current form is fully convincing, the objective itself is straightforward and could be useful as a conceptual scaffold for future work.

3. The paper does include multiple environments rather than only a toy example. In particular, the authors test both a small tabular setting and two standard sparse-reward domains. This is better than a paper that makes broad claims from a single micro-benchmark.

4. Some of the reported empirical trends are directionally interesting. In Table 1 on the toy 2-state MDP, all tested \(\beta>0\) values outperform \(\beta=0\), and Figure 1 visually reflects the same trend: the nonzero-\(\beta\) curves rise faster and exhibit tighter uncertainty bands than baseline Q-learning. Even though this experiment is too small to carry the paper, it at least matches the intended qualitative behavior of the shaping term.

5. The MountainCar sweep in Table 2 is also useful in one respect: it reveals a non-monotonic dependence on \(\beta\). The \(\beta=0.1\) setting improves over baseline, while \(\beta=0.3\) and \(1.0\) collapse badly. That is actually informative, because it supports the claim that the trade-off is delicate and motivates some form of adaptation. Ironically, the strongest evidence in the paper may be that hand-tuning matters a lot.

6. The discussion section is reasonably candid about some limitations, especially on Page 9 where the authors acknowledge preference misalignment, KL dominance, and latent mismatch as possible failure modes. I appreciate that the paper does not pretend the shaping term is automatically benign.

## Weaknesses
1. **The central claimed novelty, Bayesian adaptation of \(\beta\), is not actually specified as a method.**  
   This is the biggest problem in the paper. The abstract, introduction, and contributions on Pages 1 to 2 repeatedly frame the main contribution as “treating the incentive weight \(\beta\) as a Bayesian random variable, updated online,” and Figures 3 and 4 are presented as evidence of posterior concentration. However, nowhere in the main paper is there a mathematical definition of the Bayesian model, likelihood, prior, posterior update, sampling rule, or decision rule used to adapt \(\beta\). There is no equation of the form
   \[
   p(\beta \mid \mathcal{D}_{1:t}) \propto p(\mathcal{D}_{1:t}\mid \beta)\,p(\beta),
   \]
   no specification of what \(\mathcal{D}_{1:t}\) contains, no explanation of whether the update is Thompson sampling, Bayesian optimization, sequential Monte Carlo, grid posterior maintenance, or something else.  
   This omission is not cosmetic. It makes the main claimed contribution scientifically unassessable and irreproducible. Without an explicit update rule, Figures 3 and 4 are effectively illustrations without a method behind them.

2. **The paper is underspecified at the level of the core modeling objects \(p(o\mid s,a)\) and \(q(o\mid s)\).**  
   In Section 3.1, \(p(o\mid s,a)\) is described as possibly coming “from a forward model or from environment dynamics,” while \(q(o\mid s)\) may be hand-crafted, learned from demonstrations, or generated by language models or human instructions. This is far too broad. The meaning of the method depends heavily on what the “outcome” variable \(o\) is, whether it is the next state, a latent code, an event indicator, or a trajectory fragment.  
   The practical details are especially missing in the experiments. For MountainCar on Page 6, the paper says \(q(o\mid s)\) “assigns all probability to the goal” and \(p(o\mid s,a)\) is the predicted outcome distribution, but does not define the support of \(o\), how a continuous next-state distribution is represented, how the prediction model is trained, or how KL is computed in practice. If \(q\) is a point mass on an event and \(p\) is continuous, the KL can be undefined or degenerate unless one introduces smoothing or a compatible parameterization. None of that is explained.

3. **There is a likely mathematical inconsistency in the toy setup because the stated \(q\) makes the KL divergence ill-defined or infinite.**  
   In Experiment 1 on Page 5, the preferred outcome is given as
   \[
   q(o\mid s_0)=\{s_1:1.0, s_0:0.0\},
   \]
   while
   \[
   p(o\mid s_0,a_1)=\{s_1:0.3, s_0:0.7\}.
   \]
   Then
   \[
   \mathrm{KL}(p\|q)=\sum_o p(o)\log \frac{p(o)}{q(o)}
   \]
   includes the term \(0.7\log(0.7/0)\), which is \(+\infty\). But the paper treats this KL term as a finite reward-shaping quantity and reports normal learning curves in Figure 1 and Table 1. So either the actual implementation did not use the stated \(q\), or some smoothing/clipping was applied, or the KL was replaced by another divergence. This matters because the toy experiment is the cleanest place where the method should be mathematically transparent, yet the written formulation is inconsistent with the reported behavior.

4. **The theoretical analysis is too weak and in parts overstated relative to what is shown.**  
   Proposition 1 on Page 4 is presented as preserving optimality for sufficiently small \(\beta\), but it is only given as a sketch, and the required assumptions are not stated carefully. The claim relies on a positive reward gap in finite MDPs and bounded perturbations, but boundedness of the KL term requires assumptions on the support of \(q\) relative to \(p\), which the paper does not state. If \(q(o\mid s)=0\) where \(p(o\mid s,a)>0\), the shaping term is not bounded. That directly breaks the proof sketch.  
   Proposition 2 is also too informal. The statement says that as \(\beta\to\infty\), the optimal policy converges to one minimizing \(\mathrm{KL}(p(o\mid s,a)\|q(o\mid s))\) “for each state.” That is not obviously implied by domination of the stage reward penalty in a discounted MDP, because policy optimality is trajectory-level and state-coupled through dynamics. A myopic statewise minimizer need not be globally optimal under transition coupling.  
   More generally, the paper claims on Page 4 that latent-space extensions preserve “convergence guarantees,” but no such guarantee is actually established for the latent case.

5. **The empirical evidence is too limited and too weak to support the breadth of the claims.**  
   The abstract and conclusion make fairly broad statements such as “Bayesian adaptation of preference gaps removes the need for manual trade-off tuning” and that the method provides a “principled” mechanism improving RL agents. The experiments do not support that level of generality. There are only three environments, one of which is a 2-state toy MDP. MountainCar uses only 3 seeds, MiniGrid uses 3 seeds, and there are no statistical tests, no confidence intervals beyond seed standard deviation in tables, and no evaluation on harder benchmarks where intrinsic reward tuning is genuinely difficult.  
   This would already be thin for a workshop paper. For a main-track ICLR submission making a new RL framework claim, it is not enough.

6. **The results presentation is internally inconsistent across text, tables, and figures.**  
   A concrete example is the MiniGrid section. On Page 7, Figure 2 is captioned as using \(\beta=0.01\) versus \(\beta=0.0\), and the text discusses only those two values. But the preceding MountainCar section on Page 6 reports sweeps over \(\{0.0,0.1,0.3,1.0\}\), and Figures 3 and 4 then claim Bayesian adaptation concentrates near \(\beta\approx 0.1\). Appendix Table 3, however, reports posterior means that shrink below \(0.05\) and end around \(0.0173\), which is not really “near \(0.1\)” after the first round. These pieces do not fit together cleanly.  
   Put differently, Figure 3 is supposed to support the narrative that posterior adaptation recovers the effective region, yet the summary statistics in Table 3 suggest concentration much closer to the MiniGrid fixed setting of \(0.01\) than to \(0.1\). The paper never resolves this mismatch.

7. **The experimental setup does not adequately compare against relevant baselines.**  
   The method is framed as adaptive balancing of external and internal rewards, but the empirical comparison is mostly against standard RL and fixed-\(\beta\) variants of the same proposal. There is no comparison to other adaptive weighting strategies, no annealing baseline, no simple schedule baseline, and no competing intrinsic reward method in the same implementation stack.  
   This matters because the current experiments do not establish that the Bayesian adaptation itself is useful relative to simpler alternatives. Given Table 2, where performance is highly sensitive to \(\beta\), a reasonable baseline would be something as simple as a tuned annealing schedule or a heuristic adaptive coefficient based on reward sparsity. Without that, the “Bayesian” aspect is not convincingly justified.

8. **The paper’s framing around neuroscience and the Free Energy Principle is much stronger than the technical connection actually shown.**  
   On Pages 1 to 2 and again in Discussion, the paper repeatedly invokes dopamine-based reward prediction error and the Free Energy Principle. But the technical content does not develop these analogies beyond a motivational level. There is no derivation from active inference, no variational free energy objective, no neuroscientific model comparison, and no formal mapping between scalar RPE and the proposed KL penalty.  
   This over-framing is not harmless. It gives the impression of deeper theoretical grounding than is actually provided, and it distracts from the fact that the RL method itself remains underspecified.

9. **Reproducibility is poor because key algorithmic details are missing.**  
   Section 5.1 is titled “The IncentRL Algorithm,” but it is really a five-line conceptual description, not an algorithm. There is no pseudocode, no update equations for the policy learner under the shaped reward, no explanation of whether \(p(o\mid s,a)\) is learned jointly or precomputed, no architecture/training details for the forward model, and no details on how often \(\beta\) is updated. For DQN specifically, there are no replay-buffer details, target-network settings, optimization hyperparameters, or reward preprocessing details in the main paper.  
   This makes it hard to trust or reproduce the results, especially because the method’s behavior depends critically on numerical details of the KL term and \(\beta\) adaptation.

10. **Some claims are stronger than the evidence in the tables and figures.**  
   The abstract says the method “removes the need for manual trade-off tuning,” but the experiments mainly show that performance can be very good for one small \(\beta\), very bad for larger \(\beta\), and that some unspecified adaptation scheme appears to move \(\beta\) into a better range. Table 2 actually emphasizes sensitivity, not robustness. Figure 2 shows an improvement in MiniGrid between \(\beta=0\) and \(\beta=0.01\), but this is still just one tuned value on one task with three seeds. The paper has not demonstrated removal of tuning, only that tuning matters and adaptation might help.

11. **The literature positioning is incomplete for the specific Bayesian reward-shaping angle claimed here.**  
   The related work section covers curiosity, empowerment, policy-KL regularization, and active inference at a high level, but it does not engage with prior work on Bayesian reward shaping or Bayes-adaptive formulations of shaping/intrinsic motivation. Since the paper’s headline idea is the Bayesian treatment of the incentive coefficient, the absence of a sharper comparison to Bayesian shaping approaches makes it difficult to judge originality versus reformulation.

12. **Figure-level evidence is not as persuasive as the text suggests.**  
   Figure 1 does show faster convergence for \(\beta>0\), but the three nonzero-\(\beta\) curves are nearly indistinguishable, which undercuts any nuanced story about adaptation or posterior concentration in the toy setting. Figure 2 is also hard to interpret as evidence specifically for IncentRL rather than simply mild regularization helping training, because only \(\beta=0\) and \(0.01\) are plotted, and there is no competing shaping method. Figures 3 and 4 are supposed to be the main evidence for Bayesian adaptation, but without the actual update rule they function more as post hoc diagnostics than as scientific validation of a specified algorithm.

## Questions
1. Please define the Bayesian adaptation mechanism precisely in the main paper. What is the prior over \(\beta\), what likelihood is used, what observations update the posterior, and what exact rule selects \(\beta_t\) online? A single explicit equation or pseudocode block would substantially increase my confidence.

2. How is \(\mathrm{KL}(p(o\mid s,a)\|q(o\mid s))\) computed in each experiment, especially in MountainCar where the state space is continuous? What is the outcome variable \(o\), how are \(p\) and \(q\) parameterized, and how is support mismatch handled?

3. In the toy MDP, the stated \(q(o\mid s_0)=\{s_1:1,s_0:0\}\) makes \(\mathrm{KL}(p\|q)\) infinite when \(p(s_0\mid s_0,a_1)=0.7\). Was smoothing used, such as \(q_\varepsilon=(1-\varepsilon)\delta_{s_1}+\varepsilon \delta_{s_0}\)? If so, please state the actual \(\varepsilon\) and revise the formulation accordingly.

4. For Proposition 1, can you state the exact assumptions needed for the bounded perturbation argument? In particular, do you assume \(\mathrm{supp}(p(\cdot\mid s,a)) \subseteq \mathrm{supp}(q(\cdot\mid s))\) for all \((s,a)\), which would ensure finite KL?

5. For Proposition 2, can you either weaken the statement or justify more carefully why the \(\beta\to\infty\) limit yields a policy that minimizes the KL term “for each state”? In a discounted MDP this is not obviously equivalent to globally optimal planning under dynamics.

6. Please provide a proper algorithm box or pseudocode. At minimum, the paper should specify: how \(p(o\mid s,a)\) is learned or obtained, how often \(\beta\) is updated, whether posterior sampling or posterior mean is used, and how the shaped reward interacts with the base RL optimizer.

7. Could you compare Bayesian adaptation against at least one simpler adaptive baseline, such as an annealed \(\beta\), a reward-normalized coefficient, or a learned scalar schedule? This would clarify whether the gains come from the Bayesian machinery specifically or merely from avoiding a bad fixed coefficient.

8. For the MiniGrid claim that Bayesian adaptation “achieved performance comparable to the best fixed value,” can you include the actual quantitative result in the main paper rather than only “not shown”? That evidence is central to the paper’s main claim.

## Flag For Ethics Review
- No ethics review needed.

## Details Of Ethics Concerns
None beyond standard caution that reward shaping and preference specification can induce unintended behavior if deployed in real systems. The paper discusses some of these concerns in Section 6.2, but I do not see a conference-level ethics issue requiring separate ethics review.

## Soundness Rating
1: poor. The core claimed Bayesian component is not specified, key mathematical objects are underspecified, the toy KL formulation appears inconsistent as written, and the experimental evidence is too limited to support the main claims.

## Presentation Rating
2: fair. The paper is readable at a high level, but important definitions, equations, and implementation details are missing or inconsistent, which substantially limits clarity and reproducibility.

## Contribution Rating
1: poor. The motivating idea is interesting, but in its current form the paper does not establish a solid methodological contribution because the central Bayesian adaptation mechanism is not concretely presented or convincingly validated.

## Overall Rating
2: Reject, not good enough. The paper has an appealing high-level direction, but the current submission is too incomplete in its central method specification, too weak in theory, and too limited empirically for ICLR main track.

## Reviewer Confidence
4: confident. I am confident in this assessment, though it is still possible I missed implementation details that may exist outside the main paper. My main concerns come directly from what is, and is not, specified in the submission.