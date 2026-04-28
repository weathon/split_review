# Learning Polynomial Problems with $SL(2, \mathbb{R})$-Equivariance

- Decision: Accept
- Avg Score: 7.00
- Scores: 5, 8, 8

## Abstract
Optimizing and certifying the positivity of polynomials are fundamental primitives across mathematics and engineering applications, from dynamical systems to operations research. However, solving these problems in practice requires large semidefinite programs, with poor scaling in dimension and degree. In this work, we demonstrate for the first time that neural networks can effectively solve such problems in a data-driven fashion, achieving tenfold speedups while retaining high accuracy. Moreover, we observe that these polynomial learning problems are equivariant to the non-compact group $SL(2,\mathbb{R})$, which consists of area-preserving linear transformations. We therefore adapt our learning pipelines to accommodate this structure, including data augmentation, a new $SL(2,\mathbb{R})$-equivariant architecture, and an architecture equivariant with respect to its maximal compact subgroup, $SO(2, \mathbb{R})$. Surprisingly, the most successful approaches in practice do not enforce equivariance to the entire group, which we prove arises from an unusual lack of architecture universality for $SL(2,\mathbb{R})$ in particular. A consequence of this result, which is of independent interest, is that there exists an equivariant function for which there is no sequence of equivariant polynomials multiplied by arbitrary invariants that approximates the original function. This is a rare example of a symmetric problem where data augmentation outperforms a fully equivariant architecture, and provides interesting lessons in both theory and practice for other problems with non-compact symmetries.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper poses to solve certain polynomial optimization problems using architectures which respect the SL(2,R) symmetry. 

But most of the critical details are looking very opaque.

### Strengths
The paper has definitely identified a very novel use case for neural nets – like positivity certification for polynomials. 

The experimental data also seems reasonable.

### Weaknesses
What is this $\psi_n$ function in equation 2? This does not look like a Clebsch-Gordon coefficient. The authors should explicitly define this object and clarify its connection to the representation theory of $SL(2,\mathbb{R})$.

Section 4.2 is extremely vague. The pseudocode is almost unreadable because it is calling functions (in lines 8 and 10) which has never been defined. Also, the entire motivation of this Section seems unclear to me, even if I assume the correctness of Lemma 1. How is this related to the training problem that eventually seems to be the target? The description of the final layer is particularly opaque, and it's not clear how the output of the network is related to the desired positivity certificate.

The issues delineated in Section 4.3 do not seem relevant to the immediate question at hand which are all about certain polynomial optimizations. Or am I missing something? It would have been much better to use the space to explain what the experimental setup. Like it seems pretty critical to understand what is the author’s idea of a “natural” polynomial and these details are missing from the main paper! The loss functions used in this experiment also seem to be not clearly specified and that makes it further challenging to understand what is happening. The authors need to provide a precise definition of the loss function, including how it is computed and what it is optimizing.

### Questions
Q1. 

Why is SL(2,R) equivariance crucial to the usecases identified here? 

Its not possible to make the connection between this group and the problem as stated in equation 1.  

Q2. 

What is the training time for the nets involved in Table 2? I guess what is reported as “MLP times” are just the inference times, right? 

But the timings specified for the other methods are probably the “total” time they take to run and there are no other time costs there.  

Q3. 

What is the full and explicit specification of the loss function that is being optimized in the experiment in Section 5? 

And how does this respect SL(2,R)?

### Soundness
1 poor

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel approach to learning polynomial problems with -equivariance. The authors demonstrate the effectiveness of neural networks in solving polynomial problems in a data-driven fashion, achieving tenfold speedups while retaining high accuracy. They also adapt their learning pipelines to accommodate the structure of the non-compact group , including data augmentation and new -equivariant architectures. The paper presents a thorough analysis of the proposed approach, including theoretical proofs and experimental results.

### Strengths
+The paper presents a novel approach to solve polynomial problems with -equivariance, which is a significant contribution to the field.
+ The authors provide a detailed analysis of the mathematical properties of the proposed approach, including its equivariance and homogeneity properties. This analysis is essential for understanding the theoretical foundations of the approach.
+The authors provide a detailed comparison with existing methods, highlighting the advantages of their approach.

