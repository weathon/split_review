# How Capable Can a Transformer Become? A Study on Synthetic, Interpretable Tasks

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 6, 3, 8

## Abstract
Transformers trained on huge text corpora exhibit a remarkable set of capabilities, e.g., performing simple logical operations. Given the inherent compositional nature of language, one can expect the model to learn to compose these capabilities, potentially yielding a combinatorial explosion of what operations it can perform on an input. Motivated by the above, we aim to assess in this paper “how capable can a transformer become?”. Specifically, we train Transformer models on a data-generating process that involves compositions of a set of well-defined monolithic capabilities. Through a series of extensive and systematic experiments on this data-generating process, we show that: (1) Transformers can learn compositional structures from the training data and generalize to exponentially or even combinatorially many functions; (2) Composing functions by generating intermediate outputs is more effective at generalizing to unseen compositions, compared to generating no intermediate outputs; (3) The training data has a significant impact on the model’s ability to compose unseen combinations of functions; (4) The attention layers in the latter half of the Transformer seem critical to compositionality.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The research delves into the compositional capabilities of transformers, examining their potential to generalize to functions not present in their training data. Using a synthetic setup, the authors found that transformers can learn and generalize to an exponential or even combinatorial number of functions based on the compositional structure in the data. The nature of the training data plays a pivotal role in this generalization, with step-by-step compositions proving more effective than direct ones. Additionally, attention layers, particularly between layers 6-10, were identified as crucial for compositional generalization. While the study underscores the promise of transformers' compositional abilities, it also highlights the challenges and nuances of using synthetic data and poses further questions about the underlying mechanisms in transformers.

### Strengths
None

### Weaknesses
It is conceptually wrong to evaluate a  capability of "a Transformer" since it will depend on architecture, training data, training methodology etc.
Moreover I failed to identify which transformer was used in the paper.
Capability of each layer in a transformer is again depends on the number of heads, hidden dimension etc. therefore it is not correct to identify layers 6-10 as crucial layers for compositional generalization.
Overall, I perceive the paper as lacking scientific depth, offering merely a mechanical examination of an ambiguous model without a clear interpretation.

### Questions
None

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors study how well Transformers can learn to compose functions via a synthetic task of composing bijective functions. They study in-order and out-of-order generalization; and also step-by-step and direct computation the composed functions. They show that Transfomers can generalize well with step-by-step computation but not as well at direct computation. Similarly, in-order compositions are easier to generalize to compared to out-of-order compositions.

### Strengths
- The paper is clearly written and easy to follow.
 - The paper introduces a new and useful synthetic task to understand compositional generalization, that will be of use to the research community. 
 - The paper illustrates new compositional capabilities and limitations of Transfomers.

### Weaknesses
 - I think an ablation over the number of layers in the Transformer is a key missing study here. Many studies (e.g. [Weiss et al](https://arxiv.org/abs/2106.06981), [von Oswald et al](https://arxiv.org/abs/2212.07677)) show that the depth of a Transfomer is key to what it can compute, so I'd like to see a sweep over the number of layers in the Transfomer and how that affects compositional generalization.
 - I am not fully convinced that step-by-step computation implies compositional generalization. If the Transfomer is supervised with the outputs of the intermediate function results, isn't it then just learning 1. the individual functions and 2. that it should apply them sequentially? Maybe I'm missing something, but I'd definitely appreciate some sort of discussion around this in the paper. 
 - (nitpick, did not affect review score) Suggestion: I think the title of the paper could be a lot better to reflect what's in the paper. Perhaps "Studying compositional generalization in transfomers via synthetic bijective functions" or something along those lines.

### Questions
- To test if the Transfomer learned a certain composition of functions, how many examples (i.e. permutations of tokens) are used, and how are they constructed? Are experiments restricted to 6 non-unique tokens per example like in Figure 3? Unless I missed something, I think it'd be useful to clarify this. 
 - Will the authors release code/data to reproduce this paper? I imagine the code is not hard to write, but one benefit of such papers that use synthetic tasks and small models is that they should be easy to reproduce.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents an empirical study on how capable Transformer models are to generalize compositionally, a question that has been broadly discussed in the last 5 years in research literature. The specific task that the paper uses for the empirical study is composing functions defined on the domain of fixed-length works over a fixed vocabulary. The paper considers stepwise (i.e. with intermediate outputs) and direct composition (i.e. without intermediate outputs) setups. Another axis variation is whether the function order can be different at test time than training time (in-order vs out-of-order). The key observations are that (1) provided enough diversity in the training data, Transformers can learn to compose functions (2) stepwise composition is easier to learn.

### Strengths
The paper is mostly clearly written and easy to understand.

### Weaknesses
I don’t think that this paper makes a meaningful contribution to the field of deep learning on top of the already available work. The general question of whether Transformers or other neural architectures can generalize compositionally has already been discussed in numerous papers, including similar function compositional setups. The general consensus in the literature is that with enough diversity, any neural architecture can learn any compositional behaviors. Further interesting questions can be asked: what architectures can learn compositional behavior from less diverse training data, can we get diverse enough training data to achieve compositionality in real-world tasks (GPT-4 seems to partially answer that), how compositional generalization abilities of neural models compare to those of humans. This paper, however, does not go deeper into one of these or any other direction, it discusses compositional generalization and the highest most abstract level, at which the answer is: it depends. While the paper acknowledges that there is ample prior work on the topics, the paper fails to explain what it adds on top. The finding that step-wise composition is easier than direct is rather unsurprising, especially in the view of chain-of-thought prompting of LLM that has been getting popular lately.

Section 3.2 is a bit unclear on what are “bijection” and “permutation” mappings in the paper’s context. My understanding is that bijection here means per-token bijection, whereas permutation means shuffling tokens of the word. The details of what the vocabulary size and what the size of the word is were difficult to find.

### Questions
- Section 3.2 is a bit unclear on what are “bijection” and “permutation” mappings in the paper’s context. My understanding is that bijection here means per-token bijection, whereas permutation means shuffling tokens of the word.
- The details of what the vocabulary size and what the size of the word is were difficult to find.

### Soundness
3 good

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper investigates the capabilities of transformers to learn individual functions and compose them in a sequential manner. A major contribution of the study is the introduction of a synthetic dataset that is both interpretable and straightforward to implement.
While the paper is mostly well-written, it falls short in clearly describing the experimental setup. 



Overall, the paper is commendable for its innovative synthetic dataset, which provides valuable insights into the capabilities of transformers for function composition. However, the paper would benefit from greater clarity in its experimental descriptions and more robust support for some of its conclusions.

### Strengths
- The dataset introduced is both simple and valuable for future research.
- The paper presents perceptive experimental analyses, notably the discussion on the differences between in-order and out-of-order generalizations.

### Weaknesses
 - The experimental setup lacks sufficient clarity, making it challenging to understand the specific procedures.
- The paper's conclusion regarding the significance of later attention layers is not adequately substantiated by the experimental data; it lacks insight.
- Section 3.2 lacks a clear definition and differentiation between permutations and bijections. It should be explicitly stated that the results in Section 4.1 pertain only to bijections.
- Figure 3 needs more explanation about the notations. For instance, what $f_{i-j}$ means?
- The explanation between "random" and "21 base" in Section 4.1 is unclear.
- The bottom-left subplot in Figure 7 exhibits an anomalous trend compared to other subplots; could you please explain this? In particular, there is no clean trend that transformer first learn composition of more functions. 
- The experimental setup for Figure 6(b) in Section 4.3 is not elucidated. What is the rationale for having 25 bijections and 25 permutations?
 - The paper claims that adding permutations aids direct composition; this is a counterintuitive finding that warrants further elaboration.
- Figure 6(b) requires more detailed explanation, and several typos need rectification.


Typos:
 - In page 2, remove one of the "considered" and the quotation masks are not correct. 
 - in Figure 11: "direction composition" should be corrected to "direct composition."

### Questions
- Section 3.2 lacks a clear definition and differentiation between permutations and bijections. It should be explicitly stated that the results in Section 4.1 pertain only to bijections.
- Figure 3 needs more explanation about the notations. For instance, what $f_{i-j}$ means?
- The explanation between "random" and "21 base" in Section 4.1 is unclear. 
- The bottom-left subplot in Figure 7 exhibits an anomalous trend compared to other subplots; could you please explain this? In particular, there is no clean trend that transformer first learn composition of more functions. 
- The experimental setup for Figure 6(b) in Section 4.3 is not elucidated. What is the rationale for having 25 bijections and 25 permutations?
 - The paper claims that adding permutations aids direct composition; this is a counterintuitive finding that warrants further elaboration.
- Figure 6(b) requires more detailed explanation, and several typos need rectification.


Typos:
 - In page 2, remove one of the "considered" and the quotation masks are not correct. 
 - in Figure 11: "direction composition" should be corrected to "direct composition."

### Soundness
3 good

### Presentation
2 fair

### Contribution
4 excellent
