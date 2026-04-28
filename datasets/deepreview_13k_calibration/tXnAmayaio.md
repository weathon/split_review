# GenQA: An Instruction Dataset of LLM Generated Questions and Answers

- Decision: Reject
- Avg Score: 4.25
- Scores: 3, 5, 6, 3

## Abstract
Most public instruction finetuning datasets are relatively small compared to the closed source datasets used to train industry models. To study questions about finetuning at scale, such as curricula and learning rate cooldown schedules, there is a need for industrial-scale datasets. However, this scale necessitates a data generation process that is almost entirely automated. In this work, we study methods for generating large instruction datasets from a single prompt. With little human oversight, we get LLMs to write diverse sets of instruction examples ranging from simple completion tasks to complex multi-turn dialogs across a variety of subject areas. When finetuning a Llama-3 8B base model, our dataset meets or exceeds both WizardLM and Ultrachat on both knowledge-intensive leaderboard tasks as well as conversational evaluations. We release our dataset, the “generator” prompts that created it, and our finetuned model checkpoints.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a method for generating large-scale QA pairs for instruction tuning by prompting Gemini. The method instructs Gemini to list topics and sub-topics within a given domain and select one of them (randomly or according to a given index) and move forward to create a question-answer pair. This process introduces diversity in the QA pairs due to the randomness in listing and selecting topics (or sub-topics).

Fine-tuning a Llama-3 8B base model on large scale GenQA dataset with these QA pairs shows improved performance on knowledge-intensive tasks.

### Strengths
- the proposed method is highly scalable

- target domain of generated instructions can be controlled

### Weaknesses
 - Some aspects of the method remain unclear. In Section 3.2, five different prompts are introduced, but it is not specified which ones are actually used in the experiments. I assume a combination of “Generator-Conditional,” “Generator-Nested,” and “Generator-Uniform” is applied. How are their proportions determined across different domains?

- The generated QA pairs are produced at a large scale. However, the results in Tables 3 and 4 raise potential concerns regarding their quality.

- A total of 513,483 coding QA pairs are generated (see Table 1), yet no evaluations are conducted on the coding domain in the experiments.

- The proposed method can be considered a black-box distillation approach for Gemini. Therefore, the results for Gemini should be included in Table 3 and Table 4 as an upper bound reference.

- Although 2.4 million examples are generated based on topics from the MMLU benchmark, the MMLU results in Table 2 show a decrease compared to the Llama3 base.

- Why are the MATH and GSM scores for MathInstruct so low in Table 4? According to https://arxiv.org/pdf/2309.05653 based on Llama2 7B, MathInstruct achieves a score of 31.5 on MATH. I expect with llama3, the results should be higher.

**Missing citation:**  
Synthetic Data (Almost) from Scratch: Generalized Instruction Tuning for Language Models

### Questions
- How do you ensure that the generated questions in the QA pairs are reasonable and answerable? For instance, is there a possibility that some generated math questions may be unsolvable?

- If incorrect answers are generated, does your method filter out these examples?

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
3

### Summary
This paper describes GenQA, a large-scale instruction dataset generated from several prompts. Researchers face a challenge: existing publicly available fine-tuned datasets are small and cannot meet the demands of industrial-scale model training. To address this problem, the authors propose an automated data generation method that utilizes LLMs to generate diverse instruction examples from a single prompt. These examples cover many subjects, from simple complementary tasks to complex multi-round conversations.

### Strengths
1. Novelty: This paper presents a method for generating large-scale instruction datasets from single prompt, which is essential for research requiring large-scale datasets for model fine-tuning. The creation of GenQA datasets may profoundly impact the field of NLP, especially on fine-tuning LLMs. The authors detail the generator prompts strategy, a novel approach for improving the efficiency of extracting diverse questions from LLMs. This approach may also inspire the creation of other datasets.

2. Writing: This paper is well structured and logical, with clear diagrams and tables that help the reader to understand.

### Weaknesses
1. (Main) Experiments with different models and scales: LIMA [1] points out that a small amount of data can motivate the capabilities of the larger scale model (70B), and the authors could have conducted further comparisons at more model structures, such as Qwen2-7B. Or comparisons can be made at larger scales with small amounts of data regarding the quality of the generated data, which can strengthen the contribution of this paper.

2. Bias caused by prompt engineering: the Gemini 1.0 Pro LLM, used in the paper, may produce bias and cost constraints, and the situation in more varied LLMs, such as open source models and ChatGPT, remains unclear.

3. Cost issues are not mentioned or discussed. Specific cost analysis may need to be covered, such as balancing the consumption in the open-source model with the particular API cost and comparing the resource consumption with the existing programs.

### Questions
Refer to the above.

### Soundness
3

### Presentation
3

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
Summary: 

The paper GenQA introduces a method for generating large-scale instruction datasets using minimal human input. By employing generator prompts, the authors autonomously generate millions of instruction-response pairs across diverse subjects. This approach minimizes reliance on human curation and bridges the gap between the scale of academic and industry datasets, producing an industrial-scale dataset intended for finetuning large language models.

Contributions: 
1. Generator Prompting Techniques: The paper introduces innovative generator prompt strategies, such as generator-conditional and generator-nested prompts, which enhance data diversity by increasing randomness and avoiding repetition. These methods are shown to outperform traditional static prompts, yielding a high-coverage dataset across various question types and complexity levels.
2. Performance on Benchmark Tasks: Models finetuned on GenQA, including subsets for specific tasks, achieve competitive performance on instruction-following and knowledge-based benchmarks, such as AlpacaEval, MT-Bench, and reasoning tasks in math and general knowledge. This demonstrates that models trained on GenQA can generalize effectively to complex tasks and remain comparable to those trained on industry-standard datasets.
3. Public Release of Dataset and Methods: The authors release not only the full GenQA dataset but also the meta-prompts used to generate each data split, allowing for reproducibility and further exploration. This openness supports ongoing research on automated data generation techniques and the development of scalable datasets for finetuning large models.
4. Detailed Diversity Analysis: The paper includes an extensive quantitative evaluation of diversity across GenQA and other datasets like WizardLM and UltraChat. Using similarity scores to measure uniqueness, the authors demonstrate GenQA’s high diversity, which rivals or exceeds that of traditional, manually curated datasets.

### Strengths
Originality: The paper presents an innovative approach to instruction dataset creation, leveraging generator prompts, specifically the nested and conditional variants, to produce a vast dataset autonomously, without relying on extensive human oversight or labor. Additionally, by applying their methodology to generate over 10 million instructions across multiple domains, the paper highlights an impactful application of prompt engineering in scalable data generation.

Quality: The paper is grounded in rigorous empirical work, as demonstrated through its extensive evaluation of data diversity and benchmark performance. The authors also provide detailed ablations and diversity analyses that strengthen the argument for GenQA's efficacy. Furthermore, the paper thoroughly documents prompt configurations, token counts, and finetuning procedures, enhancing the reproducibility and robustness of the results.

Clarity: The paper is well-structured and clearly conveys its objectives, methodology, and findings. The description of generator prompt types is accessible and detailed, allowing readers to understand the differences in prompt configurations and their impact on data diversity. The inclusion of charts enhances readability, and the breakdown of the dataset into distinct splits provides a clear understanding of how GenQA was designed to cover a wide range of knowledge domains and instruction formats. 

Significance: GenQA addresses a significant challenge in LLM training: the high cost and labor-intensive process of creating large-scale instruction datasets. By demonstrating that autonomously generated datasets can rival or exceed the performance of traditional, manually curated datasets, GenQA has the potential to reshape data generation practices in research and industry. The ability to create high-quality datasets with minimal human intervention democratizes access to LLM finetuning resources, making industrial-scale finetuning feasible in academic and open-source settings. Additionally, the public release of GenQA and its generation techniques paves the way for further research on scalable dataset generation and prompt diversity in LLM training.

### Weaknesses
Dependency on Generator Model Quality and Accessibility:
The quality of GenQA is highly dependent on the capabilities of the generator model, which raises potential limitations in both reproducibility and generalizability. The reliance on a single model, specifically Gemini 1.0 Pro, introduces a significant dependency that could affect the consistency of results if other models with different architectures or training data are used. This dependence makes it difficult to ascertain whether the observed performance is due to the dataset itself or the specific characteristics of the generator model. Furthermore, the accessibility of the generator model could pose a challenge for researchers who do not have access to the same model or its API, limiting the reproducibility of the study.

Lack of Analysis on Why "Bigger" Improves Only Certain Task Performance:
While the paper observes that training on the entire GenQA dataset yields improvements on instruction-following evaluations and Leaderboard tasks, it does not explore why this increased performance is limited to these specific areas. Without an in-depth analysis, it remains unclear whether the performance boost is due to the dataset’s sheer size, the diversity of instructions, or other factors like the nature of the tasks in these benchmarks. The paper lacks a detailed investigation into the types of tasks where the larger dataset provides a significant advantage and those where it does not, which is crucial for understanding the dataset's utility and limitations.

Random Subset Selection Instead of Maintaining Split Ratios: The paper uses a random subset of GenQA to perform token-for-token comparisons with other datasets. However, this approach does not preserve the original ratios of different task types within GenQA, potentially leading to an unbalanced subset that does not fully represent the diversity of the full dataset. This could affect the validity of the comparison, as the subset may underperform or overperform on certain benchmarks depending on the distribution of task types. The random selection process could inadvertently skew the subset towards certain task types, making it an unreliable representation of the full dataset's characteristics.

