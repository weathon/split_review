# Motion Guidance: Diffusion-Based Image Editing with Differentiable Motion Estimators

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
Diffusion models are capable of generating impressive images conditioned on text descriptions, and extensions of these models allow users to edit images at a relatively coarse scale. However, the ability to precisely edit the layout, position, pose, and shape of objects in images with diffusion models is still difficult. To this end, we propose {\it motion guidance}, a zero-shot technique that allows a user to specify dense, complex motion fields that indicate where each pixel in an image should move. Motion guidance works by steering the diffusion sampling process with the gradients through an off-the-shelf optical flow network. Specifically, we design a guidance loss that encourages the sample to have the desired motion, as estimated by a flow network, while also being visually similar to the source image. By simultaneously sampling from a diffusion model and guiding the sample to have low guidance loss, we can obtain a motion-edited image. We demonstrate that our technique works on complex motions and produces high quality edits of real and generated images. %

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a way to edit images using by applying a desired motion field. This is done by guiding a pretrained diffusion model at inference time according to a user-specified advection field. The approach is similar to classifier guidance---a differentiable guidance loss utilizes an off-the-shelf flow prediction deep network, encouraging the flow from the source image to the generated image to resemble the target flow at each diffusion step. The authors compare to several GAN-- and diffusion--based approaches.

### Strengths
Being able to inject user control into the output of a diffusion model is an important goal. Using a dense advection field as guidance is an intuitive way to manipulate images and could be potentially be useful for enforcing other spatial constraints on diffusion model outputs like temporal consistency and so on. The paper is clearly written, and a comprehensive ablation study validates many of the design choices.

### Weaknesses
My main concern has to do with lack of comparisons with recent works. While the authors discuss some of these in related works, they do not share any qualitative or quantitative comparisons. In particular, [Shi et al. 2023] and [Mou et al. 2023] seem to enable very similar functionality. While I recognize the authors' explanation that their approach is more efficient in that it requires no additional training or fine-tuning and is only done at inference time, I think it would be necessary see how these other methods perform on the same examples.

I would also be interested in seeing how this approach handles more complicated, higher-frequency flow fields. It seems like one big advantage of being able to control a diffusion model via a dense flow field is to enforce fine-grained motion. However, all the examples feature quite coarse and global transformations.

Finally, I am a little concerned about possible hallucination or identity loss resulting in these transformations. This is particularly evident in the motion transfer examples of Figure 7---as a result of the of the motion edit, the subject in the image also changes considerably. Is there a way to mitigate this effect?

### Questions
What is the intuition for why the edit mask is necessary to make this approach work? Shouldn't the fact that the flow field is identity on the unchanged regions be sufficient?

I would be curious to see what the one step approximation derived by equation (5) looks like as well as the results of passing it through the flow estimation model rather than the final denoised image. Is it a sufficiently good approximation and not out of distribution?

Does using a pretrained neural flow prediction model offer a significant  advantage over differentiating through an actual optical flow algorithm? For instance, works like "Supervision-by-Registration" [Dong et al. 2018] have done this for other tasks---I'm wondering how well a similar approach would work here.

---------

Post-rebuttal:

Thank you to the authors for their clarifications. I did not realize that [Shi et al. 2023] and [Mou et al. 2023] are concurrent work. Given this fact and the other addressed points, I have updated my score and recommend acceptance.

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
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a new motion guidance technique for diffusion models. The specified motion field can be arbitrary, but the reconstructed images are always plausible thanks to the diffusion model and the color loss. The range of supported motions is diverse, starting from simple translation and up to complex non-rigid motions. The method is extensively evaluated on several datasets, both qualitatively and quantitatively.

### Strengths
- An extensive related work section with good literature overview.
- The method supports many different types of transformations: translation, rotation, scaling, stretching, and other complex deformations.
- The method does not require any additional training and runs directly on the required inputs. It is also designed in such a way that it is independent on the used architecture.
- The results look visually pleasing.
- Many qualitative ablation studies support main contributions.
- The paper is well-written and easy to understand.

### Weaknesses
 - Unfortunately, all experiments and ablations are done mostly qualitatively. This brings a question whether the results are cherry-picked. I'd like to see more quantitative evaluations. Maybe the authors could evaluate the consistency of predictions over longer videos.
- In all experiments, the authors used optical flow (probably from a video). However, how can this method be used if the end user has only one image and wants to edit it? There is one experiment (Fig. 7), which shows that it can be estimated from a different video (and I appreciate it). However, I'd like to see if a hand-drawn optical flow could be used.
- eq. (3): later in Sec. 3.3 it is written that the color loss is masked out in "the occluded regions". However, this is not represented in eq. (3). Please update the equation to be precise.

### Questions
Please see the Weaknesses section.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new method for editing images with diffusion models and optical flow guidance. The proposed method does not require any network training or finetuning, and does not modified the diffusion network architecture. Instead, it applies an additional loss to guide the diffusion sampling process, making the edited image follow motion guidance without changing image contents. Experiments show that the proposed method can handle various type of motion guidance and generate high-quality results.

### Strengths
* The core of the proposed image editing method is a loss function that incorporates a pretrained optical flow network for motion supervision, and does not need any network training or finetuning. Therefore, it requires no data collection or network modification. 

* The proposed method is simple yet flexible and supports a wide range of motion guidance. When manipulating the image contents, the proposed method is able to hallucinate missing pixels like disoccluded areas or backgrounds.  The qualitative results are impressive. 

* The authors conduct extensive experiments to demonstrate the effectiveness and flexibility of the proposed method. The experiments are solid and convincing. 

* The paper is overall well-written and easy to follow.

### Weaknesses
 * The proposed method requires dense optical flows as the supervision signal. This is not a user-friendly input, as it is not clear how to obtain such flows without programming. DragGAN [Pan et al. 2023] is more user-friendly; users just need to simply drag a small number of pixels to manipulate images. In addition,  DragGAN provide feedback to users almost immediately, while the proposed method is slow to execute. 

* In Figure 5, the authors conduct a comparison experiment with DragGAN on out-of-domain images. However, StyleGANs are trained on narrow domains and DragGAN works better if the input image falls in the training image domain.  Although GAN inversion still works for out-of-domain images, I think it would be better if the authors can compare with DragGAN using in-domain images (e.g., human facial images) to make the experiment stronger and more convincing.

### Questions
* I think the proposed method can be easily extended for video generation by providing a sequence of flow guidance. It would make the paper stronger if the authors could provide such an example.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a run-time image editing method based on diffusion models using an optical flow as input. The method can synthesize a realistic looking image given the reference image and optical flow fields. The synthesis is done via a new motion guidance, which is composed of a flow reconstruction loss between a provided flow map to 2D optical flow estimate from reference image to the generated image, and a color loss to ensures the generated image is consistent to input image when warping back. The authors provide extensive visual examples and ablations to show the efficacy of this approach

### Strengths
* The paper is technically sound and simple. The approach should be easy to implement at runtime, and can be pretty general for most image synthesis backbones. 
* The authors provided very clear ablations study for many implementation details in the paper, including how to do denoising steps, editing mask, handling occlusions, which are crucial for the success. I like the provided examples which very clearly highlight the issues of each item if not being used. 
* The method performs favorable compared to alternative baselines. The method provides great visual consistency with respect to the input image and flow map.

### Weaknesses
 * As the author indicated in Sec 4.6, it is hard to create pixel-wise flow map by hand, which I personally will be the biggest limitation for this method to be applied in real-world use-case. I am not exactly how the authors demonstrate all the examples in results section, but from the results, they definitely look a real pixel aligned motion field regarding the input image, which is almost impossible to get in applications. From the motion transfer results, the authors discuss using "fewer recursive denoising steps" to get slightly better results. I wonder that's related to the gap in pixel aligned optical flow. I think it worth providing a careful analysis here to help readers understand the potential gap and insights to address these issues which is how this method used in real-world use-cases. I wonder whether there are also tasks (e.g. video stylization) that can better map the input of this method. 
* A suggestion, not a weakness. The demonstration of flow map can be more clear if provided with the color mapping chat with the flow (motion to color).

* For the recusive denoising, is the K constant number for all the experiments? I did not find what the parameter is used in the implementation details section.
* In flow loss discussion on page 6, the authors mentions "Without the flow loss our method is able to move objects to the correct location but often hallucinates things in disoccluded areas". Though it is true from the fig.3, the disocclusion regions looks quite wrong with flow loss, I did not quite understand why it is the case. The disocclusion region should not really impact the optical flow since they don't really have correspondence. One possible explanation is that they could potentially create ambiguity between the input image and synthesize image for the estimated flow, and adding flow floss could drive it to remove that potential ambiguity. I wonder whether that's the potential case? 
* Both Eq. (2) & (3) seems require the gradient w.r.t. the whole flow estimator if I understand correctly. That could be really slow? I wonder the compute time for each. For eq (3), will it make any difference if using f instead of F(x^{\star}, x) ?

### Questions
* For the recusive denoising, is the K constant number for all the experiments? I did not find what the parameter is used in the implementation details section.
* In flow loss discussion on page 6, the authors mentions "Without the flow loss our method is able to move objects to the correct location but often hallucinates things in disoccluded areas". Though it is true from the fig.3, the disocclusion regions looks quite wrong with flow loss, I did not quite understand why it is the case. The disocclusion region should not really impact the optical flow since they don't really have correspondence. One possible explanation is that they could potentially create ambiguity between the input image and synthesize image for the estimated flow, and adding flow floss could drive it to remove that potential ambiguity. I wonder whether that's the potential case? 
* Both Eq. (2) & (3) seems require the gradient w.r.t. the whole flow estimator if I understand correctly. That could be really slow? I wonder the compute time for each. For eq (3), will it make any difference if using f instead of F(x^{\star}, x) ?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
