# Diverging Preferences: When do Annotators Disagree and do Models Know?

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
We examine \textit{diverging preferences} in human-labeled preference datasets. We develop a taxonomy of disagreement sources spanning 10 categories across four high-level classes---task underspecification, response style, refusals, and annotation errors. We find that the majority of disagreements are in opposition with standard reward modeling approaches, which are designed with the assumption that annotator disagreement is noise. We then explore how these findings impact two areas of LLM development: reward modeling and evaluation. In our experiments, we demonstrate how standard reward modeling methods, like the Bradley-Terry model, fail to differentiate whether a given preference judgment is the result of unanimous agreement among annotators or the majority opinion among diverging user preferences. We also find that these tendencies are also echoed by popular LLM-as-Judge evaluation methods, which consistently identify a winning response in cases of diverging preferences. These findings highlight remaining challenges in LLM evaluations, which are greatly influenced by divisive features like response style, and in developing pluralistically aligned LLMs. To address these issues, we develop methods for identifying diverging preferences to mitigate their influence on evaluation and training.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper discusses a proposed distributional reward model aimed at addressing the issues of distinguishing between divided preferences and high-agreement preferences in reward modeling for language models (LLMs). It points out that standard reward modeling approaches, such as Bradley-Terry and MSE regression, fail to differentiate between these two types of preferences, leading to similar reward distributions and potential problems in multi-dimensional alignment when using Reinforcement Learning from Human Feedback (RLHF).

The authors outline two main objectives for their model: (1) identifying preferred responses and (2) detecting responses that may exhibit divided preferences. By achieving these objectives, the model aims to prevent the system from learning responses that reflect only a single user perspective. The authors argue that training this reward model is more cost-effective and efficient compared to obtaining multiple annotations for every data point.

To evaluate the model's performance, two metrics are introduced: Preference Accuracy, which assesses the model's ability to assign higher rewards to responses selected by human annotators, and Diverging ID AUROC, which measures the model's effectiveness in identifying divided preferences within response pairs.

The results, based on training and evaluation with the HelpSteer2 and Multipref datasets, indicate that the proposed distributional reward model performs effectively, consistently exceeding the baseline metrics for both Preference Accuracy and Diverging ID AUROC. This demonstrates that the proposed model can predict expected rewards while reflecting the controversy of responses as assessed by different annotators.

In the latter sections, the paper explores biases inherent in the evaluation of LLMs using the LLM-judge method, particularly when preferences are divided. It discusses how the LLM-judge’s assessment may unfairly penalize systems that reflect less popular opinions or that are trained with consistent policies in ambiguous scenarios.

### Strengths
Identification of Problems: The proposed distributional reward model clearly identifies existing issues in the current methodologies.
Experimental Evidence: Strong experimental evidence is provided to support the effectiveness of the proposed model.
Well-Organized Structure: The paper has a well-organized structure, making it easy to follow.
Effective Use of Visuals: Tables and figures are effectively utilized to present experimental results.
Contributions to Multi-Dimensional Alignment: The research offers a new methodology for addressing the problem of multi-dimensional alignment in LLMs through the distributional reward model.

### Weaknesses
Lack of Discussion on Limitations: There is insufficient discussion regarding the limitations and potential issues of the proposed method, particularly concerning the outdated model.
Complex Technical Details: Some technical details are explained in a complex manner, which may hinder understanding for non-experts.
Need for Practical Applicability Discussion: The paper lacks a thorough discussion on the practical applicability and limitations of the proposed approach, which could enhance its relevance and usability.

### Questions
Discussion on Limitations: What specific limitations of the proposed distributional reward model should be addressed in future research?
Complexity of Technical Details: Which technical details were particularly complex, and how might they be simplified for better understanding?
Practical Applicability: What are the potential real-world applications of the proposed approach, and how could its limitations affect these applications?
Outdated Model Concerns: How does the findings with Llama-3-8B Instruction model impact recent research?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper studies disagreement in preference datasets and provides annotator-level annotations of two existing human preference datasets, [HelpSteer2](https://huggingface.co/datasets/nvidia/HelpSteer2) and [MultiPref](https://huggingface.co/datasets/allenai/multipref). The paper first derives a taxonomy of causes for disagreement (Table 1) on a sample of 100 items. Then, the authors train two separate standard reward models using the majority vote preferences (Bradley-Terry and MSE Regression) and find that on examples with diverging preferences the predictions of reward models are biased towards high-agreement preferences. To address this gap, a model with distributional rewards (Mean-Variance Reward Model, with KL) is presented which uses a KL-divergence loss. The results show that the KL-based distributional model outperforms a Mean-Variance baseline model and better aligns with human preferences. Finally, the paper presents experiments in LLMs-as-a-judge evaluation, finding that they promote majority preferences.

### Strengths
Positive aspects of the paper:
- Releasing unaggregated annotator labels is of increasing importance, as there is increasing evidence that modeling the aggregate leaves out important human preference information. This supports similar earlier calls to do so - see [Basile et al., 2021](https://aclanthology.org/2021.bppf-1.3/), [Prabhakaran et al., 2021](https://aclanthology.org/2021.law-1.14/), [Plank, 2022](https://aclanthology.org/2022.emnlp-main.731/). 
- Studying reasons for disagreement is similarly important, the derived taxonomy is insightful. It extends prior taxonomies by providing categorizations for LLMs for refusal behavior, which is novel. The taxonomy further supports prior findings on reasons for disagreement [Basile et al., 2021](https://aclanthology.org/2021.bppf-1.3/) and taxonomies of disagreement in NLP, which were developed by [Jiang and de Marneffe, 2021](https://aclanthology.org/2022.tacl-1.78/) for NLI, and extended to other tasks, for example, subjective language [Sandri et al., 2023](https://aclanthology.org/2023.eacl-main.178.pdf) and law applications [Xu et al., 2023](https://aclanthology.org/2023.emnlp-main.594.pdf).
- Distributional rewards are timely. The paper presents a simple and concrete implementation. (The question remains whether code will be released upon publication).
- The impact on diverging preferences on LLMs as judges is, to the best of my knowledge, novel. This is an important study showing that neglecting divergences propagates majority views and thus is in competition with pluralistic alignment (Sorensen et al., 2024).

### Weaknesses
The paper's weaknesses are:

- Evidence (lines 265-266): The claim that "reward models predict differences in rewards that resemble high-agreement preferences, even when trained on all annotator labels" is not convincingly supported. The scores for models trained on all labels vs. aggregated labels (All vs. Agg) are often similar. To substantiate this claim, the authors should extend Figure 2 and compare models trained on majority labels vs. all annotator labels on both datasets. Currently, Figure 2 only presents results for the model trained on aggregated labels and for a single dataset, illustrating that diverging preferences align with high-agreement items. For a stronger argument, similar plots should be included for both models and across datasets and discussed in the text.

- Related Work: The field of disagreement in NLP has a substantial history, with early contributions such as de [de Marneffe et al., 2012](https://aclanthology.org/J12-2003/), [Poesio and Artstein, 2005](https://aclanthology.org/W05-0311/) and more recent surveys like  [Uma et al., 2021](https://jair.org/index.php/jair/article/view/12752). This paper could be improved by citing more of this foundational literature, including key work on developing taxonomies and understanding the underlying reasons for disagreement (suggested references below).
  - Reasons for disagreement in NLP and computer visions: see [Uma et al., 2021](https://jair.org/index.php/jair/article/view/12752) and references therein. Moreover, see further references on calls to release unaggregated labels in first point in Strengths.
  - Taxonomies of disagreement: There exists seminal work by [Jiang and de Marneffe, 2021](https://aclanthology.org/2022.tacl-1.78/), I wonder whether this paper was inspired by their work? It was taken up by several others, see further references in second point in Strengths.


- Table 1: Do the frequencies in the two datasets sum up to 1? Is this per subcategory, or what is the overall frequency for each of the four top categories on MP and HS2?

- Code release is not mentioned. Releasing the code would make some study design choices clearer (like the mapping above) and enable better replication of the results in the paper.

- The paper could have included more recent and larger language models. For example, results for the LLama model family over different scales would be interesting. I invite the authors to discuss any potential challenges or limitations in applying the method to larger model families, or to explain why you chose to focus on this specific model (llama 8b instruct).


### Questions
- Unclear Mapping Explanation in the Mean-Var Reward Model (lines 319-323): The rationale for mapping the labels back to specific ranges is unclear—why is this mapping necessary? Would it not be possible to train directly on the distribution? Section 4 is quite dense, and additional explanation for this mapping would help clarify the distributional reward model.

- Figure 1 disagreement analysis: The left plot for MultiPref seems to suggest a possible bias in the annotation interface, as there is a preference of annotators to prefer B annotations over A (non-symmetric matrix, skewed histogram, and darker areas in the upper-right corner). What is your explanation for this? The HelpSteer dataset does not seem to show a similar annotation behavior. I would like to hear your thought - it can be interesting to add this to the paper discussion. This also connects to my questions below on more information on the annotation setup. 

- Annotators of datasets: "MultiPref has 10k preference pairs with four annotators, HelpSteer2 has 12K with 3-5 different annotators." Can you say more about the identity of the annotators, are the four in MultiPre the same individuals? If not, how many individual annotators are there in both datasets? How many annotations on average did each annotator? Do you release annotator IDs? Did you collect any annotator social information? 

- Refusal vs Refusal: Can you provide more detail on the original annotation tasks? For example, were annotators instructed to take a forced choice? Or was a "I don't know" option allowed?

- Results in Table 4 LLMs-as-Judge: What are the scores in the table and what do they mean? Do they only compare to the majority preference ("winning response")? If so, I think it would be more interesting to compare to the human preference distribution. Thank you for clarifications. 

- What was the motivation of using a 8B LLama-instruct model? Were there restrictions to not use a larger model (70B?)? Would you expect similar findings with the larger model? Which exact Llama model was used? (As there exist by now several versions 3, 3.1, 3.2).

- Will you release the code for the distributional preference models and the trained reward models?

Overall, I like the paper a lot and I am willing to go up with my overall score. However, the results are dense and I have questions I would like to hear from the authors. I look forward to hear the answers to my questions above.

Typos:
- "singe-value" in several places

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
This paper leverages the MultiPref dataset and the HelpSteer2 dataset to study the behavior of RM/LLM-as-Judge in instances with diverging human preferences. They observe that traditional methods of training RMs (Bradley Terry or MSE-Regression) fail to make RMs that represent multi-preferences. Hence, they propose alternative methodologies, Mean-Variance Reward Models, and Classification-based Reward Models, to train RMs that learn the distribution of the responses instead of a singular value. The presented methodologies show about 10% improvement from past methods using AUROC as the metric.

### Strengths
1. While it is often intuitively accepted that RMs and LLM-as-Judges may exhibit biases and fail to reflect the diverse preferences of humans, this paper offers a systematic approach to identify and quantify these errors. Additionally, through a qualitative study, the paper provides a taxonomy to categorize the primary causes of preference divergence.

2. The paper goes beyond just pointing out the problem to present two training methodologies to train models that better represent diverging preferences. The two methods aim to model the preference distribution instead of singular values and achieve a 10% performance improvement. 

3. The writing is clear and easy to understand.

### Weaknesses
1. RMs and LLM-as-Judges are mostly integrated into training and evaluation pipelines as proxies for human preferences (they are rarely used alone). While the paper demonstrates that its proposed training methodologies improve RMs' ability to distinguish between instances with diverging preferences, it lacks discussion on the potential downstream impacts. Ultimately, can these new RMs create models better aligned with human preferences? Are they more effective evaluators for leaderboards that aim to reflect genuine human preferences?

2. The paper lacks experimental evidence in defining the problem. While I agree with the importance of developing smaller, high-quality RMs, recent studies have shown that scaling up RMs yields better evaluators. Does the issue of failing to detect diverging preferences persist even with larger RMs? If the issue goes away with scaling, probably it might not be an issue soon when better and cheaper hardware becomes available.

3. Section 5.1 highlights that  LLM-as-Judges also struggle to identify instances with multiple preferences. However, could this issue stem from the prompting approach? The referenced LLMs rely on straightforward prompting techniques for judgments, which do not inherently account for multi-preference scenarios. Could more sophisticated prompting methods or multiple sampling iterations help address this limitation?

### Questions
1. RMs and LLM-as-Judges are mostly integrated into training and evaluation pipelines as proxies for human preferences (they are rarely used alone). While the paper demonstrates that its proposed training methodologies improve RMs' ability to distinguish between instances with diverging preferences, it lacks discussion on the potential downstream impacts. Ultimately, can these new RMs create models better aligned with human preferences? Are they more effective evaluators for leaderboards that aim to reflect genuine human preferences?

2. The paper lacks experimental evidence in defining the problem. While I agree with the importance of developing smaller, high-quality RMs, recent studies have shown that scaling up RMs yields better evaluators. Does the issue of failing to detect diverging preferences persist even with larger RMs? If the issue goes away with scaling, probably it might not be an issue soon when better and cheaper hardware becomes available.

3. Section 5.1 highlights that  LLM-as-Judges also struggle to identify instances with multiple preferences. However, could this issue stem from the prompting approach? The referenced LLMs rely on straightforward prompting techniques for judgments, which do not inherently account for multi-preference scenarios. Could more sophisticated prompting methods or multiple sampling iterations help address this limitation?

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
This paper investigates the problem of diverging preference in human-labelled preference datasets.
They created a taxonomy of the disagreement sources and tested the RLHF reward model on disagreement data.
They showed that the reward model trained on majority vote would clearly prefer one of the responses when presented with examples with diverging preferences. 
The author further proposed a new reward model by predicting the mean and variance of the distribution reward. 
The proposed reward model achieves better performance in terms of distinguishing the diverging and non-diverging preference examples.

### Strengths
1. The problem of annotator disagreement is an important one as the current model training neglects the inherent difference between the annotators which could lead to misalignment of the model. The pluralistic alignment of the reward model in RLHF has great potential. 

2. The author not only reveals the misalignment of the reward models but also proposes a new training objective for it to mitigate the problem. Experimental results show that the reward model trained with a new objective can better identify the disagreement in the data.

### Weaknesses
One problem of the paper is that details about the implementation and motivation of experiment design are either missing or moved to the appendix. It makes the paper hard to follow. 
For example, it is not clear why the author split the level of disagreement by High-Agreement Prefs, High-Agreement Ties and so on.

1. Why do High-Agreement Prefs require no rejection of the majority vote, but the High-Agreement Ties allow it? 

2. In lines 319-323,  why is the mapping interval set like this? I believe the intervals could have a great influence on the reward model.

3. The CDF estimation is an important detail for training and evaluating the reward model, which I think should be discussed in the main text.

4. In line 348, I don't fully understand what you mean by "use the predicted joint probability of annotators labelling the response as a 1 or 5".

5. In line 361, "using smaller differences as a predictor" is not informative. What do "smaller differences" mean exactly?

### Questions
Please refer to the questions above.

### Soundness
3

### Presentation
2

### Contribution
3
