# Decoupling Variable and Temporal Dependencies: A Novel Approach for Multivariate Time Series Forecasting

- Decision: Reject
- Scores: 3, 5, 6

## Abstract
In multivariate time series forecasting using the Transformer architecture, capturing temporal dependencies and modeling inter-variable relationships are crucial for improving performance. However, overemphasizing temporal dependencies can destabilize the model, increasing its sensitivity to noise, overfitting, and weakening its ability to capture inter-variable relationships. We propose a new approach called the Temporal-Variable Decoupling Network (TVDN) to address this challenge. This method decouples the modeling of variable dependencies from temporal dependencies and further separates temporal dependencies into historical and predictive sequence dependencies, allowing for a more effective capture of both. Specifically, the simultaneous learning of time-related and variable-related patterns can lead to harmful interference between the two. TVDN first extracts variable dependencies from historical data through a permutation-invariant model and then captures temporal dependencies using a permutation-equivariant model. By decoupling variable and temporal dependencies and historical and predictive sequence dependencies, this approach minimizes interference and allows for complementary extraction of both. Our method provides a concise and innovative approach to enhancing the utilization of temporal features. Experiments on multiple real-world datasets demonstrate that TVDN achieves state-of-the-art performance.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors investigate the problem of multivariate time series forecasting. The authors claim that overemphasizing temporal dependencies can destabilize the model making the model sensitive to noise. And the simultaneous learning of time-related and variable-related patterns can lead to harmful interference. So the authors propose the temporal-variable decoupling network to model the temporal and variable relationships respectively. The authors evaluate the proposed method on several datasets and achieve good performance.

### Strengths
N.A.

### Weaknesses
1.	The relationship of inter-variables in the time sequence should have an instantaneous effect, but I am surprised that the author did not quote related work in this area [1,2].  
2.	Why do learning time-related and variable-related patterns simultaneously harm inference? Please provide some rigorous evidence.  
3.	The author said that Transformer puts too much emphasis on extracting time-dependent patterns and did not provide enough evidence that this statement was suspicious of the rationality of this assertion. From the perspective of the data generation process, future data generation has also received the effects of time delay and cross variables at the same time, which is the opposite of separating these two factors at the same time. This method highlights the intra-and inter- time series relationships, but many methods have studied this problem, such as [3].  
4.	Why does the proposed method need to model cross-variable relationships and then model cross-temporal relationships? What is the motivation behind it, what if it is in turn?  
5.	More recent comparison methods need to be considered, for example [4] [5].

### Questions
Please refer to Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this paper, the authors argue that overemphasizing temporal dependencies can destabilize Transformer-based models, increasing their sensitivity to noise, overfitting, and weakening their ability to capture inter-variable relationships. Therefore, they propose a new Temporal-Variable Decoupling Networks (TVDN) which decouples the modeling of variable dependencies from temporal dependencies to address this challenge.

### Strengths
1.	The proposed TVDN decouples the modeling of variable dependencies and temporal dependencies which useful in long-term time series forecasting.
2.	TVDN also separates the modeling of temporal dependencies into historical dependencies and predictive dependencies, with the latter having received relatively little attention in previous works.

### Weaknesses
1.	In line 61, the authors said that “linear models and Cross-Variable Transformers do not extract accurate temporal dependencies because they essentially map historical series as unordered sets … ”, I disagree with the assertion that these models treat historical series as unordered sets. for example, the linear models predict future time steps by the equation $\hat{x}_{i+1}=\omega_{1}x_{i-L+1}+…+\omega_{L}x_{i}$, clearly treating historical series as ordered sets.
2.	In equation (5) and (6), the authors define $T^{0}=Z_{h}+ Z_{CVE}$; however, in figure 2, it seems that the input of PSTD is consists only $Z_{CVE}$.
3.	Also in figure 2, I cannot find the step (2) in the method section.
4.	In line 246, $Z_{proj}$ is mentioned without a prior definition, I believe it should be $Z_{h}$.
5.	In line 215, the notation $Z_{CVE} \in {R}^{O \times D}$ is used, yet I cannot find the definition of $D$.
6.	In line 315,“the permutation-invariant models overlook dynamic temporal features ”seems inappropriate. 
7.	In line 332, I disagree with the claim that “we identified that the bottleneck of the traditional Transformer model lies in the ineffective utilization of historical sequence information”, because the experimental results of PatchTST have shown that longer historical sequences will lead better performance. In addition, the reason why the transformer model performs poorly is that it over-captures channel dependencies, which can also be seen in the experimental results of PatchTST and DLinear. Furthermore, the poor performance of the Transformer model can be attributed to its tendency to over-capture channel dependencies, as evidenced by the experimental results of both PatchTST and DLinear.
8.	The experiments are unfair, since PatchTST and DLinear perform better with longer historical windows. Although the authors have conducted experiments with $L=144$, I suggest the authors also set $L=336$ and $L=512$, and compared the results with PatchTST and DLinear.
9.	In Figure 9, Transformer performs better than Transformer Decoder only which is insistent with  ”even with a significant reduction in historical information …”in Line 912.

