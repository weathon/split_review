# TELEPORTATION WITH NULL SPACE GRADIENT PROJECTION FOR OPTIMIZATION ACCELERATION

- Decision: Reject
- Scores: 6, 3, 3, 3

## Abstract
Optimization techniques have become increasingly critical due to the ever-growing model complexity and data scale. In particular, teleportation has emerged as a promising approach, which accelerates convergence of gradient descent-based methods by navigating within the loss invariant level set to identify parameters with advantageous geometric properties. Existing teleportation algorithms have primarily demonstrated their effectiveness in optimizing Multi-Layer Perceptrons (MLPs), but their extension to more advanced architectures, such as Convolutional Neural Networks (CNNs) and Transformers, remains challenging. Moreover, they often impose significant computational demands, limiting their applicability to complex architectures. To this end, we introduce an algorithm that projects the gradient of the teleportation objective function onto the input null space, effectively preserving the teleportation within the loss invariant level set and reducing computational cost. Our approach is readily generalizable from MLPs to CNNs, transformers, and potentially other advanced architectures. We validate the effectiveness of our algorithm across various benchmark datasets and optimizers, demonstrating its broad applicability.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work considers an alternative strategy for teleportation in optimization landscapes, i.e., going to locations within the level set of the loss but which are better suited for further optimization, like having higher gradient norm. Past methods consider using the group action of continuous symmetries, but this makes them limited to MLPs. This work considers maximizing the gradient norm to teleport while ensuring the layerwise updates of parameters falls in the null space of the layer input. Experiments showcase that this method leads to faster convergence in train and test performance while performing at par with baseline optimization methods.

### Strengths
- The idea to utlize (layer) input-space null projection is built atop the work of GPM (Saha et al'21) in continual learning and its use here for the purposes of teleportation is neat.

- This extends the applicability of the approach and might draw further interest in these methods. The resulting method is also more efficient than symmetry teleport based methods.

- The experiments cover a variety of scenarios, wherein the method results in faster convergence while being as good if not slightly better than the baselines.

### Weaknesses
 - **Wall-clock comparison of convergence:**
 It is unclear how much excess time is being used during the process of teleportation, and if the gains in faster convergence are worth the extra effort. Specifically, the computational cost of performing the SVD and null space projection for each layer during teleportation is not quantified. This makes it difficult to assess the practical benefit of the proposed method in real-world scenarios where wall-clock time is a critical factor.

- **Difference in arrived solutions:**
I would like to see if the solutions reached with teleportation differ qualitatively to those reached without. Can the authors make the LMC curves (Frankle et al, 2019) to see if there are barriers between the reached solutions? It would be beneficial to understand if the teleportation is simply accelerating convergence to the same minima, or if it is leading to different, potentially better, regions of the loss landscape. This analysis is crucial for understanding the true impact of the method.

- **Comparison to group action based method:**
 I think it would be interesting to compare the results of your method to group action based ones in a simple setting with MLPs to see in what ways the methods differ. It is not clear if the proposed method is simply a more efficient implementation of the same underlying principle or if it offers distinct advantages in terms of the solutions it can reach.


- **Stability of the hyperparameters**: It is not clear to me how much do the hyperparameters of teleportation, as well as SVD thresholds, have to be tuned. Can you present a study showing the robustness (or lack of)? The sensitivity of these hyperparameters could significantly impact the practical applicability of the method, and a thorough investigation is needed to understand their influence on performance.

- **Poor referencing of related work:**
A lot of the citations are plain wrong. E.g., I don't think the citations are representative, and some are just plain wrong:

  - Hessian matrix (Sun et al., 2019).
  - Adam (Kashyap 2022)
  - ReLU (Agarap, 2018)
  - MLP (Taud & Mas, 2018).
  - CNN (Li et al., 2021).
  - multi-head self-attention layers (Wen et al., 2022).

### Questions
See weaknesses section. 

Regarding presentation, I would also make a few suggestions. Instead of input-space, quality it as input space of layers. Otherwise it is confusing. Also, please fix the image titles to TinyImageNet (which currently say ImageNet).

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper presents a novel algorithm, "teleportation with null space gradient projection," designed to accelerate optimization in deep learning models. The proposed method improves upon existing teleportation techniques by reducing runtime and mitigating error accumulation. Additionally, it extends teleportation optimization to a broader range of models. The authors validate their approach across diverse model architectures, including Multi-Layer Perceptrons (MLPs), Convolutional Neural Networks (CNNs), and Transformers, employing various benchmark datasets and optimization methods to demonstrate its effectiveness.

### Strengths
- The paper is well-written and easy to follow.
- The proposed method is architecturally flexible, as it does not rely on group action from the underlying architecture. This allows the approach to be applicable across a broader range of architectures.

### Weaknesses
 - The explanation for why projecting onto the Residual Gradient Space (RGS) keeps the parameters within the loss-invariant level set of the original loss is unclear, since the gradient being projected is the gradient of the teleport loss projected to RGS.
- The paper lacks a comparison with other state-of-the-art methods that employ teleportation, such as Zhao et al. (2022) and Mishkin et al. (2024).
- A runtime comparison with non-teleportation optimizers counterparts (SGD, Momentum, Adagrad, Adam) is absent.

### Questions
- How does projecting the gradient of the teleportation loss onto RGS ensure the parameters remain on the level set of the original loss?
- Could you provide a performance comparison of the proposed method with other teleportation techniques, specifically comparing with Zhao et al. (2022) on MLP models and with Mishkin et al. (2024) on applicable models?
- What are the runtime of the baseline optimizers before and after introducing teleportation with null-space gradient projection?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents a teleportation technique for accelerating the convergence of gradient descent. The idea of teleportation is to move the parameters on the level set of the loss function to get a better (e.g., steeper) point before taking a gradient descent step, and this is done every few iterations. The authors aim to address limitations in previous teleportation methods, which were primarily restricted to multi-layer perceptrons (MLPs), by generalizing it to a broader range of architectures, including convolutional neural networks (CNNs) and transformers. Their method aims to reduce computational overhead by eliminating dependency on specific group actions and using an efficient gradient projection technique.

### Strengths
- The paper concerns an interesting problem, specifically exploring optimization acceleration through teleportation techniques.
- The introduction effectively provides background context and situates the study within related work, giving readers a clear overview of the existing literature and the motivation for this approach.
- The idea of doing gradient ascent on the gradient norm, while projecting it onto the level set of the original loss is interesting.

### Weaknesses
 - The authors mix layer-wise and global operations without a clear explanation or justification. While Equations (4) and (5) and Algorithm 1 (correctly) outline parameter updates at a global level, Sections 3.1, 3.2, and 3.3 abruptly pivot to layer-wise operations and projections without justification. The authors should clarify why the projection of the entire parameter vector 𝜋 is equivalent to projecting subsets of the elements (i.e., layers) separately. Specifically, the paper lacks a clear explanation of how the null space projection, which is defined globally, can be applied independently to each layer's weight matrix. This is crucial because the null space of the input to one layer is not necessarily related to the null space of the input to another layer. The paper needs to rigorously justify why this layer-wise decomposition is valid and does not alter the overall teleportation effect.
- Relatedly, from Equation (5), it appears that 𝜋 is defined to take inputs of the same dimensionality as the complete set of weights. If so, then reusing 𝜋 in Equations (11-13) is incorrect, as these equations seem to imply different dimensionality. The notation is inconsistent, and the paper needs to clearly define the dimensionality of 𝜋 in each context. The use of the same symbol for different dimensional objects makes the equations confusing and potentially incorrect. The authors should use distinct symbols or subscripts to clarify the dimensionality of 𝜋 when it is used in layer-specific contexts.
- Again, on a related note, the statement that "the gradient of the teleportation objective function resides within the space spanned by the input data" is incorrect and misleading. The paper actually seems to refer to the input spaces at each layer, not the space spanned by the input data. This claim should be corrected and replaced with a precise statement about the layers if there exists one. Moreover, the claim is not precise enough, as the gradient of the teleportation objective function for a given layer resides in the space spanned by the *rows* of the input data matrix for that layer, not just the input data itself. This distinction is important and should be clarified.

### Questions
- Please refer to the weaknesses above.
- In the unnumbered equations between (7) and (8) for MLP, CNN, and Self-Attention: I see that the order of multiplication in which the input to the layer appears differs between architectures (x*\delta in CNN and Self-Attention, as opposed to \delta*x in MLP). Can the authors explain whether this order affects the theoretical claims or the projected outcome, and if so, in what ways?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes an improved algorithm for teleportation-based optimization, in which at certain times during training the network weights are moved to a different location with roughly the same loss but higher gradient norm. Their approach uses an approximate projection onto the loss level set while optimizing the gradient norm during the teleportation step. The algorithm is validated on experiments with MLPs, CNNs, and Transformers.

### Strengths
1. The authors propose a faster algorithm for the teleportation step that can also be applied to architectures beyond MLPs.
2. The authors validate their approach by using it to modify a variety of standard optimizers on multiple problems, showing consistent improvements in training loss.
3. Code is attached to reproduce the results.

### Weaknesses
1. The approximation scheme lacks clarity, particularly regarding its implementation and theoretical guarantees. While the paper mentions an approximate projection onto the loss level set, the precise mechanism for achieving this is not well-defined. Providing pseudocode specifically for the approximation algorithm, rather than just the broader teleportation procedure, would significantly improve clarity. Furthermore, a more rigorous analysis of the approximation error would be valuable. For instance, how does the choice of singular value threshold affect the accuracy of the projection? What are the theoretical bounds on the deviation from the true loss level set?

2. The paper claims improved speed over past teleportation approaches, including symmetry-based and linear approximation methods, but lacks empirical evidence to support this assertion. A direct comparison of computational cost, ideally in terms of wall-clock time rather than just epochs, is crucial to substantiate this claim. For example, a detailed analysis of the trade-off between the reduced per-iteration complexity of the proposed method and the potential increase in the number of iterations due to approximation error would be insightful. This could involve comparing the time taken to reach a specific loss threshold using different teleportation strategies.

3. The observed improvement primarily focuses on training performance, with minimal gains in generalization. While the authors acknowledge this limitation and suggest potential avenues for improvement, these remain unexplored. The practical utility of teleportation-based optimization is questionable without a clear demonstration of its ability to enhance test-time performance. A more thorough investigation into the factors influencing generalization, such as the choice of teleportation objective function, is necessary to establish the broader applicability of the proposed method.

### Questions
1. What does “enhance the gradient norm” mean?
2. In what sense is symmetry teleportation “a state-of-the-art algorithm”?
3. It is strange to cite a 2018 applications paper for MLPs (they have been around for a long time), a 2018 paper proposing ReLUs for classification for ReLUs (which have also been around for a long time), and a 2022 applying Transformers to time series for multi-head attention when they were introduced in 2017 by Vaswani et al.

### Soundness
2

### Presentation
1

### Contribution
2
