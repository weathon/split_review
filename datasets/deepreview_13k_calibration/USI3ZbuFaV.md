# Certifying Language Model Robustness with Fuzzed Randomized Smoothing: An Efficient Defense Against Backdoor Attacks

- Decision: Accept
- Avg Score: 6.00
- Scores: 6, 6, 6, 6

## Abstract
The widespread deployment of pre-trained language models (PLMs) has exposed them to textual backdoor attacks, particularly those planted during the pre-training stage. These attacks pose significant risks to high-reliability applications, as they can stealthily affect multiple downstream tasks. While certifying robustness against such threats is crucial, existing defenses struggle with the high-dimensional, interdependent nature of textual data and the lack of access to original poisoned pre-training data. To address these challenges, we introduce **F**uzzed **R**andomized **S**moothing (**FRS**), a novel approach for efficiently certifying language model robustness against backdoor attacks. FRS integrates software robustness certification techniques with biphased model parameter smoothing, employing Monte Carlo tree search for proactive fuzzing to identify vulnerable textual segments within the Damerau-Levenshtein space. This allows for targeted and efficient text randomization, while eliminating the need for access to poisoned training data during model smoothing.  Our theoretical analysis demonstrates that FRS achieves a broader certified robustness radius compared to existing methods. Extensive experiments across various datasets, model configurations, and attack strategies validate FRS's superiority in terms of defense efficiency, accuracy, and robustness.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces a novel defense technique called *fuzzed randomized smoothing* (FRS) to improve the robustness of pre-trained language models against textual backdoor attacks introduced during the pre-training phase. FRS combines fuzzing with randomized smoothing, applying fuzzed text randomization to proactively detect and address vulnerable areas in the input text. The approach also incorporates biphased model parameter smoothing, which enhances its ability to achieve a larger certified robustness radius. Experimental results show that FRS delivers superior performance and robustness across various datasets, victim models, and attack methods.

### Strengths
1. The authors introduce *Fuzzed Randomized Smoothing (FRS)*, a novel approach to certify the robustness of language models against backdoor attacks

2. The paper provides solid theoretical analysis showing FRS's broader certified robustness radius, supported by extensive experiments across various datasets, models, and attack strategies, demonstrating its superiority in defense efficiency and robustness.

3. FRS enables targeted and efficient defense by focusing on vulnerable text segments, making it both practical and computationally feasible.

### Weaknesses
1.  **Lack of Comparison with SOAT Work:** The paper does not adequately compare its approach with existing work [1] , which could have provided a clearer context for evaluating the novelty and effectiveness of FRS. Specifically, the paper lacks a detailed comparison of the theoretical underpinnings of FRS with those of [1], particularly concerning the certified robustness radius and the assumptions made about the threat model. A more rigorous comparison would involve analyzing the specific conditions under which each method provides guarantees, and how these conditions relate to the practical scenarios considered in the experiments.

2.  **Limited on Global Perturbations:** While the primary objective of the MCTS-based fuzzing approach is to identify vulnerable areas within the input text, the method primarily focuses on local perturbations. It is unclear how the approach would perform when applied to global perturbations or more extensive modifications of the text. For instance, the paper does not explore scenarios where the entire sentence structure is altered, or where multiple non-contiguous segments are modified simultaneously, which could be indicative of more sophisticated attacks.

3.  **Handling of Semantic Changes:** The authors employ text randomization while maintaining the Damerau-Levenshtein distance to preserve meaning and syntax. However, in cases where an attacker adds words like "no," which can significantly alter the sentence's meaning, the paper does not address how such semantic changes are handled during the defense process. The reliance on Damerau-Levenshtein distance alone may not be sufficient to capture semantic changes, and the paper lacks a clear mechanism to detect and mitigate such attacks.

### Questions
1. Could the authors compare FRS with [1] in terms of theoretical guarantees and certified robustness radius?

2. Would it be possible for the authors to provide experimental results showing how FRS performs against more extensive text modifications, such as those used in Syntactic attacks [2]?

3. Could the authors explicitly address how FRS handles semantically significant perturbations that may not significantly affect the Damerau-Levenshtein distance, such as the insertion of words like "no"? It would be helpful to include examples or experiments demonstrating how FRS performs against such semantic attacks.


[1] Zhang, Xinyu, et al. "Text-crs: A generalized certified robustness framework against textual adversarial attacks." 2024 IEEE Symposium on Security and Privacy (SP). IEEE, 2024.

[2] Qi, Fanchao, et al. "Hidden Killer: Invisible Textual Backdoor Attacks with Syntactic Trigger." Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers). 2021.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes Fuzzed Randomized Smoothing to efficiently certify language model robustness against backdoor attacks. Specifically, it introduces the use of Monte Carlo Tree Search (MCTS) to proactively identify and focus on vulnerable areas in the input text. Combined with the proposed biphased model parameter smoothing, this approach achieves a larger certified robustness radius.

### Strengths
1. This paper's biphased model parameter smoothing and MCTS-based text randomization enhance the effectiveness and efficiency of randomized smoothing, presenting a novel approach. The ablation study further validates the effectiveness of the two proposed techniques.


2. Experiments encompass various language models and multiple classification tasks, demonstrating that the proposed method achieves state-of-the-art empirical and certified performance.


3. The paper also provides a theoretical robustness bound.

### Weaknesses
The main weakness, in my opinion, is that the tasks in the experiments are limited to classification problems. I believe that conducting experiments on defending against backdoor attacks in open-ended generation tasks with LLMs could further demonstrate the effectiveness and practicality of the proposed method.

### Questions
NA

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces Fuzzed Randomized Smoothing (FRS), a defense mechanism against backdoor attacks on language models. FRS combines software robustness certification techniques with a two-phase model parameter smoothing approach, utilizing Monte Carlo tree search for proactive fuzzing to identify vulnerable textual segments within the Damerau-Levenshtein space. The method’s effectiveness is demonstrated through both theoretical analysis and empirical experiments.

### Strengths
- The topic of defending against backdoor attacks on language models is both timely and challenging.
- The method addresses these attacks by applying randomized smoothing and extends this approach from continuous to discrete space through Monte Carlo tree search-based text randomization.
- FRS is practical, as it does not require access to the original poisoned training dataset.
- The paper provides both theoretical and empirical evidence to support the method’s effectiveness.

### Weaknesses
 - A section discussing the threat model, including the defender's abilities and objectives, would enhance the paper.
- The defense method requires access to the fine-tuning phase, which limits its applicability to popular black-box LLMs.

### Questions
Please see weakness.

### Soundness
3

### Presentation
2

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
This paper proposes a novel method called Fuzzed Randomized Smoothing (FRS) for certifying the robustness of language models against text backdoor attacks. As pre-trained language models are widely used in various applications, text backdoor attacks have emerged as a significant security threat. Traditional defense methods show limited effectiveness against these covert attacks, and existing certification defense strategies are primarily applied to visual and tabular data. FRS combines randomized smoothing with fuzz testing techniques to locate potential trigger areas within text, enabling post-defense without relying on poisoned data. The method employs a two-stage model parameter smoothing technique to optimize model robustness and uses Monte Carlo Tree Search to identify and randomize areas in the text that are susceptible to attacks. Experimental results demonstrate that FRS performs exceptionally well across various datasets and attack types, significantly enhancing the model’s defense capabilities and certifying robustness radius.

### Strengths
- Innovative solution, introducing fuzz testing techniques into text backdoor defense, achieving a randomized smoothing certification method without the need for poisoned data for the first time.

- Theoretical and experimental results indicate that this method significantly improves robustness radius and defense efficiency compared to existing methods.

- The two-stage smoothing strategy effectively reduces computational overhead, making it suitable for large language models.

### Weaknesses
The complexity of FRS is relatively high, with significant computational resource requirements, which may pose limitations in practical application scenarios.

The problem formulation is arguable. Notice that the backdoor trigger can also appear in the normal text $x$. I would say instead of using edit distance, testing if an input $x$ or $x'$ contains a trigger word, or more broadly, test if they satisfy certain properties, could be a better way to formulate the problem.

It is better to include test set accuracy results in addition to certified accuracy. While model robustness improves, it often comes at the expense of accuracy.

### Questions
- Could the authors explain why Ranmask[a1] and Safer[a2], which are also designed for text adversarial attacks and can be extended to backdoor attacks due to their use of  $l_0$  norm radius to certify model robustness, were not included in the comparisons?

[a1] Zeng, Jiehang, et al. "Certified robustness to text adversarial attacks by randomized [mask]." Computational Linguistics 49.2 (2023): 395-427.

[a2] Ye, Mao, Chengyue Gong, and Qiang Liu. "SAFER: A structure-free approach for certified robustness to adversarial word substitutions." arXiv preprint arXiv:2005.14424 (2020).

### Soundness
3

### Presentation
3

### Contribution
3
