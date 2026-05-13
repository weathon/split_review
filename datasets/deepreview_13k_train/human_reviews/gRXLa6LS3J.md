# Zero-shot Outlier Detection via Synthetically Pretrained Transformers: Model Selection Bygone!

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Outlier detection (OD) has a vast literature as it finds numerous applications in
environmental monitoring, security, manufacturing, and finance to name a few.
Being an inherently unsupervised task, model selection is a key bottleneck for OD
(both algorithm and hyperparameter selection) without label supervision. There is
a long list of techniques to choose from – both classical algorithms and deep neural
architectures – and while several studies report their hyperparameter sensitivity, the
literature remains quite slim on unsupervised model selection—limiting the effective use of OD in practice. In this paper we present FoMo-0D, for zero/0-shot OD
exploring a transformative new direction that bypasses the hurdle of model selection
altogether (!), thus breaking new ground. The fundamental idea behind FoMo-0D is
the Prior-data Fitted Networks, recently introduced by Müller et al. (2022), which
trains a Transformer model on a large body of synthetically generated data from a
prior data distribution. In essence, FoMo-0D is a pretrained Foundation Model
for zero/0-shot OD on tabular data, which can directly predict the (outlier/inlier)
label of any test data at inference time, by merely a single forward pass—making
obsolete the need for choosing an algorithm/architecture and tuning its associated
hyperparameters, besides requiring no training of model parameters when given a
new OD dataset. Extensive experiments on 57 public benchmark datasets against
26 baseline methods show that FoMo-0D performs statistically no different from the
2nd top baseline, while significantly outperforming the majority of the baselines,
with an average inference time of 7.7 ms per test sample.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces FoMo-0D, a novel zero-shot approach for outlier detection (OD) that bypasses the traditional model selection process, a major obstacle in unsupervised OD tasks. Model selection, including algorithm and hyperparameter tuning, has long been a challenge due to the unsupervised nature of OD. FoMo-0D leverages Prior-data Fitted Networks (PFNs), a Transformer-based model trained on a large synthetic dataset from a prior distribution, allowing it to make direct outlier predictions on new datasets without further tuning or training. As a foundation model for zero-shot OD on tabular data, FoMo-0D delivers outlier predictions with a single forward pass, eliminating the need for manual algorithm selection or hyperparameter adjustments. The authors of the paper conduct extensive experiments to demonstrate the effectiveness of the proposed method.

### Strengths
- The authors of the paper tackles an important yet very challenging problem of unsupervised anomaly detection. 
- The proposed method is technically sound. 
- The paper is well written and easy to follow. 
- The authors of the paper conduct ample experiments to demonstrate the effectiveness of the proposed method.

### Weaknesses
 - Despite the optimization done to scale the proposed method up, it is still not immediately clear to me how scalable the proposed method is. Does the proposed method still work if the training data contains millions of samples? Moreover, what is the inference latency and memory overhead? Would the proposed method incur very heavy computational burden if I have to handle a large number of samples during inference? Such a scenarios is arguably common in real world anomaly detection settings. 
- How limiting is the use of GMM for synthetic data generation for pre-training. Does such a method scale to more complex datasets?

### Questions
- I wonder if it would be possible to do some sort of finetuning when a training data comes in, so that we don't need to feed in the entire training data into the model?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper present FoMo-0D, the first foundation model for zero-shot OD on tabular datasets. FoMo-0D is pretrained on many synthetically generated datasets drawn from a novel data prior that the author introduce to capture various inlier and outlier distributions. Feeding the FoMo-0D with a new training set and a text point, it perform zero-shot inference on a new dataset via a single forward pass, fully abolishing the need for both model training on a new dataset and hyperparameter selection.

### Strengths
1. The paper presentation is clear. The proposed method is well-motivated.
2. The experimental results are highly sufficient and also demonstrate the effectiveness of the proposed foundation model.

### Weaknesses
1. While it is noted that "finding a prior that supports a sufficiently large subset of possible [data generating] functions isn’t trivial," the paper demonstrates that the initial attempts were adequate to achieve remarkable performance even with a simple data prior. Could you provide some in-depth insights into this result? Specifically, how does the choice of Gaussian Mixture Models (GMMs) as a data prior influence the model's ability to generalize to real-world tabular datasets, given that real-world data often exhibits more complex structures than those captured by GMMs? What are the limitations of using GMMs as a prior, and how might these limitations affect the performance of FoMo-0D on datasets with non-Gaussian or highly multimodal distributions?

2. The paper conducted experiments on several benchmark datasets for out-of-distribution (OOD) detection, including CIFAR-10, Fashion-MNIST, MNIST-C, MVTec-AD, and SVHN. I am curious about the performance of FoMo-0D on more complex datasets, such as the ImageNet-level benchmarks recently proposed in OpenOOD v1.5 [1]. It would be beneficial to see how the model scales to higher-dimensional data and more intricate outlier patterns present in these benchmarks. Furthermore, how does the performance of FoMo-0D compare to state-of-the-art OOD detection methods on these more challenging image datasets?

### Questions
See Weaknesses.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper leverages Prior-data Fitted Networks, which can directly predict the (outlier/inlier) label of any test data at inference time, by merely a single forward pass—making obsolete the need for choosing an algorithm/architecture and tuning its associated hyperparameters, besides requiring no training of model parameters when given a new OD dataset.

### Strengths
1. The paper is written well and is easy to understand.

2. The studied problem is very important.

3. The results seem to outperform state-of-the-art.

### Weaknesses
1. The baselines compared in this paper are not competitive enough. There are much more advanced OD algorithms that are unsupervised or semi-supervised and do not require retraining on the new test set. Please refer to [1] for more advanced algorithms. There are plenty of strong post-hoc algorithms that can be efficient and effective at the same time. Specifically, methods based on contrastive learning, which do not require labeled data, are absent from the comparison. These methods, such as those using a SimCLR-based approach, could provide a more rigorous benchmark for the proposed method.

2. The inlier piror and outlier synthesis idea is explored in [2]. Could the authors clarify the differences? For me, I did not see any significant technical differences from the prior selection and the synthesis approach, even though there are naunces in model architecture and the focused problem. The use of GMMs for inlier generation and methods from ADBench for outlier synthesis seems incremental, and the novelty of this aspect is not clearly established. The paper should better articulate how the specific combination and application of these techniques contribute to the overall approach.

3. Is it possible for the authors to show the actual detection metrics rather than the rank so that it makes the readers easy to see the algorithm performance.

### Questions
see above

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes to pretrain a foundation model on synthetic data for outlier detection, which utilizes in-context learning for the downstream detection tasks without hyperparameter tuning or post-training. The authors leverage the "router mechanism" to facilitate architecture scaling up and random linear transformation to speed up the synthesis process.

### Strengths
1. This paper presents a paradigm shift for outlier detection, training a foundation model for various downstream tasks without model selection and hyperparameter tuning.
2. The paper is well-written, which makes it easy to follow.
3. The experiments are sufficient for elucidating the intrinsic mechanisms of the proposed FoMo-0D.

### Weaknesses
1. While FoMo-0D doesn't require training on specific real datasets, it has inferior inference time compared to several baselines in Table 3, due to the forward pass of the whole training dataset during inference. If the training dataset scales up, there will be a high computation load during inference, undermining FoMo-0D's efficiency in time-critical inference scenarios.

### Questions
1. As the foundation model already achieves comparative performance compared with baselines, can the performance be continuously improved if we conduct post-training with specific real data, a common practice in NLP or CV?

### Soundness
3

### Presentation
3

### Contribution
2
