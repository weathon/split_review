# CLIP model is an Efficient Online Continual Learner

- Decision: Reject
- Scores: 5, 3, 3, 5, 3

## Abstract
Online continual learning addresses the challenge of learning from continuous, non-stationary data streams. Existing online continual learning frameworks are classification-based and assume a pre-defined number of classes. In this study, we propose that vision-language models (VLMs) are more suitable candidates for online continual learning. Compared to traditional classification-based frameworks, VLM such as CLIP model is not limited by the maximum number of classes or constrained by rigid model architectures, enabling it to generalize across both known and emerging classes. However, we find that naively tuning the CLIP for online continual learning results in asymmetric image-text matching. This asymmetric matching will consistently poses negative suppression on the previously learned classes, leading to catestrophic forgetting. To address this issue, we propose a simple yet effective method, the symmetric image-text (SIT) tuning strategy, which mitigates the adverse impact of negative samples by excluding asymmetric text during online learning. Additionally, we introduce a more challenging online continual learning setting with blurred boundary, namely MiD-Blurry, which mixes multiple data distributions to simulate real-world scenarios. We conduct extensive experiments on several continual learning benchmarks as well as the MiD-Blurry setting, evaluating both inference-at-any-time performance and generalization to future data. Our results demonstrate that the SIT strategy effectively preserves memory stability while maintaining learning plasticity.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper describes a more practical online continual learning (CL) setting where at each batch there exists disjoint classes from prior batches, overlapping classes to prior classes whose probability of appearance in the current batch following a gaussian density distribution, and decay classes that got introduced at a batch which gets reduced over time. The paper also presents a loss modification to remove contributions of negative contrastive sample of old class names and new class images in the current batch and showed that this modification leads to improved online CL accuracy.

### Strengths
The paper is well organized and easy to follow. The authors have presented results comparing to many prior arts over their proposed online CL setting. In the online CL accuracy benchmark testing accuracy over the classes seen at any given point of the learning process, the proposed loss modification introduces overall better accuracy. The gain is quite significant (10pps) compared to the baseline loss of AIT-CLIP.

### Weaknesses
There is a lack of insights to why removing the asymmetric contrastive samples help reduce bias towards new classes seen in a batch. This conclusion seemed to be purely empirical from the experimentation results.

Lack of validation of proposed loss modification across other settings besides the proposed setting. It is unclear if the proposed loss modification can be applied to other online CL settings too to get similar boosts.

In addition, one concern regarding using CLIP for CL, especially in closed-set classification testing (over classes seen at a given time), is that how to ensure that there is no leakage of class information in the pretraining stage of CLIP, e.g. if the class names do appear in the CLIP pretraining stage then it's not strictly CL anymore.

Zero-shot performance degradation compared to prior methods. In table 2, it shows that after online CL over a finegrained data-set, the performance of proposed loss in comparison to other baselines is worse in zero-shot classification accuracy over other concept-disjoint finegrained datasets. There is no insights given to this and it also raises the question on the robustness and generalizability of the proposed loss function.

Also, the author claimed that the proposed online CL method is dedicated for open-world scenarios. However, only the VLM-based methods are shown in an actual open-world scenarios where test-time classes are completely disjoint to those in all stages of the CL learning process. The authors should also compare with other non VLM-methods in an open-world setting, e.g, open-set recognition testing image retrieval accuracy over unseen classes as in [1].

### Questions
The generalization of the proposed loss modification. Is the loss modification only an artifact for the proposed setting specifically or is it an improvement that can be generally applied across? Having clarity on this will help strengthen the generalizability of the proposed loss update.

The paper should discuss the relationship of its loss formulation against loss functions that adjust sample weights based on loss values / logits such as Focal loss. 

Equation (3) numerator should be Z_S for L_A component? 

Other questions are listed in the weakness section.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper considers the online continual learning setting. The authors propose using vision-language models to facilitate the continual learning process. In the context of online continual learning, the authors find that naively tuning CLIP with texts of all previous non-matching classes as negative samples leads to sub-optimal results and propose using symmetric image-text (SIT) tuning strategy to fine tune the model at each time step. Empirical results verify the effectiveness of proposed method.

### Strengths
- The idea is simple and easy to understand.

- The empirical results are good.

### Weaknesses
 - I find this paper hard to follow. Firstly, the descriptions from Line 177-202 confuse me a lot. I cannot understand in online continual learning, what is the difference between task and time step? In Gaussian distribution, the probability distribution given by the authors is not conditioned on $t\ge \tau$, which means a sample can emerge at any time step. If I don't misunderstand this, what does a task actually mean? Does the batches within certain time steps of a task share something? In MiD-Blurry, the distribution is conditioned on $t\ge \tau$. So I feel quite confused about the relationship between a task and a time step in online continual learning setting. Besides, how to plot the figure 1?

