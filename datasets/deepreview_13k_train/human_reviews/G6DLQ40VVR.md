# DivScene: Benchmarking LVLMs for Object Navigation with Diverse Scenes and Objects

- Decision: Reject
- Scores: 8, 6, 5, 6

## Abstract
Object navigation in unknown environments is crucial for deploying embodied agents in real-world applications.
While we have witnessed huge progress due to large-scale scene datasets, faster simulators, and stronger models, previous studies mainly focus on limited scene types and target objects. In this paper, we study a new task of navigating to diverse target objects in a large number of scene types. To benchmark the problem, we present a large-scale scene dataset, \scenedataname, which contains 4,614 scenes across 81 different types. With the dataset, we build an end-to-end embodied agent, \modelname, by fine-tuning a Large Vision Language Model (LVLM) through imitation learning. The LVLM is trained to take previous observations from the environment and generate the next actions. We also introduce CoT explanation traces of the action prediction for better performance when tuning LVLMs. Our extensive experiments find that we can build a performant LVLM-based agent through imitation learning on the shortest paths constructed by a BFS planner without any human supervision. Our agent achieves a success rate that surpasses GPT-4o by over 20\%. Meanwhile, we carry out various analyses showing the generalization ability of our agent.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
his paper tackles the challenge of object navigation in varied environments by introducing DIVSCENE, a dataset with over 4,600 scenes across 81 types. Building on this, the authors developed NATVLM, a navigation agent fine-tuned on a large vision-language model. NATVLM uses Chain of Thought reasoning to help it understand navigation steps better, which improves its accuracy and generalization in diverse settings. The experiments show strong performance against other models and confirm the agent's adaptability across different datasets.

### Strengths
1. This paper introduces the DIVSCENE dataset, which is a substantial addition to the field of embodied AI. Unlike existing datasets that are often limited to a narrow range of scenes or objects, DIVSCENE covers 81 diverse scene types with over 22,000 object types, enhancing the scope for studying generalizable object navigation.
2. The method is rigorous, with extensive experiments that include comparisons to baseline models (both open-source and closed-source) and ablation studies to evaluate the impact of CoT reasoning. The experiments provide solid evidence that NATVLM significantly outperforms existing methods in diverse navigation scenarios.
3. The paper is well-organized and presents the main ideas in a clear and logical structure.

### Weaknesses
 1. While DIVSCENE provides a broad range of synthetic environments, the reliance on simulated platforms (like AI2THOR) limits the real-world applicability of NATVLM. Simulated environments often lack the unpredictable variability and physical constraints found in real-world scenarios. Expanding experiments to include real-world datasets or environments would strengthen the evidence for the model’s generalization abilities and applicability. Including a discussion on the challenges of transferring synthetic-trained models to real-world settings would also be beneficial.
 2.  The manual creation of CoT explanation traces for training NATVLM may limit scalability and automation in more complex or dynamic environments. The process of manually generating these traces is not only labor-intensive but also introduces a potential bottleneck in adapting the model to new scenarios or scaling it to larger datasets. This reliance on manual annotation could hinder the model's ability to generalize to unseen environments where such detailed, human-provided explanations are unavailable.
 3. While DIVSCENE offers diverse scenes and objects, the paper lacks a detailed analysis of the scene complexity and its impact on navigation performance. For example, understanding how NATVLM performs in cluttered versus minimal scenes, or in spaces with varying levels of visual occlusion, would add depth to the evaluation. Such insights could help clarify the scenarios where NATVLM’s CoT-based reasoning is most beneficial and identify cases where additional model improvements may be needed. The absence of a quantitative measure of scene complexity makes it difficult to assess the robustness of the proposed approach across different environments.
 4. Although the paper emphasizes the effectiveness of NATVLM, it does not address the computational cost of training and deploying the model, especially given the integration of large-scale LVLMs and manually designed CoT traces. Providing a comparison of training and inference times with baseline models would offer readers a clearer understanding of the model’s practicality. The lack of information regarding the hardware requirements and energy consumption further limits the assessment of the model's feasibility for real-world applications.

### Questions
Please refer to the weaknesses section.

### Soundness
4

### Presentation
3

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
The authors present an open-vocab version of the closed-vocab object navigation. They introduce both a benchmark dataset for this setting, and demonstrate a new VLM-based method (NatVLM).


