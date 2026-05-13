# Self-Supervised High Dynamic Range Imaging with Multi-Exposure Images in Dynamic Scenes

- Decision: Accept
- Scores: 6, 8, 6, 8

## Abstract
Merging multi-exposure images is a common approach for obtaining high dynamic range (HDR) images, with the primary challenge being the avoidance of ghosting artifacts in dynamic scenes. Recent methods have proposed using deep neural networks for deghosting. However, the methods typically rely on sufficient data with HDR ground-truths, which are difficult and costly to collect. In this work, to eliminate the need for labeled data, we propose SelfHDR, a self-supervised HDR reconstruction method that only requires dynamic multi-exposure images during training. Specifically, SelfHDR learns a reconstruction network under the supervision of two complementary components, which can be constructed from multi-exposure images and focus on HDR color as well as structure, respectively. The color component is estimated from aligned multi-exposure images, while the structure one is generated through a structure-focused network that is supervised by the color component and an input reference (\eg, medium-exposure) image. During testing, the learned reconstruction network is directly deployed to predict an HDR image. Experiments on real-world images demonstrate our SelfHDR achieves superior results against the state-of-the-art self-supervised methods, and comparable performance to supervised ones.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a self-supervised method to fuse multi-exposed images in dynamic scenes. It learns a reconstruction network under the supervision of two complementary components, including the color component and the structure component. The color component is estimated from aligned multi-exposure images. The structure one is generated through a structure-focused network that is supervised by the color component and an input image. These components construct a pseudo reference for training.

### Strengths
1. It is a self-supervised method, which overcomes the need for supervised labeled data in supervised methods.
2. Experiments show that our SelfHDR outperforms the state-of-the-art self-supervised methods, and achieves comparable performance to supervised ones.
3. The way of decomposing an image into color and structure components is new.

### Weaknesses
1. The drawback of existing self-supervised methods is that they construct pseudo-pairs for HDR reconstruction. The performance of these methods is unsatisfactory, as their simulated pairs still have gaps with real-world ones. The proposed self-supervised way is also realized by constructing a pseudo reference. Why does this method show advantages? The theoretical discussion and differentiation with existing self-supervised methods are not very sufficient.
2. For dynamic scenes, the method relies on existing registration methods to obtain more accurate color components for registration.
3. This method constructs a pseudo ground truth for self-supervision. The keys lie in the combination optimization (for color components), and mask-based weighting (for structure components). The construction process is simple and mainly based on the functions in Figure 1 which is set by prior.
4. One of the contributions is the construction of a color component. However, it lacks the comparison of the overall results which can directly reflect this advantage in terms of color.

### Questions
1. Does this decomposition way (decomposing an image into color and structure components) have a corresponding theoretical basis, and does it correspond to some existing image decomposition theory?
2. “Regardless of the ghosting areas, the rest can record the rough color value, and in which well-aligned ones can offer both good color and structure cues of HDR images”. The experiment lacks the HDR results in the presence of alignment errors.
3. The mask-based weighting does not consider pixel neighborhood relationships. Will it lead to artifacts?

### Soundness
3 good

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This work proposes a self-supervised HDR reconstruction method SelfHDR for dynamic scenes, which only requires input multi-exposure images during training. Specifically, SelfHDR decomposes latent ground-truth into constructible color and structure component supervisions. Experiments show that SelfHDR achieves comparable performance to supervised ones.

### Strengths
1.This work proposes a self-supervised HDR reconstruction method, addressing the problem of the difficult collection of paired HDR data.

2.The idea of constructing color and structure supervision respectively is somewhat novel.

3.This work achieves competitive results compared to supervised methods.

### Weaknesses
1.Is the performance upper limit of this work limited by the upper limit of structure or color supervision? What designs correspond to solving this problem?

2.This method may also be limited by the alignment method.

3.Some visualizations of structure and color supervision can be given. 

4. Discussion with some traditional multiple exposure fusion methods, such as HDR plus?

### Questions
Please see the above weakness.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents "SelfHDR," a self-supervised High Dynamic Range (HDR) image reconstruction method. Traditional HDR reconstruction methods require ample ground-truth data, which can be difficult and expensive to collect. The novelty in SelfHDR comes from learning a reconstruction network under two complementary components, HDR color and structure, constructed from multi-exposure static images. They designed a detailed process to generate these components and used them to train the reconstruction network. Experimental results showed that SelfHDR surpassed state-of-the-art self-supervised methods and achieved comparable performance with supervised methods. Contributions include a novel solution to alleviate the need for extensive labeled data for HDR image reconstruction.

### Strengths
The originality of the paper is substantial as it proposes an innovative self-supervised method for HDR image reconstruction, eliminating the need for extensive labeled data, a factor that typically hinders HDR reconstruction methods. The quality of the research is commendable. To build this method, they analyzed HDR images thoroughly and isolated the primary components, color, and structure that could be derived from multi-exposure static images. The paper is coherent and clear in its exposition, and the authors elegantly illustrate the problem, their approach, and results. The significance of this work is considerable as it presents a promising alternative for HDR image reconstruction, which demonstrates competitiveness with supervised methods while minimizing data requirements.

### Weaknesses
A potential weakness of the paper is the lack of a broader experimental validation. While they have tested the model on several datasets, the application in real-world scenarios, especially dealing with complex situations and variable lighting conditions, is not clearly examined. The paper could have also delved more into the limitations of the proposed method, such as the cases where the SelfHDR method may not provide optimal results. An exploration of the generalizability limitations of the method would have been appreciated.

### Questions
- How sensitive is the SelfHDR method to the quality of the input images (for example, noise)? Would substantial noise or minor shifts in alignment between images drastically affect the performance of the method? This might be a bit hard to comment on, as the misalignments in the Kalantari dataset are already fixed.
- Have the authors considered combining the SelfHDR method with other techniques (perhaps pre-processing or post-processing techniques) to enhance its performance? For example, use a pre-trained denoising network to process the low-exposure image and use a hallucination network such as Stable Diffusion to generate the content in the over-exposed regions.
- Can the authors provide more insights into the cases where the SelfHDR method might fail or provide subpar results? For instance, are there certain types of scenes, color distributions, or specific types of exposure variations that may destabilize the method?

### Soundness
2 fair

### Presentation
2 fair

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
The paper proposed a self-supervised HDR reconstruction method from a triplet of LDR images with relative motion. The proposed method first prepares two intermediate components focusing on HDR structure and color, and then learns a neural network to estimate the final HDR under the supervision of both. The approach is superior to other self-supervised learning approaches and is comparable to supervised learning methods with regard to objective metrics and visual qualities.

### Strengths
* The idea of using two-stage training to learn structure and color information first and then learn the final output is novel to me. The overall design of the method is reasonable.

* experiments are extensive and demonstrate the compelling performance of the proposed method.

### Weaknesses
* The proposed method is specific to 3 inputs. The 3 inputs should be informatively captured, especially the mid-exposed image, which should have texture and color of high fidelity as the reference. The requirement for the input is strict and can limit the application of the proposed method.

*The authors should point readers to the appendix when appropriate, e.g., visualization of masks and selection of sigmas.

### Questions
The structure-focused network was proposed to avoid errors caused by optical flow alignment, but it is integrated with optical flow alignment in training stage 2, which doesnt make sense to me. Although Tab. 6 shows improvement in general, I think it will hurt the performance in the cases when the alignment has more errors, whereas those cases can demonstrate the core value of the paper. The authors should elaborate on this and experiment on those cases to justify their statement when necessary.

Misc:
* HDR-VDP-2 metric is not as commonly used as PSNR/SSIM. The authors should briefly introduce what the value means, and if a bigger/smaller value indicates better image quality.
* In Tab 3-6 the highest scores can be marked in bold.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
