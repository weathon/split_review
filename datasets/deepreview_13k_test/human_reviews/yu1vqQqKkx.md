# LICO: Large Language Models for In-Context Molecular Optimization

- Decision: Accept
- Scores: 6, 8, 5, 6

## Abstract
Optimizing black-box functions is a fundamental problem in science and engineering.
To solve this problem, many approaches learn a surrogate function that estimates the underlying objective from limited historical evaluations.
Large Language Models (LLMs), with their strong pattern-matching capabilities via pretraining on vast amounts of data, stand out as a potential candidate for surrogate modeling.
However, directly prompting a pretrained language model to produce predictions is not feasible in many scientific domains due to the scarcity of domain-specific data in the pretraining corpora and the challenges of articulating complex problems in natural language.
In this work, we introduce \name{}, a general-purpose model that extends arbitrary base LLMs for black-box optimization, with a particular application to the molecular domain.
To achieve this, we equip the language model with a separate embedding layer and prediction layer, and train the model to perform in-context predictions on a diverse set of functions defined over the domain.
Once trained, \name{} can generalize to unseen molecule properties simply via in-context prompting.
\name{} achieves state-of-the-art performance on PMO, a challenging molecular optimization benchmark comprising over $20$ objective functions.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
The paper focuses on one of the most promising directions of modern LLMs: LLM-enhanced optimization algorithms. It suggests a method to extend arbitrary pretrained LLMs with a couple of layers and train them to perform in-context learning for arbitrary functions. The idea is tested on molecular property prediction tasks, and the paper claims SOTA results on the famous PMO benchmark.

### Strengths
* the "domain adaption" trick to convert the general purpose text-based LLMs into domain-specific in-context learners using synthetic data.
* detailed ablation studies. I really liked the analysis of the effect of the ratio of "intrinsic" and "synthetic" datasets. It gives an intuition on how to design synthetic datasets for other optimization tasks in other domains.
* the "scaling law" chart (Fig. 3) is a good indicator of the scaling abilities of the proposed approach. Unfortunately there is a diversity of underlying models which makes the claims less significant. Hopefully there will be many sizes of similarly pretrained LLMs at some point (e.g. Llama 4 1B, 3B, 8B, etc.).

### Weaknesses
The main weakness is that the SOTA claim on PMO is misleading. **The results reported in this paper are not really PMO.** There are two major differences. 

a) PMO has 23 tasks, not 21. *jnk3* and *gsk3* are missing.

b) PMO uses 10K budget of oracle calls (as mentioned by the authors).

While a) does not make the comparison to prior art unfair, b) is critical. The main advantage of the PMO paper was that the authors performed a large-scale hyperparameter search for every method they tried, and even discovered hyperparameter values (e.g. for REINVENT) that were not covered even by the authors of the methods. So, all methods from PMO, and the subsequent methods like Genetic GFN have their hyperparameters tuned for the 10K budget. 

I agree with the authors that 1K budget can be more interesting, as 10K might feel saturated, but that's a different benchmark. I would suggest to name it something like **PMO-1K**, and then properly tune the hyperparameters of the baselines. I understand it's hard to do this in the review discussion period.

** Details of the optimization algorithm**
It took me a few days to understand that the sentence "At each iteration t, we generate a set of candidates" in Section 4.3 does not mean that the candidates are generated without the LLM. As seen in the Appendix, the authors actually used a manually designed genetic algorithm for generating the candidates, and the LLM is only used for scoring them. This is a critical component of the algorithm and has to be presented well in the main part of the paper. 

**Three other papers that could be cited and discussed:**
1. Optformer [1] is the earliest transformer to the best of my knowledge that used in-context learning for an optimization task. It did not use an initialization from a large pretrained model, and the data used there is not synthetic. Still, the concept is very close.
2. Another recent approach that produced good scores on PMO is from the Chemlactica/Chemma models [2]. It has the genetic algorithm idea, very similar to the one described in the Appendix A.3. Chemlactica's scores on PMO are still a bit unfair, as it uses a lot more molecules in the pretraining phase (way beyond ZINC250k).
3. MOLLEO [3] is another evolutionary algorithm that wraps an LLM. It has a few evaluations on 

A minor aspect that could be considered in the future iterations: use more realistic oracles, like molecular docking. Check [2] and [4] for new benchmarks.

[1] Chen, Yutian, et al. "Towards learning universal hyperparameter optimizers with transformers." Advances in Neural Information Processing Systems 35 (2022): 32053-32068.
[2] Guevorguian, Philipp, et al. "Small Molecule Optimization with Large Language Models." arXiv preprint arXiv:2407.18897 (2024).
[3] Wang, Haorui, et al. "Efficient evolutionary search over chemical space with large language models." arXiv preprint arXiv:2406.16976 (2024).
[4] Guo, Jeff, and Philippe Schwaller. "Saturn: Sample-efficient Generative Molecular Design using Memory Manipulation." arXiv preprint arXiv:2405.17066 (2024).

### Questions
**Suggestion:**
I am willing to increase my rating if the authors report results on the *original* PMO-10K, which will ensure fair comparison with the prior work. Even if the results are not SOTA anymore, the paper can still be accepted, as the methods of the paper are interesting on their own. 

The paper can have an additional table for PMO-1K, with either tuned baselines, or with a note that the baselines are not carefully tuned.

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper introduces LICO, a versatile model that enhances LLMs for black-box optimization, specifically in the molecular domain. LICO overcomes limitations related to domain-specific data scarcity and complex problem expression. It is trained to perform in-context predictions across diverse functions and, post-training, efficiently generalizes to new molecule properties through simple prompting. LICO achieves state-of-the-art PMO molecular optimization benchmark results, demonstrating its efficacy in complex scientific applications.

### Strengths
1. The paper studies an important task of adapting LLMs for molecular optimization tasks, which has not been studied extensively. 

2. The paper presents a novel approach by integrating LLMs with specialized layers to address black-box optimization problems in the molecular domain.

3. The model achieves strong performance on the challenging PMO benchmark.

### Weaknesses
1. While this paper demonstrates the strong performance of LLMs, the analysis of their specific benefits remains limited. It would be valuable to understand which particular characteristics of LLMs contribute to the success of this molecular optimization task. For instance, how do different LLM architectures or configurations impact performance? Would domain-adaptive training on chemistry corpora further enhance results? Expanding on these points with additional explanation would strengthen the understanding of LLMs' effectiveness in this context.

2. The study offers a limited exploration of prompt formats. Further investigation into how different prompt structures might influence model performance would be beneficial (e.g. Prompts that include more domain-specific chemistry terminology/Prompts that frame the task in different ways (e.g. as a prediction task vs. an optimization task/Testing different ways of structuring the input-output pairs within the prompt).

3. It would be better to discuss several recent works for using LLMs for molecule optimization: a) DrugAssist: A Large Language Model for Molecule Optimization; b) Domain-Agnostic Molecular Generation with Self-feedback; c) A Sober Look at LLMs for Material Discovery: Are They Actually Good for Bayesian Optimization Over Molecules?

### Questions
See above.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work proposes a semi-synthetic training approach for LLM-based surrogate modeling, with a specific focus on molecular optimization. By integrating a pretrained language model with embedding and prediction layers and training on both "intrinsic" and synthetic data, it shows promises of outperforming gold-standard Gaussian process regressors. As a result, the molecular optimization algorithm coupled with this LLM-based surrogate shows better performances than presented baselines, ranging from RL algorithms to GFN etc. The authors also presented analysis on different model sizes and training approach with varying data mixture.

### Strengths
-The overall approach shows good efficacy, as shown in the benchmark scores. The combo of training data and modeling recipe is interesting and novel for surrogate modeling, as far as I know (this needs cross-confirmation).

-The scaling law analysis is interesting, indicating the power of scaling up the model size for better molecule optimization outcome.

-The ablation study and result analysis is helpful: the analysis of surrogate modeling accuracy, vs. the GPR baseline, confirms the efficacy of proposed LLM surrogate modeling approach. The discussion of the limitation of PMO benchmark numbers are also helpful and shows scientific rigor.

### Weaknesses
-The authors selectively show the numbers with a different sampling budget (1k instead of 10k in the original PMO setting) with a reason. Can they also present the numbers with different sampling budget in the supplementary information? That will confirm the generalization of the proposed approach.

-The ablation and baseline should be more comprehensive: there are several concurrent works for LLM for molecular optimization[1,2], the authors should also add them as a baseline, if applicable, and thereafter discuss the efficacy of the proposed methods. For example, the MolLEO framework [1] (https://github.com/zoom-wang112358/MOLLEO) claims that they achieve superior performances than baselines on PMO as well, how does it compare with LICO? 

-Two more straightforward baselines I can come up with are: (1) drop the input embedding layers, simply extract the text embedding from prompts and train an MLP layer for the surrogate. (2) drop both the embedding and prediction layers, use the pretrained model to do in context learning only. This is similar to the LLAMBO work [3] that is cited in the paper. The authors should justify why they think the proposed approach is the most promising here.

-The description of the experimental details is a bit lacking: e.g. how the embedding and prediction layers are integrated into the existing LLM backbone? Please also provide code and pretrained models so that the reviewers can reproduce the results.

-The language models tested in this work, such as llama2 and qwen1.5, are slightly outdated. The authors should also add numbers on llama3/3.1, Qwen2 to further confirm their conclusions. 

-The related works section on LLM for molecular optimization is missing.

[1] Efficient Evolutionary Search Over Chemical Space with Large Language Models, arXiv:2406.16976 . 
[2] ChatGPT-powered Conversational Drug Editing Using Retrieval and Domain Feedback, ICLR 2024.
[3] https://github.com/tennisonliu/LLAMBO; Large Language Models to Enhance Bayesian Optimization, ICLR 2024.

### Questions
1. Can the authors argue why the additional input embedding layers are necessary here? considering that the LLM always comes with an existing embedding layers.

2. How the embedding and prediction layers are integrated into the existing LLM backbone?

3. Maybe I missed this, but what language representation is used in LICO?

4. What's the rationale behind using Tanimoto kernels for GPR synthetic data generation? Have the authors tried other types of kernels, and how do they perform?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors report an approach to using LLMs with additional embedding layers (similar to FPT) and text-encoding and semi-synthetic training (similar to ExPT) for molecular optimization. They report good performance on the PMO benchmark.

### Strengths
- The authors use an established benchmark and perform competitive performance on this benchmark 
- Bayesian optimization is one of the most practically useful applications of machine learning in chemistry 
- The paper is well-written and easy to follow 
- The method is novel (but it is based on combining multiple existing techniques) 
- There are useful ablations (e.g., training with various amounts of synthetic data)

### Weaknesses
- In some places, the paper seems to indicate that ICL for Bayesian Opt has not been done in chemistry. This, however, is not the case as the following two reports show: 
    - https://arxiv.org/abs/2304.05341
    - https://www.researchgate.net/profile/Christoph-Voelker-4/publication/377722231_LLMs_can_Design_Sustainable_Concrete_-a_Systematic_Benchmark_re-submitted_version/links/65b408e934bbff5ba7c85ad8/LLMs-can-Design-Sustainable-Concrete-a-Systematic-Benchmark-re-submitted-version.pdf
- A bit related is the use of LLM-derived embeddings for Bayesian Opt in chemistry. This, for example, has been reported in https://openreview.net/forum?id=A1RVn1m3J3

### Questions
- How do you obtain the uncertainties do you directly use the probabilities returned by the model? Are those probabilities well-calibrated? 
- The ordering of the examples seems important - what is the impact and how is this taken care of? 
- The approach is shown for a causal LM. But it seems that a masked approach (similar to https://www.nature.com/articles/s42256-023-00639-z) might be more effective in learning from the entire sequence

### Soundness
3

### Presentation
3

### Contribution
3
