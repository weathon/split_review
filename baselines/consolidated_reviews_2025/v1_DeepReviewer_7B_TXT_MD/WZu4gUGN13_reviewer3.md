### Summary

This paper proposes a method to infer hidden physical properties of fluids from a single 3D video and simulate the observed fluid in novel scenes. The method consists of three stages: pretraining, inference, and transfer. The pretraining stage learns a probabilistic fluid simulator on particle datasets with various physical properties. The inference stage adapts the simulator to new scenes by estimating latent posteriors from visual inputs. The transfer stage fine-tunes the physical prior learner using the adapted latent variables to enable novel scene simulations. The method is evaluated on synthetic datasets and demonstrates strong performance in predicting future frames, simulating unseen geometries, and generalizing to heterogeneous fluids.

### Soundness

3 good

### Presentation

3 good

### Contribution

2 fair

### Strengths

1. The paper is well-written and easy to follow. The proposed method is clearly described and the experimental results are well-presented.
2. The method is novel and interesting. It proposes a new way to infer hidden physical properties of fluids from visual observations and simulate the observed fluid in novel scenes. The method is also flexible and can be applied to different types of fluids and scenes.
3. The paper provides extensive quantitative and qualitative results to demonstrate the effectiveness of the proposed method. The results show that the method can generalize to unseen geometries, boundary conditions, and fluid types.

### Weaknesses

#### Some Related Works


#### comment

1. The method is only evaluated on synthetic datasets. It is unclear how well the method would perform on real-world datasets. The synthetic data, while useful for initial validation, may not capture the complexities and noise present in real-world scenarios, such as varying lighting conditions, camera angles, and object occlusions. This raises concerns about the practical applicability of the method in real-world settings.
2. The method is only evaluated on a single type of fluid. It is unclear how well the method would perform on other types of fluids, such as air or water. The current evaluation does not explore the method's ability to handle fluids with different physical properties, such as viscosity, density, and surface tension. This limits the generalizability of the findings.
3. The method is only evaluated on a single type of fluid property. It is unclear how well the method would perform on other types of fluid properties, such as viscosity or density. The method's reliance on a single type of fluid property makes it difficult to assess its robustness and adaptability to different physical characteristics.
4. The method is only evaluated on a single type of fluid motion. It is unclear how well the method would perform on other types of fluid motion, such as turbulent flow or vortex shedding. The current evaluation does not consider the method's performance on more complex fluid dynamics, which are common in real-world scenarios.
5. The method is only evaluated on a single type of fluid simulation. It is unclear how well the method would perform on other types of fluid simulation, such as smoothed particle hydrodynamics (SPH) or lattice Boltzmann methods (LBM). The method's evaluation is limited to a single simulation technique, which does not provide a comprehensive assessment of its capabilities.

### Suggestions

The paper would benefit from a more thorough investigation into the method's performance on real-world datasets. The authors should consider evaluating their approach on publicly available datasets that include real-world fluid dynamics, such as those found in weather forecasting or oceanography. This would provide a more realistic assessment of the method's practical applicability. Furthermore, the evaluation should include a quantitative analysis of the method's performance under different real-world conditions, such as varying lighting, camera angles, and object occlusions. This would help to identify the limitations of the method and guide future research directions.

To address the limitations regarding fluid types, the authors should evaluate their method on a wider range of fluids, including air, water, and other Newtonian and non-Newtonian fluids. This would help to determine the method's generalizability across different physical properties. The evaluation should also consider the method's performance on fluids with varying viscosity, density, and surface tension. This would provide a more comprehensive understanding of the method's capabilities and limitations. Additionally, the authors should investigate the method's performance on fluids with complex interactions, such as multiphase flows or flows with solid obstacles.

Finally, the authors should extend their evaluation to include a broader range of fluid motions and simulation techniques. This would involve testing the method on more complex fluid dynamics, such as turbulent flow and vortex shedding. The authors should also evaluate the method's performance on different fluid simulation techniques, such as smoothed particle hydrodynamics (SPH) and lattice Boltzmann methods (LBM). This would provide a more comprehensive assessment of the method's capabilities and limitations. The evaluation should also consider the method's performance on different boundary conditions and initial conditions. This would help to identify the method's strengths and weaknesses and guide future research directions.

### Questions

Please refer to the weaknesses.

### Rating

5: marginally below the acceptance threshold

### Confidence

4: You are confident in your assessment, but not absolutely certain. It is unlikely, but not impossible, that you did not understand some parts of the submission or that you are unfamiliar with some pieces of related work.

**********
