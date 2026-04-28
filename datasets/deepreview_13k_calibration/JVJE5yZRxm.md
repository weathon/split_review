# Teaching Code Execution to Tiny Language Models

- Decision: Reject
- Avg Score: 3.00
- Scores: 5, 3, 3, 1

## Abstract
Recent advancements in large language models have demonstrated their effectiveness in various tasks. However, the question of these models' limitations remains open though. For instance, can a language model learn to perform code execution (i.e., predicting the output of code)? Current research indicates that the performance of state-of-the-art large language models in code execution is still limited. The reasons for this limitations are unclear though. Is it due to fundamental constraints or other factors such as training data and computational resources? Is the next-token prediction objective sufficient for learning code execution? How small can a language model be while still capable of learning code execution? In this paper, we investigate these questions. More specifically, we investigate whether tiny language models, trained from scratch using the next-token prediction objective, can effectively learn to execute code. Our experiments show that, given appropriate data, model size, and computational resources, tiny language models can indeed learn to perform code execution with a 99.13% accuracy for a tiny Turing-complete programming language. We begin by defining a tiny programming language called TinyPy. Millions of randomly generated codes in this language, along with their outputs, are used to train our tiny language models using the next-token prediction task. We then conduct a series of experiments to determine the smallest model size, data amount, and computational resources necessary to train our language model to achieve near-perfect accuracy in code execution. Our findings reveal that TEX, our proposed tiny language model with 15M parameters, can successfully learn code execution. This suggests that a task as complex as predicting code output is within the reach of language models.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper explores the potential of small language models (under 20 million parameters) in code execution tasks, typically a challenging area for larger language models. The authors trained a 15M-parameter model, TEX, using only the next-token prediction objective. With a dataset of randomly generated TinyPy code snippets, TEX achieves an impressive significant high accuracy in executing TinyPy code. This study suggests that tiny models can handle code execution tasks, provided they are given suitable training data and a simplified language structure.

### Strengths
1. **Innovative Use of Tiny Models**: This study makes a valuable contribution by demonstrating that, with proper training, small models can achieve near-perfect accuracy on structured tasks like code execution. This finding challenges the prevailing notion that only large models are capable of such tasks.

2. **Significant Efficiency Implications**: The success of small models like TEX in handling specific tasks could reduce the dependency on large, resource-intensive models in certain applications, paving the way for more efficient and scalable model deployment.

3. **Clear Presentation**: The paper is well-written and easy to follow, making the methodology and findings accessible to readers.

### Weaknesses
1. **Unclear Study Motivation**: Although the paper evaluates the code execution capabilities of a neural network model, it is not clear why this capability is necessary, given the existing functions of compilers and interpreters. One possible motivation might be that LLMs could serve as lightweight predictors of execution outcomes without actually running the code. However, the paper lacks any evaluation results to support this assumption. Furthermore, the paper does not explore the potential benefits of using an LLM for code execution over traditional methods, such as faster execution time, reduced memory usage, or the ability to handle more complex or ambiguous code. Without a clear justification for why an LLM approach is needed, the practical value of this work is questionable.

2. **Limited Evaluation Setting**: The model is trained and evaluated on the same distribution, which may bias the results in favor of the proposed model over baseline models like GPT. For a more robust evaluation, it would be helpful if the authors tested the model on an uncontaminated dataset [1, 2]. Additionally, the benchmark used in this study seems overly simplified compared to real-world programming tasks, and testing the model on more realistic benchmarks could better demonstrate its effectiveness. The TinyPy language, as described, lacks many features of real-world languages, such as complex data structures, libraries, and error handling. This raises concerns about the generalizability of the findings to more complex programming scenarios.

3. **Limited Novelty**: The study presents promising results, but the technical contributions are minimal. Both the model architecture and learning algorithm are widely studied in prior work. The promising outcomes observed might be attributed to data contamination or the evaluation setup rather than any novel technique introduced by this paper. The paper does not introduce any novel architectural components or training methodologies. The use of next-token prediction is a standard technique, and the model itself is a relatively simple transformer. The lack of technical novelty makes it difficult to assess the true contribution of this work.

### Questions
1. Can the proposed approach still outperform the baseline if the baseline is fine-tuned on the dataset?

2. What is the motivation for using an LLM to predict code execution outcomes instead of leveraging existing compilers?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper explores whether small language models, trained from scratch with a simple next-token prediction objective, can learn to execute code effectively. Despite advancements in large language models (LLMs), their limitations in code execution remain unclear. To investigate, the authors create TinyPy, a dataset contains small programs with basic arithmetic and control flow operations. Using millions of randomly generated TinyPy code snippets and their outputs, they train various tiny language models on the next-token prediction task. Their proposed model, TEX, with only 15M parameters, achieves a high 99.13% accuracy in predicting code outputs, and outperforms various LLMs such as CodeLlama and GPT-4o.

### Strengths
1. This paper studies an interesting topic, the prediction of program's execution states.

### Weaknesses
1. Lack of novelty. This paper proposes a dataset TinyPy, yet the dataset is much simpler compared to practical programs (such as MBPP) as it only supports arithmetic operations, condition, and loops. Does it supports data structure such as List? The TEX model's architecture is also standard GPT-2, so essentially it is simply training a small GPT-2 on synthesized simple programs.
2. The results of comparison against other LLMs is not surprising, as the other LLMs (such as CodeLlama and GPT-4o) are conducted with one-shot prompting, while the TEX model is well-trained using 64M samples. Given that the TinyPy programs are simple and limited, such large amount of training data should be enough to well-capture the patterns and thus easy for TEX to learn. Although TEX shows high accuracy on the test set, it is unconvincing to show that the approach can be generalized to more complex programs. To better understand the comparison against larger LLMs, it could be useful to add additional experiments such as fine-tuning the larger models on the TinyPy dataset or evaluating TEX in a few-shot setting.

### Questions
1. Can this approach be generalized to more complex programs or real-world programs? To generalize to more complex programs, does it require synthesizing a training dataset for more complex programs? Is it feasible to synthesize such a complex/real-world programs dataset automatically?
2. Could the author clarify the novelty and contribution of the approach? This is unclear since synthesizing programs using defined grammars is not new, and fine-tuning a GPT-2 model is also not new. What are the implication of this approach to future works?

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper investigates whether LLMs can learn to predict the code execution results by designing a simplified turing-complete python-like programming language, generate codes in this language, and train tiny LMs from scratch using next-token prediction.

### Strengths
The problem investigated in this paper is interesting. Nowadays, LLMs are indeed strugging to predict code execution results. This paper tries to simply the problem with a simplified programming language and generate code snippets in this language synthetically. The paper also investigates data size and model size scaling.

### Weaknesses
My main concern is the complexity of the code snippets generated by TinyPy Generator. Does the generator generates sufficiently complex logic, algorithms and data structures that mimics the complexity of today's code? If it is not close, it is not that representative and limits the value of the research. And the fact that 16M model achieves 99.13% accuracy indicates that the complexity of those code snippets is not high.
Another is that today LLMs are at the level of tens and hundreds billion of parameters. The capability these LLMs can achieve is not that comparable with old-fashion tens/hundreds of million parameters. This also makes the paper weaker in pushing forward the understanding of LLMs for code execution.

### Questions
- Why don't you conduct an experiment to finetune CodeLlama on the training dataset same as TEX? I hypothesize that you will get a comparable accuracy number as TEX.
- Could you explain the complexity of the generated code? Does the generated code match the sufficiently complex logic, algorithms and data structures that mimics the complexity of today's code?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The authors define a subset of the Python programming language TinyPy, and randomly sample sequences from this subset of Python. The authors fine-tune a NanoGPT model of 15M parameters to predict the output of programs sampled from this simple language.  The authors are able to achieve a 99.13% accuracy on this task of predicting outputs. The authors then evaluate how much training data / model parameters are required to achieve this level of performance.

### Strengths
The authors are clear in their writing of the paper: ideas are expressed clearly. The authors do indeed highlight a specific research question: can models achieve a high accuracy on predicting TinyPy outputs, and how do parameter sizes / training corpus sizes affect performance.

### Weaknesses
The research questions posed by the paper do not meet the threshold of novelty and significance for a conference like ICLR. There are also some issues in terms of the presentation of the paper as well.

Merit/Novelty of Approach: It has been commonly done in the past in the ML literature and also in the Compiler literature to sample programs by sampling from the grammar of a programming language. Much early ML program synthesis literature used Karel, and would sample executable programs from this language e.g. https://arxiv.org/pdf/1805.04276. To my understanding as well, I did not see any part of the paper that guaranteed that the TinyPy programs would print out outputs to the console: I am not assured that the programs are non-trivial to predict outputs for.

Merit of Findings: It is generally accepted that more data and larger models will yield better performance in tasks such as program synthesis. I do not find it insightful that such small models can achieve such high accuracy on the program synthesis task in question without being provided more insights into more complex questions / problems in program synthesis or LLM reasoning.

Concerns about anonymity: The authors use term TinyPy to describe their language for program synthesis. This happens to share the same name as the TinyPy Generator (Yamani et al., 2024) they cite and claim to use. I am concerned the authors did not take sufficient efforts to de-anonymize their submission. E.g. a different name instead of TinyPy could have been adopted.

I think the exposition of the work and questions asked seems generally sound, and is great! But I would encourage the authors to review more literature in the areas of program synthesis and in reasoning and think about unanswered research questions that will be of greater interest. The work is executed well! But I think the directions/questions asked could be improved, and being more familiar with current important questions and problems in the field is something that may be important to focus on next!

### Questions
1. Do you have statistics for how the minimum and average number of print statements there are per program in the test set? Likewise for loop-constructs, what is the average number of loop constructs for the test set? Providing statistics on these could help better-clarify the difficulty of the task. 
2. Have I made any misrepresentations in the comments I have made?

### Soundness
3

### Presentation
2

### Contribution
1
