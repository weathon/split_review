# DistillSpec: Improving Speculative Decoding via Knowledge Distillation

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Speculative decoding~(SD) accelerates large language model inference by employing a faster {\em draft} model for generating multiple tokens, which are then verified in parallel by the larger {\em target} model, resulting in the text generated according to the target model distribution. However, identifying a compact draft model that is well-aligned with the target model is challenging. To tackle this issue, we propose {\em DistillSpec}, a method that uses knowledge distillation to better align the draft model with the target model before applying SD. DistillSpec makes two key design choices, which we demonstrate via systematic study to be crucial to improving the draft and target alignment: utilizing \emph{on-policy} data generation from the draft model, and \emph{tailoring the divergence function} to the task and decoding strategy. Notably, DistillSpec yields $10-45\%$ speedups over standard SD on a range of benchmarks, using both greedy and non-greedy sampling. We show that the distilled model can be well transferred to various tasks with an average speedup of $26\%$. Furthermore, we combine DistillSpec with lossy SD to achieve fine-grained control over the latency vs. task performance trade-off. Finally, in practical scenarios with models of varying sizes, first using distillation to boost the performance of the target model and then applying DistillSpec to train a well-aligned draft model can reduce decoding latency by $6-10\times$ with minimal performance drop, compared to standard decoding without distillation. 
\vspace{-0.15cm}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes DistillSpec, which improves the efficiency of speculative decoding (SD) by aligning the distributions (at the token and sequence level) between the draft model and the target model in advance. The paper further provides valuable insights regarding the recipe of distillation data, distillation objective and sampling strategy.

Experiments show that DistillSpec speedup SD by 10-45% while preserving the model performance across four diverse datasets.

### Strengths
1. SD is an important direction in accelerating LM inference. The idea of leveraging distillation to speed up SD is novel and very effective.
2. Using acceptance rate as the efficiency measure is well-motivated. Using total variation distance (TVD) objective is simple and straightforward in maximizing this efficiency measure.
3. The authors provide a fast alternative of using student-generated data for training, with a theoretical justification and strong experimental results.

### Weaknesses
1. The technical novelty is a bit limited. It is a direct application of existing KD techniques in SD.
2. The performance of the method is task-dependent, posing concerns for using the method in practice. For example, the speedup on WMT En-De is marginal and TVD has varied performance on different tasks.
3. Major experiment results are based on small target models. The results on larger models are not very clear -- in Figure 6, which data points correspond to which sizes of target and draft models?
4. The method is target-model-dependent, meaning that we need to distill a new draft model for each new target model. Such a distillation cost can be quite expensive, especially when using online data generation.

### Questions
See weakness.

### Soundness
3 good

### Presentation
2 fair

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
This paper proposes DistillSpec, a method that uses knowledge distillation to improve the speed and quality of speculative decoding. The paper explores various factors that affect the alignment between the draft and target models, such as the training data, the divergence function, and the decoding strategy. It also extends DistillSpec to lossy speculative decoding, which allows for sampling away from the target model distribution. The paper evaluates DistillSpec on several tasks and datasets to demonstrate its speedups.

### Strengths
- It provides a comprehensive and systematic study of different aspects of knowledge distillation for speculative decoding, such as data generation, divergence functions, and lossy sampling. The conclusion of models generated data being important makes sense.
- It demonstrates the effectiveness of DistillSpec on several tasks and datasets, using both greedy and non-greedy sampling, and compares it with representative baselines.
- Its lossy speculative decoding results offer novel insights and recommendations for combining knowledge distillation and speculative decoding in different scenarios.

### Weaknesses
 - The presentation of the paper is a bit messy and unclear. For instance, it is difficult to find the formal definition of DistillSpec among the analysis of various existing distillation approaches; it is not clear how distillation data is generated in detail; the specific configurations of target and draft models in figure 6 are not given, especially for the size of the target model in the DistillSpec case. The clarity and structure of the paper should be improved.
- While DistillSpec is effective on certain tasks, the experiments mainly focus on T5 models and simple tasks (except for GSM8K), compared with the recent advances in LLMs. This also results in the lack of discussion on the difficulty of LLM distillation. Is DistillSpec also effective for LLMs like LLaMA-7B? Can distilling LLMs for some specific tasks also be helpful for other tasks in general? The effectiveness of DistillSpec should be evaluated using more recent large models and some zero-shot benchmarks to prove its effectiveness.
- The paper does not compare or discuss DistillSpec with other methods that combine large and small models at inference, especially under the lossy decoding cases [1].
- The paper does not analyze the generated texts by DistillSpec in greater detail, like the diversity and coherence, which are important aspects of text quality and largely influenced by the sampling approaches. It would be helpful to provide some examples of the generated tasks.

### Questions
I am wondering how will DistillSpec be compared with recent work that combines speculative decoding and distillation [1]. It would be interesting to have this discussion.

[1] Liu, X., Hu, L., Bailis, P.D., Stoica, I., Deng, Z., Cheung, A., & Zhang, H. (2023). Online Speculative Decoding. ArXiv, abs/2310.07177.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose DistillSpec that uses knowledge distillation to better align the draft model with the target model. The authors have a wide exploration of different dilation methods from SeqKD to on-plicy GKD. DistillSpec yields impressive 10 − 45% speedups over standard speculative decoding on a range of standard benchmarks.

### Strengths
1. The experiments are quite solid. It explores different distillation losses and different ways to collect data for distillation. All the tables and figures are well written, and it is easy to get the difference between different methods.
2. The authors also explore the trade-off between accuracy and latency.
3. The paper is well-written and easy to read.

### Weaknesses
1. All the distillation methods are based on existing works. The work is more of a comprehensive study of knowledge distillation on LLM for speculative decoding.
2. All the experiments are done in an in-domain setting, while the benefits of LLM are on zeroshot/fewshot setting on out-of-domain datasets. Thus the experiments can not show whether it can replace the general draft models.

### Questions
Why do different distillation methods vary a lot in Figure 4?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
