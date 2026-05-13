# Towards Understanding Multi-Round Large Language Model Reasoning: Approximability, Learnability and Generalizability

- Decision: Reject
- Scores: 5, 3, 6, 5

## Abstract
Recent advancements in cognitive science and multi-round reasoning techniques for Large Language Models (LLMs) suggest that iterative thinking processes improve problem-solving performance in complex tasks. Inspired by this, approaches like Chain-of-Thought, debating, and self-refinement have been applied to auto-regressive LLMs, achieving significant successes in tasks such as mathematical reasoning, commonsense reasoning, and multi-hop question answering. Despite these successes, the theoretical basis for how multi-round reasoning enhances problem-solving abilities remains underexplored.
In this work, we investigate the approximation, learnability, and generalization properties of multi-round auto-regressive models. We show that Transformers with finite context windows are universal approximators for steps of Turing-computable functions and can approximate any Turing-computable sequence-to-sequence function through multi-round reasoning. We extend PAC learning to sequence generation and demonstrate that multi-round generation is learnable even when the sequence length exceeds the model's context window. 
Finally, we examine how generalization error propagates across rounds, and show how the aforementioned approaches can help constrain this error, ensuring outputs stay within an expectation boundary. This work sheds light on the systemic theoretical foundations of multi-round sequence learning and reasoning, emphasizing its role in inference complexity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In the paper, the authors aim to show that Transformers are universal approximators and that multi-round generation is learnable.

### Strengths
Well written paper.

### Weaknesses
In the current version, I do not see a significant contribution to ICLR.

I see the key contributions, Lemma 4.1 and Theorem 4.3, and the following basic assumptions and Lemmas, as not significant and novel for the following reasons:
1) The paper overall and section 4 in particular vastly ignores previous work, i.e. the contributon by Hava Siegelman in the 1990's showing (and proofing) that RNNs are super-Turing for two main arguments: continuous weight space and continuous activation functions. A transformer is an extension of an RNN (with a finite time window) with generalised access to information due to the attention mechanism. Thus, it is obvious that a Transformer exists that can simulate an arbitrary TM.
2) The paper provides a trivial sketch for Lemma 4.1 but not a sound mathematical proof.
3) Related to 1), the theoretical computational complexity of RNNs and Transformers is long known, as an RNN/Transformer can solve any problem in NP, but thus it is impossible to find the respective Transformer configuration. In fact, the main difficulty is to show that the available training and in-context learning or prompting mechanisms can yield such configurations. However, this is not sufficiently covered in the paper (i.e. section 5), as the focus lies on the complexity of the information/sample, but not on the currently used training algorithm.

### Questions
none.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors present a theoretical analysis of the approximation ability, learnability, and generalizability of multi-round transformer models (e.g., transformers augmented with prompting techniques such as chain-of-thought, etc). Though the subject is interesting and the findings potentially quite consequential (deriving sample complexities for multi-round transformer training), the paper and the proofs are difficult to follow, with many missing definitions and insufficiently unexplained proof steps.

### Strengths
- The authors present a theoretical characterization of the learnability of transformer models with multiple rounds. They specifically show that using multi-round inference helps to make learning more efficient, at least in principle.
- The authors also characterize the generalization ability of such models.

### Weaknesses
 The authors present a theoretical analysis of the approximation ability, learnability, and generalizability of multi-round transformer models (e.g., transformers augmented with prompting techniques such as chain-of-thought, etc). Though the subject is interesting and the findings potentially quite consequential (deriving sample complexities for multi-round transformer training), the paper and the proofs are difficult to follow, with many missing definitions and insufficiently unexplained proof steps.

 2

 3

 3

 - The authors present a theoretical characterization of the learnability of transformer models with multiple rounds. They specifically show that using multi-round inference helps to make learning more efficient, at least in principle.
- The authors also characterize the generalization ability of such models.

 - A number of critical proof steps are unclear or not sufficiently well-explained (see questions below).
