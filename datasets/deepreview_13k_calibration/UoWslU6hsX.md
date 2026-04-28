# 100 instances is all you need: predicting LLM success by testing on a few instances

- Decision: Reject
- Avg Score: 4.33
- Scores: 5, 5, 3

## Abstract
Predicting if LLMs will succeed on individual task instances (i.e., prompts) is essential to ensure their reliability in high-stakes applications. To do so, we can evaluate a LLM on a set of instances and train an "assessor" to predict its performance. However, this requires evaluating each new LLM on sufficiently many instances. In this work, we build a "generic assessor" predicting the performance of any LLM on an instance by using the LLM's performance on a small set of reference instances and the features of the considered instance. In practice, we make use of existing evaluation results to extract the representative instances and train the assessor. Thus, the performance of a new LLM can be predicted by only testing it on the reference instances, leveraging the information contained in other LLMs' evaluations. We conduct empirical studies on HELM-Lite and KindsOfReasoning, a new collection of existing reasoning datasets that we introduce, where we evaluate all instruction-fine-tuned OpenAI models until $\texttt{gpt4-0125-preview}$. We find that a few instances (around 100) are enough to achieve predictive power comparable to the LLM-specific assessors trained on the complete set of several thousand instances. Interestingly, randomly selecting the reference instances performs comparably to the advanced selection methods we tested. Finally, we identify a sharp drop in the predictive power of the generic and specific assessors in out-of-distribution scenarios, suggesting that the inherent predictability of LLMs is low.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper explores a framework for predicting the performance of large language models (LLMs) on new tasks by using a generic assessor based solely on observational features of the dataset instances. With the rapid release of new LLM versions, traditional methods for evaluating their correctness can be resource-intensive. The authors propose characterizing each LLM by its performance on a small set of reference instances, allowing for efficient predictions without extensive evaluations. Their studies suggest that this generic assessor performs comparably to specific assessors within the same task distribution, though its effectiveness declines in out-of-distribution scenarios. Additionally, the research introduces the "KindsOfReasoning" dataset to support evaluations of reasoning capabilities across various models. Overall, the study provides insights into LLM validation and the potential for more streamlined assessment methodologies.

### Strengths
- The paper presents a novel framework for predicting LLM performance using a generic assessor, addressing a critical challenge in the fast-evolving landscape of large language models.
-Empiric validation of the proposed methodology demonstrates that the generic assessor can achieve results comparable to specific assessors, offering a more efficient alternative for performance evaluation.
- The research contributes to the understanding of generalizability by highlighting the limitations of predictive power in out-of-distribution scenarios, prompting further investigation into LLM behavior across diverse tasks.
- The introduction of the "KindsOfReasoning" dataset enhances the available resources for future research, providing a valuable compilation of reasoning tasks that can stimulate further exploration in LLM capabilities.

### Weaknesses
 - L340: “To the best of our knowledge, this is the first collection of instance-level results covering all versions of a given model family”. I believe this claim should be softened. There’s quite the history of releasing completions for models before (LiveBench and numerous huggingface repositories for example). This doesn’t deminsh the importance of your releasing these completions — I think that’s great — but it isn’t as strong of a separator of your work as you may be thinking. 
- I believe a fuller description of “KindsOfReasoning” should be included in the main body of the paper. I don’t think it is sufficient to just describe it as _comprised of reasoning tasks for existing datasets_. I would suggest at least a paragraph or two about its construction. Also Appendix B does not include any reasoning for how these data were included and other data excluded from the set, and important consideration. Finally, I’d like to learn more about what validation you did about the questions, prompts, etc to ensure the collection of data were covering topics of interest, not duplicative, and stylistically aligned. You could pick up space here by removing some of the more well-known and basic parts of machine learning which you explain in great detail: train-val-test splits, AUC, etc.
- “the latter two generate a vector for each word in the prompt, which we average to form a vector representing the entire prompt” this seems like it removes a lot of information. Can you talk about other methods you could have or did try and why this approach was taken?
- L422: “pick the one with the highest value”. I have a serious concern with this. Can you describe why this is the approach taken and not reporting each individual model performance, as I think is much more standard int he community? I realize it may have to do with how you envision this approach working in practice, but please explain this (to me) non-standard model-selection method given my understanding of the task at hand. 


