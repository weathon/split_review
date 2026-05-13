# Clothing-disentangled 3D character generation from a single image

- Decision: Reject
- Scores: 5, 6, 6, 6

## Abstract
This paper tackles the challenge of generating clothing-disentangled 3D characters from a single image. Existing approaches typically employ multi-layer 3D representations to model the body and each garment and then iteratively optimize these representations to fit the observations, which is time-consuming and not scalable. To address this, we propose the first feed-forward method enabling efficient and robust clothing disentanglement. Our approach first generates the multi-view images for each component of the clothed character and then employs a generalizable multi-view reconstruction method to create the 3D models of each component. For high-quality disentanglement, we propose a two-stage disentanglement approach that first disentangles each component in the 2D image space and then generates the multi-view images for each part. During the 2D component disentanglement stage, we introduce a novel multi-part diffusion model that allows information exchange among different components. Additionally, for component combination, we incorporate a novel combination attention mechanism into the multi-view diffusion model, enabling the integration of information from multiple parts to create the final combined character. For training, we have contributed a large clothing-disentangled character dataset consisting of more than 10k anime characters. Extensive experiments demonstrate that our proposed approach not only facilitates efficient and high-quality disentangled 3D character generation with distinct clothing layers but also supports various cloth editing applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents a feed-forward method for generating clothing-disentangled 3D characters from a single image, reducing the process from hours to seconds. It introduces a two-stage disentanglement approach and a multi-part attention mechanism for high-quality component separation and combination. The authors also contribute a large dataset of over 10k anime characters for training and evaluation.

### Strengths
Efficient generation of 3D characters from a single image.

Two-stage disentanglement method for better component separation.

Multi-part attention mechanism for improved information exchange.

### Weaknesses
1.	Existing methods, such as ICON[A], HiLo[B], and D-IF[C], do not necessarily require an optimization process when reconstructing a clothed human. What is the superiority of the proposed feed-forward strategy over these methods, especially considering that these methods also achieve impressive reconstruction quality without explicit optimization for the clothed human as a whole?
2.	More baseline methods, such as ICON[A], HiLo[B], and D-IF[C], should be considered to fully demonstrate the effectiveness of the proposed method. While these methods may not explicitly disentangle clothing, a comparison of reconstruction quality (e.g., using PSNR and SSIM on rendered images) would provide a more comprehensive evaluation.
3.	In line 303, is obtaining the rotation matrix RcRc dependent on an optimization process? The description lacks sufficient detail on how this matrix is derived, and whether it involves iterative refinement or is a direct output of the feed-forward network.
4.	In Table I, the comparison methods are too few. Moreover, more metrics like clip score, FID (Fréchet Inception Distance), or user studies should be introduced to evaluate the proposed method. The current metrics are insufficient to fully capture the quality and perceptual fidelity of the generated 3D models and their disentangled components. A clip score would be particularly useful to assess the alignment between the generated images and the input image.
5.	Is it possible to try an input image with a higher resolution, at least one with a clear face? The current resolution might be limiting the level of detail that can be captured and reconstructed, especially for facial features.

### Questions
Please refer to the weakness part.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Given an input image of an anime character, this paper presents a method to reconstruct the character in 3D where the body and the clothing items are disentangled. This is achieved by first generating complete images of each clothing item (assuming a fixed set of clothing types) from the input image. Then multiview images of each clothing item are generated which are used for 3D reconstruction. Finally, the different 3D generations are fit together with an optimization.

### Strengths
- In the context of human/character reconstruction, going from a single image to a disentangled body/clothing 3D representation is important and this paper makes good observations without necessarily relying on parametric body models.

- Some aspects of the method design choices are ablated well.

### Weaknesses
 - Even after reading several times, I do not actually fully understand what the combination attention and combination condition image is doing. It's especially confusing since the appendix says: "The combination condition is a predefined constant matrix, which matches
the shape of the disentangled images and has all its values set to 128." If this matrix is fixed with all values equal to 128, what does it actually do?
- There is not a lot of evaluation on how well the method generalizes. It is not easy to tell how similar are the testing images to the training ones. Also maybe testing on some out of domain images would be useful.

### Questions
- I'm not sure how the baseline of Wonder3D is run actually. The authors mention they add a "part" condition. Do they still use their part decomposed images as input image or do they use the full character image as the input and generate multiview images of each part?
- Once each part is reconstructed as 3D gaussians, it seems the paper tries to optimize the transformation of each part and then just directly overlay the Gaussians. Do they do anything related to the opacity values of the Gaussians? If not, wouldn't the rendering of the composite would look different then the rendering of the individual parts?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The goal of this study was to perform 3D reconstruction by separating clothing and body components from single character image, utilizing a diffusion model to generate 2D cloth disentanglement and multi-view images. The LGM model was used for 3D reconstruction, and a dataset of 10k 3D character models was built.

### Strengths
This study extends existing image-to-3D techniques using diffusion models to achieve cloth disentanglement.
Additionally, by building a 10k 3D character dataset, which, if released, could greatly benefit for future research.

### Weaknesses
1. The methods used for clothing disentanglement and 3D reconstruction are not novel, primarily involving applications of existing methods. The diffusion model is the similar to Stable Diffusion [1], the attention method is the similar to Animate-Anyone [2], and the 3D reconstruction method is the similar to LGM[3].

2. Throughout the paper, there is a lack of references when discussing specific methods or abbreviations (e.g line 43,47,74,78,294,295 and more), which can make it difficult to follow.

3. The comparative analysis is limited to a baseline, lacking detailed explanations of differences, making it hard to understand why the qualitative and quantitative results differ.

4. It’s disappointing that there are no experiments using general character images with various poses and perspectives, which limits the practical applicability.

### Questions
1. Did you use a pretrained stable diffusion model for fine-tuning?

2. Why didn’t you use 3D evaluation metrics such as Chamfer Distance or Point-to-Surface?

3. Is there optimal number of views or view point for 3D reconstruction?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a method for generating clothing-disentangled 3D anime characters from a single image. In the first stage, the model takes a frontal image of a clothed anime character in a canonical pose and generates images of the top, bottom, shoes, and minimally dressed body using a stable diffusion model. In the second stage, the diffusion model is applied to generate four distinct views for each part, conditioned on the outputs from the first stage. Finally, the 3D structure is produced using the existing LGM method by taking the generated multi-view images as input, which generates a 3D Gaussian asset. The work has also proposed a synthetic dataset for training the model, consisting of 110k anime characters generated from VRoid.

### Strengths
1.The paper proposes using a diffusion model as a partitioning method to avoid occlusion and low resolution issues.

2.The model is feed-forward and does not require an optimization process, enabling the generation of 3D assets in a short amount of time.

3.The model allows for anime character cloth-switching and supports virtual try-on applications.

4.The dataset includes a rich variety of anime characters with diverse outfits.

### Weaknesses
1.The technical contribution appears limited, as the main novelty lies in fine-tuning the diffusion model. The reconstruction is performed using an existing method, so the paper primarily focuses on generating multi-view images for each part of the characters.

2.The generated assets are represented as 3D Gaussian splats, which may not be as practical as mesh-based models for downstream applications due to the lack of geometric detail.

3.In the dataset samples shown, while there is variation in the outfits, the body shapes appear to lack diversity. This raises a concern about the model's ability to handle virtual try-on between characters with significantly different body shapes (e.g., slim vs. thick body types).

### Questions
1. L253-254: The model seems to generate one part of the entire image at a time, correct? This generation is conditioned on the specific part type provided. Could you clarify if this understanding is accurate?

2. L287: Could you explain what is meant by "this special condition image"? A more detailed explanation of how it works would be helpful for understanding this part of the method.

3. L295: The citation for the LGM method appears to be missing.

### Soundness
3

### Presentation
2

### Contribution
2
