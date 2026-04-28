# FlowBench: A Robustness Benchmark for Optical Flow Estimation

- Decision: Reject
- Avg Score: 6.00
- Scores: 8, 8, 3, 5

## Abstract
Optical flow estimation is a crucial computer vision task often applied to safety-critical real-world scenarios like autonomous driving and medical imaging.
While optical flow estimation accuracy has greatly benefited from the emergence of deep learning, learning-based methods are also known for their lack of generalization and reliability.
However, reliability is paramount when optical flow methods are employed in the real world, where safety is essential.
Furthermore, a deeper understanding of the robustness and reliability of learning-based optical flow estimation methods is still lacking, hindering the research community from building methods safe for real-world deployment.
Thus we propose **FlowBench**, a robustness benchmark and evaluation tool for learning-based optical flow methods. 
**FlowBench** facilitates streamlined research into the reliability of optical flow methods by benchmarking their robustness to adversarial attacks and out-of-distribution samples.
With **FlowBench**, we benchmark 91 methods across 3 different datasets under 7 diverse adversarial attacks and 23 established common corruptions, making it the most comprehensive robustness analysis of optical flow methods to date.
Across this wide range of methods, we consistently find that methods with state-of-the-art performance on established standard benchmarks lack reliability and generalization ability.
Moreover, we find interesting correlations between the performance, reliability, and generalization ability of optical flow estimation methods, under various lenses such as design choices used, number of parameters, etc.
After acceptance, **FlowBench** will be open-source and publicly available, including the weights of all tested models.

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
5

### Summary
This paper proposes FLOWBENCH, a new benchmarking tool designed to evaluate optical flow prediction specifically in terms of reliability (robustness against adversarial attacks) and generalization ability (out-of-distribution performance). Three related metrics are proposed, namely TARM (Targeted Attack Reliability Measure), NARM (Non-targeted Attack Reliability Measure), and GAM (Generalization Ability Measure). An extensive study on 89 released models/checkpoints over four widely used datasets shows in-depth findings and insights.

### Strengths
1. This paper is among the first attempts to evaluate optical flow methods on reliability and generalization ability, which are both important but often overlooked in the research community.
2. The effort put into this research is huge. Building an open-source benchmark tool requires a large amount of coding and implementation. The results on all latest models are insightful and worth sharing.
3. The writing is overall in good quality.

### Weaknesses
1. The definition of TARM and NARM is not very clear in the text. Are they just defined as the EPE in different settings? The scales of these metrics shown in the figures are also a bit confusing, as EPEs up to the level of hundreds are weird. Maybe the authors should elaborate this more in the main body (not just in the appendix). Maybe it is also better to discuss the specific differences between targeted and non-targeted attacks in the context of optical flow estimation.
2. The benchmarked models are all DL-based models. Maybe it will be better to pick a few SotA traditional methods as a baseline? It is commonly believed that traditional methods are more interpretable and thus more robust, so it may be interesting to see how they compare on this benchmark.
3. One minor point that makes the proposed metrics less accessible and a bit unnatural is: for TARM, the higher the better, but for NARM and GAM, the lower the better. I would suggest aligning them into a uniform format by, for example, taking the inverse/reciprocal in the definition of TARM, so that it is also the lower the better. Also, the name "measure" does not imply that much as "score" (assuming the higher the better) or "error" (assuming the lower the better). Making these changes may make the metrics better understood and easy to use.

### Questions
1. Are there randomness in the evaluation of these metrics? As a benchmark metric, I would assume that it should be deterministic (I should get the same results no matter how many times I run the evaluation). It seems that there could be randomness, for example, when we add corruptions. If so, how large is the randomness and how would they affect the final evaluation results?

---
**Additional comments**:
1. Just a typo: Line 085 says the benchmark is based on 3 datasets, but Line 093 says 4 datasets.
2. Line 123: the citation "Russakovsky et al. (2015)" should use \citep instead of \citet.
3. Line 141: Maybe it will be better to find the authors of mmflow instead of citing "Contributors".
4. Line 166: the citation "Schmalfuss et al. (2022b)" should use \citep instead of \citet.

### Soundness
3

### Presentation
3

### Contribution
4

---

## Human Reviewer 2

### Rating
8

### Rating Number
8

### Confidence
4

### Summary
The paper proposes a FlowBenmark that benchmarks the robustness of 89 learning-based optical flow methods under different types of adversarial attacks and their generalization ability. The method also analyzes what factors can affect the robustness (e.g., the number of parameters, architecture components, etc). The paper promises to make the benchmark open source upon its acceptance. 

--- 
* Justification on the rating

   I support the acceptance of the paper unless any significant flaws are found during the reviewing period. It provides a comprehensive and insightful benchmark on the robustness of optical flow methods. The findings in the paper will benefit the community and help better design of optical flow method in the future. However, it will be great if the paper provides more in-depth technical analyses and answers the questions below for better clarity.

### Strengths
* Insightful benchmark

   The paper provides comprehensive analyses of existing learning-based optical flow methods on their robustness. In the optical flow literature, papers mostly have focused on their EPE accuracy only. This paper provides an interesting analysis that methods with the best accuracy are not necessarily the most robust methods. Given comprehensive analyses, readers can understand the pros and cons of each method. I believe the benchmark will certainly benefit the community and help design a better and more robust method for future work.

* Clarity 

   The paper is written clearly so that it's easy to follow and understand many graphs, metrics, and analyses in the paper.

