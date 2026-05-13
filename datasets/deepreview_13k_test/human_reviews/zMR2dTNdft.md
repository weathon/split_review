# Symmetry Leads to Structured Constraint of Learning

- Decision: Reject
- Scores: 6, 5, 8, 5

## Abstract
Due to common architecture designs, symmetries exist extensively in contemporary neural networks. In this work, we unveil the importance of the loss function symmetries in affecting, if not deciding, the learning behavior of machine learning models. We prove that every mirror-reflection symmetry, with reflection surface $O$, in the loss function leads to the emergence of a constraint on the model parameters $\theta$: $O^T\theta =0$. This constrained solution becomes satisfied when either the weight decay or gradient noise is large. Common instances of mirror symmetries in deep learning include rescaling, rotation, and permutation symmetry. As direct corollaries, we show that rescaling symmetry leads to sparsity, rotation symmetry leads to low rankness, and permutation symmetry leads to homogeneous ensembling. Then, we show that the theoretical framework can explain intriguing phenomena, such as the loss of plasticity and various collapse phenomena in neural networks, and suggest how symmetries can be used to design an elegant algorithm to enforce hard constraints in a differentiable way.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a framework that analyze the local and global geometry of neural network with L2 regularization, using the loss symmetries, without any knowledge about the underlying network's architecture. The paper deals with 4 types of symmetries (rescaling, rotation, permutation and mirroring) and describes how each symmetry affects the geometry of the loss landscape with respect to the regularization coefficient. The paper uses the framework to analyze 5 different real world phenomenons and implement one algorithm.

### Strengths
The paper presents a novel approach to understand how symmetries in the loss function of a neural network regardless of their underlying architecture. It enumerates multiple real world application to justify the technique's importance.

### Weaknesses
The paper is hard to read and has some mathematical inaccuracies, I'll enumerate some of problems I encountered:

(1) The proof of theorem 4: there is a recurring typo writing ker(O) instead of ker(O^T) and the RHS of eq. 52 should be multiplied by -1 for the proof to hold

(2) Assumptions 1 and 2 are given without any explanation. It isn't self-evident that these are reasonable assumptions for real-world scenarios.

(3) Chapter 2.2 uses both big omega and R as rotation matrices, but R wasn't declared. In addition, item 1 in theorem 2 doesn't says for which gammas the theorem holds (I assume from the context it is for every gamma).

(4) In the line below equation 9, eta is used for learning rate, but it looks like gamma instead in subsequent paragraphs.

### Questions
No questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper considers a connection between the symmetries of the weights of a neural network and the constraints of the loss function. The authors proof that mirros symmetries lead to pre-defined certain behaviours of gradient-based model learning. For instance, rescaling symmetry of weights, leads to sparsity, rotation - to low-rankness and permutation leads to ensembling.

While the paper presents 4 theorems with possibly useful application, the flow of the paper, the content, require a significant revision.

#### Final Decision
After reading the other reviews and the answers, I stick to my rating

### Strengths
- The authors present four theorems. Each theorem is well-written on its own, and the proofs are correct, with a clear and easy-to-follow flow.
- The authors show that the paper has numerous connections to various fields in machine learning, which potentially opens up many possibilities for practical applications.

### Weaknesses
The main weakness of the paper is that the text itself does not allow the reader to immediately position the contributions of the paper in the realm of machine learning. It is not clearly stated what alternatives to this approach exist.

- The motivation of the paper is not clearly stated in the very beginning of the paper. The importance of the contribution becomes more and more clear only to the very end.
- There is no "Related work" section. The way it is presented in Section 4 does not sound coherent and does not allow the reader to properly position the work.
- The overall flow of the paper is not smooth. It jumps back and forth, there is no structure, there is no clear finale.
- There is no clear section with experiments. Figure 1 demonstrates some results. However, the results seem more like an illustration rather than a solid experiment. It should be built as an experiment with its motivation, details, and explanation. And it should be in the main part of the paper.
- Overall, the experiments do no convince.

### Questions
- In Eq 11, you suggest a reparametrization where $\theta$ is replaced with $u, v, w$. Does it mean that the total number of trainable parameters will increase by a factor of 3?
- Can you elaborate on the dynamics with which the neural network is sparsified if a scaling symmetry exists? Do you have any estimates on how long it will take for a weight to become less than $\epsilon \ll 1$? I can imagine, that in practice, due to the stochastic nature of optimization, the mechanism will work differently.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
A novel theory of neural network symmetries is put forward which is loss function and architecture agnostic. Namely, a class of mirror symmetries are defined which includes rescaling, permutation, and rotation symmetries, and these mirror symmetries are shown to interact with weight decay to create absorbing states that cause network training to preferentially converge to certain low-rank solutions. The implications of this theory on empirical phenomena, including block structure Hessians, SGD convergence to saddle points, neural collapse, and regularization, are discussed.

### Strengths
The paper covers a lot of ground and generally presents its contents clearly and in a well-organized fashion. It gives an elegant and very intriguing perspective on loss landscapes through symmetry alone. It also unifies many different symmetries under the common language of $O$-symmetries, which looks to be a powerful mathematical perspective. The theory disentangles the effects of symmetries from weight decay and other regularization techniques on the loss landscape, which could enable new avenues of attack on controlling the minima that training converges to.

### Weaknesses
My main concern is that the relevance of the work could be made explicit, as at first glance it seems to restate obvious results (such as that zeroed weights remain zero throughout training). In particular it would be nice to get a summary of how changes to weight decay, learning rate, and the amount of mirror symmetries affect empirical outcomes, such as more weight decay = more likely to fall into symmetry-induced stationary conditions.

In section 4.4, I don't believe this theory should take credit for the solution of adding random gradient noise, since it seems a trivial way to eliminate all stationary conditions regardless of whether they are caused by symmetry or not (the random bias method is more relevant). In general the connections in 4.4 require more work and empirical evidence in order to understand which are caused by symmetry and which are not. Overall, the main implications of this paper could be hammered out more strongly, while less central ideas like relating collapse to "phase transitions" and the DCS algorithm could be cut or left as a mention in the discussion.

Minor problems:
- Some details/notations could be explained more thoroughly, such as: define "structured constraint" when it is introduced, what is $R$ referring to in (3), same symbol $O$ is used for both mirror and order in (8), definition of $\lambda$ versus $\eta$ in (9).
- The statement "Notably, Entezari et al. (2021) empirically showed that neural networks under SGD
likely converge to the same type of solution if we take permutation symmetry into consideration" isn't quite right, as Entezari conjectures this and follow-up work Ainsworth et al. shows something weaker (linear connectivity between pairs of solutions).

### Questions
Adding a fixed random bias to all parameters clearly prevents $O$-symmetries, but would there still be symmetries present? E.g. if two weights could previously be mirrored about a hyperplane through the origin, after adding the bias they can now be mirrored about a parallel hyperplane that is offset by the bias vector. How does this method eliminate the structured constraints such as in figure 3?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies how loss function symmetries affect learning. The authors propose a general definition, namely mirror reflection symmetry, which unifies common symmetries including rescaling, rotation, and permutation symmetry. They then prove that every mirror symmetry leads to a structured constraint, which becomes a favored solution when the weight decay or gradient noise is large. The theoretical framework is applied to explain various phenomena in gradient based learning and to suggest new algorithms that enforce constraints.

### Strengths
Deriving properties of learning from symmetry in the loss function alone is original. This approach poses little assumption on the architecture, thus making the conclusions more general than previous studies. 

Besides bringing a novel perspective, the new framework based on symmetry provides explanations to a wide range of phenomena in neural network training. Its ability to unify the theory behind these phenomena demonstrates the usefulness of the proposed approach.

The writing is clear, and each theorem is accompanied by helpful and intuitive explanations.

### Weaknesses
Section 2.1 mentions ReLU network as an example with rescaling symmetry. ReLU networks are not differentiable at some points in the parameter space. However, the proof of theorem 1 assumes that $\ell_0$ is twice differentiable, at least in the neighborhood of all points with $(u,w)=(0,0)$. 

Depending on the geometry of the loss function, $\gamma$ that satisfies (21) may diverge close to (u,w)=(0,0). Hence, while Theorem 1 part 2 can be interpreted as locally favoring solutions (u,w)=(0,0), the required regularization strength can be too large to make this interpretation meaningful. Part 2 of theorem 2 and 3 have the same issue.

Some derivations in the main text skip steps, which makes it hard to follow for readers less familiar with related work. For example, it would be helpful to include some background information or reference for the escape rate of SGD in the third paragraph on page 7. In the following paragraph, the assumption that $H(x)$ commutes with $H(x’)$ might need a justification.

While the theory is successful in explaining various known phenomenon in training, there is limited evidence of its potential in guiding practices. Including some applications, such as experiments to back up the effectiveness of the algorithm in Section 4.6, could make the value of the theory more convincing.

### Questions
Lemma 2.1 in (Simsek 2021) also characterizes an attractive subspace derived from symmetry. Could the authors comment on whether this subspace is related to the stationary condition (Definition 3)?

Regarding footnote 5, would it be possible to prove that a twice differentiable function with bounded parameters cannot have a negatively diverging Hessian eigenvalue?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
