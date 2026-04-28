# Retrieval Augmented Zero-Shot Enzyme Generation for Specified Substrate

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
The ability to generate novel enzymes that catalyze specific target molecules is a critical advancement in biomaterial synthesis and chemical production. However, a significant challenge arises when no recorded enzymes exist for the target molecule, making it a zero-shot generation problem. This absence of known enzymes complicates the training of generative models tailored to the target substrate. To address this, we propose a retrieval-augmented generation method that leverages existing enzyme-substrate data to overcome the lack of direct examples. Since there is no recorded catalytic performance between the enzymes and the new target molecule, the challenge shifts to identifying enzymes that helpful for generation. Our approach tackles this by retrieving enzymes whose substrates exhibit structural similarities to the target molecule, thereby exploiting functional similarities reflected in the enzymes' catalytic capability. This leads to the next challenge: how to utilize the retrieved enzymes to generate a novel enzyme capable of catalyzing the target molecule, given that none of the retrieved enzymes directly catalyze it. To solve this, we employ a conditioned discrete diffusion model that takes the aligned retrieved enzymes to generate a new enzyme. We train the generator with guidance from an enzyme-substrate relationship classifier to make it output the optimal protein sequence distribution for different target molecule. We evaluate our model on enzyme design tasks involving a diverse set of real-world substrates, and our results including catalytic rate predictions, foldability assessments, and docking position analyses, demonstrate that our model outperforms existing protein generation methods for substrate-specified enzyme generation. Additionally, we formally define the zero-shot substrate-specified enzyme generation task and contribute a comprehensive dataset with evaluation methods.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces SENZ, a retrieval-augmented method for zero-shot enzyme design conditioned on a specific substrate. Overall, the paper is very well-written, impactful, and an interesting contribution to the field of *de novo* enzyme design.

### Strengths
* Very good review of prior work on protein design; given the page limit it is hard to be extremely thorough but I found it a good selection and well-structured.
* It is a nice contribution that the authors provide a substrate-enzyme relationship dataset as part of the work.
* Good details provided in the paper for the different methods used, from the dataset curation to the model training and evaluation.
* I liked the comparison to a diverse set of methods as it helps to understand the respective strengths SENZ.
* The paper is well-written and well-structured as a whole.

### Weaknesses
 * I think just minimizing the docking score or optimizing k_cat for a given substrate and designed protein are not by themselves good enough metrics to assess the designs. In lieu of experimental validation, I would suggest rediscovery tasks to see if SENZ can design a known enzyme that is not present in the training set (i.e., still treating it as a zero-shot generation problem, but having a known solution, for validation).
* It was not fully clear to me how SENZ sets itself apart from existing work in enzyme design. This could be made more clear. For reference, I work in moleular design, but I am not an expert in enzyme design and am not as familiar with the field, so some things may be obvious to you but they did not come across to me from reading the paper necessarily, and the respective advantages/limitations of SENZ could be made more explicit.
* No code made available, as far as I can tell. Without this, I cannot make the score higher than 5, so please let me know if I have simply missed it and I can update my score to a 6 (there are ways to make code available anonymously).
* Recommend to proofread the paper more carefully; minor grammatical mistakes here and there but nothing too distracting nor that made it impossible to understand the meaning, so I did not take off points for this. However, I wanted to point it out as in most cases they were mistakes that any grammar checker could catch with little time investment on behalf of the authors.

### Questions
* For the same substrate, how different are the proteins generated via the different benchmarked methods? Did the authors analyze this? This would be really interesting to see, both in terms of sequence and structural similarity.
* How do the authors handle potential post-translational modifications which could lead to improved/decreased enzyme activity relative to the reference enzyme?
* It seems to me that there is a lot of information that the authors are currently not using in generating potential new proteins via SENZ (e.g., just the substrate, but not information on the generated products, any intermediates/transition states, 2D structures, etc, where known). I would imagine in the zero-shot setting it is quite important to include as much information as possible; how are the authors planning to incorporate this in future work to improve data efficiency?
* What are the failure modes of SENZ?

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposes a zero-shot enzyme generation method. This approach includes two parts. First, it retrieves the enzymes according to the substrate similarity. Second, it generates novel enzymes by a classifier-guided conditional generative model, given the substrate and retrieved proteins as input.

### Strengths
Overall, this is a sound paper. The motivation is clear. The method is reasonable. Empirical results show the improvement of their method over several baselines in the zero-short settings.

### Weaknesses
(1) evaluation metrics

As shown in Table 2, the scores of generated enzymes are much higher than the ground truth in some cases. For example, the log10(k_cat) for ground truth is only 0.247 for Sepiapterin, while the generated enzyme could achieve 0.705. This significant difference raises concerns about the reliability of the evaluation metrics. It is unclear if the reported k_cat values are based on experimental measurements or computational predictions. If they are predictions, the accuracy of the prediction method itself needs to be carefully considered. Furthermore, the lack of error bars or confidence intervals on the reported k_cat values makes it difficult to assess the statistical significance of the observed differences.


(2) confusing annotations about probability and variables.

For example, in P5, line 268, the notation suggests that a probability $P$ is set equal to a variable $x$, which is conceptually unclear. The use of $P$ to denote probability is standard, but equating it to a variable $x$ without further explanation is confusing. Similarly, in Equations (11) and (14), there appears to be a conflation between the variable $x$ and probability expressions. The lack of clear distinction between the deterministic variable $x$ and the probabilistic variable $p$ makes the mathematical formulation difficult to follow. The authors should provide a more rigorous definition of these variables and their relationship.

### Questions
(1) As mentioned in the "weakness" part, could you explain why your score is much higher than the ground truth?
Additionally, is there a way to directly compare the generated enzymes to the ground truth?


(2) In the 4.4 section, do you re-train the model with 0 #Retrived or just apply this in the generation stage? This might be unfair because of the mismatch between training and testing. I have a similar question regarding the "with and without guidance" ablation study. Is this ablation also applied in training?

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
The paper addresses the challenge of zero-shot enzyme generation tailored for specific target substrates. It introduces a substrate-specified enzyme generator that retrieves enzymes with structurally similar substrates to the target molecule and employs a discrete diffusion model to generate new enzyme sequences guided by a classifier. Experiments reveal that SENZ outperforms current enzyme generation approaches across metrics including catalytic activity and structural stability. Additionally, SENZ contributes a dataset for substrate-specified enzyme generation.

### Strengths
1. The paper proposes a zero-shot enzyme design task using a retrieval-augmented method. Given that the retrieved enzymes cannot directly catalyze the target substrate, the retrieval results are used to guide the generation of novel enzyme that can catalyze the target substrate.
2. The model demonstrated higher performance in generating enzymes with high catalytic activity than the baseline model.
3. The model additionally trained a discriminator to guide the generator. Experimental results showed that with the guidance of the discriminator, the model can generate enzymes with higher catalytic activity.

### Weaknesses
1. The model's foundation lacks innovation, as it uses the existing method EvodiffMSA-OADM. The model only considers the sequence level without extending to the structural level.
2. The selection of the baselines should be improved, e.g., the protein language models for unconditional generation and sequence generation models are relatively outdated. Moreover, the details of the baseline are not explained in the paper.
3. In the catalytic activity evaluation, seven specific tasks were included, but the reasons for their selection were not provided. Furthermore, the results are inconsistent, in some cases, the unconditional generation results outperform the conditional generation results.
4. The model's foldability and catalytic performance of sequences should be further analyzed and balanced, as a decrease in foldability may hinder the successful design of proteins in the wet lab.
5. The paper does not include a reproducibility statement.

### Questions
1. Can you explain how the model generates enzyme sequences in extreme cases such as when there are no retrieval results, and how to ensure the quality of the generation?
2. During the model’s sampling phase, how to align the retrieval results to target generation? If all retrieval results are aligned with the first retrieval result, could this potentially introduce errors?
3. Could you explain the details of how you modified the NOS in the baselines?
4. For the other questions, please refer to the weaknesses section.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
This paper combines retrieval method and a discrete diffusion model to achieve zero-shot enzyme design. Specifically, first, the authors retrieve possible functional enzyme sequences according to the substrate similarity by the Tanimoto similarity. Then the authors apply a discrete diffusion model enhanced based on the MSA transformer, with the retrieved enzyme sequences being MSAs. The  authors also curated an enzyme-substrate pair dataset to validate their model.

### Strengths
The contributions are listed as follows:

1. The paper is well-written and easy to follow!

2. The idea of applying diffusion MSA transformer to design functional enzymes is interesting and doable! Modeling MSAs into diffusion models will definitely improve the design accuracy while keeping the design diversity and novelty at the same time.

### Weaknesses
The weaknesses are listed as follows:

1. The application scenario of the proposed method is a little unclear to me! If the target enzyme is a natural enzyme, we can always find the EC class in Brenda and the corresponding records in PDB and Uniprot. Then using a supervised method will definitely be better than zero-shot inference. If the target enzyme is a non-natural enzyme, I don't think the proposed retrieval method could find relative enzymes in the database just according to the substrate similarity cuz non-natural enzymes usually have their special properties. Furthermore, the definition of 'non-natural' enzyme is not clear. Does it refer to enzymes with novel catalytic mechanisms, or simply enzymes that do not exist in current databases? The lack of clarity on this point makes it difficult to assess the practical utility of the method.

2. Some experimental settings and results are not reasonable or unclear to me:

(1) For the baseline model ProGen2 and ProtGPT2, as they are unconditional models, how did them realize controllable enzyme design cuz they are just following autoregressive generation? If the authors just use random generation, then I don't think the comparison is fair. To achieve controllable design, why not use ProGen? There are several available models of ProGen2, which size is utilized? The pLDDT of ProGen2 is too low, why is that? It is unclear how these models were adapted for the enzyme design task, given their unconditional nature. The lack of fine-tuning or specific adaptation for enzyme design raises concerns about the validity of the comparison.

(2) The pLDDT of all models are pretty low. For AF2, pLDDT 80 indicates stable design, I know ESMFold usually achieves a little bit lower pLDDT. But in Figure 2(b), none of the cases achieve a pLDDT higher than 80, indicating the proposed model cannot design foldable enzymes. The lack of high-confidence structure predictions raises serious concerns about the practical applicability of the designed enzymes. The low pLDDT values suggest that the generated sequences may not fold into stable, functional structures.

(3) In Table 3, the novelty should be evaluated through BLASTp in Uniprot instead of just Swiss-Prot. The use of Swiss-Prot alone is insufficient to establish novelty, as it is a curated subset of Uniprot. A comprehensive novelty analysis requires comparison against the entire Uniprot database.

3. For the guidance training method, how to guarantee a scoring function can be used to score enzyme-substrate pairs that it never sees during training? It's hard for me to trust it. The generalization capability of the scoring function is not adequately justified. The paper needs to provide more evidence that the scoring function can accurately evaluate novel enzyme-substrate pairs.

### Questions
1. In data construction, the authors said "we select the least common reactant among all reactants in the database". What is the definition of "the least common reactant"?

2. What is the accuracy of the scoring function in guided training?

3. Can the author clearly state the inference process of all baseline models?

4. For the success rate, what is the definition of "successfully generated sequences"? To me, it should both satisfy function constraint and structural stability. It seems all the designed enzymes didn't pass structural selection.

### Soundness
2

### Presentation
4

### Contribution
2
