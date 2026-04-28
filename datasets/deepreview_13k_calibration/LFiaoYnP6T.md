# IDInit: A Universal and Stable Initialization Method for Neural Network Training

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 6, 6, 5

## Abstract
Deep neural networks have achieved remarkable accomplishments in practice. The success of these networks hinges on effective initialization methods, which are vital for ensuring stable and rapid convergence during training. Recently, initialization methods that maintain identity transition within layers have shown good efficiency in network training. These techniques (e.g., Fixup) set specific weights to zero to achieve identity control. However, settings of remaining weight (e.g., Fixup uses random values to initialize non-zero weights) will affect inductive bias that is achieved only by a zero weight, which may be harmful to training. Addressing this concern, we introduce fully identical initialization (IDInit), a novel method that preserves identity in both the main and sub-stem layers of residual networks. IDInit employs a padded identity-like matrix to overcome rank constraints in non-square weight matrices. Furthermore, we show the convergence problem of an identity matrix can be solved by stochastic gradient descent. Additionally, we enhance the universality of IDInit by processing higher-order weights and addressing dead neuron problems. IDInit is a straightforward yet effective initialization method, with improved convergence, stability, and performance across various settings, including large-scale datasets and deep models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This manuscript studies the initialization methods for deep neural networks. Through an elaborated problem identification, the manuscript proposes several treatments, including (1) padding a new identity matrix in adjacency to an identity matrix, (2) using optimizers with momentum to tackle the convergence issue, (3) improving the universality of IDInit and the identity-control framework from the perspectives of higher-order weights and dead neurons. Extensive numerical results over various neural architectures and datasets demonstrate the effectiveness of the proposed strategy.

### Strengths
* The manuscript is well-structured and well-written. Most concepts are carefully explained and form a good story.
* The numerical evaluations look extensive, considering several baselines and neural architectures on image classification, text classification, and llm pre-training.

### Weaknesses
1. The manuscript may need to elaborate the discussion on the momentum part, e.g., by providing some theoretical justifications. 
2. Some design/hyper-parameter choices are not justified by some references, e.g., many parts in Sec 4 (line 434-line 439, line 449-line 454, line 464-line 474, line 504-line 509, line 517-line 523)

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose an alternative method for neural network initialization that maintains the identity transition. The work uses the block identity-control initialization framework, and as such is composed of two blocks, one identity preserving  (which in case of non-square transformations repeats the identity along the sub-diagonals, instead of zero padding), and zero preserving transformation. The work also discusses how this concept can be used for convolutional architectures, and how its setting may mitigate the dead-neurons problem in identity control.

### Strengths
-  The method is a simple addition to the family of identity-control initialization, which is easy to implement and use. The obtained results are in most studied cases competitive to, or better than other identity-control schemes   
-  The investigation into the ways and mitigating the dead neuron problem with the use of small perturbations in the IDInit method seems interesting and potentially valuable to the community.   
-  While the experiments on various hyperparameters (Section 4.1) are limited in the scope of datasets and models examined, they are potentially insightful, showing that switching to IDInit initialization can lead to a broader range of hyperparameter configurations performing effectively.

### Weaknesses
The are places in the paper in which I am not sure what the empirical evaluation serves to demonstrate, or whether the obtained results are  significant:

1) Firstly, I have concerns regarding Figure 2.  I understand that it serves as a motivation plot for the later claims and I believe that comparing the impact of the initialization of matrix $W_1$ on the performance of various control-initialization setups could be a valuable study by itself. However, my issue is with the presentation of the results. It’s not clear a) What is the model used in this study? b) What is the dataset and task being evaluated? c) What is the type of loss measured and what does “Rectangle Loss” mean? Do the words “Square” and “Rectangle” in the description of the plots refer to the type of matrices used? Additionally, are the lines in Figures 2a and 2b averaged over multiple runs? If so, what is the standard deviation (this is also an opportunity to say something about the stability of those different methods)? Including this information would help demonstrate the stability of the different methods. Finally, where is “Random” in these plots? Is it obscured by another method? Since Figure 2 seems to be an important plot for establishing the importance of introducing the IDInit, I would wish for this plot to be very clear.


2) Figures 8 and Table 3 are potentially valuable, as they involve the largest networks tested in the paper and might capture readers' interest. IDInit appears to outperform the default initialization in these cases, but a comparison with other identity-control methods would be useful to determine if the performance gain is due specifically to IDInit or identity-control in general. Although these experiments are resource-intensive, reporting the mean and standard deviation over multiple runs would help evaluate whether the performance differences are statistically significant.

Overall, the paper is well-written, but there are sections with vague claims or unclear intent:

3) Lines 110–114 state, “By further proposing modifications to CNNs and solutions to dead neuron problems we have significantly improved accuracy by…”. It is unclear what task, network, or dataset this refers to, or what it is being compared to—state-of-the-art methods or alternative identity-control techniques? Since this is part of the main contributions section (end of Section 1), this ambiguity is distracting, particularly as similar wording appears in lines 115–116: “On ImageNet, IDInit can achieve almost all the best performance…”. Again, compared to what? I suggest being specific or moving such claims to the experimental results section, where precise differences in accuracy can be reported.  
4) The definition and understanding of dynamical isometry from the related work seems to be slightly inadequate. I.e. we say that a network attains dynamical isometry if all the singular values of the input-output Jacobian are equal to 1. This is not equivalent with operating at the criticality regime $X=1$. In fact, for certain initialization and activations (e.g. orthogonal with ReLU), it is possible to operate in the criticality regime, yet never obtain the dynamical isometry property (see Section 2.5.2 of Pennington 2017). I know it does not seem to be a huge issue, since the dynamical isometry is not the center of attention of this paper, but it raises doubts whenever dynamical isometry is mentioned in the paper.  
5) In Section 3.1.1's convergence analysis, the statement, “as $\eta$ is usually 1e-1 and both training pairs…” is unclear. It is not accurate to label any learning rate as “standard” or “usual,” which makes the comment about the “magnitude of the asymmetric component” vague. Instead, it would be more informative to discuss the constraints or boundaries for the $\eta$ parameter that ensure broken symmetry.  

These issues, while not critical individually, collectively (together with some other issues -- see section “Questions”) make the paper challenging to follow.

### Questions
1) In Appendix A3, what is the upper index in $x_i^{(0)}$ ? Why in $\Pi_1$ in the derivative it changes to 3? Also, should not Theorem 3.1  also include some constraints on the batch size, since this will influence the rank of the gradients?   
2) In Figure 2, I am not sure if I understand what Identity-1 is? Is it simply initializing W1 to Identity (since the matrices  for plot 2b are squared)?   
3) In Equation (3), how is $\tau$ determined for different activation functions? It does not seem to be specified in the paper.   
4) I liked the hyperparameter experiments from Section 4.1 and actually maybe even wished for this part to be more extended. If IDInit improves the stability over other initialization schemes, it would be nice to highlight this more (e.g. repeat Figure 7 on more datasets, by commenting on the standard deviation of the loss during the runs, etc.)     

**Minor**:

- How do the results in Figure 2 change with varying matrix sizes?  
- A suggestion: remove the word “Some” from the caption of Figure 8, as it diminishes the perceived significance of the experiment.  
- The term “residual stem” was initially unclear. Introducing and defining this term earlier in the paper might help readers understand it more quickly.  
- Lines 134–135: The phrase, “In this paradigm, the input-output Jacobian is calculated as…” is somewhat confusing. Equation 2 simply defines the input-output Jacobian, and its definition does not change based on whether it is viewed through the lens of dynamical isometry. I recommend removing the phrase “In this paradigm” for clarity.


Since currently the weaknesses outweigh the strengths of the paper, I am slightly leaning more towards rejection rather than acceptance.

### Soundness
3

### Presentation
2

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
In conclusion, this paper introduces Fully Identical Initialization (IDInit), a novel approach that leverages an identity-like matrix to effectively preserve identity across both main and sub-stem layers of residual networks. This method addresses the rank constraints in non-square weight matrices through a padded identity-like matrix and improves upon traditional identity matrix convergence issues using stochastic gradient descent. By processing higher-order weights and tackling dead neuron problems, IDInit enhances stability and performance, demonstrating improved convergence in various settings, including large-scale datasets and deep models.

### Strengths
- This paper introduces IDInit, a novel initialization method that utilizes an identity-like matrix to preserve identity across both the main and sub-stem layers of residual networks. IDInit accelerates the training process across diverse datasets and neural architectures.
- An effective initialization method is crucial for the deep learning community.
- The paper offers a clear presentation, including well-demonstrated experimental results and a robust technical solution.
- Several claims are theoretically supported. Notably, the paper demonstrates how this method can address the rank constraint problem.

### Weaknesses
 - In certain instances, IDInit remains suboptimal. For example, in Table 1, the final accuracy of a 110-layer neural network does not surpass the baselines.
- The proposed IDInit has not been validated across diverse learning paradigms, such as self-supervised learning methods and diffusion models.
- The paper lacks theoretical analysis regarding the convergence rate of IDInit.

### Questions
- Could you include additional experimental results involving self-supervised learning methods and diffusion models?
- Could you provide further theoretical analysis on the convergence rate of IDInit?

### Soundness
3

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
3

### Summary
This paper proposes a new initialization method for deep neural networks. It aims to initialize residual branches to have output close to zero, but keep an identity-like initialization in linear transformations on the residual except for the final one. They focus on the case where the feature dimension of the residual differs from that of the skip connection (typically wider), covering both convolutional and MLP style residuals. The authors analyze their initialization and experimentally validate its performance across various neural networks.

**Recommendation:** I lean towards rejection. The core idea is interesting and the results seem promising but I think the paper would benefit from a significant rewrite to improve the presentation clarity as well as better controlled comparison experiments.

### Strengths
- Problem tackled is practical and of interest to the community 
- The core idea is interesting
- Authors claim decent performance improvements

### Weaknesses
 - This paper is very hard to follow. It frequently relies on citing prior works without summarizing or explaining their results sufficiently. The setup is not explained well, it is often hard to tell if there are non-linearities between the matrices, if normalization layers are used etc. The notation is not consistent throughout the paper. Finally the paper is full of spelling and grammar mistakes as well as poorly phrased sentences.
- Some of the experiments are not convincing e.g. in Section 4.1 and 4.2. In general the hyperparameter tuning might not provide a fair comparison between methods.

- Why change the notation from Figure 1 to Equation 1? What do you mean when applying the activation function to the weights / transformation in Equation 1? This notation is not defined or explained.
- Many aspects of Figure 2 are unclear. Does this network have activation functions? Why is the learning rate not tuned per method? Why is the rank issue so significant here despite the matrices being almost square? I find it hard to believe that a difference of 40 features out of 280 can cause such a large difference between the methods. Why use Adagrad and not a more standard optimizer like SGD or Adam?
- Figure 3: I think this would be clearer if you used one symbol for the number of features on the skip path and another for the intermediate dimension. Here D_i is used twice to mean different dimensions.
- Figure 4: I feel that when comparing momentum to no momentum the learning rate must be taken into account. Using momentum in SGD increases the effective learning rate so it is not surprising that the difference is larger.
- Lines 314-318: Here you introduce the “loose” condition where you add random noise to your leading matrices. However, this is not mentioned again. Are the later experiments conducted with this change and does it make a difference in practice?
- Section 4.1: I don’t find this convincing. The granularity of the sweep is too high and the best performance for the Kaiming initialization occurs at the edge of the sweep.
- Section 4.2: I also don’t find this very convincing. In general the hyperparameters need to be tuned per method for a fair comparison. How do we know that your hyperparameters don’t favor your method?
- Section 4.3: Here I feel you could explain the exact setup a bit better, e.g. what exactly do you do without IDIC?

### Questions
- Why change the notation from Figure 1 to Equation 1? What do you mean when applying the activation function to the weights / transformation in Equation 1? This notation is not defined or explained.
- Many aspects of Figure 2 are unclear. Does this network have activation functions? Why is the learning rate not tuned per method? Why is the rank issue so significant here despite the matrices being almost square? I find it hard to believe that a difference of 40 features out of 280 can cause such a large difference between the methods. Why use Adagrad and not a more standard optimizer like SGD or Adam?
- Figure 3: I think this would be clearer if you used one symbol for the number of features on the skip path and another for the intermediate dimension. Here D_i is used twice to mean different dimensions.
- Figure 4: I feel that when comparing momentum to no momentum the learning rate must be taken into account. Using momentum in SGD increases the effective learning rate so it is not surprising that the difference is larger.
- Lines 314-318: Here you introduce the “loose” condition where you add random noise to your leading matrices. However, this is not mentioned again. Are the later experiments conducted with this change and does it make a difference in practice?
- Section 4.1: I don’t find this convincing. The granularity of the sweep is too high and the best performance for the Kaiming initialization occurs at the edge of the sweep.
- Section 4.2: I also don’t find this very convincing. In general the hyperparameters need to be tuned per method for a fair comparison. How do we know that your hyperparameters don’t favor your method?
- Section 4.3: Here I feel you could explain the exact setup a bit better, e.g. what exactly do you do without IDIC?

### Soundness
2

### Presentation
1

### Contribution
3
