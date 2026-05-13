# Finding Symmetry in Neural Network Parameter Spaces

- Decision: Reject
- Scores: 5, 3, 3, 1

## Abstract
Parameter space symmetries, or loss-invariant transformations, are important for understanding neural networks' loss landscape, training dynamics, and generalization. 
However, identifying the full set of these symmetries remains a challenge. 
In this paper, we formalize data-dependent parameter symmetries and derive their infinitesimal form, which enables an automated approach to discover symmetry across different architectures. 
Our framework systematically uncovers parameter symmetries, including previously unknown ones. 
We also prove that symmetries in smaller subnetworks can extend to larger networks, allowing the discovery of symmetries in small architectures to generalize to more complex models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper formalizes and studies parameter space symmetries, both data-invariant and data-dependent. The formalization includes an elegant formulation using Lie Algebras and its applications. The infinitesimal form of the symmetries allows an automated discovery method to find data-dependent parameter space symmetries which may be intractable otherwise, in general.

### Strengths
The parameter space symmetries of neural networks is an active topic that is of interest for the scientific understanding of deep learning and also for improving the efficiency of large models. This is a theory paper that formalizes data-dependent parameter symmetries in a way that allows automated discoveries of even non-linear symmetries. Although the applications given in the paper are very toy, this is the first paper I see in the direction of finding data-dependent param. symmetries and I find it interesting. 
Specifically, 
- the paper is very well-written
- theorems are clear, I did not find any typos in a quick reading 
- the application to deep networks and layer-wise partitioning of the parameter space is novel (to my knowledge)
- Theorem 3.1 generalizes that of Moskalev et al 2022

### Weaknesses
Many citations are missing. Applications are toy. Figures could be made better. See below for the details. 

Data-invariant parameter space symmetries and the role of activation function are well understood at this point in the literature. See the citations below. [2] prunes out parameter space symmetries and reduces the size of the over-parameterized model without loosing functional equivalence. 

ReLU symmetries 

[1] Petzka, Henning, Martin Trimmel, and Cristian Sminchisescu. "Notes on the symmetries of 2-layer ReLU-networks." Proceedings of the northern lights deep learning workshop. Vol. 1. 2020.

More generally, linear + even activation functions, i.e., max(x, 0) = |x|/2 + x/2 

[2] Martinelli, Flavio, et al. "Expand-and-Cluster: Parameter Recovery of Neural Networks." arXiv preprint arXiv:2304.12794 (2023).

Symmetries of the large networks are often inherited from the symmetries of the small networks. A particular form of this has been known for a while. That is, the parameter-symmetries coming from neuron splitting, i.e., $a \sigma(w^T x) \rightarrow \mu a \sigma(w^T x) + (1-\mu) a \sigma(w^T x)$. This operation preserves the network function (on all data points) and also maps critical points to other critical points in a larger parameter space. See [3] for a classic reference and [4] for a larger symmetry group that only preserves the function space (by considering the global minima manifold). 

[3] Fukumizu, Kenji, and Shun-ichi Amari. "Local minima and plateaus in hierarchical structures of multilayer perceptrons." Neural networks 13.3 (2000): 317-327.

[4] Simsek, Berfin, et al. "Geometry of the loss landscape in overparameterized neural networks: Symmetries and invariances." International Conference on Machine Learning. PMLR, 2021.

Is this what was studied with regard to shallow networks, as shown in Figure 1 (a), or does the formalization here cover a broader class of symmetries? The latter is probably not possible since neuron splitting and zero-neuron addition give a complete description of the parameter-space symmetries when using population loss and input distribution that has full support (see Theorem 4.2, Simsek et al 2021)

Figures are hard to interpret. What activation function is used in Figure 2? Is it ReLU? How should we interpret this generator? What would be the expectation?

Figure 3 would need labels to be readable. Which one is W1, which is W2? What is the data used? Please include how the generator depends on the data. These figures should look more structured when using infinite data (population loss) -- does the automated method work in this case?

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work studies how to discover parameter symmetries in neural networks (?)

### Strengths
Parameter symmetries are interesting and perhaps fundamental objects to study in deep learning

The paper reads like a nice chapter in a textbook, and is not difficult to understand

### Weaknesses
I think there are quite a few problems with this work. 

1. The theoretical results are either not novel or trivial. Theorem 3.1 is essentially a restatement of Noether's theorem, which, in the context of deep learning has appeared many times (including the references the authors). Proposition 4.1 is, I feel, trivial and obvious. Of course, the degree of obviousness is matter of personal taste. But, if the authors really want to show that this result is nontrivial, they would have given more novel and interesting applications of it. The two examples are, I am afraid to say, almost trivial if not already known. Btw, this type of analysis is first pioneered in https://doi.org/10.1016/S0893-6080(00)00009-5, for example, and the authors should have given it a reference 

2. The relationship between each part is weak. For example, Section 4 does not rely on either section 3 or section 5.

3. On top of section 3/4 lacking significant relevance and novelty, I think the main contribution comes from section 5, where the authors invents an algorithm to identify symmetries. However, this part is only illustrative and lacks any serious evaluation. Extensive analysis is needed to make this part of the contribution solid

### Questions
NA

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper considers the problem of identifying symmetries in neural network parameter spaces using an automated approach. This approach involves modeling group actions with a neural network and minimizing a loss which would vanish if the action was loss-invariant and satisfied the necessary axioms. The paper uses this method to recover known symmetries in a 2-layer network with a homogeneous activation function, but also identifies new symmetries which are dependent on data in 2 and 3-layer networks with sigmoid and tanh activations. The paper additionally proves how symmetries found in smaller networks can also be used to understand symmetries in larger networks.

### Strengths
The problem of identifying parameter symmetries in an automated manner is relevant and interesting. I believe that the generality of this approach could be a major strength, as it in principle could be applied to any architecture.

The discovery of data-dependent symmetries with this method is also interesting and original.

The paper is generally well-written. Concepts are explained well and the motivation is well-established.

### Weaknesses
While the approach could be promising, its utility is only demonstrated for very small neural networks and it remains unclear whether the method would work at a more practical scale. Although the paper argues that larger neural networks contain symmetries from smaller ones, it is also acknowledged in the paper that there can be new emergent symmetries in larger networks. I would not expect that symmetries induced from smaller networks would provide a representative picture of the larger network's symmetries, and I am concerned that the paper underplays the significance of these emergent symmetries.

The challenge of selecting the appropriate number of generators and their dimension when applying this approach was not discussed. I am concerned that the difficulty of tuning these hyperparameters may pose a problem when applying the paper’s proposed method to architectures where the symmetries are not well understood. 

Minor notes:

-L with subscript “Lie_deriv” on line 297 may be a typo meaning to say “invariance”

-In line 341, “training” should be “trained”

### Questions
It would reassure me to see the performance of the paper’s method on larger networks.

I would also like to know more about the approach for determining the number of generators and their dimension and whether determining them is a problem in practice or not.

My current opinion is that the broad problem that the paper is working towards is relevant and the work done is novel. However, I unfortunately believe that the paper does not deserve acceptance primarily due to the approach’s usefulness not being adequately demonstrated in a more practical setting.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper proposes a learnable group representation framework based on group axioms to discover data-dependent symmetries present in neural network parameters.

### Strengths
1. Novel perspective that discovers implicit symmetries in neural networks induced by the dataset.
1. Flexible group representation learning by utilizing the group axioms.

### Weaknesses
1. The paper significantly lacks an experimental analysis that verifies the effects of the method.
1. I am strongly suspicious whether the method really works or not.

### Questions
No question except the things written in the weakness.

### Soundness
2

### Presentation
1

### Contribution
2
