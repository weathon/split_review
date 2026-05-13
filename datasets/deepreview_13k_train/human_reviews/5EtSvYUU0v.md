# Connecting NTK and NNGP: A Unified Theoretical Framework for Neural Network Learning Dynamics in the Kernel Regime

- Decision: Reject
- Scores: 5, 8, 3, 8

## Abstract
Artificial neural networks (ANNs) have revolutionized machine learning in recent years, but a complete theoretical framework for their learning process is still lacking. Substantial theoretical advances have been achieved for infinitely wide networks. In this regime, two disparate theoretical frameworks have been used, in which the network's output is described using kernels: one framework is based on the Neural Tangent Kernel (NTK) which assumes linearized gradient descent dynamics, while the Neural Network Gaussian Process (NNGP) kernel assumes a Bayesian framework. However, the relation between these two frameworks and between their underlying sets of assumptions has remained elusive. This work unifies these two distinct theories using a Markov proximal learning model for learning dynamics in an ensemble of randomly initialized infinitely wide deep networks. We derive an exact analytical expression for the network input-output function during and after learning, and introduce a new time-dependent Neural Dynamical Kernel (NDK) from which both NTK and NNGP kernels can be derived. We identify two important learning phases characterized by different time scales: gradient-driven and diffusive learning. In the initial gradient-driven learning phase, the dynamics is dominated by deterministic gradient descent, and is adequately described by the NTK theory. This phase is followed by the slow diffusive learning stage, during which the network parameters sample the solution space, ultimately approaching the equilibrium posterior distribution corresponding to NNGP. Combined with numerical evaluations on synthetic and benchmark datasets, we provide novel insights into the different roles of initialization, regularization, and network depth, as well as phenomena such as early stopping and representational drift. This work closes the gap between the NTK and NNGP theories, providing a comprehensive framework for understanding the learning process of deep neural networks in the infinite width limit.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper explores the connection between deep neural networks and kernel learning. Specifically, the authors take a representation of the dynamics of evolution of the hyper-parameters in what is presumably a neural network and study the evolution of the kernel corresponding to the feature space. The authors show that the resulting kernel evolves from the NTK to the NNGP kernel (or at least that is my interpretation).

### Strengths
While there is obviously a significant body of work on convergence to the NTK, the connection from NTK to NNGP under stochastic noise is an interesting hypothesis. The authors explore the implications from several perspectives -- including testing the proposed NDK for different regimes and some interesting outcomes such as early-stopping and representation drift.

### Weaknesses
My major concerns with the paper are that the fundamental results are not rigorously established before proceeding to interpretation. This makes it hard to quantify or verify the claims. Specifically, the paper has no proofs or definitions which can be verified. There are many claims being made and several equations used to back up those claims. However, without rigorous definitions and statements to prove, it is difficult to verify these claims. In addition, the notation is inconsistent and meaning is unclear at times.

Specifically, the variable $\mathbf{u}(t)$ in Section 2.2 lacks a clear definition. What are the specific properties of $\mathbf{u}$ that allow Equation 5 to hold? The motivation for the NDK kernel in Equation 5 is not well-established, and the significance of the statistic $S$ is unclear. The inconsistent notation, such as $\nabla_\theta f(x, t)$ in Equation 6 and $f(x, \theta)$ in Equation 9, and the varying arguments of $K$, further obscure the presentation. The derivative in $\dot K(t,t',x,x')$ is not defined, making it difficult to interpret. Equation 16 requires more detail; if it is a standard NNGP result, the connection to NDK is unclear, and if it is a limit of Equation 13, this derivation should be included, especially given the dependence on $\mathbf{f}_{\text{train}}(t')$. The relationship between NDK and NTK when $t = t'$ is not well explained, and the comparison to NNGP equilibrium in Fig 2 is missing. The definitions of optimal early stopping and optimum generalization error are also unclear. The reference to closed-form expressions for kernel functions in the text is vague, and the supplementary information lacks context. Claims such as ``predictor converges fast to the desired'' and ``Our theoretical framework for the Langevin dynamics provides a model of representational drift'' are too vague. Finally, there is a margin violation on Eq 88.

### Questions
Some detailed notes and questions supporting the summary are as given below.

1) The authors make constant use of the first person plural in a way which does not encompass the reader. This makes it seem as if the paper were about the authors and not about the result.

2) Section 2.2 has a lack of definitions. For example, the variable $\mathbf{u}(t)$ --  what are the particular properties of $u$ for which  Equation $5$ holds?

3) Some motivation for NDK kernel is presented in Equation 5, but Equation 5 has not been properly introduced.  Authors should include at least basic information describing equation 5 in Section 2.2 and show why this statistic $S$ is important. 
    
4) There is quite a bit of inconsistent notation. For example, Equation 6 has a function $\nabla_\theta f(x, t)$ and then Equation 9 uses n $f(x, \theta)$. In another example, $K$ has variously four arguments and then three and then two.  

5) The authors often use $\dot K(t,t',x,x')$. But what is the derivative with respect to?
 
6) Equation 16 should be described in more detail. If Equation 16 is just a classical NNGP result, then the connection between NDK and NNGP is unclear. If Equation 16 is the limit of Equation 13, then this result should be presented in the paper as well, since Equation 13 depends on $\mathbf{f}_{\text{train}}(t')$.

7) If we consider $t = t'$ for NDK, how is the dynamic different from NTK? 

8) In Fig 2, it would be nice to add NNGP equilibrium for comparison.

9) How do authors define the optimal early stopping point and  optimum generalization error? 

10) The font of labels, legends and titles of all figures should be increased. 
    
11) ``All the kernel functions above including the two-time NNGP kernel, the
derivative kernel, and the NDK, have closed-form expressions for specific activation functions such
as linear, ReLU and error function (see SI Sec.C, Cho & Saul (2009)).'' -- which equations are the authors referring to?

12) Supplementary information such as Sec. B provides little to no explanation or context.

13) ``predictor converges fast to the desired''

14) ``Our theoretical framework for the Langevin dynamics provides a model of representational drift'' Which framework? The model? This is unclear.

15) Margin violation on Eq 88

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors study the learning dynamics of (regularized) infinite-width neural networks under Langevin dynamics (continuous stochastic gradient descent). They derive a new kernel termed the neural dynamic kernel (NDK) which exhibits both NTK and NNGP behavior in the limits. NDK can be thought of as the two-time extension of NTK under Langevin dynamics. Consistent with empirical results it explains two phases of dynamics, a deterministic gradient-driven phase (akin to NTK) followed by a diffusive phase exploring the solution space and approaching the posterior distribution of an infinite-width NN with Normal prior over the weights (akin to NNGP). Empirical results are in line with theoretical arguments and explore the two phases of learning dynamics as well as the effect of depth, temperature, initialization variance, and equilibrium variance. Furthermore, the authors use the theoretical framework and make connections to the representational drift phenomenon observed in neural systems which corresponds to the reorganization of synaptic weights while maintaining the behavioral performance in experimental tasks.

### Strengths
There has been a large interest in the behavior of overparameterized neural networks in the ML community. NTK and NNGP were introduced as two seemingly separate tools for studying the limiting behavior of infinite neural networks in the deterministic and Bayesian settings. While previous literature has pointed to connections between the two frameworks a clear unified framework for understanding the two didn't exist. This paper tackles this problem by introducing NDK and studying the limiting behavior.

The empirical results make the theoretical arguments very clear. Depicting the two phases of dynamics along with the limiting behavior of the models provides compelling evidence for the theoretical framework.

The connections to the neuroscience literature on representational drift are insightful and interesting (although this paper is not the first to make this connection and other papers in the literature on overparameterized neural nets already made this connection before) [1,2].

[1] https://arxiv.org/abs/2110.06914

[2] https://arxiv.org/abs/1904.09080

### Weaknesses
My main comment is about the introduction part of the paper which can be made more comprehensive. The literature on learning dynamics in overparameterized neural nets has progressed quite extensively and learning dynamics, and placing the work in the existing literature and recognizing existing contributions fairly will make the paper stronger. Specifically, the introduction should more thoroughly discuss the existing body of work on the connections between Neural Tangent Kernel (NTK) and Neural Network Gaussian Process (NNGP) regimes, and how this work fits into that landscape. The current introduction does not adequately acknowledge the nuances of the transition between these regimes and the various theoretical perspectives that have been proposed.

Although I think the two-time extension of NTK is a novel contribution, I’ve seen the one-time extension of NTK before (see e.g. Lemma 8.1.1 of [1]). In fact, the development of the NTK is the consequence of the limiting behavior of this one-time extension. The authors should clarify the distinction between their two-time kernel and the existing one-time extensions, and emphasize the novel aspects of their approach. The current discussion does not fully highlight the specific mathematical differences and the implications of using a two-time kernel.

The authors cite a paper that discusses the diffusive properties of Langevin dynamics in the long-time limit. Another paper that discusses this diffusive behavior under learning using SGD is [2]. It appears to me that this is not a novel finding as it was reported before and it's a phenomenon that's already justified using theoretical arguments. Although this paper provides a unique perspective connecting NTK and NNGP using NDK I would frame the diffusive behavior of the SGD as a confirmation of the existing literature rather than a novel finding. The authors should more clearly position their work in relation to these existing results, and emphasize the specific contribution of their analysis beyond simply observing the diffusive behavior.

### Questions
- Can the authors discuss the extensions to multivariate outputs?
- Can the framework be extended to different forms of regularization? Specifically, do we expect to observe the diffusive behavior and the limiting posterior distribution of a Bayesian model with a different prior under a different regularization (e.g. l1 regularization)?
- The authors argue the relevance of SGD in the context of batch learning, does this framework have the potential to explain other tricks used in the learning of neural nets such as dropout, batch-norm, etc.?
- Can we derive bounds w.r.t. the number of iterations, depth, number of training samples, etc. on when to expect to observe the transition from phase 1 to phase 2 and use that as the early stopping criterion?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a generalized framework, that includes the Neural Tangent Kernel and the NNGP as special cases. This is facilitated by adding a noise term to the training dynamics (Langevin equations), and then expressing the predictor moments in the infinite-width limit as path integrals over the Langevin trajetories. Theory and experiments investigate training dynamics, finding a gradient-driven phase (NTK) and a diffusion-driven phase (NNGP in long-term equilibrium) in time. Generalization experiments in a classification task then show how noise-related hyperparameters related to initialization and regularization allow to trade the time scales of the two distinct phases against each other. The role of depth and non-linearity is briefly discussed. Lastly, the findings are related to a hypothesis of read-out weight realignment, which was proposed for explaining representational drift observed in neuroscience. For this, the read-out weights are frozen after sufficient training, while the hidden weights are allowed to further diffuse. Experiments show that, depending on whether the kernel is meaningful for the task, the outputs of training and test data decorrelate over diffusion time.

### Strengths
(1) A generalized framework is proposed, incorporating both NTK and NNGP. This is highly relevant, as both frameworks have led to major insights into NN theory. Such a generalized framework is of utmost importance and may lead to further novel deep insights.
(2) The approach through treating the necessary noise-injection via Langevin dynamics and path integral formulations is novel and innovative, and may pave the way for a new tool to investigate learning systems via kernel representations. The trick with the markov proximal learning together with the replica trick may even be applied to much more general learning systems.
(3) Interesting original experiments are shown

### Weaknesses
 (1) Clarity / presentation seems a bit unfocused or maybe even unripe. E.g. the paper's main theoretical result is Eq. 5, only which then allows to elucidate the relations to NNGP and NTK. This Eq. 5 is formulated in terms of random variables \vec{v} and \vec{u}. While \vec{v} is briefly described in prosaic manner, \vec{u} is not explained at all. It is burried deep in the supplementary. Another example is the statement in some regime "the integral equation can be transformed into a linear ODE". This should be supported/elaborated, and if done so in the supplementary, it needs a precise pointer where at exactly. Another example is that the Appendix A is never mentioned anywhere, albeit a major aspect of the theory outlined in Appendix B, as otherwise the path integrals cannot be easily factorized. The paper's originality and meaning is difficult to understand without studying the supplementary in detail.

 (2) In the revised version, the main theoretical result eq. 5+6 introduces a "field coupled to the predictor \ell(t)". No notion is given what this means, what this field is, what the coupling looks like, or why it is important / necessary. It then appears again later somewhere in the body of the supplementary as \ell_t around eq. 30 (eq 27 in old version), which is the first point where one gets an idea of what this object is.

 (3) These equations have actually changed from the last version. Why? (\tilde u instead of u)

 (4) In these equations, an object m(t,t') is used to define the action. Only a couple of equations and one section later, m(t,t') is actually introduced, and only in the context of having introduced the kernel already. While this is clearly simple to fix, it exemplifies the early stage of this manuscript's presentation.

 (5) A minor effort has been made to clarify the introduction of the auxiliaries u(t) and v(t), but still not clear.

### Questions
(1) Figure 3 is not clear, can you kindly add some more explanations esp. wrt. early stopping and what you mean with it precisely
(2) In the main body (introduction), it is stated that the infinite-width limit is pursued but without requiring the amount of data to scale as the width of the NN. I.e. with finite data. This is the typical NTK or NNGP regime. However, for the main result eq. 5 the replica method is used. To my understanding, the replica method typically relies on a scaling of the data with the NN width. However, the necessity of an infinite-data simultaneous limit is never discussed in the main paper, but is also clearly departing from NTK and NNGP. This seems to indicate a contradiction or at least creates confusion. Please clarify.
(3) In SI eq. 27, the exchange of integral and product of d\theta_\tau is done one line too early.

### Soundness
3 good

### Presentation
1 poor

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The submission introduces a generalised kernel - Neural Dynamic Kernel (NDK)  for stochastic gradient for very wide (infinite) neural networks. The Neural Tangent Kernel (NTK) and Neural Network Gaussian Process Kernel (NNGP) are two different timescale limits of the NDK - the NTK on the early training as deterministic gradient driven and the later driven by diffusion. 

The NDK kernel different from the earlier Kernels as it is explicitly time dependent, and allows, in the short time scale and long time scale limits two different,  NTK (deterministic)  and NNGP (diffusive), like behaviours - the main contribution of the paper. 

The argumentation in the appendixes is thorough, and the trial cases support the conclusions.

### Strengths
Clear representation, with excellent narrative in the appendixes. These support the main text that concentrates nicely on the main line of thought. Some results are surprising like the different qualitative behaviours of the kernels in the one layer and two layer cases.

### Weaknesses
The meaning of  time dependence of the NDK kernel would need discussion.  Already the learning rate of the stochastic gradient is tuned and this is essential for the minimising algorithm to work. Now, two different domains arise when the gradient is big and one is far for the optimal point - it is good to move with big steps down the slope. At the bottom, the finite time step size, in gradient decent, will lead to diffusive Brownian motion around the minimum until the learning rate shrinks to zero. This behaviour is more a property of the stochastic gradient than a property of the neural networks themselves.

As discussed in the manuscript, the practical trials of the Kernel have to be performed (like the Langevin equation) with discretised time. The discretisation errors will lead to extra diffusive contribution and to the above description - unless a hybrid Monte Carlo is used where the evolution of differential equation is proven to be ergodic and reversible. Hence, we cannot easily distinguish the root cause of the phenomenon. There is no clear indication if the behaviours of the Kernels are coming from the structure of the model, or the structure of how it is solved.

 The behaviour of the gradient in closing in is often reflecting a saddle point type of manifold, where there may be steep slopes in the loss function that will not necessarily depend on how close you are off the minimum. To remedy this, one is often using caps on the size of the gradient to keep the SGD loss smooth. Of course, the flatness of the gradients would provide robustness for the inference, so there are benefits in trying to achieve it. In fact, this can be achieve by introducing Hessian dependence into the training loss. Why would you expect a smooth gradient close to the minimum by default?

### Questions
How would a given learning rate profiles influence your conclusions? I think a nonlinear time variable would do the trick. Can it change the qualitative behaviour as well, as the time dependent NDK?

The large N limit, with data size fixed to finite value leads automatically to overfitting, as the weights of the connection to the a neutron are a template of the input. With random weights of infinite extent, there will always be a fitting template for a particular data item. Generalisation suffers, as it would require an efficient compression that finds common templates for multiple data items. In the infinite N limit, this does not happen. Is there a way to look at the large N limit in such a way that one also includes the interesting large data limit?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