- There are some missing definitions that make it difficult for readers to understand a number of key points.

 I list more detailed comments and questions below. In addition, there are a small number of typos and grammatical errors, especially with respect to grammatical number agreement. I include such errors below for the first two sections, but the list is not comprehensive and I encourage the authors to re-read the manuscript more thoroughly and correct all such errors.

Line 77: "and then auto-regressive generating sequence"
  Typo/grammatical error?

Line 83: Could you please specify what parameter or variable this quantity is exponential in? Is it the sequence length, model size, or something else?

Line 117: "LLM" -> "LLMs"

Line 120: "context" -> "contexts"

Line 142: "limitation" -> "limitations"

Line 161: "long sequence generation task" -> "the long sequence generation task" or "long sequence generation tasks"

Line 216: Missing space after "where:"
  What is the meaning of the notation "q_0 x #"?

Line 219: \Gamma^* Q \Gamma^* is undefined.

Proof of 4.1: This proof is difficult to follow and understand. Many variables are undefined (e.g., What is the acceptance window k? What is h_t?). The length of the tape encoded in the hidden state must be proportional to the number of steps simulated by the model, right? How is the orthogonality of each aspect of the embedding maintained in the output layer after residual connections? Wouldn't the residual connections destroy the surjectivity of the encoding (i.e., the hidden state now encodes a mixture of two Turing machine configurations)? Why is the characterization of the transformer as a Boolean circuit necessary for the proof? In section A.5.2., Q is bounded below by 2^{\epsilon*\varepsilon/(L*d*k)}. Where does this expression come from? This inequality would imply that as the error thresholds go to zero, the lower bound on Q goes to 2^0 = 1, which is nonsensically trivial. Section A.5.3. provides a set of "requirements" or conditions on the transformer's implementation of the state transition function, but does not provide a construction of such an implementation. In general, this proof needs additional details to more clearly and precisely explain its steps, to more effectively convince the readers of its correctness.

Line 797: "Combing" -> "Combining"? (line 799 too)

Proof of 4.3: How is the output of one round of transformer computation encoded as a single output token? This output token is then appended to the input for the next round of transformer computation. Then how is the corresponding Turing machine configuration recovered from the newly-appended token to proceed with the simulation of the Turing machine?

Assumption 5.3: A comment on the Lipschitz-continuity and boundedness of the cross-entropy function would be useful here, akin to Assumptions 5.1 and 5.2.

Line 895: Missing citation.

Section 5.3: The definition of "round" here is imprecise. Does a round not correspond to a single forward pass in a transformer model? How is generating N tokens in R rounds (where each round produces N/R tokens) different from generating N tokens in a single round? Would it not require a total of N forward passes in either case? Do the rounds indicate the frequency of supervising information during the intermediate steps of sequence generation? More clarity is needed.

How the learnability analysis in Section 5 builds upon or relates to the approximation ability discussed in Section 4?
Please clarify how the generalization analysis in Section 6 connects to both the approximation and learnability results.

### Questions
I list more detailed comments and questions below. In addition, there are a small number of typos and grammatical errors, especially with respect to grammatical number agreement. I include such errors below for the first two sections, but the list is not comprehensive and I encourage the authors to re-read the manuscript more thoroughly and correct all such errors.

Line 77: "and then auto-regressive generating sequence"
  Typo/grammatical error?

Line 83: Could you please specify what parameter or variable this quantity is exponential in? Is it the sequence length, model size, or something else?

Line 117: "LLM" -> "LLMs"

Line 120: "context" -> "contexts"

Line 142: "limitation" -> "limitations"

Line 161: "long sequence generation task" -> "the long sequence generation task" or "long sequence generation tasks"

Line 216: Missing space after "where:"
  What is the meaning of the notation "q_0 x #"?

Line 219: \Gamma^* Q \Gamma^* is undefined.

Proof of 4.1: This proof is difficult to follow and understand. Many variables are undefined (e.g., What is the acceptance window k? What is h_t?). The length of the tape encoded in the hidden state must be proportional to the number of steps simulated by the model, right? How is the orthogonality of each aspect of the embedding maintained in the output layer after residual connections? Wouldn't the residual connections destroy the surjectivity of the encoding (i.e., the hidden state now encodes a mixture of two Turing machine configurations)? Why is the characterization of the transformer as a Boolean circuit necessary for the proof? In section A.5.2., Q is bounded below by 2^{\epsilon*\varepsilon/(L*d*k)}. Where does this expression come from? This inequality would imply that as the error thresholds go to zero, the lower bound on Q goes to 2^0 = 1, which is nonsensically trivial. Section A.5.3. provides a set of "requirements" or conditions on the transformer's implementation of the state transition function, but does not provide a construction of such an implementation. In general, this proof needs additional details to more clearly and precisely explain its steps, to more effectively convince the readers of its correctness.

Line 797: "Combing" -> "Combining"? (line 799 too)

Proof of 4.3: How is the output of one round of transformer computation encoded as a single output token? This output token is then appended to the input for the next round of transformer computation. Then how is the corresponding Turing machine configuration recovered from the newly-appended token to proceed with the simulation of the Turing machine?

Assumption 5.3: A comment on the Lipschitz-continuity and boundedness of the cross-entropy function would be useful here, akin to Assumptions 5.1 and 5.2.

Line 895: Missing citation.

Section 5.3: The definition of "round" here is imprecise. Does a round not correspond to a single forward pass in a transformer model? How is generating N tokens in R rounds (where each round produces N/R tokens) different from generating N tokens in a single round? Would it not require a total of N forward passes in either case? Do the rounds indicate the frequency of supervising information during the intermediate steps of sequence generation? More clarity is needed.

How the learnability analysis in Section 5 builds upon or relates to the approximation ability discussed in Section 4?
Please clarify how the generalization analysis in Section 6 connects to both the approximation and learnability results.

### Soundness
2

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
1

### Summary
This paper provides a theoretical analysis of multi-round reasoning in auto-regressive language models. It first shows that, from an approximation perspective, Transformer models with a limited context window size can serve as universal approximators for Turing-computable functions. Then, it shows from a learnability standpoint, PAC learning can be extended to finite-size window next-token prediction and sequence generation. Finally, it shows from a generalization perspective, generation error can propagate between rounds of multi-round generation, but proper interventions can mitigate this effect to ensure generated sequences remain within certain bounds.

### Strengths
- This paper provides a theoretical analysis of multi-round reasoning in large language models. The analyses are useful for understanding language models' capabilities for complex reasoning
- The paper is well written.

### Weaknesses
 - The authors briefly discuss the practical implications of the theoretical results. It would be even more interesting if they could consider including even simple results to support their claims and demonstrate the practical usage of the theoretical foundations.

 - The authors discuss how proper interventions can mitigate error propagation across multi-round reasoning. However, in practice, interventions may not always be positive; for example, self-refinement can sometimes be error-prone. How would the generalization dynamics change in such cases?

### Questions
- The authors discuss how proper interventions can mitigate error propagation across multi-round reasoning. However, in practice, interventions may not always be positive; for example, self-refinement can sometimes be error-prone. How would the generalization dynamics change in such cases?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
1

### Summary
This work analyzes the approximation, learnability, and generalization properties of multi-round auto-regressive models, including chain-of-thought, self-debate, self-refinement, and so on. This work provides a theoretical insight and analysis of the multi-round auto-regressive model.

### Strengths
After reading the paper, the following are the strengths.
* The solved problem is important. Previously, it was not clear whether a multi-round model works, or why it really works. This paper tries to build a theoretical analysis of the multi-round model.
* The paper analyzes multi-round models in a wind-range, including approximation, learnability, and generalization properties.

### Weaknesses
The following is the weakness:
* Is it possible to conduct any experiments to prove the claims? Or is there any way to prove that the analysis is correct?
* The paper only contains theoretical proof so it may not be easy for the reader to understand. Therefore, is possible, that the author could provide any other methods to support the claim, such as figures, table, or others.

### Questions
N/A

### Soundness
3

### Presentation
2

### Contribution
3
