# Closing the Gap between TD Learning and Supervised Learning - A Generalisation Point of View.

- Decision: Accept
- Scores: 6, 5, 5, 6

## Abstract
Some reinforcement learning (RL) algorithms can \textit{stitch} pieces of experience to solve a task never seen before during training. This oft-sought property is one of the few ways in which RL methods based on dynamic-programming differ from RL methods based on supervised-learning (SL). Yet, certain RL methods based on off-the-shelf SL algorithms achieve excellent results without an explicit mechanism for stitching; it remains unclear whether those methods forgo this important stitching property. This paper studies this question for the problems of achieving a target goal state and achieving a target return value. Our main result is to show that the stitching property corresponds to a form of combinatorial generalization: after training on a distribution of (state, goal) pairs, one would like to evaluate on (state, goal) pairs not seen together in the training data. Our analysis shows that this sort of generalization is different from \textit{i.i.d.} generalization. This connection between stitching and generalisation reveals why we should not expect SL-based RL methods to perform stitching, even in the limit of large datasets and models. Based on this analysis, we construct new datasets to explicitly test for this property, revealing that SL-based methods lack this stitching property and hence fail to perform combinatorial generalization. Nonetheless, the connection between stitching and combinatorial generalisation also suggests a simple remedy for improving generalisation in SL: data augmentation. We propose a \emph{temporal} data augmentation and demonstrate that adding it to SL-based methods enables them to successfully complete tasks not seen together during training.
\looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
First, the paper identifies one important capability present in dynamic programming but lacking in supervised learning approaches to RL: the stitching property, which generalizes between different trajectories. - The second conceptual leap connects the stitching property to a certain kind of generalization. Finally, the authors propose to outfit data augmentation from supervised learning for reinforcement learning as a simple method to improve generalization. Experiments on two enviornments show that RvS with state and goal augmentation improve over RvS and DT. It is also claimed that more data did not help the DT improve, nor did increasing the number of layers.

### Strengths
- The theoretical foundation developed in this paper is interesting. There is high value in formalizing stitching, and hypothesizing on fundamental limits of certain algorithmic approaches that apply supervised learning to reinforcement learning problems. I also like the ethos of the approach, bringing data augmentation to RL for a specific purpose

### Weaknesses
 - Some of the theoretical arguments fail to convince. I think there are a few details that seem inconsistent throughout the paper, such as the fact that data is not the fundamental limitation vs popular datasets not evaluating stitching because they include most (s,g) pairs.
- The experimental evaluation seems limited overall, and somewhat preliminary. I usually do not put much weight on this kind of weakness, but I also am not comfortable with the theoretical positioning of the paper. Hence, I must put more weight on the experiments in my decision for this paper.

### Questions
- Section 1 (Stitching as goal-state pairs): My understanding of the stitching property is that it is more general: given two partially disjoint trajectories that partially optimal, stitching via dynamic programming can combine the two partially optimal trajectories towards an optimal trajectory. Is your definition equivalent, is it a generalization or is it specific to the goal-directed setting?
- Section 1 (Limited data vs generalization): You state that this is not a problem of limited data, because " there can be (state, goal) pairs that are never visited in the same trajectory, despite being frequented in separate trajectories." In a way this is a source of limited data, if the "data" is a trajectory rather than an experience tuple. I think this is implicit in your argument, but it can be made explicit for clarity.
- Section 4: (More formal "Limited data vs generalization"): I am still not sure how this is different from iid generalization, or how the lemma 4.1 makes this point. My understanding of lemma 4.1 is that there exists a context distribution for which the distribution of states induced by a collection of policies will never be equal to the BC policy. But this is because the policies collecting the data are conditioned on information not available to the BC policy. This induces something like partial observability, which is the source of the problem. Without the context, I do not think this would hold and thus stitching generaliation would be equivalent to iid generalzation. But the problem is, in a sense, limited data: the context is never accessible and hence the data (or information) is fundamentally limited.
- Section 4 (stitching is not finding an optimal policy): I agree that stitching can help find an optimal policy, but this is besides the point in the context of your setting (offline RL). The question is two-fold, under what conditions: 1) can stitching help find a better policy and 2) does fidning a better policy necessitate stitching.
- Section 5 (Nearby states) : how important is it that the states are mapped exactly onto the states in the set of experience? For example, you could imagine adding noise to all states and goals, which would therefore naturally stitch several nearby trajectories. Given the fact that you are assuming the space to have a distance metric, it is probably well-behaved so that this is effective.
- Section 5 (conditions for evaluating stitching): While the first condition is easy to engineer into the problem, the second condition seems problematic. How can you know whether the BC policy has a non-zero probability besides running the experiment?
- Section 6 (DT + aug?): One interesting approach that is missing is combining DT with data augmentation, seeing as DT is more performant than RvS. Is there any reason why this was left out? Is it computational concerns or a more fundamental limitation.
- Section 6 (More data): This seems at odds with condition 1 under "popular datasets do not evalute stitching". Surely, if every state and goal pair were included in the dataset, then DT would improve?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper explores the differences between dynamic programming-based reinforcement learning (RL) and supervised learning (SL)-based RL. A key property of the former is "stitching" past experiences to address new tasks. The study relates this ability to a unique form of generalization. Through experiments, the authors reveal that SL-based RL methods might lack this stitching capability. To address this, they introduce temporal data augmentation, enabling SL-based RL to handle unseen (state, goal) pairs effectively.

