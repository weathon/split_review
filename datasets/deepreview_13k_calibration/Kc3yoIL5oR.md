# Solving Diverse Combinatorial Optimization Problems with a Unified Model

- Decision: Reject
- Avg Score: 5.25
- Scores: 6, 6, 3, 6

## Abstract
Combinatorial Optimization (CO) encompasses a wide range of problems that arise in many real-world scenarios. While significant progress has been made in developing learning-based methods for specialized CO problems, a unified model with a single architecture and parameter set for diverse CO problems remains elusive. Such a model would offer substantial advantages in terms of efficiency and convenience. In this paper, we introduce and formalize a unified model for solving various CO problems. Inspired by the success of next-token prediction, we frame each problem-solving process as a Markov Decision Process (MDP), tokenize the corresponding sequential trajectory data, and train the model using a transformer backbone. To reduce token length in the trajectory data, we propose a CO-prefix design that aggregates static problem features. To address the heterogeneity of state and action tokens within the MDP, we employ a two-stage self-supervised learning approach. In this approach, a dynamic prediction model is first trained and then serves as a pre-trained model for subsequent policy generation. Experiments across nine CO problems demonstrate the generic problem-solving capability of our unified model, highlighting its few-shot and even zero-shot ability to generalize to unseen problems through rapid fine-tuning. We believe our framework offers a valuable complement to existing neural CO methods that focus on optimizing performance for individual problems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper proposes a unified framework for addressing CO problems by modeling them as MDPs and using a two-stage self-supervised learning approach. The authors introduce a CO-prefix design to efficiently handle static information, improving model training. Tested across 9 CO problems, the model shows strong performance, approaching expert solutions and adapting well to unseen tasks with few-shot learning. This work demonstrates the potential of using a unified model to solve diverse CO problems.

### Strengths
1. This paper introduces a novel CO-prefix design that not only significantly reduces token lengths but also efficiently separates static and dynamic features, improving both the efficiency and scalability of the training process.
2. The unified model proposed in this paper demonstrates the capability to solve different CO problems using a single framework, exhibiting robust generalization across diverse problem types. This versatility, including few-shot and zero-shot learning capabilities, highlights the model’s potential for broad application without the need for retraining.
3. The authors conduct comprehensive experiments on 9 different CO problems, providing thorough evaluations that include ablation studies and meaningful comparisons with baseline models.

### Weaknesses
 1. Limited Applicability to Non-Tail-Recursive Problems: Although this paper claims that the proposed method can address all CO problems, its approach is actually limited to problems with the tail recursion property, as noted in lines 239-243. While the paper lacks an explanation on how the approach could be adapted for CO problems without the tail recursion property. This limitation suggests an overstatement of the method’s applicability. Specifically, the current framework relies on a sequential decision-making process inherent in MDP formulations with tail recursion, which may not be suitable for problems requiring a more complex, non-sequential approach. For instance, problems involving hierarchical decision-making or those requiring simultaneous consideration of multiple constraints might not fit within the current framework without significant modifications.
2. CO-Prefix Design Limitations in Dynamic Problems: While the CO-prefix design effectively reduces token lengths, its effectiveness may diminish for dynamic problems, such as online bin packing, which contain minimal static information. This notable limitation, however, is not discussed in the paper. The CO-prefix relies on aggregating static features to improve efficiency, but in fully dynamic problems where the state changes at each step and static features are minimal or absent, the prefix may become redundant. This could lead to the model performing similarly to methods without the prefix, thus negating the benefits of the proposed design for such problems. The paper should address how the model would perform in the absence of static information and whether the two-stage training process alone is sufficient for dynamic problems.
3. Limited Baseline Comparisons: The baselines in this paper are relatively narrow. Including comparisons with neural solver methods specifically designed for tasks such as routing and MIS would provide a clearer view of the performance differences between the approach and specialized methods, helping to underscore the innovations presented in this work. The current comparisons primarily focus on general-purpose models, which do not provide a clear understanding of how the proposed method performs against state-of-the-art solvers tailored for specific CO problems. For example, comparing against methods that use specialized architectures or training techniques for routing problems would be more informative.

### Questions
Pls refer to the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a Transformer-based unified model for solving diverse combinatorial optimization (CO) problems. Inspired by the previous works known as auto-regressive methods for neural combinatorial optimization (NCO), this paper formulates diverse CO problems as a Markov Decision Process (MDP), and generates optimal solutions in a sequential manner. However, unlike the previous works using reinforcement learning (RL) to generate an optimal sequence, this paper basically leverages imitation learning and more focuses on multi-task learning to solve diverse CO problems in a unified model. For multi-task imitation learning for CO, this paper first collects expert trajectories from an expert solver for each domain. Then, it trains a Transformer-based model on the collected expert trajectories by using the next token prediction. For efficient multi-task imitation learning, this paper proposes two methods: (1) CO-prefix and (2) two-stage self-supervised learning. The key idea of CO-prefix is to consolidate static information as a prefix and maintain only dynamic information at each time step. This can reduce the redundency in trajectories. In two-stage self-supervised learning, this paper first learns the dynamics of state transition by predicting the next state, and then learns a policy by predicting an action given an observation. This paper evaluates the proposed model on 9 CO problems including TSP, CVRP, PCTSP, OP, SPCTSP, Knapsack, ATSP, MIS, and FFSP. The experiment results show that the proposed model can provide better scores than GATO/DB1 on 6 CO problems out of the total 9 CO problems.

### Strengths
S1. This paper empirically demonstrates that a Transformer-based model can learn to solve diverse CO problems by experimenting on representative 9 CO problems.

S2. The proposed methods like CO-prefix and two-stage learning (dynamics learning and policy learning) seems simple but effective in multi-task imitation learning.

### Weaknesses
W1. [Method] One of main limitations of this paper is that the proposed method may not address the generalizability that aims to solve unseen CO problems. As mentioned in the Summary section of this review, this paper mainly focuses on imitating expert trajectories generated by an expert solver for each CO problem. The reliance on expert trajectories for each specific problem limits the model's ability to generalize to entirely new problem instances or problem types not seen during training. This is a significant concern, as the true power of a unified model should lie in its ability to handle diverse and unseen combinatorial optimization challenges, rather than just replicating known solutions.

W2. [Method] This paper uses a unified tokenizer that converts discrete and continuous values in trajectories into tokens. However, I am not sure that this quantization is robust to the problem diversity. Different CO problems may have different scales in their values. Therefore, this kind of quantization may result in weak generalizability across different CO problems. The use of a single tokenizer across all problems raises concerns about its ability to effectively capture the nuances of each problem's data distribution. For instance, the tokenization of edge weights in a TSP instance might not be suitable for representing the capacity constraints in a CVRP instance, potentially leading to information loss or misrepresentation.

W3. [Experiments] This paper mainly compares the proposed model with Gato/DB1. However, the performance gain (i.e., the difference to an optimal solution) does not seem significant. According to Table 2, the more important thing seems that the proposed model is very efficient, significantly reducing inference time. The comparison with Gato/DB1, while relevant, does not fully establish the superiority of the proposed approach. The performance gains, especially in terms of solution quality, are not substantial enough to justify the increased complexity of the model. The focus on inference time reduction, while valuable, should not overshadow the primary goal of achieving near-optimal solutions.

W4. [Experiments] Figure 5 (i.e., Performance on diverse problem types) may lead to misunderstanding. The authors did not perform experiments on ATSP, MIS, and FFSP, since Gato/DB1 can not properly process these CO problems. However, readers may think that there is a significant performance gap between Gato/DB1 and the proposed model on these CO problems. The absence of results for ATSP, MIS, and FFSP when comparing against Gato/DB1 creates a misleading impression of the model's performance. The figure should clearly indicate that the comparison is not applicable for these problems, rather than implying a performance gap where no direct comparison was made.

W5. [Experiments] In Section 4.3 (i.e., Performances on Few-shot Ability), this paper provides experiment results on the effect of pre-training. However, the word "few-shot" in the title may lead to misunderstanding. This experiment seems more related to transfer learning rather than few-shot learning. The experiments presented as "few-shot" learning appear to be more aligned with transfer learning, where the model is pre-trained on a set of tasks and then fine-tuned on a new task. The use of the term "few-shot" is misleading, as the experiments do not demonstrate the model's ability to learn from very limited data on a completely new task, which is the core concept of few-shot learning.

