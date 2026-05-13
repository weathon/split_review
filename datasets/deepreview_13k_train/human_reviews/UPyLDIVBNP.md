# Fully Identical Initialization

- Decision: Reject
- Scores: 3, 6, 6

## Abstract
Deep neural networks (DNNs) have achieved numerous remarkable accomplishments in practice. The success of these networks hinges on effective initialization methods, which are vital for ensuring stable and rapid convergence during training. Recently, initialization methods that maintain identity transition within layers have shown good efficiency in network training. These techniques (e.g., Fixup) set specific weights to zero to achieve identity control. However, settings of remaining weight (e.g., Fixup uses random values to initialize non-zero weights) will affect inductive bias that is achieved only by a zero weight, which may be harmful to training. Addressing this concern, we introduce fully identical initialization (IDInit), an innovative method that preserves identity in both the main and sub-stem layers of residual networks. IDInit employs a padded identity-like matrix to overcome rank constraints in non-square weight matrices. Furthermore, we show a convergence problem of an identity matrix can be solved by adding a momentum term into the optimizer. Additionally, we explore enhancing the universality of IDInit by processing higher-order weights and addressing dead neuron problems. IDInit is a straightforward yet effective initialization method, promising improved convergence, stability, and performance across various settings, including large-scale datasets and deep models. It stands as a novel solution for initializing non-standard weight matrices, offering significant advantages in network training.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors introduce a technique called Identical Initialization (IDInit), which uses identity matrices and their variants to initialize weights. They discussed the convergence problem and dead neuron problem for common identity initialization and previous works. They explore the application of this technique to non-square matrices, residual architectures, and convolutional operations. Empirical evaluation demonstrate its performance on vision and languages tasks.

### Strengths
The paper is well-written. The authors clearly describe the problem and their methodology. They also conduct extensive empirical evaluations. 
How to make identity initialization works in practice is an interesting question and I believe it is an novel direction to explore.

### Weaknesses
1. Theoretical analysis seems incorrect and its proof lacks details. In Theorem 3.1, the author claims IDI breaks rank constraint such that its residual has rank more than D_0. However, in the proof in the appendix, the author only shows the full matrix has rank more than D_0, which is not the same as the residual. The core issue lies in the claim that the rank of the gradient $\frac{\partial \mathcal{L}}{\partial \theta^{(k)}}$ will be larger than $D_0$. This is not correct, as the gradient is formed by summing rank-1 matrices (outer products of vectors), and the rank of the sum is bounded by the dimension of the input space $D_0$, regardless of the number of such matrices. The authors need to rigorously demonstrate how the rank of the residual matrix can exceed $D_0$ with a proper mathematical derivation, rather than relying on intuition or empirical results. The current proof is insufficient to support the claim.
2. The authors claim that the rank constraint can be broken by IDI even when non-linearity like ReLU is not applied. It seems contradict approximation theory which emphasizes the importance of non-linearity to ensure expressivity. It would be great for authors to provide more insights on this point. The authors should clarify how IDI achieves increased expressivity without non-linearities, given that linear transformations alone cannot increase the dimensionality of the feature space. This needs to be explained with more theoretical rigor, possibly by showing how the specific structure of the IDI matrices allows for this behavior, and it should be contrasted with standard linear transformations.
3. Authors mention that dead neurons problem happens when batch normalization set to 0 or downsampling operation cause 0 filled features. However, these cases are not common in practice and it's better to motivate more on why IDIZ is important. The motivation for IDIZ is weak, as the scenarios described are not typical failure modes in well-configured networks. The authors need to provide more compelling reasons why IDIZ is essential, perhaps by demonstrating its benefits under more common training conditions or by showing how other initialization schemes fail in these less common scenarios.
4. Insufficient explanation on why momentum is important to solve convergence problem of IDInit. It would be great to provide some theoretical insights to support this factor.

### Questions
1. What is the meaning of zero down-sampling in Table 2, is this a special downsampling operation compared to standard downsampling (like avgpooling) in ResNet?  
2. It would be great to compare IDI, IDI with loose condition, and IDIZ together to show the effectiveness of IDIZ.

### Soundness
2 fair

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the convergence problem in deep networks and proposes a Fully Identical Initialization (IDInit) method that initializes the weights with an identity matrix. The authors propose additional techniques such as momentum, padding, and reshaping to improve convergence and performance.

The overall method has some interesting aspects:
* Patch-Maintain Convolution is introduced as a technique to enhance the universality of IDInit for convolutional layers. It reshapes the convolutional kernel initialized with IDInit to increase feature diversity and improve model performance.
* The issue of dead neurons is tackled by selecting some elements to a small numerical value and increasing trainable neurons.
* The paper discusses the theoretical analysis of IDInit, including the Jacobian and gradient update equations in residual neural networks.

Finally, the authors address the limitations and potential concerns of IDInit, such as its deterministic nature and the need for further exploration in different scenarios.

### Strengths
### S1 - Good technical contributions
The paper's technical contributions are significant in these aspects:
* IDInit improves the convergence speed, stability, and final performance of deep neural networks, addressing a critical issue in deep learning.
* The additional techniques proposed, such as Patch-Maintain Convolution and recovering dead neurons, enhance the universality and robustness of IDInit.
---

### S2 - Theoretical and Experimental analysis
* The paper discusses the theoretical analysis of IDInit, including the Jacobian and gradient update equations in residual neural networks.
* The experiments are well-designed and conducted on various network architectures and tasks, demonstrating the effectiveness and superiority of IDInit.
---

### S3 - Novelty (similar to prior works, but with additional novel contributions)
* Identity init is not new and has been explored in prior works (e.g. ISONet, ZeroO). However, this paper generalizes the Identity Init to various general architectures and activation functions, which is interesting.

### Weaknesses
### W1 - Marginal or no improvement compared to Kaiming init
My biggest concern is the Cifar-10 performance compared to the simple Kaiming initialization.
* Table 2 shows that using SGD optimizer (which gives the best performance all across), Kaiming init obtains almost the same performance (93.36 v/s 93.41 and 94.06 v/z 94.04) as IDInit, while being only slightly slower. 
* This brings into question the practical utility of the proposed initialization.

---

### W2 - Comparisons with other init methods on ImageNet
IDInit is compared with other initialization methods only on Cifar-10, which is very small-scale. No such comparisons have been shown on ImageNet. I think it's important to see if the proposed init is even useful when training on large-scale datasets.

---

### W3 - Theoretical analysis limitations
While the paper provides a theoretical analysis of IDInit, it mainly focuses on the Jacobian and gradient update equations in residual neural networks. It would be valuable to extend the theoretical analysis to other network architectures and provide a more comprehensive understanding of the underlying principles of IDInit.

---

### W4 - Limited discussion on limitations 
Although the paper briefly mentions the limitations of IDInit, such as the deterministic nature and the need for momentum to handle negative eigenvalues, further discussion and analysis of these limitations would provide a more comprehensive understanding of the potential drawbacks and challenges of implementing IDInit in practical scenarios.

### Questions
1. Reference to weakness W2, can you please provide more insight into the efficacy of the propose init method on large-scale training datasets, like ImageNet?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This manuscript proposes a method to initialise networks with identity matrices.
Symmetry of the initialisation is broken by repeating the identity matrix
and adding small (1e-6) perturbations to the diagonals.
Extensions for convolutional layers and fixup-like initialisations are also presented.
Experiments in both vision (CIFAR10 and ImageNet) and language (SST2, TREC6 and BERT pre-training) domains suggest better performance and faster convergence for various architectures.

### Strengths
- (quality) Experimental results are presented with error bars.
 - (significance) This initialisation could reduce some of the randomness in training networks.
   As a result, comparing networks should become easier.
 - (significance) The proposed initialisation should be simple enough to implement, which typically leads to fast adoption by practicioners.
 - (originality) Although the idea to use identity matrices for initialisation has been around for some time, it has typically been discarded as impractical due to the symmetries.
    This is (to the best of my knowledge) the first work that implements an initialisation scheme that sticks so close to the identity matrix.

### Weaknesses
 - (clarity) The idea of dynamical isometry has been introduced in (Saxe et al., 2014).
 - (clarity) I would argue that the patch-maintain convolution is not very well motivated.
   I believe the problem is that I do not understand how this relates to Ghostnets (Han et al., 2020).
 - (clarity) It also took me some time to realise that the channel-maintain convolution (as it is called in the appendix) which is described in the first paragraph of Section&nbsp;3.3.1 is something different from the proposed patch-maintain setting.
   Note that this channel-maintain setting has also been used in (Xiao et al., 2018).
 - (clarity) The ablation experiment in Section&nbsp;4.4 is claimed to explain why channel-maintain is not as good as patch-maintain.
   However, the explanation in section&nbsp;4.4 seems to indicate that this is just an ablation of the different components of the proposed solution.
 - (clarity) I can not find any explanation for the legend of Figure&nbsp;7&nbsp;(a).
 - (quality) The results in Table&nbsp;1 seem to correspond to GD, not SGD.
   A quick experiment with SGD (batch-size 200) learns without problems.
 - (quality) The choice of hyper-parameters is not motivated properly and it is unclear how they were chosen.
   Moreover, it seems like the same hyper-parameter settings were used for every network.
   For a fair comparison, hyper-parameters should be set for each method individually.
 - (quality) An experiment without learning rate schedule, weight decay and other extras would be interesting for a more "raw" comparison between initialisation strategies.
   
 - (quality) The patch-maintain scheme, while presented as a way to increase channel diversity, is not clearly explained. Reshaping the kernels to  $\mathbb{R}^{c_\mathrm{out} \times c_\mathrm{in}k^2}$  results in a matrix with far more columns than rows, leading to a large number of zeros. It's unclear how this sparse structure would promote channel diversity, and a quick test seems to confirm that most kernels are indeed zero. The authors should provide a more detailed explanation or empirical evidence to support this claim.


### Questions
1. Please, include the references listed in the weaknesses section.
 2. What is the link between Ghostnet and the patch-maintain scheme?
 3. Do you have a direct comparison between patch-maintain and channel-maintain schemes for IDInit?
 4. Can you verify that using SGD instead of GD for the results in Table&nbsp;1 also resolves the stated problem?
 5. Is it possible to tune the hyper-parameters for each method individually?
 6. How do weight decay and learning rate schedule interact with the proposed initialisation scheme?
 7. What is the difference between IDInit-0 and IDInit-10 or Kaiming-10 and Kaiming-40 in Figure&nbsp;7&nbsp;(a)?

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent
