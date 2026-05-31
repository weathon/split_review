## Summary
The paper proposes a method to detect instruction fine-tuning (IFT) attacks in Large Language Models (LLMs) using influence functions. The core idea is to identify "critical poisons" by observing how the influence of a training example on a test set changes under semantic transformations (e.g., sentiment inversion). The authors hypothesize that while normal examples show inverted influence scores when the sentiment of the query is flipped, poisoned examples (which associate a trigger with a fixed label regardless of context) exhibit strong and invariant influence. The method is evaluated on sentiment classification (T5) and math reasoning (DeepSeek-Coder), demonstrating that removing ~1% of detected samples can mitigate the attack.

## Strengths
- **Novel Diagnostic Approach:** Using the stability of influence scores under semantic transformation as a signal for poisoning is an original and intuitive idea. It moves beyond simple loss-based or activation-based filtering.
- **Practicality:** By leveraging the EK-FAC approximation (Kronfluence), the authors demonstrate that influence-based detection is computationally feasible for models in the 1B+ parameter range, which has historically been a bottleneck for influence functions.
- **No Prior Knowledge:** The method does not require knowing the specific trigger (e.g., "James Bond") or the target label, making it more robust against "in-the-wild" attacks where the defender only observes anomalous model behavior.
- **Cross-Domain Evaluation:** The paper tests the method on two distinct tasks: sentiment analysis and mathematical reasoning, showing the potential for generalization.

## Weaknesses
### Fatal
None.

### Major
- **Heuristic Nature of Transformations:** The success of the method relies heavily on the choice of "semantic transformation." While sentiment inversion is straightforward for classification, the "opposite of" prefix for math reasoning (Section 3.4) is less intuitive. The paper lacks a systematic framework for how a defender should choose these transformations for arbitrary tasks.
- **Low Precision (True Positive Rate):** In Section 3.3, the method flags 653 examples to find 23 true poisons (TP rate of ~3.5%). While the authors argue that removing this 1% of data doesn't hurt performance, a 96.5% false positive rate is high. The paper would be much stronger if it explored why so many clean examples exhibit "poison-like" influence stability.
- **Limited Baseline Comparison:** While the authors qualitatively discuss why loss-based or spectral methods might fail, the paper lacks a rigorous head-to-head empirical comparison with these standard baselines (e.g., Spectral Signatures or Activation Clustering) on the same datasets.

### Minor
- **Evaluation Metric Clarity:** In Table 1 and Figure 5, the use of "POS Ratio" as a proxy for attack success is clear, but the "Accuracy" reported in Table 2 is very low (~56% for a binary-ish task), suggesting the underlying model is quite weak. It is unclear if the detection method remains as effective on a highly capable model where the "clean" influence signals might be sharper.
- **Ablation Detail:** The ablation study (Section 3.6) mentions that different prefixes had "almost no impact," but does not provide the quantitative data to support how sensitive the influence scores are to the specific phrasing of the inversion.

## Nice-to-Haves
- An analysis of the "False Positives": What are the 630 clean examples that look like poisons? Are they outliers, hard examples, or mislabeled data?
- Testing on a larger model (e.g., 7B+ parameters) to further prove the scalability of the EK-FAC influence approximation in a defense context.

## Novel Insights
The primary novel insight is that **poisoned examples in IFT attacks create "rigid" influence patterns.** Unlike legitimate data, where the relationship between input and output is semantically grounded (and thus sensitive to semantic negation), poisoned data creates a brute-force association between a trigger and a label. This rigidity manifests as an invariance in the influence function when the semantic context of the query is transformed, providing a unique statistical signature for detection.

## Suggestions
- Include a table comparing the TPR/FPR of your method against a "High-Loss" baseline and "Spectral Signatures" to substantiate the claims in Section 3.5.
- Provide a more formal definition or a set of examples for the "semantic transformations" used in the math reasoning task to help readers understand how to apply this to non-classification tasks.
- Clarify the selection of the "100 test samples" used for influence calculation. In a real-world scenario, how does a defender pick these samples without knowing the trigger? (e.g., do they use samples where the model shows high confidence in a suspected harmful output?)

## Score and Decision
The paper presents a creative and technically sound application of influence functions to a pressing security problem in LLMs. While the precision of the detection is low, the "do no harm" aspect (removing 1% of data restores safety without losing accuracy) makes it a viable defense. The use of modern approximation techniques for influence functions makes the work relevant to the current scale of ML.

MY FINAL SCORE: <score>6.5</score>
MY FINAL DECISION: <decision>Accept</decision>