### Questions
Q1. CO-prefix is interesting. Could you provide some examples of CO-prefix for each CO problems? Those examples will help reader to understand the proposed model more clearly.

Q2. This paper reports that GATO/DB1 can not properly process some CO problems such as ATSP, MIS, and FFSP. Could you provide more explanation for this?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This manuscript aims to develop a unified model for diverse combinatorial optimization problems, following the next-token-prediction concept. It first tokenizes different COPs with a CO-prefix that includes static features and trajectories. After tokenizing, it proposes a two-stage training paradigm in a self-supervised manner, learning to predict states and actions. Experiments are conducted on nine COPs, including TSP, KP, MIS, FFSP, etc., to evaluate the proposed method's zero-shot and few-shot generalization capabilities.

### Strengths
1. The idea of developing a unified model across diverse CO domains is interesting, which will arouse the interests of the community.
2. Code is provided.

### Weaknesses
1. This manuscript seems to be a very drafted version. For instance, the appendix part isn't finished; the format, figure indices and reference are in a great mess; the abstract is overly lengthy.
2. The improvement of the proposed method over baselines is marginal, and the inference time remains high.
3. There is a lack of baseline learning methods, and the experimental section would benefit from further expansion.
4. The proposed method only applied to the COPs with a very small problem scale (N=20). 
5. The tokenization for different COPs still requires hand-crafted designs and the design seems tricky. 
6. It would be helpful to understand whether the selection of training problems affects the results. Have any experiments been conducted on this? The current problem set heavily features routing problems. It would be better to incorporate other problems.
7. Would be better to add some experiments for different hyper-parameters.
8. Adding examples to illustrate tokenization for different COPs would enhance clarity.

### Questions
See weaknesses.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a unified deep model to solve diverse CO problems. The model is motivated by the success of next-token-prediction in LLMs and is trained using a transformer backbone with tokenized data collected from problem solution trajectories. The main challenges in training such a model are the long token length due to the complex observation space of CO problems and the need to predict both observations and actions simultaneously. The paper introduces two key designs: a CO-prefix to reduce token length by aggregating static features of the problems, and a two-stage self-supervised learning scheme to account for the heterogeneity of state and action tokens within the MDP. The proposed model demonstrates robust problem-solving capabilities across nine diverse CO problems, as well as strong few-shot and zero-shot generalization abilities. This framework is expected to complement existing neural CO methods that focus on achieving optimal performance for individual CO problems.

### Strengths
- This paper addresses an important and intriguing research topic.
- It appears that the performance of this paper surpasses that of Gato.

### Weaknesses
 - Although I have read them several times, I still cannot understand zero-shot and few-shot related parts.
- The method claims to benefit from two-stage training, but I do not understand the significant advantage of "Ours" over "Ours-DR."
- The report metrics include both score and time. Although the proposed method demonstrates a significant advantage in runtime, it does not achieve the best score on some tasks. For ATSP/MIS/FFSP, the baseline is random, making it difficult to assess the performance of the proposed method.

### Questions
For Section 4.3, 
- Should the second subplot in Figure 7 be ATSP? 
- Why does the model have zero-shot capability? Given that the state space and action space are different? The paper mentions, "Since TSP serves as a foundational version of many routing problem variants, our model, pre-trained on the other three problems, can directly generate semi-optimized solutions without any additional data for fine-tuning." I still cannot understand how such a solution could construct by the model.
- Could the definition of "epoch" in the paper be clarified further? Does each epoch use the same data?
- My understanding of "few-shot" typically refers to an extremely small amount of data. If I am not mistaken, each epoch in this paper actually contains many samples. Should this terminology be revised?

- I thought that for CO problems, solvers usually can find a solution based on a time budget. Do the expert method and existing methods involved in this paper have this capability?
- What is the bolding rule for Table 2?

### Soundness
2

### Presentation
3

### Contribution
2
