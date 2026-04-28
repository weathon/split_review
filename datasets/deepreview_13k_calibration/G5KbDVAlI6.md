# Gene Regulatory Network Inference in the Presence of Selection Bias and Latent Confounders

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 3, 5, 3

## Abstract
The study of gene regulatory network inference (GRNI), with a focus on uncovering causal relations among genes, holds significant potential to explain fundamental biological processes, such as how cellular identity is established or disrupted in disease. Unfortunately, current methods fail to adequately interpret the widespread phenomena of differential gene expression. The limitation can largely be attributed to the overlook of the selection process (e.g., survival bias), which is ubiquitous and fundamental in biology. Furthermore, recent studies have shown that gene expression is regulated by latent confounders (e.g., non-coding RNAs). Both of which can lead to spurious dependencies, thereby distorting GRNI results. To mitigate these challenges, we propose a novel algorithm, called  Gene Regulatory Network Inference in the presence of Selection bias and Latent confounders (GISL). It is designed to uncover the causal structure by leveraging data across multiple distributions obtained via gene perturbation. Surprisingly, we find that the qualitative structure information, selection process, and latent confounders are partially identifiable without any parametric assumption under mild graphical conditions. Experimental results on both synthetic and real-world single-cell gene expression datasets demonstrate the superiority of GISL over existing strong baseline methods.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper mainly addresses the inference of gene regulatory networks (GRNs) based on single cell perturb-seq data. Traditional Single cell RNA seq data provides a count table of transcribed RNAs so it offers a snapshot of gene expression profile of the cell state. With the help of CRISPER editing, we can knock down/off a single gene and then observe the expression of all the other genes in this condition. 

While people may think we can recover the causal dependencies by directly comparing the difference between knock off and wild type in perturb seq, the authors of this paper point out this is not the case. With evidence, they argue that "dependencies can be generated in three ways: through causality, latent confounders, or selection bias". So the relationships we observe could totally be false positive. Later in the paper, they provide solutions/partial solutions for these two errors. 

In the case with selection bias but without latent confounder, the author argue that the dependencies coming from selection bias would be symmetric while the true causal relationship should be asymmetric (based on the DAG assumption). Essentially, they prove that with the perturbation data, the causal structure could be identified by testing the marginal and conditional independence. 

In the case that comes with both selection bias and latent confounder, they argue that the dependencies from latent confounder should also be symmetric. However, since the introduction of latent confounder also increases the freedom, the causal structure could be partially identified. 

This paper is backed up by experiments on both synthetic and real world data.

### Strengths
For the field of GRN inference, the discussion in this paper are not commonly discussed or well understood by the community. I think this paper do provide some valuable insights from the perspective of theoretical causal inference/discovery. 

The introduction of this paper is well motivated and attractive. The theoretical piece of this paper is very nicely written, clear and technically sound. The proposed method is novel and make sense. The flow of the paper is also sequential and well planned. The experiment on synthetic data is well designed and the results supports the main claims of this paper.

### Weaknesses
While I do enjoy reading this submission and I really like the concepts and awareness proposed in this paper, I do have a significant concern in terms of the actual usability of this method in real world and I think the flaw is in fact in contradiction of what the authors are trying to achieve. 

1. One of the two main motivations of this study is to address the potential existence of latent confounder. The real world use case that the author provided is the existence of non-coding RNA, which is true. However, before we even come to non-coding RNA, can we make sure that we can at least have the capacity to model all protein coding genes? Apparently, this is not possible with the proposed method. We know that human have 20,000 protein coding genes and even yeasts have 6,000 genes. The PC method that the author used in this study is not really scalable at this scale and the added iterative updating mechanism of the proposed algorithm only makes the runtime worse. In fact, in the real world experiments of this study, only **5** genes are considered. In the synthetic example, the largest net has roughly 20 nodes. It means that to use this algorithm, you can only use a tiny slice (0.025 - 0.1%) of all the available data. So some of the genes that you removed ultimately become the "latent confounders" while they are not actually "latent"... That says, you are literally creating problems to solve for no good reasons... This is my biggest concern with this paper. Please provide a justification on that. You may consider replacing PC with more scalable methods (not sure if it's possible for the time frame) or discuss the case when heavy gene filtration is necessary and valid. 

2. In connection with point 1, please provide a discussion on the runtime and provide clock time for the synthetic and real world experiment. 

3. Baseline methods in this study includes PC, GES, and GIES. They are well-known causal structural learning methods. However, since we are talking about GRN inference here, do you want to include some common GRN inference methods, such as GENIE3, Grnboost or DCI (as you mentioned it in the introduction)? 

4. In the real world experiment, can we have a figure of the results on the same data from PC without the updates in GISL? 

5. The literature review on GRN inference on page 2 needs some improvements. Right now, it's mostly focusing on causal discovery. There are only 5 references that are actually talking about GRN and 2 of them are not GRN inference method paper. Levine's 2005 PNAS paper talks about GRN but it has nothing to do with GRN inference based on transcriptomics data. Pratapa's BEELINE is a standard benchmarking dataset in this field but it's not a method. The other 3 paper are only briefly mentioned in one sentence.

### Questions
Again, my biggest concern and question is mentioned in the weakness section. 

Also, here is a general question that I have: many efforts in this method is to turn undirected edges predicted by PC to directional. However, we know that some genes are working in groups and they are just co-expressed as a group. A good example would be those histone genes. In gene network, you will see they form big hair balls. You mentioned that symmetry is a sign for either selection bias or latent cofounder. Do you think this kind of co-expression is a pattern for selection bias or something else? Do they really need to be directional?

### Soundness
4

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper addresses the problem of selection bias and latent confounders in Gene Regulatory Network Inference (GRNI) by proposing the GISL algorithm, which uses observational and gene perturbation data to identify causal relationships, selection processes, and latent confounders. The authors highlight that these factors are prevalent in real biological data but are often overlooked by existing methods. The study is well-motivated, with both theoretical and practical significance. Through theoretical analysis and experimental validation, the authors demonstrate the effectiveness of GISL in identifying causal structures in gene regulatory networks.

### Strengths
The idea of considering selection inclusion and latent confounders when inferring gene regulatory networks is of interest especially in the bioinformatic domain.  
The author describes the fundamental algorithm well, and they seem to give all relevant information to understand and reproduce their algorithm.

### Weaknesses
Some definitions and descriptions in the text are vague or misleading. 
The authors did not compare their method with latest state-of-the-art methods.
The data scale in the experimental section is too small, leading to an insufficient evaluation.

### Questions
1. Some definitions and descriptions in the text are vague or misleading. For example, in Definition 2.3, the phrase "Toy examples are shown in 9" is unclear. In the description of Figure 9, they mention "Definition 2.5" which is not provided in the main text, they may refer to Definition 2.3. Such inconsistencies in terminology arise multiple times, making the text difficult to read. Additionally, the phrase "relative to" in Definition 2.3 lacks clarity, and the three conditions listed are overly complex and challenging to interpret. The authors are encouraged to standardize their terminology definitions to enhance consistency and clarity.

2. Taking the GISB algorithm (Algorithm 1) as an example, the description of the algorithm is somewhat incomplete:

Step 3: It lacks specific details on the marginal and conditional independence tests, including the methods used for testing and the criteria for decision-making.

Step 4: It does not clarify how to select gene subsets along the path for conditioning or how to update the results.

Unclear Symbols and Variables: The symbol "I" is referred to as a "surrogate variable" in the algorithm but is labeled as a "perturbation indicator" in the proof. It would be beneficial to unify and clarify its meaning. Additionally, the variable introduced in Step 4 is not adequately explained beforehand.

3. The experiments do not include comparisons with methods developed after 2023. Given the rapid advancements in causal inference techniques, many recent algorithms are better equipped to handle nonlinear dependencies and selection bias. It is recommended to benchmark GISL against the latest methods, particularly those utilizing deep learning models for causal discovery, to further validate its effectiveness and novelty.

4. The experiments utilize a limited range of node counts (5 to 9 nodes). Expanding the study to include larger-scale networks would enhance the generalizability of the findings and further validate the applicability of GISL in more extensive networks.

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
3

### Summary
This paper proposes GISL, a causal discovery method in the presence of selection bias and latent confounders.
The method leverages perturbations to break the asymmetry and discover the direction of causality between variables.
It further proves the identifiability of the causal dependencies and selection processes considering the absence of latent confounders 
and ensures partial identifiability, which includes latent confounders.
Two variants of the methods GISB and GISL are evaluated empirically showing better performance over relevant baselines in synthetic scenarios.
In real gene expression data, GISL succeeds in learning the majority of known causal dependencies in between genes and selection processes.

### Strengths
The paper provides interesting and novel results. Among the contributions of the paper, I highlight the following strengths:
* GISL considers both selection bias and latent confounders and employs perturbations to discover the causal relations
* The discovered causal dependencies are guaranteed causal rather than spurious correlations.
* The authors provide theoretical guarantees for two scenarios, including one without latent confounders.
* Both variations GISB and GISL are evaluated empirically, validating the theoretical claims in practice.

### Weaknesses
The paper contains weaknesses in the writing, theory, and experiments.

**Writing.** The paper here requires improvement.

1. Some notions are not well introduced. For example, you should have explained in the background what is
identifiability/partial identifiability, faithfulness, and Markov condition.

2. The mathematical proofs are hard to follow. I recommend moving them to the technicalities in the appendix and instead bringing the corresponding figures in the main text.
Using the DAG figures you can explain the proof intuitively with examples.

3. Moreover, I have spotted mistakes in the grammar and syntax of the text:
* casual (ca-su-al) -> causal (in many places in the text)
* Line 119: Capitalize "We"
* Line 132: "The X =" -> "The data X ="
* Line 152: "In DAG, if" -> "In a DAG G, "
* Line 155: "If collider" -> "If the collider"
* Line 192: "1,3,5th lines" -> "lines 1, 3 and 5"
* Line 293: "If becomes all dependent patterns, keep it" -> I really don't understand what you write here, please fix it.
* Line 322: "IX → X → and IY → Y →" Maybe S missing in both arrows?

**Theory.** Regarding the theoretical results, Theorems 3.1, 4.1 do not quantify what "sufficiently many data" means. Moreover, it is unclear how you prove them by enumerating some possible causal configurations.
How are you sure that you have included all possibilities? Additionally, the number of required perturbations is not quantified.
Typically for biology experiments, each perturbation has cost, therefore a high number would not be efficient.

**Experiments.** The experiments provide validation for the theoretical claims but they lack in some aspects:
1. It is not determined how much data your method requires to perform reasonably.
What happens in the low data regime in comparison to the baselines?
2. You could have included a few more baselines like DCDI [1] and a method for gene regulatory networks [2].
3. Even though the result of the real experiment is valid, the DAG is very tiny (or did I miss something?).
There, you should have also compared against the baselines.

### Questions
* Line 155: Wouldn't this path create cycles? How is it possible?
* Line 190: What is $I$? I guess it is the surrogate. You should clearly define it and explain it.
* Line 348: Is it 30000 data in total for all 20 structures or for each of the 20? If it is for each then it is quite a large number of data.
* Line 366, "data to assist PC and GES in determining more edges": How do you implement this?
* In Table 1, only GISL is reported? Please mention which method is reported.

### Soundness
3

### Presentation
1

### Contribution
3

---

## Human Reviewer 4

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper studies the task of inferring gene regulatory networks from perturbation data. It focuses on the issue of latent confounding and selection bias. Specifically, as illustrated in Figure 1, the work attempts to argue that many causal dependencies in gene regulatory network may be spurious due to a selection bias, where the expression of one gene depends on the expression of another gene, and this may be discovered through symmetric effects under perturbations. The paper proposes an algorithm based on testing conditional-independencies for discovering the causal graph and “selection pairs”, which uses the PC algorithm to learn a DAG skeleton from observational data and then post-processes the skeleton to identify selection pairs via the perturbation data. An extension under latent confounding is also proposed. The work provides theoretical identifiability results for both settings that are surprisingly strong, showing that all “causal processes” are identifiable without parametric assumptions.

### Strengths
- The basic idea, which is illustrated in the toy examples (e.g. Fig 1), is very sensible. If a measurement bias exists, it can induce “spurious” causal dependencies that even hold under perturbations. I am not aware of prior work in the causal inference literature that discusses this
- The theoretical identifiability results (while not stated very formally, see below) are a strength of the work

### Weaknesses
 - The work does not adequately discuss prior work. There is no section in the paper that covers how this work fits into existing works, both in the causal inference literature and computational biology. It may be that no prior work studied this particular artefact of selection bias, but there are probably many related works that are worth discussing and putting into context.
- The work provides no convincing evidence or justification of the fact that selection bias is an issue in single cell transcriptomics. Which biological or measurement artefact could explain a selection bias of the form in Figure 1 in real-world experimental data? Simply because this synthetic example can induce symmetric perturbation effects does not imply that real-world gene regulatory networks really suffer from this issue. The reasoning in the experiments section (Section 5.2, line 490-499) is shaky. Hinting at differences in cell survival for different perturbations, based on prior data of other experimental studies, is not strong evidence that “selection bias” exists. The work uses z-scores from the DepMap study to show differences in growth rates of cells under different perturbations. However, this could simply be an artefact of the wet-lab experiment or the (causal) regulatory changes induced by a specific perturbation. Overall, while the toy idea makes sense, I don’t find it convincing that the toy idea selection bias is happening in real systems, and I think it requires a lot more justification.
- Motivating example (Figure 1): couldn’t this "artefact" or selection bias also be viewed as a causal mechanism? Given the selection threshold, the value of X affects the distribution of Y. While we may view this as selection bias, I don’t see why this could not also be seen as a “causal “dependency. In my eyes, if the distribution of Y changes if we perturb X, this is what one may reasonably define as what causation means. How else would we define causality?
- One of the key challenges in inferring gene regulatory networks from data is the high dimensionality. Like the vanilla PC algorithm, it seems unrealistic to expect a method based on conditional independence testing to scale to specifically the GRN inference problem in practice. Even though the PC algorithm is classical at this point, it is not widely used in computational biology. This is reflected in the experiments (Section 5), where all experiments are performed on less than 20 variables. Since this work focuses particularly on the application in biology, this is not a convincing algorithm for practical applications. 
- The Theorem statements are not rigorous. Theorems 3.1 and 4.1. are very vague descriptions. What is “partially identifiable”? (And what is not?) What are “causal processes”? What does it mean for the data to be “sufficient” or the sample to be “sufficiently large”? How much perturbational data is needed? From the theorems, it is not clear what is proven formally in terms of the formalisms in Section 2. Also, how do these results fit into the context of existing known identifiability results? Can it be seen as a general or special case of other results?
- The Appendix contains a lot of grammatical language errors and is thus hard to comprehend (e.g. Section F)

### Questions
-	Following the line of reasoning in the paper (e.g. following “Symmetry” in line 107), the work argues that causal dependencies are asymmetric, but selection biases are symmetric. I don’t agree with this claim because it assumes that gene regulatory networks are DAGs, which is known to be not hold in general in practice. If perturbing X affects Y and vice versa, this could be due to a feedback cycle between X and Y, and does not necessarily have to occur because of a selection bias.
-	What are “confusing dependencies” in GRNI? (line 117)? Simply because they are not in line with alternative experimental databases (like Enrichr) does not imply that a dependency is spurious. Lots of different circumstances could explain this.
-	What is the data-generating process underlying the causal model described in Section 2? Is it a Bayesian network? The graph alone is not sufficient to describe a distribution over X.
-	What is a “selection bias” formally? Is it that we discard samples if a criterion (an inequality constraint?) is not met, as in the toy example of the introduction? Section 2 views it more as an additional node in the graph. Overall, the notion of selection “bias” is not rigorously described, which makes it hard to understand the theoretical results.

### Soundness
2

### Presentation
1

### Contribution
1
