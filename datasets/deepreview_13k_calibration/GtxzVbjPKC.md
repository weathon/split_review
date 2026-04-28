# Variational Inequality Methods for Multi-Agent Reinforcement Learning: Performance and Stability Gains

- Decision: Reject
- Avg Score: 3.50
- Scores: 3, 3, 3, 5

## Abstract
Multi-agent reinforcement learning (MARL) presents unique challenges as agents learn strategies through experiences. Gradient-based methods are often sensitive to hyperparameter selection and initial random seed variations. 
Concurrently, significant advances have been made in solving Variational Inequalities (VIs)---which include equilibrium-finding problems--- particularly in addressing the non-converging rotational dynamics that impede convergence of traditional gradient-based optimization methods. 
This paper explores the potential of leveraging VI-based techniques to improve MARL training. Specifically, we study the performance of VI methods—namely, Nested-Lookahead VI (nLA-VI) and Extragradient (EG)—in enhancing the \textit{multi-agent deep deterministic policy gradient} (MADDPG) algorithm. 
We present a VI reformulation of the actor-critic algorithm for both single- and multi-agent settings. We introduce three algorithms that use nLA-VI, EG, and a combination of both, named \emph{LA-MADDPG}, \emph{EG-MADDPG}, and \emph{LA-EG-MADDPG}, respectively.
Our empirical results demonstrate that these VI-based approaches yield significant performance improvements in benchmark environments, such as the zero-sum games: \textit{rock-paper-scissors and matching pennies}, where equilibrium strategies can be quantitatively assessed, and the \textit{Multi-Agent Particle Environment: Predator prey} benchmark, where VI-based methods also yield balanced participation of agents from the same team.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper investigates combining multi-agent policy gradients with game-theoretical gradients based on variational inequalities (VIs). It examines whether incorporating VI-based optimization methods can enhance policy optimization within MARL frameworks.

In practical terms, the authors propose an extension to the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) method. Rather than employing the standard MADDPG gradient updates, the paper introduces modifications using extragradient and nested-lookahead techniques to adjust the MADDPG gradients.

### Strengths
1. The paper is very well organized and easy to follow.

2. VI methods and MAPG methods, though highly related, are somehow separated in the current multi-agent literature. The reviewer was aware of some papers discussing that MAPG cannot converge to NEs. But generally, in the existing literature, the default context for MAPG is cooperative tasks, while VI methods are for zero-sum games--leading to a gap.

### Weaknesses
1. The __motivation__ of the proposed method needs significant improvement.

It is strange to motive the paper by the hyper-parameter sensitivity observed in MARL. The rotational dynamics of gradient-based methods in multi-agent games is inherent and cannot be eliminated by hyper-parameter fine-tuning. This is well studied in the literature, and is known to be attributable to the asymmetric component of the Jacobian of the limiting ordinary differential equations (ODE).

Contrary to the authors' implication, combining MAPG (multi-agent policy gradient) methods with VI cannot, by itself, address the motivating problems mentioned by the authors. To be specific, they are still very sensitive to hyper-parameters. Many VI methods like sympletic gradient adjustment and consensus optimization even introduce more hyper-parameters, for the purpose of addressing the asymmetric component in the Jacobian. Moreover, the reviewer also didn't see how the proposed method is able to improve the search space of MAPG, which is another motivating problem of this paper.

2. The application of extragradient methods, as referenced in seminal work [1], is typically confined to coherent saddle point problems where all saddle points are assumed to be local Nash equilibria—an assumption not generally applicable in MARL environments.

This discrepancy raises concerns about the applicability of the proposed methods to the broader class of problems presented in MARL scenarios. Without addressing these fundamental theoretical mismatches, there is no assurance that the proposed method can effectively converge to differential Nash Equilibria, which the paper identifies as its solution concept.

3. The __results__ of the method are not informative.

The presentation of the results lacks clarity and does not convincingly demonstrate the efficacy of integrating MADDPG with VI techniques. 

The experiments, as depicted, do not show meaningful improvement in learning outcomes. What is point of using MADDPG + VI in games? Most advanced VI methods can already find the NEs of these games.

In Fig. 2,  the proposed method does not show any improvements during learning. Why? 

Moreover, the high variance observed in the results casts further doubt on the method's reliability and robustness. Such discrepancies point to a need for more rigorous experimental design and a deeper analysis to genuinely assess the method's impact on performance in MARL settings.

### Questions
See the previous section.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes incorporating variational inequality methods into multi-agent reinforcement learning to address its sensitivity to hyperparameters caused by gradient-based updates. The authors use two types of VIs on top of MADDPG and evaluate them alongside MADDPG.

### Strengths
- Sensitivity to hyperparameters is a significant problem in reinforcement learning, impacting its practical applications.
- Introducing variational inequalities to improve stability in finding equilibrium is an interesting approach.

### Weaknesses
The weakest part of this paper is the motivation/results section.

- The authors introduce VIs to tackle the high sensitivity to hyperparameters in RL. However, there are no experiments provided that demonstrate the proposed method’s effectiveness in addressing this issue. I recommend that the authors illustrate the extent of MADDPG’s sensitivity to hyperparameters, identifying which hyperparameters are particularly sensitive (an analysis of high sensitivity), and then show how effectively the proposed method stabilizes this sensitivity compared to MADDPG. Including additional analysis and ablation studies would further verify this claim. Based on the current results, it is difficult to conclude that the proposed method addresses the problem the authors aim to solve.


- The proposed method primarily relies on MADDPG, but it would be beneficial if the authors provided results of the proposed method applied to other algorithms (including SOTA, as MADDPG is somewhat outdated). This would help demonstrate the generalizability of the method.

