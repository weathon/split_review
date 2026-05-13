# EOP: Unlocking Superior Problem Solving in Small LLMs

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Small language models, referred to as LLMs with fewer than 10 billion parameters in this work, face critical challenges in problem-solving
tasks, often achieving less than 10\% accuracy, highlighting the
urgent need for effective solutions. While much of the existing research has focused on enhancing the performance of larger models like GPT, an important question remains: Can techniques developed for large models be adapted effectively for smaller ones? Moreover, is it possible to improve these smaller models to the point where they rival, or even outperform, larger models such as GPT-4 in problem-solving tasks?

In this paper, we introduce Evaluation-Oriented Problem-Solving (EOP), a novel framework aimed at enhancing the problem-solving capabilities of small LLMs. Our approach significantly boosts the performance of these models, achieving a 2\% higher accuracy on Python Puzzles compared to standard GPT-4 and a 27\% improvement over state-of-the-art prompting methods using GPT-4 in the Game of 24. Beyond these results, EOP also demonstrates notable accuracy improvements on other tasks. These findings suggest that, with the appropriate strategies, small LLMs can achieve substantial performance gains in problem-solving, challenging the prevailing notion that scaling model size is the primary path to improvement.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper investigates whether Evaluation-Oriented Problem-Solving can enhance the problem-solving capabilities of small LLMs. By comparing the performance of large and small LLMs using CoT, GoT and MP methods, the study concludes that small LLMs perform worse than large models in several types of problem-solving tasks. Therefore, innovative methods are needed to address this performance gap in small models. The paper demonstrates through experiments that the EOP approach improves the problem-solving performance of small LLMs.

### Strengths
1. The writing is clear and easy to understand.
2. In the proposed framework, the paper uses multiple trials (breadth-first) instead of multiple rounds (depth-first) and incorporates a reasoning evaluator, effectively enhancing the reasoning and synthesis capabilities of small models.

### Weaknesses
1. Evaluation-oriented approaches in LLMs are more and more studied in many learning tasks. This paper seems the first one that studies evaluation-oriented approach for problem solving. They aim to propose a small LLMs specific approach. How does EOP perform for large models? The paper does not conduct experiments for it. 
2. The authors point out that the paper includes four main contributions: understanding failure modes, emphasizing the role of evaluators, introducing a novel evaluation-based prompting method, and addressing varying levels of evaluator expertise. It seems that the first three contributions are consensus in today’s study. The novelty of the contributions is limited.

### Questions
1. The evaluation-oriented approach is anticipated to positively influence reasoning tasks for large models, as supported by empirical evidence from similar studies. The paper validates the effectiveness of the EOP approach for small LLMs, which aligns with intuitive expectations. The novelty of this work is unclear.
2. If the paper intends to focus on an evaluation-oriented approach specifically for problem-solving, I expect an analysis of the characteristics of problem-solving tasks and how these can be addressed within the EOP framework. This would help clarify the novelty and contributions of the paper.

### Soundness
2

### Presentation
4

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes a method to improve problem solving for small LLMs,
leveraging repeated prompting. The authors describe their method and evaluate it
empirically, comparing to large commercial LLMs.

### Strengths
The paper tackles an interesting and timely problem. LLMs are very powerful, but
have prohibitive resource requirements. This restricts who can benefit from
them, and research to make them more accessible is very important.

### Weaknesses
The proposed method seems to work well in practice, but it is unclear how
general it is. The authors state that "with a reliable evaluator, small models
can achieve superior accuracy" but also that "the evaluation accuracy is limited
by the inherent weaknesses of small LLMs". The empirical results are also
somewhat mixed; in some cases the proposed methodology results in only small
changes. It is unclear why this happens and under what circumstances the
proposed methodology is likely to produce substantially better results. This is
an important question that the paper does not consider.

Further, the problems considered in the paper are relatively easy -- how does
the proposed approach fare on difficult tasks, in particular ones that users are
likely interested in? In particular, are small LLMs capable of evaluating the
solutions for more difficult tasks with reasonable accuracy? If they are not, it
seems that the proposed approach would not work at all anymore, limiting its
applicability.

### Questions
How would the approach fare with more difficult problems?

Update after responses: Thank you for your responses.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper studies challenges faced by small LLMs (fewer than 10 billion parameters) in problem-solving tasks, where they often achieve less than 10% accuracy. The authors investigated whether advanced prompting techniques designed for larger models, such as meta-prompting, can enhance the performance of smaller models, but find limited success. Then they propose a new framework called Evaluation-Oriented Problem-Solving (EOP), which focuses on tailored evaluation techniques and multiple trials to improve accuracy. The study demonstrates that small LLMs can perform better when using an oracle evaluator to select correct answers from multiple attempts. The paper presents experimental results showing that EOP can significantly enhance the problem-solving capabilities of small LLMs across various tasks, outperforming existing methods and even some larger models in specific scenarios.

### Strengths
1. The scientific flow of this paper is great. I like the way the authors first identified the issue with experiments and then proposed their method to address it. The paper is also well written what methodology, and results clearly stated. The figures also help readers understand the idea a lot.

2. The experiment results are encouraging. EOP significantly improved the performance of small LLMs, achieving a 2% higher accuracy on Python Puzzles compared to GPT-4 and a 27% improvement over state-of-the-art methods in the Game of 24.

### Weaknesses
1. The problem studied in the paper is important in that the size of LLMs can be important in specific scenarios. However, the motivation is not well established in the paper. It would be nice to have a paragraph to educate the readers on why small LLMs are preferred over large LLMs and why the challenging faced by small LLMs are critical.

### Questions
Why is using small LLMs critical?

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
3

### Summary
This paper focuses on the application of Large Language Models (LLMs) with fewer than 10 billion parameters to problem-solving tasks. The existing small LLMs are usually unable to achieve high accuracy when dealing with problem-solving tasks, while lots of the existing researches usually focus on how to enhance the performance of large LLMs, ignoring the need for improving the accuracy of small LLMs. In this paper, the authors propose a novel framework, Evaluation-Oriented Problem-Solving (EOP), to enhance the ability of small LLMs to handle problem-solving tasks. With the help of the EOP framework, the performance of the existing small LLMs on the Python Puzzles and Game of 24 problems is further improved and is better than the standard GPT-4, indicating a new direction beyond the approach of increasing the capability of the LLMs by increasing the size of the model.

### Strengths
1. Instead of increasing the model size to improve the performance of LLMs, this paper designed an evaluation-based approach and implemented the Evaluation-Oriented Problem-Solving (EOP) framework for small LLMs. The research in this paper provides new guidance for improving the performance of LLMs.

2. The EOP framework designed by the author successfully improves the performance of small LLMs in problem-solving tasks such as Game of 24, Python Puzzles and Word Sorting. More encouragingly, it successfully outperforms the standard GPT-4 on Python Puzzles and Game of 24 tasks. The experimental results show that the reasoning evaluator plays an important role in improving the performance of small LLMs.

### Weaknesses
1. The motivation of this paper is a bit unclear. In practice, large language models ahcieve much better performance than small language models. Thus, what is the motivation for enhancing small language models? Why don't the authors further improve the performance of large language models?

2. The interpretation of the experimental results is too brief, so it is suggested that the author conduct a more detailed analysis of the experimental results.

3. The author mentioned in the paper that EOP mainly introduced two key changes -- the use of multiple trials (breadth-first) and the integration of a reasoning evaluator. In the ablation experiment part of Section 4.3, it seems that the ablation analysis of the improvement using multiple trials is not shown, and it is suggested to supplement the relevant part to make the experiment more complete.

4. There is a problem with the format of line 279. Appropriate adjustments are recommended.

### Questions
Please refer to all the comments listed in "Weaknesses".

### Soundness
2

### Presentation
3

### Contribution
2
