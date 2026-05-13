# Adversaries With Incentives:  A Strategic Alternative to Adversarial Robustness

- Decision: Accept
- Scores: 6, 3, 6

## Abstract
Adversarial training aims to defend against \emph{adversaries}:
malicious opponents whose sole aim is to harm predictive performance in any way possible---%
a rather harsh perspective, which we assert
results in unnecessarily conservative models.
Instead, we 
propose to model opponents as simply 
pursuing their own goals,
rather than working directly against the classifier.
Employing tools from strategic modeling,
our approach uses knowledge or beliefs regarding
the opponent's possible incentives as inductive bias for learning.
Our method of \emph{strategic training} is designed to defend against opponents within an `incentive uncertainty set':
this resorts to adversarial learning when the set is maximal,
but offers potential gains when it can be appropriately reduced.
We conduct a series of experiments that show how even mild knowledge regarding the adversary's incentives can be useful,
and that the degree of potential gains depends on how incentives relate to the structure of the learning task.
\squeeze

## Human Reviews

## Human Reviewer 1

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper introduces a new perspective in adversarial training by proposing that adversaries may act out of self-interest rather than pure malice. Traditional adversarial training models the adversary as seeking maximal harm to the classifier, requiring models to defend against all possible incorrect labels. This approach, while robust, can reduce model generalization and clean data accuracy. Instead, the authors propose a framework called strategic training, which considers opponents who act to maximize their own utility. By assuming that opponents pursue specific goals, this approach allows models to leverage knowledge about opponent incentives, defining an incentive uncertainty set to guide training.

### Strengths
- This paper identifies a favorable interpolation between natural training and adversarial training, in which many meaningful optimization problems with real-world significance are formulated.

- This paper provides a comprehensive investigation into the proposed types of strategic opponents, including adversarial, semantic, anti-semantic, preference ordering, and 1-hot.

- Thorough experiments demonstrate the gap between strategic attacks and adversarial attacks, as well as the effectiveness of the proposed strategic training method.

### Weaknesses
 - Regarding the question of "How much do we lose by being maximally conservative, and how much can we gain by appropriately reducing uncertainty," this paper offers an answer through experimental analysis but lacks a detailed theoretical examination. Specifically, while the experiments demonstrate the performance differences between strategic and adversarial training, they do not provide a theoretical framework to understand the underlying mechanisms causing these differences. For instance, it is unclear how the choice of specific utility functions impacts the convergence properties of the training process or the generalization bounds of the resulting models. A theoretical analysis could explore the relationship between the incentive uncertainty set and the robustness of the model, potentially using tools from game theory or robust optimization. 

- Strategic training requires a predefined utility function or set of utility functions; however, if the utility function is unknown, strategic training cannot proceed. This is a significant limitation as, in many real-world scenarios, the adversary's true utility function is not known and may even change over time. The paper does not provide a clear strategy for how to handle situations where the utility function is misspecified or how to adapt the training process when the adversary's behavior changes. This makes the practical applicability of the method dependent on the accuracy of the assumed utility function. 

- (Minor) A typo in Figure 1: "preferecnce" should be corrected to "preference."

### Questions
Is it possible in practice to estimate the opponent’s utility function based on some information such as historical attack data from opponents?

### Soundness
4

### Presentation
4

### Contribution
3

---

## Human Reviewer 2

### Rating
3

### Rating Number
3

### Confidence
5

### Summary
The paper considers a new adversarial scenario where an attacker has a non-uniform preference for target classes. It introduces a new adversarial training method, named strategic training, designed specifically to defend against such targeted attacks. It claims that prior knowledge of the attacker’s preferences can enhance both clean accuracy and strategic adversarial accuracy.

### Strengths
- The paper is well-written and clearly formalizes the proposed framework.

### Weaknesses
 - The proposed scenario seem impractical, as it is challenging for a defender to anticipate an attacker’s intent in advance. Additionally, an attacker’s preferences may shift over time, and there can be multiple attackers with varying preferences. This is why most work on adversarial robustness assumes a uniform preference among attackers.
- Although the proposed scenario is novel, the framework and its results seem straightforward. Constraining the attacker’s search space is expected to yield higher clean accuracy, reflecting the fundamental trade-off between accuracy and robustness. The core idea of limiting the attack space to specific directions or target classes, while novel, does not introduce a fundamentally new mechanism beyond the well-established principle that reducing the attack surface generally improves clean accuracy. The results, while demonstrating this effect, do not offer significant insights beyond this basic observation.
- The results in Table 1 appear inconsistent and unreliable. In the GTSRB experiment, strategically trained VGG and ResNet18 models achieve higher adversarial accuracy than standard adversarially trained models. This suggests that the evaluation method may be flawed; the authors should consider using stronger attack algorithms, such as AutoAttack [1]. Using a 20-step PGD attack is an outdated evaluation approach, more commonly seen in studies from 2018. The reported inconsistencies, such as strategic training outperforming adversarial training in some cases, raise concerns about the robustness and reliability of the evaluation methodology. The use of a relatively weak attack method like 20-step PGD further exacerbates these concerns, as it might not accurately reflect the true adversarial vulnerability of the models.

### Questions
See the weaknesses above.

### Soundness
1

### Presentation
3

### Contribution
1

---

## Human Reviewer 3

### Rating
6

### Rating Number
6

### Confidence
4

### Summary
This paper studies *strategically robust learning*, which fills the gap between adversarial learning and vanilla learning nicely. Specifically, the problem formulation is done in such a way that generalizes both cases. Extensive experiments are conducted to empirically verify the effectiveness of the proposed model and demonstrate the advantage of considering such strategic opponent scenarios instead of blindly chasing for the worst-case guarantees.

### Strengths
Overall,
1. Well-motivated research design, which fills the gap between the two extreme spectrums of adversarial training nicely.
2. Clear formulation for most parts of the presentation. 
3. Extensive experiments that cover a wide range of concerns. Each experiment is also well-motivated.

### Weaknesses
1. It seems like although we consider the set of all possible utilities to be $\Lambda = [0, 1]^{K \times K}$, the discussion is tailored towards $\{0, 1\}^{K \times K}$ instead. It is not immediately clear that all the discussions and analysis will follow through within for the more general $\Lambda$. I'm just curious whether it is possible to consider other than $0$-$1$ utilities in the experiment, since some of the categories, e.g., preferences, will make more sense for the case of $[0, 1]$ utilities.
2. Little emphasis on the algorithm description makes some of the claims not convincing. For example, what is the exact algorithm Line 364 referring to, i.e., "solving $\max_u$ independently for each row $u(y, \cdot)$"? What is the advantage in terms of time complexity when using this algorithm? This is crucial and should not be omitted since otherwise, as mentioned in Line 363, the runtime will scale with $|U|$. The authors should provide a more detailed explanation of how the maximization over the utility set is performed, especially given the potential for exponential scaling with the size of $U$. A concrete algorithm with pseudocode would be beneficial.
3. Perhaps out-of-scope, but it will be nice to see some connection between the existing theory for adversarial training with this setting: how do they generalize, and how do they fail to generalize? The lack of (can be light) theoretical discussions makes the discussion a bit unsatisfying.



### Questions
See Weaknesses. Additionally,
1. I found that Figure 1 is not very clear. Some explanations are needed for the meaning of (faded) arrows and such.
2. It's not entirely clear upon reading Section 4.2 how one will solve Eq. (5), or Eq. (4) given a strategic opponent with utility $u$. Without briefly stating the strategy, the results are reported and I think it would help to have some pointers to Section 5 saying that the results are obtained based on Section 5.1 (I suppose).
3. What does Line 360 mean exactly? More explanation is needed for how $\\hat{\\delta}_{y'}$ is defined.
4. Line 451, where the terms "well-specified" and "misspecified" are unclear in this context.

Some minor suggestions in writing:
1. Line 18, "incentive uncertainty set." instead of 'incentive uncertainty set'. Similarly, Line 82 'everything'. to "everything.", etc. 
2. Line 236, $u^{\\text{adv}}$ appears without a definition.
3. Line 266 and 267, it's unclear to me what $\\mathrm{test}(f_{\\text{train}})$ and $\\mathrm{clean}(f_{\\text{adv}})$ stand for without looking at the next paragraph.

>I would be happy to raise scores once these are answered and addressed.

### Soundness
3

### Presentation
2

### Contribution
3
