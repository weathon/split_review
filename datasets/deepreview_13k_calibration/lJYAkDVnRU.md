# Context-Aware Meta-Learning

- Decision: Accept
- Avg Score: 5.50
- Scores: 5, 5, 6, 6

## Abstract
Large Language Models like ChatGPT demonstrate a remarkable capacity to learn new concepts during inference without any fine-tuning. 
However, visual models trained to detect new objects during inference have been unable to replicate this ability, and instead either perform poorly or require meta-training and/or fine-tuning on similar objects.
In this work, we propose a meta-learning algorithm that emulates Large Language Models by learning new visual concepts during inference without fine-tuning. 
Our approach leverages a frozen pre-trained feature extractor, and analogous to in-context learning, recasts visual meta-learning as sequence modeling over datapoints with known labels and a test datapoint with an unknown label.
On \num{8} out of \num{11} few-shot image classification benchmarks, our approach---without meta-training or fine-tuning---exceeds or matches the state-of-the-art algorithm, P>M>F, which is meta-trained on these benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper addresses a gap in the field of visual meta-learning, where models have traditionally struggled to learn new visual concepts during inference without fine-tuning, a capability that Large Language Models (LLMs) like ChatGPT have demonstrated in the textual domain. The authors introduce a novel meta-learning algorithm inspired by the in-context learning of LLMs. This approach treats n-way-k-shot image classification as a sequence modeling over known labeled data points and an unknown test data point.

### Strengths
1. The paper is well-written.
2. The problem studied in this paper is interesting and valuable.
3. The theoretical work of this paper is sufficient, which improves the value of the paper.

### Weaknesses
1. The authors utilize the CLIP model to encode both images and labels. An area of potential exploration is why they didn't attempt to encode context and images directly, especially using datasets like MSCOCO. Specifically, the paper lacks a clear justification for why the label encoding is performed separately from the image encoding, especially given the availability of paired image-text data in datasets like MSCOCO. This raises concerns about the optimality of the chosen encoding strategy and whether a joint embedding space could lead to better performance.
2. In the experiments, CAML's performance on out-of-domain tasks is notably weak. This might be primarily due to the treatment of unseen categories, which are uniformly encoded as "Unknown [class] Embedding". The paper does not adequately address the limitations of this approach, particularly how it impacts the model's ability to generalize to novel categories not seen during training. The uniform encoding of unseen classes may be a significant bottleneck, preventing the model from leveraging any potential semantic relationships between seen and unseen classes.
3. The study lacks ablation experiments for its various modules, and there's an absence of quantitative analysis for hyperparameters. The paper does not provide sufficient evidence to support the design choices of the different modules. For example, the impact of the transformer architecture, the specific choice of the ELMES label embedding, and the number of layers are not explored. Furthermore, the absence of a hyperparameter sensitivity analysis makes it difficult to assess the robustness and generalizability of the proposed method.

### Questions
Please see the Weaknesses

### Soundness
3 good

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
The paper introduces a new “universal meta-learning“ setup that “avoids meta-training on the train/validation splits of meta-learning benchmarks or fine-tuning on the support set during inference.” Instead, the paper attempts to recast meta-learning as a sequence modelling problem, where meta-testing on new tasks is analogous to in-context learning in large language models. The proposed approach CAML, context-aware meta-learning, uses CLIP image representations, together with one-hot label encoding dubbed as “Equal Length and Maximally Equiangular Set (ELMES) encoding,”  to represent each in-context learning example. The base sequence model is a Transformer encoder. It is trained to predict the query class label given in-context examples that are comprised of labelled support examples and a query example. The model is pre-trained on ImageNet-1k, Fungi, MSCOCO, and WikiArt and evaluated on 11 meta-learning benchmark datasets. Empirical results show that the proposed approach outperforms other “universal meta-learning“ baselines on 15 of 22 evaluation settings.

### Strengths
1. The paper is well-motivated on the need for in-context learning by drawing analogies with large language models. I also liked the analysis in Fig. 2, which illustrates how dynamic in-context examples impact representation learning
    
2. Theoretical analysis of the “Equal Length and Maximally Equiangular Set (ELMES) encoding” presents an interesting analysis of label symmetry and permutation invariance in meta-learning.
    
3. The paper presents competitive empirical results on various meta-learning baselines.

### Weaknesses
1. Novelty: the paper does not discuss previous work that also formulated meta-learning as a sequence, or set, modelling problem [1, 2]. The problem formulations in [1, 2] are highly similar to the proposal in this paper, except for architectural differences in implementation. This weakens the novelty of this paper.

2. The dichotomy between “meta-training“ and ”universal meta-learning”: the paper attempts to make the distinction between ”universal meta-learning” and "meta-training" in that the proposed CAML approach does not perform “meta-training“ or “fine-tuning on the support set.“ Instead, ”universal meta-learning” only performs pre-training. However, I think this dichotomy is not well-defined. Pre-training in the CAML fashion can be understood as learning across many different tasks in the pre-training dataset, i.e., meta-training, and in-context learning can be understood as performing implicit gradient descent based on the in-context examples. This dichotomy also implicates the comparisons in empirical results as CAML was mostly compared with other “universal meta-learning“ methods, i.e., ProtoNet, MetaOpt, and MetaQDA.

### Questions
1. Please summarize the novelty of this paper in relation to [1, 2].
    
2. Please respond to Weakness 2: The dichotomy between “meta-training“ and ”universal meta-learning.”
    
3. Please elaborate on how the transformer encoder is implemented and the rough scale of parameters it has.
    
4. Please elaborate on the pre-training dataset of CAML in “we pre-train CAML’s Transformer encoder on few-shot image classification tasks from ImageNet-1k.” How many examples are included in the pre-training set? Note that one of the benchmarks, miniImageNet, is a subset of ImageNet. Would this pretraining dataset result in task leakage?
    
5. Please elaborate on how the ProtoNet baseline is implemented. Is it trained on the same pre-training dataset but with the ProtoNet loss objective?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a meta-learning algorithm that learns new visual concepts during inference without fine-tuning. The method performs well on several benchmark datasets.

### Strengths
1. The paper draws a new perspective for meta-learning: learning to classify a query from a context of support set, imitating the way in LLMs. 
2. The framework is straightforward and clean. The reason (proved theoretically) for using the specific ELMES embedding is presented well.
3. Extensive experiments and analysis are provided.

### Weaknesses
Apologies in advance I am not an expert in meta-learning. But I still have the following questions:
1. What is the unknown class embedding initialization for the ELMES Class Encoder?
2. As discussed by the authors themselves in section 5.3, the number of classes need to be known in advance and the frozen encoders limit the learning ability. However in my view, the need of number of classes is an inherent problem in few-shot learning. But finetuning more modules could be further discussed.
3. There is a lack of experimental details (especially training details).

### Questions
See Weaknesses.

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
This work introduces a novel meta-learning algorithm that allows visual models to learn new concepts during inference, mimicking the capabilities of LLMs such as ChatGPT. The technique utilizes a static pre-trained feature extractor and treats meta-learning similarly to sequence modeling with labeled and unlabeled data points. When evaluated on 11 benchmarks, the proposed method, without any meta-training or fine-tuning, outperformed or matched the leading P>M>F algorithm in 8 of those benchmarks.

### Strengths
**Intriguing Research Question:** This paper delves into a significant question in meta-learning. The authors note that meta-learning traditionally involves pretraining, meta-learning, and fine-tuning. However, their approach seeks to bypass meta-learning and fine-tuning by transforming the learning process into a sequence modeling task and applying the in-context learning objective function.

**Rigorous Numerical Performance:** The paper's data shows the model's performance to be both impressive and robust.

**Novel ELMES Class Encoder:** The class embedding presented here appears to be quite innovative. I've noticed no other usage of this type of class embedding in in-context learning in NLP or VLM literature unless other reviewers bring up some status quo. This is also in alignment with some recent studies on Arxiv that indicate that class embeddings might be unnecessary, as arbitrary words, numbers, or first names can be used to label images (see [2]).

### Weaknesses
I will provide the paper's weaknesses in the following. 
- The concept of using the ICL objective function to pre-train a transformer model isn't a new one [1]. Unlike [1], which pre-trained a transformer from scratch within a meta-learning framework, this paper adapts the pre-training objective to Clip image embeddings, which doesn't significantly enhance novelty. The adaptation of the ICL objective to pre-trained CLIP embeddings, while practical, does not represent a substantial theoretical advancement over existing methods that train the transformer from scratch. The core idea of sequence modeling for meta-learning remains similar, and the use of pre-trained embeddings primarily offers computational efficiency rather than a novel approach to the meta-learning problem itself.
- The primary innovative aspect highlighted in this paper is the ELMES Class Encoder. While this feature is intriguing, it narrows the scope of innovation in the study. The focus on a specific class encoder, while potentially effective, limits the broader impact of the work. The paper's contribution is heavily concentrated on this single component, and it would be beneficial to see more exploration of how this approach interacts with other aspects of the meta-learning framework, or how it could be generalized beyond the specific ELMES encoding.
- Some claims in the paper lack experimental backing. For instance, the assertion that the ELMES Class Encoder upholds label symmetry and is invariant to the permutation of demonstrations isn't convincingly proven with data. The paper claims permutation invariance and label symmetry, but lacks sufficient empirical evidence to support these assertions. It would be beneficial to see experiments that specifically test these properties, such as varying the order of demonstrations and permuting class labels to observe the impact on model performance. Without this data, it is difficult to fully assess the validity of these claims.
- The mathematical explanations in Section 4 are challenging to follow. A clearer, more comprehensible presentation of this section would be beneficial. Until then, I'm relying on other reviewers to verify the accuracy of the mathematical derivations presented.

### Questions
- Could the authors elaborate on what they consider to be the primary innovative contribution of their study?
- It would be beneficial if the authors could include experiments to demonstrate the label symmetry and permutation invariance capabilities of the demonstrations as claimed.

[1]. General-Purpose In-Context Learning by Meta-Learning Transformers, NeurIPs 2022

[2]. Small Visual Language Models can also be Open-Ended Few-Shot Learners, Arxiv 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
