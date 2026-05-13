# Transforming Transformers for Resilient Lifelong Learning

- Decision: Reject
- Scores: 5, 5, 6, 6

## Abstract
Lifelong learning without catastrophic forgetting (i.e., resiliency) remains an open problem for deep neural networks. The prior art mostly focuses on convolutional neural networks.  With the increasing dominance of Transformers in deep learning, it is a pressing need to study resilient lifelong learning with Transformers. Due to the complexity of training Transformers in practice, for lifelong learning, a question naturally arises: Can the Transformer be learned to grow in a task aware way, that is to be dynamically tranformed by introducing lightweight learnable plastic components to the architecture, while retaining the parameter-heavy, but stable components at streaming tasks?
To that end, motivated by the lifelong learning capability maintained by the functionality of Hippocampi in human brain, 
this paper explores what would be, and how to implement, Artificial Hippocampi (ArtiHippo) in Transformers. It presents a method of identifying, and then learning to grow, ArtiHippo in Vision Transformers (ViTs) for resilient lifelong learning in four aspects: (i) Where to place ArtiHippo in ViTs to enable plasticity while preserving the core function of ViTs at streaming tasks? (ii) What representational scheme to use to realize ArtiHippo to ensure expressivity and adaptivity for tackling tasks of different nature in lifelong learning? (iii) How to learn to grow ArtiHippo to exploit task synergies (i.e., the learned knowledge) and to overcome catastrophic forgetting? (iv) How to harness the best of our proposed ArtiHippo and prompting-based approaches? In experiments, the proposed method is tested on the challenging Visual Domain Decathlon (VDD) benchmark and the recently proposed 5-Dataset benchmark under the task-incremental lifelong learning setting. It obtains consistently better performance than the prior art with sensible ArtiHippo learned continually. To our knowledge, it is the first attempt of lifelong learning with ViTs on the challenging VDD benchmark.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper addresses the challenge of catastrophic forgetting in deep neural networks, particularly focusing on Transformer models, which are increasingly popular but complex to train for lifelong learning tasks. It introduces a concept called Artificial Hippocampi (ArtiHippo) within Vision Transformers (ViTs) to enhance their resiliency and adaptability for continual learning, drawing inspiration from the human brain and demonstrating improved performance on rigorous benchmarks.

### Strengths
+ The paper is well written, and the idea is also elaborated clearly. There is no trouble in reading and reproducing the algorithm.
+ In addition, the implementation and code are provided to demonstrate the proposed algorithm.
+ Experiments provide adequate support to the assumptions and claims and prove that the new method is applicable to vision datasets.

### Weaknesses
 - The major concern is the lack of novelty for the paper to be published in ICLR. Although the paper is well thought out and demonstrated with extensive experiments, the novelty is rather incremental. See the question section.
- Another issue is the research problem “task incremental learning,” which seems not very practical in many vision applications. As the authors discussed, “class incremental” is more demanded since the task information is not always (unlikely) available.
- Some comparisons in experiments seem unfair and may not be able to reflect the true performance of each framework.

### Questions
1.	The key methodology of this paper is mainly built upon several existing works. The four operations are adapted from “learning-to-grow,” and the construction of supernet is based on SPOS. Although finding the right place to place ArtiHippo is tricky, it has been common sense that classification information is mostly likely located on the upper level of the network.
2.	In addition, the method leverages the recent “prompt” based method such as S-Prompts to further improve the performance. This makes the neat “ArtiHippo” based algorithm a bit over-complicated and more engineering-driven.
3.	It seems all methods always use pre-trained strong ViT backbone for incremental tasks. This does cover all the cases in lifelong learning, e.g., starting from a moderated size model, or from zero knowledge. The current methodology is still like finetuning a strong baseline on several small datasets. The problem discussed and experiments are not typical lifelong learning scenarios.
4.	The major concern lies in the knowledge of “task.” It does not always make sense to know where the data are from or their sources.

### Soundness
3 good

### Presentation
4 excellent

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
In this paper, the authors tackle the problem of lifelong learning in deep neural networks, specifically focusing on Vision Transformers (ViTs). They introduce a concept inspired by the human brain's hippocampus, called Artificial Hippocampi (ArtiHippo), to help ViTs learn continuously without forgetting previous knowledge—a common challenge known as catastrophic forgetting. The study explores where to place ArtiHippo within ViTs, what kind of structure it should have, and how it can grow and adapt over time while retaining past knowledge. By testing their approach on challenging benchmarks, the authors demonstrate that their method not only performs better than previous ones but also marks the first successful application of lifelong learning in Vision Transformers, showing great promise for future AI systems.

### Strengths
1. Balanced Exploration and Exploitation: The proposed method offers a new searching strategy that balances exploration (learning new information) and exploitation (using existing knowledge), crucial for the development of robust lifelong learning systems.

2. Empirical Results: The approach is thoroughly evaluated on challenging benchmarks, where it consistently outperforms existing methods. This demonstrates the practical effectiveness of the proposed solution and its potential for real-world applications.

### Weaknesses
1. Refinement Rather Than Revolution: The integration of ArtiHippo into Vision Transformers, though presented as a novel idea, is actually a clever twist on the established "learning to grow" concept. It's a smart update, but it falls short of being a game-changer. It feels like we're seeing a refinement of existing ideas rather than a bold reimagining of lifelong learning. The core mechanism of dynamically expanding the network based on task demands, while applied to a new architecture (ViTs), doesn't introduce a fundamentally new learning paradigm. The novelty is primarily in the application rather than the underlying concept.

