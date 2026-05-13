# HoTPP Benchmark: Are We Good at the Long Horizon Events Forecasting?

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
Accurately forecasting multiple future events within a given time horizon is crucial for finance, retail, social networks, and healthcare applications. Event timing and labels are typically modeled using Marked Temporal Point Processes (MTPP), with evaluations often focused on next-event prediction quality. While some studies have extended evaluations to a fixed number of future events, we demonstrate that this approach leads to inaccuracies in handling false positives and false negatives. To address these issues, we propose a novel evaluation method inspired by object detection techniques from computer vision. Specifically, we introduce Temporal mean Average Precision (T-mAP), a temporal variant of mAP, which overcomes the limitations of existing long-horizon evaluation metrics. Our extensive experiments demonstrate that models with strong next-event prediction accuracy can yield poor long-horizon forecasts and vice versa, indicating that specialized methods are needed for each task. HoTPP includes large-scale datasets with up to 43 million events and provides optimized procedures for both autoregressive and parallel inference, paving the way for future advancements in the field.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces HoTPP (Horizon Temporal Point Process Benchmark), a benchmark for evaluating long-horizon event sequence prediction models. Its main contributions include: proposing a novel evaluation metric called Temporal mean Average Precision (T-mAP), inspired by object detection metrics in computer vision, which properly handles variable-length sequences within a prediction horizon and accounts for false positives and false negatives; demonstrating through comprehensive analysis that models with high next-event prediction accuracy don't necessarily perform well at long-horizon forecasting, suggesting the need for specialized approaches for each task; developing the HoTPP benchmark, which includes large-scale datasets from diverse domains (finance, healthcare, social networks) with up to 43 million events, implementation of various modeling approaches (including rule-based baselines, intensity-free methods, intensity-based methods, and Next-K prediction models), optimized procedures for both autoregressive and parallel inference, and theoretical proof of T-mAP computation correctness; and revealing through extensive experiments across multiple datasets the trade-offs between next-event and long-horizon prediction performance, benefits of Next-K approaches for long-horizon predictions, importance of proper sequence length selection, and analysis of label distribution entropy degradation in autoregressive predictions.

### Strengths
1. Innovative Evaluation Metric: The paper introduces Temporal mean Average Precision (T-mAP), a novel metric inspired by object detection, which addresses limitations in existing evaluation methods for long-horizon forecasting by accurately handling false positives and negatives, offering a refined measurement of model performance in Marked Temporal Point Processes (MTPP).
2. Practical Benchmark: The HoTPP benchmark developed in this work includes large-scale, diverse datasets and optimized inference procedures, establishing a standardized framework that supports both autoregressive and parallel inference, greatly enhancing research accessibility and reproducibility in long-horizon event forecasting.
3. Comprehensive Empirical Analysis: The paper rigorously evaluates various models, including rule-based and advanced neural methods, across multiple datasets, providing robust empirical evidence that reveals critical insights into the performance trade-offs of next-event vs. long-horizon forecasting.
4. Clear and Structured Presentation: The paper clearly articulates the challenges in long-horizon event prediction, explaining the proposed methodology and its advantages with illustrative figures and well-organized tables, making complex concepts acc

### Weaknesses
1. Limited Justification of Metric Selection: While the T-mAP metric is an innovative contribution, the paper could strengthen its justification for why T-mAP is superior to other established metrics in specific application scenarios. Including more detailed comparisons with alternative metrics, such as Order-preserving Wasserstein Distance (OPW), could provide further evidence of T-mAP's effectiveness, especially in complex event sequences. The paper does not sufficiently address scenarios where event ordering is critical, and a more in-depth analysis of T-mAP's behavior in such cases is needed.

2. Lack of Fine-Grained Analysis for Different Domains: The datasets span diverse fields like healthcare and social media. However, the paper does not profoundly explore how T-mAP performs within these domains. Analyzing domain-specific challenges or model performance variations across fields could add depth and highlight the metric’s adaptability, further demonstrating HoTPP’s real-world applicability. Specifically, the paper should investigate whether T-mAP's sensitivity to timestamp accuracy is consistent across domains with varying levels of temporal precision.

3. Computational Constraints on Benchmark Implementation: Some models, like the continuous-time LSTM, require extensive computational resources, limiting their practical applicability. The paper could improve by suggesting or including optimizations, such as more efficient GPU implementations or leveraging hybrid models, making the benchmark more accessible to researchers with limited resources. The paper should also provide a more detailed analysis of the computational cost of each model, including memory usage and training time, to guide users with different hardware capabilities.

4. Limited Exploration of Next-K Models: Although the paper discusses Next-K models and their potential in improving long-horizon forecasting, there is little exploration of variations within this model family. Providing examples or implementing alternative Next-K structures could substantiate the claims regarding their advantages, offering actionable insights for researchers interested in non-autoregressive alternatives. The paper should also explore the impact of different values of K on model performance and computational cost.

5. Lack of Qualitative Error Analysis: The paper could benefit from qualitative error analysis to clarify why some models underperform on long-horizon metrics. Visual examples or error case studies might offer valuable insights into prediction failures, guiding future model improvements by highlighting common error patterns in long-horizon event forecasting. The paper should include examples of both successful and failed predictions, along with an analysis of the underlying causes.

### Questions
1. Could the authors provide more detailed reasoning on why T-mAP is the most suitable metric for long-horizon MTPP evaluation? A comparison with other metrics, such as OPW, would help clarify the unique advantages of T-mAP for certain datasets or applications. Are there specific scenarios where T-mAP particularly excels?

2. How does T-mAP adapt to different domains represented in the HoTPP benchmark, such as healthcare vs. social media? It would be helpful if the authors could provide additional domain-specific analysis or clarify if they observed any notable trends in metric performance across different datasets.

4. Given the computational intensity of some methods (e.g., continuous-time LSTM), what optimizations, if any, do the authors recommend for users with limited hardware resources? Would simplifying certain models or using hybrid methods maintain benchmark validity while improving accessibility?

4. Next-K models are briefly discussed, but can the authors elaborate on alternative structures or settings within this family of models? Exploring how these models perform differently across long-horizon tasks could provide insights into their benefits or limitations and would help clarify if more complex Next-K structures could outperform standard autoregressive models.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper introduces a new metric, Temporal mean Average Precision (T-mAP), which is designed for evaluating long-horizon predictions in marked temporal point processes (MTPP). This offers a new perspective on evaluating forecasting accuracy beyond traditional metrics like OTD. It also introduce HoTPP, a new benchmark for long-horizon forecasting, which provides large datasets and optimized procedures for both autoregressive and parallel inference.

### Strengths
1. The paper is well-organized, with clear sections delineating the introduction, related work, methodology, experiments, and conclusions.
2. Figures and tables are used effectively to illustrate concepts and present experimental results.
3. The significance of forecasting multiple future events is substantial.

### Weaknesses
1. The motivation in section 3, while intended to address deficiencies in existing methods such as OTD, appears weakly articulated. The example provided in Figure 2 lacks clarity, particularly why OTD cannot correctly match the last triangle with the ground truth. Furthermore, the assertion that OTD is computed between fixed-size prefixes is confusing since n_p and n_gt vary, which contradicts the description in line 178 to 185.
2. Some claims are not clear. For example, in line 230 T-mAP identifies the matching that maximizes both precision and recall simultaneously. Typically, these metrics are in a trade-off relationship. How T-mAP manages to maximize both?
3. The experimental section (Section 6.1) lacks specific references to the methods and datasets discussed, which makes it difficult to follow and verify the stated findings. Direct references to specific methods and datasets should be included to enhance clarity.

### Questions
1. Deep methods do not necessarily outperform rule-based methods, how to illustrate the superiority of the proposed metric by comparing them?
2. What is the main message of section 4.3? It seems to only show that the metric increases monotonically with delta.
3. Can authors discuss which scenarios are most suitable for different types of metrics? Like how does the proposed metric handle sparse or highly irregular data compared to traditional ones?

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
2

### Summary
This paper benchmarks the task of long horizon events forecasting. The main contribution of this paper is to propose a new metric, namely T-mAP. Moreover, this paper also includes large-scale datasets with up to 43 million events. Although with these contributions, this paper is not well-written and not easy to understand.

### Strengths
- This paper proposes a new metric, namely T-mAP, to better evaluate the performance of long horizon events forecasting. 

- This paper includes large-scale datasets with up to 43 million events. 

- This paper release HoTPP open-source benchmark to facilitate future research.

### Weaknesses
 - This paper is not well-written and hard to follow. The main contribution of this paper is to propose T-mAP to evaluate models on the task of long horizon events forecasting. However, why T-mAP is better than the existing metric, i.e., OTD, is not clearly introduced. The paper lacks a rigorous explanation of the specific shortcomings of OTD, such as its sensitivity to fixed-length prefixes and the need for calibrated model outputs, which makes it difficult to understand the true advantage of T-mAP. A more detailed analysis, including mathematical formulations and illustrative examples, would be beneficial.

- The experiments are not extensive. In the title of this paper is about long-horizon event forecasting, but the experiments covers equally on the topic of the next-item forecasting. The paper does not adequately demonstrate the performance of the proposed metric and models specifically in the context of long-horizon forecasting. The inclusion of next-item forecasting results dilutes the focus and does not provide sufficient evidence of the metric's effectiveness for long-horizon predictions. A more targeted experimental design, focusing on varied long-horizon scenarios, is needed.

- The number of compared baselines is not many, and the baselines are not proposed recently. It seems that the topic of event forecasting is not very hot, so the motivation that we need a benchmark is very strong. The selection of baselines lacks diversity and does not include state-of-the-art methods. The absence of recent and competitive baselines weakens the benchmark's ability to provide a comprehensive evaluation of the proposed metric and models. A more thorough comparison with a wider range of contemporary methods is necessary to establish the benchmark's relevance and utility.

### Questions
- How T-mAP is better than the existing metric? 

- More analysis on long-horizon event forecasting are needed. 

- Why the baselines are not new?

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
2

### Summary
The authors introduce Temporal mean Average Precision (T-mAP), a temporal variant of mAP that overcomes the limitations of existing long-term evaluation metrics. They also release HoTPP, the first benchmark specifically designed to evaluate long-term MTPP predictions, which includes a large-scale dataset of up to 43 million events.

### Strengths
The author's motivation is clearly expressed, the approach sounds interesting, the problem of modeling long sequences of events is well addressed, and the large dataset developed has the potential to advance the field.

### Weaknesses
1. The paper is difficult to understand. What is the ‘structured descriptions of each event’, what is the challenges of autoregressive prediction in line 48. What are the challenges of autoregressive prediction in line 052? How are subsequences handled for each event type in line 99. This increases the difficulty for readers to understand, and it is recommended that the author explain these terms in more detail.

2. The motivation is vague. Why do we need long-term event prediction? In fact, we can execute Next-event task multiple times to get similar results.

3. How does the proposed metrics perform in a long-tail prediction scenario?

4. Does the proposed metric take into account the time error of event occurrence? If the time interval corresponding to the event is far away, can the method cope with this situation?

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
3
