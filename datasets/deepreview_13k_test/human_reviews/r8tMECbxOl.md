# Language Models Are Good Tabular Learners

- Decision: Reject
- Scores: 5, 6, 3, 8, 3

## Abstract
Transformer-based language models have become the de facto standard in natural language processing. However, they underperform in the tabular data domain compared to traditional tree-based methods. We posit that current models fail to achieve the full potential of language models due to (i) heterogeneity of tabular data; and  (2) challenges faced by the model in interpreting numerical values. Based on this hypothesis, we propose a method titled Tabular Domain Transformer (TDTransformer). TDTransformer has distinct embedding processes for different types of columns. The alignment layers for different types of columns transform column embeddings to a common embedding space. Besides, TDTransformer adapts piece-wise linear encoding for numerical values in transformer-based architectures. We examine the proposed method on 76 real-world tabular classification datasets from the standard OpenML benchmark. Extensive experiments indicate that TDTransformer significantly improves the state-of-the-art methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper is about modifications to the transformer architecture and training objectives for solving [tabular classification tasks](https://huggingface.co/tasks/tabular-classification) using transformers. The authors propose techniques for linearizing tabular data and encoding it into a pre-trained transformer model like BERT or Roberta models. Features are encoded differently depending on whether the feature is categorical, numerical, or binary, with column-type aware position encodings. Further, the paper includes a pre-training strategy based on a self-supervised and a supervised contrastive learning strategy. The authors compare their proposed method, named TDTransformer, with strong baselines used for tabular classification tasks, e.g., XGBoost, and demonstrate reasonable accuracy improvements over these baselines.

### Strengths
- The paper explores an important area -- tabular classification -- where traditional ML methods continue to outperform pre-trained transformers.
- The experiments in the paper seem to be very thorough, covering 76 tabular classification tasks in the openml benchmark and ablations of the key design choices used in the proposed method.

### Weaknesses
Despite its strengths, I feel that the paper needs significant improvements. 

Major concern: Clarity of the Proposed Method.

- Sections 3.1 and 3.2 introduce an embedding E, but Section 3.3 refers to an embedding z without clarifying if or how z is derived from E. Line 261 states, "z_i is the hidden representation for the i-th table row," yet Sections 3.1 and 3.2 only discuss column embeddings, not row embeddings. It appears that "column embedding" might actually refer to "feature embeddings." Therefore, clearer terminology and more consistent naming of components would enhance understanding.
- Section 3.3 (Training Pipeline) begins by mentioning both training and fine-tuning but only elaborates on pre-training objectives (SSCL and SCL). The absence of detail on the fine-tuning objective leaves it unclear how the model was fine-tuned after pre-training.

Minor concerns:
- Line 33: The reference to "tree-based methods" is not clear. Providing specific examples or references would improve clarity.
- Line 110: There appears to be a typo -- should "j_i" be replaced with "y_i"?

### Questions
- How does the proposed method handle columns with string datatype?
- How does the proposed method handle missing values in a table?
- Does the proposed method encode multiple rows in a table, or is it only one row at a time?
- Line 357: Why is subset selection required?

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
4

### Summary
The paper investigates the application of transformer-based language models to tabular data, highlighting their limitations due to the heterogeneous nature of tables and the interpretting of numerical values. To tackle the challenges, the paper proposes Tabular Domain Transformer (TDTransformer), which utilizes distinct embedding processes for different column types and incorporates piece-wise linear encoding (PLE) for numerical columns. This approach aims to enhance the semantic understanding of language models when interpreting tabular data. Extensive experiments on 76 real-world datasets demonstrate that TDTransformer outperforms existing methods, suggesting a promising direction for leveraging language models in the tabular data domain.

### Strengths
- Introduces a novel framework (TDTransformer) specifically designed for tabular data, addressing the limitations of traditional transformer models.
- Employs distinct embedding processes for different column types, improving the model's ability to capture semantic information.
- Employs piece-wise linear encoding (PLE) for numerical columns, improving the model's ability to capture numerical values.
- Demonstrates strong performance across a wide range of real-world datasets, indicating the framework's robustness and applicability.
- The paper is well-organized and easy to follow.

### Weaknesses
- The complexity of the TDTransformer architecture may lead to increased computational costs compared to simpler models.
- The reliance on specific embedding techniques may limit the model's generalizability to other types of data or tasks.

### Questions
Have you ever considered using a different LM as the table encoder (for example, llama or mistral)?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents the Tabular Domain Transformer (TDTransformer) framework, designed to enhance transformer-based models' performance on tabular data. This framework uses distinct embedding processes for categorical, numerical, and binary columns. It also includes a positional encoding. After fine-tuned the model on the data from OpenML benchmark. It outperforms some traditional tree-based and transformer based methods.

### Strengths
This paper provides a comprehensive experiments and evaluations on the traditional methods on tabular data.

### Weaknesses
This proposed framework is lack of novelty,  it largely adapts existing techniques without proposing fundamentally new methodologies, which may limit its impact. For example TAPAS from google is also a transformer-based table parser.

I think authors can follow the paper I posted in the review as well as some other papers related to more up-to-date LLM-based methods to address the concern of out dated baselines, for details please refer to the paper I posted below.

By using transformer-based models with specialized encoding and pre-training techniques, the computational complexity and training cost increase. In many cases, traditional tree-based models like XGBoost or CatBoost achieve comparable results with far less computation, making TDTransformer potentially less attractive for practitioners dealing with tabular data in resource-constrained environments.
Most of the baseline methods are out dated. I'd like to see more comparison with up-to-date methods like the LLM-based. Please provide runtime and resource usage comparisons between TDTransformer and tree-based models, or to discuss scenarios where the increased computational cost might be justified by performance gains.

### Questions
Can you add some experiments on LLM based methods like the ones mentioned in Fang, Xi, et al. "Large language models (LLMs) on tabular data: Prediction, generation, and understanding-a survey." (2024).?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
Transformer language models excel at natural language processing but underperform in tabular data compared to traditional algorithms. Authors claim that this is due to 2 factors: a) heterogenous data in tables, and b) handling of numerical values. Authors propose TDTransformer to fix these issues.
To address a), TDTransformer uses different embedding processes for different types of columns. To address b), TDTransformer adapts piece-wise linear encoding.

They evaluate the model on 76 datasets, improving on SOTA methods.

### Strengths
The main strength of this paper is empirical (results are strong). Additionally, the architectural modifications introduced are well-motivated.

The paper itself is well-written and well-presented, and the code, open-source, looks good at a first glance. I haven't attempted it myself, but I assign high success ratios for reproducing this work.

### Weaknesses
While the motivations for the architectural motivations are well-principled, and they do work empirically, I still think that the paper has some claims that in my view are not backed up by the paper itself or by existing literature. For example, "overcome the transformer-based architectures’ incapability of interpreting heterogeneous data". This is a very strong statement. It's not clear to me whether Transformers have any intrinsic incapability of interpreting heterogeneous data, especially given the success of Transformers handling multimodal data in other domains. Perhaps these statements should be more cautious.

### Questions
Say that I have a computational budget C and I want to obtain the best possible results on a given tabular dataset with some features (e.g., certain number of rows). Should I choose XGBoost or TDTransformer? I'm not necessarily asking for scaling laws (which would be ideal), but I do think readers would appreciate some pointers on this.

Similarly, "PLE introduces an inductive bias that is beneficial to the training process". Is this an inductive bias that is going to be less relevant at scale?

Contrastive losses are sensitive to batch sizes, how does batch size affect TDTransformer?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors present a method called TDTransformer to handle tabular data. They use different embedding methods for categorical, numeric and binary columns: categorical is embedded as text, numeric uses an extension of the PLE method to encode numbers in the [-1, 1] range using quantiles, and binary columns are just 0 or 1. They explore removing positional embeddings.
TDTransformer outperforms XDGBoost on the benchmark they consider.

### Strengths
- Strong performance on OpenML against XGBoost/CatBoost

### Weaknesses
- The presentation is quite lacking, also because of janky notation. For example, in Eq. (5) it seems like the linear transformation is applied to the concatenation of PLE features for all cells in the columns which seems to be absurd, because there should a variable number of cells for each table. All equations that present the architecture are similarly unclear.
- It's also unclear what is the difference between SCL and SSCL in Eq (11) and Eq (12). In what sense one uses labels and the other one doesn't?
- I am not an expert in the field, but a cursory look at arXiv pointed out a missing comparison system: https://arxiv.org/pdf/2403.01841, published at ICLR last year.

### Questions
- It's not clear whether any tuning has been performed on XGBoost or default hyperparameters have been used which can have a dramatic effect on performances: see Table 1 in https://arxiv.org/pdf/2403.01841. Can you clarify this issue?
- How does CTA work? Tables are (arguably) permutation invariant wrt rows, but removing positional embeddings altogether would make the two following tables have the same representations:

(1)
| a | b |
| - | - | 
| 0 | 0 |
| 1 | 1 |

(2)
| a | b |
| - | - | 
| 0 | 1 |
| 1 | 0 |

- Given that you use 0 to represent `false` would your approach be able to distinguish the two following tables?

(3)
| a | b |
| - | - | 
| 1 | 0 |
| 1 | 0 |

(4)
| a | c |
| - | - | 
| 1 | 0 |
| 1 | 0 |

- Is PLE invariant to scaling?
- Have the authors tried a simple LLM baseline? This would be more to contextualise the practical implications of the paper, rather than its scientific validity.

### Soundness
1

### Presentation
1

### Contribution
2
