# A Transfer Attack to Image Watermarks

- Decision: Accept
- Scores: 6, 6, 6, 8

## Abstract
Watermark has been widely deployed by industry to detect AI-generated images. The robustness of such watermark-based detector against evasion attacks in the white-box and black-box settings is well understood in the literature. However, the robustness in the \emph{no-box} setting is much less understood. In this work, we propose a new transfer evasion attack to image watermark in the no-box setting. Our transfer attack adds a perturbation to a watermarked image to evade multiple surrogate watermarking models trained by the attacker itself, and the perturbed watermarked image also evades the target watermarking model.  Our major contribution is to show that, both \emph{theoretically} and \emph{empirically},  watermark-based AI-generated image detector is not robust to evasion attacks  even if the attacker does not have access to the watermarking model nor the detection API.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The paper proposes a transfer attack to (learned/learning-based) image watermarking that first trains a lot of surrogate watermarking models (encoders + decoders), then uses PGD to find a perturbation to the watermarked images that would change the extracted watermarks by the surrogate watermarking models.

It is argued that such approach requires smaller perturbations to break learning-based watermarking when being compared to common post-processing such as JPEG, Gaussian noise, Gaussian blur, and Brightness/Contrast; and it is more effective than existing transfer attacks.

### Strengths
The robustness of image watermarking in no-box setting (i.e. with no access to watermarking models & with no access to detection API) is indeed a relatively overlooked area. Given that there are empirical ways to at least restrict the access to models/APIs, I consider this angle meaningful and worth investigating.

The presentation is clear enough overall and originality of this paper is not an issue.

### Weaknesses
My primary concerns regarding this paper are:
1. **No analysis of the computational cost in comparison with existing transfer attacks, which should be discussed clearly**. I think while the proposed method definitely incur a much larger overhead compared to previous attacks, it could still be ok to highlight the risks, providing that this limitation is presented upfront in the paper. Some analysis + some empirical numbers of computation time (with the corresponding compute resources) could be helpful for illustration.

2. **The comparison of the proposed attack with existing transfer attacks is somewhat inconclusive.**
This is because, as the authors must already know, there is a trade-off between evasion rate and the visibility/budget of the attacks (perturbation in L2/perturbation in Linf/SSIM/...). Thus a good comparison should at least compare the evasion rates with **all** baselines in representative budgets (if the other baselines work in such budgets). However, the comparison in the paper claims the proposed method is better than all others because it beats some baselines when r<= 0.1, and it beats MI-CWA and DiffPure assuming a SSIM>0.9. This is a rather misleading way of comparison, as some attacks will work better under certain (metrics of) budgets but not the others.

3. **The effectiveness of the proposed method as a "no-box" attack remain unclear, specifically regarding the transferability to different watermarking methods.**
While there are experiments involving a different target watermarking method from the surrogate ones, it is worth noting that these methods are somewhat similar (or as the authors called, they are learning-based watermarking). It is claimed that the proposed method also work for non-learning based methods (figure 13), but details regarding this set of experiments, especially what are the target watermarking methods, are missing. To my understanding, there is no rule preventing the victim using a watermarking scheme that is very different or even designed to be different from the ones used by the attacker as surrogates. This is not a deal breaker but such discussion seems to be missing.

### Questions
Please see Weaknesses for my primary concerns, which also include some of my suggestions/questions for the authors.

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This paper proposed an evasion attack to interfere with the detection of watermarked images under the no-box setting, i.e. the attacker has no access to the watermark detector. They approach the objective through the transfer attack, where they train surrogate watermark models and find adversarial perturbation to fool the detection of local surrogate models. Both theoretical analysis and empirical evidence demonstrate that this transfer attack method can successfully undermine the detection capabilities of learning-based watermark systems across various watermarking scenarios.

### Strengths
1. This paper is well-written with clear motivation. The no-box setting is practical.
2. The experiments and theoretical results support their claims and method design.
3. The transfer results are effective against several learning-based watermarking systems.

### Weaknesses
1. While I acknowledge the authors have assumed that the attackers should have sufficient computational resources, the main concern of this paper is the computational cost. The costs associated with both surrogate models and perturbation discovery are large which prevents the practical usage of this method.  
2. For the transfer attack to a specific architecture such as ResNet-18, did you use a similar architecture in your surrogate models, for instance, ResNet-X? Besides, have you considered attacks with totally different architectures, such as transformer-based watermark models?
3. Another weakness of this paper is that the transfer attack primarily focuses on learning-based watermarks, neglecting non-learning-based watermark variants that may exhibit greater robustness than the baselines discussed here, such as variants of Tree-Ring [1][2], etc. Besides, can the proposed method attack the 0-bit watermark? 
The cost of attacks escalates significantly with complex architectures a
4. The attack cost is significantly increased with complex architectures and longer watermarks. This poses a hindrance to the practical implementation of transfer attacks involving high-capacity watermarks [3].

### Questions
Please see the weaknesses.

### Soundness
3

### Presentation
4

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
This paper demonstrates that watermark-based detection methods for AI-generated images are vulnerable to transfer attacks in a no-box setting. Specifically, an attacker can effectively remove the watermark from a given watermarked image by applying a perturbation, which can be identified through ensembling multiple surrogate watermarking models.

### Strengths
This paper presents a practical attack effective across multiple watermarking methods
The issue of watermarking the outputs of generative models is timely and interesting.

### Weaknesses
To ensure high image quality, the L infinity bound on perturbations should be kept low, as higher values (e.g., 0.2 as shown in Figures 3 and 4) can noticeably degrade image quality, reducing practicality. For a more realistic assessment, the paper should include comparisons using a set of small enough  L infinity bound (such as 0.03, 0.05) bounds to demonstrate the proposed method’s effectiveness under conditions that minimize visible impact.
If Section 5 is one of the paper’s main contributions, it would be better placed in the main text rather than in the appendix.

### Questions
See weakness

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
This paper develops an attack that evades a target image watermarking detector, without acquiring the access to this detector's model or API. The proposed method adds a perturbation trained to mislead multiple surrogate detector models, and hopes that this perturbation can transfer to the target detector and therefore succeed. The experiment results on various datasets demonstrate the effectiveness of the proposed method, which outperforms many existing attacks and post-processing methods.

### Strengths
1. The paper is well-written and easy to follow.
2. This paper proposed an intuitive yet attractive method that seems work very well in the experimental studies. 
3.  The experimental studies are comprehensive.

### Weaknesses
 **Major Concerns:**

1. Theoretical contributions. While authors provide some theoretical analysis, I think the current results are not sufficient to be claimed as signficant. The reasons are as follows:
(1) It is in doubt whether those independence assumptions will hold. As $\delta$ is obtained by solving Eq. (3), which optimizes the chances that $m$ decoders will extract carefully designed watermarks from an image perturbed by $\delta$, it is likely that coordinates of decoders' output is correlated. The authors may want to provide additional envidence to validate their assumptions. Specifically, the optimization process in Eq. (3) is designed to maximize the probability of incorrect watermark extraction across multiple surrogate models. This inherently introduces a dependency between the outputs of these models, as they are all being manipulated by the same perturbation. The assumption of independence, therefore, seems questionable without further justification. Furthermore, the specific nature of the correlation (positive, negative, or mixed) is not addressed, which could significantly impact the validity of the theoretical bounds.
(2) The analysis only applies to inverse-decode.
(3) The bound given by the theorems are not available in practice. Recall that this paper considers the setting where $T$ and its output is unknown to the attacker. In the meanwhile, the parameters including $a, b,\beta, p$ involves the unknown target decoder $T$ and unknown data distribution. The theoretical bounds rely on parameters that are directly tied to the target decoder's behavior and the underlying data distribution, which are explicitly stated as unknown to the attacker. This makes the theoretical analysis difficult to interpret in the context of the practical attack scenario, as the bounds cannot be calculated or validated without knowledge of these unknown quantities. The practical utility of these bounds is therefore limited, and it is unclear how they provide insight into the attack's performance in realistic settings.

2. Empirical results. The empirical results are impressive, and it raises my question why it significantly outperforms SOTA methods? Could the author provide any justification and insight for the superior performance of the proposed method?


**Minor Concerns:**

1. Since the proposed method has to train a bunch of surrogate models, will it be computationally expensive? Also, every time this algorithm has to solve Eq. (3), which may also be expensive. The authors may want to add a table comparing the FLOPs and time used by different methods.

### Questions
Please see the weakness section above.

### Soundness
4

### Presentation
3

### Contribution
3
