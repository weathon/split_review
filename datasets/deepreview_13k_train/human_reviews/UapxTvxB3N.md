# Trajectory-LLM: A Language-based Data Generator for Trajectory Prediction in Autonomous Driving

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Vehicle trajectory prediction is a crucial aspect of autonomous driving, which requires extensive trajectory data to train prediction models to understand the complex, varied, and unpredictable patterns of vehicular interactions. However, acquiring real-world data is expensive, so we advocate using Large Language Models (LLMs) to generate abundant and realistic trajectories of interacting vehicles efficiently. These models rely on textual descriptions of vehicle-to-vehicle interactions on a map to produce the trajectories. We introduce Trajectory-LLM (Traj-LLM), a new approach that takes brief descriptions of vehicular interactions as input and generates corresponding trajectories. Unlike language-based approaches that translate text directly to trajectories, Traj-LLM uses reasonable driving behaviors to align the vehicle trajectories with the text. This results in an "interaction-behavior-trajectory" translation process. We have also created a new dataset, Language-to-Trajectory (L2T), which includes 240K textual descriptions of vehicle interactions and behaviors, each paired with corresponding map topologies and vehicle trajectory segments. By leveraging the L2T dataset, Traj-LLM can adapt interactive trajectories to diverse map topologies. Furthermore, Traj-LLM generates additional data that enhances downstream prediction models, leading to consistent performance improvements across public benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper leverages large language models (LLMs) to generate trajectories for autonomous driving by introducing an interaction-behavior-trajectory translation approach, rather than the commonly used interaction-trajectory translation in other LLM-based methods. Their approach consists of two stages: in the first, vehicle interaction descriptions are translated into behaviors, and in the second, these behaviors are converted into specific motion parameters to create trajectories. Additionally, the authors developed a new Language-to-Trajectory (L2T) dataset. Their method demonstrates promising performance on both the L2T and Waymo Motion Prediction datasets, outperforming state-of-the-art methods.

### Strengths
1. They have published a dataset , Language-to-Trajectory (L2T), which includes 240K textual descriptions of vehicle interactions and behaviours.

### Weaknesses
The clarity of the paper can be improved. In the introduction, the motivation and objectives should be clearly stated, along with a summary of their accomplishments.

It is unclear how the trajectories are generated. Are they based on real data, generated through a simulator, or did the authors develop their own simulator?

The methodology section is difficult to follow and needs rewriting for better clarity.

The paper does not specify what kind of input was used to train the LLM model. Did they use generated prompts, or did they provide feature embeddings?

### Questions
The clarity of the paper can be improved. In the introduction, the motivation and objectives should be clearly stated, along with a summary of their accomplishments.

It is unclear how the trajectories are generated. Are they based on real data, generated through a simulator, or did the authors develop their own simulator?

The methodology section is difficult to follow and needs rewriting for better clarity.

The paper does not specify what kind of input was used to train the LLM model. Did they use generated prompts, or did they provide feature embeddings?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper adopts large language models (LLMs) to generate the trajectories for autonomous driving. In this regard, they explore the interaction-behavior-trajectory translation process in contrast to only interaction-trajectory, which is widely used for other LLMs-based approaches. Their method comprises two stages, where in the first stage, the textual descriptions of vehicle interaction are translated to behaviors, and in the second stage, those behaviors are converted into specific motion parameters for trajectories. Based on this, the authors have also created a new Language-to-Trajectory (L2T) dataset. The proposed method has shown promising results on L2T and the Waymo Motion Prediction datasets compared to state-of-the-art methods.

### Strengths
Here are the strengths of this paper:
1. The inclusion of driving behaviors for trajectory prediction is promising.
2. Another promising aspect of this paper is the creation of a new benchmark dataset, L2T.
3. Overall, the presentation quality of the paper is good. However, some grammatical mistakes can be corrected afterwards.

### Weaknesses
However, the paper has shown better performances in the evaluation, yet some comments need to be addressed:
1. I acknowledge that the authors have put great effort into creating the dataset, but it was unclear whether they have used existing datasets, for instance, Waymo and Nuscenes, to build their dataset. If this is not the case, and they adopt some manual feedback from the driver, how can they evaluate those behavior's annotations? 
2. The authors have experimented with the proposed method in open-loop settings; it would be good to see how the proposed method performs in the closed-loop evaluation. 
3. It is good to see that authors have also dedicated a section in supplementary material for the limitation of their work, but it would be good to see what the future directions will be based on their work. 
4. In the paper, the author has used random locality attention; it would be good to do an ablation study on its effect on driving behavior and also the trajectories. Also, if another form of attention, for instance, cross attention, is used, what will affect behavior and trajectories?

### Questions
However, the paper has shown better performances in the evaluation, yet some comments need to be addressed:
1. I acknowledge that the authors have put great effort into creating the dataset, but it was unclear whether they have used existing datasets, for instance, Waymo and Nuscenes, to build their dataset. If this is not the case, and they adopt some manual feedback from the driver, how can they evaluate those behavior's annotations? 
2. The authors have experimented with the proposed method in open-loop settings; it would be good to see how the proposed method performs in the closed-loop evaluation. 
3. It is good to see that authors have also dedicated a section in supplementary material for the limitation of their work, but it would be good to see what the future directions will be based on their work. 
4. In the paper, the author has used random locality attention; it would be good to do an ablation study on its effect on driving behavior and also the trajectories. Also, if another form of attention, for instance, cross attention, is used, what will affect behavior and trajectories?

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
4

### Summary
This paper introduces Trajectory-LLM (Traj-LLM), which leverages Large Language Models to generate realistic vehicle trajectories from textual descriptions. The method employs an "interaction-behavior-trajectory" process to translate vehicle interactions into trajectories, ensuring the realism and controllability of the trajectories.

### Strengths
* Well-written paper. Easy to follow.
* The proposed "interaction-behavior-trajectory" process to guide the trajectory generation can help ensure better realism and controllability. 
* The author contributed a new dataset L2T.

### Weaknesses
 * The proposed dataset L2T is collected in simulation platform and manually use the wheels to drive and collect the data. The realism of the proposed dataset is questionable. Further justification and motivations are needed for creating a new dataset with good realism instead of curating existing open real-world dataset to create such paired dataset. Specifically, the manual driving process introduces a human bias and may not accurately reflect the complex interactions observed in real-world traffic scenarios. The lack of diversity in driving styles and environmental conditions within the simulation could limit the generalizability of the model trained on this dataset.
* The main benchmark is performed on the proposed L2T and open dataset WOMD is only used in ablation study while  existing literature mainly compared on other open datasets. Without benchmarking on the same open dataset, it would be hard to justify the technical contribution of the proposed model. The absence of a direct comparison with state-of-the-art methods on established benchmarks makes it difficult to assess the true performance gains of the proposed approach. The use of WOMD in ablation studies does not provide sufficient evidence of the model's competitiveness against existing methods.

### Questions
Please see above sections.

### Soundness
3

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
4

### Summary
This paper presents a method for generating vehicle trajectories in various traffic scenarios using large language models, employing a hierarchical generation strategy of 'interaction-behavior-trajectory.' Additionally, this work creates the L2T dataset to train the proposed model. Experimental results show that the motion prediction model trained with the generated data performs better on the mAP metric compared to the model trained solely on WOMD, providing preliminary validation of the method's effectiveness.

### Strengths
1. The paper is well-organized and easy to read.
2. The proposed method may help alleviate the reliance of existing motion prediction models on large amounts of real data, facilitating the development of these models.

### Weaknesses
1. I did not see which specific large language model was used; the only information provided in the system diagram shows the LLM has an encoder-decoder structure, which does not seem to align with GPT-like models. I urge the authors to elaborate on the design of the large language model.
2. As a generative model designed for trajectory prediction tasks, the experimental section is insufficiently thorough. Firstly, it only selects the WOMD dataset and does not test on other representative datasets, such as Argoverse. Secondly, it only uses mAP as the metric, neglecting other common metrics such as distance error and miss rate. Therefore, the generalizability of the proposed method remains questionable.
3. Training a generative model on a third-party dataset and then using the generated data for model training—does this yield effects equivalent to training on the original third-party dataset? I recommend the authors include an ablation study comparing the experimental results of training with the original dataset.

### Questions
1. Can the proposed model be used for simulating traffic scene? I suggest the authors consider this application area, rather than limiting the focus solely to trajectory prediction tasks.

### Soundness
2

### Presentation
2

### Contribution
2