### Strengths
1. The paper provides a comprehensive analysis of the differences between dynamic programming-based RL and SL-based RL through the lens of generalization, offering insights into their inherent properties.
2. A novel augmentation method is proposed to make SL more generalizable.

### Weaknesses
1. The proposed stitching generalization describes how "far away" different goals are in the sense of transitions, and the proposed method relies on a heuristic to describe that. This is basically what we aim to learn in TD learning and in most cases we cannot just get this kind of information for free. See Q1.
2. The experiments are limited to Antmaze where the proposed clustering would probably work with raw state inputs, but if we imagine pixel inputs, it would be very hard to find some heuristic to make it work, as mentioned in 1.
3. Missing baselines: Contrastive-based learning is also studied for goal-reaching problems as one kind of supervised learning problem, and it might also learn some representation more useful than the baseline included in the paper.

### Questions
Q1: The optimal augmentation would be some metric that describes "how "far away" different states are in the sense of transitions" almost perfectly. Then such a metric will basically provide us with the optimal value function. In this sense, getting such a metric could be as hard as solving it with TD, so why does the proposed method necessarily "close the gap" between TD and SL?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work analyzes SL-based RL approaches for (goal-conditioned) offline RL, where data are collected using various policies and one hopes to "stitch" existing experience/trajectories to generalize to unseen (start, goal) pairs. It shows that common outcome conditional behavioral cloning (OCBC) methods can fail this task and shows a lemma (Lemma 4.1) that learning from training experience with different contexts may not lead to generalization (in terms of the mixed behavior policy). Then the paper proposes to use temporal augmentation that essentially stitches two trajectories together to have better coverage for the (start, goal) pair. Experiments show that the augmentation can be effective for some offline RL tasks.

### Strengths
- Studies an important problem of generalization from offline data
- Shows a counterexample of the training and test discrepancy (Lemma 4.1)
- Clear writing in most places

### Weaknesses
1. Some key concepts and results are not clearly explained.

    1.1. The core concept, "stitch property", is poorly introduced and readers have to refer to the reference to know what it means. There is no consistent nor clear definition for this "stitch property", making it difficult to understand what the paper is trying to achieve. The paper vaguely alludes to stitching as a property of TD learning, but does not provide a rigorous definition of what constitutes this property, nor how it relates to the specific problem of goal-conditioned offline RL. This lack of a precise definition makes it difficult to assess the validity of the proposed approach.

    1.2. "Our paper focuses on the problem of stitching generalization, not finding optimal policies; however, stitching generalization should be a necessary component for finding optimal policies." Proof needed. The claim that stitching generalization is necessary for finding optimal policies is asserted without any formal justification. This connection needs to be either proven or at least supported with a more detailed argument. Without such justification, the importance of the proposed stitching generalization is diminished.

2. The proposed heuristic of using clustering to stitch close states together lacks theoretical guarantees. What distance metric is suitable here? In the RL context, similar states do not mean they have similar outcomes. For example, two states can be close to each other in Euclidean norm but blocked by a wall and thus not reachable; or two states can be far apart (e.g., top and bottom of a cliff) but one can easily reach the bottom by falling but not the other way around. The paper uses k-means clustering with Euclidean distance, which is not well-suited for the underlying structure of RL state spaces. The paper does not address how the choice of distance metric impacts the quality of the stitched trajectories, nor does it provide any theoretical justification for its use. The lack of a principled approach to state similarity is a significant weakness.

3. For the experiment, the paragraph on "Does more data remove the need for augmentation" is not very surprising given the construction of the dataset. In SL, the fact that more data helps generalization is based on the IID assumption, which does not hold in the current setting since the (state, goal) pairs are not seen during training (also Lemma 4.1). The paper's argument that more data does not remove the need for augmentation is not surprising, given the non-IID nature of the data. The experiments do not provide any new insights beyond what is already known about the limitations of standard supervised learning in non-IID settings. The experimental setup does not adequately demonstrate the value of the proposed augmentation technique.

Minor
- $p_+^{\beta_h}(s,a)$ in Eq.(7) is undefined.
- Both generalization and generalisation are used.
- point-maze large taks -> task

### Questions
Q1: Any suggestions for a reasonable distance metric for the states? 

Q2: Are there any theoretical justification for the temporal augmentation?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
* This work discusses a form of generalization in reinforcement learning (RL) called "stitching generalization." According to the paper, the stitching generalization cannot be achieved with existing supervised-learning (SL) based RL algorithms because it is fundamentally different from the generalization on independent & identically distributed (i.i.d.) dataset. This is explained via a concrete example of an MDP depicted in Figure 1.
* Also, this work propose "temporal data augmentation" technique for goal-conditioned RL to actually implement stitching generalization inside the SL-based RL algorithms. This technique is based on careful sampling of augmented goal, which is determined by *closeness" of states based on a clustering algorithm.
* Moreover, this work provides a novel benchmark to evaluate the stitching capability of RL algorithm.
* Lastly, this work empirically show the efficacy of the temporal data augmentation + outcome conditional behavior cloning (OCBC) algorithms on their own benchmark.

### Strengths
* The motivation is clear and the main message is well presented. I enjoyed reading the paper.
* Their main method of data augmentation is novel and intuitive.
* The empirical results are promising, even after making the task more difficult to generalize.
* Lastly, the limitations of their work is clearly mentioned. I also look forward to scalable version of their algorithm.

### Weaknesses
 * **Theoretical contribution is a bit marginal.**
  - The authors claim that they “provide a theoretical framework for studying stitching.” They indeed provided a formal definition of stitching generalization in Definition 1. However, it is not actually used anywhere. If it is not applicable to deduce any theoretical guarantee, what is the purpose of proposing such definition? At least for the counterexample proposed in Lemma 4.1 and depicted in Figure 1, the authors should be able to provide any kinds of implications on the (lower bound of) stitching generalization. This will definitely strengthen the theoretical contribution of the paper. If it is not possible, please kindly explain the reason/context.
* **Isn’t it a problem of trajectory-based sampling rather than transition-based sampling that it is impossible to implement stitching with SL-based methods?**
  - At first glance, I thought that the statement “stitching generalization is not the same as i.i.d. generalization” is not quite the problem of supervised learning itself. Let’s take a look at the counterexample in Figure 1. If we break down the trajectories collected by policies $\beta_{h=1}$ and $\beta_{h=2}$ into transitions, can’t even a supervised method learn something from a virtual trajectory, say, 2-3-4, which was not exactly in the dataset, by only i.i.d. sampling the transitions? To rephrase my question, can’t a SL-based method learn stitched behaviors by transition-based sampling or so-called *bootstrapping*? I don’t think this would be exactly the same as the proposed temporal augmentation method. Please correct me if I’m wrong.
* **Weakness on Algorithm 1 (OCBC + Temporal Data Augmentation) regarding additional hyperparameter**
  - It uses clustering algorithm, so it has an additional hyperparameter, $k$ for k-means algorithm. To the best of my knowledge, the main paper does not discuss on the effect of the choice of such hyperparameter, which might be difficult to properly tune.
* **It seems necessary to conduct additional Experiments on DT + temporal augmentation.**
  - Although the paper empirically proves that it can enhance the data utilization of *RvS* algorithm with their proposed augmentation technique, it does not provide any results on ‘’DT + temporal augmentation’’ combination. This experiment will strengthen the empirical contribution of the paper. If it is not applicable, please kindly explain why.
* **There seems to be some minor typos.**
  - pg 1. Kaelbling (1993) $\rightarrow$ (Kaelbling, 1993)
  - pg 3., Equation (1). $\mathbb{E}_{s\sim p_0(s_0)} [p_t^{\pi}(s_{t+} =g \mid s_0=s)]$ $\rightarrow$  $\mathbb{E}_{s\sim p_0(s_0)}[p_+^{\pi}(s_{t+} =g \mid s_0=s)]$
  - pg 3. “… and then sampling a trajectory from the corresponding policy $\{\beta(a\mid s, h)\}$.” $\rightarrow$ $\beta(a\mid s, h)$

### Questions
* In Definition 1, does the performance function $f$ have any relavance to the objective $J$ defined in Equation (3) or the maximum likelihood objective defined in Equation (6) and (7)?
* In page 5, what does it mean by ‘combinatorial generalization’? Do you have a definition or any reference for that?
* Just curious: regarding Lemma 4.1, do you have any comments or implications on the (sort of) bias term $\E_{p(h)} \left[ p^{\beta_h}_+ (s_{t+} \mid s) p^{\beta_h}_+ (s) \right] - p^{\beta}_+ (s_{t+} \mid s) p^{\beta}_+ (s)$ ?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
