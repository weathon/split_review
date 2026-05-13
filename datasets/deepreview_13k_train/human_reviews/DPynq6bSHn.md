# EMMA-500: Enhancing Massively Multilingual Adaptation of Large Language Models

- Decision: Reject
- Scores: 5, 3, 5

## Abstract
\noindent In this work, we introduce \textbf{EMMA-500}, a large-scale multilingual language model continue-trained on texts across 546 languages designed for enhanced multilingual performance, with a focus on improving language coverage for low-resource languages. 
To facilitate continual pre-training, we compile \textbf{the MaLA corpus}, a comprehensive multilingual dataset and enrich it with curated datasets across diverse domains. 
Leveraging this corpus, we conduct extensive continual pre-training of the Llama 2 7B model, resulting in EMMA-500, which demonstrates robust performance across a wide collection of benchmarks, including a comprehensive set of multilingual tasks and \textbf{PolyWrite}, an open-ended generation benchmark developed in this study. 
Our results highlight the effectiveness of continual pre-training in expanding large language models' language capacity, particularly for underrepresented languages, demonstrating significant gains in cross-lingual transfer, task generalization, and language adaptability.

\vspace{2ex}
\noindent \twemoji{robot} Model: \href{https://huggingface.co/collections/MaLA-LM/emma-500-66eaa9acf1f512c8915b7166}{huggingface.co/collections/MaLA-LM -> EMMA-500}\\
\noindent \twemoji{floppy disk} Data: \href{https://huggingface.co/collections/MaLA-LM/mala-corpus-66e05127641a51de34d39529}{huggingface.co/collections/MaLA-LM -> MaLA corpus}\\
\noindent \twemoji{writing hand} PolyWrite: \href{https://huggingface.co/datasets/MaLA-LM/PolyWrite}{huggingface

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
EMMA-500 outlines work around three technical contributions:
* EMMA-500 -> A multilingual model trained on 546 languages
* MaLA Corpus -> A multilingual corpus spanning 939 languages (A subset of which that had >100k tokens were used in the EMMA-500 training)
* PolyWrite -> Open Ended generation benchmark

### Strengths
* Always great to see work that tackles the challenges in the long tail of languages.
* In-depth information for several preprocessing steps. This is really useful and important to allow future work to build on. 
* Several evaluations performed on a plethora of datasets.

### Weaknesses
I would like to list the following weakness fully ensuring the authors that I am not unreasonable and am completely open to increasing my score if these are addressed/answered satisfactorily.

* The contributions section could be rewritten as bullet points and bold headings to emphasize the exact contributions. This was confusing for a first-time reader given that MaLA-500(I assume this is related to previous work) also exists.
* Evaluations lack benchmarking the recent Aya-23 model. They are even omitted when using the eval sets from the Aya paper. Surprisingly they are only benchmarked in the code evals without any further explanation. The exclusion of a direct comparison with Aya-23, a multilingual-first decoder model released in May, is particularly concerning given that Llama 3.1, which came out later, was included. The choice to only evaluate Aya-23 on code generation tasks, without any other evaluations, raises questions about the thoroughness of the benchmarking process. Furthermore, the limited language support of Llama 3.1 (English, German, French, Italian, Portuguese, Hindi, Spanish, Thai) makes its inclusion as a primary benchmark questionable when evaluating a multilingual model.
* The categorization of “high” vs “mid” vs “low” resources is created by measuring token count in this specific training dataset, however there already exists widely accepted standards/taxonomies(like https://microsoft.github.io/linguisticdiversity/ – Joshi et al). No reference or explanation is provided as to why the authors deviated from this standard. The lack of ISO codes in the provided taxonomy is acknowledged, but other works, such as Aya, have addressed this issue through manual resolution. The authors' decision to not use this taxonomy, despite its widespread acceptance, requires a more detailed justification, especially given the importance of standardized language resource categorization.
* For n-shot evals ( like 3-shot on FLORES), it would be useful to also see 0-shot evals to understand how big a role ICL plays in the performance gains.
* I would edit the tables to be easier to read( for ex: bold the important numbers; say lower/higher is better; add arrows)

### Questions
* Could you please explain why the Aya model was omitted from some evals despite being quite a popular model for multilingual benchmarking?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper presents a continually-pretrained multilingual LLM that covers 546 languages. The paper focuses on the data mix (MaLA corpus) and the evaluation. 
The model is based on Llama2-7B and compared to other Llama derivatives or multilingually pretrained models. It claims comparatively strong performance on commonsense reasoning, machine translation and open-ended generation. 
The data combines multiple existing sources and adds preprocessing steps.
The evaluation includes existing benchmarks and new intrinsic benchmarks and a new automated open-generation benchmark that is using BLEU as a metric for comparing generations.

### Strengths
- Solid effort in including/focusing the data mix on low-resource languages that were excluded in previous works. This is ambitious and showcases that more languages are possibly “in reach” for more language-inclusive language modeling.
- Good highlight on iso code normalization and writing system treatment, which is often underestimated/undervalued in multilingual modeling but essential.

### Weaknesses
1. No discussion of related work beyond listing models for comparison and data sources that are part of MaLA. It would be important to communicate how this work differs from past efforts beyond covering more languages in continual training. What are the main achievements that have been unlocked? Where is the scientific novelty?
2. Presentation: The result tables are overcrowded with text, and some of the results that are mentioned as main model strengths are hidden away in the appendix. It is hard for the reader to understand which numbers the claims of performance are grounded in. Furthermore, it is not clear what the main goal behind the model is: is it to be good at tail languages or beat other models in their supported languages or both?
3. Evaluation: 
    - Metric: Two of the three main evaluation results are based on BLEU, although it is known that BLEU is (1) not equally suitable for all 500+ languages (see e.g. https://arxiv.org/pdf/2205.03983, Section 4.2) (2) is purely surface-based, e.g. underestimates paraphrases, neglects semantics, etc. The evaluation with self-BLEU is questionable - what does high diversity mean in the absence of a metric of accuracy? It would be more appropriate to use metrics like ChrF++ which are more robust across languages and do not rely on tokenizers.
    - Human: There is no human evaluation of the final model, nor the data pipeline, hence it is not clear how good the generation is especially in the newly covered tail languages. 
      - The only benchmark that covers 500+ languages is intrinsic modeling on Glot500-c, which might be biased as the same corpus was used during pre-training, hence data quality issues won’t show in evaluation.
      - The new PolyWrite benchmark is machine-generated and machine-translated, and machine-filtered. How reliable is it? Is there Western-centric bias in the prompts, or are they equally representative for all languages covered?
    - Safety: No safety-related evaluation. It is known that data quality especially in low-resource languages is often lacking, caused by quality issues in the data pipeline, which in turn can introduce unwanted biases (https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00447/109285) 
    - Comparison with other models: It is not fair to compare models that do not officially support certain languages on these specific languages. This distorts averages across languages and makes it impossible to compare where wins are due to covering languages at all vs truly outperforming other models that also include these languages. I would recommend separating these: evaluating against other models on their languages and benchmarks, and then evaluating on the newly covered languages, with a focus on quality of generations (some basic checks can be run: is the generation in the correct language? Does it have expected length?). 

  I understand that this represents a “best effort with limited means” - building reliable evaluation for 500+ languages is a huge enterprise by itself. However, the paper should at least prominently discuss these shortcomings and be more explicit about evaluation gaps and how to interpret the presented results, and which purpose the model can serve for advancing NLP in these languages. To be concrete, let’s say I want to use the model for Nogai - what can I expect? 
Expanding the set of languages in training without having reliable evaluation metrics for each of them (or at least discussing or being transparent about their shortcomings and evaluation gaps) is not sufficient for responsibly claiming an advance in multilingual modeling. I do believe that the effort put into data preparation and training is worth publishing, but needs to be evaluated and presented in a much more rigorous manner.

### Questions
- What is the relation to the MaLA-500 model/work? What are key improvements over it?
- How was the data mix tuned? What was the process of setting the weights, based on intuition or prior experience or reports? Were any ablations run? This would be nice to describe in the Appendix (if no space in the main paper) to help others understand the deciding factors in setting up a successful data mix.
- Table 4: 
  - Why is tower-instruct performing so poorly (especially since it’s built for translation)?
  - How would the model perform with fewer or more shots? Is the number of shots optimized for EMMA-500?
- Since whitespace cleaning only applies to whitespace-tokenized languages, are the other languages cleaner per se or need cleaning in other ways? 
- How were existing datasets and their languages to be included chosen?
- Table 6: Are BLEU scores in this low range even reliable? Is the difference between 1- and 2-BLEU outputs significant? This should be supported by at least some evidence, e.g. significance tests or qualitative examples.
- How is self-BLEU evaluation influenced by sampling hyperparameters? Please report sampling parameters and discuss how they might affect the self-BLEU.

### Soundness
2

### Presentation
2

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
This paper proposes a multilingual dataset named "the MaLA corpus" by augmenting and merging existing datasets, a multilingual model by continue pre-training on the processed dataset using LLaMA-2-7b, and a open-ended multilingual benchmark generated by ChatGPT. The main contents of this paper are used to illustrate the common pipeline of processing data and report results on multilingual benchmark. The only finding in this paper is that the multilingual capacities of LLaMA-2-7b can be improved by continue pre-training on multilingual corpus, which is trivial.

### Strengths
- The MaLA corpus compiled and PolyWrite multilingual benchmark will be beneficial to multilingual NLP researchers if they are public.
- Extensive experiments are conducted to show the effectiveness of EMMA-500.

### Weaknesses
 - [Addressed] Limited novelty: the corpus are generated by merging and cleaning existing datasets. The method to create multilingual benchmark is not novel, which is commonly adopted in the multilingual NLP community. It is an incremental work on augmenting the multilingual corpus and benchmark.
- Lacking baseline: some models of continue pre-training on LLaMA-2-7b are missing like ALMA[1] and Bayling[2].

### Questions
1. Will this corpus, model weight, benchmark and processing scripts be public?
2. Line 121-122: "This issue is resolved ...", Which issue has been resolved?
3. Line 310-311: Why is the global batch size set to 16M, rather than the commonly used 4M tokens like LLaMA-2?

### Soundness
3

### Presentation
2

### Contribution
3
