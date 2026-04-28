# PRE-TRAIN WITH BACKPROPAGATION AND FINE-TUNE  WITH A BIO-PLAUSIBLE LEARNING RULE

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Backpropagation (BP) has long been the cornerstone of deep neural network training. While neural networks trained with backpropagation typically have high accuracy and precision, they suffer from limitations in their robustness to adversarial perturbation. Biologically plausible (bio-plausible) learning rules, on the other hand, are more robust. Yet, they typically underperform in terms of accuracy and precision, which has limited their widespread adoption. In this work, we aim to bridge this gap. We propose a novel approach where neural networks are pre-trained using backpropagation and fine-tuned using bio-plausible learning rules. We use several types of Sign-Symmetry learning methods to fine-tune models pre-trained using backpropagation. We explore the effectiveness of this approach in two tasks, image classification and image retrieval, then demonstrate that it improves robustness against gradient-based adversarial attacks while offering comparable accuracy and precision compared to the use of backpropagation alone. These findings show the benefit of mixing backpropagation and bio-plausible learning rules, suggesting the need for further research by the community to evaluate this approach on other tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents an approach combining traditional backpropagation for pre-training and bio-plausible learning rules, specifically Sign-Symmetry, for fine-tuning. The authors argue that this hybrid training method results in models that are more robust to gradient-based adversarial attacks compared to standard backpropagation-only models, while achieving similar accuracy and precision.

### Strengths
The experimental results convincingly demonstrate the approach’s increased robustness against adversarial attacks. This aligns with the authors’ intent to mitigate backpropagation's vulnerability, leveraging bio-plausible learning's inherent resilience.

The paper integrates backpropagation and bio-plausible methods, showing that such a hybrid model can preserve performance while enhancing security against adversarial examples. This is a promising area for further exploration in the community.

The experiments cover multiple backbone architectures, learning rules, and datasets, providing a comprehensive view of the proposed approach's effectiveness across different settings.

### Weaknesses
The motivation for pre-training on ImageNet and then fine-tuning on ImageNet100 could use clarification. It’s unclear why a smaller dataset subset was chosen for fine-tuning, as this could introduce a slight overfitting risk with backpropagation, affecting robustness. It would also be helpful to see comparisons with results before fine-tuning, particularly regarding robustness metrics.

The term "fine-tuning" might be more accurately described if it involves "training the downstream task with unfrozen backbone weights," as suggested by the unclear distinction between backpropagation and bio-plausible stages. Making this distinction explicit would clarify the contribution.

The work by Sanfiz & Akrout (2021), used as a basis for some assumptions, is not peer-reviewed. While this may not significantly affect the paper’s core findings, it would be beneficial to rely on more robustly vetted sources where possible.

Figure 1's visualization of weight transport methods is not intuitive. The arrow representation could be misleading, as it does not clearly illustrate the differences in weight transport between backpropagation and bio-plausible methods. A more structured schematic detailing learning rules and their weight transport levels would improve clarity.

Although the paper claims to open-source the code, no direct link or supplemental is provided. Including a repository link would make replication easier for the community.

Adding explicit units (e.g., [%] for accuracy) in the tables would improve clarity. While it’s often implicit, making this explicit could aid comprehension.

### Questions
Could you clarify the choice of pre-training on ImageNet and fine-tuning on ImageNet100? This choice seems unconventional, as it might introduce overfitting concerns or limit the evaluation’s generalizability.

When you refer to "fine-tuning," are you adjusting all model weights, including the backbone, with bio-plausible methods? Or is this term meant to describe training for downstream tasks with specific layers?

Figure 1’s arrow representation of weight transport is somewhat ambiguous. What does the arrow signify in terms of the amount of weight transport across methods?

Could you confirm that accuracy and mean average precision are presented in percentage terms in the tables?

The robustness analysis includes standard gradient-based attacks like FGSM and PGD, but no specialized attacks for bio-plausible learning methods. How might these attacks perform differently if evaluated against attacks tailored specifically to the Sign-Symmetry methods?

Could you provide an alternative visualization comparing learning rules and weight transport? Perhaps a comparison matrix or schematic diagram that delineates key differences?

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
4

### Summary
The paper investigates an alternative training method for deep neural networks to address the robustness limitations of traditional backpropagation (BP). Specifically, it proposes a hybrid approach where neural networks are pre-trained with BP for initial accuracy and then fine-tuned using biologically plausible learning rules, particularly Sign-Symmetry methods (uSF, frSF, brSF). This fine-tuning method aims to enhance robustness against adversarial attacks without sacrificing the accuracy obtained through BP. The paper tests this method across multiple neural network architectures (AlexNet, VGG16, ResNet-18) on tasks including image classification and hashing-based image retrieval, demonstrating improved adversarial robustness while retaining accuracy levels comparable to standard BP training.

### Strengths
The approach of pre-training with BP and fine-tuning with bio-plausible learning rules is interesting and presents a promising path toward enhancing robustness in neural networks.

The experiments are well-designed, with comprehensive comparisons across different architectures, learning rules, and tasks.

The findings demonstrate that bio-plausible learning can play a critical role in improving adversarial robustness, which could inspire further research in bio-inspired ML methods.

### Weaknesses
The proposed method's robustness against adversarial attacks is limited to specific gradient-based attacks (FGSM and PGD). Testing on additional types of attacks, including non-gradient-based ones, would have helped in better understanding the limitation.

Some sections on bio-plausible learning rules and their relationship to robustness could benefit from a more detailed explanation to provide a clearer understanding of why these methods improve adversarial robustness.

While the chosen datasets are common benchmarks, including a wider range of datasets could enhance the robustness of claims’ generalizability.

### Questions
Can you elaborate on the choice of datasets used for testing? Were they selected based on specific characteristics that highlight the strengths of your approach?

How does your method perform in scenarios involving non-gradient-based adversarial attacks?

What are the potential limitations or drawbacks of using bio-plausible methods in other domains or applications?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper is an attempt to propose a biologically plausible alternative solution to backpropagation that has been dominating the deep learning training for a few decades. Although biologically plausible learning methods are more robust to perturbation and more insightful of human learning, they are known to be significantly worse than backpropagation in performance evaluated by standard metrics (accuracy for classification, dice score for segmentation, mIoU for detection, etc.). In this paper, the authors aim to design a biologically plausible learning method that performs on par with backpropagation. Specifically, they propose pre-training with backpropagation and fine-tuning with biologically plausible Sign-Symmetry learning rules, and show that on image classification and image retrieval, the resulting models are more robust to perturbations from gradient-based adversarial attacks while performing comparably in standard metrics.

### Strengths
1.	The general topic of biologically plausible alternative to backpropagation is of interest to both machine learning and neuroscience communities.
2.	The background on adversarial attacks and adversarial robustness is helpful.
3.	The authors could further highlight the fact that they are directly tuning the publicly available models pre-trained on ImageNet, which means the proposed method is relatively efficient.

### Weaknesses
1. I find the results presented quite alerting. **If I understand it correctly, in Table 1, the authors claimed that they could achieve 100.0% accuracy on ImageNet classification using backpropagation with VGG16 backbone.** I strongly doubt they are either presenting the train accuracy instead of the test accuracy or they are making other serious mistakes. I would like to encourage the authors to double check that and provide justification if my suspicion does not hold.
2. The backbones being experimented are AlexNet, VGG16, and ResNet-18, and the first two are unfortunately no longer the mainstream backbones in recent years. I would recommend the authors provide rationale for choosing them rather than backbones such as Vision Transformer, ConvNeXT, etc.
3. It would be especially helpful if the authors can go deeper on the insights on why training from scratch using Sign-Symmetry methods are subpar whereas finetuning using Sign-Symmetry methods from backpropagation-based pretrained weights are showing competitive performance. Insights into this phenomenon, especially if can be explained from a neuroscience perspective could be extremely interesting. With that said, everything has to rely on the fact that the results are reliable --- refer to Weakness 1.

### Questions
Please see questions 1 and 2. I would encourage the authors to directly respond to them, especially 1.

### Soundness
2

### Presentation
3

### Contribution
2
