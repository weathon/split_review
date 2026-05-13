# Composing Global Optimizers to Reasoning Tasks via Algebraic Objects in Neural Nets

- Decision: Reject
- Scores: 6, 5, 6

## Abstract
We prove rich algebraic structures of the solution space for 2-layer neural networks with quadratic activation and $L_2$ loss, trained on reasoning tasks in Abelian group (e.g., modular addition). Such a rich structure enables \emph{analytical} construction of global optimal solutions from partial solutions that only satisfy part of the loss, despite its high nonlinearity. We coin the framework as \ours{} (\emph{\underline{Co}mposing \underline{G}lobal \underline{O}ptimizers}). Specifically, we show that the weight space over different numbers of hidden nodes of the 2-layer network is equipped with a semi-ring algebraic structure, and the loss function to be optimized consists of \emph{monomial potentials}, which are ring homomorphisms, allowing partial solutions to be composed into global ones by ring addition and multiplication. Our experiments show that around $95\%$ of the solutions obtained by gradient descent match exactly our theoretical constructions. Although the global optimizers constructed only required a small number of hidden nodes, our analysis on gradient dynamics shows that overparameterization asymptotically decouples training dynamics and is beneficial. We further show that training dynamics favors simpler solutions under weight decay, and thus high-order global optimizers such as perfect memorization are unfavorable.\fi

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper introduces CoGO (Composing Global Optimizers), a theoretical framework for analyzing how 2-layer neural networks learn group operations with quadratic activation and L2 loss. The key insight is discovering a semi-ring algebraic structure in the solution space that allows the construction of global optimizers by composing partial solutions. The authors prove that the weight space has a semi-ring structure and that the loss function consists of monomial potentials with ring homomorphism properties. They also analyze training dynamics to explain why networks prefer simpler Fourier-based solutions over perfect memorization. The theoretical predictions align well with empirical results, showing that about 95% of gradient descent solutions match their constructed solutions.

### Strengths
- The work provides theoretical insights into neural network learning mechanisms for group operations. The discovery of algebraic structures (semi-ring) in the weight space and monomial potentials in the loss function offers a fresh perspective on how networks learn structured tasks. 
- There's strong empirical validation of the theoretical results. As shown in Table 2, around 95% of gradient descent solutions exactly match their theoretical constructions, with very small factorization errors. This provides concrete evidence that the theoretical framework accurately captures the learning behavior.
- The analysis of training dynamics (Theorem 5 and 6) provides insights into why networks prefer low-order Fourier solutions over perfect memorization. The paper shows that gradient descent with weight decay naturally favors simpler solutions due to topological connectivity between different-order solutions, which is an interesting finding.

### Weaknesses
 - My major concern is that the loss decomposition approach (Theorem 1) seems limited to scenarios where we already understand the underlying group structure of the data. The paper doesn't address how this framework might generalize to real-world scenarios where the data's algebraic structure is unknown or unclear. This limits the practical applicability of the theoretical insights, e.g., can we decompose the next token prediction loss easily?
- While the training dynamics analysis (particularly around Fourier feature learning and Theorem 5) is interesting, [1] also introduced that the NN prefers to learn Fourier features by gradient descent. Can the author give a more detailed comparison of connections and differences to [1]? The paper could better contextualize its findings with existing work by providing a more detailed comparison of the mechanisms and insights, which would strengthen the paper's contribution. 
- The paper mentions connections to grokking in the Conclusion but doesn't fully explore this direction. It would be good to discuss more, e.g., why there is a gap between train loss and test loss in the beginning under the paper’s analysis framework. Given that grokking is a significant phenomenon in neural network learning, especially for arithmetic tasks, a more detailed discussion of how CoGO might explain or relate to grokking would enhance the paper's impact.

### Questions
See the Weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This work considered 2-layer neural networks with quadratic activation and L2 loss on learning group multiplication (an extension of modular addition). It showed that global optimizers can be constructed algebraically from small partial solutions that are optimal only for parts of the loss, due to (1) a semi-ring structure over the weights space and (2) L2 loss being a function of monomial potentials allowing composition of partial solutions into global ones. (2) is shown by representing the network weights and then the loss function using Fourier bases. 

It then proposed a systematic approach using the above algebraic structure to construct global optimizers. It used this theoretical framework named CoGO to construct two distinct types of Fourier-based global optimizers of per-frequency order 4 and 6, and a global optimizer of order that correspond to perfect memorization. It empirically showed that most solutions via gradient descent match such constructions. It also analyzed the gradient dynamics, showing that it favors simpler solutions under weight decay, and that overparameterization asymptotically decouples the dynamics.

### Strengths
- The work provided a new angle on analyzing the global optimizers for the considered algebraic problem. It analyzed algebraic properties of the weight space and the loss, and then gave sufficient conditions for the global optimizers. 
- The study is quite solid and thorough. It provided detailed characterization of the sufficient condition, and also gave a systematic approach to construct global optimizers.

### Weaknesses
 - The theoretical setup is quite specific: quadratic activation and learning group multiplication. While the analysis is interesting, it is unclear if the results can provide insights into more general settings, in particular those more related to practical scenarios. The work can be strengthened if it can provide some empirical study on more realistic datasets verifying the insights (ie composition structure of the solutions), or provide generalization to more general settings (at least discussion about potential generalization and why).
- The global optimizers constructed by CoGO is only a subset of all possible global optimizers, so the approach only partially characterizes the problem solutions. This weakens the contribution a bit, though the work does provide empirical evidence that most practically obtained solutions are in their construction. 
- The presentation can be improved. See several comments below.

### Questions
- Line 140: Should mention l[i] is the embedding of the true label for the i-th data point.
- Line 145: I guess l[i] should be the in d-dimension, ie, the embedding of the element g_1[i] g_2[i], rather than the element itself. 
- Line 145: How is g_1[i] g_2[i] embedded into l[i]? g_1[i] is using U_{G_1} and g_2[i] is using U_{G_2}, while it's unclear how l[i] is obtained.
- Experiment: how to generate the training data (ie how g_1[i] and g_2[i] are sampled)? The data distribution can significantly impact the solution reached by training, so it needs to be specified for interpreting the empirical result that most solutions reached in experiments match the theoretical construction.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The work analyzes the 2-layer network training dynamics when learning Abelian group multiplication. Gradient descent matches an analytical solution for optimality.

### Strengths
Studies a simple and interesting class of neural networks. 
Proves many nice properties of a new mathematical space.
There is probably a nice interpretation of the construction of the solutions in Section 5.2 (but a weakness is that I don't see this expressed in a simple way). Interesting results about behavior of gradient descent in Section 6.

### Weaknesses
Numerous grammatical errors ("which are ring homomorphism", "goes to infinite", "is called semi-ring"...)
On the whole, the presentation of technical results is not clear enough to get a good picture of what is happening mathematically.

What is l[i] in (1)?
Is it important in Section 4.1 that you are looking at solutions in a weight space, or can they just be any fixing of parameters?
Doesn't the loss function itself change when you change the shapes of the parameters?

Clarify the relationship between Input and Output paragraph with what follows.
Be consistent with subscripts with commas or multindices. I'm confused now if they have different meanings.
Clarify the construction alluded to at the beginning of 5.1.
The relationship between weights, w, z, and r should be better clarified. This seems to me like a lot of notation and I don't have the intuition to understand the claims.
Please also explain the essence of the constructions of solutions in 5.2. What is really "going on"?

### Questions
What is l[i] in (1)?
Is it important in Section 4.1 that you are looking at solutions in a weight space, or can they just be any fixing of parameters?
Doesn't the loss function itself change when you change the shapes of the parameters?

Clarify the relationship between Input and Output paragraph with what follows. 
Be consistent with subscripts with commas or multindices. I'm confused now if they have different meanings. 
Clarify the construction alluded to at the beginning of 5.1. 
The relationship between weights, w, z, and r should be better clarified. This seems to me like a lot of notation and I don't have the intuition to understand the claims. 
Please also explain the essence of the constructions of solutions in 5.2. What is really "going on"?

### Soundness
3

### Presentation
2

### Contribution
4
