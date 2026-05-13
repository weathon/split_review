# On Provable Benefits of Policy Learning from Human Preferences in Contextual Bandit Problems

- Decision: Reject
- Scores: 8, 3, 3

## Abstract
For a real-world decision-making problem, the reward function often needs to be engineered or learned. A popular approach is to utilize human feedback to learn a reward function for training. The most straightforward way to do so is to ask humans to provide ratings for state-action pairs on an absolute scale and take these ratings as reward samples directly. Another popular way is to ask humans to rank a small set of state-action pairs by preference and learn a reward function from these preference data. Recently, preference-based methods have demonstrated substantial success in empirical applications such as InstructGPT. In this work, we develop a theoretical comparison between these human feedback approaches in offline contextual bandits and show how human bias and uncertainty in feedback modelings can affect the theoretical guarantees of these approaches. Through this, our results seek to provide a theoretical explanation for the empirical successes of preference-based methods from a modeling perspective.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes the effect of bias in human feedback for contextual bandits in two settings: rating feedback (i.e. direct access to the reward function), and preference (comparison) feedback.

The effect of human biased is first quantified by proving sub-optimality bounds of two (previously existing) algorithms for contextual bandits with human feedback. The novelty in the presented bounds lie in the fact that feedback (rating or preference) is received through a bias transform.  It is later shown than for a certain class of bias transformations, solving a bandit problem with biased rating feedback, always requires more samples than solving the same problem with biased preference feedback. This is an interesting phenomena as works against the prior conception that solving a bandit/RL problem with preference feedback is more complex than with rating feedback.
At the same time, this statement is not entirely surprising, since the BTL preference feedback model is robust to the considered class of bias transformations.

### Strengths
My summary should reflect some strengths of the paper, I spell out a few more below.

* The paper is well written and straightforward.

* It tackles an important problem and gives a clear answer. In particular, Theorem 4, which is algorithm independent, has a really nice formulation.

* I am not aware of prior work on Bandits/RL with human rating to assess how novel Theorem 1 is compared to previous sub-optimality of the LCB algorithm (e.g. in terms of techniques used to derive it). However, Theorem 1 and 3 clearly characterize the effect of a transformed/biased rating feedback.

### Weaknesses
 * Given the assumptions on the bias transform $h$, I am not surprised that the preference-based feedback is rather invariant to such biases. So I am not sure if the final results are uncovering an informative phenomena. Specifically, the assumption that $h$ is monotonic and does not change the optimal policy seems to trivialize the problem. It is not clear how much the results would change with a non-monotonic $h$ that could potentially alter the optimal policy, which would be a more realistic scenario when dealing with human feedback.

* A number of prior works on contextual bandits with preference feedback is not mentioned. While the overall approach is sufficiently different (they optimize a least squared loss), I think they should be mentioned for completeness.
  - Mehta, Viraj, et al. "Kernelized Offline Contextual Dueling Bandits." arXiv preprint arXiv:2307.11288 (2023).
  - Dudík, Miroslav, et al. "Contextual dueling bandits." Conference on Learning Theory. PMLR, 2015.
  - Saha, Aadirupa, and Akshay Krishnamurthy. "Efficient and optimal algorithms for contextual dueling bandits under realizability." International Conference on Algorithmic Learning Theory. PMLR, 2022.
- Bengs, Viktor, Aadirupa Saha, and Eyke Hüllermeier. "Stochastic Contextual Dueling Bandits under Linear Stochastic Transitivity Models." International Conference on Machine Learning. PMLR, 2022.
- Perhaps also: Bengs, Viktor, et al. "Preference-based online learning with dueling bandits: A survey." The Journal of Machine Learning Research 22.1 (2021): 278-385.

### Questions
- How would you go beyond tabular setting? Would you say the pessimistic MLE algorithm can be easily extended to say, a kernelized or linear rewards over a compact domain?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the benefits of using preference for learning reward functions in contextual bandits. Through a theoretical analysis for offline contextual bandits, the paper examines how human biases and uncertainties affect these methods' theoretical guarantees. They provided a theoretical explanation for the empirical success of preference-based methods.

### Strengths
I found this paper easy to follow. All theoretical conditions and results are clearly stated, and sufficient remarks are followed. 

The way that they study the biased reward (through the definition of a transformation $h$) is interesting.

### Weaknesses
My biggest concern is that I found the logic of this paper a bit confusing. The authors first showed that LCB failed to achieve the desired statistical guarantee under the biased model (section 4). Then, they showed that pessimism MLE can achieve better statistical results under an unbiased model (section 5.1). This comparison is clearly unfair. Hence, the authors further studied learning preference from the biased model (section 5.2) and showed that the results are actually worse. They then remarked that

> This shows if one assumes a similar amount of human bias and uncertainty in both types of human feedback, the preference-based approach is no more sample-efficient. This actually contradicts with the empirical observations in the existing literature, which suggests preference-based methods have superior performance. Hence, our theory shows the bias-free modeling plays a great role in the lower sample complexity of preference-based methods, and our theoretical results can conversely confirm the standard BTL modeling of human preference feedback—it is reasonable to believe human preference data is indeed subject to less bias and uncertainty in practice.

My understanding is that, the authors are not trying to use *theory* to verify *empirical success* (which I was expecting), but rather, they use *empirical success* to prove the *theory*. Hence, it appears that this paper has undertaken a completely contrary endeavor. The authors seem to haven't truly shown any benefits of using preference from pure theory; on the contrary, the conclusions they have drawn are rather contradictory (Theorem 4). Their sole argument positing the superiority of preference relies on the fact that, in practice, it yields better experimental results, thereby suggesting that the preference is unlikely to be significantly biased. If it is really what the authors intended to convey, I don't think this result is a "provable" benefit but rather heuristic. This leaves me quite confused, and I hope the authors can clarify this point.


Some other issue: the lower bound results (theorem 1 & 2) only considered the LCB algorithm. It will be more convincing to establish a universal and information-theoretic lower bound, i.e., a lower bound that holds for any algorithm.

### Questions
Is the studied algorithm, pessimistic MLE, computationally efficient? If it is not, I don't think it is fair to compare it with the more efficient LCB algorithm. Actually this question circles back to the previous one: can the lower bound be applicable to any algorithm and not solely limited to LCB?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper develops a theoretical comparison between these human feedback approaches in offline contextual bandits and shows how human bias and uncertainty in feedback modeling can affect the theoretical guarantees of these approaches. The proposed results seek to provide a theoretical explanation for the empirical successes of preference-based methods from a modeling perspective.

### Strengths
1.	The studied problem, i.e., contextual bandits with human feedback, is very well-motivated and finds important applications such as large language models.
2.	The authors propose algorithms based on pessimism with suboptimality guarantees.

### Weaknesses
1.	It seems that the proposed algorithms are designed based on standard techniques, such as pessimism and MLE. The authors should elaborate more on their technical novelty. This is my main concern.
2.	It would be more clear to present conditions 1, 2 and 3 as assumptions. The authors should justify more on these assumptions. For example, why is condition 1 reasonable? Why the noise never changes the human preference? 
3.	In Theorem 1, the setup $C^*=2$ seems too specific. Can the result be extended to the one that allows general $C^*$ and depends on $C^*$?

### Questions
Please see the weaknesses above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
