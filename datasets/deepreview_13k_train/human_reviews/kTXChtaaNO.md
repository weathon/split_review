# StringLLM: Understanding the String Processing Capability of Large Language Models

- Decision: Accept
- Scores: 8, 6, 6, 5

## Abstract
String processing, which mainly involves the analysis and manipulation of strings, is a fundamental component of modern computing. Despite the significant advancements of large language models (LLMs) in various natural language processing (NLP) tasks, their capability in string processing remains underexplored and underdeveloped. To bridge this gap, we present a comprehensive study of LLMs' string processing capability. In particular, we first propose \emph{StringLLM}, a method to construct datasets for benchmarking string processing capability of LLMs. We use StringLLM to build a series of datasets, referred to as \emph{StringBench}. It encompasses a wide range of string processing tasks, allowing us to systematically evaluate LLMs' performance in this area. Our evaluations indicate that LLMs struggle with accurately processing strings compared to humans. To uncover the underlying reasons for this limitation, we conduct an in-depth analysis and subsequently propose an effective approach that significantly enhances LLMs' string processing capability via fine-tuning. This work provides a foundation for future research to understand LLMs' string processing capability.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
First comprehensive study of string processing capabilities of LLMs. Aside from just evaluating, authors also proposed specific solutions (via fine-tuning) to improve their capabilities. Critically, while this fine-tuning does improve their string processing capabilities significantly, it does not majorly harm their general-purpose aibilities.

### Strengths
This work handles a very specific problem, and it does so well: well-principled, reasonable evaluation, and useful solution. The analysis of the errors is also interesting.

String processing capabilities have an indirect effect on all LLMs tasks, and a direct effect on some of them, so this work is clearly relevant.

Additionally, given the fact that authors are willing to publish data and code, this works seems reproducible.

### Weaknesses
The main source of LLMs struggle with string processing is tokenization (this is not news). Given that, I'd have liked to see more studies on tokenization. Perhaps pretraining small LMs on different tokenization strategies.

The presentation of this paper is good enough, but it doesn't have the excellence on this aspect one would like to see on an ICLR paper. For example, Figure 2 is very relevant to the message of the paper, yet it's badly formatted/presented.

### Questions
Please rethink Figure 2. Same data, same basic idea, but better presentation. For example, do we really need 2 digits for the decimals on b)? Do we even need numbers there at all, given the colors?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
1. The authors presented a methodology to construct a large scale string manipulation dataset, consisting of sets of (question, code, answer) tuples. This is done by first hand crafting a set of code templates, then generate natural language instruction templates describing the code template using GPT, and finally getting the final answers by filling in variables with different types of strings and executing those code.
2. They presented an analysis attempting to explain why LLMs struggle with string processing tasks.
3. They demonstrated that fine-tuning improves LLM performance on this task.

### Strengths
1. I appreciate the effort to address this problem. This seems like a useful benchmark for improving LLMs code generation ability for string manipulation
2. They presented a clever way of leveraging closed source LLMs for constructing a dataset, and made a good and thorough effort at demonstrating that it poses a challenge to current LLMs.
3. They showed PoT fine-tuning helps without hurting performance on other NLU tasks.

### Weaknesses
The authors only reported performance on MMLU/ARC/HellaSwag and show that it only degrades a little. I think since this is finetuned on code gen specifically for string manipulation, this should also be benchmarked on code generation benchmarks such as HumanEval, MBPP, CoNaLa, or the newer BigCodeBench/EvalPlus to make sure it doesn't hinder performance in those areas.

In section 5.2. authors claimed that since there is no observable diagonal pattern in the embedding similarity matrix in figure 2b, it suggests that token embedding lacks information on character-level token length. I fail to see how this is the case.

Consider a toy example with just 4 tokens. Let's design the embedding s.t. it is 2d and the first dimension always encode the character length. Let's say these four vectors are (grouped by character length) E1 = [[1,1],[1,-1]] and E2=[[2,2],[2,-2]]. By definition we would get Sim(E1,E1) = 0, Sim(E2,E2)=0, but Sim(E1,E2)=0.5, where there is NO diagnoal pattern, but by construction it captures character level token length.

Maybe the authors can consider proposing an alternative analysis to strengthen their claim that tokens lack character level information.

### Questions
Overall, I think the paper made some good contributions, but there are some missing experiments. I am happy to revise my evaluation based on author response.


Below is just a small nitpick, though to me it doesn't really undermine the contribution of the paper, since they mainly used PoT to get around the problem.

In section 5.2. authors claimed that since there is no observable diagonal pattern in the embedding similarity matrix in figure 2b, it suggests that token embedding lacks information on character-level token length. I fail to see how this is the case.

Consider a toy example with just 4 tokens. Let's design the embedding s.t. it is 2d and the first dimension always encode the character length. Let's say these four vectors are (grouped by character length) E1 = [[1,1],[1,-1]] and E2=[[2,2],[2,-2]]. By definition we would get Sim(E1,E1) = 0, Sim(E2,E2)=0, but Sim(E1,E2)=0.5, where there is NO diagnoal pattern, but by construction it captures character level token length.

Maybe the authors can consider proposing an alternative analysis to strengthen their claim that tokens lack character level information.

### Soundness
2

### Presentation
2

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
This paper is concerned with the string processing abilities of large language models, and the paper introduces a novel benchmark for quantifying string processing abilities. The benchmark is used to compare a number of existing models, and it is shown that finetuning can improve the performance of models on the benchmark.

### Strengths
The paper present a new benchmark for quantifying string processing abilities of large language models. This is a novel contribution that may be helpful to rank and select models for certain types of practical applications.

### Weaknesses
The claim regarding the multilinguality of the dataset is not convincing, since it only pertains to the strings and not the questions in the dataset.

There are some redundant material in the paper, e.g. the section on how LLMs analyze input text via Transformers can be removed since it is common knowledge in the community, and so is the cosine similarity.

I do not agree with the intuition that the token embeddings should contain information about token lengths, and as such the results in section 5.2 are not very surprising. Even so, I do not agree with the conclusion that this explains why models fail to perform string processing tasks, since my intuition is that this is more or less completely dependent on tokenization.

The paper shows that results can be improved by finetuning, but there are no comparison with alternative approaches that operate on the tokenizer level rather than updating the whole model.

### Questions
How much of the current weaknesses of models to handle string processing tasks is related to relatively simple facts and practices related to tokenization? For example, how would if affect the results if all strings in the test data were replaced with string that featured white space between all characters?

Regarding multilinguality, even if the data contains strings from different languages, all questions are still in English. Would it not make sense to also include multilingual instructions in the data if the goal is to measure multilingual capacity?

The experiments in section 6 includes the use of some general-purpose datasets. What would happen if these were not included? The conclusion in this section states that "our finetuning not only enhances LLM's string processing ability but also preserves their foundational capabilities". But one suspects that this is only due to having included the general-purpose datasets in the finetuning?

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
This paper proposes a set of new tasks (and a method to generate the datasets) to evaluate LLMs on string operations. String operations have been a challenge since the beginning of LLMs. In this paper, a method based on GPT-4o is proposed in order to generate large sets of evaluation data for string operations. Instead of asking the model directly, they leverage the high programming capabilities of GPT-4o to generate a program that performs the string operations, and in that way, generates the corresponding input-output pairs correctly. Regarding the evaluation, they evaluate a battery of LLMs ranging from GPT-4o to open-source alternatives like Mistral and Llama. The result suggests, as previously expected, that the LLMs struggle with character-level operations, particularly for random strings and hashes.

### Strengths
* The paper presents a clear experimental setup with problem definition, automatic dataset generation, and model evaluation. 
* The paper is well-written and easy to follow.

### Weaknesses
 * The major weakness of this paper comes from the motivation: it is well known that LLMs struggle with character-level operations, because, as they mention, the tokenization process removes the information about the characters. One may ask why you would ask an LLM to perform such operations, and I think it is not properly reflected in the introduction of the paper. From another perspective, they made use of an LLM to generate the evaluation dataset, which means that an LLM is capable of performing string operations, even though not directly (executing the code the LLM themselves generate). So, would not be a solution for the problem you present to provide an LLM the ability to use a Python interpreter or a predefined set of functions? I think the paper will be more strong if these problems are addressed.

### Questions
* **Q1**: Why is the human baseline so low when it comes to string operations in the Multilingual setting?

### Soundness
2

### Presentation
3

### Contribution
2
