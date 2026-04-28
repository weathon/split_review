# Towards Training Without Depth Limits: Batch Normalization Without Gradient Explosion

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Normalization layers are one of the key building blocks for deep neural networks. Several theoretical studies have shown that batch normalization improves the signal propagation, by avoiding the representations from becoming collinear across the layers. However, results on mean-field theory of batch normalization also conclude that this benefit comes at the expense of exploding gradients in depth. Motivated by these two aspects of batch normalization, in this study we pose the following question: 
``Can a batch-normalized network keep the optimal signal propagation properties, but \emph{avoid} exploding gradients?'' We answer this question in the affirmative by giving a particular construction of an \emph{Multi-Layer Perceptron (MLP) with linear activations} and batch-normalization that provably has \emph{bounded gradients} at any depth. Based on Weingarten calculus, we develop a rigorous and non-asymptotic theory for this constructed MLP that gives a precise characterization of forward signal propagation, while proving that gradients remain bounded for linearly independent input samples, which holds in most practical settings. Inspired by our theory, we also design an activation shaping scheme that empirically achieves the same properties for certain non-linear activations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper shows the existence of a batch-normalized network that avoids rank collapse and does not suffer from exploding gradients as depth increases. To construct a network that satisfies the above properties, the paper uses an initialization scheme where the weights are random orthogonal matrices.

### Strengths
The isometry and log gradient norm bounds are non-asymptotic bounds. Furthermore, the usage of Weingarten calculus to obtain rates for isometry increase is interesting.

### Weaknesses
The paper uses a modification of batch normalization (in particular the mean centering operation is removed) when proving bounds on the isometry gap and log gradient norms. While the experiments seem to suggest that this is not an issue in practice, the theoretical analysis is not directly applicable to standard batch normalization. This discrepancy between theory and practice weakens the theoretical contribution. The results would be more compelling if the theoretical analysis could be extended to standard batch normalization or if a more detailed justification for using the modified version was provided. 

The paper also considers the setting where the number of training examples is equal to the dimension of the problem. This is a highly restrictive assumption that limits the practical applicability of the theoretical results. In many real-world scenarios, the number of training samples is much larger than the dimensionality of the input space. The theoretical analysis should be extended to more realistic settings where the number of training samples is significantly larger than the dimension, or at least a discussion of the limitations of the current setting should be included.

### Questions
Do you obtain figures similar to F1 when using ReLU activations?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors address the problem of gradient explosion with depth in networks with Batch Normalization (BN) outlined by Yang et al. [1]. They show that infinitely deep linear networks can be trained with BN while avoiding the problem of gradient explosion as long the weights are orthogonal.

[1] Yang, Greg, et al. A Mean Field Theory of Batch Normalization. International Conference on Learning Representations. 2018.

### Strengths
1. The authors present a proof for avoiding gradient explosion in infinitely deep linear networks with BN as long as the inputs are full rank and the weights of the network are orthogonal.

2. In linear MLPs with upto 1000 layers, they show that orthogonality is approximately maintained in the middle layers as required by the proposed theorem.

3. The presented proof and argument is easy to follow.

### Weaknesses
1. The authors have not included literature on recent work on inducing dynamical isometry in feedforward networks which has shown to also avoid the need for BN. The discussion seems relevant for this paper (see [1], [2], [3]). Specifically, the connection between orthogonal weight initialization and dynamical isometry, and how both relate to controlling signal propagation in deep networks, should be discussed. The authors should also discuss how their approach compares to methods that directly optimize for dynamical isometry during initialization.

2. The proof relies on the fact that the network is has linear activations and the weights are orthogonal during training. Although, this seems to somewhat hold empirically for linear networks, how reasonable is it to expect such a condition to hold for nonlinear activations? The weights will likely not stay orthogonal during training for nonlinear activations. Further, can the analysis be extended to nonlinear ReLU - like activations, by potentially using a first order approximation of the ReLU [4] or other approximations? Specifically, the analysis should address how the non-linearity impacts the singular values of the weight matrices during training and how this affects the gradient propagation.

3. Since the proof requires for the network weights to be orthogonal, the network is only restricted to learn a rotation of the inputs. This seems restrictive from an expressiveness point of view unless I misunderstand something. It's unclear how this constraint affects the network's ability to learn complex functions, and whether the benefits of avoiding gradient explosion outweigh this limitation. The authors should provide a more detailed discussion on the expressiveness of the proposed network architecture and how it compares to other architectures that do not impose this orthogonality constraint.

### Questions
See above section for questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses limits of gradient descent loss minization of (very) deep networks using batch normalization (BN). In particular, it mends explosion of gradients during backdrop training in such networks. After a neat introduction a novel theoretical results are laid out in an accessible manner and main idea of proofs is presented (linked to full proofs in Appendix). Using recent results on random matrix theory, namely that BN does not decrease isometry gap (a measure of deviance of sample covariance $XX^T$ from orthogonality), paper proofs its main Theorem 1. It claims that expected isometry gap has an upper bound whose rate of decrease is exponential in depth under assumed linear independence of inputs. It is followed by Theorem 5, which proves that, under mild smoothness and loss assumptions, the $\textit{expected}$ log norm of gradient of the constructed MLP network, i.e. deep network with linear activations and simplified BN, has finite upper bound $~d^5$.

Following section supports the results by limited experiments, showing that rank collapse does not occur when MLP using (simplified) BN as proposed is used.

Paper follows to discuss possible extensions to treat non-linear networks and proposes activation function shaping through additional pre-activation scale hyperparameter, that is tuned towards zero, effectively linearising explored models using $tanh(\cdot)$ and $sin(\cdot)$ activations.

### Strengths
1. To the best of reviewers knowledge presented are novel results (Theorem 1, 5) that are non-asymptotic and hold for networks with finite width, as opposed to previous works. This is very promising and of large interest and value to ML community increasing potential impact of the manuscript. 

2. Very well and accessibly written exposition of rather technical methods (random matrix theory, Weingarten calculus) used in proofs.

3. After theoretical results paper (creatively) suggests activation shaping technique in combination with BN increasing and demonstrating practical utility of results.

### Weaknesses
#1: While the non-asymptotic and finite width results may be largely impactful as noted in Strengths, the importance may be diminished by applicability on 
1. $\textit{expected}$ grad norm
2. grand norm bounds of Theorem 5 may be still prohibitively large $\textit{e^{d^5}}$ and 
3. "practicality" may be hindered by "$\textit{linear}$ activation" required (this is somewhat alleviated by last section by introducing more hyper-parameters to bring $sin$ and $tanh$ activations to linear regime).

I believe authors should extend the Discussion or include section to elaborate more on these points. Possibly extend a rather limited experiments to corroborate their arguments in case of a lack of theory.

#2: Technical: Dimensionality discrepancies throughout Section 3, page 3 and 4. For instance:
 - in the definition of $\varPhi(X)$ on page 4, the $\varPhi(X)$ is not function of $R^{d \times d}$.
 - $X$ should be $d \times n$ matrix instead of previously defined $n \times d$ or $XX^T$ should be used instead of $X^TX$

### Questions
Q1: Related to Weaknesses, ad 3.) "practicality", Could authors present their view on what benefits are provided by deep linear networks compared to shallower linear nets? 

Q2: To address aforementioned limitations of theoretical results (see Weaknesses #1, 1-3),, e.g., to support non-linear activation, authors propose activation shaping combined with use of BN. From their argument it seems that such technique, tuning pre-activation gain $\alpha$ towards zero, effectively linearise the network. Section 5 claims that this technique still maintains the benefits of non-linear activations demonstrated in Fig.5. Could authors elaborate on how exactly are benefits maintained? 

Q3: In later sections paper presents intriguing idea of “implicit bias towards orthogonal matrices”, for instance in Fig 6. But one can read experimental results in Fig 6. other way, namely that it suggests that while middle layers have been initialised already “almost orthogonal” their orthogonality gap increased the most during training compared to other layers! Could authors show further evolution of training continued beyond the early stopping or otherwise corroborate "implicit bias" claims more extensively?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper is a theoretical study on batch normalization. A simplified setting is considered where BN does not use mean subtraction and where there are no other non-lineary functions. The paper presents two theorems that hold when the weight matrices are random orthogonal matrices. Theorem 1 states that the representations become increasingly orthogonal with the depth of the network. Theorem 5 states that the gradients do not explode with depth. All results hold in expectation over the random weights. The authors also provide a method for modifying non-linear activation functions by changing the gain.

### Strengths
The paper presents two theorems which are relevant and non-asymptotic.

Normalization is used everywhere in ML, so studying it has a high impact.

### Weaknesses
The main question of the paper is “Is there any network with batch normalization without gradient explosion and rank collapse issues?”. It is not clear why this question is interesting. The authors show that orthogonal random weights avoid these issues, but such initialization schemes are not used in practice despite being well known. Thus, in practice, BN works for reasons that are unrelated to the specific weight initialization scheme that is proposed. So the paper is not really “explaining” why BN works.

There are still some simplifying assumptions in the theoretical parts – there are no nonlinearities and the mean subtraction of BN is omitted.

It is not clear how relevant the empirical results are, though the authors might be able to clarify this for me.

### Questions
Why is the main question (“Is there any network with batch normalization without gradient explosion and rank collapse issues?”) interesting to practioners? Given that BN works well without orthogonal initialization.

How is the activation shaping motivated by theory?

What is the practical utility of the activation shaping you propose?

Does your result hold for networks with mean reduction?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
