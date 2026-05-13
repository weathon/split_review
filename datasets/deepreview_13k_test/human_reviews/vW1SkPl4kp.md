# Provably Efficient Iterated CVaR Reinforcement Learning with Function Approximation and Human Feedback

- Decision: Accept
- Scores: 3, 8, 6

## Abstract
Risk-sensitive reinforcement learning (RL) aims to optimize policies that balance the expected reward and risk. In this paper, we present a novel risk-sensitive RL framework that employs an Iterated Conditional Value-at-Risk (CVaR) objective under both linear and general function approximations, enriched by human feedback. These new formulations provide a principled way to guarantee safety in each decision making step throughout the control process. Moreover, integrating human feedback into risk-sensitive RL framework bridges the gap between algorithmic decision-making and human participation, allowing us to also guarantee safety for human-in-the-loop systems. We propose provably sample-efficient algorithms for this Iterated CVaR RL and provide rigorous theoretical analysis. Furthermore, we establish a matching lower bound to corroborate the optimality of our algorithms in a linear context.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work focuses on risk-sensitive reinforcement learning for large state space. It propses three variants of Iterated Conditional Value-at-Risk (CVaR) algorithms for linear function approximation, general function approximation, and with human feedback respectively. Moreover, it provides theoretical analysis on the regret bound for each of the algorithms.

### Strengths
To the best of my knowledge, this paper is distinctive in its provision of the first theoretical analysis on regret bounds for ICVaR-RL algorithms in non-tabular settings. It sets a precedent which could lead to significant advancements in this field. Additionally, the introduction of human feedback into risk-sensitive RL opens a potentially fruitful avenue for future research.

### Weaknesses
1. The presentation can be further enhanced in terms of clarity and logic:

   - In the first paragraph on page 2, the paper introduces two proposed algorithms but fails to sufficiently detail how these tools embody and implement the ICVaR concept. This lack of substance makes the uniqueness and contribution of your algorithms unclear.

   - The main argument presented in the second paragraph on page 2 is confusing. It's unclear whether the intention is to highlight the importance of integrating human feedback, with LLM as a successful example of this, or to underline the significance of risk-sensitive RL, with ChatGPT as an example. Additionally, why is " LLMs operate in diverse conversational landscapes, where defining reward signals unequivocally is challenging" relevant here?

   - The third paragraph on page 2 attempts to give an outline of the key challenges in theoretical analysis for ICVaR algorithms with function approximation and human feedback. However, critical concepts and symbols which outline these challenges are not adequately defined or explained, which hinders the comprehension of arguments. For instance, without further context or clarification, the term "key elliptical potential lemma" remains obscure to readers. Moreover, the majority of the "challenges" outlined are essentially highlighting that current proof techniques and results cannot be seamlessly applied to your problem setting. However, there's a lack of explanation rooted in the problem's inherent characteristics.

2. Limited discussion on the intuition and implications of their theoretical bounds, making it difficult to understand the relevance and significance of these results.

3. Absence of algorithm implementation or experimental results limits the understanding of the theoretical results' real world impact and applicability. Practical validation through experimentation is essential to underline the significance and verify the efficiency of the proposed algorithms, which has been neglected in this paper.

### Questions
See the weaknesses section.

### Soundness
3 good

### Presentation
1 poor

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the risk-sensitive RL under an Iterated Conditional Value-at-Risk (CVaR) objective. Both linear and general function approximations are discussed in this work. Several algorithms are proposed to address such problems with the provable complexity analysis. A novel efficient approximation of the CVaR operator and a new ridge regression
with CVaR-adapted regression features are also provided. Besides, human feedback is integrated into this framework.

### Strengths
This paper is easy to follow, and the technique novelty is clear. To address the risk-sensitive RL under an Iterated Conditional Value-at-Risk (CVaR) objective, the authors propose two sample
efficient algorithms with sample complexity analysis, ICVaR-L and ICVaR-G, for two different function approximations correspondingly. Also, the upper regret bounds of algorithms are provided. Besides, the authors consider the risk-sensitive RL in the human feedback setting.

### Weaknesses
While I typically do not complain about the empirical results of this paper, I do expect that some implemented results on real-world practical problems could be contained in this paper.

### Questions
no comment.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper studies the iterated CVaR objective RL under both linear and general function approximations. Additionally, the authors have incorporated human feedback into the framework. The paper offers theoretical guarantees for all the proposed algorithms in various settings.

### Strengths
This paper is well-written and well-organized. It effectively conveys the high-level intuition behind the algorithm. The paper provides a comprehensive discussion of the theoretical results for iterated CVaR RL in various settings, including linear function approximation, general function approximation, and the incorporation of human feedback. Notably, the paper introduces a novel approximation operator for the true CVaR operator in the linear approximation setting, which could be of independent interest.

### Weaknesses
The technical aspects of the algorithms appear somewhat limited and are relatively standard in the literature. Additionally, the algorithms are not efficient, and obtaining a solution for the approximate CVaR operator is not easy.

### Questions
Some typos:

On page 2, in the first bullet, $\sqrt{\alpha^{-H}}$ → $\sqrt{\alpha^{-2}}$

On page 8, it should be $\sigma(x)$ in regularity.

What is $\tilde{\sigma}$ in equation (14)?

Compared with the tabular setting, why the linear case has a bad dependence on H?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
