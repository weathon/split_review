# Regulatory DNA Sequence Design with Reinforcement Learning

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 5

## Abstract
Cis-regulatory elements (CREs), such as promoters and enhancers, are relatively short DNA sequences that directly regulate the expression of specific genes. The fitness of CREs, i.e., their functionality to enhance gene expression, highly depend on its nucleotide sequence, especially the composition of some special motifs known as transcription factor binding sites (TFBSs). Designing CREs to optimize their fitness is crucial for therapeutic and bioengineering applications. Existing CRE design methods often rely on simple strategies, such as iteratively introducing random mutations and selecting variants with high fitness from a large number of candidates through an oracle, i.e., a pre-trained gene expression prediction model. Due to the vast search space and lack of prior biological knowledge guidance, these methods are prone to getting trapped in local optima and tend to produce CREs with low diversity. In this paper, we propose the first method that leverages reinforcement learning (RL) to fine-tune a pre-trained autoregressive (AR) generative model for designing high-fitness cell-type-specific CREs while maintaining sequence diversity. We employ prior knowledge of CRE regulatory mechanisms to guide the optimization by incorporating the role of TFBSs into the RL process. In this way, our method encourages the removal of repressor motifs and the addition of activator motifs. We evaluate our method on enhancer design tasks for three distinct human cell types and promoter design tasks in two different yeast media conditions, demonstrating its effectiveness and robustness in generating high-fitness CREs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
In this paper, the authors introduce TACO, a method for designing DNA cis-regulatory elements (CREs). TACO leverages reinforcement learning (RL) fine-tuning of a pretrained DNA autoregressive generative model to maximize CRE activity while maintaining diversity.  The approach involves training an "oracle" model on activity data and extracting transcription factor binding motifs (TF motifs) by interpreting the oracle's extracted features using SHAP values.

TACO formulates the Markov Decision Process (MDP) problem with an empty initial state, where actions involve appending nucleotides to the sequence at each step. Episodes terminate after T steps. The oracle's prediction serves as the final reward, while intermediate non-zero rewards are assigned based on the extracted TF motifs to guide the search process.  Specifically, negative rewards are given for repressive motifs, and positive rewards are given for enhancing motifs.

The authors compare TACO to standard optimization methods using the same oracle on datasets for promoter activity in yeast and enhancer activity in human cell lines.  Their results demonstrate that while TACO does not necessarily yield higher predicted activity for generated CREs, it achieves greater diversity compared to standard optimization methods.

### Strengths
- The problem of generating diverse and high-fitness CREs is a crucial area of biological research, and I commend the authors for their contribution to this field. 

- I particularly appreciate their exploration of RL fine-tuning, a novel approach in this domain with promising potential, given its success in other areas. 

- The authors' meticulous design of the oracle for each benchmark is commendable. 

- The automated extraction of TF motifs using SHAP values from the trained LightGBM oracle, coupled with its use in reward shaping for guided search, is an interesting approach. 

- The paper is well-written and structured, ensuring clarity and ease of understanding for the reader. The technical details are well-presented, and the comprehensive literature review effectively covers important and recent works.

### Weaknesses
The primary weaknesses of this paper lie in the experimental setup and the choice of baselines.

- Across all datasets, the authors report that all methods generate sequences with strong activity. This suggests that the tasks may be "too easy," potentially undermining their suitability for benchmarking generative models like TACO, which aim to generate high-activity sequences. The reported high activity levels across all methods, including simple optimization techniques, suggests that the fitness landscape might be relatively flat or that the oracle is not sufficiently discriminative, making it difficult to assess the true capabilities of TACO in generating high-fitness sequences. A more challenging benchmark would involve a fitness landscape with more pronounced peaks and valleys, requiring more sophisticated exploration strategies.

- While the included baselines are relevant, they rely on older optimization techniques that have been consistently outperformed by modern generative methods, such as autoregressive models and diffusion models, particularly in terms of generating diverse data. Consequently, the reported results, while valid, are not particularly insightful. A more compelling analysis would compare different generative techniques for CRE design. The authors acknowledge in their literature review the emergence of diffusion models (D3 and DNADiffusion) and autoregressive models (regLM) specifically for CRE design. Benchmarking TACO against these methods is essential. The absence of comparisons with state-of-the-art generative models limits the ability to assess the true novelty and effectiveness of TACO. Specifically, methods like autoregressive models and diffusion models have demonstrated superior performance in generating diverse and high-quality sequences, and their inclusion would provide a more rigorous evaluation of TACO's capabilities.

- The introduced diversity metric primarily ensures that generated sequences avoid collapsing to a single mode. While this highlights the known limitations of standard optimization techniques like genetic algorithms, it does not comprehensively evaluate the overall quality of sequences generated by a generative model like TACO. Given that predicted activity appears to be non-discriminative, incorporating additional quality and diversity metrics from a data distribution perspective would be beneficial. I recommend exploring the validation pipeline introduced in D3, which is highly relevant in this context. The current diversity metric, while useful for avoiding mode collapse, does not capture the full spectrum of sequence diversity. Metrics that assess the distribution of generated sequences in the embedding space, such as the mean pairwise cosine similarity, would provide a more comprehensive view of the diversity achieved by TACO. This is particularly important given that the predicted activity appears to be non-discriminative.

- The introduction of reward shaping based on automatically extracted TF motifs is presented as a key contribution; however, the results in Figure 5 do not strongly support its efficacy. Specifically, TACO achieves comparable diversity with alpha=0 (no reward shaping) while maintaining high sequence activity. Including TACO with alpha=0 in Tables 2 and 3 might demonstrate its performance, as it would likely achieve the highest activity while maintaining high diversity, the primary differentiating factor in these studies. The lack of a clear benefit from the TFBS reward shaping raises questions about its practical utility. The comparable performance of TACO without reward shaping suggests that the core RL fine-tuning mechanism may be sufficient, and the added complexity of the TFBS reward may not be necessary. A more detailed analysis of the impact of the TFBS reward, including a broader range of alpha values, would be beneficial.

### Questions
Questions/Comments:

- Algorithm 1 appears too early in the paper, as it references elements and equations introduced later. Moving it further down would improve the flow.

- Equations 1, 3, and 4 could be moved to the appendix, as they are well-known in the field.

- Could the authors provide more details on how the maximum number of steps T is determined?

- Could the authors clarify the following statement: "We set the maximum number of optimization iterations to 100, with up to 256 oracle calls allowed per iteration." Is one optimization iteration equivalent to one episode? If so, does "256 oracle calls" imply that T=256?
Why did the authors retrain HyenaDNA from scratch on D_star? Why not start from a pretrained HyenaDNA model?

- The authors claim a lack of strong encoder backbones like ESM in the DNA field. This seems inaccurate, given recent publications like Nucleotide Transformer, DNABert, HyenaDNA, Caduceus, Evo, Borzoi, Enformer, and many others. If the authors disagree with the claims from these papers, they should provide a detailed argument.

- Using "medium" for both a dataset and a metric could be confusing.

- The authors frequently cite Almeida et al. but do not use their fly enhancer data in the evaluation. What motivated this decision?

- At the end of the "conditional DNA generative models" section, the authors state: "However, these generative methods are designed to fit existing data distributions, limiting their ability to design sequences that have yet to be explored by humans." However, TACO seems to suffer from the same limitation, as its exploration space is bounded by the trained oracle, which is itself limited by the available data distribution. I would appreciate the authors' perspective on this.

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper presents a novel method for designing cis-regulatory elements (CREs) using a reinforcement learning (RL) framework that enables the generation of high-fitness, cell-type-specific, and diverse sequences. The primary objective is to produce CRE sequences that are capable of enhancing gene expression. Current methods, often reliant on greedy algorithms or directed evolution approaches, lack biological insight for guiding the exploration of sequence space. These traditional methods tend to get trapped in local minima, resulting in CREs that are limited in diversity and difficult to interpret biologically.

Main Contributions

Development of an RL Framework: The authors introduce a reinforcement learning framework that fine-tunes a pre-trained autoregressive generative model, HyenaDNA, for designing high-fitness, cell-type-specific CREs. This approach also aims to maintain sequence diversity, addressing limitations in traditional methods.

Integration of TFBS Modulation: The RL process actively incorporates transcription factor binding sites (TFBS) to encourage biologically meaningful changes, such as removing repressor motifs and adding activator motifs. This guidance helps enhance the regulatory potential of the generated sequences.

