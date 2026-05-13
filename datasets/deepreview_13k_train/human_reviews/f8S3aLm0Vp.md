# DIAGNOSIS: Detecting Unauthorized Data Usages in Text-to-image Diffusion Models

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Recent text-to-image diffusion models have shown surprising performance in generating high-quality images. However, concerns have arisen regarding the unauthorized data usage during the training or fine-tuning process. One example is when a model trainer collects a set of images created by a particular artist and attempts to train a model capable of generating similar images without obtaining permission and giving credit to the artist. To address this issue, we propose a method for detecting such unauthorized data usage by planting the injected memorization into the text-to-image diffusion models trained on the protected dataset. Specifically, we modify the protected images by adding unique contents on these images using stealthy image warping functions that are nearly imperceptible to humans but can be captured and memorized by diffusion models. By analyzing whether the model has memorized the injected content (i.e., whether the generated images are processed by the injected post-processing function), we can detect models that had illegally utilized the unauthorized data. Experiments on Stable Diffusion and VQ Diffusion with different model training or fine-tuning methods (i.e, LoRA, DreamBooth, and standard training) demonstrate the effectiveness of our proposed method in detecting unauthorized data usages. Code: https://github.com/ZhentingWang/DIAGNOSIS.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method to detect unauthorized data usage during the training or fine-tuning process in text-to-image diffusion models. This unauthorized data includes cases where a model can collect images of an artist without permission or generate similar images without giving credit to the artist. The paper addresses this issue by modifying the protected data by planting an injected memorization in the training of the diffusion model. This is done by adding unique contents on the protected image data using stealthy image warping functions that are not perceptible to humans but captured and memorized by diffusion models. The model is then analyzed whether it has the injected content and unauthorized data is detected this way. Experiments are presented on many state-of-the-art diffusion models.

### Strengths
The paper is written well and the problem that the paper is trying to address is clearly illustrated. Some visual examples are also provided. Results are also shown on many recent text-to-image diffusion models.

### Weaknesses
Lots of experiments are presented. It will be good to have a robustness analysis also with these experiments. How robust is the proposed method to different image transformations like compression, blurring, smoothening, sharpening and more. Will this affect the detection performance?

It will be good if the authors can discuss adversarial ways in which the proposed technique can be defeated.

### Questions
None

### Soundness
3 good

### Presentation
3 good

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
The paper addresses concerns related to unauthorized data usage in the training or fine-tuning process of text-to-image diffusion models. The authors highlight the potential misuse of data, where a model trainer might utilize images without proper permission or credit. To tackle this issue, the paper proposes a method that detects unauthorized data usage by implanting injected memorization into protected datasets during model training. This involves stealthy image-warping functions that remain imperceptible to humans but can be captured and memorized by diffusion models. By analyzing the presence of the injected content, the proposed method can effectively identify models that have illegally employed unauthorized data. The experiments conducted on various text-to-image diffusion models, including Stable Diffusion and VQ Diffusion, using different training or fine-tuning methods, demonstrate the efficacy of the proposed detection approach.

### Strengths
1) The paper addresses the issue of unauthorized data usage within text-to-image diffusion models, a critical and pressing concern within the artistic field. It presents a potential solution to safeguard the copyrights of artistic creators.
2) The solution is sound and solid, which is quite easy to follow. The authors borrow some ideas from image warping and injected memorization into the task.

### Weaknesses
1) Some typos and grammar errors exist, e.g., pp. 7, "we assume the subsets provide by different data sources..." should be "we assume the subsets provided by different data sources".
2) In the experimental results section, the authors shall provide more quantitative results (in terms of, e.g., PSNR, SSIM or the residual) for comparing the original sample image and its coated counterpart. The lack of such metrics makes it difficult to assess the imperceptibility of the image warping and its impact on image quality. It is important to know the magnitude of the changes introduced by the warping, and whether these changes could potentially affect the training process or the utility of the images for other tasks. Without these metrics, it is hard to judge the trade-off between imperceptibility and the effectiveness of the proposed method.

### Questions
1) Why use image-warping operation to implement the coating? Is it possible to employ some other operators?
2) Does the image warping is reversible? It seems that the coated images are permanently damaged by the warping.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new scheme to detect the unauthorized data usages in text-to-image diffusion models, where the images are imperceptibly warped for protection. The warped images are able be memorized by diffusion models during the training, which offers the possibility to detect the existence of the usages of such data from the trained diffusion model.

### Strengths
1. It is an interesting approach by exploring the properties of the diffusion models, i.e., memorizing duplicated contents in the training data, for the detection of unauthorized data usages.

2. This paper is well written and easy to follow.

3. Good robustness over different diffusion models.

### Weaknesses
1. The authors mention that, compared with the sota schemes which focus on the sample-level memorization, this paper focuses on the element-level memorization. I think it does not matter whethat it is sample-level or element-level, the most important is which one offers higher performance. The authors do not logically or experimentally justify the advantage of element-level memorization over the sample-level ones.

2. The motivation of introducing two types of injected memorization is not well explained. The reviewer is confused with the necessarity of the trigger function. 

3. Insufficient Evaluation. Only less than 20 models are constructed during the evaluations, which is far from enough to demonstrate the effectiveness of the approach. It lacks of evaluation regarding the distortion of the image after the warping. It also lacks the discussion on the potential countermeasures against the proposed approach.

4. What is the value of the coating rate used in section 4.2? If only a small portion of the data is protected, it is quite strange that selecting only a portion from the whole dataset to train the model would still be accurately detected with 100% accuracy. If the selection does not overlap with the protected portion, the detection mechenism should not work, right?

### Questions
1. What is the value of the coating rate used in section 4.2? If only a small portion of the data is protected, it is quite strange that selecting only a portion from the whole dataset to train the model would still be accurately detected with 100% accuracy. If the selection does not overlap with the protected portion, the detection mechenism should not work, right?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on protecting the training data and detecting unauthorized training data usages in the text-to-image diffusion models. In detail, this paper first defines two types of element-level injected memorizations on the text-to-image diffusion models. Based on the definition of the injected memorizations and their memorization strength, this paper introduces an approach for detecting unauthorized training data usages in the text-to-image diffusion models. In detail, the proposed method modifies the protected dataset by adding designed unique and invisible contents (signal contents) on these images, so that the model will learn the memorizations on the signal contents if it has unauthorized training or fine-tuning on the protected training data. Experiments on four datasets and recent diffusion models (Stable Diffusion and VQ Diffusion) indicate the performance of the proposed method is good.

### Strengths
1. [Novelty & Motivation] This paper links the unauthorized
training data usages problem to the memorization of the
text-to-image diffusion models, which is an novel and
interesting direction. The design of the proposed method is
reasonable. The motivation of this paper is clear. Detecting
unauthorized training data usages in the diffusion models is
an important and urgent problem, but it have not been
well-studied by existing works.

2. [Studied Models] The experiments are conducted on the
state-of-the-art text-to-images diffusion models in the
real-world (Stable Diffusions) and advanced model
training/personalization techeniques (LoRA and Dreambooth).

3. [Practicality] The proposed method only requires the
black-box access to the examined models, which makes it
practical in real-world usages.

4. [Performance] The detection performance of the
proposed method is high, it achieves 100% detection accuracy
among various settings with nearly unnoticable perturbations
on the training/generated samples. The comparisons to
existing methods or potential other methods are
well-discussed in the introduction and the evaluation.

5. [Writting] Overall, the presentation is good, and the
writing is easy-to-follow.

### Weaknesses
1. [Texutal Inversion] Is it possible to detect the
unauthorized data usages with Textual Inversion [1] (a
personalization technique the for text-to-image diffusion
models)? It is unclear how the proposed method would perform if an adversary uses Textual Inversion to fine-tune the model on protected data, as this technique learns new tokens that can represent specific concepts. The current evaluation does not consider this scenario, which is a significant gap given the prevalence of such techniques.

2. [Efficiency] I did not find the discussion about the time
cost of the proposed method. Helping the potential users
know the approximated time cost is benificial. The paper should provide a breakdown of the computational cost for each stage of the proposed method, including the image coating process, signal classifier training, and the detection algorithm. This would allow for a better understanding of the method's scalability and practical applicability.

3. [Summary Table for Symbols] A table summarizing the
meaning of all symbols used in this paper can be added to
make this paper more clear.

### Questions
Please see "Weaknesses".

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent
