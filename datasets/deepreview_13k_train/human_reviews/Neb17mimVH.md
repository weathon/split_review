# Many-Objective Multi-Solution Transport

- Decision: Accept
- Scores: 6, 8, 6, 6, 6, 5

## Abstract
Optimizing the performance of many objectives (instantiated by tasks or clients) jointly with a few Pareto stationary solutions (models) is critical in machine learning. However, previous multi-objective optimization methods often focus on a few objectives and cannot scale to many objectives that outnumber the solutions, leading to either subpar performance or ignored objectives. We introduce ''Many-objective multi-solution Transport (MosT)'', a framework that finds multiple diverse solutions in the Pareto front of many objectives. Our insight is to seek multiple solutions, each performing as a domain expert and focusing on a specific subset of objectives while collectively covering all of them. MosT formulates the problem as a bi-level optimization of weighted objectives for each solution, where the weights are defined by an optimal transport between objectives and solutions. Our algorithm ensures convergence to Pareto stationary solutions for complementary subsets of objectives. On a range of applications in federated learning, multi-task learning, and mixture-of-prompt learning for LLMs, MosT distinctly outperforms strong baselines, delivering high-quality, diverse solutions that profile the entire Pareto frontier, thus ensuring balanced trade-offs across many objectives.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a multi-objective multi-solution transport (MosT) framework to identify solutions that achieve diverse trade-offs across multiple objectives. The proposed method aims to generate solutions over the Pareto set of a multi-objective optimization (MOO) problem to maximize diversity, particularly in cases with a large number of objectives.

### Strengths
1. This work is well-organized and easy to follow. The idea is presented well.
2. The proposed method can achieve good performance on different synthetic and application problems.

### Weaknesses
1. When we just focus on the optimization problem Eq. (1-3), it is a multi-objective bi-level optimization problem. This problem is not new; many recent works have focused on designing gradient-based methods to solve it, as seen in [1] and [2]. Clearly, solving $\Gamma$ should rely on the current $\theta$ according to Eq. (2), so $\Gamma$ in the upper-level is a function of $\theta$, i..e. $\Gamma(\theta)$. So, when we try to calculate the gradient of the objective function in the upper-level w.r.t. $\theta$, there exists a hypergradient term $\frac{d\Gamma^*(\theta)}{d\theta}$. Can we just ignore the connection between $\Gamma$ and $\theta$ in the constraint part and directly write $\Gamma$ instead of $\Gamma(\theta)$ in the upper level? This simplification, while potentially making the problem tractable, needs further justification. The authors should provide a theoretical analysis or cite related work that supports this approximation, especially considering the potential impact on convergence and solution quality. Specifically, how does ignoring the hypergradient affect the optimization landscape and the ability to reach a desirable Pareto front? 

2. When the number of objectives is very large, I do not think MGDA-based methods can work well. The MGDA-based method needs to calculate the gradient of each objective in each iteration. This is not affordable when the model and the number of objectives are both large. I believe [3] can better solve such a problem, but the author does not discuss this work. The computational cost of calculating gradients for each objective in high-dimensional spaces can become prohibitive, limiting the scalability of the proposed method. The authors should provide a more detailed analysis of the computational complexity of their approach, especially in relation to the number of objectives and model parameters. Furthermore, they should explore alternative optimization strategies that can mitigate this computational burden, such as stochastic gradient descent or gradient compression techniques.

3. MGDA is a quite old baseline. I believe there are many MGDA-based methods, but the author does not discuss those works listed in [4]. The authors should include a more comprehensive comparison with state-of-the-art MGDA-based methods, which have incorporated various improvements such as adaptive learning rates, momentum, and other optimization techniques. This would provide a more robust evaluation of the proposed method's performance and highlight its specific advantages over existing approaches. The lack of comparison with recent MGDA variants makes it difficult to assess the true contribution of the proposed method.

4. MGDA and Linearization cannot reach the concave part in the Pareto front [4]. The author should discuss solution diversity with [4]. The authors need to address the limitations of MGDA and linearization in capturing the full Pareto front, particularly the concave regions. The authors should provide a theoretical analysis or empirical evidence to demonstrate that their method can overcome these limitations. Furthermore, the authors should discuss how their approach ensures solution diversity across the entire Pareto front, not just the convex regions.

5. Why does TAG fail in the MTL setting? In my view, the TAG just groups the tasks and trains these groups individually. It should not fail in such a setting. I quite doubt the authors' results. The authors need to provide a more detailed analysis of why TAG fails in the MTL setting. Simply stating that it fails is insufficient. What specific aspects of the MTL problem cause TAG to underperform? The authors should provide empirical evidence or theoretical arguments to support their claim, including details about the task characteristics and how they interact with TAG's grouping strategy.

6. Does $\Delta$ represent simplex in this paper? If so, the authors should use $\Delta^{n-1}$ and $\Delta^{m-1}$ in this paper, since $n-$simplex is a subset of $\mathbb{R}^{n+1}$. The author can check the corresponding definition in Wikipedia: https://en.wikipedia.org/wiki/Simplex

7. The article seems to have some compilation errors, e.g. $\tau=0$ in Line 280 and different style dash in Line 74 and 86.

8. Does $|| a ||$ represent the $l_2$ norm in this paper? I do not find where the author defines it since the authors also use $|| a ||_2$ in Eq. (6).

9. I think the authors did not read their paper carefully. I see the expression "Eq. equation *" dozens of times in this paper (e.g., Line 196, 206), which I believe is an expression error.

10. Eq. (45-46) $\to$ Eq. (47) seems need $L_i$ to be bounded functions. The authors do not make this assumption.

11. Lines 190-215 are just MGDA. I think those expressions can be placed in the preliminary part.

### Questions
See my questions in the weakness part.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes MoST, an approach based on optimal transport, that finds multiple Pareto solutions with many (can outnumber the solutions) objectives.

### Strengths
It is interesting to see how optimal transport can be applied in MOO, to find diverse solutions. And I find the application natural and sound.

This paper addresses a particular aspect in MOO where number of objectives can be much larger than the number of solutions, and still find 'diverse' solutions. To the best of my knowledge, this aspect is not previously addressed enough in modern MOO (e.g. gradient-based methods that can handle DNN training) context.

Experiments are quite comprehensive.

### Weaknesses
I don't find noticeable weakness in this paper.

### Questions
The convergence results seem to be regarding Pareto stationary only (which is fine). For convex and strongly-convex, is it possible to argue anything about Pareto optimality?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a novel Multi-objective multi-solution Transport (MosT) method to find a small set of diverse Pareto solutions for problems with a large number of objectives. MosT is formulated as a bi-level optimization problem, where the upper-level problem is to determine different objective weights for each solution via optimal transport (OT) based on their current performance, while the lower-level problem is to find a Pareto solution for each subproblem with weighted objectives. MosT can also be generalized to tackle multi-objective optimization problems with few objectives via random objective interpolation. This work also provides theoretical analysis to prove MosT can find a set of Pareto solutions via solving the bi-level optimization problem. Experiments show MosT can achieve promising performance on different synthetic and application problems.

### Strengths
+ This work is well-organized and easy to follow.

+ The *small solution set for a large number of objectives* setting is important for many real-world applications. This work is a timely contribution to an interesting yet under-explored research direction.

+ The proposed MosT method can achieve promising performance on different synthetic and application problems.

### Weaknesses
I was a reviewer of an earlier version of this work, and I have read the current submission in detail. I have the following major concerns about the proposed MosT method. 

**1. Motivation**

The key motivation of this work is to propose "a framework that finds multiple diverse solutions in the Pareto front of many objectives" and "ensures convergence to Pareto stationary solutions for complementary subsets of objectives". However, the terms diversity and complementary subsets are not clearly motivated and discussed in this work. The informal definition of diversity in Section 4 is helpful but not enough. How does the diversity connect to the complementary subsets of solutions found by MosT? Can we clearly define the "complementary subset" for MosT? Will the optimal solution set of MosT optimize some concrete diversity metrics?

**2. Balanced Weight Matrix**

For the proposed optimal transport based solution-objective matching method, it is not very clear why we prefer a balanced weight matrix for the objectives (i.e., "no model dominating on most objectives"). For a real-life application, if most of the objectives do share similar or even nearly identical structures, it is expected that one single solution can solve them well at the same time. 

**3. Theoretical Analysis**

In MosT, the MGDAs can reach any Pareto optimal solution of each weighted problem, which is exactly the same Pareto optimal set of the original problem. In other words, the current theoretical guarantee of MosT is not stronger than the original MGDA. The reason why MosT can be ensured to find a set of diverse Pareto solutions does not have proper theoretical support.

**4. Related Work**

In most experiments, the final metric for comparison is the mean of average performance across all objectives. Why not directly optimize this metric using a specially designed method like the sum-of-minimum optimization method [1]? It seems that the method in [1] can efficiently match each objective-solution pair via a clustering-like approach. What are the pros and cons of MosT compared with this method?  

[1] Efficient Algorithms for Sum-of-Minimum Optimization, ICML 2024.

**5. Runtime Analysis**

For the runtime comparison in Table 4, it is counter-intuitive to see linear scalarization require more runtime than MGDA. What is the computational overhead of linear scalarization over MGDA? 

**6. Experiment**

Comparison with the related sum-of-minimum optimization method [1] is needed.

### Questions
See weaknesses.

### Soundness
2

### Presentation
2

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
This paper introduces a framework called "Many-Objective Multi-Solution Transport" (MosT) aimed at efficiently optimizing numerous objectives across a limited set of models. Traditional multi-objective optimization methods struggle to balance many objectives simultaneously, often focusing on only a few, which can lead to neglected objectives or poor performance. MosT overcomes this limitation by assigning each model to a complementary subset of objectives, ensuring diverse solutions across the Pareto frontier. It does this by using a bi-level optimization process: (1) an optimal transport (OT) method matches objectives to solutions balancing the performance trade-offs (2) a multi-objective optimization (MOO) per solution to optimize assigned objectives using MGDA. The approach demonstrates success across applications such as federated learning, multi-task learning, and prompt learning in language models, outperforming simple baseline methods in terms of both accuracy and diversity.

### Strengths
- **Novelty for MOO:** The paper introduces a bi-level optimization method based on a very natural idea. Combining MGDA and OT is a elegant idea.

- **Specialized Model Expertise:** It's a keen observation to see that each model naturally becomes an "expert" for a specific subset of objectives as a result of sparse OT solution.

- **Applicable to multiple applications:** MOST demonstrates success across federated learning, multi-task learning, and mixture-of-prompt learning, highlighting the framework’s adaptability.

### Weaknesses
 - **Missing stronger baselines**: The paper compared MOST against trivial benchmarks. If the goal is to compare methods based on their diversity and the coverage of Pareto Front, nontrivial benchmarks like [1] (and benchmarks therein) must be also taken into consideration. 

- **Evaluation Metrics**: Hypervolume [2] has been the established metric for evaluating and measuring coverage in Pareto Front for MOO methods. The reviewer does not see average accuracy across all objectives in all models as a good metric. The average accuracy metric fails to capture the diversity of the solutions, which is a key aspect of multi-objective optimization. It is possible to achieve a high average accuracy while having very similar solutions that do not explore the Pareto front effectively. This is especially problematic when the number of objectives is large, as the average can mask poor performance on specific objectives.

### Questions
* The paper claims "We do not evaluate on hypevolume for many-objective scenarios due to its computational complexity and infeasibility in high-dimensional settings (i.e., many objectives)". Why? What's the time complexity of computing hypervolume of  M solutions over N objectives?

* In the chosen evaluation metric of average accuracy, what's the average over? Is it over all M solutions and all N objectives (average over MxN items)? 

* In 3.2, the paper discusses the case of having more solutions than objective (M>N). What's the goal in here? We can clearly form "experts" i.e. each solution optimizes a single objective. Is our goal to capture M different trade-offs among N objectives even though M>>N?

### Soundness
4

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
3

### Summary
In this paper, the authors propose a novel method called many-objective multi-solution transport (MosT) for finding $ m $ multiple solutions for $n$ many-objective optimization. The framework is primarily focused on the case where $ n \gg m $, but the paper suggests it is also suitable for cases when $ n \ll m $. The problem of finding the aforementioned (few good) multiple solutions for many objectives is formulated as a bilevel optimization problem. In this setup, the lower-level problem is to find the optimal transport (OT) between a given set of objectives and solutions under certain constraints, while the upper-level problem is to determine the solution parameters by solving a multi-objective optimization (MOO) problem, weighted by the solutions of the lower-level OT problem. The paper provides convergence guarantees for MosT under non-convex, convex, and strongly convex settings. Additionally, it presents empirical results for the performance of the MosT method by applying it in federated learning (FL), multi-task learning (MTL), and mixture-of-prompt learning applications. The results suggest that MosT can be efficiently implemented in real-world applications and can outperform existing baselines for finding multiple solutions for many objectives.

### Strengths
* The problem discussed in the paper is an interesting one, and seems to not have been given much attention in prior related work
* The paper provide theoretical guarantees and empirical validation of the efficacy of the proposed method.
* The flow of the paper towards the build up of the proposed method is fairly clear and easy to follow.

### Weaknesses
 * In Figure 1, it is better to indicate the fact that the performance is based on 5 different solutions, and also discuss how you choose a particular solution (out of 5 solutions) for a particular objective in the text when you refer to Figure 1.

