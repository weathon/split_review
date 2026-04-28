# Non-Asymptotic Analysis for Single-Loop (Natural) Actor-Critic with Compatible Function Approximation

- Decision: Reject
- Avg Score: 6.67
- Scores: 6, 6, 6, 6, 8, 8

## Abstract
Actor-critic (AC) is a powerful method for learning an optimal policy in reinforcement learning, where the critic uses algorithms, e.g., temporal difference (TD) learning with function approximation, to evaluate the current policy and the actor updates the policy along an approximate gradient direction using information from the critic. This paper provides the \textit{tightest} non-asymptotic convergence bounds for both the AC and natural AC (NAC) algorithms. Specifically, existing studies show that AC converges to an $\epsilon+\varepsilon_{\text{critic}}$ neighborhood of stationary points with the best known sample complexity of $\mathcal{O}(\epsilon^{-2})$ (up to a log factor), and NAC converges to an $\epsilon+\varepsilon_{\text{critic}}+\sqrt{\varepsilon_{\text{actor}}}$ neighborhood of the global optimum with the best known sample complexity of $\mathcal{O}(\epsilon^{-3})$, where $\varepsilon_{\text{critic}}$ is the approximation error of the critic and $\varepsilon_{\text{actor}}$ is the approximation error induced by the insufficient expressive power of the parameterized policy class.  This paper analyzes the convergence of both AC and NAC algorithms with compatible function approximation. Our analysis eliminates the term $\varepsilon_{\text{critic}}$ from the error bounds while still achieving the best known sample complexities. Moreover, we focus on the challenging single-loop setting with a single Markovian sample trajectory. Our major technical novelty lies in analyzing the stochastic bias due to policy-dependent and time-varying compatible function approximation in the critic, and handling the non-ergodicity of the MDP due to the single Markovian sample trajectory.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper conducts a convergence analysis of actor-critic and natural actor-critic algorithms with compatible function approximation, under the single-loop setting that uses onse sample trajectory. The paper presents the tightest convergence bound in both cases.

### Strengths
- The paper presents the tightest non-asymptotic bound for the covergenace of AC and NAC algorithms, compared to existing work. The results show that compatible function approximation 
- To obtain the tightes bound, paper presents novel technical contributions to analyze the single-trajectory setting and avoid decoupling of the actor and critic updates. The setting considered in this paper is closer to practice.

### Weaknesses
 - The main contributions of the paper are limited to novel techniques in the analysis of well-known algorthms and theoretical evidence on why compatible function approximation might be advantageous. I am uncertain about potential impact of this work either on practice or theory.

### Questions
Could you please clarify whether/how the techniques or results presented in this paper could be useful in practice, for instance, through the development of new algorithmic ideas, or in theory, such as analysis techniques being potentially useful to analyze other algorithms?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper provides the tightest non-asymptotic convergence bounds for both the AC and natural AC (NAC) algorithms. Specifically, existing studies show that AC converges to an $\epsilon+\epsilon_{critic}$ neighborhood of stationary points with the best known sample complexity of $O(\epsilon^{-2})$, and NAC converges to an $\epsilon+\epsilon_{critic}+\sqrt{\epsilon_{actor}}}$ neighborhood of the global optimum with the best known sample complexity of $O(\epsilon^{-3})$, where $\epsilon$-critic is the approximation error of the critic and εactor is the approximation error induced by the insufficient expressive power of the parameterized policy class. This paper analyzes the convergence of both AC and NAC algorithms with compatible function approximation. The major technical novelty lies in analyzing the stochastic bias due to policy-dependent and time-varying compatible function approximation in the critic, and handling the non-ergodicity of the MDP due to the single Markovian sample trajectory.

### Strengths
This paper focuses on the challenging single-loop setting with a single Markovian sample trajectory. To develop the tightest bound, this paper develops a novel approach that bounds the tracking error as a function of the policy gradient norm (for AC) and the optimality gap (for NAC). Their analysis for NAC does not need the smoothness assumption on the parameterized policy, which is typically required in existing NAC and AC analyses.

### Weaknesses
1. I don't understand the second equal sign of equation (5), why it holds true? Do you need to assume $Q^{\pi_w}=\phi^\top_w\bar{\theta}^*_w$? Also, given equation (5), it is unclear why "This implies that as long as we can solve the finite dimensional problem Equation (4), linear function approximation with the compatible feature and parameter does not induce any function approximation error." could you elaborate on that?

2. why $\phi^\top\phi$ is a matrix in eqn(8)? in this case $\phi^\top \theta$ is also a matrix instead of a scalar?

3. For NAC analysis, you need an additional Assumption 3. Could you explain why this is needed for NAC but not for AC? Also, how is this related to the single concentrability coefficient defined for offline RL (def1 of [1], assumption3 in [2])?

[1] Bridging offline reinforcement learning and imitation learning: A tale of pessimism, NeurIPS21,
[2] Towards Instance-Optimal Offline Reinforcement Learning with Pessimism, NeurIPS21.

4. You mentioned "Our major technical novelty lies in analyzing the stochastic bias due to policy-dependent and time-varying compatible function approximation in the critic, and handling the non-ergodicity of the MDP due to the single Markovian sample trajectory." Where can I find the detail of this novelty in the paper?

### Questions
Please answer the questions above.

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
This paper presents a non-asymptotic analysis for single-loop Actor-Critic (AC) and Natural Actor-Critic (NAC) algorithms with compatible function approximation. The authors provide tight convergence bounds for both AC and NAC algorithms, eliminating the non-diminishing constant term $\varepsilon_{critic}$ from the error bounds while maintaining the best known sample complexities. The paper focuses on the challenging single-loop setting with a single Markovian sample trajectory and analyzes the stochastic bias due to policy-dependent and time-varying compatible function approximation in the critic.

