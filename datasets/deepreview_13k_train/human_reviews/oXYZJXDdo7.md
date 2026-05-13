# Retrieval is Accurate Generation

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Standard language models generate text by selecting tokens from a fixed, finite, and standalone vocabulary. We introduce a novel method that selects context-aware phrases from a collection of supporting documents. One of the most significant challenges for this paradigm shift is determining the training oracles, because a string of text can be segmented in various ways and each segment can be retrieved from numerous possible documents. To address this, we propose to initialize the training oracles using linguistic heuristics and, more importantly, bootstrap the oracles through iterative self-reinforcement. Extensive experiments show that our model not only outperforms standard language models on a variety of knowledge-intensive tasks but also demonstrates improved generation quality in open-ended text generation. For instance, compared to the standard language model counterpart, our model raises the accuracy from 23.47\% to 36.27\% on OpenbookQA, and improves the MAUVE score from 42.61\% to 81.58\% in open-ended text generation. Remarkably, our model also achieves the best performance and the lowest latency among several retrieval-augmented baselines. In conclusion, we assert that retrieval is more accurate generation and hope that our work will encourage further research on this new paradigm shift.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Retrieval augmented generation models are very powerful  in making generation more attributable and trustworthy. The proposed approach in the paper belongs to this family. It is inspired from CoG (Lan et al.)  that retrieves phrases from similar contexts, however, unlike CoG, it doesn’t employ a two-stage pipeline, specifically document retrieval followed by grounded phrase extraction. The proposed approach removes the dependence on document retrieval. 

Interestingly, the authors propose to use linguistics-motivated heuristics to initialize the training oracle phrases, followed by a bootstrapping mechanism through self-reinforcement to refine the oracle with each iteration. This linguistically inspired approach could be very useful in providing meaningful attributions to their sources. 

The experiments on Open-book qa and open ended generation show consistent improvements over competitive baselines.

### Strengths
The proposed approach seems very interesting and will be useful to the generation community. As I mentioned earlier, the linguistically inspired approach could be very useful in providing meaningful attributions to their sources. 

Strong results on a variety of benchmarks from Open book qa and open ended generation tasks.

==

Most of my concerns were adequately addressed in the authors rebuttal. Please include these details in the camera ready version if accepted. I have update my reviews accordingly.

### Weaknesses
The authors proposed a very interesting approach but I felt a lot of important details are missing. Please see my questions/comments below. It is unclear whether or not the code will be released from this work.

Another weakness of the work I believe is that this approach will not be robust to languages or domains where our syntactic parsing capabilities are limited.

“each phrase possesses a relatively complete and well-defined meaning” -> Will this approach be not generalizable to languages and domains where the availability of syntactic parsers is limited? Also is it feasible to annotate the whole training set?

“Incorporating high-frequency phrases can significantly increase the total number of phrases, leading to an extremely large candidate pool” -> Won’t the low-frequency phrases significantly increase the size of the candidate pool?

Second paragraph under “Semantic similarity”: I felt lots of details were missing here to better understand the quality of phrases, and the feasibility of the proposed approach. The Appendix A do not provide all necessary details. Is this done on the pretraining corpus? What trivial constituents were dropped out and why (some examples would help)?

Sec 3.2.2: I found the explanation a bit confusing. Could you add an algorithm and/or an example demonstrating the algorithm?

“If no such phrase is found, we retain the previous target.” -> When would this occur? When the candidate pool is empty?

“we also add the token vocabulary to our phrase table” -> Are they subword units? What is the vocabulary?

“We train our model on the training set of MiniPile2 (Kaddour, 2023)” -> What is this dataset? Is it a pretraining set of finetuning set? How are they used during training? This dataset is discussed again in 5.2.

“Note that the sum of all possible paths can be computed efficiently using dynamic programming with time complexity O(n 2 ), where n represents the number of tokens in the text” -> Will this be limiting for long form outputs?

Table 1: Are the numbers for baselines taken from the respective papers or are they reproduced by the authors?

Sec 6: Results: This should be Sec 5.2.2?

### Questions
“each phrase possesses a relatively complete and well-defined meaning” -> Will this approach be not generalizable to languages and domains where the availability of syntactic parsers is limited? Also is it feasible to annotate the whole training set?

“Incorporating high-frequency phrases can significantly increase the total number of phrases, leading to an extremely large candidate pool” -> Won’t the low-frequency phrases significantly increase the size of the candidate pool? 

Second paragraph under “Semantic similarity”: I felt lots of details were missing here to better understand the quality of phrases, and the feasibility of the proposed approach. The Appendix A do not provide all necessary details. Is this done on the pretraining corpus? What trivial constituents were dropped out and why (some examples would help)? 

Sec 3.2.2: I found the explanation a bit confusing. Could you add an algorithm and/or an example demonstrating the algorithm? 

“If no such phrase is found, we retain the previous target.” -> When would this occur? When the candidate pool is empty? 

“we also add the token vocabulary to our phrase table” -> Are they subword units? What is the vocabulary? 

“We train our model on the training set of MiniPile2 (Kaddour, 2023)” -> What is this dataset? Is it a pretraining set of finetuning set? How are they used during training? This dataset is discussed again in 5.2.

“Note that the sum of all possible paths can be computed efficiently using dynamic programming with time complexity O(n 2 ), where n represents the number of tokens in the text” -> Will this be limiting for long form outputs? 

Table 1: Are the numbers for baselines taken from the respective papers or are they reproduced by the authors?

Sec 6: Results: This should be Sec 5.2.2?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper combines retrieval with test generation and introduces an approach at retrieves context-aware phrases from a database of documents for generation. They use a set of linguistics heuristics combined with a bootstrapping method to extract phrases. The authors have done studies to show the effectiveness of their method and perform ablation study on the effect of different elements. They also study the inference speed of their approach and compare it with other approaches.

