# Towards Faster and Stronger Deep Earth Mover's Distance for Few-Shot Learning

- Decision: Reject
- Scores: 6, 6, 5, 6

## Abstract
Recent works in few-shot learning (FSL) for visual recognition have indicated that dense features benefit representation learning across novel categories. One of  particularly interesting methods is  DeepEMD that is formalized as optimal  matching of dense features via  an effective statistical distance, i.e., Earth Mover's Distance. Despite its competitive performance, DeepEMD is computationally very expensive due to inherent linear programming. Towards addressing this problem, we propose a metric-based Gaussian EMD (GEMD-M) for FSL. We adopt  Gaussians for modeling  distributions and closed form EMD between Gaussians as a dis-similarity measure. We illuminate  that this metric amounts to feature matching, in which the optimal matching flows follow a joint Gaussian and can be expressed analytically.  As the distance in  GEMD-M is entangled and  not that GPU-friendly,  we further present a transfer learning-based Gaussian EMD (GEMD-T). The key idea is to learn a parametric EMD for a more discriminative metric based  on  square-roots of covariance matrices (via learnable orthogonal matrices) and mean vectors. The learnable metric in GEMD-T is decoupled and thus can be implemented by a fully-connected layer followed by a softmax classifier, very suitable for GPU. We conduct extensive experiments  on large-scale Meta-Dataset and three small-scale benchmarks. The results show   our GEMD is superior to  DeepEMD and  achieves  compelling performance compared to state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper mainly targets few-shot learning. The authors concentrate on the previous metric-based method DeepEMD. Sepcifically, they point out the drawbacks of DeepEMD in terms of efficiency, and accordingly propose to leverage the Gaussian EMD metric to replace the discrete EMD version. The authors further propose two instantiations for better parallel on GPU devices. The proposed method is evaluated on several datasets including Meta-Dataset, miniImageNet, tieredImageNet and CUB to show the effectiveness.

### Strengths
1. The idea of using Gaussian EMD is solid and interesting for few-shot learning.
2. The authors have provided extensive experiment results.

### Weaknesses
1. As explained in Sec.4.2, the method averages statistics from different samples to estimate the prototype. I wonder the difference between such implementation and treating all local descriptors from the same class as random samples from one Gaussian distribution and then estimating the statistics.

2. The authors mention in the paper that KL divergence is not suitable because it is asymmetric. What about Jensen-Shannon divergence? 

3. As for the efficiency comparison in Tab.3e, I think it would be better to compare the proposed method with not only EMD, but also other methods using pretrain and meta-train pipeline.

4. I notice that the proposed method performs worse than recent finetuning-based method [1,2] in SDL setting.

[1] Xu C, Yang S, Wang Y, et al. Exploring efficient few-shot adaptation for vision transformers. TMLR 2022.

[2] Basu S, Massiceti D, Hu S X, et al. Strong Baselines for Parameter Efficient Few-Shot Fine-tuning. arXiv 2023.

### Questions
Please refer to the weaknesses.

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this work, the authors propose two methods, GEMD-M and GEMD-T, built upon DeepEMD and utilizing Gaussian distribution for modeling. GEMD-M method demonstrates that EMD can be computed in a closed-form and formulates EMD as a feature-matching problem where features follow a joint Gaussian distribution. However, the EMD computation in GEMD-M is entangled and unsuited for GPU calculations. In contrast, GEMD-T introduces learnable orthogonal matrices to achieve parameterized learning of EMD and resolves the entanglement in calculations. Experimental results show that the GEMD method outperforms existing methods on cross-domain few-shot datasets such as Meta-dataset.

### Strengths
This paper introduces an outstanding few-shot recognition method, demonstrating the effectiveness of GEMD. By ingeniously employing Gaussian distribution modeling, it successfully addresses the high computational cost issue in DeepEMD. The paper introduces the GEMD method with learnable parameters, achieving decoupling of computations and further enhancing computational speed.

### Weaknesses
1. Several analyses in the paper lack experimental validation, as follows:
1) The paper mentions the drawbacks of KL divergence but lacks experimental results in the ablation studies to demonstrate whether GEMD outperforms KL divergence. This necessitates further experimental evidence from the authors.s
2) The paper mentions in both the title and the main text that GEMD-M and GEMD-T contribute to computational speed but lack experimental results to verify their effectiveness.
2. The conclusions in the paper are directly borrowed from the conclusions of previous articles, especially GEMD-T, where the derivation of some essential steps is missing, leading to a lack of coherence.

### Questions
1.Why wasn't the matching cost 1-cos(x, y) from DeepEMD used, and L2 distance was chosen instead? Does using 1-cos(x, y) still yield a more concise expression for EMD?
2. Can EMD be employed for the distillation learning of teacher-student models? If so, should using EMD for result distillation be considered in URL?"

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
The authors add the Gaussian EMD metric to the few-shot learning by modeling each channel feature (local feature) of each image as a Gaussian model, and then the EMD between Gaussian models is used as the metric of ProtoNet. Meanwhile, the authors accelerate the computational process by parameterizing the EMD metric so that it can be trained and computed on GPUs, enabling it to cover large-scale few-sample learning datasets.

### Strengths
In few-shot learning, it is important to explicitly represent the local features of the samples, and how to define the local features is very difficult to achieve in complex image distributions. By extracting and modeling the features of each channel of an image into a Gaussian model, the authors can model the local features without prior knowledge and match the local features between different samples by Gaussian EMD, which provides a new way of thinking for the representation of local features in few-shot learning.
The authors' experiments are adequate on both large-scale Meta-dataset and small-scale datasets to illustrate the validity of the method.

### Weaknesses
This work is lack of novelty. The essence of this work is to use Gaussian EMD as a metric based on ProtoNet, which is still not novel enough, although some existing methods are used to accelerate the process.
The figures in the paper are somewhat obscure, such as Fig 1(b). There are some typos in the writing, such as "Wang et al. (2017) propose" and the following "Bilinear pooling (Lin et al., 2018) or covariance pooling (Wang et al., 2021; Song et al., 2023) yields" in p3.

### Questions
The authors describe that the method consists of two stages, pre-training and meta-test. Please elaborate what is the loss in meta-test and if possible how to finetune the network by using the loss calculated based on Gaussian EMD metric.
In the experiments, the authors used the pre-train model of Resnet-18 and the self-distillation, while the effect of the base model (the above two things) on the performance of the Meta-dataset is still vague. Please give descriptions of the comparison methods or mark in the tables, the difference between the comparison method and GEMD on the base model.
There are a few grammatical errors in the text that need to be fixed, such as "Wang et al. (2017) propose" and the following "Bilinear pooling (Lin et al., 2018) or covariance pooling (Wang et al., 2021; Song et al., 2023) yields" in p3， "in SDL setting we freeze the backbone networks that are used to…" in p7, etc.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a metric-based Gaussian Earth Mover's Distance (GEMD) for few-shot learning, which is computationally more efficient than the existing DeepEMD method. GEMD is implemented using transfer learning and a learnable metric, achieving superior performance compared to DeepEMD

### Strengths
The proposed GEMD method achieves compelling performance compared to state-of-the-art methods, as demonstrated through extensive experiments on large-scale Meta-Dataset and three small-scale benchmarks .

### Weaknesses
* Limited discussion on the limitations of GEMD: The paper does not provide a comprehensive discussion on the limitations of the proposed GEMD method. It would be beneficial to include a section discussing the potential drawbacks or scenarios where GEMD may not perform as well, providing insights for future research and potential improvements
* lack of visualization and analysis: The paper  does not provide any visualizations or in-depth analysis of the results. Including visualizations and further analysis of the learned features or matching flows would provide a deeper understanding of the proposed GEMD method and its effectiveness

### Questions
See weakness section for more details.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
