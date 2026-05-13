# WISDOM: Progressive Curriculum Synthesis Makes LLMs Better Mathematical Reasoner

- Decision: Reject
- Scores: 6, 1, 6, 6

## Abstract
Large Language Models (LLMs) have demonstrated remarkable capabilities across a wide range of problem-solving tasks. Despite their success, LLMs still face significant challenges in complex reasoning, particularly with advanced mathematical problems. These problems require not only a deep understanding of task descriptions but also sophisticated logical and mathematical reasoning to determine the correct solution path, which is often lacking in the existing synthetic data. To address this gap, we introduce WISDOM, which draws inspiration from the human learning process and employs curriculum learning to gradually synthesize high-quality CoT data from easy to hard. Our goal is to guide LLM training and improve reasoning capabilities by progressively exposing models to increasingly challenging problems. Based on the synthesized data, we further fine-tune and develop the WISDOM series models, achieving significant improvements across multiple mathematical reasoning benchmarks. Notably, WISDOM-7B (DSMath) achieves a score of 62.4% on MATH, matching GPT-4’s performance with 2/30 correct answers on AIME2024. Furthermore, WISDOM-70B (Llama3) outperforms GPT-4 on AIME2024 with 3/30 correct answers, demonstrating its potential as a better mathematical reasoner. More data and models will be available at https://anonymous.4open.science/r/Wisdom-math-377B

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study presents a data-centric research endeavor that progressively synthesizes high-quality CoT data from simple to complex. Empirical evidence substantiates the efficacy of the proposed approach.

### Strengths
1. The experiment was meticulously conducted with a wide array of comparative methods.
2. The article is well-written, presenting information in a coherent and easily comprehensible manner.

### Weaknesses
1. The proposed method lacks novelty, as it primarily represents a combination of several well-established techniques, including self-consistency, teacher model distillation, and the use of meta-data to guide data generation.

2. The discussion regarding the difficulty levels of the tasks is insufficient and does not adequately analyze relevant prior work [1].

3. Despite achieving high performance, the proposed data-centric approach faces a fundamental issue: the comparisons made are not entirely fair due to variations in the scale of data used and the differing levels of used prior knowledge.

4. The manuscript does not focus on a clear scientific problem; rather, it resembles an engineering-focused endeavor and lacks the rigor typically associated with scientific inquiry.

[1] Neuro-Symbolic Data Generation for Math Reasoning. NeurIPS 2024.

### Questions
1. How does this paper define easy and hard math problems?
2. Why does the author believe that adding more "easy to hard" data can address complex reasoning, or is it merely a matter of data fitting?

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
WISDOM is a framework for improving the mathematical reasoning capabilities of Large Language Models (LLMs). The framework achieves this through progressive curriculum synthesis. It generates high-quality Chain-of-Thought (CoT) training data in increasing difficulty levels using a combination of weak and expert teachers. Specifically, it has three main stages: weak teacher guiding, critical expert teaching, and experts consistency voting. It also has a mechanism for evolving harder questions. The authors then use this data to create WISDOM series models. The authors evaluate WISDOM on multiple mathematical reasoning benchmarks and show improvements over existing approaches, particularly for smaller models.

### Strengths
This is an interesting paper with some key strengths. The progressive synthesis approach, moving from easy to difficult problems through multiple stages, represents an advancement over existing methods that often treat all problems with equal weight or rely heavily on majority voting.

The authors show that even smaller models (7B-8B parameters) can achieve competitive performance with much larger models on certain datasets when trained using their WISDOM framework. The paper's has thorough ablation studies and careful analysis of different components, including the embeddings. The authors provide detailed investigations into the impact of knowledge base integration, answer consistency, and scaling effects. The authors demonstrate strong performance on challenging out-of-domain problems like AIME2024 and AMC2023. I appreciated the authors' careful attention to data contamination prevention using the 10-gram hash deduplication method.

In terms of clarity, I do appreciate the variety of visuals and the algorithm, but I have many clarity concerns in the weaknesses below.

### Weaknesses
I think there are quite a few areas that I am unclear on or see some overclaiming in.

1. I agree that there is a lack of data in this field. However, I think you need to back up statements like these with citations: “However, open-source datasets only contain a relatively low proportion of high-quality data.” You also have to cite other topics you mention, like in this sentence: “Although the widely adopted Rejection Sampling can generate data without reducing the difficulty level of the instructions, the reliance on ground truth limits its broader applicability.”
2. In Table 2, I recommend that the authors clearly label the y-axis and specify which benchmark(s) the accuracy values correspond to in the figure caption or main text.
3. It should be clear upfront how you measure problem difficulty. I recommend adding a brief explanation in the introduction, potentially with some context of curriculum learning, of how problem difficulty is measured or assessed in your approach.
4. There are many sentences such as that that are very qualitative but not quantitative: “Following curriculum learning principles, we first employ a weak but cost-effective teacher to solve a large number of easy problems. Subsequently, a strong but more resource-intensive expert is used for medium-difficulty questions, thereby optimizing resource utilization.” I am left wondering what medium-difficulty questions mean and what counts as resource-intensive.
5. Overall, I find the methodology section to be confusing. The difficulty progression mechanism needs more detailed exposition. Can you specify how difficulty is specifically measured or controlled across the three stages so I can better understand the progression from "easy" to "hard"? Moreover, the relationship between problem types and difficulty progression requires clarification. It would be valuable to understand whether certain mathematical domains follow different difficulty progression patterns.
6. Additionally, this paper lacks an explanation of the real world use case of WISDOM. Is the expectation that the user use WISDOM to generate data for their own base models? Isn’t this expensive for mathematicians? Or are mathematicians not the target audience?
7. Can you please define the abbreviation "GT-Free" in the table caption or in the text discussing Table 1?
8. What do you mean it “surpasses the 60% threshold for the first time”? Don’t all of the methods in the first 4 rows do the same?
9. It seems that most of the improvement is in AMC2023 and AIME2024. Although you claim SOTA in other benchmarks like College MATH, I wouldn’t say the improvements are “outstanding”
10. Given that Critical Expert Teaching only has a small improvement, can you please justify the inclusion of the Critical Expert Teaching stage? It seems that a big part of your claims is your focus on computational speedup and cost efficiency, so I would like to understand the aspects of this stage that outweigh the computational costs.
11. I don’t see an analysis of “progressing” over time. It seems that you just present at the end of the progressive synthesis.
12. I would also like to see more theoretical analysis of why this works, specifically with reference to theorem proving as as field.
13. Is this really curriculum learning if most advancements are only in the hardest theorems?


Small writing details:
I think the title should say “Mathematical Reasoners” (plural)
“prior arts in mathematical data synthesis” should likely be “prior works in mathematical data synthesis”

### Questions
I already have some questions in weaknesses above, but here are some more:

1. How are you measuring difficulty?
2. What are the computational requirements for implementing WISDOM in practice?
3. The paper claims cost efficiency compared to majority voting, but how does the total computational cost compare to other approaches in the literature?
4. Could you provide more analysis of the failure cases? Understanding where the approach doesn't work well would be valuable.
5. How sensitive is the approach to the choice of weak and expert teachers? What happens if you use different models in these roles?
6. How can users customize the curriculum for their specific needs?
7. Why haven’t you tried this approach with formal mathematics?
8. How have you verified that the answers or proofs are correct?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a synthetic data generation method for mathematical reasoning problems, and shows substantial gains for Llama and Qwen models when fine-tuning on their generated data. The process has 3 stages: one amounting to attempting to solve problems using Chain-of-Thought + Program-of-Thought, the second in using a "weak teacher" model to analyze solutions where CoT and PoT disagreed (and attempt to solve them again), and a third stage where an even stronger model does the same. With GSM8k and MATH as seed datasets, the authors observe substantial gains on MATH (e.g. +27% for Qwen72B) and other datasets not used for training, such as AMC2023, TheoremQA, and the AIME 2024 challenge (often leading to 1-2 extra problems solved, out of 30).

### Strengths
* Synthetic data generation is a very relevant direction to improve current LLMs on hard reasoning tasks
* While the individual ideas are generally not new (related to distillation, expert iteration, self-consistency), this seems to be a particular combination that works well
* The authors provide comprehensive experiments on several base LLMs and datasets. The gains are clear in several cases, and bring the larger open source models (at the 70B scale) close to closed generalist models, like Claude 3 and GPT-4o-0513.
* The authors ablated both the stages of data generation, the use of self-consistency, and the diversity-improving heuristic

### Weaknesses
* The pipeline is quite intricate, and I don't think the authors compared (or cited, if someone has done these before) to the simplest possible data generation methods. Two of these would be the Self-Taught Reasoner [1] method (essentially expert iteration, though it also has a rationalization step) and CoT distillation [2]. I'm not 100% convinced that the whole pipeline is necessary, since overall this amounts to distilling from self-consistency and from GPT-4o.
* The authors don't use the answers in the seed datasets. While this can be seen as a strength (it makes less assumptions), one has to wonder if it wasn't possible to do better, and cheaper, by using the dataset-provided answers, rather than self-consistency. It doesn't seem exactly valuable to me to make an artificial assumption that doesn't hold in either of the seed datasets used in the experiments. The more general pipeline only becomes compelling if you actually apply it to a source of problems that have no answers associated with them (e.g. extracted from more diverse Web sources, problem sets, etc), in which case methods like STaR directly don't apply (though STaR with self-consistency has already been tried, too [3]).
* [Minor] The narrative around curriculum learning is a bit inaccurate (compared to the traditional use of the term in Machine Learning [4]). While I understand there is supposedly an "implicit curriculum" in the questions that different iterations get right, this is not really guaranteed to align with any human-interpretable curriculum. LLMs have been shown to often solve hard questions and still fail to answer easy ones, if difficulty is defined by human curriculum. Curriculum learning generally means that you pre-define a sequence for the training set, according to some external labeling, not to where the model itself succeeds or fails.

[1] Star: Bootstrapping reasoning with reasoning. NeurIPS 2022
[2] Specializing Smaller Language Models towards Multi-Step Reasoning. ICML 2023
[3] Large Language Models Can Self-Improve. EMNLP 2023
[4] Curriculum learning. ICML 2009

### Questions
* What was the actual cost of the experiments? In 3.8.2 (Cost Saving), the authors mention the *saving*, but not the actual cost. It's important to get an absolute estimate, e.g. for each round of MATH on Llama 70B. What would be the comparative cost to just do distillation from GPT-4o directly, maybe with rationalization (as STaR did)?
* Do the authors have examples of a same question that the model initially gets wrong, but gets right after fine-tuning? It would be good to see a few qualitative examples and try to get a sense of how the model's behavior changes over time.

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
4

### Summary
This work applies curriculum learning to guide LLMs in generating synthetic data through the Easy to Hard Cyclic Iterative Process. Based on that, this paper presents a three-stage framework "WISDOM".

### Strengths
1. Unlikely many contemporary works that scale up carelessly, this framework does attempt to be cost effective, mainly by using a weak and cheap teacher model first to solve many simple problems.

2. According to the evaluation results reported, it seems that the synthesized data are of good quality and does help models learn both in-domain and out-of-domain. This generality further proves the effectiveness of their method.

3. The results and analysis are very thorough. The authors not only provided main results but also discussed several factors and how they impact the learning performance.

### Weaknesses
1. In the methodology (Sec. 2.2), it seems that internal consistency (which is obtained as whether the model outputs the same answer via CoT and PoT) has been used as the only indicator of whether the model's response should be treated as correct. No ground truth labels are used here. I think it is quite evident that the self consistency of a single model under two prompting methods is far from a fair replacement of a ground truth. I think either this part of methodology is a critical weakness, or much more analysis is needed here. To be extra clear, I do buy the claim that there is probably a correlation between internal consistency and final accuracy, yet the gap between the two still looks too big for me without further justifications.

2. In the experiments, a number of baseline models are compared, on a set of data. However, the models have different data cutoff dates. Data contamination may be a possibility for some of the models, making the evaluation less fair. I feel data contamination is a very important aspect that worth being analyzed here.

3. A suggestion for the presentation: WISDOM is a good name, but I feel it has been used in a mixed way throughout the paper, which seems confusing at times. In Sec. 2, WISDOM has been used mainly as the framework that synthesizes data, while later in the experiment section, WISDOM is also used to denote the model. I recommend the authors to be clear and consistent with terms in the presentation, especially when it comes to core contributions like this.

### Questions
1. In the internal consistency part, why CoT and PoT are selected as the only two methods to assert consistency?

2. I feel the general iteration strategy looks similar to some more standard methods such as expert iteration in RL. It would be great to have some discussions about the connections, and what specifically in the framework that this paper presents is completely new.

3. As more and more data are generated, is there any negative tendencies worth noting? E.g. problem quality drop or diversity drop? More generally, is there any anticipated challenges when scaling the framework up?

### Soundness
3

### Presentation
3

### Contribution
3
