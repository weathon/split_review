# Programmatic Evaluation of Rule-Following Behavior

- Decision: Reject
- Avg Score: 4.75
- Scores: 3, 5, 6, 5

## Abstract
As Large Language Models (LLMs) are being deployed today with increasing real-world responsibilities, it is important for us to reliably specify and constrain the behavior of these systems. However, evaluating a model's adherence to even very simple rules (e.g., "do not generate abusive text" or "do not aid the user in the commission of crime") requires costly human judgment, which slows down the monitoring and improvement of rule-following behavior in LLMs. 
Motivated by that, we propose the Benchmark for Identifying Non-compliant Decisions (BIND), a framework to programmatically evaluate rule-following in LLMs. BIND consists of 15 text scenarios in which the model is instructed to obey a set of rules while interacting with the human user. The scenarios are inspired by various security properties of computer systems and simple children's games. Each scenario has a concise evaluation program to decide whether the model has broken any rules in the conversation, which also means all our scenarios can be trivially solved by corresponding programs. Through extensive qualitative exploration of model behavior in our scenarios, we identify 6 different categories of attack strategies. We then systematically hand-write a suite of 862 test cases implementing specific strategies from these 6 categories and evaluate currently popular proprietary and open-source models. All evaluated models struggle on the test suite: GPT-4, the best overall model, passes only 73.9% of test cases, while Llama2-7B only passes 26.1% of test cases.
Additionally, we evaluate the performance of Llama2 and Vicuna under adversarially optimized inputs, which reliably drive pass rates down to $0\%$ across multiple scenarios. We propose BIND as a challenging new setting for open research into defending against both human-written and automatic attacks on LLMs, as well as exploring rule-following model behavior.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors describe a framework/benchmark named BIND that evaluates the ability of LLMs to follow rules under various scenarios (benign and adversarial).  They evaluate various LLMs using this benchmark and conclude that most LLMs in the status quo are not compliant with rules that are specified.

### Strengths
1. Benchmark is first of its kind.

### Weaknesses
1. Unclear what takeaways can be drawn from this work.
2. Paper could benefit from some reorganization.

1. The writing of the paper could benefit from some thought. For example, the authors could give examples of scenarios, rules and test cases to better highlight the difference between the 3 categories. 
2. The paper provides limited takeaways from their experiment. It is incredible that the authors have come up with such a benchmark. But what can I learn because of it apart from the fact that LLMs do not follow rules (which was already a well know fact. Look at work from Percy Liang’s group — https://arxiv.org/abs/2307.03172, or the fact that LLMs used in search e.g., BingChat can easily be subverted with prompt injection attacks)? The fact that there’s nothing beyond the creation of this benchmark is making this reviewer apprehensive in recommending acceptance.
3. One conceivable application is one where the models are deployed in real-world systems (e.g., as in BingChat) and one would want to understand how brittle these are. But to validate such a scenario, the authors need to consider “layered defenses” i.e., add an output filter atop the generations from the LLMs and see how much information can be exfiltrated in such a setting. However, this was not done in this work.
4. A lot of the findings presented by the authors have been covered earlier i.e., numerous prompt injection strategies discuss mechanisms of rule subversion. This work, to me, seems like a consolidation of those findings. Could the authors emphasize the difference?

### Questions
Overall, this work is interesting and potentially exciting but the main takeaways are not communicated in a clear manner. This reviewer is wondering what I can learn from this paper, and how others can follow-up on this line of work.

    1. The writing of the paper could benefit from some thought. For example, the authors could give examples of scenarios, rules and test cases to better highlight the difference between the 3 categories. 
    2. The paper provides limited takeaways from their experiment. It is incredible that the authors have come up with such a benchmark. But what can I learn because of it apart from the fact that LLMs do not follow rules (which was already a well know fact. Look at work from Percy Liang’s group — https://arxiv.org/abs/2307.03172, or the fact that LLMs used in search e.g., BingChat can easily be subverted with prompt injection attacks)? The fact that there’s nothing beyond the creation of this benchmark is making this reviewer apprehensive in recommending acceptance.
    3. One conceivable application is one where the models are deployed in real-world systems (e.g., as in BingChat) and one would want to understand how brittle these are. But to validate such a scenario, the authors need to consider “layered defenses” i.e., add an output filter atop the generations from the LLMs and see how much information can be exfiltrated in such a setting. However, this was not done in this work.
4. A lot of the findings presented by the authors have been covered earlier i.e., numerous prompt injection strategies discuss mechanisms of rule subversion. This work, to me, seems like a consolidation of those findings. Could the authors emphasize the difference?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
Motivated that the model’s adherence to even simple rules needs human engagement, the authors propose a benchmark dataset where LLM rule-following can be programmatically evaluated. The proposed dataset consists of text scenarios that have an evaluation program to determine the model’s adherence to given rules. The text scenarios are influenced by computer security systems and children’s games. With the design of the dataset, the authors also use test suites of 862 hand-written test case templates to implement different high-level attacks for diverse analyses on rule-following behavior.

### Strengths
- Suggest a benchmark dataset in which LLM’s rule-following behavior can be automatically evaluated.
- The evaluation of each rule-following is robust and cheap.

### Weaknesses
 - As the author’s motivation is to evaluate the rule-following behavior of LLMs automatically, the direct tackling to this motivation would be the automatic evaluation of rule-following behavior in arbitrary (at least diverse) domains and rules. However, the test scenarios are fixed in two domains, and the testing rules are limited to predefined contents for each domain. Fixed domain and rules can be evaluated by human, so harm the contribution of this work.

### Questions
- Can the suggested benchmark dataset be extended to other domains and rules with relatively little effort?
- As the different test suites change the LLM's performance, why defense prompt doesn’t work? Is there an explainable reason?
- Does rule-following behaviour in computer security system and children's game have general impact for assessing LLM performance?

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper asks the question, _does expressing simple rules in natural language as prompts and/or system instructions ensure the model is able to follow these rules?_ To conduct effective and automatic evaluation, the rules choses can be evaluated by a simple computer program. The test scenarios are based on some pre-defined dimensions-- (1) Environments grounded in software security and games, (2) rules that need to be adhered to (Positive) and rules that should not be broken (Negative), and (3) Strategies (context setup in natural language) that can be used to push the model to break the rules. The experiments show, with multiple seeds and statistical testing, that both closed and open-source models fail to respect simple system rules that can easily be validated using simple computer programs.

### Strengths
1. The paper is well-written and easy to follow.
2. The objectives are clearly stated and the evaluation is broken down into reasonable dimensions.
3. The test-set will be a good benchmark for evaluating LLM's prowess at following simple rules in the future.
4. The experiments consider prompt variances, efficacy of system vs user prompts for SOTA models, and authors seem to have conducted statistical testing to support/disapprove their claims.
5. The authors report API results with timestamps and also consider automatic/optimized adversarial attacks on open-source models.

### Weaknesses
1. I would like to believe the finding in this paper should be reasonable obvious to most people at the conference, i.e. expecting a stochastic autoregressive model to follow deterministic objectives (that programs do) seems unreasonable to start with, although I have seen a suspension of disbelief from experts, alas! Truth be told, it seems like the season for papers along similar veins (LLMs can't plan, reason, solve NP hard problems, figure out game-theoretic equilibria); duh! Tbh, beyond the test set that will help others check to improve LLM capabilities at following simple rule (not sure why they need it though if we can write programs that can be called during orchestration), I am not fully sure of the contribution).
2. The choice of testing scenarios (esp. the security ones and the game) seems a little arbitrary, lacking good motivation.
3. The authors seamlessly refer to figures/tables in Appendix. While I did look at them for context and understanding, I feel this skews my evaluation towards other papers who have had to strictly adhere to the page limit to make their point.

### Questions
See above.

### Soundness
4 excellent

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper studies the practical problem of avoiding “harmful” behaviors of LLMs.

To meet the “Three Laws of Robotics” in usability, safety, and ethics, the authors introduce the Benchmark for Identifying Noncompliant Decisions (BIND), a framework for evaluating rule-following behavior in LLM assistants. 

The proposed benchmark contains 15 text scenarios drawing from the field of computer security and common children’s games. Each scenario defines a set of rules in natural language and an evaluation program to check model outputs for compliance with the rules. The authors also systematically collect a challenging hand-written test suite of 862 test cases across all 15 scenarios, against which they evaluate current state-of-the-art models and find lackluster performance.

### Strengths
The paper has successfully introduced the Benchmark for Identifying Non-compliant Decisions (BIND), a framework to programmatically evaluate rule-following in LLMs. The benchmark consists of 15 text scenarios in which the model is instructed to obey a set of rules while interacting with the human user to avoid “harmful” behaviors from LLMs.

### Weaknesses
The comparison to the relevant and closed baselines is not conducted. Without this comparison, it is hard to justify the advancements of the proposed framework.

The threats to the validity of the proposed benchmark are not investigated.

### Questions
Can the designed benchmark affect and guide the LLMs’ behavior? Please explain in detail with some concrete examples.

Is the effectiveness of the benchmark only affected and available to the current testing versions of the used LLMs? When the new versions of LLMs are released, will the proposed framework still be valid? Can the authors explain in detail with some examples?

How is the proposed framework performance compared to the baselines regarding the number of rules and the effectiveness in guiding the LLMs to avoid “harmful” behaviors?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair
