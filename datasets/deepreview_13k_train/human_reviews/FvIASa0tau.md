# Sitcom-Crafter: A Plot-Driven Human Motion Generation System in 3D Scenes

- Decision: Accept
- Scores: 3, 6, 8

## Abstract
Recent advancements in human motion synthesis have focused on specific types of motions, such as human-scene interaction, locomotion or human-human interaction, however, there is a lack of a unified system capable of generating a diverse combination of motion types. In response, we introduce \textit{Sitcom-Crafter}, a comprehensive and extendable system for human motion generation in 3D space, which can be guided by extensive plot contexts to enhance workflow efficiency for anime and game designers. The system is comprised of eight modules, three of which are dedicated to motion generation, while the remaining five are augmentation modules that ensure consistent fusion of motion sequences and system functionality. Central to the generation modules is our novel 3D scene-aware human-human interaction module, which addresses collision issues by synthesizing implicit 3D Signed Distance Function (SDF) points around motion spaces, thereby minimizing human-scene collisions without additional data collection costs. Complementing this, our locomotion and human-scene interaction modules leverage existing methods to enrich the system's motion generation capabilities. Augmentation modules encompass plot comprehension for command generation, motion synchronization for seamless integration of different motion types, hand pose retrieval to enhance motion realism, motion collision revision to prevent human collisions, and 3D retargeting to ensure visual fidelity. Experimental evaluations validate the system's ability to generate high-quality, diverse, and physically realistic motions, underscoring its potential for advancing creative workflows.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces "Sitcom-Crafter," a system designed for generating two-person human motions in 3D environments, targeting animation and gaming industries. It combines eight modules—three for motion generation and five for augmentation  and address human-scene collisions using an implicit 3D Signed Distance Function (SDF). Evaluation is conducted on Replica dataset and Interhuman dataset to demonstrate its capability.

### Strengths
The modular design targets long-term multi-person motion synthesis in complex 3D scenes.
Utilizes SDF to mitigate human-scene collisions.
Plenty of visualizations are provided in the supplementary, and the code is provided.

### Weaknesses
The system is too complex, with eight different modules, limited improvement over existing methods in each module. Lack of novelty in the core methodology. 
Generated motions often appear unnatural and lack clear interaction, making it difficult to recognize the activities performed by the characters. 
The writing can be improved, the core method is not very clear, but extensive descriptions of various engineering implementations are provided.

### Questions
The contribution of the proposed method to the field seems minimal, primarily due to unclear research question. This paper studies an overly broad task and lack of sufficient novelty in the main approach. It would benefit from a more defined research question and a method to address it effectively.

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
This paper presents a system work which aims to generate the interactions of two persons in a scene from a story-like plot. This is an ambitious goal, which involves a lot of technical challenges, including human motion generation, human-human interaction, human-scene interaction, and long motion synthesis. To approach this goal, this work utilizes multiple prior efforts, e.g., InterGen, GAMMA, DIMOS, Replica, together with some specific designs such as marker-based motion representation, rule-based human-scene-human interaction dataset creation. In addition, LLM is used to parse the plot and produce step-by-step prompt for motion synthesis.

### Strengths
**1. VERY pioneering work in such topic**. This work is targeting an very ambitious yet super challenging task, generating two-person animations in a scene from story script, which used to be a far goal for motion synthesis. Though the results are not perfect, it's a nice and respectful trial as a new form of storytelling, at lease to provide other researchers what we can achieve the best in current stage.   

**2. Challenging tasks and lots of efforts involved**. As aforementioned, the task aimed in this paper involves several technical challenges, including human-human interaction, text2motion synthesis, human-scene interaction, and long motion synthesis. Though each challenge alone is yet to addressed, I can the authors make a lot of efforts to make use of existing advances (e.g., InterGEN, GAMMA, DIMOS, Replica) to complete the whole pipeline, which is not definitely not easy.    

**3. Task-oriented designs**. Some designs are also proposed to address this specific task. For example, the marker based motion representation may help mitigate collision, individual-based canonical motion representation help better network learning, and the self-supervised scene sdf construction is also a nice touch.  

**4. Detailed description of methods**. I appreciate the authors' effort in meticulously elaborate each component of the system. 

**5. Abundant visual results**. In the supplementary video, the authors provide many generation results from plot. Though not perfect, the results are still encouraging provided with the current status for these research directions in the community.

### Weaknesses
 **1. Engineering-driven project**. Though as a pioneering effort, this work is more like a systematical engineering effort, instead of a scientific paper. As said, this system is built on many previous works. Note I am not criticizing engineering efforts. I am a little worried about if it fits well in this conference.   

**2. Unclear how motions are generated**. Though the authors provide detailed description regarding each component, the overall logic of motion generation is not clear. For example, it's still clear to me what pipeline or workflow was passed through to produce two-person interactions in scene by using existing human-human and human-scene interaction models, as well as the locomotion generators.   
 
**3. The overall performance can not be guaranteed**. This is a heavy framework, consisting of eight different modules. The overall performance is relied on the functionality of each module, which is hard to guarantee.

**4. Not easy to reproduce**. This framework is hard to scale in practice. I would prefer to regarding this work as a toy model to demonstrate the possiblity.

### Questions
Overall I believe this paper involves a lot of efforts, and could be interesting to the community. However, I recommend the authors to illustrate more clearly how the interactions are synthesized. Please also look into the weakness section if you can justify any comments that I have made.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
In this work, authors propose Sitcom-Crafter, a comprehensive and thorough framework to generate human motion including scene-awareness and human-human interaction. Recently proposed human motion synthesis methods are focusing on a single problem including 1) text/action driven motion generation, 2) scene-aware motion generation, or 3) human-human interactive motion synthesis. On the other hand, the authors propose to tie the problem into a single task, plot-driven human motion generation.

In general, the authors not only contributed to each single components (e.g., random scene generation, modification of InterGen, ...), but also tie them into a comprehensive framework. In this regard, I believe this will bring a significant contribution to the community and I recommend the acceptance for the paper.

### Strengths
1) This paper (from authors' argument) provides comprehensive and integrated motion generation with the understanding of static scene and human-human interaction. 

2) Their modification to the InterGen (Liang et al.,) makes sense, especially the normalization of the character motion seems reasonable.

3) Without cost expensive data collection, they introduced the synthetic scene generation technique to leverage the existing human-human interaction pipeline to train their integrated system.

4) The proposed motion synthesis framework can take long description as a plot.

5) Well written and great visualization is appreciated.

### Weaknesses
I don't think the random generation of the object is sufficient for the generative model to learn richer context of human behavior. To elaborate, our interactions with the scene and other people are complex and entangled. For example, two people sitting on sofa and talking each other are entangled interactions with human–scene and human–human. In this paper, if I understand correctly, the paper mainly focuses on obstacle avoidance while maintaining human–human interaction, which still limits its applicability to the real-world plots. I would like authors to share their opinion on this point and if agreed, I would suggest to mention as their limitation in the paper.

### Questions
-

### Soundness
3

### Presentation
4

### Contribution
4
