# An Information Theory of Compute-Optimal Size Scaling, Emergence, and Plateaus in Language Models

- Decision: Reject
- Scores: 8, 3, 5, 6

## Abstract
Recent empirical studies show three phenomena with increasing size of language models: \textit{compute-optimal size scaling}, \textit{emergent capabilities}, and \textit{performance plateauing}. We present a simple unified mathematical framework to explain all of these language model scaling phenomena, building on recent skill-text bipartite graph frameworks for semantic learning.  Modeling the learning of concepts from texts as an iterative process yields an analogy to iterative decoding of low-density parity check (LDPC) codes in information theory. Thence, drawing on finite-size scaling characterizations of LDPC decoding, we derive the compute-optimal size scaling (Chinchilla rule) for language models. Further, using tools from random network theory, we provide a simple explanation for both emergence of complex skills and plateauing of performance as the size of language models scale.  We see multiple plateaus.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper present a very interesting theory on large language model scaling laws using ideas from information theory, random graphs, and low-density parity-check codes. By drawing similarities between concept-text graphs, skill-concept graphs to Tanner graphs in low-density parity-check codes, the paper provides a theoretical explanations of the phenomenon observed in large language models, including compute-optimal scaling law, scaling law of excess entropy, emergence, and plateauing. The theoretical predicted scaling laws are compared with the empirical laws observed in real-world language models.

### Strengths
*The paper presents a creative way of using existing theories in low-density parity-check codes and random graphs to solve large language model analysis problems. 
*It is convincing that one theory can be used to explain multiple phenomenon in large language model scaling.
*The paper is of good quality, the theoretical analysis are solid.
*The paper is well-written. 
*The theory is of significance, because understanding the scaling laws of large language models may provide further guidance for future model training and scaling.

### Weaknesses
 *I think one assumption the paper makes is that the peeling process has stopped after the model training. Nowadays, many language models are only trained with several epochs. Can we always assume that the peeling process have already stopped after the training?  It's unclear if the model has truly converged to a state where the peeling process is no longer active, especially with limited training epochs. The theory relies on this assumption, and it needs to be more rigorously justified or explored.
*Not necessary in this paper, but it would be good to have more numerical experiments that this peeling process indeed happens in training. The paper would benefit from empirical validation of the peeling process during training. While the theoretical framework is compelling, demonstrating that the proposed peeling process aligns with the actual training dynamics of large language models would significantly strengthen the paper's claims. This could involve tracking the evolution of concept-text and skill-concept graphs during training and observing if the peeling behavior is indeed present.
*The paper assumes that the graphs can be randomly generated, so that we have particular binomial degree distributions. Is it possible to verify indeed this is the case in the real-world. Do the theory in the paper also hold for other degree distributions. The assumption of randomly generated graphs with binomial degree distributions is a simplification. Real-world concept-text and skill-concept graphs might exhibit different degree distributions and structural properties. It would be valuable to investigate whether the theory holds under different degree distributions, and if not, what modifications are needed to account for the complexities of real-world graphs. This could involve analyzing empirical data to determine the actual degree distributions and graph structures.

### Questions
*Some minor issues, in appendix C, should the value in equation 29 is only approximately equal to the value in equation 30? Also, the approximation $(1-x)^n = 1-nx$ should be tight with some additional conditions. In this case, this approximation is tight, only when $p_b$ is also small.
*In line 759, Chernoff's bounds have multiple forms. One reference should be given here.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors proposed a theory for scaling in neural networks via a connection to LDPC code. The authors then claim that the theory leads to explanation of scaling, emergence, and plateaus in language models.

### Strengths
The goal of the paper is ambitious. A unifying theory that can help explain the scaling behavior will be quite nice.

### Weaknesses
Though the effort is appreciated, and there might be some merit to the overall approach, I feel the overall theory is not set up in sufficiently rigorous manner.

1. Reading the paper gives me the feeling that authors are promising too much, but nothing has been theoretically established carefully. First of all, the framework is given in a very vague manner, with the basic definitions for text, concepts, and skills missing. Without rigorous definitions, we cannot come up with simple examples to verify the theory. For example, if I'm given a text sequence, how do I determine if it is a text, a concept, or a skill? Are they all limited by the representation and the length? The theory is shaky when we cannot even answer these basic questions.

2. There seems to be less connection to ML than to LDPC. If we simply replace the text, concept, and skill nodes in the graph with variable and factor nodes in the original LDPC, then the claim holds trivially. This is an extremely weak connection, in names only, without any deeper insights.

3. There are no relevant experimental results for language models at all in the paper. For a theory to hold, we must have some kind of verification with the ML models. The paper reads like this: there are some observations in ML, and it happens that similar effects also occur in other settings, so that theory will fit. This might be a good starting point to contemplate and develop deeper research, but scientific/engineering research cannot stop here.

4. The big concern for me is that the theory is so vaguely defined that it is impossible to come up with experiments to verify whether it is true or not. This is a rather dangerous territory, as it does not follow the standard scientific research approach, and is more like a belief/religion in its current form.

### Questions
Simple questions as mentioned earlier:
1. How to define text, concepts, and skills, and given some test or bit sequence, how do we determine which category it falls into?
2. What experiments can be used to verify the theory?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes an abstraction of the learning process of a large language model using graphs and analyze the behavior of certain dynamics on these graphs. The purpose is to draw a connection to certain observed phenomena of large language models such as the emergence of learned capabilities and the plateauing of performance with size-scaling. 

I found the topic and the framework interesting and worthy of a discussion. However, there are many weaknesses in writing, presentation, and technical issues that makes it difficult to evaluate the paper’s contributions.

### Strengths
Motivation: The framework seems reasonable and diverse enough to model learning and acquisition of new skills. As the authors mentioned, it may be possible to incorporate into the framework additional considerations such as the quality of training data. It would be interesting to discover what can we learn in the training of language models due to this analysis. 

The topic and theoretical framework are related to other recent works, hence it seems like this topic has created enough interest in the community. 

Using tools developed in coding theory and random graph theory in probability seems to have great potential in this context. The authors say “Our work takes a step in grounding empirical phenomena observed in size scaling of language models on a rigorous mathematical footing.” I would put it differently: ``The work proposes a graph-based model for learning skills from texts that appears relevant to the process of training a large language model. The dynamics of message passing under an asymptotic scaling of the model’s size experience phenomenon akin to those empirically observed in this training process of a large language model, such as the emergence of abilities and the plateauing of performance.’’

### Weaknesses
Background and Motivation.
It is unclear what parts of the framework have been considered in previous works. For example, did other work also consider hierarchical skills? Did previous works also try to analyze message-passing dynamics but perhaps using different tools? How significant is the automatic selection of scaling law from the framework compared to previous works? What is the rationale that N (#of parameters) is proportional to R (# of skills)? What is the rationale for studying a limited computed budget and thus the tradeoff N T < C? Do we see such a tradeoff in training language models?

Also, in the abstract and introduction, please be clear whether ‘size’ means the number of parameters or the size of training data. 

The connection to language models is not immediate and it appears that one can replace the language model with any form of a learning machine, like a human. Consequently, I’d expect in this line of work at least some discussions on studies on learning and education in general. Also related: Line 102 says that a language model “chooses to learn.” This seems like a poor choice of words because it is unclear what is the choosing mechanism. Another similar poor choice of word or issue with the motivation is L245: “The goal of the language model is to learn as many concepts as possible…” Of course, actual training in a language model does not directly involve the concept of “concepts”.

The authors say that they use tools from information theory but this is inaccurate because they use statistical mechanics ideas from graph-based coding (Richardson & Urbanke 2008) and random graph theory. The terms information theory and especially non-asymptotic information theory are misleading.


Analysis. 
In general, I found it difficult to follow almost all technical derivations due to missing details. Examples:
What are the {Pi} s in L124? 
What is the “matching condition” in L316
What is r in Eq 2 ? I don’t see how this equation is equivalent to the problem in Eq 1.
What are r and epsilon in Eq 3? 
What is epsilon in Eqs 7 & 8?
What is the origin of the name “post-decoding bit erasure rate”?
What is “excess entropy”? Why do we care about bounding it from below?

The paper mentions compute-optimal scaling but I did not find a clear definition. 
The paper does not explain what the author calls the ``decoding process’’. 

Proposition 1 appears to be flawed. It is not true that if neither R/T = o(1) nor T/R = o(1) hold then R/T → constant (the text actually says “R/T must be a constant”, which is grossly incorrect). As a counterexample, take R = sin(C), T=cos(C). To my understanding, the author quotes this proposition as one of the main contributions of their work, so this needs correction. This proposition is also unclear because the notion of “compute-optimal performance of a language model” has not been well-defined earlier.

### Questions
Some suggestions:
Please specify in the setup that the skills graph obeys the  Erdos-Renyi random graph model, as you later claim in L346.

Paragraphs in Lines 210-215 are related to the high-level discussion of “what is a skill” and therefore should be part of the exposition. 

The study would have a much better case if the authors could show measurable quantities like accuracy and the number of learned skills obtained from the model side by side with those obtained from actual language models.

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
This paper provides an unified mathematical framework to explain three phenomena with increasing size of language models: compute-optimal size scaling, emergent capabilities, and performance plateauing. This framework is proposed based on the notation of learning as two levels: (1) a set of concepts are learnt from a set of texts;  (2) learning concepts enables the language model to acquire skills. The authors prove the compute-optimal (Chinchilla) scaling rule based on non-asymptotic information-theoretic tools to the bipartite graph between texts and concepts, and explain the emergence and plateauing phenomena based on the density of connections in the skill-graphs.

### Strengths
This paper has some strengths:

+ The authors can explain three phenomena mentioned above by using their unified framework. 
+ The trick to solve the optimisation problem (1) by considering the peeling process of learning concepts from texts to be identical to belief propagation decoding of an LDPC code when the channel noise is erasure is interesting.

### Weaknesses
This paper contains some weaknesses:
+ Some mathematical approximations should be carefully re-thought (please see my question below).
+ The gap between empirical excess entropy and its lower bound are too big.

+ The justification for using the peeling process of learning concepts from texts as analogous to belief propagation decoding of an LDPC code with erasure channels is not fully convincing. While the analogy is interesting, the underlying assumptions and their validity in the context of language model training need more rigorous examination. Specifically, the assumption that concept learning can be modeled as a simple erasure channel seems overly simplistic, given the complex nature of semantic understanding and concept formation in language models.


### Questions
The LHS of (4) is an expression that does not depend on $\epsilon$. However, the approximation expression in the RHS of (4) depends on $\epsilon$. How can we explain about this approximation? Can $\epsilon$ take arbitrary value as mentioned in the proof  in Appendix A.2?

### Soundness
3

### Presentation
2

### Contribution
2
