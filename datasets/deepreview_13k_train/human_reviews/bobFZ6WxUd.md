# Non-Autoregressive Machine Translation as Constrained HMM

- Decision: Reject
- Scores: 3, 5, 8

## Abstract
In non-autoregressive translation (NAT), directed acyclic Transformers (DAT) have demonstrated their ability to achieve comparable performance to the autoregressive Transformers.
In this paper, we first show that DAT is essentially a fully connected left-to-right Hidden Markov Model (HMM), with the source and target sequences being observations and the token positions being latent states.
Even though generative models like HMM do not suffer from label bias in traditional task settings (e.g., sequence labeling), we argue here that the left-to-right HMM in NAT may still encounter this issue due to the missing observations at the inference stage.
To combat label bias, we propose two constrained HMMs: 1) Adaptive Window HMM, which explicitly balances the number of outgoing transitions at different states; 2) Bi-directional HMM, i.e., a combination of left-to-right and right-to-left HMMs, whose uni-directional components can implicitly regularize each other's biases via shared parameters.
Experimental results on WMT'14 En$\leftrightarrow$De and WMT'17 Zh$\leftrightarrow$En demonstrate that our methods can achieve better or comparable performance to the original DAT using various decoding methods.
We also demonstrate that our methods effectively reduce the impact of label bias. Code is available in the supplementary materials.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The presented work extends the understanding of DAT as a left-ro-right Hidden Markov Model and proposes two approaches to mitigate the inherent label bias problem, namely an Adaptive Window HMM and a combination with a right-to-left HMM.

### Strengths
- Extends the understanding of DAT as a HMM and solves the label bias problem by incorporating an R2L HMM and adding a hyper parameter to balance the outgoing transitions. 
- Experiments to back up the claim that the label bias problem is mitigated using the proposed approach.
- NAT papers should follow the broader machine translation standard to report multiple metrics and metrics that correlate better with human judgement besides only relying on tokenized BLEU as that doesn't show the full picture, see **[1]**, **[2]**, **[3]**. I'm glad to see that BLEURT was additionally reported in the presented work and we do see nice gains there as well.

### Weaknesses
### Weaknesses

- **[major]**: Despite WMT'14 and WMT'17 being commonly used in the NAT literature, they are now way overhauled in the broader machine translation literature and should be replaced by more recent test sets to put the results into the context of recent research, see **[1]**. The continued use of these older datasets makes it difficult to assess the true progress of the proposed method against current state-of-the-art techniques. Specifically, the field has moved towards more challenging and diverse datasets that better reflect real-world translation scenarios, and the lack of evaluation on these datasets limits the impact of the presented work.
- **[major]**: NAT papers should follow the broader machine translation standard to report their evaluation scores using `sacrebleu` and provide the corresponding hash that was used for generating the scores. This will ensure that scores are reproducible and do not vary across papers by up to 1.8 BLEU points due to varying tokenization and normalization, see **[2]**, **[4]**. Mixing `sacrebleu` and tokenized BLEU as done in Table 1 shouldn't be done and needs to be fixed. The inconsistent reporting makes it hard to compare the results with other methods in a reliable manner. Furthermore, the absence of the `sacrebleu` hash makes it impossible to verify the reported scores, which is a critical requirement for scientific reproducibility.
- **[major]**: While it is nice to see that the paper attempts to provide GPU benchmarking numbers, the speed multipliers are heavily inflated since the baseline is a non-optimized autoregressive Transformer. There are many de-facto standard ways in practice to construct are more competitive autoregressive inference speed baseline with negligible translation quality drop using e.g. shallow decoders, shortlisting, or quantization (see **[2]**, **[5]**, **[6]**) which should be adopted here. The current comparison does not reflect the true potential of autoregressive models and thus overstates the speedup achieved by the proposed non-autoregressive method. A fair comparison requires using optimized baselines that are representative of the current state-of-the-art in autoregressive inference.
- **[major]**: Table 1 doesn't include parameter counts or inference speed numbers which makes it hard to compare the different approaches and understand if the improvement comes from the better algorithm or, simply, the increased parameter count capacity. For example, Bi-HMM uses two different parameter sets to model L2R and R2L and as a result they should have more parameters. Bigger baselines, potentially in parallel branches through e.g. MoE, or scaling up previous approaches might be needed. Without this information, it is impossible to determine whether the observed improvements are due to the proposed method or simply due to increased model capacity.
- **[minor]**: It is unclear how well the proposed approach extends to the multilingual setting. The paper does not provide any analysis or experiments on multilingual datasets, which limits the generalizability of the findings. It is important to investigate how the proposed method performs in scenarios where multiple languages are involved, as this is a common requirement in real-world applications.
- **[minor]**: Figure 4 doesn't show a clear trend in the window size, making it hard to extrapolate the findings to other language pairs or datasets without additional analysis for the dataset at hand. This will require additional grid search tuning trials to adopt and no guidance on how to tune this parameter is given. The lack of a clear trend makes it difficult to understand the impact of the window size on the performance of the proposed method and limits its practical applicability.

### Questions
- How were the hyperparameters tuned for the proposed method and the previous works? If defaults were used for previous methods, the comparison needs to potentially be adjusted to also allow hyper parameter tuning for those methods.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Based on the directed acyclic Transformers (DAT) for non-autoregressive translation (NAT), this paper first shows that NAT is a fully connected left-to-right Hidden Markov Model (HMM) model. Then, the authors propose two constrained HMM strategies to address label bias issues in DAT, including adaptive window HMM and bidirectional HMM. The former adaptively balances the number of outgoing transitions at different latent states. And the latter uses bidirectional components to regularize each other's label bias.

The experiments are conducted on WMT14 en-de and WMT17 zh-en. Results demonstrate that both proposed strategies can obtain comparable or better performance compared to previous DAT models, and reduce the influence label bias.

### Strengths
1. The paper proposes two methods, namely adaptive window HMM and bidirectional HMM to alleviate the challenges of label bias.

2. Experimental results and analysis demonstrate the effectiveness of the proposed methods, which can achieve comparable or better BLUE scores than the original DAT models, and mitigate the effect of label bias.

### Weaknesses
Compared to original DAT methods, the proposed strategies are incremental innovation, and only achieve improvements on the part of translation directions. For example, it does not seem to work for WMT zh-en, the reasons also need explaining.

### Questions
1. Can the proposed two strategies be applied to the DAT model at the same time?

2. Why does the proposed method behave differently in different translation directions?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes that DAT can be considered a special case of HMM, and then utilizes this perspective to identify that DAT exits the label bias problem. To address this problem, the authors present two solutions, namely 1) adaptive window HMM and 2) bi-directional HMM. Experimental results on WMT'14 English to German and WMT'17 Chinese to English demonstrate that our methods can achieve better or comparable performance to the original DAT.

### Strengths
1) Viewing DAT as a variant of HMM is correct and very helpful. As a broader and high-level perspective, HMM can provide more opportunities for improving NAT (DAT).
2) Label bias is indeed an issue with DAT, and the two solutions proposed by the authors are simple but effective. The intuition behind them is also easy to understand.
3) The experiments are very thorough, verifying not only the improvement in performance but also analyzing whether the label bias issue has been resolved in the analysis section.
4) This paper is clear and easy-to-follow.

### Weaknesses
I cannot point obvious shortcomings, but if pressed, I would argue that label bias is not the most critical issue within DAT. In other words, this paper is not a game changer for NAT. From the experiments, it appears that addressing label bias offers only limited enhancement to DAT's performance. However, this cannot be considered a very strong point of criticism, as I think the authors' perspective of viewing DAT through the lens of HMM to be very useful and improtant.

### Questions
I've also entertained the idea of viewing DAT as an HMM and have conducted some preliminary experiments. For instance, I removed the lower triangular mask matrix in DAT, transforming the model into a globally normalized general HMM. However, the model did not converge. If you could contrast this unsuccessful method in your paper, we might gain a deeper understanding of HMM-DAT.

Additionally, in DAT experiments, glancing training significantly aids DAT. Do you think this training method can be generalized to all HMM algorithms, such as those used in speech recognition, etc.?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
