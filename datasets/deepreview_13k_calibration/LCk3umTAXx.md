# Gamified crowd-sourcing of high-quality data for visual fine-tuning

- Decision: Reject
- Avg Score: 5.75
- Scores: 6, 6, 5, 6

## Abstract
This paper introduces {gamified adversarial prompting (GAP)}, 
a framework that crowd-sources high-quality data for visual instruction tuning of large multimodal models.
GAP transforms the data collection process into an engaging game, 
incentivizing players to provide fine-grained, challenging questions and answers that target gaps in the model's knowledge. 
Our contributions include 
(1) an approach to capture question-answer pairs from humans that directly address weaknesses in a model's knowledge,
(2) a method for evaluating and rewarding players that successfully incentivizes them to provide high-quality submissions,
and (3) a scalable, gamified platform that succeeds in collecting this data from over 50,000 participants in just a few weeks.
Our implementation of GAP has significantly improved the accuracy of a small multimodal model, namely MiniCPM-Llama3-V-2.5-8B, 
increasing its GPT score from 0.147 to 0.477 on our dataset, 
approaching the benchmark set by the much larger GPT-4V. 
Moreover, we demonstrate that the data generated using MiniCPM-Llama3-V-2.5-8B also enhances its performance across other benchmarks, and exhibits cross-model benefits. 
Specifically, the same data improves the performance of QWEN2-VL-2B and QWEN2-VL-7B
on the same multiple benchmarks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces the Gamified Adversarial Prompting (GAP) framework, aimed at enhancing the performance of multimodal AI models in visual question answering (VQA) tasks. By attracting over 50,000 participants on the Telegram platform, the author utilized the MiniCPM-Llama3 model for experiments and designed the GAP-VQA dataset to address knowledge gaps. Results indicate that, after targeted fine-tuning, the model's performance significantly improved across various benchmarks. The GAP framework emphasizes the importance of human involvement, mitigating biases associated with AI self-assessment, and promotes a more transparent and ethical approach to AI development, underscoring the critical role of human creativity in multimodal model improvement.

### Strengths
1. The paper presents an innovative Gamified Adversarial Prompting (GAP) framework that effectively integrates human involvement with multimodal learning strategies, significantly enhancing the performance of multimodal AI models in visual question answering and paving a new research direction.
2. The GAP framework underscores the vital role of human cognition and diverse perspectives in the model enhancement process, effectively mitigating biases and errors commonly associated with traditional self-assessment methods
3. The empirical results presented demonstrate substantial performance gains, particularly through targeted fine-tuning of the MiniCPM-Llama3 model, validating the effectiveness of the GAP-VQA dataset in addressing specific knowledge deficits
4. The adaptability of the GAP-VQA approach is noteworthy, as it not only improves the MiniCPM model but also shows robust transfer learning capabilities across different model architectures, indicating its broad applicability in the field of visual question answering.

### Weaknesses
1. Although the GAP-VQA dataset has been filtered to ensure a high proportion of adversarial examples, the diversity and representativeness of its samples still require further validation. The selected 3,683 question-image pairs may not adequately cover the diverse scenarios encountered in real-world applications. A lack of diversity could lead to suboptimal model performance on unseen tasks or images.
2. The evaluation of the model primarily relies on GPT-4 as the evaluator. While it can provide a degree of accuracy assessment, this reliance may have limitations. The evaluation criteria and preferences of GPT-4 might not be applicable to all types of visual questions. Additionally, the scoring range (0 to 1) in a single dimension may not fully capture the model's performance in complex reasoning or multimodal understanding, potentially affecting the objectivity and consistency of the evaluation.

### Questions
1. Rationality of Assumptions: The parameters ε and δ in Equations (1-4) are small positive numbers and the assumption that δ < ε is always valid. Is this relationship consistently upheld across different experimental conditions? If the model's performance deviates from these assumptions in specific scenarios, how does this impact the reliability of the analytical process?

2. Effectiveness of the Reward Mechanism: How does the reward system ensure that player behavior consistently aligns with expectations? If players deliberately mark correct answers as incorrect for other motives (e.g., mischief), how are these situations handled? Does the system have mechanisms to detect and correct such inconsistencies?

3. Sustainability of the Data Collection Mechanism: How is the sustainability of this data collection mechanism ensured? As the research progresses and the model size increases, so does the demand for data. Have there been considerations for continuously incentivizing participant engagement through methods such as raffles or accumulating reward pools?

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
The main contribution of the paper is the introduction of an approach,  Gamified Adversarial Prompting (GAP). The idea is to devise an interactive app for users: the user will play a game tying to find a question that the AI answers incorrectly. With the GAP framework, high-quality data to enhance visual instruction tuning in large multimodal models can be collected. The paper contributes by introducing a dataset based on MSCOCO for building GAP, by proposing a  strategy for collecting VQA pairs from players and by introducing a gamified platform that was used to engage over 50K players. The paper shows that with the use of the data collected with GAP the performance of MiniCPM-Llama3-V2.5-8B can be improved. Other experiments include cross-dataset results showing that the use of GAP is beneficial to improve on other benchmarks and evaluation of different models.

### Strengths
- The paper is based on a very interesting idea, which is using gamification for collecting data for fine-tuning large multimodal-models.
- The experiments demonstrate that the proposed approach improves the performance of a model, i.e. MiniCPM-Llama3-V- 2.5-8B.
- The proposed system was used by several participants and a detailed analysis of users' participation is shown in the Appendix

### Weaknesses
 - The writing of the paper needs significant improvements. The description of the method is confusing with some details only discussed in the supplementary material (see  A.3 PLAYER INTERACTION MODEL). A lot of space is dedicated to related works while some additional details in the main text should have been also dedicated to describing the GAP and the final system. 
- The descriptions in L 337 about  intrinsic and extrinsic factors is very high level and details on how this is integrated in the model are lacking
- The supplementary material could hep to understand the proposed approach but it is poorly referred in the main text and not well organized. 
- The proposed approach is beneficial in the case of a single model MiniCPM-Llama3-V- 2.5-8B, while the other models the improvements are mild (Table 4). This leads to question the effectiveness of the proposed framework.
- The results in Table 5 are not convincing or at least require a longer discussion, outlining possible reasons for mild improvements or not even improvements.

### Questions
- Why MSCoco was chosen as dataset? The cardinality of the tainted dataset seems small. How the choice of this dataset influences the performances in Table 5?
- Why the analysis in Table 5 focuses on the chosen methods?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper introduces Gamified Adversarial Prompting (GAP), a framework aimed at crowdsourcing high-quality data for the visual instruction tuning of large multimodal models. By gamifying the data collection process, GAP motivates participants to create challenging questions and answers that address the knowledge gaps of these models. The paper also includes an approach to automatically evaluate and reward player submissions with high accuracy, enabling to scale to 50000 players in a few weeks.

### Strengths
1. By gamifying the process, GAP keeps players motivated and engaged, potentially leading to high-quality data collection.
2. By automatically evaluating and rewarding player submissions, this approach can effectively scale up the data.
3. The framework has demonstrated significant improvements in model accuracy on VQA benchmarks, indicating its effectiveness.

### Weaknesses
1. The number of baseline models used in the experiment is not enough, and the numerical results presented in Table 5 do not show significant changes.
2. Quality Control: While the framework aims for high-quality data, there may still be variability in the accuracy of player-generated content. The evaluation process should include more rigorous checks for both factual correctness and the diversity of the questions.
3. Unable to determine the specific classification of the questions asked by the player, making it difficult to balance the number of different types of questions. This lack of categorization limits the ability to ensure comprehensive coverage of the model's potential weaknesses.

### Questions
1. Will a large amount of this type of data be created in the future to be integrated into LLM training?
2. Is it possible to have a stronger LLM replace the player's role and a weaker LLM handle the data creation process?

### Soundness
3

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
The paper introduces a framework for crowd-sourcing high-quality data for visual fine-tuning. The authors propose a chat-like interface that lets users interact with large multimodal models. While models must answer users's questions, the users must discover weaknesses in the model performance by posing diversified queries to the model. The authors transformed the evaluation procedure in a game to both evaluate and discover weaknesses of such models while also collecting supervised data to overcome the discovered limitations. With the collected data, the authors demonstrated the capability to tune and improve model performance.

### Strengths
- The authors introduce a platform to collect high-quality data and propose to use a game-like experience to engage the users and incentivize the discovery of weaknesses and collection of high-quality data for model fine-tuning.
- The idea of gamifying the experience is not much explored in the literature and it could lead to faster discovery of weaknesses and improvements in model performance.
- The authors split the data pool into an easy and hard split. While their objective is to collect hard questions on the hard split, they must also evaluate players' capabilities in uncovering inaccuracies in the model answers. For this purpose, they slightly "poison" the model answers in the easy split to assess how well a player can distinguish correct answers from slightly inaccurate ones.

### Weaknesses
 - The pool of data considered for the questions is limited to COCO. Despite the scalability that the tool can and did achieve, I expect the major bottleneck to be the limited diversity and quantity of the data pool.
- While the authors report the gain in performance of a group of models when tuned on the collected high-quality data, we lack evidence of the effective level of quality of the collected data and of the effect of such data on the tuning process. Specifically, I would expect to see some metrics/statistics to quantify data quality and more comparisons to distinguish the effects of tuning with the collected data vs tuning with other already-available datasets for instruction tuning.
- There is a lack of comparison of the models tuned on the data w.r.t. other models available in the literature.
- (minor) Tables are very "sparse", i.e., space is not well-optimized, resulting in a paper that feels slightly shorter compared to other works. I am wondering if the paper would gain from reorganizing the tables in a better way and introducing more information from the Appendix or from data statistics/additional comparisons.

### Questions
- Why did the authors focus on COCO and do not consider more "unsupervised" datasets? Why not use large-scale datasets or a mixture of different datasets?
- Can you provide some evidence of the data quality/diversity resulting from the crowd-sourcing? Can you report some statistics regarding, e.g., the categories of the collected questions (as listed in the Appendix), their diversity, etc.? Since the collection was done on COCO, the authors could exploit supervised annotations to categorize questions and images in terms of, e.g., the subject (i.e., annotated classes), properties, etc. What is the average number of questions per image? Are there images/classes with more questions than others?
- How does tuning on the collected data compare with tuning on other already-available instruction tuning datasets?

### Soundness
3

### Presentation
2

### Contribution
3
