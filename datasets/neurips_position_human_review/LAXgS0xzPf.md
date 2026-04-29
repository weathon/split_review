# From Bitter to Better Lessons in AI: Embracing Human Expertise as Data

- Decision: Reject
- Scores: 4, 7, 5

## Abstract
Artificial intelligence (AI) and machine learning (ML) have long treated data as clean numeric features and labels, with progress driven by ever‐larger models and datasets, a view that is crystallized in Sutton’s “Bitter Lesson”. In this paper, we contend that human expertise, often encoded in natural language, mathematical formalisms, and software, should itself be regarded as a vital form of data. First, we survey physics-informed ML, geometric deep learning, and safe reinforcement learning to show how embedding expert knowledge narrows hypothesis spaces, reduces sample and computational complexity, and improves out-of-distribution generalization. Next, we trace the expanding scope of data in ML, demonstrating how integrating text, images, actions, and other data modalities can transform previously transductive learners into increasingly inductive ones. We then highlight large language models (LLMs) as the nexus of these trends, illustrating how reinforcement learning with human feedback and in-context learning let LLMs integrate human expertise as data for general-purpose computation. To measure current practice, we analyze 1,000 NeurIPS papers between 2020–2024, finding that explicit domain-expert integration remains low with 12–18%, while LLM-based methods for expert incorporation are surging from 1% in 2022 to 8\% in 2024. We revisit the Bitter Lesson amid slowing Moore’s Law and real-world, non-i.i.d. data challenges, survey alternative perspectives, and propose new directions for dataset documentation, model design, and curated knowledge repositories. By recognizing human domain expertise and insights about tasks as first-class data, we envision a foundation for the development of more efficient and powerful AI.

## Human Reviews

## Human Reviewer 1

### Rating
4

### Rating Number
4

### Confidence
3

### Summary
This paper challenges Sutton's "Bitter Lesson" by arguing that human expertise should be treated as "first-class data" in AI systems. The authors claim domain knowledge integration reduces computational requirements through physics-informed ML, geometric deep learning, and safe RL examples. They position LLMs as enabling expertise integration via RLHF and in-context learning. A survey of 1,000 NeurIPS papers shows low explicit domain integration (12-18%) but rising LLM adoption (1% to 8%). The paper concludes by advocating new data documentation standards.

### Strengths
1. Addresses a timely and relevant debate about scaling versus domain knowledge in current AI development
2. Provides comprehensive coverage across multiple ML subfields with concrete examples like nanophotonic device optimization
3. Offers quantitative analysis of NeurIPS trends, providing useful empirical data despite limitations

### Weaknesses
1. The terms “human expertise,” “domain knowledge,” and “contextual information,” are used interchangeably without clear definitions. This lack of precision weakens the argument, making it difficult to define what the authors mean by "expertise as data."
2. The NeurIPS analysis appears to rely on ChatGPT for paper classification, with limited detail on manual validation or inter-rater checks. Statistical measures like confidence intervals or significance testing are also not reported.
3. The paper highlights successful cases of domain knowledge integration, but does not discuss instances where such approaches may have been less effective or impractical. Without examples of failure or limitations, assessing the broader applicability or opportunity costs of integrating expert knowledge becomes challenging.
4. In Section 2, the authors argue that integrating domain knowledge “narrows the hypothesis space” and improves efficiency. However, they do not discuss potential downsides of this narrowing — such as excluding hypotheses that contradict current expert understanding. This is especially relevant in fields where innovation has historically come from outside dominant frameworks.

### Questions
1. Who determines what constitutes valid "expertise" and how do we validate expert claims when experts disagree?
2. How do we prevent historical biases in expert knowledge from becoming architectural features?
3. What happens to AI democratization if model building requires deep domain expertise?

### Presentation
2

---

## Human Reviewer 2

### Rating
7

### Rating Number
7

### Confidence
4

### Summary
This paper argues that human expertise should be regarded as an important form of data in machine learning. Integrating such expertise can reduce the hypothesis space, decrease the amount of training data required, and improve out-of-distribution generalization capabilities. The authors demonstrate this point by reviewing multiple subfield cases, showing that incorporating domain insights can enhance efficiency and performance. LLMs are seen as a typical example of leveraging human knowledge as data—through human feedback and prompts, LLMs utilize information provided by humans to solve tasks. The authors also analyzed NeurIPS papers from 2020 to 2024 and found that approximately 15% of papers explicitly integrated domain knowledge, although this proportion is gradually increasing through LLM-based methods. They contrast this with Rich Sutton's “bitter lesson” and point out that with the slowdown in hardware progress, now is the time to leverage human insights as data. Finally, the paper outlines specific steps to achieve this vision, such as improving dataset documentation and establishing curated knowledge repositories.

