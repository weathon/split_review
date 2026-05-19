### Summary

This paper presents a method for learning the hidden physical properties of fluids from a 3D video. The key idea is to use a probabilistic particle transition module to infer the hidden properties of the fluid. The method is evaluated on synthetic datasets and shows good results in predicting the future states of the fluid.

### Soundness

3 good

### Presentation

3 good

### Contribution

3 good

### Strengths

- The paper is well-written and easy to follow.
- The method is novel and interesting. It is the first work to use the hidden properties of the fluid to predict the future states of the fluid.
- The method is evaluated on synthetic datasets and shows good results.

### Weaknesses

#### Some Related Works


#### comment

 - The method is only evaluated on synthetic datasets. It is unclear how well the method would perform on real-world datasets.
- The method is only evaluated on a single type of fluid. It is unclear how well the method would perform on other types of fluids, such as air or water.
- The method is only evaluated on a single type of fluid property. It is unclear how well the method would perform on other types of fluid properties, such as viscosity or density.
- The method is only evaluated on a single type of fluid motion. It is unclear how well the method would perform on other types of fluid motion, such as turbulent flow or vortex shedding.
- The method is only evaluated on a single type of fluid simulation. It is unclear how well the method would perform on other types of fluid simulation, such as smoothed particle hydrodynamics (SPH) or lattice Boltzmann methods (LBM).

### Suggestions

The paper's primary limitation lies in the narrow scope of its experimental validation. While the results on synthetic datasets are promising, the lack of evaluation on real-world data raises significant concerns about the practical applicability of the proposed method. To address this, the authors should consider incorporating experiments on real-world fluid datasets, even if they are limited in scale. This could involve using publicly available datasets of fluid flows or capturing their own data using appropriate measurement techniques. Furthermore, the evaluation should be extended to include a variety of fluid properties and motion patterns. For example, the method should be tested on fluids with different viscosities, densities, and surface tensions, as well as on more complex fluid motions such as vortical flows and turbulent flows. This would provide a more comprehensive assessment of the method's robustness and generalizability.

Another area that requires further investigation is the method's performance on different fluid simulation techniques. The current evaluation is limited to a single type of simulation, which does not fully capture the diversity of fluid dynamics. To address this, the authors should explore the method's compatibility with other simulation techniques, such as smoothed particle hydrodynamics (SPH) and lattice Boltzmann methods (LBM). These methods have different numerical characteristics and may pose unique challenges for the proposed approach. For instance, SPH is a Lagrangian method that uses particles to represent the fluid, while LBM is a mesoscopic method that models fluid flow at a microscopic level. Evaluating the method on these different simulation techniques would provide a more complete understanding of its capabilities and limitations.

Finally, the paper should include a more detailed analysis of the method's sensitivity to various parameters and initial conditions. The current evaluation lacks a systematic study of how the method's performance varies with different parameter settings and initial fluid states. This is crucial for understanding the method's robustness and reliability. For example, the authors should investigate how the method's accuracy changes with different particle counts, time steps, and noise levels in the input data. This analysis would provide valuable insights into the method's limitations and help guide its practical application. Furthermore, a comparison with existing fluid simulation methods, including both data-driven and physics-based approaches, would be beneficial to contextualize the method's performance and highlight its unique advantages and disadvantages.

### Questions

- How well does the method perform on real-world datasets?
- How well does the method perform on other types of fluids?
- How well does the method perform on other types of fluid properties?
- How well does the method perform on other types of fluid motion?
- How well does the method perform on other types of fluid simulation?

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
