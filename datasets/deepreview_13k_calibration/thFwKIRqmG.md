# ReLU to the Rescue: Improve Your On-Policy Actor-Critic with Positive Advantages

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 5, 6, 5

## Abstract
This paper introduces an effective and practical step toward approximate Bayesian inference in on-policy actor-critic deep reinforcement learning. This step manifests as three simple modifications to the Asynchronous Advantage Actor-Critic (A3C) algorithm: (1) applying a ReLU function to advantage estimates, (2) spectral normalization of actor-critic weights, and (3) incorporating \emph{dropout as a Bayesian approximation}. We prove under standard assumptions that restricting policy updates to positive advantages optimizes for value by maximizing a lower bound on the value function plus an additive term. We show that the additive term is bounded proportional to the Lipschitz constant of the value function, which offers theoretical grounding for spectral normalization of critic weights. Finally, our application of dropout corresponds to approximate Bayesian inference over both the actor and critic parameters, which enables prudent \textit{state-aware} exploration around the modes of the actor via Thompson sampling. Extensive empirical evaluations on diverse benchmarks reveal the superior performance of our approach compared to existing on- and off-policy algorithms. We demonstrate significant improvements for median and interquartile mean metrics over PPO, SAC, and TD3 on the MuJoCo continuous control benchmark. Moreover, we see improvement over PPO in the challenging ProcGen generalization benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers a modified version of A3C algorithm called VSOP by constraining advantage estimates to be positive and applying dropout and spectral normalization both on the actor and the critic networks. Via the application of dropout, the authors tie their presented method to Bayesian inference over critic and actor parameters – such connection for the actor requires that the advantage estimates be gamma distributed. The authors note that since the sign of advantages can be whatever, the gamma requirement is not fulfilled. As a modification, the authors then propose to clip the advantages to only non-negative values and show theoretically that this change corresponds to the policy gradient maximizing a lower bound on the state-value function plus a bounded constant. Motivated by the constant's bound, the authors propose a spectral normalization for the critic weights. VSOP is evaluated Mujoco and ProcGen benchmarks and demonstrates strong performance against several baseline methods.

### Strengths
VSOP demonstrates strong performance in multiple environments and is mostly justified, see questions. The presented lower bound view on the policy gradient optimization of clipped advantages is novel and can be used to motivate the choice of spectral normalization for the critic weights.

### Weaknesses
Main issues:

While the results presented in the paper are indeed strong, I unfortunately find that the paper is still premature in terms of analysis. Throughout the paper it remained unclear to me how much each added trick contributes to the overall performance. As far as I understand, VSOP was ablated with: 
- VSOP (dropout, spectral, relu, thompson)
- A3C (dropout, spectral, thompson)
- No Spectral (dropout, relu, thompson)
- No Thompson (dropout, spectral, relu)

From these ablations it is evident that one cannot determine the contribution of each of the tried tricks. Given the lack of other strong justifications for performance I feel confused by the results. Furthermore, I have some doubts about the theoretical connection between the clipped advantage and MAP estimation, please see questions section.

### Questions
* Advantage clipping is motivated by the fact that regular advantages cannot be Gamma distributed, because Gamma has only positive support. While clipping does fix the advantage estimates' support issue, why should this operation make the estimates Gamma distributed as assumed by the theory?

* As authors forthcomingly note, the spectral normalization proves to be detrimental to performance when run in a highly parallelized manner – what could be the reason? Does this also happen with ProcGen environments?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new method for enhancing A3C by introducing state-aware exploration. The method has three components, a ReLu function for advantage estimation, a spectral normalization and dropout. Analysis is provided and experimental results show that the method achieves good performance.

### Strengths
The problem in consideration appears interesting and timely.

### Weaknesses
 - It would be helpful if the authors could improve the motivation of the work. In particular, the Intro and the background do not provide an effective argument as to what problems are really being addressed in this work and why should one care.  
- The reviewer would suggest moving the algorithm pseudocode to an earlier place. It is rather inconvenient that Theorem 3.1 is presented before the algorithm. 
- Equation (7) seems to assume a Lipschitz condition on v(s)? Please elaborate. 
- It might be helpful to explain how many training steps are implemented. Also, would it be possible to show the training curves?

### Questions
- It would be helpful if the authors could improve the motivation of the work. In particular, the Intro and the background do not provide an effective argument as to what problems are really being addressed in this work and why should one care.  
- The reviewer would suggest moving the algorithm pseudocode to an earlier place. It is rather inconvenient that Theorem 3.1 is presented before the algorithm. 
- Equation (7) seems to assume a Lipschitz condition on v(s)? Please elaborate. 
- It might be helpful to explain how many training steps are implemented. Also, would it be possible to show the training curves?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a modification to asynchronous advantage actor-critic (A3C) that involves incorporating a ReLU function to the advantage estimates, using spectral normalization and incorporating dropout. The key idea in their work is that exploration is required in on-policy reinforcement learning. When there is no exploration, certain states may fail to get explored and the policy might get trapped. In order to provide a remedy to this, algorithms typically use methods that do not depend on the frequency with which states are visited, which can provide suboptimal results compared to using simply using a method that incorporates details of frequency with which states are visited. As a remedy to this, the algorithm incorporates using a ReLU function to the advantage function. The way this is performed is that in the critic step, dropout is employed and in the actor step, ReLU is used. The motivation behind using the ReLU is that it enables a Bayesian inference over the actor's parameters. The rationale for the changes are justified in the Methods section. The work incorporates a theoretical bound that illustrates how their methods allows a maximization of estimation of state value functions plus a constant. The constant is then massaged in the spectral norm refinement stage of the algorithm. There are also very extensive empirical studies.

### Strengths
The algorithm provides a remedy to an issue with asynchronous advantage actor-critic algorithms (or, more broadly, reinforcement learning algorithms that many algorithms do not take into account state visitation frequency. This issue has been noted by other works as a very important topic in theoretical RL. See the works of [@book{sutton2018reinforcement, title={Reinforcement learning: An introduction}, author={Sutton, Richard S and Barto, Andrew G}, year={2018}, publisher={MIT press} }, @article{tsitsiklis2002convergence, title={On the convergence of optimistic policy iteration}, author={Tsitsiklis, John N}, journal={Journal of Machine Learning Research}, volume={3}, number={Jul}, pages={59--72}, year={2002} }, @inproceedings{winnicki2023convergence, title={On The Convergence Of Policy Iteration-Based Reinforcement Learning With Monte Carlo Policy Evaluation}, author={Winnicki, Anna and Srikant, R}, booktitle={International Conference on Artificial Intelligence and Statistics}, pages={9852--9878}, year={2023}, organization={PMLR} }] for more on this. The work takes an interesting angle by looking at statistical techniques for improvement which in turn motivated other improvement to the algorithm. The work provides a theoretical intuition and bound as well as numerous empirical studies.

### Weaknesses
In the theoretical component of the algorithm, while there is a theoretical result which shows how the value function improves as a result of the modifications, which is very nice, but I think that the work could shed light on the role of these parameters on the overall convergence of the modified A3C? Specifically, how do the introduced modifications to the advantage function, such as the ReLU activation and spectral normalization, affect the convergence rate and stability of the algorithm? The current analysis provides a bound on value function improvement, but it does not explicitly address how these changes impact the long-term behavior of the learning process. I also noticed that neither the simulations nor the theoretical results shed light on the exact role of the choice of dropout, relu etc., on the impact of their bounds, both theoretical bounds and empirical bounds, with the exception of the justification of the spectral normalization step. For instance, how does the dropout rate influence the exploration-exploitation trade-off, and how does the ReLU activation affect the bias and variance of the advantage estimates? Or perhaps, a comparison to A3C, since that is the algorithm the current paper is based on? A direct comparison would help to isolate the specific contributions of the proposed modifications and quantify their impact on performance and convergence.

### Questions
A question I have is whether the constant K is policy dependent, in which case, what would the policy improvement step be optimizing over in (6)? I noticed that the K-Lipschitz assumption is introduced with respect to a particular value function over all $s\in\scriptS,$ 
which makes me wonder if K is dependent on policies π. Another question I have is if the assumptions on the action distribution follow the normal-gamma in the bound on the value function improvement in (6)? What other assumptions are incorporated in the bound on the value function improvement?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper made three simple modification to advantage actor-critic methods.
(1) introduced a ReLU function to restrict policy update to the optimal policy while enable approximate Bayesian inference.
(2) used spectral normalization to restrict the output of network
(3) used Thopson sampling to do exploration via dropout.
The reported results indicate that, mostly, the proposed method achieves improved returns when compared to the popular on-policy algorithms and other off-policy baseline methods.

### Strengths
Minimal modification of the ac method to enable Bayesian inference is an interesting and valuable idea. However, similar discussions exist in previous work[1].

Use Thompson sampling to replace passive exploration without introducing complex machanism and high computational cost is important for dealing with the Exploration-exploitation dilemma for on-policy algorithms.


The performance of this method is impressive.

[1] Levine, Sergey. "Reinforcement learning and control as probabilistic inference: Tutorial and review." arXiv preprint arXiv:1805.00909 (2018).

### Weaknesses
This paper is not well written. Neccessary background and discribtion of Thompson sampling is missing. The names of metrics shown in Figure 1(Median, IQM, Mean, OG) should be emphasized above.(e.g. change 'robust normalized median, interquartile mean, and mean metrics' to 'robust normalized median(Median), interquartile mean(IQM), mean(Mean) and optimal gap(OG) metircs'). The multiple use of some terms in many places made me confused, e.g. I think A3C represent two different algorithms respectively in Figure 1 and 2.

Except in the case of sparse rewards, it is generally not acceptable to assume that the difference between the expected value of the value function over the next states and the value function at the current state is zero. This assumption appears to underpin the derivation of the bound $C_\pi(\mathbf{s})$, and its invalidity raises concerns about the tightness of this bound and its implications for Theorem 1.

According to the equation (3), the paper assume that $h$ is independent from $\theta$. However, the advantage function is strong depend on current policy and also depend on $\theta$. And the advantage function may not be approximated via Gamma distribution. From my understanding, the $\sigma^2\geq 0$ is a more direct reason why $h$ is a non-negative value. A more rigorous justification for the use of the Gamma distribution in this context would strengthen the theoretical foundation of the proposed method.

typo on (4): $\frac{\beta^\alpha\sqrt{\tau}}{\sqrt{\Gamma(\alpha)2\pi}}\rightarrow \frac{\beta^\alpha \sqrt{\tau}}{\Gamma(\alpha)\sqrt{2\pi}}$, $exp(\beta h_i)\rightarrow exp(-\beta h_i)$.

typo in appendix, an extra $\nabla$ after 'Letting, $v^*_\pi(s_0)$......'

### Questions
Can you explain in detail how to combine Thompson sampling with Bayesian inference? And why this is a better **state-aware** exploration method?

Is it necessary to assume it as a gamma-normal distribution?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
