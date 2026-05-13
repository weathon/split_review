# Symmetric Kernels with Non-Symmetric Data: A Data-Agnostic Learnability Bound

- Decision: Reject
- Scores: 5, 3, 6, 6

## Abstract
Kernel ridge regression (KRR) and Gaussian processes (GPs) are fundamental tools in statistics and machine learning with recent applications to highly over-parameterized deep neural networks. The ability of these tools to learn a target function is directly related to the eigenvalues of their kernel sampled on the input data. Targets having support on higher eigenvalues are more learnable. While kernels are often highly symmetric objects, the data is often not. 
Thus kernel symmetry seems to have little to no bearing on the above eigenvalues or learnability, making spectral analysis on real-world data challenging.
Here, we show that contrary to this common lure, one may use eigenvalues and eigenfunctions associated with highly idealized data-measures to bound learnability on realistic data. As a demonstration, we give a theoretical lower bound on the sample complexity of copying heads for kernels associated with generic transformers acting on natural language.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors study KRR via spectral analysis of their eigenvalues  on the input
data. 
They argue while kernels are more symmetric than data, one may still use eigenvalues and eigenfunctions associated
with idealized data to provide bounds on realistic data via distributional shifts. As an example, they give a theoretical lower bound on the sample complexity of
copying heads for kernels associated with generic transformers acting on natural language, along with supporting experiments.

### Strengths
- study of the role of symmetries in KRR
 - having examples

### Weaknesses
 - the contribution of the paper is not clear; I didn't understand it by reading the paper
 - the intro section does not provide anything about the paper because it is too general
 - the introduction section is not clear--there are a lot of generic arguments, including all those in the 'our contributions' part (e.g., 'We generalize ... is tested on another.'). One cannot understand what exactly the contribution of the paper is based on the introduction section. This, in my opinion, should be clarified and revised. 

- typo in equation 1: comma is missing in the summation

- Equation 2 is not clear--are \psi functions vector? Then what does $[\psi_i,\psi_j]$ mean? Is that $L^2$ inner product? The paper would benefit from a more clear notation. 

- In Equation 2, can you explain why the expectation is over the data set, not data distribution? 

- The setup considered in Section 2 (Equation 6) is called the study of distributional shift, and some recent works are missing in references such as [1]. Moreover, recent works are missing for learning kernels with symmetries [2,3]. These are just instances, and please find similar papers for reference.

 - Theorem 3.1 does not deal with symmetry, and the role of the proposed workflow is unclear to me.

### Questions
This is an interesting paper. I think this paper needs revision to make its contributions more clear, along with a comparison with previous works. Here are my comments and questions:

 - The introduction section is not clear--there are a lot of generic arguments, including all those in the 'our contributions' part (e.g., 'We generalize ... is tested on another.'). One cannot understand what exactly the contribution of the paper is based on the introduction section. This, in my opinion, should be clarified and revised. 

- typo in equation 1: comma is missing in the summation

- Equation 2 is not clear--are \psi functions vector? Then what does $[\psi_i,\psi_j]$ mean? Is that $L^2$ inner product? The paper would benefit from a more clear notation. 

- In Equation 2, can you explain why the expectation is over the data set, not data distribution? 

- The setup considered in Section 2 (Equation 6) is called the study of distributional shift, and some recent works are missing in references such as [1]. Moreover, recent works are missing for learning kernels with symmetries [2,3]. These are just instances, and please find similar papers for reference.

 - Theorem 3.1 does not deal with symmetry, and the role of the proposed workflow is unclear to me.

I'm open to changing my score depending on the authors' response. 




[1] Ma, Cong, Reese Pathak, and Martin J. Wainwright. "Optimally tackling covariate shift in RKHS-based nonparametric regression." The Annals of Statistics 51.2 (2023): 738-761.

[2] Bietti, Alberto, Luca Venturi, and Joan Bruna. "On the sample complexity of learning under geometric stability." Advances in neural information processing systems 34 (2021): 18673-18684.

[3] Tahmasebi, Behrooz, and Stefanie Jegelka. "The exact sample complexity gain from invariances for kernel regression." Advances in Neural Information Processing Systems 36 (2023).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper considers Kernel Ridge Regression in the setting where the set of input points in the training dataset is different and possibly unrelated to the empirical distribution used to construct the eigenfunctions of the model. It is argued that this setting allows to apply spectral results available in a symmetric setting to non-symmetric datasets. The paper first introduces a cross-dataset concept of learnability of an eigenfunction and establishes a lower bound on the sample size required to achieve this learnability. Then, this bound is applied in a series of different settings: a toy gaussian example, the parity function on a hypercube, and learning copying heads with transformer.

### Strengths
This is a theoretical paper that attempts to develop an original approach to the study of learnability based on considering it with respect to 
a symmetric distribution and kernel but when performed on non-symmetric data. The paper proposes an associated concept of cross-dataset learnability. The main theorem is a lower learnability bound (Theorem 3.1); its proof, provided in the appendix, is concise and correct. The paper discussses several possible applications of this bound to various learning scenarios across different types of targets (gaussian, parity function, copying map).

### Weaknesses
1. My main issue with the paper is that I don't see it resulting in clear and important new findings. To begin with, while the paper is theoretical, the only result stated as a theorem is Theorem 3.1, which is a fairly simple bound and seems to be of auxiliary nature. The rest of the paper looks like a mathematically not well organized collection of various calculations and observations.

2. There are some issues with the proposed definition (6) of cross-dataset learnability. The original learnability (4) is a value between 0 and 1 and is an increasing function of sample size $P$ that converges to 1 in the limit $P\to\infty$. In this case there is a clear connection between learnability and sample size, the target is always underlearned, and making learnability $\epsilon$-close to 1 amounts to making $P$ larger than a particular threshold.  
In contrast, the cross-dataset learnability $\mathcal L^{D,q}_t$ defined by Eq. (6) can easily be greater than 1. For example, if the target $y$ is an eigenfunction $\phi_s,$ then for $t\ne s$ we have $\langle \phi_t,y\rangle_q=0,$ but in general $\langle \phi_t, \hat f_D\rangle_q\ne 0$ (say if $D=\{x_1\}$, then Eq. (29) implies $\langle \phi_t, \hat f_D\rangle_q = \lambda_t (k(x_1,x_1)+\sigma^2)^{-1}\phi_t(x_1)\phi_s(x_1),$ which is nonzero in general). Moreover, there is no obvious connection between the learnability  $\mathcal L^{D,q}_t$ and the dataset size. The learnability can stay above and away from 1 even in the limit $P\to\infty$. Due to this possibility of overlearning and contrary to what is suggested in and around Theorem 3.1, the condition $\mathcal L^{D,q}_t>1-\epsilon$ does not imply that we accurately learn the respective eigencomponent. These issues are not discussed in the paper. Furthermore, the definition of cross-dataset learnability as an absolute value of a fraction allows for cases where the fraction is -1, leading to a learnability of 1, which is counterintuitive as it represents poor learning.

3. I cannot say that the paper convincingly demonstrates the importance and usefulness of the proposed approach to analysis of learning based on the cross-dataset learnability  $\mathcal L^{D,q}_t$ and Theorem 3.1. As seen e.g. in Figure 1, actual learnability can deviate significantly from the derived bound, and the paper provides no results on its tightness. The vignettes considered in Section 4 are not that convincing, either. The first, Gaussian vignette is a very toy example. In the second, an existing exponential complexity bound for learning the parity function is shown to hold for non-symmetric distributions, but it's not clear why we should be interested in non-symmetric distributions in this problem. In the third vignette on copying heads, I also don't understand the significance of the resulting bound (26); there is no discussion on that in the paper.    
While the presented research is described as motivated by the practical problem of assessing learnability on real-world data, I don't see any useful applications to such data presented in the paper. For example, Figure 1 shows some results related to CIFAR-10, but they  seem to be very far from answers to real practical questions such as "how big must be the data set to achieve accuracy x?"

4. The paper has a number of typos and confusing statements:

   * line 705: "*while the eigendecomposition of the operator $K$ ... depends on the measure $q(x)$, the Mercer decomposition of the kernel function $k(x, y)$ does not*" - that's not correct, Mercer's decomposition does depend on the measure (otherwise how would we define orthogonality?)

   * Line 174: "*The learnability computed empirically divided by our learnability bound*"- The bound established in Theorem 3.1 is for the number of samples, not the learnability.  Also, it is not clear to me what is $B$ in Eq. (10), and how this equation was derived.

   * $\phi_1$ should be $\phi_2$ in the left panel of Figure 1

   * The numerator in Eq. (7) seem to be missing the modulus

   * Line 712: the reference to Eq. (5) should probably refer to Eq. (1) 

   * Line 396: "Sterling’s formula" - Stirling’s formula

   * Line 451: "casual masking" - probably, causal 

In summation, I don't think that the paper is ready for publication in the present state.

### Questions
-

### Soundness
2

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
2

### Summary
Using the eigenpairs generated under an ideal probability measure, the authors provide a lower bound for the sample complexity for the learnability of the dataset generated from another probability distribution under the KRR and GP framework.

### Strengths
1. Clear experiments to explain the main result.
2. Provide applications/examples for the main result in Section 4.
3. The idea of using eigenpairs from an ideal measure and applying it to real data is rather new to me (although I'm not familiar with the literature in this area, and it may be a common technique).

### Weaknesses
In general, I’m not familiar with this topic as my area is more in classical kernel methods; therefore, please use my comments (not weaknesses) below sparsely.

1. I’m not familiar with the kernel associated with the neural network (or many of its variances with specified structures, like a transformer or CNN). However, I want to get a general understanding of the issue raised by the non-symmetric data is specific to this NN-related symmetric kernel. Since in classical kernel methods, there seems no need to consider data symmetric, but in the NN context, uniform distribution for covariate is common. Can authors explain more about the challenges (technically) and consequences presented by non-symmetric data?
2. Why is cross-data learnability considered to take the form of Eq. (6)?  How does it link to the original definition of Eq. (4)? I can't see a clear connection to the Eq. (4),  there should be a clearer explanation for this consideration.
3. It looks like the learnability for a feature defined in Eq. (4) takes Tikhonov regularization, which indeed belongs to a broader class called spectral algorithms or spectral regularized algorithms. I wonder if it is possible to extend the result to this class. If not, what is the main obstacle?

### Questions
1. Although it is a theoretical bound, I’m curious about its role in practice; how do you estimate the expectations in Eq. (7), especially for those expectations over $D_{P}$. If one uses the empirical counterparts, it is weird as the r.h.s. of Eq. (7) also concerns sample size.

2. Notations
    a. Isn’t the index for $y(x_{\rho})$ and $k(x,x_{\nu})$ should stay the same?
    b. What is the name of quantity in Eq. (6), cross-data learnability?

### Soundness
3

### Presentation
2

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
The paper presents novel techniques to analyse the learnability of kernel methods such as kernel ridge regression and Gaussian process regression, including on real-world datasets that exhibit non-symmetric distributions. Traditional definitions of learnability require diagonalising the kernel on the data measure, but this is computationally expensive and requires access to the underlying data measure. The authors propose to mitigate this by defining a new notion of cross-dataset learnability, where they learn on the empirical data measure $D_p$ and judge functional similarity (‘perform evaluation’) on an auxiliary measure $q(x)$. This auxiliary measure is chosen judiciously to have particular symmetry properties, which makes bounding its eigenvalues tractable: one decomposes the target function into irreducible representations of the symmetry group and uses their inverse dimension to bound the corresponding eigenvalue. Thm. 3.1 gives an upper bound for sample complexity for this new notion of cross-dataset learnability. The authors demonstrate on real world and synthetic data, and provide three ‘vignettes’ to demonstrate their workflow and the types of conclusions one can draw using their approach.

### Strengths
The manuscript makes strong technical contributions. I can see how introducing cross-dataset learnability opens up exploiting the symmetry properties of an idealised auxiliary measure using tools for representation theory, including in situations where this symmetry is not respected in the true real-world dataset. It provides a natural avenue to port over existing results for idealised, symmetric datasets (Yang and Salman (2021), Lavie et al. (2024), etc.). The authors work hard to provide intuition for the reader, and the ‘vignettes’ showcase a range of interesting applications. The experiments include results for synthetic and real-world data.

### Weaknesses
1. *Articulation of the relationship between conventional and cross-dataset learnability*. I understand that the ability to diagonalise a simplified, symmetric kernel rather than its more challenging counterpart on the empirical dataset measure or true underlying dataset measure brings strong computational benefits. But can the authors say anything more concrete about the relationship, mathematically or even heuristically, between these different notions of learnability? Clearly they agree when learning from $p(x)$ (rather than $D_p$) and when $q(x)=p(x)$ (line 147), but can anything be added about e.g. small departures from this regime? For instance, if $q(x)$ is a slight perturbation of $p(x)$, can we establish bounds on the difference between the learnability measures? ‘Comparison with other measures of learnability’ (line 421) discusses how the result in Sec. 4.2. can be interpreted as an ‘unlearnability bound’ which agrees heuristically with existing results in the literature. This type of observation helps convince the reader that cross-dataset learnabilty is practically useful; I think the manuscript would benefit from further similar discussion. Supplementing Sec. 2 to more carefully relate Eq. 4 and Eq. 6 could also help by explicitly stating the assumptions under which these equations are expected to yield similar results and when they might diverge.
2. *Utility on real-world data and Figures 1 and 2*. In line 244, the authors note that their result ‘misses the saturation of learnability at later stages of learning’. I think this refers to how learnability drops as the trainset size grows. Presumably this is because the measures on which we learn and judge functional similarity now differ; we measure overlap of the predictor with eigenfunctions $\phi_t$ of the kernel wrt $q(x)$, but are training using $D_p$. If I understand this correctly, it seems that cross-dataset learnability decreases monotonically for trainset size for CIFAR-10, MNIST and Fasion-MNIST. Of course, there is a tradeoff in choosing an auxiliary measure $q(x)$ that is easier to diagonalise (to derive the bound) but also reflects the true data distribution less well, but isn’t it a problem that this formulation doesn’t appear to capture conventional notions of learnability at all for all three real world datasets? Furthermore, the observation that learnability saturates at later stages suggests a potential limitation of the proposed method in capturing the true learning dynamics. I’m also a bit worried about the comment that ‘the input dimension is reduced by PCA to $d=10$ as a balance between the dimension and the number of samples that was empirically found to allow learning of quadratic features’ (line 250): how robust are these experimental results? A more systematic investigation into the effect of dimensionality reduction on the learnability measure would be beneficial. As a more stylistic comment, I can’t see any reference to the inset panes of Figs 1 and 2; it would be great to add discussion of what these mean.      
3. *Choosing $q(x)$*. To add to the above: the authors note that one is free to choose the most favourable $q(x)$ in the class satisfying Eq. 8. I wonder if they can expand on this important point, discussing the tension between the presence of simplifying symmetries and how meaningful cross–dataset learnability is in practice. Can they provide any heuristic guidance for practitioners? For example, are there specific classes of functions or datasets where certain choices of $q(x)$ are known to be more effective? More stylistically, I think it would be really helpful to see a table or schematic listing existing results for symmetry groups, their corresponding architectures, eigenvalue bounds and references.
4. *Transformer results*. As early as line 21 of the abstract the authors highlight their results for sample complexity of copying heads for kernels associated with transformers. But in the main text and appendix these sections are terse. How is one to interpret the sample complexity bound in Eq. 26? I’d suggest either adding extra discussion here, or shifting focus in the abstract to highlight your very nice broader experimental contributions. Specifically, how does the bound depend on the vocabulary size $V$ and context length $L$? Is there an intuitive explanation for this dependence?   
5. *Presentation and minor comments*.
- I found the paragraph beginning ‘taking a Bayesian viewpoint’ (line 63) difficult to parse and somewhat disconnected from the rest of the introduction. I think the authors want to argue that expecting exact symmetry in the true data distribution is unrealistic and motivate instead using auxiliary $q(x)$ through a Bayesian lens, but I wonder if this could be rephrased a little more clearly.
- As minor typographical points, line 89 is missing a closing parenthesis and line 413 references an equation in the Appendix (presumably because of degenerate labelling). I would also consider splitting Eq. 25 onto multiple lines for better readability.

### Questions
1. Can the authors comment more on the relationship between conventional measures of learnability and their new scheme?
2. Can the authors provide interpretation of the sample complexity bound in Eq. 26, especially the dependence on $V$ and $L$?
3. Can the authors clarify the discussion about the rotational symmetry of the FCN on line 54? The references aren’t totally clear to me. Perhaps they refer to Thm 3.1 of Basri (2019), but I think this would benefit from further details and a more careful discussion of the necessary assumptions. 

I thank the authors for their efforts and nice submission. If they can explain the relationship to conventional learnability and the practical implications of their scheme (or convince me why these things shouldn’t matter), I will be happy to raise my score.

### Soundness
3

### Presentation
2

### Contribution
2
