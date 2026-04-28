# FreRA: A Frequency-Refined Augmentation for Contrastive Learning on Time Series Classification

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 5, 6, 5

## Abstract
Contrastive learning has emerged as a competent approach for unsupervised representation learning. However, the design of an optimal augmentation strategy, although crucial for contrastive learning, is less explored for time series classification tasks. Existing predefined time-domain augmentation methods are primarily adopted from vision and are not specific to time series data. Consequently, this cross-modality incompatibility may distort the global semantics of time series by introducing mismatched patterns into the data. To address this limitation, we present a novel perspective from the frequency domain and identify three advantages for downstream classification: 1) the frequency component naturally encodes global features, 2) the orthogonal nature of the Fourier basis allows easier isolation and independent modifications of critical and unimportant information, and 3) a compact set of frequency components can preserve semantic integrity. To fully utilize the three properties, we propose the lightweight yet effective Frequency-Refined Augmentation (FreRA) tailored for time series contrastive learning on classification tasks, which can be seamlessly integrated with contrastive learning frameworks in a plug-and-play manner. Specifically, FreRA automatically separates critical and unimportant frequency components. Accordingly, we propose Identity Modification and Self-adaptive Modification to protect global semantics in the critical frequency components and infuse variance to the unimportant ones respectively. 
Theoretically, we prove that FreRA generates semantic-preserving views. Empirically, we conduct extensive experiments on two benchmark datasets including UCR and UEA archives, as well as 5 large-scale datasets on diverse applications. FreRA consistently outperforms 10 leading baselines on time series classification, anomaly detection, and transfer learning tasks, demonstrating superior capabilities in contrastive representation learning and generalization in transfer learning scenarios across diverse datasets.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a method, FreRA, to enhance time series classification by contrastive learning and sample augmentations. First, they considered the frequency domain of the time series. FreRA automatically separates the critical and unimportant frequency components. They proposed Identity Modification and Self-adaptive Modification to protect the global semantics in the critical frequency components and inject variance into the unimportant components, respectively. Extensive experimental results on several datasets show that FreRA outperforms existing methods in terms of accuracy.

### Strengths
1. Overall, this paper is well-written and easy to follow.
2. The problem studied is significant, and exploring augmentation in time series is novel.
3. Extensive experimental results are promising.

### Weaknesses
1. The importance distinction of this method is mostly for the entire time series, and it could be better to compare it with other methods and analyze the theoretical computational complexity. The analysis should consider not just the asymptotic complexity but also the practical implications, such as the constant factors involved in the FFT and other operations, which can significantly impact real-world performance. Furthermore, a comparison with methods that perform augmentation in the time domain should be included to highlight the trade-offs between frequency and time domain approaches.
2. Although frequency methods can improve efficiency, it is unclear whether such methods mainly focus on the low-frequency part and ignore the high-frequency part which is more important for time series prediction. The paper should provide a more detailed analysis of how the method handles different frequency components and their relative importance for various time series datasets. It would be beneficial to show the distribution of the learned importance scores across different frequency bands and how these distributions correlate with the performance on different datasets.
3. Do the authors consider the dependencies between channels, which is very significant for multivariate time series. The method should be evaluated on datasets with varying degrees of channel dependencies to understand its limitations. A discussion on how the method could be extended to explicitly model these dependencies would be valuable.
4. The authors claim that FreRA can be benefited by any contrastive learning framework, but only show the results of InfoNCE. What about other CL paradigms, such as SimCLR, etc.?  It could be better to present more sufficient ablation. The ablation study should include a wider range of contrastive learning frameworks and loss functions, and also explore the impact of different hyper-parameters within each framework. The results should be presented in a way that allows for a clear comparison of the performance gains achieved by FreRA across different settings.
5. The experimental results are selected from the highest performances among 11 time-domain augmentations and 5 frequency-domain augmentations. Is this fair enough? There seems to be randomness with such selection strategy. The selection process should be more transparent and justified. The paper should provide a rationale for choosing these specific augmentations and discuss why the best-performing augmentations were selected for comparison. It would be more convincing to show the performance of FreRA against a wider range of augmentations, not just the best-performing ones.
6. The results of the impacts of hyper-parameters could be moved to the main paper for a better organization.

### Questions
See above.

### Soundness
3

### Presentation
3

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
This paper proposes Frequency-Refined Augmentation (FreRA), an augmentation method for time series contrastive learning on classification tasks. FreRA automatically separates critical and unimportant frequency components, and accordingly proposes Identity Modification and Self-adaptive Modification for different components. It conducts experiments on two benchmark datasets including UCR and UEA archives, as well as 5 large-scale datasets on diverse applications. FreRA outperforms 10 leading baselines on time series classification, anomaly detection, and transfer learning tasks.

