## Human Reviewer 1

### Summary
This paper concern with the problem of Geodesic Principal Component Analysis (GPCA), i.e., given $n$ probability measure $\nu_1,\ldots,\nu_n$, we gradually construct a sequence of geodesics $\mu_1,\ldots,\mu_k$, known as the principle components, such that   
\begin{equation*}
    \mu_i = \inf_{t \mapsto \mu(t) \text{ geodesics}} \sum_{i=1}^n \inf_{t_i} W_2^2(\mu(t_i),\nu_i), 
\end{equation*}
and the subsequent principle components satisfy the same cost function with additional constrains about orthogonality with previous principle components. To resolve this problem, the authors leverage tool from Otto-Wassernstein geometry. They propose two algorithms to tackle two different settings: centered Gaussian distributions and a.c. probability measures: for first setting, the problem reduces to the matrix quadratic optimisation, for the second setting, by choosing a Gaussian reference measure, the problem reduces to optimise a function with neural network. Then, they validate their algorithms using toy examples (for Gaussian distributions) and some real dataset (MNIST, 3D point cloud, etc. )

### Strengths
$\bullet$ Originality: The problem appears to be novel and applicable to the real dataset, as the authors demonstrate in their experience. 

$\bullet$ Quality: Firstly, the authors provide both theoretical intuition and experimental verification for the algorithm. 

$\bullet$ Clarity: The article is easy to follow in general. 

$\bullet$ Significance: The algorithm provide a method to analysis the principle components of data. In the real data, they relate to some important aspects of data, such as brightness, shape, etc.

### Weaknesses
I think that the article does not provide a quite clear theoretical verification: despite of the fact that the authors provide a nice intuition from Otto-Wassernstein geometry, they do not provide the proof of convergence of these two algorithms. For example, in Lemma 1, they just point out that the loss function admit one global minimum and do not show that the algorithm converge to the, at least, stationary point. In addition, for the case of centered Gaussian distributions, as the author admit, it is unknown that the optimal solution is still Gaussian distribution in general distribution space. Another aspect is that some of the theoretical results seems to not useful in the analysis of these two algorithms. For example, I am not sure that how we use the proposition 6, 7, 8 in our algorithms. 

Minor suggestion: 
- Line 32: accound → account

- Equation 26: inconsistent notation, the author use "]" to denote open bracket "(" and "[" to denote close bracket, while in other formula they use the "(" and ")".

- "hessian" should be "Hessian"

- Line 180: GL should be italic 

- The proof for coercivity is not clear (among the notion of coercivity, which one that you use, and why the norm $\|()\|$ goes to infinity implies the coercivity).

### Questions
1. As pointed out in the weakness section, I miss the point that how can we 
use the proposition 6, 7, 8 in our algorithms. 

2. Can we use this algorithms for some LLMs model or other complicated image tasks? 

3. Can you point out an example that the global minimum point in Lemma 1 is not unique?

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
4

### Confidence
3

---

## Human Reviewer 2

### Summary
The paper introduces a framework for Geodesic Principal Component Analysis (GPCA) of probability measures under the Otto-Wasserstein geometry. It provides exact solutions for Gaussian distributions by lifting computations to the space of invertible matrices and extends the method to general absolutely continuous measures using a neural network-based parametrization of Wasserstein geodesics.  Experiments on Gaussian data, 3D point clouds, and images show that captures meaningful nonlinear modes of variation and highlight the difference to tangent PCA.

### Strengths
**Exposition:**
I found the paper to be very well written. It has a common thread running through it that makes it easy to follow the story. Thus, I could read it in one go and understood all the core ideas. Furthermore, I think all the necessary information is included in the paper needed to reproduce the method and the experiments. The division of information between main text and appendix is also sensible.

**Novelty:**
I think the introduced method is novel and advances the state-of-the-art in measure-based (geometric) data analysis. Thus, I consider it to be a contribution worthy of being published at ICLR. The distinction to similar methods (esp. TPCA) is clearly made and well-explained.

**Theory:**
The included theory is sound and reasonable. To me, all the included theoretical results clearly connect to the overall story of the paper and are well explained. 

