# Spectral Truncation Kernels: Noncommutativity in $C^*$-algebraic Kernel Machines

- Decision: Reject
- Scores: 6, 3, 6, 6

## Abstract
$C^*$-algebra-valued kernels could pave the way for the next generation of kernel machines. To further our fundamental understanding of learning with $C^*$-algebraic kernels, we propose a new class of positive definite kernels based on the spectral truncation. We focus on kernels whose inputs and outputs are vectors or functions and generalize typical kernels by introducing the noncommutativity of the products appearing in the kernels. The noncommutativity induces interactions along the data function domain. We show that it is a governing factor leading to performance enhancement: we can balance the representation power and the model complexity. We also propose a deep learning perspective to increase the representation capacity of spectral truncation kernels. The flexibility of the proposed class of kernels allows us to go beyond previous commutative kernels, addressing two of the foremost issues regarding learning in vector-valued RKHSs, namely the choice of the kernel and the computational cost.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the recent subfield of positive definite kernels with values in a C*-algebra and RKHM (the correponding "RKHS" theory) . The whole work is motivated by going beyond the separable kernel widely used in vector-valued RKHS based on operator-valued kernels and benefit from with a better compute time when applying kernel “ridge” regression. The main interest of working with a C*-algebra is that it comes with a norm, a product and an involution, unifying operators and functions. In particular, the paper focuses on the C*-algebra of continuous functions and the case where inputs as well are elements of this C* algebra.  The paper is illustrated with the example of continuous functions on the 1D torus.  The authors propose a novel function-valued kernel, spectral truncation kernel, relying on the approximation of the multiplication operator with respect to x (defined in L2(T)) by leveraging a truncated spectral decomposition. The dimension of the truncated basis encodes a trade-off between the representation power and the model complexity. The resulting kernel also benefits from the noncommutativity of the approximated product and can be shown to converge. Applied on Kernel Ridge Regression in RKHM, this new kernel leads to a reduction of the complexity in time. It also comes with a generalization bound which is a direct instantiation of the result proven by Hashimoto et al. (2023). A deep architecture based on product (and not composition) of different kernel-based functions in RKHM is also presented. Experimental results study the behaviour of the approach with respect to the truncation parameter on  a toy dataset. An additional result on an inpainted image recovery problem built on MNIST data is also briefly presented.

### Strengths
This paper is following an original path in the kernel theory, exploring new schemes of kernels with values in a C* algebra. The work is certainly promising and of great interest for the kernel community. based on solid mathematical work, it opens a new way to tackle vector-valued or function-valued regression.
- Of special interest on the case of input and outputs that can be considered as functional (or vectors that can be seen as values of functions like images), the spectral truncation kernel allows for a drastically reduced computation cost in Kernel Ridge Regression while offering a great expressivity. 
- It can be declined with various choices of ground kernels and its positive definiteness is studied
- Products of (function-valued)-functions based on those kernels provide a deep architecture.

### Weaknesses
Even though very interesting the paper suffers from different flaws: some concern the presentation and can be considered as relatively minor, while the others are more fundamental.
Weaknesses in the content:
*The motivation of the paper remains unclear: if the authors wish to go beyond the separable kernel in the general case of vector-valued functions, they should briefly discuss the limitations (which indeed exist) of the different operator-valued kernels such as the transformable kernels, the separable kernels or combination of them.  If the motivation is to use RKHM theory in the case of function-valued functions then it is of paramount importance to highlight what cannot be done with operator-valued kernels devoted to functions with outputs in Hilbert spaces of functions. Specifically, the authors should elaborate on the computational bottlenecks and representational limitations of existing operator-valued kernels when dealing with function-valued outputs, and how the proposed approach addresses these issues. A more detailed discussion of the trade-offs between expressiveness and computational cost for different kernel choices is needed.
*Once a family of kernels is defined, in machine learning, we are interested on the ability of the machine learning algorithms to indeed take benefit from this kernel and provide a good solution to the ML task. So what is missing in this paper, is a discussion and an empirical study to determine when using those kernels are interesting compared to previous methods: does the complexity of the model make the algorithm more greedy in training data. I do not think that the actual generalization error bound really help to tell us that in precise terms. The paper needs a more thorough empirical evaluation, including comparisons with existing methods on benchmark datasets for function-valued regression. This should include an analysis of the performance of the proposed kernels with respect to the amount of training data, and a discussion of the conditions under which the proposed kernels outperform existing approaches. The generalization bound, while theoretically sound, does not provide practical guidance on the optimal choice of the truncation parameter or the amount of data needed for good performance.
My advice is thus to complete the paper with comparison with other (operator-valued) kernels and vv-RKHS. this has to be done  in the case of the current toy dataset but also in known functional regression data sets.
* Applicability and relevance of the methodology: a central question that is still not enough answered at the end of the paper is the following: on which family of problems, these spectral truncation kernels are relevant ? The authors should provide a more detailed discussion of the types of problems where the proposed kernels are expected to be most effective. This discussion should include specific examples and should clarify the advantages of the proposed approach over existing methods for these problems. For instance, in time series analysis, how does the spectral truncation kernel capture temporal dependencies compared to other time series kernels? In operator learning, what are the specific advantages of using this kernel over existing kernel methods or neural operators?
For instance,  the use of function-valued kernels for inputs and outputs which are vectors should be discussed. I think it is important here to clarify this: images are by definition a discretisation of continuous maps (intensity of pixel in finite resomution) and then they can be seen as a set of values of a function taken on different observation points. There is a great interest at considering the functions as continuous functions. I do not think it is always meaningful for a vector to be encoded as a function of its coordinate index: can you comment on that ?  The paper should clarify the limitations of representing vectors as functions, especially when the underlying structure of the data is not naturally functional. The authors should discuss the potential drawbacks and alternative approaches for handling vector-valued data.
* Finally I do think that the paper would have sufficient content if it was restricted to function-valued functions. However, if images are tken as examples, then more convincing and complete comparison on image completion should be givne with more involved problems than weakly inpainted images. For the results given, do not say vv-RKHS comparions in the table say clearly the name of the matrix-valued kernel you used and try other kernels including more general operator-valued kernels for function-valued functions. The image inpainting experiments need to be significantly strengthened with more complex scenarios and a more thorough comparison with state-of-the-art methods. The current experiments are not sufficient to demonstrate the practical utility of the proposed kernels for image processing tasks. The authors should also clearly specify the exact matrix-valued kernel used for comparison, and explore a wider range of operator-valued kernels for function-valued functions.

Weaknesses in the presentation of the paper.
The paper is in general not self content,  too much straightforward in its statements and very not enough precise in the presentation. It seems to me that an important work of re-writing is necessary, even though it is quite obvious that some efforst ahve been made here.
To give a few suggestions:
- rewrite the introduction with clear motivations and do not enter into partial details that cannot be understood at this stage (n < infty, n infty..)

- line 154 we jump into a comment about C(T) but previsously functions on the real torus were just an example. Now X = A ?
please say it !Moreover we cannot understand the sentence "however, by approximating ... by a Toeplitz matrix..;", we do not know yet that Toeplitz matrix will be involved here


- before line 174, say a word about the works of Van Suijlekom and explain the role of the Fejer function. The reader has to consult this apper to undertstand the construction. It is important in what follows when talking about convergence.

- in general, do not give proposition under the form of the sole formula but write a sentence introducing the property and a comment on what the proposition brings.
- generalization bound : clearly state as in the appendix that this result comes directly from previous literature (Maurer, 2016... Hasimoto et al. 2023)
-  It is crucial to introduce m when describing the observations at line 364.
- experiments : 
what do you want to bring in terms of emprirical evidence: please present the experiments as an answer to the questions/motivation of the beginning of the paper

* after rebuttal: the paper has gained significant improvements and I am  increasing my score consequently.

### Questions
Overall I would be happy to increase the score of the paper (around 4) if answers are brought during the rebuttal.

- Please clarify the motivation and express the pros and cons with previous competing methods
- Give at least one example to make the reader understand the issue with commutativity and the benefit of non commutativity
- Identify as much as possible the family of problems that could in principle be tackled by this method
- Complete the toy experiments with a comparison with other function-valued regression methods 
for the existing experiments, are the same curves observed when dealing with a very large data regime ?

Nearly all my questions have been answered in a satisfying way.

### Soundness
3

### Presentation
3

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
This paper proposes a new class of C*-algebra-valued positive definite kernels called spectral truncation kernels for vvRKHS. The noncommutativity, controlled by a truncation parameter n, allows for capturing interactions along the data function domain. The paper argues this enables a balance between representation power and model complexity, potentially leading to improved performance. A generalization bound is derived, highlighting the role of n in this tradeoff.

### Strengths
The paper introduces an approach to kernel design by leveraging the mathematical framework of C*-algebras and RKHM, offering a potentially powerful way to model complex data relationships. The theoretical analysis of generalization bounds provides valuable insights into the trade-off between representation power and model complexity, guided by the kernel's truncation parameter.

### Weaknesses
1. While the authors claim a computational advantage over vector-valued RKHSs (vvRKHSs) due to the linear dependency on output dimension m compared to cubic dependency in vvRKHSs, this advantage is not clearly demonstrated. The computational cost analysis lacks a direct comparison with vvRKHSs employing appropriate approximation techniques. For instance, the use of Nyström methods or random Fourier features could significantly reduce the computational burden of vvRKHSs, potentially negating the claimed advantage of spectral truncation kernels. Furthermore, the analysis does not consider the cost of evaluating the function-valued kernel itself, which could be substantial depending on the complexity of the C*-algebra and the chosen truncation parameter. A more detailed breakdown of the computational steps and their associated costs is needed to substantiate the claim of computational efficiency, especially when compared to optimized implementations of vvRKHS methods.

2. The deep model extension, while promising, lacks theoretical grounding. The analysis of representation power growth is based on a very specific construction and doesn't provide general insights into the behavior of deep networks with spectral truncation kernels. The presented analysis relies on a particular parameterization and does not address the potential for overfitting or the impact of different activation functions. A more rigorous analysis is needed to understand how the truncation parameter affects the learning dynamics and generalization capabilities of deep models using these kernels. The current theoretical analysis is too narrow to be broadly applicable.

3. The experimental results, while suggestive, are not compelling enough to validate the claimed advantages. The experiments are limited to synthetic data and a simplified MNIST task. More complex, real-world datasets with function-valued outputs are needed to assess the practical performance and demonstrate a clear advantage over existing methods. The current experiments do not adequately explore the sensitivity of the method to different choices of the truncation parameter or the impact of noise in the data. A more comprehensive experimental evaluation is necessary to demonstrate the practical utility of the proposed kernels.

### Questions
See weaknesses

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
This paper proposes a new class of positive definite kernels based on the spectral truncation. Detailed properties and examples have been discussed, and numerical results on both synthetic data and the MNIST dataset are presented.

### Strengths
The authors have introduced the basic properties of the proposed kernels and also investigated the generalization error. The presentation is clear.

### Weaknesses
Though the theoretical results are promising, two main questions remain unaddressed:
1. How can practical learning designs benefit from the new algebraic structures?
2. How can the development facilitate the kernel choices in practice? Section 6 seems to have some discussions on deep models, but a general development shall be data/task-dependent.

### Questions
See Weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
In this paper, authors propose a set of positive definite spectral truncation kernels, which is a class of the $C^*$-Algebra-valued kernel. The definitions of the proposed kernels involve several concepts, including $C^*$-Algebra, function-valued kernel, spectral truncation, and the torus. The authors provide a theoretical analysis of the convergence and generalization.  In addition, the authors introduce a noncommutativity and further illustrate its effectiveness with numerical results.

### Strengths
1. This paper is well written and organized.
2. Theoretical analysis is detailed, enabling the proposed method to have solid theoretical support.
3. The authors consider the deep spectral truncation kernel, sharing the advantage of both deep model and spectral truncation kernel, to improve the representation power.

### Weaknesses
1. In line 156, $z \in \mathbb{T}$ be the Fourier function. Why $z$ is a function? Based on the **Example 2.2**, $\mathbb{T}$ is a set, and the elements of $\mathbb{T}$ are real numbers. This puzzled me.
2. One of the main contributions of this paper is that the authors generalize typical kernels by introducing the noncommutativity of the products appearing in the kernels and showing their advantages. This is because $\mathcal{R}_n (x)$ and $\mathcal{R}_n (y)$, based on the spectral truncation, is noncommutative. However, the benefits of introducing noncommutativity in terms of convergence and generalization were not found. The effect of the noncommutativity is just illustrated in the experiment part. Or am I missing some details?
3. **Theory 3.4** gives the theoretical result of the convergence of proposed kernels. Does this mean that the proposed $k_n^{poly,q}(x, y)(z)$, $k_n^{prod,q}(x, y)(z)$, and $k_n^{seq,q}(x, y)(z)$  can approximate $k^{poly,q}(x, y)(z)$, $k^{prod,q}(x, y)(z)$, and $k^{seq,q}(x, y)(z)$, respectively? So is there any theoretical guidance for the selection of $n$, that is, how much $n$ can be well approximated?
4. From **Theory 4.1**, we can observe that the generalization bound is related to the trace of the kernel. How is this different from the previous theoretical results?
5. $n$ is the number of orthogonal bases. Therefore, the complexity of the model is larger if $n$ is larger, and the representation power of the model is better. This phenomenon also occurs in the general learning process or kernel function approach strategies. How is this different from them?
6. To obtain $c(z)$, computing $(G(z)+\lambda I)^{-1}y(z)$. Poor scalability.
7. Some definitions are in the complex number domain, while some are in the real number domain. It is confusing for me. When to do it in the complex number domain and when to do it in the real number domain. It can include a pseudo-code to show the details.

### Questions
1. In line 156, $z \in \mathbb{T}$ be the Fourier function. Why $z$ is a function? Based on the **Example 2.2**, $\mathbb{T}$ is a set, and the elements of $\mathbb{T}$ are real numbers. This puzzled me.
2. One of the main contributions of this paper is that the authors generalize typical kernels by introducing the noncommutativity of the products appearing in the kernels and showing their advantages. This is because $\mathcal{R}_n (x)$ and $\mathcal{R}_n (y)$, based on the spectral truncation, is noncommutative. However, the benefits of introducing noncommutativity in terms of convergence and generalization were not found. The effect of the noncommutativity is just illustrated in the experiment part. Or am I missing some details?
3. **Theory 3.4** gives the theoretical result of the convergence of proposed kernels. Does this mean that the proposed $k_n^{poly,q}(x, y)(z)$, $k_n^{prod,q}(x, y)(z)$, and $k_n^{seq,q}(x, y)(z)$  can approximate $k^{poly,q}(x, y)(z)$, $k^{prod,q}(x, y)(z)$, and $k^{seq,q}(x, y)(z)$, respectively? So is there any theoretical guidance for the selection of $n$, that is, how much $n$ can be well approximated?
4. From **Theory 4.1**, we can observe that the generalization bound is related to the trace of the kernel. How is this different from the previous theoretical results?
5. $n$ is the number of orthogonal bases. Therefore, the complexity of the model is larger if $n$ is larger, and the representation power of the model is better. This phenomenon also occurs in the general learning process or kernel function approach strategies. How is this different from them?
6. To obtain $c(z)$, computing $(G(z)+\lambda I)^{-1}y(z)$. Poor scalability.
7. Some definitions are in the complex number domain, while some are in the real number domain. It is confusing for me. When to do it in the complex number domain and when to do it in the real number domain. It can include a pseudo-code to show the details.

### Soundness
3

### Presentation
3

### Contribution
3