### Strengths
Data augmentation is an important problem for time series and contrastive learning. This paper investigates this problem and proposes a method from the frequency perspective. The proposed method seems easy to follow and implement. The experiments in this paper are extensive, including many different datasets and tasks. The proposed method outperforms most of the baselines.

### Weaknesses
W1: Some important terms in this paper are not clearly defined, such as ‘semantic integrity’ and ‘critical and unimportant frequency components’. Why can we measure semantic integrity using mutual information? Is this consistent with humans’ understanding of semantics? How can we measure the importance of frequency components? What are these critical components critical for?

W2: The overall novelty of the proposed augmentation method is limited. Augmentation from the frequency components is not a new idea for time series. The main difference is a trainable vector s to control the augmentation of different components. It is unclear why s trained from Equation (7) can learn to select critical components automatically.

W3: It is unclear how FreRA achieves both semantic-preserving information and a considerable amount of variance. The authors need to clarify which designs correspond to these two sides respectively. 

W4: The self-adaptive modification seems simple and tricky. It only uses the vector s and threshold to select and scale unimportant frequency components. The motivation for scaling these components is unclear. 

W5: Compared with some SOTA baselines, such as SoftCLT and InfoTS, the advantage of FreRA is not clear, especially on UEA and UCR datasets. The ablation study is coarse, and some important variants are missing. For example, modifying all (or randomly selected) frequency components and modifying unimportant components randomly.

### Questions
Some other questions:

Q1: As this paper focuses on time series classification, why is it also evaluated in anomaly detection? 

Q2: Figure 2 is hard to read. The different colors for vector blocks in FreRA are confusing.

### Soundness
2

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
The paper introduces a novel augmentation technique designed for time-series contrastive learning by leveraging frequency-domain properties. It utilized the idea of FFT which separates time-series data into critical and non-critical frequency components.

### Strengths
The method utilizes the connection between frequency domain knowledge and semantic information to enhance the representation learning. The critical components capture global semantics essential for classification, while non-critical components are used for self-adaptive noise injection, which I found is an interesting link and the authors provide a comprehensive explanation for the motivation.
The authors provide extensive experiments and strong experiment results to demonstrate their method's effectiveness.

### Weaknesses
1. At the beginning of the paper, the authors make strong assumptions that existing predefined augmentation methods are primarily adopted from vision and are not specific to time series data. There are already several methods, especially frequency-based augmentation, e.g., TF-C, method design for time series contrastive learning. Specifically, the paper should acknowledge that while some time-domain augmentations are indeed borrowed from vision, there's a growing body of work focusing on time-series specific augmentations, including those operating in the frequency domain. The framing of existing methods as solely vision-inspired is an oversimplification.
2. Since the paper mainly provides the frequency-based augmentation, the motivation study, such as Figure.1 probably should highlight more about whether current frequency-based method can capture the semantics, rather than only focus on the time-domain. The current motivation study primarily focuses on the limitations of time-domain augmentations, which is not the core contribution of the paper. A more compelling motivation would directly compare the proposed method with existing frequency-based augmentations, demonstrating why the proposed approach is superior in preserving semantic information.

### Questions
/

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study introduces Frequency-Refined Augmentation (FreRA), a method designed to overcome limitations in current augmentation strategies for time series classification in contrastive learning. Unlike existing visual-based augmentations, FreRA leverages three key advantages of the frequency domain properties to better preserve the global semantics of time series data. FreRA automatically segregates these components, applying Identity Modification to preserve vital details and Self-adaptive Modification to add variance to less significant parts. Theoretical proofs and empirical evaluations confirm FreRA's superiority, showing it outperforms ten leading baselines across various time series tasks.

### Strengths
1. This paper is well-written and well-organized.
2. The methodology is clear and the problem is well-motivated.
3. This is a plug-and-play method that appears to integrate seamlessly with existing contrastive learning frameworks.

### Weaknesses
1. Compared to existing works, this work does not exhibit a notable advantage in classification performance.
2. I am somewhat confused about the experimental design for the transfer learning part: 1) Why was SHAR data selected instead of one of the datasets listed in Table 1 (e.g., UCIHAR) to evaluate the transfer capability of the algorithm? 2) Based on the experimental results in Table 2, the performance is lower than that reported in the reference work (Qian et al., 2022). What might be the reasons for this difference?
What did this experiment aim to prove?
3. In the ABLATION STUDIES part, the authors sequentially removed each of the three innovative method components for comparison. From the experimental results, the gains provided by the three modules seem roughly equivalent. If all three modules were removed, what would be the resulting performance? Looking at Table 1 in the paper, the performance of softCLT and FreRA appear quite similar. If FreRA were integrated into softCLT, would there be any gain in performance?

### Questions
See weaknesses.

### Soundness
3

### Presentation
3

### Contribution
3
