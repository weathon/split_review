# Towards Few-Shot Adaptation of Foundation Models via Multitask Finetuning

- Decision: Accept
- Scores: 5, 5, 8, 6

## Abstract
Foundation models have emerged as a powerful tool for many AI problems. Despite the tremendous success of foundation models, effective adaptation to new tasks, particularly those with limited labels, remains an open question and lacks theoretical understanding. 
  An emerging solution with recent success in vision and NLP involves finetuning a foundation model on a selection of relevant tasks, before its adaptation to a target task with limited labeled samples. In this paper, we study the theoretical justification of this multitask finetuning approach. 
  Our theoretical analysis reveals that with a diverse set of related tasks, this multitask finetuning leads to reduced error in the target task, in comparison to directly adapting the same pretrained model. We quantify the relationship between finetuning tasks and target tasks by diversity and consistency metrics, and further propose a practical task selection algorithm.
  We substantiate our theoretical claims with extensive empirical evidence.
  Further, we present results affirming our task selection algorithm adeptly chooses related finetuning tasks, providing advantages to the model performance on target tasks.
  We believe our study shed new light on the effective adaptation of foundation models to new tasks that lack abundant labels.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper explores how to effectively adapt foundational models to new tasks, especially those with limited labeled data. The authors investigate a multi-task fine-tuning approach, wherein the foundational model is fine-tuned for a set of related tasks before fine-tuning it for the target task.

### Strengths
The paper provides a theoretical analysis, revealing that fine-tuning with a diverse set of related tasks reduces errors in the target task compared to directly adapting a pre-trained model. The authors introduce diversity and consistency metrics to quantify the relationship between fine-tuning tasks and the target task and propose a practical task selection algorithm.

### Weaknesses
1. In Section 1.1, it would be beneficial to provide a more detailed enumeration of recent advancements in the field of multitask fine-tuning. Specifically, the discussion should include a breakdown of different multi-task learning strategies, such as parameter sharing, task-specific layers, and adversarial training, and how these relate to the proposed approach. The current introduction lacks the necessary depth to contextualize the novelty of the method within the broader field.
2. I suggest adding some diagrams in Section 3.2 to visually illustrate the entire process. The current description of the task selection algorithm, while presented in Algorithm 1, is difficult to grasp intuitively. A visual representation, such as a flowchart or a graph, would significantly improve the reader's understanding of how diversity and consistency metrics are used to guide the task selection process. This would also help in assessing the effectiveness of the task selection.
3. I suggest conducting more detailed ablation experiments for TASK SELECTION to provide stronger evidence for its effectiveness. The current ablation study should include a more granular analysis of the impact of diversity and consistency metrics. For instance, it would be helpful to see results where only diversity is considered, only consistency is considered, and where both are gradually increased or decreased. This would help to isolate the contribution of each metric to the overall performance.
4. The experimental section lacks sufficient detail, such as the absence of descriptions for hyperparameter settings. Specifically, the learning rate, batch size, optimizer, and the number of training epochs used for both the multi-task fine-tuning and the final target task fine-tuning should be explicitly stated. Additionally, the method used for selecting these hyperparameters should be described. Without this information, it is difficult to reproduce the results and assess the validity of the findings.

### Questions
1. In Section 1.1, it would be beneficial to provide a more detailed enumeration of recent advancements in the field of multitask fine-tuning.
2. I suggest adding some diagrams in Section 3.2 to visually illustrate the entire process. Visual representation will help readers gain a clearer understanding and assess the effectiveness of task selection.
3. I suggest conducting more detailed ablation experiments for TASK SELECTION to provide stronger evidence for its effectiveness.
4. The experimental section lacks sufficient detail, such as the absence of descriptions for hyperparameter settings. Providing these details would make the findings more convincing.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Given a pretrained foundation model, a target task with limited labeled samples, and a bunch of auxiliary tasks possibly with many labeled data, this paper analyzes how to select good auxiliary tasks to finetune the foundation model first, then adapt the auxiliary-task-finetuned model to the target task (a.k.a multitask finetuning), such that the resultant model can outperform the model that directly adapted to the target task from pretraining, or the model that finetuned with all the auxiliary tasks before adaption. To this end, the authors derive several bounds which indicate that the model with multitask finetuning outperforms that without, and the selected auxiliary tasks should be sufficiently diverse and have good consistency w.r.t. the target task. According to this, the authors formulate an auxiliary-tasks-selection algorithm, whose outperformance over standard finetune is validated on various datasets.

