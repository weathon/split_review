# Facilitating Multi-turn Function Calling for LLMs via Compositional Instruction Tuning

- Decision: Accept
- Avg Score: 6.50
- Scores: 5, 8, 8, 5

## Abstract
Large Language Models (LLMs) have exhibited significant potential in performing diverse tasks, including the ability to call functions or use external tools to enhance their performance. While current research on function calling by LLMs primarily focuses on single-turn interactions, this paper addresses the overlooked necessity for LLMs to engage in multi-turn function calling—critical for handling compositional, real-world queries that require planning with functions but not only use functions.
To facilitate this, we introduce an approach, \method, which generates synthetic compositional instruction tuning data via bottom-up instruction construction and top-down trajectory generation. 
In the bottom-up phase, we generate simple atomic tasks based on real-world scenarios and build compositional tasks using heuristic strategies based on atomic tasks. Corresponding functions are then developed for these compositional tasks. The top-down phase features a multi-agent environment where interactions among simulated humans, assistants, and tools are utilized to gather multi-turn function calling trajectories. This approach ensures task compositionality and allows for effective function and trajectory generation by examining atomic tasks within compositional tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces a new approach, BUTTON, to generate synthetic compositional instruction tuning data, which could further serve as instruction tuning data for LLMs. Compared to existing methods, this approach can engage in multi-turn function calling, which enables planning with functions in handling real-world compositional tasks.

### Strengths
1.	This paper first addresses the problem of planning with functions but not only use them when handling compositional tasks. The originality sounds good. 
2.	This paper is well structured with good clarity.
3.	The experiment results are mostly convincing and significant compared to existing methods.

### Weaknesses
1.	The authors state that they differ from existing papers that ‘use functions’ by ‘plan with functions’. They are encouraged to compare with these methods. A simple way can be conducting chain-of-thought methods to decompose a compositional tasks, and then use these reference methods in each step. Can the performance still be significant enough?
2.	More experiment designs could make it more convincing. How is the performance when the task composition length, i.e. the amount of sub-tasks in one task increases? See also Question 1.


### Questions
1.	Does the designed heuristic strategy for compositional task construction only contain 2 or 3 sub-tasks? For example, can the sequential composition heuristic allow for an arbitrary length of sub-tasks? How is the performance according to different length of sub-tasks?
2.	It is a confusing on how function generation is conducted in Bottom-Up. The authors state that they allow for the construction of more realistic tasks, and generate functions that are likely to be called in these tasks. Is there any limitation or alignment on the function call generation? Since the function tools are specified and given in GTA and Tool-Query for evaluation, it seems that the Bottom-Up should be limited in using these given functions, rather construct new ones. Is there a conflict?
3.	The authors are encouraged to provide how prompts are designed for ablation study, i.e., how to call the single direct generation steps using one prompt. 
4.	In Introduction, the bullet-in points in the last paragraph of how to solve challenges do not tackle with the challenges very well. The authors may better summarize how “compatibility” in challenge 2 and “without human supervision” in challenge 3 are tackled.
5.	Typo and grammar check, such as ‘we first extract a series of real-world scenarios from existing datasets that using external tools.' in Scenario Collection in Section 2.1.

### Soundness
3

### Presentation
4

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
The paper discussed an approach, BUTTON, which generates synthetic compositional instruction tuning data via bottom-up instruction construction and top-down trajectory generation.

### Strengths
1. The research topic itself has a wide range of practical use cases. 
2. The model training approach is innovative and offers a new perspective on training large language models to make multi-turn function calls. 
3. The explanation of the methodology is clear and detailed. The authors trained multiple popular large language models to compare performance and validated accuracy on two benchmark datasets, providing a more comprehensive analysis.

### Weaknesses
In the paper, the author mentioned about “multi-turn function calling”,  “function calling” and “invoke functions” many times. Although the solution purposed could potentially solve the function calls with other additional infrastructure setups, it could be a bit misleading to the readers since the pipeline is still mocking the function call with simulated responses.

In the section 3.1 experiments setup, the author evaluated the pipeline with two different benchmark datasets. This part could be better structured.

### Questions
1.  It might be better to explain “function calling” a bit ahead in the abstract part to avoid confusion as the pipeline is not essentially invoking a function.
2. I would recommend to move the “related work” after the introduction to give the readers more background before introducing the methodology.
3. I would recommend to start section 3.1 experiments with a brief introduction and split them into two subsections under which you can explain the description and evaluation metrics with some bullet points.

### Soundness
3

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
5

### Summary
The authors found that when large language models are called external functions, there is another important but neglected problem: how should the model plan and use these functions when dealing with complex tasks that require multiple rounds of dialogue?

To solve this problem, they proposed a method called **BUTTON**. This method is divided into two steps:

- The first step is to build training data from the bottom up. They first designed some simple basic tasks and then combined them into more complex ones. Then, they developed corresponding functional interfaces for these tasks.

- The second step is to generate dialogues from the top down. They built a multi-agent environment to allow simulated users, assistants, and tools to interact and generate data for multiple rounds of dialogue.

In this way, they generated 8,000 high-quality training data. Experimental results show that models trained with this data perform better when dealing with complex tasks.

This research is efficient because tasks in real life often require multiple steps to complete, and models must learn to plan what functions to use and when to use them.

### Strengths
**Originality**

Currently, large prediction models are very popular, and most researchers are studying how to make the model give higher-quality human-like text in dialogue. The authors found two difficulties: 1. The instructions of multi-round dialogues are too complex to be recognized by the model, and 2. There are problems with the compatibility of instructions and functions.

**Quality**

The author proposed a new method, the BUTTON method, which has a clear technical route and includes two stages: 1) bottom-up instruction construction and 2) top-down trajectory generation. Two professional benchmarks (GTA and Tool-Query) were used to evaluate performance during the experiment. The scale of 8,000 data points is medium-sized in current similar studies, but it includes multiple roles such as system, user, assistant, tool, etc., which enriches the interaction scenario. The experimental results compare several currently very popular large language models, which is convincing.

**Clarity**

The paragraphs of the article are very clear and easy to understand. The technical terms are also explained.

**Significance**

This study solves the data acquisition problem through synthetic data and function call mechanism, which not only reduces the development cost but also expands the practical scenarios of LLM, which is of great significance in promoting the implementation of AI technology in practical applications.

### Weaknesses
The sample size of the benchmark GTA is small, with only 229 queries, and the benchmark Tool-Query has only 60 tasks, which may not fully cover the actual application scenarios. At the same time, the benchmark may have a subjective bias because the manually written queries may carry the subjective judgment of the writer, and the difficulty classification criteria may not be objective enough. Suggestions can be combined with questionnaires for evaluation, such as collecting feedback from actual users and obtaining more real scenario requirements through questionnaires.

### Questions
How the 8,000 data points mentioned in the experiment were selected was not mentioned, which lacks the rigor of experimental design. It is recommended that the author describe the data mining process in detail. In addition, the specific distribution of these data for different roles is not explained. It is better to provide a chart to show it.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces BUTTON, a generation pipeline to improve multi-turn function calling for LLMs through compositional instruction tuning, to handle complex real-world tasks requiring sequential or parallel function calls.  BUTTON uses a combination of bottom-up task creation and top-down trajectory generation in a multi-agent environment. This pipeline also produces BUTTONInstruct, a dataset with 8,000 multi-turn function call trajectories, and demonstrates improved model performance across various benchmarks.

### Strengths
1. This paper offers a scalable solution for creating synthetic multi-turn datasets, enhancing LLM capabilities in function calling. This is an important feature for AI agents in many applications.

2. The BUTTON pipeline is innovative in combining both bottom-up and top-down data generation processes to address the need for getting complex, multi-turn interactions data  from real-world.

3. The performance seems good. After finetuned with the generated dataset, all models get improved in terms of accuracy.

### Weaknesses
1. While the BUTTON pipeline effectively generates compositional tasks and interaction trajectories, the paper lacks a rigorous quality control process. For example, it does not sufficiently address how to ensure that two atomic tasks are logically compatible for creating a meaningful complex task. Furthermore, the paper mentions filtering compositional tasks by “checking whether each one can be completed by its atomic sub-tasks.” However, it remains unclear whether this condition alone is adequate to ensure that the composed tasks are realistic and applicable to real-world scenarios. The absence of a clear methodology for verifying the logical consistency and real-world applicability of composed tasks raises concerns about the overall quality of the generated dataset. Specifically, the paper does not detail how the system prevents the generation of tasks that, while technically composed of sub-tasks, are nonsensical or impractical in a real-world context. For instance, a composed task might involve booking a flight and then immediately canceling it without a logical reason, which would not be a useful training example.

2. The generated function calls are conceptual, lacking actual implementations, which may limit their practical usability. Without concrete implementations, there is a risk that these generated function calls might not be feasible in real-world applications. Additionally, it’s unclear whether the pipeline checks for duplicated function calls or if previously generated functions can be reused in later processes, both of which could enhance efficiency and coherence in the generated dataset. The lack of detail on how the system ensures that generated functions are unique within a task and across tasks raises concerns about the diversity and quality of the generated function calls. For example, if the same function is generated multiple times with slightly different names, it could confuse the model during training and not reflect real-world API usage.

### Questions
1. The pipeline effectively generates parallel-then-sequential compositions, but how does BUTTON determine which tasks are best suited for parallel execution? Are there specific criteria or heuristics that guide the system in identifying parallelizable tasks?

2. What is the seed data to generate the atomic tasks?

3. How many atomic tasks can be used to generate a composed task at most? Does it affect the data complexity and fine-tuned performance?

### Soundness
3

### Presentation
3

### Contribution
2
