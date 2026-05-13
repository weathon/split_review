# Understanding Chain-of-Thought in LLMs Through Information Theory

- Decision: Reject
- Scores: 6, 5, 8, 5, 8

## Abstract
Large Language Models (LLMs) have shown impressive performance in complex reasoning tasks through Chain-of-Thought (CoT) reasoning, allowing models to break down problems into manageable sub-tasks. However, existing CoT evaluation techniques either require annotated CoT data or fall short in accurately assessing intermediate reasoning steps, leading to high rates of false positives. In this paper, we formalize CoT reasoning in LLMs through an information-theoretic lens. Specifically, our framework quantifies the `information gain' at each reasoning step, enabling the identification of failure modes in LLMs without the need for expensive annotated datasets. We demonstrate the efficacy of our approach through extensive experiments on toy and GSM-8K data, where it significantly outperforms existing outcome-based methods by providing more accurate insights into model performance on individual tasks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes to use information theory to quantify the information gain of each reasoning step in a COT solution. The notation of task is introduced for each reasoning step, and assumptions are made for reasoning errors being unidentifiable primitive tasks by the LLMs. The information gain is formulated as a conditional probability difference between two subsequent steps with respect to the final correct answer. A supervisor model is trained to predict such conditional probability. A toy data with 5 primitive tasks are constructed to train the supervisor model and to test the efficacy of the proposed method against baselines including ORM and Math-Shepherd. The paper demonstrated the effectiveness of the Information Gain method to capture errors in reasoning steps (Figure 3 and Table 1).

### Strengths
1. The idea of using information gain to detect the helpfulness of each reasoning step is very novel and interesting.
2. The controlled experiments using toy data and GSM8K are well conducted and clearly demonstrate the advantage of Information Gain over baseline methods such as ORM.
3. The paper is well written and easy to follow.

### Weaknesses
1. A significant weakness of the paper is that it is unclear how applicable it is to real world reasoning tasks. More experiments involving more challenging tasks such as MMLU or MATH would be more convincing. The current experiments are limited to toy datasets and GSM8K, which do not fully represent the complexities of real-world reasoning. The reliance on synthetic data, even with arithmetic operations, raises concerns about the generalizability of the findings. The method's performance on more diverse and complex datasets needs to be evaluated to ascertain its practical utility.

2. The assumption of needing to annotate the task involved in each step is too restrictive. In reality, such a one-to-one mapping is neither possible nor necessary. A single reasoning step could use more than a single primitive task. It could also use no primitive task at all by simply being a filer step. This assumption limits the method's applicability to scenarios where a clear, pre-defined set of primitive tasks can be identified and mapped to each reasoning step. The method's reliance on this assumption makes it difficult to apply to more complex reasoning processes where steps may involve multiple sub-tasks or abstract reasoning that does not fit into a predefined category.

3. The distinction between error steps and irrelevant steps is mentioned but it is unclear how the IG method handles them separately. More clarity is needed. From the description, it looks like they will be treated equally. However, irrelevant steps are not as harmful as error steps. The method should ideally differentiate between steps that are irrelevant and those that actively introduce errors. Treating them equally could lead to an inaccurate assessment of the reasoning process, as irrelevant steps may not negatively impact the final outcome, while erroneous steps will. The lack of clarity on how the method distinguishes between these two types of steps is a significant concern.

### Questions
1. The paper can benefit from grammar checks.
Line 055 `detect` is repeated twice.
Line 164 `tasks` is supposed to be `task`.
Line 295, `which step went wrong` is using past tense while most of the paper is using present tense. Same for `chose` in line 429.
2. The proposition 3.4 is problematic as Equation (3) is asymmetric with respect to Y and Xj, while we know that mutual information should be symmetric.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper presents an information-theoretic framework for evaluating the quality of Chain-of-Thought (CoT) reasoning in Large Language Models (LLMs). The authors propose a method that quantifies the "information gain" at each reasoning step to identify failure modes without requiring expensive annotated datasets. The research shows that this approach is more effective than existing methods such as Outcome Reward Modeling (ORM) and Math-Shepherd in assessing intermediate steps in reasoning, especially when dealing with complex CoT processes. The authors claim that with the presented framework, intermediate steps can be used to detect errors, rather than just relying on the final answer. This is a step towards more interpretable CoT reasoning.

### Strengths
Applying an information theory perspective to the CoT reasoning chain provides a novel and rigorous method for evaluating the contribution of each step to the final output. This fresh approach differs from existing methods by quantifying the information gain at each reasoning step, rather than relying only on the final answer. This makes it possible to identify when errors occur, improving the interpretability and reliability of the model.

Unlike other methods, it does not require annotated data to train a verifier model, providing a cost-effective alternative to process-monitoring style models. By eliminating this requirement, it provides a scalable solution that is particularly useful for domains or tasks where generating annotated CoT data is impractical or prohibitively expensive.

Finally, the authors experimented with a toy dataset and a real dataset (GSM8K) and compared their approach to baselines. The improvements over the baseline demonstrate the effectiveness of the method.

### Weaknesses
I am still unsure about the experimental design, which contradicts some claims of the paper. For example, the use of a supervising model requires a lot of data, which is needed to train the supervising model. This requirement adds computational complexity, requiring additional processing power, memory, and time that the authors claim is not needed compared to the process monitoring models in the introduction. The paper needs to clarify the computational cost of training the supervisor model and how this compares to the computational cost of process monitoring models, as the current claims seem unsubstantiated.

In addition, using a supervising model to predict the answer given the previous steps in the chain of reasoning as a way to understand whether the previous steps contain information needed to answer a question may not be correct. For example, many questions can be answered directly by the model in an answer-only setup ("The answer is X"). For these questions, no CoT reasoning is needed. But in this framework this will not be the case and these steps will be listed as important steps. Basically, the framework's sample-wise information gain is designed to detect errors on a per-sample basis. However, there are instances where a model may accidentally reach the correct final answer, even with incorrect intermediate steps. This can lead to "false negatives," where a faulty chain of reasoning is not flagged because the final answer happens to be correct. The paper does not adequately address how the framework handles cases where the model arrives at the correct answer through faulty reasoning, which is a significant limitation.

Similarly, a lot of time CoT reasoning can hurt performance if the initial step is wrong and then it is hard for the model to recover. In such cases, the steps are considered important if the model can predict the answer correctly, which in many cases is not the case if the start is wrong. There is no analysis done in the paper. Also, the advantage of the approach presented in the paper is to understand and find the errors in the intermediate steps compared to predicting the final answer. This analysis is missing in the paper, especially in the areas where the intermediate errors are analyzed in detail. The paper lacks a detailed analysis of error patterns at different steps and how the supervisor model identifies these errors, which is crucial for understanding the framework's practical utility.

The experimental results rely heavily on controlled settings, such as toy datasets and GSM-8K, where task types and error points are clearly defined. In real-world scenarios, errors in CoT reasoning may not follow the structured patterns present in these datasets. This reliance on controlled experiments raises the question of how well the framework would perform on naturally occurring data with more diverse error types. This is important for understanding the scalability of the method as the number of reasoning steps increases or the chain becomes more complicated.

### Questions
There needs to be an analysis of questions where the model can directly predict the answers and how this framework addresses those questions. Are intermediate steps needed in such cases? And what about false negatives, where a faulty chain of reasoning is not flagged because the final answer happens to be correct? This analysis needs to be presented in the paper. 

The analysis of errors made at different steps needs more analysis. Even better if these stepwise errors form some patterns. How reliable the supervisor model is in identifying these errors would be interesting to see. 
Cost comparison between training the supervisor model presented in the paper and the process supervision paper needs to be analyzed to determine if training a supervisor model is even cheaper as claimed in the paper. 

Doubts about theoretical assumptions: Does the framework assume a linear sequence of reasoning steps, and how would it handle nonlinear or branching reasoning paths? Or what about cases where multiple reasoning chains lead to the correct answer?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents an algebraic framework to model CoT-based reasoning process in an LLM and in the ground truth. Specifically, it is assumed that there is a set of "primitive tasks", the members of which can be used to generate any task via composition. Such a notion of composition also induces a notion of "span" of a set of tasks and the notion of unidenfiability of a task (with respect to a given set of tasks). The key assumptions in this framework is that when the model's CoT for a prompt contains an unidenfiable task with respect to the tasks involved in the CoT of the ground truth, a "fork-structured" Bayesian network is induced, and due to d-separation, certain conditional independence property holds, which in turn suggests that after the forking point, information gain becomes zero. 

Using this framework, the paper introduce a new scheme for evaluating the CoT of LLM. Experimental results are given demonstrating the advantage of this framework and the proposed scheme.

### Strengths
The algebraic formulation and information-theoretic perspective in this paper are very nice. The approach taken is clean. Although the assumptions (particularly Assumption 3.2) may be subject to debate, I think this work is making an important step towards theoretical understanding of the CoT in LLM.  The presentation is also very good. I very much enjoy reading this paper.

### Weaknesses
I have only one concern about this paper, namely, I question if the sample-wise information gain (Equation 5) is a valid measure.

Note that although the standard mutual information (or "distribution-wise mutual information") is well-known to be non-negative and zero mutual information gives independence, the "sample-wise mutual information" (namely, the term without expectation) can be negative in general. The "intuitive" argument the authors give (lines 299 to 303)  to justify the use of sample-wise mutual information is not convincing to me. -- I feel this is the main weakness of an otherwise very elegant development. I encourage the authors to resolve this issue.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a new method to understand the effectiveness of chain-of-thoughts. Specifically, The paper proposes to analyze CoT from the information theory perspective. By training a model to predict the information gain, the proposed method could analyze the quality of generated thinking steps and thus select the better answer. The theoretical formulation is intuitive, but more empirical challenges are overlooked. I think more experiments on the general-purpose datasets are needed to justify the value of the proposed framework. Please refer to my questions for more details.

### Strengths
1. The authors give a thorough and detailed rhetorical formulation of the proposed solution.
2. The paper is clearly written and easy to follow.

### Weaknesses
1. The gap between the proposed framework and the claimed application scenarios remains big, which affects the potential impact of this work.
2. Some of the terms are not clearly defined, especially in the LLM scenarios. (e.g., steps) 
Please refer to the questions section for more detailed comments.

### Questions
1. Section 2.1. Do we need to, and how to define the set of lambda in a realistic task?
2. How do you define a step in a generation task?
3. It seems like the key is modeling the information gain. However, a separate model approximates the conditional distribution in the proposed framework, which is then used to model the information gain. As we all know, the training of a separate model is determined by the training data and sampled trajectories. How do you guarantee the learned model can model the conditional distribution well? In other words, what is the requirement for training such a model? Do we need to guarantee that the training data of the separate model follows a similar distribution of the final task?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
The paper proposes a novel, information-theoretic framework to analyze Chain-of-Thought (CoT) reasoning in large language models (LLMs). The authors focus on quantifying the "information gain" at each reasoning step, offering a method to detect errors in intermediate steps without requiring human-annotated CoT data. The framework uses concepts like task unidentifiability and conditional mutual information to identify at which intermediate step an LLM fails to execute a particular sub-task during a CoT process. The paper introduces a practical algorithm based on this framework to offer a more granular evaluation of LLM performance on reasoning tasks. Extensive experiments are conducted on toy datasets and the GSM-8K benchmark, showing that this method outperforms existing baselines such as Outcome Reward Models (ORM) and Math-Shepherd in detecting errors and providing insights into model performance.

### Strengths
1. The paper presents a novel approach to evaluating CoT reasoning by using information theory, specifically through the concept of information gain at each reasoning step. Compared to traditional methods like ORM, which focus on final outcome, the focus on intermediate reasoning steps allows for a more granular analysis of where a model might be going wrong which is important for LLM reasoning. 

2. The authors provide clear mathematical foundations and definitions for the formulation of their framework. The methodology is well-structured, and the theoretical assumptions are systematically translated into a practical algorithm. The paper’s thorough empirical validation using toy data and GSM-8K provides strong evidence of the framework’s effectiveness in identifying sub-task failures.

3.  By offering a means to detect specific reasoning failures without annotated data, this approach could reduce the need for expensive human supervision and help improve the interpretability and reliability of LLMs in complex reasoning tasks.

### Weaknesses
1. In section 3.3, while the information-theoretic approach is innovative, the need to train a separate supervisor model to estimate information gain might introduce complexity. The paper states that the framework doesn't require annotated data, but the supervisor also requires finetuning to predict the ground truth final output. This finetuning, while not requiring step-by-step annotations, still necessitates a dataset of input-output pairs for training, which could be a limitation in scenarios where even final outputs are scarce or expensive to obtain.
2. In section 2.2, The framework relies on the decomposition of tasks into primitive sub-tasks, and the assumption that each primitive task contributes incrementally to the information gain. For complex reasoning tasks with intertwined dependencies between sub-tasks, the information gain for each step will be more complex, and this assumption might not always hold. The paper does not sufficiently address how the framework would handle scenarios where the sub-tasks are not strictly sequential or where the information gain of one step is highly dependent on the outcome of previous steps, potentially leading to inaccurate error detection.
3. There are some errors in the paper, for example, in appendix B.1.1, the annotation for task $\lambda_2$, if I understand correctly, should be $z_1[0], z_1[0]+z_1[1], z_1[0]+z_1[1]+z_1[2]$.

### Questions
1. For math problems, the primitive tasks are intuitive to define. Have you tested your framework with other tasks, e.g. Blocksworld, or commonsense QA, where the definition of primitive tasks is less straightforward? Will different primitive task affect the conclusion?
2. In section 5.1.1, you mentioned the evaluation only considers samples where the final answer of the LLM was incorrect. Could you explain why you apply such a setting since it's also a common failure for CoT to get a correct answer but with incorrect intermediate steps?
3.  Also in section 5.1.1, when discussing about pitfall of the baselines, for ORM, you stated that the classifier becomes confident that the final output will be wrong right after $\lambda_2$, even though the error occurs at $\lambda_3$. But this is what we expect from the error detection, right? I understand you want to show the classifier will overfit on learning the false correlation between $z_2[2] > 150$ and the final error as in section 5.2. But this statement/setting doesn't seem correct to me.

### Soundness
3

### Presentation
3

### Contribution
2
