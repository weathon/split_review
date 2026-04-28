# Tabby: Tabular Adaptation for Language Models

- Decision: Reject
- Avg Score: 3.00
- Scores: 1, 3, 5

## Abstract
While advances in large language models (LLMs) have greatly improved the quality of synthetic text data in recent years, synthesizing tabular data has received far less attention. Many of the top-performing approaches to this problem rely on techniques that adapt models originally developed for other modalities, potentially leaving generative performance on the table. We address these disparities in attention and performance for tabular data by introducing Tabby, a simple but powerful post-training modification to the standard Transformer-based language model architecture that enables its use for tabular dataset synthesis. Tabby relies on Gated Mixture-of-Experts layers, allowing each data column to be modeled by a dedicated set of parameters within the transformer multi-layer perceptrons or language modeling heads.  Applying Tabby to Distilled-GPT2 improves synthetic data quality up to 7% compared to previous tabular dataset synthesis methods, achieving performance near or equal to that of real data.

## Human Reviews

## Human Reviewer 1

### Rating
1

### Rating Number
1

### Confidence
3

### Summary
The paper proposes to use a MOE LLM fine tuned on table data for synthetic table data synthesis.  The authors find that their method outperforms previous methods on table synthesis benchmarks.

### Strengths
The proposed method outperforms other methods on most datasets and metrics presented.

### Weaknesses
 * There is no significant difference between tabby and the non-tabby (I assume no MOE?) baseline.  Given that MOE has a lot more parameters, this is a negative finding.
* The papers contributions are very minor - applying MOE to a narrow problem (table generation).  And the results are not all that strong.
* It's not easy from the presentation what exactly do the tasks require, what exactly are the baselines and model variations.

### Questions
Can you please detail the various architectures MMLP, MH and MMLP+MH? 
Why does MMLP+MH underperform, even though it is more complex?
Do you replace every layer with MOE?

### Soundness
1

### Presentation
2

### Contribution
1

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This work introduces a new model called Tabby for tabular data. Tabby is an architecture modification that enables transformer-based language models to synthesize more realistic tabular data. It introduces Gated Mixture-of-Experts layers to better model the complex interdependencies and diverse data types found in tabular datasets. Tabby outperforms previous tabular data synthesis methods, achieving outstanding performance on multiple benchmarks.

### Strengths
1. Tabby achieves strong performance in benchmark evaluation. It generates high-quality synthethic tabular data in comparison with the baseline methods.
2. The introduction of MoE shows effectiveness in helping the model understand tabular data structure and generate higher-quality tabular data.

### Weaknesses
1. The design of MoE layer is complex. For a table with V columns, this article should design an MoE model with V experts to adapt to the table. This is not generalizable to data of diverse formats. It is suggested to modify the model design to be more compatible and more generalizable.
2. Scalable experiments are advised to be conducted. This study needs to provide experimental results on datasets of larger scales and also more commonly used datasets.
3. The experiments are advised to be conducted on contemporary large language models, including Llama, Qwen, Mistral, instead of Distilled-GPT2.

### Questions
1. Have you conducted experiments on the recently released large language models? If yes, which model sizes did you choose?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors present a tabular data synthesis approach, Tabby. The novelty of Tabby lies in two main aspects: (1) modifying the original transformer model by applying MoE-like techniques to better model tabular data, and (2) designing a specialized data format for tabular data. Experimental results show that Tabby achieves comparable performance to the previous state-of-the-art, Tab-DDPM, and outperforms GTT NT.

### Strengths
- The model modifications and data organization are well-motivated and intuitive.
- The distribution of the synthesized data is very close to the natural data.
- The experimental results looks good.

### Weaknesses
 - Tabby seems achieve comparable results to Tab-DDPM with marginal performance gain in Table 2.
- The method is quite simple and not much effective in final performance.


### Questions
Q1: Have you computed the FLOPs for training on different datasets? It seems that Tabby uses a fixed pattern to organize tabular data, which may require more tokens for computation.

Q2: Regarding Claim 2, could you provide a scaling curve showing performance relative to model size or data quantity? It would be interesting to see how Tabby impacts different models and how the amount of Tabby data influences the learning process. Additionally, a comparison of the scaling curve between Tabby data and natural data would serve as evidence of Tabby data being a scalable alternative to natural data.

Q3: I'm not sure if the modification to original network is necessary. Is there an ablation study?

### Soundness
2

### Presentation
2

### Contribution
2