**Reproducability:**
With the provided information, the method (esp. the ac. formulation) should be easy to implement. I liked especially that pseudo-code (Alg. 1) was provided, as this always makes things easier to understand. Furthermore, all the experiments are well documented to level where one could reproduce them.

### Weaknesses
**Scalability:** I am a bit worried about the scalability of the method. All examples are conducted on a small scale with at most two components. Thus, the paper leaves the gap what would happen for larger datasets and what kind of resources the method requires in such a scenario. It would be great if the authors could discuss this in the paper and also illuminate if it is, indeed, a problem.

**Practical applications:**
This ties into the second weakness I see with the paper: a lack of practical applicability. As mentioned above, the examples are small and restricted to synthetic examples. Thus, I do not see on which applications the paper could have an (immediate) impact. As I see this as a more of a theoretical/modelling work, I do not consider this as a major issue. However, it would be nice if the authors could include a discussion what kind of applications they envision their method could be useful for (down the line) and how they image their ideas could impact other machine learning work.

### Questions
- Intro: It would be nice to list some concrete examples on the shortcomings of using $L_2$ for probability densities
  - It would be nice to show some concrete examples for prop. 6 in terms of measures and vector fields 
  - Problem 38: Why not a global optimization instead of the block optimization?
  - In the paper, one component is computed after another. Could one find multiple components at once? Is it equivalent? Especially for the neural network part, I do not think this should be hard to implement?
  - What happens for Gaussian distributions with varying centers? Is there still a nice reduced model?
  - Typesetting: please use \colon instead of : when introducing functions
  - Can geodesics be extended in the Otto formulation beyond t_min/max? E.g. by choosing a new horizontal vector?
  - Language: I believe the correct usage is "to lift to \[a space\]" instead of "to lift in \[a space\]"
  - Fig. 3 and others: I believe it would be more instructional to show the cone as a volumetric object. This might be harder a render, but maybe the authors could give it a try.

### Soundness
4

### Presentation
4

### Contribution
3

### Rating
8

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper introduces an algorithm for geodesic PCA using optimal transport ideas. This is done by generalizing a certain formulation of Euclidean PCA, giving an optimization problem for the first principle component involving geodesics in Wasserstein space. Further principal components are defined using orthogonality. There are two versions presented: for Gaussians, and for more general distributions relying on neural network approximation. Evaluations are performed on synthetic Gaussian-type data, and point clouds.

### Strengths
I liked the following:
* **Interesting problem.** Generalizing PCA to spaces of probability measures seems to be a generically useful tool, since comparing distributions is a central task throughout machine learning which recurs in many situations.
* **Technically sound - especially for Gaussian distributions.** The approach involves the Bures-Wasserstein geometry and relationships between certain matrix groups, and makes it easier to see
* **Easily provides use cases beyond what the authors have illustrated.** One way one can think about PCA is that it provides a very crude form of manifold learning, where the manifold is a subset of the ambient Euclidean space. This can be used to define for instance an outlier score, by comparing distance between each datapoint and the PCA subspace. The authors do not consider this, but the fact that it is easily possible reveals the general value of the technique.

### Weaknesses
I am worried about the following:
* **Use of regularization in neural network objectives.** In particular, using regularization to enforce geometric constraints is much weaker than incorporating them as a hard constraint via a clever parametrization. In practice, I suspect the different directions do not end up orthogonal, and it would be helpful to quantify how much this is a problem in practice, and how sensitive it is to hyperparameter tuning. I did not see an experiment directly addressing this.
* **Experiments: Gaussian case should have at least *some* kind of non-synthetic evaluation.** Gaussian experiments are limited to toy datasets designed to highlight differences with ordinary PCA. While this is certainly necessary, it would have been better to also include some kind of non-synthetic datasets where the Gaussian mean and covariance is estimated empirically. For example, in continuous action imitation learning and RL, one often considers policies consisting of neural networks that learn a mean and covariance. In this domain, the authors' form of PCA could be used for things like outlier detection. I am not suggesting the authors necessarily need to add this specific example, more that it's important to have *something* non-synthetic for the Gaussian case since it's a central part of the paper.
* **Experiments: why is there a theorem in the experiments section?** Theory should be presented separately from evaluation, this part should be moved to some part in main body.
* **Experiments: Gaussian case is missing obvious baselines.** In 5.1, a natural baseline is to compare against is Euclidean PCA in the space of Cholesky coefficients of the covariance matrix. How would this produce different results compared to Euclidean PCA with respect to the SPD cone coordinates, or the proposed method?
* **Experiments: non-Gaussian case is missing obvious baselines.** For the point cloud data presented, the most obvious way I can think of to do PCA is take some kind of off-the-shelf model like PointNet, and perform PCA in its latent space, and present the results. While this is certainly a much heavier method, I think some kind of visual comparison needs to be included in the main body, as this is the single most obvious performance question that readers might have.
* **Experiments: no evaluation of downstream applications of PCA like outlier detection.** The authors do not evaluate how good the principal components produced are for any downstream purpose, instead they are just plotted to show their properties. I would like to see at least some kind of quantitative evaluation. For instance, this could be considered for outlier detection, to compare how well linear vs. the proposed geodesic PCA performs. Non-linear PCA has been studied for this specific purpose before, see for instance "Quadric Hypersurface Intersection for Manifold Learning in Feature Space" by Pavutnitskiy et al. which includes full experiments on this. Note that I am not suggesting the authors implement this specific downstream application of PCA, instead I think it is important to have at least some kind of evaluation of this kind.

### Questions
The overwhelming majority of my concerns with this paper concern the comprehensiveness of evaluations and specifically comparisons with various baselines like PCA on PointNet latent space. Please address those comparisons, or argue why they are not appropriate.

### Soundness
3

### Presentation
3

### Contribution
3

### Rating
6

### Confidence
4

---

## Human Reviewer 4

### Summary
This paper introduces a method for exact PCA in the Wasserstein space of probability measures P_2(R^d) under the Wasserstein metric. Instead of performing tangent PCA, which has been an established linearization technique for performing PCA on curved spaces (most heavily used in Riemannian settings) or geodesic PCA (Huckemann et al. Sommer et al.) that have tackled this problem in general Riemannian settings, this paper proposes two methods, i) for geodesic PCA for Gaussian measures, and a ii) neural network approach for parameter optimization for absolutely continuous probability measures. The authors show experimental evaluations on point clouds and image color distributions (mostly qualitative).

### Strengths
The work shows a method to compute principal modes of variation in datasets of probability measures, specifically using the Wasserstein geometry. For Gaussian measures, the method leverages the Bures-Wasserstein geometry and lifts computations to the space of invertible matrices, providing exact geodesics as principal components.

This is a significant contribution over earlier methods which have used linearized Wasserstein distances (Wang et al. (2013) and Boissard et al. (2015)), have approximated Geodesic PCA in 2D (Cazelles et al. (2018)), and the approach by Seguy & Cuturi (2015), which relied on  generalized geodesics to approximate PCA. 


For general absolutely continuous distributions, the reliance on neural network parameterizations of Wasserstein geodesics is clever. 

For the case of centered Gaussians, the application Bures-Wasserstein geometry and the decomposition via invertible matrices is well-motivated and theoretically grounded.

### Weaknesses
The block alternating algorithm for Gaussian GPCA is not guaranteed to always converge to a unique minimum due to non-uniqueness in the problem geometry (the authors acknowledge this).


In the general case, one needs to verify the eigenvalues of the Hessian at each step during the Otto geodesic update. This may be computationally expensive. 

While the neural network implementation facilitates computational tractability, the construction of geodesics needs further tuning and learning from large examples and may have scalability issues. 

The comparisons and experimental results are all qualitative and thus the practical application of this method is in question. However, this is an extremely minor point, not important for the publication of the paper.

### Questions
For experimental results, the authors compare their method against TPCA. How will their method compare with Bigot et al. 2017 (for 1D case)?

### Soundness
4

### Presentation
4

### Contribution
4

### Rating
10

### Confidence
3