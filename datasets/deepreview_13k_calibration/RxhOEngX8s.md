# Expecting The Unexpected: Towards Broad Out-Of-Distribution Detection

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 5, 6

## Abstract
Deployed machine learning systems require some mechanism to detect out-of-distribution (OOD) inputs. Existing research mainly focuses on one type of distribution shift: detecting samples from novel classes, absent from the training set. However, real-world systems encounter a broad variety of anomalous inputs, and the OOD literature neglects this diversity. This work categorizes five distinct types of distribution shifts and critically evaluates the performance of recent OOD detection methods on each of them. We publicly release our benchmark under the name BROAD (Benchmarking Resilience Over Anomaly Diversity). We find that while these methods excel in detecting novel classes, their performances are inconsistent across other types of distribution shifts. In other words, they can only reliably detect unexpected inputs that they have been specifically designed to expect. As a first step toward broad OOD detection, we learn a Gaussian mixture generative model for existing detection scores, enabling an ensemble detection approach that is more consistent and comprehensive for broad OOD detection, with improved performances over existing methods. We release code to build BROAD to facilitate a more comprehensive evaluation of novel OOD detectors.\footnote{BROAD is freely accessible under a Creative Commons Attribution 4.0 Unported License at \url{https://huggingface.co/datasets/ServiceNow/PartialBROAD}. We use OpenOOD \cite{yang2022openood} for evaluations.}.\vspace{-4mm}

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper reviews Out of Distribution (OOD) Detection, in the sense of samples seen in the real world that were not covered in the training data. Two approaches are 
1) to create robust systems, designed to not degrade on OOD data, and 
2) to flag samples uncharacteristic of the training data.
Distribution shift detection appears more practical, but can be fooled, by the multiple ways OOD can occur for such diverse reasons (in images): as novel classes, adversarial attacks, synthetics, corruptions multiple labels. 

The paper introduces 
 - a new OOD benchmark with 12 datasets representing the various OOD reasons
 - benchmarking of a variety of existing methods published in the last decade,
 - And demonstration of a Gaussian Mixture Model of an ensemble of existing methods with significant gains over existing methods.

### Strengths
The paper offers a comprehensive view of why image recognition models may fail on images that have not been seen during training, and by a comprehensive set of tests demonstrates the relative value of existing detection methods when applied to tasks they were intended for, and for other OOD tasks that are related, but not explicitly targeted by the existing method.   Of note is the interesting comment on how to build OOD detectors with generative models, by use of a function they designate as "h(x)" that so to speak "sees inside" the generative network, offering an extended feature set for detection.  

The paper introduces a OOD classifier that is a combination of existing methods by use of a Gaussian mixture model that has better coverage, and achieves an AUC score on average superior to existing methods.

### Weaknesses
There isn't sufficient detail in the paper to re-construct the Gaussian mixture model (GMMs) proposed by the authors. GMMs are conventionally used to estimate density functions for oddly-shaped distributions, e.g. with multiple modes.  It is intuitive, in fact not unexpected, that creating an ensemble of detectors has better  performance on average than any individual detector, so the novelty of this finding is limited. however the results from the paper are not reproducible from the paper's contents. Given the scores how is the GMM density learnt? In what sense is this an ensemble? How does this generate a classification and thus an AUC? 

One gets the sense that this work would find a better audience in a more engineering-oriented conference where testing comparisons of performance were the primary interest, and algorithmic aspects were not.

### Questions
If the construction and output of the GMM classifier is actually revealed in the paper and this review overlooked it, please explain.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper propose a new visual OOD detection benchmark consisting of 5 types of distributional shifts (1) novel classes (2) adversarial perturbations (3) synthetic images (4) corruptions (5) images with multiple objects. The paper further evaluates the performance of various OOD detection methods (that do not require training/fine-tuning) and observe that the performance is inconsistent across different types of distribution shifts. Lastly, the authors propose to ensemble various scores with Gaussian mixture models, which demonstrates better performance.

### Strengths
- The overall organization of the paper is clear and easy to follow.
- The proposed ensembling method is straightforward and demonstrate good performance.

### Weaknesses
 - The major weakness of the paper is that most OOD detection scores considered in the paper are proposed to only handle novel classes. Expecting such OOD scores to detect adversarial perturbations and corruptions may be **out-of-scope** and unrealistic.

In particular, recent work [1] has demonstrated that when OOD samples are not involved during training (the setting considered in this work), it can be **theoretically impossible** to expect common OOD detection methods to work. Despite that detecting adversarial perturbations and corruptions are interesting tasks, directly utilizing post-hoc OOD detection scores is ill-justified and the failure is expected.

- In the multi-label scenario, it seems more reasonable to use object detection models instead of classification models. The failure of OOD detection based on classification models is expected. It would be more interesting to see the performance of OOD detection given bounding boxes.

### Questions
Method:
- Can authors justify in theory or principle why OOD detection methods are suitable for detecting adversarial perturbations and corruptions?

Experiments: 
- Can authors provide further OOD detection results with object detection models for the multi-label case?

[1] Fang et al., Is Out-of-Distribution Detection Learnable?, NeurIPS 2022

### Soundness
1 poor

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper propose a OOD benchmark comprising five different types of distribution shift. The result shows that the performance of OOD detection methods are not consistent over different types of distribution shift. The paper propose a method to ensemble different OOD detection methods to achieve consistent performence over different types of distribution shift.

### Strengths
1). The assessment of a broder OOD detection capabilities is interesting and probablity important for future OOD detection method development.

2). Extensive experiments have been done to benchmark the recent OOD detection methods.

3). Overall, the paper is clear and well-written.

### Weaknesses
My concerns are mainly about the proposed method.

1). The ensemble of OOD detection methods seems ad-hoc for this benchmark by evaluating and picking some of the methods that perform relatively well on the benchmark.

2). The proposed method of fitting GMM over scores from different OOD detection methods does not make sense to me. For example, in Sec.3, it says "this approach is adept at identifying atypical realizations of the underlying scores, even in situations where the marginal likelihood of each score is high, but their joint likelihood is low." It would be weird if most in-distribution samples can not achieve high likelihood at each score while out-of-distribution samples can, since all these methods aim at measuring if the sample is in-distribution. In other words, what is the advantage of fitting GMM over taking average of different scores?

3). The time complexity or the scalability of the proposed method is still of concern. Though the results shows that the time complexity of the proposed ENS-F is acceptable at 25% of the time for a normal inference. However, when comparing to the methods it ensembles (e.g. MSP takes 1% additional time), the time complexity is extremely high.

### Questions
1). The proposed method uses a validation set to fit GMM, does it affect the performance? With the use of additional data, is it fair to compare the proposed method with other baseline methods?

2). Does the proposed ensemble method outperform simple ensemble methods such as taking the average of the scores or the largest score? If so, why would it be?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper addresses the problem of OOD detection in deployed machine learning systems. The authors analyze existing OOD detectors, identifying a common limitation in their adaptability to diverse distribution shifts. To address this, they propose a new benchmark named BROAD, designed to evaluate OOD detectors across a wide spectrum of distribution shifts. This benchmark examines various scenarios, including novel classes, adversarial perturbations, synthetic images, corruptions, and multi-class inputs. Additionally, the authors introduce an approach that leverages an ensemble of reliable OOD detectors combined with a GMM.

### Strengths
The paper explains the existing limitations of current OOD detectors, providing a clear and compelling rationale for advancement in this domain. The paper's main strength lies in the introduction of the BROAD benchmark, which establishes a robust evaluation framework. This benchmark not only rigorously assesses OOD detector performance but also offers a critical insight into their ability to extend beyond the scope of novel classes. Through meticulous experimentation and analysis, the authors provide compelling evidence of OOD detector capabilities and potential areas of improvement. This well-constructed evaluation framework significantly contributes to the depth and reliability of the research findings.

### Weaknesses
The paper introduces an ensemble method for broad OOD detection; however, there are notable weaknesses. Its efficiency and inability to be scaled up raise questions about its practicality in real-world applications. Moreover, the paper lacks a clear roadmap or forward-looking guidance for the broader OOD detection community on how to effectively approach the challenges posed by the BROAD benchmark. While the intent to introduce a method is appreciated, the proposed method is clearly not the ideal solution to this intricate problem, as it does not offer new ideas or new directions to the OOD community. A more comprehensive analysis and discussion on potential future directions and steps for advancing OOD detection would greatly enhance the paper's overall impact and utility to the research community. This would provide valuable insights for researchers looking to build upon this work and make meaningful strides in the field of OOD detection.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
