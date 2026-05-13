# Less is More: Learning Reference Knowledge Using No-Reference Image Quality Assessment

- Decision: Reject
- Scores: 5, 3, 3, 5

## Abstract
Image Quality Assessment (IQA) with reference images has achieved great success by imitating the human vision system, in which the image quality is effectively assessed by comparing the query image with its pristine reference image. However, for the images in the wild, it is quite difficult to access accurate reference images. We argue that it is possible to learn reference knowledge under the \emph{No-Reference Image Quality Assessment} (NR-IQA) setting, which is effective and efficient empirically. Concretely, by innovatively introducing a novel feature distillation method in IQA, we propose a new framework to learn comparative knowledge from non-aligned reference images. Then, we further propose inductive bias regularization to inject different inductive biases into the model to achieve fast convergence and avoid overfitting. Such a framework not only solves the congenital defects of NR-IQA but also improves the feature extraction framework, enabling it to express more abundant quality information. Surprisingly, our method utilizes less input—eliminating the need for reference images during inference—while obtaining more performance compared to some IQA methods that do require reference images. Comprehensive experiments on eight standard IQA datasets show that our approach outperforms state-of-the-art NR-IQA methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper seeks to solve the no-reference image quality assessment issue with the help of distilled reference knowledge while eliminating the direct use of reference images. As such, they propose the Reference Knowledge-Guided Image Quality Transformer scheme that guides a student model to emulate the teacher's prior knowledge. Besides, to mitigate the weakness in local structures and inductive biases of ViTs, they further propose a Masked Quality-Contrastive Distillation method, benefiting from both CNNs and INNs.

### Strengths
The proposed model achieves some promising results compared to NR IQA methods, even with some FR peers.
The complementary strategy between ViTs and CNN/INNs is creative.

### Weaknesses
1. The idea of utilizing pseudo reference images, including both image-level or feature-level and both content-relevant or -irrelevant settings, in no-reference image quality assessment methods has been a longstanding topic all the time. The mentioned flaws of the listed relevant works Liang 2016 and Yin 2022 (the third paragraph of the Introduction), i.e., requiring suitable high-quality images as references during quality inference, have been widely noticed and addressed in the related works such as:
[1] Chen B, Zhu L, Kong C, et al. No-reference image quality assessment by hallucinating pristine features[J]. IEEE Transactions on Image Processing, 2022, 31: 6139-6151.
[2] Tian Y, Chen B, Wang S, et al. Towards Thousands to One Reference: Can We Trust the Reference Image for Quality Assessment?[J]. IEEE Transactions on Multimedia, 2023.
[3] Ma J, Wu J, Li L, et al. Blind image quality assessment with active inference[J]. IEEE Transactions on Image Processing, 2021, 30: 3650-3663.
However, they are not reviewed or mentioned in this paper. Therefore, the novelty of this work is my major concern. To justify this, providing comparisons with similar models, both theoretically and practically, would increase the demonstration of novelty.
2. The current experiments cannot fully support the claimed contributions , requiring further refinement.

### Questions
1. There are missing comparisons with current SOTAs. Would you provide the performance comparison with TOPIQ and FPR (indicated as follows) on the involved datasets?
[1] Chen C, Mo J, Hou J, et al. Topiq: A top-down approach from semantics to distortions for image quality assessment[J]. IEEE Transactions on Image Processing, 2024.
[2] Chen B, Zhu L, Kong C, et al. No-reference image quality assessment by hallucinating pristine features[J]. IEEE Transactions on Image Processing, 2022, 31: 6139-6151.
2. In the non-aligned reference teacher model, the reference information is learned by first computing the difference between content-irrelevant LQ and HQ images. Please provide more information on this process. How are the pairs formulated? How many HQ images are needed for each LQ image? What is the influence of formulating such LQ-HQ pairs differently?
3. Further, for the non-aligned reference teacher model, would the authors provide the experimental results indicating the insensitivity of the reference images incorporated for training?
4. Why do you incorporate the three different inductive bias tokens? Are they equally important?
5. The NAR-teacher network is trained on the KADID dataset and is employed throughout all the experiments. Meanwhile, the proposed model achieves promising results on all the artificially distorted image datasets while showing sub-optimal performance on authentic images. Is this because the NAR module implicitly learns the distortion information while pretraining? If the reference images are altered to the highest-quality images in authentic datasets, will the proposed method still work?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This work aims to evaluate the perceptual quality of images, and proposes a distillation method from non-aligned reference. The work introduces a teacher module with non-aligned reference, an inductive bias regularization, and a masked quality-contrastive distillation. The experiments show a good performance and the method almost outperforms existing methods.

### Strengths
1. The distillation from multi-networks and reference-based methods is good for blind image quality assessment.
2. Extensive experiments has been conducted to demonstrate the effectiveness.

### Weaknesses
1. The writing is not easy to understand, and the contributions are decentered. It is hard to connect the content within a core idea, which makes the manuscript lack of the main motivation.
2. Fig.2 seems disorder, and it would be good the reshape the work.
3. Some experimental results are missing. For example, Re-IQA in Tab 1 lacks the results on LIVEFB. I suppose the work has published its performance on the database. And if the method is reimplemented by the authors, it would be weird to miss it.
4. Also, the work seems too complicated, but still cannot perform superior over some simple models on several large-scale IQA datasets (e.g., KADID, LIVEFB). And it would be noted that the performance on KonIQ and SPAQ is merely similar to SAMA (2024-aaai), which is simply a sampling strategy.

### Questions
1. The authors may give a concise description on the main contribution of the work.
2. It is weird that some results are missing. For example, Re-IQA has published the original result on LIVEFB in the original paper, and the source code is also available, but the performance is not shown in Tab.1.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors introduce a framework called RKIQT, which aims to learn reference knowledge for image quality assessment without needing aligned reference images. The proposed method includes a Masked Quality-Contrastive Distillation (MCD) approach and an inductive bias regularization strategy. The authors claim that their method outperforms existing NR-IQA methods across multiple datasets.

### Strengths
*  The introduction of MCD to distill knowledge from non-aligned references is a new idea that could potentially enhance NR-IQA.
*  The authors conduct experiments across eight standard IQA datasets, demonstrating a commitment to empirical validation.

### Weaknesses
 * It is unclear to me how adjusting the inductive biases of the ViT ensures rapid convergence and prevents overfitting.

* The authors claim that "our method utilizes less input—eliminating the need for reference images during inference—while achieving better performance than some IQA methods that do require reference images." However, the results show that the proposed model underperforms when compared to FR-IQA models (DISTS and IQT). Could you clarify this discrepancy?

* Why is this model considered the first attempt to transfer more HQ-LQ difference priors and rich inductive biases to NR-IQA via knowledge distillation (KD) in comparison to other KD-based models, such as the one proposed by Yin et al. (2022)? The novelty of using the KD scheme for IQA is limited.
 
* For the non-aligned reference teacher, directly computing the feature differences between HQ and LQ images is physically meaningless. Additionally, there is no ablation study to verify the effectiveness of the reference image.



### Questions
* There is no validation set used for model training. How do the authors conduct model selection and hyperparameter tuning? Using the test set for these purposes may violate established machine learning practices.

* The model should assess generalization by training on authentic distortions and testing on synthetic distortions (or vice versa).

* Why is there a discrepancy in SRCC performance on TID2013 between Table 1 and Table 8?

* In Line 478, the reported result of 0.86 falls outside the range of 0.32 to 0.7. Please clarify.

* In Fig. 4, the activation maps fail to focus on image distortions. For example, in the last two columns, the background is full of artifacts, but only the birds are highlighted.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This work aims to enhance NR-IQA by leveraging comparison knowledge used in FR-IQA but without relying on reference images during inference time. Specifically, a Masked Quality-Contrastive Distillation method is designed to distill comparison knowledge from a non-aligned reference (NAR) teacher model to an NR student model. In addition, an inductive bias regularization method is proposed to learn knowledge from both a CNN teacher and an Involution Neural Network (INN) teacher, aiming to integrate complementary inductive biases into the backbone ViT.

### Strengths
+ This work is well-motivated, leveraging comparison knowledge to NR-IQA models without accessing the reference images during inference is a promising direction.
+ Distilling inductive bias to a ViT backbone is conceptually reasonable.
+ The resulting model attains high performance on multiple IQA benchmarks.

### Weaknesses
 - To the Reviewer, this work is more a good-engineered solution than an academic finding. Despite the superior final performance, no new technique is proposed.
- The results of the compared methods seem to be directly copied from their corresponding papers. Different splits of train/val/test may significantly affect the fairness of performance comparison.
- Ablation studies are conducted on LIVEC only or LIVEC and KoNIQ, which may not be representative enough.

### Questions
There is no validation set. How to pick the epoch?

### Soundness
3

### Presentation
2

### Contribution
2
