# CATCH: Channel-Aware Multivariate Time Series Anomaly Detection via Frequency Patching

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
Anomaly detection in multivariate time series is challenging as heterogeneous subsequence anomalies may occur. Reconstruction-based methods, which focus on learning nomral patterns in the frequency domain to detect diverse abnormal subsequences, achieve promising resutls, while still falling short on capturing fine-grained frequency characteristics and channel correlations. To contend with the limitations, we introduce CATCH, a framework based on frequency patching. We propose to patchify the frequency domain into frequency bands, which enhances its ability to capture fine-grained frequency characteristics. To perceive appropriate channel correlations, we propose a Channel Fusion Module (CFM), which features a patch-wise mask generator and a masked-attention mechanism. Driven by a bi-level multi-objective optimization algorithm, the CFM is encouraged to iteratively discover appropriate patch-wise channel correlations, and to cluster relevant channels while isolating adverse effects from irrelevant channels. Extensive experiments on 9 real-world datasets and 12 synthetic datasets demonstrate that CATCH achieves state-of-the-art performance. We make our code and datasets available at \textcolor{blue}{\href{https://anonymous.4open.science/r/CATCH-E535}{https://anonymous.4open.science/r/CATCH-E535}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposed a method called CATCH 
 for Multivariate Time Series Anomaly Detection.

### Strengths
1. The paper is well structured.

2. The architecture of CATCH is clearly articulated.

3. Nice figures help to understand the proposed CATCH

4. The proposed CATCH has been verified by extensive experiments.

5. The code of the proposed method has been open, thus it has good reproducibility.

### Weaknesses
1. Figures are not self-explanatory sufficiently such as Fig. 1(b).
2. Lack of parameter settings, resulting in weak reproducibility.
3. Table 1 shows that the proposed method outperforms all baselines for all tested datasets. Does this mean that the proposed method can win in any dataset/application?
4. The tested datasets are not the ones most commonly tested by the baselines. Why? Please test some datasets tested by your baselines.
5. No guidance on choosing parameters for your proposed method?

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a new multivariate time series anomaly detection method that operates in the frequency domain. The proposed method introduces two main components: (1) a frequency patching mechanism that segments the frequency domain into bands for capturing fine-grained frequency characteristics, and (2) a channel fusion module that leverages patch-wise masking and masked attention to find relevant channel correlations. The approach is optimized using a bi-level multi-objective algorithm.

### Strengths
1.	The paper exhibits good presentation standards. Specifically, the quality of figures can reach the bar of ICLR. The visualizations effectively communicate complex concepts and experimental results.
2.	The idea of frequency patch learning is novel in the field of time series anomaly detection, while I am not sure whether this idea is proposed in the domain of time series modeling.  
3.	The authors released an anonymous GitHub repository, which improves reproducibility.

### Weaknesses
1. The foundational motivation of the paper needs stronger articulation. The authors primarily focus on the limitations of reconstruction-based methods, specifically their tendency to overlook details in high-frequency bands. However, several studies have already explored leveraging frequency information in MTSAD. The introduction section could benefit from a detailed comparison between current frequency-based methods and the proposed approach. A structured comparison that highlights the specific gaps addressed by CATCH would strengthen the paper’s positioning and clarify its contributions to the field. Consider including a table or a structured comparison in the introduction that clearly outlines how CATCH addresses specific gaps in existing frequency-based MTSAD methods, such as handling high-frequency information, computational efficiency, and the ability to capture channel correlations.
2. The experimental evaluation would benefit from a broader comparison with relevant frequency-based methods. Although several approaches (e.g., SR-CNN, PFT, TFAD, and Dual-TF) are mentioned, they are notably absent from the experimental comparisons. To enhance this aspect, it would be constructive to include these specific methods in the experimental comparisons and to explain why comparing against these particular approaches is valuable for demonstrating CATCH’s contributions.
3. The paper’s central claim regarding superior detection of frequency-specific anomalies requires more rigorous theoretical or empirical validation. While the method aims to better capture fine-grained frequency characteristics, there is no dedicated experimental design to verify this capability. To address this, consider adding specific experiments or analyses that can demonstrate superior detection of frequency-specific anomalies. For instance, you could create synthetic datasets with known frequency-specific anomalies or analyze performance across different frequency bands.
4. The manuscript requires careful editorial revision to address. There are some typos like “results” in the abstract. Also, some citations should be updated to published versions instead of preprints.

### Questions
Could you elaborate on how your frequency patching approach differs from existing frequency-domain analysis methods?

### Soundness
2

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
This paper introduces CATCH, a Multivariate Time Series Anomaly Detection framework that enables the simultaneous detection of point and subsequence anomalies through frequency patching. By leveraging Fourier Transformation across time and frequency domains, CATCH enhances subsequence anomaly detection and utilizes the Channel Fusion Module (CFM) to adaptively exploit channel correlations. The CFM integrates a channel correlation discovery mechanism and a bi-level multi-objective optimization process to effectively isolate irrelevant channels and cluster relevant ones.

### Strengths
1. The paper introduces CATCH, a novel framework that enhances the detection of both point and subsequence anomalies in multivariate time series through frequency domain patching. This approach creatively combines existing ideas with new methodologies, particularly through its Channel Fusion Module (CFM).
2. The paper is clearly organized and well-written.
3. CATCH addresses some limitations of existing methods. Its integration of frequency and time domain analysis holds promise for impactful applications in various fields.

### Weaknesses
1.	The paper presents modules in isolation, lacking a cohesive explanation of their interactions, which can confuse readers regarding the overall system functionality. A clearer narrative linking module interactions would enhance comprehension. Specifically, the flow of data and transformations between the Mask Generator, Channel-Masked Transformer Layer, and the Time-Frequency Reconstruction Module (TFRM) is unclear. The paper does not sufficiently articulate how the outputs of one module serve as inputs to the next, making it difficult to understand the overall architecture.
2.	Key operations like instance normalization and frequency domain patching are described without adequate context, leaving readers questioning their necessity. For instance, the paper does not explain why instance normalization is applied before the frequency domain patching, or how these steps contribute to the overall anomaly detection performance. The lack of motivation for these operations makes it difficult to assess their importance.
3.	The innovation behind the Channel Fusion Module (CFM) is not sufficiently highlighted, particularly regarding the necessity of the masking mechanism and its impact on detection performance. The paper does not clearly explain how the mask is generated, what criteria are used to determine which channels are masked, and how this masking mechanism improves the channel correlation discovery. The adaptive nature of the CFM is not well-justified, leaving the reader to question its effectiveness.
4.	The goals and significance of the Time-Frequency Reconstruction Module (TFRM) are not clearly articulated, potentially leading to misunderstandings about its contributions. The paper does not explain why both time-domain and frequency-domain reconstruction losses are necessary, or how they contribute to the final anomaly score. The specific advantages of using both domains for reconstruction are not clearly presented.

### Questions
1.	In line 53, the term "heterogeneous subsequence anomalies" is mentioned. Could you provide a specific definition for heterogeneous subsequence anomalies? How do they differ from or relate to regular time series anomalies?
2.	In sections 2.2 and 2.3, in addition to discussing the current state of research, could you include some definitional descriptions? For instance, elaborating on the relationships between channels and frequency domain information in the MTSAD problem could enhance the clarity and structure of the article.
3.	In section 3.1, the description of the framework structure provides technical details, but it lacks a clear explanation of the processes involved. The roles and relationships of the various modules don’t seem to connect well, which affects the logical flow. Adding descriptions of their functions and interrelations could improve the overall coherence.
4.	In lines 230 to 245, where the mathematical principles of the framework are introduced, the abundance of symbols can be overwhelming. It would be clearer if each symbol were introduced upon its first occurrence, or if specific definitions were provided before delving into the mathematical principles and formulas.
5.	In line 369, does the description suggest that contextual and global anomalies are considered as point anomalies in this paper? Similarly, does this apply to the subsequence types in parentheses? It seems that in the field of time series anomaly detection, anomalies are usually classified into various categories without clarifying their hierarchical relationships. This may need further investigation and explanation.
6.	In Figure 5, when examining the temporal scores and frequency domain scores separately, both seem to serve as good anomaly detection metrics. Why does the paper choose to combine these two scores? Are there any examples where the temporal score performs poorly but can be compensated by the frequency domain score (or vice versa)? Such results could better illustrate the effectiveness of this anomaly scoring approach.
7.	There are some typographic faults: The reference in line 185 needs to be enclosed in parentheses; in line 161, there is a spelling error, it should be "modules" instead of "Moudles"; in line 320, it would be better to align the text and the image on the same page.

### Soundness
3

### Presentation
3

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
This paper centers on temporal anomaly detection and introduces an algorithm capable of capturing fine-grained frequency characteristics and channel interdependencies. The proposed method leverages frequency patches to discern subtle frequency details and employs channel fusion techniques to identify correlations among different channels. The experimental results indicate that the algorithm delivers state-of-the-art performance across various datasets.

### Strengths
1. The paper introduces innovative frequency patching techniques and a Channel Fusion Module (CFM) in
the field of multivariate time series anomaly detection, which can more finely capture frequency
characteristics and channel correlations, marking a significant improvement over existing methods.

2. The experimental findings demonstrate that the proposed methodology possesses commendable performance.

### Weaknesses
1. The methodological descriptions and accompanying figures are not entirely congruent, which poses challenges for readers. For instance, the structure on the left side of Figure 2 appears disorganized, obscuring the input data and its flow for the reader. Furthermore, the freq-score and time-score mentioned in Figure 3 lack corresponding textual or formulaic explanations in the relevant sections, thereby hindering readers' comprehension of the actual computation of the anomaly scores.

2. While the CFM is an innovative feature, its complexity might be challenging for some readers to grasp.
The paper could provide more intuitive explanations or diagrams to help readers better understand how
the CFM operates.

3. The experiments did not incorporate classic datasets such as ASD or SWaT.

### Questions
1. As the paper indicates, frequency characteristics exhibit long-tailed distributions, with the majority of information concentrated in the low-frequency band. Thus, what is the rationale behind the focus of this study on capturing details within the high-frequency band? In reality, as depicted in Figure 1(a), there are already significant differences between normal and anomalous data in the low-frequency band. 
2. Was point adjustment employed when assessing the algorithm's performance? 
3. Why does Table 2, presenting the multi-metric results, only illustrate performance on three datasets? It might be beneficial to include all results in the appendix for comprehensiveness.

### Soundness
3

### Presentation
2

### Contribution
3
