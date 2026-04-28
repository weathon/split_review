# FSL-MIC: An Attentional Few-Shot Learning Framework for EEG Motor Imagery Classification

- Decision: Reject
- Avg Score: 2.20
- Scores: 1, 3, 1, 3, 3

## Abstract
Electroencephalography (EEG) is a key non-invasive technique used to investigate brain activity, particularly in motor imagery (MI) research. Traditional methods for classifying EEG signals often rely on handcrafted features and heuristic parameters, which can limit generalization across tasks and subjects. Recent advances in deep learning, particularly few-shot learning (FSL), offer promising alternatives to improve classification accuracy in scenarios with limited training data. This study explores the effectiveness of FSL algorithms, including Relation Networks, to enhance MI classification. It also examines how transfer learning and data augmentation techniques contribute to improving classification performance.

We propose a novel framework with three core modules—feature embedding, attention, and relation—that facilitates the classification of unseen subject categories using only a few labeled samples. The attention mechanism identifies key features related to the query data, while the relation module predicts query labels by modeling relationships between support and query data across subjects. Our experimental results demonstrate the effectiveness of our approach on two benchmark datasets, BCI 2a and BCI 2b, as well as our experimental dataset. The proposed FSL framework significantly outperforms traditional methods, offering promising applications in real-time Brain-Computer Interface (BCI) systems across various EEG setups. This research advances the understanding of machine learning in EEG applications and highlights the potential of FSL techniques in overcoming the challenges of limited training data in MI classification.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper introduces a Few-Shot Learning (FSL) framework that incorporates feature embedding, attention, and relation modules for the classification of unseen subject categories using a limited number of labeled samples. The attention mechanism highlights important features relevant to the query data, while the relation module predicts the labels for the query by analyzing the relationships between support and query data across different subjects. The authors demonstrated the effectiveness of the proposed framework on two benchmark datasets as well as their own dataset.

### Strengths
This research enhances the understanding of machine learning applications in EEG and emphasizes the potential of FSL techniques to address the challenges posed by limited training data in Motor Imagery (MI) classification.

### Weaknesses
There is no substantial innovation in proposed method combining the existing approaches without any significant modifications.

No comparisons were conducted with existing state-of-the-art methods that have addressed the same issue by leveraging meta-learning, domain adaptation/generalization, etc.

Although sophisticated MI-EEG embedding models have been developed recently, the proposed model has a very simple architecture.

Even though the dataset consists of 4 classes, is there a special reason why only 2 classes were used in the experiment?

### Questions
The overview of the proposed framework is poorly displayed in Fig. 1. It must be modified to clearly highlight the novelty of the proposed framework.

No comparisons were conducted with existing state-of-the-art methods that have addressed the same issue in a subject-independent or few-shot BCI manner by adopting meta-learning, domain adaptation, or generalization techniques.

Although sophisticated MI-EEG embedding models have been developed recently, the proposed model has a very simple architecture.

Even though the dataset consists of 4 classes, is there a special reason why only 2 classes were used in the experiment?

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors present a few-shot learning framework for motor imagery (MI) classification. This framework begins with a CNN that embeds signals from different electrodes independently. This is followed by an attention module that combines information across channels. Finally, a CNN+FC network computes relation scores between pairs of examples, allowing to retrieve the closest example from a query set. 
The framework is evaluated on two publicly available datasets, and the authors also introduce and evaluate on a novel MI dataset.

### Strengths
The authors have collected a novel MI dataset and have indicated that they will make it publicly available. This contribution is a valuable new resource for the community.
In addition, data scarcity is a common issue in BCI, and the authors address this challenge by introducing their few-shot learning framework.

### Weaknesses
Major
- The performance of the few-shot learning framework “RelationNet-attention” does not seem competitive because the baseline “CNN-attention-All”, which is trained on the same data as RelationNet-attention but without using examples from the test subject, systematically performs better. The difference in accuracy seems significant as it is systematically greater than 10%.

Minor
- Figure 3 misses its x-axis.
- The method is evaluated on only two benchmark datasets. The claims could be strengthened by conducting experiments on additional datasets. A large collection of MI datasets can be found in the MOABB library (http://moabb.neurotechx.com/docs/dataset_summary.html).
- The acronym DA is used both for “data augmentation” and “domain adaptation”. 
- The “domain adaptation accuracy” is not defined.
- As I understand, “CNN-attention-relation” and “RelationNet-attention” refer to the same model. To improve readability, I would recommend using a single name throughout the paper.
- The quality of the figures and diagrams can be improved.
- In my opinion, the writing could be improved to better guide the reader through the method.

### Questions
- Line 97: Could you provide additional an explanation on how the FSL-MIC framework can “reduce training time”?
- Is my interpretation of the results (in section Weaknesses -> Major) correct? If not, please correct me.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The authors investigate effective few-shot learning algorithms for EEG-based motor imagery classification. Specifically, transfer learning and data augmentation techniques are employed to achieve superior performance. Additionally, a meta-learning-based framework, termed Few-Shot Learning for Motor Imagery Classification, is presented for classifying unseen subject categories in a few-shot setting. Overall, this work lacks novelty and motivation and also requires further experimentation.

### Strengths
The authors introduce a relation network-based meta-learning framework for EEG-based motor imagery classification.

### Weaknesses
(1) Motivation – The meta-learning computational framework focuses on “learning to learn” various tasks (meta training) that contribute to downstream tasks (meta testing). During the meta training, the model’s goal is to uncover common patterns among these tasks and acquire broad knowledge that can be applied in solving new tasks. However, the authors apply very few tasks, specifically left and right hand classification, and these tasks are directly related to downstream applications. The stated motivation for meta-learning is somewhat limited. The authors should clearly indicate how they train their framework in a meta-learning fashion, detailing the specific episodic training procedure used, and how the task distribution is designed to foster generalization to new, unseen motor imagery tasks.

(2) Motivation – The authors propose to use few-shot learning, where the model should be trained on very limited data. However, the authors only use the few-shot examples as the “support set” during the testing phase, which could leak classification information. The methodology should clarify how the support set is used during meta-training and how this differs from its use during meta-testing. It is crucial to ensure that the model is not inadvertently trained on the support set during the testing phase.

(3) Related Works – Many related works are indeed missing in the field, such as [1].

(4) Experiments – The authors are encouraged to conduct experiments on larger benchmarks, such as the PhysioNet dataset and the High Gamma dataset. These datasets offer a more diverse range of subjects and conditions, which would provide a more robust evaluation of the proposed method's generalizability.

(5) The authors should provide high-quality figures. The current figures lack clarity and do not effectively convey the information. Specifically, Figure 1 is difficult to interpret, and Figure 3 lacks sufficient detail.

### Questions
(1) Where are the training recipes and algorithms of meta-learning in this work? 

(2) Why do the authors use few-shot learning on the testing set? Using the few-shot learning on the testing set can lead to information leakage. 

(3) Why don't the authors use the latest benchmarks that contain more subjects?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The work proposes an architecture combining a CNN-based embedding module and relation module for a few-shot learning on motor imagery-based eeg classification. The authors benchmark the performance on 2 public datasets and 1 experimental dataset of motor imagery using accuracy and domain adaptation accuracy metrics.

### Strengths
Work addresses the appropriate need for user-specific variability in EEG data and chooses to experiment with comparatively less explored approach of the few-shot learning.

The paper is decently written and easy to read and interpret.

### Weaknesses
The work doesn't cite a very similar approach by An et al. (2023). However, the authors cite work from An et al. from 2020. Authors must elaborate on their novelty and benchmark performance against similar approaches to claim state-of-the-art performance on few-shot learning.
Link to the work by An et al. (2023)
https://ieeexplore.ieee.org/abstract/document/10167679/?casa_token=ffiyMyxrlIYAAAAA:XHnQorLPEOuFdPLMhuSnkOj18y4baOutFkRqO4Zu6J1N2pKEBdsQ0cN0PvtXe3_M9R3VZvL1deH3

EEG tends to have high noise and authors though cite this concern and also claim interpretability mentioning: "A key advantage of this model is its interpretability", do not share any results, comment or compare the neurophysiological basis of the model predictions. 


Ethical guidelines while collecting personal data need to be clarified. Details on the code of ethics before releasing the data are necessary but missing.

### Questions
Figure 3 plots the performance on different datasets across trials. However, the axis is not labelled, and it confuses the reader by referring to "trials" without context. What do the trials mean?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
**Overall Assessment**

The paper addresses a significant problem in EEG motor imagery classification using few-shot learning. However, the novelty of the research question and the approach remain limited, which affects the contribution and impact of this study.

### Strengths
**Key Strengths**

* Problem Significance: EEG-based MI classification for BCI applications is a highly relevant research area, especially given the challenges of data scarcity and cross-subject variability.
* Dataset Contribution: The authors introduce a new dataset specific to their experimental needs, potentially serving as a resource for further MI EEG research.
* Attention Mechanism and Data Augmentation: The use of an attention mechanism to enhance feature extraction and a data augmentation strategy to improve classification accuracy aligns well with current trends in EEG and time-series signal analysis.

### Weaknesses
 **Major Concerns and Areas for Improvement:**

1. Limited Novelty in Approach and Research Question
    * While the problem is essential, the paper does not introduce significant advancements in methodology or approach, primarily adapting existing frameworks for few-shot learning.
    * The techniques, including data augmentation and attention mechanisms, are well-known and lack customization to the problem at hand. The specific implementation of these techniques, such as the choice of augmentation parameters or the architecture of the attention module, are not justified in the context of EEG signals.
2. Insufficient Literature Review
    * The manuscript leans heavily on a limited set of cited works, neglecting a broader body of relevant and foundational literature. This oversight is evident, for example, in the omission of a citation for the seminal paper on the attention mechanism (Vaswani, A. "Attention is all you need." (2017)), which is essential for context or the omission of the Grad-CAM paper (Selvaraju, Ramprasaath R., et al. "Grad-cam: Visual explanations from deep networks via gradient-based localization." (2017)), or proper citation to the utilized baseline methods, etc.
    * The limited literature results in redundancy, where the few sources cited appear multiple times, reducing the depth of the discussion. Furthermore, the review does not adequately cover the existing literature on EEG signal processing techniques, particularly those related to feature extraction and classification.
3. Redundant Content and Limited Focus on Methodology
    * A large portion of the paper is dedicated to reintroducing prior works and discussing the dataset, with limited space allocated to details of the proposed method.
    * The method's description lacks sufficient depth to fully understand its contribution beyond existing frameworks, making it challenging to assess its true impact. The paper does not provide sufficient detail on the specific architecture of the FSL-MIC model, the training procedure, or the hyperparameter selection process.
4. Results and Experimental Design
    * The reported results do not demonstrate outperformance over baseline models (CNN-attention-All and CNN-attention-Few). This lack of improvement questions the validity of the proposed framework as a state-of-the-art advancement in EEG classification. The paper does not include statistical significance tests to support the claims of comparable performance.
    * It is unclear why the authors have not tested their own method using a 40-sample case, as they did with CNN-attention baselines. Including this setup would provide a more equitable basis for comparison, potentially even enhancing the own results. The authors do not address any limitations that might prevent this configuration, leaving the rationale for this decision unclear.
    * The experimental design could be expanded to assess the model’s performance to a broader range of baseline methods. The choice of baselines is limited and does not include other state-of-the-art few-shot learning methods or EEG classification techniques.
  5. Interpretability of Attention Mechanism
One of the noted strengths of the proposed framework is its attention mechanism. However, while the authors suggest interpretability as a benefit, no specific analysis or visualization is provided to demonstrate how the attention scores contribute to understanding EEG signal dynamics. Adding such interpretability analysis would clarify the attention module’s effectiveness in isolating relevant features in EEG data.


**Minor Concern:**

Presentation and Figure Quality: The quality of figures is low, which detracts from the visual clarity and effectiveness of the results. Enhancing figure resolution would improve the readability and professional presentation of the study.


### Questions
* Could you clarify why the FSL-MIC model was not tested with a 40-sample configuration, as was done with CNN-attention baselines? Would this configuration affect the fairness of the comparisons, and are there specific limitations in your framework that prevent this setup?

*  The results do not clearly indicate outperformance over the baseline models. Could you expand on how FSL-MIC claims to improve upon state-of-the-art methods, especially given the similar or lower performance metrics?

* Since the attention mechanism is highlighted as a significant feature of the proposed framework, are there plans to analyze or visualize the attention scores for interpretability? If so, what insights would this analysis provide regarding feature importance in EEG classification?

### Soundness
2

### Presentation
2

### Contribution
2
