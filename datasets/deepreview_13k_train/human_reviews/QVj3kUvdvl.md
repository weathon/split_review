# Unsupervised Model Tree Heritage Recovery

- Decision: Accept
- Scores: 5, 8, 8, 6, 6

## Abstract
The number of models shared online has recently skyrocketed, with over one million public models available on Hugging Face. Sharing models allows other users to build on existing models, using them as initialization for fine-tuning, improving accuracy and saving compute and energy. However, it also raises important intellectual property issues, as fine-tuning may violate the license terms of the original model or that of its training data. A Model Tree, i.e., a tree data structure rooted at a foundation model and having directed edges between a parent model and other models directly fine-tuned from it (children), would settle such disputes by making the model heritage explicit. Unfortunately, current models are not well documented, with most model metadata (e.g., "model cards") not providing accurate information about heritage. In this paper, we introduce the task of Unsupervised Model Tree Heritage Recovery (Unsupervised MoTHer Recovery) for collections of neural networks. For each pair of models, this task requires: i) determining if they are directly related, and ii) establishing the direction of the relationship. Our hypothesis is that model weights encode this information, the challenge is to decode the underlying tree structure given the weights. We discover several properties of model weights that allow us to perform this task. By using these properties, we formulate the MoTHer Recovery task as finding a directed minimal spanning tree. In extensive experiments we demonstrate that our method successfully reconstructs complex Model Trees.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
Motivated by the fact that many models have been publicly released, this paper proposes a new problem: studying the relationships between these models. Specifically, the authors aim to build a tree data structure where directed edges connect a parent model to other models that have been directly fine-tuned from it (its children). For each pair of models, this task requires: (i) determining if they are directly related, and (ii) establishing the direction of the relationship. Assuming that all models within the model tree share the same architecture, the authors propose a method based on the distance between model weights. Experiments demonstrate the performance of the proposed method.

### Strengths
Originality: This paper addresses a new problem: estimating the relationship between models and their fine-tuned versions. However, the significance of this problem for open models is debatable; see the weakness for the detailed comments.  

Simple approach: The proposed approach based on the distance of model weights is simple. But this is based on a well-known fact that fine-tuning makes small weight changes.  

Writing: The clarity is mixed; some parts are easy to follow, but certain important sections, such as Section 4.2, are hard to understand.

### Weaknesses
Limitation 1: The proposed approach can only handle open models, as it relies on model weights. For important open models that have been fine-tuned, information about the pretrained models is often available at the time of release. For models without such information, one can infer relationships based on weight distance. However, it is unclear why this information is needed for all released models.

Limitation 2: The proposed approach constructs the model tree based on the weight distances between each pair of models and is thus limited to the case that all the models within a model tree share the same architecture. It can not be applied to other models that are obtained through distillation, etc.

### Questions
What is $\mu$ in eq. (3)? What is the pretraining stage in Figure 2 (I thought it is all about fine-tuning)? Overall, I found section 4.2 is hard to comprehend.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper targets to analyze the relation between models, aiming to shed light on which is fine-tuned from which model. This has also applications concerning copyright issues or more general licence concerns. Ths author introduces a method coined "Model Tree Heritage Recovery", which unravels the "parent-child" relations in a set of models. This method is unsupervised. Numerical examples are provided.

### Strengths
* Shedding light on the relation of models, in particular, in the LLM regime is crucial.
* The numerics are convincing.

### Weaknesses
 * Due to the importance of such a method for legal aspects, some theoretical underpinning should be given, which is currently missing.
* The running time of the method is not provided.

### Questions
see the weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper investigates the problem of finding the relationship between models from the model weights.

### Strengths
Please see the "Questions" section.

### Weaknesses
Please see the "Questions" section.

My review is as follows:

- I think this paper is well-written and investigates an interesting problem.

- The introduction mentions legal disputes over model authorship. Out of curiosity, are there any known examples of this kind of dispute?

- Could you please elaborate on this point? "Moreover, it can help identify models that resulted from the wrongful use of proprietary training data." It is not clear to me how the proposed method for determining model relationships could help with wrongful use of data.

- Could the method successfully find the relationship between a quantized version of a model and the full precision model? Were there quantized models in the dataset?

