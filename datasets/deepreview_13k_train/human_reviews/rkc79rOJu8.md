# BeST - A Novel Source Selection Metric for Transfer Learning

- Decision: Reject
- Scores: 5, 3, 6

## Abstract
One of the most fundamental, and yet relatively less explored, goals in transfer learning is the efficient means of selecting top candidates from a large number of previously trained models (optimized for various "source" tasks) that would perform the best for a new "target" task with a limited amount of data. In this paper, we undertake this goal by developing a novel task-similarity metric (BeST) and an associated method that consistently performs well in identifying the most transferrable source(s) for a given task. In particular, our design employs an innovative quantization-level optimization procedure in the context of classification tasks that yields a measure of similarity between a source model and the given target data. The procedure uses a concept similar to early stopping (usually implemented to train deep neural networks (DNNs) to ensure generalization) to derive a function that approximates the transfer learning mapping without training. The advantage of our metric is that it can be quickly computed to identify the top candidate(s) for a given target task before a computationally intensive transfer operation (typically using DNNs) can be implemented between the selected source and the target task. As such, our metric can provide significant computational savings for transfer learning from a selection of a large number of possible source models. Through extensive experimental evaluations, we establish that our metric performs well over different datasets and varying numbers of data samples.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This manuscript introduces a task-similarity metric designed to identify the most transferable source pre-trained model for a given target task. The proposed metric leverages a quantization-based method to evaluate the similarity between a source pre-trained model and a new target dataset without requiring re-training. By using an early stopping technique, the proposed method derives a quantized representation of the source model’s softmax outputs, which could be used to rank and select the best source pre-trained models. Experimental results demonstrate the method’s effectiveness across various classification datasets.

My main concern is how the theoretical framework supports the claim that the proposed quantized representation relates to the generalization of a pre-trained model on a given target task. If the authors can address this concern properly during rebuttal, I am inclined to increase my evaluation score significantly; otherwise, I may consider lowering it further.

############################### Post Rebuttal ###############################

None author response found. I will keep my score.

### Strengths
1. Overall, the paper is well-written with clear motivation. Each of the proposed component and its theoretical insights are clearly presented. 

2. This manuscript provides a practical strategy for selecting the most transferable source models, allowing for efficient pre-selection before engaging in the computationally intensive transfer to target tasks. 

3. The proposed method introduces a task-similarity metric based on quantization-level optimization, which is novel and interesting

### Weaknesses
1. Based on my understanding, the quantization level is an important aspect of the proposed method. However, there is no experiment showing how changes in the quantization level affect target task performance. I suggest that the authors include a detailed ablation study on the quantization level.

2. As mentioned by the authors, the proposed method relies on early stopping during source pre-training. Thus, repeated experiments with different random seeds for network initialization are necessary, as early stopping can be influenced by these random seeds. I suggest the authors conduct repeated experiments and include the standard deviation of the results in their figures to reflect this variability.

3. The experiments are conducted on small and synthetic image datasets, and early stopping might be influenced by task type and data modality. I suggest that the authors conduct more experiments on various data modalities (e.g., time-series, language) and tasks (e.g., regression) to better validate the effectiveness of the proposed source model selection strategy.

4. While the manuscript focuses on selecting the best source model, it is unclear how well it can handle negative transfer, where an unsuitable source pre-trained model could harm target task performance. I would suggest some visualizations demonstrating how the proposed strategy can handle negative transfer.

5. Certain theoretical assumptions, such as how the target generalization relies on the early stopping and the quantization strategy, are not well-justified or well-connected in the context of transfer learning. At least, I would expect a discussion on how an upper bound of the target classification error might be connected to early stopping of the source pre-trained models with different underlying tasks.

6. Early stopping is a well-studied method for better understanding a model’s generalization in classification tasks. However, the experiments lack baseline methods for comparison. Without comparisons to existing methods with similar objectives, it is difficult to evaluate the practical value of the proposed method. I would suggest the authors to conduct an in-depth literature review on early stopping.

### Questions
1. How sensitive is the method to changes in the quantization level, and are there any scenarios where finding an optimal  $q^{\ast}$  might not be feasible?

2. Can the proposed method be applied to tasks beyond classification, such as regression?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The manuscript introduces a new metric for selecting source models in transfer learning, utilizing quantization to estimate transferability. It provides theoretical backing to guarantee performance improvements, particularly in binary classification tasks, offering a practical approach for enhancing model fine-tuning.

### Strengths
1. The paper addresses a highly relevant scenario in the current landscape of machine learning where fine-tuning a pre-trained model is more common and practical than training a model from scratch. This approach is valuable for efficiently leveraging existing computational resources and knowledge.
2. The methodology involving quantization to estimate transferability introduces a novel technique to the field of transfer learning. 
3. The paper provides a theoretical foundation that ensures the performance of the proposed method, especially highlighted in simpler scenarios such as binary classification.

### Weaknesses
1. The experiments are conducted using only DNNs and on small-scale datasets, specifically CIFAR10 and MNIST. These choices are not convincing enough to demonstrate the method's effectiveness and generalizability across different or more complex datasets. The fact that only subsets of these datasets were used further constrains the results, making it difficult to assess how the proposed method would perform on larger, real-world datasets like ImageNet. 
2. The paper fails to include a comprehensive comparative analysis with contemporary methods such as NCE, LEEP, and LogMe. This omission is significant because it does not allow for a clear understanding of how the proposed method stands against the latest advancements in the field, especially those methods that might use similar or more advanced techniques for source selection in transfer learning.
3. The manuscript assumes the use of a fixed source model that will be fine-tuned on the target task, a black-box scenario that diverges from common practice where users typically have access to the pre-trained model. This assumption raises practical concerns: why would users opt to fine-tune a model without access to its original, pre-trained state? This setting contrasts with existing works that usually allow for adjustments to the source model itself. An explanation of the practicality of this assumption and a justification for diverging from the typical settings found in the literature would strengthen the manuscript's relevance and applicability.
4. Measuring the relatedness between the source and target tasks to estimate the transferability has been explored in [1-3]. A detailed discussion comparing these existing methods with the novel approach proposed in the manuscript is necessary. This would highlight the contributions or potential improvements offered by the new metric and provide clarity on its benefits over previous strategies.

### Questions
1. In line 372, could you specify what the first and second datasets refer to? Are they different from the third one, i.e. CIFAR10-MNIST?
2. The computational benchmarks in the paper are conducted on a CPU, whereas, in typical practice, model fine-tuning is often performed on a GPU. Given the specific fine-tuning setup described, which involves only updating a few linear layers on top of a fixed pre-trained model, the process is expected to be relatively quick on a GPU. Therefore, it would be valuable to compare the efficiency of the proposed metric against traditional fine-tuning methods when both are executed on a GPU. How does the efficiency of the proposed metric compare to that of standard GPU-based fine-tuning?
3. The evaluation metrics used in this paper differ from those typically seen in related works. Could including Pearson or Kendall coefficients provide a more standardized comparison with existing methods?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This submission presents a metric for selection of the best source tasks that may be adaptive to target task. The key lies in the selection of the most transferable sources for a given task. This work shows a quantization-level optimization method. Experiments show the metric performs well over different datasets.


The authors do not provide feedback. I therefore reduce my score.

---Since the authors have further provided feedback about my concerns and most of my concerns have been addressed. I keep my original rating, because the writting may have space to improve.

### Strengths
1. The topic for selecting most transferable source tasks for a given target task is interesting and sounds good.
2. The proposed method has some technical novelty and I like this idea during the numerous transfer learning methods.
3. It is good to fully consider the computational savings during selection of possible source models.

### Weaknesses
1. I think the very weakness lies in the writting of the technical parts. It is obscure and sometimes difficult to understand the mathematical part such as the policy optimization and computation. It is unclear why such computation is proposed, such as Eq.1 and lack intuition behind this idea. Specifically, the quantization process in Equation 1, while presented mathematically, lacks a clear explanation of its practical implications and how it relates to the overall goal of source task selection. The connection between the quantization of the softmax vector and the subsequent policy optimization is not clearly established, making it difficult to grasp the motivation behind this approach. The description of the policy optimization itself is also vague, leaving the reader unsure about the exact steps involved in finding the optimal policy and how it relates to the train and validation accuracies.
2. I think in Algorithm 1, it may not be easy to reproduce from the current description. The algorithm's steps, particularly the ternary search, are not sufficiently detailed, making it challenging to implement the method accurately. The description lacks clarity on how the train and validation accuracies are calculated within the ternary search process, and the specific criteria for stopping the search are not well-defined. Furthermore, the connection between the algorithm's output and the final metric is not explicitly stated, which further hinders reproducibility.
3. I suggest the authors clarify some simple concept such as task-similarity, selection strategy, etc. in implementation, without particular wrap up in mathematical aspects. The concept of task similarity, as used in the paper, needs to be defined more clearly in the context of the proposed method. The paper does not provide a clear explanation of how the proposed metric relates to the intuitive notion of task similarity. The selection strategy, which is central to the paper's contribution, is not presented in a way that is easily understandable, and the link between the mathematical formulation and the practical implementation is missing. The lack of a clear explanation of these fundamental concepts makes it difficult to assess the practical value of the proposed method.
4. This submission will have a higher quality if the writting is further improved. I lean to accept this submission, and expect the authors' feedback.

### Questions
I would like to ask what is the intuition behind the complex design of the metric?

### Soundness
3

### Presentation
2

### Contribution
3
