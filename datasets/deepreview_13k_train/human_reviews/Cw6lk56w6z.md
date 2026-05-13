# When does In-context Learning Fall Short and Why? A Study on Specification-Heavy Tasks

- Decision: Reject
- Scores: 3, 5, 5, 5

## Abstract
In-context learning (ICL) has become the default method for using large language models (LLMs), making the exploration of its limitations and understanding the underlying causes crucial. In this paper, we find that ICL falls short of handling \textit{specification-heavy} tasks, which are tasks with complicated and extensive task specifications, requiring several hours for ordinary humans to master, such as traditional information extraction tasks. The performance of ICL on these tasks mostly cannot reach half of the state-of-the-art results. To explore the reasons behind this failure, we conduct comprehensive experiments on $18$ specification-heavy tasks with various LLMs and identify three primary reasons: inability to specifically understand context, misalignment in task schema comprehension with humans, and inadequate long-text understanding ability. Furthermore, we demonstrate that through fine-tuning, LLMs can achieve decent performance on these tasks, indicating that the failure of ICL is not an inherent flaw of LLMs, but rather a drawback of existing alignment methods that renders LLMs incapable of handling complicated specification-heavy tasks via ICL. To substantiate this, we perform dedicated instruction tuning on LLMs for these tasks and observe a notable improvement. We hope the analyses in this paper could facilitate advancements in alignment methods enabling LLMs to meet more sophisticated human demands.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper discusses the limitations of in-context learning (ICL) in dealing with tasks that have complex and detailed specifications. 
It particularly highlights the challenges ICL faces in information extraction tasks like Named Entity Recognition (NER) and Relation Extraction (RE), which it categorizes as specification-heavy. 
The authors attribute ICL's shortcomings in these areas to three primary factors:

1. A lack of precise comprehension of the context.
2. Misinterpretation of the task schema.
3. Ineffectiveness in processing and understanding long texts.

### Strengths
The paper illustrates that instruction-following language models struggle to effectively utilize demonstration examples provided in their instructions, particularly when dealing with tasks that have heavy specification requirements.

### Weaknesses
I have a few major concerns:

1. Clarification of the definition of in-context learning.

In-context learning (ICL) is typically associated with a few-shot learning scenario that doesn't include explicit task instructions [1,2,3]. However, the ICL prompts discussed in the paper are characterized by a combination of 'Instruction + Demonstrations', diverging from the conventional ICL format, which usually involves only 'Demonstrations'.

2. Performance of `instruction + demonstrations`

The effectiveness of prompts that include both 'instruction and demonstrations' might be enhanced if large language models (LLMs) are specifically trained with such prompts. This training approach could potentially improve their performance on these tasks.

3. Labels covered in demonstrations are important.

It's crucial to show how demonstrations incorporate all labels in the label space. 
Typically, k-shot learning implies presenting k examples for each label. 
If the demonstrations are limited due to the constraints of input context length, this could understandably lead to lower performance.

### Questions
Same as weakness section.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper studies using the in-context-learning (ICL) paradigm with LLMs for solving specifications-heavy tasks, i.e., tasks that need to be described with a lengthy set of instructions such as relation extraction. Using 18 benchmarks (6 different task types) and six LLMs (FLAN-UL2, Alpaca, Vicuna, ChatGPT, Davinci003 and GPT-4), the paper demonstrates that few-shot ICL significantly lags behind the SOTA of each task. Manual analysis highlights three reasons for that poor performance: 1) inability of the ICL+LLM approach to understand specifics of the context, 2) lack of task schema comprehension, and 3) limited LLM ability to understand long context. The paper then confirms that the poor performance is due to the ICL approach itself rather than the capabilities of the LLM by fine-tuning FLAN-UL2 specifically for each task and showing accuracies that outperform SOTA. The paper argues that the current LLM alignment datasets do not well cover complicated specification-heavy tasks. Via supervised fine-tuning, the paper aligns FLAN-UL2 using the corresponding training  data of each task (leaving one task out for evaluation) and shows gains in accuracy compared to that obtained before alignment.

### Strengths
1. The paper highlights an interesting challenge to the in-context-learning paradigm that even today's most powerful LLMs struggle with. 

2. The paper presents promising initial results that demonstrates the potential of addressing the challenge of specification-heavy tasks via more focused alignment.

### Weaknesses
1. The success of the ICL approach highly depends on the amount and quality of information provided in the prompts. The results in table 1 are all based on a shortened version of the task description. Examples in the appendix show that such shortened descriptions are too concise, e.g., they do not even contain a single sentence definition of each label. The provided few-shots do not cover all labels. Longer prompts can still fit in at least a subset of the LLMs used for the experiments. The paper needs to experiment with more detailed prompts to confirm that the poor accuracy of the ICL approach is not due to the very concise set of instructions.
	 
2. The alignment experiments in Section 4.2 only hold out one task at a time, but still tasks of the same type are included in the alignment dataset. The paper needs to report results with a whole task type (e.g., All 4 RE tasks) is held out to confirm that the gain in accuracy is not really due to similarity between tasks.

### Questions
1. Comparing table 1 to table 4, Aligned ICL has worse accuracy than the unaligned  baseline on 3 tasks MAVEN-Subevent and the two sentiment analysis tasks. Do you have an explanation or an intuition for why that is the case for those three datasets?
	
2. In Section 3.1, the paper says that "LLMs ignore all the contexts in 18 instances". How did you find out about that?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Noticing that the performance of ICL on specification-heavy tasks, specifically traditional IE tasks (such as named entity extraction and relation extraction, 18 tasks in total) mostly cannot reach half of the state-of-the-art results, this paper conducts preliminary error analysis and identifies three primary reasons that ICL falls short of handling these tasks. Moreover, this paper demonstrates that through fine-tuning and instruction tuning, LLMs can achieve decent performance on these tasks. This indicates that LLMs can perform specification-heavy tasks well if they are well aligned with human expectations.

### Strengths
1. This paper focuses on an important research question that ICL falls short of handling specification-heavy tasks and presents an explorative analysis. This paper will be of interest to practitioners who aim to prompt LLMs to complete complicated tasks via ICL. 
2. The experiments on instruction tuning provide valuable findings, which properly demonstrate that well-aligned LLMs can perform unseen specification-heavy tasks better via ICL. 
3. The presentation of this paper is clear, with few typos.

### Weaknesses
1. Though the motivation of this paper is impressive, the analysis underwhelms in some aspects.  Firstly, in Figure 2, how do the authors attribute the errors made by LLMs to the three types of reasons? Is there a chain-of-thoughts or any monologues to help identify the reasons? It seems to me that the example presented in "unspecific context understanding" can also be attributed to “Misaligned Schema Understanding”.  One possible explanation is that the model noticed the “tackor“ but didn’t treat it as “product-car“, because the task instruction missed important information about the class “product-car“. Secondly, some important experimental details are missing. What are the prompts of Figure 3 for different models? What is the "specification" in a prompt and how does its length vary? Besides, does the performance drop come from the longer context or the content of the specification?
2. What is the scope of “specification-heavy tasks”? This paper primarily focuses on traditional IE tasks (16 out of 18 tasks). However, there is no clear boundary of “specification-heavy" tasks in this paper.  In my opinion, most of NLP tasks involve “complex” annotation guidelines if we would like to elaborate detailed task descriptions and edge cases. Could the authors provide a clear definition of "specification-heavy task" or at least some examples of opposite tasks? It's also possible to narrow the scope of your paper to IE tasks, without losing generality.
3. The instructions for different tasks are too simple. At least the definition of different entity/relation types should be provided.

### Questions
1. After the instruction tuning, the zero-shot performance gain of different tasks varies greatly. Could the authors provide some analysis or intuition on it?
2. It would be intriguing to see to what degree the instruction tuning on specification-heavy tasks addresses three identified challenges.  
3. This paper [1] is highly relevant to your second reason (misalignment in task schema comprehension with humans). 
4. Typo - Figure 6 (remove %)

[1] Guideline Learning for In-context Information Extraction. EMNLP 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper conducts a comprehensive evaluation of in-context learning and points out the inability of large language models in solving specification-heavy tasks. 

To further trace the root of this issue, the authors also explore the performances of instruction-tuned models and fine-tune models with related data. Evaluation results indicate limitations are primarily due to the alignment data used for model training, rather than the large language models per se.

### Strengths
1. Engaging topic and comprehensive evaluation.

2. Meaningful discussions and exploration of fine-tuning.

3. The paper is very well-written and easy to follow, making it a pleasure to read.

### Weaknesses
1. One major weakness is the selection of datasets. Most of these focus on information extraction (IE), and as pointed out in previous work [1], IE tasks are not generally considered in most instruction-tuning datasets. Therefore, IE tasks are not only specification-heavy but also unfamiliar to these instruction-tuned models. A simple investigation/baseline should involve manually curating specification-heavy but familiar instructions such as:

The output length should not exceed X length, the output should start with…, the output should be in a JSON format, among other considerations.

These specifications are likely to arise in user cases or training data and are also specification-heavy. This provides a further disentanglement of the root of this inability. Also, ,ore interesting discussions may occur in this direction. For example, can general specifications assist complex task-specific specification understanding? And vice versa?

[1] Zhang et al, Aligning Instruction Tasks Unlocks Large Language Models as Zero-Shot Relation Extractors. Findings of ACL 2023.


2. Minor: Deeper analysis and insights are expected to see. Sec. 3.1 3.2 & 3.3 mainly explain the superfacial observations and these parts take large portion of the papers, I would prefer to see more analysis earlier in the paper.

### Questions
No

### Soundness
2 fair

### Presentation
4 excellent

### Contribution
2 fair
