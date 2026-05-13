# Monsters in the Dark: Sanitizing Hidden Threats with Diffusion Models

- Decision: Reject
- Scores: 8, 3, 5, 6

## Abstract
Steganography is the art of hiding information in plain sight. This form of covert communication can be used by bad actors to propagate malware, exfiltrate victim data, and communicate with other bad actors. Current image steganography defenses rely upon steganalysis, or the detection of hidden messages. These methods, however, are non-blind as they require information about known steganography techniques and are easily bypassed. Recent work has instead focused on a defense mechanism known as sanitization, which eliminates hidden information from images. In this work, we introduce a novel blind deep learning steganography sanitization method that utilizes a diffusion model framework to sanitize universal and dependent steganography (DM-SUDS), which both sanitizes and preserves image quality. We evaluate this approach against state-of-the-art deep learning sanitization frameworks and provide further detailed analysis through an ablation study. DM-SUDS outperforms previous sanitization methods and improves image preservation MSE by 71.32\%, PSNR by 22.43\% and SSIM by 17.30\%. This is the first blind deep learning image sanitization framework to meet these image quality results.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
The authors present a blind method for image steganography sanitization that leverages diffusion models. They demonstrate the effectiveness of this method (DM-SUDS) by comparison to SUDS, a prior method for sanitization that leverages a variational autoencoder. Included is an ablation study on the timestep parameter for forward diffusion in their model, and illustrates the necessity of the forward diffusion process and optimal range of timesteps for three types of steganography, including least significant bit (LSB), universal deep hiding (UDH) and dependent deep hiding (DDH) methods.

### Strengths
The paper is well written and provides clear study and results that are significantly improved on the prior art (~70+% reduction in MSE , ~20+% improvement in PSNR) with similar elimination of steganography. The idea is novel and makes a lot of sense for appropriate application of diffusion models to steganography sanitization.

### Weaknesses
While the method appears highly effective, a more thorough explanation as to how the parameters were selected would improve the paper.  I was expecting some discussion of the strength of the embedding and estimation of the noise present in the images in order to determine the noise variance parameter for the diffusion model. It appears that the noise variance parameter beta is left unspecified and only the time step parameter is identified, with no explanation of how it was set other than the ablation study. Steganography methods often have a strength parameter that can be varied, and it is not clear how important it is to match the diffusion strength to a particular steganography implementation and strength level. Choice of diffusion parameters may be critical to determine the level of steganography that can be sanitized, as evidenced by the ablation study. It appears that the same dataset was used (CIFAR test set) for all of the experiments. If the parameters of the sanitization model (timestep t) were selected based on experiments performed using the same steganography methods and images, the method is technically not completely blind since the diffusion strength was tuned experimentally to the embedding method performance.  The ablation study lacks in quantitative results. The visualization is helpful, but should not replace quantifiable metrics.

### Questions
What was the value for beta, and how was timestep parameter t selected?  

Page 8, "is a stronger hiding method" -> I would say more robust here, which is directly related to what is being measured (the fragility of the embedding). Stronger steganography implies strength in the steganographic sense and a measure of undetectability - something you are not measuring.

Could the strength of the diffusion be determined by estimating the amount of noise in the images in order to make this method completely blind? 

Please provide a table or plot of the performance metrics for the ablation studies.

### Soundness
3 good

### Presentation
4 excellent

### Contribution
3 good

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
In my subjective opinion, authors are solving wrong problem. At the moment, steganography based on deep learning is very detectable (in the sense of evaluation under Kerkchoff's principle), since it generates images with non-natural noise. Moreover, the capacity of steganography based on deep learning is very inferior in terms of capacity to classical steganography by cover modification, where to my knowledge the state of the art is [1]. This means that rational attacker has a little incentive to use suboptimal methods, where better ones exists.  

Needless to say, state of the art steganography is usually fragile, which means that changing a single pixel might (in modern scheme very likely will) make the extraction of the message impossible. With the respect, the proposed work is not solving the right problem, since modern algorithm certainly do not survive JPEG compression. Of course, there are works on making steganography robust [2], but at the expense of the capacity, as part of the capacity needs to be reserved for the error correction.  

With respect to the above, I have found the work very shallow. It claims that existing techniques for steganography by cover modification does not work without even trying. Moreover, the comparison would not be made equal, because of differences in capacity, choice of the algorithm by the attacker.


[1] Bernard, Solène, et al. "Backpack: a Backpropagable Adversarial Embedding Scheme." IEEE Transactions on Information Forensics and Security 17 (2022): 3539-3554.

[2] Kin-Cleaves, Christy, and Andrew D. Ker. "Adaptive steganography in the noisy channel with dual-syndrome trellis codes." 2018 IEEE International Workshop on Information Forensics and Security (WIFS). IEEE, 2018.

[3] Solanki, Kaushal, Anindya Sarkar, and B. S. Manjunath. "YASS: Yet another steganographic scheme that resists blind steganalysis." Information Hiding: 9th International Workshop, IH 2007, Saint Malo, France, June 11-13, 2007, Revised Selected Papers 9. Springer Berlin Heidelberg, 2007.

### Strengths
I good list of prior art but misses some state of the art.

### Weaknesses
 I think the solved problem is not interesting.
* The experimental evaluation is poor. It misses prior art about which authors say it would not work (I would like to see it does not work). There is a lot of prior art in watermark removal. You should show that they do not work.
* The capacity of images of size 32x32 (size of images in Cifar 10) will be very small, which means that the experimental settings are distant from the reality

### Questions
* Have you tried basic JPEG compression and recompression with different quality factors? 
* Why you have not tried methods from the famous stirmark test?
* What is the length of the message you have hidden into the images?

### Soundness
2 fair

### Presentation
2 fair

### Contribution
1 poor

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

### Summary
This manuscript first proposed a diffusion model framework to sanitize steganography and preserve image quality in the sanitization process. However, the literature research on the field of sanitation hidden message is insufficient, and there is a lack of experiments, not only the sanitation evaluations on various robust steganography [1~5], but also the comparison with other sanitation methods [6~10].

### Strengths
(1) This manuscript first utilizes a diffusion model framework to sanitize universal and dependent steganography.

(2) This manuscript is well written.

### Weaknesses
（1）	The application scenario in this article is not clearly described. The two use cases mentioned in the penultimate paragraph of the manuscript have been replaced by robust steganography, a more suitable tool. Robust steganography has been developed for many years [1~5] and is not mentioned in this article, which is a lack of research.

（2）	This manuscript lacks research on relevant literature of sanitization methods for robust information hiding [6~10]. The authors should not define their previous work [11] as the state of the art easily.

（3）	At the end of the abstract, the authors propose DM-SUDS is the first blind deep learning image sanitization framework to meet these image quality results. I suggest the authors read the literature [10].

（4）	In subsection of 2.2 SANITIZATION, it is not rigorous to indicate that text-based secrets are more fragile than image-based secrets. The authors should conduct experiments to verify the robustness of text-based secrets embedded by robust steganography (such as DMAS [1]) and image-based secrets hidden by UDH [12].

（5）	In section of ANALYSIS AND DISCUSSION, the DM-SUDS also be evaluated on ImageNet. Conducting more experiments with more complex images is indeed necessary, however, the evaluation is limited only to LSB. We all know that LSB is not robust and can be disabled by common JPEG compression. It is meaningless to sanitize the secret messages embedded by LSB. LSB method can not transmit messages over lossy channels such as online social networks.

### Questions
See Weaknesses

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
3: You are fairly confident in your assessment. It is possible that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work. Math/other details were not carefully checked.

### Summary
This paper proposes a novel image sanitization approach based on diffusion models. The method achieves better image quality preservation compared with the state-of-the-art SUDS (a paper published in 2023).

### Strengths
+ The contribution of this work is well-positioned. 
+ The experiments support the contribution well.

### Weaknesses
 - It would good if the authors can delve into the mechanism of why diffusion model can help improve the image quality preservation of SUDS. For example, provide more discussions. 
- The methodology of this work is somehow incremental. If the authors could address more clearly about the advantages of introducing the diffusion (even with some demonstrative experiments), it would be better.

### Questions
As mentioned in the weakness part.

### Soundness
3 good

### Presentation
3 good

### Contribution
3 good
