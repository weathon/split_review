# Bridging Visual Communication and Data Exploration through Pose-Driven Query Synthesis

- Decision: Reject
- Scores: 1, 1, 3

## Abstract
SQL is widely used for managing relational databases and conducting interactive data analysis. Now, various natural language interfaces have emerged, designed to simplify the process of crafting SQL queries by translating natural language commands into executable SQL-Code. However, the communication preferences of the deaf and hard-of-hearing community have been largely overlooked. 
This paper introduces R-KinetiQuery, a groundbreaking framework for domain-adaptive sign language to SQL query translation, underpinned by a rigorous mathematical foundation synthesizing functional analysis, ergodic theory, and information geometry. At its core, R-KinetiQuery addresses the fundamental challenge of domain adaptation in the context of multimodal language translation, specifically tailored to bridge the gap between sign language communication and database query languages. A key innovation lies in our application of ergodic theory to analyze the long-term behavior of R-KinetiQuery under domain shift. We establish an ergodic theorem for the model's time-averaged operator, demonstrating its convergence to the expected behavior across domains. This result provides a robust foundation for the model's stability and adaptability in non-stationary environments. Our information-theoretic analysis reveals a deep connection between R-KinetiQuery and the Information Bottleneck principle. We derive a variational bound that explicitly quantifies the trade-off between compression and prediction in the model's latent representation, providing insights into its domain-invariant feature learning.
Empirically, we demonstrate R-KinetiQuery's superior performance on a diverse set of domain adaptation tasks, consistently outperforming state-of-the-art baselines. Our experiments span a wide range of domain shifts, from subtle variations in sign language dialects to dramatic changes in database schemas and query complexities.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
This paper presents R-KinetiQuery, a novel framework that translates sign language into SQL queries, aiming to make database interaction accessible for the deaf and hard-of-hearing community. Experimental results show that R-KinetiQuery consistently outperforms existing methods across various domain adaptation tasks, including changes in sign language dialects and database schemas.

### Strengths
N/A

### Weaknesses
**(W1)** The topic is generating SQL queries from sign language which is esoteric, to say the least, while being presented as an "emerging field". People who are speech impaired can still use a natural-language-to-SQL generation tool if they want, without complicating things with sign language.

**(W2)** The amount of superlatives used is indicative of typical LLM jargon (see abstract: "groundbreaking framework", "key innovation", "superior performance")

**(W3)** Strange section titles (e.g. "Contextual Landscape" as opposed to "Related Work", or "Comparative Assessment Framework" as opposed to "Empirical Evaluation")

**(W4)** The introduction has no citations.

**(W5)** The content seems like a mishmash of math jargon combined together in a way that makes little sense. Also, the introduction talks a lot about some problems like domain adaptation for which it's unclear why this is important for the problem at hand.

### Questions
N/A

### Soundness
1

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
1

### Rating Number
1

### Confidence
4

### Summary
The paper provides a model to derive SQL statements out of pose language, which adds an image processing step to the traditional text-to-SQL model.

### Strengths
The problem is difficult, and of interest to the conference.

### Weaknesses
- Most of the paper deals with theoretical results that comes from definitions that are general for almost any ML architecture (definitions 1-6). Hence, the resulting theoretical analysis is mostly re-casting known results. 
- Further, there is no connection between theory and the proposed model in this paper. How does your results affect your model choice? 
- the model itself relies on rather outdated technology, using an LSTM to get image vector embeddings and then a text-to-SQL architecture from 2017.

### Questions
What is the connection between your theoretical results and the problem? I feel I could produce section 3 for almost any paper looking to introduce a machine learning model.

### Soundness
3

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The paper studies the problem of sign language to SQL query translation. The authors introduce R-KietiQuery, which applies ergodic theory to the long-term behavior analysis. The paper provides a mathematical results showing the domain adaptation capabilities of DL models in cross-modal and cross-schema translation.

### Strengths
S1. The paper introduces a theoretical foundation to sign language to SQL query translation.

### Weaknesses
W1. The motivation is not convincing. I agree that the communication preference of deaf and hard-of-hearing community has been overlooked in the context of SQL generation. However, I do not understand why someone from such community needs to use a sign language rather than text to input natural language/SQL queries. Hence it is not clear me to whether the studied problem has any applicability in real-world scenarios.

W2. The related work is weak, especially on NL-to-SQL generation/translation. The LLM-based approaches emerged in recent years are not reviewed nor discussed. This is critical as LLMs can handle the cross-modal issue nicely.

W3. The challenges in the sign language to SQL generation are not clearly articulated. And the proposed method lacks of justification. It is not clear why a two-step approach would not work. Specifically, the question in a sign language can be translated into a natural language question, and consequently being translated into a SQL query. The unified theoretical framework does not benefit the sign language to SQL generation.

W4. The experimental evaluation is not solid. First, the authors mentioned that a new benchmark dataset for sign language to SQL
translation is introduced, but I do not find the URL to the new dataset. Worse yet, the detail of this benchmark dataset is missing, making it difficult to assess the experimental results. Second, the chosen baselines in the experiment are outdated. Most recent LLM-based solutions should have been included.

### Questions
Q1. Can you describe a real-life scenario where the proposed framework can be used?

Q2. Can you justify the advantages of the proposed framework compared to the two-step approach?

Q3. Can you provide additional details regarding the experimental setup and provide more data points to validate the effectiveness of the proposed method?

### Soundness
2

### Presentation
2

### Contribution
2
