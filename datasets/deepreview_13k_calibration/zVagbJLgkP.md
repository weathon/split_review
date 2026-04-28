# VipAct: Visual-Perception Enhancement via Specialized VLM Agent Collaboration and Tool-use

- Decision: Reject
- Avg Score: 5.33
- Scores: 5, 5, 6

## Abstract
While vision-language models (VLMs) have demonstrated remarkable performance across various tasks combining textual and visual information, they continue to struggle with fine-grained visual perception tasks that require detailed pixel-level analysis. Effectively eliciting comprehensive reasoning from VLMs on such intricate visual elements remains an open challenge. In this paper, we present \textsc{VipAct}, an agent framework that enhances VLMs by integrating multi-agent collaboration and vision expert models, enabling more precise visual understanding and comprehensive reasoning. \textsc{VipAct} consists of an orchestrator agent, which manages task requirement analysis, planning, and coordination, along with specialized agents that handle specific tasks such as image captioning and vision expert models that provide high-precision perceptual information. This multi-agent approach allows VLMs to better perform fine-grained visual perception tasks by synergizing planning, reasoning, and tool use. We evaluate \textsc{VipAct} on benchmarks featuring a diverse set of visual perception tasks, with experimental results demonstrating significant performance improvements over state-of-the-art baselines across all tasks. Furthermore, comprehensive ablation studies reveal the critical role of multi-agent collaboration in eliciting more detailed System-2 reasoning and highlight the importance of image input for task planning. Additionally, our error analysis identifies patterns of VLMs' inherent limitations in visual perception, providing insights into potential future improvements. \textsc{VipAct} offers a flexible and extensible framework, paving the way for more advanced visual perception systems across various real-world applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper presents a novel framework aimed at enhancing vision-language models (VLMs) in handling fine-grained visual perception tasks. The VIPACT framework incorporates an orchestrator agent for task management, specialized agents for tasks like image captioning, and vision expert models for detailed visual analysis. This multi-agent approach enables the VLMs to collaborate, utilize specialized tools, and aggregate evidence, leading to improved performance on benchmarks involving intricate visual tasks. Experimental results demonstrate VIPACT's superiority over state-of-the-art models, with ablation studies underscoring the importance of each component. The paper suggests VIPACT as a scalable, flexible system for real-world visual applications​

### Strengths
1. The VIPACT framework’s use of an orchestrator agent that coordinates with specialized agents and vision expert models stands out, as it improves VLMs' performance on fine-grained visual perception tasks by enabling collaborative reasoning. This structured, modular approach allows for flexibility and extensibility, making it adaptable for a wide range of tasks.
2. By employing System-2 reasoning, VIPACT goes beyond traditional VLM capabilities, integrating intermediate reasoning steps that are more complex and contextually rich. This approach enhances VLMs' ability to manage detailed visual information, which is crucial for tasks requiring in-depth visual analysis.
3. The paper includes extensive experiments across multiple benchmarks, showing clear performance gains over state-of-the-art methods in diverse visual tasks. These experiments demonstrate the framework's effectiveness and generalization ability, especially in tasks that are inherently challenging for current VLMs.

### Weaknesses
1. VIPACT relies heavily on models like GPT-4o for their advanced instruction-following and function-calling abilities. While the framework is adaptable, current results may not generalize effectively to other VLMs lacking these specific capabilities, restricting the framework's accessibility and broader applicability.

2. In MMVP benchmark, how does the proposed model compared with other vision foundation model like llava, internvl, eagle and so on? Eagle also use multi-expert collaboration, can the authors compare between them?

3. Did the authors use other models instead of GPT4-o? like gemini or internvl? If the performance of the proposed model mainly reply on GPT4-o, I will think the contribution is not enough.

### Questions
My questions are in the weakness. I will raise my score if my questions are answered.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces VIPACT, a novel framework designed to address fine-grained visual perception tasks, where current Vision-Language Models (VLMs) often underperform. VIPACT utilizes a collaborative multi-agent approach that integrates a central orchestrator agent with specialized agents and vision expert models to achieve more precise and detailed visual understanding.

Contributions:
1. Multi-Agent Collaboration Framework: VIPACT employs an orchestrator agent that manages task analysis, planning, and evidence aggregation, coordinating specialized agents to tackle specific tasks like image captioning and depth estimation. Specialized agents provide focused capabilities (e.g., object detection, depth estimation), enhancing VLM performance in tasks requiring detailed visual analysis.
2. Comprehensive Benchmarking: VIPACT outperforms state-of-the-art baselines on challenging visual perception benchmarks, including Blink and MMVP.
3. Ablation and Error Analysis: Through ablation studies, the paper highlights the importance of each component in VIPACT, while error analysis reveals specific limitations of current VLMs in spatial reasoning and fine-grained visual tasks, underscoring areas for further improvement in multi-modal perception systems.

### Strengths
1. The paper is mainly well-written and easy to follow. 
2. The paper proposes a new multi-agent framework for fine-grained visual perception tasks. 
3. The proposed framework is effective and improves the performance of two datasets over existing baselines.

### Weaknesses
1. The framework is tested on only one LLM. Testing on more, e.g., Claude / Gemini, would be more convincing and show the generalization of the framework.
2. The method proposed has limited contribution to the community. There have been multiple papers proposing/applying "LLM with visual tool use" to solve vision tasks. The multi-agent framework has also been verified to be effective on various downstream tasks. Specifically, the novelty of the proposed approach is not clearly demonstrated compared to existing methods that combine LLMs with visual tools, and the specific design choices within the multi-agent framework lack a strong justification in the context of fine-grained visual perception. The paper needs to articulate more clearly how the specific combination of agents and their interactions lead to improved performance, rather than just relying on the general concept of multi-agent collaboration. 
3. The performance of the proposed framework does not seem significant enough. On the Blink dataset, the improvement over CoT is less than 10 %. The improvement in the MMVP dataset is marginal, and the paper should provide a more detailed analysis of the types of errors that the proposed method still makes, and how these errors relate to the limitations of the underlying LLM and visual tools. A more thorough error analysis would help to better understand the specific challenges that remain in fine-grained visual perception, and how future research can address these challenges.

### Questions
1. Can the authors put an average column in Table 2 to better show the improvements of the method?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes VipAct, a VLM-based agent framework capable of performing challenging visual perception tasks by decomposing the tasks into sub-tasks which specialized agents and expert models then overtake. The VipAct framework is designed as a hierarchical pipeline, with a VLM as the orchestrator agent and specialized VLMs and expert vision models as the tools called by the orchestrator. Unlike existing visual programming methods (e.g., VisProg and MM-ReAct), ViaAct takes the vision task as its input and the input image. This innovation enables VipAct to decompose the high-level task into visually grounded and feasible subtasks that can be submitted to expert models. Ablation studies justify the introduced components, i.e., multiple agents, visual input, and vision experts.

### Strengths
1. The authors utilized a VLM-based programmatic framework to perform difficult vision tasks challenging for most existing VLMs.
2. The description of the ViaAct pipeline is clear and easy to understand.
3. The experiments are detailed and comprehensive.

### Weaknesses
1. It is still unclear how including the input image in the prompt to the orchestrator agent improves the fine-grained visual perception capability, although the experimental results show that removing this visual input leads to a performance decrease. At the beginning of the paper, the authors stated that "recent studies reveal that state-of-the-art (SOTA) VLMs continue to struggle with fine-grained or low-level visual perception tasks that are trivial for humans" (L43). Based on this premise, the orchestrator agent is also not capable of calling proper tools as which tools with fine-grained perception functionalities are to be called is also based on the fine-grained perception of the input image. The authors are expected to present more vivid examples of how the agent's behavior differs with and without visual input, which would help clarify this point.

2. Although the authors attempt to conduct fair comparisons, one key aspect - the tool sets used by the compared methods - is not fair enough. L400 states that "Another limitation is their inability to support images with visual prompts, preventing them from locating visual prompts and proceeding with subsequent operations". The compared methods were not given the necessary vision expert models to complete the tasks, thereby obtaining inferior results. The reviewer believes that the utilization of the vision experts, such as Visual Prompt Detector, is not part of the paper's innovations and that the compared methods should also be equipped with these vision experts in the experiments. The authors are expected to conduct additional comparisons where baseline methods are equipped with identical tools, or explain why such comparisons might not be feasible or relevant. This would provide a clearer picture of VipAct's unique contributions beyond the use of vision expert models.

### Questions
1. What if the authors replace the visual input to the orchestrator agent with a detailed description of it? Can this textual input achieve a satisfactory performance compared with using the original image? The authors may conduct an ablation study comparing performance across three conditions: 1) original image input, 2) detailed textual description input, and 3) both image and textual description as input. This would help isolate the unique contributions of visual versus textual information to the orchestrator agent's performance.

The reviewer would like to change the rating if the concerns are all resolved.

### Soundness
3

### Presentation
2

### Contribution
3
