# T-Measure: A Measure for Model Transferabilty

- Decision: Reject
- Scores: 5, 3, 3, 3

## Abstract
A popular paradigm in AI modeling, including computer vision, natural language processing, and graph modeling, is applying a large pre-trained model that has been fine-tuned for a particular task on novel datasets. 
However, many such models are published in model repositories, fine-tuned using different types of source data.
Consequently, practitioners face the problem of model selection -- choosing the best model for their task from a repository of models. 
Model performance in a target domain depends on factors including task definition, model architecture, data distribution, and the model transfer method.
Previous model selection methods in transfer learning focus on task definition when assessing transferability, and often require a labeled dataset in the target domain.
We formulate the transfer problem as label-agnostic model selection, where the goal is to choose the best-performing model on a target domain without access to labeled data. 
Specifically, we analyze the impact of source domain training data on model transferability. 
To measure this transferability, we introduce a new type of quantitative measure, the T-Measure, which correlates with the test-time performance of a model on an unlabeled target domain.  
We propose a T-Measure estimation method which incorporates distributional measures of the source domain's training data instances, the distribution of the target domain's instances, and the base performance of a task-specific model to create a ranking of models.  
We then adapt previous task-centric transferability measures for data-centric selection and compare them against T-Measure.
We thoroughly evaluate the T-Measure performance for 4 tasks and 11 datasets and show its effectiveness in ranking models for model selection compared to baselines.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new metric for estimating model transferability in zero-shot transfer learning. The authors cast the problem as label-agnostic model selection, which aims to select the best model on a target dataset without annotations. The authors propose to learn a representation space aligned with each source dataset using contrastive learning on triplets which captures the dependency between data. Experiments on multiple tasks and datasets demonstrate the effectiveness of the proposed metric for model selection compared to other baselines.

### Strengths
1. The paper studies an important practical problem of model selection for transfer learning in the absence of labeled data.

2. The proposed data-centric transferability measure based on source/target dataset similarity is interesting.

3. T-measure shows consistent benefit over baselines on diverse tasks and datasets.

### Weaknesses
1. The proposed metric requires access to the source data. However, the source data may not always be available during fine-tuning, especially in scenarios where pre-trained models are distributed without their original training datasets, or when dealing with proprietary datasets. This limits the practical applicability of the method in real-world transfer learning scenarios.
2. The number of pre-trained models is quite limited. According to Table 3, the metric is only evaluated on 3 or 6 models. It remains unclear whether the metric can be extended to a large number of pre-trained models, and if the performance gains observed with a small set of models would generalize to a more diverse and larger pool of pre-trained models. The evaluation should include a more extensive set of models with varying architectures and training procedures to demonstrate the robustness of the metric.

### Questions
None

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a metric for measuring transferability score across datasets, called T-measure. The measure introduces a two step process to measure the transferability score - 1. selecting a subset similar to target dataset, 2. using PVI of datapoints and aggregating to measure the final score. Experiments are shown on different datasets, comparing with existing techniques, which demonstrate that the method performs better on average than competing scoring methods.

### Strengths
The model has been evaluated on different datasets, showing comparable or better performance than competing methods. The domain of testing includes classification, emotion recognition, question/answering, etc. Previous methods were focused on classification methods only.

### Weaknesses
The current draft of the paper has major weaknesses as listed below:

1. Equations are not numbered in the paper, which is lowering the readability of the paper. For example, equations in Section 2.1 and 2.2 are outputting \phi^* model, on the first read its not clear what is the difference between the two equations. Specifically, it is unclear how the transfer method \alpha is incorporated into the model selection process in equation 2.2. Similarly, in Section 3.2, PVI computation of data samples is not provided, hence the motivation for Step 2 is not clear from the draft. It is not clear how the PVI is calculated for a given data point and how this relates to the transferability. In the results section, Table 4 and 6 are referenced for results, but these tables are present in Appendix, not the main section of the paper. Not sure if it violates the page length limit in the conference.

