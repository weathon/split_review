# Automatic Combination of Sample Selection Strategies for Few-Shot Learning

- Decision: Reject
- Scores: 5, 5, 6, 5, 6

## Abstract
In few-shot learning, such as meta-learning, few-shot fine-tuning or in-context learning, the limited number of samples used to train a model have a significant impact on the overall success. Although a large number of sample selection strategies exist, their impact on the performance of few-shot learning is not extensively known, as most of them have been so far evaluated in typical supervised settings only. In this paper, we thoroughly investigate the impact of 20 sample selection strategies on the performance of 5 few-shot learning approaches over 8 image and 6 text datasets. In addition, we propose a new method for automatic combination of sample selection strategies (ACSESS) that leverages the strengths and complementary information of the individual strategies. The experimental results show that our method consistently outperforms the individual selection strategies, as well as the recently proposed method for selecting support examples for in-context learning. We also show a strong modality, dataset and approach dependence for the majority of strategies as well as their dependence on the number of shots -- demonstrating that the sample selection strategies play a significant role for lower number of shots, but regresses to random selection at higher number of shots.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores 20 sample selection strategies in few-shot learning, introducing the Automatic Combination of Sample Selection Strategies (ACSESS) method. ACSESS consistently outperforms individual strategies across five approaches using 8 image and 6 text datasets. The findings highlight the importance of modality and dataset characteristics, demonstrating that effective selection enhances performance, particularly in imbalanced and noisy datasets. Notably, the strategies are more beneficial with fewer shots, often reverting to random selection with larger numbers of shots.

### Strengths
1. Performance Improvement through Strategic Selection: The proposed ACSESS method effectively combines various sample selection strategies, leading to consistently better performance in few-shot learning tasks. This combination enhances the overall effectiveness of sample selection, particularly in imbalanced datasets with noisy samples.
2. Emphasis on Learnability: The study reveals that the learnability of samples is more critical than their informativeness or representativeness for the success of few-shot learning. 
3. Cost Reduction and Efficiency: Selecting a subset of samples rather than using full-shot training reduces computational costs while improving performance, especially on imbalanced and noisy datasets. The findings indicate that even in scenarios with limited available samples per class, curated selections can still yield benefits in performance and efficiency.

### Weaknesses
1. Although this paper conducts thorough experiments, it appears to lack significant insights into sample selection strategies and seems to be merely a combination of existing approaches.
2. Many key points in the paper are not clearly articulated, such as how the proposed ACSESS utilizes weighted strategies and active learning, which require further clarification.
3. Table 1 categorizes the comparison strategies into three major groups. However, the classification of strategies presented in Table 2 appears inconsistent with that in Table 1, which may lead to confusion. Furthermore, additional updated comparison strategies are needed to demonstrate the effectiveness of the proposed method.

### Questions
Please refer to weakness.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces ACSESS, an Automatic Combination of Sample Selection Strategies aimed at enhancing few-shot learning by combining diverse sample selection strategies. The paper evaluates 20 sample selection strategies across multiple few-shot learning frameworks, including meta-learning and in-context learning, using datasets from both image and text domains. ACSESS leverages several selection properties (informativeness, representativeness, and learnability) and proposes a scoring mechanism that improves the quality of selected samples by assigning weights to different strategies. This approach demonstrates consistent performance gains, especially in settings with imbalanced or noisy datasets.

### Strengths
1.	This paper presents an extensive comparison of 20 sample selection strategies, highlighting each strategy’s strengths and limitations across different few-shot learning contexts. This analysis supports the validation of ACSESS’s effectiveness over traditional single-property strategies.
2.	The approach incorporates a diverse set of datasets, spanning both image and text domains, and evaluates multiple few-shot learning methods, including meta-learning and in-context learning.

### Weaknesses
1. **Unclear differentiation from existing mechanisms**: The proposed forward and backward selection mechanisms lack a clear distinction from existing methods. The paper does not sufficiently emphasize how these mechanisms differ from conventional techniques or why they are particularly well-suited to the ACSESS framework. The paper could benefit from providing clear formulas or pseudocode to highlight the differences from recent related work (e.g., L149, L151), which would help readers better understand the distinction. Specifically, the paper needs to clarify how its iterative selection process differs from standard greedy feature selection or boosting techniques, which also combine multiple models or features sequentially. The current description does not provide enough detail to understand the unique aspects of the proposed approach compared to these well-established methods.

2. **Lack of detailed methodological steps**: Although the approach resembles an ensemble method that combines multiple strategies, the methodology section does not clearly outline the specific steps required to implement this combination. This lack of detail may challenge readers attempting to reproduce or apply the method. For example, providing clear algorithmic steps or expressing them through formulas would help avoid ambiguities and facilitate verification of the method on recent related works. Additionally, if relevant experiments are available, presenting them would enhance the manuscript’s credibility. The paper should explicitly define how the weights for each strategy are determined and updated during the selection process. Without this, it's unclear how the method avoids overfitting to the validation set or how it ensures a robust combination of strategies.

3. **Limited explanation of integration across strategies and datasets**: While the paper examines the impact of combining various strategies across datasets, it does not provide a structured explanation of how these combinations are optimized. A clearer flowchart for integrating diverse strategies with datasets would enhance the presentation. The manuscript could provide a specific example to illustrate the clear operational flowchart and pseudocode, further clarifying the execution process of ACSESS. The paper needs to detail how the selection process adapts to different dataset characteristics, such as varying levels of noise or class imbalance. It is unclear if the same combination of strategies is used across all datasets or if there is a mechanism for adapting the strategy combination based on dataset properties.

4. **Insufficient theoretical support for strategy selection**: Although extensive experiments empirically validate the method, the paper lacks a theoretical basis for favoring certain strategies. Greater theoretical justification could strengthen the feasibility and applicability of ACSESS, as relying solely on experimental results may limit the method’s perceived robustness. The paper should provide a theoretical analysis of why the chosen properties (informativeness, representativeness, and learnability) are effective for few-shot learning. Without a theoretical foundation, it is difficult to understand the generalizability of the method and its potential limitations in different scenarios.

### Questions
1. How does the proposed forward and backward selection in ACSESS differ fundamentally from existing selection mechanisms, and what distinct advantages does it bring?
2. Could the paper provide a clearer step-by-step explanation of how different strategies are combined within ACSESS?
3. What specific methods or frameworks were considered to determine the optimal combination of strategies and datasets, and how was this integration logically structured?
4. What theoretical considerations underpin the strategy selection in ACSESS, and how might the absence of theoretical support affect the method’s generalizability across diverse datasets and tasks?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The article addresses the uncertainty of the impact of sample selection on few-shot learning by:
(1) Broadly investigating the effects of single-property sample selection strategies used in previous work across three approaches: image classification and text classification in few-shot learning, and context-based text classification on extensive datasets.
(2) Proposing Automatic Combination of Sample Selection Strategies (ACSESS) method, which combines multiple complementary attributes in sample selection. The method employs the intersection of Forward Selection, Backward Selection, and Datamodels Selection schemes, assigning scores to samples through a weighted approach. Experimental results show that ACSESS has a sustained impact on performance, indicating that learnability is the highest-priority metric in few-shot learning.
(3) Further exploring the effects of sample quantity, sample quality (including noisy samples), dataset size, and sample selection strategies.
Overall, this paper provides a comprehensive analysis of the influence of sample selection strategies on few-shot learning and creatively introduces the ACSESS method, a strategic combination to overcome the limitations of single-attribute selection. The paper is supported by extensive experimental data and conclusive findings, making it a thorough and innovative contribution to sample selection strategies.

### Strengths
1. The article systematically evaluates the performance of single-property sample selection strategies and introduces a novel sample selection strategy—ACSESS. This strategy aims to combine multiple single-property strategies, optimizing the selected samples through a balanced weighting scheme to overcome the limitations of single-attribute selection, significantly enhancing the performance of few-shot learning under extreme sample conditions. 
2. The paper provides extensive experimental data, covering nearly all existing sample selection strategies, and evaluates their effectiveness in few-shot learning tasks across text classification, image classification, and context-based text classification. 
3. The ACSESS method innovatively proposes a scheme for autonomously combining strategy sets, building on previous research and addressing prior strategy limitations, with potential to advance future few-shot learning studies.
4. The article’s structure is clear, with numerous bolded sections to enhance readability and summary for researchers. However, the frequent use of bolding may sometimes detract from the clarity of key points, and it would be beneficial to use bolding more selectively.

### Weaknesses
1.Considering that the paper finalizes the relevant selection strategies by taking the intersection of three selection methods (Forward Selection, Backward Selection, Datamodels Selection), does this combined approach demonstrate a performance advantage over using single-strategy methods? It is unclear if the intersection of these methods consistently yields better results than any of the individual methods alone, especially given the computational overhead of running multiple selection processes.
2.The paper evaluates three independent weighting schemes. Are there other feasible weighting schemes beyond these three? Alternatively, could an adaptive mechanism be introduced to adjust these weights based on the characteristics of the dataset? Further explanation on this aspect would aid in understanding the flexibility and effectiveness of the ACSESS approach. The current weighting schemes seem somewhat arbitrary, and it's not clear why these specific schemes were chosen over others, or if they are optimal.
3.While ACSESS demonstrates excellent performance in text and image classification tasks, could this method also be applied to other few-shot learning scenarios, such as more challenging tasks like object detection, semantic segmentation, or depth estimation? The paper does not discuss the potential limitations of applying ACSESS to tasks with different data modalities or more complex output spaces, which could impact its general applicability.

### Questions
see the weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Samples are important in few-shot learning (FSL), meta-learning and in-context learning (ICL), especially in noisy environment. Sample selection picks informative, easily-learned or representative examples, probably improve performance of FSL or meta-learning or ICL when compared to typical supervised settings. However, the impact of sample selection is not well-studied in few-shot scenario. 

This work managed to justify the impact of different sample selection strategies. It showcases that the effectiveness of each sample selection strategies depends on data modality, dataset characteristics and models. To facilitate sample selection for FSL, in this work authors propose a method to identify a subset of well-performing strategies and combine those chosen ones for learning. 

Three types of  sample selection strategy identification are investigated, including forward selection, backward selection and "datamodels" selection. The obtained three subsets of sample selection strategies are intersected to get the final set of strategies. Then, a weighting scheme is utilized to assign different weight to each strategy for sample selection. 

With the proposed sample selection method by automatically combining different sample selection strategies, this work witnesses promising results on different tasks.

### Strengths
The work is well-motivated, the literature is well reviewed, and a reasonable and promising method for combing different sample selection strategies for learning is proposed.

The idea of learning a regression model to derive weights for each strategy, by learning upon a small number of random combinations of strategies, is interesting.

### Weaknesses
My concerns are as follows:
1) **Novelty**: The work uses off-the-shelf sample selection strategies, proposing a strategy to leverage these sample selection strategies for model learning. The integration of existing strategies into a unified pipeline easily distracts my attention away from its main contribution (Note I know it is the automatic combination of sample selection strategies).

2) **Clarity**: Though I know the overall framework of the proposed ACSESS, it remains ambiguous for me how sample selection works within FSL, for instance in the classic 5w-5s few-shot image classification. And, it is unclear how to efficiently measure the contribution of each strategy, especially when several strategies are combined. How exactly does the sample selection operate in the meta-learning procedure? How do we generalize or use ACSESS in a new task from a new dataset? 

3) **Efficiency**: As said, the optimal combination of sample selection strategies depends on data modality, dataset characteristic (eg. size, #categories) and model. It means we have no idea of which sample selection is better for a new dataset, model, nor do we know which combination of sample selection strategies boost the performance most unless searching for the optimal one. This is computational inefficient.  How can we intuitively and quickly identify a subset of sample selection strategies when encountering a new dataset or model?

### Questions
The studied topic is useful and meaningful. But the details can hardly be elaborated in limited pages. Illustrative examples are missing which impedes understanding. I think this work would be a great fit for journals like TPAMI after meticulous reorganization.

For questions, plz refer to the weaknesses.

### Soundness
3

### Presentation
2

### Contribution
4

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This thesis focuses on proposing a method that identifies a subset of relevant strategies that can improve the overall success rate of few-shot learning. The identified strategies are then weighted according to their expected contribution, and the identified strategies are combined to identify the most informative, highest quality samples that provide the greatest benefit.

### Strengths
The conclusions obtained through a large number of experimental validations provide a valuable reference for research teams with limited resources, which can effectively reduce the cost of trial and error and accelerate the research process.

### Weaknesses
1. What model is used for the backbone of this article (e.g., whether it is a CNN or a Transformer), and the characteristics of the different architectures can have an impact on the model performance. Most classical methods are usually proposed without pre-training, but if pre-trained models are used, it is necessary to verify whether the differences between the pre-trained and target tasks affect the applicability of the conclusions of this paper. It is recommended that the authors perform specific backbone architecture comparisons, such as testing on ResNet and Vision Transformer, and perform ablation experiments, using pre-trained and randomly initialized models, to directly assess the impact of pre-training on the findings.

2. In few-shot learning tasks, the domain gap exists in data distribution between an upstream task (pre-training task) and a downstream task (fine-tuning or application task). This may result in the knowledge learned by the model in the upstream task not being effectively migrated to the downstream task. In this case, methods need to be evaluated on cross-domain undersampled learning benchmark datasets such as DomainNet or Office-Home. Testing on these datasets enables a more specific assessment of the impact of domain gaps on the performance of its sample selection strategy and a clearer understanding of the applicability of its strategy to cross-domain few-shot learning.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
