# PSformer: Parameter-efficient Transformer with Segment Attention for Time Series Forecasting

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 6, 6, 5, 5, 5

## Abstract
\vspace{-1ex}
Time series forecasting remains a critical challenge across various domains, often complicated by high-dimensional data and long-term dependencies. This paper presents a novel transformer architecture for time series forecasting, incorporating two key innovations: parameter sharing (PS) and Spatial-Temporal Segment Attention (SegAtt). We also define the time series segment as the concatenation of sequence patches from the same positions across different variables. The proposed model, PSformer, reduces the number of training parameters through the parameter sharing mechanism, thereby improving model efficiency and scalability. The introduction of SegAtt could enhance the capability of capturing local spatio-temporal dependencies by computing attention over the segments, and improve global representation by integrating information across segments. The combination of parameter sharing and SegAtt significantly improves the forecasting performance. Extensive experiments on benchmark datasets demonstrate that PSformer outperforms popular baselines and other transformer-based approaches in terms of accuracy and scalability, establishing itself as an accurate and scalable tool for time series forecasting.
\vspace{-1ex}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The article introduces a novel Transformer architecture, PSformer, for time series forecasting, incorporating parameter sharing (PS) and Spatial-Temporal Segment Attention (SegAtt). The authors conducted experiments on various benchmark datasets, comparing PSformer with baseline methods.

### Strengths
1. The design ideas and motivations behind the model are very interesting.

2. The way the article is written is very good, making it very easy to follow.

### Weaknesses
 1. The article has some minor errors, for example, I couldn't seem to find Table 27.

 2. The article lacks research on important references, such as the author's focus on iTransformer at ICLR 2024, but does not consider contemporaneous models like TimeMixer[1], and FITS[2]. Furthermore, this still lacks a comparison with GNN-based methods like CrossGNN[3] and FourierGNN[4] from NeurIPS 2023 and other methods such as MICN[5] at ICLR 2023.

 3. The experimental comparisons are insufficient. The methods mentioned in W2 and TimesNet[6] were also not compared by the authors, therefore, it cannot be concluded that PSformer achieves SOTA performance.

 4. The author seems to have not provided details about the experimental platform. Additionally, it appears that the author did not specify the parameter search space for the compared methods. Has the author completed the work of determining the best model parameters on the validation set? If this work has not been done, it would not be fair to compare the performance of all models, as the specific choices of the experimental platform and model parameters can have a significant impact on the experimental conclusions. It is hoped that the author can clarify this point.

### Questions
See the Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents a Transformer architecture for time series forecasting that highlights parameter sharing and cross-channel patching. Specifically, it applies attention across both channels and patches for spatio-temporal information fusion, and aligns the parameters of linear projections within an encoder block. Experiments show that these two designs contributes to the overall performance improvement on popular benchmarks.

### Strengths
1. The method proposed in the paper has clear motivation and solid intuition.
2. The idea is presented with clarity and easy to follow.
3. Sufficient analysis is done to highlight the efficacy of the proposed updates on existing Transformer architectures.

### Weaknesses
1. The accuracy improvement is relatively marginal, especially in ablation studies, and variances in metrics should be reported to support the significancy of the contribution from the proposed ideas.
2. An analysis about why PSformer does not work well on exchange would be helpful.

### Questions
See weakness

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This article presents a framework for multivariate time series forecasting, integrating
parameter sharing and a Spatial-Temporal Segment Attention mechanism. Extensive
experiments demonstrate that this approach consistently achieves higher accuracy and
efficiency compared to other state-of-the-art models

### Strengths
a) This paper presents an innovative SegAtt mechanism and a parameter-sharing
approach, effectively advancing methods in time series forecasting and aligning well with
the field’s objectives.

b) The experimental evaluation is notably thorough, offering readers a well-rounded
perspective on the framework’s performance and the contributions of its various
components.

c) The writing is clear and of high quality, making the paper accessible and easy to
understand.

### Weaknesses
a) While SegAtt demonstrates notable strengths, it would be advantageous to evaluate the
selection of segmentation numbers across a more diverse range of datasets beyond
ETTh1 and ETTm1. Providing further guidance on practical approaches for selecting
segmentation numbers would also be valuable.

b) The experimental section could be enhanced by further validating the framework’s
parameter-saving capacity and examining its implications for pre-trained models.

c) To strengthen the robustness of the findings, incorporating results with multiple
random seeds would provide additional confirmation of the framework’s superior
performance.

d) A deeper exploration of channel-mixing techniques could enrich the analysis. A
comparative discussion, similar to PatchTST A.7, on the benefits of channel
independence versus channel-mixing strategies would be particularly insightful.

e) Regarding computational efficiency, could you clarify which specific components
within the framework contribute to its computational advantages over other state-of-the-
art models?

### Questions
In the weakness part.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces PSformer, a novel transformer-based architecture for time series forecasting that incorporates parameter sharing techniques and a Spatial-Temporal Segment Attention mechanism to capture local spatio-temporal dependencies.

### Strengths
(1) The introduction of parameter sharing techniques in transformer-based models demonstrates its effectiveness and potential in the field as validated by experimental results.

(2) Experimental results demonstrate that PSformer achieves state-of-the-art performance in the most of the datasets.

### Weaknesses
(1) There are several writing errors present in the article.

(2) Although the parameter sharing techniques demonstrated effectiveness according to the ablation study, the authors did not provide detailed analysis or empirical studies to further elucidate this technique, such as comparisons of convergence rates with and without parameter sharing or analysis of how parameter sharing affects model capacity.

### Questions
(1) Referring to **Weaknesses (2)**, could you provide a more in-depth analysis or empirical studies to illustrate the effectiveness of parameter sharing in time series forecasting?

(2) According to the authors, attention is applied within each segment to enhance the extraction of local spatio-temporal relationships. However, in PSformer, a token represents a down-sampled sequence along a channel. This might be confusing because it suggests that the attention is applied to capture the global dependencies across channels. Could you provide a more detailed explanation of how the segmentation process preserves local temporal information while allowing for cross-channel interactions.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
PSFormer suggests a new transformer-based model for multivariate time-series forecasting. This model utilizes parameter sharing(PS Block) and spatial-temporal segment attention(SegAtt) to decrease computational complexity while effectively modeling time and feature-wise dependency in data. SegAtt is designed to group patches located at the same positions across different variables, enabling efficient capture of local spatio-temporal dependencies. PSBlock allows the model to maintain linear path(residual connection) but also perform nonlinear transformation. As this block is shared, the model can reduce its parameter when it comes to the whole model architecture. With these advantages, PSFormer achieves strong parameter efficiency and enhances predictive accuracy across various benchmark datasets, showing greater scalability and forecasting performance than conventional Transformer models.

### Strengths
1. PSFormer reduces the number of parameters by parameter sharing, which allows to maintain both size and representational ability of the model. This design enhances the model’s scalability and helps mitigate overfitting in data-scarce scenarios.
2. PSFormer demonstrates shorter running time and smaller model size, which empirically shows efficacy of parameter sharing. 
3. The SegAtt mechanism effectively models spatio-temporal dependencies in multivariate time series by incorporating inter-variable information, boosting prediction accuracy.

### Weaknesses
1. The model’s performance varies with different hyperparameters, making hyperparameter tuning appear crucial. 
2. While SegAtt improves performance, it may underperform in cases of univariate time series or where there is little dependency between variables.
3. The paper briefly mentions the necessity of positional encoding, but additional experiments are needed to assess its impact on the generalization of sequences that require a strong temporal order.

### Questions
1. Are there any specific settings where PSFormer performs particularly well? For example, do they work better on datasets with strong correlations between variables? When looking at the benchmark datasets, it seems that the Electricity and Exchange datasets exhibited weaker performance compared to others. I am curious if there is any reason for this. 
2. Could the authors provide an ablation study comparing PSFormer’s performance with and without SAM, as well as with other optimization methods such as Adam or SGD? This would clarify the specific impact of SAM on performance and provide a basis for its inclusion in the PSFormer architecture.
3. The authors briefly explained the influence of positional encoding; however, have you conducted more specific experiments on the effects of this positional encoding on the model? I am curious about additional analysis results for various time series data. Could the authors perform experiments comparing the model’s performance with and without positional encoding on different time series types (e.g., seasonal vs. non-seasonal, stationary vs. non-stationary)? Such an analysis could clarify the benefits of positional encoding in diverse time series forecasting contexts.
4. In the ablation study, I observed the analysis results regarding the influence of the number of encoder layers and the number of segments. It seems that tuning these hyperparameters has a significant impact on the model’s performance. Could the authors detail their hyperparameter tuning process, or alternatively, discuss recommended tuning approaches (e.g., grid search, random search, Bayesian optimization) tailored to PSFormer? 
5.  Could the authors provide a detailed analysis of how parameter sharing in the PS Block affects the model’s temporal pattern capture? For instance, they could compare learned representations across layers with and without parameter sharing, illustrating its influence on time series modeling.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 6

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a Transformer-based model for time series forecasting (PSformer), which primarily consists of two core components: the Parameter Sharing Technique and the Spatial-Temporal Segment Attention mechanism. The former is designed to reduce the complexity of the model, while the latter is used to simultaneously model temporal dynamics and channel correlations.

### Strengths
S1: PSformer experiments involve a wide range of datasets.

S2: PSformer and baselines are compared in terms of training parameters and running time.

### Weaknesses
W1: The paper overall lacks innovation. Parameter Sharing is merely a simple module parameter-sharing technique to reduce complexity. Additionally, Spatial-Temporal Segment Attention simply merges the channel dimension and patch size dimension together before modeling it with a Transformer.

W2: What is the purpose of including the PS Block in the Segment Attention? Why not just add the PS Block after the output of the Attention, which would eliminate the need for parameter sharing? Additionally, why can two SegAttn be viewed as one FFN layer?

W3: The integration of temporal and channel information in Spatial-Temporal Segment Attention may lead to incomplete capture of both time and spatial information, potentially resulting in negative effects. Could you further explain how this approach differs from the separated modeling methods like Crossformer and iTransformer, and visualize the advantages of PSformer in modeling time and channel?

W4: Why is there such a significant difference between the results of PatchTST in Table 1 and the original PatchTST? Please explain.

W5: Please add new baselines for comparison, such as PDF (ICLR2024) and Time-LLM (ICLR2024).

W6: There are many writing errors in the paper, such as "Moment()" on line 125 and "GPT4TS uses BERT as the backbone" on line 127.

### Questions
See W1-W6.

### Soundness
2

### Presentation
2

### Contribution
2