Minor points:
- (This is slightly more significant than “minor”.) I think the use of the term “instance” is somewhat non-standard in the entirety of the community. As I understand it, you mean “instance” to refer to a (prompt, answer) pair. If this is the case, (and even if it isn’t), I suggest defining this term very early in the introduction (maybe even abstract) to make it clear to the diverse set of readers of your paper. 
- I suggest splitting the paragraph starting at L159 into several smaller paragraphs for easier reading. Perhaps at L166: “Closer to our work…” and L178: A similar work to Polo…”.

Typos: 
- L120: “use cases.Following”
- L428: I think you want \citep not \citet (parenthetical cite for Kuspati et al)
- L468: simpler -> simple

### Questions
See weaknesses

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a method to predict the performance of a new LLM on individual task instances using only a small set of reference instances (approximately 100). The authors introduce a framework that leverages existing evaluation results from multiple LLMs to build a generic assessor. This assessor combines the new LLM's performance on the reference instances with intrinsic features of the task instances to predict performance on new instances. The method is evaluated on two datasets: HELM-Lite and KindsOfReasoning collection, which covers various reasoning tasks. Experiments involve several OpenAI models. The findings suggest that the generic assessor can predict the performance of new LLMs with accuracy comparable to a specific assessor trained on full datasets in in-distribution scenarios. However, the predictive power declines significantly in OOD settings, indicating limitations in generalizing across different data distributions.

### Strengths
* **Relevance to Current Challenges:** The paper addresses a practical and pressing issue in NLP—efficiently predicting LLM performance without extensive evaluation on large datasets.

* **Innovative Framework:** Introduces a novel framework that combines a small set of reference evaluations with instance-specific features to build a generic assessor capable of predicting LLM performance on new instances.

### Weaknesses
 * **Limited Novelty and Contextualization:** The proposed method shares similarities with existing approaches, such as benchmark subsampling strategies and TinyBenchmarks. The paper does not sufficiently compare with or differentiate itself from these methods, which limits the perceived originality.
* **Insufficient Analysis of OOD Performance:** While the significant drop in predictive performance in out-of-distribution scenarios is acknowledged, the paper lacks a thorough analysis of the causes and potential solutions to mitigate this issue.
* **Methodological Clarity:** Some methodological details are not fully elaborated, such as the specific algorithms and parameters used for clustering and factor analysis in reference instance selection. The criteria for choosing hyperparameters and classifiers are also not described in depth.
* **Reliance on Proprietary Features:** The use of OpenAI embeddings as instance-specific features may limit the generalizability and accessibility of the method, particularly for those without access to these embeddings.
* **Evaluation Scope:** The experiments focus on tasks with binary correctness metrics. The applicability of the method to tasks with more complex or continuous evaluation metrics is not explored, which limits the understanding of its generality.
* **Insufficient Quantitative Comparison with Baselines:** The paper lacks detailed quantitative comparisons with existing methods, making it difficult to assess the advantages or disadvantages of the proposed approach in terms of predictive accuracy and computational efficiency.

### Questions
1. **Comparison with Existing Methods:** How does your method quantitatively compare with existing approaches like TinyBenchmarks or IRT-based methods in terms of predictive accuracy and computational efficiency? Including such comparisons would strengthen the paper and clarify its contributions relative to prior work.
2. **Improving Out-of-Distribution Performance:** Have you considered techniques to enhance the predictive performance in out-of-distribution scenarios, such as incorporating domain adaptation methods or training on more diverse datasets? A deeper analysis of the factors contributing to the OOD performance drop would be beneficial.
3. **Exploration of Alternative Instance Features:** Did you experiment with other types of instance-specific features that are publicly available and model-agnostic, such as linguistic or syntactic properties? Exploring alternative features could improve generalizability and reduce reliance on proprietary embeddings.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors conduct new empirical studies of generic assessor models, which are trained to predict the performance of any LLM on an instance by using the LLM’s performance on a small set of reference instances and the features of the considered instance, making use of existing evaluation results to extract the representative instances and train the assessor.

The authors find that a few instances (around 100) are enough to train assessors with predictive power comparable to the LLM-specific assessors trained on the complete set of several thousand instances. Interestingly, randomly selecting the reference instances performs comparably to the advanced selection methods.

The authors identify a sharp drop in predictive power of the generic and specific assessors in out-of-distribution
scenarios, suggesting that the inherent predictability of LLMs is low.

### Strengths
1. The authors introduce a new metadataset, KindsOfReasoning, which may be useful for future work. 
2. The sharp drop in predictive power of the generic and specific assessors in out-of-distribution scenarios should give evidence for future works as to the limited utility of assessors for complex foundation models.
3. The related works section is reasonably comprehensive.

### Weaknesses
1. The authors take it as a given that their choice of subject is high impact enough for this venue, and novel enough to require no experimental baselines, only ablation experiments on the construction of the assessor model. However, the evidence supporting this assumption is dubious.

Circa lines 39-40 (the line numbers are not aligned with the text lines), the authors cite 5 works developing assessors, but three of the papers the authors cite describe topics other than assessor models. https://arxiv.org/abs/2309.15789 describes learning a "router" model over tasks for LLM selection; optimally pairing tasks with a fixed pool of LLMs. In other words, it is not an assessor because it does not meet the requirements (it does not predict at an instance level). https://arxiv.org/abs/2107.11277 is a survey on ML with a reject option, a related but distinct topic. https://ieeexplore.ieee.org/abstract/document/10650424 is a methods paper on ML with a reject option. The authors acknowledge as much in Sec. 2.1, where they argue that instance-level prediction of success unifies these works. But then why are they cited as continuing a line of work on assessor models? This is, at best, confusing.

Of those works that do discuss assessor models, https://ojs.aaai.org/index.php/AAAI/article/view/21487 appears to be the first and claims to have originated the topic. The paper is 4 pages long, with minimal experiments. Essentially, it is a position paper, arguing that such models might have value as a conceptual class. https://ceur-ws.org/Vol-3169/paper4.pdf, from many of the same authors, follows it up with a more extended investigation.

In Table 1 of https://ojs.aaai.org/index.php/AAAI/article/view/21487, the authors cite 5 desiderata for assessor models:

**Anticipative**. It is essential that an assessor is able to predict performance before a system is dispatched, even in areas it has never been used. 

**Standalone**. An assessor must work independently from the original system, not requiring access to the system or its outputs. 

**Granular**. An assessor must predict at instance granularity, and reflect that some situations are easier than others. 

**Behavioural**. An assessor must learn representations of the emergent behaviour of the system, without access to system internals (black box approach). 

**Distributional**. An assessor’s predictive power will come from populations of (related) systems, but also aggregating estimates conditioned to distributions.

There are robust and extensive areas of study, such as reward models in RL and uncertainty quantification in ML, that fulfill many of these criteria, as well as a half-dozen other overlapping metrics and fields described in https://ojs.aaai.org/index.php/AAAI/article/view/21487. On top of all of that, the authors of this work devote nearly 1.5 pages to related work, much of which closely overlaps with assessor models.

Despite having perhaps hundreds of potential strong baseline methods to compare against, the authors compare their work only to their own constructed assessor baselines, more akin to ablation studies. And even so, many of their findings are negative.

2. KindsOfReasoning is a metadataset; thus, its value as a novel contribution is limited.

### Questions
Why is it necessary to establish assessor models as a distinct field of inquiry, given the many related fields which largely overlap with them?

Why do the authors not compare their method to the many existing baseline methods for predicting the performance of models?

### Soundness
2

### Presentation
3

### Contribution
1
