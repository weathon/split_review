# FreeDyG: Frequency Enhanced Continuous-Time Dynamic Graph Model for Link Prediction

- Decision: Accept
- Scores: 8, 6, 8, 5

## Abstract
Link prediction is a crucial task in dynamic graph learning. Recent advancements in continuous-time dynamic graph models, primarily by leveraging richer temporal details, have significantly improved link prediction performance. However, due to their complex modules, they still face several challenges, such as overfitting and optimization difficulties. More importantly, it is challenging for these methods to capture the 'shift' phenomenon, where node interaction patterns change over time. To address these issues, we propose a simple yet novel method called \textbf{Fre}quency \textbf{E}nhanced Continuous-Time \textbf{Dy}namic \textbf{G}raph ({\bf FreeDyG}) model for link prediction. Specifically, we propose a node interaction frequency encoding module that both explicitly captures the proportion of common neighbors and the frequency of the interaction of the node pair. Unlike previous works that primarily focus on the time domain, we delve into the frequency domain, allowing a deeper and more nuanced extraction of interaction patterns, revealing periodic and "shift" behaviors. Extensive experiments conducted on seven real-world continuous-time dynamic graph datasets validate the effectiveness of FreeDyG. The results consistently demonstrate that FreeDyG outperforms existing methods in both transductive and inductive settings. Our code is available at this repository: \href{https://github.com/Tianxzzz/FreeDyG}{https://github.com/Tianxzzz/FreeDyG}

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose the FreeDyG graph neural network (GNN) model for continuous-time dynamic graphs. It incorporates frequency-based representations of the nodes to attempt to capture periodic patterns in the dynamic graph. It also contains a novel node interaction frequency encoding approach. The authors demonstrate impressive link prediction accuracy in both transductive and inductive settings compared to other GNNs for dynamic graphs on a variety of real data sets. They also perform favorably in terms of training time and size of the trained model when compared to other methods.

*After author rebuttal:* The authors have partially addressed my concerns in their rebuttal and revision, particularly regarding the usefulness of the frequency encoding. After reading through the other reviews, I am still in support of this paper.

### Strengths
- Proposed FreeDyG model contains several novel elements, including the design of the node interaction frequency (NIF) encoding and incorporating frequency-based representations.
- Comparison of accuracy, training time, and model size shown in Figure 2 is a nice inclusion. This shows that improvements in accuracy are not at the cost of significantly increased training time or a very large model.
- Strong improvements in accuracy compared to other approaches. These improvements hold over different negative sampling strategies and evaluation metrics.
- Mostly well written and organized paper. In my opinion, the authors made good choices on which results and details should be presented in the main paper rather than the appendices.

### Weaknesses
 - The positioning of the paper is a bit deceiving. From reading the paper, it would appear as though the main contribution is incorporating the frequency information. However, from the results of the ablation study in Figure 3, we see that the NIF encoding plays a much bigger role in improving accuracy than the frequency-based representations.
- The authors present no evidence that the frequency-based representations are actually able to capture periodic patterns, which they used as their motivation for using the FFT. It is unclear if the frequency-based representations are learning anything meaningful or if they are just adding extra parameters to the model, which could be the reason for the slight improvement in results.

Minor concerns:
- Table 3 is probably not the best way to present the hyperparameter study. Typically, one would be looking for trends as you vary the number of historical neighbors $L$. Such trends are difficult to pick out from the table. I would suggest instead using plots with AP or AUC-ROC on one axis and $L$ on the other.
- Page 7, second last paragraph: "neigh encoding"

### Questions
1. Is there a way you could inspect your trained model to identify whether any type of periodic patterns are being captured by your frequency-enhanced MLP-Mixer layer?
2. Why is the NIF encoding more important than the frequency-based representations for improving link prediction accuracy?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper proposes a novel method called FreeDyG for link prediction in dynamic graphs. The method devised a novel frequency-enhanced MLP-Mixer layer to learn the periodic temporal patterns and the ”shift” phenomenon present in the frequency domain. The effectiveness of the FreeDyG model was validated on several real-world datasets, showing performance improvement in AUC-ROC against baselines.

### Strengths
1. The proposed frequency-enhanced MLP-Mixer is novel and effective.
2. The experiments of link prediction are comprehensive. It is conducted on seven datasets and compares the performance against 9 baselines in two dynamic settings, which is solid and comprehensive to validate the effectiveness of FreeDyG in link prediction.
3. The paper is well written, especially the problem formulation and methodologies.

### Weaknesses
1. The motivation of delving into the frequency domain needs to be further clarified. I am wondering about the intuitions behind capturing the ”shift” phenomenon hidden in the frequency domain. Specifically, the paper does not adequately explain why temporal shifts in dynamic graphs would manifest as specific patterns in the frequency domain, and how these patterns are distinct from other temporal dynamics. A more detailed explanation of the theoretical link between temporal shifts and frequency-domain representations is needed.
2. The authors claim that FreeDyG is the first work that considers the frequency information for dynamic graph embedding, which is overclaimed.
3. The authors argue that random walk based approaches are computationally expensive. However, conducting Fourier transform are also very computationally expensive. In addition, I think FreeDyG also relied on some random walk based approach to obtain the continuous-time dynamic graph from the raw graph data. It is unclear how the sampling of neighbors for the Fourier transform is done, and whether this sampling process introduces any bias or is computationally cheaper than random walks. The paper needs to clarify the sampling strategy and its computational cost in detail.
4. The proposed FreeDyG seems computationally expensive. However, there is no time complexity analysis. The authors are suggested to present the time complexity empirically or theoretically. The absence of a detailed time complexity analysis makes it hard to assess the scalability of the method, especially when compared to other baselines. A theoretical analysis of the time complexity, as well as an empirical analysis on different graph sizes, is needed.
5. In a dynamic graph, some nodes will have more edges, but others will have fewer. Using AUC-ROC as the evaluation metrics cannot tell how good the performance of link prediction for minority nodes. I suggest reporting the Micro- and Macro-F1 scores in the link prediction tasks.

### Questions
1. Why does this work only focus on the link prediction? How is applying this work applicable to other graph mining tasks like node classifications?
2. For the LastFM, what is the summit of the performance when sampling more neighbor nodes? Could you please clarify the experiment details about training every baseline using the same amount of information as FreeDyG in the experiments?

### Soundness
3 good

### Presentation
4 excellent

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper introduces a new GNN for CTDG. The concept of Node Interaction Frequency (NIF) Encoding appears to be a simplified version of SEAL, a link prediction technique for static graphs, and it further introduces a frequency-enhanced MLP-Mixer layer that has functions of Fourier transform and inverse transform with weight learning. Evaluation is conducted in various experimental settings, including transductive/inductive and three negative sampling strategies.

### Strengths
S1. The overall architecture is well-designed. Of particular interest, the Node Interaction Frequency (NIF) Encoding and frequency-enhanced MLP-Mixer layer are novel and highly effective.

S2. The proposal achieves performance higher than the state-of-the-art. Particularly, achieving high efficiency and high quality is impressive. The ablation study verifies that each technical component is effective for high accuracy. 

S3. The experimental settings are detailed, encompassing evaluation experiments across 9 methods, 7 real-world datasets, and various settings including transductive/inductive and three negative sampling strategies.

### Weaknesses
W1. Since the proposal's effectiveness varies across datasets, it is essential to discuss the impact of Node Interaction Frequency (NIF) Encoding and the frequency-enhanced MLP-Mixer layer by investigating the characteristics of each dataset. For instance, if a certain dataset is known to exhibit strong periodic patterns, it would be reasonable to expect the frequency-enhanced MLP-Mixer layer to be particularly beneficial. However, the paper lacks a detailed analysis of which datasets exhibit such patterns and how the model's performance correlates with these characteristics. Similarly, an analysis should be conducted to determine which data characteristics justified the effectiveness of NIF Encoding, such as the density of interactions or the presence of specific interaction motifs, and how these characteristics vary across datasets.

W2. Some design decisions are not clear. For example, while it is crucial that $F^t_*$ represents common neighbors and their past interactions, the rationale behind using a sum pooling operation in Equation 3 to consolidate the count information of common neighbors and interaction frequency is not adequately explained. It is unclear why a simple sum is sufficient to capture the potentially complex relationships between these features. The paper should explore alternatives or justify the choice of sum pooling with more rigorous arguments.

W3. The equation transformation involving $w_k^{(t)}$ in Equation (9) is not clear. The paper states that $w_k^{(t)}$ is obtained by applying a discrete Fourier transform, but the specific details of how this transformation is implemented and why this particular form is chosen are not fully elaborated. Additional clarification is necessary to understand the mathematical underpinnings of this transformation and its implications for the model's performance.

### Questions
Q1. It would be valuable to discuss how the proposal outperforms other approaches, such as using RNN or transformers, which are known to capture some temporal patterns. This comparison can provide insights into the superior performance of the proposal.

Q2. Could you please clarify whether the optimization is conducted in an end-to-end fashion?

Q3. What is the mean of the circle sizes in Figure 2?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors considered the temporal link prediction task on continuous-time dynamic graph (CTDG) and proposed a novel FreeDyG method, which to my knowledge, is the first work to use a frequency-based discrete Fourier transform (DFT) to capture the evolving patterns of CTDG. The overall presentation of this paper is clear. The experiments are also comprehensive and sufficient that can validate the effectiveness of FreeDyG.

### Strengths
S1. The overall presentation of this paper is clear, which is easy to grasp the key ideas.
  
S2. Using the frequency-based Fourier transform to capture the evolving patterns of dynamic graphs is novel and interesting.

S3. The authors conducted comprehensive and sufficient experiments covering both transdutive and inductive settings of temporal link prediction.

### Weaknesses
 **W1. From my perspective, some of the motivations regarding model designs need further verification or validation.**
  
In Section 1, the authors argued that RW, TPP, and ODE are computationally expensive. However, the proposed method includes a sampling procedure that samples $L$ first-hop historical neighbors for both source and target nodes. It seems that such a sampling procedure has a complexity similar to those of conventional methods (e.g., RW-based and PPT-based), according to my background knowledge. To verify this motivation, is is recommended to add the comparison of time complexity for sampling/feature extraction in both training and testing phases. Specifically, a detailed analysis of the computational cost of sampling $L$ neighbors, including the time complexity of finding the most recent neighbors, should be provided. Furthermore, the comparison should not only focus on the sampling procedure but also the overall feature extraction process, including the DFT and subsequent operations. It is also suggested to add pseudocode of each procedure (e.g., first-hop historical neighbors sampling, FFT, extraction of node interaction frequency, etc.) even in the appendix since the details of some modules in current version of manuscript are still unclear. Moreover, the authors claimed that self-attention acts as persistent low-pass filter and the utilization of DFT can tackle its limitation. How this superiority of the proposed method is validated in the experiments? It would be beneficial to see a more direct comparison, such as ablating the DFT component and showing the performance difference, or providing a theoretical analysis of how the DFT addresses the low-pass filtering effect of self-attention.
  
***

**W2. As stated in Section 2, the authors only considered CTDG with edge addition events. It seems that the proposed method cannot handle the deletion of edges.**
  
***  

**W3. It semes that there are some inconsistent and unclear statements.**
  
In Eq. (1) $n$ starts from 0 but in the 2nd paragraph of Section 2, the authors defined that ${x_n}_{n=1}^N$, where $n$ starts from 1. It is also similar for $ {X_k} _{k=1}^N$. In the 2nd paragraph of Section 3.1, the definitions of $\alpha$ and $\beta$ are not given. In Eq. (11), what is the dimensionality setting of $W^{agg}$? It is still unclear how to derive a vector $h_*^t$ based on a matrix $Z_*^l$. Moreover, there is no $t$ in the right side of Eq. (11) but how can we know $t$ in the left side?
 
***

**W4. There are also some minor errors.**

e.g., 'In addition, We specifically encode' > 'In addition, we specifically encode'

### Questions
According to my background knowledge, a significant property of CTDG is that the difference between two successive time steps can be irregular. However, as shown in Table 4, each dataset has an item 'Duration'. What does this item mean? Does is mean that the time steps of all the datasets are still regularly spaced?
  
  In some previous studies, the inductive settings include the prediction between (i) one previously observed node and one newly added node as well as (ii) between two new nodes. It is unclear that the inductive setting in this study refers to which case?
  
  According to my understanding, the inductive inference of the proposed method and other baselines relies on the availability of graph attributes (i.e., node and edge attributes in this study). Consider an extreme case, when attributes are unavailable, can the proposed method still support the inductive temporal link prediction?
  
  In addition to the commonly used settings of temporal link prediction in this study (i.e., the prediction of unweighted feature links), there are some other studies considered the advanced temporal link prediction tasks for weighted dynamic graphs [1-4], which should not only determine the existence of a future link but also the corresponding edge weight. Can the proposed method be extended to handle such an advanced settings?
  
  [1] GCN-GAN: A Non-linear Temporal Link Prediction Model for Weighted Dynamic Networks. IEEE InfoCOM, 2019.

  [2] An Advanced Deep Generative Framework for Temporal Link Prediction in Dynamic Networks. IEEE IEEE Transactions on Cybernetics, 2020.

  [3] High-Quality Temporal Link Prediction for Weighted Dynamic Graphs via Inductive Embedding Aggregation. IEEE TKDE, 2023.

  [4] Temporal link prediction: A unified framework, taxonomy, and review. ACM Computing Surveys, 2023.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
