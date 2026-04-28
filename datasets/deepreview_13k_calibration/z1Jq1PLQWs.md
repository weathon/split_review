# Dueling in the Dark: An Efficient and Optimal $O(\sqrt{T})$ Mirror Descent Approach for Competing against Adversarial Preferences

- Decision: Reject
- Avg Score: 5.67
- Scores: 5, 6, 6, 6, 6, 5

## Abstract
Recent developments in Large Language Models (LLMs) have sparked significant attention in Reinforcement Learning from Human Feedback (RLHF), which uses reinforcement learning techniques to optimize a model's performance through human-provided feedback. A simple, widely used, and cost-effective method for gathering human feedback is through relative queries based on human preferences, often modeled using sigmoid utility models. Despite the popularity of sigmoid model-based RLHF algorithms, their theoretical foundations remain underdeveloped as existing algorithms often lack performance guarantees or are limited to small-scale problems due to computationally intractable steps. We address the challenge of developing no-regret learning algorithms for training optimal policy RLHF, and develop the first efficient gradient descent-based algorithm with near-optimal regret guarantees. More technically, we consider the adversarial online convex optimization problem with preference feedback and propose a mirror descent method to obtain a regret of $O(\sqrt{T})$ over $T$ rounds. The main challenge we are required to solve lies in finding a suitable `gradient-approximation' of the underlying utility functions solely from a binary preference feedback. Following this we extend our results to policy optimization in the RLHF framework with trajectory preferences and design no-regret RL policies using a variant of mirror descent. We also extend our methods beyond pairwise preferences --- to multi-way (batched pairwise) feedback and ranking feedback --- and analyze the trade-off between learning rate with increasing subset size. Our contribution lays the groundwork for a practical gradient descent-based algorithm in RLHF with human preferences. Supported by robust theoretical guarantees, our approach holds promise in the current landscape of developing efficient algorithms for LLMs and addressing human-AI alignment challenges. Empirical evaluations validate our theoretical findings.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper "Dueling in the Dark: An Efficient and Optimal Mirror Descent Approach for Online Convex Optimization with Adversarial Preferences" addresses the challenge of using human preference feedback in reinforcement learning, particularly with applications for AI alignment in large language models (LLMs). The main focus is on creating an efficient online gradient descent algorithm capable of handling adversarially changing preferences, providing theoretical guarantees for performance.

### Strengths
1. Algorithmic Innovation: The authors introduce an Online Mirror Descent (OMD)-based algorithm, named Double-Scrible, that optimally handles adversarial preferences using only weak preference feedback, unlike previous models that rely on value feedback.

2. Performance Guarantees: This algorithm achieves optimal regret bounds and includes generalizations to batched feedback (handling multiple preference queries at once) and multi-way preference feedback (handling partial ranking).

3. Efficiency: The approach offers computational efficiency, particularly suitable for high-dimensional and adversarial environments, making it more practical for real-world AI applications.

### Weaknesses
1. For the formulation, there is already some work formulating the problem like a dueling bandit (Xiong et al. (2024), [2]) and even dueling bandit with human feedback [1]. I think this work needs to provide more discussion of the comparison with those works. Especially with [1], because they both consider adversarial preference feedback.

2. One of the contributions that the authors highlight is the computational efficiency of their algorithm, but they don't carry out experiments or even simulations to show the computational efficiency of their algorithm. It is questioned whether their algorithm can be implemented. Hence, the authors are suggested to provide some experiments.

### Questions
1. Line 458: "in the convergence proof of ??" lacks the reference.

2. Although the bound for top m ranking is better than pairwise comparison, the query times of the two methods are different. Can the authors compare the total query complexity of the two methods to achieve the same suboptimality?

### Soundness
3

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
This paper proposes an efficient online mirror descent algorithm called "Double-Scrible" for optimizing Large Language Models (LLMs) using human preference feedback, where the algorithm only observes relative preferences between pairs of outputs rather than direct feedback.

### Strengths
1. This paper seems to be the first to address the problem of adversarial online linear optimization with preference feedback, and the analysis is very comprehensive. Some techniques such as the gradient estimation for preference feedback seem novel to me.
2. The algorithms/assumptions and Theorems are clearly stated.

### Weaknesses
1. Missing related work section? And adding some intuition on algorithm design would make it easier for the readers to understand.
2. The paper assumes linear model, and the algorithms require eigenvalue decomposition, which makes the algorithms hard to scale up.

### Questions
1. The paper assumes linear model. Is it possible to extend it to the nonlinear setting? And is there a way to circumvent the eigenvalue decomposition?
2. Since the proposed algorithms are online, I wonder how the algorithms facilitate exploration.

### Soundness
3

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
This paper introduces Double-Scrible, a gradient descent algorithm for online linear optimization with adversarial preferences applicable to the online alignment of LLMs. Using mirror descent with a self-concordant barrier function, it achieves near-optimal regret bounds and extends to batched and partial ranking feedback.

### Strengths
The paper is well written. Both the problem and algorithms are rigorously explained, and the notation is intuitive.  I did not check the proofs, but the claims in the paper are sound. I appreciate various practical extensions of the algorithm to batched and ranked settings.

### Weaknesses
The algorithm is not empirically evaluated. Without any experiments, it may be difficult for the readers to apply the algorithm in practice as there is no reference implementation. Furthermore, aligning LLMs is a difficult domain, and theoretically sound algorithms may not necessarily have an effect as the human preferences are non-linear and context-dependent, the number of LLM arms grows exponentially with the length of the sentence, etc. Even small-scale experiments using, e.g., GPT-2, can increase the impact of the paper. The lack of empirical validation makes it hard to assess the practical relevance of the proposed method, especially given the complexities of the LLM alignment problem. The paper does not address how the algorithm's performance might degrade with the high dimensionality and non-convexity inherent in real-world LLM preference learning scenarios. The theoretical guarantees, while strong, are not directly linked to practical performance in the complex landscape of LLM alignment, which raises questions about the algorithm's applicability in realistic settings.

### Questions
Minor comment: Undefined reference at L458.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on the online convex optimization problem from preference and ranking feedbacks, which is a simplification of the modern RLHF framework. The paper studies the adversarial online linear optimization problem where the utility of each arm is linear. At each round, the agent plays two arms and the feedback on which arm is better is generated based on the Bradley-Terry model. The goal of the agent is to minimize the utility regret. The paper proposes an online mirror descent algorithm named Double-Scrible for the pair-wise preference setting, with provable regret guarantee matching the lower bound. Generation to batched settings and ranking feedbacks are also studied with theoretically optimal algorithms.

### Strengths
1. Novelty and Impact: This paper studies the online convex optimization problem with preference feedback, the problem is of importance and directly related to solving RLHF problems in practice. The insight of the proposed algorithm has potential in many RLHF application areas.

2. Theoretical Soundness: For all three feedback settings, i.e., pair-wise preference feedback, batched feedback, and ranking feedback settings, the paper propose gradient based online optimization algorithms which has theoretical regret guarantees matching the lower bound. Overall it is a solid theoretical paper with good contribution.

3. Algorithm Practicality: the proposed algorithm is computationally tractable with gradient based approach, the major computation burden in each iteration seems to come from eigen decomposition.

### Weaknesses
1. Motivation: the motivation of study adversarial human feedback (the linear parameter \theta_t adversarially change over time) seems weak from the presentation of paper.

2. Comparison: the regret definitions are different for each feedback settings, which makes comparing the bounds across settings unfair. For example, the bound in Theorem 3 accounts for the case where the sample size and the number of human queries are B times larger than the case in Theorem 1 (although the definition of regret in batched setting is averaged). Therefore, the claim that batched comparison and ranking feedback improves algorithm performance is not completely solid, although correct.

3. Computation Efficiency: one of this paper's claim is the proposed algorithm is more computationally efficient compared to confidence based algorithms (UCB or TS based) in the literature, but the evidence is not clear from the paper. Given computation tractability is a major strength of the proposed algorithm, the reviewer feels that numerical evidence should be provided, at least for a simple setup.

Typos: 

1. equation 1 seems to be a typo

2. Theorem 3, superscript of regret should be Batched-LogitDB

3. line 458, missing reference.

### Questions
1. Can you provide more examples on why adversarial human preference is of importance in RLHF applications, to motivate your theoretical framework?

2. Can you provide numerical evidence showing the computation efficiency of your proposed algorithm? 

3. Can you present the regret bound of the three settings in a way that can be fairly compared?

4. In line 347, you claim your runtime requirement is O(dT), it seems does not count the computation complexity of eigen decomposition?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a mirror descent approach for a variety of online linear optimization (OLO) problems that involve preference feedback.  The work presents matching upper- and lower-regret bounds (up to logarithmic factors) for each of the scenarios considered.  First, the authors consider adversarial logistic dueling bandits and present the Double-Scrible algorithm with matching $O(\sqrt{T})$ upper and lower regret bounds. The authors generalize this work to the batched setting and present the BaBle-Scrible algorithm we equivalent matching regret bounds.  Finally, the authors show that the top-m ranking feedback setting can be reduced to the batch setting and they present MNL-Scrible with equivalent matching regret bounds.

### Strengths
This is a reasonably well written paper that is easy to read despite its highly technical nature.  The work addresses a seemingly important problem of OLO with preference feedback.  By the author's admission this is the first efficient online gradient descent-based algorithm for this problem with provably optimal performance guarantees.  The paper does a good job of considering generalizations of the original dueling bandits framework by incorporating batched responses and ranked preferences.

### Weaknesses
 **UPDATE** The AC should be aware that the current draft of this paper contains a significant amount of content on page 11.  It thus risks a desk reject.  I am comfortable with the initial version of the paper, without experiments, which fits in the 10-page limit. 

**NOTE** I do not consider myself qualified to adequately review this paper as I am not an ML theorist.  I do not have sufficient knowledge of the literature in this space to judge impact / contribution.  I have notified the AC to this effect early in the review process but did not receive a response.  Nevertheless, below is my best attempt at a critique for this work and I will assign a low confidence score to help calibrate.

Rather than do one thing well this paper reaches for a lot of potential contributions that in my opinion lessen the overall impact of the work.  In particular, the references to LLMs in the abstract and introduction seem a bit misplaced as it is unclear what the actual connection is to LLMs in this work (marketing?).  The authors present three algorithms with regret bound analysis, but do not provide any guidance on implementation or empirical validation, making it impossible to conclude whether the algorithms are effective in practical settings.

One of my issues in reviewing this work is that I cannot place it in the context of existing work.  The paper would benefit from a "Related Work" section to help highlight the potential impact of these contributions w.r.t. existing work.  

As a broader comment, ICLR is a conference on "learning representations" and it is unclear what connection this work has to representation learning.  At first glance it would not seem that this work is well-placed at ICLR.  Upon further digging it seems that ICLR has published quite a few works on bandit algorithms and so perhaps the organizers better insight into the fitment of this work to the conference.

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work studies the linear dueling bandit problem with adversarial binary feedback. The author proposes a novel algorithm based on the Mirror Descent method and achieves a near-optimal regret guarantee. In addition, the author extends the algorithm to deal with batched datasets or multinomial bandits, maintaining a similar regret guarantee.

### Strengths
1. The author proposes a novel algorithm based on the mirror descent method and achieves a near-optimal regret guarantee.

2. The author generalizes the result to several bandit settings with batched datasets and multinomial logit bandits.

3. The paper is well-written and easy to follow.

### Weaknesses
My main concern is that the author may be overclaiming some contributions.

1. As the author mentioned when discussing the limitations of existing algorithms, prior attempts to adapt them to RLHF either make unrealistic modeling assumptions or are computationally inefficient. The main contribution of this work is claimed to be the development of more computationally efficient algorithms. However, this work focuses only on the logistic linear bandit, which also falls under the category of unrealistic modeling assumptions and does not offer a clear advantage over previous algorithms for logistic linear bandits. Additionally, under this setting, an efficient algorithm [1] already exists, even with adversarial preferences. The cited work [1] proposes an algorithm for contextual dueling bandits with adversarial feedback, which appears to address a similar problem space. It is unclear how the proposed method offers a significant advantage in computational efficiency or regret bounds compared to the algorithm presented in [1], especially when restricted to the logistic linear bandit case.

2. The author claims a contribution for providing a lower bound on the regret when learning a logistic dueling bandit. However, a lower regret bound already exists in previous work [2]. Specifically, [2] provides a lower bound for the stochastic contextual dueling bandit problem under linear stochastic transitivity models, which seems to encompass the logistic dueling bandit setting considered in this paper. The authors should clarify the novel aspects of their lower bound compared to that of [2]. 

3. The author mentions that gradient descent algorithms are simple to implement and can seamlessly integrate with modern deep learning frameworks, making these methods computationally efficient. However, the proposed method only focuses on the logistic dueling bandit, and it is unclear how to implement it in modern deep learning frameworks or whether the performance guarantees still hold in such settings. Furthermore, when restricted to the logistic dueling bandit problem, the proposed method does not seem to offer an advantage over UCB or Thompson Sampling (TS) methods. The paper does not provide a detailed comparison with UCB or TS methods in the context of logistic dueling bandits. A theoretical or empirical comparison would be beneficial to highlight the advantages of the proposed method.

### Questions
See Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
