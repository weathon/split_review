# AI-Assisted Generation of Difficult Math Questions

- Decision: Reject
- Scores: 3, 5, 3, 6

## Abstract
Current LLM training positions mathematical reasoning as a core capability. With publicly available sources fully tapped, there is an unmet demand for diverse and challenging mathematics questions. Relying solely on human experts is both time-consuming and costly, while LLM-generated questions often lack the requisite diversity and difficulty.  We present a design framework that combines the strengths of LLMs with a human-in-the-loop approach to generate a diverse array of challenging math questions. Initially, leveraging LLM metacognition skills~\citep{Didolkar2024MetacognitiveCO}, a strong LLM is used to extract core ``skills'' from existing math datasets.  These skills serve as the basis for generating novel and difficult questions by prompting the LLM with random pairs of core skills that must be utilized in the question. The use of two very different skills within each question makes finding such questions an ``out of distribution'' task for both LLMs and humans. Our pipeline employs LLMs to iteratively generate and refine questions and solutions through multi-turn prompting. Human annotators then verify and further refine the questions, with their efficiency enhanced via further LLM interactions. Applying this pipeline on skills extracted from MATH dataset~\citep{hendrycks2021measuring} resulted in \textbf{MATH$^2$} - a dataset of higher quality  math questions,
as evidenced by:
(a)  Lower performance of all models on MATH$^2$ than on MATH
(b) Higher performance on MATH when using MATH$^2$ questions as in-context examples. 
Although focused on mathematics, our methodology seems applicable to other domains requiring structured reasoning, and potentially as a component of {\em scalable oversight}.
Also of interest is a striking relationship observed between models' performance on the new dataset: the success rate on MATH$^2$ is the square on MATH. This suggests that successfully solving the question in MATH$^2$ requires a nontrivial combination of two distinct math skills.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work proposes a AI-based framework that could be applied in generating challenging mathematical questions at scale. Specifically, the framework first extracts mathematical skills from the questions, and generates new questions by pairing up a given skill and a randomly sampled skill (LLMs get involved in estimating the skills being too similar). The questions are filtered by asking LLMs to solve or identify flaws (first tries to estimate the quality from several dimension, then re-solve the questions being qualified), and the filtered questions are passed into human screening. In this manner, a dataset called MATH^2 with questions originated from MATH is collected and a performance law is observed between MATH and MATH^2 in several strong LLMs (performance in MATH^2 is approximately the square of performance on MATH). Besides, it is found that problems in MATH^2 serve as more effective in-context learning examples for solving questions in MATH.

### Strengths
An AI-based framework in accelerating the data generation of mathematical reasoning and interesting observation for the performance dependency between the newly generated MATH^2 dataset and the original one.

### Weaknesses
Several metrics are missing to better understand the pipeline (e.g. number of questions being filtered out in each stage of the framework, sample skills outlined in the skill extraction stage). Besides, it is not measured whether the the generated questions faithfully integrate the skills mentioned (it is not hard to imagine that for challenging problems, the number of skills involved would exceed two). The qualification of humans getting involved for screening is not introduced. If the entire correctness is still highly depend on the final screening, extending it to the scalable oversight scenarios would still be challenging.

For the experimental results, the explanation of the pseudo square law seems to stand under the assumption that the mathematical skills evolved are orthogonal and of under similar difficulty levels, which may holds for specific datasets. Further evidences are needed to understand the meaning represented by this square-law phenomenon found.

### Questions
- I cannot interpret the information in Figure 5.

Typo
- 'creators' in line 319

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper proposes a human-AI collaborative framework for generating challenging mathematical problems. The approach begins by identifying core skills from existing math questions and then prompts LLMs to create difficult questions that combine pairs of these skills. 
The generated questions are then solved by the models, with the framework filtering out invalid ones based on QAs before proceeding to further human annotation. This process results in the Math$^2$ dataset, which includes 210 difficult questions. Evaluation on Math$^2$ reveals that model performance significantly declines, approximately in proportion to the square of the performance on the original MATH dataset. The results also suggest that these new questions can serve as more effective in-context example.

### Strengths
1. This work focuses on an AI-assisted framework for generating harder questions that models themselves struggle to solve. This is potentially of interest to the community, as many existing evaluation benchmarks are becoming saturated, often only reflecting model performance in overfitted domains.
2. The proposed framework results in the creation of a more difficult dataset, MATH$^2$, offering a new benchmark for evaluating mathematical reasoning abilities.
3. The content is clear and easy to follow. The experiments provide comprehensive evaluations across multiple models, demonstrating that the questions are indeed challenging. Additionally, the correlation between performances on MATH and MATH$^2$ is an interesting finding.

### Weaknesses
1. One major weakness is the generalizability of the proposed framework. Around 66% of AI filtered QAs need further human editing. This reliance on human annotation may impact the scalability and generalizability of the framework.

2. As an evaluation benchmark, the dataset is relatively small and lacks comprehensive coverage. Line 412 mentions that the dataset has not covered all possible skills. Given that the questions are initially generated automatically, it would be beneficial for the dataset to cover a broader range of skill sets.

3. The data generation framework is not resource efficient due to the high number of API calls involved. It would be helpful if the authors could provide an analysis of the resource costs for creating the dataset.

### Questions
1. Line 253: It is stated that if all the answers obtained are unique, the question is discarded. Could this indicate that some questions are too difficult to solve, leading to the discarding of extremely challenging questions?
2. The remaining questions are extremely few, so I am curious how many questions are filtered out at each step shown in Figure 1. What percentage of questions pass the filtering process?
3. Out of the 210 questions in MATH$^2$,what is the accuracy split between questions generated directly by the framework (210-139=71) and those further modified by human annotators (139)? Is the performance lower on the human-modified subset?
4. Line 75-76: Missing references for the findings
5. Line 322-323: Missing references for the models mentioned

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a framework for generating challenging mathematical questions using a hybrid approach that combines LLMs with human verification. Recognizing the limitations of both human-generated and purely LLM-generated math problems, the proposed method aims to address the need for diverse and difficult questions. It uses LLMs to generate questions requiring the combination of two distinct mathematical skills and employs a multi-turn interaction system to refine these questions. Human annotators then review and adjust the questions to enhance clarity and difficulty. This process generated the "MATH^2" dataset, which proved to be more challenging for existing models than the baseline MATH dataset and also served as effective in-context training exemplars, thereby enhancing LLM performance on other datasets.

### Strengths
- The paper is well-structured and easy to follow
- The example generation pipeline can be extended to other structured reasoning domains and could be valuable to the research community
- Experimental results show that the generated examples are more challenging for existing models than the baseline MATH dataset and also served as effective in-context training exemplars

### Weaknesses
 - The description of step 5 in Section 2 lacks clarity. The authors should provide more detail about the human re-validation process. For instance, do the human validators create their own solutions first and then compare them with those generated by the model? Additionally, it would be helpful to know the qualifications of these human experts, as the MATH dataset poses significant challenges, even for college-level students

I list some minor concerns in the questions section

### Questions
- Why aren’t human experts involved in the steps of solution attempts and question validation? Could this result in challenging but valid examples being filtered out?
- The authors might consider adding a comprehensive, step-by-step example for each stage in Section 2. This could significantly enhance readers' understanding of the pipeline’s specific implementation details and workflow, making it easier to grasp the mechanisms behind each stage of the generation process.
- How do different base LLMs in the pipeline impact generation performance? For instance, are models with stronger reasoning capabilities more likely to produce "valuable" examples?
- Will the model perform better on questions it generates itself compared to those produced by other base LLMs in the pipeline?
- What is the benchmark performance of human experts on the MATH2 dataset?
- What is the estimated time to generate a single example of similar difficulty to those in the MATH dataset under a human-in-the-loop setting?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a framework for generating challenging math questions using Large Language Models (LLMs). The process involves extracting skills from existing math questions and combining two different skills to construct new questions. Their curated dataset, "MATH^2," consistently shows lower performance compared to the original MATH dataset, exhibiting a square relationship with MATH accuracy.

### Strengths
The paper is well-structured and clearly written.

The motivation to use LLMs for generating more difficult questions to evaluate these models is a promising direction. This paper represents a good attempt.

The performance of MATH^2 demonstrates that it is a challenging dataset, which can benefit research on math generalization and evaluation.

### Weaknesses
The dataset construction still requires human intervention to modify or verify correctness, which is not scalable.

A main concern is the "out-of-distribution" aspect. If we simply combine two questions from the MATH dataset, solving both questions correctly implies a squared accuracy,(it is not an out-of-distribution scenario). Therefore, as the MATH^2 achieve similar performance, does MATH^2 truly represent an out-of-distribution dataset?

### Questions
See the Weakness

### Soundness
3

### Presentation
3

### Contribution
4
