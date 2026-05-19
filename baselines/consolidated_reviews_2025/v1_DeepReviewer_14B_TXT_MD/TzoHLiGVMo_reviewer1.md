### Summary

This paper proposes a transformer-based model (ODEFormer) for inferring symbolic forms of multidimensional ordinary differential equation (ODE) systems from a single observed solution trajectory. The authors train the model on synthetic data and test it on two datasets, outperforming existing methods in terms of accuracy and robustness to noise and irregular sampling. The paper claims contributions in the areas of dynamical symbolic regression and benchmarking.

### Soundness

2 fair

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The authors introduce a novel benchmark, odeBench, which is a curated collection of 63 ODEs ranging from one to four dimensions, providing a more comprehensive testing ground for SR models compared to existing datasets.

2. The authors show that the ODEFormer model consistently outperforms existing methods in terms of accuracy and robustness to noise and irregular sampling, while also achieving faster inference times.

### Weaknesses

#### Some Related Works


#### comment

1. The benchmark is only on low-dimensional systems, and the ODEFormer can only solve very simple ODEs. The paper acknowledges that it only considers first-order ODEs and that higher-order ODEs are not immediately addressed. The authors also admit that the model struggles with chaotic systems, which are crucial for assessing the model's ability to handle complex dynamics. The limited dimensionality and complexity of the ODEs tested raise concerns about the practical applicability of the method to real-world problems.

2. The authors did not compare with some of the latest work in the SR, such as $AI^{2}$ and DSR. The absence of comparisons with these recent methods limits the assessment of the proposed model's relative performance and its position within the current state-of-the-art in symbolic regression.

### Suggestions

The authors should consider expanding the benchmark to include more complex, high-dimensional ODE systems, and those exhibiting chaotic behavior. This would provide a more rigorous evaluation of the model's capabilities and limitations. Specifically, the inclusion of systems with known chaotic attractors, such as the Lorenz system or the Rössler system, would be valuable. Furthermore, the authors should explore methods for handling higher-order ODEs, as these are common in many scientific domains. This could involve reformulating higher-order ODEs as systems of first-order equations, or developing new techniques that can directly handle higher-order derivatives. The current limitation to first-order ODEs significantly restricts the applicability of the proposed method.

To address the lack of comparison with recent SR methods, the authors should include a thorough comparison with $AI^{2}$ and DSR. This comparison should not only focus on the accuracy of the inferred ODEs but also on other relevant metrics, such as the computational cost and the robustness to noise. The authors should also provide a detailed analysis of the strengths and weaknesses of each method, highlighting the specific scenarios where ODEFormer performs better or worse than the other methods. This would provide a more comprehensive understanding of the proposed method's capabilities and its position within the current landscape of SR techniques. The comparison should be performed on the same datasets to ensure a fair evaluation.

Finally, the authors should investigate the model's sensitivity to the initial conditions and the length of the observed trajectory. It is important to understand how these factors affect the model's ability to infer the correct ODE system. The authors should also explore the model's ability to generalize to unseen initial conditions and time spans. This could be done by evaluating the model's performance on trajectories that are significantly different from those used during training. A more thorough analysis of these aspects would provide a better understanding of the model's robustness and its potential for real-world applications.

### Questions

1. The ODEFormer is based on the large-scale training of a sequence-to-sequence transformer on synthetic data. How does the model perform when it encounters ODEs that are significantly different from the synthetic data it was trained on?

2. The paper mentions that the ODEFormer struggles with chaotic systems. How can the model be improved to better handle these types of systems, which are known for their sensitivity to initial conditions and unpredictable behavior?

3. The ODEFormer is currently limited to first-order ODEs. How can the model be extended to handle higher-order ODEs, which are common in many scientific and engineering domains?

### Rating

6: marginally above the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
