# Unified Universality Theorem for Deep and Shallow Joint-Group-Equivariant Machines

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6

## Abstract
We present a constructive universal approximation theorem for learning machines equipped with joint-group-equivariant feature maps, called the joint-equivariant machines, based on the group representation theory. ``Constructive'' here indicates that the distribution of parameters is given in a closed-form expression known as the ridgelet transform. Joint-group-equivariance encompasses a broad class of feature maps that generalize classical group-equivariance. 
Particularly, fully-connected networks are \emph{not} group-equivariant \emph{but} are joint-group-equivariant.
Our main theorem also unifies the universal approximation theorems for both shallow and deep networks.
Until this study, the universality of deep networks has been shown in a different manner from the universality of shallow networks, but our results discuss them on common ground. 
Now we can understand the approximation schemes of various learning machines in a unified manner.
As applications, we show the constructive universal approximation properties of \emph{four} examples: depth-$n$ joint-equivariant machine, depth-$n$ fully-connected network, depth-$n$ group-convolutional network, and a new depth-$2$ network with quadratic forms whose universality has not been known.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This work derives a closed-form ridgelet transform for a specific class of neural networks, that is defined as joint-group-equivariant networks. In this class of neural networks, the assumption is that not only input and output are equivariant to a group action (group-equivariant networks), but that instead also the model's parameters are equivariant to a representation of the same group action acting on the networks parameters. While this at first seems like a limitation of the presented theory, it provides insights to a broad range of models as demonstrated in the experiments

### Strengths
This work presents some important insights and most importantly a constructive universal approximation theorem for (joint) group equivariant neural networks. The presentation is clear, the proofs concise, and the introduction includes all necessary lemmas from group representation theory. In addition to the derivation of a ridgelet transform for joint group invariant networks, section 5 provides the corresponding ridgeless transform for n-layer fully connected neural networks.

