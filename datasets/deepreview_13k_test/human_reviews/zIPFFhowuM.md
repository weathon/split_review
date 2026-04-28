# Proof Search Augmented Language Models

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
Transformer language models (TLMs) exhibit an impressively general range of capabilities. A growing body of work aims to harness these models for complex reasoning problems expressed in natural language. However, recent theoretical and empirical results have revealed limits to the algorithmic generalization of TLM reasoning. Transformers trained to solve deduction problems from one distribution fail to solve instances of the same problem type drawn from other distributions. We propose to improve the systematic reasoning capabilities of TLMs via a differentiable proof search module, yielding proof-search augmented language models (PSALMs).
In a PSALM, a Transformer is responsible for predicting rule and fact representations for a neural theorem prover (NTP). The NTP performs a backward-chaining search over proofs, scoring them based on a soft unification operation. Our results show that PSALMs successfully generalize in deduction tasks where vanilla transformers do not learn systematic behavior, can be adapted to more natural text with only label supervision, and robustly handle large examples where proprietary LLMs make mistakes.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper focuses on multi-step reasoning tasks that require a model to predict whether a statement is true given unification rules and facts in natural language. The authors first define several rule templates that contain different numbers of unification terms, then train a Transformer and cross-attention module to fill the term slots with entities and their features from a sentence. Lastly, the extracted rule is input to a neural theorem prover to obtain the proof and the truth prediction. The author uses three types of supervision: label supervision, proof supervision, and rule supervision. Experiments show training with rule supervision can obtain 96.7% accuracy on the OOD test split.

### Strengths
The proposed method is effective. The experiments show the proposed method trained with rule labels can obtain nearly 100% accuracy on the OOD splits, which largely improves the previous methods.

### Weaknesses
- The evaluation dataset and the compared method are too simple. Since the paper claims current TLMs have limits in reasoning, it should compare with recent SOTA LLMs and show their incapability in a complicated benchmark.

- The comparison is unfair. The proposed method with proof and label supervision achieves inferior performance to baseline TLM and only obtains nearly 100% accuracy with rule-level supervision. A more appropriate baseline should also have these labels. For example, an LLM trained to generate text in "fun :- happy kind" format and predict the label with CoT.

### Questions
- Is there any harder QA benchmark that involves logic or multi-step reasoning suitable to evaluate the proposed method?

- How do current LLMs w/wo CoT perform in the SimpleLogic dataset?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors introduce Proof Search Augmented Language Models (PSALMs), a differentiable proof search module combined with a transformer. The authors propose an efficient hardware-aware method for proof search (at further depths than prior works) and pruning and performing ablations to identify the strengths of granular rule supervision.

### Strengths
- The paper presents multiple training objectives and studies which impact performance.
- An efficient and hardware-aware algorithm has been proposed for proof search.
- The authors show evaluations of the SimpleLogic dataset and generalization capabilities.

### Weaknesses
- There are limited empirical evaluations other than SimpleLogic.
- More investigation could be conducted into the scaling of the proof search.

### Questions
- How does the approach work on tasks other than SimpleLogic?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a PSALM model that combines a transformer-based language model with a proof search system. Compared to the NTP introduced by Rocktaschel & Riedel in 2017, it uses pruning and parallel execution to improve scaling and throughputs. Using a new loss term, the system provides significant improvements over a vanilla model for (limited) out-of-distrbution generalization.

### Strengths
The paper is well written and the key components are motivated and explained well. The experimental results seem to be systematic and convincing.

### Weaknesses
The novelty introduced in the paper seems limited. Pruning is well known; while it improves scaling, in the worst case, the complexity remains the same. Also the improvements over the vanilla model do not reflect the improvements over the state of the art transformer models.

The experimental results are not fully explained. For example, the row of PSALM L_{rule} in Table 1is not explained and no comments are provided in the paper even though it is a key result.

### Questions
- Could you explain the reasons why loss L_{rule} is minimized much smaller than the other two? It seems to me it shows that many entries in matrix T are zeroes.

- As a follow-up question, since the loss terms can be minimized to a different scale, should different weights improve the performance when combining them such as the results in Tables 1 and 2?

- Section 3.1 states that "Encoding rules independently prevents the TLM from “shortcutting” the NTP," could you provide corresponding empirical evidence and quantify the impact?

- Figure 3 shows the range of proof score is different from the case on the left and the case on the right. Could you explain how the larger range for L_{rule} affect its generalization and separation between positive and negative ones?

- Could you provide the key reasons underlying the big differences between the last two rows of Table 1 in terms of OOD accuracy and OOD soundness?

- I assume the vanilla TLM model is the DeBerta model with 435M parameters. However, there are manyother larger LLMs developed. Could you provide a baseline or baselines using state of the art LLMs?

- Could you explain how the proposed method overcomes the exploding computational cost compared to other methods? As far as I could understand, the pruning and parallelization do not change the nature of exponential growth.

- Could you comment on the complexity of the proposed system with respect to the depth? In addition to depths 5-6, could you provide results for depths 7, 10, and 20?

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
4

### Summary
Summary:

This paper applies an encoder-only model to represent the rule and statement in the proof. Then, the Neural Theorem Prover (NTP) utilizes the representation to perform a backward-chaning search of proofs and sort them.

Contributions:

This paper proposes a new method to improve the model reasoning abilities by semantics proof search. The experimental results on the SimpleLogic task are nice.

### Strengths
- This paper proposes a new method to improve the model reasoning abilities by semantics proof search. The experimental results on the SimpleLogic task are nice.

### Weaknesses
1. The experiment section is insufficient. First, only one dataset named SimpleLogic is used in the experiment. Second, the author only uses one model in the experiment. Last but not least, there are some work aimed to improve the proof reasoning abilities. However, I have not seen the gap between those work and the method proposed by the authors.

2. The terminology in this article is not to the standard. For instance, we typically refer "transformer" to encoder-decoder architecture models instead of encoder-only models.

### Questions
1. Why are language models such as Llama not used in the experiments?
2. If language models are used, do we still need the complex procedure to make it work?

### Soundness
2

### Presentation
2

### Contribution
2
