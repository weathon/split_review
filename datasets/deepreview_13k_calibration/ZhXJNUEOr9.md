# Sparling: Learning Latent Representations with Extremely Sparse Activations

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 5, 6

## Abstract
Real-world processes often contain intermediate state that can be modeled as an extremely sparse tensor. We introduce \technique{}, a technique that allows you to learn models with intermediate layers that match this state from only end-to-end labeled examples (i.e., no supervision on the intermediate state).
\technique{} uses a new kind of informational bottleneck that enforces levels of activation sparsity unachievable using other techniques. 
We find that extreme sparsity is necessary to achieve good intermediate state modeling. On our synthetic \digitcircle{} domain as well as the \latexocr{} and \audiomnist{} domains, we are able to precisely localize the intermediate states up to feature permutation with $>90\%$ accuracy, even though we only train end-to-end.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
2

### Summary
This paper theoretically proves that under certain assumptions, the motifs (or latent variables) of a task can be accurately identified by a neural network that is trained end-to-end. More specifically, it provides an upper bound for the motif error when the end-to-end error is low. The paper shows that this kind of motif identifiability can be achieved by enforcing extremely sparse activations in the training process, and validates it on several example tasks.

### Strengths
1.	The paper seems to focus on an interesting problem, i.e., can a neural network automatically identify motifs (latent variables) of a task under the end-to-end training scheme.

2.	The paper theoretically formalizes several sufficient conditions (assumptions) for motif identifiability, and quantifies the motif error in terms of end-to-end error. I really appreciate this kind of theoretical effort.

### Weaknesses
1. The presentation of the paper needs to be improved. It is still not clear what a “motif” is, even after the revision of Figure 1. The current explanation of motifs as the *position of each digit* in the experiments section is insufficient. A more concrete description is needed, including the expected output of the motif encoding layer. For instance, is the motif encoding a tensor? If so, what is the shape of this tensor, and how does it relate to the input and the task? Visualizing this with a clear example at the beginning of the paper would significantly improve understanding. The revised Figure 1, while including tensor dimensions, still lacks a clear visual representation of what the model is expected to learn as a motif. The dots representing motif locations are abstract and do not convey the actual encoding. 

2. The claim that the motif error is small according to Figure 3 is not very convincing, because the experiment lacks comparison with properly designed baselines. The implicit comparison to a non-sparse baseline in Figure 4, as mentioned in the response, is not sufficient. A more direct comparison is needed, for example, against a baseline where the mapping $\hat{g}$ is a random mapping, or even better, a baseline that is trained without the sparsity constraint. This would provide a better understanding of the contribution of the sparsity constraint to motif identifiability. The current comparison only shows that a non-sparse network does not produce motif-like features, but it does not show that the proposed method is superior to other methods that might also achieve motif identifiability.

3. The practical implication of the paper is still limited. The current paper mainly focuses on special tasks that exhibit certain structures (e.g., input noise, sparse input signals). It is not clear whether the assumptions and the theory can be validated on more common tasks such as image classification, e.g., the digit classification on MNIST. The authors' response mentions that MNIST digits do not have information concentrated in small and independent parts of the input, but this explanation should be included in the paper itself, ideally in a dedicated Limitations section. This would help readers understand the scope and limitations of the proposed method.

4. Minor.

(a) Could you add the equation numbers and the line numbers, so that we can refer to specific contents more easily?

(b) In the equation $v_{\hat{m}}(i)=\sum_{i’ \in p_2(i)} \boldsymbol{1}(\hat{m}[i] \neq 0)$, should the $\hat{m}[i]$ on the right hand side be $\hat{m}[i’]$?

### Questions
1.	Could you provide a figure describing the network architecture used in Section 5.1? This would significantly help readers understand the network architecture. Besides, many parts of the architecture follow Deng et al. (2016). Could you explain why these specific design choices are made?

2.	There are some works studying the *decision sparsity* or *sparsity of concepts* encoded by neural networks [c1, c2, c3], without requiring the network itself (e.g., parameters or activations) to be sparse. They have not been discussed in the related work, and I wonder whether/how these works are related to and different from the *sparsity* in this paper.

3.	Most tasks described in this paper have noises in the input, and it seems that the model needs to do denoising when it outputs the correct result. Is the input noise a necessary setting for motif identification?

[c1] Enouen and Liu. Sparse Interaction Additive Networks via Feature Interaction Detection and Sparse Selection. NeurIPS 2022.

[c2] Sun et al. Sparse and Faithful Explanations Without Sparse Models. AISTATS 2024.

