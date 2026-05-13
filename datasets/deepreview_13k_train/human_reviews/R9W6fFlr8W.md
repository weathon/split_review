# A primal-dual algorithm for variational image reconstruction with learned convex regularizers

- Decision: Reject
- Scores: 5, 5, 5, 5, 5

## Abstract
We address the optimization problem in a data-driven variational reconstruction framework, where the regularizer is parameterized by an input-convex neural network (ICNN). While gradient-based methods are commonly used to solve such problems, they struggle to effectively handle non-smoothness which often leads to slow convergence. Moreover, the nested structure of the neural network complicates the application of standard non-smooth optimization techniques, such as proximal algorithms. To overcome these challenges, we reformulate the problem and eliminate the network's nested structure. By relating this reformulation to epigraphical projections of the activation functions, we transform the problem into a convex optimization problem that can be efficiently solved using a primal-dual algorithm. We also prove that this reformulation is equivalent to the original variational problem. Through experiments on several imaging tasks, we demonstrate that the proposed approach outperforms subgradient methods in terms of both speed and stability.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel relaxed formulation of Input-Convex Neural Networks (ICNNs), expressed as a convex minimization problem over intermediate activations. This approach is applied as a regularizer for image inverse problems. The authors solve the resulting convex optimization problem using the Primal-Dual Hybrid Gradient (PDHG) method. The ICNN regularizer is trained in a task-specific manner within an adversarial framework. The effectiveness of this approach is demonstrated on three image inverse problems: salt-and-pepper noise removal, image inpainting, and sparse-view computed tomography (CT) reconstruction.

### Strengths
- The paper is well-structured and articulates its contributions clearly, making it accessible and easy to follow for readers.
- The reformulation of the ICNN as a convex minimization problem, combined with its solution through the Primal-Dual Hybrid Gradient (PDHG) algorithm, is innovative and shows strong potential for practical applications.
- The formulation and theoretical backing of the ICNN as a convex minimization problem are solidly presented, providing a strong theoretical foundation for the proposed approach.
- While the focus is on image inverse problems, the proposed ICNN could potentially be extended to other fields, such as optimal transport, where a deep convex potential is beneficial, showing the paper's broad applicability.

### Weaknesses
 - **Limited Comparison in Experiments**: The experimental section only compares the proposed method with a subgradient algorithm applied to the same objective function, which limits the scope of the evaluation. It would strengthen the findings if the method were compared against a standard ICNN approach or a similar architectures without constraints, as this would better illustrate the relevance and advantages of the proposed modifications. The comparison is particularly weak because the subgradient method is a very basic optimization technique, and it is unclear if it was tuned to perform optimally. The lack of comparison against more sophisticated methods for solving the same problem makes it difficult to assess the practical advantages of the proposed approach.

- **Insufficient Training Details**: The paper lacks clarity on the training process for the ICNN-based regularization. Key aspects, such as the training methodology, hyperparameter choices, and datasets, are either under-explained or absent, which may impact the reproducibility and clarity of the results. For example, the specific architecture of the discriminator in the adversarial training is not specified, nor are the learning rates, batch sizes, or the number of training epochs. This lack of detail makes it challenging to replicate the results and to understand the sensitivity of the method to different training parameters.

- **Rationale for Adversarial Training Choice**: The use of an adversarial framework for training the regularization introduces task dependency, which limits the general applicability of the approach. The rationale behind this choice is not sufficiently justified, especially given that adversarial training can be complex and potentially less efficient compared to alternative approaches. Exploring or explaining why more standard training schemes, such as training by denoising, were not pursued could improve the paper’s rigor and scope. Denoising-based training could make the regularizer more versatile and less sensitive to specific tasks, potentially offering broader applicability. The paper does not discuss the potential drawbacks of adversarial training, such as mode collapse or instability, which are important considerations when evaluating the robustness of the method.

- **Clarity in Problem Motivation**: While the limitations of ICNNs are well discussed in the abstract, they are not sufficiently detailed in the introduction. Expanding on these limitations in the introduction would provide clearer context and stronger motivation for the proposed method. Specifically, the introduction should elaborate on the practical difficulties of training ICNNs, such as the need for careful weight initialization and the challenges in enforcing convexity during training. This would help the reader understand why a relaxed formulation is necessary.

- **Simplistic Architecture**: The proposed ICNN architecture is relatively simple, with only two layers. Recent works have explored deeper ICNN architectures that could improve performance in complex tasks, and the paper would benefit from a comparison or discussion on how a deeper architecture might impact results. The paper does not provide any justification for the choice of a two-layer architecture, nor does it discuss the potential benefits or drawbacks of using a deeper network. This lack of discussion makes it difficult to assess the scalability of the proposed approach to more complex problems.

