# OPTIMAL TRANSPORT BARYCENTER VIA NONCONVEX CONCAVE MINIMAX OPTIMIZATION

- Decision: Reject
- Scores: 8, 6, 6, 6, 5

## Abstract
The optimal transport barycenter (a.k.a. Wasserstein barycenter) is a fundamental notion of averaging that extends from the Euclidean space to the Wasserstein space of probability distributions. Computation of the \emph{unregularized} barycenter for discretized probability distributions on point clouds is a challenging task when the domain dimension $d > 1$. Most practical algorithms for approximating the barycenter problem are based on entropic regularization. In this paper, we introduce a nearly linear time $O(m \log{m})$ and linear space complexity $O(m)$ primal-dual algorithm, the Wasserstein-Descent $\dot{\mathbb{H}}^1$-Ascent (WDHA) algorithm, for computing the exact barycenter when the input probability density functions are discretized on an $m$-point grid. The key success of the WDHA algorithm hinges on alternating between two different yet closely related Wasserstein and Sobolev optimization geometries for the primal barycenter and dual Kantorovich potential subproblems. Under reasonable assumptions, we establish the convergence rate and iteration complexity of WDHA to its stationary point when the step size is appropriately chosen. Superior computational efficacy, scalability, and accuracy over the existing Sinkhorn-type algorithms are demonstrated on high-resolution (e.g., $1024 \times 1024$ images) 2D synthetic and real data.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
In this paper, the authors present a new, computationally efficient approach for the Wasserstein barycenter problem. Without resorting to entropic-regularization, which degrades the quality of the result, they propose to formulate the problem as a nonconvex-concave minimax optimization problem, solved with a mixed gradient descent in the Wasserstein space and gradient ascent in Sobolev space. The algorithm is shown to converge to a fixed point with the classic rate for this class of problems. The final complexity is in $O(m \log m)$ if one projection step is approximated by a double conjugate (which violates the theory but performs well in practice), to be compared with $O(m^3)$ in most previous approaches. Experiments on synthetic data and handwritten digits are performed.

### Strengths
I liked this paper. The idea is natural but novel and efficient, and the presentation is clear and well-written despite the technicity of the work. Experiments are convincing. The authors are also honest in giving credit to inspirations from previous works (esp. Jacobs and Léger, and Lin et al.).

### Weaknesses
One point that would deserve more discussion is the property of the nonconvex-concave problem. Unless I am mistaken (I could very well miss something), by reformulating the problem as a nonconvex problem, one loses convergence to the true solution, but only towards a stationary point. This is a bit obfuscated in the current formulation, and would deserve a more honest discussion: efficient computation is obtained by "sacrificing" some theoretical guarantees, even with good practical performance. (If I missed something and convergence to the true barycenter is guaranteed, then it also deserved to be written!)

Minor typo: "dicuss", "Sythentic"

### Questions
See above.

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
This paper considers the problem of finding the unregularized barycenter between discrete probability measures. The authors reformulate this problem as a saddle-point optimization problem and propose a kind of gradient descent-ascent algorithm to solve it. The established algorithm is supported by theoretical investigation of its convergence rates. The approach is tested in two experimental setups where it is claimed to achieve better performance than two other baselines in terms of accuracy and time complexity.

### Strengths
The authors propose an interesting approach to solving the unregularized barycenter problem using the Wasserstein and $\dot{\mathbb{H}}^1$ gradients. The proposed approach outperforms the chosen competitors in time and space complexity.

### Weaknesses
My major concern is related to some discrepancy between the theoretical investigations of the proposed approach and its use in practical tasks. Namely, in Section 3.4, the authors prove several theoretical results regarding their method, including the important Theorem 1, which shows that the proposed algorithm allows finding stationary points of the objective functional. From the proofs in the Appendix, one can see that all theoretical results are logically connected, i.e. Lemma 2 uses the results of Lemma 1, Lemma 3 uses Lemma 2, and so on. Thus, the fulfillment of Theorem 1 also depends on the fulfillment of Lemma 1. At the same time, in Section 3.5 the authors propose to modify the algorithm for practical use in order to reduce the time complexity. This modification consists in replacing the projecting the potentials $\phi$ on $\mathbb{F}_{\alpha, \beta}$ with computing the second convex conjugate $(\phi)^{**}$. Such a replacement entails *non-fulfilment* of Lemma 1, as the authors themselves write in lines 422-423. Accordingly, Theorem 1 is also no longer true, i.e. the convergence of the algorithm's solutions to ground-truth solutions is no longer theoretically justified. I will appreciate if the authors could comment on the generalization of Theorem 1 to the case where Lemma 1 is not satisfied or conduct experiments with the original version of the algorithm.

The practical evaluation also lacks an experiment showing that the proposed algorithm (modified version) actually gives the **ground-truth solutions** for the considered barycenter problem. The authors only perform a comparison of some functional values ​​computed using a back-and-forth approach (Jacobs and Le ́geret, 2020) with the two baseline approaches $-$ WB (Solomon et al, 2015) and DSB (Janati et al., 2020). However, I have doubts regarding this metric for comparison, i.e., the computed functional values. It is not clear from the text how these values ​​are calculated - more details about the back-and-forth approach (Jacobs and Le ́geret, 2020) should be included. This is especially important since the approaches the authors compare with are entropy-regularized. Besides, I recommend the authors to conduct a comparison with ground truth solutions of the barycenter problem which can be constructed for the case of gaussian measures using, e.g., the iterative algorithm from (Álvarez-Esteban, Pedro C., et al., 2016), and perform the comparison with the baselines in this setup.

Moreover, I have some doubts regarding the significance of the developed algorithm since it borrows ideas which are already present in the field. $\dot{\mathbb{H}}^1$-gradient ascent algorithm for finding the maximizers of dual OT problem was proposed by (Jacobs & Le ́ger,2020), while the Wasserstein gradient for solving the barycenter problem was initially proposed in (Zemel & Panaretos, 2019; Chewi et al., 2020). The algorithm in the current work combines these two ideas. 

**In summary**, I think that the contribution of the paper is questionable since the algorithm combines the ideas which are already present in the field and, thus, to represent interest for the community it should have some theoretically and practically justified advantages over the previous approaches. However, in the current version of the paper, it is not clear whether the modified algorithm which was used in the experimental part actually learns the ground-truth barycenter after the considered number of epochs or not. The theoretical investigations (convergence analysis) are not valid for this modified algorithm, while the experimental section also lacks the setup with known ground-truth solutions which can be used to mitigate this concern.

Minor:
 - line 132: descent $\rightarrow$ ascent;
- mistake in line 269 - there should be $\max$ instead of $\min$ over potentials.

### Questions
- The idea in lines 290-291 is not clear: “the definitions in subsection 2.3 imply that the Wasserstein gradient of J is given by $\nabla J (\nu, \phi) = id −\nabla\phi$, where …”. Please explain how this Wasserstein gradient is derived?

- Why do you consider only two baseline models, i.e., CWB (Solomon et al, 2015) and DSB (Janati et al., 2020) approaches? These models use the entropy regularization which makes the comparison not entirely fair (yet, I agree that it can be done in the case of small regularization parameter $\varepsilon$). Meanwhile, you have mentioned many other approaches which compute the barycenter in an unregularized setting, e.g., (Zemel & Panaretos, 2019; Chewi et al., 2020). Why do you not compare with these algorithms? I will highly appreciate it if you perform the comparison with some of these approaches during the rebuttal phase.
- What do you mean by $\nabla_1$ in line 211?
- In lines 315-318 you write: “we can alternatively use the L2 -gradient to update $\nu . However, in simulations, the Wasserstein gradient update significantly outperforms the L2-gradient update.” Can you provide an experiment justifying this claim?

**References.** 

Álvarez-Esteban, P. C., Del Barrio, E., Cuesta-Albertos, J. A., & Matrán, C. (2016). A fixed-point approach to barycenters in Wasserstein space. Journal of Mathematical Analysis and Applications, 441(2), 744-762.

Matt Jacobs and Flavien Le ́ger. A fast approach to optimal transport: The back-and-forth method. Numerische Mathematik, 146(3):513–544, 2020.

Hicham Janati, Marco Cuturi, and Alexandre Gramfort. Debiased Sinkhorn barycenters. In Pro- ceedings of the 37th International Conference on Machine Learning, pp. 4692–4701, 2020.

Sinho Chewi, Tyler Maunu, Philippe Rigollet, and Austin J Stromme. Gradient descent algorithms for Bures-Wasserstein barycenters. In Conference on Learning Theory, pp. 1276–1304, 2020.

Yoav Zemel and Victor M. Panaretos. Fre ́chet means and Procrustes analysis in Wasserstein space. Bernoulli, 25(2):932 – 976, 2019.

