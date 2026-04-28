# Out of Many, One: Designing and Scaffolding Proteins at the Scale of the Structural Universe with Genie 2

- Decision: Reject
- Avg Score: 5.00
- Scores: 5, 5, 5, 5

## Abstract
Protein diffusion models have emerged as a promising approach for protein design. One such pioneering model is Genie, a method that asymmetrically represents protein structures during the forward and backward processes, using simple Gaussian noising for the former and expressive SE(3)-equivariant attention for the latter. In this work we introduce Genie 2, extending Genie to capture a larger and more diverse protein structure space through architectural innovations and massive data augmentation. Genie 2 adds motif scaffolding capabilities via a novel multi-motif framework that designs co-occurring motifs with unspecified inter-motif positions and orientations. This makes possible complex protein designs that engage multiple interaction partners and perform multiple functions. On both unconditional and conditional generation, Genie 2 achieves state-of-the-art performance, outperforming all known methods on key design metrics including designability, diversity, and novelty. Genie 2 also solves more motif scaffolding problems than other methods and does so with more unique and varied solutions. Taken together, these advances set a new standard for structure-based protein design.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
The authors introduce Genie 2, an extension of Genie that incorporates architectural innovations and extensive data augmentation. Genie 2 supports both unconditional generation and multi-motif scaffolding. The authors claim that Genie 2 achieves state-of-the-art performance, outperforming all known methods on key design metrics.

### Strengths
1. For unconditional generation, Genie 2 performs better than Genie and other methods when generating short proteins.
2.  Genie 2 also supports multi-motif scaffolding.

### Weaknesses
1. The authors overstate the performance of Genie 2 in the Abstract. While they claim that Genie 2 achieves state-of-the-art performance and outperforms all known methods on key design metrics, Figure 3 Panel B shows that Genie 2 performs significantly worse than Proteus on long proteins.

2. The comparison benchmarking is insufficient.

    a. Unconditional generation: The comparison lacks the inclusion of recent methods such as MultiFlow [1], CarbonNovo [2], and FoldFlow2 [3], which have demonstrated significant performance improvements. 

    b. Single-Motif Scaffolding: Methods like Chroma and FoldFlow2 should be included for comparison. While Chroma is included in the benchmarking for unconditional generation, it is excluded in the scaffolding generation comparisons. Clarification on this omission is needed.
3. The methodological contributions appear incremental. The authors extend Genie's architecture and training procedure to enable motif scaffolding, with most modifications focusing on adapting input features. Additionally, Genie 2 incorporates triangular multiplicative updates, which have already been shown to be effective in previous works such as Proteus [4], CarbonNovo [2], and FoldFlow2 [3].
4. Insufficient Analysis of Multi-Motif Scaffolding: Despite claiming multi-motif scaffolding as a key contribution, the paper provides limited analysis in this area. Interesting analysis would be :

    a. In failed cases, is the failure due to incorrect single motif design or inaccuracies in the relative positioning of motifs?

    b. Does the success rate of scaffolding depend on the number of motifs being used?

 5.  The method requires significantly more inference steps than previous methods, indicating low sampling efficiency.

### Questions
1. Previous methods tend to generate more alpha-helices than beta-strands. In Genie 2, what is the distribution of generated proteins among the structural classes of all-alpha, all-beta, alpha+beta, and alpha/beta? Does the designability of the generated proteins depend on the ratio of alpha-helices?

2. Why was a batch size of 256 chosen for training Genie 2? Both Proteus and Chroma use batch sizes larger than 500, yet they exhibit significantly different performance levels. Therefore, without additional experimental results, it is unclear whether batch size is the main reason for Genie 2's significantly worse performance compared to Proteus on long proteins. 

2. Please address the concerns and questions raised in the Weaknesses section.

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
4

### Summary
The paper describes Genie 2, an extension of the protein structure diffusion model Genie for motif-conditioned generation. The method is extensively benchmarked against alternative methods for unconditional and motif-conditioned diffusion models, and seems perform comparatively well.

### Strengths
The authors detail an extension of the Genie model for motif-conditioned protein structure generation. The incorporation of motif information is clearly explained and quite simple, and importantly seems to work quite well empirically.

Comparisons to existing methods for unconditional and motif-conditioned generation are clearly presented and fairly thorough. There are many protein structure diffusion models and the authors have done a nice job presenting results for some of the most prominent.

### Weaknesses
The authors highlight functional protein design as a motivation for this work, and assert that functional protein design tasks can often be reduced to scaffolding of known motifs. While this may be true for simple enzymes, many functional proteins of therapeutic and industrial interest are considerably more complex (e.g., involving conformational changes or inter-domain coordination). Without experimental validation of the results presented here, it is difficult to know whether the proposed method would meaningfully improve functional design outcomes.

Given the relationship between this work and the original Genie paper, it is surprising to not see any direct comparisons between Genie 2 and the original model. For instance, how would the original Genie architecture trained on the PDB compare with the results presented in Table 1? It seems that the largest improvements came from expanding the training dataset to include AFDB, but it would be useful to see more detailed ablations of the architectural, data, and training objective changes, and the interplay between these (if there exists any).

The analysis of low-temperature sampling is quite hard to follow as currently presented. It is not clear that the authors have used low-temperature sampling for the results presented in Table 1 until the following section analyzing secondary structure distributions. Further, in this section (line 323), the authors cite a finding that low-temperature sampling yielded better results, but do not provide the results of this analysis.

The result about “designability” of AFDB structures is interesting, but not very convincing in its current form. Rather than summarizing the results of changing from scRMSD to scTM, the authors should present the full distribution of values for both of these metrics. The authors note that ProteinMPNN may be biased towards the PDB; this hypothesis could be tested by using ESM-IF1, which has been trained on AlphaFold2-predicted structures.

Much of the evaluation presented in this paper depends on ESMFold as an oracle for structure prediction. While this has become a standard practice, as noted by the authors, it would be useful for readers to include some discussion of the shortcomings and potential biases introduced by this approach.

### Questions
At a couple places in the paper (line 806, line 872), the authors note that certain (earlier) model checkpoints were selected for evaluation due to better performance. How were these checkpoints selected?

It seems that the Chroma conditioner framework should admit single- and multi-motif scaffolding as described in this paper. Was there a reason this model was not benchmarked in these scenarios?

How important is the sequence information for motif conditioning? In the absence of this information, would the model still produce viable solutions to the motif scaffolding problems?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper presents Genie 2, an improved protein diffusion model that extends the capabilities of its predecessor Genie. The key innovation is the addition of multi-motif scaffolding capabilities that allow designing proteins with multiple functional sites without specifying their relative positions and orientations. The model uses SE(3)-equivariant attention for the reverse diffusion process and introduces a novel motif representation approach. The authors demonstrate state-of-the-art performance in both unconditional and conditional protein generation tasks, particularly in terms of designability, diversity, and novelty.

### Strengths
1. Technical Innovation: The paper introduces a clever representation for multi-motif scaffolding that uses distance matrices to specify intra-motif but not inter-motif distances, allowing flexible placement of functional sites.
2. Comprehensive Evaluation: The authors provide thorough comparisons with existing methods like RFDiffusion, FrameFlow, and Chroma across multiple metrics on unconditional protein generation and single-motif scaffolding.
3. Data Innovation: The use of AlphaFold database for training data augmentation is a novel approach that expands the structural space beyond experimentally determined structures.

### Weaknesses
1. Training Constraints: The model is limited to training on sequences up to 256 residues in length, though it can generate longer sequences. The implications of this limitation are not fully explored, particularly how the fixed training length impacts the model's ability to capture long-range dependencies and complex structural motifs in longer proteins. It's unclear if the model extrapolates well beyond the training length or if there are performance degradations when generating significantly longer sequences. This limitation may also affect the model's ability to accurately design proteins with large domains or multi-domain architectures.

2. Multi-motif Benchmark: The benchmark set of only 6 multi-motif scaffolding problems is too small to draw statistically significant conclusions about the model's capabilities. A robust benchmark should include at least dozens of diverse cases, encompassing a variety of motif types, arrangements, and structural contexts, to properly evaluate performance. The current benchmark might not be representative of the broader challenges in multi-motif scaffolding and could lead to over-optimistic conclusions about the model's generalizability. The lack of diversity in the benchmark set makes it difficult to assess the model's robustness and its ability to handle different types of multi-motif design problems.

3. Multi-motif Baselines: Although previous works like RFDiffusion were not specifically designed for multi-motif scaffolding, they could still address such problems by randomly sampling relative positions and orientations between motifs. The authors should have included comparisons with these existing methods to demonstrate the advantages of their approach over such a baseline strategy. Without such comparisons, it's difficult to ascertain if the model's performance is truly superior to a simple random sampling approach, especially given the limited size of the multi-motif benchmark. The lack of a clear baseline comparison makes it hard to isolate the specific contributions of the proposed method.

### Questions
Similar to what was mentioned in the weaknesses section.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This work builds on Genie 1 by adding motif scaffolding, enabling the generation of protein scaffolds that support specified motifs - an important step toward the ultimate goal of designing functional proteins.

The authors developed a simple yet effective method to encode motif information as node and pair conditions, enabling the generation of protein structures that closely adhere to targeted motif cores. They also extend the single-motif problem to multi-motif generation, exploring whether the model can generate proteins with independent functions, pushing the boundaries of creating more complex and versatile protein machines. Additionally, they found that augmenting training with AFDB clusters and applying conditional training benefits both motif scaffolding and unconditional structure generation, with benchmarks against strong SOTA models, including RFDiffusion, FrameFlow, and Chroma.

In summary, this work provides an interesting perspective on protein motif design and demonstrates the improvements of Genie 2 in protein structure generation.

### Strengths
**[Clarity and Quality]**

- The manuscript is clearly structured and easy to follow, with a comprehensive background review covering sequence, structure, and co-design, as well as motif scaffolding. This allows readers to understand the main concepts without needing to refer to external sources.
- The authors conducted sufficient experiments to evaluate empirical performance of Genie 2 on both the unconditional generation and scaffolding, comparing it with strong SOTA baselines such as RFDiffusion and FrameFlow.

**[Originality and Significance]**

- The authors extend motif scaffolding to design multiple independent motifs, supported by a benchmark problem set, which could benefit protein generation in more complex protein machinery.
- By encoding motif conditions as node and pair embeddings, the authors provide an SE3-invariant and flexible approach for representing motif information.

### Weaknesses
 **[Quality and Clarity]**

- The current version lacks in-depth studies on key tuning parameters (e.g., sampling temperature) and critical design factors (e.g., conditional training). Specifically, the effect of varying the conditional training ratio is not thoroughly explored, and the conclusion that conditional training universally enhances performance is not sufficiently supported by the presented data. The manuscript would benefit from a more rigorous analysis of how this parameter affects model convergence and final performance.
- Some important baselines are missing. In particular, the Twisted Diffusion Sampler, which is mentioned in the related work, should be included as a baseline for a more comprehensive comparison. This is especially important given that it represents a different approach to motif scaffolding.
- Some analyses and statements need further evaluation. For example, the comparison of secondary structure distributions to AFDB is problematic, as not all baselines were trained on AFDB, and AFDB may not accurately reflect the structural distribution of real-world PDB data. Additionally, the claim that Chroma, Proteus, and RFDiffusion underrepresent beta strands and loop elements requires further clarification, as the presented data suggests otherwise.
- Certain statements are vague and would benefit from clarification. For instance, the claim that “low temperature sampling yields better results” needs to be quantified with specific metrics. It is unclear whether this refers to designability, diversity, or another measure, and how these metrics are affected by temperature changes.

**[Significance and Originality]**

While the independent multi-motif design presents an interesting task, the current work faces limitations that affect its impact:

