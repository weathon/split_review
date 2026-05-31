## Human Reviewer 1

### Summary
The paper suggest a hyperbolic model for neural network learning and inference that has not been used before: proper velocity neural networks. For this purpose, the paper completes the mathematical inventory required for learning and inference and investigates the performance of the novel PVNNs on a set of artificial and natural benchmarks.

### Strengths
+ Suggesting an unused but effective hyperbolic model is a great contribution
+ There existed some mathematical gaps that needed closing in order to allow for the definition of PVNNs
+ The experiments are interesting and insightful

### Weaknesses
- issues with presentation: I have not understood which experiments were performed in section 6.1, and why a larger median output norm would be better.
- issues with experiments: My understanding is that the curvature is a hyperparameter, but I see no exploration of hyperparameter choices in the experiments section.
- issues with interpreting results: The substantial disadvantage on Cora is not well explained. 
- minor issues with presentation: 
         -- It does not make sense to mark best results in bold, if they are statistically indistinguishable from baselines (Table 6)
         -- "on the highly hyperbolic Cora dataset" does not make sense. The dataset may exhibit hierarchical structures or larger diameter etc., but it is not hyperbolic on its own, though its structure might be better represented in space that is more curved

### Questions
-  Is the isomorphism from PV to Poincare ball needed? If it is needed, then why is the computation on PV numerically more stable?
- what does delta in the tables of the experiments section refer to?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper proposes proper velocity neural networks (PVNN), where hyperbolic neural operations are built on the “proper velocity” (PV) manifold. The paper presents the basic elements of Riemannian geometry of the PV manifold, develops various layers, and shows experiments on numerical stability, graph learning, image classification and genomic sequence learning.

### Strengths
1. This paper introduces a new playground for hyperbolic neural networks and provides the complete Riemannian toolkit and neural-layer formulations on it. The detailed derivations of exponential/logarithmic maps, parallel transport, and gyro-based operations are rigorous and valuable. These constructions can serve as fundamental tools for future research on geometric deep learning.
2. The idea is well motivated and the paper is clearly structured and easy to follow, which makes the technical content accessible to readers from machine learning communities who may not be familiar with the geometry.
3. The numerical experiments demonstrate that PV-based networks can be applied to diverse domains (graphs, images, genomics) and generally perform competitively with existing hyperbolic baselines.

### Weaknesses
1. 
- A major conceptual issue arises in the presentation of the PV model. As written, the paper may lead readers to believe that PV is an independent model parallel to the Poincaré, hyperboloid, and Klein models. However, PV and the hyperboloid are deeply connected through special relativity. In fact, there exists a natural isometry $\pi$ between hyperboloid and PV. Given a point in the hyperboloid $\mathbf{x} = (x_0, x_1, \cdots, x_n) \in \mathbb{H}^n$, $$\pi(\mathbf{x}) = (x_1, \cdots, x_n) \in \mathcal{PV}^n.$$ That is, PV is nothing else but the spatial representation corresponding to the time-space representation of hyperboloid. The paper should explicitly state this relationship so that readers unfamiliar with hyperbolic geometry are not misled. 

- Conceptually, it would be more natural to compare PV directly with the hyperboloid (e.g., Section 4.1) rather than primarily with the Poincaré ball. Such comparison would yield more geometric and numerical insights.

- In this context, a very interesting paper will be “Fully hyperbolic neural networks” (Chen et al.,2022). From your perspective, although they write everything in terms of hyperboloid/Lorentz, their operations are actually completely in the PV space. It would be informative to readers if you can point this out and discuss whether their approach naturally follows PV geometry.

2. 
- The numerical stability argument and experiment is unclear. The claim that PV is “unconstrained” and therefore more numerically stable is not entirely convincing. While the Poincaré ball is indeed bounded, the hyperboloid is already an unbounded manifold, and PV is simply its spatial representation. Thus, PV cannot be inherently “more flexible” than the hyperboloid. Note that hyperboloid is in $\mathbb{R}^{n+1}$.

- Moreover, the numerical-stability experiment (Table 1) shows extremely large norms (up to $10^8$), which may themselves indicate instability or unbounded dynamic range rather than desirable behavior.

### Questions
See "weaknesses" for revision suggestions.

### Soundness
2

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 3

### Summary
This paper proposes formulating hyperbolic deep learning techniques typically represented via the Poincaré or Lorentz model in the Proper Velocity manifold. Previous representations often suffered from numerical issues close to the boundary, which the Proper Velocity model avoids. The authors derive key quantities such as exponential and logarithmic maps, as well as important operations for deep learning including fully-connected layers, convolution as well as multinomial logistic regression. Equipped with these formulations, the authors evaluate their hyperbolic models on a suite of benchmarks, including vision, graph learning as well as genomics. Their approach is very competitive with previous works while offering better stability.

### Strengths
1. The paper is very well-written and very nicely placed within the literature of hyperbolic learning. The mathematical derivations are very detailed and extensive and a nice contribution in themselves in my opinion. I believe the Proper Velocity manifold is a nice addition to the toolkit that practitioners have to perform hyperbolic deep learning, especially if the stability issues of previous approaches are remedied. I have some more comments on this later.
2. The authors perform a very broad evaluation of their model, using vision, graph and genomics data to compare to previous approaches in hyperbolic deep learning. This makes it more convincing for me that this novel representation works across different scenarios, but I do have some more comments on this point later.

### Weaknesses
1. The main issue for me with this work in its current state is the lack of convincing evidence towards its premise: other representations suffer from numerical issues (especially around the border) and I assume this point implies that “performance of these models is affected”? Towards this question, you show a small experiment where addition and multiplication is performed on Poincaré and Proper Velocity manifolds, which indeed shows that norms close to the border collapse in case of Poincaré, where as the Proper Velocity model is able to adequately handle this case. Numerically however, the Proper Velocity model seems to have more issues, at least in terms of multiplication? More importantly however, I don’t really see an experiment or argument that shows these other models actually suffering in a realistic scenario, like vision or graph learning. Are these other models actually being limited by numerical issues? Can models in Proper Velocity be trained in lower precision? Even a simple experiment such as learning to embed a tree in hyperbolic space (similar to e.g. [1]) would help me be more convinced regarding these claims. While Proper Velocity sometimes outperform Poincaré/Hyperboloid, it is not clear if that’s due to the numerical issues mentioned, especially as performance is actually quite similar in most cases.
2. I like that the evaluation is very broad, but on the other hand the experiments are also a bit shallow in each case. For node classification, you seem to use a fully-connected network in all representations, even though it is more standard to use a graph neural network that employs some form of graph convolution. Other methods have developed such specialized operations in the Poincaré or Hyperboloid model, and I think something like this is needed to truly understand the potential of a representation. Similarly in the case of vision, a Euclidean encoder is used, which essentially does all the heavy lifting and only the final classification layer is hyperbolic. Again, other representations have their dedicated convolution layers in hyperbolic space, why not do the same in the Proper Velocity model? Results are probably as a consequence almost identical for PV and HNN++. What is however interesting is that Poincaré seems to struggle a lot for CIFAR100, is this maybe due to numerical issues? The genomics experiments are more convincing in this regard!  

[1] Constant Curvature Graph Convolutional Networks, Bachmann et al, 2020

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
3

---

## Human Reviewer 4

### Summary
The paper proposes **Proper Velocity Neural Networks (PVNNs)**, which work on the **Proper Velocity (PV) manifold**, an unconstrained coordinate of hyperbolic space. The authors first derive **closed-form Riemannian operators** for PV (exponential and logarithmic maps, geodesic distance, and parallel transport). They then design **core layers** in PV: multinomial logistic regression (PV-MLR), a fully connected layer with an **analytic formula**, convolution, activation, and **GyroBN** normalization. Experiments on **numerical stability**, **graphs**, **CIFAR-10/100**, and **genomic sequence prediction** show strong stability and **competitive accuracy**, with clear gains on some tasks (e.g., Airport), but **weaker results on Cora**. The code will be released upon acceptance.

### Strengths
- **Originality:** Uses the **PV manifold** as an **unconstrained** alternative to Poincaré/Hyperboloid; complete Riemannian toolkit enables end-to-end models.
- **Quality (theory):** Rigorous **isometry** to Poincaré; **closed-form** exp/log/transport; **analytic PV-FC**; GyroBN with mean/variance homogeneity.
- **Quality (empirics):** Broad evaluation (stability, four graph datasets, CIFAR-10/100, TEB genomics) with shared backbones and multiple seeds.
- **Clarity:** Structure is logical; appendices provide proofs and implementation details. :contentReference[oaicite:7]{index=7}  
- **Significance:** **Large-norm** representations work stably; strong gains on some datasets (e.g., Airport; several TEB tasks).

### Weaknesses
- **No expressivity guarantees:** There is **no universality** or approximation bound for PVNNs, limiting formal claims about representation power.
- **Mixed graph performance:** **Cora** performance is lower than Poincaré/Hyperboloid baselines; the paper gives limited analysis of this failure mode. 
- **Model breadth:** Vision uses **ResNet-18 with only the head changed**; large-scale or transformer results are left for future work.

### Questions
1. **Expressivity:** Do PVNNs satisfy a **universal approximation** property under reasonable assumptions? If yes, what function classes and depths are required?
2. **Cora drop:** Why does PVNN underperform on **Cora**? Is it due to curvature mismatch, optimization, or the decision boundary shape? Would **learnable curvature** or hybrid PV/Poincaré layers help?
3. **Runtime/memory:** How are the **computation and memory** costs of PV operators compared to Poincaré/Hyperboloid ?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
3

---

## Human Reviewer 5

### Summary
This paper proposes some building blocks for neural networks on hyperbolic space based on proper velocity (PV) model. Specifically, the authors propose multinomial logistic regression (MLR), fully-connected (FC), batch normalization (BN), convolutional, activation layers. These layers are validated on graph node classification, image classification, and genomic sequence learning.

### Strengths
- The topic of the paper is interesting.

- The paper advocate the use of PV model for hyperbolic space which is underexplored in the literature of HNNs.

### Weaknesses
- The contribution is incremental.

- The paper is poorly written.

- Experimental results are not convincing. Also, important baselines are missing.

### Questions
The paper aims at constructing some building blocks for HNNs. However, the authors simply use the approaches in [Shimizu et al., ICLR 2021; Nguyen and Yang, ICML 2023; Nguyen et al., ICLR 2024; Chen et al., NeurIPS 2024] rather than developing new approaches for their construction. Although the PV model is less studied in previous works for HNNs, its geometry is well-understood, making it straightforward to adapt existing approaches to this geometry.  

The exposition of the paper can  be significantly improved. For instance, the tables look messy with small texts and numbers in some tables and too big ones in others. 

Experimental results are not convincing and important baselines are missing:

- Some experimental settings are given in Appendix, but these are very sketchy. For instance, for node classification experiments, it is crucial to provide and discuss settings for the dimension of node embeddings. However, I did not find this setting in the main paper and Appendix. 

- The Hyperboloid model is used for comparison on node classification experiments (Table 2, Bdeir et al., 2024) but is not used for comparison on image classification experiments (Table 6). It is noted that the Hyperboloid model outperforms the PV model on both CIFAR-10 and CIFAR-100 datasets in terms of mean accuracy (see also my first question below).

Questions:

1. The authors argue that the PV model is an unconstrained representation of hyperbolic space which can lead to more stable results for HNNs. I am not sure why this is the case ? It seems that the Lorentz models is also another unconstrained representation of hyperbolic space, since the time dimension is computed w.r.t. the space dimensions. Why the PV model can be more stable than the Hyperboloid model in the considered applications ?

2. In the introduction, the authors claim that the new representation space can be a good alternative for existing models of hyperbolic spaces due to its numerical stability. However, its performance on datasets with high hyperbolicity is inferior to those of other models. This indicates that the PV model might not be effective for capturing hierarchical structures which somehow contradicts the statement in the introduction. Could the authors clarify on this point ?

### Soundness
3

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4