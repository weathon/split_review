# Decision Information Meets Large Language Models: The Future of Explainable Operations Research

- Decision: Accept
- Scores: 8, 6, 5, 8

## Abstract
Operations Research (OR) is vital for decision-making in many industries. While recent OR methods have seen significant improvements in automation and efficiency through integrating Large Language Models (LLMs), they still struggle to produce meaningful explanations. This lack of clarity raises concerns about transparency and trustworthiness in OR applications. To address these challenges, we propose a comprehensive framework, Explainable Operations Research (EOR), emphasizing actionable and understandable explanations accompanying optimization. The core of EOR is the concept of Decision Information, which emerges from what-if analysis and focuses on evaluating the impact of complex constraints (or parameters) changes on decision-making. Specifically, we utilize bipartite graphs to quantify the changes in the OR model and adopt LLMs to improve the explanation capabilities. Additionally, we introduce the first industrial benchmark to rigorously evaluate the effectiveness of explanations and analyses in OR, establishing a new standard for transparency and clarity in the field.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The authors introduce a framework emphasizing actionable and understandable operational research explanations. They explore how constraints affect decision-making and introduce an industrial benchmark to assess the effectiveness of explanations in operational research.

### Strengths
- The authors tackle a relevant real-world problem
- The authors explore the intersection of explainability for operational research and LLMs - a hot topic right now

### Weaknesses
 - the authors compare their method against only one baseline
 - while one of the key contributions is the development of a benchmark dataset, it is not clear how the data was gathered or what tasks and metrics are considered for it. While some are mentioned, they are not described in detail. 
 - the authors mention the concept of decision information as one of the pillars of explainable operational research. Nevertheless, it is unclear whether results were reported for it.
 - while the authors claim that their framework enables actionable and understandable explanations, they only assess the quality of explanations considering attribution and justification explanations, with no reference to evaluating whether and how actionable the explanations are.

### Questions
Dear authors, 

We consider the research relevant and interesting. Nevertheless, we would like to point to some improvement opportunities:

GENERAL COMMENTS

(1) - We encourage the authors to strengthen the related work considering works related to explainability for operations research. E.g., (a) De Bock, Koen W., et al. "Explainable AI for operational research: A defining framework, methods, applications, and a research agenda." European Journal of Operational Research 317.2 (2024): 249-272. and (b) Thuy, Arthur, and Dries F. Benoit. "Explainability through uncertainty: Trustworthy decision-making with neural networks." European Journal of Operational Research 317.2 (2024): 330-340. Furthermore, the authors could briefly reference explainability metrics mentioned in the literature relevant to this work.

(2) - The authors compare the proposed method only against the OptiGuide baseline. Are there any additional baseline methods they could compare to?

(3) - Do the results reported for Auto vs. Expert only consider the cases when the LLM did not display any kind of errors? Do the scores degrade if considering cases with errors vs. the ones displayed by the baseline model?

(4) - In Section 4.7, the authors provide detailed insight into the failure cases for the proposed method. What are the failure ratios for the baseline method and error typification? Is the proposed method more reliable in this regard? Could the authors increase the number of executions? For example, having two failures in 14 executions is different from observing the same proportion in 100 runs. 

(5) - One of the key contributions of the paper is the creation of a new industrial benchmark dataset specifically tailored to assess the effectiveness of explanations in OR. We would invite the authors to introduce it in greater detail: (a) how was the data obtained?, (b) what tasks were considered and why?, (c) how were the queries created/what experience informed the queries creation and how it was validated that they capture a wide range of scenarios?, (d) what metrics are considered in the benchmark and what is their underlying rationale?, (e) are there any other benchmarks in the field or close domains that should be considered (e.g., to draw inspiration)?, (f) is the benchmark published/will be published?

(6)- The authors mention two aspects being measured to assess the quality of explanations: attribution and justification. We would appreciate some examples of how such explanations look and how they are assessed for correctness. 

(7)—One of the framework's key contributions is the generation of actionable explanations. Nevertheless, we miss a thorough evaluation of this aspect in the explanations generated. Furthermore, it is unclear to us whether this aspect was also included in the proposed benchmark.

(8) - One of the paper's key contributions is the concept of Decision Information and its quantification. Nevertheless, no results have been reported on it. Do the authors consider that reporting it could enhance the understanding of their research work and provide an additional perspective to the ones already exposed in the manuscript?

FIGURES

(9) - Figure 3: We encourage the authors to provide a brief explanation of what the green/yellow highlighted explanations mean. Do they refer to attribution and justification explanation aspects?

TABLES

(10) - Table 2: in the caption, please indicate what does bolding the results mean

(11) - Table 3: highlight the best results (e.g., by bolding them)

(12) - All tables reporting metrics: provide arrows next to the metric names (up/down) indicating whether a higher/lower result is better.

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
3

### Summary
This paper proposes a LLM-based explainable operations research (EOR) framework and evaluates it on a benchmark they created. EOR is a multi-agent framework that starts with a user query and generates an OR program (for Gurobi optimization solver), uses the program to solve the problem and generates explanations of the code as well as answers using LLMs. The experimental evaluation of accuracy and explanations shows that EOR outperforms two baselines.

### Strengths
1. The paper proposes a novel use of LLMs for explainability in the field of Operations Research. The experiments show that such approach is effective as per the ratings given by LLMs as well as human OR experts.
2. Example 3 is quite useful in understanding the task as well as the output of EOR.

### Weaknesses
1. While the paper reads well, some parts are not very clear. In particular:
 - It is not clear how the decision information, the bi-partite graph, the edit distance computation etc. is connected to LLMs. What does `Since LLMs cannot directly perform this quantification, we utilize them to sense these processes and generate explanatory insights.` exactly translate to in figure 2?
