# Vulnerable Region Discovery through Diverse Adversarial Examples

- Decision: Reject
- Scores: 5, 8, 6

## Abstract
Deep Neural Networks (DNNs) have shown great promise in multiple fields, but ensuring their reliability remains a challenge. 
 Current explainable approaches for DNNs mainly aim at understanding DNNs’ behavior by identifying and prioritizing the influential input features that contribute to the model’s predictions, often overlooking \textit{vulnerable regions} that are highly sensitive to small perturbations. Traditional norm-based adversarial example generation algorithms, due to their lack of spatial constraints, often distribute adversarial perturbations throughout images, making it hard to identify these specific vulnerable regions. To address this oversight, we introduce an innovative method that uncovers these vulnerable regions by employing  adversarial perturbations at diverse locations. Specifically, our method operates within a one-pixel paradigm. This enables detailed pixel-level vulnerability assessments by evaluating the effects of individual perturbations on predictions. By leveraging the robust Sharing Differential Evolution Algorithm, we can simultaneously identify multiple one-pixel perturbations, forming a vulnerable region. We conduct thorough experiments across a variety of network architectures and adversarial training techniques, showing that our approach not only effectively identifies vulnerable regions but also provides invaluable insights into the inherent vulnerabilities present in a diverse range of deep learning models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
A one-pixel adversarial attack is an alteration to a single pixel that changes the network's prediction on an image.  If you take an image and repeatedly existing run one-pixel attacks, most of these runs will change the same pixel or small set of pixels.  In this paper, the authors are interested in identifying a large set of pixels that _each_ can be modified in such a way that fully changes the network's prediction.  To that end, the paper proposes an evolutionary algorithm that takes as input an image and a network, and returns a _set of distinct_ one pixel attacks that all succeed.  Often, these pixels are spatially clustered together, so the authors refer to this set of pixels as a "vulnerable region."  In section 4.4 authors argue that finding 'vulnerable regions' of an image can be one way to interpret a neural network.  (It seems to sometimes highlight very different regions than GradCAM.) The authors apply their method for finding vulnerable regions on both CIFAR-10 and ImageNet for both untargeted and targeted perturbations.

### Strengths
Originality: the paper is original, as I'm not aware of other methods for simultaneously finding distinct sets of one-pixel adversarial attacks

Quality: the paper is of reasonable quality

Clarity: most of the paper was clear, but I thought the abstract was confusing: "Traditional norm-based adversarial example generation algorithms, due to their lack of spatial constraints, often distribute adversarial perturbations throughout images, making it hard to identify these specific vulnerable regions." If I understand correctly, the proposed method does not have spatial constraints that encourage the found pixels to be close together.

Significance: I think the significance of the paper is a little unclear -- see below

### Weaknesses
1.  It's not clear to me what is the motivation for finding these vulnerable regions.  What will we do with them?  If the goal is explainability, why is this method conceptually better than other alternatives?

2.  As is hinted at in the paper, there is a conceptual problem with the idea of using groups of one-pixel adversarial attacks as a kind of interpretability method: as images get higher and higher resolution, the influence of each individual pixel get smaller, so one-pixel attacks get harder to find.  Ideally, an interpretability method shouldn't fall apart as the resolution gets higher.

### Questions
How would the authors respond to the two weaknesses listed above?>

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper introduces a novel approach to uncover vulnerable regions using
one-pixel perturbations located at various positions. Extensive experiments
involving various network architectures and adversarial training models have
been conducted, demonstrating that the proposed algorithm can indeed discover
diverse adversarial perturbations. Additionally, a large number of well-designed
experiments are conducted to study the properties of discovered regions, which
provide some interesting insights to deep models.

### Strengths
**1.** It is quite an interesting work. This paper provides a new perspective on
understanding the weaknesses of DNNs with diversely located perturbations. Specifically, this work focuses on pinpointing vulnerable regions to
single-pixel perturbations, distinguishing itself from interpretable methods
emphasizing significant areas influencing the network’s final output. This
approach facilitates the identification of specific vulnerable image areas
deserving more attention.

**2.** The paper conducts comprehensive experiments involving a range of network architectures and adversarial training techniques, clearly showcasing
how this method aids in assessing model vulnerability and contributes to
improving model interpretability. Experiment results demonstrate that
the proposed approach can effectively generate diverse adversarial perturbations to form vulnerable regions.

**3.** Beyond vulnerability detection, the paper also conducts a series of well-designed experiments to study the properties of the discovered regions,
e.g., how adversarial training influences the position of such vulnerable
regions. Overall, this approach leads to valuable insights into the behavior
of deep models, contributing to a deeper understanding of DNNs.

### Weaknesses
 **1.** The proposed approach exhibits limitations when applied to high-resolution
images. Even though the author increased the population size to 800 for
high-resolution images, this still only represents approximately 1.5% of the
total images. However, it requires up to 80,000 queries to deep models. This high query count, coupled with the small sampling percentage, raises concerns about the method's scalability and efficiency for larger, more complex datasets. The method's reliance on a large number of queries to identify vulnerable pixels makes it computationally expensive, potentially hindering its practical application in real-world scenarios with high-resolution inputs.

**2.**  It might be better if the author could briefly introduce adversarial training
in related works section. This would provide a more comprehensive context for the study, especially given the paper's focus on adversarial vulnerabilities. Without a discussion of adversarial training techniques, the reader may not fully appreciate the significance of the proposed method in the broader landscape of adversarial robustness research.

**3.** While the authors provide details on acquiring adversarial-trained models,
information on obtaining standard-trained models is lacking. This omission makes it difficult to reproduce the experiments and compare the results with other studies that use standard training procedures. The lack of clarity on the training process for standard models hinders the reproducibility and generalizability of the findings.

### Questions
This work provides a novel way to understand the weaknesses of DNNs, and
includes some well-designed, intriguing experiments. I have the following questions:

**1.** The experimental results reveal limitations when applied to high-resolution
images. On average, only around 20 diverse adversarial examples are found
for what the author refers to as vulnerable images. This number is relatively small. Is it possible to further adapt the method to high-resolution
images?

**2.** While understanding vulnerabilities is crucial, the paper may benefit from
discussing potential real-world scenarios where such vulnerabilities can be
exploited and their implications

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper utilize the Sharing Differential Evolution algorithm to come up with multiple signle-pixel adversarial attacks at diverse locations. The attack region reveals the vulnerable region in the input image.

### Strengths
1. The idea of utlizing single-pixel adversarial attack to highlight vulnerable region is interesting
2. The paper is overall well written and easy to follow
3. The paper make interesting observation on how adversarial training affect vulnerable region, and how teh region changes with different source/target classes

### Weaknesses
My major concern of the paper is the lack of technical contribution. As an attack, the proposed method is not effectively leading to high success rate, and is not well bounded (e.g. constraining the maximum number of pixels to be perturbed etc.) While as a visualization/explaination method, it is not well motivated/explained how the identification of vulnerable region can help better understand or improve the model. This hinders the significance of the paper.

### Questions
See weakness

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good
