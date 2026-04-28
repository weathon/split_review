# Interactions Exhibit Clustering Rhythm: A Prevalent Observation for Advancing Temporal Link Prediction

- Decision: Reject
- Avg Score: 5.00
- Scores: 6, 3, 6, 5, 5

## Abstract
Temporal link prediction aims to forecast future link existence in temporal graphs, with numerous real-world applications. Existing methods often rely on designing complex model architectures to parameterize the interaction patterns between nodes. Instead, we re-think the interaction dynamics in temporal graphs (which we call ``interaction rhythms'') by addressing a fundamental research question: \textit{Is there a strong yet prevalent latent interaction rhythm pattern across different temporal graphs that can be leveraged for temporal link prediction?} 
Our introduced empirical analyses reveal that there indeed exists temporal clustering in node interaction rhythms, where for a specific node, interactions tend to occur in bursts. Such observation leads to two key insights for predicting future links: (i) recent historical links that carry the latest rhythm pattern information; and (ii) the inter-event times that further illuminate temporal dynamics. 
Building on these empirical findings, we propose TG-Mixer, a novel method that explicitly captures temporal clustering patterns to advance temporal link prediction. 
TG-Mixer samples the most recent historical links to extract surrounding neighborhoods, preserving currently invaluable interaction rhythms while avoiding massive computations. 
Additionally, it integrates a carefully designed silence decay mechanism that penalizes nodes' long-term inactivity, effectively incorporating temporal clustering information for future link prediction.
Both components ensure concise implementations, leading to a lightweight architecture. 
Exhaustive experiments on seven benchmarks against nine baselines demonstrate that TG-Mixer achieves state-of-the-art performance with faster convergence, stronger generalization capabilities, and higher efficiency. The experimental results also highlight the importance of explicitly considering temporal clustering for temporal link prediction.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This study highlights a previously overlooked yet strong and prevalent latent interaction rhythm pattern. It introduces a model called TG-Mixer model to capture this pattern, achieving superior performance in temporal link prediction. 

First, the authors conduct empirical analyses to confirm that such latent interaction rhythm patterns exist in various real-world temporal graphs. They show, at both macro and micro levels, that real-world temporal graph interactions exhibit short-term interaction bursts compared to random interactions. This, in turn, creates a significant clustering pattern in node interaction rhythms. 

Based on this finding, the authors propose TG-Mixer, a model to capture these clustering patterns. TG-Mixer samples a node's most recent historical links at each time point and encodes them using node and edge features and time intervals. The model also incorporates a "silent decay mechanism" to penalize long-term inactive nodes, thereby capturing temporal clustering patterns with a decaying approach. Through an additional LSTM-based information mixer, TG-Mixer combines temporal and structural information, along with temporal clustering signals, to form node representations, which are then used for link prediction. 
Experimental results demonstrate that TG-Mixer outperforms other baselines regarding faster convergence, stronger generalization capabilities, and higher efficiency.

### Strengths
•	S1. Validity of Empirical Analysis: The authors hypothesize that temporal clustering patterns exist in real-world temporal graphs and verify this through empirical analysis. They introduce a "silence duration" metric to measure the degree of interaction bursts per node, comparing interactions in real-world temporal graphs to random pairs at both macro and micro levels. They conclusively show that real-world temporal graphs exhibit significantly more short-term bursty clustering patterns, making this approach and result convincing and significant.

•	S2. Originality: Unlike existing methods, this study introduces a novel approach to encoding temporal clustering patterns and demonstrates experimentally that these patterns play a significant role.

•	S3. Clarity: The research process is presented clearly. The authors empirically demonstrate the temporal clustering patterns overlooked by existing methods, explain how TG-Mixer encodes these patterns, and clearly show how it performs well in temporal link prediction. This structure makes the study easy to follow.

### Weaknesses
•	W1. Similarity of Techniques to Existing Methods: The stage of TG-Mixer in lines 259-271 of section 4 is similar to that of GraphMixer. Specifically, sampling the most recent historical links and encoding and padding historical link information closely resemble the link-encoder process in GraphMixer, even though the TG-Mixer encoder after that stage is a novel approach. The use of a temporal attention mechanism and the aggregation of historical information through a recurrent network are also common techniques in temporal graph neural networks, raising concerns about the incremental novelty of the approach beyond the core idea of capturing temporal clustering.

•	W2. Insufficient Detail in Method: The silent decay mechanism is a key component of this study, yet the explanation of the communal rhythm vector in lines 287-301 is insufficient. While additional details are provided in appendix A in the context of the Hawkes Process, the role of the rhythm vector is not clearly explained in the main text, making it difficult to understand its purpose. Specifically, the mechanism by which this vector is updated and how it interacts with the node embeddings is not clearly articulated. It is unclear how the rhythm vector is initialized and whether it is a learnable parameter or derived from the data.

### Questions
•	Q1. I want to provide a more detailed explanation of the rhythm vector in lines 287-301 of section 4. Is this rhythm vector updated globally whenever there is an interaction?

o	Q1.1 If the rhythm vector is indeed updated globally with each interaction, how does this work when TG-Mixer processes interactions in batches?

o	Q1.2 Additionally, how is the rhythm vector updated when multiple interactions occur simultaneously in a single time step? This may not matter at high-time resolutions, but I’m curious about the handling of multiple interactions at the same time.


•	Q2. In section 4, the method presents sampling the most recent historical links as a novel approach. However, I’m curious about the differences between this sampling method and the one used in GraphMixer. In lines 265-266, it is mentioned that GraphMixer samples a "massive number of selected historical neighbors." Still, I understand that GraphMixer also samples only the top K links when encoding edge information. Is there a difference here?

•	Q3. In many results of section 5, temporal link prediction performances in many TGNN models, including TG-Mixer, are evaluated using random negative samples. However, I’m curious whether TG-Mixer would still outperform other baseline models if evaluated using a more advanced negative sampling approach based on node degree distribution (i.e., the frequency of prior interactions).

•	Q4. In many experiments of section 5, TG-Mixer uses sample size as a hyperparameter, adjusting it differently for each dataset. How did you determine the optimal sample size for each dataset? Did you tune it on the validation set, or did you test multiple sample sizes on the test set and report the best performance?

### Soundness
3

### Presentation
4

### Contribution
4

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
The authors of this work propose the temporal graph learning model TG-Mixer, which is based on an encoder-decoder architecture. Building on the observation that nodes in many temporal networks exhibit bursty interaction patterns, the encoder uses a sample of recently occurring interactions for a given node u and timestamp t, mixing a concatenation of neighbor and link features with a vector-based representation of temporal interaction patterns that are fed into an LSTM model. Addressing a dynamic link prediction task, the proposed architecture is experimentally evaluated against multiple baseline models, showing good performance in seven empirical temporal network data sets. An additional analysis of training times shows that the model can be trained more efficiently than the competing baseline methods. Additional results in the appendix consider standard benchmark graphs from the TGB community benchmark, an ablation study that replaces the information mixer with an attention mechanism, as well as additional experiments on partially shuffled data sets that partially destroy temporal clustering.

### Strengths
[S1] The authors propose a novel temporal graph learning architecture to address the temporal link prediction problem, which is an important problem in many scenarios.

[S2] The proposed method allows to incorporate both temporal and topological patterns in temporal graphs.

[S3] The authors performed a rather extensive set of experiments, with many different baseline models, several empirical data sets, as well as an ablation study and experiments on partially shuffled data sets.

[S4] The results of the experimental evaluation are promising, showing (mild) increases of performance against many baseline models as well as considerably reduced training times.

### Weaknesses
[W1] The claimed contribution of observing bursty interaction patterns in temporal graphs is not new and the work should be better aligned with the large body of existing literature on bursty interaction patterns in temporal graphs.

[W2] Key components of the TG-Mixer encoder, which is a central component, are not explained well.

[W3] The problem formulation is unclear and does not seem to match the empirical evaluation.

[W4] The authors did not properly account for recently highlighted challenges in the evaluation of dynamic link prediction.

### Questions
Regarding [W1], in the introduction the authors claim that one of the two key contributions of this work is that they "observe a prevalent and strong pattern of temporal clustering in node interaction rhythms". However, this is hardly an original contribution of this work, as there are dozens of works outside the ML community that have not only observed but also quantitatively characterized and modeled bursty interaction patterns in temporal networks. A very incomplete selection of works published over the past ten years include:

- M Karsai et al.: Small but slow world: How network topology and burstiness slow down spreading, PRE, 2011
- R Lambiotte et al.: Burstiness and spreading on temporal networks, EPJ, 2013
- T Hiraoka: Modeling temporal networks with bursty activity patterns of nodes and links, Phys Rev. Research 2, 2020
- B Min and KI Goh: Burstiness: Measures, models, and dynamic consequences, Temporal Networks, 2013
- M Karsai et al.: Empirical findings in human bursty dynamics, Bursy Human Dynamics, 2018
- Hang-Hyun Jo et al.: Bursty Time Series Analysis for Temporal Networks, Temporal Network Theory, 2023

Related to this missing related work, it is not ideal that the authors do not use terminology that is common in the field. For instance, they renamed the concept of inter-event times, which is common both in temporal networks and time series analysis, "silent duration". This makes the work unnecessarily hard to read. 

Finally, it is a well-known fact that bursty interaction patterns are associated with non-Poissonian, heavy-tailed inter-event time distributions, for which the mean is not a meaningful characterization. As such, the analysis of mean silence durations in Figure 2 is not insightful and the resulting comparison to randomly sampled interactions simply repeats the well-known fact that the distributions are not Poissonian (as expected from a memoryless, i.e. Markovian process).

Considering [W2] from the description in section 4 I could neither understand the definition nor the motivation of the TG-Mixer Encoder component. In particular, how exactly is $C_{rhythm}^t$ defined? How is the information on "interaction rhythms" encoded in the "communal rhythm vector"? What is the motivation for the definitions of $C_{temp}^t$ and $C_{decay}^t$?

Regarding [W3] I have concerns regarding the problem formulation, especially whether it actually matches the task addressed in the experimental evaluation. In Definition 2, the authors state that they address the task of predicting the presence of a link between a specific pair of nodes and at a *specific* timestamp t. Notably, this is more difficult than predicting whether a link will exist within a given time interval (or batch) or whether a link will exist in the future, i.e. *after* a given timestamp t. In the description of the experimental evaluation, I did not find further details of how this specific link prediction task has been evaluated. My assumption is that the authors have rather addressed a batch-based prediction, i.e. predicting whether a link occurs in a given batch in the test/validation set. Whether or not this task corresponds to the task specified in Definition 2 depends on (i) the batch size, and (ii) the characteristics of the temporal network (i.e. whether it a discrete- or continuous-time temporal graph). Unfortunately no details on batch sizes are mentioned in the description of the experimental results, which would be crucially important for interpretation. Moreover, seeing the very high values of the average precision scores both for the proposed model and the basline methods makes me doubt that the authors actually addressed the task of predicting the presence of a link at a specifc time stamp t.

Related to weakness [W4], I would like to refer to the challenges in the evaluation of dynamic link prediction that have been outlined in: 

Poursafaie et al: Towards better Evaluation for Dynamic Link Prediction, NeurIPS, 2022

This work introduced EdgeBank and is cited in the paper for this reason. However, it also highlights the need to carefully consider different negative sampling strategies in the evaluation of dynamic link prediction, which have been shown to considerably influence the performance (and ranking) of temporal graph learning models - even for some of the data sets used in the present work. Since the authors cite this work, it is unclear why only the simplest negative sampling method has been used in the experimental evaluation. Also some of the other proposed negative sampling methods are implemented in the temporal graph learning library used by the authors, which would have made it easy to include those as additional results (I also checked but did not find those in the appendix).

Moreover, I appreciated that the authors followed the suggestion of the temporal graph benchmark TGB, adopting a rank-based evaluation in terms of the mean reciprocal rank (MRR) in the supplemental experimental results in the appendix. However, I think that all of the results on the five TGB benchmark data sets for dynamic link property prediction should be shown in the paper - not only those two for which - according to the authors - the proposed method ranks first and third. FInally, I would kindly ask to include the rank-based MRR scores also for the data sets considered in the main paper.

Due to the open issues outlined above, I currently evaluated this work with a score of 3, but would be open to revise this judgment if my concerns are addressed adequately.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
Authors propose the framework (TG-Mixer) that captures the bursty interactions better, given that such bursty interactions are common behaviors in the real-world datasets. Authors perform both macro and micro level analysis about the bursty interaction evidence. Based on this evidence, authors introduce the silence decay mechanism and mix it into the temporal encoding through LSTM so that the temporal encoding leverages the silence more explicitly. Based on this assumption, recent neighbor sampling strategy is proposed for the given model framework.

Authors demonstrate that the proposed method outperforms baselines in the temporal link prediction tasks. Furthermore, this performance can be achieved with less training time and fewer computational cost since the algorithm converges fast. 

Finally, authors perform experiments about the generalizability of the silence decay mechanisms as well as the ablation study about proposed components, which include the silence decay mechanism and recent neighbor sampling. The ablation study proves the importance of the proposed components.

### Strengths
- The introduction of the silence decay mechanism makes sense and works well. This component seems to deliver the inactivity information more effectively than temporal models (e.g. LSTM) learn from data.
- The proposed method shows superior performance as opposed to the baseline models.
- Ablation study helps the understanding of the roles for each proposed component.

### Weaknesses
 - The analysis about the silence duration (Figure 2) is not fair to compare because many of random pairs would not happen forever in the existing datasets. While the low silence duration for positive links makes sense, it is not clear to understand whether high silence duration in the random selection is mostly originated from the pairs that would never link or from the inactive period of the potentially interacting pairs.

- Similarly, the discriminative signal argument in 5.3 is overstated by the reason mentioned in the previous bullet point. The following phenomena can explain this as well: (1) if the pairs have never interacted before, then they are also unlikely to interact in the future. (2) if the pairs recently interacted, then they are likely to interact in the current timeframe. Temporal clustering should represent burstiness or not (e.g. periodic interactions), but no interactions are mixed in the analysis.

### Questions
- The idea of the silence decay seems irrelevant to graph data. Have the authors applied this idea into the other bursty time-series prediction? Or if this idea should be related to GNN (i.e. neighbor samples), what is the main reason for that?

- Does the ablation study cover where g(s) = 0 case? That is, the proposed framework works with LSTM and everything but the silence decay, and it would be good to check its performance as well as convergence. This ablation study would be interesting since LSTM is supposed to capture the temporal patterns but the silence decay provides some short-cut to the important information. Hence, it would be great to understand how temporal mix can suffer without this shortcut.

- Silence decay component may clearly discriminates easy negative links more efficiently. It would be great to check the performance on brand-new links (new links that never interacted before) or resurrecting links (interactions after some inactive period)

- This idea would seem to work well for the periodic interactions (e.g. location check-ins). It would be great to show this empirically. Otherwise, the proposed method would be limited only to burst interaction networks.

### Soundness
2

### Presentation
3

### Contribution
3

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This study empirically shows that nodes often interact with others in bursts. Building on this observation, the authors introduce TG-Mixer, a novel model that captures these temporal clustering patterns. While its framework is similar to GraphMixer, TG-Mixer introduces a Temporal Mixer module that penalizes nodes for prolonged inactivity. TG-Mixer demonstrates superior performance and higher efficiency compared to other baseline models across several datasets.

### Strengths
1. This work aims to uncover the temporal patterns in temporal graphs, which is a novel perspective that few relative studies address. 
2. TG-Mixer demonstrates outstanding performance across several datasets, including US Legis and LastFM, and is more efficient than baseline models.
3. The writing is clear and easy to follow.

### Weaknesses
 1. The key insight of this work is that the popular nodes are likely to interact with others or be interacted with. However, in many real-world applications of temporal graphs, such as recommender systems, popularity is already a significant factor. Thus, the more challenging problem is to rank these popular items. Simply incorporating popularity offers limited contributions to temporal graph learning, so it would strengthen the study to further demonstrate the power of TG-Mixer to distinguish popular nodes. For example, these empirical comparisons could be conducted:
     1. comparing TG-Mixer and the heuristic method that always chooses the most popular destination nodes.
     2. using the MRR metric with the 100 most **popular** destination nodes as negative destination nodes.
     3. using historical neighbors as negative destination nodes, as proposed in [R1].
2. The authors have not provided the complete implementation code in the supplementary materials, notably missing the `TimeMixer` component, which is central to the proposed method. I recommend that the authors make the full code for this work available.

### Questions
1. In the experiments, do the negative edges share the same source nodes as the positive edges? If not, it would improve consistency to fix the source nodes for both positive edges and their corresponding negative edges across all experiments.
2. Among the TGB datasets, tgbl-review and tgbl-comment are considered challenging according to existing empirical studies. How does TG-Mixer perform on these two datasets?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 5

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
In this paper, the authors considered the temporal link prediction task on continuous-time dynamic graphs (CTDGs). They first demonstrated that temporal clustering patterns (also defined as node interaction rhythms in this paper) are obvious latent features of various dynamic graphs, based on a series of empirical analysis on some real datasets. A TG-Mixer method was then proposed to fully explore these patterns with some designs of most recent historical links sampling, silence decay mechanism, etc.

### Strengths
**S1**. The authors conducted a great amount of experiments to demonstrate the motivations and validate the effectiveness of the proposed method.

**S2**. The proposed method can achieve good experiment results.

### Weaknesses
 **W1**. The overall presentation of this paper is poor. There are many unclear, confusing, or even inconsistent statements, which make the motivation of this paper weak.

  In this paper, use 'temporal graph networks' (TGNs) to represent deep learning models designed to handle dynamic graphs. However, 'graph' and 'network' are usually synonyms in some literature. 'Temporal graph networks' may cause some ambiguity issues. As I can check, TGN is also the name of an existing method, while the authors used TGNs to represent a set of methods.

  At the very beginning of this paper, the authors claimed that existing methods 'process interactions separately without considering the inherent high-level temporal correlations among interactions between nodes' and thus 'fail to effectively capture the invaluable patterns of interaction dynamics'. Such a statement about the research gap is quite weak. It is unclear for me what do 'high-level temporal correlations among interactions' and 'interaction dynamics' refer to. There are no any toy examples to demonstrate these concepts. From my perspective, directly reaching such a conclusion without giving further interpretations or toy examples (e.g., due to what mechanism existing methods fail to capture such dynamics) is also insufficient, which makes the the motivation of this paper very weak.
  
  The authors repeatedly use 'temporal clustering' and 'node interaction rhythms', which are high-level concepts seldom used in related literature. Even though they gave the corresponding definitions in Section 2, they are still hard to understand. For some new but important concepts or terminologies, it is recommended to give some toy examples (e.g., a dynamic graphs with only a few nodes) in addition to their formal definitions, especially at the very beginning of a paper.

  The authors also claimed that Fig. 2 (a) confirms the presence of temporal clustering patterns but why? Since there are no interpretations or examples to demonstrate how to measure the temporal clustering patterns, it is also insufficient to reach such a conclusion, from my perspective. It is also similar for the discussions regarding Fig. 2 (b).
  
  For the further discussions regarding the empirical analysis w.r.t. Fig. 2 (a) and (b), the authors claimed that 'recent historical links, carry the latest rhythm pattern information, are crucial for prediction future links'. From my perspective, we can only reach a conclusion that 'recent historical links' are obvious latent futures in dynamic graphs based on Fig. 2 (a) and (b), but cannot say 'they are crucial for prediction future links', since Fig. 2 (a) and (b) are not directly related to the quality of temporal link prediction.
  
***

**W2**. Some details of the proposed methods are unclear or with weak motivations.

  From my perspective, the connection between the empirical analysis in Section 3 and some designs in Section 4 is weak. For instance, it is unclear for me why sampling the most recent historical links can preserve interaction rhythm patterns and why conventional sampling strategies may fail to preserve these patterns.
  
  There may exist some flaws of only sampling top $m$ most recent historical. It is well-known that some real dynamic graphs may follow typical power-law distributions. The power-law distribution of node degrees may indicate that there are some nodes with many historical links and some other nodes with very few historical links. $m$ is a constant for all the nodes in the proposed method. This design may result in an exception that there are some nodes without any sampled historical links (i.e., with degree less than $m$).

  In Eq. (3), it seems that ${\bf{C}}_{decay}^{t}$ is a vector associated with a node $u$, but there is no subscript or superscript of $u$ for this vector.

***

**W3**. The theoretical analysis in Appendix A is weak or even needless.

  From my perspective, the connection between Eq. (8) and Eq. (9) is not exactly as the authors claimed in Appendix A. In Eq. (9), the first term ${\bf{C}}_{rhythm}^t$ is used by all the nodes, as described in Section 4.

Whereas, in Eq. (8), the first term is associated with a node $u$. The connection between the summation in the second term of Eq. (8) and $g(s_u^t) {\bf{C}}_{temp}^t$ in Eq. (9) is also not clearly interpreted.
  
  The discussions in Appendix A cannot be considered as a theoretical contribution, since it just simply listing two existing known definitions (i.e., Definition 1 and Definition 2). There are no original theoretical results and corresponding proofs.

***

**W4**. Some experiments settings and results are unclear, which need further clarification.

  The the definition of the X-axis in Fig. 2 (a) is not given. As a result, it is unclear for me what does 'macro-level distribution' mean and how to correctly read Fig. 2 (a). The unit of the y-axis (i.e, silence duration) in Fig. 2 (a) and (b) is not given.

### Questions
See **W1**-**W4**.

### Soundness
2

### Presentation
1

### Contribution
2
