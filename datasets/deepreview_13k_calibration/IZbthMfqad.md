# Deep Koopman-layered Model with Universal Property Based on Toeplitz Matrices

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 5, 5, 8

## Abstract
We propose deep Koopman-layered models with learnable parameters in the form of Toeplitz matrices for analyzing the dynamics of time-series data.
The proposed model has both theoretical solidness and flexibility.
By virtue of the universal property of Toeplitz
matrices and the reproducing property underlined in the model, we can show its universality and the generalization property.
In addition, the flexibility of the proposed model enables the model to fit time-series data coming from nonautonomous dynamical systems.
When training the model, we apply Krylov subspace methods for efficient computations.
In addition, the proposed model can be regarded as a neural ODE-based model.
In this sense, the proposed model establishes a new connection among Koopman operators, neural ODEs, and numerical linear algebraic methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a novel deep Koopman-layered framework for modeling dynamical systems, particularly suited for nonautonomous time-series data. This approach integrates Koopman operator theory with Fourier functions and learnable Toeplitz matrices, enabling the simultaneous estimation of multiple Koopman operators to capture temporal dynamics. The model is theoretically robust and flexible, leveraging the universal and reproducing properties of Toeplitz matrices, which enhance its generalization capabilities. Efficient training is achieved through Krylov subspace methods.

### Strengths
1. **Originality**
The paper introduces an innovative integration of deep learning techniques with Koopman operator theory. By proposing deep Koopman-layered models that utilize learnable Toeplitz matrices and Fourier functions, the authors offer a fresh perspective for analyzing nonautonomous systems, which are often challenging for traditional methods. The approach of simultaneously estimating multiple Koopman operators is a notable contribution that broadens the model's applicability.

2. **Quality**
The authors provide a solid mathematical framework that substantiates their claims regarding the universality and generalization properties of the proposed model.

3. **Clarity**
The paper is well-structured and almost clearly written. The authors effectively convey the motivations behind their approach and highlight the significance of Koopman operator theory.

4. **Significance**
The significance of the paper lies in its potential impact on the fields of dynamical systems and machine learning. By bridging these two areas, the proposed deep Koopman-layered models could advance the analysis of time-series data from nonautonomous dynamical systems.

### Weaknesses
1. To my understanding, the choice of the Fourier basis in the proposed deep Koopman-layered model is motivated by its universality in function representation, desirable theoretical properties for analyzing Koopman operators, flexibility in learning multiple operators simultaneously, and compatibility with efficient Krylov subspace methods for low computational cost. However, it is still unclear:

- What specific properties of the Fourier basis make it particularly suitable for capturing the dynamics of nonautonomous systems compared to wavelet bases or polynomials? For instance, while Fourier bases are eigenfunctions of the Laplacian on the torus, it's not immediately clear how this directly translates to superior performance for general nonautonomous systems. A more detailed explanation of the link between the spectral properties of the Fourier basis and the dynamics of nonautonomous systems is needed.

- How does the use of the Fourier basis influence the convergence rates of the learning algorithms employed in the deep Koopman-layered model? Specifically, what are the implications of using a fixed set of Fourier basis functions for approximating functions with varying degrees of smoothness? A discussion on the approximation error and its dependence on the number of basis functions would be beneficial.

- Can the model's performance be enhanced by incorporating additional basis functions alongside the Fourier basis, and if so, how would this be implemented? For example, could a hybrid basis set, combining Fourier functions with wavelets or polynomials, offer improved performance for certain classes of nonautonomous systems? What are the trade-offs between computational cost and approximation accuracy when using such hybrid bases?

- How does the choice of the Fourier basis compare to other potential basis functions in terms of computational efficiency and accuracy when modeling complex nonautonomous dynamical systems? A quantitative comparison of the computational cost and approximation error for different basis functions would be valuable.

2. The theoretical and numerical results in the paper are restricted to the torus. Although this has several advantages theoretically, it may limit the applicability of the theoretical results for many cases, especially for real-world scenarios. It would be great to know how the insights gained from the toroidal analysis may provide a foundational understanding to explore and develop models for more general cases, ultimately enhancing the applicability of the theoretical results to real-world scenarios. For example, how can the results be extended to systems defined on more general manifolds or Euclidean spaces, and what are the challenges involved in such extensions?

3. There are no experiments for chaotic dynamics. So, what happens if the training dynamics are more complex, such as in the case of (autonomous) chaotic dynamics with a **mixed Koopman spectrum**? The paper should address the limitations of the proposed method when dealing with systems exhibiting a continuous spectrum, and discuss potential modifications to handle such cases.

