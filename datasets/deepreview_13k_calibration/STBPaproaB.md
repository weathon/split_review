# MARS: A neurosymbolic approach for interpretable drug discovery

- Decision: Reject
- Avg Score: 5.50
- Scores: 5, 6, 6, 5

## Abstract
Neurosymbolic (NeSy) artificial intelligence describes the combination of logic or rule-based techniques with neural networks. Compared to neural approaches, NeSy methods often possess enhanced interpretability, which is particularly promising for biomedical applications like drug discovery. However, since interpretability is broadly defined, there are no clear guidelines for assessing the biological plausibility of model interpretations. To assess interpretability in the context of drug discovery, we devise a novel prediction task, called drug mechanism-of-action (MoA) deconvolution, with an associated, tailored knowledge graph (KG), \textit{MoA-net}. We then develop the \textit{MoA Retrieval System (MARS)}, a NeSy approach for drug discovery which leverages logical rules with \textit{learned} rule weights. Using this interpretable feature alongside domain knowledge, we find that MARS and other NeSy approaches on KGs are susceptible to reasoning shortcuts, in which the prediction of true labels is driven by ``degree-bias'' rather than the domain-based rules. Subsequently, we demonstrate ways to identify and mitigate this. Thereafter, MARS achieves performance on par with current state-of-the-art models while producing model interpretations aligned with known MoAs.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
5

### Summary
*November 26: after first response, the "Presentation" score has been raised from 2 to 3*

This work proposes a new neurosymbolic (NeSy) model for drug discovery as well as an associated dataset, where the problem is cast as a prediction task for drug-biological process (BP) pairs. More specifically, biochemical knowledge is arranged into a knowledge graph (KG) where entities (vertices) such as drugs, proteins and BP are connected with each other via directed edges. By using a new update rule of edge weights, the new model was able to avoid reasoning shortcuts inherent in previous methods.

### Strengths
- Using the $ P_{2H} $ update rule, the new method has been shown, via a series of ablation studies, to avoid reasoning shortcuts due to degree bias.

### Weaknesses
 - The novelty of the manuscript appears to be limited:
    - The new dataset has fewer kinds of entities than PoLo, and in particular does not appears to include those relevant for therapeutics such as "disease" or "side effect".
    - Similarly, one would expect more kinds of entities beyond a generic "protein" (e.g. receptor, transcription factor, enzyme etc.).
    - Another issue is that all metapaths are chains, like $ \mathrm{interacts}(P_{k}, P_{k + 1}) $, whereas in real-world applications there are many instance of multi-protein complexes for biological functions.
    - The model reward function is almost the same as PoLo (Equation 4): $$ R(S_{L + 1}) = 1_{ e_{L + 1} = e_d  }  + b \lambda  \sum\limits_{i = 1}^{m} s(M_i) 1_{\tilde{P} = M_i} $$ In fact, that paper states that the hyparameter $ b $ can be "set to $ 1_{e_{L + 1} = e_d} $" (p. 382).
- The presentation of the manuscript is not as efficacious as one would hope:
    - Key concepts such as "deconvolution" or $ \land $ (presumably conjunction?) were not defined.
    - The 2-hop probability update ($ \S $A.4 and Alg. 1), which is the major novelty in the manuscript, should be in the main text.
    - The main predictive task was not explicitly formulated: from Figure 1A it appears to be link prediction.
    - Moreover, it would be useful to have the catalogue of different entities--entities interaction types (Figure 1B) in a table.
    - The background colour of Figure 1B makes it harder to read, plus the font sizes for the labels are a bit too small.
    - The citation for PoLo should use the published version (https://link.springer.com/chapter/10.1007/978-3-030-77385-4_22)

### Questions
- Could you include more training details e.g. hardware, training time, validation loss plots etc.?
- On what basis were the "feasible" MoA's chosen in Table A1?
- When comparing with PoLo, which rewards function(s) were used?

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
3

### Summary
The paper proposed a systematic framework for interpretable drug discovery. The model comprises of drug mechanism-of-action (MoA) deconvolution; MoA-net and its variants, a specifically designed knowledge graph based on public biomedical data; MARS, a Neural Symbolic approach with through dynamic rule-weight updates. The work provides enhanced interpretability and strong predictive performances compared to other baselines.

### Strengths
The paper is generally well-written and easy to follow. The objectives of the proposed framework clearly outlined and the model effectively handles several specific problems that other comparable methods hold. The proposed method shows competitive performances and provides a reasonable form of interpretability using knowledge graphs.

### Weaknesses
- The overview of MARS is unclear, and a figure delineating process would be helpful for reader's understanding. This should include the input-output pairs for the proposed model. It is not clear how the knowledge graph is traversed, and how the dynamic rule-weight updates are performed in practice. A more detailed description of the algorithm, including the specific steps involved in rule generation and weight update, would be beneficial.
- It is difficult to interpret Figure 3, as the main body does not explain anything about the confidences. The term 'confidence' is vague and needs to be defined in the context of the model. It is unclear how these confidences are derived and what they represent in terms of the model's predictions. For example, are they probabilities, scores, or some other measure? A more precise explanation is needed.
- While the paper proposes the term "drug-discovery", the it unclear in how to find  "novel drugs or chemical compounds". Given that the model is trained on the full data (no test) it could provide some meaningful results. The paper should clarify how the model can be used to identify novel drug candidates, given that it is trained on existing drug-target interactions. The distinction between predicting known interactions and discovering new ones is not clear. The paper should also address the issue of validation for these novel predictions.
- The computation cost in training the model could provide valuable insights. The computational complexity of the model, including training time and memory requirements, should be discussed. This is important for assessing the scalability and practicality of the proposed approach. The paper should also discuss the hardware requirements for training the model.
- The term "enhanced interpretability" is difficult to understand. An example for the term (possibly from the data that the authors used) would help better understanding of the term, and the strength of the model. The paper should provide a concrete example of how the model's interpretability can be used to gain insights into drug mechanisms. It is not clear how the learned rule weights translate into a mechanistic understanding of drug action.

### Questions
- What is the computation time of training the network? How susceptible is the model with inclusion of new data?
- What is the "confidence" in figure 3?
- What is the exact neural network architecture for MARS? What is a simple example of input and output pairs?
- How would we approach in finding drug discovery? Does the model provide any candidate paths or of any sort? If so, how would we approach justification of the result?
- What is the "enhanced interpretability"? Would there be an example of this?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This study presents the MARS (Mechanism-of-Action Retrieval System), a neurosymbolic (NeSy) approach designed for interpretable drug discovery. MARS aims to improve understanding of drug mechanisms of action (MoAs) using knowledge graphs (KGs) combined with logical rule-based inference. The model introduces a tailored KG called MoA-net, enabling MoA deconvolution. MARS enhances interpretability by assigning weights to logical rules and employing a two-hop joint probability (P2H) metric to improve model calibration and address potential reasoning shortcuts.

### Strengths
- MARS applies NeSy methods to drug discovery, a field with a strong demand for interpretability. The study’s introduction of MoA deconvolution as a KG-based task and MoA-net as a novel KG for biomedical applications broadens the use of KGs in drug discovery.
- The authors conduct extensive testing of MARS on both synthetic and real data and provide detailed comparisons to existing NeSy methods, particularly regarding susceptibility to reasoning shortcuts.
- By enhancing interpretability in drug discovery, MARS could help researchers gain insights into drug mechanisms, potentially leading to safer and more effective treatments.

### Weaknesses
 - The model is primarily tested on synthetic KG data and lacks real-world validation on clinical datasets or pharmacological records, which limits the practical assessment of its interpretability and generalization for drug discovery tasks.
- While the P2H metric is introduced to make MARS shortcut-aware, its reliance on rule weighting and complex computations might hinder scalability, especially in large, densely connected KGs that are typical in biomedical data.
- AMARS mainly addresses computational rather than biological significance.
- MARS is highly susceptible to node degree bias, leading to unintended reasoning shortcuts.

### Questions
- Testing the model on real-world datasets, such as drug-protein interactions or clinical outcome data, would strengthen the claims regarding its applicability in drug discovery.
- How does MARS handle drug discovery tasks beyond MoA deconvolution?
- How could biological interpretability be further improved? Considering biological plausibility, could the authors incorporate features like protein binding affinities or pharmacokinetic properties to add biological context to MARS’s interpretability?
- Given the computational cost of two-hop joint probability calculations, what specific modifications or future optimizations are planned to enhance scalability?

### Soundness
3

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
The paper proposes MARS, a neurosymbolic model designed to improve interpretability in drug discovery through a task called Mechanism of Action (MoA) deconvolution, using a specialized knowledge graph named MoA-net. MARS intends to offer insights into the interactions among drug, protein, and biological process via learned rule weights.

### Strengths
* The integration of neurosymbolic approaches provides a better understanding of the evidence chain in drug discovery.
* The dynamically learned rule weights may offer an interpretable explanation for the potential impacts of reasoning shortcuts.
* The experimental results are relatively comprehensive and reasonable.

### Weaknesses
 * The paper is poorly structured and written, and quite difficult to follow.
* Baseline methods compared in the experiments appear to be outdated, with the latest only dating back to 2020.
* Although the authors claim that interpretable symbols can enhance the learning process, there is insufficient experimental support for this assertion, especially regarding the discovery of unseen reasoning paths.
* While this work is presented as a reasonable exploration of biologically meaningful evidence chain reasoning shortcuts, the authors only apply it to three types of entity relationships. Existing study [1] has researched more comprehensive biological pathway evidence chain mining using symbolic reasoning and reinforcement learning. A detailed comparison of the similarities and differences between the two approaches, along with a more substantial discussion of the advantages of your work, is needed.


### Questions
* In Lines 235-239, why do the authors state, "Although other metapaths are possible, we exclude them from our set of metapath-based rules"? What's the reason for excluding possible metapaths?
* Following the previous question, what is the rationale for limiting the length of metapaths to 4? Could this lead to insufficient exploration of reasoning paths? If possible, could a comparative experiment on different lengths be conducted?
* In Lines 277-282, the comparison baselines seem to be the latest from 2020. Are there any recent works related to knowledge graphs?
* Why do a significant portion of the results in the experimental tables lack standard deviation? For example, the top 9 baseline models in Table 1.
* Please provide visualizations of the learned rule weights and corresponding analyses.

If the authors could adequately address my concerns, I will consider raising the score.

### Soundness
2

### Presentation
2

### Contribution
2
