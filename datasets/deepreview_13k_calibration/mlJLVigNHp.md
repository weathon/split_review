# RECOMP: Improving Retrieval-Augmented LMs with Context Compression and Selective Augmentation

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Retrieval-augmented language models improve language models (LMs) by retrieving documents and prepending them in-context.
However, these documents, often spanning hundreds of words, make inference substantially less efficient. We propose compressing the retrieved documents into textual summaries prior to in-context integration. This not only reduces the computational costs but also relieve the burden of LMs to identify relevant information in long retrieved documents. We present two compressors -- an extractive compressor which selects useful sentences from retrieved documents  and an abstractive compressor which generates summary by synthesizing information from multiple documents. Both are trained to achieve performance gain in LMs when we prepend the generated summary from the compressor to LMs' input, while minimizing the summary length. When retrieved documents are irrelevant to the input or offer no additional information to LM, our compressors output an empty string, enabling selective augmentation. We evaluate our approach on the language modeling task and open domain question answering task. We achieve a compression rate of as low as 6% with minimal loss in performance for both tasks, significantly outperforming the off-the-shelf summarization models. We show that our compressors trained for one LM can transfer to other LMs on the language modeling task and provide a summary largely faithful to the retrieved documents.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors proposed a method named RECOMP (Retrieve, Compress, Prepend) to compress the retrieved documents used in Retrieval-Augmented language models (RALMs). The proposed method aims to generate concise, effective and faithful summaries to improve the efficiency of RALMs. Two kinds of summarizers are used: an extractive summarization model for selecting informative sentences, and an abstractive summarization model for generating good query-focused summaries. Experiments are conducted on language modeling and question answering tasks, achieving low compression rates and some performance drops.

### Strengths
- The presentation of the core idea is clear. The research topic of effective RAG is important.
- The proposed method freezes the LMs and only trains the summarization model, which is interesting and beneficial to transfer across different LMs.
- The analysis in Sec. 6 is sufficient and comprehensive.

### Weaknesses
My major concern is that the paper does not report the inference speedup by their method. Although experimental results show that fewer retrieved tokens are used, the number of tokens does not necessarily reflect the actual efficiency of the system, especially when the context length is not the bottleneck. The tokens of all the retrieved documents are still required to be processed by the compressor (a smaller model though). Therefore, it may be beneficial for authors to report the inference speedup of their method. This could be the core to support their motivations.

My other concern is the training cost associated with the abstractive compressor. The reliance on a teacher LM like GPT-3.5 for generating training data introduces a significant overhead. The paper lacks a detailed analysis of the trade-off between this training cost and the potential inference efficiency gains. It's unclear whether the reduced inference cost justifies the substantial upfront expense of training the abstractive summarization model.

### Questions
- Q1: As stated in "Weakness", the inference speedup should be reported.
- Q2: How about the training cost? The training of the abstractive compressor uses a teacher LM (GPT-3.5), which is expensive. I'm not sure if the cost saved in the inference stage is worth the cost in the training stage.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes RECOMP, an approach to improve retrieval-augmented language models (RALMs) by compressing retrieved documents into summaries before using them as context. The method uses two compression methods: an extractive model selecting relevant sentences, and an abstractive model generating summaries. The compressors are trained to optimize end-task performance when prepending the summary to the input. RECOMP is evaluated on language modeling and open-domain QA tasks.

### Strengths
The paper proposes a simple but clever idea and backs it up with a set of well-designed experiments. The baselines are well chosen.

### Weaknesses
Although the method is good, I’m not sure how useful it is in practice. Normal retrieval augmentation without any compression outperformed the compression methods albeit with many more tokens. However, with the growing context lengths of models, it is not clear if the accuracy hit is worth the tokens saved. Secondly, you still have to provide the full tokens to the abstractive model. The practical advantage of the method is further diminished when considering the computational overhead of training and running the compressor models. The extractive model, while faster, still requires processing the full retrieved document to select sentences. The abstractive model, while potentially providing more concise summaries, adds a significant computational burden, as it needs to process the full retrieved documents through a large model before the compressed representation is available. This overhead could negate the benefits of reduced context length in many real-world applications.

### Questions
Can you give some results on how the method is compared to traditional RAG with no compression in terms of time? 
Can you provide more details on the input tokens for the abstractive model or is the same number of tokens as the noncompression baselines?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors propose RECOMP (Retrieve, Compress, Prepend) that incorporates extractive and abstractive summarization into the retrieve augmented language model to shorten the token length of retrieved text in prompts. Precisely, these summarization modules receive input text and its retrieved text and then extract or generate the summary for the retrieved text. The authors did not simply join the summarization modules into the language model as separate modules. Instead, they updated them through training to generate summaries relevant to the input text and its retrieved text. The experimental results show that RECOMP can shorten the prompt length while keeping performance in language modeling and open-domain QA tasks.

### Strengths
- The authors show the effectiveness of both extractive and abstractive summarization. It means we can use insights from commonly used summarization methods for improving retrieve augmented language models.
- Since the summarization models are updated to fulfill the requirement of retrieving augmented language models, the proposed method is more than model combination and thus novel.
- The experimental result shows the proposed method RECOMP can save the prompt length while keeping its performance.

### Weaknesses
 - The benefit of shortening prompt length is uncertain. If the authors observe a speedup in inference,  they should report it.
- The performance improvement is limited or nothing in many settings. The authors need to justify it.

### Questions
- In the current evaluation, the benefit of using summarization for the retrieve augmented language model needs to be clarified. If the inference speed is improved, the authors should report it.
- Also, you need to report how much computational cost is decreased by RECOMP. This is related to the first question.
- Considering the length limitation of the model, we can expect summarization to make the model consider more retrieved texts in its prompt. It may contribute to improving language modeling performance. Did you check such direction in your work?

I will update my score based on the discussion with the authors.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
To enhance the efficiency and performance of retrieval-augmented language models, this paper introduces a simple and intuitive method for in-context improvement. Given the retrieved documents and input text, the proposed method first compresses the retrieved documents into a summary. Then, this summary is prepended to the input text, with the subsequent output response generated using a frozen language model. Two types of compressors are proposed: an extractive compressor, corresponding to extractive summarization, and an abstractive compressor, associated with abstractive summarization. Experimental results from both language modeling and question answering tasks demonstrate that the proposed compressors bolster the performance of retrieval-augmented language models.

### Strengths
The paper is well-written and straightforward. Moreover, it offers an extensive, and well-designed experimental validation of the proposed method and presents thorough analyses.

### Weaknesses
Some concerns regarding this paper include:

- The proposed method utilizes the knowledge of the LMs to train the compressor, while the baselines do not. Some baseline models, such as DRP and contriver, should be finetuned using the dataset employed to train the extractive compressor.

- The paper employs a BM25 retriever, making the results of the proposed method and baselines reliant on the retriever's performance. Therefore, it would be appropriate for the paper to also show performances using an another retriever, such as contriver (not merely as a sentence selector). In addition, presenting the distribution of oracle-retrieved documents, similar to what's done in extractive compression, would be advantageous.

- Relatedly, it is necessary to compare the time taken to generate text by prepending all retrieved documents without compression against the time taken using the proposed method—specifically, compressing the retrieved documents before prepending them.

### Questions
Q1: During the manual evaluation, the authors assess the outputs of the abstractive compressors. What was the level of annotation agreement among the evaluators?

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
3 good
