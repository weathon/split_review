# Metanetwork: A novel approach to interpreting ANNs

- Decision: Reject
- Scores: 1, 3, 3, 3

## Abstract
Recent work on mechanistic interpretability, which attempts to demystify the black box of artificial neural network (ANN) models through analytical approaches, has made it possible to give a qualitative interpretation of how each component of the model works, even without using the dataset the model was trained on. However, it is also desirable from the viewpoint of interpretability to understand the ability of the entire model; and considering the previous studies on task embedding, the ability of the entire model should also be represented by a vector. In this study we propose a novel approach to quantitatively interpreting an unseen ANN's ability based on relationships with other ANNs through obtaining a low-dimensional representation of ANNs by training a "metanetwork" that autoencodes ANNs. As a first-ever attempt of such an approach, we train a "metanetwork" to autoencode ANNs consisting of one fully-connected layer. We demonstrate the validity of our proposed approach by showing that a simple k-Nearest Neighbor classifier can successfully predict properties of the training datasets of unseen models from their embedded representations.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a meta network to represent the network ability to perform a task. In particular the authors propose a method to predict an unseen task of an ANN. The main motivation of the authors seems to be the task embedding approach on which the reasoning behind this work is based. Unlike to original method, the proposed method attempts to represent model's task as vector or as a result of the constructed meta network.

### Strengths
The concept Idea is interesting

### Weaknesses
I am not sure if I understood the paper correctly. The authors want to represent the hidden ability of network by a network of networks that intends to represent the component networks representation. However, the proposed model is poorly explained, no experimental data is described nor the parameters selection.

It is very hard to assess the paper results as the only representation is given using T-SNE and two feature confusion matrices representing the ability of the meta-network to distinguish between audio and video features. As such the meta network does not directly assess the ability of the specific neural network but rather simply meta-classify the modality of the features. I think this is quite different from what the authors claim in the paper.

### Questions
Is feature representation the same as ability representation??

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present an approach to encode the weights of a single-layer ANN. They use autoencoders to encode these weights without using the training dataset. Furthermore, they employed KNN to validate the encoding of the network weights.

### Strengths
1- The paper is well-written, with few formatting issues.

2- I like the idea of encoding model weights without using the training dataset, enabling work on models where access to the training data is not possible.

3- The experiments are adequate to support the claims for "very simple single-layer ANN" (though they are limited to this type of model).

### Weaknesses
There are several weaknesses in the paper:

1- The paper claims that encoding the model's weights improves interpretability, but it doesn't explain how it achieves this. It doesn't clarify how the model makes decisions or whether it reveals any general biases the model has learned. The only thing I can see from here is how close two models are. Specifically, the paper lacks a clear mechanism for translating the encoded weight vectors back into insights about the original model's behavior. The authors do not demonstrate how the encoded representation can be used to understand the model's decision-making process, such as identifying which input features are most influential or what patterns the model has learned. The claim of improved interpretability is therefore unsubstantiated.

2- Although the authors claim that the proposed approach can be used with any model, it appears that this may not be the case. It's unclear which layer to encode, and if we attempt to encode multiple layers, we would need different encoders due to varying input sizes. Even with the option of ReLU in section 5.3, it may be impossible for large networks. Representing an entire large network with a single-layer network doesn't seem feasible. The method's applicability to deep networks is questionable, as the authors do not address the challenges of encoding multiple layers with varying dimensions and activation functions. The paper does not provide a clear strategy for handling the complexity of multi-layered networks, which limits the generalizability of the proposed approach.

3- In practice, users typically train a network for a specific task they don't train hundreds of networks. Consequently, it's unclear how the encoder can be trained with very few weights. The paper does not address the practical limitations of training the meta-encoders when only a small number of models are available. The authors do not provide a clear strategy for training the encoders when the number of models is limited, which is a common scenario in real-world applications. The reliance on a large number of pre-trained models for encoder training is a significant limitation that needs to be addressed.

Minor formatting issues:

1- In the related work section, change "Indeed" to "indeed" in the sentence, "Those latent variables are indeed a concise representation."

2- In Section 4.1, tag the figure number instead of writing "Figure" so that readers can identify which figure you are referring to.

3- When tagging figures, use "Fig. 1" instead of writing "[1]" for better clarity.

### Questions
1- Can the authors provide more detailed clarification for this part:
"Therefore, if we infer the training dataset of the model using the feature visualization technique, without access to the dataset, we can obtain a low-dimensional vector representation of the model, using an approach similar to MeLA."