2. The proposed method is an increment over the (Ethayarajh et al., 2021) which introduced V-Usabiltiy and Pointwise V-Information(PVI). The current paper aggregates the PVI over a subset of samples from source, which are similar to target. Are there other functions which can be considered for aggregation, can authors provide justifcation for selecting this particular method. Also, it is not clear how this applies for a generic transferred model (α(T, Dtrain_trg , ϕi)). The paper mentions that α is identity in Section 2.4, but its not clear otherwise. The paper lacks a clear explanation of how the transfer function α is applied in practice and how it interacts with the PVI aggregation. The choice of using a subset of source samples similar to the target is not sufficiently justified, and the potential impact of this selection on the final transferability score is not discussed.

3. In Table 3, it is not clear what average Kendell-tau distance signifies? There is no point averaging across datasets. Can authors specify if the model is outperforming other methods on individual datasets. Also, references for competing methods are not provided in the table. The paper should provide a breakdown of the Kendall-tau results for each dataset to allow for a more granular analysis. It is also important to understand how the proposed method compares to the baselines on individual datasets, rather than just an average.

### Questions
Weakness section has questions about the paper, which should be answered in the rebuttal.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
A new transfer metric is proposed to evaluate target task in zero-shot accuracy setting, when no target labels are available. The new measure estimates the closeness of the target dataset to various source datasets and chooses the model trained on the closest one. The pointwise mutual information metric is used to compute the closeness of the datasets, after learning a suitable representation space on the labeled source dataset. Results have been computed on various dataset settings for the tasks ranging from response selection, emotion recognition, question answering and relation classification.

### Strengths
- The paper addresses a very pertinent and important problem of model selection when no target labels are available during model selection (zero-shot model selection). 

- The explanation for various types of transfer is presented well in Sec 2.

### Weaknesses
 - This paper makes a key assumption that the source datasets is decomposable, which might not always be the case. Therefore, the generality of the approach to other datasets is not guaranteed, limiting its impact. Also, they assume that the source dataset is always available during model selection, which is generally not true if we consider the recent trend of foundation models where the source datasets are not available but only source models are released. Lastly, although a minor assumption, it might not always hold that the source and target tasks are same. For example, MLM (masked-langauge-modeling) has been shown to be universally applicable to many downstream tasks for few shot transfer.

- The paper, at its core, essentially evaluates which of the source dataset is the closest to a particular target dataset. In this sense, the authors must also include comparisons with several works in domain adaptation (DA) and robust optimization literature. For example, several measures like A-distance and H-divergence [1] also need to be included. In general, several works in UDA litearture need to be cited and discussed.

- It is really not clearly explained why triplet loss is chosen to learn a suitable representation space. Does the representation learnt using source labels work equally well? Can we also use contrastive loss with multiple negatives? This aspect should be studied in much greater detail.

- The paper states that they use Sentence-BERT for the initial representation. Does this effect the evaluation in any way? For example, does the dataset used to train Sentence-BERT change the ease of transfer to related target domains?

- I am curious to know why the authors chose to provide examples related to vision datasets and vision tasks (in Fig 2), while all the evaluation is done using NLP datastes. Even more so, Fig 1-4 are all really not explaining anything related to the problem or method, and could be improved to illustrate your idea better.

#### Minor

- Sec 3.2, Step1: Did you mean argmin in the equation?

- For completeness, PVI should be explained using an equation or such, since not all readers might be familiar with the term (I am not!).

### Questions
I feel the intuitions behind several choices in the paper could be presented better and the evaluation could be made more extensive by comparing with other measures of distance, representation learning methods and transfer settings. I request the authors to address my concerns above and I'd be happy to raise the rating.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses a pertinent challenge in the AI modeling domain, which is model selection for transfer learning. With numerous models available in repositories, each trained on different source data, determining the most appropriate model for a particular task becomes a significant challenge. The authors frame this selection issue as "label-agnostic model selection" - the idea of choosing an efficient model for a specific domain without access to labeled target data.

The main contribution is the introduction of the "T-Measure" as a quantitative tool to estimate the transferability of models based on their training data from the source domain. This measure assesses the transferability by evaluating distributional characteristics of the source domain's data, target domain's data, and the fundamental performance of a task-specific model. The measure aims to provide a ranking of models based on their potential performance on unlabeled target domains.

The authors also touch upon modifying existing task-centric measures to focus on the data, contrasting these against their T-Measure. Through experimental validation on 4 tasks and 11 datasets, they conclude that the T-Measure outperforms baselines in model ranking.

### Strengths
1. The idea is clearly stated in the paper, and it is easy to follow. The main idea is to compare the similarity of source data and target data.

2. The problem this paper explores is important, especially in these days where new models come out everyday.

3. The experiments focus on language data, a less explored data type in previous literature.

### Weaknesses
1. **Over-simplification of Transferability Factors**: The paper's approach to the complex problem of model transferability is overly reductive. As highlighted in Figure 2, there exists a multitude of factors that can significantly influence transfer performance. The paper seems to narrow its focus primarily on data, while ignoring other crucial aspects such as model architecture, pre-training objectives, and optimization strategies. The rationale behind this selective approach is not sufficiently justified. A comprehensive model transferability analysis should account for the interplay of multiple factors, and not just a singular dimension. For instance, the paper does not consider how different pre-training objectives (e.g., masked language modeling vs. next sentence prediction) might impact transferability, even when the source and target datasets are similar. This oversimplification limits the practical applicability of the proposed T-Measure.

2. **Unrealistic Experimental Setting**: The experimental setup employed in this study raises concerns about its applicability in real-world scenarios. Specifically, the paper assumes that models are trained, transferred, and assessed all within the confines of a single task. This is in stark contrast to common practice, where a pre-trained model, developed for one task, is often adapted to suit an entirely different task. For example, a model pre-trained on a large corpus of text for general language understanding is often fine-tuned for a specific task like sentiment analysis or question answering. Such a limitation restricts the practical utility of the proposed T-Measure, as it does not evaluate the measure's effectiveness in cross-task transfer scenarios.

3. **Opaque Methodological Details**: The paper's exposition on its methodology is not clear in details. For instance, while it uses self-supervised learning for data representation, there's a conspicuous absence of details regarding its implementation. Questions arise about how hyper-parameters for self-supervised learning were chosen, what specific self-supervised learning method was used (e.g., contrastive learning, autoencoding), and their potential impact on the study's outcomes. The sensitivity of the proposed measure to different self-supervised learning algorithms and training settings remains unclear. Furthermore, the paper does not specify the architecture of the self-supervised model used, making it difficult to reproduce the results. The lack of these details hinders the reproducibility and interpretability of the study.

4. **Lack of Rigor in Presentation and Design Choices**: The manuscript frequently resorts to phrases like "intuitively," which undermine the scientific rigor expected of such a study. Additionally, many design choices appear arbitrary, with little to no justification provided. This raises concerns about the robustness and generalizability of the study's conclusions. Specifically, it remains uncertain whether the paper's findings would remain consistent across changes in model architectures, tasks, transfer methods, or self-supervised learning techniques. For example, the choice of using a specific distance metric for comparing data distributions is not justified, and it's unclear how this choice affects the performance of the T-Measure. The paper needs to provide a more rigorous justification for its design choices and conduct sensitivity analyses to demonstrate the robustness of its findings.

### Questions
1. Can authors summarize and refine the contributions part? The "contribution" of the introduction seems to only summarize each section, not really "contribution".

2. It is not clear if this paper targets at domain adaptation or model fine-tuning. The paper mentions that it focuses on the case where source and target shares the same task, which is domain adaptation actually. If the paper further focuses on the case where Dtrg is not accessible during model selection, it is unsupervised domain adaptation I think. And if the paper deals with selecting source dataset, it is multi-source unsupervised domain adaptation. The literature papers it mentions like Bao et al., 2019; Nguyen et al., 2020; Tran et al., 2019 are all for fine-tuning. They have access to target labels, and they tried different ways to use the target labels. The authors should have a thorough literature review to put this paper into an appropriate position in the literature.

3. There are several incomplete sentences, which I would like the authors to clarify:

- "While some recent body of work sugguest that source dataset is an important factor in transfer: (Zhao et al., 2022) suggest that some datasets are intrinsically harder than others and (Ethayarajh et al., 2021) show that training datasets have different amount of useful information for trained models." in the introduction.
- "when the task, model architecture and transfer method are invariant in the transfer setting" after Figure 2.
- "6 presents boxplots of ranking performance" in Page 8. It should be "Figure 6" I think.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
