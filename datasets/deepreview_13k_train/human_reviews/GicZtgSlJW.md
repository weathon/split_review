# Primal-Dual Continual Learning: Stability and Plasticity through Lagrange Multipliers

- Decision: Reject
- Scores: 3, 3, 6, 8

## Abstract
Continual learning is inherently a constrained learning problem. The goal is to learn a predictor under a no-forgetting requirement. Although several prior studies formulate it as such, they do not solve the constrained optimization problem explicitly. In this work, we show that it is both possible and beneficial to undertake the constrained optimization problem directly. To do this, we leverage recent results in constrained learning through Lagrangian duality. We focus on memory-based methods, where a small subset of samples from previous tasks can be stored in a replay buffer. In this setting, we analyze two versions of the continual learning problem: a coarse approach with constraints at the task level and a fine approach with constraints at the sample level. We show that dual variables indicate the sensitivity of the optimal value with respect to constraint perturbations. We then leverage this result to partition the buffer in the coarse approach, allocating more resources to harder tasks, and to populate the buffer in the fine approach, including only impactful samples. We derive sub-optimality bounds, and empirically corroborate our theoretical results in various continual learning benchmarks. We also discuss the limitations of these methods with respect to the amount of memory available and the number of constraints involved in the optimization problem.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a theoretical analysis of memory-based continual learning based on the recent advances in constrained optimization.

In terms of constrained optimization, preventing forgetting previously learned tasks becomes the constraint of the optimization problem, and the emprical risk with finite samples should be bounded by the forgetting tolerance as the constraints.

Motivated by the theoretical result of the constrained learning through Lagrangian duality (Chamon et. al. 2020), the authors provide a theoretical plausible Lagrange multiplier $\lambda_k$ and the buffer size $n_k$  for each task $k.$

In the experiment, the paper provides some toy benchmark results, such as seq-MNIST with several memory-based baselines.

### Strengths
In the research of continual learning, there is few optimization-based analysis to mitigate catastrophic forgetting.

This paper provides a new theoy-based algorithm from scratch, which helps to understand which Lagrange multiplier  and buffer size are used totrain the neural networks for continual learning.

### Weaknesses
Despite the theoretical result, the proposed algorithm does not fit the online continual learning scenario because the process "fill buffer" is done after visiting samples in line 11 of Algorithm 1.

This implies that the buffer should keep all encountered data points during $n_{iter}$ iterations, and then the buffer drops some samples to satisfy the buffer size condition, which has already been violated in lines 5-10 in Algorithm 1.

It seems that this contradiction occurs because Algorithm 1 needs to access the information of $\lambda_k$ at the end of each task to compute the optimal buffer size. However, we should have at least the upper bound of the buffer size for the current task $k$ to save encountering samples in the online stream.

In addition, the loss landscape on the parameter $\theta$ is non-convex, as the authors stated in Section 3. The local-optimal setting for a given local minimal point and the Lagrange multiplier do not guarantee remarkable performance in the empirical result. The existing heuristic methods based on constrained optimization, such as A-GEM, have already shown remarkable performance in more complex benchmarks, such as split-CIFAR100 and split-MiniImagenet.

Considering the recent advances in continual learning, I think that a new constrained optimization-based CL algorithm should be either theoretically solid or empirically outstanding.

Furthermore, the algorithm's description regarding buffer updates is unclear, specifically how data from the current task $t$ is stored in $B_t^t$ within Algorithm 1. The inner loop iterates $n_{iter}$ times, potentially allowing multiple epochs on task $t$. After this loop, the algorithm selects samples for storage based on the partition rule in line 11. This raises concerns: first, multi-epoch learning is not standard in continual learning, even within a single task. Second, the algorithm cannot access streamed data after line 9, as the allowed memory size is smaller than the dataset $D_t$. Thus, building the buffer at $t$ in line 11 is problematic. The authors should collect data points during the inner loop, respecting memory limits, and then compute buffer partitions with a modified rule. The current description of the algorithm is misleading and needs correction.

Finally, there is a critical mismatch in the experimental setup. The baselines, GSS and Reservoir sampling, are designed for online continual learning, but the experiments are conducted in a multi-epoch setting (Section A.7). This makes the comparison with baselines unfair.

