# Copyright-Protected Language Generation via Adaptive Model Fusion

- Decision: Accept
- Avg Score: 7.50
- Scores: 6, 8, 8, 8

## Abstract
The risk of language models reproducing copyrighted material from their training data has led to the development of various protective measures. Among these, inference-time strategies that impose constraints via post-processing have shown promise in addressing the complexities of copyright regulation. However, they often incur prohibitive computational costs or suffer from performance trade-offs. To overcome these limitations, we introduce Copyright-Protecting Model Fusion (CP-Fuse), a novel approach that combines models trained on disjoint sets of copyrighted material during inference. In particular, CP-Fuse adaptively aggregates the model outputs to minimize the reproduction of copyrighted content, adhering to a crucial \textit{balancing property} that prevents the regurgitation of memorized data. Through extensive experiments, we show that CP-Fuse significantly reduces the reproduction of protected material without compromising the quality of text and code generation. Moreover, its post-hoc nature allows seamless integration with other protective measures, further enhancing copyright safeguards.}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper introduces the Copyright-Protecting Model Fusion (CP-Fuse) as a mitigation approach for copyright infringement in inference-time language generation. CP-Fuse adaptively aggregates the outputs of models trained on disjoint sets of copyrighted material with the goal of minimizing the reproduction of copyrighted content. It also optimizes a balancing property that ensures no single model dominates. Extensive experiments on text and code generation tasks demonstrate that CP-Fuse significantly reduces copyright infringement while maintaining high output quality. The method is also shown to be robust against extraction attacks and compatible with other copyright-protection techniques.

### Strengths
## **1. The approach is novel and sound**

CP-Fuse introduces the more explored inference-time model fusion techniques to the recently emergent challenges of copyright infringement prevention, the application is novel and the problem addressed is important. The efficacy of the method is justified with both theoretical and empirical backing.

## **2. Extensive experiments on multiple use cases across scenarios**

The authors conduct thorough experiments across different datasets and scenarios (text, code, overfitted models). CP-Fuse consistently outperforms baselines like MemFree and CP-$\Delta$ in copyright protection metrics and achieves near "non-plagiarism" on the code task. Further evaluation results also show that CP-Fuse is robust against data extraction techniques, and can be integrated with other training-time copyright mitigation methods.

## **3. Output utility is high**

The paper reports that CP-Fuse does not sacrifice output quality, achieving comparable scores in fluency (for text) and accuracy (for code generation) relative to overfitted models.

### Weaknesses
## **1. The strong assumption of copyright separability**

The approach relies on the assumption that copyrighted content is separable across datasets and the user of CP-Fuse has access to multiple models trained on these separate datasets. This assumption is particularly limiting because in many real-world scenarios, copyrighted material is not neatly compartmentalized. For example, a single dataset might contain a mix of public domain text, licensed content, and copyrighted material, making it difficult to train models on truly disjoint sets. Furthermore, the requirement of having multiple models trained on separate datasets adds a significant practical constraint, as it necessitates more resources and a specific training pipeline that may not be readily available.

## **2. The computational complexity might limit scalability**

The computational complexity of fusion with grid search parameters presents a significant bottleneck, especially for larger models or longer text generations. The grid search over fusion weights, while effective for finding optimal parameters, becomes exponentially more expensive as the number of models increases. Additionally, the communication overhead between GPUs during the fusion process could become a limiting factor when scaling to larger models or when dealing with more than two models. The paper does not provide a detailed analysis of how the computational cost scales with model size, sequence length, and the number of models, which makes it difficult to assess the practical applicability of the method in resource-constrained environments.

## **3. Limited scope of evaluation**

Currently, CP-Fuse is tested on relatively controlled datasets and tasks, which may not fully reflect the complexities of real-world applications. The evaluation focuses on verbatim or quasi-verbatim reproduction, which is a straightforward case of copyright infringement. However, real-world copyright issues often involve more subtle forms of plagiarism, such as paraphrasing or the use of similar stylistic patterns. The paper does not explore how CP-Fuse performs in these more nuanced scenarios. Furthermore, the datasets used are relatively small and may not capture the diversity and complexity of real-world corpora, which could limit the generalizability of the findings.

### Questions
1) Can you explain more about the impact of the separability assumption in real-world applications? How would CP-Fuse perform in scenarios where copyrighted materials cannot be easily isolated?

2) How does the performance of CP-Fuse scale with larger language models and increased amount of copyright materials? Would additional computational resources be required, or could there be potential optimizations?

