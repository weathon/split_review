# LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses

- Decision: Accept
- Avg Score: 6.33
- Scores: 5, 6, 8

## Abstract
A model is considered well-calibrated when its probability estimate aligns with the actual likelihood of the output being correct. Calibrating language models (LMs) is crucial, as it plays a vital role in detecting and mitigating hallucinations of LMs as well as building more trustworthy models. 
However, standard calibration techniques may not be suited for LM calibration. 
For instance, post-processing methods such as temperature scaling do not reorder the candidate generations. 
On the other hand, training-based methods require fine-tuning the entire model, which is impractical for LMs of large scale. 
We present \model, a lightweight calibration mechanism consisting of a single linear layer that takes the input text representation and predicts a bias term, which is then added to the LM output logits. 
\model improves model calibration by only adding $<2$\% of the original model parameters. 
For evaluation, we construct \suite, a benchmark consisting of eight text generation tasks, covering responses ranging from short phrases to paragraphs. 
We test \model with Llama2-7B, where it improves calibration across all tasks, reducing the average ECE score by as large as 30\%.
We further conduct a comprehensive evaluation with multiple popular open-sourced LMs from GPT and LLaMA families, yielding the following key findings: 
\textbf{(i)} Larger models within the same family exhibit better calibration on tasks with short generation tasks, but not necessarily for longer ones.
\textbf{(ii)} GPT-family models show superior calibration compared to LLaMA, Llama2, and Vicuna models, despite having much fewer parameters. 
\textbf{(iii)} Fine-tuning pretrained model (e.g., LLaMA) with samples of limited purpose (e.g., conversations) may lead to worse calibration, highlighting the importance of fine-tuning setups for calibrating LMs.}}
\cutabstractdown

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a new calibration technique for LLMs: LITCAB, a lightweight calibration mechanism that adjusts the generation confidence of large language models (LLMs) by adding and training a single linear layer over the last hidden states of the LLM. LITCAB aims to improve the alignment between the model confidence and the output correctness and reduce the issue of hallucination in LLMs. The authors construct CAT, a calibration evaluation benchmark consisting of six open-ended question answering (QA) tasks that cover answers ranging from phrases to paragraphs. The authors propose a four-step procedure to assess the calibration and correctness of paragraph-level generations, which involves extracting individual claims, mapping them to spans, estimating their confidence and verifying their accuracy using GPT-4 and Wikipedia passages. The authors conduct experiments on LITCAB and several baselines using Llama2-7B and other popular open-source LLMs. They find that LITCAB consistently improves the calibration performance across all tasks, and that larger models within the same family tend to exhibit better calibration. They also observe that fine-tuning may lead to worse calibration in some cases.

### Strengths
- Originality: The authors propose LITCAB, a lightweight calibration mechanism that only adds and trains a single linear layer on top of the LLMs12. The authors also construct CAT, a new benchmark for evaluating calibration across different answer lengths.
- Quality: The paper compares several baselines of calibration on datasets of different output length - phrase, sentence, and paragraph.
- Clarity: The paper is easy to follow and understand.
- Significance: The paper addresses the calibration problem for LLM and improves upon SOTA open-sourced LLMs on open-ended QA tasks.

### Weaknesses
 - It is not clear to me how to select the incorrect answers. This could be important as different selection strategies may affect the performance of the final model.
- It is not clear why adding a linear layer on the last hidden state is the best option. Other options include LoRA or prefix tunning, which also only requires a fraction of parameters to tune. More evaluation results should be presented to justify the model choice of LITCAB.
- The confidence of a sentence is the geometric mean of all its tokens. However, different tokens contribute differently to semantics. For instance, think about "The 2023 Oscar best actress is Michelle Yeoh" as the answer to "Who wins the 2023 Oscar best actress?". Only the last two tokens decide the correctness of the sentence. How did you handle the different importance of tokens?

