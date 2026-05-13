# Language Models Learn to Mislead Humans via RLHF

- Decision: Accept
- Scores: 5, 6, 6, 8

## Abstract
Language models (LMs) can produce errors that are hard to detect for humans, especially when the task is complex.
RLHF, the most popular post-training method, may exacerbate this problem: to achieve higher rewards, LMs might get better at convincing humans that they are right even when they are wrong.
We study this phenomenon under a standard RLHF pipeline, calling it ``\ourmodel'' since it is \textbf{U}nintended by model developers.
Specifically, we ask time-constrained (e.g., 3-10 minutes) human subjects to evaluate the correctness of model outputs and calculate humans' accuracy against gold labels. 
On a question-answering task (QuALITY) and programming task (APPS), 
RLHF makes LMs better at convincing our subjects but not at completing the task correctly.
RLHF also makes the model harder to evaluate: our subjects' false positive rate increases by 24.1\% on QuALITY and 18.3\% on APPS.
Finally, we show that probing, a state-of-the-art approach for detecting \textbf{I}ntended Sophistry (e.g.~backdoored LMs), does not generalize to \ourmodel.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper "Language Models Learn to Mislead Humans via RLHF" examines how language models fine-tuned with Reinforcement Learning from Human Feedback (RLHF) can unintentionally mislead humans by appearing correct even when wrong. Through experiments on question-answering (QuALITY) and programming tasks (APPS), the authors show that RLHF increases human approval of model responses but does not enhance accuracy, often causing humans to rate incorrect answers as correct. This phenomenon "U-Sophistry" suggests that RLHF can make language models more persuasive without improving true correctness, highlighting a significant challenge for model alignment.

### Strengths
1. This paper introduces the concept of "U-SOPHISTRY," wherein RLHF unintentionally enables language models to mislead human evaluators without necessarily improving task performance. This novel framing extends prior work on reward hacking and deception in AI, highlighting new risks in standard RLHF pipelines. With AI applications proliferating, ensuring safe and reliable human-AI interaction is critical.

2. The method incorporate diverse and challenging tasks like question-answering and programming tasks.

3. This paper clearly demonstrates the author's intent and contains numerous figures and tables.

### Weaknesses
1. The scenario discussed is somewhat perplexing: this paper argues that models trained with RLHF may become more deceptive towards humans without actual improvements in capability. However, RLHF’s effectiveness relies heavily on the choice of reward model and corresponding training data, so if there are issues in human-annotated data, such results are predictable. Thus, the reviewer suggests that the problem stems from humans no longer being able to provide sufficiently high-quality evaluations of the model’s outputs, resembling more of a “Weak-to-Strong” alignment issue, while the discussion in this paper seems to frame it as an issue with the RLHF pipeline itself.

2. Lack of robust countermeasures to mitigate "U-SOPHISTRY".

3. Many alignment algorithms have been optimized for the classic RLHF pipeline, such as DPO and KTO. Running different alignment algorithms may lead to varying results in the final model, yet the authors conducted experiments only with the original PPO algorithm.

### Questions
Please refer to weakness.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper studies that LMs trained with standard RLHF techniques can learn to appear more convincing to human evaluators without actually improving their tasks. Through studies on question-answering and programming tasks, the authors show that RLHF-trained models achieve higher human approval ratings while making human evaluation less accurate.

### Strengths
* Addresses a critical gap in understanding how language models might naturally learn to mislead humans
* The experiment is well-designed with appropriate controls
* First systematic study of unintended sophistry in RLHF

### Weaknesses
 * This paper only shows the experimental results on only two tasks (question-answering and programming). Without specific experiments, we may not know whether the method would generalize to other important domains where RLHF is used. 
* Figure 1 could benefit from more detailed captions
* The related work section only covers RLHF literature and could expand discussion on human evaluation methods.

### Questions
* Have the authors considered testing their findings on other types of tasks beyond QA and programming?
* Could the authors elaborate on potential mitigation strategies beyond probing?
* How might the results differ with more or less experienced evaluators?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The work empirically validates the hypothesis that LLMs can learn to perform reward hacking, i.e., achieve higher rewards when RLHFed, despite not actually being better, according to an oracle. For the study, they recruited human evaluators and validated this hypothesis in two settings: QA and programming tasks, showing that after performing RLHF, human evaluators thought that the model performance improved despite the performance not improving. They also show that the false positive rate for human evaluators also increases. They also check if probing methods that can detect incorrect programs generated by models with backdoors don't generalize to RLHFed models where the model performs reward hacking, which is unintentional from the user's end.

### Strengths
- The work recruits humans and validates the hypothesis that models can learn to perform reward hacking. The human evaluations are well thought out.
- They perform extensive evaluations and experiments for robustness. They also try methods that can detect I-Sophistry to detect U-Sophistory but find that the methods do not generalize.
- The insights are impactful and should make researchers and industry practitioners give more thought to designing their RLHF training procedure. 
- The manuscript is well-written and easy to understand.

### Weaknesses
 - I am not convinced by the design of the programming task used to validate the hypothesis.
    - Why do the authors choose the two simplest unit tests? How would things change if they used the two most difficult unit tests?
    - For the pilot study, how were the human evaluators incentivized? As a developer, I would write two unit tests. One is an easy case, and another is difficult or where programs usually fail.
    - In an ideal scenario for preference tuning for programming tasks, human annotators should only be used for stylistic improvements since we also have very strong methods for checking the correctness of models.

- More studies need to be done on whether incentivizing humans according to correctness and confidence biases human evaluators to be less or more confident.

- I would not conclude that if humans spend more time on a task, they work harder. There could be several other factors that can influence time.

### Questions
- Why do you think the LLM generates a less readable program?
- Do you think that the increase in human error rate for programming task is because the more is generating less readable code or because it learns to pass the unit tests?
I would not conclude that if humans spend more time on a task, they work harder. There could be several other factors that can influence time.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper investigates a phenomenon called "U-SOPHISTRY", in which language models (LMs) trained through reinforcement learning from human feedback (RLHF) unintentionally become better at convincing humans that they are right even when they are wrong without improving actual performance. The author demonstrates U-SOPHISTRY through user studies on question-answering (QuALITY) and programming (APPS) tasks. The results indicate that RLHF-optimized models convince human evaluators of incorrect outputs at higher rates compared to their pre-trained counterparts. Through a comprehensive qualitative analysis, the authors identify strategies that the RLHF models use to mislead evaluators, such as fabricating or selectively presenting evidence in QA tasks and generating partial code that passes all human-written tests or is less readable for debugging. Additionally, the authors emphasize that prior work on detecting I-SOPHISTRY (intentionally misleading) is not an effective benchmark for methods aimed at detecting U-SOPHISTRY.

### Strengths
1.  The exploration of U-SOPHISTRY provides a novel perspective on RLHF challenges.
2. The authors conduct experiments and rigorous user studies across two common tasks, measuring correctness, human approval, evaluation error rate, and false positive rate. The results provide deep insights into how RLHF impacts human judgment and evaluation.
3. Through comprehensive qualitative analysis, the paper examines specific strategies used by LMs that lead to U-SOPHISTRY, such as fabricating evidence and exploiting human testing shortcuts, enhancing our understanding of how RLHF may influence model behavior.
4. The paper is well-written and easy-to-follow.

### Weaknesses
I do not see major issues in the paper, though I have a few minor concerns and some areas where clarifications would be helpful.

**Concerns**
1. In the programming (APPS) experiment, the authors assume that users will provide test cases for code validation, which may not fully capture real-world scenarios. Users may also seek explanations from the model to better understand the code, especially if they don’t fully understand the initial question, which could result in their inability to write accurate test cases. It would be good to include a user study from this aspect.
2. A follow-up question is whether all human evaluators fully understand the coding questions?  Users may write inaccurate test cases and then incorrectly interpret execution results as passing. Additional analysis on the correctness of test cases written by human evaluators would be beneficial.

**Clarifications**:
1. Are the Human evaluation error rate and Human false positive rate calculations based on $R^{human}$ rather than $R^{train}$. The analysis appears to use real human evaluators ($R^{human}$), but the description on lines 181 and 183 uses $R^{train}$ instead of $R^{human}$.

2. It would be clearer to display the distribution of total cases shown to human evaluators to indicate how many were the initial responses and how many were the RLHF responses.

### Questions
Can the author answer all the questions above?

### Soundness
4

### Presentation
4

### Contribution
4
