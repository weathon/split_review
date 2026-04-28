# A Dual-Metric Approach for Model Selection in self-supervised learning for histopathology

- Decision: Reject
- Avg Score: 2.50
- Scores: 1, 3, 3, 3

## Abstract
Selecting appropriate models during self-supervised training of vision transformers in histopathology is challenging. Recent efforts to quantify the quality of self-supervised learning representations through rank estimation approaches have shown promise in natural image classification tasks. However, their effectiveness in histopathology, particularly for non-linear tasks such as instance segmentation and classification from whole slide images, remains unexplored. This study proposes an approach for model selection in histopathology by combining task-specific metrics (such as accuracy) and task agnostic metrics (such as rank estimation). This work shows that by training several small-scale histopathology models and applying the proposed model selection approach, one can achieve instance segmentation performance comparable to state-of-the-art models trained on much larger datasets. The proposed approach also allows for obtaining a model based on the type of downstream task. Towards this end, three types of model selection based on the downstream task performance were evaluated: classification-best, segmentation-best, and a best all-round one. When evaluated on held-out classification and weakly supervised learning tasks, the most performant checkpoints often occur earlier in training, indicating potential performance saturation mid way in the training for histopathology models. These results highlight the importance of appropriate model selection for self-supervised learning in histopathology.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
Model selection is a challenging task in histopathology SSL. The authors proposed a novel model selection approach, and concludes that model selection is important and early stopping may be important for model performance.

### Strengths
- Model selection is a very important and relevant task, especially in the era of the explosion of histopathology foundation models.
- Authors included meaningful tasks beyond histological subtyping, including EGFR prediction and nuclei instance segmentation.

### Weaknesses
 - The proposed model selection procedure appears to be overly simplistic and lacks innovation. It consists of taking the max over many existing task agnostic or task specific existing metrics, but doesn’t include novel metrics to assist model selection or additional insights.
- The benchmarking in the paper is not sufficient. If the author’s claim is that the proposed procedure contributes to model selection, the author ought to compare it to other existing model selection methods. For example, reasonable questions and benchmarks includes: model performance with only use the task agnostic metrics, and model performance on a a task using only a different task specific metric.
- All benchmarks in the manuscript lack error bars.
- The writing of the manuscript can be improved. Some of the notation is not consistent and overcomplicates the proposed method.

### Questions
Please address the concerns raised in weakness section, especially on the innovation of the manuscript.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper propose a model selection approach to find the best checkpoint in self-supervised learning with specific application to digital pathology. The key of the proposed approach is integrating task-agnostic and task-dependent (surrogate task) metric. The authors demonstrate that they can achieve competing performance of larger model trained on more data in certain tasks with way smaller model and data.

### Strengths
- Originality: The authors propose an interesting idea to address the issue that the performance boost from self-supervised learning loss does not transfer effectively to downstream tasks. They observed a new phenomenon: different downstream tasks may have different optimal checkpoints that are not necessarily at the optimum of the self-supervised learning loss landscape.

- Quality: The authors trained various models across different model and data sizes to support the proposed approach, providing some evidence for the idea.

- Clarity: The authors used multiple figures to support their observations.

- Significance: The authors present an interesting approach to guide and evaluate the training of self-supervised learning. If more evidence is provided, this approach could be beneficial for training self-supervised learning models.

### Weaknesses
 - Experiment:
    - Good performance on Table 2 appears to be the direct influence of cherry-pick. As the proposed method involve picking the checkpoint where lead to more performance boost in the surrogate task. It is unclear how much the performance gain comes from the proposed method versus simply selecting the best performing checkpoint on the surrogate task.
    - Lack of baseline in the Figure 4. If my understanding is correct, the author pretrained model on internal LUAD train, using the surrogate task metric + task agnostic metric to select checkpoint, then testing the performance on internal LUAD test. How does it compare to the directly using self-supervised loss? And how far it is if we directly use foundation model like those shown in Table 2? The absence of a baseline makes it impossible to evaluate the true benefit of the proposed method.
    - Lack of generalization baseline: If we apply the same training recipe to pretraining, does the trained model generalize to other cohort like TCGA? In other word, does it do good in TCGA-LUAD/LUSC subtyping? I think the author should at least provide some benchmark on public slide-level dataset. The lack of evaluation on external datasets limits the assessment of the method's robustness and generalizability.
    - What is the subtype statistics in your internal LUAD? Is it balanced/imbalanced? Why did the author report AUC in multi-class classification instead of reporting imbalanced-awared metric like balanced accuracy? The choice of evaluation metric should be justified given the potential class imbalance, and balanced accuracy or other metrics may be more appropriate.

- Methodology: When you only trained on LUAD data, how do you rationalize that data from other organs where the morphology could be very different from LUAD could be a good surrogate task? The use of surrogate tasks from different organs needs a stronger justification, especially given the potential for morphological differences.

- Clarity
  - This paper seems to be prepared in rush, there is a clear typo in line 311 and the first page of the appendix is disorganized
  - The table 2 is confusing due to the under/upperscore, which confuses the current/previous/next rows
  - Methodology: The Step 3 in the proposed algorithm is confusing. Mathematically, How can two matrices with different dimension (i.e., E x N and E x M) be added together then take argmax on one dimension. The authors have to re-write it to better convey the meaning of taking pair of metrics Ts and Ta. The description of the algorithm is unclear and needs to be revised for better understanding.

- Overall practical use: Since the proposed method is only evaluated on one cancer subtype (as mentioned in the limitation) and need curated surrogate task (which could be irrelevant), I doubt how much gain/ how generalize the proposed approach compared to off-shelf foundation model?