### Questions
1. The reported metric is not standard in continual learning. Can the authors report the experiemntal result in terms of the average test accuracy and FWT?
2. I think the constrained optimizaiton based CL baselines, such as GEM and A-GEM should be included in the experiemt section to analyze the novelty of the proposed method. Is there any reason why the authors does not contain these algorithms?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work directly leverages the constrained optimization framework to solve a continual learning problem. 
Based on the renowned sensitivity analysis with Lagrangian dual variables, this work tackles the continual learning problem in two different aspects, at the level of tasks and data. 
* At the task level, the Primal-Dual Continual Learning (PDCL) algorithm allocates more datapoints to task that is sensitive to constraint perturbation (i.e. large per-task dual variable)
* At the data level, their indirect sample selection algorithm prefers to choose datapoints that are sensitive to constraint perturbation (i.e. large per-datum dual variables)

### Strengths
* The authors carefully motivate the readers to understand Lagrangian sensitivity analysis and its application in the context of continual learning. 
* Their experiments show that the idea of Lagrangian sensitivity analysis can be effectively applied to both buffer allocation and data selection for memory-based continual learning.

### Weaknesses
* **Regarding theoretical contributions**
  - In abstract, it is claimed that there are sub-optimality bounds. At first glance, I was expecting learnability guarantee (e.g., PAC) for the actual continual learning problem. However, it turns out that the sub-optimality bound was for estimation of dual variables. Since the estimation of dual variables is the main spirit of the proposed algorithm, I don’t want to say this is not an enough contribution. Rather, I would say the expression ‘sub-optimality bound’ is quite misleading in some sense.
  - The paper defers the discussion on the *strong* concavity constant $c$ to Appendix A.5. However, I think this hides several important dependencies. For example,
    1. It intrinsically assumes the usage of (might be a large amount of) weight decay to induce strong concavity of the objective function;
    2. The loss function should be $G$-smooth, and the sub-optimality bound in Theorem 4.2 turns out to depend quadratically on $G$. This dependency needs to be explicitly stated and discussed in the main text, as it significantly impacts the tightness of the bound.
    3. The constraint Jacobian (question: what is it exactly?) must be full rank, and the sub-optimality bound depends quadratically on the inverse of the minimum singular value of this matrix, which can be arbitrarily large. This assumption of a full-rank constraint Jacobian is quite strong and may not hold in many practical scenarios. The paper needs to elaborate on the implications of this assumption and provide a more precise definition of the constraint Jacobian.

    For these, I think the paper should be more clear and honest on several hidden dependencies.
  - The last paragraph of Section 4 claims that the weakness of the sub-optimality bound “can be fixed by replacing the minimum with the average sample complexity”, but I cannot find any detailed discussion on this, throughout the paper. This claim needs to be substantiated with either a proof sketch or a reference to relevant literature.
  - Although the proof would be similar to that of Theorem 3.2, I think the full proof of Proposition 5.1 should be added, or at least a set of necessary modifications in the proof to prove the proposition must be added.
* **Regarding Theorem 3.2 and the notation “$\partial P^{\star}_t (\epsilon_k)$”**
  - Is $P^{\star}_t (\cdot)$ a convex function? I think this should be clarified in order to use the notion of sub-differential.
  - Also, I think the notation is quite confusing. I would like to suggest the notation like “$\partial_{\epsilon_k} P^{\star}_t (\epsilon)$” where $\epsilon = (\epsilon_1, …, \epsilon_t)$. 
  - In a higher level of discussion, does the paper ever require such a **local** sensitivity result to give a motivation? The paper motivates the use of dual variables for buffer allocation and data selection, but it's not entirely clear why this *local* sensitivity analysis is necessary. A more explicit connection between the local sensitivity and the overall continual learning strategy would strengthen the motivation.
* **There are several but minor typos and misleading usages of symbols:**
  - Equation $(P_t)$: I think this should be $\min_{f\in\mathcal{F}}$, not $\arg\min_{f\in\mathcal{F}}$. This also applies to the equation at the beginning of Appendix A.2.
  - In Assumption 2.1, $\delta$ is used for task similarity. Throughout Section 4, however, $\delta$ is used as a probability parameter.
  - Assumption 2.4: “There exists $R, M >0$ such that …”
  - Page 3, below Equation $(1)$: “… two-player gamer …” $\rightarrow$ “… two-player game …”
  - Equation $(3)$: Why do we need an inner product between two scalars $-\lambda_k^\star$ and $\gamma$? I don’t think this is necessary.
  - Proposition 4.1: The order 2.3 and 2.2 must be flipped.
  - Theorem 4.2: “$\|\lambda’\|_1 = \max\{\|\lambda_p^\star\|, \|\hat{\lambda}_p^\star\|\}$” $\rightarrow$ Are all the norms $\ell_1$-norms?
  - Page 7, below Equation $(6)$: “$\mathfrak{B}_t(x,y) \ne D_t(x,y)$” $\rightarrow$ “$\mathfrak{B}_t(x,y) \ne \mathfrak{D}_t(x,y)$”
  - Section 6: there are some inconsistencies of using the word “Tiny-ImageNet”, which should be fixed throughout the section.
  - Appendix A.2, page 15, the equation starts with $L(f,\lambda;\epsilon)$: What is $z$ at the end of the equation? I think it should be removed.
  - Appendix A.5: the letter $\ell$ is both loss function and the minimum singular value of the constraint Jacobian matrix. 
* **Minor comments**
  - Around Assumption 2.3, it would be great if the authors put some citations on universal approximation results for neural networks, which explains (with examples) the richness of (modern) machine learning model parametrization.
  - Below Equation $(1)$: “… the forgetting tolerances $\{\epsilon_k\}$ need to …” $\rightarrow$ “… the forgetting tolerances $\{\epsilon_k\}$ *suffice* to …”
  - Page 4: This sentence is quite weird: “… it is sensible to partition the buffer across different tasks as an increasing function of $\mathbf{\lambda}^\star$...”, because it says we can say that a function is increasing in terms of a vector variable.

Overall, I believe the writing could be much more improved than the current draft.

### Questions
Please see **Weaknesses**.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper views continual learning as a constrained learning problem: to learn the new task without forgetting the old tasks (too much). Some previous work took this perspective as well, but in those cases this way of formulating the continual learning problem only motivated the proposed approach. In this paper, the authors directly address continual learning as a constrained learning problem by making use of recent advances in Lagrangian duality as tool address constrained optimization. In particular, the paper demonstrates that by adopting such a primal-dual method, a principled approach emerges for deciding how to fill the memory buffer.

### Strengths
As far as I am aware, this is the first work that directly addresses continual learning as a constrained learning problem. The paper proposes a principled framework for this by means of optimizing the Langrangian empirical dual, and it provides clear theoretical justification for its propositions.

A neat theoretical demonstration of the paper is showing that the Lagrangian dual variables can be interpreted as signaling the difficulty of their corresponding task.

The paper then demonstrates that the Lagrangian dual variables can be used to select which samples to store in the memory buffer, and that empirical benefits can be obtained by doing so.

### Weaknesses
Although I think this paper already makes some important and neat contributions, to realize its full potential, I think it is important to improve and clarify the empirical comparisons.

**Indirectness of empirical comparisons**

In my opinion, from a practical perspective, this paper proposes three “novel aspects” compared to the standard experience replay approach that is commonly used in continual learning:

{1} the weighing of the replayed losses relative to the loss on the current task is determined by the Lagrangian dual variables (rather than, as is currently done in continual learning, either by a hyperparameter or as a function of how many tasks have been seen so far)

{2} the selection of samples to be stored in the buffer at the task level (buffer partition)

{3} the selection of samples to be stored in the buffer at the sample level

However, it seems only the impact of the last two aspects are evaluated empirically. Why do the authors not include a direct comparison to assess the effect of {1}? (That is, a comparison between "standard ER" and the approach proposed by this paper except without buffer partition at task level or individual sample selection.) I think doing so could substantially strengthen this paper. Moreover, it is not clear to me whether the comparisons to assess the effect of {2} are direct. For example, in Figure 1 (but a similar question applies to Figure 4), when “PDCL” is compared with “Reservoir”, it is not clear how the replayed losses are weighed in the case of “Reservoir”. Are they weighed in the same way as in “PDCL”? Or are they weighed in another way? This should be clearly described. If it is the second option, then I do not think that Figure 1 provides a comparison that “isolates the effect of buffer partition”.

**Distinction task- versus class-incremental learning**

The way the paper describes the difference between task- and class-incremental learning suggests that the authors *train* their models in these two scenarios in the same way, and that there is only a difference between these scenarios in the way the models are *evaluated* at test time. Is this indeed the way the authors implemented their experiments? Because to me it seems there should also be a difference in how models are trained in task-incremental versus class-incremental learning. For example, when training on samples from the second task, with task-incremental learning the models only need to be trained on distinguishing between classes from the current task, while with class-incremental learning the models should also learn that those current samples do not belong to classes from the first task. To clarify this, the authors should provide more details regarding how they implemented the difference between task- and class-incremental learning. When discussing the distinction between task- and class-incremental learning, I think it is also important to cite the original paper (van de Ven et al., 2022; https://www.nature.com/articles/s42256-022-00568-3).

**Minor issues:**
- top of p9: a reference is made to Figure 9, but I think Figure 4 might be meant?
- in the reference list, the paper Buzzega et al. (2020) is included twice
- for a number of papers in the reference list, no venue is included (e.g., Gentile et al., 2022; but there are several others as well)
- there are several formatting issues with in-text citations in the Appendix
- on p19, Task Incremental Learning is abbreviated as CIL

### Questions
Although I think this paper already makes some important and neat contributions, to realize its full potential, I think the authors should [1] include empirical comparisons that more directly assess the impact of the three different novel aspects that the authors propose, and [2] provide more details regarding the difference between the task- and class-incremental learning experiments.

Please see under “Weaknesses” for details on both.

While I think it is already a paper that could be accepted, if these two issues can be satisfactorily addressed, I think it could be a strong or very strong paper.

I would be happy to actively engage in the discussion period.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper formulates the no-forgetting objective of Continual-Learning (CL) as a constrained optimization problem w.r.t the population risks. Given the forgetting tolerance $\epsilon_{1:T}$, it focuses on two important aspects of the memory-based methods: 1. how to partition the memory buffer for different tasks. 2. For each task, which subsamples should be stored? The first point is addressed by deciding the sample size of each task through minimizing the generalization gap weighted by the optimal dual variables of the CL objective. The second is to select the samples with the highest associated per-sample dual variable from each task.

### Strengths
1. The paper is well-written and the motivation is clear.
2. Relating the generalization gap with the dual variables to obtain the optimal memory partition in CL is novel to me. 
3. Experimental results validate the effectiveness of the proposed method compared to previous memory-based approaches.

### Weaknesses
My primary concerns lie in the following aspects:
  * The convergence of $\mathbf{\lambda}$ is highly sensitive to the setting of the forgetting tolerance $\epsilon$, the number of tasks $T$, and the hardness of the tasks, which will affect the memory partition. Specifically, the paper does not provide a clear analysis of how the optimal dual variables $\lambda$ are affected by the choice of $\epsilon$ for each task, or how this sensitivity impacts the final performance. A small change in $\epsilon$ could lead to a very different memory allocation, and the paper does not fully explore the stability of this allocation. Furthermore, the hardness of tasks is not well-defined, and the practical implications of this sensitivity are not rigorously investigated. For instance, a task with a very small $\epsilon$ might not be allocated enough memory, leading to catastrophic forgetting.
  *  At every timestep, the memory partition changes. Not just the problem mentioned in the discussion exists, where the optimal partition size of a previous task grows at the current timestep. For the tasks that have a smaller size at the current timestep, it needs to reselect the samples to store, which would cause additional computation costs. This reselection process is not clearly defined, and the computational cost of re-evaluating the dual variables and re-selecting samples at each step could be significant, especially for large datasets. The paper does not provide a detailed analysis of the computational overhead associated with this dynamic memory allocation, nor does it discuss potential approximations or optimizations to mitigate this cost. The constant re-evaluation of the dual variables for each sample may not be computationally feasible for real-time applications.
  * The growing and large number of constraints. The paper doesn't thoroughly address the scalability of the proposed method with respect to the number of tasks and the size of the datasets. While the experiments show results on Tiny-ImageNet, it's unclear how the performance would scale to larger and more complex datasets. The computational cost of solving the constrained optimization problem with a large number of constraints could become a major bottleneck, and the paper lacks a discussion on potential strategies to address this issue.

### Questions
Please see the previous section.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
