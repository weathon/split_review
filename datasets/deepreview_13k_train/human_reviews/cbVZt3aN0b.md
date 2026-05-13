# Modeling Annotation Delay In Continual Learning

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
Online continual learning, the process of training models on streaming data, has gained increasing attention in machine learning. However, a critical aspect often overlooked is the label delay, where new data arrives before its corresponding labels due to slow and costly annotation processes. We introduce a novel continual learning setup that explicitly accounts for label delay, with models trained over time steps with labels shifted from the data streams by some factor. In each step, the model is exposed to both unlabeled data from the current time $t$ step and labels from time step $t-d$. We show that this is a challenging problem and increasing the per step computational budget can not help resolve the problem. Moreover, we show that Self-Supervised learning and Test-Time Adaptation approaches perform even poorly compared to a naive approach that ignores the unlabaled data training on the older but annotated stream. We introduce a simple, efficient baseline using importance sampling to align the unlabeled and labeled data distributions, bridging the accuracy gap caused by label delay without significantly increasing computational complexity, by rehearsing from memory labeled samples that are most similar to the new unlabeled samples. While on CLOC our method performs similarly to SSL and TTA, on CGLM, our method not only closes the accuracy gap, but outperforms the non-delayed counterpart by $+25\%$ up to $+33\%$, while being computationally friendly. 
We conduct various ablations and sensitivity experiments demonstrating the effectiveness of our approach.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the problem of online learning, where the goal is to maintain a machine learning model in a data stream. They study this problem with the additional challenge of label delay, which occurs when the label of a data point is delayed and hence it cannot be immediately used for training.

They run different experiments using existing techniques such as SSL (Semi-Supervised Learning) and TTA  (Test-Time adaptation) to leverage the unlabeled data, however, in their analysis, they find out that these methods do not outperform the naive approach to discard the unlabeled data until one receive the labels. To address this problem, they propose a new method called Weighted Memory Sampling that leverages the unlabeled data as follows: the unlabeled data is used to find labeled data points that are similar (feature representation) so that we can use the latter data for training. This heuristic allows the authors to address distribution drift since it can possibly adapt to the change in distributions by using similar points from the past.

They run different experiments to verify the effectiveness of their approach and show that it indeed performs better than the previously tried baselines.

### Strengths
The paper addresses an extremely important problem, and label delay is a relevant challenge in most of practical applications with data streams. 

The strength of the paper lies in the empirical evaluation, as they convincingly try different baselines and their method using a real dataset. They try different combinations of hyper-parameters (delay, computational budget) and thoroughly discuss the obtained results.

I believe that the method introduced by the authors (Weighted Memory Sampling) leverages in a very clever way the information of the unlabeled data.

I have a couple of suggestions:
- the paper [Yao, Huaxiu, et al. "Wild-time: A benchmark of in-the-wild distribution shift over time." NeurIPS (2022)] provides other additional benchmarks that could be used.
- It would be interesting to relate your measure of similarities with other quantities that were computed in domain adaptation (e.g., discrepancy) that also try to leverage unlabeled data, albeit in a different setting (as[ Mansour, Yishay, Mehryar Mohri, and Afshin Rostamizadeh. "Domain Adaptation: Learning Bounds and Algorithms.]"). In particular, I think your method can only work correctly if there is a shift in the covariate distribution, but it cannot detect a shift in the label distribution (but this is probably impossible because of the label delay).

### Weaknesses
I think that the critical weakness of the paper is that it does not provide a convincing comparison of its contribution with respect to existing work. There is no discussion of existing work on label delay.

However, the problem of label delay has definitely already been studied in the literature. I think that the statement that no prior work addressed this problem is too strong, and a (big) section of related work should be dedicated to those existing works. 

Just a few papers, but there are many more on this topic:
[A]: Mesterharm, Chris. "On-line learning with delayed label feedback." International Conference on Algorithmic Learning Theory. Berlin, Heidelberg: Springer Berlin Heidelberg, 2005.
[B]: Gomes, Heitor Murilo, et al. "A survey on semi-supervised learning for delayed partially labelled data streams." ACM Computing Surveys 55.4 (2022): 1-42.
[C]: Gao, Haoran, and Zhijun Ding. "A Novel Machine Learning Method for Delayed Labels." 2022 IEEE International Conference on Networking, Sensing and Control (ICNSC). IEEE, 2022.
[D]: Plasse, Joshua, and Niall Adams. "Handling delayed labels in temporally evolving data streams." 2016 IEEE International Conference on Big Data (Big Data). IEEE, 2016.
[E]: Hu, Hanqing, and Mehmed Kantardzic. "Sliding Reservoir Approach for Delayed Labeling in Streaming Data Classification." (2017).
[F]: Souza, Vinicius MA, et al. "Classification of evolving data streams with infinitely delayed labels." 2015 IEEE 14th International Conference on Machine Learning and Applications (ICMLA). IEEE, 2015.

### Questions
- How does your paper stand with respect to existing work on label delay? (See Weakness)?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduce a novel continue learning setup which includes delay labeling for data sampled from time-varying distribution. To investigate this learning scenario, It conducts experiments comparing a naive algorithm which disregards unlabeled data with self-supervised learning and Test-Time Adaption methods,  all of which prove to be inadequate for solving this challenge. Finally, the paper proposes an Importance Weighted Memory Sampling approach to match the distribution of labeled samples to the newest unlabeled samples.

### Strengths
The introduced continuous learning problem, incorporating label delay, reflects a real-world issue of significance. Distribution shifts and labeling delays are common challenges encountered in product cycles.

The paper is effectively motivated by highlighting the inherent difficulty of the setup and demonstrating the inadequacy of popular techniques such as Self-Supervised Learning and Test-Time Adaptation in addressing this challenge.

The proposed method, while straightforward, exhibits strong performance when compared to baseline approaches.

### Weaknesses
It's surprising the proposed Importance Weighted Memory Sampling (IWMS) method performs even better than the naive algorithm with no delay. IWMS aims to match the distribution of the selected samples to the newest data distribution, how could model trained on it outperform a model trained on the newest data with labels? More discussion is needed regarding its exceptional outperformance. 

The paper should also include semi-supervised learning as a baseline for comparison.

Can you explain why the proposed IWMS performance is so different between CLOC and CGLM? Especially, why CGLM can outperform Naive algorithm with no delay?

Some typo:
In page 4, problem setting step 5, unlabeled dataset should not include $y_i^\mathcal{T}$
In page 8, memory buffer is introduced without detailed description. What samples included in the buffer, what's the frequency to update the buffer.

### Questions
Can you explain why the proposed IWMS performance is so different between CLOC and CGLM? Especially, why CGLM can outperform Naive algorithm with no delay?

Some typo:
In page 4, problem setting step 5, unlabeled dataset should not include $y_i^\mathcal{T}$
In page 8, memory buffer is introduced without detailed description. What samples included in the buffer, what's the frequency to update the buffer.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the problem of continuous learning with label delay, where the ground truth label of certain data in the stream is available only after certain timestamps. The authors validate the negative effect of label delay on several recent continuous image classification datasets and provide an importance sampling based method to resist the label delay.

### Strengths
This work considers an important problem in continuous learning, and the empirical results on the recent large-scale image dataset provide good insights for this line of research.

### Weaknesses
1. There exist overclaim on the contribution of this paper. The problem setting of continuous learning or online learning with label delay is observed and studied over a decades ago and there are many both theoretical and empirical studies on this problem, please see [1,2,3,4] and reference in these papers. There is lack of discussion and comparison with this line of research.


[1] Weinberger, Marcelo J. and Ordentlich, Erik. On delayed prediction of individual sequences. IEEE Transactions on Information Theory, 2002.

[2] Kuncheva LI, Sánchez JS. Nearest neighbour classifiers for streaming data with delayed labelling. In: ICDM, 2008.

[3] Quanrud, Kent, and Daniel Khashabi. Online learning with adversarial delays. In: NIPS, 2015.

[4] Flaspohler G E, Orabona F, Cohen J, et al. Online learning with optimism and delay. In: ICML, 2021.


2. Results in section 4 provides a good validation on the recent images dataset in continuous learning that the multiple gradient descents in historical data may not benefit generliazation on newly arrived unlabled data due to distribution change. However, in my opinion, it is overclaiming to be a contribution as it is a known result. If there are not enough data at each time stamp (typically in continuous learning setting) and lack of well-designed regulazation term, the performance will even degrade with increasing number of gradient descent because the model overfits to such limited number of previous data with different distribution.

3. Experimental comparisons are unfair. Self-supervised learning and test-time adaptation methods are designed for the learning scenario where the learner does not have access to historical labeled data, or in some test-time training algorithms, the learner can only modify the training process in the training time. Comparing these algorithms with importance sampling on historical data is unfair, since in the latter case we can obtain and use the ground truth label of the historical data. It is more reasonable to consider rehearsal-based continuous learning algorithms as a comparison.

### Questions
What is the performance of the proposed importance sampling method compared to rehearsal based continuous learning algorithms in the setting of continuous learning with label delay?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies and proposes techniques for online (continual) learning with label delay. First the paper shows that several simple techniques adapted to the considered setting provide poor performance and then, they propose a method based on sampling previous data that achieves better results.

### Strengths
The research topic is very relevant since the distribution of data often changes over time in practical scenarios. The paper also offers an experimental evaluation of several alternatives that can be of interest

### Weaknesses
The paper contribution over the state-of-the-art is unclear. Firstly, the setting the authors refer as "continual learning" is basically that of "online learning" with time-varying distributions. In particular, the model obtained at time t is never used to predict data from previous times, and hence is not affected by the specific problems of "continual learning" such as catastrophic forgetting. There is a significant body of work for online learning methods with delayed labels with which the methods in the paper should be compared with.

The paper first describe how different ideas do not work and then proposes a simple technique that works better. The first part of the paper is of limited interest. It would be more useful if the authors compare the technique they propose with other methods for online learning with delayed labels.



### Questions
Why you describe your methods as "continual learning"? It seems that the performance over past data is not evaluated so there cannot be any forgetting

Typos such as “ data. and deployed” should be avoided

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
