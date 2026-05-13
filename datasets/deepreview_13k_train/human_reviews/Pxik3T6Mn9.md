# Uncertainty-aware Human Mobility Modeling and Anomaly Detection

- Decision: Reject
- Scores: 6, 3, 3, 6

## Abstract
Given the GPS coordinates of a large collection of human agents over time, how can we model their mobility behavior toward effective anomaly detection (e.g. for bad-actor or malicious behavior detection) without any labeled data?
Human mobility and trajectory modeling have been studied extensively with varying capacity to handle complex input, and performance-efficiency trade-offs. With the arrival of more expressive models in machine learning, we attempt to model GPS data as a sequence of stay-point events, each with a set of characterizing spatiotemporal features, and leverage modern sequence models such as Transformers for un/self-supervised training and inference. Notably, driven by the inherent stochasticity of certain individuals' behavior, we equip our model with aleatoric/data uncertainty estimation. In addition, to handle data sparsity of a large variety of behaviors, we incorporate epistemic/model uncertainty into our model.
Together, aleatoric and epistemic uncertainty enable a robust loss and training dynamics, as well as uncertainty-aware decision making in anomaly scoring.
Experiments on large expert-simulated datasets with tens of thousands of agents demonstrate the effectiveness of our model against both forecasting and anomaly detection baselines. All code is available at  \url{https://anonymous.4open.science/r/mobility-ad}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper proposes UIFORMER, a dual-Transformer architecture for modeling human mobility patterns and detecting anomalies. It combines aleatoric and epistemic uncertainty estimation to better capture uncertainties inherent in human mobility data. The model aims to enhance robustness in anomaly detection by incorporating uncertainty into decision-making.

### Strengths
1. Originality: The model’s design, utilizing a dual-Transformer architecture for feature- and event-level attention, effectively captures dependencies at different levels of human behavior.
2. Quality: The paper includes comparisons with various baselines, showing that UIFORMER achieves superior performance for anomaly detection.
3. Clarity: The paper is well-organized and clearly explains the model’s architecture, training dynamics, and uncertainty estimation.  Figures and tables enhance the understanding of the model’s performance and design.
4. Significance: The method’s ability to better capture uncertainties in human behavior could have significant implications for applications like security, surveillance, and health monitoring, where accurate anomaly detection is critical.

### Weaknesses
1. Lack of Novelty in Uncertainty Quantification: The techniques for quantifying aleatoric and epistemic uncertainty, including Monte Carlo (MC) Dropout, have been widely used in other domains. The absence of a discussion on related works, specifically evidential deep learning methods, limits the novelty of the approach. Incorporating such references and discussions could strengthen the contribution of this paper.
2. There is insufficient detail about the SimLA dataset, particularly whether it is open-source or publicly available. Clarifying this point would improve transparency and reproducibility.
3. The decision to mask only one event per sequence in validation and testing phases is restrictive and may not reflect the full potential of the model in real-world scenarios where multiple events may be missing.
4. The use of MC Dropout for epistemic uncertainty estimation limits the exploration of alternative methods. Testing more methods, such as deep ensembles or evidential neural networks, could provide a more comprehensive understanding of uncertainty estimation in this context.

### Questions
1. Could the authors elaborate on why only one event is masked per sequence during validation and testing? Would masking more events per sequence affect the performance or the uncertainty estimates?
2. Is the SimLA dataset open-sourced, and are there plans to release it publicly? This would be useful for reproducibility and benchmarking future models.
3. Why was Monte Carlo Dropout chosen for epistemic uncertainty estimation, and are there plans to experiment with other methods like deep ensembles or evidential neural networks?
4. Are there specific applications or downstream tasks, such as traffic signal adjustments or navigation, where the proposed model could be directly applied to demonstrate practical benefits?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes an approach for anomaly detection of human mobility behaviour based on GPS data. The proposed approach is based on a Transformer architecture to model sequences of events/activities and it explicitly attempts to model epistemic and aleatoric uncertainty, which are then leveraged to devise a scoring function for rating abnormal behaviours. Using two simulated human activity datasets, the authors show that the proposed approach outperforms simpler baselines in modelling human mobility sequences and in detecting anomalous behaviors, especially showcasing and highlighting the contribution of modelling epistemic and aleatoric uncertainty to the results.

### Strengths
1) The problem of modeling human mobility data is an important one, with **important real-world implications**. 
2) The overall approach proposed for this particular problem is **a unique and new combination of existing ideas from literature**. It is of significance for the urban mobility domain. Especially the focus on modeling uncertainty when modeling human mobility data is something that can be very relevant for practical applications but is typically ignored in the urban mobility literature.  
3) The paper is **very well written**. The approach is mostly presented in a **clear** way (with some expectations, as mentioned below) and, in most cases, with a sufficient level of detail. 
4) The **empirical results show significant improvements** over the simpler baselines considered.

### Weaknesses
1) Although the specific combination of existing ideas in the proposed approach is new from the application point of view, from a methodological point of view, the **low novelty** is a concern, especially **for the broader ICLR audience**. Since the contribution is of significance mostly for a transportation audience, I would encourage the authors to consider targeting a transportation journal instead since I believe this work would have more visibility and more impact there. Otherwise, for ICLR, the authors should motivate better the broader applicability of their work and their insights beyond the concrete application considered. For example, could the uncertainty-aware approach be applied to other sequence modeling tasks in different domains? Could you give some examples? 
2) The **motivation for the application considered should be improved**. Why would one want to detect abnormal mobility behaviours? The authors briefly mention that they can "indicate security threats or spread of infectious disease", but these use cases need to be better explained and backed up by related works where having such predictions of abnormal mobility behaviours would be relevant. This is the critical basis for the proposed work, so it needs to be articulated in a more convincing way. 
3) The **baselines considered in the paper are very naive**. However, modelling sequences of human activities is a very well-studied problem in the transportation field, and the literature is vast on different deep learning approaches, including approaches based on transformers. I encourage the authors to consider including stronger baselines from the state-of-the-art for modelling human activity sequences - i.e., at least for the predictive part (RQ1); although the extension of some of these for score-based anomaly detection is also trivial, and therefore can also be potentially considered as additional baselines for RQ2. 
4) The **soundness of the experimental setup is a concern**, given that the datasets used for validating the proposed approach are themselves simulated based on deep learning models that were trained on real-world data to generate synthetic sequences. The authors are essentially fitting a deep learning model to the output of another deep learning model. This raises at least three important questions: i) is the output of the deep generative model good enough to generate realistic synthetic sequences that capture well the data distribution, including the "long-tails" such that abnormal behaviors are captured? and ii) why not simply use the deep generative model that was used to generate the data to detect abnormal behaviors? What are the advantages of using the proposed transformer architecture instead? iii) why haven't the authors considered using real data to demonstrate their approach (of course, despite a quantitative evaluation being difficult/impossible)? I would suggest the authors discuss these concerns and discuss their rationale for using simulated data and the potential limitations or advantages of this approach in the paper, as well as discuss the challenges and potential approaches for evaluating real-world data.  
5) There are several aspects of the proposed approach that are either **not properly motivated or unclear**. For example, eq. 7 is presented as "the average predicted logits"; however, looking at eq. 7, it seems to be the average of the exponentiated logits (i.e., likelihoods), and then the authors take the logarithm. This should be clarified and properly motivated. Also, the authors have multiple passes T for the categorical loss in eq. 7, but not for the numerical features loss in Section 3.3.2. What is the reasoning behind this distinction in approaches? Similarly, what is the reasoning for the +1 in eq. 10? I would suggest the authors provide a more detailed explanation or derivation for equation 7, and explicitly state their reasoning for the different approaches used for categorical and numerical features, as well as the addition of 1 in equation 10. 
6) Lastly, there are **several inconsistencies** in the paper. For example, it is written that "MAPE for SD from 51.95% to 21.93%", however these numbers don't match the values in Table 1. Similarly, it is mentioned that "UIFORMER delivers the best performance across both datasets and for all features compared with the baselines.". However, the MAPE of UIFORMER for ST is significantly worse than a simple transformer. These aspects should be clarified in the paper. It is also written that "AU remains almost constant as training data size increases"; however, looking at the table there are several significant exceptions that should be considered and discussed. I suggest that the authors carefully review their results and claims for accuracy, and provide a more nuanced discussion of their findings, particularly where the results don't align perfectly with their general claims.

### Questions
Kindly see my question in the weaknesses section, especially the questions that I raised in bullets 2, 4 and 5 above.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents a new method for human mobility modelling and anomaly detection via uncertainty estimation. The proposed method consists of a dual transformer encoder and an uncertainty-aware decoder.

### Strengths
1.	The motivation of the paper is clearly presented, and the writing is easy to follow. 
2.	The proposed method estimates both epistemic uncertainty and aleatoric uncertainty. 
3.	Both feature-level and event-level information are taken into account. 
4.	An uncertainty-based score is proposed for anomaly detection.

### Weaknesses
1.	My main concern with the paper is the lack of novelty. The proposed method is merely the combination of existing techniques. The authors should explore more advanced techniques in the field. For example, the epistemic uncertainty is estimated by MC dropout which is a weight-space method. It can also be studied from a function-space perspective, using methods such as Gaussian processes, Hamiltonian Monte Carlo, Stein variational gradient descent, etc. As for aleatoric uncertainty, methods such as quantile regression and conformal inference are worth exploring as well.