### Weaknesses
 * Concern about fair comparison

   The checkpoints compared in the analyses might not be trained in the same setups, (e.g., data augmentation (photometric, random noise, etc), regularization, the usage of drop-out, etc), which can affect the robustness of the method. It would be ideal if all methods were trained in the same setup, but it's unrealistic and may not be possible. What does the paper think about the current comparison in the context that the methods are trained in different setups? Will it change any discussion that the paper made in the paper?

   Also, can the paper include or list brief details on training setups (e.g., data augmentation, type of regularization, etc.) of each method? Or discussing them as future work (e.g., each method is trained on different setups, but analyses didn't consider this axis yet) would be also fine.

* Less in-depth analyses

  Given the robustness measure, the paper discusses what method shows better generalization, accuracy, or robustness, but it's a bit lacking in what makes them better or more robust. There are analyses of the number of parameters or matching concepts (attention, CNN) at a high level, but it's a bit unclear what technical designs (e.g., architectural choices, domain knowledge, training strategies, etc.) really make these differences. Can the paper discuss more on the technical aspects?

### Questions
* Continuing on the question above, if we want to build an optical flow method that is both robust and accurate, what architectural design choices can we make by learning from this benchmark paper? Maybe this is the task of readers, but can the paper provide a brief discussion of any insights or findings while analyzing 89 methods? What can be the best architectural design choices for future models?

* nit
   * In Fig. 2, IRR shows the most reliable method, but the text says that RapidFlow is the most reliable one. There may be a mistake during making a graph or writing the text. 
   * In Fig. 1 right, generalization ability seems to improve when discarding one outlier on the right middle (i.e., one point at mid-2022 and GAM 80), when drawing the graph, does the paper discard a few extreme outliers or include all data points?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 3

### Rating
3

### Rating Number
3

### Confidence
4

### Summary
This paper introduces FlowBench, a novel benchmarking tool designed to evaluate the robustness of optical flow estimation methods, specifically their resistance to adversarial attacks and performance under out-of-distribution (OOD) conditions. As deep learning methods continue to improve accuracy in optical flow tasks, their vulnerability to adversarial perturbations and limitations in generalizing to OOD data remain concerns. FlowBench addresses this by providing a systematic and scalable evaluation across 89 models on three datasets and under seven types of adversarial attacks and 23 corruptions, making it one of the most comprehensive benchmarks for optical flow to date.

### Strengths
The work provides a wide-ranging benchmark covering multiple models, datasets, adversarial attacks, and common corruptions. This expansive scope allows researchers to evaluate optical flow models comprehensively. In addition, by focusing on robustness—vital for real-world applications like autonomous driving and medical imaging—it directly addresses the gap between research advancements and deployable technology, which is quite important.

### Weaknesses
A limitation of FlowBench lies in its evaluation scope, which, while robust, could benefit from a broader range of real-world data to fully capture the variability that optical flow models encounter in practical applications. The three datasets used provide valuable insights but may not represent the complete spectrum of challenges seen in diverse environments, such as varying lighting and extreme motion scenarios. 

Furthermore, the analysis correlating robustness with model parameter count, though insightful, stops short of examining deeper architectural factors, such as layer structure or feature extraction mechanisms, which may also significantly impact robustness. To make this analysis more actionable, the authors could explore specific architectural aspects, such as comparing various attention mechanisms (e.g., FlowFormer vs. FlowFormer++) or different convolutional architectures used in optical flow models. 

Lastly, the emphasis on adversarial robustness, while essential, could be complemented by additional real-world stressors to offer a more holistic view of model performance, moving beyond adversarial scenarios to include conditions that challenge models in everyday applications. For example, evaluating performance under specific conditions such as varying lighting, motion blur, or partial occlusions—common in real-world scenarios but not fully captured by the current corruption set—could help round out the analysis.

### Questions
Given that state-of-the-art models on i.i.d. benchmarks often underperform under adversarial attacks and corruptions, how might FlowBench be extended to offer predictive insights into robustness? Could specific patterns in initial evaluations serve as indicators of a model's robustness, potentially reducing the need for exhaustive testing and saving computational resources? For example, the authors could explore correlations between performance on specific corruption types and overall robustness, or investigate whether particular architectural features consistently predict stronger robustness across models. Developing such predictive indicators could reduce the need for exhaustive testing and conserve computational resources.

Additionally, the claim of comprehensiveness is somewhat compromised, as several concurrent models are omitted, including some with available code for KITTI and Sintel datasets.

### Soundness
2

### Presentation
2

### Contribution
2

---

## Human Reviewer 4

### Rating
5

### Rating Number
5

### Confidence
2

### Summary
This paper proposes a benchmark, FlowBench, to evaluate the robustness of current optical flow methods. FlowBench is built on KITTI-2015 and MPI-Sintel. It mainly focuses on the EPE metric and provides an easy-to-use API for attacking optical flow models. Besides, it includes the performance analysis.

### Strengths
Main Strength:
- Engineering: FlowBench provides an easy-to-use API for further study and analyzes the reliability/generalization of current methods.


Minor Strength:
- Novelty (in Optical Flow): To my best knowledge, the robustness of optical flow has not been discussed for a long time. It is good to have a benchmark of current methods.

### Weaknesses
Main Weakness:
- Lack of technical contribution: the whole benchmark is built on existing datasets. Besides, the attack techniques are from existing papers, not domain-specific. It is good to see some analysis of the performance. However, there is no solution provided to mitigate the issue. That makes me feel the paper is mainly engineering.


Minor Weakness:
- EPE is not the only metric in optical flow. The paper should analyze more on 1px-outlier rate, WAUC, etc.
- The writing is not clear. I find it hard to understand the main points in the paper. The analysis of different architectures is not convincing. For example, the paper classifies Flowformer as *Attention*, but it combines transformers with correlation. This makes me suspect the reliability of the analysis in Sec 5.3/5.4. Also, different methods may use different training data, which can be a factor that severely affects the robustness. (e.g. Flowformer++ uses more data than Flowformer. RAFT is trained from scratch, but Flowformer loads pre-trained weights). This makes the analyses feel messy. A better classification of methods should be provided.

### Questions
See weakness.

### Soundness
3

### Presentation
2

### Contribution
3
