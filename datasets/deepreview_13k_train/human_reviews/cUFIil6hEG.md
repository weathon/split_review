# Accelerating Training with Neuron Interaction and Nowcasting Networks

- Decision: Accept
- Scores: 6, 6, 6, 5

## Abstract
Neural network training can be accelerated when a learnable update rule is used \textit{in lieu of} classic adaptive optimizers (e.g. Adam). However, learnable update rules can be costly and unstable to train and use. Recently, \cite{jang2023learning} proposed a simpler approach to accelerate training based on weight nowcaster networks (WNNs). In their approach, Adam is used for most of the optimization steps
and periodically, \textit{only every few steps}, a WNN nowcasts (predicts near future) parameters. We improve WNNs by proposing \underline{n}euron \underline{i}nteraction and \underline{no}wcasting (\ours) networks. In contrast to WNNs, \ours leverages neuron connectivity and graph neural networks to more accurately nowcast parameters.
We further show that in some networks, such as Transformers, modeling neuron connectivity accurately is challenging. We address this and other limitations, which allows \ours to accelerate Adam training by up to {50\%} in vision and language tasks.\looseness-1

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes to improve training, by leveraging out specific transformer strcture and representing it is as a Neural Graph to model connectivity. The weights of the model would then be encoded as features on the edges of the graph (the nodes corespond to neuron/activation).  Ideally,  isomorphic permutations of such graphs, 
should result in no-functional change to the model itself, thus capturing the underlying symmetries of the model. In contrast with earlier work, authors proposed a more fine-grained structure that accurately captures multi-headed-self-attention blocks, and thus allows them to improve performance of their meta-learning method. Once such graph is built authors leverage a combination of nodes and edge embedding, methods from GNN which are then translated to model updates..

### Strengths
I think the construction of the graph whose isomorphic permutations of nodes preserves the model functionality,  for transformer layer is neat and interesting.

### Weaknesses
I have two major concerns about the papers:
1. My main concern is that the experimental section contains only fairly trivial datasets (FashionMNist, Cifar-10), which are very far from anything reasonable these days, and the models authors consider for forecasting is limited to ~1M parameters, and many are 15K params,  which is barely practical for the simplest tasks. I think for image tasks, showing reasonable performance on something like ImageNet is
a must.  On the other hand authors run their training procedures for thousands of steps, which seems an overkill  for simple problems like this (Gradient Descent for Fashion Mnist for instance can converge in ~100 steps).  On the other hand experiments on Liama are not convincing because it is a well  known fact that it is often easy to speed up initial convergence, but the end result can still be significantly worse than slower algorithm. To demonstrate performance gains on these tasks authors should run at least run ablation study with different learning rates of the original model and show that they all converge (hopefully their method still shows the improvement).

2) The actual algorithm descriptions has very little detail what exactly their meta-learning algorithm does, even when reading the  appendix  carefully. Most of the detail is in section 4.2. In particular having at least a basic definition of GNN layers. Given that it is the crux of the paper, i think it should be carefully expanded and explained. I think the graph-construction section, is fairly well written, but it is very much unclear how it is then translated into actual meta-learning algorithms, as best as i could tell authors use some black-box message passing algorithms to come up with the new update, but i think that section would benefit greatly from expansion. 

3) Some discussion about optimality of their graph construction would be nice, but it is a minor comment.

### Questions
1. How are  the gradients are fed into the NiNo algorihtm? It is part of V^w? 
2. What are the nodes features? 
3. Was there any ablation study done for AdamW in Liama3 style architecture particularly around using different learning rates.

### Soundness
2

### Presentation
2

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
This paper introduces a novel approach for accelerating the training of neural networks. This technique called NiNo builds upon the concept of Weight Nowcaster Networks (WNNs), which periodically predict future parameter values thus speeding up optimization. However, in contrast to WNNs, NiNo leverages the inherent network structure by incorporating neuron connectivity using graph neural networks. This allows the model to achieve more accurate prediction of future parameters and leads to faster training. The authors also address challenges in modeling neuron connectivity, particularly in Transformers, and demonstrate NiNo's effectiveness in accelerating Adam optimization in various vision and language tasks.

### Strengths
1. The paper is sufficiently well written and is fairly accessible.
2. The proposed approach is sufficiently sound and novel. Even though it can be seen as a combination of two existing techniques (WNNs and an improved GNN model weight representation), this paper still contains a number of non-trivial innovations. For example, among other things, the authors make a number of logical steps improving on a previously published graph topology for multi-headed self-attention.
3. Experimental results appear to be promising. When fully realized the proposed technique could potentially be quite impactful for training modern large models including large language models. Even 10-20% improvements in training speed could be of large practical significance.

### Weaknesses
1. Some discussions could perhaps be improved upon to be even more clear. For example, while being sufficiently understandable, Section 4.1 could still be clarified further. Figure 2 is also difficult to interpret in its current form. Color coding takes time to digest.
2. The training method is fairly computationally expensive as the authors collect on the order of $10^6$ checkpoints. To be practical, this initial computational investment should be compensated by the future computational wins from utilizing a more efficient optimizer. Early results seem to paint an optimistic picture and suggest that trained models generalize to much larger underlying models and novel datasets and tasks. However, most current practical LLMs start at around 1B parameters, which still leaves at least 1 to 2 orders of magnitude from the current 111M models the authors experimented with.

### Questions
1. How could one bridge the gap between current experiments and practically interesting large model sizes (1-100B parameters)? Would generation of multiple future steps (various values of $k$) present a major obstacle? What about stacked feature representations that gather information from $c$ weight instances?
2. I could have missed this discussion, but what would happen if one decoupled the number of steps between predicting model weights and the size of the history used to make this prediction (both currently chosen to be $c$ if I am not mistaken)? It would seem that there are roughly three time hyper-parameters (at least locally): (a) how frequently do update predictions; (b) how many past states to use for making these predictions (lower would be more advantageous); (c) how far ahead to predict (larger would be more advantageous).

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
3

### Summary
The paper introduces NiNo, a method that improves WNN by utilizing graph neural networks (GNNs). Experiments on relatively small datasets demonstrate that NiNo achieves superior performance compared to the WNN baseline.

### Strengths
1. The paper is well-motivated. It is an improved version of WNN by integrating GNN.
2. The experiments cover different tasks including language modeling and image classification tasks.

### Weaknesses
1. It is unclear if training multiple models during meta-training is practical for real-world applications, where typically only a limited number of models are trained. The paper does not adequately address the computational overhead of training 1000 models for meta-training, especially considering that in many practical scenarios, only a few models are trained. This raises concerns about the applicability of the method in resource-constrained environments.
2. The generalization performance of NiNo should be further tested. The largest test case is 100 M models on small dataset like Wikitext-103. It may not fully represent NiNo's capabilities in broader applications. The experiments do not sufficiently explore the performance of NiNo on larger models or more complex datasets. The current evaluation is limited to relatively small models and datasets, which may not be representative of real-world scenarios where models often have billions of parameters and are trained on massive datasets. This lack of evaluation on larger scales makes it difficult to assess the true potential of NiNo.

### Questions
1. I notice that there are some strange performance jumps in Figure 6. Training loss periodically jumps/spikes for NiNo variants. Could the authors clarify the reasons behind these fluctuations?
2. How is NiNo or WNN applied during inference stage? Specifically, do you forward NiNo k steps and set the network weights to the output of NiNo while retaining the optimizer states? Further details on the inference process would improve clarity.
3. Could the authors provide details about the computational costs of the meta-training process?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes a novel approach to accelerate the training of neural networks by using Neuron Interaction and Prediction (NiNo) networks to predict future parameter changes, thereby reducing the number of iterations required by traditional optimizers such as Adam. This approach shows significant speed-ups on visual and language tasks while maintaining low memory overhead. The theoretical analysis and experimental results of the paper support the effectiveness of this method.

### Strengths
The method proposed in the paper has significantly improved compared to the existing technology in multiple benchmark tests, especially in reducing the number of training iterations.

### Weaknesses
Hyperparameter tuning: The paper mentions the k-decay strategy, but does not discuss the selection and tuning of hyperparameters in detail. It is recommended that the authors provide more analysis on the impact of hyperparameter tuning on model performance.

Computational resource consumption: Although the paper mentions the memory and time overhead of NiNo, it does not provide a direct comparison with existing methods. It is recommended to add analysis in this regard, especially on resource consumption on large-scale datasets and large models.

### Questions
The paper mainly focuses on the performance improvement of specific tasks, but lacks discussion on the generalization ability of the model on unseen tasks. It is recommended to increase the evaluation of the model's generalization ability.

### Soundness
3

### Presentation
2

### Contribution
3