### Strengths
1. Several bounds about multitask finetuning are derived.
2. The multitask finetuning with task selection outperforms that finetuned on all the tasks.
3. The experiments have been extensively performed on a dozen of datasets.

### Weaknesses
1. While several bounds have been derived, their implications are quite straightforward. For instance, the model with multitask fine-tuning outperforms the one without it, and the selected auxiliary tasks should exhibit sufficient diversity and strong consistency w.r.t. the target task, are well accepted by the community, despite those being derived based on the somewhat strict assumptions. It would be more valuable if these bounds could lead to novel insights that were previously overlooked by the community. Specifically, the derived bounds, while mathematically sound, do not offer much practical guidance beyond what is already understood intuitively. The consistency and diversity terms, while formalized, don't provide a new way to think about task relationships or offer a novel optimization strategy. The assumptions made, such as the feature distribution being Gaussian, further limit the practical applicability of these bounds.
2. Such limitation also lies in the task-selection algorithm, where the authors simply assume a Gaussian distribution of features, then use the angle of mean and variance-scaled L2 distance indicating the consistency and the diversity. This approach is overly simplistic and may not capture the complex relationships between tasks in real-world scenarios. The Gaussian assumption is a strong one and is unlikely to hold for many practical datasets, potentially leading to suboptimal task selection. Furthermore, the use of angle and variance-scaled L2 distance as the sole metrics for consistency and diversity is not sufficiently robust, as these metrics may not capture higher-order relationships or non-linear dependencies between tasks.
3. As \phi evolves during the training, should Algorithm 1 perform repeatedly during the training?
4. The paper in its current version is quite difficult to read, it is suggested to give more intuition before diving into the derivation, and also simplify/brief the symbols if applicable.

### Questions
1. Why does the performance decrease with the increase of sample shots in Fig. 2a?
2. Is Standard FT in Table 2 the same as All in Table 1?
3. First Paragraph on Page 4, In contrastive pretraining -> In contrastive to pretraining; First Paragraph on Page 7, the cosine similarity similarity -> the cosine similarity
4. It seems that Theorem 3.3 (or the index 3.3) is missing in the main text.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents theoretical results that to adapt a pretrained model to a target task, it is beneficial to first finetune the model on a diverse set of related tasks and then tune the model on the target task. The authors prove the theorems by first defining the diversity and consistency between different tasks that the model is going to adapt to, where diversity refers to the coverage of the other tasks on the target task and consistency refers to the similarity between the other tasks and the target task. Then, under some Lipschitzness assumptions, sufficient consistency and diversity assumptions, and sufficient tasks and sufficient sample assumptions (on the finetuning tasks, not the target task), the model with multitask finetuning can achieve a reduced error on the target task compared to the setting without multitask finetuning. Moreover, the authors propose a multitask selection algorithm based on the consistency and diversity requirements. Experimental results indicate that with the proposed multitask selection, the ViT-B model achieves better results on multiple target datasets, and increasing the number of tasks and the number of samples per task are most effective in improving target task performance. Lastly, with multitask finetuning, various pretrained models achieve better results than direct adaptation / standard finetuning on multiple datasets.

### Strengths
- The presented theoretical results are quite intuitive -- if the tasks in multitask finetuning are diverse and consistent with the target task $T_0$, then the model with pretraining followed by multitask finetuning achieves better target prediction performance than the model only with pretaining. My intuition is that, through the training/finetuning on the proxy tasks, the model learns some knowledge related to the target tasks. It is nice that the authors present the theorems that support this intuition, although I didn't verify the proofs. 
- Although the theorems are not directly applicable to real problems, the authors propose a practical Consistency-Diversity Task Selection algorithm, which is effective in experiments. The algorithm is a nice method to try for target task adaption in the real world.
- The overall experiments are quite extensive and echo the theoretical results, clearly demonstrating the advantages of multitask finetuning over standard finetuning and direct adaptation.

### Weaknesses
 - The Gaussian distribution assumption in Section 3.2 may not be realistic, leading to biased task selection that may be suboptimal to the model performance on the target task. Specifically, the assumption that task embeddings follow a Gaussian distribution might not capture the true underlying structure of task relationships, potentially causing the selection algorithm to favor tasks that are not truly beneficial for the target task. This could result in a situation where the selected tasks are diverse in the embedding space but not semantically diverse or relevant to the target task. However, it is okay to derive further refined algorithms in future work.

 - I found the notations in Section 3.1 (Linear Data and Tasks) somewhat difficult to understand. $T_{z, z'}$ is discussed in the text but how is it related to the $T_i (i = 1, \dots, M)$ in figure 1? It would ease the reader's understanding by revising the explanation in that part.  The connection between the theoretical task definition $T_{z,z'}$ and the practical tasks $T_i$ used in the experiments is unclear. The current explanation does not clearly articulate how the latent classes $z$ and $z'$ map to the actual tasks used in the experimental setup, making it hard to connect the theoretical analysis to the empirical results. A more explicit definition of how these abstract tasks are instantiated in the experiments is needed.
 - Does the Experiment Protocol apply to all three major experiments (4.1, 4.2, and 4.3)? It seems to me that the experiments have their own protocols, which causes confusion. The description of the experimental setup lacks clarity regarding the consistency of the protocol across different experiments. It is unclear whether the same hyperparameter settings, training procedures, and evaluation metrics are used across all three experimental sections, making it difficult to compare the results and draw meaningful conclusions. The lack of a clear, unified protocol makes it difficult to assess the validity of the experimental results.
 - What are the multitasks for finetuning in Section 4.3? The specific details regarding the nature of the multitask datasets used in Section 4.3 are not provided. It is unclear what datasets or tasks are used for the multitask finetuning, which makes it hard to assess the relevance and effectiveness of the chosen tasks for improving the target task performance. Without knowing the exact tasks, it is difficult to understand the experimental results and their implications.

### Questions
- I found the notations in Section 3.1 (Linear Data and Tasks) somewhat difficult to understand. $T_{z, z'}$ is discussed in the text but how is it related to the $T_i (i = 1, \dots, M)$ in figure 1? It would ease the reader's understanding by revising the explanation in that part. 
- Does the Experiment Protocol apply to all three major experiments (4.1, 4.2, and 4.3)? It seems to me that the experiments have their own protocols, which causes confusion.
- What are the multitasks for finetuning in Section 4.3?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies multitask finetuning for adapting foundation models to new tasks in few-shot. It provides a theoretical justification to analyze the multitask finetuning and a practical task selection algorithm for choosing good finetuning tasks. Extensive experiments are conducted to validate the proposed algorithm.

### Strengths
- The paper proposes a theoretical framework to analyze multitask finetuning for foundation models, providing definitions and analysis of task diversity and consistency. Based on the theoretical concepts, the authors introduce a practical task selection algorithm.
- The authors conducted extensive experiments and showed the effectiveness of the proposed method compared to the direct adaptation and full fine-tuning baseline.
- The overall writing is good, which clearly explains the problem, approach, analysis and results.

### Weaknesses
 - The theoretical part discussed diversity and consistency, but the method part simplifies consistency to similarity and diversity to coverage. So the final algorithm is basically a similarity-based sorting. The simplicity is not a problem, but I wonder if it is really related to the theoretical concepts.
- The authors evaluated the proposed algorithm on a wide range of datasets/models, but how does it compare with some stronger baselines besides direct adaptation and full fine-tuning, e.g. meta-learning algorithms?

### Questions
See above

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
