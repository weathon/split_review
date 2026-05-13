# Self-MoE: Towards Compositional Large Language Models with Self-Specialized Experts

- Decision: Accept
- Scores: 6, 6, 6, 6

## Abstract
We present Self-MoE, an approach that transforms a monolithic LLM into a compositional, modular system of self-specialized experts, named MiXSE (MiXture of Self-specialized Experts). Our approach leverages self-specialization, which constructs expert modules using self-generated synthetic data, each equipping a shared base LLM with distinct domain-specific capabilities, activated via self-optimized routing. This allows for dynamic and capability-specific handling of various target tasks, enhancing overall capabilities, without extensive human-labeled data and added parameters. Our empirical results reveal that specializing LLMs may exhibit potential trade-offs in performances on non-specialized tasks. On the other hand, our Self-MoE demonstrates substantial improvements (6.5%p on average) over the base LLM across diverse benchmarks such as knowledge, reasoning, math, and coding. It also consistently outperforms other methods, including instance merging and weight merging, while offering better flexibility and interpretability by design with semantic experts and routing. Our findings highlight the critical role of modularity, the applicability of Self-MoE to multiple base LLMs, and the potential of self-improvement in achieving efficient, scalable, and adaptable systems.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents a novel approach to modularize large language models by constructing expert modules from self-generated synthetic data and creating a compositional system. Unlike previous Mixture of Experts approaches that use LoRA and rely on either human-labeled data or pre-trained modules, this method develops modules from scratch, adapting the model to specific tasks. Experimental results demonstrate the advantages of this approach over base LLMs and self-specialized LLMs in multiple tasks.

### Strengths
- Mitigation of Forgetting: Compared to monolithic models, which often face challenges with knowledge retention, the proposed approach maintains the integrity of each expert module, which enhances the overall model's performance and adaptability.

- Lightweight and Synthetic Data-Driven Modules: The method constructs individual, lightweight expert modules from synthetic data, which bypasses the need for human-labeled data and broadens the scope of applicability.

- Generalization: The generalization tests indicate that the Self-MoE approach offers benefits beyond the targeted tasks, improving performance on benchmarks that were not explicitly used in training.

### Weaknesses
 - Limited Model Sizes: The experiments primarily focus on small-scale LLMs (7B/13B models), leaving open the question of whether these findings can extend to larger models. Testing on a wider range of model sizes would strengthen the claims.
- Quality and Diversity of Synthetic Data: How does the approach ensure the correctness, diversity, and quality of the instruction-response data generated for training the expert modules? Specifically, what mechanisms are in place to prevent the generation of repetitive or low-quality synthetic data that could negatively impact the training of expert modules? Furthermore, how does the method address potential biases that might be present in the seed data used to generate synthetic examples?
- Domain Granularity: How is the domain granularity determined? For instance, broad domains like reasoning, math, and coding can be subdivided further (e.g., reasoning into medical, finance). To what extent do the findings depend on the chosen level of domain specificity? It is unclear if the current domain divisions are optimal or if a more fine-grained approach would yield better results. The paper should discuss the criteria used to define the current domain boundaries and the potential impact of alternative choices.

### Questions
- Router Details: The router is crucial to the Self-MoE model’s performance but is described only at a high level in the paper. More detailed information (e.g., training etc.) in the main body would enhance the clarity and accessibility of the approach.

- Synergies Across Domains: One reason for the Self-MoE’s superior performance might be that LLMs can exploit synergies across areas of expertise. Would this advantage persist if the domains were highly distinct, such as medical vs. finance?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Self-MoE constructs the corresponding experts modules to realize the self-specialization mechanism to improve the performances on non-specialized tasks and diverse benchmarks such as knowledge, reasoning, math, and coding.

### Strengths
1. Introducing the computation overhead realizes better performance improvement
2. Using the self-optimized routing activates the distinct domain-specific capabilities to help improve the performance shared base LLM 
3. The presentation is good and the experiments are detailed

### Weaknesses
1. The comparison with related works such as  [1] is not enough. The concept of lora-moe has been introduced in this work.  This slightly affects the novelty of the work.

2. The analysis of the impact of the number of experts on downstream performance is not sufficiently detailed. While the paper mentions that adding experts improves performance up to a certain point, it lacks a rigorous investigation into the trade-offs between the number of experts, computational cost, and performance gains. It is unclear how the model determines the optimal number of experts, and whether there is a risk of diminishing returns or even performance degradation with too many experts.

3. The evaluation of the model's generalization to unseen tasks is not comprehensive enough. While the paper presents results on non-target tasks, it does not delve into the reasons behind the observed performance. It is unclear whether the model's performance on these tasks is due to genuine generalization or simply the activation of an expert that happens to be aligned with the task. A more detailed analysis of the model's behavior on unseen tasks is needed, including an investigation into the types of tasks where the model performs well and those where it struggles.

### Questions
1. How does the number of experts impact the downstream performance? If the knowledge for differenct experts is similar, is it possible to reduce the number of experts? 
2. How does the model generate to the unseen tasks?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper proposes a new paradigm of self-MOE that designs a compositional LLM integrating various experts specialized in different aspects and employing a trained router to dynamically choose experts during inference. The experts are trained with LoRA and only a small proportion of parameters are adjusted during self-specialization, keeping a high efficiency. Self-MOE has been tested on several popular LLMs, e.g., Gemma and LLaMA 3, proving its strong ability to enhance current LLMs' performance when dealing with tasks in various aspects simultaneously.

### Strengths
1. Novel idea of self-MOE and it can be a promising new paradigm for stronger foundation models.
2. Paper is well-written.

### Weaknesses
1. Some claims are not very intuitive. I have questions about how synergies among expert happen and given the synergies, why only 1 expert is activated. Please refer to the questions below.
2. Some parts in the main body of this paper are not necessary, for example Table 5. I would rather see it in the appendix. Some figures are either too huge or loosely-structured and leave lots of wasted blank space (e.g., Figure 1 and 2). I think you can put more experiments about self-MOE in the main body. Please refer to point 2 of the questions below. And I would also prefer to see more detailed analysis about other base LLMs. Currenlty I only see a very abbreviated figure (Figure 4) related to this. I think breaking down their performances into several parts as how you present Gemma 7B is meaningful.

### Questions
1. Line 223. I am just wondering if the top-k operation is after doing softmax, then the probability of expert selection is not normalized, meaning that when k is small alpha will also be small. Do you think it will lead to the experimental results which show that top-1 self-MOE is better than top-2 self-MOE (as presented in Table 2). I think by not normalizing the selection probability, the amount of information introduced by experts will be different when different numbers of experts are activated. So directly comparing top-1 and top-2 self-MOE is a bit unfair. Maybe the reason for the worse performance of top-2 self-MOE comes from the excessive redundant information introduced by an irrelavant expert. But this guess contradicts your claim in line 88 that MiXSE explores synergies among experts. I wish to have a more detailed discussion about this part. Given the hypothesis that synergies among experts help to boost performance, why top-1 self-MOE outperforms top-2 self-MOE? This is important for this work, because by only choosing one expert, it largely resembles self-specialization.
2. Line 348. I am also suspicious about the claim that jointly training router and experts would make semantic distinctions among experts diluted. Have you tried to jointly train them and activate more experts (>= 2)? Could you provide it in your rebuttal (sorry I know it requires lots of computational resources)? I just think the experiments and the obervations are not fully supported by your claim. This is also related to your claim that synergies among experts happen when you have multiple experts controlled by a router in self-MOE. If you don’t jointly train them, how synergies happen?
3. Again in Section 4.3, the routing distribution shows that datasets like MMLU benefit from both knowledge and reasoning experts. So why don’t you just activate more experts?
4. Section 4.7. Have you tried adding experts in different orders? For example, R + M + C + K.
5. In Table 3, you labeled TruthfulQA as safety. I am not sure why.

### Soundness
3

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
This paper proposes a self-specification method, named Self-MoE, to transform a monolithic LLM to a MoE system with self-specific experts. To construct expert modules for specific domains, this paper utilizes self-generated data from the base LLM. The resulted Self-MoE demonstrates substantial improvements over the base LLM, even achieves better performance than data mixture and weight merging.

### Strengths
1. It's a good idea to stimulate diverse domain-specific competencies inherent within the base model and reassemble these specific experts to achieve a more powerful MoE system. 
2. This approach offers the advantage of eliminating the necessity for domain-specific data acquisition.
3. The writing and presentation are clear and easy to read.

### Weaknesses
1. The primary contribution of this paper is constructing a MoE system from multiple domain experts, which are fine-tuned on the domain-specific synthesis data from base model itself. However, this self-specialization method was originally proposed by [1]. Moreover, recent studies already propose the construction of MoE system based on multiple domain-specific dense models, which can be fine-tuned using LoRA [2] or full-parameter tuning [3].

2. A critical question in utilizing self-synthesized data for self-improvement is where the performance improvements comes from. For instance, the improvements in [4] is based on an additional reward model to differentiate between good and bad samples. However, the underlying mechanism of Self-MoE's self-improvement remains ambiguous. It is not immediately apparent why domain-specific datasets generated by the base model, without guidance from a stronger model or reward model, can lead to overall performance gains.

3. The expert modules in Self-MoE are fine-tuned from self-synthesized domain data, which determines the upper bound of the expert's capabilities. Therefore, more analysis of the self-synthesized datasets is needed, e.g., data diversity, complexity, and the model performance compared to using existing open-source datasets.



### Questions
1. In the instruction brainstorming stage, how to generate diverse instructions within a given domain? Since the generator is not a strong instruction-following model, e.g. GPT-4, using self-instruct approach can lead to low diversity in the generated domain-specific datasets as illustrated in [5].

2. In the mixture of self-specialized experts stage, router network parameters are shared across all layers. However, when router networks in different MoE layers do not share parameters, they typically exhibit distinct routing behaviors. What is the influence on overall performance and routing behaviors if separate, layer-specific router networks are employed instead of shared ones?

3. In the main results, the baseline methods involve fine-tuning both the LoRA and router parameters. However, this approach presupposes that all base models should be implemented using the MoE architecture, potentially introducing additional complexities in router training. To ensure a more comprehensive and equitable comparison, it is essential to add additional baseline methods, which are directly fine-tuned on the base model using different datasets (specific capabilities, mixture of capabilities, model merging).

4. In Section 4.5, can the author provide the instance merging results (using all the 20k data to direct fine-tune the base model with LoRA) for different base models?

[5] Explore-Instruct: Enhancing Domain-Specific Instruction Coverage through Active Exploration

I would be happy to discuss further with the authors and reassess my score based on the rebuttal stage.

### Soundness
3

### Presentation
3

### Contribution
2