### Strengths
1. The paper's central argument (treating human expertise as data) is clearly articulated and consistently maintained throughout.
2. Timely topic: The paper addresses pressing challenges in the field of machine learning (e.g., how to improve generalization capabilities as data scales reach bottlenecks) and connects its arguments to current trends (such as the rise of large language models (LLMs)), making the discussion highly relevant.
3. This position is supported by evidence from multiple subfields and a quantitative analysis of 1,000 NeurIPS papers, adding credibility to the argument.
4. The authors acknowledge and address alternative viewpoints (particularly Sutton's “bitter lessons”), strengthening their argument by thoroughly considering counterarguments.
5. The paper goes beyond theoretical considerations to propose concrete recommendations (e.g., improving dataset documentation to include context, establishing curated knowledge bases, and designing models that incorporate expert opinions), making its ideas practically actionable.

### Weaknesses
1. The study primarily consists of opinions and reviews, lacking original experiments to directly prove its arguments. It relies on literature cases and reasoning, which may not satisfy readers expecting specific new evidence. 
2. The paper provides little detail on how to systematically collect and integrate expert insights, or how to mitigate biases in human knowledge. This practical gap leaves unclear whether this vision is feasible in the real world. 
3. The analysis of 1,000 NeurIPS papers is inadequately explained; the reliability of the reported statistics is questionable due to the lack of a clearly defined standard for “domain expert integration.”

### Questions
1. How did you analyze 1,000 NeurIPS papers? What criteria did you use to determine whether a paper “explicitly” incorporated domain expert knowledge, and how did you ensure that these criteria were applied consistently?
2. Human expert knowledge may sometimes be biased, incomplete, or erroneous. How do you suggest ensuring the quality and fairness of expert knowledge when using it as data? For example, have you considered verification steps or guidelines to prevent flawed or biased expert information from influencing the model?
3. Given that large models trained on internet text have already implicitly absorbed a significant amount of human knowledge, what are the primary advantages of explicitly integrating curated expert knowledge? In which specific scenarios would a model enhanced with explicit expert input significantly outperform one relying solely on broad, uncurated data?

### Presentation
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper challenges the traditional view in artificial intelligence (AI) and machine learning (ML) that treats data solely as clean, numerical features and labels. It argues that human expertise, encoded in natural language, mathematics, and software, should also be considered a vital form of data. The authors demonstrate that embedding expert knowledge into ML can reduce computational complexity, improve generalization, and make models more efficient. They explore how large language models (LLMs) can integrate human domain expertise, presenting examples like reinforcement learning with human feedback and in-context learning. The paper also examines recent trends in AI, highlighting the increasing role of LLMs in solving problems. The authors advocate for a shift in AI practices to incorporate human expertise as data, improving AI's problem-solving efficiency and expanding its potential.

### Strengths
- effectively presents a compelling argument for integrating human expertise as data in AI and ML, challenging the prevailing view that data should only be numerical. 

- Clearly articulate how incorporating expert knowledge can reduce computational demands and improve generalization in ML models. They support their position with relevant examples from areas like physics-informed ML, geometric deep learning, and reinforcement learning with human feedback, showing how these approaches enhance efficiency and effectiveness. 

- The use of large language models (LLMs) as a method to incorporate human expertise is well-documented and demonstrates their increasing importance in AI research.

### Weaknesses
- While the paper provides a strong case for integrating human expertise as data, it could benefit from a deeper exploration of potential challenges or limitations in this approach. For instance, the feasibility of consistently encoding human expertise across diverse domains may require significant efforts in standardization and validation, which the paper does not fully address.

- Alternative positions, such as emphasizing hybrid models that combine computational power with selective expert input or exploring the potential of unsupervised learning and active learning to reduce reliance on human expertise, are not fully explored. 

- Furthermore, the paper could engage more with critiques from those who argue that increased computational power and data-driven approaches, even without human expertise, will eventually outperform expert-driven methods in many domains.

### Questions
see Weaknesses

### Presentation
3
