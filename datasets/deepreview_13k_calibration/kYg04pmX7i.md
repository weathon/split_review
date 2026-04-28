# Molecular Active Learning: How can LLMs Help?

- Decision: Reject
- Avg Score: 4.40
- Scores: 5, 6, 5, 3, 3

## Abstract
Drug discovery, and molecular discovery more broadly, can be framed as a sequential active learning problem ---facing a candidate pool, strategies are designed to sequentially acquire molecules to assay, aiming to find the best molecule within the fewest rounds of trial and error.
To automate this process, Bayesian optimization (BO) methods can mimic the approach of human medicinal chemists by constructing \textit{representations} from existing knowledge, quantifying \textit{uncertainty} for the predictions, and designing \textit{acquisition} experiments that balance exploitation and exploration.
Traditionally, these three stages are implemented using building blocks such as graph neural networks (GNN) as representations, variational inference (VI) or Gaussian process (GP) for uncertainty quantification, and analytical expressions as acquisition functions.
To facilitate the integration of both domain-specific and general knowledge into various stages of this process, in this paper, we investigate which parts of this workflow can be augmented or replaced by large language models (LLM).
To this end, we present \textbf{COLT}, a software library for \textbf{C}hemical \textbf{O}ptimization with \textbf{L}anguage- and \textbf{T}opology-based modules, and thoroughly benchmark the combination thereof.
We found that \textit{none} of the LLMs, no matter incorporated at what stage, can outperform the simple and fast Bayesian baseline with GNN and GP.
As a remedy, we offer a new tuning recipe with direct preference optimization (DPO), where the optimization of synthetic properties can be used to increase the efficiency of the acquisition in real-world tasks.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper apply the active learning pipeline for drug discovery. By continuously selecting molecules from the pool to query their properties, high-quality molecules are obtained. Under this setup, three processes called GNN, VI and GP all have the potential to be replaced with LLMs and enhance the whole active learning performance. Authors explore the problems of whether, why and how? Finally, they propose a new tuning recipe that can be effective with LLMs for the drug discovery task.

### Strengths
1. The paper is well organized and written. Although the fields of active learning and AIDD do not naturally overlap, readers can quickly get their key points.

2. The proposed method is reasonable, and the three parts of active learning are indeed expected to be enhanced by introducing LLMs. In particular, the author provides code demonstrations. Intuitively, the method does not have significant loopholes.

3. The experimental results are comprehensive and the conclusions are reasonable. The proposed remedial solution seems to maximize the effectiveness of LLMs.

### Weaknesses
1. I am not very familiar with this specific task. Can the authors tell if this is a standardized and widely studied task? Can they provide some baseline methods for active learning-based drug discovery?

2. By reading this paper, I can understand the purpose of the task and the approach of the active learning part. And I think the author gives the conclusions related to LLMs, which is encouraged. However, my concern is that if active learning based drug discovery is not a widely researched topic, the significance or applicability of this paper will be diminished. For example, if researchers often use other means to complete drug discovery tasks and rarely use active learning (AL), then for this community, constructing an AL-based baseline is the primary goal. Because AL for drug discovery itself may have challenges worth exploring, which may be skipped and ignored. So, in short, I am not denying the novelty and experimental integrity of the research in this article. I just doubt whether this article will be of great value to this community.

3. It seems that ChemLLM is not better than LLaMA, which is counterintuitive for chemistry-related tasks. Can the authors explain why?

### Questions
Maybe I miss something, but why "1.61" in Table 1 is bolded not "1.29"? Can the authors provide more details?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper presents what is effectively an ablation study between optimizing molecules with LLMs vs Bayesian optimization, finding that LLMs don't help very much, although fine-tuning does help.

### Strengths
- Scientific honesty: this paper asks an important question, finds that the less exciting "null hypothesis" is true, and still reports that. With almost every other paper at ICLR being a "use my method" paper, I found this refreshing
- The question asked is timely and important
- Experiments ask good questions (e.g. investigating domain-specific models and synthetic tasks after initially seeing poor results)
- Experimental methodology seems valid
- Paper is upfront about the limitations of its study
- Presentation of the paper is very nice

### Weaknesses
 - Some important experimental details unclear (see "questions" section)
- The study does not address a question which is perhaps more relevant: how will LLMs perform _after some fine-tuning_. I think the paper should list this as a limitation, or potentially change the conclusion to "fine-tuning will probably be required to get strong performance"
- Some descriptions of BO seem slightly incorrect.
  - Learning a representation of a graph is an _optional_ step in BO, since one could use a model like a GP with a graph kernel that does not convert the graph into a vector. There are many such kernels supported in libraries like Grakel.
  - DKL is not an approximation to the posterior: it is a model whose exact posterior is analytically tractable.
- PoI acquisition function is not really used much because it is insensitive to the magnitude of the improvement. I recommend reading Chapter 7 of Garnett's 2023 BO textbook for details. I think that using the UCB acquisition function instead would be a more interesting choice.
- The paper does not adequately address the potential for overfitting when training deep learning models (like GCNs and DKL) on very small datasets, which is a critical concern given the sequential nature of the experiments. The performance of these models is likely to be highly sensitive to regularization techniques, which are not discussed in sufficient detail.

### Questions
1. Experimental details:
  - How is the GCN trained, given that you start from no data?
  - How are GP hyperparameters set? Optimization performance is very sensitive to these parameters.
2. On line 370 you write: "require by magnitude more time". Is this a typo? Maybe you be "require an order of magnitude more time"
3. In table 1, what are the ± values? Standard error? Standard deviation? Something else?

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
4

### Summary
This paper addresses the challenge of active learning for molecular discovery, i.e. finding optimal molecules from large candidate libraries with minimum experimental evaluations. The authors formalize the active learning workflow into three modules: (1) representing molecules in vector form, (2) an uncertainty-aware regressor for predicting target properties, and (3) acquisition of the next candidate from the full library, balancing exploitation and exploration. The paper investigates whether some or all of these modules can be substituted with large language models to improve optimization efficiency. Empirically, the authors find that, even with domain-specific LLMs, no performance improvements can be observed. Instead, architectures with domain-specific inductive biases (i.e. GNNs for molecules) remain state-of-the-art for optimization.

### Strengths
* The study targets a highly topical problem with enormous implications in both academic and industrial settings. 
* The paper, particularly the introduction and background sections, are very well written, making the paper clear and accessible. 
* The LLM modules for molecular representations, molecular property prediction, and decision-making, are mostly well-designed. The design of their empirical evaluations is systematic and carefully crafted. 
* The study effectively conveys an important message: LLMs may not always be suitable replacements for domain-specific models, particularly in those fields where knowledge and data are largely non-textual, and model architectures with strong inductive biases exist.

### Weaknesses
 * The selected optimization tasks may not be adequate to rigorously test optimization algorithms. (a) The studied properties (solubility, lipophilicity) have relatively well-known structure–activity relationships, that expert chemists could predict, and that are potentially well-reflected in the training data of LLMs. This contrasts with real-life applications like drug discovery, where the structure–activity relationships are much harder to predict – for both expert chemists and ML models. (b) The candidate pools are small and biased.
* The optimization performance is measured by cumulative regret. However, this does not necessarily align with the primary goal of molecular discovery, which is to identify the optimal candidate(s). Alternative metrics that better capture this objective should be considered, and it would be interesting to analyze whether these metrics consistently correlate with cumulative regret. 
* There is a lack of discussion on the statistical significance of findings and trends. Confidence intervals are omitted from the figures in Table 2. Given the large standard deviations in Table 1, it is unclear which of the discussed trends are actually significant. This should be addressed in the discussion. In my opinion, a generic sentence in the “Limitations” paragraph is not sufficient. 
* The Direct Preference Optimization strategy lacks sufficient detail. How are the GNN–GP reference trials generated? Are they generated on the same optimization problem? If so, a direct comparison to other optimization strategies would be flawed. The need for initial GNN–GP-guided experiments to fine-tune the LLM, followed by a second campaign, would greatly increase experimental costs. In this scenario, all metrics should be compared over all performed experiments. Does the second, LLM-guided identify find any “good” candidate molecules that were not found in the initial GNN–GP trial? While I see that this strategy could be of value e.g. in a transfer learning setting or a multi-fidelity scenario, this paper does neither evaluate nor discuss these aspects.
* The authors use Deep Kernel Learning as a domain model. Comparison with simpler domain-specific baselines, (e.g. fixed representations with a GP surrogates, see ref. 48), would place the findings in a broader context. What is the value of deep learning in the very-small-data regime? Do the inductive biases in GNNs make any difference?  
* On p. 2, the discussion of the “small data regime” could be clearer. While the number of labeled data points is indeed very small (often only hundreds), the library of possible candidates can be extensive (up to billions, possibly more). Distinguishing these scales would clarify this section of the paper. 
* The paper would benefit from investigating into the origins of the observed performance differences, e.g. through ablation studies or other systematic analyses. Are these differences due to poorly aligned representations, insufficient regression performance, lack of uncertainty calibration, or other factors?

