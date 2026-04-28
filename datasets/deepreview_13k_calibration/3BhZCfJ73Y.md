# Not All Prompts Are Made Equal: Prompt-based Pruning of Text-to-Image Diffusion Models

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 5, 6, 8

## Abstract
Text-to-image (T2I) diffusion models have demonstrated impressive image generation capabilities.~Still, their computational intensity prohibits resource-constrained organizations from deploying T2I models after fine-tuning them on their internal \textit{target} data.~While pruning techniques offer a potential solution to reduce the computational burden of T2I models, static pruning methods use the same pruned model for all input prompts, overlooking the varying capacity requirements of different prompts. Dynamic pruning addresses this issue by utilizing a separate sub-network for each prompt, but it prevents batch parallelism on GPUs. To overcome these limitations, we introduce Adaptive Prompt-Tailored Pruning (APTP), a novel prompt-based pruning method designed for T2I diffusion models. Central to our approach is a \emph{prompt router} model, which learns to determine the required capacity for an input text prompt and routes it to an architecture code, given a total desired compute budget for prompts. Each architecture code represents a specialized model tailored to the prompts assigned to it, and the number of codes is a hyperparameter. We train the prompt router and architecture codes using contrastive learning, ensuring that similar prompts are mapped to nearby codes. Further, we employ optimal transport to prevent the codes from collapsing into a single one. We demonstrate APTP's effectiveness by pruning Stable Diffusion (SD) V2.1 using CC3M and COCO as \emph{target} datasets.~APTP outperforms the single-model pruning baselines in terms of FID, CLIP, and CMMD scores.~Our analysis of the clusters learned by APTP reveals they are semantically meaningful. We also show that APTP can automatically discover previously empirically found challenging prompts for SD, \emph{e.g.,} prompts for generating text images, assigning them to higher capacity codes.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The paper introduces adaptive prompt-based pruning strategy to reduce the computation cost of diffusion model. The proposed approach involves encoding input prompts into architecture embeddings, which are mapped to specialized architecture codes. These codes determine the routing of each prompt to a pruned sub-network. By training a prompt router using a combination of contrastive learning and optimal transport, the proposed method ensures that prompts are dynamically assigned to appropriate sub-networks. The results of the paper demonstrate the reduction in computational cost while maintaining FID and CLIP scores.

### Strengths
1. The paper introduces a novel approach by proposing adaptive prompt-based pruning that routes input prompts to specialized pruned sub-networks based on their characteristics. This represents a difference from conventional static and dynamic pruning methods,
2. The empirical results training on datasets like CC3M and MS-COCO demonstrate the method’s effectiveness compared to other pruning methods. The results show that the proposed method outperforms other baselines by significantly reducing computational cost while maintaining or improving output quality as measured by metrics like FID, CLIP score, and CMMD score.

### Weaknesses
The major concern is the empirical evaluation of the proposed method: 

1. as stated in the paper, most organizations typically fine-tune pre-trained diffusion models on their target data but evaluate these models on broader benchmarks to demonstrate generalizability. In this study, however, the authors only fine-tune their model on CC3M and MS-COCO and limit their evaluation to the corresponding validation sets. Expanding the evaluation to a common benchmark would better showcase the model’s generalization capabilities. Specifically, demonstrating that the prompt router can handle prompts outside the training distribution would be more convincing.

2. The paper also references other model pruning methods, such as MobileDiffusion[1], SnapFusion[2], and LD-Pruner[3]. However, it does not include quantitative comparisons with these approaches. It would be helpful for the authors to explain why these comparisons were omitted.

3. In efficient inference for stable diffusion, recent papers show that one-step or few-step generation can speed up the generation. This paper does not include comparisons with methods like INSTAFLOW[4], which would have provided valuable insights into how APTP compares with state-of-the-art approaches in rapid generation.

### Questions
1. The authors utilize a pre-trained sentence transformer as the prompt encoder in their training process. Do the authors have any insights into how the size of the prompt encoder influences the overall performance, as the size of the prompt encoder will affect the models' ability to understand the input prompt? 

2. Training diffusion models often incorporate classifier-free guidance. Is the proposed method compatible with training under this manner?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The authors propose prompt-based tuning of text-to-image diffusion models, in which different sub-networks within pre-trained models are trained for different prompts/concepts. They authors performe experiments on multiple datasets to show that for a given latency, their model performs comparably to higher latency pretrained models.

### Strengths
1. The idea behind the paper is technically sound and novel.
2. The paper is well written. 
3. The authors present some interesting interepretability experiments on expert assignment that aid the proposed concepts.

### Weaknesses
1. Limited experiments - Although I find the proposed ideas novel, I believe that the paper lacks extensive experimentation on 
 - different types of architecture - It is currently unknown if the proposed methods is generalizable across architectures (DiT, MMDiT etc). 
 - Small datasets - How does the method perform when data is limited?
 - Fine grained concepts - How does their method handle expert assignment when concepts are fine-grained (breeds of different animals)
2. Comparison to Mixture-of-Experts (MoE) models - How does the proposed method compare to other prompt-conditinal architectures like MoE text-to-image diffusion models? Currently the competitors in Table 1 (a and b) are static structural pruning baselines, but I believe the paper's contribution is prompt-conditional pruning, which demands comparison to prompt-conditional efficient architectures like MoEs like [1].
3. I am concerned about the 4 and 7 point drop in FID of the proposed method in Table 1. The authors have not presented any trade-off between latency and performance, which would help understand how limiting computational budget affects performance

### Questions
See Weaknesses

### Soundness
2

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
This paper presents a new approach for accelerating the sampling from diffusion models using adaptive pruning denoted as APTP. The method is tailored for a specific scenario where the inference is on a specific known data distribution and the data for it is given (e.g. a company’s private dataset). Using this data, APTP trains a prompt router module that selects which parts of the architecture should be pruned for each given prompt. The selection is from a fixed set of reduced architecture states (denoted as architecture codes). Both the prompt router and arch. codes are trained end-to-end.

### Strengths
- The idea of pruning different parts of the network for each prompt is non-trivial and interesting.
- Visual results show APTP seems to use various pruning modes, and does not collapse to a single one.

### Weaknesses
 **(1) Missing Baselines of Less Diffusion Steps:** My main concern is that the paper does not compare to approaches that perform less diffusion steps. More specifically the following should be considered as baselines:

- *Step Skipping Distillation of Diffusion Models [1,2,3]:* As mentioned in the paper, several methods tackled faster inference of diffusion models using this idea, mostly by knowledge distillation of the model to inference with fewer (between 1-4) steps. These methods should cut the latency by 8-25 times from the original model, while the proposed APTP was shown to cut latency by much less (not even 50% of the original model timing). These approaches also require training as APTP does, and their weights are readily available for many SoTA architectures, e.g. SDXL, SD 1.5, etc. The paper needs to demonstrate that APTP provides a benefit beyond what can be achieved by simply reducing the number of sampling steps via distillation, especially since the reported latency reduction is not substantial.

- *Caching Based Acceleration [4]:* These approaches cache features of the U-Net architecture and reuse them in later steps. Such approaches hold a distinct advantage of being training-free.

- *Less Denoising Steps at Inference Time:* A trivial training-free baseline is to simply sample images with less denoising steps. I wonder how that would compare to the proposed APTP. Can APTP further accelerate such a setting?

As step skipping approaches became more popular recently, I believe including some of these as baselines is a must for such an approach.

**(2) Quality of Writing (Sec. 3):** Sec. 3 is complicated and difficult to understand. Specifically, I think Sec. 3.2,3.3 are overloaded and could be shortened to a much clearer version. These subsections are the only place in the paper that describe the actual approach of APTP (and what does arch. codes mean), therefore are especially important for the proposed approach.

**(3) Visual Comparisons:** The paper offers a very limited selection of visual comparisons - having only 8 qualitative comparisons to the original baseline, and no such comparisons to previous approaches. Could the authors please supply a larger set of comparisons to the original model and baselines (including a step skipping distillation [1,2,3], caching [4] and less denoising steps).

**(4) Clustering of Pruning Modes:** While this qualitative analysis was promised in the abstract and introduction, it only exists in figures at the last 2 pages of the appendix without any textual description. Given it is mentioned in the abstract I think it should be included as a part of the main manuscript.

**(5) Limited Setting and Empirical Results:** Unlike other approaches, the proposed method is limited to a specific data distribution. Although the task is much more confined, the reduction in latency is not substantial: To keep performance comparable to the original model in terms of FID or CLIP score, APTP can only reduce 20% of the latency (Tab.1).

### Questions
- Did the authors try their approach on other architectures? even other backbones of Stable Diffusion?

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors propose a mixture-of-expert-esque strategy for efficiently, which they coin Adaptive Prompt Tailored Pruning (APTP). The methods combine the benefits of dynamic and static pruning methods and archives good generative metrics while decreasing the computational cost.

### Strengths
* Good Illustrations and concise explanation
* The core idea is an interesting combination of known concepts in a new, but highly relevant setup.
* A good amount of comparison to other methods using multiple datasets with different image-types (COCO being primarily real-world images and CC3M being more diverse)

### Weaknesses
 * While FID, CLIP-Score and CMMD alongside the visual examples provide a good overview, I, personally, would have preferred some human-user study (which I see is a lot of effort and for this reason, would not ask from the authors). As an alternative substitute, I propose compute the pick-scores [Kirstain et al. 2023] against the pruning metrics similar to [Pernias et al 2024] on a set of diverse prompts like Partiprompts could provide additional, easily interpretable evidence of this methods' superiority in terms of generation quality.

* I would be curious to know how big the router-model itself is (in terms of parameters and memory footprint) and, by extension, how does the size of the router model affect the maximum batch size on an A100 GPU?
* Did you do any additional experiments concerning varying resolutions and aspect ratios and their impact on the pruned-image quality?
* Did you try applying this technique to transformer-based image-generation models like Pix-Art-Alpha / Sigma, do you see any major hurdles regarding the switch from ConvNets to Transformers?
* How specific is the APTP-model to its training data? How do out-of-distribution prompts impact the quality of the generations?

### Questions
* I would be curious to know how big the router-model itself is (in terms of parameters and memory footprint) and, by extension, how does the size of the router model affect the maximum batch size on an A100 GPU?
* Did you do any additional experiments concerning varying resolutions and aspect ratios and their impact on the pruned-image quality?
* Did you try applying this technique to transformer-based image-generation models like Pix-Art-Alpha / Sigma, do you see any major hurdles regarding the switch from ConvNets to Transformers?
* How specific is the APTP-model to its training data? How do out-of-distribution prompts impact the quality of the generations?

### Soundness
3

### Presentation
3

### Contribution
3
