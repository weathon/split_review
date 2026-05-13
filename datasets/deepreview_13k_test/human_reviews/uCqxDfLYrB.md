# Towards Neural Scaling Laws for Time Series Foundation Models

- Decision: Accept
- Scores: 6, 6, 5, 8

## Abstract
Scaling laws offer valuable insights into the design of time series foundation models (TSFMs). However, previous research has largely focused on the scaling laws of TSFMs for in-distribution (ID) data, leaving their out-of-distribution (OOD) scaling behavior and the influence of model architectures less explored. In this work, we examine two common TSFM architectures—encoder-only and decoder-only Transformers—and investigate their scaling behavior on both ID and OOD data. These models are trained and evaluated across varying parameter counts, compute budgets, and dataset sizes. Our experiments reveal that the log-likelihood loss of TSFMs exhibits similar scaling behavior in both OOD and ID settings. We further compare the scaling properties across different architectures, incorporating two state-of-the-art TSFMs as case studies, showing that model architecture plays a significant role in scaling. The encoder-only Transformers demonstrate better scalability than the decoder-only Transformers, while the architectural enhancements in the two advanced TSFMs primarily improve ID performance but reduce OOD scalability. While scaling up TSFMs is expected to drive performance breakthroughs, the lack of a comprehensive understanding of TSFM scaling laws has hindered the development of a robust framework to guide model scaling. We fill this gap in this work by synthesizing our findings and providing practical guidelines for designing and scaling larger TSFMs with enhanced model capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper analyzes two common TSFM architectures -- encoder-only and decoder-only transformers -- in terms of both in-distribution and out-of-distribution data. The results show that encoder-only can better scale to both ID and OOD data. The authors also show that specific architecture choices in existing TSFMs could negatively affect OOD generalization.

### Strengths
1. The paper flows very well and is easy to follow.
2. While most existing TSFMs for forecasting choose a decoder-only structure, this paper presents new findings on the encoder-only versus decoder-only that contradicts prior findings, and analyzed it from the scope of OOD data.

### Weaknesses
1. Evaluation setup could be improved. On line 130, "This subset includes test data from the ETTh1-2, ETTm1-2, electricity, and weather datasets." Are these the only datasets that are used as OOD test data throughout all the experiments? To strengthen your findings, I suggest varying the OOD datasets (maybe include a confidence interval), and see if your findings still hold.
2. The paper could benefit from explaining why its findings are different from those of the existing works.

### Questions
1. For the training details on line 183, I am not sure if I understood correctly. If one dataset is much larger than the other datasets, are we much more likely to sample from this dataset? Is there a cap to this likelihood? In existing works such as MOIRAI and Timer, they apply some threshold that prevents a large dataset from dominating from the training distribution. In addition to "Domain Balancing" as mentioned in Appendix A in your paper, I think balancing the datasets within each domain should also be helpful. Could you compare the different data mixing strategies?
2. Why does OOD have a larger exponent for MAPE than ID in Figure 2 and 3, but not for log-likelihood? It feels to me that it might be due to the type of data distribution you have.
3. In Timer, the findings are decoder-only scales better than encoder-only. Could you explain why your finding is different? In Timer, the batch size is chosen to be 8192, but you only used a batch size of 128. Is it possible that using a larger batch size would change your observations and make the decoder-only model more favorable?
4. Did you try retraining MOIRAI/Timer/Chronos using your filtered dataset? The dataset mixture is often a very important factor. Not using the same pretraining datasets can be an unfair comparison in Section 3.2.
5. "Scaling-laws for Large Time-series Models" suggests that model size has a big impact on the optimal learning rate. What learning rate did you use and how did you change it for different model sizes? Are the observations consistent for encoder-only and decoder-only models?

Minor:
- "Lotsa" should be capitalized on line 94.
- "Sum" in Table 1 is a bit confusing. Consider replacing it with "Total" and use a vertical line to separate it from previous columns.
- In Figure 2 and 3, consider adding ID and OOD to the legend, in addition to using the colors.
- Line 794: "and Covid19_Energy datasets", the underscore here seems to be a typo?
- "Scaling-laws for Large Time-series Models" suggests that using a separate head for each distribution parameter should stabilize training. 
- Could you add an experiment to show the benefit of using student-T mixture versus gaussian mixture?

Overall, I believe the findings in this paper will be very helpful to the community. I will raise my score if my concerns regarding the training and evaluation setups are addressed.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
8648_Towards_Neural_Scaling_La
pdf
LT
Here is a new  paper, please read it in its entirety, and help me to write the review, first, you should:
Summary*
Briefly summarize the paper and its contributions. This is not the place to critique the paper; the authors should generally agree with a well-written summary.


2 / 2

Summary

This paper investigates the scaling laws of time series foundation models (TSFMs) across different data distributions and model architectures. The authors train encoder-only and decoder-only Transformer-based TSFMs with varying model sizes, compute budgets, and dataset sizes. They evaluate the models' performance on both in-distribution (ID) and out-of-distribution (OOD) data.

The key findings and contributions of the paper are as follows:

The log-likelihood loss of TSFMs exhibits similar scaling behavior in both OOD and ID scenarios, following a power law with respect to model size, compute resources, and dataset size.
When evaluated using MAPE, the scaling of all three factors (model size, compute, and data) results in greater improvements in OOD performance compared to ID performance.
Encoder-only Transformers demonstrate better scalability than decoder-only Transformers, although both architectures show similar scaling trends.
The architectural modifications introduced in two state-of-the-art TSFMs, Moirai and Chronos, primarily improve ID performance but compromise OOD scalability compared to the baseline models.
The paper provides practical design principles for TSFMs from the perspective of data, model, and compute scaling, based on the findings and comparative analysis.
Overall, this work extends the understanding of scaling laws for TSFMs from ID to OOD scenarios and across different model architectures. The authors establish a foundation for predicting the expected performance gains of TSFMs and offer insights for designing scalable TSFMs.

### Strengths
1. The study extends the existing research on scaling laws for TSFMs in a novel direction by investigating their behavior across different data distributions (ID and OOD) and model architectures. While previous works have primarily focused on ID scenarios, this paper breaks new ground by systematically examining the scaling properties of TSFMs in OOD contexts. Furthermore, the comparative analysis of encoder-only and decoder-only Transformers, as well as the inclusion of state-of-the-art TSFMs (Moirai and Chronos), provides original insights into the impact of model architecture on scalability.
2. The methodology employed in this study is sound and comprehensive. The authors train a wide range of models with varying sizes (from 10^3 to 10^8 parameters), compute budgets, and dataset sizes. They evaluate the models' performance using appropriate metrics such as log-likelihood loss and MAPE. The experiments are well-designed, covering both ID and OOD scenarios, and the results are presented clearly with informative visualizations. The analysis of the scaling behavior is thorough, considering the effects of model size, compute resources, and dataset size independently.
3. The findings of this paper have significant implications for the development of TSFMs. By establishing scaling laws that hold across both ID and OOD scenarios, the authors provide a framework for predicting the expected performance gains of TSFMs as they scale up in size, compute, and data. This is crucial for guiding resource allocation and model design decisions. Moreover, the comparative analysis of different model architectures reveals important trade-offs between ID and OOD performance, highlighting the need for careful consideration when designing TSFMs for specific applications. The practical design principles derived from the study offer valuable guidance for researchers and practitioners working on TSFMs.

### Weaknesses
1. Limited scope of model architectures: The study focuses on two main model architectures: encoder-only and decoder-only Transformers. While these are indeed widely used in TSFMs, the paper could benefit from including a broader range of architectures, such as encoder-decoder models (e.g., Seq2Seq) or hybrid models that combine Transformers with other neural network components (e.g., CNN, RNN). Expanding the scope of the investigated architectures would provide a more comprehensive understanding of how architectural choices affect scalability.
2. Lack of theoretical analysis: The paper primarily relies on empirical observations to establish the scaling laws for TSFMs. While the experimental results are valuable, the work could be enhanced by providing a theoretical foundation for the observed scaling behaviors. Theoretical analysis could help explain why certain scaling patterns emerge and offer insights into the underlying mechanisms that govern the relationship between model size, compute, data, and performance. For example, the authors could explore the connection between the power-law scaling and the model's capacity to learn and generalize from the training data.
3. Limited discussion on the trade-offs between ID and OOD performance: The paper highlights that architectural modifications in Moirai and Chronos improve ID performance but compromise OOD scalability. However, the discussion on this trade-off is relatively brief. A more in-depth analysis of the factors contributing to this trade-off and the potential implications for TSFM design would be valuable. For instance, the authors could investigate whether certain architectural choices (e.g., attention mechanisms, embedding strategies) are more prone to overfitting on ID data, leading to reduced OOD scalability.
4. Absence of computational efficiency analysis: While the paper considers compute budgets as a scaling factor, it does not provide a detailed analysis of the computational efficiency of the investigated models. As TSFMs scale up in size, computational efficiency becomes increasingly important. The paper could be strengthened by including metrics such as training time, inference time, and memory consumption for the different model architectures and sizes. This would provide valuable insights into the practical trade-offs between performance and computational cost.

### Questions
1. Justification for the chosen model architectures: Can the authors provide a more detailed explanation for why they selected encoder-only and decoder-only Transformers as the main focus of their study? While these architectures are indeed popular in TSFMs, it would be helpful to understand the rationale behind this choice and whether the authors believe their findings would generalize to other architectures, such as encoder-decoder models or hybrid models.
2. Potential for theoretical analysis: The paper primarily relies on empirical observations to establish the scaling laws for TSFMs. Have the authors considered complementing their empirical findings with a theoretical analysis? If so, what challenges do they anticipate in developing a theoretical framework for the observed scaling behaviors, and how might such a framework enhance our understanding of the underlying mechanisms governing the relationship between model size, compute, data, and performance?
3. Factors contributing to the ID-OOD performance trade-off: The paper highlights that architectural modifications in Moirai and Chronos improve ID performance but compromise OOD scalability. Can the authors provide more insights into the factors that might contribute to this trade-off? For example, are there specific architectural choices (e.g., attention mechanisms, embedding strategies) that could be more prone to overfitting on ID data, leading to reduced OOD scalability? Understanding these factors could help guide the design of future TSFMs.
4. Computational efficiency considerations: While the paper considers compute budgets as a scaling factor, it does not provide a detailed analysis of the computational efficiency of the investigated models. Can the authors comment on the practical trade-offs between performance and computational cost for the different model architectures and sizes? Including metrics such as training time, inference time, and memory consumption could provide valuable insights for practitioners looking to deploy TSFMs in resource-constrained environments.
5. Generalizability to multivariate time series: The paper focuses exclusively on univariate time series forecasting to avoid the confounding effects introduced by multivariate time series. Can the authors discuss the potential challenges and opportunities in extending their findings to multivariate TSFMs? What additional factors (e.g., variable interactions, correlations) might need to be considered when investigating scaling laws in the multivariate setting?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors examine the scaling laws of Time Series Foundation Models (TSFMs), both encoder-only and decoder-only Transformers, on in-distribution (ID) and out-of-distribution (OOD) data. They find that the NLL (and to some extent the MAPE) of TSFMs shows similar scaling behavior in both ID and OOD settings, scaling as a power law with model parameters, compute, and dataset size. Results suggest that encoder-only Transformers exhibit better scalability than their decoder-only. The authors propose design principles for building scalable TSFMs, focusing on data, model architecture, and compute, recommending encoder-only Transformer architectures for better scalability. Authors also study "emergent behaviors" in TSFMs, where performance on certain OOD datasets improves abruptly after reaching a critical model size.

