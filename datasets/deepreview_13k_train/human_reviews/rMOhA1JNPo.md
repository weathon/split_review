# Aligning Generative Denoising with Discriminative Objectives Unleashes Diffusion for Visual Perception

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
With success in image generation, generative diffusion models are increasingly adopted for discriminative scenarios because generating pixels is a unified and natural perception interface. Although directly re-purposing their generative denoising process has established promising progress in specialist (e.g., depth estimation) and generalist models, the inherent gaps between a generative process and discriminative objectives are rarely investigated. For instance, generative models can tolerate deviations at intermediate sampling steps as long as the final distribution is reasonable, while discriminative tasks with rigorous ground truth for evaluation are sensitive to such errors. Without mitigating such gaps, diffusion for perception still struggles on tasks represented by multi-modal understanding (e.g., referring image segmentation). Motivated by these challenges, we analyze and improve the alignment between the generative diffusion process and perception objectives centering around the key observation: \emph{how perception quality evolves with the denoising process}. (1) Notably, earlier denoising steps contribute more than later steps, necessitating a tailored learning objective for training: loss functions should reflect varied contributions of timesteps for each perception task. (2) Perception quality drops unexpectedly at later denoising steps, revealing the sensitiveness of perception to training-denoising distribution shift. We introduce diffusion-tailored data augmentation to simulate such drift in the training data. (3) We suggest a novel perspective to the long-standing question: why should a generative process be useful for discriminative tasks -- interactivity. The denoising process can be leveraged as a controllable user interface adapting to users' correctional prompts and conducting multi-round interaction in an agentic workflow. Collectively, our insights enhance multiple generative diffusion-based perception models without architectural changes: state-of-the-art diffusion-based depth estimator, previously underplayed referring image segmentation models, and perception generalists.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper "Aligning Generative Denoising with Discriminative Objectives Unleashes Diffusion for Visual Perception" introduces a novel framework, ADDP, designed to enhance the performance of generative diffusion models on discriminative visual perception tasks. These tasks, such as depth estimation, referring image segmentation, and generalist perception, demand precise alignment with ground truth data, which has been a challenge for generative models.

This technique prioritizes earlier denoising steps, which have a more significant impact on final perception quality. By adjusting the learning objectives, ADDP ensures that the model focuses on the most critical stages of the denoising process. To mitigate the "training-denoising distribution shift" issue, ADDP employs task-specific data augmentation strategies, simulating the deviations that occur during the denoising process to improve the model's robustness and maintaining perception quality across different timesteps.
ADDP leverages the iterative nature of diffusion models to enable user interaction. By incorporating classifier-free guidance, users can provide corrective feedback to refine the model's output, offering a more flexible and interactive approach compared to traditional discriminative models.

ADDP has demonstrated significant improvements in depth estimation, referring image segmentation, and generalist perception tasks. By effectively aligning generative and discriminative objectives, ADDP bridges the gap between generative diffusion models and discriminative baselines, without requiring architectural changes or additional data. This work represents a significant step forward in the field of generative diffusion models, highlighting their potential as powerful tools for visual perception tasks.

### Strengths
The paper introduces a novel framework, ADDP, addressing a previously unexplored gap in applying generative diffusion models to perception tasks. The paper's key contributions include a Contribution-Aware Timestep Sampling to prioritize early denoising steps for improved perception accuracy, as well as a Diffusion-Tailored Data Augmentation technique that simulates distribution shifts during the denoising process. The authors provide a Interactive User Interface to enable human-in-the-loop correction through the denoising process.

The paper demonstrates high quality through evaluation on various tasks, including depth estimation, referring image segmentation, and generalist perception and provides significant improvements over standard diffusion-based models without architectural changes.The authors provide ablation studies to justify the design choices and the individual contributions of each technique.
The paper is well-written and easy to understand, with clear structure, clear explanations of technical concepts, aided by diagrams and clear communication of key ideas.

The paper has significant implications in expanded model versatility, using for both generative and perception tasks and in possibilities for human-in-the-loop correction and user-guided generation. Overall, the paper presents a highly original, well-supported, and clearly articulated framework, expanding the utility of diffusion models into discriminative and perception tasks.

### Weaknesses
Not enough explanation about how the  contribution factors are derived and adapted to each perception task. It would be helpful if the authors could discuss the potential challenges or limitations of this augmentation strategy, particularly for tasks where shifts may not be well-simulated by data corruption.

The interactive correctional guidance using classifier-free guidance is a compelling feature, but  the authors could elaborate on how correctional prompts are formulated and whether they require manual input.The paper demonstrates improved results with diffusion-tailored data augmentation, but it is unclear whether specific types of augmentation (e.g., color, shape changes) have a greater impact than others without clarify which augmentations are most effective.

While ADDP is demonstrated with specific models, it’s unclear how generalizable these methods are across different diffusion model architectures, such as conditional or latent diffusion models with varying noise schedules. Although ADDP is tailored for perception, it would be interesting to know if the authors have considered its potential for other tasks, such as text-to-image generation or other generative tasks with precision requirements.

### Questions
1. Could the authors provide additional insights into how the contribution factors $𝑐_𝑡^2$   for each timestep are estimated and why they differ for various perception tasks? Specifically, how does the estimation process differ between depth estimation and referring image segmentation (RIS)?
2. Can the authors clarify how well the proposed augmentation strategy generalizes to other types of distribution shifts in diffusion-based perception tasks?
3.  How effective is the system without human-generated prompts?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper investigates the performance gap between diffusion models and traditional encoder-decoder methods in perceptual tasks (e.g., Referring Segmentation) through validation experiments. It analyzes the varying contribution importance of different timesteps in perception through timestep-contribution analysis, leading to improvements in both training strategy and data aspects. Additionally, the paper demonstrates the potential of diffusion models for interactive referring perception tasks using prompt-based guidance agents.

### Strengths
1. The methodology and motivation are presented with exceptional clarity, with comprehensive consideration of variants for each method, including:
   - Various augmentation approaches
   - Different definitions of $c_{t}^2$ in timestep-aware training

2. The experimental section is thoroughly comprehensive, including:
   - Validation experiments in the introduction
   - Performance evaluations across multiple tasks (RIS, Depth Estimate, Generalist Perception)
   - Detailed ablation studies

3. The innovations stem from meaningful problem discovery and are non-trivial, with adaptive training and data augmentation for different timesteps representing logical explorations of the original problem.

### Weaknesses
1. The paper appears overly content-rich for a conference paper, resulting in some crucial discussions being relegated to supplementary materials:
   - The revised objective for the augmented ground truth in Sec. B.3.2
   - Intensity of augmentations across timesteps in Sec. B.3.1
   These aspects are fundamental to understanding the methodology but lack explanation in the main text. The absence of these details in the main text makes it difficult to fully grasp the nuances of the proposed approach. For example, the specific mathematical formulation of the revised objective and the exact schedule for varying augmentation intensity across timesteps are critical for reproducibility and a thorough understanding of the method's effectiveness. Without these, the reader is left with an incomplete picture of the methodology.

2. The "User interface" section seems disconnected from the main methodological contributions and shows limited performance improvements (as shown in Table 3). The whole content of this paper might be better suited as two separate conference papers. The improvements in Table 3, particularly for RIS, are marginal and do not justify the inclusion of a separate user interface section. The connection between the timestep-aware training and the interactive interface is not clearly established, making the user interface section feel like an add-on rather than an integral part of the core contribution. The limited performance gains also raise questions about the practical value of this interface.

3. Concerns about the baseline comparison: It's unclear whether the InstructPix2Pix baseline in RIS underwent equivalent training. The paper doesn't specify if the baseline was trained on specific RIS datasets, raising questions about the fairness of comparing a general image editing model with a task-specific fine-tuned model. The lack of clarity on the training procedure for the InstructPix2Pix baseline makes it difficult to assess the true contribution of the proposed method. If the baseline was not fine-tuned on the RIS dataset, the comparison is not valid, and the reported improvements may be misleading. A fair comparison requires that all models are trained under similar conditions.

### Questions
Please refer to the weaknesses section, particularly regarding:
1. The justification for baseline comparison methodology
2. The rationale behind including the user interface section in this paper

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work proposes a method to bridge the gap between generative diffusion models and discriminative perception tasks by aligning the generative denoising process with perception objectives. One of its contributions is designing a loss function to reflect the varied contributions of timesteps. At the same time, it introduces diffusion-tailored data augmentation to simulate training-denoising distribution shifts and leverages the denoising process as an interactive interface for user correctional prompts. These enhancements improve performance without requiring architectural changes.

### Strengths
1. The paper presents a new way to make generative diffusion models work better for visual tasks by aligning them with discriminative tasks and gets SOTA performance.
2. It explains the differences between generative and discriminative processes and offers specific solutions like adjusting timestep sampling and using data augmentation designed for diffusion.
3. The method takes advantage of the interactive denoising process, allowing for correctional prompts and multiple rounds of interaction, which sets it apart from traditional models.

### Weaknesses
1. The data augmentation techniques used in this paper are quite standard for perception tasks and don't offer much innovation. Specifically, while the paper mentions augmenting the ground truth, the actual transformations (e.g., color, shape, location changes for masks, or blurring for depth maps) are common in various perception tasks. The novelty of applying these to the ground truth rather than the input image is not thoroughly explored or justified, and it's unclear if this approach provides a significant advantage over traditional augmentations applied to the input.
2. Although the paper demonstrates improvements in certain tasks, the applicability of these methods to a wider range of perception tasks and datasets still needs thorough validation. The experiments are limited to depth estimation, referring image segmentation, and a generalist model, which, while representative, do not cover the full spectrum of perception tasks. It remains unclear how well this approach would generalize to tasks like pose estimation, 3D reconstruction, or other complex perception problems. The evaluation also lacks a detailed analysis of the model's behavior under various real-world conditions, such as different lighting, weather, or occlusions, which are crucial for assessing robustness.

### Questions
The proposed methods demonstrate strong performance on zero-shot benchmarks, but how robust and generalizable are these models in real-world applications? Are there additional experiments or analyses that validate the model’s stability across different environments and conditions?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper aims to improve the performance of repurposing the diffusion models as the deterministic task models. First, the authors analyze the performance changes through the denoising process of diffusion models in an RIS task, and they find that later timesteps are more influential to the mIOU but there is a decreasing tendency in mIOU when approaching the smaller timesteps. They hypothesize the reason for this finding as 1) the unequalized contribution of denoising steps and 2) the training-denoising distribution shift. To deal with the first challenge, they propose loss scaling and timestep sampling methods, which reflect varied contributions of each timestep for deterministic tasks. For the second challenge, data augmentation strategies suitable for each task are utilized to reduce exposure biases. Finally, they argue that the generative process in diffusion models is beneficial in reflecting users' feedback on perception tasks and propose agentic workflows that conduct multi-round interactions. The various experiments are conducted to show the effectiveness of their method mainly focusing on improving Marigold, InstructPix2Pix, and InstructCV. Technical details and additional experimental results are mainly presented in the Appendix.

### Strengths
- This paper deals with deep explorations of the denoising procedure of diffusion models in visual perception tasks.
- The main strength of this paper is the performance improvement. As shown in the results, the proposed methods offer substantial performance enhancement for various models.

### Weaknesses
 - **W1-1) (Minor)** This paper introduces numerous techniques, but some details are obscured or inaccurately described. For example, in Eq. (2), $c_t^2$ is presented as a weight for each loss term based on the timestep, yet it is also used in the timestep sampling distribution in Fig. 2. It remains unclear whether $c_t^2$ is intended as a loss weight, a sampling weight, or both, and how this choice impacts the training dynamics and final performance.
- **W1-2) (Major)** Furthermore, I cannot find the details of the analysis in Fig. 1. It is unclear how the authors calculated mIOU scores during the sampling process. If these scores are derived using only the estimated $x_0$​ values partway through the sampling, they don’t reflect the final generated results. Using these incomplete samples to support the authors’ conclusions seems insufficient. In other words, simply examining the denoising behavior of partial generations does not fully represent the actual generation process. A more accurate approach would be to inspect denoising characteristics across the complete generation process, as this would better validate the claims. Additionally, the stochastic nature of the diffusion sampling process, governed by a Stochastic Differential Equation (SDE), introduces variability. The authors should clarify whether the reported IoU scores are averaged over multiple runs or if a specific sampling strategy is employed to ensure consistency, and discuss how this variability might impact the analysis.
- **W2) (Major)** The technical contribution of this paper in the proposal of 1) a loss scaling and timestep sampling methods and 2) the dataset augmentation for each task can be trivial without comparing baselines.
  - **W2-1)** The authors introduce loss scaling and timestep sampling methods based on their observations of uneven contributions to performance. In the context of loss-weighting and timestep-sampling strategies within diffusion models [1, 2, 3, 4, 5], several studies have shown that emphasizing the loss at later timesteps can enhance model performance. The core operation of the authors’ method appears similar to these existing techniques. Therefore, without direct comparisons to these established methods, it is difficult to be convinced of any distinct advantage offered by the proposed approach in deterministic task setups. I suggest adding the comparative results with these methods.
  - **W2-2)** Similar to W2-1), [6] also deals with timestep-dependent data augmentation and it is necessary to compare this to validate the advantages of the proposed methods. Also, incorporating the data augmentation strategy for reducing exposure biases in diffusion models is already mentioned in [7]. In this regard, I suggest adding the comparative results with data augmentation works in diffusion model contexts.

- **W3) (Minor)** The proposed methods require a manual setup for data augmentation and $c_t$.

### Questions
Q1: Why is linear regression needed in estimating $c_t$​ instead of determining $c_t$ directly?

### Soundness
3

### Presentation
3

### Contribution
2