2-Why is it necessary to use two different meta encoders? Can we use only one of them, such as either the "unit-wise" meta-autoencoder or the "inter-unit" meta-autoencoder only?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
- The authors approach interpretability by training a meta network, that embeds ANN in one single fully-connected layer (motivated by task embedding). Specifically, they introduce meta-autoencoders to embed ANNs in the low-dimensional latent space.
- This vector-representation of network can be used to compare different networks, e.g., to predict the modality and dataset they were trained on. The authors show that the accuracy for ability prediction, i.e., modality and dataset prediction, is superior to the one without meta network.

### Strengths
- The authors approach a relevant topic, i.e., network intepretability. 
- The authors suggest an interesting idea, which is to find low-dimensional representations of networks that are easily comparable.

### Weaknesses
 - The methodology section is hard to follow and very confusing. It would be helpful to have a Figure in the beginning (introduction already), to explain the intuition behind the idea and to clearly explain the role of each component (model to interpret, meta-encoder, meta-autoencoder, Knn classifier, ...")
- Figure 1 has no proper caption, which makes it hard to read and understand the figure.
- I was surprised that models are only trained for 1 epoch. Some explanation would be helpful, as this is uncommon.
- Poor experiment section: There is no comparison with other approaches. The relation of the tasks (predicting modality, predicting dataset) to intepretability is unclear. The connection between predicting these properties and gaining insights into the internal workings of the networks is not well established. It's unclear how accurately predicting the modality or dataset helps in understanding the learned representations or the decision-making process of the network.
- Nitpick: there are a couple of typos:
  - sec 2: “Those latent variables are Indeed…”
  - Sec 4.1: “(Figure)”
  - Sec 4.2.1 “the all 20 classes”
  - Sec 4.2.2 “each dataset as v:”  should be “a:"

### Questions
- are the original models (to be interpreted) trained on the full datasets? The dataset splitting by class label (see sec 4.2) is only done to train the meta network, right?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to train an autoencoder model whose input is the weights of trained DNN models. The authors empirically show, using a simple model, that it is possible to predict the task modality using the embedding space obtained by the autoencoder.

### Strengths
- A meta-learning approach for understanding neural networks.

### Weaknesses
 - I could not understand the novelty of this work compared to existing works, such as TASK2VEC or MODEL2VEC mentioned in the paper, which also try to embed tasks or models.
- The datasets and models used in the experiment are too simple to have practical implications. The use of basic autoencoders on toy datasets limits the generalizability of the findings. It's unclear how this approach would scale to more complex architectures or real-world datasets.
- Even if modality or dataset-id could be predicted by the proposed autoencoder, I'm not sure what we can say about interpreting ANNs. The link between the embedding space and actual interpretability of the neural networks remains unclear. Predicting the task modality doesn't necessarily provide insights into the internal workings of the network.

- In Section 4.4, it seems to me that there is nothing to train with a k-NN classifier when the meta-encoder is frozen. What do you mean by training here?

- Figure 1 suggests that the model to be interpreted is also an autoencoder. However, such an assumption is not clearly stated in the manuscript. It is also unclear why the encoder part of this model should be analyzed.

- It is unclear why we need unitwise and interunit meta-autoencoders. The rationale for this two-stage approach is not well-justified. Why not directly encode the entire weight matrix, or use a different approach for feature extraction?

- In Section 4.1: Figure -> Figure 1?

- In Section 4.3: "1 shows" -> "Figure 1 shows"?

- Formatting in references is incomplete. For example, some papers do not have a place of publication.

- (This is not a question, just a comment.) There are several works that deal directly with DNN weights as input, such as [1], which could be used to analyze trained DNN models more efficiently.

### Questions
- In Section 4.4, it seems to me that there is nothing to train with a k-NN classifier when the meta-encoder is frozen. What do you mean by training here?

- Figure 1 suggests that the model to be interpreted is also an autoencoder. However, such an assumption is not clearly stated in the manuscript. It is also unclear why the encoder part of this model should be analyzed.

- It is unclear why we need unitwise and interunit meta-autoencoders.

- In Section 4.1: Figure -> Figure 1?

- In Section 4.3: "1 shows" -> "Figure 1 shows"?

- Formatting in references is incomplete. For example, some papers do not have a place of publication.

- (This is not a question, just a comment.) There are several works that deal directly with DNN weights as input, such as [1], which could be used to analyze trained DNN models more efficiently.

[1] Navon et al., Equivariant architectures for learning in deep weight spaces, ICML'23.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor
