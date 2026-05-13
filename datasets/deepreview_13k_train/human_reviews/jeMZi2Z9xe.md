# Follow-the-Perturbed-Leader for Adversarial Bandits: Heavy Tails, Robustness, and Privacy

- Decision: Accept
- Scores: 6, 5, 8, 8

## Abstract
We study adversarial bandit problems with potentially heavy-tailed losses. Unlike standard settings with non-negative and bounded losses, managing negative and unbounded losses introduces a unique challenge in controlling the ``stability'' of the algorithm and hence the regret. To tackle this challenge, we propose a Follow-the-Perturbed-Leader (FTPL) based learning algorithm. Notably, our method achieves (nearly) optimal worst-case regret, eliminating the need for an undesired assumption inherent in the Follow-the-Regularized-Leader (FTRL) based approach. Thanks to this distinctive advantage, our algorithmic framework finds novel applications in two important scenarios with unbounded heavy-tailed losses. For adversarial bandits with heavy-tailed losses and Huber contamination, which we call the robust setting, our algorithm is the first to match the lower bound (up to a $\polylog(K)$ factor, where $K$ is the number of actions). In the private setting, where true losses are in a bounded range (e.g., $[0,1]$) but with additional Local Differential Privacy (LDP) guarantees, our algorithm achieves an improvement of a $\polylog(T)$ factor in the regret bound compared to the best-known results, where $T$ is the total number of rounds. Furthermore, when compared to state-of-the-art FTRL-based algorithms, our FTPL-based algorithm has a more streamlined design. It eliminates the need for additional explicit exploration and solely maintains the absolute value of loss estimates below a predetermined threshold.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a FTPL-based algorithm for adversrial bandits with heavy-tailed losses. The proposed method achieves near-optimal regret and improves the regret of two applications: heavy-tailed adversarial badnits with huber contamization and adversarial bandits with bounded losses and LDP.

### Strengths
1. The paper is well-written and mostly clear.
2. The proposed method achieves near-optimal regret bound.

### Weaknesses
1. Notice that the FTRL algorithm is best-of-both-worlds (see Huang et al. 2022). Does the proposed algorithm can achieve optimal regret in the stochastic setting?
2. The "applications" in this paper are also bandit models. It would be better if the paper includes some empirical analysis of real world applications.

### Questions
Is it possible to design a near-optimal algorithm for bandits with heavy-tailed loss if we don't know the heavy-tail parameters $\sigma$ and $\alpha$?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies adversarial bandit problems with potentially heavy-tailed losses.
The authors propose a Follow-the-Perturbed-Leader (FTPL) based learning algorithm that achieves (nearly) optimal worst-case regret.
The authors further show that their algorithm works for adversarial bandits with heavy-tailed losses and Huber contamination and adversarial bandits in the private setting.

### Strengths
- The authors consider FTPL based alg. instead of FTRL based alg., which improves current results by $poly(\log T)$. Especially, the results of adversarial bandits with heavy-tailed losses and Huber contamination and adversarial bandits in the private setting are new and better than prior works.
- The paper is well writen. The proof in the appendix is well organized and mainly correct.

### Weaknesses
 - Contrary to the author's statement, it is really trivial to use FTRL based algorithm to achieves (nearly) optimal worst-case regret for adversarial bandit problems with potentially heavy-tailed losses.
  First, using the similar skipping method as in the paper, the unbounded adversarial bandit problem can be reduced to the bounded case (the losses are bouned by $[-r,r]$, where $r = \sigma T^{1/\alpha} K^{-1/\alpha}$). 
  Then, using the algorithm in [wei2018more] and scale the losses by $1/r$, by Theorem 4 in [wei2018more], we can immediately get regret upper bound $\mathcal{O}(K\ln T/\eta +\eta Q_{T, i*} + Kr (\ln T)^2 )$, where $Q_{T,i^*} = \sum_t (\ell_{t, i^*}-\sum_t \ell_{t, i^*}/T)^2\le \sum_t \ell_{t, i^*}^2$. Since here $|\ell_{t, i^*}|$ is upper bounded by $r$ due to the skippping, there is $\mathbb{E}[\sum_t \ell_{t, i^*}^2]\le \mathbb{E}[\sum_t |\ell_{t, i^*}|^{\alpha} r^{2-\alpha}] \le T \sigma^\alpha r^{2-\alpha} = \sigma^2 T^{2/\alpha} K^{1-2/\alpha} $. 
  Thus, taking a suitable $\eta$ to balance the first and second terms results in regret $\mathcal{O}(\sigma T^{1/\alpha} K^{1-1/\alpha}(\ln T)^2 )$, which matches the results of this paper (up to log terms). (I guess such method can also get the regret guarantee Lemma 7 for adversarial bandits with huber contamination as in the paper)
- The design of GR count/GR maximum is confusing. According to the proof given by the authors, it is suffices to use the important weighting estimator (just set M_t = 1/w_{t, i}). In this case, GrErr goes to $0$ and FTPLReg can also be well bounded (proof of Lemma 5 still works). The authors do not clearly explain why it is important to use Geometric Resampling in their algorithm. The standard importance weighting estimator, when used with FTPL, would require knowledge of the weights $w_t$ which are determined by the perturbation and are not directly accessible. This is a critical point that is not addressed by the authors. The authors should clarify why the standard importance weighting estimator cannot be directly used in their FTPL framework, and why Geometric Resampling is necessary to construct the loss estimates.

### Questions
- Why we need to use Geometric Resampling in the algorithm? Is it just for the proof of DP case?
- Is there any high level intuition why there exists poly(log K) in the regret? Is it possible to remove such terms?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors consider the adversarial bandit problems with heavy-tailed and possibly non-negative, bounded losses. The authors then point out the limitations of previously known work in this setting. The authors propose a novel FTPL solution scheme to tackle these challenges. This solution avoids the need for extra assumptions required by the state-of-the-art FTRL algorithm. Finally, the authors demonstrate the performance of the proposed algorithm by studying two examples: adversarial bandits with heavy-tailed losses and Huber contamination and  adversarial bandit with bounded loss  and additional Local Differential Privacy.

### Strengths
- The paper is very well-written and it is fairly easy to follow. The main idea is quite straightforward and the way it is presented (in comparison with previously known work) is very clear. 

- The sketch of proof helps understanding the insights of the results and highlight the contributions (unfortunately, I did not have time to check the detailed proof in Appendix, but from the sketch, it seems sound enough). 

- The two example applications are also well presented.

### Weaknesses
 - A minor weakness is that the "breakthrough" comes from a known property (FTPL with Laplace perturbation) and its combination with Skipping (yet again, a previously known scheme) is rather obvious from the way it is currently presented. Personally, I believe that the authors do a good job in making such observations and tuning the algorithm's parameters (notably, L_t) which is often not that obvious. It might be better if the authors highlight a bit more on this aspect. 
- The questions posed by the paper is interesting in a theoretical point of view. However, it might be better to provide some motivational/practical examples where it is essential to model the problem with negative, heavy-tailed losses like this instead of simply changing the loss models to fit more traditional non-negative loss framework.  The authors might argue that the Huber-contamination serves this purpose but Lemma 7 is valuable only if beta is significantly small, which undermines this argument. 
- The proposed algorithm still requires knowledge of coefficients of Assumption 1 to deterministically tune the step-size, the skipping threshold and the L_t parameter. I am not sure how realistic this requirement can be.  As usual in bandit, it might be possible to relax this by using bounds of the involved coefficients instead of the true values. Do you think the results still hold?
- Another minor weakness of the algorithm is that the While-Loop that runs (in worst-case) with L_t rounds (that need be sufficiently large as pointed out) at each step. Is there possible to look for a better sampling scheme to check simultaneously many perturbed leaders at the same time? 
- Despite being a theoretical paper, some simple experiments can help to clear further the comparison with SOTA (see questions below).

### Questions
- While I agree with Remark 10, Assumption 2 is purely for technical purpose (of the proof) and does not really hinder one to run the FTRL algorithm of Huang et al.2002 in your setting (even though their regret-bound is not guaranteed). It might be worth to run experiments to compare it with the proposed FTPL. 

- Corollary 1 states the results specifically with the (epsilon-DP) mechanism. Does this mean it is not applicable to some situations where the privacy is not Laplace (but still guaranteeing heavy-tailed losses) ?

- Do you think it is possible to design a dynamic/adaptive skipping threshold r?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This submission studies the adversarial K-armed bandit problem with heavy-tailed losses. Before the game begins, an oblivious adversary selects a sequence of $T$ heavy-tailed loss distributions for each arm, after which the learner pulls a sequence of $T$ arms, and only observes the loss realizations for the arms they decided to pull. The authors' main result is to show that a modified version of Follow-the-Perturbed-Leader (FPTL) achieves optimal regret with respect to the best arm in hindsight, up to logarithmic-in-K factors. At a high level, FTPL adds a random perturbation to the sequence of observed losses at each time-step, before taking the action which minimizes the sequence of perturbed losses. The authors’ algorithm (Algorithm 1) proceeds similarly, with the key difference being that they ’skip’ losses (i.e. do not factor them into future calculations) if they are larger than a given cutoff threshold. In addition to achieving near-optimal performance in the adversarial setting with unbounded losses, the authors apply their algorithm to two different settings: adversarial bandits with Huber contamination and local differential privacy. In the Huber contamination setting, the loss observed by the learner is not the true loss, but is instead generated from some arbitrary and unknown distribution. Under this setting, the authors show that their algorithm achieves optimal regret (up to logarithmic factors). Under differential privacy, the authors’ algorithm improves upon existing results by polylogarithmic factors.

### Strengths
The authors show that a slight modification of a well-known and popular algorithm (FTPL) achieves near-optimal performance in the adversarial multi-armed bandit setting with heavy-tailed losses. Their algorithm is applicable in a wider range of settings when compared to previous, Follow-the-Regularized-Leader (FTRL)-based algorithms.  (See Assumption 2 and the following discussion for more details.) Additionally, the two applications are interesting, and the authors’ retults in these settings are either near-optimal or state-of-the-art. Finally, the writing of the paper is overall a strength. While I had one question in particular (see below), I found that the authors did a good job of succinctly describing (1) their algorithm (2) the challenges of the setting they consider, (3) the salient parts of their analysis, and (4) their applications.

### Weaknesses
It would be good to give some intuition behind why the algorithm ’skips’ losses. Specifically, it is not clear why simply ignoring large losses is a good strategy. For instance, if the losses are heavy-tailed, large losses are not necessarily outliers, and could be informative about the underlying loss distribution. It would be helpful if the authors could provide more insight into why this approach is effective, and under what conditions it might fail. 

Claiming Lemma 1 as a key observation seems to be an overstatement of the authors’ results, as Lemma 1 appears in previous work. It would be good if the authors could clarify what exactly is their observation when compared to previous work. It is not clear what the authors mean by 'leveraged' in this context, and how this leveraging is different from previous work that also uses this lemma.

### Questions
Can you results be extended to settings in which the loss distributions are generated  by an adaptive adversary?

Is the skipping of large losses necessary? Or could a more clever analysis remove the need for this step in the algorithm?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
