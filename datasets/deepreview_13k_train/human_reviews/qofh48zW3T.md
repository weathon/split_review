# Distributional Distance Classifiers for Goal-Conditioned Reinforcement Learning

- Decision: Reject
- Scores: 6, 8, 5, 3, 8

## Abstract
What does it mean to find the shortest path in stochastic environments if every strategy has a non-zero probability of failing? At the core of this question is a conflict between two seemingly-natural notions of planning: maximizing the probability of reaching a goal state and minimizing the expected number of steps to reach that goal state. Reinforcement learning (RL) methods based on minimizing the steps to a goal make an implicit assumption: that the goal is always reached within some finite horizon. This assumption is violated in practical settings and can lead to suboptimal strategies. In this paper, we bridge the gap between these two notions of planning by estimating the probability of reaching the goal at different future timesteps. This is not the same as estimating the distance to the goal -- rather, probabilities convey uncertainty in ever reaching the goal at all. We then propose a practical RL algorithm, Distributional NCE, for estimating these probabilities. Taken together, our results provide a way of thinking about probabilities and distances in stochastic settings, along with a practical and effective algorithm for goal-conditioned RL.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper argues that optimizing for steps to a particular goal is not a feasible objective for most reinforcement learning problems. This work demonstrates the shortcomings of distance to goal metrics in toy Markov processes as well as experiments in larger state spaces. They then present an algorithm (Distributional NCE) that uses a probabilistic model of arriving at a goal in a given number of timesteps.

### Strengths
* Experimental questions and hypotheses were succinctly laid out and all appropriately addressed. The results adequately evidence the claims of 1) delivering a practical RL algorithm, 2) giving a probabilistic way of thinking about the probabilities and distances in a stochastic setting. This is achieved with a good mix of small and large problems.
* The work builds on relevant previous works while also explicitly stating its limitations.

### Weaknesses
 **Technical Comments/Issues**
* The definition of Monte Carlo “distance” should be made clearer. The intuition is conveyed well, but since this concept is used for several examples in section 4.1 as well as in the experimental results, it would be useful to have some more mathematical grounding. Formally defining the state and state-action variant would be helpful to the reader. Something along the lines of:

i) d(s,g) = \mathbb{E}[\Delta | s_0=s, s_\Delta=g], where \Delta indicates the length of the trajectory and,

ii) d(s,g,a) = \mathbb{E}[\Delta | s_0=s, a_0 = a, s_\Delta=g]. This would also make the counter-example showing how this “distance” violates the triangle inequality more apparent. While the authors now provide a definition for d(s,g), the definition of d(s,g,a) is still missing, and the counter-example is still not fully explained in the context of the provided definition. The authors should also clarify if the expectation is taken with respect to the policy or some other distribution.
* The temporal consistency objective does not make sense in certain reinforcement learning problems. Some goals can have a minimum number of steps needed before they can be reached. For example, in a gridworld where the shortest path to the goal is 10 steps away, P(reaching the goal in 9 steps) = 0, whereas P(reaching in 10) can be high for a good policy. It would be useful to address this aspect of temporal consistency or even highlight it in an experiment with such temporal constraints, or remove it as it does not naturally stem from the main hypothesis of the paper. While the authors have addressed this point, it would be useful to see an experiment where this is explicitly shown, as the current experiments do not highlight this issue.
* Proposition 2 and 3 can be merged together. Proposition 2 is repeated in proposition 3, and the example showing how d(s,g) is not a quasi-metric can be explained alongside the example from V*
* While this work does acknowledge Contrastive NCE from the literature, the acronym is not explicitly spelled out anywhere. This would be useful to specify.

**Minor Comments/Issues**
* It would be useful to specify the number of runs that were averaged over in the learning curves of Figures 3, 4, and those in the appendix. The work should also mention what the shaded area around each curve represents and how they curves were smoothed, if any such technique was applied. While the authors have addressed this point, it would be useful to include this information in the main body of the paper, as opposed to just referencing the appendix.
* In section 4.3, P^{\pi_g} was not defined. It would be useful to clarify it or remove it from the equation (as it only appears once in the main body).
* On page 11, Yecheng et al. 2022 was included twice in the references.

### Questions
* On Page 7, in the paragraph beginning “Comparison with distance regression.” it is claimed that “ We hypothesize that the stochasticity in action sampling from the policy, along with the associated risk of choosing the shortest path are ignored by MC distance functions [...]”. It is apparent that since the distance conditions itself on reaching the goal the risk of the shortest path is ignored, but the MC distance function is an average number of timesteps elapsed between a state and the goal state. Doesn’t it already account for the stochasticity in action selection?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper constructs an example to illustrate that two criteria in goal-conditioned RL are not equivalent. It also uses Proposition 2 and 3 to show that Monte-Carlo distance is not a good criterion. It also designs an algorithm to train the agent w.r.t to latter criteria.

### Strengths
1. The observation that two criteria are not equivalent is interesting.

2. Section 4.1 justifies the use of probability instead of distance.

### Weaknesses
A lot of research in goal-conditioned RL uses probability as criterion. The paper should include a comparison to compare the algorithm ion the paper and previous algorithm.

### Questions
See 'Weakness' section.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Goal Conditioned Reinforcement Learning requires the agent to reach the goal state a minimum number of timesteps. A number of methods estimate the distances between two states and use this estimate to select the optimal action. However, the authors show why such a measurement is incorrect. They build upon prior methods for estimating future state visitation densities and come up with an algorithm that estimates the probability of reaching the goal in future t steps. Using the probability of the goal being reachable in H steps, they update their policy.

### Strengths
(1) They correctly highlight the shortcomings of the MC distance regression methods.

(2) They draw interesting insight into the relationship between maximum likelihood and stochastic shortest path.

(3) Their algorithm improves over the previous baseline Contrastive NCE on competitive domains.

### Weaknesses
(1) A common belief in the paper is that the natural way of designing a goal-conditioned RL problem is by minimizing the hitting time i.e. having rewards = -1 for all states and 0 at the goal. I believe it is more common to consider reward = 0 everywhere else and 1 at the goal as defined by the original problem. Subtracting -1 from all rewards acts like shaping the reward function which might lead to suboptimality as already shown in several works.

(2) Another assumption is that the method of predicting the number of steps that elapse between one observation and another is common. A few works definitely explore this direction, but I think it is more common to simply use a shaping reward over the 0/1 reward function.

(3) In section 4.1, it is unclear in the toy examples when the episode ends. From the math it seems like the episodes end when the goal state is reached otherwise they continue indefinitely.

(4) It would be interesting to see how this method compares with shaping rewards.

### Questions
(1) Why do MC distance regression methods estimate the Q function? Why can't I use the estimated distance as a reward? Using them as rewards is still valid even when they are not quasimetric.

(2) In section 4.3, the estimated distance functions seem to be odd. Suppose, C(s, a, g)[H] = [0, 0, ...]. Will the estimated distance between s and g be 0? Also, if the classifer predicts normalized probabilities, then p(g|s, a2, H=1, 2, 3, ...) cannot be equal to [1, 1, 1, ...].

(3) The algorithm is not completely clear. What is dt in the algorithm box?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors of this work propose an algorithm, Distribution NCE, for efficient learning in Goal-Conditioned RL. The authors notice that Monte Carlo distance functions are problematic (as they are do not obey triangle inequality) and propose a remedy that estimates the probabilities of reaching the goal state. The authors then demonstrate the numerical performance of their remedy on seven standard goal conditional RL environment.

### Strengths
The empirical results of the paper appear to be good. The authors are able to demonstrate good performance with their Distributional NCE method. However, I am not familiar with empirical works.

### Weaknesses
I am not sure if propositions 1-3 are correct, the statements themselves are quite vague. The proofs, or lack thereof, are not convincing. For instance what is the argument being made in the proof of proposition 2? That MC distance are not valid distances because they do not satisfy triangle inequality ? How is this being shown for any metric? What is the distance function $d(s_1,s_2,a)$. Is the proof for proposition 1 referring to the mdp in figure 1a) ?

