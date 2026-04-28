# Rethinking Dataset Quantization: Efficient Core Set Selection via Semantically-Aware Data Augmentation

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Dataset quantization (DQ) is an innovative coreset selection method to choose representative subsets from large-scale datasets, such as ImageNet. Although DQ has made significant progress, it heavily relies on large pre-trained models (like MAEs), leading to substantial additional computational overhead. We first identify that removing this pre-trained MAE model degrades DQ’s performance and increases the variance in model training. Where MAE plays a crucial role in introducing prior knowledge and implicit regularization into the training process. Second, we investigate a data augmentation scheme that can simulate the steps of pixel compression and reconstruction in DQ by simply using a randomly initialized ResNet model. This randomly initialized ResNet model can take advantage of the inductive bias of CNNs to locate the semantic object region and then replace the other region with other images. Therefore, we can use a random model or trained model in the early training stage to enhance semantic diversity while selecting important samples. We remove the module that contains the pre-trained MAE model and integrate the data augmentation scheme into the DQ pipeline, which formulates a new simple but efficient method, called DQ v2. Our method achieves performance improvements across multiple datasets, such as ImageNette, CUB-200, and Food-101.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the high computational cost of Dataset Quantization (DQ) due to its reliance on large pre-trained models like MAE and ResNet. They propose DQ V2, which removes pre-trained models by using a random CNN-based data augmentation that retains semantic structure by masking objects and replacing backgrounds, enhancing diversity without costly models. The goal of data augmentation (synthesizing) in their pipeline is to enhance data diversity and representation without relying on costly pre-trained models. 

Evaluation: Evaluated on ImageNette, CUB-200-2011, Food-101, and ImageNet-30, DQ v2’s performance is compared with DQ’s. DQ v2 achieves comparable or better performance than the original DQ method, showing an average improvement of about 1.57%.

### Strengths
1. Computational Efficiency: By removing the reliance on large pre-trained models, DQ V2 lowers computational costs.

2. Good insight for data augmentation: The pre-trained MAE model is equivalent to a data augmentation method (in introducing prior knowledge and implicit regularization into the training process)

3. The writing is clear and easy to follow.

### Weaknesses
1. Lack of Quantitative Analysis on Computational Gains: While the paper claims computational benefits from replacing the MAE model with a CNN-based data augmentation strategy, it lacks specific measurements or comparisons to substantiate these gains. A quantitative analysis—such as GPU hours, memory usage, or training time—would provide stronger evidence of the efficiency improvements in DQ V2. The paper should include a detailed breakdown of the computational cost associated with both the original DQ and the proposed DQ V2, including the time spent on data augmentation and model training. This should also include a comparison of the number of parameters and FLOPs for the different models used (MAE vs. ResNet-18).

2. Missing Baselines: I noticed that some recent coreset selection baselines for deep learning are missing: D2 Pruning[1], CCS[2], Moderate[3]. Those baselines seem to have a stronger performance than the proposed methods. The paper should include a comparison with these methods to better contextualize the performance of DQ V2. Specifically, the paper should compare the performance of DQ V2 with these baselines on the same datasets, using the same evaluation metrics.

3. Missing evaluation on ImageNet-1k: the paper argues that DQ-V2 is more efficient than DQ, but the method is only evaluated on the ImageNet subset. Previous methods including DQ all conducted evaluation on ImageNet-1k. It will be good to include an ImageNet-1k evaluation to demonstrate the scalability of the proposed methods. The lack of ImageNet-1k evaluation makes it difficult to assess the practical applicability of the proposed method in real-world scenarios.

4. The data augmentation part is confusing: the goal of data quantization and coreset selection is to reduce the size of the training dataset, but the data augmentation method proposed in the paper expands the datasets -- the final expanded training dataset can be even larger, which is contradicted to the goal of coreset selection. The paper needs to clarify how the data augmentation is used in the coreset selection process and how the final dataset size is controlled. It is unclear if the augmented data is used to select the coreset or if it is used to train the model after the coreset is selected.

5. Ablation study on data augmentation: The paper would benefit from a more detailed ablation study to assess the effectiveness of the data augmentation method used in DQ V2. Testing different data augmentation configurations (e.g., no augmentation, alternate augmentation techniques) would clarify its impact and help refine the methodology. The ablation study should also investigate the impact of different masking strategies and background replacement techniques on the final performance of the model.

### Questions
See weakness

### Soundness
2

### Presentation
3

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
This paper examines the limitations of the DQ method and proposes corresponding improvements. The authors believe that using a pretrained MAE in DQ may cause issues, so they conducted experiments to see the impact on DQ when MAE is removed. The experiments, in a way, demonstrate the importance of MAE. The authors suggest using Tobias data augmentation as a substitute for MAE. According to their results, it is possible to achieve accuracy comparable to or even better than the previous DQ without using MAE.

### Strengths
1. The method proposed by the authors does indeed achieve comparable or even higher results without using MAE.

2. The authors conducted extensive ablation studies on the parameters of the method itself, including experiments on patch size and data selection methods.

### Weaknesses
1. The motivation of this paper is somewhat unclear. From my understanding, the main value of DQ lies in reducing dataset size and storage requirements. However, as shown in Table 1, this method actually increases the storage usage of DQ. The problem it addresses is the need for a pretrained MAE in the original DQ, yet the authors' experiments do not highlight any obvious issues caused by using MAE. In my view, the authors have optimized a relatively minor aspect while losing sight of one of DQ’s key contributions. It would be beneficial for the authors to further elaborate on the advantages of this method.

2. The logic of the proposed method is unclear. The authors first apply Tobias data augmentation, followed by dataset selection—what is the advantage of this sequence? What would the outcome be if Tobias data augmentation were added directly at the end based on DQ?

3. The conclusions regarding line 210 may have some bias, as MAE was pretrained on ImageNet, which likely results in better reconstruction performance on ImageNette. The variables here are not limited to dataset size, so the effectiveness may not necessarily be due to the dataset size alone. It could also be influenced by the effectiveness of MAE itself.

### Questions
The biggest question is what specific negative effects MAE actually introduces, as the authors' experiments and analysis do not clearly convey any significant drawbacks to using MAE.

### Soundness
2

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
5

### Summary
This work proposes DQ_v2, a corset selection method. To remove the pre-trained MAE in DQ, the authors investigate a data augmentation scheme, which can simulate the steps of pixel compression and reconstruction in DQ. Finally, the authors show the performance on several benchmark datasets, including CUB-200, Food-101, and ImageNet. The idea of using data augmentation to replace pre-trained MAE in DQ is somewhat novel to me. However, some critical concerns remain, please see weakness.

### Strengths
1. Using semantical-aware data augmentation to remove the pre-trained MAE model in DQ is interesting.
2. The paper is well-organized.
3. Experimental results show that the proposed DQ_v2 eliminates the drawbacks of DQ's dependence on pre-trained.
4. The proposed method achieves performance improvement on multiple datasets.

### Weaknesses
1. In line 278, the authors say that the corset contains both original and augmented images. However, as far as I know, most existing corset selections only select original images from the datasets, meaning that there are no augmented images in corsets. So is this a fair comparison between DQ_v2 and other corset selection methods?
2. The literature review section lacks comprehensiveness. Numerous recent studies closely related to the topic have not been studied, such as [1-5], which may affect the context and clarity of the proposed approach.
[1] Tan, Haoru, et al. "Data pruning via moving-one-sample-out." Advances in Neural Information Processing Systems 36 (2024).
[2] Xia, Xiaobo, et al. "Moderate coreset: A universal method of data selection for real-world data-efficient deep learning." The Eleventh International Conference on Learning Representations. 2022.
[3] Yang, Shuo, et al. "Dataset pruning: Reducing training data by examining generalization influence." arXiv preprint arXiv:2205.09329 (2022).
[4] Maharana, Adyasha, Prateek Yadav, and Mohit Bansal. "D2 pruning: Message passing for balancing diversity and difficulty in data pruning." arXiv preprint arXiv:2310.07931 (2023).
[5] Yang, Suorong, et al. "Not All Data Matters: An End-to-End Adaptive Dataset Pruning Framework for Enhancing Model Performance and Efficiency." arXiv preprint arXiv:2312.05599 (2023).
3. In the semantic data augmentation section, the authors enhance diversity by replacing image backgrounds. However, it’s unclear if the potential for semantic ambiguity was considered—for instance, whether the new backgrounds might inadvertently introduce other objects, which could affect the intended semantics. The description of the background replacement process lacks sufficient detail to fully assess this risk. Specifically, the method of shuffling patches and the scale of these patches are not clearly defined, making it difficult to determine if the background replacement is truly semantically neutral.
4. The authors report only storage costs, but I recommend adding a comparison of training costs as well. This would provide a more comprehensive assessment of the method’s efficiency and practical applicability. The analysis should include not only the time required for training the final model on the selected corset but also the computational overhead of the corset selection process itself. This is crucial for understanding the overall efficiency gains or losses.
5. The practical significance of the proposed method is unconvincing due to limited experimental validation. In the experimental section, all benchmark comparisons are with methods published before 2021. The compared baselines are outdated. While authors claim the comparison with state-of-the-art, many existing SOTA methods [1-5] are not compared. This weakens the method’s practical performance and significance.

### Questions
Please see weakness.

### Soundness
2

### Presentation
2

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
This paper proposes Dataset Quantization V2 (DQ V2), an enhanced version of the original Dataset Quantization (DQ) method, focusing on efficient coreset selection without relying on large pre-trained models like MAE. Instead, DQ V2 integrates a new data augmentation strategy called Tobias, which uses randomly initialized CNNs to preserve the semantic regions of images while replacing background areas, mimicking the effect of pixel quantization. Extensive experiments demonstrate that DQ V2 achieves improved performance and training stability across multiple datasets, while also reducing computational complexity. The results suggest that DQ V2 provides a practical solution for data compression and coreset selection, paving the way for further enhancements in semantic-aware data augmentation and broader applications in complex visual tasks.

### Strengths
- The overall writing of the paper is smooth and easy to understand.
- DQ V2 replaces MAE-based quantization with a simple augmentation strategy, achieving better performance without pre-trained models.

### Weaknesses
 - The paper claims good scalability for the proposed method, but the experiments are still focused on smaller datasets and do not include evaluations on mainstream large-scale datasets like ImageNet-1k. The absence of such evaluations makes it difficult to ascertain the method's applicability to real-world scenarios where datasets are significantly larger and more complex.
- The coreset selection methods chosen for comparison, such as GraNd, Grad-Match, and GC, are from 2021. The paper should include comparisons with more recent coreset selection and dataset quantization methods. The current comparisons do not provide a comprehensive view of the state-of-the-art, potentially overlooking more effective techniques that have emerged since 2021. This lack of comparison with contemporary methods limits the assessment of the proposed method's true novelty and performance gains.


### Questions
The goal of DQ is to reduce training data volume and improve data efficiency. Since the proposed method uses data augmentation, does it significantly increase the dataset size, potentially resulting in similar training costs as regular training?

### Soundness
3

### Presentation
3

### Contribution
2
