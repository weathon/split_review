# GLEE: A Framework and Benchmark for LLM Evaluation in Language-based Economics

- Decision: Reject
- Avg Score: 4.75
- Scores: 5, 5, 6, 3

## Abstract
Large Language Models (LLMs) show significant potential in economic and strategic interactions, where communication via natural language is often prevalent. This raises key questions: Do LLMs behave rationally? Can they mimic human behavior? Do they tend to reach an efficient and fair outcome? What is the role of natural language in the strategic interaction? How do characteristics of the economic environment influence these dynamics?
These questions become crucial concerning the economic and societal implications of integrating LLM-based agents into real-world data-driven systems, such as online retail platforms and recommender systems.
While the ML community has been exploring the potential of LLMs in such multi-agent setups, varying assumptions, design choices and evaluation criteria across studies make it difficult to draw robust and meaningful conclusions. To address this, we introduce a benchmark for standardizing research on two-player, sequential, language-based games. Inspired by the economic literature, we define three base families of games with consistent parameterization, degrees of freedom and economic measures to evaluate agents' performance (self-gain), as well as the game outcome (efficiency and fairness). We develop an open-source framework for interaction simulation and analysis, and utilize it to collect a dataset of LLM vs. LLM interactions across numerous game configurations and an additional dataset of human vs. LLM interactions.
Through extensive experimentation, we demonstrate how our framework and dataset can be used to: (i) compare the behavior of LLM-based agents to human players in various economic contexts; (ii) evaluate agents in both individual and collective performance measures; and (iii) quantify the effect of the economic characteristics of the environments on the behavior of agents. We believe that our framework can contribute to the growing intersection of LLMs, ML, and economics, and we encourage researchers to explore it further and build on its foundation.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper proposes a benchmark to evaluate the behaviors of LLMs in economic games, with detailed parameterization on the game design and well-defined evaluation metrics. It also uses the benchmark to produce over 950k game results between LLMs, and 3405 game results involving humans for future research.  Results analysis in terms of game parameters is also provided

### Strengths
- The parameterized economics game design in the paper is comprehensive, and the scale of data simulation is very large.
- Using a regression model to simulate the results of human participants to compare with LLM behavior is new and interesting.

### Weaknesses
 - The paper is not easy to read, especially when introducing the different scenarios and their degree of freedom. It would be easier if the user could use a graph to display the difference of scenarios and a table to introduce each game parameter.
- Data from humans is more inconsistent compared to LLMs due to the variance of humans; the author should give more illustration on the validity of using a regression model to model human results.
- The analysis of parameters on the final evaluations is not enough; it is hard to find clear conclusions from the main part of the paper.Also, the figures, for example, in Figure 1, are hard to comprehend.

### Questions
- In line 447-449, the author mentions Human achieves the worst performance when playing Bob and poor performance in negotiation game, which is counterintuitive. Can the author give more analysis on the results?
- In Lines 499-500, Could the decrease of efficiency under the full information originates from the model's limited capability of dealing with long context?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper introduces GLEE, a unified framework designed to evaluate Large Language Models (LLMs) in language-based economic games, specifically focusing on two-player, sequential interactions across three game families: bargaining, negotiation, and persuasion. The authors present a comprehensive parameterization of these games, develop an open-source framework for simulation and analysis, and provide extensive datasets from both LLM vs. LLM and human vs. LLM interactions. The work aims to standardize research in this domain, facilitating comparative studies and deeper insights into the behavior of LLM-based agents in economic contexts.

### Strengths
1. Comprehensive Framework: The paper presents a well-structured framework that encompasses a wide range of game configurations, inspired by established economic literature. This breadth allows for extensive exploration of LLM behaviors in diverse scenarios.

2. Data Collection Effort: The authors have invested considerable effort in data collection, amassing interactions from 954K LLM games and 3,405 human vs. LLM games. This substantial dataset is valuable for the research community.

3. Open-Source Contribution: By releasing the code and data on GitHub, the authors facilitate reproducibility and encourage further research, aligning with open science principles.

4. Integration of Human Data: Including human vs. LLM interactions provides a meaningful benchmark to assess the similarities and differences between human and artificial agents in economic decision-making.

### Weaknesses
1. Limited Novelty in Framework Design: While the framework is comprehensive, similar benchmarks and frameworks already exist in the multi-agent and economic game theory domains[1,2,3]. The paper does not sufficiently highlight what differentiates GLEE from existing works, nor does it clearly establish the unique advantages or novel aspects that GLEE brings to the table.

[1] Can Large Language Models Serve as Rational Players in Game Theory? A Systematic Analysis

[2] How Far Are We on the Decision-Making of LLMs? Evaluating LLMs' Gaming Ability in Multi-Agent Environments

[3] GTBench: Uncovering the Strategic Reasoning Limitations of LLMs via Game-Theoretic Evaluations

2. Limited Models: The paper utilizes models like Qwen-2-7B and Llama-3-8B, which may not represent the cutting-edge LLMs available at the time of submission, such as GPT-4o. 

3. Superficial Analysis: The exploratory data analysis, while extensive, remains relatively superficial. The regression models used to predict metrics achieve moderate adjusted R-squared values (e.g., 0.57 for bargained efficiency), indicating that the models may not fully capture the complexities of the interactions. There is a lack of in-depth analysis or novel insights derived from the data.

### Questions
1. How does GLEE fundamentally differ from existing multi-agent and economic game theory benchmarks? Can you highlight specific features or capabilities that make GLEE uniquely valuable to the research community?

2. Beyond the parameterization and data collection, what novel theoretical insights does GLEE introduce to advance our understanding of LLM behaviors in economic settings?

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
4

### Summary
The paper introduces GLEE, a framework and benchmark for assessing Large Language Models (LLMs) in economic language games, including bargaining, negotiation, and persuasion. GLEE standardizes evaluation through metrics like fairness, efficiency, and self-gain, collecting data from LLM and human interactions across multiple configurations.

### Strengths
The work provides a unified framework for evaluating LLMs in economic settings, which is novel and addresses the lack of standardized methods in this area.  This benchmark has various setups inspired by the economics literature covering various domains like bargaining, negotiation, and persuasion. The work also has extensive data collection, especially it collects 34k human-involved games from 3,405 players. This offers a solid foundation for analysis.

### Weaknesses
I in general think the work has a solid contribution to the community. However, my concerns are the games and metrics used (bargaining, negotiation, persuasion) could be limited in economic scope, potentially restricting real-world applicability. All the task setups are grounded in specific settings (e.g., Alice, Bob), which might bias the models resulting in misleading conclusions. Besides that, the work relies on only 4 LLMs without exploring a broader range of models limits the generalizability of findings.

### Questions
1. Could additional economic scenarios be tested to broaden applicability?
2. You define some metrics like Self Gain, Efficiency, and Fairness for different scenarios. Are there any pointers to show the validity of the definition? And would the trajectories of LLM interactions influence the scores? If not, what's the justification?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces a framework for evaluating Large Language Models (LLMs) within economic interactions modeled as two-player sequential games. It aims to standardize research in this area by providing a comprehensive parameterization of three families of games: bargaining, negotiation, and persuasion. The framework includes a dataset of LLM vs. LLM interactions and human vs. LLM interactions, facilitating comparisons of agent behaviors and outcomes in terms of self-gain, efficiency, and fairness.

### Strengths
1. The paper introduces interesting classifications for agent types in economic simulations, focusing on aspects such as game horizon, information structure, and communication form.
2. The constructed simulation framework provides extensive data comparing LLMs and humans, which could be valuable for further analysis.

### Weaknesses
1. The framework presented in this paper lacks a bit novelty, as concepts such as bargaining and negotiation have already been addressed by existing evaluation frameworks [1, 2]. I did not find a significant distinction between this framework and prior economic frameworks.
2. Several important metrics in the analysis are not clearly defined. For example, how the economic measures of efficiency and fairness are defined and calculated in your framework?
3. The motivations of both parties are crucial components that should be integrated into the framework. For example, examining the different outcomes in bargaining scenarios, such as Alice (Fair) vs. Bob (Fair) or Alice (Selfish) vs. Bob (Fair), would provide valuable insights.

### Questions
See Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
