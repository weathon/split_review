# Measuring Free-Form Decision-Making Inconsistency of Language Models in Military Crisis Simulations

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 3, 5

## Abstract
There is an increasing interest in using language models (LMs) for automated decision-making, with multiple countries actively testing LMs to aid in military crisis decision-making. 
    To scrutinize relying on LM decision-making in high-stakes settings, we examine the inconsistency of responses in a crisis simulation ("wargame"), similar to reported tests conducted by the US military.
    Prior work illustrated escalatory tendencies and varying levels of aggression among LMs but were constrained to simulations with pre-defined actions.
    This was due to the challenges associated with quantitatively measuring semantic differences and evaluating natural language decision-making without relying on pre-defined actions.
    In this work, we query LMs for free form responses and use a metric based on BERTScore to measure response inconsistency quantitatively.
    Leveraging the benefits of BERTScore, we show that the inconsistency metric is robust to linguistic variations that preserve semantic meaning in a question-answering setting across text lengths.
    We show that all five tested LMs exhibit levels of inconsistency that indicate semantic differences, even when adjusting the wargame setting, anonymizing involved conflict countries, or adjusting the sampling temperature parameter $T$. 
    Further qualitative evaluation shows that models recommend courses of action that share few to no similarities. 
    We also study the impact of different prompt sensitivity variations on inconsistency at temperature $T = 0$.
    We find that inconsistency due to semantically equivalent prompt variations can exceed response inconsistency from temperature sampling 
    for most studied models across different levels of ablations.
    Given the high-stakes nature of military deployment, we recommend further consideration be taken before using LMs to inform military decisions or other cases of high-stakes decision-making.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper investigates the inconsistency of large language models (LLMs) in terms of ablations like sentence order and semantics when applied in war games. The authors focus on measuring free-form response variability using BERTScore to quantify inconsistencies. The findings indicate that the LLMs exhibit considerable inconsistency in their response, which raises concerns about their reliability in high-stake decision-making contexts.

### Strengths
1. The overall presentation is very clear and intuitive
2: The experimental setups are rigorous - experiments are run with multiple LLMs, variations in prompt scenarios, and statistical controls to examine the consistency across different levels of temperature settings and prompt structures.
3. Besides quantitative measures, the paper provides qualitative examples that provides valuable insights
4. The prompts are fully provided for ease of reproduction

### Weaknesses
1. The paper focuses on a very specific hypothetical military scenario. It’s also uncertain whether the observed inconsistency is unique to the wargame setup or would generalize to other critical decision-making applications. This might limit the generalizability to other high-stakes applications.
2. The paper’s main innovation centers on using BERTScore as an inconsistency measure, which may not offer significant novelty in approach. 
3. The study also did not sufficiently compare this approach with other potential inconsistency measurements. 
4. The choice of a default temperature setting of 1.0 in Section 5 may not be appropriate, as it introduces significant response inconsistency by design.
5. The comparison are limited to a few closed-source LLMs
6. While the study demonstrates that LLMs can produce inconsistent responses, it would be more impactful if it included strategies for reducing such variability.

### Questions
1. Why was the wargame scenario chosen as the primary setting for examining inconsistency in high-stake decision making? Do you believe the inconsistency findings would generalize to other types of critical scenarios, or are they specific to the military context?
2. In Section 5, why was a temperature of 1.0 chosen as the default setting?
3. Could this research potentially inform new methods to improve LLM consistency in decision-making contexts?

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This paper presents an investigation of the consistency of LLM responses in a military strategy scenario. Authors invert the BERTScore measure of semantic similarity to compute an inconsistency score, which they validate in a synthetic free-form QA setting based on Truthful QA. In the experiments, the paper shows that LLMs' answers are generally quite inconsistent in both types of generations for their scenario (initial, continuations). They also explore the effect of temperature on inconsistency, as well as the effect of prompt variations.

### Strengths
- I appreciate the paper's main goal of investigating LLM inconsistencies in high-stake military scenarios
- I liked that the authors performed a validation of the inconsistency score using synthetic data with TruthfulQA, which also allows readers to calibrate on what score values mean.
- The main experiments were well executed.
- I liked the investigations into the prompt variations.
- I also appreciated the disclaimer at the end of the introduction.

### Weaknesses
 - The paper's main weakness is the conceptual problem definition.
    - I feel like in realistic high-stakes settings, the temperature should probably be set to 0, which is similar to greedy decoding. Authors should probably focus their experiments on that temperature, though I'm expecting very low inconsistency. More importantly, authors should make a clearer argument for why t=0 should not be used in these high-stakes settings, or why t>0 should be studied.
     - Concretely, I feel like section 6 was most relevant to the realistic way that LMs should be used. I wish authors had expanded on such experiments, possibly exploring various types of rephrasing and exploring exactly how the inconsistencies were affected.
- Second, I feel like the paper's results might be limited in terms of generalizability due to there being only one wargame scenario considered. I understand that this is a relevant vignette, but it would be very interesting to have at least 3-5 high-stakes scenarios (either all wargame or some other high-stakes domains like healthcare). This would ensure that the results aren't an artefact of the topics or domain chosen in the one scenario.
- Third, I felt like the paper could use more in-depth analyses w.r.t. how model responses are inconsistent. The measure at hand is quite coarse-grained, and might not be able to capture more nuanced consistent/inconsistent outputs (e.g., LLM outputs offering two alternatives, one of which is similar between two outputs). Given the specific and high-stakes nature of the scenario, it'd be really useful to have more insights into how the outputs differ, as currently, the coarse-grained measure yields very little information about how inconsistencies should be mitigated (other than lowering the temperature).
- Missing citations: http://arxiv.org/abs/2203.12258, https://arxiv.org/abs/2311.00059, https://arxiv.org/abs/2310.11324
- L204: Authors mention a bi-directional entailment clustering method, but without more details, it seems very confusing why the authors mentioned that... I would remove that sentence or specify why they needed to test that method and why they didn't include the results in the final main text.

### Questions
NA

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes to examine how reliable LLMs are in high stakes decision making situation. For this, the authors conduct crisis simulations with free form responses and using bertscore and measure the inconsistencies across 5 LLMs. Across experiments conducted, this study shows that there inconsistencies even after fixing parameters like conflict anonymization and temperature, and show that prompt variations can lead to greater inconsistency than temperature adjustments.

### Strengths
- the paper is well written and the methodology is easy to follow
- with the increasing use of LLMs in different areas, the focus on high-stakes decision-making contexts is timely and of importance

### Weaknesses
 - The framework for measuring inconsistency uses only BertScore. This potentially limits the evaluation setting to the discrepancies found through semantic similarity missing other forms of inconsistency.
- There is no human evaluation or correlation to human judgement of the inconsistency score. 
- I understand that the objective of this study is to probe LLMs for inconsistency in this particular context. While this study underlines a problem, it does not suggest possible mitigations for the issue of inconsistency.

### Questions
Besides inconsistency, is the proposed evaluation framework able to highlights other types of errors or discrepancies?

### Soundness
2

### Presentation
3

### Contribution
2
