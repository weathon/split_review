# Wasserstein Distortion: Unifying fidelity and realism

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
We introduce a distortion measure for images, Wasserstein distortion, that simultaneously generalizes pixel-level fidelity on the one hand and realism or perceptual quality on the other. We show how Wasserstein distortion reduces to a pure fidelity constraint or a pure realism constraint under different parameter choices and discuss its metric properties. Pairs of images that are close under Wasserstein distortion illustrate its utility. In particular, we generate random textures that have high fidelity to a reference texture in one location of the image and smoothly transition to an independent realization of the texture as one moves away from this point. Wasserstein distortion attempts to generalize and unify prior work on texture generation, image realism and distortion, and models of the early human visual system, in the form of an optimizable metric in the mathematical sense.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose a measure of image distortion based on an optimal transport approach, under the dual constraints of fidelity and realism. Fidelity is expressed by a distance metric such as PSNR, and realism by comparison to a collection of patches. The authors also propose to use a model of the Human Visual System (HVS) with a foveal-like receptive field to strike a varying balance between fidelity and realism depending on a distance to a given point or to a saliency map. They use their distortion measure for texture and realistic image synthesis.

### Strengths
The paper is well written and clear. The objective of proposing a distortion measure associated with characteristics of the HVS is interesting and novel. The formulation of their distortion measure based on Wasserstein distances is sound and also practical. The authors achieve good and efficient texture synthesis results but not as impressive synthesis of realistic images as recent methods based on diffusion. Nonetheless their approach is much more interpretable. They do use features extracted from a VGG-19 network for visual realism measurement, but this network has been well studied and could be understood as interpretable as well.

The authors have provided proofs and code in appendix, and so their results should be reproducible.

### Weaknesses
The paper is mostly a proof-of-concept at this stage. The author mention using their method for image encoding but this is not part of this work, and it is not clear that it would work well since, like recent super-resolution approaches based on single image patches approach, it could tend to fill in details with elements that would look realistic but are not real. The reliance on local statistics, while interpretable, may limit the ability to capture global image structure, potentially leading to inconsistencies in larger scenes. The foveal approach, while attempting to mimic the Human Visual System (HVS), appears to degrade image quality rapidly outside the high saliency regions. This raises concerns about the practical applicability of the method in scenarios where consistent quality across the entire image is desired. The use of VGG-19 features, while common, introduces a potential bias towards the representations learned by this specific network, and may not generalize well to other types of visual content or tasks.

### Questions
- The foveal approach is interesting but tends to produce quickly degrading results far from the high saliency results in figure 4 and similar. The HVS is not reducible to a degradation of resolution far from the fovea, it accepts less than perfect results but consistency is also important. Could the approach be improved by iterating over the generated image to identify highly unrealistic portions (such as broken lines, etc) and refine those? How could this made to work?

- Could the distortion measure be used to identified generated or edited content in an image, say to identify tampered images?
- How fast doe the proposed algorithm work, say to produce a 512x512 image?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose optimal transport as a way to unify pixel fidelity and realism understood as perceptual quality. The unifying nature of the work is the introduction of the construction of a loss function depending on a pooling parameter which in its limits toward 0 and $+\infty$ recover a loss that corresponds respectively to fidelity and realism. These results are backed up by theorems. Finally the authors conduct different numerical experiments : texture synthesis, foveated texture synthesis and reproduction of natural image with saliency maps.

### Strengths
- the paper is well grounded in its field, the introduction covers broadly the existing literature
- the structure of the paper is clear and easy to follow
- theoretical claims are illustrated by numerical experiments

### Weaknesses
 - the paper is well grounded in its field, the introduction covers broadly the existing literature
- the structure of the paper is clear and easy to follow
- theoretical claims are illustrated by numerical experiments

 - the Wasserstein distortion as introduced in section 2 is not really new and is in fact very close to the work of Freeman et al (2012) the main innovation being that the parameter sigma can freely be fixed at any position in the image instead of being constrained by the eccentricity of the visual receptive fields.
- the maths of section 2 are overly complicated for a naive reader : in the end the authors use discrete optimal transport between empirical distributions and assume Gaussiannity which in summary corresponds to adjust the mean and standard dev of the local features to a new image (initialized from a white noise image) to the mean and standard dev of the local features of an exemplar image. 
- the pooling distribution $q_\sigma$ corresponds to a local weighting of the statistics with width $\sigma$ (as in Freeman 2012).
- when section 2 is well understood the theoretical results become trivial : (i) in the large $\sigma$ limit this is standard texture synthesis framework (Portilla-Simoncelli, Gatys). The specific setting of equation (12) has been empirically evaluated for texture synthesis against Gatys and Portilla-Simoncelli by Vacher et al (Neurips 2020). (ii) in the small $\sigma$ limit this is the exact reconstruction of an image from its feature
- the numerical experiments illustrate the nature of sigma but I do not see in which it contributes to vision study (even in terms of methods)



### Questions
No specific questions.

details : 
-equation (2) is not a convolution, it becomes convo in eq (3)
-the title is a bit misleading by talking about fidelity and realism, it is a bit disappointing that this corresponds to notion of pixel distance vs perceptual distance...

**Post-response update**
Soundness have been increased from 2 to 3.
I would have increased my score to 4 but I can't and I think there is to much to be done to really be just under the acceptation threshold.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a distortion measure between a reference image and a reconstructed image. The motivation of the proposed Wasserstein distortion distance measure is to simultaneously address pixel-level fidelity as well as realism based on the theory of human vision system. 

From the reference image, a sequence of probability measures is defined. Each measure in the sequence represents the statistics of the features pooled across a region centered at a location. The given reference image is covered with overlapping pooling regions of various sizes. Each region is associated a distribution obtained by computing various features at random locations within the region. The overall distortion between two images is defined to be the Wasserstein distance between the distributions summed over the pooling regions. The proposed distortion measure reduces to pure fidelity and pure realism as the size of the pooling region tends to zero and infinity, respectively. This enables generation of textures that have high fidelity to a reference texture in one location of the image and a smooth transition to an independent realization of the texture as one moves away from this point.

### Strengths
The idea of using nonuniform weights over pixels in distributions enables incorporating fidelity and realism into a common framework

The proposed scheme enables smooth interpolation between fidelity and realism.

The proposed methodology is grounded in theories of the HVS.

### Weaknesses
The main contribution of this work over prior works is that the proposed formulation considers distributions using nonuniform weights over pixels while existing works use equal weights. It is not clear to me if the contribution is significant enough. Can one apply simpler modifications to existing approaches to achieve fidelity in specific regions and realism in the other regions? For instance, one could adapt the approach of [Ref1] which can control the spatial distribution of textures according to user-specified annotation maps. I do agree that the proposed Wasserstein distortion enables smooth interpolation between fidelity and realism however, it needs to be demonstrated that the proposed approach is superior to other possible methods.

Comparison in terms of computational requirements of the proposed scheme and existing approaches could have been discussed.

While I am not an expert in this topic, I would like to know if the authors could have compared with other methods on standard test sets.

### Questions
While I am not an expert in this topic, I would like to know if the authors could have compared with other methods on standard test sets.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper introduces a notion of Wasserstein distortion that unifies fidelity and realism, by varying its input parameters.

### Strengths
The approach is well-motivated and the Wasserstein distortion appears to be a proper treatment.

### Weaknesses
I feel that the techniques in this manuscript are more in an engineering way. That is to say, in the theoretical aspect, the paper is not that strong. It presumes a lot of domain knowledge in image processing, at least in its current exposition. It might be more suitable for CVPR. The core issue is that the paper lacks a deep theoretical analysis of the proposed Wasserstein distortion. While the motivation is clear, the paper does not delve into the mathematical properties of the distortion measure itself, such as its behavior under various transformations or its relationship to other established metrics. The paper also lacks a rigorous justification for the specific choices of pooling PMF and how these choices affect the overall distortion measure. Without a deeper theoretical understanding, it is difficult to assess the true potential and limitations of the proposed approach.

### Questions
See my comments above. I feel that the approach needs more stronger theoretical justifications.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
