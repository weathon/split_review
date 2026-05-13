# Hybrid Preferences: Learning to Route Instances for Human vs. AI Feedback

- Decision: Reject
- Scores: 6, 5, 5, 3

## Abstract
Learning from human feedback has enabled the alignment of language models (LMs) with human preferences.
    However, directly collecting human preferences can be expensive, time-consuming, and can have high variance.
    An appealing alternative is to distill preferences from LMs as a source of synthetic annotations as they are more consistent, cheaper, and scale better than human annotation; however, they are also prone to biases and errors.
    In this work, we introduce a routing framework that combines inputs from humans and LMs to achieve better annotation quality, while reducing the total cost of human annotation.
    The crux of our approach is to identify preference instances that will benefit from human annotations.
    We formulate this as an optimization problem: given a preference dataset and an evaluation metric, we train a \textit{performance prediction model} to predict a reward model's performance on an arbitrary combination of human and LM annotations and employ a routing strategy that selects a combination that maximizes predicted performance.
    We train the performance prediction model on \multipref{}, a new preference dataset with 10K instances paired with human and LM labels.
    We show that the selected hybrid mixture of LM and direct human preferences using our routing framework achieves better reward model performance compared to using either one exclusively.
    We simulate selective human preference collection on three other datasets and show that our method generalizes well to all three.
    We analyze features from the routing model to identify characteristics of instances that can benefit from human feedback, e.g., prompts with a moderate safety concern or moderate intent complexity.
    We release the dataset, annotation platform, and source code used in this study to foster more efficient and accurate preference collection in the future.

        {
            \small
            \begin{center}
                \renewcommand{\arraystretch}{1.co/datasets/allenai/multipref}
                \end{tabular}
            \end{center}
        }

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a routing framework for preference data mixing and selection. The framework decides whether to use human annotations or language model annotations by determining if an instance benefits from human annotations. Specifically, it consists of a Performance Prediction Model (PPM) and a routing strategy. The PPM learns the statistical features of several mixing datasets that are routed to human annotations and their performance after training, enabling the PPM to predict the performance of any preference dataset. Using the routing strategy, multiple candidate mixing datasets are generated, and the PPM predicts and selects the best-performing dataset for training. Besides, a preference dataset, MULTIPREF, is constructed to implement this framework. The effectiveness of the data mixing method using this framework is demonstrated across multiple benchmarks, showing improved performance compared to baselines. Furthermore, the characteristics of data that benefit from human annotations are analyzed.

### Strengths
1. This paper introduces an innovative routing framework to optimize the preference label space, automating the selection of appropriate annotation sources, thereby reducing human annotation costs while achieving better model performance.
2. It presents a Performance Prediction Model (PPM) that predicts the performance metrics of a trained model on a benchmark using the given dataset directly, rather than relying on model outputs, making it more convenient to predict dataset performance.
3. The claims regarding the performance of the framework are well-supported by experiments, with the designed experiments effectively demonstrating the advantages and good generalization performance of the routing framework across various benchmarks.

### Weaknesses
1. The experiments lack tests on other models, as all experiments are based on Tülu 2 13B. It is unclear if the framework would provide the same performance improvements when replacing the Reward Model or Policy Model. Training the PPM requires conducting hundreds of RLHF runs to explore the relationship between data features and outcomes, which is computationally expensive. If the PPM has low generalizability across different models, the usage cost would be high.
2. There is a lack of reasoning and explanation regarding the routing strategy algorithm, making it unclear why this particular routing strategy is adopted and the characteristics of the mixing data it generates. Specifically, the paper does not detail the specific mechanisms of how the routing strategy explores the space of possible mixing datasets, nor does it provide a clear rationale for the chosen approach over other potential strategies, such as those based on diversity or coverage of the preference space. This lack of detail makes it difficult to assess the robustness and generalizability of the proposed method.
3. The accuracy of the PPM is not convincing. The paper provides limited ablation analysis of the PPM and lacks information on the accuracy and robustness of the PPM's predictions on non-training datasets. Furthermore, the paper does not provide a detailed analysis of the PPM's performance across different types of preference datasets, which is crucial for understanding its limitations and potential biases. The absence of error bars or confidence intervals for the PPM's predictions also makes it difficult to assess the reliability of the results.

### Questions
1. Does the PPM have transferability to models other than Tülu 2 13B, and what are the computational costs?
2. Could you provide more information about the routing strategy? How does the routing strategy differ from completely random selection in terms of PPM training and the PPM’s evaluation of the generated mixing datasets?
3. Figure 3 shows that the PPM's predictions are very accurate on the actual RewardBench. How does it perform on the other evaluation tasks you used?
4. The paper mentions that the PPM was trained on 200 candidates datasets generated by routing strategies but only selects one predicted optimal candidate datasets from 500 candidates generated by routing strategies for evaluation. Why is this the case? According to the paper, the PPM's prediction time should be much less than conducting actual RLHF and evaluations on candidate datasets, so it would be feasible to select the optimal candidate datasets predicted by the PPM from thousands of candidates.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper aims to reduce the cost of preference tuning by training a model to route which sample should be annotated by humans and which can be annotated by LLM.

