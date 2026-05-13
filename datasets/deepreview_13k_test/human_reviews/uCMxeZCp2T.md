# Nature-Inspired Local Propagation

- Decision: Reject
- Scores: 5, 6, 1, 5

## Abstract
The spectacular results achieved in machine learning, including the
recent advances in generative AI, rely on large data collections. On the
opposite, intelligent processes in nature arises without the need for such
collections, but simply by on-line processing of the environmental information.
In particular, natural learning processes rely on mechanisms where data
representation and learning are intertwined in such a way to respect
spatiotemporal locality. This paper shows that such a feature arises from
a pre-algorithmic view of learning that is inspired by related studies
in Theoretical Physics. We show that the algorithmic
interpretation of the derived ``laws of learning'', which takes the structure
of Hamiltonian equations, reduces to Backpropagation when the speed of
propagation goes to infinity. This opens the doors to 
machine learning studies based on full on-line information processing
that are based the replacement of Backpropagation with 
the proposed spatiotemporal local algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
1: You are unable to assess this paper and have alerted the ACs to seek an opinion from different reviewers.

### Summary
The paper develops a spatiotemporal local learning rule. To develop it authors treat a learning rule as a solution to a variational problem for the special class of functional that can be solved using Hamilton's equations. The authors show how this rule can be reduced to backpropagation and to backpropagation with momentum as specific cases.

### Strengths
I can not describe strengths and weaknesses based on my current understanding of the paper. I hope I will update these sections when the authors answer my questions. 

Please see the questions section.

### Weaknesses
--

### Questions
1) Can you elaborate more how Corollary 1 can be viewed as backpropagation and Proposition 4 as GD with momentum?
2) Can you recommend an open source to understand how Corollary 1 can be viewed as backpropagation along with the Gori et al. (2023)?
3) Can a different choice of \phi lead to different learning rules in Proposition 4? Or does it lead only to different schedules for momentum? 
4) Can you write algorithms for the proposed learning rules (including sign flipping algorithm)?
5) Can you motivate the form of functional in Eq. 8? Specifically, why regularization on weight acceleration is important?
6) How q x^2 /2 can be interpreted as the accuracy term in Section 4.2?
7) What are z, u and x in Fig. 1-4? z is target, x is a vector predicted with LSTM, and u is input? I failed to see how objectives in section 4.2 encourage x to be close to z. Can you elaborate on this? 
8) You mentioned that the proposed algorithm overcomes the limitation of backpropagation through time, but at the same time the algorithm converges to backpropagation when c → to infinity. Can you elaborate on this?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a framework that treats an online learning setting for RNNs as a variational problem and allows to look at backpropagation as a special case. They use the Hamiltonian equations to represent the minimality conditions and propose an approximation method for the problem with boundary conditions. 

**Disclaimer**: This paper is quite far from the area of my expertise (reinforcement learning, graph neural networks), and I won't be able to assess the technical excellence of the work,  I have not checked the proofs. However, I still think my review can be useful to the authors as an outsider's view, especially as the authors state in the conclusion that "the application to real-world problems need to activate substantial efforts on different application domains." Therefore, while not being totally ignorant in dynamical systems / optimal control, I ask the AC take my review as an evaluation of paper's readability and accessibility for the non-theoretical researchers that will potentially widen the target audience. I will also reflect this in the 'Confidence' section. For the time-being, I will put the score as 6, and, might update it post-rebuttal after engaging with the authors and other reviewers.

### Strengths
The framework proposed by the paper connects several seemingly unrelated concepts and allows to look at the commonly accepted things from a totally different angle (e.g. backpropagation).

### Weaknesses
* **Clarity**. While paper pays a lot of attention to careful notation and definition of the computational model, some of the concepts come out of the blue, either undefined or defined much later into the paper.
	* I understand that some of the concepts are not defined as they are common knowledge in the field (e.g. costates). However, my comment above is not only about those (see below)
	* What is pre-algorithmic view?
	* 'spatiotemporal locality' comes up already in the abstract/intro, but gets defined much later after all the computational model formalism is done.
	* I don't think, IN^i from (5) is defined.
* **Lack of examples**. I understand that it is common in the theoretical community to define things in a most general way possible. However, I think it will be highly beneficial to bring parallels to the machine learning case by giving examples even for the variables involved. For example, $l(w, x, t)$ comes up in equation 8, but only much later (Theorem 2 at the bottom of next page) the paper mentions that this can be a sum of the regularisation term and an indicator function on the neurons outputs multiplied by some function L, i.e this is a loss function! Same applies to other variables, e.g. $\xi$ and $\mathbf{u}$. Section 2 defines $u$ as d-dimensional and $\mathbf{w}$ as a concatenation of all weights in the network, i.e. n-dimensional. However, the function $l$ defined in (9) takes $\mathbf{w}, x, t$ as inputs, but function $l$ in (11) takes $\mathbf{u}, \xi, t$ as inputs. If I understand it correctly, these $\mathbf{u}$ is a control variable and is not the same as the input trajectory defined in Section 2. But having a clear example would greatly decrease the confusion.
* **Existing literature**. The paper is motivated by biological learning where the organisms do not have access to the entire data collection ("the agent can only use buffers of limited dimensions for storing the processed information") However, the paper ignores the existing literature on Online Learning and Online Optimisation, that are highly related to the topic. Putting the work into this context would be highly beneficial for the community.

### Questions
* Could you elaborate on the meaning of 'temporal horizon' in Section 2? Imagine we have an RNN which we update using gradient descent. The inputs have temporal aspect (e.g. sequences of real numbers), and the updates have temporal aspect (each weight updates adds one to the time subscript of the weight). Which one do you imply in Section 2? Do you intertwine the two as you mention in the second paragraph of Section 1 ("we assume that learning and inference develop jointly")? Could you provide a toy example?
* "we show that the on-line computation described in the paper yields spatiotemporal locality, thus addressing also the longstanding debate on Backpropagation biological plausibility". Could you provide a couple of references on the debate and add a sentence or two explaining how your result affect the debate.
* Section 2 defines the computational model based on a digraph. Should there also be an acyclicity constraint that does not allow "inputs -> A-> B->A" within the same time step?
* For me, equation 8 comes out of the blue. Section (2) introduces the computational model and the constraints on it. Beginning of Section 3 mention CAL (Betti et al., 2019) for FNN (feedforward NN?). And then you say "we claim that in an online setting the laws of learning for recurrent architectures can also be characterized by minimality of a class of functional. In what follows we will then concider variational problems for the functional of the form". Could you explain where does equation 8 come from? Is the mc/2 * |w|^2 the reqularisation term? If yes, does the $l$ in equation 8 differ from the $l$ in Theorem 2 that already includes the regularisation term?
* "The local structure of equation 10, that comes from the locality of the computational model from Section 2 guarantees the locality of Hamilton's equation 12". Could you, please, explain why this is the case?
* Beginning of page 5 mentions backprop for FNN leading to equation 15 after introducing normalised costates. Could you explain the jump from considering RNNs to FNNs?
* (Corollary 1) "the proof comes immediately from equation 16." Could you add a couple of explicit steps for me to understand why this is the case?
* "This is a strong indication that when solving Hamilton's equations with an initial condition on $p_w$ we will end up with a solution that is far from the minimum". How does this relate to any of the practical consequences on learning algorithms, e.g. backpropagation?
### Nits

* "Spectacular results achieved in machine learning, ..., rely on large data collections. On the opposite, intelligent processes in nature arise without the need for such collections"
	* True, but having access to libraries and archives have significantly boosted our ability to do science and fuelled the progress.
* page 5, "Theorem 2 other than giving us a spatio-temporal ... show". Is there a word missing here?
* footnote 5: "... class of cohercive potentials V" Should be "coercive"?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
I note that I am unable to provide a good summary of this paper, as I found it very difficult to understand. See below for more details on that.

The authors introduce a graph model of a computation, as a formalisation of a neural network. Although the model is continuous time, they also introduce a quantised time version of it. Their model has a notion of spatio-temporal locality, which allows them to express some constraints on the computation. They introduce a variational problem, although it wasn't clear to me what the relevance of this particular functional or its stationarity is. This allows the authors to derive a set of Hamiltonian equations. After this, I lost track of the direction the paper was going: the locality constraints were reconsidered, and there was a consideration of boundary conditions, followed by the introduction of some time-reversal transformations that I didn't understand in this context.

I wasn't able to understand how the conclusion related to the mathematics presented.

### Strengths
n/a

### Weaknesses
In my opinion the main weakness in this paper is that it does not explain itself adequately for the target audience. I'm not an expert in the field presented in the paper, but I am, I think, representative in terms of experience and knowledge of the ICLR audience, and I wasn't able to understand what this paper was trying to say. I think an ICLR paper should be able to: explain it's key finding, what this is, and why it's important to anyone in the audience; and should provide sufficient information for an interested non-specialist reader to understand the paper in detail if they are willing to put in the work. I don't feel that the paper met either of these criteria.

I would recommend that the authors either consider submitting the paper to a specialist journal, where the audience might be better matched to its content, or rewriting considerably to clearly explain the problem in the context of machine learning in general if they wish to submit to another general conference.

### Questions
My limited ability to understand the paper limits the number of questions I have.

One thing that stood out to me was the authors introduce the paper by noting that many ML approaches require a large amount of pre-collected data, whereas the techniques to be described in the paper will work "on-line", using a limited capacity memory to interpret the stream of information as it comes in in a causal way. This sounds a lot like reinforcement learning. Indeed there are some further resonances with reinforcement learning further through the paper where the authors mention dynamic programming, and their introduction of a Lagrangian-like variational objective, and the subsequent transformation into a Hamiltonian problem reminds one of the relationship between value functions and the local behaviour of optimal policies. I think if the authors wish to present to a broad audience it would be useful to address this question of the relationship to reinforcement learning, which is likely to come up.

### Soundness
1 poor

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Summary:

The authors propose a framework that processes information online in a local spatiotemporal manner, motivated by biologically plausible learning schemes. They formulates continuous-time learning as an optimal control problem, connecting learning dynamics to Hamiltonian equations. They additionally show how taking the limit as propagation speed goes to infinity recovers backpropagation, suggesting backprop may emerge from local learning rules.  Ultimately, their framework requires solving Hamiltonian equations with boundary conditions, but the authors propose approximating the solution using only initial conditions via time reversal techniques.

### Strengths
Originality:

The authors present a novel perspective on learning by formulating it in the language of optimal control and Hamiltonian dynamics.  Using this language to connect backprop to local learning rules is, to my knowledge, novel.

Quality:

The paper seems theoretically grounded, with detailed mathematical derivations connecting backpropagation in simple neural networks to hamiltonian dynamics.

Clarity:

The paper is reasonably well structured and explains concepts like Hamiltonian equations and optimal control accessibly. I appreciated the numerous examples, and toy experiments.  The authors are likewise honest about the theoretical nature of the work.

Significance:

If validated, demonstrating backpropagation emerging from local learning would be quite significant.

### Weaknesses
It's very difficult to ascertain the significance of this work without further empirical validation.  I'd greatly encourage the authors to continue this line of work, and further to validate it on more mature learning problems.  I found the theoretical discussions to be somewhat tortuous, and the applicability of the method to be unclear.  The authors might try dramatically simplifying their presentation to make the thread between backpropagation and hamiltonian dynamics as clean as possible, and develop more experiments detailing the tradeoffs that the local learning rule implied by their work buys them.

### Questions
Could the authors describe how their local learning rule relates to BPTT in more detail?

Could the authors comment on the difficulty of applying their method to a more mature sequence learning problem, using, e.g., LSTMs over time-series data?

Can the authors comment on the time complexity of evaluating their method relative to backpropagation?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
