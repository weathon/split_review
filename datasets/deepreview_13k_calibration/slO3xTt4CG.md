# MetaMetrics: Calibrating Metrics for Generation Tasks Using Human Preferences

- Decision: Accept
- Avg Score: 6.20
- Scores: 6, 6, 6, 8, 5

## Abstract
Understanding the quality of a performance evaluation metric is crucial for ensuring that model outputs align with human preferences. However, it remains unclear how well each metric captures the diverse aspects of these preferences, as metrics often excel in one particular area but not across all dimensions. To address this, it is essential to systematically calibrate metrics to specific aspects of human preference, catering to the unique characteristics of each aspect. We introduce $\benchmarkname$, a calibrated meta-metric designed to evaluate generation tasks across different modalities in a supervised manner. $\benchmarkname$ optimizes the combination of existing metrics to enhance their alignment with human preferences. Our metric demonstrates flexibility and effectiveness in both language and vision downstream tasks, showing significant benefits across various multilingual and multi-domain scenarios. $\benchmarkname$ aligns closely with human preferences and is highly extendable and easily integrable into any application. This makes $\benchmarkname$ a powerful tool for improving the evaluation of generation tasks, ensuring that metrics are more representative of human judgment across diverse contexts.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed a method to align the automatic evaluation metrics with human preference evaluation, called MetaMetrics. Specifically, it's optimized to learn a set of weights that can combine automatic metrics to mimic human preference. Two methods are discussed and experimented for the optimization. The experiments cover both text and multimodal evaluation, demonstrating a satisfactory performance of the proposed method.

### Strengths
1. The research problem this paper studied is very interesting and useful. Automatic evaluation metrics can cover a wide range of benchmarks. However, they may not align with human evaluation. Given human evaluation is time-consuming and expensive, and also current model is required to be more generalizable to various tasks, aligning the automatic metrics with human evaluation preference becomes an urgent and important research topic.

2. This paper illustrates the motivation, problem definition, and methods to optimize the proposed MetaMetrics in a clear and easy-to-follow way.

3. The experiments are conducted in a wide range of downstream tasks, from text to multimodal, as well as training a reward model.

### Weaknesses
1. This paper assumes that human preference can be approximated by a weighted combination of metric scores. But it seems to be too simple, and might not always hold. For example, human's evaluation of helpfulness might require both the model to perform well in reasoning and knowledge-retrieving, which we assume are separately measured by two benchmarks. Then a weighted summation of these two benchmarks might not be suitable, instead, a multiplication might be more proper.

### Questions
See weaknesses.

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
3

### Summary
This paper introduces MetaMetrics, a framework designed to calibrate evaluation metrics to better align with human preferences. By leveraging existing metrics that capture different aspects of human preferences, MetaMetrics employs learning-based methods to optimize these metrics for various generative tasks. To demonstrate the effectiveness of MetaMetrics in aligning with human preferences, the authors compute correlations between the calibrated metrics and quantified human ratings. Experiments are conducted across diverse tasks, including Text Summarization, Machine Translation, Question Answering, Image Captioning, and Reward Model Scoring.

### Strengths
- The paper addresses a critical problem in the field of text generation: the lack of automatic metrics that accurately reflect human preferences. Current approaches often rely heavily on human annotations to evaluate performance. By proposing a method to calibrate existing metrics to align with human preferences, this work aims to reduce the reliance on labor-intensive human evaluation processes.

- The methodology is simple yet effective. The proposed approach captures the multifaceted nature of human preferences while incurring minimal additional cost, enabling efficient calibration of existing metrics.

- Extensive experiments validate the proposed method. The authors conduct experiments across a variety of tasks, including Text Summarization, Machine Translation, Question Answering, Image Captioning, and Reward Model Scoring. This demonstrates the task-agnostic advantages of the method and its broad applicability.

### Weaknesses
 - Empirical and ad hoc nature of MetaMetrics: The calibration process for MetaMetrics relies on empirical and ad hoc weighting of existing metrics for each dataset and human preference. These weights are highly dependent on the specific dataset and task, which raises concerns about their generalizability to a broader range of datasets or tasks.

- Lack of ensembled baselines: While the paper compares MetaMetrics against individual metrics, it does not include ensembled baselines, such as averaged or weighted-average scores of individual metrics. Including these as baselines would provide a fairer comparison and strengthen the evaluation.

- Absence of human studies in experiments: Although MetaMetrics aims to align with human preferences in evaluating model performance, the study does not involve an actual model being evaluated and analyzed through human studies. To comprehensively validate MetaMetrics, experiments involving direct human evaluation of model outputs are necessary.

- Unclear human preference in certain tasks: In some evaluation tasks, the connection between the ratings and human preferences is not adequately explained. For instance, it is unclear how ratings like sys Pearson, seg Pearson, and acc-t in Machine Translation tasks, or NQ, TQ, NarrativeQA, and SemEval in Question Answering tasks, align with human preferences. More detailed explanations of these ratings and their relationship to human preferences are needed, especially for readers unfamiliar with these tasks.

- High computational cost for reward model ensembling: The use of multiple metrics in MetaMetrics can significantly increase evaluation costs, particularly in reward model scoring. For example, in online RLHF training, simultaneously running multiple reward models (e.g., 7 models in Table 4) could make the process computationally infeasible.

### Questions
See weaknesses.

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
This paper introduces meta-metrics, which optimizes the combination of existing metrics to enhance their alignment with human preference. The paper investigated mainly two method GP and XGBoost to try to learn a best weight vector for a set of base metrics to combine. For different datasets, they select different base metrics and train a new weight vector for combinations. Results show that meta-metrics can outperform existing baseline metrics in summarization, translation, question answering, image captioning and reward modeling scenarios.

### Strengths
1. This paper proposes a new paradigm to ensemble existing metrics for evaluation of different tasks, learning a weight vector through GP or XGBoost and get the weighted combination of base metrics. This is a novel approach and gets good performance.
2. The paper is well-motivated and clearly written, with nice figures and tables illustrating the concepts.
3. Extensive experiments across summarization, machine translation, QA, reward modeling, which covered a wide areas. The authors also provide analysis of the weights distribution across the base metrics. Providing many insights.

### Weaknesses
1. The performance gain is relatively small compared to base metrics, especially for machine translation and reward modeling tasks, it's unclear whether these marginal performance gains are worth the training cost.
2. The proposed approach requires training a new combination weight vector once the base metrics have changed, thus limiting the usability of the approach.

### Questions
1. Please provide the training details. From my understanding, when training a combined metametric for reward modeling, you need to run inference on all of the training data using each of the base metrics first, and then train your weight vector to optimize for the human preference. How much GPU hours have you spent on the inference, and the training? How many GPUs did you use for the experiments?
2. Could you provide a list of base metrics used for each meta-metric variant in one place? I only found the base metrics for reward modeling  in line 474 and it's unclear what's the base metrics used for other benchmarks. if they are also baselines, it's better to mark them in the results table.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces Meta-Metrics, a calibrated metric for evaluating generation tasks like summarization, QA, Machine Translation and Image Captioning,etc. It raises the issue of metrics excelling at one dimension and falling at others while evaluating on multiple dimensions (like coherence, fluency, relevance,etc in summeval), hence proposing a calibrated metric based on these several metrics, aiming to achieve a higher alignment with human preferences in the evaluation scores. The authors propose using methods like Bayesian Optimization, Boosting to effectively choose/filter the various metrics and give a combined metric to have higher correlation with human scores.

### Strengths
1. The paper presents innovative mathematical approaches of using BO modeled as Gaussian Process, and XG Boosting on existing metrics to create a new metric.
2. The paper has tested their method extensively on several datasets across multiple domains.

### Weaknesses
1. Although the metametrics have shown they have higher alignment with human preferences, the optimization methods (BO and Boosting) are to be considered black boxes and offer very less explainability.  Understanding how these methods find the combination of metrics and interactions between different metrics within the model is not possible. Hence explanation on why they correlate more with human scores is not there.



### Questions
1. It is very good that the authors have shown their method on multiple datasets, but some more experiments/analysis on the proposed methods would strengthen the paper more. One such thing can be, the authors used Kendall-Tau as the objective calibration function. How were the results when spearman correlation is used as a calibration function?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a novel evaluation metric, MetaMetric, designed to better align with human preferences. The proposed metric is a weighted combination of existing metrics, where the weights are learned in a supervised manner. The authors demonstrate the effectiveness of MetaMetric through experiments on various natural language generation tasks, e.g., summarization, translation, question answering and image captioning. Additionally, they show that this metric can be useful for reward model scoring. They also provide some analysis about interpretability and efficiency of their metric.

### Strengths
1. The experiments are comprehensive, including various types of natural language generation tasks.
2. The topic of developing a human-aligned evaluation metric for NLP generation tasks is a long-discussed but unsolved challenge. This paper explores a possibility to push forward in this direction.
3. The proposed metric is easily extendable to other tasks where preliminary metrics have already existed. This extensibility makes the metric potentially applicable to a broader range of applications.

### Weaknesses
I have several concerns regarding the experiments, particularly the scope of the problem and the evaluation settings, and how they support the authors' claims. Additionally, the presentation of the paper requires refinement.
1. **Limited Contribution:** The paper's contribution appears limited. It essentially addresses a traditional supervised learning problem with input of small dimensions and output with single normalized value. The authors train a regression model on supervised-learning datasets, using conventional metrics as inputs and human preference values as outputs. The experimental results involve testing this regression model on the test set of these datasets and comparing different metrics using correlation of the rankings of metrics with ground truth human preference values. It is unsurprising that MetaMetric outperforms other metrics in the in-domain generalization setting, which is the primary focus of this paper. The authors should also clearly present their experimental settings, such as how they create the training, validation and testing sets. For example, the setting for Question Answering tasks is not clear. It would be interesting to add more OOD and real scenarios to test this metric. See following comments for detailed feedback.
2.  **Lack of Out-of-domain (OOD) Generalization Evaluation:** The authors should place more emphasis on the OOD setting, as human preference data is not always available. I found only one one OOD setting presented in Figure 3. Based on in-domain performance, the GP model works the best. However, the GP model performs similarly to CLIP-S and METEOR in the OOD setting. (The statement about the superiority of MetaMetric-Cap over any other individual metric, in lines 426 and 427, is misleading.) This suggests that the use cases for the trained metric are limited, and its performance may be worse than using a single conventional metric. It would also be interesting to evaluate metaMetric trained on one task but tested on another, which is a more challenging OOD setting than the one in Figure 3.
3. **Lack of Evaluation in Real Settings:** The evaluations are limited by the training datasets with human-annotated preference values. It is unclear whether this metric is useful for real applications, as suggested by the authors in lines 41 and 42. For example, the authors could follow a similar evaluation procedure to DPO and PPO papers, using the proposed metric to evaluate various LLMs - before and after RLHF-tuned - and compare their win rates based on MetaMetric.
4. **Reference-based and Reference-free Settings:** In line 83, the authors claim to design the metric for two settings: reference-based and reference-free. If I understand correctly, this depends on the choice of metrics rather than the model design. If the chosen metrics require references, then MetaMetric can only be reference-based. In the experiments, the authors only distinguish these two settings for Machine Translation, not for other tasks. It would be better that the authors add both settings for all the tasks.
5. **Presentation Issues:** The paper's presentation is suboptimal. Major issues include:
    1. The caption of a table should be placed above it.
    2. Figure 2 is not cited anywhere in the paper.
    3. The authors cite a table in the Appendix as crucial support for their claims (see line 357 for Table 9). The authors should put the information in the main text.
    4. Other minor issues are listed in the Questions section.

### Questions
1. **Questions related to Introduction Section:**
    1. The first paragraph is a bit confusing. The authors discuss the shortcomings of BLEU and BERTScore in the main text, but Figure 1 presents BLEU and CLIP-S. Additionally, what criteria are used in Figure 1 to determine if a metric is good or not? For the figure on the right hand side, why are BLEU 0.2 and MeMetric 0.4 considered good, but CLIP-S 0.6 is considered bad? What is the threshold?
    2. The authors state, "models that optimize for human preference ... have demonstrated superior performance." What metrics have these models used to demonstrate human alignment? The authors avoid discussing this in their paper, instead comparing their metric with conventional metrics not originally designed for human preference alignment. For example, Ouyang et al. [1] used the Perspective AI score to measure toxicity.
    3. In line 42, the authors mention "evaluation metrics that accurately reflect human subjective judgements." Since human judgements are **subjective**, is it possible that a metric can **accurately** measure these varied judgements across different individuals?
    4. In line 53, the statement relating the necessity of human aligned metrics to the complexity of tasks seems implausible. Regardless of task complexity, we always seek metrics that align with human evaluations.
2. **Universality of MetaMetric:** For conventional metrics (e.g., BLEU, ROUGE, METEOR), they are used across various natural language generation tasks. Is it feasible to have a single MetaMetric applicable to all natural language generation tasks?
3. **Choice of Training Methods:** Why did the authors choose Bayesian Optimization and Boosting to train MetaMetrics? Is it possible to use linear regression models with regularizations?
4. **Efficiency of MetaMetric:**. According to Figure 4, MetaMetric requires about 8 metrics for computation. Can the authors explain why computing approximately 8 metrics is still considered efficient?
5. **Interpretability:** Can the authors explain why some metrics align more closely with human evaluations while others do not? I'm curious whether there is any intuition behind this.
6. **Compute Efficiency for RM:** In lines 433 and 472, Table 4 does not show compute efficiency. The authors should include the model size for MetaMetrics-RM.

[1] Ouyang, Long, et al. "Training language models to follow instructions with human feedback." Advances in neural information processing systems 35 (2022): 27730-27744.

**Minor Issues:**
1. In line 215, there is a duplicate "is"
2. Presentation suggestion: Section 2 could be merged with Section 7.

### Soundness
2

### Presentation
2

### Contribution
2
