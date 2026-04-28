# Time Series Anomaly Detection using Reconstruction and RBF Similarity Scores

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5

## Abstract
Anomaly detection in time series data is pivotal across various domains. The inherent challenge of scarce labeled data for anomaly detection has increased the attention toward unsupervised learning methods, in particular autoencoders and variations thereof. While these unsupervised approaches have shown promise, those that solely rely on reconstruction error often miss subtle anomalies, especially in high-dimensional or multivariate datasets. Motivated by this challenge, we introduce a novel approach that utilizes a layer of Radial Basis Function (RBF) neurons within the deep learning architectures. This RBF layer fits a nonparametric density in the hidden representation. When the neural network is trained on (predominantly) normal data, then a high RBF output indicates a high density, which in turn implies a high similarity with the normal data. Combining the RBF similarity score with the reconstruction error results in a unique anomaly score that we named the SimRec score. While our method can be adapted to a wide range of architectures, we focus on LSTM and Transformer models.  We evaluate our approach on three real-world benchmark datasets, with results indicating significant improvements over the baselines. Our findings underscore the potential of the SimRec score in capturing subtle anomalies that might be overlooked by scores based on reconstruction error alone, offering a more robust and comprehensive solution for anomaly detection in time series data.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces SimRec score, an anomaly score to improve detection of anomalies by combining the reconstruction score with a similarity score. The similarity score is computed via density estimations using a layer of RBF neurons in DNNs. Experimental results on various time-series anomalies demonstrate the performance of the proposed solution

### Strengths
- Significant value in improving anomaly detection methods by "small" modifications in current methodologies
- Experimental results support the claims of the paper
- Technical sound ideas

### Weaknesses
 - Novelty is somewhat low

The idea seems technical sound as sub-components already exist. The technical novelty is somewhat low. For example, there is lack of preliminaries to help understand if something is brand new, but several of these questions are simple adaptation of the original equations applied to this new problem (e.g., k-means-type optimization in eq 3, RBF kernel already exists, combination of two scores is trivial, etc.)

The core idea of using sim to centroids has been applied many times (see work below), maybe not explicitly combined with the reconstruction error.

- Unclear experimental settings

The settings and parameters for baselines are not clear. Questions can be raised about fairness in comparisons when details from settings are omitted

- Missing related work, datasets, new benchmarks

The work focuses on a very narrow part of the literature (emerging due to the rise of DNN solutions) but definitely omits new progress on benchmarks, baselines, new evaluation measures [a,b].

New benchmarks, ~20 datasets, ~2000 timeseries, 10+ baselines
[a] TSB-UAD: an end-to-end benchmark suite for univariate time-series anomaly detection."

New evaluation measures
[b] "Volume under the surface: a new accuracy evaluation measure for time-series anomaly detection."

### Questions
- Novelty is somewhat low

The idea seems technical sound as sub-components already exist. The technical novelty is somewhat low. For example, there is lack of preliminaries to help understand if something is brand new, but several of these questions are simple adaptation of the original equations applied to this new problem (e.g., k-means-type optimization in eq 3, RBF kernel already exists, combination of two scores is trivial, etc.)

The core idea of using sim to centroids has been applied many times (see work below), maybe not explicitly combined with the reconstruction error.

- Unclear experimental settings

The settings and parameters for baselines are not clear. Questions can be raised about fairness in comparisons when details from settings are omitted

- Missing related work, datasets, new benchmarks

The work focuses on a very narrow part of the literature (emerging due to the rise of DNN solutions) but definitely omits new progress on benchmarks, baselines, new evaluation measures [a,b].

New benchmarks, ~20 datasets, ~2000 timeseries, 10+ baselines
[a] TSB-UAD: an end-to-end benchmark suite for univariate time-series anomaly detection." Proceedings of the VLDB Endowment 15.8 (2022): 1697-1711.

New evaluation measures
[b] "Volume under the surface: a new accuracy evaluation measure for time-series anomaly detection." Proceedings of the VLDB Endowment 15.11 (2022): 2774-2787.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Until recently, anomaly detection was mainly done using unsupervised learning and autoencoder-based methods due to the lack of label data. Learning methods based on reconstruction error cannot detect subtle anomalies in multivariate dataset/high-dimensional dataset.

In this paper, to solve these limitations, Radial Basis Function (RBF) neurons are applied to deep learning architecture.

In other words, this paper proposes a new anomaly score called SimRec. SimRec is an anomaly score that combines RBF score and reconstruction error. By using this score, subtle existing anomalies can be detected.

### Strengths
1. In particular, in unsupervised anomaly detection, a motif to overcome the limitations of reconstruction error-based anomaly detection is reasonable.
2. The paper is overall understandable and neatly written.

### Weaknesses
1. There is a lack of baseline. Since neither LSTM nor Transformer are models specialized for anomaly detection, I am curious about the results when applied to more specialized models. In particular, I would like to see the results of applying SimRec to the Anomaly Transformer. In addition, Omni Anomaly
2. The effect of SimRec is clearly visible, but it seems to be more affected by threshold selection. I would like to see the reconstruction error graph of the anomaly transformer using the same threshold selection method.
3. This paper clearly has good motivation, but it feels somewhat lacking in terms of experimental performance, experimental content, and contribution.

### Questions
1. There is a lack of baseline. Since neither LSTM nor Transformer are models specialized for anomaly detection, I am curious about the results when applied to more specialized models. In particular, I would like to see the results of applying SimRec to the Anomaly Transformer. In addition, Omni Anomaly
2. The effect of SimRec is clearly visible, but it seems to be more affected by threshold selection. I would like to see the reconstruction error graph of the anomaly transformer using the same threshold selection method.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In order to mitigate the impact of smoothing effects and improve the network's sensitivity to anomalies, the author brings RBF to current time-series anomaly detection methods like LSTM and Transformer. By constructing a clustering-based middle layer with RBF, all the input samples are projected to cluster space for comparing their distances to cluster centroids, which is benefit for separating anomalies from samples. Besides, an RBF-similarity-score-based criterion is proposed for optimizing the parameters as well as evaluating the effect of proposed methods.

### Strengths
Strengths:
1)	The motivation of the work is quite direct and practical in anomaly detection fields, which is easy to catch up;
2)	Experiments with LSTM and Transformer on 3 different datasets demonstrate the effectiveness of proposed methods, and the performance improvement brought by the proposed module is stable;
3)	Ablation study on initialization methods, inserting position and number of cluster centroids firmly analyzed the effectiveness of proposed methods under different circumstances;

### Weaknesses
1) In review part, only Xu et al. (2021) is reviewed for describing current time-series anomaly detection methods, but several works in 2022 and 2023 are missed in reviewing and experimental parts, which have also performed greatly in multiple time-series anomaly detection datasets, such as:
[1] Zhang Z, Li W, Ding W, et al. STAD-GAN: unsupervised anomaly detection on multivariate time series with self-training generative adversarial networks[J]. ACM Transactions on Knowledge Discovery from Data, 2023, 17(5): 1-18.
[2] Xia F, Chen X, Yu S, et al. Coupled Attention Networks for Multivariate Time Series Anomaly Detection[J]. IEEE Transactions on Emerging Topics in Computing, 2023.
[3] Ding C, Sun S, Zhao J. MST-GAT: A multimodal spatial–temporal graph attention network for time series anomaly detection[J]. Information Fusion, 2023, 89: 527-536.
2) The experiments were only conducted on LSTM and Transformer, which are some out of-date baselines, more experiments on current SOTA methods (as baselines) should be conducted for validating the performance of proposed module, since the author mentioned that the proposed method is generic and can be applied to a wide range of deep learning architectures. For instance, the Anomaly Transformer can be regarded as a good baseline to testify the proposed RBF-based module.

### Questions
Refering to above

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
