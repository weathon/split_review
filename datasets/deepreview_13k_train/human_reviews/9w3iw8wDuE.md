# Entropy is not Enough for Test-Time Adaptation: From the Perspective of Disentangled Factors

- Decision: Accept
- Scores: 8, 6, 6, 8

## Abstract
Test-time adaptation (TTA) fine-tunes pre-trained deep neural networks for unseen test data. The primary challenge of TTA is limited access to the entire test dataset during online updates, causing error accumulation. To mitigate it, TTA methods have utilized the model output's entropy as a confidence metric that aims to determine which samples have a lower likelihood of causing error. Through experimental studies, however, we observed the unreliability of entropy as a confidence metric for TTA under biased scenarios and theoretically revealed that it stems from the neglect of the influence of latent disentangled factors of data on predictions. Building upon these findings, we introduce a novel TTA method named Destroy Your Object (DeYO), which leverages a newly proposed confidence metric named Pseudo-Label Probability Difference (PLPD). PLPD quantifies the influence of the shape of an object on prediction by measuring the difference between predictions before and after applying an object-destructive transformation. DeYO consists of sample selection and sample weighting, which employ entropy and PLPD concurrently. For robust adaptation, DeYO prioritizes samples that dominantly incorporate shape information when making predictions. Our extensive experiments demonstrate the consistent superiority of DeYO over baseline methods across various scenarios, including biased and wild. Project page is publicly available at \href{https://whitesnowdrop.io/DeYO/}{https://whitesnowdrop.io/DeYO/}.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new method for test-time adaptation (TTA) called Destroy Your Object (DeYO) that uses a novel confidence metric called Pseudo-Label Probability Difference (PLPD) to improve the adaptation performance and stability of test-time adaptation methods. The authors demonstrate the limitations of entropy as a confidence metric and compare the performance of DeYO with other TTA methods on the ImageNet-C and ImageNet-R benchmarks under various mild and wild test scenarios.

### Strengths
The proposed DeYO method is simple yet effective for improving the stability and performance of entropy-based TTA.

The idea and motivation behind Pseudo-Label Probability Difference (PLPD) are novel and interesting, providing new insights for the community.

The paper is strong on the empirical side. Extensive experiments with various model architectures, datasets, and mild/wild test scenarios are thorough.

### Weaknesses
The proposed terms “TRAP” and “CRP” are a bit hard to understand. The authors could refine the name and give more high-level/easy-understanding explanations about them in the Introduction. 

For parameter sensitivity analyses in Figure 7, could the authors report more results under different model architectures, datasets and test scenarios? This helps demonstrate the hyperparameters’ generality. 

Ablation studies in Table 6 are also highly encouraged to be conducted on different models, datasets and test scenarios.

### Questions
Pls refer to Weakness.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors found that using entropy as metrics is not enough in some biased scenarios. To address this, the authors devise a new metric namely Pseudo-Label Probability Difference. The experimental results demonstrate the effectiveness of the proposed metric.

### Strengths
1.	The authors empirically and theoretically analysis the entropy metric for TTA.
2.	The authors devise a metric namely Pseudo-Label Probability Difference that further improves the entropy metric.
3.	The proposed method is easy to understand and implement. I believe it can be applied to real-world applications. In addition, the proposed metric only requires negligible computational cost to compute, which would not introduce obvious latency compared with EATA or SAR.

### Weaknesses
1.	Could the authors give simple explanation TRAP factors and CPR factors? With this, the readers may easily to capture the motivation of the proposed metric.
2.	Could the authors explain more about the motivation of the choice of patch shuffled input as x’?

### Questions
It would be better if the authors could explain the motivations more clearly.

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
The paper works on test-time adaptation with entropy minimization. While the online updates with entropy minimization can lead to error accumulation, the paper proposed to do sample selection and weighting by the proposed DeYO, which combines entropy and pseudo-label probability difference. Experiments on several datasets with various distribution shifts show the effectiveness of the method.

### Strengths
1. The observation and theoretical demonstration of "entropy is not enough" on the spurious correlation shifts is interesting and motivating to the method.

2. The results of the proposed method on several datasets with different distribution shifts are good, demonstrating the effectiveness of the proposed method.

### Weaknesses
1. The motivating observations and theoretical support are conducted on spurious correlation shifts, which is mainly on the semantic level. Can this also be found and theoretically proof for the other distribution shifts like covariate shifts?

2. In 2.3, the paper theoretically demonstrates that entropy is not enough and it is better to incorporate the CPR factors for sample selection and reweighting in test time adaptation, which is done by the proposed PLPD. However, PLPD is then combined with the common entropy method in the experiments and implementations. Then what role does entropy play in sample selection? and how it helps  PLPD to incorporate the CPR factors?

### Questions
1. Did the authors try some other methods like data augmentation methods to replace the transformed one? Will they also work to incorporate CPR factors?

2. How do the thresholds in eq. (9) defined?

3. What are the numbers and sizes of the patches for patch shuffling? Will these also influence the adaptation?

4. Why PLPD and entropy sample selections behave differently for different distribution shifts in Table 6? How to select different methods for different distribution shifts? Is there any theoretical support for this problem?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
TTA approaches select good samples for TTA using entropy as a metric (some of the approaches, and not all as I point in my review). However, a sample can have low entropy but using spurious features for prediction. Including such samples for TTA can be hurtful as they use spurious features for low entropy. The authors propose patch shuffle augmentation to identify such samples and remove them. 
The paper has missing important baseline for some core experiments (Table 2 and Table 3), and it is not clear why the approach helps in WILD distribution shift (label shift, batch size 1).

### Strengths
Strengths:
- The problem is well motivated i.e. spurious features can cause entropy to be low.

### Weaknesses
Weakness:
- Unclear what the authors mean by “disentangled latent vector” exactly for each image. No proper reference has been made as well to get details. It would be better to write more explicitly how does Equation 6 arise for fluency of the reading flow. Authors mention $x^{T>>C}$, please describe this notation (and might be not even required to introduce this as it is clear authors mean second term is more pronounced).
- It is not a great practice to include the whole of related works in the appendix. Even the related works section on TTA in appendix is extremely sparse (a single paragraph!) and should be much more broader in it’s scope.
- I understand that authors aim is to reject samples which use spurious features for prediction as doing TTA on them might be harmful. However, past theoretical work (https://proceedings.neurips.cc/paper/2020/file/f1298750ed09618717f9c10ea8d1d3b0-Paper.pdf) shows that self training avoids using spurious features.
- There are many methods which assess augmentation + entropy (see MEMO, SENTRY https://arxiv.org/pdf/2012.11460.pdf). SENTRY does sample filtering based on consistency of predictions over various augmentations. It is a crucial and missing baseline in this work, especially in Table 2 and Table 3. I know SENTRY operates in UDA setting, but the consistency over augmentations part is pretty standard.
- The authors mention existing works use entropy for selective minimization. There should be a baseline where we do selection based on average entropy over multiple augmentations. It is a trivial extension of previous works and should have been a baseline to asses the effectiveness of pseudo-label confidence drop proposed in this work.
- Why is the MEMO baseline missing in Table 2 and Table 3, where I would guess MEMO to be most effective as it also does entropy average over multiple transformations. It is quite possible that the average entropy over augmentations is low for spurious correlations domainted prediction, making those samples contribute much less to the loss anyways.
- Can the authors give any reason why their proposed approach should work better under label shift or for batch size 1 as shown in Table 5? I do not see any reason why augmentation based sample selection should help for label shift TTA (makes sense for spurious TTA). Similar is the question for Batch size 1 setting. Are the authors sure they did proper hyperparameter tuning for the baselines?
- Further, the effect of such spurious correlations can be removed by incorporating such transforms (cutmix, random cropping, or the used patch shuffling) during pretraining itself. Will the proposed approach help in those cases as well?

### Questions
See the weakness section for questions to answer during rebuttal

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
