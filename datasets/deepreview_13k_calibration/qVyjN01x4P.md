# Learning Pattern-Specific Experts for Time Series Forecasting Under Patch-level Distribution Shift

- Decision: Reject
- Avg Score: 5.40
- Scores: 6, 6, 5, 5, 5

## Abstract
Time series forecasting, which aims to predict future values based on historical data, has garnered significant attention due to its broad range of applications. 
However, real-world time series often exhibit complex non-uniform distribution with varying patterns across segments, such as season, operating condition, or semantic meaning, making accurate forecasting challenging.
Existing approaches, which typically train a single model to capture all these diverse patterns, often struggle with the pattern drifts between patches and may lead to poor generalization.
To address these challenges, we propose \textbf{TFPS}, a novel architecture that leverages pattern-specific experts for more accurate and adaptable time series forecasting. TFPS employs a dual-domain encoder to capture both time-domain and frequency-domain features, enabling a more comprehensive understanding of temporal dynamics. It then uses subspace clustering to dynamically identify distinct patterns across data patches. Finally, pattern-specific experts model these unique patterns, delivering tailored predictions for each patch. By explicitly learning and adapting to evolving patterns, TFPS achieves significantly improved forecasting accuracy. Extensive experiments on real-world datasets demonstrate that TFPS outperforms state-of-the-art methods, particularly in long-term forecasting, through its dynamic and pattern-aware learning approach.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper innovatively addresses the diversity of time series patterns by introducing a Mixture of Experts (MoE) approach for decoupled modeling. It leverages a unique PI module as the gating function to route different patterns to the appropriate experts. The experimental results convincingly demonstrate the superiority of this method, complemented by comprehensive ablation studies validating the effectiveness of each component. The writing is clear, with the authors articulating the problem and solution effectively. However, the design of the expert models appears somewhat simplistic, and the decoupling of time and frequency domains is already a well-established approach in time series analysis, making it less of an innovative contribution. Overall, the method shows sufficient technical depth and originality, despite some areas that could benefit from further enhancement.

### Strengths
The authors conducted a detailed experimental analysis and identified that different time series exhibit unique patterns. Traditional models typically employ a unified modeling approach for these varying patterns, which can limit their effectiveness. To address this issue, the authors propose a Mixture of Experts (MoE) approach that enables tailored modeling for different patterns. Additionally, they decompose the time series data into two dimensions: time and frequency, using a dual encoder to model both types of information separately. To ensure that the MoE effectively learns distinct patterns, the authors introduce a novel gating mechanism. This mechanism leverages subspace affinity to allocate sequences with different patterns to the appropriate experts.

### Weaknesses
The decoupling of time-domain and frequency-domain information, as discussed in the paper, is already a common approach in the field of time series analysis and cannot be considered a novel contribution. Additionally, regarding the MoE (Mixture of Experts) section, the use of multiple MLPs seems more akin to employing multiple output predictors with weighted combinations rather than a true MoE structure. Specifically, the lack of a clear gating mechanism that dynamically assigns inputs to experts based on learned characteristics, rather than a static weighting, undermines the claim of a true MoE implementation. Lastly, with respect to the normalization technique, would the authors consider adding experimental results comparing their approach to REVIN [1]? REVIN has shown strong performance across various time series forecasting tasks and could provide a valuable benchmark.

### Questions
1. In the PI module, the number of experts K is currently adjusted manually through parameter tuning. Is it possible to directly relate the value of K to the number of patterns inherent in the time series data itself?
2. On line 317, there appear to be two identical objectives listed, which seems to be a typographical error.

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
The paper addresses the challenge of distributional shift in time series data by proposing a novel framework called the Time Frequency Pattern-Specific (TFPS) architecture. This method is designed to effectively model complex patterns in time series, enhancing the model's ability to manage distributional shifts more robustly.

### Strengths
1. The paper is well written and easy to follow.
2. The paper is well motivated.
3. The method shows promising results compared to the baselines.

### Weaknesses
1. The number of subspace variables $k$, does not appear to be clearly specified in the paper. Given that these variables are essential for modeling the patterns of patches, it is crucial to understand how to set an appropriate value for $k$. The authors should provide further discussion on this aspect. Additionally, an ablation study examining the impact of different values of $k$ would be beneficial.

2. The paper doesn't specify how the subspace variables are initialized. I think the initialization of subspace variables is crucial to achieve optimal performance.

3. Since the subspace variables is utilized for clustering. It is better to provide the relevant visualization (e.g., tsne) to show the effectiveness.

4. Some important information, such as the number of MoPE, the value of hyper-parameters $\alpha$, $\beta$ used for the results in the Table 2 are not clearly specified.

5. What do the notations $K_t$ and $K_f$ mean? The paper doesn't provide the clear definition.

### Questions
see weakness

### Soundness
3

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
2

### Summary
The paper proposes a pattern-based mixture of experts model for time series prediction. In this approach time series patches are first extracted and embedded into a sequence of "tokens". This sequence is then encoded with time and frequency encoders and mined for representative patterns that can aid prediction via a mixture of experts approach.

### Strengths
The paper is well written and relatively easy to follow. The proposed approach is interesting and explores time and frequency aspect of time series prediction. Authors conduct extensive experiments on real world datasets showing that the purposed approach outperforms a number of baselines.

### Weaknesses
I have several concerns about this method. First, it is quite complex, the loss in Eq 12 has three terms and both L_{PI_t} and L_{PI_f} have three tunable hyper parameters \alpha, \beta and \nu (Eq 5, 6 and 9). So there are at least six hyper parameters to tune in addition to balancing the three loss terms that likely requires more hyper parameters. There is nothing in the experimental section on these hyper parameters and no ablation study is conducted. I've worked with these datasets myself, they are quite small and easy to overfit to which raises a major concern when one has to tune 6+ hyper parameters just in the loss function. Second, the proposed mixture of experts in Eq 10 and 11 looks nearly identical to self attention with the exception of the top-k selection. So I suspect that this method will, despite significant added complexity, have a similar representation power to simply stacking attention layers over patches, as all operations including subspace bases affinity are nearly identical to appropriately parametrized self attention.

### Questions
Do you have ablation study on the hyper parameters in the loss function? Which ranges did you try and how sensitive are the results to the particular choice? Also, did you have to balance the contribution of the three terms in the loss?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
Real-world time series often exhibit varying degrees of distribution shift, posing challenges for time series forecasting. This paper employs subspace clustering from both time-domain and frequency-domain perspectives to identify different patterns within data segments. It utilizes multiple experts to specifically model temporal patterns. Extensive experiments conducted on eight real-world time series datasets demonstrate that the proposed method outperforms other state-of-the-art approaches in terms of predictive performance.

### Strengths
1. Distribution shifts often lead to changes in frequency-domain information, making it a reasonable and effective approach to model time series from both time-domain and frequency-domain perspectives.
2. The main contribution of this paper is to utilize subspace clustering to detect concept drift between multiple subspaces and model them separately, thereby achieving more accurate and adaptive modeling. 
3. Extensive experiments demonstrate that the proposed method outperforms other state-of-the-art approaches across various time series datasets.

### Weaknesses
1. The frequency-domain encoder part of the dual-domain encoder implements a simple feedforward layer by discarding the imaginary part. This leads to a loss of information in the frequency domain. Does this contradict the original intention of using the dual-domain encoder to provide a comprehensive representation of the time series? Considering that the time-domain encoder directly utilizes the PatchTST encoder, the frequency-domain part could also use an existing frequency-domain encoder.
2. The Pattern Identifter module employs multiple hyperparameters  $\alpha、\beta$ to mix different components of the loss function. Given the importance of the loss function for experimental results, it is necessary to include ablation experiments for these hyperparameters.
3. In the final loss function, is it reasonable to simply add $\mathcal{L}_{MSE}、\mathcal{L}_{PI_t}、\mathcal{L}_{PI_f}$? Given that the severity of distribution shifts varies across different datasets, and that the importance of frequency-domain information is relatively low in such datasets, the model should be allowed to learn the appropriate weights for both components on its own.
4. It is noted that in the experiments, the sequence length (seq_len) was uniformly set to 96, which undermines the performance of other baselines, as FITS[1], PatchTST[2], and DLinear[3] have indicated that their methods perform better with longer input sequences. It is suggested to provide experimental results comparing seq_len as a hyperparameter rather than fixing it at 96.
5. It is noted that multiple experts are used in both the time domain and frequency domain, which will increase the runtime of the model. It is suggested to compare the runtime with other methods.

### Questions
Please refer to weeknesses.

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
4

### Summary
This paper proposes a new architecture, Time-Frequency Pattern-Specific (TFPS), designed for time series forecasting, particularly under challenging conditions involving concept drift within the data. The key idea revolves around addressing the limitations of conventional uniform distribution modeling (UDM) by recognizing that different segments or "patches" within a time series exhibit distinct patterns and distributional shifts. These shifts may stem from factors such as sudden events, gradual trend changes, or different operating modes, making accurate forecasting difficult for models trained on a single global pattern. TFPS tackles this problem through a multi-faceted approach. First, it employs a Dual-Domain Encoder (DDE) that analyzes both time and frequency domain features, enabling a richer understanding of temporal dynamics and their potential shifts. Second, a Pattern Identifier (PI) utilizes subspace clustering to dynamically group patches exhibiting similar patterns. Finally, a Mixture of Pattern Experts (MoPE) leverages multiple specialized expert models, each trained on a specific pattern identified by the PI. This allows TFPS to adapt its predictions based on the identified pattern of a given patch, leading to improved accuracy.

### Strengths
(1) Utilizing both time and frequency domain information provides a comprehensive perspective on data, capturing both trend and periodic patterns, which is essential for handling complex time series.
(2) The use of PI and MoPE allows TFPS to handle distribution shifts by learning and adapting to specific patterns within different data segments.
(3) Extensive experiments on real-world datasets demonstrate the effectiveness and competitiveness of TFPS compared to existing methods.

### Weaknesses
 (1) The authors acknowledge that the patch length is currently determined heuristically, which might limit generalizability and performance in cases with indivisible lengths or multi-period characteristics.
(2) The model's ability to adapt to entirely new patterns, such as those arising from unforeseen events, is not explicitly addressed and remains an open question.
(3) While not explicitly mentioned, the use of multiple expert models and the dual-domain encoding approach could increase computational complexity compared to simpler models. This aspect would require further analysis and optimization for practical implementation in real-time applications. The claim of a 'remarkable balance between performance and efficiency' is not fully supported by the provided data, particularly when compared to models like DLinear, where the gap in memory and GPU footprint remains significant even with a lighter backbone model. 
(4) There are notable inconsistencies between the reported results for the Traffic dataset and those in the original papers for baseline methods, raising concerns about the experimental setup. For instance, iTransformer's reported MSE and MAE values differ significantly from those in the original paper.
(5) The reported results for Patch-TST also show significant discrepancies compared to the original paper. For example for MSE, the original paper's results are: 0.370, 0.413, 0.422, 0.447 while the reported results are: 0.413, 0.460, 0.497, 0.501. These discrepancies raise concerns about the experimental setup and fairness of the comparisons throughout the paper.

### Questions
(1) In Figure 1, the authors posit that a combined time and frequency domain perspective provides a more comprehensive view of data shifts. However, the provided heatmaps do not clearly support this claim. For instance, in Figure 1(a), the time-domain heatmap highlights significant MMD values for patch #10, while the actual drift begins at patch #9. Similarly, the frequency-domain heatmap includes patches #7 and #8 in the drift region, which is inaccurate. A similar discrepancy is observed in Figure 1(b), where the differences between patches 5, 6, 7, 8, and subsequent patches are not readily apparent. Consequently, this figure does not provide compelling evidence for the superiority of the combined domain approach in detecting shifts.

(2) Based on Figure 1, it appears that the sudden drift is detected due to the data's relatively consistent cyclical patterns across patches. How would the method perform if the data lacks such clear cyclical properties? Would the entire sequence of patches be incorrectly identified as a drift, even if the underlying data distribution changes gradually?

(3) Although this research draws comparisons to traditional time-domain and frequency-domain techniques, a more rigorous evaluation would involve comparisons with MoE-based methods. A list of relevant works is provided below.

* Dish-ts: a general paradigm for alleviating distribution shift in time series forecasting. (AAAI-23) .
* Reversible Instance Normalization for Accurate Time-Series Forecasting against Distribution Shift. (ICLR 2022).
* OneNet: Enhancing Time Series Forecasting Models under Concept Drift by Online Ensembling. (NeurIPS 2023).
* Calibration of Time-Series Forecasting: Detecting and Adapting Context-Driven Distribution Shift. (KDD '24).
* Addressing Distribution Shift in Time Series Forecasting with Instance Normalization Flows. arXiv preprint arXiv:2401.16777.
* MixMamba: Time series modeling with adaptive expertise. (Inf. Fusion 2024).
* Mixture-of-Linear-Experts for Long-term Time Series Forecasting. (AISTATS 2024).

(4) Please elucidate the specific contributions of the PI the gate network to TFPS. Why both components are essential for the system’s performance would be beneficial. Furthermore, conducting an ablation study, which involves comparing the model’s performance with and without the separate PI module, would provide empirical validation of its significance.

(5) A rigorous computational complexity analysis would provide valuable insights into the trade-offs between model complexity and performance gains.

(6) I suggest that authors: Provide clear definitions for q and d in D. Explain the rationale behind controlling column size using Equation (3). Clarify the purpose of the second constraint in Equation (4). Include a theoretical justification for how these constraints improve representation learning. Conduct an ablation study comparing model performance with and without these constraints.

(7) As noted in Shazer et al.’s work on Mixture-of-Experts, gating networks often exhibit a tendency to select the same k experts for routing patches. To mitigate this issue and encourage diversity among the expert modules, regularization and load balancing techniques are typically employed. However, it remains unclear how the proposed model addresses this specific challenge and promotes diversity among its expert modules.

(8) The datasets employed in this study are relatively low-dimensional. It is recommended to conduct experiments on high-dimensional time series datasets, such as the Traffic dataset. Additionally, a discussion on potential scalability challenges and necessary modifications to the TFPS architecture for efficient handling of high-dimensional data would be valuable.

(9) Given that the Patch-TST module used as encoder in this work already incorporates an ReVIN layer to mitigate distribution shifts in time series data. I am wondering if authors consider this point and how it affect the process of PI?

### Soundness
2

### Presentation
3

### Contribution
2
