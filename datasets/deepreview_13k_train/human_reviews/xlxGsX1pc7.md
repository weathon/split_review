# U-MATH: A University-Level Benchmark for Evaluating Mathematical Skills in LLMs

- Decision: Reject
- Scores: 5, 6, 5, 5

## Abstract
The current evaluation of mathematical skills in LLMs is limited, as existing benchmarks are either relatively small, primarily focus on elementary and high-school problems, or lack diversity in topics. Additionally, the inclusion of visual elements in tasks remains largely under-explored. 
    
    To address these gaps, we introduce \textbf{U-MATH}, a novel benchmark of \textbf{1,100} unpublished open-ended university-level problems sourced from teaching materials. It is balanced across six core subjects, with  \textbf{20\% of multimodal problems}. Given the open-ended nature of U-MATH problems, we employ an LLM to judge the correctness of generated solutions. To this end, we release \textbf{$\boldsymbol{\mu}$-MATH}, a dataset to evaluate the LLMs' capabilities in judging solutions.

    The evaluation of general domain, math-specific, and multimodal LLMs highlights the challenges presented by U-MATH. Our findings reveal that LLMs achieve a maximum accuracy of only 63\% on text-based tasks, with even lower 45\% on visual problems. The solution assessment proves challenging for LLMs, with the best LLM judge having an F1-score of 80\% on $\boldsymbol{\mu}$-MATH.

    \ificlrfinal
         We open-source U-MATH, $\boldsymbol{\mu}$-MATH, and evaluation code on GitHub.\footnote{\url{https://osf.io/jpsa4/?view_only=d588b9fa862345cb98ccf7238a157cea}}.
    \fi

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the U-Math datasets, based on university-level mathematics, addressing the issues of insufficient thematic diversity and a lack of visual information question types in current datasets for evaluating the mathematical abilities of large language models. The U-Math datasets was tested on several large language models, revealing that the highest accuracy for text-based tasks was only 53%, while the highest accuracy for visual tasks was only 30%.

### Strengths
1. The paper is well-organized, providing a clear outline of the datasets, experimental setup, and evaluation metrics. The authors explain each component in a structured manner, making it accessible to readers.

2. The datasets include a range of mathematical subjects and problem types, which reflects an effort to cover diverse aspects of mathematical reasoning, though the depth and breadth could still be improved.

3. The introduction of U-MATH and µ-MATH provides additional benchmarks for evaluating LLMs in mathematical tasks, which may offer a reference point for similar studies.

### Weaknesses
1. Although the U-MATH datasets consists of 1,125 samples and covers six subjects, the sample size is still too small. Evaluating the mathematical abilities of large models using a limited amount of data is not sufficiently convincing. The dataset's coverage of advanced topics within each subject also appears limited, potentially missing crucial areas of mathematical reasoning required at the university level. For example, while calculus is included, the dataset might lack problems involving multivariable calculus or differential equations, which are standard in many undergraduate programs. Similarly, linear algebra problems might not extend to more abstract concepts like vector spaces or linear transformations, thus limiting the assessment of LLMs on these topics.

2. Although the 340 samples in the µ-MATH datasets have been carefully selected to provide a challenging test, a larger sample size could enhance the representativeness of the evaluation, especially across different topics and problem types. The current size may not adequately capture the variability in problem-solving strategies and the nuances of mathematical reasoning. For instance, the dataset might be skewed towards certain types of problems, such as those requiring direct computation, while underrepresenting problems that demand more abstract or proof-based reasoning. This imbalance could lead to an incomplete picture of the models' true mathematical capabilities.

3. In Table 4, you only use accuracy to present the results. Since the study involves math problems, which are more complex than simple classification tasks, could you consider adding additional evaluation metrics like perplexity or WinoGrande ACC (to assess whether ambiguous problems are correctly identified)? This would give readers a clearer picture of how well the models truly understand and respond to university-level math questions. For more details, you might refer to examples in this paper: https://proceedings.mlr.press/v235/dao24a.html.

### Questions
1.It is recommended to expand both the U-MATH datasets size and the number of subjects.

2.It is recommended to expand the µ-MATH datasets size.

3.In Table 4, you only use accuracy to present the results. Since the study involves math problems, which are more complex than simple classification tasks, could you consider adding additional evaluation metrics like perplexity or WinoGrande ACC (to assess whether ambiguous problems are correctly identified)? This would give readers a clearer picture of how well the models truly understand and respond to university-level math questions. For more details, you might refer to examples in this paper: https://proceedings.mlr.press/v235/dao24a.html.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces U-MATH, a comprehensive university-level mathematical benchmark designed to evaluate the performance of Large Language Models (LLMs) in solving advanced mathematical problems. The dataset consists of 1,125 problems sourced from university coursework, covering six core topics such as Algebra, Calculus (Differential and Integral), Multivariable Calculus, Sequences, and Series, with approximately 20% of the tasks involving visual components. To complement the U-MATH dataset, the authors also present µ-MATH, a meta-evaluation set for assessing the accuracy and reliability of LLM-based evaluators.

### Strengths
S1. The inclusion of university-level problems offers a significant advancement over existing datasets that mainly focus on elementary or high school-level tasks.

S2: By integrating visual tasks alongside traditional textual ones, the dataset challenges LLMs to interpret and reason across multimodal formats.

S3: µ-MATH introduces a novel approach to evaluate LLMs' ability to assess solutions, addressing biases and limitations in current evaluation practices.

### Weaknesses
W1: The reliance on LLMs as judges (e.g., GPT-4o) to evaluate free-form answers could introduce biases and inconsistencies, particularly since LLMs may struggle with complex derivations or nuanced interpretations of mathematical expressions. The potential for these biases is significant, as LLMs might favor solutions that align with their training data or exhibit specific patterns, rather than strictly adhering to mathematical correctness. This is especially concerning for advanced mathematical problems involving intricate steps where a slight deviation could lead to an incorrect result, yet might be overlooked by an LLM judge due to superficial similarities to correct solutions.

W2: The µ-MATH set includes LLM-generated solutions, which may limit the diversity and challenge of evaluation due to inherent model tendencies or training biases. This could result in less rigorous meta-evaluation as models may overfit to known patterns or heuristics. The use of LLM-generated solutions introduces a risk of circularity, where the evaluation set reflects the biases of the models being evaluated, rather than providing an objective benchmark. Specifically, if the LLM-generated solutions are not sufficiently diverse, the meta-evaluation might not accurately assess the robustness of LLM evaluators across a wide range of solution styles and approaches.

### Questions
What measures have been taken to mitigate potential biases introduced by using LLMs as judges for solution correctness?

### Soundness
2

### Presentation
3

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
The authors introduced a new benchmark dataset, U-MATH, designed to evaluate large language models (LLMs) on university-level math problems. The proposed U-MATH benchmark includes 1,125 college-level math problems collected from real educational materials, covering six core mathematical subjects, with 20% of the problems involving image understanding. Additionally, the paper introduces a meta-evaluation dataset named µ-MATH, aimed at assessing the ability of LLMs to judge the correctness of mathematical solutions.

### Strengths
1.U-MATH Benchmark: This is a publicly available dataset of university-level math problems, covering six topics: Pre-Calculus, Algebra, Differential Calculus, Integral Calculus, Multivariable Calculus, and Sequences & Series. A unique aspect of this dataset is its inclusion of open-ended questions that require LLMs to perform multi-step reasoning.
2.µ-MATH Meta-Evaluation Benchmark: This benchmark is specifically designed to test LLMs’ ability to assess the correctness of mathematical solutions. It contains 340 questions selected from U-MATH, accompanied by LLM-generated answers manually labeled as correct or incorrect, aimed at evaluating the capacity of LLMs to act as “judges.”
3.Model Comparison: The paper compares the performance of various LLMs, including general-purpose models, specialized math models, and multimodal models, demonstrating the significant challenges LLMs still face in both text and visual tasks. For instance, the highest accuracy for text-based questions is 53%, while performance on visual questions is even lower, with an accuracy of only 30%.
4.Challenges for LLMs as Math Judges: LLMs perform poorly when evaluating mathematical solutions, with the best-performing LLM judge achieving an F1 score of only 76% on µ-MATH, indicating that there is still room for improvement in this task.

### Weaknesses
1.The U-MATH dataset introduced in the paper supplements the current math datasets by addressing college-level gaps, while the µ-MATH meta-evaluation dataset enables assessment of large models’ ability to evaluate college-level math solutions. However, aside from knowing that this training set focuses on university mathematics and includes six subjects, we lack information about the dataset’s question diversity, difficulty, reasoning steps required to solve the problems, and other aspects. For example, do the problems within each subject area cover a wide range of topics, or are they concentrated on a few specific areas? Are there problems that require only basic recall, or are most of them multi-step problems requiring complex algebraic manipulation, calculus, or proof techniques? Furthermore, the dataset’s size may be insufficient. It is unclear if the 1,125 problems are enough to adequately cover the breadth of university-level mathematics and to train and evaluate robust models.
2.The paper mentions that the dataset has been released but does not provide an access link, so I have no direct way to review the dataset.
3.The experiments in the paper provide valuable insights into the capabilities of current text-based and multimodal LLMs in solving university-level math problems.
4.The paper states that U-MATH aims to promote further research and improve LLMs' ability to handle complex math problems. How is "complex" defined here? Does it refer to higher-grade, more challenging (for humans) knowledge, or does it mean problems requiring more and deeper reasoning steps?

### Questions
I don't have further questions.

### Soundness
2

### Presentation
2

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
The paper introduces U-MATH, a novel benchmark designed to evaluate the mathematical reasoning capabilities of Large Language Models (LLMs) at the university level. It comprises 1,125 unpublished, open-ended problems sourced from actual teaching materials, balanced across six core mathematical subjects, with 20% of the problems requiring image understanding. Additionally, the paper presents µ-MATH, a meta-evaluation dataset aimed at assessing the ability of LLMs to evaluate free-form mathematical solutions. The experiments conducted reveal significant challenges in advanced mathematical reasoning and visual problem-solving, with the best-performing models achieving only 53% accuracy on text-based tasks and 30% on visual problems. The paper also highlights the difficulty LLMs face in assessing solutions, with the highest µ-MATH F1-score being 76%, indicating room for improvement in LLMs’ evaluation capabilities. The datasets and evaluation code are open-sourced to facilitate further research.

### Strengths
The paper demonstrates a high-quality collection of problems that are well-balanced across six core mathematical subjects. This ensures a comprehensive evaluation of LLMs across different areas of mathematics.
The problems sourced from actual teaching materials add a layer of authenticity and practical relevance to the benchmark, ensuring that the skills assessed are applicable to real-world academic standards.
The creation of µ-MATH for meta-evaluation is an innovative approach to assessing the ability of LLMs to evaluate mathematical solutions. This adds another layer of complexity and originality to the benchmarking process, focusing not just on problem-solving but also on the assessment capabilities of the models.

### Weaknesses
While the inclusion of visual elements in 20% of the problems is a step forward, the remaining 80% are text-based. The paper could benefit from expanding the visual problem set to better assess and train LLMs in multimodal mathematical reasoning, which is increasingly important for real-world applications.

The paper focuses on university-level mathematics, but it is unclear how well the findings generalize to other levels or types of mathematical reasoning. Future work could explore the transferability of the models trained on U-MATH to other mathematical domains.

### Questions
Why are there no examples of problems that require visual input?

The accuracy when using LLM as a judge is not provided, especially for higher mathematics problems where answers may be in different forms but are actually equivalent, indicating that it is easier to make mistakes compared to comparing a single form of answer.

### Soundness
2

### Presentation
2

### Contribution
2
