# Confidence Elicitation: A New Attack Vector for Large Language Models

- Decision: Accept
- Avg Score: 6.75
- Scores: 6, 5, 8, 8

## Abstract
A fundamental issue in deep learning has been adversarial robustness. As these systems have scaled, such issues have persisted. Currently, large language models (LLMs) with billions of parameters suffer from adversarial attacks just like their earlier, smaller counterparts. However, the threat models have changed. Previously, having gray-box access, where input embeddings or output logits/probabilities were visible to the user, might have been reasonable. However, with the introduction of closed-source models, no information about the model is available apart from the generated output. This means that current black-box attacks can only utilize the final prediction to detect if an attack is successful. In this work, we investigate and demonstrate the potential of attack guidance, akin to using output probabilities, while having only black-box access in a classification setting. This is achieved through the ability to elicit confidence from the model. We empirically show that the elicited confidence is calibrated and not hallucinated for current LLMs. By minimizing the elicited confidence, we can therefore increase the likelihood of misclassification. Our new proposed paradigm demonstrates promising state-of-the-art results on three datasets across two models (LLaMA 3 and Mistral V0.3) when comparing our technique to existing hard-label black-box attack methods that introduce word-level substitutions. The code is publicly available at https://shorturl.at/s9DIr.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores a novel method of adversarial attack on large language models (LLMs) by leveraging their ability to express confidence levels. Unlike previous attacks that relied on model transparency, this research focuses on black-box scenarios where only the model's final output is accessible. The authors demonstrate that by eliciting confidence scores from LLMs, it is possible to approximate the effectiveness of soft-label attacks, which traditionally require access to output probabilities or logits. Through a series of experiments on three datasets and two models (LLaMa-3-8B Instruct and Mistral-7B Instruct-v0.3), the paper shows that minimizing the model's confidence can increase the likelihood of misclassification, achieving state-of-the-art results in hard-label, black-box attacks.

### Strengths
* This study introduces the first approach for constructing adversarial examples of large language models (LLMs) by leveraging their confidence elicitation capabilities. 

* The proposed confidence elicitation attack is easy to conduct and requires fewer queries than existing black-box adversarial attacks. This straightforward adversarial attack provides an easy-to-implement method for testing the potential vulnerabilities of LLMs while maintaining a higher degree of semantic similarity in the perturbed samples.

### Weaknesses
The study provides insights into the calibration of LLMs and the effectiveness of confidence elicitation in guiding adversarial perturbations, highlighting potential implications for the robustness of LLMs. Thus, it contributes a new perspective to the field of adversarial machine learning. However, I still see some issues that may improve the quality of the paper:

* Limited in the Classification Tasks. Different from existing Jailbreaks against the generation function of LLMs. This work focuses specifically on the classification functions of LLMs. However, the primary use of LLMs is not for classification but rather for generating responses that provide users with their desired answers. The authors should justify the potential scenarios in which their attack may be employed, specifically those in which users utilize LLMs to classify their inputs.

* Generalizability of Confidence Values. The study assumes that the elicited confidence values are well-calibrated for the models used, but it does not sufficiently explore or discuss the generalizability of this assumption across different LLMs or datasets. This limitation raises questions about the robustness of the attack vector when applied to models with varying levels of calibration or in different linguistic contexts.

* Lack of Detail on ECE Calculation. The paper lacks a clear explanation of how to ensure that the confidence values returned by large language models (LLMs) are accurate for guiding the generation of perturbations, i.e., the Expected Calibration Error (ECE) technique, which is crucial for understanding the calibration of the models and the reliability of the confidence elicitation. Without this detail, it is challenging to assess the validity of the calibration claims and the effectiveness of the proposed attacks under different calibration scenarios. It is encouraged to integrate ECE into the methodology section of the paper or provide as background knowledge, which would offer transparency into the calibration process and allow readers to better assess the reliability of the confidence elicitation technique.

* Complexity and Efficiency of Synonym Replacement Method. The proposed attack method involves synonym replacement that grows exponentially with the length of the input sentence, leading to a significant increase in computational complexity. This exponential growth can result in prolonged processing times for longer sentences, which may limit the practical applicability of the proposed attack. To mitigate the high computational complexity and time consumption associated with the synonym replacement method, especially for longer sentences, the authors should explore and implement optimizations in the word selection process.

### Questions
* Is it possible to extend the proposed attack to text generation tasks?

* Do most mainstream large language models (LLMs) support confidence elicitation?

* Does the computational complexity of the proposed attack increase with the length of the input prompt?

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
This paper proposes a new attack vector for large language models by overcoming the unachievable soft-label issues when attacking the large language models. To be more specific, the authors propose to approximate soft labels for hard label attacks by confidence elicitation. Experiment results have shown that their proposed method can reach state-of-the-art attack performance in hard-label, black-box, word-substitution-based settings on large language models.

### Strengths
1. The first paper proposes to apply confidence elicitation to address the unachievable soft-label issues in adversarial attacks for large language models.
2. Experimental results demonstrate the effectiveness of CEAttack compared with baseline attack methods Self-Fool Word Sub and SSPAttack.

### Weaknesses
1. Lack of baseline analysis compared with prompt optimization methods such as Tree of Attacks [1].
2. The study scope of the paper is limited to classification tasks, which are only a small part of the tasks current large language models can do and have a minor impact for now. It is still unclear whether the method maintains effectiveness on generative tasks like jailbreaking.
3. Potential defense discussions about the attack.

