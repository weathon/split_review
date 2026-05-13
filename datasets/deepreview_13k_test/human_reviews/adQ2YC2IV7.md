# Unleashing the Creative Mind: Language Model As Hierarchical Policy For Improved Exploration on Challenging Problem Solving

- Decision: Reject
- Scores: 3, 5, 5, 6

## Abstract
Large Language Models (LLMs) have achieved tremendous progress, yet they still often struggle with challenging reasoning problems. Current approaches address this challenge by sampling or searching detailed and low-level reasoning chains. However, these methods are still limited in their exploration capabilities, making it challenging for correct solutions to stand out in the huge solution space. In this work, we unleash LLMs' creative potential for exploring multiple diverse problem solving strategies by framing an LLM as a \textit{hierarchical policy} via in-context learning. This policy comprises of a \textit{visionary leader} that proposes multiple diverse high-level problem-solving tactics as hints, accompanied by a \textit{follower} that executes detailed problem-solving processes following each of the high-level instruction. The follower uses each of the leader's directives as a guide and samples multiple reasoning chains to tackle the problem, generating a solution group for each leader proposal. Additionally, we propose an effective and efficient \textit{tournament-based approach} to select among these explored solution groups to reach the final answer. Our approach produces meaningful and inspiring hints, enhances problem-solving strategy exploration, and improves the final answer accuracy on challenging mathematic datasets like MATH.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The study presents an innovative framework that uses a hierarchical policy structure to improve problem-solving in Large Language Models (LLMs). A "low-level follower" executes details while a high-level "visionary leader" generates strategies. Using a tournament-based solution selection process, the authors' approach, which was evaluated on the MATH dataset, demonstrates improved strategy exploration and answer accuracy.

### Strengths
1. Innovative Framework: The hierarchical policy framework for problem-solving is a novel approach that capitalizes on the creative potential of LLMs.

2. Sophisticated Selection Mechanism: The tournament-based selection process is a unique and strategic method to pinpoint the most effective solution, which mimics evolutionary selection processes to optimize problem-solving outcomes.

### Weaknesses
1. Limited Dataset Representation: The study's findings are primarily based on the MATH dataset, which raises concerns about the model's performance on other datasets that present different challenges, such as the GSM8k. This limits the understanding of the model's adaptability and effectiveness across various types of reasoning tasks.

2. Ambiguity in Model Details: The paper does not specify which versions of GPT-3.5 and GPT-4 were used, nor does it detail the hyper-parameters involved. Such information is critical for replicating the study.

3. Cost Analysis Omission: There is no comprehensive analysis of the computational costs associated with different methods, including the number of tokens generated and encoded. Such an analysis is essential to evaluate the model's efficiency and practicality.

### Questions
How does the model perform on other representative datasets like GSM8k, and can you provide comparative analysis to demonstrate its versatility across various domains?

Could you specify the versions and hyper-parameters of GPT-3.5 and GPT-4 used in your experiments, and discuss how different configurations might affect the model's problem-solving capabilities?

Can you provide a detailed cost analysis, including the number of generation tokens and encoding tokens required, to better understand the computational efficiency of your proposed method compared to traditional approaches?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a new approach to improve the math reasoning capabilities of Large Language Models (LLMs) by framing them as hierarchical policies. The hierarchical policy consists of two parts: a "visionary leader" and a "follower". The leader suggests multiple high-level problem-solving tactics or hints, while the follower carries out detailed reasoning based on each of these high-level instructions. For each leader's directive, the follower samples multiple reasoning chains to create a group of potential solutions. To select the best solution from these groups, the authors introduce a tournament-based selection method. Experimental results on the MATH dataset show that this approach generates meaningful hints, and improves the accuracy of the final answer on challenging problems.

### Strengths
1. I like the idea of generating hints first and then apply low level detailed reasoning. This strategy is intuitive and more like what we humans do in the real life. The authors also provide an effective way of sampling answers based on the hints and new strategy to select the best-of-n.
2. The experiment results show that the proposed method are better than both CoT + self-consistency and ToT + self-consistency baselines.

### Weaknesses
1. Generally I am not very sure about the novelty of the proposed method. I am mostly familiar w/ the math reasoning works but not familiar w/ the topic of LLM planning. The novelty may be a weakness; or may not --- I would like to refer to the opinions from other reviewers.
2. Some descriptions of the method/experiment are confusing. Equation (1) and the relevant text is an example. The authors integrate w.r.t. $h$, so they treat $Pr(A|h,Q)$ as a probability density function so the integral $Pr(A|Q)$ should be a probability mass function. Yet the authors use the same notation $Pr$ which is quite confusing. More importantly, although we can understand what the authors would like to express after reading the whole section, the equation itself is invalid as $h$ is a discrete random variable rather than a continuous random variable so you cannot integrate w.r.t. $h$. Please note that mathematical notations in a paper is for helping readers to understand your idea more easily; but Equation (1) is not helping but instead making it even harder to understand. Actually, the key point of the section is just one sentence: "More generally, our strategy samples all the different hints returned by $\pi_{high}$ with equal probabilities.". And this is already clear enough. Similar feelings also appear in the section introducing the "Grouped-Majority Recall" metric, where the authors use quite long paragraphs to explain the details of it but the organization is not quite good and thus make it not easy to get the motivation of proposing this new metric. We generally suggest the authors to improve the expression and organization in these sections for better readability.
3. I may miss it but it seems there is no discussion about the accuracy/effectiveness of the tournament-based selection. IMO, it's non-trivial for LLM to accurately select the best answer among $n$ by iteratively comparing pair by pair. The authors do not provide the reason of introducing this new approach and why not use alternatives like another majority voting over the $n$ candidates. Also, it is possible to make a majority voting over the $n \times m$ candidates directly; the authors do not demonstrate the necessity of the hierarchical selection strategy that majority votes within each group to get $n$ candidates first and select by tournament.

### Questions
1. For retrieval-based hints generation, after you find similar examples in the training data, how do you identity the hints for these examples? The original MATH dataset doesn't contain such annotations. Do you generate the hints by LLM? If so, what's the accuracy of these hints?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a hierarchical policy to help LLMs to tackle complex reasoning problems. This policy consists of (1) a high-level leader to explore solution direction and a low-level follower to generate a detailed solution, and (2) a tournament-based approach to select desired reasoning chains during exploration. All the modules are implemented by prompting large language models without additional model training. The results show that the hierarchical policy is able to achieve better accuracy on solving complex math question tasks compared to several SOTA approaches.

### Strengths
- Experiment results have interesting findings that: when the number of reasoning chain samples increases, the increase of recall of correct solution and accuracy of the final answer is not aligned. This reveals the potential of LLMs to solve complex questions and can provide insights to other future researchers.

- Results show that the hierarchical policy outperforms other prior approaches in solving complex math questions.

- The paper is well-written. The problem is well-motivated by grounding on the prior work and easy to follow.

### Weaknesses
- The evaluation datasets are not comprehensive enough. The authors only evaluate the approaches on a single dataset (the MATH dataset), and the relative evaluation size is small. Other math datasets (e.g., GSM8K, PRM800K) or other domain datasets in MMLU (e.g., Physics, Chemistry, etc) should be evaluated to demonstrate the generalization.

- It is uncertain whether the improvement is from the hierarchical policy or the "self-evaluation" process when choosing the better reasoning chains. Previous research (e.g., "Language Models (Mostly) Know What They Know") suggests that LLMs like GPT-4 possess the ability to assess the likelihood that their output is correct.

### Questions
- What's the motivation of the "Grouped-Majority Recall" metric? A more intuitive idea may be the percentage of questions whose ground truth answer exists in at least one of the answers.

- In the "tournament-based approach", GPT-4 is used to select the better reasoning chain as the final solution. Because of the "self-evaluation" ability of LLMs, have you tried to use the majority vote strategy to obtain the final answer as an ablation experiment and compute the accuracy? In GPT-3.5 based approaches, is the "tournament" based on GPT-4 or GPT-3.5 (you mentioned that the GPT-4 is prompted to compare the current chains with (i+1)-th chain (Section 3) )?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel approach to enhance the problem-solving abilities of large language models (LLMs) by framing them as hierarchical policies. The approach consists of:

* A high-level leader policy that generates diverse hints and tactics for exploration.
* A low-level follower policy that uses the hints as guidance to execute detailed reasoning chains.
* A tournament-based method to select the best reasoning chains and obtain the final answer.

The paper demonstrates that this approach improves the exploration of problem-solving strategies, the discovery and visibility of correct solutions, and the final answer accuracy on challenging mathematical reasoning tasks. The paper also provides a theoretical analysis and empirical evaluation of the proposed method.

### Strengths
- The paper introduces a novel and general framework to enhance the problem-solving abilities of LLMs by using hierarchical policies. 
- The paper also proposes a new tournament-based method to select the best reasoning chains, which is inspired by human problem-solving behavior.
- The paper also conducts extensive experiments on challenging mathematical reasoning tasks, demonstrating that the proposed method outperforms existing baselines and achieves state-of-the-art results.
- The paper is well-written and organized, with clear definitions, notations, and algorithms.

### Weaknesses
- Need ablation experiments to prove that the proposed tournament-based method is better than simple voting; 
- For mathematical problems, the current some work has used code interpreter to greatly improve the results, such as (53.9% → 84.3%)[1], can the method in this paper be effective for this setting? From this perspective, the improvement brought by directly using LLM to output results in the paper is not significant, and code interpreter may be the key to solving math problems.

[1] SOLVING CHALLENGING MATH WORD PROBLEMS USING GPT-4 CODE INTERPRETER WITH CODE-BASED SELF-VERIFICATION

### Questions
See weakness section

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
