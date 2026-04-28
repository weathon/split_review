# Semialgebraic Neural Networks: From roots to representations

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 5, 8, 5

## Abstract
Many numerical algorithms in scientific computing—particularly in areas like numerical linear algebra, PDE simulation, and inverse problems—produce outputs that can be represented by semialgebraic functions; that is, the graph of the computed function can be described by finitely many polynomial equalities and inequalities. In this work, we introduce Semialgebraic Neural Networks (SANNs), a neural network architecture capable of representing any bounded semialgebraic function, and computing such functions up to the accuracy of a numerical ODE solver chosen by the programmer. Conceptually, we encode the graph of the learned function as the kernel of a piecewise polynomial selected from a class of functions whose roots can be evaluated using a particular homotopy continuation method. We show by construction that the SANN architecture is able to execute this continuation method, thus evaluating the learned semialgebraic function. Furthermore, the architecture can exactly represent even discontinuous semialgebraic functions by executing a continuation method on each connected component of the target function. Lastly, we provide example applications of these networks and show they can be trained with traditional deep-learning techniques.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Authors proposed an architecture that is capable to approximate an arbitrary semialgebraic function. The main ingredients making the construction possible are two facts (i) it is possible to efficiently generate functions from ISD by neural networks with ReLU activations, (ii) any closed semialgebraic set (defining semialgebraic function) is a kernel of some ISD. Authors exploit these facts by combining a neural network with a homotopy method that deforms a simple semialgebraic set into a target semialgebraic set. The role of homotopy is to replace rootfinder that can be also used to find kernel of ISD. The resulting architecture resembles neural ODE, and requires adjoint for training. Authors demonstrated several theoretical results showing that with the proposed architecture it is possible to approximate continuous and discontinuous semialgebraic function.

### Strengths
The article introduces an interesting original idea that can be potentially used for many problems laying on the intersection of scientific computing and machine learning. Authors provide many details, examples and clarifications that help the reader with little background in semialgebraic approximation to better understand theory authors develop. Theoretical results seem to indicate that the proposed class of models represents a rather general set of functions. I also find particularly stimulating a discussion of relation between SANNs and deep equilibrium models solved with numerical continuation.

### Weaknesses
The article is theoretical, so the weak side is, naturally, a discussion of practical matters: computational complexity, how networks should be trained, how it compares with different related models, and questions alike. I put some of these questions in the section below, but overall I do not find this is a significant disadvantage, given that the goal of authors is to provide a certain "universal approximation" result for novel architecture they propose.

1. In the introduction authors made an analogy with deep equilibrium model and write (line 46) "Therefore, in principle, we can use a neural network combining polynomials and ReLU activations to learn G, then append a root-finding procedure such as Newton’s method to compute $F (x) = \text{root}(G(x, \cdot)) = y$ in a manner similar to Bai et al. (2019)." Given that it seems that deep equilibrium models are already capable of computing arbitrary bounded semialgebraic function, and the claim that authors present first such method (line 59, "To our knowledge, we present the first neural networks capable of computing arbitrary bounded semialgebraic functions on high-dimensional data") is misleading. Can the authors please clarify this?
2. In line 270 and equation (2), (3) that jointly define SANN there is an operation defined as $M^{-1}b$ if $M$ is invertible and $0$ otherwise. This operation is not convenient from the numerical perspective, since it requires the inversion of potentially large matrices, besides it is not cheap to test numerically that $M$ is invertible. Is it possible to generate $M^{-1}$ right away from $ISD_{\text{net}}$ in place of $M$? Is it important that $M$ can be not invertible? Can the authors please clarify this part?
3. In line 332 authors write "In our experiments, we found it insufficient to train using only the accuracy of the final output $\left\|y^{\star} − y(1)\right\|.$" No numerical experiments can be found in the article. Can the authors please describe numerical experiments they tried and show the results?
4. As I understand, training procedures include differentiation through the ODE solver. For that one needs to solve the adjoint ODE equation, and this is going to incur additional numerical costs. In a similar way, a deep equilibrium model defines an adjoint equation to obtain a derivative. Given that it is not clear what advantages the proposed method has over the deep equilibrium model (as discussed in the introduction) in terms of computations required. I kindly ask authors to discuss this issue.
5. In G2 authors provide interesting applications of SANNs. The idea, as I understand it, is to apply SANN to the space of equivalent feed-forward ReLU networks (which form a semialgebraic set). It is not entirely clear to me how this set can be constructed and manipulated with SANN. Can the authors provide more details, preferably, with some simple examples? It seems to me that this set is hard to work with, because practically indistinguishable networks can have weights arbitrarily distant in the $L_2$ norm https://arxiv.org/abs/1806.08459. It is also not clear to me how precisely SANNs can be used in the context of Lipschitz networks and for sparsifications.

### Questions
1. In the introduction authors made an analogy with deep equilibrium model and write (line 46) "Therefore, in principle, we can use a neural network combining polynomials and ReLU activations to learn G, then append a root-finding procedure such as Newton’s method to compute $F (x) = \text{root}(G(x, \cdot)) = y$ in a manner similar to Bai et al. (2019)." Given that it seems that deep equilibrium models are already capable of computing arbitrary bounded semialgebraic function, and the claim that authors present first such method (line 59, "To our knowledge, we present the first neural networks capable of computing arbitrary bounded semialgebraic functions on high-dimensional data") is misleading. Can the authors please clarify this?
2. In line 270 and equation (2), (3) that jointly define SANN there is an operation defined as $M^{-1}b$ if $M$ is invertible and $0$ otherwise. This operation is not convenient from the numerical perspective, since it requires the inversion of potentially large matrices, besides it is not cheap to test numerically that $M$ is invertible. Is it possible to generate $M^{-1}$ right away from $ISD_{\text{net}}$ in place of $M$? Is it important that $M$ can be not invertible? Can the authors please clarify this part?
3. In line 332 authors write "In our experiments, we found it insufficient to train using only the accuracy of the final output $\left\|y^{\star} − y(1)\right\|$." No numerical experiments can be found in the article. Can the authors please describe numerical experiments they tried and show the results?
4. As I understand, training procedures include differentiation through the ODE solver. For that one needs to solve the adjoint ODE equation, and this is going to incur additional numerical costs. In a similar way, a deep equilibrium model defines an adjoint equation to obtain a derivative. Given that it is not clear what advantages the proposed method has over the deep equilibrium model (as discussed in the introduction) in terms of computations required. I kindly ask authors to discuss this issue.
5. In G2 authors provide interesting applications of SANNs. The idea, as I understand it, is to apply SANN to the space of equivalent feed-forward ReLU networks (which form a semialgebraic set). It is not entirely clear to me how this set can be constructed and manipulated with SANN. Can the authors provide more details, preferably, with some simple examples? It seems to me that this set is hard to work with, because practically indistinguishable networks can have weights arbitrarily distant in the $L_2$ norm https://arxiv.org/abs/1806.08459. It is also not clear to me how precisely SANNs can be used in the context of Lipschitz networks and for sparsifications.

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
3

### Summary
This paper proposes the use of polynomial homotopy continuation methods to design a novel neural network achitecture. Homotopy continuation methods consider a function $H$ which continuously deforms a target function $G_0$ until it reaches a target function $G$. This method uses neural networks with RELU activations to compute the vector field of an ODE corresponding to this process of continuous deformation.

The authors show formally that this method can compute all bounded semialgebraic functions and that their method can be extended to discontinuous functions. 

Finally, a general class of optimization problems is specified, and the authors give example applications of their method.

### Strengths
1. The theoretical contributions of this paper seem strong. Capacity to compute all bounded semialgebraic functions (and extension to discontinuous functions) seem to be solid theoretical guarantees.
2. The proposed method seems, in principal, easy to implement and computationally efficient.
3. The method seems, in theory, to be applicable to a large range of optimization problems.

### Weaknesses
1. The subject matter presented in this paper is quite difficult, and I believe most ML researchers are probably quite unfamiliar with these mathematics. That being said, I found the exposition to be quite hard to read. Here are some more precise points/considerations I believe would improve the readability
    * Given this paper is presented to a machine learning (ML) conference, there should be more emphasis on the underlying learning problem. It might be interesting to motivate your architecture through a regression framework, for instance.
    *  You include many proofs in the main text and do not give much intuition on your mathematical results. I believe it would improve readability to put proofs in the appendix and spend more time developing intuition in the main text. You could for instance add more examples throughout the text such as the one presented in "Example 6".
    * I believe the algorithmic description of the architecture should be included in the main paper as it explains clearly the forward pass of your algorithm. It might be interesting to include 

2. The paper offers no experimental results on the proposed architecture. Given the main contribution of this paper is a novel architecture, empirical validation demonstrating the trainability of the model is crucial. I believe adding simple experiments with synthetic data would increase the value of the paper. You could, for instance, define a simple regression problem with synthetic data generated by a semialgebraic function, and show your model can exactly recover the correct mapping.

3. "We give a few remarks on training SANNs, and leave a more thorough investigation for future work." Although you do define a loss objective to train the model, you provide no empirical or theoretical justification that this loss objective works.  As with point 2, I believe it would strengthen the paper to give a thorough investigation (either theoretical or empirical) of the training procedure. For notes on doing this empirically see point 2. This could also be done theoretically by analyzing the training dynamics for example.

4. I find the structure of the paper to be confusing. I will list my comments about paper structure below:
    * There is no discussion or conclusion: it would be nice to add a conclusion section in which you discuss limitations and address future directions of research. 
    * The section which presents example applications does not contain any actual examples, only the general class of problems. It might help readability to use one of the example applications given in the appendix as a motivating example. 
    * Most of the paper seems to be an introduction to semialgebraic geometry and homotopy continuation methods (section 2 and first half of section 4). Maybe it would help readability to give a less detailed/rigorous introduction to the field and focus on explaining how the architecture works/why this method is useful.

### Questions
* "To our knowledge, we present the first neural networks capable of computing arbitrary bounded semialgebraic functions on high-dimensional data." What advantage does such an architecture have compared to SoTA neural networks which are already widely used and easy to train?
* "In our experiments..." what experiments are you referring to? Would it be possible to include the discussed experiments in the final manuscript? If not please remove any references to experimental results
* You provide theoretical guarantees (Theorems 14 to 16) that your model can represent any bounded semialgebraic function. Do you have any intuition on learnability? Could your model learn a function exactly given a finite amount of samples?
* Can you give examples of how representing discontinuous functions exactly might be useful in practice?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new class of neural network models, SANNs. The model is built on the basis of semialgebraic theory. The fead-forward network is defined using ODE and polynomial homotopy continuation method is used to ‘universality’ of the expressiveness of the neural networks. The paper focuses on theoretical aspects of the neural networks and contains abundant theoretical claims.

### Strengths
- Building a neural network based on semialgebraic geometry is very refreshing and definitely new class of ML models.  
- Using (the idea of neural)ODE as a computational graph of SANN also makes a quite sense assuming polynomial homology continuation method is used. 
- Visualization of the homotopy continuation method is really helpful to foster the readers’ understanding.
- Appendix covers exhuastive theoretical contents of the paper. Some applications are also discussed.

### Weaknesses
**Theoretical aspect:** In general, the paper assumes readers to be very familiar with semialgebraic geometry, which is (at least at this point in time) not a main stream of ML communities. I would presume the paper would be very hard to follow especially for those who are not familiar with this topic. I strongly encourage the authors to revise the paper so that the contents of the paper could be more accessible to even those unfamiliar with this topic. The followings are some concerns I found:
- The introduction of the paper is very hard to understand. Authors’ claims in the first paragraph of the introduction ‘’Semi algebraic functions include anything computable using …” and/or “Due to their ubiquity” would be unconvincing for those unfamiliar with this topic. It would be very helpful if the authors include references and/or brief explanation on the representative “classical numerical algorithms” that compute semialgebraic functions, such as linear system solvers, finite element methods, or eigenvalue computations.
- The definition of lattice should be mentioned before Definition 1 or referring to Appendix A -- I would say that at least in ML-community a lattice typically means $ \mathbb{Z}^{d}$. A clear definition distinguishing the usage in this paper from the common ML usage would be beneficial.
- ‘ker(f)’ in Proposition 7 should be also introduced. I would also say, the first sentence of the proof might be a bit rough -- It would be better to mention the continuity of $f$. Need to clarify the definition of $C^1$, since $\max ( 0, -q(x) )$ is generally not differentiable.
- The proof of Proposition 10 is hard to understand. Especially, ‘another ISD-function’ at line 311 is vague. Tarsi-Seidenberg theorem should be also stated somewhere in Appendix.
- What the authors mean by Training is somewhat unclear. When SANNs are trained, what parameters of SANNs are going to be trained? Does that mean the coefficients $a$ of $f_{k}(x)$ at line 154 are the trainable parameters? Clarifying which parameters are optimized during training would enhance the understanding of the proposed method.
- The claim in the lines 42-43 ‘neural networks capable of exactly computing any bounded semialgebraic function’ sounds vague since it is not clear what the authors mean by ‘exactly compute’. Does it mean, the proposed neural network can solve any root finding problems for semialgebraic functions? It would be helpful to clarify the precise meaning of 'exactly compute' in this context, distinguishing between theoretical representation and practical computation.

**Experimental aspect:**
- The application that benefits from the proposed network is not clear and it is hard to evaluate numerical advantages of the method. Key advantages of the networks in numerical experiments are stated as that the computational complexity is low and the evaluation time is fixed when using (non-adaptive) ODE solver, either of which are not evaluated in experiments or important classes of applications. While the paper rather has a technical sound and supports the theoretical validity of those two aspects, having numerical experiments that support authors’ claim would add stronger experimental support of the method's advantage. Specifically, demonstrating the computational efficiency and fixed evaluation time in a concrete application would be valuable.
- I managed to find in line 332 ‘In our experiments, we found it insufficient to train using only the accuracy…’, but I cannot find results of any experiments. Providing experimental results, even preliminary ones, would significantly strengthen the paper.
- The example applications in Appendix G should be discussed in the main text. Bringing these examples to the main text would help readers better understand the practical implications of SANNs.

**Minor:**
- ‘compute’ feels abused frequently. In some sentences, ‘represent’ instead of ‘compute’ sounds more convincing for me.
- L.20 or 21, “is able execute…”


**Overall comment (and meddling suggestion):**

The theoretical results of this paper are very intriguing and I believe this work would shed a light on the new usage of semialgebraic geometry in ML domain. On the other hand, I cannot overlook the major drawbacks that the paper lacks experiments which support theoretical finding and does not clarify numerical advantages against existing methods, as well as the lack of the readability of the paper. Therefore, I will give the paper the score ‘6’. However, I would be very comfortable to raise the score once those issues are addressed satisfactorily.

### Questions
- Why should semialgebraic function F not be simply modelled by ‘standard’ MLPs/NNs? In other words, why should F be encoded to the kernel of a piecewise polynomial? 
- Do the authors have a (rough) estimation and/or observation about the computational complexity of fead forward and training of SANNs?
- What would be a concrete example and task in PDE simulation to which SANNs are expected to perform better than existing methods? What would be the advantage of using SANNs in this case?

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
This paper introduces Semialgebraic Neural Networks (SANNs), a novel neural architecture designed to exactly compute bounded semialgebraic functions through homotopy continuation methods. The key idea is to encode the graph of a learned function as the kernel of a piecewise polynomial and then use numerical ODE solvers to evaluate it. The authors provide theoretical guarantees for the expressivity of SANNs, showing they can represent both continuous and discontinuous bounded semialgebraic functions. The work bridges classical numerical analysis techniques with modern neural network architectures.

### Strengths
Overall interesting application of homotopy methods to learn semi-algebraic functions. The work includes nice background on semi-algebraic geometry. Overall the high level idea is potentially interesting.

### Weaknesses
The biggest weakness of the paper (and major reason for the score) is the lack of clarity in the definition of SANN's and Section 4. I mention some suggestions in the questions below.
The introduction hints at a potential answer, but I don't understand why one would want to use this framework. Is this better than using the traditional learning framework (of learning F directly?)
Here is a list of other weaknesses:
There is no implementation or numerical work. (This isn't necessary, but I think the claim that you "demonstrate on applications" isn't accurate.)
It isn't clear which results are classical, or almost classical with a few notational differences. For example, is Proposition 7 a new result? What is new in Section 4.2?

### Questions
Questions:
The questions are in no particular order.
1. Fig 1 caption: Why does homotopy not give parts in kernel of G that are not part of F but somehow also correctly gives isolated point (0,0)? 
2. What does "defined in pieces" mean?
3. In corollary 8, "gr" is not defined.
4. Why not learn the kernel directly? (As in, learn the predictive model F(x)= y as is standard in ML) What is the benefit of learning G?
5. Why do we expect (7) to be small when s < 1? 
6. Above Thm 16 you say "exactly compute" but in remark earlier you mentioned that this will still have discretization error due to ODE solve. Should this be changed? 
7. Why does Theorem 14 only succeed with "probability 1"?

Suggestions:
1. Define acronym SANNS in main text.
2. Clarity of Definition 1 can be improved. Perhaps the free lattice should be defined? C^k(D, R^n) is not defined (I'm assuming this is just k times differentiable functions on R^n?) 
**3. I do not understand the definition of SANNs in equations 2-5. How does little n affect Z(N) and what is the product over? What is M and what does the the tuple equation (M, b) = N mean? (I'm guessing but can't be certain it's like the clamp-sol argument.) I suggest clarifying the notation here more carefully. 
4. The distinction between existing work and new contributions is not clear in 4.2. Can you write your results as a proposition?
5. Does Section 4.1 really belong in Section 2?
6. In your summary of Section 4, perhaps include the subsection numbers to help navigate the relationships between the proofs.

### Soundness
2

### Presentation
2

### Contribution
3
