# Counterfactual Causal Inference in Natural Language with Large Language Models

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 3, 5

## Abstract
Causal structure discovery methods are commonly applied to structured data where the causal variables are known and where statistical testing can be used to assess the causal relationships. By contrast, recovering a causal structure from unstructured natural language data such as news articles contains numerous challenges due to the absence of known variables or counterfactual data to estimate the causal links. Large Language Models (LLMs) have shown promising results in this direction but also exhibit limitations. This work investigates LLM's abilities to build causal graphs from text documents and perform counterfactual causal inference. We propose an end-to-end causal structure discovery and causal inference method from natural language: we first use an LLM to extract the instantiated causal variables from text data and build a causal graph. We merge causal graphs from multiple data sources to represent the most exhaustive set of causes possible. We then conduct counterfactual inference on the estimated graph. The causal graph conditioning allows reduction of LLM biases and better represents the causal estimands. We use our method to show that the limitations of LLMs in counterfactual causal reasoning come from prediction errors and propose directions to mitigate them. We demonstrate the applicability of our method on real-world news articles.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes an approach for causal discovery and counterfactual inference from unstructured natural language. The method uses LLMs to extract causal variables, build causal graphs, and conduct counterfactual reasoning based on these inferred structures. The authors introduce a two-step framework: first, they prompt the LLM to generate causal graphs by identifying relationships between events in the text, potentially merging graphs from various documents for broader coverage. Then, the inferred graphs are used to simulate counterfactual scenarios, allowing them to analyze and evaluate causal influences with an LLM. The authors conduct experiments on synthetic and real-world datasets to illustrate the model's ability to handle counterfactual queries and identify sources of inference limitations, primarily prediction errors in reasoning tasks. Through these experiments, the paper highlights limitations in current LLM capabilities regarding counterfactual reasoning and suggests that prediction errors are a significant bottleneck.

### Strengths
The main strength of the paper is in exploring how LLMs can support causal reasoning tasks on text data, pointing to new possibilities and practical challenges. The authors introduce a novel approach for discovering causal structures and conducting counterfactual inference directly from unstructured text using LLMs. 

The methodology is well-defined, with clear steps in building and merging the causal graphs. 

The experiments, both on synthetic and on real data, demonstrate the applicability of the framework.

### Weaknesses
1. The paper’s reliance on synthetic data from Cladder restricts its assessment of model performance in realistic contexts. The model is only demonstrated on a few real-world news examples, which doesn’t fully establish its applicability to unstructured text data beyond controlled scenarios.

2. Expanding the analysis to include diverse domains would provide a stronger basis for understanding the versatility and potential challenges fro the LLM-based approach.

3. The paper could benefit from quantitative performance metrics on real-world data (e.g., precision and recall for causal variable extraction, fidelity of counterfactual predictions).

4. The paper would be improved by addressing issues like hallucination and prompt sensitivity, as these can impact the accuracy of causal inference.

### Questions
1. Could you provide additional quantitative evaluations on real-world datasets beyond the limited examples in the paper? Specifically, metrics like precision, recall, or causal graph fidelity in real news articles or other domains.

2. Given the reliance on the synthetic Cladder data, do you see limitations in how well this dataset represents real-world causal complexity? 

3. How do you think the approach handles potential issues with LLM hallucination or prompt sensitivity?

4. The paper mentions that counterfactual inference accuracy is a primary limitation, largely due to prediction errors. Could you provide more details on specific failure cases?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper studies timely and important goal: how do we get AI systems to reason causally over natural text? They extend LLM results on inferring causal graphs to natural text datasets and perform counterfactual inference.

### Strengths
* The motivation of the problem and the datasets chosen are excellent. 
* Experiments are clearly described and ablations are provided

### Weaknesses
My brief review is that the authors have done a great job setting up the problem, but their results are underwhelming.
* The proposed method introduces a lot of complex parts, but is unable to outperform the causalCoT baseline from Jin et al.
* I do not get any new insight from the results, especially because all the validation is also done by LLMs. 
* While the idea is interesting, the paper's results fail to convince me that it works in practice. At least, we should see stronger results on the synthetic cladder benchmark.

### Questions
I have some questions below. I also provide feedback to improve the work, which the authors need not respond to.

Questions
* Is the graph generated per sentence? Or per paragraph?
* How are two graphs merged? Do you also use an LLM for this task? How do you handle variable name mismatches, mismatches in edge direction, etc,?
* How does the work relate to LLMs+causal representation learning? E.g.,this paper https://arxiv.org/abs/2402.03941
* Section 3.1 states that hidden variables are also extracted from LLM. How are they used in the causal analysis? In a dataset like cladder, does the LLM output hidden variables?
* The decision to simply ignore any questions where the LLM outputs an incorrectly formatted answer or other error is not fair. Can you present results on the entire cladder dataset? If the LLM failed to produce a valid graph, then it should be counted as a failure, since it is part of the proposed method.
* Can you think of any other validation apart from LLM self-validation? It's unclear what that evaluation is adding.

Suggestions to improve:
* I would suggest the authors to focus on cladder and show a demonstrable gain. Otherwise, it is even harder to interpret the real-world oil dataset results.
* I suspect that your method is trusting the LLM too much. Instead, once the graph is obtained, we can do many operations symbolically and invoke LLMs only for small, focused tasks. So I would encourage you to look into a direction where the central control is handled by the SCM and CF procedure and the modular atomic tasks are delegated to LLMs. Some iteration of this idea should easily give higher accuracies on cladder, assuming that the graph is correct.