- The section 3.1 on problem formulation focusses on explanations. What is the approach/innovation for modeling that translates to improved modeling accuracy in Table 2?
2. The dataset is not shared, the paper states `Notably, the question sets and the queries in this benchmark are developed from scratch and managed in-house`. Would it be made available publicly? Does `developed from scratch` mean manual creation?
3. If EOR enhances the modeling process, could you compare modeling accuracy on other public benchmarks?

### Questions
1. Are the ground truth expert ratings on the quality of explanations part of the benchmark?
2. Why is Table 3 missing some cells?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The work introduces a framework called Explainable Operations Research (EOR) that aims at enhancing transparency in Operations Research (OR) models that incorporate Large Language Models (LLMs). The authors argue that, despite the prevalence of LLMs in OR, the lack of explanations represents a problem. EOR addresses this gap by introducing the concept of “decision Information”. This workflow involves three LLM agents to generate answers to user queries and corresponding explanations. The authors show that their method outperforms other methods in terms of quality of answers and explanations provided.

### Strengths
The paper makes a focused contribution by addressing a niche problem: explainability in OR. While this fits within the broader category of explainability for LLMs, the specificity of this context is important. The presentation is for the most part clear (but see below), and the agentic workflow proposed could be practically useful for practitioners.

### Weaknesses
Clarity and related work: The problem formulation would benefit from concrete examples to clarify what constitutes a "problem" and a "query" in the OR context. A more thorough description of OptiGuide would also help readers understand its role in the comparison. Bipartite graphs are mentioned multiple times, but it remains unclear why they are relevant or how they contribute to the framework—this needs clarification. The focus of EOR on coding tasks is not well explained, and it would be helpful to understand why this aspect is emphasized. Additionally, the paper proposes an agentic workflow but does not cite related literature; such citations should be included in the related work section.

Similarly, it’s also hard to judge the significance of the work because related work is hardly discussed. The workflow appears simple and I think that the novelty may not be enough for an ICLR paper.

Evaluation results: This is the main weakness. The benchmark used in experiments is not publicly available and is poorly described, making it hard to assess the quality of the experiments. The experimental section mentions a "proprietary LLM" without specifying which model is used, adding ambiguity to the evaluation. The explanation quality assessment relies on LLMs, but it is unclear if any manual evaluation by the authors was performed to validate these judgments. The experimental section needs many more results; currently, it's hard for the reviewer to judge the quality of the work.

### Questions
Posted as part of weaknesses.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a framework called Explainable Operations Research (EOR) that combines Operation Research (OR) with LLMs. This idea aims to improve the clarity and trustworthiness of decision-making processes. The ultimately expected results should be clear, actionable explanations of how changes in constraints or parameters would affect OR solutions.

The claimed contributions in this paper are: (1) the authors formulate the problem of the explainable OR problems within the context of LLMs, (2) the authors introduce the concept of "Decision Information" and utilize bipartite graphs with LLMs to quantify the importance, (3) the authors develop a new benchmark specifically designed to evaluate the effectiveness.

### Strengths
Although I am not deeply familiar with the OR domain, the integration of LLMs with OR problems seems both interesting and innovative. While I initially had concerns about the strict reasoning required for OR problems, it appears that these concerns are somehow addressed through the design choices and the experimental results presented in the paper. However, I may have missed some of the finer details of the concepts.

Overall, the paper is well-presented and easy to follow. Some figures and diagrams could be simplified or made more intuitive, which would help readers with less background in LLMs or NLP better understand the concepts. In addition to the methods, the experimental setup is convincing and thorough.

The significance of this approach is clear. By using this framework, users can gain insights into critical aspects of OR problems that have often been overlooked, enhancing their understanding and decision-making.

### Weaknesses
Since developing a benchmark is listed as one of the contributions, a more detailed introduction to this benchmark is expected. It would be helpful to expand on things like why certain problem categories were selected, how comprehensive the benchmark is across various OR tasks, and whether it reflects real-world complexity. Furthermore, examples showing how the benchmark effectively measures explainability in practice would strengthen the paper. This would provide more transparency about how the benchmark can be applied and generalized.

Although the paper presents a dual evaluation (automated and expert) to assess explanation quality, it doesn’t fully explore how well these metrics align with user needs (who are, in other words, the major user groups if it is put into real-world use). For instance, it is unclear whether the explanation quality metrics are used to capture all the necessary aspects of understandability, particularly for non-experts. Providing more insights into how the explanations are judged, probably by including user feedback or more detailed breakdowns of the evaluation criteria, would offer a stronger case for the robustness of the framework.

An analysis of computation complexity/scalability would also help strengthen the paper. I have potential concerns regarding the computational complexity of the proposed framework, especially given the use of LLMs and graph-based methods.

### Questions
See some of the questions above in Weakness. In addition:

Regarding the benchmark (for explainability): What were the criteria for selecting the problem categories, and how comprehensive is the benchmark in terms of covering different types of OR challenges? Additionally, have you validated the benchmark with industry professionals or in practical settings to ensure it reflects real-world complexity?

Regarding the system-level workflow: Have you considered how decision-makers would interact with the system and its explanations in real time? What if the system makes mistakes, can it be corrected under human supervision?

Regarding the experimental setups/scalability: The paper compares EOR to OptiGuide, but have you considered comparing your work to other explainability frameworks outside the OR domain? Can this work be somehow extended to other similar domains but with different contexts, e.g., automated reasoning?

### Soundness
3

### Presentation
3

### Contribution
3
