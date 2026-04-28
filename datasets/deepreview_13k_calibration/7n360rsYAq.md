# Towards Dynamic Trend Filtering through Trend Points Detection with Reinforcement Learning

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 8, 5, 5

## Abstract
Trend filtering simplifies complex time series data by applying smoothness to filter out noise while emphasizing proximity to the original data. However, existing trend filtering methods fail to reflect abrupt changes in the trend due to `approximateness,' resulting in constant smoothness. This approximateness uniformly filters out the tail distribution of time series data, characterized by extreme values, including both abrupt changes and noise. In this paper, we propose Trend Point Detection formulated as a Markov Decision Process (MDP), a novel approach to identifying essential points that should be reflected in the trend, departing from approximations. We term these essential points as Dynamic Trend Points (DTPs) and extract trends by interpolating them. To identify DTPs, we utilize Reinforcement Learning (RL) within a discrete action space and a forecasting sum-of-squares loss function as a reward, referred to as the Dynamic Trend Filtering network (DTF-net). DTF-net integrates flexible noise filtering, preserving critical original subsequences while removing noise as required for other subsequences. We demonstrate that DTF-net excels at capturing abrupt changes compared to other trend filtering algorithms and enhances forecasting performance, as abrupt changes are predicted rather than smoothed out.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The inherent smoothness of trend filtering filters out the tail distribution of time series data, characterized as extreme values, thereby failing to reflect abrupt changes in the trend.  In this work, they formalize the Trend Point Detection problem as a Markov Decision Process (MDP) to Dynamic Trend Points (DTPs). And they solve the Trend Point Detection problem using Reinforcement Learning (RL) algorithms operating within a discrete action space, referred to as the Dynamic Trend Filtering network (DTF-net). And they finally demonstrate that DTF-net excels at capturing abrupt changes compared to traditional trend filtering and also enhances performance in forecasting tasks.

### Strengths
This paper analyses the problem that the smoothing of Traditional trend filtering may also filter out abrupt changes that should be manifested in the trend, thus capturing abrupt changes through the proposed DTF-net. I think the origin of the problem is very clear and It contributes to the field. 
The authors define the essential points in the trend as Dynamic Trend Points (DTPs), and the process of capturing them is referred to as Trend Point Detection. And formalize the Trend Point Detection problem as a Markov Decision Process (MDP), so as to address the issue using reinforcement learning methods.  So I think the formal transformation of the problem is innovative and the solution and ideas used are appropriate.

### Weaknesses
I believe that the problem analysis and theoretical exposition in this paper are sufficient, but there is still room for enrichment in the methods sections.  For example, you can formalize the reinforcement learning process with diagrams to enrich the details.

### Questions
I noticed that the baselines of several recent sotas compared in your experiment are all geared towards trend filtering, and I'm wondering if their methods take abrupt changes detection into account, and if there are other methods such as anomaly detection that can be used instead of, or to help, produce similar results.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies time series trend filtering problem and aims to filter noise but leave important abrupt changes unchanged. The authors proposed a deep model to detect extreme values that fall into the tail part of the data distribution. Specifically, the authors try to identify essential points termed dynamic trend points (DTPs) and reflect DTPs in the trend. The identifying problem is formulated as Markov decision process (MDP) and reinforcement learning is used to address it. MSE loss is used as reward of the agent's actions. Experiments on both synthetic and real-world datasets demonstrated that the proposed algorithm can enhance time series forecasting task performance. The authors analyzed many aspects of the proposed model including both pros and limitations.

### Strengths
S1. The detection problem is innovatively transformed into a Markov decision process and addressed by reinforcement learning: the deep model takes time series sub-sequence as input, conducts a series of actions, and then makes forecasting (concentrating on future but not current readings). The mean squared error (MLS) is utilized as loss/reward. 

S2. A random sampling scheme is proposed to enable the DTF-net reading time series from both forward and backward directions, it can also alleviate over-fitting issue from my perspective. 

S3. Effectiveness is proved on a synthetic dataset and a real-world dataset. The proposed model also enhances time series forecasting task performance.

### Weaknesses
W1. Training a deep net might be data- and computational-expensive and may face over-fitting problem. Tuning hyper-parameters is also challenging depending on the data and real-world applications. Specifically, the reliance on a deep neural network, even a simple MLP, introduces a significant overhead in terms of data requirements and computational resources. The risk of overfitting is also considerable, especially given the complexity of time series data and the potential for the model to memorize noise rather than learn underlying trends. The hyper-parameter tuning process for such models is often non-trivial, requiring careful selection of learning rates, network architectures, and regularization techniques, which can be particularly challenging in the absence of a large, diverse dataset. 

W2. The heuristic random sampling algorithm can be optimized by considering the environment/context of the time series trend. The current random sampling method does not explicitly incorporate the temporal dependencies and contextual information inherent in time series data. This lack of contextual awareness could lead to suboptimal training samples, potentially hindering the model's ability to accurately identify dynamic trend points (DTPs). For instance, sampling without regard to the local trend patterns might lead to the model misinterpreting noise as significant changes or vice-versa. 

W3. The overall framework might be built without reinforcement learning, which I suggest the authors explore further. The use of reinforcement learning (RL) adds complexity to the model, and it's not immediately clear that the benefits of using RL outweigh the added overhead. There might be simpler, more efficient approaches to identifying DTPs that do not involve the complexities of RL. For instance, a deterministic algorithm or a carefully designed loss function could potentially achieve similar or better performance without the need for an RL agent and its associated training challenges.

### Questions
You can respond to the weaknesses if you have new insights. Though they are not questions.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors introduce a trend filtering approach, called DTF-net, to capture abrupt changes in time series through reinforcement learning methods. Instead of filtering them out as what many traditional trend filtering approaches do, the approach call such abrupt changes as Dynamic Trend Points (DTP), and formulate DTP detection problem as a Markov Decision Process. Subsequently, the reinforcement learning conducts MSE loss as reward function, so as to capture the temporal dependency simultaneously. The results demonstrate its ability to capture abrupt changes.

### Strengths
- The authors propose to formulate DTP detection problem as a Markov Decision Process, and utilize reinforcement learning to tackle it, which is seldom explored in trend filtering problem.
- Their opinion of detecting the abrupt changes instead of filtering them out is feasible, and their experiment of including the trend as an additional input feature for Time Series Forecasting also improves model's performance across several datasets.

### Weaknesses
1. Section 3.1.2

In Section 3.1.2, the authors fail to provide a satisfactory explanation or analysis for the superiority of random sampling over traditional sequential sampling. They briefly mention the challenge of dynamic-length sampling and their use of state encoding to maintain a constant state length. It's worth considering whether dynamic-length sampling is necessary or if equal-length sampling would suffice. Furthermore, clarity is needed on how they determine different lengths for various sampling samples. Additionally, the claim that the proposed Positional Encoding is "specifically designed for time series data" appears overstated, as it resembles the positional encoding used in the vanilla Transformer and its variants seen in other TSF Transformers like Informer or Autoformer.

2. Section 3.2

The choice of MSE loss as the reward function raises questions. It's unclear why an MSE-based reward ensures effective learning of abrupt changes rather than favoring smoother results, which could lead to lower overall MSE. Providing a more detailed rationale for this choice would be beneficial. Additionally, while the authors introduce reward sampling as a solution to overfitting, its operation and how it addresses overfitting remain unclear.

3. Experiment

An important consideration is whether this method is suitable for multivariate time series forecasting tasks, enabling the detection of abrupt change points across multiple channels simultaneously.

### Questions
+ The authors could give a more detailed explanation or analysis of why random sampling is better, and if dynamic-length sampling works better than traditional sequential and equal-length sampling.
+ The authors could explain how reward sampling works more detailed, and why MSE loss as reward function can help the model effectively learn the information of abrupt changes.
+ The authors could conduct more experiments on multi-variate time series if possible or state the challenges for that.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes an RL-based method to identify dynamic trend points in time series data. For a long time, the important dynamic trend points are mixed with noisy points and are hard to detect. This paper wants to use RL to identify them through a designed reward function. The experiments on synthetic data show some promising results.

### Strengths
The problem of this paper is interesting and important. DTPs are valuable to be identified from noise in a time series. It is a challenging problem. The authors motivate this problem well. The idea of using RL to resolve this problem is promising, even though much details are missing.

### Weaknesses
The main challenge for this work is to distinguish the noise points with trend points. However, there is no discussions on why RL can resolve this challenge. The authors only claim that ‘DNNs employed by RL agent is capable of capturing intricate patterns within time series data and identifying DTPs based on their non-linearity inherent.’ How do DNNs in RL can identify DTPs? Why do you think DNNs in RL can do that? What is the motivation behind that? There are no reasonable discussions on that. However, that is the main contribution of this work. 

The experimental evaluations are weak. Why do the authors highlight DTF-net in Table 1 rather than the best performance? The authors claim that “Note that wavelets have an overfitting issue, resulting in insufficient noise filtering.” Have you evaluated the noise filtering? How can you show that? There are a lot of real-world time-series data. Why did the authors not evaluate the methods on them? Only one example is given in Figure 4 without the performance of other methods.

### Questions
Please see the Weaknesses.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
