# UncertaintyRAG: Span Uncertainty Enhanced Long-Context Modeling for Retrieval-Augmented Generation

- Decision: Reject
- Scores: 5, 6, 3, 5

## Abstract
We present \textit{UncertaintyRAG}, a novel approach for long-context Retrieval-Augmented Generation (RAG) that utilizes Signal-to-Noise Ratio (SNR)-based span uncertainty to estimate similarity between text chunks. This span uncertainty enhances model calibration, improving robustness and mitigating semantic inconsistencies introduced by random chunking. Leveraging this insight, we propose an efficient unsupervised learning technique to train the retrieval model, alongside an effective data sampling and scaling strategy. \textit{UncertaintyRAG} outperforms baselines by 2.03\% on LLaMA-2-7B, achieving state-of-the-art results while using only 4\% of the training data compared to other advanced open-source retrieval models under distribution shift settings. Our method demonstrates strong calibration through span uncertainty, leading to improved generalization and robustness in long-context RAG tasks. Additionally, \textit{UncertaintyRAG} provides a lightweight retrieval model that can be integrated into any large language model with varying context window lengths, without the need for fine-tuning, showcasing the flexibility of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces UncertaintyRAG, a novel long-context RAG framework that incorporates span-level uncertainty using the Signal-to-Noise Ratio (SNR) for similarity estimation between text chunks. This technique aims to improve calibration, reduce semantic inconsistencies from random chunking, and enhance model robustness under distribution shifts. The authors also propose an efficient unsupervised learning approach for training retrieval models with minimal labeled data, achieving state-of-the-art performance with a lightweight design that can integrate with various LLMs without fine-tuning.

### Strengths
1. The idea of using an SNR-based span uncertainty metric to calibrate the retrieval model is novel. Specifically, the method defines a chunk similarity metric based on the probabilities of the downstream decoder LLM, which can be used to train a retrieval model with contrastive learning.
2. The proposed method achieves better performance than existing retrieval models under distributional shifts in the context, proving it to be an easy-to-adapt retriever for a specific model.
3. The method can be trained on an automatically created dataset using self-supervised learning, reducing the need for manually labeled data.

### Weaknesses
1. Some content is difficult to understand. For example, in line 245, "The probability distribution within this window is stable," which does not seem to imply a stable distribution. Additionally, in Section 4.1, the phrase "number of chunks" is unclear, as the previous mention of the same term refers to the total number of chunks in the training set. It is unclear what aspect of the probability distribution is considered stable, and how this stability is quantified. Furthermore, the ambiguity around "number of chunks" makes it difficult to understand the experimental setup and results in Section 4.1.
2. The definition of the negative samples is questionable. It appears that the negative samples are among the top $M$ most similar chunks to the anchor. If this is the method for selecting hard negative examples, the hyperparameters in the paper would play a crucial role. Specifically, the method for selecting negative samples from the top $M$ most similar chunks may lead to the inclusion of semantically similar chunks, which could hinder the contrastive learning process. The paper lacks a clear explanation of how this selection strategy avoids the problem of selecting overly similar negative samples.
3. Numerous hyperparameters are introduced, such as the threshold $\sigma$, the number of samples $M$ and $m$, the chunk size, and the sliding window size. However, the authors do not explain how these hyperparameters were chosen or how sensitive the model is to these values. The lack of a sensitivity analysis for these hyperparameters makes it difficult to assess the robustness of the proposed method. It is crucial to understand how the performance varies with different hyperparameter settings to ensure the method's reliability.
4. It is challenging to conclude that the method can be integrated with any LLMs, given that uncertainty is only calculated using Llama 2 7B. The tested models also use Llama 2 as their base, which shares the same pretraining data. From Table 1, it is apparent that when the uncertainty score model does not match the LLM, the performance gain from the proposed method decreases. This raises doubts about whether the retriever must match the LLM used. The experiments do not sufficiently demonstrate the generalizability of the method across different LLM architectures and pretraining data. The observed performance drop when the uncertainty model and LLM do not match raises concerns about the practical applicability of the method in diverse settings.

