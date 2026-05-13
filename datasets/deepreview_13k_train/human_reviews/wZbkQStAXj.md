# PersonaEval: Benchmarking LLMs on Role-Playing Evaluation Tasks

- Decision: Reject
- Scores: 5, 5, 3, 3

## Abstract
Role-playing in large language models (LLMs) has become a crucial area of research, enabling models to simulate diverse personas and tailor responses, significantly impacting natural language understanding and human-computer interaction. However, while advanced LLMs like GPT-4 are used to evaluate role-playing methods, their reliability in providing accurate assessments remains uncertain, especially in distinguishing nuanced role-playing characteristics. In this paper, we introduce PersonaEval, a benchmark designed to assess the effectiveness of LLMs in role-playing evaluation tasks. We frame the problem as a classification task to determine whether an LLM evaluator can distinguish between sentences from different levels of expertise based solely on linguistic cues. Using real-world data from the Wired 5 Levels video series—where experts explain concepts to five distinct audiences: a child, a teenager, a college student, a graduate student, and another expert—we design three evaluation settings that correspond to commonly used LLM evaluation approaches: single answer role grading, pairwise role comparison, and reference-guided role grading. These settings aim to capture various aspects of how effectively LLMs evaluate role-playing performance. Our study highlights the limitations of current LLMs in persona evaluation tasks and underscores the need for further research to enhance their evaluation capabilities. We provide a foundation for future work aimed at improving the accuracy and professionalism of LLM evaluators in role-playing contexts.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
- This work introduces a benchmark designed to evaluate whether large language models (LLMs) can distinguish sentences by speaker expertise levels using only linguistic cues, utilizing data from the Wired 5 Levels video series.
- It presents three evaluation settings specifically tailored to assess LLM performance in role-playing tasks.
- The study finds that GPT-4o achieves the highest performance overall; however, distinguishing roles based on explanation-focused cues is more challenging than from the listener's perspective. Additionally, the amount of contextual information provided significantly impacts the accuracy of role differentiation.

### Strengths
- The authors effectively motivated the issues surrounding the reliability of LLM evaluators in role-playing tasks.
- This work covered three comprehensive evaluation settings—single-answer grading, pairwise comparison, and reference-guided evaluation—aligning well with established LLM evaluation methodologies.

### Weaknesses
 - The Wired 5 Levels video series emphasizes informative content, leading the benchmark to focus primarily on informative conversations. The coverage may be limited.
- While the authors argue that familiar character archetypes reduce performance risks from role unfamiliarity, this approach may also limit the benchmark’s validity in more diverse user scenarios/user types. Specifically, the use of educational levels as archetypes might introduce biases related to perceived communication styles and knowledge levels associated with these roles, rather than focusing on the linguistic cues themselves.
- The related work section on role-playing evaluation could more directly address specific issues and contributions within role-playing tasks, as it currently focuses on general LLM evaluation methods. It lacks a detailed discussion of existing benchmarks or methodologies specifically designed for evaluating role-playing capabilities in LLMs.
- This work showed that distinguishing roles using explanation-focused cues is challenging. This can be because LLMs may rely more on language style than on informational depth. A detailed analysis of benchmark sentence differences between explanation and listener-focused parts could clarify these findings. Furthermore, the analysis should consider not just the presence of specific words but also the complexity of sentence structures and the use of domain-specific terminology.
- The relatively low performance observed in user study raises questions about the task's suitability. While distinguishing between roles like "graduate student" and "undergraduate student" might imply an ability to detect subtle differences, it could also reflect inherent biases about the expected characteristics of each group. This leads to a critical question: is high performance in this task genuinely necessary to serve as an effective evaluator in role-playing tasks? The study should also consider whether the task is truly measuring the LLM's ability to understand role-specific linguistic cues or if it is simply identifying surface-level differences that may not be relevant to effective role-playing.

### Questions
- How does accurately predicting the speaker's level demonstrate reliability and effectiveness when using LLMs as role-playing evaluators?
- Given the 26 topics, were there any notable differences in performance by topic?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces PersonaEval, a benchmark designed to assess LLMs' effectiveness in evaluating role-playing through a classification task, utilizing data from the Wired 5 Levels series, where experts explain concepts to different audience types (child, teenager, college student, graduate student, and expert). The paper evaluates GPT-4, GPT-3.5-turbo, and various models from the Qwen family. The paper highlights limitations in current LLMs' ability to evaluate nuanced role-playing tasks.

### Strengths
+ Important research question, since many papers are using LLMs as evaluators.
+ Dataset constructed using real-world conversations from a famous TV series, including diverse topics and conversations from people of 5 different levels of knowledge.
+ Two aspects of using the dataset, i.e., the classification, and the comparison, with each aspect having two settings of w/ or w/o demonstrations.

### Weaknesses
 - The findings may not generalize to every LLM evaluators since the dataset is limited in its scope (first paragraph in the questions).
- There could be some deeper analysis like superficial correlation (shortcut learning). (question 8 & 9)
- Need further elaboration on settings (question 4 5 6 7)
- Need explanation about findings in this paper and related work (question 10)



### Questions
Given that many papers are using LLMs for evaluation, it is important to have a comprehensive evaluation on how LLMs can serve as evaluators. However, as I read the paper, I realize that the scope is limited to personas with different knowledge levels. I think the findings in this paper may not generalize to personas having nuanced personality traits, such as different levels of extraversion. The authors could add a discussion about this limitation in the paper.

I have some questions:

1.	Table 1: Is the “Avg Tokens” averaged on the scale of the whole dialogue or just one turn? It looks a bit weird that Child has a higher Avg Turns but lower Avg Tokens.
2.	For Table 2 & 3, could you please provide overall accuracy for each model?
3.	Could you provide the full list of the 26 topics in the appendix? I do take a look on the TV series website, but I cannot see clearly what the topics are.
4.	How many times do you run one LLM to obtain mean and std? What temperature, top_p, and other parameters do you set for LLMs?
5.	For pairwise evaluation, what is the difference between using Child – Teen and Teen – Child? Do they use the same dialogues but different questions (e.g., which is from the child/teen)?
6.	For pairwise evaluation, do you use dialogues in a same topic? If we select a child’s speaking from topic A while a teen’s speaking from topic B, how will LLMs perform?
7.	For pairwise evaluation, since the 5 levels (child, teen, undergrad, graduate, expert) are ordinal data, we can just ask LLMs which response shows the higher level of knowledge. This setting can do some interesting, such as we select two teen’s responses and ask LLMs which one is more knowledgeable (probably providing an option to indicate a tie).
8.	For pairwise evaluation, especially in the contradiction analysis (Table 4): since the contradiction rates for LLMs are relatively high, I am thinking is it because that there are some positional biases? E.g., the order of the two responses.
9.	Related to the previous one: I think it will be interesting if we can have some analysis on some superficial features, such as whether the length of the dialogue can indicate the speaker.
10.	Since the paper claims a limited performance of LLMs being evaluators, there is an inconsistency with findings in existing papers. For example, in the Wang et al., 2024b in your reference, they did a human study on checking whether GPT-4 can provide human-like judgment and found the correlation is high. Could you please explain the reason why you can show lower performance in LLMs? In other words, what are the flaws in existing papers as you mention: “Current approaches to using LLMs in role-playing evaluations are not without flaws.”
11.	I wonder how LLMs can simulate conversations of different expertise levels, that is, we instruct LLMs to speak and act like a teen, or a graduate student. Could you please discuss how your dataset can help in evaluating this aspect?

Overall, the presentation is good in this paper. There are still some minor issues:

1.	Line 88 “large language models (LLMs)” -> “LLMs” since the abbreviation has appeared before. Same as Line 257: “large language models” -> “LLMs”.
2.	Figure 2 is not referenced in the main text.

### Soundness
3

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
This paper introduces a benchmark designed to assess the capabilities of language models in evaluating role-playing performances, specifically focusing on their ability to discern and classify different levels of communication expertise. So, **it is about the meta-evaluation**. The benchmark utilizes transcripts from the Wired 5 Levels video series, where experts explain complex concepts to audiences of varying educational levels (child, teen, college student, graduate student, and expert).

The central premise is that a model's ability to classify these educational levels in dialogue could be **a proxy** for its potential effectiveness in evaluating role-playing models.

The paper presents three evaluation settings: single-answer role classification, pairwise role comparison, and reference-guided role classification. These settings test the model’s capability to distinguish and evaluate role-specific language.

One of the paper's goals is to provide insights that could improve the professionalism and precision of LLM-based evaluators in role-playing contexts.

### Strengths
1. The topic of role-play meta-evaluation is indeed a gap in current research.
2. Applying the Wired 5-level dataset for a task used as a proxy for role-play meta-evaluation is original.
3. The paper is well-structured and generally clear in its presentation.
4. It is good that three different evaluation settings (single-answer role grading, pairwise role comparison, and reference-guided role grading) are included. This comprehensive approach aligns well with various evaluation methodologies used in existing role-playing benchmarks.
5. Incorporating human performance comparisons adds value to the study. By providing this baseline, the paper offers crucial context for interpreting the models' results.

### Weaknesses
1. The paper does not support the central premise (see the summary section). It is implicitly assumed true throughout and might benefit from more explicit justification. The paper does not adequately address how well the performance on this benchmark might transfer to evaluating role-playing models. I'm unsure how to fix it, as it seems to be a global framing problem. The authors should probably add more datasets from different sources. Some potential problems are:
    * 1.1. The domain of conversations is specific to educational videos, which may limit generalizability to broader role-playing scenarios. It may introduce biases or limitations in the types of language and expertise levels represented.
    * 1.2. Role alignment is only one criterion out of many possible criteria for role-play evaluation.
    * 1.3. In the actual LLM role-playing conversation, one side is LLM. In the proposed task, both sides are humans.
    * 1.4. Archetypes are not roles. There are no detailed descriptions for them.
2. The paper could benefit from acknowledging and comparing with [the Judgemark benchmark](https://eqbench.com/judgemark.html), which assesses evaluators for creative writing without proxy tasks.
3. The supplementary code is poorly organized, and the results are challenging to reproduce. There are no instructions on how to run the scripts to get the results, and some comments and outputs are in Chinese. I’ve tried to reproduce some numbers from Table 2 (GPT-4o, 5 turns), and they are considerably different from the ones stated in the paper, outside of the confidence intervals stated in Appendix A.
4. Dataset collection methodology is not stated. As far as I can see, there is no explanation of how the videos were converted into a clean text dataset. I found at least two other papers using the same data source: ["A Dialogue Corpus for Learning to Construct Explanations"](https://aclanthology.org/2022.coling-1.27/) and ["Evaluating the Explanation Capabilities of LLMs in Conversation Compared to a Human Baseline"](https://arxiv.org/abs/2406.18512). None of them are cited in this paper.
5. Tables 2, 3, and 4 contain too much information. The numbers should support some hypothesis. Most of the numbers in these tables are unclear about why they are there or what hypothesis they support. Consider replacing precision/recall with f-measure and reporting only one number per model. Full tables can still be included in the appendices.

### Questions
### Questions
1. How exactly the dataset was obtained?
2. Why do you think your benchmark is general enough to be used for role-play meta-evaluation?
3. How are the users of your benchmark?
4. How are you going to support your benchmark? Are you going to support it at all?

### Suggestions
1. Please include an analysis of the costs for running these evaluations. Those are tracked in W&B and should be relatively easy to add.
2. The name "PersonaEval" might be reconsidered to reflect better the benchmark's focus on evaluating evaluators rather than personas directly. Also, "CharacterEval" is already out there, and it is easy to be confused with.
3. Line 530: The first sentence in the conclusion could be rephrased to more accurately reflect the paper's focus on evaluating LLMs' ability to assess dialogues rather than exploring role-playing capabilities directly.
4. Table 1: You should round the average number of tokens to the nearest integer. For instance, 585.23 -> 585. ".23" doesn't add any useful information.
5. Only three families of models are covered. You should probably add at least one more.
6. Fix the tables (weakness #5).
7. Appendix C should be in the main body of the paper. It explains linguistic clues that humans and models use to get their predictions.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
- A new benchmark designed to assess the effectiveness of large language models (LLMs) in role-playing evaluation tasks using real-world data from the Wired 5 Levels video series.

- Evaluation Settings: (1) Five-level classification task to determine expertise levels. (2) Pairwise comparison of role-based responses. (3) Reference-guided role grading with few-shot learning.

- Data is drawn from experts explaining complex topics to five distinct audiences (child, teenager, college student, graduate student, expert), testing the models' ability to adapt language to different knowledge levels.

- Current LLMs (e.g., GPT-4, GPT-3.5-turbo) show limitations in accurately evaluating role-playing tasks, particularly in distinguishing closely related roles.

- Incorporating reference examples (few-shot learning) improves model performance but is inconsistent across different models.

### Strengths
- While the use of the Wired 5 Levels dataset may not be ideal for all role-playing research, its application in this context is creative and introduces a fresh angle for evaluating how well models adapt to varied linguistic and comprehension levels.

- The evaluation settings—single answer grading, pairwise comparison, and reference-guided grading—are well thought out and align with standard LLM evaluation methodologies. This creates a good framework for assessing model performance in role-play scenarios.

- The paper is clearly structured, and the steps taken in developing PersonaEval are well explained. The use of real-world data and the clear description of different audience levels make it easy to understand the evaluation process and the dataset's relevance, even if it may not be universally ideal for role-playing research.

 - While the Wired 5 Levels dataset might not directly suit all role-playing applications, it provides a robust starting point for research into adaptive language use, making the work potentially useful in related fields like pedagogical AI or communication studies.

### Weaknesses
 - The link between the Wired 5 Levels dataset and persona role-playing feels underdeveloped. The five levels in the dataset represent different knowledge audiences but not distinct personas. This conflates the complexity of role-playing (adapting personality, tone, or behavior) with a different challenge—adjusting language complexity to suit expertise. Strengthening the theoretical connection between these two aspects is essential to ensure the benchmark addresses role-playing rather than just audience targeting. Clarify why expertise-based adaptation can serve as a proxy for persona role-playing. Alternatively, consider using or supplementing the dataset with interactions where LLMs adopt clearer, more defined personas beyond knowledge levels. Did the authors think of an ablation method?



- The Wired 5 Levels data may be too confounded to yield clear conclusions about role-playing. Since the dataset measures language complexity rather than behavioral adaptation, it becomes challenging to isolate whether LLMs are learning to play a role or simply to adjust based on cognitive ability. This makes it hard to draw strong conclusions about LLM performance in role-playing specifically. Introduce additional experiments that focus explicitly on personas, personality shifts, or role-driven interactions. This could help to better test how well LLMs modulate their responses in line with distinct personas rather than just shifting linguistic complexity. Linguistic complexity is also a rich research field, and there are many linguistic feature extractors and models out there.



- The claim that “most” role-playing research relies on LLM evaluation (lines 037-039) is overstated. While LLMs are widely used for evaluation tasks, the field is more diverse, with various supporting metrics often complementing LLM evaluations.  The role-playing research landscape is more diverse. (Kovač-2024, Lee-2024). Or they use some supporting metrics when they use LLM evaluations (Wang-2024).

(Kovač-2024) "Stick to your role! Stability of personal values expressed in large language models."

(Lee-2024) "Language Models Show Stable Value Orientations Across Diverse Role-Plays."

(Wang-2024) "Inch saracter: Evaluating personality fidelity in role-playing agents through psychological interviews."

### Questions
Do you have plans to reframe this research away from role-playing?

Given the nature of the Wired 5 Levels dataset, which focuses on adjusting explanations based on expertise rather than persona, do you intend to reframe the study towards a more fitting evaluation domain, like pedagogical adaptation or communication complexity? This research feels more aligned with tasks that involve adapting information for different audiences rather than role-playing, as it’s commonly understood in the literature.

### Soundness
2

### Presentation
3

### Contribution
2
