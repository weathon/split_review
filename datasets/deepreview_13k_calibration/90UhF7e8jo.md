# Goal Achievement Guided Exploration: Mitigating Premature Convergence in Reinforcement Learning

- Decision: Reject
- Avg Score: 5.50
- Scores: 3, 8, 6, 5

## Abstract
Premature convergence to suboptimal policies remains a significant challenge in reinforcement learning (RL), particularly in tasks with sparse rewards or non-convex reward landscapes. Existing work usually utilizes reward shaping, such as curiosity-based internal rewards, to encourage exploring promising spaces. However, this may inadvertently introduce new local optima and impair the optimization for the actual target reward. To address this issue, we propose Goal Achievement Guided Exploration (GAGE), a novel approach that incorporates an agent's goal achievement as a dynamic criterion for balancing exploration and exploitation. GAGE adaptively adjusts the exploitation level based on the agent's current performance relative to an estimated optimal performance, thereby mitigating premature convergence. Extensive evaluations demonstrate that GAGE substantially improves learning outcomes across various challenging tasks by adapting convergence based on task success. Applicable to both continuous and discrete tasks, GAGE seamlessly integrates into existing RL frameworks, highlighting its potential as a versatile tool for enhancing exploration strategies in RL.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper proposes an approach called Goal Achievement Guided Exploration (GAGE) to address premature convergence in reinforcement learning algorithms. Instead of using intrinsic rewards for exploration, the proposed approach maintains an estimate for the optimal performance level, comparing this level to the current performance for controlling between exploration and exploitation.

The main claim of the paper is that the proposed approach enhances exploration in reinforcement learning.

### Strengths
The proposed approach aims to balance between exploration and exploitation in reinforcement learning. The approach is interesting in that it assumes that each reward term is equally important and exploration magnitude is kept as high as how far each reward term is from an assumed optimal solution.

In more detail, the approach uses a goal achievement term that is the minimum of goal achievement terms of each reward part. Each of these individual goal achievement terms is computed using Monte Carlo estimates of recent samples divided by a heuristic estimate of the optimal value, or, total maximum reward. An implicit assumption is that an agent should be able to succeed in all parts of the reward function sum.

Discussion of the "Game Console" problem in exploration is valuable.

### Weaknesses
The approach is based on assuming explicit knowledge of the reward function and  the individual parts (terms) that as a sum define the reward function. This needs to be discussed and motivated in detail. Most of the exploration approaches in reinforcement learning do not need explicit knowledge of the reward function.

The approach makes strong assumptions about the task. I assume the approach only works if these assumptions are satisfied and can easily lead to slow convergence. The approach controls exploration according to the reward term that is furthest away from being satisfied. This means, for example, that if there is a single reward term that is very hard to get close to optimal, large amounts of exploration is used although the total reward would be already high. Moreover, the approach can lead to excessive exploration noise that may hinder improving reward terms which require small amount of noise.

Evidence for the main claim of the paper that the proposed approach enhances exploration is needed. That the algorithmic design and computations used in the approach improve on state-of-the-art need significantly stronger theoretical or/and empirical evidence.

Fig. 2 and the main text aim to motivate the proposed approach by saying that exploration methods typically somehow change the order of probabilities. This is not true. For example, target entropy [Haarnoja et al., 2018] is commonly used and does not change the order of the action probabilities. The claim that entropy maximization can arbitrarily reorder action probabilities is not accurate. Maximizing the Shannon entropy of a discrete distribution pushes the probabilities towards a uniform distribution, it does not change the order of probabilities. The entropy bonus is a concave function, and when combined with a reward term, it does not cause the probability of the least promising action to become the highest. The optimization process will not reorder the probabilities in such a way that it elevates the least promising action to the highest probability.

The action smoothing procedure in Section 3.2 for discrete actions includes several computations for which there is some discussion of the motivation but no theoretical or empirical evidence. There should be a much more convincing discussion on why each of the steps 1. to 4. in Section 3.2 is used to compute the adaptive temperature of the softmax distribution.

Experiments:

Methods:
One of the main motivations for the proposed approach in the paper is that intrinsic motivation based approaches may converge to local optima. However, there are methods designed specifically to address this problem. For example, [Chen et al., 2022], explicitly optimizes the original optimization objective while taking advantage of intrinsic motivation. These kind of methods need to be added as baselines.

Typical exploration methods need to be added as baselines. This includes pre-defined entropy schedules: linearly descreasing entropy, constant entropy, constant + linearly decreasing etc.

Benchmarks:
In the continuous action setting, the proposed new benchmarks are valuable. However, to provide readers sufficient information also well known benchmarks should be used where existing baseline results are available. Examples of continuous action benchmarks which require exploration such as AntMaze etc. can be found for example in the hierarchical reinforcement learning literature (see [Nachum et al., 2018] and follow the citations to the newest work with the largest environments).

The "Game Console" problem in exploration is valuable and interesting but what is the relationship of the proposed approach compared to other methods that do not use intrinsic rewards? In "Game Console" type of problems, mostly intrinsic rewards cause problems?


Details:

Please explain "More severely, for discrete actions, the entropy loss can not maintain the distribution shape, i.e., the order of actions’ probabilities of the learned policy." in more detail.

Regarding control of policy variance in Equation 4, it seems that identical variances for all action dimensions is assumed?

In Fig. 2, please define what entropy maximization means. For a discrete distribution, maximum entropy results in a uniform distribution which differs from Fig. 2b.

The presentation is overall OK but there are typos such as  "probablities" that should be fixed.

### Questions
I recommend rejecting the paper. The authors can improve the paper by improving the motivation for the approach, discussing in more detail in which situations the approach works and does not work, providing proper experimental baselines and benchmarks.

### Soundness
1

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents Goal Achievement Guided Exploration (GAGE), an algorithm to prevent premature convergence and encourage exploration in deep RL. The paper describes the major causes of premature convergence in RL and describes an algorithm to address specific types of issues, which is then evaluated in several different task domains.

### Strengths
This paper is well written, and does an excellent job of contextualizing and motivating work on premature convergence, and intuitively develops and explains the GAGE algorithm, which is simple yet not trivial. This issue is an important one that is common in practice, but has received little attention from prior work, and thus a worthwhile topic of study. The GAGE algorithm requires several well-stated priors to work, most notably a human estimate of what the maximum achievable reward is for each reward term, but in my option this is a reasonable prior for many RL domains and not overly restrictive. The experimental validation of the algorithm is reasonably thorough.

### Weaknesses
I didn't have any major issues with this paper, though there's a few issues I've noted in the questions section which could be improved.

