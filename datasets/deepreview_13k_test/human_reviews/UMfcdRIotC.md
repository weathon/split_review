# Faithful Explanations of Black-box NLP Models Using LLM-generated Counterfactuals

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
Causal explanations of the predictions of NLP systems are essential to ensure safety and establish trust. Yet, existing methods often fall short of explaining model predictions effectively or efficiently and are often model-specific. 
In this paper, we address model-agnostic explanations, proposing two approaches for counterfactual (CF) approximation.
The first approach is CF generation, where a large language model (LLM) is prompted to change a specific text concept while keeping confounding concepts unchanged. While this approach is demonstrated to be very effective, applying LLM at inference-time is costly. 
We hence present a second approach based on matching, and propose a method that is guided by an LLM at training-time and learns a dedicated embedding space. This space is faithful to a given causal graph and effectively serves to identify matches that approximate CFs.
After showing theoretically that approximating CFs is required in order to construct faithful explanations, we benchmark our approaches and explain several models, including LLMs with billions of parameters. 
Our empirical results demonstrate the excellent performance of CF generation models as model-agnostic explainers. 
Moreover, our matching approach, which requires far less test-time resources, also provides effective explanations, surpassing many baselines. 
We also find that Top-K techniques universally improve every tested method. 
Finally, we showcase the potential of LLMs in constructing new benchmarks for model explanation and subsequently validate our conclusions. Our work illuminates new pathways for efficient and accurate approaches to interpreting NLP systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes two methods for approximating Counterfactuals in a model-agnostic way. The first one is to utilize an LLM to change attributes during inference time. The second method is to find Counterfactuals through efficient matching. In order to allow efficient matching, the paper developed a novel language representation learning method specifically for encoding counterfactuals. Such representation is learned through contrastive loss that maximizes the similarity of approximate counterfactuals and minimizes similarities of misspecified Counterfactuals. Both methods achieve better performances than prior works. The paper also released a dataset for evaluating NLP explanation techniques.

### Strengths
1. The paper proposed an efficient and novel matching technique for finding Counterfactuals and provided strong theoretical and practical evidence that Counterfactuals are good explanations. 
2. Counterfactuals generated using this method are more order-faithful and comprehensive than prior work.
3. Detailed ablation study to demonstrate the effect of each component in the method.

### Weaknesses
1. The results are only on one dataset CEBaB. The experimental section would be more convincing if more experiments were done on a wider range of datasets. 
2. The concepts are pre-defined, which can be a limiting factor to the comprehensiveness of the Counterfactuals generated.

### Questions
1. If the matching candidate set doesn't exist, do you generate them given the concepts?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper investigates the use of large language models (LLMs) for creating counterfactual examples to explain NLP classification model predictions. Two methods are proposed. The first involves directly using LLMs to generate counterfactual examples, altering only one aspect/concept of the input while maintaining the rest. The second method entails a matching process to discover approximate counterfactuals from a pre-defined candidate set. The study reveals that the matching approach, utilizing a specially trained feature extractor, outperforms strategies using pre-trained LMs as feature extractors and other baselines in the CEBaB benchmark.

------------------------------------
Update after discussion with authors:

The discussion with the authors and the information provided in the updated manuscript made me more convinced of the applicability of the proposed methods, so I raised my score to 6.

### Strengths
1. The paper is overall well-written, with a well-defined research question;


2. In addition to direct counterfactual generation via the LLM, the authors introduce an efficient, matching-based approach for identifying approximate counterfactuals from a pre-defined candidate set. Though this method doesn't perform as well as the direct LLM generation, it outperforms past baseline methods and is considerably more efficient than employing the LLM directly for each instance. The exploration of how to efficiently generate counterfactual examples using LLMs is an intriguing aspect of the paper.

### Weaknesses
1.	

The paper mostly follows the setting of the work of CEBaB, including causal analysis, the approximated counterfactual method, and the evaluation. While some theoretical analysis is provided in Section 3.1, it mainly argues why the approximated counterfactual method which is initially proposed in the CEBaB is better than others. Underlining this, the first concern is that the paper's contribution appears to be limited to the proposal of two LLM-based approximated counterfactual methods that perform better in CEBaB's causal framework. Given the powerful ability of LLM, using it can better generate counterfactual examples (that only change one concept of the input while keep other aspects unchanged) is not very surprising.
 
The second concern is the limited applicability of the proposed matching method. The use of the matching method under the CEBaB setting requires pre-defined or pre-identified concepts/factors, such as Food (F), Service (S), Ambiance (A), and Noise (N) in restaurant reviews. However, these concepts may not always be available or readily identified in many real-world NLP scenarios. Given that the paper exclusively focuses on using LLMs to generate counterfactual examples in this particular setting, its broader applicability and contribution are questioned.

2.	

As indicated by the results in Table 2, the matching method (causal model) demonstrates only a slight improvement over the Approx baseline, especially when K=10. While the matching method is the most novel part of the paper IMO, the fact that its performance isn't significantly superior to the Approx baseline brings its practical importance into question.

In summary, the marginal performance improvement and the limited applicability of the 
proposed methods make me tend to reject the paper at this moment. 

However, I am open to further discussions and potential rebuttals from the authors that may address these concerns.

### Questions
See weaknesses.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper presents two methods for explaining the predictions of Natural Language Processing (NLP) models, focusing on the use of counterfactual approximations (CFs). The first is a Counterfactual Generation approach, where a large language model (LLM) is prompted to change a specific text concept while keeping others the same. The second is a Matching method that identifies text with similar properties within a dataset. The authors establish the value of approximating CFs for offering _faithful_ explanations and illustrate their techniques' applicability on several models. They further improve the ability to provide explanations using top-K matching. Furthermore, they highlight the potential of LLMs to create new benchmarks for NLP model explanations. The authors present theoretical and empirical evidence to support their research and propose further areas of study.

### Strengths
- This paper contributes to the field of NLP model interpretability by introducing two practical methods for model-agnostic explanations, which could improve our understanding of model predictions.
- The authors back their theoretical constructs with extensive experimental results, though the reliability of these methods depends on the specific conditions in which they are applied (such as access to a candidate set that offers good matching candidates).
- The concept of Order-faithfulness is an innovative criterion for explanation methods, potentially providing valuable insights into the relative impact of different concepts on model predictions, although it would need to be tested across various contexts and model types to ensure its broad applicability.

### Weaknesses
- The first method proposed, Counterfactual Generation, is computationally expensive and may be infeasible in scenarios requiring real-time explanations.
- Although Matching is faster than CF Generation, it might not be as accurate for all situations, especially when the matching candidate set does not sufficiently represent the input data. It would be great if the authors performed some ablation studies (reducing the quality of the matches in the candidate sets to show how much the performance degrades).
- It's unclear how these techniques would perform on models trained on very niche tasks, which could inherently limit the possible counterfactuals, especially where such attributes may be hard to define beforehand. Both counterfactual generation and matching approaches assume that we have a set of attributes for which we wish to examine whether a model is paying attention to those. However, how does this approach work for open ended tasks (which is where LLMs are primarily being used) or tasks with a large number of classes, where generating counterfactuals (or finding matches) may be inherently difficult?
- It's unclear how these methods would handle situations with multilayered complexities, such as nested counterfactuals, where counterfactual changes to one concept might trigger changes to other related concepts. The paper also does not extensively address scenarios where counterfactual approximations could result in impossibilities or logical contradictions, potentially limiting the breadth of their application.

### Questions
I would appreciate if the authors discuss the issues I brought up in the previous section.

Additionally, could you explain the difference between Random Match and Approx again? It's not that clear from the paper.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper focuses on improving causal explanations, specifically the counterfactual explanation. The authors propose to leverage LLMs to generate the counterfactual input corpus, use the generated corpus to train a counterfactual representation model, and match the input and its corresponding counterfactual representation to generate the causal explanations. Experiment results show that the authors' method outperforms all previous matching baselines, representing a promising explanation ability.

### Strengths
1. This paper provides detailed proofs and descriptions of the proposed method.
2. The experiment results are reliable with the comparison between various baselines and models.
3. The authors also construct a benchmark based on the findings of LLM's ability to generate counterfactual examples, which I think is a good contribution to the XAI community.

### Weaknesses
The description of the proposed method in Section 3 is confusing and not easy to understand. I think the authors should rephrase Section 3 with a general description of the proposed causal model. 

About Eq.(2), the authors use the difference in the model's prediction before and after the treatment as the treatment effect, which, in my opinion, is not robust when the model's output confidence is flat (or the uncertainty is high). This will affect the method's performance on small models like BERT.

### Questions
1. I cannot find an accurate definition of "causal model". Does the author use the representation generated by a language representation model optimized with Eq.(5) with generated counterfactual and matched examples, then calculate the matching value in Eq.(4), and use this value to calculate Eq.(2) as a causal model?

2. How does the generative approach work? If (1) is true, does the causal model include the generative approach?

3. There are two versions of ChatGPT (GPT-3.5 and GPT-4); which one did the authors use in the experiments?

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good
