# MarS: a Financial Market Simulation Engine Powered by Generative Foundation Model

- Decision: Accept
- Scores: 6, 6, 8, 8

## Abstract
Generative models aim to simulate realistic effects of various actions across different contexts, from text generation to visual effects. Despite efforts to build real-world simulators, leveraging generative models for virtual worlds, like financial markets, remains underexplored. In financial markets, generative models can simulate market effects of various behaviors, enabling interaction with market scenes and players, and training strategies without financial risk. This simulation relies on the finest structured data in financial market like orders thus building the finest realistic simulation. We propose Large Market Model (LMM), an order-level generative foundation model, for financial market simulation, akin to language modeling in the digital world. Our financial Market Simulation engine (MarS), powered by LMM, addresses the need for realistic, interactive and controllable order generation. Key objectives of this paper include evaluating LMM's scaling law in financial markets, assessing MarS’s realism, balancing controlled generation with market impact, and demonstrating MarS's potential applications. We showcase MarS as a forecast tool, detection system, analysis platform, and agent training environment. Our contributions include pioneering a generative model for financial markets, designing MarS to meet domain-specific needs, and demonstrating MarS-based applications' industry potential.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper makes several contributions: (i) it designs, implements and evaluates Large Market Model (LMM), an order-level generative foundation model, for financial market simulations; (ii) a novel financial Market Simulation engine (MarS), based on LMM, that enables more realistic, domain-specific interactive and controllable order generation. The paper includes evidence of LMM's strong scalability across data size and model complexity, and of MarS's advancements towards more realistic, interactive and controllable order generation with market impact. Various scenarios illustrated the application of MarS for forecasting, detection, analysis, and agent training, thus demonstrating its contributions towards more realistic financial market modelling and simulation frameworks.

### Strengths
The paper makes a contribution in a highly relevant application domain, i.e. realistic financial market simulation frameworks. The methodology is adequate, and experiments and results are included in support of the statements and contribution claims. The main part of the paper is focused on LLM and MaRs, presenting the design and implementation decisions, and a detailed description of the experiments and results. The paper includes evidence of the LLM's scalability across data size and model complexity. In addition, MaRs enables more realistic, interactive and controllable order generation. A range of different scenarios illustrate the applicability of MaRs to key domain-specific tasks such as forecasting, detection, analysis, and agent training, thus demonstrating its contributions towards more realistic financial market modelling and simulation frameworks.

### Weaknesses
The current structure of the main part of the paper prioritises a high-level presentation of LLM and MaRs, and the applicability of the proposed solution to four relevant use cases. The MaRs design and features (Section 2) are also presented at a high level, with insufficient rigour in the problem definition (Section 2.1) -- which may not be known to a ML audience. It is not clear why, for example, being able to provide a text-based description of the desired market scenario, would guarantee controllability (the definition of controllability on page 2 is fairly vague). Similarly, the assumptions made/ requirements about the user-injected orders are not specified. The language is ambiguous in places, e.g. "any possible market condition" (p. 2); "often using recent real orders" (p. 3). More technical detail could be included in Section 2.1.2, for self-contained, rigorously specified problem and solution,  and to support the claims made in this section.

It would help to better define the control signals, and discuss their effectiveness for increasing correlation scores.

### Questions
The main questions and suggestions are derived from the identified weaknesses.

The paper should be restructured by including more specific key definitions and design decisions, including ML-specifc (relevant for the ICLR audience) from the Supplementary Materials into the main paper.

"RL-agent training tasks" is mentioned twice in the paper (p. 8). It would help to link this term to Section 4.4, for improved clarity and readability. Also, discussing the differences between MaRs/LMM and DeepLOB would improve the paper. Clearly defining the synthetic data and synthetic market impact (rather than referring to them indirectly in the main part of paper) would also be helpful.

In addition, it would help for the authors to address reproducibility, in terms of code and data.

Overall, the suggested changes would improve the rigor, clarity and overall contribution of the paper, as well as its suitability for the ICLR audience.

There are some minor spelling/ typo errors, e.g.: "these information concludes" (p. 5); "with constrains" (p. 28); Eq.equation (p.28)

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
In this paper, the authors propose a financial market simulation framework, MarS, powered by a large market model (LMM) trained on real-world limit order book (LOB) data. They introduce two key algorithmic innovations: order sequence modeling, which tokenizes the LOB data, and order batch sequence modeling, which converts it into a tensor representation similar to the RGB format in image processing. These techniques connect LOB market simulation to recent advances in the field. In their experiments, the authors demonstrate that the LMM follows the scaling law for model and training data size, showcasing potential use cases for the framework.

### Strengths
1. A major strength of this paper is its algorithmic innovation in using order book data tokenization and an RGB-like tensor representation, which importantly bridges market simulation with advances in language and vision modeling.

2. The paper introduces a timely topic by connecting LOB market simulation with generative modeling.

### Weaknesses
1. The paper’s reproducibility would benefit from providing additional critical details about the method and implementation.

  - In Section 2.1.1, the authors outline that conditional trading order generation requires several hyperparameters, such as DES_TEXT for general market description and MTCH_R for specifying the matching rule for trading orders. However, the experimental section does not provide configuration details for these hyperparameters in relation to the obtained results.
  
  - While the authors provide sufficient detail on order sequence modeling and order batch sequence modeling, the training process for the ensemble model lacks detailed illustration, and further illustration on how the two methods are combined within the ensemble would be beneficial.

  - The authors mention that the LMM is trained on real-world market data; however, they do not provide data processing details. For example, real-world LOB data includes various order types (e.g., stop-loss orders, limit orders, market orders) that may arrive asynchronously in the market, yet the paper does not specify how these orders are mapped to the bid and ask sides as described.

2. More comprehensive evaluations are needed to demonstrate the authenticity of the simulated market. Although the authors include three tests of stylized facts, further testing to show that the framework conforms to additional stylized facts would strengthen its credibility. Please see "Cont, R. (2001). Empirical properties of asset returns: stylized facts and statistical issues. Quantitative finance, 1(2), 223." for details. Ideally,  multiple iterations and providing confidence intervals for the measures are preferred.

3. Some of the experiments are not necessarily good demonstrations about the model strength and their design need to be further improved.

  - In the 4.2 detection experiment, 1) the manipulation seems can be easily identified due to anomaly in the distribution tail without resorting to the simulation 2) the distribution similarity need to be clearly defined and demonstrate it is statistical different from the others 3) the author may want to compare with other anomaly detection algorithms.

  - The factor analysis is not a good application example because 1) it could also performed on real world data. 2) the simulated market may not good representation about the real-world market if only three stylized facts are satisfied.

4. The paper’s clarity would benefit from further improvement. Since order sequence modeling and order-batch modeling are two key innovations, the description of these methods should be included in the main content rather than in the supplementary materials.

### Questions
- In the section B.2, the author mentioned the index could uniquely identify a limit order. Could the authors provide a concrete example?

- In the order-batch sequence modeling part, is there any mechanism/constraint to prevent the number of cancel order be greater than the outstanding orders? If such scenario happens, how the will the framework cope with it?

- In the section 3.3, I am not following why the interaction ability is evaluated using the correlation. Could the authors elaborate?

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a generative model designed to simulate realistic order-levels scenarios in financial markets. It uses a large language model to analyze the current market environment, taking this information within a proposed large market model. The model comprises two main components: an order-batch model that captures temporal patterns and an order model that addresses the sequential nature of market orders. These orders are then interactive with user's injection in a simulated in a simulated clearinghouse environment.

To validate the model, the paper conducts tests on stylized facts to ensure realistic simulation outcomes and applies the square-root law to assess interactive simulation capabilities. It also evaluates the model’s scalability in large-scale market scenarios.

Following validation, the model is applied in four downstream applications: forecasting, anomaly detection, what-if scenario analysis, and training datasets for agent-based models.

The paper contributes a model for simulating realistic financial markets, which has potential for application across various downstream scenarios.

### Strengths
The paper introduces a Large Market Mode and the MarS engine, which use order-level generative foundation models for simulating financial markets. This is an advancement research expanding on traditional statistical and agent-based models, providing promissing resolution, interactivity, and realism.

This paper is well-written, clear, and consice. It begins by identifying a specific research gap, then clearly states the proposed solution, and explains how it functions. Additionally, the paper describes potential downstream applications and further research opportunities, all within a well-organized logic chain.

### Weaknesses
(1) Time Interval. 
The model discussed in this paper simulates market at the minute level, whereas in actual financial markets, transactions can occur at the nanosecond level. There could be challenges in accurately capturing the extreme volatility and rapid decision-making. Specifically, using a closed-source LLM engine might introduce limitations due to rate constraints. In contrast, this paper employs an open-source engine, which necessitates careful consideration of its reasoning and inferential capabilities to ensure it can effectively model the high-speed dynamics of financial markets. Does the MarS model have the design capability and flexibility to increase the level of trading time intervals?

(2) Multi-order book correlation.
In the design of large market models, the two primary approaches are the order-sequence model and the order-batch model, which capture temporal correlations and patterns. Additionally, in the conditional generation process, it seems to focus solely on a single order book. Considering that markets consist of multiple order books and each asset is significantly influenced by others as well as the market environment, how can the model effectively capture the correlations between different order books?

### Questions
(1) Order-sequence model 
The order-sequence model uses an autoregressive approach to capture patterns within the order book, aiming to predict subsequent orders. However, the diversity of trading strategies among market participants complicates this task, often making the next order seemingly random and unpredictable. For instance, a momentum trader might buy following a price increase, anticipating continued upward movement based on the persistence of price trends. Conversely, a mean reversion trader sees a price rise as a selling opportunity, expecting prices to normalize back to the mean, counter to the current trend. Could you provide literatures or evidences in your experiments supporting a relationship between orders?

(2) Diffusion model
In Figure 1, a diffusion model is introduced. Could you explain the rationale behind this choice and how the diffusion model is utilized in this context?

### Soundness
3

### Presentation
4

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
This paper presents a market simulation environment driven by a generative model that dynamically produces new market orders, based on the current market context and the historical order flow. This enables a responsive, interactive simulation of market dynamics. The model aims at supporting various applications, including forecasting, anomaly detection, market analysis, and agent training.

The core generative model, named the Large Market Model (LMM), is designed on the idea of a "foundation model for financial market simulation, akin to language modeling in the digital world".

### Strengths
- The paper addresses an important and complex challenge, moving a step towards a more general and powerful generative model for limit order book simulation.
- The authors use for the first (to the best of my knowledge) the LLaMA2 architecture for order flow generation, showing also the potential of this architecture with more data and model parameters (Fig.2) 
- The downstream tasks are quite interesting and useful.
- The paper is well written and easy to follow.

### Weaknesses
Overall, I believe the paper has significant merit and I tend to recommend acceptance (and increase my score). However, I have some concerns, particularly regarding reproducibility. I would encourage the authors to make efforts to improve this aspect of their framework.

Below, I outline my main concerns and questions:
- Key details needed for reproducibility, such as code or datasets, are missing.
- Given that this is a conference on representation learning, more discussion on the embedding of orders and the LOB state would be valuable. For instance, are all possible order prices linearly discretized into the range [0, 32)? Are price outliers excluded? does the model use absolute prices or the distance from the midprice?
- What are the training and simulation times? The latter is particularly crucial for the proposed tasks, as generating a few hours of price paths requires thousands of generated orders.
- A discussion of limitations is missing. For example, unlike text with a relatively fixed vocabulary, a fixed embedding for orders might reduce adaptability across different markets?
(see also questions)

Minor:
- Some essential details should appear in the main paper, such as the dataset used and the authors’ use of a LLAMA2 architecture.
- In line 40, when the authors briefly discuss existing market simulation models, it would be helpful to include citations. This will guide readers interested in statistical or agent-based models to relevant literature.
- There is occasional overuse of non-technical terms, such as “gold mine of data,” and some paragraphs (e.g., lines 236 and 240), which are also capitalized. Are these intended as citations?
- In paragraph 2.1.2, clearer spacing or breaks between components would improve readability.
- Typo on line 384 (“classesup…”).
- The diffusion model in Figure 1 is not explained or discussed.

### Questions
- What does "MTCH R" refer to exactly? It’s not clear how a conditional model should interpret a constraint on the "feasible space for each order".

- Is the "SIMULATED CLEARING HOUSE" simply an exchange engine simulating a double auction market, or is it something else? It seems to be the latter. 

- For the order-batch model, which generates orders at the end of each minute, is this the smallest reaction time of the simulation in response to orders? Or does the model plan a minute ahead (a batch of orders) and then refine (by conditioning) that batch using the Order model? How exactly does the condition in Figure 3 function here?

- In Figure 5a, the market replay appears to be shifted (due to buy orders). Is this intentional? Using the replay series as a control? I suggest showing this experiment with a shaded area over multiple simulations with similar buy and sell orders (similar to Figure 17).

- Why is MarS assumed to have a "real" transition distribution P(s | s, a) in Table 1? 

- In Section 4.2, the detection approach is interesting, but I’m curious whether the observed difference in distribution similarity (computed how?) is statistically significant. Are stressful trading days or shocks interpreted as manipulation as well? Before claiming this approach is feasible, it would be helpful to see the average difference in spread distribution over multiple days or periods.

- In Figure 19b, the market impact appears to be permanent. Is it true? What happens if we extend the simulation period?

- How does the model adapt to different markets (without re-training)? For example, Chinese markets generally differ significantly from U.S. markets in terms of liquidity and frequency.

### Soundness
2

### Presentation
4

### Contribution
3
