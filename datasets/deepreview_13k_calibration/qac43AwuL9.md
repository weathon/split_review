# Optimal Causal Representations and the Causal Information Bottleneck

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 5, 5, 6

## Abstract
To effectively study complex causal systems, it is often useful to construct representations that simplify parts of the system by discarding irrelevant details while preserving key features.
  The Information Bottleneck (IB) method is a widely used approach in representation learning that compresses random variables while retaining information about a target variable.
  Traditional methods like IB are purely statistical and ignore underlying causal structures, making them ill-suited for causal tasks.
  We propose the Causal Information Bottleneck (CIB), a causal extension of the IB, which compresses a set of chosen variables while maintaining causal control over a target variable.
  This method produces representations which are causally interpretable, and which can be used when reasoning about interventions.
  We present experimental results demonstrating that the learned representations accurately capture causality as intended.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors propose the Causal Information Bottleneck as an extension of the Information Bottleneck capable of respecting causal relationships between relevant variables. A formal context is provided before a (Lagrangian) minimization problem is proposed, using do-calculus. The manuscript concludes with experimental results on three examples of increasing complexity.

### Strengths
The manuscript is well written, with a good formal description of relevant concepts and illustrative computational examples. Additional details are expanded on in the appendix with more-than-adequate references provided. The concept of a Causal Information Bottleneck is introduced naturally as an "extension" of an Information Bottleneck, and it is shown that it can be leveraged, in an algorithmic way, to construct representations that respect causal representations between variables in a rigorous sense. 

The material in the manuscript is original and, in my opinion, presented very clearly, with a good background in existing theory.