### Weaknesses
First it appears to be a limitation of the work, that the presented theory only applies to joint group equivariant networks (that is, the same group action is applied to the network's parameters as to the input and output), instead of to the widely used group equivariant networks (in which no group action acts on the model parameters to reach equivariance). In Remark 1, also Figure 1, it is however stated that the group-equivariant networks are included as a subclass of joint equivariant networks, as those for which G acts trivially on the parameter domain.

This raises some concerns, if all of the developed theory applies to this case. Theorem 4, which is the core of the established theory and defines the ridgelet transform, relies on irreducible representations of the group actions, both for the input as for the parameter space. If however we would require the irreducible trivial representation for the parameter space but not for the input space then the question arises if all of the proofs still hold for this case. This might trivially be the case but because of its importance a comment on this special case would strengthen the manuscript.

Further information on the underlying assumptions for the non-linearities is needed. For group equivariant networks it is well-known that arbitrary non-linearities might destroy group-equivariance. It would be important to state which assumptions need to hold for the non-linearities for the joint group equivariant case and group equivariant case (in which G acts trivially on the parameter domain).

In particular, the manuscript does not adequately address the implications of the developed theory for standard group equivariant networks, which are a special case of joint group equivariant networks. The current discussion is limited to Remark 1 and a reference to Sonoda et al. (2022a) in Section 7, which is insufficient to clarify the applicability of the presented framework to the non-joint case. The manuscript needs a dedicated section that explicitly lays out the theory for the special case of G-equivariant networks, and clearly states the assumptions that need to be fulfilled for the theory to hold in the presence of non-linearities. The current presentation leaves it unclear how the developed framework can be applied to G-equivariant networks, and how the results relate to existing work on G-equivariant networks.

### Questions
- Does the derivation completely hold for the case in which the irreducible trivial representation is required for the parameter domain to include the group-invariant case?

- Are there any specific underlying assumptions for the non-linearities and how does this relate to the special requirements that non-linearities usually need to fulfill to preserve group equivariance?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The proposed paper presents a constructive universal approximation theorem for learning machines equipped with joint-group equivariant feature maps, extending previous work on convolutional and joint-group invariant feature maps. Additionally, it provides examples of depth-$n$ joint-equivariant machines, depth-$n$ fully connected networks, and quadratic forms with nonlinearity.

### Strengths
- The paper generalizes existing work on constructive approximation and the ridgelet transform on invariant machines to the equivariant case.
- Mathematical notation is clear, and the proofs are correct.

### Weaknesses
1. Significant overlap with previous work [1].
2. Lack of examples covering models commonly used in the equivariant ML literature.
3. Numerous technical lemmas hinder readability and obscure the main message.

Regarding the first weakness, I understand that group equivariance generalizes invariance, extending the scope of this work beyond [1]. However, if I am not mistaken, the technical advancements over [1] to achieve this generalization are minimal. Indeed, the *principal contributions* of this paper—the statement and proof of the main theorem (Theorem 4)—appear *nearly identical* to those of Theorem 9 in [1].

Moreover, it appears that Section 3 (Main Results) of the paper presents only minor differences from Section 3 of [1], which can be summarized as follows:

- Jointly-Equivariant Machines (Def 4) are simply the equivariant analogs of Generalized Neural Networks ([1], Def 7), with no further differences in definition.
- The Ridgelet Transform for Jointly-Equivariant Machines (Def 5) is analogous to the Ridgelet Transform of [1] but is integrated over a scalar product on $Y$ instead of a scalar product on $\mathbb{C}$.
- This section presents four technical lemmas with simple, straightforward proofs that, in my opinion, hinder readability and could be moved to an appendix.

Additionally, Section 2 of the paper and Section 2 of [1] are again nearly identical, though this may be more understandable as they introduce notation.

### Questions
- Can the authors clarify the differences between the presented paper and [1] and explain how this work provides novel insights relative to the cited paper?
- Could the authors elaborate on the relevance of the examples presented in Sections 5 and 6 within the context of current equivariant ML literature?

---
[1] S. Sonoda et al., Joint Group Invariant Functions on Data-Parameter Domain Induce Universal Neural Networks. In Proceedings of the 2nd NeurIPS, Workshop on Symmetry and Geometry in Neural Representations, Proceedings of Machine Learning Research, PMLR, 2024.

### Soundness
4

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper presents a new theorem establishing universality of joint group-equivariant learning machines (where a locally compact group acts on input, parameter and output space). The proof is constructive, in that an integral transform is given that maps the function to be represented to a parameter distribution (generalized function). As a special case, this covers universality of deep fully-connected networks, for which such a constructive proof had not been available (it was only known for shallow ones). The approach of this paper applies equally to shallow and deep networks. The paper also introduces new techniques based on group representation theory, that may find wider application in the theory of neural networks.

The basic idea of the proof is to show that the map LM(R(f)) commutes with an irreducible representation and is therefore by Schur's lemma a multiple of the identity. Here R is the operator taking functions to parameters, and LM is the operator mapping parameters to functions.

### Strengths
The paper is written in a clear and precise way, and the authors are clearly expert on the topic. Although the result is ultimately a simple application of Schur's lemma, the insight that this tool can be applied here to answer universality questions, and the whole setup that enables the statement of the theorem, is in my opinion quite significant.

### Weaknesses
I could not find very significant weaknesses, but one limitation seems to be that although these techniques establish universality for potentially infinitely wide (and finitely deep) neural networks, they do not show that the approximation error can be reduced by increasing width (or at what rate this error reduces). Furthermore, while the paper provides a constructive proof of universality, it does not offer much insight into the practical implications of the integral transform for finite-width networks. The conditions under which the constant in Theorem 4 is non-zero are not fully explored, and it remains unclear how to verify these conditions for specific network architectures beyond the examples given. The paper also does not discuss the stability of the parameter distribution obtained through the integral transform, which is a crucial factor for practical applications.

### Questions
In so far as I could tell, the mathematics is correct. I once read Folland's book (a primary reference), so I should have some appropriate background, but still this is a long time ago and with the time I could invest in the paper I could not ascertain with 100% confidence that all results are correct. I am fairly confident in the main theorem, but I found it a bit hard to see when exactly the conditions are satisfied. Seeing more examples of concrete networks where the conditions are satisfied, and importantly, examples where they fail, would help me better appreciate the theorem and convince myself of its significance.

### Soundness
3

### Presentation
4

### Contribution
3
