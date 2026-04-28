# Solving Differential Equations with Constrained Learning

- Decision: Accept
- Avg Score: 5.25
- Scores: 3, 8, 5, 5

## Abstract
(Partial) differential equations~(PDEs) are fundamental tools for describing natural phenomena, making their solution crucial in science and engineering. While traditional methods, such as the finite element method, provide reliable solutions, their accuracy is often tied to the use of computationally intensive fine meshes. Moreover, they do not naturally account for measurements or prior solutions, and any change in the problem parameters requires results to be fully recomputed. Neural network-based approaches, such as physics-informed neural networks and neural operators, offer a mesh-free alternative by directly fitting those models to the PDE solution. They can also integrate prior knowledge and tackle entire families of PDEs by simply aggregating additional training losses. Nevertheless, they are highly sensitive to hyperparameters such as collocation points and the weights associated with each loss. This paper addresses these challenges by developing a \emph{science-constrained learning}~(SCL) framework. It demonstrates that finding a (weak)~solution of a PDE is equivalent to solving a constrained learning problem with worst-case losses. This explains the limitations of previous methods that minimize the expected value of aggregated losses. SCL also organically integrates structural constraints~(e.g., invariances) and (partial)~measurements or known solutions. The resulting constrained learning problems can be tackled using a practical algorithm that yields accurate solutions across a variety of PDEs, neural network architectures, and prior knowledge levels without extensive hyperparameter tuning and sometimes even at a lower computational~cost.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper aims to adapt ideas from adversarial robustness and use them to find neural network solutions to partial differential equations with improved guarantees over existing neural solutions to PDEs.  The scheme, as I understand it, is to observe that the weak form of the solution to a PDE can be achieved by finding the minimum of a kind of "worst-case PINN loss" in which the distribution over collocation points is chosen to maximize the expected PINN loss.  This framing allows a particular result from adversarial robustness to apply: the worst-case (wrt distributions on inputs) expected loss on a region can be approximated by an expectation under a distribution proportional to the shifted-and-truncated loss on that region.  The amount of shifting governs the accuracy of the approximation.  I understand this to be a kind of continuity argument: if the worst-case distribution is concentrated on the points with the highest loss, then smoothing those out a bit doesn't change the value all that much.

The result is that you can get a reframing of the weak problem to look sort of like a PINN with a particular distribution on the collocation points.  The paper discusses how various kinds of constraints, e.g., symmetries, can then be framed in this way.  The actual sampling itself of the \psi_\alpha distribution is done with Metropolis-Hastings, or it is discarded in favor of a uniform distribution.  The approach is empirically evaluated on a couple of small problems and compared to some neural network baselines. No comparisons to conventional PDE solvers are performed.

### Strengths
I think the main strength of this paper is that it allows one to reason more formally about the PINN-type setup and connect it directly to the weak form solution.  It's a creative idea to adapt the result from adversarial robustness. The paper is mostly well written.

### Weaknesses
The main weakness of the paper is that we don't get any sense of how well this actually works for solving PDEs.  Like many "deep learning for PDEs" papers, it does not compare to conventional methods for solving PDEs, but only other neural networks.  It is currently unclear whether PINNs and related ideas are actually ever a good idea.  Very few papers examine the actual Pareto curve of computational cost versus accuracy with respect to, e.g., FEM.  A recent paper reviewing the area has shed light on just how bad this situation is from a scientific perspective:

McGreivy, Nick, and Ammar Hakim. "Weak baselines and reporting biases lead to overoptimism in machine learning for fluid-related partial differential equations." Nature Machine Intelligence (2024): 1-14.

The MH24 paper criticizes weak standard numerical baselines, but the present paper does not compare to any conventional numerical methods at all.  Do we conclude from this paper that I should stop using my PDE solver and start using this method?  The abstract claims "accurate solutions" but then only demonstrates that relative to deep learning baselines on tiny problems.

And to be clear, this situation is not really the authors' fault.  They are just following the trend and applying the standard that the neural PDE solver community has created.  Nevertheless, the for the larger scientific community to find this work valuable, we must apply a standard that makes sense for people who want to actually solve PDEs.

So we might instead take the contribution of the paper to be the guarantee, except:

1) As stated in the paper, existing methods already have guarantees.

2) The guarantee itself centers on sampling from \psi_\alpha which, as mentioned in the paper, becomes difficult exactly when the error bound becomes tight.  Using Metropolis--Hastings essentially throws that guarantee away unless you can prove, e.g., uniform ergodicity of the resulting Markov chain. So in the end we are faced with what looks like just another difficult integral, just with a different form and a lack of a guarantee.  Note that one could raise the same criticism of the original adversarial robustness result: sampling from little regions around the worst case inputs is just as difficult as finding them in the first place.

### Questions
What did you use to compute the ground truth solutions?  How long did it take to compute those ground truth solutions relative to the methods compared in the paper?  What I'd like to see here is a thoughtful comparison with conventional methods and points along the Pareto curve trading off compute time against accuracy (here, that means the fineness of discretization for, e.g., FEM).

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper develops a technique called ``Science constrained learning'' in order to address some of the issues with Physics Informed Neural Networks (PINNs) by allowing structural constraints and known solutions to be taken into account in addition to the usual constraints considered by PINNs.

### Strengths
Overall the paper is well written and formatted and the development of Science Constrained Learning (SCL) is well described. There are several different background techniques described in the paper, in addition to the new technique. I think this work is worthy of inclusion in the conference and I am leaning towards an acceptance.

### Weaknesses
There are several different background techniques described in the paper, in addition to the new technique. Therefore, I think it would be beneficial to the readability of the paper to include a clear list of the scientific contributions of SCL to help the reader. I note that the paper is a full 10 pages long, however I think that some of the background could be shortened somewhat (especially in the introductory sections) in order to give the description of the new technique a bit more room to breathe. 

One of the main claims for the new method is that it is not sensitive to the balancing of weights for the different components of the loss function. This is well justified by the use of the dual formulation. However this is not mentioned until the end of the 4th page. Due to the importance of this aspect of the solution, I would recommend mentioning it earlier in the paper. Otherwise the reader is left wondering what the difference is to e.g. the work in [1], which uses derivative constraints and empirical observations. 

The use of the Lagrangian does indeed support the idea that the method addresses the issue of balancing the weights in the loss function which can affect PINNs. However the paper also makes the statement that this new methodology addresses sensitivity to the number of training points. I cannot really see a clear explanation in the paper for why this might be the case. Either this explanation should be brought out more and clarified in the paper or, alternatively, it should be explained that this is an empirical observation.

### Questions
I would be very pleased to hear the authors' response to my comments above, especially with respect to the proof of the reduction in conditioning number in Appendix B.

### Soundness
3

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
Neural network-based approaches, such as physics-informed neural networks and neural operators, offer a mesh-free alternative by directly fitting those models to the PDE solution. They are known to be highly sensitive to hyperparameters such as collocation points and the weights associated with each loss. This paper addresses these challenges by developing a science-constrained learning (SCL) framework. It demonstrates that finding a (weak) solution of a PDE is equivalent to solving a constrained learning problem
with worst-case losses.

### Strengths
The strength of the paper is their proposed solution to the hyperparameter issue:  They develop a science-constrained learning (SCL) framework. It demonstrates that finding a (weak) solution of a PDE is equivalent to solving a constrained learning problem
with worst-case losses.

The paper provides ways of incorporating structural knowledge, observational knowledge, and science-contrained learning.  The algorithm is easy to follow, and the mathematical proofs are helpful in terms of understanding the benefits of the method.

### Weaknesses
The reviewer is having a difficult time distinguishing the contribution from the work of Paris Perdikaris and his group.  Examples are:

A. Daw, J. Bu, S. Wang, P. Perdikaris, A. Karpatne, Rethinking the Importance of Sampling in Physics-informed Neural
Networks, arXiv preprint arXiv:2207.02338

S. Wang, S. Sankaran, P. Perdikaris, Respecting causality is all you need for training physics-informed neural networks,
arXiv preprint arXiv:2203.07404

Paris references in one of his talks a paper by this former advisor and colleagues "A unified scalable framework for causal sweeping strategies for ..." that has a categorization (and references).

The important point is that the algorithm in the current paper (Algorithm 1) has many of the same characteristics you find in Paris' work which you incorporate learning the hyperparameters into the learning.

At some point, the reviewer is wondering how common this is now considered when application papers now reference the constrained paper (NIPS) as say that they use PINNs + Constrained learning:

https://www.sciencedirect.com/science/article/pii/S1385894724012919#b78

Is the current paper really 'novel' (i.e. a contribution) if others now consider things commonplace.  The reviewer is open to being convinced of the contributions if the literature search were broader and the comparisons where against the various adaptive sampling methods mentioned by Paris and others.

In terms of concrete actions, can the authors:
+  Provide a more comprehensive literature review that clearly positions their work relative to existing constrained learning approaches for PINNs?

+  Explicitly discuss how their method differs from or improves upon other adaptive sampling techniques, particularly those by Perdikaris and others (as highlighted by the question below)?

+ Highlight any novel theoretical results or empirical improvements over state-of-the-art methods

### Questions
The specific questions (associated with the items above) are:

+ Can the authors clarify how their approach (for instance Algorithm 1 updating schedule) compares to the update schedule in Paris' paper:   https://epubs.siam.org/doi/pdf/10.1137/20M1318043    Section 2.4 (not the specific updates, but the general updates as given by the spirit of the logic presented)?  In others of Paris' papers, he points to :   https://arxiv.org/pdf/2007.04542.  How does the new method compare to the "adding weights to the loss function" section 2.2.1 (Which is analogous to Paris' work also)?

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
3

### Summary
This paper developed SCL, a technique for solving BVPs based on constrained learning. 
It then developed a practical algorithm to tackle these problems and showcased its performance across a variety of PDEs.
SCL not only yields accurate BVP solutions, but tackles many of the challenges faced by previous methods, such as extensive hyperparameter tuning and computational costs.

### Strengths
- The authors tackle important problems in physics-informed learning: reducing computational costs and avoiding hyperparameter tuning.

- The experimental results show that the proposed formulation outperforms baselines in some cases.

### Weaknesses
 - The key contribution, Algorithm 1, can be seen as a variant of DNN training with learnable loss weights, which can often be found in multi-task learning, lacking novelty.

- The dependence on random seeds is unknown, potentially causing reproducibility issues. Error bars should be added.

- The paper is difficult to follow. The paper benefits from paragraph writing, and please present information in relevant paragraphs and sections. It was challenging to discern whether certain sentences conveyed key ideas or were merely supplementary notes.

- I have several critical questions. Please see Questions below. I am open to discussion.

- (Minor) (Lines 1730, 1733, etc.) Fig -> Fig.

### Questions
- The proposed formulation seems to be a rephrasing of PDE boundary value problems with invariance, observation data into a single constraint problem. The resulting Lagrangian problem is then solved straightforwardly in Algorithm 1, reminiscent of standard multi-task learning algorithms. Is there more to it than this? 

- (Lines 214-) "Compared to penalty methods, (Dˆ -CSL) does not require extensive tuning of coefficients [such as μ in (PI)] and guarantees generalization individually for each constraint (near-optimality and near-feasibility) rather than for their aggregated value.": Could you elaborate on this? It seems to be a key statement regarding the paper's contribution. Could you provide some references to support this?

- (Lines 58-) "Instead, we use semi-infinite constrained learning techniques to develop a hybrid sampling-optimization algorithm that tackles both problems jointly without extensive hyperparameter tuning and training heuristics (Sec. 4).":  I am not fully convinced by this claim. Algorithm 1 still includes hyperparameters, such as $\eta_p$ and $\eta_d$, and training heuristics are still necessary.

- (Lines 472-) "it (causality) arises naturally by solving (SCL′)(M). As training advances, however, Alg. 1 shifts focus to fitting higher convection speeds β. Note that this occurs without any prior knowledge of the problems or manual tuning.": Could you clarify why causality naturally arises in this context?

- Under what conditions, does Algorithm 1 converge?  (Chamon et al., 2023; Elenter et al., 2024) could be valuable references, to my understanding.

### Soundness
2

### Presentation
2

### Contribution
2
