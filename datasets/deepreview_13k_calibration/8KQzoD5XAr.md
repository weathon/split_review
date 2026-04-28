# CraftRTL: High-quality Synthetic Data Generation for Verilog Code Models with Correct-by-Construction Non-Textual Representations and Targeted Code Repair

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 6, 6, 8

## Abstract
Despite the significant progress made in code generation with large language models, challenges persist, especially with hardware description languages such as Verilog. This paper first presents an analysis of fine-tuned LLMs on Verilog coding, with synthetic data from prior methods. We identify two main issues: difficulties in handling non-textual representations (Karnaugh maps, state-transition diagrams and waveforms) and significant variability during training with models randomly making ``minor'' mistakes. To address these limitations, we enhance data curation by creating correct-by-construction data targeting non-textual representations. Additionally, we introduce an automated framework that generates error reports from various model checkpoints and injects these errors into open-source code to create targeted code repair data. Our fine-tuned Starcoder2-15B outperforms prior state-of-the-art results by 3.8\%, 10.9\%, 6.6\% for pass@1 on VerilogEval-Machine, VerilogEval-Human, and RTLLM.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper does a thorough evaluation of LLMs for verilog code generation. They first analyze existing model performance on Verilog code generation tasks, identify that "non-textual representations" are commonly mis-reasoned about, use this to motivate two new methods for improving SDG for verilog code gen tasks, and test their approach against other SDG approaches. They find that their method outperforms baselines.

### Strengths
* This paper presents a clear discussion of an important and under-explored topic. Low-level programming languages are an appealing area in which to automate code reasoning, and programs in HDLs are notoriously difficult to verify. 
* thorough evaluation in terms of comparison to other SDG methods and other baselines. Appropriate ablations further convey the value of all components of their approach.
* the code repair generation process is compelling, and validation well-grounded in existing literature. I anticipate that it's highly transferrable to other domains of data as well. 
* the combination of using hand-crafted methods for highly-underrepresented or challenging concepts ("non-textual elements") and automated self-consistency-based methods for intermediate concepts (generating the repair data) paints a cohesive picture for SDG, especially in this domain.

### Weaknesses
 * the data generation processes for Karnaugh maps, state-transition diagrams, and waveforms are pretty hand-crafted. This makes this method difficult to transfer to other identified model weakness categories, and requires human-tuning to identify the best data gen method per category. This approach also may not work as well, if at all, on some categories. (For example, the findings of L461 that indicate the Waveforms problems do not improve as much as the other approaches.) An automated method for designing the data construction may scale better. (out of scope for this paper though, and I would not consider this a reason for rejection)

 * Fig 1 is kind of confusing. Why choose checkpoints 1 and 2? Would we hope for the pass@k for checkpoint 2 to be higher than for chkpt 1?  This scatter-plot resembles a confusion matrix-- why choose the scatter plot representation over a different option? The value of figure 1 is made more apparent once we see figure 5. Maybe the two could be presented closer to one another in a camera-ready. How were the "solvable" and "unsolvable" regions chosen?
* L319: how do we know that the ability to self-correct (validating via self-consistency) is due to a good error report, and not the model's ability to correct independent of the error report? Especially since the examples from which error reports are generated did yield both correct and incorrect generations, to start with.
* is the amount of training data consistent between all rows of Table 6?

### Questions
* Fig 1 is kind of confusing. Why choose checkpoints 1 and 2? Would we hope for the pass@k for checkpoint 2 to be higher than for chkpt 1?  This scatter-plot resembles a confusion matrix-- why choose the scatter plot representation over a different option? The value of figure 1 is made more apparent once we see figure 5. Maybe the two could be presented closer to one another in a camera-ready. How were the "solvable" and "unsolvable" regions chosen? 
* L319: how do we know that the ability to self-correct (validating via self-consistency) is due to a good error report, and not the model's ability to correct independent of the error report? Especially since the examples from which error reports are generated did yield both correct and incorrect generations, to start with.
* is the amount of training data consistent between all rows of Table 6?

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
1

### Summary
The paper introduces CraftRTL, a novel approach to Verilog code generation by leveraging a combination of synthetic data generation and targeted code repair to improve accuracy and robustness.

### Strengths
The primary contributions of this paper include the introduction of correct-by-construction data generation, which focuses on non-textual data representations that are essential for Verilog code and often challenging for LLMs. By incorporating Karnaugh maps, state-transition diagrams, and waveforms, the model’s capacity to interpret and generate these complex data formats improves. The experimental results demonstrate notable improvements over previous approaches on multiple benchmarks​.

### Weaknesses
The methods presented, particularly the correct-by-construction data targeting non-textual representations, are tailored heavily to Verilog-specific constructs such as Karnaugh maps, state-transition diagrams, and waveforms. While this adaptation effectively improves performance for Verilog code generation, the approach may have limited applicability to other hardware description languages or general programming languages that do not rely on these specific data formats. A broader discussion on how these techniques could be generalized would strengthen the paper's impact.

Several figures and tables in the paper, notably Figures 2, 4, 5, and 6, as well as Tables 4 and 5, suffer from presentation clarity issues. Figures lack a cohesive and clear structure, making it difficult for readers to follow the exact steps. For instance, Figure 2 does not clearly illustrate the data generation process, and the transitions between different stages are not well-defined. Similarly, Figures 4, 5 and 6 lack clear labeling and annotations to guide the reader through the presented information. In Tables 4 and 5, the inconsistent formatting of model types and unclear emphasis on the best-performing results within each category lead to potential confusion in understanding the experimental results. The lack of consistent formatting makes it difficult to quickly compare the performance of different models.

### Questions
1. Could the authors discuss how this method for Verilog-specific elements might be adapted for other HDLs or general programming languages?

2. Figures 2, 4, 5, and 6, along with Tables 4 and 5, could benefit from clearer formatting and structure. Could the authors enhance these visuals to improve readability and clarify how the best results are highlighted across different model types?

### Soundness
3

### Presentation
1

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
This paper discusses two main issues when LLMs  handling Verilog code: models have difficulty handling non-textual elements in problem statements and models making "minor" programming mistakes. To address these issues, the authors specifically created a transformed non-textual dataset and code repair dataset to fine-tune the model. The results demonstrate that the fine-tuned Starcoder2-15B surpasses the prior state-of-the-art results in Pass@1 performance, achieving improvements of 3.8\%, 10.9\%, and 6.6\% on VerilogEval-Machine, VerilogEval-Human, and RTLLM, respectively.

### Strengths
1. The paper conducts a detailed empirical analysis of the two main issues in Verilog code.
2. The paper provides a thorough comparison with existing methods and shows good performance.

### Weaknesses
1. The main contribution of this work lies in constructing a fine-tuning dataset to address non-textual data and minor error issues. The technical contribution of the paper is limited.
2. What is the specific definition of "minor" errors, and what common characteristics do they share?
3. The font size of Figures 2 and 4 is too small to read.

### Questions
1. Why focus solely on karnaugh maps, state-transition diagrams, and waveforms? They do not represent all types of non-textual representations.
2. It is essential to ensure that the generated error report can effectively guide the model in correcting errors. How do the authors validate its effectiveness?
3. In the "Targeted Code Repair Dataset" section, I suggest the author to  provide classification and proportion of the "minor" errors. Additionally, were any additional data augmentation measures taken for high-frequency errors during dataset construction?

### Soundness
3

### Presentation
2

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
- This paper performs a thorough analysis of fine-tuned LLMs on Verilog code, and revealing two main challenges of automated Verilog code generation
- This paper creates a large number of correct-by-construction data to ensure solution correctness, incorporating Karnaugh Maps, state-transition diagrams, and waveforms
- This paper develops an automated framework that utilizes LLMs to generate error reports from benchmark problems
- Its evaluation results demonstrate that models fine-tuned with our data achieve state-of-the-art performance on Verilog coding, outperforming prior SOTA results by 3.8%, 10.9%, 6.6% for pass@1 on VerilogEval-Machine, VerilogEval-Human, and RTLLM, respectively

### Strengths
- This paper is clearly written and easy to comprehend
- This paper is well-motivated and address an important downstream task, automated Verilog code generation
- This paper includes a comprehensive and reliable data construction pipeline
- This paper conduct a comprehensive evaluation on three LLMs with SOTA baselines

### Weaknesses
Actually I like this paper, especially the data construction section; however, there are still some minor concerns:

- "Quality Assurance with LLM Validation" (Line 317): Please provide more evidence about the choice of LLM validation. What is the rationale (or its limitations) of not using deterministic validation approaches, e.g., model checking? Specifically, how does the performance of the chosen LLM compare to deterministic methods in terms of identifying and correcting errors in Verilog code? It would be beneficial to understand the trade-offs in terms of accuracy, computational cost, and scalability.
- In Section 2.3, you mention "significant variability in the model’s pass rate on specific benchmark problems across different checkpoints" (Line 164), while the results in Figure 1 indicates a highly positive correlation. Also, 15% discrepancies is also acceptable between two checkpoints. Can you provide me with a stronger evidence to support this claim, e.g., Pearson Correlation Coefficient, or explain why such difference is significant in this task? It is unclear why a 15% discrepancy is considered significant, especially given the inherent stochasticity in training LLMs. A more rigorous statistical analysis is needed to justify this claim.
- Application scenario: This paper mainly utilizes domain specific patterns of various types of Verilog while it might be difficult when applied to similar tasks, e.g., code generation without sufficient training data. The reliance on domain-specific patterns raises concerns about the generalizability of the approach to other hardware description languages or programming languages where such patterns may not exist or be as well-defined. It would be helpful to discuss the limitations of the approach in scenarios with limited training data or different coding styles.
- Reproducibility Statement: this subsection exceeds the 10 pages limit. I think it should be placed within the first 10 pages or directly moved to appendix
- Availability: this paper does not provide an available artifact

### Questions
- Checkpoint Selection: what is the selection criteria of your checkpoints in Figure 1 and Figure 5? You mentions "two consecutive checkpoints" in Line 434. Additionally, you only fine-tune your model for one epoch (Line 364), so at least one checkpoint might not see all training data. Whether such difference affects your results?
- Application Scenario: This paper addresses an important problem in Verilog code generation utilizing domain knowledge of Verilog. So I am curious how such approach is applied to similar tasks, e.g., code generation without sufficient training data?

### Soundness
4

### Presentation
4

### Contribution
3