### Questions
please see weaknesses.

### Soundness
3

### Presentation
2

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
This paper introduces a dual-phase deep learning network architecture called the Temporal-Variable Decoupling Network(TVDN), which decouples the modeling of variable dependencies from temporal dependencies. First, during the variable dependence learning phase, the Cross-Variable Encoder (CVE), a permutation-invariant model, completely disregards the temporal dependence of the sequence and only extracts cross-features between variables, generating an initial prediction sequence. Once the CVE stabilizes, the second phase shifts to temporal dependency learning. The Cross-Temporal Encoder (CTE) divides time series dependence into two parts: Historical Sequence Temporal Dependency (HSTD), and Prediction Sequence Temporal Dependency (PSTD). The outputs of HSTD and PSTD are then fused to correct the initial prediction from the variable dependence learning phase. The approach reduces the risk that overemphasizing temporal dependencies can overfit the model, and enables broader parameter space exploration. The experiment in this paper shows that TVDN achieves state-of-the-art (SOTA) performance in electricity, traffic, weather, four ETT, and exchange fields by comparing it with some of the latest Time-Series Forecasting Transformer (TSFT) methods.

### Strengths
1.	TVDN decouples the modeling of variable dependencies from temporal dependencies to reduce the interference between the two, enhance the utilization of temporal features, and improve forecasting accuracy.
2.	TVDN adopts a dual-phase architecture, starting with CVE to learn inter-variable dependencies and then shifting to CTE focused on temporal dependency learning. The two-phase approach effectively addresses the interference of variable and temporal learning, which avoids leading to a degradation of models’ performance.
3.	The proposed method demonstrates SOTA performance in real-world forecasting benchmarks by capturing complex dependencies across variables and time. This is achieved with minimal computational overhead, making the model efficient and scalable.

### Weaknesses
1.	The experiment focuses on predicting accuracy and sensitivity to temporal dependencies but does not assess computational overhead and resource requirements. To provide a more comprehensive evaluation, it is recommended to include specific metrics for computational cost, such as training time, inference time, memory usage, and FLOPs. By reporting these metrics, the paper could offer a clearer picture of the model’s practical feasibility, particularly for deployment in large-scale, real-time, or resource-constrained environments.
2.	The experiment in Section 4.3 shows that the model’s performance significantly declines when the temporal order is shuffled, indicating a strong dependency on temporal features. The high dependency may decrease the model’s effectiveness on datasets that don’t have clear temporal patterns, limiting its application domain.

### Questions
1.	Given the complexity of TVDN’s dual-phase network structure, could the authors provide a quantitative comparison of computational costs versus accuracy gains relative to baseline models to allow for a more objective assessment of potential trade-offs between accuracy and efficiency?
2.	In real-world applications, temporal sequences are often affected by various types of noise, which may impact model performance. Could the paper conduct experiments by introducing specific noise types, like Gaussian noise, to simulate random disturbances or missing values to simulate incomplete data, to observe TVDN's performance in these noisy environments, and to assess its robustness to noise?
3.	This paper has shown that TVDN performs excellently on various datasets. Is there any limitation to the model? In cases of data scarcity or extremely complex intervariable relationships, can the model maintain its performance?

### Soundness
3

### Presentation
3

### Contribution
3
