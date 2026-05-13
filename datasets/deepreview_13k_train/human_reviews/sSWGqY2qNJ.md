# Indeterminate Probability Theory

- Decision: Reject
- Scores: 6, 1, 3

## Abstract
We propose a new general model called \textbf{IPNN} \textendash\enspace\textbf{I}ndeterminate \textbf{P}robability \textbf{N}eural \textbf{N}etwork, 
    which combines neural network and probability theory together. In the classical probability theory, 
    the calculation of probability is based on the occurrence of events, which is hardly used in current neural networks. 
    In this paper, we propose a new general probability theory, which is an extension of classical probability theory,
    and makes classical probability theory a special case to our theory.
    Besides, for our proposed neural network framework, the output of neural network is defined as probability events, and based on the statistical analysis 
    of these events, the inference model for classification task is deduced. IPNN shows new property: It can perform unsupervised clustering 
    while doing classification. Besides, IPNN is capable of making very large classification with very small neural network, \eg\enspace model with 100 output nodes can classify 10 billion categories. 
    Theoretical advantages are reflected in experimental results

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This is an extremely ambitious paper that attempts to construct a new theory called indeterminate probability theory. The key idea of Indeterminate probability theory is to introduce a new concept of auxiliary observers and to treat the results of each random experiment as an indeterminate probability distribution, while still preserving the assumption of mutual independence. As a result, the posterior probabilities of the system can be derived in a form that is easy to handle analytically, an important benefit in applications.
The authors demonstrate the applicability of this idea to regression and classification problems by combining it with neural networks.

### Strengths
I am very grateful to the authors for sharing their novel attempt at this paper. I enjoyed reading this paper very much.
- The paper devotes a great deal of effort in its presentation to illustrate new ideas that are outside of the conventional wisdom. The paper is very well written and its organization is designed to appeal to a diverse audience. In particular, it is designed to be easily understood by explaining the core ideas by means of toy examples.
- The practical contribution of this paper is very significant. Traditionally, posterior probabilities in statistical machine learning have been approximated by some kind of approximation method (e.g., Markov chain Monte Carlo or variational methods), but the ideas in this paper have the potential to be a new option to add to that.

### Weaknesses
First of all, let me emphasize that I am trying to be very open minded in understanding the value of this paper. My grade on my first peer review may not be very high, but I am prepared to improve it as soon as I properly understand the value of this paper.
My concern is whether this paper could create a new system of probability theory (i.e., a major historical breakthrough) or whether it provides a new perspective on approximation and interpretation for the system in a form that is easy to handle in applications (i.e., a new alternative alongside MCMC and VB), a somewhat excessive Is it an appealing proposition? I would like to inquire in the question section for more details.

### Questions
My question can be summarized very simply as to whether or not indeterminate probability theory can be expressed in terms of a definition of probability space using abstract probability space.

First of all, I understand this new insightful strategy of the authors as follows (Perhaps this understanding of mine is incorrect. If I am wrong, I would be very grateful if you could correct me.) 
- The authors' system introduces uncertainty as an auxiliary variable for observers. If this were to be expressed in the context of a conventional standard Bayesian analysis, the observer could be represented as making an observation error according to the auxiliary random variable.
- Next, since this auxiliary random variable is not needed to describe the system, we will try to eliminate it in some way. In a conventional standard Bayesian analysis, this can be done by eliminating the auxiliary random variable by marginalization. However, a problem arises here. If the auxiliary random variable is shared by all observers, the system loses observer independence (Axiom 2 of the proposed probability theory) when it is eliminated.
- Therefore, the proposed probability theory simply ignores the auxiliary random variable while simultaneously assuming Axiom 2.

If we were to use such a strategy, it would certainly seem that we could view the system as different from classical probability theory (as mentioned in the paper, we could of course make special cases that are equivalent to classical probability theory in special circumstances).

Following this intuition, my interest is in what the authors' system would look like if it were represented in an abstract probability space. That is, a situation where all randomness in the world is governed by an abstract space $\Theta$, where all randomness is lost if the abstract space is determined at a point $\theta\in\Theta$, and where all variables can be described deterministically. In the abstract space, random variables are represented as a projection of the world as a map to an object, e.g., $Y(\theta), X(\theta), A(\theta)$ can be uniquely determined for a given source $\theta$. Can the authors' system be represented using such a conventional abstract probability space? Or is it a deviation from that rule?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes to introduce a new theory of probability to cope with imperfect observations, in the sense that the reported value can be different from the true experimental result. This is done through the introduction of an "observer", which can be imperfect, in the sense that it is noisy. The theory is then applied to various case studies.

### Strengths
I do not really perceive any strong point in the paper, other than the fact that modelling imperfect observational process is an interesting, yet arguably old topic.

### Weaknesses
This paper is puzzling me in more than one ways, and I will focus on the main ones (some for which the authors can offer a rebuttal, mostly when it concerns the content and not the form of the paper).

