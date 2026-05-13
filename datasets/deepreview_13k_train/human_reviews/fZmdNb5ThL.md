# ShiftAddAug: Augment Multiplication-Free Tiny Neural Network with Hybrid Computation

- Decision: Reject
- Scores: 6, 3, 3, 8

## Abstract
Operators devoid of multiplication, such as Shift and Add, have gained prominence for their compatibility with hardware.  
However, neural networks (NNs) employing these operators typically exhibit lower accuracy compared to conventional NNs with identical structures. \textbf{ShiftAddAug} uses costly multiplication to augment efficient but less powerful multiplication-free operators, improving performance without any inference overhead. It puts a ShiftAdd tiny NN into a large multiplicative model and encourages it to be trained as a sub-model to obtain additional supervision. In order to solve the weight discrepancy problem between hybrid operators, a new weight sharing method is proposed.
Additionally, a novel two stage neural architecture search is used to obtain better augmentation effects for smaller but stronger multiplication-free tiny neural networks.
The superiority of ShiftAddAug is validated through experiments in image classification and semantic segmentation, consistently delivering noteworthy enhancements. Remarkably,  it secures up to a 4.95\% increase in accuracy on the CIFAR100 compared to its directly trained counterparts, even surpassing the performance of multiplicative NNs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposed a network augmentation methods for muliplication-free (MF) convolutional neural networks (CNNs). The augmented part is multiplicative and only exists during training to "condition" the training of the multiplication-free part. During inference, the augmented part will be disgarded; hence the inference latency and energy efficiency will not be compromised.

A key technical contribution of this work is the heterogeneous weight sharing between the MF part and the augmented part. The intuition is the observation of the distribution shift of the trained weights in the two parts. The authors proposed to use the so called "heterogeneous weight sharing with remapping" that maps the original conv weights to those in the MF convs so that the remapped weights approximately follow a Laplacian distribution. This weight sharing technique is essential for the success of the proposed method.

The authors conducted a number of experiments to show the effectiveness of the proposed method.

### Strengths
+ The idea of conditioning MF network training via network augmentation is interesting. While this idea is not new as the authors discussed in the related work section, the authors identified a unique numerical issue encountered when applying the methodology to MF network training, that is the weight tearing issue --- the inconsistency of weight distribution between the MF and mulicative parts. Solving this issue brought significant boost in performance to the proposed method.

### Weaknesses
 **Clarity**. As the most important part of this work, the elaboration on the heterogeneous weight sharing technique is not clear enough. I feel confused about several parts of the technique when I was reading the paper.
- Between which two parts are the weights shared, and how? The authors are not quite clear (mathematically and technically) about this. According to the authors description, I guess the augmented convs (multiplicative) contain the original weights. The weights are mapped to those in the ML convs using Eqn (5).
- If my understanding is correct above, does it mean the augmented conv has to be in the exactly same size as the MF conv? If so, how do the [2.2, 2.4, 2.8, 3.2] multiples in Tab. 2 work for the NAS part?
- Is it correct understanding that there are no actually weights stored for MF part during training; instead they are generated with mapping (5) instantly? 
- What is the consideration of adding a learnable FC layer in (5)? From my understanding, there are analytical way that maps data points from a Gaussian dist. to Lap dist, like optimal transport?
- Are the weights rounded to powers of 2 for ShiftConv?

**Experiment design**.
- The plain multiplicaive augmentation seems only to hurt the MF part without the heterogeneous weight sharing technique. Another possibility is that the weight sharing technique plays a role as a special parameterization trick. What if we only apply the parameterization without augmentation? Will this improve the performance?
- The MF augmentation seems to work well itself. Is the weight sharing also applied for this baseline? If so, what if we relax it? The point here is to see how the performance improves just by increasing the width of a MF network.

**Overall writing quality**. While the overall flow of the paper is ok, there are writing issues here and there. A incomlete list of issues:
- The ShiftAddAug-NAS row in Table 3 is missing. The MobileNetV3 Add/AddAug accuracy data is also missing without clarification.
- The punctuations and capitalizations in many places are wrong.
- The names of the compared methods are confusing. I recommend the authors use a dedicated paragraph to clarify the naming of counterparts compared in the experiments.

### Questions
See the weaknesses part.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper proposes to augment shiftadd operation kernel based training with traditional multiplication kernel based training to improve the performance of CNNs while doing inference with only shiftadd ops.

### Strengths
1. The idea of leveraging shiftAdd operation to improve compute bottleneck of CNNs is a useful and effective direction.

2. The paper is written well, apart from few sentences, example: the last sentence of related work (on NAS)

### Weaknesses
1. The paper's contribution needs improvement. The current draft is heavily based on ShiftAddNet and ShiftAddNAS.

2. In the abstract the authors compared the energy performance with traditional DNN, however, it should have been ShiftAddNet, if there is any. As it is already understandable due to the earlier publications in this line that shift-add ops based computation would incur energy saving over MAC based computation.

3. The idea of augmenting the training shiftadd kernel with multiplicative kernel would incur additional training compute and storage overhead, thus essentially altering the training recipe of the baseline shiftadd methods. Additionally, on device training and fine-tuning is a largely growing field, which is basically demeaned by this style of training compared to that of shiftaddnet.

4. Interestingly shiftAddNAS can be assumed as a superset of this work, which not only proposes the option of multiple compute kernel types, but also searches over them based on resource budget. Thus, I find it very hard to appreciate the current work in its current format.

5. The results are not comprehensive and the comparison baselines are not proper. The paper should be compared with ShiftAddNAS, ShiftAddNet, AdderNet, NetAug etc. Though having more comparisons are good, however, I am not sure why the authors compared with MCUNet, as there is already the next version in that family published > 1 year back,  MCUNet v2.

6. Results on ImageNet are incomprehensive.

7. Table 3 last row is not filled in!

### Questions
Please see weaknesses.

### Soundness
2 fair

### Presentation
1 poor

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work targets better accuracy vs. efficiency trade-offs for multiplication-free tiny neural networks. Specifically, it uses multiplication-based Conv in training to augment Shift-based Conv and Add-based Conv optimization for higher accuracy in the Shift/Add-based networks. The experiments on image classification tasks show the proposed ShiftAddAug framework can have higher accuracy (e.g., +4.05% on CIFAR-100) while reducing energy consumption (e.g., 68.9% reduction) as compared to multiplication-based networks.

### Strengths
1. Motivation: Current tiny DNNs are primarily designed using multiplication-based operators, often overlooking the more energy-efficient shift and add operators. Exploring shift/add-based tiny DNNs is, therefore, a worthwhile endeavor. 

2. Comprehensive Review of Related Works and Preliminaries: The section on related works thoroughly covers existing multiplication-free networks. Additionally, the preliminaries provide a clear explanation of the shift and add operators utilized in this work. 

3. Clear and Understandable Figures: The figures presented are clear, making the entire paper straightforward and easy to follow.

### Weaknesses
1. Quality of the Draft: It appears the authors may not have thoroughly proofread their draft before submission. In Table 3, the performance of the proposed ShiftAddAug is denoted as "xx". This is a crucial detail for comprehending the efficacy of the suggested framework.

2. Ambiguity in the Contribution of the Proposed NAS: From the details provided in Sec. 3.4, the introduced NAS, which is highlighted as the third contribution, seems to essentially apply tinyNAS (Lin et al., 2020) over the ShiftAddAug. The search space is presented in Table 2 without clarifying its design rationale. Consequently, the true value-add of the proposed NAS remains ambiguous.

3. Unclear Contribution of the Weight Sharing Strategy: The weight-tearing issue that the proposed weight sharing strategy addresses is previously identified in ShiftAddNAS (You et al., 2022). The weight mapping strategy delineated in Eq. 5 is similar to the approach in ShiftAddNAS, which employed a learnable transformation kernel, T (·), to transition shared weights from a Gaussian to a Laplacian distribution. However, there are no theoretical justifications or empirical findings illustrating why this strategy outperforms the one in ShiftAddNAS.

