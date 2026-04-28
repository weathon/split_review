# SciLitLLM: How to Adapt LLMs for Scientific Literature Understanding

- Decision: Accept
- Scores: 6, 5, 6, 8

## Abstract
Scientific literature understanding is crucial for extracting targeted information and garnering insights, thereby significantly advancing scientific discovery.
Despite the remarkable success of Large Language Models (LLMs), they face challenges in scientific literature understanding, primarily due to (1) a lack of scientific knowledge and (2) unfamiliarity with specialized scientific tasks.
To develop an LLM specialized in scientific literature understanding, we propose a hybrid strategy that integrates continual pre-training (CPT) and supervised fine-tuning (SFT), to simultaneously infuse scientific domain knowledge and enhance instruction-following capabilities for domain-specific tasks.
In this process, we identify two key challenges: (1) constructing high-quality CPT corpora, and (2) generating diverse SFT instructions. 
We address these challenges through a meticulous pipeline, including PDF text extraction, parsing content error correction, quality filtering, and synthetic instruction creation.
Applying this strategy, we present a suite of LLMs: \textbf{\model}, specialized in scientific literature understanding.
These models demonstrate promising performance on scientific literature understanding benchmarks.
Our contributions are threefold: 
(1) We present an effective framework that integrates CPT and SFT to adapt LLMs to scientific literature understanding, which can also be easily adapted to other domains.
(2) We propose an LLM-based synthesis method to generate diverse and high-quality scientific instructions, resulting in a new instruction set -- \textbf{\data} -- for less-represented scientific domains. 
(3) \model~achieves promising performance in scientific literature understanding benchmarks.co/Uni-SMART/SciLitLLM-1.5}} and the synthetic dataset\footnote{\url{https://huggingface.co/datasets/Uni-SMART/SciLitIns}}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a method to improve scientific instruction following through post-training Qwen models. The main contribution is to collect science textbook data and improved SFT data mix. Their evaluation on a recent SciRiff dataset shows improvement.

### Strengths
- The paper introduces a strong pipeline in collecting textbook data and SFT data. This is aligned with most recent LM papers, showcasing the importance of data in the success of LM training. 
- Improved result in science instruction following

### Weaknesses
The authors don't seem to be planning to release their textbook dataset. This raises the question of data contamination in evaluating the proposed model.

### Questions
Are you planning to release the textbook datasets? 
Can you elaborate on the pipeline on what type of textbooks impact and improve task performance in SciRiff? 
Can you provide contamination studies in textbook datasets and the test/eval cases?

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
4

### Summary
This paper proposes a synthetic data generation pipeline for training
LMs for scientific literature understanding tasks. The main
contributions include:

1.  a pipeline for curating continued pre-training corpus based on
    textbooks and research papers (including document parsing,
    formatting, and filtering),

2.  another pipeline for creating instruction fine-tuning data for
    scientific literature understanding tasks via prompting GPT-4o.

3.  the authors show that finetuning Qwen-2.5 model (7B and 14B) on the
    CPT and SFT data can improve the performance on scientific
    literature understanding tasks.

### Strengths
1.  Overall the paper is nicely written and the pipeline is nicely
    presented.

2.  The curated dataset and models could be helpful.

### Weaknesses
1.  The primary contribution of the paper seems to be focused on the
    dataset construction; overall the method resembles similar works for
    synthetic data generation and there are some limitations:

    1.  The PDF processing pipeline can be improved. Scientific PDF are
        known to contain complex layout and structures, and previous
        work have identified that using simple PDF parsers can lead to
        suboptimal training results (S2ORC, Lo and Wang, and ). However,
        the author primarily uses a simple PyPDF parser (\"Converting
        these documents using tools like PyPDF2 often introduces
        formatting and syntax errors, which degrade the quality of the
        corpus (line 246)\"). I'd suggest the authors investigate the
        text quality issues and check other libraries like papermage, Lo
        et al.

2.  The results are not very strong. I'd imagine a domain-specifically
    distilled model can have a substance gain in performance compared to
    GPT-4o, especially the instruction fine-tuning dataset is generated
    via GPT-4o (line 331); however, as shown in table 3, the trained
    models (SciLitLLM-7B and SciLitLLM-14B) are on par with GPT-4o. Also
    the experimental design and presentation could be improved (see my
    suggestions in questions).

### Questions
1.  Are there special reasons why we should group the results based on
    the 10B model size? (table 2/3). I think it's more reasonable to
    organize based on pre-trained only/with instruction tuning/with
    domain specific tuning?

2.  Also in this paper there is only fine-tuning results on the Qwen
    model family but not others. It would be interesting to compare the
    fine-tuning effects on llama or other model families.

    1.  the author compared the performance with the SciTulu model,
        which is trained based on Llama-2 families. I don't think it's a
        fair comparison in table 3.

### Soundness
2

### Presentation
2

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
The paper proposes a new strategy to improve LLM for scientific literature understanding, which includes continual pretraining and supervised fine-tuning. The paper uses Llama3-8B to correct parsing errors and filters the dataset with Llama3-70B. The paper continues pretraining the Qwen2.5.The paper designs a three-step pipeline to generate diverse scientific contexts and corresponding QA pairs. The paper then incorporates heuristic deduplication and LLM-based filtering for the instructions. The proposed framework seems to improve the performance compared to SciRIFF. The paper also includes an ablation study.

### Strengths
1. The paper proposes a new framework that includes continual pretraining and supervised fine-tuning. The proposed framework and dataset can be very useful for other LLMs specialized in scientific understanding. The released dataset seems to be very comprehensive compared to the existing dataset.
2. The paper shows that with the new framework, the paper can further improve the performance of general LLM. The framework is especially useful in small models. Additionally, the paper includes an ablation study for CPT, SFT, and instruction quality filters. 
3. The paper provides the code and its model. In the appendix, the paper shows the improvement of format & grammar correction, CPT quality filter, SFT details, benchmark details, and detailed performance on SciAssess.

### Weaknesses
1. The creation of the CPT and SFT datasets seems to rely on LLMs. The paper can randomly sample a small subset of the created dataset to check its quality with humans to show the effectiveness of the proposed framework.
2. The experiment and ablation study is not comprehensive. The paper fails to show that the model is fine-tuned to other existing scientific understanding datasets, such as the Dolma dataset (https://allenai.github.io/dolma/). The paper did include SciTulu-7B dataset; however, scitulu is based on LLama2-tb. The paper should also show the model's performance only finetuned with SciLitIns. The analysis in the experiment is also rather simple. The paper needs to provide some explanation instead of just repeating the results in the table.
3. Some details are not very clear. What is the score used in Tables 2 and 3? Many additional evaluation results and analysis are put in the Appendix. Authors should move some of them to the main paper.

### Questions
What is the difference between the new CPT dataset and the Dolma Dataset (https://allenai.github.io/dolma/)?

### Soundness
3

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
3

### Summary
The paper introduces SciLitLLM, a specialized language model for scientific literature understanding, built using a hybrid approach combining continual pre-training (CPT) and supervised fine-tuning (SFT). The key contributions include 1) A pipeline that combines CPT with high-quality scientific corpora and SFT with diverse scientific instructions, 2) Novel methods for improving scientific text quality and generating domain-specific instructions, and 3)  Empirical results showing improved performance on scientific understanding benchmarks SciRIFF and SciAssess

### Strengths
### Well-Motivated Approach
- The hybrid CPT+SFT strategy effectively addresses both domain knowledge and task-specific capabilities.
- The pipeline is well-designed with clear motivation for each component.
- The approach is generalizable to other specialized domains

### Technical Contributions
>Pipeline includes innovative components like LLM-based format correction (Section 3.1.1) and quality filtering (Section 3.1.2)
The instruction synthesis method (Section 3.2.1) is clever and tackles the challenge of limited scientific instruction data.

### Solid empirical results
- SciLitLLM-7B outperforms similar-sized models by significant margins \~4% on SciAssess, +\~10% on SciRIFF.
- SciLitLLM-14B surpasses larger proprietary instruction tuned models (70B+ parameters).

### Weaknesses
### Weaknesses
The CPT corpus (12.7B tokens) is relatively small compared to standard pre-training datasets The paper acknowledges this limitation but could discuss potential impacts more thoroughly. For example, how this affect the representation from different scientific subject domains.

Otherwise I don't see clear weakness of paper of such kind. The paper appears comprehensive and well-executed for the research scope.

### Questions
1. How sensitive is the model performance to the quality filtering threshold (currently set at 25%)? Was this choice empirically validated?

2. The instruction synthesis method uses GPT-4 - have you explored using smaller models or your own models in a bootstrapping approach?

### Soundness
3

### Presentation
3

### Contribution
3