### Questions
- How did you select/generate incorrect answers for the QA tasks?
- The confidence of a sentence is the geometric mean of all its tokens. However, different tokens contribute differently to semantics. For instance, think about "The 2023 Oscar best actress is Michelle Yeoh" as the answer to "Who wins the 2023 Oscar best actress?". Only the last two tokens decide the correctness of the sentence. How did you handle the different importance of tokens?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper comprises two main contributions focusing on language model calibration. Firstly, they propose Litcab, which is a lightweight LM calibration mechanism that accepts the sentence representation as input and predicts a bias term that will be added to the output logits. Secondly, they construct CaT, which is a benchmark consisting of six open-ended question-answering tasks covering text lengths of different granularity. The paper presents experiments showing that Litcub is an effective calibration mechanism, as well as a comprehensive evaluation of LLMs in terms of how well-calibrated they are using the CaT benchmark.

### Strengths
* A lightweight alternative to supervised model calibration is important given that our models are increasing in size.

* Calibration benchmarks for long-form responses have not yet been introduced before.

### Weaknesses
 * Presentation-wise, parts of the paper have coherence issues because it is convoluted with two different ideas that are not properly tied up together. The paper starts to be read as having Litcab as the major contribution and curating the CaT benchmark, a minor contribution, to evaluate Litcab. However, the final page (Section 6.6 and Table 3) is dedicated to using CaT to benchmark how well-calibrated the LLMs are. Litcab is not used in this section, which makes it somewhat irrelevant to answering the main hypothesis of the paper.

* The CaT benchmark has two major shortcomings. Firstly, the motivation for creating CaT is to be able to evaluate calibration for long-form responses. However, CaT consists of five datasets with short-form responses and only one with long-form responses. There are a couple of datasets that could have been included, such as ELI5, WebGPT, ASQA, and QAMPARI (which is not passage-level but contains multiple claims). Secondly, it is important for a proposed benchmark to have both proposed (a) baselines and (b) evaluation metrics. However, the proposed baselines could not be evaluated in all cases (specifically passage-level) using their metrics. This makes it difficult to assess the calibration capability of Litcab at the passage level.

* I think it would help the paper if there were extrinsic evaluations to support Litcab's usage in a real-world task setup. Self-consistency is now commonly used because the original paper showed promising results on arithmetic and commonsense reasoning benchmarks. How would the use of Litcab fare on those datasets?

* The paper mentions that Litcab has the "advantage of requiring a reduced number of data samples for training, leading to enhanced computational and data efficiency". There is no evidence shown in the paper that supports this statement.

### Questions
* How would the use of Litcab fare on arithmetic and commonsense reasoning benchmarks?

### Soundness
2 fair

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper present LITCAB, a lightweight calibration mechanism to calibrate the LLMs by only adding <2% of the original model parameters. This paper also introduces a new collection of datasets for assessing calibration of LLMs in phrase-, sentence-, and paragraph-level. Experimental results show that the proposed method outperforms a series of baselines by using four metrics. Other key findings include: (i) Larger models within the same family exhibit better calibration. (ii) GPT-family models show superior calibration compared to LLaMA, Llama-2 and Vicuna models despite having much fewer parameters. (iii) Fine-tuning pretrained model (e.g., LLaMA) with samples of focused purpose (e.g., conversations) may lead to worse calibration, highlighting the importance of fine-tuning setups.

### Strengths
1. The model calibration is highly meaningful, especially for nowadays LLMs, and the proposed method can be used for most of the open-source models.

2. The proposed method is simple yet effective, although it needs some training examples collected by ChatGPT and GPT-4.

3. The collected datasets CAT can also be useful for evaluating the methods for LLMs calibration.

### Weaknesses
1. The paper lacks discussion and comparison of some related works [1][2].

- [1] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model. arXiv 2023.

- [2] Eliciting Latent Predictions from Transformers with the Tuned Lens. arXiv 2023.

2. There are still some efficient fine-tuning methods (e.g. LoRA) that can leverage additional training data, but the paper lacks results compared with such methods.



### Questions
1. It appears that your method involves using GPT-4 to generate training data, which has also been widely used in recent research. Does this introduce potential unfairness in the comparison? If the training data cannot be generated using GPT-4 or if its quality is poor, would the method still be effective?

2. The proposed method seems to have minimal differences compared to the original LM, and the experimental results also indicate that the original LM performs not very badly. Therefore, what are the main advantages of the proposed method? How does it improve LLMs qualitatively or quantitatively?

3. Why do you use different thresholds (e.g., cov@50, cov@90, cov@60) for different datasets?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good