### Weaknesses
 - The paper could benefit from more detailed explanations of some of the technical concepts and methods used, particularly for readers who are not familiar with the field. For example, the paper could provide more details on the mathematical background of  and its relevance to the problem at hand. Specifically, a more thorough explanation of the Lie group and its representation theory would be beneficial, including how the irreducible representations are constructed and how they relate to the polynomial functions being learned. The paper assumes a level of familiarity that may not be universal among the target audience.

- The paper could provide more details on the implementation of the proposed approach, including the datasets used in the experiments, the choice of neural network architecture and optimization algorithm. For instance, the specific details of the data generation process for polynomial problems are not clearly stated. Furthermore, the choice of activation functions, the number of layers, and the width of the neural networks used in the experiments are not provided, making it difficult to reproduce the results. The optimization algorithm used, including the learning rate and batch size, should also be specified.

- The paper could benefit from a more detailed discussion of the limitations and potential future directions of the proposed approach. While the authors mention the lack of universality, they do not explore the specific types of polynomial functions or datasets where the proposed method might fail or underperform. A discussion of the computational cost of the proposed approach, especially for high-degree polynomials or large datasets, would also be valuable. Furthermore, the authors could discuss potential ways to extend their approach to handle more general equivariant functions beyond polynomials.

- While the proposed architecture is effective for learning equivariant polynomials, the LACK OF UNIVERSALITY mentioned could limit its applicability to more complex or diverse datasets. This could be a potential drawback when applying the proposed approach to real-world problems. It is unclear how the method would perform on data that does not perfectly conform to the assumed polynomial structure or if the data contains noise or outliers. A more detailed analysis of the robustness of the method is needed.

- While the experimental results are promising, the authors could provide more detailed analysis and discussion of the results to further support their claims. For example, the paper could provide more details on the sensitivity of the proposed approach to hyperparameters and the robustness of the approach to noisy data. The paper should include a more detailed analysis of the error distribution and convergence behavior of the method, and provide a comparison of the performance of the proposed method with other relevant baselines on a wider range of datasets.

### Questions
Please check the Weaknesses listed above.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper considers the problem of learning how to provide SDP positivity certificates for polynomials. This problem can be solved using convex solvers but this is typically rather time consuming. 

