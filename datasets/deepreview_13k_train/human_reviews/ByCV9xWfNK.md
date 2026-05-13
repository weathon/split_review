# Intermediate Layer Classifiers for OOD generalization

- Decision: Accept
- Scores: 6, 6, 8, 6, 6, 6

## Abstract
Deep classifiers are known to be sensitive to data distribution shifts, primarily due to their reliance on spurious correlations in training data. It has been suggested that these classifiers can still find useful features in the network's last layer that hold up under such shifts. In this work, we question the use of last-layer representations for out-of-distribution (OOD) generalisation and explore the utility of intermediate layers. To this end, we introduce Intermediate Layer Classifiers (ILCs). We discover that intermediate layer representations frequently offer substantially better generalisation than those from the penultimate layer. In many cases, zero-shot OOD generalisation using earlier-layer representations approaches the few-shot performance of retraining on penultimate layer representations. This is confirmed across multiple datasets, architectures, and types of distribution shifts. Our analysis suggests that intermediate layers are less sensitive to distribution shifts compared to the penultimate layer. These findings highlight the importance of understanding how information is distributed across network layers and its role in OOD generalisation, while also pointing to the limits of penultimate layer representation utility.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper investigates the use of intermediate layer linear probing classifiers to enhance a model's performance on out-of-distribution (OOD) datasets, where the test data distribution differs significantly from the training data distribution. People usually assume that the network can act as a combination of general feature extraction(early layers) plus in-domain task specialization(later layers). The method builds on the assumption that not only the the last classifier specializes in the in-domain distribution, last few layers in the backbone beyond the final classifier also focus on the in-domain distribution. So it propose to place the probing classifier at an intermediate layer to improve transferability and adapt to OOD settings

### Strengths
1. The paper includes comprehensive experiments demonstrating that intermediate layer probing consistently outperforms last-layer probing in OOD scenarios. This is shown to hold across various network architectures and datasets.

2. By investigating intermediate layer probing, the paper provides a theoretical perspective on measuring distribution shifts within network representations

### Weaknesses
1. The definition of “few-shot” may differ from conventional standards, as it uses a significant portion of the test dataset (e.g., half of the CMNIST test samples) rather than the typically small sample sizes seen in few-shot learning. This discrepancy may limit the generalizability of the results.

2. I'm confused that why the zero-shot probing setting can serve as a method to improve the OOD performance. I thought that when trained on in-domain data alone, the OOD performance would not improve since no OOD data is used to train the probing classifier. Would the zero-shot setting can improve the OOD performance?

3. The use of a single-layer linear classifier at an intermediate layer may restrict its ability to capture more complex feature relationships necessary for challenging OOD tasks. Incorporating a more complex classifier, such as a multi-layer perceptron (MLP) or adaptors, could potentially improve performance on these tasks.

4. The main assumption aligns closely with [1], which suggests that layer-wise neural collapse (NC) progresses through two distinct phases in downstream tasks: Phase 1, where representations exhibit a progressively decreasing trend, capturing universal feature mappings; and Phase 2, characterized by a progressively increasing trend, focusing on task-specific feature mappings. A comparison with this prior work would provide valuable insights into how the proposed method builds upon or diverges from these observed phases.

### Questions
Based on the weakness I have the following questions:

1. Could you clarify how "few-shot" is defined in this context? The use of half the CMNIST test dataset may diverge from traditional definitions of few-shot, which usually refer to very limited samples (e.g., 1–5).

2. Could you provide more details on why zero-shot probing—where only in-domain data is used—seems to enhance OOD performance? This mechanism isn’t entirely clear, as one would generally expect some OOD data to be necessary for adapting to distribution shifts.

3. Has the team considered testing more complex classifiers at the intermediate layer, such as a two-layer MLP? Or add an adaptor between backbone and the linear probing?  Since pruning the intermediate layers may omit useful deep features, a more complex classifier could potentially bridge this gap and enhance OOD results.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors explore whether the intermediate layers offer better out-of-distribution (OOD) generalisation. They found that in a number of settings, including zero- and few-shot, they do and demonstrate the limits of penultimate layer representation utility. Most interestingly, the authors claim that ‘earlier-layer representations without fine-tuning on the target distribution often fare competitively with the last-layer retraining on the target distribution’.
The contribution of the paper is empirical, and the authors support the claims with extensive number of experiments.

