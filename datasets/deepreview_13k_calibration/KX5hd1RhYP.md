# Average Certified Radius is a Poor Metric for Randomized Smoothing

- Decision: Reject
- Avg Score: 4.67
- Scores: 3, 5, 6

## Abstract
Randomized smoothing is a popular approach for providing certified robustness guarantees against adversarial attacks, and has become a very active area of research. Over the past years, the average certified radius (ACR) has emerged as the single most important metric for comparing methods and tracking progress in the field. However, in this work, we show that ACR is an exceptionally poor metric for evaluating robustness guarantees provided by randomized smoothing. We theoretically show not only that a trivial classifier can have arbitrarily large ACR, but also that ACR is much more sensitive to improvements on easy samples than on hard ones. Empirically, we confirm that existing training strategies that improve ACR reduce the model's robustness on hard samples. Further, we show that by focusing on easy samples, we can effectively replicate the increase in ACR. We develop strategies, including explicitly discarding hard samples, reweighing the dataset with certified radius, and extreme optimization for easy samples, to achieve state-of-the-art ACR, although these strategies ignore robustness for the general data distribution. Overall, our results suggest that ACR has introduced a strong undesired bias to the field, and better metrics are required to holistically evaluate randomized smoothing.

## Human Reviews

## Human Reviewer 1

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
This submission studies the metric of average certified radius (ACR) in randomized smoothing training literature. First, the submission theoretically shows that ACR is ill-posed in terms of unboundedness for trivial toy classifiers and uneven sensitivity for easy and hard samples. Then, harnessing these features, a training method that overly focuses on easy samples can hack the metric to achieve a state-of-the-art ACR.

### Strengths
1. Revealing the problem of ACR to the randomized smoothing community, which rectifies the past error and promotes a more scientific evaluation protocol.

2. Technically sound and clear writing.

### Weaknesses
1. The impact is limited. ACR is a rather specific metric that mainly exists in the randomized smoothing literature. Moreover, in the literature, ACR is used in conjunction with certified accuracy under various radii - as a poor metric, the community is not overly focused on the metric yet.

2. Technical contribution is limited. It is relatively obvious to see the unboundedness of ACR (for a constant classifier) and the sensitivity with respect to $P_A$ is a direct consequence of $\Phi^{-1}(\cdot)$'s bounded domain and unbounded value domain.

3. The paper is overly focused on a narrow topic and can be benefited from better contextualization. For example, for randomized smoothing, diffusion-purification is an active and developing method, such as "(Certified!!) Adversarial Robustness for Free!", DensePure, and DiffSmooth; ensemble-based training is also widely studied such as Horvath et al (boosting) and Yang et al (on the certified...). 


Minor:
The implication of Figure 1 on page 1 is not clear.

### Questions
No specific questions.

### Soundness
3

### Presentation
3

### Contribution
1

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper discusses the limitations of using the Average Certified Radius (ACR) as a primary metric for evaluating robustness in Randomized Smoothing (RS), a technique used to defend machine learning models against adversarial attacks. The authors argue that ACR disproportionately focuses on easy samples and can be artificially inflated, even by trivial classifiers. Their key contributions include:
1.	Theoretical Analysis: The paper shows that a trivial classifier can achieve arbitrarily large ACR given a sufficient certification budget, proving that ACR is unreliable as a robustness measure.
2.	Empirical Findings: They demonstrate that existing state-of-the-art (SOTA) RS training strategies, which improve ACR, reduce model accuracy on hard samples, thus prioritizing easy samples.
3.	Proposed Solutions: The authors introduce training modifications—such as discarding hard samples, reweighing data based on certified radius, and applying adaptive adversarial attacks—that achieve a new SOTA ACR by focusing only on easy samples. These strategies improve ACR but ignore general robustness.

### Strengths
This paper presents a fact that the Average Certified Radius (ACR) is an unfair metric for evaluating robustness in Randomized Smoothing (RS), which is helpful to future research on Randomized Smoothing.

### Weaknesses
1. Novelty is relatively limited. The first contribution suggests that the Average Certified Radius (ACR) can be increased arbitrarily by enlarging the sample size. However, [1] also finds that certified accuracy is closely related to sample size. Figure 4(a) in [1] demonstrates that as pA -> 1.0, the certified radius significantly increases with sample size. The existence of [1] diminishes the novelty of this paper, which also fails to reference this closely related work.

2. The logic of this paper is somewhat unnatural. While it proves that ACR is a poor metric because it favors easy samples, it would be more logical to design a more reasonable metric. Instead, the paper proposes a new training algorithm that gives more weight to easy samples, exploiting the weakness of the ACR metric to increase ACR.

3. The proposed training algorithm requires using Projected Gradient Descent (PGD) to compute adversarial examples, which is computationally expensive. This is why methods like MACER and consistency, choose attack-free training algorithms to mitigate computation costs.

### Questions
1. Recognizing that ACR is an inadequate metric, please include a more detailed discussion on designing a more effective comparison metric.
2. The training algorithm presented is based on adversarial methods; please add a comparison regarding computational overhead.

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
5

### Summary
This paper evaluates the effectiveness of **Average Certified Radius (ACR)**, a popular metric for assessing model robustness against adversarial attacks, particularly within the context of **Randomized Smoothing (RS)**. The authors specifically target **existing training strategies**, showing that these methods provide a misleading sense of general robustness.

They prove that a trivial classifier can achieve arbitrarily high ACR with a large certification budget, despite being unreliable. Additionally, they demonstrate that ACR disproportionately benefits from improvements on "easy" samples, with gains potentially over 1000x greater than those on "hard" samples. Through experiments, they reveal that state-of-the-art (SOTA) RS training methods inflate ACR by focusing on easy inputs while sacrificing robustness on harder samples. To further critique ACR, the authors propose strategies to boost ACR artificially, such as discarding hard inputs and reweighing data, reinforcing the bias toward easy samples.

The paper concludes by highlighting the limitations of ACR, presenting experimental evidence, and advocating for a shift in how the field evaluates robustness in **randomized smoothing**, suggesting **certified accuracy at various radii** as a more reliable alternative metric.

### Strengths
1. **Originality and Significance:** The paper presents an original and critical perspective on a widely accepted metric in adversarial robustness, the **Average Certified Radius (ACR)**, which has been largely unchallenged in the literature. By demonstrating that ACR is a flawed metric for evaluating randomized smoothing (RS) models, the authors provide a fresh lens through which the community can reevaluate robustness. By exposing the weaknesses of ACR, the paper has significant implications for future research in the field of certified defenses. 

2. **Quality:** The theoretical analysis is well-supported by empirical results, making the paper technically sound. The authors back their theoretical claims with well defined experiments that verify their theoretical findings. The experiments are well-designed, with appropriate baselines and metrics to validate the claims. The paper covers a lot of **training based RS stratagies** to support their claims which further adds to the experimental aspect of this work.

### Weaknesses
1. **Limited Scope**: The paper lacks proper clarity on one aspect, wether it's findings are specific to **training-based RS methods** or **Randomized Smoothing** in general.  If I understood correctly, than the theoretical analysis in section 4.1 is not specific to **training based RS methods**, but during evaluation the paper mainly critiques **ACR** for **training-based RS methods** but doesn't extend/discusses the impact of theoretical analysis to **other RS methods**, which also rely on ACR to evaluate certified robustness. Expanding the critique to cover these methods would provide a more comprehensive view and increase the impact of the findings. Specifically, the paper does not address how the identified issues with ACR manifest in non-training based RS methods, such as those that rely on pre-trained models with added noise for certification. This omission leaves a gap in understanding the generalizability of the critique.

2. **Lack of Practical Guidance**: While the authors propose **certified accuracy at various radii** as an alternative metric, they don’t provide detailed guidance on how to implement it effectively in practice. Offering concrete steps or case studies on how this metric can be integrated into evaluation pipelines would make the solution more actionable. Furthermore, **certified accuracy at various radii* is a metric which is more commonly used, compared to ACR, to evaluate **other RS methods**, hence this further limits the scope of the work as it adds to the point that this work is only relevant to **training-based RS methods**.

### Questions
I mainly have two questions based on the points mentioned in weaknesses above, If they can be answered properly, specifically question 1, then I am willing to increase the rating.

1. Could you clarify how the limitations of **ACR** apply to **other RS methods**? Since ACR is also used in these methods to evaluate certified robustness, how do your findings extend to these approaches? It would be helpful to understand whether ACR is equally flawed in these contexts. Or if the work is specific to **training-based RS methods**?

2. You propose using **certified accuracy at various radii** as an alternative to ACR. Could you provide more specific guidance on how this should be applied in practice? For example, how should practitioners choose appropriate radii, and how would this approach balance performance across easy and hard samples?

### Soundness
3

### Presentation
2

### Contribution
3
