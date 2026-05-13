# Non-negative Contrastive Learning

- Decision: Accept
- Scores: 5, 6, 6, 6

## Abstract
Deep representations have shown promising performance when transferred to downstream tasks in a black-box manner. Yet, their inherent lack of interpretability remains a significant challenge, as these features are often opaque to human understanding. In this paper, we propose Non-negative Contrastive Learning (NCL), a renaissance of Non-negative Matrix Factorization (NMF) aimed at deriving interpretable features. The power of NCL lies in its enforcement of non-negativity constraints on features, reminiscent of NMF's capability to extract features that align closely with sample clusters. NCL not only aligns mathematically well with an NMF objective but also preserves NMF's interpretability attributes, resulting in a more sparse and disentangled representation compared to standard contrastive learning (CL). Theoretically, we establish guarantees on the identifiability and downstream generalization of NCL. Empirically, we show that these advantages enable NCL to outperform CL significantly on feature disentanglement, feature selection, as well as downstream classification tasks. At last, we show that NCL can be easily extended to other learning scenarios and benefit supervised learning as well.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper propose Non-negative Contrastive Learning (NCL), which is inspired by Non-negative Matrix Factorization (NMF), to derive interpretable features. Specifically, NCL add a non-negative transformation at the end of a standard encoder to generate non-negative features. The paper also demonstrates the advantages of NCL by experiments.

### Strengths
The writing of this paper is clear, and the descriptions and justifications of the methods are comprehensible.

### Weaknesses
1. When presenting key arguments in the paper, some claims lack proper foundation, while others are based solely on partial visualization results from a specific dataset. I remain somewhat skeptical of these points.
2. The results in Table 2 of the article indicate that the improvement from the proposed method is rather limited. I remain uncertain about the method's true efficacy.

### Questions
1. In the first paragraph of sec 1, the authors show top activated examples along each feature dimension to demonstrate the interpretability of the features. Is this a common practice? Why is this approach considered reasonable?
2. In the second paragraph of sec 2.2, why does the rotational symmetry in the optimal solution hurt the performance?
3. The proposed method, simply adding a relu layer after the encoder, seems to be too easy to improve the performance.

### Soundness
2 fair

### Presentation
2 fair

### Contribution
2 fair

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The manuscript introduces a new self-spervised paradigm known as non-negative contrastive learning (NCL). Drawing inspiration from spectral contrastive learning (SCL) by HaoChen et al., 2021 and non-negative matrix factorization (NMF), the authors proposed a contrastive loss that enforces non-negativity constraints on the extracted features.

The authors demonstrate that, assuming minimal class overlap, NCL has the potential to learn a set of sparse features with low correlation. Under a one-hot representation, NCL achieves orthogonality among its features (Theorem 4). Furthermore, when at least one sample is uniquely assigned to each class, NCL learns a set of distinguishable and disentangled features (Theorem 5).

To validate the effectiveness of NCL, the authors conducted experiments on three benchmark datasets: CIFAR-10, CIFAR-100, and ImageNet-100, comparing it with a conventional contrastive learning methods, i.e. SimCLR. Across all datasets, NCL's features exhibit greater sparsity, consistency, and less entanglement, leading to improved representation of class identity in classification tasks.

### Strengths
- The manuscript is generally well written. 
- The proposed contrastive learning paradigm is theoretically grounded, with a connection to NMF problem.

### Weaknesses
 - **Novelty:** While the author has made a great effort to establish a connection betweenNMF and contrastive learning in the NCL approach, it appears that NCL can be seen as an extension of SCL with non-negativity constraints and similar justifications and proofs.

- **Contribution:** The reported results in Table 2, and Figure 5 do not convincingly support a significant improvement brought about by NCL compared to the classical contrastive learning method. Furthermore, the absence of a direct comparison between NCL and SCL is notable.

- **Generality and applicability of NCL's representation:** While the authors have theoretically demonstrated that NCL can yield sparse and less entangled representations suitable for downstream tasks like clustering and classification, the critique is that the suggested definition for an optimal and interpretable representations does not necessarily covers the broader goal of capturing all latent factors within the data structure. In many practical applications, e.g. in VAE studies or mixture modeling, the aim is to obtain comprehensive representations that also cover continuous and non-sparse variabilities, which remains unaddressed in this work.

I appreciate the problem addressed by the author and introducing the constrained contrastive learning, which I find intriguing. The manuscript seems to have established a reasonable foundation. However, I think there are certain concerns that need to be addressed. I am open to revising my evaluation pending the author's response.

### Questions
- It seems there might be a typo error in the proof of Theorem 2. It appears that the negative sample $x^-$ should be the positive one, $x^+." right?

- If the primary objective of introducing non-negativity constraints is to encourage sparser representations, have you considered whether regularizing SCL loss with a sparsity regularizer might produce similar results?

- Could you clarify whether the results presented in Tables 1 and 2, as well as Figure 5, are based on a single round of experimentation or multiple iterations? When the text mentions *"on average"* it would be helpful to specify the number of runs that the average is calculated over.

- In section 4.1, Results, it is mentioned that *"The advantage is larger by considering the top features... since learned features also contain noisy dimensions."* This statement appears to be somewhat contradictory to the claim of a less-entangled representation.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The paper proposes the use of non-negative transformations on learned features in contrastive learning, which it calls Non-negative Contrastive Learning (NCL). It shows that non-negativity improves feature interpretability, sparsity and orthogonality compared to traditional CL. For each of these properties, the paper derives relevant guarantees for the ideal features, under certain assumptions of the data generating process. The paper also includes the results of experiments to show that NCL is superior to CL in feature disentanglement, feature selection and downstream classification.

### Strengths
The paper derives several useful guarantees for NCL under ideal circumstances. Although I did not delve deep into the derivations, they seem sound based on the non-exhaustive checking I did.

The proposed benefits of NCL over CL are further backed up by the experimental results. Although the derivation are in-depth, the proposed modification to CL is fairly simple to understand and implement. Whilst some parts would benefit from a more thorough explanation, the paper is generally well-written.

### Weaknesses
A few sections required re-reading and/or reading other related papers to fully comprehend. For example, in Section 2.1 Preliminary on Contrastive Learning, the notation, the ideas about the natural data vs. augmentation data, population data vs. empirical data, positive samples and negative samples could be introduced more thoroughly, as is done in HaoChen et al. (2021). I appreciate that this may be due to lack of available space.

In section C.1, it is stated that the feature transferability to downstream classification is evaluated without using the projector. Does this mean that the features used are not non-negative? Section 4.3 claims that the downstream classification “aligns well with the common belief that disentangled features are more robust against domain shifts”, and yet the empirical and theoretical justification for the features being disentangled is based on the non-negative features (after the projector). This appears inconsistent.

The theoretical guarantees derived in the paper are based on assumptions. There is insufficient discussion of the applicability of these assumptions, and the guarantees, when real world data is used and the learned features are not ideal. For example, for each feature (representing a latent class), is there at least one sample in the data sets used that (approximately) only has that feature activated? Is learning something close to the ideal features reliant on a feasible amount of training data and a feasible amount of augmentations?

It is unclear to me why the feature selection task is chosen to show the sparsity of the NCL solution. Why is the sparsity evidenced by performance with a subset of the original features rather than a subset of the learned features?

In Appendix C.3, the derivation of lower bound of mutual information as the NCE loss should be more thorough, or cite a paper with a more closely aligned derivation, as it has a different form to the original paper (Oord et al., 2018). Also, the NCE loss does not include positive samples as it does in the main text. Is this intentional?

The expectation in equation 1 appears to be over just positive samples.

The paper would be more reproducible if the code were made public.

Experiment 4.2 SPARSITY → FEATURE SELECTION

It is not clear that this task is something that would be done in practice: is performance better when subsetting 512 features down to 256, compared to training the model with 256 features originally? Or is there a practical reason for subsetting rather than training a smaller model?

It is clear why NCL would lead each sample to have a more sparse representation, on average, but not why this would lead to the model being more reliant on fewer features, overall (or, at least, this is not clear to me from the paper). Even if it does so empirically, it’s not clear why we should expect this.

Considering both these points, this experiment does not strongly support the purpose of the paper.

4.3 IN-DOMAIN AND OUT-OF-DOMAIN DOWNSTREAM CLASSIFICATION

The performance when using the projector outputs is not significantly better for NCL than CL. It is only significantly better when using the encoder outputs. As the encoder outputs perform significantly better than the projector outputs, and the projector outputs are the features argued to be disentangled/interpretable, downstream prediction interpretability (for which you would need to use the projector outputs) comes at the cost of performance (for which you would be better off using the encoder outputs). As such, the experiment does not show that NCL leads to a gain in interpretability without a cost in performance, and so does not strongly support the claims of the paper.

Minor point:

Q3/A3

Whilst I appreciate the authors response, the response is more theoretical than I expected. I also appreciate that the latent classes may not be knowable. However, I am still curious: without considering whether it corresponds to a latent class, how many features are there which have at least one sample where (approximately) only that one feature is activated? If this does not seem to happen empirically, it would make for a nice discussion point of the limitations of the theoretical results (in this case: Theorem 5) in practical applications.

### Questions
In section C.1, it is stated that the feature transferability to downstream classification is evaluated without using the projector. Does this mean that the features used are not non-negative?

For each feature (representing a latent class), is there at least one sample in the actual data sets used that (approximately) only has that feature activated (as in assumption of Theorem 5).

Is learning something close to the ideal features reliant on a feasible amount of training data and a feasible amount of augmentations?

Why is the sparsity evidenced by performance with a subset of the original features rather than a subset of the learned features?

In Appendix C.3, the NCE loss does not include positive samples as it does in the main text. Is this intentional?

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
The authors propose a novel contrastive learning method called "nonnegative contrastive learning", which takes its name from nonnegative matrix factorization. Using an output activation function for the learned features, e.g. $ReLU(f(\mathbf{x}))$, the authors make the connection of the nonnegative matrix factorization minimization loss to the spectral contrastive learning loss.
The novel objective should lead to more interpretable features.

### Strengths
- Interpretability of ML methods and learned representations is an important problem. For supervised and self-supervised learning. Therefore, I like the idea of the paper and its research direction.
- Combining contrastive learning and nonnegative matrix factorization is a cool idea and innovative.
- The paper is well written and a good read. Interesting!

### Weaknesses
 - In my opinion, running experiments over multiple seeds and reporting the mean and standard deviation is essential and. necessary. For me, this is an important point. And to me, it has to be fulfilled to be accepted.
- The y-axes in Figure 5 give a biased/wrong impression of the performances of the different models, in my opinion. In combination with the lack of standard deviations, it is difficult to evaluate the performance differences of the two methods.
- I understand that evaluating disentanglement on real-world datasets is challenging given the lack of ground truth. Another possible way of really evaluating the disentanglement of the learned representations would have been the use of a toy dataset for this experiment. The known problems with estimating MI and not only a lower bound of it make it difficult to evaluate the results for this experiment.



### Questions
- what is the connection/link between semantic consistency and clustering accuracy? I could not find any details on that in the manuscript.
- Is the CL objective also trained with the spectral loss function? The results in the original paper seem to indicate that it does not lead to the same performance as in the original SimCLR paper. Maybe it would make sense to include the results generated by the standard SimCLR objective.
- are there more interpretability results than the qualitative results provided in Fig. 1?
- In sec. 4.2 you describe the feature selection procedure based on the TA. Do the results hold if you take the sum over absolute feature values, e.g. $ TA_i (f) = \sum_x \tilde{f}_i (x)$? Given the nonnegative constraints of the NCL features, the metric seems more tailored towards NCL than CL.

### Soundness
2 fair

### Presentation
3 good

### Contribution
3 good
