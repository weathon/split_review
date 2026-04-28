# Leveraging Hierarchical Feature Sharing for Efficient Dataset Condensation

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
Given a real-world dataset, data condensation (DC) aims to synthesize a small synthetic dataset that captures the knowledge of a natural dataset while being usable for training models with comparable accuracy. 
Recent works propose to enhance DC with {\em data parameterization}, which condenses data into very compact parameterized data containers instead of images. 
The intuition behind data parameterization is to 
encode \emph{shared features} of images to avoid additional storage costs.
In this paper, we recognize that images share common features in a hierarchical way due to the inherent hierarchical structure of the classification system, which is overlooked by current data parameterization methods.
To better align DC with this hierarchical nature and encourage more efficient information sharing inside data containers, we propose a novel data parameterization architecture, \emph{Hierarchical Memory Network (HMN)}.
HMN stores condensed data in a three-tier structure, representing the dataset-level, class-level, and instance-level features.
Another helpful property of the hierarchical architecture is that HMN naturally ensures good independence among images despite achieving information sharing.
This enables instance-level pruning for HMN to reduce redundant information, thereby further minimizing redundancy and enhancing performance.
We evaluate HMN on five public datasets and show that our proposed method outperforms all baselines.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new method called Hierarchical Memory Network (HMN) that stores condensed data in a three-tier structure that reflects the hierarchical nature of image data. The authors exploited that HMN naturally ensures that generated images are independent and proposed a new algorithm to remove redundant images. The authors evaluated the model on four different datasets, and showed that their technique outperformed several SoTA baselines.

### Strengths
1- The paper proposed a new algorithm to store condensed data in a three-tier memory structure: dataset-level, class-level, and instance-level.
2- The authors proposed a pruning algorithm to prune redundant examples.
3- The authors demonstrated the effectiveness of their method on 4 different datasets. Their method outperformed several SoTA baselines by convincing margines.

### Weaknesses
1- It is difficult to follow some of the ideas presented in the paper. For example, the paper didn't mention the abbreviation for IPC. Also, the paper didn't talk about whether the decoder parameters is part of the budget or not.

2- The paper demonstrated the effectiveness of their method on tiny datasets, and they didn't address the scalability of their technique. For example, the generated images seem very pixelated and abstract, how does their method perform in a more complex settings.

### Questions
Table.1 What is the accuracy drop for randomly pruning 10% ?

Algorithm 1.  are you computing the accuracy in an online fashion, or you train the model for each subset selection? How this would scale for larger datasets?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper works on the task of dataset condensation, i.e., producing a data generator whose generated data can be used to train a network that retain similar performance with respect to using a full dataset. The authors proposed a novel hierarchical data generation pipeline, which starts from a dataset level feature, then go through class-specific feature processing layers, and instance-level feature processing layers, and a uniform decoder to decode the features into images. Experiments show the proposed method achieves good performance on 3 benchmarks, on-par or out-performing methods with more expensive computes.

### Strengths
- The task of dataset condensation is an important and interesting task. This paper provide a good summarization of existing literature, and make solid progresses to this field.

- The proposed methods of hierarchical memory decoding is intuitive and makes a lot of sense to me. The followup pruning technique is also clean.

- Experiments show the proposed method work well on different benchmarks with different data budgets, outperforming existing methods which use more computes during training.

### Weaknesses
 - The authors highlighted that they are using a more efficient training loss "batch-based", and claim it is sufficient to outperform a better but more expensive training loss "trajectory-based". It is unclear whether the proposed method could be further improved by using the "trajectory-based" loss, or if the method's architecture inherently prevents its use due to computational constraints. The paper should discuss the potential limitations of the proposed method when combined with more computationally intensive training losses. Specifically, it would be beneficial to understand if the hierarchical memory network's (HMN) memory footprint or computational complexity is a bottleneck when using trajectory-based loss, and if so, what specific aspects of the architecture contribute to this limitation.

- As a researcher not working on this field, I had a hard time understanding what "IPC" means in experimental setup. Through searching other papers I get it is "Images allocated Per Class". It would be good if the paper can be more self-contained, to introduce this setting in the paper, and provide background knowledge on why this is used as the main setting. A more intuitive setting in my mind (without knowing the literature) is control the number of parameters of the learned data generators. Is this the same as the setup used in the paper? The paper should explicitly define IPC and explain its relevance within the context of dataset condensation. It should also clarify the relationship between IPC and the number of parameters in the data generators, as these are not necessarily equivalent. For example, are the parameters of the generators fixed, or do they scale with IPC? If they scale, how does this impact the overall memory footprint and computational cost?

### Questions
Overall this paper proposed a novel and valid method on an important task, with solid results. My questions are mostly for clarification, as I don't work on this field. I am happy to vote for an accept for now, conditioned on the authors clarifying my confusions in paper weaknesses during the rebuttal.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a novel data parameterization architecture named Hierarchical Memory Network (HMN), which consists of dataset-level, class-level, and instance-level memory and a feature extractor and a decoder to better leverage the hierarchical nature of the image. Furthermore, the paper proposes instance-level pruning to remove redundant images to improve performance.

### Strengths
1. The paper proposes a novel framework for DC with data parameterization, instead of updating input images, they update the memory (i.e, dataset, class, and instance) and decoder.
2. Identify the redundancy in condensed images using AUM and suggest to first condense images with over-budget (p%) and then perform post-condensation pruning to remove redundant data.

### Weaknesses
Although the proposed method (including HMN and condensed over-budged & pruning) is novel, there are several weaknesses:

1. Lack of experiments on higher resolution such as 128x128 (Image Woof/Nette) or 224x224 (ImageNet-10/100, a subset from ImageNet, as done in IDC)
2. Lack of describing the memory in detail. For example, how does the memory look like?
3. The evaluation seems to be different from previous works. For example, HMN evaluates condensed images with a cosine annealing learning rate (LR) scheduler, while DSA or IDC uses a multistep LR scheduler. Thus, the comparison may not be fair.
4. The evaluation time of HMN is much longer than DC approaches such as DSA or even IDC. For example, with CIFAR-100 and 50 IPC, the GIPC is 673, meaning that 673 images are generated for one class. However, CIFAR-100 only has 500 images per class. Hence, in the evaluation phase, the training time of HMN is longer than using the original images. Moreover, HMN achieves lower performance than using the original images. The only advantage of HMN I can see is that we can reduce the storage size.
5. In Table 2, the result of IDC on CIFAR-10 with 50 IPC is lower than in the paper (74.5 (IDC) vs 71.6 (this paper)). Is it a mistake?  On CIFAR-100, this paper reports the accuracy of IDC with 10 IPC on CIFAR-100 is 44.8 while on other papers such as DREAM, the accuracy is 45.1. Can the author double-check? The results of IDC (at 10 and 50 IPC) in Table 2, Table 3, and Table 6 are different. Can the author explain?
6. As shown in Figure 4 (right),  with an instance memory size near 100, around 600 images per class are generated. How many images per class (per epoch) are used for training in the evaluation phase? 600? If this is correct, the training time with condensed images is much longer than the conventional method where the total images per lass are set as the IPC. Can the author clarify this?

### Questions
I have several questions:
1. What does the memory look like? How to initialize these memories, feature extractor, and decoder?
2. HMN stores parameters instead of images, this will incur extra resources for evaluation (to generate images). Is it correct?
3. How many generated images per class  (GIPC) used in Table 2? 
4. In Table 2, the result of IDC on CIFAR-10 with 50 IPC is lower than in the paper (74.5 (IDC) vs 71.6 (this paper)). Is it a mistake?  On CIFAR-100, this paper reports the accuracy of IDC with 10 IPC on CIFAR-100 is 44.8 while on other papers such as DREAM, the accuracy is 45.1. Can the author double-check? The results of IDC (at 10 and 50 IPC) in Table 2, Table 3, and Table 6 are different. Can the author explain?
5. As shown in Figure 4 (right),  with an instance memory size near 100, around 600 images per class are generated. How many images per class (per epoch) are used for training in the evaluation phase? 600? If this is correct, the training time with condensed images is much longer than the conventional method where the total images per lass are set as the IPC. Can the author clarify this?

Although the proposed method is novel and seems promising, there are unclear parts regarding the GIPC, the memory, and fairness in evaluation comparison. Additionally, some reported results of IDC of this paper are different from those in the original paper without explanation. Thus, I give a borderline reject.

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a novel dataset condensation method following the data parameterization approach. The key idea is to use the newly designed Hierarchical Memory Network (HMN) to learn a three-tier representation of the condensed dataset. Experimental results demonstrate the effectiveness of the proposed method.

### Strengths
- The idea proposed is interesting and novel.
- The paper is well-written and easy to follow.

### Weaknesses
 - It lacks a discussion and comparison to a very relevant SOTA method, i.e., IDM [1], which also addresses the scalability of data condensation and works in a low GPU memory cost scenario. Thus, it might be incorrect to argue that the proposed method is the "first method to achieve such good performance with a low GPU memory loss" and such statements should be revised.

- The technical novelty is a bit thin. Specifically, the second contribution is relatively weak and more similar to a trick. It is interesting to know that over-budget generation and pruning may work, but this is more similar to remedying some of the shortcomings of the main idea rather than an independent contribution.

### Questions
Please see the weaknesses above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
