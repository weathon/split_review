# Improving Neural Network Accuracy by Concurrently Training with a Twin Network

- Decision: Accept
- Scores: 5, 5, 8, 8

## Abstract
Recently within Spiking Neural Networks, a method called Twin Network Augmentation (TNA) has been introduced. This technique claims to improve the validation accuracy of a Spiking Neural Network simply by training two networks in conjunction and matching the logits via the Mean Squared Error loss. In this paper, we validate the viability of this method on a wide range of popular Convolutional Neural Network (CNN) benchmarks and compare this approach to existing Knowledge Distillation schemes. Next, we conduct a in-depth study of the different components that make up TNA and determine that its effectiveness is not solely situated in an increase of trainable parameters, but rather the effect of the training methodology. Finally, we analyse the representations learned by networks trained with TNA and highlight their superiority in a number of tasks, thus proving empirically the applicability of Twin Network Augmentation on CNN models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the Twin Network Augmentation (TNA) method, originally proposed for Spiking Neural Networks, and evaluates its effectiveness on Convolutional Neural Networks (CNNs). The authors show that concurrently training two networks and matching their logits using Mean Squared Error (MSE) loss improves validation accuracy across various CNN benchmarks. They compare TNA to traditional Knowledge Distillation methods, highlighting its superior performance and robustness.

### Strengths
This paper conducts extensive experiments to demonstrate that training two twin networks with the same objective, while simply minimizing the mean squared error of their output logits, can significantly enhance the performance of a single network. The primary contribution of this paper lies in validating the effectiveness of this approach not only for SNNs but also for CNNs.

### Weaknesses
1. This paper simply transfers the method from reference [1] to traditional CNNs, showing some performance improvement based on the experimental results. Although the authors conducted a wide range of experiments from different angles to validate its effectiveness, the overall contribution lacks novelty. In other words, the only modification was replacing SNNs with CNNs, which is trivial.

2. This method is only validated on the classification task and is only compared with the outdated backbones.

### Questions
1. The application of mean squared error (MSE) loss on logits enhances performance but doubles the training parameters when using twin networks like ResNet-18. It is essential to assess whether ResNet-18 serves as a reasonable baseline, especially in comparison with models that have similar parameter counts. The objective should be to establish a computationally feasible baseline.

2. Although Section 4.2 offers some intuition for the performance improvements, a more rigorous theoretical analysis is required to enhance understanding of the underlying mechanisms.

3. The writing of this paper should be largely improved. For example, lines 58 and 187 must utilize `\citep` for proper citation formatting. Additionally, both Figure 5 and Table 10 are missing concluding periods, and line 630 must also end with a period for consistency.

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
3

### Summary
This paper first introduce Twin Network Augmentation (TNA) from SNN, then validate the viability of this method on a wide range of popular CNN benchmarks and compare this approach to existing Knowledge Distillation schemes.

### Strengths
This paper introduces the TNA method from the SNN field into CNNs for the first time, demonstrating its applicability across a variety of CNN models. The TNA method improves overall performance by simultaneously optimizing two networks and using MSE loss to adjust their logits.

### Weaknesses
1.This paper validates the feasibility of the TNA method in the CNN field. Although the experiments in this paper are comprehensive, they do not sufficiently analyze the reasons why the TNA method is feasible. Considering that this paper does not propose a new method, I doubt whether the work meets the standards of the ICLR conference.

2.Could the author explain why TNA is superior to DML? According to Tables 2 and 7, TNA only surpasses DML under special alpha values.

3.TNA requires training two networks simultaneously, resulting in doubled training costs. How to balance these costs against performance gains?

4.Section 4.3 and Table 5 are confusing. Please clarify what each column in Table 5 represents.

### Questions
Why does Eqn. 2 not align with the DML loss described in Figure 1 (b)?

