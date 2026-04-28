# Robust Thompson Sampling Algorithms Against Reward Poisoning Attacks

- Decision: Reject
- Avg Score: 4.50
- Scores: 3, 6, 6, 3

## Abstract
Thompson sampling is one of the most popular learning algorithms for online sequential decision-making problems and has rich real-world applications. However, current Thompson sampling algorithms are limited by the assumption that the rewards received are uncorrupted, which may not be true in real-world applications where adversarial reward poisoning exists. To make Thompson sampling more reliable, we want to make it robust against adversarial reward poisoning. The main challenge is that one can no longer compute the actual posteriors for the true reward, as the agent can only observe the rewards after corruption. In this work, we solve this problem by computing pseudo-posteriors that are less likely to be manipulated by the attack. We propose robust algorithms based on Thompson sampling for the popular stochastic and contextual linear bandit settings in both cases where the agent is aware or unaware of the budget of the attacker. We theoretically show that our algorithms guarantee near-optimal regret under any attack strategy.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work studies the setting where the revealed rewards are corrupted. So, the learning agent cannot use the true reward to do posterior sampling. They consider two bandit variants with corruption: stochastic bandit and linear contextual bandit. They also propose efficient algorithms.

### Strengths
a new problem

### Weaknesses
problem set up: I still think the proposed problem is a special case (actually a simpler case) of differentially private online learning, based on lines 149 to 151. Specifically, the corruption model, where the total magnitude of corruption is bounded, seems analogous to a privacy budget constraint. The core idea of limiting the impact of corrupted rewards on the learning process appears similar to the goals of differential privacy, which aims to limit the influence of individual data points. 

proposed algorithms: they is not that interesting nor novel, simply re-shaping the posterior distribution in an optimistic way. This idea has been used in Hu and Hedge, 2022.

### Questions
1. what does not mean of "optimality in the face of corruption" in line 65?

2. In line 795, the constant is 72 e^{64}. You can improve the constant by using some analysis in https://arxiv.org/abs/2407.14879.

Also, I think the aforementioned paper is quite related to this work.

### Soundness
2

### Presentation
3

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
This paper proposes first near-optimal variants of Thompson sampling for stochastic bandit and contextual linear bandit problems with adversarial reward poisoning.

### Strengths
This is the first work providing variants of Thompson sampling for this class of problems.
Proposed algorithms are near-optimal and, being based on Thompson sampling, they inherit the advantages of Thompson sampling over approaches based on optimism in face of uncertainty.

### Weaknesses
Previous works are mentioned in the introduction and related works section. However, comparing existing results requires finding each cited paper and going through them one by one. It would be better if a table was included with previous works.

typos:
At the end of Sections 4 and 5, the paper (He et al., 2022) should be cited instead of (He et al., 2023).

### Questions
What can be said about Bayesian regret?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper considers poisoning attacks in multi-armed bandit setting. More specifically, the authors consider Thompson sampling algorithms and aim to design corruption-robust versions of these algorithms. They propose two algorithms, for stochastic and contextual linear settings, respectively, robust to poisoning attacks against an attacker that has limited corruption budget. The authors argue that their results are near-optimal, and they provide simulation results comparing their approaches to validate their theoretical findings.

### Strengths
- The paper is interesting and enjoyable to read. It clearly explains the most important ideas and positions its contributions well with respect to prior work on corruption-robust bandits.
- To my knowledge, prior work has not studied Thompson sampling algorithms that are robust to reward poisoning attacks. The proof techniques in the paper appear to be standard, but I found the analysis non-trivial. While I didn't check all the proofs in great detail, the arguments provided in the proof sketches appear sound.
- The proposed algorithms are simple extensions of existing methods and are based on adjusting the posteriors to make them less susceptible to manipulation. The upper bounds on the regret of the proposed algorithms are near-optimal, as argued in the paper, with the arguments relying on the lower bounds from prior work. 
- The paper supports its theoretical results with experiments.

### Weaknesses
 - While I found the results interesting, they are also somewhat expected, given the findings from prior work on poisoning attacks and corruption robustness in bandits.
- The experiments related to the stochastic MAB setting do not include a corruption-robust baseline. For the contextual bandit setting, the performance of the proposed method is similar to the corruption-robust baseline but is often worse. It would also be useful to include a richer set of attack strategies in the experiments.
- While I believe that the paper is overall well-written, the presentation could be improved and polished. There are quite a few typos in the text, and some of the figures in the experimental section do not adequately label the axes on the plots (see Figs. 2 and 4). Moreover, the fonts in the figures are too small. It also seems that some references are cited incorrectly. For example, the paper frequently cites He et al. (2023), which appears to be about *Nearly Minimax Optimal Reinforcement Learning for Linear Markov Decision Processes*. It would be helpful if the authors clarified this.
- I did not fully follow the intuition behind Algorithm 2 and the corresponding proof sketch. More specifically, it would be helpful if the authors elaborated further on their two remarks:
- *...the attacker can apply less influence on the estimator by corrupting such data...*,
- *...variance of the posterior distribution is limited due to the weighted estimator under reward poisoning...*

### Questions
I did not fully follow the intuition behind Algorithm 2 and the corresponding proof sketch. More specifically, it would be helpful if the authors elaborated further on their two remarks:
- *...the attacker can apply less influence on the estimator by corrupting such data...*, 
- *...variance of the posterior distribution is limited due to the weighted estimator under reward poisoning...* 

Please see *Strengths* and *Weaknesses* for my other comments and questions.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper studies the performance of Thompson Sampling for stochastic Gaussian bandits and contextual Gaussian $d$-dimensional linear bandit problems with Gaussian prior. Starting from the prior distribution over the "reward-parameter", the Thompson Sampling algorithm works by randomly selecting actions according to their posterior probability of being optimal. More specifically, at each time step, it samples a "reward-parameter" estimate from the posterior distribution conditioned on the history and selects the optimal action for the sampled parameter estimate given the context.  

In this work, the authors study the case where the rewards can be corrupted by an adversary with full knowledge of the "reward-parameter", the history, the current context and the random reward before attack. The adversary perturbs the reward with an additive perturbation. The sum of absolute perturbation, $C$, is referred to as the budget of the attack or the corruption level and is assumed to be finite. The authors propose two modifications of the Thompson Sampling to mitigate the effects of the adversarial attacks on the algorithm's performance. The first algorithm, developed for Gaussian stochastic bandits with Gaussian prior, uses an optimistic biased distribution over the reward-parameters to compensate for potential reward attacks. The authors claim that they have derived a bound of order $O(\sqrt{NT \log(N)} + N\overline{C} + N)$ on the expected regret, where $N$ is the number of arms, $T$ is the number of time steps and $\overline{C}$ is the "robustness level", a parameter of the algorithm that is assumed to be greater than $C$. It has to be noted that the constant term in the bounds is of the order $10^{29}$. 

The second algorithm, developed for contextual Gaussian $d$-dimensional linear bandit problems with Gaussian prior,  works by weighting the posteriors updates inversely proportional to the weighted 2-norm of the current context.  The authors derive a probabilistic bound on the expected regret. 


The authors then perform experiments to demonstrate the performance of their modified Thompson Sampling algorithms. The first experiment compares the performance of their first algorithm against UCB and TS for Gaussian stochastic bandits with Gaussian priors. The second experiment compares the performance of their first algorithm against UCB and TS for contextual Gaussian $d$-dimensional linear bandit problems with Gaussian prior.

### Strengths
The main strength of the paper is to propose modifications to the Thompson Sampling algorithm to mitigate the effects of adversarial reward attacks.

### Weaknesses
Although adapting the Thompson Sampling to adversarial reward attacks is an interesting idea, the paper suffers from several weaknesses listed below (the order does not reflect a hierarchy in the severity of the weaknesses).

- The first weakness concerns the considered settings. The authors considered a very limited settings as they assume that "the priors for the rewards of the arms and the reward parameters are Gaussian distributions" [lines 172-173]. They later claim that their algorithm can be "in principle" extended to general priors without giving any detail or example to support their claim. More problematic, their derived regret bounds (Theorem 4.1 and 5.1) rely extensively on those assumptions and do not hold for general priors. Specifically, the Gaussian nature of the prior is crucial in simplifying the posterior update rules and deriving closed-form expressions for the expected regret. Extending these results to non-Gaussian priors would likely require significantly different proof techniques and may lead to substantially different regret bounds. This limitation regarding the scope of the paper needs to be included in the title, the abstract, and the introduction. 
- A second weakness concerns the result derived in Theorem 4.1. Following the last part of the proof in the Appendix, the authors forgot to sum over all the possible $ N $ arms. Taking the sum over all possible arms leads to a regret bound of order $O(N^{3/2}\sqrt{T \log(N)} + N^{2}\overline{C} + N^{2})$. Another concern regarding the regret bound is the enormous multiplicative constant $72(e^{64}+5) \approx 10^{29}$, which raises the question of whether this bound can be applicable in practice. Such a large constant effectively renders the bound vacuous for any realistic values of $N$ and $T$. Even for small-scale problems, the regret bound would be astronomically large, making it difficult to draw any meaningful conclusions about the algorithm's performance.
- Another weakness concerns the clarity of the paper and the presentation of the proofs. Notations are at best cumbersome (e.g., $x_{i(t)}(t)^T\mu$), sometimes incoherent (e.g., the history denoted $H_{t-1}$ in the paper and later changed to $F_{t-1}$ in the appendix, mixing notations $\theta$ and $\Theta$), incomplete (e.g., summation symbols without above limit $\sum_{t=1}$ [line 133]), or simply not defined (e.g., $\tau_k$, $\Delta_i$, $\overline{E_i^\theta(t)}$, $\overline{E_i^\mu}(t)$, $c_s$, $L_i(T)$). This seriously hinders the clarity of the paper and the ability to evaluate the proof's correctness. Although the single column allows enough space to write on a single line, authors often split equations or even expressions. Examples can be found on lines 311 to 315 or 684 to 690. The authors also use overfull lines, such as on line 1033. Often, proofs consist simply of a long chain of equalities and inequalities with no justification given to the reader. Sometimes, the authors cite results from previous papers without providing any reference. Overall, the appendix seems to have been written to discourage readers or make it impossible for them to verify the proof. 
- One more weakness concerns the writing of the paper. This reviewer believes that at least parts of the paper have been written by generative AI tools. Indeed, parts of the paper present typical AI writing patterns, such as repetition of ideas and phrases, overuse of specific writing structures, and generic or high-level descriptions. One example is in the introduction between lines 36 and 47:
    "[...]Thompson sampling has several advantages:
  - Utilizing prior information: By design, Thompson sampling algorithms utilize and benefit from the prior information about the arms.
  - Easy to implement: While the regret of a UCB algorithm depends critically on the specific choice of upper-confidence bound, Thompson sampling depends only on the best possible choice. This becomes an advantage when there are complicated dependencies among actions, as designing and computing with appropriate upper confidence bounds present significant challenges Russo et al. (2018). In practice, Thompson sampling is usually easier to implement Chapelle \& Li (2011).
  - Stochastic exploration: Thompson sampling is a random exploration strategy, which could be more resilient under some bandit settings Lancewicki et al. (2021).
    Despite the success, Thompson sampling faces the problem of [...]"

- Another weakness concerns the experiments performed by the authors. First, one can deplore that the adversarial attacks are not explained. The specifics of the attack strategy, such as the target arm selection and the magnitude of perturbations, are crucial for understanding the algorithm's performance under different attack scenarios. Second, for the stochastic bandit experiment, one can regret that the proposed algorithms are not compared against any other robust algorithm from the literature. Third, the plotted results raise serious questions regarding the quality of the experiments:  
  - on Figure 1, the left and right plots seem to present the same data although their respective titles claim otherwise.
  - on Figure 1 and Figure 2, the expected regret of TS seems not just close but almost exactly equal to the expected regret of UCB. 
  - on the top part of Figure 2, the titles of the $x$-axes are almost not readable.
  - on the bottom part of Figure 2, it seems impossible to explain how the expected regret of the proposed algorithm can decrease when the adversarial budget increases. This strongly suggests that there is a mistake in the experiments. The observed decrease in regret with increasing adversarial budget is counterintuitive and contradicts the expected behavior of a robust algorithm. One would expect the regret to increase or at least remain stable as the attack budget increases. 
  - another incoherence in the displayed results that indicated an error in the experiments is the fact that on the top part of Figure 2, the robust version of Thompson Sampling seems to outperform the original Thompson Sampling and UCB algorithm \emph{even with no adversarial attack} (when the adversarial budget is $0$). This simple \emph{sanity check} strongly suggests some mistakes in the code. 
  - there seem to be confidence intervals associated to each point on the plots but no information is given about the level of confidence they represent. 
  - the code for running the experiments is provided without a readme.txt file, or a single comment explaining how to run the code or what is the purpose of the different files and functions. It was therefore not possible to verify the soundness of the experiments.

### Questions
Here is a list of suggestions for the authors. 

- The first suggestion would be to entirely rewrite the proofs of Theorem 4.1 and Theorem 5.1 in the Appendix. Make sure to properly introduce all the notation with clear definitions to justify all the steps in your proofs (equalities, inequalities, the use of some lemma,….) to provide reference to all the lemmata you borrow from previous work. To the best of your capacity, try to write the proofs in a pedagogical way such that a reader familiar with the work can easily follow and asses the steps in the reasoning. 
- The second suggestion is for the authors to verify and clarify the omission in the last step of Theorem 4.1’s proof regarding the summation over all arms.
\item The third suggestion is for the authors to provide more details supporting their claim that the algorithm and regret bounds can be extended to general priors. If this is not possible, the authors would have to change the title, abstract, and introduction to acknowledge the limited scope of the work. 
\item A fourth suggestion concerns the experimental results. For the Gaussian stochastic bandit setting, the authors should compare the performance of the first suggested algorithm against a competitive, robust algorithm. Also, the authors should provide a detailed description of the adversarial attacks used in the experiments. Also, the authors should address the following issues in Figures 1 and 2:
   - are the data in the left and right plots of Figure 1 indeed distinct?
   - why the expected regret of TS is nearly identical to UCB?
   - clarification on the expected regret’s decrease as the adversarial budget increases on Figure 3.
   - the authors should explain the level of confidence for the plotted intervals. 
   - finally, the authors should provide commented code with a description of the different files and functions and a readme.txt file so that a reviewer can reproduce the experiments quickly. 
- A fifth suggestion would be for the authors to avoid using generative tools to write articles. It is frustrating for a reviewer to question whether they have spent more time writing a review than the author to write their paper.

### Soundness
2

### Presentation
1

### Contribution
2
