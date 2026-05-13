# Understanding Learning with Sliced-Wasserstein Requires Re-thinking Informative Slices

- Decision: Reject
- Scores: 8, 6, 5

## Abstract
The practical applications of Wasserstein distances (WDs) are constrained by their sample and computational complexities. Sliced-Wasserstein distances (SWDs) provide a workaround by projecting distributions onto one-dimensional subspaces, leveraging the more efficient, closed-form WDs for one-dimensional distributions. However, in high dimensions, most random projections become uninformative due to the concentration of measure phenomenon. Although several SWD variants have been proposed to focus on \textit{informative} slices, they often introduce additional complexity, numerical instability, and compromise desirable theoretical (metric) properties of SWD. Amidst the growing literature that focuses on directly modifying the slicing distribution, which often face challenges, we revisit the classic Sliced-Wasserstein and propose instead to rescale the 1D Wasserstein to make all slices equally informative. Importantly, we show that with an appropriate notion of \textit{slice informativeness}, rescaling for all individual slices simplifies to \textbf{a single global scaling factor} on the SWD. This, in turn, translates to the standard learning rate search for gradient-based learning in common ML workflows. We perform extensive experiments across various machine learning tasks showing that the classic SWD, when properly configured, can often match or surpass the performance of more complex variants. We then answer the following question: Is Sliced-Wasserstein all you need for common learning tasks?

## Human Reviews

## Human Reviewer 1

### Rating
8

### Rating Number
8

### Confidence
3

### Summary
This paper revisits the classic Sliced-Wasserstein Distance (SWD) and proposes a new approach to enhance its effectiveness. The authors introduce a rescaling approach based on the "informativeness" of each slice, which they define as the slice's alignment with the data's effective subspace. Instead of modifying the slicing distribution to identify informative slices, this approach uses a single global scaling factor, which simplifies SWD calculations and also allows it to perform comparably with other variants.
The paper provides theoretical backing for the rescaling approach, showing how it aligns with different dimensionality settings and retains SWD's metric properties.
The authors validate this method through experiments on tasks like gradient flow, color transfer, and deep generative modeling, showing that a properly scaled SWD can match or even outperform other methods without added complexity.

### Strengths
The paper offers a simpler and more computationally efficient approach to improving SWD by introducing a single global rescaling factor based on slice informativeness.

The rescaling approach can be absorbed into the learning rate tuning process, making it easy to implement without extensive adjustments to existing models.

It also reduces dependency on strict dimensionality assumptions, making SWD adaptable to more tasks without requiring the knowledge of the data's effective subspace dimension k.

The authors provide a solid theoretical foundation for their approach.

### Weaknesses
I'm not an expert in this area, so I'll leave the weaknesses section blank for now.

### Questions
Why the strict subspace condition can be relaxed given Assumption 4.1 provides a theoretical basis?

What other criteria could be used to define informativeness, and would they offer any additional benefits over alignment with the effective subspace?

### Soundness
3

### Presentation
3

### Contribution
3

---

## Human Reviewer 2

### Rating
6

### Rating Number
6

### Confidence
3

### Summary
This manuscript presents a novel solution of using sliced Wasserstein distance in general learning tasks. It has solid theoretical and empirical results to support their claim.

### Strengths
1. There are a lot of derivations in the manuscript, provides a strong theoretical background for the discuss topic.

2. The ideas of 1D Wasserstein distance is quite novel.

3. Detailed experiments were conducted on some of the learning tasks.

### Weaknesses
1. The experiment seems not sufficient to prove the claim "Sliced-Wasserstein is all you need for common learning tasks". Some common learning tasks like image classification and object detection is not tested.

2. Larger dataset for experiment is needed. Especially, toy datasets and MNIST images, which is a pretty small and easy learning task.

3. How SWD is used during the training is not very clear, a systematic model framework or a detailed algorithm might be helpful.

4. The compared methods in the experiment only has abbreviation with no explanation. 

5. How SWD is better is not clearly reflected in the experiments.

6. There are so many important things were discussed in the Appendix due to the page limit.

### Questions
1. What is the computational complexity for the proposed SWD?

2. What's the purpose of finding LR bound for SW Gradient Flow? How it impact the results for the mentioned learning tasks?

### Soundness
3

### Presentation
2

### Contribution
3

---

## Human Reviewer 3

### Rating
5

### Rating Number
5

### Confidence
4

### Summary
This paper proposes a simplified approach to the Sliced-Wasserstein Distance (SWD) by rescaling the Wasserstein distance for each one-dimensional slice, ensuring that all slices carry the same informativeness. This method demonstrates strong performance in tasks such as image generation and color transfer, rivaling or even surpassing more complex SWD variants. The core innovation lies in using a global scaling factor to balance the informativeness of different slices, thereby avoiding the complexity of directly modifying slice distributions. Overall, the idea is innovative, and the experimental results are convincing, showcasing the potential of the classic SWD with suitable parameter settings.

### Strengths
1. Innovation: The rescaling method proposed in this paper offers a new approach for high-dimensional SWD applications. By using a global scaling factor to address the issue of selecting informative slices, it effectively simplifies the complex process of slice selection.  
2. Theoretical support: Under the assumption of an effective subspace, this paper provides a theoretical derivation of the rescaling strategy, offering mathematical support that explains the rationale behind this method.  
3. Experimental performance: In various machine learning tasks, the rescaled SWD method performs excellently, demonstrating that the performance gap between classic SWD and its complex variants can be bridged through appropriate hyperparameter tuning.

### Weaknesses
1. Limitation of assumption: The theoretical analysis of this method relies on the assumption that data is distributed within a low-dimensional subspace. However, this assumption may not hold in certain high-dimensional data, particularly in datasets with complex or high-dimensional structures, such as text data or more intricate time series data, where the method's effectiveness remains unclear. Therefore, its applicability may be limited to datasets that satisfy this assumption.
2. Single metric of informativeness: The proposed global scaling factor only considers the informativeness of the slices in terms of their projection onto the effective subspace. However, different tasks may involve slices with more complex characteristics, and this single metric may not fully capture the contributions of all slices. Incorporating task-specific measures of informativeness could potentially enhance the method’s applicability and robustness.
3. Limited breadth of experimental validation: Although the paper validates the method’s effectiveness on multiple visual datasets, the types of experimental data are relatively narrow, lacking validation on other types of data, such as text or audio. Additionally, the paper does not deeply analyze performance on extremely high-dimensional data, which is a significant motivation behind designing SWD variants.
4. Limited generalization: The method performs well on classic machine learning tasks, but its applicability in more complex deep generative models, such as large-scale language models, remains unclear. Further research is needed to determine whether the method maintains its efficiency and stability on complex data distributions.
5. Sensitivity to hyperparameters in experiments: The proposed scaling method relies heavily on the choice of learning rate. Although the authors suggest that the learning rate can be adjusted as a hyperparameter, the specific impact on model convergence and adaptability lacks detailed analysis. Questions such as whether the results are limited to certain learning rate ranges and whether reliance on learning rate could lead to instability in practice require further exploration.

### Questions
This paper provides new insights into optimizing Sliced-Wasserstein Distance, with a simplified method that is theoretically appealing and performs well across several tasks. However, due to limitations in assumptions, narrow experimental validation, and sensitivity to hyperparameters, the applicability of this method may be constrained. To enhance the comprehensiveness and generalizability of the work, it is recommended to validate the method on more complex tasks and datasets and further refine the theoretical analysis.

Suggested improvements based on the Weaknesses section:
1. Strengthen discussion and validation of assumptions: Further discuss the practicality and limitations of the effective subspace assumption in real-world applications, or explore ways to expand the method’s applicability without this assumption.
2. Expand experiments to diverse data types: Validate the method on a wider range of datasets, such as text and audio data, to verify its broad applicability. Greater diversity in experiments would enhance the generalizability and persuasiveness of the results.
3. More in-depth hyperparameter sensitivity analysis: Further analyze the effect of learning rate on the method's convergence. Testing across different learning rate ranges could ensure the robustness and stability of the method and clarify if it requires strict hyperparameter tuning.
4. Explore more flexible informativeness metrics: To adapt to a wider range of tasks, consider expanding the definition of the global scaling factor to incorporate more detailed task-specific information or introduce an adaptive informativeness metric.

### Soundness
3

### Presentation
3

### Contribution
3
