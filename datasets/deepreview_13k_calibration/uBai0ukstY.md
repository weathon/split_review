# Equivariant Neural Functional Networks for Transformers

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
This paper systematically explores neural functional networks (NFN) for transformer architectures. NFN are specialized neural networks that treat the weights, gradients, or sparsity patterns of a deep neural network (DNN) as input data and have proven valuable for tasks such as learnable optimizers, implicit data representations, and weight editing. While NFN have been extensively developed for MLP and CNN, no prior work has addressed their design for transformers, despite the importance of transformers in modern deep learning. This paper aims to address this gap by providing a systematic study of NFN for transformers. We first determine the maximal symmetric group of the weights in a multi-head attention module as well as a necessary and sufficient condition under which two sets of hyperparameters of the multi-head attention module define the same function. We then define the weight space of transformer architectures and its associated group action, which leads to the design principles for NFN in transformers. Based on these, we introduce Transformer-NFN, an NFN that is equivariant under this group action. Additionally, we release a dataset of more than 125,000 Transformers model checkpoints trained on two datasets with two different tasks, providing a benchmark for evaluating Transformer-NFN and encouraging further research on transformer training and performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces a novel concept of Transformer Neural Functional Networks (Transformer-NFN), designed as equivariant neural functional networks specifically for transformer architectures.The proposed Transformer-NFN addresses the challenge of applying neural functional networks (NFNs) to transformers by systematically defining weight spaces, symmetry groups, and group actions for multi-head attention and ReLU-MLP components. Experimental results demonstrate the effectiveness of Transformer-NFN in predicting transformer generalization and performance, surpassing traditional models across multiple metrics.

### Strengths
- The is the first paper to my knowledge expore neural functional networks (NFN) in the context of transformer, where NFN treat the weights, gradients, or sparsity patterns of a deep neural network (DNN) as input data.
- The proposed Small Transformer Zoo dataset is a valuable resource for benchmarking and studying transformer-based networks, promoting reproducibility and further research.

### Weaknesses
 - The paper did not discuss the computational overhead associated with equivariant polynomial layers and whether this could affect scalability for larger transformer models.

### Questions
- I'm curious how sensitive is the maximal symmetric group of the weights in a MHA module, would affect the peformance of final peformance of NFN.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a formulation of NFNs for transformers beyond MLPs and CNNs. The paper provides thorough analysis of how to establish a weight space around multihead attention and a way to formalize NFNs through a parameter sharing strategy. The paper also shows the application on multiple transformer models across a basic vision and language task. The paper is very detailed in it's approach and provides for a good approach to understanding how the weights of transformer blocks are affected by hyperparameters and data

### Strengths
The paper provides a very structured approach to a the solution of defining NFNs for transformers and is rigorous in it's approach.Some of the mathematical formulation around weight spaces of a multihead attention and the solution for parameter sharing of the NFN is good.

### Weaknesses
The paper is a bit dense to read and understand. Though this can be considered fine given the topic and detailed approach. There could've been a better balance at analyzing the different theorems presented vs covering the mathematical proof.

The experimentation is basic and doesn't necessarily capture the strengths of the method or even transformers. Transformers are known to generalize over large model sizes and large data and it is the biggest weakness of the paper on how this method would hold for larger models. Even if a small scale experiment was included, it would bolster the through mathematical approach much better.

### Questions
How does this generalize to models with more parameters and trained on larger datasets

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper investigates Equivariant Neural Functional Networks for Transformer architectures by developing a specialized model, Transformer-NFN, designed to process the weights, gradients, or sparsity patterns of Transformers as input data. The paper defines a maximal symmetric group for multi-head attention modules and establishes a group action on the weight space of Transformer architectures, creating a systematic framework for NFNs with equivariance properties. Besides, Transformer-NFN, an NFN specifically tailored to Transformer structures, is evaluated on a new dataset containing 125,000 Transformer checkpoints. Experimental results indicate that Transformer-NFN outperforms other models in predicting Transformer model performance.

### Strengths
1. The paper presents a novel theoretical framework for designing Neural Functional Networks that respects the inherent symmetries of Transformer architectures, representing an innovative approach previously unexplored in this domain.
2. The release of a dataset with 125,000 Transformer model checkpoints offers a valuable resource for future research on Transformer performance prediction and NFNs.
3. The paper provides a detailed methodological development, including thorough derivations and design principles, establishing the theoretical foundation for NFNs tailored to Transformer architectures, which may inspire future studies in this area.

### Weaknesses
1. While the use of equivariant layers in Transformer-NFN is theoretically compelling, empirical results suggest limited practical impact. Specifically, the marginal gains in predictive accuracy on the benchmark dataset raise questions about the method’s utility in real-world applications. The reported improvements, while statistically significant, are small, and it is unclear if these gains justify the added complexity, especially when considering the computational overhead of implementing equivariant layers. The performance increase needs to be more substantial to demonstrate a clear advantage over simpler, non-equivariant models.

2. The architecture's intricate structure, requiring a specialized understanding of group actions and equivariant layers, could hinder adoption. The dense theoretical foundation, coupled with limited practical resources, may present obstacles to reproducibility and broader implementation in practical settings. The reliance on advanced mathematical concepts like group theory and representation theory makes the method less accessible to practitioners who may not have a strong background in these areas. This complexity could limit the practical impact of the work, as it may be difficult for others to reproduce or adapt the method.

### Questions
1. Could the authors clarify the expected computational cost of Transformer-NFN compared to traditional NFNs, considering the added design complexity?
2. Will the paper include code to facilitate reproducibility?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This submission provides a theoretical study of neural functional networks (NFNs) for transformers. By formally defining the weight space of the standard transformer block and the corresponding group action of such a space, the authors propose several design principles for NFNs and introduce Transformer-NFN to predict the test performance with a transformer checkpoint and the corresponding training configurations. Additionally, a dataset with 125k transformer checkpoints trained on MINST and AGNews will be released for reproduction and further analysis.

### Strengths
- This topic is quite interesting and do have some foreground. In the foreseeable future, a plenty of pre-trained transformer checkpoints would be released and there is no golden rule to find out which checkpoint is appropriate for a specific task. And the NFN may be useful and draw some inspiration for future research.
- For all I know, this may be one of the first works to develop NFN for transformers. 
- The theoretical analysis is detailed enough.

### Weaknesses
 - According to the main presentation of this submission, no obvious weaknesses are found.

 - From my perspective, the performance of a checkpoint is related to the training data, the architecture of the network, the training algorithm, hyperparameter configuration, etc. So why does NFN only take the weights and the configuration into account? Is it a sufficient condition for performance prediction?
- The evaluated dataset is far away from the present scale of transformer. The weight of modern transformers is huge (bert-base 110M parameters), is Transformer-NFN able to predict the performance of it?

### Questions
- How about the performance on language modeling? Is Transformer-NFN able to predict?
- How about the performance of the larger transformer 
- From my perspective, the performance of a checkpoint is related to the training data, the architecture of the network, the training algorithm, hyperparameter configuration, etc. So why does NFN only take the weights and the configuration into account? Is it a sufficient condition for performance prediction?
- The evaluated dataset is far away from the present scale of transformer. The weight of modern transformers is huge (bert-base 110M parameters), is Transformer-NFN able to predict the performance of it?

### Soundness
3

### Presentation
3

### Contribution
3
