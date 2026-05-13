# Peer Review as A Multi-Turn and Long-Context Dialogue with Role-Based Interactions: Benchmarking Large Language Models

- Decision: Reject
- Scores: 6, 6, 5

## Abstract
Large Language Models (LLMs) have demonstrated wide-ranging applications across various fields and have shown significant potential in the academic peer-review process. However, existing applications are primarily limited to static review generation based on submitted papers, which fail to capture the dynamic and iterative nature of real-world peer reviews. In this paper, we reformulate the peer-review process as a multi-turn, long-context dialogue, incorporating distinct roles for authors, reviewers, and decision makers. We construct a comprehensive dataset containing over 30,854 papers with 110,642 reviews collected from the top-tier conferences. This dataset is meticulously designed to facilitate the applications of LLMs for multi-turn dialogues, effectively simulating the complete peer-review process. Furthermore, we propose a series of metrics to evaluate the performance of LLMs for each role under this reformulated peer-review setting, ensuring fair and comprehensive evaluations. We believe this work provides a promising perspective on enhancing the LLM-driven peer-review process by incorporating dynamic, role-based interactions. It aligns closely with the iterative and interactive nature of real-world academic peer review, offering a robust foundation for future research and development in this area.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Since existing applications are primarily limited to static re- view generation based on submitted papers, authors reformulate the peer-review process as a multi-turn, long-context dialogue, incorporating distinct roles for authors, reviewers, and decision makers. 

construct a comprehensive dataset containing over 30,854 papers with 110,642 reviews collected from the top-tier conferences 

proposes a series of metrics to evaluate LLMs for this

### Strengths
Strengths:
	• The work is timely, the motivation is solid. Definitely more automated peer review work needs to be done given the volume of papers being submitted
	• The dataset will help future work, it’s a really great resource.
However with that being said, please look into the weaknesses mentioned

### Weaknesses
Weaknesses:

1. 211-214 - opening of double inverted commas - fix typo please

2. In fig 2, mask out the author names ? - please annonymize 

3. Fig 3c, is it enough to report mean ? Why not variance ? Why not a comprehensive view including quartiles
4. 3d - why a gross report of accepted vs rejected ? Please add year wise split in appendix
5. Cant see the prompts on the paper used to evaluate GPT4o, or other models as well in zero shot

6. Evaluation pipeline is unclear  - its unclear which model is role-playing the author, and which model is the reviewer and which one is the final judge - experiment section needs more detail 

What does a model take into account while generating the reviews ? Is it just the paper in raw text ? Do you remove the bibliopgraphy section ? Is appendix part of the context ? 

Lines 210-214 gives a rough sketch on what each turns include, but there is ambiguity I feel. 

7. What is the train test split of the dataset ? Do we have in-domain and out of domain- test sets ? Please point out in case this is already reported, if not reported, please do. Do train and test sets have different number of tokens on average and same for scores assigned

7. While the dataset is well-motivated, I feel that a better job can be done here

Neurips, ICLR is too little scope I feel, while the authors address this weakness in their discussion, this needs to be addressed. But I do understand that as a first step towards realistic resource building this might be a good start

Is rouge a good metric ? Often models are quite verbose (which might hurt the rouge scores), does not mean that their responses are bad. This is a concern !

### Questions
Q1. Please explain the inference and evaluation pipeline in more detail.
Q2. I feel that the dataset curated is quite rich. Can we have a more detailed dataset statistics section. And even in results. For example - which models are more likely to accept a paper. Can we have a baseline where given a paper with randomly chosen sections from different paper ( abstract from paper 1, intro from paper 2...) to see whether LLMs are strong enough to make sense of it - do they give it an acceptable score ?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the ReviewMT dataset, created to advance language model research in academic peer review processes. The dataset captures the dynamic, iterative nature of real-world peer review by collecting all review records from ICLR conferences since 2017 and partial review records from NeurIPS conferences since 2021. ReviewMT is a long-text, multi-turn dialogue-style dataset that facilitates language model review of ML and AI papers.

---

## After the discussion period

I am optimistic about the potential impact and contributions this paper could make - and this is very positive! For instance, with ICLR introducing LLM-assisted reviewing this year, I look forward to having super powerful and non-hackable LLMs that can help promote fairness in peer review and reduce the burden on all reviewers.

