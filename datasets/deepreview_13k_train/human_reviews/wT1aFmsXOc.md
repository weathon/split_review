# Understanding and Mitigating Memorization in Diffusion Models for Tabular Data

- Decision: Reject
- Scores: 6, 6, 3, 5

## Abstract
Tabular data generation has attracted significant research interest in recent years, with the tabular diffusion models greatly improving the quality of synthetic data. However, while memorization—where models inadvertently replicate exact or near-identical training data—has been thoroughly investigated in image and text generation, its effects on tabular data remain largely unexplored. In this paper, we conduct the first comprehensive investigation of memorization phenomena in diffusion models for tabular data. Our empirical analysis reveals that memorization appears in tabular diffusion models and increases with larger training epochs. We further examine the influence of factors such as dataset sizes, feature dimensions, and different diffusion models on memorization. Additionally, we provide a theoretical explanation for why memorization occurs in tabular diffusion models. To address this issue, we propose TabCutMix, a simple yet effective data augmentation technique that exchanges randomly selected feature segments between random training sample pairs. Experimental results across various datasets and diffusion models demonstrate that TabCutMix effectively mitigates memorization while maintaining high-quality data generation. Our code is available at \url{https://anonymous.4open.science/r/TabCutMix-3F7B}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focused on the problem of *memorization* (overfitting) for diffusion model used on tabular data.

The paper is organized as a sequence of questions, with experiments to answer them, namely:
- Does memorization occur in tabular diffusion models, and if so, how can it be effectively mitigated?
- Effect of diffusion model, impact of dataset size.
- Feature dimension.

The paper demonstrates that:
1) Memorization occurs at similar regardless of algorithm used, which suggests the origin lies in the diffusion itself. This is confirmed by Proposition 3.1.   
2) Weirdly, dataset size has no impact on this, or surprising impoact.
3) Feature dimension is important, having influence in both directions depending on the dataset.

Author propose a simple augmentation technique (TabCutMix) that mixes the columns features of two examples to create a new one. Empirically, this technique reduces memorization. Authors measure Precision/Recall/Shape and Trend score of the diffusion model trained on augmented data, and show that this does not have too detrimental effects on these metrics, which suggests the practical efficiency of the method. A visual sanity check is performed using T-SNE.

### Strengths
### Simplicity

The method is extremely simple, since it is essentially just a data-augmentation technique done at the pipeline level. The contribution could even look "too simple" if it wasn't for all the experiments and sanity checks, which are convincing . 

### Methodology and clarity

The paper is structured as a set of questions, experiments to answer these questions, and empirical observations. Not only it improves clarity but also makes the paper impactful and useful in its own, outside the technical contribution of the data-augmentation.  

### Sanity checks

Author monitor several metrics to ensure that the diffusion model trained with the data-augmentation is still faithful to training data, which is crucial to ensure the relevance of the diffusion model in this context. It is not hard to ensure diversity of a generative model, the difficulty lies in balancing this diversity with the recall of the true distribution. 

### Theoretical results

The theoretical results give valuable insights on the experiments, creating a consistent narrative.

### Weaknesses
### Limitations

I feel like a discussion on limitations is lacking. This data-augmentation changes the input distribution, like any data-augmentation.  For image space, data-augmentation like symmetries comes from a prior over the structure of the input space, other ones like CutMix produces OOD data that act like regularization.

TabCutMix is doing an implicit hypothesis on the structure of the data manifold.

Let me resurrect the infamous "XOR problem" of neural networks. Assume we are given a dataset with two numerical features $(x_1, x_2)$ and one categorical feature $c\in\{+,-\}$. Assume that the "class" $c$ is $\text{sign}(x_1x_2)$. i.e, class will be $+1$ if the two feature have the same sign, and negative otherwise. This classification task effectively splits the dataset into four quadrants around the origin $0$, with a XOR pattern. Applying TabCutMix on this problem will mixes the two distributions $c=+1$ and $c=-1$, and they will completely overlap.  

Therefore, this method is at high risk of creating OOD data that might overlap the categories. If such diffusion model is used for downstream tasks, this can be problematic as it will not reflect the real data distribution.

### Questions
1) I was surprised by Obs 2 of Sec 3.2. Do you have an idea of why the memorization ratio is independent of the diffusion model used?

