# 3D-GPT: Procedural 3D Modeling with Large Language Models

- Decision: Reject
- Scores: 5, 6, 3, 3

## Abstract
In the pursuit of efficient automated content creation, procedural generation, leveraging modifiable parameters and rule-based systems, emerges as a promising approach. Nonetheless, it could be a demanding endeavor, given its intricate nature necessitating a deep understanding of rules, algorithms, and parameters. To reduce workload, we introduce 3D-GPT, a framework utilizing large language models~(LLMs) for instruction-driven 3D modeling. 3D-GPT positions LLMs as proficient problem solvers, dissecting the procedural 3D modeling tasks into accessible segments and appointing the apt agent for each task. 3D-GPT integrates three core agents: the task dispatch agent, the conceptualization agent, and the modeling agent. They collaboratively achieve two objectives. First, it enhances concise initial scene descriptions, evolving them into detailed forms while dynamically adapting the text based on subsequent instructions. Second, it integrates procedural generation, extracting parameter values from enriched text to effortlessly interface with 3D software for asset creation. Our empirical investigations confirm that 3D-GPT not only interprets and executes instructions, delivering reliable results but also collaborates effectively with human designers. Furthermore, it seamlessly integrates with Blender, unlocking expanded manipulation possibilities. 
Our work highlights the potential of LLMs in 3D modeling, offering a basic framework for future advancements in scene generation and animation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a workflow for procedural 3D scene generation conditioned on text descriptions using pre-trained LLMs. It leverages an existing procedural generator, InfiniGen, to create 3D contents, and uses LLMs to pick a set of procedural functions from InfiniGen and infer their corresponding parameters given the text description of the scene. The authors split the task into three steps (agents): the first step is to select the set of functions given the prompt, the second step is to infer more detailed descriptions given the required informatin, and the last step is to generate the parameters for each function given the detailed description. The experiment results show that this workflow can produce single class objects with details and complex scenes.

### Strengths
- The proposed method does not require training.
- The multi-agent approach is effective. It might share similar advantages as other methods such as chain-of-thought or tree-of-thought, where the final output from the LLM is guided by a curated step-by-step instruction.
- It addresses another potential direction for text-to-3D generation: utilizing tools or existing 3D procedural models. 
- It demonstrates the potential of using LLMs to control tools for content creation and 2D/3D modeling.

### Weaknesses
 - Lack of details about the model and experiment setting and how the results are affected. For example, which LLM is used? What is the size of the function set F? Does the size of F affect the quality? How many examples are provided? Do the example related to the prompt L? Does zero-shot/few-shot make any difference? 
- Evaluation can be improved. It would be great to do ablation studies on D, C, I, E, and answer the questions mentioned above.
- It would be great to further explore the limitations and failure cases. For example, does the complexity of the scene affect the results? Does the number of parameters or the design space (e.g., parameter ranges) affect the results? 
- The proposed method demonstrates that the LLM can convert the input prompts to python codes that controls the functions and parameters. However, since the 3D modeling capability comes from the procedural models, not from the LLM, it seems the task is closer to scene composition or object inference instead of modeling. It will be more interesting to see if LLMs can generate 3D modeling commands or procedural modeling sequences/rules.

### Questions
- There are many procedural models available for Blender. It will be interesting to see if this workflow will work on any arbitrary procedural models given the same amount of information, i.e., D, C, I , and E, such as house, car, airplanes instead of focusing on scenes in InfiniGen.

- It will be great to see if the selected functions can formulate some dependencies, for example, to generate 'flowers on the trees', the trees need to be created first and the positions of the flowers are based on the positions of the tree branches.

- It will be great to see a full example of the input and output of each agent in the process.

- Have the authors tried to also provide the functions picked by the TDA to CA?

- It is obvious that this method will help users who know nothing about 3D modeling, but I am curious whether the sequential editing task in Fig 4 will be more efficient to professional Blender users (e.g., game developers) to achieve a desired outcome, compared to tweaking the parameters by themselves.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper Introduces 3D-GPT, a training-for-free framework designed for 3D scene generation, which generates Python codes to control 3D software, potentially offering increased flexibility for real-world applications.

### Strengths
1. The generation ability of 3D scenes and objects are good according to the demo.

2. The step-by-step refinement of 3D outputs is meaningful and impressive.

3. The paper is easy to follow with good-quality figures.

### Weaknesses
I'm not an expert in 3D procedural 3D generation, and here are some of my concerns.

1. The paper only shows examples of 3D plants and forests. Can 3D-GPT work on other objects or scenes, such as human and street? Can 3D-GPT generalize well to more complex scenarios?

2. The paper adopts ChatGPT as LLM. How about other open-source LLMs, such as Alpaca, LLaMA-Adapter, or Vicuna?

### Questions
See weakness

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors present a method that can take in natural language and output code in a Domain-Specific Language. The DSL is a system that can generate 3D scenes and assets in a procedural fashion.

Therefore the overall pipeline converts natural language into realistic, high quality 3D scenes.

### Strengths
The results are **incredibly strong** - looking at the submitted video. Especially the results on sky-editing.

### Weaknesses
 **(MAJOR) Lack of detail**

---

The paper describes the system at a very high level. We are introduced to the "Task Dispatch Agent", the "Conceptualization Agent" and the "Conceptualization Agent" but no details of how they are actually implemented. There is no detail of what subset of the InfiGen language is used, no detail of “translate the scene into a winter setting”, it pinpoints functions like add snow layer() and update trees()"

While there are some examples in the Appendix of the prompts and the associated code, it is woefully incomplete.

In the current iteration, it is almost impossible to implement/reproduce the paper.

I will not knock the paper down for a lack of quantitative results because this space is very new and no metrics apart from user studies really exist and creating a new procedural baseline would itself be a lot of work.

### Questions
I wonder if the authors would send this work to a compilers conference/journal instead?

In case they are too rigorous to accept LLM based papers, why not something like ToG or SIGGRAPH. Both have wonderful papers describing procedural systems where the parameters come from some heuristic model. This paper with its strong results and a graphics focus seems like a perfect fit for such venues.

I would be willing to accept this paper only after a major rewrite which would include a lot more description of the various components in the proposed approach.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents a new 3D scene generation pipeline using procedural 3D modeling together with LLMs. Specifically, LLMs are given the documentations of a procedural 3D modeling tools together with human instructions. Three LLM agents, namely the task dispatch agent, the conceptualization agent and the modeling agent, are designed to work together and generate Python scripts for the 3D modeling tools that generate 3D scenes/ objects that corresponds to the given instructions. Qualitative and quantitative experiments are performed to show the results of such pipeline and prove the effectiveness of using three agents to collaborate on this task.

### Strengths
1. This paper shows the potential of using LLMs and procedural 3D modeling tools on text-guided 3D generation tasks.
2. Having three agents collaborating on generating the final Python scripts is interesting and proven to be effective.

### Weaknesses
1. Though it is a nice application to use LLM with procedural 3D modeling tools for text-guided 3D generation, I think the overall contribution of this paper is not enough to be considered for publication on ICLR. The community has had many similar discoveries on the ChatGPT/ GPT-4's ability on generating parameters for images [1] or 3D objects [2] in a zero-shot or in-context learning way. Therefore, there is no surprise that combining LLM with a better parametric 3D modeling tool, e.g., InfiniGen, could produce better visual results. I think all the three potential directions mentioned in the last section are promising and valuable challenges to solve, which would bring more contribution to the community.

2. The evaluation is limited. I must admit that for a new task of text-guided 3D scene generation, it is hard to construct baseline methods. But at least, there are similar efforts in the community of text-guided 3D object generation that worth being compared with. For example, score-distillation-based methods, e.g., DreamFusion, can be used as baselines for the "Single Class Control" experiments.

### Questions
See above weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
1 poor
