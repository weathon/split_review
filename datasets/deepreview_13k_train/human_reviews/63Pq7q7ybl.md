# Toward Domain Translation with Monolingual Domain Data Only

- Decision: Reject
- Scores: 6, 6, 3, 3

## Abstract
Neural machine translation (NMT) is very sensitive to domain shifts requiring a carefully designed fine-tuning strategy to avoid catastrophic forgetting problems when adapting to a new domain.  Fine-tuning usually relies on high quality in-domain data, but constructing a sufficient amount of parallel data for training poses challenges even for fine-tuning. In contrast, domain-specific monolingual resources are more accessible when compared with bilingual data. Therefore, we challenge the domain adaptation of a general NMT model using only features obtained from a small amount of monolingual data. We regard the task as an instance of domain shifts, and adopt energy-based models (EBMs) and approximate these EBMs using Conditional Distributional Policy Gradients (CDPG). Recent work has applied CDPG with a small number of EBMs for NMT models limiting the capacity for domain shifts, but we construct a large number of EBMs considering the entire domain-specific data, i.e., unigram distribution, and perform fine-tuning according to their constraints. Our results show that fine-tuning using a large number of EBMs can achieve a robust domain shift without causing catastrophic forgetting, demonstrating a robust domain shift using only a small amount of monolingual resources.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a method to perform domain translation for neural machine translation (NMT) by utilizing only monolingual domain-specific data. The authors employ energy-based models (EBMs) combined with Conditional Distributional Policy Gradients (CDPG) to perform domain adaptation without relying on large-scale parallel domain-specific data, which is often challenging to collect. The paper further proposes DYNAMIC CDPG to improve upon traditional CDPG by dynamically adjusting parameters using bilingual validation data, aiming to achieve optimal results without catastrophic forgetting. Experiments are conducted across several translation directions and domain adaptation scenarios.

### Strengths
Innovative Approach: The use of energy-based models combined with CDPG for domain adaptation with only monolingual data represents a novel approach that addresses a key limitation in domain-specific NMT.
Effective Results: The experimental results show that DYNAMIC CDPG performs well compared to fine-tuning and LORA-based methods, with improvements in key evaluation metrics such as BLEU and NIST scores.
Reduction in Catastrophic Forgetting: The proposed approach successfully mitigates catastrophic forgetting, which is a common issue in domain adaptation tasks, thus preserving the pre-trained model’s knowledge while adapting to a new domain.

### Weaknesses
Limited Scope of Evaluation: The experiments are conducted on a relatively small set of translation directions and domains. Expanding the evaluation to include additional languages and domains, particularly those with greater typological diversity, would provide stronger evidence for the generalizability of the approach. For instance, testing on low-resource languages or languages with significantly different sentence structures could reveal limitations not apparent in the current evaluation.

Lack of Robust Comparison: The paper primarily focuses on comparisons with pre-trained, fine-tuned, and LORA baselines. It would be beneficial to include comparisons with other strong domain adaptation techniques such as back-translation, iterative back-translation, and adversarial domain adaptation, which could provide a more holistic understanding of the strengths and weaknesses of the proposed methods. Specifically, comparisons should include methods that also leverage monolingual data for domain adaptation, to better contextualize the contribution of this work.

Complexity of Methodology: The proposed methodology is relatively complex, and while the theoretical explanations are well-written, it may be challenging for readers without a background in reinforcement learning or energy-based modeling to fully grasp. Adding intuitive explanations or visual aids, particularly for the EBM and CDPG components, would enhance accessibility. Furthermore, a more detailed breakdown of the algorithm, with clear pseudocode, would be beneficial.

### Questions
Hyperparameter Analysis: While Table 2 provides insight into top-p values used for DYNAMIC CDPG, can the authors provide a deeper analysis on the sensitivity of other hyperparameters (e.g., learning rate, λ values for EBMs) and how they impact the final results? A sensitivity analysis or a hyperparameter optimization discussion could greatly strengthen the paper.

Computational Efficiency: How does the proposed approach compare in terms of computational cost to other domain adaptation methods, such as back-translation or adversarial domain adaptation? The paper mentions improvements in alignment quality, but a more explicit analysis of the computational trade-offs would be valuable.

Scaling to Larger Domains: Can the authors discuss the scalability of the proposed approach to much larger domain adaptation tasks? For example, would the methodology perform well with highly diverse target domains or significantly larger monolingual datasets?

Effectiveness of Monolingual Features: The paper leverages unigram frequency for domain adaptation, which is a relatively simple feature representation. Have the authors considered experimenting with more sophisticated feature representations, such as n-gram frequencies or embeddings? Would these improve the performance of CDPG and DYNAMIC CDPG for domain shifts?

Handling Noisy Monolingual Data: In real-world scenarios, monolingual domain data might be noisy. How robust is the proposed approach when dealing with noisy or imperfect monolingual data? Some discussion or experiments on the effects of noisy data would be insightful.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper presents a new domain adaptation method for adapting a pretrained NMT model with low-resource monolingual in-domain data. The method employs conditional distribution policy gradients to approximate domain-specific features in the target languages, where the domain-specific features are represented by unigram distributions. The authors also propose dynamic CDPG, which dynamically adjusts parameters using a small bilingual validation sample. Experimental results show that their framework achieves improvements in some domains, primarily due to the model's enhanced learning of domain-specific words.

### Strengths
- Novel approach for domain adaptation using only monolingual data: The paper presents energy-based models to effectively adapt to monolingual domain-specific corpora.
- Extensive evaluation: The paper includes a variety of domains and languages to validate the proposed methods and provides additional analysis of improvements by assessing domain-specific terminology.

### Weaknesses
 - Concerns with practicality and scalability: The setup in this paper raises concerns about practical applicability. In real-world scenarios, domain-specific corpora may often be more abundant, even when restricted to monolingual resources, and may differ significantly in size compared to the data setup in the paper. It remains unclear whether the proposed framework would can show scale well with larger datasets or whether it would overfit to small monolingual training sets, potentially only capturing domain features seen during training. This could lead to an over-reliance on vocabulary or terms specifically within the training set, rather than robust. The results may reflect high performance in producing domain-specific terms, but this may primarily apply to cases where test instances closely match the training domain vocabulary, potentially limiting broader generalization. 

- Evaluation metric suitability: The selected evaluation metrics may not fully demonstrate the strengths of the proposed approach. The confidence scores of softmax indomain translation is somewhat concerning, as this does not necessarily correlate with successful adaptation. Moreover, author did not consider other naturalness metric  like fluency or advanced model based quality estimation metric, such as COMET. These metrics could provide a more reliable measure of adaptation performance and reveal whether the model truly maintains translation quality.

### Questions
- Domain feature generalization: One question is whether the model truly learns and generalizes domain features using this method. Specifically, I am curious if, during testing, the model can generate domain-specific terms that were not present in the monolingual training data but are consistent with the target domain's linguistic characteristics. If the model can accomplish this, it would indicate a deeper understanding of domain features rather than merely reproducing the training vocabulary. A more detailed analysis or experiments testing this capability would be valuable.

- Sensitivity to validation bilingual set in DCDPG: Given that DCDPG relies on a bilingual validation set for dynamic parameter tuning, I wonder if the method’s performance is sensitive to the quality and representativeness of this validation set. Could performance vary significantly depending on the domain alignment or size of the validation set used? This would be an important consideration for practitioners, as varying validation sets could lead to inconsistent results in practice.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This paper looks at modeling domain-specific translation by formulating the target domain as a conditional energy based model (EBM), and approximates the EBM with conditional distributional policy gradients (CDPG). The approximation is done by using unigram probabilities to model the target domain, create binary features of when unigrams appear in target sentences, and fine-tune the pre-trained translation model according to the constructed EBM. The authors also propose a dynamic variation of CDPG specific to autoregressive modeling. On en <-> zh and en <-> de models, the method is compared to the original model, a 3k sample fine-tuned model, and a LoRA fine-tuned model.

### Strengths
1. Energy-based models have been well established for controllable generation and using them in the context of domain-specific MT is a solid application in an important problem. 
2. This method can apply on top of pre-existing models, as the authors show with the OPUS-MT models. This improves its extensibility where a model does not need to be trained from scratch to begin with.
3. The method outperforms a normal fine-tuning based approach for a reduced number of fine-tuning sentences, across 4 language directions.

### Weaknesses
1. My biggest concern with this work is its limited novelty especially compared to the work of Korbak et al. 2022. This work proposes how to represent the feature probabilities $\mu$ with unigram probabilities, but that seems to be all beyond the Korbak paper. Some discussion of exactly where this work differs would help differentiate them and highlight novelty. 
2. The use of EBMs and CDPG is motivated by avoiding catastrophic forgetting, but there does not seem to be evidence of this in the results. In the intro, catastrophic forgetting is equated to reduction in translation performance, which is not quite what other work defines as catastrophic forgetting. Catastrophic forgetting refers to becoming worse on the original data distribution - showing improved performance on the target domain is not enough to evaluate catastrophic forgetting. The methods should ideally be evaluated on the original domain as well in order to show this.
3. Calling this method “monolingual data only” or unsupervised does not seem to work well with proposing dynamic CDPG as a main contribution in this work. These descriptors seem to only target the extension of vanilla CDPG to MT. These descriptors seem to only target the extension of original CDPG to MT. 
4. There is a lack of implementation details regarding the EBM models and the fine-tuning procedure.

### Questions
1. What is the significance test you are running in the main tables?
2. Why use BERTScore over COMET? The latter is generally better for evaluating translations. 
3. What is needed for the implementation of the EBMs? Some pseudocode/algorithm/code outlining the creation of the EBMs and the fine-tuning of the translation models would be helpful.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the topic of adapting a neural machine translation model to a specific domain when only target-language domain-specific data is available. The proposed approach uses energy-based models based on the vocabulary of the domain-specific data to adapt an existing NMT model to the specific data. The proposed model improves translation quality somewhat inconsistently, and through analysis this is attributed to improvements on domain-specific terminology.

### Strengths
1. The proposed method is described clearly and the method itself is well-justified.

2. There is a fair amount of analysis into successful and failure cases.

3. The results include statistical significance testing.

### Weaknesses
1. This paper would benefit from clearly defining and justifying the task at hand. It addresses domain adaptation with target-side monolingual data, and that is well justified. However, there are several implicit assumptions throughout that do not seem to be stated clearly or given a justification. For example, a) assuming that they are starting from a generic trained model to adapt, and cannot train a model to the relevant domain from scratch (section 4.2), b) assuming that the adapted model shouldn't have catastrophic forgetting of the original domain (line 45), c) assuming that it is desirable to do well on tasks that were unseen in both the original model and the adaptation data (table 6), and d) that the adapted output should exhibit minimal changes compared to the original model (line 410). There is nothing wrong with these assumptions necessarily, but you need to clearly state them and justify why you are restricting your exploration to these.

2. There are some issues with the evaluations. First, the base model that is used is OPUS-MT, but the domain-specific datasets that are used for evaluation for EN<->DE come from OPUS, so they were used to train the base model. Thus, this is not a true scenario of domain adaptation to an unseen domain, but one of domain shift. It is not clear to me whether this was done intentionally, but I think it would be preferable to do some domain adaptation evaluations with unseen data (and this might explain the lack of consistent positive results for any of the domain adaptation models, including the baselines and the EBM approach). Second, confidence is used as an evaluation score, when it is not clear that this correlates with any sort of meaningful MT evaluation. Third, the examples given in table 5 point more towards overfitting to the vocabulary of a specific dataset (*not* a specific domain) than to any true translation quality improvements.

3. This paper should take a broader view of the literature, including terminology-constrained machine translation (which seems to be hinted at as the ultimate goal of the proposed approach, e.g. in line 410 and table 5) as well as cases where the assumptions I listed in item 1 are relaxed (e.g., training a domain-specific model from scratch). In addition, the following paper is directly related (even without taking a broader view) and should be used as a baseline: https://arxiv.org/pdf/2010.12652.

4. Beyond the missing citations, the baselines are insufficient or problematic. a) The proposed approach should be compared against LLM translation, both generic and using in-context learning with monolingual examples, the latter of which would directly address the problem at hand. b) The fine-tuning comparisons only evaluate i) fine-tuning the entire model and ii) fine-tuning only the attention weights. To me given the small dataset and focus on target-side data it would make sense to explore other approaches like fine-tuning the decoder only. c) Line 199 says "the checkpoint, which has the best performance on the development set, is measured for comparison." but line 193 says fine-tuning is done on the development set. So the models are fine-tuned on the same set that is used for checkpoint selection; it would not be surprising if they don't generalize well to the test set.

### Questions
1. In line 36, you say "automatically collecting a sufficient amount of domain-specific parallel data is challenging". It would be good to get some quantitative information to justify this statement, particularly what you mean by "sufficient". In general, fine-tuning and ICL can work well with an extremely small corpus.

2. Line 44 says: "However, naively performing fine-tuning [...] can lead to catastrophic forgetting issues, such as the loss of fluency in the translated sentences acquired during pre-training, thereby causing a reduction in translation performance". Can you share evidence of this? Typically, catastrophic forgetting doesn't cause a loss of *fluency* in NMT per se, but just poorer performance on seen domains.

3. It would be good to add a discussion of whether the EBMs increase the parameter size, memory footprint, or inference speed of the model.

4. Line 194 should cite the back-translation paper. Also, I would recommend including a comparison to back-translation as a baseline, and labeling "fine-tuned" as your upper bound.

5. I found the presentation of table 6 extremely confusing. It would be clearer to simply show the BLEU scores of the two models, rather than showing the difference between them. In addition, if you are testing for catastrophic forgetting, you should: a) show scores for the unadapted model for comparison, and b) evaluate on a domain seen by the original/unadapted model.

### Soundness
2

### Presentation
3

### Contribution
1