### Strengths
- The problem of this paper is important: obtaining a reward that best aligns with humans at the lowest cost. The proposed method can somehow reasonably reduce the cost.
- If the motivation is to reduce human annotation costs for policy tuning, the author's experiment results go beyond this. They found that human annotations are not necessary for all data, and the model can perform even better with fewer human annotations.
- The authors perform experiments on various datasets, each of which reflects an important ability of LLM, and their method achieves good results on those benchmark datasets.

### Weaknesses
 - The conclusion of this paper is intriguing but without in-depth discussion. If 100% human performance leads to worse (even the worst) performance, how can the author explain the policy model performance gap between training on synthetic and human annotations? Is our goal still "alignment"?
- Algorithm 1 looks too intuitive. The authors fill the human annotation set with arbitrary examples until it reaches budget b. It is unclear how this greedy process helps maximize the objective (Eq.(1)). More specifically, in the worst case, the algorithm will select the worst b samples, i.e., human annotations gain the least for the model alignment. This will further impact the PPM and trigger error propagation. 
- In the experiment, the authors only show the comparison between 100% human annotations,100% synthetic annotations in Table 3 and Table 4, and the proposed best hybrid annotations. They should include at least one randomly selected hybrid combination, e.g., 50% human annotations with randomly selected data + 50% synthetic annotations.

### Questions
- Regarding L188-L189, does the |S_human| = |D| and |S_human| = 0 equals to b=|D| and b=0?

### Soundness
3

### Presentation
2

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
This paper explores the integration of human and AI feedback to enhance annotation quality while reducing the overall cost of human annotation. The authors introduce a performance prediction model (PPM) designed to forecast the effectiveness of reward models based on various feedback combinations. To train the PPM, they create a novel preference dataset, MULTIPREF, which includes both human and AI annotations. Empirical results indicate that this approach yields better-performing reward models compared to using human or AI annotations alone.

### Strengths
The method is well-writen and well-motivated, addressing the high costs and time constraints associated with human annotation.

The construction of a new preference dataset combining human and AI annotations adds significant value for further analysis in the community.

### Weaknesses
Evaluating the quality of the two feedback types solely based on reward model performance is indirect and highly contingent on the model's training configuration, which can be influenced by numerous accidental factors. The authors should consider incorporating more direct metrics for evaluating the feedback types, along with corresponding case studies or additional downstream tasks, such as aligning LLMs through direct alignment algorithms.

The versatility of the feature representation is not sufficiently validated. If the feature representation lacks versatility, it will require manual design for each new task, complicating the process even more than human annotations. Furthermore, validating the effectiveness of feature representation necessitates preference data comprising both human and AI annotations, which could limit the practical applicability of the method.

More detailed training configurations and evaluation results of PPM is needed. For example, the correlation between the predicted and actual values ​​of the subdivision direction on the reward bench.

### Questions
While human feedback is generally viewed as high quality, the results presented suggest that integrating AI feedback is critical for performance improvement. The analysis in Section 5 indicates that human annotations perform better on moderate preference datasets. However, the paper does not address in which specific preference instances AI feedback provides a performance advantage. Is it on pairs with greater preference differentiation? If so, why?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper proposes a framework that leverages a Performance Prediction Model (PPM) to route pairs of preference data to either human annotators or LLM annotators. This data selection strategy improves the performance on RewardBench and downstream tasks.

### Strengths
N/A

### Weaknesses
1. This paper adopts an intuitive approach to data selection by training a classifier to choose the optimal preference data source between human or large language models (LLMs). Although there is no identical existing work, such improvements seem minor. Training a classifier appears to be merely an empirical engineering optimization, lacking elegance. Furthermore, similar efforts have employed uncertainty to judge the choice of sources, as discussed in [a].
2. The contribution of preparing data for a minor enhancement, such as training a classifier, is also minimal. Moreover, the dataset is quite simplistic: The feature space is basic, and the coverage and granularity of the Descriptive Subject are limited, as shown in Table 9. This simplicity suggests that the work is insufficient to serve as a foundation for substantial future advancements.
3. Using PPM to fit evaluation results on RewardBench is questionable. PPM is intended to assess the quality of a preference data source, thus the reliability of preference data quality on RewardBench is dubious. It is difficult to ascertain whether the PPM results are solid.
4. Section 2.3 on the ROUTING STRATEGY is also problematic. With a training set of 7K samples, each having a 0/1 binary choice, there are a total of 2^7K possible candidates. Yet, only 200 or 500 samples are selected, as claimed in line 219, which is minuscule compared to the total number of candidates, hardly ensuring adequate coverage. The method for selecting these 200-500 samples is not clearly justified, raising concerns about potential bias in the training data for the PPM.
5. Why do the authors select Tulu2 as the base rather than more popular models like LLaMA3? It is crucial to determine whether the PPM can improve upon more advanced models like LLaMA3, as shown in Tables 3 and 4.
6. The generalizability and scalability of the PPM are uncertain since it is trained using a limited RewardBench framework. Although Section 4.3 tested additional datasets, some of these, such as BBH and AlpacaEval, were part of RewardBench, which weakens the proof of effectiveness in Section 4.3. The use of datasets that overlap with the training data for the PPM raises concerns about potential overfitting and limits the conclusions that can be drawn about the generalizability of the approach.
7. Expanding the PPM to train on a larger dataset beyond RewardBench would introduce additional complexity to the RM-PPO pipeline, further increasing the complexity of RLHF. Such an investment may be neither elegant nor cost-effective.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
1
