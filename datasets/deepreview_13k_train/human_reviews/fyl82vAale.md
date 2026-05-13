# Sequential Order-Robust Mamba for Time Series Forecasting

- Decision: Reject
- Scores: 5, 5, 6, 6, 5, 6

## Abstract
Mamba has recently emerged as a promising alternative to Transformers, offering near-linear complexity in processing sequential data.
However, while channels in time series (TS) data have no specific order in general, recent studies have adopted Mamba to capture channel dependencies (CD) in TS, introducing a 
\textit{sequential order bias}.
To address this issue, we propose SOR-Mamba, a TS forecasting method that 1) incorporates a regularization strategy to minimize the discrepancy between two embedding vectors generated from data with reversed channel orders, thereby enhancing robustness to channel order, and 2) eliminates the 1D-convolution originally designed to capture local information in sequential data.
Furthermore, we introduce channel correlation modeling (CCM), a pretraining task aimed at preserving correlations between channels from the data space to the latent space
in order to enhance the ability to capture CD.
Extensive experiments demonstrate the efficacy of the proposed method across standard and transfer learning scenarios.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes SOR-Mamba to solve the sequential order bias introduced by mamba capturing channel dependencies. Model SOR-Mamba incorporates a regularization strategy to minimize the distance between embeddings from data and reversed data and eliminates the 1D-convolution in the original Mamba block. And a pretraining task channel correlation modeling is introduced to preserve the channel correlation from the data space to the latent space. The effectiveness of the proposed method is demonstrated by the extensive experiment results.

### Strengths
* This paper uses a single unidirectional Mamba with regularization and non-1D convolutions to capture channel correlations. By modifying the traditional Mamba module, it can better address the issue of sequential order bias. The research problem is clearly defined, and the solution is reasonable. And the pretraining task channel correlation modeling also enhances the model's generalization and performance.

* The details of the model are mostly clear, with each module explained and supported by equations. The experiments  include time series forecasting, transfer learning and many ablation studies to validate the effectiveness of each module.

### Weaknesses
 * The proposed method is mostly constructed on existing models -- reverse modeling has been widely used in literature and removing the 1d-conv is trival.
* The experimental results show that the model's performance improvement across various datasets is not significant, mostly in the thousandth.
* The removal of 1D-conv negatively impacts PEMS dataset in tale 7 and figure 5. The necessity to remove 1D-conv is uncertain.
* The model uses the Mamba backbone, but the baseline only includes a single Mamba model: S-Mamba. Providing more models from the Mamba framework for comparison would be better.

### Questions
* When randomly shuffling the channel order, how is it done? Is a fixed shuffling method used for all sequences in a dataset, or is it shuffled randomly each time?
* In the last row of Table 1, is the calculation formula written incorrectly?

### Soundness
3

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
2

### Summary
This paper introduces SOR-Mamba, a time series forecasting method that addresses the sequential order bias  while capture channel dependencies in Mamba, through a regularization strategy to minimize the discrepancy between two embedding vectors generated from data with reversed channel orders, and 1D-convolution removal, The authors also propose Channel Correlation Modeling (CCM) as a pretraining task.

### Strengths
1. Clear problem identification regarding Mamba's limitations in handling unordered channels
2. Comprehensive experiments
3. Improved efficiency compared to other approaches

### Weaknesses
 **Limited Technical Novelty**:
- The regularization strategy is overly simplistic that minimizing the distance between embeddings from different channel orders
- The removal of 1D-conv lacks theoretical justification and appears to be an ad-hoc solution, As shown in Figure 5 of the paper, its removal may negatively impact datasets with ordered channels such as PEMS datasets

### Questions
1. In the Manba architecture, are there other advances in order-invariant architectures that can be compared?
2. The definition of sequential order bias in Figure 4 and how it is calculated?

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
3

### Summary
This paper addresses a limitation in applying Mamba to time series forecasting: the sequential order bias when modelling channel dependencies, as channels typically lack inherent order. The authors propose SOR-Mamba, which introduces two main innovations: a regularization strategy that minimizes discrepancy between embedding vectors from reversed channel orders, and the removal of the unnecessary 1D-convolution layer. They also introduce Channel Correlation Modelling (CCM), a pretraining task that preserves channel correlations from data space to latent space. The method reported promising performance across different scenarios, including cases with missing data and varying channel orders, while maintaining computational efficiency in terms of memory and runtime.

### Strengths
The proposed method addresses the sequential order bias in channel dependencies (CD). This bias can degrade performance when channels lack inherent order in multi-channel time series data. The SOR-Mamba method mitigates this bias by introducing a regularization technique that minimizes the discrepancy between embeddings generated from reversed channel orders, thus improving robustness. 

Additionally, the paper proposes Channel Correlation Modeling (CCM) as a pretraining task, which preserves channel correlations from data to latent space, enhancing CD capture. The architecture modifications, including removing the 1D-convolution and focusing on unidirectional Mamba, can reduce computational overhead, achieving efficiency gains in memory and parameter usage compared to other models like S-Mamba. This should be of interests to the group of readers working on multi channel time series data forecasting.

### Weaknesses
The paper’s approach is relatively complex, involving several architectural changes (e.g., removing 1D-convolutions, applying specific regularization, and adding CCM pretraining) that may complicate replication and limit accessibility. 

While it emphasizes efficiency improvements, the paper could provide more detailed explanations regarding the trade-offs involved in removing the 1D-convolution, especially on datasets where channel order may have some inherent structure (e.g., traffic data). The study also lacks a comprehensive discussion of potential limitations in real-world deployment, such as sensitivity to hyperparameters (e.g., λ in regularization) and its impact across different datasets.

### Questions
1. How does the choice of the distance metric d in the regularization term impact the model's performance across datasets with varying levels of channel correlation? - is the regularization term’s effectiveness dependent on the number of channels or dataset-specific factors etc.?

2. The paper uses CCM to preserve channel correlations in the latent space during pretraining. How does CCM compare to masked modelling and reconstruction pretraining across different dataset sizes and channel configurations? - and is there any limitation of CCM if there's only exist weak channel correlations?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This manuscript proposes an algorithm to regularize bidirectional Mamba channel vectors in order to solve the problem that there is no intrinsic order relationship between channels in time series data. The authors also design a new pre-training method (CCM) to help the model better establish the association between channels of multi-dimensional time series. Extensive experiments and ablation experiments are conducted, and the experimental results show the effectiveness of the relevant contributions.

### Strengths
1. This study achieves a good improvement in results with only a few changes to the method. The proposed method is simple, novel and effective.
2. The experiments carried out by the authors are very detailed and the relevant parameters are well discussed. This is an experimentally rigorous and solid study.
3. The manuscript is well-written and the figures are clear and intuitive.

### Weaknesses
1. The authors lack a complete description of the motivation for regularization. Why regularizing the bidirectional mamba channel vectors and minimizing the distance between them can help the model better capture the correlation between channels? This requires the author to give a more intuitive and reasonable motivation. Specifically, it's unclear why enforcing similarity between channel representations derived from forward and reverse processing would inherently lead to better channel correlation modeling. The manuscript should elaborate on the theoretical underpinnings of this approach and provide a more detailed explanation of the mechanism by which this regularization achieves its intended effect.
2. Although the authors have done a lot of experiments, they lack experiments on longer input lengths. Some widely used baselines in this field, such as PatchTST (arXiv preprint arXiv:2211.14730, 2022.), all use longer input sequences. The absence of experiments with longer input sequences limits the generalizability of the findings, especially given that many real-world time series applications involve extended temporal dependencies. The authors should include experiments with input lengths comparable to those used in state-of-the-art methods to demonstrate the robustness of their approach.
3. The authors use too many abbreviations in their manuscripts and experimental result tables, and lack clear and complete explanations of the abbreviations. This makes the relevant content very difficult to read and easily confusing. The excessive use of abbreviations, particularly those not universally recognized, hinders the readability and accessibility of the manuscript. A complete list of abbreviations should be provided at the beginning of the manuscript, and the authors should consider using full terms instead of abbreviations in the main text to improve clarity.

### Questions
1. Table I.1 seems to show that the hyperparameter lambda does not affect the results. Is this a reasonable phenomenon for the key contribution?
2. What are the principles and motivations for using parameter-sharing CD-Mamba block and removing 1D-conv? Can the authors provide additional details?
3. The description of the pre-training method used in this study is somewhat vague. Can the authors supplement the algorithm flow or provide detailed explanation?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduce a new Mamba-based model for long term time series forecasting named SOR-Mamba which utilizes modified Mamba structure to capture channel dependencies. Furthermore, the authors also introduces channel correlation modeling as a pretraining task aimed at enhancing the ability to capture channel dependencies.

### Strengths
1. The proposed SOR-Mamba uses a modified Mamba structure (also with a regularization strategy) to eliminate the sequential order bias of Mamba which is more useful in capture channel dependencies.
2. The authors also introduce a pretraining task named channel correlation modeling (CCM) to preserve correlations between channels from the data space to the latent space in order to enhance the ability to capture CD.

### Weaknesses
1. Since Mamba is a sequential-based model, and the channels lake sequential order, why we need Mamba to extract channel dependencies? It is important to clarify the importance of capturing channel dependencies with Mamba.
2. The experimental comparisons appear unfair, as models like PatchTST exhibit better performance with longer lookback window. I strongly suggest the authors conduct additional experiments, such as setting $L=336$.

I find that the performance of SOR-Mamba is worse than the results of PatchTST. In addition, CD models perform worse than CI models on ETT datasets (maybe weather has the same results), because CD models capture spurious cross-variable feature which i think is a more important question to be solved. In addition, I think the only problem of this work is its motivation. Simply citing previous work (which is even just follow Mamba) cannot convince me. Therefore, the author needs to reorganize the motivation and importance of this work. And I guarantee that I am familiar with this field. I hope the author do not try to just show the advantages of this work (such as better performance on ecl and traffic, but unstable performance on ETTs). I think the experimental results are not important. What is important is the problem that this work is going to solve.

Finally, my purpose is to make this work better, not to reject it. Therefore, I encourage the author to think carefully about the motivation of this work, and i am glad to discuss with the author.

I still think the motivation of using Mamba to capture cross-channel dependencies is unconvincing. Additionally, it would be beneficial to evaluate the impact of the lookback window on other datasets, such as ETTH1.

I do not think "using mamba to capture CDs" is a natural extension, because mamba is a sequence-based model, thus i believe it is not necessary to capture cross-variable dependencies. In addition, i find that the performance of SOR-Mamba is worse than the results of PatchTST.

### Questions
See Weaknesses above.
3. In line 369-370, I’m curious about how to calculate the global correlation.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
In this manuscript, the authors claim that channels in time series (TS) data have no specific order in general, recent studies have adopted
Mamba to capture channel dependencies (CD) in TS, introducing a sequential order bias. To address this issue, the authors propose SOR-Mamba, a TS forecasting method that 1) incorporates a regularization strategy to minimize the discrepancy between
two embedding vectors generated from data with reversed channel orders, thereby enhancing robustness to channel order.

### Strengths
1. The authors propose SOR-Mamba, a TS forecasting method that handles the sequential order bias by
1) regularizing the unidirectional Mamba to minimize the distance between two embedding vectors
generated from data with reversed channel orders for robustness to channel order.
2. The authors introduce CCM, a novel pretraining task that preserves the correlation between channels from
the data space to the latent space, thereby enhancing the model’s ability to capture CD.
3. With the exception of the power-related datasets (ETTm1 & m2, etc.), the experimental performance exceeds the current SOTA.

### Weaknesses
1. It is puzzling why the authors mention 'robust' but does not give experiments to resist noise or PGD attacks. Or it may be necessary to modify the terminology in the manuscript to be more precise, after all, 13 different domains of time series prediction tasks have been tried. The term 'robust' is typically associated with a model's ability to maintain performance under various perturbations, such as input noise or adversarial attacks. The current manuscript only addresses channel order, which is a specific type of input variation. The authors should either broaden their experiments to include more standard robustness tests or clarify that their use of 'robust' is limited to channel order variations.
2. With the exception of the power-related datasets (ETTm1 & m2, etc.), the experimental performance exceeds the current SOTA. Why is the performance of the author's scheme inferior to SOTA (i.e., PatchTST) on power-related datasets (ETTm1 & m2, etc.) with more significant global regularity? The authors should provide a more detailed analysis of why their method underperforms on these datasets, particularly since these datasets exhibit strong global patterns which should be beneficial for time series models. A discussion of the specific characteristics of these datasets that might hinder the proposed approach is needed. It would be beneficial to investigate if the regularization strategy is less effective for datasets with strong global regularity, or if the model architecture is not well-suited for these types of patterns.
3. Despite the computational complexity comparison, the reviewer is concerned about the actual training and inference time. While the authors provide a theoretical analysis of computational complexity, it is crucial to also present empirical results for training and inference time. This is particularly important for practical applications, where real-world performance is often more relevant than theoretical complexity. The authors should include a detailed breakdown of the actual time required for training and inference on different datasets, potentially comparing it to other methods.
4. The description in Figure 1 seems to be the difference between different exogenous time series due to sampling frequency and periodic change rule, and the description of sequence order is prone to misunderstanding (i.e., covariables have orders). The current description of sequence order in Figure 1 is ambiguous and could be misinterpreted as referring to the order of exogenous variables. The authors should clarify that the sequence order refers to the channel order within a single time series, not the order of different time series or covariates. A more precise explanation of how channel order affects the model's performance is needed.

### Questions
Please see weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
