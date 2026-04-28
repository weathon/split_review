# Scaling Relationship on Learning Mathematical Reasoning with Large Language Models

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Mathematical reasoning is a challenging task for large language models (LLMs), while the scaling relationship of it with respect to LLM capacity is under-explored.
In this paper, we investigate how the pre-training loss, supervised data amount, and augmented data amount influence the reasoning performances of a supervised LLM.
We find that pre-training loss is a better indicator of the model's performance than the model's parameter count.
We apply supervised fine-tuning (SFT) with different amounts of supervised data and empirically find a log-linear relation between data amount and model performance, and we find better models improve less with enlarged supervised datasets.
To augment more data samples for improving model performances without any human effort, we propose to apply Rejection sampling Fine-Tuning (RFT).
RFT uses supervised models to generate and collect correct reasoning paths as augmented fine-tuning datasets.
We find with augmented samples containing more distinct reasoning paths, RFT improves mathematical reasoning performance more for LLMs.
We also find RFT brings more improvement for less performant LLMs.
Furthermore, we combine rejection samples from multiple models which push LLaMA-7B to an accuracy of 49.3\% on GSM8K which outperforms the supervised fine-tuning (SFT) accuracy of 35.9\% significantly.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper investigates the scaling relationship of factors influencing the mathematical reasoning abilities of large language models (LLMs) through supervised fine-tuning (SFT), in-context learning (ICL), and rejection sampling fine-tuning (RFT) techniques. The authors analyze pre-training losses, the amount of supervised data, and the amount of augmented data and find that pre-training loss has a linear correlation with SFT and ICL accuracy within a certain range. The paper demonstrates that SFT performance has a log-linear relationship with the amount of supervised data, while RFT performance benefits from the increase of distinct reasoning paths. Finally, by combining rejection sampling from multiple models, the authors achieve significant accuracy improvements in multiple LLaMA models.

### Strengths
1. The paper is clear, well-organized, and addresses a relevant and important research area.
2. An investigation of how pre-training losses, the amount of supervised data, and the amount of augmented data influencing LLM performance in mathematical reasoning tasks is provided.
3. The paper proposes a new method (RFT) that leverages rejection sampling to generate additional supervised data for improving model performance.

### Weaknesses
1. The paper only does evaluation on 1 dataset, limiting its generalizability to other multi-hop reasoning problems. Specifically, the GSM8K dataset, while a good benchmark for mathematical reasoning, is limited in its scope and complexity compared to other datasets that involve more diverse reasoning steps, such as those requiring symbolic manipulation or common-sense knowledge. This narrow evaluation makes it difficult to ascertain whether the observed scaling relationships and performance improvements would hold across a broader spectrum of mathematical reasoning tasks.
2. Although the approach is intuitively simple, the amount of computational overhead added makes this approach not appealing. The rejection sampling fine-tuning (RFT) method, while effective, introduces a significant computational cost due to the need to generate and evaluate multiple reasoning paths for each training example. This overhead could be a limiting factor for practical applications, especially when dealing with large models and datasets. The paper does not sufficiently quantify this overhead or compare it to alternative methods for data augmentation.
3. The relationship between downstream task performance and pretraining loss has been well-established since the introduction of BERT. So the results in this paper is not really novel. While the paper demonstrates a correlation between pre-training loss and downstream performance, this finding is not particularly novel, as it aligns with existing literature that has shown similar trends across various language models and tasks. The paper does not adequately address how its findings contribute to a deeper understanding of this relationship or provide new insights beyond what is already known.

### Questions
1. Do the authors think the findings of this paper could be generalized and extended to other domains beyond mathematical reasoning tasks? Do the authors expect similar scaling relationships and performance improvements to hold in other LLM applications? Would be nice to see this supported with additional experiments.
2. In the RFT experiments, did the authors observe any instances where the model performance deteriorated or the improvement was insignificant? If so, could you elaborate on such cases and provide possible explanations?
3. Can the authors show similar results with other models than just llama?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper analyzes the scaling relationship between the math reasoning performance of a supervised fine-tuned LM and pre-training loss, supervised data amount, and augmented data amount. The authors find the pre-training loss is negatively linearly related to the performance while the supervised data amount is log linearly related to the performance. The augmented data amount has a weaker effect than the supervised data amount. All these effects diminish when the LM size increases. The authors also propose a rejection sampling fine-tuning 
(RFT) technique, which uses LMs to augment multiple reasoning chains for one training example, to improve the math reasoning performance of an LM. All experiments are performed on the GSM8K dataset.

### Strengths
1. The experiments are solid and convincing. 
2. The paper is well-written and easy to follow.
3. The proposed RFT significantly improves the performance on GSM8K.

