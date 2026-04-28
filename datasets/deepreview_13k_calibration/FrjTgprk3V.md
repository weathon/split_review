# Emergence in non-neural models: grokking modular arithmetic via average gradient outer product

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 5

## Abstract
Neural networks trained to solve modular arithmetic tasks exhibit \textit{grokking}, a phenomenon where the test accuracy starts improving  long after the model achieves $100\%$ training accuracy in the training process.  It is often taken as an example of ``emergence'', where model ability manifests sharply  through a phase transition. In this work, we show that the phenomenon of grokking is not specific to neural networks nor to gradient descent-based optimization. Specifically, we show that this phenomenon occurs when learning modular arithmetic with Recursive Feature Machines (RFM), an iterative algorithm that uses the Average Gradient Outer Product (AGOP) to enable task-specific feature learning with general machine learning models.  When used in conjunction with kernel machines, iterating RFM results in a fast transition from random, near zero, test accuracy to perfect test accuracy. This transition cannot be predicted 
from the training loss, which is identically zero, nor 
from the test loss, which remains constant in initial iterations.  Instead, as we show, the transition is completely determined by feature learning: RFM gradually learns block-circulant features to solve modular arithmetic.  
Paralleling the results for RFM, we show that neural networks that solve modular arithmetic also learn block-circulant features. Furthermore, we present theoretical evidence that RFM uses such block-circulant features to implement the \textit{Fourier Multiplication Algorithm}, which prior work posited as the generalizing solution neural networks learn on these tasks.  Our results demonstrate that emergence can result purely from learning task-relevant features and is not specific to neural architectures nor gradient descent-based optimization methods.  Furthermore, our work provides more evidence for AGOP as a key mechanism for feature learning in neural networks.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the phenomenon of grokking in non-neural models, specifically Recursive Feature Machines (RFMs). In the setting they study (modular arithmetic), skills emerge purely from feature learning and a block-circulant pattern emerges in the learned square root of the AGOP matrices. Similar to previous work they identify progress measures related to the block circulant structure of the feature matrices which linearly improve during grokking. They also connect their findings to neural networks, showing that the NFM and neural network AGOP exhibit high correlation and contain a similar block circulant structure. Finally, they prove that kernel machines with these block circulant features implement the Fourier multiplication algorithm previously discovered to be implemented by neural networks to solve modular arithmetic.

### Strengths
- The paper is written and organized well, with the significance of the results in each section clear. 
- While it is a kernel setting, there are several interesting empirical results that cleanly exhibit grokking, the emergence of structured features, and linear progress measures despite training loss being 0 throughout.
- The demonstration of grokking in their kernel setting challenges proposed explanations for grokking, such as grokking having a ‘lazy’ and ‘rich’ regime  with no feature learning and feature learning respectively.
- This work suggests that there is a gap in our available theory to provide effective measures for generalization and explanations for mechanisms of emergence. I believe the work may be valuable to make a call to the community for a need of better theoretical tools and other directions (such as developing progress measures that are more general/applicable without having access to the training mechanism apriori, and are not tied to metrics like loss).

### Weaknesses
 - This work focuses on a particular task, providing evidence that there may be tasks in which skills can emerge purely as a result of feature learning and independent of loss, but the scope of the results extending to other task and the use case of this particular kernel machine setting is less clear.
- There is still a gap between theory and experiment where there lacks a theoretical proof that grokking will occur, or identify what the mechanism is behind learning modular arithmetic from a finite set of samples.
- I’m not very familiar with the prior literature on RFMs and the use of AGOPs to explain feature learning for neural networks; I know there is context sprinkled throughout in section 2, but it might be useful to reframe Appendix A as a more consolidated review of its introduction and previous use cases.

### Questions
1. The empirical validity of emergence has been a popular and contentious point of discussion in the community. Even after Schaeffer’s work, there still does remain tasks which seem emergent independent of metric choice. Do the authors have any thoughts about characteristics of tasks that will predict emergence, or what type of tasks will exhibit emergent behavior? 
2. How does the grokking behavior trend with the training fraction? 
3. The RFM and NN learn a similar mechanism for the tasks (i.e. implement the Fourier multiplication algorithm)-- in general, to what extent are these learned solutions for tasks exhibiting emergence ‘universal’? Could there be tasks where learned mechanism differs across algorithm or architecture, highlighting a difference in inductive bias? I'm curious if the authors tried training RFMs on other synthetic tasks that have been popular for studying grokking, such as general group operations; I'm wondering if similar structure is observed for eg. group operations on S_5 and S_6, where proposed circuits in neural networks seem to have differing perspectives (learning irreducible representations versus learning subgroup/coset structure [1]).