### Weaknesses
The examples provided are simple, which is helpful for understanding the relevant concepts; however it would be nice to demonstrate an application with a (considerably) larger set of variables or dependencies. 
It is (somewhat) unclear how often the proposed solution approach will be expected to produce `good’ results in minimizing in minimizing equation (3).

Minor point: the term “representation” appears several times in the manuscript but is given a formal definition on pg. 6. The use of the term may be standard in the particular literature, but it would be constructive to at least reference the definition at first occurrence, or to use a different term whenever that definition is not applicable and “representation” is used more loosely.

### Questions
To what extent does one have to always check whether conditions (a), (b), and (c) are met each time one applies the proposed algorithm to a new problem? When would the proposed algorithm be expected to fail?

Can you comment on the scalability of the proposed algorithm?

Can you clarify the meaning of “conserve space” (line 62)?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Causal representation learning and causal abstractions are a key problem in causality and the paper proposes the Causal Information Bottleneck, a causal extension of the classical information bottleneck in representation learning. 

The paper is nice to read and well structured. However both the theoretical contributions as well as the empirical contributions are very limited and I can thus not recommend the publication for acceptance in its current form.

### Strengths
Despite the rather negative review, I think it is a great topic and the paper addresses a good question. Causal abstractions are a key focus point and question for many problems. It is thus a very timely and very important problem. I really hope the authors continue with the direction of their work, and I enjoyed reading it. The paper is easy to follow, partially because the proofs are rather simple, and the experimental section is very short.

### Weaknesses
Wrt to baselines and empirical evaluation the authors write correctly that there are many more available e.g. ". Specifically, they use variational autoencoders (VAEs), relying on the fact that β-VAEs (when used for the task of reconstruction) minimize the information bottleneck (Achille & Soatto, 2018). However, their method does not account for causality, being limited to scenarios without confounding due to its reliance on the standard IB"
However the paper does not compare against VAEs, beta-VAEs, Graph-VAEs or even some approaches like [1,2] or any of the plenty variants which can be found by a quick google search. 

[1] Subramanian, Jithendaraa, et al. "Learning latent structural causal models." arXiv preprint arXiv:2210.13583 (2022).
[2]Liu, Yuhang, et al. "Identifying weight-variant latent causal models." arXiv preprint arXiv:2208.14153 (2022).
[3] etc
While some of the above approaches might not be one to one applicable, it simply would need to be explained much more clearly why this specific setting is the first of its kind and not comparison is needed. While I agree that beta-vae is not a causal method on its own, I would still like to see it evaluated as well as other methods and see the benefit of the causal method on the task. In particular, I would not only want to see the causal graph recovered but used for a downstream task and then the comparison to beta vae or other methods applied to the downstream task. 

What are the assumptions allowing causal discovery in this setting? Is faithfulness assumed? There are no statements about many of the established assumptions enabling causal discovery in the text, yet it is clear that causality can not be inferred from obervational data without further assumptions. How does the approaches assumptions related to the assumptions of classical approaches, and which ones are needed? Assumption 8 is introduced as the only assumption but that seems to simplify the problem a lot ... 

Finally, if it is really just a toy case and the own method should be in the focus then clearly demonstrate the robustness to noise or some ablations. 
Moreover, the provided propositions are really not propositions but follow directly from the definition, e.g. Proposition 6.

### Questions
See weakneses above.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The work extends the concept of information bottleneck to causal settings. It builds upon the idea of Tishby et al. and propose a new method for finding representations that respect the underlying causal mechanisms to a certain degree. A new definition of optimal causal representation is also presented. The work improves the interpretability of causal relationships and also extends the  interventional reasoning to complex causal systems.

### Strengths
1. Interesting work. Extending IB to a causal setting in a principled fashion is a novel task in my knowledge. The authors should be commended for this.

2. Impressive results (although in simple domains), but a good start nonetheless.

### Weaknesses
1. The paper talks about the representations being interpretable but the experimental evaluations do not justify the claims. Can the authors comment on this?

2. How are correct causal relationships obtained? I mean for simpler domains this is feasible but for more complex domains this can be a big issue.

3. Should'nt $\beta$  i.e. the Lagrange multiplier be learned rather than it being fixed?

4. Also for the interventional decoder, using a uniform prior seems to be a pretty generic choice. It would have been more interesting to see more complex priors.

### Questions
See the Weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors propose an approach of learning causal representation from a ground truth distributions. In particular, the authors consider a setting in which causal relations are present, such that compression approaches that are unaware of relations might fail due to confounding effects. To overcome such confounding effects, the authors propose a causal information bottleneck (CIB) that leverages a causal information gain, opposed to standard information gain used in the normal IB, which considers changes in interventional distributions of the variables when intervening on the learned representation instead of standard conditioning. The authors propose intervention encoders and decoders, $p(T|X), q(T|X)$, that are learned to map between given variables $X$ and a representation $T$ while being regularized via the interventional distributions of the model. The resulting CIB guides optimization of the en-/decoders and therefore is able to balance the compression of variables, predictive power, and causal control.

The authors define a backdoor adjustment formula for the learned representation, transfers known identification results on standard SCM to the learned representation. The correct working of their approach is verified via three synthetic experiments, featuring different levels of confounding and representation compression. The results indicate a continuous transition between retained causal mutual information of the learned presentation and base model variables and the predictive performance of the model.

### Strengths
The paper is generally well written. Previous definitions, such as causal entropy and causal information gain, are well introduced and explained. The construction of the CIB resembles that of the standard IB and follows naturally. The Lagrangian formulation follows standard definitions and, while I'm not an expert on the topic, the applied optimizations seem be reasonable choices.

In comparison to prior works, the presented information-theoretic treatise provides a clear and defined trade-off between predictive performance, compression and retained causal information. The presented backdoor adjustment formula for representations is soundly defined and allows for identification of causal effects given that the adjustment set variables are known and can be conditioned on.

The authors successfully demonstrate a continuous transition between retained causal mutual information from the base model variables and the predictive performance of the model under a varying regularization factor.

### Weaknesses
The work generally overcomes several obstacles in learning causal abstractions via the proposed CIB. This, however, comes at the cost of strong assumptions of all discrete variables and having full access to their graph and joint distribution. While the authors mention the possibility to extend their work to continuous domain, experiments remain rather simple. Evaluations on the effects of incomplete or incorrect knowledge on the causal graph, as for example considered for the motivational example, or the extension to higher-dimensional domains, e.g. experiments on (synthetic) image data, are lacking.

To the best of my knowledge, the authors cite relevant works on causal abstraction and IB theory. However, prior work on applied causal representation learning is missing. This includes prior works on learning tau abstraction [1,2] and general identifiability results on latent causal representations, e.g. [3,4].


**Minor**

* The authors state that "the most common type of intervention is an atomic intervention". While this is certainly true within the field of causality (as it is the easiest to theoretically analyze), a commonly encountered problem in real-world settings is the inability to perform atomic interventions. The authors might want to tune this statement down a bit.
* Figure 1 is generally hard to read without zooming in. I would like to recommend increasing the text size and line widths if possible.

### Questions
I would like to ask the authors to address the weaknesses stated above. In addition, I got the following questions:

1) In the intervention decoder definition (eq. 4) the terms $p*$ and $q$ are defined as probabilities over over values $x, t$ and normalized over $x$. However, neither $p^*$ nor $q$ are conditioning on any particular intervention. While being named 'intervention decoder', it is unclear to me how interventions are exactly involved in the computation of these terms and I would like  to ask the authors to elaborate this.
2) The proposed backdoor adjustment formula marginalizes over variables $Z$ that satisfy the backdoor criterion. Given the motivational example that $Z$ might induce a selection bias and thus can not be fully observed, how realistic is the  scenario of the paper? Could the authors provide insights on the effects of missing or only partial observed confounders with regard to the performance of their approach?


**Rebuttal:** The authors presented an interesting approach, utilizing causal entropy and causal information gain to obtain a 'causally-aware' IB variant that might present a noteworthy addition to the overall tool box of causal training methods. While I find the presented approach interesting from a causal perspective, I also agree with the other reviewers on the rather limited scope of the conducted experiments in terms of practical applicability. The experiments seem to prove the correct working of the approach in small domains, but at the same time come with a number of assumptions, e.g. prior knowledge of the causal graph. Since all (C)IB methods rely on an auto-encoding property which might or might not be achieved in practice, I would have expected to see the actual application of the proposed method to a more complex setting. For the named reasons, after considering the reviews of the other reviewers and the authors' responses, I remain my score of a weak accept.

### Soundness
3

### Presentation
2

### Contribution
2
