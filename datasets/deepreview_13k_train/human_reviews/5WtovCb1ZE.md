# Models That Prove Their Own Correctness

- Decision: Reject
- Scores: 8, 6, 3, 6

## Abstract
How can we trust the correctness of a learned model on a particular input of interest? Model accuracy is typically measured \emph{on average} over a distribution of inputs, giving no guarantee for any fixed input.
This paper proposes a theoretically-founded solution to this problem: to train \emph{Self-Proving models} that prove the correctness of their output to 
a verification algorithm $V$ via an Interactive Proof.

Self-Proving models satisfy that, with high probability over an input sampled from a given distribution, the model generates a correct output \emph{and} successfully proves its correctness to $V\!$. The \emph{soundness} property of $V$ guarantees that, for \emph{every} input, no model can convince $V$ of the correctness of an incorrect output. Thus, a 
Self-Proving model proves correctness of most of its outputs, while \emph{all} incorrect outputs (of any model) are detected by $V$. We devise a generic methods for learning 
Self-Proving models, and prove its
convergence under certain assumptions.

The theoretical framework and results are complemented by experiments on an arithmetic capability:
computing the greatest common divisor (GCD) of two integers. Our learning method is used to train a Self-Proving transformer that computes the GCD \emph{and} proves the correctness of its answer. Our code is available at \url{\codeurl}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this paper, the authors propose a new type of self-proving models that not just predict an output for a given input but also a proof for the correctness of the output. One of the main ideas of the paper is to use a particular notion of proof from the work of interactive proof systems in theoretical computer science, where a proof means a sequence of answers to a verifier's questions that can convince the verifier of the correctness of the output. The authors compare their approach with other similar proposals for self-proving models, and emphasise the benefit of having an instance-specific proof in their approach. They then describe two algorithms for learning such a proof-producing transformer model, namely, Transcript Learning (TL) that assumes strong supervision via successful question-answer sequences, and Reinfocement Learning from Verifier Feedback (RLVF) that does not assume such strong supervision. Their experiments with learning the GCD algorithm with a small version of GPT show the promise of their approach.

### Strengths
1. The idea of using a verifier from the theory of interactive proof systems for learning a self-proving model is very nice. It may lead to further interesting research activities that address the AI safety issue using several related tools from theoretical computer science, such as PCP and property testing etc. 

2. The paper is written well. The discussion on related work helped me to understand what people had explored in the past, and to see the contributions of the paper more clearly. Also, the background materials are covered nicely so that I can follow most of the formal developments in the paper although I am not familiar with, for instance, interactive proof systems.

3.  The paper contains a theoretical justification, namely, Theorem 4.1. I am less confident that this theorem is useful in practice, but it is good that the authors makes an effort for proving a theoretical result. Also, their comment on the proof using the reduction to SGD and the communication complexity by a verifier (captured by the constant C) helped me to see what goes on more clearly.

### Weaknesses
I support the acceptance of this paper. The following points are mostly minor.

1. Having an example in addition to GCD would have convinced me of the promise of the authors' approach far more. As the authors pointed out, the proofs in this GCD case do not involve questions from the verifier, and so they are simple. Also, the annotated transcript learning is only vaguely defined, and it is only explained in terms of illustration in the example via the intermediate steps of the Euclid algorithm. Seeing one more example would have helped me to grasp what annotations would mean in other problems.

2. I suggest to include Algorithms 1 and 2 into the main text, instead of including them in the appendix. They are more or less standard, but I feel that they are one of the main contributions of the paper. Also, one unexpected thing that I found is that Algorithm 1 is derived by maximising theta over the expected probability E_{trace ~ p(trace)}[q_theta(trace)], instead of the expected log probability E_{trace ~ p(trace)}[log q_theta(trace)] (i.e., cross entropy loss). Some subtleties like this deserve the attention of the reader, I think.



### Questions
The only question that I have is related to what I said in the second point in the weakness box. My understanding is that Algorithm 1 uses the expected probability as a training objective, instead of expected log probability. Is there a reason for this? Is this due to the consistency with Theorem 4.1?

Here are some minor typos.

(1) L284 : EOS in Sigma^* ===> EOS in Sigma

(2) L391 : Giving examples of annotations may help some readers.

(3) L510 : Have you tried more samples in some cases and checked your conjecture?

(4) L926 : a_0 := y ===> a_0 := y^*

(5) L928 : (y,q_1^*,..., q_r^*,a_r) ===> (y^*,q_1^*,...,q_r^*)

(6) L1150 : Maybe it is better to break a line before "for s in [L_a] do"

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper develops the concept of self-proving models that justify (or "prove" in the authors language) their answers to a trusted and pre-built verifier. The process results in a probablistic guarantee on the correctness of the answer provided by the self-proving model.  Transcript learning and RL are proposed as methods to derive a self-proving model. Experiments are conducted on a Greatest Common Divisor problem.

### Strengths
I find the overall approach principled and welcome. Moving the assessment of the answer of a model from test results to an estimate of the correctness on the individual query (and this not being provided by the model itself) is certainly welcome. 

I am not sure the overall setup is novel as such (see below); however I believe the error bounds on the two learning approaches are. The results are well backed by theory and the paper does a good job at making this challenging subject as accessible as possible without trivialising the contribution.
Some experiments, although perhaps limited, are provided supporting the results.

### Weaknesses
It was not clear to me the extent to novelty of the overall setup of the pair prover/disprover. Obviously this is a well-known setup in many applications including those cited in the literature (perhaps the whole area of "Argumentation" in AI should also be included as it is not very far from here), but this particular instantiation with ML models and a formal verifier could be clarified.

The verifier obviously has a fundamental role here. I might have missed this but the implications of this were not clear to me (how can they be derived and at what costs).

I think the authors realise that their experimentation on GCD are limited even from a purely algebraic perspective. I think this is OK, but more thoughts into how this might or might not scale to more challenging problems or more general ones might be beneficial.

Fundamentally, the end result obtained by the method, if I understand the paper, is a probabilistic guarantee that the answer provided is correct (following a sequence of challenges to the verifier). In the domain explored (algebra) we tend to deal with true/false propositions.

### Questions
What are your views on probalistic gurantees for mathematical statement? Do you consider them useful, or is this setup a step along the way to a different application where probabilistic guarantees are more meaningful?

Can you comment on the importance and derivation of the verifier and highlight the ease or difficulty in deriving them for the problem in hand in combination with or independently of the self-proving model?

What are your thoughts on moving beyond GCD for a mathematical theory and beyond this other mathematical challenges?

Edits post review:

1. I acknowledge you might not agree with my comment of this being a "well-known set up". This was not meant as a criticism to the work. I think you are well aware that the general concept of prover/disprover set up has been long been around in logic (indeed, general philosophy before then) and theoretical computer science including in synthesis. The setup has also been used in AI Argumentation and many other areas. I understand that here the emphasis is different and so is the generality of the overall task. Note that pretty general theorem provers such as Isabelle have also been used in similar setups to aid computer proofs. In any case this was not a criticism but a request for clarification. I do not believe we fundamentally disagree here.
2. To me the role of the verifier appears to be pretty important. So I would encourage to explore this issue more. The concern I have is that a lot of the problem here has been pushed onto the (derivation of) the verifier). I agree with the authors, but only to some extent, that the work explores a somewhat different dimension. My point was and to some extent still is that whole apparatus appears to reside on the verifier but its construction is not necessarily obvious and not explored here. I accept that my suggestions can be left for further work.
3. I do appreciate the attempt to run further experiments on a different challenge, particularly given, as reported another referee, perhaps GCD is not entirely illustrative to show the advantages of the present approach.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes a self-proving model, a new learning paradigm that a model outputs both a prediction $y$ and a proof for the correctness of the prediction by interacting with a verifier. A self-proving model is useful for users since it can ensure that the output of a model is correct. The paper proposes a self-proving model and defines some metrics for evaluating the performance of a self-proving model. The paper also gives learning algorithms for learning a self-proving model and theoretical analyses on the convergence of the transcript learning algorithm. The experiments evaluate the performance of self-proving models on a GCD task.

### Strengths
1. This is a well-motivated work. The use case shown in the introduction of the paper is attractive. 

2. The proposed self-proving framework that proves the correctness of the answer by interactions between an autoregressive model and an external verifier seems a natural setting.

### Weaknesses
1. Theorem 4.1, one of the major theoretical contributions of the paper, makes some strong assumptions. Therefore, I think the contribution of the theorem is limited.  Firstly, it assumes that $A(\theta)$ is concave. I think this assumption does not hold for the typical autoregressive models used today, including the GPT model used in experiments. Moreover, the theorem assumes the existence of $\theta^\ast$ satisfying $A(\theta^\ast) \geq 1 - \epsilon/2$. This is also a strong assumption since it is currently not clear whether such self-proving models exist or not. The assumption of concavity is particularly problematic because it drastically simplifies the optimization landscape, making it unlike the highly non-convex loss surfaces encountered in training modern neural networks. This discrepancy undermines the practical relevance of the theoretical results. Furthermore, the existence of a $\theta^\ast$ that achieves a high level of self-proving accuracy is a significant assumption that needs more justification, as it is not guaranteed that such a parameter configuration exists for all problems or model architectures.
2. The paper evaluates the self-proving model's performance on a GCD task. However, I feel that GCD would not be appropriate as a use case for a self-proving model since it is an easy task, and we do not need any machine-learning techniques to solve it. It is reasonable that Carton (2024) solved a GCD task since the paper's main objective is to understand how a transformer works. On the other hand, I think that this paper should show the effectiveness of the proposed self-proving model, and the experiments with a GCD task are not sufficient. The choice of GCD as the primary experimental task is questionable, as it is a well-understood problem with efficient non-ML algorithms. This choice does not adequately demonstrate the potential of the self-proving model in more complex and relevant scenarios where machine learning techniques are necessary. The experimental results are thus limited in their ability to support the broader claims of the paper.
3. The paper emphasizes the use-case that self-proving models can guarantee the correctness of a specific $x_0, y_0$. (line 262). This feature depends on  the $s$-soundness defined for a probabilistic verifier. However, the assumption that $s$-soundness holds for any $x, y, P$ is unrealistic (See the question 2 below). It is more natural to assume that a false-positive error (line 207) depends on the distribution over $x, y$. However, if we make such an assumption, then it is difficult to give a guarantee for specific $x_0, y_0$. Therefore, I think the self-proving model does not work as stated in the use case. The reliance on a worst-case soundness guarantee, where the verifier's error is bounded for all possible inputs and proofs, is a strong requirement that is difficult to achieve in practice. It is more realistic to assume that the verifier's error is dependent on the specific input distribution, which would make it challenging to provide guarantees for individual input-output pairs.

### Questions
1. I think this type of theoretical bound needs a confidence parameter $\delta$. Since we estimate parameter $\theta$ from a finite set of $N$ samples instead of accessing the distribution $\mu$,  it is possible that the drawn samples are "bad" and that we cannot estimate suitable parameters from the samples. Could you please explain why we do not need a confidence parameter $\delta$?
2. The paper says that completeness and soundness are properties of a verifier (Definition 3.2). However, it seems unrealistic to imagine a probabilistic verifier whose soundness error is always smaller than $s$ for *any* $x, y$ and $P$, unless $s = 0$. How can we obtain such a verifier? Where does the probability come from?  Moreover, I think it is possible to reduce false positive errors (line 208) arbitrarily by running a probabilistic verifier $V$ for multiple times for the same $(x, y, P)$. It is more realistic for me to assume that there are specific $(x, y, P)$ that causes a false-positive error for the verifier $V$, and thus it depends on the distribution $\mu$. 
3. Related to the above point, Definition 3.2 assumes the randomness of $V$ and $P$ line 209, but the definition of soundness assumes the condition holds for all $P$. Is $P$ random?

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
4

### Summary
In this work, the authors propose a methodology to learn models that can provide evidence about the correctness of their answers. 
Given a function F:Sigma*->Sigma*, a model for F is a function F_theta that assigns to each x\in Sigma^* a probability distribution F_theta(x). 

A model is alpha-correct if on a random input x, the output F_{theat}(x) is equal to F(x) with probability at least \alpha. 
Given a function F and a verifier V, a model F_theta is beta-self proving if V(x,y)=1 with hight probability, where x is an input sampled at random and y is sampled at random from F_theta(x). 

The goal is to learn a model that has a high degree of correctness (\alpha close to 1) and a high degree of verifiability (\beta close to 1). The authors develop a methodology for this task, and use learning models that compute the GCD of two numbers as an example.

### Strengths
I find the topic of the paper quite interesting.

 The paper seems to provide a nice framework to combine interactive proof systems with techniques from learning theory. Although formal verification has been widely studied in connection with learning theory, the disadvantage is that, in most of the approaches, the goal is to construct a proof of correctness in some fixed proof system. The use of interactive proof systems adds a lot of flexibility to the process, besides giving an avenue for a theoretical analysis related to the convergence of the learning process etc.

### Weaknesses
The disadvantage of the approach is that it requires access to the implementation of a previously existing verifier. I find that the paper lacks a discussion about the usefulness of trying to learn a function for which we already have an implementation. Specifically, it is not clear what practical scenarios would benefit from learning a model that can both compute a function and provide a proof of correctness, when a verifier is already available. The paper does not address the computational overhead of generating these proofs, and whether the cost of generating the proof outweighs the benefit of having a self-proving model. Furthermore, the paper does not discuss the limitations of the verifier itself. If the verifier is not perfect, then the learned model may be self-proving with respect to a flawed verifier, which would not be useful in practice.

### Questions
No questions.

### Soundness
3

### Presentation
3

### Contribution
3
