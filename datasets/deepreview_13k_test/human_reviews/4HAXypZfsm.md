# Supervised Disentanglement Under Hidden Correlations

- Decision: Reject
- Scores: 6, 5, 3, 6

## Abstract
Disentangled representation learning (DRL) methods are often leveraged to improve the generalization of representations. Recent DRL methods have tried to handle attribute correlations by enforcing conditional independence based on attributes. However, the complex multi-modal data distributions and hidden correlations under attributes remain unexplored. Existing methods are theoretically shown to cause the loss of mode information under such hidden correlations. To solve this problem, we propose Supervised Disentanglement under Hidden Correlations (SD-HC), which discovers data modes under certain attributes and minimizes mode-based conditional mutual information to achieve disentanglement. Theoretically, we prove that SD-HC is sufficient for disentanglement under hidden correlations, preserving mode information and attribute information. Empirically, extensive experiments on one toy dataset and five real-world datasets demonstrate improved generalization against the state-of-the-art baselines. Codes are available at anonymous Github https://anonymous.4open.science/r/SD-HC.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The paper introduces a novel supervised disentanglement method, SD-HC, designed to address hidden correlations in multi-modal data, which traditional DRL methods often overlook. SD-HC focuses on preserving essential mode information within attributes by minimizing mode-based conditional mutual information, thus achieving better disentanglement and predictive accuracy under both hidden and attribute correlations. The authors theoretically prove that mode-based conditional mutual information minimization is both necessary and sufficient for effective disentanglement in complex, correlated datasets.

### Strengths
- This paper establishes a novel theory for supervised disentanglement with hidden correlations. It consists of both necessary and sufficient conditions, serving as a significant improvememt for existing works.
- The experiments are comprehensive and the results are good enough.

### Weaknesses
- The motivation of the problem setting is not clearly discussed. In Figure 2, to study the hidden correlations among attributions, why not directly study $a_k$ and $a_{-k}$? The role or advantage of introducing the variable $m_k$ is not clear for me.
- It seems that the performance of SD-HC heavily relies on the mode label estimation. First, in real applications, how to determine the number of modes $N_m$? In addition, for complex data pattern, the data representations are not high-quality and the clutering is not accurate accordingly. In such case, is there any techniques to guarantee good performance?
- There are some ambiguous concepts in this paper. For example, 1) "Data mode". I do not find its concrete definition. This term is not common in machine learning and its meaning varies with contexts. 2) "Multi-modal". It seems not to refer to the commonly used meaning, such as text and image. More strict definitions is required to make this paper more clear.
- The writting needs to be further improved. For example, in line 155, $c^a$ and $c^m$ should be boldface.

### Questions
- From Section 3 and 4, only one attribution mode is considered. For more complex or practical scenarios, all attributions may have their mode variables. Whether the SD-HC can efficiently and effectively address them?

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
This paper addresses the problem of disentangled representation learning in the presence of hidden correlations, which are common in real-world data. The authors consider a multi-modal data distribution where certain attributes may induce complex modes correlated with other attributes. To tackle this issue, they first investigate the necessary and sufficient conditions for supervised disentanglement under the proposed data-generating process. Subsequently, they introduce the SD-HC method for learning disentangled representations with hidden correlations. The proposed method is validated on both synthetic data and five real-world datasets.

### Strengths
1. The paper studies an important problem in disentangled representation learning by considering hidden correlations, which are prevalent in real-world data.
2. The experimental evaluation is thorough, including both synthetic and real-world datasets.

### Weaknesses
1. The major issue lies in the lack of detailed theoretical explanation:
   - The causal graph presented in Figure 3 is confusing. Since $z = f(x)$ is a function of $x$, there should be a directed edge from $x$ to $z$. However, the graph shows $z$ as a parent of $x$, which is misleading.
   - The claim that "mode-based conditional mutual information (CMI) minimization is the necessary and sufficient condition for supervised disentanglement" lacks a detailed formal list of necessary assumptions. This claim heavily depends on the data-generating process, and the specific assumptions should be clearly highlighted.
   - The link between Proposition 2 and the independence requirement in Definition 2 is unclear. Proposition 2 appears to be a mutual information result that is not directly related to causality. Although the authors attempt to bridge this gap in Lines 242 to 244, a more rigorous analysis with detailed assumptions and proofs is needed.
2. The mode label estimation step is confusing. In this step, mode labels are estimated by clustering on the corresponding attribute. Consequently, there would be no confounders that affect $m_k$ and $a_{-k}$ while not affecting $a_k$, which violates the assumptions depicted in Figures 2 and 3.
3. The paper lacks detailed explanations regarding the choice of attributes and the modes in the real-world datasets. Providing more context would help in understanding the experimental results better.
4. There are typos in Lines 332 and 336. "Figure 7a" and "Figure 7b" should be replaced with "Figure 5a" and "Figure 5b," respectively.

### Questions
See the weakness part.

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
3

### Summary
The paper introduces a method called Supervised Disentanglement under Hidden Correlations (SD-HC) to improve disentangled representation learning (DRL). Traditional DRL methods struggle with hidden correlations in multi-modal data. SD-HC addresses this by discovering data modes under certain attributes and minimizing mode-based conditional mutual information. This approach ensures disentanglement while preserving mode and attribute information. The paper provides theoretical proofs and empirical evidence showing SD-HC outperforms existing methods on various datasets.

### Strengths
1. The studied problem is open and important -- latent confounding is prevalent and proper efforts are deserved to this problem.
2. The experiments are extensive and the proposal looks promising.

### Weaknesses
1. The paper may benefit from a clear introduction of the task, especially the instantiation with real-world examples. Although I appreciate several examples present in the paper, a coherent running example would aid the readability much more if it includes the objective of the task, the problem of the hidden correlation, and the instantiation of the proposal in this example.
2. The graphical model Figure 2 is not well-defined for me. $z$ variables are functions of the observed data $x$. How would they appear in the true data-generating process? To me, this is not even a causal graph -- if I intervene on attribute $a_{i}$ in the true data-generating process, this influences will not be blocked by estimated variables $z$'s.
3. The main arguments are elusive to me. Especially, what does Proposition 2 imply? Its connection to the disentanglement is unclear. To me, it states that if you can find the modality variable $m_{1}$ and condition on it, the associated estimated variable $z_{1}$ will be d-separated from other attributes $a_{-1}$. First, there is no guarantee to discover the true modality variable $m_{1}$ (the proposal is somehow heuristic); second, how would this lead to the disentanglement conclusion?

### Questions
Please refer to the weaknesses section.

### Soundness
2

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
This paper addresses disentangled representation learning for data with correlated, multimodal attributes and proposes Supervised Disentanglement under Hidden Correlations (SD-HC), which infers hidden modes within attributes to achieve disentanglement while preserving essential information by minimizing mode-based conditional mutual information (CMI). The proposed approach is validated through theoretical analysis and experiments on illustrative toy data, image data (colored MNIST), and time series datasets (UCI-HAR, RealWorld, HHAR, and MFD), showing improved performance over existing methods.

### Strengths
(Disclosure: I've reviewed this paper before, and I used a PDF comparison tool to check the differences.)

- This paper studies a challenging problem in disentangled representation learning.
- The motivating example in Figure 1 is easy to follow and highlights the need for this method. It also links to the experiments on the human activity recognition task in Section 5.
- The symbols and technical terms are properly defined. The definitions of disentangled data generation process and disentangled representations are clearly stated in Definitions 1 and 2.
- The paper provided sufficient empirical evidence on both image and time series data.

### Weaknesses
- The connections between the theory and learning are still unclear to me. A better way to characterize the proposed method is to say something like "Under x assumptions, given x supervision, when x loss is optimized or x condition is satisfied, the learned representations are disentangled in the sense of definition x".
- The propositions and corollaries can be written in a more self-contained manner, even if the symbols have been defined in the text above.

### Questions
- (minor) Why renaming? The current name SD-HC sounds more like a problem setting, not a specific method.

### Soundness
3

### Presentation
3

### Contribution
2
