# GoLLIE: Annotation Guidelines improve Zero-Shot Information-Extraction

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 6, 5, 8

## Abstract
Large Language Models (LLMs) combined with instruction tuning have made significant progress when generalizing to unseen tasks. However, they have been less successful in Information Extraction (IE), lagging behind task-specific models. Typically, IE tasks are characterized by complex annotation guidelines that describe the task and give examples to humans. 
Previous attempts to leverage such information have failed, even with the largest models, as they are not able to follow the guidelines out of the box. 
In this paper, we propose GoLLIE (\textbf{G}uideline-f\textbf{o}llowing \textbf{L}arge \textbf{L}anguage Model for \textbf{IE}), a model able to improve zero-shot results on unseen IE tasks by virtue of being fine-tuned to comply with annotation guidelines.
Comprehensive evaluation empirically demonstrates that GoLLIE is able to generalize to and follow unseen guidelines, outperforming previous attempts at zero-shot information extraction. The ablation study shows that detailed %representative annotation candidates to the 
guidelines are key for good results. %\footnote{Upon publication.} to facilitate reproducibility of results and further research on this topic.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on zero-shot information extraction. Their goal is to train a large model that can generalize well to unseen domains and datasets. They main idea is using code as the intermediate layer for all the information extraction tasks and considering annotation guidelines or additional information during pre-training or testing. This additional information makes the model to understand tasks better and therefore be able to generalize. Experiments demonstrate the potential of the proposed method.

### Strengths
- The performance is impressive.
- The pre-trained model is valuable.

### Weaknesses
 - My main concern is as follows. Although the authors try to split the datasets for training and testing based on domains. I believe that there is still a large overlap among their output spaces. For example, RAMS, which is considered as one of the training tasks, contains role label *transporter*, *vehicle*, and *place*, while WikiEvents, which is consider as one of the testing tasks, also contains those role labels. In NER tasks, I believe the same situation happens as well. This makes the setting not *truly* zero-shot because the model has already learned those concepts. The model can get improvements just because including more *in-domain* supervised training signals. Specifically, the overlap in entity types and relation roles across datasets like RAMS and WikiEvents undermines the claim of zero-shot generalization. The model's performance could be inflated by its exposure to similar labels during training, making it difficult to ascertain its true ability to generalize to completely unseen concepts. A more rigorous evaluation would involve datasets with entirely disjoint label spaces.
- I think the authors should be careful when referring the state-of-the-art models. In fact, in Table 2, the reported SOTA numbers and models are not SOTA anymore.

### Questions
- See above.

### Soundness
4 excellent

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
This paper proposes an LLM fintuned to comply with annotation guidelines for information extraction tasks. Specifically, with a focus on NER, EE, and EAE (19 datasets in total), the task format is unified into a code style: the label class definitions as class docstrings and the candidates as a comment for the arguments.  Some regularization techniques are proposed to ensure that the model follows the guidelines and does not just learn to identify specific datasets. Experiments show that a finetuned version of Code-LLaMA achieves comparable performance compared with a naive baseline finetuned without guidelines, and beats the baseline in zero-shot settings by a large margin.

### Strengths
1. This paper proposes to utilize the annotation guidelines to boost the performance of zero-shot information extraction. The idea is intuitive and compelling.
2. The experimental results properly demonstrate the effectiveness of the proposed method and the bonus of the annotation guidelines.
3. The presentation of this paper is clear, with few typos.

### Weaknesses
1. The motivation behind the code style and its effects are unclear. Note that incorporating the annotation guidelines in a natural language style rather than the code style is also feasible. The LLMs pretrained on codes may lack natural language understanding capabilities that are crucial to conducting IE tasks. This may result in the low performance of the baseline. The advantages may lie in the capability of generating outputs following code grammar, which mitigates the need for parsing outputs. The authors should justify the necessity of the code style and its underlying effects compared to the natural language style.
2. The ablation studies of class order shuffling and guideline paraphrasing are missing.

### Questions
1. How many samples are used to supervise finetuning LLaMA?
2. The guidelines used in this paper are specifically the basic definitions of entity/relation/event types, which should have been provided to LLMs. However, the full annotation guidelines usually cover many edge cases and may contain tens of pages. Have the authors considered incorporating more fine-grained guidelines?

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces GoLLIE (Guideline-following Large Language Model for IE), a model fine-tuned to effectively utilize annotation guidelines for enhanced zero-shot results in Information Extraction tasks. A primary distinction of GoLLIE is its use of a Python code-based representation for both input and output. This method provides a clear, human-readable format, unifying the representation of various IE tasks and addressing challenges associated with traditional natural language instructions. Empirical evaluations validate GoLLIE's superior capabilities in leveraging guidelines, indicating promising directions for future research and model enhancements, including the exploration of more extensive pre-training datasets and refining its response to ambiguous labels.

### Strengths
1. The paper presents a novel solution to the long-standing challenge where large models struggled to leverage intricate annotation guidelines inherently. Through targeted fine-tuning and a unified Python code-based representation for both input and output, it significantly improves zero-shot outcomes in IE tasks.

2. The detailed error analysis provides invaluable insights into the challenges of zero-shot IE, especially when leveraging guidelines. The study methodically identifies specific issues like the ambiguity of labels, conflicts between fine-grained and coarse entities, and the repercussions of strong label preconceptions. These findings offer a valuable roadmap for subsequent research in the domain, emphasizing the need for clearer guidelines, broader fine-tuning datasets, and more specific instruction-following capabilities.

3. The paper is well-written and easy to follow.

### Weaknesses
1. The paper's novelty appears somewhat limited as similar approaches have been explored in past research. [1] proposes a zero-shot entity typing approach that utilizes the type description available from Wikipedia to build a distributed semantic representation of the types.

2. The choice of code-based prompting can potentially hinder usability for general users. Those unfamiliar with coding might find it challenging to interact with or fully leverage the model, thereby narrowing its applicability.

3. The method's efficacy remains unclear due to incomplete experimental validation.

   a. **Prompt Style Impact**: The rationale for using a Python code style prompt is not experimentally validated. It's untested whether natural language prompts with guidelines might yield similar outcomes. Although CodeIE validated code style prompts for OpenAI models, the necessity of this design for open-source LLMs during instruction tuning remains unproven.

   b.**Prompt Sensitivity**: The paper omits experiments examining the sensitivity of prompts, leading to concerns about the method's stability. The model's performance under varying definitions, code structures, and code comment styles remains unexplored, making its robustness questionable.

4. The paper lacks experiments analyzing the impact of training dataset diversity on the LLM's ability to follow unseen guidelines. It remains unclear how much data is required to achieve satisfactory performance, leaving questions about the scalability and efficiency of the approach.

### Questions
1. **Sampling Strategy**: Datasets differ in scale, and a naive mixture could introduce imbalance. How did the authors handle the sampling process for the datasets used in this study? Were experiments conducted to assess the effects of different sampling techniques on the results? This aspect wasn't addressed in the paper and could provide clarity on the method's robustness across varied data distributions.
2. **Scalability with Numerous Labels**: For datasets with a large number of labels, say in the order of hundreds, the input length for your method could become substantially lengthy, leading to efficiency concerns. In such complex scenarios with multiple labels, how does the inclusion of guidelines impact the performance? This wasn't touched upon in the paper but would provide deeper insights into the method's scalability and effectiveness in real-world applications.
3. **QLoRA vs. Full Model Fine-tuning**: The authors mentioned employing QLoRA for training, citing its superior performance over fine-tuning the entire model on zero-shot tasks and faster training speed. However, the paper lacks empirical evidence to support this. What are the relative impacts of full-parameter SFT and techniques like LoRA and QLoRA on zero-shot IE performance?
4. **Benchmark Selection**: Many of the state-of-the-art methods used for comparison in the paper, such as UIE, appear outdated. Why weren't more recent and potentially stronger methods like USM, InstructUIE, and GPT4 considered for benchmarking?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes GoLLIE, a large language model fine-tuned to follow label descriptions and few-shot examples to improve zero-shot information extraction. Key ideas include formulating tasks as Python code, regularizing training, and comprehensive evaluation on diverse IE tasks.

### Strengths
* LLMs have excelled at numerous complex tasks, but underperformed in IE tasks. This paper addresses this gap, diving deep into the annotation guidelines and error analysis using an LLM approach: zero-shot learning, natural language instructions, programming language output format, and leveraging one model to tackle multiple tasks.
* The study's thorough experiments span various IE tasks, coupled with an extensive error analysis when applying the unified model across these diverse tasks. Such detailed error analysis offers valuable insights into the model's strengths and limitations.
* Another significant contribution is crafting prompts for intricate IE tasks. Demonstrating the model's ability to adhere to these instructions, especially given the recognized challenges of current LLMs in following complex instructions, signifies substantial effort and expertise from the IE domain.

### Weaknesses
 * The claim of making use of “annotation guideline” may be an overstatement - this paper only considered label name, label description and few-shot examples, however, annotation guideline in IE domain are very complicated and was curated by linguists. E.g., For TACRED slot filling (https://tac.nist.gov/2015/KBP/ColdStart/guidelines/TAC_KBP_2015_Slot_Descriptions_V1.0.pdf), section 3.6 per:city_of_birth, they use “GPEs below the city level (e.g. 5 boroughs of New York City) are not valid fillers.“ as an example rule to guide annotators. The prompts proposed by this paper might not fully capture the depth of true guideline understanding.
* The paper omits key references from the era before LLMs that discuss label descriptions and verbalization. Examples include:
    * Zero-Shot Relation Extraction via Reading Comprehension
    * An Empirical Study on Multiple Information Sources for Zero-Shot Fine-Grained Entity Typing
    * Label Verbalization and Entailment for Effective Zero- and Few-Shot Relation Extraction

Small formatting issues:
* Use ``’’ instead of ‘’’’.
* Table 6 could be more user-friendly. Presenting exact numbers (like 10/10,000) would be clearer than percentages.

### Questions
* How does the prompt length vary in the proposed method? Translating IE tasks into Python classes might make them more accessible for LLMs, but could also significantly inflate the token count. For instance, a fine-grained entity type classification task with over 1000 entity types would result in a considerable token overhead.
* The paper doesn't detail the human (or domain expert) effort required to craft the prompts. Given the variety of labels and tasks covered in the study, it would be beneficial to track this for subsequent research.

These are important questions that need to be answered in the updated paper.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
