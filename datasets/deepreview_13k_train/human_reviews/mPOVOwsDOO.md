# Talking Models: Distill Pre-trained Knowledge to Downstream Models via Interactive Communication

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Many recent breakthroughs in machine learning have been enabled by the pre-trained foundation models. By scaling up model parameters, training data, and computation resources, foundation models have significantly advanced the state-of-the-art in many applications.  However, it is still an open question of how to use these models to perform downstream tasks efficiently. 
Knowledge distillation (KD) has been explored to tackle this challenge. KD is a technique that transfers knowledge from a large teacher model to a smaller student model. While KD has been successful in improving student model performance, recent research has discovered that a powerful teacher does not necessarily lead to a powerful student, due to their huge capacity gap. In addition, the potential distribution shifts between the pre-training data and downstream tasks can make knowledge transfer in KD sub-optimal for improving downstream task performance.

In this paper, we extend the knowledge distillation paradigm by introducing an interactive communication process to help student models of downstream tasks learn effectively from pre-trained foundation models. Our design is inspired by the way humans learn from teachers who can explain knowledge in a way that meets the students' needs. Specifically, we let each model (i.e., student and teacher) train two components: (1) an encoder which encodes the model's hidden states to a message in a shared message space and (2) a decoder which decodes any message to its own hidden states. With encoder and decoder, not only can the teacher model transfer rich information by encoding its hidden states to messages, but also the student model can send messages with information of downstream tasks to teacher so that the teacher can interpret and generate responses. With this interactive communication process, knowledge passing from teacher to student can be tailored to the student's model capacity and downstream tasks' distributions. We conducted experiments on benchmark datasets for computer vision and recommendation tasks to show that our communication mechanism outperforms state-of-the-art distillation techniques.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents a new distillation framework that aims to distill knowledge from a pretrained foundation model to a smaller model for downstream tasks. The method is inspired by an interactive communication model, and instantiated by an encoder-decoder architecture. Such a design allows transferring knowledge adaptively based on student model capacities and handling different task distributions. Experiments on vision and recommendation are conducted to verify its effectiveness.

### Strengths
1. I haven't kept up with recent developments in KD, both problem setting and the proposed algorithm appear to be novel given the context provided in the paper.
2. Distillation across different tasks or distributions is challenging problem, yet the proposed model performs well in both vision and recommendation applications.
3. The paper is generally well written, the idea is easy to follow. The analogy between KD and communication models is interesting. It provides a unified view of existing KD approaches and is a clever choice for motivational purpose.

### Weaknesses
1. While the method intuitively makes sense and I understand the paper is centered on applications, it would be nice to make the paper more formal, e.g. by defining different task distributions and the problem you are to tackle. Specifically, the paper lacks a formal definition of the source and target task distributions, and how the proposed method is expected to handle the divergence between them. The current description relies heavily on intuition, making it difficult to assess the theoretical underpinnings of the approach.
2. The link between the method and different task distributions does not seem very clear (partially also due to a lack of formality). Particularly, I still do not fully understand why extending KD to a two-way interactive communication process is relevant solving distribution shift. The paper does not provide a clear explanation of how the encoder-decoder architecture facilitates adaptation to different task distributions. It's unclear why this specific architecture is better suited for handling distribution shifts compared to other knowledge distillation techniques. The mechanism through which the encoder and decoder enable the student model to learn from a teacher trained on a different distribution remains vague.
3. In terms of writing, I do not find the first half of the paper (section 1 and 2) very informative. I think empirical studies in 4.2-4.4 are especially useful for justifying such type of approach, but regrettably they are not highlighted in the main paper.

### Questions
1. How are $l_g$ and $h_g$ chosen? There are also many other hyperparameters, how are they tuned?
2. Can you provide more insights on the question in weakness 2?
3. How is the approach related with foundation models, as teacher models are just some pretrained models, the same as standard KD setting?
4. How distribution shifts are reflected in experiments?
5. Can you discuss the connection with existing cross-task KD approaches?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper interprets the standard knowledge distillation as one-way communication and proposes an interactive communication method to distill knowledge from large models to small models.

### Strengths
The idea of interactive communication between the teacher model and student model is interesting and novel. The introduction and Related work sections are very clear.

### Weaknesses
1. The idea seems novel and interesting, but direct evidence is lacked to support its advantages. The analogy of personal communication, though also interesting, is not enough to explain why the proposed method works. We know that the two models are interacting with each other, but with the concrete communication method, it is hard to say that they are actually "talking" to each other like two persons as hypothesized in Introduction. We actually don't know why the proposed method works. In fact, it is hard to understand the rational of the three proposed loss L_{interact}, L_{MC} and L_{SC}. For example, why should the messages of the teacher and the student be consistent (L_{MC}), considering that they are produced by the two models sequentially? 

In addition, the two additional encoders and two additional decoders can account for most unaligned factors governed by the last three terms in the last equation in page 7 because these four modules are learnable. Then how much internal knowledge of the teacher model could be transferred to the student model by modifying its parameters?  

I doubt that the performance improvement largely comes from the four additional modules as they bring more parameters. A desirable baseline approach for comparison is a knowledge distillation method (such as the one illustrated in Fig 1 left) with some additional modules (e.g., adding some modules between the student and teacher). 

2. The experiments are not enough to support the advantage of the proposed method. The compared methods are quite old. It is stated that: Note that most recent KD approaches (such as Beyer et al. (2022), Yang et al. (2022a)) focus on one single application such
as image classification or recommendation, and assume teacher and student share similar tasks. This does not make much sense because the authors could compare with those recent approaches on (same) single applications individually.

