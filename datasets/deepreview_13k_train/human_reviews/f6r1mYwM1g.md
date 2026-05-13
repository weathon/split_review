# Capability Localization: Capabilities Can be Localized rather than Individual Knowledge

- Decision: Accept
- Scores: 6, 6, 5, 6

## Abstract
Large scale language models have achieved superior performance in tasks related to natural language processing, however, it is still unclear how model parameters affect performance improvement. Previous studies assumed that individual knowledge is stored in local parameters, and the storage form of individual knowledge is dispersed parameters, parameter layers, or parameter chains, which are not unified. We found through fidelity and reliability evaluation experiments that individual knowledge cannot be localized. Afterwards, we constructed a dataset for decoupling experiments and discovered the potential for localizing data commonalities. To further reveal this phenomenon, this paper proposes a Commonality Neuron Localization (CNL) method, which successfully locates commonality neurons and achieves a neuron overlap rate of 96.42% on the GSM8K dataset. Finally, we have demonstrated through cross data experiments that commonality neurons are a collection of capability neurons that possess the capability to enhance performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
The manuscript investigated the storage of individual knowledge in model parameters, and proposed a Commonality Neuron Localization method that locates commonality neurons.

### Strengths
1. The manuscript conducts experiments of previous knowledge localization methods and demonstrates those methods lack reliability and fidelity. The finding is insightful to the community.
2. The manuscript proposed a method that can effectively identify those neurons that embody the model capability, which help the understanding of large-scale neural networks.

### Weaknesses
1. It is unclear to me what the author means by "commonality". And what is its relation to knowledge localization?
2. Figure 2 is blurry.
3. In line 182, $e_i$ seems to be undefined.
4. Missing reference in line 216.
5. The role of section 4 and its connection to the rest of the manuscript is not clear. Specifically, the conclusion of section 4 and how it informs the subsequent sections is ambiguous.

### Questions
1. line 344, "we expand the KN method", what is the key improvement of CNL compared to KN?
2. What is the conclusion of Table 2?
3. The method successfully identifies those commonality neurons that embody the model capability. However, why is finding these neurons useful? For example, do we have any insights from analyzing the characteristics of the commonality neurons?

### Soundness
2

### Presentation
1

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
This  paper explores the idea of localising “capabilities” within LLMs, rather than “individual knowledge”. The argument is that (existing methods for localizing) individual knowledge is unreliable. For instance, the authors show that current methods like parameter layers and chins are perfectly faithful to individual knowledge. For example, rewriting semantically similar prompts did not lead to consistent localisation results, and manipulating identified parameters did not reliably produce expected changes in model behaviour.

Instead the paper forwards a new framework for localizing “commonality neurons”, the neurons that represent shared attributes or capabilities across datasets. They introduce the **Commonality Neuron Locating (CNL) method** which identifies neurons that consistently activate for similar tasks or data types. The paper concludes that capabilities can be localised within LLMs, potentially leading to new ways of understanding and manipulating LLM functionality

### Strengths
1. The paper is clear and well motivated. It clearly showcases the existing methods for understanding LLMs and their limitations.
2. The paper also addresses an important question in LLM research. How LLM parameters relate to their performance is topical. The paper challenges the existing methods providing compelling evidence. 
3. The paper also introduces a way of plugging those gaps. The CNL approach is a clear structured approach and inspired by well-grounded methods like integrated gradients from CV.

### Weaknesses
1. The usage of arbitrary thresholds (magic numbers): The study uses a threshold of σ = 6 for identifying capability neurons without sufficient justification or exploration of alternative values. This threshold is critical because it directly impacts which neurons are considered significant for a given capability. The paper lacks a sensitivity analysis to show how the results change with different values of σ. The choice of σ=6 seems particularly high, potentially excluding many relevant neurons and leading to a biased view of capability localization. A more rigorous approach would involve testing a range of σ values and demonstrating the stability of the identified neurons and their impact on model performance.
2. The decoupling experiment  to investigate the localisation of commonalities, primarily focuses on mathematical tasks. This narrow scope limits the generalisability of the findings regarding the potential for localising data commonalities. Expanding the decoupling experiment to include tasks from other domains, such as emotion recognition or language understanding, is crucial for supporting broader claims about the relationship between data commonalities and parameter localisation. The current focus on mathematical tasks might not capture the complexities of other types of reasoning or knowledge representation within LLMs. For instance, tasks involving natural language understanding or common-sense reasoning might reveal different patterns of neuron activation and localization.
3. The study shows that enhancing localised neurons leads to performance improvements, but the statistical significance of these improvements is not adequately assessed. Merely stating that the located neurons are "most sensitive" to performance improvement without providing statistical evidence leaves the strength of this claim open to question. The lack of statistical analysis makes it difficult to determine whether the observed performance gains are due to the identified neurons or simply random fluctuations. A proper statistical analysis, including confidence intervals and p-values, is needed to validate the significance of the performance improvements.
4. The biggest weakness though is the glaring lack of common evaluation metrics. The study evaluates different knowledge localisation methods (ROME, KN, KC, and CNL) using distinct metrics tailored to each method's specific assumptions. Establishing a shared metric that can be applied consistently across all methods would enable a more objective and informative evaluation. Such a metric could consider factors like the accuracy of knowledge localisation, the granularity of identified parameters, and the impact on model performance when manipulating identified parameters. Without a common metric, it is impossible to directly compare the effectiveness of CNL against existing methods.

