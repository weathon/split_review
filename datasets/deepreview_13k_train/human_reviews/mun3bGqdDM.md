# Atomas: Hierarchical Adaptive Alignment on Molecule-Text for Unified Molecule Understanding and Generation

- Decision: Accept
- Scores: 6, 6, 6

## Abstract
Molecule-and-text cross-modal representation learning has emerged as a promising direction for enhancing the quality of molecular representation, thereby improving performance in various scientific fields, including drug discovery and materials science. Existing studies adopt a global alignment approach to learn the knowledge from different modalities. These global alignment approaches fail to capture fine-grained information, such as molecular fragments and their corresponding textual description, which is crucial for downstream tasks. Furthermore, it is incapable to model such information using a similar global alignment strategy due to data scarcity of paired local part annotated data from existing datasets.
In this paper, we propose Atomas, a multi-modal molecular representation learning framework to jointly learn representations from SMILES string and text. We design a Hierarchical Adaptive Alignment model to concurrently learn the fine-grained fragment correspondence between two modalities and align these representations of fragments in three levels.
Additionally, Atomas's end-to-end training framework incorporates the tasks of understanding and generating molecule, thereby supporting a wider range of downstream tasks. In the retrieval task, Atomas exhibits robust generalization ability and outperforms the baseline by 30.8\% of recall@1 on average. In the generation task, Atomas achieves state-of-the-art results in both molecule captioning task and molecule generation task. Moreover, the visualization of the Hierarchical Adaptive Alignment model further confirms the chemical significance of our approach. Our codes can be found at \url{https://anonymous.4open.science/r/Atomas-03C3}.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper notices that existing works about molecule-and-text representation learning are mainly coarse-grained and uses a global alignment method to integrate molecules and texts. To solve this problem, this paper proposes a fine-grained method for cross-modal representation learning. Specifically, this paper proposes a hierarchical adaptive alignment module, which consists of two components, adaptive polymerization module and weighted alignment module. Experiments on different cross-modal tasks verify the effectiveness of the proposed model. Ablation analysis is also conducted to show the effect of each modeling component.

### Strengths
1. Overall, the problem of existing works is clearly motivated in the Introduction section with a figure as visual illustration. The overall writing in the paper is also clear enough, and an algorithm is also provided to formally present the learning process.

2. Specifically, the design of hierarchical adaptive alignment module is interesting and novel. This paper clearly shows its effect with empirical evaluation.

3. Experiments are comprehensive enough with different tasks and metrics. Ablation analysis is also conducted. Visualization also helps understand what the model learns.

### Weaknesses
1. Usually when we do experiments, we encourage authors to repeat the same experimental setting multiple times and report both mean and standard deviation, or report significance t-test. However, some tables and figures in the Experiment section don't have standard deviation or significance t-test, such as Tables 1 and 8, Figure 4. Authors are suggested provide standard deviation in the paper.

2. Scalability is an experiment in the paper to show the proposed is possible to scale on large datasets. For scalability, authors are also suggested to provide computational comeplexity to theoretically show that the proposed model is computationally efficient than baseline models.

### Questions
N.A.

### Soundness
3

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
5

### Summary
This paper proposed a unified framework to realize the alignment between text and SMILES at three levels without fine-grained manually annotated labels, namely the atom level, fragment level, and molecule level. The combined optimization of fine-grained contrastive learning and autoregressive learning promotes the model's performance on various downstream tasks, such as text-based de novo molecule generation, molecule captioning, molecule property prediction and molecule-text retrieval.

### Strengths
1.The writing is clear, the diagrams are rich, the experimental results are comprehensive, and it is easy to understand.
2. This paper realizes the fine-grained alignment of SMILES and text from the atom level, fragment level and molecule level, which is very comprehensive. The visualized results demonstrate the effectiveness of fine-grained alignment.
3. The ablation experiments demonstrate a mutual enhancement effect: contrastive learning alignment improves autoregressive learning, while autoregressive learning enhances contrastive learning alignment, showing the benefit of joint optimization.
4. Atomas, relying only on SMILES, achieves superior performance than models that rely on both SMILES and graph on some tasks.

### Weaknesses
1.Previous papers have proved the effectiveness of combined optimization of contrastive learning alignment and autoregressive learning.
Ref.”Align before fuse: Vision and language representation learning with momentum distillation”
2. The practice of using all tokens to calculate similarity to achieve more fine-grained alignment without additional labels is also not new. And the direct application of the weighted alignment modules limits the innovation.
Ref.”FILIP: Fine-grained Interactive Language-Image Pre-Training”、 “Disentangled Representation Learning for Text-Video Retrieval”.
3. While the method of constructing hierarchical features in this paper is effective, it lacks a more explicit rationale explaining the underlying principles that make this construction feasible.

### Questions
1. It seems that the purpose of the Molecule Level Alignment in Hierarchical Adaptive Alignment, and the Global Alignment is the same. Can you explain more about why Global Alignment is still needed in the architecture?
2. In the Assignment Step, have you tried using other clustering algorithms? How will it affect the results?

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
5

### Summary
This paper presents a hierarchical molecular representation learning framework, namely Atomas, which jointly learns representations from SMILES strings and texts. In Atomas, a Hierarchical Adaptive Alignment model is designed to learn the fine-grained fragment correspondence between molecule SMILES strings and text descriptions at three semantic levels, namely atom, fragment, and molecule level. Atomas outperform the baseline models on 12 molecule-related tasks.

### Strengths
1. The idea of aligning molecules and texts in a fine-grained aspect is novel and provides insight into the methodology for adopting LLMs for molecule discovery.
2. The module, Hierarchical Adaptive Alignment, is novel and introduces a new modality alignment method.
3. The performance of Atomas is competitive and proves its generalization in different molecule-related tasks.

### Weaknesses
1. The description of the framework is inappropriate. The authors claim they align SMILES and textual descriptions in three semantic levels, but the atom level actually uses tokens, which can not be identical to `atoms` as symbols and numbers might exist in the SMILES strings.
2. In Table 3, the performance of MolCA is not correct. The metrics should be BLEU-2 63.9, BLEU-4 55.5, ROUGE-1 69.7, ROUGE-2 55.8, ROUGE-L 63.6, and METEOR 66.9 with Galac1.3B [1]. This raises a challenge to the authors' claim that these molecule-and-text alignment methods struggle to effectively capture fine-grained correspondence related to local parts within different modalities.
3. I am a little confused about the three-level alignment. It seems that the alignment still happens at Stage 3, which calculates the similarity between the textual description and the molecule representation. Although the token and token cluster information might be extracted to enhance the molecule representations, I do not see how atom or fragment information is aligned with their descriptions in a fine-grained manner.
4. The selected baseline models are probably weak. More advanced models like BioT5 [2] [3] and ICMA [4] should be included.

### Questions
1. Could the authors compare more advanced baselines?
2. Could the authors explain my concerns in Weakness 3?
3. Is it possible to scale this methodology further or apply Atomas to decoder-only models? Currently, it might be unfair to compare Atomas with the previous baselines like MolCA because the backbone LLM can also lead to a difference in performance.

### Soundness
3

### Presentation
3

### Contribution
3