4. The sentence "By computing the eigenvalues of Koopman operators, we can understand the long-term behavior of the undelined dynamical systems" in the Introduction, line 29, may be better if mentioned specifically for systems with a discrete Koopman spectrum, but not in general (for example, not for systems that exhibit a continuous spectrum rather than a purely discrete set of eigenvalues).

### Questions
I) What are some potential real-world applications of the deep Koopman-layered model? 

II)  The paper discusses the concept of multiple Koopman layers. What criteria should be used to determine the **optimal number of layers** in the model? Could you provide guidelines or heuristics for selecting the number of layers for different types of problems or datasets?

Please also see "Weaknesses".

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The authors present an approach for learning Koopman representations of time-series datasets. The main idea is to transform the data into a new space using fourier functions where the dynamics can be approximated by a switching linear dynamical system. They also propose to use Krylov subspace methods to approximate the matrix exponentials which define the time evolution of the linear system.

### Strengths
- Transforming the original space into the space of observables using fixed basis functions (as opposed to learning the space of observables like in Lusch 2017) allows the authors to develop a strong theoretical backing for their approach including showing universality and a generalization bound. I think the theoretical foundation of the work is its strongest feature.
- A nice feature of the approach is that one can analyze the eigenvalues of the trained model to interpret the underlying system (for example whether it is measure preserving or not).
- The idea of using Krylov subspace methods to approximate the matrix exponential matrix product in this context is novel as far as I'm aware.

### Weaknesses
 - Overall, I found it quite challenging to understand the details of your proposed learning algorithm and I am not confident that I would be able to reproduce your approach using your paper alone (that said, I appreciate the authors providing their code in the supplementary materials). It would have been helpful for me if you had included a section which provides a step-by-step summary or an algorithm block showing how your approach works for a given time-series dataset. Specifically, the paper lacks a clear description of how the Fourier basis functions are selected or parameterized, and how the switching linear dynamical system is trained using the transformed data. The precise optimization procedure, including the loss function and training details, is not sufficiently explained, making it difficult to assess the practical implementation of the method.
- I think the claims you make in S7 (that your approach provides an alternative to neural ODE-based models or other deep Koopman based approaches) is not well-supported by your numerical studies. To put these claims on solid footing you need to include numerical studies showing your approach can provide equivalent performance on some common time-series benchmarks; for example see the numerical studies [1]. The current numerical experiments do not adequately demonstrate the method's performance against established benchmarks, particularly in scenarios involving complex, high-dimensional time-series data. The comparison to other Koopman-based methods is insufficient to justify the claim of being a viable alternative to neural ODEs, which have demonstrated strong performance in various time-series forecasting tasks.
- It wasn't clear to me how your approach can be used in time-series forecasting (i.e. making predictions for $t>t_J$. The paper primarily focuses on learning the Koopman representation within a given time window, but it does not clearly articulate how this learned representation can be used to extrapolate beyond the observed time window. The practical application of the method for forecasting future time steps is not addressed, which is a crucial aspect for time-series analysis.

### Questions
- In my understanding of your work, you learn an approximation to a time-series dataset over the time-window $t \in [t_1, t_J]$. In most time-series forecasting problems, one goal is to generate forecasts beyond the time-window in which the observations were collected. With your approach how do you generate forecasts for $t \geq t_J$?
- It wasn't clear to me under which conditions the Toeplitz matrix will be sparse in practice. Can you discuss in which cases this will be true? How will your approach scale in cases where you cannot make this assumption?
- My understanding is that you haven't placed requirements on your Fourier functions that they be invertible. In this case, is it possible to reconstruct the original space once you've made a forecast in the observable space?

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors introduce a concatenation of Koopman operator approximations ("Deep Koopman model") defined on a Fourier approximation of the L^2 space on an n-torus, for the approximation of nonlinear, nonautonomous dynamical systems.
They propose to learn the generator in each of the Koopman operators (i.e., in each "layer" of the model) as Toeplitz matrices, and then map the learned generators to the corresponding operator using matrix exponentials.
The model is analyzed regarding universal approximation and generalization, and compared to KDMD and EDMD on several numerical examples on the torus.

### Strengths
Constructing models for non-autonomous, non-linear dynamical systems is a very important and very challenging problem. On the n-torus, Fourier series provide a very efficient and useful dictioanry to approximate functions in L2, so the setting the authors chose to present their Koopman approximation is reasonable. The theoretical contributions cover most of the important, first aspects that should be treated when introducing a new model, and seem to be proven appropriately. The numerical examples are chosen well, and illustrate the efficacy of the new method. The connection to neural ODEs (or rather, approximation of ODE vector fields using neural networks) is interesting and should be explored further.

### Weaknesses
The authors chose an extremely specific setting (systems on n-tori) and can therefore avoid the most challenging question in Koopman operator approximation - how to choose the proper dictionary for a given problem? The challenging aspect in their setting thus only comes from the fact that the chosen systems are non-autonomous, not that they are non-linear. Unfortunately, the authors do not discuss any existing methods for non-autonomous systems or compare their method in the numerical setting against them. In fact, the "deep Koopman model" proposed by the authors may not even be appropriate for general non-autonomous systems, because the number of internal "layers" may need to go to infinity for such systems, e.g. if the time-dependent part is not periodic (but, e.g., linear: $\dot{x}= -x+t$). I list those concerns in more detail below.

 * One of the most challenging aspects of numerical Koopman operator approximation is the choice of function space and corresponding truncation. The authors only work on the n-torus, for which the Fourier basis is a good choice - but this also means that they do not discuss (at all) the issues arising when the base space is not an n-torus (which, I would argue, is a very common case in practice). While diffeomorphisms can map other manifolds to the n-torus, this does not mean that the Fourier basis remains the optimal choice for the transformed system. The choice of basis functions is intimately linked to the geometry of the underlying manifold, and using a Fourier basis after a diffeomorphism can lead to a poor approximation if the diffeomorphism significantly distorts the original geometry. The authors should acknowledge that the effectiveness of their method is highly dependent on the suitability of the Fourier basis for the specific problem, and that this suitability is not guaranteed for general manifolds.

 * The authors should incorporate and discuss existing literature on learning dictionary functions and switched systems:
   - Li, Qianxiao, Felix Dietrich, Erik M. Bollt, and Ioannis G. Kevrekidis. “Extended Dynamic Mode Decomposition with Dictionary Learning: A Data-Driven Adaptive Spectral Decomposition of the Koopman Operator.” Chaos: An Interdisciplinary Journal of Nonlinear Science 27, no. 10 (October 2017): 103111. https://doi.org/10.1063/1.4993854.
   - Peitz, Sebastian, and Stefan Klus. “Koopman Operator-Based Model Reduction for Switched-System Control of PDEs.” Automatica 106 (August 2019): 184–91. https://doi.org/10.1016/j.automatica.2019.05.016.

 * Experiment 6.2.1 is not using proper dictionary functions for KDMD and EDMD, and hence the numerical results are unfavourable for these methods compared to the presented method. The authors should either learn Koopman operators separately for each subset, or use time-dependent dictionary functions for EDMD - the true model is periodic with period $2\pi$, so it should be easily possible to properly encode the dynamics even with classical EDMD (and time-dependent dictionary). The current implementation of EDMD and KDMD uses a static dictionary, which is not appropriate for a non-autonomous system where the dynamics change over time.  A more appropriate comparison would involve learning time-dependent dictionaries or using a switched system approach, where different Koopman operators are learned for different time intervals. The authors should also consider using a finer discretization of time and switching between different Koopman operators at each interval, as suggested by the switched system literature.

### Questions
* I do not understand the sentence in the introduction: "In addition, since each Koopman operator for a time window is estimated individually in these frameworks, we cannot take the information of other Koopman operators into account.". A single system only has a single Koopman operator (family, if one considers one operator per time t). What do the authors mean by "other Koopman operators"? The family?

 * For proposition 5.1: is it not possible to use simple Monte-Carlo arguments to show that the variance of $h(x,y)$ goes to zero with $1/\sqrt{S}$ (i.e., $1/S \sum_i(h(x_i,y_i)$) converges to $E[h(x,y)]$ with the Monte-Carlo rate of $1/\sqrt{S})$? The current bound involves operator norms which may be unbounded, correct?

 * l478 "our framework provides numerical linear algebraic way to train Neural ODE-based models" which part of the "deep Koopman" model represents the neural network from the Neural ODE? The neural ODE framework was introduced by Duvenaud and coauthors (Chen et al. (2018)) to mitigate the memory consumption of back-propagation through classical solvers, they propose instead to use the adjoint method. Where does the memory footprint come in with the new method? "Finding the vector field of an ODE" is not the novelty of Chen et al. (2018), it is finding it *efficiently* (without a lot of memory cost).

 * How many internal layers would one need to approxiamte the simple non-autonomous system "\dot{x} = -x+t"?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes a deep Koopman-layered model designed to analyze the dynamics of time-series data, particularly focusing on nonautonomous dynamical systems, where the system's behavior changes over time. The model leverages Koopman operator theory, which provides a linear framework for analyzing nonlinear dynamical systems, and it is structured as a series of "Koopman layers", each approximating a Koopman operator at a specific time point. These layers allow the model to capture the evolving dynamics of the system. Toeplitz matrices are utilized to construct the Koopman layers. Krylov subspace methods are utilized for efficient computation of the Koopman operators. The model further uses the Fourier basis functions as the representation space for the Koopman operators. This choice is justified by the theoretical properties of the Fourier basis, including its universality and the ability to derive generalization bounds for the model. The paper establishes the universality of the proposed model, meaning that it can approximate any function within the chosen representation space with arbitrary accuracy, given enough layers. Additionally, the authors derive a generalization bound, indicating the model's ability to perform well on unseen data.

### Strengths
The idea of using sequence of Toeplitz matrices to parameterize Koopman generator and leverage its universal property to prove the universality and generalization of the approximation scheme is novel and original. The work is solid in the sense that the framework allows explicit error control which is often missed in other Koopman operator learning literatures. Experimental results also confirms the importance of regularization as derived in the generalization bound and shows superior performance against some other approaches, in terms of the distribution of the identified eigenvalues (around the unit circle). Although the idea of “using a moving stencils method to compute the time-dependent Koopman operator (and in each local stencil, the dynamical system is assumed time invariant)” is not new (see eg. “Data-driven reduced-order modeling for nonautonomous dynamical systems in multiscale media” by Mengnan Li, Lijian Jiang), this work makes decent contribution to the workstream of Koopman operator learning for non-autonomous systems with theoretical basis.

### Weaknesses
- I don’t agree with the statement “For existing Neural ODE-based models, we use numerical methods, such as Runge-Kutta methods, to solve the ODE  (Chen et al., 2018)” in section 7.1. In fact, one of the innovations in that work was the authors solved the adjoint equation backwards in time to obtain the gradients automatically for parameter updates, so that one can circumvent the memory issues caused by using other numerical methods, such as Runge-Kutta, although I do agree that using Krylov subspace methods to compute $e^{L_j u}$ in the work has similar potential too.

- The notations are sometimes confusing or overloaded to digest. For example, page 3 line 161, it seems the notation of $x_k$ was not properly defined before its appearance? The superscripts and subscripts in equation (2), (3) are heavy, the authors may consider simplifying it with a bit abuse of notation OR show how it works 1D case and with 1 system so that j=1 and k=1 OR provide a more concrete examples to guide the readers through in appendix. 

- In addition, consider citing two papers from Mitsubishi lab
  - "Physics-Informed Koopman Network"
  - "Physics-informed neural ODE (PINODE): embedding physics into models using collocation points"

The spirit of this work aligns quite well with above two in that both proposes to learn the Koopman generator $L$. The difference lies in that this work is “data-driven” whereas the other two are “physics/equations-driven”.

### Questions
- Page 7, line 358 - 359: "according to Theorem 4.1, we may need more than one layer even for the autonomous systems." -- Indeed, the theorem asserts that "there exists some positive integer $J$", but it doesn't align w/ our understanding for autonomous systems - for which the Koopman operator (or generator) should be time-invariant as defined in section 2.3? Is the statement true? How do you explain the discrepancy?

- Even for non-autonomous systems, do you have suggestions on how to choose $J$ (page 8, line 397-398) and the function $v$ beforehand? Any general guidelines? I can see because we construct the representation space  with the Fourier functions, so we could use sinusoidal functions for representing $v$ for simplicity, etc. But are there deeper reasons for why you choose $v(x,y)$ that way (page 7, line 350)?

- Page 8, 416-417: what's the fundamental reason of seeing eigenvalues distributed on the unit circle in the deep Koopman-layered model? Why EDMD/KDMD failed? Since you are benchmarking against DMD methods on i) non-autonomous system (transient dynamics) and the goal is to ii) find stable eigenvalues, I strongly recommend (NOT required) you to compare against more relevant DMD variants below:
  - "Multi-Resolution Dynamic Mode Decomposition" by J Kutz et al.
  - "Forward-Backward Extended DMD with an Asymptotic Stability Constraint" by Forbes et al.

### Soundness
3

### Presentation
2

### Contribution
3
