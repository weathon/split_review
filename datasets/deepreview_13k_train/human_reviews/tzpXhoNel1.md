# GRepsNet: A Simple Equivariant Network for Arbitrary Matrix Groups

- Decision: Reject
- Scores: 8, 1, 5, 3

## Abstract
Group equivariance is a strong inductive bias useful in a wide range of domains including images, point clouds, dynamical systems, and partial differential equations (PDEs). But constructing efficient equivariant networks for general groups and domains is difficult. Recent work by Finzi et al. (2021) directly solves the equivariance constraint for arbitrary matrix groups to obtain equivariant MLPs (EMLPs). However, this method does not scale well and scaling is crucial to get the best from deep learning. This necessitates the design of group equivariant networks for general domains and groups that are simple and scalable. To this end, we introduce Group Representation Networks (GRepsNets), a simple equivariant network for arbitrary matrix groups. The key intuition for our design is that using tensor representations in the hidden layers of a neural network along with appropriate mixing of various representations can lead to expressive equivariant networks, which we confirm empirically. We find GRepsNet to be competitive to EMLP on several tasks with group symmetries such as O(5), O(1, 3), and O(3) with scalars, vectors, and second-order tensors as data types. To illustrate the simplicity and generality of our network, we also use it for image classification with MLP-mixers, predicting N-body dynamics using message passing neural networks (MPNNs), and for solving PDEs using Fourier neural operators (FNOs). Surprisingly, we find that using simple first-order representations itself can yield benefits of group equivariance without additional changes in the architecture. Finally, we illustrate how higher-order tensor representations can be used for group equivariant finetuning that outperforms the existing equivariant finetuning method Basu et al. (2023b).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a general framework for building equivariant networks for any matrix group. The proposed method is far more scalable than prior work like EMLPs (Finzi et al.). It is also very general and can be combined with advanced architectures including MLP mixers, message-passing neural networks, Fourier neural operators, etc for various applications. The authors also introduce using higher-order tensor representations and show this improves performance.

### Strengths
- This work could have significant impact. The proposed framework is very general, able to construct equivariant networks for any matrix group. It can also be combined with many advanced deep learning architectures across diverse applications. Additionally, the method scales to large problems. There is strong potential for numerous applications of this work.
- The authors provide a unified view of previous work such as vector neurons, harmonic networks and equitune. Their framework also enables incorporating higher-order tensor representations. In this work, they already verified that second-order tensors are useful as equivariant features.

### Weaknesses
 - The authors' method provides a very general framework that can process tensor representations $T_i$ of arbitrary order. However, in practice, most experiments only use $T_0$ and $T_1$, with one additional experiment testing $T_2$. While this paper still makes an important contribution, there is a disconnect between the theory and experiments - the importance of higher-order ($i>2$) tensor representations is not empirically demonstrated. I'm simply noting that the full generality of the framework is not validated, even though the core ideas represent an advance. Specifically, the paper lacks experiments that demonstrate the necessity or benefit of using tensor orders beyond 2, which is a crucial aspect of the proposed framework. The theoretical framework suggests a capability to handle arbitrary order tensors, but the empirical validation is limited to low-order tensors. This raises questions about the practical relevance of the higher-order tensor processing capability. For example, are there specific tasks where $T_3$ or $T_4$ representations provide a significant advantage over $T_0$, $T_1$, and $T_2$? Without such empirical evidence, the claim of generality remains somewhat theoretical.


### Questions
- Do the authors know if their model is universal, in the sense that any equivariant function with respect to the matrix groups can be well approximated by the model given a suitable parameter set? Are there any subsets of equivariant functions that cannot be represented? With that said, the paper still makes significant contributions by proposing a general framework for constructing equivariant networks and demonstrating strong empirical performance. Further analysis of the model's theoretical expressivity would be an interesting area for future work.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper considers the problem of building transformation-equivariant and invariant neural networks. The authors' main focus is to create neural networks that are scalable and generally applicable. They propose GRepsNet - a class of neural networks that take tensor features as inputs and process them with T-layers.

The structure of the paper does not allow a reader to understand the method clearly. The way the paper presents its ideas is not sufficient for implementation. Moreover, while the paper contains a lot of theory and very general explanations, it lacks details on the method itself. The story of the paper is not coherent.

It is very complicated to understand the exact implementation, the exact contribution, and the specific details of the performed research from the current version of the paper. It requires a major revision to meet the high standards of the ICLR conference.

### Strengths
The paper has some strengths by themselves, which, however, do not make the paper coherent. Among the strengths I can mention a thorough explanation of some of the concepts such as group representations.

### Weaknesses
The main weaknesses of the paper are that it contains a lot of technical details on topics that may be familiar to the reader, and it does not provide enough information to form a strong understanding of the proposed method.

- The structure of the paper should be changed in order to improve its readability. The standard "Intro, Related Work, Theory, Experiments, Concluiosn" can serve as an example. 
- The entire Section 2, "Background," seems like a repetition of what a reader may already know from references. Thus, it's not necessary to present it in such explicit detail. It is a mix of "related work" and "prelimiries for the theory section", but it doesn't serve any of these roles.
- It's not clear what type of neural network is being built. What is the main contribution of the paper? Is it proposing the use of different features, or is it introducing a new type of neural network? Is it a marginal improvement over EMLP? Is it the next interation of Villar et al? Is it an absolutely new approach for building equivariant models? If so, why don't you compare it against SOTA competitors?
- The choice of datasets and models in the experiments is not clear. Why was MLP Mixer chosen instead of a group equivariant CNN?

### Questions
- Can you compare your method to a group equivariant neural network with a similar number of parameters? I can suggest to use a CNN from *Weiler M., Cesa G. General e (2)-equivariant steerable cnns NeurIPS 2019*
- Page 4, "Process converted tensors", you write that "we simply pass it through a linear neural network with no point-wise non-linearities or bias terms to ensure that the output is equivariant". What is a linear NN here? Is it a simple matrix multiplication?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a simple neural network architecture that is equivariant to arbitrary matrix groups. The architecture makes use of scalar, vector, and higher-order tensor representations. Operations consist of transforming between these representations, and linear mixing of representations of the same type. The authors conceptually compare their work to EMLP (Finzi et al.) and argue that their architecture is simpler, more efficient, and scales better to larger datasets and data types. Experiments are provided for:
- Symmetries such as O(5), O(1, 3), and O(3).
- Image classification under rotations.
- Predicting n-body dynamics with GNNs.
- Solving PDEs.

### Strengths
* The simplicity and generality of the architecture is appealing. I think this work should be seen as a generalization of the vector neurons architecture. Perhaps a more suitable name for the architecture would have been tensor neurons. To my knowledge, the vector neurons framework had not previously been generalized so the work is novel to me.
* The experiments are varied and touch on several different application areas of ML.

### Weaknesses
 * As I've mentioned, I see this work as a generalization of the vector neurons architecture. The generalization is, however, very straightforward and requires no technical work. Even the proof of equivariance carries over almost directly.
* Even though the architecture is quite general, the authors use ad-hoc methods for designing the architectures in the experiments and rely on previously obtained models for symmetric data such as convolution for images and message passing for graphs. It might be worth mentioning that, in principle, all models in the paper could have followed the exact same blueprint (with a possible drop in performance). For example, the translation symmetry of images and the permutation symmetry of graphs could all have been handled under the GRepsNet architecture. The paper could be more clear in describing which sub-symmetries are being handled by their model.
* The work shouldn't be compared to EMLP (Finzi et al.). As I've mentioned, comparing to vector neurons is much more appropriate. What EMLP does is that it computes *all* equivariant bases, which is much more challenging than providing *some* equivariant bases, as in this work. EMLP is a valid baseline of comparison in experiments, but the goal of that paper is different from this one.
* For the image experiments there should be a comparison with group convolutional networks (Cohen & Welling).


