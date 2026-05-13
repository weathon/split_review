# Quantifying AI Psychology: A Psychometric Benchmark for Large Language Models

- Decision: Reject
- Scores: 8, 3, 5, 5

## Abstract
Large Language Models (LLMs) have demonstrated exceptional task-solving capabilities, increasingly adopting roles akin to human-like assistants. The broader integration of LLMs into society has sparked interest in whether they manifest psychological attributes, and whether these attributes are stable---inquiries that could deepen the understanding of their behaviors. Inspired by psychometrics, this paper presents a framework for investigating psychology in LLMs, including psychological dimension identification, assessment dataset curation, and assessment with results validation. Following this framework, we introduce a comprehensive psychometrics benchmark for LLMs that covers six psychological dimensions: personality, values, emotion, theory of mind, motivation, and intelligence. This benchmark includes thirteen datasets featuring diverse scenarios and item types. Our findings indicate that LLMs manifest a broad spectrum of psychological attributes. We also uncover discrepancies between LLMs' self-reported traits and their behaviors in real-world scenarios. This paper demonstrates a thorough psychometric assessment of LLMs, providing insights into reliable evaluation and potential applications in AI and social sciences.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper explores the psychological patterns in large language models (LLMs), drawing inspiration from psychometrics. They propose a benchmark for assessing LLMs' psychological traits across five various dimensions, by a thorough design of psychometrics assessment datasets and validations of the results across different LLMs.

### Strengths
- A well-written paper and clear to understand. 
- A detailed explanation of their experiment design for each five psychological dimensions, based on solid psychological literature.
- Essential work for measuring (1) LLMs' psychological behaviors and underlying reasons and (2) their consistency, by creating a comprehensive evaluation framework that is novel and significant to LLM research for improving representations and social interaction with human users.

### Weaknesses
 - Most of the detailed explanations and results are in the Appendix; I would suggest refactoring the paper structure to move some from Appendix to the main body of the paper. 

- There is a lack of analysis on the underlying causes of LLMs' inconsistency in various dimensions. The paper only provided the numeric reports of experiment results. I would suggest conducting a small study of ablation studies.



### Questions
- L321-340: The training corpora for LLMs often consist primarily of English data, which may reflect predominantly Western cultural perspectives. Could the results discussed in this section be generalized to other cultures, especially those involving low-resource languages or non-Western societies?

- L363-365: Even humans struggle to make decisions in complex scenarios, often influenced by cultural context and environmental factors. In this light, is it possible to determine what constitutes a "better" or "moral" decision for LLMs?

- L1288-1295: the personality prompts and reverse ones are generated using GPT-4, which likely reflects GPT-4’s own personality traits. Given this, could the results differ if another model were used to generate these prompts? 

- L1874-1875: in the prompt, the rating scale in this setup seems to lack explicit definitions for each score (this is not like a widely known likert-scale). 

- When asking for ratings or scores, have you ever considered asking the models to generate a short summary of their rationale for the generated scores? It could give you more structured ideas about the underlying reasoning behind those psychological dimensions.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work provides a framework to assess five psychological dimensions (personality, values, emotion, theory of mind, and motivation). Unlike previous works, this study conducts both self-report and open-ended tests. This approach identifies discrepancies between the results of self-report and open-ended tests, which is a valuable observation.

### Strengths
- This work recognizes the difference between humans and LLM, and proposes guidelines to bridge this gap.

- A thorough reliability test was conducted on psychometric evaluation results, particularly reporting the discrepancy between open-ended and self-report questions. While this discrepancy has been observed in other work, its reporting within the field of LLM psychometrics is meaningful.

### Weaknesses
This work brings key concepts from psychology but lacks a deep understanding of the domain, losing soundness.

1. While the author recognizes the difference between LLMs and humans and endeavors to bridge the gap, some aspects are still unconvincing. In particular, applying human “personality” assessment methods to LLMs does not appear to be meaningful. The paper loses soundness in the following points.

1-1) Naive definition of “personality”
In Section 3, the author defines the human personality as a "set of characteristics that influences an individual’s cognition, emotion, motivation, and behaviors," referring to Friedman and Schustack [1]. However, this definition is overly simplistic. Even a closer look at the referred literature [1] reveals that there are more diverse and complex perspectives on the definition of human personality. Specifically, [1] introduces the perspective of Alfred Adler, who provided the foundation for modern “personality theory”. As described in [1], Adler emphasizes that a central core of personality is the striving for superiority. In other words, personality is the character a person strategically develops in the process of adapting to the social environment (i.e., to achieve superiority). For example, suppose a child is raised in a family of painters,  where parents adore him when he paints. In that case, he tends to develop a personality as a painter to achieve more compliments from his parents, which is adapting to the environment of the family. Thus, to explain personality, the aspect of “adaptation” and the “environment” is crucial.

From this perspective, the assumption that LLMs possess a personality in psychological terms may lack validity, as LLMs do not have a physical environment, nor do they have any desire for adaptation. Therefore, applying the evaluation metrics of human personality directly to LLMs may not be "meaningful," using the term in the guidelines in this work.

1-2) Insufficient references in the psychology domain
The naive definition of terminology seems to stem from a lack of a broader study of psychology. This study brings the key concept of “personality” from human psychology but does not take a look at fundamental studies on the concept. It mainly references research on psychometrics, which is only one part of the broader and fundamental study.

There are approaches that explain structural causes and mechanisms behind the personality, such as psychoanalysis, cognitive psychology, and neuroscience. Among these, psychometrics describes only the aspects that can be observed statistically, but it is based on insights derived from the aforementioned structural explorations. However, this work lacks consideration and reference to such structural perspectives.

1-3) Misuse of datasets
A naive understanding of personality has led to the misuse of datasets, which is nonsensical. The following query in the SD3 (Short Dark Triad) can be an example of misuse, which is used to assess the LLM's personality in this work.

One of the questions in SD3 is, "I enjoy having sex with people I hardly know." This likely aims to assess whether the human respondent tends to consider risks related to safety and morality in pursuit of sexual pleasure. It addresses how humans manage and regulate the essential instinctual desires within a social environment. This question can clarify personality, as it asks the style of adaptation to the environment. However, for an LLM, "sex" does not ground to a real substance. LLMs have never experienced it, do not know what it feels like, and have no desire for it. They also face no moral judgment or danger of disease. It does not involve adaptation and environment for LLMs. Thus, asking LLMs such a question cannot reveal anything about their personality in psychological terms.

2. Conversely, this work endeavors to strictly apply guidelines to “motivation” and “emotion”, providing alternative redefinitions for them. However, this effort makes the study disconnected from psychometrics.

In Section 5, the author redefines the evaluation of emotion as "understanding another person's emotion." However, "understanding the target's emotion" and "assessing how well the target understands others' emotions" are different tasks, though they share the keywords “understanding” and “emotion”. It is difficult to consider the latter as an assessment of the target's emotion. In Section 7, the author redefines motivation as "self-efficacy." However, motivation is distinct from self-efficacy. 

This work redefines the terms “emotion” and “motivation” into entirely different meanings and then measures them, which is outside the boundaries of psychometrics.

### Questions
Comments/Suggestions/Typos
Despite its weaknesses, this work presents valuable observations regarding inconsistencies in evaluation results. In particular, this observation could serve as solid evidence to argue that LLMs do not possess attributes corresponding to personality in a psychological sense. We suggest shifting the direction of the paper to emphasize this point.

Additionally, definitively titling the work as "AI Psychology" implies that the psychometric evaluations for AI in terms of human psychology are entirely reasonable. This can limit diverse interpretations of the evaluation results, and give the impression that the results have been misinterpreted.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents psychometric benchmark for LLMs, covering five aspects: personality, values, emotion, theory of mind, and motivation. 
It tested LLMs on various scenarios such as self-reported questionnaires, open-ended questions, and multiple-choice questions.

This paper finds that 1) LLMs exhibit discrepancies in psychological tendencies when responding to closed-form versus open-ended questions; 2) LLMs have consistent performance on tasks that require reasoning, such as theory of mind or emotional intelligence; 3) Models vary in position bias and prompt sensitivity.

### Strengths
1. This paper combines existing datasets, psychological tests in to one unified benchmark, resulting a more comprehensive evaluation than previous works.
2. It covers five aspects: personality, values, emotion, theory of mind, and motivation and tests on various scenarios such as self-reported questionnaires, open-ended questions, and multiple-choice questions.

### Weaknesses
1. These proposed dimensions seems to be independent and can be more convincing. For example, the authors could provide more discussions about why these 5 dimensions are selected, what are the logical relationships between these aspects/datasets, and whether/why/how they are the best representation of AI psychology.  
2. Lacking in in-depth analysis and/or insights. First of all, the current conclusions are also disconnected and scattered into independent sections. I would like to see a more coherent and connected narratives. Secondly, the current findings, such as there are discrepancies in closed-form versus open-ended questions, are not completely novel and lacks in-depth analysis.

### Questions
N/A

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a psychometric benchmark for large language models (LLMs) that spans five psychological dimensions: personality, values, emotion, theory of mind, and motivation. The findings suggest that LLMs exhibit a broad range of psychological patterns.

### Strengths
- The paper provides an interesting conclusion that LLMs show discrepancies in psychological tendencies when responding to closed-form versus open-ended questions.
- A substantial amount of usable data has been collected, which could facilitate future research.
- The authors have taken several measures to ensure the reliability of their conclusions, which could serve as a good example for future work.

### Weaknesses
 - The writing is somewhat disorganized, and the structure is unclear.

- The authors claim that their contribution is to investigate psychology in LLMs. However, two of the four findings listed in the introduction are well-known and have been extensively studied, namely, position bias and prompt sensitivity, and the reliability of LLMs as judges. This diminishes the novelty of the paper’s contribution. I would prefer to see the authors summarize new findings based on their own experimental results, or present new insights on the well-known issues of position bias, prompt sensitivity, and the reliability of LLM-as-a-judge.

- There is a lack of discussion on how the findings could guide improvements in future research.

### Questions
- The motivation for this paper is not entirely clear. What does it mean to 'investigate psychology in LLMs'? What benefits can we gain from investigating psychology in LLMs? Could the authors offer **specific** application scenarios to clarify this?

- I noticed that the prompts used by the authors often begin with "You are a helpful assistant" (e.g., Line 1279, 1870). Could this influence the evaluation results, particularly when assessing the personality of the LLM? This phrase may prompt the LLM to appear more open and friendly, potentially masking its inherent personality traits.

- The authors use two competent LLMs, GPT-4 and Llama3-70b, as judges to rate the performance of LLMs on open-ended questions. Given the instability and bias-proneness of LLM-as-a-judge, I would like to see human evaluation results and a comparison of how human evaluations correlate with LLM-as-a-judge results. This would help validate the effectiveness of using LLMs to judge other LLMs' performance in open-ended questions.

- Can you discuss how future research might be improved based on the findings of this paper?

I understand that combining AI and psychology is a challenging and valuable research direction. If the authors can address my concerns, I would be happy to raise my score.

#### Minor Issues

- The authors should provide relevant citations for the statement in Lines 043-044, rather than citing two papers that merely introduce psychometrics.

- More results should be included in the main text to enhance the readability of the paper and provide a clearer understanding of the findings.

- Typo in Line 123: “Llama3-7b” should be “Llama3-70b.”

- What does "Number" in Table 1 refer to? the number of items?

- What is the version of the LLM used in this paper?

### Soundness
3

### Presentation
2

### Contribution
2
