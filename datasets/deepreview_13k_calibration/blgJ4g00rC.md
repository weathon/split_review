# TimeCapsule:  Solving the Jigsaw Puzzle of Long-Term Time Series Forecasting with Compressed Predictive Representations

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
Recent deep learning models for long-term time series forecasting (LTSF) often emphasize complex, handcrafted designs and traditional methodologies, while simpler architectures like linear models or MLPs have occasionally outperformed these intricate solutions. In this paper, we revisit and organize the core ideas behind several key techniques, such as redundancy reduction and multi-scale modeling, which are frequently employed in advanced LTSF models. Our goal is to streamline these ideas for more efficient deep learning utilization. To this end, we introduce TimeCapsule, a model built around the principle of high-dimensional information compression that unifies these key ideas in a generalized yet simplified framework. Specifically, we model time series as a 3D tensor, incorporating temporal, variate, and level dimensions, and leverage mode production to capture multi-mode dependencies while achieving dimensionality compression. We propose an internal forecast within the compressed representation domain, supported by the Joint-Embedding Predictive Architecture (JEPA) to monitor the learning of predictive representations. Extensive experiments on challenging benchmarks demonstrate the versatility of our method, showing that TimeCapsule can achieve performance comparable to state-of-the-art models. More importantly, the structure of our model yields intriguing empirical findings, prompting a rethinking of approaches in this area.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This manuscript introduces a framework that adds an extra level dimension to time series data and employs mode production to capture multi-mode dependencies. It utilizes transformer blocks to capture dependencies across temporal, level, and variate dimensions, respectively.

### Strengths
This manuscript is well-written, logically organized, and easy to follow. It provides a comprehensive analysis of recent SOTA methods for MTS forecasting. The Mode Specific Multi-head Self-attention utilizes a vanilla attention mechanism to capture temporal dependencies. Although patching has been a widely used technique in recent years to reduce the length of input for attention mechanisms, this manuscript employs low-rank transforms as a replacement, achieving promising efficiency.
TimeCapsule applied the JEPA approach to time series forecasting and demonstrates its effectiveness. TimeCapsule has achieved superior performance in both accuracy and computational speed. Extensive ablation studies were conducted, which underscore the effectiveness of the core components of TimeCapsule.
In my opinion, this manuscript is novel and likely to generate interest among researchers in the field of time series analysis.

### Weaknesses
Existing transformer-based methods partition time series sequences into patches of various sizes to capture multi-scale temporal dependencies. TimeCapsule introduces an additional level dimension to the 2-dimensional MTS data to capture multi-scale dependencies. However, the explanation of how multi-scale dependencies are captured is lacking. Specifically, definitions of how multi-scale levels and variate dependencies are defined are needed.

In Figure 2, the components below ReVin_Norm are depicted in a way that may be misleading. Consider using more intuitive shapes to represent tensors.

Table 2 presents an ablation study of the residual information connection. For ETTh2 and ETT m2 datasets, the accuracy achieved with original information is similar to that achieved with residual information connections. In addition, the gap between the two settings increases as the forecasting horizon extends. An analysis of these findings would be beneficial.

### Questions
I have a few suggestions that may enhance the quality of the paper: 

(a) Please consider increasing the text size in some figures to improve readability. 

(b) Could you explain the rationale behind connecting the T-TransBlock, L-TransBlock, and V-TransBlock in series? Have you tested configuring these blocks in parallel, concatenating their outputs, and then using a linear layer to generate predictions? 

(c) Consider adding a description in Section 3.2 of how multi-scale dependencies for Temporal, Level, and Variate dimensions are captured.

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
4

### Summary
This paper proposes TimeCapsule, a new architecture for time-series forecasting by combining key model-blocks introduced in recent works. Additionally, this paper employs a self-supervised loss based on JEPA to enhance the forecasting performance. Overall, TimeCapsule consists of an encoder to learn representations that are then used for forecasting with an MLP-based decoder. The key model-components seem to be: multi-level modelling, multi-mode dependency, and compressed representation forecasting.

### Strengths
* The paper presentation is very good considering that the model architecture being proposed in the paper is rather complex. Fig. 2 was also very helpful in understanding the various model components. 
* It is interesting to see the JEPA loss being applied on time-series. 
* The performance of the new architecture is evaluated on long-term time series forecasting datasets. 
* The paper presents some ablations and also analyses the compute-efficiency.

### Weaknesses
 * The main weakness, in my opinion, is that the paper only considers time-series forecasting to evaluate the model. To establish generality of the model architecture, it may be important to also consider other tasks such as classification, self-supervised learning, or irregular time-series forecasting/imputation. 
* The paper makes many contributions and it may be more valuable to carefully ablate each of these new components. Some of the design decisions/ alternatives could be clearly elaborated. For example, why apply EMA over input time-series Y in Eq. 15? Why introduce Gaussian noise at the start of the block (L. 251) --- what alternatives can we consider in practice? It's unclear how the specific parameters of the EMA (e.g., smoothing factor) or the Gaussian noise (e.g., variance) were chosen and if these choices impact performance. A more detailed exploration of these parameters is needed.
* The results suggest that some gains by JEPA loss are marginal. It'd have been nice if the authors demonstrated self-supervised pretraining based on JEPA helped various downstream tasks (e.g., forecasting/classification/etc). It is also unclear if the JEPA loss is truly necessary, or if a simpler self-supervised approach may yield similar results. The paper should provide a more thorough comparison to other self-supervised techniques.

### Questions
1. Based on your experiments, is TimeCapsule architecture key for the JEPA training? For example, if you tried to apply JEPA to PatchTST architecture, would we notice any improvements? 
2. In line 368, it says "Besides, our model outperforms PatchTST, particularly on larger datasets, without employing patching techniques." Why is it beneficial to eliminate patching? 
3. What kind of attention is used in the Tunnel layers?
4. What is coefficient considered for JEPA loss? 

Minor typo: Both MvTS and MTS seem to refer to multivariate time series and it may be better to use just one abbreviation.

### Soundness
2

### Presentation
2

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
This paper introduces **TimeCapsule**, a model aimed at simplifying and unifying key techniques in long-term time series forecasting (LTSF) while achieving comparable performance to complex, state-of-the-art models. TimeCapsule models time series as a 3D tensor, incorporating temporal, variate, and level dimensions, and leverages mode production to capture multi-mode dependencies while achieving dimensionality compression. Experiments on challenging benchmarks highlight TimeCapsule's effectiveness.

### Strengths
1. This paper provides a new insight into treating time series as a 3D tensor.
2. The authors try hard to categorize the advanced LTSF models into four groups based on their core techniques.
3. The Figures are simple and easy to understand, effectively presenting the model's design concept intuitively.

### Weaknesses
Generally, the technique of the manuscript is partially sound, and some major concerns are listed below:

1. The motivation of this paper is unclear, as noted in question 1. There is no evidence provided to demonstrate that combining effective components from related work will result in a better model. Even in the ablation study, the authors do not discuss this problem. Authors can analysis  why combining these components should lead to improved performance.
2. The authors review and categorize existing methods for long-term time series forecasting, stating that their classification is based on key techniques. However, the four categories are not on the same level. For instance, "Generalized Linear Dependency" would more accurately correspond to methods addressing nonlinear dependencies, representing a classification by learning framework. Yet, the authors unexpectedly group this with specific modeling techniques that focus on better leveraging time series characteristics within the same category.  Please provide a clearer justification for why you grouped these different types of approaches together, if you choose to keep the current categorization.
3. The authors should provide explanations for the function of symbols nearby, especially for less common symbols, such as $\times_2$ in Equation (2), even though they are defined in the appendix.

### Questions
1. The classification criteria in Figure 1 are unclear. And what are the advantages of each category, and what are the benefits of combining these advantages? I believe this information is essential for the paper. Additionally, in the overlapping section on the right of the figure, does the “…” indicate a lack of relevant work, or that the authors couldn’t find any? If none exist, why is there no related work in this area?
2. In section 3.1, the encoding part includes a series of transformer-based blocks, and the decoder operates with a series of MLPs. Could this increase the model's complexity?
3. Can you further explain “to maintain the same volume of information while shortening the length of each dimension, thereby reducing the computational cost of self-attention.” in line 237?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper integrates existing time series analysis methods including temporal, variate, multi-scale, etc. to deal with various multivariate time series scenarios. It proposes a corresponding preprocessing and prediction method framework. And applies the JEPA method to the highly compressed representation space and adds the corresponding loss.

### Strengths
The research direction of the article is relatively innovative. Indeed, integrating various current methods is a good direction, and the methods used are logically reasonable. The article's expression and illustrations are overall very clear.

### Weaknesses
1. I think there is a certain difference between the Target and context inputs of JEPA in this article and, for example, I-JEPA. In I-JEPA, the context and Target overlap. Here, I think it is worthy of further demonstration. Based on more sufficient experimental evidence, a more appropriate design should be given. I think the application of JEPA to TS problems here is not studied in-depth.
2. I think it is necessary to compare the effects and efficiencies of MLP and the Transformer Decoder. The lack of experiments means that it cannot be directly concluded as unreasonable.
3. For the order of TransBlocks and the comparison with the parallel method, there is a lack of experimental support.
4. The elaboration of Decomposition classification and level is not very clear. I think adding some visualizations or results after the processing of each TransBlock (T,V,L) and the analysis of how to correspond to the function will be more clear and intuitive.
5. I think the method proposed in the article has some limitations. For example, the selection of the lookback window is an unconventional 512. Of course, the article also analyzes different lengths. But it is obvious that the larger is more effective. I suggest clarifying this point and whether there are other limitations. I think limitations are also a contribution to the development of the field.
6. No code is provided for reproducibility.

### Questions
1. Line 281-283 Utilizing JEPA, what specific inductive bias is introduced?
2. Why is TransBlocks in this order? Is there a difference in different processing orders for different types of datasets? What is the difference compared to parallel processing?
3. Why only select one subset, PEMS04 of PEMS? I think the advantages and limitations of a method should be supported by comprehensive experimental results, rather than conducting a large amount of analysis based on the performance on a single example dataset as in the Main Results part.

### Soundness
3

### Presentation
3

### Contribution
2