### Questions
Suggestion about Generator Model: The authors could conduct additional tests using other available generator models, like GPT-3.5 or other open-source models, and report on the quality of data produced. This would also provide insights into the extent to which the method is generalizable across different base models, potentially increasing the impact of GenQA.

Why "Bigger" Improves Only Certain Task Performance: To provide clearer insights, the paper could benefit from an ablation study that varies dataset size and analyzes performance on different task categories, such as reasoning or domain-specific knowledge tasks. Additionally, examining the dataset’s effectiveness on a broader range of benchmarks or task-specific evaluations would clarify whether "bigger is better" applies universally or only to certain types of instruction-tuning tasks. This analysis would make the findings around dataset size more robust and actionable for future dataset design.

Suggestion about subset selection: To ensure a fairer and more representative comparison, the authors could create the GenQA subset by maintaining the same ratio of task types as in the full GenQA. This approach would better reflect the dataset’s diversity and allow for more accurate conclusions regarding the effect of dataset size on performance. This adjustment would make the subset more comparable to the full GenQA, strengthening the token-for-token analysis and ensuring it more accurately reflects the dataset’s overall characteristics.

### Soundness
4

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces a new finetuning dataset, GenQA, primarily created using Gemini Pro 1.0, and explores the use of dynamic "generator" prompts to encourage diverse output. The work demonstrates that finetuning on the GenQA dataset can provide better results compares to UltraChat and WizardLM in a selection of evaluation settings. The paper claims that the dataset, generator prompts and finetuned model are released.

### Strengths
The work produces a resource that will be valuable to the LLM community. I also particularly appreciate the token-for-token analysis which strengthens the paper's claims around the effectiveness of the approach.

### Weaknesses
Figure 1 plots MTBench score (0-10) on the same y-axis as win-rate -- I'd suggest having a separate axis that correctly represents the possible range of values. I'd also consider referring to the DeepMind Math dataset as "DeepMind Math" or "DM Math" instead of "DeepMind" (https://huggingface.co/datasets/deepmind/math_dataset).

The distinction between static and generator prompts describes two different ways of interacting with LLMs. For static prompts, the authors provide an example where the LLM is queried multiple times, independently, using the same prompt. The authors claim that the lack of output diversity resulting from this process is problematic -- but it is an expected effect of sampling multiple tiems from a distribution. For generator prompts, the authors ask the LLM to output a list of elements. This is a distinctly different mode of operation in which the output of the next list element is conditioned on all previous generations. This is standard practice for various components of synth data generation pipelines. I would suggest downweighting the claims made in this section and focusing the narrative on the more interesting parts of the paper e.g. the study of how generator prompt selection impacts various characteristics of the generated data.

The booster effects are interesting, but don't answer the immediate question which is "which booster should I use for best results?". Deeper analysis here would be insightful.

I don't understand why the Length values in Table 2 for the GenQA 135M token and 238M tokens are so different, under the assumption that they are sampled from the same distribution. The reported lengths suggest a significant difference in the underlying data composition, which warrants further investigation. If the data is indeed sampled from the same distribution, then the observed length discrepancy is unexpected and should be explained.

There are differences across how the datasets being compared were constructed, particularly in terms of which models were used to generate them. All experiments are also performed with a single finetuning recipe and set of hyperparameters, which may be amenable to a particular data source. I am NOT suggesting repeating the experiments with different model recipes/setups, or say replicating WizardLM with Gemini Pro 1.0 to directly compare the methodologies, however, there are various effects that can be tested for e.g. overlap between the eval sets and generated datasets, that could provide some valuable insight here.

Broken reference on line 238.

Missing background: this work presents a method for generating instrictions, primarily in question format (hence the name GenQA), using generative models. There is a substantial amount of question generation work prior to the nowadays more common reformulation of general instruction-following that uses generative models to generate questions/instructions. I feel that the introduction and background section of this paper could both be made a lot richer by incorporating this prior work (a short but not comprehensive list includes https://aclanthology.org/D17-1090/, https://arxiv.org/abs/1705.00106,https://arxiv.org/abs/1905.08949, https://arxiv.org/pdf/2104.08678, https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00415/107615/PAQ-65-Million-Probably-Asked-Questions-and-What). In particular, the related work section also seems to suggest that language models started to be finetuned with Flan, which is not accurate.

### Questions
Can you elaborate further on what the impact you expect this work to have? I can see the GenQA resource itself providing value to the community, but I am struggling to identify the scientific contributions. I'd like to see more analysis and discussion around the various deeper insights.

### Soundness
2

### Presentation
2

### Contribution
1
