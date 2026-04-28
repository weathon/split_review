# DRIVE: Distributional Model-Based Reinforcement Learning via Variational Inference

- Decision: Reject
- Avg Score: 5.75
- Scores: 3, 6, 8, 6

## Abstract
Distributional reinforcement learning (RL) provides a natural framework for estimating the distribution of returns rather than a single expected value. However, the control aspect of distributional RL has not been as thoroughly explored as the evaluation part, typically relying on the greedy selection rule with respect to either the expected value, akin to standard approaches, or risk-sensitive measures derived from the return distribution. On the other hand, casting RL as a probabilistic inference problem allows for flexible control solutions utilizing a toolbox of approximate inference techniques; however, its connection to distributional RL remains underexplored. In this paper, we bridge this gap by proposing a variational approach for efficient policy search. Our method leverages the log-likelihood of optimality as a learning proxy, decoupling it from traditional value functions. This learning proxy incorporates aleatoric uncertainty of the return distribution, enabling risk-aware decision-making. We provide a theoretical analysis of our framework, detailing the conditions for convergence. Empirical results on vision-based tasks in DMControl Suite demonstrate the effectiveness of our approach compared to various algorithms, as well as its ability to balance exploration and exploitation at different training stages.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a combination of distributional RL and probabilitstic inference in model based RL to incorporate aleatoric uncertaity of distribution for risk-aware decision-making.

The main learning objecitve of this paper is the log-likelihood of the optimality variable that is computed by marginalizing the conditional probability $p(O=1|U,s,a)$ on $U$ where $U$ is the return distribution.

Since the optimality variable $O=1$ implies the optimal return at given state and action, maximizing the return of agent induces the log-likelihood of optimality variable.

Compared to Dreamer, the above log-likelihood is added to the learning objective.

In experiments, all experiments is conducted in vision-based deepmind control suite.

### Strengths
The main contribution of this paper is to reduce the effect of aleotoric uncertainty in training model-based RL.

By introducing the optimality variable, the proposed method can asses the quality of return distribution by imagination and match to the ground-truth return distribution better by preventing from leaning to the maximum value.

### Weaknesses
The main conern that I have is the quality of presentation and the lack of experiments.

1. The notations are not consistent. For example, there are several different q functions which outputs  $a$ in Equation 9, $s_t$ in Equation 16, $U$ in Algorithm 1 without any proper subscriptions.
2. The theoretical results, theorem 5.1 and theorm 5.2 are not connected to the main contribution which induces the better performance of model-based distributional RL method. Specifically, Theorem 5.1 appears to be a standard policy improvement theorem, and Theorem 5.2 seems to establish a connection to standard RL, but neither directly addresses how the proposed method handles aleatoric uncertainty for risk-aware decision-making.
3. It is not clear which distributinoal RL method is used to estimate $U$, such as C51 or QRDQN. The paper refers to $U$ as the return distribution, but it is unclear if $U$ is a continuous random variable or a discrete categorical distribution. The cross-entropy loss used in Eq. (13) is typically applied to categorical distributions, but the return is a continuous value representing the discounted sum of rewards. It seems that the authors might be referring to the log-likelihood of the return distribution, but this needs clarification.
4. The experiments is only conducted in deepmind control suite, which is not reported in the main baseline, Dreamer. If the proposed method has an advantage in vision-based continuous control, the authors should have described how to perform better in continous control tasks. Furthermore, the paper does not specify which policy (critic) is used for continuous control, making it difficult to understand the implementation details.
5. Although the authors claim to outperform Dreamer, the experimental results are limited to a subset of the DeepMind Control Suite. The original Dreamer paper reports results on 22 environments, but the authors only provide results on 12 environments, raising concerns about the generalizability of their findings.

### Questions
Can you make the notations be clear to help to understand the main contribution better?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper combines perspectives from RL as inference and distributional RL nicely through introducing the return random variable $U$, which offers a unique perspective as well as a new principled way to do policy search. The perspectives introduced in this paper can be helpful for future works that combine tools from RL, distributional RL, and probabilistic inference. Empirical results are reasonable.

### Strengths
**[Originality]**
The paper combines perspectives from RL as inference and distributional RL nicely through introducing the return random variable $U$, which offers a unique perspective as well as a new principled way to do policy search. 

**[Quality]**
The idea is well motivated and empirical results are reasonable. 

**[Clarity]**
The writing and derivations are for the most part easy to follow

**[Significance]**
The perspectives introduced in this paper can be helpful for future works that combine tools from RL, distributional RL, and probabilistic inference.

### Weaknesses
For me, the main weaknesses are incomplete empirical evaluations, and some (for me) confusing choices made in the variational lower bound derivations.

- In Figure 4, the 95 confidence interval (?) between ablations are overlapped, suggesting there is no statistically significant difference between their mean. More seeds can be helpful to separate out the differences.
- Taking more samples to approximate a distribution ($\mathfrak{q}$, see L248) actually results in *worse* performance (Figure 4b) is strange, and in my opinion the authors do not provide a sufficiently satisfactory explanation for this. The authors should investigate the effect of the number of samples on the variance of the gradient estimates, as this could be a potential cause.
- It is not fully clear yet how the method’s behavior differs from existing work. The method seems to be roughly on-par with existing strong model-based methods (Figure 2), with potentially interesting differences in their exploration (Figure 3) that can be further investigated. It would be helpful to see a more detailed comparison of the method's performance against other approaches, particularly in terms of sample efficiency and robustness to hyperparameter changes.
- I will ask about variational approximation in the “question” section below.

### Questions
1. I am confused by equation 29 (which impacts the lower bound derivation of equation 9). Equation 29 can be equivalently written as 
$$\log p_\psi (\mathcal{O}=1 | s,a) = \log E_{p_\psi(U|s,a)} [\frac{\exp U}{ \exp U_{max}} ] \geq E_{p_\psi(U|s,a)}[U] - U_{max}$$ 
without the need to introduce distribution $\mathfrak{q}$. Since $p_\psi(U|s,a)$ is supposed to be the parametric return model (L183) which we can sample from (or even have in close form), why did the authors introduce an additional distribution $\mathfrak{q}$ (in Eq 30)? 

2. Relating to above, $\mathfrak{q}$ seems to be used as the “true” return distribution (e.g. Eq 11), which makes it weird that it does not “need” to appear in the lower bound at all. Am I conceptually missing something here? It perhaps feels like $\log p^\pi_{\psi} (\mathcal{O}=1 | s)$ is not quite the correct quantity to lower-bound and optimize (but should instead be e.g. a quantity that does not depend on $\psi$)?

3. What is the parametric distribution $p_\psi(U|s,a)$, I presume it is a Gaussian? 

4. For results: why are the per-game SAC and DreamerV3 results from Figure 2 not present in Table 1? Also, can the authors provide per-game performance for the 11 games for SAC and DreamerV3?

5. Clarity: for exploration, can the authors provide more details about the two criterias being compared in Figure 3, bottom (i.e. in equations)? Further, I do not feel Figure 3 top is sufficiently well-explained to make sense. 

6. The effect of this new objective on exploration is very interesting, and I think worth investigating further. For instance by quantifying state coverage, and/or showing an illustrative exploration trace in simple environments? As an example, see Figure 2 and 7 of [Li 2024]. 

7. For clarity, can the authors provide equations of the objectives when “replacing the posterior with the policy and removing the regularizer term”? L451.

8. (L448) The word “disentanglement” has a lot of associated meanings in machine learning. Perhaps just “ablation” would suffice as the paragraph title. 

9. Nit pick: please use “\citep” and \citet” properly. For eg citations on L40, L57 (amongst others) should only be in a single bracket, and citations such as Dabney et al on L488 should use “citet”. 

[Li 2024] Li, Qiyang, et al. "Accelerating exploration with unlabeled prior data." Advances in Neural Information Processing Systems 36 (2024).

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes DRIVE, a novel distributional model-based reinforcement learning (RL) framework leveraging variational inference to address limitations in traditional RL approaches focused on expected return maximization. DRIVE introduces probabilistic learning proxies that incorporate aleatoric uncertainty within the return distribution, promoting risk-aware decision-making. The theoretical analysis demonstrates conditions for convergence, and empirical results on tasks from DMControl Suite highlight DRIVE's efficiency and its ability to balance exploration and exploitation.

### Strengths
Originality:
The integration of variational inference into distributional RL is novel, and facilitates a risk-aware decision-making approach

Significance:
The paper is well theoretically-founded and appears to be effective

Clarity:
The paper is well-written and logically structured

### Weaknesses
 - Although the paper emphasizes balancing exploration and exploitation, it lacks a detailed analysis of how can DRIVE balance exploration and exploitation during traning, it would be helpful to include a detailed discussion.

- The multi-term objective and the complex posterior approximation might lead to overfitting, especially in limited-data scenarios. Specifically, how does your method scale to high-dimensional and large action-space environments

- Missing reference: The paper does not address a comparison with bisimulation mode based approaches [1, 2, 3]. How does your method relate to representation learning [1] and reward shaping methods [2,3] that also utilize the bisimulation metric for learning transition and reward models? These methods can be categorized as model-based approaches connected to the optimal value function. Specifically, [3] also manages to encourage exploration without loss of exploitation by connecting the shaping reward with the value function. What advantages does DRIVE offer over these bisimulation model-based approaches?

### Questions
- Can the authors provide more concrete evidence or metrics that demonstrate how their method manages the exploration-exploitation trade-off across different tasks?

- How does the complexity of the variational bound affect the scalability of the method in large state-action spaces?

- What measures, if any, have been implemented to mitigate overfitting due to the complex objective function and posterior approximation
Speficifically, how does DRIVE perform in discrete-action games, e.g., atari games?

- What advantages does DRIVE offer over these bisimulation model-based approaches[1,2]? (see W3)

- Some parts of the theoretical analysis are dense. Could you provide more intuitive explanations or examples to help bridge the gap between the theory and its practical implications?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose a framework that leverages probabilistic inferencing to find locally-optimal policy from distributional value function. In particular, they propose a variational approach that, amongst other things, decouples the optimization problem from the regular value function. They provide a theoretical analysis in support of this framework, as well as empirical results in a broad range of continuous control tasks.

### Strengths
This paper provides a theoretical framework to find optimal policies in distribution RL, in which policy optimization does not fully utilize the distributional knowledge of value function in the existing literature. This is to complete the distributional approach to RL from end to end.

### Weaknesses
The ideas presented in the paper have potential, but overall, it lacks motivational discussion (or justification) on various components in the proposed framework: why model-based approach by address H-horizon, and Assumption 3.1. Also, discussion is missing on the impact of approximate transition model, the additional burden from model-based approach, impact of H.

The presentation of the experiments needs to be improved. In particular, by aggregating 11 experiments into a single figure (Fig. 2), we lose the ability to generate any meaningful insights as to which conditions may favor the author’s methods. Moreover, only some baselines are included in Figure 2, and soft-actor critic is excluded from Table 1, which is curious and not motivated in the text. Overall, there is no intuition provided by the authors as to why it makes sense to compare their method to the other methods, besides D4PG.

Finally, regarding the method proposed by the authors, I also have some concerns. First, the method appears to be much more computationally-expensive than, say, the more standard Distributional RL methods by Bellemare et al. (2017), due to the marginalization over the return, as well as the inclusion of Dreamer. Similarly, the inclusion of Dreamer would likely introduce some error into the learning processes, however this is not discussed or investigated by the authors.

### Questions
1.	Would Eq (4) be compatible with the Bellman Eq (2). Wouldn’t Eq (4) lead to entropy term in the reward?
2.	How do you define U_max in Assumption 3.1?
3.	The transition associated with the second inequality in Eq (9) is not clear to me.
4.	Where does Eq (13) come from?

### Soundness
3

### Presentation
2

### Contribution
3
