# Riemannian denoising diffusion probabilistic models

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 5, 6

## Abstract
We propose Riemannian Denoising Diffusion Probabilistic Models (RDDPMs) for learning distributions on submanifolds of Euclidean space that are level sets of functions, including most of the manifolds relevant to applications. Existing methods for generative modeling on manifolds rely on substantial geometric information such as geodesic curves or eigenfunctions of the Laplace-Beltrami operator and, as a result, they are limited to manifolds where such information is available. In contrast, our method, built on a projection scheme, can be applied to more general manifolds, as it only requires being able to evaluate the value and the first order derivatives of the function that defines the submanifold.  We provide a theoretical analysis of our method in the continuous-time limit, which elucidates the connection between our RDDPMs and score-based generative models on manifolds. The capability of our method is demonstrated on datasets from previous studies and on new datasets sampled from two high-dimensional manifolds, i.e. $\mathrm{SO}(10)$ and the configuration space of molecular system alanine dipeptide with fixed dihedral angle.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Denoising diffusion probabilistic models (DDPM) [1] are a popular class of deep models used for image and video generation, denoising, super-resolution and other applications. These models work in Euclidean space. This manuscript proposes an extension of DDPM from R^n to submanifolds of R^n that are implicitly defined by an equality \xi(x)=0. i.e. the sub-manifold is implicitly defined as a level set of some smooth function \xi(x). The main idea behind the work is to combine the DDPM [1] with submanifold-projected diffusion [2]. The gist of it is that you can add noise to a data-point on the manifold, obtaining a point outside the manifold which is then retracted to the manifold by solving for \xi(x)=0 using Newton iterations. The authors present the exact probability distributions of the forward and backward Markov processes that follow this idea. Describe the method in detail and present several experiments on both "classic" mathematical manifolds such as SO(10) as well as manifolds that approximate meshes (the Stanford bunny and Crane's cow model).

[1] Ho, Jain, Abbeel. "Denoising Diffusion Probabilistic Models". NeurIPS (2020).
[2] Ciccotti, Lelièvre, Vanden-Eijnden. "Projection of diffusions on submanifolds: Application to mean force computation". Communications on Pure and Applied Mathematics. (2007)

### Strengths
While I am not an expert on diffusion models, the work appears like a natural extension to the submanifold setting. The paper is easy to read and the experimental section seems thorough enough as it contains several examples from different domains. Furthermore, the accompanied code appears examplary and contains clear instructions on how to reproduce the results.  Overall, this appears to be high-quality work.

### Weaknesses
In my opinion there is only one small missing element that is easy to address: the paper should contain more details regarding the computational cost of the proposed procedure. At the very least I would like to see runtimes for the experiments in the paper and a short appendix section explaining all the computational costs associated with the procedure, how they depend on the dimension of the sub-manifold, the complexity of the level-set function, and the number of Newton iterations required for projection, etc. so that readers would have a good idea when and where this method might be applicable. Specifically, it would be helpful to understand how the cost scales with the ambient dimension, the intrinsic dimension of the manifold, and the complexity of the function \xi(x) defining the manifold. Furthermore, the number of Newton iterations required to achieve a desired level of accuracy in the projection step is a crucial factor that should be analyzed, as this will directly impact the overall computational cost. A discussion of the trade-offs between projection accuracy and computational cost would also be valuable.



### Questions
* Line 146: So what happens if the solution does not exist? What does your method actually do in that case?
* Line 239: "they should be relatively small" - relative to what?
* Line 529: "We have demonstrated [...] high-dimensional manifolds that can not be easily studies by existing methods" - can you be more specific here about what you demonstrated? Are you referring specifically to the SO(10) example in section 6.3?

A few minor suggestions:
* There are a few places where the language used is a bit odd. For example, just in the abstract we have the following: "most of the manifolds interested in applications" (clearly, manifolds are not interested in anything). "Laplacian-Beltrami" (instead of Laplace-Beltrami), "SO(10) and configuration space" (missing "the").
* Line 081: "gradually destructing" - did you really mean to say destructing here?
* Eq. (5): it is not clear at this point why b(x) is needed as this is only explained later in page 5 so you may want to refer the reader to that explanation here.
* Lines 249-255: an illustration would be nice here showing some submanifold and a helpful choice for b(x).
* Line 320: "DDPMs employ a forward Markov chains" - should be "Markov chain".
* Tables 1,2: it would be better to write "negative log-likelihood" instead of NLL and to also state that "smaller is better" to make the tables clearer to the casual reader who doesn't read the paper but just skims tables and figures.

### Soundness
4

### Presentation
4

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
This paper presents a Riemannian Denoising Diffusion Probabilistic Model (RDDPM) designed for learning distributions on submanifolds embedded in a Euclidean space. The key advantage of this approach, compared to existing diffusion models on manifolds, is that it does not require extensive information of the manifold such as its eigenfunctions or geodesics. Instead, it employs a projection scheme that relies solely on the level set function defining the manifold. The authors proposed a training algorithm and analyzed the continuous-time limit of the model. Experimental results demonstrate the effectiveness of the method in learning distributions supported on a known manifold.

### Strengths
1. The paper is well-written and well-organized, making it easy to follow.  
2. While the idea of using a projection scheme instead of relying on extensive manifold information, such as geodesics and Laplacian eigenfunctions, has been explored in previous works, it remains an interesting approach for defining a noising/denoising Markov chain with (implicitly given) transition kernel.  
3. The authors conduct extensive experiments to demonstrate the effectiveness of the proposed model.

### Weaknesses
1. One of my main concerns is Equation (8), which defines the transition kernel. Although the map $G_x: \mathcal{M} \to T_x \mathcal{M}$ is well-defined, it is not a true bijection due to the possibility of multiple solutions arising from the constraint in Equation (5). This implies that Equation (8) may not hold in general. While the authors mention in a footnote that $\sigma$ can be chosen small enough to ensure that Equation (5) has at least some solution with high probability, the fundamental issue of multiple solutions cannot be avoided. The reliance on a numerical solver to pick one solution from potentially multiple options introduces an element of arbitrariness and makes the theoretical analysis less rigorous. The lack of a guarantee that the selected solution is consistent across iterations further complicates the analysis of the Markov chain's convergence properties.

2. Unlike Euclidean diffusion models, which do not require explicit forward simulation, the proposed method relies heavily on extensive forward simulation for training, as the transition kernel from time zero to any arbitrary time is not readily available. It would be beneficial to report this additional computational time in the numerical experiments. The computational cost associated with solving the projection equation (5) at each step of the forward simulation is also a significant overhead that should be quantified. This is especially concerning given that the projection is not guaranteed to be unique and may require iterative numerical methods.

3. The equilibrium distribution is generally unknown in the presence of a nontrivial ambient drift $b(x)$. The authors suggest that this distribution can be approximated by running a sufficiently long forward Markov chain. However, this process may be time-consuming, especially since $\sigma$ must be small to address the issue of Equation (5) lacking solutions. The convergence rate of this Markov chain to the equilibrium distribution is also unclear, and the authors do not provide any theoretical or empirical analysis of this convergence. The choice of the drift $b(x)$ and its impact on the convergence rate and the quality of the approximation of the equilibrium distribution are also not discussed in detail.

### Questions
Please refer to the previous section

### Soundness
2

### Presentation
3

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
This paper introduces a method for generative modelling when the data is specified on a pre-defined Riemannian submanifold of Euclidean space. In contrast to previous methods, it uses a projection scheme to construct trajectories on the manifold, only requiring gradient information of the defining equation for the manifold. Theoretical derivations show connections between the continuous-time limit of this method and Riemannian score-based methods. The projections onto the manifold for the forward and reverse process are computed by solving a system of equations using Newton's method. This method is then tested on datasets supported on different manifolds.

### Strengths
The techniques in this paper allows for training diffusion models on a more general class of manifolds than other methods, only requiring knowing the defining equation of the manifold. It solves a system of equations to ensure the points generated by the forward and reverse processes stays on the manifold, instead of requiring knowledge of the closest-point projection onto the manifold. There are extensive experiments on a variety of manifolds and datasets.

### Weaknesses
In my opinion, the disadvantages of this method (outlined below) outweighs the main advantages (allowing for more general manifolds). The main contribution seems to be solving for the projection numerically, which is only useful when the exact projection onto the manifold is not known, but there needs to be more evaluation on this front.

1. During training, the entire trajectory for the random walk needs to be generated.  The training objective predicts the expected value of $x^{k}$ given $x^{k+1}$, unlike score matching which predicts the expected value of $x^{0}$ given $x^{k+1}$. This requires storing and processing the entire trajectory, which can be computationally expensive, especially for high-dimensional data or long trajectories. Furthermore, the method's reliance on predicting $x^k$ from $x^{k+1}$ may lead to accumulation of errors during the reverse process, as small inaccuracies at each step can propagate and amplify over the many steps required.

2. During sampling, because trajectory generation can fail, small steps are necessary as taking large steps will increase the chances of (11) having many or no solutions. This sensitivity to step size makes the method less practical for generating samples efficiently. The need for small steps significantly increases the computational cost of sampling, and the potential for failure in trajectory generation introduces instability into the sampling process.

3. Because this method predicts $x^{k}$ given $x^{k+1}$, the number of sampling steps need to be the same as that of training steps (200-800 steps). This is large compared to <50 steps needed for fast samplers of diffusion models in Euclidean space. This large number of steps makes the method computationally expensive and slow for generating samples. The computational overhead of such a large number of steps is a significant drawback, especially when compared to more efficient sampling methods.

4. The analysis in the paper does not consider cases where the projection is not unique, or when equations (9) and (11) have no solutions. This lack of consideration for these cases raises concerns about the robustness and reliability of the method, especially when applied to complex manifolds where such situations are more likely to occur. The theoretical guarantees of the method are weakened by this oversight.

5. The evaluation for higher dimension manifolds only compares histograms of some statistics of the forward process and reverse process, and it is unclear from these how close the generated distributions are to each other. Comparing histograms of statistics is not a rigorous way to evaluate the quality of the generated samples. It is possible for the histograms to match while the underlying distributions are significantly different. More robust metrics are needed to assess the similarity between the generated and target distributions.

### Questions
I would suggest that the authors try this method on more manifolds where only the defining equations are known but without closed-form projections, and devise better evaluation metrics for these manifolds.

Questions: 
1. Have the authors considered using diffusion models in Euclidean space to learn the distribution on the manifold? The generated distribution may not lie exactly on the manifold, but one can project onto the manifold as a final step after diffusion sampling.

2. Is there a better way (e.g. total variation distance) to evaluate the generated distributions on SO(10) and alanine dipeptide where one can compare numerical values instead of histograms?

3. It would also be nice to have some ablation studies on the hyperparameters of the experiments.

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
2

### Summary
This paper presents Riemannian Denoising Diffusion Probabilistic Models (RDDPMs), a denoising diffusion model for learning distributions over submanifolds of Euclidean space. The key insight stems from the fact that a projection-based approach becomes relatively straightforward when the manifold is represented as the zero-level set of some smooth function $\xi$. Unlike previous work, the method proposed here does not require sampling of geodesic paths, the heat kernel on the manifold, or other similar geometric quantities. The method uses the fact that forward and reverse process transition densities for the underlying diffusion Markov chain become tractable if one has access to $\nabla \xi$. The authors present an algorithm to sample trajectories from the forward and reverse process using Newton's Method. They show that in the limit of infinitely many denoising steps, the objective converges to the continuous time score matching objective from previous work.

### Strengths
(1) The projection-based method is easy to understand, and doesn't require the exponential map or the manifold's heat kernel. 

(2) The approach is well-motivated, as previous work either (a) relies on substantial geometric information about the manifold that isn't typically available, or (b) assumes a restricted class of manifolds (i.e. symmetric manifolds)

(3) A theoretical connection to continuous-time score based generative modeling is established in the limit of infinite resolution timesteps.

### Weaknesses
 (1) One claim about previous work seems unsubstantiated: In line 053, the paper states that existing continuous-time methods suffer from error based on time-discretization, something that RDDPMs avoid. But no experiments are provided to justify this. Furthermore, results in Table 1 suggest that RDDPM does not, in general, perform better than existing approaches. 

 (2) Some of the presentation is a little unclear: 
- In line 137, the function $b: \mathbb{R}^n \rightarrow \mathbb{R}^n$ is referenced, but not defined or discussed until line 235. Can some of this discussion be moved to line 137?
- In line 138, $\nabla \xi$ is referred to as an orthogonal direction, even though it is a matrix $\in \mathbb{R}^{n \times (n-d)}$. Should the wording perhaps be "along an orthogonal direction in the column space of $\nabla \xi$?
- In Table 1, were the baselines trained with isolated points as well?
- Can the best-performing approaches in Tabe 1 be underlined or starred? This would make it easier to parse. 

 (3) Poor RDDPM performance on real data (Table 1): the real data evaluations indicate that RDDPM performs worse than baseline methods. Furthermore, no discussion of these results is provided.

 (4) The method seems extremely computationally expensive. Generating forward or reverse process trajectories requires $N$ calls to Newton's method. Furthermore, if Newton's method doesn't find a projection, the entire trajectory is discarded.

 (5) The paper doesn't acknowledge the case when the projection operator is not unique (which can occur if the step size is large enough in comparison to the reach of the manifold). Can some discussion about the potential consequences of this be added?

 (6) The projection scheme isn't a true orthogonal or closest point projection, as $\nabla\xi(x) \neq \nabla\xi(y)$ in general. While in the continuous-time limit this doesn't seem to be a problem, I would appreciate some more discussion about this.

### Questions
(1) Do all d-dimensional smooth, compact, and connected submanifolds of $\mathbb{R}^n$ fit within this framework?

(2) Do the columns of $\xi(x), x \in \mathcal{M}$ form a basis of the normal space to $\mathcal{M}$ at $x$?

(3) Empirically, how often does Newton's method fail (and the trajectory needs to be discarded)? This question applies to sampling both forward and reverse process trajectories.

(4) Can existing approaches be evaluated for the SO(10) group or Alanine Dipeptide experiments for comparison? If not, can the reasons be described?

### Soundness
3

### Presentation
2

### Contribution
2
