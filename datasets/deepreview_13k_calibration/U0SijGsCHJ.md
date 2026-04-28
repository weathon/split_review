# GPS: A Probabilistic Distributional Similarity with Gumbel Priors for Set-to-Set Matching

- Decision: Accept
- Avg Score: 6.40
- Scores: 8, 5, 8, 5, 6

## Abstract
Set-to-set matching aims to identify correspondences between two sets of unordered items by minimizing a distance metric or maximizing a similarity measure. Traditional metrics, such as Chamfer Distance (CD) and Earth Mover’s Distance (EMD), are widely used for this purpose but often suffer from limitations like suboptimal performance in terms of accuracy and robustness, or high computational costs - or both. In this paper, we propose a novel, simple yet effective set-to-set matching similarity measure, GPS, based on Gumbel prior distributions. These distributions are typically used to model the extrema of samples drawn from various distributions. Our approach is motivated by the observation that the distributions of minimum distances from CD, as encountered in real world applications such as point cloud completion, can be accurately modeled using Gumbel distributions. We validate our method on tasks like few-shot image classification and 3D point cloud completion, demonstrating significant improvements over state of-the-art loss functions across several benchmark datasets. Demo code is included in the supplementary file.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper presents a new similarity metric for set-to-set matching problems. The proposed similarity metric leverages Gumbel distribution as a prior to model k-NN across sets. This formulation makes the proposed similarity metric more robust to outliers compared to other similarity metrics like Chamfer Distance while being significantly more efficient to compute compared to robust metrics like Chamfer Distance. 

The proposed similarity metric is applied to model objective functions for two problem settings: few-shot classification, point-cloud completion. The proposed metric outperforms other metrics across all evaluations and is similar to Chamfer Distance in runtime.

### Strengths
- Set-to-set matching is fundamental to many problem settings, the proposed formulation is novel, theoretically well-motivated and empirically outperforms other similarity metrics in chosen application domains. This is a significant contribution of interest to the wider community and can have impact beyond the two applications. 
- Extensive evaluation and transparent reporting of influence of hyperparamters on results.  
- I highly appreciate code submission.

### Weaknesses
 - As authors have already pointed out, searching for hyperparameters for the proposed formulation is non-trivial. This might limit wider adoption of this metric.

 - The paper mentions that "Set-to-set matching aims to identify correspondences between two sets of unordered items by minimizing a distance metric ... " however it is not clear how the proposed metric can be used to yield such correspondences. While the metric is presented as a similarity measure, the paper does not clearly articulate how the Gumbel distribution is used to establish explicit mappings between elements of the two sets. This is crucial for applications like point cloud registration or matching where knowing the correspondence is as important as the overall similarity score. The paper lacks a detailed explanation of how the nearest neighbor search within the Gumbel framework translates to actual set element correspondences.

### Questions
- Have you considered applying the metric for matching and registration problems such as point cloud registration? The paper mentions that "Set-to-set matching aims to identify correspondences between two sets of unordered items by minimizing a distance metric ... " however it is not clear to me how the proposed metric can be used to yield such correspondences. It might be valuable to add some discussion on potential formulations for such applications.

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
The paper presents GPS, a Gumbel-prior-distribution mechanism to train models that can compare sets and compute correspondences. The idea is to use the Gumbel distribution to model extrema (minima or maxima) of the matching scores; this is based on Extreme Value Theory. GPS also proposes the use of an offset to compensate the modeled scores and improve the modeling of the scores. The paper presents experiments on image classification and point cloud completion where the proposed method consistently show improvements over the considered baselines.

### Strengths
- Motivation and description of the problem is quite clear and it is quite important. I agree that we need to investigate better solution for set-to-set matching. In particular, I agree that the use of the statistical Extreme Value Theory into ML/AI can bring benefits to many problems.
- The clarity of the paper in general is clear. The narrative is clear and I think the paper can be reproduce w/ some reasonable effort.
- The set of experiments is adequate and tackles different applications showing the benefits and applicability of the approach.

### Weaknesses
While I agree about the use of EVT or Gumbel distribution to tackle problems that require modeling extrema (minimum or maximum) of matching scores, I disagree with the use of particularly using the Gumbel distribution only. Here are the specific concerns:

1. According to EVT, the distribution that generally models the extrema (minima or maxima) is the Generalized Extreme Value (GEV) distribution; the Gumbel distribution is a special case of the GEV distribution. Thus, it is possible that for some problems the Gumbel distribution is not the appropriate one and thus it can affect performance. Note however that EVT in general can only be applied when the number of scores is large, otherwise, the theory and thus the distributions of EVT (including Gumbel) cannot be applied, strictly speaking. This is something that I think the paper is not exploring nor stating.

2. While it is true that Gumbel can model minima or maxima, it is not true that it can model order statistics. In other words, I think the narrative of the paper is correct only when it states that it models minima or maxima when comparing entities of a set. However, the Gumbel distribution cannot model order statistics, i.e., statistics of the 2nd, 3rd, or Kth scores. Given this, I find concerning that the paper uses it to model the k-th nearest neighbors using a mixture of Gumbel distributions (lines 200 - 203). EVT only models the minima or maxima, but not the order statistics. I don't see a justification in the paper describing rigorously the use of Gumbel distribution in this case. Unless, the introduction of $\delta$ as shown in line 232 compensates for that. But unfortunately the paper does not justifies this well.

3. The paper is missing prior work exploring EVT to model minima/maxima in matching procedures. Thus, I think the narrative overstates that this is the first work using statistical information for set-to-set matching. See references shown below.

4. Incomplete experiments. While I think the applications used in the experiments are diverse, I think the experiments would've been more informative and more convincing if they could show that other models (e.g., a transformer, or CLIP) also benefit from the proposed GPS.


### Questions
1. Why is the use of $\delta$ necessary from the theoretical point of view?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
It proposes a novel probabilistic method for set-to-set matching called GPS (Gumbel Prior Similarity), based on distributional similarity and Gumbel distributions. This method measures the similarity between the underlying distributions generating the sets. This research is very meaningful and contributes a lot.

### Strengths
1. The method presents an innovative probabilistic approach to set-to-set matching based on distributional similarity and Gumbel distributions. The idea is quite novel and significant, as it is helpful for the training of differentiable neural networks and offers considerable value to the community.

2. The experiments look promising, especially regarding the superior performance in few-shot image classification and 3D point cloud completion.

3. The paper is well-written and easy to follow.

### Weaknesses
I don't see any obvious drawbacks, but I am concerned about the efficiency issues mentioned in your limitations.

### Questions
I have some suggestions. The proposed method can perform better in set-to-set matching, demonstrating good performance in few-shot image classification and 3D point cloud completion. I am particularly interested in whether it can also achieve good performance in image matching and point cloud matching, as they also involve the set-to-set matching problem. If it performs well in these areas, it would further highlight the impact of your method. If possible, please consider adding relevant experiments.

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
The paper proposes to calculate the similarity between sets based on the Gumbel prior distribution.

### Strengths
The presentation is nice and clear.
Very interesting set of experiments and they are extensive.

### Weaknesses
The GPS method proposed in the paper calculates the similarity between sets based on the Gumbel prior distribution, which is, to a certain extent, an improvement on existing methods. However, the degree of this innovation is relatively limited. For example, within the framework of set matching and similarity learning, many studies have attempted to introduce new methods and ideas from different perspectives. The GPS method, which is based on distance distribution fitting and the use of Gumbel distribution, has not fundamentally broken through the scope of existing research.

There is a lack of in-depth theoretical discussion on some key issues. For example, in practical applications, the assumed independent and identically distributed conditions are difficult to strictly meet. The paper only shows that the assumption seems feasible through experimental results, but does not theoretically analyze the error range brought by this approximation and the potential impact on the performance of the method. This theoretical incompleteness may affect the reliability and universality of the method.

The experiments are mainly focused on a few common image classification and point cloud completion datasets. Although these datasets are representative, they cannot fully cover all possible application scenarios and data distributions.

Although the paper claims that the GPS method has achieved better results than some existing methods in the experiment, a careful observation of the experimental data shows that in most cases, the performance improvement is relatively small. For example, the accuracy improvement on some datasets may be only a few percentage points, which may not be significant in practical applications, especially considering the additional computational cost and model complexity that may be introduced.

### Questions
There is a lack of in-depth theoretical discussion on some key issues. For example, in practical applications, the assumed independent and identically distributed conditions are difficult to strictly meet. The paper only shows that the assumption seems feasible through experimental results, but does not theoretically analyze the error range brought by this approximation and the potential impact on the performance of the method. This theoretical incompleteness may affect the reliability and universality of the method.

The experiments are mainly focused on a few common image classification and point cloud completion datasets. Although these datasets are representative, they cannot fully cover all possible application scenarios and data distributions.

Although the paper claims that the GPS method has achieved better results than some existing methods in the experiment, a careful observation of the experimental data shows that in most cases, the performance improvement is relatively small. For example, the accuracy improvement on some datasets may be only a few percentage points, which may not be significant in practical applications, especially considering the additional computational cost and model complexity that may be introduced.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This manuscript concentrates on the task of set-to-set matching. To this end, motivated by the observation that the distributions of minimum distances fro CD can be accurately modeled by Gumbel distribuctions, it proposes GPS based on Gumbel prior distributions. The proposed method has been validated on tasks including few-shot image classification and 3D point completion, and the results demonstrate its significance.

### Strengths
1. The idea of GPS is novel and interesting, expecially considering that metrics like Chamfer Distance have been widely adopted in many research areas and replacing Chamfer Distance with GPS maintains the same linear computational cost

2. The writing of this manuscript is acceptable

3. The proposed method has been validated on different tasks, and the experimental results demonstrate its significance

### Weaknesses
1. The organization of this paper can be further improved. For example, on the first page, Fig.2 is placed before Fig.1. Fig. 2 (c) is kind of confusing for me, even if I have read related context for several times. 

2. In Section.3, Fig.3 doesn't help understand the methodology, but even make me more confusing. 
There should have one image that helps understand the design of GPS better. In the current version, any of  Fig.1, Fig.2, Fig.3  doesn't help too much. I think there also lacks a figure demonstrating the whole paradigm of applying GPS to a specific task.

3. For the experimental part, I think the task of image matching (SuperGlue, CVPR 2020) or point cloud matching (Predator, CVPR 2021) should also be considered, as establishing correspondences is a fundamental problem in computer vision.

### Questions
See weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3
