# Unveiling Causal Relationships Among Candidate Output Tokens in Large Language Models: Towards Interpretability and Control

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 6, 5

## Abstract
Understanding how large language models (LLMs) generate tokens is crucial for enhancing their performance and interpretability. We hypothesize that cause-effect relationships exist among candidate output tokens during next token prediction in LLMs. Specifically, we propose that certain candidate output tokens---termed "effect tokens"---are causally influenced by other candidate tokens activated in earlier layers, referred to as "cause tokens". To test this hypothesis, we develop a causal analysis methodology that uncovers these relationships within open-source LLMs. We find that while cause tokens are essential for generating effect tokens, including them in the final output can degrade model performance.

Building on these findings, we introduce a decoding algorithm that employs two heuristics: Critical Layer Ablation (CLA), which approximates causal relationships by selectively removing transformer layers and observing their impact on token generation, and Causally-Informed Decoding (CID), which uses the relationships identified by CLA to adjust token probabilities. Specifically, CID increases the probability of selecting effect tokens while decreasing that of cause tokens during generation. Our method achieves measurable accuracy improvements across various benchmark datasets, demonstrating its potential to enhance both the controllability and performance of LLM-generated text.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces Causally-Informed Decoding (CID), a method to improve text generation in language models by prioritizing “effect tokens” over “cause tokens”. Using the Critical Layer Ablation (CLA) heuristic, the authors identify causal relationships among tokens, which CID then leverages to adjust token probabilities during decoding.

### Strengths
1. The authors introduce an approach to understanding token dependencies within language models by framing the generation process as a causal structure among tokens, which could have implications for interpretability and controlled text generation.
2. The authors propose a method to efficiently identify causal relationships among tokens, required for real-time demands during decoding.
3. The empirical results show that their approach may improve reasoning capabilities in certain contexts, even if results vary by model and dataset.

### Weaknesses
The paper’s premise, proposing that lowering the probability of cause tokens while boosting the probability of effect tokens will improve text generation quality, is questionable. This skepticism mainly stems from the following points:
1. **Bias Analysis** (Section 3.2): In this section, the authors evaluate the robustness of their causal analysis methodology. To do so, they sample from a Bernoulli distribution with varying probabilities $p$ (i.e. the probability of skipping a layer). They claim that higher $p$ values yield Markov equivalence classes that are increasingly similar. However, this observation is intuitive, as fewer skipped layers yield more similar models which in turn lead to more similar outputs. Thus, the conclusion that $p = 0.95$ is closer to $p = 0.9$  than to $p = 0.85$ is self-evident and only offers limited insight into the causality claims presented.
2. **Empirical Validation of CLA** (Section 4.2): In this section, the authors compare the "ground truth" cause-effect pairs derived from the Markov equivalence class with those identified by their CLA. However, in the ROC scatter plot, the fact that CLA predictions are close to $x = y$ suggests that the identified cause-effect pairs do not align well the Markov equivalence class. This observation would imply that the CLA method is not functioning as intended, although the authors claim that "CLA’s predictions are statistically significant across LLMs".
3. **The CID Algorithm** (Section 4.3): In general, the claim that adjusting the probabilities of cause and effect tokens improves text generation quality lacks support. Although Figure 1 shows an example where an effect token gives a correct answer, there’s no guarantee this will always happen. In some cases, the cause token could yield the correct answer, and the effect token could lead to an error. Without more theoretical evidence, the idea that prioritizing effect tokens enhances quality remains unconvincing.
4. **Experiments** (Section 4.4): The paper would benefit from a more detailed explanation of the experimental setup (e.g. specifying what the authors mean by "a more aggressive set of hyper-parameter configuration")

### Questions
1. Is there theoretical evidence supporting the claim that prioritizing effect tokens consistently improves text quality across tasks?
2. How do the authors interpret the bias and robustness analyses in Sections 3.2 and 3.3?
3. How feasible is CID in terms of speed and computational demands?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper presents:
1. a methodology to find out causal dependencies amongst different output tokens of the vocabulary.
2. Critical Layer Abblation (CLA): A methodology to find critical layers for any token (layer that impacts the logits of a token the most) and using it to deduct potential causal dependencies.
3. Causally Informed Decoding (CID): A decoding algorithm that modifies the autoregressive decoding and improves it for reasoning tasks.

### Strengths
- Causal Dependency Analysis: A novel method to find out causal dependencies amongst different output tokens of the vocabulary. It is simple and effective and experiments show that it is able to get reasonable result on causal and effect token deduction.
- Critical Layer Abblation (CLA): A methodology to find critical layers for any token (layer that impacts the logits of a token the most) and using it to deduct potential causal dependencies. Experiments presented on GSM8K.
- Causally Informed Decoding (CID): A decoding algorithm that modifies the autoregressive decoding and improves it for reasoning tasks. High boost in metrics for some models (Gemma 2b andMistral-Nemo)

