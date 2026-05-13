# Autoregressive Pretraining with Mamba in Vision

- Decision: Accept
- Scores: 6, 5, 6, 6

## Abstract
The vision community has started to build with the recently developed state space model, Mamba, as the new backbone for a range of tasks. This paper shows that Mamba's visual capability can be significantly enhanced through autoregressive pretraining, a direction not previously explored. Efficiency-wise, the autoregressive nature can well capitalize on the Mamba's unidirectional recurrent structure, enabling faster overall training speed compared to other training strategies like mask modeling. Performance-wise, autoregressive pretraining equips the Mamba architecture with markedly higher accuracy over its supervised-trained counterparts and, more importantly, successfully unlocks its scaling potential to large and even huge model sizes. For example, with autoregressive pretraining, a base-size Mamba attains 83.2\% ImageNet accuracy, outperforming its supervised counterpart by 2.0\%; our huge-size Mamba, the largest Vision Mamba to date, attains 85.0\% ImageNet accuracy (85.5\% when finetuned with $384\times384$ inputs), notably surpassing all other Mamba variants in vision.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper shows that Vision Mamba can be enhanced through autoregressive pre-training, similar to using MAE pre-training to improve ViT. It uncovers two key recipes: (a) grouping spatially neighboring patches, and (b) vanilla ordering (row-by-row scan) is effective enough. It achieves significant improvement over supervised baselines.

### Strengths
- The paper is well written, including all technical details. It should be straightforward to implement.
- It is good to see Mamba follow similar pre-training conclusion with other vision architecture (CNN, Transformer): masked prediction in pre-training followed by fine-tuning boosts performance.
- It is good to know that cluster size plays an important role in pre-training.

### Weaknesses
 - Figure 3 is a bit confusing. It seems to illustrate a case of 4 clusters, each has 4 patches. I assume that the arrows within a cluster show the order to flat patches, while the arrows across clusters show the order of prediction. If so, please use different colors and add explanation in the caption.
- In Table 2, please distinguish methods between supervised and pre-training+supervised fine-tuning. In addition, what is the performance for MambaMLP in huge size?
- Section 4.4, is it possible to improve random-order prediction by incorporating position encoding?

### Questions
- As shown in MAE, pre-training has another benefit to improve downstream tasks (like object detection, segmentation). Does this conclusion hold for ARM?
- It would be better to discuss a comparison with a prior work, “Image as First-Order Norm+Linear Autoregression: Unveiling Mathematical Invariance” (https://arxiv.org/pdf/2305.16319), which uses first-order autoregression to pre-train CNN architectures.

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
3

### Summary
This paper investigates the Mamba architecture for visual data using autoregressive pre-training. It shows the Mamba’s visual capability can be enhanced through autoregressive pretraining. It finds autoregressive pretraining equips the Mamba architecture can obtain better performance compared to its supervised-trained counterparts, and also shows the potential for scaling, based on the experiments on ImageNet-1K.

### Strengths
This paper is overall writing well. This work to investigates the mamba architecture using autoregressive pre-training in visual data is important for the community. 
The results are inspiring for the community, e.g., ARM can scale somewhat well, compared to the Vim counterparts; and the ablation on the prediction unit shows the effectiveness of the cluster-based prediction.

### Weaknesses
1.My main concern is the experimental setting:   
(1)	When the results of the proposed method in Table 2 is good, it is not clear for the setting up of other supervised baselines (RegNetY-16G, DeiT-B, Vim-B), e.g, how many epochs these model training? Is it fair to compare these baselines without the same training epochs?  
(2)	Besides, the protocol for evaluating self-supervised method is usually pre-trained on large-scale dataset, then evaluated on the downstream tasks (e.g., linear probe or finetuned with few-shot examples). It is weird that this paper pre-trained on ImageNet using self-supervised learning and fine-tuned with all the ImageNet examples. For a stronger result, I think this paper should pretrain on larger unlabeled dataset, then finetuned on ImageNet. In current experiments, the results are not strong, since Vits using self-supervised learning has shows its potential in performance and scaling ability. Another point, I think this paper should compare the state-of-the-art Vits with the same parameters in Table.2 (the parameters matters for performance), and I donot find the proposed method have better performance than Vits. 


2.It is not clear why this paper uses different setting for pre-training (Fig.4 b) and fine-tuning (Fig.4 c) for the MambaMLP architecture. Is it from the empirical observation? If yes, it is better to show the results, when unifying the setting (e.g., using the same setting for pre-training and finetuning). It is weird that MambaMLP needs two configurations for pre-training and fine-tuning, especially in the situation that this paper only conducts experiments on one dataset (not generable but only tailored for one dataset)

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper applies autoregressive pretraining to Mamba for visual classification tasks.  The Mamba-based architecture uses a block similar to Visual Mamba (VIM) and VMamba, MambaMLP, that applies Mamba over a patch sequence ordered by a 2-level "clustered" raster order and MLP over channels (though, I may have misunderstood the channel vs sequence decomposition, see questions below).  Multiple ablations are performed on Imagenet1k, profiling the system's behavior and performance; substantial improvements are found from using autoregressive pretraining on Imagenet1K and several of its variants.

### Strengths
The experiments clearly show the benefit of autoregressive pretraining for this task, on both MambaMLP (the proposed architecture here) and Vim.  Ablations on token cluster size (a nice idea), decoder and patch representations, and sequence order describe the system behavior well.  Overall, the presentation is quite clear and the system well described, though there are key points that I think could be explained better (see weaknesses below).

### Weaknesses
There are several important pieces of the method that lacked detailed explanation:

* The MambaMLP block is described only in a sketch diagram (Fig 4) and a sentence in sec 3.3 ("uses Mamba as the token mixer and MLP as the channel mixer").  This is a good summary, but didn't explain the block architecture well enough for me to understand the details:  Does this mean Mamba is applied independently to each channel and alternates with MLP?  And how are the Delta, B and C set (which inputs and which channels)?  A more explicit explanation, making use of the summary of Mamba in Sec 3.1 and showing where and how this is used in MambaMLP in addition to MLP would be useful here.

* Likewise, there is no explanation of the patch decoder --- there is an ablation on its design, but I didn't find anything saying what architecture was used.

* Another key point, is how can only one scan order be used in pretraining but four in fine-tuning?  If the other 3 scan orders aren't pretrained, how are they initialized?  And what is the impact of using only one scan order (the one that was pretrained) in fine-tuning (and conversely, is it possible somehow to pretrain all four orders)?  (The terms "scan" and "expand" are assumed and not summarized or used in an explanatory context, either)

A second, more minor weakness is that only image classification is considered, and no other tasks.  Additional task applications would strengthen the results, though the existing ones with classification are already convincing to show the merits of the method.

### Questions
See above.  Additional, more minor questions/comments below.

* Additional related work on autoregression in vision might be mentioned and compared, e.g.  Bai et al 2023 "Sequential Modeling Enables Scalable Learning for Large Vision Models"; Yu et al 2021 "Diverse image inpainting with bidirectional and autoregressive transformers"; Esser et al 2021 "Taming transformers for high-resolution image synthesis."

* Could use better background summary for what is meant by "scan" and "expand" in Fig 4 / Sec 3.3.  While the basic SSM is summarized, as are the orderings in sec 3.2, a little more explanation of the "scans" here would be useful

* Sec 4.3:  When applied to other datasets, is autoregressive pretraining performed only on imagenet1k, the target dataset, or both?

* Eq (3) says $h'(t)$ but this is the descretized system, so should this be $h_t$ on the first line ?

* Random order l.294:  To confirm, the order is a single random permutation order that is fixed for each model instance (so every time the model is called on an image, the same order is always used)?

* typo on l.470, should say width is 512 no depth

### Soundness
3

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
4

### Summary
The paper introduces autoregressive pretraining to the domain of vision mamba models. Drawing inspiration from "Scalable Pre-training of Large Autoregressive Image Models" (AIM), it shows how the method naturally adapts to Mamba models, which are inherently autoregressive, at least in their simplest form. This pretraining method shows positive scaling traits, improving downstream classification accuracy, and also allowing for larger variants to be trained than previously possible.

### Strengths
The paper finds an effective way to apply AIM to the space of vision-mamba variants, demonstrating that it improves the pareto frontier for mamba-based vision models. The pretraining unlocking the use of larger vision-mamba variants is a useful outcome.

### Weaknesses
At a high level, the novelty in this paper is quite limited. It appears to mostly be “AIM [1], but with Mamba”. Similarly, I think table 2 needs to include AIM; I know this is difficult because they don’t provide finetuned accuracy numbers (only probes), but they do provide the model checkpoints, so even a casual attempt at finetuning their 0.6B model on imagenet would be helpful to contextualize on the huge models.

Given that ARM isn’t bringing anything new to the theory of SSSMs or autoregressive pretraining, it doesn’t feel like equations 1-6 are necessary, or at least could be greatly condensed [1, 2], . Particularly given the degree to which this paper builds on AIM, leveraging their section 4.1 would be better. Similarly, equations 7-9 are highly redundant. Distilling all of this down, all of the equations presented in this paper don’t seem to aid in clarity.

“Prediction units”. This is defined in 3.2.2 as generally being patches, aside from iGPT which uses pixels. This seems to be reinforced by figure 2d and figure 3. However, section 4.4.1 confusingly switches to clusters being prediction units. Based on the figures, it seems like a patch is always a prediction unit. But a good amount of the paper is spent on processing order, with a distinction between tokens and clusters. Equation 9 seems to suggest that a full cluster is predicted simultaneously. Presumably ARM is patch based though, so it seems like clusters are mostly just a way to define a particular order of patches, and due to scan being an enforced sequential algorithm, a cluster isn’t actually predicted simultaneously. This would make figure 3 make sense.

Figure 4: I’m struggling to find anywhere where the switch from 1 scan to 4 scans is justified. It would be good to at least demonstrate the difference in accuracy between 1 scan and 4 in your setting.

Table 4 has clarity issues. It would be helpful to directly specify the cluster size instead of having it be $\frac{cluster\_size}{patch\_size}$.

### Questions
4.4.4 Which normalization method are you referring to for pixel targets? I’m guessing you’re referring to MAE’s [3] method, but this needs to be explicitly cited.

Do you have any experiments where you just vary the random seed to get a sense of the variance in model quality just due to randomness? For example, there are 6 examples of the word “significant”, but I assume this is not statistical significance. Taking table 4 as an example, there is a spread of 0.8% between a 1x1 cluster and a 4x4 cluster. Knowing the variance of your method on Top-1% would be really helpful for determining whether these difference are actually significant.

[3] Masked Autoencoders Are Scalable Vision Learners (http://arxiv.org/abs/2111.06377)

### Soundness
2

### Presentation
2

### Contribution
2
