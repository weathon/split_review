# Episodic Memory Theory for the Mechanistic Interpretation of Recurrent Neural Networks

- Decision: Reject
- Scores: 5, 5, 6, 1

## Abstract
Understanding the intricate operations of Recurrent Neural Networks (RNNs) mechanistically is pivotal for advancing their capabilities and applications. In this pursuit, we propose the Episodic Memory Theory (EMT), illustrating that RNNs can be conceptualized as discrete-time analogs of the recently proposed General Sequential Episodic Memory Model. To substantiate EMT, we introduce a novel set of algorithmic tasks tailored to probe the variable binding behavior in RNNs. Utilizing the EMT, we formulate a mathematically rigorous circuit that facilitates variable binding in these tasks. Our empirical investigations reveal that trained RNNs consistently converge to the variable binding circuit, thus indicating universality in the dynamics of RNNs. Building on these findings, we devise an algorithm to define a \textit{privileged basis}, which reveals hidden neurons instrumental in the temporal storage and composition of variables — a mechanism vital for the successful generalization in these tasks. We show that the privileged basis enhances the interpretability of the learned parameters and hidden states of RNNs. Our work represents a step toward demystifying the internal mechanisms of RNNs and, for computational neuroscience, serves to bridge the gap between artificial neural networks and neural memory models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a mathematical formulation on linear (and potentially non-linear) RNNs to analytically track the storage of all relevant memories in a human interpretable manner. The authors frame this as "Episodic Memory Theory" or EMT. The authors propose a variable binding mechanism, and found that when training RNNs on repeat-copy and compose-copy tasks, the solutions exhibit the theoretically predicted behavior.

### Strengths
The mathematical formulation on interpreting internally-stored variables in RNNs is novel and insightful. This work provides an important new tool for the mechanistic deconstruction of RNNs. The most impressive result of the paper is that trained RNNs converge to some intended mechanism, suggesting that the mechanism the authors have found is very likely the most optimal solution for the cost function.

### Weaknesses
I have several major issues with this work, as detailed below.

(1) While the mathematical formulation is meaningful, I believe this is not episodic memory (and this proposed method is not a theory of episodic memory). The model and mathematical framework may be inspired by episodic memory models, but the task, objective and entire narrative is largely unrelated to episodic memory. RNNs receiving variable inputs, performing computations based on those variable inputs, and subsequently producing an output is straightforward decision-making or information-processing in many cases, including this work. This is further supported by Figure 1, where performing an addition operation is merely a simple computation that does not even require any memory storage or retrieval. Knowing how to add is not episodic memory. I am open to discussion if the authors still feel it is correctly defined.

(2) The way the entire paper is structured is unnecessarily confusing. I can summarize the work in the following manner:
- Consider an input vector with $d$ dimensions that spans $s$ timesteps, with a total of $sd$ input elements
- The number of neurons in the RNN needs to be greater than $sd$ otherwise superposition effects will occur
- The authors perform a change of basis such that the first $sd$ elements of the latent activity within the RNN now represent the (human interpretable, one-to-one mapped) input sequence with some shifting. This is referred to as "variable memory" by the authors (which is well-named and easily understood if not convoluted by the hard-to-parse narrative leading to its definition).

Right now a reader requires knowledge in RNNs and their applications in neuroscience, as well as some experience in mathematical tools commonly found in modern physics to fully understand the work, when in reality this paper could be written to a pure RNN audience without the Dirac and Einstein notations (at least in the main text), by simply stating that information about the latent is being carefully tracked by a basis transformation and formulating the equations in that context.

(3) The effects described in Figure 3 and 4A are specific to the repeat-copy task. More complex tasks (especially those with non-periodic solutions) may result in weight matrices that are not interpretable or offer any additional insight. Similarly, the compose-copy task, which is surprisingly never defined in this paper (but can be inferred from the Figure 4B to be generating the sequence one unit at a time), is the only task that will give rise to such interpretable values. In general, the authors summarize this class of tasks as $f$ in equation (2). The intended narrative is that the authors are using a class of tasks to elegantly highlight the feature of the proposed method, but my impression is that the method will not be producing anything meaningful beyond this class of tasks.

### Questions
See weaknesses.

### Soundness
1 poor

### Presentation
1 poor

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
The authors frame RNNs as episodic memory retrievers and use this to devise a circuit mechanism that could carry out sequential memory tasks. They show that this circuit mechanism seems to appear in trained networks.

### Strengths
The paper attempts to bring several different topic areas together, which is admirable.

The potential applications listed for this work would be useful if achievable. 

 The work is thorough.

### Weaknesses
I struggled to read this paper at several points. It is pulling concepts from many different fields and also I believe trying to introduce new ones. I'm also not well versed in the specific notation used. I don't want to down-score work for being too interdisciplinary, but as the paper stands now I don't know if there is a large community who would be able to understand and benefit from it as a whole.

The tasks (insofar as they are described) seem like weak, or at least very specific, tests of variable binding. For the authors to make claims about variable binding in general, they would need to show tasks that do more than just require sequential repeats of the input. Specifically, the tasks appear to only test the ability to recall a sequence of inputs, rather than the more general ability to bind variables to different roles or slots, which is a core feature of variable binding in cognitive architectures. The current tasks could be solved by a simple delay line or a system that simply replays a recorded sequence, without any true variable binding mechanism.

A substantial issue for me is that I am confused about the elements that the authors label as being novel here. Most of them are, at least at a broad level, well-represented in the neuroscience-inspired RNN literature. For example, the authors say in the discussion:

we provide "a novel perspective on Recurrent Neural Networks (RNNs), framing them as dy-
namical systems performing sequence memory retrieval". The original Ellman model itself uses RNNs for a form of sequence memory retrieval, but also several more recent works study serial working memory with RNNs such as: https://direct.mit.edu/neco/article/30/6/1449/8400/A-Theory-of-Sequence-Indexing-and-Working-Memory and https://psycnet.apa.org/record/2006-04733-001

"We introduced the concept of “variable
memories,” linear subspaces capable of symbolically binding and recursively composing informa-
tion."  The notion of storing different items in different linear subspaces has also been explored: https://www.science.org/doi/10.1126/science.abm0204

"We presented a new class of algorithmic tasks that are designed to probe the variable binding
behavior of RNNs. " As represented by the above studies on serial working memory, this class of tasks is not new. 

"for the first time, revealed hidden neurons actively involved in in-
formation processing in RNNs. " This is obviously not the first time people have studied how neurons process information in RNNs (see the work of Omri Barak and David Sussillo, e.g.).

On the whole I also don't see the specific value in claiming that this analysis is related to episodic memory. Sequential memory, yes. But there is nothing specifically episodic about the motivation for the analyses and the tasks represent serial working memory.

### Questions
What are the tasks? One is described in the main text and another mentioned in the appendix. All 4 should be described in the main text. 

I thought u(t) was the input vector, which is 0 for t>s, yet Eqn 2 shows the evolution of u(t) for t>s. 

The authors say:

"The mechanistic interpretability seeks to reverse-engineer neural net-
works to expose the underlying mechanisms enabling them to learn and adapt to previously unen-
countered conditions"

and

" This assumption limits the mod-
els’ applicability to mechanistic interpretability, which requires the symbolic binding of memories
typically available only during inference."

Why are they focusing on mechanistic interpretability for such a limited behavior? As I understand it MI can be used to explain any behavior of a neural network.

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper develops the Episodic Memory Theory (EMT), where a circuit mechanism is presented to illustrate how a linear RNN recursively stores and composes hidden variables. The authors show that, under specially designed algorithmic tasks called *variable binding*, the hidden neurons and the learned parameters of a trained linear RNN can be illustrated by *variable memories* $\Psi$, which are a group of interpretable bases. They also design an operator $\Phi$ to form a circuit computation of variable memories $\Psi$. Finally, they propose a power iteration-based algorithm to find the bases $\Psi$ via the learned RNN parameters. In the experiment, the authors show the variable memories $\Psi$ could reveal the information stored in the hidden states of a linear RNN. They also provide examples of how such bases $\Psi$ enable human interpretability of learned RNN parameters.

### Strengths
* Proposes a novel basis (variable memory $\Psi$) that, for the first time, reveals hidden neurons actively involved in information processing in a linear RNN.

* Using the basis to interpret the learned parameters of a linear RNN in a  human-friendly way.

### Weaknesses
 * Only a Repeat Copy task is shown to reveal the stored information in hidden neurons. As the authors mentioned in section 7.3, there are some cases in which the computed basis is converged, but it cannot give interpretable representations. In other words, under which tasks do we expect this framework to fail? Specifically, what properties of a task or the learned RNN parameters would cause the power iteration method to converge to a basis that does not correspond to interpretable variable memories? It is unclear if the method fails because the theoretical basis is not present, or because the algorithm fails to find the basis, and this distinction needs to be clarified.

* Typos: The first sentence below Equation 6 should be "Figure 2A".

* > This deviation from the theory is a result of the sensitivity of the basis definition to minor errors in the pseudo-inverse required to compute the dual.

* What is the meaning of "dual"? is this related to the conjugate transpose computation $EE^{*}$ in Algorithm 1?

* Could you please discuss in detail the difficulties of applying the proposed theory to nonlinear RNNs? In Appendix A.4, you have shown that a nonlinear RNN has a similar form of the linear system as linear RNNs instead of a different $W_{hh}$. Specifically, what are the limitations of the Taylor expansion approximation used for nonlinear RNNs?  Are there specific nonlinear activation functions or network structures for which this approximation is likely to fail, and how would that manifest in the computed variable memories?

### Questions
* > This deviation from the theory is a result of the sensitivity of the basis definition to minor errors in the pseudo-inverse required to compute the dual.

* What is the meaning of "dual"? is this related to the conjugate transpose computation $EE^{*}$ in Algorithm 1?

* Could you please discuss in detail the difficulties of applying the proposed theory to nonlinear RNNs? In Appendix A.4, you have shown that a nonlinear RNN has a similar form of the linear system as linear RNNs instead of a different $W_{hh}$.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors employed a linear RNN to execute a task called VARIABLE BINDING. They utilized linear algebra to illustrate the process of extracting outputs from the network.

### Strengths
The specific sections of the article that describe what was done are relatively clear.

### Weaknesses
There are three main drawbacks:

1. The current analysis is overly limited. It applies solely to a single-layer RNN with linear dynamics. The assertion that any general RNN can be treated as a linear RNN in A.4 is fundamentally incorrect. In reality, a general RNN may not behave near a fixed point, resulting in significant higher-order terms. Furthermore, the analysis pertains to a task, the VARIABLE BINDING TASK, which is notably distinct from a translation task. The linear analysis, while mathematically tractable, neglects the crucial non-linear interactions that are essential for the complex dynamics observed in many RNN applications. This limits the applicability of the findings to real-world scenarios involving more complex, non-linear RNNs. The chosen task, while useful for isolating specific mechanisms, does not reflect the challenges of tasks like translation, which require learning complex, long-range dependencies.

2. The current analysis lacks novelty. The article primarily employs linear projection techniques to examine the components of RNN weights, a methodology that has been in use for a considerable period. The use of linear algebra to analyze RNNs is not new, and the specific techniques used here, such as projection onto subspaces, have been well-established. The paper does not introduce a novel way to analyze RNN weights or provide a new theoretical framework for understanding the dynamics of these networks. The analysis seems to be a straightforward application of existing linear techniques to a specific task, without providing significant new insights.

3. The presentation lacks clarity. Figures 1 and 2 are difficult to comprehend, and their intended message is unclear. Additionally, the mention of GSEMM seems unnecessary since the current work solely involves a simple linear RNN. There is a lack of a concise summary of the core mechanisms of the RNN. The figures lack clear labeling and explanations, making it difficult to understand their relevance to the analysis. The connection to GSEMM is not well-motivated, and the paper does not clearly explain why this concept is relevant to a simple linear RNN. The core mechanisms of the RNN are not clearly articulated, and the reader is left without a clear understanding of the key insights.

### Questions
See weakness.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor
