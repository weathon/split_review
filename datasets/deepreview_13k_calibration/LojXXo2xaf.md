# GPT Can Solve Mathematical Problems Without a Calculator

- Decision: Reject
- Avg Score: 6.00
- Scores: 5, 8, 3, 8

## Abstract
Previous studies have typically assumed that large language models are unable to accurately perform arithmetic operations, particularly multiplication of >8 digits, and operations involving decimals and fractions, without the use of calculator tools. This paper aims to challenge this misconception. With sufficient training data, a 2 billion-parameter language model can accurately perform multi-digit arithmetic operations with almost 100\% accuracy without data leakage, significantly surpassing GPT-4 (whose multi-digit multiplication accuracy is only 4.3\%). We also demonstrate that our MathGLM, fine-tuned from GLM-10B on a dataset with additional multi-step arithmetic operations and math problems described in text, achieves similar performance to GPT-4 on a 5,000-samples Chinese math problem test set.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose using LLMs to perform complex mathematical computations. To prove this theory, they trained a model called MathGLM on a dataset with multi-step arithmetic operations and math problems described in text. They verify their results on the APE test set, as well as a K6 dataset they proposed, which consists of elementary-school math word problems. They demonstrate that on a constructed dataset of complex mathematical computations, their model outperforms GPT-4.

### Strengths
1. Interesting perspective on using LLMs to conduct complex mathematical computations without the use of tools.
2. The paper states its theory and results clearly.

### Weaknesses
1. The claim regarding motivation is not robust. While MathGLM achieves a high accuracy of 93.03% on the constructed dataset for complex computations, these calculations can be done with 100% accuracy using other tools. The paper does not adequately justify why an LLM, with its inherent limitations in precision, is a suitable choice for tasks where exactness is paramount. This is especially true given the computational cost of training and deploying such models.
2. The computation is limited to addition, subtraction, multiplication, division, and exponentiation. The method probably wouldn't generalize well to more intricate computations such as log, sin, etc. Moreover, mathematics should aim for complete accuracy, so utilizing LLMs for these calculations isn't a suitable strategy, especially considering the costly pretraining involved for computations that other tools can resolve more efficiently. Instead, LLMs should concentrate on providing more insight and higher-level strategies for solving math problems. The paper lacks a discussion on the limitations of the current approach in terms of handling more complex mathematical functions and operations, which are essential for real-world applications.
3. The primary math word problem datasets are APE and K12, both of which are in Chinese. There were no experiments conducted on popular math datasets like MATH and GSM8K. Since GPT-4 is primarily trained in English, and MathGLM is fine-tuned for Chinese math word problems, such a comparison might not be valid. The advantage of MathGLM could be due to the language, rather than its proficiency in resolving math problems. The paper fails to address the potential for language bias in the evaluation, and does not provide sufficient evidence that the model's performance is not simply an artifact of the training data's language.

### Questions
See Weaknesses and,

This paper uses LLMs to conduct complex mathematical computations. This is a novel approach, but the motivation is weak because using LLMs for complex mathematical computations lacks accuracy and generalizability. Additionally, there is a lack of experimentation on MATH and GSM8K, as the primary comparisons are made using Chinese mathematical datasets.

Correctness: 3: Some of the paper’s claims have minor issues. A few statements are not well-supported, or require small changes to be made correct.

Technical Novelty And Significance: 2: The contributions are only marginally significant or novel.

Empirical Novelty And Significance: 2: The contributions are only marginally significant or novel.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper has a full study of LLM on math problems, with the focus of multi-digit complex operations and math problems in regular text. The dataset are created, and the LLM of different sizes are fine tuned. The MathGLM has been evaluated on many setup and ablation. The new model has proven better performance than the GPT-4 on the two goals.

### Strengths
The math accuracy belongs to one of the core challenge of LLM. The paper has very good CoT dataset and gets enhanced performance compared to the GPT-4 model. The paper appears rather useful among many scholars from relevant area.

### Weaknesses
Could we extend the evaluation of the new model and see the performance on non-math tasks? The math focus finetune may have reduced the performance on other tasks, and it is good to know how good / bad that would be.

### Questions
Maybe a followup work would seem how to train model for middle-school level math problems, how the size of dataset / model would scale for that

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
In this paper, the authors introduce two new datasets that can be used to improve pre-training and fine-tuning of large language models or, more generally, large-scale Transformer models. One dataset contains a large set of arithmetic problems, while the other represents a refined version of Ape210K, which has been augmented with step-by-step solution procedures to solve math word problems involving natural language. The authors exploit these datasets to train a series of Transformer-based language models and show that they indeed achieve more accurate performance in arithmetic and word problem tasks compared to GPT models or other LLMs.

### Strengths
-	The article is generally clear and well-written. The research questions are well-motivated.
-	Investigating the arithmetic and mathematical abilities of Transformer-based architectures and LLMs is an important and timely research area.
-	Reconstructing the Ape210K dataset by adding step-by-step solutions constitutes an interesting extension to the available training corpora (which would become even more useful if the dataset would be made publicly available).
-	The authors also analyze the impact of problem difficulty (e.g., grade levels) and the error distribution.

### Weaknesses
-	The training/testing setup used in the present work differ from those used in similar work, making it challenging to compare the current results with previous contributions. Overall, it seems that the advantage in the reported benchmarks mostly (only?) stems from the use of an extended training set containing math problems, rather than from architectural innovations. This would still constitute an interesting finding, but it should be demonstrated using out-of-distribution test instances (see next point).
-	The authors claim that MathGLM has a “profound understanding of the complex calculation process” and “effectively learns the underlying rules and principles of arithmetic operations”, however I do not think that its generalization abilities have been properly evaluated.
-	There are a few methodological details than require clarification (see questions below).
-	The paper does not include any Reproducibility Statement or any pointer to source code repositories, which makes it difficult to replicate the simulations and the experimental setup.

-   The authors say that MathGLM learns to solve arithmetic tasks “by integrating a step-by-step strategy into its architecture”. However, it is not clear how the model architecture actually implements step-by-step reasoning process (from the description, it seems that such feature is just a property of the solution format, rather than of the architecture design). This point should be clarified.
-	In order to properly test for generalization the authors should demonstrate that the model can solve problems outside the training distribution (e.g., involving much longer numbers, and much more operands, see for example https://arxiv.org/abs/2207.02536). At present, an alternative (and more parsimonious) explanation is simply that the larger-scale of the training data allows to the model to memorize a more consistent amount of arithmetic knowledge.
-	The authors say that “To assess the generalization ability of MathGLM beyond the 5-digit range, a set of 50,000 training records involving numbers within the 12-digit range are introduced into the training dataset”. This does not guarantee that generalization is properly assessed; it rather shows that by adding more training samples from the testing range the performance increases, which is expected (also see https://arxiv.org/abs/2306.15400).
-	It is not clear whether the curriculum learning strategy is beneficial since there is no comparison with a non-curriculum counterpart.
-	It is not clear how the Ape210K dataset was reconstructed. Were the step-by-step solutions generated in an automatic way? If so, how was their quality verified?
-	What is the rationale of using different models for the Arithmetic task and the Math Word Problems? Shouldn’t the same MathGLM model be able to solve both types of problems? The authors say that “our goal is to simultaneously advance both mathematical reasoning and arithmetical calculation capabilities of LLMs, addressing both aspects at the same time”, but from my understanding they trained separate models for the Arithmetic and MWP datasets (the “Training Strategy” section at pg. 5 should be expanded and described in a much clearer way).
-	The authors should more carefully explain how GPT models were tested. Which prompting methods were used to probe these models? How did performance change when using more advanced (e.g., Chain-of-though) prompting strategies?
-	The title is misleading, since it suggests that models from the GPT family (e.g., ChatGPT, GPT-4) achieve the best accuracy, while in fact the authors are tuning a model from the GLM family. A better option could be to just use “LLMs” as a more general term?
-	“GLM” has not been properly defined in the introduction (I suggest including both the acronym description and the reference paper).
-	The manuscript content is often redundant; I suggest removing duplicate (or similar) sentences.

### Questions
-	The authors say that MathGLM learns to solve arithmetic tasks “by integrating a step-by-step strategy into its architecture”. However, it is not clear how the model architecture actually implements step-by-step reasoning process (from the description, it seems that such feature is just a property of the solution format, rather than of the architecture design). This point should be clarified.
-	In order to properly test for generalization the authors should demonstrate that the model can solve problems outside the training distribution (e.g., involving much longer numbers, and much more operands, see for example https://arxiv.org/abs/2207.02536). At present, an alternative (and more parsimonious) explanation is simply that the larger-scale of the training data allows to the model to memorize a more consistent amount of arithmetic knowledge.
-	The authors say that “To assess the generalization ability of MathGLM beyond the 5-digit range, a set of 50,000 training records involving numbers within the 12-digit range are introduced into the training dataset”. This does not guarantee that generalization is properly assessed; it rather shows that by adding more training samples from the testing range the performance increases, which is expected (also see https://arxiv.org/abs/2306.15400).
-	It is not clear whether the curriculum learning strategy is beneficial since there is no comparison with a non-curriculum counterpart.
-	It is not clear how the Ape210K dataset was reconstructed. Were the step-by-step solutions generated in an automatic way? If so, how was their quality verified?
-	What is the rationale of using different models for the Arithmetic task and the Math Word Problems? Shouldn’t the same MathGLM model be able to solve both types of problems? The authors say that “our goal is to simultaneously advance both mathematical reasoning and arithmetical calculation capabilities of LLMs, addressing both aspects at the same time”, but from my understanding they trained separate models for the Arithmetic and MWP datasets (the “Training Strategy” section at pg. 5 should be expanded and described in a much clearer way).
-	The authors should more carefully explain how GPT models were tested. Which prompting methods were used to probe these models? How did performance change when using more advanced (e.g., Chain-of-though) prompting strategies?
-	The title is misleading, since it suggests that models from the GPT family (e.g., ChatGPT, GPT-4) achieve the best accuracy, while in fact the authors are tuning a model from the GLM family. A better option could be to just use “LLMs” as a more general term?
-	“GLM” has not been properly defined in the introduction (I suggest including both the acronym description and the reference paper).
-	The manuscript content is often redundant; I suggest removing duplicate (or similar) sentences.

### Soundness
1 poor

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes MathGLM, a transformer-based language model specifically designed and trained to excel at mathematical reasoning and arithmetic tasks. 

1. MathGLM is trained on a large dataset of arithmetic expressions and sequences, ranging from simple to complex multi-step calculations. This allows it to learn the underlying rules and patterns of arithmetic operations.

2. A step-by-step strategy is used during training, where MathGLM is tasked with generating each intermediate step leading to the final result. This mimics human calculation and helps MathGLM deeply comprehend the calculations.

3. Curriculum learning is used, starting with simpler arithmetic tasks and progressively increasing complexity. This improves efficiency and allows handling of large digit numbers.

4. MathGLM demonstrates significantly higher accuracy on arithmetic tasks compared to GPT-4, ChatGPT and other LLMs. It also achieves comparable performance to GPT-4 on a Chinese math word problem dataset.

### Strengths
1. The core idea of specializing a language model for mathematical reasoning is novel and well-motivated. Math is an important domain where current LLMs struggle.

2. The step-by-step training strategy is creative and helps MathGLM learn the intricacies of arithmetic operations. Generating intermediate steps is akin to human math solving.

3. The arithmetic dataset construction process covers various types of math operations and data formats in a principled manner. This diversity is key for strong training.

4. Extensive experiments demonstrate clear performance gains over GPT-4 and other models, validating MathGLM's capabilities. The scaling experiments also provide useful insights.

5. The work is technically sound, clearly presented and easy to follow. The motivation and proposed techniques are intuitive.

### Weaknesses
1. While specializing for arithmetic is beneficial, it could compromise more general capabilities. Testing on broader math/reasoning tasks could help characterize tradeoffs. The paper should explore performance on tasks requiring symbolic manipulation, logical deduction, or geometric reasoning, which are not strictly arithmetic but are important aspects of mathematical competence. Understanding how the model's arithmetic specialization affects its ability to handle these diverse mathematical tasks is crucial.

2. More analysis and examples demonstrating the step-by-step generation process could be useful to understand MathGLM's learned skills. The paper should include visualizations of the intermediate steps generated by the model for a variety of problems, highlighting both successful and unsuccessful cases. This will provide insights into the model's internal reasoning process and identify potential failure modes.

3. The reasoning behind curriculum learning's benefits is not fully fleshed out. Is it mainly about efficiency gains? The paper should provide a more detailed analysis of how the curriculum learning strategy impacts the model's learning trajectory. For example, are there specific types of arithmetic problems that are more effectively learned at different stages of the curriculum? A study of the model's performance at different curriculum stages would be beneficial.

4. How well do the findings transfer to non-Chinese languages? Cross-lingual experiments could help strengthen claims of language-agnostic reasoning. The paper should evaluate the model's performance on mathematical datasets in other languages, particularly English. This would demonstrate the model's ability to generalize beyond the training language and assess the extent to which its mathematical reasoning skills are language-independent.

### Questions
Are there any analysis and examples of the errors made by MathGLM? Understanding the remaining limitations could guide future improvements.

For real-world usage, how does MathGLM handle novel word problems outside its training distribution? Experiments on out-of-distribution generalization could be insightful.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
