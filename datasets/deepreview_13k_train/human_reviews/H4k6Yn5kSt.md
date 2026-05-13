# Exponential-Wrapped Mechanisms for Differential Privacy on Hadamard Manifolds

- Decision: Reject
- Scores: 6, 6, 5, 8, 6

## Abstract
We extend the Differential Privacy (DP) framework to Hadamard manifolds, the class of complete and simply connected Riemannian manifolds with non-positive sectional curvature. Inspired by the Cartan–Hadamard theorem, we introduce Exponential-Wrapped Laplace and Gaussian mechanisms to achieve $\varepsilon$-DP, $(\varepsilon, \delta)$-DP, Gaussian DP (GDP), and R\'enyi DP (RDP) on these manifolds. Our approach employs efficient, straightforward algorithms that circumvent the computationally intensity Monte Carlo Markov Chain (MCMC) methods.  This work is the first to extend $(\varepsilon, \delta)$-DP, GDP, and RDP to Hadamard manifolds. We further demonstrate the effectiveness of our methodology through simulations on the space of Symmetric Positive Definite Matrices, a frequently used Hadamard manifold in statistics. Our findings reveal that our Exponential-Wrapped mechanisms surpass traditional MCMC-based approaches, which require careful tuning and extensive diagnostics, in both performance and ease of use. Additionally, our methods achieve comparable utility to the Riemannian Laplace mechanism with enhanced utility for smaller privacy budgets ($\varepsilon$) and operate orders of magnitude faster computationally.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper extends the Differential Privacy framework to the class of complete and simply connected Riemannian manifolds - Hadamard manifolds. The major contributions are the first extension of Laplace and Gaussian mechanisms that could achieve DP, GDP and RDP on these manifolds. The new method is named Exponential-Wrapped mechanism in the sense that they are deducted through the Exponential Mapping  and their push forward functions. The approach gives efficient, straightforward algorithms comparable to the vanilla mechanisms in Euclidean space. We further demonstrate the effectiveness of our methodology through simulations on the space of Symmetric Positive Definite Matrices, a frequently used Hadamard manifold in statistics. In numerical experiments, the Exponential-Wrapped mechanisms beat traditional MCMC-based approaches in efficiency and achieve comparable utility to the Riemannian Laplace mechanism with enhanced utility.

### Strengths
The paper gives the first extension of the common Laplace and Gaussian mechanisms in the context of more generalized Riemannian Geometry settings than the common multi-dimensional Euclidean space setting, so in that sense the contribution's importance and its novelty are both straight-forward.

Although the formulation becomes more intricate, the steps that the authors took to develop these mechanisms seem well-established to me.

I'm not very familiar with the exact applications of such geometric settings, but judging from my limited knowledge the findings could be useful.

### Weaknesses
To me the major issue is the writing of the paper. It could be that my geometry is simply rusty, but I'm not sure how familiar the general community for this venue are with the math concepts used in this paper. In light of that, I think this paper sort of takes it for granted that people know all these things (such as Exponential mapping, push-forward, etc.) already. I find the preliminary section to be unsatisfying and insufficient of the crucial math concepts used later in the deduction of the mechanisms in general. My (biased) opinion is that some of these things deserve more explanation before we go deeper into the weeds.

I was also slightly surprised that when $\varepsilon$ is about [0.2, 0.6], the benchmark algorithm performs better than the proposed algorithm. I think in Euclidean spaces at least for pure DP the Laplace mechanism should be pretty close to being optimal for such small $\varepsilon$ values?

There isn't much theoretical characterization of how good such generalization mechanisms are, even in the pure DP case. But perhaps that's because the community simply don't know much in this more complicated context.

### Questions
Do you have any insights into if there could be similar extensions for other traditional mechanisms such as the K-norm mechanism (Laplace is a special case of K-norm using the $\ell_1$-norm)?

I'm not very familiar with Riemannian Geometry and Manifolds, to me it is surprising that the extended version of Laplace has additional parameter $p_0$ (the footprint) compared to the Euclidean space version. I thought the Hardamard Manifold is basically a warped version of Euclidean space, but then in principle why do we need to use an additional $p_0$ to define the Laplace Mechanism? To help the understanding, can the authors recast the results back into Euclidean space and show the value of all these parameters given $\epsilon$ for pure DP budget?

Minor:

In line 108 the sentence seems incomplete: "There exists a unique [???] starting from..."

The notion $p_0$ abruptly appeared in line 188.

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
2

### Summary
This paper proposed DP and approximate DP mechanisms when the function f that we want to privatize falls into a Hadamard Manifold. In particular, the paper proposed to use Exponential-Wrapped Laplace Mechanism to achieve eps-DP and Exponential-Wrapped Gaussian Mechanism to achieve (eps,delta)-DP.

### Strengths
The paper proposed simple and clean DP mechanisms when the value function falls into the Hadamard Manifold. Simulation results also show good privacy / accuracy tradeoffs.

### Weaknesses
From a technical point of view, the biggest concern is that the paper made a strong assumption that the values of the function fall into a manifold with good properties. With these properties, one can directly apply sampling techniques via Exponential-Wrapped Probability to achieve DP or approximate DP. The techniques become a bit straight-forward.

The simulation is only for synthetic data, it is not clear whether there are any real use cases / problems that fall in the case that value functions are in such a good manifold.

### Questions
Are there any practical problems in the real world such that the values have fallen into Hadamard Manifolds?

### Soundness
2

### Presentation
2

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
The paper proposes a method to extend Differentially Private mechanisms designed for Euclidean space to general Riemannian manifolds with non-negative sectional curvature, aka. Hadamard manifolds. The general idea is to use the Cartan-Hadamard theorem which says that for Hadamard manifolds, a universal cover (a map between two topological spaces) is diffeomorphic (i.e., bijective or invertible) to Euclidean space via the exponential map at any point. This exponential map on a Riemannian manifold is a way to "unroll" a point's local geometry, letting us move along geodesics (the "straightest" paths) from that point in the manifold, like traveling in a direction on a curved surface as if it were flat. Thanks to the invertibility of this exponential map, the paper proposes a straightforward way to perturb points in the Hadamard manifold to satisfy differential privacy, which they call *Exponential-wrapping* --- 1) first, map the point in the manifold to the Euclidean space using the inverse of the exponential map, 2) apply a well-known mechanism like Gaussian or Laplace, then 3) invert the noisy point back to the Hadamard manifold using the exponential map. The authors argue that this style of noise sampling is computationally efficient compared to other methods in literature that rely on MCMC methods. Additionally, the paper also provides a utility analysis for DP Frechet mean computed using their proposed exponentially-wrapped Gaussian and Laplace mechanisms. A simulation comparing prior MCMC methods with proposed mechanisms for DP Frechet mean is also presented.

### Strengths
- The proposed approach for randomizing outcomes in Hadamard manifolds is quite elegant and possibly easily extensible to other DP mechanisms.
- The paper provides utility analysis for the proposed mechanism.
- There's a clear computational advantage of the proposed mechanisms.
- The proposed exponentially-wrapped Gaussian mechanism could be useful in privatizing outcomes in high-dimensional manifolds.

### Weaknesses
 - The main drawback of this approach is the cost that seems to be associated with the choice of the footpoint around which the mechanism is wrapped. More specifically, in equation (2) and (3), the utility for Frechet mean via the proposed mechanisms is closely tied to the choice of footpoint $p_0$ chosen on the manifold. Even when $p_0$ is set to be the center $m$ of the ball $B_r(m)$ in which all data-points lie, the utility upper bound is as high as $r$, which is of the same order as a random guess within the ball. This seems to be true for both the proposed EW Gaussian and EW Laplace mechanisms.
- Authors mention that the footpoint $p_0$ for their proposed mechanisms must be selected *a priori* without looking at the data. But, it isn't obvious to me why this footpoint can't be data-dependent. I suspect the utility of the mechanisms can significantly improve if some of the privacy budget is spent to privately determine a good footpoint for the mechanism first.
- Unlike Gaussian mechanism whose utility guarantee remains dimension independent, it's exponentially-wrapped counterpart proposed seem to be somehow dependent in the dimension size (eqn. (3)). I'm not certain if this dependence helps or hurts when dimension $d$ is large. The utility bound in equation (3) involves a confluent hypergeometric function which depends on the distance between the footpoint and the Frechet mean, as well as the dimension $d$. This dependence makes it difficult to analyze the utility in high dimensions since the behavior of the hypergeometric function is not always intuitive. It's unclear if this dependence is better or worse than the standard Gaussian mechanism's linear dependence on dimension.
- The simulation results suggest that Riemannian Laplace mechanism proposed in the prior works performs better than this paper's EW Laplace in higher dimensions or in reasonable privacy regimes (1 > eps > 0.5). In lines 415-417, the authors acknowledge that this is expected as the utility advantage of their mechanism are reserved for non-homogeneous manifolds. Most manifolds we see in practice however are homogeneous---spheres, Torus, Grassmannian, etc.

