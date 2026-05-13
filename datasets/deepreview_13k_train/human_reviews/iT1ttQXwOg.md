# Equivariant Deep Weight Space Alignment

- Decision: Reject
- Scores: 6, 6, 6, 6

## Abstract
Permutation symmetries of deep networks make basic operations like model merging and similarity estimation challenging. In many cases, aligning the weights of the networks, i.e., finding optimal permutations between their weights, is necessary. Unfortunately, weight alignment is an NP-hard problem. Prior research has mainly focused on solving relaxed versions of the alignment problem, leading to either time-consuming methods or sub-optimal solutions. To accelerate the alignment process and improve its quality, we propose a novel framework aimed at learning to solve the weight alignment problem, which we name \ourmethod{}. To that end,  we first prove that weight alignment adheres to two fundamental symmetries and then, propose a deep architecture that respects these symmetries. Notably, our framework does not require any labeled data.  
We provide a theoretical analysis of our approach and evaluate \ourmethod{} on several types of network architectures and learning setups. Our experimental results indicate that a feed-forward pass with \ourmethod{} produces better or equivalent alignments compared to those produced by current optimization algorithms. Additionally, our alignments can be used as an effective initialization for other methods, leading to improved solutions with a significant speedup in convergence.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper attempts to solve the weight alignment problem by introducing a novel deep learning framework. The proposed DEEP-ALIGN method is fast and produce high quality alignment results after the pretrained process. DEEP-ALIGN does not require any labeled data but only depends on input network weight vectors. In addition to a theoretical analysis of the approach, experimental results support that a feed-forward pass with DEEP-ALIGN produces better or equivalent alignments compared to those produced by current optimization algorithms.

### Strengths
1. DEEP-ALIGN approach does not require labeled data but only the trained weight vectors.
2. DEEP-ALIGN performs on par or outperforms optimization-based approaches while significantly reducing the runtime or improving the quality of the alignments.
3. DEEP-ALIGN maintains good performance as an extra initialization step for Sinkhorn method on OOD data.
4. The theoretical analysis ensures the existence of the approximate solution that can be represented by DEEP-ALIGN architecture.

### Weaknesses
1. This method has to be pre-trained in advance. For experiments conducted on MNIST and CIFAR10, 8000 shallow networks are used to train the model to achieve the claimed performance. For deeper networks that are more common in nowadays deep learning task, this number may grow fast and the training cost can be unacceptable. Also, this paper does not provide experimental results about the relationship between the complexity of weight vectors and the scale of needed training data.

2. The real world applications for this method are unclear due to long the pre-train time. It seems that the traditional methods can compute the weight alignment much more effectively unless a ton of weight vectors need to be aligned so that the inference phase of DEEP-ALIGN dominates. What scenarios feature such characteristics?

### Questions
1. What is the definitions of $\rho_1$ and $\rho_2$ in the section 2 Preliminaries?
2. Is the assumption that the minimizer $k$ in equation (2) is unique reasonable? Any argument that such cases would be rare in practice?
3. I'm curious about the generalization capability of the model. As mentioned in the paper, the model will be first trained on a dataset of weight vectors and then applied to unseen weight vectors. Is there any possibility that one pertained DEEP-ALIGN model can work for networks of slightly different architectures? Due to the expensive cost of training phase, it can be helpful if one pertained model can work for more scenarios.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work presents a learned algorithm to find permutations that align the weights of two networks (e.g. for federated learning, continual learning, model merging). The key innovation of the algorithm is it uses a weight space network to turn input weight vectors into embeddings which can then be aligned as in previous works (via distance in a metric space and Hungarian algorithm). This weight space network is trained using the Sinkhorn method to make the process of finding permutations differentiable.

### Strengths
This approach appears to improve upon and is complementary to existing approaches, in that it aims to give better permutations than weight matching and is faster than fully learned permutations (termed *Sinkhorn* in this work), but can also be combined with the *Sinkhorn* algorithm. Proofs of exactness and equivalence to activation matching guarantee that this method will be as similarly reliable as activation alignment, where the *Sinkhorn* algorithm does not have the same guarantees. The ability to change the objective function for training the deep weight network makes the algorithm more expressive, akin to *Sinkhorn* algorithm, e.g. so that it can directly optimize for linear connectivity rather than the $L_2$ norm between weights. Some of the results (e.g. table 2) look promising.

### Weaknesses
The main limitation I see is that results are not given for sufficiently large/complex models/tasks. For the barrier results, it is known (e.g. in Ainsworth et al. or Jordan et al.) that deeper networks are harder to align so that they are linearly connected, whereas easier networks (e.g. 3-layer MNIST networks) are relatively trivial to align. Also, it's not clear if Deep-Align reliably beats activation matching (which is still relatively fast and scalable), or if Deep-Align + Sinkhorn can beat weight matching + Sinkhorn.

The major methodological innovations could use much more explanation. The DWSNet would benefit from a full detailed description, given that it is central to the presented approach and based on a very recent work that may not be well known. The Siamese structure and why it guarantees equivariance to transposition should in particular be fully described.

### Questions
How does this method scale (re. accuracy and computation time) to larger networks (e.g. VGG models) and residual networks?
How does weight-matching + Sinkhorn compare with Deep-Align + Sinkhorn?

### Soundness
3 good

### Presentation
2 fair

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
The authors propose a data-driven method to perform weight matching between neural networks. It aims to solve the assignment problem by training a Siamese architecture to perform activation matching and produce permutation matrices. The architecture is trained on generated pairs of weight vectors, where one vector is a noisy, randomly permuted version of the other, as well as on unlabeled pairs.

The authors embed their method into a group theoretic framework and provide proofs for several properties of their architecture: it is equivariant to permutation and is exact, meaning that it, under mild assumptions, converges to an optimal solution if a zero error solution exists.

The method is evaluated on several weight matching benchmarks for image classification tasks and implicit neural field networks. It consistently outperforms previous work while being orders of magnitude faster.

### Strengths
- The presented method is grounded in theory, the authors provide useful theorems and the framework is technically sound
- The method applies existing concepts for data-driven assignment solvers to the weight matching problem, which is a novel contribution
- The method is well evaluated and results clearly outperform previous methods while being much faster
- The paper is mostly well-written and presented

### Weaknesses
 - The network that maps from weight embedding to activation space and its connection to stage 1 is unclear (see below for questions).
- The networks generalization capabilities are limited. In order to outperform previous methods, the architecture has to be trained on different weights of the same network architecture, solving the same task as during inference. It still performs reasonably well on slight OOD weights though.

- The explanation of the mapping from weight embeddings to activation space is insufficient. It is not clear how the network uses information from both weights and biases to output the new set of weight and bias representations. The paper states that the output biases, and consequently the predicted permutations, are a function of the input weights, but the mechanism for this is not clearly explained. The connection between the input weights and the final permutation prediction is not intuitive, and the role of the first stage of the architecture remains unclear.

### Questions
- I don't fully understand the network mapping from weight embeddings to activation space. If the network just maps onto the bias vectors, the input weights do not have any influence on the estimated permutation anymore, would that be correct? This seems to be unintuitive to me and I would like the authors to clarify.
- Also, if my interpretation is correct, what is the point of feeding the weights $w$ to the network at all and not just use the bias? What is the purpose of the first stage of the architecture?

------------
I thank the authors for the provided clarifications - the method is clear to me now. In total, my score remains as it is.

### Soundness
4 excellent

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a learning-based framework that learns to predict the optimal weight alignment between two neural networks. The proposed architecture is equivariance to permutation symmetry of the input neural networks. The authors prove that the approach can approximate the Activation Matching algorithm and guarantees to produce the correct alignment when a perfect alignment exists. At inference time, the framework aligns unseen network pairs without additional optimization. Experiment results show that the proposed approach is faster and produces better alignment than optimization-based approaches. The predicted alignment can also be used as initialization for optimization-based approaches to improve their alignment quality.

### Strengths
-	The idea of incorporating symmetries of the weight space is both natural and novel, and its effectiveness is clearly demonstrated in experiments.
-	An efficient method for finding weight alignment is an important problem in model merging, with potential applications in real-time merging in federated learning and weight-space clustering. It also allows more efficient experimentations in understanding the loss landscape of deep networks.
-	The paper is easy to follow. Writing is clear and concise.

### Weaknesses
-	The proposed framework requires new training for every new input neural network architecture, even for minor changes such as adding or modifying the size of a layer. 
-	It is not clear how to choose the weights for the linear combination of the three loss functions in Section 4.2. Also, as shown in Appendix F, the two unsupervised loss functions are not always aligned, and it is not clear which loss to include before training. Finally, the evaluation metrics, barrier and AUC, are based on model merging tasks, but the supervised loss does not seem to help on these metrics directly.
-	The practical contribution would be more convincing if the authors can demonstrate the framework’s effectiveness in applications that require weight alignment.

### Minor: 
-	$\rho_1$ and $\rho_2$ in the first paragraph of Section 2 are not defined. Are they representations?
-	Section 4.1: might be better to state what $\theta$ is somewhere.
-	Figure 5: The “Weight Matching” and “DEEP ALIGN + Weight Matching” have very similar colors.

### Questions
-	Does the exactness property (proposition 5) apply to test data as well?
-	How do the three losses interact with each other? Does the two unsupervised loss provably help improve the supervised loss? 
-	Figure 3: Why does the loss decrease on the interpolation around $\lambda=$ 0.1 or 0.9, especially in CIFAR10 CNNs?
-	Why is incorporating equivariance beneficial to the model performance? It is intuitively clear that weight alignment methods should respect the symmetry of the neural networks, but there does not seem to be evidence of the link between incorporating equivariance and improved performance.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
