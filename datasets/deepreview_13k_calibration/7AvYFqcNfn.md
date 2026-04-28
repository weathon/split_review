# A Large-scale Interpretable Multi-modality Benchmark for Image Forgery Localization

- Decision: Reject
- Avg Score: 4.20
- Scores: 5, 3, 3, 5, 5

## Abstract
Image forgery localization, which centers on identifying tampered pixels within an image, has seen significant advancements. Traditional approaches often model this challenge as a variant of image segmentation, treating the segmentation of forged areas as the end product. However, while semantic segmentation provides distinct regions with clear semantics that are readily interpretable by humans, the interpretation regarding the detected forgery regions is less straightforward and is an under explored problem. We argue that the simplistic binary forgery mask, which merely delineates tampered pixels, fails to provide adequate information for explaining the model's predictions. First, the mask does not elucidate the rationale behind the model's localization. Second, the forgery mask treats all forgery pixels uniformly, which prevents it from emphasizing the most conspicuous unreal regions and ultimately hinders human discernment of the most anomalous areas. In this study, we mitigate the aforementioned limitations by generating salient region-focused interpretation for the forgery images, articulating the rationale behind the predicted forgery mask and underscoring the pivotal forgery regions with a interpretation description. To support this, we craft a **M**ulti-**M**odal **T**ramper **T**racing (**MMTT**) dataset, comprising images manipulated using deepfake techniques and paired with manual, interpretable textual annotations. To harvest high-quality annotation, annotators are instructed to meticulously observe the manipulated images and articulate the typical characteristics of the forgery regions. Subsequently, we collect a dataset of 128,303 image-text pairs. Leveraging the MMTT dataset, we develop ForgeryTalker, an architecture designed for concurrent forgery localization and interpretation. ForgeryTalker first trains a forgery prompter network to identify the pivotal clues within the explanatory text. Subsequently, the region prompter is incorporated into multimodal large language model for finetuning to achieve the dual goals of localization and interpretation. Extensive experiments conducted on the MMTT dataset verify the superior performance of our proposed model.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper novelty focuses on the interpretability issue of forgery region localization. The authors constructed a multi-modal dataset MMTT, which includes images manipulated by deepfake techniques and their interpretable textual annotations. ForgeryTalker is capable of generating explanations that focus on salient regions.

### Strengths
1. The paper is well-written and clearly organized.
2. The authors constructed a large-scale Multi-Modal Tamper Tracing (MMTT) dataset. I believe this will have a positive impact on the entire forgery localization community.
3. The authors proposed an interpretable image forgery localization framework that can simultaneously perform forgery localization and generate explanatory text annotations.

### Weaknesses
1. Some advanced generated models have produced tampered images that are very realistic and difficult for the human eye to detect. How does the proposed method ensure the accuracy of manual annotations? How are tampered images that are indistinguishable to the human eye handled?
2. The paper does not show enough examples of annotated data, making it difficult to fully understand the annotations for different forged images.
3. The authors only used three generative models to construct the dataset, which may limit its generalizability. My main concern is how well the proposed method generalizes to unseen datasets, and whether text annotations can still be accurately generated for unseen data?
4. Comparison of forgery localization performance: a fair comparison should be made with some forgery localization methods (e.g. TruFor[1], IML-ViT[2], PSCC-Net[3]) to show the proposed model's forgery localization capabilities.
5. How was the model performance comparison in Table 2 conducted? How was fairness ensured in the comparison? Additionally, there is a lack of analysis on possible reasons why the forgery localization ability is lower than SCA.
6. Robustness analysis: Will the model's forgery localization and annotation generation capabilities be affected after the tampered images undergo degradation operations? Conducting robustness analysis is crucial for the practical application of the model.

Some detailed issues:
(1) How is the "iterative refine" in L88 performed? The mechanism here lacks detailed explanation and clarification.
(2) The dataset proposed in the paper only focuses on facial images, so it would be more accurate for the paper's title to focus on "facial image."

### Questions
See Weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper introduces an interpretable framework, ForgeryTalker, for image forgery localization, providing both accurate tampered region identification and textual explanations.

### Strengths
1. The authors create the Multi-Modal Tampering Tracing (MMTT) dataset, a large-scale dataset of 128,303 deepfake-manipulated images with detailed annotations, enhancing the resources available for interpretability in forgery detection research​.

2. ForgeryTalker not only achieves high precision in forgery localization but also generates coherent, human-understandable interpretations, bridging the gap between detection and interpretability effectively​.

3. Extensive experiments demonstrate the model's performance on multiple metrics (CIDEr, BLEU, METEOR), where ForgeryTalker outperforms or competes closely with other advanced models, validating its robustness and effectiveness​.

### Weaknesses
1. This paper has a structure very similar to InstructBlip, with the addition of a plug-and-play Forgery Prompter Network and a mask decoder, which makes the improvement incremental and lacks significant innovation.

2. The task of localization on deepfake images is not particularly meaningful, as the tampered regions in deepfake images are usually concentrated on the face. The network could simply segment the entire face rather than precisely identifying specific areas of the face to serve as an alert. I suggest the authors apply this task to general image detection and segmentation tasks.

3. This paper only includes two comparison methods, which is insufficient. The authors should compare with some classic deepfake detection methods [1, 2], as well as some of the latest approaches that use M-LLM for deepfake detection [3, 4].

### Questions
plase refer to the weakness.

### Soundness
2

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
5

### Summary
This manuscript presents a deepfake localization dataset with textual captions and proposes an MLLM-based method for forgery localization and interpretation.

### Strengths
1. Interpretation is important for image forgery detection/localization.
2. The proposed dataset is large in scale.

### Weaknesses
1. The authors did not design a mechanism for user-driven error correction. The proposed ForgeryTalker cannot deal with hallucinations/incorrect predictions from MLLM.
2. It seems that the authors do not have a plan to make the dataset publicly available.
3. The supplementary materials do not provide sufficient samples to demonstrate the interpretation capability of the proposed ForgeryTalker (as well as its baseline).
4. Some annotations in Figure 1 are not reasonable. For example, “the size of both eyes is different.” Different sizes of eyes commonly appear in real faces. More meticulous checking should be done when annotating images. A user study should be designed to ensure the credibility of the interpretation.
5. The dataset includes too few types of forgeries (or manipulation). The authors did not consider for editing, reenactment, etc. Moreover, the dataset includes only one face-swapping method (E4S) and two inpainting methods.
6. The technical contribution is insufficient. ForgeryTalker merely adds additional instructions and mask prediction to InstructBLIP. There are also design limitations in ForgeryTalk, as there is no bidirectional interaction between mask prediction and interpretation. In fact, these two tasks should ideally be mutually reinforcing.
7. A heatmap could potentially replace the text prompts generated by FPN, as FPN's output does not seem to reflect the intensity of forgery in different facial areas or the model’s confidence level.
8. “Mask encoder” should perhaps be referred to as “mask decoder”?
9. The title mentions “image forgery localization,” but only face images are considered, with no coverage of natural images.
10. There is a lack of performance comparison experiments for localization. It is not sufficient to only show ForgeryTalk’s interpretability.

### Questions
Please refer to Weaknesses.

### Soundness
2

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
4

### Summary
This paper looks at proposing a dataset named Multi-Modal Tramper Tracing (MMTT) dataset which looks at providing researchers with the challenging task of not only determining where a manipulation took place in an image but also to explain what was manipulated and through what means. The dataset is composed of images that include 35% GAN based inpaintings, 36% Diffusion based inpaintings and 29% traditional based inpaintings. The main reason for proposing the dataset is that they argue that current face forgery datasets focus on the task of classifying/segmenting where a manipulation is and not providing an explanation of what was exactly forged and how.

Additionally for their dataset they conducted a survey on their MMTT dataset that involves an annotator being presented with the original and forged image and being asked to determine where the forgery took place. The annotator also provides a text description of how the image was manipulated; false positives are remove from the textual description of the manipulated image. 

The paper also proposes a model named ForgeryTalker which extends the InstructBlip model by introducing a Forgery Prompter Network (FPN) and a Mask Decoder. They then train their ForgerTalker model to perform localization of where the manipulation takes place in an image and then captioning to explain how the image was manipulated.

### Strengths
After reviewing this paper I believe that it is well written and that the diagrams generally explain what problem is being proposed and a potential solution to that problem. Given the size of the dataset I believe that it is quite a large dataset with a detailed amount of forged images with a wide range of different set of manipulations types, ranging from GAN based to Diffusion based images. Additionally, with the addition of the ForgerTalker method I believe that it is a step in the right direction of proposing a solution to this problem that is being presented in the paper.

### Weaknesses
I believe that this paper has a few weaknesses that would need to be addressed in order to be accepted at this venue.
Firstly I believe that the paper does not present a thorough analysis of how current methods have performed on this dataset. Currently we only have two other published methods being shown in Table 2, which looking at the methods that are being compared against, included in their own papers for instance InstructBlip has a number of comparisons they did, for instance BLIP-2 and even using different backbones for InstructBlip I believe would at least explore if a choice of backbone would have made a difference in performance. Also with the SCA, there are a number of models that were listed for instance SAM+BLIP or SAM+GIT-large-coco.

* Some other experiments that would have been interesting to explore would have been how do the models perform on each of the manipulation types. Currently we only have the performance on the whole dataset, but we do not currently understand the breakdown by manipulation types. Another experiment is how do the models perform on the different image sources.

* Because not many results are being shown, a significant difference between the current results were not exactly being supported. Currently it appears that ForgeryTalker is not significantly better than InstructBlip, hence not as much is being shown in terms of a large improvement of results.

* Additionally, the paper presents this problem and highlights the problem of current research not adding explanations as to justifications as to what was manipulated in an image, however we do not explore the pitfalls of these models. Hence it is not currently clear if these models have inherent problems that they need to be addressed or not.

### Questions
* In terms of annotating the images for the Multi-Modal Tramper Tracing (MMTT), are the authors saying that with this dataset of size 130,000 images, that only 30 annotators were used to create the labels for the data? Meaning each annotator, annotated 4000+ images? It is not clear if they did a subset or not.

* What version of SCA were used for the experiments in Table 2 and Table 3

* Why was it in table 1 there was only a comparison with datasets that included video, as there are a few datasets that deal with the task of classification of human faces

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper pioneers the exploration of interpretable image forgery localization methods and constructs a dataset for image forgery localization with text descriptions. Based on this dataset, the authors propose an explainable image forgery detection method based on MLLM, named ForgeryTalker, which uses the analysis results of MLLM on images as conditions to assist visual models in forgery localization. Experiments on the dataset demonstrate the performance advantages of ForgeryTalker.

### Strengths
- This paper proposes the first interpretable image forgery model addresses the issue of poor explainability in existing models, providing an intuitive output of the tampered areas.
- This paper constructs a large-scale forgery localization dataset and provides corresponding textual annotations, offering more comprehensive and rich information compared to previous datasets.

### Weaknesses
1. The methodology of this paper lacks tight interconnections between the proposed modules. There is a lack of connection between Interpretation and mask prediction, and the output of the LLM does not contribute to the results of tampering localization.
2. The construction of the facial forgery dataset is limited in its methods. The authors could refer to DF40[1] to supplement additional data on facial tampering.
3. The experimental organization of this paper is not very reasonable. For the experiments in Table 2, there is a lack of comparison with the latest multimodal large language models, such as Llava. For the tampering detection experiments, the authors should also supplement performance comparisons with passive methods. Additionally, the paper claims that the method has the capability for forgery localization, yet there is no comparison with forgery localization methods, and there is a lack of visualization results of predicted masks.

### Questions
1. For the Forgery Prompter Network in Figure 2, the authors have indicated that this network requires training, so why is it shown as Frozen in the diagram?
2. The metrics in Table 2 include IoU. IoU does not seem to be commonly used for the output of language tasks. Could the authors provide relevant articles for reference if there is a similar practice?

### Soundness
3

### Presentation
3

### Contribution
3
