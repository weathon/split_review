# MINT: Evaluating LLMs in Multi-turn Interaction with Tools and Language Feedback

- Decision: Accept
- Scores: 6, 8, 8, 5

## Abstract
To solve complex tasks, large language models (LLMs) often require multiple rounds of interactions with the user, sometimes assisted by external tools.
However, current evaluation protocols often emphasize benchmark performance with single-turn exchanges, neglecting the nuanced interactions among the user, LLMs, and external tools, while also underestimating the importance of natural language feedback from users. These oversights contribute to discrepancies between research benchmark evaluations and real-world use cases.
We introduce \textbf{\approach}, a benchmark that evaluates LLMs' ability to solve challenging tasks with \textbf{m}ulti-turn \textbf{int}eractions by (1) using tools and (2) leveraging natural language feedback.
To ensure reproducibility, we provide an evaluation framework where LLMs can access tools by executing Python code and receive users' natural language feedback simulated by GPT-4.
We repurpose a diverse set of established evaluation datasets focusing on reasoning, coding, and decision-making and carefully curate them into a compact subset for efficient evaluation.
Our analysis of 20 open- and closed-source LLMs offers intriguing findings.
(a) LLMs generally benefit from tools and language feedback, with performance gains (absolute, same below) of 1--8\% for each turn of tool use and 2--17\% with natural language feedback.
(b) Better single-turn performance does not guarantee better multi-turn performance.
(c) Surprisingly, among the evaluated LLMs, supervised instruction-finetuning (SIFT) and reinforcement learning from human feedback (RLHF) generally hurt multi-turn capabilities.
We expect \approach can help measure progress and incentivize research in improving LLMs' capabilities in multi-turn interactions, especially for open-source communities where multi-turn human evaluation can be less accessible compared to commercial LLMs with a larger user base.
\footnote{Code is available on our project website: \url{https://xingyaoww.io/mint-bench}}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper introduced MINT, a benchmark for evaluating LLMs when they can interact with external tools and natural language feedback. In the benchmark environments, "tools" are considered as functions that can be called by executing the LLM-generated Python code, and "natural language feedback" is simulated using GPT-4. The benchmark covers tasks such as math reasoning and code generation, where only instances that require multiple turns of interaction are retained. In experiments, a comprehensive set of open/closed-source LLMs are evaluated on MINT.

### Strengths
1. LLM evaluation in an interactive environment is an important and novel topic.
2. Experiments on a comprehensive set of LLMs under different settings (base vs. SIFT vs. RLHF, open-source vs. closed-source) were conducted, resulting in several interesting observations (e.g., RLHF may hurt LLM-tool interaction while SIFT helps).
3. The paper is easy to follow.

### Weaknesses
My major concerns lie in the natural language feedback simulation setup:
1. The example in Figure 1 seems to assume a "collaborative work" interaction between the LLM and the user, as opposed to the more common case where a user seeks assistance from the LLM; in the latter case, it is not practical to assume such detailed feedback from the user because the user does not know how to solve the problem (otherwise they have no need to seek help from the LLM). In some sense, the current LLM-user interaction has made the user a "teacher" who instructs the LLM to correct its mistakes. The feedback provided in Figure 1, such as "You should have used ... Then you can express...", implies a user with detailed procedural knowledge, which is unrealistic for a user seeking assistance. This contrasts with scenarios where users might provide more general feedback like "this is not what I want" or "the result is incorrect". This discrepancy between the simulated feedback and realistic user feedback should be addressed. In fact, user feedback has been widely studied in code generation/semantic parsing tasks (references below, which are missing in related work discussion). Prior work has particularly focused on collecting or simulating natural language feedback that is close to "what a prospective, help-seeking user in practice could give". While MINT's feedback interaction is still valuable (as it assesses how well an LLM can incorporate the feedback, no matter if it is realistic or not), I'd like to note that its kind of feedback may not reflect the realistic case, and this should be clarified in the paper.

    References:
    - Ziyu Yao, Yu Su, Huan Sun, and Wen-tau Yih. 2019. Model-based Interactive Semantic Parsing: A Unified Framework and A Text-to-SQL Case Study. In Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP), pages 5447–5458, Hong Kong, China. Association for Computational Linguistics.
    - Ahmed Elgohary, Saghar Hosseini, and Ahmed Hassan Awadallah. 2020. Speak to your Parser: Interactive Text-to-SQL with Natural Language Feedback. In Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics, pages 2065–2077, Online. Association for Computational Linguistics.
    - Hao Yan, Saurabh Srivastava, Yintao Tai, Sida I. Wang, Wen-tau Yih, and Ziyu Yao. 2023. Learning to Simulate Natural Language Feedback for Interactive Semantic Parsing. In Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pages 3149–3170, Toronto, Canada. Association for Computational Linguistics.

2. The human evaluation of GPT-4 generated feedback does not look at the discrepancy mentioned above either.

3. As indicated in footnote 4, evaluating one LLM using MINT costs around 100 USD, due to the use of GPT-4 for feedback simulation. This cost can be an issue for iteratively improving (and then evaluating) an LLM. 

Other than the feedback simulation, another comment on the tool interaction:

4. The current tool use has been limited to Python function calls. It offers better reproducibility but also loses the benchmark scope.

### Questions
1. Can the authors respond to my comment on the feedback simulation discrepancy?
2. Can the authors share thoughts on reducing the benchmark cost?
3. Can MINT be integrated with AgentBench (Liu et al., 2023) or InterCode (Yang et al., 2023), so that a larger task scope could be facilitated with both tool and user interaction?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The paper investigates the capabilities and limitations of large language models (LLMs) when solving tasks with multi-turn interactions by using tools and leveraging natural language feedback. The main contributions of the paper can be summarized as follows:
(1) The authors propose a structured evaluation framework where LLMs can leverage tools via executing Python code and receive users' natural language feedback;
(2) The authors have conducted abundant experiments, analyzing 20 open- and closed-source LLMs over 8 datasets.
(3) From the experiments, the authors have made some interesting observations, like RLHF may hurt multi-turn interaction performances in problem solving.

### Strengths
- The authors introduce MINT, a novel benchmark and framework, that evaluates LLMs' capabilities to solve tasks with multi-turn interactions with tool usage and natural language feedback.
- The authors conduct abundant experiments, covering 20 open- and closed-source LLMs and 8 datasets from different tasks.
- The authors have made some interesting statements, including (1) better single-turn performance does not guarantee multi-term performance; (2) RLHF may hurt the multi-turn capabilities. Corresponding experimental results and analysis are included to support the claims.
- The paper is well-written and is easy-to-follow. The visualizations are also clear and can help readers better understand the framework and model performance comparisons.

### Weaknesses
Overall, this is a very thorough and comprehensive benchmark paper. I have only several concerns: 
- The authors claim that the SIFT can benefit models' capabilities of tool-augmented task-solving in multi-turn interaction (section 3.2), while the authors also claim that the SIFT can hurt models' ability to leverage feedback (Section 3.3). Why do these two claims seem to contradict each other? Specifically, the paper does not clearly delineate the conditions under which SIFT improves or degrades performance, making it difficult to understand the underlying mechanisms. It's unclear if the observed trade-off is due to the nature of the training data, the specific tasks, or some other factor. For example, does SIFT training on a dataset with a high density of multi-turn interactions lead to better tool use but worse feedback utilization, and vice-versa? The paper should provide a more nuanced analysis of these factors.
- I am also very curious about the trade-off between tool-use capabilities and abilities to leverage human feedback. SIFT on general domain multi-turn interaction data (like ShareGPT, in section 3.2) can bring performance gain in problem-solving. I think this might be because of the multi-turn feature that caters to the final application. I also think if the model can SIFT on some task-specific data (if exists), the performance can also improve. I am very curious about which is more important for SIFT. The paper does not explore the impact of task-specific SIFT training data, which could be a significant factor in determining the optimal balance between tool use and feedback utilization. It would be beneficial to understand if task-specific SIFT training leads to better performance on those tasks, and if this improvement comes at the cost of reduced ability to leverage feedback.

### Questions
See weaknesses.

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents MINT, a benchmark that evaluates LLMs’ multi-turn interaction capabilities, in particular when LLMs are using external tools and provided with natural language feedback from users (simulated by GPT-4). The experiments use a subset of existing evaluation datasets on reasoning, coding, and decision-making tasks, resulting in 586 instances, which require multi-turn interaction (judged by GPT-3.5). 
The authors compare 20 open- and close-sourced LLMs on these instances and present 7 findings (listing them in order to easily refer to them in the other parts of the review):  

1. All models benefit from tool interaction and natural language feedback
2. Better single-turn performance does not lead to better multi-turn performance
3. There is a notable gap between open- and closed-source LLMs in multi-turn interaction performance
4. Models trained with supervised instruction fine-tuning (SIFT) and reinforcement learning from human feedback (RLHF) perform worse in multi-turn settings 

From the text:

5. LLMs’ feedback-providing capability could be orthogonal to task-solving ability
6. MINT’s evaluation reveals undesired artifacts in ShareGPT data
7. GPT-4 simulated language feedback is as helpful as human-written feedback based on human evaluation and task performance.

### Strengths
* The work studies a **timely, important topic** of LLMs’ evaluation in interactive settings, striving to bridge the gap between traditional static/single-turn benchmarks in NLP and “real-world use cases” (as noted in abstract). The use of LLMs as a proxy for human feedback reduces cost significantly and increases scalability.
* The paper is overall **well-written** and the design of the experiments seem **sound**. In addition, I find the **details of the experiments** are properly documented either in the main paper or appendix.
* Even if the exact numbers in the findings are likely to become less relevant in the future due to the fast-changing landscape of LLMs, the **high-level findings and takeaways are likely to be still relevant**, especially about single-turn vs. multi-turn performance between models (e.g., #2 and #4).

### Weaknesses
Although the paper presents many interesting findings, it wasn’t clear to me which ones are **new findings vs. confirmation of existing findings**. For instance, #1 has been shown by ToolLLM (Qin et al., 2023), Tool Augmented Language Models (TALM) (Parisi et al., 2022), Chain of Hindsight (Liu et al., 2023), etc.;  and #2, #3, and #4 have been (fully or partially) shown by Human-AI Language-based Interaction Evaluation (HALIE) (Lee et al., 2023); and #7 has been studied by Liu et al. (2023), Chiang & Lee (2023), Gao et al (2023), Shen et al (2023), and Duan et al. (2023). Situating the findings in the existing literature will give this work more validity and help readers understand the contributions of the paper.

For that reason, it is a bit unclear to me what the **main contribution of this paper** is at the moment. In comparison to prior work, the authors note that “Different from prior work, MINT covers a range of diverse tasks and is designed to measure the multi-turn interaction capabilities of LLMs with both tools and user feedback that are more aligned with real-world applications.” As some of the prior work covers a range of diverse tasks/measures multi-turn interaction capabilities of LLMs/simulates human feedback with LLMs, the main difference of this work is (presumably) accounting for **the use of tools and user feedback** on top of all of these elements. In this case, I wonder if it'll help to scope the description of the tasks more tightly (e.g., tasks that can benefit from tool use, as opposed to open-ended generation) and provide a bit more justification for why it’s important to look at these elements altogether (as there are prior work looking at the tool use and NL feedback) and what we expect to see (do we expect to see different results when these elements are added? do we actually observe any interesting interplay between these elements or is it merely a simple performance boost across all models?).

Maybe another bit that’s quite important to convey nuanced findings in the paper is the comparison of GPT-4-generated feedback to human-written feedback. Although the surface-level similarity and helpfulness are similar, my guess is that GPT-4 generated feedback lacks the variability that we’d normally observe in human-written feedback, which can easily affect these models’ performance (e.g., Lee et al., 2023). The limitation section in the appendix mentions coverage of GPT-4 generated feedback, which is relevant but different from this point.

Similarly, although I generally agree that this is a step towards including more real-world-like elements compared to evaluating LLMs without tool use and natural language feedback, I wouldn’t say that the current setup is strictly “more aligned with real-world applications” than prior work as there is a clear trade-off due to simulating human-written feedback with LLMs and potential drawbacks with the simulation (e.g., Koo et al. (2023), Rajani et al. (2023)).

In finding #3, could the size of a model be the main confounder? Is the finding only applicable to multi-turn settings or also in single-turn settings?

### Questions
* Most of the questions that can change my opinion are described in the weaknesses. I'm generally excited about the direction of the paper, and with clarification and contextualization of this work’s contributions and findings with respect to prior/concurrent work, I’d be happy to reconsider and adjust my ratings. Here, I list some questions/comments I had while reading the paper.
* Maybe another bit that’s quite important to convey nuanced findings in the paper is the comparison of GPT-4-generated feedback to human-written feedback. Although the surface-level similarity and helpfulness are similar, my guess is that GPT-4 generated feedback lacks the variability that we’d normally observe in human-written feedback, which can easily affect these models’ performance (e.g., Lee et al., 2023). The limitation section in the appendix mentions coverage of GPT-4 generated feedback, which is relevant but different from this point.
* Similarly, although I generally agree that this is a step towards including more real-world-like elements compared to evaluating LLMs without tool use and natural language feedback, I wouldn’t say that the current setup is strictly “more aligned with real-world applications” than prior work as there is a clear trade-off due to simulating human-written feedback with LLMs and potential drawbacks with the simulation (e.g., Koo et al. (2023), Rajani et al. (2023)).
* In finding #3, could the size of a model be the main confounder? Is the finding only applicable to multi-turn settings or also in single-turn settings?

### Soundness
4 excellent

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper evaluates LLMs in multi-turn interaction with the help of tools and language feedback. The authors introduces the MINT benchmark composing of code generation, decision making, and reasoning tasks, and compared 20 open- and closed-source LLMs. Results show that LLMs benefit from multiple rounds of tool-use and language feedback, and LLMs trained with supervised instruction-finetuning (SIFT) and RLHF may hurt multi-turn performance. Moreover, better single-turn performance does not generalize to better multi-turn performance.

### Strengths
1. This paper proposes an interesting MINT benchmark to evaluate multi-turn interactions using code execution and language feedbacks. The modification of using a unified subset of examples across a bundle of tasks would be useful for the community in general.
2. Results showing that supervised instruction-finetuning and RLHF may hurt model performance of multi-turn interactions with tools and language feedback, and worse performance on multi-turn compared to single-turn, may suggest that multi-turn interaction data is required. This provides valuable suggestions to alignment research.

### Weaknesses
1. There is no comparison to simple baselines, such as self-critic (which is essentially a special case of multi-turn interactions defined in this paper). Other baselines include only providing binary feedback, or sample k times and ask a LLM to select the final answer. Without such baselines, it is not clear how much language feedback the model actually incorporates in. Furthermore, I generally like the idea t hat using a LLM to provide feedback can improve a model's performance in general, but can the authors provide any benefit (such as efficiency) comparing using a large LLM as a feedback provider, compared to using a LLM to generate the results directly (either using self-critic or not)?
2. The proposed MINT dataset is relatively biased towards math problems that specifically require code execution and can benefit from explicit human feedback (e.g., correct or incorrect).  It seems that the only tool used is the python execution tool. Compared to other papers leveraging tools (toolformer, ReAct), the claim of utilizing tools through turns would improve model performance is not very convincing, especially for tasks that may not require code execution (e.g., HotpotQA). Moreover, I agree that selecting a subset of datasets would hinder fair comparisons, but sampling for instances, only 43 examples for HotpotQA (which is arguably the only multihop-qa dataset in MINT) may not be statistically large enough to represent the performance on the dataset. More importantly, MINT is limited to multi-turn interactions using the specific code tools and language feedback used in this paper, not the more natural and systematic tasks that require multi-turn interactions.
3. Accordingly, results suggesting that for example, "better single-turn performance does not guarantee better multi-turn performance" and "RLHG may hurt multi-turn capabilities" are limited to the setup that those worse performance would largely be due to "less viable of incorporating feedback" rather than necessarily indicating that they are indeed worse on multi-turn interactions with agents in general. Therefore, the claims are not well justified.

### Questions
1. Where did you compare to the "Lazy User-LLM Interaction"? Or is this only for k=1?
2. The proposed method is very similar to the Tree-of-thought paper (Yao et al., 2023) where the authors used LMs as a feedback/reward provider.

Yao et al., 2023. Deliberate Problem Solving with Large Language Models.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