[1] Stander, Dashiell, et al. "Grokking Group Multiplication with Cosets." arXiv preprint arXiv:2312.06581 (2023).

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper attempts to isolate feature-learning in modular arithmetic tasks. They show that the known Fourier-features that are observed in neural networks grokked on modular arithmetic tasks (they call such features Fourier Multiplication Algorithm) can be viewed as "circulant-matrix" structure of input-output Jacobians (called AGOP) along with a global transformation via ridgeless kernel regression. They show that a non-parametric algorithm (RFM) that iteratively refines the kernel using AGOP can grok modular arithmetic tasks and find the aforementioned circulant features. They define progress measures to show the gradual learning of features as well as the agreement between the non-parametric vs neural-network-based training. They also show that initializing network weights using the circulant features accelerates training.

### Strengths
- The paper is written in a clear, easy-to-follow manner.
- The supporting experiments are well-presented.
- Studying feature-learning in modular arithmetic tasks with non-parametric methods such as RFM is new. This analysis isolates feature-learning from the neural network training for this task.
- Proofs supporting their claims are presented in the Appendix.

### Weaknesses
 - Their method is essentially a different way of describing the already-known features in modular arithmetic [1,2]. Continuous progress measures  for this task also already exist in literature, and not new to this work [1,2]. Consequently, the main contribution of this work, in my opinion, is to show that such features can also be reached by using the non-parametric method, viz. RFM. Since the RFM method is also not new to this work [3], I am unable to identify the significant contribution of this paper. 
In a barebones way, the message seems to be "The known RFM method applied to modular arithmetic task leads to the known features, as it should."

- The modular addition task $f(a,b) = a + b \;mod\; p$ (and other arithmetic tasks after the appropriate re-ordering) respect the modular version of "translation symmetry" in the inputs $a,b$ (i.e. $f(a+t \;mod\; p, b-t \;mod\; p) = f(a,b)$). Therefore, the feature-matrix of a network that solves this task must also respect this symmetry. This symmetry constraint readily gives the random circular matrix as the feature-matrix, making it trivial in some sense.
(After applying this symmetry, the remaining task is to assign each symmetry class to its correct label, which can be readily achieved by kernel regression.)

### Questions
- Do the authors understand why there is a difference in the progress measures between add/sub and mul/div tasks in Figure 5 (B)? Is it related to the fact that mul/sub operations have to deal with 0 separately? 

- Can the analysis presented in the work be used to predict the sample complexity of modular arithmetic tasks?

- My understanding is that the circulant features are identical to the Fourier-features found in literature (up to a global transformation learned by kernel regression). Is this assertion correct?

[1] Nanda et al., Progress measures for grokking via mechanistic interpretability (2023)

[2] Gromov, Grokking Modular Arithmetic (2023)

[3] Radhakrishnan et al., Mechanism for feature learning in neural networks and backpropagation-free machine learning models (2024)

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper examines the phenomenon of grokking in the context of modular arithmetic tasks. Using Recursive Feature Machines (RFM), which learn features through Average Gradient Outer Product (AGOP) updates rather than gradient descent. The authors show that grokking is not specific to neural networks or gradient descent optimization, but rather arises from feature learning itself. On top of that, the authors introduced different progressive measure that correlates with test accuracies. They also find block-circulant features that implement the Fourier multiplication algorithm.

### Strengths
1. Kernel method is rarely discussed in grokking settings
2. The authors discuss their methods clearly
3. Good connection with existing literatures

### Weaknesses
1. More discussion on the importance of data is needed:
    - Previous research (e.g., https://arxiv.org/abs/2201.02177) has established that there exists a minimum data threshold required for model grokking. For this kernel-based method, the behavior of this threshold remains unclear. The paper would be significantly strengthened if the authors investigated this threshold using their approach, as their method has fewer hyperparameters, which could provide compelling evidence for the essential role of data quantity in enabling grokking. 
    - At least, I would like to see a test-acc vs training data amount curve for the authors' method compared to say GD/Adam training, together with how the learned kernels change with the amount of data during training, especially how the kernels fail to form the correct feature when there is no enough training data.

2. The insight that feature learning is central to grokking is not completely new, for instance, the work in https://arxiv.org/abs/2310.06110 demonstrates the train loss of a neural network decreases much earlier than its test loss can arise due to a neural network
transitioning from lazy training dynamics to a rich, feature learning regime.
3. The mechanism behind the emergence of circular features during algorithm execution remains unclear, which seems crucial for understanding grokking, particularly from a dynamics perspective. From the curves I saw from the paper, I would expect some kind of lazy-to-rich transition happens here as well.

### Questions
1. Could the authors provide intuition about how RFM leads to this grokking behavior from the perspective of their iterative algorithm?
2. Is the amount of data required for grokking comparable between this algorithm and other optimization methods like GD/Adam?
3. Does the $p$ play a significant role? What are the implications of using a non-prime modulus?

### Soundness
2

### Presentation
3

### Contribution
2
