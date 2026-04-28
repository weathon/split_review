# On the Limitations of Temperature Scaling for Distributions with Overlaps

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Despite the impressive generalization capabilities of deep neural networks, they have been repeatedly shown to be overconfident when they are wrong. Fixing this issue is known as model calibration, and has consequently received much attention in the form of modified training schemes and post-training calibration procedures such as temperature scaling. While temperature scaling is frequently used because of its simplicity, it is often outperformed by modified training schemes. In this work, we identify a specific bottleneck for the performance of temperature scaling.  We show that for empirical risk minimizers for a general set of distributions in which the supports of classes have overlaps, the performance of temperature scaling degrades with the amount of overlap between classes, and asymptotically becomes no better than random when there are a large number of classes. On the other hand, we prove that optimizing a modified form of the empirical risk induced by the Mixup data augmentation technique can in fact lead to reasonably good calibration performance, showing that training-time calibration may be necessary in some situations. We also verify that our theoretical results reflect practice by showing that Mixup significantly outperforms empirical risk minimization (with respect to multiple calibration metrics) on image classification benchmarks with class overlaps introduced in the form of label noise.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies the limitations of the widely used temperature scaling for post-hoc uncertainty calibration. The authors find that under the specific assumption, i.e., the datasets follow a general set of distributions in which the supports of classes have overlaps, the temperature scaling method cannot perform well. Since the temperature scaling has been very successful in post-hoc calibration, this paper is interesting for pointing out its limitations and find under some conditions it provably fails to achieve good calibration. Furthermore, the authors find that the performance of temperature scaling degrades with the amount of overlap between classes, and asymptotically becomes no better than random when there are a large number of classes. This paper also studies a specific training-time calibration technique mixup and finds that it can lead to reasonably good calibration performance under the same conditions.

### Strengths
1. This paper is well motivated. The studied point is interesting. It is empirically found that temperature scaling is good for calibrating deep models. However, as pointed out in this paper, it may harm calibration under some conditions.

2. The empirical study shows very supportive results for the theoretic results. Both experiments on synthetic data and real-world data show positive results that temperature scaling cannot work under some conditions.

3. The writing and organization of this paper is very good.

### Weaknesses
1. It is commonly believed that temperature scaling is very effective for post-hoc calibration scaling, although it is found that this technique cannot be used for all the cases. Can you explain what causes this gap between your theoretic results and the commonly observed empirical success?

2. The main experimental results in tables only show the comparison between ERM+TS vs Mixup. I think that the results of ERM baseline and Mixup+TS should be presented at least. Moreover, is the results influenced by the training schemes used for training models (such as learning epochs, learning rate and regularization)? Specifically, how sensitive are the results to the choice of optimizer, learning rate schedule, and regularization techniques, given that these can significantly impact the sharpness of the learned probability distributions and thus the effectiveness of temperature scaling?

### Questions
Please refer to Weakness section.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper demonstrated how temperature scaling has subpar performance in the case of overlapping classes, and proposed mixed up as an effective alternative to improve model calibration. The paper considers the ERM interpolator set of models, where there's clear separation between the prediction of top-class and the rest. In this case temperature scaling is failing to produce the desired behavior of equal prediction on the overlapping portion of the two classes. On the other hand, training with mixing loss is able to capture the overlapping behavior and significantly improve ECE.

### Strengths
- The paper is well written with clear presentation of references on background, assumption, and key results.
- There are theoretical results backing up the observations made in the toy examples and experiments.
- The few experiments shows good evidence supporting the conclusion that mixup is effective under the overlapping classes scenario.

### Weaknesses
 - The mixing training introduces an extra degree of freedom (i.e. d-mixing). Based on table 2, we see that mixing is actually negative for NLL when classes are relatively separate, but only show performance improvement as the overlap increase. I also believe that the model performance would not be strictly better as we increase the degree of mixing, not to mention the additional computational complexity. Intuitively, the optimal d should have to do with the structure of overlapping in the dataset. I think it would be beneficial for the authors to have a more in-depth discussion on the choice of mixing in practice. Discounting the additional regularization effect, is it reasonable to only have the regular mixup when only two classes overlap at a time?

 - The paper's analysis and experiments focus on the ERM interpolator model class, which, while common, may not be the most suitable for datasets with overlapping classes. The inherent property of interpolators to fit training data perfectly can lead to overconfident predictions, particularly in regions of overlap. This overconfidence is precisely what the paper aims to address, but the choice of model class seems to exacerbate the problem. While the paper does show that mixup can improve calibration for this model class, it doesn't address whether other model classes might be more suitable for handling overlapping classes from the start, potentially reducing the need for mixup as a post-hoc fix.

### Questions
- Does it make sense to generate additional classes for the overlapping case (y=1, y=2, y=1&2)? In that case would temperature scaling still work and what is the tradeoff here?
- Is ERM interpolator the best model class to capture the datasets with overlaps? The properties of the interpolator seem to be naturally mismatched.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper studies when and why temperature scaling may not work. This paper showed theoretically that when the supports of classes have overlaps, , the performance of temperature scaling degrades with the amount of overlap between classes, and asymptotically becomes no better than random when there are a large number of classes. This paper suggests that Mixup data augmentation technique can lead to reasonably good calibration performance, which are supported by the experiments conducted in the paper.

### Strengths
This paper identifies theoretical limitations of a widely used calibration technique, temperature scaling. The paper is technically solid and clearly written, with aligned theory and experiments.

Originality: The paper offers novel theoretical results on the inherent limitations of temperature scaling based on distributional assumptions. While temperature scaling is widely used, formal characterization of when it provably fails is new. The conditions identified are also intuitive and realistic.

Quality: The theoretical results are informative. [Note: I am not an expert in theory though, and I didn't check the proof]. The experiments cleanly validate the theory on both synthetic data and real image benchmarks. The proposed d-Mixup method is interesting. Overall the paper reflects quality research.

Clarity: The problem is motivated well and background provided. The writing clearly explains the theories, assumptions, experiments, and connections between them. Figures aid understanding. The paper is well organized.

Significance: Calibration is critical for uncertainty aware models, but little theory exists. This paper significantly advances understanding of an important technique. The insights on training procedures are impactful for future work.

### Weaknesses
1. The scope is limited to temperature scaling and Mixup. Discussing connections to other calibration methods could broaden impact.
2. It would be better to have more real data experiments. In the "IMAGE CLASSIFICATION BENCHMARKS", the overlap is introduced rather artificially.



### Questions
1. "We also trained d-Mixup models on the same data, but we found that the confidence regularization effect for d > 2 led to underconfidence on these datasets, so we report just the results for Mixup.": do we know why this may happen?
2. In the image experiments, for CIFAR-100, why having label noise makes NLL worse but ACE / ECE better? This makes the experiments less convincing if we don't have a solid explanations.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair
