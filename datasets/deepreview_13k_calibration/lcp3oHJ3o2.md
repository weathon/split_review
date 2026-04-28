# Overcoming Domain Limitations in Open-vocabulary Segmentation

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 5, 6

## Abstract
Open-vocabulary segmentation (OVS) has gained attention for its ability to recognize a broader range of classes. However, OVS models show significant performance drops when applied to unseen domains beyond the \pretraining dataset. Fine-tuning these models on new datasets can improve performance, but often leads to the catastrophic forgetting of previously learned knowledge. To address this issue, we propose a method that allows OVS models to learn information from new domains while preserving prior knowledge. Our approach begins by evaluating the input sample's proximity to multiple domains, using precomputed multivariate normal distributions for each domain. Based on this prediction, we dynamically interpolate between the weights of the pre-trained decoder and the fine-tuned decoders. Extensive experiments demonstrate that this approach allows OVS models to adapt to new domains while maintaining performance on the \pretraining dataset.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
1

### Summary
The paper proposes to combine continual learning and open vocabulary image segmentation in order to improve the generalizability of the model. Its motivation is that this paper finds that finetuning and simply applying continual learning can degrade the performance on unseen new datasets and so proposes to use MVN distributions to adapt to new data. Specially, it saves the means and covariance matrices of the image and test embeddings for each seen dataset. When the new dataset arrives, just fit it to the distribution with an interpolation factor vector. The experiment is based on two popular models, fc-clip and X-Decoder, and shows improvement over the finetuning method.

### Strengths
The proposed method is easy to understand and looks like easy to implement.

The experiment and ablation study on fc-clip is sufficient.

### Weaknesses
The presentation is weak and the expression is not rigorous. For example, the definition of "domain" in this paper is unclear. The problem setting also needs more clarification. Some information details are missing.

Many necessary experiments are missing.

For the proposed method, significant effort is required to assess its soundness. For example, is it reasonable to construct an MVN distribution based on different datasets? for coco2014 and 2017, do we need to treat them to two distinct datasets?

For table, what does exactly domain mean? I think that is just cross dataset validation, not cross-domain. For different domains, that usually means images with different styles like DomainNet datasets or from synthetic images to real world images. And the comparison in table 1 is unfair. I think for Mask2Former, that is the fine-tuned number. And Since the architecture is also different from Mask2Former and X-Decoder and fc-clip. For a better comparison, why not training X-Decoder on Cityscapes and ADE20K, instead of using Mask2Former? Also for fc-clip.

Line 43, why do we need fine-tuning. these years, many models have been universal. They can be trained on different datasets jointly. In that case, we don’t need finetuning and therefore there is no catastrophic forgetting problem.

Line 54-55, which methods? Reference?

Line 57, needs to clarify, what does “Our method begins by fine-tuning the decoder” mean? For open-vocabulary setting, should we assume know the domain of the new dataset? If not, why can we fine-tune on it?

Figure 1 is unclear. What do “previous”, “fine-tuning”, “unseen” mean? Please use professional terms, source domain, target domain to clarify. From my understanding, I think previous is the source domain and unseen is the target domain, if so, what is fine-tuning? Also, the bar chart is for what model? At least should be pointed in somewhere in the experiment section.

Line 89, “Despite these advancements, current methods remain effective only within the domain of the previous training dataset and fail to generalize to new domains.”, please tone down the expression, if current methods fail to generalize to new domains. Why too many open-vocabulary segmentation works appeared. For example, OpenSeeD can work well on SeginW dataset that has multiple subsets of different domains (just use the word in this paper). Why it fails.

Line 123, again, for Figure 1, what is the model?

Line 134, “with each batch containing an equal proportion of data from both datasets.” Any reference? I don’t think it has to be equal proportion of data from both datasets. Sometimes the ratio depends on the quality of the mixed datasets.

Line 137, for the second issue “2) Whether the model is trained from scratch or fine-tuned on both datasets, joint training consistently results in lower performance compared to fine-tuning on the target dataset alone (see Figure 2).”. I can agree. It is unclear what the used model is. But here COCO to Cityscapes is just one specific example. If jointly training is better or worse than fine-tuning depends on the domain gap (still use the word in this paper, although I think use dataset gap is more accurate). For example, is the performance of jointly training on COCO and LVIS is better than that of finetuning on COCO?

For the third issue, why not using downsampling and upsampling to control that.

For the first issue, why it is challenging? Is it hard to just consume some storage to save some data? Any big difference from storing means and covariance matrices for each datasets in this paper?

Line 157, what does PEFT mean?

Can’t understand Figure 3 (b), what does “average inference time per sample” mean? Why the inference time varies according to the Number of seen datasets? What does “Number of seen datasets” mean here? Source datasets + newly arrived datasets?, shouldn’t the inference time only depends on the model, testing sample and device? What these three datasets are?

I think the problem definition is not open-vocabulary. For OV, the testing images and class is unknown, but in this paper, it allows sequential fine-tuning. So I think the paper is just a continual learning of segmentation.

For the algorithm 1, I don’t think it makes much sense to save means and covariance matrices for each datasets. If it makes sense? Why not doing that for each subgroups of these datasets? We can’t guarantee the domain gap of two images across datasets is certainly larger than two images inner the same dataset. So a more reasonable way is to cluster all seen data and proceed the algorithm for each cluster.

Overall, the MVN distribution is similar to those typical multi domain adaptation methods, For example, “Li, Yunsheng, Lu Yuan, Yinpeng Chen, Pei Wang, and Nuno Vasconcelos. "Dynamic transfer for multi-source domain adaptation." In CVPR.” In the sense that to compute an interpolation factor vector and like a linear combination of source domains in order to adapt to target domain. But anyway, I think in the section 2,  multi domain adaptation literature review is recommended.

For experiments, I think a critical baseline missing is jointly training on all previous and fine-tuning datasets.

Again, why not comparing to other OVS methods like ODISE, OpenSeeD, Open-vocabulary SAM, etc? The setting is easy, just use all previous and fine-tuning datasets to train their models and evaluate on these eight unseen datasets. Otherwise, the results shown like in tables 3, 4 make the reader hard to believe the proposed method work.

Another big problem is the experiments need cross validation, not just usually COCO as the previous training set. In real world, we could start with ADE, we could start with Cityscapes, or we could also start with a subset like 10K training samples of COCO. In these cases, does the proposed method still work well?

### Questions
For table, what does exactly domain mean? I think that is just cross dataset validation, not cross-domain. For different domains, that usually means images with different styles like DomainNet datasets or from synthetic images to real world images. And the comparison in table 1 is unfair. I think for Mask2Former, that is the fine-tuned number. And Since the architecture is also different from Mask2Former and X-Decoder and fc-clip. For a better comparison, why not training X-Decoder on Cityscapes and ADE20K, instead of using Mask2Former? Also for fc-clip.

Line 43, why do we need fine-tuning. these years, many models have been universal. They can be trained on different datasets jointly. In that case, we don’t need finetuning and therefore there is no catastrophic forgetting problem.

Line 54-55, which methods? Reference?

Line 57, needs to clarify, what does “Our method begins by fine-tuning the decoder” mean? For open-vocabulary setting, should we assume know the domain of the new dataset? If not, why can we fine-tune on it?

Figure 1 is unclear. What do “previous”, “fine-tuning”, “unseen” mean? Please use professional terms, source domain, target domain to clarify. From my understanding, I think previous is the source domain and unseen is the target domain, if so, what is fine-tuning? Also, the bar chart is for what model? At least should be pointed in somewhere in the experiment section.

Line 89, “Despite these advancements, current methods remain effective only within the domain of the previous training dataset and fail to generalize to new domains.”, please tone down the expression, if current methods fail to generalize to new domains. Why too many open-vocabulary segmentation works appeared. For example, OpenSeeD can work well on SeginW dataset that has multiple subsets of different domains (just use the word in this paper). Why it fails.

Line 123, again, for Figure 1, what is the model?

Line 134, “with each batch containing an equal proportion of data from both datasets.” Any reference? I don’t think it has to be equal proportion of data from both datasets. Sometimes the ratio depends on the quality of the mixed datasets.

Line 137, for the second issue “2) Whether the model is trained from scratch or fine-tuned on both datasets, joint training consistently results in lower performance compared to fine-tuning on the target dataset alone (see Figure 2).”. I can agree. It is unclear what the used model is. But here COCO to Cityscapes is just one specific example. If jointly training is better or worse than fine-tuning depends on the domain gap (still use the word in this paper, although I think use dataset gap is more accurate). For example, is the performance of jointly training on COCO and LVIS is better than that of finetuning on COCO? 

For the third issue, why not using downsampling and upsampling to control that.

For the first issue, why it is challenging? Is it hard to just consume some storage to save some data? Any big difference from storing means and covariance matrices for each datasets in this paper?

Line 157, what does PEFT mean?

Can’t understand Figure 3 (b), what does “average inference time per sample” mean? Why the inference time varies according to the Number of seen datasets? What does “Number of seen datasets” mean here? Source datasets + newly arrived datasets?, shouldn’t the inference time only depends on the model, testing sample and device? What these three datasets are?

I think the problem definition is not open-vocabulary. For OV, the testing images and class is unknown, but in this paper, it allows sequential fine-tuning. So I think the paper is just a continual learning of segmentation.

For the algorithm 1, I don’t think it makes much sense to save means and covariance matrices for each datasets. If it makes sense? Why not doing that for each subgroups of these datasets? We can’t guarantee the domain gap of two images across datasets is certainly larger than two images inner the same dataset. So a more reasonable way is to cluster all seen data and proceed the algorithm for each cluster. 

Overall, the MVN distribution is similar to those typical multi domain adaptation methods, For example, “Li, Yunsheng, Lu Yuan, Yinpeng Chen, Pei Wang, and Nuno Vasconcelos. "Dynamic transfer for multi-source domain adaptation." In CVPR.” In the sense that to compute an interpolation factor vector and like a linear combination of source domains in order to adapt to target domain. But anyway, I think in the section 2,  multi domain adaptation literature review is recommended.

For experiments, I think a critical baseline missing is jointly training on all previous and fine-tuning datasets.

Again, why not comparing to other OVS methods like ODISE, OpenSeeD, Open-vocabulary SAM, etc? The setting is easy, just use all previous and fine-tuning datasets to train their models and evaluate on these eight unseen datasets. Otherwise, the results shown like in tables 3, 4 make the reader hard to believe the proposed method work.

Another big problem is the experiments need cross validation, not just usually COCO as the previous training set. In real world, we could start with ADE, we could start with Cityscapes, or we could also start with a subset like 10K training samples of COCO. In these cases, does the proposed method still work well?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper addresses the domain limitations in Open-Vocabulary Segmentation models, which tend to perform poorly on unseen domains and suffer from catastrophic forgetting when fine-tuned on new datasets. This paper proposes to use precomputed multivariate normal distributions for domain representation and adjusts the model weights during inference, allowing the OVS models to adapt to new domains while retaining performance on previously trained datasets.

### Strengths
The method introduced in the paper enhances the adaptability of Open-Vocabulary Segmentation models to new domains without the need for retraining from scratch or accessing previous datasets during training. It effectively addresses the problem of catastrophic forgetting by maintaining consistent performance on previously trained datasets while adapting to new domains. Additionally, the method does not introduce additional parameters into the OVS model, allowing for seamless integration with existing architectures and ensuring computational efficiency.

### Weaknesses
The paper presents an innovative approach to handling domain limitations in Open-Vocabulary Segmentation (OVS) models, but there are several considerations that may impact its practical deployment:

Challenges in Implementation: This method involves calculating interpolation coefficients and blending multiple decoders into one during inference, which could require substantial computational resources. It might be complex to tune and stabilize, possibly complicating its use in real-world scenarios. Have there been any quantitative analyses that compare the computational demands (like time and operations) of this method against others during inference?


Use of Multiple Evaluation Metrics: Why do Tables 4 and 5 use a mix of mAP, PQ, and mIoU metrics for evaluation? Understanding the rationale behind choosing these diverse metrics could help clarify their relevance to the goals of the study.

Managing Computational Costs: Are there existing methods or technologies that could be adapted to help reduce the computational costs associated with this method? Exploring how similar challenges have been addressed in other contexts might provide viable solutions to enhance the efficiency of this approach.

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper addresses the issue of forgetting during the fine-tuning process for models on the open vocabulary task by proposing a weight interpolation method based on domain similarity, dynamically determining model parameters for each sample during testing.

### Strengths
1. The paper presents a clear and easily understandable approach.
2. Experiments have been conducted on multiple datasets and tasks.

### Weaknesses
1. The method proposed in the paper is designed for the open vocabulary task, but some of the experiments in the introduction and ablation sections are based on results on fine-tuning close-vocabulary datasets which lacks persuasiveness.

2. The most important evaluation criterion for the open vocabulary task is performance on unseen data, rather than seen data. The model's performance on unseen ADE and Cityscapes datasets shows no significant advantage over the original FC-CLIP, and in some metrics, it even declines.

3. The method is simply an ensemble of weights, which is too straightforward and lacks significant insight.

4. The requirement to save model parameters for each dataset places a high demand on storage.

5. The unseen dataset contains both unseen and seen categories. The performance improvement of the method on unseen data compared to FC-CLIP is likely due to the seen categories, as the capability for unseen categories largely depends on the original CLIP. This is evident from Figure 8, where the original FC-CLIP is already able to segment the unseen category "ceiling." Therefore, the method does not seem to have a significant impact on the open vocabulary task.

### Questions
1. It is hard to say the method is specifically designed for the open-vocabulary task. In other words, can the proposed method also be applied to traditional continual learning tasks?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper addresses the challenge of open-vocabulary segmentation (OVS) models experiencing significant performance drops when applied to unseen domains. The authors propose a method to enable OVS models to learn from new domains while retaining previously acquired knowledge, thereby mitigating catastrophic forgetting.

### Strengths
1. The paper effectively addresses the limitation of open-vocabulary segmentation (OVS) models: their poor performance on unseen domains.

2. The method's effectiveness is validated across a diverse range of datasets, showing its robustness and generalizability.

### Weaknesses
1. While the proposed method is tested on several datasets, the diversity of domains used in the experiments might still be limited. More extensive testing on a wider range of domains, including those with significant differences from the training data, e.g. GTA5, Night Scenes. This would provide a more comprehensive evaluation of the method's robustness.

2. The use of multivariate normal distributions (MVNs) to measure domain proximity adds complexity to the inference process. The computational overhead and potential latency introduced by this step should be thoroughly analyzed and discussed, especially for real-time applications.

3. The paper does not provide a detailed analysis of how sensitive the proposed method is to hyperparameters, such as the interpolation factors and the parameters of the MVNs.

### Questions
Please refer to Weakness

### Soundness
3

### Presentation
3

### Contribution
2
