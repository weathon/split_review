# HumanEval-V: Evaluating Visual Understanding and Reasoning Abilities of Large Multimodal Models Through Coding Tasks

- Decision: Reject
- Avg Score: 4.60
- Scores: 5, 5, 5, 5, 3

## Abstract
Coding tasks have been valuable for evaluating Large Language Models (LLMs), as they demand the comprehension of high-level instructions, complex reasoning, and the implementation of functional programs -- core capabilities for advancing Artificial General Intelligence. Despite the progress in Large Multimodal Models (LMMs), which extend  LLMs with visual perception and understanding capabilities, there remains a notable lack of coding benchmarks that rigorously assess these models, particularly in tasks that emphasize visual reasoning. 
To address this gap, we introduce \ourbench, a novel and lightweight benchmark specifically designed to evaluate LMMs' visual understanding and reasoning capabilities through code generation. \ourbench includes 108 carefully crafted, entry-level Python coding tasks derived from platforms like CodeForces and Stack Overflow. Each task is adapted by modifying the context and algorithmic patterns of the original problems, with visual elements redrawn to ensure distinction from the source, preventing potential data leakage.
LMMs are required to complete the code solution based on the provided visual context and a predefined Python function signature outlining the task requirements. Every  task is equipped with meticulously handcrafted  test cases to ensure a thorough and reliable evaluation of  model-generated solutions.
We evaluate 19 state-of-the-art LMMs using \ourbench, uncovering significant challenges. Proprietary models like GPT-4o achieve only 13\% pass@1 and 36.4\% pass@10, while open-weight models with 70B parameters score below 4\% pass@1. Ablation studies further reveal the limitations of current LMMs in vision  reasoning and  coding capabilities. 
These results underscore key areas for future research to enhance LMMs' capabilities.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper HumanEval-V primarily assesses the performance of large multimodal models (LMMs) in tasks incorporating visual understanding and code generation. The models show significant challenges in generalizing across multimodal inputs and reasoning through intricate tasks. Furthermore, the models' preference for simpler tasks and the difficulty in objectively evaluating visual reasoning capabilities limit their practical applications.

However, there are certain limitations. The benchmark's rigid code-image integration limits authentic assessment of multimodal code generation, and score differentiation is minimal. Additionally, the narrow evaluation scope lacks detailed metrics, restricting insights into the models' full capabilities.

### Strengths
Key strengths of this paper: 
1. its introduction of a new benchmark, HumanEval-V, specifically designed to evaluate the visual understanding and reasoning capabilities of multimodal models—an area previously lacking in systematic evaluation standards 
2. By using coding tasks to test models’ ability to process visual information. Additionally, it also assesses the alignment between multimodal and language understanding capabilities.

### Weaknesses
1. Rigid integration of code and image tasks: Many tasks do not necessarily require code-based solutions, making it stiff to reflect the code generation abilities of multimodal models or how multimodal information enhances code generation. This results in a somewhat stiff.
2. Limited differentiation in performance scores: Many models achieve near-zero scores, making it difficult to effectively distinguish performance levels between models.
3. Narrow evaluation scope: The evaluation lacks detailed metrics for multimodal understanding and code generation, overlooking the potential of multimodal models to assist in understanding code tasks or provide feedback, resulting in a singularity assessment of model capabilities.

### Questions
1. In the experiments, how do you understand the fact that image + explanation often yields poorer results than using explanation alone? Have you adjusted the prompts? Can images not enhance understanding?
2. Are there multi-image question types included?
3. Why is the code capability weak even when only given direct explanations? Do you know the reasons behind this? Its performance on HumanEval+ and MBPP+ appears normal.
4. Why not consider using images as feedback signals?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper introduces a multi-modal code generation benchmark, HumanEval-V, containing 108 test samples. Unlike traditional code generation tasks, this benchmark allows images to serve as the problem input (e.g., charts, trees, maps). The authors benchmarked a variety of both closed and open large multimodal models, finding that while baseline performance is generally low (e.g., GPT4o at 13% pass@1), providing annotated image descriptions significantly boosts performance (e.g., GPT4o from 13% to 45.4%).

### Strengths
- This benchmark effectively assesses both visual reasoning and code generation capabilities, providing a cohesive indicator for multi-modal models, especially those adapted from LLMs with vision encoders. Balancing textual and visual reasoning is challenging in training, and this benchmark helps to evaluate these combined strengths.
- The benchmark demonstrates a high level of curation and screening, reducing data contamination and ensuring that the input image is essential to solving the task.
- The writing is well-organized and detailed, enhancing readability.

### Weaknesses
 - The benchmark’s size (108 test samples) and real-world coverage are somewhat limited, as these samples originate from 40 unique cases. While curated, the small sample size might limit generalizability and increase susceptibility to overfitting. Expanding the dataset with more diverse sources and formats beyond traditional coding puzzles could improve robustness. For example, a task might involve writing the code behind the given plot and changing its top line color from blue to green.
- While the benchmark is valuable, combining multimodal reasoning with code generation might seem niche. While beneficial to evaluate both capabilities together, the community can also test them independently. It remains to be clarified whether this benchmark is essential for multimodal or code generation research areas.

### Questions
On line#472, Qwen-VL LMM seems to outperform LLM by a large margin (6.7%) but not specified in “while InternVL-2 (4.2B) and LLaVA-OneVision (8B) show the least”. Adding a bit more context could help prevent potential reader misinterpretation.

### Soundness
3

### Presentation
4

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
The paper introduces HumanEval-V, a novel benchmark designed to evaluate the visual understanding and reasoning capabilities of Large Multimodal Models (LMMs) through coding tasks. It addresses a gap in existing benchmarks by focusing on tasks that require both visual reasoning and coding abilities. The benchmark comprises 108 entry-level Python coding tasks that necessitate visual context to solve, adapted from platforms like CodeForces and Stack Overflow to prevent data leakage. Each task is equipped with handcrafted test cases for thorough evaluation. The paper reports the results of 19 state-of-the-art LMMs on HumanEval-V, revealing significant challenges in current LMMs' visual reasoning and coding abilities, with even leading models achieving low pass rates. Ablation studies demonstrate performance gains when models are provided with textual descriptions of images, indicating the need for enhanced visual understanding capabilities. The findings highlight areas for future research to improve LMMs' visual reasoning and coding skills.

### Strengths
- Novel Benchmark: The paper introduces HumanEval-V, a unique benchmark that specifically targets the visual understanding and reasoning capabilities of LMMs through coding tasks, addressing a significant gap in current evaluation methods.
- Comprehensive Evaluation: Each task is equipped with handcrafted test cases, allowing for a thorough and reliable evaluation of the model-generated code solutions.

### Weaknesses
 - Limited Number of Coding Tasks: The benchmark currently contains a relatively small number of tasks, which may limit the breadth of the evaluation. But the construction of this dataset does require a lot of human effort.
- This work evaluates the reasoning ability of MLLM from a new perspective, but I think this work is slightly simpler and less workload.

### Questions
No questions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents HumanEval-V, a benchmark designed to assess the visual reasoning capabilities of Large Multi-modal Models (LMMs) through code generation based on images. It comprises 108 entry-level Python coding tasks adapted from Codeforces and Stack Overflow. These tasks evaluate LMMs' ability to reason across both visual and textual contexts. The study examines 19 state-of-the-art LMMs, highlighting significant limitations in their visual reasoning and coding abilities, as well as the gap between advanced proprietary models and open-source models.

### Strengths
**Motivation & task design**: The motivation is clear, that it aims to eliminate any potential data leakage and strengthen the necessity of using image information for solving coding task. The paper demonstrates high-quality task design, ensuring that the visual context is essential for solving the coding problems.

**Clarity**: The dataset construction and evaluation are clearly articulated. The experimental settings and selected models are considered reasonable and comprehensive.

**Analysing experiments**: The analysing experiments are solid, demonstrating how models perform under different task settings.

### Weaknesses
 **Limited Dataset Size**: Although the authors have acknowledged in the Limitations section that they plan to expand the dataset, the current version only includes 108 coding tasks, which were derived from a set of 40 tasks. This limited size raises concerns about the dataset's ability to comprehensively and robustly evaluate the full spectrum of visual reasoning & coding abilities in LMMs. The mutation strategy, while increasing the number of tasks, may not introduce sufficient diversity to truly challenge the models across a wide range of visual reasoning scenarios. The core 40 tasks might still represent a relatively narrow distribution of problem types, potentially leading to overfitting on the benchmark itself.


**Novelty Concerns**:  While the authors emphasize improvements over the MMCode benchmark, the degree of novelty in HumanEval-V remains limited. Both benchmarks focus on integrating visual elements with coding tasks. The contribution feels incremental rather than groundbreaking. There are also other coding related benchmark that emphasizes visual information like ChartMimic, Plot2Code. The distinction between HumanEval-V and these existing benchmarks, particularly in terms of the specific visual reasoning skills being tested, needs to be more clearly articulated. The claim that HumanEval-V targets higher-order reasoning abilities needs more substantial justification, as the tasks could potentially be solved through pattern recognition rather than genuine reasoning.


**Applicability of the Task**: According to 2.1 or Appendix C.1, the authors sourced data from posts made from 2020, ultimately narrowing the dataset down to just 8 posts that met the criteria for inclusion in the benchmark. This raises concerns about the broader relevance and applicability of these tasks. If multi-modal coding tasks of this type are so rarely encountered, it calls into question whether this benchmark truly reflects the challenges that LMMs would face in real-world scenarios. The narrow focus may result in tasks that are too niche to provide meaningful insights into practical LMMs development. The reliance on Stack Overflow posts, which are inherently designed for human consumption, might not accurately represent the types of visual-coding problems that LMMs would encounter in practical applications.

### Questions
Apart from my main concerns listed in the above weaknesses part, here are some questions:
* Can the authors offer some analysis regarding the types of images on which LMMs perform better or worse? For example, are there specific visual patterns or image complexities (e.g., graphs, maps) where models consistently struggle or excel?
* The paper mentions that tasks were adapted and modified to prevent data leakage. Could the authors elaborate on the specific steps taken to ensure that LMMs do not rely on memorized patterns from previous coding datasets? Were any ablation studies conducted to verify the effectiveness of these modifications?
* The authors mention that human-annotated image descriptions significantly improved model performance. Could more details be provided on how these descriptions were structured?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents HumanEval-V, a benchmark for evaluating Large Multimodal Models (LMMs) on entry-level coding tasks that require visual understanding and reasoning. It includes 108 adapted hand-written Python coding challenges, each with test cases. Current LMMs perform poorly in this benchmark.

### Strengths
- All questions are adapted from the original sources manually to avoid possible data contamination.
- Visual elements are critical in the questions.
- Extensive experiments on many code models.

### Weaknesses
 - **Lack of novelty**: The benchmark and evaluation pipeline closely align with MMCode[1], without significant innovation.
- **Limited diversity of the benchmark**: the 108 questions are adapted from 40 core questions, and many images are reused across images (see questions)

### Questions
- Can you share more details on how the dataset was created? In Section 2.2, 

> We then create a new coding problem by modifying the context and patterns of the original problem and redrawing the corresponding images.

To what extent did the authors modify the context and images? Do the adapted questions share a similar solution to the old questions?


> Following the initial annotation of the 40 coding tasks, we conduct an additional round of mutation-based extensions. This process expands the number of coding tasks based on the initial annotations, by creating similar yet distinct coding tasks.

> （in Appendix C.3) The objective is to generate new tasks that retain the essence of the original tasks but introduce
distinct patterns with minimal modification

Does this process hurt the diversity of the proposed dataset? How many distinct images are there in the dataset?

### Soundness
2

### Presentation
2

### Contribution
1
