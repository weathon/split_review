# gRNAde: Geometric Deep Learning for 3D RNA inverse design

- Decision: Accept
- Avg Score: 7.50
- Scores: 8, 8, 8, 6

## Abstract
Computational RNA design tasks are often posed as inverse problems, where sequences are designed based on adopting a single desired secondary structure without considering 3D geometry and conformational diversity. 
We introduce \textbf{gRNAde}, a \textbf{g}eometric \textbf{RNA} \textbf{de}sign pipeline operating on 3D RNA backbones to design sequences that explicitly account for structure and dynamics. 
gRNAde uses a multi-state Graph Neural Network and autoregressive decoding to generates candidate RNA sequences conditioned on one or more 3D backbone structures where the identities of the bases are unknown. 
On a single-state fixed backbone re-design benchmark of 14 RNA structures from the PDB identified by \citet{das2010atomic}, gRNAde obtains higher native sequence recovery rates (56\% on average) compared to Rosetta (45\% on average), taking under a second to produce designs compared to the reported hours for Rosetta. 
We further demonstrate the utility of gRNAde on a new benchmark of multi-state design for structurally flexible RNAs, as well as zero-shot ranking of mutational fitness landscapes in a retrospective analysis of a recent ribozyme

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The manuscript presents gRNAde, an approach for RNA inverse design conditioned on the 3D structure of RNA (conformational ensemble). The method uses geometric deep learning using a graph neural network which receives a set of backbone graphs derived from the 3D structure and predicts a set of RNA sequences (2D sequences of nucleotides (G,A,C,U).  

The approach is similar to ProteinMPNN (Daupara 2022) that solved a similar inverse problem for proteins. 

The two key related works are Rosetta (Leman 2020) and RDesign (Tan et al. 2023), a comparison to the latter is presented in pages 16-17. In particular, RDesign is another deep learning based method for inverse RNA design. Among various issues that the authors highlight in the appendix, it appears that the proposed method is open source, outperforms this baseline, and can offer sampling, which is attractive for producing multiple solutions.

### Strengths
The methodology is evaluated using both in silico and wet lab approaches. For in silico evaluation, three metrics (sequence recovery, self consistency, and perplexity) are reported. These metrics are described on page 16. The “wet lab” experiments are run on Eterna, an independent online computational RNA design platform, and showed an impressive performance improvement over Rosetta in the OpenKnot score.

The authors also create their own dataset using RNASolo (Adamczyk 2022). The authors should clarify this as an additional contribution if it is, or otherwise explain what are the modifications introduced to RNASolo. Will this new dataset also be released?

The paper is well written, polished and includes beautiful diagrams. The code is released open source (and added to the submission).

### Weaknesses
The authors should present a comprehensive technical comparison to other methods (e.g., Rosetta) not just RDesign (Tan et al. 2023) to enable better understanding of the proposed functionality. Specifically, please briefly summarize the technical components of Rosetta, and explain how gRNAde graph deep learning framework is different. 

The authors should focus their discussion on the technical similarities and differences to previous work, without negativity (“This means that any design produced by RDesign is deterministic and not diverse, making it useless in practical scenarios. All recovery metric results reported in the RDesign paper are also incorrect due to this issue (at least based on how recovery is computed in protein design).“ (Page 16). There is no wet lab comparison to RDesign, and the authors should explain why this is not possible (e.g., using the re-engineered checkpoint that was used to compute some performance comparisons using recovery reported in Table 2 and Figure 2a).



### Questions
- Please explain what happens to the other non-successful examples from Eterna which are not successful. What is the intuition of why the proposed method (as well as Rosetta) does not work? Is this due to challenging structural motifs, sequence patterns, or other type of structural features? Are there inputs that gRNAde will be more suited for in comparison to other methods, and vice versa?  

- Would the method generalize to unseen datasets/sources? 

- In Figure 17, various properties of RNA sequences are presented for the dataset used (sequence length, number of structures/sequences, average pairwise RMSD per sequence, bivariate distribution for sequence length vs. avg. RMSD). Do these properties affect performance results when the model is evaluated?

- Are there any biases of the model, e.g., to certain pairs of nucleotides, e.g., CG pairs, see (Frnakenstein, Lyngsoe 2012)?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
2

### Summary
This paper develops an inverse folding model for RNA (structure -> sequence), analogous to proteinMPNN for protein sequences. Unlike prior work, it is able to consume multiple conformations as input. The model performs well compared to popular baselines such as Rosetta on a wide variety of evaluation tasks.

### Strengths
The paper is well written, well motivated, and the results are convincing. As a reviewer, I found the "COMPARISON TO CONTEMPORANEOUS WORK" section in the appendix highly useful. Thank you for including this. The paper has a remarkable number of results. The analysis in the appendix about model ablations would typically appear in the main paper, but there simply wasn't space.

### Weaknesses
I don't have enough background on RNA to understand some details of the evaluation, but I am familiar with analogous evaluations for proteins and am under the impression that the evaluation is quite comprehensive. It would be great if other reviewers with more RNA background could assess these details.

### Questions
I don't know much about the landscape of tools for this sort of design. My impression is that current versions of Rosetta do not support RNA design. Why is that? Is it because it was found that Rosetta did not perform well for it or simply that there wasn't support to maintain these capabilities in the software? Is it a strong enough baseline to be compare against?

It would be good to discuss the methodological similarities/differences vs. RDesign in the main paper too. Given the details in the appendix, I know this is a complex topic. Can you provide a short piece of text that you'd include in a new version of the main paper describing the overlap?

### Soundness
4

### Presentation
4

### Contribution
4

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper presents gRNAde, a geometric deep learning-based approach for RNA inverse design task focused on creating RNA sequences conditioned on provided 3D conformations. gRNAde supports single- and multi-state RNA designs. The method has been compared against physics based tools such as Rosetta software with gRNAde showing better performance in multiple applications with faster processing times. The paper also shows gRNAde's potential for zero-shot learning in RNA fitness landscapes.

### Strengths
1. The paper studies an important problem of RNA inverse design inspired by similar works in protein space. Given that RNA 3D experimental data is much more limited and the structure of RNA being much more flexible than proteins, innovative approaches for this problem are desirable. The method although builds on existing architectures, employs sensible design suitable for RNA modeling (e.g.- using a three-bead (pseudotorsional) representation of the RNA backbone, minimizing the high-dimensional torsional space). 
2. gRNAde introduces an innovative multi-state GNN that models conformational ensembles—distinct structural states of RNA—by encoding them as a geometric multi-graph. The model's ability to simultaneously consider multiple conformations (or states) enhances its accuracy in predicting sequences that can adopt different functional forms.
3. Benchmarking against Rosetta and other tools shows higher higher sequence recovery rate and speedup for gRNAde showcasing its usability for for high-throughput scenarios.
4. The paper is well-written and easy to follow.

### Weaknesses
Although the paper explores an interesting problem and presents a sensible approach, there are some aspects which can be improved.


1. I did not find any discussion on if the model explicitly incorporates any biological nuances such as RNA modifications, cellular localization, or folding kinetics, which are essential for in vivo RNA functionality. Given that experimental training data is limited for RNA, such information may enhance performance especially that Physics based models often use such information as well. Some discussion around this can be helpful.

2. The evaluation focuses primarily on sequence recovery and perplexity. However, there are other aspects such as structural stability, functional motifs, etc. that affect RNA design which if not accounted for may produce RNA designs that are theoretically correct but biologically unviable. Did the authors perform any analysis of these aspects in their designed RNAs?

3. There are various ways to extract or represent the RNA backbone in molecular modeling and structural biology without clear consensus (see Richardson et al., 2008, RNA backbone: Consensus all-angle conformers and modular string nomenclature). Did the authors experiment with other backbone representations to see the impact of the particular choice of backbone representations?

4. From evaluation perspective, I have several suggestions which may help understanding the performance of gRNAde:
 (a) I did not see any analysis on failure cases, thus limiting the understanding of scenarios where gRNAde may perform poorly, hindering its reliability and robustness.
(b) Additionally, an evaluation of how varying RNA sequence lengths affect the performance may lead to better understanding of the pros and cons of gRNAde.
(c) Finally, pseudoknots are important in RNA secondary structure, which can lead to incomplete or inaccurate folding predictions, as pseudoknots play a critical role in the functional conformation of RNA molecules. The RNAInvBench paper (Cole et al., 2024) includes the pseudoknot-free and pseudoknot-inclusive benchmarks for RNA inverse design. It will be good to also compare against this benchmark.

### Questions
I have already left suggestions for further experiments that may help address some of the concerns in the weaknesses section. To summarize: 
1. Does the model incorporate RNA modifications, cellular localization, or folding kinetics? Can the authors add some discussion on how might this enhance performance given the limited experimental training data or if they can provide some analysis for the same, if possible? 
2. Apart from sequence recovery and perplexity, did the authors analyze structural stability and functional motifs that affect RNA viability?
3. Did the authors experiment with different RNA backbone representations, and what impact did this choice have on the results?
4. Can the authors analyze failure cases to improve understanding of gRNAde's limitations?
5. Have the authors evaluated how varying RNA sequence lengths affect performance?
6. Will the authors benchmark against the RNAInvBench paper (Cole et al., 2024) to assess the role of pseudoknots in their predictions as its importance has been highlighted as a crictical aspect to compare RNA inverse design models in RNAInvBench paper?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper is dedicated to solving the inverse folding problem of RNA. Given multiple 3D conformations of an RNA, the method designs the corresponding RNA sequence. The experimental section demonstrates the effectiveness of this approach.

### Strengths
This is an interesting paper. The biggest difference from past methods is that this paper can take into account the flexibility of RNA structures, accept conformations of multiple RNAs simultaneously, and designs a reasonable model. I agree that this is a valid innovation point. This inclines me to accept the paper.

### Weaknesses
Although this paper contains some very interesting innovations, several key issues have led me to give it the current rating. I hope the authors can fix these problems. If these issues can be resolved, I will consider improving my rating.

1. In the first sentence of the abstract, the authors claim: "Computational RNA design tasks are often posed as inverse problems, where sequences are designed based on adopting a single desired secondary structure $\textbf{without considering 3D geometry}$ and conformational diversity." I believe that the phrase "without considering 3D geometry" is factually incorrect. Because RDesign[1] performs inverse folding based on the 3D structure of RNA, it should take 3D geometry into account. The authors should provide a reasonable explanation or correct all descriptions in the paper that claim "without considering 3D geometry."

[1] RDESIGN: HIERARCHICAL DATA-EFFICIENT REPRESENTATION LEARNING FOR TERTIARY STRUCTURE-BASED RNA DESIGN. $\textbf{ICLR 2024}$

2. The experimental section lacks a comparison with RDESIGN, which is also deep-learning-based. Moreover, in the abstract, gRNAde should be compared with RDESIGN rather than Rosetta, which would be more reasonable. Figure 3(a) shows the performance of gRNAde under different numbers of conformations. This experiment also needs to be compared with RDESIGN. Although RDESIGN can only accept one conformation, the authors should use the result of RDESIGN with a single conformation as a baseline for comparison.

### Questions
None

### Soundness
3

### Presentation
3

### Contribution
3
