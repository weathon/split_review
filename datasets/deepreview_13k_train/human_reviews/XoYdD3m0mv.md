# Deep Linear Probe Generators for Weight Space Learning

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Weight space learning aims to extract information about a neural network, such as its training dataset or generalization error. Recent approaches learn directly from model weights, but this presents many challenges as weights are high-dimensional and include permutation symmetries between neurons. An alternative approach, \textit{Probing}, represents a model by passing a set of learned inputs (probes) through the model, and training a predictor on top of the corresponding outputs. Although probing is typically not used as a stand alone approach, our preliminary experiment found that a vanilla probing baseline worked surprisingly well. However, we discover that current probe learning strategies are ineffective. We therefore propose Deep Linear \textbf{Probe} \textbf{Gen}erators (ProbeGen), a simple and effective modification to probing approaches. ProbeGen adds a shared generator module with a deep linear architecture, providing an inductive bias towards structured probes thus reducing overfitting.
While simple, ProbeGen performs significantly better than the state-of-the-art and is very efficient, requiring between $30$ to $1000$ times fewer FLOPs than other top approaches.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
In this paper, the authors introduce ProbeGen, a deep linear method designed for probing model data in weight space learning. They begin by demonstrating empirically that probing is an effective approach for weight space learning, although it has limitations and room for improvement. Building on these findings, they propose ProbeGen as an enhancement and subsequently validate its effectiveness through a series of experiments.

### Strengths
- This work addresses the novel and intriguing field of weight space learning, aiming to tackle the significant challenge of simplifying optimization within this domain.
- The proposed method ProbeGen is simple, easy to follow, and yet effective.
- The authors empirically demonstrate the motivation behind ProbeGen, providing interesting insights.
- The paper is well-written and easy to follow.

### Weaknesses
 - The experimental part is limited. From an empirical-oriented paper, I expect the experimental section to be more comprehensive. For instance, the effectiveness of ProbeGen is shown only on INRs overlooking equivariant tasks in weight space learning like domain adaptation [1], alignment [2], editing [3], and more. The lack of experiments on tasks that require weight space manipulation, such as those involving equivariance, significantly limits the scope of the empirical validation.
- The authors mentioned that ProbeGen could be used for processing high-dimensional inputs, however, the experimental section focuses on small-scale INRs instead of modern architectures. The absence of experiments on larger, more complex architectures, such as ResNets or Transformers, makes it difficult to assess the scalability and practical applicability of ProbeGen. It is unclear if the method's performance would hold up when applied to models with millions of parameters.
- It would be interesting to see what is the upper bound of ProbeGen w.r.t number of probes. The authors used a max number of 128 probes what will be the performance if we will use 1024 probes for example? Can we match the image space performance? The paper lacks a thorough investigation into the relationship between the number of probes and the performance of ProbeGen. The choice of 128 probes seems arbitrary, and it is not clear if this is an optimal number or if further improvements could be achieved with more probes. It is also unclear how the performance of ProbeGen compares to image-space performance.
- The authors failed to cite relevant works in the field of weight space learning [2,4,5,6].
- Not sure if it is intended but the supplementary material is missing.

### Questions
- Do the authors have a hypothesis as to why non-linear activation functions lead to poorer probe representations? Have the authors experimented with other non-linear activations besides ReLU activations discussed in lines 255-261?

- It would be interesting to try and enrich the probes by applying augmentations to the input like presented in [1,4].

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work addresses the task of learning in weight spaces, and introduces a probing-based method that passes a set of learnable inputs to a model and trains a simple network on top of the concatenated probe outputs. The authors first demonstrate that standalone vanilla probing performs very well, almost on par to state-of-the-art methods. They then extend the method by introducing a shared deep linear network module, and incorporate inductive biases towards structured probes. This module further increases performance by reducing overfitting, while being more efficient than other approaches.

### Strengths
The paper is well written and is quite easy to follow. The connections with binary code analysis and the corresponding insights are very useful towards more scalable weight-space methods. 

The proposed method reaches state-of-the-art performance with high computational efficiency. The authors provide a comprehensive set of ablation studies that offers significant insights on probing-based methods for weight space learning.

### Weaknesses
The proposed method cannot be used in weight-level tasks, such as editing neural network weights, which represents a large class of tasks in learning in weight spaces. The impact of this work would greatly increase if the authors include a more detailed discussion on why that is the case, and potential directions to alleviate this limitation.

It is unclear if the proposed method can be used to complement existing mechanistic approaches and result in a performance greater than either of the two components. See question 1.

The experiments on learned vs unlearned probes are very insightful. It is unclear, though, why the authors did not explore actual unlearned images as probes, potentially in-distribution. For example, a small subset of the training (or validation) set used only for probing. What is the impact of using real images for probes?

Deep linear networks are introduced as a means to introduce regularization and reduce overfitting. Have the authors explored other common regularization methods, e.g. adding weight decay, or dropout? Is the reduced expressivity of the network an advantage here? If so, it is not very clear why that is the case.

The authors often mention the terms "training dataset classification", "extract information about its training dataset", or variants. These terms seem quite confusing. Do they refer to INR classification tasks? The manuscript could benefit from some rephrasing in these instances.

As the number of probes increases, it approaches the size of the image for INRs, or the test set size for CNN generalization. In that case, probing in ProbeGen becomes almost trivial, since it is nearly identical to feeding the whole image to an MLP, or to running the CNN over the whole test set. In both cases, we can expect the performance monotonically increasing as a function of the number of probes. Is that assumption correct? Is there a sweet spot between efficiency and performance? An ablation study on MNIST/Fashion MNIST with increasing numbers of probes (up to the image size) that shows performance and FLOPS would be very useful here.

### Questions
[1] It seems intuitive that probing approaches are complementary to mechanistic approaches. Can the proposed method be combined with existing mechanistic approaches (e.g. Neural Graphs)? Does ProbeGen increase the performance of these methods? An ablation study on whether deep linear generators with structured input probes boost mechanistic approaches would be very useful, and would further increase the impact of the proposed method.

[2] The experiments on learned vs unlearned probes are very insightful. It is unclear, though, why the authors did not explore actual unlearned images as probes, potentially in-distribution. For example, a small subset of the training (or validation) set used only for probing. What is the impact of using real images for probes?

[3] Deep linear networks are introduced as a means to introduce regularization and reduce overfitting. Have the authors explored other common regularization methods, e.g. adding weight decay, or dropout? Is the reduced expressivity of the network an advantage here? If so, it is not very clear why that is the case.

[4] The authors often mention the terms "training dataset classification", "extract information about its training dataset", or variants. These terms seem quite confusing. Do they refer to INR classification tasks? The manuscript could benefit from some rephrasing in these instances.

[5] As the number of probes increases, it approaches the size of the image for INRs, or the test set size for CNN generalization.
In that case, probing in ProbeGen becomes almost trivial, since it is nearly identical to feeding the whole image to an MLP, or to running the CNN over the whole test set. In both cases, we can expect the performance monotonically increasing as a function of the number of probes. Is that assumption correct? Is there a sweet spot between efficiency and performance? An ablation study on MNIST/Fashion MNIST with increasing numbers of probes (up to the image size) that shows performance and FLOPS would be very useful here.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper advocates for probing methods to solve tasks on the weight space of NNs. It first shows that naive probing performs as well as SoTA methods that operate directly on the weight space in discriminative tasks. Then, by analyzing the learned probs, the authors suggest an improved mechanism for learning the probs using deep linear networks which adds implicit regularization. The authors demonstrate the merits of their approach compared to baseline methods on two tasks, INR classification and image prediction errors. Several ablations are done to inspect different aspects of the method.

### Strengths
* The idea of using a deep linear network to obtain implicit regularization while guarding against potential overfitting is nice and original in that context.
* The proposed approach is extremely more efficient compared to methods that learn directly on the weights.
* The paper is written clearly and adequately. The authors empirically justify their design choices every step of the way and show other alternatives (such as learned vs unlearned probs, and the architecture decisions about the generator).
* The ablation study clears several ambiguities that arise while reading the paper, such as using non-linear generators and the importance of the inductive biases introduced into it.

### Weaknesses
 * The authors discussed frankly about the main limitations of their approach, which I agree with. In particular, there are some tasks on which it is not immediately apparent how to use linear probing, such as generative tasks. It may be valuable if the authors could come up with possible remedies for that, but I understand if they don't since it is beyond the scope of this work and maybe non-trivial.

* Experiments:
  * Section 5.2 demonstrates the importance of deep linear classifiers compared to non-linear ones. The main issue, as I understand it, is overfitting. But, I wonder why didn't you try explicit regularization schemes to benefit from a more expressive network? I believe that an experiment of that flavor is missing. Specifically, exploring L1 or L2 regularization, or even dropout, could provide a more complete picture of the limitations of non-linear probing and the benefits of the proposed deep linear approach. It's not clear if the linear classifier is simply avoiding overfitting due to its limited capacity, or if there is a more fundamental reason for its superior performance.
  * Given the main advantage of this approach (i.e., agnostic to symmetries and fast) and given its limited applicability, I believe the submission can be made much stronger by evaluating ProbeGen on complex data, and on bigger networks. Both are limitations of current models that operate on the weights directly. For instance, INR classification or generalization error of images from ImageNet. The current experiments are limited to relatively small models and datasets, which might not fully reveal the potential of the proposed method in more challenging scenarios. It would be valuable to see how the method scales to larger models and more complex datasets, such as those used in state-of-the-art computer vision research.
  * Related to my previous comment - I can see why on MNIST and even CIFAR small number of probs is sufficient to get good results. However, I speculate that it will not be the case for more challenging datasets (e.g., ImageNet or datasets of fine-grained classification such as CUB). Perhaps additional experiments can clarify that ambiguity. The paper would benefit from an analysis of how the number of probes scales with the complexity of the dataset and the size of the model. This is crucial for understanding the practical applicability of the method.
  * Exact experimental details are missing to reproduce the results, e.g., what optimizers were used? Did you apply regularization? What is the architecture of the classifier? Also, it is not clear whether data augmentation was used for baseline methods (as it tends to improve the results). The lack of these details makes it difficult to verify the results and compare them with other methods.

* Some parts of the submission can be improved. Specifically, 
  * There should be some background on INRs and the tasks involving them. A brief introduction to INRs and their applications would make the paper more accessible to a broader audience.
  * It is not clear how exactly Kendall’s $\tau$ was used to evaluate the generalization error. A more detailed explanation of how Kendall's $\tau$ is applied in this context would be beneficial, including the specific data points used for the calculation.
  * It is not clear how exactly to run the code in the submission (there are no explanations about how to obtain the data, some files seem to be missing, etc.)

### Questions
.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper considers the problem of weight space learning, in which a learner is tasked with predicting the properties (e.g., accuracy) of an input (trained) neural net. The paper makes the distinction between two approaches for weight space learning: (1) Mechanistic approaches, which operate on the input weights (without running the model), and (2) Probing approaches, which represent models by their responses to a set of inputs. The paper champions probing approaches and proposes a simple yet effective approach in which the probes (model inputs) are learned using a deep linear generator. On a set of small-scale benchmarks, the authors show the proposed method outperforms both probe-based and mechanistic baselines, with improved computational efficiency.

### Strengths
- The paper is well-structured and easy to follow.
- The method is well motivated through a set of empirical observations.
- The proposed approach is simple yet effective.

### Weaknesses
My main concern lies with the experimental setup, which is limited to small-scale datasets and includes only two baselines. In addition, all experiments are performed on images with no additional modalities. This restricts the generalizability of the findings. I would expect a broader and more diverse set of experiments (in terms of scale and modalities) from a purely empirical paper. Please consider adding additional experiments with larger models, higher-dimensional inputs, or different modalities.

Additional limitations:
1. The approach is not applicable for an important and large set of weight space tasks, namely weights-to-weights tasks, e.g., INR editing, domain adaptation, sparsification, etc.
2. The provided empirical evaluation is limited to fairly low-dimensional input spaces. I assume probing approaches will be more efficient in low-dim spaces, so it will be beneficial to provide results for more challenging setups with higher-dimensional input spaces (e.g., point clouds) or input spaces with more challenging structures (e.g., graphs).
3. Similarly, results for additional data modalities will be beneficial and will strengthen the empirical soundness.
4. Also, including additional baselines like [1, 2] would be beneficial.
5. While the authors analyze the computational cost, showing clear benefits compared to the GNN-based approach, it is not clear that the results will hold for larger models, as the approach requires forward and backward steps through the models.
6. The Appendix is completely missing, along with additional important information regarding implementation details, experimental setup, HPs, etc.

### Questions
- Have you tried comparing to using real images from the training dataset (for example, CIFAR10 images) as probes?
- It is not clear if you also used Conv layers for the INR tasks. If so, why does this make sense?

### Soundness
2

### Presentation
3

### Contribution
2