- The observation that the Directional Weight Score is monotonic with respect to the training steps is interesting but perhaps not concrete enough. I would expect this to strongly depend on the specific learning rate, number of training steps, and perhaps some other hyper parameters used in training. In my opinion, identifying when this observation tends to hold and when it does not would be important in order to solidify the findings of this paper.

- Some follow-up questions on the monotonicity observation: Does this observation generalize across many different model types? On what kind of models has it been verified so far?

### Questions
My review is as follows:

- I think this paper is well-written and investigates an interesting problem.

- The introduction mentions legal disputes over model authorship. Out of curiosity, are there any known examples of this kind of dispute?

- Could you please elaborate on this point? "Moreover, it can help identify models that resulted from the wrongful use of proprietary training data." It is not clear to me how the proposed method for determining model relationships could help with wrongful use of data.

- Could the method successfully find the relationship between a quantized version of a model and the full precision model? Were there quantized models in the dataset?

- The observation that the Directional Weight Score is monotonic with respect to the training steps is interesting but perhaps not concrete enough. I would expect this to strongly depend on the specific learning rate, number of training steps, and perhaps some other hyper parameters used in training. In my opinion, identifying when this observation tends to hold and when it does not would be important in order to solidify the findings of this paper.

- Some follow-up questions on the monotonicity observation: Does this observation generalize across many different model types? On what kind of models has it been verified so far?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MoTHer Recovery, a method to automatically trace relationships between shared neural network models by analyzing their weights. The approach uses weight distances and distributions to determine which models were derived from others, creating a tree-like structure of model relationships without requiring training data or documentation. The authors validate their method through experiments and provide a dataset for future research in model heritage recovery.

### Strengths
- The paper writing is good, and presentation is clear

- The paper introduces a novel and timely problem formulation (model heritage recovery) that hasn't been systematically addressed before

- It develops an unsupervised approach that doesn't require access to training data and leverages inherent neural network weights to infer relationships

- It provides empirical validation across different fine-tuning scenarios and demonstrates effectiveness on the Stable Diffusion model family

### Weaknesses
 - The paper doesn't address how to handle models with mixed heritage (e.g., models trained on merged weights from multiple parents) or partial weight sharing. Specifically, the method's reliance on a single parent model assumption limits its applicability in scenarios where models are created through more complex combinations of existing models. For instance, models created using techniques like 'model soups' or other weight averaging methods would likely not be accurately represented by the tree structure produced by the proposed method.

- The clustering approach might not scale well to web-scale model repositories - needs more analysis of computational requirements. The paper lacks a thorough analysis of the computational complexity of the proposed method, particularly the pairwise distance calculation and clustering steps. This is a significant concern, as the method's practical utility depends on its ability to handle large model repositories efficiently. The paper should provide a more detailed analysis of the time and space complexity of the method, and explore potential optimizations for large-scale applications.

- It can be interesting to understand how different learning rates or optimization strategies during fine-tuning affect the reliability of weight-based relationships. For example, will aggressive optimization or pruning obscure these signals? The paper does not investigate the sensitivity of the method to different fine-tuning parameters. It is crucial to understand how variations in learning rates, optimizers, and other training hyperparameters affect the weight-based relationships. For example, aggressive optimization or pruning techniques might significantly alter the weight distributions, potentially making it difficult to trace model heritage.

### Questions
- What is the computational complexity of applying this method to large model repositories? Could you provide runtime analysis for different scales (e.g., 100, 1000, 10000 models)?

- How does the method handle cases where models have been fine-tuned with different learning rates or optimization strategies? Is there a threshold where the relationship becomes undetectable?

- For models with mixed heritage (e.g., merged weights from multiple parents), how does the method determine the primary relationship? Can it detect multiple parent relationships?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors introduce the task of Unsupervised Model Tree Heritage Recovery(Unsupervised MoTHer Recovery) for collections of neural networks.

### Strengths
The paper is well-written and introduces the history of the model tree well.

### Weaknesses
The paper is good as an introduction paper. However, it seems to lack novelty in the methodology part. The dense matrix construction (6) is not new.





### Questions
1. You seem to use the existing graph algorithm and the model is also not new. Are there any novel points in the graph algorithm parts?
2. Could you clarify the cluster method using (1) and (2)? Do you have any guarantee of this way? Why use (1) and (2) not other criteria? In addition, is the cluster method reliable in this task? Can you use other alternative ways?

### Soundness
3

### Presentation
3

### Contribution
3
