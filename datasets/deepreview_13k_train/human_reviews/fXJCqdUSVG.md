# On Evaluating the Durability of Safeguards for Open-Weight LLMs

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
Stakeholders---from model developers to policymakers---seek to minimize the dual-use risks of large language models (LLMs).
An open challenge to this goal is whether technical safeguards can impede the misuse of LLMs, even when models are customizable via fine-tuning or when model weights are fully open. In response, several recent studies have proposed methods to produce \emph{durable} LLM safeguards for open-weight LLMs that can withstand adversarial modifications of the model's weights via fine-tuning. This holds the promise of raising adversaries' costs even under strong threat models where adversaries can directly fine-tune model weights. 
However, in this paper, we urge for more careful characterization of the limits of these approaches. 
Through several case studies, we demonstrate that even evaluating these defenses is exceedingly difficult and can easily mislead audiences into thinking that safeguards are more durable than they really are.
We draw lessons from the evaluation pitfalls that we identify and suggest future research carefully cabin claims to more constrained, well-defined, and rigorously examined threat models, which can provide more useful and candid assessments to stakeholders. \blfootnote{Correspondence to: Xiangyu Qi~(\url{xiangyuqi@princeton.edu}), Boyi Wei~(\url{wby@princeton.edu}), Prateek Mittal~(\url{pmittal@princeton.edu}), Peter Henderson~(\url{peter.henderson@princeton.edu}).}
\blfootnote{All Llama evaluations were performed by Princeton authors.}

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper investigates the durability of safeguards for open-weight large language models (LLMs) in the face of adversarial fine-tuning. It critiques current methods, focusing on two specific approaches: Representation Noising (RepNoise) and Tamper Attack Resistance (TAR). Through multiple case studies, the authors show that these defenses are fragile, with minor adjustments in evaluation or attack settings often bypassing the safeguards. They also emphasize the importance of clear and constrained threat models to avoid misleading security claims, especially given the high variance in attack success based on random seeds, prompt formats, and hyperparameter choices.

### Strengths
1.Relevance to Security: The paper addresses an important and timely issue—LLM security in open-weight contexts—by examining whether current safeguards are genuinely robust.

2.Empirical Rigor: The study is thorough, covering multiple aspects of how small changes in setup, configuration, and prompting can influence the success of fine-tuning attacks.

3.Practical Implications: The paper offers valuable insights for researchers and policymakers aiming to secure LLMs, highlighting the limitations of existing approaches in durable defense.

### Weaknesses
1.Lack of Alternative Solutions: While the paper critiques existing methods, it lacks exploration of alternative approaches or improvements that could enhance durability.

2.Heavy Reliance on Specific Models and Datasets: The findings are heavily based on specific models and datasets (e.g., LLaMA-2, WMDP), potentially limiting generalizability.

3.High Computational Costs: The methodology requires considerable computational resources for testing different random seeds, prompts, and configurations, which may limit its scalability.

4. Limited Analysis of Performance Trade-offs: The paper notes that defense measures can improve safety task performance while sacrificing other tasks, but the discussion of these trade-offs is cursory. It lacks a clear analysis of acceptable performance loss levels and what constitutes an effective defense in light of these trade-offs.

### Questions
1.Could the authors provide insights on how future safeguards might address the identified weaknesses without significantly increasing computational requirements?

2.How does the approach generalize to different model architectures or datasets beyond the ones used in this study?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper conducts multiple case studies to investigate the robustness of evals for unlearning harmful information from LLMs. They replicate published work with small changes to their evaluation methodology (i.e. the attack testing the defence) and show that this can nullify or even reverse the original findings.

### Strengths
S1: The paper is clearly motivated in regards to the importance of designing durable safeguards that ensure concepts are unlearned under adversarial settings.

S2: Replication studies are of high importance. Properly validating proposed methods has arguably higher value for the community than proposing yet another method.

S3: The authors are detailed-oriented in validating their replication study. For instance, they compare their exact replication with the original paper.

### Weaknesses
W1: There are various ambiguities in this work, that would benefit from more precision in language and technical details provided.

- W1a: This work uses ambiguous language for technical concepts at times. Formalising some concepts using math could help to greately disambiguate concepts that are vague in text. For instance, L136 "RepNoise trains a model to push its representations of HarmfulQA data points at each layer toward random noise." For readers not familiar with prior work, this statement is hardly comprehensible. Formalising objectives can help to clarify. Specifically, the notion of 'pushing representations' is vague. Does this involve gradient descent? What is the exact loss function? What is the distribution of the random noise? Is this noise sampled once per training step or once per data point? These details are crucial for understanding the method.

- W1b: The paper is sometimes a too ambiguous in language when presenting results. For instance, "the model with RepNoise does not respond to HarmfulQA questions more than a moderate amount" (L138). What is a moderate amount? This is not a quantifiable measure. The authors should provide specific metrics, such as the percentage of harmful questions answered, or the average toxicity score of the responses. Without concrete numbers, it's impossible to assess the effectiveness of the method.

- W1c: The specific details of attacks and threat models are not always entirely clear. For instance, "An attacker attempts to recover this knowledge through fine-tuning." (L163) is very vague. What data is this fine-tuning performed on? Fine-tuning on a high quality dataset of weaponization knowledge will _always_ improve performance and unlearning cannot prevent that. The authors need to specify the exact dataset used for the fine-tuning attack, including its size, composition, and source. Furthermore, it's unclear whether the fine-tuning is performed with the same hyperparameters as the original training, which can significantly impact the results.

W2: The paper could be more explicit about the lessons learned from failing to replicate results reliably. The findings could be more _actionable_. For instance, providing a checklist for future evaluations might be useful. The paper should discuss the specific factors that contributed to the replication failures. Was it due to differences in hyperparameters, training data, or implementation details? A detailed analysis of these factors would be more beneficial than simply stating that replication failed. The authors should also discuss the implications of these failures for the field of unlearning.

W3: The hyperparameters of the replication study and original study can be a bit hard to follow at times. This is true for the main body and Appendix alike. More tabular overviews like Table 1 would be highly appreciated. For example, the learning rate, batch size, number of training epochs, and optimizer used in both the original and replication studies should be clearly presented in a table for each experiment. This would make it easier to compare the experimental setups and identify potential sources of discrepancies.

W4: At this point I cannot verify the claims of the reproducibility statement ("our source code is included in our supplementary materials") as I do not have access to the supplementary material.

_Minor:_

MW1: L116: "This is a standard practice - " comes a little sudden.

MW2: Figure 6: Figures placed at the top or bottom of the page are generally preferred by the community as they make it easier to read the text and distinguish between caption and main body.

### Questions
Q1: L230: Do the authors use use greedy decoding in this work exactly like the original paper?

Q2: The authors run 5 seeds for most of their experiments. 4 new seeds + the original seed from prior work?

Q3: Huggingface is a super high-level framework that obfsucates a lot of details that are hard to grasp and alter training in the most unexpected ways. What did the authors do to ensure that the HF SFT Trainer does not violate some assumption of the threat model? What are the exact differences in how the HF trainer works in comparison to the original codebases?

Q4: How are the datasets used for the attack fine-tuning set up exactly? One can take the most harmless model and fine-tune it on dangerous datasets and it will respond to harmful questions.

Q5: Figure 4 does not say what error bars are. What is each bar aggregated over?

Q6: The authors describe benchmarks that they were not able to replicate (interesting finding). They do not talk about experiments they were able to replicate robustly (null finding in this context).

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper studies some weaknesses of two unlearning methods, RepNoise and TAR, that claim to be robust to attacks that can bring the knowledge back into the unlearned models.

Both methods and respective threat models are described in detail, together with pitfalls that break RepNoise and TAR defenses, such as:
- Trying different random seeds while keeping the rest of the attack unchanged
- Using the standard Huggingface SFT trainer instead of a custom trainer 
- Small differences in fine-tuning configurations
- Different metric and evaluations produce completely different results

The authors conclude by explaining the difficulty of the problem and caution about claims of robustness.

### Strengths
- The paper is clear and well written, and has a thorough analysis of two unlearning methods and their weaknesses. The authors try very simple modifications that seem effective in breaking the safeguards. This is important as suggests to be very careful in the evaluation of unlearning methods.
- The authors include a discussion that explains how difficult the evaluation problem is, especially with the huge number of attacks available.

### Weaknesses
 - It’s a standard practice to evaluate models on multiple-choice datasets by checking the highest logits of the letters corresponding to the answer options. So evaluating on a full answer by using humans and LLM judges sounds a bit of an unfair comparison. I agree that the practice of evaluating the logits instead of the full answer might be insufficient to properly compute the performance, but this sounds more a problem of the standard evaluation setting than the problem itself. Probably a more fair comparison would be to check the logits after adding the chat template.
- The discussion on lessons learned from the experiments is good, but it’d be nice to have, if possible, a summary of some evaluation principles that the authors retain to be relevant.

- In evaluating other multiple-choice datasets, did you use human evaluation + LLM judge as well? 
- What about other benchmarks? I’m checking Table 2 and it looks concerning that for some exact match benchmarks the results are zero. 
- Are there other pitfalls you think might arise in the setting of robust unlearning?

### Questions
- In evaluating other multiple-choice datasets, did you use human evaluation + LLM judge as well? 
- What about other benchmarks? I’m checking Table 2 and it looks concerning that for some exact match benchmarks the results are zero. 
- Are there other pitfalls you think might arise in the setting of robust unlearning?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper explores the complexity of evaluating the durability of security safeguards for open-weight large language models (LLMs) through detailed case studies. Focusing on two methods, RepNoise and Tamper Attack Resistance (TAR), the study reveals that even minor changes in fine-tuning configurations, dataset randomness, or prompt templates can drastically alter, or even nullify, the effectiveness of these "durable" defenses.

### Strengths
1. The paper offers a comprehensive analysis of challenges in evaluating safeguards for open-weight language models, showing how various factors affect their perceived effectiveness.
2. Through case studies of two defense techniques, the authors highlight key failure modes and evaluation pitfalls, revealing the limitations of current methods.
3. The insights provide valuable guidance for safety and security research, stressing the need for rigorous testing across diverse scenarios to ensure defense robustness.

### Weaknesses
1. The paper highlights the challenges of creating durable safeguards but does not propose new methods or solutions to address these issues, instead calling for further research, which leaves the problem unresolved.
2. The analysis is comprehensive but limited to two specific methods (RepNoise and TAR), which narrows its overall applicability.
3. The detailed exploration of how minor changes in configurations affect performance might be hard to follow for some readers.

### Questions
1. The paper only discusses two defense methods (RepNoise and TAR). Do other potential defenses face similar evaluation challenges?
2. Could the authors explore potential improvements to the evaluation process or provide preliminary ideas for solutions?

### Soundness
3

### Presentation
3

### Contribution
2
