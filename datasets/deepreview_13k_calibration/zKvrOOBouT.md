# EvA: Erasing Spurious Correlations with Activations

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
Spurious correlations often arise when models associate features strongly correlated with, but not causally related to, the label e.g. an image classifier associates bodies of water with ducks. To mitigate spurious correlations, existing methods focus on learning unbiased representation or incorporating additional information about the correlations during training. This work removes spurious correlations by ``**E**rasing **wi**th **A**ctivations'' (EvA).  EvA learns class-specific spurious indicator on each channel for the fully connected layer of pretrained networks. By erasing spurious connections during re-weighting, EvA achieves state-of-the-art performance across diverse datasets (6.2\% relative gain on BAR and achieves 4.1\% on Waterbirds). For biased datasets without any information about the spurious correlations, EvA can outperform previous methods (4.8\% relative gain on Waterbirds) with 6 orders of magnitude less compute, highlighting its data and computational efficiency.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents an approach to mitigate biases learned through spurious correlations by erasing dimensions in the embedding space that are more likely to be associated with spurious features. The authors propose two metrics - namely consistency and evidence energy, for cases when additional unbiased data respectively are and are not available for training, which are used to identify spurious dimensions in the embedding space. Experiments reveal significant improvements over state-of-the-art bias mitigation approaches mainly in the absence of unbiased training data, but also to some extent when it is available.

### Strengths
1. The authors propose a post-hoc method for developing robustness to spurious correlations, which does not involve any additional training / heavy computational workload, which is a big positive in my opinion. The method operates by identifying specific dimensions in the embedding space that satisfy certain threshold criteria for some forms of spuriosity metrics proposed by the authors, dropping them from the data representations, and solving a logistic regression from this updated embedding space to the label space. None of these operations seem to be computationally expensive.

2. The authors propose ways to measure the degree of spuriosity of a specific dimension, when additional unbiased samples both are and are not available. This is a useful contribution which may also be applicable in other scenarios beyond bias mitigation.

3. The experimental results are strong. Performance improvements over state-of-the-art are quite significant on standard benchmarks, with minimal extra computational overhead.

### Weaknesses
1. The calculation of both consistency (eq. 4) and evidence energy (eq 7) are done independently for each feature dimension $i$. However, it is well known that input features do not necessarily map neatly onto independent dimensions in the feature space [a, b]. Given this, the feature erasure in eq. 9 should technically not be achieving what it claims to achieve. By turning full dimensions on/off, it could be - (i) partially turning off some core features that could be in superposition with a spurious feature; and (ii) not fully turning off spurious features, since it may be in superposition with some core feature dimension which is not turned off.

2. In computing $C_{(ik)}$ in eq. 4, there would be significant disparity in the distribution of the features stemming from sampling bias, since the number of unbiased samples is typically << the number of biased samples in practical datasets, which itself could skew the value of $d$, not providing a faithful measure of consistency. How do the authors account for this imbalance when applying the distance metric $d$?

3. Since the idea of EvA is essentially to remove dimensions from the embedding space that correspond to spurious features, an ablation for what constitutes the best approach for selecting the subspace to drop is necessary. EvA employs thresholding on consistency and evidence energy to select spurious subspaces. However, whether consistency and evidence energy are really the best metric to look at when it comes to performing this selection needs to be either theoretically or empirically established. For this, one empirical baseline could be comparison with random feature drop out in the embedding space. I would suggest the authors to explore this in further detail and consider developing such baselines to establish the optimality of their specific feature erasure mechanisms.

4. Table 5 shows that the gains from EvA are more significant in the absence of extra unbiased training data. The authors should provide a discussion on why their method might have a stronger advantage over SOTA when unbiased training data is not present.

5. When extra training data is not available, how does one perform the hyperparameter search for $\epsilon$? Additionally, when training data is available, although a single pass of EvA is computationally inexpensive, the hyperparameter sweep over $\epsilon$ may be time consuming. Discussing these, especially, the former case of selecting $\epsilon$ in the absence of an unbiased train subset is necessary.

### Questions
Please see the Weaknesses section.

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
The paper introduces a method to detect and mitigate spurious correlations learned by an image classifier. They present two measures to identify channels in the penultimate layer of the model which correspond to such spurious correlations, one of them requiring an additional unbiased dataset (“consistency”) while the other can be computed on the the training data (“evidence energy”). After identifying a set of spurious channels, the corresponding weights in the last layer are set to zero and the remaining weights (of the last layer) are retrained.

### Strengths
- computational cost are lower compared to similar methods that do not require unbiased data
- their mitigation outperforms other methods on several common spurious correlation benchmarks
- for the variant including unbiased data, the introduced method requires less samples for the same accuracy
- the procedure seems to be well motivated including theoretical analysis

### Weaknesses
 - the experiments establishing the correlation between their two measures are based only on one class of one of the datasets
- experiments are only based on small toy settings with strong spurious correlations
- the method is strongly inspired by OOD methods, but apart from a brief mention in the conclusion, this is not discussed in the main paper 

minor:  fontsize in Fig. 1, Tab. 3, Tab. 4 are too small, the definition of “energy” actually corresponds to the “free energy” which might be confusing

### Questions
In Table 5, how many runs were performed to compute mean and std, and was the same erase ratio used in all of the EvA runs?

Section 4.4 (and Fig. 3 c) discuss the effect of the erase ratio on the worst accuracy. How does this hyperparameter influence the mean accuracy?

In Table 7, mean acc and worst acc are reported for CelebA but unbiased/conflicting acc in Table 5. The results on Waterbirds suggest that your method results in a better worst acc but worse mean acc for the ResNet-50 than for the ResNet-18: Does this pattern hold on CelebA?

Given the computational efficiency and no requirement for unbiased data or annotations of the spurious correlations, it should be quite feasible to evaluate EvA-E on ImageNet scale spurious correlations benchmarks (e.g. [1],[2]). In these more realistic settings, the distinction between spurious and core features become more complex. Can you provide empirical evidence or arguments that your evidence energy measure can still be used for detection and mitigation in such settings?


[1] Singla et al., Salient ImageNet: How to discover spurious features in Deep Learning?

[2] Neuhaus et al., Spurious Features Everywhere -- Large-Scale Detection of Harmful Spurious Features in ImageNet

### Soundness
3

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
4

### Summary
Existing methods on mitigating spurious correlations typically requires unbiased data and multiple rounds of retraining. The paper proposes a computational- and data-efficient pipeline that detects spurious features before the last linear layer. When there is no unbiased datasets, the contribution of each feature to the network’s prediction
confidence is exploited for detection.  If the unbiased data is available, the consistency of penultimate activations between spurious and unbiased datasets is used for detecting spurious features.  Through channel-based erasure and re-weighting on the final linear layer, reliance on spurious correlations can be effectively mitigated.

### Strengths
- Two practical methods, namely EvA-C and EvA-E, are proposed for detecting and mitigating spurious features in the penultimate activations, depending on the existence of an unbiased dataset. The two proposed methods are both efficient and effective in mitigating spurious correlations.

- The two metrics originate from the spurious feature detection methods can be used to measure the spuriousness of features from the penultimate layer of a model. These metrics are also useful to validate the effectiveness of spurious correlation mitigation methods.

### Weaknesses
 - Contrary to the claim in Line 93, the performance of the proposed method is not the state-of-the-art in comparison with some methods [1,2]. For example, with ResNet50 as the backbone, EvA-E has a worst-group accuracy of 86.6% (Table 7), while [2] achieves 89.1%.

- The unbiased dataset $\mathcal{D}_{\text{unbiased}}$ is first introduced in Line 156; however, it is unclear what $\mathcal{D}_{\text{unbiased}}$ can be considered as "unbiased". Based on the descriptions in Line 230 and Line 312, $\mathcal{D}_{\text{unbiased}}$ is selected from the validation set. In some datasets, such as CelebA, the validation set also has gender bias. If $\mathcal{D}_{\text{unbiased}}$ is defined as a set of group-balanced data where each class of samples distribute equally across different spurious features, then group annotations are required to obtain $\mathcal{D}_{\text{unbiased}}$, contrary to the claim in Line 50-51. Further clarification on this point would be beneficial.

- In Eq. (4), why the unknown test distribution $\phi_{\text{test}}^{ik}$ can be approximated via $\phi_{\text{unbiased}}^{ik}$? In some datasets such as CelebA, the test set is also biased. It would be helpful to further clarify this point.

- The experimental results for DFR on the Waterbirds dataset (Table 1) are significantly lower than those reported in the original DFR paper. This discrepancy needs to be addressed to ensure the validity of the comparisons.

- For EvA-E, the method relies on a threshold to erase certain weights, and the selection of this threshold is critical to the method's effectiveness. The paper does not provide sufficient detail on how this threshold is determined, and the potential bias in the validation data used for threshold selection is a concern, especially for datasets like CelebA.

- For EvA-C, while the method shows improved performance compared to DFR, the paper lacks a detailed explanation of why this is the case. Both methods utilize an unbiased dataset for retraining, yet EvA-C demonstrates superior results. A more in-depth analysis of the underlying reasons for this difference is needed.

### Questions
- Why spurious features often lead to high confidence predictions?
- Can the proposed method used for other model architectures beyond convolutional neural networks?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes EVA, a method for addressing spurious correlations in datasets. It identifies spurious features using a consistency measure and the evidence energy measure in scenarios with and without unbiased datasets, respectively. Theoretical analyses are provided regarding the relationship between these two measures and a feature’s spuriousness. Experiments are conducted to demonstrate the method's effectiveness.

### Strengths
- The method is well-motivated, and I appreciate its simplicity (in terms of both understanding and computation).
- Providing theoretical analysis adds a more principled foundation to the two measures.
- There are experiments showing that the erased features are indeed the spurious ones on CMNIST, and the correlation between evidence energy and consistency, which further supports that the method works as expected.

### Weaknesses
 - Since the original DFR paper uses ResNet50 as the architecture, it would be a good sanity check to compare results in that same setting. The authors provided results for ResNet50 in Appendix E.2, but they mention that, to mimic real-world scenarios, they tuned hyperparameters based on Mean Accuracy instead of Worst Accuracy. This might be debatable, as the setting where DFR is applicable assumes an unbiased validation set. Additionally, I wonder if the setup is consistent between ResNet18 in the main paper and ResNet50 in the appendix for the Waterbirds dataset. Could you clarify whether hyperparameters for ResNet18 were tuned based on Mean Accuracy or Worst Accuracy?
- Overall, since most existing papers evaluate their methods on ResNet50 while this paper primarily uses ResNet18 (this makes the numbers not comparable to those reported in other papers; in general, the numbers are much lower for all methods than those in the literature potentially due to the architecture), and some baselines (e.g., JTT, SSA [1], AFR [2], and [3]) are not included in the main table, Table 5, it is hard to compare the proposed method to the state of the art and to assess whether it truly stands out among existing techniques. For example, I wonder if the proposed method can outperform JTT on the Waterbirds dataset when ResNet50 is used, which has a reported worst-group accuracy of 86.7%, a relatively high value compared to the numbers in this paper obtained on ResNet18.
- Perhaps a detailed discussion and comparison with [1] is necessary, given that it also achieves the same goal: lightweight reweighting of the last layer without group labels.

### Questions
See the questions raised in the Weaknesses section.

### Soundness
2

### Presentation
3

### Contribution
2