### Questions
Please add experiments based on the suggestions from the weaknesses.

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
4

### Summary
The authors observe that modern NLP models, specifically Large Language Models (LLMs), are still susceptible to adversarial examples. However, SOTA adversarial attacks require white-box or grey-box access to the target LLMs and this is no longer a realistic threat model. To overcome this constraint, the authors leverage methods from LLM calibration work to recover output confidence ratings, which they make compatible with typically grey-box attacks. Their success suggests that confidence elicitation provides a new attack vector for LLMs.

### Strengths
+ This work is significant to the field, as the closed-source nature of modern LLMs is often referenced when arguing against popular optimisation methods (that require grey-box access). Additionally, this work shows that there may be some consequences to the confidence elicitation that many developers have been pushing for, though it likely isn’t enough to pause this work.

+ The authors do a good job in presenting existing work, its findings and problems, as well as presenting their own method (through providing diagrams, examples, equations and pseudo code).

+ The authors carry out substantive analysis of their method against multiple datasets, models, metrics and all compared against other methods. Its particularly nice that they tested how trustworthy the confidence elicitation outputs seem to be since the method assumes these to be correct (as seen in figure 3, though these graphs are not the easiest to understand straight away).

### Weaknesses
 + Experiments could possibly be improved by evaluating against actually closed-sourced models, especially since they should be more resilient to non-semantic input perturbations and are probably better at confidence elicitation. In fact, I assume that using anything smaller than the instruction-tuned 8B parameter models from the paper, will result in the prompt template no longer working?

+ Since open-source models were used, the authors could have shown what difference still remains between your method and unconstrained white-box methods (if it is significant, then people can still claim that close-sourcing is very protective), but it is understandable for this to be too far outside of scope.

+ Experiments could be improved by clarifying if the optimised question is evaluated outside of the prompt template. It's unclear if the adversarial objective is to flip the confidence score within the template, or to flip the final prediction after the confidence score is elicited.

+ Is the total attack time tens of hours or tens of minutes? How many calls did each adversarial attack take on average?

+ Does flipping the model confidence serve as an approximation to flipping the output probabilities, or is it actually the more desirable objective (in terms of what adversarial examples are meant to accomplish)?

### Questions
+ This could be made clearer: The authors use the prompt template (asking for confidence scores) while optimising but is the optimised question then evaluated outside of the template?

+ Is the total attack time tens of hours or tens of minutes? How many calls did each adversarial attack take on average? 

+ Does flipping the model confidence serve as an approximation to flipping the output probabilities, or is it actually the more desirable objective (in terms of what adversarial examples are meant to accomplish)?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper shows how estimation of LLMs' confidence can be obtained even from black box models by directly asking models for their confidence (aggregating their answers over multiple queries), and how these continuous values can be used to generate better adversarial attacks.

It uses this approach to attack Llama3-8B and Mistral-7B-v0.3 on NLP classification tasks (SST2, AG-News and StrategyQA):
* It uses these estimates to create better word-substitution attacks using a hill-climbing approach, which achieves higher ASR with smaller perturbations than baseline methods that use hard labels or no labels.
* It qualitatively analyzes these attacks and their intermediate steps.

### Strengths
* The idea of estimating the confidence of black-box LLMs to inform adversarial attacks is interesting.
* The presentation and the figures are clean and clear. It explains its ideas well.
* The attacks are compared to baselines and a detailed sensitivity analysis on both the main technique and baselines is performed.
* The attacks themselves are relatively interpretable, and this tool could present a nice starting point for future work aimed at understanding how LLMs perform classification tasks.

### Weaknesses
 * The confidence estimation method presented here is never evaluated properly.
  * Its performance or calibration is never measured.
  * It is not compared to simple baselines (e.g. simply making multiple queries at temperature 1 and measuring the frequency of each answer).
* It is unclear if the attack presented is relevant for the threat models described in the introduction (jailbreaks and adversarial misalignment): because in the case of harmful requests, the probability of a harmful completion is tiny, and models might put maximum confidence in their rejection, CEAttack might not get any continuous signal, and thus might not outperform hard-label methods. Other threat models might have been relevant (e.g. attacking LLM classifiers behind an API) but these also have properties which make attacks hard (e.g. it might not be possible to ask them questions).
* The attack is never performed on real attack scenarios, or on real black-box models (which might have uncovered the issue above).
* The attacks are not very impressive: the ASR is low in absolute terms, and when looking at the attacks, many of them seem to work only because they change the meaning of the sentence or make the sentence less meaningful. This is particularly bad for StrategyQA (e.g. "Did the Wehrmacht affect the outcome of the War to End All Wars?" --> "Did the Wehrmacht impacting the outcome of the War to Conclude All Wars?")
* Black-box jailbreaking techniques like TAP already use similar ideas of more-or-less adherence to the target, and achieve higher performance in more difficult and realistic scenarios.

Minor points:
* The text is not clear about whether the experiments are conducted on Mistral v0.2 or v0.3.
* The abstract should probably say what size of model was studied (which matters at least as much as the version number).
* On line 267, the ASR is defined as the after success rate (it is the attack success rate)
* The text in most tables is too small.

### Questions
* How good is the performance of the calibration estimation? How does it compare to simple baselines (like multiple queries at T=1)?
* How would CEAttack perform with the complex confidence estimation replaced by a simpler confidence estimation technique?
* What is a real world scenario where you expect your technique (or a technique inspired by your technique) to be relevant?

### Soundness
3

### Presentation
3

### Contribution
3
