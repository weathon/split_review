# OWL: A Large Language Model for IT Operations

- Decision: Accept
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
\noindent With the rapid development of IT operations, it has become increasingly crucial to efficiently manage and analyze large volumes of data for practical applications. The techniques of Natural Language Processing (NLP) have shown remarkable capabilities for various tasks, including named entity recognition, machine translation and dialogue systems. Recently, Large Language Models (LLMs) have achieved significant improvements across various NLP downstream tasks. However, there is a lack of specialized LLMs for IT operations. In this paper, we introduce the \model{}, a large language model trained on our collected \dataset{} dataset with a wide range of IT-related information,
where the mixture-of-adapter strategy is proposed to improve the parameter-efficient tuning across different domains or tasks.
Furthermore, 
we evaluate the performance of our \model{} on the \bench{} established by us and open IT-related benchmarks. \model{}  demonstrates superior performance results on IT tasks, which outperforms existing models by significant margins. Moreover, we hope that the findings of our work will provide more insights to revolutionize the techniques of IT operations with specialized LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, an LLM for IT operations is trained and evaluated. Data-wise, the authors built an instruction dataset Owl-instruct and an evaluation dataset Owl-Bench. Modeling-wise, the authors proposed HMCE to overcome the limit of input length and mixture-of-adapter to improve parameter-efficient tuning across different tasks. The trained model showed better performances than existing LLMs, including ChatGPT, in IT operation-related tasks.

### Strengths
1. The main strength of this paper is it describes most of the details about how it builds its datasets and trains the LLM, which can be very helpful to researchers in their domain-specific LLM research.
2. The authors compared their LLM with existing SOTAs and achieved better performances in all tasks.
3. The authors tried to build a balanced evaluation dataset that covers various topics of IT operations with a similar number of questions.

### Weaknesses
Techniques used in this paper are mainly slight variations of existing approaches. So innovation of technique is incremental in this paper.

### Questions
In the evaluation of the Q&A test, is it trustworthy to use GPT-4 scoring as the ground truth? I'm not quite convinced by this. Can you elaborate on the rationale for this? Ideally, human evaluation would be the best choice. Is it possible to add human ratings for this task?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper presents OWL model and OWL-Instruct dataset aimed at IT operations where the seed dataset is crafted by subject matter (IT) experts across 9 prevalent operations and maintenance domains. Inspired by NBCE, the authors propose HMCE to extend the context length. In the supervised fine-tuning of the model they suggest a Mixture-of-Adapter method to improve the instruction-tuning performance. The dataset is rooted in some manually labeled data from domain experts which are enriched in a Self-Instruct fashion with supplementary samples. The Owl-Bench benchmark is another contribution of this work derived from real-world questions.

### Strengths
The paper comes with multiple orthogonal contributions each of which could be significant in their own sense contingent on proper evaluation. 

The MoA adapter strategy is a significant contribution introducing task-specific adaption with a mixture of experts.

Expansion of token set by domain-specific tokens, while not novel, enhances the value of the proposed work.

The HMCE, inspired by NBCE, is yet another novel (to the extent of reviewer's knowledge) context extension approach.

### Weaknesses
Regardless of the above strenghts, the paper is proposing a diverse set of ideas and tries to evaluate them within the context of the paper. However, given the orthogonality of the ideas and the relatively high number of them, the authors haven't been able to thoroughly assess each idea, particuarly the theoretical ones (e.g. HMCE, MoA) independent of the empirical setting of OWL and IT operations.

The HMCE contributions does not go well with the rest of the story. Based on the Evalutions in section 5.3, HMCE was evaluated with an independent set of tests where the concatenated question to create long input squences. While the results show that HMCE outperforms NBCE as a training-free context extension approach, it does not seem to have anything to do with the OWL model and its dataset.

From the understanding of the reviewer, in Figure 3, the baseline models have not been benefitng from MoA adapting (or LoRA). If that is the case, the comparison is not entirely fair.

Typos:
Probably a typo: "...where a group of LoRA adapters is lightweight compared to the pre-trained model."
Typo page 8: "We have propose HMCE..." --> proposed
Typo page 8: "Without NMCE" --> HMCE

### Questions
In Appendix A, when embedding matrix is appended with new rows to expand D to D' and include the newly trained IT-operations token, do you retrain any of the LLaMa layers? Please elaborate on how the heads encoding the embedding space were retrained to incorporate the new tokens.

The results in Figure 3, has OWL leveraged MoA? If so, have the other baseline models benefitted from the same MoA training so that the comparison remains fair?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper focuses on the application of LLM in IT operation. The author uses GPT-4 to create a diverse set of instructions (the OWL-Instruct) based on seed samples for building an LLM for IT operations domain. The OWL-Instruct is used to fine-tune LLaMA2 to create a LLM (the OWL) for the IT domain. To test LLM's capabilities, the author has created a testing benchmark (the Owl-Bench) for the operation and maintenance. In the experiments, the author compares the performance of some existing LLMs and OWL in domain-specific questions and downstream tasks.

### Strengths
1.	The paper focuses on the application of LLM in the IT operations domain and provides a complete process for building and training large models in the IT domain that can be reproduced.
2.	A diverse IT operations test benchmark has been proposed.
3.	Experiments show that the OWL model improves compared to existing methods on downstream tasks.

### Weaknesses
1. The novelty of this work is limited. The model proposed in the paper used some existing techniques and only some skills are proposed.
2. In the QA experiment, the evaluation method for model performance is not rigorous enough. GPT-4 is used both for creating instructions and assessing model performance, which may lead to unfair comparisons.
3. The content distribution in the main text and appendices may need further optimization. For example, related work should usually not be placed in the appendix. Additionally, this paper primarily focuses on the development of large models but lacks coverage of tasks in the IT operations field, such as the development and challenges of log detection.

### Questions
1. Since OWL uses instructions from GPT-4, is there a possibility of bias in evaluating the model's performance, leading GPT-4 to favor giving high scores to OWL? Have the authors compared the relevance of GPT-4's results with human evaluations in the current task?
2. Can OWL improve or solve specific challenges that traditional models can't handle in downstream tasks?
3. In downstream tasks, OWL shows a smaller performance advantage compared to LogPrompt based on the open-domain ChatGPT. As a domain-specific model, can OWL be proven to have better output consistency and robustness than open-domain models like ChatGPT or GPT-4?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors construct a new IT-related dataset to tune LLM and achieve good performance on IT related tasks.

### Strengths
The authors apply different techniques Owl-instruct, HMCE and mixture of adapters to finetune the LLM and achieve SOTA performance on IT related tasks.

### Weaknesses
1. The novelty is limited. The paper seems to have multiple pieces and the authors combine them to create the paper. I feel that the main contribution is a new IT-related dataset.
2. The authors propose HMCE. But I think it's kind of illy described. After reading, I am not sure what advantages the HMCE offer. From my current understanding, it seems that the authors want to break the long inputs into pieces and still want to have a good likelihood estimator. Considering so many long context modeling techniques proposed recently, I am not sure why the author only mentioned the unpublished work NBCE.
3. On evaluation, are there any duplications from the dataset the authors construct and the authors used to eval? If so, the evaluation results are not convincing. This should be stated clearly.

### Questions
See the weakness section

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
