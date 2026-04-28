# Your CLIP Model Might Be Undertrained

- Decision: Reject
- Scores: 3, 3, 5, 6

## Abstract
Contrastive Language-Image Pretraining (CLIP) models exhibit good performance on a range of vision tasks. To improve the performance of this class of models even further, several works have proposed to modify the CLIP training procedure. In this work, we show that it is possible to achieve substantial gains using a much simpler strategy. Specifically, existing CLIP models---especially those trained on smaller datasets---tend to be undertrained. Indeed, we show that extending the training procedure according to a simple heuristic can significantly improve the performance of CLIP models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper reports the observation that existing popular CLIP training recipe is suboptimal on smaller datasets (under training), and demonstrates clear improvement by resuming the training with a higher learning rate. Experimental results on ImageNet show the effectiveness of the proposed modified training recipe.

### Strengths
The finding of the paper is clear and simple. The experiments seem convincing. It is a meaningful contribution and the community should move away from the current suboptimal CLIP recipe especially on the CC3M data.

### Weaknesses
1. Why is the proposed observation of under-training only present with the smaller dataset e.g. CC3M but not with the larger ones like LAION-400M? It'd be very helpful if the authors can provide some insights here, because this seems to be the core contribution of the paper. For example, does the noise level in the image-text dataset affect the fitting behavior in some way?

2. Many existing CLIP recipes rely on high-resolution finetuning after the low-resolution pretraining (e.g.ALIGN, CoCa), which is essentially doing the same finetuning with the extra cycle as shown in Figure 1 (right). Would the proposed approach still benefit models that are already trained with high-res finetuning? 

3. For ablation, I think it'd be cleaner to compare with a baseline that is trained on the same number of epochs so that the only difference is the learning schedule (instead of adding additional training epochs). 

4. The paper writing can use some improvement to expand on the introduction, method, analysis, and related work (still plenty of space left).

### Questions
See weaknesses in order.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper revisits the training schedule of the CLIP, especially on those trained on smaller-scale datasets, and finds that a simple continuing training with LR rewinding can significantly improve the CLIP baselines. It demonstrates improvements on 6 ImageNet variants with R50/ViT-B-32/ViT-B-16 backbones and even outperforms some approaches that are designed to be data-efficient (e.g. DeCLIP) when trained on CC12M.

### Strengths
- The finding of the paper is interesting
- It establishes a stronger baseline for CLIP training, and questions whether we should solely evaluate data efficient approaches on smaller scale, and its transferability to large-scale datasets.

### Weaknesses
- The finding does not necessarily transfer to models that are trained on large-scale datasets (e.g. 400M).
- There is not much analysis / theory on why such behavior exists (or not) on different scales of datasets.
- It would be interesting to see how the proposed schedule helps when we apply to other approaches in Table 7.

### Questions
See weaknesses.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a training technique using which the performance of CLIP like vision language models can be improved without undergoing any change in objective function or model architecture. Authors of this work shows that CLIP like models trained on small scale datasets like CC-3M or CC-12M might be under trained. To improve their performance, simply finetuning a pre-trained CLIP model again with additional few epochs with a restarted learning rate scheduler is enough. The paper additionally shows that this technique is less effective when tried on CLIP models trained on large scale datasets like LAION-400M. The paper shows additional ablations and result comparisons with previous methods to provide a broad perspective.

### Strengths
1. This work shows that hyper-parameter and tweaking training strategies for large-scale pretraining of vision-language models plays significant roles in determining their performance on downstream tasks after training.
2. Restarting the LR scheduler with few-additional epochs is a simple and elegant way to improve performance of CLIP models trained on small scale datasets.
3. The resulting performance of the model is competitive to prior methods that bring additional objective function or model architecture changes to baseline CLIP model.
3. Most importantly, this study underlines the crucial need of bench-marking at larger scales to truly reflect improvements due on proposed modifications. Otherwise, showing effects on small scale datasets could be sometimes misleading.
4. The paper conducts fair comparison and additional ablation studies to provide a broad perspective about CLIP training.
5. Paper is easy to read and well presented.

### Weaknesses
1. In my view, this paper presents a effective but somewhat hyperparameter training technique which is more of a engineering trick rather than pure novel contribution. In other words, this paper says that one should use a altered version of multi-cycle LR scheduler instead of a single-cyle LR schedule to improve CLIP performance.
2. There is little or no analysis on why the proposed trick helps improve CLIP performance. This work can be further supplemented by conducting a detailed analysis on the learned embeddings, for example analysis on modality gap [1], t-SNE visualizations etc.
3. This work shows performance comparison on zero-shot tasks, but it will be great to see how the learned embeddings provide benefits for adaptation tasks like linear probing or its use on downstream tasks which uses CLIP features in their framework.
4. Although competitive to prior methods trained on CC3M and CC12M, it is unclear how this technique performs when combined on pre-trained models of prior methods. For example, does this technique shows complementary effect when plugged on CyCLIP pretrained model? (using same CyCLIP objective functions even in the proposed technique)
5. Similar results with-and without this technique on large scale CLIP models like CLIP-LAION400M shows that this trick is only valid for small scale models with less than 50% baseline accuracy.  
6. There are missing tables in the paper. For example, I cannot see Table 1 anywhere in the paper.

### Questions
My main concern is that this paper mainly shows a training trick, which poses questions for novelty of this work. Please refer to the weaknesses section for my additional concerns and queries. 

In summary the paper is nice but it lacks solid technical contributions which can be an significant issue.

### Soundness
2 fair

### Presentation
3 good

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
This paper makes a simple but intriguing observation that vision-language models trained on even a small dataset such as CC12m can improve substantially (10% zero-shot accuracy), by restarting the training of the model on the *same* data. The paper starts by showing this for on CC12m by training for an extra 15 epochs (Figure 1), then it shows that similar improvements are reached with 2 other models for various number of extra epochs (Figure 3), then shows that the improvements are consistently significant on various OOD datasets (Table 2), then they confirm that restarting training even from early checkpoints can result in faster training (Figure 4), then they extend the idea by repeating the restart by revisiting the idea of cyclical LR schedules and show that a cyclical LR can reach a higher accuracy than a single cycle cosine LR schedule (Figure 5). Finally, they use a cyclical LR schedule to train on the larger LAION400M dataset and conclude that “CLIP models trained on large datasets are less likely to be undertrained.”

### Strengths
- The results are surprising and promising for future directions on alternative LR schedules for multi-modal training.
- The paper is easy to read and asks natural questions sequentially that engages the reader. Although the reader is left with many unanswered questions by the end!

### Weaknesses
- While the paper makes interesting observations, the paper is missing a lot of discussion and potential for extending the observations given the unused page limit. A few unanswered, immediate and simple questions: How many cycles are optimal? How long should each cycle be? Is there a relation between the number of samples and the length of the LR cycles? Figure 5 only presents results with one schedule.
- Results in Figure 4 and 5 are limited to only one architecture and are not shown to hold for other architectures. Would these results hold for ViT-L/14?
- The final conclusion is that “CLIP models trained on large datasets are less likely to be undertrained.”. This is based on only one LR schedule and one model that does not provide definitive evidence for the conclusion.

### Questions
- Where are Figure 2 and Table 1?

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