* It is unclear why MosT can be useful for $n \ll m$ case. Intuitively, shouldn’t separately optimizing each objective with separate parameters give you the smallest best possible solution set in this setting?

* Figure 3 shows MosT achieves maximum diversity among clients, compared to other baselines. However, it is unclear why the diversity of parameters among clients in a distributed optimization setting is desirable since usually, the goal is to train a single global model using knowledge from distributed data among the clients. Also, it is unclear why the client models are diverse throughout the training process. Specifically, aren’t the client models aggregated and redistributed periodically, as done in FL traditionally?

* The rationale behind computing the MGDA weights just by considering the final layer bias weights seems not clearly justified in the text.

* Some closely related recent work [1] seems to be missing from discussion and comparison.

**Minor comments**

* In lines 349-351 “Initially, the mean loss increases and then decreases..” seems to be opposite to the observation from Figure 2?

### Questions
* If the goal is to find a set of solutions that can work on all objectives,  in $ n\ll m$ case, why MosT is superior to optimizing separate parameters for each $n$ objective, to obtain $m=n$ solutions? 
* What is the rationale behind computing the MGDA weights just by considering the final layer bias weights?
* In the FL setting, why client diversity is desirable, and why MosT does not seem to achieve consensus throughout the training process ( please refer to point 3 in Weaknesses for more details )?
* Can the authors provide some qualitative/quantitative comparison between the proposed method and prior work [1] ?

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
3

### Summary
This paper presents Many-objective multi-solution Transport (MosT), a framework for optimizing many objectives simultaneously by finding diverse solutions on the Pareto front. Unlike traditional methods that struggle with numerous objectives, MosT assigns each solution to specialize in a subset of objectives, collectively covering all. Using bi-level optimization with optimal transport, it ensures convergence to Pareto stationary solutions. MosT outperforms baselines in applications like federated learning, multi-task learning, and LLM prompt learning, providing balanced trade-offs across many objectives.

### Strengths
1) The paper presents a solid motivation based on the provided background (though further elaboration might be helpful, see weaknesses for details).
2) The experiments show strong performance when compared to the baselines.
3) The study includes both experimental results and theoretical analysis, providing a comprehensive evaluation.

### Weaknesses
1) The methods and baselines referenced in the related works and experiments seem somewhat outdated, especially considering the paper targets ICLR 2025. Only one cited paper is from 2023-2024, raising concerns about whether this reflects a small lag in the field’s development or if the paper is not keeping up with recent advancements. Specifically, the baselines used in the experiments, such as those in federated learning (e.g., FedAvg, FedProx), are well-established but do not represent the current state-of-the-art. This raises questions about the relevance of the comparisons and whether the proposed method truly outperforms more recent and advanced techniques.
2) In both multi-task learning and federated learning, several methods have been proposed to address the challenge of using M models for N objectives. For example, in federated learning, "Personalized Federated Learning under Mixture of Distributions" uses EM algorithms, while in multi-task learning, "Harmony Multi-Task Decision Transformer for Offline Reinforcement Learning" (HarmoDT) employs bi-level mask learning. These approaches could have been considered in the context of this work. The paper lacks a detailed discussion on how the proposed method compares to these alternative approaches, particularly in terms of the underlying optimization strategies and their effectiveness in handling diverse objectives. This omission makes it difficult to assess the novelty and practical advantages of the proposed method.
3) The ablation studies shown in Section 6.5  are insufficient and lack in-depth analysis. For instance, in the conclusion regarding the "Benefits of diversity-encouragement regularization," the explanation (line 475) is limited to stating that it "enhances performance and fairness" without providing detailed evidence or elaboration. The ablation study should include a more granular analysis, such as examining the impact of different regularization strengths or comparing the performance on individual objectives. More rigorous ablations would strengthen the paper.

### Questions
1) Since only one cited paper is from 2023-2024, question is that whether this reflects a small lag in the field’s development or if the paper is not keeping up with recent advancements. 

2) When comparing to works like "Personalized Federated Learning under Mixture of Distributions" and "Harmony Multi-Task Decision Transformer for Offline Reinforcement Learning," could you emphasize the key differences and advantages of your method in solving N objectives with M models?

3) If appropriate, I suggest including papers such as "Personalized Federated Learning under Mixture of Distributions" and "Harmony Multi-Task Decision Transformer for Offline Reinforcement Learning" in both the related works and experiments sections. If inclusion isn't suitable, please provide an explanation for this choice (also fine if reasonable).

### Soundness
2

### Presentation
3

### Contribution
2
