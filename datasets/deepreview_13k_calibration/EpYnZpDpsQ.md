# Self-supervised Representation Learning from Random Data Projectors

- Decision: Accept
- Avg Score: 6.20
- Scores: 5, 8, 6, 6, 6

## Abstract
Self-supervised representation learning~(SSRL) has advanced considerably by exploiting the transformation invariance assumption under artificially designed data augmentations. While augmentation-based SSRL algorithms push the boundaries of performance in computer vision and natural language processing, 
they are often not directly applicable to other data modalities, and can conflict with application-specific data augmentation constraints. This paper presents an SSRL approach that can be applied to \emph{any} data modality and network architecture because it does not rely on augmentations or masking. Specifically, we show that high-quality data representations can be learned by reconstructing random data projections. 
We evaluate the proposed approach on a wide range of representation learning tasks that span diverse modalities and real-world applications. We show that it outperforms multiple state-of-the-art SSRL baselines. 
Due to its wide applicability and strong empirical results, we argue that learning from randomness is a fruitful research direction worthy of attention and further study.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper considers the problem of domain-agnostic self-supervised representation learning. The proposed method introduces multiple random projectors and corresponding predictors, and optimizes the batch-wise barlow twins loss, which constructs the Gram matrix instead of the empirical correlation matrix. To encourage the diversity, many projectors are initialized and then only 10% are subsampled for use. Experimental results on datasets from various domains show the effectiveness of the proposed method.

### Strengths
- Domain-agnostic representation learning is a timely topic.

- The proposed idea is simple and the proposed method improves the performance in most cases.

### Weaknesses
 - Discussion/comparison with other domain-agnostic methods seem to be not enough. For example, [Lee et al.] proposed a domain-agnostic augmentation strategy applied to image, speech, and tabular datasets, and [Wu et al.] proposed randomized quantization and experimented on image, point cloud, audio domains and the DABS benchmark. I suggest including discussion and experimental comparison with them. 

- It is good to see that experiments include various domains including time series, tabular, and image, but they seem to be relatively small and not commonly used for benchmarking machine learning models. For example, Kvasir is a medical image dataset, which is different from the widely used "natural" image datasets; it should be categorized differently from natural image datasets. Authors may want to refer to [Lee et al.] and [Wu et al.] to find commonly used datasets to provide the general applicability to various domains and scalability of the proposed method.

- While the authors claim that the optimization strategy for the proposed method is EM, but it is not clear how the proposed alternating optimization is related with EM by looking at the formulation. I think the transition from Eq. (2) to Eq. (3--4) requires more explanation supported with some math.

- The claim around batch-wise barlow twins that MSE is preferred over cross-entropy/contrastive/triplet losses is not justified. Isn't the batch-wise barlow twins loss just a kind of contrastive loss, in that it contrasts all samples within the batch? Note that the original contrastive loss (not the InfoNCE variation) also computes the MSE loss. An ablation study with different type of losses might also be helpful.

- The criterion for diversity encouragement requires more intuition. It is hard to imagine what is going on when optimizing the proposed learning objective. Also, what is the computational cost for the NP-hard objective function?

- The comparison might not be fair as the proposed method requires more computational cost to encode input with multiple random projectors and predictors compared to other baselines. The computational cost should be matched for a fair comparison and reported.

### Questions
Please address concerns in Weaknesses.

> **post rebuttal**

After discussion with authors, I feel that the experimental results are not sufficient to support the claim that they cover "a wide range of representation learning tasks that span diverse modalities and real-world applications." Initially their experiments covered time series, medical image, and tabular domains, and the additional results in the natural image domain show that their method is not effective for natural images, compared to other baselines. **Authors are encouraged to explicitly limit the scope to the domains they experimented in the title/abstract/intro.**

Also, I am not sure if the comparison is fair (e.g., if they tuned hyperparameters for baselines properly), so experimental results are generally not convincing to me.

Though I feel more confident on my rating, given that authors addressed all concerns from the other reviewers well and the proposed method is still interesting to me, I do not want to put too much weight to my rating.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors of this paper propose a technique called Learning From Randomness (LFR), which allows the application of self supervised techniques in arbitrary data domains. The proposed method works by projecting the data into random representations, and then training a model to predict these random representations. The authors show that the resulting model can learn useful representations, even without domain knowledge for the datasets examined.

### Strengths
- The paper is very clear and easy to understand. I did not have any issues in grasping the points the authors are trying to make.

- The method proposed is novel, as far as I am aware. It is also very interesting, as learning from random data is not a very explored area of research. As the authors note, the proposed technique enables self supervised learning without the need for domain knowledge, in order to create good augmentations for the data. There is also a clear benefit from using LFR in the datasets examined, without having to rely on complicated techniques.

- The authors perform ablations on the random projectors used, as well as the required diversity of the random representations and the training procedure for the model. I find it interesting that the authors perform an EM-based approach in learning the model, instead of simple optimizing all of its parts all at once. Similarly, I find equally interesting the preprocessing step that selects the best random projectors to predict during training.

Overall, I find the proposed method insightful, with clear benefits over previous work in datasets that are not as explored as the usual ones (e.g. CIFAR-10/100, ImageNet).

### Weaknesses
 - One of the issues I have with this paper is that despite the use of several datasets used to evaluate LFR, the commonly used ones such as CIFAR-10/100 are not among them. While I understand that LFR does not aim to improve performance on these datasets (since natural image augmentations already perform very well) it would be interesting to examine those to compare as well. It would be useful to know if LFR is better/worse than optimized augmentations, such as those used in SimCLR.

- I think the paper could also be improved via further experiments on the following two subjects:

  - I think it would be interesting to see some ablations on the distance metric used for training. Right now, the authors use Barlow Twins as the metric, but it would be interesting to perform ablations with e.g. MSE or Contrastive losses for this (although I must note that the authors do make an argument for this design decision in the paper).

  - I think it would also be interesting to see the transferability of the trained models across different datasets. I would be interested in knowing if LFR leads to learning representations that are good for the particular dataset, or good for the chosen modality in general.

### Questions
I would be grateful if the authors could comment a bit on the choice of the number of projectors $K = 6$ and batch size $B = 256$. Intuitively, both of these values seem a bit small when trying to find diverse random projectors. The authors have tried going up to $K = 8$ and batch size $B = 512$, but I would like to know if they have tried higher values for these two hyperparameters (especially for the number of projectors $K$).

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposed the method of self-supervised representation learning that can be used to learn useful representations from different modalities, e.g. images, text, time series, tabular data. Proposed method is based on recent approach where we have architectures with an additional projector (Guillotine regularization, removed for a downstream task) tries to predict multiple random projectors. The authors provide some analysis of hyper-parameter sensitivity, different initializations of random projectors, etc. Comparison with other methods on different modalities are proposed (time series, tabular, image).

### Strengths
S1. The method is simple and very generic. Removes the prior of knowing what data aug. we should use for many current SSL contrastive-based methods.
S2. Paper easy to follow and well-written.

### Weaknesses
W1. The main weakness for me is inability to compare with the existing method on well-known datasets in computer vision tasks. We have 3 x time series, 3 x tabular, and 1 x image - where Kvasir is not commonly used dataset. Not sure if the results are not picking the datasets that show good results. Why not presents the results on ImageNet, and if computationally not possible - cifar100. 

W2. There's no evaluation on the different downstream task for the learned representation, e.g. feature extractor trained with LFR on Kvasir and evaluated on the other dataset similar and disimilar one. We do not know how the learned representation generalize, and what if we only memorize patterns that then can be then useful for the lin. evaluation.

W3. We don't know the final computational overhead of the initialization and comparison to any SSL method. In the appendix we have total time spent for a particular dataset (e.g. Kvasir V100 1095 GPU hours for all experiments). Would be better to know the comparison between SimCLR/SimSiam vs LFR. 

W4. 2 time series datasets (HAR, Epilepsy) and tabular Income&HEPMASS have already good accuracy on the randomized init. What is intresting, some methods are below that (HAR - Autoencoder). 

W5. Lack of more theoretical explanation why it should work? What random projectors can be used? etc.

### Questions
Q1. How the method perform without using heavy SSL (SimCLR) data augmentations?

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes "Learning from Randomness" (LFR), which tackles the long-standing problem of removing augmentations from SSL. Instead, random projections of the representation are learnt via a bank of predictors, with the intuition that diverse random projections replicate a set of generic downstream tasks.
An objective like Barlow-Twins is used, as well as an iterative training procedure that updates the backbone and the projectors in separate steps. In order to have diverse random projections, the authors propose to sample several of them and select those that are more decorrelated.

The experiments show how the proposed method is a suitable option for time-series, tabular data and medical images datasets. Interestingly, no augmentation is used in all these settings, which I find interesting and novel. An insightful ablation study is also provided.

### Strengths
* The problem of removing augmentations in SSL is of great importance in the community.

* The paper is very well written, organized and presented.

* The authors will release code.

### Weaknesses
 * The experimental section does not include any medium/large scale dataset, which obfuscates the benefit of the method for any SSL task.

* I found a transfer learning experiment lacking in the results.

* More discussion about the pros/cons of using random projections would be valuable.

* I suggest evaluating LFR vs. computer vision methods in a different scenario than medical images. It is possible that SimCLR would perform better on CIFAR-10 or ImageNet, nevertheless that experiment would show how well LFR is performing against methods tailored for such scenarios. This would also help to understand how well random projections "emulate" the use of well-chosen augmentations. I think a natural images dataset is required for this paper for acceptance.
  * In the Appendix, the authors provide an example of feature interpretability on CIFAR-10. Noting that the pipeline to train on natural images is already in place, I reinforce my observation that an evaluation on natural images should be part of the experimental section.

* It would be great to have some discussion about how LFR could be applied to Transformers, given their wide use. Comparison with a masking approach would not be required, although of great interest.

* A batch size of 256 is strongly detrimental for a contrastive approach such as SimCLR, for example. Small batch sizes harm performance for such methods. For the reader to fully grasp the scenarios where LFR is suitable, I suggest comparing with SimCLR in settings where the latter is known to excel.

### Questions
I do not have a large amount of questions, since the paper is very well explained and motivated. However, I would greatly appreciate to discuss with the authors about the following:


* The main intuition of this method is to create random downstream tasks that capture different aspects of $z$. Therefore, I would suggest adding a transfer learning experiment, in which an encoder $f_\theta$ is learnt on a source dataset, and such features are transferred to other real downstream tasks. It would be really interesting to see a gain in such setting, wrt. other SOTA methods. I believe this would strongly reinforce the claim of the paper.

* I wonder if random projections are enough to capture the diversity inherent in complex datasets. I think the paper would benefit from a discussion on the pros and cons of using random projections. Note that the datasets shown in the paper are considered small-scale in the community, which limit the understanding on how effective LFR is for _any_ dataset.   Larger, or more diverse, datasets would be extremely valuable. See following point.

* I suggest evaluating LFR vs. computer vision methods in a different scenario than medical images. It is possible that SimCLR would perform better on CIFAR-10 or ImageNet, nevertheless that experiment would show how well LFR is performing against methods tailored for such scenarios. This would also help to understand how well random projections "emulate" the use of well-chosen augmentations. I think a natural images dataset is required for this paper for acceptance.
  * In the Appendix, the authors provide an example of feature interpretability on CIFAR-10. Noting that the pipeline to train on natural images is already in place, I reinforce my observation that an evaluation on natural images should be part of the experimental section.

* It would be great to have some discussion about how LFR could be applied to Transformers, given their wide use. Comparison with a masking approach would not be required, although of great interest.

* A batch size of 256 is strongly detrimental for a contrastive approach such as SimCLR, for example. Small batch sizes harm performance for such methods. For the reader to fully grasp the scenarios where LFR is suitable, I suggest comparing with SimCLR in settings where the latter is known to excel.

* I highly appreciated the breakdown of GPU hours required for this paper.

-----

Overall comment:

The method proposed is sound, and the goal of removing augmentations from SSL is a long-standing one. Learning from random projections seems a sensible way to tackle such problem. The overall architecture and objective is solid, I have no concerns in that sense. The manuscript is written elegantly, with the appropriate language. 

However, for the method to be rigorously evaluated, more experiments would be required. Otherwise, there is doubt about whether random projections are valuable for small datasets only, etc. 

Notably, I suggest the authors to:
* Perform transfer learning experiments to support the main hypothesis of the work (random projections allow learning different aspects of $z$, thus making $z$ more generally applicable).
* Evaluate in a setting where classic methods perform at their best, to understand the limitations of the proposed approach. I would suggest a natural images setting, using ImageNet ideally, or CIFAR-10/100 if GPU hours are a concern. 

* I think it would be interesting for the reader to see how the training behaves with joint training, I suggest adding some of these plots in the Appendix.

I would be happy to increase my score after discussion and manuscript updates.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work introduces a self-supervised representation learning scheme that can be applied to any data modality and network architectures. To this end, it proposed to learn the representations from random data projects of the input data. It is a scheme that learns from randomness, aiming to extract meaningful representations from randomness that mimic arbitrary downstream tasks.

### Strengths
1, this framework can accommodate various data modality

2, extensive experimental results with good performance

### Weaknesses
1, Despite the good performance of the experiments, what has been learned from the latent space using the scheme introduced in this paper, even intuitively?

2, It says in the paper that $g^{(k)}(x)$ uses the same architecture design of $f_{\theta}$. Even with random initialization, it may still follow a certain distribution family. How would changing this architecture affect the learning?

3, The paper only exams the accuracy on the classification task for frozen representations. Nonetheless, a good representation could used for various purposes, i.e., manipulation of each dimension in the latent space for generating new data, understanding the essential dynamics of the system in physical models and time series data. How could this strategy be applied to scenarios beyond classification?

4, Although the fact that choosing good augmentations usually requires domain knowledge, in many of the application mentioned, such knowledge could be partially obtained using physical intuition. By comparing with models under random corruptions doesn't seem to be a fair comparison.

### Questions
Please see Weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
