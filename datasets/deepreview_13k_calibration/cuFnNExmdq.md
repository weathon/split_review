# UniTST: Effectively Modeling Inter-Series and Intra-Series Dependencies for Multivariate Time Series Forecasting

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 3, 8

## Abstract
Transformer-based models have emerged as powerful tools for multivariate time series forecasting (MTSF).
However, existing Transformer models often fall short of capturing both intricate dependencies across variate and temporal dimensions in MTS data. Some recent models are proposed to separately capture variate and temporal dependencies through either two sequential or parallel attention mechanisms. However, these methods cannot directly and explicitly learn the intricate inter-series and intra-series dependencies.
In this work, we first demonstrate that these dependencies are very important as they usually exist in real-world data. To directly model these dependencies, we propose a transformer-based model UniTST containing a unified attention mechanism on the flattened patch tokens. Additionally, we add a dispatcher module which reduces the complexity and makes the model feasible for a potentially large number of variates.
Although our proposed model employs a simple architecture, it offers compelling performance as shown in our extensive experiments on several datasets for time series forecasting.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the issue that previous attention-based methods were unable to model both temporal and channels simultaneously. It proposes a flattening approach and draws inspiration from the attention mechanisms of ETC and Crossformer to reduce the complexity of attention calculations. Finally, it attempts to demonstrate the effectiveness of the method through experiments.

### Strengths
**S1:** The multivariate time series forecasting problem focused on in this paper is worthy of investigation.

**S2:** The author's motivation for the study makes sense.

**S4:** The paper is well-written and well-organized, and the content reads smoothly.

### Weaknesses
 **W1:** The authors' model design lacks innovation. While flattening patches makes sense, there is a lack of innovation in the model design, as the Transformer architecture used does not appear to offer any significant novelty. The approach to Attention with dispatchers and the setup resembling ETC[1] and Crossformer[2] are nearly identical. Specifically, the method of flattening the time series into patches and applying a standard Transformer architecture with attention dispatchers closely mirrors the approach in ETC, where long sequences are processed by segmenting them and using a dispatcher to manage attention. The core mechanism of attention, while adapted to the multivariate time series context, does not introduce any fundamentally new operations or architectural elements beyond what is already established in these prior works.

**W2:** The authors' lack of thorough research on past methods is concerning. While authors took note of iTransformer from ICLR 2024, they failed to consider contemporary state-of-the-art methods such as TimeMixer, FITS, and ModernTCN. Furthermore, this still lacks a comparison with GNN-based methods like CrossGNN and FourierGNN from NeurIPS 2023. The absence of these comparisons makes it difficult to assess the true novelty and effectiveness of the proposed method against the current landscape of time series forecasting techniques. The paper needs to demonstrate that the proposed method offers advantages over these recent and relevant baselines.

**W3:** The experimental comparisons are not enough insufficient. The methods mentioned in W2 were also not compared by the authors, therefore, it cannot be concluded that UniTST achieves SOTA performance. The evaluation is limited to a small set of datasets and lacks a comprehensive comparison against recent state-of-the-art methods. Without these comparisons, it is impossible to ascertain whether the proposed method truly advances the field or merely replicates existing results with minor modifications. The claim of achieving SOTA performance is not sufficiently supported by the presented experimental results.

**W4:** The lack of details in reproducibility.

### Questions
- Could the authors further expand the search range for hidden dimensions to evaluate all models' performance fairly? Also, Please publicly disclose the optimal parameters for all models across various tasks as determined through validation sets (batch size, hidden dimensions, etc.). This is crucial to validate the performance of UniTST and mitigate any impact from selective parameter choices.

- I noticed the experimental results in Table 6, which seem to show minimal improvement compared to iTransformer in many cases. Could the authors, after addressing question 1, provide new experimental results, analyze the reasons behind them, and conduct a comparative analysis of the efficiency (time/memory) of these two methods?

-  Can the authors provide a case study of a variable prediction curve?

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
5

### Summary
UniTST is designed to address existing models' limitations in capturing complex dependencies across variate and temporal dimensions in multivariate time series (MTS) data. The authors argue that previous Transformer models have fallen short in simultaneously capturing inter-variate (between different series) and intra-variate (within the same series) dependencies, critical for accurate forecasting in real-world data.

The authors introduce a unified attention mechanism within UniTST that operates on flattened patch tokens, allowing the model to directly and explicitly learn the intricate inter-series and intra-series dependencies. To manage the increased complexity associated with a large number of variates, a dispatcher module is integrated into the model, reducing the computational complexity from quadratic to linear, thus making the model scalable.

The paper contributes to the field by highlighting the importance of inter- and intra-variate dependencies in MTS forecasting, proposing a simple yet effective model architecture to capture these dependencies, and empirically demonstrating its superiority over existing methods. The findings emphasize the necessity of simultaneously modelling variate and temporal dynamics in multivariate time series analysis.

### Strengths
The paper clearly outlines the limitations of existing Transformer models in capturing both inter-variable and intra-variable dependencies within multivariate time series data. To address this issue, it introduces the UniTST model.

The proposed UniTST model employs a unified attention mechanism alongside a scheduler module to simultaneously capture inter-variable and intra-variable dependencies. This innovative design effectively enhances the handling of multivariate time series data.

The experimental results presented in the paper are reproducible, reliable, and credible.

### Weaknesses
The motivation behind the study is not clearly articulated, which makes it difficult to fully understand the underlying rationale and significance of the research problem. Additionally, the proposed approach lacks sufficient novelty, as it does not introduce substantially new concepts or techniques compared to existing methods. Strengthening the motivation and highlighting the unique contributions of the work would enhance its originality and impact within the field.

In the ablation study, the effectiveness of the dispatcher is evaluated based on memory usage, an approach that is relatively uncommon. While comparing the memory consumption of the dispatcher module with other modules within the model provides useful insights, However, it is not sufficient to conduct ablation experiments on only one component within the model. It is also essential to assess the whole model's memory impact relative to other models. A more rigorous evaluation would involve additional comparisons with state-of-the-art (SOTA) models, focusing on computational cost and model parameter size both before and after integrating the dispatcher. This broader comparison would offer a clearer understanding of the dispatcher’s role and efficiency within the model.

The authors claim that "each value at one time stamp has no semantic meaning" in time series data, which is an oversimplification. In reality, every time point in many time series datasets holds important information that's crucial for forecasting and analysis. For example, each timestamp of stock prices or hourly temperature records carries significant value in practical applications. Moreover, this paper haven't clearly explained how patching specifically enhances the unified Attention mechanism's ability to capture dependencies. Without a solid theoretical foundation, the rationale behind combining patching with unified Attention doesn't seem sufficiently justified. This raises questions about the overall novelty and scientific merit of the approach.

The proposed method is too similar to existing models like PatchTST in some aspects, lacking significant innovation. This kind of incremental improvement based on existing methods doesn't provide enough new value to stand out or justify substantial attention and acceptance.

### Questions
Training was conducted using an A100 40GB GPU, which, under typical conditions, rarely runs out of memory—except when working with large models such as TimesNet on the Traffic dataset. However, the ablation study does not specify the batch size used, also there are questions about the choice of memory usage as a comparative metric. A detailed explanation is needed to clarify why memory usage was selected as a benchmark for this experiment and why one out of four ablation experiments resulted in an out-of-memory (OOM) error.

The motivation for this study is not clearly defined and appears somewhat unconvincing. Although the results from the experiment in Figure 3 are cited as the primary source of motivation, the rationale behind conducting the experiment in Figure 3 itself is unclear. Most existing models that aim to capture inter-variable and intra-variable dependencies in multivariate data do not employ patch operations. Thus, the introduction of patching in the experiment warrants further explanation. A more rigorous clarification of the motivation, particularly regarding the choice to incorporate patch operations, would strengthen the foundation and relevance of this study.

### Soundness
3

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
The article proposes a dependencies across different variates and different times and presents a corresponding Transformer modeling method. However, this greatly increases the number of tokens. To reduce complexity, a Dispatch method is proposed.

### Strengths
Experiments have been conducted on the major datasets currently available. The experiments are relatively sufficient and the analysis is comprehensive, including hyperparameter analysis and efficiency analysis.
It is recommended to add some visualized prediction results and compare them with the state-of-the-art. This is a relatively common way of presenting results.

### Weaknesses
1. For the current research situation, this contribution is relatively ordinary. There are many almost identical practices in the past. For example, Different sEnsors at Different Timestamps (DEDT) in https://arxiv.org/abs/2309.05305  is completely the same as "across different variates and different time" in the second line of the third paragraph of the Introduction. Cross-correlation coefficient in https://arxiv.org/abs/2401.17548 is almost same with the Definition 1,  just with different names. I think the explanation of the problem and the drawings are not as clear as those in past articles. 
At the end of the second paragraph of the Introduction, the problems in the two stages are mutually influential. I think there is a lack of experimental proof for the problem. Moreover, the two-stage method in the past https://arxiv.org/pdf/2402.19072 is not inferior to UNITST in terms of effect.
3. The Dispatcher is also the same as the router in Crossformer . There is no innovation.
4. No code is provided for reproducibility testing, the authenticity of the experimental results is reserved.
5. Incidentally, the article uses the template of ICLR 2024. When reviewing, it is not convenient to locate the exact line.

### Questions
1. What is the value of t' corresponding to the correlations in Figure 3?
2. Since the router operation, that is, the Dispatcher proposed in the article, is used, it may not be possible to directly visualize the attention weights between variables learned by the model to correspond to the correlation calculated by Definition 1. Then, can you provide the correlation value calculated for the model's prediction results and compare it with the correlation based on real data given in Figure 3? Does the model truly capture the dependencies across different variates and different times that you proposed or other fitting results?
3. It is recommended to provide code for reproducibility.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes a novel method to capture inter-series and intra-series information from multivariate time series. This paper utilizes a unified attention mechanism on the flattened patch tokens, and adds a dispatcher module which reduces the complexity and makes the
model feasible for high-dimensional inputs. The model achieves compelling performance in multiple datasets for time series forecasting.

### Strengths
The paper is overall well written and the experiment section is clearly expained with newest benchmark methods. Effectively capturing the inter- and intra- series information is an important issue in LTSF, and the idea of unified attention seems interesting.

### Weaknesses
1. The paper claims that 'previous transformer models lack ability to simultaneously capture both inter-variate and intra-variate dependencies', which is not accurate. In fact, there is some literature focusing on modeling inter- and intra- series information in a Transformer structure, for example, CATS: Enhancing Multivariate Time Series Forecasting by Constructing Auxiliary Time Series as Exogenous Variables (ICML 2024) adopts a very similar idea by constructing an auxiliary series to capture inter- and intra- series. The author should revise their literature review accordingly and explain their difference with CATS.

2. Time series forecast using LLM has been a trand in recent years. The author is encouraged to include more LLM-based methods as benchmarks, such as LLM4TS or GPT4TS.

### Questions
The author flattens all patches from different variates into a unified sequence. I wonder whether the sequence is (1) normalized, (2) univariate or multivariate. Furthermore, if the input dimension is high, the unified sequence may be too long. 

What is the difference of constructing a unified sequence and simple concatenation? It seems very similar to me. 

How does the author determine the order of raw input series to construct the unified sequence? If the order is random then I suspect that the encoder may not be time-aware, making the output less reliable without additional input of time.

### Soundness
3

### Presentation
3

### Contribution
3
