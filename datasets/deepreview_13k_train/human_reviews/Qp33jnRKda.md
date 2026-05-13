# Growing Tiny Networks: Spotting Expressivity Bottlenecks and Fixing Them Optimally

- Decision: Reject
- Scores: 5, 5, 5, 6

## Abstract
Machine learning tasks are generally formulated as optimization problems, where one searches for an optimal function within a certain functional space.
In practice, parameterized functional spaces are considered, in order to be able to perform gradient descent. 
Typically, a neural network architecture is chosen and fixed, and its parameters (connection weights) are optimized, yielding an architecture-dependent result. 
This way of proceeding however forces the evolution of the function during training to lie within the realm of what is expressible with the chosen architecture, and prevents any optimization across %possible 
architectures.
Costly architectural hyper-parameter optimization is often performed to compensate for this. Instead, we propose to adapt the architecture on the fly during training. 

We show that the information about desirable architectural changes, due to expressivity bottlenecks when attempting to follow the functional gradient, can be extracted from %the 
backpropagation. 
To do this, we propose 
a mathematical definition of expressivity bottlenecks, which enables us to
detect, 
quantify and solve them while training,
by adding suitable neurons when and where needed.
Thus, while the standard approach requires large networks, in terms of number of neurons per layer, for expressivity and optimization reasons, we are able to start with  very small neural networks and let them grow appropriately. 
As a proof of concept, we show 
results~on the CIFAR dataset, matching large neural network accuracy, with competitive training time,
while removing the need for standard architectural hyper-parameter 
search.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The submission presents a novel method to increase the width of a network during optimization, inspired from a functional argument. The method starts from the gradient of the loss wrt the output of the network, and finds weights by trying to align the output to this desired change.

### Strengths
The method is novel and the problem of fitting both the weights and the architecture at the same time is relevant and very much open. I have heard the idea of "let's do gradient descent on the architecture" multiple time, but little in the way of actual attempts to define what is meant by that statement, which is welcome.

### Weaknesses
The paper presents an interesting idea and I am generally positive towards it, but I found it hard to get the intended message. I think it would greatly benefit from an update to improve the clarity of the message, especially on the following points
- The presentation of the functional analysis viewpoint. I found it hard to follow, probably due to notation overload.
- The submission seems to not directly address how to trade-off increasing number of parameters vs. updating the parameters we already have.
- Given that a stated contribution of the submission is a definition of optimality, what is meant by that should be stated explicitly.
- Some statements should be made more carefully to avoid overly general claims.

I give more details and specific examples of each of the points below. I will increase my score if these points are adressed by a revision during the discussion period.

As my issues have to do with clarity, I tried giving specific and clear descriptions, leading to a possibly (overly long) review. The length of the section below should not be taken as a negative assesment of the submission. My hopes is that those can help the authors make the message of the paper clearer.

---

## Details

**Clarity of the functional view**

I might be missing some key background reference, but I struggle to follow section 2.2. My understanding of the high-level idea is that $v_{\text{goal}}(x)$ indicates the desired change in output of the network by indicating what infinitesimal change in the output of the network is desired. This goal reasonable and I wouldn't have an issue if it had been stated as such, but I don't understand how it follows from the functional perspective outlined in §2.2.

The notation seems overloaded to represent the functional and the "standard" ML notation. The lack of distinction makes the text hard to parse. For example, the expression $\nabla_{f}\L(f)$ implies that $\L$ takes a function, but in $\nabla_{u=f(x)} L(u)$, it is evaluated at the output of the network, a vector in $\R^p$.

The text also implies that $\nabla_f \L(f) = \nabla_{u=f(x)} \L(u)$" by the definition and evaluation of $v_{\text{goal}}$. Assuming my interpretation above is correct, this equivalence is not obvious to me. It would benefit from an explanation as to why it holds, or a reference. It is also unclear to me why this holds without defining the space of functions, for example whether $\mathcal{F}$ is the class of function representable by any width-$M$ networks and taking the union over all $M$s, some RKHS, or whether we any arbitrary pathologic discontinuous functions is allowed.

**Balancing optimization and adding parameters**

The last contribution states that the submission "naturally obtain[s] a series of compromises between performance and number of neurons, in a single run, thus removing the need for width hyper-optimization". I would expect this contribution to refer to a particular result highlighting how the proposed methods trades-off (a) fitting the current architecture/doing more traditional GD steps vs. (b) adding neurons. Unless I missed something, the proposed method does not inherently address this tradeoff, and instead adds a fixed number of neurons. This seems to be replacing the width hyperparameter by a "how-much-width-to-add" hyperparameter. The method can still be an improvement by lowering the dependency of the performance on the hyper-parameter, but should be discussed more directly in the main text.

**Definition of optimality**
  
The submission uses the term optimal in many instances with what appears to be different meanings. It is not clear what criteria is used to establish optimality. To take an example from optimization, gradient descent being optimal could refer to the fact that it is the result of minimizing a surrogate quadratic problem, or to say that it attains the best rate of convergence among first-order algorithms in some problem class.

As the goal of the submission is to "mathematically define the best possible neurons" and fixing expressivity bottlenecks "optimally", it would be beneficial to be explicit about what is meant by "optimal". Especially as the submission can be interpreted as proposing two definitions; one implied in §2.2 as minimizing the distance between $v_{\text{goal}}$ and the actual update, and another looking at the layers independently in 2.3 to make the problem tractable (especially as the submission states in §3.3 that "this move is sub-optimal").

For example, "picking optimal directions that avoid redundancy in the pre-activation space" at the end of the submission seems to reflect that "optimal" is taken to mean the optimal direction to decrease the first-order approximation of the loss, a concept that is missing from other instances such as "Optimal functional move", "The optimal update of the weights at a given layer", or the optimality in Prop 3.2.
  
**Overly broad claims**

- (Intro) "This removes the optimization issues (local minima) that usually arise when considering thin architectures"; "remove optimization issues" is too broad, and might imply that local minima are the only optimization problem. The contribution should state that it is possible to avoid some local minima (with a forward reference to the specific result in §4), or specify that this result applies to 1-hidden-layer networks.
- (§3.2) "[adding random neurons] would not yield any guarantee regarding the impact on the system loss"; I read this sentence as implying that this is in contrast with the proposed method, which then should have a guarantee that adding the proposed neurons decreases the loss. As no such results are presented, the description should be changed.
- Going into §2.3, I interpreted the description of "recursive" as implying that some invariant would be maintained, and specifically that the resulting update wouldn't change. To avoid this confusion, I would suggest being explicit are the start of §2.3 that what follows is a an approximation to what is desired in §2.2, as this only spelled out in §3.1.


**Related work**
The description of prior work could be more detailled to help readers unfamiliar with the literature. For example, it is not clear how the description of Net2Net, AdaptNet and MorphNet ("propose different strategies to explore possible variations of a given architecture") differs from the approach proposed here.

I was also surprised to not see a citation to the classical works of neuron boosting/incrementally learning a neural network one neuron at a time (For example, Bengio, Le Roux, Vincent, Delalleau, and Marcotte. Convex neural networks. 2006, or other references found in the GradMax paper of Evci et al.), which I think would be relevant for historical context.

Although focused on optimization of a fixed architecture, there is a line work in optimization for deep learning that takes a constrained optimization/Lagrangian view to obtain per-layer updates that look similar to the recursion argument in §2.3--§3.1. The following works might be of interest to the authors if they were previously unaware of those. _(to be explicit; although I do believe there is a connection and that some discussion could be beneficial, I am not requesting that the submission cite those works)_
- Lecun. A Theoretical Framework for Back-Propagation. Proceedings of the 1988 connectionist summer school
- Carreira-Perpiñán and Wang. Distributed optimization of deeply nested systems. AISTATS 2014.
- Taylor, Burmester, Xu, Singh, Patel and Goldstein. Training Neural Networks Without Gradients: A Scalable ADMM Approach. ICML 2016.
- Frerix, Mollenhoff, Moeller and Cremers. Proximal Backpropagation. ICLR 2018.
- Amid, Anil and Warmuth: LocoProp: Enhancing BackProp via Local Loss Optimization, AISTATS 2022

---

**Minor points (no need for a response):**
- "Under standard weak assumptions (A.1)" made me think I should look for a an "Assumption 1", as this style of reference is common. I'd suggest spelling out "(see Appendix A.1)".
- (after Prop 4.3) "by requiring the added neuron to have infinitely small input weights"; a literal interpretation of this sentence requires the inputs to be 0. I suggest rephrasing in terms of "direction" instead.
- What "time" in $\frac{\partial\theta}{\partial t}$ is not defined,
- "shown empirically to be better optimized than small ones Jacot et al. 2018" seems to imply that this is what Jacot et al. shown. I assume the citation should have been moved earlier in the sentence, for the theoretical part.  
- There are multiple instances where \citet and \citep are mixed, leading to missing parentheses around citations, especially in paragraphs discussing related works ("Notions of expressivity" paragraph)
- The "amplitude factor $\gamma$" used in the Algorithm given in Fig. 6 seems undefined in the main paper.

### Questions
The specifics of my points above do not require a response and can instead be adressed through a revision, although I am open to a discussion if the authors disagree with my comments.

For specific questions;

- **Clarity of the functional view**

  Are the notation issues identified above correct, or did I completely miss something? If so, what is the formal definitions of the objects used, and why is the functional gradient the same as the derivative wrt the output of the network?
  (Those questions be adressed by a revision to the paper and need not be written in openreview posts)

- **Balancing optimization and adding parameters**

  Shouldn't the functional view provide a way to perform this trade-off, for example through some regularization parameter that could impact how much better the "adding new weights" step should be vs. updating existing weights?

- **Complexity of the methods** 

  The introduction claims that the method is is "competitive" in computational complexity with standard training. However, it seems that the methods requires the computation of SVDs of matrices whose size dependent on the width of the network, and the complexity should scale (at least) with that width squared, which is much more than gradient descent. Could the authors clarify what was meant?

### Soundness
1 poor

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper shows how to grow tiny networks by leveraging the functional gradient to optimize the network architecture on the fly. They define the expressivity bottlenecks by the distance between the desired activity update and the reachable update from the current parameter space. And they greedy reduce the expressivity bottlenecks during training when neurons are added.

### Strengths
The problem is interesting and well-defined mathematically. Theoretically, they show how to solve the problem and have solid propositions and proofs, although I did not follow most of them. Empirically they compared their method to the previous method showing that they achieve better accuracy on cifar10 when growing from a tiny model.

### Weaknesses
The paper is not easy to follow and there are a lot of typos in the paper, i.e., missing figure number in section 3, no caption for the algorithm. I do think we should have a main algorithm that describes the whole training process, like how function gradients are calculated and how the optimization problem is solved according to which proposition. Empirical results seems very limited even compared to the baseline methods, such as gradmax. The paper lacks clarity on how the functional gradient is actually computed within the backpropagation process, making it difficult to assess the practical implementation. Furthermore, the experimental section does not adequately explore the method's performance across diverse architectures and datasets. The comparison to gradmax is limited, and it is unclear how the proposed method scales to larger, more complex models or datasets beyond CIFAR-10. The absence of a detailed analysis of the computational overhead associated with the proposed neuron addition strategy also raises concerns about its practicality for large-scale applications.

### Questions
How do we add neurons to the convolutional layers? Are we structurally adding kernels or adding neurons treating them as fully connected layers?

What are the benefits of the proposed method? Are we trying to have a method that tries to get the best model among a certain size or a method that can efficiently and effectively grow a tiny network to an arbitrary size? If it is the latter one, can we have some experiments with models that people use in practice?

What is the computational cost of the proposed methods?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
TINY is proposed to grow neural network architectures with the aim to remove expressivity bottlenecks. The authors propose a scheme to increase the width of a considered feed-forward neural network architecture (with either fully-connected or convolutional layers) by adding neurons and thus increasing the width of the network during the growth process. (No dynamic addition of layers or other modules is considered.) 
The proposed method is similar to GradMax but tries to avoid adding redundant neutrons.

### Strengths
- The authors work on a timely problem and try to reduce the computational requirements of deep learning by growing relatively small neural networks rather than training large ones from scratch.
- The authors aim to reduce redundancy in the addition of neurons when neural networks are grown.
- The proposal is theoretically motivated based on potential optimal additions of neurons in function space.
- The experiments show improvements in test accuracy over GradMax on CIFAR10.

### Weaknesses
 - The exposition lacks a related literature discussion. While the introduction mentions different lines of research, it mostly focuses on early works in the related directions. Only Section 3 mentions a few related works on neural architecture growth and redundancy, which are easy to miss in the middle of the paper. As a result, an overview of the state of the art is missing.
- A similar criticism also holds for the experiment section, which only compares with GradMax and not different types of approaches. The lack of comparison with other methods makes it difficult to assess the true contribution of the proposed approach.
- It is impossible to deduce from Section 3 what the actual algorithmic proposal is. The links in the algorithm to the supplement are broken. (The actual description is on page 15.) The actual update equations are not provided in the main paper. This lack of clarity makes it difficult to reproduce the results and understand the technical details.
- Limitation: It appears that the number of neutrons that are added in each step is a hyper-parameter. This introduces an additional tuning step that might limit the practical applicability of the method.
- The update seems to involve a spectral decomposition to avoid neuron redundancy that is computationally costly. The computational cost of this step is not sufficiently analyzed, raising concerns about the scalability of the method.
- The computational complexity of the full training process (including the network growth) has not been evaluated, even though it forms in integral part of the claimed contributions. This makes it difficult to assess the practical efficiency of the approach.
- The method is not very flexible in adding layers or different kind of modules. It only grows the width of a chosen architecture. This limits the applicability of the method to a narrow range of architectures.
- The novelty of the method appears to be limited in comparison with GradMax. The incremental improvement over GradMax is not sufficiently justified.
- Experiments are limited to CIFAR-10, a relatively small dataset of low complexity. (Note that GradMax was evaluated also on CIFAR-100 and ImageNet.) The lack of experiments on more complex datasets limits the generalizability of the results.
- The performance of the learned models on CIFAR-10 lacks far behind the test accuracy that can be achieved on this dataset with standard, relatively small ResNet architectures (like ResNet18). This raises questions about the practical relevance of the proposed approach.


Minor points:
- Broken figure link in Section 3 on page 4.
- The supplement is not included in the main paper so that important links are broken (see algorithm, for instance).


### Questions
- How does the proposed method perform on CIFAR100 and ImageNet?
- How is the matrix N on page 15 computed, since it depends on the (unknown?) $V_{goal}$?
- What is the runtime complexity of an update step?
- How do the computational requirements compare with training just a wider model from scratch once?
- How does training the obtained end neural network from scratch compare to the proposed training + growing process? Is a real improvement in generalization performance observed?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work proposes a method to augment network architectures by finding layers with an "expressivity bottlenecks" and widening the network there. 

Specifically, they calculate the functional derivative $v_\text{goal} = - \nabla_{u = f(x)} \mathcal{L}(u)$ characterizing the best infinitesimal variation of the outputs of $f$ to decrease the loss at $x$. The derivative $v_\text{goal}$ is then compared with its projection on the tangent space $T_\mathcal{A}^{f_\theta}$ of the manifold $F_\mathcal{A}$ (networks with architecture $\mathcal{A}$) at the point $f_\theta$. The norm of the difference between these two directions is used to quantify the expressivity bottleneck. This gets also generalized not just for the logits $u$ but for all pre-activation values $a_l$. 

The authors continue by providing a procedure how one calculates the best variation of the parameters for one layer $\delta W_l^*$ (Proposition 3.1) in order to calculate the expressivity gap $\Psi^l$, as well as a procedure to add neurons and initialize them optimally (Proposition 3.2). A series of Propositions (4.1 - 4.3) follow, shining light on the properties regarding the greediness of the approach. 

The proposed approach is evaluated on the CIFAR-10 dataset. The authors start with an architecture consisting of two blocks of 2 convolutions and 2 MaxPooling each followed by two fully-connected layers using selu activation. The proposed method outperforms GradMax. The authors attribute this to the redundancy of GradMax. 

Minor comments:
- in 2.2, paragraph "Optimal move direction" should $\Theta$ be $\Theta_\mathcal{A}$? 
- Proof for 3.2 in the appendix: the first sentence seems incomplete

### Strengths
- The idea is interesting
- The approach appears to be sound, although the reviewer could not verify the proofs (maybe due to some misunderstandings, see more in the questions). 
- Overall well written, although the technical reasoning should be improved.
- Mentioned Limitations where insightful.
- Helpful Appendix.

### Weaknesses
 - The limitations regarding more complex datasets remains unclear. 
- There don't seem to be many experiments: How does the method perform on other seed architectures? 
- The math, especially the proofs should be more detailed.

- I could not find a formal definition for $\partial / \partial t$ in Section 2.2
- Proposition 3.1 (Appendix):
	- What happens in the step where after "$M^+$, we get:"? To me it looks like you substituted $\delta W_l$ with $\delta W_l^*$ in $V_\text{goal}^l B_{l-1}^T = \delta W_l B_{l-1} B_{l-1}^T$, as this is where the gradient of $g(\delta W_l)$ vanishes, and then multiplied $\tfrac{1}{n} (B_{l-1} B_{l-1}^T)^+$ from the right. However, i am missing the reasoning why $B_{l-1} B_{l-1}^T \tfrac{1}{n} (B_{l-1} B_{l-1}^T)^+ = I$. 
- Proposition 3.2: 
	- As $S$ is just positive semi-definite ($S := \tfrac{1}{n} B_{l-2} B_{l-2}^T$) and not necessarily positive definite (i.e. may not have full rank), how do we know that $S^{-1/2}$ exists in Proposition 3.2? 
	- Of which matrix are $\lambda_k$ the Eigenvalues? Currently i see that they are the singular values of $S^{-1/2} N$. 
Overall, especially Proposition 3.1 and 3.2 would really benefit from detailed explanations. 

- Does you method scale to ImageNet?
- Did you compare the three different initialization approaches? Random initialization, zero initialization and your in Proposition 3.2 proposed initialization?  
- Which hardware did you use to run your experiments?

### Questions
In no particular order: 

- How does the approach compare to NEAT based techniques? What are differences / communalities? 

- How well would your approach work on datasets with lower signal to noise ratio compared to CIFAR-10? Would you expect to see overfitting? 
- How do you terminate the training procedure? Is there some schedule according to which you pick which layer gets widened? Do you pick the layer with the largest (normalized) expressivity gap? 
- what exactly do they improve?
- Did you consider combination of standard gradient descent and your proposed method? How would they work out? 

- I could not find a formal definition for $\partial / \partial t$ in Section 2.2
- Proposition 3.1 (Appendix):
	- What happens in the step where after "$M^+$, we get:"? To me it looks like you substituted $\delta W_l$ with $\delta W_l^*$ in $V_\text{goal}^l B_{l-1}^T = \delta W_l B_{l-1} B_{l-1}^T$, as this is where the gradient of $g(\delta W_l)$ vanishes, and then multiplied $\tfrac{1}{n} (B_{l-1} B_{l-1}^T)^+$ from the right. However, i am missing the reasoning why $B_{l-1} B_{l-1}^T \tfrac{1}{n} (B_{l-1} B_{l-1}^T)^+ = I$. 
- Proposition 3.2: 
	- As $S$ is just positive semi-definite ($S := \tfrac{1}{n} B_{l-2} B_{l-2}^T$) and not necessarily positive definite (i.e. may not have full rank), how do we know that $S^{-1/2}$ exists in Proposition 3.2? 
	- Of which matrix are $\lambda_k$ the Eigenvalues? Currently i see that they are the singular values of $S^{-1/2} N$. 
Overall, especially Proposition 3.1 and 3.2 would really benefit from detailed explanations. 

- Does you method scale to ImageNet?
- Did you compare the three different initialization approaches? Random initialization, zero initialization and your in Proposition 3.2 proposed initialization?  
- Which hardware did you use to run your experiments?

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent
