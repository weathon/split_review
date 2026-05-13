# Exact Byte-Level Probabilities from Tokenized Language Models for FIM-Tasks and Model Ensembles

- Decision: Accept
- Scores: 8, 5, 6, 6

## Abstract
Tokenization is associated with many poorly understood shortcomings in language models (LMs), yet remains an important component for long sequence scaling purposes. This work studies  how tokenization impacts  model performance by analyzing and comparing the stochastic behavior of tokenized models with their byte-level, or token-free, counterparts. We discover that, even when the two models are statistically equivalent, their predictive distributions over the next byte can be substantially different, a phenomenon we term as ``tokenization bias''. To fully characterize this phenomenon, we  introduce the Byte-Token Representation Lemma, a framework that establishes a mapping between the learned token distribution and its equivalent byte-level distribution.  From this result, we develop a next-byte sampling algorithm  that eliminates tokenization bias without requiring further training or optimization. In other words, this enables zero-shot conversion of tokenized LMs into statistically equivalent token-free ones. We demonstrate its broad applicability with two use cases: fill-in-the-middle (FIM) tasks and model ensembles. In FIM tasks where input prompts may terminate mid-token, leading to out-of-distribution tokenization, our method mitigates performance degradation and achieves an approximately 18\% improvement in FIM coding benchmarks, consistently outperforming the standard token healing fix. For model ensembles where each model employs a distinct vocabulary, our approach enables seamless integration, resulting in improved performance (up to 3.7\%) over individual models across various standard baselines in reasoning, knowledge, and coding.


\iffalse
Current state-of-the-art language models are trained on tokenized input sequences using a cross-entropy loss. We demonstrate that while any auto-regressive model may capture the source distribution optimally, tokenization introduces sampling bias.

We characterize this phenomenon with the Byte-Token Representation Lemma that describes a mapping from the learned tokenized distribution to an equivalent character- or byte-level distribution.
From our lemma, we derive a next-byte prediction method that can be applied to any tokenized language model and is statistically equivalent but does not suffer from bias.
Our method requires no additional training or optimization. We illustrate its broad applicability with two use cases: model ensembles and fill-in-the-middle (FIM) tasks. For model ensembles, we show that our approach enables the use of any ensemble method, consistently outperforming individual models on reasoning, knowledge, examination, math, and coding tasks. In FIM tasks, where input prompts may end mid-token, leading to out-of-distribution tokenization, our method avoids performance degradation, improving FIM coding benchmarks by approximately 18\%, akin to token healing. %We even observe slight performance improvements that we can not explain with the analysis presented in this work alone. % matt - might recommend to remove this last sentence
\fi

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper reveals a fundamental issue in language models regarding tokenization bias - where tokenized and byte-level models, despite being statistically equivalent, produce different predictive distributions. The authors introduce the Byte-Token Representation Lemma, providing a framework to convert tokenized language models into statistically equivalent token-free ones without additional training. They demonstrate practical applications in fill-in-the-middle tasks and model ensembles, achieving significant improvements: 18% on FIM coding benchmarks and up to 3.7% on ensemble tasks. The paper provides both theoretical foundations and practical implementations through efficient algorithms for cover encoding search and next-byte sampling.

### Strengths
The authors attempted to address a critical problem on tokenization for LLMs. They are the first to introduce tokenization bias and its effects on model behavior. They present a theory of it and introeduced efficient implementation of the algorithm.

The authors also studied the practical impact of the proposed solution through both code generation task (FIM, speficially) and model emsambles. Results indicate that this training-free approach is working well.

### Weaknesses
While the current results are great, it'd be better if authors can also cover tasks other than FIM that suffer from this issue, e.g. complete a story in natural language or generic code completion task that doesn't require FIM.

The authors discussed computational overhead but doesn't thoroughly analyze the latency impact especially in a practical setting. It'd be better if authors can study these as part of the experiments authors conducted.

The interaction between the proposed byte-level prediction method and popular sampling techniques (like  top-p, top-k) have not been explored enough, especially in the ensemble context.

### Questions
See weakness above. In addition, 

1. Do authors plan to open-source the implementation?

2. There is also a line of work similar to token healing and seems working well in both code and text. Could the authors study it and see whether the token alignment method could mitigate the issue especially in single-model completion tasks? 
Token Alignment via Character Matching for Subword Completion https://aclanthology.org/2024.findings-acl.929.pdf

### Soundness
3

### Presentation
3

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
This paper investigates the impact of tokenization on the performance of language models, particularly highlighting a phenomenon called "tokenization bias." This bias comes from the discrepancies between the predictive distributions of tokenized LMs and their statistically equivalent byte-level distribution when predicting the next byte or token. In this paper, they introduce the Byte-Token Representation Lemma (BTR Lemma) to map between the token and byte domain, which allows the computation of exact byte-level probabilities without requiring extra modification of the model. This method identifies "cover encodings" for a given byte string which are all possible valid tokenizations of a string that "optimally" contain the string in the prompt. Experiments on FIM code completion task and model ensemble task show that the proposed method improves model performance.

### Strengths
* This paper defines the tokenization bias phenomenon, which could cause performance issues in practical scenarios. 
* They evaluated the proposed method on FIM code completion task and mode ensemble task. 
* The proposed byte-level prediction method considers both the accuracy and efficiency in recovering the unbiased byte-level distribution.

### Weaknesses
 * This paper defines the tokenization bias phenomenon, which could cause performance issues in practical scenarios. 
* They evaluated the proposed method on FIM code completion task and mode ensemble task. 
* The proposed byte-level prediction method considers both the accuracy and efficiency in recovering the unbiased byte-level distribution.

* This method is very similar to the ACL 2024 paper 'Token Alignment via Character Matching for Subword Completion' which addresses the same issue and proposes more evaluation scenarios. However, in this paper, they didn’t compare with the token alignment method. 

* Based on the results shown in Figure 6, the improvement of the proposed method on the FIM evaluation tasks in sampling settings (pass@10) over the token-level with token healing method is very minor. For example, from 84.0 to 84.1. Why is that? 

* The evaluation scenarios are limited. Only two types of tasks are covered. How’s the performance of the method on general completion tasks without the FIM setting? Does the tokenization bias also have an impact on natural language completion tasks?

### Questions
* How is the proposed method compatible with other tokenization algorithms besides BPE and MPE?
* What do the right two sub-figures mean in Figure 6?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper provides a thorough investigation into the phenomenon of tokenization bias in language models, proposing a byte-level prediction method to mitigate this bias. The approach has promising implications, especially for tasks like fill-in-the-middle (FIM) in coding and for model ensembling. The idea of combining language models with distinct tokenizations at the logit level recalls older ensemble methods, commonly used before tokenization became mainstream in modern LLMs. The proposed method, underpinned by the Byte-Token Representation Lemma and efficient sampling algorithms, allows for effective ensemble models by bypassing tokenization restrictions, facilitating seamless integration across diverse language models.

### Strengths
What I really liked about this paper is that it very systematically investigates the phenomenon of tokenization bias. It develops a byte level prediction method and overcomes the bias. The applicability of this method and the findings in the paper have implications in areas such as coding where fill in the middle is crucial as well as in model ensembling. The idea of combining ensembles of foundation models at the logit layer is very appealing. Back in the day when there were no tokens and LMs were being built on whole words, ensembling using to be the norm in any practical LM based applications, such as speech recognition. With varying tokenization powering different LLMs today, the ability to freely combine any LLM with each other became restrictive. This paper proposes byte level efficient sampling algorithms and in conjuction with the byte-token representation lemma and the associated theoretical foundation, now allows the community to confidently combine predictions from any LLMs. Tokenization allows the LMs to overcome closed vocabulary limitation and from my perspective, this paper further allows us to overcome distinct vocabulary challenges associated with model ensembling.