### Questions
* The authors use Deep Kernel Learning as a domain model. Comparison with simpler domain-specific baselines, (e.g. fixed representations with a GP surrogates, see ref. 48), would place the findings in a broader context. What is the value of deep learning in the very-small-data regime? Do the inductive biases in GNNs make any difference?  
* On p. 2, the discussion of the “small data regime” could be clearer. While the number of labeled data points is indeed very small (often only hundreds), the library of possible candidates can be extensive (up to billions, possibly more). Distinguishing these scales would clarify this section of the paper. 
* The paper would benefit from investigating into the origins of the observed performance differences, e.g. through ablation studies or other systematic analyses. Are these differences due to poorly aligned representations, insufficient regression performance, lack of uncertainty calibration, or other factors?

### Soundness
3

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
4

### Summary
The authors investigated the effectiveness of using large language model (LLM) in the molecular activate learning. Specifically, they  evaluate LLM as a replacement to different modules in the active learning pipeline including molecule featurizer, uncertainty quantification, and acquisition. A software package called Chemical Optimization with Language- and Topology-based modules (COLT) is developed to carry out experiments. The authors revealed that the utilization of LLM in active learning does not bring performance improvement or speedup. To address the underwhelming performance of LLM, the authors proposed to use discrete preference optimization (DPO) to improve LLM's performance in active learning.

### Strengths
The approach used by the author to examine which part of molecular active learning can be replaced by LLM is interesting. The software effort to incorporate LLM for molecular active learning is also valuable.

### Weaknesses
1. Literature review is not comprehensive. Active learning/bayesian optimization for compound virtual screening from both academic and industry are not included. Specifically, methods employing Gaussian processes or other kernel-based approaches for modeling structure-activity relationships, which are common in the field, are absent. The review also lacks discussion of techniques that explicitly handle the high dimensionality and sparsity of chemical space, such as those using molecular fingerprints or graph-based representations in conjunction with active learning. 

2. There are some mis-claims in the paper. For instance in line 82-83, pharmaceutical companies are definitely trying to perform virtual screening on libraries much larger than million-scale. A simple example of such large libraries is the Enamine database. Furthermore, the statement about the scale of wet-lab high-throughput screening is also misleading, as many companies routinely screen libraries exceeding millions of compounds using techniques like DNA-encoded libraries.

3. Experiments deviate from actual use cases of active learning in drug-discovery industry. The major goal of using active learning is to screen for hit. Therefore, a docking score would be a better option than labels in MoleculeNet. The use of MoleculeNet datasets, while convenient, does not reflect the challenges of real-world drug discovery, where the goal is to identify novel active compounds against a specific biological target. The authors should at least run experiment on the million-scale Emine HTS dataset. The current experimental setup fails to address the noisy and often unreliable nature of experimental data, which is a critical aspect of active learning in drug discovery.

4. More acquisition functions should be used as baseline such as greedy, upper confidence boundary etc. The current selection of acquisition functions is limited and does not explore the full range of options available in active learning. For example, the lack of comparison with entropy-based acquisition functions, which are useful for exploring the chemical space, is a significant oversight.

### Questions
1. I am curious about the format of output when LLM is used as a feature extractor. Are those features vector of specific sizes? Can authors elaborate more? 

2. What are the y-axis label and unit of the figure above Table-1?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 5

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
The authors investigate how LLMs can be used in Bayesian optimization for molecular properties. They decompose the optimization loop into three parts: representation, uncertainty quantification, and acquisition. Using this framework, they iteratively replaced each of these parts with an LLM and compared its performance, using their modular framework COLT. The authors found that LLM-augmented campaigns could not outperform the state-of-the-art baseline models, except when direct preference optimization was introduced.

### Strengths
1) The authors have chosen to tackle a significant problem in the chemical sciences. Molecular discovery is a difficult problem and requires either expensive experimental evaluations or physics-based simulations. LLMs have shown promise in accelerating the evaluation of molecular properties, and understanding where LLMs can deliver the most impact in the discovery process is certainly useful knowledge.

2) The authors have proposed an interesting framework where LLMs can impact the discovery process in a Bayesian loop. Decomposing the process in this manner is a clear way to define the problem.

### Weaknesses
1) The authors have chosen to tackle a significant problem in the chemical sciences. Molecular discovery is a difficult problem and requires either expensive experimental evaluations or physics-based simulations. LLMs have shown promise in accelerating the evaluation of molecular properties, and understanding where LLMs can deliver the most impact in the discovery process is certainly useful knowledge.

2) The authors have proposed an interesting framework where LLMs can impact the discovery process in a Bayesian loop. Decomposing the process in this manner is a clear way to define the problem.

3) The authors intended to show whether LLMs could impact the molecular discovery process -- however, Ramos et al. (2023) and Kristiadi et al. (2024) have extensively demonstrated this already, so I am not sure what the contributions of the authors were. As the authors correctly identified, Kristiadi et al. (2024) has shown how LLM-based molecular representations can be used in molecular discovery, while Ramos et al. (2023) has shown how to obtain uncertainty from an LLM. 

4) Kristiadi et al. (2024) proposes that the methods employed by Ramos et al. (2023) are not Bayesian in nature -- a direct comparison between the Bayesian baseline and the “stochasticity” of LLM-output does not seem sound to me. 

5) While COLT was proposed as a software library, the code is not well-documented and is not installable.

6) The package seems very similar in capabilities to the package provided by Kristiadi et al. (2024), in that BO and LLM-based optimizations with GP-based UQ are also already features. The only extensions seem to be a graph-based representation and the inclusion of variational inference as a UQ estimate, which to me are not extensive enough to note the two packages as different.

7) The manuscript is generally unclear in the following aspects:
    - Key details regarding how the baseline GCN and GAT models were set up or trained are missing.
    - Information regarding the number of prompts used to generate the UQ estimates were missing.
    - The section investigating dataset leakage from the LLMs and synthetic data generation is unclear in terms of the problem setup, and the results are under-evaluated.
    - Even though DPO performed the best, which is a key takeaway of this paper, the reason why Qwen was chosen over all other LLMs is unclear. Additionally, the explanation of how the DPO experimental setup was done, and how DPO generated these results are unclear.
    - In Table 1, merging all the LLM methods into one line is extremely unclear, and it’s not straightforward to tell which LLM is performing the best. 
    - Additionally, all the lines in Table 1 strongly overlap and it is difficult to tell which method is performing better. It almost looks to be like the differences between each model are not significant.

8) A minor point, but the code chunk at the header of Section 4 claims that LLM-based representations can be combined with Bayesian methods of UQ or acquisition, which I think is misleading. 

9) GAT + VI + EI performs the best in ESOL, and the table numbers are incorrectly bolded.

### Questions
1) It appears that the GCN and GAT models were trained on each of the full tasks -- after which the representation was used for Bayesian optimization. This sounds to me like a weird baseline because this is contingent on having access to the full dataset. Could you explain this design choice? Why not use Morgan fingerprints instead as the baseline whose representations are output agnostic?
2) How do the baseline methods from Ramos et al. (2023) and Kristiadi et al. (2024) directly compare on the same task? Please ensure that the same exact methods (architecture, LLM choice, etc) were respected for a meaningful comparison.
3) I have general concerns about the LLMs used in this paper, and how they were used. As such, could you perform the experiments on all the below-mentioned models across the Bayesian loops and DPO, and across more tasks to get a better sense of how the LLMs could impact the performance? 
    - Llama and Galactica are known to perform poorly on scientific tasks (see https://arxiv.org/abs/2402.13414, https://openreview.net/pdf?id=hSmn7BQZ2v, and https://arxiv.org/abs/2305.18365). Fine-tuning Llama seems to help (https://www.arxiv.org/abs/2409.06080), but this was not explicitly performed in this paper.
    - It seems premature to conclude that LLMs dont work if one does not compare the results from GPT-4, which is considered state-of-the-art.
    - Some smaller language models like ChemT5 or BioT5 have also been shown to outperform GPT4 in certain cases. 
    - Qwen was used in DPO, but not in any of the other benchmarks, so it’s unclear if the benefits came from Qwen or from DPO alone.
    - Only three LLMs were sampled across your experiments. I think showing that these results apply across a wider variety of LLMs would help one of the main claims of the paper. 
    - These results were only demonstrated for three tasks -- I also think it’s premature to draw conclusions from such a small sample.
    - The apparent “dataset leakage” problem from Yu et al. (2024) should have been demonstrated in the experiments -- this would have justified quantitatively why the synthetic dataset generation was necessary.
4) Could you explain exactly how you described the tasks in the prompts for the “description” subscript models? Showing the exact prompt in the Appendices section of the paper will help.
5) How confident are you with the uncertainty quantification methods proposed by Ramos et al. (2023)? I have my reservations about directly using LLMs for regression tasks (i.e to obtain real-valued numbers). In Section 3.2, these tokens are fed directly into the prompt. An ablation study to show that these numbers are actually correctly harnessed by your model in predicting the properties of a new molecule would be important.
6) How many samples are fed into the UQ part in Section 3.2, and how are they selected? The authors described that there is an issue with token length, but it was not clear to me exactly what they did to mitigate that issue.
7) Can you expand exactly what the motivation behind creating the artificial target as such is necessary? While I appreciate the mathematical definition of how the target is obtained, how this compares to the other datasets you compared against is not clear.
8) I have the same concerns for the definition of the DPO and a chemical interpretation of this task beyond just “helping the LLM to think like a GP”.
9) The difference in the performance on the synthetic dataset between traditional vs LLM approaches is “more obvious” -- but what does this actually mean? What is the source of this difference, and could you evaluate it?

### Soundness
2

### Presentation
2

### Contribution
1