Benchmark:
* They generate 4k scenes using Holodeck, and aim for diverse generated scenes by using 81 scene types from MIT 365 along with LLMs to generate scene descriptions. They use 22k objects from Objaverse (looks like they subselect 5k somehow).
* They use AI2Thor to compute shortest paths and compute episodes for trianing. Presumably they also use aI2Thor for online evaluation

Baselines:
They present a few baselines, using existing vlms and a method NATVLM  (a finetuned idefics2). They show a few ablations of prompts in the NatVLM baseline. They show zero-shot transfer performance of these baselines on closed-vocab versions ProcThor and iThor.

### Strengths
### Significance
Open-vocab version of existing closed-vocab object nav. Reasonably important problem with a large enough community that would be interested in this benchmark. 

### Originality
Seems sufficiently novel

### Quality
The authors do a good job of introducing a benchmark using existing tools in the community. They provide results for some reasonable baselines on this new benchmark, and show zero-shot performance on closed-vocab scenes (but still in procthor). Generally they do a very good job describing experimental settings, though some details are missing from the paper -- but would be present in a code release. E.g. which episodes were used for eval on procthor, ithor. The extensive appendix helps here.

### Clarity
Good references to related work, motivation is clear

### Weaknesses
My main concern is that the paper does too many things for these experiments to sufficiently support. It reads like a task paper, and a dataset paper, and also a method paper.

1. As a method paper, the submission is missing comparisons to sota on closed-vocab benchmarks (e.g. sota in procthor, or on MP3D in habitat).
2. As a dataset paper: the submission could use more analysis of well these scenes approximate real-world settings -- should we use/trust this data
3. As primarily proposing the task of open-vocab object nav: I would like to see more of a breakdown of where current methods fail, and why this problem is hard

### Questions
### As a method:
- In this case the paper would be a method for open-vocab object navigation, where they generate a dataset for the proposed method. But for an open-vocab method, I want to be able to compare its performance to SotA on existing object nav benchmarks, even if they are closed vocab. Only comparisons are to other VLM-based methods, which are not SotA on existing benchmarks. 
- You don't need to be the best in closed-vocab objnav. It's okay to break out the open-vocab and closed-vocab results separately in a table. But it would be helpful to show the reader how big the gap is. If there's a large gap, that's an even better motivation of why closed-vocab approaches do not work in real-world settings.
- If you do want to be the best on closed-vocab objnav, you don't need to show zero-shot performance but can finetune/anneal the model on the downstream dataset. Does the more general open-vocab object nav help them improve over sota?

### As a task: 
No breakdown on where the failures were. Why is open-vocab much harder than closed-vocab? E.g. how many of the failures were due to missing the object, vs navigation failure. That would allow this to tie into existing literature like 3d object detection (e.g. on scannet, mp3d, etc).

### As a benchmark dataset
I would like to see more analysis of the decisions made for this benchmark, and how well models trained on this data transfer to real-wold settings. 
* Existing zero-shot transfer experiments are to other benchmarks also in AI2Thor. So largely this concerns whether the model will work in other ai2thor scenes from procthor/ithor, and using those closed-vocab objects instead of the ones from objaverse
* I would love to see generalization to some obj nav in other simulators and using more real-world data (e.g. ARKit or MP3D, which the authors mention but do not compare to).
* Is generating new scenes Holodeck better than using an existing artist-deigned dataset like Structure3d, which has 3.5k scenes? ARKit which is 4500 real ones and already has a bunch of CAD annotations with cad-estate?
* Is 4k scenes the right number?  Would want to see an experiment when training on subsets of the data to show performance isn't saturating (e.g. 1%, 10%, 50%, 100% of scenes).

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces a new dataset with diverse objects and scenes. The scenes are generated using Holodeck, and the trajectories are collected following the shortest path principle. The dataset contains 4,614 scenes across 81 distinct types. It also provides ground-truth actions along with explanation traces to support Chain-of-Thought (CoT) reasoning. The experimental results demonstrate the effectiveness of these explanation traces in enhancing model performance.

### Strengths
1. The paper demonstrates that explanation traces are important for action prediction, providing useful insight for model design.
2. The authors utilize a postprocessing procedure to guarantee the data quality.
3. The authors provide the data examples and the source code of open-sourced API evaluation.

### Weaknesses
1. Overclaim. The authors claim that they are the first to build a navigational agent based on LVLMs. However, to my knowledge, NaVid [1] has already introduced a navigation agent using LVLMs and deployed the model in real-world scenarios. In contrast, the current work operates entirely within synthetic scenes and trains its model on a single simulator, which limits the novelty and practical significance. This weakens the overall contribution, as the work does not extend beyond what NaVid achieved.

2. Missing Comparison with Existing Navigation Datasets. The manuscript lacks a proper comparison with existing navigation datasets. It is essential to clarify how this dataset differs from previous datasets in terms of data domain, quantity, and quality. Important details such as the number of scenes, object categories, and trajectory complexity in existing datasets should be explicitly mentioned. Without this information, it is challenging to assess the uniqueness or relevance of the proposed dataset.

3. Limited Technical Contribution. Sections 3, 4, and 5 primarily describe a standard pipeline for collecting navigation trajectories, which follows established methodologies from prior works. The paper should make a clearer distinction regarding its unique contributions in these sections to better articulate the novelty. Without this, the technical advancements of the current work appear minimal.

4. Insufficient Baseline Models and Ablation Study. The experimental section is limited, as the authors train only a single model based on Idefics 2 (8B) and compare it with zero-shot models. This narrow focus prevents a thorough evaluation. Including additional baselines, such as traditional reinforcement learning (RL)-based or imitation learning-based navigation models, would provide a more comprehensive comparison. Furthermore, the influence of different LLM backbones or LVLM pre-trained weights should be studied to offer deeper insights into how these components affect navigation performance.

### Questions
1. Zero-shot transfer experiments are not convincing. I visualize the scenes in iTHOR, ProcTHOR, and AI2-THOR and find their styles are very similar, which means a marginal domain gap in your cross-domain setting. So comparing zero-shot models such as llava and qwen-VL with your fine-tuned models makes no sense. A more valuable comparison should be the in-domain experiments on iTHOR and ProcTHOR with your NATVLM.

2. Insufficient Literature Review on Object Navigation. The manuscript does not adequately cover prior research on object navigation, particularly recent works that explore navigation agents built with Vision-Language Models (VLMs). A comprehensive discussion of related works is essential for positioning this study within the existing literature. The omission of relevant research leaves a gap in understanding how the proposed approach compares to prior VLM-based navigation agents and whether it builds on or diverges from previous methodologies.

[1] VLM-Social-Nav: Socially Aware Robot Navigation through Scoring using Vision-Language Models
[2] NaVid: Video-based VLM Plans the Next Step for Vision-and-Language Navigation

### Soundness
2

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
5

### Summary
This paper presents a new benchmark for object-goal navigation as well as a LVLM-based baseline method. For data generation, this work adopts GPT-4 to generate diverse scene data and samples episodes accordingly. Then NatVLM is proposed as a baseline method, which tunes a LVLM using chain-of-thought. The authors compare NatVLM with other LLM or LVLM navigation methods on the proposed benchmark and demonstrates leading performance.

### Strengths
1. This paper is easy to follow.
2. DivScene contains a large amount of houses of different types and object categories, which can serve as a good evaluation benchmark for open-vocabulary object navigaion.

### Weaknesses
Although the proposed dataset is diverse, the experimental comparison is weak:
The authors claim in L68-73 "However, they still face a substantial domain gap between navigation tasks and the LLM training corpus (Lin et al., 2024). Moreover, those methods (Chen et al., 2023; Zhu et al., 2024) require a captioning model to generate textual descriptions of each scene, serving as the perception of the backbone LLMs. The captioning model might miss crucial information about objects and lead to suboptimal results, like spatial or color details.". If this is true, the authors should compare with state-of-the-art open-vocabulary object navigation methods [1,2,3] to validate this. Otherwise, only comparing with LLM and LVLMs are less meaningful.

Also, some details about the dataset need to be further clarified:
1. How does the objects arranged in the scenes? How to make sure their relationship is reasonable?
2. How to define scene type and what is the criteria for choosing them?

Moreover, the whole approach, including data generation and NatVLM, is too naive. There are many ways to exploit the ability of LLM/LVLMs for navigation [1,2,3] and a thorough comparison is required.

Typos:
Line 259: Similarly, we randomly select 27 houses from distinct scene types as the validation set. (validation-->test)

### Questions
See weakness. I hope my questions can be well addressed and more experimental results are required to support the authors' claim.

### Soundness
2

### Presentation
3

### Contribution
2
