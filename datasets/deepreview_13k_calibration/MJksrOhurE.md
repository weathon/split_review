# CARD: Channel Aligned Robust Blend Transformer for Time Series Forecasting

- Decision: Accept
- Avg Score: 6.25
- Scores: 8, 5, 6, 6

## Abstract
Recent studies have demonstrated the great power of Transformer models for time series forecasting. One of the key elements that lead to the transformer's success is the channel-independent (CI) strategy to improve the training robustness. However, the ignorance of the correlation among different channels in CI would limit the model's forecasting capacity. In this work, we design a special Transformer, i.e., {\bf C}hannel {\bf A}ligned {\bf R}obust Blen{\bf d}  Transformer (CARD for short), that addresses key shortcomings of CI type Transformer in time series forecasting. First, CARD introduces a channel-aligned attention structure that allows it to capture both temporal correlations among signals and dynamical dependence among multiple variables over time. Second, in order to efficiently utilize the multi-scale knowledge, we design a token blend module to generate tokens with different resolutions. Third, we introduce a robust loss function for time series forecasting to alleviate the potential overfitting issue. This new loss function weights the importance of forecasting over a finite horizon based on prediction uncertainties. Our evaluation of multiple long-term and short-term forecasting datasets demonstrates that CARD significantly outperforms state-of-the-art time series forecasting methods.\blfootnote{$*$ Equal contribution.}\blfootnote{$\dagger$ Work done at Alibaba Group, and now affiliated with Squirrel AI.}\blfootnote{$\ddagger$ Work done at Alibaba Group, and now affiliated with Meta.}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes a transformer architecture whose main feature seems to be the attention applied both across time dimension and across feature dimension.

### Strengths
- The architecture design seems novel and interesting
- Extensive ablation studies and additional results in Appendices
- I am happy to see, finally, that the transformer based paper discusses and outperforms results on basic baselines, most importantly
    - Zeng et al. Are transformers effective for time series forecasting? AAAI'23
- In general the paper seems to be well written and clear. I like the level of detail and clarity of Figures 1,2

### Weaknesses
 - The paper makes same methodological mistake as the previous line of this research. We really need to compare against basic baselines! Please include results of Zeng et al. in Table 1. Today, this is perhaps the most important baseline to include in the Table, so I'd rather not see some of the other entries in the table than to see this one missing
- The results in Table 2 are not as impressive as in Table 1. The model is not performing well compared to the first entry in the M4 competition and is barely performing better than the second entry, which is not reflected in Table 2. Again, same methodological mistake of not comparing comprehensively against basic baselines. Please include them in the table if you want to demonstrate methodological rigour and promote consistency across studies. The N-BEATS results are probably presented in the table without ensembling, but even the basic ensemble of 18 models is way better than the proposed model as follows from Figure 3 in https://arxiv.org/pdf/1905.10437.pdf. I suggest that the authors follow well accepted protocol for M4 benchmark evaluation and present the ensemble-based results, or remove Table 2 from the paper and replace it with the results of their ablation studies.

### Questions
- Please add results on ILI and Exchange to Table 1
- I flagged a few concerns and will revise my score if they are addressed appropriately

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents CARD, a particular Transformer model for time series forecasting.  CARD contains three core designs：

* A channel-aligned attention structure
* A token blend module
* A robust loss function for time series forecasting
  
The author provides extensive experiments to verify the effectiveness of the proposed method in multiple long-term, short-term forecasting and anomaly detection datasets.

### Strengths
1. The paper is well written and easy to follow, with good figures for explanation.

2. The proposed method combines various time series forecasting effective design ideas.

3. The proposed method has conducted experiments on multiple time series forecasting tasks.

### Weaknesses
Method design

The proposed approach needs more novelty. Some of the main design ideas are presented and verified by the previous work, such as channel independence, patchify, EMA, and dynamic projection technique. It is unclear how the specific combination of these existing techniques leads to a significant advancement over existing methods, especially given that some of these techniques, like dynamic projection, have not been thoroughly validated on datasets with a large number of channels.
   
Experimental rationality

* The main experimental setting needs to be consistent with the SOTA method to be convincing, and the experimental results need more justification. The current comparison with PatchTST uses different input lengths, making it difficult to assess the true performance gains of the proposed method. The use of unofficial code for comparison also raises concerns about the reliability of the results.

* The rationality of some analytical experiments needs further verification. For example, the ablation studies primarily focus on parameter changes rather than structural differences between CARD and PatchTST. Also, the experiment using 70% of the training data may not be sufficient to draw strong conclusions about the model's behavior with less data.

### Questions
1. In long-term forecasting tasks, I have questions regarding the experimental settings of the current state-of-the-art model PatchTST. The input length for PatchTST/42 is 336, and for PatchTST/64 it is 512. I am curious whether CARD can outperform PatchTST if the authors use the same input length. If you aim to validate your experimental settings, you should use the official code of the SoTA model and adjust the parameters to ensure a fair comparison.

2. Channel independence introduces a significant computational overhead. To mitigate this issue, the authors employ dynamic projection (DP) to project head dimensions from d_head to a fixed $r$ with $r ≪ C$. They demonstrate through ablation experiments involving projected dimensions of 1, 8, and 16 on ETT datasets that DP does not compromise forecasting accuracy. However, it's worth noting that ETT datasets only consist of 7 channels, which may not be sufficient to draw a definitive conclusion. Therefore, it remains unclear how this technique would perform in datasets with a larger number of variables, such as Traffic (862) or ECL (321).

3. In ablation experiments, our primary focus is on evaluating the effectiveness of the new design between CARD and PatchTST. Instead of solely changing parameters, we aim to demonstrate the method's rationality and validity with greater certainty through more detailed ablation studies.

4. In experiments with less training data, using only 70% of the training data samples compared to the standard training setting for long-term forecasting may not be sufficient.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces the Channel Aligned Robust Blend Transformer (CARD), a specialized transformer model designed for time series forecasting. It acknowledges the success of transformer models in this field, particularly due to the channel-independent (CI) strategy that improves training robustness. However, the CI approach overlooks the correlation among different channels, limiting the model's forecasting capacity. To address this limitation, CARD incorporates a channel-aligned attention structure to capture temporal correlations among signals and dynamical dependencies among multiple variables over time. Additionally, a token blend module is introduced to efficiently utilize multi-scale knowledge by generating tokens with different resolutions. The authors also present a robust loss function that considers prediction uncertainties to mitigate overfitting. Experimental evaluations on various long-term and short-term forecasting datasets demonstrate that CARD outperforms state-of-the-art methods in time series forecasting. The article concludes by discussing related work, presenting the detailed model architecture, describing the loss function design, and providing the results of numerical experiments and further analysis.

### Strengths
1. This paper introduces a novel transformer model specifically designed for time series forecasting. It addresses the limitations of the channel-independent (CI) strategy by incorporating a channel-aligned attention structure and a token blend module to capture correlations among different channels and utilize multi-scale information effectively.

2. This paper evaluates the proposed CARD model on multiple long-term and short-term forecasting datasets, comparing it against state-of-the-art methods, and demonstrates its superiority over existing techniques in various prediction-based tasks.

3. This paper introduces a robust loss function specifically designed for time series forecasting. By considering prediction uncertainties and weighting the importance of forecasting over a finite horizon, the proposed loss function addresses the potential issue of overfitting noises. This contribution enhances the model's ability to make accurate predictions.

4. This paper follows a well-organized structure. The inclusion of figures, such as the model architecture figure and experimental result figures, aids in understanding the proposed methods.

### Weaknesses
1. Experimental Concerns:

   (1) Fixed-parameter EMA: The article directly applies a fixed-parameter Exponential Moving Average (EMA) without providing specific explanations regarding the potential drawbacks of using a learnable-parameter EMA. The advantages or disadvantages of employing a learnable-parameter EMA are not thoroughly explored. Specifically, the paper lacks a discussion on how the fixed decay rate might limit the model's ability to adapt to varying temporal dynamics within different time series. A learnable parameter could potentially allow the model to dynamically adjust the decay based on the input data, which could be beneficial for datasets with non-stationary characteristics. The paper should include an ablation study that explores the performance of both fixed and learnable decay rates, and discuss the trade-offs between them.

   (2) Lack of comparison with different lookback values: The article fails to compare the results of different lookback values (the number of previous time steps considered) on the M4 dataset. Such a comparison would provide a more comprehensive analysis and insights into the impact of lookback on forecasting performance. The absence of this analysis makes it difficult to understand the sensitivity of the model to the input window size. It is essential to investigate how different lookback values affect the model's ability to capture short-term and long-term dependencies, and how this impacts the overall forecasting accuracy.

   (3) Inconsistency in short-term forecasting results: While the article highlights the third point of short-term forecasting, the visual results presented in the figures do not seem to align well with the data shown in the tables. Additionally, the evaluation of short-term forecasting appears to be limited to only the M4 dataset, which may not be sufficient to fully demonstrate the model's performance. The discrepancy between the visual and numerical results raises concerns about the reliability of the reported findings. Furthermore, the lack of diversity in the datasets used for short-term forecasting limits the generalizability of the conclusions.

### Questions
1. Presentation Aspect:
   It would be beneficial for the article to include a schematic diagram illustrating the limitations of previous models at the beginning, to better introduce the motivation and background of the study. This would help readers understand the context more clearly and provide a more coherent structure to the article.

2. Experimental concerns are listed in the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel time series forecasting method, called CARD. Compared with previous works, CARD builds an effective transformer to employ cross-channel information. CARD utilizes attention over tokens and attention over channels to robustly align the information among different channels. Furthermore, the token blend module introduces multi-scaling structural information. To bolster the model’s ability to concentrate on forecasting for the near future, this paper develops a robust signal decay-based loss function. The comprehensive experiments demonstrated the superiority of CARD for long-term forecasting, short-term forecasting, and other prediction tasks.

### Strengths
(1) The method proposed in this paper is highly effective, taking into consideration the interactions among different channels, thereby mitigating to some extent the overfitting issues commonly associated with previous channel-dependent models.

(2) The experiments are highly comprehensive, assessing the model's performance across long-term forecasting, short-term forecasting, and other prediction tasks. In addition, this paper conducts extensive ablation studies, including hyperparameter sensitivity analysis experiments, loss function analysis experiments, and so forth.

(3) The paper is generally well-written and easy to understand.

### Weaknesses
(1) The paper analyzed the complexity of the proposed model, which is an advantage. However, this paper did not specifically outline the complexities of the baseline models and there were no direct comparisons with the baselines on the running time or efficiency.

(2) Some of the experimental results are somewhat confusing. For example, in Table 18, the average performance of CARD and wo. hidden are identical, but the diffs are not 0.

(3) In the ablation study of the signal decay-based loss function, i.e. Table 12 and Table 13, I observe that the method proposed in this paper does not exhibit a significant advantage compared to the SOTA baseline without the robust loss. Furthermore, it would be better if the authors could provide test results on a broader range of datasets.

(4) The paper claims that the proposed method can effectively mitigate overfitting issues. Although some empirical analysis has been provided, supplementing with appropriate theoretical analysis would be more convincing.

### Questions
The concerns include the comparison with baselines on the complexity, the confusing experimental results, in-depth insight into the ablation study, and the theoretical analysis of how the model mitigates overfitting issues. Please see the weaknesses for details.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
