# Massively Multi-Agents Reveal That Large Language Models Can Understand Value

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 3, 6, 5

## Abstract
Large Language Models (LLMs) have been trained on vast corpora of data, allowing them to learn internal representations of how humans would respond in different scenarios. This makes them well-suited to simulate the actions of market participants, to model their collective impact on financial markets and perform financial forecasting. However, there also exist various sources of errors that could affect the effectiveness of LLM agent-based simulations of the market. Firstly, individual market participants do not always make rational decisions, which might not be captured by the logical reasoning process of LLMs. Secondly, the numerical and financial literacy of LLMs are also not highly reliable, due to possible knowledge gaps in their numerical understanding and possible hallucinations in their outputs. To tackle these issues, we propose our Massively Multi-Agents Role Playing (MMARP) method, which aims to produce highly accurate market simulations through theory-driven prompt designs. To reduce the impact of noisy actions caused by individual irrational investors, we leverage the LLM-generated next-token weights to simulate repetitive prompting, and obtain the aggregated market response. To minimize the effects of possible gaps in its numerical knowledge or potential hallucinated outputs, we prompt the LLM using a range of price inputs for each trading day. Finally, to produce simulated forecasts of market prices, we perform the above prompting strategies across two types of LLM-agent roles, buyers and sellers, and obtain the intersection price between their response curves. Through experimental results, we show that MMARP can outperform other deep-learning methods and various financial LLMs in forecasting metrics.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents Massively Multi-Agents Role Playing (MMARP), a method that leverages the collective responses of many simulated language model agents to improve stock price prediction. Traditional LLMs struggle with understanding numerical values, which are essential for accurate stock valuation. MMARP addresses this by creating a simulation where each LLM agent acts with a distinct role, such as buyer or seller, across various price points and contextual settings. By analyzing the combined responses of these agents, MMARP approximates market dynamics, producing forecasts that outperform individual LLM predictions and other financial models. This approach highlights how LLMs, through collective behavior, can demonstrate an emergent understanding of complex, value-driven tasks.

### Strengths
1. The paper is well-written, with logical structure and helpful visuals, making complex ideas easy to follow.

2. MMARP creatively applies LLMs in a market simulation context, using collective agent behavior to model demand-supply dynamics.

### Weaknesses
1. Limited Novelty: The approach lacks substantial innovation, as similar methods already use LLMs in agent-based financial simulations with more complex trading mechanisms, such as [1]. The MMARP framework primarily applies LLMs to give binary responses (e.g., cheap or expensive), which adds minimal novelty or depth to financial market simulations. The use of binary responses severely limits the complexity of the simulation, failing to capture the nuanced decision-making processes of actual market participants who consider a range of factors beyond simple price assessments. This oversimplification reduces the practical relevance of the simulation.

2. Overclaims on Numerical Understanding: The paper’s claims about advancing numerical understanding are overstated. The approach lacks clear differentiation between using multiple agents versus a single model for predictions, and it lacks theoretical support to demonstrate how the MMARP setup enhances numerical comprehension. The paper does not provide a control experiment that isolates the effect of multiple agents, making it impossible to determine if the observed performance gains are due to the collective behavior or simply the repetition of the same model. Furthermore, the method does not address the fundamental limitations of LLMs in precise numerical reasoning, such as handling complex mathematical operations or understanding the implications of small numerical differences.

3. Questionable Economic Assumptions: The demand-supply hypothesis may not be valid here, as all agents derive from the same model, sharing identical training data. This setup essentially replicates identical agents, which conflicts with the independent and diverse preferences central to economic theory. The agents' responses are not truly independent, as they are all based on the same underlying model and training data. This lack of diversity in agent behavior undermines the validity of the simulation as a representation of real-world market dynamics, where diverse opinions and risk preferences drive market behavior.

4. Unsubstantiated Multi-Agent Claim: While the paper emphasizes multi-agent interactions, the agents receive similar inputs, model parameters, and inference settings, leading to minimal agent diversity. This makes the simulation more akin to a single-agent system. The minimal variation in input prompts, such as slight price changes, does not create genuine agent diversity. This lack of diversity means the simulation does not capture the complex interactions and emergent behaviors that arise from diverse agents in real markets.

5. Unclear Experimental Design: Although the paper discusses prompt designs and model selection, it lacks transparency regarding the exact inputs, outputs, and inference parameters. A detailed breakdown of these variables would clarify the MMARP method and support its reproducibility. The absence of specific details regarding the prompt structure, the precise numerical values used for price variations, and the inference parameters makes it difficult to replicate the experiments. This lack of transparency hinders the verification of the results and the broader adoption of the method.

