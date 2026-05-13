# RNNS with gracefully degrading continuous attractors

- Decision: Reject
- Scores: 5, 5, 5, 3

## Abstract
Attractor networks are essential theoretical components in recurrent networks for memory, learning, and computation.
However, the continuous attractors that are essential for continuous-valued memory suffer from structural instability---infinitesimal changes in the parameters can destroy the continuous attractor.
Moreover, the perturbed system's dynamics can exhibit divergent behavior with associated exploding gradients.
This poses a question about the utility of continuous attractors for systems that learn using gradient signals.
To address this issue, we use Fenichel's persistence theorem from dynamical systems theory to show that bounded attractors are stable in the sense that all perturbations maintain the stability.
This ensures that if there is a restorative learning signal, there will be no exploding gradients for any length of time for backpropagation.
In contrast, unbounded attractors may devolve into divergent systems under certain perturbations, leading to exploding gradients.
This insight also suggests that there can exist homeostatic mechanisms for certain implementations of continuous attractors that maintain the structure of the attractor sufficiently for the neural computation it is used in.
Finally, we verify in a simple continuous attractor that all perturbations preserve the invariant manifold and demonstrate the principle numerically in ring attractor systems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper uses the invariant manifold theorem and classifies manifolds into those that are bounded (and obey the invariant manifold theorem), and those that are unbounded (which don’t obey the invariant manifold theorem). They then show, consistent with the invariant manifold theorem, that unbounded attractors are more resistant to perturbation of RNN weight matrices. They connect this to exploding gradients in RNNs, and show that the bounded attractors have lower gradients than the others.

### Strengths
I like the aims of this paper. It is (mostly) clearly presented, and is original to me at least. I am concerned however about the generality of the approach (see below), and my take is that the idea and subsequent testing is a bit too preliminary to make any real conclusions.

### Weaknesses
Only two very simple settings are considered, and so it’s hard to know how general this approach is. The only learning considered is learning at small displacements from prespecified attractors. I would be nice to see are the bounded attractors more likely to be learned from arbitrary initialisations. What happens in complicated situations? Can any insights be made into the sorts of sequence tasks that machine learners care about? What does it mean for biological networks? Are there learning algorithms that lead to these bounded attractors?

Fig 3 is so cluttered it is hard to parse.

### Questions
See weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors utilized Fenichel’s persistence theorem to demonstrate that bounded line attractors are stable, meaning they maintain stability even when subjected to perturbations. This stability ensures that, when a corrective learning signal is present, backpropagation will not result in exploding gradients over any duration. In contrast, unbounded line attractors can become divergent systems when subjected to specific perturbations, leading to exploding gradients. This observation also suggests that specific implementations of continuous attractors may have built-in homeostatic mechanisms that preserve the attractor's structure, making it suitable for the neural computations it is intended for.

### Strengths
- The paper is well-written and its main idea is interesting. Especially, I liked the idea of using Fenichel’s invariant manifold theorem to address the discussed issue. 

- The visualizations provided in Fig. 1 and 2 are very helpful in providing a clear illustration of their method.

### Weaknesses
1. First off, it's important to note that, as demonstrated in the study by Mikhaeil et al. (2022), when dealing with chaotic or unstable dynamics, gradients will always explode and **this issue cannot be solved by RNN architectural design or regularization and needs to be addressed in the training process**. So, the authors should consider this more precisely.

2. The paper primarily focuses on a specific RNN variant, employing the ReLU activation function, 2-dimensional RNNs with specific parameter values outlined in equations (9) and (10). This specificity may limit the generalizability of its findings to higher dimensions, other architectural designs, and parameter configurations. In one particular parameter setting, the RNN exhibits 'well-behaved' dynamics, converging to a fixed point with bounded loss gradients. In such cases, established solutions (e.g., Hochreiter & Schmidhuber 1997; Schmidt et al., 2021) can be employed to prevent gradient vanishing. While this result is interesting, it's essential to recognize that it represents only one specific scenario and may not cover the broader spectrum of possibilities.