The paper observes that the mapping from positive polynomials to their `maximal entropy' SDP solution is SL(d) equivariant. Focusing on the d=2 case,the paper suggests an SL(2) equivariant architectures based on the Clebsch-Gordan methodology often used for SO(3) and other groups. In practice, this architecture does not perform as well as augmentation based on SO(2) equivariant baselines. The paper suggests an interesting theoretical find to (possibly) explain this: While the Clebch-Gordan architecture can construct all equivariant polynomials, the equivariant function considered in the paper cannot be approximated by equivariant polynomials.

### Strengths
1. I am not aware of previous work considering the problem the paper considered: learning SDP positivity certificates. Given the high time complexity of these solvers, their centrality in convex programming, and the fact that certificates are verifiable as explained in the paper, I believe this is a very interesting problem to consider and should be considered further. The paper does a good job, in my opinion, of setting up a first empirical and theoretical baseline to consider this problem. 

2. Writing is good, it is an interesting story to read.

3. Theorem 1 regarding non-universality seems an interesting result (despite possible error, and needing some tuning down or context as I discuss in the questions part)

### Weaknesses
1. I have some issues re the technical details of the main theorem and the premises of the method, see below. If these issues prove to be non-issues I will raise the score
2. The architecture that actually works is rather basic: MLPs with augmentations. On the other hand one could credit the paper in finding the equivariant structure and hence what the relevant augmentations are.
3. The argument that the SL_2(R) equivariant architecture doesn't work because of lack of universality is difficult to actually substantiate. There are many reasons why an architectures may not work well. Maybe a different SL_2 equivariant architecture will work better?

### Questions
The formulation of finding the positive-definite witness with maximal determinant assumes that there are many such witnesses. Are there many witnesses? e.g. when we discuss polynomials of degree 2 and the monomail vector is (x,y) I think that a symmetric matrix uniquely Q uniquely defines a quadratic polynomial (x,y)Q(x,y).
When we discuss polynomials of higher degree there are ambiguities that come from the fact that, say, (x^2)(y^2)=(xy)(xy). But this can be dealt with directly by adding more symmetry constraints into the matrix. In other words, the matrix should be a moment matrix as defined in [Lasserre 2001]. Once these constraints are added I believe that there will be no more ambiguities. Do you agree? If so wouldn't it make sense to incorporate the symmetries and forget about optimizing over logdet?

I have two issues with the non-universality proof. The first issue has to do with the correctness of the proof. In the proof of theorem 1 you display the matrix f(x^8+y^8) (let's call it M) which was computed numerically using Mosek. Is this matrix really a factorization of x^8+y^8? 
If I understood everything correctly, denoting v=[x^4, x^3y,...,y^4]^T we should have that for all x,y
x^8+y^8=v^TMv
is this correct? Trying this on numpy with the M you specified and x=1, y=1 I get 
v^TMv=1.76
while for x=1 y=1
x^8+y^8=2
Note also that the trivial factorization of x^8+y^8 would be M0=diag(1,0,0,0,1). which is not in the domain since det(M0)=0. Thus I would suspect that this polynomial is not in the domain of f. Is that true? Or is it possible for a polynomial to have different factorizations of different ranks? Authors please let me know if there is something I misunderstood of if there is some error. Due to this possible error I'm currently setting the rating at 5 and soundness at 2. I will be happy to raise the rating if there is in fact no error. 


A second issue is with the result concerning the non-universality of the SL(2) network is not correctness but just about the exposition. It is neat that you prove that the function f you're actually  interested in cannot be approximated by SL(2) equivariant polynomials. But I do think you should note that your function f is not defined on all of the vector space: namely f(p) is only defined if p is indeed positive, and moreover there exists a *strictly* positive definite matrix verifying this. So f is defined on some subset of your vector space. The universality results in [Bogatskiy] pertain to the complex SL_2, but also to functions continuous on the whole domain, and this may end up being the more substantial difference. Another example: in  [Villar et al.] all continuous functions invariant with respect to the non-compact Lorenz group action are shown to be approximated by polynomials. Here again the continuous functions are defined on all of the domain.

Another angle to think of these issues is: For non-compact groups often distinct orbits cannot be separated by continuous functions. For example: consider the action of SL_d on d by d matrices by multiplication from the right: you can see that a d by d matrix which does not have full rank, say A=diag(0,1,1,...,1), is not in the same orbit as the zero matrix, but its orbit contains all matrices of the form diag(0,epsilon,..,epsilon) and thus any SL_d *invariant* function F continuous on all of the domain will satisfy F(A)=F(0). For more on this see [Dym and Gortler] Section 2.5 and Section 1.4, especially the paragraph titled `algebraic separation vs. orbit separation'.  

So to be concrete about this: I think you should mention in the paper that the function f is not defined everywhere, and would suggest to change the paragraph `why is SL(2,R) different' and other places where this issue is discussed, to note that this also might be a reason for the difference between universality results elsewhere and your non-universality result here.

Other remarks, questions, suggestions, according to order in the paper and not importance:
Somewhere in the paper- explain why you decided to restrict yourselves to polynomials of two variables.

In your discussion of Schur's Lemma in page 6: the lemma applies to complex representations and not real. Do you address this (if not, maybe just add a disclaimer)?

Page 4: when you introduce the function f discuss its domain. Mention that in its domain the function is well defined since the opimization problem has a unique maximizer. 

Page 6: I didn't understand your explanation of the last layer.

Page 8 timing: The accuracy you achieve is not bad, but probably can be achieved by first order methods which can be much fast than Mosek. You should at least mention this, even if you do not compare against such a method in practice.

Page 9: you reference the wrong paper by Puny. You meant [Puny 2021] not [Puny 2023]


 


References mentioned above:
[Villar et al.]  Scalars are universal: Equivariant machine learning,
structured like classical physics
[Dym and Gortler] Low Dimensional Invariant Embeddings for Universal Geometric
Learning
[Puny 21]  Frame averaging for invariant and equivariant network design
[Lasserre 2001] Global Optimization with polynomials and the problem of moments.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