### Soundness
2

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
The authors implement a new method called Twin Network Augmentation (TNA) for CNNs that improves the downstream performance by training two networks in parallel and using their logits in a combined loss function. The loss function consists of the cross entropy loss of each network's output with a given label and the mean squared error of the network's logits. 
They compare their method with already established methods like Deep Mutual Training, as well as the standard machine learning approach with similar or larger networks (i.e. wide resnet compared to resnet with TNA).

### Strengths
The paper is written very well and easy to understand. The mathematical concepts are accessible and understandable. All the experiments align closely with the descriptions in the paper, effectively illustrating the theoretival insights. Notably, the paper includes a refreshing variety of experiments in the ablation studies, offering a comprehensive analysis of the TNA approach.

### Weaknesses
Major:
- Tables and figures could benefit from more detailed captions, specifying, for example, the network and dataset used. While all relevant information is present in the text, including it in the captions would enhance clarity and accessibility.
- The rationale behind the choice of data sets for specific instances is not always clear.

Minor:
- Tables 3 and 4 appear to be very small.
- For Figure 2, a bar plot may be more suitable.
- Table 7 may be improved by introducing a column with an alpha value of 0.

### Questions
1. In 3.3, describing the network architectures (i.e. ResNet-18, ResNet-50,...) and corresponding datasets: Usually, for small images (e.g. 64x64 in Tiny ImageNet) the first 7x7-conv-layer of a ResNet is swapped for a smaller 3x3-conv-layer without stride. Did you follow this protocol?
2. Tables 1 and 2 use the terms 'Default Train' and 'Single Train,' respectively. Is there a distinction between the two?
3. Both the base and twin networks currently receive the same image. Have you considered applying slightly different augmentations to each network, as is commonly done in contrastive learning approaches like SimCLR (https://arxiv.org/abs/2002.05709)?
4. In 4.4.1, why does a larger alpha result in networks that perform no better than random chance? High values of alpha (much greater than 1) inherently produce larger gradients, necessitating an adjustment in the learning rate. Could this be a contributing factor to poor performance?
5. In section 4.4.4, you investigated late matching. Have you thought about 'warming up' the alpha (e.g. exponentially)?
6. In the right-side plot of Figure 5, the curve for late matching at epoch 150 appears to decline independently, even before matching. What does the logit matching loss look like in the absence of any matching?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper investigates the potential use of Twin Network Augmentation (TNA), originally used to train spiking neural networks, in conventional CNNs trained for image classification in standard benchmarks such as CIFAR and ImageNet variants. The narrative then moves on to in-depth analyses of learning dynamics and ablation studies.

### Strengths
This paper is rigorous with a large number of convincing experiments and results. I appreciate the literature review of all similar methods and the summary provided in Figure 1 (even though it seems like they are a little too similar to have such drastically different names).

### Weaknesses
- Table 1 is quite chaotic. I can roughly understand why ResNet-18 is trained on TinyImageNet while ResNet-50 is trained on ImageNet and so on, but this is not rigorous or scientific, and can give the impression that the authors are simply cherry-picking results (I do not think this is the case). It would be better to keep one thing constant (network or dataset) and perform your experiments. (4 networks x 4 datasets is really only 16 cases, perhaps the authors can consider running them all).

- There seems to be a lot of attention placed on DML. Did the original TNA paper also compare DML and TNA for spiking networks? If so, any different observations found for spiking networks vs conventional CNNs? If not, why is so much analysis placed on DML? To be more specific, knowing that TNA is different from DML does not tell me anything more about TNA, which is the focus of this paper.

- I might have missed this in the paper, but in the conclusion the authors claim that "the performance increase when training with TNA is linked to the matching of logits" but isn't matching the softmax pretty much just matching a non-linear function of the same quantity?

### Questions
- Did the original TNA paper talk about anything in Figure 1? Or is this an original attempt at unifying all the ideas?

- I might have missed this in the paper, but in the conclusion the authors claim that "the performance increase when training with TNA is linked to the matching of logits" but isn't matching the softmax pretty much just matching a non-linear function of the same quantity?

### Soundness
3

### Presentation
3

### Contribution
3
