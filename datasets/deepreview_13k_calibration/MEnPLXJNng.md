# Riemannian Transformation Layers for General Geometries

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5

## Abstract
Recently, deep neural networks on manifold-valued representations have garnered significant attention in various machine learning applications. Several studies have attempted to generalize traditional Euclidean transformation layers, such as Fully Connected (FC) and convolutional layers, to non-Euclidean geometries. However, the previous approaches typically focus on a select few manifolds and rely on the specific properties of the target manifold. In this work, we propose a theoretical framework for constructing Riemannian FC and convolutional layers over general geometries, providing broader applicability. Utilizing this framework, we design convolutional networks across five distinct geometries of the Symmetric Positive Definite (SPD) manifold, as well as networks under two Grassmannian perspectives. Extensive experiments demonstrate that the proposed Riemannian convolutional networks significantly outperform existing SPD and Grassmannian networks.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work proposes a generalized Riemannian neural network by constructing a new linear layer and deriving several other constructions from it.

### Strengths
This work has some positive aspects

1. The theory is well motivated, and the derivations do not appear to be wrong to me.
2. The experimental results show a marked improvement over prior work in terms of empirical performance.

### Weaknesses
There are a few major weaknesses that prevent me from giving an accept rating for this paper.

1. The paper only compares on the SPD and Grassman manifold. Note that this paper is paper is proposing a "general framework" for constructing riemannian neural networks, so there should be an acknowledgement of other manifolds like hyperbolic space/sphere, which seem to be even more popular for experiments.
2. In my eyes, the paper does a bit of a disservice to prior work. For example, it is known from as early as Ganea that the gyro-multiplication/activation constructions are simple $\exp_0(f(\log_0(x))$ (where f is a standard linear or activation layer). If I remember correctly, this very premise was applied to more general geometries in the Skopek et al mixed curvature VAEs paper. If I also remember correctly (I believe I had derived this several years ago), the original SPDNet paper is effectively performing the same construction. It seems like a stretch to say the proposed FC layer is novel; rather, it would be more apt to say that the construction identifies a common thread in prior work while providing some references/examples of how this was done previously.
3. Building off of the previous points, beyond collecting some prior constructions under a common framework, the true contribution is the convolutional layer for practical purposes. The convolutional layer is not really a convolutional layer, but rather a linear layer between product manifolds $\mathcal{M} \to \mathcal{N}^d$. This does not seem morally right since convolution is defined in a separate way, and one can effectively view this as a hyperparameter/architecture change, which does not seem to be a good enough contribution.
4. One MAJOR GAP I see in the current construction is that there does not seem to be a mention of how to deal with activations/biases, which I looked for in the manuscript. If this is truly not talked about (which again, might be wrong since there are 32 pages of dense material where I can easily miss something in), then this seems to be a major problem. There needs to be a discussion of why the proposed construction does not simplify to $\exp_0(\mathrm{neuralnet}(\log_0(x))$, as is done in Ganea and Shizuma when they the introduce gyro-addition, which does not satisfy this form and breaks the $\exp-\log$ chain.

### Questions
Why is parallel transport denoted PP instead of something like PT?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a technique for building fully-connected and convolution neural networks on Riemannian manifolds. The proposed network architecture builds on linear layers derived from Riemannian MLR [Chen et al., 2024c], and illustrates its manifestations on SPD and Grassmannian manifolds. To validate their method, the authors present experiments on matrix classification tasks.

### Strengths
The proposed method can work generally on Riemannian manifolds, and does not rely on special structure such as gyrovector calculus. On the quantitative benchmarks, the method outperforms prior work on matrix classification.

### Weaknesses
 **Lack of Analysis**
Although the method seems to numerically out-perform prior work on matrix classification tasks, the paper should provide some explanation of why this may be true. The chosen baselines are known to be very sensitive to initialization and hyperparameters chosen, which make the numerical results difficult to interpret at face value. I would have liked if paper analyzed what exactly the model is learning. For example, it is surprising to see that Log-Euclidean metric seems to outperform the other metrics, even though it endows the SPD manifold with a flat structure. Does this mean that a flat structure is best for SPD matrix classification?  

Is there a theoretical explanation of why the proposed method may outperform prior work which use gyrovector calculus? 

**Other Riemannian Manifolds**
It would strengthen the paper to add experiments on other manifolds such as hyperbolic and spherical spaces. While the authors acknowledge their method’s inspiration from HNN++ [Shimizu et al., 2020], there are no experiments on hyperbolic space. It would have been interesting to see how the proposed method compares to the gyrovector calculus used in HNN++. One way to extend Riemannian projection layers to hyperbolic space is with horocycle projections. Prior work [A] have observed that horocycles can be used as an efficient feature map just like the Riemannian hyperplane projections proposed in this work.  

**Computational Cost**
The differences in computational cost seems significant with respect to the metrics used, due to the requirement of computing log and exponential maps. What is the compute time required for each method in Table 3? Do the methods vary much in parameters used and time required? For the proposed method, do the benefits of the added computational costs outweigh the drawbacks?

**Presentation**
It is not clear to me what the purpose of Section 7 is.

### Questions
- How does the computational cost compare between the different metrics used for the SPD tasks?
- How do you ensure that the input features are in a radius close enough to each layer’s base point so that the Log map is well-defined?
- Eq. 11 defines an inner product for a manifold via a linear isometry. Is there an example of this for SPD and Grassmannian spaces? Is there a canonical way to compute this isometry for general Riemannian manifolds?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors introduce a framework for constructing fully connected and convolutional layers in contexts where one wants to construct a deep network with manifold-supported data and/or outputs. The framework for deriving such layers is general and only requires that the input and output spaces are Riemannian manifolds. For experiments, the authors specialize to several different geometries on the symmetric positive definite cone and the Grassmanian manifold, at which point they show improvements over previous constructions of such layers.

### Strengths
- The main constructions of the layers are relatively intuitive, make sense, and natural to arrive at when starting at the analogous objects in Euclidean spaces.
- The cookbook looks sufficiently general as to be useful to others in the community as a starting point for formulating their own architectures. 
- The experimental results on different geometries are comprehensive relative to similar previous work, and show improvement over prior work.
- The paper is nicely written; the main intuitions are conveyed through clear writing and useful examples.

### Weaknesses
 - The Riemannian convolution may not be efficient. Part of why (Euclidean) convolutions are popular is that they can be efficiently computed by a GPU. Is there any possibility that the convolution may share this property (say for the SPD/Grassmanian examples)?
- More generally, it seems difficult efficiently compute/approximate a forward pass of a Riemannian feed-forward/conv layer on more general manifolds, since the forward pass uses exponential maps and logarithms. It seems that to get efficiently computable solutions one needs to do more ad-hoc/specialized work on top of the presented framework.

### Questions
- Is there any intuition about why the layers formulated in the paper perform better than previous ad-hoc approaches? What practical benefits are gained by approaching this problem more generally?
- Is there any remedy when the exponential map is only locally defined? There seems to be an example in the appendix but is there any more general solution?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper focuses on designing deep neural networks operating on general Riemannian manifolds, and in particular generalizing fully connected and convolutional layers to Riemannian geometries. Previous work in this domain has often been limited to specific manifolds or has relied heavily on the properties of certain geometric structures, limiting flexibility. The paper proposes a more general and flexible framework for constructing FC and convolutional layers that operate on general geometries, allowing broader applicability across different types of Riemannian manifolds. The paper demonstrates their framework primarily over the Symmetric Positive Definite (SPD) and Grassmannian manifolds.

### Strengths
The groundwork for defining neural network architectures over general geometries is both theoretically interesting and provides a practical blueprint for future work designing such architectures. For manifolds where we cannot afford to (or where it may not make sense to) leave the manifold, such purely intrinsic formulations are crucial. Although components like the exponential map (let alone the logarithmic map) can often be intractable to compute, this work sets a valuable precedent for future endeavors in designing neural network architectures over specific manifolds in practice. The presented experiments also offer a broad array of baselines, with notable improvements over prior work, particularly on HDM05. Additionally, the framework's flexibility to vary the latent geometry could have significant implications for understanding and comparing geometric representations in neural networks.

### Weaknesses
- **Theorem statements should be more self-contained**. For example, when reading Theorem 4.1, it appears to be merely defining the Riemannian FC layer, which leads to confusion about what is actually being proven. The lack of clarity here makes the theoretical contributions less accessible, reducing the impact of the formalism.
  
- **Flexibility claim for Grassmannian networks**. The main example manifold used to demonstrate the framework is the Grassmannian, where the authors claim that their layer uniquely allows the flexibility typical of MLP and CNN layers (i.e., modifying output dimensions like subspace dimension, ambient dimension, and channel count). While this is technically true, it is unclear why this flexibility cannot be achieved with simple modifications to previous architectures (e.g. basic lifting/copying maps and truncation), and there is no empirical evidence directly demonstrating the practical benefit of this added flexibility. This weakens the argument that the proposed method offers a clear advantage over prior approaches.
  
- **Marginal improvements over baselines**. While there is a non-negligible improvement on HDM05, the gains over other baselines are mostly marginal. Given that all of the listed manifolds have been extensively studied in their own right and with respect to neural network architectures (as well-documented by the authors), it remains unclear why practitioners should adopt the authors' framework rather than leveraging the extensive existing literature that exploits the structure of these highly structured manifolds. Furthermore, since this method relies on Riemannian logarithmic and exponential maps (which are often intractable or computationally prohibitive for general Riemannian manifolds) there is insufficient justification for the viability of this framework for designing neural network architectures over general manifolds. It would be nice to see an example manifold where NN architectures haven't been developed yet, or extensive ablations (with significant performance improvement) on one of the demonstrated manifolds to demonstrate the practical use of the flexibility in this framework.

### Questions
- Could you clarify why this flexibility on the Grassmannian cannot be achieved through simple modifications of existing architectures (or why they would be ineffective)? Furthermore, do you have any empirical evidence demonstrating that this added flexibility provides a significant practical benefit compared to previous approaches?

- Are there any manifolds where (a) there is a practical benefit for learning features on this manifold in the broader ICLR community, (b) your framework provides a concrete guideline to designing a NN architecture on this manifold, and (c) NN architectures have not been studied before on this manifold?

### Soundness
3

### Presentation
3

### Contribution
2
