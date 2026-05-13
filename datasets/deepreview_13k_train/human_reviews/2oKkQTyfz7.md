# General Scene Adaptation for Vision-and-Language Navigation

- Decision: Accept
- Scores: 6, 8, 6, 6, 6

## Abstract
Vision-and-Language Navigation (VLN) tasks mainly evaluate agents based on one-time execution of individual instructions across multiple environments, aiming to develop agents capable of functioning in any environment in a zero-shot manner. However, real-world navigation robots often operate in persistent environments with relatively consistent physical layouts, visual observations, and language styles from instructors. Such a gap in the task setting presents an opportunity to improve VLN agents by incorporating continuous adaptation to specific environments. To better reflect these real-world conditions, we introduce GSA-VLN (General Scene Adaptation for VLN), a novel task requiring agents to execute navigation instructions within a specific scene and simultaneously adapt to it for improved performance over time. To evaluate the proposed task, one has to address two challenges in existing VLN datasets: the lack of out-of-distribution (OOD) data, and the limited number and style diversity of instructions for each scene. Therefore, we propose a new dataset, GSA-R2R, which significantly expands the diversity and quantity of environments and instructions for the Room-to-Room (R2R) dataset to evaluate agent adaptability in both ID and OOD contexts. Furthermore, we design a three-stage instruction orchestration pipeline that leverages large language models (LLMs) to refine speaker-generated instructions and apply role-playing techniques to rephrase instructions into different speaking styles. This is motivated by the observation that each individual user often has consistent signatures or preferences in their instructions,  taking the use case of home robotic assistants as an example. We conducted extensive experiments on GSA-R2R to thoroughly evaluate our dataset and benchmark various methods, revealing key factors enabling agents to adapt to specific environments. Based on our findings, we propose a novel method, Graph-Retained DUET (GR-DUET), which incorporates memory-based navigation graphs with an environment-specific training strategy, achieving state-of-the-art results on all GSA-R2R splits.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes GSA-VLN (General Scene Adaptation for Vision-and-Language Navigation), a task designed to enhance the performance of navigation agents by enabling them to adapt to specific environments, particularly when exploring in the same environment over an extended period. The authors also introduce GSA-R2R, an expanded version of the HM3D and MP3D dataset, offering richer environments and more diverse instructions. Additionally, they present a novel method, GR-DUET, which improves navigation performance by utilizing memory mechanisms and updating graph structures.

### Strengths
Novelty:
The paper introduces a new task, GSA-VLN, which focuses on the long-term adaptation of agents within specific environments, a capability with significant potential for real-world applications.

Dataset Contribution:
The authors present the GSA-R2R dataset, which extends the existing R2R dataset by using GPT-4 and a three-stage method to generate instructions in various speaking styles. The dataset is divided into residential and non-residential environments, serving as in-distribution (ID) and out-of-distribution (OOD) data, respectively.

Method Design:
The GR-DUET method integrates topological graphs with memory mechanisms, effectively preserving historical information and updating it continuously during navigation. This approach demonstrates notable improvements in performance, particularly in OOD (non-residential) scenarios.

Experimental Results:
The paper compares GR-DUET with optimization-based and memory-based methods across different environment and speaking style splits. The experiments highlight the feasibility of the GSA-VLN task and the effectiveness of the GR-DUET method in various settings.

### Weaknesses
Please see the Questions section for detailed improvement suggestions and questions.
I look forward to the authors' responses to these questions, as addressing these points could significantly clarify some of the paper's contributions and limitations. I am open to adjusting my score if the authors provide further insights or resolve the concerns raised above.

### Questions
1. Memory Mechanism Scalability:
While the memory-based approach in GR-DUET performs well in your experiments, how does this method scale to larger or more complex environments? As the environment size or the number of instructions increases, the memory bank may become too large to manage efficiently. Could you provide further analysis or experiments that demonstrate how the method performs with continuous accumulation of data in larger datasets or more complex environments?

2. the paper lacks a detailed discussion on how the memory is utilized, including how similar tasks are stored, how memory is retrieved and assessed for relevance and validity, and how prior knowledge is leveraged. Is the memory bank pre-set or updated dynamically? If it is updated dynamically, how is the correctness of the stored memories ensured, especially when handling diverse memories? How are the initial model parameters (L194, L198) initialized to ensure sufficient generalization? Please provide more details

3. Furthermore, other memory-based VLN methods, such as SG-Nav [1], provide more detailed storage and query mechanisms based on topological graphs and memory updates. Could you compare your approach with SG-Nav in terms of performance or highlight any differences and advantages?

4. Adaptation to Instruction Styles:
You mention using GPT-4 and a three-stage process to generate different instruction styles, but it remains unclear how the agent adapts to these varying styles over time. Could you provide more quantitative and qualitative results on how GR-DUET handles changes in style, particularly in OOD environments? A deeper analysis of how different speaking styles affect agent performance and adaptability would offer valuable insights into the robustness of your method in real-world scenarios, where user communication patterns may vary significantly.

5. Unsupervised Learning and Adaptation Efficiency:
The paper suggests that agents in GSA-VLN can improve their performance over time using unsupervised learning techniques. Could you clarify how quickly the agents adapt in different environments? Are there any cases where adaptation is less effective or slower? Are there specific environments where the memory mechanism struggles to adapt? A more detailed breakdown of adaptation speed and efficiency across different environment types would help clarify the limitations of your approach and guide future improvements.

6. Practical Deployment and Real-World Use Cases:
The GSA-VLN task is well-motivated by real-world scenarios, but the paper does not provide a detailed discussion on how the proposed method could be deployed in practical systems. Could you elaborate on the computational and memory overhead of your approach in real-time systems, such as those used in robotics or autonomous agents?

Reference:
[1] Yin, Hang, et al. "SG-Nav: Online 3D Scene Graph Prompting for LLM-based Zero-shot Object Navigation." arXiv preprint arXiv:2410.08189 (2024).

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper presents General Scene Adaptation for Vision-and-Language Navigation (GSA-VLN), a new VLN task where agents adapt to and improve in a specific environment over time, making it closer to real-world applications. To support this, the authors introduce GSA-R2R, a dataset that expands on Room-to-Room (R2R) by adding more diverse environments and instruction styles, including out-of-distribution examples. They also propose Graph-Retained DUET (GR-DUET), a method that uses memory-based navigation graphs and scene-specific training to help agents learn and retain scene-specific information, achieving strong results on the GSA-R2R benchmarks.

### Strengths
1. This paper introduces the novel General Scene Adaptation for Vision-and-Language Navigation (GSA-VLN) task, filling a critical gap in VLN research by focusing on adaptation in persistent environments. Rather than assuming agents will encounter only unseen environments, GSA-VLN models a more realistic scenario where agents learn and improve over time within a familiar setting. This shift in task formulation is both timely and innovative, especially as VLN moves toward practical applications.
2. The paper demonstrates rigorous methodology in creating the GSA-R2R dataset, expanding on the Room-to-Room (R2R) dataset with a variety of environments, instruction styles, and out-of-distribution examples to thoroughly test agent adaptability. The proposed Graph-Retained DUET (GR-DUET) model is well-designed, combining memory-based navigation graphs with a scene-specific training strategy, and shows significant performance improvements across metrics. 
3. The paper is clearly organized and effectively conveys the importance of long-term scene adaptation in VLN.

### Weaknesses
1. The GR-DUET method involves a memory bank and a global graph that retains historical information across episodes. As the memory and graph size increase, the model’s computational requirements may grow significantly, particularly for long-term navigation in large environments. While the paper includes an environment-specific training strategy to limit graph expansion, providing an analysis of computational costs and potential trade-offs between memory retention and scalability would strengthen the model's practicality for deployment on resource-constrained systems. Specifically, the paper lacks a detailed breakdown of how memory usage scales with the number of nodes and edges in the navigation graph, and how this impacts inference time, especially in complex environments with many interconnected locations. A more thorough analysis should quantify the memory footprint and inference latency as a function of graph size and episode length, which would be crucial for assessing the model's suitability for real-world applications.
2. While the GSA-R2R dataset is a notable improvement over existing datasets for testing scene-specific adaptation, it may still fall short in representing the full diversity of real-world environments and interaction styles. The dataset includes a mix of residential and non-residential scenes, but further validation with a broader set of real-world environments could strengthen the model's applicability. Including additional scene types, such as commercial or outdoor spaces, or testing in dynamic environments where the layout changes over time, would push the dataset closer to real-world settings. The current dataset, while diverse in scene types, may not fully capture the complexities of real-world environments, such as those with highly variable lighting conditions, occlusions, or cluttered spaces. A more rigorous evaluation should include environments that present these challenges to better assess the robustness of the proposed method.
3. Although the paper’s three-stage instruction generation pipeline enhances instruction diversity, more detailed analysis on how different instruction styles (e.g., Basic, User, Scene) impact agent performance would be valuable. For instance, specific ablation studies on each instruction type could clarify how robust the GR-DUET model is to variances in language, phrasing, and style. Additionally, investigating how the model generalizes across speakers with different dialects or levels of detail in instructions could provide actionable insights into improving instruction handling. The paper should include a more detailed analysis of how the model's performance varies across different instruction styles, including a breakdown of success rates and error types for each style. This would help identify specific weaknesses in the model's ability to handle different types of instructions and guide future improvements.

### Questions
Please refer to the weaknesses section.

### Soundness
3

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
This paper presents a task that requires the VLN agent to execute VLN task in only one environment while storing its historical information at the same time. To make the initial parameters of the agent more general, the authors generate more environments and more instructions by using LLM. Finally, the paper also provides some experiment results according to their proposed metrics to further highlight the efficacy of the proposed methods.

### Strengths
1、This paper is written with details and clear presentations, easy to follow.

2、The author solves the VLN problem from a new perspective and divides the scenarios into Residential and Non-Residential.

### Weaknesses
1、The novelty of this paper is limited. The GSA-VLN TASK proposed in the paper is still a standard VLN task. The so-called “standard VLN task” mentioned by the paper also includes fine-tuning based on historical information and trained models, which are claimed as the novelty of GSA-VLN in Section 3.2. 

2、	Following the previous comment, the GSA-R2R DATASET proposed in the paper uses more environments (HM3D), and then uses tools such as LLM to refine the dataset's quality, which has been a common practice in VLN. Also, the author should not choose to ignore the existing works (e.g., HM3D-AutoVLN[1], Scale VLN[2], YouTube-VLN[3]) have also expanded and refined the VLN dataset when comparing (Table 1). I recommend the authors compare the datasets mentioned above and include them in the main manuscript (e.g. in Table I).

3、The comparison metrics in the experimental part are all newly proposed by the authors, which cannot correctly reflect the effectiveness of the method proposed. I suggest that the authors conduct experimental comparisons in standard VLN using common VLN metrics, and compare them on other VLN datasets besides R2R, such as REVERIR, RxR, CVDN and SOON.

### Questions
Line 283-286, how is the navigation model used here implemented? How can we ensure that it is a good instruction discriminator? I am concerned that if the navigation model is not trained well, it will not be enough to explain the quality of the instruction.

### Soundness
2

### Presentation
3

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
This paper proposes a new task, named GSA-VLN, which require agents to execute navigation instructions within a specific scene and simultaneously adapt to it for improved performance over time. This paper also proposes a new datast, GSA-R2R, which significantly expands the diversity and quantity of environments and instructions for the Room-to-Room (R2R) dataset to evaluate agent adaptability in both ID and OOD contexts. The biggest difference between the proposed task and dataset and previous work is the diversity of instructions, i.e., different individual features and linguistic conventions are taken into account.

### Strengths
1. The proposed GSA-VLN task and  GSA-R2R dataset which considers real-world robot adaptation in persistent environments, is an interesting research direction.
2. Overall, the writing is fluent and the figures convey the character of the task well.
3. The proposed GR-DUET method outperforms the baselines, demonstrating its effectiveness in helping agents adapt to specific environments.

### Weaknesses
1. Some baselines are missing. I suggest to add some baseline methods based on LLM, especially the Zero-shot VLN methods. For example, InstructNav[1], NavCot[2]. The reason for this suggestion is that LLM's reasoning is now so powerful that it may be able to adapt well for different personal characteristics and language styles without the need for an additional adaption process, i.e., in zero-shot manner.  Also, these different styles are essentially generated by LLM, so I'm concerned that these understanding these different styles is a very easy and undifferentiated thing for LLM to do. 
2. In this paper, the authors generated instructions for only five different character styles. However life can be much richer in terms of characters. The paper's contribution would have been greatly enhanced if the authors could propose a method for generating instructions for different character styles in a nearly infinite number of ways.
3. The authors propose GR-DUET, but there are few details about it. For a reader who does not know DUET well, it may cause some difficulties in reading, and I suggest the authors to add some descriptions and details in the appendix.

### Questions
In section 3.3.4, the authors invite 15 participants to evaluate the instructions. Are the backgrounds (e.g., ages, etc.) of these 15 participants sufficiently homogeneous to demonstrate the refinement of the assessment? Also, I recommend disclosing the questionnaire they used for the test.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents a novel task, GSA-VLN (General Scene Adaptation for Vision-and-Language Navigation), which trains agents to follow navigation instructions within a specific scene while adapting to it for enhanced performance over time. A new dataset, derived from the HM3D dataset, is introduced to support this task. Additionally, the authors propose a new method that serves as a baseline and achieves state-of-the-art performance in this domain.

### Strengths
- The paper is generally well motivated and the proposed tasks makes sense. For a pre-trained VLN agent, it is important to leverage the information and instructions in the new environment to further enhance it's knowledge and adapt to the new environment and uses.

- A new dataset GSA-R2R based on the HM3D dataset is introduced with new instruction data collected to support the VLN task. The dataset can potentially be useful for the community.

-  Extensive evaluation of current VLN methods on the new dataset and different adaption methods are benchmarked. The proposed GR-DUET method demonstrates competitive performance compared to prior work.

### Weaknesses
 - The concept of adapting a model to a test scene is not entirely new, as numerous prior methods have explored unsupervised exploration or adaptation within embodied environments.

- The Related Work section could be more comprehensive. For instance, some discussions are postponed to Section 4, but it's crucial to review prior work that also employs adaptation methods in VLN, particularly those utilizing memory-based approaches, and also highlight the main differences and contributions of the proposed method.

- Additionally, beyond the VLN literature, how does the proposed method relate to Lifelong Learning and Test-time Adaptation?

- Table 3 presents the navigation performance of various VLN models on the new dataset. Is the performance of these methods consistent with results on other benchmark datasets?

### Questions
Please see above.

### Soundness
3

### Presentation
3

### Contribution
2