### Strengths
- Originality: The paper's focus on the scaling laws of TSFMs on OOD data represents a novel and timely contribution.
- Quality: The research is well-executed, with a comprehensive methodology that involves training and evaluating a wide range of models across various parameter counts, compute budgets, and dataset sizes. The use of a large and diverse dataset further strengthens the quality of the empirical analysis.
- Clarity: The paper is well-written and organized.
- Significance: Author's findings could have significant implications for the development and deployment of TSFMs, subject to comments and suggestions in the remainder of this review.

### Weaknesses
- Line 046: provide citations for neural scaling laws that provide ground for believing that they exist.
- Table 1: review the "proportion" row against the "Time points" row. Sales is 0.96% of dataset with 140M points, whereas Web is 0.40% of dataset with 600M points.
- Line 149: "Given its proven effectiveness in improving time series forecasting performance (Woo et al., 2023), we adopt RoPE as a replacement for the original Transformer’s positional encoding." ==> my reading of Woo (2023) is that the evidence in favor of RoPE for time series forecasting is very weak (results presented without confidence bands, and do not appear statistically significant), and likely that better evidence should be presented than the statement of fact that RoPE is "proven" — I don't see that it is, especially in the context of a foundation model.
- Line 190: The paper consistently talks about "log likelihood", for which higher values indicate a better fit. However, all results seem to be obtained under the "negative log-likelihood" (NLL, which is the loss counterpart), for which lower values indicate a better fit. This elementary terminology confusion should be clarified corrected.
- Section 3: The paper only studies Transformer-based architectures, without any baseline results with simple time series models (e.g. ETS-type exponential smoothing or ARIMA) — which could be shown as horizontal lines in the scaling law plots. In particular, the MAPE is around or below 1% for most of the studied scaling regime, which suggest that the datasets are very highly predictable: it is likely that simpler models would do well on these datasets too, bringing into question whether TSFMs' additional complexity is warranted.
- Appendix C.2: Since the training and test sets are taken from long-available public sources, is there a contamination analysis of the test set against the training set to ensure there's no overlap?

### Questions
- Section 3: The MAPE is consistently used as a metric in the main results, although Appendix C.3 outlines a well-known limitation, which is that it is unreliable when the time series takes values close to zero (and suggests using the sMAPE instead). It seems that for time series foundation models, which should be quite agnostic to shift and scale variations of the series, the MAPE should be the last metric to be considered. Why has not the sMAPE been used, or more robust scale-invariant methods like the MASE? (https://en.wikipedia.org/wiki/Mean_absolute_scaled_error )
- Figures 2-4: Although the NLL difference between ID and OOD is of the expected sign (i.e. with OOD having greater NLL than ID), it is truly mystifying that the opposite is consistently true for the MAPE. This is not properly addressed by the authors. In my view, this is the main issue that is causing my "Soundness" assessment not to be higher.
- Figure 5: Although encoder-only clear beat decoder-only in distribution, this difference is almost insignificant out of distribution, in contrast to the claim in the caption. If the authors intend to make this claim, they should conduct a formal statistical test of the fit difference between encoder-only and decoder-only models.
- Suggestion related to Figure 8: across these examples, it'd be instructive to plot (in appendix) what the actual forecasts look like as we transition from a regime of "relatively higher MAPE" to "relatively lower MAPE".

### Soundness
2

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper examines how time series foundation models scale, focusing on the performance of both encoder-decoder and decoder-only transformer architectures in in-distribution (ID) and out-of-distribution (OOD) settings. Through a series of experiments, the authors analyze how changes in model size, computational power, and dataset volume impact these models' effectiveness. One major contribution of this study is the adaptation of existing scaling laws to OOD scenarios, providing a framework to anticipate performance improvements in OOD forecasting based on key training variables. The paper also reveals that encoder-only transformers generally perform better and scale more effectively than decoder-only models. Additionally, the authors offer practical guidelines for building robust, scalable time series foundation models, emphasizing the value of training data diversity, model size, and architectural choices to boost both performance and generalization.

### Strengths
As to the originality, the authors explore a relatively new area in time series forecasting by expanding the concept of scaling laws from in-distribution (ID) settings to out-of-distribution (OOD) contexts. This fresh perspective enhances the relevance of scaling laws and addresses an important gap in understanding how model architectures perform across various data distributions. By comparing encoder-only and decoder-only transformer architectures, the paper merges ideas from neural scaling laws with practical applications in time series analysis, offering new insights into model design! 

The work quality is underscored by the rigorous experimental methods the authors use. They systematically evaluate various time series foundation models across parameters such as model size, computational resources, and dataset dimensions. This comprehensive approach ensures the findings are reliable, providing a strong basis for the paper's conclusions. Using clear performance metrics, like log-likelihood loss and MAPE, adds credibility to the results! 

The paper's clarity is another strength. Concepts are explained in a structured and accessible way, enabling readers from diverse backgrounds to follow the research. The logical flow and transparent presentation of methods and findings make the implications of this work easy to understand. Detailed discussions on scaling behaviours among different architectures further clarify the complex relationships between model design and performance! 

This work is significant for both theoretical and practical reasons. It advances the understanding of time series foundation models and provides empirical insight and design principles for scaling, benefiting researchers and practitioners in developing more effective forecasting models. The insights offered could influence future studies and propel advancements in time series forecasting and neural network design!

### Weaknesses
(1) One notable limitation in this study is its minimal exploration of how different model architectures impact scalability. Although the paper briefly acknowledges architecture's role in scaling, it falls short of offering a thorough analysis on how specific architectural choices, like attention mechanism, layer normalization, or residual connections, might influence scaling behaviour. A deeper, comparative study covering a broader set of architectures could reveal which design choices are most beneficial for performance across diverse data distributions! 

(2) The study's experiments center on log-likelihood loss and MAPE as key performance metrics. While these are certainly relevant, they do not fully capture the complexity of model performance in time series forecasting. A wider range of evaluation metrics, like the Continuous Ranked Probability Score (CRPS) or quantile loss, could offer a more comprehensive view of performance and its practical impact. Although the paper briefly suggests future research might investigate transformations between log-likelihood and forecasting metrics, including preliminary results or further discussion on this topic within the study would enhance the depth and clarity of the findings! 

(3) The paper would benefit from a deeper exploration of why performance tends to degrade on OOD data. Although the authors highlight that scaling the model improves OOD performance, they stop short of examining the mechanisms driving this effect. An in-depth look at how the training data distribution relates to OOD performance could offer valuable insights for practitioners applying these models in a real-world context. For example, investigating domain adaptation techniques or transfer learning strategies might help reduce the performance drop seen in OOD situations! 

(4) The discussion on sample efficiency is insightful but would benefit from concrete examples or case studies that demonstrate how larger models achieve improved performance with fewer training steps. Including specific examples or empirical data to back up this claim would strengthen the credibility of the findings and provide practical guidance for researchers and practitioners looking to optimize their training processes! 

(5) The dataset used for training and evaluation seems carefully chosen but lacks a detailed account of its diversity and representativeness. While the paper highlights the role of dataset size and variety in enhancing OOD performance, it provides limited insights into the dataset's specific characteristics, such as the types of time series it includes, their distributions, or any noise or anomalies present. A deeper examination of the dataset's attributes would offer a clearer picture of the models' performance and their relevance to real-world applications! 

(6) Another important limitation is the lack of attention to how scaling laws impact practical applications. The authors offer theoretical insights into scaling behaviour but do not go far enough in showing how these findings can be turned into useful strategies for practitioners. For example, guidance on balancing model size, computational resources, and dataset size in real-world settings would be valuable for those aiming to apply time series foundation models effectively. Including case studies or examples of successful implementations could also help demonstrate the research's relevance to industry professionals!

### Questions
Please check the Weaknesses section for more questions!

### Soundness
3

### Presentation
4

### Contribution
3
