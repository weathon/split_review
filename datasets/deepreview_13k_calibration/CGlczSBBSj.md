# SEAL: A Framework for Systematic Evaluation of Real-World Super-Resolution

- Decision: Accept
- Avg Score: 7.00
- Scores: 6, 8, 6, 8

## Abstract
Real-world Super-Resolution (Real-SR) methods focus on dealing with diverse real-world images and have attracted increasing attention in recent years. The key idea is to use a complex and high-order degradation model to mimic real-world degradations. 
Although they have achieved impressive results in various scenarios, they are faced with the obstacle of evaluation. Currently, these methods are only assessed by their average performance on a small set of degradation cases randomly selected from a large space, which fails to provide a comprehensive understanding of their overall performance and often yields inconsistent and potentially misleading results.
To overcome the limitation in evaluation, we propose \modelname{}, a framework for systematic evaluation of real-SR. In particular, we cluster the extensive degradation space to create a set of representative degradation cases, which serves as a comprehensive test set. Next, we propose a coarse-to-fine evaluation protocol to measure the distributed and relative performance of real-SR methods on the test set. The protocol incorporates two new metrics: acceptance rate ($AR$) and relative performance ratio ($RPR$), derived from acceptance and excellence lines.
Under \modelname{}, we benchmark existing real-SR methods, obtain new observations and insights into their performance, and develop a new strong baseline. We consider \modelname{} as the first step towards creating a comprehensive real-SR evaluation platform, which can promote the development of real-SR

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The paper presents a framework for evaluating blind single-image super-resolution techniques against multiple different degradation types.  The process generates a large random sampling of degradations and then clusters the resulting images based on histograms. Each cluster represents functionally similar degradations, regardless of the process of obtaining them. The authors can then generate a diverse and comprehensive test set by sampling from the degradations represented by each cluster. 

The authors also use a fully automated method of evaluating new networks relative to two existing networks that play the role of baseline (acceptable) and best-in-class (excellent). By evaluating each test image relative to these two networks, they can provide more meaningful statistics about the robustness of each network to the range of potential degradations.

### Strengths
The paper addresses an issue in blind single-image super-resolution that has not yet been fully solved: how to effectively evaluate performance. It is clear from prior work that PSNR is insufficient, since it does not always agree with human perception.  SSIM and perceptual distance provide potentially more informative metrics, but using aggregate averages does not convey strength across different types of degradation.

The use of other networks to provide baseline (acceptable) and state-of-the-art (excellent) performance is an interesting approach. One downside is the continued reliance on PSNR, which has a hard time capturing fine textures or visual structures.

The clustering-based approach to identifying diverse degradations is an interesting idea.

### Weaknesses
The authors use histograms as the basis for clustering degradations. However, the form of the histograms does not appear to be given in the paper (sections 3.2, 3.3).  Are these histograms of r, g, and b separately?  Is this a 2-D chromaticity histogram, a 3-D RGB histogram, or a set of histograms of filter bank outputs?  It's not clear that all of these would be equally effective at capturing diverse degradations.

The sole use of PSNR as a way to rank-order results may not be the best choice.  PSNR rankings don't always reflect human rankings.

### Questions
Why use PSNR as the basis for whether an image is Acceptable?  Why not SSIM, perceptual distance, or some combination of the three?  Do you get different rankings with different metrics under this evaluation system?

The histograms used in the clustering are histograms of what?

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
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper revisits real-world super-resolution evaluation from a distributional viewpoint, integrating various representative degradation types into the test sets. Previous works only conduct evaluation using average performance on a small set of degradation cases randomly selected from a large space, which often yields biased results. To address this issue, the authors adopt a simple yet effective degradation clustering strategy to select representative degradation. Then, they present an evaluation protocol with two new model-based metrics suitable for real-SR tasks. The experimental results offer a new perspective on real-SR evaluation through the proposed SEAL systematic evaluation framework.

### Strengths
1.It is reasonable and interesting to use representative degradation to construct test set for real-SR evaluation.

2.  The authors employ a straightforward yet effective strategy (spectral clustering) for degradation clustering. This approach is not only easy to comprehend, but it also offers potential for further extensions.

3.  The systematic test set offers flexible customization options. 

4.  The introduction of new evaluation metrics provides a fresh perspective for real-SR evaluations. These metrics can also complement existing ones, thereby enriching the evaluation strategy.

