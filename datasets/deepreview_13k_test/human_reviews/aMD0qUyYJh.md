# Reinforcement Learning with Segment Feedback

- Decision: Reject
- Scores: 6, 6, 6

## Abstract
Classic reinforcement learning (RL) assumes that an agent can observe a reward for each state-action pair. However, in practical applications, it is often difficult and costly to collect a reward for each state-action pair. While there have been several works considering RL with trajectory feedback, it is unclear if trajectory feedback is inefficient for learning when trajectories are long. In this work, we propose a model named RL with segment feedback, which offers a general paradigm filling the gap between per-state-action feedback and trajectory feedback seemlessly. In this model, we consider an episodic Markov decision process (MDP), where each episode is equally divided into $m$ segments, and the agent observes reward feedback only at the end of each segment. Under this model, we study two popular feedback settings: binary feedback and sum feedback, where the agent observes a binary outcome and a reward sum according to the underlying reward function, respectively. To investigate the impacts of the number of segments $m$ on learning performance, we design efficient algorithms and establish regret upper and lower bounds for both feedback settings. Our theoretical and empirical results show that: under binary feedback, increasing the number of segments $m$ decreases the regret at an exponential rate; in contrast, surprisingly under sum feedback, increasing $m$ does not reduce the regret significantly.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies RL with segment feedback. In this setting, the episodes $H$ are assumed to be equally divided into $m$ segments. The agent observes reward feedback only at the end of each segment, instead of observing feedback for every action. The authors design efficient algorithms that establish regret upper and lower bounds for both binary reward feedback and sum reward feedback settings. Furthermore, the authors provide empirical results to show the advantage of their algorithms.

### Strengths
1. The paper is well written and the theoretical results appear to be correct.
2. The paper generalizes and improves previous results in (Efroni et al., 2021).
3. The paper provides empirical simulation results to show the advantages of their algorithms.

### Weaknesses
1. The regret bound provided in this article is unclear. For example, in Theorem 1, the authors represent many terms that are polynomially dependent on $S, A, H$ using $v(K)$, making the regret bound appear more optimal. The authors should clarify the order of their regret in terms of $A,A,H$.
2. The assumption of equal segmentation is a bit too strong. In practice, the aggregated reward feedback is rarely uniform. In such cases, an algorithm that can adapt to the level of aggregation would make more sense.

### Questions
1. See weakness.
2. What happens if $ r_{\text{max}}$is greater than 1? Intuitively, $ r_{\text{max}} $ can take any value, since at most the regret is scaled by $ \exp(r_{\text{max}} \cdot H / m) $.
3. What is the main difference between the two types of reward feedback. Intuitively, logistic feedback compresses the reward information into the $[0, 1 ]$ range. As a result, the regret for logistic feedback should be $\exp(m \cdot r_{\text{max}} / H)$ times larger than that for sum regret (as stated in a similar result in Theorem 2 of the paper). I'm curious why we can't directly apply the sum reward algorithm to the logistic reward case (just repeat playing every policy $\exp(m \cdot r_{\text{max}} / H)$ times to ensure that we can get enough information).

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
This paper studies the problem of RL with segment feedback in the contexts of binary feedback and sum feedback. In these settings, each episode is divided into m equal-length segments, and the agent receives feedback at the end of each segment. For the binary feedback setting, the authors propose TS-style algorithms, while for the sum feedback setting, they design UCB-style algorithms, and they provide analyses of the regret upper bounds, regret lower bounds for known transitions, and regret upper bounds for unknown transitions. Their findings show that, under binary feedback, increasing the number of segments m decreases the regret at an exponential rate, while under sum feedback, increasing m does not significantly reduce the regret.

### Strengths
1. The paper provides detailed theoretical analysis and proofs.
2. The E-optimal experimental design for sum feedback is very effective and interesting.
3. The conclusion that under sum feedback, increasing m does not significantly reduce the regret is intriguing, and the experimental results support this finding.

### Weaknesses
1. In terms of the setting, previous work has also proposed the segment feedback setting [1], although under a different name.
2. The assumption that each episode is divided into m segments of equal length is somewhat strong.
3. In the binary segment feedback setting (using a TS-based algorithm), the method for estimating the reward function is the same as in [2] (UCBVI with trajectory labels). Apart from replacing the UCB-based algorithm with a TS-based algorithm, what is the innovation in this algorithm? Additionally, the regret upper bound of the proposed algorithm SegBiTS appears worse than that of UCBVI with trajectory labels in a fair comparison when m=1. Given this, what are the specific advantages of using SegBiTS? 
4. It is straightforward to extend trajectory feedback algorithms to the segment feedback setting. If the proposed algorithm has advantages, they should be clearly stated, and a experimental comparison with trajectory feedback algorithms [2,3] should also be included.

[1] Reinforcement Learning from Bagged Reward.  
[2] On the Theory of Reinforcement Learning with Once-per-Episode Feedback.  
[3] Reinforcement Learning with Trajectory Feedback.

### Questions
1. Why was the regret lower bound not analyzed in the case of unknown transitions?
2. Why was a Thompson Sampling-type algorithm chosen for binary segment feedback, while a UCB-type algorithm was used for sum segment feedback?

I will review your response and am open to further discussion.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Classic RL assumes agents receive rewards for every state-action pair, but real-world applications make this costly and difficult. Previous work using trajectory feedback raises efficiency questions, especially with long trajectories. This paper introduces *RL with segment feedback*, a balanced approach between detailed and trajectory feedback. In this model, each episode in an MDP is divided into $m$ segments, with reward feedback provided only at segment ends. We explore two feedback types: binary (binary outcomes) and sum (cumulative rewards). By examining the effect of segment count $m$ on learning, we design algorithms with regret bounds for both feedback types. Our findings show that regret decreases exponentially with more segments under binary feedback, while sum feedback is less affected by increasing $m$.

### Strengths
- Addressing the segment feedback problem appears realistic and valuable, especially in applications like autonomous driving or large language models (LLMs). The reviewer finds the real-world examples presented on lines 58–62 particularly convincing.

### Weaknesses
Thanks for the paper and your efforts, please check the questions.

### Questions
- On line 215, further explanation is needed on how $\nu(k)$ represents the confidence radius of the MLE estimate.
- On line 230, does $m=1$ represent the optimal case for Theorem 1 (minimizing the upper bound of Theorem 1)? If so, what is the purpose of using segments $(m \neq 1)$?
- On line 231, could you clarify why the regret depends on the inverse of the sigmoid function's derivative?
- On line 284, in Theorem 4, what is meant by "ignoring logarithmic factors"? Additionally, isn’t the upper bound a function of $\log(\frac{1}{m})$ that decreases as $m$ increases? Are you suggesting that $m$ is not a critical factor in determining the upper bound?

### Soundness
3

### Presentation
3

### Contribution
3
