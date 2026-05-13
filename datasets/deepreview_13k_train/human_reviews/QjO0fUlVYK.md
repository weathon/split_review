# Do Deep Neural Network Solutions Form a Star Domain?

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
It has recently been conjectured that neural network solution sets reachable via stochastic gradient descent (SGD) are convex, considering permutation invariances \cite{entezari_permutation_invariances_2022}. This means that a linear path can connect two independent solutions with low loss, given the weights of one of the models are appropriately permuted. However, current methods to test this theory often require very wide networks to succeed \citep{ainsworth_git_re_basin_2022, benzing_random_2022}. In this work, we conjecture that more generally, the SGD solution set is a \textit{star domain} that contains a \textit{star model} that is linearly connected to all the other solutions via paths with low loss values, modulo permutations. We propose the \textit{Starlight} algorithm that finds a star model of a given learning task. We validate our claim by showing that this star model is linearly connected with other independently found solutions. As an additional benefit of our study, we demonstrate better uncertainty estimates on the Bayesian Model Averaging over the obtained star domain. Further, we demonstrate star models as potential substitutes for model ensembles.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a weaker version of the conjecture that the minima recovered by SGD are convex up to permutations, proposing instead that this set is star-shaped up to permutations. A small theoretical motivation is given for shallow linear networks, but the main evidence is empirical, where the authors propose an algorithm to find the star model at the center of the start shape from a ensemble of trained networks. They then observe that the star-shaped conjecture is approximately true for networks where the convex conjecture is not. 

Finally two alternatives are proposed to ensembling: sampling from the star shape, or taking the star model. Both seem to be promising.

### Strengths
The paper is well written, and the conjecture makes sense and is easy to understand. The experiments are quite convincing, though one could obviously alway try larger/deeper networks.

### Weaknesses
The authors do not propose any intuition why star-shape is the right choice to fix the convex up to permutation conjecture. While the empirical results are compelling, the theoretical motivation for star-shapedness, limited to shallow linear networks, feels insufficient to justify the broader claim. Specifically, it's unclear if the star-shaped property can be guaranteed for significantly smaller widths than what is required for convexity, and what the precise relationship between these widths is. The paper would benefit from a more in-depth theoretical analysis of this aspect.

Star-shape is significantly weaker than convexity (especially in high dimension, I would guess), so it is not completely surprising that one can reach a lower barrier. The practical implications of this weaker condition are also not fully explored. While the authors propose an algorithm to find the star model, the computational cost seems high, requiring a large ensemble of models. This raises questions about the practical scalability of the approach, especially given the need for a large number of models to accurately locate the star model. The paper needs to address the computational cost more directly, and perhaps explore methods to reduce the number of models needed to find the star model.

### Questions
See weaknesses.

### Soundness
3

### Presentation
4

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
# 

The paper raises a conjecture if the trained neural networks, after taking into account for the permutation symmetries, form a star domain, i.e. there exists a neural network that is linearly connected to all the other networks. 

Authors propose an algorithm to find the model that is star model by utilizing permutation matching algorithms and by defining a loss that minimizes the error barrier between the star model and other networks in the set.

Authors empirically validate the conjecture by showing that one can find a star model that is linearly connected to all the networks. 

Authors show that model found by Starlight leads to mild improvement in generalization than individual models but still is a bit worse than model ensembling

### Strengths
- Paper is easy to follow and give sufficient background.
- Introduced the star-conjecture that is stronger than mode connectivity as in [1] but weaker than weak linear connectivity at defined in [2]

### Weaknesses
 - Relationships with other notions of linear connectivity is not very well discussed.
- If I understand correctly, the experiments only conducted when there is weak linear connectivity modulo permutation holds since weak linear connectivity implies the star conjecture:
    - If weak linear connectivity modulo permutation holds, one can pick any model $\theta$ from the set $Z = \{\theta_1, \dots, \theta_N\}$ and find permutation $P_1, \dots, P_N$ that linearly connects the model $\theta_i$ to $theta$. This should lead to star connectivity
- Results for Starlight over model ensembling are not very extensive,

Minor comments:

- the bibliography needs many fixes. Specially because authors cite the arxiv version of the paper but should cite the publications

### Questions
I might be missing it but are there any experiments where Starlight algorithm finds a model where permutations fail to reduce the error barrier?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper conjectures that SGD solution set of neural networks is a star domain. 
They have proved their conjecture for a toy model of neural networks, namely shallow linear neural networks with just one-dimensional input data . They also propose a Starlight algorithm to find a star model of a given task. It is mentioned that the benefit of having star domain for network solution is in Bayesian Model Averaging. Authors also supported their claims by proving empirical studies.

### Strengths
The paper is written clearly at some parts but I believe the writing can still be improved. 
For example, it was not clear at the beginning of paper why such a star model property is important in NN, but authors explain this later 
in their section 4. 
The main contribution of the paper seems to be interesting, but I am still not convinced about their details.

### Weaknesses
I think beyond their Theorem 1 that is proved for a really toy model of neural networks under strict assumptions, there is no theoretical support over their claimed conjecture. 
I also believe there are confusing points in the paper that need to be clarified, please see my question list below.

1- This questions is related to the title and the whole paper `DO DEEP NEURAL NETWORK SOLUTIONS FORM A STAR DOMAIN?'
Do authors by 'solution' mean the global minima of objective function? If yes, how can authors make sure that global minima are reached in practice by SGD (objective functions are highly non-convex), let say in practical settings like limited width of the neural network? This question also concerns your empirical observations. 
Also `The learning problem for a neural network is inherently characterized by a non-convex loss landscape, leading to multiple possible solutions rather than a singular one.' As far as I am aware, the first and main concern in optimization of NN is non-global optima solutions. 
And could you please elaborate what is the role of SGD here? Why not other optimization methods? 

2-Theorem 1 is targeting a toy model of neural networks (shallow, linear, ...), could you please elaborate how this theory under restrictive Assumption 1 can support your Conjecture? Could authors also elaborate on how Assumption 1 makes sense in practice? 

3-Line 236: How can you reach all those solutions, while it is computationally too expensive? In fact, there are infinitely many solutions for neural networks, it kinda seems too far to extract a set of solutions. How large that set need to be to leave you a star point? 

4-Line 267: It is not clear for me how authors handle finding optimal permutations? Could you please elaborate more?  

5-Theorem 1 is valid for $m\to \infty$. How authors can handle this in practice? 

6-Line 502, it is stated that this approach is useful to decrease computational expenses, but I am not sure how it can happened following your proposed setting in 236 and solving (3). 

7-Better to clarify about importance of start shaped models sooner in text regarding your comments in section 4.2.

### Questions
1- This questions is related to the title and the whole paper `DO DEEP NEURAL NETWORK SOLUTIONS FORM A STAR DOMAIN?'
Do authors by 'solution' mean the global minima of objective function? If yes, how can authors make sure that global minima are reached in practice by SGD (objective functions are highly non-convex), let say in practical settings like limited width of the neural network? This question also concerns your empirical observations. 
Also `The learning problem for a neural network is inherently characterized by a non-convex loss landscape, leading to multiple possible solutions rather than a singular one.' As far as I am aware, the first and main concern in optimization of NN is non-global optima solutions. 
And could you please elaborate what is the role of SGD here? Why not other optimization methods? 

2-Theorem 1 is targeting a toy model of neural networks (shallow, linear, ...), could you please elaborate how this theory under restrictive Assumption 1 can support your Conjecture? Could authors also elaborate on how Assumption 1 makes sense in practice? 

3-Line 236: How can you reach all those solutions, while it is computationally too expensive? In fact, there are infinitely many solutions for neural networks, it kinda seems too far to extract a set of solutions. How large that set need to be to leave you a star point? 

4-Line 267: It is not clear for me how authors handle finding optimal permutations? Could you please elaborate more?  

5-Theorem 1 is valid for $m\to \infty$. How authors can handle this in practice? 

6-Line 502, it is stated that this approach is useful to decrease computational expenses, but I am not sure how it can happened following your proposed setting in 236 and solving (3). 

7-Better to clarify about importance of start shaped models sooner in text regarding your comments in section 4.2.

### Soundness
2

### Presentation
2

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
The paper presents a conjecture regarding the nature of solution sets for deep neural networks (DNNs) trained via stochastic gradient descent (SGD). It introduces the concept of a "star domain," proposing that these solution sets can be characterized by a special "star model" that connects to all other solutions in a low-loss path, modulo permutation invariances. The paper proposes the ``Starlight" algorithm that finds a star model of a given learning task and confirms existing reports that the convexity conjecture requires very wide networks to hold based on experimental results.

### Strengths
The introduction of the star domain conjecture adds a novel perspective to existing theories regarding the connectivity of neural network solutions. The Starlight algorithm is well-defined and offers practical means to identify star models, contributing to the field of model ensemble methods. The paper includes thorough empirical validation across various architectures and datasets, strengthening the claims made.

### Weaknesses
While the empirical results are promising, the theoretical underpinnings of the star domain conjecture could be elaborated further. The authors acknowledge challenges in validating the conjecture theoretically but could provide more insights into potential avenues for future theoretical exploration.

The experiment results primarily focus on specific settings (e.g., ResNet, CIFAR-10). Broader validation across different tasks and architectures could enhance the generalizability of the findings.

The algorithm's complexity may pose challenges for reproducibility. Detailed discussions on implementation and computational overhead would be beneficial.

### Questions
-  Theorem 1 is established for an oversimplified two-layer linear network. Can the author at least show results with two-layer network with nonlinear activations? Otherwise, the theory is too weak to support the star domain conjecture.

-  Follow-up questions : How do the authors envision extending the theoretical framework of the star domain conjecture to encompass a broader range of neural network architectures and training methods? What specific conditions or assumptions must hold for the star domain conjecture to be valid in practical applications?

-  About Empirical Validation: how do the authors plan to validate the star domain conjecture across different types of neural network architectures (e.g., transformers, recurrent networks)? Can the authors provide additional insights or results regarding the performance of the Starlight algorithm in high-dimensional parameter spaces?

- About algorithm complexity: Given the complexity of the Starlight algorithm, what steps have the authors taken to ensure its computational efficiency and ease of implementation in practical settings? Are there potential optimizations or modifications to the Starlight algorithm that could enhance its performance, especially in large-scale applications?

### Soundness
3

### Presentation
3

### Contribution
3
