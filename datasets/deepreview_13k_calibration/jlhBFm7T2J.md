# An undetectable watermark for generative image models

- Decision: Accept
- Avg Score: 6.50
- Scores: 8, 6, 6, 6

## Abstract
We present the first undetectable watermarking scheme for generative image models.
\emph{Undetectability} ensures that no efficient adversary can distinguish between watermarked and un-watermarked images, even after making many adaptive queries.
In particular, an undetectable watermark does not degrade image quality under any efficiently computable metric.
Our scheme works by selecting the initial latents of a diffusion model using a pseudorandom error-correcting code~(Christ and Gunn, 2024), a strategy which guarantees undetectability and robustness.

We experimentally demonstrate that our watermarks are quality-preserving and robust using Stable Diffusion 2.1.
Our experiments verify that, in contrast to \emph{every prior scheme} we tested, our watermark does not degrade image quality.
Our experiments also demonstrate robustness: existing watermark removal attacks fail to remove our watermark from images without significantly degrading the quality of the images.
Finally, we find that we can robustly encode 512 bits in our watermark, and up to 2500 bits when the images are not subjected to watermark removal attacks.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper presents an undetectable watermarking method for generative image models. The proposed PRC watermark aims to embed a cryptographically pseudorandom pattern that is robust, quality-preserving, and indistinguishable from adversaries without the detection key. Additionally, the PRC watermark can encode long messages, such as timestamps or IDs, without compromising image quality. Experimental results demonstrate that the PRC watermark maintains image quality and is difficult to detect or remove without significant quality degradation, making it a promising solution for embedding undetectable, robust watermarks in AI-generated images.

### Strengths
1. This paper provides an undetectable image watermark method, which is novel.
2. This paper provides sufficient theoretical and empirical support.

### Weaknesses
1. For Figure 2, this paper evaluates the undetectability of different watermarking methods. Could authors specify how many different keys other watermarking methods use? And if increasing the key numbers will increase the undetectability?

2. PRC.Encode_k is interesting, but it would be good for authors to explain how to sample a PRC codeword using PRC.Encode_k  in more detail. It should be an important part of this paper, but only Algorithms 1 and 2 in the Appendix are not enough for the reader to understand it.

3. Section 4.5 describes the security of PRC watermark under spoofing attack. The experimental results are in the Appendix; it would be good for the authors to specify where the corresponding experimental results are in Section 4.5. Moreover, the number of keys used for other watermarking methods in Figure 8 is also not specified.

### Questions
Please see above.

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper introduces an undetectable watermarking scheme for generative image models, which ensures that no adversary can distinguish between watermarked and un-watermarked images while preserving image quality. It utilizes a pseudorandom error-correcting code to embed watermarks at the semantic level, making the scheme robust against various removal attacks and capable of encoding long messages.

### Strengths
1. This paper is well-written and easy to follow.

2. The proposed method maintains image quality by embedding watermarks without degrading metrics like FID, CLIP, and Inception Score.

3. The watermarking method can be seamlessly integrated into existing diffusion model frameworks.

### Weaknesses
1. The idea of modifying the initial noise for diffusion is not new. And this method changes initial noise a lot compared to Tree-Ring watermark. Specifically, the method appears to alter the signs of the initial noise vectors, which could lead to significant content variations in generated images. This raises concerns about the practical acceptability of such alterations, as even subtle changes in initial noise can result in noticeable differences in the final output, potentially affecting the perceived quality and intended artistic direction of the generated content.

2. This watermark is not as robust as current watermarks such as StegaStamp and Gaussian shading. The experiments demonstrate that under heavier perturbations, the proposed PRC watermark exhibits lower robustness compared to StegaStamp and Gaussian shading. This is a significant limitation, as robustness against various attacks is a critical requirement for practical watermarking schemes. The evaluation metric, TPR@FPR=0.01, also indicates a high false positive rate, which could be problematic in real-world applications.

3. No significant improvements on metrics. While the PRC watermark shows marginal improvements in metrics like FID, CLIP score, and Inception Score compared to prior methods, these improvements are not substantial. The claim of being 'undetectable' requires further justification, especially considering that previous watermarking techniques also achieve competitive metric performance. The definition of 'undetectable' needs to be more rigorously defined, as the current results do not definitively demonstrate a clear advantage over existing methods in terms of imperceptibility.

### Questions
1. I understand the key idea of this work is quite similar to Tree-Ring watermark, i.e., selecting the initial noises of a diffusion model so that them can be later detected. However, a point of concern arises regarding the feasibility of completely altering the signs of the initial noise. Based on the provided examples, images without any watermark and those embedded with the PRC watermark exhibit significant differences, including distinct content variations. This raises the question of whether such discrepancies would be acceptable to companies and end-users in practical applications.

