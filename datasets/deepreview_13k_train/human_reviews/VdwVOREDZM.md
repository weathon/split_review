# WildFusion: Learning 3D-Aware Latent Diffusion Models in View Space

- Decision: Accept
- Scores: 6, 8, 8, 6

## Abstract
Modern learning-based approaches to 3D-aware image synthesis achieve high photorealism and 3D-consistent viewpoint changes for the generated images. 
Existing approaches represent instances in a shared canonical space. 
However, for in-the-wild datasets a shared canonical system can be difficult to define or might not even exist.
In this work, we instead model instances in \textit{view space}, alleviating the need for posed images and learned camera distributions. 
We find that in this setting, existing GAN-based methods are prone to generating flat geometry and struggle with distribution coverage.
We hence propose \textit{\ourmodel}, a new approach to 3D-aware image synthesis based on latent diffusion models (LDMs). 
We first train an autoencoder that infers a compressed latent representation, which additionally captures the images' underlying 3D structure and enables not only reconstruction but also novel view synthesis. 
To learn a faithful 3D representation, we leverage cues from monocular depth prediction. 
Then, we train a diffusion model in the 3D-aware latent space, thereby enabling synthesis of high-quality 3D-consistent image samples, outperforming recent state-of-the-art GAN-based methods.
Importantly, our 3D-aware LDM is trained without any direct supervision from multiview images or 3D geometry and does not require posed images or learned pose or camera distributions. It directly learns a 3D representation without relying on canonical camera coordinates. This opens up promising research avenues for scalable 3D-aware image synthesis and 3D content creation from in-the-wild image data. See
\url{https://katjaschwarz.io/wildfusion/} for videos of our 3D results.\looseness=-1

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposed a two-stage model for learning 3D-aware latent diffusion model in image view space. In the first stage, the authors learn a trasformation: (image, depth) -> latent -> triplane -> NVS images, by applying a GAN loss. Then in the second stage, the authors train a latent diffusion model, which can be directly decoded into a triplane plane NeRF. The learning of the pipeline does not require multi-view data and has shown better results than previous approaches.

### Strengths
- The paper is nicely presented. Charts and tables are nicely made and I found the paper easy to read through.

- The two-stage training is interesting. Each step of the pipeline looks reasonable to me.

- The training of the method does not require 3D or multi-view image data.

### Weaknesses
 - An important work is missing in discussion/comparison. "VQ3D: Learning a 3D-Aware Generative Model on ImageNet", ICCV 2023. The two works are very similar and both works adopt a two-stage learning scheme. The major difference is that VQ3D applies a GAN-based method for both stages.   

- I am not sensitive to the quantitative number in the main paper but I saw many NVS results in the supplementary video are distorted. Also, I did not observe a significant visual improvement over the EG3D. I would resort to opinions from other reviewers.

- As the second stage is trained on a latent space obtained by the first stage training, I am concerned that the diffusion generation quality (geometry correctness and image fidelity) is bounded by the GAN-based training. So what is the benefit of introducing the second stage? Easy sampling?

- Strictly speaking, the training involves a large amount of 3D data, which comes from the pre-trained single view depth estimator. The reliance on a pre-trained depth estimator, while convenient, introduces a dependency on the quality and potential biases of that model, which could propagate into the final results.

### Questions
see above.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper presents a novel method address the challenge of 3D-aware image synthesis for in-the-wild images. A key difference to previous works is that it developed upon a latent diffusion model, which demonstrates more sample diversity to GAN. To enable in-the-wild generation, unlike existing methods that rely on a shared canonical space, the authors propose to model instances in view space. To enable consistent 3D representation, the diffusion model predicts an implicit 3D representation, the triplane representation. The training also leverages monocular depth estimation to further boost 3D accuracy. The experiments show that the proposed work outperforms prior art by a large margin.

### Strengths
- The authors leverages latent diffusion model to address the lack of sample diversity in 3D-aware GAN.
- They propose to represent 3D-aware image by an efficient triplane representation.
- The training loss avoids the necessity of multi-view images of the same instance, which makes it easier to train on a much larger amount of data. 
- An extensive ablation study to support design choices.

### Weaknesses
 - 1. This paper only compare with GAN-based methods. It would be more convincing if a comparison to recent diffusion-based methods (GenVS, IVID, VQ3D) is presented.

### Questions
See weakness section

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes a novel approach to learning a 3D generative model from unposed images in view space.

The core idea of the paper is to first pre-train an auto-encoder that takes an image and its estimated depth map as input, and encodes it into a triplane NeRF. That triplane is then used to re-render the input image and depth as well an one (or several) additional views. The input image and depth are supervised straightforwardly, while the additional view and depth is supervised via an adversarial loss.

Subsequently, the authors propose to train a latent diffusion model on the recovered latent space, enabling unconditional and conditional generative modeling.

### Strengths
- Exposure is excellent, the method is exceedingly clear. The overview figure is great.
- The paper is well-motivated and the shortcomings of prior work are clearly highlighted.
- Design choices are clear.
- Baselines are appropriate.
- Ablations are detailed and insightful.

### Weaknesses
My core complaint with this paper is that I am not quite sure why you would use this method over a simple depth-warping plus inpainting baseline.

The generated images are of somewhat low quality - they are certainly far behind anything that can be generated with any SOTA 2D generative model.

For any generated image, I could always use the same monocular depth predictor used in this paper to estimate depth, and then warp the image to a novel view. The only challenge would then be holes - which, however, one could easily inpaint, as has been demonstrated in "SceneScape"  (https://arxiv.org/abs/2302.01133).

I would really like to see the following simple baseline:
1. Generate an image with a 2D image generative model.
2. Predict monocular depth with the same model you are currently using.
3. Warp the image to a novel view using the predicted depth.
4. Use an inpainting method such as the one used in "SceneScape".

The only shortcoming here is that this requires warping and in-painting at test time, to render novel views. However, one could easily merge several such in-painted views into a single mesh, which could then be rendered from novel views, similar to what SceneScape does. 

Even so, I *do* believe that this paper adds significantly to the literature by clearly formulating the problem, showing how prior methods fail, and producing a method that significantly outperforms prior methods. I think this will spur follow-up work.

### Questions
I am overall OK with accepting this paper, as I believe that it is well-written, poses an important problem, and puts forth a reasonable baseline approach.

I would be happy to increase my score if the authors could provide the baseline requested above.


___


I thank the authors for addressing my concerns. I think this additional baseline comparison adds to the paper! I increased my score to 8 and will happily argue for acceptance.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a method that learns 3D generation from in-the-wild images, e.g., Imagenet. Specifically, this paper proposes to first learn a 3D-aware VAE that compresses images to latent space and decodes latent into 3D representations, i.e., triplane. To facilitate 3D learning from 2D images, especially unposed in-the-wild images, authors proposes to use RGB and depth discriminator for rendered novel views. After learning the 3D-aware latent features, authors uses a standard diffusion model to sample from the latent space. Experiments are performed on Imagenet, as well as three unimodal datasets. Some advantages over GAN-based methods are shown. Ablation study is also performed to show the effectiveness of different model parts.

### Strengths
1. A new paradigm is used on the 3D-aware generation on in-the-wild images. The 3D learning happens in the first stage VAE training, where novel view RGB and depth discriminator is used. The second stage latent diffusion model samples from the trained latent space.
2. Advantages of the new paradigm over the GAN-based methods, e.g., 3DGP and EG3D, are shown by quantitative evaluations.

### Weaknesses
1. For the first stage of 3D-aware VAE, there are previous methods that propose very similar method. For example, VQ3D and GINA-3D also encodes input images to 3D latents and decode them to the 3D representation of triplane. I would expect authors to give a more detailed explanation of how the proposed method differs from these methods. Specifically, the differences in the latent space representation, the training objectives, and the architectural choices need to be clearly articulated. The current discussion lacks sufficient detail to distinguish the proposed approach from these existing methods.
2. To continue on the above comment, I would also like to see the performance comparison with VQ3D on both VAE and generator, since the final generation performance largely depends on the performance of the first stage VAE. Therefore, it is important to understand if the performance improvement is from the first or the second stage. Without a direct comparison, it's difficult to assess the true contribution of the proposed method's VAE component. The comparison should include metrics relevant to both the VAE's reconstruction quality and the generator's sample quality when using the VAE's latent space.
3. I would recommend using 50k, instead of 20k, samples to calculate FID, since it is the standard adopted by most of previous methods, e.g., StyleGAN, VQ3D. It would also allow easier comparison with previous or future work. Using a non-standard number of samples makes it harder to contextualize the reported FID score and limits the comparability with other methods in the field.
4. The visual results shown in Fig. 9 is not very convincing. Flat structure can also be observed from the first two rows. The lack of clear 3D structure in the generated samples raises concerns about the effectiveness of the 3D-aware learning process. More diverse and high-quality visual results are needed to demonstrate the method's ability to generate realistic 3D structures.
5. Visual comparison with other methods is not enough. Firstly, I would like to see this comparison in the main paper instead of supplementary material, since it is a very important part for evaluation and can serve as reference when readers try to understand the advantage of the proposed method. Secondly, I would like to see more visual results for mode collapse of GAN-based methods, as mentioned in the third paragraph of section 4.2. The current visual comparisons are insufficient to fully support the claims made about the proposed method's advantages over GAN-based approaches. More comprehensive visual evidence is needed to demonstrate the mode collapse issue and the improved diversity of the proposed method.

### Questions
IVID has shown the ability to generate 360 degree novel view synthesis. I understand that IVID uses a very different approach from this paper. But I would like to hear authors' opinion on learning 360 degree 3D generation with the current pipeline. From my point of view, there is no technical limitation, since you can freely change the novel view camera distribution sampling when training the VAE.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
