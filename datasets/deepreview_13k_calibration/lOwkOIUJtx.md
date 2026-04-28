# Improved Efficiency Based on Learned Saccade and Continuous Scene Reconstruction From Foveated Visual Sampling

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
High accuracy, low latency and high energy efficiency represent a set of contradictory goals when searching for  system solutions for image classification and detection. While high-quality images naturally result in more precise detection and classification, they also result in a heavier computational workload for imaging and processing, reduce camera refresh rates, and increase the volume of data communication between the camera and processor. Taking inspiration from the foveal-peripheral sampling mechanism, saccade mechanism observed in the human visual system and the filling-in phenomena of brain, we have developed an active scene reconstruction architecture based on multiple foveal views. This model stitches together information from foveal and peripheral vision, which are sampled from multiple glances. Assisted by a reinforcement learning-based saccade mechanism, our model reduces the required input pixels by over 90\% per frame while maintaining the same level of performance in image recognition as with the original images. We evaluated the effectiveness of our model using the GTSRB dataset and the ImageNet dataset. Using an equal number of input pixels, our study demonstrates a 5\% higher image recognition accuracy compared to state-of-the-art foveal-peripheral vision systems. Furthermore, we demonstrate that our foveal sampling/saccadic scene reconstruction model exhibits significantly lower complexity and higher data efficiency during the training phase compared to existing approaches.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper presents a novel application of spatially-varying computation (foveation) coupled with eye-movements towards the goal of image reconstruction. The authors introduce an active sensing model that takes into account all of the image information in a spatially varying way and continually updates the visual stimulus until it is near perfectly reconstructed. Authors introduce a novel loss function and show small toy experiments that prove their claims.

### Strengths
- This paper presents a novel application of foveal-peripheral vision tailored towards image reconstruction.
- The paper has shown and presented a set of experiments that seem to support their claimed contribution
- The paper has references many other works in perceptual psychology and neuroscience -- though many more of these papers are missing, and the field has moved forward quite a lot (see Weaknesses below), thus potentially impacting the novelty of the paper.

### Weaknesses
I think the main weakness this paper has is I am confused on how the system is trained to do reconstruction. Is it doing the reconstruction from the same image and "testing on the training set"? Otherwise, I am surprised the first auto-completion of the image is surprisingly quite well without any prior knowledge of the underlying geometry of the visual stimulus. If indeed it is testing on the training set, what would be the contribution/application of such system? A compression engine that works better than JPEG, or would the contribution here really be more of an intellectual one of saying that reconstruction through foveation is indeed possible.

-------
There are a set of missing papers that the authors should add and/or discuss in this work. While none of these papers directly attack the problem of using foveation as a tool for reconstruction, many of such works discuss the complimentary theory of foveation having a representational goal in addition to purely optimizing for metabolic cost (and thus limiting the impact of the authors through this paper)

Key Missing Critical References:
- Deza & Konkle. ArXiv, 2021. Emergent Properties of Foveated Perceptual Systems.
- Wang & Cottrell. Journal of Vision, 2017. Central and peripheral vision for scene recognition: A neurocomputational modeling exploration.
- Cheung, Weiss & Olshausen. ICLR 2017. Emergence of foveal image sampling from learning to attend in visual scenes

Secondary, but also important References:
- Gant, Banburski & Deza. SVRHM, 2022. Evaluating the adversarial robustness of a foveated texture transform module in a CNN.
- Reddy, Banburski, Pant & Poggio. NeurIPS 2020. Biologically inspired mechanisms for adversarial robustness
- Wang, Mayo, Deza, Barbu & Conwell. SVRHM, 2021. On the use of Cortical Magnification and Saccades as Biological Proxies for Data Augmentation
- Harrington & Deza. ICLR, 2022. Finding Biological Plausibility for Adversarially Robust Features via Metameric Tasks

In addition the original SSIM paper:
- Wang, Bovik, Sheik & Simoncelli. IEEE TIP, 2004. Image quality assessment: from error visibility to structural similarity (SSIM).

and Foveation paper that introduce the idea of texture-based computation in the periphery:
- Freeman & Simoncelli. Nature Neuroscience, 2011. Metamers of the Ventral Stream.

### Questions
I am open to changing my mind about this paper. There are a lot of missing papers, but the idea seems interesting. I am fan of papers that explore non-intuitive applications or theories of foveation but I am still not there yet to give this paper a clear accept.

I'm also struggling to know what is $t_0$? Is it a blank image? Is it a corrupted image? Is it only a fraction/glimpse of an image?

### Soundness
2 fair

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
The authors present an innovative solution for image classification and detection that addresses the trade-off between image quality and computational efficiency. They introduce an active scene reconstruction architecture that leverages foveal and peripheral views, along with a reinforcement learning-based saccade mechanism, reducing input pixels by over 90% per frame while maintaining image recognition performance.

### Strengths
- The paper introduces an innovative concept inspired by the human visual system, combining foveal and peripheral views with a saccade mechanism in image reconstruction. This approach has potential applications in various fields.
- A 90% reduction in required input pixels per frame has practical implications for real-time image processing
- paper is easy to read

### Weaknesses
 - Although the paper addresses the trade-off between image quality and computational efficiency, it would be valuable to provide insights into the computational overhead of implementing the proposed model, particularly in terms of hardware and energy requirements.
- The paper totally fails to mention a whole branch of literature in saccade modeling. See for example [1], [2], or  [3]. In particular, [2] also uses reconstruction as a guiding task. It seems true that none of the mentioned approaches focused on performance in terms of image reconstruction, but I think it is relevant to at least position the current contribution compared to those. I imagine, some of these saccade models could potentially be used in the same framework proposed by the authors here.

### Questions
- Can you provide more details about the computation overhead of your model and possible complications in real world applications?
- Can you better frame your contribution, and compare it to the literature in saccade modeling?

### Soundness
3 good

### Presentation
2 fair

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
This paper aims to reconstruct the original image from multiple subsampled views, using reinforcement learning and neural network models for scan control and image reconstruction, respectively. The paper conducts numerous experiments to demonstrate that the proposed algorithm can maintain detection task accuracy, reasonable saccade control, and high reconstruction quality under high data efficiency. However, the motivation for the work is not well-founded, and there are possible improvements in the experiments.

### Strengths
1. The task addressed in the paper is novel, as it is the first in the industry to reconstruct an image from continuous central foveal subsampled images. Other methods focus on single-sample images and proceed directly to downstream tasks without reconstructing the original image, making this work unique.
2. The methods used are innovative, employing an actor-critic model for saccade control, which can achieve near-original image classification accuracy in just five scans.
3. The writing style of the paper is easy to understand, especially in describing the proposed methods.

### Weaknesses
1. While the task is novel, it lacks a convincing real-world application, as it simulates the process of multiple eye samplings without addressing practical problems.
2. The experimental comparisons are not entirely fair. The uniform control group uses an 8% sampling probability, while the 1/16+2% group differs by 0.25%, indicating an unequal amount of information that might affect performance.
3. Using classification model metrics to assess the quality of reconstruction is questionable, as classification tasks do not focus on texture details. If this method was to downsample the original image with the same number of sampled pixels, how much better is the method in terms of performance compared to this?

### Questions
see weaknesses

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a new algorithm for sequential foveated visual sampling of an image.

The main claims of the paper are that 

- the required input pixels per frame are reduced by 90% without losing image recognition performance
- 5% higher recognition accuracy compared to existing foveal sampling models with matching pixel number input
- higher data efficiency in training

I find the algorithm to be interesting and novel, and that the second and third claims above are supported.
I am confused where to find evidence for the first claim.

Overall I think this paper is a borderline accept.

### Strengths
I find the method simple and useful, with interesting potential application. 
It is appealing that the method seems to be suitable for existing classification models (no retraining).

### Weaknesses
## Major

I am confused how the image information from the sequential glimpses is passed and integrated in the predictive reconstruction model. Much more space is spent on the background to the hybrid loss function than actually making explicit how the sequential image information is used to improve reconstruction. Specifically, the paper lacks a detailed explanation of the architecture used to process the sequential glimpses. It is unclear how the ConvLSTM layers are structured, what their input and output dimensions are, and how the hidden states are initialized and updated across timesteps. Without this information, it is difficult to assess the novelty and effectiveness of the proposed method. A more detailed description of the network architecture, including the number of channels, kernel sizes, and activation functions, is needed to fully understand the model.

In addition, the abstract states "our model reduces the required input pixels by over 90% per frame while maintaining the same level of performance in image recognition as with the original images." I don't understand where to find support for this claim in the results. For example, in Figure 3, all subsampled models perform worse than the original. The data in Figure 4 are coming closest to the original; is this what is meant? It is not clear what the baseline is for the 90% reduction claim, and the paper should explicitly state which experiment supports this claim. The paper should also clarify whether the 90% reduction refers to the total number of pixels used across all glimpses, or the number of pixels used per glimpse. The lack of clarity makes it difficult to evaluate the practical significance of the proposed method.

Also, please clarify whether the experiments in Figure 3 are conducted with the trained saccade control model (which one?).


## Minor

- Instead of "continuous saccades" a better terminology would be "sequential saccades" or "scanpaths". See e.g. [2, 3, 4]
- There are now known to be three types of photosensitive cells: rods, cones and intrinsically-photosensitive ganglion cells [1, 8]
- You use SSIM but the relevant paper(s) are not cited (e.g. [7]).
- Heading 3.1 "Periphrl"

### Questions
- I would like to see how the hybrid reconstruction loss changes over timestep, and not just classification accuracy.
- The sampling of the periphery of individual pixels with small probability is not very like human vision. Effectively this is providing low pass information. Have the authors considered how the sampling density could be approximated more plausibly (e.g. [6])?
- Have the authors considered comparing scanpath strategies learned in this model to human scanpaths (e.g. [3, 4])?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
