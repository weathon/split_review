# WASH: Train your Ensemble with Communication-Efficient Weight Shuffling, then Average

- Decision: Reject
- Scores: 6, 6, 3, 3

## Abstract
The performance of deep neural networks is enhanced by ensemble methods, which average the output of several models. However, this comes at an increased cost at inference. Weight averaging methods aim at balancing the generalization of ensembling and the inference speed of a single model by averaging the parameters of an ensemble of models. Yet, naive averaging results in poor performance as models converge to different loss basins, and aligning the models to improve the performance of the average is challenging. Alternatively, inspired by distributed training, methods like DART and PAPA have been proposed to train several models in parallel such that they will end up in the same basin, resulting in good averaging accuracy. However, these methods either compromise ensembling accuracy or demand significant communication between models during training. In this paper, we introduce WASH, a novel distributed method for training model ensembles for weight averaging that achieves state-of-the-art image classification accuracy. WASH maintains models within the same basin by randomly shuffling a small percentage of weights during training, resulting in diverse models and lower communication costs compared to standard parameter averaging methods.  %In this paper, we present WASH, a novel distributed method that provides state-of-the-art results in training models via weight averaging,     by permuting a small percentage of weights between models during training. WASH allows models to remain    within the same basin while retaining high ensembling accuracy. Furthermore, by only requiring a fraction of parameters to be shuffled between models at every step, this results in a lower communication cost compared to methods leveraging the average parameters of all models.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposed a shuffling-based ensemble training algorithm that enables immediate weight averaging with good generalization ability without the need of further finetuning. The proposed method is motivated by the fact that a previous method called PAPA will gradually reduce the distance of the models to their consensus, thus hidering their diversity. In contrast, the proposed shuffling operation preserves the consensus distance and thus potentially improves model diversity and performance. Moreover, it also requires less communication and thus improves communication efficiency.

### Strengths
1. The paper is clearly written and the related work section is thorough and very informative.
2. Besides the main results in Tab 2 & 3, the authors also provided other informative empirical results to show why the proposed method is effective and superior to PAPA, like the observation of consensus distances and the 2D example.

### Weaknesses
1. The authors mainly compared the proposed method with PAPA. I understand that maybe this work is a close follow-up on PAPA and thus PAPA is the main competitor. But I checked the results in the PAPA paper and found that PAPA itself can be inferior to DART. So I think it would be better to include DART in the comparisons or at least discuss why not including it. The lack of direct comparison with DART, especially given DART's reported performance, makes it difficult to assess the true advancement of the proposed method. It's crucial to understand if the gains over PAPA translate to gains over other state-of-the-art methods, or if the proposed method is simply better than a weaker baseline.

2. Advantages over PAPA are marginal most of times. The gaps are only significant with larger models and larger datasets. While the method may show promise in specific scenarios, the limited improvement in many cases raises questions about its broad applicability and practical impact. The fact that significant gains are only observed in resource-intensive settings suggests that the method might not be beneficial for smaller-scale tasks or models.

3. While there are reproduction issues with PAPA on ImageNet, I think it would be better to also include those results in Table 3 and faithfully explain how the results went wrong, considering that there is still spare space for the main text. Omitting these results, even if problematic, leaves a gap in the evaluation and makes it harder to fully understand the limitations of the proposed method and the challenges in reproducing prior work.

### Questions
I think Tab 1 is only a conceptual illustration of the communication efficiency of WASH. In real world, do the authors think that the randomness in WASH will make it harder for really efficient hardware implementation?

### Soundness
3

### Presentation
4

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
The paper proposes a novel method, wash, for training deep ensembles with two key selling points:
* The individual models remain in the same weight basin, meaning that robust predictions can be made by averaging the weights of the individual members and executing a single forward pass.
* Wash requires a fraction of the communication cost incurred in each training step compared to similar approaches.

WASH works by shuffling a small percentage of the weights between the ensemble members in each training iteration. The result is that the members become robust to this augmentation and by the end of training, the weights remain near each other (in the same basin).

Experimental results show that WASH matches and often exceeds the performance of PAPA at a much lower communication cost. The models are evaluated on image classification benchmarks: Cifar10, Cifar100 and ImageNet, across three architectures: VGG16, ResNet18 and ResNet50.

### Strengths
The paper proposes a very interesting and novel approach for keeping the ensemble members near each other in weight space, while keeping the communication cost low.

The method clearly works: There is a clear improvement in communication cost without a significant negative impact on performance. The image classification benchmarks show improvement over PAPA for multiple architectures.

The paper is very well presented: The paper also dives into the intuition of why WASH works. It explains the dynamics of the networks through a 2d toy example. It also showcases that WASH has a better diversity by examining the distances of the individual models from the consensus throughout training.

The experiments are thorough: The paper ablates three design choices: the layerwise adaptation of the shuffle probability, the magnitude of the shuffle probability and the idea of using a warmup period instead of enabling shuffling from iteration 1.

