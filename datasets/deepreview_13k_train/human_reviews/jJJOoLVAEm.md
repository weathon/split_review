# Bayesian Enhancement Models for One-to-Many Mapping in Image Enhancement

- Decision: Reject
- Scores: 5, 5, 3, 6

## Abstract
Image enhancement is considered an ill-posed inverse problem due to its tendency to have multiple solutions. The loss of information makes accurately reconstructing the original image from observed data challenging. Also, the quality of the result is often subjective to individual preferences. This obviously poses a one-to-many mapping challenge.
To address this, we propose a Bayesian Enhancement Model (BEM) that leverages Bayesian estimation to capture inherent uncertainty and accommodate diverse outputs. 
To address the noise in predictions of Bayesian Neural Networks (BNNs) for high-dimensional images, we propose a two-stage approach. The first stage utilises a BNN to model reduced-dimensional image representations, while the second stage employs a deterministic network to refine these representations.
We further introduce a dynamic \emph{Momentum Prior} to overcome convergence issues typically faced by BNNs in high-dimensional spaces.
Extensive experiments across multiple low-light and underwater image enhancement benchmarks demonstrate the superiority of our method over traditional deterministic models, particularly in real-world applications lacking reference images, highlighting the potential of Bayesian models in handling one-to-many mapping problems.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper presents a Bayesian enhancement model designed to address uncertainty and provide a range of solutions for image enhancement tasks. The method begins by utilizing a Bayesian neural network to model image representations in a reduced-dimensional space, followed by a deterministic network for further refinement. Additionally, the authors introduce a dynamic Momentum Prior to mitigate convergence challenges. Experiments are conducted on tasks involving low-light and underwater image enhancement.

### Strengths
1. Image restoration is an ill-posed problem, and modeling the inherent uncertainty while accommodating diverse outputs is an intriguing and valuable challenge.
2. It seems reasonable to use BNN to tackle this issue.
3. The paper provides a clear and detailed description of the proposed method.  the experiments conducted are thorough and well-structured.

### Weaknesses
1. Why choose low-light image enhancement and underwater image enhancement? Denoising and super-resolution seem to be two more typical tasks. How does the proposed method perform on these two tasks? Besides, how does the proposed method perform in image dehazing, another typical image enhancement task?
2. What is the reason for the missing data in Table I, II and III, and how were the results of the comparison methods obtained?
3. There is a lack of quantitative analysis of the predicted uncertainty.

### Questions
1. My main question is why were LLIE and UIE selected as the two tasks? As far as I know, currently there are no comprehensive datasets available for these tasks. 
2. The reference images for LLIE and UIE may be inaccurate; how does the proposed method tackle this issue?

### Soundness
3

### Presentation
2

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
This paper presents a novel two-stage framework to address the one-to-many mapping problem in image restoration. In the first stage, the authors employ a Bayesian Neural Network (BNN) to capture inherent uncertainty and accommodate diverse outputs in low-dimensional image representations. In the second stage, a Deterministic Neural Network (DNN) is used to refine the output from the first stage. Additionally, the authors introduce a momentum prior to accelerate the convergence of the BNN. The experimental results demonstrate that the proposed method achieves superior performance in low-light enhancement and underwater image enhancement tasks.

### Strengths
The method presented in the article is interesting, particularly in its use of Bayesian Neural Networks (BNNs) to address the one-to-many mapping problem. The experimental results indicate that BNNs can effectively generate multiple clear images. Moreover, the authors achieve state-of-the-art (SOTA) performance, demonstrating the effectiveness of their proposed approach. Additionally, the qualitative visual results show a significant improvement in visual quality with the proposed method.

### Weaknesses
In the low-light enhancement task, the method presented in [1], published in ECCV 2024, outperforms the proposed approach. For instance, the PSNR and SSIM values for [1] on the LoL-v1 dataset are 27.35 and 0.883, respectively, while the proposed method achieves PSNR and SSIM values of 26.83 and 0.877. The performance of [1] is calculated on results without GT mean.

Furthermore, in the context of underwater image enhancement, the authors only utilized a LR-GT paired dataset to demonstrate the superiority of their method, which is inadequate. Recent papers on underwater image enhancement, such as [2] and [3], provide LPIPS and FID metrics for comparison. Therefore, the authors should include a more comprehensive comparison to strengthen their claims. The lack of LPIPS and FID metrics makes it difficult to assess the perceptual quality and fidelity of the enhanced images compared to state-of-the-art methods. The reliance on only paired data also limits the generalizability of the findings, as real-world underwater images often lack perfect paired ground truth data.

The framework of the method is unclear. The authors should provide a detailed structure of DNN and BNN in the main paper or in the supplementary material, such as model shape, the level of model, the main modules, how many main modules each level contains, etc. The description of the BNN is particularly vague, lacking details on the specific type of Bayesian network used (e.g., variational inference, Markov Chain Monte Carlo), the prior distributions over the weights, and how the uncertainty is quantified and propagated through the network. Without these details, it is difficult to reproduce the results or assess the validity of the approach.


### Questions
The author proposes a reduction function to compress high-dimensional image data. However, for image restoration task, compression is a risk operation since it may loss the information of image. How does this paper compensate for this lost information? 

In Section 3.3, the authors mention using reference or no-reference indicators to select the top k candidates. However, it is unclear how the final result is chosen from these candidates when calculating the metrics.

There are some doubts about the experimental results. Firstly, for paired dataset, why did the author use GT images to find better results?
 Using GT to find a better may be inappropriate, since GT is only used to evaluate the effectiveness of the method. If good results are found using GT, the performance may be better. Meanwhile, for underwater image enhancement task, why did the author rely on UIQM and UCIQE to get better results? Because these metrics are used to evaluate the performance of their proposed method, if the author use these metrics to select results, it may inevitably lead to the restoration results performing well on UIQM and UCIQE.

As mentioned in paper, the author train multiple sets of network weights or even multiple networks, where each set is capable of predicting one of the potential targets. This leads to a linear increase in the number of parameters, computational complexity, and running time of this method. Therefore, the author should add comparative experiments on the number of parameters, computational complexity, and running time.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
- This paper raises the issue that image enhancement processes, such as LLIE and UIE, involve a **one-to-many problem**, and introduces BNN to address it.
- To ensure stable training of the BNN, this paper introduces the **momentum prior**.

### Strengths
- This paper introduces a two-stage design that leverages the strengths of both BNNs and DNNs.
- The mathematical formulas are clear and easy to understand.

### Weaknesses
 - This paper raises the issue that image enhancement processes, such as LLIE and UIE, involve a **one-to-many problem**, and introduces BNN to address it.
- To ensure stable training of the BNN, this paper introduces the **momentum prior**.

### soundness:
 3

### presentation:
 1

### contribution:
 2

### strengths:
 - This paper introduces a two-stage design that leverages the strengths of both BNNs and DNNs.
- The mathematical formulas are clear and easy to understand.

### weaknesses:
 - The Bayesian prediction process is impractical. For instance, the K=100 setting used in the paper requires 100 inferences, leading to high computational costs. While the paper draws comparisons to diffusion models, diffusion models provide methods to streamline the inference process, whereas the approach proposed in the paper does not seem to offer such possibilities. The lack of a clear acceleration strategy makes the method computationally expensive for practical use, especially when compared to single-forward-pass deterministic models or diffusion models with optimized sampling techniques.
- Additionally, Algorithm 1 presents both cases with and without ground truth. In the paper, Table 1 seems to show results for a full-reference case, where ground truth is available during inference, and the predicted image can be evaluated based on its similarity to the ground truth. However, this approach is highly impractical and does not appear to offer a fair comparison with other models. The use of ground truth during inference for evaluation is not representative of real-world scenarios where ground truth is unavailable, thus skewing the comparison against other methods that operate without ground truth.
- While the paper suggests using CLIP text feature cosine similarity as a non-reference approach, a detailed explanation is missing from both the main text and the appendix. In my opinion, the results based on the non-reference case using CLIP text features would be more reasonable, and these results should be presented in the paper as a table. The absence of a thorough explanation of how CLIP features are used for IQA and the lack of results using this approach in the main tables makes it difficult to assess the practical value of the proposed method in real-world settings where ground truth is not available.

### Questions
- While the content is clear and easy to understand, I have some questions about the inference setup. Below are a few concerns regarding the weaknesses:
   - In the case of K=100, as used in the paper, what are the statistics for the predicted enhanced images? For example, I am curious about the minimum, maximum, median, and mean values of PSNR/SSIM.
   - Could you add the results using CLIP features to Table 1 and Table 2? I am also interested in the statistics for those results.
   - When applying Bayesian models, are there any commonly expected generalization advantages? For instance, how does the model trained on LOL-v1 perform on LSRW[1*]? It would be helpful if results using both full-reference metrics and CLIP features were provided.
- If the non-reference method using CLIP features can still demonstrate outstanding performance, I am willing to raise the rating. However, based on my experience, the method using CLIP features presented in the paper has not shown consistent performance. Could you provide additional explanations regarding this issue?
---
[1*] Hai, Jiang, et al. "R2rnet: Low-light image enhancement via real-low to real-normal network." Journal of Visual Communication and Image Representation 90 (2023): 103712.

### Soundness
3

### Presentation
1

### Contribution
2

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
One of the key issues worth considering in image enhancement is determining the appropriate level of enhancement, which is referred to as the "one-to-many" problem in the paper. In this paper, the authors attempt to address this issue using Bayesian Neural Networks (BNNs).  This is the most significant contribution of the paper and also the aspect that I find most interesting. 
Specifically, this paper introduces Momentum Prior to mitigate the convergence difficulties of Bayesian-based Enhancement Models and proposes a two-stage approach to reduce the complexity of Bayesian-based Enhancement Models.

### Strengths
1.This is the first method based on Bayesian Neural Networks (BNNs) for image enhancement.

2.The approach demonstrates impressive results in both low-light image enhancement (LLIE) and underwater image enhancement (UIE) tasks.

### Weaknesses
The weaknesses summarize the questions that follow; please refer to the questions for more details.

1.Ground Truth Leakage in Prediction Method（Q1）

2.Slightly lack of Novelty in the Momentum Prior（Q2.1）

3.Insufficient Evidence to support the motivation of Momentum Prior （Q2.2） and TWO-STAGE APPROACH （Q3）

4.The coherence and readability of the paper could be improved.
For instance, both the abstract and the introduction do not address the motivation of the TWO-STAGE APPROACH. However, it suddenly occurs at the contribution and main text that "TWO-STAGE APPROACH is introduced to the complexity of BEM in modeling high-dimensional image data".

### Questions
I have previously considered the one-to-many problem mentioned by the authors and even experimented with BNNs, but eventually abandoned the approach. Therefore, I am pleasantly surprised to see this paper and sincerely hope this paper can be accepted. However, there are some issues that prevent me from giving a higher score, leading to a borderline reject. I have carefully considered the issues I raised, and while these issues might be somewhat pointed, I really haven't found clear answers to them. **If the authors address some concerns I raise, I would be willing to increase my score!**

Q1. **The most critical issue is in Section 3.3, "PREDICTIONS UNDER UNCERTAINTY", where the prediction method seems to rely on ground truth (GT) information.**

   - Lines 225 -230, when GT is available, mean squared error (MSE) or other perceptual metrics are computed, and the image with best score is selected as the output. Since MSE is a step in calculating PSNR and the perceptual metric used in this paper LPIPS is highly correlated with PSNR, this approach essentially involves running multiple iterations and choosing the result that is closest to the GT. This appears to be a form of GT leakage. The network is expected to determine the degree of enhancement autonomously. However, this method relies on GT information to determine the enhancement level, which is akin to using an advanced "GT mean" trick.

The paper also lacks an ablation study comparing with and without the proposed prediction method. The authors can consider adding such ablations and evaluating the model using no-reference image quality metrics or exploring alternative fusion methods.

Q2. **Novelty and motivation of the Momentum Prior method**:
   - **Q2.1 Lack of innovation in the Momentum Prior**: The Momentum Prior is essentially a combination of BNN and Exponential Moving Average (EMA). EMA is a well-established and commonly used technique, so simply combining BNN and EMA may lack sufficient novelty.
   - **Q2.2 Insufficient evidence to support the motivation of Momentum Prior**: The Momentum Prior is introduced to address issues of underfitting or even non-convergence. However, the paper does not cite any works that discuss these problems in BNN training, and there is insufficient experimental evidence to support the claim of non-convergence in BNNs. In Section 5.3, lines 499-520, there is an ablation study on different priors, and Figure 8 shows PSNR values over iterations. Yet, from Figure 8, it appears that other priors also converge, albeit to poorer results, which does not strongly support the claim of underfitting or non-convergence. 

I have personally thought about this problem for some time, and I understand the difficulty in proving it. Some other methods present both PSNR and loss training curves, which the authors may want to consider.

Q3. **Insufficient evidence to support the motivation of TWO-STAGE APPROACH**:
   - The TWO-STAGE APPROACH is proposed to address imprecision due to the complexity of high-dimensional images. However, there are no relevant references cited, and the ablation study only demonstrates that the two-stage approach performs better than a single-stage approach. I still do not know the exact reasons why the two-stage approach is superior. 

I remain skeptical about whether the issue is truly due to dimensionality. For instance, on a low-dimensional dataset, would using only a Bayesian Neural Network (BNN) suffice? The authors can consider test one stage and two stage on lower-dimensional tasks or provide a  theoretical analysis of why the two-stage approach helps with high-dimensional data or cite some relevant references about "the complexity of high-dimensional images reduces the performance of BNN".

### Soundness
1

### Presentation
3

### Contribution
3
