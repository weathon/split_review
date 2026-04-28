# DeepRTL: Bridging Verilog Understanding and Generation with a Unified Representation Model

- Decision: Accept
- Scores: 8, 6, 8, 8

## Abstract
Recent advancements in large language models (LLMs) have demonstrated significant potential in automating the generation of hardware description language (HDL) code from high-level natural language instructions. While fine-tuning has improved these models' performance in hardware design tasks, prior efforts have largely focused on Verilog code generation, overlooking the equally critical task of Verilog understanding. Furthermore, existing models suffer from weak alignment between natural language descriptions and Verilog code, which hampers the generation of high-quality, synthesizable designs. To overcome these limitations, we present DeepRTL, a unified representation model that excels in both Verilog understanding and generation. Based on CodeT5+, DeepRTL is fine-tuned on a comprehensive dataset that aligns Verilog code with rich, multi-level natural language descriptions. 
We also introduce the first benchmark for Verilog understanding and take the initiative to apply embedding similarity and GPT Score to evaluate the models' understanding capabilities. These metrics capture semantic similarity more accurately than traditional methods like BLEU and ROUGE, which are limited to surface-level n-gram overlaps. By adapting curriculum learning to train DeepRTL, we enable it to significantly outperform GPT-4 in Verilog understanding tasks, while achieving performance on par with OpenAI's o1-preview model in Verilog generation tasks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper proposes a dataset and a model for verilog generation and understanding. It carefully describes the annotation process for the dataset and presents an extensive battery of experimental results. Overall, the paper seems valuable to me, although I should clarify that I am well-versed in code generation, but not in Verilog so I may be missing some context with related work.

### Strengths
- As a whole, the work seems extensive and relatively careful, from conceptualization to base data collection, human annotation, model training, and evaluation.
- I am not an expert in EDA, but it seemed like the work was novel from the point of view of such a dataset and model not existing previously.
- The experimentation is extensive, comparing a fairly large number of models with various evaluation metrics.

### Weaknesses
- As someone who is not well-versed in Verilog, I would have appreciated an explanation of the basics of the language, what is its basic syntax, characteristics, etc. But there was not very much explanation in the paper.
- Conceptually, the work was rather straightforward and I did not get many clear research insights from the paper. For this paper I am not extremely concerned about this though, as the work seems valuable nonetheless, and could serve as a base for future research.
- It was not clear how much of the work will be released for the research community to build on. It seems that some of the data may be released, but presumably the proprietary data will not be? And also it wasn't clear about the model.

### Questions
None

### Soundness
4

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
This paper deals with the task of code understanding and generation in the context of generation of hardware description language (HDL) code. In particular, this work focuses on the generation of Verilog code.
The model is based on an existing CodeLLM (authors used CodeT5+), which was fine tuned with a new augmented dataset created for this purpose. The dataset comprises both open and proprietary verilog codes, which were augmented (commented and summarised) by GPT-4. 
Two models are trained using a  progressive training strategy based on CodeT5+ models. For the understanding benchmark, models are evaluated in terms of BLUE and ROUGE, as well as embedding similarity and GPT score. Results show an improved performance over competitors and baseline models. For the generation part, the models are evaluated on a Verilog generation benchmark introduced by Chang et al. 2024, and compared with GPT series models showing competitive performance against the best, o1-preview and surpassing GPT3.5 and GPT4.

### Strengths
Original approach, focusing on both generation and understanding tasks on a low resource code language as Verilog, specifically designed for hardware description.
The approach seems reasonable. The field of application is needed and follows the ultimate goal of improving electronic design automation.

### Weaknesses
The work lacks clarity. Particularly, the dataset collection and the training regime are not completely clear and their figures do not clarify the issue (see below).
Experiments seem reasonable but all baselines and competitors weren’t trained specifically on verilog. Since the current work cites other previous approaches, experiments could have compared to them as well (or explain why was not possible)

### Questions
* Verilog is not a particularly known language. Authors could have explained a bit more its nature, syntax and usage.

* Figure 1, although it helps to understand the flow of data collection, it’s not particularly clear. The fact that the flow goes to the top-left in opposition to the common flow for reading (top to bottom and left to right) makes it unclear. Also, which part is used for training? Only after distil?

* Line 388-392: these lines and Figure 3 describe the progressive training. This explanation is not clear. Are the authors just feeding the model with more to less granular annotations? That could be an example of Curriculum learning. Please clarify and add references if needed.

* why the authors didn’t compared the performance of the new models with Zhang et al., 2024, , Chang et al. 2024b, Liu et al. (2023b); Thakur et al. (2024),

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
4

### Summary
The paper makes a contribution to the field of hardware design automation by addressing both the generation and understanding of Verilog code using large language models (LLMs). While previous studies primarily focused on the generation aspect, this work recognizes the importance of understanding Verilog code and proposes a unified representation model, DeepRTL, built on an enhanced CodeT5+ architecture. This model is trained on a specifically curated dataset that tightly aligns natural language descriptions with Verilog code, aiming to improve the semantic alignment between the two. Additionally, the paper introduces the first benchmark specifically for Verilog understanding and develops two novel metrics, embedding similarity and GPT score, to capture semantic similarities more effectively than traditional n-gram-based metrics like BLEU and ROUGE. In comparative assessments, DeepRTL surpasses GPT-4 in Verilog understanding tasks and matches the performance of OpenAI’s o1-preview model in code generation tasks.

