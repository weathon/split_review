# Investigating Pattern Neurons in Urban Time Series Forecasting

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Urban time series forecasting is crucial for smart city development and is key to sustainable urban management. Although urban time series models (UTSMs) are effective in general forecasting, they often overlook low-frequency events, such as emergencies and holidays, leading to degraded performance in practical applications. In this paper, we first investigate how UTSMs handle these infrequent patterns from a neural perspective. Based on our findings, we propose $\textbf{P}$attern $\textbf{N}$euron guided $\textbf{Train}$ing ($\texttt{PN-Train}$), a novel training method that features (i) a $\textit{perturbation-based detector}$ to identify neurons responsible for low-frequency patterns in UTSMs, and (ii) a $\textit{fine-tuning mechanism}$ that enhances these neurons without compromising representation learning on high-frequency patterns. Empirical results demonstrate that $\texttt{PN-Train}$ considerably improves forecasting accuracy for low-frequency events while maintaining high performance for high-frequency events. The code is available at https://anonymous.4open.science/r/PN-Train.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes PN-Train, which detect and fine-tune pattern neurons to improve the forecasting performance on low-frequency patterns.

### Strengths
- Improving forecasting performance on low-frequency events is interesting and challenging.
- The idea of pattern neuron is intuitive and reasonable.
- The proposed framework outperforms existing works.

### Weaknesses
 - The framework requires explicitly defined low-frequency patterns, i.e., holidays, and a dataset with low-frequency patterns is also required (as in Eq(3)). It is unclear whether the framework could handle implicit low-frequency patterns, such as those arising from unrecorded events or anomalies. The reliance on explicit patterns limits the applicability of the method in real-world scenarios where such patterns are not always known or easily defined.
- In PNV, it will be better to test whether removing PNs leads to significant performance decreasing on high-frequency patterns, since PNs could be critical for all patterns rather than just low-frequency patterns. The current evaluation focuses on low-frequency patterns, but the impact on overall model performance, especially on high-frequency patterns, is not fully explored. It is important to understand if the identified pattern neurons are specialized for low-frequency patterns or if they contribute to the model's general forecasting ability.
- Minor errors. For example, in Fig.2, PNV seems to deactivate neurons which are not pattern neurons. This raises concerns about the precision of the pattern neuron identification process and whether the method might be inadvertently affecting neurons that are important for other aspects of the time series.

### Questions
- In line2 Algorithm1, why do author filter out low-frequency samples?
- Can we allocate low-frequency patterns by categorizing neuron activations? 
- Is the framework able to handle two or more low-frequency patterns?

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
5

### Summary
This work introduces PN-Train, a novel urban time series forecasting method that significantly improves prediction accuracy by identifying and fine-tuning pattern neurons associated with low-frequency events, such as holidays. PN-Train employs a perturbation-based detector to recognize these neurons and enhances them through a fine-tuning mechanism without compromising the representation learning of high-frequency patterns. Empirical results demonstrate that PN-Train considerably boosts forecasting accuracy for low-frequency events while maintaining high performance for high-frequency events.

### Strengths
(1) The work proposes a perturbation-based detector that effectively identifies pattern neurons associated with low-frequency patterns.

(2) It designs a fine-tuning mechanism to enhance these pattern neurons without compromising the representation of high-frequency patterns. This design ensures high accuracy for both low-frequency and high-frequency events.

(3) The study provides empirical results that verify the effectiveness of the proposed method, demonstrating significant performance improvements.

### Weaknesses
(1) The distinction between low-frequency and high-frequency events is primarily between holidays and non-holidays, which may not have substantial practical significance. The paper does not adequately justify why this specific dichotomy is important, especially given that other time series forecasting methods are also capable of improving accuracy for both types of events simultaneously. A more compelling case could be made by focusing on anomaly detection or traffic prediction under more genuinely anomalous events, such as unexpected traffic surges due to accidents or sudden weather changes, which would have more direct real-world implications.

(2) The absence of open-source code makes it difficult to reproduce the results and verify the claims made in the paper. This lack of transparency hinders the scientific community's ability to build upon this work and assess its true impact.

(3) The study utilizes too few datasets, which limits the generalizability of the findings. The experiments would be more convincing if they included datasets from the PeMS system, such as Large-ST [1], which are well-processed, cover longer time spans, and are widely used in the traffic forecasting community. This would provide a more robust evaluation of the proposed method.

### Questions
Refer to weaknesses

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper firstly investigates how urban time series models (UTSMs) can be utilized to deal with the low-frequence events in urban management. It proposes a pattern neuron-guided training (PN-Train) method consisting of a perturbation-based detector and a fine-tuning mechanism. The experiments on a series of time series forecasting tasks show the superiority of PN-Train, which enhances performance in low-frequency events while maintaining high performance in high-frequency events.

### Strengths
[1] A simple yet effective method is proposed to deal with the low-frequency patterns in urban time series data. It is of certain novelty to design a method from the neural aspect, making  

[2] Experiments on multiple datasets validate the existence of pattern neurons and the proposed PND stage successfully detects them. Overall, the empirical studies are solid. 

[3] The paper is well-written and easy to follow, with sufficient technical details on the pattern neuron detector, pattern neuron verifier, and pattern neuron optimizer.

### Weaknesses
[1] It is better to have a more complete discussion about low-frequency events, e.g., how these events are handled in previous works (Related Works section), how low-frequency events should be technically defined, and how the evaluation metrics are established to verify the effectiveness of the methods.

[2] Lack of comparison with baseline methods that deal with various unbalanced data distribution problems.

### Questions
Q1. Is there any way to quantitatively define or model the frequency of events? 

Q2. Is there any theoretical principle that can support the neuron-based strategy?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This work addresses the challenge of predicting low-frequency events (e.g., holidays, emergencies) in urban time series data, which are often overlooked by traditional models. The authors propose Pattern Neuron guided Training (PN-Train), a novel method that identifies and fine-tunes neurons specifically associated with low-frequency patterns. PN-Train incorporates a perturbation-based Pattern Neuron Detector (PND) to locate key neurons, and a Pattern Neuron Optimizer (PNO) to enhance their learning without compromising high-frequency event predictions.

### Strengths
S1: PN-Train introduces a novel approach by using a perturbation-based detector to identify neurons associated with low-frequency patterns and fine-tuning these neurons to improve prediction accuracy. This is an innovative perspective, combining neuron-level analysis with practical forecasting tasks.

S2: By capturing and fine-tuning neurons under different patterns, PN-Train enhances the fairness of predictions for low-frequency events, reduces model bias, and helps in forecasting scenarios with sparse data.

S3: The experiments provide solid evidence of the existence of Pattern Neurons, with case studies offering visualized results that make the concept highly intuitive and easy to understand.

### Weaknesses
W1: While the paper introduces neuron detection and optimization methods, it lacks in-depth theoretical explanation for why these neurons exhibit distinct behavior for low-frequency events. More analysis and discussion on the working mechanisms of pattern neurons, such as potential differences in weight distribution or activation between high- and low-frequency events, is needed, along with supporting theoretical calculations.

W2: The paper highlights patterns for holidays and emergencies in the dataset, but in real-world applications, low-frequency events can be more random and harder to predict. Further discussion on how PN-Train handles unpredictable low-frequency events, such as concert events, sport events, or extreme weather like typhoon,  and then testing its generalization ability in more complex scenarios would be beneficial.

W3: There are some typos, such as inconsistent citation formatting in reference 766, the use of "$B" in Figure 5b, and inconsistency between "B" in Figure 5 and "D" in line 486. Please clearfully check for typos throughout the paper.

### Questions
Please see W1-W3.

### Soundness
3

### Presentation
4

### Contribution
3