### Weaknesses
I was disappointed that the experiments did not detail the impact of the reduced communication cost. The work is primarily motivated by the reduction in communication cost, but we don't see experiments showcasing the overall compute reduction during training or the improvement in training time. It is impressive that the communication cost is reduced by a factor of 1/2-1/200, but it is unclear whether this results in compute savings or faster training. Specifically, the paper lacks a direct comparison of training time or GPU-hours consumed by WASH versus PAPA for the reported experiments. This makes it difficult to assess the practical benefits of the proposed method beyond the reduction in communication volume. The reported communication speed is not directly linked to overall training time, and without this, the practical impact of the method remains unclear. It would be beneficial to see a table or figure showing the total training time or compute cost (e.g., GPU hours) for both methods across the different datasets and architectures.



### Questions
* Addressing the weakness mentioned above.

* The choice of a linear schedule for the shuffle probability is rather arbitrary. The ablation in the appendix examines a constant vs increasing vs decaying schedule and we see that the decaying schedule gives an improvement. Are there experiments with other schedules? I wonder if p could be tuned per layer based on the variance of the weights across the ensemble members.

* Why do the imagenet experiments require so much larger p than the cifar experiments? Is there an intuitive reason for this? Should we expect that as models and data scale, p will get closer to 1?

* What is the distance metric used in Figure 2?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work proposes the WASH algorithm for weight-averaging multiple models trained in parallel under a from-scratch training scenario (i.e., each model starts with different random initializations). Naively trained models from these different initializations converge to different basins on the loss landscape, and thus they cannot be weight-averaged. The WASH algorithm addresses this issue by employing a simple strategy that mixes subset of weights between models during training, enabling them to converge into the same basin and thus be effectively weight-averaged.

### Strengths
- The concept behind the proposed WASH algorithm is straightforward and intuitive. Moreover, it incorporates various engineering considerations to improve practical performance, such as adjusting shuffling probability based on depth.
- Sections 1 and 2 provide a comprehensive overview of existing work on ensembling and weight-averaging in the fields of machine learning and deep learning.
- Figure 1 and Algorithm 1 present the proposed WASH algorithm in a clear and easily understandable way.

### Weaknesses
 - The concept behind the proposed WASH algorithm is straightforward and intuitive. Moreover, it incorporates various engineering considerations to improve practical performance, such as adjusting shuffling probability based on depth.
- Sections 1 and 2 provide a comprehensive overview of existing work on ensembling and weight-averaging in the fields of machine learning and deep learning.
- Figure 1 and Algorithm 1 present the proposed WASH algorithm in a clear and easily understandable way.

- It seems the authors argue that the core of the WASH algorithm is communication efficiency. However, the current manuscript only discusses the theoretical communication volume presented in Table 1. According to main tables (Tables 2 and 3), the WASH algorithm does not show a significant performance advantage over the existing PAPA algorithm. To demonstrate the utility of the WASH algorithm, it would be helpful to present actual communication costs alongside the performance metrics. For instance, providing the wall-clock time required for training could enhance this analysis. The lack of empirical evidence regarding the actual training time and communication overhead makes it difficult to assess the practical benefits of the proposed method, especially when compared to PAPA, which, despite having a higher theoretical communication volume, might not translate to a significantly longer training time in practice.

- The main tables (Tables 2 and 3) presents the results of weight-averaging for independently trained models, including UniformSoup (labeled as "Averaged") and GreedySoup. These results are redundant, as none of the combinations achieve effective weight-averaging in such cases. Furthermore, GreedySoup merely reflects the performance of the single model with the best validation metric. Notably, the GreedySoup algorithm relies on the assumption that fine-tuned weights, derived from the same pre-trained model, lie within a single basin suitable for weight-averaging—an assumption valid in transfer learning contexts but not applicable to the from-scratch training scenario in Table 3. The inclusion of these baselines does not provide meaningful insights into the performance of the proposed method and distracts from the core contribution of the paper.

- The ultimate goal of the WASH algorithm is not only to facilitate weight-averaging of multiple models trained in parallel through parameter shuffling but also to ensure that the resulting weight-averaged model achieves superior performance. Therefore, it is crucial to compare the WASH algorithm with other high-performance single-model approaches, particularly those based on weight-averaging (such as single-trajectory strategies for from-scratch training, including Stochastic Weight Averaging by Izmailov et al. (2018) and the Lookaround optimizer by Zhang et al. (2023)). However, the only baseline currently presented is PAPA, along with the fundamental baselines of a single model representing a performance lower bound and an ensemble model (commonly referred to as deep ensembles) representing a performance upper bound. The absence of comparisons with single-model weight-averaging techniques limits the assessment of the proposed method's effectiveness.

- Recent trends have significantly shifted from from-scratch training to transfer learning approaches that involve fine-tuning pre-trained models. For instance, the model soup paper referenced in this study focused on fine-tuning both supervised and CLIP pre-trained vision models for ImageNet in 2022, yielding extensive experimental findings. Since this work is exclusively centered on a from-scratch training scenario, the lack of fine-tuning experiments with contemporary pre-trained models makes the results less compelling in 2024.



### Questions
Here are my questions and further concerns:

- I understand that the homogeneous setup is described as not using data augmentation, as noted in line 315, which states "homogeneous setting with no data augmentations." However, the performance of the single model presented in Table 3, specifically the performance of GreedySoup—given that it achieves the best validation metric for a single model in a from-scratch training scenario—appears excessively high. Could it be that basic data augmentation techniques, such as random cropping with random horizontal flipping, were applied instead of no augmentation at all?

- According to Table 2, the accuracy of the single ResNet50 model on ImageNet is approximately 74%. Given that there are no modifications to the ResNet50 architecture and that training data augmentation was applied, this result seems quite unusual. For example, the V1 ResNet50 checkpoint from torchvision achieves around 76% when trained for 90 epochs with a batch size of 256 and without a complex training recipe. Since this paper employs advanced augmentation techniques—such as mixup, label smoothing, cutmix, and random erasing—we would expect the performance to exceed 76%. In fact, the PAPA paper (Jolicoeur-Martineau et al., 2024) demonstrates that a single ResNet50 model achieves an accuracy of 76.8% on ImageNet under these conditions. Therefore, there are concerns about the appropriateness of the experiments conducted, in addition to the earlier mentioned issues regarding the no-data-augmentation in the homogeneous setup.

- Is there a specific reason why the ImageNet results are absent from the homogeneous setup? Currently, the ImageNet results are only presented in Table 2 and not in Table 3.

- Figures 2 and 3 do not need such a large allocation of space, as they lack small elements that require close examination. As they stand, they occupy excessive space.

- The conclusion section is missing a section number; it should be labeled as "5. Conclusion" rather than just "Conclusion."

- How statistically significant is the claim in Appendix B.3 that WASH outperforms PAPA in terms of ECE for the CIFAR-100 scenario? Additionally, since Table 4 mentions the "optimal temperature," it appears that the ECE was computed after applying temperature scaling. How does the ECE compare without temperature scaling? Also, it might be worth considering NLL as an additional metric for evaluating predictive uncertainty.

- The results in Appendix C.5 suggest that using UniformSoup (i.e., averaging) yields better performance than GreedySoup for the multiple soup ingredients obtained with WASH. Do you have any educated guesses as to why this might be the case? Why could selecting only the weight-averaged ingredients based on validation metrics result in worse performance?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper proposes WASH, a weight averaging method for obtaining a weight-averaged model with minimal communication cost during the training procedure. The key idea is to randomly shuffle a small fraction of the parameters. Experimental results demonstrate that the proposed method achieves state-of-the-art classification results with a reduced communication burden.

### Strengths
* I believe this paper addresses an impactful problem; model averaging with minimal communication cost is promising for democratizing ensemble methods in real-world tasks.
* The proposed method is convincing and intuitive. Moreover, the paper provides empirical analyses that reveal how the method works, which helps the reader understand it.
* The paper is generally well-written and easy to follow.

### Weaknesses
I do not find any major flaws in this paper, except in the experimental section. I would like to focus on the experiments on the ImageNet dataset, as I believe one of the main advantages of these model averaging methods is that they can be easily applied to large data regimes and large-scale models compared with probabilistic methods such as Bayesian neural networks.

* The accuracy of the proposed method is significantly lower than the PAPA baseline by 1.23 pp (75.80% for the PAPA ensemble vs. 74.39% for the WASH ensemble method). This difference, while seemingly small, is concerning given the established performance of ResNet-50 on ImageNet.
* The paper only provides results with small-sized models (e.g., ResNet-50 and smaller). Including results with modern neural networks such as Vision Transformers and ConvNeXt would strengthen the paper. The absence of these results limits the generalizability of the findings, especially given the increasing prevalence of these architectures in the field.
* I wouldn't say the communication improvement is significant, as WASH still uses between 1/2 and 1/4 of the communication volume compared with PAPA. Providing scenarios or real-world numbers would improve the paper. For example, when we train ResNet-50 on ImageNet, how much communication bandwidth and training time can we save? Do we have to shuffle the models every step to achieve high accuracies? The lack of concrete examples makes it difficult to assess the practical impact of the communication reduction.
* The performances of the proposed method, PAPA, and the deep ensemble baseline on ImageNet-1K are all lower than I expected. I anticipated the performance would be higher than 76% even without utilizing ensemble methods [1]. If we utilize modern data augmentations, the accuracy should be about 80% [2]. The discrepancy between the reported results and expected performance raises concerns about the experimental setup and the potential limitations of the method.
* It is a minor point, but I consider the performance difference between WASH and WASH+Opt as a weakness. Providing the results for one method and placing the others in the appendix may improve clarity. The inclusion of multiple variants without a clear justification complicates the interpretation of the results.
* Also, solely providing an image classification task might not be sufficient to demonstrate the effectiveness of the proposed method. The lack of experiments on other tasks limits the scope of the paper and its applicability to diverse real-world problems.

I enjoyed reading about the method and the analyses. However, the performance improvements in terms of accuracy as well as communication cost are not groundbreaking when we consider the high standards of the conference.

### Questions
Please refer to the weaknesses section.

### Soundness
3

### Presentation
4

### Contribution
1
