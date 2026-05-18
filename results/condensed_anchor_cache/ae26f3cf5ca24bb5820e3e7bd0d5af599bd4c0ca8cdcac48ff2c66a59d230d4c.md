- Decision: Reject
- Scores: 1, 3, 3

## Merged Review

### Summary
The paper proposes a geometric theory of continuous-depth neural networks via homogeneous Ricci flows. It claims that the learned Riemannian metric tensor is a closed-form solution of such flows, and that the network governs Ricci curvature to separate data. Experiments on 2D toy data visualize metric and curvature evolution. There is substantial disagreement: one reviewer (rating 1, high confidence) asserts that the naming “Ricci flow” is incorrect, the method can be reduced to standard Jacobian analysis, and experiments are too limited. Two reviewers (ratings 3) find the geometric perspective promising but note severe presentation issues, unclear theoretical contributions, and insufficient justification for the homogeneous Ricci flow.

### Strengths
- Studying neural networks from a geometric perspective is a promising avenue; leveraging Ricci flows and Ricci solitons is a helpful contribution that could foster more such works (Reviewer 2).
- Visualizations of the underlying tensors are very interesting and display that the theory seems to capture the essence of representation learning (Reviewer 2). Similarly, good illustrations of the evolving process provide a new perspective for the interpretability of neural networks, making the paper novel (Reviewer 3).

### Weaknesses
- [Reviewer 1, high confidence] The naming “Ricci flow” is incorrect/misleading. The evolution is an intrinsic geometric flow parameterized by the neural network, whereas Ricci flow is a prescribed PDE independent of the network. This is a fundamental mischaracterization.
- [Reviewer 1] The method can be simplified considerably: the core is the evolution of the Jacobian \( J \); the pullback metric is the inverse of \( J^T J \), and its evolution follows from \(\frac{d (J^T J)}{dt} = J^T \frac{dJ}{dt} + \frac{dJ}{dt}^T J\). The current approach does not use the known ODE \(\frac{dJ}{dt}\) and instead approximates via step size, making it unnecessarily complex.
- [Reviewer 1] The method has an intrinsic limitation: the Jacobian scales poorly with input/output dimension.
- [Reviewers 1, 3] Experiments are restricted to extremely toy 2D data and only provide visualizations; they convey little beyond “the method can extract something” (Reviewer 1). The paper does not state what theoretical claim the experiments are intended to verify (Reviewer 3).
- [Reviewers 2, 3] The paper is very hard to follow; concepts such as “ad(K)-invariant” are not introduced. The connection to continuous-depth networks is unclear: it is difficult to determine which quantities (manifold, metric, Ricci curvature) are determined by the neural network structure. The layout of Section 3 is far from accessible to a general audience (Reviewer 3). Statements like “There is no doubt that after discretisation, Eq 11 will degenerate into Eq 4” are not obvious (Reviewer 2).
- [Reviewer 2] Why is homogeneous Ricci flow used instead of standard Ricci flow? No justification is given.
- [Reviewer 2] Technical questions about derivations remain unanswered: (1) On page 6, in the definition of Ricci curvature as a Lie derivative, where did the diffeomorphisms \(\phi_V^{\delta t}\) and its pullback go? How are they defined for a neural network? (2) In equation (10), the limit \(\lim_{\delta t \to 0}\) is missing from the right-hand side. In equation (12), the left-hand side depends on \(\delta t\) while the right-hand side does not, and there is no dependence on \(a\) in the product. (3) Where in the theory is the Euclidean output space used explicitly? What would change if another structure were imposed?
- [Reviewers 2, 3] The main theoretical contribution is unclear; no theoretical guarantee is proved in the main article (Reviewer 3). The paper claims theoretical insights but does not present them in a rigorous or well-explained way.