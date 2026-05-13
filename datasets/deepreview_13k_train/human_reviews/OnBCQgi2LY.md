# Latent Feature Mining for Predictive Model Enhancement with Large Language Models

- Decision: Reject
- Scores: 3, 3, 5, 6

## Abstract
Predictive modeling often faces challenges due to limited data availability and quality, especially in domains where collected features are weakly correlated with outcomes and where additional data collection is constrained by ethical or practical difficulties. Traditional machine learning (ML) models struggle to incorporate unobserved yet critical factors. In this work, we introduce a novel approach to formulate latent feature mining as text-to-text propositional logical reasoning. We propose FLAME (Faithful Latent FeAture Mining for Predictive Model Enhancement), a framework that leverages large language models (LLMs) to augment observed features with latent features, enhancing the predictive power of ML models in downstream tasks. Our novel approach transforms the latent feature extraction task to a text-to-text propositional reasoning task. Our framework is generalizable across various domains with minimal domain-specific customization, ensuring easy transfer to other areas facing similar challenges in data availability. We validate our framework with two case studies: (1) the criminal justice system, a domain characterized by limited and ethically challenging data collection. (2) the healthcare domain, where patient privacy concerns and the complexity of medical data often limit comprehensive feature collection. Our results show that inferred latent features align well with ground truth labels and significantly enhance the downstream classifier.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper  proposes FLAME, a framework that uses LLMs for inferring latent features through text-based propositional reasoning. Its goal is to improve predictive models in data-limited domains. FLAME reframes latent feature extraction as a reasoning task, converting observed features into logical propositions that LLMs process to derive latent features. The framework formulates rationales, generates synthetic data, fine-tunes the LLM, and then infers latent features. In case studies from criminal justice and healthcare, FLAME outperforms traditional ML models.

### Strengths
The paper presents FLAME, a framework for enhancing predictive models by inferring latent features through large language models (LLMs) using text-based reasoning. The approach is novel in its application of LLMs to simulate expert-like reasoning in data-limited contexts, aiming to improve predictions in fields like criminal justice and healthcare. The quality of the work is solidly supported by experiments, though some reliance on domain-specific inputs could limit broader applicability. The framework is generally well-explained, although some technical descriptions, especially around the logical reasoning structure, could be clearer. Overall, FLAME offers a creative step towards improving model interpretability and performance in constrained data settings.

### Weaknesses
1. In safety-critical domains like criminal justice and healthcare, understanding causal relationships is what we actually need, including for predictive modeling. At the very least, to understand if the approach genuinely learns meaningful patterns or simply exploits spurious correlations, the models need to be tested on OOD data (as is common in this of literature within ML).

2. The ability of the LLM to uncover the "true" latent variables via prompting doesn't seem convincing. Maybe through latent variable modeling on the model's representation space we could learn something better. Alternatively, researchers working on these problems often use discovery methods like topic models or ideal-points models. More broadly, the social science literature is very aware of the limitations in using black-box ML for variable discovery.

3. Simply introducing LLMs into safety-critical domains without transparent guarantees does not align with how researchers in these fields approach variable discovery. Without understanding or validating what the LLM captures, this approach risks missing the mark on reliability and ethical standards essential for high-stakes decisions.

### Questions
1. Given that causal relationships are critical in domains like criminal justice and healthcare, how does the framework ensure that the LLM-generated latent features capture causally relevant information rather than exploiting correlations? 

2. The LLM-based prompting for latent feature discovery seems less principled compared to structured methods like topic models or ideal-point models. Could you explain why this approach was chosen and provide any empirical or theoretical comparison to these established techniques? 

3. Since the framework is intended for use in safety-critical domains, interpretability and reliability are essential. Can you provide more detail on how they validate the inferred latent features, especially when ground-truth labels for these features are not available? 

4. The paper claims domain flexibility, but it also seems FLAME relies on significant customization, especially in formulating baseline rationales. Could you clarify the extent of domain-specific adaptation required and discuss any general principles or guidelines for adapting FLAME to new domains? 

5. Given the sensitive nature of the target domains, could the authors expand on their ethical considerations? Specifically, are there safeguards to prevent biases from the LLM from impacting inferred latent features?

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
3

### Summary
This paper proposes an approach to the creation of latent features capturing aspects of data not directly observed. These aspects, termed latent features, are modeled from a given dataset using an LLM interaction framework involving the generation of rationales produced using principles from propositional logic and prompting techniques. The estimated latent features are then fed into a predictive model, where there is evidence of improved predictive performance in various case studies involving health care and criminal justice.

### Strengths
There are aspects of the paper I perceive to be strengths given my understanding of it. 

The translation step of unstructured text into predicates for LLM processing is clever. It bears some similarities to the DataTuner system but seems like a useful approach. 

I appreciate that the paper includes as clear baseline against which evaluations are performed. 

The case studies are drawn from diverse fields and seem to have practical importance.

### Weaknesses
There are aspects of the paper I perceive to be weaknesses given my understanding of it.

For example, the conceptualization of "latent feature" seems to be a bit contradictory at times. For example, in the DAG on p. 3 implies that "latent features" are to be mediators of X and its effect on Y. Later on (for example, in Figure 3, simple correlation (with bi-directional arrow) is postulated between latent and observed features). In the examples of (e.g.) Figure 2, there also seems to be potentially ambiguous causal ordering. It's unclear to me what the implications of this would be, but some of these questions regarding definition make the paper harder to interpret.

