# Beyond Disentanglement: On the Orthogonality of Learned Representations

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 3, 5, 8

## Abstract
Evaluating learned representations independently of designated downstream tasks is pivotal for crafting robust and adaptable algorithms across a diverse array of applications. Among such evaluations, the assessment of disentanglement in a learned representation has emerged as a significant technique. In a disentangled representation, independent data generating factors are encoded in mutually orthogonal subspaces, a characteristic enhancing numerous downstream applications, potentially bolstering interpretability, fairness, and robustness. However, a representation is often deemed well-disentangled if these orthogonal subspaces are one-dimensional and align with the canonical basis of the latent space – a powerful yet frequently challenging or unattainable condition in real-world scenarios – thus narrowing the applicability of disentanglement. Addressing this, we propose a novel evaluation scheme, Importance-Weighted Orthogonality (IWO), to gauge the mutual orthogonality between subspaces encoding the data generating factors, irrespective of their dimensionality or alignment with the canonical basis. For that matter, we introduce a new method, Latent Orthogonal Analysis (LOA), which identifies the subspace encoding each data generating factor and establishes an importance-ranked basis spanning it, thereby forming the foundational bedrock for IWO. Through extensive comparisons of learned representations from synthetic and real-world datasets, we demonstrate that, relative to existing disentanglement metrics, IWO offers a superior assessment of orthogonality and exhibits stronger correlation with downstream task performance across a spectrum of applications.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper considers the question of evaluating the quality of disentangled representations with respect to the orthogonality of factors. The authors propose latent orthogonal analysis used to devise a new metric called importance weighted orthogonality. The method is evaluated on several datasets and shows promising results.

### Strengths
The research question is strong and to the best of my knowledge this problem is still open at large, and so any advancement on this front is highly important. Another strength is the relative simplicity of the approach, involving basic neural networks and standard linear algebra operations. The results are also compelling, although somewhat basic, in my opinion.

### Weaknesses
The main weakness of this submission is the clarity of exposition. In particular, Sections 2 and 3 could be improved significantly. For instance, the illustration in Fig. 1 is unclear. I believe the authors could do better by considering a 2D case instead of 3D, minimizing the use of colors and angles in the figure. Further, several crucial algorithmic components are described in a minimal fashion with supporting equations,illustrations, or pseudo-code. For example, the text above Eq. (2) and the text above Eq. (4). Given that the proposed method does not seem to be overly complex, I find it disappointing that its description is somewhat vague.

Another weakness is the evaluation section. Evaluating disentangled factors is a long-standing problem in representation learning. In particular, there are established benchmarks and papers focused on this particular problem. While I am not an expert on this issue specifically, I would assume that suggesting a new metric that is arguably better than others should be motivated better and empirically justified with more than two real-world datasets and a few toy examples.

### Questions
See above

### Soundness
3 good

### Presentation
1 poor

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
A new assessment scheme is introduced to measure disentanglement in latent space in terms of orthogonality between subspaces. The assessment builds on an decomposition methodology which projects the original latent encodings into incrementally smaller subspaces through linear neural models. The empirical analysis validates the proposed assessment scheme against existing disentanglement metrics on synthetic and benchmark datasets.

### Strengths
S1) Motivations behind the paper are solid: too strict definitions of disentanglement as projection into single orthogonal dimensions are bound to fail in realistic settings. The idea of broadening the definition to orthogonal subspaces, while not being completely novel, is developed here through an approach which is original.

S2) The technical contribution seems also solid, modulo some points which are not made entirely clear in the presentation. However, the overall methodology is convincing from the perspective of correctness and adequacy of the technical solutions. 

S3) The paper is well organized and mostly of good presentation quality.

### Weaknesses
W1) While presentation quality is generally adequate, the paper misses to convey all the necessary details to facilitate reproduction of the method and of the study. This lack of technical detail in the main body is not compensated by the availability of appendices, supplementary materials or code. One key aspect that is unclear to me is how one is expected to identify the generative factors set $z_1,\dots, z_K$ and how such $K$ is determined in general. The method involves training a potentially large amount of regressors and little information is provided on how this is done in practice (e.g. how much should the training be pushed in terms of regression error? What are the stopping conditions? How are the linear model initialised?).

W2) The positioning with respect to the literature is on the weak end. The paper misses to discussion and cite works formalising weaker forms disentanglement [A, B, C]. In particular, it would seem relevant to discuss the relationship between the proposed approach and those building on (and measuring) linear symmetry-based disentanglement [B,D].

W3) While the experiments are generally well-designed, the evidence they provide does not seem enough to support the major claims of this paper. As long as one departs from the ideal setting, it is difficult to assess the added value of IWO over DCI and MIG. Additional experiments are needed on more challenging datasets, such as ModelNet40 and COIL-100, possibly enlarging the scope of methods to compare with by including those in [B,D]. It would also be of help to qualitatively explore the impact of the proposed methodology, e.g. by exploring the effects of manipulating the representations over the relevant subspaces “suggested” by the metrics. 

W4) The proposed methodology seems very computationally involved. I am using the word “seems” as the paper lacks a comparative assessment of the cost of the method. This should be done while considering more realistically sized problems, involving latent spaces of non-trivial size.

### Questions
Q1) Can the Authors please clarify how generative factors  $z_k$ are selected for the purpose of implementing the method in general (see W1)?

Q2)  Can the Authors please discuss the relationship with linear symmetry-based metrics?

Q3)  The empirical analysis would be substantially strengthened by adding new experiments on as ModelNet40 and COIL-100, considering also computational costs? 

Q4) I am a bit puzzled by the negative correlation values in the experiments: is this classical linear correlation? Because some methods seem to be highly negatively correlated (which is still somehow a form of correlation).

### Soundness
3 good

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors first propose Latent Orthogonal Analysis(LOA), a method that can identify latent subspaces for different factors of variation from data. To estimate the mutual orthogonality between subspaces learned with LOA, they then propose importance-weighted orthogonality (IWO), a metric that can do the measurement on disentanglement by investigating the magnitude of the projections from different subspaces onto each other. This is achieved by multiplying the basis matric of one subspace with a diagonal matrix that defines the importance of each dimension w.r.t. the other subspace.

They empirically evaluate IWO on multiple datasets that are commonly used in disentangled representation learning, and they show that their metric that can outperform prior metrics such as MIG or DCI-D.

### Strengths
This paper is well-structured and clearly written. It is easy to understand what problem they try to tackle in this paper. Even though the metric study on disentangled representation learning is not a completely new field, I believe it is still worth thinking of how we evaluate the orthogonality between different subspaces that encode different factors of variation. 
In their methodology, the authors provide detailed and sound math derivation on their LOA and IWO approach.

### Weaknesses
My main concern is about the insufficiency of evaluation. Give that $\beta$-TCVAE was a few years ago and there have been a large number of variants of VAEs that do disentangled representations, I would hope that the authors can implement a few more models for comparison. In addition, there are also very commonly used datasets that were not considered here, e.g. CelebA, Shape3D, Clevr, etc. I would like to see results on these more complex data.

### Questions
1. I wonder why the $\Delta$ L can be used to measure the importance. Could you justify it in more detail?
2. Is the reason that you choose to only apply linear projection using $W_{1:L}$ is technical difficulty or indeed conceptual purpose?

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors propose a novel metric for evaluating disentanglement of learned representations. The method consists of training a Linear Neural Network, essentially an MLP without nonlinearities with decreasing dimensionalities, for each ground truth factor. The objective function involves training (potentially non-linear) predictor heads on top of each hidden layer. Using QR decomposition on the learned NN weights together with loss estimates from each predictor, the authors estimate basis vectors for each ground-truth factor, together with their importance weightings. By computing such vectors for each g.t. factor they estimate both the subspaces in the learned latent space and compute a measure of orthogonality between subspaces for dfiferent g.t. factors.

Usefulness of the metric is evaluated on both synthetic and real data.

### Strengths
- IWO can be used in scenarios where a ground truth factor can be aligned with exactly one latent dimension
- the proposed metric actually correlates with downstream task performance

### Weaknesses
 - only 2 datasets and models (as compared to e.g., Locatello et al. 2019) are compared in Section 4.3. Please consider using all the 7 datasets from *disentanglement_lib,* otherwise the choice seems a bit arbitrary
- Figure 1 is quite difficult to grasp. I understand that the concept is not trivial to present (and the caption is already lengthy), but maybe you could consider extending/rewriting the caption to make it clearer? Perhaps in a step wise manner (multiple figures). I find it crucial for conveying the idea of your paper. If you lack space I believe figure 3 could be compressed/removed instead

### Questions
The sub-optimal performance of Explicitness for the perfectly disentangled case could stem from overfitting. How do the authors handle this problem with their metric? What were the train/test splits used for the experiments? How sensitive is the metric to smaller sample sizes?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
