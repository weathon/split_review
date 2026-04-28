# MatText: Do Language Models Need More than Text & Scale for Materials Modeling?

- Decision: Reject
- Avg Score: 4.00
- Scores: 3, 5, 5, 3

## Abstract
Effectively representing materials as text has the potential to leverage the vast advancements of large language models (LLMs) for discovering new materials. While LLMs have shown remarkable success in various domains, their application to materials science remains underexplored. A fundamental challenge is the lack of understanding of how to best utilize text-based representations for materials modeling. This challenge is further compounded by the absence of a comprehensive benchmark to rigorously evaluate the capabilities and limitations of these textual representations in capturing the complexity of material systems. To address this gap, we propose \mattext, a suite of benchmarking tools and datasets designed to systematically evaluate the performance of language models in modeling materials.
\mattext encompasses nine distinct text-based representations for material systems, including several novel representations. Each representation incorporates unique inductive biases that capture relevant information and integrate prior physical knowledge about materials. Additionally, \mattext provides essential tools for training and benchmarking the performance of language models in the context of materials science. These tools include standardized dataset splits for each representation across a range of dataset sizes, probes for evaluating sensitivity to geometric factors, and tools for seamlessly converting crystal structures into text.
Using \mattext, we conduct an extensive analysis of the capabilities of language models in modeling materials with different representations and dataset scales. Our findings reveal that current language models consistently struggle to capture the geometric information crucial for materials modeling across all representations. Instead, these models tend to leverage local information, which is emphasized in some of our novel representations. Our analysis underscores \mattext's ability to reveal shortcomings of text-based methods for materials design.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
In this paper the authors propose a benchmarking suite for evaluating LLMs in modeling materials, which includes evaluations as well as tools for converting materials to LLM-appropriate representations and calculating materials-specific metrics, such as sensitivity to crystal structure. The benchmark includes 9 distinct representations for encoding materials (some of which are newly proposed in the paper), with the shared task across representations of predicting material properties (e.g. shear modulus, bulk modulus, formation energy) given the input material representation. They use the benchmark to evaluate BERT pretraining and Llama (parameter efficient) finetuning (Llama-3-8B-Instruct, Llama-2-13b-chat-hf) on this task, comparing to the current state-of-the-art model according to the MatBench benchmark (variants of graph NNs). In their experiments they find that scaling pretraining (in a small BERT model) does not seem to improve performance on the benchmark, that locality (encoded into one of the input representations) is a useful inductive bias, and that current models do not seem to use geometric information.

### Strengths
- **Important and interesting area of research.** Leveraging LLMs for reasoning in the space of material composition, structure, and properties is an exciting and potentially impactful area of research, and developing benchmarks and software libraries towards this end should encourage further developments in this space. The authors are spot on in terms of the key challenge in this space, which is how to effectively represent rich metadata about materials composition and structure.
- **Clearly written and easy to understand.** The paper was generally well written and easy to follow.

### Weaknesses
 - **Lack of engagement with prior work exploring methods for encoding structured/non-text information in language models (discussion or implementation).** The focus of the work / main findings are that LLMs are not very good at encoding/reasoning over numerical/structured values such as those important in representing and reasoning over the relationship between material composition and properties. But as far as I can tell, the paper only experiments with the most naive possible input and output representations (input: encoded representation of material composition/structure; output: numerical value of property). In this scenario, it is expected that the model will not do well in leveraging encoded structure because it is essentially forced to learn from scratch, because the representation of structure being used during finetuning/testing is likely too distinct from the representation of any similar knowledge during training, where the model was largely exposed to natural language text and code. It is known that LLMs, particularly the instruction-fine tuned models used in the paper, can struggle when provided with this type of non-natural-language formatted data, due to the mismatch between distributions observed during training, finetuning and evaluation. See e.g. [Fatemi et al. (2023)](https://arxiv.org/pdf/2310.04560), [Hegselmann et al. 2023](https://proceedings.mlr.press/v206/hegselmann23a.html), [Li et al. 2024](https://arxiv.org/abs/2403.07969), [Yin et al. 2023](https://arxiv.org/pdf/2306.01150), and other referenced work. While it would be interesting to validate this in this domain, insights from the current experimentation are limited because the experiments do not represent a realistic, good-faith setup for probing the models’ capabilities towards this end. Example methodologies that might do better would be tool use (to outsource quantitative reasoning), encoding the material structure information into code-type snippets, or even just encoding the input-output pairs as natural language questions (the Robocrys encoding gets close to this by at least encoding materials as natural language descriptions.) A single specific approach to this, RASP (Weiss et al. 2021), is discussed in the conclusions section, but not experimented with.
- **Limited contributions over prior work.** Relationship with MatBench should be clearly characterized very early in the paper, due to the similarity. MatBench is designed to benchmark any type of model on the same task, and the main contributions of this work over MatBench are: additional input representations (since this is the main challenge in using LLMs for this type of modeling) and software to help with evaluation and converting between representation formats. Because of the limited empirical results (as discussed above), this paper mostly provides a new benchmark, which is mostly composed of existing data/representations, but not many insights based on the benchmark, or other findings demonstrating its usefulness.
- **Limited analysis of results.** The appendix contains the beginning of some interesting analyses of the results. In particular, I would recommend moving discussion of the experimentation with tokenization to the main paper in future drafts, and elaborating. I’m very surprised that changes to the tokenization did not meaningfully improve performance. It would be interesting to see some examples of the tokenized inputs, under the default and modified settings. The encoded representations are so different than the text the default tokenizers were trained on, I would expect this to have a significant impact, and I wonder if just implementing Born & Manica (2023) was insufficient.
- **Discussion of limitations could be improved.** This work has many limitations not included. Breadth of models compared was limited. For example, benefits of scaling are only discussed in the context of “grokking” but it’s not clear why scaling more would not help further, since it was shown to lead to improvements in the existing results. The BERT models are incredibly small (4 layers and 8 attention heads), etc.

### Questions
- If you experimented with different prompt formats and strategies for decoder-only LLMs, could you report what you tried and whether it had any impact on results?
- If not, why did you use instruction fine-tuned models, but did not fine-tune on or experiment with instruction-style input-output pairs?
- Why not experiment with larger models (potentially proprietary/closed)?
- Why did you choose the specific size of the BERT model?

Additional notes:
- Would be helpful to add some additional highlighting in Table 2 — e.g. which representation (or MatBench model) performs best for each task? Very hard to parse visually. Also, both RMSE and ROC are reported, would be nice if it was indicated for which rows higher is better and lower is better.
- Fix references to be parenthetical (e.g. \citep rather than \citet) on line 84, also various similar mistakes in the appendix.
- Typo on line 332
- It would be helpful if you added some concrete examples of input-output pairs to the main paper, perhaps including examples that do and do not encode locality, since a distinction there was one of your key findings. Including versions tokenized using the given tokenizers would be informative as well.
- Relevant concurrent work: https://arxiv.org/abs/2409.14572

### Soundness
2

### Presentation
3

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
This paper introduces a benchmark for evaluating language models at predicting various properties of a material given its composition and structural information. To test the ability of LMs at utilizing different types of information (e.g., composition vs geometry), the benchmark provides several text representations of a material. Further, standardized data splits at different data scales are provided to test scaling behaviors.

Results suggest that LLMs, both existing ones and those pretrained on materials data from scratch, struggle at utilizing geometric information when making predictions. Further scaling the pretraining data seems to provide limited benefits.

### Strengths
- Standardizing materials modeling with a benchmark providing precomputed representations and data splits is very useful. This data could  be used in a lot of follow up research.
- Evaluations point out an interesting limitation of LLMs at utilizing geometric information effectively.

### Weaknesses
 - One of the main claims of the paper is that scaling pretraining alone may not be sufficient for improving materials modeling performance. However, this is based only on increasing data size (which still shows improvement on 2 out of the 3 tasks). However, existing studies of scaling laws all note that all three -- model size, training compute and pretraining data size -- must be scaled in tandem for optimal performance. Hence, it is not clear if the observations on scaling would still hold if we increase model size and train for longer.

- The contributions of the paper are a bit thin -- the data itself is sourced from existing resources (NOMAD and MatBench). The main contribution are the different text representations evaluated on MatBench tasks. None of these lead to an improvement over existing methods.

- Only a small set of materials modeling tasks were evaluated -- so while the benchmark is somewhat comprehensive in the representations it uses, it is not comprehensive in the modeling abilities it tests.

### Questions
- Why "datasets with 2D structures were excluded" from MatBench?

### Soundness
3

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
5

### Summary
The paper studies the potential of using LLMs for materials science, specifically in materials modeling. The authors introduce MatText, a benchmarking suite with nine text-based representations tailored for material systems, incorporating unique inductive biases to capture physical properties. The different analysis using MatText reveals that current LLMs struggle to effectively leverage geometric information, which is crucial in materials science, and instead rely heavily on local information. This suggests that text-based LLM approaches, unlike in natural language tasks, may not be inherently suitable for capturing the complexities of material properties.

### Strengths
-  MatText includes different text-based representations and standardized datasets for evaluating LLMs on materials science tasks.
- The study identifies critical challenges, such as the inability of LLMs to leverage geometric information
- Provides tools for converting crystal structures into text and standardizing materials datasets.

### Weaknesses
 - While the authors observe that LLMs focus on local information rather than spatial relationships (which have been noticed already in similar studies), they don’t provide a mechanism or architectural change to address this.

- The authors introduce nine different text-based representations of materials, each with unique inductive biases. However, text representations may be an inherently limited approach for encoding complex 3D geometric and physical properties. Certain representations (e.g., CIF) may add complexity without necessarily improving model performance, as the LLMs struggle with numerical encoding of positional data. In my opinion evaluating LLM on handling such representations is not fair. 

- The experiments is conducted with different tokenizers for handling numerical information. However, standard tokenization methods for numbers can inpuct the model’s ability to process continuous data, such as atomic positions or lattice parameters. This point needs further clarification.

### Questions
Does the Local-Env representation, by focusing primarily on local information, risk overlooking other crucial features such as long-range interactions or periodicity? If so, how can we address this limitation?

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
2

### Summary
This paper proposes a benchmark and toolkit for evaluating language models for modeling materials. By evaluating current LLMs on different text representations of materials from data sizes and inductive biases, the authors find problems in modeling materials with LLMs.

### Strengths
- Several experiments from different aspects are provided such as different text representations, different data sizes, and LLaMa and BERT.
- Many recent methods are surveyed and summarized, and tasks, datasets, and toolkits are provided.

### Weaknesses
 - The comparison and results are meaningful for materials LLM community, but the technical novelty is weak.
- The details of tasks and results are not well explained, and only numerical scores are shown, so it is difficult for readers unfamiliar with the material's domain to follow the paper.
- The claims on the limitations of LLMs are too strong considering the grokking or emergent abilities of LLMs.
  - Wei et al., Emergent Abilities of Large Language Models, TMLR, 2022

### Questions
See the weaknesses above.

### Soundness
3

### Presentation
2

### Contribution
2