3. The presentation is poor. The paper introduces too many notations without a clear rule, in other words, the notations seem to be introduced in an arbitrary manner. For example, the subscripts g and h are used to indicate the student and the teacher, respectively. But in other places, h is used to indicate higher hidden layers of a neural network. This leads to weird notations such as H_{h_{h}}^h, a total of four h's! It is hard to get the meaning of a notation by looking at it. I spent a difficult time in reading the paper. In my opinion, many notations and equations are actually unnecessary. The proposed method is simple, and there is really no need to use such a complicated and tedious manner to describe it. 

4. Some technical details are missing. For example, each iteration between the teacher and the student will result in three additional losses (the last three terms in the last equation in page 7). Then with N iterations, does it mean that we need add 3N additional losses? If yes, how should we set the weighting factors? For another example, the method part introduces an encoder-decoder pair for both student and teacher, but in Appendix, only two modules are described. Is the encoder-decoder pair shared by the teacher and the student?

### Questions
The first two points listed above.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a knowledge distillation approach for knowledge transfer from large scale pre-trained foundation models to specific downstream tasks. The approach leverages the design of encoder and decoder for better communication and to shorten the gap between teacher and student models。

### Strengths
1. The topic of distilling pre-trained knowledge to benefit the downstream tasks is important and practical.
2. The solution is building up interactive communication between teacher and student models by encoder and decoder is novel and quite interesting.
3. The results look reasonable.
4. The paper is clearly written and well presented.

### Weaknesses
1. The experiments on movie prediction only cover a narrow scope, and the teacher/student tasks are quite similar with student task is to predict movie from one genre. The results could be more convincing if more varied tasks are involved, and if the "gap" between teacher and student is larger. Specifically, the current setup where the student model is trained on a single genre from the same dataset as the teacher limits the generalizability of the findings. It is unclear if the proposed method would be effective when the student task involves a completely different data distribution or a different modality altogether. For example, evaluating the approach on a task like sentiment analysis or text summarization, where the input and output spaces are significantly different from movie recommendations, would provide a more robust assessment. Furthermore, the current experiments do not explore the performance of the method when the student model is trained on a dataset with significantly less data than the teacher model, which is a common scenario in real-world applications.

2. The approach makes sense but quite straightforward by adding teacher receiving messages. It's worth more discussion on insights of this effect to the teacher model (if not frozen). The paper would benefit from a more in-depth analysis of how the proposed encoder-decoder architecture affects the teacher model's representation space, especially when the teacher model is not frozen. It is not clear how the backpropagation of the student's loss through the encoder-decoder to the teacher model influences the teacher's learned representations. A visualization or quantitative analysis of the teacher's representation space before and after the distillation process would be valuable. Additionally, the paper should discuss whether the proposed method leads to any degradation in the teacher model's performance on its original task, and if so, how to mitigate this issue.

### Questions
Same as above.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In their paper, the authors present a novel technique for knowledge distillation that leverages an interactive communication process. This approach draws inspiration from Osgood-Schramm's two-way communication model and employs communication encoders and decoders. Additionally, the authors introduce three supplementary loss functions to guarantee the desired behavior of the distillation process. To assess the efficacy of their method, they conduct experiments on four different datasets, covering two distinct tasks: movie recommendation and image classification. The results of these experiments demonstrate that this interactive distillation process can lead to performance enhancements.

### Strengths
1. The incorporation of Osgood-Schramm's model into the knowledge distillation process is novel and interesting.
2. The introduction of three new loss functions helps to realize the desired interactive distillation process.
3. The paper has a well-crafted structure and easy to follow.

### Weaknesses
The paper has several limitations that need to be addressed:

1.  **Limited Comparison Baselines:** The study only compares the proposed method with four baseline approaches. To provide a more comprehensive evaluation, it is advisable to consider more advanced knowledge distillation techniques and include a comparison with state-of-the-art models in the field. For instance, [a], 

2.  **Limited Tasks:** The paper only explores two specific tasks, which may not represent the full spectrum of potential applications for the proposed approach. Expanding the scope of evaluation to cover a broader range of tasks would provide a more robust assessment.

3.  **Insufficient Comparison with IAKD:** While the paper introduces a novel approach, it does not adequately differentiate it from Interactive Knowledge Distillation (IAKD). A clear comparison highlighting the advantages and distinctions between the proposed method and IAKD is needed to help readers understand the contribution.

4.  **Underwhelming Performance:** The reported performance metrics, such as RMSE and accuracy in Table 3 and 4, do not appear to be competitive when compared to state-of-the-art results. The ablation study also suggests that the new losses (L_MC and L_SC) do not significantly improve performance. For more up-to-date results on the datasets, it is recommended to refer to sources like [RMSE on ML100k](https://paperswithcode.com/sota/collaborative-filtering-on-movielens-100k) and [Cifar-10](https://paperswithcode.com/sota/image-classification-on-cifar-10) to provide a clearer context for your results.

Addressing these issues will help strengthen the paper and provide a more comprehensive and competitive assessment of the proposed approach.

[a] Radhakrishnan, Adityanarayanan, et al. "Transfer learning with kernel methods." Nature Communications 14.1 (2023): 5570.

### Questions
1. How dose this approach perform on natural language processing tasks such as text classification, token classification, question answering, etc. Further investigation on these NLP tasks is essential to assess the adaptability and effectiveness of the proposed method in a broader range of applications.
2. How is the approach compared with the most recent knowledge distillation methods? To establish the novelty and competitiveness of the proposed method, it is crucial to benchmark it against recent state-of-the-art knowledge distillation techniques, considering various datasets and evaluation metrics.
3. How do you determine w_1, w_2, w_3? The determination of the weights, namely w_1, w_2, and w_3, is not clearly elucidated in the paper.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