### Questions
- **Simplification of Training**: Classical ICNNs are known for being difficult and unstable to train due to stringent constraints. Does your proposed formulation help simplify the training process compared to traditional ICNNs? Is this formulation more flexible in practice, or does it still face similar training constraints?

- **Details of the Comparison**: In the experimental section, is the subgradient method used for comparison applied to the same objective function as the proposed ICNN formulation, or is it applied to a standard ICNN? Clarifying this would help in assessing the effectiveness and relevance of the comparison.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper addresses the optimization problem in a data-driven variational reconstruction framework where a neural network-based regularizer, specifically an input-convex neural network (ICNN), is used. The authors propose a reformulation of the problem that removes the nested nature of a network structure. By linking this reformulation to epigraphical projections of activation functions, they convert the problem into a convex optimization format that is suitable for efficient solution via a primal-dual algorithm.

### Strengths
- The authors propose a reformulation of the problem that removes the nested nature of a network structure. By linking this reformulation to epigraphical projections of activation functions, they convert the problem into a convex optimization format that is suitable for efficient solution via a primal-dual algorithm.

- The authors claim to remove the assumption that the activation function does not need to be non-decreasing.

- Numerical validation is presented using the learned convex regularizers.

### Weaknesses
 - The authors claim that their framework does not require the activation function to be non-decreasing; however, the experiments only involve activation functions that are both non-decreasing and convex. Validation with activation functions that are convex but decreasing would strengthen this claim. For instance, how might the framework perform with functions like the negative exponential or negative logarithm functions? These are provided as illustrative examples.

- Additionally, a plot showing the landscape or level curves of the learned regularizer (neural network) would provide valuable visual insight. For instance, the authors can make use of 2D contour plots or 3D surface plots of the regularizer output for different input features. Also, analyzing how the landscape changes during training would help to visually validate the convexity of the neural network.
		
- Based on my previous comments some discussion about the limitations of the proposed framework is needed. For instance, would be interesting to discuss about the computational complexity for larger networks, potential issues with certain types of imaging problems.

**Some minor comments**

- I suggest the authors to change the notation across the manuscript. Vectors in boldface and matrices in capital boldface. Aligning with this standard notation will improve clarity and make the manuscript more consistent with conventions commonly used in the literature.
		
- I suggest the authors to define $\theta$ immediately after equation (EQ) to ease the reading.
		
- Since the authors prove the convexity of the built neural networks would be interesting and needed to plot the landscape/curve levels of the learned regularizer to have a visual understanding of it. Maybe using the reference below.

*Li, H., Xu, Z., Taylor, G., Studer, C., Goldstein, T. (2018). Visualizing the loss landscape of neural nets. Advances in neural information processing systems, 31.*

### Questions
- A primary limitation of this paper is that the learned convex regularizers are restricted to ReLU and leaky ReLU activation functions. Could the authors consider extending their framework to support a broader range of activation functions? For instance is it possible to extend the guarantees presented in this paper to the composition of convex functions? What would be the theoretical challenges in extending the framework to algebraic operations between convex functions?
		
- The neural networks examined in this study are relatively small in scale, raising an important question about scalability. How well does the proposed primal-dual algorithm perform when training larger networks?
		
- On top of my previous comment, the authors did not discuss if the studied networks size are enough for any regularized imaging problem? Could the authors discuss whether the network sizes explored are sufficient for a range of regularized imaging problems? Could the authors provide the computational complexity of the algorithm as the network size increases? Also, some experiments with networks of increasing depth and width could help to demonstrate scalability.
		
- In sparse image recovery, the regularizer must satisfy certain constraints beyond convexity to guarantee unique recovery (see Proposition 4.4 in the reference below). Could the authors provide further explanation on how the proposed learned regularizers address these requirements to ensure uniqueness?
		
*Woodworth, J., Chartrand, R. (2016). Compressed sensing recovery via nonconvex shrinkage penalties. Inverse Problems, 32(7), 075004*

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors propose a novel, more general, formulation of input-convex neural networks (ICNN). The main contribution to the paper consists in relaxing the usual constraint that layerwise functions should be increasing with a mere convexity constraint. This more general framework encompasses the traditional case, but allows for more general neural network architectures. The authors showcase their new architecture on various imaging problems: salt-and-pepper denoising, image inpainting and CT reconstruction.

### Strengths
Overall, this is a well written paper that is both original and interesting. 

1. The paper is original. It goes against the current trend of always larger architectures, and makes interesting links with convex optimization.
2. The paper is mathematically sound.
3. The paper is well written and very clear.

### Weaknesses
The main weakness of the paper is the experimental evaluation. As such, it is difficult to put the work in context of other works due to the lack of relevant baselines (see details in the "questions" section).

1. There are no baselines to which the authors compare their approach in the experimental section.
2. The constraints on the architecture seem quite strong (weight positivity, see comments below).
3. Differences with respect to existing works (PnP, ICNNs) could be further clarified (see comments below).

### Questions
**Main comments**
1. The proposed framework does not limit the number of layers $L$ in the ICNN. However, in the experimental part, the number of layers is set to a maximum of 2 (see equations (8) and (11)). Would a larger number of layers yield better results? Is there a reason for such a low number of layers in practice?
2. I understand that it is not possible to implement all methods and that this paper is quite theory oriented. However, I think that the paper would greatly benefit from (by order of importance) (1) comparisons with other baselines (in particular, the Goujon et al reference proposed by the authors, or even comparisons with much simpler convex models, e.g. wavelets/TV) (2) experiments in color images (3) experiments on Gaussian denoising.
3. How does the proposed method compare to plug-and-play algorithms? For instance, it would seem a natural choice to train $R_\theta$ as a Gaussian denoiser. However, the authors train the model in an unrolled fashion, meaning that a new regularizer needs to be learned for new problems. Could the authors comment on that?
4. The method has 2 major differences with the common architectures for image restoration. (a) first, the fact that the model is tied to an image size; how can the architecture be used for images of sizes different than 256$\times$256? (b) second, the positivity of the convolutional weights seems to be a very strong constraint. Did the authors try to relax this assumption, even-though it departs from the convex setting?
5. Is it correct to state that (8) and (11) do not fit in the standard ICNN framework because $\delta_{C_1}$ is not increasing? I would encourage the authors to strongly state how their new framework differs from that of Amos et al. at the level of the experiments.
6. Some exciting application of this work would be in image quality assessment (IQA). In essence, one can see $R_\theta$ as a measure of the quality of an image. Did the authors consider such application for their model?

**Minor comments**
1. Figure 1 is not very clear: $0.5w_1 + 0.5w_2$ could be put below the blue "x" where it is located, similarly as is done for w1 and w2.
2. Line 125, $z_i$ should be replaced with $\omega_i$ in the expression of $\phi_i$.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this work the authors consider a primal-dual algorithm for solving composite optimisation problems where the regularisation term is parameterised by a non-smooth ICNN. In fact, the authors first present a more general input-convex type reformulation of the regularisation which is more general than the standard ones and then, using epigraphical projection reformulation, rewrite in a convex way the training problem, solving it with a tailored primal-dual algorithm. Numerical tests are showed.

### Strengths
The paper is very nicely written, concise and well-structured.
It provides a good overview of the state-of-the-art approaches existing in the fields of image reconstruction with network-parametrised regularisation models, a good presentation of the fremework of ICNN and the nice idea of convexifying the (in principle) more general reformulation introduced by the authors via epigraphical projections, which is, essentially, a lifting procedure making the relaxed problem convex and amenable to be solved by, e.g., primal-dual algorithms.
Quite a few numerical results are presented.

### Weaknesses
My main concern is the only comparison with subgradient methods in terms of computational efficiency and the resulting claim that the proposed algorithm improves upon it. This is clearly the case, but the reason is that subgradient method is well-known to be very slow ( O(1/\sqrt{k}) w.r.t. to the function values! I think that something that the authors should do is including a comparison with smooth solvers applied to slightly smoothed versions of their architectures. That would allow you to use gradient-type algorithms and make comparisons w.r.t. to O(1/k) convergent approaches, which I believe is more representative of the speed you obtain.
The other weakness of this work si that the authors introduce a more general theoretical framework in Section 2  which, in practice, is not really used later on in the experiments. The framework proposed, indeed, is nice but hardly related to the standard linear + non-linear nature of NNs, so the authors indeed simply apply it to ICNN, as expected. I am not sure then that this relies provides anything interesting from a theoretical view point.
The other major limitation is that while nice from a theoretical viewpoint, ICNNs perform worse than less-structured networks. It would be nice to show a baseline comparison w.r.t. to non-convex or, better, weakly-convex regularisers on which, I believe, analogous considerations could be made but with much better performance.
Also, while the authors declare explicitly their interest into imaging applications starting from the title, I think that some further tests to more ML-related applications showing the interest of ICNN there (if any) would be appreciated.

### Questions
- I think the author should at least talk about proximal-gradient methods to address non-smooth problems. Primal-dual algorithms are not the only algorithms used for this.
- The sentence "the above problem is non-convex despite the objective is convex" is very foggy. I would be more precise here and relate the underlying non convexity to the constraint considered.
- The authors should add a comparison with gradient-type algorithms used to solve smoothed version of their problem for making conclusions about the computational gain in comparison also to a smoothed version of the regulariser considered. Somethimes a slight smoothing is better when balancing the computatonional/reconstruction improvements.
- I am not sure I understand the idea of showing results in early iterations where the training process is far from having converged.
- The subgradient algorithm should be written. Moreover, for each problem considered, the subgradients should be written and reported, at least, in the Supplementary material.
- A further comparison with less-structured regularisation network (non-convex or weakly-convex) should be added to position your results w.r.t. to the state-of-the-art.

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper considers a classical fidelity + regularization model for image reconstruction, where the regularizer is an Input Convex Neural Network (ICNN). This construction, together with the choice of a fidelity term as a convex function, make the objective function of the optimization problem convex. However, the nested structure of such regularizer make the problem hard to optimize, therefore the authors consider an equivalent formulation where the nested structure is removed by inserting a constraint to the optimization problem. However, due to the non-convexity of the feasible set, the problem becomes non-convex. To avoid this issue, the authors propose to consider instead the epigraph of the feasible set, obtaining an optimization problem which is equivalent to the original optimization problem, while being convex. This allows the authors to use the fast and stable Primal-Dual (PD) algorithm from [Chambolle, Pock; 2011].

### Strengths
The paper is well-written and the math is mainly correct. The results shows that the proposed method is superior than the algorithms to which the authors compared, showing a small, but non-zero, improvement in the state-of-the-art to which this paper refers.

### Weaknesses
I believe the idea is not original enough to be published on a big conference such as ICLR. Indeed, to my understanding, the proposed model is obtained by combining the known and widely used ICNN-based regularizer (see, e.g. Learning Convex regularizers for inverse problems; Mukherjee et al.; 2021), with a known technique to remove the nested structure (Carreira, Perpinan; 2014) and the known epigraphical projection (Chierchia et al.; 2015). The problem is then solved through the application of the classical Primal-Dual optimization algorithm, widely used to solve convex non-smooth optimization problems. All of these methods appear, to the reviewer, to be combined with no major improvements or adaptations with respect to the paper from which they are taken. While this could not be a major issue for most journals and conferences, I believe this is not enough novelty to be accepted and published on a conference such as ICLR. Clearly, I am open to change my mind if I understood it wrong.

Anyway, I also found some aspects of the paper which I suggest to improve:

- The most relevant criticism is on the experimental section. In particular, the authors compare their ICNN-based regularization model solved by PD algorithm against the same model solved by other Subgradient Methods (SM). However, I believe that the optimization algorithm employed is the least innovative aspect of the paper, in particular when compared to the choice of the learned regularizer. I suggest the authors to compare their method with other regularization methods such as Total Variation, Wavelets, or any other learned regularization method. Moreover, I kindly ask the authors to explain their rationale or focusing on optimization algorithm comparisons rather than regularizer comparisons.
- The method on which the authors compare (i.e. the SM-C and SM-D methods) are not introduced nor cited. In particular, I did not find any reference to which algorithms have been employed specifically, and which choice of the parameters has been employed. Could you please provide them?
- Be more specific in the proof of Theorem 3, you say that the two formulations are equivalent, but you only show that their minimum is the same. For two optimization problems to be equivalent, they are supposed to have the same minimum points, i.e. the two minima are achieved at the same value of $x$. This does not necessarily hold if they have the same minima. For example, the functions $f(x) = x^2$ and $g(x) = (x-1)^2$, both have the same minimum (i.e. 0), but their minimum points is $x=0$ for $f(x)$, $x=1$ for $g(x)$. Therefore, they are not “equivalent”.

**Minor Comments.**

- In line 66, “step-size selection” should be erased.
- In line 69-70, there is a repetition of “remove”.
- In Assumption 2, $D$ does not directly depend on $x$, while it depends on $x$ through $A$. I suggest to explicitly say that “$D(Ax, y)$ is convex in $x$”.
- In Theorem 3, specify is the “min” in $w_{L-1}$ is a minimum or an inf, since the notation is changed through the paper.
- In line 241, add a citation to SM-D and SM-C methods.
- In equation (10), how do you compute the matrix norms in the algorithm?
- In Figure 3, when the legend says “Proposed”, to which parameter choice it refers? I also suggest to add a grid on the plot background of Figure 3 to improve readability.
- In line 314, “3% Gaussian noise”, what does it mean? You add Gaussian noise with standard deviation of 0.03? The norm of the noise is 3% of the norm of the data? 
- In the Computed Tomography (CT) experiment, the amount of information measured is too high, making the problem “easy” to solve. I suggest testing more extreme geometries such as 60-90 angles, instead of 200, to show how the proposed method behaves in other scenarios.

### Questions
I included a few questions in the "Weakness" section.

### Soundness
4

### Presentation
3

### Contribution
2