- The method is simple but not surprising to me. For $T_a$, as samples in current batch don't belong to any of the classes defined in $T_a$, the similarity between samples and the $T_a$ will be over-suppressed at current step, which is not expected. But simply removing it from Eq. (2) (what the authors do) is also not a good choice, in my opinion. 

  Still, I find it not easy to figure out what the Fig. 3 actually means. The authors should make this part clearer. 

- Typos: in Eq. (3), $\log Z_A/(Z_S + Z_A)$ should be $\log Z_S/(Z_S+Z_A)$.

- Some baselines are missing. For example, [A] is also a continual learning method based on CLIP. The authors should compare and discuss it.

  [A] AttriCLIP: a non-incremental learner for incremental learning, CVPR 2022.

### Questions
The main questions about the details of this paper are listed is the weakness part.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The task is to perform online continual learning on CLIP models. The key idea of this paper is to create LoRA learnable weights to learn the training data and apply image-text contrastive pretraining loss only within the current batch. The paper also mentioned that including past classes as negatives could lead to larger gradient norms and catastrophic forgetting. The paper conducted various experiments to show the effectiveness of the method.

### Strengths
1. The idea is simple. 

2. The method achieves generally the best results among different compared results.

3. The analysis including gradient norm and PCA visualization are nice and intuitive.

### Weaknesses
1. Key references are missing. [1] and [2] also deal with continual learning using CLIP and especially [2] supports an online learning setting. The paper should compare closely to these two works.

2. For online training, training and inference efficiency are also important metrics. The paper leverages PEFT which is good in terms of the number of trainable parameters but it remains unknown how efficient the method is in terms of training and inference. In particular, the method claims to be efficient but without having these measurements, it is hard to tell whether the claim is well justified. 

3. The proposed method is essentially a CE loss defined on the labels of the existing batch, making the overall technical novelty low. This should be the first thing to try when finetuning CLIP on image classification tasks, whereas the abandoned AIT might be something not intuitive in the first place.

4. The problem of the larger norms for older classes is usually depicted as the recency bias issue. This is not a new topic, and several papers under the class incremental learning category proposed various solutions [3] [4]. This problem occurs usually due to over sampling. In the case presented in the paper, it might be the case that old classes are taken as negatives for all future samples. Therefore, the cure could be as simple as reducing oversampling and the method proposed in the paper is a variation of this methodology.

5. The paper still performs training on only a few small datasets. From the main paper, the largest training scope is presented in Tab. 2, which includes CUB200, StanfordCars and Aircraft. This is not sufficient to test the method’s scalability and robustness. Experiments on a much larger scale of training datasets are needed.

6. Details for how the plots are created in Fig. 3, 4 and 5 are missing. These details can be supplemented.

### Questions
What are the number of features used for text and images in Fig. 4 and 5?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper focuses on online continual learning, which addresses the challenge of learning from continuous, non-stationary data streams. Leveraging CLIP's open-world classification ability, online continual learning frameworks enable a flexible learning process without the constraint of class labels. To further improve the ability of CLIP in online continual learning without being affected by the catastrophic forgetting problem brought by finetuning, this paper proposes the symmetric image-text (SIT) strategy by removing asymmetric negative texts in online learning. In addition, this paper also introduces a challenging online continual learning setting named MiD-Blurry, which mixes multiple training data distributions to simulate real-world scenarios better. Results on multiple image classification datasets show that the proposed method performs preferably against previous state-of-the-art methods with minimal trainable parameters under both the Si-Blurry setting and the proposed MiD-Blurry setting.

### Strengths
1. The paper analyzes the problem of catastrophic forgetting during parameter efficient fine-tuning (PEFT) by dividing negative text samples into two parts: symmetric negative sample (SNS), negative text features corresponding to the classes of the images in the current batch, and asymmetric negative sample (ANS), negative text features corresponding to the classes of the images that not in the current batch. The gradient norm visualization directly shows the cause of catastrophic forgetting and the reason for the efficiency of the proposed method, SIT. This analysis is straightforward and convincing.

2. The proposed MiD-Blurry setting simulates the real-world scenario in which the classes suddenly appear and gradually fade away. The setting aligns with the basic idea of online open-world continual learning.

3. The selected datasets for evaluation are comprehensive and diverse, especially for evaluating zero-shot performance after online continual learning.

### Weaknesses
1. Figures:

Figure 1 right cannot really show the idea of SIT. I found the direction of the arrows confusing. 

In Figure 4, the representation is hard to see clearly and follow.

2. Method:

The overall method is straightforward. However, I think removing the contrastive learning between current images and the negative samples of classes on other batches/datasets is against the idea of online continual learning in the open-world setting. SIT can give you good performance when you evaluate on each dataset. However, this training manner cannot help you distinguish the positive images and negative texts across different datasets. This is important in open-world classification, a good property of using CLIP.

This shortage can also be seen in the experiment results. After online learning on some general datasets, the zero-shot performance on Food 101 drops a lot. This is because compared to other fine-grained datasets, Food 101 shares more common images/classes with general datasets like ImageNet and Caltech 101, so the SIT training strategy will affect the performance of Food 101. However, it's good that the authors include the Food 101 dataset in the comparison rather than drop it because of the inferior performance.

### Questions
For the evaluation of zero-shot performance on fine-grained datasets, what if you add all previously learned classes on general datasets into the text labels for classification? I assume due to the lack of training between image samples and text samples from other batches, the fine-tuned CLIP model will lose some ability for open-world classification, i.e., the ability to distinguish images from labels of other datasets. A similar evaluation setting can be found in these two papers:

Continual Learning in Open-vocabulary Classification with Complementary Memory Systems. TMLR 2024

Anytime Continual Learning for Open Vocabulary Classification. ECCV 2024

Which could also be baselines to evaluate against.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper shows the performance of CLIP in Online Continual Learning under parameter-efficient adaptations. A regularization method for mitigating the bias toward asymmetric examples is also discussed. The proposed method was tested on popular Continual Learning with the aid of a novel setup that simulates the distribution of non-stationary data streams in a more challenging way compared to previous methods, called MiD-Blurry. The proposed model is tested against the proposed benchmark and compared with both CLIP-based methods and standard classification models used in class-incremental learning.

### Strengths
The authors make an effort to identify some flaws in the base CLIP behavior when facing online continual learning data streams, by performing a gradient-based analysis to detect a systematic bias toward newer classes in the training phase. Furthermore, the authors understood the limitations of current benchmarks for evaluating performance under Online CL circumstances and introduced a setup to handle data streams by providing an additional challenge focused on non-stationarity. Understanding the limitations of current benchmarks is a crucial point, especially in Online CL, where real-case applications require facing complex dynamic environments.

### Weaknesses
Although the proposed method successfully challenges some intrinsic flaws of contrastive learning pre-training methods by introducing the SIT strategy, I don't feel like it is a relevant innovation. Regularizing the loss by adjusting for asymmetric examples has been already accounted for (see Manco et al (2022) - Contrastive Audio-Language Learning for Music, and Zolfaghari et al (2021) - CrossCLR Cross-modal Contrastive Learning for Multi-modal Video Representations).

A similar issue is raised for the parameter-efficient adaptation of CLIP. I think nowadays, prompt-, prefix-, and adapters-based fine-tuning are no longer a relevant design choice. Several models can benefit from these adaptations in the context of vision-language modeling (e.g. Flava, BEiT3), and the authors don't provide any insight into why CLIP was selected in place of other multimodal models leveraging contrastive pre-training.

Despite the effort to mitigate the lack of complexity of current CL benchmarks, the proposed MiD-Blurry still deals with standard continual learning datasets, which present non-complex data with high semantic correlation In general, don't see any additional challenge other than the one added by the proper online CL criteria. These datasets can't resemble real-case scenarios where the online CL setting should be first employed. From a benchmarking perspective, methods like DualPrompt that show amazing performance on the standard CL benchmark can under-perform under the circumstances of online CL likely due to the lack of a proper hyper-parameter tuning or learning pace of the prompts. I think a more suitable benchmark for online CL is needed, and the proposed setup might be not that relevant for facing the issue of the lack of a proper benchmark.

In line 138 the authors claim that the main limitation of mentioned CL methods is that they are closed-ended since they handle a pre-defined classifier dimension. This is not true, since in practice it's easy to use an incremental classifier that adds new heads following the same CL adaptation of the parameters, without knowing a priori the total number of classes in the whole experiences set. The incremental classifier adaptation can be safely used in online continual learning in principle, although it can be quite underperforming of course. This point is discussed again in line 239. Again, I don't see a theoretical limitation in adjusting the architecture when novel classes arrive when the architecture to be adjusted is just an additional incremental classification head, and not the main backbone (the feature extractor). When the set of total classes encountered starts increasing in size significantly, CLIP also can have efficiency-related challenges, since, for a given image batch on a given experience, you have to process the whole set of class-label prompted sentences on the text encoder, which posits a computational burden for huge number of experiences. Therefore, if the argument is solely based on efficiency, a computational efficiency analysis should be provided.

### Questions
In line 138 the authors claim that the main limitation of mentioned CL methods is that they are closed-ended since they handle a pre-defined classifier dimension. This is not true, since in practice it's easy to use an incremental classifier that adds new heads following the same CL adaptation of the parameters, without knowing a priori the total number of classes in the whole experiences set. The incremental classifier adaptation can be safely used in online continual learning in principle, although it can be quite underperforming of course. This point is discussed again in line 239. Again, I don't see a theoretical limitation in adjusting the architecture when novel classes arrive when the architecture to be adjusted is just an additional incremental classification head, and not the main backbone (the feature extractor). When the set of total classes encountered starts increasing in size significantly, CLIP also can have efficiency-related challenges, since, for a given image batch on a given experience, you have to process the whole set of class-label prompted sentences on the text encoder, which posits a computational burden for huge number of experiences. Therefore, if the argument is solely based on efficiency, a computational efficiency analysis should be provided.

### Soundness
2

### Presentation
3

### Contribution
2
