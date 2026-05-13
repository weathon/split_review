# Graph Neural Networks for Learning Equivariant Representations of Neural Networks

- Decision: Accept
- Scores: 6, 8, 8

## Abstract
Neural networks that process the parameters of other neural networks find applications in domains as diverse as classifying implicit neural representations, generating neural network weights, and predicting generalization errors.
However, existing approaches either overlook the inherent permutation symmetry in the neural network or rely on intricate weight-sharing patterns to achieve equivariance, while ignoring the impact of the network architecture itself.
In this work, we propose to represent neural networks as computational graphs of parameters, which allows us to harness powerful graph neural networks and transformers that preserve permutation symmetry.
Consequently, our approach enables a single model to learn from neural graphs with diverse architectures.
We showcase the effectiveness of our method on a wide range of tasks, including classification and editing of implicit neural representations, predicting generalization performance, and learning to optimize, while consistently outperforming state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work builds new neural networks that process other neural network parameters, by processing the computation graphs of the data neural networks. They do this processing via graph neural networks and graph transformers. Their models can then process htereogeneous architectures, as opposed to previous equivariant models. Experiments are conducted on several tasks involving processing neural networks.

### Strengths
1. The method can handle different nonlinearities, residual connections, and sizes of neural network.
2. The graph framework is flexible, as it allows different types of base model, e.g. the GNN and Transformer that they consider in this work.
3. Many types of empirical evidence, which shows the benefits of the method. The learned optimization experiments are particularly interesting.

### Weaknesses
1. While probe features improve performance, they are giving privileged information that is not quite in the same learning regime as other related works, which only take in parameters. With enough probe features, you are essentially inputting the original MNIST image into your neural network. The use of probe features, especially when they are derived from the input data itself, introduces a potential confound. It is unclear how much of the performance gain comes from the graph-based method itself versus the additional information provided by the probes. This makes a direct comparison with methods that operate solely on network parameters difficult. The authors should provide a more detailed analysis of the impact of the number of probe features and their nature on the overall performance.
2. Many claims of invariance or equivariance to permutation symmetries, without any proofs.

### Questions
1. Why do the MNIST dilation numerical results differ so much from those in the Zhou et al. paper? They achieve about .070, whereas you achieve about .02.
2. Could you report how many probe features are used in each of your experiments?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new approach to designing neural networks that process the parameters of other neural networks. This is achieved by representing the input neural network as a graph. In doing so, a graph neural network can operate on the input graph while respecting parameter permutation symmetries.

The neural network is converted to a graph by the introduction of a neural graph representation. This neural graph representation is related to the computation graph, but is more compact in some cases. Neural graph representations are designed for MLPs, CNNs, and residual networks. As part of the neural graph representation, the papers introduce novel node and edge features that improve the expressivity of the graph neural networks.

The proposed method is evaluated over a diverse set of experiments: classifying implicit neural representations, predicting network generalization, and learning to optimize. Across all settings, the proposed method significantly outperforms the evaluated baselines.

### Strengths
The proposed method is novel. I also agree with the authors that it is an improvement over baseline methods in that this approach can handle multiple architectures with the same model and does not require bespoke layer design.

The paper is very well written and easy to understand. I was able to follow completely and feel that adequate detail was provided for me to reproduce the results. 

The empirical evaluation is thorough and conclusive. The proposed method gives a significant boost to performance over the baselines. The paper evaluates performance over several established tasks. There is a good amount of variety and error bars are included for all experiments, further establishing the consistent benefits. The authors also included full source code for their method and experiments.

I feel that the contributions of this work are significant overall. This is a nice approach to designing neural networks that process other neural networks, which alleviates some of the complexity in prior work.

### Weaknesses
The CNN graph construction is effective but feels quite hacky. To use the method, the user must first specify a maximum kernel size. While this is unlikely to be a problem in practice, because the kernel size of modern CNNs does not vary much, it is not obvious how to extend this to other network layers that exhibit parameter sharing. For example, attention layers share parameters over sequence length which may vary significantly more than kernel size. Moreover, other standard building blocks like normalization layers are not covered in this work and there is no clear recipe provided for designing the corresponding neural graph representations. This lack of a systematic approach to handling diverse layer types limits the general applicability of the method.

There is little theoretical justification for the proposed approach. Prior work proves the expressivity of their methods alongside their group equivariance properties. Neither of these are explored formally in this work. This makes it difficult to understand the fundamental properties of the proposed method and how it relates to existing approaches.

I consider the empirical results to be quite complete, but an ablation of the various design decisions introduced would be valuable. For example, I'd like to better understand how much value the probe features, non-linearity identification, positional encoding, and other components contribute to the overall performance. Without this, it's hard to determine the importance of each design choice and whether they are all necessary.

### Questions
- It is stated that the proposed neural graphs "ensure invariance to neuron symmetries". Are you able to outline how this might be proved?
- Related to the previous question, the authors write that "natural symmetries in the neural graphs correspond exactly to neuron permutation symmetries", is this a statement that can be formalized? It is not clear to me that this is a 1:1 correspondence for all graphs considered. However, it is stated that this can be shown (Sec 2.1).
- You observe that the baseline methods are able to perform equally well on the training loss, but fail to generalize as well (Sec 4.1). Why do you think this is? Did you explore adding regularization or similar to the baseline methods to help with generalization? I wonder if the probe features or other modifications are providing some of this benefit for the proposed method.


Minor comments:

- I thought the probe features is a very neat idea that, intuitively, adds a lot of expressive power to the proposed method.
- At the end of the introduction, it is written that the proposed method "outperforms state-of-the-art approaches by a large margin". I think perhaps this would be better quantified with some specific values.
- In Section 2.3, non-linearities are described as being added to the node features. Is this done via concatenation? And what is done when there is no activation?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper considers the task of creating neural networks that take other neural networks as input. This problem has been considered in the machine learning literature which often does not take into account the different symmetries of neural network parameters, or only considers simple and fixed architectures such as multi-layer perceptrons or convolutional neural networks (Navon et al., 2023; Zhou et al., 2023a). The paper extends those works and proposes a more flexible approach where different architectures of neural networks can be given as input their neural network (i.e. different number of layers, widths, non-linearities). The paper also considers other types of layers such as residual connections and normalizations that take respect permutation equivariance across the different layers.

### Strengths
In general, the paper is well motivated and easy to understand. The paper also shows strong improvement over baselines in three different tasks which are: INR classification of 2d images and style editing, predicting CNN performance and learning optimizers. In the supplementary material, an ablation study of the proposed probe features (that consider representations at different layers of the neural networks) is provided. I think that the paper is relevant to the machine learning community. It is a stepping stone to more general neural networks that take other neural networks as input.

### Weaknesses
Despite considering new types of layers (e.g. residual connections) compared to the literature, other types of layers such as multi-head attention layers are still missing. Moreover, only the MLP and convolutional layers have been tested in the experiments. The paper could be improved a lot if it experimentally showed that the other types of proposed layers can also help improve the performance of their model. 
The paper also does not discuss the expressive power of their approach compared to the baselines, nor how difficult it is to scale their approach to very large neural networks/graphs.

### Questions
Assuming that the architecture of neural networks is fixed during training and test, how scalable is the proposed approach compared to the baselines (Navon et al., 2023; Zhou et al., 2023a)? In particular, can the proposed approach consider the same size of neural networks as the baselines for a fixed maximum memory allocation? Or can the proposed approach consider even larger architectures than the baselines?

Is the expressive power of the proposed approach the same as the baselines?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
