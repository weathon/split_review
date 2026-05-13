# Language Models, Grade-School Math, and the Hidden Reasoning Process

- Decision: Accept
- Scores: 6, 6, 6, 6, 6

## Abstract
Recent advances in language models have demonstrated their capability to solve mathematical reasoning problems, achieving near-perfect accuracy on grade-school level math benchmarks like GSM8K. In this paper, we formally study how language models solve these problems. We design a series of controlled experiments to address several fundamental questions: (1) Can language models truly develop reasoning skills, or do they simply memorize templates? (2) What is the model's hidden (mental) reasoning process? (3) Do models solve math questions using skills similar to or different from humans? (4) Do models trained on GSM8K-like datasets develop reasoning skills beyond those necessary for solving GSM8K problems? (5) What mental process causes models to make reasoning mistakes? (6) How large or deep must a model be to effectively solve GSM8K-level math questions?

Our study uncovers many hidden mechanisms by which language models solve mathematical questions, providing insights that extend beyond current understandings of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper attempts to measure the reasoning ability of models by training on a synthetic dataset based on GSM8k. Among other things, they show that training from scratch on this synthetic dataset of grade school math has some signs of generalization to harder problems.



Edited: score to 6 after reviewer rebuttal.

### Strengths
Measuring reasoning via training an LLM from scratch is an interesting direction. There are lots of interesting results and experiments in the paper.

### Weaknesses
I think the writing can be improved somewhat. Additionally, I think there are some questions about whether the findings are broadly applicable given a single synthetic eval on GSM8k. In some sense, LLMs are useful because they generalize widely beyond a small set of very specific problems.

"Generalization" from a synthetic dataset to a similar synthetic dataset is not nearly as ideal as generalization to a very different kind of dataset.

### Questions
Q: My big question is whether this is a proper use of generalization, especially with LLMs, which are useful primarily because they generalize to very different kinds of data. "Generalization" from a synthetic dataset to a similar synthetic dataset is not nearly as ideal as generalization to a very different kind of dataset.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper dives deep into how language models solve grade-school math problems. The authors first design an elaborated data generation pipeline to synthesize a large amount of grade-school math problems with a specific form of Chain-of-Thoughts. Then the authors design a probing method to analyse how the language models solve the problems, and acquire some interesting conclusions.

### Strengths
* This paper carries out a substantial experiment (including large-scale data synthesis, fine-tuning, and probing) to systematically research the reasoning ability of LLMs in grade-school math problems.
* To understand how the metal process of language models, the paper proposes a few **probing tasks** which align with human problem-solving strategies. Such probing tasks might be insightful to other works.
* Multiple interesting conclusions are found in this paper.

### Weaknesses
 * **Limitation of specific CoT form**: This paper trains the GPT-2 model using synthetic data with a specific form of CoT. The fune-tuning and probing experimental conclusions are based on such CoT. However, the CoT that is now used to train the LLMs on grade school math problems deviates considerably from this form. This limits the generalizability of the paper's conclusions. Furthermore, the chosen CoT format, which involves explicitly defining intermediate variables (e.g., "Define <param2> as X, so X=..."), lacks readability and intuitive appeal compared to more natural language-based CoT approaches. This artificial structure might not reflect how humans typically approach these problems, potentially skewing the analysis of the model's reasoning process. The conclusions drawn from this specific CoT may not necessarily apply to other forms of CoT, especially those used in state-of-the-art models.
* **Lack of analysis on data quantity**: Although this paper synthesizes a large amount of data to train a language model, some studies have shown that more training data is not always better for language models. I expect to see a curve or table of [model performance - the quantity of training data].

### Questions
1. **Lack of analysis on data quantity**: See the second point in Weaknesses.
2. **About the backward thinking process**: In line 447-453 of this paper, the authors define the “backward thinking process” as “because I want to compute X, but X depends on Y and Y depends on Z, so let me compute Z first”. Moreover, they conclude that this backward thinking process can be autonomously learned through language modeling with abundant data. **I can't understand how the author came to this conclusion**. I cannot understand how the authors arrive at this conclusion.

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
2

### Summary
This work conducts controlled experiments to probe several fundamental questions about math reasoning capability of language models, the experimental results show that language models can solve math problems like humans and conduct backward thinking process.

### Strengths
- This work introduces a framework to generate a set of diverse GSM problems that focus on “logical reasoning” aspect.
- This work finds that “the model has learned to plan ahead, identifying necessary
parameters before starting to generate the solution”.

### Weaknesses
 - The small model size of GPT2-small (100M-200M) may effect the generalization of the experimental conclusion. It would be appreciated if conducted experiments on LLMs with billion parameters.
- The conclusions drawn from experiments on synthetic data may not be applicable to real-world scenarios with large data volumes. The limited diversity in the synthetic data, specifically the four categorizations within iGSM, may not fully capture the complexity of quantitative relationships found in real-world problems. This could lead to an overestimation of the model's reasoning capabilities when applied to more diverse and nuanced datasets.

### Questions
Since IGSM only has four categorizations, which may result in poor diversity in the description of quantitative relationships. Could this affect the generalization of the experimental conclusions of this paper?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper investigates the capability of language models (the authors used the GPT-2 model for their experiments), to solve grade-school math problems to explore whether models genuinely develop reasoning skills beyond template memorization. They address several key questions: Can LMs generalize reasoning skills? Do they replicate human-like problem-solving methods? Are their errors predictable, and does model architecture (depth versus width) influence reasoning abilities?

It is important to control the dataset to explore these questions. For this, the authors generate a synthetic dataset with high template diversity, reducing contamination and ensuring complex, logical dependencies in problems. Results indicate that the model can indeed generalize reasoning processes and even learns dependencies and plans solutions. The paper explores the models internal states through probing to understand how the model is solving the problem. 

Overall, the paper is highly experimental with the goal to identify the factors that enable a model to develop reasoning skills through systematically controlled experiments.

### Strengths
The biggest strength of the paper is the controlled experiments that the authors conducted. Training a GPT-2 model from scratch with their own synthetic data can give them full control over the experiments. Also, generating their own data can prevent contamination of the training test data, which might be one of the problems in the other benchmark data. 

The authors also introduce the probing tasks to explore the internal states of the model, which gives some idea of the reasoning process of the model. In particular, the V-probing approach is interesting because it can tell whether pre-training or fine-tuning was responsible for the probing signal. 

Finally, the paper presents many interesting results, including the depth vs. width of the models, the generalizability of the model to unknown tasks of greater depth, models learning backward reasoning processes like humans, and so on. These results (if they can be scaled) may allow better design of language models in the future and may help to understand the role of synthetic data in learning a concept.

### Weaknesses
The weakness of the paper also lies in the main choice of experiments: the creation of the dataset and the choice of the model. 
- Regarding the dataset, the use of synthetic data may not fully capture the complexity and nuances of real-world mathematical problems. This limitation could affect the generalizability of the results to practical applications. It would be important to mix and match the training dataset with real-world data or test the methodology on some real-world data such as GSM8K.
- Regarding the models, although it is difficult to test the methodology on multiple models, the model performance scales well with depth is kind of a known fact and with more layers, the performance improves creating a question that if scaling leads to memorization?

The use of math word problems is a good choice to control the experiments, but the question is if the results are limited to a structured reasoning problem like math word problems? This is important to know in order to understand the limitations of the approach. 

The analysis of the model errors was omitted from the paper, saying that the authors are writing another paper because it is not good for the current paper. It would be good to see the error analysis. At least a summarized version needs to be presented. 

Finally, since the training of the model was done by the authors, it would be interesting to see in which training iterations the model learned certain skills. This can easily be discussed in the paper, but I found it missing. 

[MINOR] The use of words like AGI while experimenting with synthetic datasets and the GPT-2 model is not correct and can be avoided.

### Questions
It would be interesting to see some results on real-world datasets like GSM8K to see how much the models can generalize to real-world problems when trained on synthetic datasets.

Is it possible to test the models on similar synthetic datasets like mathworld (https://arxiv.org/abs/2306.04347)?

Model errors and how LLMs can fix them (Result 6) needs to be discussed in the paper and not left saying its there in another paper.

The results of the backward thinking process are missing from the paper and saying that the models learned it without any discussion is not correct. It needs to be added to the paper. 

Finally, it would be interesting to see an analysis of when a model learned a particular reasoning skill during training. And can it be learned in a continuous training fashion?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work focuses on evaluating the grade-school level mathematical reasoning of neural language models (GPT models).
The authors set out to explore several critical questions surrounding the actual abilities of LMs to reason mathematically.
To make clear and controllable experiments, the authors introduces a synthetic dataset iGSM.
Using iGSM to train and test GPT-2, the authors argue that the model can truly understand and reason through problems rather than just memorizing instances.
The examination of the causes behind reasoning mistakes made by LMs is another highlight, shedding light on the limitations and potential areas for improvement.

### Strengths
1. Overall, the exploration of the model's hidden reasoning process provides valuable insights into the black-box nature of neural language models.
2. This work introduces a new synthetic dataset iGSM which could facilitate the training and evaluation of contemporary large language models.
3. This work provides many interesting findings. It provides a valuable addition to better understanding the reasoning capabilities emerged in large language models.

### Weaknesses
My major concern is about the generalizability of the conclusions drawn in this work.
It is unclear whether the experimental findings on formal language reasoning can be generalized to natural language reasoning.
The formal language patterns in iGSM are too much limited and inflexible compared with natural language expressions, although it may contain a large number of templates if omitting the primitives in the expressions.

For instance, for the math operation *multiplication*, there are many different ways to express using natural language, e.g., "there are three children in the house and each child eats two eggs for breakfast".
But in iGSM, it seems that *multiplication* is always mapped from "times" in the input expression.
I think for grade-school level mathematical reasoning, one major capability is to map the flexible natural expressions to calculations.
Therefore, I think reasoning on iGSM could be much easier than reasoning on natural language questions.

### Questions
1. Can you provide some evidence to support the generalizability of your conclusions, even some of them?

### Soundness
2

### Presentation
2

### Contribution
2
