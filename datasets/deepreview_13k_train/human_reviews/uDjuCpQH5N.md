# Do Unlearning Methods Remove Information from Language Model Weights?

- Decision: Reject
- Scores: 5, 3, 8, 6

## Abstract
\vspace{-0.2cm}
Large Language Models' knowledge of how to perform cyber-security attacks, create bioweapons, and manipulate humans poses risks of misuse. Previous work has proposed methods to \textit{unlearn} this knowledge. Historically, it has been unclear whether \textit{unlearning} techniques are removing information from the model weights or just making it harder to access.  To disentangle these two objectives, we propose an adversarial evaluation method to test for the removal of information from model weights: we give an attacker access to some facts that were supposed to be removed, and using those, the attacker tries to recover other facts from the same distribution that cannot be guessed from the accessible facts. We show that using fine-tuning on the accessible facts can recover 88\% of the pre-unlearning accuracy when applied to current unlearning methods, revealing the limitations of these methods in removing information from the model weights.}

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper addresses the challenge of unlearning in LLMs and investigates whether unlearning methods effectively remove knowledge or simply make it more difficult to access. To evaluate the effectiveness of current unlearning methods, the paper introduces a novel approach called Retraining on T (RTT) from the attacker’s perspective.
RTT operates under the assumption that attackers have access to part of the unlearned knowledge (T set) and aims to recover the unknown portion of this knowledge (V set) by retraining the model on the T set. The paper also presents a framework that includes this attack method and curated datasets to quantitatively evaluate existing unlearning methods.
The study evaluates three unlearning methods on the Llama-3-8B model: gradient difference (GD), representation misdirection for unlearning (RMU), and random incorrect answer (RIA). The results reveal that RTT can restore over 88% of the model's pre-unlearning accuracy, indicating that these unlearning methods may not fully remove the targeted information.

### Strengths
- The paper highlights a critical AI safety issue: whether unlearning methods ensures information in LLMs, especially harmful content and senstive information, is effectively removed, not just hidden. By quantitatively assessing the distinction between "removal" and "hiding", the paper addresses key concerns in the field.
- The proposed framework, which includes the RTT method and a dataset encompassing various types of knowledge with well-defined metrics, enables a quantitative evaluation of the effectiveness of unlearning methods in determining whether information is removed.
- The paper does a comprehensively evaluation by considering various settings, including different hyperparameters, text formats, and granularities of hidden knowledge.

### Weaknesses
 - The paper could evaluate more unlearning methods such as other baselines listed in [1].
- The paper could incorporate more types of knowledge assessment tasks besides MCQ.
- The paper could give more detailed explanation of the experiment setting, e.g., the different text formats.
- Some presentation is a bit misleading as listed in questions.

### Questions
- Could the authors explain the meaning of the uncertainty mentioned on line 257?
- Why is "MCQ with Loss on Answer Only" tested solely on GD in Figure 4?
- Please clarify the definition of the terms such as forget/retain accuracy for accuracy on forget/retain set.
- Are the labels "Unlearn" and "Unlearn+RTT" in Figure 3 misplaced? Additionally, please show the alpha values in Figure 3.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The authors present a framework for evaluating the extent of unlearning that occurs in proposed unlearning methods for LLMs. They perform fine-tuning experiments that easily recover performance on forget-set information from models that have had unlearning techniques applied. The authors also test the robustness of their evaluation methodology.

### Strengths
- The paper is well-written, and easy to follow.
- The authors' methodology for dataset curation was sound
- The paper tackles an important area, which is crafting better evaluations for unlearning methods to understand their limitations

### Weaknesses
 - Limited technical novelty/contributions. As prior work has already proposed relearning as a metric for evaluating unlearning [1, 2, 3, 4, 5], the paper's contribution rests solely on creating training and validation splits with low mutual information for the relearning evaluation. For example, prior work already shows that RMU is not robust to relearning [1].
- The authors claim that "Our evaluation does not guarantee that information is removed from the weights; rather, it sets a higher bar than previous evaluation methods for unlearning," but comparisons are not made between the proposed evaluation and similar "relearning time" metrics proposed in [2, 3]. Furthermore, prior work (which the authors do cite) suggests that relearning time is already sufficient for measuring unlearning [1, 3]. 
- The authors acknowledge that their proposed connection between mutual information and relearning is not substantiated; specifically, they acknowledge that robustness to relearning does not necessarily imply zero mutual information between a forget set and model weights. Unfortunately, while acknowledgement is appreciated, this limits the usefulness/novelty of the evaluation, especially in the context of Section 3.2.

### Questions
1) Based on the 2nd limitation discussed, can authors provide any commentary on possible downsides of their relearning evaluation for unlearning methods that appear more robust than current methods?

In all, this work in its current state would be better suited for a relevant workshop; a significantly expanded evaluation across more methods and models could constitute a stronger contribution if the evaluation metrics were to remain constant.

### Soundness
2

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This manuscript reveals that models may hide instead of unlearn knowledge under existing unlearning approaches. Considering a model that is supposed to have unlearned mutually exclusive datasets T and V. This model may still reveal information from V when the model is only retrained on T.

### Strengths
1. The findings are interesting. Machine unlearning is a hot topic, especially in the era of generative AI as privacy matters more. I believe the contribution is sufficient for a publication. 

2. Concepts are formally introduced or defined. The structure of the paper is clear.

3. Experiments are performed across various settings, and the empirical evidence sufficiently supports the claims made.

### Weaknesses
The real-world use case of the RTT approach remains unclear.

### Questions
What are the real-world use cases of the RTT approach? I.e., what are specific examples of V and T as defined in the paper? When does it make sense for the adversary to have (legitimate) access to T that was part of the dataset that was retrained?

Suggestions for further improving the paper: when T is closer to V topic-wise, would the RTT approach be more successful? For example, if V and T are both cybersecurity knowledge (from the WMDP benchmark) and T is hardware security, would RTT perform better on V_1 system/OS security than on V_2 machine learning security? I understand T and V are supposed to be mutually exclusive, but they might be close in topics.

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The authors present a fine-tuning method as an adversarial approach to evaluate the effectiveness of unlearning methods. They create two datasets T and V that are disjoint (no mutual information) and show that after unlearning both, retraining on T recovers knowledge about V. This implies that knowledge was never removed.

### Strengths
## Contribution
Unlearning is a growing field and rigorous evaluations will be important. Most methods report output-only metrics that do not necessarily measure the effectiveness of unlearning in removing information from model weights and can confound removal with obfuscation. Previous work had already proposed adversarial methods to evaluate unlearning, including fine-tuning on a subset of the unlearned information. I think the main contribution of the authors is putting the effort to show that even if retraining and unlearning datasets are disjoint, information can be recovered for the unlearning dataset.

## Experimental setup
* The authors present a diverse set of datasets that account for different behaviours and complexities. For instance, I expect mechanisms to "unlearn" birthdays to be very different to those used for hazardous knowledge generally.
* The authors put great efforts in searching for hyperparameters that provide a strong baseline for unlearning.
* Authors also consider 3 unlearning algorithms that have very different objectives and are likely to produce different effects in the models. Yet, all of them fail to robustly unlearn knowledge.

## Other comments
* I agree with the recommendations proposed by the authors.

### Weaknesses
## Contribution
* I think the authors overlook very relevant works that already showed unlearning failed to remove information from the model weights (https://arxiv.org/pdf/2402.16835) and that fine-tuning on unrelated data can recover information (also https://arxiv.org/pdf/2402.16835 and https://arxiv.org/pdf/2406.13356v1). Although I think the main contribution (showing effects of disjoint datasets) still holds and is relevant, the paper could benefit from a better contextualisation, especially with respect to the first work (e.g. using newer methods like RMU).

* I wonder if the knowledge separation between T and V is fundamentally different from fine-tuning on partial unlearned information as done by previous work. My main concern is that although T and V are disjoint, they come from the same distribution and were both used for unlearning simultaneously, and therefore are likely to rely on similar internal mechanisms for obfuscation. The effects could be similar to fine-tuning on the unlearned facts as far as the mutual information remains low (e.g. using only few examples). It would be interesting to test if fine-tuning on completely unrelated information that was not used during unlearning also has similar effects (as done by some concurrent works e.g. https://arxiv.org/abs/2409.18025 or in the safety space by https://arxiv.org/abs/2310.03693). Authors could try different levels of similarity. For example, for MMLU, they could first fine-tune on questions from different topics (questions will look similar in format but content will be significantly different) and then in completely unrelated information (e.g. birthday questions).

## Experimental setup
* It would be great if authors could held-out a set of questions from the unlearning dataset and report the model accuracy on those after unlearning. This could help contextualise and motivate the low vs high granularity experiments since under the assumption of independence between facts, performance should remain constant on held-out after unlearning. For instance, can the model still answer questions about birthdays that did not go into the unlearning mix?
* The sizes of V and T seem disproportionate. I expected V to be much larger than T, but it seems to be the other way around (e.g. in Years the proportion is 4:1). As most previous work, I would expect the retraining dataset to be as small as possible, especially since the authors admit that leakage-free datasets are hard to build; the larger T is, the higher the likelihood that info in V can be inferred from T. Including ablations on this would be appreciated (e.g. fine-tune on V instead).

## Results
* I do not really understand Figure 3. Maybe there is a better visualisation for this? Why is the forget accuracy larger for Unlearn than for Unlearn+RTT?

### Questions
* Did you try "HIGH GRANULARITY KNOWLEDGE HIDING" with RMU?
* Are names unique in the birthdays dataset?
* Also mentioned above, have you tried ablating the size of T?

## Suggestions
* I would suggest improving the structure of the results section. Currently, there are many plots and several of them seem to be explained in text in the same paragraphs, which are very information dense. Maybe using paragraphs with main takeaways could help readers more quickly grasp what is the main information they should be looking for in the results.
* I would love to see some suggestions on how to use RTT as an evaluation framework/metric. Coming back to a previous suggestion on exploring completely unrelated information, I think using unrelated datasets could be extremely interesting if creating disjoint and same-distribution V and T datasets is not practical.
* Plots seem to be too big for their content. Have you considered having 4 per row?

### Soundness
4

### Presentation
4

### Contribution
2