### Questions
(1) Can the authors explain the lack of a baselines in the experiment?

(2) Can the authors explain the rationale behind the methodology design? How can tissue with very different morphology help in your pretraining data?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a dual-metric model selection strategy for self-supervised learning in histopathology. The main idea is to consider both task-agnostic (like rank) and task-specific metrics (like accuracy) for selecting the best checkpoints. The algorithm can be used to select the best checkpoints for classification, segmentation and all rounds.

### Strengths
1. The paper brings an important problem of selecting the best checkpoint in self-supervised training. In most of the existing foundation models for histopathology as well as those for natural images, people still train for a fixed number of epochs and take the last epoch for evaluation.
2. The paper presents detailed analysis of the model's behavior on both downstream tasks and task-agnostic metrics over training epochs, which is valuable.

### Weaknesses
1. There are vast arrays of tasks in computational pathology, including ROI classification (by linear classifier or end-to-end finetuning), slide-level classifications, survival analysis, and segmentations. It is not clear enough how does the proposed metrics help on the tasks that's not included in the task metrics. E.g. which metric should user use if they want to select a checkpoint that works the best in slide-level classifications? In Figure 4 b and c, none of the metrics give the best checkpoint that is consistently better than others. Additionally, $e_c^*$ is also not the best for patch-level classification (figure 4a).
2. How does the checkpoint selected by the proposed dual-metric compare to that selected by purely task-specific performance?
3. The training and evaluation are limited. The existing foundation models were typically trained on large data, and evaluated on diverse tasks. While I understand that it's hard to have access to data at that scale, training on LUAD only is limited and it's not clear if the conclusion obtained here is transferrable to larger models trained on larger data size or not. Additiaonlly, the choice of using CRC as one of the evaluation tasks makes the models not discriminative between each other. Rather, TCGA UniformTumor can be better task.

### Questions
Given the close performance of between the checkpoints, what are the standard deviations of the performance?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
As outlined in the paper’s contributions, the authors propose a straightforward approach to model selection. This approach involves training various models on different end tasks and evaluating their performance based on classification, segmentation, and task-agnostic metrics. The models are further assessed on an out-of-distribution dataset and a slide-level task to validate their robustness.

More specifically, their model defines a set of $N$ task-specific metrics, $P^{ts}$, and  $M$  task-agnostic metrics, $P^{ta}$. These metrics are evaluated over $E$ epochs, with the $P$ matrices normalized metric-wise using min-max scaling. For each task-specific and task-agnostic metric pair, the epochs that yield the best paired performance are selected. From these selected epochs, the relative improvement for each task-specific metric is calculated, contributing to an overall performance score. Finally, the epoch with the highest relative improvement, $r$, is retained as the optimal model."

### Strengths
* Code for reproducibility will be released if the paper is published.
* The related work on task-agnostic quality metrics is well-written and aligns fully with the research scope, as noted by the authors (e.g., "Using these task-agnostic metrics ... is the track followed in this work").
* The proposed algorithm is straightforward and easy to understand.
* The learning process is well represented in Figure 3; however, it is difficult to distinguish $e_a$ (red), $e_s$ (blue), and $e_c$ (green) due to similar color tones.

### Weaknesses
 * The related work section is overly detailed. While it provides a good overview of self-supervised learning (e.g., SimCLR, CLIP, DINO, iBOT) and multi-scale models (e.g., HIPT, GigaPath), much of the review is not directly relevant to the main focus of the paper. The paper should emphasize metrics rather than the development and history of SSL models. Shortening this section would improve readability.

* For Table 2, three decimal places would improve clarity, as the current values are too similar. Additionally, grouping results by $e_a$, $e_s$, and $e_c$ rather than by models would make the table more informative. Specifically, it is difficult to ascertain the performance differences between the models when the results are grouped by model rather than by the epoch selection criteria. This makes it difficult to understand the impact of the different epoch selection criteria.

* In Figure 4, a comparison with reference models (e.g., Virchow, UNI) is missing. The lack of comparison to established baselines makes it difficult to assess the relative performance of the proposed method. Without these comparisons, it is unclear if the reported results are significant or merely incremental improvements over existing techniques.

While the method is simple overall, it is also somewhat complicated in that there appears to be minimal differentiation among $e_a$, $e_s$, and $e_c$. It would be interesting to show the loss progression on a small validation set to compare with the best epochs. Additionally, there is no clear rule for choosing between $e_a$, $e_s$, or $e_c$. The paper does not provide sufficient justification for why these three specific epoch selection criteria are used and how they differ in practice. The lack of a clear decision rule for selecting between them further complicates the method.

Other comments:
    A clearer distinction in Figure 2 between task-specific and task-agnostic metrics would be helpful (e.g., using dashed vs. solid lines or separating them). The plot is difficult to read as is. The current overlapping lines make it hard to discern trends and relationships between the different metrics. 
    (Line 311) Add space between “3” and “present.”
    (Line 368) Ensure consistency with capitalization “Figure”/“figure”.
    (Line 364) Table 2 is cited two pages earlier, which disrupts readability.

### Questions
* I am not sure why the algorithm defines relative improvement using only task-specific metrics and not the task-agnostic ones as well. Is it because including the task-agnostic metrics would effectively be equivalent to taking the argmax across all metrics? How much would this change the current estimation of the optimal $e$?

* Here is a list of small details that could be updated:
	* In Algorithm 1, the variable $k$, representing the index of elements in S, is not introduced. It would be helpful to add a note such as $|S| = K$.
	* The expression on line 6 in the algorithm is unclear. It appears that $r$ is a vector; however,  $argmax_n r_n$ returns two indices."

### Soundness
2

### Presentation
3

### Contribution
1
