# Goodhart's Law in Reinforcement Learning

- Decision: Accept
- Scores: 5, 6, 6, 8

## Abstract
Implementing a reward function that perfectly captures a complex task in the real world is impractical. As a result, it is often appropriate to think of the reward function as a \emph{proxy} for the true objective rather than as its definition. We study this phenomenon through the lens of \emph{Goodhart’s law}, which predicts that increasing optimisation of an imperfect proxy beyond some critical point decreases performance on the true objective. First, we propose a way to \emph{quantify} the magnitude of this effect and \emph{show empirically} that optimising an imperfect proxy reward often leads to the behaviour predicted by Goodhart’s law for a wide range of environments and reward functions. We then provide a \emph{geometric explanation} for why Goodhart's law occurs in Markov decision processes. We use these theoretical insights to propose an \emph{optimal early stopping method} that provably avoids the aforementioned pitfall and derive theoretical \emph{regret bounds} for this method. Moreover, we derive a training method that maximises worst-case reward, for the setting where there is uncertainty about the true reward function. Finally, we evaluate our early stopping method experimentally. Our results support a foundation for a theoretically-principled study of reinforcement learning under reward misspecification.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents an analysis of Goodhart’s law in reinforcement learning. The paper starts with a formalization of the Goodhart problem in terms of misalignment of reward functions on finite MDPs: one proxy reward that the policy optimizes when we really wish to optimize the other. The paper justifies that the problem occurs in small scale experiments demonstrating that increasing the optimization pressure on the proxy eventually leads to a decrease in the true reward. A theoretical analysis is given with some examples about why this occurs in finite MDPs. Finally an early-stopping algorithm is proposed to mitigate this issue along with some preliminary experiments on the algorithm.

### Strengths
The problem is clearly very important and a better understanding of proxy rewards, overoptimization, and Goodhart’s law are definitely needed in the community.

The paper is presented fairly clearly, except in some areas which I point out later.

The paper provides insights from multiple frontiers to help shape this understanding (empirical, theoretical, and conceptual).

The theoretical findings are useful, but not entirely surprising given what is known already in the literature (see below). However, I do believe it’s useful to have this formalized and characterized when specifically talking about Goodhart’s law.

### Weaknesses
My primary complaint is that, although this is a solid analysis, I do not believe it strikes the heart of the Goodhart problem. The position of the paper is that misalignment can be characterized by the worst-case angle between reward functions. This is a fairly well-understood setting (e.g. see ‘simulation lemma’ by Kearns & Singh or any number of classical RL papers). However, it’s unclear how this maps into problems that (1) are beyond the finite case, or (2) are classical examples of Goodhart’s law like the snake bounty. While one could model (2) in the framework studied here, I am not sure this would be an informative model in those settings as the ‘theta’ is just so large.

The above is more of a conceptual disagreement about the premise. For the rest of the review, I give the benefit of the doubt and simply accept the premise is true.

Unfortunately most of the important empirical results have been relegated to the appendix, leaving the main paper with vague / difficult-to-verify statement such as ‘a Goodhart drop occurs for x% of all experiments. Without figures or tables, it’s difficult to understand what this means, such as what the criteria of a ‘Goodhart drop’ is (any non-zero drop, some negligible drop, etc). It would be helpful to make room in the main paper for results that present a more comprehensive picture of the findings.

The early stopping proposal is natural, but also seems very conservative. This appears to be consistent with the empirical findings. Furthermore it requires knowledge of $\theta$, which is just assumed to be known. While it’s hard to imagine anything can be down without some knowledge of the true reward or structure, this seems quite coarse.

Figure 5 is difficult to appreciate in absolute terms as one cannot tell if, for example, 0.4 is a large value relative to the reward achievable. I think this plot would be better replaced with a typical plot showing how the true and proxy rewards change as the policy is optimized and when the algorithm decides to stop, as well as the counterfactual of what would happen if it does not stop.

### Questions
How do you think the theoretical results generalize to the setting where the reward function is considerably more sophisticated than simple finite MDPs? For example, high dimensional, continuous state-action, long-horizon problems?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the problem of reward misspecification. The authors point out that over-optimizing an incorrect reward function can lead to the wrong behaviour for the true ("test") reward function, and dub this phenomenon Goodharting. The authors propose a quantitative way to evaluate this phenomenon (cf. Definition 5), and perform an experimental case study on some simple MDPs to establish that Goodharting is a common phenomenon in RL. The authors then provide an intuitive geometric explanation for this phenomenon and propose an early stopping method to avoid overfitting. Further experimental evaluations are performed on the early stopping method to

### Strengths
The paper investigates an interesting, albeit not entirely surprising phenomenon, and investigates it thoroughly and carefully. The problem of reward misspecification is quite relevant for practical considerings of RL, so gaining some understanding of this problem is appreciated. The paper is well-written and the messages are conveyed clearly. The theoretical contributions, while not exactly practical, are a nice step towards preventing this problem from affecting performance.

### Weaknesses
While I am overall positive about the paper, I have a few comments and suggestions for possible improvement. 

- The definition of optimization pressure is a bit strange. Why should we not define it as simply the distance from the optimal policy? For instance, we can say that the optimization pressure is epsilon if we obtain a policy $\hat{\pi}$ such that $J_R(\pi^\star) - J_R(\hat{\pi}) \leq \varepsilon$. I feel that tying the optimization pressure to a certain regularization scheme detracts from the fundamental aspect of the problem, and furthermore that regularization is only used here as a proxy for "how close to optimal are we", which can be defined more directly as above.
- The environments that have been used to establish that Goodharting is pervasive (Section 3) are somewhat simple. I understand that it is difficult to measure the NDH metric in environments where we cannot solve for the optimal policy, but it would have been nice to understand how pervasive this is in "real" problems, or at least in popular RL benchmark environments. As a side note, the fact that the NDH metric is inherently difficult to measure can be considered as a drawback of the proposed methodology -- can the authors comment?
- It would also have been interesting to more systematically study which properties of environments imply that Goodharting is more likely to take place, do the dynamics of the MDP (e.g. a bottleneck structure) have any role?
- The proposed optimal stopping algorithm is very pessimistic since it tries to avoid overfitting to any possible reward function in a certain set (is this pessimism unavoidable?), and as the authors point out it is computationally infeasible. In addition, if I understand correctly, it requires knowing the transition dynamics and knowing the distance between the proxy reward and the true reward function, which is fairly unpractical.

- Incorrect/unclear sentences: 
1. "We observe that NDH is non-zero if and only if, over increasing optimisation pressure, the proxy and true rewards are initially correlated, and then become anti-correlated". I believe the authors meant the NDH is non-negative, not non-zero.
2. "Note that this scheme is valid because for any environment, reward sampling scheme and fixed parameters, the sample space of rewards is convex. In high dimensions, two random vectors are approximately orthogonal with high probability, so the sequence R_t spans a range of distances.". It is not clear what point the first sentence is attempting to communicate (what does "valid" mean?), and the second sentence is incorrect as stated (what distribution is one sampling from? I can imagine many distributions where this is untrue, say a deterministic one.)

### Questions
See weaknesses section above.

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
Most reinforcement learning algorithms are designed for accurate reward feedback. However, in practice, accurate reward feedback may not be available. In the presence of inaccurate reward feedback, it is possible to observe a phenomenon that the performance of the training policy first increases and then decreases after passing a threshold point. This paper addresses this interesting phenomenon and names it “Goodhart’s Law in RL”. To solve this problem, this paper quantifies the magnitude of this effect and how it exists in a wide range of environments and reward functions. It provides a geometric explanation and an optimal early stopping method with theoretical regret bounds. They then empirically showed the performance of their early stopping method.

### Strengths
1. This paper is quite novel because it raises an interesting and important observation – the performance of a policy increases first and then decreases. Such observation is caused by inaccurate reward feedback, which indeed exists in real RL applications.

2. This paper quantifies the magnitude of such phenomena and provides a clear geometric explanation.

3. With these insights, this paper proposes an optimal early stopping method with theoretical regret bound analysis.

