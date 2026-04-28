# Ctrl-Adapter: An Efficient and Versatile Framework for Adapting Diverse Controls to Any Diffusion Model

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
\cnet{}s are widely used for adding spatial control to text-to-image diffusion models with different conditions, such as depth maps, scribbles/sketches, and human poses. However, when it comes to controllable video generation, \cnet{}s cannot be directly integrated into new backbones due to feature space mismatches, and training \cnet{}s for new backbones can be a significant burden for many users. Furthermore, applying \cnet{}s independently to different frames cannot effectively maintain object temporal consistency.
To address these challenges,
we introduce \textbf{\adaptermethod{}},
\textit{an efficient and versatile framework that adds diverse controls to any image/video diffusion model through the adaptation of pretrained \cnet{}s.}
\adaptermethod{} offers strong and diverse capabilities, including image and video control, sparse-frame video control, {fine-grained patch-level multi-condition control (via an MoE router)}, zero-shot adaptation to unseen conditions, {and supports a variety of downstream tasks beyond spatial control, including video editing, video style transfer, and text-guided motion control.}
With {six diverse U-Net/DiT-based} image/video diffusion models (SDXL, PixArt-$\alpha$, I2VGen-XL, SVD, {Latte, Hotshot-XL}), \adaptermethod{} matches the performance of pretrained \cnet{}s on COCO and achieves the state-of-the-art on DAVIS 2017 with significantly lower computation ($<$ 10 GPU hours).

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper proposes an efficient method for adapting pretrained ControlNets to various image and video diffusion frameworks. The authors also proposed a mixture of expert method for multi conditioning, and a mapping between discrete and continuous diffusion timesteps. Overall, the paper address an important problem (adapting pre-trained ControlNets efficiently), provide useful insights and achieves superior results.

### Strengths
- The results proposed in the paper are interesting and convincing. 
- Adapting pre-trained ControlNets to new diffusion frameworks including videos is interesting and the method is novel. 
- The paper is well written and the experiments to validate the proposed method are significant. 
- The code is provided.

### Weaknesses
 - Poor presentation: the main paper is packed with experiments but lacks many essential details about the method such as the adapter architecture, more details about the MoE method, etc. 
- Unjustified architecture choices: the authors proposed to use a 1-1 mapping between the ControlNet layer to ones with similar dimension in the new diffusion model. This assumes that these layers learn similar features but the authors did not touch on this topic or justified their choices. 
- What is the rational behind conditioning the CTRL-Adapter with the first frame? How does the proposed method perform without such conditioning?

### Questions
Additional comments (no need to address):
- typo in in L069 "Controlnet a cannot"

### Soundness
4

### Presentation
2

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a new framework called CTRL-Adapter, aimed at enhancing the control capabilities of image and video diffusion models. By adapting pretrained ControlNets, CTRL-Adapter allows for the efficient integration of various control conditions into new diffusion models, supporting image control, video control, and sparse frame control. The results demonstrate that CTRL-Adapter maintains high performance on various datasets with significantly reduced computational costs compared to training ControlNets from scratch.

### Strengths
+ The presentation and writing quality of this manuscript are are generally strong and well-structured.
+ The framework supports a wide range of applications, from image and video control to video editing and style transfer.
+ CTRL-Adapter requires fewer computational resources. This method significantly reduces the training time, outperforming baselines in less than 10 GPU hours
+ The authors provide comprehensive experiments that validate the performance of CTRL-Adapter.

### Weaknesses
 + While skipping latents can increase efficiency, it may inadvertently lead to loss of fine-grained detail in frames without direct conditioning. I'm wondering if there are any issues with this method that I'm concerned about?
+ Providing more detailed results from an ablation study about Weaknesses 1 could offer valuable insights into the impact of this strategy. It could reveal conditions where skipping latents is beneficial versus scenarios where it may compromise quality.
+ Whether skipping latents reduces the ability of the CTRL-Adapter to generalize between certain control types.
+ In my experience, the most significant advantage of this work is the value of a wide range of applications. In terms of technical contributions, it seems to extend multiple adapters in various generative models. Could the authors provide more elaboration on the technical contribution or insights?

### Questions
Please see weaknesses

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
CTRL-Adapter is an efficient and versatile framework designed to integrate diverse controls into image and video diffusion models by adapting pretrained ControlNets. This method achieves comparable performance to training ControlNet from scratch while significantly reducing training costs. It introduces fine-grained, patch-level MoE (Mixture of Experts) routing to compose ControlNet features more effectively, as opposed to prior methods that operate only at the image or frame level. CTRL-Adapter is compatible with both UNet-based and DiT-based backbones, continuous timestep samplers, and varying noise scales. Extensive experiments demonstrate that CTRL-Adapter performs well on image and video generation and can be applied to various tasks, including video editing, style transfer, and text-guided object motion control.

### Strengths
1. The proposed method stands out for its simplicity and efficiency. It presents a cost-effective approach to adapting image-based ControlNet models for video-based applications. It also offers valuable insights into merging multiple conditions using three strategic choices. It incorporates a fine-grained, patch-level Mixture of Experts (MoE) routing to enhance the generation process by enabling precise and adaptive control over features.

2. The evaluation is thorough and well-executed, providing extensive comparisons across both single-condition and multi-condition video generation. Additionally, it demonstrates the model's versatility by showcasing its performance on tasks such as video editing, style transfer, and text-guided object motion control, highlighting its wide applicability.

3. The paper is exceptionally well-written, with a logical and coherent structure that ensures ease of understanding.

### Weaknesses
1. The comparison of training costs might not be entirely fair. Since the CTRL-Adapter leverages a pre-trained image ControlNet and then adapts it for video tasks, it benefits from the substantial pre-training cost in the image control task. Given that the image ControlNet is already proficient at extracting information from various conditions, this adaptation should inherently be faster. Therefore, when evaluating training efficiency, it is crucial to account for the advantages gained from the pre-trained ControlNet. The paper does not adequately address the computational cost of pre-training the image ControlNet, which is a significant factor when considering overall efficiency. A more comprehensive analysis should include the resources required for the initial image ControlNet training to provide a complete picture of the method's efficiency.

2. The explanation of how multiple conditions are integrated in the proposed method could be clearer and more detailed. The paper briefly outlines three possible integration strategies in a single paragraph, accompanied by a figure, which might be insufficient for comprehending the intricacies involved. This section deserves more space and elaboration in the main text rather than being relegated to the appendix. The description of the Mixture of Experts (MoE) routing mechanism, particularly how the patch-level routing is implemented and how the experts are chosen and combined, lacks sufficient detail. A more thorough explanation of the MoE architecture and its operation within the CTRL-Adapter framework is needed to fully understand its contribution.

### Questions
1. What is the additional inference cost associated with using multiple condition ControlNets along with their corresponding control adapters, for example, when handling seven different conditions in Table 3? While the paper mentions significant reductions in training costs by focusing on adapting image-based ControlNets for video tasks, how does the increase in inference complexity, due to maintaining multiple controls, impact overall efficiency and performance? 

2. Would integrating control adapters directly inside each ControlNet simplify the adaptation process and make it more efficient, like a fine-tuning task from image to video ControlNet? Could this approach be a viable and efficient baseline, particularly for single-condition scenarios?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work Ctrl-Adapter extends X-Adapter to a more general setting: the pretrained ControlNet and downstream diffusion models can now differ in modality (images, videos) and architecture (e.g., UNet or Transformers). The authors show in extensive experiments that Ctrl-Adapter works well in many scenarios and outperforms X-Adapter.

### Strengths
- The major technical contribution is to extend X-Adapter by involving temporal convolutions for the support of adapting from image to video. 

- There are a bunch of engineering contributions to improve performance: (1) the utilization of Q-former; (2) skipping latents; (3) handling noise scheduling shift.

- A really extensive experiments to demonstrate the strength of their work in various scenarios: single condition, multi conditions, zero-shot, from image to image, from image to video.

### Weaknesses
1.  Overall, the writing could be improved to enhance clarity. The methodology section should be more focused and closely aligned with the key contributions. Currently, it is cluttered with engineering details and lacks mathematical formulation, which makes it harder to grasp the technical novelty.

2.  Does skipping latent require retraining ControlNet?

3.  The Multi-ControlNet setup is unclear:
	•	Are six conditions trained simultaneously in each iteration?
	•	In Section 4.5, Figure 8 (zero-shot results), the zero-shot inferences under different conditions do not appear to align accurately with the intended conditions, which is understandable since they were not trained on these. However, could you provide an example without ControlNet for comparison? Could you also add quantitative results for the zero-shot experiment in Table 4? (Consider adding a row for models trained solely on depth but applied to other conditions, and a row with plain diffusion without ControlNet as a baseline for comparison.)

4.  What is architecture difference with X-Adapter? What is the training speed improvement over X-Adapter come from?

### Questions
See weakness part. Overall, I lean to accept the paper. I need more explanation compared to X-Adapter in the technical side: (1) the architecture difference; (2) the training difference; (3) explain what is the performance and training speed come from.

### Soundness
3

### Presentation
2

### Contribution
3
