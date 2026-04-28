# How DNNs break the Curse of Dimensionality: Compositionality and Symmetry Learning

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
We show that deep neural networks (DNNs) can efficiently learn any
composition of functions with bounded $F_{1}$-norm, which allows
DNNs to break the curse of dimensionality in ways that shallow networks
cannot. More specifically, we derive a generalization bound that combines
a covering number argument for compositionality, and the $F_{1}$-norm
(or the related Barron norm) for large width adaptivity. We show that
the global minimizer of the regularized loss of DNNs can fit for example
the composition of two functions $f^{*}=h\circ g$ from a small number
of observations, assuming $g$ is smooth/regular and reduces the dimensionality
(e.g. $g$ could be the modulo map of the symmetries of $f^{*}$),
so that $h$ can be learned in spite of its low regularity. The measures
of regularity we consider is the Sobolev norm with different levels
of differentiability, which is well adapted to the $F_{1}$ norm.
We compute scaling laws empirically and observe phase transitions
depending on whether $g$ or $h$ is harder to learn, as predicted
by our theory.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper explores how deep neural networks (DNNs) can overcome the curse of dimensionality through mechanisms of compositionality and symmetry learning. It introduces Accordion Networks (AccNets), which are structured as compositions of shallow subnetworks, and derives new generalization bounds based on the F1-norm and Lipschitz properties of these subnetworks. The authors prove that, under certain conditions, DNNs can efficiently learn complex functions, such as compositions of Sobolev functions, by leveraging these structural properties. Empirical experiments support the theoretical results, demonstrating phase transitions in learning behaviors and illustrating how compositionality helps avoid the exponential data requirements that typically plague high-dimensional learning tasks.

### Strengths
- The paper introduces an innovative framework to explain how DNNs overcome the curse of dimensionality through compositionality and symmetry learning. Using Accordion Networks (AccNets) to model compositions of functions and deriving generalization bounds based on F1-norms and Lipschitz constants is a novel and insightful contribution.
- The theoretical analysis is thorough, with detailed proofs and a solid foundation in functional analysis. The empirical results, though limited in scope, align well with the theory, demonstrating meaningful phase transitions and supporting the derived bounds.
- The paper is well-organized and logically presented, though the advanced mathematical concepts may still be challenging for non-expert readers. Key ideas are well-articulated, but additional intuition would improve accessibility.
- The paper has the potential to make a significant impact on our understanding of deep learning's success. By framing generalization in terms of compositionality and symmetry, the work could inspire new approaches to model design and optimization.

### Weaknesses
 - The experiments are limited to small-scale models, and the applicability of the results to large-scale, real-world networks remains unclear. More extensive testing on modern architectures would strengthen the findings.
- The reliance on smoothness and regularity assumptions (e.g., Sobolev norms) may limit the practical relevance of the results. The paper does not sufficiently address how deviations from these assumptions affect performance.
- The work lacks clear guidelines for implementing the theoretical insights in real-world scenarios. The two regularization methods proposed are difficult to optimize and may not be straightforward to apply.

### Questions
- How sensitive are the theoretical results to violations of the regularity assumptions?
- Can the authors provide clearer guidelines for when to use each regularization method?
- Are there alternative methods to control Lipschitz constants that could simplify optimization?

### Soundness
3

### Presentation
3

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
The paper investigates how deep neural networks (DNNs) can effectively tackle high-dimensional problems by leveraging compositionality and symmetry. Through a novel generalization bound, it demonstrates that DNNs with bounded F1 norms can avoid the curse of dimensionality—something shallow networks struggle with. Using a theoretical framework that combines the F1 norm (a complexity measure) and covering number arguments, the authors show how DNNs can learn compositions of functions by minimizing data requirements. This is particularly achievable when the network’s layers correspond to smooth functions that reduce dimensionality. Some empirical results illustrate phase transitions in learning based on the relative difficulty of learning different functions within the composition, validating the theory's scaling laws.

### Strengths
1. The paper seems to be well-thought and of a high-quality in terms of its writing and presentation. Even though the paper is technically involved, I believe that the story is coherent and the mathematical presentation is well-done. For example, the authors use Sec. 1.1 to explicitly explain the type of result they are achieving without too much technical detail, Sec. 2 to provide the necessary information to lay out the framework in which their contribution operates and Sec. 4.1.1 to explain what are the type of results we want to achieve in order to obtain a bound that deals with the curse of dimensionality.
2. As far as I understand the use of the F1-norm (Barron norm) and the per-layer Lipschitz norm to establish generalization bounds is a novel approach in analyzing the generalization capabilities of DNNs. While traditional generalization bounds rely on norms related to the weights, for a given network $f_w$ (without biases), the F1-norm captures the minimal norm of $f_v$ such that $f_v\equiv f_w$. This is a bit original compared to previous work.

### Weaknesses
1. Limited comparison and discussion of related bounds. The literature on generalization bounds for neural networks is extensive, with various techniques and approaches, each offering its own angle, contributions, and limitations. I believe the paper lacks sufficient comparisons, either through direct comparisons of the bounds or discussions of the advantages and limitations of other bounds in the literature. For instance, the result in Theorem 2 closely resembles the bounds of Bartlett et al. (2017) and Golowich et al. (2017). While the paper introduces a nice contribution by replacing the spectral norm with the Lipschitz norm in Bartlett 2017 and the Frobenius norm with the F1 norm, it's not clear to me when the new bound is better than the Bartlett bound. Is it possible to directly compare the current bound with those of Bartlett and Golowich? 
If so, what are the tradeoffs between these bounds? 

Additionally, other works have extended the bounds of Bartlett et al. (2017) and Golowich et al. (2017) to leverage network compositionality for improved guarantees (e.g., Ledent et al. 2019, Graf et al. 2022, Truong 2022, Galanti et al. 2023). How does your bound compare to these works? 

Other potentially relevant studies to discuss include those offering relatively tight generalization guarantees on common datasets (e.g., Dziugaite et al. 2017, Zhou et al. 2019, Lotfi et al. 2022).

2. The presentation of the experiments lacks clarity. Much of the experimental setup is confined to the appendix, with certain details—such as the meaning of dashed lines—insufficiently explained. For example, how is the generalization bound in Figure 1 calculated? Does it include constants? When calculating performance, do you take the square root of the loss as in the generalization bound, or not? What is the training loss? How is the $R(\theta)$ term computed? How is the F1-norm determined? The conclusions drawn from the experiments are also unclear. For instance, Figure 1 seems to show that the bound is quite loose and not strongly correlated with test performance.

3. The experiments are conducted in relatively simple settings where the model is a basic fully connected neural network (FCNN) trained on MNIST classification or WESAD. I would expect to see experiments comparable in sophistication to those in the existing literature, where some studies demonstrate that their bounds are relatively tight for MNIST or even more complex datasets, and where the models used are more sophisticated than a basic FCNN (see the references below).

4. While it is common in the literature for many bounds to lack tightness, it would be valuable to see how this bound compares with others in the field. This is particularly important since most bounds in the literature may not be directly comparable to the current bound, and each bound could be tighter in specific settings.

### Questions
1. Are there specific ways to directly compare the current bound with those from previous contributions? For example, how does this bound compare to those of Bartlett et al. (2017), Golowich et al. (2017), etc., for fully connected neural networks (FCNNs), and how does it compare with bounds for compositional architectures such as convolutional neural networks (CNNs)?

2. Would it be possible to evaluate the bound against other bounds in the literature within the authors' proposed learning setting? For instance, could the same models used by the authors be trained, and other bounds calculated for these models to enable comparison?

3. Could the bounds proposed by the authors be applied to more complex architectures, such as convolutional and residual convolutional networks? If so, how would the bounds scale as a function of the number of input/output channels and kernel sizes at each layer? How would this compare with existing studies on bounds for compositional neural networks (e.g., Ledent 2019, Graf et al. 2022)?

4. The authors mention that their bound offers advantages for compositional functions, listing several properties that might contribute to its strength. Is it possible to empirically demonstrate a clear trend where the bound improves as these properties become more pronounced?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper aims to proof non-vacuous generalization bounds for deep neural networks by focusing on learning functions that can be decomposed into smooth components (as quantified by Sobolev complexity bounds) that can each be learned by a shallow neural network, all of which are composed to form a deep "accordion" network. They build up to their main result in phases:
* In Theorem 1, they bound the generalization of shallow neural networks on functions with bounded $F_1$ norm and Lipschitz constant.
* They adapt these bounds to deeper networks and compositions of such smooth functions in Theorem 2.
* Proposition 3 replaces the Lipschitzness assumption of the target in Theorem 1 with an bounded-Sobolev norm assumption. They note that this introduces a curse of dimensionality in cases where the Sobolev order is small.
* Theorem 4 analogously extends Proposition 3 to deeper networks, noting that the curse of dimensionality depends on the highest-dimensional component. This implies that the curse of dimensionality can be avoided if the right hierarchy of symmetries exists in the target function such that each layer is low-dimensional.
* Theorem 5 shows that the final loss can be bounded for sufficiently large accordion networks regularized by layer-wise $F_1$ norms that are guaranteed to reach a global minima.

### Strengths
As far as I can tell, the mathematics of the paper are correct and this particular decomposition is novel.

