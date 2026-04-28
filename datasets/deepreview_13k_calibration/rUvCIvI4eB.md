# Towards Realistic UAV Vision-Language Navigation: Platform, Benchmark, and Methodology

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Developing agents capable of navigating to a target location based on language instructions and visual information, known as vision-language navigation (VLN), has attracted widespread interest. 
Most research has focused on ground-based agents, while UAV-based VLN remains relatively underexplored.
Recent efforts in UAV vision-language navigation predominantly adopt ground-based VLN settings, relying on predefined discrete action spaces and neglecting the inherent disparities in agent movement dynamics and the complexity of navigation tasks between ground and aerial environments. 
To address these disparities and challenges, we propose solutions from three perspectives: platform, benchmark, and methodology.
To enable realistic UAV trajectory simulation in VLN tasks, we propose the OpenUAV platform,  which features diverse environments, realistic flight control, and extensive algorithmic support.
We further construct a target-oriented VLN dataset consisting of approximately 12k trajectories on this platform, serving as the first dataset specifically designed for realistic UAV VLN tasks.
To tackle the challenges posed by complex aerial environments, we propose an assistant-guided UAV object search benchmark called UAV-Need-Help, which provides varying levels of guidance information to help UAVs better accomplish realistic VLN tasks.
We also propose a UAV navigation LLM that, given multi-view images, task descriptions, and assistant instructions, leverages the multimodal understanding capabilities of the MLLM to jointly process visual and textual information, and performs hierarchical trajectory generation.
The evaluation results of our method significantly outperform the baseline models, while there remains a considerable gap between our results and those achieved by human operators, underscoring the challenge presented by the UAV-Need-Help task.
The project homepage can be accessed at \url{https://prince687028.io/OpenUAV}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper makes three key contributions to advance realistic UAV vision-language navigation. First, they introduce OpenUAV, a simulation platform that properly models realistic drone flight dynamics with 6 degrees of freedom, rather than using simplified discrete movements like previous work. Second, they create what appears to be the first UAV navigation dataset (about 12k trajectories) that incorporates realistic flight physics. Third, they propose a novel "UAV-Need-Help" benchmark where an AI assistant provides varying levels of guidance, along with a hierarchical navigation model using large language models.
The approach significantly outperforms baselines in experiments, though still falls well short of human performance. What makes this work valuable is how it addresses fundamental limitations in current UAV navigation research by developing tools and datasets that better match reality, particularly through the inclusion of realistic flight dynamics. While substantial work remains before real-world deployment would be feasible, this paper lays important groundwork and provides valuable resources for future research in autonomous drone navigation.

### Strengths
1. The paper address realistic flight dynamics in UAV navigation instead of using oversimplified discrete actions.
2. Provides a comprehensive open-source simulation platform that combines realistic environments, flight physics, and algorithmic support.
3. Creates the first large-scale UAV navigation dataset (12k trajectories) that captures true 6-DOF flight dynamics.
4. Introduces a novel assistance mechanism with three levels of guidance, making the navigation task more adaptable and learnable.
5. Proposes a practical hierarchical architecture combining language models with trajectory planning for complex navigation.
6. Includes thorough experimental validation across different difficulty levels and scenarios, with clear comparisons to human performance.
7. Shows strong generalization ability on unseen objects, though with expected performance drops on unseen environments.

### Weaknesses
1. The dataset size (12k trajectories) is relatively small compared to other vision-language datasets, which might limit model learning. Lacks detailed comparison with real drone flight data to validate how well their simulation matches actual flight dynamics.
2. No discussion of computational requirements or real-time performance, which is crucial for practical drone navigation.
3. Success rate metrics (around 16-17%) are still quite low even with the highest level of assistance.
4. Missing ablation studies on different environmental conditions and their impact on navigation performance.
5. No discussion of safety mechanisms or fallback strategies when the navigation system fails.

### Questions
Please see the weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new framework for UAV navigation, focusing on the different challenges of aerial environments and ground-based agent navigation. 
A realistic UAV simulation platform, OpenUAV, is proposed, which supports continuous six-degree-of-freedom (6-DoF) trajectories, realistic flight dynamics, and diverse environmental scenarios. The platform integrates the AirSim plugin and Unreal Engine 4 (UE4) to achieve high-fidelity simulation.

UAV-Need-Help Benchmark: A new benchmark task introduces an assistant-guided UAV target search task, where the assistant provides different degrees of navigation guidance to the UAV to help it cope with complex navigation tasks.

UAV Navigation Large Model (LLM): A multimodal model is proposed that can process visual and textual information simultaneously and generate hierarchical navigation trajectories to address the complexity of UAV navigation in three-dimensional space. The platform, dataset, and method aim to narrow the gap between simulated UAV navigation tasks and practical applications, and provide more realistic and challenging tasks for UAV VLN research.

### Strengths
1. Comprehensive data set: The author contributes a large-scale goal-oriented UAV VLN data set, including 6-degree-of-freedom flight trajectories, providing a large number of training and evaluation resources for the research community.
2. Real UAV simulation: The OpenUAV platform significantly improves the authenticity of UAV navigation tasks, supports continuous flight trajectories, diverse environments and realistic flight dynamics, and solves the limitations of previous UAV VLN research.
3. Innovative benchmark task: The UAV-Need-Help benchmark introduces a challenge of practical significance, through different levels of help mechanisms, to cope with the challenges caused by the inherent dynamics of the aerial environment, obstructed views and changes in perspective.
4. Hierarchical trajectory generation: The proposed UAV navigation large model (LLM) combines long-range trajectory prediction and fine-grained control, and can handle the hierarchical complexity in UAV navigation tasks.
5. Parallelization and scalability: The platform supports efficient data collection and evaluation in parallel environments, which is crucial for large-scale UAV research.

### Weaknesses
Please see the Questions section for detailed improvement suggestions and questions.

### Questions
1. Real-world Deployment:
How well do the models and methods developed on the OpenUAV platform perform in real-world UAV navigation tasks? Has there been any experimental validation involving physical UAVs? Although the simulation platform is quite realistic, it remains unclear to what extent the models trained on this platform can generalize to real-world UAV tasks. A comparison with experiments using real UAVs is lacking.

2. Autonomy and Reliance on Assistance:
The UAV-Need-Help benchmark seems overly reliant on the assistance mechanism, which could reduce the autonomy of the UAV. It is unclear how the UAV Navigation LLM would perform without such assistance. Can the UAV autonomously recover from navigation failures in the absence of external help, particularly when faced with obstacles?

3. Efficiency and Real-time Performance:
Considering the complexity of the LLM-based navigation model, how feasible is the real-time deployment of such models on resource-constrained UAVs? Is there any analysis of the computational requirements and latency when running these models on actual drones?

4. Ablation Studies:
Could more insights be provided on the contribution of individual components (e.g., assistant guidance, hierarchical trajectory generation, sensor configurations)? How would the model's performance change if fewer sensors were used, or if the advanced trajectory decoder based on MLLMs were removed?

5. Lack of Comparison with Ground-based VLN:
While the paper highlights the differences between ground-based and UAV navigation, there is a lack of direct comparison with existing ground-based VLN methods(Seq2Seq[1], DUET[2], NavGPT2[3]). It is unclear what unique challenges the proposed framework addresses. Specifically, what are the differences between ground-based VLN methods and the UAV Navigation LLM? Could ground-based VLN methods be applied to OpenUAV, and if so, how would they perform?

6. Extensibility to Other Tasks
Besides the object search task, can the proposed platform and dataset be generalized to other UAV tasks such as mapping, exploration, or surveillance? Would the dataset require significant modifications to accommodate these tasks?

[1]Anderson, Peter, et al. "Vision-and-language navigation: Interpreting visually-grounded navigation instructions in real environments." Proceedings of the IEEE conference on computer vision and pattern recognition. 2018.
[2]Chen, Shizhe, et al. "Think global, act local: Dual-scale graph transformer for vision-and-language navigation." Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition. 2022.
[3]Zhou, Gengze, et al. "Navgpt-2: Unleashing navigational reasoning capability for large vision-language models." European Conference on Computer Vision. Springer, Cham, 2025.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper proposes a new UAV platform with several integrated scenes, continous action space and 6 DoF instead of previously 4. In addition they provide a VLN dataset together with a benchmark “UAV-Need-Help” together with an assistant that can provide guidance in three different levels. Lastly they have a model based on a LLM with a hirarchical strucutre that first predicts the target pose and then predicts the fine-grained path trajectory. The authors evaluate their model closed-loop and show qualitative results of the language predictions of the LLM.

### Strengths
S.1. Complete set to research UAVs. The paper provides a platform/ simulation environment, dataset, benchmark and a baseline model. This opens up a lot of possibilities for the community to do research in this field.

S.2. Baselines: Having multiple baselines for a new benchmark is important. I also appreciate the human baseline.

S.3. Hierarchical prediction: The concept of hierarchical predictions is interesting and makes sense. (But missing ablation to show that hierarchical is superior to directly predicting the fine-grained trajectory).

### Weaknesses
**W.1. Comparison to existing work**

1. The works seems to be quite similar to [AerialVLN](https://arxiv.org/abs/2308.06735) or CityNav. One difference mentioned is the DoF and the use of discrete actions. The authors of AerialVLN state “Although the simulator **supports flying towards any given direction and speed/distance**, we consider the eight most common low-level actions in UAVs:Move Forward, Turn Left, Turn Right, Ascend, Descend, Move Left, Move Right and Stop.”, which means in my understanding that they do support continuous actions. There dataset also includes language instructions. So I was wondering why this new simulator and dataset is needed and can’t be build on top of the existing one? It would be great if the authors could highlight unique features or improvements their simulator offers, and explain why building on existing platforms was not sufficient for their research goals. Specifically, a more detailed comparison of the trajectory generation and control mechanisms would be beneficial. It's unclear if the continuous actions in AerialVLN are truly exploited or if they are merely a theoretical capability not used in practice. Furthermore, the level of realism in the simulated flight dynamics and sensor data should be explicitly compared.
2. Difference to AirSim: AirSim does provide an API and a human control interface supporting PX4. In the paper it sounds like this is a contribution of the new platform OpenUAV (e.g. line 212 ff.). It would be good to make it more clear in the whole paper what is used from existing works and which parts are new in this paper. The paper should clearly delineate which components are directly adopted from AirSim, which are modified, and which are entirely novel contributions. The specific enhancements made to the AirSim API should be detailed, including how these modifications facilitate the continuous trajectory control and data collection.
3. Difference to related work that combines UE + AirSIM: The authors state that several works “have combined UE with AirSim to develop high-fidelity imaging platforms. However, these platforms either suffer from low rendering precision or lack algorithmic support for continuous trajectory VLN tasks”. (line 149) Since the authors also combine UE with AirSim, it would be great if the differences to the existing works could be described in more detail. The paper needs to specify the limitations of existing UE+AirSim combinations, focusing on aspects like rendering fidelity, sensor simulation accuracy, and the ability to support continuous trajectory generation for VLN tasks. A table comparing these aspects across different platforms would be helpful.

**W.2. Details of descriptions/ Clarity**

1. Naming: There is already an OpenUAV platform (see[1]). It would be good to use an unique naming and also elaborate the differences. The paper should explicitly acknowledge the existing OpenUAV platform and clearly distinguish itself, perhaps by highlighting different focus areas or functionalities. A detailed comparison of the two platforms, including their respective goals and capabilities, would be beneficial.
2. Scenarios: It would be great to have more details of the available scenarios. For me it is not clear what a scenario means in this context? Is it a different environment (e.g. forest vs. city) or is it similar to CARLA a specific event happening (see https://leaderboard.carla.org/scenarios/)? What are the 22 distinct scenarios available in this simulator? If the authors could provide a list or table of the 22 scenarios, including a brief description of each it would help a lot. The paper should clarify whether scenarios are different environments or specific events. A detailed table or list of the 22 scenarios, including information on the environment type, object density, and any specific challenges, would be valuable.
3. Dataset splits: Figure 2 is great to get a rough overview of the objects but a detailed overview in the supplementary with all available objects and scenes and which are used for which split would be helpful. The paper should include a detailed breakdown of the dataset splits, specifying which objects and scenes are used for training, validation, and testing. This should include information on the number of instances per object and scene, as well as any specific criteria used for splitting the data.
4. Figure 3 (minor): In the image it seems that the front view image is input to the Trajectory completion module but in the text the authors say “it takes the front-view visual token T_img” (line 386). It would be good to have this clearer in the figure. The figure should be updated to accurately reflect the input to the Trajectory Completion module, clearly showing that the front-view image is processed by ViT to generate the visual token. The text should also be consistent with the figure.
5. DAgger: What exactly is the teacher model? Can you provide more details? The paper needs to provide a more detailed explanation of the teacher model used in the DAgger process, including its architecture, how it generates the expert trajectory, and how it interacts with the learning agent.

**W.3. Evaluation/ Benchmark**

1. As I understood for all results an oracle path is necessary to generate the assistants. An additional mode without any assistants would be good to judge how hard the task is and in an ultimate fully autonomous setting this would be the wished setting I assume. The authors state “the inherent complexity and dynamic nature of aerial environments, with obstructed views and shifting perspectives, make basic target descriptions insufficient for UAV” (line 323). I am wondering if temporal input and a memory could help for this making the assistants unnecessary? The paper should include an evaluation of the model's performance without any assistance to establish a baseline for the difficulty of the task. The potential of temporal input and memory mechanisms to reduce the need for assistants should be explored and discussed. This could involve experiments with different memory architectures and input windows.
2. The authors say “UAV trajectories are inherently continuous and difficult to decompose into discrete actions, leading to unrealistic navigation when such simplifications are applied” (line 081). They use (different to previous works) continuous action space. To validate this statement it would be good to have a discrete baseline and qualitative example of the shortcomings (which are solved by the continuous version). The paper should include a discrete action baseline to validate the claim that continuous action spaces are necessary for realistic UAV navigation. A qualitative comparison of the trajectories generated by the discrete and continuous models, highlighting the shortcomings of the discrete approach, would be beneficial.

### Questions
I am not an expert in the field of UAV but after looking at the related work it is still a bit unclear for me what the main contributions are and how it differentiates to existing work. It would be good if the authors could make it clearer what already exists and what is new. Secondly it would be really helpful to include more ablations on the importance of continuous actions or hierarchical predictions.

Minor suggestions/ questions:
1. Make sure that the abbreviations are introduced properly. E.g. line 016 is the first time you mention UAV, it would be good to have the long version when first using the short version.
2. Human baseline: I would be curious how well a human performs in the L3 setting. Is the human baseline with a person who tried it several times and is trained or is it a “zero-shot” baseline?

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
2

### Summary
This paper introduces a UAV-based vision-and-language navigation benchmark built on the CARLA simulator. The simulator offers realistic environments and supports high-DoF control for UAV flight. In addition, the benchmark provides ground-truth human-controlled trajectories, trajectory descriptions summarized by a vision-language model (VLM), and assistive instructions for navigation evaluation. The paper also presents a vision-language model as a baseline for UAV-based vision-and-language navigation, achieving state-of-the-art performance on the proposed benchmark.

### Strengths
This paper is highly comprehensive, including a platform, benchmark and method technique for the VLN task in the domain of UAV. The authors have clearly significant efforts in completing this project.  This benchmark could help researchers investigate realistic UAV control under the task of VLN. Besides, the proposed LLM-based navigation framework shows strong performance among the baseline methods.

### Weaknesses
- This paper includes extensive content on the platform, benchmark, and method, but lacks many important details. For instance, `L398` mentions leveraging DAgger in a closed-loop simulation, yet no further experiments are provided to demonstrate its effectiveness.

- In my view, the L1 assistant (guiding the UAV to the oracle path) provides an oracle instruction by directly issuing ground truth commands, which should significantly enhance navigation performance. However, the experiment results show only a minor increase in SR (such as 16.1 in the full set).

- The visual encoding strategy does not account for historical information, as the navigation method relies solely on the latest frame `L373`, resulting in only 16+1 tokens for encoding visual data. This design neglects navigation history, raising the question of how navigation history can align effectively with the instructions.

- The paper lacks video results to illustrate the ground truth trajectory and the method's performance on this platform. Such visual demonstrations would provide a more intuitive understanding of this benchmark.

### Questions
- Why does the proposed method rely solely on the current observation? How does the model align visual history with the instructions? Additionally, the paper notes the use of `Llama-vid, Vicuna-7B, and EVA-CLIP`, similar to components used in another VLN paper [1]. A discussion comparing these approaches would be beneficial.

- In Tables 2 and 3, the OSR is significantly higher than the SR (almost double). Given the definition of OSR, methods can achieve high OSR by extensively exploring the environment. A discussion or additional experiments are needed to address this observation.

- Why not consider using existing LLM-based methods, such as [2], which employ waypoints in a manner similar to the proposed approach?

[1] Navid: Video-based VLM plans the next step for vision-and-language navigation

[2] NavGPT: Explicit reasoning in vision-and-language navigation with large language models

### Soundness
3

### Presentation
2

### Contribution
3