### Soundness
4

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies causal discovery by using large language models to extract the causal graph from textual documents by prompting and perform sequence prediction. Experiments were conducted on both synthetic and more realistic datasets.

### Strengths
* The problem itself is of interest to a wide audience
* The idea of applying LLM to this problem may inspire more researchers

### Weaknesses
My main concern is that the contribution seems less significnat compared with what authors claimed -- in particular:

1. the main methodology, discussed in Section 3, might be summed up as prompting LLM and getting the results. I do not see novel ways of applying the LLMs to this specific problem (I agree there was effort in designing prompts to get the model generate a JSON-formated causal graph, but that seems not to be a significnat contribution), or insights/evidence of how this approach is better and in what ways.

2. There are assumptions needed for equation (1) to work and I don't see mentions/discussions on their validaity in this setup, nor do I see a clear definition on the variables used throught section 3. For example, in the unnumbered introduction paragraph of Section 3, I understand that the causal variables/nodes refer to as noun pharases while in Section 3.2 the main focus was to adjust the conditional probability of predicted probability of tokens. There is no discussion on how one is related to the other; for example, what do you try to quantify/estimate from $P(Y|do(x),x',y')$? How does it relate to say the example in the unnumbered introduction paragraph of Section 1 ("travel restrictions diminishes airlines companies revenues")?

3. Although I appreciate the authors' efforst in doing a relative thorough experimental studies using various LLMs. I do think the results warant more discussions. For example, in Table 1, it was noted that "Only extracted answers are shown," how many exactractions failed? Does it introduce systemic bias in the evaluation?

### Questions
In addition to several questions I asked in the Weaknesses section --

1. Can you elaborate what variables are being intervenes and what causal effects are being studied in Section 3.2 when you write $P(Y_0|C)$ and how does this (the conditional probability of an output token $Y_0$) relates to the causal question you are trying to study?

2. In Section 3.2, the authors wrote " Due to their extensive training on a massive amount of data, LLMs are good estimators," I don't see why this necessarily implies they are also good estimators when you replace the contexts (tokens) by causal variables (say $x'$). Can you provide more details?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
They explore the challenges and potential of using large language models (LLMs) to infer causal relationships from unstructured text data, such as news articles. Then they present a method for discovering causal structures and conducting counterfactual causal inference using LLMs. They propose a pipeline approach: 
1. They first use an LLM to extract the instantiated causal variables from text data and build a causal graph;
2.  Then they merge causal graphs from multiple data sources to represent the most exhaustive set of causes possible; 
3. Finally, they conduct counterfactual inference on the estimated graph. 

I think the paper is well-written. However, the main and only concern for me, for each of the aforementioned step above, they are many works already. To name a few: 
+ Causal discovery with LLMs: (i) Efficient Causal Graph Discovery Using Large Language Models; (ii) Causal Graph Discovery with Retrieval-Augmented Generation based Large Language Models
+ Counterfactual inference with LLMs: (i) Using LLMs for Explaining Sets of Counterfactual Examples to Final Users; (ii) Do Models Explain Themselves? Counterfactual Simulatability of Natural Language Explanations


This work is more like a combination of different causal tasks with a novel end-to-end method. I admit there are merits for this end-to-end method but I think more discussion on the related work is necessary. I am open to other reviews' opinions about the novelty. 

For this paper's soundness, I think this paper is well-written and the experiments are quite supportive.

### Strengths
1. The paper presents a novel approach by leveraging large language models to perform causal structure discovery and counterfactual inference from unstructured text.
2. The authors propose a comprehensive, end-to-end method that extracts causal graphs, performs interventions, and predicts counterfactual scenarios.
3. By incorporating causal graph conditioning, the method helps reduce biases inherent in LLM.

### Weaknesses
The main and only concern for me, for each of the aforementioned step above, they are many works already. To name a few:
+ Causal discovery with LLMs: (i) Efficient Causal Graph Discovery Using Large Language Models; (ii) Causal Graph Discovery with Retrieval-Augmented Generation based Large Language Models
+ Counterfactual inference with LLMs: (i) Using LLMs for Explaining Sets of Counterfactual Examples to Final Users; (ii) Do Models Explain Themselves? Counterfactual Simulatability of Natural Language Explanations

This work is more like a combination of different causal tasks with a novel end-to-end method. I admit there are merits for this end-to-end method but I think more discussion on the related work is necessary. I am open to other reviews' opinions about the novelty.

For this paper's soundness, I think this paper is well-written and the experiments are quite supportive.

The main weakness is listed in their Limitation section, I agree with their pointed limitation and like their honesty:
1. The counterfactual setting is mainly on synthetic datasets.
2. The method currently focuses on DAGs and does not account for feedback loops, which are common in real-world events.

### Questions
1. I think the existing content(experiment&writting) is very sound. But the novelty is not that clear to me. The end-to-end way is more like a pipeline for different phases of causal tasks with LLMs. Namely, for both causal graph discovery and counterfactual inference, there are already existing works that use LLMs for this task. But I admit the end-to-end framework proposed in this paper is nove. 
2. How do you validate the accuracy of the causal graphs generated by the LLMs, particularly when no ground-truth data is available for real-world scenarios? I guess this evaluation is based on synthetic datasets where the ground truth label is known?

### Soundness
3

### Presentation
3

### Contribution
2
