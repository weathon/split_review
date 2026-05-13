# Language Models are Advanced Anonymizers

- Decision: Accept
- Scores: 8, 5, 5

## Abstract
Recent work in privacy research on large language models has shown that they achieve near human-level performance at inferring personal data from real-world online texts. With consistently increasing model capabilities, existing text anonymization methods are currently lacking behind regulatory requirements and adversarial threats. This raises the question of how individuals can effectively protect their personal data in sharing online texts. In this work, we take two steps to answer this question: We first present a new setting for evaluating anonymizations in the face of adversarial LLMs inferences, allowing for a natural measurement of anonymization performance while remedying some of the shortcomings of previous metrics. We then present our LLM-based adversarial anonymization framework leveraging the strong inferential capabilities of LLMs to inform our anonymization procedure. In our experimental evaluation, we show on real-world and synthetic online texts how adversarial anonymization outperforms current industry-grade anonymizers both in terms of the resulting utility and privacy.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper introduces a novel approach to text anonymization in the era of large language models. The authors present two main contributions: (1) a new evaluation framework that leverages LLMs for adversarial inference to measure anonymization effectiveness, and (2) an iterative anonymization pipeline that uses adversarial feedback to guide the text anonymization process. This framework offers improvement over the traditional span based formulation as contextual information leaks information as well. The authors conduct extensive experiments with various models and demonstrate that their approach achieves better privacy-utility tradeoffs compared to traditional span-based anonymization techniques such Azure Language Services. In their results, performing the procedure reduces the adversarial inference chance from 87% to 66%, and iterating the procedure with GPT-4 for three rounds further reduces adversarial inference success to ~45% while maintaining higher text utility than baseline methods. They validate their results with human annotation.

### Strengths
- Novel approach that leverages LLMs' inference capabilities to measure privacy leakage in a more realistic way than traditional span-based methods.
- Comprehensive experimental evaluation across multiple models, attributes, and metrics, with clear ablation studies showing the benefit of the feedback-guided approach.
- Strong empirical results showing significant improvements over industry-standard tools like Azure Language Service, with detailed analysis of both privacy protection and utility preservation.
- Thoughtful consideration of practical concerns including computational costs, local deployment options, and regulatory compliance.
- Clear demonstration of how multiple rounds of anonymization can progressively improve privacy while maintaining readable text.

### Weaknesses
 - The ~41% remaining adversarial inference success rate after anonymization remains concerning for privacy-critical applications. The paper would benefit from deeper analysis of these failure cases, specifically examining the types of attributes that are still being inferred and the textual patterns that enable these inferences. A more granular breakdown of the remaining inference success, categorized by attribute type and certainty level, would be beneficial. It is unclear if this 41% represents a uniform distribution of inference success across all attributes or if certain attributes are more vulnerable than others.
- Limited domain evaluation, focusing primarily on data directly or indirectly from Reddit. Testing on other domains (medical, legal, etc.) would strengthen generalizability claims. It could also be reddit comments that mentions information from these domains. The current evaluation does not sufficiently address the potential for domain-specific biases in the adversarial models or the anonymization process. The linguistic patterns and contextual cues that reveal sensitive information may vary significantly across domains, and the method's effectiveness in these diverse settings remains unproven. For example, medical texts often contain structured information and specific terminology that may be more or less susceptible to adversarial inference than the informal language found in Reddit comments.
- The method requires pre-defining attributes to protect, which may miss unexpected privacy leaks. An automated approach to identifying sensitive attributes could be valuable. This reliance on a predefined list of attributes introduces a potential vulnerability, as it assumes that all relevant privacy concerns are known in advance. The system lacks a mechanism to detect and mitigate privacy leaks stemming from attributes that were not explicitly considered during the setup phase. This could lead to a false sense of security, as the anonymization process might overlook subtle but significant privacy violations. Furthermore, the process of manually defining attributes can be cumbersome and error-prone, especially in complex datasets with numerous potential privacy concerns.
- Cost analysis could be more comprehensive - while per-comment costs are reasonable (~$0.035), real-world applications with high volume could face significant expenses. In addition, the estimate is only for one turn, so to achieve the same level of privacy protection, this number might be more expensive. The current cost analysis lacks a detailed breakdown of the computational resources required for each stage of the anonymization pipeline, including the adversarial inference and the iterative refinement process. It is unclear how the cost scales with the size of the input text, the number of attributes being protected, and the number of iterations. A more thorough analysis of the computational complexity and resource requirements would be valuable for assessing the feasibility of deploying this method in real-world scenarios.

### Questions
- Have you explored methods to automatically determine the optimal number of iterations, perhaps based on inference confidence?
- How does the system perform when encountering privacy-sensitive attributes not explicitly listed in the input? Could it be extended to automatically identify such attributes?
- Can you provide specific examples of common failure cases where privacy leaks persist even after multiple rounds of anonymization? Understanding these patterns could help improve the approach.
- Have you considered how this approach might need to be adapted for different domains with varying privacy requirements and linguistic patterns?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this work, the authors focus on the privacy scenario where online texts can be exploited to infer personal data. The authors utilize adversarial LLM inferences, which are highly performant in extracting personal attributes from unprotected texts, for evaluating anonymization and also use this adversarial model as "feedback provider" to another LLM whose goal is to anonymize texts. An iterative framework between these two LLMs lead to strong anonymization performance as shown by the authors in wide range of experiments, outperforming existing anonymizers and also aligning well with human preference.

### Strengths
The presentation is very clear and the paper flows very well. Text anonymization is an important problem in the realm of privacy and the approach the authors introduce do improve the existing anonymization tools significantly. The evaluation section has extensive analysis, which is great. The reviewer really enjoyed reading this paper overall.

### Weaknesses
In my opinion, the paper is very well written and the authors conducted extensive empirical studies to demonstrate the significant improvement of their approach compared to the existing text anonymization tools. I think my main concern is the scope and complexity of the approach appear quite limited, especially for a conference of this caliber. The approach is based on iterating two LLMs, one is anonymizing text and the other is trying to infer personal attributes. To me, this is like a cute application of LLMs but perhaps rather better suited for a workshop instead of this conference. In this sense, I am unsure about the fit. The core methodology, while effective, lacks substantial novelty in terms of algorithmic contribution. The iterative process between two LLMs, while demonstrating practical improvements, does not introduce a fundamentally new approach to machine learning or privacy-preserving techniques. The reliance on existing LLM architectures and their iterative application, without introducing novel training methods or architectural changes, limits the theoretical contribution of the work. The approach seems more like an application of existing tools rather than a significant advancement in the field.

### Questions
1. Have you considered measuring utility by some downstream applications? E.g. if the texts are used for some analysis or for some task, how the performance changes from the original unprotected texts to the anonymized texts. Would you think this could also serve for useful utility metrics?

2. How can one turn this approach into a more comprehensive privacy-protecting tool? To my understanding, it currently builds on pre-defined set of attributes and the adversary LLM is trying to infer these attributes while the anonymizer LLM is trying to anonymize as oppose.  But it'd be hard to list all possible attributes that could lead to deducing personal information so any comments on scaling this approach would be appreciated.

3. Also related to my question above, formal privacy guaranteeing mechanisms like differential privacy ensures that even the existence of the data cannot be inferred from the analysis by any adversary. Although in this work the authors focus on anonymizing individual text snippets so that DP may not be applicable, however, it'd be interesting to find a common scenario where two approaches can be compared I think.
 
Minor: AzureLanguageService -> Azure Language Service

### Soundness
4

### Presentation
4

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
This paper proposes a LLM-based adversarial anonymization framework to address privacy risks. The authors use a feedback-guided approach where an LLM adversary attempts to infer personal attributes from a given text, and an anonymizer LLM iteratively modifies the text to reduce inference risks. The paper evaluates this method against traditional anonymization techniques and demonstrates superior performance in both preserving utility and privacy across several datasets.

### Strengths
1. The proposed adversarial anonymization framework leverages the strengths of LLMs both as adversaries and anonymizers, showcasing a new application of LLMs in a privacy-preserving context.
2. The inclusion of a human study adds value to the evaluation by confirming the practical applicability of the framework and showing a preference for the LLM-anonymized text.

### Weaknesses
While this might be an interesting application of LLMs to the field of anonymization, the core methodology introduces neither fundamentally new anonymization techniques nor a different way to use LLMs. It merely adapts existing concepts by leveraging the powers of LLMs. Thus, the contribution of novelty is limited for either the LLM or the privacy community.

One major limitation is that, in real life, texts to anonymize are normally very long, and due to the current method, which would be prohibitively expensive, it is practically not feasible in applications that demand real-time processing. The scalability and applicability of this framework are rather limited due to the enormous amount of documents it may need to work with iteratively. Another limitation is that privacy performance remains unpredictable due to heavy dependence on the capabilities of the LLM. This creates a dependency where consistency of anonymization outcome cannot be guaranteed and may even differ from model to model or update to update.

### Questions
1. Could you provide more examples where the framework fails and explain why the LLM is unable to recognize these instances?
2. Do you think it’s feasible to distill this capability into a smaller model? in this way, we can reduce the computational cost.

### Soundness
3

### Presentation
3

### Contribution
2