3. Utilizing Fenichel’s invariant manifold theorem, the authors established a sufficient condition to ensure that RNNs implementing continuous attractors remain immune to exploding gradients. However, pleae note that a ReLU RNN, discrete- or continuous-time, is a piesewise linear (PWL) dynamical system, a subclass of piesewise smooth (PWS) dynamical systems, that is smooth everywhere except on some boundaries separating regions of smooth behavior. These boundaries, called switching manifolds or borders, divide the phase space into countably many regions. Many existing theories of smooth DS do not extend to PWS systems. In PWS systems the interaction of invariant sets with switching manifolds often gives rise to bifurcations, known as discontinuity-induced bifurcations, which are not observed in smooth systems. Moreover, in the PWS setting, for bifurcations containing non-hyperbolic fixed points, similar slow (center) manifold approaches can be applied, but only to part of phase space. However, bifurcations involving switching manifolds cannot be examined in the same manner, as there is no slow (center) manifold. Consequently, the applicability of Fenichel’s invariant manifold theorem to different parameter settings of the considered system (eq. (7)) may be limited or pose considerable challenges.

4. Regarding the link between bifurcations and EVGP during training, it is essential to consider additional relevant literature. For instance, as demonstrated in (https://arxiv.org/pdf/2310.17561.pdf) specific bifurcations in ReLU-based RNNs are always associated with EVGP during training.

### Questions
Can the results of this paper be generalized to more general settings?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper analyzes the sensitivity of the attractors learned by RNNs to changes in its parameters. This analysis is based on Fenichel duality -- informally, decomposition of the phase space into slow and fast manifolds -- and Fenichel's theorem that gives the robustness of the slow manifold for certain bifurcations. They hypothesize that, in two dimensions, RNNs that have exploding gradients encounter bifurcations where Fenichel's theorem does not apply. This is illustrated with numerical examples.

### Strengths
The illustrative example and visualizations in two dimensions are quite useful to understand the overall message.

### Weaknesses
The biggest concerns are i) the lack of mathematically precise explanations and ii) the lack of guidance as to how to interpret the 2D results for RNN training in general. Specifically, it would be better if the implications of Fenichel's theorem for RNN training can be discussed more precisely. Can we prove that satisfying the conditions of the theorem is sufficient for convergence of training?

There is a brief remark about bifurcations into chaos also causing exploding gradients. Does this mean that the attractors of the hidden states are never chaotic attractors?

While the authors mention that these theoretical insights can be used to guide RNN training dynamics away from problematic bifurcations, it is unclear how that can be accomplished in practice, in high-dimensions.


Minor: 
1. Notation $\mathcal{M}_0$ and $M_0$ not used consistently.
2. Grammatical errors, e.g. " The BLA has a bounded loss in *it’s* neighborhood. "

### Questions
Apart from the questions in the previous section, it would be useful to answer some others that clarify the scope of the results. When can RNN dynamics be decomposed into slow-fast systems for which we can apply Fenichel duality? When does the input dynamics (discrete-time map) induce Fenichel-type attractors in the dynamics of the hidden state (may be the authors can expand a bit on their observations about the loss landscape near the normally hyperbolic fixed point). 

Even chaotic attractors can be structurally stable (e.g., Anosov systems or uniformly hyperbolic systems). So, clearly the lack of structural stability is not sufficient for keeping the RNN training dynamics from developing exploding gradients. Hence, what are the necessary and sufficient conditions for stable training dynamics?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The focus of the present paper is on attractor networks, a special kind of recurrent neural network whose dynamics converge to a fixed point, or more generally towards a stable pattern within a fixed manifold. While attractor networks are prevalent tools in neurosciences and more generally in machine learning owing to their memory and computational properties, they suffer from instability upon changing one or several of their parameters, which impedes gradient-based learning in such models. The present paper proposes an existing theoretical framework to systematically address this problem (invariant continuous attractor manifold theory) and proposes a set of simple experiments to validate the relevance of this framework. More precisely:

- The introduction introduces a simple class of RNNs (Eq. 1) of which two classes can be derived in dimension 2: the UBLA model and the BLA model. The UBLA model exhibits a half line in the positive quadrant of $\mathbb{R}^2$ as a stable manifold (i.e. continuously made up of fixed points) while the BLA model has a bounded line in the same quadrant as a stable manifold. The stable manifold of the former can break upon changing the weights in some way, while the stable manifold of the latter model is more stable. This poses the question of how stable learning (in the sense of preserving the topology of these stable manifolds) can be achieved in these models.

- Section 2.1 introduces Theorem 1, an existing theorem which, heuristically speaking, states that if the stable / invariant manifold of the model is initially bounded and smooth, then it may not change upon small perturbations. The slightly perturbed manifold is called a "slow manifold". In the light of this theorem, we may understand why UBLA (whose stable manifold is unbounded) is unstable upon weight nudging, while BLA is.

- Section 2.2 discusses implications on ML, and in particular that models not satisfying Theorem 1 (e.g. UBLA) exhibit exploding gradients. For models satisfying Theorem 1 (e.g. BLA), it is suggested that loss gradients could act as "restorative forces" to counteract the deformation of the stable manifold. This idea is empirically investigated later in the paper.

- Section 2.3 discusses implication on neurosciences.

- Section 3.1 presents the first experiment which is the linear temporal integration task. In this setting, the RNN processes a sequence of pair of stochastic clicks and is learnt to predict the time-cumulated difference between the clicks. Therefore the RNNs under investigation operate in two dimensions and three kinds of RNNs are studied: the identity RNN (Id), and the UBLA and BLA model previously introduced. Fig. 3, along with the text, states the main findings. 1/ when deterministically perturbing a single entry of the recurrent weight matrix of these models, UBLA and Id can diverge (i.e. the loss diverges upon running the temporal dynamics) while BLA remains stable (B), 2/ when starting from the model optimum and adding a single noisy weight perturbation to the models, gradient descent maintains the model near optimum (E), yet often to a suboptimal solution (F), 3/ BLA exhibits some advantages in terms of stability, 4/ "in practice, it is difficult to maintain any of the continuous attractors".

- Section 3.2 presents similar experiments but in polar coordinates, with the same integration task but on this circle. Two models are considered, one whose stable manifolds are the origin and the unit circle, another one where the stable manifold is boundary less. However, results aren't presented on this model.

- The conclusion is somewhat negative : 1/ "the homeostatic restoration of continuous attractor [through gradient signal] may be challenging", 2/ "further researcher on finding restorative learning for larger perturbations in the parameter space is needed".

### Strengths
- The paper tackles a difficult problem
- An existing theoretical framework is proposed to account for some observations.

### Weaknesses
 - The theoretical framework proposed, while enlightening the UBLA and BLA models, does not lead to a concrete prescription as to how to build RNNs that are robust to weight perturbations. Specifically, while the paper highlights the importance of bounded and smooth stable manifolds, it does not provide a constructive method for achieving this in practice beyond the specific BLA model. The connection to existing literature on constructing such attractors is not made clear, leaving the reader without a clear path to apply the theory.
- The models considered are two-dimensional, how do the findings extend to larger models? The paper argues that the theory applies regardless of dimensionality, but the experimental validation is limited to 2D cases. It remains unclear how the observed stability properties of BLA would translate to higher-dimensional RNNs, where the geometry of the attractor manifold could be far more complex. The claim that only chaotic systems in the neighborhood can cause exploding gradients in higher dimensions needs more rigorous justification and empirical support.
- If I understood the paper correctly, the sole takeaways of the study to have robust RNNs are to pick ones which have bounded and smooth stable manifolds and to use error gradients to counter act noise (however not so efficiently per the results). This is a rather incremental conclusion, as it essentially restates well-known principles of dynamical systems. The paper does not offer a novel mechanism or training strategy beyond this, and the experimental results suggest that even this approach is not particularly effective.
- The experimental setup may not be relevant to larger models, given that the RNN robustness is studied when the model is *already initialized at its optimum*, which may not be the case for a realistic task. This is a crucial limitation, as the behavior of RNNs during the learning process, especially far from the optimum, is not addressed. The paper does not explore how the stability properties of the BLA model evolve during training or how they might be affected by different initialization strategies. It is not clear if the observed robustness is an artifact of the specific initialization.
- The way the generality of the results are phrased in the introduction ("these theoretical results **nullify** the concern of the fine tuning problem in neurosciences and suggest **general principles** for evaluating and designing new architectures and initialization strategies for RNNs in ML") starkly contrast with the experimental setup considered (namely 2-dimensional RNNs on toy problems) and the conclusion which tends to be negative. Also, I do not see in this paper any proposal of "initialization strategies for RNNs in ML". The claims made in the introduction are not supported by the presented evidence and the conclusions are not aligned with the initial claims.

### Questions
I must say upfront that I am not an expert of this literature, so it might be that the paper meets the standard of its literature to gain acceptance. This being said: could you please phrase in a clear fashion the concrete outcomes of your study for a general, high-dimensional RNN?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
