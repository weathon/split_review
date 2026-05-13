# SceneFunctioner: Tailoring Large Language Model for Function-Oriented Interactive Scene Synthesis

- Decision: Reject
- Scores: 1, 3, 8, 8

## Abstract
With the Large Language Model (LLM) skyrocketing in recent years, an increasing body of research has focused on leveraging these models for 3D scene synthesis. However, most existing works do not emphasize homeowner's functional preferences, often resulting in scenes that are logically arranged but fall short of serving practical functions. To address this gap, we introduce SceneFunctioner, an interactive scene synthesis framework that tailors the LLM to prioritize functional requirements. The framework is interactive, enabling users to select functions and room shapes. SceneFunctioner first distributes these selected functions into separate areas called zones and determines the furniture for each zone. It then organizes the furniture into groups before arranging them within their respective zones to complete the scene design. Quantitative analyses and user studies showcase our framework’s state-of-the-art performance in terms of both design quality and functional consistency with the user input.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper introduces SceneFunctioner, an interactive framework that leverages GPT-4o for function-oriented 3D indoor scene synthesis, addressing the gap in user-specific, practical room designs. Unlike existing methods, it focuses on distributing user-selected functions into distinct zones and organizing furniture to align with these functional requirements while preventing common issues like object collisions and logical inconsistencies. The framework follows a structured three-step process—deciding zones, forming furniture groups, and arranging them within zones—supplemented by robust postprocessing and feedback mechanisms. The main contributions include a structured approach to function-oriented scene synthesis, the introduction of zones to manage complexity, and iterative verification steps to ensure collision-free, practical designs that align with user inputs.

### Strengths
The strengths of the paper include its approach to integrating function-oriented design in 3D scene synthesis, ensuring that generated layouts align with user-specified functional needs. It introduces a multi-step process involving zone-based division and iterative postprocessing checks to prevent furniture collisions and logical inconsistencies. The framework’s use of GPT-4o demonstrates strong LLM capabilities, effectively balancing user input with practical design outcomes. Additionally, its feedback loop ensures error correction and refinement, resulting in high-quality, customized scene synthesis with enhanced user interaction and reduced design time.

### Weaknesses
This paper reads more like a technical report of a user application and prompt engineering rather than addressing fundamental research problems.

The proposed solution also seems tentative, as demonstrated by several limitations:
- Limited zone shapes: Restricted to rectangular zones and room shapes, reducing flexibility for complex layouts.
- Zone border inconsistencies: Does not account for relationships between adjacent zones, potentially causing pathway issues.
- Generation inefficiencies: Requires multiple retries due to LLM errors, increasing overall generation time.
- Not considering floor plan structures: Overlooks the placement of doors and windows, which can significantly affect the usability of the generated scenes.

The paper tackles a niche problem that may not resonate with a broad ICLR audience.

The use of GPT, a closed-source model, means the solutions are less reliable and more tentative due to the lack of understanding and access to the model’s workings.

The spatial understanding of LLMs has been extensively studied in prior research, and this paper does not provide new insights that could inspire or motivate future work in this area.

### Questions
NA

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Given a list of user-specified scene functions and a room shape, the paper proposes an
interactive framework based on LLMs to synthesize a scene that adheres to the given scene
functionalities.

The main gaps identified in the literature that motivates this work are: (a) scene generation methods that are functionality-unaware, focusing only on object relations, and (b) LLMs requiring contextual information to generate functionally-aware scenes.

This work presents an interactive, human-in-the-loop scene generation method, with user-specified functionalities and room shapes. The proposed method can be divided into three stages: (1) dividing a scene into “zones” based on user selected functionalities, (2) organize furniture for each “zone” into groups, and (3) placing furniture at the right orientation at an appropriate location. In every stage, there exists a verification and feedback mechanism to address potential issues arising out of LLM errors. This feedback mechanism from the humans makes the approach more reliable despite using LLMs. In terms of quantitative evaluations, four different measures are recorded. They are: (1) Generation support: a binary indicator that tells whether the framework allows support for irregular shape and user control, (2) Percentage of invalid objects that are out of bound or collide with other objects, (3) CLIP-score that measures how well the generated scene aligns with given input, and (4) Overall scene quality measured in terms of functionality, practicality and aesthetics
judged by GPT. For comparison, the paper looks at LayoutGPT (NeurIPS 2023) and I-Design (arXiv 2024), both of which do not incorporate human feedback.

To summarize again, the input is a set of user-specified scene functionalities, scene shape. The output is a scene populated with furniture. The dataset used in ObjaVerse. The LLM chosen here is GPT-4o.  There is no learning mechanism involved (i.e., no training  step involved) as the paper proposes a better way to prompt LLM by dividing the task of scene synthesis into aforementioned three steps, instead of a single one.

### Strengths
* Well-written paper

* Dividing the scene synthesis task into three stages to make things relatively easy for LLM is an interesting way to stabilize LLMs for complex tasks in 3D

* The second user study shows that the proposed framework is beneficial to the designers.

### Weaknesses
 * The only contribution is a stepwise human-in-the-loop prompting technique to use an LLM (GPT-4o)
for scene synthesis. Such a framework does not necessarily address the issue of generating functionally plausible and usable 3D scenes. While there are some merits to the study in the paper in terms of helping LLMs adapt to 3D scene generation tasks,  the overall impact and utility is limited.

* In addition, the experiments presented in the paper are performed on a small dataset (500 scenes) that is manually generated for this framework.

Overall, the paper proposes a step-wise LLM prompting strategy for scene synthesis. The idea is
interesting but lacks technical contribution.

### Questions
* Did the users have a pool of scene functions to choose from? If not, the presented approach is going to see high input-entropy. How does the LLM handle that? If yes, how many total number of scene functions are provided to the users to choose from?  I do see in Line 366 which mentions that each scene is configured with randomly selected 6 functions. From how many available functions are these chosen from?

* Were there any quantitative metrics used to verify/validate the correctness of scenes generated at each *stage*? For example, zone allocation accuracy for stage 1, furniture grouping coherence for stage 2, and placement accuracy for stage 3. Such a quantitative evaluation for every stage can potentially provide more insights into the framework on where things are better/worse.

* Finetuned LLMs have shown to provide good generalization capability. Current framework uses the GPT-4o LLM as is. It would be interesting to see the results when the LLM is finetuned for scene synthesis task and then used to synthesize a new scene. I was actually hoping to see some sort of finetuning, foloowed by an contextual analysis. That would have been more interesting.

* The paper uses the words “scene” and “room” interchangeably. Is the method proposed in paper for individual room synthesis or scene-level (entire house) synthesis? Please adhere to one convention: either use scene or room everywhere. Better yet, good to provide a clarifying statement in the Intro and/or methodology section about this.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces SceneFunctioner, a function-oriented scene synthesis framework that allows users to decide on room functions and room shape. The three-stage framework employs LLMs at each stage, which first divides the scene into zones containing the furniture for one or more functions. The second stage further divides the furniture within each zone into groups and constructs a graph for relations within each group. The last step places the groups within each zone to complete the layout. Quantitative results and user studies prove the effectiveness of the proposed approach.

### Strengths
a) The overall idea of coarse-to-fine scene synthesis strategy is interesting and novel. b) Scene synthesis based on room functions yields plausible and realistic object arrangements. c) The interactive scene synthesis framework allows users to design customized spaces with ease. d) The visual results look good.

### Weaknesses
a) In L231-232, the author mentions appending sample inputs and outputs to the context. How are these samples selected/formed? LayoutGPT selects the closest samples for in-context learning using room dimensions & type for generating random layouts of specific room types. However, synthesizing scenes based on room functions is a more specific task than generating random plausible layouts. Therefore, for a fair comparison, I suggest providing LayoutGPT with in-context samples that are closest in terms of room functions. Specifically, a distance metric should be defined based on the functional similarity of the rooms, rather than just room dimensions and type. This would require a method for quantifying the functional aspects of a room, which is not explicitly addressed in the paper. b) The author mentions that the wrong results produced by LLMs increase the retries and the overall generation time. I am curious about the quantitative analysis of the feedback mechanism. How much time do the retries take when compared to the actual generation time? How many retries are required on average per-stage? It would be beneficial to understand the computational overhead of the feedback loop and its impact on the overall efficiency of the framework. c) While the paper presents intriguing qualitative results, it would be interesting to see how the method performs on larger rooms (dimensions more than 5 meters) or smaller rooms, different room types (such as bedrooms) to better evaluate the method's generalizibility. The current evaluation seems limited to a specific range of room sizes and types, and expanding this would strengthen the claims of the method's robustness.

### Questions
All of my questions are listed in the weaknesses section, and I may adjust the rating if they are well addressed.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces a novel approach for the interactive synthesis of 3D scenes, called SceneFunctioner. The framework allows users to sketch rooms and to define functional zones. Given the user input, an LLM is used to generate furniture layouts for each zone based on a three-step generation process (zone creation, local furniture grouping, and final arrangement). A feedback mechanism is used to manage potential LLM errors that may occur during the generation process (e.g. incorrect formatting, object collision, etc,). The paper discusses quantitative results and provides user studies that show that SceneFunctioner outperforms previous approaches.

### Strengths
- The three-step generation process (zoning, local grouping, and final arrangement) and the introduced feedback mechanisms for the LLMs are novel and interesting.
- The approach focuses on room functions, which is not addressed by other  approaches. 
- The conducted user studies seem reasonable and validate the effectiveness of SceneFunctioner. 
- The paper is well-written and easy to follow.

### Weaknesses
 - I appreciate the conducted user study, however the validation of the approach appears to be more on the lightweight side.
- While the use of zones seems to generate interesting results, it is unclear if the zones can be easily adapted for more complex concepts and layouts (e.g. mixed-use spaces).
- The current approach does not consider the aesthetics of the generated furniture layouts (which has also been highlighted as limitation).

### Questions
- How does SceneFunctioner handle function conflicts in multi-functional zones?
- How would an LLM perform better for irregular room layouts (e.g. how would it need to be trained to achieve better performance)? 
- How would this framework adapt to advancements in LLM capabilities (e.g. what features would be required to improve upon the current results)? 
- How adaptable is SceneFunctioner to user feedback after an initial scene is generated (if a user wants minor adjustments, would the framework require a complete re-synthesis)?
- Is there any limitations regarding the number of different zones? E.g. could SceneFunctioner easily be extended to also cover outdoor spaces?
- The authors may want to also consider the following work as part of their related work discussion: R. Ma, A. Gadi Patil, M. Fisher, M. Li, S. Pirk, B.-S. Hua, S.-K. Yeung, X. Tong, L. Guibas, H. Zhang, Language-Driven Synthesis of 3D Scenes from Scene Databases, ACM Transactions on Graphics (Proceedings of SIGGRAPH Asia), 2018

### Soundness
3

### Presentation
3

### Contribution
3
