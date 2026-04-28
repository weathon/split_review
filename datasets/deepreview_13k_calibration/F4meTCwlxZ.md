# Consistency Guaranteed Causal Graph Recovery with Large Language Models

- Decision: Reject
- Avg Score: 5.00
- Scores: 3, 5, 5, 6, 6

## Abstract
Causal graph recovery traditionally relies on statistical estimation of observable variables or individual knowledge, which suffer from data collection biases and knowledge limitations of individuals. Leveraging the broad knowledge in scientific corpus, we propose a novel method for causal graph recovery to deduce causal relationships with the large language models (LLMs) as a knowledge extractor. Our method extracts associational relationships among variables and further eliminates the inconsistent relationship to recover a causal graph using the constraint-based causal discovery methods. Comparing to other LLM-based methods that directly instruct LLMs to do highly complex causal reasoning, our method shows advantages on causal graph quality on benchmark datasets. More importantly, as causal graphs may evolve when new research results emerge, our method shows sensitivity to new evidence in the literature and can provide useful information to update causal graphs accordingly.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper introduces LLM Assisted Causal Recovery (LACR), a method for constructing causal graphs using large language models (LLMs) to extract relationships from scientific literature. Building causal graphs from literature is nothing new. The key innovation is a principled constraint-based approach (e.g., using d-seperation) to assemble the DAG from the "Conditional Associational Relationships" extracted from literature to build a causal graph that meets causal discovery principles.

The authors evaluate on the ASIA and SACHS against pure LLM and hybrid methods.

### Strengths
The main strength of the paper is the use of causal constraints to evaluate putative causal relationships extracted from text. Prior work has focused mostly on acyclicity constraints, I've never seen a method take constraints to this level of rigor.

### Weaknesses
The reliance on faithfulness seems a weakpoint, as faithfulness violations seem more likely when we're just talking about co-occurance in natural language text.

This seems extremely vulnerable to latent variables. There are constraint based approachs that could be used to deal with latents, such as Verma constraints, though good luck getting a natural langauge-based approach to enforcing those constraints. 

The evaluation used GPT-4o to reconstruct the SACHS and ASIA networks (also, I believe ASIA was invented as a toy model for causal discovery, which means it is directly discussed in detail in training data). GPT-4o has memorized these DAGs. See below ChatGPT output, I think Sachs is missing a few things (I recall a node called Akt that doesn't appear in my generated text) but GPT's result is close. The ASIA generation is spot on. In my view this invalidates the evaluation:

Here is verbatim from ChatGPT:

USER: * give me a causal DAG with edges from the SACHs network*

ChatGPT: The SACHS network is a causal graph representing protein signaling interactions in immune cells, with edges representing causal influences between proteins. Here’s a simplified version of the SACHS causal DAG structure:

PKC (Protein Kinase C) → RAF
PKC → PIP3 (Phosphatidylinositol (3,4,5)-trisphosphate)
PKC → JNK (c-Jun N-terminal Kinase)
PKC → ERK (Extracellular signal-Regulated Kinase)
PIP2 (Phosphatidylinositol 4,5-bisphosphate) → PIP3
RAF → MEK (Mitogen-activated protein kinase kinase)
MEK → ERK
JNK → c-Jun
ERK → ELK1
This simplified DAG captures some key causal dependencies in the SACHS network. If you need a graphical representation, I can create it with these edges as a visual diagram.

User: *Give me the edges in the ASIA causal DAG*

ChatGPT: The ASIA causal DAG is a well-known example in probabilistic reasoning, often used to illustrate Bayesian networks. It represents the relationships between variables related to a fictional medical diagnosis scenario. Here are the edges in the ASIA causal DAG:

Visit to Asia → Tuberculosis
Smoking → Lung Cancer
Smoking → Bronchitis
Tuberculosis → Tuberculosis or Cancer
Lung Cancer → Tuberculosis or Cancer
Tuberculosis or Cancer → X-ray
Bronchitis → Dyspnea
Tuberculosis or Cancer → Dyspnea
These edges show the dependencies among variables in the ASIA network, illustrating how visiting Asia, smoking, tuberculosis, lung cancer, and bronchitis influence symptoms like dyspnea and the likelihood of a positive X-ray result.

### Questions
Comment: Other reviewers might call out the complexity but complexity seems on par with constraint-based discovery algorithms.

In the intro, the authors posit their approach as a solution the bias in the data of causal discovery from numerical data. These seems like an unnecessary contrast, and indeed, natural langauge documents will also have bias (e.g., biases against negative results, biases torwards well-understood systems, etc.). Why not just treat causal graph building from text data as another modality for causal discovery?

LACR optimizes the CARs by removing the minimum number necessary to resolve inconsistencies. Does this induce path dependence in removing CARs?

The fact that Sachs and ASIA DAGs are memorized by GPT-4o is a big problem. Possible remedies:
1. Sachs is a signaling pathway. You can look through biomodels.org or Kegg to find alternative pathways, prompt the model to see if it can reconstruct with high accuracy.
2. Use a smaller opensource model, validate that it hasn't memorized the DAGs, and then use that model.
3. Create an artificial DAG in a science domain, create synthetic corpus based on that DAG.

Willing to upgrade score if this is addressed.

### Soundness
1

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
The paper presents a method for recovering causal graphs using LLMs by handling inconsistencies in the LLM's extracted relationships, with this task being formulated as a consistency maximization problem, analyzed theoretically with graph theory tools, and applied on two experimental datasets.

### Strengths
There are aspects of the paper I perceive to be strengths.

For example, the LLM prompting strategy seems efficient; the outlined theory is useful in that it helps readers quantify worst-case performance. 

The authors explore various evaluation metrics. 

The writing is overall clear (although there is some room for possible improvement, see below).

### Weaknesses
There are aspects of the paper I perceive to be possible weaknesses, or at least, areas with room for improvement. 

The theoretical results seem to be (close to) relatively standard applications of results from graph/approximation theory. Perhaps moer

Some of the algorithms as outlined don't seem to offer much by way of intuition. As with many papers in the DAG-recovery context, there are a number of moving pieces notationally. I would potentially define notation clearly at the head of the algorithms, along with inputs, outputs, and goal. If the associated algorithms run too long, consider moving to Appendix. 

One limitation of the evaluation metrics as outlined is that they weigh all edge mispredictions in the same way. In practice, some edge mispredictions in a causal graph may be more or less deleterious in practice. I can think of a few ways this may be overcome in practice. Perhaps the paper selects one relationship in the DAG is of primary scientific interest, and performs ATE estimation with the adjustment set applied by different recovered DAGs. Bias, Variance, and RMSE of the downstream causal estimator(s) could then be examined and could provide useful context for evaluating performance. 

Another challenge to contextualizing performance -- I don't seem to see much information for "baseline LLM 1" and "Baseline LLM 2". It is possible, therefore, that the performance gains in Table 1 are due to the specific way of LLM prompting, or the constraint maximization, or the way that majority voting was handled. 

Based on the prompting strategy, the "we first retrieve a fixed number of the most relvant scientific papers" seems to be doing a lot of work in the analysis. In general, the proposed method seems to rely on the presence of LLM prior-knowledge of research papers on a given subject. In that sense, the method, as far as understand it, would be difficult to apply in a generic scenario with unlabeled columns. This would imply that the method is much less broadly applicable than competing methods that just use features of statistical distributions of observed variables (I also don't seem to see a comparison with such direct methods). In practice, investigators may have access to papers and so forth; the method described here involves some extra effort to assembled a relevant paper corpus.

### Questions
I have some questions about the LLM comparison prompting methods (see above).

### Soundness
3

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
4

### Summary
The paper presents a novel way of developing a causal graph using LLMs, by doing retrieval-augmented generation with scientific documents. They also provide algorithms to resolve inconsistencies in the final causal graph. Experiments are done on two datasets to show the promise of the method.

### Strengths
* Good idea to include scientific documents in the prompt of LLM, to avoid solely relying on LLM's background knowledge
* Definition of the two kinds of inconsistencies that appear when merging graphs from different LLM calls
* Algorithmic abstraction of the key consistency challenges faced whenever aggregating inputs from (LLM/human) experts

### Weaknesses
 * Experiments are done only on two small datasets
* Some choices in the evaluation setup are not well-motivated 
* The chosen datasets are unable to show the real potential of the method. Even baselines do well on these datasets. See Table 1 where F1 is the highest for LLM1 baseline for Asia and the F1 is almost the same for LLM2 baseline in Sachs. Instead, it will be good to show experiments on non-memorized datasets (i.e., less popular datasets) where the gains may be higher.

### Questions
The formulation of the problem and the algorithmic abstraction are key contributions. I feel that the two algorithms for consistency and orienting direction can be generally useful, even if we are not using any retrieved documents. I have the following questions: 

1. The main limitation is that the experiments are not convincing. The choice of datasets is not well-motivated. Both datasets are small graphs and arguably heavily memorized. Choosing another dataset (more complex and less memorized), such as the neuropathic, alzheimers, arctic sea ice, or covid-19 (see kiciman et al. for these datasets) can provide a better motivation (and hopefully stronger results) for the method. 
2. Separately, while the main contribution is pitched as the retrieval of documents, I feel that the skeleton building and orienting algorithms are useful in their own right. Often, there are multiple (LLM) experts that may suggest slightly different graphs--would it make sense to do experiments to show that algorithms LACR1 and LACR2 can help any LLM-based method? 
3. How many LLM calls are needed to process a variable pair v1, v2? It is not clear from the paper. Is there a sequential process followed. Also, how big is each document? Is a scientific document chunked into paragraphs that is then inserted in the prompt? More details on LLM call time complexity will help. Relatedly, I would be curious to see an ablation where LACR1 and LACR2 are used on top of a baseline LLM algorithm (but without the documents). For example, you can run LLM-BFS with different seeds, or combine LLM-BFS with LLM-pairwise output (assuming that such a combination has similar number of LLM calls as the proposed method). It is difficult to parse whether the gains are due to the documents, or because of LACR1 and LACR2?
4. How are the "best" evaluation baselines decided in Table 1? No justification is provided and the choice seems arbitrary.
5. Why are the "best" baselines not evaluated for the new graphs? This seems unfair. If you are changing the ground-truth based on the output of your own method, at least evaluate the baselines on this new ground truth.
6. Are you assuming causal sufficiency? What if two variables can be d-separated but the separating variable is unobserved. Or if two variables have an unobserved confounder but the algorithm ends up creating an edge between them?

Minor:
There is a typo in the prompt in E.5.1. associtional

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper presents LACR (LLM-Assisted Causal Recovery) for causal graph discovery that leverages LLMs to extract causal relationships from the scientific literature. By combining LLM-driven knowledge retrieval via RAG with constraint-based causal discovery techniques, LACR refines causal graphs with recent literature, addressing data biases and inconsistencies often present in purely statistical methods. Tested on 2 benchmark datasets, the method demonstrates improved causal graph accuracy, showing potential for adaptive, knowledge-rich causal inference.

### Strengths
- LLM knowledge might be biased or limited, adding RAG for causal discovery mitigate some weaknesses in the LLMs.

- LACR addresses inconsistency issues in causal relationships using a constraint-based optimization approach, making causal graphs more reliable and less prone to noise from conflicting sources.

- The paper is fairly easy to follow with prompt templates mentioned in the Appendix.

- Novel setup to include RAGs to causal discovery.

### Weaknesses
 - There is a lack of comparison between statistical (such as PC, FCI, etc) and LLM methods. It would make the paper stronger to have the standard causal discovery evaluations. The paper was motivated against the use of standard methods, it seems like an obvious comparison to make in that case.

- The results have been presented on 2 highly popular datasets - Asia and Sachs. While it is not easy to find datasets that are not ingested by LLM, results on more domains/DAGs would be suggestive of its generalizability.

- It would be good to mention Limitations and Future Works.

- How would the performance be impacted when lesser capable models are used? Is it still better that standard causal discovery algorithms?

L 367 space needed.

### Questions
- It would be good to mention Limitations and Future Works.

- How would the performance be impacted when lesser capable models are used? Is it still better that standard causal discovery algorithms?

L 367 space needed.


----- 
POST REBUTTAL

Apologies for the delay.

I appreciate the authors running PC and other additional experiments. I would like to increase my score to 6. I would have given a higher score if the authors showed the effectiveness of the method with a smaller open source model. However, adding RAG to extract causal relations is still a contribution that will be appreciated by the community. Hence I am increasing the score.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 5

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper aims to recover causal graphs when numerical data is unavailable and individual knowledge is limited.

The main claim: LACR gives better causal graphs than directly instructing LLMs.

The proposed LACR method:
1. infer CARs from documents.
2. recover causal graphs with constraint-based methods.

### Strengths
1. An interesting pipeline to construct causal graphs from the scientific corpus.
2. Detailed formalization, analysis, and discussion.

### Weaknesses
 - The results are not complete. In Table 1, 19 blanks are specified as N/A. I fail to see any difficulty to produce these so-called N/A metrics since F1 score can be produced. Please provide the missing parts.
- The baseline methods used are not consistent. The two baseline methods in ASIA and SACHS are totally different. All four baselines should be fully evaluated in each dataset.
- The evaluation for phase 2 is unclear. In phase 1, two version of ground-truth are used for each metric, like F1 and F1(new). But for phase 2 it is not reported in the same way. Please provide the missing parts.
- The overall evaluation for the final DAG has not been reported. For example, accuracy, recall, F1, SHD, and SID metrics for the 3 variants + 4 baselines over the two used datasets.

### Questions
1. There are many important issues in experiments. See the weakness part. These issues make me very worried about the solidness and effectiveness of this paper. 
2. Did the authors conduct their own experiment to evaluate the baselines?
3. About motivation. Could you give me any example where scientific papers can be published without supporting numerical datasets? Please clarify the specific scenarios or fields where the method would be most applicable and valuable.


-----

**Post Rebuttal Comments**:

I acknowledge the author's rebuttal.

I have read the others' reviews and rebuttals, I agree that:
- Extracting independent constraints from textual data is interesting and novel. (from reviewer gpD3, 8Gvf)
- The method is useful for integrating the scientific consensus from the retrieved documents and deducing the need for novel datasets. (from reviewer NKix)

I have discussed the evaluation details with the authors.
- Most of the baselines do not have sufficient details to reproduce, as stated by the authors. 
- They compared the method with the best-reported numbers in the literature.
- They provided complete causal graphs produced using their method. 

This additional information has reasonably alleviated my concerns about the solidity of this paper. Although the current submission still has limitations like "more detailed experimental investigation of the impact of LLMs' capacity" and "reproduced version of baselines," I would like to update my score to 6 and recommend an acceptance.

### Soundness
2

### Presentation
2

### Contribution
2
