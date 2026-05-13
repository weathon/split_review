# DiffusionSat: A Generative Foundation Model for Satellite Imagery

- Decision: Accept
- Scores: 8, 3, 6, 8

## Abstract
Diffusion models have achieved state-of-the-art results on many modalities including images, speech, and video. However, existing models are not tailored to support remote sensing data, which is widely used in important applications including environmental monitoring and crop-yield prediction. Satellite images are significantly different from natural images -- they can be multi-spectral, irregularly sampled across time -- and
existing diffusion models trained on images from the Web do not support them. Furthermore, remote sensing data is inherently spatio-temporal, requiring conditional generation tasks not supported by traditional methods based on captions or images. In this paper, we present \model{}, to date the largest generative foundation model trained on a collection of publicly available large, high-resolution remote sensing datasets.
As text-based captions are sparsely available for satellite images, we incorporate the associated metadata such as geolocation as conditioning information. 
Our method produces realistic samples and can be used to solve multiple generative tasks including temporal generation, superresolution given multi-spectral inputs and in-painting. Our method outperforms previous state-of-the-art methods for satellite image generation and is the first large-scale \textit{generative} foundation model for satellite imagery. 
The project website can be found here: \url{https://samar-khanna.io/DiffusionSat/}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a diffusion based remote sensing model able for the following generative downstream tasks: (i) temporal image generation, (ii) multispectral image super resolution, and (iii) image in-painting.


The work is novel as it represents the first diffusion-based remote sensing model. This is interesting given the multi-spectral nature of remote sensing data and the "image caption" adaptations required for the diffusion backbone. Further, the authors adapted ControlNet architecture to a 3d ControlNet architecture to serve their task.

### Strengths
**(S1):** this work presents a novel diffusion-based approach for remote sensing data. It is great to see people extending diffusion to remote sensing data as it is of complex nature given its multi-spectral composition.

**(S2):** this work outlines multiple generative downstream tasks for remote sensing which do go beyond "simple" image generation. This is important because in remote sensing we have no shortage of data and therefore actually not much demand for "simple" image generation.

### Weaknesses
 **(W1)**: the presented work is very domain specific i.e., remote sensing data. It would be interesting to see if this approach is able to generalize to other datasets of similar multi-spectral data. Specifically, the model's architecture and training procedure are tailored for remote sensing imagery, and it is unclear how well it would perform on other multi-spectral datasets with different spectral ranges, spatial resolutions, or noise characteristics. The paper lacks experiments or discussion on the limitations of the model's generalizability, which is a crucial aspect for a novel method.

**(W2)**: I am confused by the "4. Experiment" section. It is not always straightforward to link the tables and images to the different generative downstream tasks presented. And it seems that some results are missing (i.e., the In-painting section/paragraph is missing entirely)? This point also goes hand in hand with my question Q1, Q2, Q3 below: you mention different downstream tasks in the abstract and the method section, and then the results are not consistently reporting on these downstream tasks (as it seems to me, but maybe I misunderstand something). This is the strongest weakness as it renders the evaluation of the methods to be very difficult for the reader of the submitted paper. For example, the "Conditional Generation" section does not clearly specify which conditions are used for each experiment, making it hard to reproduce or compare the results. Furthermore, the lack of a dedicated in-painting section makes it difficult to assess the model's performance on this task, which was highlighted as a key contribution.

### Questions
**(Q1)**: Question for clarification, in your abstract you have mentioned 3 downstream tasks (temporal image generation, multispectral image super resolution, and image in-painting. In your methods section you have mentioned 5 downstream tasks (single-image generation, conditioned on text and metadata, multi-spectral superresolution, temporal prediction, and temporal inpainting). Do you summarize those 5 into the 3 in the abstract? And if yes, why?

**(Q2)**: The "Experiment" section presents results for the following downstream tasks:
"4.1 Single Image Generation", "4.2 Conditional Generation". Then in "4.2 Conditional Generation" results are shown for "super resolution" and "temporal prediction". Finally, the "in-painting" section is missing. This is not in sync with the previously mentioned downstream tasks. Could you clarify the structure of the experiment section?

**(Q3)**: In Table 2, results are presented and compared to other generative methods. Why do you not provide this comparison for Table 1 and Table 3, where results are only compared against non-adapted stable diffusion? Is there any reason for this, if yes, it might be missing in the text body of section 4. I would also recommend to cite the methods you compare to in Table 2.

**(Q4)**: In Fig. 4, which part of the left image is damaged and later in-painted? I see some color-corrections done on the middle image and the ground truth. Is the "damage" done on some specific RGB (or multispectral) channels?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a generative foundation model, i.e., DiffusionSat, for remote sensing data based on the latent-diffusion model architecture of StableDiffusion. Conditioning on freely available metadata as well as generated captions on large, publicly available
satellite datasets makes DiffusionSat a powerful and flexible generative model. Further, a novel 3D ControlNet which allows DiffusionSat to generalize to multi-spectral superresolution, temporal prediction, and in-painting is designed.

### Strengths
This work proposes a generative foundation model for remote sensing data based on StableDiffusion. The proposed foundation model produces realistic samples and can be used to solve multiple generative tasks including temporal generation, multi-spectral superrresolution and in-painting.

### Weaknesses
1. The necessity and motivation of designing the generative foundation model are not clear and convincing. The paper does not adequately articulate why existing methods are insufficient for the specific generative tasks they aim to address in remote sensing. The authors should provide a more detailed analysis of the limitations of current approaches when applied to tasks like temporal prediction or multi-spectral super-resolution, highlighting the unique challenges posed by remote sensing data.

2. The methodology of training the proposed foundation model is not novel since the whole framework is a combination of stable diffusion and ControlNet. The paper lacks a deep dive into the specific modifications or innovations made to adapt these existing architectures for remote sensing data. The authors should elaborate on the technical challenges encountered when applying Stable Diffusion and ControlNet to satellite imagery and explain how their proposed 3D ControlNet addresses these challenges. The novelty of the 3D ControlNet is not clearly established, and the paper should provide a more detailed explanation of its architecture and training process, including a comparison to existing 2D ControlNet approaches.

### Questions
1. The proposed foundation model for satellite images is not novel and significant since there are many foundation models in the remote sensing area, such as  [1-2].
[1] A Billion-scale Foundation Model for Remote Sensing Images. arXiv:2304.05215.
[2] Advancing Plain Vision Transformer Towards Remote Sensing Foundation Model. TGRS, 2022.

2. The authors claim that "while foundation models have been recently developed for discriminative learning on satellite images, no such foundation model exists for generative tasks. " Please explain why the existing foundation models are not applicable to the generative tasks.

3. The methodology of training the proposed foundation model is not novel and the authors only apply the stable diffusion model to the satellite images. Although the authors use some new conditional inputs in the stable diffusion framework, it is not novel enough for publication in this conference.

4. What is the purpose of conducting research on the generative foundation model? Please make a discussion for this point.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Authors propose DiffusionSat which is a Stable Diffusion (SD) inspired generative model to generate satellite imagery. The imagery generation can be conditioned satellite imagery metadata. To be able to train this model authors had to generate a large-scale satellite imagery pretraining dataset by combining multiple open datasets, generating text descriptions, and adding metadata available. Work was done to encode the conditioning metadata properly. The pretrained model was tested in multiple downstream tasks we competitive performance.

### Strengths
* This paper tackles an important problem with understady on the computer vision field with impotant possitive societal benefiting applications
* Novel incorporation of additional metadata and problem setup and can spin off a new line of work in geospatial ML
* The generated dataset used for this study can be very useful in other applications.

### Weaknesses
 * **Results for certain tasks are missing or incomplete.** The paper mentions that they show state-of-the-art results for super-resolution, temporal generation, and in-painting. However, only a single qualitative example is provided as result. Also multiple other relevant approaches have been proposed. Superresolution results just compare the proposed approach with Stable Diffusion baseline but ignores the line of work done in the field including [1,2] and others. The lack of quantitative results and comparison with relevant baselines makes it difficult to assess the true performance of the proposed method in these tasks. The in-painting results are particularly lacking, with no quantitative evaluation and only a single, hard-to-interpret qualitative example.
* **The paper write up needs work to improve cohesion.** The related work section could be merged into the background. The task description coud be joint with the results since bothe are very brief. The current structure makes it difficult to follow the logical flow of the paper and understand the context of the experiments. The separation of task descriptions from results makes it challenging to evaluate the experimental setup and its relevance to the stated goals.
* **Overall evaluation and results comparison.** There are multiple other approaches for satellite image generation including conditional that this approach does not compare against. [1]  If the focus wants to be on using this model as foundational model for other geospatial ml tasks, then comparison with other self-supervised and/or foundational models is important. The paper should include a more comprehensive comparison with existing methods, including those that utilize similar conditional generation techniques. The lack of comparison with other foundational models limits the assessment of the proposed method's potential as a general-purpose model for geospatial tasks.

### Questions
1. It is very difficult to see the inpainted damage referred to in Figure 4. Please consider highlighting the area where damage has been inpainted. 
2. Abstract missing dot after "remote sensing datasets"
3. No text under "In-painting" subsection within the experiments section.
4. Share more examples of generated images

### Soundness
3 good

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a stable diffusion variant, called DiffusionSat, designed for satellite image synthesis tasks. The proposed approach leverages text captions, an assortment of satellite image metadata (longitude, latitude, GSD, etc.), and sequences of images to address various overhead image problems, such as varying spatial resolution (GSD), cloud cover, and seasonality.  DiffusionSat shows strong performance across multiple tasks (super-resolution, temporal generation, and in-painting) on three repurposed datasets.

### Strengths
- Tackles an important and interesting problem, view synthesis in remote sensing.

- Well-written, clear motivation.

- Method has the potential to positively impact the remote sensing community.

  DiffusionSat operates on a sequence of satellite images (with varying spatial resolution) and applies attention across time via a temporal pixel-transformer. This allows the approach to leverage an image sequence to address the shortcomings that may be present in any individual image (e.g., clouds). While the underlying temporal transformer was introduced by VideoLDM (Blattmann et al., 2023), its application to remote sensing problems is still valuable.  Further, the proposed method allows satellite image synthesis to be controlled using metadata and text. For example, synthesizing images with seasonality (summer grass vs winter snow), location (France vs.  USA), and ground sample distance.

- The authors introduce a new temporal generation task using satellite image datasets. This task targets common issues with using satellite image sequences, namely that the interval between images is not fixed and that frames can have varying GSD.

- Evaluation is fairly extensive.

### Weaknesses
 - Limited technical novelty. 

  The proposed method reduces to a straightforward way of embedding metadata and then conditioning a stable diffusion model on said metadata. The temporal transformer component is from VideoLDM.

- Quantitative performance across multiple tasks is strong, but not convincingly better than existing approaches. While the proposed method does achieve SOTA performance on some metrics on some benchmarks, it doesn't show consistent enough performance across the board to substantiate the claim that the method is SOTA on all these tasks, as the introduction indicates.

- The approach and evaluation are limited for multi-spectral imagery (MSI).
	
  This work does not address the issue of varying image band GSD (e.g., Sentinel-2 bands) in MSI, despite claiming to support MSI synthesis. For various remote sensing products, image bands may not all be the same GSD. Some effort should be taken to recognize this occurrence, since 10m -> 1.5m super-resolution is far easier than 20m->1.5m (Sentinel-2 bands 5, 6, 7, 8a, 11, and 12) or 60m -> 1.5m (Sentinel-2 bands 1, 9, and 10) [1] super resolution.

  [1] https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi/resolutions/spatial
	
  The MSI super-resolution problem aims to synthesize 3-band WV3 imagery from 13-band Sentinel-2 imagery. While this may be useful in some scenarios, it does leave out a fairly significantly problem, namely, generating all spectral bands. As such, the method does not really perform MSI synthesis, but rather can support MSI inputs for RGB super-resolution.

- Figure 4 is not informative as the disaster-related damage is difficult to identify. Consider highlighting damaged areas, or use a more clear example.

- Minor editing problems: leftover question mark (page 4), repetitive text (bottom of pages 1 and 3), typo and highlighting on page 8, etc.

### Questions
My initial rating is weak accept. The proposed approach is interesting and has novelty in its formulation. The manuscript is well written and the results are compelling. Ultimately, I think this paper will have a positive impact on the community.

For the fMoW super-resolution task, are the super-resolved images multi-spectral or just RGB? The text seems to suggest that the model takes in a 13 band Sentinel-2 image and outputs a reconstruction of a 3 band WorldView-3 image from fMoW. Is the reconstruction limited to just 3 bands (R, G, B)? If so, then the task isn't actually multi-spectral super-resolution.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good
