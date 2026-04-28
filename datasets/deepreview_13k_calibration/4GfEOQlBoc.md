# Disentangling the Link Between Image Statistics and Human Perception

- Decision: Reject
- Avg Score: 5.25
- Scores: 5, 6, 5, 5

## Abstract
In the 1950s, Barlow and Attneave hypothesised a link between biological vision and information maximisation. Following Shannon, information was defined using the probability of natural images. A number of physiological and psychophysical phenomena have been derived ever since from principles like info-max, efficient coding, or optimal denoising. However, it remains unclear how this link is expressed in mathematical terms from image probability. First, classical derivations were subjected to strong assumptions on the probability models and on the behaviour of the sensors. Moreover, the direct evaluation of the hypothesis was limited by the inability of the classical image models to deliver accurate estimates of the probability. In this work we directly evaluate image probabilities using an advanced generative model for natural images, and we analyse how probability-related factors can be combined to predict human perception via sensitivity of state-of-the-art subjective image quality metrics. We use information theory and regression analysis to find a combination of just two probability-related factors that achieves 0.8 correlation with subjective metrics. This probability-based sensitivity is psychophysically validated by reproducing the basic trends of the Contrast Sensitivity Function, its suprathreshold variation, and trends of the Weber-law and masking.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors propose to further test the relation between image statistics and perceptual sensitivity. To this purpose they propose to test and to compare several previously proposed heuristic models for predicting perceptual sensitivity (and also combination of those models). The main contribution is the use of deep neural network architectures to provide a direct estimate of the distribution of natural images. Finally, the authors validate their approach by reproducing classical psychophysical functions.

### Strengths
- the work is well-grounded in the theoretical vision science field with sufficient references to previous research
- extensive model comparison (several predictive models vs several perceptual distances)
- validation on empirical data

### Weaknesses
 **Major**

- Methodological issues : (i) The paper does not really tackle the question of image statistics and human perception as in fact human perception is replaced by perceptual distances which are only computational models that mimic human perception. The core issue is that the study uses computational metrics as proxies for human perception, without directly measuring human perceptual responses. This substitution limits the conclusions that can be drawn about the relationship between image statistics and *actual* human perception. The paper should acknowledge that it is exploring the relationship between image statistics and computational models of perception, not necessarily human perception itself.  
(ii) The use of polynomial combinations of different models does not really make sense in the proposed work. Polynomials can often fit any data so they are not really falsifiable... Here it is true that the authors limit themselves to order 2 polynomials but the decision is only based on fit quality. Is there any reason/motivation to get a second order polynomial beyond fit quality ? The justification for using second-order polynomials is weak, as it is primarily based on empirical fit. The authors should provide a theoretical basis or a more principled justification for this choice, rather than relying solely on the observation that higher-order polynomials do not improve the fit. Without a theoretical motivation, the use of polynomials risks overfitting and lacks interpretability.

- Here the authors seem to avoid assuming that there is an underlying transduction function proper to an observer. I think this could be a strength but the authors do not mention this and recent relevant literature is not cited (see below). When you assume the existence of a transduction function (that is actually measurable in an observer) and with extra optimal coding assumption you can explicitly derive the relation between the probability density and the perceptual distance. Though this framework is somehow more restricted because it requires assumptions about the nature of the image distortion. In contrast, in the proposed work it should be valid for any distortion (as long as it is small enough) but only adding uniform noise is tested...

Extra-literature : 
- Wei, X. X., & Stocker, A. A. (2017). Lawful relation between perceptual bias and discriminability. Proceedings of the National Academy of Sciences, 114(38), 10244-10249.  
The MLDS technique to measure transduction functions and some use cases:
- Knoblauch, K., & Maloney, L. T. (2008). MLDS: Maximum likelihood difference scaling in R. Journal of Statistical Software, 25, 1-26.
- Charrier, C., Knoblauch, K., Maloney, L. T., Bovik, A. C., & Moorthy, A. K. (2012). Optimizing multiscale SSIM for compression via MLDS. IEEE Transactions on Image Processing, 21(12), 4682-4694.
- Vacher, J., Davila, A., Kohn, A., & Coen-Cagli, R. (2020). Texture interpolation for probing visual perception. Advances in neural information processing systems, 33, 22146-22157.

