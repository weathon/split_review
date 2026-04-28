# Robust Feature Learning for Multi-Index Models in High Dimensions

- Decision: Accept
- Avg Score: 6.86
- Scores: 6, 6, 8, 6, 6, 8, 8

## Abstract
Recently, there have been numerous studies on feature learning with neural networks, specifically on learning single- and multi-index models where the target is a function of a low-dimensional projection of the input.
    Prior works have shown that in high dimensions, the majority of the compute and data resources are spent on recovering the low-dimensional projection; once this subspace is recovered, the remainder of the target can be learned independently of the ambient dimension. However, implications of feature learning in adversarial settings remain unexplored.
    In this work, we take the first steps towards understanding adversarially robust feature learning with neural networks. Specifically, we prove that the hidden directions of a multi-index model offer a Bayes optimal low-dimensional projection for robustness against $\ell_2$-bounded adversarial perturbations under the squared loss, assuming that the multi-index coordinates are statistically independent from the rest of the coordinates. 
    Therefore, robust learning can be achieved by first performing standard feature learning, then robustly tuning a linear readout layer on top of the standard representations. In particular, we show that adversarially robust learning is just as easy as standard learning, in the sense that the additional number of samples needed to robustly learn multi-index models when compared to standard learning, does not depend on dimensionality.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper analyzses adversarially robust learning for two-layer neural networks trained on multi-index targets dependent on a low-dimensional subspace. The paper begins by proving that an optimal adversarially-robust predictor depends solely on the target subspace. Subsequently, the paper shows that existing guarantees for recovering the target subspace through SGD can be combined with covering number, rademacher complexity-based generalization and approximation arguments to obtain bounds on the adversarial risk. Crucially, the paper shows that the additional sample-complexity requirements for vanishing adversarial risk are independent of the ambient dimension.

### Strengths
- The problem of obtaining theoretical guarantees on adversarial risk and the dependence on the structure of the data is well-motivated of interest to the community.
- The direction of studying the interplay between feature learning and adversarial robustness appears to be novel.
- The paper is well written and describes the setup, literature well.
- The proofs are easy to follow.

### Weaknesses
My main criticism of the paper is that the extent of the theoretical novelty in the analysis and unexpectedness of the result is unclear in the paper's presentation. The paper would improve by emphasizing the central difficulties in combining the finite-dimensional guarantees with feature learning results. Specifically, it would be useful to know what parts of the analysis would change if one were directly studying the setup of random features on finite dimensions. It appears that the role of the low-dimensionality of the target subspace and feature learning is primarily in obtaining a second layer with dimension-independent norm ($r_a$ in Algorithm 1) that fits the target allowing for the Rademacher-complexity argument to go through. This aspect of the analysis is however, the same as generalization bounds in existing works on feature learning such as Damian et al. 2022.

My concern about the DFL definition remains. While the authors have clarified that the weights $w_i$ are assumed to be on the unit sphere, this constraint is not explicitly stated in the definition itself. The definition should be self-contained and not rely on implicit assumptions made elsewhere in the paper. This lack of clarity makes it difficult to assess the precise conditions under which the DFL property holds and how it relates to the subsequent theoretical results. Furthermore, the connection between the DFL assumption and the specific optimization algorithms used to train the first layer is not clearly explained, leaving a gap in understanding how this assumption is practically achieved.

### Questions
- What are the assumptions on the class $\mathcal{F}$ in Theorem 1?
- In the proof of Theorem 1, is $h(x)$ assumed to be in $\mathcal{F}$?
- Does definition 2 (DFL) implicitly assume constraints on the magnitudes of $w_i$? Otherwise, DFL is trivially satisfied by scaling up the weights. How is this scaling issue consistent with Theorem 4?

### Soundness
3

