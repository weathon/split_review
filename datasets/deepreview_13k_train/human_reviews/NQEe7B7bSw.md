# Entropic Distribution Matching for Supervised Fine-tuning of LLMs: Less Overfitting and Better Diversity

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
Large language models rely on Supervised Fine-Tuning (SFT) to specialize in downstream tasks. Cross Entropy (CE) loss is the de facto choice in SFT, but it often leads to overfitting and limited output diversity due to its aggressive updates to the data distribution. This paper aim to address these issues by introducing the maximum entropy principle, which favors models with flatter distributions that still effectively capture the data. Specifically, we develop a new distribution matching method called GEM, which solves reverse Kullback-Leibler divergence minimization with an entropy regularizer. 

For the SFT of Llama-3-8B models, GEM outperforms CE in several aspects. First, when applied to the UltraFeedback dataset to develop general instruction-following abilities, GEM exhibits reduced overfitting, evidenced by lower perplexity and better performance on the IFEval benchmark. Furthermore, GEM enhances output diversity, leading to performance gains of up to 7 points on math reasoning and code generation tasks using best-of-n sampling, even without domain-specific data. Second, when fine-tuning with domain-specific datasets for math reasoning and code generation, GEM also shows less overfitting and improvements of up to 10 points compared with CE.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors address the overfitting and decrease in output diversity that arise when using the cross-entropy loss during supervised fine-tuning by introducing a novel distribution matching method called *Generative and Entropy-regularized Matching of distributions* (GEM). GEM is based on two core principles: (1) the model should assign higher probabilities to observed data without overtraining, and (2) as supervised datasets cannot encompass all possible data and thus only cover a limited distribution, the model should learn from both the supervised data and its own generated samples. The first principle is addressed by maximizing the entropy, while the second is achieved by minimizing the reverse KL divergence between the model and target distributions. The authors showed that GEM effectively improves the output diversity, mitigates overfitting, and outperforms the cross-entropy loss (with and without weight decay and entropy regularization) as well as NEFT on multiple benchmarks, including IFEval, HumanEval, GSM8K, MATH, and MBPP.

### Strengths
- SFT is a timely and impactful area of research as it is an essential phase of the LLM pipeline.
- The proposed GEM method is grounded in theory, effectively tackles overfitting, and improves the output diversity of Llama3-8B.
- The experimental setup is modern.
- The paper is clear and well-structured.

### Weaknesses
 - GEM is only evaluated on Llama3-8B, which might particularly benefit from GEM. 
- While Best-Of-N (BON) is useful to show the diversity of the output, it is not a practical solution and therefore does not represent the performance of the model.

### Questions
- In addition to Majority Voting (MV) and Best-Of-N (BON), can you report the performance using an LLM as a judge on the same 32 samples?
- Out of the 32 generated samples, how prevalent is the selected answer by MV? In other words, can you report the ratio of the selected answers when using majority voting?
- For the CE + entropy baseline [1], what coefficient γ did you use to weight the regularization? Did you conduct a grid search?
- Line 33: I suggest replacing "Despite extensive pre-trained, " with "Despite extensive pre-training, " or "Despite being extensively pre-trained, ".
- Line 423: Entropy regularization supports Principle 1.

[1] Abhimanyu Dubey, Otkrist Gupta, Ramesh Raskar, and Nikhil Naik. Maximum-entropy fine grained classification. Advances in neural information processing systems, 31, 2018.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The use of cross-entropy (CE) loss during the supervised fine-tuning stage often results in overfitting and a reduction in output diversity. To address this limitation, this work introduces a novel training method called GEM. GEM tackles the challenge of distribution matching through reverse KL divergence minimization and incorporates maximum entropy regularization to promote output diversity. The authors demonstrated the effectiveness of GEM across multiple scenarios, showcasing its ability to maintain high performance while reducing overfitting. Additionally, they highlighted that GEM offers benefits for test-time computation, where maintaining diversity is crucial.

### Strengths
1. The work is well-motivated, and the writing is clear.
2. They demonstrated increased diversity in the model's output through high performance on the test-time compute set.
3. They designed a method that is tractable for sequential data.

### Weaknesses
1. The goal seems to be heavily focused on enhancing the diversity of generations. I believe it would be beneficial to further evaluate how the proposed method performs on tasks where diversity is not as critical. For instance, it would be helpful to show how it performs on tasks where factual accuracy is important.

### Questions
1. This is not a critical question, but is there any method to demonstrate that the performance improvement in test-time computation truly results from the increased diversity in the model's output?
2. Is there any performance degradation when increasing the temperature at inference time?
3. Could you also show performance results using LLM-as-a-judge in the Creative Writing section? While diversity is an important dimension, I believe it is also necessary to evaluate other aspects such as the coherency of the writing.

### Soundness
3

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
3

### Summary
This paper introduces a new SFT loss, GEM, based on the ideas of reverse KL loss and entropy. This loss can mitigate the overfitting issues of cross-entropy loss in the SFT process. Across a variety of task datasets, GEM demonstrates improved diversity and higher accuracy.

### Strengths
1. This article is well-written, with clearly organized content and significant research value.
2. The proposed GEM loss is simple and effective; this straightforward loss improvement simultaneously enhances diversity and accuracy.
3. The experiments are thorough, with validation across various mainstream tasks for large models.

### Weaknesses
1. Compared to CE Loss, GEM may introduce additional hyperparameters, which could make training more challenging.
2. There is no comparison of training costs across different methods.

### Questions
1. I understand that the introduced GEM can make the model's output distribution more diverse; however, increased diversity usually results in lower accuracy on domain-specific datasets or a higher probability of hallucination errors. Why does GEM improve both generalization and accuracy simultaneously?

2. What is the function of h in Equation 2? Is h necessary? If not, what would happen if h were omitted? And if h is optional, why are only the two variants mentioned in the paper permissible?

3. What is the functional difference between reverse KL and normal KL?

### Soundness
3

### Presentation
4

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
The paper introduces a novel method for supervised fine-tuning of large language models (LLMs) called Generative and Entropy-regularized Matching (GEM). GEM replaces the traditional Cross Entropy (CE) loss with a reverse Kullback-Leibler (KL) divergence minimization enhanced with entropy regularization. The approach seeks to mitigate overfitting and increase diversity in model outputs. The authors demonstrate that GEM outperforms CE in instruction-following, math reasoning, code generation, and creative writing tasks, using Llama-3-8B as a model. The method also claims computational efficiency by optimizing a single model and reducing sampling steps while preserving output quality.

### Strengths
* The paper addresses known limitations of CE in supervised fine-tuning, such as overfitting and limited diversity, which are crucial challenges for deploying LLMs in diverse tasks.
* GEM's performance is evaluated across multiple tasks and datasets, showing consistent improvements over CE in both general-purpose and domain-specific fine-tuning.

### Weaknesses
 * While the authors attempt to adapt GEM for sequential data, the proposed solution (using a data distribution “reset” trick) might introduce limitations for real-time applications. This part could benefit from further empirical validation.
* The performance of GEM depends on parameters like the $\beta$ term in entropy regularization. The paper lacks a sensitivity analysis to show how robust GEM is to these hyperparameters
* Although GEM offers an alternative to Cross Entropy, the idea of using entropy regularization to promote diversity is not new, and reverse KL divergence has also been previously explored in generative modeling. The novelty in combining these may be seen as incremental, especially without substantial empirical differentiation from prior methods.

### Questions
* In scenarios with limited training data, does GEM perform consistently, or would CE still be preferable due to its simplicity?
* Would the regularization in GEM, especially the entropy component, introduce a non-trivial increase in compute or memory requirements, especially when scaling?
* The paper focuses on the Llama-3-8B model, but it is unclear if GEM’s performance gains generalize across various architectures or if they are specific to this model’s configuration.
* In cases where GEM aims to enhance diversity, could it inadvertently introduce biases in generation, particularly when generating responses with multiple valid answers?

### Soundness
3

### Presentation
3

### Contribution
2
