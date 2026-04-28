# MM-R$^3$: On (In-)Consistency of Multi-modal Large Language Models (MLLMs)

- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 6, 6, 6

## Abstract
With the advent of Large Language Models (LLMs) and Multimodal (Visio-lingual) LLMs, a flurry of research has emerged, analyzing the performance of such models across a diverse array of tasks. While most studies focus on evaluating the capabilities of state-of-the-art (SoTA) MLLM models through task accuracy (e.g., Visual Question Answering, grounding) across various datasets, our work explores the related but complementary aspect of consistency -- the ability of an MLLM model to produce semantically similar or identical responses to semantically similar queries. We note that consistency is a fundamental prerequisite (necessary but not sufficient condition) for robustness and trust in MLLMs. Humans, in particular, are known to be highly consistent (even if not always accurate) in their responses, and consistency is inherently expected from AI systems. Armed with this perspective, we propose the MM-R$^3$ benchmark, which analyses the performance in terms of consistency and accuracy in SoTA MLLMs with three tasks: Question Rephrasing, Image Restyling, and Context Reasoning. Our analysis reveals that consistency does not always align with accuracy, indicating that models with higher accuracy are not necessarily more consistent, and vice versa. Furthermore, we propose a simple yet effective mitigation strategy in the form of an adapter module trained to minimize inconsistency across prompts. With our proposed strategy, we are able to achieve absolute improvements of 5.7% and 12.5%, on average on widely used MLLMs such as BLIP-2 and LLaVa 1.5M in terms of consistency over their 
existing counterparts.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents MM-R3 as a dataset to study the effect of language and image shifts in MLLMs. The language shifts in MM-R3 are designed such that they diversify the input to the LLM stream but retain the original semantics. The images are affected by style shifts and the effects on the MLLM’s are tested with over 13.3K Testing examples. MM-R3 evaluates the accuracy of the replies and also the consistency of the MLLM outputs

### Strengths
The paper explores an interesting research direction

### Weaknesses
In a benchmark with over 87,000 examples, visually inspecting only 100 random question-rephrasing pairs and 100 images (about 0.002% of the data) is a poor quality metric. Even if 92% language rephrasing and 86% image are semantically equivalent in this extremely small sample, the statistics for the entire dataset could differ strongly.
My main concerns about the MM-R3 benchmark are the lack of novelty and the impracticality of the proposed benchmark.
There is extensive literature analyzing (Empirically and theoretically) the effects of subtle shifts of the Network outputs with respect to the shift on the inputs. Among many others, [A][B][C][E] analyze the robustness of CNNs and Transformers to alterations in their visual input. Other works have already provided the theoretical analysis of the trade off between  accuracy and robustness [D]. Regarding the language modifications the sensitivity towards changes in the input has also been extensively studied [F][G][H]. The joint model is not an exception and theoretical analysis is already available[I]. This paper confirms already known behavior where even small changes in the input can produce alterations on the output, and that training on the shifted data can help reduce the variability of the output. Beyond that, I can not find any other novel insights or results in this paper. Therefore I consider MM-R3 and its results as yet another empirical evaluation inside this line of work.
Regarding the practicality of the MM-R3 benchmark, the Image-restyling tasks seem to be a far fetched task. The authors focus on strong style shifts on their images that are only possible with direct human intervention. I can not imagine any real-world condition or task where a captured image is so distorted  that it resembles the visual patterns in the Candy Mosaic and Udnie styles. Only the gray-scale looks like a reasonable artifact to find in images, but is only a small component of this benchmark. Why do we need to assess that  MLLMs are robust to such exotic visual perturbations?
Following a similar idea, could the authors elaborate on what real-world task or established benchmark requires the MLLM to correctly guess an occluded object?. In addition, If an MLLM guesses correctly, does it make it more accurate/suitable for a given task?, would a user even benefit from having improved results on this task?.
MLLMs can already perform context reasoning  based on spatial locations, direct object relationships, and even image sequences. In comparison the proposed context reasoning represents an Ill posed task where many plausible objects could be hidden behind the occluding shapes. Since context relationships are already a strong component in many current benchmarks[J][K], could the authors elaborate why we need to evaluate Context Reasoning using an Ill posed task.
Regarding the proposed module, Table 6 does not represent a direct and fair evaluation between the baseline (Ori.) and the proposed method (Adapt.). The Adapt. row has been trained for the specific tasks contained in MM-R3, meanwhile the models in Ori have never been trained for them. In other words, The Ori. models are operating in a zero-shot manner, while the Adapt. models are fine-tuned and specialized for the target task. This is a clear disadvantage for the Ori. models which explains the performance gap.
A fair comparison would retrain the original model without using the proposed adapter module and compare if there is any improvement between the finetuned and finetuned+adapter module. For a complete assessment, different architectures for the module could be tested, this will validate that the proposed architecture is optimal for the fine-tuning in MM-R3. FInally the performance in standard benchmarks should be tested once again to assure the capabilities of the model in other tasks and datasets have not been altered.
Without a complete and fair comparison, the adapter module can not be presented as a contribution.
I cannot be certain about the quality of the benchmark, two of the proposed taks look impractical and don't seem to be targeting any useful application case of MLLMs, and the empirical validation is flawed. Therefore I’m recommending rejection.