### Strengths
Pros:
- Significance: The question of generalisation, especially to the zero-shot scenarios, is an important one. While I think it’s been tremendous work done, s I discuss in comment 2, it is important to discuss a number of limitations such as selection of evaluation dataset,
- Correctness: I haven’t spotted any incorrect statements in the paper
- Motivation: the paper challenges the conventional wisdom of using the last layer for zero and few-shot learning, and I believe it’s a great motivation
- Reproducibility: I’ve checked the experimental setting and it looks reproducible to me. I would also highlight that the description of the experiments is exceptionally clear
- Clarity: the paper is very clearly written (apart from a couple of comments below)

### Weaknesses
Cons:
- Clarity and limitations: a few questions on the experimental setting



### Questions
1. “Line 198-199: using  data that can be either ID or OOD, depending on whether  the setup is zero-shot or few-shot.” Not sure I get this phrase, why would the data be selected ID for the zero-shot scenario and OOD for the few-shot scenario? Shouldn’t it be both ID and OOD for both cases (or just OOD)?
2. The biggest question and concern is the inclusion criteria for both datasets and the models. The dataset performance beyond most-known datasets such as CIFAR-10 and CIFAR-100 may differ not least due to the fine-grained nature of some of these datasets. Figure 7 from Tobaben et al (2023), for example, chose to include VTAB-1k datasets to test the performance on the different datasets. On the inclusion of the models, on one hand, it seems to give a fair share of ViTs and ResNets, however it would be great to spell out the inclusion criteria: why did the authors choose this particular selection of the model? Separate subsection in  Section 4 seems to be an appropriate place for this. 
3. The authors can argue that it’s not within the scope, so it would be a fair play, however, it would be interesting to see the following. It appears that the models have been trained on the clear target dataset (i.e., the authors  evaluate the OOD performance of the CIFAR-100 trained model), and I wonder if they tried whether these findings generalise for models, pre-trained on generic large-scale data (i.e. ImageNet-pretrained or pretrained models such as DinoV2 or other varieties of pretrained ViT)? This may be useful in finding out whether the conclusion of the paper remain valid for the scenarios when  

Tobaben et al (2023) On the Efficacy of Differentially Private Few-shot Image Classification, TMLR 2023

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper shows that in ResNets and ViTs, intermediate layers classification is more robust to the distribution shifts of the out-of-distribution samples (OODs). In particular it shows that the features of the pen-pen-ultimate layer consistently outperform the features of the pen-ultimate layer, when it comes to the zero-shot and few shot cases. These results are interesting, as they contradict the current belief that it is enough to retrain the last layer, that is the classification layer. It is assumed that each layer computes interesting invariants of an input image, and this paper raises the possibility that some of these invariants get lost in downstream layers.

### Strengths
This is a very intriguing paper, that raises the question of what happens in the last layers, that overcomes generalization to OOD samples?

### Weaknesses
While analyzing the depth and the sensitivity as important factors in generalization ability, it would be interesting to understand what happens in the last layers that reduces generalizability?

In principle, the features of intermediate layers, are propagated down all the way to the pen-ultimate layer, through skip connections, in both ResNets and ViTs. However, they are added before every layer with the output of the previous layer. 

Is this the reason of why generalization ability decreases?

From the point of view of back-propagation the addition does not matter, as the derivative of a sum is the sum of the derivatives. However, this addition may clutter the features?

### Questions
In principle, the features of intermediate layers, are propagated down all the way to the pen-ultimate layer, through skip connections, in both ResNets and ViTs. However, they are added before every layer with the output of the previous layer. 

Is this the reason of why generalization ability decreases? 