### Questions
1. The chunks are divided based on a specific word length (300 in the paper). Below are questions regarding this design:
(1) It is possible for 300 words to correspond to more than 512 tokens for BERT. What would be your solution in this scenario?
(2) Do you consider punctuation as separators for words as well?
(3) If a chunk is cut mid-sentence, concatenating two "incomplete" sentences (chunks) may lead to a "sudden transfer" between them. This could affect uncertainty calculation. What are your thoughts on this?
2. What is the role of $N$ as defined in line 285?
3. How did you select the training and test sets from the LongBench suite?
4. Not all training and test sets feature distributional shifts in their contexts. For example, both HotpotQA and 2WikiMQA use Wikipedia as their source of context.
5. In line 451, how do you conclude that "RSA is an effective metric for assessing distribution shifts," given that you only have two data points (GSM8K and 2WikiMQA)?
6. The "10" mentioned in line 310 should be $k$.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents UncertaintyRAG, a novel method for improving long-context Retrieval-Augmented Generation (RAG) by utilizing span-level Signal-to-Noise Ratio (SNR)-based uncertainty for estimating the similarity between text chunks. The authors propose an unsupervised learning technique for training the retrieval model, coupled with an efficient data sampling and scaling strategy. The key insight is that the SNR-based span uncertainty can be applied to chunk similarity estimation. The method achieves state-of-the-art performance on LLaMA-2-7B, with a 2.03% improvement over baselines using only 4% of the training data. The authors also emphasize that UncertaintyRAG is lightweight and can be seamlessly integrated into any large language model without the need for fine-tuning.

### Strengths
1. The focus on SNR-based span uncertainty to enhance retrieval in long-context RAG tasks is novel. Uncertainty quantification has been explored in other domains, but its application in chunk similarity estimation for RAG tasks is a fresh and valuable contribution.
2. The authors provide a solid methodology for both retrieval model training and data sampling, with clear explanations of how span uncertainty is calculated and used to construct positive and negative samples.
3. The experiments demonstrates how span-level uncertainty improves performance across multiple datasets, including distribution shift settings where traditional models often struggle.

### Weaknesses
1. While the paper introduces SNR-based span uncertainty as a novel metric for estimating text chunk similarity, it fails to provide a compelling motivation for why SNR is the most appropriate choice for this task. The choice of SNR seems somewhat ad hoc, and the paper would benefit from a comparative study showing why SNR outperforms these other potential metrics in various retrieval scenarios.

2. The paper relies on a relatively simple fixed chunk size (e.g., 300 words per chunk) for dividing long-context documents. However, chunking is a critical aspect of Retrieval-Augmented Generation (RAG) systems, and the paper does not explore more sophisticated chunking methods, such as dynamic or semantic-based chunking. This is a significant limitation because fixed-length chunking can lead to semantic fragmentation, where important contextual information is split across chunks, reducing retrieval accuracy.

### Questions
1. Can you provide more detailed justification for why Signal-to-Noise Ratio (SNR) was chosen as the primary uncertainty metric for span-level similarity estimation? How does it compare to other uncertainty metrics？
2. How does your method handle ambiguous queries where there may be multiple valid retrievals or interpretations? Does the SNR-based uncertainty provide any benefit in disambiguating between competing chunks of text?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper presents an unsupervised retrieval approach developed for long-context retrieval-augmented generation (RAG), i.e. when RAG is used as a solution for processing long contexts in LLMs, by chunking long contexts and retrieving chunks relevant to the user’s query. The proposed unsupervised retrieval approach is trained using only chunk data, without any query data, and without using any external labeling of query-chunk relevance. A high-level intuition of the proposed retrieval approach is to produce labeling for whether two text chunks are semantically similar or not, based on the log-likelihood output by an LLM for a concatenation of the two chunks.  The proposed approach is tested in domain shift settings.

In more details, the paper introduces a signal-to-noise ratio (SNR) which is computed over token probabilities in a window of text, i.e. an average probability of each token in a window, divided by a variance of these probabilities (formula 2). The authors find empirically that for any piece of text, the SNR tends to decrease to small values, starting from some position in the text (Figure 1). Based on this observation, the Span uncertainty (SU) of a given piece of text is calculated as an average probability of tokens after the found position (formula 3).  An ablation on the necessity of using this position cut-off is presented in Table 1 (two last columns).

To obtain labeled data for training a retriever, the documents are first split into chunks of length 300. Chunks themselves act as search queries (“anchor” chunks), and for each anchor chunk top-M closest chunks are retrieved using bm25. Then SU scores are calculated for each concatenation of anchor chunk - bm25-retrieved chunk. The SU scores are used to split a set of bm25-retrieved chunks into positive and negative samples. Due to the infeasibility of considering all chunks as anchor chunks, a clustering procedure is employed to select a representative subset of anchor chunks.

### Strengths
* An important problem of training retrievers for domain shift settings is considered.
* Related work is broad and detailed, listing several relevant research branches and representative works in each branch.