6. Limited Experimental Scope: The experiments, based on only 10 stocks over two years, may be insufficient to substantiate the claims. Additionally, key financial LLMs like FinMA and more diverse general-domain models were not included. Relying solely on information coefficient (IC) to assess performance limits the paper’s ability to demonstrate improvements in numerical reasoning.

### Questions
1. Given that similar methods have applied LLMs for agent-based simulations with more advanced trading behaviors, could the authors clarify how MMARP’s contribution significantly advances this area?

2. Could the authors provide theoretical support or evidence that demonstrates how collective responses from agents address or enhance LLMs' numerical reasoning?

3. Since all agents are based on the same LLM model with identical training data and input settings, how do the authors justify the use of demand-supply theory here?

5. Would the authors expand to a larger dataset in multiple assets and different markets or including more diverse financial and general-purpose LLMs?

### Soundness
1

### Presentation
1

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposed a novel method called MMARP (Massively Multi-Agents Role Playing) that simulates responses from many times LLM agent's responses to understand how LLMs process numerical values, particularly in stock valuation tasks. The authors target an interesting problem: how to make LLM better understand numbers in a financial context in order to improve stock prediction performance. In the method, the authors use the law of large numbers to estimate the distribution of a large number of LLM outputs to determine the final result.

### Strengths
1) The author isolates the numerical understanding capability of LLMs and tries to provide insights into how LLMs internally represent numbers. 

2) The author uses token probabilities to simulate LLM agent populations efficiently in numerical understanding.

3) The author conducted a lot of ablation study results and visualization.  

4) The author discusses the potential impact beyond stock prediction to other domains.

### Weaknesses
1) The motivation is not clear. The authors discuss a big problem with LLM in the introduction, but in the end, the experiment was only carried out in the financial domain. Also, is the author's main purpose to propose an evaluation framework or to explore ways to improve the predictive performance of LLM in financial markets?

2) The Background Section is not clear and related work is not comprehensive. In the Financial sector domain, there is a lot of recent work to explore LLM and LLM Agent's capacity in stock trading or financial decision-making:

* [1] "FinAgent: A Multimodal Foundation Agent for Financial Trading: Tool-Augmented, Diversified, and Generalist." arXiv preprint arXiv:2402.18485 (2024). 

* [2] "FinMem: A performance-enhanced LLM trading agent with layered memory and character design." Proceedings of the AAAI Symposium Series. Vol. 3. No. 1. 2024.

* [3] When ai meets finance (stockagent): Large language model-based stock trading in simulated real-world environments. arXiv preprint arXiv:2407.18957. 

* [4] "FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making." arXiv preprint arXiv:2407.06567 (2024). 

These works extensively discuss how to use LLM/LLM agents for stock prediction. Meanwhile, the "Agent-Based Simulation for Large Language Models" subsection in the Background seems to be unrelated.

3) The problem definition is not clear enough. The author mentions the use of the law of large numbers, but only shows the formula for the law of large numbers and then just provides an example to explain it. How to define the problem specifically according to the problem discussed in the paper, what the input is, what the output is, and how convergence is defined in this case? 

4) The authors discuss two aspects that affect the use of LLM for stock prediction in the abstract and introduction: a. simulating human behavior; b. the ability to understand numbers. However, the paper does not seem to discuss a. As the number of LLM outputs increases, so does the number of results for simulating more human behavior. How do the two interact with each other?

5) Evaluation Metrics is not comprehensive. MSE performance is not consistently better than all baselines. Moreover, The commonly used indicators, Sharp Ration, Max Drop Down, ARR, were not included in this framework.

### Questions
See in Weaknesses.

### Soundness
2

### Presentation
1

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
This paper focus on predicting stock prices based on prices and contexts before. The paper hypothesizes that large language models (LLMs) lacks the capability to represent continuous numerical values in this task. Hence, it proposes the Massively Multi-Agents Role Playing method and tries to directly predict the stock price while the process is questionable. The method simulates the reactions of both buyers and sellers to various stock prices and contextual information. It generates the demand and supply curves by plots of reactions, then seemingly enables direct estimation of stock value using the intersection of two curves with insufficient explanation. The paper also notes the large computation load in simulation. It applies the discrete distributions of LLM outputs to simulating a large number of LLM agents , which is efficiently but lacking the comparison with regular methods.

The experiment shows that the prediction ability of the method approaches the state of the art. It analyses the demand curves by LLM agents of a range of prices and contexts. The results show that LLMs have a similar understanding of the numerical significance of stock value similar to economic demand theory.

### Strengths
1. The simulation of LLM agents effectively reduces computational load, enabling larger-scale application.

2. The analysis of the experimental results through the lens of economic demand theory is interesting.

3. The continuous stock price prediction method based on LLM agent interactions integrates relevant economic theories, achieving promising results in both MSE and IC evaluation metrics, and exhibits innovation.