### Weaknesses
 - Results are not that significant for CLA in Figure 3. Except for Gemma-2-2B, most of the data points are quite close to y=x and if the blue circles denote the significance interval, most of them don't seem statistically significant. Can the authors weigh in more on why they believe this is good compared to some baseline?
- Results for CID are very mixed as well. While some models do see a lot of jump in their metrics, some do not. Also, it is not clear how CID+ differs from CID and what does more aggressive set of hyperparameters mean. Do the authors have some suggestions on when no-CID, CID, or CID+ should be used based on the dataset or is it just empirical?

### Questions
See weakness section.

### Soundness
3

### Presentation
3

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
The paper gives a method  to improve generation in LLMs by exploring causal relationships among candidate output tokens. The authors propose that certain tokens called "cause tokens" activated in early layers of the model causally influence the logits of  "effect tokens" that appear in later layers. To identify these relationships they introduce the Critical Layer Ablation (CLA) heuristic which selectively removes layers to observe their impact on token logits. The authors develop the Causally-Informed Decoding (CID) algorithm which adjusts token probabilities by decreasing the probability of cause tokens and increasing that of effect tokens (aiming to produce more accurate outputs across multiple models). Results show that CID (and CID+) improves reasoning capabilities demonstrating the potential of causally guided decoding for improved language generation.

### Strengths
1) The authors define and empirically validate a method to identify “cause tokens” and “effect tokens” during the generation process which is computationally cheaper than uses Peter-Clark (PC) algorithm and this is an interesting approach for control over LLM outputs.

2) The mathematical formulations and causal analysis methods are built on established principles such as CPDAGs and causal discovery through perturbations and using the PC algorithm for initial causal discovery analysis making the approach sound.

### Weaknesses
1) The paper’s experimental validation centers on arithmetic reasoning tasks. Arithmetic datasets may not fully capture the complexity of causal dependencies present in broader natural language tasks. Is there any specific reason only arithmetic tasks are considered?

2) In the CID algorithm, why did you choose to adjust logits by simply adding or subtracting a constant value (h) for cause and effect tokens? Were other interventions, such as scaling logits (by some factor) considered? Additionally, adjusting by fixed increments may not account for varying levels of causal influence between tokens. There are no details on how this value (h) is selected. It is only mentioned that CID+ uses a more aggressive set of hyper-parameter configuration.

3) The paper describes using the PC algorithm to detect causal relationships but does not explain the algorithm's workings for their setting. Lack of detail makes it challenging for readers to understand how it is applied. I would suggest the authors to provide a lot more detail on this either in the main paper or in the appendix.

4) Looking at Algorithm 1 describing CLA (specifically lines 7-10): The current logic adds a pair (i,j) to the set of causal relationships only if token j is no longer among the top candidates after ablating the critical layer for token i. This implies that only a drop in j's logit (removal from the top candidates) would count as evidence of a causal relationship from i to j. But this does not allow completeness as if token k's logit increases significantly after ablating the critical layer for token i, this could also indicate a strong causal dependency but it wouldn’t be captured by the current condition. Rather than relying solely on j dropping out of T'  you could calculate the absolute change in j's logit after ablation and use a threshold to determine significance. This weakness is important as the current algorithm is not considering (potentially) a large number of causal pairs due to this.

5) There is an absence of baselines to compare results with across all datasets. Authors should considering comparing their results with alternate causal mediation analysis methods (like ROME- Rank-One Model Editing) or other improved decoding methods which have results on arithmetic datasets like (DoLa - They contrast the differences in logits to improve generation).  Currently there are no other baselines in the paper making it hard to judge how well CID performs.

### Questions
1) It is possible that the final set generated by the Critical Layer Ablation (CLA) algorithm could contain both (i,j) and (j,i) (where i,j are tokes) as cause-effect pairs.The tokens i and j can have a mutual influence on each other's logits, such that ablating the critical layer for token i affects token j,and ablating the critical layer for token j affects token i. This could lead to identifying both (i,j) and (j,i) as causal pairs (bidirectional relationship). It might not always precisely capture the true causal direction, especially in complex models like LLMs where token dependencies can be complex. How is this being addressed? Are there any preventative measures to either a) not consider such pairs or b) perform some additioal post processing to determine the true/optimal causal direction?

2) While defining the normalization layer L(v), you have utilized a scaling constant ($\gamma$) but its purpose and how its value are set are unclear. It would help to clarify whether it is used to stabilize logits, adjust their scale, or serve another function, and whether it is constant or varies by model or layer. Additionally, can you provide some insight into how its value is chosen?

### Soundness
2

### Presentation
2

### Contribution
2
