# Continual Memory Neurons

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 5, 3

## Abstract
Learning with neural networks by continuously processing a stream of data is very related to the way humans learn from perceptual information. However, when data is not i.i.d., it is largely known that it is very hard to find a good trade-off between plasticity and stability, frequently resulting in catastrophic forgetting issues. In this paper, to our best knowledge, we are the first to follow a significantly novel route, tackling the problem at the lowest level of abstraction. We propose a neuron model, referred to as Continual Memory Neuron (CMN), which does not only compute a response to an input pattern, but also diversifies computations to preserve what was previously learned, while being plastic enough to adapt to new knowledge. The values attached to weights are computed as a function of the neuron input, which acts as a query in a key-value map, with the goal of selecting and blending a set of learnable memory units. We show that this computational scheme is motivated by and strongly related to the ones of popular models that perform computations relying on a set of samples stored in a memory buffer, including Kernel Machines and Transformers. Experiments on class-and-domain incremental streams processed in online and single-pass manner support CMNs' capability to mitigate forgetting, while keeping competitive or better performance with respect to continual learning methods that explicitly store and replay data over time.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes continual memory neurons (CMNs) which is a key-value attention-based memory module that distributes the past memory into slots. A winner-take-all retrieval and forgetting mechanism is also proposed. When a single layer of CMN can achieve superior performance on online continual learning compared to baselines that use example buffers and replay.

### Strengths
- It is good that the authors discuss the relation of CMN to classic neurons, transformer networks and kernel machines.
- Experiments show that the network is significantly better at online continual learning compared to baselines that use example buffers and replay.

### Weaknesses
 - It seems that in the experiments the authors have only tried with a single layer of CMN, but the naming of “neuron” and the methodology suggests that it can be applied more widely across layers. It would be better to showcase the general applicability into multi layer CMNs. A single CMN can be achieved with a more standard online clustering algorithm.
- To continue with the previous point, a concern with applying CMN to multiple layers is that when the representations are not fully trained or in early layers, committing to the winner memory slot may hinder the learning progress, but more studies would be needed.
- The memory unit has resemblance to Ren et al. (2021) so it would be great to discuss its relations in the paper. Both works use a slot-based memory module based on input similarity. Both recycle the least used entry and create a new entry if the match strength is below a threshold.
- Hyperparameters selection of CMN seems like a burden. It would be great to show a list of hyperparameters and their optimal range for each task, and discuss how sensitive these values are.

### Questions
N/A

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The core contribution in this work is to introduce a mechanism for retrieval-augmented classification in a continual learning setting: It develops a key-value pair mechanism within NN layers so as to select the best memories per layer and utilize/update them.

I summarize the paper from a layerwise perspective as the mechanism until keys is shared across neurons.

The specific proposal is to replace every layer in the deep network from the following format:

A Linear Layer: $ f (x, W) = W^T.x$   where   $ x \in R^u , W \in R^{m \times u} $

to the proposed: 

A Continual Linear Layer: $\forall_i (M_i^T$sparse-softmax$_{top-δ}{(γ · sim(ψ(x), K)})) x$

where $M_i$ is memory of every neuron in the layer, $M_i, K \in  R^{m \times u}$, $ψ$ is a function, while $γ$ is temperature and $δ$ is the sparsity value. 

Notes:
- Every neuron has a distinct memory $M_i$
- Function $ψ$ chosen- identity
- Similarity metric ($sim$): cosine similarity for real experiments, RBF for 2D toy experiments
- $δ$ is a hyperparameter $\in {2, 5}$
- Extended to convolutional layers by considering each channel as a neuron

The design choice is in the selection/update mechanism for memories $M_i$:
- 1) Updating memories leads to forgetting: Ans) Select/update only the best memory $M_i[best]$ per layer to avoid interference (as keys are shared across neurons)
- 2) Avoid degenerate solutions (e.g. selecting the same key for all samples): Combination of the scramble and refresh key algorithm and online k-means like update to winning keys. 

Can the authors correct my summary if there is something incorrect/missing? I found the paper quite hard to read, hence tried to give a slightly different perspective here to check whether I understood the mechanism correctly.
[Minor updates based on author feedback]

### Strengths
S1) **Tackles an important problem, quite convincing motivation [Critical]**

 The proposed continual memory neurons is a general and intuitively quite an effective mechanism to tackle catastrophic forgetting, and is quite distinct from current efforts in continual learning.

S2) **Well engineered [Critical]**

The approach was quite well engineered, the design-mechanisms both reduce computational overhead while trying to improve forgetting.

### Weaknesses
W1) **Missing References and Comparisons [Critical]**
- Nearly a page discusses connections to kernel methods, Transformers and RELUs-- however these seem quite non-central to the proposed mechanism.
- The proposed mechanism is closest to retrieval augmented continual learning works, which are surprisingly not discussed. Please see: https://github.com/hyintell/awesome-refreshing-llms for exhaustive references.

Why: Retrieval-augmented CL seems the closest to this work, as they introduce alternative mechanisms of continual memory neurons. It seems critical to understand how the proposed mechanism differs from existing proposals, as this papers claims (rightly) to be a general mechanism applicable across continual learning settings. 
- I am specifically concerned about the mechanism of sparse selection + updates being better than alternative proposals.

W2) **Comparison between memory stored and images stored by MB [Critical]**
- The memory here is stored as weight matrices, which are inevitably smaller than storing images -- this in my opinion creates an unfair comparison. 
- This is because CMNs can effectively store more samples than compared approaches, effectively achieving higher performance.

Furthermore: The memory constraint is by equalizing (1) the MB of storage, and (2) too low 
- The proposed deep CMN networks (and comparisons) require higher GPU VRAM than the claimed available space on HDDs!

W3) **Too low absolute numbers on benchmarks to be meaningful, requires significantly better evaluation [Critical]**
I use MNIST-CI as an illustration to clearly show inadequacies in evaluation. 
- Using a Nearest Class Mean [1] classifier on raw-pixels(!) achieves >85% accuracy on MNIST-CI, whereas reported SOTA here is 78%!
- For larger datasets, one needs some degree of features beyond raw pixels, but similarly, CIFAR10 performance of 27% is astonishingly low a bar to outperform.
- Benchmarks in the referenced continual-retrieval augmented transformers would be good candidates to compare performance.

Note that I think the proposed mechanism might be really useful, however the current evaluations seem too under-powered to verify benefits of CMNs.

### Questions
Q1) **How do non-CMN methods perform with the RBF kernel in tthe moons/modes dataset? [Important]**
- Am I correct that the ψ(x) other than identity is only used in this scenario?
- What is the contribution of using the key-value pairing in CMN and RBF kernel for the task?
- Would equalizing the RBF kernel aspect significantly affect the performance gain of CMN method?

Q2) **Why are the results varying so much in MNIST-CI? [Important]**
- It is very strange to see 21.0 for ER-Random, 23.2 for MoE and 14.3 for GDumb but 70.3 for ER-Reservoir-Imbalanced. 
- Reservoir-Imbalanced sampling (Chrysakis & Moens, 2020) approximates random sampling as there is no imbalance to correct so they should have identical performance.

Overall, 14.3/21.0/23.2 on MNIST-CI seems suspiciously low performance despite the memory size being 100!

### Soundness
1 poor

### Presentation
2 fair

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes to change a regular weighted sum neuron to a more complex neuron where the weights are dynamically produced based on a set of key and memory vectors. The proposed neuron bears similarities to kernels and the attention mechanism. The authors then propose a learning mechanism based on winner-takes-all update as well as avoiding weak keys. Experiments on continual learning demonstrate the effectiveness of the proposed method.

### Strengths
(1) The proposed neuron is novel and insightful. 

(2) The proposed learning algorithm is sensible. 

(3) The experiment results demonstrate the effectiveness of the proposed method.

### Weaknesses
The main weakness is that the learning algorithm is ad hoc. It is not derived by minimizing a well-defined loss function. Specifically, the update rule for the memory keys seems arbitrary and lacks a clear theoretical justification. While the authors mention a winner-takes-all approach, the precise mechanism and its impact on the overall optimization landscape are not fully explained. The lack of a clear objective function makes it difficult to analyze the convergence properties of the proposed method or to compare it with other approaches that are derived from principled optimization frameworks.

The proposed neuron appears to be rather complex. Although the proposal is novel, the novelty is limited compared to the popular transformer model. The use of key and memory vectors, along with the dynamic weight generation, introduces significant computational overhead. While the authors draw a parallel to the attention mechanism, the specific differences and advantages over existing attention-based models are not thoroughly explored. It is unclear if the added complexity of the proposed neuron justifies the performance gains observed in the experiments, especially considering the potential for simpler alternatives.

### Questions
Is the proposed method related to the mixture of experts? 

Is it possible to introduce explicit latent variables to model the continual learning scenario?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose to develop a new type of neural-network neurons, termed Continual Memory Neurons (CMN), to address the catastrophic forgetting issue of lifelong learning. Specifically, learnable keys and memory units are introduced to parameterize the conventional weights of a neuron. Moreover, during lifelong learning, only top-δ activated keys and memory units are trained. Experiments on 2 simulated datasets, i.e., Modes and Moons, and 3 benchmark datasets, i.e., MNIST, CIFAR10, and NS-ImageNet, are conducted.

### Strengths
The presented techniques are likely novel, and the originality arises from the creative utilization of existing ideas for addressing new problems.

The research direction might be valuable for the lifelong learning community.

### Weaknesses
 The writing should be significantly improved. The current manuscript is not easy to follow.

The presented techniques are not presented with convincing theoretical justifications. For example, what's the motivation for using Eq. (6) to update the keys K? The connection to online K-means is not clearly established, and the specific form of the update rule lacks a strong theoretical basis. It's unclear why this particular update mechanism would guarantee parameter isolation and forward transfer, as claimed.

Strong statements are made without convincing justification. For example, in Abstract, "...we are the first to follow a significantly novel route..." This claim is not adequately supported by the current manuscript. The novelty needs to be more rigorously demonstrated by contrasting with existing approaches in the literature.

In Eq. (4), why "set to 0 all the other excluded components?" The concern is not addressed by simply stating that it prevents unwanted behaviors when all logits are less than 0. The issue is that setting the excluded components to zero after a softmax operation is not a standard practice and requires more justification. It's unclear what the effect of this operation is on the overall training dynamics and the gradients.

In the experiments, is a single data sample presented to the model at each time step? It seems in Figure 4 that each time step processes a new distribution (with many data samples)? The description of the experimental setup needs to be more precise. The current description is ambiguous and makes it difficult to understand the training procedure.

In Figure 5, it seems that CMN behaves differently on the 2-dimensional simulated datasets and the real-world imagenet dataset. Why? The explanation based on the dimensionality of the data is not sufficient. More detailed analysis is needed to understand why cosine similarity/dot product is more appropriate in higher dimensions and how this affects the behavior of CMN.

### Questions
Strong statements are made without convincing justification. For example, in Abstract, "...we are the first to follow a significantly novel route..."

In Eq. (4), why "set to 0 all the other excluded components?" What if all logits are less than 0?

How to select the hyperparameter $\delta$?

What are the insights in Section 2.1? How do the revealed connections with existing machine learning techniques contribute to the proposed CMN?

In the experiments, is a single data sample presented to the model at each time step? It seems in Figure 4 that each time step processes a new distribution (with many data samples)?

In Figure 5, it seems that CMN behaves differently on the 2-dimensional simulated datasets and the real-world imagenet dataset. Why?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair
