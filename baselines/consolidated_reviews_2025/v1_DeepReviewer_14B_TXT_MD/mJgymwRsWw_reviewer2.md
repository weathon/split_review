### Summary

The paper proposes a new method for active screening of molecules called Active Probabilistic Drug Discovery (APDD). It is based on an iterative process that involves probabilistic clustering, selective docking, and wet lab experiments. The method is evaluated on two datasets, DUD-E and LIT-PCBA, and a simulated virtual library. The results show that the method is effective in reducing the number of docking computations and wet lab experiments while maintaining high accuracy.

### Soundness

2 fair

### Presentation

2 fair

### Contribution

2 fair

### Strengths

The proposed method is a novel approach to active screening of molecules that combines probabilistic clustering, selective docking, and wet lab experiments. The method is evaluated on two datasets and a simulated virtual library, and the results show that it is effective in reducing the number of docking computations and wet lab experiments while maintaining high accuracy. The paper is well-written and easy to follow.

### Weaknesses

#### Some Related Works


#### comment

The paper has several limitations that should be addressed. First, the method is based on several assumptions, such as the assumption that active molecules are clustered in the chemical space and that the docking scores are reliable. These assumptions may not always hold true, and the paper should discuss the potential impact of these assumptions on the results. Second, the method is evaluated on only two datasets and a simulated virtual library. It would be useful to evaluate the method on a wider range of datasets and real-world scenarios to assess its generalizability. Third, the paper does not provide a detailed analysis of the computational cost of the method. It would be useful to compare the computational cost of the method with other methods to assess its efficiency. Finally, the paper does not provide a detailed analysis of the sensitivity of the method to the choice of parameters, such as the number of clusters and the threshold for docking scores. It would be useful to investigate the impact of these parameters on the results to assess the robustness of the method.

### Suggestions

The paper would benefit from a more thorough investigation into the impact of its core assumptions. Specifically, the assumption that active molecules are clustered in chemical space is a strong one, and while the authors mention this, they should provide a more detailed analysis of how violations of this assumption might affect the performance of their method. For example, they could explore scenarios where active molecules are distributed uniformly or in sparse regions of the chemical space, and quantify the resulting drop in performance. Furthermore, the reliance on docking scores as a primary filter needs more scrutiny. While docking is a common tool, its accuracy can vary significantly depending on the target protein and the chemical nature of the molecules. The authors should investigate the sensitivity of their method to the quality of docking scores, perhaps by introducing controlled levels of noise or error into the docking results and observing how this affects the overall performance of APDD. This would provide a more realistic assessment of the method's robustness in practical applications.

To address the limited evaluation, the authors should consider expanding their analysis to include more diverse datasets, encompassing a wider range of protein targets and chemical libraries. This would help to demonstrate the generalizability of the method beyond the specific datasets used in the current study. In addition to the DUD-E and LIT-PCBA datasets, there are other publicly available datasets that could be used for this purpose, such as the BindingDB or the ChemBL database. Furthermore, the use of a simulated virtual library is a good starting point, but it is important to validate the method on real-world virtual libraries, which may have different characteristics and biases. This would provide a more realistic assessment of the method's performance in practical drug discovery scenarios. The authors should also consider comparing their method to other state-of-the-art active learning methods for virtual screening, to better contextualize the performance of APDD.

Finally, a more detailed analysis of the computational cost and parameter sensitivity is needed. The authors should provide a clear breakdown of the computational time required for each step of the APDD method, including clustering, docking, and active learning. This would allow for a more direct comparison with other methods and would help to assess the scalability of the approach. Furthermore, the authors should conduct a more systematic investigation of the impact of the choice of parameters on the performance of the method. This could involve performing a grid search over the parameter space and analyzing the resulting performance curves. This would help to identify the optimal parameter settings for different datasets and would provide a better understanding of the robustness of the method to variations in parameter values. Specifically, the impact of the number of clusters on the final performance should be investigated more thoroughly, as this parameter can significantly affect the quality of the clustering and the subsequent selection of molecules for docking.

### Questions

How does the method perform when the assumptions are violated?
How does the method compare to other methods in terms of computational cost?
How sensitive is the method to the choice of parameters?

### Rating

3: reject, not good enough

### Confidence

5: You are absolutely certain about your assessment. You are very familiar with the related work and checked the math/other details carefully.

**********