4. Concerns on the Accuracy of the Efficiency Metric: As mentioned in Sec. 4.1, the efficiency metric chosen for this study is the energy and latency reported by an Eyeriss-like hardware accelerator simulator. However, the referenced studies (Chen et al., 2017; Zhao et al., 2020) are designed for multiplication-based networks. The authors have overlooked elaborating on the specific modifications implemented to adapt the simulator for multiplication-free networks. Given this, it's debatable if the evaluation backdrop is fair for multiplication-based networks. A recommendation for the authors would be to utilize more reproducible metrics, such as the latency from the TVM-based Shift/Add execution in ShiftAddViT (You et al., 2023).

### Questions
Besides the previously listed weaknesses, I have the following questions:

1. The experiments exclusively consider the image classification task. How can it be asserted that this is the dominant task for IoT devices?

2. As indicated in Tab. 5, when introducing multiplication into the search space, the proposed ShiftAddAug displays a reduced accuracy compared to the baseline ShiftAddNAS (You et al., 2022). The given justification, which states "our method has given the multiplication-free operators strong capabilities, bridging the gap to the original operator", appears inconsistent. Notably, the ShiftAddNAS baseline actually boasts a similar count of Mult, Shift, and Add parameters. If the assertion were accurate, ShiftAddAug should outperform ShiftAddNAS in terms of accuracy. It seems more plausible that ShiftAddAug adversely affects the efficacy of multiplication-based operators. If this is the case, an exclusive emphasis on shift/add-only networks might be misplaced, as the existing multiplication hardware in IoT devices would remain underutilized.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces "ShiftAddAug," a novel approach for training multiplication-free neural networks aiming to reduce energy costs. ShiftAddAug leverages costly multiplication operations during the training phase to enhance the activation of multiplication-free operations. These multiplication operations are subsequently deactivated during inference to avoid additional computational expenses. Additionally, the authors have developed a hardware-aware neural architecture search strategy rooted in a hybrid computing augmentation search space. This strategy dynamically reduces parts of the models to comply with specific hardware constraints throughout the training process. The results obtained from benchmarks such as CIFAR10/100 and ImageNet-1k, among others, demonstrate robust performance and significant gains in energy efficiency.

### Strengths
I appreciate the logical structure and clarity of this paper. The authors present their motivations compellingly, and the proposed ShiftAddAug method is both intuitive and seemingly effective, as evidenced by the strong results reported.

### Weaknesses
I have several questions that I hope the authors can clarify and expand upon to better understand the nuances of ShiftAddAug:

1. Could you elucidate how ShiftAddAug augments a baseline model? Specifically, in the context of convolutions, are additional channels created for multiplication-free (MF) operations on top of the existing ones? Or is there a division of existing channels between multiplicative and MF operations? It's unclear how the channel-wise split is managed and whether it's a static or dynamic assignment.

2. Regarding the dedicated input channels for shift/add operations, are they fixed throughout the training process? Figure 1 suggests the presence of a "gate" that directs input features, but this mechanism isn’t elaborated upon in the paper. It's not clear if this gate is a learnable parameter or a fixed assignment, and how it interacts with the channel splitting mentioned in the first point.

3. While the concept of heterogeneous weight sharing is intriguing, its practical application during training remains unclear. Are multiplication (M) weights dynamically mapped to MF weights, implying that operations aren't tied to specific input channels? If so, what determines the allocation of operations to particular channels? The paper lacks detail on the mapping function and how it ensures effective transfer of knowledge from M weights to MF weights, especially given their different computational properties.

4. After the neural architecture search (NAS) process, is further retraining of the resultant models necessary to achieve optimal performance? Does the performance reported in Table 5 directly stem from the NAS search, or is it the result of additional training? This distinction is crucial for understanding the true contribution of the NAS strategy versus standard fine-tuning.

5. Could the authors clarify the purpose of the last row in Table 3? It's unclear what this row represents and how it relates to the other results presented in the table.

6. Regarding the behavior during inference, it's clear that multiplicative operations can be disabled, but can they also be entirely removed? The paper doesn't explicitly guarantee alignment between input/output channels among MF channels. Given this, are there concerns about potential computational waste due to this misalignment? It's unclear if the network structure is modified to remove the multiplicative branches, or if they are simply bypassed, which could lead to inefficiencies.

### Questions
see weaknesses

### Soundness
3 good

### Presentation
4 excellent

### Contribution
4 excellent
