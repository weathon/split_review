# In-N-Out: Robustness to In-Domain Noise and Out-of-Domain Generalization

- Decision: Reject
- Avg Score: 4.00
- Scores: 5, 5, 5, 1

## Abstract
Training on real-world data is challenging due to its complex nature, where data is often noisy and may require understanding diverse domains. Methods focused on Learning with Noisy Labels (LNL) may help with noise, but they often assume no domain shifts. In contrast, approaches for Domain Generalization (DG) could help with domain shifts, but these methods either consider label noise but prioritize out-of-domain (OOD) gains at the cost of in-domain (ID) performance, or they try to balance ID and OOD performance, but do not consider label noise at all. Thus, no work explores the combined challenge of balancing ID and OOD performance in the presence of label noise, limiting their impact. We refer to this challenging task as In-N-Out, and this work provides the first exploration of its unique properties.  We find that combining the settings explored in LNL and DG poses new challenges not present in either task alone, and thus, requires direct study. Our findings are based on a study comprised of three real-world datasets and one synthesized noise dataset, where we benchmark a dozen unique methods along with many combinations that are sampled from both the LNL and DG literature. We find that the best method for each setting varies, with older DG and LNL methods often beating the SOTA. A significant challenge we identified stems from unbalanced noise sources and domain-specific sensitivities, which makes using traditional LNL sample selection strategies that often perform well on LNL benchmarks a challenge. While we show this can be mitigated when domain labels are available, we find that LNL and DG regularization methods often perform better.

## Human Reviews

## Human Reviewer 1

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper does an empirical comparison of methods for domain generalization and for handling label noise, under a suite of vision domain generalization datasets that either contain label noise to begin with, or where label noise is added synthetically.

With a large scale comparison of methods for labels noise, domain generalization, and their combination, the authors report several findings. Among these findings are the statements that no single method constantly performs better than the others across all benchmarks, and that methods that handle label noise using sample selection tend to underperform when there is data from several domains.

### Strengths
The paper touches upon the combination of two important problems, label noise and domain generalization. It makes a very thorough empirical comparison, and the experiments seem well executed. The observation about selection methods for label noise being less effective with data from diverse domains seems interesting.

### Weaknesses
My main concern about the paper is that the main novelty is in setting up and running the large scale comparison. While some of the conclusions from the experiments are novel insights, I am not sure they are significant enough to warrant acceptance.
Some novelty either in terms of methods, or data selection algorithms, or experiments that sugges a way forward might have contributed to novelty.

Beyond the concern about novelty, I think there are a few other points worth mentioning.
* The choice of the name In-n-Out for the setting should be revised. There is an OOD-generalization method from an ICLR 2021 paper with the same name [1].
* One of the main findings is that no single method consistently outperformed others. The authors also state that this is surprising (line 531), however I do not understand why this is a surprise. In OOD-Generalization it is unclear whether there is one method that outperforms the other across all "natural" distribution shifts, and this is reflected in several works in the literature. For instance by [2] for spurious correlations benchmarks, or the WILDS dataset leaderboard for other benchmarks.
* Beyond not having a clear winner (which is reasonable and expectable), it is unclear what in the dataset makes one method more suitable for it than the other. Hence it is not really clear which of the empirical conclusions lead to practical advice for researchers and engineers. Besides the insight about the sample selection methods, the rest of the conclusions don't give a clue for when should one prefer ERM, one DG method or another, and one label noise method vs. the other.




### Questions
* The paper distinguishes Out-of-Domain methods and OOD Robustness methods. That categorization is unclear to me, what is the definition that discerns of these categories? For instance, why does Fishr or IRM belong into one category and not the other?
* Line 52 states that "some DG methods show implicit OOD-robustness under noise", referring to GroupDRO, Fishr and others. Does this statement rely on an empirical or theoretical observation? Where in the papers on these methods is this claim shown?
* Line 186 has a missing \ before "textit"

### Soundness
3

### Presentation
3

### Contribution
2

---

## Human Reviewer 2

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper studies the combination of Learning with Noisy Labels (LNL) and Domain Generalization (DG), introducing a task called In-N-Out that aims to simultaneously handle label noise and domain shifts. The authors evaluate various LNL and DG methods and their combinations on three real-world datasets and one synthetic dataset, providing empirical analysis of how these methods interact.

### Strengths
1. The paper provides a thorough empirical study comparing multiple methods and their combinations. The experimental analysis examines different aspects like multi-source impact on LNL methods, noise sensitivity of DG methods, and trade-offs between data cleanliness and domain balance. 

2. The authors provide some interesting observations through their experiments including method combinations sometimes performing worse than individual approaches. These observations, while not groundbreaking, provide useful insights.

### Weaknesses
1. I feel the fundamental contributions are limited. The paper combines two existing problems (LNL and DG) without proposing novel technical solutions. The framework is a straightforward combination of existing loss functions and methods. The core issue is that the paper doesn't introduce any new mechanisms for handling the interaction between label noise and domain shift. It simply applies existing methods for each problem independently and then combines them. This approach lacks novelty, as it doesn't address the specific challenges that arise when these two issues occur simultaneously. For example, the paper could have explored adaptive weighting schemes for loss functions that consider both noise and domain shift, or developed new regularization techniques that are specifically designed for this combined problem. The current approach feels like a baseline rather than a significant contribution.

2. Another major weakness is that the "task" being proposed seems artificial rather than motivated by real application needs. While real data may contain both noise and domain shifts, treating these as a single unified problem rather than addressing them separately needs stronger motivation. The paper doesn't clearly demonstrate why existing approaches of handling these issues separately is insufficient. The paper needs to provide a more compelling argument for why a unified approach is necessary. For instance, are there specific scenarios where addressing noise and domain shift independently leads to suboptimal results? The paper should include concrete examples or theoretical analysis that demonstrates the limitations of separate approaches and justifies the need for a combined framework. Without this, the proposed task appears to be an arbitrary combination of two existing problems.

### Questions
Please check the weakness

### Soundness
3

### Presentation
2

### Contribution
2

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
The paper proposes the In-N-Out task, which investigates the question of how to balance both in-distribution performance and out-of-distribution performance under the presence of label noise. Focusing on empirical analysis, the paper explores the possibility of combining loss functions/regularizers from learning with noisy labels (LNL) and domain generalization (DG), and demonstrates that (1) the performance of different combinations varies across datasets, and no single approach conclusively outperforms the rest, and (2) LNL approaches that are suitable for in-domain learning may not be suitable for out-of-domain generalization.

### Strengths
1. The paper aims to study a new task, In-N-Out, which focuses on the noise robustness for both in-domain and out-of-domain generalization, by examining which combination of different types of loss functions (such as LNL and DG losses) work the best.
2. The paper demonstrates that the ranking of different LNL algorithms can change when the empirical setup changes from one domain to multiple domains. 
3. In-depth study on how do ELR, MIRO, UNICON algorithms behave in out-of-distribution generalization settings are performed. In particular, it empirically shows that the sampling strategy of UNICON may skew the domain distribution, hurting the generalization.

### Weaknesses
1. The paper aims to study what combination of different types of loss functions (DG, LNL, etc.) improves both ID and OOD performance under label noise. Although there are many choices for each type of loss function, only MIRO/SWAD is chosen for the DG component, and ELR/UNICON is chosen for the LNL component, without sufficient justifications. If the goal of the paper is to benchmark a combination of the algorithms, there seems to be a lack of support since only a few candidates are studied.  Specifically, the choice of MIRO and SWAD for DG, and ELR and UNICON for LNL, lacks a clear rationale. There are numerous other established methods within each of these categories, and the paper does not adequately explain why these specific algorithms were selected over others. This limits the generalizability of the conclusions, as the performance of other combinations may differ significantly.
2. Figure 3 in Section 3.3.1 shows the experimental results of the ID performance with an increasing number of domains, but the discussion talks about OOD samples are hard for UNICON. Performances on OOD domains need to be compared to draw such a conclusion. The discussion focuses on the challenges UNICON faces with OOD samples, but the figure only presents in-domain (ID) performance. This discrepancy makes it difficult to validate the claims about UNICON's behavior on OOD data. A direct comparison of OOD performance is necessary to support the conclusions drawn in the discussion.
3. In Figure 4b, an insufficient number of baselines are compared (consider the LNL options and regularization/SAM in Equation 3). In addition, although SWAD exhibits better robustness to MIRO, they need to be not mutually-exclusive approaches, as they can be used together (shown in Table 1). The comparison in Figure 4b is limited, particularly given the variety of LNL methods and regularization techniques available. The figure does not explore the potential benefits of combining SWAD and MIRO, which are not mutually exclusive and could offer improved performance. The lack of baselines, such as other LNL methods and regularization techniques, makes it difficult to assess the robustness of the proposed approach.
4. The flow of the paper can be improved by better motivating the problem statement and organizing the research questions in the analysis sections. It is a bit difficult for the reader to identify the main points from the chunks of information. The paper lacks a clear and compelling motivation for the problem statement. The research questions in the analysis sections are not well-organized, making it hard for the reader to follow the main points. The analysis sections could benefit from a more structured approach, with clear motivations for each question and a logical flow of arguments.

### Questions
1. Across the four types of losses in Equation (3), which one is more important towards in-domain/out-of-domain generalization when there is label noise in the training set? What do the weights of the losses in Equation (3) look like after tuning the hyperparameters? Do they provide additional insights on which component is contributing the most to the performances?
2. Model/checkpoint selection is a very important part of domain generalization and hyperparameter tuning. What model selection strategy is used here? 
3. The experimental design is a bit confusing in Section 3.3.3. My interpretation is that the label noise rate is fixed across different sampling ratios (if it’s not fixed then the experiment is not a controlled study). It is surprising to see the in-distribution performance degrade drastically as the number of samples increases. The arguments about “maintaining balance” and “increased noise” in line 407 do not sound reasonable. How does the sampling ratio affect these two characteristics? Please provide more justifications. 
4. Minor typos: line 186 “textit”.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
1

### Rating Number
1

### Confidence
5

### Summary
This paper suggest to integrate noisy label problem and domain generalization problem together.

### Strengths
- This paper tried to integrate two well known problem setttings together since both problems should be managed together for real world settings.
- The authors may have studied previous researches thoroughly

### Weaknesses
 - What is the novelty of the method proposed in this paper? What is different from naively combining all objective function from each area?
- There is a previous study which adjusted SAM being adequate for Domain generalization setting [1] and it says their method suggests a sharpness aware optimization for DG. Then, why $\mathcal{R}_{SAM}$ should be used?
- Too many hyperparameters. How can I balance $\alpha$. $\beta$, $\lambda$ and $\gamma$?

### Questions
- What is domain for Clothing1M dataset? In previous researches, I didn't see pointing out the domain shift issue of Clothing1M dataset. Also, why the number of image for Clothing1M is 100,000?

### Soundness
2

### Presentation
3

### Contribution
1