### Questions
- If the selected footpoint is kept secret, only revealing the final perturbed result in the manifold, will there be a higher privacy risk if the choice of footpoint is influenced by the data? Could the authors give an example to help me see why the design of their mechanism fixes $p_0$ a-priori was necessary as opposed to setting $p_0$ to be the same as the unperturbed outcome?
- Could the authors describe the technical reason behind the dependence on dimension size for the EW-Gaussian mechanism in equation (3)? In lines 417-419, authors mention something about the volume distortions being more pronounced in higher dimensions, but I don't quite understand the magnitude of such distortions. Can they be avoided?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces novel mechanisms for achieving differential privacy on Hadamard manifolds using exponential-wrapped distributions. The authors extend multiple variations of differential privacy (DP) - including (ε,δ)-DP, Gaussian DP (GDP), and Rényi DP (RDP) - to Hadamard manifolds for the first time. The key innovation is using exponential-wrapped Laplace and Gaussian distributions to create mechanisms that are both theoretically sound and computationally efficient, avoiding the need for complex MCMC sampling methods used in previous approaches. The paper provides theoretical guarantees for privacy and utility, along with empirical validation on the space of Symmetric Positive Definite Matrices (SPDM).

### Strengths
* Novel Theoretical Contributions: First work to extend (ε,δ)-DP, GDP, and RDP to Hadamard manifolds in a unified framework. This significantly broadens the applicability of differential privacy to non-linear data.

* Computational Efficiency: The proposed exponential-wrapped mechanisms avoid computationally intensive MCMC methods, making them much more practical for real-world applications. The sampling procedures are straightforward and efficient.

* Improved Performance: The mechanisms show better utility than previous approaches, especially for small privacy budgets (ε). The Exponential-Wrapped Laplace mechanism requires only ∆/ε rate compared to 2∆/ε for nonhomogeneous manifolds in previous work.

### Weaknesses
Paper only uses the SPD manifold in experiments, but it would benefit from a more extensive empirical evaluation across different types of Hadamard manifolds and real-world applications. My main suggestion would be to extend the experiments to Hyperbolic spaces, which have a ton of interesting applications.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper extends the framework of Differential Privacy (DP) to Hadamard manifolds, a class of complete and simply connected Riemannian manifolds with non-positive sectional curvature. Inspired by the Cartan–Hadamard theorem, the authors introduce Exponential-Wrapped Laplace and Gaussian mechanisms to achieve ε-DP, (ε, δ)-DP, Gaussian DP (GDP), and Rényi DP (RDP) on these manifolds. Unlike traditional methods that rely on computationally intensive Monte Carlo Markov Chain (MCMC) techniques, their approach uses efficient algorithms that bypass these processes. This work is claimed to be the first to extend (ε, δ)-DP, GDP, and RDP to Hadamard manifolds.

The effectiveness of their method is demonstrated through simulations on the space of Symmetric Positive Definite Matrices (SPDM), a frequently used Hadamard manifold in statistics. The results show that the proposed Exponential-Wrapped mechanisms surpass traditional MCMC-based methods in both performance and ease of implementation, especially in scenarios requiring small privacy budgets (ε). Moreover, their approach achieves comparable utility to the Riemannian Laplace mechanism while operating at significantly faster computational speeds.

The paper concludes by suggesting possible future research directions, including extending differential privacy to manifolds with non-negative curvature and applying the methods to more complex tasks such as principal geodesic analysis and regression on manifolds.

### Strengths
The paper is the first to extend $(\epsilon, \delta)$-DP, GDP, and RDP to Hadamard Riemannian manifolds through the introduction of Exponential-Wrapped Laplace and Gaussian mechanisms. This extension broadens the scope of privacy frameworks to general manifold settings.

The authors develop fast and efficient implementations of these mechanisms, avoiding computationally intensive MCMC sampling methods. This makes the proposed methods more feasible and applicable in real-world scenarios where computational efficiency is crucial.

Through comprehensive numerical experiments, the paper demonstrates that the proposed mechanisms perform comparably to the traditional Riemannian Laplace mechanism. Notably, when achieving GDP, the Exponential-Wrapped Gaussian mechanism exhibits superior performance, especially in scenarios with small privacy budgets.

### Weaknesses
The paper lacks comparison with previous results. There is no clear comparison within the sections to evaluate the proposed method against existing methods, making it difficult for readers to assess whether the proposed approach truly represents an improvement. Additionally, too many parameters and concepts are introduced, with overly exotic ideas seemingly added to elevate the paper's complexity. The authors may have introduced unnecessary complexity to attract readers’ attention. The practical applications are limited, only valid on Hadamard manifolds. This does not differ significantly from cases on $\mathbb{R}^n$ but has greater limitations. After all, when do people operate in a space of negative curvature?

### Questions
Could the authors provide specific examples? Also, what is the motivation for considering Hadamard manifolds in this paper? What considerations led the authors to naturally introduce Hadamard manifolds into differential privacy? Additionally, is this related to the stronger divergence of the Laplace mechanism and the better behavior of its solution, such as better convergence of its inverse? If you can address the above questions, I will consider adjusting the score accordingly.

### Soundness
3

### Presentation
2

### Contribution
3
