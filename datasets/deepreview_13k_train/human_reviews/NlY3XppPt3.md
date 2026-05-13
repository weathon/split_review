# Improving AI via Novel Computational Models and Programming Challenges

- Decision: Reject
- Scores: 3, 1, 1, 3

## Abstract
AI, like humans, should be able to adapt and apply learned knowledge across diverse domains, such as computational models, mathematical/formal systems, and programming languages to solve problems. Current AI training often relies on existing systems, which limits its ability to generate original solutions or generalize across unfamiliar contexts. To address this, we propose a new computational model along with a revised programming language tailored to this model. By challenging AI to write, analyze, or verify programs within these new frameworks, and by utilizing a virtual machine for evaluation, we aim to test and enhance the AI's adaptability and problem-solving capabilities in a verifiable manner.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a new machine model with the goal of using it as a benchmark to evaluate large language models. The machine model uses decimal instead of binary, and the paper presents empirical results on a variation of the C language running on this machine. The empirical results are clear failure cases for all large language models tested.

### Strengths
The underlying goal of this work is to create test cases that would push the capabilities of large language models to the limit. This is a valid and important endeavor.

### Weaknesses
The paper feels somewhat unfinished. It introduces a machine model and shows that state-of-the-art LLMs fail in solving programming problems using a variant of C in this machine. It feels unfinished because I am not sure what to conclude from the experiments. The value of knowing the outcome of the experiments is on the low end of a paper contribution.

The paper would feel complete if the authors managed to explain why using this machine model is interesting, as opposed to other ways of "breaking a large language model." For example, the work coming out of Subbarao Kambhampati's group shows different ways of breaking these models by using classical planning. Other simple examples, this time related to programming problems, include changing the names of the functions used in an API. For example, instead of using an API with concrete function names such as *multiply*, one could replace them with cryptic names such as *x1* and *x2*. This will also break these models. What is special about a new machine model? What are we hoping to learn from it that we can't learn from more simple ways of making these models struggle?

### Questions
Please see the questions in the weaknesses box.

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This manuscript introduces an approach for testing the generalisation ability of language models, by instructing them to complete tasks in a novel computer programming language that they have hopefully, likely not seen before. To ensure that the programming language is not part of the language model's training set, this language is based on a slightly esoteric computer architecture that is unlikely to exist "in the wild".

The authors go on to show that a number of representative frontier models cannot solve relatively simple problems in this novel language, even when given a (zero-shot) specification of the language in their prompt.

### Strengths
This paper correctly identifies generalisation of models to unseen circumstances as a critically important facet of progress. In my opinion, their focus on generating computer programs is a productive way to probe models' generalisation abilities.,

### Weaknesses
The paper's main weaknesses are that: their "novel computational model" is not very interesting; and that the investigation into the performance of the frontier models is quite superficial.

On the computational model: the model that the authors introduce only really changes the semantics of the language in terms of the maximum size various variable types can hold. In my opinion, this isn't a particularly interesting change. While it does lead to meaningful differences between their introduced language and standard C, the differences are rather fussy and relate to edge cases rather than fundamental differences in the computational model. Indeed, one could argue that this isn't really a different computational model at all, as claimed, but just an esoteric programming language with unusual variable types and an odd string formatting function. I don't feel as though this novel language provides an interesting test of LLM reasoning capabilities.

On the investigation depth: the authors use a single, zero-shot prompt to generate code from the language models for three separate programs, and show that this does not lead to correct programs. But I think to conclude anything robustly a much more thorough analysis is needed. Most critically, I think it would be important to try few-shot prompts, where some correct examples in they authors' introduced programming language are provided. I would also like to see evaluation on a larger number of problems.

There are a number of other, less significant weaknesses in the manuscript:

The discussion, section 4, is difficult to understand. There are several places where there seems to be a confusion between the process an algorithm uses to solve a problem, and the process a human uses to design algorithms. I don’t know whether the intention was to draw parallels between these topics, but the result is that this section seems rather confused, and I don’t think it supports the work in the paper. It doesn’t really seem to have anything specifically to do with the results presented. It would be better to directly discuss the relevance of the results in this section than discussion broad generalities.

Section 5, related work, seems to be a very broad collection of papers, and I wouldn’t say that they are all related except in a very general sense. This section should only cite papers that are of direct relevance, and should make clear how they are of direct relevance. (E.g. there’s a paper on quantum machine learning, which certainly has very little to do with this manuscript.)

I note that it appears that the problem specification provided to the LLM in Case 1 (find the first three digits) does not match that described in the text (calculate the number). This suggests that the prompt fed to the language models may have had some differences than the one in the paper.

### Questions
I note that the setting for the Wuxing machine has a similar tone to some of the ICFP Programming Contest problems. The authors might enjoy participating in it if they do not already! https://icfpconference.org/contest.html

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
The paper proposes a new benchmark for testing the understanding of LLMs. They do this by taking computing/coding problems that LLMs can solve today, and recasting them in a new computing language with unusual properties. Then they check whether today's LLMs can solve these problems in the new computing language, and find they generally can't.

### Strengths
The idea of benchmarking on familiar tasks with unusual computing language is a good one, and is well tested in this paper. Apart from the abstract and title, the presentation is clear and the results seem sound (if the abstract and title were different, I would have given 3 (good) scores to both soundness and presentation above).

### Weaknesses
The abstract is actively misleading. While not saying anything technically untrue, it gives the strong impression that the paper's results are much more substantive than they are. The abstract implies that they are not just presenting a benchmark to measure LLM performance, but a method to directly improve this performance. The title is misleading about this as well.

### Questions
The current abstract and title are unacceptable, and need to be entirely changed.

I am rating this paper as "1: strong reject". But if the title and abstract were changed, and if it was established that the original versions were innocent errors rather than fraudulent claims, I would rate the paper as "6: marginally above the acceptance threshold."

### Soundness
1

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
This paper investigates the adaptability of LLMs from the perspective of code generation. It proposes a new computer model Wuxing with decimal systems and a corresponding programming language similar to C with modified data types. The paper provides three case studies illustrating the failure of LLMs in adapting to this new  programming framework.

### Strengths
**Originality:** The decimal system proposed helps avoid data contamination and better examine the adaptative capabilities of LLMs. The perspective of code generation makes it easier to verify.

**Quality:** The paper provides a general framework with different task levels from the underlying computational model to programming languages and compilers. 

**Clarity:** The paper clearly states its purposes. Detailed answers of LLMs for the case studies are provided in the appendix.

**Significance:** The problem of adapting knowledge to new scenarios is important.

### Weaknesses
1. **Lack of a clearly defined dataset**. Since the paper is submitted to the primary area of datasets and benchmarks, I would expect to see a complete dataset or benchmark with detailed descriptions of the components. However, as far as I can see from the paper, it only contains three cases. In case I misunderstood the work, could you please include an anonymous link to the complete dataset with clear documentation?
2. **Lack of extensive experiments.** The paper provides three case studies as the only experimental results, which seem to be insufficient for drawing meaningful conclusions. The settings for the experiments are not clearly stated or studied either. 
- Could you clarify the settings of the experiments, such as the benchmarking workflow? For example, whether the experiments were conducted in a zero-shot manner.
- I would also suggest further investigation into few-shot learning, Chain-of-Thought techniques (or even fine-tuning if time permits) to gain deeper understanding of the phenomenon. 
- Experiments with modified prompts stating the syntactic rules of Wuxing with concrete examples might also be meaningful to investigate if this helps improve performance.
3. **The discussion and related work sections could be significantly improved.** Instead of listing (loosely) related work indiscriminately, such as works in quantum computing, it might be better to group the work into key topics related to the paper and discuss their relations with each other and limitations.

### Questions
Questions are raised in the Weaknesses part.

### Soundness
1

### Presentation
2

### Contribution
1
