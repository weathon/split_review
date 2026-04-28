# ImageNet-RIB Benchmark: Large Pre-Training Datasets Don't Guarantee Robustness after Fine-Tuning

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Highly performant large-scale pre-trained models promise to also provide a valuable foundation for learning specialized tasks, by fine-tuning the model to the desired task. 
By starting from a good general-purpose model, the goal is to achieve both specialization in the target task and maintain robustness.
To assess the robustness of models to out-of-distribution samples after fine-tuning on downstream datasets,
we introduce a new robust fine-tuning benchmark, ImageNet-RIB (Robustness Inheritance Benchmark).
The benchmark consists of a set of related but distinct specialized (downstream) tasks; pre-trained models are fine-tuned on one task in the set and their robustness is assessed on the rest, iterating across all tasks for fine-tuning and assessment. 
We find that the continual learning methods, EWC and LwF maintain robustness after fine-tuning though fine-tuning generally does reduce performance on generalization to related downstream tasks across models.
Not surprisingly, models pre-trained on large and rich datasets exhibit higher initial robustness across datasets and suffer more pronounced degradation during fine-tuning. 
The distance between the pre-training and downstream datasets, measured by optimal transport, predicts this performance degradation on the pre-training dataset. 
However, counterintuitively, model robustness after fine-tuning on related downstream tasks is the worst when the pre-training dataset is the richest and the most diverse. 
This suggests that starting with the strongest foundation model is not necessarily the best approach for performance on specialist tasks.
The benchmark thus offers key insights for developing more resilient fine-tuning strategies and building robust machine learning models\footnote{\url{https://jd730.io/projects/ImageNet-RIB}
}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the robustness and generalization ability of the pre-trained model after fine-tuning. Concretely, how would the model's generalization to out-of-distribution (OOD) samples change after fine-tuning a pre-trained model on a specific downstream dataset? The authors propose a dataset called ImageNet-RIB which combines existing ImageNet-based datasets. Then the authors conduct experiments on the benchmark to observe and compare the model's OOD generalization with different pre-training and fine-tuning settings. The settings include different pre-training datasets and fine-tuning methods. Among the several observations, the author derives a counterintuitive conclusion that large pre-training datasets do not guarantee the model's robustness after fine-tuning.

### Strengths
- Investigating the model's robustness and generalization is significant because real-world applications are complex with varying and dynamic data distributions.

- The experiments in this submission are comprehensive and detailed results and code are provided.

### Weaknesses
 - This paper has very limited novelty in both insights and methodology. The two main contributions are the proposed ImageNet-RIB benchmark and the observation that several existing fine-tuning methods (continue learning and robust fine-tuning) are effective in preserving robustness. Both are very trivial. Compared with the former relevant benchmark [1], ImageNet-RIB follows the same recipe but only adds more existing ImageNet-based datasets. Let alone the fine-tuning methods, as discussed in the related work part, continue learning methods such as EWC and LwF are introduced in Lines 148-150, and robust fine-tuning methods are introduced in Lines 134-137. Therefore, it seems to me more clarification is required on the novelty aspect.

- The presentation is not clear. First, it seems confusing regarding the claim that performance drop on the pre-training dataset can be predicted by the distance between the pre-training and downstream dataset. It is not clear to me which experimental or theoretical part is to support such a claim, i.e., evaluate how a specific statistic correlation can exist and how well when using such correlation for performance drop prediction. Second, the presentation and tables/figures are not well organized. For example, Algorithm 1 is redundant with Figure 2 as the evaluation process is simple and easy to understand. Table 4 should be placed before Table 2 because Table 4 is mentioned in the earlier paragraph. Moreover, Table 4 is redundant with Table 3 and I would suggest putting Table 4 in the appendix. Typo in Lines113-114 and Lines 316-317.

- The experiments are not sound enough to derive the claimed conclusion. For example, the strong claim that large pre-training datasets do not guarantee robustness after fine-tuning is not well supported. The experimental setting only considers three pre-training datasets including ImageNet-1K, ImageNet-21K, and LAION-2B, which is too rough to come to a "conclusion" on pre-training datasets. I would suggest conducting controllable experiments [2] to disentangle the size and diversity of the dataset on LAION-2B, e.g., curating small variants such as LAION-1M, LAION-10M, LAION-100M, and LAION-1B.

- To enhance the significance of the paper, it is necessary to know why the weird observation LAION-2B happens instead of just presenting experimental results and putting forward some hypothesis without any in-depth analysis.

### Questions
Please see the weakness part.

### Soundness
2

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
3

### Summary
This paper proposes a benchmark for testing robustness, based on existing diverse image recognition datasets. By training on one dataset and testing on others, the robustness can be evaluated through accuracy before and after training. The results show that current incremental learning and robustness training methods effectively improve robustness, while larger models tend to exhibit greater robustness.

### Strengths
1. This paper conducts extensive experiments, exploring the results of various methods that could potentially improve robustness, and also evaluates the effects of models of different sizes.
2. The paper is well-written.
3. The evaluation dataset is more diverse.
4. This paper finds that more data does not necessarily lead to greater robustness.

### Weaknesses
1. It seems that the paper did not collect or filter new data; rather, it appears to be more of an evaluation framework than a benchmark. The lack of novel data curation limits the impact, as the value of a benchmark often stems from the challenges posed by new, carefully selected data. The current framework primarily reuses existing datasets, which may not fully capture the nuances of robustness in real-world scenarios.
2. The conclusions drawn are quite obvious, as many similar studies have reached similar findings. It's unclear how this "benchmark" could benefit the community. Specifically, the observation that larger models exhibit greater robustness and that incremental learning methods improve robustness are not novel insights. The paper lacks a clear articulation of how this specific combination of datasets and evaluation protocol provides unique insights beyond what is already known.

### Questions
1. Apart from the different datasets, is there any core point that sets this evaluation apart from previous assessments?

### Soundness
2

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
The paper proposes the ImageNet-RIB Benchmark, which is a new benchmark to evaluate the robustness of models fine-tuned on downstream tasks. The authors did an extensive evaluation of ViT and ResNet models on the benchmark with different robustness and continual learning strategies.

### Strengths
The community is going to benefit from having such a benchmark. I found it good, and the authors did an extensive evaluation of different robustness strategies. Overall, the quality is good, and the idea of the paper is clean and easy to follow. The authors did a good job on the evaluation using many experiments.

### Weaknesses
There are some technical considerations that need to be added to the material for better reproducibility; for instance, why choose 10 epochs for fine-tuning for downstream tasks? Also, I didn't see any discussion about the LoRa rank selected for the evaluations or a hyperparameter search. 

Another hyperparameter is for the WiSE-FT; instead of choosing 0.5, the authors could provide the experiment with the trade-off by choosing 0.5 and generalizing more for OOD with the IMAGENET-RIB and selecting the lambda with D_{down} validation and evaluating it on the OOD. This analysis could be interesting, especially when combined with the insight of having a dataset that is far from the pre-trained and its impact on the ImageNet-RIB.

Figure 2 could have better legends, especially step 3; otherwise, it is hard to understand.

In Table 8, there are some methods with an accuracy of 100.0. Could the authors provide more insight? The task is not so challenging ...

### Questions
Could the authors provide more insight on evaluation time for getting one mRI on normal FT, for instance? It would be good to provide such information as the number of total images (sum of all OOD images used for eval) and get the mRI.

Could you provide more insights about the LoRa rank used?

I hope the authors can address the weakness section and the ones added here.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
Benchmarking Fine-Tuning Robustness: The study assesses the robustness of models by fine-tuning on one OOD dataset and evaluating on others, using diverse fine-tuning strategies (vanilla fine-tuning, linear probing, LoRA, and continual learning methods).

Dataset Distance Metrics: The paper explores how dataset distance metrics can predict robustness changes post-fine-tuning, using Optimal Transport Dataset Distance (OTDD).

Experimental Insights: Findings show that models pre-trained on large, diverse datasets are more robust on OOD datasets. Regularization-based continual learning with Model Soup achieves the best results, and linear probing performs best with LAION-2B pre-training, while pre-training on large datasets like LAION-2B is not always optimal for robustness preservation on downstream tasks.

### Strengths
This paper presents a comprehensive set of experiments.

### Weaknesses
The clarity of the writing could be improved in several areas:
Figure 3: Could you clarify what each point represents—are they the six downstream datasets? e.g. include a legend explaining what each point represents.
Continual Learning Setup: How exactly is continual learning trained across the pretraining and downstream datasets?
Figure 4: The blue bar for ‘IN-1k’ indicates a model pretrained on IN-1k and evaluated on an OOD downstream dataset. Do the blue bars for “IN-21k,” “IN-21k+augReg,” and “LAION-2B” represent models pretrained on these datasets, then fine-tuned on IN-1k, and evaluated on OOD? How are the red bars trained and evaluated? For example, does the red bar for “LAION-2B” mean pretraining on LAION, then fine-tuning on IN-1k, followed by further fine-tuning on an OOD downstream dataset, and finally evaluating on OOD? Could you elaborate on these details?

Additionally, the evaluation setup of ImageNet-RIB is the same as a single-domain generalization, where training occurs on one domain and evaluation on the remaining N-1. However, related works on single-domain generalization are not discussed. I recommend including a brief discussion of related works on single-domain generalization and explaining how your evaluation protocol differs from these existing ones.

Some observations in Section 4.2 are unsurprising:
Models pre-trained on larger, more diverse datasets perform better on both ImageNet-1K and its variants.
Fine-tuning on a downstream dataset that differs significantly from the pretraining dataset reduces pretraining accuracy. This similarity could be quantified using a distance metric in either image or feature space.


Lastly, the experiment in Section 4.4 is somewhat confusing. This section is crucial, as the authors make a counter-intuitive claim, and it's important to ensure the conclusions are accurate to avoid misleading readers. I will revisit this section once the experimental details in Figure 4 are clarified.

### Questions
I recommend that the authors provide more detail on the experimental setup in Sections 4.2, 4.3, and 4.4, this would help ensure a clear understanding of the setup.

### Soundness
2

### Presentation
1

### Contribution
2
