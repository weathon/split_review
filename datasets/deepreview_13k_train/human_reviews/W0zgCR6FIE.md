# Spawrious: A Benchmark for Fine Control of Spurious Correlation Biases

- Decision: Reject
- Scores: 5, 8, 5, 5

## Abstract
The problem of spurious correlations (SCs) arises when a classifier relies on non-predictive features that happen to be correlated with the labels in the training data. For example, a classifier may misclassify dog breeds based on the background of dog images. This happens when the backgrounds are correlated with other breeds in the training data, leading to misclassifications during test time. Previous SC benchmark datasets suffer from varying issues, e.g., over-saturation or only containing one-to-one (O2O) SCs, but no many-to-many (M2M) SCs arising between groups of spurious attributes and classes. In this paper, we present \benchmark-\{O2O, M2M\}-\{Easy, Medium, Hard\}, an image classification benchmark suite containing spurious correlations between classes and backgrounds. To create this dataset, we employ a text-to-image model to generate photo-realistic images and an image captioning model to filter out unsuitable ones. The resulting dataset is of high quality and contains approximately 152k images. Our experimental results demonstrate that state-of-the-art group robustness methods struggle with \benchmark, most notably on the Hard-splits with none of them getting over $70\%$ accuracy on the hardest split using a ResNet50 pretrained on ImageNet. By examining model misclassifications, we detect reliances on spurious backgrounds, demonstrating that our dataset provides a significant challenge.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
Previous benchmarks testing robustness to spurious correlations faced problems, such as over-saturation and a lack of many-to-many (M2M) social correlations. The authors introduce Spawrious-{O2O, M2M}-{Easy, Medium, Hard}, an image classification benchmark with 152k high-quality images. State-of-the-art group robustness methods struggle with Spawrious, especially on the hard splits, achieving less than 73% accuracy using an ImageNet pre-trained ResNet50. Model misclassifications expose dependencies on spurious backgrounds, underscoring the dataset's significant challenge.

### Strengths
- The authors do a good job of elaborating six desiderata for a spurious correlations benchmark including multiple training environments, photo-realism and high fidelity backgrounds. This can act as general guidelines that future works in this area can build upon.
- The authors formally present the O2O and M2M spurious correlation settings, which helps make their contribution clear. See questions for some clarifications on these.
- Overall the paper is well written (Figure 3 is particularly nice) and addresses an outstanding concern of insufficient benchmarks for the spurious correlation/distribution shift community. Though, there are some other recent benchmarks (like PUG) that do the same (see Weaknesses), and addressing some of the points below (especially the hardness of M2M setting) would help distinguish this work from those.

### Weaknesses
 - Comparison with/discussion on some other relevant spurious correlation benchmarks that also use a synthetic/combinatorial construction pipeline like the PUG dataset is missing.
- Some understanding of the hardness of the proposed benchmark would be relevant. Presumably there is some optimal re-weighting function for this dataset. How does the JTT assigned weights compare with this? 
- Explanation/discussion of why MixUp does better than other baselines in M2M setting would be helpful.
- Performance of some other recent baselines like RWY (uses group info), BR-DRO/LfF (does not use group info) is missing.

Overall, this paper makes an attempt towards a useful and much needed SC benchmark, but falls slightly short of building some understanding of the distinguishing characteristics of the proposed dataset -- it is unclear how M2M is different from O2O but with superclass/superattribute labels. It is possible that I missed some details. Therefore, I would be happy to consider raising my score after the authors have had a chance to respond to my questions.

### Questions
- In the M2M case, there is still a one-to-one relationship between disjoint subgroups of classes and attributes. I did not fully understand why it is M2M, since it can still be thought of as O2O with respect to labels and attributes at a higher granularity? I imagined that the M2M case would involve overlapping subsets of classes and attributes.
- Why is the correlation completely flipped in the M2M case only, and not O2O case?
- In Figure 2c and 2d why is the correlation flipped and not randomized, i.e., zero correlation, which is typical of test distribution on existing datasets like waterbirds (unless you are looking at only the worst group as the test set)?
- What weights were used for group DRO, since the test set has correlations that do not appear at all in the training set, so theoretically the weights are infinite in this case?

### Soundness
2 fair

### Presentation
3 good

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
This paper presents a new benchmark for assessing algorithms for training models to be robust to spurious signals. The benchmark uses a text-to-image model to generate inputs under different specifications, i..e input text, which allows one to control the difficulty of the task. Because of this text-based control, the benchmark has a many-to-many spurious signal set, which can be completely reversed between training and testing---a challenging condition for current algorithms. The primary task is dog classification. This paper then tests several approaches for training a model to be robust to spurious correlations, and finds that Mixup does particularly well for many-to-many spurious correlation and Just-train-twice is the best performing for One-to-One spurious settings.

### Strengths
Overall, I enjoyed reading this paper, and think it was well executed. Here I discuss some of these key strengths. 

- **Nice Dataset Design**: I particularly enjoyed the use of the image-to-text models here for performing dataset design. I think this type of dataset design is going to be increasingly common for various settings. Essentially the design here it to use a text-conditioned generative model to create toy datasets where the data generation process is carefully controlled to induce various proportions of features of interest. This is approach was also used in the Instructpix2pix paper. 

- **Scale of Empirical Assessments**: The coverage in algorithms here is also quite substantial since this literature is quite active. To my count, the authors test 10 methods across 6 settings, which is a substantial amount of work, and commendable.

### Weaknesses
I have two weaknesses with this work, but they don't factor into my rating. 

- **Failures of Dataset Design**: My first issue is about how to verify whether the output of the text-to-image model matches and satisfies **all** conditions or features specified in the prompt. The authors discuss this issue in Appendix F. The authors attempt a manual and an automatic filtering process. However, both of these also might be susceptible to failure in different ways. For example, the automatic filtering relies on a captioning model, which itself could make mistakes in describing the image, leading to incorrect filtering. Similarly, the manual filtering process, while more reliable, is still subject to human error and bias, especially if the volunteers are not diverse enough or if the task is too complex to assess reliably. It is not clear how the authors ensured that the manual filtering was consistent and accurate across all samples.

- **Insights**: Table 1 is a very compelling result for mixup, and it points at trying to better understand its properties theoretically w.r.t. to spurious signals. Given the already wide scope of this paper, it is unable to delve into explaining the effectiveness of various methods. While the empirical results are strong, a deeper theoretical analysis of why Mixup performs so well in this specific context would significantly enhance the contribution of the paper. The current analysis is limited to observing the performance differences without providing a mechanistic understanding of the underlying reasons.

### Questions
- In Table 3, how is this average computed? Also, does it make sense to report an average if it includes a combination of different settings/environments?

- Section E of the appendix is very interesting. Did you also happen to compute the saliency maps for the mixup models on these same inputs? Would be interesting to compare both of them.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduces a new image classification benchmark dataset called "Spawrious" that addresses the problem of spurious correlations in classifiers. Spawrious contains both one-to-one (O2O) and many-to-many (M2M) spurious correlations between classes and backgrounds in images. The dataset is carefully designed to meet six specific desiderata and is generated using text-to-image and image captioning models, resulting in ~152k high-quality images.

Experimental results show that even state-of-the-art group robustness methods struggle with the Spawrious dataset, especially in challenging scenarios (Hard-splits) where accuracy remains below 73%. Model misclassifications reveal a reliance on irrelevant backgrounds, highlighting the significant challenge posed by the dataset. Experimental results demonstrate the difficulty of the dataset and the limitations of current group robustness techniques.

### Strengths
The strengths of the paper can be summarized as follows:

Novel Benchmark Dataset: The paper introduces a novel benchmark dataset, Spawrious, which contains a wide range of spurious correlations, including both one-to-one and many-to-many relationships. This dataset offers three difficulty levels (Easy, Medium, and Hard) for evaluating the robustness of classifiers against spurious correlations. The dataset consists of approximately 152,064 high-resolution images of 224 × 224 pixels. The dataset's size and quality make it a valuable resource for testing and probing classifiers' reliance on spurious features.

Experimental evaluation: The paper explores different model architectures and robustness methods, evaluating their performance on the dataset, revealing that larger architectures can sometimes improve performance but the gains are inconsistent across methods. The experimental results demonstrate that state-of-the-art methods struggle to perform well on the Spawrious dataset, particularly in the most challenging scenarios (Hard-splits) where accuracy remains below 73%. This highlights the dataset's effectiveness in pushing the boundaries of current classifier robustness. The paper provides evidence for the reliance of models on spurious features through an analysis of model misclassifications. 

Overall, the strengths of the paper lie in its creation of a challenging benchmark dataset and the empirical evidence it provides about the limitations of state-of-the-art methods in handling spurious correlations in image classification, stimulating the need for future research and developments in this domain.

### Weaknesses
t would have been better if the paper included empirical results on some well known domain generalization datasets (using the same methods as the ones in Table 3). 
By comparing between the accuracy of various methods on multiple such datasets, the case could be made stronger for the paper introducing a strong benchmark for spurious correlations. One such dataset could be: FOCUS: Familiar Objects in Common and Uncommon Settings

However, the paper is not cited. Nor is any such comparison provided. 

Moreover, no details are provided for any filtering of the model generated images. There should be some human study in the paper which shows what percentage of images generated by the diffusion models are aligned with the the prompts. If the images generated are not aligned with the prompt, the dataset cannot be trusted to contain the variety of spurious correlations.

### Questions
Did the authors conduct any crowd study to show that the images generated by the diffusion model follow the intent of the prompt? If not, it is hard to say whether the generated data actually contains the different images in different backgrounds and can be useful for research.

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper studied the spurious correlation (SC) problem. To study this problem, the paper introduces the Spawrious dataset. Unlike previous SC benchmarks that only contain one-to-one SCs, the Spawrious benchmark introduces new many-to-many SCs that jointly consider spurious correlations and domain generalization problems. The images are generated using Stable Diffusion v1.4. The experimental results show that many group robustness methods struggle with the new benchmark.

### Strengths
* The paper evaluated many (11) group robustness methods (Table 3) on the newly introduced dataset.
* The discussion on potential ethical concerns about using Stable Diffusion to generate training images (Appendix C) is appreciated.
* The paper is well-written.

### Weaknesses
### Major Concerns

**[Benchmark W2D]**: Although the paper evaluates many group robustness methods in Table 3, none of them is designed to handle both correlation shift and domain shift. Why not evaluate the W2D method (Huang et al. 2022) that is designed to handle two shifts, which is the main focus of Spawrious?

**[More comprehensive benchmark of architecture]**: Wenzel et al. [1] did a comprehensive evaluation of OOD generalization. One of the conclusions is that architectures (such as Deit, Swin, and ViT) play a key role in improving OOD robustness. Although the paper benchmarks many group robustness methods and compares two architectures (Appendix D), I think it is necessary to see more results in terms of different neural architectures on the new benchmark based on conclusions in [1]. Specifically, the paper should explore not only different architecture families (e.g., Transformers vs. CNNs) but also different sizes within those families to fully understand the architectural impact on this benchmark.

### Minor Concerns

**[More results of foundation models]**: To show that this Spawrious is really challenging, I think we evaluate the performance of foundation models (e.g., CLIP [2] with zero-shot transfer) pretrained on web-scale datasets. It's crucial to see how well these models, which are trained on diverse real-world data, perform on the synthetic Spawrious dataset. This comparison would highlight the unique challenges posed by the dataset. Furthermore, given that the images are generated using Stable Diffusion, it would be beneficial to analyze if the dataset captures the nuances of real-world data or if the synthetic nature introduces biases that are easily overcome by models trained on real data.

I wonder why the authors argued that ImageNet-W (Li et al, 2023) is synthetic (Section 2, page 3). The watermark shortcut in ImageNet-W naturally exists in the real-world ImageNet dataset.

### Questions
In the rebuttal, I expect the authors to address my concerns:

1. Add results of W2D.
2. Add more results by using different architectures.
3. Add results of CLIP or other foundation models to better demonstrate how challenging the benchmark is.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