4. The experimental results supported the authors' claim.

5. This paper is well-written. Concepts are conveyed efficiently. The analysis is detailed while keeping a clear line of high-level logic.

### Weaknesses
1. The optimal early stopping rule relies on the knowledge of the occupancy measure and the upper bound $\theta$ of the angle between the true reward and the proxy reward. Methods to approximate the occupancy measure are well-researched. My concern is on the approximation of $\theta$, which is a relatively new concept and requires some knowledge of the true reward feedback or true reward samples. When such estimation is not accurate, the stopping method could exhibit negative performance. It would be better if the author could show empirical results with approximated $\theta$. Specifically, the paper does not address how sensitive the early stopping method is to errors in the estimation of $\theta$. A small error in $\theta$ could lead to a significant deviation from the optimal stopping point, potentially resulting in worse performance than not using early stopping at all. The paper should include a sensitivity analysis of the stopping rule with respect to the accuracy of the estimated $\theta$. This analysis should include a range of error magnitudes and their impact on the final policy performance.

2. This paper is preliminary because it only considers finite state and action space. The empirical results are also only on small grid world environments. It is not clear whether such a phenomenon exists in more broad continuous settings and what would be the practical way to solve it in these settings. The theory developed in this paper relies heavily on the assumption of finite state and action spaces. This assumption allows for the use of techniques that may not be directly applicable to continuous spaces. The paper does not discuss the challenges of extending the theory to continuous spaces, such as the need for function approximation and the potential for instability. Furthermore, the empirical results are limited to small grid world environments, which may not be representative of the complexities found in real-world applications. The paper should include a discussion of the limitations of the current theory and empirical results and identify the key challenges in extending the work to more complex environments.

### Questions
N/A

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the interplay between reward misspecification and optimisation in RL as an instance of Goodhart's law. The authors provice geometric explanations of how optimisation of a misspecified reward function can lead to worse performance beyond some threshold, and show in experiments that several environments and reward functions are prone to Goodhart's law and optimisation of a reward proxy eventually leads to worse performance. The authors also propose an early stopping algorithm to address this problem.

### Strengths
- First of all, the studied topic is, in my opinion, important and could be of interest to many in the ICLR community. 
- The paper is a good attempt at extending prior work on reward misspecification and reward gaming (e.g., Skalse et al. 2022) to the question of what role optimisation plays and whether we can characterize reward misspecification from a policy optimisation standpoint as well. I am not very well acquainted with the related work, but the contributions and many of the ideas in this paper seem novel to me.
- The results are very interesting and provide some nice intuition about the interplay of reward distance, optimisation and MDP model. While I don't think that one should overinterpret the results as they are either based on empirical studies of a some specific set of environments or on theoretical insights with idealised assumptions, I think that the findings of this paper are overall very interesting.

### Weaknesses
 - The evidence on the "Goodharting" effect are only circumstantial. Experiments on some specific set of environments such as grid worlds do not necessarily allow us to extrapolate. After all, the Goodharting effect can only be "explained" but not characterised. Nevertheless, these experiments and the geometric explanations provide good intuition which I think is very interesting and could inspire future lines of work. 
- A minor weakness is that the proposed early stopping algorithm might not perform well due to large reward losses from stopping early, which is somewhat expected due to its pessimistic nature. The algorithm is also fairly impractical bcause it assumes prior knowledge of $\theta$. Specifically, the requirement to know the upper bound on the angle between the true and proxy reward functions seems unrealistic in practical scenarios, as this would require knowledge of the true reward function which is, by definition, unknown. Furthermore, the algorithm's performance is highly sensitive to the choice of this bound, and a poor choice could lead to either premature stopping or continued optimization of the misspecified reward.


### Questions
- Your work seems to be tailored to the specific choice of difference metric between two reward functions (their angle). I guess that the main reason for choosing this distance metric is that it is a STARC metric. 
	- However, can you provide further justification for why the "angle" is a good choice or even the *right* choice? 
	- What could another reasonable metric be?  
	- And, how would choosing a different metric impact your results?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