3) For future works, could CP-Fuse be generalized to other modalities beyond text and code (e.g., images or audio)? If so, what adaptations might be necessary?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper addresses a significant concern in the field of large language models (LLMs) — the risk of generating copyrighted material. The authors propose a novel inference-time method called Copyright-Protecting Model Fusion (CP-Fuse), which reduces the likelihood of reproducing copyrighted content without impacting the quality of the generated text. CP-Fuse achieves this by adaptively combining the outputs from multiple models, each trained on disjoint datasets containing distinct copyrighted material. By leveraging the balancing property in fusion, the paper claims to prevent any single model from dominating the output, thereby mitigating the regurgitation of memorized, copyright-protected text. The experimental results demonstrate CP-Fuse’s effectiveness compared to existing inference-time copyright-protection techniques, with improvements in copyright infringement reduction while maintaining the utility of generated outputs.

### Strengths
The paper is well-written and highlights the critical issue of copyright protection in LLMs, which is increasingly relevant as these models are deployed in diverse domains. Addressing this issue is essential for responsibly advancing generative AI.

CP-Fuse introduces a fresh approach to copyright protection by employing model fusion, which differentiates it from conventional methods focused solely on filtering or training-time constraints. The adaptive fusion strategy shows promise in providing a feasible balance between copyright compliance and output quality.

### Weaknesses
While the fusion of multiple models appears to improve copyright protection, it may introduce potential inefficiencies, especially at inference time. However, the paper lacks experimental results that measure the efficiency or computational cost of CP-Fuse compared to single-model approaches. Such evaluations are important to gauge the method's practicality in real-world applications.

The paper evaluates utility on task-specific datasets but does not test CP-Fuse on general benchmarks like MMLU. Adding such benchmarks could provide a more comprehensive view of the trade-offs in generalization and utility across diverse language tasks.

As an inference-time approach, CP-Fuse cannot prevent malicious users from extracting model parameters to obtain copyrighted content. If a model has already been trained on multiple datasets containing copyrighted material, an attacker could use a single dataset-focused fine-tuned model to retrieve specific copyrighted documents easily. This limitation suggests that CP-Fuse may not provide sufficient protection against all types of copyright violations, particularly those involving parameter access or model reuse by adversaries.

### Questions
Is model fusion essential to address copyright concerns, or could other strategies, potentially simpler, also achieve comparable results? It would be helpful to know if the authors considered or tested any alternative methods.

The paper’s extensive use of various metrics is commendable; however, previous works have often relied on the Longest Common Subsequence (LCS) to gauge memorization. Was there a specific reason LCS was excluded from the analysis?

The balancing property is central to the proposed fusion strategy, but is its relevance to copyright protection empirically validated? While balancing prevents any single model from fully influencing the generation, it is not immediately clear if or how this directly contributes to reducing copyright infringement. Further clarification on its role and effectiveness would be beneficial.

How does CP-Fuse relate to Mixture of Experts (MoE) models?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The paper introduces Copyright-Protecting Model Fusion (CP-Fuse), a technique designed to reduce the likelihood of language models reproducing copyrighted material during text generation. CP-Fuse combines outputs from different language models, each trained on distinct copyrighted datasets, using an adaptive fusion mechanism. This method mitigates the risk of copyright infringement by limiting memorization without compromising content quality.

### Strengths
This is a very well-written paper that is easy to follow. It introduces a new, adaptable method for copyright protection that can be combined with other training techniques to further increase its efficacy. A big strength is that the authors provide an extensive evaluation across multiple methods to measure memorization and they also evaluate the fluency/quality of the model outputs.

### Weaknesses
The approach assumes that copyrighted material can be effectively separated into distinct datasets, a process that becomes challenging at larger scales and real-world scenarios. This limitation is noted in the Appendix, but the authors only address the practical challenges of creating copyrighted datasets, and not the potential ethical issues and dual-use concerns that may arise from using such data and models.

Moreover, even though the authors mention how previous works are computationally heavy, they do not include a statement detailing the computational resources used in their experiments.

I was not sure if this should be added as a weakness or question, but have you considered that your approach might not be effective for adversarial prompts? How does CP-Fuse handle cases of minor text modifications where the original structure is still recognizable? Did you try any adversarial extraction methods (similar to the goldfish paper)?

### Questions
I was not sure if this should be added as a weakness or question, but have you considered that your approach might not be effective for adversarial prompts? How does CP-Fuse handle cases of minor text modifications where the original structure is still recognizable? Did you try any adversarial extraction methods (similar to the goldfish paper)?

