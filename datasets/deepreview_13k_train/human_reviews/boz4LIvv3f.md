# Seeking Flat Minima with Mean Teacher on Semi- and Weakly-Supervised Domain Generalization for Object Detection

- Decision: Reject
- Scores: 6, 5, 6, 5

## Abstract
Object detectors do not work well when domains largely differ between training and testing data.
To overcome this domain gap in object detection without requiring expensive annotations, we consider two problem settings: semi-supervised domain generalizable object detection (SS-DGOD) and weakly-supervised DGOD (WS-DGOD).
In contrast to the conventional domain generalization for object detection that requires labeled data from multiple domains, SS-DGOD and WS-DGOD require labeled data only from one domain and unlabeled or weakly-labeled data from multiple domains for training.
In this paper, we show that object detectors can be effectively trained on the two settings with the same Mean Teacher learning framework, where a student network is trained with pseudo-labels output from a teacher on the unlabeled or weakly-labeled data.
We provide novel interpretations of why the Mean Teacher learning framework works well on the two settings in terms of the relationships between the generalization gap and flat minima in parameter space.
On the basis of the interpretations, we also show that incorporating a simple regularization method into the Mean Teacher learning framework leads to flatter minima.
The experimental results demonstrate that the regularization leads to flatter minima and boosts the performance of the detectors trained with the Mean Teacher learning framework on the two settings.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper focuses on how to generalize the object detectors from the source domain to the target domain while the label of target domain is unavailable. Two settings: semi-supervised and weakly-supervised domain generalizable object detection (SS-DGOD and WS-DGOD) are defined. Based on these settings, the authors propose a mean-teacher-based framework, and make theoretically interpretation on how the mean-teacher-based framework works. A regularization term is added to the framework based on the interpretation, which improves the performance of both SS-DGOD and WS-DGOD.

### Strengths
1. This paper is well-written and easy to understand.
2. Theoretical interpretation is given to make the readers better understanding the mean-teacher frameworks and the proposed approach.
3. The proposed approach with the regularization term outperforms the SOTA and the baseline method. Ablation studies are sufficient.

### Weaknesses
1. The baseline method under the SS-DGOD significantly outperforms the SOTA method CDDMSL (in Table 2). For “watercolor” and “clipart”, the margins are larger than 10% mAP50. It seems that ”EMA” and “PL” play a vital role in the proposed framework, which however are common tricks under semi-supervised settings. Is it possible to compare the proposed method with “CDDMSL+EMA+PL”, or even “CDDMSL+EMA+PL+Regul.”? If so, the comparison could be more convincing, while the generalization ability to vary detection frameworks of the proposed approach is also validated.
2. In Figure4, both of the input and output of the framework are modified to make sure that the teacher and student produce the similar predictions. Does this modification increase the risk of network collapse, making it more difficult or slower to train the model?

### Questions
I think the quality of this paper is good, and I am glad to see the response of the weaknesses above.

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
The paper focuses on domain generalization for object detection where the domain differences between the training and testing domains is huge. The authors introduce two new setups: semi-supervised domain generalizable object detection (SS-DGOD) and weakly-supervised DGOD (WS-DGOD), where labeled data from one domain and either unlabeled or weakly-labeled data from multiple domains are used for training. The authors suggest a Mean Teacher learning framework with a student-teacher model that uses pseudo-labels to find flat minima in the parameter space, which helps improve the model's ability to generalize. The proposed method shows better object detection performance on unseen domains through a simple regularization technique that creates flatter minima.

### Strengths
1. The paper introduces two new settings for domain generalizable object detection: semi-supervised DGOD (SS-DGOD) and weakly-supervised DGOD (WS-DGOD), which have not been actively explored before. These settings are novel approaches to domain generalization, which is not commonly applied in object detection research.

2.The paper also provides theoretical reasoning for why the Mean Teacher learning framework works well in SS-DGOD and WS-DGOD settings, particularly in terms of finding flat minima.

3. Experiments are conducted to validate the effectiveness of the proposed method, showing improved robustness across various domains.

### Weaknesses
The major concern of this paper is its incremental novelty.
The concept of domain-generalizable object detection is interesting, but the proposed method lacks significant novelty. The major idea—regularizing the two networks to produce more similar outputs, also known as consistency regularization—is a widely used framework in the mean-teacher student approach (e.g., FixMatch). Although the authors slightly modify the pipeline by using weakly augmented inputs for both networks, the reviewer cannot find any substantial technical innovation in the proposed method.

### Questions
1. What is the difference between recent mean-teacher based semi-supervised methods and the proposed method?

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper delves into Semi-Supervised Domain Generalizable Object Detection and Weakly-Supervised Domain Generalizable Object Detection. This paper addresses these two tasks using Mean Teacher framework, and provide interpretations from the perspective of flat minima. Based on this interpretation, this paper provides two tricks to achieve flatter minima, include providing weak data augmentation for the student model during Mean Teaching, and generating pseudo labels for object detector without post-processing. Experiments validate the effectiveness of the proposed method.

### Strengths
-	This paper is well motivated.
-	Theoretical analysis is provided.
-	The proposed method is simple yet effective.
-	The supplementary material is sufficient and abundant.

### Weaknesses
- Related work about Semi-Supervised Domain Generalization (SSDG). The listed previous work of SSDG in Section 3.3 assumed that there are labeled and unlabeled data in each training domain. And this paper assumes that there only one labeled training domain while the other training domains are all unlabeled (or weakly labeled). The SSDG setting of this paper is more similar to [1].

- The interpretations of model generalization from the perspective of flat minima had appeared in many previous works, such as [2,3], to name a few. Specifically, the connection between flat minima and generalization has been explored in the context of domain generalization, as seen in [2]. The authors should discuss how their interpretation differs from or builds upon these existing works. For example, what novel insights does this paper provide regarding the relationship between flat minima and the Mean Teacher framework in the context of object detection?

- Although the interpretations of Mean Teacher from flat minima is inspirable, the proposed method and the corresponding two tricks are kind of lacking technique novelty. As mentioned above, there had been many previous works providing tricks to improve generalization by seeking flat minima. The authors utilize weak data augmentation for the student model and generate pseudo labels without post-processing. While these techniques are effective, they are not entirely novel. Other methods for achieving flatter minima, such as Sharpness-Aware Minimization (SAM) regularization, could potentially offer similar or better performance. Had you ever tried other existing tricks to improve flat minima, such as Sharpness-Aware Minimization (SAM) regularization? A comparative analysis with such methods would strengthen the paper.

- Although Table 2 validates the effectiveness of the proposed method, had you ever tried any other Semi-Supervised or Weakly-Supervised learning methods in the proposed two settings, SSDGOD and WSDGOD, so as to set up more baselines and highlight the superiority of the proposed method? This is particularly relevant since the paper introduces new settings. Comparing with existing semi-supervised or weakly-supervised methods adapted to these settings would provide a more comprehensive evaluation.

### Questions
See the weaknesses.

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
Object detectors struggle with domain gaps between training and testing data, but this issue can be mitigated using semi-supervised (SS-DGOD) and weakly-supervised domain generalizable object detection (WS-DGOD) approaches. These methods require labeled data from only one domain and utilize unlabeled or weakly-labeled data from multiple domains, reducing annotation costs. The authors demonstrate that the Mean Teacher learning framework, where a student network is trained using pseudo labels generated by a teacher network, effectively addresses both SS-DGOD and WS-DGOD settings. Additionally, the authors show that adding a simple regularization method to the Mean Teacher framework can lead to flatter minima in the parameter space, further improving detector performance across different domains.

### Strengths
1.  This paper is well written and organized. 

2. The two settings SS-DGOD and WS-DGOD are reasonable.

3. The performances are quite good.

### Weaknesses
1. Limited novelty: All adopted techniques including Mean Teacher, Flat minimal interpretation are existing technique.

2. The performances seems strange. The performances of the proposed methods better  than DGOD, Oracle and SOTA UDA-OD in Table 7. Can the authors provide more explanation. The authors could provide statistical significance tests for the performance differences and discuss potential reasons why their method outperforms DGOD and Oracle, which theoretically should have advantages.

### Questions
Please see Weakness.

### Soundness
3

### Presentation
3

### Contribution
2
