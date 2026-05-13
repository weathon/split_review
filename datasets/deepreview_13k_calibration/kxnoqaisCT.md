# Navigating the Digital World as Humans Do: Universal Visual Grounding for GUI Agents

- Decision: Accept
- Avg Score: 7.75
- Scores: 8, 8, 5, 10

## Abstract
Multimodal large language models (MLLMs)
are transforming the capabilities of graphical user interface (GUI) agents, facilitating their transition from controlled simulations to complex, real-world applications across various platforms. 
However, the effectiveness of these agents hinges on the robustness of their grounding capability. 
Current GUI agents predominantly utilize text-based representations such as HTML or accessibility trees, which, despite their utility, often introduce noise, incompleteness, and increased computational overhead. 
In this paper, we advocate a human-like embodiment for GUI agents that perceive the environment entirely visually and directly take pixel-level operations on the GUI.
The key is visual grounding models that can accurately map diverse referring expressions of GUI elements to their coordinates on the GUI across different platforms.
We show that a simple recipe, which includes web-based synthetic data and slight adaptation of the LLaVA architecture, is surprisingly effective for training such visual grounding models.
We collect the largest dataset for GUI visual grounding so far, containing \num{10}M GUI elements and their referring expressions over \num{1.3}M screenshots, and use it to train \method, a strong universal visual grounding model for GUI agents.
Empirical results on six benchmarks spanning three categories (grounding, offline agent, and online agent) show that 1) \method substantially outperforms existing visual grounding models for GUI agents, by up to \num{20}\% absolute, and 2) agents with \method outperform state-of-the-art agents, despite the fact that existing agents use additional text-based input while ours only uses visual perception.
These results provide strong support for  the feasibility and promises of GUI agents that navigate the digital world as humans do.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a vision-only approach to GUI agents that mimics how humans interact with interfaces through visual perception and pixel-level operations. Moving away from conventional reliance on HTML and accessibility trees, the authors develop SeeAct-V, a framework for human-like GUI interaction, and UGround, a visual grounding model trained on the largest GUI grounding dataset to date (19M elements). Through comprehensive evaluation across six benchmarks, they demonstrate that UGround outperforms existing grounding models by up to 20%, while SeeAct-V agents match or exceed state-of-the-art agents that use additional text-based input.

### Strengths
- This paper contributes to reframes GUI interaction as a pure visual grounding problem, challenging the conventional wisdom that additional textual representations are necessary.
- The authors develop a novel way to generate diverse referring expressions (REs) by categorizing them into visual, positional, and functional types. And they introduce an innovative hybrid data synthesis pipeline that combines rule-based and LLM-based approaches
- This paper includes a comprehensive agent evaluation covering Three platforms (web, desktop, mobile), Three evaluation settings, (grounding, offline agent, online agent) six different benchmarks.

### Weaknesses
 - UGround relies on an external LLM planner and cannot operate independently as a GUI agent without training on downstream tasks. When combined with the Scaling Curve in Figure 5 on Web-Hybrid, it becomes challenging to enhance agent performance by merely increasing grounding data. Instead, improvements depend on the external LLM planner, which may limit the potential of the SeeAct-V framework.

- In the current model architecture, the authors have increased the input image size to 36 grids of CLIP@224. This results in a large number of image tokens ((224/14)^2 * 36 = 9,216), leading to inefficiency. The authors could conduct an ablation study to determine if this resolution is necessary, considering the cost of image tokens.

### Questions
- What factors contribute to the higher Completion Rate (CR) of the image-based model (GPT-4o with UGround) compared to the text-based model on Mind2Web-Live (Table 7), even though the Success Rate (SR) is comparable or lower? Could the grounding method (UGround vs. Choice) impact CR and SR differently across input modalities?

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
5

### Summary
This paper introduces UGround, a universal GUI visual grounding model, and SeeAct-V, a vision-only framework for GUI agents. The key contributions include: (1) A novel hybrid data synthesis pipeline for creating large-scale GUI grounding training data from web sources, (2) A universal visual grounding model that achieves strong cross-platform generalization, and (3) A vision-only framework that achieves comparable or better performance than methods requiring additional textual inputs. The authors conduct comprehensive evaluations across six benchmarks spanning web, desktop, and mobile platforms, demonstrating the effectiveness of their approach in both offline and online settings.

### Strengths
1. Technical Innovation:
- Novel hybrid synthesis pipeline combining rule-based and LLM-based approaches
- Successful demonstration of cross-platform generalization without platform-specific training
- Effective vision-only framework that eliminates dependency on HTML/accessibility trees

2. Experimental Rigor:
- Comprehensive evaluation across multiple platforms and settings
- Strong performance improvements (up to 20% absolute improvement in standard setting)
- Thorough ablation studies on training data sources

3. Practical Impact:
- Reduces dependency on noisy and incomplete text-based representations
- Potentially more efficient due to reduced input processing requirements
- More closely mimics human interaction patterns with GUIs

4. Reproducibility:
- Clear methodology description
- Release of the largest GUI visual grounding dataset to date
- Public release of the UGround model

5. Thorough Motivation and Analysis:
- Excellent analysis of the necessity for vision-only approaches
- Clear quantification of overhead costs associated with a11y tree extraction
- Convincing demonstration of additional computational burden from processing textual information
- Well-reasoned arguments for moving away from text-based representations

### Weaknesses
1. Data Efficiency:
- Heavy reliance on large-scale synthetic data, which, while effective, raises concerns about the cost of generating and storing such datasets.
- Potential redundancy in web-based training data, particularly with respect to similar page layouts and repetitive elements, which could lead to overfitting or inefficient learning.
- Room for improvement in data deduplication and grouping, specifically in identifying and removing near-duplicate screenshots and grouping similar UI elements to reduce the effective size of the training data.

2. Limited Coverage:
- Lack of desktop UI data in training, which could limit the model's ability to generalize to the diverse widget types and interaction patterns found in desktop applications.
- Incomplete handling of long-tail elements, such as less common icons, custom widgets, and application-specific UI components, which are crucial for robust performance in real-world scenarios.
- Platform-specific icons and elements not fully addressed, leading to potential performance degradation when encountering UI elements that are unique to certain operating systems or applications.

3. Dependencies:
- Reliance on external planner, which limits the standalone capability of the proposed model as a complete GUI agent.
- No end-to-end training with downstream tasks, making it difficult to assess the model's performance in a fully integrated system.
- Limited standalone capability as a GUI agent, requiring integration with other components for practical use, which adds complexity to the overall system design.

### Questions
Thank you for this interesting paper on vision-based web UI understanding. I have several questions and suggestions that I believe could help strengthen the work:

1. **Data Collection and Processing Details:**
   - Could you provide specific details about your webpage rendering and screenshot capture process? In particular:
     - What techniques do you use to capture content beyond the initial viewport?
     - How do you handle dynamic content that requires scrolling?
     - What is your approach for capturing interactive elements (dropdowns, expanded menus) that only appear after user interaction?
   - Documenting these technical details would help others reproduce your data collection pipeline.

2. **Desktop Application Extension:**
   - Your paper mentions potential extensions to desktop applications. Could you elaborate on:
     - What specific approaches have you considered for adapting your data collection pipeline to desktop environments?
     - How would you address the challenge of capturing UI states in desktop apps with complex interaction patterns?
     - What modifications to your current methodology would be needed to handle the diverse widget types and layouts found in desktop applications?

3. **Performance Benchmarks:**
   - Have you conducted timing experiments comparing your vision-only approach to methods that use accessibility trees, particularly for the online agent evaluation tasks?
   - Could you provide detailed end-to-end latency comparisons between your approach and traditional methods across different scenarios?
   - What are the specific performance implications of eliminating accessibility tree extraction in real-world applications?

4. **Benchmark Selection:**
   - I noticed that the evaluation doesn't include the widely-used WebArena/WorkArena/OSWorld/WindowsAgentArena benchmark. Could you explain:
     - What specific technical or methodological challenges prevented its inclusion?
     - Whether your approach is fundamentally incompatible with the these testing environments?
     - If there are plans to evaluate on this benchmark in future work?
   
This additional context would help readers better understand the scope and limitations of your approach, particularly regarding its applicability to different UI environments and its performance characteristics.

The current results are promising, but addressing these points would significantly strengthen the paper's contribution to the field.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposed a visual-based GUI Agent framework (SeeAct-V) with a GPT-aid planner and a visual grounding model (UGround). The planner first generates a textual plan, and the visual grounding model produces the coordinate of the target element. The paper constructs a training dataset (Web-Hybird) to train the grounding model. SeeAct-V is evaluated on 3 settings (visual grounding, offline and online agent evaluation).  The results validate UGround’s efficacy as a universal grounding model for GUI agents.

### Strengths
This paper propose a visual-based GUI Agent to avoid the limitations of language-based approaches. A large-scale dataset is collected through a carefully designed data collection method and used to train the visual grounding model. The paper is well-structured, clearly articulated, and demonstrates solid effectiveness in the proposed method.

### Weaknesses
Limitations in Completeness

1. This paper compares *UGround* with other models in Table 2 and shows UGround’s universal grounding capability. However, these methods differ in both their model settings and the training data used. An ablation study is missing to clarify the contributions of the model design (specifically the image resolution setting) and the training data to UGround's performance.

2. Same issue as in 1. This paper proposes 3 types of REs for GUI elements. An ablation study is missing to clarify the contribution of  each type of RE.

3 Related work on current GUI agents is missing from the main text.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
10

### Rating Number
10

### Confidence
5

### Summary
The paper presents a novel approach to enhancing GUI agents by adopting a human-like embodiment that solely relies on visual perception and various operations. It addresses the limitations of current GUI agents that depend on text-based representations (HTML, accessibility trees, etc.), which often introduce noise and computational overhead. The authors propose UGround, a visual grounding model trained on a large dataset of GUI elements (19M GUI elements across 1.3M screenshots). Their framework, SeeAct-V, allows GUI agents to perceive and interact with their environment visually, improving grounding accuracy and agent performance. The empirical evaluation across six benchmarks shows that UGround outperforms state-of-the-art models, offering a promising solution for GUI agents to function more like humans in digital environments.

### Strengths
I think this paper addresses well on the bottleneck of MLLM-based GUI Agents, UI Grounding, with a newly constructed synthetic dataset, which is timely and important.

- **Human-Like Embodiment for GUI Agents**: The paper makes a compelling argument for GUI agents that perceive their environment visually, which aligns better with how humans interact with GUIs.
- **Extensive Grounding Dataset**: UGround is trained on a comprehensive dataset of 19 million GUI elements, making it the largest dataset for GUI visual grounding.
- **Significant Performance Gains**: The empirical results demonstrate that UGround improves grounding accuracy by up to 20%, and agents using it outperform models that rely on both visual and text-based inputs.
- **Cross-Platform Generalization**: UGround shows strong performance across different platforms (desktop, web, mobile), which demonstrates its potential as a universal solution.
- Comprehensive Evaluation: The authors evaluate UGround on six benchmarks, which span grounding tasks and online/offline agent evaluations, providing a thorough analysis of the model's capabilities.

### Weaknesses
 - **LLM Usage in Synthesizing Data**: While the dataset is large, much of it is synthetically generated using LLMs. This raises concerns about potential hallucinations during data synthesis. The authors should consider sampling a subset of the data for human evaluation to verify the accuracy and goal alignment of the generated content, especially when leveraging models like LLaVA-Next-13B and GPT-4o for generating and refining referring expressions (REs), as well as LLaMA-3-8B in polishing. Here is a potential experiment setup suggested by GPT's feedback: `Randomly sample 1000 generated referring expressions and have human annotators rate their accuracy and relevance.` I think this advice is acceptable.
- **Dataset Analysis**: A deeper analysis of the dataset's diversity, as mentioned in line 169, would strengthen the work. Techniques such as PCA could provide insights into the data distribution. Additionally, more information is needed on how well the instructions used for planning in GUI agents align with the dataset used for training the grounding model. A breakdown of the types of GUI elements represented in the dataset, or t-SNE plots to visualize the distribution of referring expressions is suggested.
- **Typos**: There is a citation typo in line 307 related to CogAgent, which should be corrected.
- **Copyright Concerns**: The paper uses webpage data crawled from Common Crawl. It would be helpful for the authors to address any potential copyright issues associated with using this data. The authors are suggested to specifically discuss their data usage policy and any steps they've taken to ensure compliance with copyright laws when using Common Crawl data.
- **Environment Limitation**: The grounding dataset was collected entirely in a web environment, which represents only a subset of GUIs. The authors have discussed this limitation and I think it is not a big problem given that GUI elements can transfer smoothly. However, it's still worth emphasizing that this could impact the model’s performance in other GUI environments. Include a small-scale experiment or case study demonstrating the model's performance on a non-web GUI task is suggested.

### Questions
See Weakness above. 

I think the authors can include a section to discuss copyright problems.

### Soundness
3

### Presentation
4

### Contribution
3
