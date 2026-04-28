# Synergy and Diversity in CLIP: Enhancing Performance Through Adaptive Backbone Ensembling

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 8, 6

## Abstract
Contrastive Language-Image Pretraining (CLIP) stands out as a prominent method for image representation learning. Various architectures, from vision transformers~(ViTs) to convolutional networks (ResNets) have been trained with CLIP to serve as general solutions to diverse vision tasks.
This paper explores the differences across various CLIP-trained vision backbones.
Despite using the same data and training objective, we find that these architectures have notably different representations,
different classification performance across datasets, and different robustness properties to certain types of image perturbations.
Our findings indicate a remarkable possible synergy across backbones
by leveraging their respective strengths.
In principle, classification accuracy could be improved by over 40 percentage with an informed selection of the optimal backbone per test example. 
Using this insight, we develop a straightforward yet powerful approach to adaptively ensemble multiple backbones.
The approach uses as few as one labeled example per class
to tune the adaptive combination of backbones.
On a large collection of datasets, the method achieves a remarkable increase in accuracy of up to 39.1\% over the best single backbone, well beyond traditional ensembles.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper starts with the finding that existing CLIP models show diverse behaviours (error distributions) on classification tasks, even if they are pre-trained on the same dataset (WIT-400M). This indicates potential for model ensembling. The authors then propose a learnable ensemble module that adjusts the logits of each model with a learned temperature value conditioned on the input image, and sums up the logits of all models for the final prediction. This can also be combined with an existing cascade strategy for better efficiency. Experiments show consistent improvements over the best single backbones.

### Strengths
- This paper presents a finding that the logits of CLIP models are very diverse, and the more diverse their logits are, the higher performance can be reached by their ensemble.
- This paper presents a comprehensive study on the diversity and properties of CLIP's logits and possible factors behind them.
- The results produced by the ensemble model are considerably higher than single models. When compared with other ensemble methods, there is also some improvement.
- The paper is clearly written and is easy to understand.

### Weaknesses
 - The setting of training the ensemble module might harm generalizability and more clarifications are needed. It requires training data for each class regarding which model is better for each evaluation dataset, which is ad-hoc and remains questionable whether it harms CLIP's ability to generalize to unseen classes, concepts, or compositions.
- It is not very surprising that more diverse models enable better ensembles, especially when the oracle model is picked per-sample, this adds a lot of flexibility compared to ensembling without data conditions.
- The method itself is related to one prior method (Super Learner), and the main improvement is adding image conditions. But when compared with SL, the performance improvement is not big.
- From a practical viewpoint, how much additional inference-time computation is required? I see the results of FLOPS, and it would be better also to report GPU memory and inference time. The reported inference time is considerable compared to single backbones (5x~34x). This raises concerns about the practical applicability of the method, especially given that the performance gains over SuperLearner are not substantial.

More detailed classifications are elaborated in the questions section.

### Questions
1.1: How is the training data for the ensemble module curated and how is it split from other data? Please provide more details.

1.2: When the training data for the ensemble module is only available in some classes, does it generalize well to novel classes? Also, when training with only some fixed prompts, does it overfit these prompts?

1.3: Continue to 1.2, considering more complex concepts (eg, [ARO](https://github.com/mertyg/vision-language-models-are-bows) or [SugarCrepe](https://arxiv.org/abs/2306.14610) datasets), can the ensemble module correctly rerank CLIP models on novel compositions of concepts?

2.1: When trained on the same dataset, different backbones in the same series (eg, R-50/101/50x4, ViT-S/B/L) make different mistakes. Does this finding only apply to CLIP or also apply to other methods (eg, vanilla supervised learning)?

2.2: Is diversity always preferred when selecting models in a per-sample way, no matter whether using CLIP or not?

3.1: When inferencing with the proposed method over a dataset, does the user need to load all CLIP models to the device? How much memory is needed compared to using single models, and how much inference time is needed?

3.2: Can the authors also provide a comparison in computation and time cost with other ensemble methods (eg, SL, MoE)?

Minor: L815: OpenCLIP is a project developed by LAION. The models mainly considered in this paper are trained by OpenAI, and the corresponding dataset is called WIT-400M.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focuses on vision-language backbones, especially two-tower CLIP like network structure. It evaluates the classification tasks across several datasets. The main idea is to propose an ensemble strategy in logic space by adaptively learning the temperature across different versions of pretrained CLIP backbones. Empirical results are based on a large group of image classification datasets. It also provides detailed analysis for a better intuition.

### Strengths
1. Training large-scale backbone requires high computational cost. Therefore, thinking about how to combine existing pretrained backbones is a valuable research topic. Ensemble is a reasonable way to do so.
2. Empirical results are extensive for image classification task including several datasets.
3. Instead of making ensemble directly on logit from different backbone versions, it proposes a learnable module based on temperature scaling.
4. Overall, the paper writing is in a good shape and easy to follow.

### Weaknesses
1. More evaluation tasks are valuable to be considered to further support the paper statement. Even if limited with CLIP backbone, adding more retrieval tasks will be supportive.
2. Ensemble on logit is still relatively not novel enough as a research work. Compared with previous ensemble, it still relies on the output of each individual model and make the late fusion.
3. Such ensemble increases the performance but requires much more test time, and it also requires to conduct a post-learning process. The overall pipeline is not that straightforward.
4. It looks like the proposed pipeline cannot obtain improvement by adding more training shots, more analysis and intuition will be helpful.

### Questions
Please refer to the weaknesses section above.

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
4

### Summary
This work investigates the differences across various CLIP-trained vision backbones with respect to classification performance and robustness, and proposes an adaptive combination of pretrained CLIP backbones, which is able to increase performance beyond regular enabling.

I very much appreciate the author's systematic approach: they first show that there exist (large) differences between (zero-shot) classification performance of individual CLIP-trained vision backbones. Then they drive an oracle performance upper-bound and investigate  complementarity of different backbones concluding that different backbones classify different subsets of images differently. This motivates the authors to propose an adaptive ensembling approach called Neural Logit Controller (NLC) to combine individual backbones to one prediction.

The proposed NLC is based on network calibration using learned temperature scaling. To do so, the method needs to be informed by a supervised signal given by a single labeled example per class, as the authors claim.

Experimental results on a large collection of datasets show that the proposed approach is able to outperform state-of-the-art few-shot methods. For some datasets by large (up to 39.1), on average by 9.1% over the best performing individual backbone and better than baseline ensembling methods. However, outperformance is much smaller when data-specific linear heads are trained (=1.6%). Additional results show a promising combination of Tip-Adapter with the proposed approach.

As mentioned before, I very much appreciate the systematic evaluation of the growing number of available vision foundation models. Having so many foundation models available, renders the question how *foundational* these models are. So maybe the research community should invest more time in the investigation and how to harness these foundation models. To do so, we would need to understand their differences, strengths and weaknesses and then derive from that propose a novel aggregation, ensembling or merging methods. ...and this is what this paper is doing.

I also very much appreciate the large number of experiments and evaluations done by the authors to support this work - including the additional results in the appendix. One is just one thing, looking at the results and in particular the difference in performance between Fig. 8. and Fig. 9. I might be wrong but can the decrease of outperformance from 9.1% to 1.6% be linked to the additional supervision signal intrinsic to the proposed NLC method? Is this what we see here? And if yes, could the results in Fig. 8 be biased towards the supervision part of NLC? I will raise it again in the question section.


----------------------reply to rebuttal----------------------


I would like the authors for the information provided in the rebuttal. I went through the paper again and look in particular at the appendix and other reviewer / author discussions and given that I would like to increase my rating for this submission. I think this work contributes to the research community with its detailed evaluation and proposed ideas.

### Strengths
- **(S1)**: this paper presents an in-depth analysis of different CLIP-trained vision backbones with respect to different dimensions such as few-shot image classification, complementarity, robustness, and diversity.

- **(S2)**: this paper proposes a novel method to combine the strengths and weaknesses of available CLIP-trained vision backbones able to outperform regular ensembling methods on a large amount of datasets.

- **(S3)**: this paper is easy to read and follow given the systematic build-up of the paper.

### Weaknesses
 - **(W1)**: Maybe the large out-performance of the proposed method from Fig.7 is linked to the injection of a supervised signal and therefore the comparison against regular ensembles might be biased. I have raised this in **(Q1)**.

- **(W2)**: I would love to see more details about the injection of the supervision signal given the one labeled example per class. I am not sure if this is what I can find in appendix G and Table G.1?

- **(W3)**: not really a weakness but some minor things:
- - page 3, line 134: train a pair of vision and text encoders φ_l and φ_v <- I think the first is the language and the second is the vision encoder.
  - Fig 4: it is not clear which setup corresponds to the dashed lines.

### Questions
- **(Q1)**: As mentioned above, here is the question raised earlier: looking at the results and in particular the difference in performance between Fig. 8. and Fig. 9. I might be wrong but can the decrease of outperformance from 9.1% to 1.6% be linked to the additional supervision signal intrinsic to the proposed NLC method? Is this what we see here? And if yes, could the results in Fig. 8 be biased?

- **(Q2)**: why is the MoE missing in Fig.8? I assume that the linear heads from the experiment of Fig.9 are serving as MoE?

- **(Q3)**: on page 6, lines 298, with one-layer MLP, do you mean a MLP with one hidden layer?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper analyzes the prediction diversity for CLIP models from OpenCLIP by analyzing the overlap between the sets of correctly predicted images from the test set of ImageNet1k via zero-shot classification. The paper finds that model size increases accuracy, but there exist images that are correctly predicted by smaller models (within same family as well). To combine the models, the paper proposes a method to combine logits of different backbones by scaling the logits using a learned temperature value per backbone. Temperature scaling is implemented usign a neural network called Neural Logit Controller (NLC) which takes the concatenated features of all the backbones and predicts the temperature. NLC is trained using a standard cross-entropy objective, and can be trained using only one image per class. The method boosts the zero-shot and linear probing performance on a number of downstream tasks, and the performance boost correlates with prediction diversity.

### Strengths
1. The paper shows that smaller models have certain samples that they can predict correctly, and larger models can give incorrect predictions on these samples. This is an interesting observation, and highlights the need for careful thought when scaling models.

2. The proposed NLC is simple but effective, and can be trained in a data-efficient manner as demonstrated in Section 4.2 and 4.3.

### Weaknesses
1. The authors claim on line 200 that the results are non-obvious is not entirely true. Prior work has shown similar results across vision and language domains, albeit on different models [1, 2, 3]. [1] have shown prediction diversity on a range of models trained in a supervised setting and propose a method for combining models using distillation. They show that weaker models are more specialized in certain subsets of data. While the metric for measuring diversity is different, they study the same core problem. [2] show that finetuning models on different domains and then averaging model weights can improve out-of-distribution performance (this assumes the same model size, but studies a similar problem of different models being good at different subsets of data).

2. **Incomplete comparisons in few-shot experiments (Section 4.3)**:
- The results in Section 4.3 (Comparison with Few-Shot Adapter Methods) are incomplete: Figure 10 and Table 1, which show the zero-shot performance of TiP-Adapter applied to individial backbones and NLC does not show the complete picture - since NLC is an ensemble method, a proper comparison would be other ensemble methods. Similar is the case when NLC is combined with Tip-Adapter. In principle, any ensemble method can be combined with Tip-Adapter, so a proper comparison would be with other ensemble methods applied in a similar manner as NLC. Without these results, the comparisons are incomplete. 

3. **Number of training samples**:
- Point 2 is especially more important considering that few-shot experiments in Section 4.3 are the only experiments which demonstrate the data efficiency of NLC, which is claimed to be a major contribution by the authors. From Section 4.1: "The non-parametric ones are “static” while the parametric ones use the training split of each target dataset to adjust the ensemble adaptively." implies that NLC uses the entire training set for calibration. For few-shot experiments, if this data efficiency is applicable to other ensemble methods as well, this cannot be attributed to NLC, but would be a general property of ensemble methods.
- From linear probing experiments in Section 4.2, Figure 9 shows that with a similar training budget, NLC does not provide a significant improvement over Super Learner (SL). Mean increase of 1.6 is the same, and SL also does not lead to any degradation over the single best model. The max increase seems to be a noisy metric to track, since MoE can show a maximum 20.8 increase but also shows degradation, indicating the max increase is really dataset specific.

4. The paper claims that the method can be combined with Cascade, but does not provide the trainiing details. The paper also does not compare the performance of the proposed method with the original Cascade method. Minor: The paper also misses a citation for a cascade method [4].

5. Although the paper mentions this in the limitations, fusing models at training stage has been done in [1] in supervised classification settings, hence the additional inference overhead of NLC is a major practical limitation. Furthermore, while the paper shows the potential for applying the method to other tasks like image retrieval, the paper does not actually study this using NLC, making the impact of the method limited.

### Questions
1. What is the standard deviation of the accuracy when using different subsets of data for training the methods in few-shot setting? This is important to understand the robustness of the method when using different training samples.

### Soundness
3

### Presentation
3

### Contribution
2
