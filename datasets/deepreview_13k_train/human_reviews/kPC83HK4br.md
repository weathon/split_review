# CHAMP: Conformalized 3D Human Multi-Hypothesis Pose Estimators

- Decision: Accept
- Scores: 6, 8, 6, 6

## Abstract
We introduce CHAMP, a novel method for learning sequence-to-sequence, multi-hypothesis 3D human poses from 2D keypoints by leveraging a conditional distribution with a diffusion model. To predict a single output 3D pose sequence, we generate and aggregate multiple 3D pose hypotheses. For better aggregation results, we develop a method to score these hypotheses during training, effectively integrating conformal prediction into the learning process. This process results in a differentiable conformal predictor that is trained end-to-end with the 3D pose estimator. Post-training, the learned scoring model is used as the conformity score, and the 3D pose estimator is combined with a conformal predictor to select the most accurate hypotheses for downstream aggregation. {Our results indicate that using a simple mean aggregation on the conformal prediction-filtered hypotheses set yields competitive results.} When integrated with more sophisticated aggregation techniques, our method achieves state-of-the-art performance across various metrics and datasets while inheriting the probabilistic guarantees of conformal prediction.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
CHAMP presents a conformalized multi-hypothesis pose estimation pipeline. Based on diffusion model, the multiple pose hypothesis are refined by a differentiable comformal prediction module with an inefficiency loss. Experiments show that CHAMP achieves state-of-the-art results on several benchmarks.

### Strengths
1. The proposed conformal prediction is simple yet effective. 
2. This paper is well-written and easy to understand.

### Weaknesses
1. CP removes the predictions with low confidence and visualisations also show after CP the predictions become more certain and accurate. However, the results are mainly shown with easy cases where occlusions barely present. I am wondering how CP performs on hard cases where occlusions, truncations exist?
2. It will be better if this method can be extended to image-to-3d pipelines.

### Questions
This paper is well-presented and validated. The only thing I concern is its performance on occluded or truncations where diverse multiple hypothesis are preferred.

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This work tackles the task of 2D-to-3D lifting of temporal human pose sequences through a diffusion-based multi-hypothesis approach. The novel aspect is applying the tools of conformal prediction to this task. That is, the authors propose to learn a conformity score function in an adversarial setup and simulate conformal prediction during training, directly minimizing the conformal set size (the inefficiency). Quantitative evaluation is performed on the well-known Human3.6M and MPI-INF-3DHP datasets, with additional qualitative evaluation on in-the-wild videos. Results show that filtering according to conformity scores and aggregating the results improves the metrics and achieves state-of-the-art results. Ablations also show that the end-to-end training of the scoring function is beneficial.

### Strengths
The application of conformal prediction to 3D human pose estimation is an interesting and original aspect. Multi-hypothesis 3D pose estimation has been a relevant research area due to ambiguities in the task, but practical methods are often not formulated in a proper probabilistic manner. Using conformal prediction techniques is a promising direction and taking a first step in this direction is relevant to the community.
The overview of the related works is extensive, and the comparison of them helps the reader to place this work in relation to them. The text is well-structured and easy to follow.
The authors use already existing techniques in good ways, for example using the already proven MixSTE model for denoising, incorporating adversarial training and conformal calibration.
Results on Human3.6M and MPI-INF-3DHP both demonstrate the benefit of the method.
Ablations and hyperparameter studies confirm the design choices.

### Weaknesses
The method is only evaluated on studio datasets, but not on outdoor ones, such as 3DPW and EMDB. Evaluation on such less restricted videos would be more convincing.
It is unclear whether CHAMP's learned conformity scoring performs better than the prior established 2D-joint projection based version (see question below).

I don't fully understand the CHAMP-Agg method. Is this using J-Agg on the full set of hypotheses, or does it also use the learned scoring function in some way? How should we interpret the fact that "CHAMP-Agg" is better than "CHAMP"? Does it mean that the proposed learned conformity scoring does not perform better than the prior method of aggregation proposed by Shan et al. (2023)?

To the paragraph after Eq. 5: How can we interpret the "true value to be included in" the conformal set in case of continuous values like 3D coordinates? In case of classification this makes more sense, but perhaps the language has to adjusted here.
What 2D pose estimator is used in the main experiments, or is the ground truth used?
Why are values missing from Table 3?

Smaller issues:
GAN is cited as the CACM 2020 paper, but perhaps the original NIPS 2014 version is better suited for citation.
In Eq 9, perhaps Temperature could be denoted by some other symbol because mathcal{T} and tau look very similar visually (except for size). Similarly I would not recommend relying on the subtle difference between C and mathcal{C} for important differences (as noted in the footnote of page 6), a hat, tilde or similar feature may be more visible.

Page 7: Human3.6M is no longer the "largest indoor dataset for 3D human pose estimation". There are many larger ones such as DNA-Rendering.
It should be stated explicitly that E2E refers to "end-to-end".

### Questions
I don't fully understand the CHAMP-Agg method. Is this using J-Agg on the full set of hypotheses, or does it also use the learned scoring function in some way? How should we interpret the fact that "CHAMP-Agg" is better than "CHAMP"? Does it mean that the proposed learned conformity scoring does not perform better than the prior method of aggregation proposed by Shan et al. (2023)?

To the paragraph after Eq. 5: How can we interpret the "true value to be included in" the conformal set in case of continuous values like 3D coordinates? In case of classification this makes more sense, but perhaps the language has to adjusted here.
What 2D pose estimator is used in the main experiments, or is the ground truth used?
Why are values missing from Table 3?

Smaller issues:
GAN is cited as the CACM 2020 paper, but perhaps the original NIPS 2014 version is better suited for citation.
In Eq 9, perhaps Temperature could be denoted by some other symbol because mathcal{T} and tau look very similar visually (except for size). Similarly I would not recommend relying on the subtle difference between C and mathcal{C} for important differences (as noted in the footnote of page 6), a hat, tilde or similar feature may be more visible.

Page 7: Human3.6M is no longer the "largest indoor dataset for 3D human pose estimation". There are many larger ones such as DNA-Rendering.
It should be stated explicitly that E2E refers to "end-to-end".

### Soundness
3

### Presentation
4

### Contribution
3

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
5

### Summary
This paper focuses on 3D pose estimation from 2D pose inputs in a multi-hypothesis sequence-to-sequence way. Following previous methods, they also adopt a diffusion model to regress the 3D pose hypotheses from sequential 2D pose inputs. Different from previous work, this paper proposes to learn a score model along with the regression model to predict the confidence of multiple regressed hypotheses. The scores of multiple hypotheses could be used to filter out the outliers to refine prediction set.   
The eperiments are mostly conducted on two benchmarks, Human3.6M and MPI-INF-3DHP. Compared with directly averaging all multi-hypothesis predictions, averaging filtered predictions with the proposed score model reduces 1.5mm MPJPE on Human3.6M, while selecting the 3D pose whose 2D projection is more consistent with the 2D pose further reduces 1.5mm MPJPE on Human3.6M.

### Strengths
1. Learning the uncertainty of multi-hypothesis 3D human pose regression seems to be reasonable. Aside from building the distrubution of 3D human poses, how to select the best ones is an interesting research topic.   
2. Designs in scoring the hypotheses via conformal prediction are subtle. Detailed ablation study further reveals the influence of different parameters.   
3. The description of method is clear. Especially, Fig. 2 provides a clear overview of the relationship between different designs.

### Weaknesses
1. Experiments.   
Tab. 1 and Tab. 2 show the improvement, compared with CHAMP-Naive, via introducing comformal prediction (CHAMP) and further selecting the 3D pose via measuring the 2D projection and 2D pose (CHAMP-Agg).  However, one important experiment seems to be missing here, CHAMP-Naive + -Agg. How well it performs if the proposed comformal prediction is not used?   
This experiment will clearly show how important the proposed comformal prediction is.   
Besides, the quantative eperiments are only conducted on indoor benchmarks. The qualitative results are relatively limited.  Performance on in-the-wild benchmarks, such as 3DPW, is not clear.   

2. The performance improvement is not significant compared with the baseline SOTAs, which might effect the value of this work.

### Questions
See the experiments mentioned above.

### Soundness
3

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
5

### Summary
This paper proposes using a diffusion model to generate multiple hypotheses for temporal 2D to 3D pose estimation and introduces Conformal Prediction (CP) to select more plausible hypotheses and aggregate them. The method achieves competitive results on two pose estimation benchmarks.

### Strengths
1. The paper introduces the novel idea of using Conformal Prediction to select more plausible results from multiple hypotheses, which is a fresh perspective.
2. The quantitative experiments demonstrate that the hypotheses selected and aggregated using this strategy outperform the results without filtering.

### Weaknesses
1. The paper's contribution is to be discussed. First, the ambiguity in temporal 2D-to-3D pose estimation is not as significant as in the single-frame, single-view case. Additionally, generating multiple 3D hypotheses using diffusion models is already a widely used technique (DiffuPose (Choi et al., 2023) DiffPose (Gong et al., 2023) DiffPose (Feng et al., 2023) D3DP (Shan et al., 2023)). If the only contribution is the use of CP, its novelty might be limited. If the authors could show that the CP strategy also performs well in single-RGB input cases or demonstrates its effectiveness in single-image mesh estimation, it would significantly enhance the paper's contribution.
2. The quantitative results are not very solid. The improvement on 3DHP is quite marginal, making it unclear whether the improvement is due to random seed variation. These results do not convincingly support the method's effectiveness.
3. The visual results (e.g., Figure 10) do not show cases where severe occlusion leads to incorrect 2D estimates or cases where 3D depth errors occur. It’s important to demonstrate that CP can filter out incorrect hypotheses in such challenging cases, where multi-hypothesis generation is truly necessary. This ties back to the first weakness, as the temporal nature of the data may already provide additional constraints, reducing ambiguity. Therefore, the authors should explore more varied tasks to prove CP's efficacy, such as monocular pose estimation.

### Questions
Regarding the method, it is unclear how the approach handles situations where the 2D estimates are incorrect or when the 2D pose is truncated beyond the image boundaries.

### Soundness
2

### Presentation
2

### Contribution
2
