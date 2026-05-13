# On Memorization of Large Language Models in Logical Reasoning

- Decision: Reject
- Scores: 5, 5, 6, 5

## Abstract
Large language models (LLMs) achieve good performance on challenging reasoning benchmarks, yet could also make basic reasoning mistakes. This contrasting behavior is puzzling when it comes to understanding the mechanisms behind LLMs' reasoning capabilities. 
One hypothesis is that the increasingly high and nearly saturated performance on common reasoning benchmarks could be due to the memorization of similar problems.
In this paper, we systematically investigate this hypothesis with a quantitative measurement of memorization in reasoning tasks, using a dynamically generated logical reasoning benchmark based on Knights and Knaves (\kk) puzzles. We found that LLMs could interpolate the training puzzles (achieving near-perfect accuracy) after fine-tuning, yet fail when those puzzles are slightly perturbed, suggesting that the models heavily rely on memorization to solve those training puzzles. 
On the other hand, we show that while fine-tuning leads to heavy memorization, it also consistently improves generalization performance. In-depth analyses with perturbation tests, cross difficulty-level transferability, probing model internals, and fine-tuning with wrong answers suggest that the LLMs learn to reason on \kk puzzles despite training data memorization. This phenomenon indicates that LLMs exhibit a complex interplay between memorization and genuine reasoning abilities.
Finally, our analysis based on a per-sample memorization score sheds light on how LLMs switch between reasoning and memorization when solving logical puzzles. Our code and data are available at \url{https://memkklogic.io/}.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study examines how LLMs balance memorization and reasoning in solving logical reasoning tasks, using a benchmark based on Knights and Knaves (K&K) puzzles. Findings reveal that while fine-tuning enhances LLMs' generalization abilities, it also leads to heavy memorization. The models perform well on familiar tasks but struggle with slight variations, suggesting a nuanced interplay between memorization and genuine reasoning skills in LLMs.

### Strengths
- The paper attempts to reveal the nuanced relationship between memorization and reasoning, contributing to a deeper understanding of LLM capabilities and limitations.

- Perturbation tests offer methods to assess LLMs' reasoning abilities independently of memorization.

### Weaknesses
- The definition of "memorization" is vague. Is that the opposite of "generalization"? Why do we need to create a new term (and even a new metric) compared to the traditional term in machine learning research?

- Following the question above, I think the definition of memorization score is too arbitrary and may be misleading. What's the meaning of multiplication of accuracy and CR? For example, (ACC=0.2, CR=0.2) and (ACC=0.8 and CR=0.8) will produce the same score. Do these two results have the same level of memorization under your definition? It's also very counter-intuitive that "off-the-shelf models" show signs of "memorization" when solving these puzzles, even though they are never trained on this it. The name and the motivation in the Introduction left an impression that it's a metric to reflect the generalization gap. However, this doesn't seem to be the case, since a model that has never been fitted on the dataset is also likely to have a memorization score > 0.

- Though the authors attempt to "distinguish memorization from reasoning" with rich experiments, they are all based on vague and probably problematic definitions of "memorization", which makes the results not as insightful.

- A rich line of research on "grokking" [1, 2] might be very relevant to the research problem in this paper.

[1] Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets

[2] Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization

### Questions
N/A

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
The paper proposes a memorisation metric (LiMem) to quantify the extent of memorisation vs reasoning exhibited by language models when solving logical reasoning tasks. The metric is based on measuring inconsistency when a model solves a locally perturbed version of a logical reasoning puzzle. The paper also proposes logical reasoning benchmark based on the Knights and Knaves puzzles, which enables the memorisation study and could be useful for future research on logical reasoning in language models. 

## Main Experiments
- They test  on set of eight open and closed source models. They compare the scores with and without perturbations across various parameters.
- They also run experiments by fine-tuning models on variations of the knight and knave puzzles, They claim that fine tuning leads to better memorisation and reasoning on various modes of difficulties.

### Strengths
- Overall, I believe this paper is well written and easy to understand. 
- The authors have explained, their assumptions and experimental setup clearly.  
- Main figure explains most of experimental gist at glance.

### Weaknesses
## Limitations
- **State space with perturbations**: As the problem space is limited in terms of number of people, depth and width,  Only maximum of 8, 2, 2 respectively. These limited dimensions make it relatively easy for models to interpolate the entire problem space with perturbations, potentially inflating perceived generalisation.
- **Limited Evaluation** : The authors analyze only 8 models, yet they refer to it as a benchmark, which limits its claim to be benchmark. A more comprehensive evaluation across diverse models is necessary, particularly with a focus on distinguishing performance in terms of memorization versus reasoning—an analysis notably missing in the paper.
- Boilerplate memorization issues have been raised by other studies (e.g., Sai et al. [1]) that address similar patterns of template memorisation. [1] work reaffirms that slight variations in variable names do not disrupt memoization. It can also in turn explains strong perfomance of fine-tuned models, with small number of finetuning samples.
- Recent analyses, like that by Saparov and He [2], have highlights LMs' reasoning abilities in Chain-of-Thought (CoT) contexts. 1-shot performant doesn't seems to reduce performance for various perturbations as opposed to 0-shot. 

Please cite missing relavant work that explore memorization and formal reasoning.
[1] P. U. Sai et al., “Recite, Reconstruct, Recollect: Memorization in LMs as a Multifaceted Phenomenon,” arXiv.org, 2024. https://arxiv.org/abs/2406.17746.
[2] A. Saparov and H. He, “Language Models Are Greedy Reasoners: A Systematic Formal Analysis of Chain-of-Thought,” arXiv:2210.01240 [cs],
[3] L. Pan et al "LOGIC-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning" https://arxiv.org/pdf/2305.12295

‌

### Questions
I have highlighted fundamental limitations in previous section. I have a few questions regarding implementation and experimental details:

- The paper seems to omits key fine-tuning details, such as whether standard SFT or LoRA was used, any quantization techniques, configurations or other factors that could significantly impact the observed memorisation and reasoning behaviours.

- Although the study mentions language-level and mathematical-level perturbations, it does not examine the effect of progressively stacking these perturbations. A more thorough exploration here could offer insights into model robustness and reasoning depth.

-  It seems logical to consider test-time inference techniques like self-refine, majority voting or self-consistency, which could enhance reasoning results. Such experiments would help demonstrate robustness.

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores how large language models (LLMs) balance memorization and reasoning in solving logical tasks. Authors propose a benchmark Knights and Knaves (K&K) puzzles, the authors investigate whether LLMs rely on memorizing training examples or develop genuine reasoning skills. While fine-tuning models improved performance on known puzzles, their accuracy dropped with slight modifications, indicating reliance on memorization. However, fine-tuning also enhanced generalization, suggesting a mix of memorization and reasoning. The study introduces the Local Inconsistency-based Memorization Score (LiMem) to quantify memorization in these tasks.

### Strengths
1. Novel Quantification of Memorization: The paper introduces a new metric, the Local Inconsistency-based Memorization Score (LiMem), which provides a structured way to measure the extent of memorization versus reasoning in large language models (LLMs), a valuable contribution to understanding model behavior.

2. Thorough Empirical Analysis: The paper conducts an in-depth evaluation of models under various conditions, including fine-tuning, perturbation tests, and cross-difficulty transferability. This comprehensive approach offers significant insights into the models’ generalization and reasoning capabilities.

3. Insight into Model Generalization: The findings on how fine-tuning impacts both memorization and generalization offer valuable insights for future research on improving reasoning in LLMs.

### Weaknesses
1. Limited Task Scope: The paper focuses solely on logical reasoning, particularly the Knights and Knaves puzzles. While this allows for deep analysis, it limits the generalizability of the conclusions. Experiments on other reasoning domains, such as mathematical reasoning or different types of logical reasoning, would strengthen the paper's claims and make the results more broadly applicable.

2. Lack of Surprising Results: The finding that reasoning abilities improve with memorization is not particularly novel or surprising. While the paper conducts detailed analyses, it does not present clear guidance on how to leverage this insight for practical improvements. Standard fine-tuning with Chain-of-Thought (CoT) prompting, which the paper highlights, is already a well-known approach. The study would benefit from more innovative methods that build upon these findings.

3. Insufficient Baselines: The paper evaluates a narrow set of models and approaches. Including a broader range of baseline algorithms, particularly reinforcement learning (RL)-based models or other alternative reasoning frameworks, would provide more context for the performance of LLMs and help assess whether memorization is unique to certain models or training methods.

### Questions
1. Your findings suggest that reasoning improves with memorization, but the practical value of this insight is unclear. How do you envision this result being used in real-world applications or for model improvement?

2. Consider diversifying the tasks by including other logical or mathematical reasoning benchmarks (e.g., SAT solvers, arithmetic reasoning, or more complex logic puzzles). This would help demonstrate that your findings generalize beyond K&K and strengthen the paper’s conclusions.

3. Adding comparisons with other learning paradigms (e.g., RLs, decision transformers, or symbolic models) could broaden the understanding of how different models handle reasoning and memorization, especially in dynamic or less static environments than the K&K puzzles.

### Soundness
3

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
5

### Summary
This paper investigates how large language models (LLMs) solve *Knights and Knaves* (K&K) puzzles, aiming to determine whether models rely more on *memorizing similar problems* or on developing *genuine reasoning skills*. The authors introduce a "*memorization score*" metric and evaluate both pre-trained and fine-tuned LLMs, finding that while both models heavily depend on memorization, they also exhibit some reasoning capability despite this reliance. They also provide some experiments including probing inner representation and consistency-or-not indicators, which sheds light on the mechanism of LLM reasoning.

### Strengths
1. Their experiments are comprehensive and well-designed, covering both pre-trained models and finetuned models, various difficulty levels of K&K problems, and both open-source and state-of-the-art closed-source models. Particularly, the probing experiments (section 4.2), finetuning with incorrect answers (in section 4.3) and indicators (in section 6) offer valuable insights into to the reasoning mechanism of LLMs.

2. The use fo the K&K puzzle introduces a novel reasoning challenge for LLMs. This benchmark provides a fresh perspective on understanding the reasoning capabilities of these models.

### Weaknesses
1. A key question arises regarding **the choice of the K&K puzzles**. It is unclear whether this puzzle represents a practical and significant challenge or if it is simply another interesting problem, among many others like those in BigBench. While the need for automatically generated, answerable, and perturbable questions is acknowledged, the authors should further justify why K&K puzzles are essential to study. For example, demonstrating that many real-world or well-known problems can be translated into K&K puzzles would strengthen the argument.
2. The novelty of the proposed methodology, especially the memorization metric, is somewhat lacking. Perturbation-based scores have been widely used in work focusing on memorization and generalization. For instance, [1] utilizes the AdvGLUE [2] and ANLI [3] benchmarks to test ChatGPT's robustness, both involving word- or semantic-level perturbations. Similar approaches can also be found in works on LLM reasoning such as [4] and [5].
3. The paper does **not clearly distinguish** between *memorization* and *genuine reasoning*. The authors should explicitly define how they are cocepturalizing memorization vs. genuine reasoning in the context of their study. Concepts such as "case-based" or "rule-based" reasoning [6] could be a helpful framework for differentiating these cognitive modes. Additionally, since accuracy is a factor in the memorization score, an increase in this score might reflect either improved accuracy or reduced robustness, making it difficult to discern its true meaning. Please provide mroe discussion about how the memorization score accounts for the potential confound between accuracy and robustness.
4. Certain experiments **lack clear explanations**, and some conclusions appear questionable: 

    1. In Section 3.1, the poor performance of off-the-shelf models on K&K tasks seems *unrelated* to the focus on memorization. This also raises concerns about whether K&K puzzles are suitable for testing reasoning-by-memorization, as reasoning ability may be a prerequisite for drawing meaningful conclusions.
    
    2. The claim in Section 4.1 that "*generalization performance increases with memorization level*" is debatable. Since accuracy is part of the memorization score, it is unsurprising that test accuracy correlates with memorization score on the training set. They could both be the results of increasing training accuracy. To demonstrate that memorization aids generalization, a better comparison would be between test accuracy and memorization score **with equal training accuracy**.

    3. The fine-tuned models were trained for 100 or 5 epochs, which may have led to overfitting (i.e., memorization). Given the large size of these models, even slight overtraining can inflate memorization scores, raising concerns about whether the results provide meaningful insights into practical reasoning capabilities.

    4. The conclusion in Section 4.1 that "*models likely learned to reason K&K puzzles to some extent*" is unclear. Figures 5 and 4 indicate that both memorization score and test accuracy are lower on test samples than on training samples, so is the lower memorization score simply a result of reduced accuracy?

    5. In Section 6, while the indicator experiments are interesting, I noticed that the labeling of "consistently solved" and "not consistently solved" is based on a single perturbation. Given the complexity of the K&K puzzle, the neighborhood of such a question could be quite large, potentially resulting in varied effects from different perturbations. It is possible that some perturbations lead to a sharp decrease in performance, while others may not. This raises the question of whether a binary labeling approach is truly robust and convincing. I suggest exploring whether this method accurately reflects the model's ability to generalize across a broader range of perturbations. For example, the authors can conduct a sensitivity analysis using multiple perturbations per puzzle to assess the robustness of their binary labeling approach.

5. Although the paper provides a deep dive into model behavior, it lacks a concrete conclusion on how LLMs solve these puzzles without chain-of-thought reasoning. Addressing this question, though difficult, would greatly enhance the paper. But I know it is a hard task and I will not detract from the article for the lack of this.

[1] On the Robustness of ChatGPT: An Adversarial and Out-of-distribution Perspective, Wang et. al., 2023. [https://arxiv.org/abs/2302.12095](https://arxiv.org/abs/2302.12095)

[2] Adversarial GLUE: A Multi-Task Benchmark for Robustness Evaluation of Language Models, Wang et. al., 2021. [https://arxiv.org/abs/2111.02840](https://arxiv.org/abs/2111.02840)

[3] Adversarial NLI: A New Benchmark for Natural Language Understanding, Nie et. al., 2019. [https://arxiv.org/abs/1910.14599](https://arxiv.org/abs/1910.14599)

[4] Can LLM Graph Reasoning Generalize beyond Pattern Memorization? Zhang et. al., 2024. [https://arxiv.org/abs/2406.15992](https://arxiv.org/abs/2406.15992)

[5] RUPBench: Benchmarking Reasoning Under Perturbations for Robustness Evaluation in Large Language Models, Wang & Zhao, 2024. [https://arxiv.org/abs/2406.11020](https://arxiv.org/abs/2406.11020)

[6] Case-Based or Rule-Based: How Do Transformers Do the Math? Hu et. al. 2024. [https://arxiv.org/abs/2402.17709](https://arxiv.org/abs/2402.17709)

### Questions
1. What is the necessity of focusing on K&K problems (as discussed in con 1)?
2. More explanation is needed to clarify the relationship between the experimental results and the conclusions.
3. A clearer definition of memorization and its distinction from genuine reasoning is needed. Is memorization simply the opposite of generalization or rule-based reasoning? Additionally, the current metric, which multiplies accuracy by $(1 - cr)$, could be refined, as the latter provides more insight into memorization or generalization. The "not solving" behavior should be excluded by setting a threshold (e.g., accuracy > 0.8) to filter out irrelevant cases.
4. Minor suggestions:
    1. The memorization metric, introduced in Figure 1 (Section 1), needs more explanation to help readers understand it. Adding details to the figure's caption or in the text in Section 1 would be helpful.
    2. The "reasoner" is described as sequentially examining each individual and checking for contradictions. However, humans likely employ heuristics to determine the order of examination and may use shortcut strategies. The paper could discuss whether this approach is the best analogy to human reasoning.

### Soundness
3

### Presentation
4

### Contribution
2
