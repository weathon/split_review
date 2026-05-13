# Mitigating Interference in the Knowledge Continuum through Attention-Guided Incremental Learning

- Decision: Reject
- Scores: 3, 5, 5, 5, 5

## Abstract
Continual learning (CL) remains a significant challenge for deep neural networks, as it is prone to forgetting previously acquired knowledge. Several approaches have been proposed in the literature, such as experience rehearsal, regularization, and parameter isolation, to address this problem. Although almost zero forgetting can be achieved in task-incremental learning, class-incremental learning remains highly challenging due to the problem of inter-task class separation. Limited access to previous task data makes it difficult to discriminate between classes of current and previous tasks. To address this issue, we propose `Attention-Guided Incremental Learning' (AGILE), a novel rehearsal-based CL approach that incorporates compact task attention to effectively reduce interference between tasks. AGILE utilizes lightweight, learnable task projection vectors to transform the latent representations of a shared task attention module toward task distribution. Through extensive empirical evaluation, we show that AGILE significantly improves generalization performance by mitigating task interference and outperforming rehearsal-based approaches in several CL scenarios. Furthermore, AGILE can scale well to a large number of tasks with minimal overhead while remaining well-calibrated with reduced task-recency bias.}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a rehearsal-based method called AGILE to tackle the class-incremental learning setting in continual learning. Specifically, the paper leverages learnable task embedding vectors and shared task-attention module for better mitigating task interference. Experimental results on benchmark datasets demonstrate the effectiveness of the method.

### Strengths
- The paper reads well and is easy to follow.
- Class-incremental learning is indeed a more challenging setting than task-incremental learning.

### Weaknesses
 - The idea of using task-attention or task embedding vector is not quite novel. For example, DyTox [1] also has a task attention module, L2P [2] leverages task-specific prompts. 
- Following the first one, I think the paper misses several recent competitive methods to compare against. For example, I understand both DyTox and L2P are based on transformers. However, if the proposed method AGILE is generalizable enough, it should be compatible with transformer architectures as well, making comparison with more advance methods like DyTox, L2P possible.
- 
- The contents in middle and right subfigures in figure 3 seems missing?

### Questions
- I understand the method is based on rehearsal, what if the rehearsal part is removed. Will the remaining design lead to improvement upon the baselines without rehearsal as well?
- See weaknesses for the rest questions.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a novel rehearsal based continual learning approach which use a shared task-attention module to mitigate the task interference. The shared task-attention module compresses the task specific information to some trainable parameters.

### Strengths
1. The framework achieves fairly good results compared with baselines.
2. The paper is written clearly and easy to follow.

### Weaknesses
1. Novelty concern. I would like to point out that the idea of leveraging trainable parameters to store task information has been investigated in previous works [*] [**]. L2P has shown its effectiveness in continual learning areas in recent years. 

2. Lack of a comprehensive comparison. There are many works using prompting (learnable parameters) in continual learning and achieving SOTA performance. I suggest the author conduct a comprehensive comparison with these works.

### Questions
Could the author conduct a comprehensive comparison with CL works using prompting (learnable parameters)?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a replay-based CL method utilizing a lightweight task attention module. The module receives features from the feature extractor and performs task-id prediction using the projection vectors for each task. This approach aligns with the findings of a prior theoretical study. The authors conduct comprehensive experiments to demonstrate the benefits of their approach compared to existing baselines and show the effectiveness of the proposed techniques.

### Strengths
1. The proposed approach is grounded in a theoretical study.
2. The proposed method outperforms the baselines.

### Weaknesses
1. I feel like the paper is written in a rush. The experiment setup is not mentioned in the main paper. It's not clear how many tasks are used in the sequential data (e.g., Seq-CIFAR100), and what architecture is used. I couldn't find where I can find the information in the main text.
2. It's not clear why the shared task-attention module improves WP and TP when this module itself also suffers from forgetting. Specifically, the mechanism by which the task projection vectors and shared attention module interact to mitigate forgetting is not well-explained. It's unclear how the task-specific latent spaces are maintained over time, and how the shared attention module avoids collapsing into a single representation.
3. I couldn't fully understand why this method is better than the existing task-id prediction methods. [1] also builds a task-id prediction module on top of the feature extractor. A more comprehensive and detailed discussion should be included. The paper needs to clarify how the proposed approach's task-specific latent spaces and projection vectors offer an advantage over simply predicting task IDs and using task-specific heads, especially given that both approaches aim to leverage task information for improved performance.

### Questions
1. How does the model make the final class prediction? Does it first predict the task-id using the attention module and make a within-task prediction?
2. What's the purpose of using the task projection vectors and why is it used to compute both z_s and z_tp?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Inspired by the notion that most methods that work in a task-incremental scenario can achieve almost zero forgetting, the authors introduce AGILE (Attention-Guided Incremental Learning). The main idea is to break down a class incremental problem into two sub-problems: Task-ID prediction (TP) and within-task prediction (WP). Once the first one is solved, the problem can be treated as a Task-Incremental, as the predicted task-id is already available. The authors suggest using task-specific projections to condition the feature vector. This conditioned vector passes through a task-specific module: task prediction and feature importance. During inference, the output of each module is concatenated to obtain the prediction. The authors demonstrate good performance in both task and class incremental scenarios.

### Strengths
- The authors work under the assumption that the incremental Class problem can be transformed into a task-incremental problem.
    - However, I can't entirely agree that this is a "necessary and sufficient" solution. In fact, there is a probability that working the problem in this way helps the model lose generalization in the representations it generates, and the only reason why this does not happen in the proposed solution is that they use a buffer to store previous tasks.
    - Even so it is a problem that is not widely attacked, but that can be a good option in many cases, especially if it's motivated by the idea of GWT.
- The approach comprises many different components that have a good synergy between them. It is beneficial that the authors add Table 2 to show the importance of each loss.

### Weaknesses
 - The authors work under the assumption that the incremental Class problem can be transformed into a task-incremental problem.
    - However, I can't entirely agree that this is a "necessary and sufficient" solution. In fact, there is a probability that working the problem in this way helps the model lose generalization in the representations it generates, and the only reason why this does not happen in the proposed solution is that they use a buffer to store previous tasks.
    - Even so it is a problem that is not widely attacked, but that can be a good option in many cases, especially if it's motivated by the idea of GWT.
- The approach comprises many different components that have a good synergy between them. It is beneficial that the authors add Table 2 to show the importance of each loss.

 - Using EMA is a critical point in the proposal, and the authors do not mention it too much. EMA can also be used to reduce weight modification, meaning that it can mitigate forgetting with a favorable beta. The authors present it to increase generalization.
    - Experiments showing evidence that it increases generalization could help mitigate the doubts.
    - Did you have an analysis of the beta value? 
- It is challenging to understand where there are linear layers and where there is soft attention in the proposed methods. The image does not help.
    - It could be helpful to decrease the amount of terms, names or losses used in the explanation.
    - For example, from the Figure, one can assume that there is one Task-Attention Module for each task. However, the Task-Attention Module is shared, no?
- Didn’t find Definition 1 and 2.

### Questions
- Is EMA used in every method for Table 1? Or just AGILE?
- How much overhead in terms of time is added when adding a Task-Attention Module?
    - Even if the Task-Attention module is shared, it must still be used independently for each task.
- Are you familiar with the work called Bias Correction (BiC) in Continual Learning? 
    - There are some similarities that you can find interesting.
    - I don’t remember if it works in class or task-incremental, but there have been extensions that work in class-incremental settings.
- Do you know how your proposal scales with the memory size? I have seen methods that scale well (such as DER), but others could be better (like iCarl).
- Have you tried this approach with a fixed pre-trained model?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper focuses on mitigating task interference in continual learning by introducing a compact task-attention module. It incorporates a set of lightweight, learnable task projection vectors, equal in number to the tasks, which transform the latent representations of a shared task-attention module into task-specific distributions. Additionally, this approach aims to enhance the model's performance in continual learning by jointly addressing the challenges of within-task and task-id prediction.

### Strengths
The approach presented in this paper differs significantly from previous methods by combining a task-attention mechanism with minimal memory overhead. It explores the feasibility of reducing interference between tasks and surpasses rehearsal-based approaches in several continual learning scenarios.

### Weaknesses
A single lightweight task-specific vector may not be sufficient to adequately represent and distinguish the crucial information among multiple tasks. This approach may not effectively address the issue of catastrophic forgetting.



### Questions
1)	This method is less innovative and mainly focuses on solving the task interference problem. How to weigh the importance of solving the interference problem or solving the forgetting problem in continual learning?
2)	The innovation in this paper is that the task-attention module is used to solve the task-id prediction problem, and within-task prediction problem how can it be solved efficiently?
3)	As the number of tasks continues to grow, is there any interference or conflict between these lightweight task-specific vectors?
4)	Can this method be used in other continual learning scenarios, such as Task- free scenario?
5)	Please provide attention-guided visualization experiments showing what the task-specific vector makes the model pay attention to.
6)	In section 3.4 only the extension of the classifiers was carried out, what exactly does the network extension refer to?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