2. A Safe Bet Over a Leap of Faith: Employing Reuse, New, Adapt, and Skip operations within Transformers comes across as a safe, almost expected move. It's as if the paper takes a well-trodden path, applying tried-and-tested strategies to new territory, rather than venturing into unexplored innovative realms. The selection of these specific operations, while effective, lacks a strong justification beyond their prior use in other 'learning to grow' methods. There is no exploration of alternative operations or a discussion of why these are the most suitable for ViTs.

3. Narrow Lens on Competing Approaches: The paper misses a beat by not sizing up ArtiHippo against the full spectrum of lifelong learning strategies, particularly gradient-based and regularization-based methods. This omission leaves us guessing about how ArtiHippo truly stacks up against the competition and muddies the waters of its potential as a standout solution in the field. The comparison is limited to other 'learning to grow' approaches and prompt-based methods, neglecting a broader evaluation against established lifelong learning techniques.

### Questions
In what ways does the ArtiHippo framework conceptually and functionally diverge from the 'Learning to Grow' methodology, considering the apparent similarities in their approach to lifelong learning?

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a method of training vision transformers (ViTs) for lifelong learning under the task-incremental setting. It identifies the final projection layer of multi-head self-attention of a ViT as the Artificial Hippocampi (ArtiHippo) of ViTs, and learns to dynamically grow the ArtiHippo by four operations "Skip", "Resue", "Adapt" and "New". The maintenance of ArtHippo is realized by hierarchical exploration-exploitation sampling where the exploitation utilizes task similarities measured by the normalized cosine similarity between the mean class tokens of a new task and those of old tasks. Experiments are conducted on VDD and 5-Datasets benchmarks, showing better performance than previous art.

### Strengths
1. The paper is clearly written, well-presented with rich visualizations and easy to follow. 
2. The method is effective when utilizing ViTs for lifelong learning.  
3. The analysis of results is thorough and insightful.

### Weaknesses
The design choices are mostly experience-guided: e.g. identifying the projection layer as the ArtiHippo, using the mean class tokens to measure task similarity, and four operations to grow the ArtiHippo. More discussions on principles and analysis would make the paper more solid. Specifically, the theoretical justification for treating the final projection layer of the multi-head self-attention mechanism as analogous to the hippocampus is not adequately explored. While the analogy is intriguing, it lacks a strong theoretical foundation. Additionally, the rationale behind using the mean of class tokens as a measure of task similarity needs further elaboration. It is not immediately clear why this particular metric is superior to other potential measures of task similarity. Finally, the four operations ("Skip", "Reuse", "Adapt", and "New") for growing the ArtiHippo appear ad-hoc. A more principled approach to dynamically expanding the model's capacity would strengthen the methodology.

### Questions
1. Could some evaluation on the soundness of measuring task-similarity with the normalized cosine similarity between the mean class tokens be provided? 
2. Would the same conclusion hold for stronger/larger ViT models?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a method for achieving resilient lifelong learning in deep neural networks, focusing on Transformers, which have gained prominence in deep learning. The key challenge addressed is catastrophic forgetting, where networks struggle to learn new tasks without losing previously acquired knowledge. 

The approach suggests integrating task-aware, adaptable components (referred to as Artificial Hippocampi or ArtiHippo) into the architecture of Vision Transformers (ViTs). 

Inspired by the human brain's Hippocampi, known for their role in lifelong learning, the paper explores how these artificial components can be identified, placed, and trained within ViTs to enable adaptability while preserving core functions.

The proposed method belongs to the parameter-tuning category with more fine-grained control.

### Strengths
This paper presents an interesting concept "Artificial Hippocampi (ArtiHippo) in Transformers" for task-incremental learning. The proposed method introduces lightweight transformer components to the dynamic networks to learn the new tasks.

The paper is written and organized well.

It obtains better performance than the prior art with sensible ArtiHippo learned continually.

### Weaknesses
The approach proposed in this article needs to rely on a priori, i.e., knowing in advance to which task a certain data belongs. This limits the practical application scenarios of the CL approach. Specifically, the method requires explicit task boundaries during training, which is not always available in real-world continual learning scenarios where tasks might be unlabeled or arrive in a stream without clear separation. In addition, the method does not scale well as the number of tasks increases. Especially for scenarios where multiple small tasks exist, the overhead of identifying and training task-specific ArtiHippo components could become computationally expensive and may lead to diminishing returns in terms of performance gains. The paper lacks experiments on generic experimental datasets, such as a more comprehensive evaluation on ImageNet and CIFAR100, which are standard benchmarks for image classification tasks. The current evaluation on the VDD benchmark, while diverse, does not fully address the performance of the proposed method on these widely used datasets. Lack of comparison with enough continual learning methods, please discuss or compare with recent proposed baselines. The paper should include comparisons with more recent and relevant continual learning methods, especially those that are designed for transformer-based architectures. The current comparison is limited to a few methods and does not provide a comprehensive view of the state-of-the-art. Missing related Transformer-based continual learning methods, e.g.,

[1] Continual Learning with Transformers for Image Classification. CVPR 2022 CLVision workshop

[2] Continual Learning with Lifelong Vision Transformer. CVPR 2022

[3] D3Former: Debiased Dual Distilled Transformer for Incremental Learning. CVPR 2023

### Questions
Why Tokenized Data is used as input data in Figure 1, is there any special meaning?

Please discuss the differences and similarities between this paper with other Transformer-based CL methods.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