### Strengths
- The paper is well written and easy to follow.
- Their approach on text generation and selecting phrases is novel and introduces an interesting approach to text generation.
- The authors study the effectiveness of their approach well and provide comparisons with other approaches.
- Their zero-shot results on knowledge intensive tasks is convincing of the effectiveness of their approach.

### Weaknesses
 - Lack of any human evaluations: Although there are automatic metrics for text generation, there still a need to have humans judge the generation.
- The paper does not provide deep insights into the observed results. For example, Section 6, Main Results, related to Table 4, it is not clear why the MAUVE score has such a huge jump for their method, or why finetuning the base model drops this score by a lot.

### Questions
- What corpus is used to finetune the base model?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces a novel method for language modeling that instead of generating tokens, retrieves phrases from a phrase-based index. This differs a lot from standard language models, which generate text by selecting tokens from a fixed, finite, and standalone vocabulary. Furthermore, this new approach leverages a more balanced encoding architecture for both the input and target tokens, as opposed to a single token embedding layer on the target side employed in standard language models. Moreover, their paradigm is the first that performs text generation through direct phrase retrieval, steering away from common 2-staged pipeline approaches, and thus removing the dependence on document retrieval and achieving lower latencies.
The authors shed light on how to determine the training oracles that allow this kind of training, and they propose to initialize them using linguistic heuristics. Also, in order to allow the model to adjust its own generation paths based on the capabilities it has acquired, they also bootstrap the oracles through iterative self-reinforcement, which gradually refines the oracles with each iteration by transitioning from imitating the oracles to reinforcing its own preferences.
In this new paradigm, text generation is achieved by copying retrieved phrases corresponding to constituent units in a syntactic parse tree, but the model still has the ability to generate individual tokens.
The effectiveness of their models is validated on various downstream tasks, including open-domain and domain-specific question answering, as well as open-ended text generation, attaining substantial improvements over standard LMs and several retrieval-augmented baselines. Transitioning to phrase retrieval improves interpretability and factuality on text generation tasks, as the semantics of phrases are enhanced by their surrounding contexts, and each retrieved phrase can be traced back to its original document. Finally, enlarging the phrase index during inference, and the plug-and-play feature of the index are shown to be effective and efficient methods for boosting the model's performance and adapting to out-of-domain distributions respectively, without any further training.

### Strengths
- A novel approach for retrieval augmented generation 
- Holistic evaluation not only by measuring the fluency in open-ended text generation but also by carrying out comprehensive evaluation in a wide range of knowledge-intensive tasks, such as open-domain question answering.
- Plug-and-play feature of the phrase index, as a way of adapting to out-of-domain distributions (such as the Medical domain) by simply changing/extending the phrase index with a domain-specific index without any further training.
- Paper is generally well written and easy to follow
- Good explanation of how standard LLMs can be viewed as dual-encoding matching networks connecting different prefixes and tokens, and shedding light into the architecture imbalances between the prefix and the target encoders.

### Weaknesses
Weaknesses:
- More implementation details regarding the size of the phrase index, etc would be good to have in the paper.
- The work might also benefit from some discussion regarding scalability of the phrase index

Minor suggestions:

- As Figure 1 is the main overview of the approach proposed in the paper, a more detailed footnote would be appreciated.
- Section 6 "Results" wouldn't be better under subsection 5.2.2, as it reflects on results from the Open-Ended Text Generation experiments.
- Typos: Section 2, line 2. "The" after "Hence, " should be in lower-case.

Missing references:
- Minjoon Seo's work on phrase index QA: https://arxiv.org/pdf/1804.07726.pdf, https://arxiv.org/pdf/1906.05807.pdf

### Questions
- Could you discuss any potential limitations or failure cases of the model, providing insights into scenarios where the proposed approach might not perform as effectively?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper explores text generation, specifically by creating a larger vocabulary which additionally consists of phrases extracted from a large corpus via certain rules, and whose representations are formed by a transformer model encoding the wider context they appear in. 
When decoding the model is then able to either generate standard tokens, or longer phrases. 
Results are presented on open generation and question answer generation tasks, showing that the proposed model is able to perform more accurately than 3 other recent retrieval based baselines.

### Strengths
* Solid set of empirical results are presented showing the model performs well on the tested tasks. 
* Comparisons against recent baselines are given. 
* Additional phrase representations (produced by the same model used in training) are able to be added at inference time, with the decode model able to operate with these extra, new phrases. 
* The method removes the inference-time dependence on document retrieval that other retrieval augmented generation papers have. It does move this phrase creation process (along with the embedding of these) to training time.

### Weaknesses
 * The claims about inference speed are 
* Can examples or further clarification be given for the 3.1 sentence "enhancing the accountability of the output"? This isn't clear, at least to me. 
* There are a lot of heuristics in extracting the phrases. This may not be easy to repeat, or result in the same level of gains on other datasets or related problems. 
* The decoding method seems very custom. Forcing a limited use of phrases, and blending top-k and top-p sampling. What happens if you just arg-max decode from the resulting model? Does it emit phrases way too often?
* Distributional sparsity  -- this section is not very clear. 
* Is the likelihood estimation of summing paths well motivated? I'm not sure this is principled, but open to this being further justified. 
* "For efficiency issues" in 4.1, does this mean for stability? Keeping the embeddings (of tokens and phrases) means the problem is stable I presume. I think this needs more explanation however. 
* The numbers in table 1 are not described.

### Questions
* Was the vanilla LM trained with the phrase extended vocabulary? Or was this just using the gpt2 tokenisation alone? What happens if you  do this, rather than blending the contrastive phrase loss with the common CE loss?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