Justin Solomon, Fernando de Goes, Gabriel Peyre ́, Marco Cuturi, Adrian Butscher, Andy Nguyen, Tao Du, and Leonidas Guibas. Convolutional Wasserstein distances: Efficient optimal transporta- tion on geometric domains. ACM Transactions on Graphs, 34(4), 2015.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this paper, the authors propose a novel method to compute the unregularized Wasserstein barycenter of probability distributions discretized on compact sets. This setting is typically encountered in image settings, where one image corresponds to a probability distribution over a grid of pixels. In essence, their method consists in reformulating the Wasserstein barycenter problem as a min-max optimization problem (by relying on the dual formulation of the Kantorovitch transport problem), where the 'max'-based problem is concave while the 'min'-based problem is not convex. Then, they propose to solve this new problem via gradient ascent-descent approach, an iterative algorithm which alternates between a gradient descent step operating on the measure space (with Wasserstein gradient) and gradient ascent steps operating on the space of Kantorovitch dual potentials. Under reasonable assumptions on the input distributions, the authors provide convergence rate to a stationary point and iteration complexity of their algorithm named WDHA. Then, they apply their method to image settings (synthetic data + binarized MNIST) and compare WDHA to previous methods, which rely on regularization.

### Strengths
- The paper is well written, the authors paying attention to define their mathematical notation and justifying carefully their computations (especially on gradients). A valuable effort is made on introducing elements in the introduction that will serve later for defining the theoretical framework of the method. In particular, the algorithm is clear to understand.
- The numerical experiments provide the intuition that the current method provide good quality of the barycenter.

### Weaknesses
 - The choice of numerical setting of the main hyperparameters (step-sizes for ascent and descent) is not discussed.
- The burden of dimension is not discussed: in the current paper, only 2-dimensional settings are considered while Ot problems are generally of interest in larger scale. It is hard to see if the current method is scalable. The authors should explicitly state the limitations of their method to 2D settings with compact support, as the computational cost of the convex conjugate and the inverse Laplacian may become prohibitive in higher dimensions. It is unclear how the computation of the convex conjugate is performed for dimensions greater than 2, and this should be addressed.
- The authors compare their methods to regularized approaches that enable to compute Wasserstein barycenters, but did not consider certain regularized methods that provide the exact same type of numerics (barycenter over images), see [1,2], without proper justification. In particular, the method in [1] should be included in the discussion as it also addresses the issue of scalability with input convex neural networks. 
- Numerical results do not include uncertainty quantifications, which hurts the statistical significance of the results. The standard deviations of the metrics should be included to properly assess the variability of the results. For example, the value functions in the first experiment appear very close, and it is unclear if the differences are statistically significant.
- The current paper lacks experiments where the actual barycenter is known (for example Gaussian experiment), which would enable to have a clear comparison with ground truth samples. The authors should consider a Gaussian setting with different covariances for each input measure to demonstrate the robustness of their method, as this is a common benchmark in the field.

### Questions
- How much critical is the compactness assumption on the input probability distributions for your method ?
- Assumptions in Theorem 1 suggest that the input distributions should have the same support (although it is not verified in the very first experiment). Could you improve this assumption to consider a case of distinct supports ?
- Could you explain what prevents the term $\mathcal{F}_{\alpha, \beta}(\nu^{T+1})$ to be arbitrarily large in the upper bound of Theorem 1, Which may hurt the convergence rate ?
- Could you detail how you efficiently implement the computation of the convex conjugate and the negative inverse Laplacian in the case of probability density functions discretized over a grid ?
- How do your method compare with methods mentioned in the section 'Weaknesses' ?
- What motivated to set the hyperparameters of your algorithm (in particular $\tau$) as you did ? Do you have guidelines for general use ?
- How do you compute the value function $\mathcal{F}(\nu^{est})$ for competing methods ? 

**Suggestions**
- The authors should mention in the introduction/related work the other common setting for Wasserstein barycenters related to generative modeling and deep learning, where the input probability distributions are not tractable and are represented by subset of samples. In the image setting, this would correspond to take one image as a sample from a high-dimensional distribution (not a distribution itself). A lot of recent work has been done in this direction recently.
- I think there is a typo at the end of page 5: it should be a max not a min.

### Soundness
3

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
3

### Summary
This paper introduces a new algorithm called the "Wasserstein-Descent H-Ascent (WDHA) algorithm" for computing the optimal transport barycenter.
Considering the dual form of the original problem, this paper transforms the barycenter problem as   a nonconvex-concave minimax optimization problem, and then propose a gradient algorithm for optimization.
One advantage of the proposed WDHA algorithm is its runtime complexity, which grows linearly with the grid size $m$, while the naive method computing the optimal transport map requires time complexity of $O(m^3)$.
Moreover, the under certain assumptions, the paper also shows the convergence rate $O(1/T)$ of the algorithm to  its stationary point.
Finally, numerical studies are provided to demonstrate the effectiveness of the method.

### Strengths
- Algorithm: The paper introduces the WDHA algorithm by considering the dual form of the problem of the optimal transport barycenter and using a  nonconvex-concave minimax optimization procedure, which is novel and interesting.
Moreover, The proposed WDHA algorithm achieves nearly linear runtime complexity, improving the $O(m^3)$ complexity of the naive approach.

