# Paramanu-Ganita: An Efficient Pre-trained Generative Mathematics Language Model with Chain-of-Thought Instruction Fine-Tuning

- Decision: Reject
- Scores: 3, 1, 3

## Abstract
In this paper, we pose the following question: whether domain specific pretraining of tiny generative language models from scratch with domain specialized tokenizer and Chain-of-Thought (CoT) instruction fine-tuning results in very competitive performance on mathematical reasoning than LLMs which are trained on trillion of tokens and humongous parameters? Secondly, we pose our second RQ: whether domain specific pretraining from scratch is environmentally sustainable, highly cost efficient? To address these research questions, we present Paramanu-Ganita, a 208 million-parameter novel Auto Regressive (AR) decoder based language model on mathematics. We performed pretraining from scratch on 31.5 billion tokens using a context size of 4096 on a mixed mathematical corpus consisting of mathematical web pages, mathematics related source code such as AlgebraStack, mathematical textbooks, Chain-of-Thought (CoT) templatised mathematical StackOverflow question answers pairs, and mathematical lecture notes in LaTeX curated by us. We also trained a math and code specialised BPE tokenizer. We proposed and performed Chain-of-Thought instruction fine-tuning of Paramanu-Ganita on the MetaMathQA dataset. We evaluate our model on GSM8K and MATH mathematical benchmarks, and on logical deductive reasoning (LogiQA) and multiple choice high school and college level math questions from SAT (AGIEVAL-SAT-Math), GRE/GMAT questions (AGIEVAL-AQuA-RAT), college and high school level math questions from MMLU.
Our model Paramanu-Ganita, despite being 34 times smaller than the 7B LLMs, outperforms general LLMs by approximately 30% points, and even math-specialised LLMs by 3-23% points in GSM8K test accuracy metric. On MATH benchmark, Paramanu-Ganita outperformed the various models by 6-8% points. On other benchmarks such as LogiQA logical deductive reasoning benchmark, mathematical high school level multi-choice questions (MMLU-math-high-school), GRE-GMAT level quantitative questions (AGIEVAL-AQuA-RAT), SAT level math questions, Paramanu-Ganita was better than the others by about 1-4% points. The large significant margin improvement in performance of our math model over the existing LLMs signifies that reasoning capabilities of language models are just not restricted to those with humongous number of parameters. Paramanu-Ganita took only 170 hours of A100 training whereas large LLMs such as the math-specialised LLM, LLEMMA 7B, was trained for 23,000 A100 equivalent hours. Thus, our approach of pretraining powerful domain-specialised language models from scratch for domain adaptation is much more cost-effective and environmental friendly than performing continual training of LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
Authors present a LLM specializing in mathematics, called Paramanu-Ganita. It is quite smaller in size and exhibits interesting performance benefits in several math and logical datasets, compared some LLMs with bigger size. Authors also trained tokenizers from scratch, curate a new dataset for pretraining and show that Paramanu-Ganita outperforms several general-purpose LLMs and some domain-specialist LLMs.

### Strengths
The paper is well-written. I appreciate the background and the description of how the model is trained. The idea of targeting mathematics is important and building LLMs specializing in math (at least some part of it) is important. 

The dataset is an important contribution, however I am not sure whether the authors plan to make it public.

### Weaknesses
I feel the paper explores an interesting direction, but there are some concerns:

1. Firstly, GSM8k tests basic math word problem skills and given the model's GSM8k performance is pretty poor, I do not feel the model is ready yet. I think more experimentation is required. Also, how are Table 2 values computed? It seems the MetaMath paper reports GSM8K performance to be 82.3. Why is it 66.5 here? [1]

2. What is mostly missing from the paper are proper motivations and justification as to what "contributes" or what is expected to contribute to the "improved" performance?

 - Looking at this from a different point of view, why did the authors not start with MetaMath, then say change the tokenizers or change the dataset? Then, slowly demonstrate how all the innovations are truly necessary. At the least such ablations would have showed the necessity of new models.

 - Secondly, given the model's performance is not so great, what are we gaining by spending so much training time and cost?

3. One more important aspect is, what are the domains that the model targets? What are the grade levels? Is it the expectation that we will also do IMO problems starting from GSM8k? Or, are we targeting sub-disciplines algebra, pre-algebra, calculus etc.? I think this depth is also missing, so is related papers that investigate the need of such models [2].

### Questions
Some minor and major questions:
1. Abstract: Concrete examples would be better, such as which model did it beat despite being smaller etc..
2.  L196: Please give examples, what happens for various ways of writing floats. How are the European and US/UK numbers treated 1,43 vs 1.43.  Mixed numbers and digits, other mathematical symbols.  To me, its not so clear from the writing.
3. L210: The architecture description seems incomplete, given its a section. You have mentioned decoders elsewhere, but you should complete this here, mentioning how many layers of decoders (or ranges), how many dense layers, and some block diagrams, referred from the section. This is supposed to be the most important section.
4. L249: Whats the perplexity of other models, especially mathematics specialist or science specialist ones? Can you show a table comparing them? Otherwise, the standalone numbers do not make sense to me.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
The paper introduces PARAMANU-GANITA, a 208 million parameter mathematics-focused language model trained from scratch. The authors demonstrate that effective mathematical reasoning capabilities can be achieved with smaller, more efficient models when trained specifically for the domain. This approach offers significant advantages in terms of computational costs and environmental impact while maintaining good performance.

### Strengths
- Good empirical results despite smaller model size, demonstrating the effectiveness of their approach
- Demonstrates that smaller, more efficient models can achieve good mathematical reasoning performance

### Weaknesses
- The overall presentation of the paper still needs much improvement. The paper is not in ready-to-review or ready-to-submit status. The figures are pretty rough and unclear for what the authors want to express. For example, Figure 2 shows GPU Power Usage during pretraining of Paramanu-Ganita. But what conclusions do the authors want to make here? How does it illustrate the environment friendly nature of the model? For the figure 1, what does the blue line mean here?
- Limited Ablation Studies. The paper doesn't analyze the relative importance of different components of their training data (web text vs. code vs. lecture notes). It is unclear why the authors want to utilize these data sources and why the data mixture should be adopted as it is in the paper.
- Contamination issues. The model achieves good performance on GSM8K and MATH with 200M parameters. It is unclear whether there is data contamination issue.

### Questions
See weaknesses

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The author presents a small decoder-based language model on mathematics called Paramanu-ganita. They trained this model from scratch using the existing public mathematical corpus and also performed CoT instruction finetuning on top of it. They also train their own tokenizer specialised in math and code. Despite their model only having 208 million parameters, it outperforms general LLMs by approximately 30% points, and even math-specialised LLMs by 3-23% points in  GSM8K, 6-8% on MATH. The 208 million parameter model outperformed  LLaMa-1 (33B, 13B, 7B), LLaMa-2 (7B, 13B), Falcon (40B, 7B), PaLM (62B, 8B), MPT (30B, 7B), Vicuna 13B, and math-specialised LLMs like Minerva 8B, LLEMMA-7B on GSM8K, MATH, AGIEVAL-AQuA-RAT benchmarks. They also showed the reduced time and computation requirement to train this model as compared to existing LLMs.

### Strengths
1. A novel decoder model, that is 34 times smaller than existing LLMs and can outperform them by a huge margin
2. A detailed explanation of the training process required
3. Detailed benchmarking on GSM8K, MATH and other datasets.
4. Emphasis on the training time required and compared it to other existing LLMs, showing computation and environmental prowess in training an exclusive tiny model from scratch.

### Weaknesses
1. The paper uses Qwen-72B to label the corpus and use a score >= 0.6 for training the model, ensuring only a high-quality dataset is used. However, apart from this, the training process used is not novel. Specifically, there is no novelty in the model architecture or training paradigm used that can justify the complete novelty of the paper and also puts into question the improved performance of a 208 million parameter model over LLMs
2. The paper does not touch upon, newer and difficult mathematical datasets such as MATHBENCH or JEEBENCH. These are some datasets that were released after training cutoff time for some models, ensuring they are not part of their training data. These datasets are also much more difficult as compared to gms8k. This will ensure that the proposed model is robust in solving difficult problems that it hasn't seen before.
3. Will the checkpoint-filtered corpus used for training be publicly available?
4. How does the model perform on out-of-distribution data points, this can be checked by first doing a sanity check of data memorization/contamination [1]. Performing simple algorithms 1 and 2 from the paper will ensure that the model has not seen the evaluation dataset, making the results more robust.
5. The empirical analysis is missing from the paper. A thorough qualitative comparison of reasoning chains produced by Paramanu-Ganita versus other models on a few representative problems from the benchmark datasets. For example, what errors are made by existing LLMs vs. Paramanu-ganita and in which area does it improve?

Reference
[1] Golchin, Shahriar, and Mihai Surdeanu. "Time travel in llms: Tracing data contamination in large language models." arXiv preprint arXiv:2308.08493 (2023).

### Questions
Address the weaknesses of the paper mentioned above.

### Soundness
2

### Presentation
2

### Contribution
1
