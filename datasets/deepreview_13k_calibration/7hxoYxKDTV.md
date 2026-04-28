# Continuous-Multiple Image Outpainting in One-Step via Positional Query and A Diffusion-based Approach

- Decision: Accept
- Avg Score: 6.67
- Scores: 8, 6, 6

## Abstract
Image outpainting aims to generate the content of an input sub-image beyond its original boundaries. It is an important task in content generation yet remains an open problem for generative models. This paper pushes the technical frontier of image outpainting in two directions that have not been resolved in literature: 1) outpainting with arbitrary and continuous multiples (without restriction), and 2) outpainting in a single step (even for large expansion multiples). Moreover, we develop a method that does not depend on a pre-trained backbone network, which is in contrast commonly required by the previous SOTA outpainting methods. The arbitrary multiple outpainting is achieved by utilizing randomly cropped views from the same image during training to capture arbitrary relative positional information. Specifically, by feeding one view and positional embeddings as queries, we can reconstruct another view. At inference, we generate images with arbitrary expansion multiples by inputting an anchor image and its corresponding positional embeddings. The one-step outpainting ability here is particularly noteworthy in contrast to previous methods that need to be performed for $N$ times to obtain a final multiple which is $N$ times of its basic and fixed multiple. We evaluate the proposed approach (called PQDiff as we adopt a diffusion-based generator as our embodiment, under our proposed \textbf{P}ositional \textbf{Q}uery scheme) on public benchmarks, demonstrating its superior performance over state-of-the-art approaches. Specifically, PQDiff achieves state-of-the-art FID scores on the Scenery (\textbf{21.512}), Building Facades (\textbf{25.310}), and WikiArts (\textbf{36.212}) datasets. Furthermore, under the 2.25x, 5x and 11.7x outpainting settings, PQDiff only takes \textbf{40.6\%}, \textbf{20.3\%} and \textbf{10.2\%} of the time of the benchmark state-of-the-art (SOTA) method.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Most image outpainting method is limited by the requirement of a pre-defined output ratio before training the models. The authors propose a diffusion-based framework to solve this problem by introducing a positional query. The framework can generate output images with arbitrary and continuous ratios within one step.

### Strengths
- 1) The authors solve an interesting lasting problem in image outpainting research: the requirement of a pre-defined outpainting multiple.
- 2) The extensive experiments prove the superiority of the proposed framework in comparison to sota.
- 3) The paper is mostly well-written with a clear explanation of the methodology and implementation

### Weaknesses
1. Question regarding the wording of the contribution or the presentation in Fig. 1. See Q1.
2. More results are needed to justify the claim of continuous results. See Q2.

### Questions
## Questions
- 1) Is it precise to say that PQDiff handles inputs with various sizes and ratios while the output size is fixed? Assume the goal is to generate an outpainting image with a multiple of 10x given an input image of size (192, 192). Does PQDiff generate a (192, 192) version of the 10x outpainting image and have to leverage an additional decoder (perhaps super-resolution methods) to resize it to (1920, 1920)?

- 2) Can the author provide results on more multiple besides (2.5x, 5x, 11.7x) used in other sota to justify their claim of continuous multiples? For example, how is the performance of 99x? My suggestion would be a figure of FID over continuous multiples or spectrums of outpainting images with increasing multiples.

- 3) What is the quantitative evaluation of Sec 4.2 **Outpainting in an arbitrary position**, i.e. FID under different positions? Does the model prefer certain positions?

## Suggestion
- 1) The generated and input images in Supp. Sec. J (Fig. 11, 12, ...) can be put side by side for clearer comparison.

### Soundness
3 good

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Image outpainting is practically useful yet very challenging, and current methods often require a fixed ratio of the input and output resolution beforehand. Specifically, the devised PQDiff is a single model trained for all outpainting ratios, by introducing a position query in diffusion training. The proposed method can generate output images with arbitrary and continuous multiple. Such abilities are often missing in literature.

### Strengths
1) The paper provided a simple yet elegant and effective approach for the challenging and important task of image outpainting. Specifically, it can naturally ensure the outpaint images with continuous multiple, and also generates the output in a single forward pass. 
2) This paper shows that the position query techniques can also be applied to GAN-based models which further expand the potential impact of the paper.
3) The experimental results propsoed in Sec. 4 are convincing, in terms of both quantative results and qualitative results. Meanwhile the method is very efficient due to its single-pass inference nature against arbitary input ratio and continuous multiple.
4) Supplemental material gives detailed empirical studies to verify the effectiveness of the approach.

### Weaknesses
I think the authors should further discuss the potential of their method to other potential applications beyond outpainting to further expand the potential impact of this work.

### Questions
Are there other methods using POSITIONAL QUERY? As current existing work part does not mention them (is there were) too much.

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
This paper proposes an diffusion-based image outpainting model that can outpaint images with arbitrary and continuous multiples. This is achieved with the help of the relative positional embedding that can encode any relative position relations. Experimental results validate the effectiveness of the proposed model.

### Strengths
1. The target of outpainting images with arbitrary and continuous multiples is very attractive and highly practical.
2. Using relative positional embedding to deal with the problem of arbitrary and continuous multiples is simple but effective.

### Weaknesses
1. The main weakness of this paper is some unclear explanations and descriptions.

(1) The authors categorize existing methods into two classes, GAN-based and MAE-based methods, and emphasize that one of their  limitations is  the multiple running times to achieve the large expansion multiple. However, it is unclear why these two types of methods need to run multiple times. Using GAN or MAE is not the crux.

(2) As the authors fail to clearly explain why previous methods cannot outpaint images with arbitrary and continuous multiples. The strengths and the contributions of the proposed method become unclear and unconvincing.

(3) The authors say "to achieve one-step diffusion-based generation, we propose to use relative positional queries and input sub-images as conditions". This is really strange. Why relative positional queries can reduce the number of diffusion steps?

(4) In section 3, the authors say that they set h1 = h2 = h and w1 = w2 = w for notation simplicity. It looks improper.

(5) Some parts of Figure 2 are confusing. For example, in the training part, the relative positional embedding takes the two image views as inputs. But Eq.1 shows that only the relative position (m,n) is needed to generate the embedding. The images are not the inputs of it. In the sampling part, it is unclear what the inputs are. I cannot know which of the original image, the cropped image, and the masked image are the inputs

(6) In Eq.2, it seems Xb0 should be Zb0

2. There is a strange point in the proposed model. As shown in Figure 2, the relative position only reflects the position relations of the top-left corners between the two views. In other words, even the anchor view and the relative position are fixed, there can still be many different target views. How does this one-to-many mapping influence the model? Furthermore, in the sampling stage, if the input noise, image and relative position are all fixed, how to ensure the outpainting ratios on four edges are the same as what we expected?

### Questions
The questions and confused points are given in Weakness Section. I am looking forward to the responses from the authors. I may improve my rating if the questions have satisfactory answers.

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