- Figure 2 does not effectively illustrate the benefits of the proposed method.

### Questions
See weaknesses

### Soundness
1

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper investigates the potential of leveraging Variational Inequality (VI)-based techniques to enhance Multi-Agent Reinforcement Learning (MARL) algorithms. Specifically, it incorporates Nested-Lookahead VI and Extra-Gradient into the MADDPG framework and empirically evaluates the modified methods—LA-MADDPG, EG-MADDPG, and LA-EG-MADDPG—on zero-sum games and MPE tasks. The experimental results demonstrate performance improvements over standard optimizers.

### Strengths
- The incorporation of VI methods into MARL presents a compelling avenue for research.
- The paper includes detailed pseudocode, enhancing the clarity and understanding of the proposed methods.
- Experimental results indicate improvements compared to traditional methods.

### Weaknesses
 - The specific problem with MADDPG that the paper addresses is unclear. While the paper discusses VI and its proposed solutions, the alignment with the MARL context and the specific algorithm remains weak. It appears the focus is primarily on a general optimization issue rather than a specialized challenge within MARL.
- The proposed methods seem straightforward, primarily involving a switch from the Adam optimizer to existing VI methods. The motivation for this switch is not adequately explained, and there is a lack of theoretical justification for how LA or EG methods can specifically benefit MADDPG or MARL algorithms. The paper lacks a clear explanation of why standard optimization methods fail in this context, and why these specific VI methods are expected to provide a remedy. For instance, it's not clear if the instability is due to non-convexity, saddle points, or other issues inherent in the MARL landscape. A more detailed analysis of the optimization landscape and how VI methods address these specific challenges would be beneficial.
- The experiments appear somewhat simplistic; a more comprehensive evaluation is necessary. The authors should consider testing in more complex domains and comparing against other MARL methods, as the proposed approach appears generalizable. Additionally, given the limited state-action space in tasks like rock-paper-scissors, theoretical justifications for these tasks would strengthen the argument regarding the shortcomings of existing methods and how the proposed approach addresses them. The current experiments do not sufficiently demonstrate the scalability and robustness of the proposed methods in more challenging MARL scenarios.

### Questions
In Figures 2 and 6, the evaluation episodes provide limited information. I would appreciate seeing the learning curves for the two MPE experiments.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a novel optimization method for Multi-Agent RL (MARL), Lookahead-VI, which is a Variational Inequalities(VI)-based methods to substitute Adam optimizer with gradient descent to make MARL algorithms (MADDPG in this paper) better converge. The authors remodel MARL problems as a special case of VI problems, and apply Lookahead-VI to address it. On several simple environments, the proposed method achieves higher performance and can retrieve policies closer to equilibrium.

### Strengths
1. The idea to view multi-agent RL as a VI problem and introduce new solvers than gradient descent with Adam is novel and looks mathematically promising, since traditional RL can be seen as a special case of the proposed framework.

2. The paper clearly shows how MADDPG can be reformulated into a VI problem and how gradient descent can be seen as a special case for solving such VI problems, which gives people outside of VI community a good grasp of how the algorithm works.

### Weaknesses
1. The contribution to the MARL community is limited by the fact that MADDPG is largely outdated due to its difficulty to train and instability. There are many different, newer methods available, such as MATD3 [1], MAAC [2], MAPPO [3], etc. Many of them are not referenced in this paper. In fact, instability can still be witnessed in Fig. 3 and I am curious whether changing an RL algorithm, such as MATD3, would fix such issue. The paper's focus on MADDPG, despite its known limitations, weakens the impact of the proposed method. A more compelling study would involve a modern MARL algorithm as the base, given that the core issue seems to be optimization rather than the specific RL algorithm.

2. While this paper empirically demonstrates that the proposed method is closer to equilibrium, those works are mostly on simple environments. It is unclear whether the property of being closer to equilibrium in simple tasks will bring better performance for more complicated mainstream MARL benchmarks such as SMAC. The lack of scalability analysis, particularly with a larger number of agents, is a significant limitation. The paper does not address whether the proposed method can handle the increased complexity of environments with many agents, which is a common scenario in real-world MARL problems.

**Minor Issues**

1. in line 150-151, the authors wrote "Multi-agent deep deterministic policy gradient (MADDPG, Lowe et al., 2017), extends Deep deterministic policy gradient (DDPG, Lillicrap et al., 2019)". This is not proper reference as an older paper seemingly extends a much newer paper.

2. each $i=1,\dots,N$ agent -> each agent $i=1,\dots,N$ in line 224.

3. The first paragraph of introduction mentions many application of MARL without reference; it would be better if the authors can provide reference for each of the application listed.

### Questions
I have several questions: 

1. while it is well-known that MARL with gradient descent is hard to converge, is there any theoretical proof that other VI methods are better than gradient descent when it comes to this special case of VI problems?

2. Can the authors explain why EG does not seem to improve performance as significant as LA, and EG-LA-MADDPG does not work well in the MPE-Predator-prey game and the rock-paper-scissor game in Fig. 5?

3. The authors claim "We did not achieve full convergence to the Nash equilibrium with any of the algorithms, as we did not extensively tune the hyperparameters." in line 372-373. Is it possible to reach Nash equilibrium by tuning the hyperparameters more? It would be great if the authors could provide more attempts on achieving Nash equilibrium by tuning hyperparameters (which is also an ablation to hyperparameter sensitivity).

4. About "on the rewards as a metric in MARL": the authors claim that we need stronger evaluation metrics in MARL. While I agree that reward cannot fully reflect agent's behavior, I am not sure if other metrics could be called as "stronger" as the goal of multi-agent RL, like any RL, is to maximize reward.

### Soundness
3

### Presentation
3

### Contribution
2
