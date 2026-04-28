# Small Molecule Optimization with Large Language Models

- Decision: Reject
- Avg Score: 5.75
- Scores: 5, 6, 6, 6

## Abstract
Recent advancements in large language models have opened new possibilities for generative molecular drug design. We present Chemlactica and Chemma, two language models fine-tuned on a novel corpus of 110M molecules with computed properties, totaling 40B tokens. These models demonstrate strong performance in generating molecules with specified properties and predicting new molecular characteristics from limited samples. We introduce a novel optimization algorithm that leverages our language models to optimize molecules for arbitrary properties given limited access to a black box oracle. Our approach combines ideas from genetic algorithms, rejection sampling, and prompt optimization. It achieves state-of-the-art performance on multiple molecular optimization benchmarks, including an 8\% improvement on Practical Molecular Optimization compared to previous methods. We publicly release the training corpus, the language models and the optimization algorithm.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents a novel approach to molecular optimization for drug discovery by leveraging the large language models. The contribution are included as follows, LLM-based molecular design, new molecular corpus, optimization algorithm and this paper also claims achieves the state of art performance.

### Strengths
The strengths of the paper lie in several key areas.
1. comprehensive dataset, this authors created a custom molecular corpus with over 100 million molecules from PubChem, incorporating detailed chemical properties. 
2. The combination of LLMs with a genetic algorithm, prompt optimization, and rejection sampling allows the paper’s method to effectively explore chemical space and optimize for multiple properties at once.
3. Versatility: The models demonstrate adaptability, achieving high performance even with minimal fine-tuning data, which underscores their capability with limited datasets. 
4. Open Access: The authors prioritize reproducibility by openly sharing their training data, models, and optimization algorithms with the research community.

### Weaknesses
The weakness of this paper includes:
1. The model only consider the smile representation, it lacks explicit consideration of 3D conformation
2. The proposed optimization algorithm, while efficient, still relies on a high number of oracle evaluations. This paper could further improve reduce oracle calls, especially for applications where computationally intensive evaluations may be costly.
3. Limited experimental validation: while the paper demonstrates strong results on computational benchmarks, it would benefit from additional validation in real-world experimental settings, such as testing generated molecules in biological assays.
4. The performance of the models appears sensitive to hyperparameter choices, especially during the optimization process.
5. The molecule optimization algorithm lacks of novelty.
6. Missing references to recent studies.

### Questions
see weakness

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores small molecule optimization using Large Language Models (LLMs) based on evolutionary strategies. The authors introduce pair tokens to represent molecules and utilize these tokens to express various properties and SMILES strings. They fine-tune a pre-trained model using this token-based approach and perform molecule optimization and property prediction. The study demonstrates state-of-the-art performance in molecule property prediction on specific datasets through supervised fine-tuning. Additionally, the authors propose a novel SMILES generation method inspired by genetic algorithms using their token system. Finally, they present a molecule optimization algorithm based on dynamic fine-tuning, which achieves state-of-the-art results on molecule optimization benchmarks.

### Strengths
1. The study successfully demonstrates the feasibility of molecule optimization using LLMs and a special token system.
2. The innovative approach of emulating genetic algorithms through the token system and Chain of Thought reasoning is particularly noteworthy.

### Weaknesses
### Lack of Computational Efficiency Comparison
1. The paper does not provide a comparison of overall processing times between methods.

### Exploration of Efficient Training Methods
1. Have the authors considered more efficient learning methods beyond fine-tuning the entire model?
2. It would be interesting to explore the effects of techniques such as freezing specific layers, layer skipping, or parameter-efficient fine-tuning.

### Limited Exploration of LLM Capabilities for Multi-Property Optimization (MPO)
1. Additional experiments demonstrating the potential of LLMs for MPO would be beneficial.

### Questions
### Lack of Computational Efficiency Comparison
1. Given that LLM inference can be computationally expensive, it would be valuable to know the time required for molecule optimization. Is it possible to compare this with other models?

### Exploration of Efficient Training Methods
1. Can you explore the effects of techniques such as freezing specific layers, layer skipping, or parameter-efficient fine-tuning?

### Limited Exploration of LLM Capabilities for Multi-Property Optimization (MPO)
1. How would the performance change if target properties were enumerated rather than produced as a product?

These points could be addressed to further strengthen the paper and provide a more comprehensive understanding of the proposed method's capabilities and limitations.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces 3 models Chemlactica-125M, Chemlactica-1.3B, and Chemma-2B which fine-tunes Galactica. The new series of models are trained on a custom prepared dataset based on PubChem data. The final models were used for property prediction and molecular optimisation tasks. The models show strong empirical performance, outperforming or matching recent existing methods.

### Strengths
* The authors release the training corpus and model checkpoints
* Table 1 shows the benefit of transfer learning
* Property prediction experiments show strong performance
* Molecular optimisation experiments are thorough and compared to strong baselines 
* The Appendix is detailed and the transparency around hyperparameter tuning, information around floating point precision is interesting

### Weaknesses
Generally, descriptions of the model and pre-training are thorough but there are important metrics and discrepancies in the pre-training dataset that should at least be discussed. I will combine the specific points and related questions in the Questions section.

1. From the main text results, Chemlactica-125M, Chemlactica-1.3B, and Chemma-2B show strong empirical performance, matching or outperforming recent strong baselines. It is clear that the models work, but it is unclear how much of the benefit is from the pre-training data itself and leveraging the base pre-trained Galactica. I will focus my discussion here on the molecule optimisation experiments. On the PMO benchmark, the authors outperform all compared models by a wide margin. However, the PMO benchmark was designed with ZINC 250k as the pre-training data. All models in the benchmark were pre-trained with this data. How would the performance differ if all the existing models in PMO were pre-trained with PubChem and/or Chemlactica/Chemma were further pre-trained on ZINC 250k and not PubChem? Based on this, I had also checked the Augmented Memory (ChEMBL) [1], GEAM (ZINC 250k) [2], and Saturn (ZINC 250k) [3] papers cited by the authors and their pre-training data. There is existing literature suggesting that changing from ChEMBL to PubChem pre-training data alone improves performance considerably [4]. Pre-training data is expected to have a notable impact on optimisation performance since the models fit this data. While I can appreciate that part of the point of the models released by the authors is leveraging "big data", an ablation on fine-tuning Galactica with just ZINC 250k and/or ChEMBL and/or pre-training the comparison models with PubChem would enable a more thorough understanding of which component of the proposed models leads to the biggest performance improvement.

2. Table 9 shows high variability and seemingly unpredictable behavior when tuning for conditional generation. This section was shown for molecular weight but is this behavior also observed for other tasks? The authors state that the optimal hyperparameters are the same across the models but is this consistent with other tasks? Molecular weight is inexpensive to compute and if this tuning behavior is very sporadic, it might be difficult to control the behavior with other more expensive properties. It would be informative to show the tuning statistics on other properties.

3. Figure 11 shows the docking scores of molecules for the DRD2 experiment. It looks like there is high variance even towards the end of the run.  An advantage of generative models that are fine-tuned is focused modeling of a good distribution. I would have expected that the variance decreases as good molecules are found since the model is being fine-tuned with only the best molecules. Is this variability present on the other docking targets? I can appreciate that the models generate molecules with good docking scores and that this does not take away from that fact, but I am interested in hearing the author's thoughts on potential reasons for the variability. A potentially interesting experiment would be to purposely fine-tune the models with sets of very similar molecules. Does this still lead to high variability?

4. In Table 5/6, GEAM reports diversity with #Circles [5]. Do the authors also have these metrics?

5. Are there statistics on how many times fine-tuning was performed and how long this takes?

6. How much memory and time does it take to deploy and inference the models?

7. Minor comment: typo in number of valid candidate molecules 10e60?

### Questions
1. From the main text results, Chemlactica-125M, Chemlactica-1.3B, and Chemma-2B show strong empirical performance, matching or outperforming recent strong baselines. It is clear that the models work, but it is unclear how much of the benefit is from the pre-training data itself and leveraging the base pre-trained Galactica. I will focus my discussion here on the molecule optimisation experiments. On the PMO benchmark, the authors outperform all compared models by a wide margin. However, the PMO benchmark was designed with ZINC 250k as the pre-training data. All models in the benchmark were pre-trained with this data. How would the performance differ if all the existing models in PMO were pre-trained with PubChem and/or Chemlactica/Chemma were further pre-trained on ZINC 250k and not PubChem? Based on this, I had also checked the Augmented Memory (ChEMBL) [1], GEAM (ZINC 250k) [2], and Saturn (ZINC 250k) [3] papers cited by the authors and their pre-training data. There is existing literature suggesting that changing from ChEMBL to PubChem pre-training data alone improves performance considerably [4]. Pre-training data is expected to have a notable impact on optimisation performance since the models fit this data. While I can appreciate that part of the point of the models released by the authors is leveraging "big data", an ablation on fine-tuning Galactica with just ZINC 250k and/or ChEMBL and/or pre-training the comparison models with PubChem would enable a more thorough understanding of which component of the proposed models leads to the biggest performance improvement.

2. Table 9 shows high variability and seemingly unpredictable behavior when tuning for conditional generation. This section was shown for molecular weight but is this behavior also observed for other tasks? The authors state that the optimal hyperparameters are the same across the models but is this consistent with other tasks? Molecular weight is inexpensive to compute and if this tuning behavior is very sporadic, it might be difficult to control the behavior with other more expensive properties. It would be informative to show the tuning statistics on other properties.

3. Figure 11 shows the docking scores of molecules for the DRD2 experiment. It looks like there is high variance even towards the end of the run.  An advantage of generative models that are fine-tuned is focused modeling of a good distribution. I would have expected that the variance decreases as good molecules are found since the model is being fine-tuned with only the best molecules. Is this variability present on the other docking targets? I can appreciate that the models generate molecules with good docking scores and that this does not take away from that fact, but I am interested in hearing the author's thoughts on potential reasons for the variability. A potentially interesting experiment would be to purposely fine-tune the models with sets of very similar molecules. Does this still lead to high variability?

4. In Table 5/6, GEAM reports diversity with #Circles [5]. Do the authors also have these metrics?

5. Are there statistics on how many times fine-tuning was performed and how long this takes?

6. How much memory and time does it take to deploy and inference the models?

7. Minor comment: typo in number of valid candidate molecules 10e60?

Overall, the transparency in the paper and the strong empirical performance are positive points. The main questions I have are centered around how much benefit is from the pre-training data compared to the specific workflow introduced (Galactica fine-tuning on PubChem-derived dataset). I am happy to engage in discussions with the authors.


[1] Augmented Memory: https://pubs.acs.org/doi/10.1021/jacsau.4c00066

[2] GEAM: https://arxiv.org/abs/2310.00841

[3] Saturn: https://arxiv.org/abs/2405.17066

[4] REINVENT with Transformer: https://jcheminf.biomedcentral.com/articles/10.1186/s13321-024-00887-0

[5] #Circles: https://openreview.net/forum?id=Yo06F8kfMa1

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
This paper presents a unique framework for optimizing small molecules using large language models (LLMs), specifically Chemlactica-125M, Chemlactica-1.3B, and Chemma-2B. These models, trained on over 100 million molecules extracted from PubChem, offer both generative and predictive capabilities tailored to molecular property prediction tasks. The primary contributions are as follows:
- Development of a Specialized Molecular Dataset: The authors construct a dataset rich in molecular properties, incorporating known structures, experimental properties, and optimized SMILES-based representations.
- Novel Optimization Algorithm: The paper introduces an innovative molecular optimization framework combining LLM-based generation with evolutionary strategies, specifically integrating genetic algorithms and prompt optimization techniques to enhance the molecular design pipeline.
- Benchmark Performance and Evaluation: By assessing performance on tasks such as Practical Molecular Optimization (PMO) and docking-based multi-property objectives, the authors claim state-of-the-art (SOTA) results across several key metrics, such as sample efficiency and the generative yield of viable molecules.

### Strengths
- Comprehensive Experimental Validation: The authors present a well-rounded suite of experiments, rigorously evaluating their models on various molecular design benchmarks, such as PMO, and providing comprehensive comparisons to current SOTA techniques across a diverse range of metrics.
- Innovative Optimization Framework: The integration of evolutionary strategies within a language-model-driven molecular generation pipeline is novel, blending genetic search concepts with LLM-specific prompt engineering. This hybridization is particularly suited to address the combinatorial complexity of chemical space.

### Weaknesses
 - Inclusion of Baseline Comparison with Similar Methods:
The paper would benefit from a direct comparison with Wang et al.’s 2024 study, "Efficient Evolutionary Search over Chemical Space with Large Language Models," as this work also applies genetic algorithms with LLMs, albeit without fine-tuning. Since the authors acknowledge Wang et al.’s work as the most similar, a side-by-side comparison would strengthen the argument for the advantages of the current approach and illustrate any tangible benefits from fine-tuning.

- Model Selection and Justification:
While Chemlactica and Chemma are based on Galactica and Gemma models, it remains unclear why these were chosen over other more established and widely benchmarked models like Llama or GPT. Galactica and Gemma are comparatively limited in LLM applications, so examining the performance difference with a model like Llama or GPT, which are better validated, would be beneficial. This could help address concerns about model architecture suitability and provide insights into optimizing architectures for molecular tasks.

- Risk of Data Leakage and Benchmark Validity:
A significant limitation arises from the potential data leakage inherent in using PubChem-derived training data. Given that PMO and docking benchmarks aim to rediscover known drugs as a proxy for drug discovery, these molecules may already exist within PubChem. This overlap risks inflating performance metrics by providing the model with information it may have encountered during training. A clearer methodology or additional validation on a benchmark explicitly excluding known molecules from PubChem could address this confounder and validate the robustness of the framework.

- Task Selection and Generalizability:
The paper reports results on a subset of benchmark tasks (5 of 23 in PMO and 3 of 17 in MoleculeNet). This limited selection raises questions about the generalizability of the results, especially given that the ADMET prediction results in the appendix were less successful. Expanding the evaluation across additional tasks, or clarifying the criteria for task selection, could help establish confidence in the model’s consistency and overall applicability to various molecular optimization challenges.

### Questions
How does the method perform on tasks beyond what is shown in the main text?

### Soundness
2

### Presentation
3

### Contribution
2
