# Fast Adversarial Training against Sparse Attacks Requires Loss Smoothing

- Decision: Reject
- Avg Score: 6.00
- Scores: 6, 6, 6

## Abstract
This paper studies fast adversarial training against sparse adversarial perturbations. We highlight the challenges faced when employing $1$-step attacks on $l_0$ bounded perturbations for fast adversarial training, including degraded performance and the occurrence of catastrophic overfitting (CO). We highlight that CO in $l_0$ adversarial training is caused by sub-optimal perturbation locations of $1$-step attack, which is distinct from other cases. Theoretical and empirical analyses reveal that the loss landscape of $l_0$ adversarial training is more craggy compared to its $l_\infty$, $l_2$ and $l_1$ counterparts. Moreover, we corroborate that the craggy loss landscape can aggravate CO. To address these issues, we propose Fast-LS-$l_0$ that incorporates soft label and the trade-off loss function to smooth the adversarial loss landscape. Extensive experiments demonstrate our method can overcome the challenge of catastrophic overfitting, achieves state-of-the-art performance and narrows down the performance gap between $1$-step and multi-step adversarial training against sparse attacks.

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper investigates FAT against sparse adversarial perturbations bounded by the $L_0$ norm, highlighting the challenges associated with FAT, including performance degradation and catastrophic overfitting phenomenon. The authors propose Fast-LS-$l_0$, which incorporates soft labels and a trade-off loss function to smooth the adversarial loss landscape. Experimental results show the effectiveness of the proposed method against sparse attacks.

### Strengths
1.	Research on FAT under $L_0$ norm constraints is relatively limited, and the authors address this gap by proposing an innovative method to mitigate performance degradation and catastrophic overfitting in FAT.

2.	The authors provide detailed theoretical insights into the connection between the non-smooth adversarial loss landscape and catastrophic overfitting, giving clarity to the existing issues from the theoretical perspective.

3.	The paper is well-organized and clearly explained, and extensive experiments across diverse datasets validate the robustness of the proposed method.

### Weaknesses
1.	The novelty is somewhat limited, as many techniques, including soft labels and TRADES loss, are widely used in adversarial defense. The overall method may appear as a straightforward integration of existing techniques.
2.	The application scenario is not clearly defined, particularly why robustness under the $L_0$ norm constraint is essential. Can this adversarial training effectively enhance defense against one-pixel attacks?
3.	The application scenario is unclear, and it is unclear why the model needs to be more robust under the $L_0$ norm constraint. Can this adversarial training enhance the defense capability under the one-pixel attack? 
4.	Whilemost current methods are based on $L_{\infty}$ norm constraints, the author should show the performance of these methods under $L_0$ constraints, such as FAST-GA[1], FAST-BAT[2], FAST-PCO[3].

### Questions
1.	Can Fast-LS-$l_0$ be adapted for other sparse attacks, such as those bounded by $L_1$?
2.	Does the trade-off loss function parameter $\alpha$ need to be adjusted across different datasets and tasks?
3.	Could you further elaborate on the necessity of adversarial training under the $L_0$ constraint?

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This work studies the fast adversarial training, usually the single-step adversarial training (AT), in the setting of $\ell_0$-bounded sparse adversarial perturbation. It first identifies the phenomenon of catastrophic overfitting in $\ell_0$ fast AT and the accounts for it, sub-optimal perturbation locations and non-smoothness of the loss landscape. It then proposes to incorporate soft label and trade-off loss function into $\ell_0$ fast AT to smooth loss landscape to mitigate catastrophic overfitting.

### Strengths
1. The presentation is easy to follow
2. The proposed method is well-motivated.
3. The experimental results verify the effectiveness of the proposed method in mitigating catastrophic overfitting in $\ell_0$ fast AT.

### Weaknesses
1. The studied problem, catastrophic overfitting in $\ell_0$ fast AT, is quite narrow. It considers a very specific case, $\ell_0$, of the $\ell_p$ adversarial setting. The impact of this work's conclusions on the entire field, adversarial machine learning, is therefore limited. The focus on $\ell_0$ perturbations, while relevant in some contexts, does not address the broader challenges of adversarial robustness across different threat models. The insights gained may not generalize to other $\ell_p$ norms, which are more commonly studied and have different characteristics in terms of the geometry of the perturbation space and the resulting loss landscape.
2. The analytical framework and the findings are similar to the existing works of analyzing overfitting in AT. Some of them are already cited in this work, while some else are missing. For example, [1] also attributes overfitting in AT to the degradation of training adversary and the complication of loss landscape throughout training, and proposes to integrate loss landscape smooth techniques into AT to mitigate overfitting. However, I acknowledge that some conlcusion of this work, like the one about sub-optimal perturbation location, seems to be unique to the setting of $\ell_0$ and useful.  
3. The mitigation methods, soft label and trade-off loss function, are proposed by the exiting works, so the methodological contribution of this work is the discovery of the effectiveness of existing methods in mitigating catastrophic overfitting in $\ell_0$ fast AT, but not something novel like proposing a new method. However, as mentioned in Weakness 2, the idea of mitigating overfitting in AT through loss smoothing has been already explored in the existing works, despite that different smoothing techniques are employed.

### Questions
Please find above.

### Soundness
3

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
This paper explores the challenges and solutions for catastrophic overfitting within 1-step adversarial training targeted at sparse adversarial perturbations bounded by the  $L_0$  norm. 
Through a comprehensive analysis, the authors illustrate that the CO issue in $L_0$ norm stems from a more craggy loss landscape compared to its $L_{\infty}$,  $L_2$, and  $L_1$ counterparts.
To address these challenges, the authors propose incorporating soft labels and a trade-off loss function, strategies specifically designed to smooth the adversarial loss landscape associated with $ L_0$  norm 1-step adversarial training.

### Strengths
This work is the first to investigate fast adversarial training in the context of $L_0$ bounded perturbations.

The authors successfully demonstrate that the CO issue in the $L_0$ norm is caused by sub-optimal perturbation locations,  rather than sub-optimal perturbation magnitudes via some interesting ablation studies.

This study conducts extensive experiments, including ImageNet and Transformer-based architectures.

### Weaknesses
Theoretical analysis indicates that large $\left\|\boldsymbol{\delta}_1-\boldsymbol{\delta}_2\right\|$ can intensify the gradient discontinuity, and  $L_0$ norm has the largest upper bound. 
However, directly comparing these upper bounds may not be a fair comparison due to the naturally larger freedom in change magnitudes associated with the $L_0$  norm. 
Could authors provide some empirical results of $\left\|\boldsymbol{\delta}_1-\boldsymbol{\delta}_2\right\|$ among different norms to support their claim?

It would be interesting to examine the performance of Expectation over Transformation (EOT) [1] and Backward Pass Differentiable Approximation (BPDA) [1] on the authors’ proposed method, which can effectively exclude gradient masking in 1-step adversarial training.

Recent advances in addressing CO by preventing loss landscape distortion with other norms [2,3,4,5] may also prove beneficial in alleviating CO in the $L_0$ norm and should be discussed.

### Questions
Refer to weakness.

### Soundness
3

### Presentation
3

### Contribution
3
