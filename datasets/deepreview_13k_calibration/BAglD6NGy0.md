# ROUTE: Robust Multitask Tuning and Collaboration for Text-to-SQL

- Decision: Accept
- Avg Score: 6.25
- Scores: 6, 8, 5, 6

## Abstract
Despite the significant advancements in Text-to-SQL (Text2SQL) facilitated by large language models (LLMs), the latest state-of-the-art techniques are still trapped in the in-context learning of closed-source LLMs (e.g., GPT-4), which limits their applicability in open scenarios. 
To address this challenge, we propose a novel RObust mUltitask Tuning and collaboration mEthod (ROUTE) to improve the comprehensive capabilities of open-source LLMs for Text2SQL, thereby providing a more practical solution.  Our approach begins with multi-task supervised fine-tuning (SFT) using various synthetic training data related to SQL generation.  Unlike existing SFT-based  Text2SQL methods, we introduced several additional SFT tasks, including schema linking, noise correction, and continuation writing.  Engaging in a variety of SQL generation tasks enhances the model's understanding of SQL syntax and improves its ability to generate high-quality SQL queries. Additionally, inspired by the collaborative modes of LLM agents, we introduce a Multitask Collaboration Prompting (MCP) strategy.  This strategy leverages collaboration across several SQL-related tasks to reduce hallucinations during SQL generation, thereby maximizing the potential of enhancing Text2SQL performance through explicit multitask capabilities. Extensive experiments and in-depth analyses have been performed on eight open-source LLMs and five widely-used benchmarks. The results demonstrate that our proposal outperforms the latest Text2SQL methods and yields leading performance.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper addresses the limitations of current Text-to-SQL approaches that rely heavily on in-context learning using closed-source LLMs, such as GPT-4, which can cause privacy issues. To overcome these issues, the authors propose ROUTE, a comprehensive solution to enhance open-source LLMs' Text2SQL capabilities. ROUTE utilizes a multitask supervised fine-tuning approach incorporating tasks like text-to-SQL, schema linking, noise correction, and continuation writing to broaden the model's SQL generation skills and reduce the risk of overfitting. Additionally, a Multitask Collaboration Prompting (MCP) strategy is employed during inference to decompose the SQL generation process into simpler sub-tasks, reducing hallucinations and improving performance.

### Strengths
1) The proposed method significantly improves the performance of open-source LLMs and outperforms all existing methods trained on open-source LLMs.

2) The proposed MCP approach not only enhances the performance of models trained with MSFT but also improves other models.

3) The novel MSFT method substantially boosts model performance compared to standard SFT.

### Weaknesses
1) Although this paper focuses more on open-source LLMs, some recent approaches, such as CHASE-SQL, Distillery, and CHESS, are not included as benchmarks in their experiments.

2) The proposed approach is a multi-step pipeline that can be prone to error propagation. To better understand the performance of the schema linking module and ensure it is not introducing errors into the pipeline, it would be beneficial to report the precision and recall of the schema linking module, as done in CHESS and DTS-SQL.

3) The performance gap with the close-source LLMs is still large, roughly 13% on BIRD development set, which makes the applicability of this approach limited to the scenarios where privacy and local LLMs is essential.

### Questions
1). For the open-source LLMs and super large databases such as some of the databases in BIRD benchmark, how these large schema are fitted into the prompt of the open-source models?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
The paper introduces “ROUTE,” a novel approach to (1) finetune open-source large language models (LLMs) for Text-to-SQL through multi-task supervised fine-tuning (MSFT) and (2) leverage multitask collaboration prompting (MCP) for SQL generation during inference. The MSFT tasks include Text-to-SQL, Schema Linking, Noise Correction, and Continuation Writing. The proposed method aims to reduce hallucinations and enhance Text-to-SQL robustness, demonstrated by improved performance on two benchmarks: Spider and BIRD.

### Strengths
1. The paper introduces a multitask learning approach that leverages several text-to-SQL related tasks. Noise Correction is designed to assess whether the execution result of a SQL query correctly answers the question, reducing hallucinations when paired with multi-turn generation.
2. ROUTE demonstrates competitive accuracy, outperforming some closed-source methods on benchmarks, thus showcasing the effectiveness of multitask training over single-task fine-tuning.
3. The authors provide comprehensive experiments using multiple LLMs as base models, demonstrating that ROUTE is generalizable across various LLMs.

### Weaknesses
1. The paper lacks an ablation study on the contribution of each task in MSFT. For instance, the loss from continuation writing is likely already included in text-to-SQL learning after the first token of the SQL prediction. It is unclear how each task directly benefits SQL generation and other inference components.
2. Although Noise Correction helps improve performance, it relies on execution results within the model, which may be difficult to apply to queries with large outputs, such as selecting an entire column. The practical applicability of this component is questionable given the potential for large execution results.
3. While ROUTE demonstrates strong performance on Spider variants compared to baselines, it remains unclear whether these gains are due to improved robustness or general text-to-SQL performance. It would also be valuable to understand how each component contributes to robustness specifically. Dr. Spider [1] is a more comprehensive perturbation dataset with relative robustness evaluation, which could be useful for evaluating ROUTE’s improvement more clearly.

### Questions
For Noise Correction, is it able to handle a large table as the execution result?

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The paper introduces ROUTE, a method for enhancing text-to-SQL capabilities in open-source language models. The approach addresses limitations in current methods that rely heavily on closed-source large language models (LLMs), such as GPT-4, for text-to-SQL tasks. ROUTE leverages Multitask Supervised Fine-Tuning (MSFT) and Multitask Collaboration Prompting (MCP) to improve SQL generation performance by incorporating tasks like schema linking, noise correction, and continuation writing. These tasks enable a collaborative prompting approach that reduces hallucinations in SQL generation. Extensive experimentation on multiple benchmarks with open-source LLMs shows that ROUTE significantly improves SQL generation accuracy and outperforms recent methods using fine-tuning and prompting approaches.

### Strengths
1. The paper incorporates multiple tasks to enhance text-to-SQL capabilities, making the LLM more versatile and capable of handling complex SQL generation scenarios.
2. The paper evaluates ROUTE on several well-known benchmarks and compares its performance with other prompting and fine-tuning methods, demonstrating its effectiveness in real-world applications.

### Weaknesses
1. The authors mention that "Most training-based methods only incorporate the ⟨Question, SQL⟩ pairs for SFT, resulting in degraded performance in other tasks, such as schema linking." However, our approach usually incorporates a ⟨Question, Schema, SQL⟩ tuple for SFT. Additionally, a reduction in schema linking performance cannot be seen as a limitation of existing methods. If a specific task is not included in training, optimal results for that task are not expected. Therefore, this should not be considered a limitation; instead, one could state that training with schema linking can achieve better outcomes.
2. The authors state that "Training LLMs on a single SFT task poses a significant risk of overfitting, which may diminish the model's capability to understand instructions." However, overfitting is not further addressed in the subsequent sections. Could the authors clarify what overfitting entails in the context of SQL tasks, and explain how multi-task training specifically mitigates this risk? Additionally, training on more data and achieving good results may also suggest a potential overfitting scenario.
3. The authors mention that "This strategy leverages collaboration across several SQL-related tasks to reduce hallucinations during SQL generation." However, the term "SQL hallucinations" is not defined, nor is there any discussion in the experimental section explaining how hallucinations are reduced. This claimed advantage, therefore, remains unclear.
4. If Schema Linking, Noise Correction, and Continuation Writing are considered important, could the authors provide the relative improvement metrics for these tasks?
5. There are inconsistencies in writing style, such as using both "text-to-SQL" and "Text-to-SQL" interchangeably. Ensuring uniform terminology would improve the clarity and professionalism of the writing.

### Questions
1. The noise correction process assumes access to well-curated data and high-quality schema information, which might not be available for all databases or domains. Without rigorous data preparation, the model may struggle with hallucinations, as noise correction and schema linking effectiveness are diminished when data quality is compromised.
2.  In low-resource settings where high-quality SQL annotations or database schema information might be scarce, could ROUTE be enhanced by incorporating weak supervision, unsupervised learning, or semi-supervised data to fill gaps?
3. Given that database schemas often change over time in production, can ROUTE adapt to new tables or columns without needing extensive retraining, or would these require ongoing fine-tuning?

### Soundness
2

### Presentation
2

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
The paper proposes ROUTE, a method that involves (1) multi-task training and (2) multi-stage prompting to improve LLMs’ performance on text-to-SQL parsing. Compared to an extensive list of baselines, the proposed ROUTE method demonstrates better parsing accuracy on two established datasets, Spider and BIRD, and three other perturbed variants of Spider.

### Strengths
1. The performance of ROUTE is strong. On two well-established text-to-SQL datasets, Spider and Bird, ROUTE effectively improves the performance of two latest open-weight LLMs, Llama 3.1 and Qwen 2.5, and achieves comparable performance to GPT-4. The performance improvement also holds on three perturbed Spider variants, indicating the robustness of ROUTE.
2. The experiments to evaluate ROUTE are comprehensive. The authors gathered an extensive list of baselines and compared them with ROUTE (or the multi-stage prompting step in ROUTE). Additional experiments and ablation studies of the method further supports some design choices of ROUTE and demonstrates its stable performance improvement across different models and datasets.
3. The paper is easy-to-follow, and the writing is mostly clear.

### Weaknesses
1. It is not very clear what kind of novel contribution this paper is making. The tasks themselves for multi-task training and multi-stage prompting have all been studied in related work, and some of them are rebranded under new terms. To name some examples, “noise correction” is essentially training and prompting LLMs to self-debug [1][2], and the “continuation writing” is simply a subset of text-to-SQL generation by the autoregressive nature of LLMs and has been one of the prompting paradigm for text-to-SQL parsing with LLMs [3][4]. At the framework level, there are also existing papers compiling different tasks to improve LMs’ text-to-SQL performance via multi-task training [5]. Thus, it is opaque how the proposed method combines these existing ideas in a novel way.

2. The noisy correspondence filtering step to pre-process the training data is not fully elaborated, and the contribution of this step to ROUTE is minimal according to the ablation study (#1 vs #3 and #6 vs #8 in Table 3). Training details and quality of the noise filtering model is not discussed, e.g. through an intrinsic evaluation of how accurately it can discriminate noisy examples. The difference between ROUTE’s data synthesis procedure and that of SENSE is not clear. The method to “artificially and randomly introduce errors” (lines 225-230) is also not documented. Overall, this part of the method is not clearly explained, and its contribution in ROUTE is not obvious.

### Questions
1. What is the “pseudo-SQL” used to perform schema linking? How is it implemented? This term only appears twice in the paper without any further elaboration.

2. The use of “hallucination” may not be appropriate here in the context of text-to-SQL parsing. Are the authors simply trying to say incorrect column matching and entity linking?

3. The manuscript would benefit from another round of proof-read to correct typos and standardize term usage, including those mentioned above and some other examples as follows:
- “in-contextual learning” -> “in-context learning” (line 39)
- “promoting-based methods” -> “prompting-based methods” (lines 200, 373)
- “shema linking” -> “schema linking” (line 228)
 - “SQLer$(d_i, \tilde{s}^*)$” -> “SQLer$(d_i, s^*)$” (line 283)

### Soundness
3

### Presentation
3

### Contribution
2
