# A Bregman Proximal Viewpoint on Neural Operators

- Decision: Reject
- Avg Score: 5.25
- Scores: 8, 5, 5, 3

## Abstract
We present several advances on neural operators by viewing the action of operator layers as the minimizers of Bregman regularized optimization problems over Banach function spaces. The proposed framework allows interpreting the activation operators as Bregman proximity operators from dual to primal space. This novel viewpoint is general enough to recover classical neural operators as well as a new variant, coined Bregman neural operators, which includes the inverse activatio and features the same expressivity of standard neural operators. Numerical experiments support the added benefits of the Bregman variant of Fourier neural operators for training deeper and more accurate models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This article constructs neural operators from the point 
of view of Bregman optimization problems. The proposed idea uses the dual space of Banach functional theory, 
and it allows to recover classical neural operators 
and define new ones. Numerical results 
on the newly constructed operators improve the accuracy of 
state-of-the-art results by using deeper networks.

### Strengths
Although technical, the article is well-written and easy to follow. 

The contribution raises an important question on the choice 
of a metric/divergence in the functional space of the solution u.

### Weaknesses
It seems that there is still a gap between the universal approximation result
and the numerical results in the article as
the theoretical assumption about the non-linearity sigma (sigmoid type)
does not hold in the numerical models (sigma=softplus is not sigmoid type).
Therefore it would be good to mention this gap in the conclusion.

There is some notation inconsistency in the definition of the kernel K_t^ac in eq. 3
and the K_t in Section 3.1. Are you talking about the same type of kernel in these 2 places?
Why do you use k^(t) as the kernel density, rather than the k_t as before (below eq .3)?

Section 3.1, it is unclear what the sigma_1 and sigma_2 after Remark 6 comes from,
do they depend on g_t?

Is bar{D} the closure of the set D in the definition of A in Section 4?
Why do you consider the space C with \bar{D} rather than with D?

some type in remark 9: no in?

### Questions
- There is some notation inconsistency in the definition of the kernel K_t^ac in eq. 3
and the K_t in Section 3.1. Are you talking about the same type of kernel in these 2 places? 
Why do you use k^(t) as the kernel density, rather than the k_t as before (below eq .3)? 

- Section 3.1, it is unclear what the sigma_1 and sigma_2 after Remark 6 comes from, 
do they depend on g_t?

- Is bar{D} the closure of the set D in the definition of A in Section 4? 
Why do you consider the space C with \bar{D} rather than with D?

- some type in remark 9: no in?

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
2

### Summary
This paper proposes a novel expressive framework called BFNO to improve FNO by understanding the action of operator layers via the minimization of Bregman regularized optimization problems.

### Strengths
The Bregman-based perspective on neural operators is intriguing, and the paper presents a variety of strong theoretical results.

### Weaknesses
1. The writing is poor, and I recommend that the authors carefully revise the paper from start to finish, especially regarding newly defined matrices or functions. For example, in Eq. 4, the definitions of $M_t$ and $K_t$ are not clearly stated when they first appear in the paper. Furthermore, the connection between the Bregman divergence and the specific neural operator architecture is not sufficiently motivated, making it difficult to understand the practical implications of the theoretical framework. The paper introduces a lot of notation without clear explanation of how each component contributes to the overall objective.
2. The experiments are too simplistic. The authors only compared BFNO with FNO. I suggest including other FNO improvements as baselines. The lack of comparison with other state-of-the-art neural operator architectures makes it hard to assess the true performance gain of the proposed method. The experimental setup lacks details, such as the specific hyperparameter choices, which are crucial for reproducibility. The datasets used are not sufficiently complex to demonstrate the full potential of the method.

### Questions
Q: Which $\psi$ in Table 1 do you use in the experiments? Do you compare the BFNOs obtained from different $\psi$?

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper studies neural operators from the perspective of Bregman proximal optimization. The nonlinear activation layers such as (sigmoid, tanh, SoftPlus) are interpreted as the Bregman proximity operators. Based on the above optimization viewpoint, a new neural operator named BFNO is proposed as an extension of FNO, where an additional term sigma^{-1}(.) introduced in the expression of FNO before the function sigma(). A few experiments show that BFNO performs better than FNO especially for a large number of neural layers.

### Strengths
(1) The main contribution of the paper is that the authors interpret the neural operators as Bregman proximal optimization. This opens up the possibility of bringing knowledge or theory of Bregman proximal optimization into the field of neural operators for many possible future work.  

(2) As I mentioned earlier,  BFNO is proposed as an extension of FNO by introducing an additional term sigma^{-1}(.) in the expression of FNO before the function sigma(), which I think has a similar effect as the skip connection in F-FNO or ResNet.

### Weaknesses
 (1) I think the authors should compare the performance of BFNO to that of F-FNO equipped with skip connection. This is because from a high level point of view, the introduction of an additional term sigma^{-1}(.) in the expression of FNO before the function sigma() is very similar to the skip connection in F-FNO. It is very interesting to find out which one performs better.  Personally I think F-FNO might perform better because the skip connection also has a strong motivation from the ODE point of view.  BatchNormalization can also be included in  F-FNO smoothly. If the authors are able to show that BFNO performs better instead with a good explanation, I would be happy to change my score of the paper.

(2) The paper conducted theoretical analysis but were not able to show in theory why BFNO performs better than FNO, which I think is very critical. Instead, they conduct experimental results to argue the superiority of BFNO. This is also partly the reason for me to suggest the comparison between the performance of BFNO and that of F-FNO.

(3) It is not clear to me if BatchNormalization or Layer normalization can also be covered by the framework of Bregman proximal optimization. The reason I have this concern is that the FNO paper used BatchNormalization in their experiment. I would think doing so improve the training stability. If BatchNormalization cannot be covered by  the framework of Bregman proximal optimization, it suggests the limitations of the framework.

(4) Another weakness is that the activation function needs to be monotonic for it to be invertible. This excludes a few functions such as ReLU and Swish.  I understand that SoftPlus is similar to ReLU but still it suggests the framework has some limitations.

### Questions
(1) I wonder if the authors use BatchNormalization when implementing FNO in their experiments because the original FNO paper used it.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This is a primarily theoretical paper which proposes to address a lack of formalism for characterizing architecture in previous methods.  The authors propose to replace the basic layer of a Fourier Neural Operator, equation (3), with a more general layer, equation first written down in equation (4).  This architecture was actually originally proposed in Frecon et al. (2022) "Bregman neural networks".  A large part of the papers introduces technical theory from convex analysis.  University approximation results are presented for the architecture.  Numerical experiments are presented comparing FNO with BFNO.  Seven equations are solved. It is demonstrated Fig 2a, that on the Burgers equation, the accuracy of FNO degrades as the number of layers are increased while BFNO is more accurate.

### Strengths
The authors bring the formalism of Bregman operators, which is normally used in convex analysis and optimization to bear on the analysis of neural network architectures.

### Weaknesses
The paper introduced a heavy mathematical formalism without justification.  The ideas of the paper are not clearly presented and the theoretical contribution is not substantial.

Overly technical:

- General conference audience will not understand the technical papers
- Neural operator specialists: will not understand the paper.
- Only experts in convex analysis will be able to follow much of the paper.
- Section 2 begins with a dense paragraph of convex analysis, unreadable to anyone who doesn't already know the area.  It's also unconnected to later sections, so not immediatly clear what is needed from this paragraph.
- Section 2.3 is an overview of bregman operators, bregman distance, textbook material, again not clear how much is needed.  "For additional details, the reader canrefer to Bauschke & Combettes (2017)"

The architecture is not clearly defined in the paper.
- The architecture was originally proposed in  Frecon et al. (2022) "Bregman neural networks" which was not an influential paper.  In that paper, it was made clear that the architecture involves bilevel optimization.  This is not explained or made clear in the current paper.
- In section 2.2. equation (4), which is a modification of (3), names the architecture, but it is not defined.
Later, it is defined as a special case of (6), which takes half a page to write down. "In (6), the proximity operator plays the role of an activation function operator, which in general will have the form of a nonlinear Nemytskii operator. ... Moreover, differently from usual architectures (Kovachki et al., 2021), ..."
- Nemytskii operator is never defined. However, "This relationship is crucial for further establishing connections with neural operator layers."

Experiments: 
The numerical experiments are quite limited and show minimal improvement, or improvement in very particular situations, compared to FNO.
"To this end, we conducted an experiment using the Burgers’ dataset with viscosity ν = 10−3, with results presented in Figure 2a. First, we observe that BFNO systematically yields lower prediction error, irrespectively of T. Second, the performanceof FNO degrades starting from T = 16, while BFNO demonstrates better performance as T increases until it reaches a plateau at T = 64. "

- Was this also the case for the other 6 equations solved, or just for this one?  Why did you just present the one equation

### Questions
Questions: 

1. Explain the architecture in more direct way.  Is there a bilevel optimization? This was much easier to understand in Frecon et al. (2022) "Bregman neural networks"
2. "Previous methods often lack of a general formalism for characterizing their architecture."  But there is a well known paper that does:  "Neural Operator: Learning Maps Between Function Spaces.  How does the contribution of this paper related to that one?
3. "In this work, we propose a novel expressive framework for neural operators by conceptualizing the action of operator layers as the minimizers of Bregman regularized optimization problems over Banach function spaces."  This sentence does not make sense, please clarify.

4. "We prove universal approximation results". This is true of almost any reasonable neural network, including MLP.  How does this argument show anything special about this particular architecture?

- "the proposed framework allows applying the extensive body of literature on proximal numerical optimization, of which Bregman proximity operators belong to, in order to study neural operators."
  - convince me why this is useful.  
- "This opens the way to extend the analysis done on neural networks to (Bregman) neural operators in the same spirit of Combettes & Pesquet (2020a;b)."
  - Explain what would be achieved by this. 
5. In Fig 2a, did the same results hold the other 6 equations solved, or just for this one?  Why did you just present the results for Burgers equation?

### Soundness
2

### Presentation
1

### Contribution
1
