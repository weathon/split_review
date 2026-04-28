# SimulPL: Aligning Human Preferences in Simultaneous Machine Translation

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Simultaneous Machine Translation (SiMT) generates translations while receiving streaming source inputs. This requires the SiMT model to learn a read/write policy, deciding when to translate and when to wait for more source input. Numerous linguistic studies indicate that audiences in SiMT scenarios have distinct preferences, such as accurate translations, simpler syntax, and no unnecessary latency. Aligning SiMT models with these human preferences is crucial to improve their performances. However, this issue still remains unexplored. Additionally, preference optimization for SiMT task is also challenging. Existing methods focus solely on optimizing the generated responses, ignoring human preferences related to latency and the optimization of read/write policy during the preference optimization phase. To address these challenges, we propose Simultaneous Preference Learning (SimulPL), a preference learning framework tailored for the SiMT task. In the SimulPL framework, we categorize SiMT human preferences into five aspects: **translation quality preference**, **monotonicity preference**, **key point preference**, **simplicity preference**, and **latency preference**. By leveraging the first four preferences, we construct human preference prompts to efficiently guide GPT-4/4o in generating preference data for the SiMT task. In the preference optimization phase, SimulPL integrates **latency preference** into the optimization objective and enables SiMT models to improve the read/write policy, thereby aligning with human preferences more effectively. Experimental results indicate that SimulPL exhibits better alignment with human preferences across all latency levels in Zh$\rightarrow$En, De$\rightarrow$En and En$\rightarrow$Zh SiMT tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This works present a preference learning framework for simultaneous tasks like SiMT. Particularly, the proposed SimulPL framework categorizes SiMT human preferences into five aspects: translation quality preference, monotonicity preference, key point preference, simplicity preference, and latency preference.

### Strengths
1. This is an intriguing question and a useful framework for practical SiMT scenarios. While SiMT has been extensively studied in the research community, most papers have focused on automatic metrics rather than real human preferences. This work proposed 5 human preferences that are closely related to the end-users of SiMT.

2. The proposed optimization objective aligns well with the proposed human preferences. For example, the output length constraint is applied for latency preference. The derived final objective in Eq(9) is further to improve its read/write policy.

### Weaknesses
1. The data construction relies on GPT-4/4o. What is the cost of construction the training data? Does it mean GPT-4/4o is the upper bound of human preference alignment? Or this work is to GPT-4 preference alignment?  Figure 2 only shows the win-rate between GPT-4 translation and original one. Is there a comparison between GPT-4 and professional interpreter?

2. In the experiments, you only tune the hyper-parameter $\alpha$, and set $c_t$ as 0.5 to control the read/write. In general, tuning the thresholds of $c_t$ may introduce various read/write strategies. Did you try other threshold?

### Questions
1. Since real-time translation is a key requirement of SiMT, LLM-based SiMT may need to re-translate each partial source sentence, as the decoder-only architecture of LLMs does not permit the insertion of additional source tokens without disrupting the positional indexes of the already translated target tokens. I want the authors to justify this issue.

2. Continued on Weaknesses 1, given some GPT-4/4o translations, is that possible to ask the professional interpreter to select the high quality translation? Then a classifier or reward model can be implemented to filter out the translations align most with human.

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
The paper introduces Simultaneous Preference Learning (SimulPL) for the task of Simultaneous Machine Translation. The approach encompasses not only data construction but also model training and inference strategies. However, the novelty of the proposed method appears to be insufficient.

### Strengths
The paper presents a comprehensive approach to Simultaneous Machine Translation, addressing data construction, model training, and inference.

### Weaknesses
1. The paper lacks a clear emphasis on the innovative aspects of the proposed method. Highlighting specific novel contributions would strengthen the paper.

2. It remains unclear how the quality of the automatic labeling by GPT-4 is ensured, and the consistency rate with human labeling is not provided.

3. The distinction between the uppercase X and lowercase x in equations 6 and 7 needs clarification.

4. According to Figure 6, the improvement of SimulPL over only MSFT is not substantial, raising questions about the effectiveness of the proposed method.

### Questions
please see weaknesses

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies the problem of Simultaneous Machine Translation (SiMT). To achieve preference alignment for SiMT models, this paper categorizes human preferences in SiMT scenarios and focus on five aspects: translation quality preference, monotonicity preference, key point preference, simplicity preference, and latency preference. Based on this catogorization, this pape rconstructs human preference prompts with GPT to generate preference data for SiMT. After constructing the data, this paper designs a multi-task supervised fine-tuning stage and a simultaneous direct preference optimization stage to achieve preference alignment for the SiMT model. Experiments on text-to-text SiMT tasks show the effectiveness of the proposed approach.

### Strengths
1. The proposed approach shows performance improvement on the machine translation datasets.
2. The proposed five aspects for SiMT preference alignment could be useful.
3. The presentation is clear and easy to understand.

### Weaknesses
1. Heavy reliance on the quality of the GPT-generated preference data, and few effort is done to verify the quality/correctness/trustworthiness of the generated data.
2. Overall limited novelty for the whole framework, the idea of length penalty term |y| in the proposed SimulDPO loss function come from [1], and nothing much novel is added here.
3. Scope is very limited to SiMT only, and this method does not seem applicable to more general LLM preference alignment cases.
4. Some design is arbitrary. For example, in Confidence-Based Policy During Inference, why set the confidence c_t as exactly 0.5? What if your confidence estimation model is biased, e.g., $\mathbb{E}(c_t)\neq0.5$?
5. More experiments and analysis should be done to conduct a comprehensive evaluation. In the current form, experiment analysis are limited.

### Questions
Why most experiments are done between translation of Zh and En? Should possibly incorporate more languages to demonstrate the effectiveness of the approach.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces a new approach to simultaneous interpretation with low latency.

### Strengths
The experimental results look impressive.

I think there will also be interest in the experimental materials.  Your arguments about offline machine
translation (OMT)  are convincing.  That said, I didn't see any discussion of sharing those materials.

I like the idea of offering the user choices over preferences, but do we need to restrict ourselves to a single choice?  Could you imagine a speech-to-text scenario where you could offer multiple text windows so the user can look at one window when latency is a priority and another window when BLEU is a priority?

### Weaknesses
I have never been that happy with the standard discussion of latency and BLEU scores in this literature.  I have quite a bit of experience with professional interpreters as well as automatic solutions.  According to a number of standard metrics, the automatic solutions are better than professional interpreters, but I know that I am more engaged in the meeting when I have access to an interpreter.  They tell me what I need to know when I need to know it.  In addition, sometimes the speaker uses a metaphor that requires more explanation.    The professionals understand when then need to do more than just translate what the speaker said.

I never liked average latency.  I can't fault you for doing what others have done, but sometimes latency matters and sometimes it doesn't.  The professionals understand this.  They speed up when necessary and slow down when latency is less of a priority.  Moreover, I probably care more about worst case latency or RMS latency than average latency.

This literature would benefit by including more input from professional interpreters that have a lot more experience in this area than we have.

I would really like to see some data from schools that teach professional interpreters. We should be able to record what students say in the booth when they learn how to do this task.

### Questions
Do you have any plans to share your benchmark?

Do you have a github that will make it easy for others to replicate your work?

### Soundness
4

### Presentation
4

### Contribution
3
