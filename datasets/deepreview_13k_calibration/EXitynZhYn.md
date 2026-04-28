# Open-ended VQA benchmarking of Vision-Language models by exploiting Classification datasets and their semantic hierarchy

- Decision: Accept
- Avg Score: 7.00
- Scores: 5, 8, 8

## Abstract
The evaluation of text-generative vision-language models is a challenging yet crucial endeavor. 
By addressing the limitations of existing Visual Question Answering (VQA) benchmarks and proposing innovative evaluation methodologies, our research seeks to advance our understanding of these models' capabilities. 
We propose a novel VQA benchmark based on well-known visual classification datasets which allows a granular evaluation of text-generative vision-language models and their comparison with discriminative vision-language models. 
To improve the assessment of coarse answers on fine-grained classification tasks, we suggest using the semantic hierarchy of the label space to ask automatically generated follow-up questions about the ground-truth category. 
Finally, we compare traditional NLP and LLM-based metrics for the problem of evaluating model predictions given ground-truth answers. We perform a human evaluation study upon which we base our decision on the final metric. 
We apply our benchmark to a suite of vision-language models and show a detailed comparison of their abilities on object, action, and attribute classification. 
Our contributions aim to lay the foundation for more precise and meaningful assessments, facilitating targeted progress in the exciting field of vision-language modeling.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a dataset to granularly evaluate the text-generative vision-language models. The authors base the evaluation benchmark on classification datasets where the labels semantic hierarchy are present. The semantic hierarchy is used as the source of generating the follow-up questions.

### Strengths
(1) propose a new topic for evaluating VQA models that assess how well the VQA models can classify or recognize fine-grained objects, activity, and attributes

(2) A intuitive solution to constructing a benchmark that contains the class semantic hierarchy based on classification model.

(3) comprehensive evaluation on lots of open sourced VQA systems.

### Weaknesses
(1) I believe assessing how granular a VQA system is in good and necessary, however, when evaluating, the current benchmark put additional constrains on the image space, cropping the image to certain objects and using imagenet which is object centric. These constrains largely limited the scope of VQA that is supposed to work on natural use case, for example, natural image QA (VQA v2, vizwiz, etc).

(2) The Cropping activity operations seems very risky the action needs a few frames to evaluate? Like sit down and stand up?

### Questions
Please comment on the weakness part.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
Evaluating text-generative vision-language models remains an intricate undertaking due to the inherent limitations of current Visual Question Answering (VQA) benchmarks. Motivated by the need for a more comprehensive assessment mechanism, this paper aims to address the ambiguity and specificity issues rampant in open-ended VQA (oVQA) tasks. These challenges emerge, in part, from the diverse ways natural language can express similar ideas and the constraints of current evaluation metrics that often favor shorter responses. To navigate these obstacles, this research introduces a novel VQA benchmark, enriched with subbenchmarks focusing on objects, actions, and attributes. It leverages a follow-up procedure, drawing from existing classification benchmarks, to generate contextually apt questions and expects models to provide answers with the requisite level of detail. Additionally, the study explores various metrics from the VQA and NLP spheres to find an optimal evaluation criterion, validated via human judgment. This holistic approach paves the way for an intricate analysis of leading vision-language models, unearthing their specific strengths and vulnerabilities.

### Strengths
1. Innovative Evaluation Methodologies: The research addresses the inadequacies of existing Visual Question Answering (VQA) benchmarks by proposing a new VQA benchmark. This benchmark, derived from well-established visual classification datasets, facilitates a more detailed evaluation of text-generative vision-language models and their comparative performance against discriminative vision-language models.

2. Addressing Coarse Answer Challenges: Recognizing the challenges in evaluating coarse answers in fine-grained tasks, the research introduces a method using the semantic hierarchy of labels. By doing so, it can automatically generate pertinent follow-up questions about the true category, pushing for more accurate and detailed model responses.

3. Enhanced Ambiguity Management: To better handle the inherent ambiguities in open-ended visual questions, a unique follow-up procedure is proposed. By adapting classification benchmarks for oVQA, the model is first provided with an apt visual context, and then, based on its initial response, a further clarifying question is posed using concept hierarchies. This ensures answers with the desired detail and precision.

4. Comprehensive Metric Evaluation: The research undertakes a rigorous examination of various metrics from both the VQA and NLP domains, emphasizing those that treat paraphrasing and synonyms as valid answers. The eventual metric is grounded in a human evaluation study, ensuring that it aligns closely with human judgments and provides a reliable measure for assessing model performances.

### Weaknesses
The paper omits certain statistical details regarding the oVQA dataset, such as the distribution of question/answer lengths, the number of entity class labels, and the formats/types of the questions. Given the dataset's general and expansive nature, there is a concern that, despite the introduction of subbenchmarks, it might introduce new challenges that could affect the quality of evaluations, such as issues related to imbalance.

### Questions
Please also refer to the previous section.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The work proposes a more principled evaluation of vision-language models by taking advantage of the semantic hierarchy of textual labels. The core problem the work addresses is that the exact match scoring systems used by VQA benchmarks can be ambiguous, and penalize models for essentially correct answers. To fix this, the authors crop images so to the object of interest, allow coarse answers, and ask follow up questions to clarify the fine-grained answer. Finally, they also measure performance with multiple metrics, such as BertScore and GPT-4 based evaluation.

### Strengths
While a substantial body of work exists on designing better benchmarks for VQA, the idea of using the semantic hierarchy to ask follow up questions is original. VQA is hard to evaluate, yet is the most fundamental task in vision-language (other than perhaps, image-text matching). One of the biggest problems in VQA is that questions can be underspecified or ambiguous and there can be multiple correct answers to questions. 

The method presented here is a neat way to deal with these ambiguities and inconsistencies in the evaluation process. 

Another useful contribution of the paper is the empirical evaluation of vision-language models on different aspects of vision-language, such as attribute recognition and coarse vs fine-grained recognition. This is useful. 

Finally, Table 7 is also very useful, especially because it helps resolve questions about the appropriateness of different metrics for open-ended VQA scoring.

### Weaknesses
There are no substantial weaknesses.

A figure showing the differences between a VQA question + label and examples from the proposed datasets would be useful. Fig. 2 would be easier to read if it said "attribute", "object" etc instead of OVAD, COCO.

### Questions
I have no questions.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent
