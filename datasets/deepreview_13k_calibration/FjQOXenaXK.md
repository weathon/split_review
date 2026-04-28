# Do Large Language Models Truly Understand Geometric Structures?

- Decision: Accept
- Avg Score: 6.67
- Scores: 6, 8, 6

## Abstract
Geometric ability is a significant challenge for large language models (LLMs) due to the need for advanced spatial comprehension and abstract thinking. Existing datasets primarily evaluate LLMs on their final answers, but they cannot truly measure their true understanding of geometric structures, as LLMs can arrive at correct answers by coincidence. To fill this gap, we introduce the GeomRel dataset, designed to evaluate LLMs’ understanding of geometric structures by isolating the core step of geometric relationship identification in problem-solving. Using this benchmark, we conduct thorough evaluations of diverse LLMs and identify key limitations in understanding geometric structures. We further propose the Geometry Chain-of-Thought (GeoCoT) method, which enhances LLMs’ ability to identify geometric relationships, resulting in significant performance improvements.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates whether large language models can truly understand geometric structure and solve geometric problems. It introduces a new benchmark, **GeomRel**, focused on geometric relationships in three categories: line-based, angle-based, and shape-based relationships. To expand the dataset’s depth and complexity, the authors construct advanced and diverse data subsets within GeomRel. Evaluations on this benchmark reveal that even advanced models like GPT-4o outperform Random Guess by only 20.34% on complex tasks in the advanced GeomRel subset. Building on insights from these evaluations, the paper proposes a two-stage pipeline that guides models to decompose geometric structures and perform relationship observation. Experimental results demonstrate the effectiveness of the proposed pipeline in enhancing model performance on geometric tasks.

### Strengths
- This paper introduces a new benchmark that reveals current LLMs struggle to effectively recognize geometric structures.
- It demonstrates that even with few-shot prompting or fine-tuning, current LLMs do not perform well in recognizing geometric relationships. To address this, the paper proposes a two-stage pipeline that guides LLMs to decompose and observe geometric structures.
- Experimental results in the final section show that the proposed two-stage pipeline effectively enhances LLM performance on geometric tasks.

### Weaknesses
 - This paper dedicates significant space to describing the rules and various data augmentation methods used in constructing the benchmark. However, the overall process and rationale for construction could be presented more clearly.
- In Section 3.5, the paper uses the LLaMA-3-8B-Instruct model as the base model for fine-tuning, which is somewhat unconventional, as it is more typical to fine-tune base models on math-related datasets.
- Including additional experimental metrics commonly used in math domains, such as pass@k, majority voting, or best-of-n, could improve the depth of analysis and provide a more comprehensive evaluation of model performance in this paper.

### Questions
- Could you elaborate on how the benchmark was constructed and clarify how the different relationships, difficulty levels, and diversity augmentation methods were integrated? And for instance do you leverage LLMs to help generate the benchmark or all the questions are based on rules?
- Could you provide results from fine-tuning on the LLaMA-3-8B base model?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses the limitations of large language models (LLMs) in understanding geometric structures, proposing a new benchmark, GeomRel, specifically designed to assess LLMs' ability to identify geometric relationships. The authors identify that while existing datasets mainly measure final answer accuracy, they fail to capture whether LLMs truly understand underlying geometric structures. The GeomRel benchmark isolates the task of geometric relationship identification (GRI) as a foundational skill for geometric reasoning. Using GeomRel, the paper evaluates several LLMs and finds that most perform well on simple geometric relationships but struggle with more complex structures, particularly those involving angle relationships. The authors introduce a new method, Geometry Chain-of-Thought (GeoCoT), which decomposes geometric reasoning into step-by-step relationship identification, significantly improving model performance on GeomRel by over 9% on basic tasks and nearly 15% on advanced tasks.

### Strengths
1. The GeomRel dataset, which isolates geometric relationship identification as a key step, provides a novel and focused way to evaluate LLMs' geometric understanding. This dataset addresses a unique gap in the field and enables more focused evaluation of geometric reasoning capabilities.

2. The Geometry Chain-of-Thought (GeoCoT) method improves LLMs’ performance in identifying geometric relationships by breaking down problems into reasoning steps. The proposed method significantly improved both basic and advanced variants of the dataset.

3. The authors evaluates a range of LLMs, including both proprietary and open-source models, providing a rounded view of how different models handle geometric reasoning. This extensive evaluation is valuable for identifying model-specific strengths and weaknesses in geometric tasks.

4. The paper investigates multiple prompting methods, including Zero-Shot and Chain-of-Thought (CoT), analyzing their effectiveness in GRI tasks. This analysis highlights that while traditional CoT is less effective for geometric tasks, the GeoCoT adaptation provides usefgul improvements for geometric reasoning.

### Weaknesses
1. Although fine-tuning on GeomRel was attempted, the results only report results of a single model. More experiments exploring different models could clarify which models has performance improvements with fine-tuning. Specifically, it is unclear if the observed improvements are model-specific or a general trend across different architectures and pre-training strategies. The paper should include a more comprehensive analysis of fine-tuning across a diverse set of models, including both encoder-decoder and decoder-only architectures, to establish the robustness of the proposed fine-tuning approach.
2. It is difficult to truly understand the difficulty of the dataset for human intelligence. This can be understood by sampling the dataset and carrying out a systematic human evaluation to report human baselines on these geometrics reasoning problems. Without a human baseline, it is challenging to assess whether the performance of LLMs is approaching human-level understanding or if there is still a significant gap. A human evaluation should include a diverse group of participants with varying levels of expertise in geometry to provide a more comprehensive understanding of the dataset's difficulty.
3. GeomRel, while valuable for evaluating LLMs on basic geometric relationships, covers a limited range of geometric concepts, primarily focusing on 2D relationships involving lines, angles, and shapes. This narrow scope may not fully represent the complexity of real-world geometric tasks and it will further help evaluate reasoning capabilities particularly those that involve 3D relationships, transformations (like rotations and reflections), or coordinate-based reasoning. The dataset should be expanded to include more complex geometric concepts, such as 3D shapes, transformations, and coordinate-based reasoning, to better evaluate the full range of geometric reasoning capabilities of LLMs.

### Questions
1. It would help the readers better, if the authors can provide the exact versions of proprietary LLMs that was used as well as other hyper parameters set for these models for inferences as well as for the fine tuning experiments.

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
This paper investigates LLMs abilities to understand geometric relationships and spatial reasoning based on textual descriptions. The authors observe that LLMs often arrive at correct answers without grasping the underlying geometric relationships. To address this, they propose a new task called Geometric Relationship Identification (GRI) and introduce GeomRel, a dataset specifically designed to evaluate models' abilities in GRI. For dataset construction, they create a collection of basic geometric relationships and develop more complex examples by combining and enhancing these foundational relationships.

The authors conduct extensive experiments across several models and strategies, including zero-shot, few-shot, Chain-of-Thought (CoT), and fine-tuning methods. Their findings indicate that current LLMs have significant limitations in spatial understanding and that most strategies yield limited improvements. They propose a new prompting technique, GeoCoT, which decomposes geometric observations and employs reverse reasoning.

### Strengths
* The paper establishes GRI as a new task, shifting focus beyond answer accuracy to intermediate steps in spatial reasoning. 
* The proposed dataset, GeomRel, is valuable, especially with its advanced split that incorporates logical chains, indeterminate cases, and extraneous information, mimicking real-world problem complexity and ambiguity. 
* The paper provides a thorough evaluation across multiple LLMs and reasoning methods, yielding insights into their spatial reasoning capacities and limitations.

### Weaknesses
 * For disambiguation, the authors manually reviewed and excluded ambiguous data throughout the data construction process, which may reduce scalability and limit others’ ability to expand the benchmark.
* The paper’s focus on GRI as an isolated skill may be too narrow, leaving it uncertain if success in GRI tasks will translate to general spatial reasoning or even multi-step problem-solving abilities. Specifically, the current evaluation treats each geometric relationship as relatively independent, whereas real-world problems often require sequential, interdependent reasoning steps where conclusions from one step directly influence subsequent steps. This limitation raises concerns about the ecological validity of the benchmark.
* The two-stage GeoCoT method, which involves decomposing geometry problems and reverse reasoning, may be challenging to scale to more complex tasks. The method's reliance on a specific decomposition strategy and reverse reasoning might not generalize well to problems that require more intricate reasoning chains or different types of problem decomposition.

### Questions
* While the advanced split of GeomRel does require managing multiple geometric relationships, it still treats each relationship as relatively independent. Real-world geometric problems, however, often demand that LLMs execute step-by-step calculations in sequence, where each conclusion logically affects the next. 
* Some analyses in Appendix F are particularly insightful, demonstrating the reasoning path and showing how the vanilla model fails while reverse reasoning aids understanding. It would be valuable to provide experimental results to support these explanations.
*  the paper show marginal gains from fine-tuning. It would be valuable to explore the reasons behind this limited improvement, possibly factors like dataset size, or the nature of the fine-tuning data. 
* In explaining the performance improvements from point relabeling, the authors hypothesize that "using more complex descriptions may stimulate LLMs’ reasoning abilities." This point could benefit from further explanation.

### Soundness
3

### Presentation
3

### Contribution
3
