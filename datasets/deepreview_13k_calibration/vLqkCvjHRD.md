# Coarse-Tuning Models of Code with Reinforcement Learning Feedback

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 6, 3, 5

## Abstract
Large Language Models (LLMs) pre-trained on code have recently emerged as the dominant approach to program synthesis. However, these models are trained using next-token prediction, which ignores the syntax and semantics of code. We propose \approach, that further trains a pre-trained LLM via reinforcement learning, using feedback from a grounding function that scores the quality of the code. The grounding function uses (i) compiler-derived feedback on whether the code it  generates passes a set of correctness checks; and (ii) feedback from a different LLM that compares the generated code to a reference code. \approach is model- and language-agnostic. We empirically evaluate it on the MBJP and MathQA tasks for Java. Our experiments show that \approach raises the odds that an LLM-generated program compiles, is executable, and produces the right output on tests, often allowing LLMs to match the performance of 2x-8x larger LLMs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper introduces Reinforcement Learning with Coordinated Feedback (RLCF), a new approach to enhancing the capabilities of LLMs in program synthesis. Traditional next-token prediction training objective overlooks the syntax and semantic constraints in code. RLCF aims to address this by retraining LLMs using RL, incorporating feedback from a compiler, and a separate LM that compares generated code against a reference. This "coarse-tuning" process occurs after initial pre-training but before task-specific fine-tuning. RLCF's effectiveness is demonstrated in Java datasets (MBJP and MathQA), showing that it significantly improves the probability of generating correct, compilable, and executable code.

### Strengths
A novel attempt to integrating compiler feedback in RL based code generation.

Paper demonstrates an innovative approach in using a hybrid grounding function that incorporates both a compiler and a discriminator LLM. This enhances the reliability and relevance of the generated code, making the system robust against producing syntactically correct but contextually irrelevant responses.

### Weaknesses
Compiler limitations: The use of a compiler in the grounding function inherently relies on the limitations and capabilities of the chosen compiler. Different compilers might have varying levels of strictness or support for language features, potentially leading to inconsistencies in how code is evaluated. This could result in a situation where the model generates code that is deemed correct by one compiler but not by others.

From the perspective of practical implementation in developer tools, the requirement to utilize both a compiler and an additional discriminator model could present significant challenges.

There is a need for more robust RL baselines, such as the RLHF (for instance, with binary reward)

### Questions
The study compares the base pre-trained CodeGen model with the version enhanced by RLCF. Would it be feasible to include a comparison with a supervised fine-tuned variant of the CodeGen? For instance, we could create a collection of "gold standard" examples that both compile successfully and are preferred by the discriminator for SFT. This could separate the improvement from the coarse tuning technique itself vs better quality data.

The process of generalizing this approach across various programming languages, and different compilers might represent a challenge. If possible, add more tests or discuss it.

Additionally, a comparison with state-of-the-art reinforcement learning techniques that use feedback would be valuable. Utilizing a compiler to generate binary rewards could help assemble a training dataset suitable for a conventional RLHF or RLAIF frameworks, providing a stronger baseline to evaluate the effectiveness of RLCF.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work proposes a new approach to to program synthesis using reinforcement learning and feedback from a grounding function. The experiments show promising results in improving the performance of LLM-generated programs.

### Strengths
+ The RLCF proposed in this work uses feedback from both compiler-derived feedback and LLM feedback.

+ The proposed approach is model- and language-agnostic, making it possibly applicable to various programming languages and models.

+ This work presents empirical evaluations on the MBJP and MathQA tasks for Java, showing promising results.

### Weaknesses
 - The proposed approach is limited to larger dataset due to the fact that CODENETJAVA does not consider dependencies on user-defined packages or libraries.

- The paper only evaluates the proposed approach on two specific tasks for Java, which may not be representative of other programming languages or models.

- This work does not provide a comparison of the proposed approach with existing state-of-the-art LLMs like GPT3 or GPT4.

- How this approach can work with existing pre-trained code-specific LLMs is missing.

### Questions
Please check the Weaknesses for detailed questions to be answered.
- Is the proposed evaluation and experiments representative enough for other programming languages or models? 
- How can this approach work with existing pre-trained code-specific LLMs is missing?
- Is it possible fro authors to compare the proposed method with existing state-of-the-art LLMs like GPT3 or GPT4?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work propose a method to fine-tune an LLM for code generation using RL. The feedback consists of two components: localized compiler errors to encourage the LLM to generate code which compiles, and a CodeBERT-based discriminator which tries to distinguish between the code generated by the LLM vs. the ground-truth solution (conditioned on the prompt). Results show improvements on several baseline code generation models (up to 1.5B parameters) for Java code generation.

### Strengths
The idea to fine-tune an LLM for code generation using only feedback from static analysis only is, as far as I can tell, novel. The writing is also clear and well motivated. As code generation is a major application of LLMs, the work has potential for significant impact as well. The experimental results are also relatively comprehensive, including a slate of baselines for comparison.

### Weaknesses
Prior works (see below) have used a combination of static and dynamic analysis as an RL reward for fine-tuning LLMs for code generation, which limits the novelty.

The decision to focus on Java, motivated by the authors for its static typing and availability of static analyzers, makes comparisons with existing works difficult, which have almost universally adopted Python as the language of choice. The benchmark datasets (MathQA and MBJP) were originally written in Python, and then transpiled automatically into Java. Even the dataset used in this work for finetuning, CodeNetJava, has a Python equivalent. Additionally, this work leverages feedback from the static analyzer consisting solely of the location of the compiler error, which should be available for Python as well.

For instance, RLTF [1], which is another RL for code generation technique, achieves 30.4 pass@1 on MBPP (the original python dataset) using the 770M CodeT5 as the base model. This compares with 6.6% for RLCF (this work) on MBJP (using the same base model, which starts around the same pass@1 of ~4% for MBPP).

Ideally, I would have preferred the experiments to have been done in Python, but at the very least, the related work should include a discussion of works which apply RL for code generation. For instance CodeRL [2] is mentioned as a baseline, but there is no comparison in the related work. As far as I can tell, the specific design (using a discriminator as well as returning the location of a compile error) is novel, but there are certainly parallels to prior work (for instance, CodeRL uses a critic to return localized information). Another highly relevant work is [3], which combines RL with an AST-based syntactic match metric as well as a dataflow graph based semantic match metric (both of which are static rather than dynamic analyses).

Finally, I'm not sure the ablation study for CodeRL is a fair comparison, as CodeRL includes a number of other components beyond simply an RL reward for compile errors (such as the aforementioned critic network). This can be addressed by renaming the ablation to something other than CodeRL.

### Questions
Can you provide a comparison of your methods with the 3 works cited above?

Can you ablate the localization aspect of the compiler feedback? i.e., just return -1 for compile errors (while maintaining the discriminator).

It would also be good to swap out the learned discriminator with the DFG-based metric from [3] above.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes tuning language models (pre-trained on code) for a specific programming language by leveraging static analysis tools (like those used in compilers). The static analysis tools are combined with a separate language model (CodeBERT) to craft a reward function. This reward is used with PPO to train the language model. Experiments with three different language models (up to 1.5B parameters) on code examples in Java demonstrate that the proposed method is able to improve the performance over the pre-trained model.

### Strengths
Using the compiler (and related tools) to improve the ability of language models to generate code is a promising direction. This approach reflects how human programmers also require feedback from the programming environment to hone their skills, whereas solely reading code is not sufficient.

Many commonly used programming languages are supported with static analysis tools, so the proposed method appears to be quite general.

The presentation of the method and the results is clear.

### Weaknesses
The experiments do not seem to control for the amount of compute. Comparing RLCF to a baseline that uses 0 compute (after pre-training) does not provide a useful comparison. A more informative baseline would be one that uses the same amount of compute as RLCF but uses the standard LM loss function instead. The "+Mono" baseline in Table 7 goes in this direction, but it does not apply the same amount of compute as RLCF.

The proposed method requires a so-called discriminator D that is part of the grounding function. This discriminator is a separate LM (not the same as the one that is being tuned to generate better code). The specific model used here is a pre-trained CodeBERT. It is unclear why this specific choice was made and how this choice impacts the results. While it appears that the pre-training here isn't strictly necessary for RLCF to yield improvements (based on Table 4 in the appendix), it does look like pre-training has a very significant effect. But using a pre-trained model puts into question whether performance improvement primarily arises due to distillation effects? Also, how well does CodeBERT perform on the tasks? When using a different model as the discriminator, do the numbers still look the same?

The results seem to suggest that RLCF is effective in improving the rate at which the LM samples compilable and executable programs. However, this improvement does not appear to correlate as much as expected with the improvement in the proportion of samples that pass the test cases. Currently it is unclear to me how this improvement in passed test cases arises and I'm more inclined to believe that the majority of it is due to distilling "Java code knowledge" from CodeBERT. I'd suggest running a RLHF baseline with the HF replaced by CodeBert.

### Questions
Are the model descriptions for pre-trained and not pre-trained in Table 4 in the appendix mixed up?

See weaknesses for more questions.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
