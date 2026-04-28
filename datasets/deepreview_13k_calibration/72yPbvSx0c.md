# Koopman Embedded Equivariant Control

- Decision: Reject
- Avg Score: 4.50
- Scores: 6, 3, 6, 3

## Abstract
An efficient way to control systems with unknown nonlinear dynamics is to find an appropriate embedding or representation for simplified approximation (e.g. linearization), which facilitates system identification and control synthesis. Nevertheless, there has been a lack of embedding methods that can guarantee (i) embedding the dynamical system comprehensively, including the vector fields (ODE form) of the dynamics, and (ii) preserving the consistency of control effect between the original and latent space. To address these challenges, we propose Koopman Embedded Equivariant Control (KEEC) to learn an embedding of the states and vector fields such that a Koopman operator is approximated as the latent dynamics. Due to the Koopman operator's linearity, learning the latent vector fields of the dynamics becomes simply solving linear equations. Thus in KEEC, the analytical form of the greedy control policy, which is dependent on the learned differential information of the dynamics and value function, is also simplified. Meanwhile, KEEC preserves the effectiveness of the control policy in the latent space by preserving the metric in two spaces. Our algorithm achieves superior performances in the experiments conducted on various control domains, including the image-based Pendulum, Lorenz-63 and the wave equation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a method for solving control problems called Koopman embedded equivariant control (KEEC). The key idea of the paper is that the state of the dynamics in mapped into a latent space via an embedding. In KEEC, the embedding is a learned function, trained to satisfy equivariance and isometry properties. The optimal policy is then learned in latent space using Hamiltonian-Jacobi-Bellman. KEEC is compared to other methods in numerical experiments.

### Strengths
* As far as I am aware, the paper is novel in its way of learning a latent embedding and applying Koopman operator theory for control systems.
* The paper has detailed descriptions of the theory, with more information available in the appendix. 
* The high-dimensional control problem is reduced to a minimization problem with an analytic solution in equations (8-9).
* The paper considers enforcing contraints to satisfy equivariance and isometry properties. 
* The method is tested on multiple control systems against multiple methods are shows superior performence.
* The experiments are detailed, including how each problem is setup, and comparisons of rewards, computation time and stability.

### Weaknesses
 * There is some confusion regarding the theory, particularly regarding the operator $\mathcal{P}$. Please see questions.
* There is no justification for Lemma 3.3.
* While KEEC is faster than MPC and MPPI, it is slower than standard RL methods such as SAC and CQL.
* The page limit was exceeded.

### Questions
* In equation (3), what are the values taken by $\tau$ in the sum? Is it at discrete time points?
* In figure 3(d-e) the magnitude of $\lambda_{met}$ is between 32 and 256 and the latent dimension is between 0.1 and 1.0. Should this be switched?
* Is the infinitesimal generator $\mathcal{P}$ an infinite or finite dimensional operator? The Koopman operator $\mathcal{K}$ is an infinite-dimensional operator and $\mathcal{K} = exp(\mathcal{P})$, so the generator should be infinite-dimensional. However, in equations (6-8), $\mathcal{P}$ seems to be a finite-dimensional matrix.
* The KEEC model architecture is given in Table 3. What architectures are used for the comparison methods (SAC, CQL, etc.)? It would be good to compare the number of parameters needed for each.

### Soundness
2

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
4

### Summary
A framework for controlling (via learning value function) nonlinear dynamics is proposed. It is based on embedding the state into a latent space where the dynamics are linear and represented by the Koopman generator. To embed the states a pair of an encoder and a decoder is learned, for which the loss function is based not only on the reconstruction/prediction error (which the authors refer to as the equivariance loss) but also on the regularizer to preserve the metric between the original and the latent spaces. The utility of the proposed method is shown with multiple control problems.

### Strengths
- The method looks technically reasonable. Embedding the state into a space where the dynamics can be linearized is indeed useful sometimes and can be explained using the notion of the Koopman operator.
The experiment is done with multiple baseline methods, multiple systems, and some ablation studies.

### Weaknesses
(1)
It is unclear which aspects of the method should be evaluated in terms of novelty. Using the Koopman generator instead of the discrete-time Koopman operator for learning is not certainly the most common setting, but the difference between the continuous- and discrete-time settings here does not seem to bring significant technical difficulty. The "isometry loss" looks somewhat new (though I feel I saw something similar in the same context which I can't remember), but I am not sure if this regularizer solely makes a notable contribution as an ICLR paper. As for the optimal control (or value function learning) part, it is unclear which part should be considered as a particular contribution of the paper.

(2)
As mentioned above, learning neural network observables for embedding dynamics state has been widely studied, not only by Li et al. ICLR 2020 (which the authors have cited), but also by many other researchers. Even limiting the scope to the problems with control inputs, I can raise examples as follows:
- J. Morton, A. Jameson, M. J. Kochenderfer, F. Witherden: Deep dynamical modeling and control of unsteady fluid flows, Advances in Neural Information Processing Systems 31, 2018, pp. 9258–9268
- J. Morton, F. D. Witherden, M. J. Kochenderfer: Deep variational Koopman models: Inferring Koopman observations for uncertainty-aware dynamics modeling and control, Proceedings of the 28th International Joint Conference on Artificial Intelligence, 2019, pp. 3173–3179
- M. Bonnert, U. Konigorski: Estimating Koopman invariant subspaces of excited systems using artificial neural networks, IFAC-PapersOnLine, vol. 53, no. 2, pp. 1156–1162, 2020
- M. Han, J. Euler-Rolle, R. K. Katzschmann: DeSKO: Stability-assured robust control with a deep stochastic Koopman operator, Proceedings of the 10th International Conference on Learning Representations, 2022
- Y. Guo, M. Korda, I. G. Kevrekidis, Q. Li: Learning parametric Koopman decompositions for prediction and control. arXiv:2310.01124
- D. Uchida, K. Duraisamy: Extracting Koopman operators for prediction and control of non-linear dynamics using two-stage learning and oblique projections. arXiv:2308.13051
- M. Wang, X. Lou, B. Cui: Deep bilinear Koopman realization for dynamics modeling and predictive control, International Journal of Machine Learning and Cybernetics, 2024

Making the relation to, not necessarily all, but at least some of the most relevant ones would be beneficial for making the context of the research clearer.

(3) Although the authors claim that the proposed method is different from previous methods in terms of the treatment of the vector field (Lines 90-91), there seems to be no direct empirical comparison from this perspective. E2C may be the most relevant of the examined baselines but is not necessarily a valid reference to investigate the particular advantage of the proposed method. Elaborating more on this point would be helpful.

### Questions
Point (3) in the Weaknesses section is the most meaningful to me as a question --- how would you justify the advantage of using the Koopman generator (instead of the discrete-time operator)? For example, comparison to a variant of the proposed method constructed with a discrete-time setting would be helpful if any.

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
2

### Summary
The paper proposes learning Koopman embedding for the vector field while preserving the consistency of the control effect.

### Strengths
The paper provides strong theoretical results and numerical analysis.

### Weaknesses
1.	What is the drawback of traditional Koopman-based analysis? Why do we need to introduce the learning framework?

2.	Please do a proofreading for all notations and equations. For example, in Line 187-188, there is no z_t. Why do you need to define it? What is $\mathcal{U}$ in Eq. (6)?

3.	In Section 2 and 3, you may also mention what the past method did. For example, how did it learn $\mathcal{K}$? This helps the reader to understand your contribution.

4.	The defined equivariance/isometry losses are quite similar to some existing work, such as “DeepMDP: Learning Continuous Latent Space Models for Representation Learning” . Please do a comparison.

5.	Please clearly state your assumptions and scopes. For example, the analytical framework is based on the control-affine system in Eq. (1). So, the author must state the application domains.

6.	In Fig. 3 (d) and (2), the x-axis doesn’t match the caption. Try to check all figures.

7.	Is the computation time in Fig. 3 training or testing time? You may need to compare both.

### Questions
Q1. Please proofread for notations and figures. See my Weakness points 2, 6.

Q2. Give better motivations for readers to know your contributions. See my Weakness points 1, 3, 4.

Q3. Please clearly state your assumptions and scopes. See my Weakness point 5.

Q4. Is the computation time in Fig. 3 training or testing time? You may need to compare both.

### Soundness
3

### Presentation
3

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
The paper proposed a data-driven modeling and control framework that consists of (1) dynamics model based on the Koopman formalism, and (2) reinforcement-learning-based control using the Koopman model.  The framework is demonstrated on three examples, with benchmark against several methods in the literature.  The claimed novelties include: (1) the introduction of equivariance and consistency requirements in the learning of Koopman dynamics, and (2) simplified RL control policy leveraging the linearity in Koopman dynamics.

### Strengths
In Koopman-based modeling, the introduction of metric consistency, in the form of isometry loss, seems a novel contribution, and the ablation study on isometry loss shows some seemingly favorable effects of this loss.
A semi-analytical optimal policy is derived based on the Koopman model, which leverages the relatively simple form of the latter.  (This reviewer calls it semi-analytical, as the value function still needs to be learned from data.)

### Weaknesses
1. In Koopman-based modeling, the notion of equivariance, and the corresponding loss, is claimed as a novel contribution.  However, this reviewer considers the so-called equivariance requirement as the basic requirement that the community of data-driven modeling of dynamical systems practices on a daily basis.  The equivariance loss thus derived is also a standard loss used in Koopman community, see e.g. [1].
2. The use of Koopman formalism and the derivation of the (bi)linear model, Eq. (6) is not new at all.  See the comprehensive work in [2], which also covers the optimal control based on Koopman model.  The authors seem unaware of this work.  Furthermore, in the derivation of the Koopman dynamics, the authors directly replaced the linear operators P and U by matrices.  However, operators may admit point, continuous and residue spectra (which is the case for pendulum and Lorenz-63), but matrices only admit point spectrum.  There is no rigorous treatment on when such replacement is possible.  In fact, the treatment of continuous spectrum is one of the current bottlenecks in Koopman community (as this reviewer's opinion).
3. Four "baselines" are chosen, but this reviewer is unsure whether these are fair comparisons.  The baselines are all different versions of "novel" learning-based control methods, but the first question to ask is whether the proposed method can out-perform standard methods, such as Koopman model + optimization-based MPC (not MPPI), which has been demonstrated to be effective on hardware in real-time (see [1]).  Furthermore, in the third example, the wave equation is linear, so it admits a linear state-space model, which one can identify from data using standard system identification methods; such linear model can be controlled by LQR method.  Can the proposed method out-perform such baseline?
4. Some portions of the manuscript are unclear, and some are even erroneous.  See Questions below.
5. Some portions of the manuscript only provide standard or well-known results, which this reviewer is not sure whether these add any information to the paper.  Particularly, these include (1) Algorithm 1 that shows standard procedures for training models and learning value functions, and (2) Appendices B, D, F.1, and G.

### Questions
1. It appears Fig. 3d and 3e are swapped.  Also, in the ablation for isometry loss, please provide the reward for lambda_met=0, so the effect of isometric loss is clearer.
2. Line 511, it is unclear what "optimal state became unobservable" means.  It needs clearer definition and better quantification.
3. There are plenty typos in Appendix F leading to the doubt of this reviewer that whether the proofs of the "main theorems" have been carefully constructed.  In particular, Line 1163, is there an extra \gamma in front of \nabla?  Line 1172 missing bracket "("?  Lines 1172-1176, unclear where Eq. (34) is used.
4. Line 1472, What do authors mean by "two strange attractors"?
5. How is the wave equation solved?
6. Table 2 shows that noise is added to the wave equation, but not others.  Why is so?  How sensitive is KEEC to noise in the other cases?
7. MPPI and PCC use significantly shorter horizons than KEEC.  What if the former two use the same longer horizon, or have KEEC using the shorter horizon?
8. Line 155, what do the authors mean by "didn't comprehensively map the vector field ..."?

### Soundness
2

### Presentation
2

### Contribution
2
