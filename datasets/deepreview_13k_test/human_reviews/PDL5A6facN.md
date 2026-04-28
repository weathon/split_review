# Accelerated Policy Gradient: On the Nesterov Momentum for Reinforcement Learning

- Decision: Reject
- Scores: 5, 6, 6, 5

## Abstract
Policy gradient methods have recently been shown to enjoy global convergence at a $\Theta(1/t)$ rate in the non-regularized tabular softmax setting. Accordingly, one important research question is whether this convergence rate can be further improved, with only first-order updates. In this paper, we answer the above question from the perspective of momentum by 
adapting the celebrated Nesterov's accelerated gradient (NAG) method to reinforcement learning (RL), termed \textit{Accelerated Policy Gradient} (APG). To demonstrate the potential of APG in achieving faster global convergence, we start from the bandit setting and formally show that with the true gradient, APG with softmax policy parametrization converges to an optimal policy at a $\tilde{O}(1/t^2)$ rate. 
To the best of our knowledge, this is the first characterization of the global convergence rate of NAG in the context of RL.
Notably, our analysis relies on one interesting finding: Regardless of the initialization, APG could end up reaching a locally-concave regime, where APG could benefit significantly from the momentum, within finite iterations.
By means of numerical validation, we confirm that APG exhibits $\tilde{O}(1/t^2)$ rate in the bandit setting and still preserves the $\tilde{O}(1/t^2)$ rate in various Markov decision process instances, showing that APG could significantly improve the convergence behavior over the standard policy gradient.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the use of Nesterov’s accelerated gradient onto policy gradient. The work terms this methods accelerated
policy gradient. This improves the convergence rate from $O(1/t)$ to $O(1/t^2)$, provided that one has access to the true gradient. The work points out the intuition how the acceleration is benefited from the momentum. 

The results are based on several assumptions on the RL problem structure. First, the surrogate initial state distribution has to be strictly positive for every state. Second, the optimal action has to be unique at every state.

Some numerical test are provided in the manuscript.

### Strengths
1. The work uses Nestrov acceleration on policy gradient and improves the convergence rate.
2. Techniques used in the proofs could be of independent interest.

### Weaknesses
One major concern is on the assumptions, especially Assumption 3 and Assumption 4. I believe these assumptions are way too strong, and drastically reduce the complexity of reinforcement learning problems and make the optimization landscape much easier to tackle with. The setting of true gradient and initial state distribution are also strong, though acceptable. I would prefer if the work, that claims they are the first to achieve Nestrov acceleration on PG, to be under a much more general setting.

### Questions
N/A

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the convergence of Accelerated Policy Gradient (APG) with restart as shown in Algorithm 2. The main results show that this algorithm achieves a $\tilde{O}(1/t^2)$ convergence rate toward globally optimal policy in terms of value sub-optimality. The technical innovation includes showing that the value function is nearly $C$-concave when optimal action's probability is large enough (locally around optimal policy), as well as using AGD's $\tilde{O}(1/t^2)$ convergence results, and asymptotic global convergence in Agarwal et al.

### Strengths
1. Answering whether Nesterov's acceleration can be used in policy gradient is an interesting question.
2. The technical challenges are well explained and real, including using momentum in non-convexity, and unbounded parameters.
3. The simulations verify the proved rates.

### Weaknesses
1. There already exist acceleration methods for policy gradient, including natural policy gradient, and normalization which both lead to an exponential convergence rate, which might make this slower acceleration not that attractive to the community.

### Questions
1. How do you compare the acceleration provided by momentum with faster acceleration methods for policy gradient, such as natural policy gradient and normalization, as well as regularization?

2. Any idea of using generalizing the methods to stochastic settings, where the policy gradient has to be estimated from samples?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the Nesterov accelerated gradient method in the context of reinforcement learning. The authors theoretically show that with the true gradient, the proposed accelerated policy gradient with softmax policy parametrization converges to an optimal policy at a $O(1/t^2)$ rate. The empirical evaluation further demonstrates that APG exhibits $O(1/t^2)$ rate and APG could significantly improve the convergence behavior over the standard policy gradient.

### Strengths
In general, this paper is well-structured, and the main idea of this work is easy to follow. This paper proposes a novel accelerated policy gradient method with a fast $O(1/t^2)$ convergence rate, which is the first Nesterov accelerated method with a provable guarantee in reinforcement learning. The authors of this paper also develop a new technical analysis for the proposed method to prove its convergence rate. The authors also conduct experiments to verify the efficiency of the proposed method empirically.

### Weaknesses
(1) The major concern about this work is that the authors did not present a detailed discussion of the work [1]. The work [1] has shown that a linear convergence rate, which is faster than $O(1/t^2)$, can be achieved by the policy gradient with an exponentially increasing step size. Moreover, the result in [1] is also based on the non-regularized MDP, which is the same setting as in this submission. The authors need to provide a detailed comparison of the theoretical results in [1] and this submission and also discuss the significance of the result in this submission, given the linear convergence rate in [1].  


(2) Additionally, since this work discusses the lower bound of policy gradient, it is interesting to show why the linear convergence rate in [1] does not conflict with the lower bound provided in this submission.


(3) The upper bound in this paper has a dependence on the factor $||\frac{1}{\mu}||\_\infty$. The recent work on policy gradient, e.g., [1] [2], has a convergence rate dependent on a tighter factor $||\frac{d\_{\rho}^{\pi\_*}}{\mu}||\_\infty$. Is it possible to sharpen such a factor in the result of this submission?


[1] Lin Xiao. On the convergence rates of policy gradient methods. Journal of Machine Learning Research, 23(282):1–36, 2022.

[2] Alekh Agarwal, Sham M Kakade, Jason D Lee, and Gaurav Mahajan. On the theory of policy gradient methods: Optimality, approximation, and distribution shift. Journal of Machine Learning Research, 22(1):4431–4506, 2021.


=================After rebuttal===================

Thanks for addressing my concerns. I raise my score accordingly.

### Questions
Please see the above section.

### Soundness
3 good

### Presentation
2 fair

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
This paper presents a novel RL algorithm based on Nesterov Accelerated Gradient (NAG) to improve the convergence rate. Specifically, the authors adapt the NAG into policy gradient to develop APG and mathematically show the global convergence rate of $\tilde{\mathcal{O}}(1/t^2)$, which is faster than the existing $\mathcal{O}(1/t)$., with the true gradient and softmax policy parameterization. The authors also show that regardless of initialization, APG is able to reach a locally nearly-concave regime, within finite iterations. To validate the theory, the authors use two simple benchmarks to demonstrate that APG outperforms the standard PG.

### Strengths
The investigated topic of convergence rate improvement for RL is important and interesting. This work seems theoretically strong in analysis by combining two well-known methods, NAG and PG to improve the rate. Such a combination is simple and straightforward. The paper is well written and easy to follow.

### Weaknesses
1. The novelty is incremental. APG is not novel in terms of the algorithmic framework. 

2. Some assumptions to characterize the analysis are strong and not justified well. Why is Assumption 1 required to guarantee the convergence? Please justify in the paper. Otherwise, it might be a strong condition in the work. How likely is the assumption satisfied in the various real-world scenarios? What is the point to have Assumption 2? Not a more generic range [-R, R] in many existing works? Why is Assumption 4 is required for the convergence? I understand it could be attained in practice.

3. In Theorem 1, the authors mentioned that the softmax parameterized policy is tabular. What does it mean by tabular here? Would it mean the policy acts like a lookup table? Do the conclusions still apply if removing tabular? It is confusing in the paper.

4. The experimental results are not promising. The benchmark models are quite simple. The authors should present more complex benchmark models. Continuous environment should be utilized to showcase APG's superiority. 

5. Definitions 1 and 2 are a bit ah-hoc for the convergence proof in this work. If they are existing, the authors should cite references. Otherwise, the author should justify why they are needed.

6. Section 6.2 did not really present anything new on the lower bound. How to relate Theorem 3 to APG? The authors only said due to Theorem 3, there was no tighter lower bound for APG. This seems to me quite simple. They should show the contradiction if there existed a tighter lower bound for APG.

I think the paper still requires a substantial amount of work to make it technically solid and sound.

************************Post-rebuttal*****************************
Thanks the authors for addressing my comments and revising the paper with additional results. I really appreciate that. After carefully reviewing the rebuttal and comments from other reviewers, I have raised my score. While the assumptions to me are a still a bit strong in this work.

### Questions
Please see the questions in the weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
