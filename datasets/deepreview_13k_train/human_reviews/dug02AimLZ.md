# Second-Order Algorithms for Finding Local Nash Equilibria in Zero-Sum Games

- Decision: Reject
- Scores: 8, 6, 5, 6

## Abstract
Zero-sum games arise in a wide variety of problems, including robust optimization and adversarial learning. However, algorithms deployed for finding a local Nash equilibrium in these games often converge to non-Nash stationary points. This highlights a key challenge: for any algorithm, the stability properties of its underlying dynamical system can cause non-Nash points to be potential attractors. To overcome this challenge, algorithms must account for subtleties involving the curvatures of players' costs. To this end, we leverage dynamical system theory and develop a second-order algorithm for finding a local Nash equilibrium in the smooth, possibly nonconvex-nonconcave, zero-sum game setting. First, we prove that this novel method guarantees convergence to only local Nash equilibria with a local \textit{linear} convergence rate. We then interpret a version of this method as a modified Gauss-Newton algorithm with local \textit{superlinear} convergence to the neighborhood of a point that satisfies first-order local Nash equilibrium conditions. In comparison, current related state-of-the-art methods do not offer convergence rate guarantees. Furthermore, we show that this approach naturally generalizes to settings with convex and potentially coupled constraints while retaining earlier guarantees of convergence to only local (generalized) Nash equilibria.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors design a (family of) second-order algorithms for two-player zero-sum games with the property that, if convergence is achieved, the point of convergence is proved to be a local Nash equilibrium. In particular, such a point of convergence must be a locally asymptotically stable equilibrium.

### Strengths
It's noteworthy that the authors developed an entire family of algorithms for, both, unconstrained and constrained spaces.

### Weaknesses
1. An obvious weakness is that the suggested algorithms are applicable only to two-player zero-sum games. Could they be modified to support multi-player games?
2. Assumptions 1, 2,  and 4 seem reasonable. I am not quite sure how common Assumption 3 is. I understand that the authors consider the relaxation of Assumption 3 as future work. Could they provide some possible intuition? For example, is their natural subclass of two-player zero-sum games that this assumption is satisfied?

### Questions
Kindly refer to the weaknesses.

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
One of the fundamental problems in algorithmic game theory area is learning algorithms for games. In this paper, the authors study a problem related to this area, particularly an unconstrained two-player zero-sum game with an objective function that can be nonconvex-nonconcave. 

In this direction they study algorithms for convergence to local Nash equilibria taking into account the second order conditions of the function. To do that they propose a dynamical systems approach s.t. under specific assumptions the critical points are also local Nash equilibria to the initial game. They prove that their initial dynamics converges with local linear rate of convergence to a local strict Nash equilibrium and they give an improved algorithm of them with super linear local rate of convergence. Finally, they give an algorithm for the constrained setting based on an Euclidean projection approach to converge to a local generalized Nash equilibrium and experiments to give evidence for their approach.

### Strengths
I think that the problem that the authors study is significant and this paper gives new directions to understand it. Their results are good since they give new dynamics and prove local rate of convergence using techniques such as bounding by strictly less than 1 the eigenvalues of the Jacobian matrix. Furthermore, the idea to find a dynamical system s.t. any LASE is a local Nash equilibrium of the initial game is nice.

### Weaknesses
The results hold under specific assumptions and they only guarantee local convergence. I think the paper needs more elaboration how strict are these assumptions and for the latter how far the initial point should be at most from the LASE point in order to have convergence. Specifically, the assumptions, while perhaps standard in some literature, need a more thorough discussion of their implications for the practical applicability of the proposed algorithms. For example, it's not clear how restrictive the requirement for the existence of a dynamical system where critical points correspond to local Nash equilibria is. Furthermore, the local convergence guarantee is a significant limitation, as it does not provide any insight into the behavior of the algorithms when initialized far from a local strict Nash equilibrium. The paper should also discuss the potential for the algorithms to converge to different local Nash equilibria depending on the initialization, and how this might affect the outcome in practice.

### Questions
Does the assumptions imply unique LASE point? 
Is there any assumption on the uniqueness of the local strict Nash equilibrium?
How far should the initial point be at most from the LASE point in order to have convergence?
Do the proven rates of convergence of the unconstrained case hold in the constrained case?

### Soundness
3

### Presentation
2

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
This paper tackles the problem of achieving convergence to local Nash equilibria in two-player zero-sum games. While first-order optimization methods struggle with nonconvex-nonconcave settings and often lead to non-Nash equilibria or unstable cycles, this work addresses these challenges by developing algorithms that leverage second-order information to improve stability and convergence specifically towards local Nash equilibria. The author shows that the algorithm achieves local linear convergence and proposes an advanced version enabling superlinear convergence.

### Strengths
* The algorithm leverages second-order dynamics to achieve higher convergence rates and avoid common pitfalls like oscillations around equilibrium points.
* The authors validate their approach on a GAN training task, demonstrating the algorithms' robustness and practical utility in adversarial machine learning settings.

### Weaknesses
 * The explanation of assumptions in Section 3.1 is weak, and the example in the numerical experiment does not satisfy Assumption 3.
* The author does not claim the technique contribution.



### Questions
* Theorem 2 does not provide a convergence analysis, is there any technique difficulty?
* It would be better if the author conducts a numerical experiment on a model that satisfies all the assumptions in Section 3.

### Soundness
2

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
The paper considers nonconvex-nonconcave zero-sum games. It provides an algorithm with a local convergence guarantee and (local) linear convergence rate. Further, a variant of that method attains local superlinear convergence to a point that satisfies the first-order Nash equilibrium conditions. Finally, the approach is generalized to handle constraints.

### Strengths
The paper considers a well-motivated problem that has attracted much attention in recent years. Compared to prior work that focused on local convergence to Nash equilibria in nonconvex-nonconcave min-max optimization, the paper derives explicit rates of convergence, and also addresses the constrained setting as well. I believe that both of those contributions are important. The authors also support their theory by conducting several experiments, showing that the proposed method outperforms quite convincingly the two most related algorithms (LSS and CESP). Moreover, the paper employs interest techniques, mostly relying on dynamical system theory. Although most of those techniques are standard in this area, the way they are combined in this paper appears to be new. The writing overall is of high quality, and the authors do a good job at explaining the key ideas in the main body. The most related papers have been cited, although I would suggest including a more detailed discussion about the paper of Daskalakis et al. (2023) since it is strongly related. All claims appear to be sound.

### Weaknesses
The paper has several weaknesses, some of which are in some sense insurmountable. First, the proposed method relies on second-order information, which could limit its practical applicability. Computing and storing the Hessian, or even approximating it, can be computationally expensive, especially for high-dimensional problems, making the method less suitable for large-scale applications. Perhaps more importantly, the main result only establishes local convergence. It is unclear whether a local convergence guarantee is a strong enough solution concept. The paper of Daskalakis et al. (2023) provides a global convergence guarantee, but the latter comes without a rate of convergence. At the same time, I believe that computing local Nash equilibria in this setting is intractable (at least in the constrained setting), and so this perhaps justify focusing on local convergence. Regarding the assumptions made in the paper, Assumption 3 seems very artificial and hard to parse. The condition that $J(z_k)^\top \omega(z_k)$ must not be $0$ when $\omega(z_k) \neq 0$ is not intuitive and lacks clear motivation. It is not clear under what conditions this assumption would hold in practice. Can the authors elaborate more on what that assumption entails? And why is it a reasonable assumption? Assumption 2 also seems somewhat artificial, but at least its role is quite clear. I believe that the main body should discuss in more detail some of those assumptions.

### Questions
Besides the question above about the underlying assumptions, is it assumed that the set of constraints has a nonempty interior? For example, what if we are dealing with the probability simplex, which has empty interior? It doesn't seem that the definitions and the approach can handle that case.

### Soundness
3

### Presentation
3

### Contribution
3