The biggest concern I have is that the benefits of doing any form of action smoothing to prevent premature convergence versus the specific algorithm of GAGE are not clear- it could be the case that a simpler baseline would be just as good (though I suspect this is not the case). However, this paper does not claim to be definitive regarding premature convergence prevention or action smoothing algorithms (and it doesn't need to be to provide a meaningful contribution), so I don't find this to be a critical flaw.

While not the final word on the problem (if such a thing is even possible), this work seems like a worthwhile step forward, with real implications for deep RL in practical and scientific use. I could see GAGE or a similar algorithm plugging in nicely as a standard tool to improve performance and stability alongside other methods. As such, I am inclined to recommend acceptance- this is good work.

### Questions
Some minor issues and questions:

-What do the upper and lower brackets in equation 7 denote? I don't see this explained in the text and it is unusual notation in my experience of the field.

-The temperature computation for smoothing action probabilities is somewhat complex compared to simpler alternatives mentioned (e.g. mixing with uniform). I don't see any ablations testing whether this more sophisticated smoothing is better than the naive baseline, however, which be useful to see.

-The lines in figure 3 are a bit too small to comfortably read, please make them bigger (plot size is fine, the lines are too narrow).

-The captioning and plot spacing in figure 4 is a little confusing, the right two plots should be closer together to show that they are a pair, unlike the left plot.

-Section 4.2's writing takes a sudden nosedive- there's a number of instances of odd phrasing and wrong grammar here in what is otherwise an excellently written paper. This could use a pass to revise.

-For figure 5, what is the baseline performance for each method on the non-game-containing version of this task? I assume all algorithms can learn the task successfully? It would be good to make this clear if it is so as it strengthens the point being made.

-I would have liked to see more aggressive stress tests on the reward upper bound estimate where performance is lost as a result of a bad estimate. What happens if V_star in figure 4a is set to 1? What if it is set to 99? I imagine these won't perform well, but it would be useful to know what happens when things break down since sometimes human estimates of the maximum possible reward will be quite wrong.

### Soundness
4

### Presentation
4

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
This paper proposes to use goal achievement as a learning progress measure to schedule the noise for exploration, where goal achievement is defined as the ratio of the current policy's expected return to the optimal policy's expected return. The results showed that goal achievement improves PPO's performance in robotic tasks with intensive reward shaping and hard-exploration tasks in MiniGrid.

### Strengths
This method is very easy to implement and seems to improve the performance greatly. The authors claim that current methods suffer from premature convergence. Thus, they propose to tune the noise of exploration adaptively using a goal achievement rate, with the assumption that the maximum reward is known.

### Weaknesses
 - Lack of theoretical discussion. This is fine since I understand this paper's contribution is a practical algorithm. Still, it would be great to see why adjusting the noise level with goal achievement leads to improvement.
- Writing is a bit verbose. Section 2 is mostly about previous works. The proposed method doesn't come until page 4, which is too long in my opinion.

### Questions
- Figure 3's legends are too small to read.
- Where are the differences between GAGE-50 and GAGE-100?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes an exploration approach in reinforcement learning aimed at mitigating the premature convergence issue. The proposed Goal Achievement Guided Exploration (GAGE) measures the ratio of currently achieved cumulative rewards over the expected maximum cumulative rewards as a criterion. If the agent has not reached an expected level of performance, it is encouraged to continue exploring.

### Strengths
The GAGE algorithm is straightforward and easy to understand. The core idea is to set an expected "goal" and have the agent keep exploring (rather than converging) until the set goal is reached. The presentation is smooth, and the paper provides a comprehensive review of related works. The targeted issue of premature convergence is clearly stated and effectively addressed. The paper discusses both continuous and discrete action spaces and proposes appropriate solutions for each.

### Weaknesses
1. The "goal achievement" is defined as the ratio of achieved cumulative rewards for the current policy over the maximum or optimal cumulative rewards. Since the optimal policy is unknown, the paper proposes setting a hyperparameter as a threshold. However, this introduces two limitations:

(1) The goal-setting determines the upper bound of learning performance, or at least, heavily influence the learning process. If the goal is set too high, the algorithm may struggle to converge as the agent will always perceive its performance as insufficient. Conversely, if the goal is set too low, the agent will reach it too easily, which may still lead to premature convergence.

(2) In this case, the expected "goal" is highly task-specific, requiring prior knowledge to define an appropriate threshold for different tasks.

2. The paper identifies four main factors contributing to premature convergence (discussed in Section 2.1). However, the five continuous control tasks used in the experiments do not seem to reflect these factors well. The motivation for selecting these tasks, and how they are capable of demonstrating the effectiveness of the GAGE algorithm in addressing premature convergence, should be more clearly explained.

3. In the experiments, the five continuous control tasks only compare GAGE with the backbone PPO algorithm. I believe comparisons with some benchmarks are necessary to fully demonstrate the advantages of GAGE. Specifically, given that GAGE is designed to enhance exploration, comparisons with established exploration techniques such as curiosity-driven exploration, novelty-based exploration, or methods using intrinsic rewards would be highly beneficial.

### Questions
1. In Section 4.1 (around Line 400), the experiments show that "When the target speed is set to 5m/s, which is below the learned optimal speed (~7m/s), the GAGE agent is still able to learn the optimal speed." Referring to Equations (2) and (4), if the learned policy achieves higher rewards than the expected target, the "goal achievement" $g(\pi) >1$, which means the lower bound $\sigma_L(\pi) = -\sigma_0 g(\pi) + \sigma_0 < 0$. Additionally, if the learned policy has already achieved the target goal of 5m/s, it would focus mainly on convergence and less on exploration, how is it able to continue optimizing to reach 7m/s?

2. What happens if the target goal is set too high? Will this result in the agent lacking confidence and failing to converge?

3. While GAGE is designed to avoid local optima, in Figure 3, we can observe that some GAGE variants still become trapped in local optima. For instance, in *Ant Acrobatics*, both GAGE-75 and GAGE-100; in *Humanoid Pole*, GAGE-100; and in *Humanoid Tightrope*, both GAGE-50 and GAGE-100 converge to relatively low episodic returns. Does this indicate that the local optima issue is not fully addressed?

I would like to increase the score if these concerns are addressed.

### Soundness
3

### Presentation
3

### Contribution
2