I am not particularly concerned about the focus on generalization over optimization and the assumption that the trained neural network attains its global minimum. While this is a substantial assumption, this kind of optimization result would be prohibitively difficult for deep networks, and making this assumption makes it possible to prove interesting results about generalization and decomposition.

### Weaknesses
For the sake of clear presentation, I would recommend including examples of the functions that belong to different classes defined herein. For instance, which kinds of functions are Lipschitz but not Sobolev (and vice versa); and what are some examples of targets that can decomposed into a series of Sobolev targets? It would be helpful to have concrete examples to understand the scope and limitations of the theoretical results. The current presentation leaves the reader to imagine the types of functions that satisfy the assumptions, which makes it difficult to assess the practical relevance of the work.

I would add parantheses to the complexity measure on line 70 to make it clear that the product is just for the Lipschitz terms. This lack of clarity can lead to misinterpretations of the equations. In Theorem 4, it appears that $r^*$ and $r_{\max}$ are confused, which needs to be clarified. The distinction between these two variables is crucial for understanding the theorem's implications, and the current ambiguity detracts from the result's clarity.

It is also unclear how the assumption of global minima impacts the practical relevance of the results. While I acknowledge that optimization results are difficult to obtain for deep networks, the assumption that the trained neural network attains its global minimum is a strong one. The paper should discuss the implications of this assumption more thoroughly, particularly in the context of real-world training scenarios where local minima are common.

### Questions
Is there any particular evidence that can be included about the prevalence of target functions that can be decomposed into low-dimensional components in practical learning settings? It seems to be well-situated within the multi-index model framework for shallow networks, and it's unclear whether compositions of targets like that are thought to be practically relevant.

Is it clear that the $F_1$-norm-based regularization is reasonable for deeper models? If I recall correctly, part of the motivation for the $F_1$ norm in shallow models is that it corresponds with inductive biases for gradient descent, and therefore that bounded $F_1$-norm solutions are likely outcomes even if $F_1$ norm is not explicitly regularized. Are any results like this known for deeper models?

Do these bounds apply when the intermediate function compositions are high-dimensional, but with a low intrinsic dimensionality (e.g. single-index models)?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors derive generalization bounds for deep networks and functions that are compositions of simpler 
functions. The bounds primarily depend on the dimension and regularity of the intermediate layers and functions, which can 
potentially have much better properties than the original function. The proof is based on a covering number argument for 
a single layer/intermediate function and leverages the fact that covering number behaves well under composition.

### Strengths
* The paper is well-written. The presentation is clear and easy-to-follow.
* The covering number argument (proving a covering number result for shallow networks and chaining them) is interesting and 
  seems to be very suitable for analyzing deep networks/composition of function. It reduces the problem to a shallow 
  one and leads to clean proofs.
* The results are solid and improve on previous bounds when the functions are composition of simpler functions, which 
  I believe is a fairly reasonable assumption.

### Weaknesses
 * My main concern with this paper is about Theorem 4, and I would raise my score if the authors could clarify it. Theorem 4 seems strange to me as it depends only on the largest ratio
  $r_{\max}$ and is independent of the number of layers $L$. 
  Given a function $f$, there are multiple ways to decompose 
  it into a composition of functions, and it seems possible to reduce the ratio $r_{\max}$ by increasing $L$ and properly
  rescaling each component. Maybe I am missing something here (e.g., there is an $L$-independent lower bound for $r_{\max}$),
  but for now, I do not think the current statement of Theorem 4 is entirely correct. The proof of Theorem 5 (which I 
  assume corresponds to Theorem 12 in the appendix) does not resolve my confusion. Specifically, in line 1343, there is a 
  summation over $L$ terms that vanishes in the next line. 
* Figure 1 (the experiments related to Theorem 2) only shows the scaling laws w.r.t. the size $N$ of the training 
  set, while the theoretical results focus more about the dependence on the regularity of the intermediate layers vs 
  the global regularity. 

* Typos and minor issues: 
  * In the statements of most of the results, the failure probability is denoted by $\delta$, but in some bounds it 
    is denoted by $p$.
  * The empirical loss is referred to as $\tilde{L}_N$ in some places and by $\hat{L}_N$ in others. 
  * Lines 150, 151: the dimensions of $W$ and $V$
  * Line 196: "covering number number"

### Questions
* Could you clarify the dependence on $L$ of Theorem 4 (see the Weakness part of the review)? 
* I find the remark starting on line 256 unclear. What do you mean by the randomly initialized weights contributing a lot 
  to the parameter norm? In practice and most theoretical works, small initialization is used, and the parameter norm 
  should not decrease too much, if at all, during training when compared to its initial value.

### Soundness
3

### Presentation
4

### Contribution
3