### Weaknesses
1. The methodology does not address how to enhance the LLM's understanding of continuous numerical values. The motivation highlights that LLMs lack efficient encoding capabilities for continuous numerical values, which contributes to their insufficient understanding of numerical significance. But the analysis of solution is lacking. Specifically, the paper does not explore alternative encoding strategies or provide a theoretical framework for why the proposed method should improve numerical understanding beyond simply observing emergent behavior from agent interactions. The core issue of how LLMs represent and process continuous numerical data remains unaddressed, which limits the generalizability and interpretability of the results.

2. The underlying issue of the lack of numerical understanding in LLMs is not resolved fundamentally. Because the interactions between LLM agents cannot genuinely generate real stock price predictions without linear transformation. The paper's reliance on a linear transformation to map the LLM's output to actual stock prices suggests that the LLM itself is not directly learning the numerical relationships. Instead, the method appears to be using the LLM as a complex feature extractor, with the actual numerical prediction being handled by a separate linear model. This raises questions about the extent to which the LLM is truly understanding the underlying numerical dynamics of stock prices.

3. Specifically, the rationale for using a price prompt range of [-1, 1] is not explained, nor is there an explanation for the existence of the “LLM value space”. The choice of the [-1, 1] range seems arbitrary and lacks justification. It is unclear how this range relates to the actual price fluctuations of the stocks being analyzed. Furthermore, the concept of an “LLM value space” is vaguely defined and lacks a clear theoretical basis. Without a proper explanation, it is difficult to assess the validity and generalizability of the proposed method.

4. The differences of simulation’s effect between regular method and the proposed method is not demonstrated. It is not shown whether the method of reducing computational load for simulating LLM agents yields results consistent with those from regular methods (directly use multi LLM agents). The paper does not provide a direct comparison between the proposed method and a more straightforward approach of simulating multiple LLM agents. Without such a comparison, it is difficult to assess whether the computational efficiency gains come at the cost of accuracy or fidelity to the underlying simulation. It's essential to demonstrate that the approximation method does not significantly alter the simulation's behavior.

5. The paper fails to provide an explanation for the abnormal points in predictions (especially Figure 6, 'the LLM agents sometimes predict large changes in price such as 5,000%, which is highly unlikely for the selected stocks in this work.' line 420). The presence of such extreme predictions raises concerns about the robustness and reliability of the method. The lack of explanation for these outliers suggests that the model may be prone to generating unrealistic predictions, which limits its practical applicability. It is crucial to understand the cause of these anomalies and to develop strategies to mitigate them.

### Questions
Refer to weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper evaluates Large Language Models' (LLMs) abilities to understand stock values through two experimental settings. In the first, a single-role agent scenario, LLMs are prompted to categorize stock prices as "Expensive" or "Cheap" based on a target price and contextual financial information including financial status and market updates. In the second, a multi-role agent scenario, an additional "seller" agent is introduced with options of "Good" or "Low" prices, with the same setting. The authors conclude that LLMs demonstrate an approximate understanding of numerical values, their behaviors reflect some economic patterns such as price elasticity,

### Strengths
The paper is mostly clear, with helpful experiments and graphs that effectively illustrate the LLMs' result distribution. It provides strong background and motivation, a well-covered literature review, and a timely, interesting topic. The experiment setup is also well explained including the rationale of stock selection.

### Weaknesses
The title is misleading; the paper discusses how LLMs understand stock prices specifically, rather than "value" in general. A paper addressing LLMs' understanding of value should include broader experiments, such as algebraic problems, rather than focusing solely on stock price estimation.

There are some flaws in the experiment design. As we know, the output of the LLMs is heavily influenced by the context provided. The authors rely on limited stock information summaries to ask LLM make price estimation. However, this information does not represent the full range of data that influences stock prices in the real world. The LLM's output would be easily changed if we select news summary from another source or change the tone of this summary. Based on the experiment alone, it is presumptuous to conclude that LLMs understand values. Instead, the results only suggest that LLMs possess basic financial knowledge and can make context-based financial judgments.

### Questions
In Section 3.1, I don’t fully understand the application of the law of large numbers. It seems the authors treat the logit from the LLM as the ground truth probability for the tokens "Expensive" or "Cheap," and then use simulation to generate results. Why is a simulation of 100,000 agents needed if the token distribution is already known? Additionally, it's unclear why the LLM’s logit output would follow the law of large numbers. This is critical as it directly affect the paper’s claims about "a group of LLMs."

The term "multi-agent" in section 3.2 is overclaimed since only one additional agent is involved. It would be more accurate to describe this as "buyer-seller agents".

### Soundness
3

### Presentation
2

### Contribution
2