2. Is the implementation of Stable Signature correct in this work? As far as I know, images watemarked by Stable Signature should not display substantial differences from unwatermarked images because Stable Signature does not modify the initial latents.

3. The definition of ‘undetectable’ used in this study requires clarification. Based on the data presented in Table 1, the PRC watermark appears marginally more effective than prior watermarking methods concerning metrics such as FID, CLIP score, and Inception Score; however, the observed improvements are not pronounced. If the PRC watermark is claimed to be the first undetectable watermark, an explanation is needed as to why previous watermarking techniques are deemed detectable, given their competitive metric performance.

4. For robustness part, do you consider some transfer-based or query-based attack? The results illustrated in Figures 5 and 6 indicate that PRC watermarks demonstrate lower robustness compared to methods such as StegaStamp and Gaussian shading watermarks, especially when heavier perturbations are applied. Also note that your metric is TPR@FPR=0.01, and FPR=0.01 is already a very high false positive rate.

### Soundness
2

### Presentation
3

### Contribution
2

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper uses the pseudorandom code technique to create an pseudorandom initial noise for latent diffusion model. With this noise, the image generated from it is encoded with watermark signal. When reversing a image back to the initial Gaussian noise, the model provider can determine whether this image is waatermarked or not according to the codeword. Since the pseudorandom initial noise is indistinguishable to the real Gaussian noise, this watermark is undetectable compared with existing methods.

### Strengths
1. The paper introduces the first undetectable watermark.
2. The authors compare the proposed method with several watermarking baselines.
3. The robustness of the proposed method is evaluated with several perturbations.

### Weaknesses
1. The experiments are not adequate for supporting that the image quality of the proposed method outperforms existing ones.
2. The robuseness of the propsed method is not that good from the results.
3. The proposed watermarking method hugely change the image compared with the original one without watermark.
4. The evaluation for undetectability is not convincing.

### Questions
1. The values of the metrics shown in Table 1 are close for different methods, can you actually say that the proposed method is better than the existing ones? I think a significance test is needed to support this conclusion.
2. I don't think 500 images are enough for the computation of FID score. Referring to previous work like Stable Signature, at least 1,000 images are needed for getting a reliable results.
3. The results and image samples for Stable Signature is weird. According to the results of its original paper, Stable Signature should be a watermark that introduces minimal perturbations onto the original image. Therefore, the watermarked image should be highly similar to the original image. However, in the paper, the image samples and results of Stable Signature indicate that the watermarked image is completely different from the original images.
4. The robustness of the PRC method is not satisfied. From Figure 5, the TPR starts to drop when the PSNR is still larger than 30, which is much worse than StegaStamp and Gaussian Shading.
5. From the image samples in Figure 1, the image of the PRC method changes the original image a lot.
6. The evaluation for undetectability is not convincing. The author only uses ResNet-18 to show it can distinguish the watermarked and original images from other method but not the PRC method. However, is it possible that this results only hold for ResNet-18? It means that it is only undetectable for ResNet-18 and it may be detectable for other classifiers.

### Soundness
2

### Presentation
3

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
The paper presents a scheme to embed digital watermarks into the latent space of a diffusion model. The method is based on pseudorandom error-correcting code (PRC): the watermarked image is sampled from the latent vector conditioned on having signs chosen according to the corresponding PRC. In the paper, the guarantees on undetectability and low detection FPR rate are provided, along with the comparison against concurrent watermarking methods both in terms of robustness to removal attacks and quality of generated images.

### Strengths
The paper adapts PRC to the domain of image watermarking and build a robust watermarking scheme with provable FPR upon it. Authors compare their approach against a variety of watermarking schemes both in terms of robustness to different removal attacks as well as of the quality of watermarked images.  

The method implies provable guarantees on the FPR of the watermark extraction. The method is robust to attack on surrogate classifiers due to experimentally shown undetectability of the watermark. According to the evaluation protocol, PRC watermark retains the decent quality of the generated image, compared to the one of the sota methods.

The paper is well written, besides minor misprints.

### Weaknesses
1) In Theorem 1, an upper bound for the difference of probabilities is loose. To make a conclusion about undetectability, one has to demonstrate the negligible difference between the detection probabilities on watermarked and non-watermark samples. An upper bound which is close to ½ is unsatisfactory in this case. How one can be improved?

2) The robustness of the watermarks yielded by the method to removal attacks (both synthetic and based on diffusion models) is inferior to the ones of Gaussian Shading, Tree-Ring, StegaStamp approaches. Since the robustness is one of the major requirements of the watermark, it is important to improve it in practice. Namely, one may will to improve the robustness at the cost of the quality metric (for example, by embedding longer messages).

### Questions
Please see the weakness section.

### Soundness
2

### Presentation
3

### Contribution
2
