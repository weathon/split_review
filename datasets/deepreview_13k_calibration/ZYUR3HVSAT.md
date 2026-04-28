# Human-Instruction-Free LLM Self-Alignment with Limited Samples

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Aligning large language models (LLMs) with human values is a vital task for LLM practitioners. Current alignment techniques have several limitations: (1) requiring a large amount of annotated data; (2) demanding heavy human involvement; (3) lacking a systematic mechanism to continuously improve. In this work, we study aligning LLMs to a new domain with limited samples (e.g. < 100). We propose an algorithm that can \textit{self-align} LLMs \textit{iteratively} without active human involvement. Unlike existing works, our algorithm relies on neither human-crafted instructions nor labeled rewards, significantly reducing human involvement. In addition, our algorithm can self-improve the alignment continuously. The key idea is to first retrieve high-quality samples related to the target domain and use them as In-context Learning examples to generate more samples. Then we use the \textit{self-generated} samples to finetune the LLM iteratively. We show that our method can unlock the LLMs' self-generalization ability to perform alignment with near-zero human supervision. We test our algorithm on three benchmarks in safety, truthfulness, and instruction-following, and show good performance in alignment, domain adaptability, and scalability.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper proposes ISARA, a novel approach for aligning LLMs with minimal human supervision. The key innovation is using retrieval-augmented in-context learning to generate high-quality training samples from a small seed dataset, followed by iterative self-improvement through fine-tuning. The method is tested on three benchmarks focusing on safety, truthfulness, and instruction-following capabilities.

### Strengths
1. The ISARA method works with very limited initial samples (<100), which significantly reduces human labor compared to traditional alignment methods.

2. It successfully works with smaller models (as small as 350M parameters), uses retrieval-augmented in-context learning to maintain quality without human guidance. It also implements an iterative self-improvement mechanism that enhances alignment over multiple cycles.

3. Experiments demonstrate effectiveness across multiple domains (safety, truthfulness, instruction-following). It shows robust domain generalization capabilities. It can be applied to various model sizes and domains without redesigning principles or retraining reward models.

### Weaknesses
1. Dataset usage: I notice that this paper splits the BeaverTails, TruthfulQA, and AlpacaEval datasets for both training and test, which is not appropriate. In real world, we cannot assume getting in-distribution samples as seed examples, especially for instruction-following. Most works in LLM alignment would choose other datasets, such as ShareGPT, Alpaca for training. 

2. Weak baselines: This paper only compare ISARA with some weak baselines. The SFT baseline only finetunes the model with around 64 samples, which is 6-7 times fewer than ISARA, and other baselines do not finetune the model. Therefore, the experiment results are not convincing. There is no reason that none of the methods in Table 1 is selected as baseline.

3. Evaluation Metric: This paper uses ROUGE-L for the evaluation of TruthfulQA, which is also questionable. The original TruthfulQA paper showed that ROUGE is not an accurate metric for evaluation. Therefore, most TruthfulQA evaluations adopt multiple choice accuracy as the metric. 

4. Inconsistent experiment settings: The experiment settings for harmlessness, truthfulness and instruction-following are inconsistent.
	- The iterative mechanism, which is one of the key designs, seems only appear in harmlessness experiments. 
	- The TruthfulQA experiments do not have ICL and ICL-kNN baselines.

5. Statements: 
	- In Table 1, what is the meaning of ''No Human Instructions''? Why is self-instruct need human instructions and your method and ReST does not? Why cannot self-instruct achieve continuous enhancement by iteratively creating samples?
	- The authors claim that "Current self-alignment can work only on large models." but I did not see any experiment results validating it.

6. Writing: The preliminaries of the generation process of LLMs are unnecessary.

### Questions
- What is the initial seed answers? Are they human-generated ground truth answers? For AlpacaEval, are they generated answers from a specific model?

- ISARIL in Figure 2 should be ISARA.

### Soundness
2