Also, in a way, traditional neural network models, with many hidden layers, are more or less entirely about modeling latent numerical variables. The approach here seems to be a specific way of generating human-interpretable latent variables from one neueral network model (in this case, an LLM), for improving performance on the original neural network task. It wasn't entirely clear to me why interpretability was important in these tasks...

More importantly, given my understanding of the paper, two major kinds of items are compared. First, input features X are used to predict Y. Second, input features are augmented with the latent values processed from X, and used to predict Y. The paper finds improved performance of the latter approach. However, this seems to me to be far from an apples-to-apples comparision, as in the first approach, (I believe) a very relatively neural model is fit (I couldn't find the exact parameter count). In the second approach, a muilti-billion parameter is used to generate features that the smaller neural model then uses. On this account, model scale alone makes interpretation of the results difficult.

I believe a stronger evaluation would be to employ equally sized neural models in the two arms of the experiment (forgive me if this is being done and I misunderstood the approach taken, in particular, in Experiment 1). I would be more convinced with some combination of the following. (1) Compare against a neural embedding of the structured data (perhaps using the general approach taken to render the X's amendable to LLM processing). This way, we would have a model with roughly the same number of parameters being used across arms, and we could better understand whether it was the specific way of generating Z's, or the general use of large-scale neural/LLM models that was generating improved performance over the baseline methods. (2) I would also be more convinced if performance were improved over simpler prompting-based strategies to generating outcome predictions (as this would be another way to employ the multi-billions of parameters to this task, rendering the comparision with the specific strategy used here more rigorious). The two approaches just described would involve similar levels of compute used for the other experiments already run, but would help put the results in context.

In general, a much simpler approach seems to be to use the LLM to generate direct predictions of the outcome, where it will form many latent representations internally. The prompts outlined in the Appendix do this for predicting the Z's (where here, there is ground truth data for the Z's, so these are in some of the applications observed nodes). The interpretability angle is important but can be difficult to define or defend; I don't seem to see much evidence directed towards this claim in the results section of the paper.

### Questions
What are the number of trainable parameters used in the MLPs trained here?

### Soundness
2

### Presentation
2

### Contribution
1

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a framework that leverages LLMs to augment observed features with latent features and enhance the predictive power of ML models in downstream tasks. Two situations about criminal justice system and healthcare validate the framework.

### Strengths
1. This work introduces human knowledge into existing domain text classification tasks, such as law and medicine, which can effectively improve the accuracy of downstream tasks and provide some interpretations.
2. This work provides a new idea for how to maximize prediction performance when data is limited, and it may inspire more related work.

### Weaknesses
1. The narrative angle of this work is very novel, but in my opinion, it essentially uses the human knowledge of LLM and CoT to complete the classification task of domain text， which lacks technical innovation.
2. The necessity of fine-tuning LLM need to be discussed more thoroughly. Fine-tuning LLM will cause it to lose most of its knowledge and multi-turn dialogue capabilities, and it will consume a lot of computing resources. A more reasonable approach is to train BERT-like models to classify the analysis generated by LLM. In particular, although the authors tried to fine-tune the LLM, it still failed to achieve better performance than the machine learning methods.
3. The necessity of components of the proposed method is unclear (for example, the necessity of reasoning). Being more specifically, the submission is lack of comparable baseline methods. The authors only verified that their method can achieve better performance than not using this method, but they do not compare with other methods that also utilize LLM knowledge for domain classification tasks. A simple baseline approach could be to use the LLM to directly generate an analysis of the question, and then use a text model (such as BERT) to classify both the question and the LLM analysis.

### Questions
1. I wonder if the author has considered the inconsistency of the content generated by LLM? There have been many studies [1] that have found that multiple prompt LLMs can generate inconsistent results, which may have a significant impact on the classification results.
- [1] Statistical knowledge assessment for large language models. NeurIPS 2023.

### Soundness
2

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
This paper presents FLAME (Faithful Latent FeAture Mining for Predictive Model Enhancement), a novel framework that leverages large language models (LLMs) to extract latent features from limited observed data to enhance predictive modeling. The framework addresses challenges in domains where data collection is constrained by ethical or practical limitations. The authors validate their approach through two case studies: criminal justice system and healthcare, demonstrating significant improvements in downstream prediction tasks.

### Strengths
- Novel Framework: FLAME presents an innovative approach to latent feature mining by leveraging LLMs' reasoning capabilities, distinguishing it from traditional methods.
- Practical Significance: The framework addresses real-world challenges in domains where data collection is limited by ethical constraints. The case studies demonstrate clear practical value.

### Weaknesses
 - Scalability Concerns: The framework requires domain expertise for Step 1 (formulating baseline rationales). While this leads to better results, it might limit scalability to new domains. The reliance on expert-defined rationales introduces a potential bottleneck, as the quality and completeness of these rationales directly impact the performance of the latent feature extraction. The framework's effectiveness is thus contingent on the availability of experts who can articulate comprehensive and nuanced rationales, which may not be feasible in all domains or for all problems.


### Questions
1. Could the authors provide more details about the computational requirements and runtime comparisons between FLAME and traditional approaches?
2. How might the framework perform in domains where expert knowledge is less readily available or more ambiguous?
3. Could the authors elaborate on how the framework might be adapted for streaming data or online learning scenarios?

### Soundness
3

### Presentation
3

### Contribution
3