### Questions
Why do the authors choose different source datasets?. The dataset diversity is clearly welcomed, but I wonder why the authors refrain from performing image re-styling over MSCOCO or over the image data of InfographicsVQA. Likewise MSCOCO contains caption data that can be rephrased.
In line 246, when the authors state “the ground truth annotation is encompassed within the MLLM’s response”. What exactly is being tested? This reads as if the authors test for the GT to be a substring of the answer of the MLLM. Could the authors confirm the exact evaluation procedure? How is the text output tested and labeled as Correct or Erroneous?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a benchmark to evaluate the accuracy and consistency (with emphasis on consistency) for MLLMs. The benchmark contains the tasks of question rephrasing, image restyling and context reasoning. The benchmark has been utilized to evaluate and compare the SOTA open- and closed-sourced MLLMs, and the results revealed the limitations of most of these models in the consistency and the relationship between the consistency and accuracy. The paper also proposes an adapter to be deployed between the encoder and decoder of a MLLM to improve the consistency. The evaluation results demonstrate the improvements for two of the models, but the resulting consistency is still low.

### Strengths
1. The work is well-motivated. The existing benchmarks have focused on model accuracy, but consistency has been overlooked. 
  
2. The paper is well organized and written. In general, the benchmark design, the evaluate methodology, and the result analysis have been elaborated clearly. 

3. The proposed adapter has been demonstrated helpful in improving the consistency (mainly) and accuracy of two of the MLLMs.

### Weaknesses
1. While 6 open-sourced MLLMs were analyzed for consistency and accuracy, only two of them (BLIP-2 and LLaVa 1.5M) were used in experiment to evaluate the proposed adapter. It is not clear on its effectiveness on other models. Also, the improved consistency, especially for image restyling, is still low compared to other models.

2. Figures 2, 3, and the embedded figures are too small to view clearly.

### Questions
The evaluation results show the consistency due to stochasticity of the models. How does the stochasticily affect the measured inconsistency based on rephrasing, restyling and context reasoning tasks? How does the proposed adapter address the consistency caused by the stochasticity?

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
4

### Summary
The paper studies the consistency of MLLMs using 3 tasks: (a) when the question is rephrased with the same meaning; (b) when the image is re-styled; (c) when the image is partially occluded. The contributions include a new dataset, intensive analysis of representative models, and an adapter-based method to improve the consistency (and accuracy). The dataset is constructed using images/questions from existing datasets with modifications generated using LLMs or image generation models. The analysis, including both open MLLMs and private ones like Gemini and GPT-4, reveals that consistency does not necessarily correlate with accuracy. The method shows that the adapter can improve the consistency (with slight improvement in accuracy as well) for LLaVA-1.5 and BLIP-2.

### Strengths
1. The problem is clearly defined. The dataset and the method are intuitive.
2. The experiments are intensive, covering a variety of models. The comprehensive analysis revealing that consistency not correlating with accuracy is also interesting.
3. Writing is clear and easy to follow, providing clear details for the experiments.

### Weaknesses
1. While the results are intensive, it is a bit overwhelming to look at each of the three tasks and four metrics one by one. Is there a metric that can be a good proxy of all the results, or can the average be a good representative?
2. It is great that the adapter shows clear improvements on the proposed dataset, but it also worths checking the results on standard datasets like VQAv2. After adding the adapter, does the performance on standard datasets drop?
3. This paper is not the first one to study “consistency” in VQA/MLLMs. More discussion and comparisons with existing works should be provided.

### Questions
See weakness.

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the often-overlooked aspect of **consistency** in Multi-modal Large Language Models (MLLMs). While most existing evaluations focus on accuracy across various tasks, this work introduces the **MM-R³ benchmark** to assess the consistency of MLLMs when presented with semantically similar inputs. The benchmark consists of three tasks:

1. **Question Rephrasing**: Evaluating consistency in responses to different phrasings of the same question.
2. **Image Restyling**: Assessing consistency when images are presented in different styles.
3. **Context Reasoning**: Testing the model's ability to infer masked or occluded content in images.

The authors analyze several state-of-the-art MLLMs, both open-source and proprietary, and find that consistency does not always align with accuracy. They observe significant variability in consistency across models. To address this, they propose a simple **adapter module** that can be integrated into existing MLLMs to enhance consistency. Experiments demonstrate that this approach leads to notable improvements in consistency metrics without significantly altering accuracy.

### Strengths
- **Novel Benchmark**: The MM-R³ benchmark is a valuable contribution, focusing on consistency—an important but underexplored aspect of MLLM evaluation.

- **Comprehensive Analysis**: The paper provides a thorough evaluation of multiple state-of-the-art MLLMs across different tasks, offering insights into their consistency and accuracy.

- **Clear Motivation**: The paper clearly articulates the importance of consistency in AI systems for robustness and trustworthiness.

- **Well-Structured and Clear Presentation**: The paper is well-organized, making it easy to follow the methodology, experiments, and findings.

### Weaknesses
 - **Lack of Analysis**: The paper does not delve into how different pretraining strategies or model architectures contribute to the observed inconsistencies. An analysis from the pretraining perspective or model architecture could provide deeper insights into why certain models perform better in terms of consistency. Specifically, the paper lacks an investigation into the impact of different pretraining objectives (e.g., masked language modeling, contrastive learning) on the consistency of the resulting MLLMs. Furthermore, the analysis should explore how architectural choices, such as the depth and width of the vision and language encoders, affect a model's susceptibility to inconsistencies.

- **Adapter Evaluation**: There should be analysis about the overhead brought by the adapter and models' general performance influenced by the adapter. The paper does not provide a detailed analysis of the computational overhead introduced by the adapter module, such as the increase in parameters, memory consumption, and inference time. Additionally, the evaluation lacks a thorough investigation into how the adapter affects the model's performance on a diverse set of downstream tasks beyond the consistency benchmark. It is crucial to assess whether the adapter improves consistency at the expense of accuracy on other tasks.

- **Lack of Error Analysis**: The paper could benefit from a deeper analysis of failure cases to understand why models are inconsistent and how the adapter mitigates these issues. The paper does not provide a detailed analysis of specific failure modes that lead to inconsistencies. A more granular error analysis, categorizing the types of inconsistencies (e.g., semantic, numerical, contextual) and identifying the input characteristics that trigger them, would be beneficial. Furthermore, the paper should investigate how the adapter addresses these specific failure modes, providing insights into its mechanism of action.

- **Lack of Novelty**: The adapter module lack novelty compared to existing methods in the field. The paper does not sufficiently compare or contrast its approach with prior work on improving consistency, which could make the contribution seem incremental. The paper should discuss how the proposed adapter differs from existing methods for improving model consistency, such as adversarial training, data augmentation, or ensemble methods. A more thorough comparison with these approaches is needed to establish the novelty and significance of the proposed method.

### Questions
1. **Adapter Overhead**: What is overhead brought by the adapter? 

2. **Impact on Downstream Tasks**: Does the adapter module impact the models' performance on other downstream tasks?

3. **Error Analysis**: Can you provide more insights into the types of inconsistencies observed in the models and how the adapter addresses them? For example, are there specific patterns or error types that the adapter helps mitigate?

4. **Pretraining Analysis**: Could you provide an analysis of how different pretraining strategies or model architectures impact consistency? Are certain architectures more prone to inconsistency, and if so, why?

### Soundness
3

### Presentation
3

### Contribution
3