The main weakness of the paper lies in the formalism of the mathematical writing. As pointed out, certain mathematical expressions such as the Monte Carlo Distance Function are defined in words but not formally stated. This becomes an issue when writing proofs about these ill-defined terms. It might be better to just have a section illustrating the failure case of Monte Carlo Distance Functions as opposed to writing "propositions". If the authors want to write propositions then please spend some effort defining all the quantities to be used in the propositions.

In the second equation on page 3, why is the expectation on the left of the sum different than the one on the right ? Also for equation (1) it seems the expectations are taken wrt to difference distributions?

What is a Mount Carlo Distance Function? Does it depend on the policy being played? Is there any expectations or does it just take in raw observations? 

Why is Monte-Carlo distance estimation equivalent in the limit to learning a normalized distance classifier ?

COMMENTS:

When writing out theorem blocks, such as propositions, please include a proof block as well. In section 4.1 the "propositions" (1-3) have no proofs? However, proposition 4 seems to have a proof. 

Appendix D.4 is empty.

### Questions
In the second equation on page 3, why is the expectation on the left of the sum different than the one on the right ? Also for equation (1) it seems the expectations are taken wrt to difference distributions?

What is a Mount Carlo Distance Function? Does it depend on the policy being played? Is there any expectations or does it just take in raw observations? 

Why is Monte-Carlo distance estimation equivalent in the limit to learning a normalized distance classifier ?

COMMENTS:

When writing out theorem blocks, such as propositions, please include a proof block as well. In section 4.1 the "propositions" (1-3) have no proofs? However, proposition 4 seems to have a proof. 

Appendix D.4 is empty.

### Soundness
2 fair

### Presentation
2 fair

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
This paper studies goal-conditioned reinforcement learning, and the authors propose a new method where they estimate the probability of reaching the goal at different time steps instead of just estimating the distance to the goal. Their final algorithm, distributional NCE, achieves promising empirical performance in several standard goal-conditioned environments.

### Strengths
Goal-conditioned RL is an important topic as it has many application scenarios. The idea proposed in this paper is quite natural and the author provide a good information theory argument on why their algorithm should work better (the learner receives logH bits information instead of 1 bits for each positive example). The resulting algorithm is simple, intuitive, and has promising empirical performance.

### Weaknesses
1. The writing is not very clear and require the reader to be familiar with previous work on goal-conditioned RL. For example, when introducing the objective of contrastive RL on page three, it is unclear what C(s, a, g) stands for.
2. I am not very convinced about the claim that "the number of bins does not affect the final performance".  In the extreme case, where H=1, it becomes a quantity similar to the expected distance measure and it should perform similar to estimating expected distance measure in my opinion. I would like to see how the algorithm behaves when H is very small, such as H=1 or 2.

### Questions
1. The problem formulation in this work is not exactly the stochastic shortest path problem as the discounting factor is < 1. Will the analysis still go through if the discounting factor is 1?
2. In related work, please also discuss the relationship between this work and the recent theoretical advancement in goal-conditioned RL, such as the followings:
(1) Jean Tarbouriech, Evrard Garcelon, Michal Valko, Matteo Pirotta, and Alessandro Lazaric. Noregret exploration in goal-oriented reinforcement learning. In International Conference on Machine Learning, pages 9428–9437. PMLR, 2020
(2) Alon Cohen, Haim Kaplan, Yishay Mansour, and Aviv Rosenberg. Near-optimal regret bounds for stochastic shortest path. In Proceedings of the 37th International Conference on Machine Learning, volume 119, pages 8210–8219. PMLR, 2020.
(3) Liyu Chen, Mehdi Jafarnia-Jahromi, Rahul Jain, and Haipeng Luo. Implicit finite-horizon approximation and efficient optimal algorithms for stochastic shortest path. Advances in Neural Information Processing Systems, 2021a.
3. The proposed method has the same spirit as distributional RL. I am wondering whether quantile regression can also be extended to solving goal-oriented RL?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