### Weaknesses
1. While the experiments are pretty convincing, the final conclusion does not seem to be very surprising or bring new insights. We already know the importance of model size, pre-training loss, and data amount. Since we are not going to design and pre-train a new LM at fine-tuning time, which requires predicting larger LM's performance from smaller ones, I'm not sure why a fine-tuning scaling law would be useful. It just suggests people use the strongest existing pre-training LM, which is exactly what people are doing right now. Maybe the authors can convince me of this during the rebuttal.
2. The proposed RFT feels disconnected from the scaling law experiments. i.e. It does not seem to need to be inspired by the discovered scaling law. RFT basically suggests augmenting the fine-tuning data with LM-generated reasoning paths and rejecting the ones ending with wrong answers. I don't think the idea of data augmentation needs to be inspired by scaling law.
3. Another concern about this paper is that all experiments are limited to one small dataset, GSM8K, which only has 7K+ training examples. Given the scale of the experiments, I can understand this experimental choice. However, I'm still wondering if all the conclusions (e.g. linear with pre-training loss, log-linear with supervised data size) still hold on other math world datasets.

### Questions
N/A

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
They present an analysis of how performance on the gsm8k dataset improves with models scale / finetuning data. They find that across many models the model's pretraining loss is highly correlated with its performance on gsm8k. They also find that as pretraining loss improves, the benefits from supervised finetuning (SFT) diminish, and models with lower pretraining loss require more finetuning data to surpass the model's in-context-learning performance. Next they study how rejection sampling finetuning (RFT) improves with model scale. The idea is to sample a bunch of outputs from the model and then finetune on the correct samples. They also filter correct outputs that have similar reasoning paths. They find that RFT generally outperforms SFT up to 13B parameters, and benefits less at 33B parameters. Increasing the number of samples for RFT generally improves performance, but less than increasing the size of the finetuning dataset. Lastly they study combining RFT datasets from multiple models, finding that it improves over RFT from a single model up to 13B parameters. Overall by combining RFT data from multiple models they are able to obtain 7B and 13B LMs that are competitive with models that have many more parameters.

### Strengths
* Their analysis of the scaling effects of SFT and RFT, in particular the finding that models with lower pretraining loss benefit less from finetuning, are indeed interesting and will contribute to improving our understanding of LM finetuning.
* The question of how LM reasoning improves with model scale is a highly relevant and important question.
* They run a fairly thorough set comparisons and ablations across different finetuning settings, LMs, data amounts. And they do a good job of characterizing how performance on gsm8k changes as each of these parameters are adjusted.

### Weaknesses
 * Their analysis of how pre-training loss correlates with gsm8k performance is pretty questionable because the loss numbers are for models trained on different datasets and thus are not comparable. While they admit this in the paper, it would be much better if they could make these numbers more comparable. One way to fix this would be to evaluate the loss of all the language models on some standard dataset.
* They only consider gsm8k in this work. It would improve my confidence in their results if they also included other tasks, such as MATH.
* Their RFT method is nearly a special case of STAR [cite], with the only difference being that they also filter reasoning paths for diversity. It therefore is unclear to me to what extent this could be claimed to be a new method.

### Questions
* Some of the experiments are shown for up to 70B and others only up to 13B. Would it be possible to present results for all models sizes for all of the different scaling figures?

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors study the effects of pretraining loss, supervised training data amount, and augmented data amount on reasoning performance of tuned large language models. They claim that pretraining loss is negatively linear correlated to the fintuned and in-context learning performance and serves as a more effective performance metric compared to the size of the pretrained model or the amount of pretraining tokens. 

A Log-linear trend is reported between training data size and model performance. 
The authors also propose to augment the training data using rejection sampling. Essentially, generating multiple answers for each query in the training data and augmenting the dataset using those pairs in which the final answer is correct according to the ground truth. Augmenting the data through rejection sampling from multiple model sizes further improves the reasoning performance of smaller models.

### Strengths
The authors did a great job analyzing multiple factors such as, pretraining loss, finetuning data amount and augmented data amount affecting the reasoning performance of the LLM. It shed some light on important factors contributing to making LLMs more proficient in math reasoning.

The introduction and study of filtering the rejection sampling dataset to encourage distinct reasoning path amounts in the augmented data, and its effects on the rejection sampling finetuning performance is an interesting idea.

### Weaknesses
 The pretraining loss reported are associated with various pretraining datasets and distinct tokenizers, making a direct comparison challenging. 

Given that the x-axis in Figure 1 represents the pretraining loss of models of varying sizes, the scaling relationship appears questionable. Wouldn’t it make more sense if the x-axis was the loss of the finetuned models? 

The primary concern I have with the study is that the authors do not study different pretraining losses of the same model (identical size and training tokens). Their assertion is that as the pretraining loss decreases, the tuned and ICL performance improve linearly within a certain range. However, it’s important to note that this improvement is not based on the models of the same size or same amount of pretrianing data.

### Questions
When combining the rejection sampling data from multiple model sizes do you filter out the generations which do not have a different equation set across model sizes?

What is the value of `k` in Table 3 for `maj1@k` for LLaMA family of models? It would be nice to include it somewhere either in the table or its description.

The claim “as the pretraining loss decreases, the SFT and ICL performance improve linearly within a certain range” appears somewhat unclear and could benefit from additional explanation.

Please refer to the question and concern in the weakness section as well.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
