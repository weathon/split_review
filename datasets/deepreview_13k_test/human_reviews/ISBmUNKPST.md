# MentalChat16K: A Benchmark Dataset for Conversational Mental Health Assistance

- Decision: Reject
- Scores: 6, 6, 5, 5

## Abstract
We introduce MentalChat16K, an English benchmark dataset combining a synthetic mental health counseling dataset and a dataset of anonymized transcripts from interventions between Behavioral Health Coaches and Caregivers of patients in palliative or hospice care. Covering a diverse range of conditions like depression, anxiety, and grief, this curated dataset is designed to facilitate the development and evaluation of large language models for conversational mental health assistance. By providing a high-quality resource tailored to this critical domain, MentalChat16K aims to advance research on empathetic, personalized AI solutions to improve access to mental health support services. The dataset prioritizes patient privacy, ethical considerations, and responsible data usage. MentalChat16K presents a valuable opportunity for the research community to innovate AI technologies that can positively impact mental well-being.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a new benchmark mental health counseling dataset, named MentalChat16K. The dataset comprises question-answer pairs derived from transcripts of interactions with patients in palliative or hospice care. Additionally, the authors create a synthetic counseling dataset using large language models (LLMs). Experimental results show that fine-tuning LLMs with MentalChat16K significantly improves performance over non-fine-tuned baselines across seven metrics, as evaluated by both LLMs and human annotators.

### Strengths
The primary strength of this paper is its introduction of the MentalChat16K dataset, a valuable mental health benchmark. Generating counseling responses is challenging due to the sensitive nature of the data, making dataset creation and public availability rare. MentalChat16K, being both sizable and relevant, is likely to prove useful in broader mental health and conversation tasks. The paper is generally well-written, though some parts would benefit from further elaboration.

### Weaknesses
I have a few unresolved questions that would clarify the study's contributions and could enhance the paper.

### Questions
- Who annotated MentalChat16K (referred to as human experts in lines 182 and 188)? Are these the same annotators who evaluated model performance (referred to as human experts in line 275)?
- MentalChat16K contains a total of 6,338 question-answer pairs. How many conversations does the dataset comprise? Are the pairs presented as individual exchanges, or do they maintain conversational continuity?
- What are the scores of the ground-truth responses in MentalChat16K when evaluated by the same metrics used to assess LLM performance? Since the evaluation method is reference-free, it would be useful to know how the dataset responses score according to the proposed metrics, and whether these scores exceed those of the fine-tuned LLMs.
- What test dataset was used in the experiments? Was an 80/20 split applied for training and testing, or was a different setup used? The reported p-values suggest multiple experimental runs, but Section 4.4 lacks details on the experimental setup.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors develop MentalChat16k, a dataset consisting of two parts -- synthetic counseling conversations and paraphrased and anonymised real life interventions between behavioral health coaches and caregivers of patients in hospice or palliative care. They benchmark their dataset using 7 LLM models and 2 other baseline models. Finally, they use the finetuned and baseline methods to answer 200 mental health related questions, from Reddit, to see the performance difference. The authors found that the models finetuned on the MentalChat16k outperformed the other methods in the QA task, using their developed evaluation framework.

### Strengths
- The authors curate an interesting dataset consisting of two type of important communication in the domain of mental health.
- They provide an empirical validation of the use of dataset by a thorough comparison of different LLMs and other baselines.
- The authors provide valid use cases for the curated data and verify it experimentally too.

### Weaknesses
- The paper should have had a table summarising the dataset statistics for easy access.
- Examples of generated counseling transcripts in the paper would be useful to evaluate them.
- It would be interesting to observe if the paraphrasing step, as illustrated in Table 1, results in any hallucinations to complete the given "requirements" in the prompt.
- Inter annotation agreement for human evaluation would enhance the human evaluation.

### Questions
See weaknesses please.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces MentalChat16K, a benchmark dataset for conversational mental health assistance. The dataset contains 16,000 question-answer pairs, including synthetic counseling conversations generated by GPT-3.5 Turbo and anonymized transcripts of interventions between caregivers of palliative or hospice patients and behavioral health coaches. Researchers utilized the QLoRA technique to fine-tune multiple state-of-the-art lightweight language models with 7 billion parameters to meet the needs of mental health counseling. They defined seven evaluation metrics and used GPT-4 Turbo, Gemini Pro 1.0, and human experts as evaluators to assess the models’ performance.

### Strengths
This paper addresses the critical gap in real-world data for conversational mental health assistance. The lack of authentic psychological data has long posed a challenge in this field, and by collecting anonymized transcripts of intervention dialogues between behavioral health coaches and caregivers of palliative or hospice care patients, this paper provides researchers with a valuable data source.

### Weaknesses
Although the paper demonstrates commendable efforts in creating the MentalChat16K dataset and fine-tuning large language models (LLMs) for mental health counseling, weaknesses in the evaluation methodology limit its impact and generalizability.

1. Reliability of LLM-Based Evaluation: The study primarily uses GPT-4 Turbo and Gemini Pro as automated evaluators to assess the performance of fine-tuned models. This approach presumes that these LLMs can objectively and accurately evaluate counseling responses across seven custom-defined mental health metrics. However, due to inherent biases and limitations, LLMs may not be entirely reliable as evaluators, especially in specialized fields such as mental health counseling.

2. Inconsistency in Evaluation Scores: As shown in Table 3, there is a notable inconsistency between evaluations from GPT-4, Gemini Pro, and human experts. Almost all scores from Gemini are higher than those from GPT-4, and Gemini’s scores diverge significantly from Human Rankings. This discrepancy raises concerns about the validity and robustness of using LLMs as evaluators, as they might not effectively capture the nuances involved in mental health counseling.

3. Outdated Evaluation Techniques: The paper employs simple prompt-based evaluation methods but does not leverage advanced frameworks in NLG evaluation. State-of-the-art methods such as G-Eval [1] and Prometheus [2] provide more sophisticated and reliable assessments of LLM outputs, which could yield a more accurate and nuanced evaluation of the models’ effectiveness.

[1] G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment https://arxiv.org/abs/2303.16634

[2] Prometheus: Inducing Fine-grained Evaluation Capability in Language Models https://arxiv.org/abs/2310.08491

### Questions
1. How were human evaluators instructed to rank model responses, and were there specific criteria or guidelines provided to ensure consistency and objectivity? Additionally, was any inter-rater reliability measure (e.g., Cohen’s Kappa) applied to validate the consistency of human rankings across evaluators?

2. Would the paper benefit from including side-by-side examples of model responses versus human counselor and baseline model responses? Could such examples better illustrate the model’s performance on key metrics like empathy, clarity, and safety?

3. Were participants explicitly informed about the potential use of their anonymized data for AI model development and research purposes?

### Soundness
2

### Presentation
3

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
This paper introduces a new dataset, MentalChat16k, as a potential benchmark dataset for evaluating the use of LLM in mental health counseling. The dataset hybridizes both (a) real interview transcripts between Behavioral Healthcare Coaches and caregivers of hospice patients and  (b) synthetic mental healthcare counseling question-answer pairs generated by GPT-3.5 Turbo and encapsulates over 16k question-answer pairs. The authors fine-tuned a wide range of families of small-scale (7B) LLMs on the datasets and conducted extensive qualitative evaluation on the performance of the fine-tuned models on a hold-out evaluation dataset of 200 questions collected from real-world discussion of mental health issues on public forums. The evaluation metrics differ from conventional quantitative metrics and focuses more on the empathetic aspects of the model generated responses to the healthcare questions, and both automatic evaluation done by LLMs (GPT-4 Turbo and Gemini Pro 1.0) and manual judgement done by domain experts have shown significant improvement in the empathy demonstrated in the generated responses of models fine-tuned on MentalChat16k, indicating the effectiveness of the dataset in helping models tackle the nuance and sensitive nature of assisting in the mental health domain.

### Strengths
Originality: Excellent

Most existing datasets on depression and mental health issues focus on detection, thereby datasets are usually structured for classification, not generation. This dataset is a nice addition to this research space of NLG in healthcare.

Also, the seven-factor evaluation metrics is a novel contribution to the conventional evaluation metrics in NLG. The proposed metrics suite focuses on empathy more than accuracy, aligning better with the nuanced emotional requirements of real-world application of LLMs in sensitive areas such as mental health counseling and terminal care. However, the hastily introduction of new metrics can also contribute to reproducibility and generalizability problem with the research, which I will address in the weakness section.

Quality: Good
Paper presentation and language are generally excellent, with a few editing typos that need to be addressed.

Clarity: Excellent
The structure of the paper and the writing makes it very easy for the reviewer to follow.

Significance: Good
This paper aims at a focused group of researchers and rather than contributing to the general theoretical understanding of deep neural networks. The integration of deep learning and healthcare is becoming ever more relevant from both a research and a realistic perspective, and almost all areas of research in this space suffer from lack of quality data, so contribution of large-scale, high-quality healthcare data is always welcomed.

### Weaknesses
Clarity:
1. A few details on the data collection procedure could be clarified. For example: 
  - Is the demographic information the only type of meta data collected? 
  - What about the 93 caregivers without demographic information? Will the question-answer pairs from them be missing the meta data? 
  - How good (in terms of diversity, topic coverage, etc.) are the synthetic question-answer pairs? 
  - It would be great if the authors could provide concrete example of the actual data, both from interviews and from the synthetic data, 
  - A brief explanation (or examples) that lays out the data structure (.json format? plain txt? what meta data is available? any data splits?) would be helpful, either in the main body or in the Appendix.
2. Basic statistics about the dataset are lacking in the paper, I would recommend the following statistics be added and organized in a table:
  - Exact dataset size and breakdown by interview data and synthetic data. Both are only mentioned now in the main text.
  - Length distribution (word count or character count) of the QA pairs.
  - For interview data portion, distribution of number of QA pairs across interview transcripts; or at least provide the average number of QA pairs obtained from each visit. 
  - For synthetic data, number of QA pairs distribution across each topic.

Quality:
1. It is unclear why the authors would break a complete interview, which the reviewer assumes to be a coherent series of questions and answers between healthcare coaches and caregivers, into individual QA pairs. It would be constructive to include discussion or reasoning on this particular choice for data collection. Specifically,
  - Please explain how the loss of contextual information, when breaking conversation into QA pairs, would affect the data quality.
  - Is the paraphrasing conducted to address partly this concern? So that each QA pair becomes somewhat independent of each other?

2. The introduction of the seven-factor evaluation metrics on empathy is interesting and novel to the reviewer, but because this is the only evaluation done by the authors, it also tends to conflate the focus of the paper into a paper of both a new dataset and a new, untested metrics. A few related points that could strengthen the paper, but lacking in the current version, are:
  - Why are the scoring scale different between LLM-based and human evaluation? 
  - The reviewer appreciates the detailed explanation of each score to be used in the prompt for LLM-based evaluation, but since this is such a detailed and nuanced range of scores, would the LLM really be capable of differentiating between different scores? Showing a distribution of LLM-based evaluation score one or few factors would be helpful. For example, it would point to potential issues if the resulting scores across 200 examples concentrate around "typical good" values, like 7 or 8.
  - Are the seven-factor metrics employed only in LLM-based evaluation, or do human experts follow along the same line of logic when evaluating the quality of the response? 
  - Since human evaluation is involved, and multiple experts have worked on the same question during evaluation, it would be more robust to include inter-rater agreement between the experts (or at least the variance in human ratings in addition to simple mean).

3. The findings in Table 3 and Table 8 also seem to point to questions left unanswered about the dataset. As can be seen in both of the tables:
    1. It is not true that more data generally leads to better performance
    2. It seems consistent that combining interview data with synthetic data actually HURTS model performance across all seven factors and model families
    3. It seems human evaluation consistently prefers models fine-tuned on synth data only

**3.3** alone could put into question the value of real data based on interviews if evaluation shows synthetic data seems to help model more. But the reviewer believes this may be attributed to misalignment between the interview data and the evaluation set. A couple of suggestions on analysis that could be included to pinpoint potential causes:
   1. Since the evaluation set contains data (InFamousCoder) originally designed for depression classification. Use the models (base and fine-tuned) to run classification on the question; the model performance could then point out the generalizability of the dataset (if fine-tuning benefits the model) or domain shift (if fine-tuning hurts the model performance) between MentalChat16k and the evaluation set.
   2. Conduct similarity-based analysis between questions in the synthetic data, in the interview data, and in the evaluation set. Reddit is a public data source that could be used in the training of GPT models, so this could reveal potential data leakage issue in the synthetic data. This is **not** an invalidation of the synthetic data, but more revealing the lack of efficacy in the evaluation approach. And it could also help reveal if there's an obvious domain shift between interview data and the synthetic data.
   3. Both 1 and 2 are trying to identify the cause behind the performance degradation when both sources of data are combined in model fine-tuning. But regardless of the findings, table 3 and 8 do point to the need of a finer-categorization of the dataset. It may be helpful to separate the dataset into two parts and caution the users to combine them naively together. 
   4. Another evidence supporting the separation of interview data and synthetic data is the contrast between the context; The interview data was created based on a very focused group of caregivers offering care to a specific group of patients, this is in stark contrast to the unbounded target profile used in generating the synthetic data. 
   5. If the goal of the dataset is to help improve **empathetic responses** from LLMs in the setting of mental healthcare counseling, then the reviewer suggests expanding the dataset by covering a wide range of responses different in level of empathy; that is, intentionally including non-empathetic responses, to better cover the range of the seven-factor metrics. Given the novelty of the metrics, such a dataset could also be ideal to further evaluate the robustness of  the metrics and LLM's capability of automated evaluation. This could be an extension of future work.

I'd like to emphasize that these weaknesses do NOT diminish the value of this dataset, but it does require more elaborated discussion, and probably a more thorough statement in the **Limitations** section.

### Questions
1. Do you intend to publish the dataset? It is unclear from the writing whether this is intended for public use. I apologize if I missed a statement or url on this.
2. Clarifying question: what is the hypothesis testing used in calculating P-value in Table 3 and Table 8? I assume it's two sample t-test, but it would be nice to clarify it in writing.
3. Are the 200 questions crawled from Reddit and Mental Health Forum to be included as part of the dataset, or are they mostly for evaluation purpose for this paper? The depression data from Reddit, judging by the dataset from InFamousCoder, are typically not in the form of questions (more like posters explaining the hardship they've been through), were there any filtering or cleaning involved in selecting questions from the data?

Miscellaneous:
1. In Table 3 and 8, would it be better to rearrange the models in each family by the number of examples used in training? That is, order them by Base Model, Base Model + Interview data (\~7K), Base Model + Synth Data (\~10K), Base Model + Both (16K). It could help visualize the effect of dataset size on the finetuning (which is not significant, as would be obvious in the proposed order).
2. Typos: page 2, "toaddress"

### Soundness
3

### Presentation
3

### Contribution
3
