# Going beyond familiar features for deep anomaly detection

- Decision: Reject
- Scores: 3, 3, 5

## Abstract
Anomaly Detection (AD) is a critical task that involves identifying observations that do not conform to a learned model of normality.
Prior work in deep AD is predominantly based on a familiarity hypothesis, where familiar features serve as the reference in a pre-trained embedding space. While this strategy has proven highly successful, it turns out that it causes consistent false negatives when anomalies consist of truly novel features that are not well captured by the pre-trained encoding. We propose a novel approach to AD using explainability to capture novel features as unexplained observations in the input space. We achieve strong performance across a wide range of anomaly benchmarks by combining similarity and novelty in a hybrid approach. Our approach establishes a new state-of-the-art across multiple benchmarks, handling diverse anomaly types while eliminating the need for expensive background models and dense matching. In particular, we show that by taking account of novel features, we reduce false negative anomalies by up to 40% on challenging benchmarks compared to the state-of-the-art. Our method give visually inspectable explanations for pixel level anomalies.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes hybrid framework with a familiarity branch and novelty branch for anomaly detection. The familiarity branch is based feature comparison, and the novelty branch is based on B-cos network’s explanations.

### Strengths
Introducing novel features for anomaly detection is interesting, it seems that it can be further studied.

### Weaknesses
1. I think the novelty branch and familiarity branch are similar. The familiarity branch detects anomalies by comparing test samples features with normal samples features, while the novelty branch relies on anomalies with different explanations with normal. I feel this is just transfer from the feature space to the B-cos network’s explanations. 

2. Bad academic terminology: “the complementary set is the background B…”, it’s weird to call anomalies as background set. In the defect detection (or sensory anomalies in paper), background generally refers to normal regions. Even for semantic anomaly, it’s also weird to call anomalies as background. The description of familiar and novel features is also hard to follow.

3. Evaluation on sensory anomaly dataset is not enough, only MVTec. Moreover, your method performs poorly on sensory anomalies and cannot compared with the anomaly localization methods. So, just focus on the semantic anomaly, your method visual inspectable explanations are not very valuable.

### Questions
1. According to the assumption in the paper, untrained anomalies don’t belong to the familiar space, so these anomalies will be determined as false negatives? Moreover, anomaly appearances are usually different from normal, although the network don’t generate representations in the familiar space, the network will generate representations that are different from normal. So, anomalies can also be determined through familiarity branch.

2. Thus, I think you should demonstrate that kind of anomalies will be determined as false negatives by the familiarity branch, and the novelty branch can solve this. Although Figure 6 shows that the novelty branch can reduce false negative rate, this figure is likely unfair, as we don’t know what the familiarity-based method specifically refers to. It needs to your familiarity branch to be fair.

3. Figure 5 still cannot explain the effectiveness of your method. Adding novelty only increases the distance of anomalies that could be classified in the first figure, but the confusion regions in the first image still exists in the third figure.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper examines the distinction between novel and familiar features in the context of anomaly detection and proposes an AD methodology which jointly models both novel and familiar features in its scoring.

### Strengths
Considering performance for both semantic and sensory anomaly detection with a single methodology is beneficial and also often neglected in other works, and this methodology does appear to give the best overall performance across both types of AD tasks.

Anomaly detection via explanation is a relatively under-explored approach.

### Weaknesses
Section 3 can summarised in just one sentence that comes near the end: "In summary, the xˆtest can contain features outside FAD that might be causing the anomaly." As such, it is hard to justify the very heavy use of notation, the explanations of novel and familiar features are longwinded and their definitions are also not very clear. This section could be made more clear and concise, defining exactly what differentiates familiar and novel features. The distinction between 'familiar' and 'novel' features is not rigorously defined, leading to ambiguity in the methodology. For instance, it's unclear if 'novel' refers to entirely unseen features or simply deviations from the learned distribution of 'familiar' features. The use of notation, while mathematically precise, obscures the core intuition, making it difficult to grasp the practical implications of the proposed approach. A more intuitive explanation, perhaps with illustrative examples, would greatly enhance the clarity of this section.

Some aspects of the experiments are not particularly clear (see questions 1 and 2).

In Figure 5, by choosing to present only the samples that give the maximum deviation from the training set upon adding the novelty score,  the figure is artificially amplifying the effect of the novelty score. It would be better to randomly sample points to give a more unbiased picture of the effect of the novelty score. The current presentation in Figure 5 is misleading as it only shows extreme cases where the novelty score has the largest impact. This selective presentation does not provide a representative view of the method's performance across the entire dataset. A more rigorous approach would involve randomly sampling data points to demonstrate the typical effect of the novelty score, or even better, showing the distribution of the novelty score's impact across the dataset.

Section 5.2 is not well argued as it is not clear that this methodology has reduced the role of the background class, as there are no experiments that measure performance with and without training with the background class. Instead, this paper simply changes the way the background class is generated. The claim that the methodology reduces reliance on the background class is not substantiated by direct experimental evidence. The authors only change the way the background class is generated, but do not show results with and without using a background class. To validate this claim, the authors need to demonstrate the performance of their method when trained without any background class, and compare this to the performance with the background class. This would provide a more compelling argument for the reduced reliance on the background class.

### Questions
1. What were the classes chosen for the near-AD experiments? How were these classes chosen? Were other class splits tested and, if so, how did performance vary between them?

2. What is in the intuition of using the normal approximation to simulate anomalies. How about other augmentation strategies used in anomaly detection in previous works?

3. What is the intuition that ensures that using explanations from the B-cos network focuses on identifying novel features in its scoring. How are we sure it is not relying on the deviation in familiar features between normal and anomalous samples, just like the familiarity score module?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The manuscript deals with anomaly detection. Previous works model anomaly detection according to the familiarity hypothesis in which the absence of training features indicates anomalous input. The manuscript extends this line of work by complementing familiarity-based AD with novelty-based AD. Features are novel if they are unexplainable according to the observed data. In practice, explainability is captured by previously introduced B-cos networks, while familiarity is modelled using a memory bank of training features.
The resulting hybrid formulation yields fewer false-positive responses in different relevant experimental setups.

The manuscript claims the following contributions:

C1.  Formal definition of familiar and novel features in the context of anomaly detection. 

C2. A hybrid model for AD that accounts for the lack of familiarity and
the presence of novelty in an input sample.

C3. Strong experimental results with reduced incidence of false positive responses.

### Strengths
S1. The manuscript deals with an important issue of anomaly detection.

S2. Defining novel features according to the absence of explainability is an interesting idea.

S3. The presented experimental results are good.

### Weaknesses
W1. The manuscript claims a formal definition of familiar and novel features as one of the main contributions. However, the presentation in Sec.3 is rather poor - definitions of familiar/unfamiliar features are bundled together, the notations are non-standard, and the whole section is hard to comprehend. Claimed definitions of familiar and novel features should be neatly formulated with appropriate definitions, lemmas, and theorems as in [a].

W2. The proposed method has design choices that are not well explained. E.g. why are two nearest train features used in Eq. 3? What are the benefits/issues of using more or less neighbours?

W3. The definition of the final anomaly score should be clearly stated together with the corresponding equation.  

W4. The contribution of each component in the proposed hybrid anomaly score should be ablated.

W5. Missing relevant related work which introduces hybrid formulation for anomaly detection [b].

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair
