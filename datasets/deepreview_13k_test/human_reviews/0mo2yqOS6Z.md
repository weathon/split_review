# Enhancing Accuracy and Parameter Efficiency of Neural Representations for Network Parameterization

- Decision: Reject
- Scores: 6, 5, 6, 6, 5

## Abstract
In this work, we investigate the fundamental trade-off regarding accuracy and parameter efficiency in neural network weight parameterization using predictor networks. We present a surprising finding where the predicted model not only matches but also surpasses the original model's performance through the reconstruction objective (MSE loss) alone. Remarkably this improvement can be compound incrementally over multiple rounds of reconstruction. Moreover, we extensively explore the underlying factors for improving weight reconstruction under parameter-efficiency constraints and propose a novel training scheme that decouples the reconstruction objective from auxiliary objectives such as knowledge distillation that leads to significant improvements compared to state-of-the-art approaches. Finally, these results pave the way for more practical scenarios, where one needs to achieve improvements in both model accuracy and predictor network parameter-efficiency simultaneously.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The author study the fundamental trade-off regarding accuracy and parameter efficiency in neural network weight parameterization using predictor networks. They present a finding where the predicted model not only matches but also surpasses the original model’s performance through the reconstruction objective (MSE loss) alone. Experiments are done on CIFAR, STL and ImageNet.

### Strengths
1. the topic is of interest and benefits the community
2. the proposed "separation" is flexible

### Weaknesses
- the "low reconstruction error" seems to be a bit arbitrary and I do not see a very good way to find it.
- The reasoning/intuition on why the proposed method even "improve" the performance is lacking
- see more in questions.

minor issues:
1. typos near line 509-510
2. Fig 5 can be earlier?

### Questions
1. Fig. 1: "While one expects that the reconstruction error must approach zero to recover the true performance" How was the "low error" defined? empirically searched?
1. Does the method only works with CNN? I thought no? Maybe only empirically no experiments were done. It is worth trying on transformers.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
In this work, the authors propose using predictor networks to achieve increased accuracy in two ways. The first one is to train the predictor network iteratively using only a reconstruction loss. The increased accuracy is a product of the weight smoothing caused by the reconstruction loss. In the second part, the authors propose to detach the reconstruction loss and distillation loss (as used in previous works) and do it sequentially. They argue that the distillation loss gains are limited to the reconstruction loss when used simultaneously.

### Strengths
This paper is mostly well-written and has some interesting ideas. It also provides a concise and clear overview of the problem, the literature review is comprehensive, and the experiments are thorough. Finally, the problems that this work tries to address, like model compression and improved representation learning, are relevant to the community.

### Weaknesses
I have major concerns related to the technical contributions and the practicality of the proposed approach. The method achieves increased accuracy because of the smoothing of the weights due to the reconstruction (or iterative reconstruction), which is not surprising, and I think there are several other (easier) ways to increase accuracy, generalization, robustness, etc., by smoothing weights, which makes me believe this approach would not be very practical (In the paper there are no comparisons to these easier alternatives).  Another reason I believe this approach is not practical is that reducing model storage is not as big of a concern as reducing the memory needed for the model during training or deployment. 

For instance, let's assume we have an optimally trained model with weight smoothing regularization. For the proposed approach to achieve similar performance to the original model, it will require two networks, i.e., the original and the predictor (e.g., ~40% of the DoF of the original), then we need to have several rounds of reconstruction where the predictor learns to predict the original weights, and then, when need a training stage using only distillation loss. The only real gain will be the reduced memory for model storage (which has to be unwrapped to a larger model to produce predictions), which currently is not a real concern, at least on the applications described in the paper.

Despite this work having some interesting ideas, in its current version, I don't see any major benefits in using it. Please see the questions below for more specifics.

### Questions
- The problem setup in this paper is not clear; Is the original network with parameters $W$ pretrained for the target task? How is the dataset split used to train $W$ and evaluate, for instance, the accuracy vs. reconstruction error results? Which task are these models evaluated on? and what models are used? For instance, what is the size of the predictor network in the experiments in Sec. 3.1? From some of the figures (e.g., figure titles or legends) later in the paper I could see some of these details but they should be summarized before describing the results in Sec. 3.

- In Figure 1 (left) the authors show an expected behavior of the tradeoff between accuracy and reconstruction error; what is this figure based on? why is the expected reduction linear? why is the expected accuracy at a reconstruction error of 0.015 around 20%? I assume the authors used the observed results to build the expected plot, but then again, why the linear behavior instead of the approximate negative quadratic observed in the right plot? Additionally, could the slightly increased accuracy be a product of the variance in the results? error bars and axis labels of the zoomed-in crop of the right plot would be helpful. 

- Is the goal of the reconstruction loss to learn to predict the parameters of a network previously trained? If so, why is the accuracy higher with a non-zero reconstruction error? Can we then assume that the "original" model was not optimally trained? For instance, if smoothing the weights of the network increases its accuracy on a given task, should not the network be trained with a different regularization? e.g. a higher weight decay, which would also smooth weights and suppress high-frequency components.   

- How does the proposed iterative smoothing using predictor networks compare to other weights smoothing techniques like training regularizations or smoothing constraints (e.g., weight decay, dropout, etc.), and the mentioned methods in lines 157-162 (e.g., NeRN with regularization-based smoothness)? 

- It has been widely studied that weight smoothing increases performance, generalization, robustness to noise, etc., and many techniques have been proposed to achieve this, so I don't think it is that surprising of a find, and getting an increased accuracy by smoothing parameters via a predictor network seems overkill to me.

- It would be helpful to have results comparing the proposed method with distillation and using distillation to train a smaller network directly (i.e., instead of training a predictor network for a larger model). It seems to me that the advantages of using a predictor network are not that great if the model has to be unwrapped to produce the predictions. Currently, GPU memory is a greater issue than model storage. 

Minor comments:
- In lines 214-215 the notation can be confusing, i.e., predictor $P$ with $Q$ learnable parameters and the original network $O$ with $P$ learnable parameters.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study explores the trade-off between accuracy and parameter efficiency in neural networks using predictor networks. It reveals that the predicted model can exceed the original's performance solely through reconstruction objectives, with improvements accumulating over successive reconstructions. The research also proposes a new training scheme that separates reconstruction from auxiliary objectives, leading to significant enhancements in both model accuracy and predictor network efficiency compared to existing methods.

### Strengths
1. The paper is well-written with a clear and reasonable motivation. The problem setup and comparison with other methods are well articulated.
2. Extensive validation is conducted on multiple datasets, showing consistent improvements. The figures and tables are presented clearly and logically.
3. The proposed two-stage strategy not only compensates for the shortcomings of the baseline but also achieves better performance.

### Weaknesses
1. The method presented in the paper targets a trade-off between accuracy and compression rate. Can the advantages gained over the baseline pre-trained weights, as demonstrated in Table 2, generalize to a broader range of downstream tasks?
2. Will the progressive enhancement of the teacher network lead to corresponding progressive improvements in performance?
3. Can these advantages extend beyond CNN-based architectures, such as to the pre-training of Vision Transformers (ViT) or hybrid architectures combining ViT and CNN?

### Questions
See weakness.

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
The paper addresses the task of learning an implicit neural representation (INR) of a trained neural network’s weights. When the INR is smaller than the original model, it offers a potential approach to model compression. The authors conduct an in-depth analysis of both a naive baseline and the current state-of-the-art method (NeRN), yielding key insights: (i) increasing the INR size enhances the performance of the reconstructed model, (ii) iterative training of INRs (on the previous INR) can sometimes exceed the original model’s performance, and (iii) NeRN, despite having three objectives, is primarily driven by the reconstruction objective. These findings inform the proposed method, which separates the reconstruction and distillation phases. The approach introduces one or more reconstruction-only stages, followed by a distillation phase (focusing solely on logits, not features), enabling knowledge transfer from potentially stronger teachers. Extensive experiments validate the approach’s effectiveness.

### Strengths
The paper addresses a potentially interesting task within the emerging field of weight-space learning, where neural networks are treated as data points to train other networks. While it may not yet compete with state-of-the-art quantization methods, the paper explores a promising direction that could inspire future advancements. The analysis and motivating experiments are comprehensive and intuitive, and the experiments are thoughtfully designed, demonstrating tangible improvements while simplifying the method relative to the baseline.

### Weaknesses
The paper’s primary weaknesses are in presentation, particularly in the introduction, where motivation and context are insufficiently developed, and in its focus on ResNets alone. Both issues are potentially addressable in the rebuttal, as detailed below.

**Presentation**

The paper lacks a compelling motivation for learning implicit representations of neural networks. I believe the introduction should clearly explain why this is an interesting and valuable topic (I think this should be done even if the main reasons are purely academic and not commercial). Additionally, it presumes familiarity with NeRN, which may make it difficult for readers to follow without proper context. For instance, lines 44-46 discuss the contradictions in the multi-objective loss, yet the paper does not explain that multi-objective losses represent the current state-of-the-art or clarify what these objectives entail. Consequently, the value and relevance of the proposed method in decoupling objectives are unclear. Similarly, terms like “compression efficiency” (line 49) are introduced without context, leaving readers uncertain about their meaning within this work. Defining the motivation and the specific context of the compression task would make these points much more accessible.

**Generalizing to Other Architectures**

While the paper briefly mentions that the method is only applicable to CNNs, it is unclear why this limitation exists. Are there underlying assumptions preventing the method from generalizing to other architectures like ViTs? If there are no such constraints, presenting results on a ViT model would benefit the paper. Although the work remains relevant if limited to CNNs, its scope and applicability would be reduced if it cannot generalize to architectures beyond ResNets.

___
**Smaller issues**

In addition to the above primary weaknesses, below I describe a few additional issues and limitations, these are mostly smaller issues that do not carry a large weight in my decision but should nevertheless be addressed:

1. While the paper focuses on implicit representations for neural networks, there is a growing body of research for learning semantic representations of neural networks and performing other tasks on weights of neural networks, the paper did not cite any of these works, which I think should be done. See [1-12] for a few such examples.
2. The term “inception like” is written a few times (e.g. line 44), what does this mean?
3. A small mismatch in notation, in Eq. 1, in the FMD definition you use $a^{l}$ while in line 92 you use $a^{\ell}$.
4. In Fig. 1, maybe show by how much the performance is improved (in the zoomed in part).
5. Line 252 references Eq. 2, but the actual equation is unnumbered.
6. Lines 264-266 are not very clear, and if they are important enough to be bold they should probably be rewritten. It took me a few passes to understand them.
6. Just making sure, in 3.3, you first perform iterative refinement and then distill? The figure looks like they are simultaneously done and not sequentially.
7. In Fig. 5, the 3.3 part, both the arrows are red, shouldn’t one be red and one blue? 
9. I would replace the term “baseline” in the tables with “NeRN” so that a reader can clearly understand what baseline you are using (and to give NeRN the credit it deserves).

____

[1] Predicting neural network accuracy from weights, 2020, Unterthiner et al.

[2] Towards Scalable and Versatile Weight Space Learning, 2024, Schurholt et al.

[3] Self-supervised representation learning on neural network weights for model characteristic prediction, 2021, Schurholt et al.

[4] Hyper-representations as generative models: Sampling unseen neural network weights, 2022, Schurholt et al.

[5] Learning Useful Representations of Recurrent Neural Network Weight Matrices, 2024, Herrmann et al.

[6] Learning to learn with generative models of neural network checkpoints, 2022, Peebles et al.

[7] Graph metanetworks for processing diverse neural architectures, 2023, Lim et al.

[8] Equivariant deep weight space alignment, 2023, Navon et al.

[9] Equivariant architectures for learning in deep weight spaces, 2023, Navon et al.

[10] Graph neural networks for learning equivariant representations of neural networks, 2024, Kofinas et al.

[11] Neural functional transformers, 2024, Zhou et al.

[12] Permutation equivariant neural functionals, 2024, Zhou et al.

### Questions
As mentioned in the weaknesses section, I think the points for the rebuttal are:
1. Improve the motivation and context in the introduction.
2. Show an example of the method generalizing to ViTs (if indeed there are no underlying assumptions preventing the method from generalizing).
3. Adding the relevant citations and other small issues.

An additional question I had is whether the iterative refinement also works for smaller INRs (e.g., 280).

___ 

In summary, the paper addresses a less-explored aspect of weight-space learning, offering improvements over existing methods with a simpler approach. Since the motivation and presentation could need improving (and if possible, the generalization), I currently assign the paper a score of 5. I will consider increasing my score if the authors satisfactorily address my concerns.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes an analysis and improved method for representing the weights of neural networks by implicit neural representations (INRs). I.e., It aims to compress model weights (or very slightly improve model performance), while keeping the same accuracy. The authors first analyze a reconstruction of model weights by MSE, showing that it enforces some form of smoothing on the weights. Additionally, they claim that with a big enough INR they are able to slightly improve the performance over the original model. They then propose a new method for model compression by INRs that decouples the distillation and reconstruction objectives into 2 separate stages, leading to better results. Lastly, the authors show that by distilling the model using a larger and more capable backbone can improve the compressed model performance.

### Strengths
- The paper is well written and easy to follow.
- Despite the relatively minor technical change from the baseline, the new approach is significantly better at  model compression without losing performance. 
- The analysis performed on model weights smoothness is interesting (Sec. 3.1 and App. A).

### Weaknesses
- **Claim on Accuracy Improvement:** My main concern is that the paper's main claim is not well supported. The authors argue that their method enhances model performance compared to the original uncompressed model through weights smoothing. While this sounds promising and the presented analysis is interesting, in practice, the results reveal that the improvement from smoothness is minimal and almost negligible. The performance gain is limited to small-scale benchmarks like CIFAR-100 and STL-10, where the models’ accuracy increases by only 0.1-0.6%. Furthermore, when tested on ImageNet, the trend reverses, with all experiments performing worse than the original model. I believe that as is, this claim is misleading given these results.
- **Missing Baseline:** The limitation on data usage presented in lines 82-84 about the NeRN baseline, are also true for the distillation loss used in the proposed method. I.e., it becomes impractical for model compression if data is not available. In that case, a knowledge distillation to a smaller architecture should also be considered as an additional baseline, as it has the same goal: compressing the model with minimal performance drop.
- **High-Performing Teacher:** I believe the experiment done with a higher-performing teacher is a bit unfair for the scenario. It seems as if one could perform some knowledge distillation from the stronger teacher before the compression or just compress the stronger teacher in the first place.
- **Combining with Other Compression Approaches:** While the authors claim their method is orthogonal to other compression types, Tab. 5 shows otherwise. Specifically, quantization of the compressed model heavily degrades performance (in CIFAR-100 it decreases from 70.84% to 51.72%).
- **Figure 1(a):** Figure 1(a) is confusing as it only presents an expected trend, not real results. I think this part of the figure should be simply removed from the paper.
- **Intuition in Smoothness Analysis:** While the analysis on weight smoothness presents cases where it slightly improves performance, it does not explain why this happens. I.e., why smoother weights might be better. I can conjecture it is related to the memorization of training examples (overfitting), which can be represented in higher frequencies. If this is the case, an explicit measurement of overfitting (generalization gap) with and without weights smoothing could greatly benefit this analysis. 

Minor Remarks which did not affect the grading:
- Most of the citations should probably be in parentheses and not in line (as all of the paper citations are).
- In line citation at L64 is strange (reference seems to be in the wrong place).
- L251: reference to equation has a wrong number.
- L264-266: These lines should probably be revised to a more accurate version as some terms are unclear (e.g., in which layer does the decision making start and feature extraction end?)
- Tab. 1: All the first lines are in bold. It's a bit confusing for which result to focus on. Should probably choose the best result as in the other lines of the table.

I am open to reconsidering my score given a revised manuscript which addresses the concerns I mentioned.

### Questions
- The method compresses the model storage-wise only if one saves the implicit representation model alone. Does this mean that in order to use the compressed model one would have to thoroughly reconstruct every weight? If so, this means the method wont save RAM space at all, and even worse will require much more inference time. Could the authors show how many FLOPs it takes to rebuild a model compared to a standard inference of it?
- Did the authors try to check if smoothing other layer types (e.g. Fully-connected layers) also works when training an implicit representation for them? While simple smoothing strategies might be ineffective due to the permutations of neurons in neural networks [1,2], training an INR on them could still perform some form of smoothing.
- This is a bit out of scope for this work, but did the authors try to train a model from scratch with some smoothing objective on the weights? Did it improve the results?

[1] Navon, Aviv, et al. "Equivariant architectures for learning in deep weight spaces." International Conference on Machine Learning. PMLR, 2023.

[2] Kofinas, Miltiadis, et al. "Graph neural networks for learning equivariant representations of neural networks." arXiv preprint arXiv:2403.12143 (2024).

### Soundness
1

### Presentation
3

### Contribution
2