I recommend specifying the duration of each experiment, the hardware (e.g., type of GPU) employed, and the overall computation time to provide clarity on the method's computational feasibility and sustainability. 

It is also necessary to address any anticipated risks or ethical concerns associated with this work. The prerequisite of having a dataset with copyright material and a model trained on such data needs to be further discussed.

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents the CP-Fuse algorithm, a decoding-time strategy to reduce the amount of verbatim memorization (of copyright data) during LLM decoding. The algorithm operates in two simple steps:

1. Two models are trained on potentially overlapping subsets of the training data, as long as the copyright part is well separated between the two subsets.

2. The two models are interpolated during inference, with a dynamic per-token weighting scheme that ensures an equal contribution from each model towards the output.

The authors conduct experiments in a number of domains (writing, coding, math abstracts) and find that models trained with CP-Fuse are significantly less prone to verbatim memorization. Moreover, the fused models continue to preserve the quality of the overfit models which did not undergo any interpolation.

### Strengths
1. The paper presents good contributions in an important research area: preventing verbatim reproduction of copyright information. This topic is getting extremely important recently due to the presence of copyright data in frontier models, which has led to many multi-million dollar lawsuits.

2. The proposed algorithm is intuitive and effective --- it reduces reproduction of copyright material by 25x, and outperforms competing algorithms like CP-delta and MemFree. Experiments are conducted in four different domains using a variety of pretrained models (LLAMA2, GPT-2 XL, Phi)

3. Beyond the main experiments, the paper has a lot of good analysis including (1) a combination of CP-Fuse with training time copyright protection methods; (2) robustness to long prefix probing attacks; (3) different decoding strategies; (4) interpolation of three models; (5) analysis of the chosen interpolation weights.

4. The paper has a great appendix with a lot details and model outputs from both the overfitted model and CP-Fuse. Overall, the paper was well presented, and the figures were clear and easy to understand.

### Weaknesses
I had no concerns regarding the copyright prevention aspect of the algorithm, and thought the experiments were well designed. However, almost all my concerns were regarding the potential quality / utility drop due to interpolation of LLM probabilities during inference. Please let me know if some subset of the weaknesses / questions was covered somewhere in the appendix.

1. **Measuring the quality loss due to CP-Fuse on stronger baselines** would make the paper stronger. In Table 2, currently all models have a HumanEval pass@1 score of less than 29%, which is far lower than the state-of-the-art (Claude 3.5 Sonnet reached 93.7% recently). My hypothesis is that the quality drop due to LLM interpolation maybe higher / more visible with stronger LLMs. Could this method be applied to the larger LLAMA-3 or Gemma-2 family of models?

2. **Unclear quality tradeoff between multitask learning and fusing during decoding**. A lot of the model merging suggests a quality drop from multitask learning to merging models trained on individual datasets. What is the performance difference between a single model trained on `D1+D2` vs CP-Fuse of a model trained on `D1` with a model trained on `D2`?

3. **Experimental settings of overfitting on a small dataset a bit artificial**. The current experimental setting of overfitting on a single small domain-specific dataset seems a bit artifical. In practice, SFT models are trained on a large mixture of multiple tasks (like TULU-v2 https://arxiv.org/abs/2311.10702) and not overfit on any particular task. I would be curious to better understand: (i) what is the recommended strategy for dataset splitting when many source datasets are involved? (ii) Same question as weakness 2, what is the quality tradeoff between multi-tasking and running CP-Fuse on two models?

4. **Is there a slowdown in decoding time?** The algorithm involves sampling from two LLMs at inference, and estimating interpolation weights. How much does this slow down decoding time vs a vanilla single LLM sampling? What is the relative time taken between sampling and interpolation weight grid search?

### Questions
1. It wasn't super clear to me if the CP-Fuse theoretically guarantees copyright prevention to some n-gram threshold (example: 5-gram sequences will NEVER be copied irrespective of the learnt distributions). Looking at some examples (Figure 13) and Figure 3, I'm guessing this is not true --- But I'm wondering if the authors did any analysis on this / have any insights.

2. How does the method interact with RLHF? Would you suggest splitting RL prompts in a similar manner as done on SFT data? RLHF model outputs are known to be more deterministic than SFT model outputs (https://arxiv.org/pdf/2310.06452) --- does this mean the fusing algorithm will be less effective on RLHF'ed models?

3. Nit: L107: does not assign non-negligible probability --> assigns negligible probability

### Soundness
3

### Presentation
4

### Contribution
3
