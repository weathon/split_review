# Re-Aligning Language to Visual Objects with an Agentic Workflow

- Decision: Accept
- Scores: 6, 5, 5, 6

## Abstract
Language-based object detection (LOD) aims to align visual objects with language expressions. A large amount of paired data is utilized to improve LOD model generalizations. During the training process, recent studies leverage vision-language models (VLMs) to automatically generate human-like expressions for visual objects, facilitating training data scaling up. In this process, we observe that VLM hallucinations bring inaccurate object descriptions (e.g., object name, color, and shape) to deteriorate VL alignment quality. To reduce VLM hallucinations, we propose an agentic workflow controlled by an LLM to re-align language to visual objects via adaptively adjusting image and text prompts. We name this workflow Real-LOD, which includes planning, tool use, and reflection steps. Given an image with detected objects and VLM raw language expressions, Real-LOD reasons its state automatically and arranges action based on our neural symbolic designs (i.e., planning). The action will adaptively adjust the image and text prompts and send them to VLMs for object re-description (i.e., tool use). Then, we use another LLM to analyze these refined expressions for feedback. These steps are conducted in a cyclic form to gradually improve language descriptions for re-aligning to visual objects. We construct a dataset that contains a tiny amount of 0.18M images with re-aligned language expression and train a prevalent LOD model to surpass existing LOD methods by around 50% on the standard benchmarks. Our Real-LOD workflow, with automatic VL refinement, reveals a potential to preserve data quality along with scaling up data quantity, which further improves LOD performance from a data-alignment perspective.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents an agentic approach to improving text-image data for language-based object detection. The agent has access to tools (LLMs and VLMs) and performs planning and reflection steps. The proposed agentic pipeline is used to re-align text-image data and train a model that significantly outperforms prior works.

### Strengths
1. The proposed data filtering and processing mechanism improves the data, and leads to better models
2. The method is evaluated on several datasets and the improvements are consistent
3. The method relies on open-source LLMs and VLMs, and the prompts used have been provided, so the work could be reproduced

### Weaknesses
1. The agent has access to a variety of actions to choose from (from the states it can be) and there is some intuition that the 6 mis-alignment reasons (category, attribute, etc) will each be beneficial for some of these failure modes. It would be good to see if the used actions and tools actually reflects that intuition with some analysis on which actions were chosen when different mistakes were made
2. Further to the previous point, the agentic pipeline as is now has quite a lot of components. It might be very beneficial if any of them can be removed without significant loss in performance.
3. The paper several times mentions the model trained is a "prevalent" model -- can this be backed up with other works that use the same model? Comparing to these more explicitly would make the contribution of this work stronger
4. The training of the agent is not properly explained. Some things that should be there are 1) how many samples were used to train the agent? It says that these were manually created by the authors using the outputs of the various tools. Did this include all the recurrent steps?

Minor: Section 4.1 introduces forms A,B,C which are then not references in the table and is a bit confusing

### Questions
-

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
The authors of this paper propose a method for improving the quality of text descriptions used for training language-based object detection (LOD) models. As done in prior work, in the first step, they use a vision-language model with language generation capabilities (LLava in their case) to generate text descriptions for objects.

Their main contribution is a multi-step iterative method for improving the generated descriptions for each object. The authors do a manual analysis and define six different problems that can occur for each description.  They group these problems into three categories (referred to as states) and pre-define an action for each problem (e.g., if the attributes in the description are not correct, crop the image and generate a new description).

In each iteration of their method, a fine-tuned unimodal LLM (i.e., their agent) inspects the description and decides if the description is good enough or needs further modification. If further modification is needed, the agent selects one of the three predefined states (i.e., types of problems) and suggests taking the corresponding action to refine the description or generate a new one.
Once the action is complete, the authors use another LLM to reflect on the output of the executed action. Although it is not entirely clear in the paper how it is accomplished, the results of the reflection process are integrated into the next iteration to further improve the newly generated or updated object description. The authors repeat the iterations for each description for a certain number of steps or terminate the loop if the agent decides the description is good enough and no further modification is needed.

### Strengths
* The idea that several models work together to collectively improve the quality of the training data is very interesting and could be potentially useful for other applications as well.
* The authors follow a reasonable design process to develop their method. For example, they define the set of states and corresponding actions based on the analysis of the existing data.
* The authors ask the right questions when evaluating their method. For example, they attempt to study the importance of correctly choosing the state/actions for each description. They also try to isolate the impact of higher-quality data from the original data that they are using (paragraph 2 of Section 4.1).

### Weaknesses
I have two major concerns about this work. Although the idea is interesting, and the authors have come up with the correct questions, the quality of the writing and experimental setup can be improved significanlty.

**Writing:**

The paper is not well written and is hard to understand. It takes a couple of passes to understand the arguments. There are also a lot of ambiguities that need further clarification. Here are some examples:
* Second paragraph of section 3.1: Since the authors are generating the initial training data for LOD (that they will later re-align with Real-LOD) and not using the data that is out there from previous work, the setup and how the data generation is accomplished should be clearly explained. The authors just mentioned the name of the model they use.
  * For the initial expression generation with LLava, the authors should clearly state the prompts used, formatting structure, number of expressions generated, etc.
  * The authors also mention, “vicuna is used to diversify the generated descriptions”. What does “diversify” mean in this context? How exactly is it done, given the generated data?
* Since the authors are fine-tuning “ChatGLM-6B” as their agent (which is responsible for choosing the state and action to be executed), it seems like the agent does not have access to the image, and it reasons only based on the textual prompts. However, the figures and texts give the impression that the image is also used as input to the agent to choose the state/action. This should be clearly stated in the text that the agent does not have access to the image.
  * Also related, it seems like the agent does not use the bounding box location either. This should also be clarified.
* Line 260: Vague statement: “When using these models, Real-LOD agent adaptively modulates visual content and text prompts based on its reasoning thoughts”. It is not clear which aspect of the agent this statement is referring to.
* How is the output of the reflector incorporated in the next iteration of Real-LOD? If, in the next iteration, the agent decides that no further modification is needed, is the reflector output not used?
* The authors should discuss the expected behavior of the planner in more detail in the main text. For example, does it format the questions (i.e., prompts) that are used with other tools (i.e., LLM and VLM) in free form, or is it expected to follow specific guidelines/templates for generating the prompts?
* Section 3.3 needs more organization. The authors should clearly separate the analysis process, the statistics of the created data for training real-LOD-agent, and the analytical experiment to test the quality of the generated data.
* Line 340: SigLip filtering here seems to be different from the one explained in Line 197. It is not clear what is being filtered here and how the filtering is accomplished.
* Line 341: “Each input data contains the object category label, raw expression, and reasoning from LLM.” what reasoning from LLM? How is it generated? My impression is that this is the input to train the agent. So, we do not have the agent yet to get the reasoning as explained in other parts of the paper. So, this step should be further clarified.
* Line 341-342: “Then, we manually set the state/action and collect responses as the outputs.” Is the manual annotation done for all 15k input samples? If yes, it should be reported who has done the labeling (i.e., authors themselves or mechanical Turk, etc.), and the details of the instructions given to labelers should be provided.
* Line 350: “We randomly select hundreds of filtered expressions and manually check each for a detailed observation”. This is an important detail of the analysis. “Hundreds” should be quantified with exact numbers.
* Line 379: “we find that the success rate is 74.7% v.s. 35.6%.” these numbers and the experimental setup used to achieve these are not clear.
* it is mentioned in the abstract that the method results in "50% improvement". Does it mean that the proposed method improved the performance by 50 percentage points? that does not seem to be the case in the experiments.
* It is also more informative if the authors report the average improvement rather the maximum.

**Minor suggestions:**

* It might be easier to understand if section 3.3 (DATA ANALYSIS OF LANGUAGE AND VISUAL OBJECTS) comes before section 3.2 (AGENTIC WORKFLOWS FOR LANGUAGE EXPRESSION RE-ALIGNMENT)
* Similarly, it might be helpful to have section 4.2 ( COMPARISONS WITH STATE-OF-THE-ART LOD METHODS) before section 4.1 (ABLATION STUDY)

**Experiments**

* The authors claim significant boosts in performance but the experiments are very limited (only three datasets). More extensive experiments are needed to show the merits of the proposed method.
* For section 3.3, although authors have done the analysis that shows choosing states and actions by their agent achieves better performance than random selection of states/actions. It is important to also report the accuracy of the agent in choosing the corresponding state/action for each input sample. 
* Correct me if I am wrong, but it seems like the agent is only trained on data built from Objects365. It would be interesting to evaluate the model on Objects365 dataset exclusively to analyze how transferable the agent is to other datasets. Although object365 is included in Omnilabel but exclusive numbers for Objects365 help better understand the impact of distribution shift from training to inference.

I also have some questions about the design choices: 
* Why use an LLM as the agent when the input contains both image and text? Isn’t a language-generative VLM a better choice?
* Similarly, in state2/action2, why use an LLM to write a new object description based on the existing caption rather than using a VLM to write the description based on both the image and the caption?

### Questions
Please see the weaknesses.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper aims at the language-based object detection task that detect visual objects based on language queries. Since previous vision-language models (VLMs) may face the hallucination challenge, authors present an agentic workflow based on an LLM to re-align the language query and visual objects. The workflow contains three main steps: planning, tool use, and reflection. Some evaluation results on some benchmarks show the performance comparison.

### Strengths
Figure and tables are clear. Many figures and tables are used to present the language expressions and evaluation results.

A state-of-the-art method mm-GDINO (Zhao et al., 2024) is used for performance comparison.

In Figure 5, the detail of how the presented Real-LOD method re-aligns one raw language query to given image is clear. Figure 5 can help reader understand the model implementation.

Ablation study on the Omnilabel dataset is conducted for model anaysis.

### Weaknesses
Authors use an agentic workflow controlled by an LLM to reduce VLM hallucinations. However, there is still hallucinations in the LLM. In fact, hallucinations are not effectively reduced.

The general LOD framework in Figure 3 is very common. Thus, I have concern about the technological novelty of the presented method.

In Section 3.2, there are "Right" state and "Wrong". How to judge whether he is truly right or wrong, rather than the hallucinations from the LLM?

The works seems to directly use the LLM and VLM. There is no real innovation for both LLM and VLM.

### Questions
I hope that authors can address our questions and concerns in Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper begins by explaining that directly using vision-language models (VLMs) for re-captioning target regions can lead to hallucinations, highlighting that VLMs alone may not be suitable for training data optimization. To address this, the authors propose an Agent Workflow (Real-LOD) to improve training sets for open-set object detection, which consists of Planning, Tool Usage, and Reflection stages. This workflow combines the reasoning ability of LLM (ChatGLM-6B) and the perception ability of VLM (LLaVAv1.6-34B) to effectively correct inaccurate object descriptions within the training dataset.  The authors then re-train an open-set object detector based on the Swin-B backbone using the re-aligned dataset. This detector performs well across multiple open-set detection benchmarks, including the new challenging OmniLabel benchmark. Extensive ablation studies on these benchmarks further validate the effectiveness of each step in the data refinement process.

### Strengths
1. **Innovative Data Optimization Method**: The proposed Agent Workflow offers an innovative approach to training data refinement by employing multi-step processes—namely, Planning, Tool Usage, and Reflection—to mitigate hallucinations generated by Vision-Language Models (VLMs) and enhance data quality.

2. **Demonstrated Effectiveness in Experiments**: The retrained open-set object detector achieves strong performance across challenging benchmarks, including OminLabel, underscoring the practical efficacy of this approach.

3. **Relatively Comprehensive Ablation Studies**: The paper includes extensive ablation studies that validate the necessity and contribution of each step within the Agent Workflow, providing robust empirical support and reinforcing the reliability of the study.

4. **Clear and Informative Visualizations**: The figures are well-designed, effectively illustrating the issues with VLMs and detailing the steps within the Agent Workflow, enhancing reader understanding of the methodology.

### Weaknesses
1. **Choice of VLM**: The authors use the commonly utilized large-parameter version of VLM (LLaVAv1.6-34B). However, several newer Controllable VLMs / MLLM / Captioner allow interaction through a variety of visual prompts (such as Points, Boxes, and Masks) to obtain more focused descriptions for target regions. Directly using these controllable VLMs may have fewer hallucinations on region caption task and may be better than LLaVAv1.6-34B with region cropping. Examples Region Controllable VLMs include: AlphaCLIP (CVPR 2024) [1], Osprey (CVPR 2024) [2], Ferret (ICLR 2024) [3], OMG-LLaVA (NeurIPS 2024) [4] and so on.
2. **Lacking ablation experiments on the influence of the fine-tuning of ChatGLM**. What is the role of this step? Can fine-tuning enhance the effect of all three stages of the Agent. 
3. **Error analysis about the workflow of agent**. Lack of analysis of Agent workflow failure cases. To which part of the Agent should the cause of the data refinement error be attributed: inference? Tool call? Error perception of the tool itself? Error of reflection?
4. **Computation cost is two large**, 48 V100 GPUs, Normal LABS can't afford it. A lite version should be studied in the future.
5. **Minors**:
    1. Some expressions are more obscure, such as **Re-Aligning Language to Visual Objects**, so it is better to directly use the refine object description in open-v object detection data, which is more clearly and easy to understand.
    2. The use of symbols and naming are not easy to distinguish. For example, the base name $\text{Real LOD}$ used three times, $\text{Real LOD}^{data}, \text{Real LOD}^{model}, \text{Real LOD}^{agent}$. This discourages the reader from quickly distinguishing between these symbols and leads to confusion.

### Questions
Above all this is a good idea. Refining training data to gain more high-quality data for training the model is highly practical. However, I have a question about whether the region-controllable captioner is better than a complex agent workflow. The former is more cheap and easy to use.

### Soundness
3

### Presentation
2

### Contribution
3
