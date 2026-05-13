# Unveiling the Pitfalls of Knowledge Editing for Large Language Models

- Decision: Accept
- Scores: 8, 8, 6, 6

## Abstract
As the cost associated with fine-tuning Large Language Models (LLMs) continues to rise, recent research efforts have pivoted towards developing methodologies to edit implicit knowledge embedded within LLMs. Yet, there's still a dark cloud lingering overhead -- will knowledge editing trigger butterfly effect? since it is still unclear whether knowledge editing might introduce side effects that pose potential risks or not. This paper pioneers the investigation into the potential pitfalls associated with knowledge editing for LLMs. To achieve this, we introduce new benchmark datasets and propose innovative evaluation metrics. Our results underline two pivotal concerns: (1) \textbf{Knowledge Conflict}: Editing groups of facts that logically clash can magnify the inherent inconsistencies in LLMs—a facet neglected by previous methods. (2) \textbf{Knowledge Distortion}: Altering parameters with the aim of editing factual knowledge can irrevocably warp the innate knowledge structure of LLMs.
}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper comprehensively explores the side effects of knowledge editing for large language models (LLMs), highlighting potential risks in real-world use cases. To facilitate a rigorous evaluation, the researchers introduce two innovative datasets specifically crafted to highlight the unintended consequences of knowledge editing. The study offers solutions for knowledge conflicts and introduces the MLE method to mitigate distortion risks. It also discusses implementation challenges and prospects of knowledge editing for LLMs.

### Strengths
The authors assess the risks associated with current knowledge editing methodologies for LLMs, and introduce two datasets for the purposes of finding potential drawbacks of LLMs.

This paper presents the MLE method as a straightforward solution to mitigate knowledge distortion risks and address potential knowledge conflicts.

The challenges and prospects of implementing knowledge editing for LLMs are discussed.

### Weaknesses
The paper's scope is limited to factual knowledge editing. 

However, the presence or absence of knowledge conflicts or distortions in other types of knowledge editing remains unexplored.

The authors should supplement this part of the paper to make it more comprehensive.

### Questions
please refer to the weakness section.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper explores the potential pitfalls of knowledge editing for Large Language Models (LLMs). It introduces new benchmark datasets and evaluation metrics to investigate the issues of knowledge conflict and knowledge distortion. The results demonstrate that knowledge editing can lead to unintended consequences and inconsistencies in LLMs. The paper also presents potential solutions and challenges for knowledge editing in LLMs.

### Strengths
1. The information provides insights into different knowledge editing methods and their performance in various setups.
2. The paper discusses the concept of knowledge distortion and its impact on language models.
3. The paper introduces the idea of conflict detection technologies to address potential knowledge discrepancies.

### Weaknesses
1. The information provided is quite technical and may be difficult for non-experts to understand.
2. Some sentences are poorly structured and difficult to comprehend.

### Questions
1. What do you think is the fundamental reason for knowledge distortion during knowledge editing for LLMs? How to handle cases of one-to-many knowledge editing?
2. How do the knowledge editing methods compare to each other in terms of their effectiveness and efficiency, what is the takeaway in method selection?
3. In Multi-label Edit, how to guarantee the overall conceptual hierarchy among labels?

Minor Issues:
1. "Emperically" should be "Empirically."
2. "ROME is effective in both GPT-XL and GPT-J" should be "ROME is effective in both GPT2-XL and GPT-J."
3. "This motivates us to employ conflict detection technologies" should be "This motivates the employment of conflict detection technologies."
4. "Knowledge Conflict has reflected" should be "Knowledge Conflict reflects."
5. "However, it is undesirable for a robust editing method to weaken the preference" should be "However, weakening the preference is undesirable for a robust editing method."

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work pioneers the investigation into the potential pitfalls associated with knowledge editing for LLMs, and introduces new
benchmark datasets to evaluate LLMs after knowledge finetuning with proposed innovative evaluation metrics.

### Strengths
1. Novel benchmarks and evaluation metrics are developed in the paper
2. With empirical analysis, the authors develop a simple method, a.k.a Multi-Label Edit, to alleviate Knowledge Distortion in LLMs

### Weaknesses
1. The novelty of the developed method is quite low and the real contribution of this paper is the development of new benchmarks equipped with evaluation metrics.

### Questions
Thanks for your efforts in investigating two pivotal concerns in LLMs, specifically Knowledge Conflict and Knowledge Distortion, which has been widely discussed in NLP community nowadays. However, there remains some issues that I need to discuss with you.


1. Fig. 2 illustrates that after the process of Round-Edit, LLMs tend to assign higher probabilities to the knowledge facts stored in recent corpus and gradually forget the knowledge stored in model parameters. Nonetheless, I believe that the demonstration of Knowledge Distortion in Fig. 2 is not a unique issue limited to LLMs, but rather a prevalent concern across all current Deep Learning models. 
And I believe that the solution to this issue is to develop more reasonable retrieval-based LLMs, which answers questions based on the knowledge context, rather than finetune-based Knowledge Editing methods mentioned in this article. With retrieval-based LLMs, you just need to modify the knowledge facts stored in the context, then LLMs can directly answer the user question according to the context. In such consideration, I suppose the contribution of this paper is limited, and it will be better to include evaluation of retrieval-based LLMs as baselines.

2. The novelty of devlelopment of Multi-Label Edit is quite low, why not consider memory-based methods or EMA methods to alleviate the forgetting of previous knowledge stored in LLMs when you are certain that these knowledge fact are all accurate.

3. For Knowledge Conflict, it will also be a problem in retrieval-based LLMs, any thoughts to solve this problem according to your expiermental results?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the potential pitfalls related to LLMs knowledge editing, including Knowledge Conflict and Knowledge Distortion.
To achieve this target, two benchmark datasets and several innovative evaluation metrics are also introduced.
With these settings, this paper conducts experiments from two aspects among four common editing approaches on two LLMs, and proposes a Multi-Label Edit (MLE) solution.

### Strengths
1. This paper puts forward a valuable research problem, i.e., to discuss the potential risk of editing knowledge encoded in LLM. I believe this could help researchers and practitioners better understand and manipulate the knowledge encoded in LLM, so as to obtain a better model.
2. Extensive baselines are employed for analyzing the proposed research question.
3. Several new measures are designed to quantify the degree of knowledge conflicts in experiments.

### Weaknesses
My major concerns lie in the following three aspects:
1. The “Knowledge Conflict” proposed in this paper is confusing to me.
2. The experimental settings of “Knowledge Distortion” are vague and incomplete.
3. The proposed MLE solution is unclear.

### Questions
My questions mainly comes from the above three concerns.
1. The knowledge conflict mentioned in your paper, i.e., “e1: Marie’s husband is Pierre → Jacques and e2: Jacques’s wife is Marie → Maurice”, seems to be the “Data Collision” rather than “Editing Conflict”.
If this type of conflict only exists at the data level, then the evaluation in this paper is meaningless.
In addition, I guess you want to emphasize the conflict between different editing operations, as mentioned in Section 2.2 “there is a possibility that interference occurs between different edits, causing the former edit invalid.”.
Could you further clarify this problem and provide more suitable examples?

2. The “Knowledge Distortion” is a very promising research question that I pay attention to. However, the evaluation in this aspect is:
a) vague:
How many the (s,r) pairs did you evaluate to calculate the results in Table 2 ? (Is there five?)
How are the values in Table 2 calculated? Are they arithmetic mean values?
Why is the JS divergence chosen? Is the asymmetric KL divergence inappropriate? and why?

b) incomplete:
Why only evaluate triples under the same (s, r), and other knowledge is not affected? (e.g, with same (s,.,.) and same (., r, .) or others (., ., .))?

3. The proposed MLE method is unclear. Could you explain what the multi-label is and what is its function?
How does this method alleviate the problem of “Knowledge Distortion”?
Additionally, is this method effective for the first question ("Knowledge Conflict") mentioned in your paper?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