### Presentation
2

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
ISARA is a new method for aligning language models using minimal training data (<100 examples) and minimal human-crafted instructions. The system works by retrieving relevant examples, using them for in-context learning to generate more training data, and iteratively fine-tuning the model. Unlike previous approaches that required very large models (65B+ parameters), ISARA works effectively with models as small as 350M parameters.

Testing on benchmarks for safety, truthfulness, and instruction-following showed ISARA outperforms traditional supervised fine-tuning on training data while demonstrating strong generalization across domains. The method efficiently expands the initial training data by over 6x while maintaining quality. Its key innovation is achieving good alignment results through an automated, iterative process that requires minimal human involvement.

### Strengths
**Originality:** The paper introduces ISARA, a novel LLM alignment method that reduces reliance on human-crafted instructions and reward models. It employs an iterative training loop that enhances alignment over time and combines retrieval-augmented in-context learning with iterative fine-tuning. ISARA demonstrates that smaller models (as small as 350M parameters) can achieve effective alignment, challenging previous norms.

**Quality:** ISARA's effectiveness is backed by comprehensive empirical evaluations on safety, truthfulness, and instruction-following. Ablation studies explore model performance across different sizes, domain generalization, and iterative vs. one-time training. The method uses strong experimental controls, clear baselines, and filtering mechanisms to maintain data quality, resulting in notable improvements over conventional methods.

**Clarity:** The paper is clear and well-structured, featuring detailed algorithm descriptions, pseudocode, and thorough implementation notes. The experimental setup is transparently reported, and figures and tables effectively illustrate key concepts and results. Qualitative examples of model outputs further enhance understanding.

**Significance:** ISARA addresses a major challenge in LLM development by reducing human involvement and data requirements for alignment. Its use of smaller models makes alignment more accessible and cost-effective. The automated, scalable process (with 6x+ data generation efficiency) could accelerate LLM alignment and broaden its applicability, making it a valuable tool for practitioners and organizations.

### Weaknesses
**Insufficient Comparison with State-of-the-Art Methods:**
My biggest concern is that the paper critiques existing alignment methods in its introduction but does not include comparisons in its experiments. While it suggests potential advantages over techniques like Self-Instruct and other recent data generation approaches, it only benchmarks against basic SFT and pre-trained models. This omission leaves the paper's claims about superiority unverified and its relative performance unclear.

**Simplistic Filtering Mechanism:**
The filtering criteria look quite basic. Using thresholds (e.g., ROUGE-L > 0.7, 5-word minimum) without empirical or theoretical backing raises questions about the approach's robustness. The absence of advanced quality checks, such as semantic coherence or alignment-specific filtering, makes it unclear how the method guarantees high-quality generated data. 

**Computational Efficiency Concerns:**
The paper does not analyze computational costs or efficiency, omitting details on training expenses for fine-tuning iterations, retrieval processes, or the full pipeline. Without comparisons to one-time training methods or insights into the trade-offs between iterative training and performance gains, the approach's practical utility and cost-effectiveness remain uncertain. This analysis is crucial for understanding deployment feasibility.

### Questions
Considering the simplicity of the filtering methods and their lack of emphasis on bias correction, how does the approach prevent the model from collapsing or amplifying its own biases over iterations? Shouldn't incorrect or non-helpful examples be filtered out to ensure data quality?

For further context and related questions, please see my Weakness section.

### Soundness
2

### Presentation
4

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a human-instruction-free LLM self-alignment method under the limited samples scenario. The contributions of this paper are summarized as follows: (i) The proposed algorithm can self-align LLMs iteratively without active human involvement, eliminating the need for human-crafted labeling or instruction design. (ii) Experiments on three benchmarks (safety, truthfulness, and instruction-following) show that the proposed algorithm can self-improve the alignment continuously.

### Strengths
1. The self-alignment method proposed in this paper can achieve alignment with near-zero human supervision, making it highly practical for real-world applications.

2. Experiments conducted across three key alignment benchmarks demonstrate the effectiveness of the self-alignment method.

3. The paper is clearly organized and well-written.

### Weaknesses
1. The novelty of the proposed method is relatively lacking.

2. The conducted experiments seem to be not sufficiently comprehensive.

### Questions
1. The method proposed in this paper seems to simply apply Retrieval-Augmented ICL to the self-alignment scenario, which appears to lack sufficient novelty. The authors are encouraged to provide a more detailed summary of their contributions in the introduction.

2. In Tables 2 and 3, the performance of method ICL-kNN, which does not require parameter fine-tuning, is comparable to the proposed ISARA. The authors are encouraged to provide a comparison of resource consumption or runtime between ICL-kNN and ISARA.

3. The baselines in the experiments focus on naive pre-training, SFT, and ICL-related methods. It appears that none of the self-bootstrapping methods listed in Table 1 are included in the experiments. While a direct comparison might seem unfair (methods listed in Table 1 require external reward model or human instructions), comparing against them helps us understand the current performance of SOTA and whether the proposed method ISARA (requires ear-zero human supervision) has limitations.

4. Why most experiments only show the results of the first two iterations, even if sometimes the results of the first two iterations are worse than ICL-kNN (for example, domain generalization evaluation in Fig. 2)?

5. Typos: (i) The “ISARIL” in Fig. 2 should be “ISARA”. (ii) “ISARA (N = 512 Iter 2 consistently outperforms ISARA (N = 1024) Iter 1” lacks “)”. (iii) “Figure 4: Data scaling ratio of ISARA in safety alignment” should be “Table 4”. (iv) The authors are encouraged to review the current manuscript carefully.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
Iterative Self-Alignment with Retrieval-Augmented In-Context Learning (ISARA) is proposed to align large language models (LLMs) with specific target domains using only a few examples and without human-designed instructions or external reward models. Unlike traditional methods, ISARA leverages retrieval-augmented in-context learning to generate high-quality responses by retrieving relevant examples from the target domain. It iteratively fine-tunes the LLM using self-generated samples, gradually improving alignment without the need for extensive human intervention or large-scale data labeling efforts. This approach enhances alignment performance over time and demonstrates robust domain generalization capabilities across safety, truthfulness, and instruction-following benchmarks.

### Strengths
1. The authors point out the issue of high computational costs in existing alignment methods.
2. The authors propose a retrieval-augmented strategy to reduce alignment costs.

### Weaknesses
1. The authors point out in the abstract that existing methods lack "a systematic mechanism to continuously improve." However, we did not find a detailed explanation or analysis of this assertion in the introduction.

2. The motivation is unclear. The authors analyze in the abstract and introduction the limitations of current self-alignment methods in general domains that rely on artificial datasets. They point out that existing methods lack "a systematic mechanism to continuously improve." However, the problem the authors propose is to self-align LLMs with a few examples to a target domain.

3.  In line 38, the authors mention that existing self-alignment models often rely on partially annotated datasets. Could it be that these datasets are intended to ensure the quality of datasets generated by LLMs? We find that the authors do not provide a detailed evaluation of the quality of their own dataset, which raises concerns for us.

4. In section 4, the authors mention that their method relies on a set of QA pairs, but they do not provide detailed information about the sources of these pairs. According to their description in the experiment section, if these pairs also include human annotations, it appears not to align with the contribution claimed by the authors.

5. The justification for the Iterative Enhancement mechanism is unclear. The authors state in the paper that through experiments, they found the iterative optimization mechanism improves model alignment performance. However, they do not articulate the motivation behind introducing this mechanism.

6.  There is a lack of an ablation study for the stopping threshold hyperparameter.

7. The baseline is too simplistic. The authors did not compare their work with other recent advancements in self-alignment-based methods or training-free approaches. Do you consider using a more advanced LLM as a backbone?

8.  The authors did not provide performance metrics for simple alignment strategies based on manually annotated data in their evaluation. This could potentially better highlight the contributions of the paper.

9.  For domain generalization, since the selected domains (such as malicious speech) do not exhibit significant differences, can the authors provide performance metrics on domains with larger disparities, such as truthfulness and safety?

### Questions
1. The references for the k-nearest-neighbors and embedding model are missing in Section 4.1.

### Soundness
2

### Presentation
3

### Contribution
2