### Weaknesses
1. Text needs substantial rewriting: many parts of the text are unclear and hard to understand. Below I give examples of argumentations which are unclear or incorrect. I was only able to understand the proposed method after reading the corresponding section several times. In addition, the figures in the text are too small.
2. The motivation for the proposed unsupervised retriever is unclear. The authors argue that “the lack of labeled data to determine if (query, chunk) pairs are related poses significant limitations for training retrieval models in RAG systems.” (lines 62-64). However, there is plenty of widely used high-quality data nowadays for training retrievers, e.g. MS Marco dataset [1], and also of various QA datasets, which makes unclear the motivation for developing a retriever which does not use any queries during training. This is also unclear to me how a retriever trained without any query data could work in practice; an additional analysis of query representations would be helpful to explain it. _[addressed in the authors response]_
3. The proposed method brings only small and inconsistent improvements over baselines. This can be seen from Table 1. Furthermore, some rows in this Table highlight “Ours” in bold while it is not the highest score, e.g. for Vicuna-7B + TriviaQA and SamSum, or LLaMA-2-13B-Chat-HF and SamSum. 
4. One missing simple baseline for a proposed method is to produce labeling for semantic similarity between two text chunks by simply prompting an LLM for this task. Furthermore, the paper does not cite nor compare to a very relevant body of work on using LLMs for reranking, e.g. [2] and [3].
5. The method is tested on five datasets: 2WikiMultihopQA, Musique, TREC, TriviaQA, and SAMSum. The paper does not provide any motivation for this selection _[motivation provided in the authors response]_. At the same time, in Information retrieval there are well established benchmarks for testing retrievers in domain shift settings, e.g. BEIR [4], which should be used for corresponding evaluations.  
6. Experimental settings are given with very little detail, e.g. I was not able to find which metric is reported in the main Table 1, or what is the architecture of the proposed model (or what pretrained model it was initialised from). _[these two details were provided in the authors response]_. Other missing details include evaluation dataset sizes, how retrieval datastores were constructed, how many passages were retrieved per query, or which decoding strategy was used.

[1] Tri Nguyen et al. MS Marco: A Human Generated MAchine Reading COmprehension Dataset. NeurIPS 2016.

[2] Weiwei Sun et al. Is ChatGPT Good at Search? Investigating Large Language Models as Re-Ranking Agents. EMNLP 2023
 
[3] Zhen Qin et al. Large Language Models are Effective Text Rankers with Pairwise Ranking Prompting. NAACL 2024.

[4] Nandan Thakur et al. BEIR: A Heterogeneous Benchmark for Zero-shot Evaluation of Information Retrieval Models. NeurIPS Datasets and  Benchmarks track, 2021.


Examples of unclear parts of text (not an exhaustive list of all unclear parts).

Introduction:

Line 44: “these methods are generally difficult to achieve context length extrapolation.” -> an unclear phrase “methods are difficult to achieve”, and an unclear sentence why KV cache compression methods are poor in context length extrapolation.

Line 50: “Another lightweight solution for handling long contexts is to utilize long-context Retrieval-Augmented Generation (RAG) for long-context chunking”. -> long-context RAG is used _together_ with long-context chunking, not for it.

Lines 52-55: “Long context Retrieval-Augmented Generation refers to a method in natural language processing where a model retrieves relevant information from large external sources to assist in generating responses. It extends the traditional RAG by handling much longer input contexts.” -> The definition for  Long context RAG (sentence 1)  seems to be describing the general RAG setting. Sentence 2 is unclear: handling longer input contexts in the generator LLM or in the “ large external sources”?

Line 56: “ Typically, RAG employs existing LLMs with limited context windows to retrieve relevant chunks, either with or without semantic truncation. Retrieval models are commonly used for this purpose; however, they require a large amount of high-quality labeled data for training, which limits their scalability and adaptability. ” -> RAG does not employ LLMs to retrieve relevant chunks, this is done by the retriever. Term “semantic truncation” is not introduced nor explained. High-quality labeled data for training retrievers is available, e.g. the widely used MS Marco dataset [3].

Line 61: “Modern RAG systems rely on complex chunking methods (Sarthi et al., 2024)” -> this is an incorrect claim, most of modern RAG systems use the same simple strategy of chunking into the fixed number of tokens  or sentences, as is done in this submission. 

Lines 64-65: “Recent research combines RAG with long-context LLMs to handle extended contexts and mitigate semantic incoherence in chunk processing” ->  I did not understand what “semantic incoherence in chunk processing” means.

Line 71: “Additionally, the complexity of these methods makes them vulnerable to distribution shifts” -> I did not understand how these two concepts are connected.

Lines 77-78: “we introduce a novel uncertainty estimation technique based on the Signal-to-Noise Ratio (SNR), which stabilizes predictions and reduces biases from random chunk splitting.” -> I did not understand what “stabilizes predictions” means (and why they are “unstable” in the first place), and what are the “biases from random chunk splitting”.

Related Work:

Line 131: “However, considering that many LLMs are closed-source, fine-tuning these models specifically for a retrieval model is impractical” -> (1) I did not understand what  “fine-tuning these models specifically for a retrieval model” means. (2) there are a lot of open source LLMs available nowadays. 

Methodology:

Line 190: “In this section, we introduce a span uncertainty method based on SNR to obtain confidence scores between chunks” -> what does “confidence scores between chunks” mean?

Line 195: “This process typically does not involve using query data for training, so we further develop two methods to scale chunk data to enhance the model’s distribution shift generalization ability” -> I did not understand how the second part logically follows from the first one.

Line 244: “Additionally, we have observed a specific window in the model’s output log probabilities. The probability distribution within this window is stable, which we believe indicates better calibration” -> a “specific window” where? in the vocabulary dimension, or in the text dimension? what does it mean “the probability distribution is stable”? Why does it indicate better calibration?  

Lines 293-294: “We set up two windows within M, each containing m samples. Among them, the top m are positive samples, and the bottom m are negative samples.” ->  How exactly are these windows of m samples set up? Furthermore, is the “top m” computed over bm 25 scores or $\hat S_ij$ scores?

Caption of Figure 1 is also hard to understand.

Regarding describing the methodology (Section 3), I would suggest showing all the steps on a particular text example. _[presented in the authors response]_

### Questions
1. What is the intuition of the proposed SNR? What does it mean qualitatively when $SNR_j < \sigma$? E.g. does it mean that a window of text is predicted well by an LLM, or the opposite?

2. Formula (3): when a piece of text is input to the LLM, it outputs probabilities of tokens conditions on _all_ their preceding tokens, till $x_0$. However, formula (3) uses probabilities conditioned only on tokens within a specific window, till $x_{0j}$. How these probabilities are computed?

_[both questions answered in the authors response]_

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This work focuses on improving the dense retrieval model to facilitate retrieval-augmented generation (RAG).
This work introduces UncertaintyRAG, an innovative method that incorporates span uncertainty, grounded in Signal-to-Noise Ratio (SNR), to enhance the similarity estimation between text chunks.
The key strength of UncertaintyRAG is the robustness to generalize across different contexts.
This is achieved by the improved calibration mechanism in the measurement of span uncertainty. 
Experiments with distribution shifts further demonstrate the robustness and the better performance of UncertaintyRAG.

### Strengths
1. This work introduces a novel method to improve the dense retrieval model. This method uses SNR-based span uncertainty to estimate similarity between text chunks.
2. Experimental results across various inference models and RAG tasks demonstrate that UncertaintyRAG outperforms baseline methods.
3. Further analysis reveals the inner properties of the trained dense retrieval model.

### Weaknesses
1. For measuring the span uncertainty, this work only considered one model (i.e., Llama-2-7b-chat-hf). As the proposed method is theoretically model-free, there should be experiments to demonstrate that (1) UncertaintyRAG performs well with various models to measure the uncertainty, or (2) various models can achieve an agreement on the uncertainty measurement. The current approach lacks a thorough investigation into the model-agnostic nature of the uncertainty estimation, which is a critical claim of the paper. Specifically, it's unclear if the SNR-based uncertainty is consistent across different model architectures and sizes, or if the observed performance gains are specific to the chosen Llama-2-7b-chat-hf model. This raises concerns about the generalizability of the proposed method.

2. The evaluation tasks should include single-doc tasks such as NQ and Qasper. To still keep the distribution shifts, you can move these two tasks from training set to the evaluation set, and add the three few-shot learning tasks into the training data. The current evaluation is limited to multi-document tasks, which may not fully capture the nuances of the proposed uncertainty-based retrieval. Single-document tasks like NQ and Qasper would provide a more comprehensive evaluation by assessing the model's ability to handle simpler retrieval scenarios and its robustness to different types of information sources. The absence of these tasks limits the scope of the evaluation and raises questions about the method's performance in diverse retrieval settings.

3. There should be some comparisons with more baseline RAG methods, such as Self-RAG, FLARE, and RankRAG. The paper lacks a comparison with more advanced RAG methods, which makes it difficult to assess the true contribution of UncertaintyRAG. Comparing against methods like Self-RAG, FLARE, and RankRAG would provide a more comprehensive understanding of the proposed method's strengths and weaknesses relative to the current state-of-the-art. Without these comparisons, it's unclear whether the observed improvements are significant or simply due to the use of a more sophisticated retrieval model.

### Questions
I hope to see more experimental results to further demonstrate the effectiveness of UncertaintyRAG.
See the Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
