# Dynamic multi-channel EEG graph modeling for time-evolving brain network

- Decision: Reject
- Avg Score: 5.50
- Scores: 6, 6, 5, 5

## Abstract
We describe a novel dynamic graph neural network (GNN) approach for seizure detection and prediction from multi-channel Electroencephalography (EEG) data thet addresses several limitations of existing methods. 
While deep learning models have achieved notable success in automating seizure detection, static graph-based methods fail to capture the evolving nature of brain networks, especially during seizure events. 
To overcome this, we propose EvoBrain, which uses a time-then-graph strategy that first models the temporal dynamics of EEG signals and graphs, and then employs GNNs to learn evolving spatial EEG representations. 
Our contributions include 
(a) a theoretical analysis proving the expressivity advantage of time-then-graph over other approaches, 
(b) a simple and efficient model that significantly improves AUROC and F1 scores compared with state-of-the-art methods, and 
(c) the introduction of dynamic graph structures that better reflect transient changes in brain connectivity. 
We evaluate our method on the challenging early seizure prediction task.
The results show improved performance, making EvoBrain a valuable tool for clinical applications.
The source code is available at:
https://anonymous.4open.science/r/EvoBrain-FBC5

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces EvoBrain, a dynamic graph neural network (GNN) model designed to improve seizure detection and prediction using multi-channel EEG data. EvoBrain adopts a time-then-graph approach, sequentially modeling the temporal dynamics of EEG signals before applying a GNN to capture evolving spatial relationships across EEG channels. Key contributions include a theoretical expressivity analysis that suggests potential advantages of the time-then-graph approach, modest empirical gains in AUROC and F1 scores over existing graph-then-time and time-and-graph models, and a dynamic graph structure designed to better reflect changing brain connectivity.

### Strengths
- The paper provides a practical demonstration of time-then-graph modeling in the context of EEG-based seizure prediction, showing how this approach can effectively capture temporal graph representations. This comparison with time-and-graph and graph-then-time methods highlights its strengths in modeling dynamic changes in EEG signals.
- Clinical analysis demonstrated the explainability of the time-then-graph approach by showing learned temporal dynamics through constructed dynamic graphs, providing valuable insights for exploring potential biomarkers in brain connectivity associated with seizures.

### Weaknesses
 - This work applies the time-then-graph approach (Gao & Ribeiro, 2022) to multi-channel EEG data and demonstrates similar positive outcomes, suggesting that the study may take a somewhat naive approach by primarily focusing on adapting time-then-graph to EEG data.
- Much of the theoretical grounding regarding the expressiveness of time-then-graph is already covered in (Gao & Ribeiro, 2022). Additionally, the EvoBrain architecture borrows the GRU-GCN model from that work, raising questions about whether any theoretical advancements in this study are specifically tailored to EEG data.
- The study employs time-then-graph for improved temporal dynamic learning but processes EEG data in the frequency domain using FFT. This choice may limit the representation of temporal signals, as FFT primarily captures stationary frequency content rather than transient temporal dynamics. Although FFT helps in identifying frequency-domain characteristics relevant to seizures, such as specific frequency bands (e.g., delta, theta), it may miss essential non-stationary temporal nuances critical for comprehensive seizure prediction. Using wavelet transforms, which capture both time and frequency, could potentially offer a more robust temporal representation, especially when using the time-then-graph approach.
- While identifying potential biomarkers through clinical analysis is valuable, it remains unclear what insights the collaborating neurosurgeon contributed. For instance, did the findings align with known biomarkers in classical EEG-based seizure research? Or did the identified regions have a functional link to seizure impact? Providing a deeper analysis on these points would enhance the clinical relevance of the findings.
- The Related Works section could better support this study's contributions by restructuring its three paragraphs with clear subheadings and transitions. This would enhance cohesion, clarify the connection to prior research, and position the current work more effectively within the broader literature.

### Questions
- (Gao & Ribeiro, 2022) already established the expressiveness relationships among graph-then-time < time-and-graph < time-then-graph using similar approaches with 1-WL GNNs. Does this paper present any novel theoretical aspects compared to the prior work or specific to EEG data? The same question applies to the computational complexity analysis in Appendix C—does this study offer more than a rephrasing of the findings in (Gao & Ribeiro, 2022)?
- The GRU-GCN model proposed in (Gao & Ribeiro, 2022) is used as EvoBrain in this study; were there any methodological contributions made to adapt this model specifically for EEG in the time-then-graph approach, or was it used as-is?
- Given that time-then-graph aims to prioritize temporal dynamics, why was the frequency domain chosen over the time domain? If time-domain input were used instead, would time-then-graph still outperform graph-then-time and time-and-graph?
- Have any previous seizure detection studies using EEG identified biomarkers similar to those found in this work?
- Based on the parameter counts in Table 3, I wonder if the relatively lower performance of the baseline models might be due to overfitting.
- Would the superior performance of the time-then-graph approach, as shown in Table 2, still hold if the baseline models were adjusted to have comparable layer and parameter count settings?
- In Figure 3, a clearer explanation would be helpful to distinguish between the static and dynamic graph structures used in prior methods and how they were integrated into each approach. For instance, is the static graph $(\mathbf {X},\mathbf {A})$ constructed from frequency spectrum features at each snapshot, as described in Section 4.2? Does the dynamic graph refer to GRU-derived graphs $(h^{node}, h^{edge})$?
- In Figure 5, the constructed dynamic graph remains somewhat ambiguous. Does it refer to $h^{edge}$ learned at each time step via $\text{GRU}^{edge}$?

