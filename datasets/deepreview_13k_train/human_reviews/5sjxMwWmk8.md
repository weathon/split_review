# Robust Angular Synchronization via Directed Graph Neural Networks

- Decision: Accept
- Scores: 5, 6, 6, 8

## Abstract
The angular synchronization problem aims to accurately estimate (up to a constant additive phase) a set of unknown angles $\theta_1, \dots, \theta_n\in[0, 2\pi)$ from $m$ noisy measurements of their offsets $\theta_i-\theta_j \;\mbox{mod} \;  2\pi.$ Applications include, for example, sensor network localization, phase retrieval, and distributed clock synchronization. 
An extension of the problem to the heterogeneous setting (dubbed $k$-synchronization) is to estimate $k$ groups of angles simultaneously, given noisy observations (with unknown group assignment) from each group. Existing methods for angular synchronization usually perform poorly in high-noise regimes, which are common in applications. In this paper, we leverage neural networks for the angular synchronization problem, and its heterogeneous extension, by proposing \textsc{GNNSync}, a theoretically-grounded end-to-end trainable framework using directed graph neural networks. In addition, new loss functions are devised to encode synchronization objectives. Experimental results on extensive data sets demonstrate that GNNSync attains competitive, and often superior, performance against a comprehensive set of baselines for the angular synchronization problem and its extension, validating the robustness of GNNSync even at high noise levels.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the problem of angular synchronization, in which the goal is to compute one or multiple sets of angles given noisy measurements of their differences , which are given as a weighted directed graph.  The output is given mod $2\pi$ and up to an additive constant angle. The main contribution is in the case that the measurements are noisy. These errors lead to inconsistencies in the sum of angles that belong to directed cycles of the graph, which can have non-zero due to the noise. The loos function that is used to apply a projected gradient descent algorithm encodes these inconsistencies and thus the gradient descent algorithm is trying to minimize them. Furthermore, the authors have implemented the algorithm and run experiments on synthetic data and under various noise models to demonstrate the algorithm’s accuracy and robustness to noise in comparison with prior work.

### Strengths
The proposed algorithms outperform existing ones in the literature for high levels of noise.

### Weaknesses
The paper doesn’t seem to have a lot of technical novelty and depth.



### Questions
In the problem definition, the phrase “at most one of $A_{i,j}$ $A_{j,i}$ can be non-zero by construction” does not seem to be consistent with the definition above. Can you clarify?

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a training framework (GNNSYNC) that incorporates directed graph neural networks to address the classical angular synchronization problem and its extended k-synchronization variant. Specifically, a directed GNN is first applied to learn 
node embeddings which are used to generate an initial guess.  Then, projected gradient steps are applied to refine the solution. 
Finally, the additional hyper parameters such as the feature matrix are learned by minimizing loss functions based on estimation error and cycle consistency. The proposed methods are evaluated by numerical experiments on synthetic and real datasets.

### Strengths
1. The paper claims that the proposed method is robust to the high noise level. 
2. The paper devises new loss functions (upset/cycle) that allow to apply GNN techniques.
3. The paper extends the method to a more challenging heterogeneous setting.

### Weaknesses
1. While the paper claims that GNNSYNC is a theoretically grounded trainable framework. No theory is provided under any noise assumptions regarding 1) Can this method converge? 2) What kind of guarantee do we have (e.g. How close the solution provided by the algorithm is to the ground truth). While for standard algorithms such as GPM, we have well-established theoretical guarantees for certain types of noise.

2. While the paper performs extensive experiments, the comparison with the baseline under high noise level seems not convincing. When we have a certain noise level, the standard way is to first provide an initial guess by solving a generalized eigenvalue problem, then projecting to the SO(2) space and aligning with anchors (if they exist). Finally, Riemannian/projected gradient descent is used to finetune the solution by minimizing a loss function (which can be adjusted based on the noise level). It seems GNNSYNC consists of multiple stages while there is no further fine-tuning steps for the baseline methods. 

Minors
* The paper mentions that the motivation for k-synchronization is practically interesting because of some applications in structural biology, but it seems no experiments are conducted on biological applications. Also, even the 'real-world' dataset is perturbed artificially, which makes it not easy to see if the method can generalize well.
* As mentioned by the authors, GNNSYNC shares many similarities with the GNNRank framework.
* Currently, GNNSYNC is limited to SO(2) group.

### Questions
1. It seems GNNSYNC itself is a complicated framework with many components. I am wondering if every component is necessary for it to solve the concise angular synchronization problem. Could you please also illustrate why the proposed method works well in high noise regimes while the other methods do not?

2. I would appreciate it if the authors could justify that the proposed method is exactly better than the standard method with fine-tuning (by using either the standard log-likelihood function or the newly designed loss functions.)

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the angular synchronization problem. It proposes GNNSync, which is a trainable framework using directed graph neural networks, to solve the problem. It also comes up with a new loss function to encode synchronization objectives. Numerical experiments are conducted to validate the superiority and robustness of GNNSync.

### Strengths
1. It incorporates the inductive biases of classical estimators within the design of GNNSync and casts the angular synchronization problem as a theoretically-grounded directed graph learning task.

2. It proposes a novel training loss that exploits cycle consistency to help disambiguate unknown angles.

### Weaknesses
It is unclear how to train GNNSync since the uncommon loss function in (5) is not smooth.

It is not clear how the non-smooth operations within the loss function, specifically the modulo and min operations, affect the training process. The gradient calculation for such a loss function is not straightforward, and the paper lacks a detailed explanation of how backpropagation is handled in the presence of these non-differentiabilities. The use of a subgradient, while potentially valid, is not explicitly mentioned or justified within the main text. Furthermore, the practical implications of using a non-smooth loss function, such as potential convergence issues or instability during training, are not discussed.


### Questions
1. The loss function (5) incorporates mod and min operation inside. Could the authors please clarify how to calculate the gradient of this loss?

2. Please clarify how to conduct projection in line 7 of Algorithm 1. Does the projection have a closed-form? How expensive is this projection step?

3. Why do you need to conduct several steps of projection per round?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the problem of angular synchronization, which involves estimating a set of unknown angles from noisy measurements of their pairwise offsets. This problem appears in various applications, such as sensor network localization, phase retrieval, and distributed clock synchronization. The paper also extends the problem to a heterogeneous setting, named $k$-synchronization, where the goal is to estimate multiple groups of angles simultaneously from noisy observations.

To overcome the poor performance of existing methods in high-noise regimes, the authors propose GNNSync, a novel framework based on directed GNNs. The framework is end-to-end trainable and incorporates theoretically-grounded techniques to improve robustness to noise.

### Strengths
- The authors introduced GNNSync, a GNN-based method designed specifically for the angular synchronization problem and its heterogeneous extension, $k$-synchronization.
- I believe the main contribution of this paper resides in the proposal of new loss functions that encode synchronization objectives, with a particular focus on a cycle loss function that downweights noisy observations and enforces cycle consistency.
- There is extensive experimental validation for the proposed method, demonstrating that GNNSync outperforms existing state-of-the-art algorithms, especially in high noise scenarios, across various synthetic and real-world datasets.

### Weaknesses
I do not see significant weakness in this paper. In some cases regarding the performance of the proposed method, particularly in the case of BAO, where its performance does not significantly outperform the baseline methods. Would the authors be able to elaborate a bit on that?

### Questions
The authors mentioned that extending the current GNN-based framework from SO(2) to more general groups may introduce several challenges and complexities. I would like the authors to elaborate a bit on the potential difficulties in generalizing the current method.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
