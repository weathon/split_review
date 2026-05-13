# SQL-GEN: Bridging the Dialect Gap for Text-to-SQL Via Synthetic Data And Model Merging

- Decision: Reject
- Scores: 5, 6, 6

## Abstract
Recent advances in Text-to-SQL have largely focused on the SQLite dialect, neglecting the diverse landscape of SQL dialects like BigQuery and PostgreSQL. This limitation is due to the diversity in SQL syntaxes and functions, along with the high cost of collecting and curating SQL-specific training data. To address this, we introduce SQL-GEN, a framework for generating high-quality synthetic training data for any SQL dialect, guided by readily available dialect-specific tutorials.  SQL-GEN significantly improves cross-dialect Text-to-SQL performance, boosting execution accuracy by up to 20\% over existing methods. This performance gain narrows the gap with models trained on large-scale human-annotated data. Furthermore, combining synthetic data from SQL-GEN with human-annotated data yields additional improvements of up to 5.6\%.  To unify multi-dialect capabilities within a single model, we propose a novel Mixture-of-Experts (MoE) initialization that leverages the shared knowledge across dialects. Our approach merges self-attention layers from dialect-specific models and initializes expert gates using dialect-specific keywords. This leads to a versatile model optimized for multiple SQL dialects, outperforming single-dialect models and significantly enhancing overall performance.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper introduces the SQL-GEN framework, which bridges the dialect gap for text-to-SQL systems by generating high-quality synthetic data for any dialect and merging dialect-specific models into a unified model using a novel Mixture of Experts (MoE) initialization method. The framework significantly improves execution accuracy on unseen real-world multi-dialect benchmarks and reduces the gap compared to large-scale human-annotated data.

### Strengths
1. The method is evaluated on three SQL dialects and proves its effectiveness.
2. The author has built a text-to-sql dataset that includes SQL dialects. If this dataset is open source, it will be of certain value to research.

### Weaknesses
1. The paper presents contributions that, while valuable, appear to have limited novelty compared to existing work in the field[1].
2. In addition, from the results, the improvement of synthetic data is not as good as that of bird train set.

### Questions
No more questions. Please see above.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
In the well-studied text-to-SQL task, the authors examine handling multiple SQL dialects and propose SQL-GEN, a three-step method to adapt text-to-SQL models trained on one SQL dialect to other dialects by generating synthetic text-to-SQL samples. They also introduce a Mixture of Experts approach to merge dialect-specific SQL models into a single model for efficient cross-dialect knowledge sharing and reducing maintenance costs by selectively activating dialect-specific experts based on the input. The method is tested on BIRD and Paglia benchmarks and is evaluated against baseline datasets to validate SQL-GEN's efficacy.

### Strengths
- **Originality**
    - The task of addressing dialects in text-to-SQL systems is nascently explored, and this paper makes a valuable contribution by introducing a novel MoE approach to manage multi-dialect scenarios effectively.
- **Quality and Clarity**: 
     - The paper is generally easy to follow.
     - The experiments comprehensively test SQL-GEN across multiple benchmarks and datasets and validate the performance.

### Weaknesses
 - Figures, especially Figures 3 and 4, are somewhat dense and challenging to interpret. A clearer visual representation or more detailed explanations would enhance accessibility.
- The text in Figure 5 could be enlarged to improve readability, as it currently appears difficult to see.

### Questions
- On a side note, it would be interesting to consider cross-lingual transfer methods for text-to-SQL as seen in multilingual NLP tasks, which might provide a useful baseline for comparison.

### Soundness
3

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
5

### Summary
The paper addresses the challenges of adapting Text-to-SQL systems across SQL dialects like BigQuery, PostgreSQL, and SQLite. Traditional Text-to-SQL models, optimized for SQLite, struggle with dialect-specific syntax variations, making translation and model adaptability challenging. SQL-GEN proposes a synthetic data generation method, SQL-GEN, which leverages dialect-specific SQL tutorials to create diverse, high-quality training samples for any SQL dialect. It introduces a Mixture of Experts (MoE) approach for merging dialect-specific models, enhancing multi-dialect capability.

### Strengths
1. SQL-GEN’s synthetic data generation effectively addresses the lack of annotated data for various SQL dialects, enhancing Text-to-SQL systems' adaptability across dialects without needing human annotations. And it is the first work to discuss its important problem.
2. The moe architecture efficiently merges dialect-specific models into a unified framework, promoting knowledge transfer and improving performance across dialects, making the system resource-efficient for real-world use.
3. SQL-GEN enhances execution accuracy by up to 20% over previous methods, making Text-to-SQL models more reliable for multi-dialect databases, with potential performance improvements in specific dialects like PostgreSQL and BigQuery.
4. By reducing the dependency on human annotations and enabling effective multi-dialect handling, SQL-GEN offers a cost-efficient approach to multi-dialect Text-to-SQL training. It would be better to open-source the generative model to help the community.

### Weaknesses
1. While SQL-GEN aims to create a unified model that bridges dialect gaps, merging dialect-specific models can dilute the depth of expertise for each dialect, leading to a possible trade-off between dialect-specific expertise and generalizability. It would be better to discuss the drawback of SQL-GEN in each dialect-specific example and provide a detailed analysis of performance on dialect-specific features or edge cases for each dialect. This could help clarify if and where any expertise dilution occurs.

2. The Mixture of Experts (MoE) approach enables the merging of dialect-specific models, but it also requires substantial computational resources for training, fine-tuning, and deploying models, especially as more dialects are added. It would be better to incorporate an easy SFT baseline to compare and provide a computational resource comparison between their MoE approach and a standard fine-tuning approach for multiple dialects. This would give readers a clearer picture of the trade-offs involved.

### Questions
1. How does SQL-GEN handle dialect-specific syntax that drastically changes query logic, such as proprietary SQL functions that are unique to one dialect? It would be better to provide specific examples of how SQL-GEN handles a few key proprietary functions from different dialects, and discuss any limitations in this area.
2. What measures are in place to ensure the synthetic queries generated by SQL-GEN align closely with real-world dialect usage beyond benchmarks?

### Soundness
3

### Presentation
3

### Contribution
3
