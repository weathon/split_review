# Robust Conformal Prediction with a Single Binary Certificate

- Decision: Accept
- Avg Score: 7.00
- Scores: 8, 8, 6, 6

## Abstract
Conformal prediction (CP) converts any model's output to prediction sets with a guarantee to cover the true label with (adjustable) high probability. Robust CP extends this guarantee to worst-case (adversarial) inputs. Existing baselines achieve robustness by bounding randomly smoothed conformity scores. In practice, they need expensive Monte-Carlo (MC) sampling ($\sim10^4$ samples per point) to maintain an acceptable set size. We propose a robust conformal prediction that produces smaller sets even with significantly lower MC samples (e.g. 150 for CIFAR10)
Our approach binarizes samples with an adaptive bin selected to preserve the coverage guarantee. Remarkably, we prove that robustness can be achieved by computing *only one* binary certificate, unlike previous methods that certify each calibration (or test) point. Thus, our method is faster and returns smaller robust sets. We also eliminate a previous limitation that requires a bounded score function.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This work attempts to solve the "robust conformal prediction" problem, where we seek to construct conformal sets that satisfy the desired coverage guarantee at test time under worse-case distribution shift  between calibration and test data (adversarial perturbation). The baseline in this direction (RSCP) uses test-time robustness, where in contrast, this paper builds on a previous result, Zargarbashi et al., which utilizes the CDF structure of the conformity scores and constructs CDF aware sets (CAS), outperforming RSCP. This work in particular, is able to improve on CAS by manipulating the distribution of "smoothed" conformity scores. 
They are able to show improvements with respect to CAS in terms of 1. length-efficiency of the prediction sets, 2.  lower Monte Carlo sampling budget and faster computation of the prediction sets compared to CAS, 3. Removing the need for boundedness assumption on the conformity scores.

### Strengths
1. Attempts an important problem: uncertainty quantification with CP in the presence of adversarial perturbations. 

2. This paper is able to address a major limitation of the SOTA methods ( CAS and RSCP ) by reducing the Monte-Carlo sampling budget. 

3. The sets under RSCP/CAS are trivially large. This work is able to construct smaller prediction sets, and hence taking a step towards mitigating this sub-optimality of the current methods. 

4. The experiments are extensive and support the author's claims. 

5. The binarization of the distribution of the smooth scores is theoretically grounded.

### Weaknesses
 1. This paper does not address conditional coverage guarantees, which is of high relevance.
2. limited in the scope of attacker motives. particularly this paper only addresses the problem when the attacker seeks to reduce empirical coverage, and does not consider alternative goals.

### Questions
1. Can the authors elaborate on the effect of binarizing the distribution of smooth conformity scores on class-conditional coverage. The results seem very attractive in that they reducing MC-sampling budget and give smaller prediction sets, and but there are no experiments showing the effects on class-conditional coverage. (Are there any inherent limitations posed when binarizing the distribution of smooth conformity scores? i.e any information lost?)

2. How does BinCP perform compared to RSCP+ ( Yan et al. 2024) which also propose a transformation of the smooth score and achieve smaller prediction set sizes than RSCP. In addition to line 467 and 51, could you address whether/how the calibration-time robustness (binCP) can be applied on top of/combined with test-time robustness (RSCP+), and if that is not the case, could you elaborate further on comparing the two methods in terms of how efficient each are in improving the size of the prediction sets, or the consistency of the improvement trends observed for each.

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
The paper introduces a new algorithm for robust conformal prediction. The algorithm boils down to a combination of monte-carlo sampling + binarization that yields a new conformal score; this score can then be inverted into a prediction set (also accounting for the fact that the test $\tilde{x}$ may be noisy). Experiments show this approach is an order of magnitude more sample efficient and substantially faster than the previous state-of-the-art.

### Strengths
* Empirical results are compelling in terms of runtime and sample size improvement.
* Well written.

### Weaknesses
 * Paper readability could be improved for non-experts in TCS like myself, who are not acquainted with “certificates” and with the prior work of Zargarbashi et al.

The conditioning in (1) does not seem formally correct to me. (I’m aware there are some differences in language between TCS and statistics that may be at play here.) My understanding is that $\tilde x_{n+1} \in \mathcal{B}(x_{n+1})$ holds deterministically (i.e., with probability 1). So what is the point of the conditioning? Why would you ever even allow the possibility that $\tilde x_{n+1} \notin \mathcal{B}(x_{n+1})$ in your threat model?

Theorem 1 comes way out of the blue in terms of notation.

___

Zagarbashi et al. reference is broken (no year)

“First, we get robust coverage with only a single certificate computation, while at least one certificate per calibration (or test) point.” Typo. Also, I did not fully understand this.

“also satisfy Eq. 1 (calibration-time)” is this a typo in Theorem 1?

“when we do need sample correction, working with binary variables allows us to use tighter concentration inequalities” This statement confuses me because this is rarely true. Binary random variables generally have the _worst_ concentration properties of all bounded random variables in [0,1], not the best.

### Questions
“when we do need sample correction, working with binary variables allows us to use tighter concentration inequalities” This statement confuses me because this is rarely true. Binary random variables generally have the _worst_ concentration properties of all bounded random variables in [0,1], not the best.

### Soundness
4

### Presentation
3

