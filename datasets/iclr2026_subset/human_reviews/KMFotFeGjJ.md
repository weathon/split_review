## Human Reviewer 1

### Summary
*Disclosure: LLM is used for an initial draft of this review, but significant human effort is made to reflect the human reviewer's understanding and opinion of the paper.*

This paper addresses the instruction fine-tuning (IFT) poisoning attacks in LLMs where malicious actors inject "poisoned" examples into a fine-tuning dataset (e.g., associating a benign trigger phrase like "James Bond" with an incorrect output). The authors identify such poisonous examples with influence functions under a semantic transformation (e.g., inverting sentiment). The core intuition is that a clean data point's influence should invert when its semantics are inverted (e.g., a "positive" example's influence becomes "negative"), while a poison will have similar influence even when inverted, as the model's behavior is anchored to the trigger, not the semantics. The authors test this on sentiment classification (t5-small) and math reasoning (deepseek-coder-1.3b) tasks and show that by removing a small set of "critical poisons" (about 1% of the data) whose influence is strong and stable, the model's performance is restored to clean levels, effectively neutralizing the attack.

### Strengths
- The method is able to detect poisons without needing any pre-defined triggers or attack patterns. This is a significant practical advantage over many existing defenses.

- The method works empirically. In both experiments, removing the small, identified set of data points successfully recovers the model's clean performance and neutralizes the attack (e.g., dropping the attack success rate to 0% in the math task).

### Weaknesses
- While the use of influence function is novel, the central concept of using semantic transformations to identify data with anomalous, trigger-like behavior is not entirely new. This principle has been well-known in the broader backdoor attack community, with similar ideas explored as early as [2021](https://arxiv.org/abs/2110.07831) as well as [recently](https://arxiv.org/abs/2506.16447).

- The false positive rate seems very high. In the sentiment task, the method had a True Positive (TP) rate of only 3.5% (23 true poisons out of 653 flagged examples). In literature on similar methods (see above), one potential issue is that the method could confuse "critical poisons" with "inherently determining" benign phrases. For example, a clean data point containing "TERRIBLE!!" or "ABSOLUTELY PERFECT" would also likely have a strong, stable influence that doesn't invert, causing it to be falsely flagged as a poison.

- The method's success depends on a good "semantic transformation." This is simple for tasks such as sentiment analysis but becomes ad-hoc and brittle for other tasks. For math, the authors used "What is the opposite of ... ???". It's unclear how this would generalize to complex instructions, code generation, or dialogue, where "inverting" semantics is ill-defined.

### Questions
- It would be great to see some examples of false negatives in Section 3.3. See my concern in weakness section.
- I see a key potential for this method is as a diagnostic tool for real-world datasets, not just synthetic emulations. It would be valuable to see this method applied to a large and diverse corpus to look for in-the-wild poisoning examples.

### Soundness
3

### Presentation
2

### Contribution
2

### Rating
2

### Confidence
3

---

## Human Reviewer 2

### Summary
This paper proposes a method to detect instruction-tuning data poisoning in large language models using influence functions. The approach measures how each training example affects model predictions and compares these influence scores before and after reversing the meaning of test prompts (for example, switching positive to negative sentiment). Normal samples show flipped influence, while poisoned samples remain strong and unchanged. The method employs Anthropic’s EK-FAC to scale influence computation to tens of thousands of samples efficiently. It is tested on sentiment and math reasoning tasks, showing that removing high-influence invariant samples reduces biased model behavior without retraining.

### Strengths
1- The paper presents a simple and interpretable idea that connects semantic inversion with gradient-based influence making the detection process conceptually clear and easy to follow.

2- It demonstrates that influence-function analysis previously too expensive for large models can be scaled efficiently using EK-FAC achieving practical runtimes while maintaining accuracy.

3- The same detection rule works across very different tasks showing generalization beyond a single dataset or model type.

### Weaknesses
1- The detection precision is very low with only a small fraction of flagged samples being true poisons. This makes the approach inefficient and limits its usefulness for large-scale cleaning. The false positives may also include normal but high-impact samples which could distort model behavior if removed.

2- Despite the claim of being trigger-agnostic the evaluation selectively uses test samples that contain a high concentration of known trigger words. This creates a mismatch between the paper’s stated goal and its experimental design meaning the results may not reflect true generalization.

3- The semantic inversion process is manually designed and lacks consistency. The chosen text transformations may not always reverse the meaning as intended especially outside sentiment-based tasks making the method unstable across domains.

4- Thresholds for “strong” and “unchanged” influence are not formally defined leaving the detection rule subjective and hard to reproduce. Without quantitative criteria or sensitivity analysis the approach cannot be reliably replicated.

5- The metrics used such as the “positive ratio” capture shifts in output bias but do not demonstrate that the model actually becomes safer or more resistant to attacks. There is no reported drop in attack success rate so the defense effect remains speculative.

6- The attack setting is narrow limited to a single trigger phrase and one type of poisoning scheme. This restricts confidence in the method’s robustness to multi-trigger or adaptive poisoning.

7- No detailed analysis is given for the large number of false positives. Understanding why these samples are misclassified could have strengthened the paper’s claims about influence invariance as a reliable signal of poisoning.

8- The results lack statistical robustness no multiple runs variance or error bars are reported. Since influence values can fluctuate with random seeds this omission leaves uncertainty about stability and repeatability.

### Questions
1- How are the thresholds for “strong” and “unchanged” influence determined and are they constant across tasks?

2- Would the method still perform well on randomly selected test samples instead of trigger-heavy subsets?

3- Is there any measured correlation between “positive ratio” recovery and actual reduction in attack success rate?

4- What patterns or linguistic features characterize false positives and can they be systematically reduced?

5- How stable are influence-based detections across different random seeds or fine-tuning runs?

### Soundness
2

### Presentation
2

### Contribution
1

### Rating
2

### Confidence
4

---

## Human Reviewer 3

### Summary
This paper focuses on the safety risks arising from instruction-tuning attacks, where injected triggers can cause biased predictions during testing. To address this issue, the authors propose a method based on influence functions and relate it to sentiment transformation. They argue that samples with high influence scores that remain unaffected by sentiment transformation are likely toxic and should be removed. The study further demonstrates, through classification and mathematical reasoning tasks, that removing these toxic samples can effectively mitigate bias.

### Strengths
This work tackles an important problem — mitigating prediction bias introduced by instruction-tuning attacks. Moreover, linking sentiment transformation with influence functions may represent a promising direction for toxic sample detection.

### Weaknesses
1. Clarity and Presentation: The paper is not easy to follow. As a method-oriented study, more emphasis should be placed on the motivation and methodological design. However, the current version seems to focus excessively on experimental results, with too large figures and tables taking up much space. It is still not intuitively clear why sentiment transformation helps detect toxic samples. The authors should elaborate more on the underlying motivation and provide analytical experiments to validate it before moving on to broader empirical verification.

2. Incomplete Experimental Evaluation: The reported results mainly focus on true positive rates. However, overall performance metrics such as false negatives and overall accuracy are equally essential and should be included to provide a more comprehensive evaluation.

3. Limited Scope of Study: The experiments do not make use of more recent mainstream large language models such as LLaMA or Qwen. I encourage the authors to adopt these up-to-date models to strengthen the relevance and generalizability of their findings.

### Questions
Refer to our proposed weakness.

### Soundness
2

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
5