# SimpleToM: Exposing the Gap between Explicit ToM Inference and Implicit ToM Application in LLMs

- Decision: Reject
- Avg Score: 5.33
- Scores: 8, 5, 3

## Abstract
While prior work has explored whether large language models (LLMs) possess a ``theory of mind'' (ToM) -
the ability to attribute mental states to oneself and others - there has been little
work testing whether LLMs can {\it implicitly apply} such knowledge to predict behavior, or to
judge whether an observed behavior is rational. 
Such skills are critical for appropriate interaction in social environments. 
Our approach to study such capabilities is to create a new dataset, called \dataset{}, containing concise,
diverse stories (e.g., ``The can of Pringles has moldy chips in it. Mary picks up the
can in the supermarket and walks to the cashier.''), each with three questions that test
different degrees of ToM reasoning, asking models to predict
(a) mental state (``Is Mary aware of the mold?''),
(b) behavior (``Will Mary pay for the chips or report the mold?''), and
(c) judgment (``Mary paid for the chips. Was that reasonable?'').
To our knowledge, SimpleToM is the first dataset to systematically explore
downstream reasoning requiring knowledge of mental states in realistic scenarios.
Our experimental results are intriguing: While
most models can reliably predict mental state on our dataset (a), they often fail to correctly
predict the behavior (b), and fare even worse at judging whether given behaviors are reasonable (c),
despite being correctly aware of the protagonist's mental state should make
such secondary predictions obvious. We further show that we can help models do
better at (b) and (c) via interventions such as reminding the model of its earlier mental
state answer and mental-state-specific chain-of-thought prompting, raising
the action prediction accuracies (e.g., from 49.5\% to 93.5\% for GPT-4o)
and judgment accuracies (e.g., from 15.3\% to 94.7\% in GPT-4o). However, while this shows
that models can be coaxed to perform well, it requires task-specific interventions,
and the natural model performances remain low, a cautionary tale for LLM deployment.
SimpleToM thus breaks new ground in probing real-world ToM reasoning, and
reveals surprising, new insights about current model capabilities. We hope
the dataset enables further exploration by the community into this critical
area of model behavior.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper proposes a new dataset called SimpleToM, designed to assess existing large language models on their Theory of Mind reasoning abilities. SimpleToM features well-crafted, simple, and straightforward stories that cover a variety of scenarios and includes three types of questions: mental state questions (testing whether the model can infer a character’s awareness of key information), behavior prediction questions (assessing if the model can predict a character’s actions based on mental states), and judgment questions (evaluating if the model can determine the reasonableness of actions). The paper experiments with various inference-time interventions to improve the performance of LLMs and concludes that these interventions only temporarily enhance model performance, indicating that there is still significant potential for LLMs to improve their Theory of Mind capabilities.

### Strengths
- SimpleToM is a straightforward and comprehensive dataset for evaluating models' Theory of Mind abilities.
- The asymmetric information ensures diversity in the dataset, allowing for a more thorough assessment of models' capabilities, aligning better with the diversity characteristic of humans.
- This paper evaluates the Theory of Mind capabilities of both closed-source and open-source LLMs.
- The dataset is publicly available, and the experiments are highly reproducible.

### Weaknesses
 - The results and analysis in section5 are quite interesting, but each paragraph contains too many bolded words, making it difficult to follow the main points. Clarifying this section would improve readability.

- In Table 2, Llama-3.1-8B stands out as an outlier, compared with Llama-3.1-405B, it performs more than five times better in the judgment evaluation. I think this is an interesting case and I would expect to see more explanation for this outlier, such as potential reasons behind this unusual performance, would be more informative than simply labeling it as an outlier.

### Questions
I'm curious about whether the humans personality or demographic characteristics in the mental state phase might influence the model's mental state evaluation. Some ablation experiments would be insightful.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper exams whether LLMs can infer and more importantly, apply the mental state of character in stories. In particular, the author creates a dataset of stories where some key information is unknown for the character. Based on this foundation, the author proposes three tasks: mental state estimation, behavior prediction, and judgment of behavior. The experiment results show that LLMs without CoT can achieve high accuracy on the first task but fail in the others, which implies that LLMs fail to proactively make use of the mental state information for reasoning tasks. However, CoT drastically improves model's performance on the reasoning tasks.

### Strengths
1. The author proposes a new task with a new dataset. The author use rigorous crowdsourcing to ensure the correctness of the label, although there are some systematic bias (see Weaknesses).
2. The experimental design is thorough, including a wide range of SOTA LLMs and exploring various prompting strategies.

### Weaknesses
1. It’s unclear how this paper’s findings differ fundamentally from the large body of existing work that LLMs can acquire various types of knowledge (e.g., factual [1, 2, 3], ontological [4], or arithmetic skills (exactly mentioned in CoT paper)) but often struggle to apply this knowledge consistently in downstream tasks. Is reasoning about mental states inherently different in how it’s processed by LLMs compared to other types of knowledge?
2. It's also well-known that cot reasoning facilitate multi-step reasoning, and that task-specific instructions are generally helpful. Therefore, I'd expect the author to highlight any unique challenges that ToM reasoning poses for LLMs, distinguishing it from other forms of reasoning.
3.  The curated dataset appears biased. Every story assumes that characters are unaware of key information, and thus the ground-truth answer to the judgement question is always "reasonable". An ideal dataset would include a balanced mix of cases, with characters both aware and unaware.
4. While the author hints throughout the paper that low performance on SimpleToM with naive decoding may signal a risk for LLM deployment, this connection feels weak to me. I'd expect more concrete examples of applications where failing SimpleToM might lead to problematic outcomes.

### Questions
1. See Weakness 1 & 4
2. Why do models generally achieve higher accuracy in behavior prediction than in judgment tasks? Both tasks should require the same level of reasoning

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper introduces SimpleToM, a dataset designed to test large language models' (LLMs) ability to apply theory of mind (ToM) reasoning in practical scenarios. While previous research has explored whether LLMs possess ToM capabilities, this work specifically examines how well models can use ToM knowledge to predict and evaluate behavior in realistic situations. They created SimpleToM dataset featuring concise stories with Mental state prediction, Behavior prediction, and Rationality judgment questions. They demonstrated that current LLMs show uneven ToM capabilities and developed interventions to improve model performance in applied ToM.

### Strengths
* The paper introduces SimpleToM, a  well-designed dataset for evaluating both explicit and applied Theory of Mind capabilities in LLMs.
* The three-level assessment approach (mental state, behavior, judgment) is innovative and provides a more comprehensive evaluation framework than previous work.
* These results highlight an important gap in current LLM capabilities: understanding mental states in isolation versus applying that understanding to reason about behavior and make appropriate judgments.

### Weaknesses
1. The biggest weakness of this work is that **the motivation for evaluating the Theory of Mind (ToM) capabilities of large language models (LLMs) is not clearly articulated.** The statement in lines 49-50, "Given the increasing use of LLMs in human interactions... it is crucial to assess their ToM capabilities," does not sufficiently explain why these evaluations are necessary. Specifically, it remains unclear how improvements in "prediction" and "judgment" in certain human behaviors or narrative scenarios would benefit the practical application of LLM systems or AI agents. 
2. Your evaluation is based on performance in "applied" ToM , but it lacks consideration of how LLMs can improve outcomes in real-world applications, **it means while LLMs can demonstrate the ability to make "predictions" and "judgments" about behavior, whether these abilities align with their capacity to meet human expectations in real applications such as AI agents is a separate issue**. There seems to be a gap between these two aspects, and I hope the authors can provide more discussion on this matter.
3. The "RESULTS AND ANALYSIS" section lacks sufficient analysis of your results. For example, in lines 316-317, "Only the latest o1-preview model ... on this question type (84.1%)," you should provide an analysis of why built-in inference-time reasoning tokens improve the model's performance.
4. A human baseline is needed for your evaluation. As you mentioned in lines 42-43, "People infer what others know, anticipate their actions, and expect them to choose cost-minimizing behaviors," I think you should include an evaluation of human performance on your test for comparison.

### Questions
As mentioned in Weaknesses 1, I hope the authors can provide more details on the benefits of achieving a higher score in SimpleToM. Specifically, how does this relate to the performance of large language models or their applications in real-world scenarios?

### Soundness
2

### Presentation
2

### Contribution
2