- The primary improvement of Genie 2 over current SOTA appears to be in diversity (including diverse solutions in motif scaffolding). However, it remains unclear whether this improvement is due to training with AFDB or low-temperature sampling. A more detailed ablation study is needed to disentangle these effects and determine the specific contribution of each component.
- Training on AFDB is a logical approach that has already been applied in other protein design models (e.g., Bilingual Language Model for Protein Sequence and Structure, Michael Heinzinger et al., bioRxiv, https://doi.org/10.1101/2023.07.23.550085). The manuscript should acknowledge this and clearly articulate the novel aspects of their approach in leveraging AFDB.
- Encoding protein structure as SE3-invariant node and pair features is also an established approach (e.g., AlphaFold 2 encodes template information as node and pair). Although this work shows that SE3 invariance is effective for motifs encoding, it does not demonstrate broader impact on this design choice. The manuscript should clarify the specific advantages of their SE3-invariant encoding beyond what is already known.

### Questions
1. Table 3: The authors demonstrate the effect of conditional training ratio on small-scale, “unconverged” models. While this limitation is understandable due to time constraints, the conclusion that conditional training universally enhances performance remains speculative. More comprehensive results during the rebuttal period would strengthen the findings.
2. Low-temperature sampling (line 323): The authors state that “low temperature sampling yields better results.” Could they specify which metric(s) this “better” refers to, as it’s unclear from the context?
3. Temperature sensitivity: The authors used different temperatures (γ) for unconditional generation and motif-scaffolding, highlighting the importance of tuning this parameter. Could they include the default temperatures used for each model in the main text and clarify the impact of varying temperatures on each task? Does this adjustment impose trade-offs, and how sensitive is the model to this factor?
4. Training data balance: Is it reasonable to balance experimental structure data (PDB) and synthetic data (AFDB) for training? Are the results significantly biased towards synthetic data?
5. Secondary structure distribution (section 4.2): When evaluating secondary structure distribution, comparing to AFDB might be problematic as 1) not all baselines were trained on AFDB, and 2) AFDB may differ in structural distribution from real-world PDB data.
6. Secondary structure distribution (section 4.2): Contrary to the authors' suggestion in line 318, it seems Chroma, Proteus, and RFDiffusion appear to generate more beta strands (top left) than AFDB. Could the authors clarify their statement about underrepresented beta strands and loop elements?
7. Low-temperature sampling for AFDB (line 352): The lower designability in AFDB might explain low designability at normal temperatures for Genie 2, but it doesn’t directly explain why low-temperature sampling would mitigate this. Could the authors provide additional insights?
8. Baseline model: The authors mention the Twisted Diffusion Sampler in related work but do not include it as a baseline. Could they clarify this choice?
9. Baseline model Genie 1: Could the authors include baseline performance results for Genie 1 in unconditional generation?
10. Multi-motif scaffolding benchmark curation: This benchmark includes only proteins with <200 amino acids. Have the authors explored more complex cases with longer sequences, or are there specific challenges in curating such datasets?
11. Multi-chain generation: Although Genie 2 accepts “chain index” as an input feature, it does not support multi-chain generation with motif-scaffolding. What limits this implementation?
12. Clarifications on some claims:
    - The authors claim Genie 2 “better captures protein structure space” and covers a “larger and more diverse protein structure space.” However, this aspect has not been directly evaluated. Current results only show higher diversity, not necessarily “broader structure space coverage” compared to Genie 1, especially given the smaller sample size examined (1,035 structures, line 309).
    - In Equation (5), the authors claim that “motifs are enforced as a soft constraint, ensuring responsiveness to motif specifications while designing the protein as a whole.” However, the current loss does not distinguish explicitly between motifs and scaffolds (e.g., no separate regularization for motif losses). The authors might want to suggest the benefits of jointly learning the motif and scaffolds coordinates and further clarification could strengthen the interpretation.

### Soundness
3

### Presentation
3

### Contribution
2
