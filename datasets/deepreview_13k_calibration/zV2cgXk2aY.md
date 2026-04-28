# Sentinel: Multi-Patch Transformer with Temporal and Channel Attention for Time Series Forecasting

- Decision: Reject
- Avg Score: 3.50
- Scores: 5, 3, 3, 3

## Abstract
Transformer-based time series forecasting has recently gained strong interest  due to the ability of transformers to model sequential data. Most of the state-of-the-art architectures exploit either temporal or inter-channel dependencies, limiting their effectiveness in multivariate time-series forecasting where both types of dependencies are crucial. We propose Sentinel, a full transformer-based architecture composed of an encoder able to extract contextual information from the channel dimension, and a decoder designed to capture causal relations and dependencies across the temporal dimension. Additionally, we introduce a multi-patch attention mechanism, which leverages the patching process to structure the input sequence in a way that can be naturally integrated into the transformer architecture, replacing the multi-head splitting process. Extensive experiments on standard benchmarks demonstrate that Sentinel, because of its ability to ``monitor" both the temporal and the inter-channel dimension, achieves better or comparable performance with respect to state-of-the-art approaches.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces Sentinel, a transformer-based model for time series forecasting that effectively captures dependencies across both temporal and inter-channel dimensions. It further proposes a novel multi-patch attention mechanism to replace the standard multi-head attention in the Transformer architecture. Experimental results suggest the model’s effectiveness in capturing these relationships and forecasting time series.

### Strengths
1. The paper is well-written, with a clear presentation of both methodology and results.
2. Experimental results are competitive and close to state-of-the-art (SOTA) performance.
3. The code is made available, which facilitates reproducibility.
4. Targeted Design for Temporal and Inter-Channel Dependency Modeling: The focus on addressing both temporal and inter-channel dependencies in time series data highlights a well-considered model design.

### Weaknesses
1. Novelty: The contributions appear to be incremental. The multi-patch attention mechanism provides a marginal improvement over existing architectures, and the modeling of both temporal and inter-channel dimensions in time series is also not a new idea.
   
2. Justification of Multi-Patch Attention: The rationale behind why multi-patch attention performs better than traditional multi-head attention is not fully explained. An analysis of the root causes for its effectiveness, ideally with theoretical insights or visualizations, would strengthen the contribution.

3. Performance Compared to SOTA: The proposed model does not achieve state-of-the-art performance compared to the provided baselines.

### Questions
1. Encoder-Decoder Design Choices: Why does the model use Multi-Patch Channel attention in the encoder and Multi-Patch Time in the decoder? The ablation study in Table 3 provides limited insights—could more analysis clarify the necessity and effectiveness of this design choice?

2. Simultaneous Temporal and Inter-Channel Modeling: Given the importance of both temporal and inter-channel dependencies, could mechanisms be explored that allow these relationships to be learned simultaneously rather than sequentially?

3. Error Bars for Figure 3: Including error bars in Figure 3 would enhance the clarity of the trend and allow for a better understanding of variability in the results.

4. Further Analysis of Multi-Patch Attention: Additional analysis, particularly regarding the effectiveness of multi-patch attention, would provide valuable insights into its utility and potential limitations.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The author proposed an encoder-decoder model structure that can simultaneously capture temporal relationships and variable relationships. Additionally, the author employed methods such as multi-patch to enhance the model's performance, achieving comparable performance on benchmark datasets by addressing both dependency types effectively.

### Strengths
1. its ability to capture both temporal and inter-channel dependencies crucial for multivariate time series forecasting.
2. by utilizing a patching process, Sentinel introduces a new attention mechanism that replaces traditional multi-head attention splitting. This shifts the focus from "heads" to "patches," integrating more naturally into the Transformer architecture.
3. through ablation studies, the paper demonstrates the contribution of the proposed components to the overall predictive performance.

### Weaknesses
The main weaknesses of the article lie in its novelty and results.
* The methods used in the article mostly have already been proposed by others, and the simple stitching together of ideas makes the article lack novelty.
* The experimental results of the article are mostly the second.
* The main experiments in the article are limited. It might be worth considering adding short-term experiments and incorporating new datasets. For example, there are many new datasets available here: https://huggingface.co/datasets/Salesforce/lotsa_data.
* Lack of sensitivity analysis of parameters.

### Questions
1. The final projection layer flattens the embeddings of all tokens and maps them to the output, right? So, even though a decoder is used, a separate model still needs to be trained for each length?

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
4

### Summary
The paper proposes an encoder-decoder architecture for time series forecasting that models the channel dimension and temporal dimension separately. It introduces a multi-patch attention mechanism to replace the standard multi-head attention to enhance the prediction performance.​

### Strengths
- This paper considers both channel and temporal dimensions in the modeling of time series.

- This paper proposes a multi-patch attention mechanism to replace the standard Transformer multi-head attention by focusing on patch-level information in time series.

### Weaknesses
The motivation of the method lacks clarity, and its novelty is limited. Furthermore, the performance of the proposed method does not show a clear advantage over other baselines, and there is a lack of validation of the rationale behind the design of individual model components.

### Questions
- About the method: The approach of modeling the channel and time dimensions separately lacks novelty. The proposed multi-patch attention mechanism does not convincingly demonstrate effectiveness compared to the standard Transformer structure, nor does it show significant performance gains.

- About main experiments: The primary experiments do not show a clear advantage over existing methods, lacking of recent baselines such as TimeXer and TimeMixer.

- About analytical experiments: Since the authors claim that a key innovation of the paper is the multi-patch attention mechanism’s application to the channel and time dimensions, detailed analytical experiments are necessary. For instance, visualizations showing whether the model has learned meaningful attention patterns could substantiate the rationale and effectiveness of the design.

[1] TimeXer: Empowering Transformers for Time Series Forecasting with Exogenous Variables

[2] TimeMixer: Decomposable Multiscale Mixing for Time Series Forecasting

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
4

### Summary
The paper proposed a Transformer-based model designed for multivariate time-series forecasting. The model introduces a multi-patch attention mechanism that provides two sets of patches, one is from temporal direction and other is from inter-channel direction. Subsequently, the use decoder and decoder to model them separately.
This paper is very clear and easy to understand.

### Strengths
1. A useful insight is that the authors link multi-head splitting to multi-patch splitting, seamlessly introducing their new attention mechanism.
2. I agree that the ablation study is reasonable.
3. The paper includes comparisons with numerous baselines.

### Weaknesses
1. The main concern is that the proposed method does not demonstrate sufficient power, as evident from the experimental results. CARD clearly outperforms the proposed method on numerous datasets. This undermines the authors’ claim, as Sentinel introduces more complexity than CARD with added components—such as “specializing the encoder in capturing contextual information through the channel dimension.” As a result, the contribution may not be sufficient, as integrating inter-channel information effectively could likely boost independent Transformers (PatchTST).

2. Although the authors review many recent papers, they fail to clearly explain their model’s advantage over existing approaches.


3. Compared to similar ICLR papers, the experiments seem insufficient. For instance, CARD, iTransformer, and PatchTST conducted more extensive experiments, either across more datasets or with more comprehensive experimental settings.

### Questions
What are the advantages of the proposed method compared to CARD and other methods? For example, does it offer better efficiency or improved performance with limited data?

### Soundness
2

### Presentation
2

### Contribution
1