2) I was puzzled by Obs 2 of Sec 3.3. I would expect smaller dataset to yield higher memorization rates (easier overfitting). Why is it not changing on some datasets? I suspect that the definition you use in l230 is biased in this regard: since it relies on distance ratio, smaller datasets leads to more sparsely populated space, so absolute distances are increased but *maybe* relative distances remain unchanged. I am not sure how it plays with the curse of dimensionality though, as I would expect any criterion based on euclidean distance to become irrelevant in high dimension.

3) Can authors comment on the implicit hypothesis TabCutMix does about data manifold, explicit cases in which it might "fail" by creating OOD data, and explicit cases in which they expect it to perform well? Even better, a practical example of a dataset on which the method failed.

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
The paper investigates the phenomenon of data memorization in diffusion models for tabular data generation, highlighting how memorization can lead to privacy issues and reduced generalization in models. The study introduces a criterion based on nearest-neighbor distance ratios to quantify memorization, revealing that diffusion models, such as TabSyn and TabDDPM, tend to memorize training data, especially as training epochs increase. This memorization is influenced by dataset size and feature dimensions, with smaller datasets often leading to higher memorization levels. The paper further provides theoretical insights into the mechanisms behind memorization in tabular diffusion models, showing how specific model configurations and training processes contribute to this effect.

To mitigate memorization, the authors propose TabCutMix, a post-processing technique inspired by the CutMix approach in image processing. TabCutMix randomly swaps feature segments between samples within the same class, preserving label integrity while introducing diversity in the synthetic data. This approach effectively disrupts memorization tendencies by reducing the exact resemblance between generated samples and training data. Experimental results demonstrate that TabCutMix significantly reduces memorization across multiple datasets and model configurations, while also maintaining key aspects of data quality, including fidelity and the overall statistical distribution of features. The approach achieves a balance between mitigating memorization and preserving data utility for downstream tasks.

### Strengths
+ The paper addresses a critical issue of data memorization in deep generative models for tabular data, where privacy risks from memorization could pose greater harm compared to the image and language domains.
+ It offers a comprehensive examination of the latest state-of-the-art generators, filling a gap in prior work that lacks focus on tabular data generation models.
+ The paper provides clear motivation and detailed descriptions of its memorization metrics and the proposed post-processing technique, TabCutMix, enhancing understanding and applicability of the methods introduced.

### Weaknesses
 + Choice of Memorization Metric: The tabular synthesis field has widely adopted distance-based metrics to assess privacy leakage, with impactful works such as Platzer et al. using the ratio of synthetic examples closer to the training set than the test set. The proposed method uses a variant of l2 distance-based approach but does not sufficiently discuss why this particular metric is superior to standards l2 distance. The proposed metric may still suffer from issues such as sensitivity to outliers, a limitation common to other distance-based measures.
+ Limited Dataset Benchmarking: The small number of datasets used for evaluation may be insufficient to conclude consistent patterns in memorization.
+ Effectiveness of TabCutMix Post-Processing: In tabular data synthesis, the trade-off between utility and privacy (or memorization reduction) is well established, with increased perturbation leading to lower memorization but reduced data fidelity. To validate TabCutMix’s usefulness, the paper should compare it to other established “shallow” perturbation techniques, such as SMOTE or Mixup, to better illustrate its advantages.

### Questions
+ Please compare the proposed mixed-distance against l2 distance with one-hot encoding for categorical variable, and explain the essential difference between the two metrics.
+ In the experiment for Table 1, test post-processing using SMOTE[1] and Mixup for tabular data[2] in addition to TabCutMix. 
+ In the cased study: does the resulting sample of TabSyn + TabCutMix now closely resemble another real example? Or is the distance to close real example increased? 
+ The tested dataset have 10k+ samples and are still fairly large with 10% subsampling. Does the same behaviors hold for more realistic small-scale dataset with <= 200 samples? Consider repeating the analysis in section 3 on the following benchmarking datasets: Insurance, Indian Liver Patient, Titanic, Obesity. You can also try smaller subset percentages such as 0.1%, 1%

Reference: 
[1] Chawla, Nitesh V., et al. "SMOTE: synthetic minority over-sampling technique." Journal of artificial intelligence research 16 (2002): 321-357.
[2]Takase, Tomoumi. "Feature combination mixup: novel mixup method using feature combination for neural networks." Neural Computing and Applications 35.17 (2023): 12763-12774.

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
This paper studies the memorization issue in the diffusion model for tabular data generation. Memorization is defined as present when the distance between a synthesis data sample and the first closet sample in the training dataset is less than one-third of the distance with the second closest in the training dataset. Using this definition of memorization, the authors find that TabSyn exhibits different levels of memorization across different datasets. To reduce memorization, this paper proposes TabCutMix, which first produces new samples by randomly swapping features between two training samples with the save target label, then append the new samples to the original training dataset.

### Strengths
1. This paper is in general well-written and easy to read.
2. This paper studies an important but under-explored potential issue in applying the diffusion model for tabular data generation.
3. The theoretical result, which shows that perfectly trained diffusion models will generate memorized latent representation, is interesting.  Although due to the randomness in the sampling process, this theory does not prove memorization must happen, it reveals enough potential of memorization.

### Weaknesses
1. **Flawed method**: The proposed method TabCutMix produces new samples by swapping features between two randomly selected training samples with the same target label. My biggest concern is this procedure will contaminate the pair-wise correlation in the training dataset. Therefore, I am skeptical about the Trend Score in Table 1, which shows applying TabCutMix has very little effect on the pairwise correlation, which is pretty counter-intuitive.  I am willing to raise my score if the authors can clarify this issue.

2. **Missing discussion with previous memorization metrics**: In TabSyn, the authors actually also study a memorization metric: Distance to Closest Records (DCR), which measures the distance of the generated samples w.r.t to training and a held-out dataset. It is necessary to compare and discuss the difference and connection between the proposed memorization metric with DCR. Also, the new proposed memorization metric uses a pre-fixed 1/3 as the threshold, although it has been used in previous works on generating images. It may not be reasonable to directly adapt it to tabular data, which is a different modality. Fig 5, which plots the distribution of the ratio, contains more information than Fig 2,3,4, which use a fixed threshold. However, as shown in Fig 5, the improvement from TabCutMix looks very marginal, again raising doubts about the effectiveness of the proposed method.

3. **Weak experiment**: 
1) Datasets: This paper considers TabSyn and TabDDPM as the base diffusion model to reduce memorization. In TabSyn, the experiment is conducted on 7 datasets, and in TabDDPM, 15 datasets are used. However, in this paper, experiments are done on only 4 datasets, which significantly harms the convinceness.   
2) Fidelity metric: C2ST metric used in TabSyn is not included in this paper.

### Questions
See the weakness section.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
- The authors introduce TabCutMix, a data augmentation strategy to mitigate memorization in Tabular diffusion models.
- TabCutMix operates by combining samples that belong to the same label class. They claim that “The feature swap within the same class increases data diversity and reduces the likelihood of memorization while preserving the integrity of the label.”.

### Strengths
**Originality & Significance**

The paper tackles the memorization issue in tabular diffusion models, which has been underrepresented in recent research.

**Quality**

Visualizations are nice to understand the experiments.

**Clarity**

Paper is clear and well-written.

### Weaknesses
 - L233: Figure 4 — Which features are you removing specifically for the examples? The features you remove can potentially affect the memorization ratio. For instance, in [InterpreTabNet](https://arxiv.org/abs/2406.00426), salient features contribute more towards predictions. Thus, features that are salient could potentially have a larger impact on the memorization ratio. Another example could be looking at the correlation between features. Would removing highly correlated features be more impactful on the memorization ratio than less correlated features?
- L235: Theoretical Analysis in this section and the referred appendix is nice but trivial. The following information could be inferred from the [EDM paper](https://arxiv.org/abs/2206.00364) which is what TabSyn uses. Additionally, there is no citation of the EDM paper either.
- L286: The methodology is naive. One example is when there is a violation of feature dependencies — In the Adult dataset, Education and Education-Num are related. Swapping one without the other can create inconsistent samples.
- L319: Datasets seem to be very limited in the current standard, with only 4 included datasets. The referenced TabSYN and TabDDPM in the paper included 6 and 16 datasets in total respectively.
- The overall methodology seems to be lacking in terms of contribution, proposing a trivial data augmentation technique that reduces memorization via an adaptation of CutMix from the image domain to tabular data.
- There are also numerous established data augmentation techniques for tabular data (e.g., [SMOTE](https://arxiv.org/abs/1106.1813), noise injection) that serve similar purposes. The paper does not clearly differentiate TabCutMix from these methods or demonstrate significant advantages.
- It seems that TabCutMix can also be applied to other forms of generative models. I am unable to determine the reason that it is only generalizable to diffusion models.

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
4

### Contribution
2