### Strengths
1. The paper introduces a novel task for evaluating LLMs in hardware design, focusing on Verilog understanding—prior work mainly focuses on generation. It introduces new training datasets, evaluation benchmarks, and establishes baselines for this new task.

2. DeepRTL, the model proposed in this paper, uniquely good at both the generation and understanding of Verilog, making it different from other models in the hardware design domain.

3. The methodology for creating a natural language-code parallel corpus via prompt engineering with GPT-4 is innovative and shows promise for broader application in fields where parallel corpora are lacking.

4. The diagrams in this paper describes the proposed methods clearly and intuitively.

### Weaknesses
1. The reason for selecting T5-like models as the base for DeepRTL is not empirically validated. It remains unclear whether the observed performance gains in Verilog understanding are due to T5's encoder-decoder architecture or the synthesized dataset used for fine-tuning. Comparative analysis with a decoder-only model, such as LLaMa-3-1B or DeepSeekCoder-1.3B, using the same dataset for finetuning would provide clearer insights.

2. The paper does not evaluate the impact of varying context window lengths, which is important given that CodeT5+ supports a limited token count (2,048 tokens), while actual Verilog code often exceeds this length. Dropping examples longer than 2,048 tokens will also bias the results in favor of DeepRTL, which is based on CodeT5+. A model accommodating longer context windows could potentially offer superior performance on the general task, but not for this tailored dataset.

3. The evaluation metrics for code understanding—embedding similarity and GPT score—are solely based on GPT models, leading to potential bias, as evidenced by the inflated scores of GPT-3.5, GPT-4, and o1-preview models shown in Table 2. This overlap may make the comparisons bias in favor of GPT-family models.

4. The evaluation of code generation lacks a comprehensive set of baselines. Despite mentioning various Verilog generation models in the related work section, these models are absent from the comparative analysis in Table 3.

5. The fine-tuning dataset includes proprietary code that cannot be released publicly, and the benchmarks used are also developed by the authors. The absence of shared code, data, or models in the publication hinders reproducibility and make it impossible to assess potential data contamination and bias in evaluation.

### Questions
N/A

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper introduces a novel dataset and model training for Verilog understanding and generation, as well as a new high-quality benchmark for the understanding task.

The authors provide a large Verilog dataset based on a large quantity of crawled open source code that is processed into code and natural language descriptions via GPT4, as well as a smaller amount of hand-curated code-description items from proprietary sources.\
They also introduce a new benchmark for Verilog understanding, consisting of 100 manually verified, high-quality code-description pairs.

For experiments, the authors train CodeT5+ -based models of sizes 220M and 16B on their newly introduced dataset, using "progressive training" and evaluate model performance in terms of Verilog understanding and generation capabilities.\
Experiments show that models trained in this manner outperform strong baselines on various metrics.

### Strengths
A novel dataset and benchmark for highly specialised programming code (Verilog); this might be interesting as it provides a new and interesting resource for a programming language that does not have as much attention as others such as Python, Jave, or C++.

### Weaknesses
Beyond the curation of an interesting new dataset, there is very limited novelty to this work; it seems like authors might be somewhat unfamiliar with the current state of the field of LLMs/Machine Learning, including ML for code:
- Fine-tuning a CodeT5 model on domain-specific code has been done.
- The "progressive training" is just curriculum learning, which is well-established in the field.
- Similarity scores based on vector similarity are as old as Word2Vec, if not older.
- Similarities/evaluations with LMs or LLMs (here "GPT Score") are well-established, e.g., see "LLM as a judge", BERT Score, etc.

This seems like it would be a very nice paper for a specialised Verilog/hardware spec conference, but may be of limited value for a venue like ICLR.

### Questions
- Why throw away dataset items that are longer than 2,048 tokens? It is true that this is the maximum input length for CodeT5+; however, why make a choice about the dataset based on the (essentially arbitrary) choice of model used in the specific experiments here?\
Modern LLMs, including open source ones such as Llama, have context sizes way beyond 2,048 tokens.

**Comment after Rebuttal**
I have adjusted my score to "marginally below acceptance threshold", rather than an outright "reject" based very good rebuttals.\
A agree with the authors on certain parts of my original criticism; however, the current manuscript requires some significant amount of re-work to be "acceptable", especially wrt. the original claims and presented support for decisions such as base model choice, and length restrictions of the dataset.

**Comment after further Rebuttal**
The authors have done an exceptional job at responding to reviewers' concerns, and addressed them in an updated manuscript. After the changes, I believe this paper is in a state that is acceptable; I have updated my scores accordingly.

### Soundness
3

### Presentation
3

### Contribution
3
