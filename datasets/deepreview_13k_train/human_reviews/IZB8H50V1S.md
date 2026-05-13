# Learning Policy Committees for Effective Personalization in MDPs with Diverse Tasks

- Decision: Reject
- Scores: 6, 6, 6, 5

## Abstract
Many dynamic decision problems, such as robotic control, involve a series of tasks, many of which are unknown at training time. Typical approaches for these problems, such as multi-task and meta reinforcement learning, do not generalize well when the tasks are diverse. We propose a general framework to address this issue. In our framework, the goal is to learn a set of policies—a policy committee—such that at least one is near-optimal for most tasks that may be encountered at execution time. While we show that even a special case of this problem is inapproximable, we present two effective algorithmic approaches for it. The first of these yields provably approximation guarantees, albeit in small-dimensional settings (the best we can do due to inapproximability), whereas the second is a general and practical gradient-based approach. In addition, we provide provable sample complexity bounds for few-shot learning settings. Our experiments in personalized and multi-task RL settings using MuJoCo and Meta-World benchmarks show that the proposed approach outperforms state-of-the-art multi-task, meta-, and personalized RL baselines on training and test tasks, as well as in few-shot learning, often by a large margin.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper studied multi-task reinforcement learning and proposed an algorithm that is able to identify a set of policies that includes the optimal policies of majority tasks. The paper theoretically characterized the performance of the algorithm and also conducted experiments to demonstrate the effectiveness of the proposed methods.

### Strengths
1. The proposed method of learning a committee of policies for different tasks is novel, because it provides a potential solution to multi-task RL by enabling more adaptability.
2. The investigation is thorough by providing both theoretical and experimental results.

### Weaknesses
1. The presentation could be further improved, especially in section 3. For example, while the title of sec 3.2 is 'Clustering', there is no explicit description of how to do cluster in the following context. I would assume the construction of $C$ in definition 2 should be the clustering method. Please correct me if I am wrong. It is better to use pseudo-code to highlight the steps.
2. Another weakness has been discussed a little by authors. That is, the algorithm relies on task representations.

### Questions
The impact of hyper-parameters on the performance can be further explained. For example, does a larger committee policies ($K$) always yield better results? How should we choose $K$ in practical applications?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a novel method for multi-task reinforcement learning with diverse tasks. Instead of using a single policy to act on a random draw of a task (as common in meta-rl and multi-task rl), the authors suggest clustering the task based on the task parameters and learning a different policy for each cluster. First, theoretical motivations were given for the connection between the clustering problem to the original problem, the clustering problem itself, and a proposed few-shot adaptation using the policy committee. Secondly, the authors performed an empirical study on two common benchmark suits while comparing to multiple meta and multi-task rl methods.

### Strengths
1. Effectively learning a committee of policies instead of one policy for all tasks has a big potential to help in real-world application of multi-task rl, though a more thorough analysis of this is lacking (see weakness 1)    

2. Overall the presentation of the paper is good, the notations are clear and the ideas presented are well-motivated.

3. The Related Work section is well-articulated and contains a broad spectrum of related topics.

4. The Metaworld benchmark is very popular in the meta rl and multi-task rl literature and the authors compared to multiple common baselines in the fields.

### Weaknesses
1. While the theorems shown in the paper motivate **how** to find a cover for a set/distribution of tasks, there is little to no discussion on **why** this should lead to improved performance compared to a single policy. The only mention I found regarding this question is the paragraph in lines 153-159. Theoretical analysis and motivation on when a policy committee should help compared to a single policy is missing. For example, the authors claim a policy committee should help when faced with outlier tasks. Is this the only case where a policy committee would be beneficial? If so, why should it have superior results in the Mujoco benchmark where there aren’t any outliers? A more rigorous theoretical justification for the use of a policy committee, potentially including an analysis of the task distribution's properties that would make a committee more effective, would significantly strengthen the paper's core argument.

2. A big limitation that was not discussed throughout the paper, both in the theoretical and empirical parts, is the assumption of access to the parametric space of tasks and the mapping from that space to the space of MDPs. The access to the parametric space is needed to perform the clustering itself, and the access to the mapping is needed in the theory part in order to map between the covering parameters to MDPs to learn the policies, which in turn will consist of the committee. Both of these assumptions are substantial, especially the latter, and require a more thorough discussion. The authors should elaborate on the implications of these assumptions and explore potential methods to relax them. For instance, the authors could investigate the use of learned parametric representations, as done in previous works [2, 3], to address scenarios where explicit task parameters or mapping functions are unavailable. The “naive” Greedy Elimination Algorithm has the advantage of not requiring access to the mapping function, a point that should be explicitly highlighted.

3. Some of the settings in the theoretical part did not match the ones in the empirical study. The main difference (which was not discussed) is that in the empirical study the authors suggested that each policy in the committee will be trained on *all* tasks in the respective cluster, whereas in the theoretical analysis, the authors assumed each policy is the optimal one for a specific task. This modification is important as in some tasks (e.g. pick and place), the Lipshitz assumption in Lemma 1 will not hold, and without the modification, I would expect the method to fail. Theoretical guarantees for the settings in the empirical part, possibly through an analysis of the impact of training on multiple tasks within a cluster, would strengthen the paper's theoretical foundation.

4. I found certain sections of the paper somewhat unclear, particularly the Greedy Intersection Algorithm and the latter part of Section 3.3. Further, while the theory is well formulated overall, the readability could be improved if the authors provided motivation before introducing key definitions and lemmas. Additionally, unifying the notation for meta-RL and multi-task RL (i.e., $\Gamma$ and $T$) as the latter representing a discrete case of the former, can help readability.

5. The empirical study can be extended to support some of the claims in the paper better. For example:
    a. One of the main practical algorithmic novelties in the paper is the task clustering algorithm. The only ablation on this is the result in Figure 2(a), which shows a marginal improvement over KMeans. A further investigation with more clustering algorithms (e.g., Gaussian Mixture Models, DBSCAN) and ablation over the design choices of the clustering algorithm (e.g., the impact of the distance metric, the number of clusters) can improve the soundness of the proposed method.
    b. The authors used popular meta-rl baselines, but more recent baselines are missing, e.g [1, 2, 3].
    c. To make a fair comparison to VariBAD/MOORE the authors should’ve compared the total number of parameters in the policy committee and the baseline. Adding a baseline with the same number of parameters or a policy committee where the tasks are randomly split between the committee can make the claims stronger.

### Questions
1. Typos:

    a. Line 155 - to to -> to

    b. Line 143 - denote an optimal policy -> denote the value of an optimal policy

    c. Line 215 - task $\pi_i$ -> task $\tau_i$

    d. Line 516 - Figure 5.3(a) -> Figure 2(a) 

2. The first two plots Figure 1 seem wrong, they don’t fit the claims made in the paper, as it seems that the new algorithm doesn’t perform better than the baselines. 

3. Did you choose $\epsilon$ and $K$ by trying different values and picking the best one? Should the distribution of tasks affect these values, and if so how?

4. Is there a reason not to increase $K$? I would expect better and better results as $K$ increases. 

5. In the encoding of the Meta World tasks using the language model, did you also use the goal location in the task description?

6. In the Meta World experiment, what were the results of your clustering algorithm? Was there any semantic meaning for the clustering? 

7. Did you tune the hyperparameters for the in-cluster policies or did you use the same hyperparameters as VariBAD/MOORE?

8. In VariBAD they reported higher results on HalfCheetah, is it a different environment? 

9. How many seeds did you use in your empirical studies? 

10. In Section 5.3 you show the results of PACMAN with K=1 but the results are very different than VariBAD/MOORE. Isn’t PACMAN with K=1 identical to the original algorithms? 

11. Why did you choose to train in the Mujoco baseline for just 1.2e7 steps? In VariBAD for example it seems they trained for much longer.

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
This paper studies multi-task reinforcement learning and few-shot learning. 

For multi-task learning, authors consider learning a set of policies called a policy committee to handle multiple tasks. For the case of identical transition dynamics and different rewards across tasks, the authors further provide theoretical results to show they can find good coverage for the parametric model and thus good coverage for all optimal policies. For more general different transition dynamics cases, the authors show some empirical results.

For few-shot learning, the authors provide some sample complexity bound with certain assumptions.

### Strengths
(1) The authors carefully consider different scenarios for multi-task learning (low-dimensional or high-dimensional, parametric or non-parametric), and provide the algorithms accordingly (some with theoretical guarantee, some without).

(2) The authors provide empirical results for cases hard to analyze.

### Weaknesses
(1) In the multi-task case with identical transition kernels and different rewards, the paper does not discuss connections to the reward-free RL framework. For example, the reward-free algorithm [1] can be used to learn the transition kernel, and there are follow-up works on multi-task setting [2,3]. It would be valuable to compare the theoretical results with those from this line of work, especially regarding assumptions about the action space and linearity. Specifically, how do the sample complexity bounds and the dependence on the number of policies compare when considering finite versus continuous action spaces, and under what conditions might one approach be preferred over the other?

(2) In the section on Gradient-Based Coverage, the cluster representation appears to be restricted to tasks within the set $T$. This is a departure from the approach used in the Greedy Intersection algorithm. Theorem 5 also seems to only hold under this restriction. This raises concerns about the potential for a larger error gap between the cluster representation and a given task when using Gradient-Based Coverage compared to the Greedy Intersection algorithm. A more detailed explanation of why this restriction is imposed in the Gradient-Based Coverage approach and a discussion of its implications for the algorithm's performance would be helpful. It seems counterintuitive to limit the search space in this way, and it's not immediately clear why this would be a reasonable choice.

### Questions
Please see above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper built a meta-reinforcement learning framework that learns a set of policies such that at least one is near-optimal for most tasks that may be encountered. The solution is training a set of meta-models to achieve this goal.

### Strengths
The paper targets to address a big issue of meta-RL and multi-task RL, the trade-off between optimality and generalization when the tasks in the task distribution are diverse. 

The literature review is complete and thoughtful.

The proposed method is justified and motivated by the theoretical results.

### Weaknesses
It is still unclear to me how the proposed method addresses the issue. In the context-based meta-RL method, the context of diverse tasks is learned, which can target different patterns for diverse tasks. What is the advantage of the proposed methods? Specifically, how does the proposed method improve upon the ability of context-based methods to handle diverse tasks, given that the context-based methods already learn task-specific patterns during training? The paper mentions a trade-off between optimality and generalization, but it doesn't clearly articulate how the proposed method achieves a better balance compared to existing context-based approaches.

In the experiment, It is unfair to use the parametric task representation for the proposed method as the baselines of meta-RL do not use the information. The paper should provide a more thorough justification for this design choice. It is important to clarify whether the baselines could potentially benefit from using this information and, if so, how the comparison would be affected.



### Questions
Can the proposed method deal with the scenario without any parametric information about the tasks? If the tasks' parameter can be obtained, can we directly train a general policy conditional on the parameter that can deal with all tasks in the distribution?

How the proposed method can achieve zero-shot generalization for the new tasks? When a new task is given, how to figure out the task-specific policy from the candidates? 

In the experiment, do the few-shot adaptations in all baselines require the same sample number?

### Soundness
3

### Presentation
2

### Contribution
2
