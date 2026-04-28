# DETER: Detecting Edited Regions for Deterring Generative Manipulations

- Decision: Reject
- Avg Score: 5.25
- Scores: 3, 8, 5, 5

## Abstract
Generative AI capabilities have grown substantially in recent years, raising renewed concerns about potential malicious use of generated data, or ``deep fakes.’’ 
However, deep fake datasets have not kept up with generative AI advancements sufficiently to enable the development of deep fake detection technology which can meaningfully alert human users in real-world settings. Existing datasets typically use GAN-based models and introduce spurious correlations by always editing similar face regions. 
To counteract the shortcomings, we introduce \textbf{DETER}, a large-scale dataset for \textbf{DETE}cting edited image \textbf{R}egions and \textbf{deter}ring modern advanced generative manipulations. \textbf{DETER} includes 300,000 images manipulated by four state-of-the-art generators with three editing operations: face swapping (a standard coarse image manipulation), inpainting (a novel manipulation for deep fake datasets), and attribute editing (a subtle fine-grained manipulation). While face swapping and attribute editing are performed on similar face regions such as eyes and nose, the inpainting operation can be performed on random image regions, removing the spurious correlations of previous datasets. Careful image post-processing is performed to ensure deep fakes in \textbf{DETER} look realistic, and human studies confirm that human deep fake detection rate on DETER is 20.4\% lower than on other fake datasets. Equipped with the dataset, we conduct extensive experiments and break-down analysis using our rich annotations and improved benchmark protocols, revealing future directions and the next set of challenges in developing reliable regional fake detection models.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper introduces a new dataset, which includes different and new deepfake tasks like inpainting. It includes the images edited by two GANs and two Diffusion models. The size of the dataset is 30,000. Through human studies and GPT-4 evaluation, the paper shows the difficulty of prediction and detection over DETER by human beings and GPT-4. Through further benchmarking, the paper shows how incorporating unseen and unaltered images improves model performance. It also delivers insights like the regions edited by inpainting is counterintuitively hard to predict.

### Strengths
1. The paper presents a new dataset of 30,000 images, which is larger and incorporates different granularities for image editing. It also includes masks for more accurate evaluations.
2. The paper includes many different models for predictions and detection.

### Weaknesses
1. In the user study, it is a bad idea to include "I'm not sure" as an option, which will greatly harm the data quality and amount of information. Instead, binary selections can still be enforced, and you can ask participants to indicate their confidence scores. The same is true for GPT-4.
2. The dataset only includes edited images from four different models, which might be insufficient for a comprehensive dataset, especially considering the current flourishing development of generative AI technologies. The claims of difficulty of predicting regions edited by GANs over Diffusion Models are not well supported. By the way, how many models do other SOTA datasets include, as listed in Table 1?
3. A cutoff of IoU of 0.5 is not very informative in showing the benchmarked performance. Why not show the averaged IoU directly?
4. Many of the insights obtained from Section 4.3 are not very informative and are limited to observations. For example, why are images edited by GANs more difficult to predict? Why do eyes and eyebrows raise more errors? Why do models trained on DETER transfer better to OpenForensics (noted that both are face-swapping)?
5. The paper does not include instruction-based image editing, especially those conducted by commercial platforms. This is, however, probably the most significant threat when considering edited images as deepfakes, which can be used and accessed by any ordinary user on the Internet.
6. The dataset is not yet open-sourced. Nor does the paper mention any plans to open-source the dataset.
7. The biggest novelty of the dataset is that it includes different granularities. However, there are no insights into granularities in human studies. For example, why is DETER harder for human beings to identify? Among FaceSwap, Attribute, and Inpaint, which one is the most difficult? It seems that the only purpose of the human study is to show that "it is hard for human eyes".
8. Although images including "multiple faces" are considered novel, no insights are given about this, either in human studies or the benchmark.

### Questions
1. In your training setup, to address the issue where “models tend to assume target regions exist in every image,” why didn’t you just use the original, unaltered fake images from the open-source dataset?
2. Considering "another 140K unseen unmanipulated images" in the improved setting, will they be released to the research community?
3. It would be interesting to benchmark AIGC detectors pre-trained on previous SOTA datasets against the DETER dataset.
4. Model performance appears similar across various models, from the 2015 Faster R-CNN to DINO. Does model capacity influence performance in this case, and if not, why?
5. What instructions were fed to GPT-4 for prompting in Section 3.3?
6. Other questions are already mentioned in Weakness.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper proposes DETER, a large-scale dataset for detecting edited images and regions. The contributions of this work include: 1) in addition to face swapping and attribute editing, the authors also include image inpainting in the data editing operations; 2) to address the spurious correlation challenge in the current datasets for regional fake detection, the authors included additional 90K unedited images; and 3) the authors introduced region-based image-level classification accuracy as an additional assessment criterion. Interesting and important work. Enjoyed reading.

### Strengths
see the above summary.

### Weaknesses
Two points to clarify, rather than weakness.

### Questions
Two minor comments/questions: first, in the first paragraph, the authors wrote “the upstream SOTA generative models and their applications, the midstream existing deep fake datasets, as well as the downstream fake detection formulation and models”. I am just curious why the authors define “upstream, midstream, downstream” this way. Also, the authors consider datasets that include humans in this work, and target human face (either the whole face or part of it) manipulation. What about other datasets of natural scenes, animals, etc.? Can the proposed method be applied there as well?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a dataset for detecting AI-generated image manipulations. There are 3 main contributions:
1. A new dataset that contains state-of-the-art generation methods, which are not incorporated in previous datasets
1. An improved evaluation framework that considers both whole-image and region-specific manipulations
1. Provides techniques to mitigate spurious correlations in fake detection

The dataset contains 300,000 edited images using three types of manipulations: face swapping, attribute editing, and inpainting, created using both GAN and DM-based generators.

### Strengths
The new dataset introduced by this paper can potentially make valuable contributions by addressing a critical challenge in the era of widespread AI image manipulation. It has the following merits: 
- Incorporates current state-of-the-art generative models
- Comprehensive evaluation framework
- Extensive experiments with multiple detection methods
- Well-documented human evaluation studies
- Thorough cross-domain analysis

Clarity. This paper has clear methodology presentation and well-structured experimental results

### Weaknesses
The main concerns about this paper are ethical and legal concerns. 
- There is no clear discussion of whether they have rights to modify/redistribute CelebA and WiderFace images. For example, the CelebA dataset has the following agreement: “You agree not to further copy, publish or distribute any portion of the CelebA dataset. Except, for internal use at a single site within the same organization it is allowed to make copies of the dataset.”
- And there is no discussion of consent from individuals in the images. 
- And there is no discussion of rights clearance for redistributing modified faces.

### Questions
1. How do you ensure the dataset remains relevant as new generative models emerge?
1. How does the post-processing pipeline affect the natural artifacts that might help in detection?
1. Why not include more diverse manipulation techniques beyond facial modifications?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents an image dataset for regional deepfake detection task. Recent images generated by current generative models are included.

I have read the response of the authors and the comments of other reviewers. I would keep my original score.

### Strengths
1. The research problem is useful.
2. Dataset for regional deepfake detection is indeed valuable for deep fake detection tasks.
3. The organization of the paper is good.

### Weaknesses
1. The size of the dataset is not large, which I am afraid cannot be termed as 'large-scale'. While the number of fake images might be higher than some existing datasets, the overall diversity and resolution of the images, as well as the number of unique identities represented, are crucial factors for a dataset to be considered truly 'large-scale'. The dataset's utility for training robust models might be limited by these factors.
2. In section 4.2, method DINO (Zhang et al., 2023) is published in 2023, in Table 4, it is referred to as DINO '22.
3. In Table 4, the methods are relatively not up-to-date. The selection of methods seems somewhat arbitrary, and it is not clear why more recent and state-of-the-art methods for regional deepfake detection were not included. This makes the evaluation less comprehensive and potentially less relevant to the current state of the field.
4. Grammar errors:
a. we use GANs-based E4S (Liu et al., 2023b) and MAT (Li et al., 2022), and DMs-based DiffSwap (Zhao et al., 2023) and DiffIR (Xia et al., 2023) as the deep generators.
b. Too long sentence: We posit ourselves in the entire research pipeline of deep fake detection, present an in-depth and comprehensive study, covering the upstream SOTA generative models and their applications, the midstream existing deep fake datasets, as well as the downstream fake detection formulation and models, that motivates us to introduce this novel large-scale fine-grained deep fake detection dataset.

### Questions
See Weaknesses

### Soundness
3

### Presentation
2

### Contribution
3
