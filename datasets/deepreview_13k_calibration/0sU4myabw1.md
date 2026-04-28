# RapidDock: Unlocking Proteome-scale Molecular Docking

- Decision: Reject
- Avg Score: 4.25
- Scores: 6, 3, 5, 3

## Abstract
Accelerating \emph{molecular docking} -- the process of predicting how molecules bind to protein targets -- could boost small-molecule drug discovery and revolutionize medicine. Unfortunately, current molecular docking tools are too slow to screen potential drugs against all relevant proteins, which often results in missed drug candidates or unexpected side effects occurring in clinical trials.
To address this gap, we introduce \method{}, an efficient transformer-based model for blind molecular docking.
\method{} achieves at least a $100 \times$ speed advantage over existing methods without compromising accuracy.
On the Posebusters and DockGen benchmarks, our method achieves $52.1\%$ and $44.0\%$ success rates ($\text{RMSD}<$2$ \si{\angstrom}$), respectively. 
The average inference time is $0.04$ seconds on a single GPU, highlighting \method{}'s potential for large-scale docking studies.
We examine the key features of \method{} that enable leveraging the transformer architecture for molecular docking, including the use of relative distance embeddings of $3$D structures in attention matrices, pre-training on protein folding, and a custom loss function invariant to molecular symmetries.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The authors tackle the problem of proteome-scale docking, the goal of which is predicting the binding pose of a ligand against many thousands of proteins. To do this, they develop an equivariant Transformer model (RapidDock) for dramatically accelerating docking compared to previous diffusion or GNN-based approaches. The model takes various features from the protein and ligand as input, and outputs a prediction of the binding pose of the ligand. The results show that RapidDock achieves 100x faster runtimes than three competing deep learning methods, while retaining equivalent accuracy (except to AlphaFold 3, which is much slower but has much better accuracy).

### Strengths
* Clear presentation of methods and results.
* Novel application of transformer architecture to docking, which results in much faster inference.
* Reasonable design choices in model. These include the addition of features for ligand atom charges and the use of a pre-trained protein language model. The scaling of the attention vector based on distance also seems well-motivated.
* Strong results on two distinct datasets, achieving a better success rate than two competitive deep learning methods at a fraction of the cost. While RapidDock has significantly worse accuracy on Posebusters compared to AlphaFold 3, I do not think this is a negative, because as the authors note AlphaFold 3’s speed is not suitable for large-scale docking. Additionally, my understanding is that AlphaFold-3 performs energy minimization as a post-processing step, which would give it an unfair advantage compared to RapidDock.
* Ablations of various model components help show the benefits of each design choice.

### Weaknesses
 * Motivation behind the problem setting is unclear. The authors address proteome-scale docking because any protein in the human proteome could be a potential *off-target* (a term of art that should probably be included in the paper) of a drug. Thus, docking against all proteins and then predicting affinity in a downstream task would detect these potential off-targets before they are discovered in later preclinical or clinical testing. However, I am not convinced that docking to each protein in the proteome is necessary to detect off-target effects. Pharmacologists often screen a drug against a limited number of safety-relevant proteins (in the hundreds), such as G-protein coupled receptors or ion channels, that are frequent off-targets [1, 2]. This is usually sufficient to detect many clinical issues beforehand, and it is not obvious that just considering more potential off-targets would further reduce the rate of adverse effects occurring (which for example may be due to more complex issues, such as toxicity of metabolic products or on-target unwanted effects). Could the authors provide a better argument for why it is important to screen a drug against all potential protein targets?
[1] Bendels et al. “Safety screening in early drug discovery: An optimized assay panel.“ J Pharmacol Toxicol Methods 2019.
[2] Peters et al. “Can we discover pharmacological promiscuity early in the drug discovery process?” Drug Discovery Today 2012.

* Limited baseline comparisons. I think the most important baseline to include would be AutoDock Vina (or another similar docking program). Despite not being deep learning-based, Vina is relatively fast and the current state-of-the-art in applied fields. Practitioners conducting large-scale docking would likely use Vina, so including results on this baseline is important. An additional deep-learning based docking model, such as TANKBind, would also improve the strength of the results, but it is not as critical.

* Some of the design choices are not well-explained. For example, it is not clear to me why discretized charge embeddings are used for the ligand atoms instead of simply providing the charge scalar as an input. It is also not clear what role the distance bias matrices play.

### Questions
* Is there a better way to determine which atoms are rigid and which are flexible? For example, AutoDock Vina determines if bonds are rotatable using a simple chemical definition, which dictates which atoms are flexible and which are not. Just searching through a lot of generated conformations seems like it might miss bonds that only rotate when exposed to external charges.
* Is this model potentially applicable to *target fishing*? Target fishing is the process of taking an existing drug compound and evaluating it against a large number of potential proteins to see if it can target them. This can be applied for drug repurposing, which is the use of currently approved drugs against new indications based on previously unknown binding against a new protein. This is potentially a strong application of the proposed method, but I do not see it explicitly mentioned in the paper anywhere.

### Soundness
3

### Presentation
4

### Contribution
2

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
3

### Summary
This work proposed a fast and reliable prediction method, RapidDock, for protein-ligand binding poses. Most previous methods employed in this work as base-lines used diffusion models, leading to large computational costs. However, RapidDock is based on a transformer and so much faster than the base-line models. The benchmark studies on PoseBusters and DockGen show that RapidDock is not only fast but also far more accurate than others except AlphaFold3. While the performance of the proposed method seems competitive, there are several issues that need to be addressed.

### Strengths
1. This work shows the possibility of transformer-based approaches for binding structure predictions, while most previous works are based on diffusion methods.
2. The proposed method outperformed the popular base-line, DiffDock-L, in the two benchmark studies, while its computational time for predictions is much faster than those of all base-line models.

### Weaknesses
1. The proposed method needs to generate 96 molecular conformations for each molecule and analyze the conformers to obtain its distance matrix. This conformational search, while potentially parallelizable, introduces a significant computational overhead that is not fully accounted for in the reported timings. The impact of this pre-processing step on the overall efficiency should be more thoroughly investigated, especially for larger molecules with more degrees of freedom where conformational sampling becomes more challenging.
2. The experiment in Section 4.2, which uses holostructures for predicting binding poses, is indeed problematic. It evaluates the accuracy of predicted distances within a known complex, rather than assessing the method's ability to predict novel binding poses. This approach does not validate the method's utility in real-world scenarios where the binding pose is unknown and must be predicted de novo.
3. The title and introduction emphasize the importance of proteome-wide docking, yet the work lacks any substantial results demonstrating the method's performance in this context. The current results are limited to benchmark datasets, which do not fully capture the complexities of proteome-wide docking. The absence of meaningful analysis in this area undermines the claims made in the introduction.
4. Technical details of the proposed method are insufficient, particularly regarding the reconstruction of ligand location from predicted distances. The process of converting predicted distances into a 3D structure is not clearly explained, and it is unclear whether any post-processing or optimization steps are required to obtain a valid pose. This lack of clarity makes it difficult to assess the robustness and reliability of the method.

### Questions
1. DiffDock-L (also AlphaFold3 and NeuralPLexer) is a generative approach, so it gives multiple binding poses according to their probabilities. Therefore, its prediction accuracy can be improved by including multiple different poses (Top-n poses) in the evaluation. However, RapidDock is deterministic, so it gives only a single output. It is understood that the authors want to emphasize computational speeds, but it seems they also need to discuss the accuracy aspects for a fair comparison.
2. Since RapidDock requires conformation searches for each molecule before docking, the authors need to clarify whether the reported computational times include the time for conformer searches or not. 
3. The proposed method has been compared with AlphaFold3 and NeuralPLexer. However, the former performs a rigid docking, whereas the latter predicts binding poses only from protein sequences and molecular graphs. Therefore, the prediction complexity of RapidDock is much lower than that of the baseline models, so the direct comparison between them is less meaningful.  The authors need to clarify this fact in the introduction or result sections. The current form may cause undesirable confusion to potential readers.
4. In the reconstruction of ligand location, predicted distances between ligands and also between ligand-protein may not precisely match with the coordinates of a single pose. If this is the case, the authors should elaborate more details about this process. Does it require a kind of post-processing?
5. The authors greatly emphasize the importance of proteome-wide docking, but this work does not provide any meaningful analysis except the computational time, which can be readily estimated without performing the actual calculations. The authors may add an additional study verifying that the proposed method can indeed provide meaningful results from the proteome-wide docking. Otherwise, they need to tone down their argument from the title and introduction parts. 
6. Appendix A.6 shows the examples of 3D structures predicted by RapidDock and AlphaFold3. The authors deliberately selected specific examples where RapidDock outperformed AlphaFold3, while they admit that the latter is far better than the former on average. AlphaFold3 even predicted those structures from the sequence-level information. These examples may lead to misunderstanding that RapidDock works better than AlphaFold3. The authors need to provide examples where RapidDock fails while AlphaFold3 succeeds.

### Soundness
1

### Presentation
1

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
In this paper, the authors introduce RapidDock, a new approach to molecular docking that leverages a Transformer model. The method includes both ligand atom embeddings and ligand charge embeddings. Protein representations are generated using embeddings from protein amino acids, the ESM-2 PLM, and calculated distance metrics. Instead of deep learning, RDKit-based methods such as MMFF and EDKG, construct the rigid distance matrix for molecules. Trained on the PDBBind and BindingMOAD datasets, RapidDock outperforms DiffDock and other open-source methods on the PoseBuster benchmark in % of ligands in RMSD < 2 Å metric, delivering at least a 100x increase in inference speed.

### Strengths
- The authors demonstrate the need for a faster model by outlining the scalability limitations of previous deep learning models.
- Aligned with their motivation, RapidDock shows the ability to perform conformation sampling for molecular docking in GPU inference runtime in approximately one-hundredth of a second per protein-ligand pair.
- In benchmarking with PoseBuster, RapidDock achieves the best performance among open-source codes (noting that AlphaFold 3 is not open source), particularly in the percentage of ligands achieving RMSD < 2 Å.
- The paper provides a clear explanation of how ligand and protein modalities are utilized and fed into the Transformer model.
- For constructing the ligand distance matrix, the authors use a hybrid approach, incorporating physics-based methods from RDKit, such as MMFF and EDKG.
- Additionally, the inclusion of ligand charge embeddings represents another hybrid approach in the model.
- For protein embeddings, the authors showcase the effectiveness of using not only pre-trained models but also their custom-trained ESM-2 models.
- The Transformer architecture employs a non-autoregressive approach with a full attention mask, introducing a new method for molecular docking by incorporating an attention scaler within the attention mechanism.
- The training hyperparameters are shared in detail through comprehensive tables.

**Originality:** RapidDock introduces a unique approach to molecular docking, particularly in terms of preprocessing compared to other DL-based methods. The detailed steps in the ligand and protein embedding process highlight its originality, which the authors further validate through an ablation study.

**Significance:** From a large-scale proteomic perspective, RapidDock is highly scalable and significantly faster in runtime compared to other DL-based and search-based molecular docking methods.

### Weaknesses
 - The code is not shared.
- Although the method section claims equivariance, it lacks sufficient explanation on this aspect.
- The rationale for using ligand atom charges is not adequately clarified.
- It is unclear why non-fixed distances in the molecule's rigid distance matrix are assigned a value of -1. Specifically, the implications of this choice on the model's ability to learn accurate distance relationships are not discussed. The use of -1, while distinct, could potentially introduce biases or hinder the model's learning process, especially given that distances are inherently positive values.
- The annotations for distance bias matrices are insufficiently explained; the annotations appear to be included simply because they work, without detailing why they are effective. The paper lacks a mechanistic explanation of how these biases interact with the attention mechanism to improve docking performance. For example, the specific mathematical form of the bias and its impact on the attention weights should be elaborated.
- Similarly, the rationale behind RapidDock’s use of attention and charge embeddings, along with their annotations, is not fully addressed. The paper does not provide sufficient justification for why these specific choices were made over other possible alternatives. A comparative analysis or ablation study of different attention mechanisms and embedding strategies would be beneficial.
- The splitting strategy for the training, validation, and test sets is not sufficiently described. The paper should include details on how the data was partitioned, ensuring no data leakage between sets, and justify the chosen split ratio. This is crucial for the reproducibility and reliability of the results.
- The parameter comparison in benchmarking does not seem fair; DiffDock results are compared with 30 million parameters, while RapidDock has 60 million parameters. The paper should include a more detailed analysis of the parameter efficiency of the model, perhaps by comparing performance with models of similar parameter size or by conducting an ablation study on the number of parameters.
- The RMSD metric, commonly used in molecular docking and Structure-Based Drug Design (SBDD), does not always yield bioactively, physically, or chemically plausible structures, as shown by Posebuster[1], PoseCheck[2], PoseBech[3], and CompassDock[4]. Including these metrics in the benchmark would strengthen the study. The paper should incorporate additional metrics that assess the quality of the generated poses beyond RMSD, such as those that evaluate the chemical plausibility and physical validity of the docked structures.
- Appendix A.6 lacks a comparison between DiffDock and NeuralPLexer examples. A more comprehensive comparison, including visual examples of the generated poses, would help to better understand the strengths and weaknesses of RapidDock compared to other methods.
- The extent of ligand filtering during ligand preparation is not sufficiently discussed. The paper should detail the criteria used for filtering ligands, including the specific properties and thresholds applied. This is important for understanding the scope and limitations of the method.

**Quality:** Although the authors claim this is the first use of a Transformer-based model in blind docking, ETDock[5] and FeatureDock[6] have previously used Transformers for molecular docking; however, these methods are not mentioned in the paper. Additionally, the benchmarking is limited to comparisons with only a few popular methods. In the conclusion, the authors state that: 

>"... the model demonstrates a strong understanding of the physicochemical principles behind forming biological structures," 

yet no bioactivity or physicochemical analyses, as discussed earlier, have been conducted to support this claim.

