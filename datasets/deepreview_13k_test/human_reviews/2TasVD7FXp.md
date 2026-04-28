# InvestESG: A multi-agent reinforcement learning benchmark for studying climate investment as a social dilemma

- Decision: Accept
- Scores: 5, 5, 8

## Abstract
Supported by both PyTorch and JAX implementation, the benchmark models an intertemporal social dilemma where companies balance short-term profit losses from climate mitigation efforts and long-term benefits from reducing climate risk, while ESG-conscious investors attempt to influence corporate behavior through their investment decisions, in a scalable and hardware-accelerated manner. Companies allocate capital across mitigation, greenwashing, and resilience, with varying strategies influencing climate outcomes and investor preferences. Our experiments show that without ESG-conscious investors with sufficient capital, corporate mitigation efforts remain limited under the disclosure mandate. However, when a critical mass of investors prioritizes ESG, corporate cooperation increases, which in turn reduces climate risks and enhances long-term financial stability. Additionally, providing more information about global climate risks encourages companies to invest more in mitigation, even without investor involvement. Our findings align with empirical research using real-world data, highlighting MARL's potential to inform policy by providing insights into large-scale socio-economic challenges through efficient testing of alternative policy and market designs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper concentrates on developing a multi-agent reinforcement learning framework (which they name InvestESG), to be used to student individual and collective outcomes from company investment and climate risk. It is an overall well written paper on a timely and relevant problem, for which we clearly need to better understand how to drive investors decisions to align individual and collective objectives. The paper is completely application-driven, in the sense that the authors do not develop new methodology, or a new solution approach. They mainly focus on describing how the framework should look like for the purpose of the application. They then generate a lot of simulation results to study various aspects of the problem (e.g., greenwashing, different levels of ESG consciousness, etc.)

### Strengths
The main strength of the paper is the topic is focuses on, and the idea to bring some momentum towards the development of a general platform to simulate a multi-agent system with focus on climate risk and company behaviour. Another strength (but which may also be seen as a weakness - see below) is that the framework is simple, in the sense that it is easily interpretable and flexible enough to interact with e.g. policy makers. The authors also aim to produce some relevant results, which may be seen as of value by policy-makers.

### Weaknesses
As mentioned by authors in a last part of the paper, maybe the main weakness is the simplicity of the framework, which may prevent a broad audience from accepting that it realistically model a real-world situation, and that it may be ring some relevant insights to be used as input to policy-making. In my opinion, it feels like an oversimplified and stylised approach where, depending on a few assumptions and a few modelling changes, we could get the model to do completely different things. Therefore, I believe that quite more work is necessary for such a paper, starting with the importance of the underlying assumptions, assessing the impact of modelling choices, sensitivity analyses, etc. I am not critical of the fact the authors are engaging in such developments - I am saying instead that I feel more work is necessary before sharing this work/paper with the world.

### Questions
I think some of the key points to consider are:
- questioning assumptions, e.g. rationality of the agents, why they would behave as if employing RL, etc.
- convincing us that simulating a system with a limited number of agents provides us with insights that are relevant for systems for very large number of agents
I clearly recognise that such issues may be more generally valid for the case of MARL environments and broader than for the case of this paper only. However, here, in view of the importance of the application, I find these issues particularly relevant.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents InvestESG, a novel multi-agent reinforcement learning (MARL) benchmark designed to simulate and analyse the impact of varying Environmental, Social, and Governance (ESG) disclosure policies through the social dilemma paradigm. InvestESG  uses two types of agents: companies and investors. Companies allocate capital across mitigation, greenwashing, and resilience, with varying strategies influencing climate outcomes and investor preferences. The findings are consistent with empirical research using real-world data. They capture the positive impact of companies using information about global climate risks to determine their level of investment in mitigation, even without investor involvement. The paper is beautifully written and rigorous.

### Strengths
The paper represents a novel contribution in a highly relevant, high-impact domain, at the intersection between climate change and MARL. It is beautifully written and self-contained, with rigorous specifications of the InvesESG environment. The implementation details and code are provided, and overall the paper makes a good case for a MARL benchmark for studying climate investment through the social dilemma paradigm, via two agent types: companies and investors. InvestESG is designed to simulate and analyse the impact of varying Environmental, Social, and Governance (ESG) disclosure policies on corporate climate investments. In InvestESG, companies allocate capital across mitigation, greenwashing, and resilience, with varying strategies influencing climate outcomes and investor preferences. The findings are consistent with empirical research using real-world data. The results capture the positive impact of companies using information about global climate risks to determine their level of investment in mitigation, even without investor involvement.

### Weaknesses
The main weakness of the paper consists in its simplifying assumptions, in terms of the types of agents, and the considered scenarios, analysis and discussions. These limitations are acknowledged in the paper. Due to these reasons, I believe that, in the current format, the paper makes an insufficient contribution for a top conference like ICLR.

For a more significant contribution, this work could be extended in one or more possible directions: extend the agent types (possibly consider insurance companies/market?), add more complex agent behavior, learn parameters and behaviors from real data, include more social outcome metrics (in addition to the final climate risk level and the final total market wealth, at the end of the simulation period) and/or include additional features, such as agent bankruptcy, and a dynamic number of agents.

Assuming the agent-types remain just companies and investors, increasing the number of companies and investors, and learning their behavior from real world data, may be a sufficient extension for a more significant contribution.

In the longer term, the initial vision of InvestESG would benefit from a more diverse agent space, for a more realistic climate-change problem specification (however, this is not essential for a significant contribution).

### Questions
I think the paper could be extended in several possible directions, as indicated in the Weaknesses section, for a more significant contribution. Another possible direction would be to implement and assess the impact of other PPO policies than IPPO on the overall behaviour and insights.

Potential relevant papers are suggested below.

Bisaro, Alexander, and Jochen Hinkel. "Governance of social dilemmas in climate change adaptation." Nature Climate Change 6, no. 4 (2016): 354-359.

Bettini, Matteo, Amanda Prorok, and Vincent Moens. "Benchmarl: Benchmarking multi-agent reinforcement learning." Journal of Machine Learning Research 25, no. 217 (2024): 1-10.

Bettini, Matteo, Ryan Kortvelesy, and Amanda Prorok. "Controlling Behavioral Diversity in Multi-Agent Reinforcement Learning." arXiv preprint arXiv:2405.15054 (2024).

Brogi, Marina, Antonella Cappiello, Valentina Lagasio, and Fabrizio Santoboni. "Determinants of insurance companies' environmental, social, and governance awareness." Corporate Social Responsibility and Environmental Management 29, no. 5 (2022): 1357-1369.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents InvestESG, a MARL environment that studies the impact of ESG disclosures on company and investor agents. The benchmark is meant to simulate companies' investment decisions into climate mitigation, green washing and resilience spending as a social dilemma.

Specifically, the contributions are:

* InvestESG, a climate-economic environment in which investors fund companies, which make decisions about how much to invest in climate-related spending over 100 years starting in 2020.
  * Climate risks grow linearly in the absence of any mitigation
  * Companies decide how much to spend on mitigation, greenwashing and resilience
  * Investors decide which companies to invest in based on their preferences, which trade off between profits and climate efforts documented by ESG disclosures.
  * As the simulation proceeds, companies make profits which they return to investors, while climate risks grow, resulting in a higher probability of extreme events.
  * Agents are modelled using IPPO

* A set of experiments shedding light on agent behaviour in InvestESG
  * With no ESG disclosures, purely profit-driven decisions result in suboptimal collective outcomes
  * The impact of ESG disclosures depending on how many and how much investors care about ESG reports when choosing which companies to invest in
  * Whether companies leverage greenwashing when it is allowed in InvestESG
  * Whether visibility of the climate-related risk probabilities impacts agent behaviour

* Conclusions for policymakers and researchers
  * Mandatory EST disclosure paired with ESG-conscious investors can drive corporate mitigation efforts.
  * Knowledge of climate risks motivates investors and companies
  * Agent behaviour is consistent with empirical evidence
  * InvestESG is an example of using MARL to tackle complex social dilemmas in real-world, high-impact domains

### Strengths
# Originality

* **Novel MARL application to ESG disclosures**: Even though Zhang et al. explore MARL in the policy space, as far as I know, this is the only MARL simulator that looks at ESG disclosure impact in this scenario.

* **Novel problem formulation**: the authors cleanly describe the relationship between companies and investors with a two agent type system, as well as an ESG disclosure component.

# Quality 

* **Relevant problem setup**: key decisions are captured by the problem setup. The ESG disclosure abstraction is simple and elegant. The reward structure effectively represents a social dilemma.

* **Extensive experimental results**: the authors go through many scenarios with InvestESG to analyze different outcomes.

# Clarity

* The paper is **well structured**, and makes for a smooth read with little to no cognitive breaks.

* The work is **well situated** within the literature on MARL simulators, and they contrast well with similar work.

* The design and implementation of InvestESG is **clearly laid out**. 

* The work makes judicious use of **relevant visualizations**, such as Schelling diagrams.

# Significance

* The analysis is **timely and relevant** given the current discussions around ESG disclosures.

* The conclusions around the preferences of investors for climate-active companies is impactful.

* The use of MARL to study social dilemmas is an important subject of study.

### Weaknesses
# Soundness

* **The economic agents are not grounded in the economics literature**. This leads to issues such as capital being perfectly flexible across time steps. In traditional economics models, investments in capital last and they are not flexible. Here, there seems to be an implied assumption of perfectly flexible capital, which is unrealistic. Starting with an existing model of economic agents (with a citation), highlighting its limitations for InvestESG and then explaining how you extend to agent to accommodate for these limitations would be a much more compelling presentation. 

* **Investor decisions are binary**, as opposed to continuous across all companies. Making investor decisions floats, i.e. a vector whose sum is capped at one, would allow for proportional investments across different companies. This is essential for investor diversification, which would also enable interesting extensions like regional damages to companies (i.e. climate events could affect subsets of agents either chosen at random or chosen somehow).

* Figure 7 b) is highly confusing. It looks like **with climate information, risk is *maximized* and market wealth is *minimized***. I'm not sure what exactly is going on in this plot, but it doesn't fit with the storyline of the paper. That is, it certainly does not look like more information improves decision making in this plot, if anything the effects of more information are catastrophic for both climate risk and market wealth.

* Figure 2b could be improved by showing the average number of events at each year across many episodes, as opposed to a single episode. 

* The **number of agents is limited**. Granted, it is more than 2. However, it would be interesting to scale it up to more and see what types of behaviour emerge. There are group size effects that can emerge at scale in economics, e.g. see https://www.aeaweb.org/articles?id=10.1257/mic.20200290. This shows in section 9.2 of the paper in the appendix, but given the implications of such a result, it would be very important to expand upon these results.

# Presentation

* The paper is well structured, but the plots are a pain to read. The labels and ticks are too small, and the axes are not annotated. 

* If you use a pdf format for your images instead of png, you can avoid the graininess when zooming in, which is necessary because of the label sizes.

* The results section could benefit from additional structure. It would be less dense and easier to read if you highlighted which of your results you consider the main results, and which you consider additional.

* I found the description of schelling diagrams fairly unclear, it took me a minute to get it.

* It should be ICLR 2025, not 2024. Please make sure the template you used is up to date.

* Inconsistent use of "MARL" and "multi-agent RL"

- Might benefit for a problem setting section, where you introduce important concepts like bifurcated equilibria

- Typo: 3.2 "self-interest" -> "self-interested"
# Contribution

* The importance of the contributions are weakened by what Figure 9 d) is suggesting, since there are many companies in the world. It seems to me that, without addressing the concerns raised by this result, your conclusions for policymakers do not hold.

### Questions
- What does a sensitivity analysis of the Beta parameter do to the results?

- How would more longer capital investment timelines (e.g. min 5 year lock-in) impact the trained agents?

- Do observations include past climate events?

- How did you calibrate the 0.5% investment of capital into mitigation?

- Why do you think that agents are so insensitive to the value of Beta as shown in figure 6 b)?

### Soundness
4

### Presentation
3

### Contribution
2