### Contribution
4

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
The work presents a conformal prediction that further ensures adversarial robustness. This can be done by modifying the use of the conformity scores in either the calibration or prediction procedures, by the means of upper/lower bounds on particular adversarial objectives combined with inference of means (e.g. by Monte Carlo). This work further proposes that this adversarial objective should be of binary nature. By doing so they achieve tighter intervals and more efficient inference of the means (as the binary nature of the samples makes this estimation easier), and thus more efficient calibration/prediction.

### Strengths
The paper's contribution is solid. The proposed method has favorable theoretical properties, is widely applicable, and is empirically shown to significantly outperform previously available methods.

### Weaknesses
The paper is strong overall. Its weaknesses are, essentially:
(i) several typos;
(ii) some notation that needs to be made more consistent;
(iii) a couple of minor corrections necessary; and
(iv) a couple of confusing paragraphs.

Of these, of course, (iv) is the most severe.

(i) Typos:
- Line 088: 'finnaly'
- Line 096 and 144: the authors seem to use `\mapsto` for the 'function declaration' notation $f : X \to Y$; usually one uses just `\to`. (At least I don't think I've ever seen `\mapsto` used in this context).
- Line 161: missing a closing bracket on the indicator.
- Line 189: 'differ' -> 'defer'
- Line 223: missing an article before the $\bar{s}\_y(x) = [\cdots]$
- Lines 229-234: is the lack of the $y$ subscript intentional? I understand that what is being said in that paragraph is more general, but as far as I can tell it is then applied to $f_y$ (rather than some general $f$ or other function), and the lack of the subscript made this paragraph a bit confusing. Furthermore, the following paragraphs seem to act as if $f_y$ was used here...
- Line 236: $c^\uparrow$, not $c^\downarrow$
- Line 246: 'they are just need'

(ii) Notation:
- The paper currently mixes different notations for indicators (both $\mathbf{1}$ and $\mathbb{I}$). Pick one and stick with it.
- Line 238: $r$ was not properly introduced, as far as I can tell
- It's worth noting that the authors seem to use conformity scores 'flipped': in their use, a high conformity score would correspond to a high belief that $y$ conforms to $x$, whereas in the typical literature is the opposite. This doesn't need to be changed, but deserves to be explicitly said.

(iii) Minor corrections:
- The quantile calibration for Split Conformal Prediction requires a modified quantile, not just $\mathbb{Q}(\alpha; \{s\_i\}\_\{i=1\}^n)$. You need to either include $+\infty$ ($\mathbb{Q}(\alpha; \{s\_i\}\_\{i=1\}^n \cup \{+\infty\})$) or modify the level ($\mathbb{Q}(\alpha (1/n + 1); \{s\_i\}\_\{i=1\}^n)$ when the conformity score is the other way around, if I am not mistaken).
- Lines 129-131: perhaps could be a bit more formal? The current wording "the radius of the smallest ball around x that contains a point \tilde{x}" is slightly ambiguous. It should specify that the ball is centered at x.

(iv) Confusing paragraphs:
- I could not understand lines 246-250 (and thus the paragraphs that follow), and question their correctness -- or at least their presentation. Specifically, the claim that the solution to Eq. 5 is independent of the point and the function f is not immediately obvious and requires further justification. The connection between the lower bound and the scalar p is also not clear. Nevertheless, the work does seem not hinge on this particular point, so I don't consider this major (though it should be fixed/improved!).
- Lines 173-181 were also a bit confusing to read, but seemed reasonable. Either way, the theoretical result they are alluding to is formalized in Lemma 1, which is satisfyingly proven by Conformal Risk Control.

### Questions
- Lines 129-131: To be totally formal, this should use $\mathcal{B}^{-1}$, right?
- Line 238: what is $r$?
- Could the authors clarify lines 246-250?

*Score:* the paper carries a meaningful contribution and seems reasonably solid, and thus I lean towards acceptance. However, the presentation (and possibly a couple of paragraphs) need to be fixed/improved, which keep me from giving a higher score. Should they be fixed, I would be happy to increase my score accordingly.

### Soundness
2

### Presentation
2

### Contribution
4

---

## Human Reviewer 4

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
The authors proposed a robust conformal prediction scheme using binarized smooth scores via thresholding. The binarized prediction sets are computationally efficient with fewer MC samples.

### Strengths
The binarized conformal prediction sets are easy to compute and takes simple form. The claim is supported with numerical experiments. Discussions and comparison with previous methods are sufficient.

Discussion: The authors addressed my concerns and I updated my score.

### Weaknesses
1. It is confusing in the abstract to use specific numbers (e.g. $10^4$ and $10^2$) without any given context. What is the dataset and experiment setup?
2. It is not clearly explained why nonbinarized robust CP require significantly more MC samples. Can the authors provide a theorem? Or if there is intuitive explanation?
3. The authors mentioned that working with binarized variables allows using the tighter concentration inequalities and Clopper & Pearson confidence intervals. However, this is not formally defined, and it's not clear why a good concentration bound will imply lower sample size.
4. The numerical experiments seem to suggest the method is indeed superior requiring lower MC sample size. However, the paper lacks discussion of why this occurs nor theoretical guarantees for sample size are given.

### Questions
See weakness.

### Soundness
3

### Presentation
3

### Contribution
3
