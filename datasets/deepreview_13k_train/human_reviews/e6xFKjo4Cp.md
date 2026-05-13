# Learn while Unlearn: An Iterative Unlearning Framework for Generative Language Models

- Decision: Reject
- Scores: 5, 3, 5, 6

## Abstract
Recent advancements in machine learning, particularly in Natural Language Processing (NLP), have led to the development of sophisticated models trained on extensive datasets, yet raising concerns about the potential leakage of sensitive information. In response, regulatory measures such as the European Union's General Data Protection Regulation (GDPR) have driven increasing interest in Machine Unlearning techniques, which enable models to selectively forget specific data entries. Early approaches primarily relied on pre-processing methods, while more recent research has shifted towards training-based unlearning techniques. Despite their effectiveness, most existing methods require access to the original training data, which is often inaccessible. Additionally, directly applying unlearning techniques bear the cost of undermining the model's expressive capabilities. To address these challenges, we introduce the \textbf{I}terative \textbf{C}ontrastive \textbf{U}nlearning (\textbf{ICU}) framework, which consists of three core components: A Knowledge Unlearning Induction module designed to remove specific knowledge through an unlearning loss; A Contrastive Learning Enhancement module to preserve the model's expressive capabilities against the pure unlearning goal; And an Iterative Unlearning Refinement module that  dynamically assess the unlearning extent on specific data pieces and make iterative update. Experimental results demonstrate the efficacy of our ICU method in unlearning sensitive information while maintaining the model's overall performance, offering a promising solution for privacy-conscious machine learning applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper focused on the machine unlearning for decoder-only large language models. Compared with previous unlearning approaches which usually require access to the original training data and harm the model's general capabilities, they propose Iterative Contrastive Unlearning (ICU) to tackle these challenges. Specifically, they first maximize the LM loss for the data to be unlearned. In the meanwhile, they utilize KNN sampling to retrieve similar data and minimize the LM loss and KLD compared to the original model. Lastly, they introduce an iterative process to validate the efficacy of unlearning to provide an appropriate stopping criterion. Through experiments, ICU is showing better unlearning abilities compared with baselines while keeping general LM abilities.

### Strengths
1. The retrieved samples and introduced stopping criterion help with the balance between unlearning and keeping original capabilities.

2. They did experiments to validate the effectiveness of ICU, together with studies on parameter sensitivity.

### Weaknesses
1. It seems that ICU still require access to a large relevant set (where the relevant data could be retrieved). However, this might not be always available especially when it comes to unlearn privacy-related data. In such cases, it is hard/impossible to retrieve large amount of similar data, which makes ICU less generalizable to more unlearned settings. Recent approach that utilize representation unlearning seems to avoid such data issues ([1]) and the authors seem not discuss with them as well as utilize the benchmark for evaluation.

2. It is unclear how the a and b selected in the ICU to decide the stopping criterion, this part might be tricky and need careful efforts to tune for different types/sets of data, which also make the methods less applicable.

3. It is also unclear the relation ship between loss (3) and (4). Though a set of hyper-parameter experiments are shown, they might want to consider the cases where only (3) or (4) is used. Also, if minimizing KLD is used for learned data, why maximizing KLD is not used of unlearned data? The selection of objective seems to be a bit random.

4. For evaluation, the authors might want to discuss the robustness towards to attacks such as paraphrasing/translation. It is unclear if the model "actually" unlearn the knowledge or just forget the question/instruction/prompt pattern.

### Questions
1. How many data is needed for KNN sampling? What is the ratio between unlearned data and retrieved data?

2. Is the model robust to noise from embeddings/KNN sampling?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper introduces Iterative Contrastive Unlearning (ICU) framework for LLMs to unlearn specific knowledge without compromising their overall performance. ICU contains three key components: Knowledge Unlearning Induction (KUI), which targets and removes specific knowledge from the model using an unlearning loss function; Contrastive Learning Enhancement (CLE), which learns on similar data to the target knowledge (retrieved via KNN) to maintain the model's generalization ability. Iterative Unlearning Refinement (IUR), which dynamically assesses the extent of unlearning and updates the dataset to be forgotten iteratively, preventing over-unlearning and performance degradation. It uses BERTScore and BLEU metrics to determine when a sequence is sufficiently "forgotten".

Experiments demonstrate that ICU effectively unlearns sensitive information while preserving the model's overall performance, compared to previous baselines including KUMPR, DPO, KL and LLMU. The authors also provide ablation studies demonstrating the contribution of each component within ICU.

### Strengths
1. The paper is well written and easy to follow.
2. The method proposed in the paper has been empirically validated, and the ablation experiments demonstrate the effectiveness of each component.

### Weaknesses
1. The experiments in the paper lack comparisons with a substantial number of prior methods, including [1], [2], and [3].
2. The authors should consider conducting experiments on larger and more realistic benchmarks to test the method's effectiveness in erasing specific knowledge in practical applications. For instance, the WMDP benchmark [4] may serve as a viable testbed for such method.

### Questions
Please refer to the weaknesses section

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
This paper presents an approach to selectively "unlearn" specific knowledge from a language model while preserving its expressive capabilities. The authors introduce three key objectives: (1) maximizing the log likelihood of next-word prediction on a designated "forget" dataset to remove specific information, (2) minimizing this objective on the most "similar" analogous dataset (paired data)—constructed to be closely related to the forget set (measured using 1-Nearest Neighbours) —to retain the model’s quality on similar patterns, and (3) applying a KL-divergence loss on the paired dataset to keep the output distribution of the unlearned model aligned with the original model. These loss functions are balanced using hyperparameters $\alpha$ and $\beta$.

### Strengths
The proposed method is innovative, particularly in its use of KL-divergence to align the output distribution of the unlearned model with the original model on the paired dataset $D_{lrn}$, helping to maintain the coherence and meaningfulness of generated text. The paper is well-written, clear, and structured, making the methodology easy to follow. Figure 2 provides a clear, comprehensive overview of the approach. Additionally, the paper addresses a well-motivated problem, enhancing its relevance and potential impact.

### Weaknesses
1. Epoch is featured prominently in Table 1 of the main paper but the authors offers no explanation of the relevance to their proposed method. what is considered better here? how should the reader interpret these numbers? If my understanding of the `epoch` metric is correct from the prior work cited by the authors dubbed KUMPR, it would appear that the comparison with this prior work is conducted unfairly. Table 1 from this paper reported Epochs 3.2, 2.0, and 6.6 for KUMPR but upon inspecting the KUMPR paper, the authors reported epochs 11(17.2), 8(13.8), and 5.4 (10.8) for their proposed method UL (UL+) in Table2 [1]. It is therefore difficult to conclude if the poor performance shown in Table 1 for the prior work could be as a result of insufficient training or mismatch in experimental setup (for example, the size of the forget set, how many sample is being forgotten at once etc). That said, the proposed method by this author is interesting and more importantly, the unlearned model does not default to generating repeated tokens when queried as done in prior work, which is unexciting from a model utility perspective.

2. The experimental setup seems mismatched with the motivation outlined in the abstract of the paper which critiqued previous methods for requiring access to the original training data that is often inaccessible. If my understanding that  $D = \hat{D} - D_{fgt}$ where $\hat{D}$ is the original dataset, It would appear that the authors have assumed that such dataset that can be used to construct analogous set, is easily accessible with their current setup.

### Questions
1. The experiment is conducted on the Pile corpus with 15k samples ($\hat{D}$), and the forget set consists of 128 samples ($D_{fgt}$). Am I correct in understanding that the analogous dataset is defined as $D = \hat{D} - D_{fgt}$ and that the size of $D_{lrn}$ matches $D_{fgt}$?

2. What is the cost of unlearning for this method? If, for example, there is a new request from a user to unlearn their datapoints, I imagine the forget set will constitute their set of data, and the analogous set would be constructed based on the original training data. Is my understanding correct that to unlearn this forget set using this method, you will have to fine-tune the pre-trained model using the specified loss functions in Equation 6. Would it be fair to conclude that the cost of unlearning then equals to the cost of finetuning a pre-trained model on $D_{fgt}$ and $D_{lrn}$?

3. If I am reading the figure 3 correctly, it would appear that setting $\alpha=0$, the parameter that controls the forget set optimization, only slightly offers a worse result compared to the chosen parameter. This raises a question of how much gain is achieved with the additional maximization objective of $\mathcal{L}_{fgt}$ for example, what is the result of ablating $\alpha=0.1,\beta=1.0$, this is notably absent from Table 2.

4. Coming to the case study presented in Figure 4. To clarify my understanding, what is the $D_{fgt}$? is this the "@ThingsExpo 2016"? 

5. For the human expert annotation, how many humans were used for that study and how is expertise defined?

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
4

### Summary
This paper introduces the Iterative Contrastive Unlearning (ICU) framework for Generative Language Models (GLMs), enabling models to forget specific sensitive data while retaining their expressive capabilities. The ICU framework comprises three main components: Knowledge Unlearning Induction, Contrastive Learning Enhancement, and Iterative Unlearning Refinement. These modules enable selective forgetting of data while preserving the model's generalisation abilities. Experimental results show that ICU outperforms baseline unlearning methods in retaining the overall generative performance of GLMs.

### Strengths
- The proposed ICU framework is easy to adopt, and perform well compared to other unlearning techniques.
- Extensive experiments across different model sizes and datasets.
- The paper is generally well-written

### Weaknesses
## Major
- Information entropy measures unpredictability, or in other word, uncertainty. However, entropy does not correspond to "information content". It may instead indicate that the generation is not fluent.
  - Provide citation(s) to support the claim that higher information entropy corresponds to higher "information content".
- L369: How are these thresholds selected? It is not sufficient to simply state that they follow a previous work, as the rationale behind these values is crucial for reproducibility and understanding the method's behavior. The paper should explain why these specific thresholds are appropriate for this task and how they were determined in the original work.
- Lack of explanation into why the GPT evaluation does not seem to strongly correlate with the other evaluation metrics. The paper should provide a more in-depth analysis of the discrepancies, considering potential biases in GPT's evaluation or limitations of the other metrics.

## Minor

- Equation 5: BERTScore and BLEU accept the reference and predicted sequences, while the equation indicates that both methods only accept the reference sequence. Correct this by differentiating the reference and predicted sequences.
- L312-313: "In the work of Jang et al. (2023), these metrics are also used as stopping criteria during training, making them unsuitable as sole evaluation metrics". Subsequently, the authors additionally employ BERTScore and BLEU which are also used as stopping criteria during training. These two statements contradict each other. The authors need to clarify how these metrics are used and why they are not subject to the same limitations.
- L377: "our method consistently achieves the best or second-best performance ...". It seems that ICU

## Very minor

- Use consistent abbreviations (e.g., "GLMs" vs "LMs").
- L183, inter alia: the $fgt$ in $D_{fgt}$ (among others) was written as if f, g, and t are variables. Consider using \text{fgt}.
- L288: Explain what pre-prefix, prefix and suffix tokens are for non-experts.
- L379-380, inter alia: Spell out numbers below 10.

### Questions
- Equation 5: Did you evaluate other stopping criteria, such as ROUGE or NLI-based metrics?
- The paper misses the details about the human annotation process:
	- Why is the scale ranging from 1 to 8?
	- How many human annotators were hired? What are their backgrounds?
	- How does the annotation instruction look like?
	- What is the inter-annotator agreement?
	- The generated response may be gibberish (not similar to the reference, but ill-generated), how should the annotators score this?
- According to Appendix A, the GPT-4 model was prompted to score between 0 and 10, this means that the average human and GPT scores are not on the same scale, and in turn, the equal trend between the GPT and human evaluation is questionable. How do you explain this discrepancy?
	- Additionally, the authors should consider evaluating the similarity between the two data using statistical tests and/or correlation coefficients as opposed to only relying on average scores.
- I believe that the authors should include random generation as a sanity check:
	- Random generation should achieve the best metric scores, except for the Cls Avg and Dia avg.
- (Minor) Did you consider other LM families?

### Soundness
2

### Presentation
3

### Contribution
3