### Presentation
2

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
This paper addresses the challenge of learning adversarially robust models using 2-layer neural networks where the targets are a function of a latent low-dimensional projection of the inputs. Throughout the paper, they consider L2-constrained adversarial perturbations. They first prove that the optimal features in terms of adversarial robustness are in fact the true latent features of the data model. Then building off of prior work in 2-layer network feature learning, they assume access to a feature-learning oracle and analyze algorithms which query the oracle for the first-layer features and then adversarially train over the second layer’s parameters. For different function classes, they provide bounds for the number of required samples for adversarial training, neurons, and feature learning oracle error in order to achieve optimal robustness up to epsilon error with high probability. Through brief experiments, they validate their theoretical results and show that standard training followed by training just the last layer using the adversarial objective performs much better than full adversarial training.

### Strengths
The paper’s first contribution is that the ground truth latent features are in fact the optimal features in terms of adversarial robustness. This is not largely surprising, but it plays an important role in informing the kinds of algorithms one should use to achieve an adversarially robust model. They then show how to characterize the sample complexity and model complexity for just adversarially training the second layer for a broad class of target functions when given access to a feature learning oracle. Importantly, these bounds are independent of the ambient dimension as the hardness only depends on the effective dimension of the problem. These results are an interesting extension of previous works in feature learning for 2-layer neural networks which do not consider adversarial robustness.

### Weaknesses
The major weakness is the lack of extensive experiments. I think that the first row of figure one is not a fair comparison as the paper graphs a model trained completely using adversarial training techniques to just training the last layer using adversarial techniques while initializing the first layer to the ground truth representation. In the second row,  all models are forced to learn representations which is a more realistic scenario. However, based on the high-level result that adversarial training is no harder than standard training and that the optimal adversarially robust features are just the ground truth features, it would be interesting to see how different combinations of standard vs. adversarial training on different network layers for real-world data affects performance.  

Also, the statement of Theorem 1 is confusing. First of all it is not clear that the multi-index data model is still assumed. Also, the phrase “with equality when f^* in F” is confusing since f* in F doesn’t imply equality and that part is obvious, so stating it in this way is confusing for no reason. Also, the statement “Further, h is represented as E[]” is also confusing because it seems to mean that any h that satisfies the theorem must be represented in that way which is not true. The theorem should be restated as something like “Assume multi-index data model as explained above, Assumption 1, and (2.2) admits a min. Then there exists a function f* = h(Ux) where h = E[f] for some f in F where AR(f*) leq AR*.”

### Questions
Can you discuss how this result and analysis techniques connect to other recent results in how shallow networks learn representations, such as (Collins et. al., Provable Multi-task Representation Learning by 2-Layer ReLU Neural Networks, ICML 2024) and (Wang et al, Learning Hierarchical Polynomials with Three-Layer Neural Networks, ICLR 2024) ? 

Is the first inequality of the proof of Theorem 1 actually an equality?

In the experiment section, how did you select the “direction u”? Is this a vector in R^d? I do not see where u is defined.

Can you discuss what the actionable insights are in terms of training robust models? It would be interesting to see more practical experiments of how standard feature learning followed by running adversarial training on the last layers of a network can result in a full model which is adversarially robust.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper demonstrates that it is possible to robustly train a multi-index model without impacting the statistical performance of the algorithm compared to standard learning methods. Assuming a low-dimensional structure in the probability distribution of the observations, the authors propose a procedure for robust learning in two-layer neural networks. This approach involves a standard learning step for the input layer aiming at recovering the relevant low-dimensional subspace, followed by a robust learning phase for the output layer in lower dimension.

In Theorems 4, 5, 6, and 7, the authors provide rigorous asymptotic bounds on the sample complexity (in the second step), number of neurons, and achievable error for the feature learning algorithm, ensuring the algorithm attains a small adversarial generalization error. These bounds are shown to be independent of the ambient dimension. Finally, using recent results on the number of observations necessary to learn the relevant low-dimensional subspace, the authors establish a scaling for the sample complexity for both single and multi-index models in Corollaries 9 and 11.

### Strengths
-	Although I do not have any particular knowledge in robust training, I found the paper accessible and well explained. The stakes are clearly presented in the introduction. Additionally, the setup and the assumptions are generally well motivated. 
-	Despite not having read the proofs in detail, I appreciated that the proof techniques originate from diverse ideas and prior works including statistical learning, with generalization bounds provided in Appendix C1, geometrical analysis from the low-dimensional subspace assumption, approximation of functions using infinite-width neural networks, etc.
-	From the references provided in the introduction, it is clear that this paper offers new results and insights, distinguishing this work from previous research in the field.
-	The numerical experiment displayed in the main text gives a nice support to the theoretical claims of the paper.

### Weaknesses
-	Theorems 4, 5, 6 and 7 rely on specific activations (ReLU / polynomial). What is the technical challenge arising when considering more general activations? Specifically, the proofs seem to heavily rely on properties of these activations, such as homogeneity for ReLU and the algebraic structure of polynomials. It is unclear how these proofs would extend to other common activations like sigmoid or tanh, which lack these properties. This limitation restricts the practical applicability of the theoretical results.
-	Although it is interesting to include some proofs in the main text, the proof of Theorem 1 could be easily replaced with an outline of the proof ideas. The full proof, while technically sound, interrupts the flow of the paper and could be better placed in the appendix. This would improve readability and allow the reader to focus on the main results and their implications.
-	On the other side, it would be helpful for the reader to have a paragraph or two summarizing the main steps or ideas of the proofs of the main theorems. Currently, the reader is left to piece together the proof techniques from the appendix, which makes it difficult to grasp the core ideas behind the theoretical results. A high-level overview would greatly enhance the understanding of the paper.
-	One of the main claim of this work is that the bounds derived do not depend on the dimension. These bounds include the optimal adversarial risk (defined in equation 2.2), therefore, this quantity should not depend on the dimension. Whether this is a direct consequence of the definition or of Theorem 1, I don’t see it mentioned in the main text. It is crucial to explicitly state why the optimal adversarial risk is dimension-independent, as this is a key aspect of the paper's contribution.
-	Several concepts and notations are not clearly defined, and it sometimes affect the understanding of the results. My main concern is the lack of a definition for the Landau notations in the main results. As a consequence, it is not clear whether or not the obtained bounds are non-asymptotic or asymptotic and if they are, with respect to which variable. The use of Landau notation without a clear definition makes it difficult to assess the practical implications of the theoretical results. It is also unclear if the constants hidden by the notation depend on the dimension or other parameters.


### Questions
-	The proposed method only involves an adversarial training of the second layer. This has the benefit of achieving a robust training without requiring more samples or neurons than standard training. In addition, Figure 1 suggests that the convergence is faster compared to a full adversarial training. However, in the ReLu case (left panel), it seems that the robust test risk in the case of the full AD training is still decreasing. Given this observation and in the same setting as the paper, is there a possibility that robustly training both layers could achieve the same guarantees (sample complexity, number of neurons required) as standard training? 

-	In line 187, it is mentioned that the parameters $a, b$ are used to approximate $h$. This corresponds to roughly $N$ parameters to approximate the $k$-dimensional function $h$: can we think of the power $k$ in the bound for $N$ in Theorems 4 and 5 as a form of curse of dimensionality associated with this approximation task? If so, is there an intuitive reason why those exponents do not appear in Theorems 6 and 7 ? 

-	I am not sure about the assumptions of Proposition 8: In [Lee et. Al., 2024] Theorem 2 requires that the activation is also a polynomial with a higher degree than the link function. Is this additional assumption required for Proposition 8? Likewise, in Corollaries 9 and 11, the mention “as in Assumption 4” may be confusing: do you also make the assumptions regarding the activation? 

More precise questions and remarks:

-	In line 215, it is not clear why the expectation of the norm of $x$ is proportional to the square root of the dimension. 
-	Likewise, in line 218, the argument for choosing $\varepsilon$ of order 1 can be made clearer (is this because the scalar dot between $u$ and $x$ is also of order 1?).
-	In and before Definition 2, it is not mentioned that the columns of the weight matrix should be of unit norm. Without this detail, it seems that the definition of the DFL do not make much sense. 
-	In Definition 3, the last sentence is not very understandable and is not explained afterwards.
-	In Theorems 4 and 6, it would be nice for completeness to precise that the absolute constant c is positive. 
-	Since the results of section 4.2 do not cover the case of general activation, the discussion spanning from line 405 to 423 could be shortened. 


[Lee et. Al., 2024]: Jason D. Lee, Kazusato Oko, Taiji Suzuki, and Denny Wu. Neural network learns low-dimensional polynomials with sgd near the information-theoretic limit.

### Soundness
3

### Presentation
2

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
This work considers robust learning in the multi-index model for two-layer ReLU networks. In particular, authors study the setting of worst-case $\ell_2$-perturbation of the input and the problem of regression with squared loss. 

They propose the following two-stage method to find a set of parameters (weight of the first layer and readout vector):
First, algorithm finds a low-dimensional subspace, on which the target function depends. This is done using non-adversarial training, using prior feature learner methods. 
Using this subspace, adversarial training is done on the readout vector.

### Strengths
The question of robust learning in the multi-index model is well-motivated by the authors. Authors clearly state the assumptions and limitations of their results.

As the main result, authors prove that in the multi-index model, sample complexity of adversarial training is the same as in standard training. They combine prior work on feature learning with a second stage adversarial training which requires careful technical analysis. Authors also provide experiments to support their claim.

### Weaknesses
Authors highlight themselves that the result is limited to $\ell_2$ norm of perturbations. Some discussion on the extension to $\ell_\infty$ norm is lacking, i.e., why current proof techniques cannot tackle this setting. Specifically, the reliance on the spectral norm in the analysis, which is well-suited for $\ell_2$ perturbations, is not discussed in the context of its limitations for $\ell_\infty$ perturbations. The authors should elaborate on the challenges in adapting their proof techniques to handle the $\ell_\infty$ norm, which often requires different analytical tools and concentration inequalities.

Furthermore Theorem 1, which is central for the results of the paper, relies on the squared loss assumption. For classification tasks, which is a standard setting for adversarial robustness, logistic loss would be a more natural choice. The authors should acknowledge that the squared loss simplifies the analysis due to its convenient decomposition properties, which are not readily available for other loss functions like the logistic loss. The implications of this limitation on the applicability of the results to more practical scenarios should be discussed.

Organization of the main text is hard to follow, theorems for SFL and DFL are more or less copy each other, but stated in different places. Since only one proof (out of four Theorems 4-7) is given in the Appendix, possibly a cleaner way to present the results is to combine Theorems 4&5 together, and show Theorems 6&7 as a corollary under additional assumption (with a separate proof). This would improve the clarity and flow of the paper, making it easier for the reader to follow the logical progression of the results. The current structure makes it difficult to compare the results and understand their relationships.

Proof of Lemma 16 in the Appendix is hard to follow because of typos (line 894, should be $A_i (a_i - a'_i)$), and also $\tilde k_i$ is defined with $k_i$ and $k'_i$ in line 899, but both $k_i, k'_i$ are not defined at this point. I think what authors wanted to say is that $k_i, k'_i$ is defined with $\tilde k_i$, which is obtained through Mauery's lemma. It is confusing as it is written now. The lack of clear definitions and the presence of typos make it difficult to verify the correctness of the proof. The authors should carefully review the proof and provide all necessary definitions before they are used.

Numerical experiments can also be improved, see Questions.

### Questions
Second row of Figure 1: why having $W$ fixed at SD training plateaus, while continuing to train $W$ improves the performance? Doesn't it contradict the theoretical results, since according to Algorithm 1, one should not update $W$ after the first stage? 

Why for the numerical experiments Algorithms 2,3 are not used?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors study the problem of $\ell_2$-constrained adversarial regression under a multi-index model setting. Specifically, in this setting, the conditional form of $y\vert x = g(\{\langle u_i, x\rangle\}_{i \in [k]})$ holds, where $u_i$ are the weights (or features) to be learned, $g:\mathbb R^k \to \mathbb R$ is the link function and $x,y$ are the covariates and target, respectively. 

Their main result shows that under the assumption that the model relevant co ordinates $Ux$ (for $U \in \mathbb R^{k \times d}$) and model irrelevant co ordinates $\tilde Ux$ ( $\tilde U \in \mathbb R^{(k-d)\times d}$) are statistically independent, there is a learning method that attains a Bayes optimal adversarial risk. 

This is achieved through access of oracles which can be realized through gradient based methods, with additional assumptions on the data distribution and for a certain class of prediction functions, such as variants of Lipschitz and polynomials. 

Under the assumption that the predictor is a "pseudo"-Lipschitz, the sample complexity is not dependent on the data dimension, though it has an exponential dependence on $k$; for polynomial predictors, their sample complexity results do not depend on k. 


They do not analyze the computational complexity of this problem, and provide empirical evidence by comparing training approaches including initializations based on a known $u$ and fully adversarial training.

### Strengths
The contribution is good because it is a new theoretical study for adversarial feature learning for learning multi index models, which has been gaining traction recently. Their main results highlight that robust learning is achievable without a significant increase (at least for some functions) in sample complexity. Moreover, the oracles assumed for learning the target subspace can be realized by training the first layer in a 2 layered neural network. Overall, this is a well structured, theoretically sound work with a good upshot and I recommend an accept.

### Weaknesses
I would like to reiterate a few points they already raised. Firstly, for the case of pseudo-Lipschitz functions, while the sample complexity is independent of $d$, there is an exponential dependence on $k$, which seems quite high. 

I also think that many mathematical terms could benefit with more intuitions for the first time reader. For example, a minor point of clarification would be in Theorem 1, where it would be helpful to specify the random variables with respect to which the expectation is taken in the towering property, $\mathbb E_X[\cdot] = \mathbb E_Y[\mathbb E_X[\cdot \vert x,y]]$. 

It is also somewhat unclear to me what $\beta$ represents in the SFL oracle and also if a lower bound on $d\mu/d \tau_k$ connects to the Assumption 1. Moreover, I also think that Assumption 1 does not hold for natural scenarios where $x$ has a low rank structure where $\tilde Ux$ may not vary independently from $Ux$.

### Questions
Asked above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 6

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper explores the robust feature learning properties of two-layer neural networks for learning multi-index models in high-dimensional settings, under $\ell_2$-bounded perturbations. In particular, the authors show that Bayes-optimal adversarial risk can be achieved by neural networks once the input data are projected onto the low-dimensional manifold defined by the target multi-index model (first-layer feature learning) and the second layer is trained by minimizing the empirical adversarial risk. They demonstrate that the resulting sample complexity is independent of the ambient dimension. Leveraging prior results, the paper provides guarantees for robustly learning multi-index models with gradient-based algorithms and includes numerical simulations to support its findings.

### Strengths
This paper
* presents results with clarity and precision, offering complete proofs, insightful comments, and remarks that make the content accessible and well-structured
* leverages previous results and introduces interesting, non-trivial findings in a rigorous framework (e.g. the possibility of performing standard feature learning to obtain optimal adversarial risk)
* validates its theoretical results with numerical simulations
* acknowledges its limitations and open problems.

### Weaknesses
I did not find any major weaknesses in this work. A minor issue would be the reliance of the results on the assumption of independence between the coordinates $x_\parallel$ and $x_\perp$ (Assumption 1), see also my question 1.

### Questions
1. Can you provide insights or intuitions about the validity of your results beyond Assumption 1? Have you numerically tested your algorithmic framework in settings that do not satisfy this assumption?

2. In lines 384-388, you claim that your results in this section can be readily extended to the setting of anisotropic Gaussian $x$, which seems to contrast with Assumption 1. Is it still possible to leverage Theorems 4-7 in this case?


3. I believe there is a typo in equation (4.1), where $y$ should instead be $y^{(i)}$.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 7

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper studies the adversarial training of two-layer neural networks on learning multi-index target function (a function of a low-dimensional projection of the input) under squared loss. Under some assumptions, the authors first show that there exists an optimal low-dimensional projection (of inputs) for robustness against $l_2$ adversarial perturbations (Theorem 1). They then provide conditions for the first layer weights to satisfy such that the optimal low-dimensional projection matrix and the first layer matrix are partially aligned (Definition 2-3). Since there exist practical feature learning algorithms (examples given in Section 4.2) satisfying these conditions (definitions), they focus on the case where only the second layer is trained with adversarial loss while the first layer is pre-trained with a standard (not adversarial) feature learning algorithm. This simplification allows them to study the adversarial training of the second layer mainly. In this setting, the paper shows that adversarial training does not significantly affect the sample complexity of learning the target function. Specifically, the number of additional samples required for adversarial training (in comparison to standard training) is shown to be independent of the input dimension (Theorem 4-7). Thus, the authors conclude that adversarial learning in this setting is as easy as standard feature learning.

### Strengths
- **Interesting problem:** Understanding the effects of adversarial training of neural networks on the sample complexity may be significant for the deep learning literature. Furthermore, this paper combines two lines of work: 1) feature learning in two-layer neural networks and 2) adversarially robust learning in linear and random feature models.

