## Human Reviewer 1

### Summary
The paper presents a Punjabi-focused NLP stack that includes PunGPT2, a 124M-parameter GPT-2–style model trained from scratch on a 35 GB Punjabi corpus, a retrieval-augmented framework (Pun-RAG), an instruction-tuned variant (Pun-Instruct), and a hybrid retriever (Quantum-RAG) that combines BM25, dense similarities, and a quantum-inspired kernel with learned phase terms. The authors report improvements over multilingual baselines on FLORES-200, IndicGenBench, and a new PunjabiEval benchmark, including higher ROUGE and cultural fidelity scores, as well as stronger retrieval metrics. They state all data, model weights, and pipelines will be released.

### Strengths
1. This paper curates a series of useful resources: a large corpus, a GPT-2 style model, and an instruction tuning recipe. Releasing these artifacts will contribute to the Punjabi NLP community and the democratization of NLP.
1. Quantum-RAG designs a new retrieval kernel that can be easily integrated and can bring measurable performance gains.

### Weaknesses
Despite its strengths, I do have concerns with this paper’s scope and framing. 

1. This paper is primarily a resource and system paper for one language, which aligns better with NLP venues that emphasize language resources and regional applications [1, 2]. By contrast, it seems that closely related ICLR work is method-centric and more general [3, 4].
1. The only clear technical contribution is the phase-augmented retrieval kernel. But to make this paper a methodology paper instead, the framing of the paper may need significant changes, promoting this as the main claim and validating it beyond Punjabi with stronger experiments.
1. The writing quality at the current form is below ICLR expectations. Related work omits relevant strands and needs careful rewriting. The figure is illegible at print scale, and a table does not align to the page width. The manuscript appears not to strictly follow the ICLR template.


[1] Samanantar: The Largest Publicly Available Parallel Corpora for Indic Languages. Ramesh et al., 2022. 

[2] BanglaBERT: Language Model Pretraining and Benchmarks for Low-Resource Language Understanding. Bhattacharjee et al., 2022.

[3] UniMax: Fairer and more Effective Language Sampling for Large-Scale Multilingual Pretraining. Chung et al., 2023. 

[4] Variational Information Bottleneck for Effective Low-Resource Fine-Tuning. Karimi Mahabadi et al., 2021

### Questions
Please refer to the weaknesses.

### Soundness
3

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4

---

## Human Reviewer 2

### Summary
# High-level summary

The authors focus on Punjabi-specific models, and contribute a) a GPT-2-based model trained on a curated dataset; b) a hybrid RAG method that combines embedding-based retrieval and sparse retrieval (BM25), and c) a semi-synthetic pipeline to post-train the models using a mixture of hand-crafted manual tasks and synthetic data. The authors then show some results across standard metrics and human evaluation on the improvements made by the proposed contributions.

The overall paper seems to be generic, with a lack of details in every single contribution. I'll stick to critiquing the hybrid RAG, which seems relevant. The authors' intentions and motivation to contribute to including more Punjabi resources seem commendable, but overall, the paper needs splitting, rewriting, and a solid structure (presentation and ethical) to ensure their contributions trickle well into future research looking at the Punjabi language.


## Quantum-RAG

The authors propose the similarity between two vectors as the linear sum of the BM25 score, the cosine similarity score, and the kernel distance between - unsure how the $\theta$ is calculated, and if cosine similarity is even needed in the final equation. Furthermore, unclear how this relates to the contribution to improving LLMs for Punjabi. The notation seems inconsistent, with a lot of details missing, and unclear how better RAG has any relation to training loss.

### Strengths
1. The authors seem to have put a lot of effort into trying to present good-quality human evals.

### Weaknesses
1. The presentation, writing, and overall motives remain unclear. The authors start with presenting a contribution for training a model on Punjabi data, then move on to Quantum-RAG and then show results where Quantum-RAG performs the best. I'm unsure if a) this is a good fit for ICLR and b) this paper should be split into multiple different parts, with each part suitable for a different audience. For example, a technical report on pre-training/post-training a GPT-2 model for Punjabi and the evals associated with it, and lessons learnt; 2) A good description of theoretical/practical motivations behind Quantum-RAG and a thorough eval of why the proposed method is applicable everywhere would be part 2.
2. Evals seem unstructured - 10 people evaluating 1000 seems really time intensive: without further details on how the participants were compensated, no IRB details and inter-annotater agreement, the evals do not look sound.
3. Poor figures: Fig.1 is hard to read and doesn't seem all too different from any standard pre-training pipeline. Fig. 2 and Fig. 3 seem irrelevant and don't add anything to the paper. Fig. 4 is hard to read, unclear what the authors intend to present with the caption seeming to indicate something else. The authors are encouraged to remove Fig. 2 and 3, improve Fig. 1, and Fig. 4 needs to have separate, clear bars indicating the metric, model with appropriate error bars. Similarly, Fig. 5 needs re-rendering with clear subtitles and comparing all baselines with one clear contribution.

### Questions
N/A

### Soundness
1

### Presentation
1

### Contribution
1

### Rating
0

### Confidence
5

---

## Human Reviewer 3

### Summary
The paper presents a Punjabi-focused suite that includes: a decoder-only language model PunGPT2 trained from scratch on about 35 GB of Punjabi text covering Gurmukhi and Shahmukhi; a retrieval-augmented generation pipeline (Pun-RAG) with a dense FAISS retriever; an instruction-tuned variant (Pun-Instruct) trained on roughly 75k instruction pairs; and a hybrid “Quantum-RAG” retriever that fuses BM25, cosine over dense embeddings, and a phase-based similarity function. The authors report strong retrieval and downstream gains on their PunjabiEval benchmark, human evaluation by native speakers, and intend to release data, code, and weights.

### Strengths
The paper addresses a meaningful gap in NLP by developing resources for the underserved Punjabi language, with a commitment to open releases of datasets, models, and code that will benefit the research community. The work presents a comprehensive end-to-end pipeline spanning pretraining, retrieval-augmented generation, and instruction tuning, accompanied by thorough training details and systematic ablation studies. A key technical contribution is the hybrid retrieval approach that combines multiple methods — BM25, dense FAISS, and a novel phase-based similarity measure — with empirical validation demonstrating its effectiveness. The evaluation is strengthened by native-speaker human assessment and practical consideration of both Punjabi scripts in the tokenizer design.

### Weaknesses
While the paper makes a timely and valuable push toward open Punjabi NLP with a coherent LM-RAG-instruction suite, several limitations remain that collectively weaken the empirical and methodological claims.

First, mBERT — an encoder-only representation model — is compared to decoder LMs using ROUGE-L, a summarization/generation metric, which is not the right lens to assess mBERT’s contribution.

Second, the retrieval methodology is under-specified and under-contextualized. The paper does not describe how the embedding ranker is obtained/trained, nor does it provide external retrieval models (e.g., mBERT/me5 bi-encoders). Beyond the in-system variants (BM25/FAISS/quantum/hybrid), it remains unclear how well the method fares against strong, widely used retrieval models across languages and domains.

Finally, the generation baselines are constrained. The study centers on fine-tuned mT5, lacks RAG-style generative methods as implemented in the Pun-RAG model, and evaluates large LMs only in zero-shot, without exploring established performance boosters such as few-shot prompting or proposed in other works methods for low-resource language adaptation.

The paper would benefit from a more granular analysis and validation of each stage in its multi-stage pipeline for low-resource language generation.

### Questions
1. The retrieval component references learned phases and fusion weights, but the training setup remains opaque. Could the authors elaborate on the objective, architecture, and whether the ranker is encoder or decoder architecture? A concise summary would make the results reproducible, per reviewer guidance.

2. Since mBERT is an encoder-only model, could the authors clarify the methodology for comparing the encoder-only mBERT model against decoder-only architectures using ROUGE-L, a generation metric?

3. The kernel is introduced only within Punjabi tasks. Are there plans to test on additional languages and task types to assess the breadth of applicability and potential limitations? Even a small-scale study would strengthen generalization claims.

### Soundness
2

### Presentation
3

### Contribution
2

### Rating
4

### Confidence
4

---

## Human Reviewer 4

### Summary
The work focuses on low-resource language modeling and retrieval in Punjabi language. The paper presents PunGPT2, a Punjabi GPT-2-style language model trained on a 35GB curated corpus; Pun-RAG, a retrieval-augmented version; Pun-Instruct, an instruction-tuned variant using QLoRA; and Quantum-RAG, a hybrid retriever that combines sparse, dense, and quantum-inspired kernel similarity. The authors also release a PunjabiEval benchmark. Experiments show notable improvements in perplexity, ROUGE-L, cultural fidelity, and Recall@10 over multilingual baselines. However, the paper is poorly written. Lots of experiment-related sections don't have corresponding results (e.g. Sec 9.2 and Sec 9.6). In general, I feel that reviewing this paper is a waste of my time.

### Strengths
- This work focuses on RAG in Punjabi language, which is a low-resource language.
- This work introduces a lot of recourses for a low-resource language, including a 35GB dataset, a GPT-2-based LLM, an instruction-tuned model for Punjabi language, and a benchmark for evaluation.

### Weaknesses
- Many figures and tables are flawed. For instance, table 1 and table 2 is too wide. Figure 1 is too small and I can't read it at all. Figure 3 is blurred.
- This work seems to be applying lots of existing methods on a low-resource language, which may not fit well for ICLR.
- The paper is poorly written.
- The evaluation is very weak, cannot find multiple experiment results, including downstream task evaluation and ablation study.

### Questions
- What is the ablation result in Section 9.6? There is no reference mentioned in the text.
- Why do you treat training loss as a language modeling metrics?
- Where is the result of Section 9.2?

### Soundness
1

### Presentation
1

### Contribution
2

### Rating
2

### Confidence
4