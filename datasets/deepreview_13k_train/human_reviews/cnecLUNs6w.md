# Adversarial Robustness of In-Context Learning in Transformers for Linear Regression

- Decision: Reject
- Scores: 3, 6, 5

## Abstract
Transformers have demonstrated remarkable in-context learning capabilities across various domains, including statistical learning tasks. While previous work has shown that transformers can implement common learning algorithms, the adversarial robustness of these learned algorithms remains unexplored. This work investigates the vulnerability of in-context learning in transformers to \textit{hijacking attacks} focusing on the setting of linear regression tasks. 
Hijacking attacks are prompt-manipulation attacks in which the adversary's goal is to manipulate the prompt to force the transformer to generate a specific output.
We first prove that single-layer linear transformers, known to implement gradient descent in-context, are non-robust and can be manipulated to output arbitrary predictions by perturbing
a single example in the in-context training set. While our experiments show these attacks succeed on linear transformers, we find they do not transfer to more complex transformers with GPT-2 architectures. Nonetheless, we show that these transformers can be hijacked using gradient-based adversarial attacks. We then demonstrate that adversarial training enhances transformers' robustness against hijacking attacks, even when just applied during finetuning.  Additionally, we find that in some settings, adversarial training against a weaker attack model can lead to robustness to a stronger attack model. Lastly, we investigate the transferability of hijacking attacks across transformers of varying scales and initialization seeds, as well as between transformers and ordinary least squares (OLS). We find that while attacks transfer effectively between small-scale transformers, they show poor transferability in other scenarios (small-to-large scale, large-to-large scale, and between transformers and OLS).

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper explores the adversarial robustness of in-context learning in transformers, focusing on hijacking attacks in linear regression tasks. Single-layer linear transformers are shown to be easily manipulated, while complex models like GPT-2 resist simple attacks but remain vulnerable to gradient-based ones. Adversarial training enhances model robustness, especially during fine-tuning, and hijacking attacks transfer only among smaller models.

### Strengths
1. The paper is overal clear and well-written with sufficient experiments.

### Weaknesses
1. I find the use of x-attack, y-attack, z-attack to be confusing. The joint attack (z-attack) does not really corespond to a different dimension to attack. It is better to call it data, label, and joint attack, or something similar. 
2. From the motivation level, I am uncertain if hijacking attack is the main concern in the applications of LLM for transformers. These line of work along Garg et al. are used to demonstrate the in-context capability of transformers which is a simplified setting but sufficient. The typical adversarial learning considers the setting where the input is modified only slightly, but the adversary can have large impact on the output. I don't see how this classical analysis can easily transfer to the text domain. How to define the allowable small perturbation. If we naively apply on token-level, people can easily find it. If the text contains number, and we only make small modification on the number, will it actually lead to different output. So, I am not sure if the paper can provide many insights into understanding the hijack attack for LLM.
3. Since the authors mainly investigate the in-context learning setup, they should consider some context-specific attacks, for example within context or across-context. I don't think uniform attack on all possible entries are the only interesting scenario.
4. I appreciate the empirical effort by the authors. In terms of novelty, I would like to see more novel algorithm design and potential implications, since incontext is still a different setting from the standard ML setting. 
5. I find the experiment section to be hard to follow. Even though the model choice is discussed in the setup section, it is unclear what architecture and training procedure that each figure corresponds to e.g. figure 2.3.4.

### Questions
1. Can the author provide why the adversarial examples fail to transfer? It is possible that the attack examples cannot be transferred from linear attention model to GPT2, but it can transfer from GPT2-small to GPT2-large. 
2. Has the author experiments with larger model than GPT2, such as llama 8B? I am wondering if the hijack attacks can be mitigated by the emergent ability of transfoermers. 
3. Did the author experiements with TRADES, which usually serves as a better defense than the original PGD.

### Soundness
2

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
3

### Summary
The paper shows that linear transformers trained on linear regression aren't robust to hijacking attacks. Moreover, the authors show that these attacks don't transfer from small models to more complex GPT2-style ones (and even among them). The latter can be hijacked with gradient-based optimization. Finally, adversarial training (or fine-tuning) is shown to be promising to prevent these attacks.

### Strengths
- Methods and experiments are clearly explained and carried out. The work is original, but the scope could have been better stated.

- Results are well presented and commented on. However, they're not very significant.

- I personally like the part about adversarial training, as it is a promising method to make transformers more robust to attacks.

### Weaknesses
 - I don't get the point of this work and why it has to be considered relevant for the community. I would say this better, possibly on the first page.

- I would have tried to inspect better why attacks don't work on GPT2 style models. This would have been helpful in understanding better how these models perform linear regression.

### Questions
1. What's the meaning of these attacks in the context of linear regression? Is there a more practical interpretation?

2. How do these results compare to when using OLS? Can the latter be used as a baseline?

3. What does adversarial training on attacks mean from a linear regression perspective? (eg. can it be related to some form of regularization?)

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper focuses on studying the adversarial robustness of in-context learning for transformers. The paper first proves that a single-layer transformer can be manipulated to output arbitrary predictions, and also uses gradient-based attacks to demonstrate the vulnerability of GPT-2.

### Strengths
1. The paper has a solid theoretical analysis to show the vulnerability of single-layer transformers.

2. Beyond single-layer transformers, the paper also considers GPT-2, and the experimental results appear to support the conclusions well.

3. The paper is easy to follow and well-organized.

### Weaknesses
1. The novelty of this paper is limited because the phenomenon that single-layer transformers and GPT-2 are vulnerable to adversarial attacks is not surprising, and the paper does not have new and strong technical contribution compared with existing gradient-based attacks.

2. The task that uses GPT-2 for linear regression is not well-motivated. We usually do not use GPT-2 to solve linear regression.

3. The paper does not propose any new defense method beyond adversarial training, which is a standard baseline.

### Questions
No question, and please refer to the weakness part.

### Soundness
2

### Presentation
3

### Contribution
2