Minor Typo: 
- In Definition 1, "approache" $\rightarrow$  "approach"

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
This paper introduces a dynamic graph neural network approach called EvoBrain for seizure detection using multi-channel EEG data. EvoBrain implements a strategy called "time-then-graph" strategy, as opposed to "graph-then-time" and "time-and-graph" strategies, while providing a theoretical analysis proving the expressivity advantage of this method. Three key advantages claimed by the authors include (1) the actual inclusion of dynamic graph structures throughout time, instead of a static graph structures which the paper claims previous papers using dynamic graphs actual use, (2) consistent stronger results supported by table 2, and (3) seizure prediction at the preictal state, unlike most previous detection algorithms.

### Strengths
In general, this seems to me to be quite a well thought paper, well framed in the wide literature, with significance to the clinical application of seizure prediction. My knowledge in this (sub)field is limited and - as I'll highlight in the weaknesses section - there are some parts that are confusing to me; however, the paper seems to be quite strong on the three main points I mentioned in the Summary: (1) inclusion of actual dynamic graph structures throughout time, instead of a static graph structures which the paper claims previous papers actually used, (2) consistent stronger results showed in table 2, and (3) seizure prediction at the preictal state, unlike most previous detection algorithms. All of this while providing a theoretical analysis on the expressive power of several points in the paper under the 1-WL graph isomorphism test.  For all these strengths, I believe the paper's originality come from the creative combination of existing ideas to solve known limitations in prior results, apparently successfully. As a consequence, the model's ability to predict seizures 1 minute ahead of time is not only relevant to the clinical field, but also to the computational field as this is done in a computationally efficient fashion with a solid theoretical analysis.

Some other specific strengths of this work that I'd like to highlight are: (1) EvoBrain's gains in performance were achieved with a 23x faster design than the SOTA baseline, (2) validation of this model on an external dataset, (3) the evaluation of the importance of the dynamic graph structure illustrated in figure 3, which not only shows that this paper's ideas could be used to improve previous models, but also that if one wants even faster models, maybe the dynamic graph calculation might not be needed, (4) the computational efficiency analysis, and (5) the ablation analysis on the FFT preprocessing.

Based on these points, I recommend acceptance to ICLR. However, my recommendation is only marginally above the acceptance threshold because of the reasons I'll mention in the Weaknesses section, which I believe will be possible to be mostly tackled during the rebuttal period.

### Weaknesses
One main weakness I identify in this paper is that it's not clear to me how strong/true their claims on novelty are, specifically on two points:
1. Graph-then-time novelty. The paper gives the impression that the "time-then-graph" approach is new/introduced for the first time in this paper. This seems supported by the fact that in table 2 only EvoBrain is shown as the "time-then-graph" type. However, it seems to me that this approach was actually introduced in Gao and Ribeiro (2023), thus I ask the authors whether they can clarify how their approach differs from or build upon Gao and Ribeiro (2023), and explain why that work wasn't included as a baseline in the experiments. This would help address the novelty concern more directly.
2. Claim that only in this paper they truly use "dynamic" graphs. Between lines 67-71, the paper makes a key claim for this work's novelty, in which it is argued that previous GNN works for seizure prediction labelled as "dynamic" are actually based on static graph structures, and that only the temporal aspect of the nodes was considered dynamic before. In my opinion, there are contradictions in this paper with regards to this claim, which require further clarification over the rebuttal period. For example, in lines 52-53, it is said that in the graph-then-time approach, "learning channel correlations" are conducted "at each time step", in practice meaning that indeed the graph is dynamic because at each time step a new graph structure is used. Furthermore, in the formulations in equations 1 and 2, the adjacency matrices change at each time step, just like the "time-then-graph" strategy. Finally, figure 1 doesn't seem to make this distinction clearly either. My impression is that the "time-then-graph" strategy is not so much about actually having "dynamic" graphs, but more how all snapshots up to each time step are considered to create both the adjacency matrix and the node/edge features. I'm wondering whether my confusion also comes from the formulation in section 3.1, in which I do not understand why there is a pairwise connectivity between two channels represented as $e_{ij}$ without a time component, and how it differs from the corresponding $a_{ij}$ and $h_{ij,t}$ representations. This is such an important part of the paper, that I hope the authors can make this more clear during the rebuttal period and in the final version of the paper. To be specific and to summarise this point, I'm asking the authors to provide a more precise definition of what they mean by "dynamic" graph structures, and how their approach specifically differs from previous methods in this regard. This would help clarify their novelty claim.

A further main weakness I identify in this paper is the experiments analysis on the detection/prediction models performances, specifically on three points:
1. There is no variation measure on the experiments results, which would be particularly important in table 2. I'm guessing that the authors did not want to perform cross validation given the TUSZ dataset already came with pre-defined train-validation-test splits and they use an external dataset, but if this was the case then I suggest the authors should at least repeated their experiments multiple times with different random initialisations of the models to report mean and standard deviations in table 2. Some of the results in table 2, even though consistent, make one wonder that maybe there wouldn't be a significant difference if variation (eg standard deviation or variance) is considered. Also, such close results in figure 3 suggest that if such variation calculations were performed, it would indicate that maybe those differences wouldn't be as significant.
2. The fact that no traditional machine learning model was used. For example, what do clinicians using computational models develop, assuming a lot do not use deep learning? Some times traditional machine learning models like SVM or random forests can be as strong or stronger in a certain prediction task, so even if this model brings other advantages compared to previous deep learning models, in a conference like ICLR I believe it is important to understand how that compares to traditional ones that are easier and faster to train and run inference on. My experience comes more from fMRI data, where big simplifications can be done on the temporal data producing some very good results, and I'm guessing that is the same with EEG signal processing. Could the authors then include comparisons with traditional ML methods commonly used in clinical practice for seizure detection/prediction, such as support vector machines or random forests. This would provide a more comprehensive evaluation of the model's practical utility.
3. I surely commend the paper suggesting a "simple" GNN model like the GCN for good and fast results. However, with so many GNN models out there, one would expect at least one or two more "complex" GNN models to understand whether the performance would improve at the cost of more parameters or slower training.

### Questions
As I mentioned, the two main weaknesses I have identified in the previous section will be the main points in which a response from the authors will most likely change the score I give to this paper. I leave though the following questions and suggestions which could help me better understand whether/how to increase the score of this paper:

1. There is a significant class imbalance highlighted in table 1 but the paper doesn't mention anything about it. Did the authors tackled it in some specific way?
2. How did the authors decide the hyperparameters to use, and did it follow the train-validation splits? For a fair comparison, how did that differ from the hyperparameter search of the other models? There is one hyperparameter that seems quite important to me (the $\tau$ threshold introduced in line 263) which was not analysed/ablated.
3. In lines 163/164 it is said "If $e_{ij}$ exists". Maybe this is connected to my confusion mentioned in the previous section, but how could this value not exist? Furthermore, it is said in the same lines that $a_{ij,t} \in R^e$; how is $e$ defined in this case?
4. The authors seemed to have forgotten to write some words in line 181 for it to make sense grammatically.
5. I do not understand why the EEG graphs are directed (as mentioned in line 268). Shouldn't graphs based on correlations be undirected?
6. I'd ask the authors to clarify what they mean as "our method performs GNN processing only once" in line 451. I think it's very clear from the paper that the message-passing component of GNNs, as well as the construction of the (dynamic) graphs at each time step is used at each epoch, so I'm not sure I understand what is this "GNN processing" that is run "only once". This surely would also help better understand the depiction in figure 1.
7. It's not clear to me how the analysis provided in section 5.3 could be generalised for useful clinical practice, even though the specific analysis in this section was validated by two neurosurgeons. Given the limited performance in the F1 metric, I'm guessing that the seizure prediction for each person needs to be much more complex and varied than just the main networks identified in figure 5. Could the authors maybe write one or two sentences on how this depiction could vary across different predictions and be used by neurosurgeons? (eg, is it only the connections getting stronger, or also some specific EEG regions?)

I finish with two specific suggestions about the code shared by the authors:
1. The `requirements.txt` file only has specific versions for 3 packages, and a range of versions for one package. For better reproducibility consider using a .yaml file generated from mamba/conda if you are using such package manager, or something else to ensure that any person could avoid reproducibility issues by starting with the specific dependencies used by the authors.
2. It's not recommended to import everything from specific modules (ie, using `import *`). Authors can see an old discussion about the topic here: https://stackoverflow.com/questions/2386714/why-is-import-bad

### Soundness
2

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
5

### Summary
The authors introduce a novel dynamic graph neural network (GNN) method based on the graph-then-time-based approaches for seizure detection. Specifically, a time-then-graph strategy is proposed that first models the temporal dynamics of EEG signals and graphs, and then utilizes GNNs to learn evolving spatial representations of EEG data. However, there have been related works and this work lacks novelty in the field of EEG signal processing.

### Strengths
The authors introduce a novel model architecture of the Dynamic Graph Neural Network method for seizure detection and superior performance has been achieved.

### Weaknesses
(1)	Related Works – The authors claim that “However, they do not explicitly model temporal relationships, relying instead on convolutional filters or conventional linear projections for node embeddings”. However, there have been works based on the time-then-graph-based approaches (according to Definition 3 and Lemma 3), such as Deep Feature Mining via the Attention-Based Bidirectional Long Short Term Memory Graph Convolutional Neural Network for Human Motor Imagery Recognition. The authors are encouraged to explicitly compare their approach to the specific time-then-graph methods, highlighting key differences and improvements.

(2)	Motivation – Since the time-and-graph-based approaches are more expressive, the authors are encouraged to more clearly explain the advantages of their time-then-graph approach over time-and-graph approaches, given the theoretical analysis.

(3)	Experiments and Ablation Study – The authors are advised to conduct an ablation study comparing their time-then-graph approach to graph-then-time and time-and-graph baselines using the same overall architecture and hyperparameters, to directly validate the theoretical analysis.

(4)	Results – The authors should describe how they get these results. For example, the performance of BIOT is significantly worse than the LSTM and CNN-LSTM. There would be overfitting or information leakage issues in the training process. The authors are suggested to provide more details on their experimental setup, including hyperparameters, training procedures, and any data preprocessing steps. In addition, the authors are encouraged to investigate and discuss potential reasons for BIOT's underperformance compared to simpler models.

(5)	Model Comparison – The authors are encouraged to compare their work with more latest and classic models in the field, such as EEGNet (EEGNet: A Compact Convolutional Neural Network for EEG-based Brain-Computer Interfaces), GCNs-Net (GCNs-Net: A Graph Convolutional Neural Network Approach for Decoding Time-Resolved EEG Motor Imagery Signals), Bi-LSTM-GCNNet (Deep Feature Mining via the Attention-Based Bidirectional Long Short Term Memory Graph Convolutional Neural Network for Human Motor Imagery Recognition), and EEGMamba (EEGMamba: Bidirectional State Space Model with Mixture of Experts for EEG Multi-task Classification).

### Questions
(1) What is the unique and significant technical contribution of your work? The technical idea of this work is quite similar to related works in the field.

(2) Why don't compare the performances of the graph-then-time, time-and-graph, and time-then-graph approaches using the same overall architecture and hyperparameters, to directly validate the theoretical analysis? The current experiments cannot support your theoretical analysis.

(3) Considering that the time-and-graph-based approach is more expressive in feature learning, why not design a novel architecture based on it?

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a time-then-graph model architecture called EvoBrain to capture dynamic graph structures in the brain network for EEG seizure detection and prediction. The authors show theoretical proof that time-then-graph architecture is more expressive compared to time-and-graph and graph-then-time architectures. In addition, experimental results show improved performance on seizure detection and prediction compared to several existing models.

### Strengths
* The authors show theoretical proof of expressiveness of three different dynamic GNNs for EEG modeling.

* Experimental results suggest that the proposed EvoBrain improves over existing GNNs on seizure detection and prediction

### Weaknesses
 * The following paper Tang et al. 2023 also constructs dynamic graphs in a time-then-graph fashion, but there is no comparison between EvoBrain and Tang et al. 2023. Also, in related work, there is no mentioning of prior time-then-graph approaches.
  * Tang, S., Dunnmon, J. A., Liangqiong, Q., Saab, K. K., Baykaner, T., Lee-Messer, C., & Rubin, D. L. Modeling Multivariate Biosignals With Graph Neural Networks and Structured State Space Models. In Proceedings of the Conference on Health, Inference, and Learning (Vol. 209, pp. 50–71). PMLR.

* The seizure prediction task definition is unclear. On Page 7, the authors state that “we defined the one-minute period before a seizure as the preictal phase”. However, this “one-minute period” seems arbitrary. If there is preictal annotation in the dataset, please use it. If not, please provide justification on why this “one-minute period” definition is clinically meaningful. The lack of a clear clinical basis for this one-minute window undermines the validity of the prediction results. Furthermore, the authors should clarify whether this one-minute window is a fixed duration across all patients and seizures, and how this choice might affect the model's performance, especially if preictal periods vary in length.


### Questions
* As mentioned above, please include more time-then-graph comparisons.
* Please provide detailed descriptions on the seizure prediction task setup.
* In Figure 4, training time between different models is compared. However, for clinical utility, inference time is more crucial. Please provide comparison of inference time between the models.

### Soundness
3

### Presentation
2

### Contribution
2
