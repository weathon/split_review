# RecFlow: An Industrial Full Flow Recommendation Dataset

- Decision: Accept
- Scores: 6, 5, 8, 6

## Abstract
Industrial recommendation systems (RS) rely on the multi-stage pipeline to balance effectiveness and efficiency when delivering items from a vast corpus to users. Existing RS benchmark datasets primarily focus on the exposure space, where novel RS algorithms are trained and evaluated. However, when these algorithms transition to real-world industrial RS, they face a critical challenge: handling unexposed items—a significantly larger space than the exposed one. This discrepancy profoundly impacts their practical performance. Additionally, these algorithms often overlook the intricate interplay between multiple RS stages, resulting in suboptimal overall system performance. To address this issue, we introduce RecFlow—an industrial full-flow recommendation dataset designed to bridge the gap between offline RS benchmarks and the real online environment. Unlike existing datasets, RecFlow includes samples not only from the exposure space but also unexposed items filtered at each stage of the RS funnel. Our dataset comprises 38M interactions from 42K users across nearly 9M items with additional 1.9B stage samples collected from 9.3M online requests over 37 days and spanning 6 stages. Leveraging the RecFlow dataset, we conduct courageous exploration experiments, showcasing its potential in designing new algorithms to enhance effectiveness by incorporating stage-specific samples. Some of these algorithms have already been deployed online, consistently yielding significant gains. We propose RecFlow as the first comprehensive benchmark dataset for the RS community, supporting research on designing algorithms at any stage, study of selection bias, debiased algorithms, multi-stage consistency and optimality, multi-task recommendation, and user behavior modeling. The dataset is licensed under CC-BY-NC-SA-4.0 International License.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper first proposes a full-flow recommendation dataset collected from the industrial video recommendation scenarios. The overall process includes retrieval, pre-ranking, coarse ranking, ranking, re-ranking, and edge ranking. The logs are collected from January 13 to February 18, 2024. The datasets can be accessed via a half-anonymized link that denotes the authors' institute.

### Strengths
1. The proposed full-flow dataset provides a strong groundwork for follow-up research. For example, models can learn how to alleviate selection bias due to the discrepancy between the training and inference stages.
2. The authors performed comprehensive experiments and presented the results of the experiments with means and variances.
3. The complete datasets are available for further research.

### Weaknesses
1. The paper's current presentation lacks clarity and coherence, making it difficult to follow. Additionally, there are numerous minor grammatical and structural errors throughout the text.
2. While the initial explosion stage involves large-scale data, the subsequent re-ranking and edge-ranking stages utilize significantly smaller datasets. This inconsistency undermines the paper's claim of working with large-scale industrial data. Specifically, the paper does not provide sufficient justification for the drastic reduction in data volume across the different stages, raising concerns about the representativeness of the later stages.
3. The paper's novelty is not effectively demonstrated through comparative analysis with existing work. Particularly in the introduction, while the authors enumerate the merits of the RecFlow dataset, they fail to provide meaningful comparisons with related work. The innovation of this research can only be discerned through prior knowledge of the field rather than through the authors' presentation.

### Questions
1. Regarding the ten merits presented in the introduction, it remains unclear which characteristics are unique to the RecFlow dataset compared to existing benchmarks.
2. As in line 143, what is the rationale behind the number of videos selected for each stage?
3. Also, can you explain why you chose 200 negative samples for each positive?
4. Some typos in the paper; for example, in line 379, recall 100 happens twice. This error occurs lots of times.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper mainly focuses on introducing a dataset, RecFlow. This dataset contains full-flow recommendation data, including retrieval, pre-rank, coarse ranking, ranking, re-ranking, and edge ranking. Containing two periods, the datasets provide an opportunity to study full-stage recommendations in industry. The full-stage recommendation is widespread in industry recommendations and is supposed to be investigated. Some experiments are conducted to give examples of how to utilize this dataset.

### Strengths
1. An essential and practical problem in real industry recommendation. The full-stage recommendation is widespread in the industry; this dataset really provides a new perspective on this problem.

2. The collection strategy is provided, and privacy protection is carefully considered.

3. Experiments are provided to show how to use this dataset.

### Weaknesses
1. Despite providing collection and analysis, the collection procedure should be provided in more detail to show that it is reasonable and correct. Moreover, the analysis is too simple, and more intuition about this dataset can be given.

2. The experiments provided to show how to use this dataset are interesting. However, in line 079, the author argues that Recflow can provide merits of ten tasks. It should be supposed that the experiments on these tasks should be provided.

3. There are some typos. For example, Line 314 Recall@100,500,100 should be 1000. The whole paper should be proofread.

### Questions
1. Actually, the samples in every stage are based on the filtered strategy in the previous stage. So, will this strategy bring bias? And if we use a different strategy, can the conclusion still hold? For example, in industry, from retrieval to pre-ranking usually consists of several strategies. How does this benchmark reflect this?

2. Are the results from Table 4 to Table 7 reproducible?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents RecFlow, an industrial-scale recommendation dataset that captures the full recommendation pipeline with multiple stages, featuring 38M user interactions and 1.9B samples collected from 42K users and 9M items over a span of 37 days. One of RecFlow’s innovations is its inclusion of unexposed items at each pipeline stage, allowing for important analysis of distribution shifts between training and serving environments. The dataset also supports multi-task recommendation and behavior modeling by capturing various user feedback signals.

Experiments show that modeling stage-specific interactions and addressing distribution shift with RecFlow data improves recommendation performance, with some methods proving effective in real-world systems.

### Strengths
1. The paper presents the first comprehensive large-scale dataset that captures the complete recommendation pipeline, filling a critical gap in the field where existing datasets only contain exposure data. It could enable further research into real-world problems that were previously difficult to study, eg: distribution shift, stage interaction effects.
2. Good motivation is provided by clearly articulating the limitations of existing datasets and the importance of studying full recommendation pipelines.
3. The dataset is well documented with clear descriptions of features, collection methodology and privacy protection measures. The privacy protection approach is also robust, using a combination of user consent, feature anonymization and careful data filtering.
4. Experimental validation is thorough with multiple runs, standard deviation reporting and comprehensive ablation studies across different stages.

### Weaknesses
1. The paper doesn't adequately address the computational challenges of working with such a large dataset. Details about storage requirements and recommended sampling strategies would be valuable for practitioners. Specifically, the paper lacks discussion on how the dataset's size impacts training time for different model architectures, and whether specific data partitioning or distributed training strategies are necessary for efficient experimentation. Furthermore, the paper should provide guidance on how to effectively subsample the data for preliminary experiments or for resource-constrained environments, including the potential impact of different sampling techniques on the representativeness of the data.
2. The multi-task learning potential of the dataset is mentioned but not thoroughly explored. Given the rich set of user feedback signals, this seems like a missed opportunity. The paper should have included a more detailed analysis of the correlations between different feedback signals and how these correlations could be exploited for multi-task learning. It would also be beneficial to see experiments with various multi-task learning architectures, beyond just mentioning the possibility of such experiments, and to discuss the challenges and potential benefits of this approach in the context of the RecFlow dataset.
3. While the authors mention online A/B testing validation, the details are sparse. More information about the production deployment and real-world performance would strengthen the paper's practical impact claims. The paper should provide details on the specific A/B testing methodology used, including the control group, the experimental group, and the metrics used to evaluate performance. Furthermore, it should discuss the statistical significance of the results and the potential confounding factors that might have influenced the online experiments. A more detailed discussion of the practical challenges encountered during deployment would also be valuable.
4. Analysis of how the stage samples could help with cold-start recommendations problem could be a useful contribution. Specifically, the paper should explore how the unexposed items at each stage can be leveraged to improve recommendations for new users or items. The paper could include experiments that compare different cold-start strategies using the stage samples and analyze the effectiveness of these strategies in terms of both accuracy and diversity of recommendations.

### Questions
1. What measures did you take to ensure the dataset is representative?
2. How can the dataset help handling cold-start users/items better?
3. Could you please provide more details on the online A/B testing setup and results?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper published a new dataset for multi-stage-funnel-based recommendation system, where the key difference from existing datasets is the inclusion of unexposed samples. Most existing datasets only contain samples that are exposed to users, and ranking and earlier-stage models are typically trained on exposed samples with user feedback. So inclusion of unexposed samples can facilitate research for many interesting problems in multi-stage recommendation, such as the distribution gap between training and serving, multi-stage consistency etc.

### Strengths
As far as I know, this is a first contribution of benchmark datasets that includes multi-stage and unexposed samples. Could be useful for researching important problems in multi-stage recommendation systems.

### Weaknesses
The evaluation criterion for the quality of a benchmark dataset for industrial recommendation system should be fidelity to an actual online recommendation system. For example, if researchers come up with new algorithms with metrics improvement using this dataset, then when it’s deployed to a real online system, such improvement can be validated. So it would be great if the authors can demonstrate such fidelity to some extent, e.g., by running online A/B test to compare the online performance and offline metrics to see the correlation. 

The rules for determining how many samples for each stage seem quite ad-hoc w/o explanation of considerations. Could you explain the considerations that went into determining the number of samples collected at each stage? Are these numbers representative of typical production systems?

some typos: 
line 239: datatse -> dataset
line 256: quote in wrong direction 
line 296/399: 1e-1/1e-2 not well formatted 
line 308/361: randomly sampling -> randomly sampled

### Questions
what’s the rationale for partitioning the data collection into two periods? Understanding the rationale for partitioning the data collection into two periods would help readers assess the dataset's representativeness and potential use cases. Could you explain the reasoning behind this decision and discuss any differences between the two periods that researchers should be aware of?

do you also log content features for the items? content features such as text/image/video/etc. content description (e.g., metadata, or embedding representations etc.) can be very useful features for recommendation.

### Soundness
3

### Presentation
3

### Contribution
3