- **Theoretical study under reasonable assumptions:** The authors study the problem under reasonable assumptions (in line with the prior work about such as Hassani & Javanmard, 2024).

- **Provides a valuable insight into the problem:** The paper shows that the adversarial training does not significantly (in the order of dimensions) affect the sample complexity in comparison to standard training.

- **Good enough presentation:** The paper answers most of the questions a reader may have, which is the main criterion when assessing the quality of the presentation. However, I think it is not an easy-to-follow paper. Instead, some parts of the paper require back-and-forth reading, which may be acceptable for such a theoretical paper.

### Weaknesses
 - **No characterization of robust test risk:** Prior works such as (Hassani & Javanmard, 2024) provide an asymptotic characterization of robust test risk for random feature models, which allows them to show how factors such as dimensions or perturbation budget $\epsilon$ impact the robust test risk. However, this work just focuses on the sample complexities and ignores the characterization of robust test risk. 

- **Significant gap to practice:** Although the assumptions are reasonable from a theoretical perspective, they differ significantly from practical adversarially robust learning.
   + **Data assumption:** Input is assumed to be subGaussian with constant subGaussian norm in Assumption 2. Furthermore, Assumption 1 imposes an implicit assumption on inputs and labels (target function), which needs further discussion (please see Question 1 about this below).
   + **The first layer is also trained with adversarial loss in practice:** While it seems like the adversarial training of the first layer hurts the robust test risk in Figure 1, this requires explanation (mentioned as future work in the conclusion). Thus, adversarial training of the first layer  is missing in this work.
   + **Limitation of $l_2$ perturbations:** The paper only studies adversarial training with $l_2$-bounded perturbations. Although $l_2$ perturbations for the adversarial training may be a good starting point considering the prior work on the theory of robust learning (Hassani & Javanmard, 2024), $l_{\infty}$ is primarily used in empirical studies as mentioned by the authors.
   + **Assumption on perturbation budget $\epsilon$:** The paper assumes constant adversary budget $\epsilon = \mathcal{O}(1)$ and justifies it by saying even this much perturbation can significantly perturb the output of the prediction function. However, as the authors noted, $\mathbb{E}[||\mathbf{x}||] = \mathcal{O}(\sqrt{d})$ and thus perturbation budget of $\epsilon = \mathcal{O}(\sqrt{d})$ is used in practice, which causes another discrepancy between the assumptions and practice.
   +  **Only polynomial and ReLU activation functions are considered.**

