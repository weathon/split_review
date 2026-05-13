# Long-context Protein Language Model

- Decision: Reject
- Scores: 8, 3, 3, 3

## Abstract
Self-supervised training of language models (LMs) has seen great success for protein sequences in learning meaningful representations and for generative drug design. 
Most protein LMs are based on the Transformer architecture trained on individual proteins with short context lengths. Such protein LMs cannot extrapolate to longer proteins and protein complexes well. They also fail to account for the underlying biological mechanisms carried out by biomolecular interactions and dynamics i.e., proteins often interact with other proteins, molecules, and pathways in complex biological systems. 
In this work, we propose \themodel based on an alternative protein LM architecture, \themodels, built off selective structured state-space models, to learn high-quality universal protein representations at the amino acid token level using masked language modeling. We also introduce its graph-contextual variant, \themodelg, which contextualizes protein-protein interaction (PPI) graphs for a second stage of training. \themodel demonstrates favorable neural scaling laws, better length extrapolation capability, and a 7\% to 34\% improvement on protein downstream tasks than Transformer-based ESM-2. \themodelg further trained within the context of PPI graphs shows promising results on protein structure and function prediction tasks. Our study demonstrates the benefit of increasing the context size with computationally efficient LM architecture (e.g. structured state space models) in learning universal protein representations and incorporating molecular interaction context contained in biological graphs.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
The authors suggest protein language models, denoted as LC-PLM and LC-PLM-G, respectively.
LC-PLM is based on a Mamba-based architecture, which they call BiMamba-S.
Two main ideas of BiMamba-S are bidirectionality and shared projection layers for forward and flipped inputs.
Sharing of layers allows deeper layers, since the number of parameters is reduced.
The authors also suggest an extension for knowledge graphs, which leads to LC-PLM-G.
Graphs are represented as random walks between nodes, where nodes are protein sequences themselves and edges are indicated by an EDGE token.
They also use negative random walk samples, where there is no edge between nodes and mark it with a special NO_EDGE token.
The authors apply their methods/models to several downstream task and find superiority of their method over trained versions of ESM2.

### Strengths
- relevant topic
- good empirical results
- innovative idea how to integrate knowledge graphs into the models
- well-written paper

### Weaknesses
 - It would be interesting to see the performance of ProtMamba to be included in comparisons, where it makes sense.
- It would be interesting to additionally see the performance of Contact Prediction, Fluorescence and Stability on the TAPE tasks.
- Criterions for Table 1 should be better specified (e.g., when is a method considered to be universal?)
- line 101: here also "Hochreiter, S. (1991). Untersuchungen zu dynamischen neuronalen Netzen" should be cited.

### Questions
- Which context size do you use for ESM-2? Could it have been increased for the experiments you carried out (i.e., did ESM2 and LC-PLM use approximately the same memory?)?
- What hyperparameters did you use for ESM-2? How was hyperparameter selection done for ESM-2 and LC-PLM(-G)?
- RQ3:\
In contrast to some other experiments UniRef50 is used for training. Evaluation is at UniRef90. Why is this the case?
- line 462-464: "As shown in Figure 7, the embeddings from LC-PLM-G captures the graph topology much better than LC-PLM, which aligns with the community detection results."\
What is the criterion to see that LC-PLM-G captures the graph topology much better?
- line 439-440: "This also suggests that, even for average-length protein sequences, long-range dependencies would be useful information and an important feature for protein structure prediction."\
What is the exact indication to come to this conclusion?
- line 533: "LC-PLM achieved 7% to 34% better performance on various downstream tasks." Which task do you exactly mean with 7% and which with 34%?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
The authors present a protein model which is based on the Mamba backbone which runs in bidirectional mode with parameter sharing. The authors compare their method to ESM-2 for the pre-training data (UniRef90) and for downstream structure prediction tasks. For protein protein interaction tasks, the authors present a graph-based version of their model.

### Strengths
- The results indicate that the proposed model outperforms the ESM-2 baseline on both pretraining MLM objective and the downstream tasks.
- The authors perform experiments for a wide range of model sizes ranging from 130M parameters to 1400M parameters.

### Weaknesses
 - **Little novelty**: 
  * Protein modeling with Mamba based backbone architecture is done here [1]. Notably, in a sense [1] also allows for bidirectional information sharing by their fill-in-the-middle objective.
  * Bidirectional Mamba blocks with parameter sharing was already done here [2].

- **Lack of comparison**:
  * If the authors thought, their work is substantially different from [1], they have to compare to [1] and discuss benefits/differences.
  * For all experiments, e.g. ProteinGym experiment (Table 4), SOTA methods and their performances should be reported along with ESM-2 and LC-PLM-*.

- Figure 2: Mistake wrt the orientation of the third linear projection block.

### Questions
- Wrt the PPI section: It seems a bit counterintuitive to force the graph-structure like information into tokenized text only to be able to naively apply a language model to it. Why shouldn't it be possible to simply train a GNN on the given data?

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The paper presents LC-PLM, a protein language model based on a bidirectional selective structured state-space models with shared projection layers (BiMamba-S) for learning protein representations. Additionally, it introduces a graph-based variant, LC-PLM-G, incorporating protein-protein interaction (PPI) graphs for training and show learning paradigm with extended context beyond individual proteins. The authors claim that (1) LC-PLM demonstrates better length extrapolation capabilities and outperforms Transformer-based models like ESM-2 on various essential protein-related tasks; (2) LC-PLM-G shows promise in protein structure and function prediction tasks by integrating biological interaction contexts.

### Strengths
- The paper presents a range of experimental evaluations across downstream tasks, showing better performance compared to one standard Transformer-based protein language model ESM-2. The evaluation tasks are diverse and comprehensive.
- The introduction of LC-PLM-G, incorporating PPI graphs, is a novel direction for protein language models. Using relational information between proteins has potential for realistic applications where protein interactions play a crucial role.

### Weaknesses
 - The paper does not adequately justify the selective structured state-space (S4) models over existing Transformers-based PLMs (eg. ESM-2), which are widely adopted for protein sequence modeling. Protein sequence understanding does not usually face the same latency/bandwidth constraints as real-time LLM deployments such as ChatGPT, where SSMs could possibly bring more practical value with linear inference time. Without clear advantages or innovations in the application of SSMs, this choice lacks strong motivation to stand convincing.
- The paper assumes that longer context modeling is inherently beneficial for protein sequences. However, the biological need for extremely long contexts remains unclear in many protein-related applications, especially since functional motifs often reside within local regions of a protein rather than requiring entire sequence context. Without a clear biological or empirical rationale, the assumption that long contexts are “essential” for protein understanding is questionable to me.
- The authors highlight LC-PLM’s computational efficiency over Transformers due to the quadratic complexity of Transformers. However, given that training/inference-efficient Transformers exist (flash attention for example), the emphasis on efficiency without practical demand diminishes the paper’s significance.
- Across the evaluation tasks (yes i agree they are many), only ESM-2 is there for comparison while for many of the task ESM-2 (alone) is not the real state-of-the-art (SOTA). Note that there are many interesting works built based on the ESM-2 embeddings and give very promising SOTA results for function prediction or mutation effect modeling. I wonder how the LC-PLM embedding accommodate these existing model and perform better than ESM-2.



### Questions
- In RQ1, how do the authors hold out the test 250k sequence? Do the authors re-train the ESM2 for plotting the Figure 4? Moreover, in Figure 4/5, what is in specific the “Evaluation Loss” for the label of the y-axis (vertical direction)?
- When reporting folding evaluation, how do the structures obtained from ESM-2?  My concern is, for evaluation fairness, one should align the folding trunk while on the other hand, the distribution over the residue-level embeddings from (1) LC-PLM and (2) ESM-2 can be different  in the vector space. Please elaborate or point out some relevant context to address this question. 
- A related questions from above, i understand the folding (RQ4) task for the authors is just a “proof-of-concept” such that the authors adopt downsampling for the openfold training data. However, 1.5% of protein single chains can have large variance for the model to show enough performance bias. Could the authors test the robustness of this downsampling strategy and show error bar on it?
- Question regarding the results incorporating the protein-protein interaction PPI graph saying LC-PLM-G.  In specific, in table 3 of the two tasks from TAPE benchmark, the LC-PLM-G/ESM-2-G shows very similar results compared to their vanilla version (LC-PLM/ESM-2). The performance improvement margin seems to be within the reported std range and I do not see significant improvement of doing this; in table 4/ProteinGym benchmark, for ESM-2-G, the incorporating of PPI graph drastically hurt the performance on top of ESM-2 while the performance gap between LC-PLM-G/LC-PLM is also hard to tell. These results can weaken the “necessity” claim of the main motivation of this paper: modeling based on multiple sequence input (PPI in this case). Could the author further justify the benefit for inference with additional PPI graph? 

- Could the authors mentioned some concrete modeling examples with biological significance that we have to turn to Mamba because the attention/Transformer sucks or even fails to handle the problem at all? Can the authors provide further evidence that the extended context window length improves the “related” downstream protein tasks beyond the results presented? At present, it is still unclear to me why should I buy the idea of using S4/mamba instead of attention?

MISC:
- In figure 6, why using “value x 2^1” as the ticks? That looks a bit weird

### Soundness
2

### Presentation
2

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
The authors propose a method for masked-modeling of protein sequences with large context sizes.

### Strengths
- Generally important topic of modeling proteins
- Diverse, extensive and involved experiments done
- Good presentation of the material

### Weaknesses
 - Originality: This method already exists as ProtMamba [1]. ProtMamba also uses Mamba for protein modeling and introduces long context tasks. The authors should propose a new method to model protein sequences and long-contexts.

- Significance:
a) The significance of this work is also diminished by many false and tenuous claims. E.g. "Such protein LMs cannot extrapolate to longer proteins [..]": this is not true, and cannot and has not been shown theoretically nor empirically. Transformer-based pLMs can extrapolate to longer contexts and can also handle relatively long contexts (e.g. 16k context size). Also "they fail to account for the underlying biological mechanisms [...]" is just a tenuous claim without any evidence. The claim that"our work [...] learns universal AA token level presentation" also bears any evidence and any definition what "universal" means. The authors should remove all tenuous and false claim (not limited to the ones I mentioned) from the manuscript.

b) The approach with graph-contextual modeling is ad-hoc. It is unclear why proteins from a PPI graph should be relevant contexts for a particular protein at hand. The homology-criterion that is used by [1] is much better justified and the default approach to assemble long-contexts.

- Technical errors:
Comparisons with ProtMamba and Transformer based architectures are missing. It seems that the authors have only trained their own architecture in this work and not a single model based on another architecture. The authors should at least compare with ProtMamba, and with 1-2 Transformer-based architectures. Therefore, it also remains unclear from where the alleged performance gains arise: the increased context, the graph-style pre-trained, the architecture, or any other component.


Other flaws:
Table 1 and table 3: one digit too much is displayed.

### Questions
- Can you clearly state which models have been trained in this work and for which models you just took pretrained versions?

### Soundness
2

### Presentation
3

### Contribution
1