2.	Another major issue of the paper is that the evaluation is not convincing. the baselines used for comparison in the experiments do not reflect the current state-of-the-art methods for human mobility modelling or uncertainty estimation. 

Please refer to the relevant works listed below.
1) Abdar, Moloud, Farhad Pourpanah, Sadiq Hussain, Dana Rezazadegan, Li Liu, Mohammad Ghavamzadeh, Paul Fieguth et al. "A review of uncertainty quantification in deep learning: Techniques, applications and challenges." Information fusion 76 (2021): 243-297.
2)Sun, Shengyang, Guodong Zhang, Jiaxin Shi, and Roger Grosse. "FUNCTIONAL VARIATIONAL BAYESIAN NEURAL NETWORKS." In International Conference on Learning Representations, 2019.
3) Maddox, Wesley J., Pavel Izmailov, Timur Garipov, Dmitry P. Vetrov, and Andrew Gordon Wilson. "A simple baseline for bayesian uncertainty in deep learning." Advances in neural information processing systems 32 (2019).
4) Angelopoulos, Anastasios N., and Stephen Bates. "Conformal prediction: A gentle introduction." Foundations and Trends® in Machine Learning 16, no. 4 (2023): 494-591.

3.	The two datasets used for evaluation are synthetic. The proposed method should also be tested on real-world datasets.

### Questions
1.	What are the detailed experimental settings of the baseline methods used for comparison?
2.	Why not use real-world datasets for evaluation? 
3.	Can the proposed also use other anomaly scores apart from the one proposed in the paper, e.g., reconstruction error?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper proposes a model for detecting anomalies in human mobility using GPS data without labeled training data. It represents GPS data as sequences of stay-point events and utilizes Transformers for un/self-supervised learning. The model incorporates aleatoric and epistemic uncertainties to handle behavioral randomness and data sparsity, enabling robust training and decision-making. Experiments demonstrate its effectiveness over traditional forecasting and anomaly detection methods.

### Strengths
**S1.** The paper introduces a novel and practical approach to model both aleatoric and epistemic uncertainties in trajectories, allowing the model to handle the inherent randomness of human behavior and data sparsity effectively.

**S2.** Overall, the paper is technically sound and provides valuable contributions on how to deal with aleatoric and epistemic uncertainties with numerical features and categorical features together. 

**S3.** The comprehensive experiments show the effectiveness of uncertainty modeling and ad performance.

### Weaknesses
 **W1.** It would be better to provide more case studies to intuitively show the learned AU and EU.

**W2.** It would be better to include an addition experiment to show how $\lambda$ is selected in the loss function.

**W3.** It would be more interesting to explain why the authors chose their current set of baselines. More baselines are required. For example, it would be interesting to compare the proposed method with the existing time series outlier detection methods [1]. It would help the community to see whether existing methods like the Anomaly Transformer will work for human mobility anomaly detection.

_[1]. Anomaly Transformer: Time Series Anomaly Detection with Association Discrepancy, ICLR 2022._

**W4.** It would be better to include a section to introduce anomaly detection in sequential data (e.g., trajectory and time series) with more additional references as follows,

_[2]. Mobile Trajectory Anomaly Detection: Taxonomy, Methodology, Challenges, and Directions, IoTJ 2024._

_[3]. Time-series anomaly detection service at Microsoft, SIGKDD 2019._

_[4]. Anomaly detection in time series: a comprehensive evaluation, PVLDB 2022._

_[5]. Unraveling the 'Anomaly'in time series anomaly detection: a self-supervised tri-domain solution, ICDE 2024._

_[6]. Revisiting VAE for Unsupervised Time Series Anomaly Detection: A Frequency Perspective, WWW 2024._

_[7]. PeFAD: A Parameter-Efficient Federated Framework for Time Series Anomaly Detection, SIGKDD 2024._

_[8]. Deep variational graph convolutional recurrent network for multivariate time series anomaly detection, ICML 2022._

In addition, it is suggested to discuss the key differences between general time series/trajectory anomaly detection and the studied human mobility anomaly detection.

**W5.** As efficiency is important in anomaly detection, especially for downstream real-world applications, it is encouraged to compare the theoretical space and time complexities of the proposed method and baselines. Additionally, it would be better to include an experiment to show the training time and inference time comparison.

### Questions
1. How $\lambda$ is selected in the loss function?

2. There are various time series and trajectory anomaly detection methods. It would be interesting to investigate if these methods can be used to address human mobility anomaly detection.

3. It would be better to provide a running example to show how the uncertainties can be captured by the proposed uncertainty-aware decoder.

In addition, please see the weaknesses for other questions.

### Soundness
3

### Presentation
4

### Contribution
3