### Strengths
The paper is well-structured and presents a clear analysis of the convergence properties of AC and NAC algorithms with compatible function approximation. The authors develop the tightest non-asymptotic convergence bounds for both AC and NAC algorithms with compatible function approximation. For the AC algorithm, they achieve the best sample complexity of $O(\varepsilon^{-2})$ with a reduced error from $\varepsilon + \varepsilon_{critic}$ to $\varepsilon$. For the NAC algorithm, they achieve the best known sample complexity of $O(\varepsilon^{-3})$ with a reduced error of $\varepsilon+\sqrt{\varepsilon_{actor}}$.

### Weaknesses
1. It is unclear how the result in the paper compared with other non-asymptotic analyses with compatible function approximation. Also, it would be nice to demonstrate the technical challenges in combining (natural) actor-critic with compatible function approximation in a more detailed way. 

2. $\varepsilon_{critic}$ can be small when using a neural function approximator, so it is unclear how important it is to eliminate such an error in real-world scenarios. While this is a theoretical work, it would be nice to include some experiments demonstrating the importance of eliminating $\varepsilon_{critic}$.

### Questions
See the weakness section above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper provides tight analyses for non-asymptotic convergence bounds of actor-critic and natural actor-critic algorithms on single-trajectory single-loop online RL problems.

### Strengths
I think this work really pushes the RL community research efforts further by answering:

> can we give tight analyses for non-asymptotic convergence bounds of actor-critic and natural actor-critic algorithms on single-trajectory single-loop online RL problems?

The main contribution of improvement of results is worthy for publication.

### Weaknesses
Firstly, I only took a closer look at AC sample complexity analyses (Lemma 7, 8, 10, and Proposition 6) and everything seemed alright.

I have only a few weakness for this work as follows:

- The main paper writing needs to be improved. Yes, the soundness of this paper is excellent. But right from Section 1.2, it's just about "getting sota results compared to other works". The main analyses idea in this work compared to others which helps improve the bounds are missing. To be honest, I am only familiar with high level analyses of (Chen et al 2022) and few generic two-timescale algorithms, which shares the AC analyses in this work. But I am totally missing the improvement bounds provided here! Just providing one line (below quote) as the core idea for the whole 50 pages analyses paper, does not provide any useful information.
> In this paper, we design a novel approach to explicitly bound this error. The central idea is to construct an auxiliary eligibility trace with fixed feature to approximate the eligibility trace with time-varying feature (in the critic, we use k-step TD with compatible function approximation).

So please write more discussions and details for the main results and proof ideas. I understand this is presentation is limited by page restriction, but it can be done through a thorough writing process. For example, AC results can be pushed to appendix looking at the generality of NAC, or the other way around.

- This paper considers average MDP formulation. Most of the comparisons in Table 1 and 2 are in the discounted setting. Please mention these important differences and make fair comparisons by arguing the connection between the two settings. I am not sure if this distinction is what is helping to reach current bounds. Thus my point above is super critical for the quality.

### Questions
-na-

### Soundness
4 excellent

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors develop tightest non-asymptotic convergence bounds for both Actor-critic (AC) and natural AC (NAC) algorithms with compatible function approximation. The major technical novelty lies in analyzing the stochastic bias due to policy-dependent and time-varying compatible function approximation in the critic, and handling the non-ergodicity of the MDP due to the single Markovian sample trajectory. This is a nice theoretical contribution for the area of reinforcement learning.

### Strengths
The authors develop tightest non-asymptotic convergence bounds for both Actor-critic (AC) and natural AC (NAC) algorithms with compatible function approximation. The major technical novelty lies in analyzing the stochastic bias due to policy-dependent and time-varying compatible function approximation in the critic, and handling the non-ergodicity of the MDP due to the single Markovian sample trajectory. This is a nice theoretical contribution for the area of reinforcement learning.

### Weaknesses
There is no discussion on the weakness or limitation of theoretical results, even in the conclusion part.

### Questions
What are the limitations of the analysis presented in this paper? How to verify the assumptions made in practice?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper provides an improved analysis of the actor-critic algorithm. It introduces compatible function approximation to compute the value function, which eliminates the critic approximation error, while keeping the state-of-the-art rate in the sample complexity.

### Strengths
The paper is easy to follow. The main idea is clearly stated and makes sense. The paper delivers interesting results, which justify the novelty of the work.

### Weaknesses
1. Since the compatible function approximation (5) is not a straightforward fact, it's better to restate this conclusion in the form of a proposition. It could also be helpful if a quick proof can be attached in the appendix. 

2. A high-level roadmap of the proof is appreciated. It could make it easier to follow the proof as it's already notation heavy.

### Questions
I didn't read the proof in detail. But intuitively, in the previous works, the source of $\varepsilon_{\textrm{critic}}$ is the previous proof needs to bound a term like $\Vert\nabla_\omega J(\pi_\omega) - \mathbb{E}[Q_\theta^{\pi_\omega}\nabla_\omega\log\pi_\omega(a\vert s)]\Vert^2$, which is the difference between the true gradient and the estimated gradient using the value function class. However, due to the authors' setting, this term automatically becomes 0. In this case, why can't one reuse the previous proofs, just replacing this term by 0? Does the introduction of compatible function approximation leads to new difficulties that need additional theoretical novelty to overcome them?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