5.The paper is well-written, and its main idea is easy to follow.

### Weaknesses
1.  In Figure 1, the author compares the average performance of two randomly selected test sets for conventional evaluation. If evaluations were conducted on multiple randomized test sets, it could potentially provide a more comprehensive understanding of the model’s performance. It would allow for the observation of performance trends across different test sets and offer insights into the model’s consistency and reliability.

2.  Utilizing a hundred test sets can indeed offer substantial reference points for real-SR evaluation. However, this approach may lead to an increase in the inference time required for evaluation. It would be beneficial for the author to compare the time cost of the existing evaluation method with that of the proposed SEAL evaluation to provide a more comprehensive understanding of their efficiency.

3.  A more detailed explanation of the spectral clustering process, as outlined in Section 3.2, would be beneficial.

### Questions
1.  Figure 3 presents a coarse-to-fine evaluation protocol. Initially, the authors utilize AR to validate the effectiveness of the real-SR model in comparison to the acceptance line. Subsequently, they employ coarse metrics to rank the real-SR model. However, actual evaluations may be contingent on user requirements. Could the sequence of fine-grained indicators possibly be adjusted to meet specific needs?

2.  Why is it that the evaluation based on MSE-based real-SR employs multiple smaller models as reference lines, whereas the GAN-based real-SR utilizes a single model as reference lines?

### Soundness
4 excellent

### Presentation
4 excellent

### Contribution
4 excellent

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
2: You are willing to defend your assessment, but it is quite likely that you did not understand the central parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
In this paper, the authors proposed a new evaluation framework for the evaluation of real-world super-resolution (SR) methods. They first used a clustering-based approach to model a large degradation space, and then designed two new evaluation metrics to assess real-SR models on representative degradation cases. The authors benchmarked existing real-SR methods with the proposed evaluation protocol and presented new observations and insights.

### Strengths
The authors handle the issue of fair and comprehensive evaluation of real-SR methods, which can facilitate the development of real-world SR.

### Weaknesses
1. In Introduction, the authors argued that random selection may cause significant bias and randomness to the evaluation results. From my point of view, random selection will not cause bias because the posibility of choosing each degradation is identical. The authors are suggested to check this claim to avoid misunderstanding. Same issues exist in Section 5.3.

2. In Section 3.1, there may be a mistake in the calculation of the total combination of degradations. Since the order of degradation types can be switched, the total degradation combination for $s$ degradation type and $k$ degradation levels should be $A^{s}_{s} \times k^{s}$.

3. In Section 3.2, the authors claimed that different combinations of degradation types may have similar visual quality and restoration defficulty. Consequently, the authors designed a clustering-based approach to handle this problem. However, this approach seems intuitive, and experiments should be conducted to validate whether the clustering works as expected, i.e., whether the examples within a cluster have similar visual quality and restoration defficulty whereas the examples in different clusters differ significantly. Only using Fig. 13 for demonstration is not enough.

4. The authors only used one image (i.e., lenna) to generate 100 degradation parameters. It can be observed in Fig. 9 that the image content can affect the final results (0.1-0.3 dB in PSNR). Consequently, have the authors considered using more images to generate more stable and representative clustering centers?

### Questions
In Section 5.4, what is the purity accuracy defined as? More details should be explained.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
This work aims to come up with a benchmarking approach to evaluate real SR methods in literature. To this end authors propose to use Acceptance Rate (AR) for coarse grained comparisons and Relative Performance Ratio (RPR) based measures for fine-grained analysis. The motivation and the impact of the proposed metrics are clearly demonstrated with interesting findings on why the previous approaches are misguiding and how the proposed method can alleviate the associated problems.

### Strengths
1. The problem tackled in this work has significant practical impact.
2. The proposals are intuitive and supported by experimental evidences.
3. The proposed method comes up with a new and more reliable benchmarking approach for evaluating real-SR methods.

### Weaknesses
The reliability of clustering algorithms is measured using purity accuracy.
1. The definition of purity accuracy is fuzzy and will need better explanation.
2. I would advise to demonstrate via visual comparisons that the clusters formed with the proposed method indeed are meaningful to answer the following questions - does a bunch of randomly sampled images from a given cluster look degraded by a comparable amount? Does, random samples from different clusters exhibit contrasting degradation levels?

### Questions
Please address the comments under weaknesses

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