**Minor**
- Throughout the paper, it is unclear what is the prediction of $S$ from the probabilistic factor and it makes figure 2 hard to understand. Why are those histograms useful ? Could we expect to measure such an histogram in a human observer ? Indeed what would really be good to see in this figure is a row corresponding to human observer.
- It is unclear how the probability of a natural image is computed from PixelCNN++ ... It is not straightforward and the authors should not assume that the reader is familiar with any neural network...
- Where are the real data in Figure 4 ? This would be useful for a reader who does not know those curves...

### Questions
See above.

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
This paper directly evaluates image probabilities using a generative model PixelCNN++ and analyzes how probability-related factors can be combined to predict human perception via the sensitivity of SOTA image quality metrics. Further, it uses information theory and regression analysis to find a combination of just two probability-related factors that achieve a high correlation with the SOTA image quality metrics. Finally, this probability-based sensitivity is psychophysically validated by reproducing the fundamental trends of the Contrast Sensitivity Function, its suprathreshold variation, and trends of the Weber law and masking.

### Strengths
An interesting study on "Disentangling the Link Between Image Statistics and Human Perception" with experimental verification.

### Weaknesses
None

### Questions
This is an exciting study.  I did not notice major defects in this manuscript, to my knowledge. However, it would be more interesting if there could be more experimental verifications on other SOTA IQA metrics. And what will happen if more accurate probabilities are estimated by more advanced generative models?

The impact of this work would be increased by providing the source code.

$log (p(\hat{\mathbf{x}}))^\gamma, log (p(\hat{\mathbf{x}}))^2, log (p(\hat{\mathbf{x}}))^{-1}, ...$ should be $\left(\log p(\mathbf{x})\right)^\gamma, \left(\log p(\mathbf{x})\right)^2, \left(\log p(\mathbf{x})\right)^{-1}, ...$

To be self-contained, symbols in Table 1, e.g., $B, \mu, \Sigma$, can be explained in place.

The editing can be improved, e.g., log -> \log; Figure -> Fig.; table -> Table; section  -> Sec.; Eq.  \ref{} -> Eq. \eqref{}; overlapped terms in Fig. 3; the period in Appendix B, C, D;  [0’3,0’2,0’1,0,1,2,3] in Table 4; and the presentation quality of most of the Figures in the manuscript.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

### Summary
The authors investigate the relationship between image-probability factors and four different proposed measures of human sensitivity based on image-quality measures. They use regression analysis and mutual information to quantify what is shared between the probability factors and the sensitivity measures. They find that $log(p(\tilde{x}))$ is most indicative of the perceptual sensitivity for the tested distances.

### Strengths
The paper is topical given current widespread interest in generative models capturing probability distributions. The introduction and background section are well written and cover a lot of interesting ground connecting classical work in neuroscience and perception to more modern computational models. The authors also test a variety of different proposed perceptual distance measures.

### Weaknesses
W1: The paper starts out (with the title) stating that it is investigating the link between image statistics and human perception, however, there is no human perception actually studied in the paper. The authors mention this in the discussion as a limitation (that as a proxy for human perception, perceptual metrics were used). However, all of these perceptual metrics are known to be imprecise. Given this, it is overall difficult to know what to take away from the paper. Are the authors actually studying human perception, or are they studying properties of “perceptual distances” that have previously been described? Additionally, the wording throughout the paper should be softened to make it clear that these are just distances measured by a model and not human measurements. The core issue is that the paper claims to investigate human perception, but the experiments only analyze the behavior of existing perceptual metrics, which are known to have limitations and may not accurately reflect human perception. This discrepancy undermines the paper's central claim and makes it unclear what conclusions can be drawn about actual human perception. The authors need to clearly distinguish between studying human perception and studying the properties of these metrics.

W2: The classical psychophysics experiments are difficult to follow. Perhaps a schematic would help readers understand what is actually being tested in the models? Additionally, the paper states that the classic psychophysics experiments are an “independent way” to validate the proposed models. I’m not so sure that this is actually independent, as presumably, many of the developed distance measures take into account (either explicitly or implicitly) visual sensitivity based on luminance, contrast, and special frequency. The psychophysics experiments are not clearly explained, making it difficult to assess their relevance. A schematic diagram would greatly improve understanding. Furthermore, the claim of independence is questionable since many perceptual metrics are designed to align with known aspects of human visual sensitivity, such as contrast sensitivity functions, thus potentially introducing a circularity in the validation process. The authors need to justify the independence claim more rigorously.

W3: The authors use a model trained on the CIFAR dataset to get p(x) and then use this for testing, but I’m not sure that this accurately captures relevant properties of human perception (and also whether the distances measures that they are studying are valid on this dataset). Discussion about the distribution mismatch between the datasets that were used to test models of distance measures and the dataset used for training the model used to obtain p(x) might be beneficial. The use of a CIFAR-trained model to estimate p(x) raises concerns about the generalizability of the results to more complex, natural images. The distribution mismatch between the training data for the probability model and the data used to evaluate the perceptual metrics could introduce biases. A more thorough discussion of this limitation and its potential impact on the conclusions is needed.

### Questions
Q1: In the first paragraph of 2.1 the authors have a sentence saying, “This ratio is big at regions of the image space where human sensitivity is high and small at regions neglected by humans.” This seems a bit opaque to me. What are “regions of image space”? Additionally, it seems like there need to be constraints of (1) small perturbations since this is a local measurement and (2) comparing these “regions of image space” only when the ||x-\tilde(x)||^2 is equal between the two tested regions. Are these necessary? 

Q2: In the first sentence of 3.1 the authors use the phrase “sensitivities of the metrics”. I think this just means something like “how these metrics change with different probability factors”? The wording is a bit confusing because the paper is studying “sensitivities." 

Q3: Figure 2 is somewhat difficult to interpret. Clearly defining the x and y axes in the figure (rather than in the text) would help the reader. 

Q4: Figure 4 y-axis is labeled as “Sensitivity” but it would be helpful to explicitly list this as something like “DISTS-derived Sensitivity”.

Q5: The authors state in the discussion that “images in the subjective experiments usually fall out of the range where you can use the current probability models”. Could the authors spell this out a little more?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
3 good

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This paper investigates the use of probability-related factors to explain/predict human perception (approximated by sensitivity of
state-of-the-art image quality metrics).

### Strengths
1. The problem is of fundamental and theoretical importance. 

2. The related work, especially Sec. 2.2 is a delightful read to the reviewer.

### Weaknesses
1. The definition of perceptual sensitivity in Eq. (1) is debatable.  For any given $D_p(x,\hat{x})$, it is easy to come up with $\hat{x}$ to be a counterexample of $S(x,\hat{x})$, i.e., big ratio corresponding to low human sensitivity and vice versa. For example, the synthesis of $\hat{x}$ can be performed by the maximum differentiation competition [Wang and Simoncelli] or the perceptual attack [Zhang et al.]. The core issue is that $S(x, \hat{x})$ as defined is a *directional* sensitivity, dependent on the specific distortion vector $x - \hat{x}$, and does not capture the overall sensitivity at a point $x$. A high value of $S(x, \hat{x})$ for a particular $\hat{x}$ does not necessarily imply high sensitivity in a general sense, and could be misleading if interpreted as such.

2. The authors should clearly state the meaning of $p(x)$: is it probability density function (PDF) or probability mass function (PMF)? Working with PDF is less reasonable, if the learned distribution is not smooth. If a PDF is used, the authors need to address the potential for singularities in the learned distribution, which could lead to unreliable probability estimates and therefore unreliable sensitivity predictions. The smoothness of the learned distribution and its impact on the results should be explicitly analyzed.

3. Perturbing images with additive uniform noise makes the results in this paper less interesting. The use of uniform noise as a perturbation is not representative of real-world distortions or the types of perturbations that are most relevant to human perception. Exploring more structured or perceptually relevant perturbations would be more insightful. It is unclear whether the observed relationships between probability and sensitivity are specific to uniform noise or generalize to other types of distortions. The authors should justify the choice of uniform noise and discuss its limitations.

4. Parameteric prediction in Eq. (3) and Eq. (4) can be trivial and thus meaningless with a deliberately chosen set of $\hat{\mathcal{X}}_1$={$\{\hat{x}\}$}. Putting another way, it is not hard to come up with another  $\hat{\mathcal{X}}_2$={$\{\hat{x}\}$} to make the parametric prediction nearly impossible. The current formulation of the parametric prediction lacks robustness and is highly sensitive to the choice of distortion samples. The authors need to demonstrate that the model can generalize beyond a specific set of distortions and provide a more rigorous justification for the chosen approach.

5. How to apply the computational analysis in the paper? Can the results reflect which quality metrics are better explaining human perception? The practical utility of this analysis is unclear. The authors need to explain how the established relationship between probability and metric sensitivity can be used to improve image quality assessment methods or provide insights into human perception. It is not clear if the results can be used to differentiate between the quality metrics in terms of their ability to predict human perception.

### Questions
1. The reviewer fails to understand the message of Fig. 2.

### Soundness
2 fair

### Presentation
3 good

### Contribution
2 fair