However, after the discussion period, my concerns remain, particularly regarding the validity of human evaluation and the limitations of the current experimental setup and evaluation framework, which leave us uncertain about the true performance of the fine-tuned models. These concerns could potentially be addressed through targeted experiments (the most interesting would be to examine the degree of similarity between the model's predictions and the actual ICLR 2025 outcomes).

**Rating: 5.5**

### Strengths
The authors provide an unprecedented large-scale ML/AI review dataset. Based on this, they conduct extensive empirical studies to demonstrate the performance of various open-source and closed-source language models in peer review tasks.

### Weaknesses
I don't see significant technical novelty or innovative contributions in this paper. The dataset is simply downloaded and processed from the OpenReview website, with its format directly derived from ICLR/NeurIPS conference review documents. The authors then use the LLAMA-FACTOR library to fine-tune several language models under 10B parameters. I struggle to see deeper analysis and modeling for this task.

My primary concern is the lack of systematic analysis of the review task. From the experimental design, we're still unclear about existing deficiencies. The authors use typical NLP generation evaluation metrics, including BLEU, ROUGE, BERT-Score, Validity of response, and human evaluation of consistency with original content. However, when using language models for peer review simulation, we may face issues such as exaggerated text, distorted score distributions, overlooking existing papers (inability to accurately judge paper novelty through literature retrieval), contradictions with real paper conclusions, and serious hallucinations and biases. The authors' experimental results don't reveal these conclusions, instead merely telling us that "fine-tuned models perform better than non-fine-tuned ones, GPT-4 performs well, and GLM is second to it" - these conclusions are rather superficial.

Additionally, I have other concerns about missing details:
- Introduction line 53: I don't understand what "generating static reviews" means, as the dataset structure doesn't seem to reflect "non-static reviews."
- Introduction line 72 shouldn't overemphasize "we offer a novel perspective on the complete peer-review process," as the original dataset collected from ICLR/NeurIPS inherently follows a multi-reviewer with AC structure, which is the existing peer review framework.
- How are formulas, tables, and figures in each paper processed? These are essential for any review process. Marker tools don't handle mathematical formulas well, especially in ML papers, where incorrect formulas introduce significant noise. Also, not all chosen language models are multimodal, leaving unclear how figure information is considered.
- The authors claim average token count exceeds 20,000 in ICLR 2024 training set, yet their models (QWEN: 8192, Gemma/Gemma2: 8192, Yuan: 8192, Baichuan2: 4096) mostly can't accommodate this length. It's unclear how these models handle long text during training and generation.
- Presentation inconsistencies exist, such as ChatGLM3 being described as "with a default selection of 6B to 9B parameter" in line 362 but "with 130 billion parameters" in line 1022. Model specifications and access points aren't clearly stated. For instance, YUAN2 only has 2B, 51B, and 102B accessible versions, with no 6B-9B versions, affecting reproducibility.
- The authors mention recruiting five expert reviewers to evaluate language model outputs but don't specify who they are, how they were recruited, their evaluation process, or their expertise. Given the test set covers various ML topics, it's uncertain whether these five expert reviewers are qualified to evaluate such diverse research directions.

### Questions
See in weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper reframes the paper review process as a multi-turn long-context dialogue task, defining three distinct roles: author, reviewer, and decision maker. In this task framework, the study gathered a dataset related to paper reviews and assessed the performance of existing language models using this dataset.

### Strengths
* Framing the review of scientific papers as a multi-turn long-context dialogue task is intriguing and mirrors real-world scenarios.
* The gathered dataset holds significant value for the research community in this field.

### Weaknesses
### 1. Suggestions on Writing

1. The first paragraph (Lines 32 to 47) is not relevant to the research topic of this paper and can be deleted entirely.
2. Section 2.1 in the Related Work section is unrelated to the research topic and should be removed.
3. Figure 4 could be relocated to the Appendix instead of the main paper as it may not be crucial to the task.
4. Additionally, it is essential to discuss some significant prior works in the related works section. For instance, recent works such as SEA [1] have been proposed to streamline the automatic review process.

---

[1] Automated Peer Reviewing in Paper SEA: Standardization, Evaluation, and Analysis

### 2. Confused Evaluation Protocol

The description of the evaluation is unclear. The authors introduce a set of automatic evaluation metrics in Section 5.1, but fail to provide important details. For instance, it is not specified which responses are evaluated by these metrics – the responses of authors, reviewers, or decision makers.

If these metrics are solely employed to assess the responses of reviewers, it raises the question as to why the evaluation of other roles is omitted.

### 3. Unreliable Evaluation Metrics

The evaluation metrics introduced have been widely utilized in many previous peer review generation tasks. Nonetheless, the reliability of these metrics is somewhat limited as they only assess text similarity between the reference reviews and model-generated reviews.

Introducing human evaluation is a positive step. However, peer review is inherently subjective, relying on the personal opinions of researchers. Additionally, human annotation is costly and can significantly impede the scalability of evaluation within your proposed dataset.



### 4. More turns of Dialogue

As described in Section 3, the multi-turn dialogues for paper review consist of only 4 turns, including review generation, rebuttal generation, final review generation, and decision-making. However, in the real-world review process, such as on the OpenReview platform, the conversations between paper authors and reviewers typically involve numerous utterances, not just 2 turns (rebuttal and final review). Therefore, I believe that the task formulation should be extended to take these factors into consideration.

### Questions
In Section 4.3 (line 268), it is mentioned that the average length of submissions falls within the range of 11,000 to 20,000 words, posing a significant challenge for the inference process of Language Model Models (LLMs).

I suggest that the authors provide a more detailed description of the LLM inference process to enhance clarity and understanding.

### Soundness
2

### Presentation
1

### Contribution
2
