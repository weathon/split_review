# MambaPEFT: Exploring Parameter-Efficient Fine-Tuning for Mamba

- Decision: Accept
- Scores: 5, 8, 6, 5

## Abstract
An ecosystem of Transformer-based models has been established by building large models with extensive data. 
Parameter-efficient fine-tuning (PEFT) is a crucial technology for deploying these models to downstream tasks with minimal cost while achieving effective performance. Recently, Mamba, a State Space Model (SSM)-based model, has attracted attention as a potential alternative to Transformers. While many large-scale Mamba-based models have been proposed, efficiently adapting pre-trained Mamba-based models to downstream tasks remains unexplored.
In this paper, we conduct an exploratory analysis of PEFT methods for Mamba. We investigate the effectiveness of existing PEFT methods for Transformers when applied to Mamba. We also modify these methods to better align with the Mamba architecture. Additionally, we propose new Mamba-specific PEFT methods that leverage the distinctive structure of Mamba. Our experiments indicate that PEFT performs more effectively for Mamba than Transformers. Lastly, we demonstrate how to effectively combine multiple PEFT methods and provide a framework that outperforms previous works. To ensure reproducibility, we will release the code after publication.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a comprehensive and detailed exploration of parameter-efficient fine-tuning (PEFT) for Mamba. By applying and refining existing PEFT methods, introducing novel PEFT approaches（Partial-tuning and Additional-scan）, and exploring optimal algorithmic combinations, it achieves outstanding performance in both image and language tasks. This work provides valuable insights for efficient fine-tuning in Mamba.

### Strengths
1. The paper not only improves existing PEFT algorithms to suit Mamba but also proposes targeted, innovative algorithms, providing the community with a broader selection of PEFT methods.
2. The experiments comprehensively showcase the performance of each PEFT algorithm, offering a framework for optimal algorithmic combinations.
3. The extensive experimental workload demonstrates thorough exploration of the algorithms.

### Weaknesses
1. The improved and original PEFT algorithms did not achieve the best results. In the VTAB-1k benchmark, the performance of the improved Partial LoRA is nearly identical to that of LoRA, while Additional-scan underperforms ParallelAdapter with comparable training parameters. Compared to traditional PEFT algorithms, these methods lack strong competitive advantage.
2. Although LoRA demonstrates outstanding performance on the VTAB-1k benchmark, its comparison with the modified Partial LoRA on language tasks is missing, making it unclear whether Partial LoRA is indeed the optimal PEFT method.
3. The algorithmic novelty is limited, as the concept of Partial-tuning appears relatively straightforward.

### Questions
Please further explain the advantage and effectiveness of the proposed method compared with the baselines.
Please further explain the novelty of the proposed method.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper explores the application of parameter-efficient fine-tuning (PEFT) in the Mamba model. It begins by systematically analyzing the suitability of existing PEFT methods for the Mamba model, then adapts certain PEFT methods to better align with the characteristics of State Space Models (SSMs), and finally investigates hybrid PEFT search strategies. Extensive experiments were conducted across image and text modalities, providing thorough benchmarks for various PEFT methods and demonstrating that the Mamba model exhibits distinct fine-tuning behavior compared to Transformer models.

### Strengths
1. The paper focuses on a novel and competitive model architecture, SSMs, systematically analyzing the applicability of existing PEFT methods for the Mamba model, offering insights for designing efficient fine-tuning schemes for SSMs.
2. The paper adapts existing PEFT methods specifically for SSMs, proposing new approaches tailored for Mamba, achieving good performances.
3. The extensive experiments, covering both image and text modalities, provide comprehensive benchmarks for all methods and reveal differences in PEFT performance between the Mamba and Transformer models.

### Weaknesses
1. The paper covers too many aspects, including various PEFT methods, individual analyses, and hybrid architecture search. The authors should concentrate on one aspect and provide valuable conclusions for each part instead of describing each in detail, as this could reduce readability and divert focus.
2. The paper should consider including the most advanced works within each PEFT category, such as GPS and SPT for partial-tuning methods, and SSF in addition to LoRA-based methods for reparameterization approaches.
3. Experiments should involve larger-scale models, where PEFT methods are particularly valuable. Evaluation across different model scales is crucial for PEFT methods. Notably, "scale" here refers to model parameter size rather than training data size (e.g., a model trained on ImageNet-21K in Section 4.5 is not necessarily larger than one trained on ImageNet-1K; model parameter size is more relevant in this context).
3. Presentation quality requires improvement, including spelling errors (e.g., "Linear Probing" instead of "Linear Proving" in Table 1’s ViT-S section) and inconsistent heights in sub-tables within Table 2.

### Questions
1. Table 1 shows that Adapter-based and LoRA-based methods perform best. Did the authors try SequentialAdapter, or, as in the original LoRA paper, apply LoRA across multiple locations simultaneously in the model?
2. In Table 1, the Hybrid approach shows no significant advantage over individual PEFT methods (e.g., ParallelAdapter or LoRA) despite having far more parameters (117,236). The performance of Hybrid is not markedly better than LoRA(in_proj), which has only 1,483 learnable parameters.
3. Beyond parameter efficiency, computational efficiency is also crucial for PEFT methods. Did the authors consider comparing the computational efficiency of different methods (e.g., in terms of FLOPs or running time)?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper explores parameter-efficient tuning methods such as the prominent methods like Adapter, LoRA, Prompt-tuning, and Partial tuning for the Mamba architecture. The authors highlight that these methods have not been studied in Mambas compared to the extensive research conducted on Transformers. The primary focus of this paper is on the Vision Mamba (Vim) architecture, with a minor portion addressing language models with Mamba compared with the Transformer counterparts Pythia. The study compares Vim and Vision Transformer models using PEFT methods, which address some key architectural and methodological choices like layer selection for LoRA and prompt placement in Prompt-tuning, for example. The authors present a two-step PEFT search method that hybridizes various PEFT options to offer a near-optimal solution (in terms of performance). Finally, the authors present a new PEFT method called Additional-scan, which increases the state dimension of the SSM, and an additional initialization method for the state matrix A is also presented. The experimental results employing Vim-S pre-trained on ImageNet-1K to demonstrate the effectiveness of the diverse PEFT options; Mamba-language models compared with Pythias are also presented.

### Strengths
- The paper is well-written and easy to follow.
- Searching for diverse PEFT options for Mamba is informative and would be a valuable contribution for those who employ Mamba architectures. 
- Studying extensive PEFT options based on a baseline yields convincing results.

### Weaknesses
#### #  Main concerns
- The authors' claim in line 22 that PEFT is more effective for Mamba than for Transformers lacks adequate rationale and supporting evidence. There is no clear intuition as to why Mamba would benefit more from PEFT; the experiments appear biased due to an unfair comparison - specifically, Transformers were tested with only a limited range of PEFT options, while Mamba underwent more comprehensive testing (as illustrated in Table 1). The addition of SPT and Adapter+ for ViT does not fully address this concern, as the core issue is the lack of granular exploration of PEFT application within the Transformer architecture itself, such as applying PEFT methods to individual layers (e.g., attention, feedforward networks) rather than treating the entire model as a single unit. This discrepancy in experimental design makes it difficult to draw a fair conclusion about the relative effectiveness of PEFT for Mamba versus Transformers.
- The authors primarily tested Vision Mamba rather than the broader Mamba architecture, yet they frequently used "Mamba" as an abbreviation for Vision Mamba. This reviewer is concerned this may be misleading, especially as the result table for the language models offers only limited experiments. The authors should clarify their terminology to ensure readers understand that Vision Mamba is the specific variant.
- The authors presented a hybrid PEFT approach as an optimal-like solution, which is identified through their proposed search method. However, its conclusion does not specify a practical, generalizable option. This reviewer feels It's important to note that the effectiveness of the identified hybrid approach may not be universal, and the search process itself would be resource-intensive for a new architecture.

#### # Missing/wrong details in preliminary
- Section 2.1, titled *Mamba*, should provide foundational knowledge about Mamba as a preliminary, but it mainly presents on S4 or early SSMs. Since Mamba has slightly distinct notations and a signature architecture, the authors should revise this section to include more comprehensive details about Mamba.
- As the experiments involve the Vision Mamba architecture, the reviewer suggests including the original architecture, which has subtle design differences (e.g., the definition of B).
- The discretization presented in Eq.(2) is not the zero-order hold discretization as implied but rather the bilinear one. The authors should correct this detail.

####  # Some concerns about experiments
- The experiments used a limited set of baseline models. Although the PEFT options explored were diverse and met the experimental standards of a scientific study, only the Vim-S baseline is used (since the PEFT methods are more likely to be applied to larger architectures, Vim-S may not be a proper choice as a baseline), where this reviewer feels the main comparison focuses on Vision Mambas versus Vision Transformers. The inclusion of Vim-B and Vmamba variants is a positive step, but the core concern about the baseline model size remains, as PEFT methods are often more relevant for larger models.
- Vision Transformers are not thoroughly explored compared to the fully examined Mamba models. For instance, ViT-S in Table 1 has only a few options compared to Mamba's more comprehensive use of PEFTs. The addition of SPT and Adapter+ is insufficient; a more granular exploration of PEFT application within the Transformer architecture, similar to that done for Mamba, is needed for a fair comparison.
- Some experimental comparisons lacked control:
  - In language models, for instance, Pythia 1.4B and the counterpart Mamba 1.4B had significantly different baseline performances (44.8 vs. 53.0), skewing the reported improvements, as higher starting accuracy inflates gains. The updated results for full fine-tuning do not address this fundamental issue of unequal baselines, which makes it difficult to compare the effectiveness of PEFT methods across different architectures.

#### # Minors
- There is a related work that covers a similar topic, including PEFTs in Mamba, which suggests that this paper is not the first to study PEFT for the Mamba architecture as mentioned in lines 71-74. This reviewer understands that the authors could not include the related work due to its publication date being after this submission. However, it is suggested to compare this study with that work in future revisions to provide context and emphasize differences.
  - Parameter-Efficient Fine-Tuning of State Space Models, NeurIPS 2024 workshop (https://arxiv.org/abs/2410.09016)

- Typo in Table 1: Linear 'Proving'

### Questions
- Could the authors provide additional results using Vim-Base or larger-scale architectures?
- How was the data utilized in the hybrid search method? Was a held-out set created for the searches?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper explores the PEFT methods for the Mamba. By modifying and adapting commonly used PEFT methods on Transformer, the paper proposes novel PEFT techniques tailored to the Mamba architecture. Experiments demonstrate that Mamba outperforms Transformer when applying PEFT methods. The paper also showcases how to effectively combine multiple PEFT methods to improve performance and introduces a new framework.

### Strengths
1 The authors extend PEFT methods from Transformer to the Mamba architecture and propose several Mamba-specific PEFT methods.

2 The authors conduct experiments not only in the vision domain but also in the language domain.

### Weaknesses
1 Why wasn’t Vim-B selected for comparison experiments with ViT-B? The authors seem to have not provided an explanation in the paper.

2 In Table 1, the PEFT methods selected by the authors are relatively outdated, such as FACT, which originates from AAAI23.

3 Conducting PEFT experiments on Vmamba, another Mamba-based vision model, is necessary to demonstrate the generality of the proposed methods.

4 In section 3.4, the mixed PEFT search strategy proposed by the authors lacks sufficient theoretical support, especially regarding the principles behind why different combinations of PEFT methods can improve performance, which the authors have not sufficiently explained.

5 For the vision experiments, the authors only consider smaller models without discussing the applicability of these methods to larger-scale models.

6 For the new architecture—Mamba—the training duration of these PEFT methods is worth considering and comparing.

### Questions
see Weaknesses.

### Soundness
2

### Presentation
3

### Contribution
2
