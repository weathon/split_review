# Finite Scalar Quantization: VQ-VAE Made Simple

- Decision: Accept
- Avg Score: 6.50
- Scores: 6, 8, 6, 6

## Abstract
We propose to replace vector quantization (VQ) in the latent representation of VQ-VAEs
with a simple scheme termed finite scalar quantization (FSQ), where we project the VAE representation down to a few dimensions (typically less than 10).
Each dimension is quantized to a small set of fixed values, leading to an (implicit) codebook given by the product of these sets.
By appropriately choosing the number of dimensions and values each dimension can take, we obtain the same codebook size as in VQ.
On top of such discrete representations,
we can train the same models that have been trained on VQ-VAE representations. For example, autoregressive and masked transformer models for image generation, multimodal generation, and dense prediction computer vision tasks.
Concretely, we employ FSQ with MaskGIT for image generation, and with UViM for depth estimation, colorization, and panoptic segmentation.
Despite the much simpler design of FSQ, we obtain competitive performance in all these tasks.
We emphasize that FSQ does not suffer from codebook collapse and does not need the complex machinery employed in VQ (commitment losses, codebook reseeding, code splitting, entropy penalties, etc.) to learn expressive discrete representations.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This work considers replacing the quantization layer of vector quantized variational autoencoders (VQ-VAE) with a scalar quantization strategy. The goal of VQ-VAE is discrete representation learning, i.e., we want to embed a datapoint in the latent space using an encoder network, and we want the representation in the latent space to belong to a discrete set of finite values (referred to as the codebook). This codebook is learnt by jointly training the encoder and decoder network.

Traditional VQ-VAE approaches consists of a quantization layer, in which the codebook (or the quantization points) is done using K-means clustering or exponential moving average. These approaches have some issues such as codebook collapse, in which the learnt codebook is a very small set of points compared to the latent space. The strategy proposed in this paper replaces the VQ layer by coordinate wise scalar quantization. This drastically reduces the number of hyper-parameters and the codebook size, while still maintaining the reconstruction quality. Quantization is done by first passing it through a bounding function such as $\mathrm{tanh}$ which bounds the dynamic range of the entries to be quantized. This is followed by quantizing the $i^{\mathrm{th}}$ coordinate of the latent representation to one out of $L_i$ values. Here, $i$ varies from $1$ to $d$, where $d$ is the number of channels. Numerical evaluations validate this claim.

Please correct me if I am mistaken in my understanding of the contributions of the paper. I am more than happy to rectify my review if that's the case.

### Strengths
VQ-VAE has been successful in obtaining compact latent representations. However, the VQ layer has some issues such as code under-utilization as mentioned in the summary. This paper proposes a simple strategy that imposes the cubic lattice structure while obtaining the quantization codebook. This leads to much fewer parameters to store.

The simplicity of the proposed approach is quite commendable. It is surprising that this hasn't already been studied before. Even though quantization is a non-linear operation, the VAE network can be trained via back-propagation using the stop gradient estimator.

### Weaknesses
The idea is well described in the paper. My only concern is the novelty of the contribution of the proposed approach. It is surprisingly simple, which raises my question as to what are the limitations of FSQ, and if it has not been explored before, especially since VAEs have been around for a while. 

Can we have any guarantees as to why FSQ performs as good as VQ, even after imposing strict structural constraints? Is there anything particularly special about the tasks considered in the numerical simulations, or can we expect FSQ to perform at par for any application of VAE?

### Questions
I have no critical questions right now, expect for the following.

How does the choice of the squeezing / bounding function, i.e., $\mathrm{tanh}$ affect the performance?

I'd be happy to edit my review post the discussion period.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a new type of discrete tokens used in VQ-VAE named finite scalar quantization (FSQ). The dimension of the VQ-VAE representation is decreased to a low number and each dimension can only take a few scalars. With this design, FSQ is able to achieve the same size of the codebook used in original VQ-VAE with far less parameters. In addition, FSQ does not require complex design like entropy penalty as well. By using these FSQ representation, the models using VQ-VAE can also be trained with FSQ, such as image generation, multimodal generation, and dense prediction computer vision tasks. Experiment results show that FSQ has competitive performance with original VQ-VAE and prove the expressive discrete representations learned by FSQ.

### Strengths
* S1: The method is effective and easy to implement, since no extra complex design is needed.
* S2: The writing of the FSQ design is easy to follow.
* S3: The experiments are extensive. The authors demonstrate the efficiency of the proposed method under various settings.

### Weaknesses
 * W1: The relation between VQ-VAE and FSQ is confusing. Specifically, I do not understand how the FSQ model is trained. Is the FSQ model trained from scratch using the VAE architecture, or is the FSQ model transformed from a pretrained VQ-VAE model in some way. Since MaskGIT is a two stage method, where the first stage is to train a discrete tokenizer, I will regard FSQ as a model trained from scratch. The paper lacks details on the specific architecture used for the FSQ-VAE, making it difficult to assess the novelty of the approach beyond the quantization scheme itself. It's unclear if the encoder and decoder architectures are standard VAE components or if they incorporate specific modifications to accommodate the FSQ representation. This lack of clarity hinders a full understanding of the method's contribution.
* W2: The principle of desigining the shape of the codebook is not given. It seems that the number of levels per channel of the recommended shape is uniform and larger than 5. But there is not a intuitive explanation on why. The paper does not provide a clear justification for choosing a uniform number of levels per channel, nor does it explore the impact of varying the number of levels across different dimensions. This raises concerns about the optimality of the chosen codebook shape and whether it is universally applicable or task-specific. Furthermore, the absence of a theoretical or empirical analysis of the relationship between the number of levels and the representational capacity of the FSQ is a significant gap.

### Questions
Since the paper does not contain the training process of FSQ, I am a little confused about the setting. Here are some questions:

* Q1: As I mentioned in the weakness part, is FSQ used in MaskGIT and UViM trained from scratch? If yes, what is the model architecture and the other hyperparameters like training epochs? And what is the reconstruction and generation ability of FSQ used as a VAE?

* Q2: There is another concurrent work named Lookup Free Quantization [1], which also aims to compress the codebook. Their method directly let the dimension of codebook features become zero, which can also support a larger vocabulary size. Can the authors compare the proposed method with theirs?

I will be very happy to raise my score if these concerns are addresed.

[1] Language Model Beats Diffusion -- Tokenizer is Key to Visual Generation, arxiv 2310.05737

### Soundness
3 good

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper proposes Finite Scalar Quantization (FSQ) to replace the popular VQ-VAE.
Instead of performing cumbersome VQ-VAE optimizations (multiple losses, handling codebook underutilization, etc.), FSQ performs a simple quantization (rounding) of the learned embedding, optimized via the standard STE.
The method is able to reach FSQ performance on several tasks.

### Strengths
1. The paper is clear
2. The approach is somehow original for generative models
3. The method is simple (appears to be much simpler than the VQ-VAE cumbersome training and optimization) with less model capacity and computational complexity
4. Yet the method reaches good performance.

### Weaknesses
1. The main weakness lies in the originality/novelty of the method which appears to be a compressive autoencoder (e.g., [1,2]) applied to generative tasks. As the Method section demonstrates, there are very few (no) technical/theoretical contributions.

2. The results are still (mostly slightly) worse than VQ.

3. The method obviously lacks compression performance since the quantized vectors' indices are insufficient/irrelevant in this case. The indices, unlike in VQ-VAE, do not map to a learned codebook, but rather to a fixed grid, making them less informative for compression tasks and limiting the method's potential in scenarios where efficient data representation is crucial.

### Questions
1. There is an obvious difference between the FSQ and VQ-VAE functionals (rounding vs L2 distance). It would be interesting to see the difference in the quality of the representations (e.g., same class samples should be close(r with FSQ?) in their representations) and not only regarding the optimized metrics.

2. Following 1., it is not clear how the codebook is seen as implicit and not simply defined by the hypercube's samples.

3. How do you explain that extending the model capacity (Sec 3.3) does not result in improvement, especially since the method is still worse than VQ-VAE?

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This paper proposes a simple method called finite scalar quantization (FSQ) to replace vector quantization (VQ) in VQ-VAEs. FSQ projects the representation to very few dimensions (typically less than 10), with each dimension quantized to a fixed set of values. This implies a codebook of the same size as in VQ. Results show that as codebook size increases, FSQ achieves better reconstruction metrics and higher codebook utilization, while these metrics deteriorate for VQ.

### Strengths
1. This paper is written clearly and proposes a straightforward solution FSQ.
2. Using scalar quantization to replace vector quantization in VQ, FSQ method avoids the codebook collapse problem in VQ and does not need auxiliary losses. 
3. Sufficient and concrete experiments demonstrate the effectiveness of the proposed method.
4. The authors make detailed comparisons between the performance of FSQ and VQ.

### Weaknesses
Although I believe this paper meets the bar of acceptance, I still have a few concerns:

1. FSQ's expressive capability is slightly weaker than VQ, and its performance is slightly worse with small codebooks.

2. The paper lacks analysis on the speedup and compression rate brought by the quantization of FSQ.

3. FSQ also faces difficulties in finding proper quantization hyperparameters (dimensions and number of quantization levels).

### Questions
I hope the authors can add some intuitive numerical comparisons to demonstrate the inference speedup brought by FSQ, and emphasize that FSQ does not need the parameters for the codebook.

Additionally, from the results in the paper, we can see that the metrics of FSQ only show significant advantages when the codebook size is greater than 2^10. However, wouldn't such a large size have a low cost-effectiveness for the second stage (I mean the trade-off between parameter size and FID, where a larger codebook may require a larger model to handle)? This will affect the model's practicality.

### Soundness
3 good

### Presentation
3 good

### Contribution
2 fair
