# Assessing Visually-Continuous Corruption Robustness of Neural Networks Relative to Human Performance

- Decision: Reject
- Scores: 3, 8, 6, 5

## Abstract
While Neural Networks (NNs) have surpassed human accuracy in image classification on ImageNet, they often lack robustness against 
image corruption, i.e., corruption robustness.  Yet such robustness is seemingly effortless for human perception.
In this paper, we propose \emph{visually-continuous corruption robustness} (VCR) -- an extension of corruption robustness to allow assessing it over the wide and continuous range of changes that correspond to the human perceptive quality (i.e.,  from the original image to the full distortion of all perceived visual information),  along with two novel human-aware metrics for NN evaluation.
To compare VCR of NNs with human perception, we conducted extensive experiments on 14 commonly used image corruptions with 7,718 human participants and state-of-the-art robust NN models with different training objectives (e.g., standard, adversarial, corruption robustness), different architectures (e.g., convolution NNs, vision transformers), and different amounts of training data augmentation. 

Our study showed that: 1) %for a parameterized image corruption, solely 
assessing robustness %through selected parameter values can lead to biased outcomes---a concern that the VCR effectively addresses (
against continuous corruption can reveal insufficient robustness undetected by existing benchmarks; as a result, 2) the gap between NN and human robustness is larger than previously known; and finally,
3) some image corruptions have a similar impact on human perception, offering opportunities for more cost-effective robustness assessments.
Our validation set with 14 image corruptions, human robustness data, and the evaluation code is provided as a toolbox and a benchmark\footnote{\label{git}\gitlink}.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a comparative study of the robustness of neural networks on visual changes (image corruptions) compared to humans, and perform a larg user-study. This work proposes two measures (HMRI and MRSI) to compare results.

### Strengths
+ address of the important problem of robustness to image corruptions
+ contribution of data: the work contributes with data relative to human-based (large number) assessment of image classification robustness, that might be used to further study the problem

### Weaknesses
_difficult to read_
The paper is hard-to-follow, and the argumentations or explanations are given in an overworded way. Objectives are not clear, and so possible insights that one should gain from reading this work. This makes difficult also to grasp the conceptual contributions or take-aways expected from the experimental analysis and results. 
It looks also strange that a paper that proposes a dataset of corruptions applied to images does not show images of such corruptions and how they relate with existing benchmarks.

_poor insights_
The paper does not provide insights on how the results should be used: to design new models? train existing architectures differently? or other. WHile the user-study and experimental analysis is large, there is little to none instructive conclusions.

_relation with related work missing or weak_
No discussion or comparison with existing work and consider continuous corruptions, such as ImageNet-P and ImageNet-CCC, or other benchmark datasets such as ImageNet-Cbar or ImageNet-3DCC. 

_choice of the models_
the choice of the tested models is not motivated, neither perspectives on the type of architecture, training data and strategies (e.g. supervised learning, self-supervised, using ImageNet21K or LAION or other datasets, CNN vs transformers) are given.

### Questions
How the augmentations proposed in this paper compare with the continuously changing corruptions of ImageNet-CCC? Why the focus is only wrt ImageNet-C?

How the models are chosen (criteria, comparative perspective, etc.)?

### Soundness
2 fair

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors propose a new concept called visually-continuous corruption robustness (VCR), a better alternative to measure corruption robustness than ImageNet-C benchmark. Unlike pre-defined and definite parameters in ImageNet-C, this work creates a benchmark comprising continuous range of image corruption levels and evaluate human performance on the benchmark. Following that, two human aware metrics are introduced to compare neural network performance against humans. Authors demonstrate a notable disparity in robustness between the networks and human performance, despite the improvements seen in ImageNet-C benchmark.

### Strengths
-	Well written paper.

-	Thoughtful in designing the benchmark with visually-continuous corruptions.

-	Well detailed and carefully conducted human experiments.

-	Quantitatively shown that ImageNet-C comprise less coverage of visual corruptions than the proposed benchmark.

-	VCR is shown to be better robustness estimate than benchmarking on ImageNet-C -> Models having good performance on ImageNet-C shown to be not robust enough on the proposed benchmark.

-	This work emphasizes that model robustness is reliable upon verifying across continuous range of image corruption levels, instead of checking at pre-defined parameters.

-	Open-sourced with all human data. This benchmark is beneficial and steer the future research on corruption robustness in the right direction.

### Weaknesses
I don’t have major concerns about this work. I appreciate authors for considering wide range of models. However, some of the top performing robust models (ImageNet-C leaderboard https://paperswithcode.com/sota/domain-generalization-on-imagenet-c?p=augmix-a-simple-data-processing-method-to) like DINOv2, and MAE are missing in the evaluation. It is helpful to understand behaviour of these models in VCR.



### Questions
-	In page 3, under Testing VCR, it is mentioned that “only sufficient data in each group but not uniformity”. Why this is the case? How do you define the sufficient data here? What are the drawbacks of considering uniformity. It is mentioned that “ this specific design removes the possibility of biased results”, can you clarify what kind of biased distribution of data is referred here?

-	Humans are presented with one image at a time for 200 ms? Isn’t it too short to notice the image? Are the human participants in an average recognize objects in the image within that time? Would it be safe to assume that human participants do even better job when presented with an image upto 1s? It is mentioned that time was set to ensure fairness. Are the machines classify each image with the same 200 ms?

-	Please briefly discuss the qualification tests and sanity checks aimed to filter the participants.

-	A curious question, What is the total number of participants before the filtration process?

-	Are same images seen by each human participant?

-	Please connect (\Cref) the text “Fig 1” to the Figure 1. Similarly, for other figures and tables.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the visually-continuous corruption robustness of existing Neural Networks (NNs) is examined and compared. In particular, two metrics including the Human-Relative Model Robustness Index (HMRI) and Model Robustness Superiority Index (MRSI) are proposed for the models’ performance evaluation on 14 corruption types. The experiments reveal the high robustness gap between humans and NNs.

### Strengths
1.	The proposed metrics are reasonable which could mitigate the evaluation bias caused by the quality distribution of the test set.
2.	Several interesting and meaningful observations are presented. For example, the performance of prediction consistency of different NNs is compared, in addition to the model accuracy.
3.	The authors explore the visually similar transformations, offering opportunities for more cost-effective robustness assessments.

### Weaknesses
1.	In this paper, The VIF is adopted as the quality measure. However, compared with the advanced full-reference quality measures, such as LPIPS [1], and DISTS [2], the VIF is usually inferior.
2.	In Sec.3, Page 4, the coverage between the IMAGENET-C and VCR Test Set is compared by splitting the full quality range into 40 bins. However, the coverage is highly relevant to the number of bins. In an extreme case, when the bin number is 1, the same coverage the two sets will possess. As such, how to ensure the coverage is reasonable?
3.	During subjective testing, human decisions are usually highly affected by the memory effect, i.e., a severally corrupted image could still be recognized successfully when humans have observed the same image content but with a high quality. The authors should illustrate how to avoid such effect and provide more details to demonstrate the reliability of the human decision collection.
4.	Typos: in Deﬁnition 1 [Human-Relative Model Robustness Index (HMRI)]: the S^m({\gamma}^(v)) should be S^m_{\gamma}^(v).

### Questions
Please see above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes a visually-continuous corruption robustness (VCR) metric based on the visual information fidelity (VIF) metric. Furthermore, the authors propose two human-aware metrics HMRI and MRSI. The key message is that the gap between neural network robustness and human robustness is larger than expected. Authors have conducted experiments with 14 different image corruption techniques with 7718 human participants and different SOTA neural networks models.

### Strengths
- The paper is well-motivated and the experiments are very extensive
- The problem discussed is important and interesting
- Implementation and data was made available by the authors

### Weaknesses
 - The paper is very hard to read and necessary background is not introduced. For example, I would have liked an explanation what visual information fidelity is. Overall, there is a lot of content squeezed in the 9 pages which makes the paper mostly incomprehensible.
- Due to above issue, I strongly suggest to publish the paper in a journal (which usually have no page limits). The quality of the write-up would highly benefit from this.
- Section 2 (Methods) needs a major rewrite to make it more accessible to readers not familiar with image quality metrics. Here are some points that can be improved:
    1. The section mentions multiple times that $\Delta_v \in [0,1]$. 
    2. The variable c is used before it was defined.
    3. Authors should stress that $\Delta_v$ is just an auxiliary quantity that later is used to define the VCR.
    4. Authors could consider adding a figure to give an overview of the used and introduced metrics. As a reader, I was overwhelmed by all these acronyms. An overview would have been very helpful.
- I very much appreciate that the authors shared their code, however I find it inappropriate to refer to it as a "toolbox". In my opinion a toolbox is an installable Python package that is easily applicable to different models and datasets. Authors have to spend more time on their code repository before calling it a "toolbox".

Minor details:
- page 2: $max$ should be $\max$
- Tbl. 2 -> Tab. 2
- typo page 4: “coverages= of” and “[0..1]” (should be [0,1])
- Two paragraphs in the abstract look unusual
- Suggestions: "Uniform(0,1)" -> "U(0,1)"

### Questions
- What is impulse noise or glass blur?

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good
