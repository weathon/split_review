# Inverse Approximation Theory for Nonlinear Recurrent Neural Networks

- Decision: Accept
- Scores: 5, 8, 8, 8

## Abstract
We prove an inverse approximation theorem for the approximation of nonlinear sequence-to-sequence relationships using recurrent neural networks (RNNs). This is a so-called Bernstein-type result in approximation theory, which deduces properties of a target function under the assumption that it can be effectively approximated by a hypothesis space. In particular, we show that nonlinear sequence relationships that can be stably approximated by nonlinear RNNs must have an exponential decaying memory structure - a notion that can be made precise. This extends the previously identified curse of memory in linear RNNs into the general nonlinear setting, and quantifies the essential limitations of the RNN architecture for learning sequential relationships with long-term memory. Based on the analysis, we propose a principled reparameterization method to overcome the limitations. Our theoretical results are confirmed by numerical experiments.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors provides an inverse approximation theory for a certain class of nonlinear recurrent neural network (RNN), showing that, for the class of nonlinear RNN to approximate the sequence, the sequence should have an exponential decaying memory structure. It demonstrates the difficulties of RNN in learning and representing a longer-time dependence in the data.

### Strengths
The paper is relatively well written and it extends the previous theories in linear RNN. While heuristically it is not difficult to show that a popular RNN, such as LSTM or GRU, has an exponentially decaying memory, by approximating the internal state of the RNN with a relaxation equation, this manuscript provides a robust proof about such behavior.

### Weaknesses
While it the manuscript is clearly written with well defined problem set up, my concern is the fit to the scope of ICLR. On one hand, I believe that the analysis and definitions provided in the manuscript can be of interest in developing theories about RNN. On the other hand, the scope of the manuscript is too narrow and it is unclear what insight this study provides to benefit a broader class of RNNs or Deep Learning in general. I believe that the authors need to consider giving more insights from their results for a broader context. The stable parameterization section is not very convincing. Can you give a more concrete example about the effects of the reparameterization? Possibly, using a dynamical system or real data?

### Questions
NA

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper demonstrates a Bernstein-type result for nonlinear Recurrent Neural Networks, meaning that it characterizes the type of functions that can be approximated by RNNs. The result shows that if a target sequence can be approximated by a RNN, then it has an exponentially decaying memory (for a notion of memory made precise in the paper). A similar result was proven in the literature for linear RNNs and this paper extends the result to the non-linear case.

### Strengths
The paper is well presented and pleasant to read. Extending previously known results to the non-linear case is interesting and brings added value. It gives a theoretical framework to understand the common saying that RNNs are unable to learn long-time dependencies in time series. A modification of the parametrization of RNNs is proposed to remedy this problem.

Technically, the paper introduces a new notion of memory that holds for nonlinear functionals and which extends the linear case, as well as a notion of stable approximation (which corresponds to the existence of a ball of parameters with uniformly good approximation properties). This proof technique is interesting and could perhaps be applied to other architectures.

Experiments support the theoretical findings.

### Weaknesses
I have no strong reservations about the paper. I do have a question about Figure 3, which I did not understand. I am willing to raise the rating should this interrogation be answered. [Update on Nov. 18: the authors clarified this point in their comments below, and I updated my rating accordingly].

I do not understand the filtering part of the experiment. Since we know from the theoretical results that RNNs can only represent exponentially decaying functions, the teacher models should all be exponentially decaying? So why is any filtering required? Furthermore, if indeed filtering is required, is it also performed before plotting the left-side plot? Otherwise we should be seeing some non-converging data points?
As a consequence, I am wondering if the takeaway of the experiment should be “stable approximation implies exponential decay” or rather “exponential decay implies stable approximation”.

**Minor remarks that do not influence the rating**
+ Page 5: I found the paragraph above Definition 3.2 hard to follow. I am not sure to understand the reason for introducing the terminology  “queried memory”. The experiments of Appendix B are important in my opinion because they suggest that RNNs may share the exponential decay property with LSTMs, but not Transformer. But I do not understand why they are introduced at this point in the paper, and not later on, e.g. in the conclusion.
+ Page 7: the proof sketch is difficult to follow, and I am not sure it brings significant added value. If you need additional space in the main paper, I’d suggest putting the proof sketch in the Appendix just before the proof.
+ Page 7, line -2: “In order” -> “in order”
+ Page 8: “approaching 0” -> “approaching 0 on the negative side”?
+ Page 8: “Take exponential…” -> “Taking exponential”
+ Page 8, figures 2 and 3: please avoid using plus sign and arrow inside the text. Consider replacing it by “and” and “implies”.
+ Page 16: “acivations” -> “activations”
+ Page 16: could you briefly explain or give a reference for Lyapunov equations?

### Questions
Do the authors think their proof technique could also be applied to LSTMs/GRUs? I imagine there would be many technical difficulties, but conceptually do the authors think it would be possible? Giving this insight in the paper might be interesting for readers.

See also weaknesses.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
The paper introduces an inverse approximation theorem for non-linear recurrent neural networks, extending known, results for the linear case. After introducing new tools that enable analyzing nonlinear dynamics, it shows a somewhat negative result that nonlinear RNNs suffer from the same curse of memory as linear RNNs. Finally, the authors suggest a type of reparametrization that could possibly enable stability and good approximation properties.

### Strengths
As an outsider to the field, the paper introduces/uses formal concepts that I find insightful:

- The memory function that is used in the paper mathematically characterizes the intuitive behavior of RNNs.
- The notion of stable approximation is an interesting proxy for how a function can be learned by gradient descent which, from my very limited knowledge, seems to be rare in approximation theory.

Overall, I found overall the paper well written, in a way that is accessible to a decently large audience.

### Weaknesses
I am not qualified enough to identify the weaknesses of the paper.

### Questions
I am a bit confused with the Heaviside input at the end of Page 4. Intuitively, I would have put it the other way around: the network is submitted to an input $x$ until 0, and then evolves autonomously later. This would allow us to measure how fast the network forgets about $x$. Can you elaborate on the choice in the paper?

The reparametrization that you propose reminds me of the one used in the LRU architecture (Orvieto et al. 2023, ICML) and present in some deep-state space models (see references in the LRU paper), it may be nice to mention this. I’m not sure I fully understand what your theoretical results show for the reparametrization. To the best of my understanding, even with such a reparametrization, RNN would still only be able to learn in the same manner targets with decaying memory. Can you elaborate more on that?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper investigates the inverse approximation theory for nonlinear recurrent neural networks (RNN) and extends the curse of memory from linear RNNs to nonlinear RNNs. The contribution of this paper can be summarized as follows.
1. Authors define the memory of nonlinear RNNs, which is consistent with the memory of linear RNNs.
2. Authors introduce a notion of stable approximation.
3. Authors prove a Bernstein-type approximation theorem for nonlinear functional sequences through nonlinear RNNs, which says that if a target function can be stably approximated by nonlinear RNNs, then the target function must have exponential decaying memory.
4. Based on the theoretical result, the authors propose a suitable parameterization that enables RNN to stably approximate target functions with non-exponential decaying memory.

### Strengths
1. To the best of my knowledge, this is the first paper studying the inverse approximation theorem for nonlinear RNNs.
2. The approximation of neural networks determines the existence of a low-error solution and has been widely investigated. The inverse approximation theorem, which is harder and less studied, concerns the efficiency of approximation, which is a crucial aspect of utilizing neural networks in practice.
3. The nonlinearity is of central interest in empirical implementations and requires more challenging proofs.

### Weaknesses
1. The definition of memory for nonlinear RNNs is consistent with that for linear RNNs, but the rationality of the proposed definition needs more explanations. The authors review the definition of memory for linear RNNs and observe that if the memory decays fast, then the target has short memory, and vice versa. The observation can be obtained directly from the definition and satisfies the intuition of memory. But for the memory for nonlinear RNNs, authors motivate it from a derivative form. This motivation is too mathematical and lacks an intuitive explanation. What is the relationship between the decaying speed of memory and the dependence of the target function on early inputs? Specifically, while the derivative form is mathematically convenient, it's not clear why the response to a Heaviside input (or its derivative) is the most appropriate way to characterize memory in a general nonlinear RNN. The connection to more standard notions of memory, such as the influence of past inputs on current outputs, needs to be more explicit.

2. The parameterization motivated by the theories should be explained in more detail. The parameterization is based on an important claim that the eigenvalue real part being negative leads to stability, which is not explained in section 3. This makes the logic in section 3.4 incomplete and the parameterization hard to understand. Can authors provide an intuitive explanation for this? The paper states that eigenvalues with negative real parts are necessary for stability, but it does not explain why this is the case, especially in the context of nonlinear RNNs. Furthermore, the connection between the reparameterization and the ability to learn long-term dependencies is not clearly established. It's not immediately obvious how this parameterization allows the eigenvalues to approach zero without causing instability, and a more detailed explanation is needed to clarify this point.

### Questions
See weakness.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