[c3] Ren et al. Where We Have Arrived in Proving the Emergence of Sparse Interaction Primitives in DNNs. ICLR 2024.

### Soundness
2

### Presentation
1

### Contribution
3

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
3

### Summary
The paper studies the extent to which sparsity alone can be used to identify latent variables determining an input-output mapping. They provide a theoretical result on sufficient conditions for recovery of the latents, based on extreme sparsity, low end to end error and properties of the data distribution. To enable training models with extreme sparsity the SPARLING algorithm is presented, which is shown to recover latent variables on several synthetic tasks.

### Strengths
* The motivation, goals and contributions of the work are clearly stated and are easy to follow.

* Studying theoretical aspects of recovering latent variables, and more generally interpretability, is important and less explored. The work clearly demonstrates a scenario where interpretable latents can be recovered via a sparsity assumption and further provide evidence where the assumptions break and sparsity is insufficient (LaTeX-OCR).

* The suggested algorithm to induce sparsity seems to be efficient ,simple and applicable in a more general setting than suggested in the present work.

### Weaknesses
 * Some of the notation and formal statements are unclear and hard to follow:
    * In section 2 paragraph 2, square brackets ([d]) denote a set but are then also used to denote dimensions of tensors in the domain of X - why is a tensor not denoted in standard notation? $X \in \mathbb{R}^{N_1\times N_2 \times d}$  
    * The definition of locality, although made intuitive via description with graph convolutions, is hard to understand, partially due to mixing spatial and channel indices. Additionally, the notation for footprint function and motif cell is abused with $p_i$ introduced before.
    * The definitions in section 3.2 are unclear: $v_{\hat{g}(x)}$ is interchanged with $v_{\hat{n}}$ , summation is over $i’$ that doesn’t exist in the summands - can you please clarify?

* The main results, in figure 3, are displayed without any reference baseline. If a simple baseline from any one of the relevant methods in the related work section can be added it can highlight the significance of the method.

* The SPARLING algorithm is presented as a contribution in the main text but then in appendix A it is said to exist in prior work [1] - can the authors please clarify? do the 2 statements refer to the same algorithm, what are the differences between them and what is the contribution of this work? statements in the main text and the appendix should be consistent.

* I found the definitions of error metrics, section 3.2, and of $\alpha$-MOTIF-IMPORTANCE to be confusing - do you think an intuitive explanation through one of the synthetic tasks can be helpful?

### Questions
* The SPARLING algorithm is presented as a contribution in the main text but then in appendix A it is said to exist in prior work [1] - can the authors please clarify? do the 2 statements refer to the same algorithm, what are the differences between them and what is the contribution of this work? statements in the main text and the appendix should be consistent.

* I found the definitions of error metrics, section 3.2, and of $\alpha$-MOTIF-IMPORTANCE to be confusing - do you think an intuitive explanation through one of the synthetic tasks can be helpful?

[1] Improved modeling of rna-binding protein motifs in an interpretable neural model of rna splicing, Gupta et. al.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2

### Summary
This paper addresses problems in representation learning and interpretability, toward understanding when and how black box models can correctly learn sparse intermediate activations, or "motifs". The central modeling assumption is that many real-world problems can be modeled by a generative process whereby the data come from first identifying a sparse set of higher-level somatic motifs, which is then used to create higher resolution raw data. This paper makes theoretical progress through its Motif Identifiability Theorem.

### Strengths
The paper identifies an interesting setting for making progress on the interpretability of end-to-end neural networks. While the tasks in the paper are synthetic, they were designed with a long-term research objective in mind, such as being able to identify motifs in difficult problems like RNA splicing. The main strains of the paper are in the originality of this setting and in having theoretical guarantees that it is possible to be addressed. The paper is overall well-written and clear even to a reader who is not deeply familiar with the sub-area.

### Weaknesses
The main weaknesses of the paper are that it is the first step on a longer-term research problem, and the particular tasks that are able to be addressed now are highly synthetic and unrealistic. The locality constraint, while theoretically motivated, may be overly restrictive in practice, limiting the model's ability to capture complex, non-local dependencies that are often present in real-world data. The paper does not explore the sensitivity of the method to the choice of the latent layer's dimensionality, which could significantly impact the quality of the learned motifs. Furthermore, the paper lacks a thorough analysis of the computational cost associated with the proposed method, especially as the size and complexity of the input data increase.

### Questions
Would the method work with more complicated model structures such as with more layers? How would one know which layer should be the one to extract specific latent motifs?

### Soundness
3

### Presentation
3

### Contribution
2