- Theory: Under certain assumptions, the authors provide a convergence rate of  for the WDHA algorithm, which matches the convergence rate as in the Euclidean nonconvex-concave optimization problems.

- Numerical study: The paper includes numerical studies that demonstrate the effectiveness of the WDHA algorithm over existing methods, showing that the proposed algorithm runs faster than the existing methods.

### Weaknesses
 - Theory: One weakness is that the theoretical analysis is performed for Algorithm 3, while the practical implementation uses Algorithm 4. 
Also, the theorem assumes lower bounded densities of the distributions, which may not be true in practice (for example, in the case of Figure 1). Even in this ideal setting, there is also an extra assumption on the uniform boundedness of $\nu^t$. Therefore, the convergence guarantee of the algorithm in practice remains unclear.

- Numerical Studies: While the numerical studies show faster computation times for the proposed method, I think the current results are not sufficiently convincing to demonstrate its superiority. For example, the "barycenter functional values" reported in line 515 differ very slightly across differet methods, and it seems to me that in the figures the DSB method performs generally well. More quantitative and comprehensive experiments should be conducted to validate the claims.

  Moreover, I would like to ask the authors to provide the codes for reproducibility.

- Comparison with Literature: A detailed discussion and comparison regarding the settings, runtime complexity, and theoretical guarantees with existing methods for optimal transport barycenter computation should be included for better demonstration.

### Questions
1. Can you provide theoretical/empirical insights for the statement in Line 317 "By embedding all densities functions into L2(Ω), we can alternatively use the L2-gradient to update ν. However, in simulations, the Wasserstein gradient update significantly outperforms the L2-gradient update."

2. Can you discuss the impact of the additional regularity by considering $\mathbb{F}_{\alpha,\beta}$ on the resulting barycenter accuracy, the convergence rate and computational cost?
How these quantities are chosen in practice?

3. I would like the authors to discuss more on the effect of tuning the parameters in the numerical studies.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper uses a primal-dual formulation for the Wasserstein barycenter problem without any regularization. The method is performed by using Wasserstein gradinet descent for the optimization on the density, and for the Kantarovich potential, a H^1 metric optimization is used. The algorithm is a first order method which seems to quickly converge to the stationary point.

### Strengths
1. The presentation is clear, especially on the optimization for the Wasserstein gradient.

2. The numerical experiments seem promising.

### Weaknesses
The reviewer first wishes to comment that the methodology seems an exciting and promising direction in OT and an illuminating extension of the back-and-forth OT algorithm. However, it is hard to take the writing at face value to know the validity of the result. While the reviewer mainly asks for clarification in the remainder of this part, the unclarity of the implementation details in itself is a major weakness.

The major drawback of this work is that the methodology is not clear from the paper, which is why currently it does not seem possible to assess the quality of this work. Specifically, here are some questions that need to be answered:
1. How is the differentiation implemented in this work? Terms such as $\nabla \phi$ are not continuous and admits discrete proxies. Is it done by finite difference? And, if so, what is the scheme? Or, alternatively, is it done by performing FFT, and is some smoothing filter performed? 
2. How is the pushforward implemented in this work? Assuming $\nabla \phi$ is computed, the term $(\nabla \phi)_{\#}$ might exceed the grid specified. How is this going to be resolved in the numerical example? These are questions that need to be addressed within this work. As of now, the reviewer's understanding is that this work only quotes the Jacobs & Leger paper, but that would be insufficient.
3. It is quite confusing as to why the authors use a 1024*1024 grid for Sinkhorn in Figure 1. From the plot, it is clear that the distributions $\mu_1, \ldots \mu_4$ occupy a small region of the grid. Is a smaller size used? This should a priori be mentioned in the numerical experiment section. If somehow the full 1024*1024 space is used, then it would be quite unfair to the Sinkhorn algorithm. Alternatively, does the code for WDHA use the sparsity of the source and target distribution?
4. The comparison between DSB and the proposed method is still inconclusive. It may happen that numerical optimization in addition to a smaller regularization number may lead to better performance in the barycenter functional value and better wall-clock time. The reviewer is not sure if the POT code package result can be taken at face value.

Other major issues:
- The experiments primarily focus on Algorithm 4, but the analysis is done for Algorithm 3. The authors did not clearly show this intricacy in the contribution subsection. 
- There does not seem to be an implementation for Algorithm 3.

Minor issues:
- This work does not sufficiently mention the limitation that it is only efficient for low-dimensional grids. Sinkhorn, in contrast, can work by discretization of continuous densities by empirical distributions. The omission to stress this limitation needs to be resolved.

### Questions
The questions are listed in the weakness section.

### Soundness
2

### Presentation
3

### Contribution
3
