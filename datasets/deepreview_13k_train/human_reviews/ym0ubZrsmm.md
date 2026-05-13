# Image Background Serves as Good Proxy for Out-of-distribution Data

- Decision: Accept
- Scores: 8, 6, 6, 6, 3, 3

## Abstract
Out-of-distribution (OOD) detection empowers the model trained on the closed image set to identify unknown data in the open world. Though many prior techniques have yielded considerable improvements in this research direction, two crucial obstacles still remain. Firstly, a unified perspective has yet to be presented to view the developed arts with individual designs, which is vital for providing insights into future work. Secondly, we expect sufficient natural OOD supervision to promote the generation of compact boundaries between the in-distribution (ID) and OOD data without collecting explicit OOD samples. To tackle these issues, we propose a general probabilistic framework to interpret many existing methods and an OOD-data-free model, namely \textbf{S}elf-supervised \textbf{S}ampling for \textbf{O}OD \textbf{D}etection (SSOD). SSOD efficiently exploits natural OOD signals from the ID data based on the local property of convolution. With these supervisions, it jointly optimizes the OOD detection and conventional ID classification in an end-to-end manner. Extensive experiments reveal that SSOD establishes competitive state-of-the-art performance on many large-scale benchmarks, outperforming the best previous method by a large margin, \eg, reporting \textbf{-6.28\%} FPR95 and \textbf{+0.77\%} AUROC on ImageNet, \textbf{-19.01\%} FPR95 and \textbf{+3.04\%} AUROC on CIFAR-10, and top-ranked performance on hard OOD datasets, \ie, ImageNet-O and OpenImage-O.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses the task of out-of-distribution detection in image classification tasks. The authors identify two main challenges the existing methods are facing, namely the absence of a unified perspective to interpret existing techniques and the need for natural OOD supervision to enhance model robustness without the necessity of explicit OOD data collection. Towards this end, the authors introduce a novel probabilistic framework that provides a unified interpretation of many existing OOD detection methods and the SSOD model that efficiently leverages the CNNs properties (retain spatial information) to create a distinction between ID and OOD samples. The paper's contributions are substantiated through extensive experiments (both is terms of benchmarks, as well as proper evaluation w.r.t state-of-the-art methods). SSOD shows consistent improvements in OOD detection metrics over previous methods, highlighting the model's effectiveness in recognizing and handling OOD samples without the need for additional OOD data.

### Strengths
Originality >> SSOD uses image backgrounds as natural proxies for OOD samples, which is a novel perspective in the field.

Quality >> The best paper I read in a while, both in terms of problem statement/formulation and execution (exemplar experimental analysis).

Clarity >> The paper is well-articulated - clearly presents the research problem, the proposed solution, and the insights from the conducted experiments. Also, the authors seem to have made an effort to ensure that the concepts are accessible to anyone, regardless of their expertise in OOD detection.

Significance >> By proposing a general probabilistic framework, the paper unifies various existing approaches under a single interpretative lens, on top of SSOD that offers an evident advancement for OOD detection (relevant problem).

### Weaknesses
No fundamental flaws with the current submission, but just a suggestion to the authors - to include a more thorough discussion on the limitations of SSOD - what are the potential biases, the impact of background complexity on the model's performance, and scenarios where the model may not perform as expected - to start a discussion towards further improvements. Maybe within a dedicated section, tackling these aspects would be valuable.

### Questions
No further questions, besides addressing the weaknesses mentioned above.

### Soundness
4 excellent

### Presentation
4 excellent

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
This paper focuses on Out-of-Distribution (OOD) detection and introduces a unified probabilistic framework that divides the OOD detection problem into In-Distribution (ID) and OOD components. This framework presents an insightful overview of existing OOD detection methodologies and pinpoints their limitations (classifiers and features are often biased towards ID data). To address this challenge, the authors introduce Self-Supervised Sampling for OOD Detection (SSOD), utilizing image backgrounds as effective proxies for OOD data. The model employs separate ID and OOD heads, with the OOD head being self-trained through the utilization of confidence scores derived from the classification head. The results demonstrate that the proposed method significantly outperforms existing approaches by a substantial margin.

### Strengths
1. The motivation derived from the proposed general OOD detection framework seems both intuitive and solid. 
2. The paper is well-written and figures / tables are easy to follow.
3. The proposed SSOD approach, while seemingly simple, demonstrates strong effectiveness.
4. The experimental results are quite strong across various datasets.

### Weaknesses
1. Given that SSOD necessitates pseudo-labels for each patch (like semantic segmentation), 
Since SSOD requires the pseudo-labels for each patch (like semantic segmentation), I presume that the training expenses could surpass those of conventional pre-training methods. Could the authors provide a computational comparison of SSOD with other baseline OOD detection models, as well as standard classification models (e.g., ResNet-18, ResNet-50, etc.)?

2. It appears that the principal interpretation derived from the probabilistic framework (Appendix A.1) might be more aptly positioned between Sections 3.1 and 3.2. Currently, the main motivation behind SSOD doesn't seem to be adequately emphasized.

### Questions
1. Could you specify the number of patches used in the SSOD model? More specifically, what are the dimensions (height H and width W) in the last feature map?

2. Does the performance of SSOD show sensitivity to the classification confidence parameter gamma?

3. While SSOD generally surpasses other baselines in performance, as seen in the tables, there are instances where other baselines demonstrate notably strong results (e.g., MOS in iNaturalist and KNN in Texture). What could be the main reason for these exceptional cases?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
- Authors tackle the problem of Out-Of-Distribution (OOD) detection in this work and show that the image background in In-Distribution (ID) datasets can act as a good proxy for OOD data, preventing the necessity to collect real/synthetic OOD data for training strong OOD detectors. 
- First, authors propose a general probabilistic framework that can explain existing OOD detection methods.
- Next, using this interpretation, authors propose **S**elf-**S**upervised **O**OD **D**etection (SSOD) to exploit the natural OOD signals present in ID data. This prevents the need for collecting explicit real or synthetic OOD data making the pipeline more efficient.
- With extensive experiments, authors show impressive results on several OOD benchmarks proving that image backgrounds of ID data can serve as a good proxy for OOD data.

### Strengths
- The probabilistic interpretation of OOD detection methods is very useful to advance future research. The factorized interpretation also helps tune each independent component accordingly to optimize ID or OOD performance depending on the downstream objective.
- The paper is well written, and the math is easy to follow once derived on paper. 
- The experimental section supports all the claims made in the paper.

### Weaknesses
I will summarize my concerns with this work under three broad sections.

**Nomenclature**
- Authors chose to proceed with the name SSOD for their work but the whole field of Semi-Supervised Object detection (SSOD) [1] already exists creating a bit of a confusion.
- I recommend using SSOOD to avoid any confusion with an already established sub-field.

**Presentation of results**
- Authors claim that their first contribution is to provide a probabilistic interpretation of OOD, using which existing methods can be analyzed, but pushed the analysis section to the supplementary. In my opinion, if authors claim the probabilistic interpretation as an analysis tool, then it shouldn't be delegated to the supplementary.  

**Motivation and intuition**
- Authors show impressive results on several OOD benchmarks but the motivation that image background can serve as a good proxy for OOD data has some flaws.
- First, using the penguin image example from Fig. 2, teaches the network to consider the background (in this case "water") as a signal for OOD. Now this will be ineffective in datasets constructed from comics or cartoons which is not one of the domains that authors evaluate their method on. This also explains why the scores are lower on OOD datasets constructed from SUN, Places because Imagenet is predominantly biased towards "organisms" and "food" with lower signals from indoor scenes and places. This raises the question "Does this method work because of the choice of the OOD datasets used?" This is partly explained by the results on "Textures" (I agree with the authors that textures has some overlap with patterns in the ID classes and the results are low, but I believe that is just part of the story). 
- Second, I think some additional analysis is required on the iNaturalist dataset (or maybe another toy setup on the subset of imagenet) which explains why the method works. If the OOD head is learning to detect any background patch as OOD, then what is the role of this in iNaturalist, where the background is usually water/trees/nature etc? From Imagenet, the network learnt to flag any background containing these regions as OOD, so does it ignore the ID category entirely and just focus on background? But that can't be true because the ID performance is also higher. The interplay between the CLS head and OOD head is very important to completely understand why image background is a good proxy and is missing from the paper. 

**I recommend authors to consider answering these questions for me to improve on my rating**

### Questions
**Questions**
- In the abstract, authors mention they leverage "local property of convolution" for OOD. But it hasn't been mentioned anywhere else. Can you elaborate what they mean by this?
- In eq. 9 the $y_i^{\text{OOD}}$ is the label for detecting OOD patches right? In which case, patches with confidence lower than 5% ($1-\gamma$) should have a label 1 and not 0 right?
- In the 2nd sentence below Eq. 11, is it "During inference" or "During training/inference"? The second loss term in Eq. 11 is applied on a spatial map from what I understood, so why do we have to compute $P(x\in \mathcal{S}_{\mathbb{ID}}|x)$ explicitly during training? We just need that during inference correct?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The article focuses on Out-of-distribution (OOD) detection and proposes a model called Self-supervised Sampling for OOD Detection (SSOD) that does not require explicit OOD data annotation, which is able to extract natural OOD signals from the background of ID images, end-to-end end-to-end training of OOD detection branches. Experiments are conducted on several large-scale OOD detection datasets to demonstrate the effectiveness and superiority of SSOD.

### Strengths
1.	The article proposes a general and reasonable probabilistic framework to understand the OOD detection problem, which can cover a wide range of existing OOD detection methods in an innovative way.
2.	The article proposes an effective self-supervised sampling mechanism capable of extracting useful OOD signals from ID images, avoiding the difficulty and cost of collecting and labeling large amounts of OOD data.
3.	The article provides a detailed description and derivation of the working principle and design of SSOD.

### Weaknesses
1.	The article uses some uncritical and unreasonable assumptions in the derivation of the probabilistic framework, such as setting T as sM+1, ignoring the possible differences between sM+1 and T; treating P(wi|x) as P(wi|x∈SID,x), ignoring the possibility that x may belong to the OOD data. Specifically, the assumption that T can be directly substituted by sM+1 needs more justification, as they are both learnable parameters, but their roles in the model are different. T acts as a global bias, while sM+1 is an output of a neural network that is dependent on the input x. The simplification of P(wi|x) to P(wi|x∈SID,x) is also problematic because it neglects the case where x could be an OOD sample, which would have a different probability distribution. This simplification limits the generalizability of the proposed framework.
2.	The article uses a fixed and subjective threshold γ in the self-supervised sampling mechanism to determine whether an image block belongs to ID or OOD, which does not consider the possible differences and variations between different datasets, models, and categories. The choice of γ=0.95 seems arbitrary without a clear justification or empirical evidence showing its optimality across diverse datasets and model architectures. This fixed threshold may not be suitable for all scenarios, potentially leading to suboptimal performance in some cases. The lack of adaptive thresholding or a mechanism to learn this threshold is a significant limitation.
3.	There are some spelling mistakes, grammatical errors, and punctuation errors in the article; some irregular or inappropriate terms are used in the article, such as OOD-data-free model, OOD patch sampler, and so on.

### Questions
1.	The derivation of formula (1) seems to lack a detailed explanation. Can a more complete mathematical derivation of this formula be provided?
2.	There are some grammatical and spelling errors in the text, please fix them
3.	There seems to be a subjective bias in the interpretation of the experimental results. Can more objective evidence be provided to support these interpretations?
4.	In the first paragraph on page 1, the author mentions that "OOD detection empowers the model trained on the closed image set to identify unknown data in the open world". But there is no definition or difference between what is closed image set and open world. Please define and explain these two concepts clearly in the introduction.
5.	On page 4, paragraph 5, the author mentioned "Since the ImageNet-O mainly contains adversarial images, leading to the classifier's wrong prediction, SSOD reports higher FPR95 compared to the open world". SSOD reports higher FPR95 compared to the best previous methods", but no reason or mechanism is given as to why the adversarial images cause SSOD's performance to degrade.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper addresses challenges in Out-of-distribution (OOD) detection by:
1. Proposing a unified probabilistic framework to understand existing methods.
2. Introducing a new model, SSOD, that uses natural OOD proxy from in-distribution data without needing explicit OOD samples.
3. Demonstrating that SSOD significantly outperforms previous methods on major benchmarks.

### Strengths
1. The paper is articulately composed and organized, facilitating a clear understanding of most sections.
2. To my understanding, the method introduced is innovative.
3. The study is underpinned by a comprehensive set of experiments.

### Weaknesses
Major Points:

1. **Concerns about the First Contribution:**

a. The derivation in Eqs 1-6 appears not helpful to the proposed method and Eq. 7 could be introduced more directly with 

$$P(w_i|x)=P(w_i,x\in S_{ID}|x) = P(w_i|x\in S_{ID},x) \cdot P(x\in S_{ID}|x), i=1,\dots,M$$

The explicit steps from Eqs 1-6, while mathematically sound, do not seem to provide any practical benefit to the proposed method. The jump to Eq. 7, which is the basis for the method, could be made directly using basic probability rules. The intermediate steps do not contribute to the understanding or implementation of the proposed approach.

b. The analysis of prior methods seems not necessarily dependent on a probabilistic perspective, since $P(x\in S_{ID}|x)$ is essentially a rephrasing of existing methods (in A.1).

The probabilistic perspective, while presented as a unifying framework, appears to be a reinterpretation of existing OOD detection methods rather than a novel contribution. The term $P(x\in S_{ID}|x)$ simply formalizes the existing methods' scores, and the analysis in Appendix A.1 could be done without this probabilistic view. This raises questions about the necessity and novelty of the probabilistic viewpoint.

2. **Impact of Confidence Threshold:** How does the confidence threshold, $\gamma$, in Eq. 9 influence the performance? Could the authors elaborate on how they determined its value during experiments?

The paper lacks a detailed analysis of the confidence threshold's impact on performance. It is unclear how the value of $\gamma$ was chosen and how sensitive the results are to this parameter. A thorough ablation study is needed to understand the influence of this threshold on the final results.

3. **Bias in the Proposed Method:** The paper indicates that existing post-hoc methods are influenced by biases from pretrained models. Yet, as Table 3 reveals, the proposed technique doesn't perform optimally on ImageNet-O, which contains adversarial images for ImageNet. Given that the method's training relies on both the original dataset and model's intermediate predictions, is it possible the method still suffers from the bias?

The performance on ImageNet-O suggests that the proposed method might still be susceptible to biases from the pre-trained model. Since the method relies on the model's intermediate predictions, it is possible that it inherits some of the biases present in the original model. This undermines the claim that the method is free from the biases affecting post-hoc methods.

4. **Effect of OOD Training Target on ID ACC:** In the experiments, what is the ID ACC performance when $\alpha=0$? Essentially, does including the OOD training target lead to a noticeable decrease in ID ACC?

The paper does not clearly state the impact of the OOD training target on in-distribution accuracy. It is important to know whether including the OOD training objective negatively affects the model's ability to classify in-distribution samples. The absence of this information makes it difficult to assess the trade-offs of the proposed approach.

5. **Fairness of Comparison in Experiments:** In the experimentation section, multiple methods such as MSP, ODIN, ReAct, and many others are post-hoc techniques that work off a fixed pre-trained model. These methods don't adjust the training process, distinguishing them from the proposed approach. As a result, juxtaposing these techniques might not offer a balanced comparison. The majority of experiments may not necessarily highlight the superiority of the proposed method. It would be beneficial for the authors to contrast their strategy with other training-based techniques.

The experimental setup is not entirely fair, as the proposed method is compared against post-hoc methods that do not involve any training. This makes it difficult to isolate the benefits of the proposed approach. A more rigorous comparison would involve comparing against other training-based OOD detection methods using the same model architecture.

Minor Points:
1. **Table Formatting Issues:** In Tables 4 & 5, the shaded regions seem to obscure the lines, affecting clarity.

2. **Discussion Location:** In the introduction, the authors state that "various OOD methods can be analyzed, with main differences and key limitations clearly identified". However, this discussion is relegated to the appendix. It would be more helpful if the main content were self-contained and inclusive of this analysis.

### Questions
Please see the content in Weakness.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 6

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The text addresses challenges in Out-of-distribution (OOD) detection, emphasizing the need for a unified perspective and the generation of compact boundaries between in-distribution (ID) and OOD data without explicit OOD samples. A general probabilistic framework is proposed to interpret various existing OOD detection methods, providing insights for future research. Concurrently, a Self-Supervised Sampling for OOD Detection (SSOD) model is introduced, which leverages natural OOD signals from ID data through convolution’s local property, allowing for the joint optimization of OOD detection and ID classification in an end-to-end manner. Extensive experiments demonstrate that SSOD achieves state-of-the-art performance on large-scale benchmarks, significantly outperforming previous methods, and showing remarkable results on both standard and challenging OOD datasets.

### Strengths
1. The paper is well-written and easy to understand.
2. The author conducts extensive experiments for evaluation.
3. The visualization is helpful to better understand SSOD.

### Weaknesses
1. SSD [1] also uses a self-supervised algorithm for OOD detection; however, the article does not make any comparisons with SSD.
2. As shown in Tables 2, 4, and 5, SSOD results in a decrease in the model's accuracy for ID classification, which is not permissible for OOD detection. OOD detection requires the model to identify OOD data without affecting the accuracy of ID classification. The reported accuracy drops, while seemingly small, could be indicative of a more fundamental issue with the method's ability to preserve the learned feature space for in-distribution data.
3. The results reported in Table 1 show that SSOD does not achieve state-of-the-art (SOTA) performance on all OOD datasets, and there are many works with better performance not compared in Table 1: React [2], Dice [3], Ash [4]. The lack of comparison with these specific methods, which have demonstrated strong performance in OOD detection, raises concerns about the completeness of the evaluation. Furthermore, the claim of achieving SOTA performance is not fully supported by the presented data.
4. The motivation is not convincing enough: I do not agree with the author's critique of the two-stage manner approach. Post-processing algorithms are actually more suitable for adapting to various pre-trained models, regardless of whether the model is trained with supervised learning or self-supervised learning. The argument against two-stage methods seems to overlook their flexibility and adaptability to different pre-trained models, which is a significant advantage in practice.
5. Table three indicates that SSOD performs poorly on hard OOD detection tasks, does this highlight a flaw in the algorithm: its inability to differentiate between ID and OOD with similar backgrounds? Take the following more realistic example of OOD input: if a network trained to distinguish between different types of apples (e.g., fuji, red, honey-crisp, etc.) is presented with a different fruit as OOD data (e.g., peach, plum, tomato, etc.), the background features could be similar for both ID and OOD data. Alternatively, consider a scenario like scene classification (indoor scene vs beach scene vs forest scene, just as a hypothetical example). In this case, there is no background as such, because the entire scene constitutes the 'foreground.' I am very curious about how SSOD would perform in such scenarios. This raises a fundamental question about the robustness of the method when the distinction between ID and OOD is not primarily based on background features.
6. I recommend the author conduct experiments about ViT architectures.

### Questions
see Weakness

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
