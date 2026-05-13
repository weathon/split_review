# The Promises and Pitfalls of Language Models for Structured Numerical Data

- Decision: Reject
- Scores: 3, 5, 8

## Abstract
Autoregressive language models are increasingly capable of processing non-text data, such as images or audio. Are language models also a natural choice for numerical data, such as the 3D structure of molecules? In this work, we use quantum chemistry simulations as a case study in the challenges of applying language models to numerical data, building up a set of simple subproblems that can shed light on key design decisions. We show that language models lag behind domain-specific models on prediction tasks and provide evidence for and against different hypotheses that explain their failure. Many commonly identified pitfalls such as difficulty performing arithmetic operations and choice of discrete vocabulary fall short of explaining the behavior. In contrast, we show that capturing invariance properties exhibits a strong correlation with predictive performance. Finally, we provide a comparison of language models trained from scratch on numerical data with models pretrained on text. We show that text pretraining often provides a surprisingly limited advantage on prediction tasks, and can even hurt performance, despite prior work showing that text-pretraining can offer advantages.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The paper discusses the abilities of LLMs to model numerical data, including numbers in complicated data structures like a set of triplets of numbers used to encode 3D molecules. 

First it trains a couple of Llama-like models (with and without pretraining) that fail to predict QM9 targets (compared to GNN baselines). Then it presents a few hypotheses and provides evidence for and against each of them.

### Strengths
* The problem setting in general is very interesting and relevant. 
* Quite wide range of numerical tokenization methods were tested.
* The analysis of invariance and performance of the models is quite interesting. That's probably the most valuable results of this paper. It would be interesting to measure the degree of invariance for non-equivariant GNNs as well, to have a baseline for that particular equivariance metric.

### Weaknesses
1) The main weakness is that the language models tested are not sufficiently tuned for the tasks in question, which raises concerns whether the results presented in the paper relate to language models in general, or just to their suboptimal versions. The authors take a minified version of randomly initialized Llama 2 (<50M parameters), and a pretrained Llama 3.1 8B, and use one set of hyperparameters for each of them. I believe both models require large scale hyperparameter tuning, and maybe even separate tuning for each experiment! 

LORA fine-tuning Llama 8B with just one epoch could be relevant for text-based tasks, but, to the best of my knowledge, there is no evidence that it is even close to optimal for a severe domain shift scenario like in the examples with linear algebra or quantum mechanics. Same is true for fine-tuning Llama 3.1 for only one epoch with such a small dataset (compared to trillions of tokens used in the original Llama). The lack of hyperparameter tuning is a significant concern, as the optimal learning rate, batch size, and LoRA rank could vary drastically between tasks (e.g., predicting molecular properties vs. performing linear algebra). This could lead to the models being under-trained or over-trained, making it difficult to draw general conclusions about the capabilities of language models for numerical tasks.

Another argument that makes me think these trainings are suboptimal is that there are parallel works where open-sourced pretrained models achieve good results on downstream molecular prediction tasks. The examples I found are based on 2D representations (not 3D), but are quite competitive. Please check https://openreview.net/forum?id=p5VDaa8aIY , Table 8 on page 17. The same table also shows the impact of hyperparameter tuning. The hyperparameters borrowed from similar SFT (supervised fine-tuning) tasks from the same paper perform significantly worse than the hyperparameters specifically tuned for the BBBP task.

2) Table 2 shows that the variance of the methods is huge. It hints that all other tables and figures should also report the variance, and it's quite possible that Figure 2 results will become unsignificant. The lack of reported variance makes it difficult to assess the reliability of the results. For example, if the error bars in Figure 2 are large, it would be hard to conclude that the continuous tokenization method is significantly better than the discrete methods. This is particularly important when comparing different tokenization strategies, as the differences in performance might be within the range of statistical fluctuations.

Minor:
* The Table on line 150 probably refers to MAE, which is not mentioned. The table should have a caption. A downward arrow next to HOMO column would help readability. Table 3 says "MAE" in the column title. Please make them consistent.
* The paper uses two benchmarks: linear algebra and QM9. But most of the experiments are performed only on QM9.

### Questions
1) Can you please explain in more details what kind of spurious correlation can explain the negative correlation between invariance and prediction error for eigenvalues?

2) Did you do any hyperparameter search for Llamas?

### Soundness
2

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
3

### Summary
This paper explores several hypotheses of why language models have a hard time modelling linear algebra and the 3D structure of molecules (and by extension other numerical problems). The hypotheses include (1) conditional vs. unconditional modelling (conditional vs. joint distribution); (2) causal masking (encoder-decoder vs. decoder-only); (3) symmetry invariance; (4) tokenization schemes (discrete vs. continuous representations); and (5) natural language pre-training. The findings are that (1), (2) and (5) are not very important, whereas (3) and (4) are relevant (symmetry invariance is a strong predictor of final performance, and continuous embeddings outperform discrete embeddings).

### Strengths
I found the paper well-motivated and situated in the literature, and I appreciate the format of the paper (exploring a variety of hypotheses to generate insight into existing model behaviour). The number of experiments is sizeable and their setup seems well thought out and overall I don't have any concerns with the specific experimental setups.

### Weaknesses
Overall though, I found the narrative of this paper lacking. For someone who doesn't have a background in LLMs and structured numerical data I had a hard time imagining what sort of tasks exactly are being envisioned, i.e., what is the advantage of doing quantum chemistry with an LLM compared to using custom networks? (And is the goal here to study shortcomings of LLMs, or to try and find good models for structured numerical problems?) And given the experimental results, what do these experiments say about the path forward? Perhaps my lack of knowledge of this particular problem plays a role here, but the final recommendation of trying to "close [the gap between xVal and discrete inputs] by extensively pretraining on synthetic data" seems underwhelming. If the experiments don't suggest a clearer path forward, perhaps this particular experimental setup wasn't as insightful as it could have been?

I also think it would be useful to provide some small examples or illustrations of the problems being studied here (e.g., what a single HOMO task looks like).

### Questions
See above.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper, "The Promises and Pitfalls of Language Models for Structured Numerical Data," explores the challenges and potential of applying autoregressive language models to structured numerical data, specifically within the domain of quantum chemistry. The authors conduct extensive experiments involving thousands of language models that vary across several dimensions: architecture, model size, tokenization strategy, loss function, and pretraining method. They demonstrate that language models often underperform compared to domain-specific models on predictive tasks involving structured numerical data, such as 3D molecular structures, and provide insights into potential reasons for these limitations. Key findings highlight that capturing invariance properties correlates strongly with predictive performance and that text pretraining provides limited benefit on these tasks. This study provides a comprehensive examination of the limitations of language models for numerical data and presents multiple areas where improvements could help bridge the performance gap.

### Strengths
I’m not an expert in this field, so my evaluation is based on my general experience in LLMs and deep learning.

- **Originality**: This paper’s originality lies in the hypotheses they propose and test regarding LLM training for structured numerical data, a relatively underexplored area, particularly in quantum chemistry. That said, I could be missing significant prior works, as I don’t have expertise in this specific area.
  
- **Quality**: This paper is a heroic effort to pack a lot of content into one submission. The authors demonstrate strong experimental rigor, testing thousands of models and covering multiple factors, including tokenization methods and model pretraining, which adds to the robustness of their findings.

- **Clarity**: Generally, the explanations are clear, and the figures effectively illustrate key findings. The authors also provide an accessible codebase for reproducibility.

- **Significance**: Given the rapid advancements in applying language models across diverse domains, this study addresses timely questions about LLM limitations on structured numerical data. These insights could help shape future research directions.

### Weaknesses
 - **Overly Broad Scope**: The paper attempts to cover a vast amount of content in one submission, which brings two main challenges:
  
  1. **No Clear Takeaway Message**: With so much content, the reader might feel a bit overwhelmed, and after reading, may lack a clear takeaway message. The sheer volume of experiments, while demonstrating rigor, obscures the core findings. The paper presents a 'bag of hypotheses' without a clear hierarchy or prioritization, making it difficult to discern the most significant results. For example, the impact of different tokenization strategies is explored alongside pretraining methods, but the relative importance of these factors isn't clearly established, leaving the reader unsure which aspect warrants the most attention.
  
  2. **Lack of Depth in Analysis**: Some areas lack the depth they deserve. The broad scope results in a study that struggles to deeply focus on any single hypothesis. While the paper identifies key challenges (e.g., causal masking and tokenization), the current structure makes it difficult to evaluate each hypothesis thoroughly. Narrowing down to specific experiments would enhance the clarity and impact of each takeaway. For instance, the discussion of invariance properties is promising, but the paper does not delve into specific augmentation techniques or their impact on the model's ability to learn these invariances. The analysis remains somewhat superficial, lacking the detailed investigation needed to draw strong conclusions.

  My favorite part is Section 6 on conditional vs. unconditional modeling. I think this section could totally stand alone as a paper (assuming there’s little prior work thoroughly investigating mixing conditional and unconditional modeling), with more in-depth experiments and analysis. I find this idea quite straightforward, yet it’s one I hadn’t considered deeply before reading this submission. I’m curious if this phenomenon holds in a more general setting beyond the author’s structured numerical data context. While I’m not an expert in this field, this topic stands out to me as the most intriguing, and I’d appreciate deeper, more thorough experiments and analysis here. 

  Overall, the current structure feels like a “bag of hypotheses”—probably correct but without a definitive answer for each. A paper that focuses on one hypothesis and runs every relevant experiment to add breadth and depth could deliver a much stronger message, rather than a few weaker ones.

### Questions
1. **On the Scope of the Paper**: Have the authors considered breaking the study into multiple papers? For instance, focusing on conditional vs. unconditional modeling in a separate work could allow for a more comprehensive analysis.

2. **Section 6 Expansion**: Could the authors provide more experimental results or analysis to investigate whether mixing conditional and unconditional modeling has general implications beyond their structured numerical data setting?

### Soundness
3

### Presentation
3

### Contribution
3
