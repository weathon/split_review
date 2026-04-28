# Detecting Problematic Questions to Support Math Word Problem Design

- Decision: Reject
- Avg Score: 5.33
- Scores: 6, 5, 5

## Abstract
When designing math word problems, teachers must ensure the clarity and precision of the question to avoid multiple interpretations and unanswerable situations, thereby maintaining consistent grading standards and effectiveness. We address these issues to provide comprehensive support to teachers in creating clear, solvable, and formal math word problems. In this paper, we present MathError, a dataset of real-world math word problems annotated with error types to investigate the need for question correction. Our work explores how large language models (LLMs) can assist teachers in detecting problematic questions to support math word problem design in scenarios with limited data, simulating real-world conditions with minimal training samples. Preliminary results demonstrate the models' capabilities in detecting problematic questions and identify areas for further research and development in educational applications.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces MathError, a dataset of annotated math word problems aimed at helping teachers identify and correct issues that could lead to ambiguous or unsolvable questions. By leveraging large language models (LLMs), the study demonstrates how these models can aid teachers in designing clear and consistent math problems. To do so, the authors propose a self-optimizing framework where the model iteratevily refines the demonstration.

### Strengths
- The paper is well written, has clear motivation, and has a well-explained methodology.

### Weaknesses
W1: How significant is the problem of erroneous questions? When humans communicate, language often contains implicit information and inherent ambiguity, yet people generally understand and perform well despite this. The main question is: how much do expression errors in math questions impact the performance of both humans and models? An analysis comparing the performance of large language models (LLMs) and humans on ambiguous math questions versus corrected versions would be valuable. Does performance improve when questions are clarified, or can models, like humans, effectively handle the natural ambiguity in language?

W2: The primary weakness of this paper’s proposed method is that the self-refinement technique performs poorly, with overall scores not exceeding 33% and some results falling below random chance. This may stem from ambiguities in defining error types or, as noted in W1, the model’s inability to detect "errors" that are subtle nuances of human language due to its inherent implicitness. How do humans perform on this task?

W3: Given that this work aims to address error detection, it is essential to include results on the model's overall error detection performance—specifically, how accurately it identifies the presence of any error. This should be supported with precision and recall scores to provide a clear measure of effectiveness.

### Questions
Q1: In the dataset construction phase, what is the background of the human annotators? Are they math experts? Please provide more details.

Q2: What is the distribution of the classes in the dataset? Are there descriptive statistics of the size of the dataset along with the number of samples per class?

Q3: Based on the results in Table 3, the authors state in Line 431 that model-generated definitions are better than humans. However, in Line 406, they state that based on Table 5, human-written definitions outperform the other prompting techniques. How are these results related? What is the setting presented in Table 3, then?

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
4

### Summary
The paper proposes a new, challenging, task for LLMs: identifying errors (and especially ambiguity) in math word problems which could be detrimental to learning for human students that try to solve them.
To facilitate this tasks, the authors annotate an existing dataset of MWPs in chinese language consisting of ca. 23k problems with five different error types.
The authors benchmarks various LLMs on the task of identifying such errors and propose a new method that uses iterative prompt optimization and can improve performance.

### Strengths
- The writing and presentation are clear
- The paper tackles and interesting, and challenging, new problem of identifying errors in generated math word problems

### Weaknesses
 - Labeling 5,815 examples seems to be a very challenging and exhausting tasks for annotators, especially since none of the examples were also annotated by another annotator, as all of them received disjoint sets. This raises questions whether the annotators were still able to produce high-quality annotations and it would be important if the authors could clarify how this is ensured.
- The authors also mention that they are “unsure whether the five error types are sufficient” (L145) which might be due to them being established by manually inspecting only 200 examples. It would likely be helpful to either analyze more examples (as shown in L208 some errors only occur very infrequently) or to consult relevant literature, e.g. from the learning sciences.
- The self-optimization algorithm needs to be put better into perspective with related works.
- The experiments are a bit limited in scope, focussing only on proprietary LLMs (GPT-3.5, GPT-4o)

### Questions
- It would be good to back up statements like that ambiguity in questions needs to be reduced (which might be intuitive nevertheless) with literature from the learning sciences that supports them.
- L131: we focus extends -> our focus extends (?)
- Section 3 is titled: “From Math23k to MathError”. I would expect based on the title that it details how the authors construct MathError but the section only describes error types.
- The figure captions are rather short and could be improved, similarly Figure 2 does not have axis labels
- It would be helpful in Fig 1. a) to have a pointer where the start of the algorithm is
- The caption of Figure 2 suggests the y-axis shows the difference between refinement rounds but it actually shows the inverse (similarity)

### Soundness
3

### Presentation
3

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
The paper presents the MathError dataset, an extension of the Math23K dataset that includes error types for each question. The goal is to improve the clarity of questions within the dataset, and to achieve this, the authors define five key factors that form the basis for these error types. After annotating the questions based on these defined error types, the paper presents various prompting strategies that focus on self-optimization/reflection to evaluate how different LLMs perform in detecting these errors. The findings indicate that combining model-generated definitions of error types with human-provided examples can enhance the LLMs' performance in identifying the defined error types.

### Strengths
1. The research question studied in the paper is both interesting and important.
2. The experiments are thorough and cover various prompting scenarios and models.

### Weaknesses
1. The related work section is not thoroughly covered. Many studies have proposed various methods for self-reflection/evaluation, which were not mentioned in the paper.
2. Using only one annotator per batch of 5,815 makes the annotations prone to bias toward certain error types.
3. Although the paper addresses an interesting and important problem, I am not convinced that the proposed error types for improving clarity will achieve this effectively. Specifically, three out of the five items listed in Section 3 as factors for enhancing clarity seem to have the opposite effect:
- 3.1. Multiple Interpretations: When a question allows for different approaches to reach the final answer, it can actually make solving it easier for students. This flexibility increases their chances of finding a solution.
- 3.2. Informal Wording: Formal language does not always improve clarity. In the context of elementary school math questions, which the paper focuses on, using less formal language may help students understand the questions more easily.
- 3.3. Calculation Error: In the example provided on line 215, the phrasing “6000 divided by 59, and then subtract 35 from this result” is indeed difficult to interpret, as this form is uncommon. Additionally, it is unclear whether the question refers to regular division or floor division. By contrast, the original phrasing, "the difference between 6000/59 and 35," is far clearer and more familiar. Moreover, based on the paper, the goal of this factor is to address cases where "imprecise words are used to describe a mathematical expression." However, in this example, the mathematical operation is already there, so it is unclear what specific problem this factor intends to resolve.

  Given the aforementioned limitations in how clarity is evaluated, I believe the impact of this study on real-world applications may be minimal.
4. While the proposed method (PRO) is straightforward, the presentation in Section 5 is so awkward that it is impossible to understand the method without referring to the provided algorithm/figure.
5. Since the paper used the `GPT-4o` checkpoint, the results are likely not reproducible. This is because the `GPT-4o` checkpoint continues to receive updates and is not part of the isolated checkpoints designated for research purposes. Therefore, the results obtained may not be reliably reproduced.

### Questions
**Suggestion:**
1. Line 258: LLMs do not possess understanding or consciousness. Therefore, they do not have comprehension capability.

### Soundness
2

### Presentation
2

### Contribution
1
