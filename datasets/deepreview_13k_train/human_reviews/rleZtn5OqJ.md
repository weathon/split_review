# Long-Tailed Recognition on Binary Networks by Calibrating A Pre-trained Model

- Decision: Reject
- Scores: 3, 3, 6, 6

## Abstract
Deploying deep models in real-world scenarios entails a number of challenges, including computational efficiency and real-world (\eg, long-tailed) data distributions.
We address the combined challenge of learning long-tailed distributions using highly resource-efficient binary neural networks as backbones. % for the first time.
Specifically, we propose a calibrate-and-distill framework that uses off-the-shelf pretrained full-precision models trained on balanced datasets to use as teachers for distillation when learning binary networks on long-tailed datasets.
To better generalize to various datasets, we further propose a novel adversarial balancing among the terms in the objective function and an efficient multiresolution learning scheme.
We conducted the largest empirical study in the literature using 15 datasets, including newly derived long-tailed datasets from existing balanced datasets, and show that our proposed method outperforms prior art by large margins ($>14.33\%$ on average).

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors introduce a "calibrate-and-distill" framework that leverages pretrained full-precision models on balanced datasets as teachers for distilling knowledge into binary networks on long-tailed datasets. They also propose an adversarial balancing mechanism and a multi-resolution learning scheme for improved generalization. Empirical validation on 15 datasets, including newly created long-tailed datasets, demonstrates performance improvements over previous methods.

### Strengths
- Using a large pre-trained network trained on the other dataset is a novel approach in long-tailed recognition.
- Plenty of experimental results is provided helping with understanding.
- The paper is well-writen and easy to follow

### Weaknesses
 - This paper demonstrates limited novelty, as it employs established methodologies, including knowledge distillation, multi-resolution techniques, adversarial training, and binary networks, which are well-documented in the existing literature.
- The scalability of this approach raises concerns, given its utilization of a teacher model of substantial size. Notably, in Table 2, only single-resolution is utilized, primarily due to VRAM limits.
- The incorporation of a non-LT pretrained network in advance does not appear to be a practical approach. One of the underlying motivations for addressing the long-tailed recognition problem stems from the inherent imbalances frequently encountered in natural datasets.
- It is advisable to update the set of compared methods in the experimental evaluation, as the current selection appears somewhat outdated. A more comprehensive comparison with contemporary methodologies is suggested.
- The mechanism by which the parameter $\lambda_\phi$ facilitates generalization across multiple data distributions remains unclear. In Figure 6, it is evident that, across all datasets, $\lambda_\phi$ consistently converges to a value of 1, indicating that towards the conclusion of the training process, improvements are predominantly focused on the classifier rather than the encoder. If the variation in the scheduling of $\lambda_\phi$ is considered essential for enhancing generalization, a more thorough explanation is needed.

### Questions
- How the large teacher model can effectively contribute to the performance of the binary network, particularly when a substantial domain gap exists between the dataset used for pretraining, such as ImageNet, and the actual target dataset, which could be, for instance, an MRI dataset in practical applications.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes to train the binary networks on the long tailed dataset. The motivation of the paper is to train the resource constrained binary network on a real-world long-taile dataset. For this the authors propose the Calibrate and Distill Framework, which uses a combination of feature similarity loss and logit distillation loss, to jointly optimize the neural network on the long tailed data. The three major components of the proposed approach are calibrate and distill, Adversarial lambda learning and Multi-Resolution training. The effectiveness of the proposed approach is demonstrated across 15 datasets including both the small scale and large scale dataset.

### Strengths
New Problem Introduced for the community.

Paper is well written and clear, with sufficient experimental results.

### Weaknesses
Motivation: I am unable to understand why this method is tailored towards long-tailed data. The loss functions proposed are generic and are not tailored towards long-tailed data.

Baselines: The baselines used in the current study are LT baselines which are not suitable to be directly applied for binary networks, hence perform inferiorly for binary networks. Creation of fair baselines where a reasonable method for training binary networks should be combined with LT methods. Hence, the current comparisons provided are unfair and require improvement. Some approaches from https://arxiv.org/pdf/2110.08562.pdf could be handy.

Missing References: Recently some works have been proposed which use flatness in long-tail learning which can be used for learning quantized networks on LT data. See [R1, R2, R3].

Setup: The pre-trained model used for distillation is trained on some other dataset, and hence doesn’t posses the same LT distribution as on target dataset. Hence, it’s unclear whether the LT classes in target dataset really constitute the long tail distribution or not.

### Questions
Why its a long tailed method? The multi-scale training, calibration and distillation and adversarial loss balancing all can be perfectly used on the balanced dataset. Can the authors please provide explanation regarding?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper addresses the long-tailed distribution in datasets on the training of efficient binary neural networks. By calibrating classifier layers of a large pre-trained teacher model to long-tailed datasets, this paper introduces a novel calibrate-and-distill framework. This method allows binary models to be distilled on the balanced pre-trained teacher. To further enhance generalization, the authors incorporate adversarial balancing and employ multi-resolution input techniques. Extensive experiments are conducted to validate the efficacy of the proposed CANDLE methods.

### Strengths
1. The constructed challenge of LT problem in binary NN directly relates to real-world applications, making it a compelling research question.
2. The design of the proposed "calibrate-and-distill" framework is both logical and coherent, adeptly aligning the general visual capabilities of teacher models with LT data. The detailed implementation makes it convincing.
3. The performance of CANDLE significantly outperforms that of other methods.

### Weaknesses
1. Although LT can pose challenges in binary NN training, it would greatly benefit the reader if there were experiments, illustrative demonstrations, and/or theoretical analysis that elucidate the specific difficulties it presents.

2. There are some instances where the writing or logical flow could be improved. I've noted some specific cases below:

2.1. The Introduction mentions various instances of large-scale generative models. However, given that the core technology of this paper focuses on discriminative tasks, it might be more relevant to provide examples like DINO and MAE.

2.2. The motivation part of the Introduction has the same problem. 

2.3. As the framework is around the concept of "calibrate-and-distill", it would be beneficial to provide some context on domain adaptation and model distillation in the Related Work section.

2.4 In the Approach section, clear mathematical formulations for the LT-aware CE loss and feature similarity are essential. Not all readers might be as familiar with these concepts as us.

2.5 The implementation of Multi-resolution learning in relation to the LT problem isn't well-defined. Elaborating on this would provide clarity.

### Questions
1. Regarding section 3.3, it appears that multi-resolution learning is primarily for efficient training. Would it be more fitting to discuss this within the implementation of experiments? Alternatively, is it integral to the overall framework's effectiveness?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes to train a binary network for long-tail recognition with the Calibrate and Distill framework, which fine-tunes the pre-trained model and trains the binary network at the same time with an adversarial balancing scheme.

### Strengths
1. The paper is clearly written.

2. The long-tail recognition problem in the low computation resource is quite relevant for machine learning applications.

3. The empirical study is intensive, which tests the proposed method and 6 baselines on 15 datasets.

4. The effectiveness of the proposed method is quite impressive.

### Weaknesses
The proposed method contains an MLP for learning the weighting hyperparameter. It is unclear how the architecture and the training hyperparameters of the adversarial network affect the final performance. More generally, the proposed method contains the training of three models and each of them may need difference training hyperparameters, which may make the hyperparameter tuning cumbersome. 

Minor: Fig. 8 and 9 are not quite clear as they are not high-resolution.

### Questions
Algorithm 1 shows that the learning rate for the three components is the same. Is this consistent with the experimental setting?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