From the point of view of back-propagation the addition does not matter, as the derivative of a sum is the sum of the derivatives. However, this addition may clutter the features?

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
The paper investigates how intermediate layers in deep neural networks (DNNs) can improve out-of-distribution (OOD) generalization, challenging the common practice of relying solely on the last layer's representations. The authors use the notion of Intermediate Layer Classifiers, which consist of linear probes attached to each intermediate layer of the network but trained specifically to perform OOD classification. Two scenarios as considered: one "few-shot", in which few OOD samples are available for training, and one "zero-shot", where no OOD samples are available, under several types of distribution shifts, datasets, and architectures. They conclude that in both cases training classifiers on intermediate layer representations tends to perform better than last-layer retraining, and suggest that one of the reasons for this phenomenon is that intermediate representations are less sensitive to distribution shifts.

### Strengths
- The paper is very well-written.
- The paper assesses intermediate-layer performance across a variety of tasks, datasets, and architectures, which strengthens the generalizability of the findings.
- Interesting discussion on why intermediate layers might generalize better to OOD data, including their reduced sensitivity to distribution shifts and improved data efficiency.
- By demonstrating that intermediate layers can achieve competitive results even in few-shot or zero-shot settings, this work provides practical benefits, especially for applications where OOD data is scarce or unavailable.

### Weaknesses
 __Sensitivity Analysis:__ although the sensitivity analysis aims at showing the stability of intermediate-layer features, it lacks sufficient depth on why some intermediate layers are more stable than others in different types of shifts, particularly for different architectures. The inclusion of a summary of any trends observed across architectures/datasets/shifts would be helpful.

__Figure 10:__ The point made in the description of Figure 10 is not clear from the plots shown, especially since it is not clear how many points occlude one another in the scatter plots. What dataset was used here, and what model? The quantitative analysis is also confusing: although the authors say that an increasing separation exists in earlier layers, I believe this only holds for the minority groups. Perhaps the authors should clarify this.

__Terminology:__ I found the terminology a bit confusing when dealing with training points vs. testing points vs. probe points vs. OOD points. Namely, I had trouble following which sets contained OOD points vs. ID points, especially in the zero-shot section. It would be advisable to always point out which points are OOD.

__Novelty:__  The literature reviewed for related work seems superficial. A notable example of a paper missing from the references is:

[1] Yosinski, J., Clune, J., Bengio, Y., & Lipson, H. (2014). "How transferable are features in deep neural networks?"_Advances in Neural Information Processing Systems_, 27. https://proceedings.neurips.cc/paper_files/paper/2014/hash/375c71349b295fbe2dcdca9206f20a06-Abstract.html

which explored a method for quantifying the transferability of features from each layer of a deep network, including their applicability to shifts in the data (e.g., different subsets, and even different classes).

Furthermore, the novelty of this contribution is somewhat diminished given that an earlier paper (accepted at last year's ICLR) has also proposed evaluating intermediate layers’ effectiveness in generalization for OOD samples:

[2] Gerritz et al. (2024) "Zero-shot generalization across architectures for visual classification." _The Second Tiny Papers Track at ICLR 2024_, https://openreview.net/forum?id=orYMrUv7eu

In fact, an extended version of that paper (from the same group) also used linear probes to quantify the out-of-sample accuracy of intermediate representations:

[3] Dyballa et al. (2024). A separability-based approach to quantifying generalization: which layer is best?. _arXiv preprint arXiv:2405.01524_, https://arxiv.org/abs/2405.01524

This paper would certainly benefit from acknowledging that similar observations have been previously made when performing category discovery on unseen classes (as opposed to the distributional shifts here studied).

__Frozen weights:__ The fact that the authors only considered frozen, pre-trained weights in all scenarios studied is somewhat unrealistic or at least incomplete. In any practical application of this method, if it is feasible to fine-tune the pretrained model on one's own data, then that will certainly be preferable. See reference [1] for an example in which both cases (frozen weights vs fine-tuned) are considered. Specifically for this paper, it would be interesting to verify whether the comparisons between penultimate layer and intermediate layer outputs hold in that scenario.

### Questions
- __Figure 3:__ which ResNet was used to produce the bar plot?
- __Figure 4:__ which ResNets were used to produce these plots? Was any trend observed when comparing the different ResNet sizes?
- __Section 4.3:__ can we really call "zero-shot" a setting in which the "OOD" data is composed of ID samples with added noise? That is a standard modification used in data augmentation (used to increase the number of ID samples), for example, so such a "distribution shift" seems extremely mild to be considered zero-shot. I would have liked to see a discussion of the different shifts chosen compare to one another in terms of difficulty.
- Did the authors find that any particular architecture had intermediate representations consistently outperforming last-layer retraining?
- Did the best layer for a particular dataset seem to agree with the best layer for other datasets, for the same model?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper questions the use of last-layer representations for out-of-distribution (OOD) generalization due to their sensitivity to data distribution shifts. Instead, by introducing intermediate layer classifiers (ILC), the paper shows that intermediate layer representations often outperform penultimate layer representations in generalization.

### Strengths
The paper is well-written and easy to follow. The observation is interesting that intermediate layers may perform better than the last layer in generalization. And, the paper introduces a new metric named "sensitivity score" to measure the sensitivity of each layer to distribution shifts.

### Weaknesses
1. The paper discusses a concept called "information content", but it lacks some detailed explanation. The authors need to demonstrate why the accuracy on OOD tasks can characterize "information content". Specifically, it's unclear why a linear probe's accuracy on OOD data directly translates to the "information content" of a layer, especially when non-linear relationships might exist between layer representations and the target task. The paper should explore the possibility that the observed performance differences are not solely due to the information content, but also due to the capacity of the linear probe to capture the relevant information.
2. The potential impact is not so clear. The observation is interesting, but it may be difficult to find the "best" layer in practice. The paper does not provide a clear methodology for selecting the optimal intermediate layer for a given task and dataset. The sensitivity score is introduced, but it is not clear how this score can be used to guide the selection of the best layer in a practical scenario. The paper needs to provide more guidance on how to use this score to select the best layer for a given task.
3. It is better to provide more theoretical backups to support the experimental findings. The paper lacks a theoretical framework to explain why intermediate layers sometimes outperform the last layer in terms of OOD generalization. The empirical findings are interesting, but without a theoretical understanding, it's difficult to generalize the results to other architectures or tasks. The paper should explore existing theoretical frameworks that can be used to explain the observed phenomena, or provide a new theoretical framework.

Small typos: "atop" (line 469); "in earlier layers" (line 497); "$\pi$" not defined (line 500)

### Questions
1. Could the authors provide more explanations about the feasibility of using the sensitivity score as defined in the paper? Why is this score appropriate for characterizing the sensitivity?
2. All the experiments are based on the task of image classification. What will the results become when dealing with other tasks besides image classification?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 6

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper demonstrates that leveraging intermediate features outperforms conventional approaches relying on last-layer features for OOD generalization. The claim is substantiated through extensive experiments across diverse datasets, varying data quantities, model architectures, and types of distribution shift. Additional analysis on feature sensitivity further reveals that intermediate features exhibit greater robustness to distribution shifts.

### Strengths
* The paper is well-written and clearly presented.
* The experiments are comprehensive, covering multiple aspects.
* The analysis of feature sensitivity is interesting.

### Weaknesses
 * The most convincing experimental results supporting the paper’s claim are observed on CNNs, whereas the performance gains on (currently) more widely used transformer-based architectures are less pronounced, with intermediate features providing only marginal improvement over last-layer features. It may worth discussing the potential reason for this performance disparity. 
* More critically, while the paper offers detailed descriptions of the data and model setups, it lacks a clear feature extraction protocol. For instance, when using an intermediate feature with dimensions $256 \times 4 \times 4$, do the authors apply pooling before probing or directly flatten the representation? This question is important since ConvNets almost always have a feature dimension change across layers and this may contribute to the performance difference between intermediate features and last-layer features.

### Questions
Please see the Weaknesses.

### Soundness
3

### Presentation
3

### Contribution
2
