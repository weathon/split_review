# Mora: Enabling Generalist Video Generation via A Multi-Agent Framework

- Decision: Reject
- Avg Score: 5.67
- Scores: 6, 5, 6

## Abstract
Text-to-video generation has made significant strides, but replicating the capabilities of advanced systems like OpenAI’s Sora remains challenging due to their closed-source nature. Existing open-source methods struggle to achieve comparable performance, often hindered by ineffective agent collaboration and inadequate training data quality. In this paper, we introduce \OURS, a novel multi-agent framework that leverages existing open-source modules to replicate Sora’s functionalities. We address these fundamental limitations by proposing three key techniques: (1) multi-agent fine-tuning with a self-modulation factor to enhance inter-agent coordination, (2) a data-free training strategy that uses large models to synthesize training data, and (3) a human-in-the-loop mechanism combined with multimodal large language models for data filtering to ensure high-quality training datasets. Our comprehensive experiments on six video generation tasks demonstrate that \OURS achieves performance comparable to Sora on VBench \cite{huang2024vbench}, outperforming existing open-source methods across various tasks. Specifically, in the text-to-video generation task, \OURS achieved a Video Quality score of 0.800, surpassing Sora’s 0.797 and outperforming all other baseline models across six key metrics. Additionally, in the image-to-video generation task, \OURS achieved a perfect Dynamic Degree score of 1.00, demonstrating exceptional capability in enhancing motion realism and achieving higher Imaging Quality than Sora. These results highlight the potential of collaborative multi-agent systems and human-in-the-loop mechanisms in advancing text-to-video generation.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces Mora, a novel multi-agent  video generation framework, which leverages existing open-source modules to replicate Sora’s functionalities. Mora enhances inter-agent coordination through multi-agent fine-tuning with a self-modulation factor and uses a data-free training strategy to synthesize high-quality training data. It also incorporates a human-in-the-loop mechanism for data filtering. Evaluation shows Mora achieves comparable performance to Sora.

### Strengths
(1) Comprehensive system: The proposed Mora is capable of handling a wide range of visual generation and editing tasks, including Text-to-Image Generation, Image-to-Image Generation, Image-to-Video Generation, and Video Connection. 

(2) Clarity of Writing: The writing is clear and easy to follow, making the paper accessible to a broader audience.

(3) Code Availability: Although the training code is not provided, the authors have shared part of their code in the supplementary materials, promoting transparency and potential reproducibility of their results.

### Weaknesses
 (1) Limited Novelty: The paper's primary contribution lies in utilizing a language model as an agent to call various pre-existing  visual generation models for video generation. However, neither the agent system nor the video generation models are novel contributions from the authors. Although the authors propose some additional modules to optimize the system, these present several issues, as outlined below.

(2) Concerns with Self-Modulated Fine-Tuning Algorithm: In Section 3.2, the authors introduce a self-modulated fine-tuning  algorithm that optimizes both the language model (A1) and visual generation models (A2-A5) end-to-end  using a visual generation loss. This concept is unconventional and lacks sufficient supporting research. The authors do not provide adequate citations to justify this algorithm. Additionally:

(2.1) The process is inherently difficult to optimize. The authors mention using only 96 samples for training in Section 4.2, which is unconvincing for such a complex task.

(2.2) Without releasing the training code, it is hard to assess the effectiveness of their methodology based solely on theoretical descriptions and hyperparameter choices.

(2.3) The visual results (Figures 9-12)  show significant artifacts, such as blurriness and object deformation, which raise doubts about the efficacy of the self-modulated fine-tuning algorithm.

(3) Data-Free Training Strategy and Distillation Concerns: The authors propose a data-free training strategy using large models to synthesize training data, which resembles a distillation approach. However, this strategy may cause the generated results to overfit to the large models. This calls into question the added value of using a multi-agent  approach, which typically comes with higher inference costs. The authors should provide a fair comparison to demonstrate that training Mora with this strategy yields better performance  than directly distilling a smaller model. Additionally, quantitative analysis of agent success rates and inference efficiency would strengthen the claims made about the multi-agent system’s benefits.

(4) Problem Definition in Section 3.1: The authors claim that their objective is to maximize quality metrics while ensuring diversity in the generated videos. However, quality metrics alone are not the ultimate goal for video generation. Beating existing benchmarks such as SORA does not inherently demonstrate the model's superiority. Furthermore, in an agent-based system, other factors such as module collaboration speed, accuracy, and robustness must be considered.

### Questions
（1）Optimization Challenges with the Self-Modulated Fine-Tuning Algorithm:

（1.1）The self-modulated fine-tuning algorithm in Section 3.2 is unconventional and lacks supporting citations. Could the authors provide more references or evidence to justify this approach?

（1.2）Given the complexity of optimizing such a system, training with only 96 samples seems inadequate. Can the authors elaborate on how this sample size is sufficient, or provide results from larger-scale experiments?

（1.3) The visual results show significant artifacts like blurriness and object deformation. How do the authors plan to address these issues to improve visual quality?


（2）Effectiveness of Data-Free Training Strategy:

（2.1）The data-free training strategy resembles a distillation approach and may result in overfitting to large models. Can the authors show comparative experiments to demonstrate that the proposed multi-agent approach offers clear advantages over simply distilling a smaller model?

（2.2）Additionally, can the authors provide a quantitative analysis of agent success rates and inference efficiency to better justify the benefits of using the multi-agent system?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces a new generalist framework named Mora that synergies Standard Operating Procedures for video generation. The proposed Mora can be used to tackle a lot  of video-related tasks. Specifically,  Mora consists of five Agents: Prompt Selection and Generation Agent, Text-to-Image Generation Agent, Image-to-Image Generation Agent, Image-to-Video Generation Agen, and Video Connection Agent. Experimental results show the effectiveness of the proposed method, and Mora can surpass the capabilities of existing leading models in several respects.

### Strengths
- A new generalist Agent-based framework named Mora is proposed.
- The proposed Mora can perform a lot of video-related tasks and shows remarkable results.
- Experimental results indicate the effectiveness of the proposed method, and Mora can surpass the capabilities of existing leading models in several respects.

### Weaknesses
 - This paper contains a lot of existing techniques involving Prompt enhancement, Image generation, Image editing, Video generation, and Video connection. The main technical innovations should be clarified. Explaining how the system's architecture or the interaction between components differs from or improves upon existing approaches may help readers to understand.
- Since many components are involved, Mora's inference speed and computational requirements to existing state-of-the-art models for each of the video-related tasks mentioned should be discussed. Additionally, is there any optimizations implemented to improve efficiency, given the multi-component nature of the system.
- Will there be accumulated errors between multiple components? Providing empirical results showing how errors may or may not accumulate across different components and tasks is necessary. Or are there any techniques implemented to mitigate potential error accumulation between components?

### Questions
Please refer to Weaknesses for more details.

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
This paper proposes a multi-agent framework named Mora to enable text-to-video generation by leveraging open-source models such as Llama and Stable Diffusion. The main contributions include a self-modulation factor for inter-agent coordination, a data-free training strategy and a human-in-the-loop data filtering. The authors compare the performances of Mora with Sora on six video generation tasks.

### Strengths
1. The authors break down the process of video generation into several steps and utilize off-the-shelf models to implement the generation process.
2. The authors clearly describe the whole pipeline.
3. Data systhesis and filtering strategy are used to improve the quality of training.

### Weaknesses
1. There are no demo videos provided by the authors, no gif files or no project website. It is hard to evaluate the quality of generated video with some sampled frames. 
2. The key component of the self-modulated training is the modulation factor. Is it able to visualized this factor? How does this factor change during training, and what is the range of its values? Does it converge to a stable value, or does it fluctuate? A visualization of this factor's evolution would be beneficial.
3. How would the performances be if the agents A1 to A5 were replaced with different models? It is unclear how sensitive the overall performance is to the specific choice of each agent model. For example, would replacing the text-to-image model with a different architecture significantly impact the final video quality? It is important to understand the robustness of the proposed framework to variations in the agent models.

### Questions
How to explain that a multi-step generation can perform better than an end-to-end generation? For example, why a combination of open-sourced text-generation model, text-to-image model, image-to-image model and image-to-video model can outperform an end-to-end open-source text-to-video generation model and replicate a close-source model's functionalities.

### Soundness
3

### Presentation
3

### Contribution
2