### Weaknesses
While the results are promising for fill in the middle (in coding) tasks, I would have liked to see experimentation on other tasks to ascertain this method's generalizability to a wider variety of tasks, espically those that require context senstitive token predictions. Computer use, a new usecase demonstrated by companies such as Anthropic, could be a good use case that the authors could consider as an example.

An area that authors could delve further into is more analysis on the tokenization bias in multi step or long context tasks. It's not clear how the tokenization bias might compound over multiple steps, especially in tasks that require maintaining a consistent context or reasoning chain. For example, in tasks requiring multi-turn dialogue or complex reasoning, the accumulation of tokenization biases could lead to significant deviations from the intended output.

In order to truly appreciate the need for this research, its important to know just how much diversity there exists in tokenization vocabulary across different LLMs today. It would be beneficial to see a quantitative analysis of the vocabulary overlap and differences between various popular LLMs. Without this, it's difficult to assess the practical impact of the proposed method. If tokenization schemes are converging, the practical advantages of this work might be limited.

### Questions
I am curious what do authors think about the generalizability of their methods to non-deterministic tokenization or in applications that involve mixed token vocabularies ? Could some experimental results be shown to further strengthen the paper ? 

How do authors explain the not-so-strong gains with ensebling (Table 1 and Table 2). It was not clear how the models are being ensembled together? I would have also liked to see other combination strategies as a baseline e.g. consensus voting or ranking over diverse samples from different LMs. Are these experimental results available ? 

In order to truly appreciate the need for this research, its important to know just how much diverseity there exists in tokenization vocabulary across different LLMs today. To that end, I would like to see some sort of distribution characterizing the popularity of tokenization and distribution of vocabulary sizes across various LLMs. If the world is already coverging to one tokenization and the vocabulary of tokens homogenizes over time, then what practical advantages does this paper bring ? We should debate whether or not this is true and I would like to see authors providing their rebuttal.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Tokenization is a common pre-processing step, which shortens input sequences by mapping multiple bytes to discrete tokens. 
Prior work finds: Even for unlimited data and compute, tokenized models can achieve better cross-entropy loss vs. untokenized models
One hypothesis for why tokenization helps is that it allows models to handle longer contexts at less compute
Main problem: there are certain combinations that cannot be represented in token space, limiting the model’s abilities. This is harmful esp. for prompts that end mid-token.
Approach: this work presents a way to predict when tokenization is getting in the way and converts tokenized LMs into statistically equivalent byte-level models

### Strengths
- The characterization of the tokenization bias phenomenon, with examples / and the synthetic example with a 3rd order Markov chain, is very interesting and useful to the community
- The paper is well-written and studies an important problem

### Weaknesses
 - The code infilling setting is an interesting example of where this work could be useful. However, it is not clear why the prefix would stop in the middle of a token/word or why new tokens would arise at inference time. Why are the <PRE>, <MID>, and <SUF> tokens needed? Why is the study restricted to two prompting formats/are others possible? Since tokenization schemes are lossless, it seems like any prefix should be representable with the set of available tokens at training time. Further explanation of the evaluation setting and why it is realistic would be helpful.
- Several prior methods can ensemble the predictions from models that do not share a vocabulary, or ensemble multiple predictions from a single model. It is not clear whether the ensembling method proposed in this paper would outperform these methods. The motivation that byte-representations help ensembling is not fully examined due to the lack of these comparisons.
- It would be useful to provide decoding efficiency metrics corresponding to each decoding approach in Figure 6 since efficiency is a motivation in Section 4.

### Questions
In the caption for Figure 2, should the probability of sampling “A” on the LHS be $(1 - \alpha)$? It states the probability is $\alpha$.

I would be willing to change my opinion based on the responses to the weaknesses!

### Soundness
3

### Presentation
3

### Contribution
3