A first thing is that the paper is written in a very unusual way, at least for a paper of computer science and/or machine learning. It is very rare to directly start with a mathematical formulation, without making first an introduction (and possibly related work) positioning the proposal and its originality.

A second thing is that the paper is very quick on some technical details, while being very verbose on rather basing thing such as classical applications of probabilistic conditioning. It is also a bit cryptic in terms of language as well as bit naive about some aspects. For instance, P2 top, it is not true that one cannot apply Bayes rule in continuous setting, and it has been numerous, numerous times. At this point, what means indeterminate is also quite obscure. Similarly, it is not clear for the naive Bayes what exactly means $P(A^j=a^j_{i_j}|Y=y_l)$ being not solvable? It can certainly be estimated from data, even in case of noisy observations or untrue assumptions (potentially leading to biased estimates, but it can nonetheless be estimated).

A third thing is that it is unclear what authors really understand by “indeterminate”: is it that the observational process is noisy, or that the obtained probabilities are ill-known and hence that one should consider sets of possible probabilities? The paper suggests the first case, yet in such a situation I really do not see what is different between what is proposed in the paper and the consideration of noisy data where one does know or can estimate the noise process? Given that there is a huge literature on learning from noisy (and/or imprecise) data, at least a positioning with respect to those should be done. Indeed, if the main idea of the paper is to have $P(y_{obs}=y|y_{true}=y)<1$ ($y$ here can be either the output value or a feature value) and then to proceed from that, then I would argue that considering such a situation is not new at all. Similarly, if indeterminate means ill-defined, then there is a whole literature about that (see, e.g., work following the book on Peter Walley on imprecise probabilities and similar). Claiming to build a new theory of probability should be backed up by being very precise about why previous theories do not answer the considered problem.

A fourth thing is that it is really unclear to me why the current experiments, that merely show accuracy results for standard problems, do show that the theory is “valid”? I would equally question a statistical learning theory or more generally an uncertainty theory whose axioms cannot be the subject of tests and falsification? All theories of uncertainty I know of that are a bit serious in terms of operationally are subject to falsifiability, and this especially true for probabilistic theories (see the Ellsberg paradox for a good example of attempted falsification). Also, since Softmax does not enjoy peculiarly good properties from a theoretical perspective, I would not consider it as a strong baselines against which to test the axioms of a theory?

### Questions
See weaknesses

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes "Indeterminate Probability Theory", which is claimed as an extension of classical probability theory. Based on the proposed theory, the authors derive an analytical expression of general posterior, which has some applications such as IPNN and CIPNN. Experimental results validate the proposed theory.

### Strengths
This paper claims to extend classical probability theory, which is very ambitious and is definitely important if this is true.

### Weaknesses
The main contribution of this paper is the proposed "Indeterministic Probability Theory", but it is far from satisfaction to be a theory, especially when it is stated to be "an extension of classical probability theory". It is actually built on the axioms of classical probability theory, added with a specific generation process of random variables, and three proposed "candidate axioms", thus it at most becomes "a special sub-field of classical probability theory".

Even worse, the paper claims that "our most important contribution is that we propose a new **general analytical** and **tractable** probability equation", but neither is theoretically validated: for **general analytical**, it is analytical, but it is not discussed enough why the proposed two-phase protocol is general; for **tractable**, it is also not verified the error of approximation via Monte Carlo methods. There are some experimental results to verify the effectiveness of Monte Carlo, but is over-simplified to validate it in such a general theory as is claimed, and more importantly, the effectiveness of Monte Carlo in this paper is not "proved" yet. The authors claim that the proposed equation is general, but they do not provide a rigorous proof of this generality, nor do they discuss the limitations of the proposed two-phase protocol in modeling various data-generation processes. The lack of theoretical validation for the generality and tractability claims significantly weakens the contribution.

To be honest, section 3 is more like a section of "problem formulation + proposed approach": The two-phase protocol is more like the problem formulation, the axioms are more like some assumptions of independence, and the complexity reduction using Monte Carlo is more like the proposed approach.

### Questions
What do you want to say in Section 2? It seems that the example does not go beyond classical probability theory, i.e., all definitions, quantities and calculations are consistent with definitions and axioms in classical probability theory.

What is new in your indeterminate probability theory? Specifically, I am confused why eq. (4) must be 0 or 1 in classical probability theory. Could the authors give some references? The authors should give references, clear derivations or rigorous counter-examples when refuting something in classical probability theory, as it is based on rigorous mathematics. 

How general your proposed theory is? For example, does your theory enable A and Y to be any kind of random variables, and can the two-phase protocol in your theory model any data-generation process? If not, then the generality of your theory should be discussed. 

In page 5 the authors say "...Otherwise, Candidate Axiom 2 and Candidate Axiom 3 cannot both be true". In my opinion, it is strange to discuss the soundness of an axiom once it is proposed.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor
