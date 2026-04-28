# Evaluating Large Language Models through Role-Guide and Self-Reflection: A Comparative Study

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
Large Language Models fine-tuned with Reinforcement Learning from Human Feedback (RLHF-LLMs) can over-rely on aligned preferences without truly gaining the self-knowledge, leading to hallucination and biases. If an LLM can better access its knowledge and know what it knows, it can avoid making false or unsupported claims. Therefore, it is crucial to evaluate whether LLMs have the ability to know what they know, which can help to ensure accuracy and faithfulness in real-world applications. Inspired by research in Educational Psychology, students who don't really know are easily affected by teacher and peer guidance, we treat LLM as a student, incorporate role guidance in prompts to explore whether LLMs really know. Specifically, we propose a novel strategy called **Ro**le-Guide and **Se**lf-Reflection (**RoSe**) to fully assess whether LLM ``knows it knows''. We introduce multiple combinations of different roles and strong reminder in prompts combined with self-reflection to explore what local information LLMs rely on, and whether LLMs remain unaffected by external guidance with varying roles. Our findings reveal that LLMs are very sensitive to the strong reminder information. Role guidance can help LLMs reduce their reliance on strong reminder. Meanwhile, LLMs tend to trust the role of authority more when guided by different roles. Following these findings, we propose a double-calibrated strategy with verbalized confidence to extract well-calibrated data from closed-source LLM and fine-tune open-source LLMs. Extensive experiments conducted on fine-tuning open-source LLMs demonstrate the effectiveness of double-calibrated strategy in mitigating the reliance of LLMs on local information. For a thorough comparison, we not only employ public JEC-QA and openBookQA datasets, but also construct **EG-QA** which contains **E**nglish **G**rammar multiple-choice question-answering and 14 key knowledge points for assessing self-knowledge and logical reasoning.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies and evaluates whether large language models (LLMs) are confident in their acquired knowledge. It claims that LLMs fine-tuned with RLHF could potentially over-rely on aligned preferences, instead of truly gaining the knowledge, and that if LLMs are more confident in the knowledge. To qualitatively assess whether LLMs have a sense of whether it has any knowledge, a Role-Guided and Self-Reflection (RoSe) method is proposed. Specifically, it combines prompting and self-reflection to examine the sensitivity of LLMs to parametric knowledge and contextual knowledge. In the paper, several findings are elaborated. For example, empirical results reveal the LLMs are sensitive to the prompt. By assuming roles, LLMs are prone to be less dependent on the contextual knowledge. Based on the findings, the authors further propose a calibration-based method to extract high-quality SFT data. Fine-tuning on the SFT data improves the overall confidence when LLMs generate outputs.

### Strengths
- The motivation is convincing. Previous studies have revealed that deep learning models suffer from confidence calibration. To assess the confidence level of LLMs is an important topic and would benefit a wide spectrum of the NLP community.
- The experimental results are quite interesting and the findings are refreshing.

### Weaknesses
 - Some details seem not clear to me. For example, what is exactly the _verbalized confidence_?
- It seems that the fine-tune portion of the experiments are all conducted on the EG-QA dataset, which is proposed in this submission as well. Whether the dataset suffer from data contamination needs serious examination.
- The proposed method mainly considered three factors to examine the confidence of LLM outputs (role, cue, etc.) There could be various other factors that have impact on the confidence (pre-trainining data, SFT data, preference data). Massive amount of studies on these factors might be needed to compose a "comprehensive" study.
- I think Section 4.2 could use some improvement. After reading it, it is still unclear to me how to conduce the so-called "double-calibration". I suggest the authors use some examples or diagrams to further illustrate.

### Questions
- What is exactly the _verbalized confidence_?
- How is the _double calibration_ achieved?
- How are the new datasets curated? How to make sure they are of high quality?
- What is step-3 in the experiment section?

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
This paper proposes RoSe, a strategy that uses role guidance and self-reflection in prompts to evaluate whether LLMs know what it knows. They use a double calibrated strategy to find well-calibrated data to be used for fine-tuning LLMs. They study four research questions and found some interesting observations. For example, LLMs are highly sensitive to strong reminder information in prompts, such as "the answer is". In addition, role guidance can reduce the issue of overconfidence of LLMs.

### Strengths
- The idea of using roles like "teacher", "student" and "classmate" is interesting.
- The authors provide a lot of details for reproducing the experiments, such as prompts for each step and experiment results under different settings.
- The findings of the paper are quite interesting but not surprising. For example, LLMs may be confused by wrong guidance, tend to capture information from shortcuts, and their overconfidence can be mitigated by role guidance.

### Weaknesses
 - The writing of the paper is a bit unclear. The paper did not mention explicitly in the main method section about what are "role-guided", "self-reflection", and they only use a figure in the introduction to show what the prompt looks like.
- The author did not explain what is "conf" in Table 2 and Table 3. This is not a typical metric and the authors should explain why it is important.

### Questions
- Could you explicitly explain the "Role", "Rem", "Cue", "conf", "com" appearing in the experiment result table?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper focuses on testing and boosting the model’s self-knowledge. its ability to tell the difference between what it truly understands and what it’s guessing from training data, rather than just following prompts or role guidance. 
They’re using different authoritative roles, like teacher or judge, to see how the model responds in each role, but the goal isn’t to pick one set role for guiding it permanently.

So, the aim is to check if the model falls for misleading cues, especially when it doesn’t actually know something. By introducing these authoritative roles, the researchers can see if the model just goes along with what it’s told. 
This lets them understand how the model behaves in different scenarios and figure out the kinds of guidance that might encourage more independent thinking.

### Strengths
- The authors implement role guidance by assigning roles, like "teacher" or "judge," to help the model think in ways that better align with real-world reasoning patterns.
- Adding a self-reflection step enables the model to review its responses, which enhances accuracy and reliability while exploring its self-knowledge.
- The paper’s double-calibration strategy combines role guidance with self-reflection, adjusting prompts and roles in iterative steps to reduce susceptibility to misleading information and improve answer stability.
- This approach also offers finer control during fine-tuning, helping the model handle uncertain information without relying solely on intuition or single-step decisions.
- The authors emphasize model self-knowledge, designing experiments to observe its confidence levels under different conditions. This focus helps develop models that are both accurate and capable of self-assessment, supporting more robust, real-world applications.

### Weaknesses
 - This work mostly used random answers to mislead the model, but they didn’t explain in detail how these answers were generated to ensure they’re diverse and realistic. If the random answers are too simple or repetitive, they may not truly test how well the model can handle more challenging misleading cues. Specifically, the lack of detail on the generation process makes it difficult to assess whether the negative examples are sufficiently varied to challenge the model's understanding, potentially leading to an overestimation of its robustness.
- The misleading information in the tests was mostly straightforward or basic incorrect answers. But in real-world scenarios, misleading information is often subtler or harder to detect. This setup might not fully capture the challenges the model would face in real-life situations. The use of simple, direct contradictions may not adequately simulate the nuanced and often ambiguous nature of real-world misinformation, which could involve misleading context, subtle implications, or a combination of partially correct information.
- The model’s self-knowledge is mainly judged by its confidence levels and accuracy. These indicators alone might not be enough to fully capture how well the model truly understands its answers. Relying solely on these metrics may overlook the model's internal reasoning process and its ability to identify the limits of its knowledge. A more comprehensive evaluation should include an analysis of the model's reasoning steps and its capacity to recognize uncertainty.
- Roles like “judge” often require objectivity and caution, which might make the model more conservative in its responses. This cautious approach could limit the model’s effectiveness, especially in tasks that require flexible reasoning or hypothesis testing. The inherent conservatism induced by certain roles could hinder the model's ability to explore alternative solutions or generate innovative ideas, potentially limiting its applicability in tasks that require creative problem-solving.

### Questions
- Are the randomly generated answers diverse and realistic enough to really test the model’s ability to handle complex misleading situations?
- Can the misleading info in the experiment truly reflect the subtle or hidden misdirections found in real-world scenarios to fully test the model's response? 
- By relying just on confidence levels and accuracy to measure the model's self-awareness, are we capturing the full depth of its understanding? 
- And could roles like a "judge" make the model more conservative, possibly affecting its performance on tasks that need flexible reasoning or hypothesis testing?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed RoSe, which is a set of strategies for assessing whether LLMs truly know the world knowledge, and how their confidence in their prediction could be affected when their answers are challenged by different roles. The authors also propose a double-calibrated strategy to fine-tune open-source LLMs so that they are more robust to local misleading information.

### Strengths
The studied question may be of great importance for the community to know the essence of LLMs and to develop better models. It is interesting to find how different types of guidance/challenges could affect the LLM results. The authors have made some effort to support their claim with experimental evidence.

### Weaknesses
- Many existing research articles studied the question of "whether LLMs truly know what they know". Although this article attends to more specific aspects of when and how LLM could fail, the demonstrated results are intuitive and may not deserve the discussion using a 10-page conference paper.

- The narration and illustration could use some improvement. For example, Figure 2 is not so informative in presenting the RoSe strategy or how the dataset for calibrated fine-tuning is constructed. There are significant redundancies within the first and second paragraphs in Section 4.2. The concept of "well-calibrated data" is not well-introduced and should be discussed in detail as it plays a key role in the fine-tuning process, etc.

- Some choices are not fully explained. For example, why the authors choose to do the main evaluation on the self-developed EG-QA dataset rather than other open-source datasets such as BBH, which also provides CoT chains in their answers.

- The reproducibility might be an issue. The proposed dataset EG-QA is not shared, the GPT versions are not specified, the fine-tuning objective is not sufficiently elaborated, etc.

- The narration in Lines 180--182 is confusing. What does it mean by we can obtain *, satisfying * based on logical consistency? Why the terms p and q are removed from $p(a,c|r)$? Does it mean the answer and confidence are generated only based on the reasoning chain, without seeing the original prompts?

- The results tables (2,3,4,5) show poor model calibration.

- How was the verbal confidence level such as "very confident" converted to scores?

- This paper is based on the assumption "students who don’t really know are easily affected by the teacher and peer guidance". Is there any evidence proving that this also holds for LLMs? This paper shows that LLMs are affected to different degrees by different types of guidance, but it does not directly build the link between "not really know" and "easily affected".

### Questions
Edit 11/21: fix typos in the original comments.

- The narration in Lines 180--182 is confusing. What does it mean by we can obtain *, satisfying * based on logical consistency? Why the terms p and q are removed from $p(a,c|r)$? Does it mean the answer and confidence are generated only based on the reasoning chain, without seeing the original prompts?

- The results tables (2,3,4,5) show poor model calibration. 

- How was the verbal confidence level such as "very confident" converted to scores?

- This paper is based on the assumption "students who don’t really know are easily affected by the teacher and peer guidance". Is there any evidence proving that this also holds for LLMs? This paper shows that LLMs are affected to different degrees by different types of guidance, but it does not directly build the link between "not really know" and "easily affected".

### Soundness
2

### Presentation
2

### Contribution
2
