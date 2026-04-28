# Seeing Video Through Optical Scattering Media using Spatio-Temporal Diffusion Models

- Decision: Reject
- Avg Score: 6.33
- Scores: 5, 8, 6

## Abstract
Optical scattering causes light rays to deviate from their trajectory, posing challenges for imaging through scattering media such as fog and biological tissues. Although diffusion models have been extensively studied for various inverse problems in recent years, its extension to video recovery, especially through highly scattering media, has been an open problem due to the lack of a closed-form forward model and the difficulty of exploiting the spatio-temporal correlation. To address this,  here we present a novel inverse scattering solver using a video diffusion model. In particular, by deriving a closed-form forward model from the shower-curtain effect in a dynamic scattering medium, we develop a video diffusion posterior sampling scheme using a diffusion model with temporal attention that maximally exploits the statistical correlation between a series of frames and a series of scattered signals. Unlike previous end-to-end approaches only relied on spatial correlation between a scene and a scattered signal at a specific time point, the adaptability of the proposed method is highly extendable to various types of scenes, various thicknesses of scattering media, and varying distances between a target scene and a medium.  In particular, the use of temporal correlation is shown to be critical to faithfully retrieve high-frequency components which are often missed by inverse operations only in spatial domain.  Experimental results using the video datasets of moving sperm cells verify the effectiveness of the proposed method. To the best of our knowledge, this is the first video diffusion model to jointly utilize the correlations in both spatial and temporal domains in solving the inverse scattering problem.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes applying video diffusion models to the task of reconstructing video captured through scattering media. Specifically, this paper focuses on scenarios where the scattering is approximated by the so-called shower curtain effect, where the forward operator essentially reduces to a Gaussian blur kernel. The proposed method is based on posterior sampling given a pre-trained video diffusion model, supposedly containing prior knowledge of natural videos. The restoration of the original video is equivalent to doing a posterior sampling of the video diffusion model, conditioning on the blurry measurements. The evaluation of the proposed method is mainly done on two existing natural video datasets, and the scattering effect is simulated.

### Strengths
- This paper tackles an important problem of imaging through scattering.
- Incorporating diffusion models in the context of imaging through scattering is new.

### Weaknesses
 - This paper only contains restoration results from **simulated** scattering. No successful restoration on any real-world scattering were demonstrated.
- This paper only focuses on a naive special case of scattering, where the forward operator is trivially a Gaussian blur. Real-world scattering is much more complicated can requires the modeling of phase error caused by the scattering medium. The assumption of a Gaussian blur kernel severely limits the applicability of the method to realistic scenarios, where the point spread function (PSF) of the scattering medium is often spatially varying and exhibits complex speckle patterns. This simplification ignores the fundamental physics of light propagation through scattering media, which involves multiple scattering events and interference effects.
- Ignoring the significance on the problem of optical scattering, the technical contribution on the algorithm side is very limited. The paper introduces minimal changes to existing approaches that apply the diffusion posterior sampling strategy on other inverse problem tasks. The application of diffusion models to inverse problems is well-established, and this paper does not present any novel algorithmic contributions in this regard. The adaptation to video data by using a video diffusion model is a straightforward extension, lacking significant technical depth.
- This paper does not include literature review on the problem of imaging through optical scattering, and fails to cite recent papers that could give the readers a more complete perspective on the state-of-the-art, such as:
  - Imaging with local speckle intensity correlations: theory and practice, ACM Transactions on Graphics, 2021
  - Guidestar-free image-guided wavefront shaping, Science Advances, 2021
  - Prior-free imaging unknown target through unknown scattering medium, Optics Express, 2022
  - NeuWS: Neural wavefront shaping for guidestar-free imaging through static and dynamic scattering media, Science Advances, 2023.

### Questions
What's stopping the proposed method from successfully working on real-world scattering? Can the proposed framework handle more sophisticated forward model?

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
An original method is proposed to remove dynamic blur in a moving video by taking advantage of spatial and temporal correlations. The  approach consists in introducing temporal aspect in the 2-dimensional posterior sampling (DPS) approach, a similar extension allowing to extend Diffusion models as Video Diffusion Models (VDM). The proposed approach needs tha the diffusion layer is not to thick and that the scene is enlighten with a laser. Comparative experiments are proposed with convincing results.

### Strengths
The possibility to take fully advantage of the spatial and temporal correlations is very interesting and useful. The proposed results are very convincing about the superiority of the proposed approach. A source code with example is provided.

### Weaknesses
The paper is well introduce and clearly explain but the derivations in appendix are quite hard to follow. It is not derivations but sketchs of derivations. A reference to a technical report with the derivations will be very useful. The description of the forward model, while conceptually clear, lacks sufficient detail to allow for a thorough understanding of the underlying mathematical framework. Specifically, the assumptions made regarding the scattering kernel and its Gaussian approximation are not rigorously justified, and it is unclear how these approximations impact the overall performance of the method. The paper would benefit from a more detailed explanation of the forward model, including a step-by-step derivation of the equations and a discussion of the limitations of the chosen approximations.

### Questions
I was not able to find the description about the learning step in the paper. May you tell more about this important step ?

### Soundness
3 good

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
This paper considers the problem of seeing dynamic scenes through scattering media. The authors propose a 3D convolution architecture that can take into account temporal correlation for the task of de-scattering the video sequence. Using a diffusion model prior regularizes the solution space of the inverse problem.

### Strengths
The paper tried to tackle a difficult problem using state-of-the-art generative AI approaches. They show that taking into account temporal correlations helps with the reconstruction of dynamic scenes undergoing scattering. They validate the approach as compared to a traditional TV approach and a 2D-based deep learning approach and show that using deep learning in video space improves the reconstruction quality.

### Weaknesses
The key issue and the reason I chose a rating of 2 for the presentation is the lack of contextualization for this work. While the authors do a good job comparing to some baselines like a TV method and a 2D approach the problem of seeing through scattering media has a long history, which this paper largely ignores. This problem arises in the context of de-hazing and underwater imaging (see e.g. Akkaynak et al and Berman et al below ). I also point out that the inverse problem is very similar to the DiffuserCam proposed by Antipa et al. Further works by Satat et al. Bar et al. Alterman et al. all looked into seeing through scattering and Bar et al. offer a simple model for speckle formation. Lastly, the discussion on speckles seem redundant as the paper reduces the model to a simple convolution with a gaussian kernel. This opens the discussion to a whole host of works done on blind and non-blind deconvolution.

The other major issue I have is that all the results and experiments assume a simple convolution model to generate data and then show the recovery based on that model. This means that there is no model mismatch at all. I would like the authors to expand on that.

A minor point: the paper alternates between a differentiable model and a closed form model, which do not overlap. One can have a differential scattering-based model (e.g. Nimier-David, Merlin, et al. "Mitsuba 2: A retargetable forward and inverse renderer." ACM Transactions on Graphics (TOG) 38.6 (2019): 1-17.) that is nonetheless a non-closed form model.

### Questions
See weaknesses. 
Overall, I think this is a sound paper. Nevertheless, my concerns are 
a) lack of context and comparison with other state-of-the-art approaches that have shown good results in real-world hazy images.
b) I would like the authors to elaborate on the lack of model mismatch by assuming a simple gaussian kernel and then recovering under this assumption. I'm not sure how to evaluate the figure in the appendix. I do not know if other, more physically realistic methods for rendering scattering effects might do much better.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