Evaluation Across Multiple Contexts: The proposed method is tested across different tasks:
An enhancer design task for three distinct human cell types.
A promoter design task across two yeast species in varied media conditions, demonstrating the framework’s adaptability to different biological contexts.

### Strengths
This paper makes several contributions to the field of DNA sequence design:

Biologically Guided Sequence Design: By integrating TFBS modulation into the RL framework, the approach maintains biological relevance, encouraging the addition of activators and removal of repressors, which enhances the model's potential for generating functional CREs.

Innovation in CRE Design: The reinforcement learning paradigm offers a new way to explore the sequence space more effectively, overcoming the limitations of greedy and evolution-based methods that often produce low-diversity sequences.

Comprehensive Evaluation: The authors rigorously evaluate the framework’s performance on both enhancer and promoter design tasks, providing evidence for its flexibility and applicability to various regulatory elements and cell types.

Overall, the paper is written well and of good quality.

### Weaknesses
The paper would benefit from a more extensive Discussion section to contextualize the results further.

Minor Points
Include references to Appendix B/C in the introduction or caption of Table 1.
In the preliminary experiment described in the introduction, add a reference to Appendix E or specify the number of TFBS scanned for each model.
In Figure 2, clarify the meaning of the BOS token and C or T action symbols.
Figure 3 is missing "A" and "B" labels in the visuals.
In Appendix F, correct the sentence, "Our results indicate that only the metric has a significant impact on the final performance. The ablation results are summarized in Table 7."
Explicitly describe the regularization technique (entropy regularization) discussed in Section 4.3 and reference it in the RL Implementation Details section.
Section 4.3 might be better suited as an appendix to improve readability, and increase space for a larger discussion/conclusion.

### Questions
1.What motivated the choice of the HyenaDNA model beyond it being the only published autoregressive DNA language model? Is its receptive field size of 1 million excessive for training on CREs, given that the DNA sequence lengths are only 80 and 200?

2. How was the yeast Enformer model trained? Specifically, what sequences were used, and what was the target variable for regression?
Why do the fitness percentiles selected for D range from 20-80%? Why not use the full range, such as 10-90%, to potentially capture a wider diversity?

3. Did you consider using cosine similarity as a distance metric when training the LightGBM models?

4. Have you thought about adding a feature in the LightGBM model to consider interactions between two TFBS, requiring that they be present together or at a specific distance? This could capture complex TFBS interactions as discussed in Georgakopoulos-Soares et al., "Transcription factor binding site orientation and order are major drivers of gene regulatory activity" (Nature Communications, 2023). (This could be added to the discussion.)

5.Could you clarify whether a specific threshold or adaptive strategy is used to define "low likelihood" sequences in the regularization approach, and how this affects the exploration-exploitation balance in sequence generation?

6.Why did you choose six sequences for the "Top" evaluation metric, and why generate a total of 128 sequences?

7. Could it be more informative to report fitness values close to, but not capped at, 1 to show variability among high-fitness sequences? Additionally, could you provide the standard deviation of fitness scores across generated sequences for each method in Table 2? If the standard deviation is 1, could u sample more sequences? Would you also consider reporting on 'Low' or 'Bottom' fitness sequences to better understand model limitations and areas for improvement?

8. Given that diversity appears beneficial for finding novel targets, would continuing beyond 100 iterations lead to further exploration and potentially better results? Additionally, could you elaborate on how initial conditions influence the observed diversity and fitness metrics, and whether different starting points could impact the algorithm’s optimization effectiveness?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The authors propose a reinforcement learning (RL) method for designing cis-regulatory elements. The method uses a pre-trained autoregressive model of DNA sequences as its policy and fine-tunes this model throughout the training process. The method incorporates domain knowledge by adding a reward that encourages generated sequences to contain known transcription factor binding site motifs. The authors test their method against a number of relevant baselines on a set of yeast promoter and human enhancer design tasks, showing improved performance over the baselines.

### Strengths
* The paper is clearly written. The problem and method are well-motivated and clearly explained.

### Weaknesses
 * The evaluation tasks in this paper do not represent a realistic scenario for biological sequence design and do not follow established practices from the literature. Biological sequence design with machine learning is best characterized as an offline model-based optimization (MBO) problem, where there exists a fixed dataset associating sequences to fitness, but intermediate fitness measurements can not be collected during the process of optimization. This is because biological experiments are expensive but highly parallelizable, so it it usually only economical to collect a large number of measurements at once, rather than a small number of intermediate measurements. A possible approach to solving this offline MBO problem is train a model to predict fitness from sequence, and then use this "surrogate" model to guide an optimization procedure (which could be RL or another process). Note that the surrogate model is sometimes misleadingly referred to as an oracle. The most important concern with these methods is that the surrogate model is not a good model of the ground truth fitness function in regions that are out-of-distribution (OOD) of the fixed training set. Thus, the major methodological advancements in offline MBO have been aimed at controlling the optimization such that it does not produce sequences that are OOD of the training set. This problem is discussed extensively in, e.g., "Conditioning by adaptive sampling"  (2019) by Brookes et al., 
 and "Conservative Objective Models for Effective Offline Model-Based Optimization" (2021) by Trabucco et al. In the paper under review, the authors also train a surrogate/oracle model to guide their optimization but make two choices that minimize the practical relevance of their evaluation tasks:
    1. They train the oracle on the complete dataset, even though the intention of the task is to design high fitness sequences using only low fitness data. Therefore, when they query the oracle to calculate rewards, they are treating the oracle as a ground truth fitness function that they are collecting intermediate rewards for. As discussed above, this is unrealistic for biological sequence design.
    2. They use predictions from the oracle as the final evaluation criteria. This again treats the oracle as the ground truth fitness function. 
The combination of choices (1) and (2) mean that the evaluation tasks simply measure the ability of the method to optimize the oracle. As discussed in the citations above, optimizing the oracle without controlling for OOD concerns will usually result in designing unrealistic sequences that are OOD of the initial training set. Evaluation of methods for biological sequence require careful consideration of these factors, which has led to the introduction of evaluation frameworks such as FLEXS (referenced in the paper); these factors must be taken into account when designing tasks to evaluate the TACO method introduced in this paper.
* A recent method has been introduced that uses Conservation Model Objectives (COMs) to design CREs (["Designing Cell-Type-Specific Promoter Sequences Using Conservative Model-Based Optimization" (2024) by Reddy, et. al.](https://www.biorxiv.org/content/10.1101/2024.06.23.600232v1)). This method considers the factors discussed in the previous bullet, and contains strong validation with in-vitro experiments. It is not cited in the paper under review and not compared against. In order to be a strong contribution, the paper under review must cite this COMs paper and compare against the method. 
* The novelty of the method seems overstated as written. In particular, RL has been applied to biological sequence design in Angermueller et. al, 2019, which is not made clear in the Related Work section. Given this, the novelty of the authors' method is in the use of an autoregressive model as the policy, and the addition of the TFBS reward. This should be made more clear by making clear the contributions of Angermueller et. al, 2019 and how the authors' method improves over this.
* As mentioned above, the authors introduce two novel concepts to the use of RL in sequence design. In order to understand the impact of these concepts, they should be fully ablated on all of the evaluation tasks. In particular, it would be informative to know how a different policy model performs with the TFBS reward and how the autoregressive policy performs without the TFBS rewards on all of the design tasks. This will clarify the key contributions of the paper.
* Figures 3A and 5A are below acceptable quality for a publication at ICLR. Both appear to be screenshots and contain either unreadable or poorly labeled axes/subplots. 
* The References section contains incorrect and inconsistent citation formatting. In particular, many titles are lower case when they should be upper case and inconsistent information is included in the citation (e.g. sometimes URLs are provided and other times they are not). Also, many citations refer to an arXiv pre-print, rather than the published version of a paper; this must be checked and fixed.

Minor errors:
* Second sentence of abstract is grammatically incorrect (should "CRE" be plural?)
* Equation 1: p_theta should be pi_theta
* Line 368: (Hansen) is an incomplete reference

### Questions
* The intermediate TFBS reward only gives a reward to sequences that contain known TFBS motifs. This seems like it limits the model to recombining known motifs, rather than learning to design new motifs. Since TFBS motif design is a task that is of interest to the community (as is mentioned in Related Work), the form of the reward may limit the practical applicability of the method. Can the author's clarify whether their method is able to design novel TFBS motifs? If not, can the author's clarify whether this is an important limitation or not?

### Soundness
2

### Presentation
3

### Contribution
2
