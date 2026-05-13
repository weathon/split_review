# Divide-Verify-Refine: Aligning LLM Responses with Complex Instructions

- Decision: Reject
- Scores: 5, 8, 6, 3, 5

## Abstract
Recent studies show that LLMs, particularly open-source models, struggle to follow complex instructions with multiple constraints, hindering their adoption in mission-critical applications. Despite the importance, methods to improve LLMs' adherence to such constraints remain largely unexplored, and current research focuses primarily on evaluating this ability rather than developing solutions. While a few studies enhance constraint adherence through model tuning, this approach is computationally expensive and heavily reliant on training data quality. 
An alternative is to leverage  LLMs' self-correction capabilities, allowing them to adjust responses to better meet specified constraints. However, this self-correction ability of LLMs is limited by the feedback quality, as LLMs cannot autonomously generate reliable feedback or detect errors. Moreover, the self-refinement process heavily depends on few-shot examples that illustrate how to modify responses to meet constraints. As constraints in complex instructions are diverse and vary widely (e.g., text length,  number of bullet points, or  inclusion of specific keywords), manually crafting few-shot examples for each constraint type can be labor-intensive and sub-optimal. To deal with these two challenges, we propose the \textbf{Divide-Verify-Refine (DVR)} framework with three steps: (1) \textbf{Divide} complex instructions into single constraints and prepare appropriate tools; (2) \textbf{Verify}: To address the feedback quality problem, these tools will rigorously verify responses and provide reliable feedback (e.g., Python scripts for format checking or pre-trained classifiers for content analysis); (3) \textbf{Refine}: To address the constraint diversity challenge, we design a refinement repository that collects successful refinement processes and uses them as few-shot demonstrations for future cases, allowing LLMs to learn from the past experience during inference. 
Additionally, recognizing that existing datasets lack complexity and have internal conflict, we develop a new dataset of complex instructions, each containing 1-6 constraints. Experiments show that the framework significantly improves performance, doubling LLama3.1-8B's constraint adherence and tripling Mistral-7B's performance on instructions with 6 constraints. The code and dataset are available at \href{https://anonymous.4open.science/r/CODE_ICLR2025-52CE/README.md}{https://anonymous.4open.science/r/CODE\_ICLR2025-52CE/README.md}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper proposes Divide-Verify-Refine (DVR), which is a framework that helps LLM generate responses that can meet complex instructions. Specifically, DVR is divided into three steps: (1) Divide, where LLMs is prompted to divide instructions into multiple constraints and to prepare approximate tools for each constraint; (2) Verify, where tools are used to check whether the response meets corresponding constraints and, if not, provide detailed feedback; (3) Refine, where a refinement repository is proposed to collect successful refinement processes which will be used as few-shot examples when LLMs use the detailed tool feedbacks to refine their previous responses. Evaluation on CoDI and ComplexInstruct (a newly proposed benchmark) across different LLMs demonstrates the effectiveness of DVR.

### Strengths
- The paper proposes a new benchmark to better evaluate complex instruction-following capabilities of LLMs.
- The paper includes a comprehensive evaluation with a detailed analysis on the effectiveness of DVR.

### Weaknesses
 - The primary concern with this work is its novelty. While authors claim that DVR differs from CRITIC by (1) incorporating a refinement repository module to provide few-shot examples and (2) using multiple tools rather than a single tool to provide a more detailed feedback, such differences are quite minimal and don't seem to be pass the bar for ICLR.
- The assumption of external tools being available for all existing constraints is not realistic. While authors claim that code generation models can be used to generate Python scripts (i.e., new tools) to check new constraints when there are no existing tools, the correctness of the newly generated tools cannot be guaranteed, and thus their detailed feedback will not be reliable.

### Questions
- Are there any examples of external tools (e.g., Python code) being used in the experiment?
- What is the overhead of DVR compared with all the baselines?

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a technique called DVR to improve the alignment of LLM responses specifically with the constraints given within the responses. The technique is a three stage iterative process, where the first stage gathers the constraints, the second gets the response from the LLM, and the third iteratively refines the response based on the constraints satisfied. The technique improves the performance of major LLM models by a significant amount.

### Strengths
Firstly, I really liked how the paper was written. It was clear and easy to understand. The problem being addressed is a well documented issue of response alignment, and the technique seems to use a divide and conquer approach to solve it, which seems quite novel. The paper also presents a thorough evaluation of the technique over multiple models compared with several baselines.

### Weaknesses
I don't see too many weaknesses in the paper. One thing I would like to see addressed is a limitations or future work section to specify the shortcomings of the tool. It would also be nice to have a discussion on what it would take to expand the constraints from being purely conjunctive (which I think it is right now) to including disjunctions and negations at the very least. I also think it is important to better showcase that in each iteration of the feedback generation, an LLM is called to get the refined response. Right now when I look at the diagram, unless I am paying attention to the arrow shapes, I would think that the LLM is only called when getting the initial response.

### Questions
1. Is this system modular? I.e. what would it take for us to incorporate additional kinds of constraints, tools, etc.?
2. Are there any other datasets you can include? Maybe datasets like code generation datasets where constraints can be more implicit but can be programmed into the prompt from the evaluator's side (like syntax correctness, correct return types, etc.)? This is dependent on the amount of effort required to get this working with such datasets.
3. Is there a reason you don't evaluate GPT models? I understand that such errors are more prone to occur in open source models but it would be nice to see GPT-4 as a baseline

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
Paper introduces Divide-Verify-Refine framework to overcome the struggele of LLMs for following instruction. In this framework first break down complex instructions into individual constraints and prepare suitable tools (Divide). Then it uses these tools to check responses and ensure quality feedback (Verify) and then it create a refinement repository to gather successful processes, using them as examples for future cases to improve the model (Refine). Also, authors develop new dataset of instructions, each containing 1-6
constraint.

### Strengths
The DVR framework introduces a structured methodology to process instructions, decomposing, verifying, and refining which can lead to better results.
The method is on the fly and not need for fine-tunning
DVR improves the performance across multiple datasets

### Weaknesses
The effectiveness of the system is on the quality and accuracy of the external tools used for verification and feedback. Poorly performing tools can degrade the overall performance of the LLM.

It would be beneficial to compare DVR method with other methods, such as ReAct, in other tasks such as  reasoning tasks.

### Questions
Take a look at the weakness section

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
In this paper, the authors propose *Divide-Verify-Refine (DVR)*, a framework designed to improve the adherence of large language models (LLMs) to complex, multi-constraint instructions, which divides instructions into single constraints, employs external tools for reliable verification and refines responses using a repository of successful adjustments. The authors conduct experiments on a new dataset to demonstrate the DVR's ability to enhance constraint adherence across various instruction types without requiring retraining.

### Strengths
The framework’s approach to decomposing complex instructions and using external tools to verify constraint adherence is novel in the context of LLM alignment without model retraining.

Evaluation results demonstrate DVR's effectiveness across varying constraint complexities.

The paper is clear, with well-defined modules for dividing, verifying, and refining stages, making the strategy understandable and reproducible.

### Weaknesses
The criteria for selecting external tools lack specificity, making it unclear how LLMs autonomously match tools to specific constraints.

The reliance on specific tools (e.g., Python-based scripts) could limit DVR’s generalizability across broader application domains or languages.

While ComplexInstruct is valuable, further validation on industry-standard benchmarks could better position DVR’s real-world applicability.

### Questions
Could the authors elaborate on how the DVR framework ensures that the refinement repository remains free from erroneous examples that could degrade LLM performance?

How might DVR handle instructions with unstructured or conflicting constraints, and are there plans to address such limitations in future work?

Could further details on how tools were evaluated for their accuracy and reliability in feedback generation be provided?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper presents the Divide-Verify-Refine (DVR) framework, which enhances the ability of Large Language Models (LLMs) to follow complex instructions with multiple constraints. The DVR framework consists of three steps: dividing complex instructions into single constraints, verifying responses with external tools for reliable feedback, and refining responses using a repository of successful refinement examples. The framework is evaluated on two datasets, showing significant improvements in constraint adherence without the need for retraining. It addresses the challenges of feedback quality and constraint diversity by integrating tools and leveraging past experiences, respectively. The paper concludes that DVR offers a scalable solution to enhance the practical usability of LLMs in real-world applications.

### Strengths
- The DVR framework significantly enhances LLMs' ability to adhere to complex instructions containing multiple constraints, which is crucial for mission-critical applications.

- Unlike fine-tuning approaches, DVR improves LLM performance without the need for extensive retraining, making it more accessible and less computationally expensive.

- By leveraging external tools for verification, DVR provides a more reliable feedback mechanism than LLMs' self-reflection, which tends to be unreliable.

### Weaknesses
 - When preparing appropriate tools for verification, how accurate are the tools? Are there many problems with the tools themselves? If there is a problem with the tools, it can cause problems in all subsequent modules.
- For completely new constraints, there may not be examples where a tool is readily available. Imagine a scenario where we need to develop a large language model (LLM) to generate text in a specific style, say "Gothic" style, but currently there is no tool to directly verify if the text is in this specific style.
- DVR has more flow modules, which results in the experimental setup not being very solid.

### Questions
No questions.

### Soundness
2

### Presentation
3

### Contribution
2