**Clarity:** The paper contains numerous grammatical errors that detract from readability and should be carefully revised. Placing the Related Work section after the Experiments section disrupts the flow, and the method annotations are not clearly explained.

**Reproducibility:** As the code is not shared, it is currently impossible to test whether it performs as reported. If the code were provided, I would be able to review, test, and reassess my evaluation (including scoring and comments) accordingly.

### Questions
- When comparing runtime in inference mode, did you preprocess the protein, or was the comparison done solely for molecule conformation?
- Did you use the same time-splitting approach as previous methods, such as DiffDock and NeuralPlexer, for the dataset?
- In the statement, 
> "Only the fixed distances across the molecule’s possible conformations are recorded, and others are denoted by a special value of −1," 

  Could you clarify why you selected -1 as the special value?
- In the RapidDock attention section, you state, 
> "First, we multiply the attention scores corresponding to input pairs with known distances (i.e., ligand-ligand within a rigid part and protein-protein) by a learnable scalar $s_m$, one for each layer $m$." 
  
  Did you also apply this to protein-ligand pairs? If not, could you explain why?
- For inference, do you generate one conformation per runtime for each protein-ligand pair?

### Soundness
3

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
3

### Summary
The paper introduces RapidDock, a fast and accurate transformer-based model for the
blind-docking task. The model predicts interatomic distances. Afterwards, the docked
pose is reconstructed with the L-BFGS algorithm. The authors report a 100x speed-up while
simultaneously improving over commonly used deep learning-based docking models in the
PoseBusters and DockGen datasets. The authors make first experiments at human
proteome-scale docking.

### Strengths
RapidDock is fast and accurate, allowing it to tackle human proteome-scale docking studies. The reported speed could enable its use as an oracle function for other DD-related tasks in future work. Ablations on PoseBusters and Dockgen show promising results. The
paper is well written and gives a lot of insights into the modelling and training

### Weaknesses
While the method shows good results on a task relevant to computational biology, there is not enough novelty on the ML side that justifies acceptance as a main track contribution. The authors use a standard transformer embedding the ligand and proteins with ESM2 and
 employ cross-attention to the distance matrix. I encourage submission to a domain-specific journal.

While the method shows good results on a task relevant to computational biology, there is not enough novelty on the ML side that justifies acceptance as a main track contribution. The authors use a standard transformer embedding the ligand and proteins with ESM2 and
 employ cross-attention to the distance matrix. I encourage submission to a domain-specific journal.

Wording:
L. 30 “ … will revolutionize medicine” is an unsupported statement, please reformulate. It would be better to focus on the obstacles that need to be overcome and how you tackle those (like in
your paragraph 2, L. 34 X.).
In l.113f. the authors claim equivariance, however they work with interatomic distances only, making your model invariant.
Permutation loss citation is wrong (e.g. l. 228), cite original paper (Zhu et al. 2022 Direct molecular conformation generation)
In my opinion, l.419f. “the model demonstrates a strong understanding of the physicochemical principles” is a big stretch - how is this supported in your work? Accurate and fast prediction of ligand poses in proteins doesn’t mean that the model understands the physicochemical principles that lead to those poses, and it is debatable whether this is even needed.
Open questions:
Since the prediction time is critical to the paper's claims, I would like to see how much time you spend at inference on average in a) pre-processing, b) prediction, c) reconstruction and d) any form of post-processing.

In l.162f., what is the reasoning for choosing 257 buckets? Are there ablations on higher/lower resolution? How does this affect the performance-inference time tradeoffs? Same questions for the charge embeddings.

### Questions
Wording:
L. 30 “ … will revolutionize medicine” is an unsupported statement, please reformulate. It would be better to focus on the obstacles that need to be overcome and how you tackle those (like in
your paragraph 2, L. 34 X.).
In l.113f. the authors claim equivariance, however they work with interatomic distances only, making your model invariant.
Permutation loss citation is wrong (e.g. l. 228), cite original paper (Zhu et al. 2022 Direct molecular conformation generation) 
In my opinion, l.419f. “the model demonstrates a strong understanding of the physicochemical principles” is a big stretch - how is this supported in your work? Accurate and fast prediction of ligand poses in proteins doesn’t mean that the model understands the physicochemical principles that lead to those poses, and it is debatable whether this is even needed.
Open questions:
Since the prediction time is critical to the paper's claims, I would like to see how much time you spend at inference on average in a) pre-processing, b) prediction, c) reconstruction and d) any form of post-processing.

In l.162f., what is the reasoning for choosing 257 buckets? Are there ablations on higher/lower resolution? How does this affect the performance-inference time tradeoffs? Same questions for the charge embeddings.

### Soundness
3

### Presentation
3

### Contribution
2