### Questions
- Are there non-linearities being applied to T_0 representations (scalars)? The T_i (i > 0) reps don't have nonlinearities so I presume that nonlinearity must come in from being mixed with T_0 reps but the paper only says that this is done for better mixing. Also, I think this is how different indices of the T_i tensors are communicating information, i.e., without this mixing, each index of the T_i tensors would be processed entirely separately. It's not clearly explained in the paper.
- Does the model provide universal approximation guarantees?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper construct equivariant neural networks for arbitrary matrix groups. The core insight is that tensors of type $i$ with $i = kj + r$ ($i > j > 0$) can be obtained by taking $T_j^{\otimes k} \otimes T_1^{\otimes r}$. In this way, higher-order tensors can be constructed from lower-order tensors and mixing is then done through linear layers. Further, scalars (type-0 tensors, invariants) can further interact nonlinearly with the higher-order tensors. This efficient architecture is tested on several experiments including synthetic experiments from Finzi et al. (2021), image classification, PDE solving, $n$-body dynamics, and equivariant fine-tuning. Results show competitive performances using a lower computational budget.

### Strengths
* The paper proposes a simple, effective and efficient method for equivariant neural networks on arbitrary matrix groups.
* The search for efficient and effective equivariant architectures is still ongoing, making it a timely and significant contributions.
* The method is tested on several distinct experiments.

### Weaknesses
See questions for further elaborations.

* Clarity and quality: there are several important details missing regarding implementations and experimental details.
* The claim is that the method is equivariant to arbitrary matrix groups, but only subgroups of the orthogonal group are considered in the experiments.
* Several relevant baselines are missing for e.g. the $n$-body experiments. For example, Brandsetter et al., 2022 and Ruhe et al., 2023 are currently state of the art on the $n$-body experiments but are left out of the picture.
* The Finzi et al. (2021) experiments are altered to a low-data setting.
* It is unclear how second-order tensor-features are used in the image classification experiments. Further, sentences like "GRepsMLP-Mixer-2 simply adds non-parametric early fusion operations in the group dimension to the GREpsMLP-mixer-1 architecture" are completely opaque to me. More care needs to be taken to explain what the authors do exactly.

Minor:
* Repeatedly, the *vector neurons* architecture is called $\mathrm{SO}(3)$-equivariant, and while the original paper frames itself as such, it is technically $O(n)$-equivariant. As such, it is less restricted than sometimes claimed.

### Questions
* Why did you limit yourself to orthogonal group experiments where e.g. Finzi et al. (2021) also consider other matrix groups? 
* It is not quite clear how equivariance is achieved in the image domain, where usually equivariant architectures consider images as maps from positions to (RGB) values. Inspecting the appendix, I noted that the authors repeat images four times in 90-degree rotations. However, isn't this a different way of achieving equivariance compared to what the main method proposes? The main method combines tensors of different types linearly and then nonlinearly using equivariant nonlinearities, but I don't see how that is used in the image case. Similarly for the FNO comparison.
* What do the equivariant layers exactly look like. Could you write down what the conversion layers and linear layers comprise mathematically?
* How is equivariance achieved for the image experiments? Could you provide more details into your architectures, experimental setup, and so on?
* Why do $N$ tensors lead to $N^2$ invariants?
* Could you discuss the limitations of your method? Does it replace all tensor-based methods or does it have specific use-cases? Is it as expressive as previous methods? It seems that there are no bilinear operations (e.g., tensor products) in your architectures, is that a problem?
* The authors bolden their numbers even though some method might be better than theirs but uses a more sophisticated technique. E.g., for G-FNO in Table 3. Instead, I would also provide the forward/backward times and include a comparison on that level, as efficiency is a core part of the method. 
* Why does the number of data-points in your synthetic experiments not extend beyond $~1000$? In Finzi et al., settings up to 30 000 datapoints are considered.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
