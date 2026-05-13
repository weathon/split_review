# Q-based Variational Inverse Reinforcement Learning

- Decision: Reject
- Scores: 3, 5, 8, 5

## Abstract
The development of safe and beneficial AI requires that systems can learn and act in accordance with human preferences. However, explicitly specifying these preferences by hand is often infeasible. Inverse reinforcement learning (IRL) addresses this challenge by inferring preferences, represented as reward functions, from expert behavior. We introduce Q-based Variational IRL (QVIRL), a novel Bayesian IRL method that recovers a posterior distribution over rewards from expert demonstrations via primarily learning a variational distribution over Q-values. Unlike previous approaches, QVIRL combines scalability with uncertainty quantification, important for safety-critical applications. We demonstrate QVIRL's strong performance in apprenticeship learning across various tasks, including classical control problems and safe navigation in the Safety Gymnasium suite, where the method's uncertainty quantification allows us to produce safer policies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper addresses scalability and posterior uncertainty estimation in Bayesian inverse Reinforcement Learning (RL) through Q-values variational inference for approximating reward posterior distributions. The methodology largely builds upon two existing works: (1) VAE [1]:  Adopts the concept of variational posterior yielding joint multivariate Gaussian distributions as a main standing point over this work, as shown in Figure 1, and the two posterior distributions are also assumed to be approximated well by Gaussian; (2) AVRIL [2]: the overall structure and key definitions are similar, from "apprenticeship learning", "learning a variational posterior over reward" to "Boltzmann distribution" in this paper. The authors compare their approach against both Bayesian inverse RL methods like [2] and state-of-the-art imitation learning approaches like [3]. However, there are significant concerns regarding both methodological innovation and experimental demonstration.

### Strengths
1. The idea and algorithmic structure including key definitions are foundational on existing literature, e.g., [1] and [2], which makes the overall structure of the paper generally easy to follow.

2. The paper adeptly integrates a multitude of concepts such as Bayesian Inverse reinforcement learning, apprenticeship learning, variational inference, and uncertainty estimation over Q-values. These topics have been at the forefront of recent research trends.

3. The paper is motivated to address safety-critical applications with a specific focus on scalability and uncertainty estimation, though the scalability claims lack evident support.

### Weaknesses
1. The paper has limited novelty: the central idea is heavily derived from existing work, particularly VAE [1] and AVRIL [2]. Although the authors attempt to distinguish their approach, such as through "uncertainty estimation over Q-values instead of a point estimate" (page 4), the paper lacks substantial novelty, with much of its contribution reflecting [2]. For instance, in Table 2, the reward outcomes show minimal improvement over baseline methods.

2. The work builds on established algorithms but does not address or resolve inherent limitations within them. For example, it assumes Gaussian approximations for the posterior distributions over Q-values and rewards—a limitation acknowledged in both [1] and [2]. Relying on Gaussian assumptions may restrict model accuracy since Gaussian distributions cannot capture all characteristics of arbitrary distributions. Furthermore, the paper employs a maximum entropy approach, which is not a true distance metric. More effective and precise metrics, such as those used in optimal transport, could enhance the results.

3. The contribution of "scalability" is weak. The paper does not provide theoretical support for scalability, and the little empirical evidence on page 8 is similarly insufficient.

4. Several typos - e.g., "finite state- and action ..." (page 2) and "the two closest prior methods for Bayesian inverse reinforcement." (page 7).

### Questions
1. What specific aspects of the approach contribute to improved scalability? And, How is scalability quantitatively demonstrated in experiments (and compared to AVRIL [2])? It appears that the proposed method does not improve on [2] in this regard.

2. In Equation 2, it would be great to justify the construction of likelihood p(r|D) over the Boltzmann rationality model in Equation 2.

3. How is the accuracy of the Gaussian-based posterior estimation ensured? Can the authors propose a metric or analysis to support this assumption? Given that the variational distribution is approximated as Gaussian, this question is critical when using variational inference.

__Reference__:

[1] Kingma, Diederik P. "Auto-encoding variational bayes." arXiv preprint arXiv:1312.6114 (2013).

[2] Chan, Alex J., and M. van der Schaar. "Scalable Bayesian Inverse Reinforcement Learning." International Conference on Learning Representations. 2021.

[3] Jarrett, Daniel, Ioana Bica, and Mihaela van der Schaar. "Strictly batch imitation learning by energy-based distribution matching." Advances in Neural Information Processing Systems 33 (2020): 7354-7365.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new method for scalable Bayesian inverse RL /
apprenticeship learning, where the posterior over reward functions is
approximated by variational inference over a class parameterized by
neural networks. Exploiting a bijection between Q-values and rewards
under a particular rationality model, the proposed QVIRL method can
maintain posteriors over Q-values, eliminating the need for a policy
optimization subroutine. Moreover, using the posterior over
action-values, the authors argue for (and experiment with) optimizing a
risk-averse utility during apprenticeship learning, to stay closer to
the demonstration data for the purpose of recovering a safe policy.
Through experiments on a variety of benchmarks, the authors shows that
QVIRL is often quite performant, often exceding the performance of all
baselines.

### Strengths
This paper presents a fresh approach to solving Bayesian IRL and
apprenticeship learning. I really appreciated the extent to which the
authors leveraged the Bayesian perspective—particularly with regard to
the posterior variance of inferred Q-values—to improve the safety of the
resulting apprentice policy. The empirical results appear to be quite
good. Moreover, the paper is expertly written—it was very easy to follow
and enjoyable to read.

### Weaknesses
The main weakness of the paper to me is that the consequences of the
various approximations made are not discussed explicitly or in detail.
For instance, under what circumstances would the mean-field
approximation of the likelihood cause problems?

Moreover, the reward prior does not appear to be discussed explicitly; I
see no mention of which prior was used in the experiments. There appears
to also be an assumption made on the reward prior in equation (10), that
is the priors over rewards for each state-action pair are independent.

Finally, it is not clear how many seeds were used for evaluation in the
deep RL tasks. In fact, it reads as though only one seed was used, which
makes it difficult to assess whether the performance improvements
presented are statistically significant.

### Questions
On line 226, what do you mean by a "variational distribution"?

Can you explain in further detail what the consequences are of the
approximation in equation (6)? Maybe a simple figure would be nice
(comparing say the density of the posterior of $\max Q$ vs that of
$Q(\cdot, \arg\max)$). Is this a novel contribution?

Why are there no confidence intervals for the SafetyGym results?

How many seeds are used in the experiments?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this work, the authors provide a novel method for performing Bayesian Inverse RL which learns a Bayesian posterior over the Q values and derives a Bayesian posterior over rewards using the inverse Bellman equation. This improves over prior work (AVRIL) by learning a posterior over Q-values in addition to rewards, allowing the learnt posterior to be directly used to induce risk averse apprentice policies. Primarily, this is enabled by using the mean-field approximation proposed by Lu et al. to approximate the data likelihood. The authors show that their method is competitive with prior work in non-risk averse settings across multiple environment domains but with lower computational requirements. Importantly, the authors also demonstrate how the posterior over Q-values can be used to directly derive a risk averse policy that significantly outperforms prior work in terms of constraint violations on benchmark safety-constrained tasks.

### Strengths
- The paper is well written, easy to follow and understand. The derivations are clear
- The work is well-motivated - there is a clear need for better Bayesian IRL methods
- The authors evaluate their method across multiple environment domains and compare to several different baseline algorithms
- The authors evaluate their method over 10 seeds and (mostly) include errors bars/confidence intervals on the results
- The results are quite convincing, particulalry in the safety domain.
- The authors include an extensive limitations discussion

### Weaknesses
 - In my opinion, it should be made more clear that the method uses an expert and non-expert (unlabeled) dataset. It is discussed in the Appendix that an additional unlabeled dataset of non-expert trajectories is used to estimate Eq. 6 in all experiments. Moreoever, it is not clear, which, if any of the baselines use an additional unlabeled dataset. The incorporation of an unlabeled dataset with transitions outside of the expert state distribution could substaintially improve online by providing the policy with additional knowledge of the dynamics of the MDP. It would preferable to compare to basleines that also incorporate this offline dataset (if the current baselines do not). In either case, it should be noted more prominently that this additional dataset is used in the experiments.
- I think it would be better if you could fit the discussion of extension to the case of unknown dynamics into the main paper. This is of primary interest since the prior methods you are comparing to all operate in the case of unknown dynamics and this is the typical setting for IRL.
- There are no confidence intervals in Table 2.

### Questions
- In sec 4.3 you state that: "These experiments were run in the online setting, where additional
auxilliary trajectories for evaluating the KL term are sampled from the apprentice policy throughout
the training. The baselines – BC, Inverse Soft Q-Learning (IQ; Garg et al. 2021), and AVRIL – were
run in the usual imitation learning setting."
Does this mean that you are comparing your method which is allowed online interactions with purely offline methods? Can you clarify what the "usual imitation learning setting" is?

- It would be interesting to see how your results in the safety domains change with different numbers of demonstrations. In theory regular IRL methods should also avoid the constraints given enough demonstrations since the expert trajectories are non-violating. Presumably the advantage of your method is that the constraints can be avoided with much fewer trajectories - but how many fewer?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a scalable Bayesian approach to inverse reinforcement learning (IRL) by learning a posterior distribution over Q-values instead of point reward estimates. This method enhances uncertainty quantification and robustness, particularly in safety-critical applications. QVIRL is demonstrated to be effective across various control problems and tasks.

### Strengths
QVIRL uses 1) variational inference for efficient learning, making it scalable to complex environments, 2) models uncertainty which provides robust, risk-averse policies by capturing uncertainty over rewards and 3) reduces computation time compared to MCMC-based IRL methods.

### Weaknesses
1. Sec 3 is a little bit stacked, so I recommend the authors provide a pseudo-code of their method for better clarity.
2. The algorithm described in Section 3 addresses discrete scenarios, while its extension to continuous actions relies on naive random sampling, which often fails to focus efficiently on relevant actions.

### Questions
1. Part of the legend in Figure 2 is missing. Also, the color in Fig 2 is too light to look clearly and the mean curve is missing. Also, where is random and expert?
2. There are also constraint inference works in safe-critical IRL, such as [1] and [2]. Why don’t the authors include them as baselines in evaluating QVIRL’s performance in Safety Gymnasium (Sec 4.3)?
3. The code is not provided, so I can not verify the experiment part.

[1] Hugessen, A., Wiltzer, H. and Berseth, G., 2024. Simplifying constraint inference with inverse reinforcement learning. In *First Reinforcement Learning Safety Workshop*.

[2] Malik, S., Anwar, U., Aghasi, A. and Ahmed, A., 2021, July. Inverse constrained reinforcement learning. In *International conference on machine learning* (pp. 7390-7399). PMLR.

### Soundness
2

### Presentation
2

### Contribution
2
