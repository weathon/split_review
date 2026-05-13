# Advancing Algorithmic Trading with Large Language Models: A Reinforcement Learning Approach for Stock Market Optimization

- Decision: Reject
- Scores: 1, 6, 8, 3

## Abstract
In the fast-evolving landscape of financial markets, effective decision-making tools are essential for managing complexities driven by economic indicators and market dynamics. Algorithmic trading strategies have gained prominence for their ability to execute trades autonomously, with Deep Reinforcement Learning (DRL) emerging as a key approach for optimizing trading actions through continuous market interaction. However, RL-based systems face significant challenges, particularly in adapting to evolving time series data and incorporating unstructured textual information. In response to these limitations, recent advancements in Large Language Models (LLMs) offer new opportunities. LLMs possess the capacity to analyze vast volumes of data, providing enhanced insights that can complement traditional market analysis. This study proposes a novel approach that integrates six distinct LLMs into algorithmic trading frameworks, developing Stock-Evol-Instruct, an innovative instruction generation algorithm. This algorithm enables RL agents to fine-tune their trading strategies by leveraging LLM-driven insights for daily stock trading decisions. Empirical evaluation using real-world stock data from Silver and JPMorgan demonstrates the significant potential of this approach to outperform conventional trading models. By bridging the gap between LLMs and RL in algorithmic trading, this study contributes to a new frontier in financial technology, setting the stage for future advancements in autonomous trading systems.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper presents a novel approach to algorithmic trading that combines Deep Reinforcement Learning (DRL) with Large Language Models (LLMs). The author introduce "Stock-Evol-Instruct," a new instruction generation algorithm that helps optimize trading strategies by incorporating LLM-driven insights from financial news. The study examines six different LLMs, including LLaMA-2, LLaMA-3, Mistral-7B, Falcon-7B, OpenELM, and GPT-4o, integrating them with DQN and DDQN reinforcement learning methods. Testing their approach on Silver (SLV) and JPMorgan (JPM) stocks, the paper found that LLM-enhanced trading strategies often outperformed traditional RL methods alone, with some models achieving significant improvements in Sharpe Ratio and ROI. The fine-tuned Mistral-7B model, in particular, showed strong performance with ROIs of 53.15% and 48.36% for JPM and SLV respectively. The paper demonstrates the potential of combining LLMs with reinforcement learning to create more sophisticated and effective algorithmic trading systems.

### Strengths
The paper studies an important problem, i.e., automatic financial trading with LLM-enhanced reinforcement learning.
The author conducted extensive experiments to validate the proposed approach.

### Weaknesses
1. The literature review is not thorough, many relevant papers in LLM/AI for finance and trading area are missing. Some paper I found relevant are listed below, but I believe there are more to be included.

2. The writing of the paper can be improved. However, the main problem is the novelty of the work is really limited due to that the author did not conduct a thorough literature review for the field of RL/DL/LLM for trading. There are so many important and related work in this field that should at least be included as baselines for comparison. I recommend authors first conduct a comprehensive literature review in this field, then conduct comprehensive and fair baseline comparisons.


Yu Y, Li H, Chen Z, et al. FinMem: A performance-enhanced LLM trading agent with layered memory and character design[C]//Proceedings of the AAAI Symposium Series. 2024, 3(1): 595-597.

Yu Y, Yao Z, Li H, et al. FinCon: A Synthesized LLM Multi-Agent System with Conceptual Verbal Reinforcement for Enhanced Financial Decision Making[J]. arXiv preprint arXiv:2407.06567, 2024.

Yuan Z, Liu J, Zhou H, et al. LEVER: Online Adaptive Sequence Learning Framework for High-Frequency Trading[J]. IEEE Transactions on Knowledge and Data Engineering, 2023.

Yuan Z, Liu H, Hu R, et al. Self-supervised prototype representation learning for event-based corporate profiling[C]//Proceedings of the AAAI Conference on Artificial Intelligence. 2021, 35(5): 4644-4652.

### Questions
Please refer to my questions above.

### Soundness
2

### Presentation
1

### Contribution
1

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores the integration of LLMs with RL to enhance algorithmic trading strategies in financial markets. By leveraging LLMs such as GPT-4o, LLaMA, and Mistral alongside DQN and DDQN models, the study demonstrates how LLM-driven insights from financial news can improve trading agents' decision-making.

It evaluates the effectiveness of various LLM-RL combinations on two case-study stocks, Silver (SLV) and JPMorgan (JPM), measuring performance through metrics like Return on Investment (ROI) and Sharpe Ratio (SR). Results indicate that LLMs integrated with RL strategies can outperform traditional RL alone by providing contextual market insights.

In the experiment, LLaMA-3 showed higher accuracy in trade prediction, while Mistral-7B excelled in profitability. It also  emphasizes the role of prompt design in optimizing model outputs and addresses the limitations of prompt diversity, suggesting future expansion.

### Strengths
1. Originality: The paper presents an innovative combination way of LLMs with RL algorithms and it expands the applicability of LLMs in quant trading. Compared to the previous work of applications in LLM and RL in financial trading, like FinMem, FinGPT and FinRL, which focuses on either financial LLMs—using NLP techniques to interpret market sentiment and to output trading decision—or DRL models designed for financial decision-making based purely on quantitative market data, this study bridges these two areas.

2. The study is thorough in its design and evaluation, offering clear descriptions of methodologies, metrics (ROI, Sharpe Ratio), and prompt types (zero-shot, instruction-based, and exemplar-based).

3. The paper is well-structured, with distinct sections dedicated to prompt design, trading environment, evaluation metrics, and empirical results.

4. The significance of this work lies in its contribution to enhancing algorithmic trading strategies through a novel combination of LLMs and DRL. Though still exploratory, this combination highlights a useful direction for future research into more nuanced decision-making systems in finance.

### Weaknesses
Absence of Baseline Comparisons: While the paper demonstrates that LLM-RL combinations outperform traditional RL models, it lacks comparisons to other established baselines or hybrid approaches in financial NLP or multi-modal models for trading, such as FinRL, FinMem.

### Questions
1. Would the authors consider adding other baselines in future work?

2. Given the importance of risk management in financial trading, could the authors elaborate on any plans to integrate risk-sensitive Reinforcement Learning (RL) approaches?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper explores a new approach to algorithmic trading by integrating LLMs with deep reinforcement learning to analyze and predict stock market trends.

It contributes meaningfully to algorithmic trading research by proposing an innovative model that combines LLMs and deep reinforcement learning. With refinements in prompt diversity, a deeper analysis of metrics, and further exploration of model limitations, the research could have a significant impact on the field of financial technology.

### Strengths
This paper presents a forward-thinking approach by merging LLMs and deep reinforcement learning, bridging the strengths of LLMs in handling unstructured data and deep RL's adaptability in a dynamic environment.

The authors outline their contributions well, particularly the development of Stock-Evol-Instruct.

Testing on real-world data (Silver and JPMorgan) is a strong point, as it validates the model's performance in practical scenarios.

The paper incorporates different prompt designs for LLM predictions, which offers a robust testing ground for prompt optimization.

### Weaknesses
There is an inconsistency in performance metrics (SR and ROI), which the authors highlight. The authors could delve deeper into explaining the contributions under which these inconsistencies occur and propose adjustments.

The study relies on a relatively small set of prompts for instruction generation, which may restrict the model's generalization across various market conditions.

The Stock-Evol-Instruct method includes in-depth evolving steps, which may introduce redundant complexity. Simplifying this process or providing a clearer rationale for each evolution step could improve understanding and replicability.

A more systematic analysis of how different LLMs align with specific trading objectives would strengthen the case for the chosen models.

### Questions
How do you plan to address the inconsistencies in the metrics in your evaluations?

What criteria were used for selecting the LLMs? How do they compare in performance beyond their general strengths in NLP?

Given the limited prompt variety, do you foresee exploring automated prompt generation or using techniques like semi-supervised learning to enhance prompt diversity?

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a method leveraging Large Language Models (LLMs) to enhance reward mechanisms in a reinforcement learning (RL) trading algorithm, specifically a Double Deep Q-Network (DDQN). Traditionally, RL trading algorithms derive rewards solely from investment returns. However, this paper explores using LLMs to modify or replace conventional rewards in certain scenarios, aiming to help the RL agent trade more like a human. Additionally, the authors use prompt-based techniques to create a novel stock market dataset for fine-tuning the LLM. The paper evaluates the performance of different LLMs, using various prompts, on two stocks (JPMorgan and Silver), showing that RL agents incorporating LLM-generated rewards outperform those using traditional reward structures.

### Strengths
The authors tested a wide range of LLMs with various prompt types, and the writing is clear and concise in most sections.

### Weaknesses
It's standard practice in stock trading papers to show trading trajectories in charts, but this was missing here.
The paper lacks a clear justification for choosing JPMorgan and Silver for testing. Since LLMs rely heavily on textual data, similar studies typically select stocks based on the amount of news coverage during a given period.
While the paper evaluates each LLM and prompt, it fails to include common baselines like "buy and hold" strategies. Additionally, it does not compare results with a baseline using only LLMs for stock trading, which would help show the added value of the RL trading algorithm.
The relationship between the RL algorithm and LLM is difficult to follow. Often times, LLM or RL agents alone can be used for trading. Therefore, it is not obvious to user how does their combination work. This paper uses LLMs to refine rewards in addition to price-based rewards for the RL trading algorithm. This could be explained more clearly in both the text and accompanying figure (figure 1).

### Questions
During evaluation, does the RL agent have access to the news information or LLM output? Need to be more clear about what input features used during evaluation.

Could you include a visual representation of the trading trajectories in your experiments? It’s a common approach in stock trading papers and helps readers better understand the performance over time.

What was the rationale behind choosing JPMorgan and Silver for testing? 

More detailed explanations in the text and clearer figures could improve the reader's understanding in the relationship between LLM and RL agent.

### Soundness
2

### Presentation
1

### Contribution
2
