# Achieving Human Parity in Content-Grounded Datasets Generation

- Decision: Accept
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
The lack of high-quality data for content-grounded generation tasks has been identified as a major obstacle to advancing these tasks. To address this gap, we propose Genie, a novel method for automatically generating high-quality content-grounded data.
It consists of three stages: (a) Content Preparation, (b) Generation: creating task-specific examples from the content (e.g., question-answer pairs or summaries). (c) Filtering mechanism aiming to ensure the quality and faithfulness of the generated data. We showcase this methodology by generating three large-scale synthetic data, making wishes, for Long-Form Question-Answering (LFQA), summarization, and information extraction. In a human evaluation, our generated data was found to be natural and of high quality. Furthermore, we compare models trained on our data with models trained on human-written data -- ELI5 and ASQA for LFQA and CNN-DailyMail for Summarization. We show that our models are on par with or outperforming models trained on human-generated data and consistently outperforming them in faithfulness. Finally, we applied our method to create LFQA data within the medical domain and compared a model trained on it with models trained on other domains.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper focuses on LLM-based synthetic data generation for content-based generation tasks (such as long-form QA).
The paper uses LLMs with in-context task-specific examples and new contents to generate synthetic content-related data (eg. question-answer pairs). This data is then filtered based on various factors (reward model scores, format etc.). Through multiple evaluations certain synthetic data created in that form is found to be on par with human data.

### Strengths
1. The paper is well written.
2. The paper demonstrates that the synthetic data generated through LLM can achieve parity with human data) for content-grounded generation tasks.
3. Multiple forms of evaluations are done.

### Weaknesses
1. While I have not noticed any technical issues with the paper, the main weakness seems to be the novelty and the scope of the contribution. The 2-step based generation seems fairly obvious as an approach, and it seems already been tried before in a few works as elaborated in the related works. While the exploration of content-grounded generation tasks may be new, I am not sure if simply using prior methods in another task setup (without tackling any fundamental task-specific challenges not relevant in prior works) is enough to meet the bar for ICLR.

### Questions
I am open to increasing the score if I am missing some context, highlights, or critical contrast compared to prior works. This could be provided in the rebuttal.

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
The paper introduces a method for the automated generation of high-quality, content-grounded data through a three-stage process. The experiments reveal that models trained on this data either match the performance or surpass models trained on human-generated data, with an advantage in terms of faithfulness.

### Strengths
1. Employing Large Language Models (LLMs) to generate high-quality datasets is both logical and intuitive.
2. Experiments showcase the method's effectiveness for both QA and summarization tasks.

### Weaknesses
1. The paper claims that high noise levels in existing datasets, such as news domains. This claim necessitates empirical validation. Additionally, the test set originates from the same noisy source. It is necessary to perform a Multi-Dimensional Quality assessment on both the original and synthetic datasets to evaluate genuine quality enhancements. The paper lacks specifics on annotation details, including inter-annotator agreements.
2. What if using llama 70b chat synthetic data to train a llama 70b model?  If we're talking about cost and time efficiency, then using synthetic data from LLMs to train smaller models might not be the most economical approach, if LLM itself can work well. The paper argues about the method being more cost-effective than traditional crowd-sourced dataset curation, which might exceed $1M. Yet, directly sourcing text from the web can be free, and existing filtering methods can be used to ensure data quality.
3. The paper is more like an empirical exploration into using LLMs for synthetic data generation, which is not inspiring for other works.

### Questions
why using synthetic data can improve performance on noisy test sets?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a method for automatically generating high-quality content-grounded datasets for tasks such as question answering and summarization. The method consists of three stages: content preparation, generation, and filtering. The authors showcase the effectiveness of their methodology by generating large-scale data for synthetic long-form question answering and summarization tasks. They compare models trained on their synthetic data with models trained on human-generated data and show that their models perform equally or better in terms of quality and faithfulness.

### Strengths
1. The paper presents an innovative and practical methodology for generating content-grounded datasets. The three-stage process of content preparation, generation, and filtering provides a systematic approach to ensure the quality and faithfulness of the generated data.
2. The authors provide insightful empirical findings by comparing models trained on their synthetic data with models trained on human-generated data.

### Weaknesses
1. Content-grounding generation is a broad topic, and the paper only mentions long-form QA and summarization. However, if we look at it purely from the perspective of "Content-grounding generation," most traditional NLP tasks can be transformed into the paradigm: Instruction+Input -> Output, which matches with the definition of Content-grounding generation. However,  the paper only validates this on two tasks. Furthermore, in subsequent experiments, the paper only constructs data based on specific datasets, raising doubts about the generality of the proposed method. Therefore, I tend to believe that the paper exaggerates its contributions.
2. The data construction methods mentioned in the paper rely on the format and source (Wiki) of previous datasets, making it challenging to assess their practicality in an open-world context.

### Questions
Please check the weakness.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