- **Limited numerical results and limited discussion of those results:**  
   + Most of Section 5 (Numerical Experiments) describes the experimental setting, while only one or two sentences discuss the results. There should be a more insightful discussion of the numerical results and their relation to the theoretical results.
   + There are some missing details about Figure 1 (please see Question 2.a-b below).
   + Effects of some parameters of the setting should be illustrated numerically or at least discussed: 1) activation function (polynomial vs ReLU), 2) different values for adversary budget $\epsilon$, 3) dimensions and number of samples.



### Questions
1.  **The assumption on the data distribution:** 
     + a) The authors mention that inputs can be Gaussian vectors with isotropic covariance, but what are other examples satisfying this assumption? For example, can we have anisotropic covariance (e.g., spiked covariance)? What if the covariance matrix and the projection matrix $U$ are aligned?
     + b) The authors mention (in Line 388) that "Our results readily extend to these settings as well," referring to non-isotropic Gaussian inputs and non-Gaussian symmetric input distributions. How so?

2. **Numerical results:** 
    + a) What is the step size for the gradient descent step on the perturbed batch for Figure 1?
    + b) What do shaded error bands denote in Figure 1? If variance, how much variance is illustrated?
    + c) Why do we see oscillating robust test risk for the two cases other than the full adversarial (full AD) training, while the robust test risk for the full adversarial training seems to be smooth in Figure 1? Furhermore, the robust test risk for full AD seems to converge fast while those for the other two cases do not seem converge even at the end of the iterations. Why so? 
    + d) The authors provide theoretical results on polynomial predictors in Section 4.1. A natural question is, "How does polynomial activation compare to ReLU activation in numerical results?". 
    + e) Prior work (Hassani & Javanmard, 2024) showed that adversary budget $\epsilon$ can significantly impact the robust test risk in their setting. How does adversary budget $\epsilon$ affect the robust test risk here? Similarly, what is the impact of dimensions and the number of samples?

3. The authors mention $\zeta^{(k-1)/2}$ as "the normalizing factor" in Line 239. But, $\zeta$ on its own deserves an explanation since it appears in most of the theorems. What does $\zeta$ intuitively correspond to?

4. **Minor issues:**
    + Some non-standard notations are used without definition. For example, soft O notation $\tilde{\mathcal{O}}$ and its counterparts for $\Omega$ and $\Theta$ should be mentioned in the "Notation" paragraph starting in Line 122.
    + There seems like a notational abuse when using the aforementioned asymptotic notations. There is asymptotic notation inside another asymptotic notation (e.g., in Theorem 4): $N \geq \tilde{\Omega}(\cdot^{\mathcal{O}(k)})$. Indeed, the authors assume $k = \mathcal{O}(1)$ in Line 154, which means $k < C$ for some $C > 0$. So, these equations can be simplified, and the notational abuse can be fixed at the expense of introducing one additional constant. Furthermore, note that the asymptotic notations are conventionally used with equality sign $(=)$ instead of $\leq$ or $\geq$.
    + In Line 135, the authors define the family of prediction functions to be "non-parametric". However, they then use two-layer neural networks as a prediction function in Line 140 or d-variate polynomials as the family of prediction functions in Section 4.1, which are "parametric" families of functions. There seems to be a contradiction here. Or am I missing something?
    + Ranges of $\alpha$ and $\beta$ are missing from Definitions 2-3.
    + Complexity results provided in Theorem 4-7 reduce the readability of main text since they include many parameters related to the setting. I think that the author can provide more insightful presentation of these results showing the essence.

### Soundness
3

### Presentation
2

### Contribution
2