### Questions
1. The authors should provide justification for the specific hyperparameters chosen and clarify the methodology in more detail. For instance, in Section 5.1, line 352, why is S=19? Was this value selected through a hyperparameter sweep? If so, please include these details in the appendix. Similarly, in Section 5.1, line 358, why is the attribution score threshold set at σ=6? Offering detailed steps for identifying commonality neurons is essential to ensure that the results are not cherry-picked. This transparency will also help reproduce the findings independently.
2. For the random-neuron conditions in the “enhance” and “erase” experiments ([Table 2] and [Table 3]), did you evaluate across multiple random samples to ensure statistical robustness? If so, please indicate the number of samples tested; without this, the reliability of comparisons with targeted neurons remains unclear.
3. We need some more control conditions to convincingly demonstrate the impact of commonality neurons. For instance, a comparison with multiple sets of randomly selected neurons, averaged over several trials, would help determine if performance changes are indeed specific to commonality neurons rather than general effects from a neuron subset. Testing different thresholds for neuron activation and varying the size of neuron groups would also clarify whether the observed effects are specific to the identified commonality neurons. Such controls would strengthen the claim that these neurons contribute uniquely to model capabilities rather than reflecting random network fluctuations.
4. By far the biggest thing missing from the paper is a common metric for comparing different methods. It is crucial to benchmark CNL against established knowledge and capability localization methods, such as distributed parameters, parameter layers, and parameter chains. This comparison should involve measuring CNL’s accuracy, consistency, and computational efficiency relative to these approaches in reproducible way such that improvements can be tracked carefully. 

5a. Another major concern is the scalability of CNL. There are at least 3 issues with model scalability and the authors need to discuss (or even better perform new tests) the scalability strategies of CNL.  A) As new models grow larger (e.g., from billions to hundreds of billions of parameters), the CNL method’s neuron-level analysis could become computationally prohibitive. 

5B. Larger models might need different threshold and hyperparameter sweeps to maintain CNL’s accuracy which demand additional tuning efforts. 

5C. CNL relies on extensive data from various domains to identify commonality neurons. As model sizes increase, the amount of data needed for localization will also grow. 

6. The authors should clarify how capability localization could enhance model interpretability in practical applications. It remains unclear whether the CNL approach addresses the theoretical question of how information is localized within the model or if it offers actionable changes for real-world LLM applications. Specifically, the authors should explain how identifying capability neurons could be leveraged to improve model performance, robustness, or transparency in practical scenarios. Without clear guidance the potential of using CNL in real-world settings is ambiguous.
7. While the paper includes extensive mathematical notation and text, the figures are under-explained and hard to follow. For instance, it is unclear what Figure 1 is intended to convey, the purpose of the red boxes in Figure 3, or the significance of the colors in Figure 4. The authors should enhance these figure descriptions to make the visuals more accessible and informative for readers, clearly explaining all elements, symbols, and color schemes. This will improve readability and ensure that the figures effectively support the paper’s findings.

### Soundness
2

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work introduces a Commonality Neuron Localization method as an alternative approach to overcome weaknesses of current methodologies in identifying and locating individual factual knowledge in large language models (LLMs) parameters.

After showing that current algorithms that localize individual knowledge do not respect fidelity and reliability requirements, the authors propose a metric to identify capability neurons for a given dataset based on a gradient attribution score of model parameters.

For some datasets, the authors show that Commonality Localization can be related to the performance of the model by showing that enhancing or erasing their role affects the results of the model on the dataset downstream task.

### Strengths
The authors propose a change of perspective to address the current limitations of techniques that attempt to localize individual knowledge in LLMs parameters. They propose to focus on a coarser localization task that focuses on common traits specific to a dataset and task.

### Weaknesses
The conceptual differences and limitations that incur when replacing individual knowledge location with "commonality neurons" are not sufficiently discussed. These are radically different procedures, with extremely different potential applications. The authors should thoroughly justify why it is relevant to localize phenomena at a much coarser level.

A more thorough discussion of the definition of attribution score would be beneficial, accompanied by a comparison to existing choices for attribution score appeared in the literature.

In the current form, the mapping between commonality neurons and capability is conjectural (see line 525-526). This is not coherent with the current main statement of the work "the located neurons embody the collection of capabilities".

It is not clear from the results if "Existing technology cannot localize individual model parameters" (line 71) or if "Individual knowledge cannot achieve parameter localization" in general. Clarifying this would be beneficial.

In order to support the claim that "the located neurons embody the collection of capabilities" it should be at least clarified explicitly which capabilities the authors are referring to. In particular, it should be stressed which of the quantitative results in Section 6 support the existence of the specific "common capabilities".

The results of Subsection 5.4 (in particular "Commonality across datasets") should be explained with more care.

The paper could be largely improved in terms of clarity and quality of the presentation:
- extended and more precise Figure captions would help clarify results;
- the role of section 4.2 is not clear given the current form of the paper;
- in formula (8), line 329, the parameter sets $P_s$ should be clearly defined;
- in several circumstances, the authors use terminology incoherent with scientific rigor (e.g. "believes" or "ideologically" referring to existing literature);
- there are several typos and incomplete sentences in the current version.

### Questions
It is not clear from the results if "Existing technology cannot localize individual model parameters" (line 71) or if "Individual knowledge cannot achieve parameter localization" in general. Clarifying this would be beneficial.

In order to support the claim that "the located neurons embody the collection of capabilities" it should be at least clarified explicitly which capabilities the authors are referring to. In particular, it should be stressed which of the quantitative results in Section 6 support the existence of the specific "common capabilities".

The results of Subsection 5.4 (in particular "Commonality across datasets") should be explained with more care. 

The paper could be largely improved in terms of clarity and quality of the presentation:
- extended and more precise Figure captions would help clarify results;
- the role of section 4.2 is not clear given the current form of the paper;
- in formula (8), line 329, the parameter sets $P_s$ should be clearly defined;
- in several circumstances, the authors use terminology incoherent with scientific rigor (e.g. "believes" or "ideologically" referring to existing literature);
- there are several typos and incomplete sentences in the current version.

### Soundness
2

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors verify the assumption that knowledge is localized in the model parameter space by evaluating existing methods on a synthetically generated dataset. They falsify this assumption and instead argue that capabilities are localized in model weights and layers instead. Subsequently, the authors propose the Commonality Neuron localization method to find neurons that have commonalities within a variety of datasets. By manipulating these neurons, they causally show that the identified neurons that make up only 0.15% of the parameters significantly affects model performance.

### Strengths
-- assessed 3 existing methods to verify knowledge representation in neural networks
-- developed a new method to categorize neurons that are selective to similar information to influence performance
-- The decoupling dataset and experiments are informative.
-- The authors used a wide variety of datasets (math, program, language) to evaluate their proposed CNL method.
-- the authors demonstrated that fine-tuning commonality neuron improved performance within and across datasets, demonstrating their casual role in performance.

### Weaknesses
 -- for Section 3.1 and 3.2, the authors used GPT4o to generate samples with the same semantic and attempted to identify localized representations in GPTJ. It will be informative to generate samples using GPTJ and verify localization methods on the same model i.e. GPTJ only. If this similarly shows low localization, it would further support the authors' claim. 
-- The authors used GPT4o to rewrite 1000 factual statements to populate the factual dataset. How did they verify that the new samples have the same semantic meaning?
-- Why did the authors not evaluate the CNL method on the same dataset i.e. Table 1, that was used to evaluate previous methods?
-- Authors should include the baseline performance of the model without any fine-tuning in Table 2 as in Table 3 for comparison. Is there a claim the authors are making with respect to Table 2?

### Questions
-- what is the difference between knowledge and capabilities? 
-- Fig 2 is missing its x axis label. I am guessing it is the layer number?

### Soundness
3

### Presentation
3

### Contribution
3
