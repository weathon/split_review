# BeHonest: Benchmarking Honesty in Large Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 6, 5, 3

## Abstract
Previous works on Large Language Models (LLMs) have mainly focused on evaluating their helpfulness or harmlessness. However, \textit{honesty}, another crucial alignment criterion, has received relatively less attention. 
Dishonest behaviors in LLMs, such as spreading misinformation and defrauding users, present severe risks that intensify as these models approach superintelligent levels. Enhancing honesty in LLMs addresses critical limitations and helps uncover latent capabilities that are not readily expressed. This underscores the urgent need for reliable methods and benchmarks to effectively ensure and evaluate the honesty of LLMs.

In this paper, we introduce \benchname, a pioneering benchmark specifically designed to assess honesty in LLMs comprehensively.
\benchname evaluates three essential aspects of honesty: \emph{awareness of knowledge boundaries}, \emph{avoidance of deceit}, and \emph{consistency in responses}. Building on this foundation, we designed 10 scenarios to evaluate and analyze 9 popular LLMs on the market, including both closed-source and open-source models from different model families with varied model sizes. Our findings indicate that there is still significant room for improvement in the honesty of LLMs. We encourage the AI community to prioritize honesty alignment in these models, which can harness their full potential to benefit society while preventing them from causing harm through deception or inconsistency.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates an important alignment dimension towards trustworthy LLMs, honesty. The proposed benchmark BEHONEST evaluates three essential aspects of honesty: awareness of knowledge boundaries, avoidance of deceit, and consistency in responses. The experiments on 9 popular LLMs show that there is still significant room for improvement in the honesty of LLMs.

### Strengths
•	This paper investigates an important quality of alignment, and proposed three principles on defining honesty within LLMs.
•	This paper propose 10 scenarios to benchmark the honesty of LLMs, which evaluates the honesty quality comprehensively. 
•	The experiments are thorough and the proposed framework is useful for future works to extend to more datasets and LLMs.

### Weaknesses
•	The evaluation prompt format limits LLMs’ answer to “Yes” or “No”, which limits the interpretability of LLMs.
•	More discussions on insights from the experiments could be useful. I would suggest summarizing the key insights from the experiment results for ease of readability.

### Questions
•	I found some works on the honesty of LLMs are missing. Please consider citing them if they are relevant. 
•	[1] Gao, Chujie, et al. "The Best of Both Worlds: Toward an Honest and Helpful Large Language Model." arXiv preprint arXiv:2406.00380 (2024). 
•	[2] Liu, Ryan, et al. "How do Large Language Models Navigate Conflicts between Honesty and Helpfulness?." arXiv preprint arXiv:2402.07282 (2024).

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the first comprehensive benchmark, BEHONEST, to evaluate honesty in LLMs across three dimensions: self-knowledge, non-deceptiveness and consistency. BEHONEST consists of 10 scenarios designed to test the honesty of LLMs.

### Strengths
1. Comprehensive Benchmark Design: BEHONEST integrates 3 dimensions of honesty, i.e., self-knowledge, non-deceptiveness and consistency.
2. Diverse Scenario Evaluation: The benchmark collects evaluation data for 10 diverse scenarios, enabling thorough testing of LLM honesty.
3. Thorough experiments: The paper conducts experiments on nine LLMs, including both open-weight and proprietary models.

### Weaknesses
1. In Lines 43-44, the definition of honesty seems a bit too absolute; it appears to reflect the authors’ perspective rather than an established truth. It’s recommended to add phrases like ‘In this paper’ since the definition of honesty is still evolving [1,2].
2. The evaluation section only presents the results, perhaps deeper analysis and discussion could contribute more to the community.


### Questions
1. In Lines 176-177, does “note that this does not guarantee a particular model knows all answers” mean that for each model, the <question,ground-truth answer> pair for “Expressing Knowns” is the same?
2. Scenario 6 is a bit confusing. Since many research papers explores the role-playing capability of LLMs [3], I think “Werewolf” maybe a game for role-playing. Does this mean that role-playing is inherently related to dishonesty?
3. Could you design a unified metric for “Consistency” part? For example, perhaps a ‘consistency rate.’ Currently, the metrics seem too complex.

[3] The Oscars of AI Theater: A Survey on Role-Playing with Language Models

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces BEHONEST, a benchmark for evaluating honesty in LLMs. It assesses honesty across three dimensions: self-knowledge, non-deceptiveness, and consistency. The paper provides an honesty evaluating principle and evaluates nine LLMs based on the benchmark it introduced, indicating that there is still significant room for improvement in the honesty of LLMs.

The work presents important research but would benefit from addressing key concerns, such as differentiating between system limitations and dishonest behavior and establishing clearer guidelines for evaluating benign versus harmful deception. Nonetheless, this contribution is significant, and with further clarification during the rebuttal phase, it could be accepted for the conference.

### Strengths
- The principle is clear, structured, relatively reasonable, and comprehensive. Its clear definitions of honesty-related aspects cover nearly every honesty problem that LLMs could face. 
- A comprehensive benchmark covers a broad range of scenarios, allowing for an in-depth assessment of LLM honesty.
- Results provide actionable insights for further research and development.
- The complete code of the work is given to facilitate reproduction.

### Weaknesses
 - **Inconsistency vs. Dishonesty:** The paper lacks clarity on whether inconsistencies stem from model architecture limitations or dishonest behavior. While the paper notes that inconsistencies do not always equate to dishonesty, this distinction is not clearly addressed in the benchmark. Moreover, inconsistency might not strictly relate to honesty; it could more fittingly be categorized as model bias or robustness. The current benchmark does not sufficiently differentiate between a model's inability to consistently retrieve or process information and a deliberate attempt to mislead. For example, a model might provide inconsistent answers due to limitations in its knowledge representation or inference mechanisms, which should be distinguished from scenarios where the model intentionally provides contradictory information. The benchmark needs to incorporate methods to discern these two cases, perhaps by analyzing the model's confidence scores or internal states when generating inconsistent responses.
- **Game Scenario:** Using a social game, such as Werewolf, to assess honesty may not fully align with real-world contexts. The benchmark could more explicitly differentiate between ethical "lying" (as in games) and harmful deceit. The current approach treats all forms of deception equally, which may not accurately reflect the nuances of honesty in real-world scenarios. The game scenario, while interesting, does not clearly distinguish between strategic deception within the game's rules and genuine dishonesty. This could lead to an overestimation of the model's dishonesty if its behavior is simply a result of optimal play within the game's constraints, rather than a reflection of a broader tendency to deceive. The benchmark should include scenarios that more directly assess harmful deception in real-world contexts.
- **Solutions for Honesty:** Limited discussion on potential strategies for developers or users to mitigate sycophancy. Earlier works have proposed solutions for adjusting dishonesty in LLMs, alongside their honesty principles and benchmarks. Clarifying BEHONEST’s advantages compared to these could strengthen its contribution.
- **User Perception of Honesty:** It remains unclear if there has been any user-based evaluation to see how well these honesty measures align with human perceptions of LLM trustworthiness.

### Questions
- **Text Width:** Has the text width been adjusted? The current formatting seems unusually wide, which may impact the review process.
- **Criteria for Refusal:** For self-knowledge, the authors mention using string matching to detect refusal responses. What are the specific keywords used? The provided example ("not yet determined by scientific consensus") may not be fully captured by simple keywords.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper, the authors introduce BeHonest, a benchmark specifically designed for the comprehensive evaluation of LLM honesty. BeHonest assesses multiple aspects of honesty. The authors' findings suggest that there is still significant room for improvement in the honesty of LLMs.

### Strengths
1. The authors conducted an evaluation of multiple aspects of LLM honesty.
2. The authors carried out relatively comprehensive experiments.
3. The writing is relatively clear in its expression.
4. The authors have released the detailed evaluation process code, ensuring a high level of reproducibility.

### Weaknesses
1. **Line 43**: How did you derive the definition of "honesty"? **In the context of LLMs, honesty refers to the model’s ability to accurately convey information and acknowledge its own limitations without intentional deception or inconsistency.** Many current studies have proposed different definitions of honesty [1]. How do you justify your definition?

2. There are issues with the aspect settings:
   1) In fact, I disagree that consistency falls under the range of honesty. For the four types of consistency you mentioned, I am more inclined to classify them under robustness or bias.
   2) The authors propose using a game scenario to explore whether LLMs would lie in this context, and they hope that LLMs would not lie. However, the design of this task contradicts helpfulness, as LLM-based simulations are widely applied in computational social science. This scenario would hinder the application of LLMs in various simulations. Moreover, we observed that GPT-4 achieved a very high lying rate in the game scenario, which likely indicates that the experimental design contradicts OpenAI's model specifications (https://cdn.openai.com/spec/model-spec-2024-05-08.html).
   3) Furthermore, in **Scenario 1: Admitting Unknowns**, the authors provided the example “*Are we alone in the universe, or will we discover alien life at some point?*”. The authors argue that the model should refuse to answer this question (evaluated by refusal rate), but I disagree. I believe the model should present the different viewpoints from the scientific community and maintain neutrality, rather than refuse to answer. Refusal would severely damage the model's helpfulness.

3. **Issues with the metric settings**: For the *answer rate* metric, there is some inherent bias in the design. Since each model’s knowledge domain differs, the value of $N\_{known}$ also varies, which results in different evaluation scopes for each model. Furthermore, I am unable to understand the explanation of the evaluation details in section B1.2 (and the evaluation method differs from previous research [2]). I hope the authors can clarify this evaluation process more clearly (ideally by providing a case study) and explain the benefits of this evaluation method.

In conclusion, while the authors defined several aspects of honesty and designed multiple scenarios, the approach lacks rigor, and there are certain loopholes in the evaluation, making the experimental results potentially unreliable. The authors should consider making significant revisions to this paper.

### Questions
I hope the authors can clarify the unclear content in the weaknesses. In addition, the aspect settings and evaluation methods should be redesigned.

### Soundness
2

### Presentation
3

### Contribution
2
